import pymupdf, re, json, sys
d = pymupdf.open(sys.argv[1])
linhas = []
for pn in range(2, d.page_count):
    for b in d[pn].get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            x0, y0, x1, y1 = l["bbox"]
            if y0 < 60 or y1 > 805: continue
            CX = 315 if pn == 17 else 300
            # linhas que atravessam as duas colunas: separa os spans por coluna
            for lado in (False, True):
                sp = [s for s in l["spans"] if (s["bbox"][0] >= CX) == lado]
                if not sp: continue
                bb = [min(s["bbox"][0] for s in sp), y0, max(s["bbox"][2] for s in sp), y1]
                linhas.append((pn, lado, round(y0), bb[0], {"bbox": bb, "spans": sp}))
linhas.sort(key=lambda t: (t[0], t[1], (t[4]["bbox"][1] + t[4]["bbox"][3]) / 2))
# agrupa linhas da mesma altura (justificação quebra a linha em pedaços; o círculo da letra fica um pouco desalinhado)
grup = []; ref = None; gi = -1
for t in linhas:
    yc = (t[4]["bbox"][1] + t[4]["bbox"][3]) / 2
    if ref is None or (t[0], t[1]) != ref[:2] or yc - ref[2] > 3: gi += 1; ref = (t[0], t[1], yc)
    grup.append((t[0], t[1], gi, t[3], t[4]))
linhas = [(a, b, round(c), x, l) for a, b, c, x, l in sorted(grup, key=lambda t: (t[0], t[1], t[2], t[3]))]
# y real do grupo para medir distâncias
ygr = {}
for a, b, c, x, l in linhas: ygr.setdefault((a, b, c), l["bbox"][1])
linhas = [(a, b, ygr[(a, b, c)], x, l) for a, b, c, x, l in linhas]
Q = {}; atual = 0; alt = None; ult = None
for pn, col, y, x, l in linhas:
    sp = l["spans"]; txt = "".join(s["text"] for s in sp).strip()
    if re.fullmatch(r"\d{1,2}", txt) and "Bold" in sp[0]["font"] and int(txt) == atual + 1:
        atual += 1; Q[atual] = {}; alt = None; continue
    if not atual: continue
    novo = False
    for s in sp:
        t = s["text"]
        if s["font"].startswith("CircledLetters") and t.strip() in list("ABCDE"):
            alt = t.strip(); Q[atual][alt] = ""; novo = True; ult = (pn, col, y); continue
        if alt and (novo or (ult and (pn, col) == ult[:2] and 0 <= y - ult[2] <= 16)):
            Q[atual][alt] += t
    if alt and not novo and ult and (pn, col) == ult[:2] and 0 <= y - ult[2] <= 16: ult = (pn, col, y)
    elif not novo: alt = None if (ult and ((pn, col) != ult[:2] or y - ult[2] > 14)) else alt
out = {str(k): {a: re.sub(r"\s+", " ", v).strip() for a, v in v.items()} for k, v in Q.items()}
json.dump(out, open(sys.argv[2], "w"), ensure_ascii=False, indent=0)
bad = [k for k, v in out.items() if sorted(v) != list("ABCDE") or any(not t for t in v.values())]
print(len(out), "ruins:", bad)
