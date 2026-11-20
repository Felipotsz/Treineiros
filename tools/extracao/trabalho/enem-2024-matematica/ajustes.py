# Enem 2024, 2º dia, caderno azul: Matemática (questões 136 a 180 do caderno; no site, 1 a 45, com numeroOriginal).
# Texto dos blocos do PDF; frações, potências e fórmulas reescritas em KaTeX a partir do caderno; alternativas-imagem nas Q161, 168, 174.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, enunciado_enem, paragrafos_enem

ID = "enem-2024-matematica"
META = {"id": ID, "banca": "Enem", "ano": 2024, "titulo": "Enem 2024: Matemática", "fonte": "Inep", "dataExame": "2024-11-10",
        "duracaoMinutos": 150, "area": "Matemática", "caderno": "azul", "dia": 2}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2024-dia2-azul")
Q = {}
P = lambda n: paragrafos_enem(D[n])
p = lambda *xs: "".join(f"<p>{x}</p>" for x in xs)
ap = lambda *xs: "".join(f'<p class="apoio">{x}</p>' for x in xs)
fonte = lambda x: f'<p class="fonte">{x}</p>'
K = lambda s: f"\\({s}\\)"
FR = lambda a, b: K(f"\\dfrac{{{a}}}{{{b}}}")
LISTA = lambda s, cls="apoio": f'<ul class="{cls}">' + "".join(f"<li>{x.strip()}</li>" for x in re.split(r"•|<br>", s) if x.strip()) + "</ul>"


def figs(*pares):
    return [{"arquivo": a, "alt": t} for a, t in pares]


def tabela(cab, linhas):
    return ('<table class="tabela"><thead><tr>' + "".join(f"<th>{c}</th>" for c in cab) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in l) + "</tr>" for l in linhas) + "</tbody></table>")


def X(n, assunto, expl, imagens=(), tags=(), enun=None, trocas=(), alts=None):
    Q[n - 135] = {"materia": "Matemática", "assunto": assunto, "area": "Matemática", "tags": list(tags), "numeroOriginal": n,
                  "enunciado": enun or enunciado_enem(D[n], trocas), "alternativas": dict(alts or D[n]["alternativas"]),
                  "imagens": list(imagens), "explicacao": expl}


X(136, "Razão e proporção", "<p>O olho enxerga no mínimo 100 µm = 0,1 mm. A hemácia mede 0,007 mm, então a ampliação total precisa ser de pelo menos 0,1 ÷ 0,007 ≈ 14,3 vezes. Com a ocular de 10×, a objetiva deve ampliar pelo menos 1,43×. A menor que atende é a de 2× (lente I): 10 · 2 = 20 vezes. Alternativa <strong>A</strong>.</p><p>A lente V (1,4×) dá só 14×, pouco abaixo do necessário; II e III também funcionam, mas ampliam mais que o preciso.</p>",
  figs(("q136", "Desenho de um microscópio óptico, com a lente ocular no alto e as lentes objetivas em um disco giratório acima da platina.")),
  ["escala", "micrômetro"], enun=ap(P(136)[0][1].replace("10-3 milímetros", "10<sup>−3</sup> milímetro")) + LISTA(P(136)[1][1]) + "[[fig:1]]" + ap(P(136)[3][1], P(136)[4][1]) + p(P(136)[5][1]))
X(137, "Média", "<p>Se S é a soma das notas, a média certa é S/4, e a errada, S/5. A diferença é 1: S/4 − S/5 = S/20 = 1, logo S = 20. A média correta é 20 ÷ 4 = <strong>5</strong>. Alternativa <strong>B</strong>.</p><p>4 (A) é a média errada; 20 (perto de D e E) é a soma das notas.</p>",
  tags=["equação do 1º grau"])
X(138, "Análise combinatória", "<p>Algarismos: 5 teclas (1, 2, 5, 7 e 0), dois distintos em ordem: 5 · 4 = 20. Letras: as teclas 1 e 0 não têm letras; 2 tem A, B, C; 5 tem J, K, L; 7 tem P, Q, R, S. São 10 letras, três diferentes em ordem: 10 · 9 · 8 = 720. Total: 20 · 720 = <strong>14 400</strong>. Alternativa <strong>B</strong>.</p><p>Permitir algarismos repetidos dá 25 · 720 = 18 000 (C).</p>",
  figs(("q138", "Teclado alfanumérico de telefone: 1; 2 ABC; 3 DEF; 4 GHI; 5 JKL; 6 MNO; 7 PQRS; 8 TUV; 9 WXYZ; *, 0 e #.")),
  ["princípio multiplicativo"])
X(139, "Operações", "<p>Cada enfeite usa 2 X e 1 Y. Loja I: 2 · 3,00 + 1,00 = R$ 7,00. Loja II: 2 · 2,00 + 4,00 = R$ 8,00. A loja I é mais barata, <strong>R$ 7,00</strong>. Alternativa <strong>A</strong>.</p><p>B soma um X e um Y; C esquece que são dois X; D e E escolhem pelo preço de um componente só.</p>",
  tags=["custo"], enun=ap(P(139)[0][1]) + tabela(["Loja", "Componente X (R$)", "Componente Y (R$)"], [["I", "3,00", "1,00"], ["II", "2,00", "4,00"]]) + ap(P(139)[2][1]) + p(P(139)[3][1]))
X(140, "Porcentagem", "<p>João acertou 75% de 200 = 150 questões: conceito “muito bom” (75 ≤ P &lt; 90). Felipe acertou 30% a menos que 150: 150 · 0,7 = 105 questões, ou 105 ÷ 200 = 52,5%: “regular”. Alternativa <strong>B</strong>.</p><p>Subtrair 30 pontos percentuais (75 − 30 = 45%) daria “insatisfatório” (C), mas o texto fala em 30% a menos da quantidade de João.</p>",
  tags=["porcentagem de porcentagem"], enun=ap(P(140)[0][1]) + LISTA(P(140)[1][1].replace("<", "&lt;")) + p(P(140)[2][1], P(140)[3][1]))
