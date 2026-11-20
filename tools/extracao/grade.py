#!/usr/bin/env python3
"""Renderiza páginas de um PDF com uma grade de coordenadas (em pontos), para escolher recortes de figura.
Uso: python3 tools/extracao/grade.py PROVA.pdf PASTA 4 7 11   (números das páginas)"""
import sys, pathlib, pymupdf
from PIL import Image, ImageDraw
pdf, pasta, pags = sys.argv[1], pathlib.Path(sys.argv[2]), [int(x) for x in sys.argv[3:]]
pasta.mkdir(parents=True, exist_ok=True)
doc = pymupdf.open(pdf)
ESC = 1.6                                     # pixels por ponto
for n in pags:
    pg = doc[n - 1]
    pix = pg.get_pixmap(matrix=pymupdf.Matrix(ESC, ESC))
    im = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    d = ImageDraw.Draw(im)
    for v in range(0, int(pg.rect.width) + 1, 25):
        d.line([(v * ESC, 0), (v * ESC, im.height)], fill=(255, 0, 0) if v % 100 == 0 else (255, 190, 190), width=1)
        if v % 50 == 0: d.text((v * ESC + 2, 2), str(v), fill=(200, 0, 0))
    for h in range(0, int(pg.rect.height) + 1, 25):
        d.line([(0, h * ESC), (im.width, h * ESC)], fill=(0, 0, 255) if h % 100 == 0 else (190, 190, 255), width=1)
        if h % 50 == 0: d.text((2, h * ESC + 2), str(h), fill=(0, 0, 200))
    im.save(pasta / f"grade-p{n:02d}.png")
print("ok")
