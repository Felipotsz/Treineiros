#!/usr/bin/env python3
"""Recorta figuras de uma prova em PDF a partir de uma lista de retângulos (em pontos) e salva em WebP.
Uso: python3 tools/extracao/recortar.py PROVA.pdf recortes.json PASTA_SAIDA
recortes.json: {"q06": [4, 120, 40, 450, 300], ...}  → nome: [página, x0, y0, x1, y1]
Largura máxima 1100 px (boa no celular e no zoom); fundo branco; qualidade 82."""
import io, json, sys, pathlib, pymupdf
from PIL import Image
pdf, lista, saida = sys.argv[1], json.load(open(sys.argv[2])), pathlib.Path(sys.argv[3])
saida.mkdir(parents=True, exist_ok=True)
doc = pymupdf.open(pdf)
for nome, (pag, x0, y0, x1, y1) in lista.items():
    r = pymupdf.Rect(x0, y0, x1, y1)
    dpi = min(300, max(150, int(1100 / (r.width / 72))))         # figura pequena ganha mais resolução
    pix = doc[pag - 1].get_pixmap(clip=r, dpi=dpi)
    im = Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB")
    if im.width > 1100: im = im.resize((1100, round(im.height * 1100 / im.width)), Image.LANCZOS)
    im.save(saida / f"{nome}.webp", "WEBP", quality=82, method=6)
    print(f"{nome}.webp {im.width}x{im.height} {(saida / f'{nome}.webp').stat().st_size // 1024} KB")