X(141, "Funções", "<p>Pelo primeiro gráfico, quando I vai de 1 a 3, II vai de 1,5 (em I = 1) a 3 (em I = 2) e a 3,5 (em I = 3). Pelo segundo, com II entre 1,5 e 3,5, III vale 2,5 em II = 1,5, cai até 1 em II = 3 e sobe a 2 em II = 3,5. O máximo é <strong>2,5</strong>. Alternativa <strong>B</strong>.</p><p>4,0 (E) é o máximo de III no gráfico todo, que exigiria II = 0, fora do intervalo.</p>",
  figs(("q141", "Dois gráficos de segmentos de reta. Grandeza II em função da I: passa por (0, 0), (2, 3) e (4, 4). Grandeza III em função da II: passa por (0, 4), (3, 1) e (4, 3).")),
  ["composição de funções", "leitura de gráfico"])
X(142, "Sequências", "<p>Na 1ª etapa há 3 figuras, e cada etapa dobra a anterior: 3, 6, 12, … Na etapa n há 3 · 2<sup>n−1</sup> figuras. Na 20ª: <strong>3 · 2<sup>19</sup></strong>. Alternativa <strong>A</strong>.</p><p>3 · 2<sup>20</sup> (B) conta uma duplicação a mais.</p>",
  figs(("q142", "Quadro com as etapas. 1ª: inseriu três figuras de carinha no visor (3 carinhas). 2ª: copiou o que havia e colou (6 carinhas). 3ª: copiou o que tinha na 2ª etapa e colou ao lado (12 carinhas).")),
  ["progressão geométrica"], alts={"A": K("3 \\times 2^{19}"), "B": K("3 \\times 2^{20}"), "C": K("3 \\times 2^{21}"), "D": K("3 \\times 2^{20} - 1"), "E": K("3 \\times 2^{20} - 3")})
X(143, "Porcentagem", "<p>Previsão: 60% de meias. Real: 50% a mais, ou 90% de 500 = 450 meias e 50 inteiras. Ingressos: 450 · 65 + 50 · 130 = 29 250 + 6 500 = R$ 35 750. Lucro com ingressos: 35 750 − 34 350 = R$ 1 400. Faltam 17 000 − 1 400 = R$ 15 600 de lucro com comida. Se o lucro é 60% do vendido, as vendas precisam somar 15 600 ÷ 0,6 = R$ 26 000, ou 26 000 ÷ 500 = <strong>R$ 52,00</strong> por pessoa. Alternativa <strong>D</strong>.</p>",
  tags=["lucro", "porcentagem"])
X(144, "Geometria espacial", "<p>Girando o trapézio retângulo em torno do lado PS (perpendicular às bases), as bases PQ e SR descrevem dois círculos de raios diferentes, e o lado inclinado QR descreve uma superfície lateral cônica: o sólido é um <strong>tronco de cone</strong>. Alternativa <strong>D</strong>.</p><p>Só um retângulo daria cilindro (B), e um triângulo retângulo, cone (A); sólidos de revolução nunca são pirâmides (C e E).</p>",
  figs(("q144", "Trapézio retângulo PQRS azul preso pelo lado vertical PS a uma vareta; Q fica em cima à esquerda de P e R embaixo, mais à esquerda; uma seta indica o giro em torno da vareta.")),
  ["sólidos de revolução"], enun=ap(P(144)[0][1]) + LISTA(P(144)[1][1]) + ap(P(144)[2][1]) + "[[fig:1]]" + p(P(144)[4][1]))
X(145, "Geometria plana", "<p>Área antiga: 110 · 75 = 8 250 m<sup>2</sup>. Nova: 105 · 68 = 7 140 m<sup>2</sup>. Redução: <strong>1 110 m<sup>2</sup></strong>. Alternativa <strong>D</strong>.</p><p>Subtrair as dimensões (5 · 7 = 35) dá B; somar as diferenças, 12.</p>",
  tags=["área do retângulo"], alts={k: v for k, v in D[145]["alternativas"].items()})
X(146, "Funções", "<p>Os dois lados L custam 2 · 20L = 40L, e os dois lados C, 2 · 15C = 30C. Com o gasto máximo: 40L + 30C = 6 000. A área LC é máxima quando o dinheiro se divide igualmente entre os dois tipos de lado: 40L = 30C = 3 000, logo L = 75 m e C = 100 m. Conferindo: A = L · (6 000 − 40L)/30 é uma parábola com vértice em L = 75. O maior lado mede <strong>100 m</strong>. Alternativa <strong>B</strong>.</p>",
  tags=["função quadrática", "máximo"], trocas=[("comprimentos L metro e C metro", "comprimentos <em>L</em> metro e <em>C</em> metro"), ("comprimento L metro", "comprimento <em>L</em> metro")])
X(147, "Números racionais", "<p>Valores: I) 4<sup>1/2</sup> = √4 = 2; II) 4½ = 4,5; III) 10/45 ≈ 0,22; IV) 18/4 = 4,5; V) 4,5; VI) 4/5 = 0,8. As três quantidades iguais estão em <strong>II, IV e V</strong>. Alternativa <strong>B</strong>.</p><p>Confundir 4<sup>1/2</sup> (potência) com 4½ (número misto) leva a incluir a posição I (A).</p>",
  figs(("q147", "Máquina caça-números com o título “Encontre três quantidades iguais” e seis compartimentos: I) 4 elevado a 1/2; II) quatro e meio; III) 10/45; IV) 18/4; V) 4,5; VI) 4/5.")),
  ["potência de expoente fracionário", "frações"])
