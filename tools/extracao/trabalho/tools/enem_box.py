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


def box_decod(pdf, pag, ini, fim, folga=3, x0=None, x1=None):
    """Como box(), mas procura o texto na camada decodificada (Enem 2021, texto embaralhado)."""
    from enem_decod import dict_decodificado
    d = _d.setdefault(pdf, pymupdf.open(pdf)); pg = d[pag - 1]; W = pg.rect.width
    linhas = [("".join(s["text"] for s in l["spans"]), l["bbox"]) for b in dict_decodificado(pg)["blocks"] for l in b.get("lines", [])]
    a = next(bb for t, bb in linhas if ini in t)
    col = 0 if a[0] < W / 2 - 5 else 1
    b = next(bb for t, bb in linhas if fim in t and bb[1] >= a[1] - 2 and (0 if bb[0] < W / 2 - 5 else 1) == col)
    cx0 = x0 if x0 is not None else (24 if col == 0 else W / 2 + 4)
    cx1 = x1 if x1 is not None else (W / 2 - 4 if col == 0 else W - 24)
    return [pag, round(cx0), round(a[1] - folga), round(cx1), round(b[3] + folga)]
