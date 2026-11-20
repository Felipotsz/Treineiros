#!/usr/bin/env python3
"""Gabaritos do caderno azul para os anos em que o 1º dia era Humanas (1–45) + Natureza (46–90)
e o 2º dia Linguagens (91–135, com 91–95 de inglês/espanhol) + Matemática (136–180). Uso: gab_enem_antigo.py ANO"""
import json, sys, re, pymupdf
ano = sys.argv[1]; g = json.load(open("gabaritos.json"))
L = lambda c: "ANULADA" if c.lower().startswith("anul") else c
ok = lambda c: re.fullmatch(r"[A-E]|[Aa]nulad[oa]", c)
t1 = pymupdf.open(f"fontes/enem-{ano}-dia1-azul-gabarito.pdf")[0].get_text().split()
t2 = pymupdf.open(f"fontes/enem-{ano}-dia2-azul-gabarito.pdf")[0].get_text().split()
m = {}
for i in range(len(t1) - 1):
    if t1[i].isdigit() and 1 <= int(t1[i]) <= 90 and ok(t1[i + 1]): m.setdefault(int(t1[i]), L(t1[i + 1]))
ing, esp, d2 = {}, {}, {}
for i in range(len(t2) - 2):
    if t2[i].isdigit() and 91 <= int(t2[i]) <= 95 and ok(t2[i + 1]) and ok(t2[i + 2]): ing[int(t2[i])], esp[int(t2[i])] = L(t2[i + 1]), L(t2[i + 2])
for i in range(len(t2) - 1):
    if t2[i].isdigit() and 96 <= int(t2[i]) <= 180 and ok(t2[i + 1]): d2.setdefault(int(t2[i]), L(t2[i + 1]))
assert all(n in m for n in range(1, 91)) and len(ing) == 5 and all(n in d2 for n in range(96, 181)), ([n for n in range(1, 91) if n not in m], ing, [n for n in range(96, 181) if n not in d2])
mk = lambda d: {str(k): {"g": v, "comp": None} for k, v in d.items()}
com = {n - 90: d2[n] for n in range(96, 136)}
g[f"enem-{ano}-humanas"] = mk({n: m[n] for n in range(1, 46)})
g[f"enem-{ano}-natureza"] = mk({n - 45: m[n] for n in range(46, 91)})
g[f"enem-{ano}-matematica"] = mk({n - 135: d2[n] for n in range(136, 181)})
g[f"enem-{ano}-linguagens-ingles"] = mk({**{n - 90: ing[n] for n in ing}, **com})
g[f"enem-{ano}-linguagens-espanhol"] = mk({**{n - 90: esp[n] for n in esp}, **com})
json.dump(g, open("gabaritos.json", "w"), ensure_ascii=False, indent=1)
print("ok", ano, "anuladas:", [n for n, v in {**m, **d2}.items() if v == "ANULADA"] + [f"{k}-ing" for k, v in ing.items() if v == "ANULADA"] + [f"{k}-esp" for k, v in esp.items() if v == "ANULADA"])
for k in ["humanas", "natureza", "matematica", "linguagens-ingles", "linguagens-espanhol"]:
    v = g[f"enem-{ano}-{k}"]; print(k, "".join(v[str(i)]["g"][0] for i in range(1, 46)))
