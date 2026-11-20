# Enem 2013, 2º dia, caderno azul: Matemática (questões 136 a 180; no site, 1 a 45).
# Texto legível. Frações em KaTeX nas alternativas curtas; quadros em tabela HTML. Alternativas-imagem nas Q151, Q154, Q164 e Q180.
# Sem anuladas nesta área.

import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, paragrafos_enem

ID = "enem-2013-matematica"
META = {"id": ID, "banca": "Enem", "ano": 2013, "titulo": "Enem 2013: Matemática", "fonte": "Inep", "dataExame": "2013-10-27",
        "duracaoMinutos": 150, "area": "Matemática", "caderno": "azul", "dia": 2}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2013-dia2-azul")
Q = {}
P = lambda n: paragrafos_enem(D[n])
T = lambda n, i: P(n)[i][1]
p = lambda *xs: "".join(f"<p>{x}</p>" for x in xs)
fonte = lambda x: f'<p class="fonte">{x}</p>'
ALT = lambda ini: {k: f"[[fig:{i}]]" for i, k in enumerate("ABCDE", ini)}
FR = lambda *xs: {k: f"\\({v}\\)" for k, v in zip("ABCDE", xs)}
LISTA = lambda s: "<ul>" + "".join(f"<li>{x.strip()}</li>" for x in s.split("•") if x.strip()) + "</ul>"
ap = lambda *xs: "".join(f'<p class="apoio">{x}</p>' for x in xs)
tit = lambda x: f'<p class="apoio"><strong>{x}</strong></p>'
OL = lambda *xs: "<ol>" + "".join(f"<li>{x}</li>" for x in xs) + "</ol>"
LIMPA = lambda s: re.sub(r"fi ([a-zà-ú])", r"fi\1", re.sub(r"fl ([a-zà-ú])", r"fl\1", re.sub(r"(\w)- -(\w)", r"\1-\2", s)))


def figs(*pares):
    return [{"arquivo": a, "alt": t} for a, t in pares]


def tabela(cab, linhas):
    return ('<table class="tabela"><thead><tr>' + "".join(f"<th>{c}</th>" for c in cab) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in l) + "</tr>" for l in linhas) + "</tbody></table>")


def X(n, assunto, expl, imagens=(), tags=(), enun=None, alts=None, anulacao=None, trocas=()):
    q = {"materia": "Matemática", "assunto": assunto, "area": "Matemática", "tags": list(tags), "numeroOriginal": n,
         "enunciado": LIMPA(enun or p(*[x for t, x in P(n) if t == "p"])), "alternativas": {k: LIMPA(v) for k, v in dict(alts or D[n]["alternativas"]).items()},
         "imagens": list(imagens), "explicacao": expl}
    if anulacao: q["anulacao"] = anulacao
    for a, b in trocas:
        assert a in q["enunciado"], a; q["enunciado"] = q["enunciado"].replace(a, b)
    Q[n - 135] = q

K = lambda s: f"\\({s}\\)"
PP = lambda n: [x for t, x in P(n) if t == "p"]
F = lambda n, *figidx: None


def EF(n, antes, fig="[[fig:1]]", fnt=None, depois=None):
    """Parágrafos p antes da figura, figura, fonte opcional e o resto."""
    ps = PP(n)
    s = p(*ps[:antes]) + fig + (fonte(fnt) if fnt else "")
    return s + p(*(ps[antes:] if depois is None else depois))


X(136, "Trigonometria", "<p>A torre é um prisma oblíquo inclinado 15° em relação à vertical, com altura AB = 114 m. O deslocamento horizontal do topo é 114 · tg 15° = 114 · 0,26 = 29,64 m, que corresponde ao lado da base quadrada. A área é 29,64² ≈ 878,53 m², <strong>maior que 700 m²</strong>. Alternativa <strong>E</strong>.</p><p>Quem toma 29,64 como área, e não como lado, chega a uma das opções menores.</p>",
  figs(("q136", "Foto de uma das torres Puerta de Europa, em Madri: prédio de vidro inclinado, com o ponto A no topo e o ponto B na base, indicando a altura.")),
  ["tangente", "prisma oblíquo"], enun=p(T(136, 0)) + "[[fig:1]]" + fonte(T(136, 2)) + p(T(136, 3)),
  alts={"A": "menor que 100 m<sup>2</sup>.", "B": "entre 100 m<sup>2</sup> e 300 m<sup>2</sup>.", "C": "entre 300 m<sup>2</sup> e 500 m<sup>2</sup>.", "D": "entre 500 m<sup>2</sup> e 700 m<sup>2</sup>.", "E": "maior que 700 m<sup>2</sup>."})
X(137, "Estatística", "<p>As dez notas são 18, 16, 17, 13, 14, 1, 19, 14, 16 e 12, com soma 140 e média 14. Descartando a maior (19) e a menor (1), sobram 120 em 8 notas: média 15. A nova média é <strong>1,00 ponto maior</strong>. Alternativa <strong>B</strong>.</p><p>A nota 1, muito baixa, puxava a média para baixo.</p>",
  figs(("q137", "Gráfico de colunas “Notas (em pontos)”, com duas colunas por avaliador (conhecimentos específicos, em preto, e pedagógicos, em cinza): Avaliador A, 18 e 16; B, 17 e 13; C, 14 e 1; D, 19 e 14; E, 16 e 12.")),
  ["média aritmética", "leitura de gráfico"], enun=p(T(137, 0)) + "[[fig:1]]" + p(T(137, 2), T(137, 3)))
