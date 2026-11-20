"""Lê os 30 gabaritos oficiais (texto do pdftotext -layout) e gera gabaritos.json."""
# ATENÇÃO: rodar de novo apaga as retificações feitas à mão em gabaritos.json (ver PROGRESSO.md).
import re, json, pathlib
F = pathlib.Path("/home/claude/extracao/fontes")
item = re.compile(r"(?<!\d)(\d{1,3})\s{1,20}([A-E]|ANULADA)(?![A-Za-z])\s+(?:(C\d)|([A-Za-zÀ-úﬁ][A-Za-zÀ-úﬁ ]*?))?(?=\s{2,}|\s*$)")
saida = {}
for t in sorted(F.glob("*-gabarito.txt")):
    nome = t.stem.replace("-gabarito", "")
    qs = {}
    for linha in t.read_text().splitlines():
        for m in item.finditer(linha):
            n = int(m.group(1)); 
            if n in qs or n > 64 or n < 1: continue
            qs[n] = {"g": m.group(2), "comp": m.group(3), "disc": (m.group(4) or "").replace("ﬁ", "fi").strip() or None}
    saida[nome] = qs
    esperado = 50 if nome.startswith("etec") else 60
    faltam = [i for i in range(1, esperado + 1) if i not in qs]
    anul = [n for n, v in sorted(qs.items()) if v["g"] == "ANULADA"]
    print(f"{nome:16} {len(qs):3} questões  faltam={faltam}  anuladas={anul}")
json.dump(saida, open("/home/claude/extracao/gabaritos.json", "w"), ensure_ascii=False, indent=1)