X(148, "Funções", "<p>Em t = 0, T = 100: a + 80 · b<sup>0</sup> = a + 80 = 100, logo <strong>a = 20</strong>. No gráfico, em t = 10 a temperatura é 60 °C: 20 + 80 · b<sup>10</sup> = 60, então b<sup>10</sup> = 0,5 e <strong>b = (0,5)<sup>1/10</sup></strong>. Alternativa <strong>C</strong>.</p><p>a = 100 (B) seria a temperatura inicial, não a de equilíbrio; b = 40 (E) não é uma base de decaimento (precisa estar entre 0 e 1).</p>",
  figs(("q148", "Gráfico “Temperatura da caneca (em grau Celsius)” × tempo (em minuto), de 0 a 20: a curva começa em 100 °C, passa por 60 °C em t = 10 e chega a cerca de 40 °C em t = 20, decrescendo cada vez mais devagar.")),
  ["função exponencial"], enun=p(P(148)[0][1].replace("T(t) = a + 80 bt", K("T(t) = a + 80\\, b^{t}")).replace("temperatura T,", "temperatura <em>T</em>,").replace("tempo t,", "tempo <em>t</em>,")) + "[[fig:1]]" + p("Os valores das constantes <em>a</em> e <em>b</em> são"),
  alts={"A": K("a = 20;\\ b = \\log(0{,}5)"), "B": K("a = 100;\\ b = 0{,}5"), "C": K("a = 20;\\ b = (0{,}5)^{\\frac{1}{10}}"), "D": K("a = 20;\\ b = \\dfrac{(40)^{\\frac{1}{10}}}{80}"), "E": K("a = 20;\\ b = 40")})
X(149, "Geometria espacial", "<p>Volume do cilindro: π r<sup>2</sup> h = 3 · 9 · 15 = 405 cm<sup>3</sup>. O cubo terá 80%: 0,8 · 405 = 324 cm<sup>3</sup>. Aresta: ∛324 = ∛(27 · 12) = <strong>3∛12</strong> cm. Alternativa <strong>E</strong>.</p><p>6∛6 (D) seria ∛1 296; 6√6 (C) confunde raiz cúbica com quadrada.</p>",
  tags=["volume", "raiz cúbica"], alts={"A": "6", "B": "18", "C": K("6\\sqrt{6}"), "D": K("6\\sqrt[3]{6}"), "E": K("3\\sqrt[3]{12}")})
X(150, "Geometria plana", "<p>As colunas ficam numa linha de 3 m = 300 cm, com vãos de no máximo 15 cm entre colunas e nas paredes. Com n colunas de diâmetro d, há n + 1 vãos: n · d + 15(n + 1) ≥ 300.</p><ul><li>I (d = 10): 25n ≥ 285, n = 12, custo 12 · 60 = R$ 720;</li><li>II (d = 20): 35n ≥ 285, n = 9, R$ 630;</li><li>III (d = 24): 39n ≥ 285, n = 8, <strong>R$ 600</strong>;</li><li>IV (d = 30): 45n ≥ 285, n = 7, R$ 630;</li><li>V (d = 40): 55n ≥ 285, n = 6, R$ 720.</li></ul><p>Alternativa <strong>C</strong>.</p>",
  figs(("q150", "Planta da sala retangular, de 6 m por 3 m, com uma fileira de colunas circulares azuis atravessando a sala no meio, paralela aos lados de 3 m, e portas desenhadas na parede de baixo.")),
  ["círculo", "otimização"], enun=ap(P(150)[0][1]) + "[[fig:1]]" + ap(P(150)[2][1]) + tabela(["Loja", "Raio (cm)", "Preço por unidade (R$)"], [["I", 5, 60], ["II", 10, 70], ["III", 12, 75], ["IV", 15, 90], ["V", 20, 120]]) + p(P(150)[5][1], P(150)[6][1]))
X(151, "Escala", "<p>Na escala 1 : 200, as áreas ficam divididas por 200<sup>2</sup> = 40 000. 1 672 m<sup>2</sup> ÷ 40 000 = 0,0418 m<sup>2</sup>, e como 1 m<sup>2</sup> = 10 000 cm<sup>2</sup>, são <strong>418 cm<sup>2</sup></strong>. Alternativa <strong>E</strong>.</p><p>Dividir só por 200 (escala linear) leva a valores errados, como 8,36 (B).</p>",
  tags=["escala de áreas"], trocas=[("1 672 m2", "1 672 m<sup>2</sup>")])
X(152, "Estatística", "<p>Saldo = exportações − importações. Junho de 2009: cerca de 14,5 − 10 = 4,5. Janeiro de 2010: as linhas quase se encontram, com importações um pouco acima (saldo próximo de zero ou negativo). Junho de 2010: 17,1 − 14,8 = 2,3. Do maior para o menor: <strong>S<sub>1</sub>, S<sub>3</sub>, S<sub>2</sub></strong>. Alternativa <strong>A</strong>.</p><p>Quem olha só o valor das exportações coloca S<sub>3</sub> em primeiro (D e E).</p>",
  figs(("q152", "Gráfico de linhas “Valor total de exportações e importações”, em bilhão de dólares, de junho de 2009 a junho de 2010. Em junho de 2009, exportações perto de 14,5 e importações perto de 10. Em janeiro de 2010, as duas linhas quase se tocam, perto de 11,5, com exportações um pouco abaixo. Em junho de 2010, exportações em 17,1 e importações em 14,8.")),
  ["balança comercial", "leitura de gráfico"], enun=ap(P(152)[0][1]) + "[[fig:1]]" + fonte(P(152)[3][1]) + p(P(152)[4][1]) + LISTA(P(152)[5][1].replace("S1", "S<sub>1</sub>").replace("S2", "S<sub>2</sub>").replace("S3", "S<sub>3</sub>"), "lista") + p(P(152)[6][1].replace("S1, S2 e S3", "S<sub>1</sub>, S<sub>2</sub> e S<sub>3</sub>")),
  alts={k: re.sub(r"S(\d)", r"S<sub>\1</sub>", v) for k, v in D[152]["alternativas"].items()})
X(153, "Porcentagem", "<p>Porcentagem é divisão por 100: 135,25% = 135,25 ÷ 100 = <strong>1,3525</strong>. Alternativa <strong>D</strong>.</p><p>135,25 (B) é o número sem a divisão; 13,525 e 0,13525 (C e E) dividem por 10 e por 1 000.</p>",
  tags=["taxa percentual"])
X(154, "Média", "<p>Média: (36 + 17 + 27 + 13 + 13 + 13) ÷ 6 = 119 ÷ 6 ≈ <strong>19,8 min</strong>. Alternativa <strong>C</strong>.</p><p>13 (A) é a moda; 15 (B), a mediana (média de 13 e 17). 23,3 (E) é a média só dos três primeiros serviços.</p><p>A média é muito puxada pelo serviço A (36 min), bem acima dos demais.</p>",
  tags=["média aritmética"], enun=ap(P(154)[0][1], P(154)[1][1]) + tabela(["Tipo de serviço", "Tempo de leitura (min)"], [["A", 36], ["B", 17], ["C", 27], ["D", 13], ["E", 13], ["F", 13]]) + fonte(P(154)[3][1]) + p(P(154)[4][1]))
