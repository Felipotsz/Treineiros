#!/usr/bin/env python3
"""Valida as provas em data/provas/*.json e, com --indexar, gera data/provas.json.

Uso (na raiz do projeto):
  python3 tools/validar.py                     # só valida
  python3 tools/validar.py --indexar           # valida, reescreve data/provas.json e atualiza o sw.js
  python3 tools/validar.py --aceitar-assuntos  # inclui em data/assuntos.json os assuntos novos encontrados
"""
import json, re, sys, pathlib, difflib, unicodedata, html as htmllib
from html.parser import HTMLParser

RAIZ = pathlib.Path(__file__).resolve().parent.parent
BANCAS = {"Enem", "ETEC", "FATEC"}
LETRAS = "ABCDE"
VOID = {"br", "img", "hr"}
ARQ_ASSUNTOS = RAIZ / "data" / "assuntos.json"


def ler_assuntos():
    if not ARQ_ASSUNTOS.exists(): return {}
    d = json.loads(ARQ_ASSUNTOS.read_text(encoding="utf-8"))
    return {m: list(v) for m, v in d.items() if not m.startswith("_")}


class Equilibrio(HTMLParser):
    """Confere se as tags HTML abrem e fecham direito."""
    def __init__(self):
        super().__init__(); self.pilha = []; self.problemas = []
    def handle_starttag(self, tag, attrs):
        if tag not in VOID: self.pilha.append(tag)
    def handle_endtag(self, tag):
        if tag in VOID: return
        if self.pilha and self.pilha[-1] == tag: self.pilha.pop()
        else: self.problemas.append(f"</{tag}> sem par")
    def fim(self):
        return self.problemas + [f"<{t}> não fechada" for t in self.pilha]


def checar_html(texto, onde, avisos):
    p = Equilibrio(); p.feed(texto); p.close()
    for problema in p.fim(): avisos.append(f"{onde}: HTML com problema ({problema})")


def texto_puro(h):
    return re.sub(r"\s+", " ", htmllib.unescape(re.sub(r"<[^>]+>|\[\[fig:\d+\]\]|\\[()\[\]]", " ", h or ""))).strip()


def normalizar(t):
    """Igual ao Render.normalizar do site: minúsculas e sem acentos."""
    return "".join(c for c in unicodedata.normalize("NFD", t.lower()) if unicodedata.category(c) != "Mn")


def rotulo(prova, q):
    o = q.get("origem") or {}
    return prova["titulo"] + (f", caderno {o['caderno']}" if o.get("caderno") else "") + f", questão {o.get('numeroOriginal') or q['numero']}"


