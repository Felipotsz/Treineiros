#!/usr/bin/env python3
"""Monta o JSON final de uma prova a partir do rascunho (rascunho.py), do gabarito oficial e de um arquivo
de ajustes escrito na conferência humana (texto corrigido, figuras com descrição, matéria, assunto, explicação).

Uso:
  python3 tools/extracao/montar.py AJUSTES.py RASCUNHO.json GABARITOS.json PASTA_FIGURAS
O arquivo AJUSTES.py define:
  META = {"id", "banca", "ano", "semestre", "titulo", "fonte", "dataExame", "duracaoMinutos", ...}
  Q = { numero: {
        "materia", "assunto", "tags": [...],
        "enunciado": "<p>...</p>"            (opcional: substitui o do rascunho)
        "trocar": [("antigo", "novo"), ...]   (opcional: correções pontuais no enunciado do rascunho)
        "alternativas": {"A": "..."}          (opcional: substitui as alternativas indicadas)
        "imagens": [{"arquivo": "q06", "alt": "..."}]   (figuras recortadas por recortar.py)
        "explicacao": "<p>...</p>", "anulacao": {...}, "retificada": True,
        "apoio_de": (32, "<p>pergunta da 32</p>")   (opcional: usa o texto de apoio da questão 32, sem a pergunta dela)
  } }
  EXTRAS = {"apresentacao": "descrição"}   (opcional: figuras da prova fora das questões, ex.: ilustração de abertura)
Saída: data/provas/<id>.json e assets/img/<id>/*.webp (dentro do projeto).
O gabarito vem SEMPRE do gabarito oficial; explicacaoRevisada sai sempre false.
"""
import importlib.util, json, pathlib, re, shutil, sys

RAIZ = pathlib.Path(__file__).resolve().parents[2]


def carregar_ajustes(caminho):
    spec = importlib.util.spec_from_file_location("ajustes", caminho)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod


def limpar(html):
    """Padroniza o HTML vindo do rascunho."""
    # faixa "Leia o texto para responder às questões..." vira chamada (destaque discreto)
    html = re.sub(r"<p>\s*<strong>\s*((?:Leia|Observe|Analise)[^<]*?)\s*</strong>\s*</p>", r'<p class="chamada">\1</p>', html)
    html = html.replace("‹HIFEN›", "-").replace("\u200b", "")
    html = re.sub(r"ﬂ ?", "fl", html); html = re.sub(r"ﬁ ?", "fi", html)          # ligaduras do PDF (“ﬂ ores”)
    html = re.sub(r"ﬂ ?", "fl", html); html = re.sub(r"ﬁ ?", "fi", html)          # ligaduras do PDF (“ﬂ ores”)
    html = re.sub(r"(?<=\S) {2,}(?=\S)", " ", html)                      # espaços duplos do PDF
    html = re.sub(r"(\w)- (se|nos|lo|la|los|las|me|te|lhe|lhes|o|a|os|as)\b", r"\1-\2", html)   # “libertando- se” (quebra de linha no PDF)
    html = re.sub(r"\s+</p>", "</p>", html)
    html = re.sub(r"<p>\s+", "<p>", html)
    return html.strip()