X(155, "Geometria plana", "<p>Área do setor: (α/360) · π R<sup>2</sup>, com π = 3:</p><ul><li>I: (15/360) · 3 · 400 = 50 m<sup>2</sup>;</li><li>II: (30/360) · 3 · 484 = 121 m<sup>2</sup>;</li><li>III: (40/360) · 3 · 144 = 48 m<sup>2</sup>;</li><li>IV: (60/360) · 3 · 256 = 128 m<sup>2</sup>;</li><li>V: (90/360) · 3 · 100 = 75 m<sup>2</sup>.</li></ul><p>Cobrem pelo menos 70 m<sup>2</sup> os tipos II, IV e V. Como o preço cresce com a área, o mais barato é o de menor área entre eles: o <strong>tipo V</strong>. Alternativa <strong>E</strong>.</p>",
  figs(("q155", "Vista superior: um setor circular azul com vértice no sensor S, raio R e ângulo α.")),
  ["setor circular"], enun=ap(P(155)[0][1].replace("ângulo α", "ângulo <em>α</em>").replace("raio R", "raio <em>R</em>")) + "[[fig:1]]" + ap(P(155)[2][1], P(155)[3][1]) + LISTA(P(155)[4][1]) + p(P(155)[5][1].replace("70 m2", "70 m<sup>2</sup>"), P(155)[6][1]))
X(156, "Funções", "<p>Valor = parte fixa + R$ 0,26 por minuto + R$ 1,40 por quilômetro: <strong>V = 2,00 + 0,26T + 1,40D</strong>. Alternativa <strong>B</strong>.</p><p>A multiplica a tarifa fixa por F; C esquece o preço do quilômetro; D esquece a tarifa fixa; E não usa os valores.</p>",
  tags=["função afim"], enun=ap(P(156)[0][1]) + LISTA(P(156)[1][1]) + p(P(156)[2][1], P(156)[3][1]))
X(157, "Equações", "<p>Hoje, 5 porções custam 10 + 5 · 25 = R$ 135. Com a taxa nova: 15 + 5x = 135, logo 5x = 120 e x = <strong>R$ 24,00</strong>. Alternativa <strong>C</strong>.</p><p>A taxa de entrega subiu R$ 5,00 e esse valor foi diluído nas 5 porções: R$ 1,00 a menos em cada uma. Tirar ou somar os R$ 5,00 inteiros no preço da porção dá 20,00 (B) ou 30,00 (D).</p>",
  tags=["equação do 1º grau"])
X(158, "Operações", "<p>Para 20 ha são precisos 40 L do tipo A (20 ÷ 0,5) ou 50 L do tipo B (20 ÷ 0,4).</p><ul><li>Só A: 40 · 4,20 = R$ 168,00; como passa de 35 L, ganha a máscara.</li><li>Só B: 50 · 3,00 = 150,00 + máscara 12,50 = <strong>R$ 162,50</strong>.</li><li>Misto com 35 L de A (17,5 ha, máscara grátis) e o resto com B (2,5 ha = 6,25 L): 147,00 + 18,75 = R$ 165,75.</li></ul><p>O menor valor é R$ 162,50. Alternativa <strong>C</strong>.</p><p>150,00 (B) esquece a máscara; 147,00 (A) esquece os 2,5 ha restantes.</p>",
  figs(("q158", "Cartaz amarelo: “Promoção: compre pelo menos 35 litros de defensivos do tipo A e ganhe a máscara para aplicação. Defensivo tipo A: R$ 4,20/litro. Defensivo tipo B: R$ 3,00/litro. Máscara para aplicação: R$ 12,50”.")),
  ["custo mínimo"])
X(159, "Grandezas e medidas", "<p>O fluxo é proporcional à vazão (mL/s) e inversamente proporcional à área (cm<sup>2</sup>): φ = vazão ÷ área, com unidade (mL/s) ÷ cm<sup>2</sup> = <strong>mL/(cm<sup>2</sup> · s)</strong>. Alternativa <strong>C</strong>.</p><p>A e B multiplicam pela área em vez de dividir; D e E invertem a razão.</p>",
  tags=["unidades de medida"],
  enun=ap(P(159)[0][1]) + p(P(159)[1][1]),
  alts={"A": K("\\text{mL} \\cdot \\text{s} \\cdot \\text{cm}^2"), "B": K("\\dfrac{\\text{mL}}{\\text{s}} \\cdot \\text{cm}^2"), "C": K("\\dfrac{\\text{mL}}{\\text{cm}^2 \\cdot \\text{s}}"), "D": K("\\dfrac{\\text{cm}^2 \\cdot \\text{s}}{\\text{mL}}"), "E": K("\\dfrac{\\text{cm}^2}{\\text{mL} \\cdot \\text{s}}")})
X(160, "Razão e proporção", "<p>Primeira piscina: 2 500 000 ÷ 6 000 ≈ 416,7 min. A segunda deve encher em 20% a mais: 416,7 · 1,2 = 500 min. Vazão: 2 750 000 ÷ 500 = <strong>5 500 L/min</strong>. Alternativa <strong>D</strong>.</p><p>8 250 (A) e 7 920 (B) aumentam a vazão em vez do tempo.</p>",
  tags=["vazão"])
