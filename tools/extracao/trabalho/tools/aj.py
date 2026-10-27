# Ajudantes para os arquivos ajustes.py: partem do enunciado do rascunho e devolvem o enunciado corrigido.
import json, re, pathlib

A = '</p><p class="apoio">'


def carregar(id_):
    d = json.load(open(pathlib.Path(__file__).resolve().parent.parent / id_ / "rascunho" / "rascunho.json"))
    return {q["numero"]: q for q in d["questoes"]}


def quebrar(html, frases):
    """Abre um parágrafo novo antes de cada frase; dentro de texto de apoio, o parágrafo novo também é de apoio."""
    for f in frases:
        i = html.find(" " + f)
        if i < 0: i = html.find(f)
        if i < 0: raise ValueError(f"frase não encontrada: {f[:40]!r}")
        abre = html.rfind("<p", 0, i)
        classe = re.match(r'<p( class="([^"]+)")?>', html[abre:])
        sep = "</p><p>" if not classe or not classe.group(2) else f'</p><p class="{classe.group(2)}">'
        html = html[:i] + sep + html[i:].lstrip()
    return html


def enun(R, n, quebras=(), trocas=(), chamada=None, figs=None, tirar_figs=True):
    """figs: {"p03-2": 1} troca o marcador do rascunho pela figura 1 da questão; os demais marcadores somem."""
    h = R[n]["enunciado"]
    for velho, novo in trocas:
        if velho not in h: raise ValueError(f"Q{n}: trecho não encontrado: {velho[:50]!r}")
        h = h.replace(velho, novo)
    for nome, k in (figs or {}).items():
        h = h.replace(f"[[FIG:{nome}]]", f"[[fig:{k}]]")
    if tirar_figs: h = re.sub(r"\[\[FIG:[^\]]+\]\]", "", h)
    # cabeçalho e número de página que vazaram para o texto
    h = re.sub(r"<p>(<strong>)?\s*(\d+\s*)?VESTIBULINHO[^<]*(<sup>[^<]*</sup>)?[^<]*(</strong>)?[^<]*</p>", "", h)
    h = re.sub(r"<p><strong>\d{1,2}</strong></p>", "", h)
    h = quebrar(h, quebras)
    if chamada: h = f'<p class="chamada">{chamada}</p>' + h
    return h


def tabela(cab, linhas):
    th = "".join(f'<th scope="col">{c}</th>' for c in cab)
    tb = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in l) + "</tr>" for l in linhas)
    return f'<div class="tabela-rola"><table><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table></div>'


def colunas(rotulos, linhas):
    """Alternativas em tabela (I, II, III) viram texto: "I: x; II: y; III: z"."""
    # ponto final da célula sai, para não ficar ".;" entre as colunas
    return {l: "; ".join(f"{r}: {v.rstrip().rstrip('.')}" for r, v in zip(rotulos, vals)) + "." for l, vals in zip("ABCDE", linhas)}


def completar(Q, R):
    """Questões sem enunciado próprio usam o do rascunho, sem os marcadores de figura soltos."""
    for n in R:
        Q.setdefault(n, {})
        if "enunciado" not in Q[n]: Q[n]["enunciado"] = enun(R, n)
    return Q


def trecho(id_, pag, inicio, fim, paragrafos=()):
    """Copia um trecho do texto extraído do PDF (<id>/texto.txt), da frase 'inicio' até a frase 'fim' (inclusive).
    Junta as linhas, mantém o hífen de palavras compostas partidas no fim da linha e abre parágrafo novo
    antes de cada frase de 'paragrafos'. Devolve a lista de parágrafos (para apoio(*...) ou p(*...))."""
    t = (pathlib.Path(__file__).resolve().parent.parent / id_ / "texto.txt").read_text(encoding="utf-8")
    sec = re.split(r"^===== (\d+)$", t, flags=re.M)
    pagina = dict(zip(sec[1::2], sec[2::2]))[str(pag)]
    pagina = re.sub(r"ﬂ ?", "fl", re.sub(r"ﬁ ?", "fi", pagina))
    junto = re.sub(r"-\s*\n\s*", "-", pagina)
    junto = re.sub(r"\s+", " ", junto)
    i = junto.find(inicio)
    if i < 0: raise ValueError(f"p{pag}: início não encontrado: {inicio[:40]!r}")
    j = junto.find(fim, i)
    if j < 0: raise ValueError(f"p{pag}: fim não encontrado: {fim[:40]!r}")
    s = junto[i:j + len(fim)].strip()
    marcas = sorted({s.find(f) for f in paragrafos})
    if -1 in marcas: raise ValueError(f"p{pag}: parágrafo não encontrado em {paragrafos}")
    cortes = [0] + [m for m in marcas if m > 0] + [len(s)]
    return [s[a:b].strip() for a, b in zip(cortes, cortes[1:])]
