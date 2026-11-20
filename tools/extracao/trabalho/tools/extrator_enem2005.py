import pymupdf, re, json, sys, os
YMIN = float(os.environ.get("YMIN", "36")); YMAX = float(os.environ.get("YMAX", "738"))  # 2004: YMIN=60 YMAX=775
d = pymupdf.open(sys.argv[1])
itens = []          # (pág, y, x, tipo, conteúdo)
for pn in range(int(os.environ.get("START", "1")), d.page_count):  # 1998: START=0 (questões já na pág. 1)
    pg = d[pn]
    for b in pg.get_text("dict")["blocks"]:
        x0, y0, x1, y1 = b["bbox"]
        LIN = os.environ.get("LINHAS") == "1"  # 2001: filtra por linha, não por bloco (blocos de coluna inteira passam do rodapé)
        if (b["type"] == 1 or not LIN) and (y0 < YMIN or y1 > YMAX): continue
        if b["type"] == 1:
            if x1 - x0 < 5 or y1 - y0 < 5: continue
            itens.append((pn + 1, y0, x0, "IMG", [round(v) for v in b["bbox"]])); continue
        for l in b["lines"]:
            s = "".join(sp["text"] for sp in l["spans"]).strip()
            if not s: continue
            if LIN and (l["bbox"][1] < YMIN or l["bbox"][3] > YMAX): continue
            negr = all(os.environ.get("NFONT", "Bold") in sp["font"] for sp in l["spans"] if sp["text"].strip())
            itens.append((pn + 1, l["bbox"][1], l["bbox"][0], "N" if (negr and re.fullmatch(r"\d{1,2}\.?", s)) else "T", (s, [round(v) for v in l["bbox"]])))
    # desenhos vetoriais grandes (gráficos)
    rs = [dr["rect"] for dr in pg.get_drawings() if dr["rect"].width > 30 and dr["rect"].height > 30]
    for r in rs: itens.append((pn + 1, r.y0, r.x0, "DRW", [round(r.x0), round(r.y0), round(r.x1), round(r.y1)]))
COLS = {int(x) for x in os.environ.get("COLS", "").split(",") if x}; COLX = float(os.environ.get("COLX", "300"))  # páginas em duas colunas (2002: COLS=4,5,11,15,17 COLX=300)
itens.sort(key=lambda t: (t[0], (t[2] >= COLX) if t[0] in COLS else 0, round(t[1]), t[2]))
Q = {}; atual = "0"; esperado = 1
NXR = [tuple(map(float, r.split("-"))) for r in os.environ.get("NXR", "").split(",") if r]  # faixas de x aceitas para o número da questão (2001: NXR=44-88,345-360)
for it in itens:
    if it[3] == "N" and (not NXR or any(a <= it[4][1][0] <= b for a, b in NXR)) and int(it[4][0].rstrip(".")) == esperado:
        atual = it[4][0].rstrip("."); esperado += 1; Q[atual] = []; continue
    Q.setdefault(atual, []).append(it)
out = []
for k, v in Q.items():
    out.append(f"===== Q{k}")
    for p, y, x, t, c in v:
        if t == "T": out.append(f"p{p} {c[1][0]:>3},{c[1][1]:>3} {c[0]}")
        else: out.append(f"p{p} {t} {c}")
open(sys.argv[2], "w").write("\n".join(out))
print(len(Q), esperado - 1)