X(161, "Funções", "<p>A água cai num dos compartimentos laterais, o da divisória mais alta (H/2). Cada compartimento tem 1/3 da base, e o tanque inteiro enche em 12 h:</p><ul><li>o primeiro compartimento enche até H/2 (1/6 do tanque) em 2 h, e a maior altura sobe até H/2;</li><li>depois a água transborda e enche os outros compartimentos até H/4 e então até H/2 (mais 1/3 do tanque, 4 h), sem passar de H/2: a maior altura fica constante de 2 h a 6 h;</li><li>com tudo em H/2, o tanque enche por igual até H na metade restante do tempo (6 h), em linha reta.</li></ul><p>É o gráfico da Alternativa <strong>B</strong>: sobe até 2 h, fica parado até 6 h e volta a subir até 12 h.</p>",
  figs(("q161", "Tanque em forma de paralelepípedo, de comprimento L, com a entrada de abastecimento no teto, à direita. Dentro, dois anteparos verticais dividem a base em três partes de comprimento L/3; um deles tem altura H/4 e o outro, H/2, sendo H a altura do tanque."),
       ("q161a", "Alternativa A: maior altura sobe até 2 h, fica constante até 4 h e depois sobe em dois trechos de inclinações diferentes até 12 h."),
       ("q161b", "Alternativa B: maior altura sobe até 2 h, fica constante até 6 h e depois sobe em linha reta até 12 h."),
       ("q161c", "Alternativa C: maior altura sobe até 2 h, fica constante até 10 h e depois sobe rapidamente até 12 h."),
       ("q161d", "Alternativa D: valores em degraus, com a altura caindo entre 2 h e 4 h e depois saltando para o máximo, que fica constante até 12 h."),
       ("q161e", "Alternativa E: maior altura sobe, cai entre 2 h e 4 h, volta a subir de repente em 6 h e fica constante até 12 h.")),
  ["vazão", "gráficos de funções"], alts={k: f"[[fig:{i}]]" for i, k in enumerate("ABCDE", 2)},
  enun=ap(P(161)[0][1]) + "[[fig:1]]" + ap(P(161)[2][1]) + p(P(161)[3][1]))
X(162, "Progressões", "<p>As parcelas crescem sempre (acréscimo percentual fixo), então as de maio mais valiosas são as últimas. São 100 parcelas: os quatro meses a partir do mês da compra aparecem 9 vezes, e os demais, 8. O melhor é que maio esteja entre esses quatro e que a última parcela (a 100ª, a maior) caia em maio. A 100ª parcela ocorre 99 meses depois da 1ª, ou seja, 3 meses à frente no calendário: comprando em <strong>fevereiro</strong>, ela cai em maio. Alternativa <strong>A</strong>.</p>",
  tags=["progressão geométrica", "calendário"])
X(163, "Geometria plana", "<p>A correia tem dois segmentos retos de 15 cm, um arco na polia pequena e um arco na grande. Pela figura, o arco de contato na polia pequena (r = 4) corresponde a 150°, e na grande (R = 8), a 360° − 150° = 210°. Comprimentos, com π = 3: (150/360) · 2 · 3 · 4 = 10 cm e (210/360) · 2 · 3 · 8 = 28 cm. Total: 15 + 15 + 10 + 28 = <strong>68 cm</strong>. Alternativa <strong>D</strong>.</p><p>Usar meia volta em cada polia dá 30 + 12 + 24 = 66 cm (C).</p>",
  figs(("q163", "Duas polias: a menor, de centro A e raio r = 4 cm, à esquerda, com ângulo de 150° marcado; a maior, de centro B e raio R = 8 cm, à direita. Uma correia as envolve, com dois trechos retos tangentes de 15 cm.")),
  ["comprimento de arco"])
X(164, "Geometria plana", "<p>Os postos formam um triângulo equilátero de lado 10 km, e o hospital está à mesma distância dos três: é o circuncentro, que no triângulo equilátero coincide com o baricentro. A distância é 2/3 da altura: (2/3) · (10√3/2) = 10√3/3 = 10/√3 ≈ 5,77 km, <strong>entre 5 e 6</strong>. Alternativa <strong>C</strong>.</p><p>A altura inteira (≈ 8,66 km) cairia em E.</p>",
  figs(("q164", "Triângulo equilátero de vértices P₁ (em cima), P₂ (embaixo à direita) e P₃ (embaixo à esquerda), com lados de 10 km; no centro, o ponto H (hospital), ligado aos três vértices por segmentos marcados como iguais.")),
  ["triângulo equilátero", "circuncentro"], trocas=[("pontos P1, P2 e P3", "pontos P<sub>1</sub>, P<sub>2</sub> e P<sub>3</sub>")])
X(165, "Probabilidade", "<p>Com o sinal vermelho por t segundos a cada 60, a chance de pegar um sinal vermelho é t/60, e de pegar os dois, (t/60)<sup>2</sup>. Para dar 4/100: t/60 = 2/10, logo t = 12 s. Como hoje são 15 s, a redução é de <strong>3 s</strong>. Alternativa <strong>B</strong>.</p><p>Esquecer de tirar a raiz (t/60 = 4/100) dá t = 2,4 s e redução de 12,6 s (D).</p>",
  tags=["eventos independentes"],
  enun=ap(P(165)[0][1]) + p("O engenheiro de tráfego da prefeitura calculou a probabilidade de um ônibus encontrar cada um deles vermelho, obtendo " + FR(15, 60) + ". A partir daí, estabeleceu uma mesma redução na quantidade do tempo, em segundo, em que cada sinal ficará vermelho, de maneira que a probabilidade de um ônibus encontrar ambos os sinais vermelhos numa mesma viagem seja igual a " + FR(4, 100) + ", considerando os eventos independentes.", P(165)[3][1]))
X(166, "Razão e proporção", "<p>d(Q) = habitantes de Q ÷ área de Q = (h/2) ÷ (3a/4) = (h/a) · (1/2) · (4/3) = (2/3) · d(R). Alternativa <strong>E</strong>.</p><p>3/2 (D) inverte a razão; 1/2 e 3/4 (B e C) consideram só uma das duas mudanças.</p>",
  tags=["densidade demográfica", "frações"],
  enun=ap(P(166)[0][1], P(166)[1][1].replace("região R", "região <em>R</em>").replace("região Q", "região <em>Q</em>").replace("área de Q", "área de <em>Q</em>").replace("área de R", "área de <em>R</em>").replace("habitantes de Q", "habitantes de <em>Q</em>").replace("habitantes de R", "habitantes de <em>R</em>")) + p("A expressão que relaciona <em>d</em>(<em>Q</em>) e <em>d</em>(<em>R</em>) é"),
  alts={k: K(f"d(Q) = \\dfrac{{{a}}}{{{b}}}\\, d(R)") for k, (a, b) in zip("ABCDE", [(1, 4), (1, 2), (3, 4), (3, 2), (2, 3)])})
