#!/usr/bin/env python3
"""Atualiza em sw.js a lista de arquivos guardados para uso offline."""
import hashlib, json, pathlib, re

RAIZ = pathlib.Path(__file__).resolve().parent.parent
IGNORAR_PASTAS = {"tools", ".github", "node_modules", "q"}   # q/ = páginas estáticas por questão (muitas; o site funciona sem elas offline)
IGNORAR_ARQUIVOS = {"sw.js", "README.md", "PUBLICAR.md", ".nojekyll", "treineiros-continuar.md", "sitemap.xml", "robots.txt"}


def main():
    arquivos = []
    for p in sorted(RAIZ.rglob("*")):
        rel = p.relative_to(RAIZ)
        if not p.is_file() or rel.parts[0] in IGNORAR_PASTAS or p.name in IGNORAR_ARQUIVOS:
            continue
        if p.suffix in {".zip", ".py", ".md", ".txt"} or p.name in {"styleguide.html", "revisar.html", "package.json", "package-lock.json"}:
            continue
        # pesado para o celular: vai para o cache só quando a pessoa abre (ou guarda) a prova
        if rel.as_posix().startswith(("data/provas/", "assets/img/", "assets/provas/", "assets/fotos/")) or rel.as_posix() == "data/busca.json":
            continue
        arquivos.append(rel.as_posix())
    sw = RAIZ / "sw.js"
    texto = sw.read_text(encoding="utf-8")
    # VERSAO muda sozinha quando qualquer arquivo da casca muda: os aparelhos pegam a versão nova sem ninguém lembrar de trocar
    h = hashlib.sha256()
    for a in arquivos: h.update(a.encode()); h.update((RAIZ / a).read_bytes())
    texto, n = re.subn(r'var VERSAO = "[^"]*";', f'var VERSAO = "treineiros-{h.hexdigest()[:10]}";', texto)
    assert n == 1, "VERSAO não encontrada em sw.js"
    bloco = "/* ARQUIVOS:INICIO */\nvar ARQUIVOS = " + json.dumps(["./"] + arquivos, ensure_ascii=False, indent=2) + ";\n/* ARQUIVOS:FIM */"
    novo, n = re.subn(r"/\* ARQUIVOS:INICIO \*/.*?/\* ARQUIVOS:FIM \*/", lambda m: bloco, texto, flags=re.S)
    assert n == 1, "marcadores não encontrados em sw.js"
    sw.write_text(novo, encoding="utf-8")
    print(f"sw.js atualizado com {len(arquivos) + 1} arquivos para uso offline.")


if __name__ == "__main__":
    main()
