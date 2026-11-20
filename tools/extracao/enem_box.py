"""Caixa de recorte por busca de texto: box(pdf, pág, início, fim) -> [pág, x0, y0, x1, y1] na coluna do início."""
import pymupdf
_d = {}


def box(pdf, pag, ini, fim, folga=3, x0=None, x1=None):
    d = _d.setdefault(pdf, pymupdf.open(pdf)); pg = d[pag - 1]; W = pg.rect.width
    a = pg.search_for(ini)[0]
    bs = [r for r in pg.search_for(fim) if r.y0 >= a.y0 - 2]
    col = 0 if a.x0 < W / 2 - 5 else 1
    bs = [r for r in bs if (0 if r.x0 < W / 2 - 5 else 1) == col] or bs
    b = bs[0]
    cx0 = x0 if x0 is not None else (24 if col == 0 else W / 2 + 4)
    cx1 = x1 if x1 is not None else (W / 2 - 4 if col == 0 else W - 24)
    return [pag, round(cx0), round(a.y0 - folga), round(cx1), round(b.y1 + folga)]
