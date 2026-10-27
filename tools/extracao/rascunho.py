#!/usr/bin/env python3
"""Rascunho de extração de uma prova em PDF (ETEC/FATEC) para o formato do Treineiros.

NÃO gera a prova final: gera um RASCUNHO para conferência humana, questão por questão,
com a imagem da página ao lado. O que ele faz sozinho:
  - lê o texto na ordem de leitura (uma ou duas colunas), sem cabeçalho e rodapé;
  - mantém negrito, itálico, sobrescrito e subscrito (<strong>, <em>, <sup>, <sub>);
  - troca o "l" cursivo das fórmulas químicas (fonte Mistral) por "ℓ";
  - divide nas questões ("Questão 01"...), separa enunciado e alternativas (A)...(E);
  - reconhece textos de apoio compartilhados ("Leia o texto para responder às questões 8 e 9");
  - marca o texto que está dentro de caixas (texto de apoio) com <p class="apoio">;
  - recorta as figuras (imagens e desenhos vetoriais) em WebP e põe um marcador [[FIG:nome]] no lugar.

Uso:
  python3 tools/extracao/rascunho.py PROVA.pdf PASTA_SAIDA [--paginas 2-24]
Saída: PASTA_SAIDA/rascunho.json, PASTA_SAIDA/fig/*.webp, PASTA_SAIDA/pag/*.png (páginas para conferência)
Precisa de: pip install pymupdf pillow
"""
import argparse, io, json, pathlib, re, statistics
import pymupdf
from PIL import Image

RE_QUESTAO = re.compile(r"^\s*Quest[ãa]o\s*(\d{1,2})?\s*$", re.I)
RE_QUESTAO_JUNTA = re.compile(r"^\s*Quest[ãa]o\s+(\d{1,2})\b\s*(.*)$", re.I)
RE_ALT = re.compile(r"^\s*\(([A-E])\)\s*")
RE_COMPARTILHADO = re.compile(r"quest[õo]es\s*(?:de\s*n[úu]meros\s*)?(?:de\s*)?(\d{1,2})\s*(?:a|e|até)\s*(\d{1,2})", re.I)
RE_RODAPE = re.compile(r"VESTIBULINHO|VESTIBULAR\s|^\s*\d{1,2}\s*$|^\s*•?\s*(Etec|Fatec)\s*$|Página \d+ de|\bSEM\s*\|", re.I)


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def formatar_linha(linha):
    """Transforma os spans de uma linha em HTML simples, detectando sobrescrito e subscrito pelo tamanho e altura."""
    spans = [s for s in linha["spans"] if s["text"]]
    if not spans: return ""
    tam_base = max(s["size"] for s in spans)
    base = statistics.median([s["origin"][1] for s in spans if s["size"] >= tam_base * 0.9])
    partes = []
    for s in spans:
        t = s["text"].replace("\t", " ").replace("\xa0", " ")
        if "Mistral" in s["font"] and t.strip() == "l": t = "ℓ"          # cloro: HCℓ, NaCℓ
        t = esc(t)
        if not t.strip(): partes.append(t); continue
        menor = s["size"] < tam_base * 0.85
        negrito = "Bold" in s["font"] or "Black" in s["font"] or (s["flags"] & 16 and "Univers" not in s["font"])
        italico = "Italic" in s["font"] or "Oblique" in s["font"] or s["flags"] & 2
        alfanum = re.search(r"[0-9A-Za-zÀ-ú+]", t)                         # "–" ou "−" menor não é expoente
        if menor and alfanum and s["origin"][1] > base + 0.8: t = f"<sub>{t}</sub>"
        elif alfanum and (menor and s["origin"][1] < base - 0.8 or (s["flags"] & 1)): t = f"<sup>{t}</sup>"
        if italico: t = f"<em>{t}</em>"
        if negrito: t = f"<strong>{t}</strong>"
        partes.append(t)
    html = "".join(partes)
    html = re.sub(r"</(strong|em)>(\s*)<\1>", r"\2", html)              # junta trechos vizinhos de mesmo estilo
    return re.sub(r"\s+", " ", html).strip()


def texto_puro(html):
    return re.sub(r"<[^>]+>", "", html)


def caixas_de_texto(pagina):
    """Retângulos desenhados (molduras) que contêm texto: viram texto de apoio."""
    caixas = []
    for d in pagina.get_drawings():
        r = d["rect"]
        if r.width > 120 and r.height > 25 and d.get("type") in ("s", "fs", "f") and len(d["items"]) >= 1:
            caixas.append(r)
    return caixas


