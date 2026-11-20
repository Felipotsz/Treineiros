#!/usr/bin/env python3
"""Importa dados oficiais do Inep (microdados do Enem) para uma prova do Treineiros.

Preenche em cada questão, quando possível:
  "tri":         {"a": ..., "b": ..., "c": ...}   parâmetros da TRI  → estimativa de nota no resultado
  "estatistica": {"pctAcerto": 37.4}              % dos candidatos que acertaram
E confere o gabarito do JSON contra o gabarito do Inep (avisa se divergir).

Onde baixar: gov.br/inep > Dados abertos > Microdados > Enem. No ZIP do ano:
  DADOS/ITENS_PROVA_<ano>.csv     (pequeno: parâmetros e gabarito de cada item)
  DADOS/MICRODADOS_ENEM_<ano>.csv (grande, vários GB: respostas de cada participante; opcional)

Uso (na raiz do projeto):
  1) Descobrir o código do caderno (CO_PROVA) de cada área e cor:
       python3 tools/importar_microdados.py --itens ITENS_PROVA_2023.csv --listar
  2) Importar:
       python3 tools/importar_microdados.py --itens ITENS_PROVA_2023.csv --prova data/provas/enem-2023-dia2-azul.json \\
           --co-prova MT=1211 --co-prova CN=1191 [--microdados MICRODADOS_ENEM_2023.csv]
     (as siglas são as do Inep: LC, CH, CN, MT. Use os códigos do caderno da mesma cor do JSON.)
  3) python3 tools/validar.py --indexar

Como as questões são ligadas: pela área (Linguagens→LC, Ciências Humanas→CH, Ciências da Natureza→CN, Matemática→MT)
e por origem.numeroOriginal (= CO_POSICAO do Inep). Nas questões de língua estrangeira (Linguagens 1 a 5),
informe no JSON origem.lingua = "ingles" ou "espanhol"; sem isso, elas ficam sem dados.
"""
import argparse, csv, json, pathlib, sys

AREAS = {"Linguagens": "LC", "Ciências Humanas": "CH", "Ciências da Natureza": "CN", "Matemática": "MT"}
LINGUA = {"ingles": "0", "espanhol": "1"}           # TP_LINGUA nos microdados
csv.field_size_limit(10_000_000)


def abrir(caminho):
    """Os CSVs do Inep usam ';' e, conforme o ano, UTF-8 ou Latin-1."""
    bruto = pathlib.Path(caminho).open("rb").read(4096)
    try: bruto.decode("utf-8"); enc = "utf-8-sig"
    except UnicodeDecodeError: enc = "latin-1"
    return csv.DictReader(open(caminho, encoding=enc, newline=""), delimiter=";")


def numero(v):
    try: return float(str(v).replace(",", "."))
    except (TypeError, ValueError): return None