X(138, "Análise combinatória", "<p>No sistema antigo, cada um dos 6 dígitos tem 10 opções: 10<sup>6</sup> senhas. No novo, há 26 maiúsculas, 26 minúsculas e 10 algarismos, 62 símbolos, que podem se repetir: 62<sup>6</sup> senhas. O coeficiente é \\(\\dfrac{62^6}{10^6}\\). Alternativa <strong>A</strong>.</p><p>Os fatoriais (B e C) só valeriam se os símbolos não pudessem se repetir.</p>",
  tags=["princípio multiplicativo", "senhas"],
  alts=FR("\\dfrac{62^6}{10^6}", "\\dfrac{62!}{10!}", "\\dfrac{62!\\,4!}{10!\\,56!}", "62! - 10!", "62^6 - 10^6"))
X(139, "Grandezas e medidas", "<p>De meia-noite às seis são 6 h = 21 600 s. Com uma gota a cada 3 s, são 7 200 gotas, e 7 200 × 0,2 mL = 1 440 mL ≈ <strong>1,4 L</strong>. Alternativa <strong>C</strong>.</p><p>A opção B (1,2) seria o resultado arredondado para baixo ou com conta de tempo errada.</p>",
  tags=["conversão de unidades", "proporcionalidade"])
X(140, "Razão e proporção", "<p>Como só 90% do tipo B é aproveitado, o custo real por quilo aproveitado é o preço dividido por 0,9: arroz 1,70 ÷ 0,9 ≈ 1,89 (melhor que 2,00, então B); feijão 4,10 ÷ 0,9 ≈ 4,56 (pior que 4,50, então A); soja 3,50 ÷ 0,9 ≈ 3,89 (pior que 3,80, então A); milho 5,30 ÷ 0,9 ≈ 5,89 (melhor que 6,00, então B). A escolha é <strong>B, A, A, B</strong>. Alternativa <strong>D</strong>.</p>",
  tags=["custo-benefício", "porcentagem"],
  enun=p(T(140, 0)) + tabela(["Produto", "Tipo A", "Tipo B"], [["Arroz", "2,00", "1,70"], ["Feijão", "4,50", "4,10"], ["Soja", "3,80", "3,50"], ["Milho", "6,00", "5,30"]]) + p(T(140, 2)))
X(141, "Geometria plana", "<p>Os centros dos três canos formam um triângulo equilátero de lado 60 cm. A distância do centro do triângulo a cada vértice é \\(\\dfrac{60}{\\sqrt{3}} = 20\\sqrt{3} \\approx 34\\) cm. Somando o raio de um cano (30 cm) e o espaçador (10 cm): R = 34 + 30 + 10 = <strong>74 cm</strong>. Alternativa <strong>C</strong>.</p>",
  figs(("q141", "Três circunferências iguais, tangentes entre si, dentro de uma circunferência maior de raio R. O raio de uma das menores é 30 cm, e há um espaço de 10 cm entre ela e a maior.")),
  ["triângulo equilátero", "circunferências tangentes"], enun=p(T(141, 0)) + "[[fig:1]]" + p("Utilize 1,7 como aproximação para \\(\\sqrt{3}\\). O valor de <em>R</em>, em centímetros, é igual a"))
X(142, "Razão e proporção", "<p>O índice é (tempo de lactação × produção diária) ÷ intervalo entre partos: Malhada 360 × 12 ÷ 15 = 288; Mamona 310 × 11 ÷ 12 ≈ 284; Maravilha 260 × 14 ÷ 12 ≈ 303; Mateira 310 × 13 ÷ 13 = 310; Mimosa 270 × 12 ÷ 11 ≈ 295. A mais eficiente é a <strong>Mateira</strong>. Alternativa <strong>D</strong>.</p>",
  tags=["índices", "comparação"],
  enun=p(T(142, 0), T(142, 1)) + tabela(["Vaca", "Tempo de lactação (em dias)", "Produção média diária de leite (em kg)", "Intervalo entre partos (em meses)"],
    [["Malhada", "360", "12,0", "15"], ["Mamona", "310", "11,0", "12"], ["Maravilha", "260", "14,0", "12"], ["Mateira", "310", "13,0", "13"], ["Mimosa", "270", "12,0", "11"]]) + p(T(142, 5)))
X(143, "Escalas", "<p>Contando os lados de quadradinho percorridos no trajeto de casa até a escola, são 16 cm. Na escala 1 : 25 000, 1 cm vale 250 m, então a ida tem 16 × 250 = 4 000 m = 4 km. Ida e volta somam 8 km por dia; em cinco dias, <strong>40 km</strong>. Alternativa <strong>E</strong>.</p><p>A opção A (4) é só a ida de um dia.</p>",
  figs(("q143", "Malha quadriculada com quadrados de 1 cm de lado: o trajeto em escada, só com segmentos horizontais e verticais, vai da casa, no canto inferior esquerdo, até a escola, no canto superior direito; um ciclista aparece no caminho.")),
  ["escala", "distância"], enun=p(T(143, 0)) + "[[fig:1]]" + p(T(143, 3)))
X(144, "Porcentagem", "<p>O maior crescimento é o de Guarulhos (60,52%) e o menor, o de São Paulo capital (3,57%). A diferença é 60,52 − 3,57 = <strong>56,95</strong> pontos percentuais. Alternativa <strong>C</strong>.</p><p>A opção D (45,76) subtrai o estado de São Paulo, e não a capital, que tem o menor crescimento.</p>",
  figs(("q144", "Gráfico de colunas “Crescimento - Indústria”: Brasil, 30,95%; São Paulo (Estado), 14,76%; São Paulo (Capital), 3,57%; Guarulhos, 60,52%.")),
  ["leitura de gráfico", "porcentagem"], enun=p(T(144, 0), T(144, 1)) + "[[fig:1]]" + fonte(T(144, 6)) + p(T(144, 7)))
