#!/usr/bin/env python3
"""Enem 2010: o PDF "Prova_Caderno_Azul_Gabarito" marca a resposta com um círculo verde em volta da letra.
Para cada círculo verde, pega o texto da linha à direita e acha a alternativa no rascunho (enem.json).
Uso: gab_enem2010.py  (lê enem-2010-dia{1,2}-azul) -> imprime {numero: letra} e as marcas não resolvidas."""
import json, re, sys, pymupdf
sys.path.insert(0, "tools")
from enem_decod import dict_decodificado
norm = lambda s: re.sub(r"\W+", "", s.lower())
res = {}
for dia in (1, 2):
    D = json.load(open(f"enem-2010-dia{dia}-azul/enem.json"))
    doc = pymupdf.open(f"fontes/enem-2010-dia{dia}-azul-prova.pdf")
    for pn in range(2, len(doc) + 1):
        pg = doc[pn - 1]
        verdes = [dr["rect"] for dr in pg.get_drawings() if dr.get("color") and dr["color"][1] > 0.5 and dr["color"][0] < 0.3 and dr["rect"].width < 25]
        if not verdes: continue
        linhas = []
        for b in dict_decodificado(pg)["blocks"]:
            for l in b.get("lines", []):
                linhas.append((pymupdf.Rect(l["bbox"]), "".join(s["text"] for s in l["spans"]).strip()))
        for v in verdes:
            cy = (v.y0 + v.y1) / 2
            cand = sorted([(r.x0, t) for r, t in linhas if abs((r.y0 + r.y1) / 2 - cy) < 5 and v.x1 - 3 < r.x0 < v.x1 + 25 and t], key=lambda x: x[0])
            txt = norm(cand[0][1])[:30] if cand else ""
            achou = [(n, L) for n, q in D.items() if abs(q["pag"] - pn) <= 1 for L, a in q["alternativas"].items() if txt and norm(a).startswith(txt)]
            achou = sorted(set(achou), key=lambda x: (abs(D[x[0]]["pag"] - pn)))
            if len(achou) >= 1 and len({a[0] for a in achou}) == 1:
                res[achou[0][0]] = achou[0][1]
            else:
                print("?", dia, pn, [round(x) for x in v], repr(cand[0][1][:40]) if cand else None, achou[:4])
print(json.dumps(res))
json.dump(res, open("/tmp/claude-0/gab2010.json", "w"))