def gerar_indices(provas, pasta=None):
    """Índices leves para o celular: o site só baixa a prova inteira quando ela é aberta.
    indice-questoes.json: matéria/assunto de cada questão (treino, estatísticas, caderno de erros)
    busca.json: palavras de cada questão, sem acento e sem repetição (busca por texto)."""
    indice, busca = [], []
    for p in provas:
        for q in p["questoes"]:
            item = {"p": p["id"], "n": q["numero"], "m": q["materia"], "a": q.get("assunto", "")}
            if q.get("gabarito") == "ANULADA": item["x"] = 1
            if q.get("tags"): item["t"] = q["tags"]
            indice.append(item)
            proprio = re.sub(r'<p class="(chamada|fonte)">.*?</p>', " ", q["enunciado"])
            trecho = texto_puro(proprio)
            todas = " ".join([texto_puro(q["enunciado"])] + [texto_puro(v) for v in q["alternativas"].values()] + [q["materia"], q.get("assunto", ""), p["titulo"]])
            palavras = list(dict.fromkeys(w for w in re.findall(r"[0-9a-z]+", normalizar(todas)) if len(w) > 1))
            busca.append({"p": p["id"], "n": q["numero"], "r": rotulo(p, q), "b": p["banca"], "m": q["materia"], "a": q.get("assunto", ""),
                          "e": (trecho[:200] + "…") if len(trecho) > 200 else trecho, "w": " ".join(palavras)})
    d = pasta or (RAIZ / "data")
    (d / "indice-questoes.json").write_text(json.dumps(indice, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    (d / "busca.json").write_text(json.dumps(busca, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    print(f"índices: {len(indice)} questões ({(d / 'indice-questoes.json').stat().st_size // 1024} KB), busca ({(d / 'busca.json').stat().st_size // 1024} KB)")


def checar_edicoes(ids_provas):
    """data/edicoes.json lista todas as edições (inclusive sem prova). Confere com os arquivos de prova."""
    arq = RAIZ / "data" / "edicoes.json"
    if not arq.exists(): return []
    erros = []
    eds = json.loads(arq.read_text(encoding="utf-8"))["edicoes"]
    ids_ed = {e["id"] for e in eds}
    for i in ids_provas:
        if i not in ids_ed and not i.startswith("enem"): erros.append(f"edicoes.json: a prova '{i}' não está na lista de edições")
    for e in eds:
        if e["id"] in ids_provas and e.get("status") in ("sem-prova",): erros.append(f"edicoes.json: '{e['id']}' tem arquivo de prova, mas está marcada como sem prova")
    return erros


def checar_assunto(q, onde, assuntos, avisos, novos):
    """Assunto fora da lista oficial: avisa e sugere o nome parecido que já existe."""
    m, a = q.get("materia"), q.get("assunto")
    if not a: return
    if a in assuntos.get(m, []): return
    if not assuntos:                                   # lista ainda vazia: só registra (para --aceitar-assuntos)
        novos.setdefault(m, set()).add(a); return
    todos = sorted({x for v in assuntos.values() for x in v})
    parecido = difflib.get_close_matches(a, todos, n=1, cutoff=0.6)
    dica = f" — quis dizer '{parecido[0]}'?" if parecido else " (novo? confira e rode --aceitar-assuntos)"
    avisos.append(f"{onde}: assunto '{a}' fora da lista de {m}{dica}")
    novos.setdefault(m, set()).add(a)


def validar_prova(caminho, assuntos=None, novos=None):
    erros, avisos = [], []
    assuntos = assuntos or {}; novos = novos if novos is not None else {}
    try:
        d = json.loads(caminho.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return None, [f"JSON inválido: {e}"], []
    for campo in ("id", "banca", "ano", "titulo", "fonte", "duracaoMinutos", "questoes"):
        if campo not in d: erros.append(f"falta o campo '{campo}'")
    if erros: return d, erros, avisos
    if d["id"] != caminho.stem: erros.append(f"id '{d['id']}' deve ser igual ao nome do arquivo '{caminho.stem}'")
    if not re.fullmatch(r"[a-z0-9-]+", d["id"]): erros.append("id deve ter só letras minúsculas sem acento, números e hífen (ex.: enem-2023-dia1-azul)")
    if "linkProva" in d and not str(d["linkProva"]).startswith("https://"): erros.append("linkProva deve ser um endereço https:// do caderno oficial (PDF)")
    # ETEC e FATEC: semestre e data do exame (o Enem é anual)
    if d.get("banca") in ("ETEC", "FATEC"):
        if d.get("semestre") not in (1, 2): erros.append("semestre deve ser 1 ou 2 (semestre de ingresso, como no nome oficial: 1SEM26)")
    if "dataExame" in d and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(d["dataExame"])): erros.append("dataExame deve estar no formato AAAA-MM-DD")
    if "pdf" in d and not (RAIZ / d["pdf"]).exists(): erros.append(f"pdf '{d['pdf']}' não encontrado")
    if "apresentacao" in d: checar_html(d["apresentacao"], "apresentação", avisos)
    if d["banca"] not in BANCAS: erros.append(f"banca '{d['banca']}' inválida (use {', '.join(sorted(BANCAS))})")
    if not isinstance(d["ano"], int): erros.append("ano deve ser número inteiro")
    if not isinstance(d["duracaoMinutos"], int) or d["duracaoMinutos"] <= 0: erros.append("duracaoMinutos deve ser inteiro positivo")
    if not d["questoes"]: erros.append("a prova não tem questões")
    vistos = set()
    for q in d["questoes"]:
        n = q.get("numero"); onde = f"questão {n}"
        if not isinstance(n, int): erros.append(f"questão sem número inteiro: {q.get('enunciado', '')[:30]}"); continue
        if n in vistos: erros.append(f"{onde}: número repetido")
        vistos.add(n)
        for campo in ("materia", "enunciado", "alternativas", "gabarito"):
            if not q.get(campo): erros.append(f"{onde}: falta '{campo}'")
        alts = q.get("alternativas") or {}
        letras = sorted(alts)
        if len(letras) < 4 or letras != list(LETRAS[:len(letras)]):
            erros.append(f"{onde}: alternativas devem ser A, B, C, D (e E), sem pular letras")
        if q.get("gabarito") not in list(alts) + ["ANULADA"]:
            erros.append(f"{onde}: gabarito '{q.get('gabarito')}' não existe nas alternativas")
        imgs = q.get("imagens", [])
        for k, img in enumerate(imgs):
            src = img if isinstance(img, str) else (img or {}).get("src", "")
            if not src or not (RAIZ / src).exists(): erros.append(f"{onde}: imagem '{src}' não encontrada")
            if isinstance(img, str) or not (img or {}).get("alt"): avisos.append(f"{onde}: figura {k + 1} sem descrição (alt) para leitor de tela")
        textos = [q.get("enunciado", ""), q.get("explicacao", "")] + list(alts.values())
        for m in re.findall(r"\[\[fig:(\d+)\]\]", " ".join(str(t) for t in textos)):
            if not 1 <= int(m) <= len(imgs): erros.append(f"{onde}: marcador [[fig:{m}]] sem figura correspondente")
        if q.get("gabarito") == "ANULADA":
            an = q.get("anulacao") or {}
            if not an.get("motivo"): avisos.append(f"{onde}: anulada sem justificativa (anulacao.motivo)")
            elif an.get("fonte") not in ("oficial", "analise"): erros.append(f"{onde}: anulacao.fonte deve ser 'oficial' ou 'analise'")
            else: checar_html(an["motivo"], f"{onde} (anulação)", avisos)
        if "tags" in q and not (isinstance(q["tags"], list) and all(isinstance(t, str) for t in q["tags"])): erros.append(f"{onde}: tags deve ser uma lista de textos")
        if "retificada" in q and not isinstance(q["retificada"], bool): erros.append(f"{onde}: retificada deve ser true ou false")
        junto = " ".join(str(t) for t in textos)
        if junto.count("\\(") != junto.count("\\)") or junto.count("\\[") != junto.count("\\]"):
            erros.append(f"{onde}: fórmula com delimitador sem par (\\( \\) ou \\[ \\])")
        if "[ILEGÍVEL]" in junto: erros.append(f"{onde}: contém [ILEGÍVEL]")
        if not q.get("explicacao"): avisos.append(f"{onde}: sem explicação")
        elif "REVISAR" in q["explicacao"]: avisos.append(f"{onde}: explicação marcada REVISAR")
        if not q.get("assunto"): avisos.append(f"{onde}: sem 'assunto'")
        else: checar_assunto(q, onde, assuntos, avisos, novos)
        # campos opcionais com dados do Inep (microdados): estatística de acerto e parâmetros da TRI
        est = q.get("estatistica")
        if est is not None and not (isinstance(est, dict) and isinstance(est.get("pctAcerto"), (int, float)) and 0 <= est["pctAcerto"] <= 100):
            erros.append(f"{onde}: 'estatistica' deve ser {{\"pctAcerto\": 0 a 100}}")
        tri = q.get("tri")
        if tri is not None and not (isinstance(tri, dict) and all(isinstance(tri.get(k), (int, float)) for k in ("a", "b", "c"))):
            erros.append(f"{onde}: 'tri' deve ter os números a, b e c")
        if d["banca"] != "Enem" and tri is not None: avisos.append(f"{onde}: 'tri' só é usado no Enem")
        for i, t in enumerate(textos):
            checar_html(str(t), f"{onde} ({'enunciado' if i == 0 else 'explicação' if i == 1 else 'alternativa'})", avisos)
    return d, erros, avisos


def main():
    indexar = "--indexar" in sys.argv
    aceitar = "--aceitar-assuntos" in sys.argv
    assuntos, novos = ler_assuntos(), {}
    arquivos = sorted((RAIZ / "data" / "provas").glob("*.json"))
    if not arquivos:
        print("Nenhuma prova em data/provas/."); return 1
    total_erros, indice = 0, []
    for arq in arquivos:
        d, erros, avisos = validar_prova(arq, assuntos, novos)
        marca = "ERRO" if erros else ("aviso" if avisos else "ok")
        print(f"[{marca}] {arq.name}" + (f" ({len(d['questoes'])} questões)" if d and not erros else ""))
        for e in erros: print(f"    erro:  {e}")
        for a in avisos[:15]: print(f"    aviso: {a}")
        if len(avisos) > 15: print(f"    ... e mais {len(avisos) - 15} avisos")
        total_erros += len(erros)
        if not erros:
            qs = d["questoes"]
            indice.append({
                "id": d["id"], "banca": d["banca"], "titulo": d["titulo"], "ano": d["ano"],
                **({"semestre": d["semestre"]} if d.get("semestre") else {}), **({"dataExame": d["dataExame"]} if d.get("dataExame") else {}),
                "anuladas": sum(1 for q in qs if q.get("gabarito") == "ANULADA"),
                "duracaoMinutos": d["duracaoMinutos"], "totalQuestoes": len(qs),
                "arquivo": f"data/provas/{arq.name}",
                "materias": sorted({q["materia"] for q in qs}),
                "assuntos": sorted({q["assunto"] for q in qs if q.get("assunto")}),
                "temTri": d["banca"] == "Enem" and all(q.get("tri") for q in qs if q.get("gabarito") != "ANULADA"),
                "revisadas": sum(1 for q in qs if q.get("explicacaoRevisada")),
            })
    # trechos para preencher antes de publicar (página Apoie)
    for pag in sorted(RAIZ.glob("*.html")):
        n = len(re.findall(r'class="[^"]*\bpreencher\b', pag.read_text(encoding="utf-8")))
        if n: print(f"[aviso] {pag.name}: {n} trecho(s) marcados com class=\"preencher\" ainda sem os seus dados.")
    erros_ed = checar_edicoes({p["id"] for p in indice})
    for e in erros_ed: print("    erro: ", e)
    total_erros += len(erros_ed)
    print(f"\n{len(arquivos)} arquivo(s), {total_erros} erro(s).")
    if aceitar and novos:
        bruto = json.loads(ARQ_ASSUNTOS.read_text(encoding="utf-8")) if ARQ_ASSUNTOS.exists() else {}
        for m, v in novos.items(): bruto[m] = sorted(set(bruto.get(m, [])) | v)
        ARQ_ASSUNTOS.write_text(json.dumps(bruto, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"data/assuntos.json: {sum(len(v) for v in novos.values())} assunto(s) incluído(s).")
    if total_erros: return 1
    if indexar:
        indice.sort(key=lambda p: (-p["ano"], p["banca"], p["id"]))
        (RAIZ / "data" / "provas.json").write_text(json.dumps(indice, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"data/provas.json atualizado com {len(indice)} prova(s).")
        gerar_indices([json.loads((RAIZ / p["arquivo"]).read_text(encoding="utf-8")) for p in indice])
        import gerar_paginas, gerar_sw
        gerar_paginas.main()          # páginas estáticas por questão + sitemap (para buscadores)
        gerar_sw.main()
    return 0


if __name__ == "__main__":
    sys.exit(main())