X(167, "Números racionais", "<p>4 5/6 − 3 1/2 = 29/6 − 7/2 = 29/6 − 21/6 = 8/6 ≈ 1,33, que com uma casa decimal fica <strong>1,3</strong>. Alternativa <strong>D</strong>.</p><p>1,0 (C) subtrai só as partes inteiras; ler as frações como decimais erradas (5/6 como 0,5, por exemplo) leva a valores como 1,0 ou 0,5.</p>",
  figs(("q167", "Dois celulares lado a lado com a diagonal da tela indicada: o celular 1, menor, com 3 1/2 polegadas, e o celular 2, maior, com 4 5/6 polegadas.")),
  ["números mistos"],
  enun=p("Atualmente, há telefones celulares com telas de diversos tamanhos e em formatos retangulares. Alguns deles apresentam telas medindo " + K("3\\tfrac{1}{2}") + " polegadas, com determinadas especificações técnicas. Além disso, em muitos modelos, com a inclusão de novas funções no celular, suas telas ficaram maiores, sendo muito comum encontrarmos atualmente telas medindo " + K("4\\tfrac{5}{6}") + " polegadas, conforme a figura.").replace("<p>", '<p class="apoio">') + "[[fig:1]]" + fonte(P(167)[4][1]) + p(P(167)[5][1]))
X(168, "Trigonometria", "<p>O amortecedor aprovado tem amplitude constante em cada trecho e menor no asfalto (os 9 primeiros minutos) do que na estrada de chão (de 9 a 20 min). O gráfico certo mostra ondas pequenas e iguais até 9 min e ondas maiores e iguais de 9 a 20 min. Alternativa <strong>A</strong>.</p><p>Os outros gráficos têm amplitude que varia dentro de um mesmo trecho, maior no asfalto que no chão, ou com a troca fora dos 9 min.</p>",
  figs(("q168a", "Alternativa A: senoide com amplitude pequena e constante até 9 min e amplitude maior e constante de 9 a 20 min."),
       ("q168b", "Alternativa B: senoide com amplitude que cresce e depois diminui ao longo do tempo."),
       ("q168c", "Alternativa C: senoide com amplitude que diminui aos poucos de 0 a 20 min."),
       ("q168d", "Alternativa D: senoide com amplitude que muda várias vezes, sem ficar constante em cada trecho."),
       ("q168e", "Alternativa E: senoide com amplitude constante nos 20 minutos, mudando só a frequência.")),
  ["funções trigonométricas", "amplitude"], alts={k: f"[[fig:{i}]]" for i, k in enumerate("ABCDE", 1)},
  enun=ap(P(168)[0][1], P(168)[1][1]) + p(P(168)[2][1]))
X(169, "Probabilidade", "<p>Há 25 padrões possíveis (deslocamentos de 1 a 25; o de 26 deixaria o texto igual). Errar na 1ª tentativa: 24/25. Errar na 2ª, eliminado o padrão já testado: 23/24. Acertar na 3ª: 1/23. Probabilidade: <strong>(24/25) · (23/24) · (1/23)</strong>. Alternativa <strong>E</strong>.</p><p>A e B somam em vez de multiplicar; C multiplica probabilidades de acertar; D não elimina as tentativas frustradas.</p>",
  tags=["probabilidade condicional", "criptografia"],
  enun=ap(P(169)[0][1]) + '<p class="apoio">Na tabela da Cifra de César, cada letra do texto original (A, B, C, …, Z) corresponde, no texto codificado, à letra três posições à frente (D, E, F, …, Z, A, B, C).</p>' + fonte(P(169)[4][1]) + ap(P(169)[5][1], P(169)[6][1]) + p(P(169)[7][1]),
  alts={"A": K("\\dfrac{1}{25} + \\dfrac{1}{25} + \\dfrac{1}{25}"), "B": K("\\dfrac{24}{25} + \\dfrac{23}{24} + \\dfrac{1}{23}"), "C": K("\\dfrac{1}{25} \\times \\dfrac{1}{24} \\times \\dfrac{1}{23}"), "D": K("\\dfrac{24}{25} \\times \\dfrac{23}{25} \\times \\dfrac{1}{25}"), "E": K("\\dfrac{24}{25} \\times \\dfrac{23}{24} \\times \\dfrac{1}{23}")})
X(170, "Logaritmos", "<p>E<sub>1</sub> é um décimo de E<sub>2</sub>, então E<sub>2</sub>/E<sub>1</sub> = 10 e log 10 = 1. M<sub>2</sub> − 6,9 = (2/3) · 1 ≈ 0,67, logo M<sub>2</sub> ≈ <strong>7,6</strong>. Alternativa <strong>C</strong>.</p><p>Inverter a razão (log 0,1 = −1) dá 6,2 (B).</p>",
  tags=["escala Richter"],
  enun=ap("Em uma região com grande incidência de terremotos, observou-se que dois terremotos ocorridos apresentaram magnitudes M<sub>1</sub> e M<sub>2</sub>, medidos segundo a escala Richter, e liberaram energias iguais a E<sub>1</sub> e E<sub>2</sub>, respectivamente. Entre os estudiosos do assunto, é conhecida uma expressão algébrica relacionando esses valores dada por") + ap(K("M_2 - M_1 = \\dfrac{2}{3} \\log\\left(\\dfrac{E_2}{E_1}\\right)")) + ap("Estudos mais abrangentes observaram que o primeiro terremoto apresentou a magnitude M<sub>1</sub> = 6,9 e a energia liberada foi um décimo da observada no segundo terremoto.") + p("O valor aproximado da magnitude M<sub>2</sub> do segundo terremoto, expresso com uma casa decimal, é igual a"))