X(145, "Razão e proporção", "<p>O setor tem 7 fileiras de 10 cadeiras, 70 no total. Contando as escuras, são 17 reservadas. A razão é \\(\\dfrac{17}{70}\\). Alternativa <strong>A</strong>.</p><p>A opção B divide pelo número de cadeiras livres (53), e não pelo total.</p>",
  figs(("q145", "Vista do setor 3 de um teatro: 7 fileiras com 10 cadeiras cada; 17 cadeiras estão em preto (reservadas) e as demais em branco.")),
  ["razão", "contagem"], enun=p(T(145, 0)) + "[[fig:1]]" + p(T(145, 2)),
  alts=FR("\\dfrac{17}{70}", "\\dfrac{17}{53}", "\\dfrac{53}{70}", "\\dfrac{53}{17}", "\\dfrac{70}{17}"))
X(146, "Probabilidade", "<p>O produto A teve 10 + 30 + 60 = 100 compradores, 30 em fevereiro; o B teve 20 + 20 + 80 = 120, 20 em fevereiro. Os sorteios são independentes: \\(\\dfrac{30}{100} \\cdot \\dfrac{20}{120} = \\dfrac{3}{10} \\cdot \\dfrac{1}{6} = \\dfrac{1}{20}\\). Alternativa <strong>A</strong>.</p>",
  figs(("q146", "Gráfico de colunas do número de compradores: janeiro, A 10 e B 20; fevereiro, A 30 e B 20; março, A 60 e B 80.")),
  ["eventos independentes", "leitura de gráfico"], enun=p(T(146, 0)) + "[[fig:1]]" + p(T(146, 3), T(146, 4)),
  alts=FR("\\dfrac{1}{20}", "\\dfrac{3}{242}", "\\dfrac{5}{22}", "\\dfrac{6}{25}", "\\dfrac{7}{15}"))
X(147, "Geometria plana", "<p>Sem o lado do rio, a cerca mede 81 + 190 + 81 = 352 m. Com rolos de 48 m, são 352 ÷ 48 ≈ 7,33 rolos; como não se compra fração, são <strong>8 rolos</strong>. Alternativa <strong>C</strong>.</p><p>Arredondar para baixo (7, B) deixaria parte do terreno sem cerca.</p>",
  figs(("q147", "Terreno retangular com um lado de 190 m e os dois laterais de 81 m; o quarto lado é margeado por um rio.")),
  ["perímetro", "arredondamento"], enun=p(T(147, 0)) + "[[fig:1]]" + p(T(147, 2)))
X(148, "Razão e proporção", "<p>900 telhas são 900 ÷ 1 500 = 60% da carga máxima. Sobram 40%, que correspondem a 0,4 × 1 200 = <strong>480 tijolos</strong>. Alternativa <strong>D</strong>.</p><p>Subtrair os números diretamente (1 500 − 900 = 600, E) ignora que telhas e tijolos têm pesos diferentes.</p>",
  tags=["proporcionalidade", "frações"])
X(149, "Progressões", "<p>A produção cresce 1,25 t por ano: é uma progressão aritmética com a<sub>1</sub> = 50,25 e razão 1,25. Em 2021 (10º termo): 50,25 + 9 × 1,25 = 61,50. A soma é \\(\\dfrac{(50{,}25 + 61{,}50) \\cdot 10}{2} = \\) <strong>558,75 t</strong>. Alternativa <strong>D</strong>.</p>",
  tags=["progressão aritmética", "soma dos termos"],
  enun=p(T(149, 0)) + tabela(["Ano", "Projeção da produção (t)"], [["2012", "50,25"], ["2013", "51,50"], ["2014", "52,75"], ["2015", "54,00"]]) + p(T(149, 2)))
X(150, "Probabilidade", "<p>Falam pelo menos uma das línguas 1 200 − 300 = 900 alunos. Como 600 + 500 = 1 100, há 200 que falam as duas. Não falam inglês 600 alunos; desses, falam espanhol 500 − 200 = 300. A probabilidade é \\(\\dfrac{300}{600} = \\dfrac{1}{2}\\). Alternativa <strong>A</strong>.</p><p>A opção B (5/8) não desconta quem fala as duas línguas.</p>",
  tags=["probabilidade condicional", "conjuntos"],
  alts=FR("\\dfrac{1}{2}", "\\dfrac{5}{8}", "\\dfrac{1}{4}", "\\dfrac{5}{6}", "\\dfrac{5}{14}"))
X(151, "Geometria analítica", "<p>A circunferência x² + y² = 9 tem raio 3, então o “rosto” vai de −3 a 3. A parábola y = −x² − 1 tem concavidade para baixo e vértice em (0, −1): é a “boca triste”. Os quadrados ficam em cima, entre 1 e 2 no eixo y, e o ponto (0, 0) é o “nariz”. É a <strong>figura E</strong>. Alternativa <strong>E</strong>.</p><p>Em A e B o raio é 9, e em C e D a parábola está virada para cima.</p>",
  figs(("q151a", "Alternativa A: circunferência de raio 9 com dois quadradinhos perto do centro e uma curva voltada para baixo."),
       ("q151b", "Alternativa B: circunferência de raio 9 com dois quadradinhos e uma curva voltada para cima, como um sorriso."),
       ("q151c", "Alternativa C: circunferência de raio 3 com dois quadradinhos, um ponto no centro e uma curva voltada para cima abaixo dele."),
       ("q151d", "Alternativa D: circunferência de raio 3 com dois quadradinhos, um ponto e uma curva voltada para cima acima do ponto."),
       ("q151e", "Alternativa E: circunferência de raio 3 com dois quadradinhos acima, um ponto no centro e uma curva voltada para baixo, como uma boca triste.")),
  ["circunferência", "parábola"],
  enun=p(T(151, 0)) + "<ul><li>I — é a circunferência de equação <em>x</em><sup>2</sup> + <em>y</em><sup>2</sup> = 9;</li><li>II — é a parábola de equação <em>y</em> = −<em>x</em><sup>2</sup> − 1, com <em>x</em> variando de −1 a 1;</li><li>III — é o quadrado formado pelos vértices (−2, 1), (−1, 1), (−1, 2) e (−2, 2);</li><li>IV — é o quadrado formado pelos vértices (1, 1), (2, 1), (2, 2) e (1, 2);</li><li>V — é o ponto (0, 0).</li></ul>" + p(T(151, 6), T(151, 7)),
  alts=ALT(1))
