#!/usr/bin/env python3
"""Lê os gabaritos do caderno azul (dia 1 e dia 2) de um ano do Enem e grava as 5 provas em gabaritos.json. Uso: gab_enem.py ANO"""
import json, sys, re, pymupdf
ano = sys.argv[1]; g = json.load(open("gabaritos.json"))
L = lambda c: "ANULADA" if c.lower().startswith("anul") else c
t1 = pymupdf.open(f"fontes/enem-{ano}-dia1-azul-gabarito.pdf")[0].get_text().split()
import os; t2 = pymupdf.open(f"fontes/enem-{ano}-dia2-{os.environ.get('COR2', 'azul')}-gabarito.pdf")[0].get_text().split()
m = {}
for t in (t1, t2):
    for i in range(len(t) - 1):
        if t[i].isdigit() and 46 <= int(t[i]) <= 180 and re.fullmatch(r"[A-E]|[Aa]nulad[oa]", t[i + 1]): m[int(t[i])] = L(t[i + 1])
ing, esp = {}, {}
for i in range(len(t1) - 2):
    if t1[i].isdigit() and 1 <= int(t1[i]) <= 5 and re.fullmatch(r"[A-E]|[Aa]nulad[oa]", t1[i + 1]) and re.fullmatch(r"[A-E]|[Aa]nulad[oa]", t1[i + 2]) and int(t1[i]) not in ing:
        ing[int(t1[i])], esp[int(t1[i])] = L(t1[i + 1]), L(t1[i + 2])
com = {}
j = t1.index("ESPANHOL") if "ESPANHOL" in t1 else 0
for i in range(j, len(t1) - 1):
    if t1[i].isdigit() and 6 <= int(t1[i]) <= 45 and re.fullmatch(r"[A-E]|[Aa]nulad[oa]", t1[i + 1]): com.setdefault(int(t1[i]), L(t1[i + 1]))
assert len(ing) == 5 and len(com) == 40 and all(n in m for n in range(46, 181)), (len(ing), len(com), [n for n in range(46, 181) if n not in m])
mk = lambda d: {str(k): {"g": v, "comp": None} for k, v in d.items()}
g[f"enem-{ano}-humanas"] = mk({n - 45: m[n] for n in range(46, 91)})
g[f"enem-{ano}-natureza"] = mk({n - 90: m[n] for n in range(91, 136)})
g[f"enem-{ano}-matematica"] = mk({n - 135: m[n] for n in range(136, 181)})
g[f"enem-{ano}-linguagens-ingles"] = mk({**ing, **com})
g[f"enem-{ano}-linguagens-espanhol"] = mk({**esp, **com})
json.dump(g, open("gabaritos.json", "w"), ensure_ascii=False, indent=1)
an = [n for n in range(46, 181) if m[n] == "ANULADA"] + [f"{k}-ing" for k, v in ing.items() if v == "ANULADA"] + [f"{k}-esp" for k, v in esp.items() if v == "ANULADA"] + [k for k, v in com.items() if v == "ANULADA"]
print("ok", ano, "anuladas:", an)