X(171, "Geometria plana", "<p>Com perímetro k: triângulo de lado k/3, área (√3/4)(k/3)<sup>2</sup> = √3k<sup>2</sup>/36 ≈ 0,048k<sup>2</sup>; quadrado de lado k/4, área k<sup>2</sup>/16 = 0,0625k<sup>2</sup>; hexágono de lado k/6, área (3√3/2)(k/6)<sup>2</sup> = √3k<sup>2</sup>/24 ≈ 0,072k<sup>2</sup>. O maior é o <strong>hexágono</strong>, com √3k<sup>2</sup>/24. Alternativa <strong>A</strong>.</p><p>B esquece de dividir o lado por 6; E usa k como lado do triângulo.</p>",
  tags=["polígonos regulares", "área"],
  alts={"A": "hexágono regular, pois a área do jardim, em metro quadrado, será " + K("\\dfrac{k^2\\sqrt{3}}{24}") + ".", "B": "hexágono regular, pois a área do jardim, em metro quadrado, será " + K("\\dfrac{3k^2\\sqrt{3}}{2}") + ".",
        "C": "quadrado, pois a área do jardim, em metro quadrado, será " + K("\\dfrac{k^2}{16}") + ".", "D": "triângulo equilátero, pois a área do jardim, em metro quadrado, será " + K("\\dfrac{k^2\\sqrt{3}}{36}") + ".",
        "E": "triângulo equilátero, pois a área do jardim, em metro quadrado, será " + K("\\dfrac{k^2\\sqrt{3}}{4}") + "."})
X(172, "Razão e proporção", "<p>Os ônibus saem juntos de lados opostos e se aproximam a 250 + 150 = 400 m/min: encontram-se após 9 000 ÷ 400 = 22,5 min, quando A percorreu 250 · 22,5 = 5 625 m, ou 5 625/9 000 = 0,625 do percurso. As câmeras cobrem, em sequência, 1/5 (até 0,2), 3/10 (até 0,5), 1/10 (até 0,6), 1/10 (até 0,7) e 3/10 (até 1). O ponto 0,625 está entre 0,6 e 0,7: <strong>câmera IV</strong>. Alternativa <strong>D</strong>.</p>",
  figs(("q172", "Esquema do trajeto entre o terminal 1 (à esquerda) e o terminal 2 (à direita), com cinco câmeras (I a V) em sequência; cada triângulo azul mostra o trecho coberto por uma câmera, e os trechos se encostam uns nos outros.")),
  ["encontro de móveis", "frações"],
  enun=ap(P(172)[0][1]) + "[[fig:1]]" + ap(P(172)[2][1]) + '<ul class="apoio"><li>câmera I: ' + FR(1, 5) + " do percurso;</li><li>câmera II: " + FR(3, 10) + " do percurso;</li><li>câmera III: " + FR(1, 10) + " do percurso;</li><li>câmera IV: " + FR(1, 10) + " do percurso;</li><li>câmera V: " + FR(3, 10) + " do percurso.</li></ul>" + ap(P(172)[4][1]) + p(P(172)[5][1]))
X(173, "Estatística", "<p>Pelo gráfico: administrativo 80 (20% até 25, 30% de 25 a 45, 50% acima de 45), logística 120 (25%, 40%, 35%) e produção 200 (40%, 35%, 25%). Contando:</p><ul><li>até 25: 16 + 30 + 80 = 126;</li><li>de 25 a 45: 24 + 48 + 70 = <strong>142</strong>;</li><li>a partir de 45: 40 + 42 + 50 = 132.</li></ul><p>A faixa de 25 a 45 anos tem mais funcionários, então é a mais provável. Alternativa <strong>A</strong>.</p><p>E soma porcentagens de grupos de tamanhos diferentes, o que não faz sentido; B, C e D usam critérios que não definem a probabilidade.</p>",
  figs(("q173", "Gráfico de barras empilhadas da quantidade de funcionários por setor. Administrativo, 80: 20% até 25 anos, 30% entre 25 e 45 e 50% a partir de 45. Logística, 120: 25%, 40% e 35%. Produção, 200: 40%, 35% e 25%.")),
  ["probabilidade", "gráfico de barras"])
X(174, "Geometria espacial", "<p>As duas paredes são perpendiculares à base, então todo ponto de uma parede se projeta sobre a reta onde essa parede encontra o chão. B e C estão na parede da esquerda; A, D e E, na da direita; F já está no chão.</p><ul><li>AB vai da borda direita até a borda esquerda;</li><li>BC é vertical, então se projeta num único ponto (B e C caem no mesmo lugar);</li><li>CD volta da borda esquerda para a direita;</li><li>DE está na parede da direita, mas não é vertical (D e E têm profundidades diferentes), e vira um segmento sobre a borda direita;</li><li>EF desce da borda direita até F, no chão.</li></ul><p>É o desenho da Alternativa <strong>C</strong>.</p><p>A e B mostram BC como segmento, o que só aconteceria se ele não fosse vertical; D e E não têm o segmento DE sobre a borda.</p>",
  figs(("q174", "Duas paredes verticais quadriculadas, paralelas, sobre uma base. A trajetória: A no alto da parede da direita, ao fundo; B e C na parede da esquerda, com C logo abaixo de B; D e E na parede da direita, E abaixo e à frente de D; F no chão, à frente."),
       ("q174a", "Alternativa A: projeção vista de cima com um retângulo no meio, ligando as bordas esquerda e direita por dois segmentos horizontais."),
       ("q174b", "Alternativa B: segmentos que vão à borda esquerda, voltam pela horizontal à borda direita, descem por ela e seguem em diagonal até embaixo."),
       ("q174c", "Alternativa C: do canto superior direito até um ponto da borda esquerda, de lá em diagonal até a borda direita, um segmento vertical sobre a borda direita e uma diagonal até a borda de baixo."),
       ("q174d", "Alternativa D: do canto superior direito à borda esquerda, um segmento horizontal até a borda direita e uma diagonal até embaixo."),
       ("q174e", "Alternativa E: do canto superior direito à borda esquerda, de lá em diagonal até a borda direita e outra diagonal até embaixo, sem segmento sobre a borda.")),
  ["projeção ortogonal", "geometria espacial"], alts={k: f"[[fig:{i}]]" for i, k in enumerate("ABCDE", 2)},
  enun=ap(P(174)[0][1]) + "[[fig:1]]" + p(P(174)[2][1]))
