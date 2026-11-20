#!/usr/bin/env python3
"""Rascunho de uma prova do Enem a partir dos blocos de texto do PDF (o caderno tem duas colunas e texto limpo).
Uso: enem_rascunho.py <id> <pág-inicial> <pág-final>
Saída: <id>/enem.json  {numero: {paragrafos: [[tipo, html]], alternativas: {A..E}, figs: [[pág, x0, y0, x1, y1]]}}
tipo: "p" (texto), "fonte" (referência em letra pequena), "fig" (lugar de uma figura; o índice está em figs)."""
import json, re, sys, pathlib, pymupdf
id_, ini, fim = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
base = pathlib.Path("/home/claude/extracao") / id_
doc = pymupdf.open(base.parent / "fontes" / f"{id_}-prova.pdf")
LIG = lambda s: s.replace("ﬁ", "fi").replace("ﬂ", "fl").replace("ﬀ", "ff").replace("ﬃ", "ffi")
CAB = re.compile(r"^(\*[A-Z0-9]+\*|\d{1,2}|20\d\d|CIÊNCIAS (HUMANAS|DA NATUREZA).*|LINGUAGENS.*|MATEMÁTICA.*|Questões de \d+ a \d+.*|.*\| Caderno \d+ - [A-Z]+ - Página \d+|.*\| \dº DIA \| CADERNO \d+ \| [A-Z]+|E SUAS TECNOLOGIAS.*)$", re.I)
qs, atual, modo = {}, None, None
import os
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from enem_decod import dict_decodificado
DECOD = os.environ.get("DECOD") == "1"
ALT2010 = os.environ.get("ALT2010") == "1"
ALTSPAN = os.environ.get("ALTSPAN") == "1"
TOPO = float(os.environ.get("TOPO", "50"))           # Enem 2009: cabeçalho no rodapé; texto começa em y≈36


def juntar(linhas):
    s = ""
    for l in linhas:
        l = l.rstrip()
        if not s: s = l.strip(); continue
        if s.endswith("-") and l[:1].islower() and not re.search(r"\s\S{1,3}-$", s): s = s[:-1] + l.strip()   # sílaba partida
        else: s += " " + l.strip()
    s = re.sub(r"\s*\d+ –[A-Z]{2} • \dº DIA • CADERNO \d+ • [A-ZÇ]+–", "", s)          # rodapé do Enem 2023 colado ao texto
    s = re.sub(r"\s*\d*\s*(?:(?:CN|MT|LC|CH) • \dº DIA • CADERNO \d+ • [A-ZÇ]+\s*)+", " ", s).strip()  # rodapé sem travessões (2023, 2º dia)
    return re.sub(r"\s+", " ", LIG(s)).strip()