def main():
    aj = carregar_ajustes(sys.argv[1])
    rasc = {q["numero"]: q for q in json.load(open(sys.argv[2]))["questoes"]}
    meta = aj.META
    gab = json.load(open(sys.argv[3]))[meta["id"]]
    figs = pathlib.Path(sys.argv[4])
    destino_img = RAIZ / "assets" / "img" / meta["id"]
    if destino_img.exists(): shutil.rmtree(destino_img)
    destino_img.mkdir(parents=True)

    questoes, problemas, finais, imagens_de = [], [], {}, {}
    total = len(gab)
    for nome, alt in getattr(aj, "EXTRAS", {}).items():          # figuras fora das questões
        shutil.copy(figs / f"{nome}.webp", destino_img / f"{nome}.webp")
        meta.setdefault("imagensProva", {})[nome] = {"src": f"assets/img/{meta['id']}/{nome}.webp", "alt": alt}
    for n in range(1, total + 1):
        r, a = rasc.get(n), aj.Q.get(n, {})
        herdadas = []
        if r is None and "enunciado" not in a: problemas.append(f"questão {n}: não está no rascunho nem nos ajustes"); continue
        enun = a.get("enunciado") or r["enunciado"]
        for velho, novo in a.get("trocar", []):
            if velho not in enun: problemas.append(f"questão {n}: trecho para trocar não encontrado: {velho[:50]!r}")
            enun = enun.replace(velho, novo)
        if a.get("apoio_de"):                                         # texto de apoio compartilhado com outra questão
            fonte_n, pergunta = a["apoio_de"]
            base = finais[fonte_n]
            if pergunta not in base: problemas.append(f"questão {n}: pergunta da questão {fonte_n} não encontrada para separar o apoio")
            enun = base.replace(pergunta, "") + enun
            if "[[fig:" in base.replace(pergunta, ""):               # o apoio tem figura: ela vem junto, e as da questão andam o índice
                # só as figuras do apoio (as da pergunta da outra questão ficam de fora)
                marcas = re.findall(r"\[\[fig:(\d+)\]\]", base.replace(pergunta, ""))
                herdadas = imagens_de[fonte_n][:max(int(k) for k in marcas)] if marcas else []
        enun = limpar(enun)
        finais[n] = enun
        alts = dict(r["alternativas"]) if r else {}
        alts.update(a.get("alternativas", {}))
        for letra, (velho, novo) in a.get("trocar_alt", []):
            if velho not in alts[letra]: problemas.append(f"questão {n} ({letra}): trecho não encontrado: {velho[:40]!r}")
            alts[letra] = alts[letra].replace(velho, novo)
        alts = {k: limpar(v) for k, v in sorted(alts.items())}
        if re.search(r"\[\[FIG:", enun + " ".join(alts.values())): problemas.append(f"questão {n}: ainda tem marcador de figura do rascunho")
        if "‹CONFERIR›" in enun + " ".join(alts.values()): problemas.append(f"questão {n}: tem ‹CONFERIR›")
        imagens = list(herdadas)
        for im in a.get("imagens", []):
            orig = figs / f"{im['arquivo']}.webp"
            shutil.copy(orig, destino_img / orig.name)
            item = {"src": f"assets/img/{meta['id']}/{orig.name}", "alt": im["alt"]}
            if im.get("legenda"): item["legenda"] = im["legenda"]
            imagens.append(item)
        imagens_de[n] = imagens
        g = gab[str(n)]
        q = {"numero": n, "materia": a.get("materia", ""), "assunto": a.get("assunto", ""),
             "origem": {"numeroOriginal": n}, "enunciado": enun, "imagens": imagens, "alternativas": alts,
             "gabarito": g["g"], "explicacao": a.get("explicacao", ""), "explicacaoRevisada": False}
        if a.get("tags"): q["tags"] = a["tags"]
        if g["g"] == "ANULADA":
            if not a.get("anulacao"): problemas.append(f"questão {n}: anulada sem justificativa")
            else: q["anulacao"] = a["anulacao"]
        if a.get("retificada"): q["retificada"] = True
        if not q["materia"]: problemas.append(f"questão {n}: sem matéria")
        if not q["explicacao"]: problemas.append(f"questão {n}: sem explicação")
        questoes.append(q)

    prova = dict(meta); prova["questoes"] = questoes
    saida = RAIZ / "data" / "provas" / f"{meta['id']}.json"
    saida.write_text(json.dumps(prova, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{saida.relative_to(RAIZ)}: {len(questoes)} questões, {sum(len(q['imagens']) for q in questoes)} figuras")
    for p in problemas: print("  PROBLEMA:", p)
    return 1 if problemas else 0


if __name__ == "__main__":
    sys.exit(main())
