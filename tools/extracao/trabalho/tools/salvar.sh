#!/bin/bash
# Copia o trabalho de extração (ajustes, recortes, ferramentas) para dentro do projeto e gera um zip de segurança.
# Uso: salvar.sh <nome-do-zip>
set -e
X=/home/claude/extracao; T=/home/claude/proj/treineiros/tools/extracao/trabalho
rm -rf $T; mkdir -p $T/tools
cp $X/tools/*.py $X/tools/*.sh $T/tools/ 2>/dev/null || true
cp $X/gabaritos.json $X/PROGRESSO.md $T/
for d in $X/etec-* $X/fatec-*; do
  [ -d "$d" ] || continue; n=$(basename $d); mkdir -p $T/$n
  for f in ajustes.py recortes.json; do [ -f $d/$f ] && cp $d/$f $T/$n/; done
done
mkdir -p /home/claude/entrega; cd /home/claude/proj
rm -rf treineiros/tools/__pycache__ treineiros/tools/extracao/__pycache__
rm -f /home/claude/entrega/$1.zip; zip -qr /home/claude/entrega/$1.zip treineiros -x '*/__pycache__/*' '*/node_modules/*'
ls -la /home/claude/entrega/$1.zip
