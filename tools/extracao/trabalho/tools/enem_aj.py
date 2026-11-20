"""Ajudantes para os ajustes das provas do Enem montadas a partir de <id>/enem.json (tools/enem_rascunho.py)."""
import json, pathlib, re
A = '</p><p class="apoio">'
RAIZ = pathlib.Path(__file__).resolve().parent.parent


def carregar_enem(id_dia):
    return {(int(k) if k.isdigit() else k): v for k, v in json.load(open(RAIZ / id_dia / "enem.json")).items()}


def montar_enunciado(q, pular=(), trocas=()):
    """Texto de apoio (antes da última referência) em parágrafos de apoio; referência em letra pequena; o comando em <p>."""
    par = [x for i, x in enumerate(q["paragrafos"]) if i not in pular]
    ult = max([i for i, (t, _) in enumerate(par) if t == "fonte"], default=-1)
    html = []
    for i, (t, x) in enumerate(par):
        if t == "fig": html.append(f"[[fig:{x}]]")
        elif t == "fonte": html.append(f'<p class="fonte">{x}</p>')
        elif i < ult: html.append(f'<p class="apoio">{x}</p>')
        else: html.append(f"<p>{x}</p>")
    s = "".join(html)
    for a, b in trocas:
        assert a in s, a; s = s.replace(a, b)
    return s


FIM_REF = re.compile(r"^(.{0,360}?(?:Acesso em: ?\d{1,2} ?[a-zç]{3,4}\.? ?\d{4}|(?:1[89]|20)\d\d)(?: ?\((?:adaptado|fragmento)\))?\.)\s+(?=[A-ZÀ-Ú“])")
INICIO_REF = re.compile(r"^(Disponível em|Acesso em|[A-ZÀ-Ú][A-ZÀ-Ú'\-]+(?: [A-ZÀ-Ú'\-]+)*, [A-ZÀ-Ú]|[A-ZÀ-Ú][a-zà-ú]+ [A-ZÀ-Ú][a-zà-ú]+, (?:jun|jan|fev|mar|abr|mai|jul|ago|set|out|nov|dez))")


def paragrafos_enem(q):
    """Paragrafos do rascunho com as referências separadas do comando e títulos curtos reconhecidos.
    Devolve lista [tipo, texto] com tipos 'titulo', 'p', 'fonte', 'fig'."""
    par = []
    for t, x in q["paragrafos"]:
        if t != "fig" and isinstance(x, str) and not x.strip(): continue        # parágrafo vazio (rodapé removido)
        # quebra de coluna no meio da frase: junta com o parágrafo anterior
        if par and t == "p" and par[-1][0] == "p" and isinstance(x, str) and x[:1].islower() and not re.search(r"[.:;?!]$", par[-1][1]):
            par[-1][1] += " " + x; continue
        if par and t == "p" and par[-1][0] == "p" and isinstance(x, str) and x.startswith("•") and par[-1][1].lstrip().startswith("•"):
            par[-1][1] += "<br>" + x; continue                # lista com marcadores: um bloco só
        par.append([t, x])
    out = []
    for i, (t, x) in enumerate(par):
        if t == "p" and isinstance(x, str):
            ant = out[-1][0] if out else None
            m = FIM_REF.match(x)
            if m and (ant == "fonte" or INICIO_REF.match(x)):
                ref, resto = m.group(1), x[m.end():]
                if ant == "fonte": out[-1][1] += " " + ref
                else: out.append(["fonte", ref])
                x = resto
            elif INICIO_REF.match(x) and i == len(par) - 1 and m is None and ant != "fonte":
                pass
        if t == "p" and isinstance(x, str) and len(x) < 75 and not re.search(r"[.:;?!,]$", x) and i < len(par) - 1 and not x.startswith("•"):
            if out and out[-1][0] == "titulo": out[-1][1] += " " + x
            else: out.append(["titulo", x])
            continue
        out.append([t, x])
    return out


def enunciado_enem(q, trocas=(), tit_tag="strong"):
    par = paragrafos_enem(q)
    ult = max([i for i, (t, _) in enumerate(par) if t == "fonte"], default=-1)
    h = []
    for i, (t, x) in enumerate(par):
        if t == "fig": h.append(f"[[fig:{x}]]")
        elif t == "fonte": h.append(f'<p class="fonte">{x}</p>')
        elif t == "titulo": h.append(f'<p class="apoio"><{tit_tag}>{x}</{tit_tag}></p>' if i < ult else f"<p><{tit_tag}>{x}</{tit_tag}></p>")
        elif i < ult: h.append(f'<p class="apoio">{x}</p>')
        else: h.append(f"<p>{x}</p>")
    s = "".join(h)
    for a, b in trocas:
        assert a in s, a; s = s.replace(a, b)
    return s
