#!/usr/bin/env python3
"""Aplica nas provas o arquivo baixado em revisar.html.

Uso (na raiz do projeto):  python3 tools/aplicar_revisao.py revisao.json
- "revisada": true  → explicacaoRevisada = true
- "explicacao": "…" → troca o texto da explicação (e, se não vier "revisada", volta explicacaoRevisada para false)
Depois rode:  python3 tools/validar.py --indexar
"""
import json, sys, pathlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent


def main():
    if len(sys.argv) < 2:
        print(__doc__); return 1
    dados = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
    if dados.get("app") != "treineiros-revisao":
        print("Este arquivo não veio da página revisar.html."); return 1
    por_prova = {}
    for chave, alt in dados.get("alteracoes", {}).items():
        pid, _, num = chave.rpartition("#")
        por_prova.setdefault(pid, {})[int(num)] = alt
    total = 0
    for pid, alts in por_prova.items():
        arq = RAIZ / "data" / "provas" / f"{pid}.json"
        if not arq.exists():
            print(f"aviso: {arq.name} não existe; ignorado"); continue
        prova = json.loads(arq.read_text(encoding="utf-8"))
        for q in prova["questoes"]:
            alt = alts.get(q["numero"])
            if not alt: continue
            if "explicacao" in alt:
                q["explicacao"] = alt["explicacao"]; q["explicacaoRevisada"] = False
            if alt.get("revisada"):
                q["explicacaoRevisada"] = True
            total += 1
        arq.write_text(json.dumps(prova, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"{arq.name}: {len(alts)} questão(ões) atualizada(s)")
    print(f"\n{total} alteração(ões) aplicada(s). Agora rode: python3 tools/validar.py --indexar")
    return 0


if __name__ == "__main__":
    sys.exit(main())
