#!/usr/bin/env python3
"""Mostra o rascunho de uma prova, questão por questão. Uso: ver.py <id> [de] [até]"""
import json, sys, re
id_ = sys.argv[1]; a = int(sys.argv[2]) if len(sys.argv) > 2 else 1; b = int(sys.argv[3]) if len(sys.argv) > 3 else 99
d = json.load(open(f"/home/claude/extracao/{id_}/rascunho/rascunho.json"))
for q in d["questoes"]:
    if a <= q["numero"] <= b:
        print(f"=== Q{q['numero']} (pág. {q['pagina']}) figs={q['figs']}")
        print(re.sub(r"</p>", "</p>\n", q["enunciado"]))
        for k, v in q["alternativas"].items(): print(f"  ({k}) {v}")
