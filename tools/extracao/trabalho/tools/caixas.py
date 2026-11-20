#!/usr/bin/env python3
"""Lista retângulos de imagens e desenhos de uma página (coordenadas PDF) para montar recortes.json. Uso: caixas.py PROVA.pdf pág"""
import sys, pymupdf
d = pymupdf.open(sys.argv[1]); pg = d[int(sys.argv[2]) - 1]
print("página", pg.rect)
for i in pg.get_image_info():
    print("img", [round(x) for x in i["bbox"]])
rs = [dr["rect"] for dr in pg.get_drawings() if dr["rect"].width > 15 and dr["rect"].height > 15]
for r in rs: print("des", [round(r.x0), round(r.y0), round(r.x1), round(r.y1)])