for pn in range(ini, fim + 1):
    pg = doc[pn - 1]; W = pg.rect.width; H = pg.rect.height
    blocos = []
    MARCAS = [d["rect"] for d in pg.get_drawings() if ALT2010 and d.get("fill") and max(d["fill"]) < 0.3 and 5.5 < d["rect"].width < 8.5 and 5.5 < d["rect"].height < 8.5]
    for b in (dict_decodificado(pg) if DECOD else pg.get_text("dict"))["blocks"]:
        if b["type"] != 0: continue
        # letra da alternativa numa fonte de símbolos (Enem 2021: BundesbahnPi) vira "A\t", como nos outros anos
        linhas = ["".join((sp["text"].strip() + "\t") if sp["font"].startswith(("BundesbahnPi", "Circled-Letter", "CircledLetters")) and re.fullmatch(r"\s*[A-E]\s*", sp["text"]) else sp["text"] for sp in ln["spans"]) for ln in b["lines"]]
        if ALTSPAN:                                  # Enem 2006: letra numa fonte própria, num span de um só caractere
            linhas = [("@\t" + "".join(sp["text"] for sp in ln["spans"][1:]).lstrip()) if len(ln["spans"]) > 2 and re.fullmatch(r"[A-E]", ln["spans"][0]["text"]) and ln["spans"][0]["font"] != ln["spans"][2]["font"] else l
                      for l, ln in zip(linhas, b["lines"])]
        if ALT2010:                                  # Enem 2010: letras das alternativas são círculos desenhados à esquerda da linha
            linhas = [("@\t" + l.lstrip()) if any(abs((m.y0 + m.y1) / 2 - (ln["bbox"][1] + ln["bbox"][3]) / 2) < 4.5 and ln["bbox"][0] - 25 < m.x0 < ln["bbox"][0] + 20
                                                   for m in MARCAS) else l for l, ln in zip(linhas, b["lines"])]
        txt = "\n".join(linhas).strip()
        if not txt: continue
        tam = max((sp["size"] for ln in b["lines"] for sp in ln["spans"] if sp["text"].strip()), default=10)
        x0, y0, x1, y1 = b["bbox"]
        if (y0 < TOPO and not re.search(r"^\s*Questão\s*\d", txt, re.M | re.I) and not re.match(r"\s*Questão\s*$", txt)) or y1 > H - 25: continue   # Enem 2009: "Questão N" no topo da página (y≈43)                                   # cabeçalho e rodapé
        if all(CAB.match(l.strip()) for l in linhas if l.strip()): continue
        if re.fullmatch(r"(Rascunho\s*)+", txt): continue                    # Enem 2010: faixa "Rascunho" depois da última alternativa
        if tam < 4: continue                                                # marca-d'água (ENEM2025... em letra de 1,5 pt)
        col = 0 if x0 < W / 2 - 5 else 1
        # "QUESTÃO NN" no meio do bloco (Enem 2022: alternativas da anterior + rótulo no mesmo bloco): parte o bloco ali
        cortes = [i for i, l in enumerate(linhas) if i > 0 and re.match(r"^\s*QUESTÃO\s+\d+", l, re.I)
                  and not all(CAB.match(x.strip()) or re.match(r"^(Questões de|Texto para)", x.strip()) for x in linhas[:i] if x.strip())]
        ini = 0
        for c in cortes + [len(linhas)]:
            ls = linhas[ini:c]
            if "\n".join(ls).strip():
                yy0 = b["lines"][ini]["bbox"][1]; yy1 = b["lines"][c - 1]["bbox"][3]
                blocos.append({"col": col, "x0": x0, "y0": yy0, "x1": x1, "y1": yy1, "txt": "\n".join(ls).strip(), "linhas": ls, "tam": tam})
            ini = c
    # figuras: imagens e desenhos (sem filetes, logotipos e o cabeçalho), unidos quando se tocam
    vis = [pymupdf.Rect(i["bbox"]) for i in pg.get_image_info()] + [pymupdf.Rect(r) for r in pg.cluster_drawings(drawings=[d for d in pg.get_drawings() if d["rect"].width > 3 and d["rect"].height > 3])]  # sem filetes (Enem 2016: filetes juntavam a página toda numa "figura")
    vis = [r for r in vis if r.y0 > 48 and r.y1 < H - 25 and r.width > 30 and r.height > 20]
    for r in vis:                                    # imagem que sangra um pouco para a outra coluna: corta no meio da página
        if r.x0 < W / 2 - 50 and W / 2 - 3 < r.x1 < W / 2 + 30: r.x1 = W / 2 - 3
        if r.x1 > W / 2 + 50 and W / 2 - 30 < r.x0 < W / 2 + 3: r.x0 = W / 2 + 3
    juntou = True
    while juntou:
        juntou = False
        for i1 in range(len(vis)):
            for i2 in range(i1 + 1, len(vis)):
                if (vis[i1] + (-4, -4, 4, 4)).intersects(vis[i2]): vis[i1] |= vis[i2]; vis.pop(i2); juntou = True; break
            if juntou: break
    for r in vis:
        blocos.append({"col": 0 if r.x0 < W / 2 - 5 else 1, "x0": r.x0, "y0": r.y0, "x1": r.x1, "y1": r.y1, "fig": [pn, round(r.x0) - 3, round(r.y0) - 3, round(r.x1) + 3, round(r.y1) + 3], "txt": "", "linhas": [""], "tam": 10})
    # página em coluna única (Enem 2025): a maior parte do texto atravessa o meio da página
    largos = [b for b in blocos if b["txt"] and b["x0"] < W / 2 - 30 and b["x1"] > W / 2 + 30]
    if len(largos) * 2 >= len([b for b in blocos if b["txt"]]) * 0.6 and len(largos) >= 3:
        for b in blocos: b["col"] = 0
    blocos.sort(key=lambda b: (b["col"], b["y0"]))
    for i in range(len(blocos) - 2, -1, -1):          # Enem 2009: "Questão" e o número em blocos separados
        a, b2 = blocos[i], blocos[i + 1]
        if re.fullmatch(r"Quest[ãa]o", a["txt"], re.I) and re.fullmatch(r"\d{1,3}", b2["txt"]) and a["col"] == b2["col"]:
            a["txt"] = f"Questão {b2['txt']}"; a["linhas"] = [a["txt"]]; blocos.pop(i + 1)
    for b in blocos:
        # cabeçalho da área colado ao "QUESTÃO NN" no mesmo bloco (Enem 2024): descarta as linhas de cabeçalho
        iq = next((i for i, l in enumerate(b["linhas"]) if re.match(r"^\s*QUESTÃO\s+\d+", l, re.I)), None)
        if iq and all(CAB.match(l.strip()) or re.match(r"^(Questões de|Texto para)", l.strip()) for l in b["linhas"][:iq] if l.strip()):
            b = dict(b, linhas=b["linhas"][iq:], txt="\n".join(b["linhas"][iq:]).strip())
        m = re.match(r"^QUESTÃO\s+(\d+)", b["txt"], re.I)
        if b.get("fig"):
            if atual is not None:
                # texto dentro da figura (rótulos, falas) não entra como parágrafo
                qs[atual]["figs"].append(b["fig"]); qs[atual]["paragrafos"].append(["fig", len(qs[atual]["figs"])])
            continue
        if atual is not None and any(f[0] == pn and f[1] <= b["x0"] and b["x1"] <= f[3] and f[2] <= b["y0"] and b["y1"] <= f[4] for f in qs[atual]["figs"]):
            continue
        # espaço vazio grande na coluna, dentro de uma questão: figura
        if m:
            atual = int(m.group(1))
            if atual in qs: atual = f"{atual}-es"                 # Linguagens: questões 1 a 5 de espanhol repetem a numeração
            qs[atual] = {"paragrafos": [], "alternativas": {}, "figs": [], "pag": pn}; modo = "enun"
            resto = b["txt"][m.end():].strip()
            if resto: qs[atual]["paragrafos"].append(["p", juntar(resto.split("\n"))])
            continue
        if atual is None: continue
        q = qs[atual]
        # bloco que mistura o fim do comando com o começo das alternativas: separa nas duas partes
        ia = next((i for i, l in enumerate(b["linhas"]) if re.match(r"^[A@]\t", l)), None)
        if ia and modo != "alt" and b["tam"] >= 8.5:
            q["paragrafos"].append(["p", juntar(b["linhas"][:ia])])
            b = dict(b, linhas=b["linhas"][ia:])
        if re.match(r"^[A-E@]\t", b["linhas"][0]) or (modo == "alt" and b["tam"] >= 8.5):
            modo = "alt"; cur = q.get("_alt")
            for l in b["linhas"]:
                ma = re.match(r"^([A-E@])\t\s*(.*)$", l)
                if ma:
                    cur = ma.group(1) if ma.group(1) != "@" else "ABCDEF"[min(len(q["alternativas"]), 5)]
                    q["alternativas"][cur] = ma.group(2)
                elif cur: q["alternativas"][cur] += " " + l.strip()
            q["_alt"] = cur
            continue
        tipo = "fonte" if b["tam"] < 8.5 else "p"
        txt = juntar(b["linhas"])
        if tipo == "fonte" and q["paragrafos"] and q["paragrafos"][-1][0] == "fonte": q["paragrafos"][-1][1] += " " + txt
        else: q["paragrafos"].append([tipo, txt])
    # figura no fim da coluna (depois do último bloco de texto da questão)
for q in qs.values():
    q.pop("_alt", None)
    q["alternativas"] = {k: re.sub(r"\s+", " ", LIG(v)).strip() for k, v in q["alternativas"].items()}
(base / "enem.json").write_text(json.dumps(qs, ensure_ascii=False, indent=1))
nums = [k for k in qs if isinstance(k, int)]
falta = [n for n in range(min(nums), max(nums) + 1) if n not in qs or len(qs[n]["alternativas"]) != 5] + [k for k in qs if not isinstance(k, int) and len(qs[k]["alternativas"]) != 5]
print(f"{len(qs)} questões; com problema nas alternativas: {falta}")
