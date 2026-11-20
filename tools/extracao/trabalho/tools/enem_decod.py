"""Decodifica PDFs do Enem (2021) cuja camada de texto sai embaralhada. As fontes embutidas (CFF) têm glifos
chamados /gN — o índice N segue a ordem padrão de glifos do TrueType (Arial): g68 = 'a', g109 = 'atilde'.
page.get_texttrace() dá, para cada caractere extraído, o número do glifo no CFF; o charset do CFF dá o nome.
mapas(pdf) -> {nome_da_fonte: {char_extraído: char_certo}}; traduz(txt, mapa)."""
import io, re
import pymupdf
from fontTools.cffLib import CFFFontSet
from fontTools.ttLib.standardGlyphOrder import standardGlyphOrder as SGO
from fontTools.agl import toUnicode

EXTRA = {"g4231": "ff", "g3032": ""}   # glifos /gN fora da ordem padrão, descobertos pelo contexto


def _nome2char(nome):
    g = re.fullmatch(r"g(\d+)", nome)
    if g:
        n = int(g.group(1))
        if nome in EXTRA: return EXTRA[nome]
        # O Arial do Windows não tem 2 glifos da ordem padrão do Mac: a partir de 172 desloca 1, a partir de 209 desloca 2
        n = n if n < 172 else n + 1 if n < 209 else n + 2
        if n < len(SGO): nome = SGO[n]
        else: return EXTRA.get(nome, "�")
    return toUnicode(nome) or EXTRA.get(nome, "�")


def _charset(doc, xref):
    try:
        _, ext, _, buf = doc.extract_font(xref)
        cff = CFFFontSet(); cff.decompile(io.BytesIO(buf), None)
        return cff[cff.fontNames[0]].charset
    except Exception:
        return None


def mapas(pdf):
    doc = pymupdf.open(pdf)
    cs, out = {}, {}
    for pg in doc:
        for xref, ext, _, nome, ref, _ in pg.get_fonts():
            base = nome.split("+")[-1]
            if base not in cs: cs[base] = _charset(doc, xref)
        for sp in pg.get_texttrace():
            base = sp["font"].split("+")[-1]
            ch = cs.get(base)
            if not ch: continue
            m = out.setdefault(base, {})
            for c in sp["chars"]:
                u, gid = chr(c[0]), c[1]
                if u not in m and 0 <= gid < len(ch):
                    nome = ch[gid]
                    if re.fullmatch(r"g\d+", nome) or toUnicode(nome):
                        m[u] = _nome2char(nome)
    return out


def traduz(txt, mapa):
    return "".join(mapa.get(ch, ch) for ch in txt)


if __name__ == "__main__":
    import sys
    m = mapas(sys.argv[1])
    for k, v in m.items():
        print(k, len(v), "".join(sorted(set(v.values())))[:120])
    if len(sys.argv) > 2:
        pg = pymupdf.open(sys.argv[1])[int(sys.argv[2]) - 1]
        for b in pg.get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                print("".join(traduz(s["text"], m.get(s["font"], {})) for s in l["spans"]))


_CS = {}


def dict_decodificado(pg):
    """Como pg.get_text('dict'), mas com o texto de cada span refeito glifo a glifo (pelo charset do CFF)."""
    doc = pg.parent
    for xref, ext, _, nome, ref, _ in pg.get_fonts():
        base = nome.split("+")[-1]
        if (id(doc), base) not in _CS: _CS[(id(doc), base)] = _charset(doc, xref)
    pos = {}
    for sp in pg.get_texttrace():
        ch = _CS.get((id(doc), sp["font"].split("+")[-1]))
        for c in sp["chars"]:
            if c[0] == 0xFFFD and c[1] > 0:        # Enem 2010: fonte CID Identity-H sem ToUnicode; o CID é o glifo do Arial
                novo = _nome2char(f"g{c[1]}")
            elif ch and 0 <= c[1] < len(ch):
                nome = ch[c[1]]
                novo = _nome2char(nome) if (re.fullmatch(r"g\d+", nome) or toUnicode(nome)) else chr(c[0])
            else:
                novo = chr(c[0])
            pos[(round(c[2][0], 1), round(c[2][1], 1))] = novo
    d = pg.get_text("rawdict")
    for b in d["blocks"]:
        for l in b.get("lines", []):
            for s in l["spans"]:
                s["text"] = "".join(pos.get((round(c["origin"][0], 1), round(c["origin"][1], 1)), c["c"]) for c in s["chars"])
    return d