def figuras(pagina, linhas):
    """Regiões de figura: imagens (sem os rótulos 'Questão') e grupos de desenhos que não são só moldura de texto."""
    regs = []
    # rótulos "Questão NN" nunca fazem parte de figura (o fundo do rótulo é desenho/imagem)
    marcas = [pymupdf.Rect(l["bbox"]) for l in linhas if RE_QUESTAO_JUNTA.match(texto_puro(l["html"]).strip())]
    for info in pagina.get_image_info(xrefs=True):
        r = pymupdf.Rect(info["bbox"])
        if r.height < 28 or r.width < 28: continue                              # rótulos e ícones pequenos
        if r.width > pagina.rect.width * 0.8 and r.height < 40: continue        # faixas decorativas
        if any(r.intersects(m) for m in marcas): continue
        regs.append(r)
    try:
        grupos = pagina.cluster_drawings(x_tolerance=6, y_tolerance=6)
    except Exception:
        grupos = []
    for r in grupos:
        r = pymupdf.Rect(r)
        if r.height < 30 or r.width < 30: continue
        if r.width > pagina.rect.width * 0.8 and r.height < 40: continue
        # quantos caracteres de texto há dentro: moldura de texto tem muito texto e quase nenhum traço interno
        if any(r.intersects(m) for m in marcas): continue
        dentro = sum(len(texto_puro(l["html"])) for l in linhas if pymupdf.Rect(l["bbox"]).intersects(r))
        area = r.width * r.height
        if dentro > area / 120: continue                                        # é caixa de texto, não figura
        regs.append(r)
    # junta regiões sobrepostas
    final = []
    for r in sorted(regs, key=lambda r: (r.y0, r.x0)):
        for f in final:
            if f.intersects(r) or (abs(f.y1 - r.y0) < 6 and f.x0 - 6 < r.x1 and r.x0 < f.x1 + 6):
                f |= r; break
        else:
            final.append(pymupdf.Rect(r))
    return final


def linhas_da_pagina(pagina):
    d = pagina.get_text("dict")
    linhas = []
    h = pagina.rect.height
    for b in d["blocks"]:
        if b["type"] != 0: continue
        for l in b["lines"]:
            html = formatar_linha(l)
            if not texto_puro(html).strip(): continue
            y0, y1 = l["bbox"][1], l["bbox"][3]
            if (y0 > h - 45 or y1 < 22) and RE_RODAPE.search(texto_puro(html)): continue   # cabeçalho/rodapé
            linhas.append({"bbox": l["bbox"], "html": html})
    # "Questão" e o número costumam ser linhas separadas, lado a lado: junta numa só ("Questão 11")
    for q in [l for l in linhas if RE_QUESTAO.match(texto_puro(l["html"]).strip()) and not RE_QUESTAO.match(texto_puro(l["html"]).strip()).group(1)]:
        cy = (q["bbox"][1] + q["bbox"][3]) / 2
        for n in linhas:
            t = texto_puro(n["html"]).strip()
            if re.fullmatch(r"\d{1,2}", t) and abs((n["bbox"][1] + n["bbox"][3]) / 2 - cy) < 7 and 0 < n["bbox"][0] - q["bbox"][2] < 120:
                q["html"] = "Questão " + t
                q["bbox"] = [q["bbox"][0], min(q["bbox"][1], n["bbox"][1]), n["bbox"][2], max(q["bbox"][3], n["bbox"][3])]
                linhas.remove(n); break
    return linhas


