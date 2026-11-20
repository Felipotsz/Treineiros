#!/bin/bash
# Começa uma prova: rascunho (páginas de questão), texto.txt e a listagem do rascunho. Uso: iniciar.sh <id> <pág-inicial> <pág-final>
set -e
cd /home/claude/extracao; id=$1
rm -rf $id/rascunho; mkdir -p $id
python3 /home/claude/proj/treineiros/tools/extracao/rascunho.py fontes/$id-prova.pdf $id/rascunho --paginas $2-$3 | tail -1
python3 - "$id" <<'PY'
import pymupdf, sys
id_=sys.argv[1]; d=pymupdf.open(f'fontes/{id_}-prova.pdf')
open(f'{id_}/texto.txt','w').write("\n".join(f"===== {i}\n"+p.get_text() for i,p in enumerate(d,1)))
PY
python3 tools/ver.py $id 1 99 > /tmp/claude-0/ver-$id.txt; wc -l /tmp/claude-0/ver-$id.txt
