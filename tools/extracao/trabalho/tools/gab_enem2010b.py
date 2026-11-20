#!/usr/bin/env python3
"""Enem 2010: as letras das alternativas são círculos pretos desenhados; a resposta tem um círculo verde em volta
(no PDF original "Prova_Caderno_Azul_Gabarito"). Cada círculo pertence à última "Questão NN" acima dele na mesma coluna
(ou à última da coluna anterior). Dentro da questão, a ordem vertical dá a letra. Uso: gab_enem2010b.py"""
import json, re, sys, pymupdf
sys.path.insert(0, "tools")
from enem_decod import dict_decodificado
out, prob = {}, []
for dia in (1, 2):
    doc = pymupdf.open(f"fontes/enem-2010-dia{dia}-azul-gabmarcado.pdf")
    ultimo = None; vistos = set(); grupos = {}
    for pn in range(2, len(doc) + 1):
        pg = doc[pn - 1]; W = pg.rect.width; dr = pg.get_drawings()
        brancos = [d["rect"] for d in dr if d.get("fill") and min(d["fill"]) > 0.9 and d["rect"].width < 7 and d["rect"].height < 7]
        ms = [d["rect"] for d in dr if d.get("fill") and max(d["fill"]) < 0.3 and 5.5 < d["rect"].width < 8.5 and 5.5 < d["rect"].height < 8.5 and 60 < d["rect"].y0 < pg.rect.height - 30]
        ms = [m for m in ms if any(m.contains(pymupdf.Point((b.x0 + b.x1) / 2, (b.y0 + b.y1) / 2)) for b in brancos)]
        vs = [d["rect"] for d in dr if d.get("color") and d["color"][1] > 0.5 and d["color"][0] < 0.3 and d["rect"].width < 25]
        cab = []
        for b in dict_decodificado(pg)["blocks"]:
            for l in b.get("lines", []):
                t = "".join(s["text"] for s in l["spans"]).strip()
                m = re.match(r"^Questão\s+(\d+)", t)
                if m: cab.append((0 if l["bbox"][0] < W / 2 else 1, l["bbox"][1], int(m.group(1))))
        itens = [(0 if m.x0 < W / 2 else 1, m.y0, "m", m) for m in ms] + [(c, y, "q", n) for c, y, n in cab]
        itens.sort(key=lambda x: (x[0], x[1]))
        for col, y, tipo, v in itens:
            if tipo == "q":
                n = str(v)
                if n in vistos: n = n + "-es"
                vistos.add(n); ultimo = n; grupos[n] = []
            elif ultimo:
                verde = any(r.contains(pymupdf.Point((v.x0 + v.x1) / 2, (v.y0 + v.y1) / 2)) for r in vs)
                grupos[ultimo].append(verde)
    for n, g in grupos.items():
        if len(g) != 5 or sum(g) != 1: prob.append((dia, n, g)); continue
        out[n] = "ABCDE"[g.index(True)]
print("problemas:", prob); print(len(out))
json.dump(out, open("/tmp/claude-0/gab2010b.json", "w"))