X(175, "Geometria espacial", "<p>A folha vira a superfície lateral: um lado é a altura, e o outro, o comprimento da circunferência da base (2πr).</p><ul><li>Embalagem 1: altura 20, 2πr = 10, r = 5/π, volume π(5/π)<sup>2</sup> · 20 = 500/π.</li><li>Embalagem 2: altura 10, 2πr = 20, r = 10/π, volume π(10/π)<sup>2</sup> · 10 = <strong>1 000/π</strong>.</li></ul><p>A maior é a 2. Alternativa <strong>D</strong>.</p><p>Usar 10 e 20 como diâmetro ou raio leva a A e B.</p>",
  figs(("q175", "Duas folhas retangulares de 10 cm por 20 cm enroladas em cilindros: na embalagem 1, o lado de 20 cm fica na vertical (cilindro alto e fino); na embalagem 2, o lado de 10 cm fica na vertical (cilindro baixo e largo).")),
  ["volume do cilindro"], enun=ap(P(175)[0][1]) + "[[fig:1]]" + p(P(175)[2][1]),
  alts={"A": K("4\\,000\\,\\pi"), "B": K("2\\,000\\,\\pi"), "C": K("\\dfrac{4\\,000}{\\pi}"), "D": K("\\dfrac{1\\,000}{\\pi}"), "E": K("\\dfrac{500}{\\pi}")})
X(176, "Funções", "<p>A reta de tendência passa exatamente por dois cruzamentos da grade: 4 em 2014 e 6 em 2020. Ela sobe 2 milhões em 6 anos, ou 1/3 de milhão por ano. De 2020 a 2026 são mais 6 anos: 6 + 6 · 1/3 = <strong>8 milhões</strong>. Alternativa <strong>B</strong>.</p><p>Usar os pontos (e não a reta) ou estender a reta até outro ano leva a valores diferentes.</p>",
  figs(("q176", "Gráfico da receita anual (em milhão de reais) de 2014 a 2021, com pontos espalhados entre cerca de 3,5 e 6,7 e uma reta de tendência crescente que passa perto de 4 em 2014 e de 6,4 em 2021.")),
  ["função afim", "reta de tendência"])
X(177, "Funções", "<p>Entre 30 e 50 mochilas, o custo sobe 1 650 − 1 050 = 600 em 20 unidades: R$ 30 por mochila. Custo fixo: 1 050 − 30 · 30 = R$ 150. Para 80 mochilas: 150 + 30 · 80 = <strong>R$ 2 550,00</strong>. Alternativa <strong>C</strong>.</p><p>Esquecer o custo fixo dá 2 400 (A).</p>",
  tags=["função afim"], enun=ap(P(177)[0][1]) + tabela(["Quantidade de mochilas", "Custo total (R$)"], [[30, "1 050,00"], [50, "1 650,00"], [100, "3 150,00"]]) + p(P(177)[2][1]))
X(178, "Estatística", "<p>Em ordem: 46, 54, 60, 64, 64, 66. Com seis valores, a mediana é a média dos centrais: (60 + 64) ÷ 2 = <strong>62</strong>. Alternativa <strong>E</strong>.</p><p>59 (C) é a média aritmética; 64 é a moda.</p>",
  tags=["mediana"], enun=ap(P(178)[0][1]) + tabela(["Mês", "Umidade relativa média (%)"], [["Maio", 66], ["Junho", 64], ["Julho", 54], ["Agosto", 46], ["Setembro", 60], ["Outubro", 64]]) + p(P(178)[2][1]))
X(179, "Razão e proporção", "<p>Total a dividir: 40% de 71 250 = R$ 28 500. Horas: I, 4 · 5,5 = 22; II, 5 · 4 = 20; III, 6 · 2,5 = 15; total 57 h. Cada hora vale 28 500 ÷ 57 = R$ 500. A maior diferença é entre I e III: (22 − 15) · 500 = <strong>R$ 3 500</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["divisão proporcional"], enun=ap(P(179)[0][1]) + LISTA(P(179)[1][1]) + p(P(179)[2][1]))
X(180, "Análise combinatória", "<p>“Pelo menos 3 cardiologistas” separa três casos: 3 cardiologistas e 2 neurologistas, 4 e 1, ou 5 e 0. Em cada caso, multiplicam-se as combinações, e os casos se somam: C(7,3)·C(6,2) + C(7,4)·C(6,1) + C(7,5)·C(6,0), que é a expressão da Alternativa <strong>E</strong>.</p><p>D multiplica os casos em vez de somar; B e C consideram só um caso ou somam as combinações de dentro de cada caso.</p>",
  tags=["combinação"],
  enun=p("Um hospital tem 7 médicos cardiologistas e 6 médicos neurologistas em seu quadro de funcionários. Para executar determinada atividade, a direção desse hospital formará uma equipe com 5 médicos, sendo, pelo menos, 3 cardiologistas.", "A expressão numérica que representa o número máximo de maneiras distintas de formar essa equipe é"),
  alts={"A": K("\\dfrac{7!}{4!} \\times \\dfrac{6!}{4!}"), "B": K("\\dfrac{7!}{3! \\times 4!} \\times \\dfrac{6!}{2! \\times 4!}"), "C": K("\\dfrac{7!}{3! \\times 4!} + \\dfrac{6!}{2! \\times 4!} + \\dfrac{5!}{1! \\times 4!}"),
        "D": K("\\left(\\dfrac{7!}{3!\\times4!} + \\dfrac{6!}{2!\\times4!}\\right) \\times \\left(\\dfrac{7!}{4!\\times3!} + \\dfrac{6!}{1!\\times5!}\\right) \\times \\left(\\dfrac{7!}{5!\\times2!} + \\dfrac{6!}{0!\\times6!}\\right)"),
        "E": K("\\left(\\dfrac{7!}{3!\\times4!} \\times \\dfrac{6!}{2!\\times4!}\\right) + \\left(\\dfrac{7!}{4!\\times3!} \\times \\dfrac{6!}{1!\\times5!}\\right) + \\left(\\dfrac{7!}{5!\\times2!} \\times \\dfrac{6!}{0!\\times6!}\\right)")})

completar(Q, R)
