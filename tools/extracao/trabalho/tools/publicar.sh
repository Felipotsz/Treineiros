#!/bin/bash
# Fecha uma prova: copia o PDF para o site e tira o status "em preparação" da edição. Uso: publicar.sh <id>
set -e
id=$1; P=/home/claude/proj/treineiros
cp /home/claude/extracao/fontes/$id-prova.pdf $P/assets/provas/$id.pdf
python3 - "$id" <<'PY'
import json, sys
p = "/home/claude/proj/treineiros/data/edicoes.json"
d = json.load(open(p))
for e in d["edicoes"]:
    if e["id"] == sys.argv[1]:
        e.pop("status", None)
json.dump(d, open(p, "w"), ensure_ascii=False, indent=1); open(p, "a").write("\n")
PY
echo "publicada: $id"
