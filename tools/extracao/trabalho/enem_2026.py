"""Ajudantes do Enem 2026 (dia 1 caderno azul, dia 2 caderno amarelo).
- dict_limpo: texto sem os espaços falsos de kerning que o PDF de 2026 põe nas palavras em negrito.
- texto_longo: textos de apoio longos com linhas numeradas (ex.: Q46–50, Q9–13): parágrafos pela indentação, sem os números de linha.
- SEM_LINHA: tira as indicações "(l. N)" dos comandos e alternativas, porque o site não numera as linhas."""
import re, pathlib, pymupdf

RAIZ = pathlib.Path(__file__).resolve().parent
PDF1 = RAIZ / "fontes" / "enem-2026-dia1-azul-prova.pdf"
PDF2 = RAIZ / "fontes" / "enem-2026-dia2-amarelo-prova.pdf"
LIG = lambda s: s.replace("ﬁ", "fi").replace("ﬂ", "fl").replace("ﬀ", "ff").replace("ﬃ", "ffi")


def dict_limpo(pg):
    d = pg.get_text("rawdict")
    for b in d["blocks"]:
        for ln in b.get("lines", []):
            for sp in ln["spans"]:
                cs = sp.get("chars", [])
                sp["text"] = "".join(c["c"] for c in cs if not (c["c"] == " " and abs((c["bbox"][2] - c["bbox"][0]) - 0.2261 * sp["size"]) > 0.144 * sp["size"] / 10))
    return d


def _fmt(sp):
    t = sp["text"]
    if not t.strip(): return t
    f = sp["font"]; b = "Bold" in f or (sp["flags"] & 16); i = "Italic" in f or (sp["flags"] & 2)
    if b and i: return f"<strong><em>{t}</em></strong>"
    if b: return f"<strong>{t}</strong>"
    if i: return f"<em>{t}</em>"
    return t


def texto_longo(pdf, pag, y0, y1, x0=0, x1=9999, formatar=True):
    """Parágrafos de um texto corrido com linhas numeradas na margem. Nova linha mais recuada que a margem = novo parágrafo."""
    pg = pymupdf.open(pdf)[pag - 1]; d = dict_limpo(pg)
    linhas = []
    for b in d["blocks"]:
        if b["type"]: continue
        for ln in b["lines"]:
            bx = ln["bbox"]
            if not (y0 <= bx[1] and bx[3] <= y1 and x0 <= bx[0] and bx[2] <= x1): continue
            spans = [sp for sp in ln["spans"] if sp["text"].strip() and sp["size"] >= 4]      # sem a marca-d'água (1,5 pt)
            texto = [sp for sp in spans if not re.fullmatch(r"\d{1,2}", sp["text"].strip())]
            if not texto: continue                                                  # linha só com o número
            xt = texto[0]["bbox"][0]
            spans = [sp for sp in ln["spans"] if not (re.fullmatch(r"\s*\d{1,2}\s*", sp["text"]) and sp["bbox"][2] < xt - 2)]
            txt = "".join((_fmt(sp) if formatar else sp["text"]) for sp in spans)
            if not txt.strip(): continue
            linhas.append((round(bx[1], 1), xt, txt))
    linhas.sort()
    # junta spans da mesma linha visual (blocos diferentes na mesma altura)
    vis = []
    for y, x, t in linhas:
        if vis and abs(vis[-1][0] - y) < 2: vis[-1][2] += t if vis[-1][1] < x else ""; continue
        vis.append([y, x, t])
    margem = min(x for _, x, _ in vis)
    pars = []
    for y, x, t in vis:
        t = t.rstrip()
        if not pars or x > margem + 8: pars.append(t.strip()); continue
        s = pars[-1]
        if s.endswith("-") and t.lstrip()[:1].islower(): pars[-1] = s[:-1] + t.strip()
        else: pars[-1] = s + " " + t.strip()
    lim = lambda s: re.sub(r"</strong>\s*<strong>", " ", re.sub(r"</em><em>|</strong><strong>", "", re.sub(r"\s+", " ", LIG(s)))).strip()
    return [lim(p) for p in pars]


SEM_LINHA = lambda s: re.sub(r"\s*\((?:<em>)?l(?:</em>)?\.\s*[\d\-–, e]+\)", "", s)


def apoio(pars, titulo=None, fonte=None):
    h = (f'<p class="apoio"><strong>{titulo}</strong></p>' if titulo else "") + "".join(f'<p class="apoio">{x}</p>' for x in pars)
    return h + (f'<p class="fonte">{fonte}</p>' if fonte else "")
