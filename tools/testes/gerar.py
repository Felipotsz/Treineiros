#!/usr/bin/env python3
"""Gera os índices das provas de exemplo usadas nos testes (tools/testes/). Rode depois de mudar os exemplos."""
import json, pathlib, sys
AQUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent))
import validar
provas = [json.loads((AQUI / f"{p['id']}.json").read_text(encoding="utf-8")) for p in json.loads((AQUI / "provas.json").read_text(encoding="utf-8"))]
validar.gerar_indices(provas, AQUI)
