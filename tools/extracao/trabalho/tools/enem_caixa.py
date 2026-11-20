"""Caixa (em pontos) que cobre o texto de um trecho do PDF, da linha que contém 'ini' até a que contém 'fim', na mesma coluna.
Uso como módulo: caixa(pdf, pág, ini, fim) -> [pág, x0, y0, x1, y1]"""
import pymupdf, re
_docs = {}


def caixa(pdf, pag, ini, fim, folga=4):
    d = _docs.setdefault(pdf, pymupdf.open(pdf)); pg = d[pag - 1]
    linhas = []
    for b in pg.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            t = "".join(s["text"] for s in l["spans"])
            linhas.append((t, pymupdf.Rect(l["bbox"])))
    i0 = next(i for i, (t, r) in enumerate(linhas) if ini in t)
    col = 0 if linhas[i0][1].x0 < pg.rect.width / 2 - 5 else 1
    r0 = linhas[i0][1]
    i1 = next(i for i, (t, r) in enumerate(linhas) if fim in t and r.y0 >= r0.y0 - 1 and (0 if r.x0 < pg.rect.width / 2 - 5 else 1) == col)
    y0, y1 = r0.y0, linhas[i1][1].y1
    x0 = 30 if col == 0 else pg.rect.width / 2 - 2
    x1 = pg.rect.width / 2 + 2 if col == 0 else pg.rect.width - 30
    return [pag, round(x0), round(y0 - folga), round(x1), round(y1 + folga)]
