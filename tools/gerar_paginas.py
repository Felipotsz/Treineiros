#!/usr/bin/env python3
"""Gera uma página HTML estática por questão (q/<prova>/<número>.html), o sitemap.xml e o robots.txt.

Para que serve: o Google não executa bem sites que montam tudo com JavaScript a partir de JSON.
Com uma página "pronta" por questão, quem buscar "Enem 2023 questão 136 porcentagem" pode cair direto no Treineiros.

Roda sozinho em "python3 tools/validar.py --indexar". Também dá para rodar direto:
  python3 tools/gerar_paginas.py
O endereço do site vem da linha og:url do index.html (troque SEU-USUARIO antes de publicar).
"""
import html, json, pathlib, re, shutil

RAIZ = pathlib.Path(__file__).resolve().parent.parent
PASTA = RAIZ / "q"
PAGINAS_FIXAS = ["", "provas.html", "busca.html", "estudo.html", "redacao.html", "vestibulares.html", "etec.html", "fatec.html", "enem.html", "apoie.html", "fontes.html"]


def site():
    m = re.search(r'<meta property="og:url" content="([^"]+)"', (RAIZ / "index.html").read_text(encoding="utf-8"))
    url = m.group(1) if m else "https://SEU-USUARIO.github.io/treineiros/"
    return url if url.endswith("/") else url + "/"


def texto(h):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", h or ""))).strip()


def imagens(q):
    """Mesma regra do js/render.js: texto simples ou objeto {src, alt, legenda}."""
    out = []
    for i, im in enumerate(q.get("imagens", [])):
        if isinstance(im, str): im = {"src": im}
        out.append({"src": im["src"], "alt": im.get("alt") or f"Figura {i + 1} da questão {q['numero']}", "legenda": im.get("legenda", "")})
    return out


def figura(im):
    e = html.escape
    return (f'<figure class="fig"><img class="figura" src="{e(im["src"])}" alt="{e(im["alt"])}" loading="lazy">'
            + (f"<figcaption>{im['legenda']}</figcaption>" if im["legenda"] else "") + "</figure>")


def com_figuras(texto, lista, usadas):
    def troca(m):
        k = int(m.group(1)) - 1
        if k >= len(lista): return ""
        usadas.add(k); return figura(lista[k])
    return re.sub(r"\[\[fig:(\d+)\]\]", troca, texto or "")


def anulacao(q):
    if q["gabarito"] != "ANULADA": return ""
    a = q.get("anulacao") or {}
    origem = "Justificativa oficial da banca" if a.get("fonte") == "oficial" else "Análise do Treineiros (a banca não divulgou o motivo)"
    return ('<div class="anulada" role="note"><p class="anulada__titulo">Questão anulada pela banca</p><p>Ela vale ponto para todos os candidatos, qualquer que seja a resposta.</p>'
            + (f'<p class="anulada__origem">{origem}</p>{a["motivo"]}' if a.get("motivo") else "") + "</div>")


def rotulo(prova, q):
    o = q.get("origem") or {}
    return prova["titulo"] + (f", caderno {o['caderno']}" if o.get("caderno") else "") + f", questão {o.get('numeroOriginal') or q['numero']}"


