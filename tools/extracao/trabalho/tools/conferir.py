#!/usr/bin/env python3
"""Confere a prova montada: gabarito oficial, figuras, marcadores, explicações. Uso: conferir.py <id>"""
import json, sys, re, pathlib
id_ = sys.argv[1]; P = pathlib.Path("/home/claude/proj/treineiros")
p = json.load(open(P / f"data/provas/{id_}.json")); g = json.load(open("/home/claude/extracao/gabaritos.json"))[id_]
for q in p["questoes"]:
    n = q["numero"]; av = []
    if q["gabarito"] != g[str(n)]["g"]: av.append(f"gabarito {q['gabarito']} ≠ oficial {g[str(n)]['g']}")
    texto = q["enunciado"] + " ".join(q["alternativas"].values())
    usadas = {int(k) for k in re.findall(r"\[\[fig:(\d+)\]\]", texto)}
    if usadas and max(usadas) > len(q["imagens"]): av.append(f"fig:{max(usadas)} sem imagem ({len(q['imagens'])})")
    if len(q["imagens"]) > len(usadas): av.append(f"{len(q['imagens'])} imagens, {len(usadas)} marcadores")
    for im in q["imagens"]:
        if not (P / im["src"]).exists(): av.append("arquivo falta " + im["src"])
        if len(im.get("alt", "")) < 15: av.append("alt curto")
    if len(q["alternativas"]) != 5: av.append(f"{len(q['alternativas'])} alternativas")
    if q["gabarito"] != "ANULADA" and f"<strong>{q['gabarito']}</strong>" not in q["explicacao"]: av.append("explicação não cita a letra")
    if re.search(r"\w- \w|‹|FIG:|VESTIBULINHO|ﬂ|ﬁ", texto): av.append("artefato no texto")
    if len(q["explicacao"]) < 200: av.append("explicação curta")
    print(f"Q{n:02d} {q['gabarito']} {q['materia']}/{q['assunto']}" + ("  ⚠ " + "; ".join(av) if av else ""))