def ordenar(linhas, largura):
    """Ordem de leitura: faixas separadas por linhas de largura total; dentro da faixa, coluna esquerda e depois direita."""
    meio = largura / 2
    def tipo(l):
        x0, x1 = l["bbox"][0], l["bbox"][2]
        if x0 < meio - 30 and x1 > meio + 30: return "cheia"
        return "esq" if x1 <= meio + 30 else "dir"
    duas_colunas = sum(1 for l in linhas if tipo(l) == "dir") > 5 and sum(1 for l in linhas if tipo(l) == "esq") > 5
    if not duas_colunas:
        return sorted(linhas, key=lambda l: (round(l["bbox"][1] / 3), l["bbox"][0]))
    linhas = sorted(linhas, key=lambda l: l["bbox"][1])
    saida, faixa = [], []
    def esvaziar():
        saida.extend(sorted([l for l in faixa if tipo(l) == "esq"], key=lambda l: (l["bbox"][1], l["bbox"][0])))
        saida.extend(sorted([l for l in faixa if tipo(l) == "dir"], key=lambda l: (l["bbox"][1], l["bbox"][0])))
        faixa.clear()
    for l in linhas:
        # linha comprida ou figura que ocupa a largura toda separa as faixas de colunas
        if tipo(l) == "cheia" and (l.get("tipo") == "fig" or len(texto_puro(l.get("html", ""))) > 40):
            esvaziar(); saida.append(l)
        else:
            faixa.append(l)
    esvaziar()
    return saida


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf"); ap.add_argument("saida")
    ap.add_argument("--paginas", default="2-")
    ap.add_argument("--dpi", type=int, default=200, help="resolução dos recortes de figura")
    a = ap.parse_args()
    out = pathlib.Path(a.saida); (out / "fig").mkdir(parents=True, exist_ok=True); (out / "pag").mkdir(exist_ok=True)
    doc = pymupdf.open(a.pdf)
    ini, _, fim = a.paginas.partition("-")
    paginas = range(int(ini) - 1, int(fim) if fim else len(doc))

    fluxo = []                    # sequência de itens: linhas de texto e figuras, na ordem de leitura
    for pi in paginas:
        pg = doc[pi]
        pg.get_pixmap(dpi=110).save(out / "pag" / f"p{pi + 1:02d}.png")
        linhas = linhas_da_pagina(pg)
        caixas = caixas_de_texto(pg)
        figs = figuras(pg, linhas)
        for l in linhas:
            r = pymupdf.Rect(l["bbox"])
            l["apoio"] = any(c.contains(r) or (c & r).get_area() > r.get_area() * 0.8 for c in caixas)
            l["dentro_fig"] = any((f & r).get_area() > r.get_area() * 0.6 for f in figs)
        itens = [dict(l, tipo="linha", pag=pi + 1) for l in linhas if not l["dentro_fig"]]
        figs = [f for f in figs if (f & pg.rect).width > 2 and (f & pg.rect).height > 2]   # descarta figuras vazias ou fora da página
        for k, f in enumerate(figs):
            nome = f"p{pi + 1:02d}-{k + 1}"
            pix = pg.get_pixmap(clip=f + (-3, -3, 3, 3), dpi=a.dpi)
            Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB").save(out / "fig" / f"{nome}.webp", "WEBP", quality=82, method=6)
            # texto que ficou dentro da figura (rótulos, legendas): guardado para conferência
            rotulos = " / ".join(texto_puro(l["html"]) for l in linhas if l["dentro_fig"] and (f & pymupdf.Rect(l["bbox"])).get_area() > 0)
            itens.append({"tipo": "fig", "nome": nome, "bbox": list(f), "pag": pi + 1, "rotulos": rotulos[:300]})
        fluxo.extend(ordenar(itens, pg.rect.width))

    # Junta "Questão" + número quando vierem em linhas separadas
    marcados = []
    i = 0
    while i < len(fluxo):
        it = fluxo[i]
        if it["tipo"] == "linha":
            t = texto_puro(it["html"]).strip()
            m = RE_QUESTAO.match(t)
            if m and not m.group(1):
                for j in range(i + 1, min(i + 4, len(fluxo))):                 # número logo ao lado
                    if fluxo[j]["tipo"] == "linha" and re.fullmatch(r"\d{1,2}", texto_puro(fluxo[j]["html"]).strip()):
                        marcados.append({"tipo": "questao", "n": int(texto_puro(fluxo[j]["html"])), "pag": it["pag"]})
                        fluxo.pop(j); break
                else:
                    marcados.append(it)
                i += 1; continue
            if m and m.group(1):
                marcados.append({"tipo": "questao", "n": int(m.group(1)), "pag": it["pag"]}); i += 1; continue
            m2 = RE_QUESTAO_JUNTA.match(t)
            if m2 and len(t) < 14:
                marcados.append({"tipo": "questao", "n": int(m2.group(1)), "pag": it["pag"]}); i += 1; continue
        marcados.append(it); i += 1

    # Divide em questões
    questoes, atual, pre = {}, None, []        # pre = texto antes de uma questão (apoio compartilhado)
    compartilhado = {}                           # nº da questão -> lista de itens de apoio
    for it in marcados:
        if it["tipo"] == "questao":
            atual = {"numero": it["n"], "pag": it["pag"], "enunciado": [], "alternativas": {}, "figs": [], "_alt": None, "_ult": None, "_x0": 0}
            questoes[it["n"]] = atual
            if pre:
                txt = " ".join(texto_puro(p.get("html", "")) for p in pre if p["tipo"] == "linha")
                m = RE_COMPARTILHADO.search(txt)
                alvo = range(it["n"], int(m.group(2)) + 1) if m and int(m.group(1)) == it["n"] else [it["n"]]
                for n in alvo: compartilhado.setdefault(n, []).extend(pre)
                pre = []
            continue
        if atual is None:
            pre.append(it); continue
        if it["tipo"] == "linha":
            t = texto_puro(it["html"])
            m = RE_ALT.match(t)
            if m:
                atual["_alt"] = m.group(1); atual["_ult"] = it; atual["_x0"] = it["bbox"][0]
                atual["alternativas"][m.group(1)] = re.sub(r"^\s*\(\s*[A-E]\s*\)\s*", "", it["html"])
                continue
            if atual["_alt"] == "fim":
                pre.append(it); continue
            if atual["_alt"]:
                ult = atual["_ult"]; alt_l = ult["bbox"][3] - ult["bbox"][1]
                continua = (it["pag"] == ult["pag"] and it["bbox"][0] >= atual["_x0"] + 6
                            and it["bbox"][1] - ult["bbox"][3] < alt_l * 0.6 and not it.get("apoio"))
                if continua:
                    atual["alternativas"][atual["_alt"]] += " " + it["html"]; atual["_ult"] = it
                elif atual["_alt"] == "E" or atual["_alt"] == "D" and len(atual["alternativas"]) == 4 and False:
                    pre.append(it); atual["_alt"] = "fim"                     # texto depois da (E): apoio da próxima questão
                else:
                    atual["alternativas"][atual["_alt"]] += " ‹CONFERIR› " + it["html"]; atual["_ult"] = it
            else:
                atual["enunciado"].append(it)
        else:
            if atual["_alt"] in ("E", "fim"): pre.append(it); atual["_alt"] = "fim"
            elif atual["_alt"]: atual["alternativas"][atual["_alt"]] += f" [[FIG:{it['nome']}]]"
            else: atual["enunciado"].append(it)

    def paragrafos(itens):
        """Agrupa linhas em parágrafos pelo espaçamento vertical; figuras viram marcadores."""
        html, par, ult, ult_apoio = [], [], None, None
        def fecha():
            if par:
                html.append(f'<p{" class=\"apoio\"" if ult_apoio else ""}>{" ".join(par)}</p>')
                par.clear()
        for it in itens:
            if it["tipo"] == "fig":
                fecha(); html.append(f"[[FIG:{it['nome']}]]"); ult = None; continue
            b = it["bbox"]; alt = b[3] - b[1]
            novo = ult is None or it["pag"] != ult["pag"] or b[1] - ult["bbox"][3] > max(1.2, alt * 0.12) or it["apoio"] != ult_apoio \
                or (b[0] - ult["bbox"][0] > 12 and texto_puro(it["html"])[:1].isupper())
            if novo: fecha()
            if par and par[-1].endswith("-") and texto_puro(it["html"])[:1].islower():
                par[-1] = par[-1][:-1] + "‹HIFEN›"                             # conferir: hífen de quebra ou palavra composta?
                par.append(it["html"]); par[-2:] = ["".join(par[-2:])]
            else:
                par.append(it["html"])
            ult, ult_apoio = it, it["apoio"]
        fecha()
        junto = "".join(html)
        # crédito da fonte ("<https://...> Acesso em: ...") vira parágrafo próprio, discreto
        junto = re.sub(r'\s*((?:Fonte[^<]{0,40}:\s*)?&lt;https?://[^&]+&gt;\s*(?:Acesso em:?\s*[\d./]+\.?)?\s*(?:Original colorido\.|Adaptado\.)?\s*(?:Original colorido\.|Adaptado\.)?)\s*</p>',
                       r'</p><p class="fonte">\1</p>', junto)
        return re.sub(r"<p( class=\"apoio\")?></p>", "", junto)

    saida = []
    for n in sorted(questoes):
        q = questoes[n]
        apoio = paragrafos(compartilhado.get(n, []))
        saida.append({
            "numero": n, "pagina": q["pag"],
            "enunciado": apoio + paragrafos(q["enunciado"]),
            "alternativas": {k: re.sub(r"\s+", " ", v).strip() for k, v in q["alternativas"].items()},
            "figs": re.findall(r"\[\[FIG:([^\]]+)\]\]", apoio + paragrafos(q["enunciado"]) + " ".join(q["alternativas"].values())),
        })
    sobras = paragrafos(pre) if pre else ""
    json.dump({"questoes": saida, "sobras_fim": sobras}, open(out / "rascunho.json", "w"), ensure_ascii=False, indent=1)
    print(f"{len(saida)} questões no rascunho; figuras em {out / 'fig'}; páginas em {out / 'pag'}")
    falt = [i for i in range(1, max(questoes) + 1) if i not in questoes] if questoes else []
    if falt: print("ATENÇÃO, questões não encontradas:", falt)
    for q in saida:
        if len(q["alternativas"]) < 4: print(f"  questão {q['numero']}: só {len(q['alternativas'])} alternativas")


if __name__ == "__main__":
    main()