def pagina(prova, q, ant, prox, base_url):
    e = html.escape
    rot = rotulo(prova, q)
    desc = texto(re.sub(r'\[\[fig:\d+\]\]|<p class="(chamada|fonte)">.*?</p>', " ", q["enunciado"]))[:155]
    url = f"{base_url}q/{prova['id']}/{q['numero']}.html"
    ex = q.get("explicacao") or "Sem explicação cadastrada."
    expl = (ex if ex.lstrip().startswith("<p") else f"<p>{ex}</p>") + (
        '<p class="legenda">Gabarito retificado: a banca corrigiu a resposta desta questão depois da primeira divulgação.</p>' if q.get("retificada") else "")
    lista, usadas = imagens(q), set()
    enun = com_figuras(q["enunciado"], lista, usadas)
    alts = "".join(f'<li><span class="alt__letra">{l}</span><span>{com_figuras(v, lista, usadas)}</span></li>' for l, v in q["alternativas"].items())
    imgs = "".join(figura(im) for k, im in enumerate(lista) if k not in usadas)
    resp = "questão anulada pela banca (vale ponto para todos)" if q["gabarito"] == "ANULADA" else f'{q["gabarito"]}) {com_figuras(q["alternativas"][q["gabarito"]], lista, set())}'
    est = f'<p class="legenda">No Enem, {str(q["estatistica"]["pctAcerto"]).replace(".", ",")}% dos candidatos acertaram esta questão (microdados do Inep).</p>' if q.get("estatistica") else ""
    nav = "".join([
        f'<a class="btn" href="q/{prova["id"]}/{ant["numero"]}.html">Questão anterior</a>' if ant else "",
        f'<a class="btn" href="q/{prova["id"]}/{prox["numero"]}.html">Próxima questão</a>' if prox else ""])
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<base href="../../">
<title>{e(rot)}: {e(q["materia"])}{(", " + e(q["assunto"])) if q.get("assunto") else ""} | Treineiros</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{e(url)}">
<meta property="og:title" content="{e(rot)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{e(url)}"><meta property="og:image" content="{e(base_url)}assets/og.png">
<meta name="theme-color" content="#1E1813">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="css/variables.css"><link rel="stylesheet" href="css/base.css"><link rel="stylesheet" href="css/components.css"><link rel="stylesheet" href="css/simulado.css">
<script src="js/theme.js"></script>
</head>
<body>
<main id="conteudo">
<article class="questao">
<h1>{e(rot)}</h1>
<p><span class="tag">{e(q["materia"])}</span>{f' <span class="tag">{e(q["assunto"])}</span>' if q.get("assunto") else ""}</p>
<div class="enunciado">{enun}</div>{imgs}
<ol class="alts-lista">{alts}</ol>
<p><a class="btn btn--primary" href="questao.html?id={prova["id"]}&amp;n={q["numero"]}">Responder e ver se acertei</a></p>
<details class="revisao"><summary>Ver resposta e explicação</summary>
<p><strong>Resposta:</strong> {resp}</p>{anulacao(q)}{est}
<div class="explicacao"><span class="explicacao__rotulo">Correção comentada</span>{expl}
<p><span class="tag">{"Explicação revisada" if q.get("explicacaoRevisada") else "Explicação ainda não revisada"}</span></p></div>
</details>
<div class="nav">{nav}<a class="btn" href="simulado.html?id={prova["id"]}">Fazer a prova inteira</a></div>
<p class="origem">Fonte: {e(prova["fonte"])}{(", exame de " + "/".join(reversed(prova["dataExame"].split("-")))) if prova.get("dataExame") else ""}. Questão reproduzida para fins de estudo.</p>
</article>
</main>
<script src="js/config.js"></script><script src="js/storage.js"></script><script src="js/formulas.js"></script><script src="js/logo.js"></script><script src="js/layout.js"></script>
<script>Formulas.renderizar(document.querySelector(".questao"));</script>
</body>
</html>
"""


def main():
    base_url = site()
    if PASTA.exists(): shutil.rmtree(PASTA)            # recria do zero (questões removidas somem)
    urls = [base_url + p for p in PAGINAS_FIXAS]
    total = 0
    for arq in sorted((RAIZ / "data" / "provas").glob("*.json")):
        prova = json.loads(arq.read_text(encoding="utf-8"))
        qs = prova["questoes"]
        (PASTA / prova["id"]).mkdir(parents=True, exist_ok=True)
        for i, q in enumerate(qs):
            (PASTA / prova["id"] / f"{q['numero']}.html").write_text(
                pagina(prova, q, qs[i - 1] if i else None, qs[i + 1] if i + 1 < len(qs) else None, base_url), encoding="utf-8")
            urls.append(f"{base_url}q/{prova['id']}/{q['numero']}.html")
            total += 1
    (RAIZ / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
        "".join(f"  <url><loc>{html.escape(u)}</loc></url>\n" for u in urls) + "</urlset>\n", encoding="utf-8")
    (RAIZ / "robots.txt").write_text(f"User-agent: *\nDisallow: /revisar.html\nDisallow: /importar.html\nSitemap: {base_url}sitemap.xml\n", encoding="utf-8")
    print(f"{total} página(s) de questão em q/ e sitemap.xml com {len(urls)} endereço(s).")
    if "SEU-USUARIO" in base_url: print("aviso: troque SEU-USUARIO no og:url do index.html antes de publicar (o sitemap usa esse endereço).")


if __name__ == "__main__":
    main()