def listar(itens):
    vistos = {}
    for r in abrir(itens):
        k = (r["CO_PROVA"], r["SG_AREA"], r.get("TX_COR", ""))
        vistos[k] = vistos.get(k, 0) + 1
    print("CO_PROVA  ÁREA  COR (itens)")
    for (co, area, cor), n in sorted(vistos.items(), key=lambda x: (x[0][1], x[0][2], x[0][0])):
        print(f"{co:>8}  {area:<4}  {cor} ({n})")
    print("\nDica: há vários cadernos da mesma cor (aplicação regular, reaplicação, adaptados). Use o da aplicação regular.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--itens", required=True); ap.add_argument("--prova"); ap.add_argument("--microdados")
    ap.add_argument("--co-prova", action="append", default=[], help="ÁREA=CÓDIGO, ex.: MT=1211 (pode repetir)")
    ap.add_argument("--listar", action="store_true")
    a = ap.parse_args()
    if a.listar: return listar(a.itens) or 0
    if not a.prova or not a.co_prova: ap.error("informe --prova e ao menos um --co-prova (ou use --listar)")
    cos = dict(x.split("=", 1) for x in a.co_prova)

    # 1) Parâmetros e gabarito oficial de cada item: (área, posição, língua) -> linha
    itens = {}
    for r in abrir(a.itens):
        area = r["SG_AREA"]
        if cos.get(area) != r["CO_PROVA"]: continue
        lingua = r.get("TP_LINGUA", "") if area == "LC" else ""
        itens[(area, int(r["CO_POSICAO"]), lingua if lingua not in ("", "nan") else "")] = r
    if not itens: print("Nenhum item encontrado com esses CO_PROVA. Rode com --listar."); return 1

    arq = pathlib.Path(a.prova); prova = json.loads(arq.read_text(encoding="utf-8"))
    ligadas, avisos = {}, []
    for q in prova["questoes"]:
        area = AREAS.get(q["materia"]); o = q.get("origem") or {}
        pos = o.get("numeroOriginal")
        if not area or area not in cos or not pos: continue
        r = itens.get((area, pos, LINGUA.get(o.get("lingua", ""), ""))) or itens.get((area, pos, ""))
        if r is None:
            avisos.append(f"questão {q['numero']} (nº {pos}): sem item correspondente" + (" — falta origem.lingua?" if area == "LC" and pos <= 5 else ""))
            continue
        ligadas[q["numero"]] = (q, r, area)
        gab = (r.get("TX_GABARITO") or "").strip()
        if r.get("IN_ITEM_ABAN") == "1" and q["gabarito"] != "ANULADA":
            avisos.append(f"questão {q['numero']}: o Inep marca o item como abandonado/anulado, mas o JSON tem gabarito {q['gabarito']}")
        elif gab and q["gabarito"] not in ("ANULADA", gab):
            avisos.append(f"questão {q['numero']}: GABARITO DIFERENTE — JSON {q['gabarito']}, Inep {gab}")
        pa, pb, pc = numero(r.get("NU_PARAM_A")), numero(r.get("NU_PARAM_B")), numero(r.get("NU_PARAM_C"))
        if None not in (pa, pb, pc): q["tri"] = {"a": round(pa, 5), "b": round(pb, 5), "c": round(pc, 5)}

    # 2) % de acerto, lendo os microdados linha a linha (o arquivo é enorme)
    if a.microdados:
        alvo = {}                                    # área -> {posição relativa: [acertos, total]}
        primeiro = {area: min(p for (ar, p, _) in itens if ar == area) for area in {k[0] for k in itens}}
        for num, (q, r, area) in ligadas.items():
            alvo.setdefault(area, {})[num] = [0, 0]
        lidos = 0
        for linha in abrir(a.microdados):
            lidos += 1
            if lidos % 500000 == 0: print(f"  {lidos:,} participantes lidos…", file=sys.stderr)
            for area, qs in alvo.items():
                if linha.get(f"CO_PROVA_{area}") != cos[area]: continue
                resp = linha.get(f"TX_RESPOSTAS_{area}") or ""
                lingua = linha.get("TP_LINGUA", "")
                for num, cont in qs.items():
                    q, r, _ = ligadas[num]
                    pos = int(r["CO_POSICAO"]); gab = (r.get("TX_GABARITO") or "").strip()
                    # LC: as questões 1 a 5 existem em inglês e em espanhol; conta só quem escolheu aquela língua.
                    # ATENÇÃO: confira no dicionário dos microdados do ano como TX_RESPOSTAS_LC organiza essas posições.
                    if area == "LC" and pos <= 5 and r.get("TP_LINGUA", "") != lingua: continue
                    i = pos - primeiro[area]
                    if i < len(resp) and resp[i] not in ("", "*", "."):
                        cont[1] += 1
                        if resp[i] == gab: cont[0] += 1
        for qs in alvo.values():
            for num, (ac, tot) in qs.items():
                if tot >= 100: ligadas[num][0]["estatistica"] = {"pctAcerto": round(ac / tot * 100, 1)}
        print(f"{lidos:,} participantes lidos.")

    arq.write_text(json.dumps(prova, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    com_tri = sum(1 for q in prova["questoes"] if q.get("tri"))
    com_est = sum(1 for q in prova["questoes"] if q.get("estatistica"))
    print(f"{arq.name}: {len(ligadas)} questões ligadas aos itens do Inep; {com_tri} com parâmetros TRI; {com_est} com % de acerto.")
    for x in avisos: print("aviso:", x)
    print("Agora rode: python3 tools/validar.py --indexar")
    return 0


if __name__ == "__main__":
    sys.exit(main())