X(152, "Funções", "<p>O vértice V está sobre o eixo x, então a parábola toca o eixo em um só ponto: o discriminante é zero. Δ = 36 − 4 · \\(\\tfrac{3}{2}\\) · C = 36 − 6C = 0, logo C = <strong>6</strong>. Alternativa <strong>E</strong>.</p><p>Outra forma: o vértice tem x = 6 ÷ 3 = 2, e f(2) = 6 − 12 + C = 0.</p>",
  figs(("q152", "Taça em perfil sobre um plano cartesiano: o interior tem forma de parábola com vértice V sobre o eixo x, no fundo da taça; o eixo de rotação z passa pelo meio; o líquido ocupa a parte de baixo, até a altura C no eixo y.")),
  ["função quadrática", "vértice"],
  enun=p(T(152, 0)) + "[[fig:1]]" + p("A função real que expressa a parábola, no plano cartesiano da figura, é dada pela lei \\(f(x) = \\dfrac{3}{2}x^2 - 6x + C\\), onde <em>C</em> é a medida da altura do líquido contido na taça, em centímetros. Sabe-se que o ponto <em>V</em>, na figura, representa o vértice da parábola, localizado sobre o eixo <em>x</em>.", T(152, 6)))
X(153, "Funções", "<p>“O cubo da área S é proporcional ao quadrado da massa M” significa S³ = k·M². Tirando a raiz cúbica dos dois lados: \\(S = k^{\\frac{1}{3}} \\cdot M^{\\frac{2}{3}}\\). Alternativa <strong>D</strong>.</p><p>A opção E esquece a raiz cúbica no expoente de M.</p>",
  tags=["potências", "proporcionalidade"], enun=p(T(153, 0)) + fonte(T(153, 1).replace("Cálculo e aplicações", "<em>Cálculo e aplicações</em>")) + p(T(153, 2)),
  alts=FR("S = k \\cdot M", "S = k \\cdot M^{\\frac{1}{3}}", "S = k^{\\frac{1}{3}} \\cdot M^{\\frac{1}{3}}", "S = k^{\\frac{1}{3}} \\cdot M^{\\frac{2}{3}}", "S = k^{\\frac{1}{3}} \\cdot M^{2}"))
X(154, "Funções", "<p>Em órbita circular, a distância de cada satélite à Terra não muda, então a força também não muda com o tempo: os gráficos são retas horizontais. Como os satélites têm a mesma massa, quem está mais perto sofre força maior (a força cai com o quadrado da distância). A ordem, da maior para a menor força, é E, D, C, B, A, como no <strong>gráfico B</strong>. Alternativa <strong>B</strong>.</p><p>O gráfico A tem as retas horizontais, mas com a ordem invertida.</p>",
  figs(("q154", "Esquema com a Terra no centro e cinco órbitas circulares concêntricas; os satélites E e D estão nas órbitas mais próximas, depois C e B, e A está na órbita mais externa."),
       ("q154a", "Alternativa A: retas horizontais, com A no topo, depois B, C, D e E na parte de baixo."),
       ("q154b", "Alternativa B: retas horizontais, com E no topo, depois D, C, B e A na parte de baixo."),
       ("q154c", "Alternativa C: curvas crescentes que partem da origem, A a mais alta e E a mais baixa."),
       ("q154d", "Alternativa D: retas crescentes que partem da origem, A a mais inclinada e E a menos."),
       ("q154e", "Alternativa E: retas crescentes que partem da origem, E a mais inclinada e A a menos.")),
  ["gravitação", "proporcionalidade inversa"],
  enun=p(T(154, 0)) + p("\\(F = G\\dfrac{m_1 m_2}{d^2}\\)") + p("onde <em>m</em><sub>1</sub> e <em>m</em><sub>2</sub> correspondem às massas dos corpos, <em>d</em> à distância entre eles, <em>G</em> à constante universal da gravitação e <em>F</em> à força que um corpo exerce sobre o outro.", T(154, 3)) + "[[fig:1]]" + p(T(154, 5)),
  alts=ALT(2))
