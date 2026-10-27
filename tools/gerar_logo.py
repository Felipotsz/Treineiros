#!/usr/bin/env python3
"""Gera o logo do Treineiros: "treineiros" em Alegreya ExtraBold, com os pingos dos "i"
trocados por gotas de tinta caindo da ponta de uma caneta-tinteiro.

Só é preciso rodar de novo para mudar o desenho:
  pip install fonttools
  python3 tools/gerar_logo.py
Saídas: assets/logo.svg (claro), assets/logo-noturno.svg e js/logo.js (usa as cores do tema).
"""
import pathlib
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

RAIZ = pathlib.Path(__file__).resolve().parent.parent
FONTE = RAIZ / "assets/fonts/playfair-display-800.woff2"
TAM, BASE = 100, 100
TEXTO = "treıneıros"           # ı = "i" sem pingo


def f(n):
    return f"{n:.2f}".rstrip("0").rstrip(".")


def gota(cx, cy, r):
    """Gota com a ponta para cima; (cx, cy) é o centro da parte redonda."""
    return (f"M{f(cx)},{f(cy - r*2.1)}C{f(cx + r*.35)},{f(cy - r*1.3)} {f(cx + r)},{f(cy - r*.6)} {f(cx + r)},{f(cy)}"
            f"A{f(r)},{f(r)} 0 0 1 {f(cx - r)},{f(cy)}C{f(cx - r)},{f(cy - r*.6)} {f(cx - r*.35)},{f(cy - r*1.3)} {f(cx)},{f(cy - r*2.1)}Z")


# Pena da caneta-tinteiro com a ponta em (0,0), apontando para baixo; respiro e fenda vazados (evenodd)
PENA = ("M-9,-34L9,-34L9,-26C9,-17 4,-8 0,0C-4,-8 -9,-17 -9,-26Z"
        "M-1.9,-22.5a1.9,1.9 0 1,0 3.8,0a1.9,1.9 0 1,0 -3.8,0Z"
        "M-.55,-20.4L.55,-20.4L.3,-3L-.3,-3Z")


def main():
    fonte = TTFont(FONTE)
    escala = TAM / fonte["head"].unitsPerEm
    cmap, glifos, larguras = fonte.getBestCmap(), fonte.getGlyphSet(), fonte["hmtx"]
    x, partes, hastes = 0.0, [], []
    for ch in TEXTO:
        nome = cmap[ord(ch)]
        pen = SVGPathPen(glifos)
        glifos[nome].draw(TransformPen(pen, (escala, 0, 0, -escala, x, BASE)))   # y da fonte cresce para cima
        partes.append(pen.getCommands())
        if ch == "ı":
            from fontTools.pens.boundsPen import BoundsPen
            bp = BoundsPen(glifos); glifos[nome].draw(bp)
            x1, _, x2, y2 = bp.bounds
            hastes.append(((x + (x1 + x2) / 2 * escala), BASE - y2 * escala))
        x += larguras[nome][0] * escala
    largura = x

    r = 6.2
    enfeites = []
    for i, (cx, topo) in enumerate(hastes):
        cy = topo - 13                                   # gota no lugar do pingo
        ty = cy - r * 2.1 - 7                            # ponta da pena logo acima da gota
        inclina = -18 if i == 0 else 14                  # canetas inclinadas em sentidos opostos
        enfeites.append(f'<path class="logo-pena" fill-rule="evenodd" transform="translate({f(cx)} {f(ty)}) rotate({inclina})" d="{PENA}"/>'
                        f'<path class="logo-tinta" d="{gota(cx, cy, r)}"/>')
    topo = min(t for _, t in hastes) - 13 - r * 2.1 - 7 - 38
    vb = f"-4 {f(topo)} {f(largura + 8)} {f(BASE + 26 - topo)}"
    corpo = f'<path class="logo-letras" d="{"".join(partes)}"/>' + "".join(enfeites)

    def solto(letras, tinta, pena):
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="Treineiros">'
                f"<style>.logo-letras{{fill:{letras}}}.logo-tinta{{fill:{tinta}}}.logo-pena{{fill:{pena}}}</style>{corpo}</svg>\n")
    (RAIZ / "assets/logo.svg").write_text(solto("#2D2723", "#7A2E22", "#9C7228"), encoding="utf-8")
    (RAIZ / "assets/logo-noturno.svg").write_text(solto("#EADCC0", "#C0503E", "#D4AC5E"), encoding="utf-8")
    (RAIZ / "js/logo.js").write_text(
        "/* Logo do Treineiros (gerado por tools/gerar_logo.py; não edite à mão). As cores vêm de .logo em css/components.css. */\n"
        f"var LOGO_SVG = '<svg class=\"logo\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"{vb}\" aria-hidden=\"true\" focusable=\"false\">{corpo}</svg>';\n",
        encoding="utf-8")
    print("logo gerado, viewBox", vb)


if __name__ == "__main__":
    main()