X(155, "Proporcionalidade", "<p>No reservatório atual, 6 ralos escoam 900 m³ em 6 h: cada ralo escoa 900 ÷ 6 ÷ 6 = 25 m³ por hora. O novo precisa escoar 500 m³ em 4 h, ou 125 m³ por hora: 125 ÷ 25 = <strong>5 ralos</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["regra de três composta", "vazão"], trocas=[("900 m3", "900 m<sup>3</sup>"), ("500 m3", "500 m<sup>3</sup>")])
X(156, "Geometria plana", "<p>Triplicando o lado, a área de cada placa fica 3² = 9 vezes maior. Para cobrir a mesma área S, são necessárias 9 vezes menos placas: \\(X = \\dfrac{N}{9}\\). Alternativa <strong>A</strong>.</p><p>A opção C (N/3) esquece que a área depende do quadrado do lado.</p>",
  tags=["área", "semelhança"], alts=FR("\\dfrac{N}{9}", "\\dfrac{N}{6}", "\\dfrac{N}{3}", "3N", "9N"))
X(157, "Geometria espacial", "<p>O volume da piscina é 3 · R² · 1 = 12, então R = 2 m. A ilha ocupa 3r² · 1 m³, e a água restante deve ter pelo menos 4 m³: 12 − 3r² ≥ 4, ou r² ≤ \\(\\tfrac{8}{3}\\) ≈ 2,67. Logo r ≤ 1,63, ou seja, <strong>1,6 m</strong>. Alternativa <strong>A</strong>.</p>",
  figs(("q157", "Vista de cima da piscina circular de raio R e centro O; no meio, a ilha de lazer circular, de raio r, com o mesmo centro; a região entre as duas circunferências é a água.")),
  ["cilindro", "inequação"],
  enun=p(T(157, 0).replace("12 m3", "12 m<sup>3</sup>").replace("4 m3", "4 m<sup>3</sup>")) + "[[fig:1]]" + p("Considere 3 como valor aproximado para π.", T(157, 3)))
X(158, "Porcentagem", "<p>O lucro foi 34 000 − 26 000 = 8 000 reais. O imposto é 15% do lucro: 0,15 × 8 000 = <strong>R$ 1 200,00</strong>. Alternativa <strong>B</strong>.</p><p>Calcular 15% do valor de venda daria R$ 5 100,00 (E).</p>",
  tags=["porcentagem", "imposto de renda"], enun=p(T(158, 0)) + fonte(T(158, 1)) + p(T(158, 2)))
X(159, "Razão e proporção", "<p>A mistura tem 1 + 4 + 2 = 7 partes, das quais 1 é de cimento. Em 14 m³, o cimento ocupa 14 ÷ 7 = <strong>2,00 m³</strong>. Alternativa <strong>B</strong>.</p><p>A opção A (1,75) divide por 8 partes, e a C (2,33), por 6.</p>",
  tags=["divisão proporcional", "razão"], trocas=[("14 m3", "14 m<sup>3</sup>"), ("em m3,", "em m<sup>3</sup>,")])
X(160, "Razão e proporção", "<p>O lucro médio anual é o lucro dividido pelo tempo: F, 24 ÷ 3 = 8; G, 24 ÷ 2 = 12; H, 25 ÷ 2,5 = 10; M, 15 ÷ 1,5 = 10; P, 9 ÷ 1,5 = 6. O maior é o da empresa <strong>G</strong>. Alternativa <strong>B</strong>.</p><p>H tem o maior lucro acumulado, mas em mais tempo.</p>",
  tags=["razão", "média"],
  enun=p(T(160, 0), T(160, 1)) + tabela(["Empresa", "Lucro (em milhões de reais)", "Tempo (em anos)"], [["F", "24", "3,0"], ["G", "24", "2,0"], ["H", "25", "2,5"], ["M", "15", "1,5"], ["P", "9", "1,5"]]) + p(T(160, 4)))
X(161, "Funções", "<p>Pelo gráfico, uma carta de 100 g custa R$ 1,70; de 200 g, R$ 2,65; de 350 g, R$ 4,00 (cada degrau inclui o seu limite direito). O total é 2 × 1,70 + 3 × 2,65 + 4,00 = 3,40 + 7,95 + 4,00 = <strong>R$ 15,35</strong>. Alternativa <strong>D</strong>.</p>",
  figs(("q161", "Gráfico em degraus do custo (R$) em função da massa (g), de 0 a 400 g, em faixas de 50 g, com bolinha aberta no início e fechada no fim de cada degrau: até 20 g, 0,80; até 50 g, 1,25; até 100 g, 1,70; até 150 g, 2,15; até 200 g, 2,65; até 250 g, 3,10; até 300 g, 3,55; até 350 g, 4,00; até 400 g, 4,45.")),
  ["função definida por partes", "leitura de gráfico"],
  enun=p(T(161, 0)) + "[[fig:1]]" + fonte("Disponível em: www.correios.com.br. Acesso em: 2 ago. 2012 (adaptado).") + p(T(161, 2)))
X(162, "Estatística", "<p>Ordenando as diárias dos 200 hotéis: 25% (50 hotéis) custam 200; 25% (mais 50, até o 100º) custam 300; 40% (do 101º ao 180º) custam 400; 10% custam 600. A mediana é a média do 100º e do 101º valores: \\(\\dfrac{300 + 400}{2} = \\) <strong>R$ 350,00</strong>. Alternativa <strong>C</strong>.</p>",
  figs(("q162", "Gráfico de setores: A, 25%; B, 25%; C, 40%; D, 10%.")),
  ["mediana", "gráfico de setores"], enun=p(T(162, 0)) + "[[fig:1]]" + p(T(162, 3)))
X(163, "Porcentagem", "<p>Com a remarcação de 20%, o produto passa a custar 0,8 × 50 = R$ 40,00. O cartão daria mais 10% sobre esse valor: 0,1 × 40 = <strong>R$ 4,00</strong>. Alternativa <strong>E</strong>.</p><p>A opção D (5,00) aplica os 10% sobre o preço original.</p>",
  tags=["descontos sucessivos", "porcentagem"])
X(164, "Geometria plana", "<p>Simetria em relação a um ponto é a rotação de 180° em torno dele. A figura original fica acima e à esquerda de O; a figura simétrica fica abaixo e à direita, de cabeça para baixo, com o triângulo escuro e o cinza trocando de lado, como na <strong>figura E</strong>. Alternativa <strong>E</strong>.</p><p>Em D, a cópia foi refletida em vez de girada: os triângulos estão em posição de espelho.</p>",
  figs(("q164", "Figura original: retângulo com a metade de cima dividida na diagonal em um triângulo preto e um cinza, e a metade de baixo branca; o ponto O fica no canto inferior direito."),
       ("q164a", "Alternativa A: a figura original e, à direita, uma cópia em pé com triângulos preto e cinza na vertical."),
       ("q164b", "Alternativa B: a figura original e, à direita, uma cópia com a parte branca em cima e os triângulos embaixo."),
       ("q164c", "Alternativa C: a figura original e, à direita, uma cópia refletida em espelho, lado a lado."),
       ("q164d", "Alternativa D: a figura original e, abaixo e à direita de O, uma cópia de cabeça para baixo, com os triângulos em posição de espelho."),
       ("q164e", "Alternativa E: a figura original e, abaixo e à direita de O, a cópia girada 180° em torno de O.")),
  ["simetria central", "rotação"], enun=p(T(164, 0)) + "[[fig:1]]" + p("Figura original", T(164, 3)), alts=ALT(2))
X(165, "Análise combinatória", "<p>Colorindo os vértices A, B, C e D de modo que vizinhos tenham cores diferentes: se A e C têm a mesma cor, são 3 × 2 × 2 = 12 maneiras; se têm cores diferentes, 3 × 2 × 1 × 1 = 6. Seriam 18 colorações. Mas a joia é um objeto que pode ser girada 180° e virada, e várias colorações são a mesma joia. O losango não quadrado tem 4 simetrias: ficar parado (as 18 colorações continuam iguais), girar 180° (A↔C e B↔D: só as 6 com A e C da mesma cor e B e D da mesma cor ficam iguais), refletir trocando só B e D (12 ficam iguais) e refletir trocando só A e C (12). Pelo lema de Burnside, o número de joias distintas é a média: \\(\\dfrac{18 + 6 + 12 + 12}{4} = \\) <strong>12</strong>. Alternativa <strong>B</strong>.</p><p>A conta 18 (C) trata como diferentes joias que são iguais depois de girar ou virar.</p>",
  figs(("q165", "Losango com os vértices A (em cima), B (direita), C (embaixo) e D (esquerda), cada um com uma pedra.")),
  ["contagem", "simetria"], enun=p(T(165, 0), T(165, 1), T(165, 2).replace("vértices A, B, C e D", "vértices <em>A</em>, <em>B</em>, <em>C</em> e <em>D</em>")) + "[[fig:1]]" + p(T(165, 4)))
X(166, "Funções", "<p>Se após 30 anos resta metade, (2,7)<sup>30k</sup> = \\(\\tfrac{1}{2}\\). Queremos (2,7)<sup>kt</sup> = 0,1. Escrevendo (2,7)<sup>kt</sup> = \\(\\left(\\tfrac{1}{2}\\right)^{t/30}\\) e tirando o logaritmo: \\(\\tfrac{t}{30} \\cdot \\log 2 = 1\\), então t = 30 ÷ 0,3 = <strong>100 anos</strong>. Alternativa <strong>E</strong>.</p>",
  tags=["função exponencial", "logaritmo"],
  enun=p(T(166, 0).replace("(2,7)kt", "(2,7)<sup><em>kt</em></sup>"), "Considere 0,3 como aproximação para log<sub>10</sub> 2.", T(166, 2)))
X(167, "Geometria plana", "<p>Reduzir os lados em 20% é multiplicá-los por 0,8. A área fica multiplicada por 0,8² = 0,64, ou seja, passa a ser 64% da original: uma redução de <strong>36%</strong>. Alternativa <strong>C</strong>.</p><p>A opção B (20%) aplica a redução linear à área.</p>",
  tags=["área", "semelhança"], enun=p(T(167, 0)) + fonte(T(167, 1)) + p(T(167, 2), T(167, 3)))
X(168, "Probabilidade", "<p>P = 0,54 × 0,025 + 0,46 × 0,038 = 0,0135 + 0,01748 ≈ 0,031, ou cerca de 3,1%. Esse valor está entre 2/100 e 4/100: desempenho <strong>bom</strong>. Alternativa <strong>B</strong>.</p><p>A conta é uma média ponderada das taxas de defeito, com pesos iguais à participação de cada máquina na produção.</p>",
  tags=["probabilidade total", "porcentagem"],
  enun=p(T(168, 0), "Em setembro, a máquina I produziu \\(\\tfrac{54}{100}\\) do total de parafusos produzidos pela fábrica. Dos parafusos produzidos por essa máquina, \\(\\tfrac{25}{1\\,000}\\) eram defeituosos.", "Por sua vez, \\(\\tfrac{38}{1\\,000}\\) dos parafusos produzidos no mesmo mês pela máquina II eram defeituosos.", T(168, 4).replace("em que P indica", "em que <em>P</em> indica"))
  + tabela(["Probabilidade de defeito", "Desempenho"], [["0 ≤ P &lt; 2/100", "Excelente"], ["2/100 ≤ P &lt; 4/100", "Bom"], ["4/100 ≤ P &lt; 6/100", "Regular"], ["6/100 ≤ P &lt; 8/100", "Ruim"], ["8/100 ≤ P ≤ 1", "Péssimo"]]) + p(T(168, 7)))
X(169, "Análise combinatória", "<p>A chance de ganhar é proporcional ao número de sextinas cobertas. Uma cartela com n números cobre C(n, 6) sextinas: 1 (6 números), 7, 28, 84 e 210. Arthur: 250; Bruno: 41 × 7 + 4 = 291; Caio: 12 × 28 + 10 = 346; Douglas: 4 × 84 = 336; Eduardo: 2 × 210 = 420. Os maiores são <strong>Caio e Eduardo</strong>. Alternativa <strong>A</strong>.</p>",
  tags=["combinação", "probabilidade"],
  enun=p(T(169, 0), T(169, 1), T(169, 2)) + tabela(["Quantidade de números escolhidos em uma cartela", "Preço da cartela (R$)"], [["6", "2,00"], ["7", "12,00"], ["8", "40,00"], ["9", "125,00"], ["10", "250,00"]])
  + p(T(169, 5)) + "<ul><li>Arthur: 250 cartelas com 6 números escolhidos;</li><li>Bruno: 41 cartelas com 7 números escolhidos e 4 cartelas com 6 números escolhidos;</li><li>Caio: 12 cartelas com 8 números escolhidos e 10 cartelas com 6 números escolhidos;</li><li>Douglas: 4 cartelas com 9 números escolhidos;</li><li>Eduardo: 2 cartelas com 10 números escolhidos.</li></ul>" + p(T(169, 9)))
X(170, "Grandezas e medidas", "<p>355 mL = 35,5 cL. Dividindo por 2,95 cL por onça: 35,5 ÷ 2,95 ≈ <strong>12,03 fl oz</strong>. Alternativa <strong>C</strong>.</p><p>A opção E (120,34) divide 355 mL por 2,95 sem converter as unidades.</p>",
  tags=["conversão de unidades", "divisão"])
X(171, "Equações", "<p>Se o verde dura X, o vermelho dura \\(\\tfrac{3X}{2}\\) e o amarelo, 5 s. O ciclo é Y = X + \\(\\tfrac{3X}{2}\\) + 5. Multiplicando por 2: 2Y = 5X + 10, ou <strong>5X − 2Y + 10 = 0</strong>. Alternativa <strong>B</strong>.</p>",
  tags=["equação do 1º grau", "modelagem"],
  enun=p("Na aferição de um novo semáforo, os tempos são ajustados de modo que, em cada ciclo completo (verde-amarelo-vermelho), a luz amarela permaneça acesa por 5 segundos, e o tempo em que a luz verde permaneça acesa seja igual a \\(\\tfrac{2}{3}\\) do tempo em que a luz vermelha fique acesa. A luz verde fica acesa, em cada ciclo, durante <em>X</em> segundos e cada ciclo dura <em>Y</em> segundos.", T(171, 2)))
X(172, "Funções", "<p>A porta abre quando T = 39: 400 − \\(\\tfrac{t^2}{4}\\) = 39, então t² = 4 × 361 = 1 444 e t = <strong>38 minutos</strong>. Alternativa <strong>D</strong>.</p><p>A opção A (19) é a raiz de 361, sem multiplicar por 4.</p>",
  tags=["função quadrática", "equação"],
  enun=p("A temperatura <em>T</em> de um forno (em graus centígrados) é reduzida por um sistema a partir do instante de seu desligamento (<em>t</em> = 0) e varia de acordo com a expressão \\(T(t) = -\\dfrac{t^2}{4} + 400\\), com <em>t</em> em minutos. Por motivos de segurança, a trava do forno só é liberada para abertura quando o forno atinge a temperatura de 39 ºC.", T(172, 3)))
X(173, "Aritmética", "<p>O ciclo 1 ocupa 1755 a 1765, e cada ciclo começa 11 anos depois do anterior: o ciclo n começa em 1755 + 11(n − 1). Para 2101: 2101 − 1755 = 346 e 346 ÷ 11 ≈ 31,5, então já se passaram 31 ciclos completos e 2101 está no ciclo <strong>32</strong> (de 2096 a 2106). Alternativa <strong>A</strong>.</p>",
  tags=["divisão", "sequências"], enun=p(T(173, 0)) + fonte(T(173, 1)) + p(T(173, 2)))
X(174, "Escalas", "<p>As escalas são 1 : 25 000 000 e 1 : 4 000 000. A razão entre as medidas lineares é 25 000 000 ÷ 4 000 000 = 6,25, e a área é ampliada pelo quadrado disso: 6,25² ≈ 39,06, <strong>maior que 30 e menor que 40</strong>. Alternativa <strong>D</strong>.</p><p>A opção A usa só a razão linear (6,25).</p>",
  figs(("q174", "Mapa do Brasil na escala 1 : 25 000 000 com o estado do Rio de Janeiro destacado e, num quadro ao lado, o mesmo estado ampliado, na escala 1 : 4 000 000.")),
  ["escala", "razão de áreas"], enun=p(T(174, 0)) + "[[fig:1]]" + p(T(174, 2), T(174, 3)))
X(175, "Geometria analítica", "<p>As antenas estão em A(30, 20), B(70, 20) e C(60, 50). O ponto equidistante de A e B está na reta x = 50. Igualando as distâncias a A e a C: (50 − 30)² + (y − 20)² = (50 − 60)² + (y − 50)², ou 400 − 40y + 400 = 100 − 100y + 2 500, então 60y = 1 800 e y = 30. O ponto é <strong>(50 ; 30)</strong>. Alternativa <strong>E</strong>.</p><p>É o circuncentro do triângulo ABC.</p>",
  figs(("q175", "Plano cartesiano com eixos x (km) e y (km), de 0 a 90 e de 0 a 70, com os pontos A(30, 20), B(70, 20) e C(60, 50).")),
  ["distância entre pontos", "circuncentro"], enun=p(T(175, 0)) + "[[fig:1]]" + p(T(175, 2), T(175, 3)))
X(176, "Geometria espacial", "<p>A forma tem uma parte externa que se alarga para cima e uma parte interna (o tubo do meio) que se estreita para cima. As duas têm bases circulares de tamanhos diferentes: são <strong>dois troncos de cone</strong>. Alternativa <strong>D</strong>.</p><p>O tubo central não é um cilindro (A), já que a base de cima é menor que a de baixo.</p>",
  figs(("q176", "Forma de bolo vista em perspectiva: a parede externa é um tronco de cone mais largo em cima; no centro, um tubo também em forma de tronco de cone, mais estreito em cima; as bordas de baixo aparecem tracejadas.")),
  ["sólidos geométricos", "tronco de cone"], enun=p(T(176, 0)) + "[[fig:1]]" + p(T(176, 2), T(176, 3)))
X(177, "Estatística", "<p>No gráfico, os países abaixo da média ficam abaixo do eixo horizontal: Rússia, Portugal, Itália, Israel e México. Entre eles, o que está mais à direita (mais horas de estudo) é <strong>Israel</strong>. Alternativa <strong>C</strong>.</p><p>Holanda e Finlândia (A e B) estão acima da média.</p>",
  figs(("q177", "Gráfico com o eixo vertical das notas no Pisa (350 a 600) e o eixo horizontal das horas de estudo dos 7 aos 14 anos (4 500 a 9 000), cruzando-se na média. Acima da média: Finlândia, Coreia do Sul, Japão, Holanda e Austrália. Abaixo: Rússia (cerca de 5 500 h), Portugal, Itália, Israel (o mais à direita, cerca de 8 000 h) e México.")),
  ["leitura de gráfico", "média"],
  enun=tit(T(177, 0)) + ap(T(177, 1)) + "[[fig:1]]" + fonte("* Considerando as médias de cada país no exame de matemática. <em>Nova Escola</em>, São Paulo, dez. 2010 (adaptado).") + p(T(177, 5)))
X(178, "Geometria plana", "<p>Na figura, A e B estão no eixo do copo, então AC é o raio da parte mais larga do copo (o bojo, na altura do líquido) e BD, o raio da base. Quatro copos em 2 × 2 encostam pelo bojo (centros a 2·AC de distância), e a base de cada um precisa caber dentro da bandeja: l = 2·AC + 2·BD = 2 · \\(\\tfrac{7}{5}\\)BD + 2BD = \\(\\tfrac{24}{5}\\)BD. A razão é \\(\\dfrac{24}{5}\\). Alternativa <strong>D</strong>.</p><p>Tomar AC e BD como diâmetros daria 12/5, que não está entre as opções.</p>",
  figs(("q178", "Copo em perfil, com uma linha tracejada no eixo: na parte mais larga do bojo, A está no eixo e C na borda; na base, B está no eixo e D na borda.")),
  ["circunferência", "otimização"],
  enun=p(T(178, 0)) + "[[fig:1]]" + p("Considere que \\(\\overline{AC} = \\tfrac{7}{5}\\overline{BD}\\) e que <em>l</em> é a medida de um dos lados da base da bandeja.", "Qual deve ser o menor valor da razão \\(\\dfrac{l}{\\overline{BD}}\\) para que uma bandeja tenha capacidade de portar exatamente quatro copos de uma só vez?"),
  alts=FR("2", "\\dfrac{14}{5}", "4", "\\dfrac{24}{5}", "\\dfrac{28}{5}"))
X(179, "Geometria plana", "<p>Pela semelhança de triângulos, a haste no cruzamento dos cabos mede \\(\\dfrac{6 \\cdot 4}{6 + 4} = \\dfrac{24}{10} = \\) <strong>2,4 m</strong>, qualquer que seja a distância entre os postes. Alternativa <strong>C</strong>.</p><p>Em detalhe: chamando AF = a e FB = b, EF/4 = b/(a + b) e EF/6 = a/(a + b); somando, EF(1/4 + 1/6) = 1.</p>",
  figs(("q179", "Dois postes verticais: AC, com 4 m, à esquerda, e BD, com 6 m, à direita, sobre o solo AB. Os cabos AD e BC se cruzam no ponto E, e a haste vertical EF vai de E até o solo.")),
  ["semelhança de triângulos", "média harmônica"], enun=p(T(179, 0)) + "[[fig:1]]" + p(T(179, 4).replace("haste EF", "haste <em>EF</em>")),
  alts={**D[179]["alternativas"], "E": "2\\(\\sqrt{6}\\) m"})
X(180, "Geometria espacial", "<p>Os pontos A e B descrevem arcos de circunferência num plano vertical, em torno do pivô. Projetando esses arcos no chão, perpendicularmente, eles viram <strong>segmentos de reta</strong> horizontais, como na figura B. Alternativa <strong>B</strong>.</p><p>A opção C mostra os arcos vistos de lado, e não projetados no chão.</p>",
  figs(("q180", "Gangorra inclinada sobre um pivô triangular, com a ponta A embaixo, à esquerda, e a ponta B em cima, à direita, sobre o chão."),
       ("q180a", "Alternativa A: um ponto acima de A e outro acima de B."),
       ("q180b", "Alternativa B: um segmento horizontal acima de A e outro acima de B."),
       ("q180c", "Alternativa C: dois arcos curvos, um acima de A e outro acima de B."),
       ("q180d", "Alternativa D: dois segmentos verticais, um acima de A e outro acima de B."),
       ("q180e", "Alternativa E: duas linhas em forma de V invertido e de V.")),
  ["projeção ortogonal", "circunferência"], enun=p(T(180, 0), T(180, 1).replace("pontos A e B", "pontos <em>A</em> e <em>B</em>")) + "[[fig:1]]" + p(T(180, 4).replace("pontos A e B", "pontos <em>A</em> e <em>B</em>")), alts=ALT(2))

completar(Q, R)
