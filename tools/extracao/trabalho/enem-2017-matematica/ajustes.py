# Enem 2017, 2º dia, caderno azul: Matemática (questões 136 a 180; no site, 1 a 45).
# Texto legível (sem DECOD). Frações e fórmulas em KaTeX; quadros em tabela HTML. Alternativas-imagem na Q152.
# Sem anuladas nesta área.

import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, paragrafos_enem

ID = "enem-2017-matematica"
META = {"id": ID, "banca": "Enem", "ano": 2017, "titulo": "Enem 2017: Matemática", "fonte": "Inep", "dataExame": "2017-11-12",
        "duracaoMinutos": 150, "area": "Matemática", "caderno": "azul", "dia": 2}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2017-dia2-azul")
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


def X(n, assunto, expl, imagens=(), tags=(), enun=None, alts=None, anulacao=None):
    q = {"materia": "Matemática", "assunto": assunto, "area": "Matemática", "tags": list(tags), "numeroOriginal": n,
         "enunciado": LIMPA(enun or p(*[x for t, x in P(n) if t == "p"])), "alternativas": {k: LIMPA(v) for k, v in dict(alts or D[n]["alternativas"]).items()},
         "imagens": list(imagens), "explicacao": expl}
    if anulacao: q["anulacao"] = anulacao
    Q[n - 135] = q

K = lambda s: f"\\({s}\\)"
PP = lambda n: [x for t, x in P(n) if t == "p"]
F = lambda n, *figidx: None


def EF(n, antes, fig="[[fig:1]]", fnt=None, depois=None):
    """Parágrafos p antes da figura, figura, fonte opcional e o resto."""
    ps = PP(n)
    s = p(*ps[:antes]) + fig + (fonte(fnt) if fnt else "")
    return s + p(*(ps[antes:] if depois is None else depois))


X(136, "Matemática financeira", "<p>Quitando no ato de pagar a 6ª parcela, a pessoa paga a 6ª pelo valor cheio (P) e antecipa a 7ª e a 8ª, que venceriam em 1 e 2 meses. O valor atual de cada uma é P dividido por " + K("(1 + \\tfrac{i}{100})") + " elevado ao número de meses que faltam:</p><p><em>P</em> · [1 + 1/(1 + <em>i</em>/100) + 1/(1 + <em>i</em>/100)<sup>2</sup>]. Alternativa <strong>A</strong>.</p><p>A alternativa E esquece a 6ª parcela, que é paga no próprio mês, sem desconto.</p>",
  tags=["valor presente", "juros compostos"],
  enun=p("Um empréstimo foi feito à taxa mensal de <em>i</em>%, usando juros compostos, em oito parcelas fixas e iguais a <em>P</em>.", T(136, 1), T(136, 2)),
  alts={"A": "<em>P</em> · [1 + 1/(1 + <em>i</em>/100) + 1/(1 + <em>i</em>/100)<sup>2</sup>]", "B": "<em>P</em> · [1 + 1/(1 + <em>i</em>/100) + 1/(1 + 2<em>i</em>/100)]", "C": "<em>P</em> · [1/(1 + <em>i</em>/100)<sup>2</sup> + 1/(1 + <em>i</em>/100)<sup>2</sup>]", "D": "<em>P</em> · [1/(1 + <em>i</em>/100) + 1/(1 + 2<em>i</em>/100) + 1/(1 + 3<em>i</em>/100)]", "E": "<em>P</em> · [1/(1 + <em>i</em>/100) + 1/(1 + <em>i</em>/100)<sup>2</sup> + 1/(1 + <em>i</em>/100)<sup>3</sup>]"})
X(137, "Logaritmo", "<p>Chamando x = 1,013<sup>n</sup>, a condição P ≤ 400 fica " + K("\\dfrac{5000 \\cdot 0{,}013\\,x}{x - 1} \\le 400 \\Rightarrow 65x \\le 400x - 400 \\Rightarrow x \\ge \\dfrac{400}{335}") + ".</p><p>Aplicando log: n · 0,005 ≥ 2,602 − 2,525 = 0,077, logo n ≥ 15,4. O menor número inteiro é <strong>16</strong>. Alternativa <strong>D</strong>.</p>",
  tags=["função exponencial", "inequação"],
  enun=p("Para realizar a viagem dos sonhos, uma pessoa precisava fazer um empréstimo no valor de R$ 5 000,00. Para pagar as prestações, dispõe de, no máximo, R$ 400,00 mensais. Para esse valor de empréstimo, o valor da prestação (<em>P</em>) é calculado em função do número de prestações (<em>n</em>) segundo a fórmula")
       + "<p>\\[P = \\frac{5000 \\times 1{,}013^n \\times 0{,}013}{1{,}013^n - 1}\\]</p>" + p(T(137, 2), T(137, 3)))
X(138, "Trigonometria", "<p>O valor máximo de I é k, quando sen x = 1 (x = 90°). Para x = 30°, I = k · sen 30° = 0,5k: a intensidade cai a <strong>50%</strong> do máximo. Alternativa <strong>B</strong>.</p><p>86% (E) seria o valor com cos 30°, que corresponderia ao ângulo medido a partir da vertical.</p>",
  figs(("q138", "Raio de sol, representado por uma seta pontilhada, chegando à superfície de um lago e formando com ela o ângulo x.")),
  ["seno", "porcentagem"],
  enun=p("Raios de luz solar estão atingindo a superfície de um lago formando um ângulo <em>x</em> com a sua superfície, conforme indica a figura.", "Em determinadas condições, pode-se supor que a intensidade luminosa desses raios, na superfície do lago, seja dada aproximadamente por " + K("I(x) = k \\cdot \\text{sen}(x)") + ", sendo <em>k</em> uma constante, e supondo-se que <em>x</em> está entre 0° e 90°.") + "[[fig:1]]" + p("Quando <em>x</em> = 30°, a intensidade luminosa se reduz a qual percentual de seu valor máximo?"))
X(139, "Gráficos", "<p>O veículo está imóvel quando a velocidade é zero: no gráfico, a linha fica encostada no eixo do tempo de 6 a 8 minutos, isto é, <strong>2 minutos</strong>. Alternativa <strong>C</strong>.</p><p>Trechos horizontais acima do eixo (de 0 a 1 e de 3 a 4 min) são velocidade constante, não parada.</p>",
  figs(("q139", "Gráfico da velocidade em função do tempo (min), de 0 a 10: começa num valor baixo, sobe até o máximo em 2 min, desce e fica constante de 3 a 4 min, sobe um pouco em 5 min, cai a zero em 6 min, fica em zero até 8 min e depois volta a subir até 10 min.")),
  ["leitura de gráfico", "velocidade"], enun=EF(139, 1))
X(140, "Geometria plana", "<p>As taças ficam lado a lado, com as bordas (raio 5 cm) se tocando: os centros ficam a 10 cm um do outro. Só as bases (raio 4 cm) precisam estar sobre a bandeja.</p><p>Comprimento: 3 × 10 + 4 + 4 = 38 cm. Largura: o diâmetro da base, 8 cm. Área: 38 × 8 = <strong>304 cm²</strong>. Alternativa <strong>C</strong>.</p><p>Usar o diâmetro das bordas nas duas medidas dá 40 × 10 = 400 cm² (E).</p>",
  figs(("q140", "Taça de espumante de boca larga, com haste fina e base circular.")), ["círculo", "área do retângulo"], enun=EF(140, 1))
X(141, "Razão e proporção", "<p>Cada suco leva 2/3 de polpa de morango e 1/3 de acerola. A alta da acerola encarece o suco em (15,30 − 14,70) × 1/3 = 0,20 real por embalagem de suco.</p><p>Para compensar, a redução x no morango deve cumprir x × 2/3 = 0,20, logo x = <strong>0,30 real</strong>. Alternativa <strong>E</strong>.</p>",
  tags=["proporção", "custo"],
  enun=p("Em uma cantina, o sucesso de venda no verão são sucos preparados à base de polpa de frutas. Um dos sucos mais vendidos é o de morango com acerola, que é preparado com " + K("\\tfrac{2}{3}") + " de polpa de morango e " + K("\\tfrac{1}{3}") + " de polpa de acerola.", *PP(141)[2:]))
X(142, "Geometria espacial", "<p>O cubo de 80 cm só cabe em caixas com as três dimensões de pelo menos 80 cm, o que exclui a caixa 2 (75 cm). Entre as outras, sobra menos espaço na de menor volume:</p><ul><li>1: 86 × 86 × 86 = 636 056 cm³;</li><li>3: 85 × 82 × 90 = 627 300 cm³;</li><li>4: 82 × 95 × 82 = 638 780 cm³;</li><li>5: 80 × 95 × 85 = 646 000 cm³.</li></ul><p>A escolhida é a <strong>caixa 3</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["volume", "paralelepípedo"], enun=p(T(142, 0)) + LISTA(T(142, 1).replace("<br>", "")) + p(T(142, 2), T(142, 3)))
X(143, "Análise combinatória", "<p>Como a posição não importa, um modelo é definido só por quantos carrinhos há de cada cor: a + b + c + d = 10, com cada cor pelo menos 1. Pintando antes um carrinho de cada cor, sobram 6 para distribuir livremente entre 4 cores: são as soluções de a′ + b′ + c′ + d′ = 6, que somam " + K("C_{9,3}") + " = 84. Alternativa <strong>B</strong>.</p><p>" + K("4^6") + " (E) e " + K("6^4") + " (D) contariam posições diferentes como modelos diferentes.</p>",
  figs(("q143", "Desenho de um caminhão-cegonha com uma carreta de três andares carregando dez carrinhos.")),
  ["combinação com repetição"], enun=EF(143, 1),
  alts=FR("C_{6,4}", "C_{9,3}", "C_{10,4}", "6^4", "4^6"))
X(144, "Grandezas e medidas", "<p>A água fica 50 cm abaixo da borda: profundidade da água = 1,7 − 0,5 = 1,2 m. Volume: 3 × 5 × 1,2 = 18 m³ = 18 000 L.</p><p>Produto: 18 × 1,5 mL = <strong>27,00 mL</strong>. Alternativa <strong>B</strong>.</p><p>Usar a profundidade total da piscina (1,7 m) dá 38,25 mL, que não está nas opções.</p>",
  tags=["volume", "conversão de unidades"])
X(145, "Estatística", "<p>Calculando 1,96 · σ ÷ √N para cada pesquisa:</p><ul><li>P1: 1,96 · 0,5 ÷ 42 ≈ 0,0233;</li><li>P2: 1,96 · 0,4 ÷ 28 = 0,028;</li><li>P3: 1,96 · 0,3 ÷ 24 ≈ 0,0245;</li><li>P4: 1,96 · 0,2 ÷ 21 ≈ 0,0187;</li><li>P5: 1,96 · 0,1 ÷ 8 ≈ 0,0245.</li></ul><p>Só a <strong>P4</strong> tem erro menor que 0,02. Alternativa <strong>D</strong>.</p>",
  tags=["margem de erro", "raiz quadrada"],
  enun=p(T(145, 0), T(145, 1), T(145, 2)) + tabela(["Pesquisa", "σ", "<em>N</em>", "√<em>N</em>"], [["P1", "0,5", "1 764", "42"], ["P2", "0,4", "784", "28"], ["P3", "0,3", "576", "24"], ["P4", "0,2", "441", "21"], ["P5", "0,1", "64", "8"]])
       + p("O erro <em>e</em> pode ser expresso por " + K("|e| < 1{,}96\\,\\dfrac{\\sigma}{\\sqrt{N}}") + ", em que σ é um parâmetro e <em>N</em> é o número de pessoas entrevistadas pela pesquisa.", "Qual pesquisa deverá ser utilizada?"))
X(146, "Razão e proporção", "<p>A travessia dura 90 s, e os dois bondinhos têm a mesma velocidade. Quando se cruzam, A andou 40 s, ou seja, 40/90 do caminho; B andou o resto, 50/90, o que leva 50 s. Logo B saiu 50 − 40 = <strong>10 s</strong> antes de A. Alternativa <strong>B</strong>.</p>",
  tags=["velocidade", "proporção"],
  enun=p(T(146, 0).replace("bondinho A", "bondinho <em>A</em>").replace("bondinho B", "bondinho <em>B</em>"), T(146, 1).replace("bondinho B", "bondinho <em>B</em>").replace("bondinho A", "bondinho <em>A</em>")))
X(147, "Porcentagem", "<p>Pelo gráfico, às 15 h a profundidade é h + 6 e às 16 h é h + 4 (cada linha vale 1 m). A queda de 10% dá:</p><p>h + 4 = 0,9 (h + 6) → h + 4 = 0,9h + 5,4 → 0,1h = 1,4 → h = 14 m.</p><p>Às 16 h: 14 + 4 = <strong>18 m</strong>. Alternativa <strong>A</strong>.</p>",
  figs(("q147", "Gráfico “Registro de profundidade”: profundidade (m) em função da hora, de 13 a 17 h. O ponto das 13 h está no nível h; às 14 h, duas linhas acima; às 15 h, seis linhas acima (máximo); às 16 h, quatro linhas acima; às 17 h, uma linha acima.")),
  ["equação do 1º grau", "leitura de gráfico"],
  enun=p(T(147, 0).replace("profundidade h,", "profundidade <em>h</em>,").replace("partir de h,", "partir de <em>h</em>,")) + "[[fig:1]]" + p(*PP(147)[1:]))
X(148, "Geometria espacial", "<p>Na Figura 2, a estrutura tem duas faces triangulares paralelas e iguais (as pontas da cabana), ligadas por três faces retangulares, uma delas no chão. É um <strong>prisma triangular reto</strong>. Alternativa <strong>E</strong>.</p><p>O tetraedro e as pirâmides (A, B e C) terminam em um vértice, não em uma aresta horizontal.</p>",
  figs(("q148", "Figura 1: foto de uma cabana de madeira em forma de “A”, com o telhado descendo até o chão dos dois lados. Figura 2: o esqueleto da estrutura, um sólido com duas faces triangulares nas pontas ligadas por arestas paralelas.")),
  ["prismas", "planificação"], enun=p(T(148, 0)) + "[[fig:1]]" + fonte("ROMERO, L. Tendências. <strong>Superinteressante</strong>, n. 315, fev. 2013 (adaptado).") + p(T(148, 4)))
X(149, "Probabilidade", "<p>Cada letra ao lado de um número é vizinha dele:</p><ul><li>P, vizinho do 2: 2 minas em 8 casas, 2/8;</li><li>Q, vizinho do 1: 1/8;</li><li>S, vizinho do 4: 4/8;</li><li>T, vizinho do 3: 3/8;</li><li>R, longe dos números: cerca de 40 minas em 252 casas, ≈ 0,16, mais que 1/8.</li></ul><p>A menor probabilidade é a do quadrado <strong>Q</strong>. Alternativa <strong>B</strong>.</p>",
  figs(("q149", "Tabuleiro de Campo Minado 16 × 16 com quatro quadrados abertos: o 2 em cima à esquerda, com P logo abaixo; o 1 um pouco à direita, com Q logo abaixo; o 3 embaixo à direita, com T logo abaixo; e o 4 embaixo à esquerda, com S logo abaixo. R fica sozinho no meio do tabuleiro. No canto, o contador marca 40 minas.")),
  ["probabilidade", "jogos"], enun=EF(149, 1))
X(150, "Ângulos", "<p>Na posição original, o lado AB era a diagonal do quadrado, com A no canto de cima à esquerda e B no de baixo à direita. Depois do giro, B ficou no canto de cima, com a diagonal AB vertical e a tela em forma de losango. Para levar B de volta ao canto de baixo à direita pelo menor caminho, a tela deve girar <strong>135° no sentido horário</strong>. Alternativa <strong>B</strong>.</p><p>Girar 225° no sentido anti-horário também funcionaria, mas é um ângulo maior.</p>",
  figs(("q150a", "Tela quadrada “O peixe”, na posição original, fixada nos pontos A (canto superior esquerdo) e B (canto inferior direito)."),
       ("q150b", "A mesma tela depois de girar: presa só pelo ponto B, no alto, ela ficou como um losango, com um lado formando 45° com a horizontal.")),
  ["rotação", "ângulos"],
  enun=p(T(150, 0).replace("intitulada O peixe,", "intitulada <em>O peixe</em>,").replace("pontos A e B", "pontos <em>A</em> e <em>B</em>"), T(150, 1)) + "[[fig:1]][[fig:2]]" + p(T(150, 6)))
X(151, "Estatística", "<p>Para ser “Bom”, a média precisa ser pelo menos 7. Total de créditos: 12 + 4 + 8 + 8 + 10 = 42. Soma das notas já obtidas, ponderadas: 8 · 4 + 6 · 8 + 5 · 8 + 7,5 · 10 = 195.</p><p>" + K("\\dfrac{12x + 195}{42} \\ge 7 \\Rightarrow 12x \\ge 99 \\Rightarrow x \\ge 8{,}25") + ". Alternativa <strong>D</strong>.</p>",
  tags=["média ponderada", "inequação"],
  enun=p(T(151, 0)) + tabela(["Avaliação", "Média de notas (<em>M</em>)"], [["Excelente", "9 &lt; <em>M</em> ≤ 10"], ["Bom", "7 ≤ <em>M</em> ≤ 9"], ["Regular", "5 ≤ <em>M</em> &lt; 7"], ["Ruim", "3 ≤ <em>M</em> &lt; 5"], ["Péssimo", "<em>M</em> &lt; 3"]])
       + p(T(151, 2), T(151, 3)) + tabela(["Disciplinas", "Notas", "Número de créditos"], [["I", "", "12"], ["II", "8,00", "4"], ["III", "6,00", "8"], ["IV", "5,00", "8"], ["V", "7,50", "10"]]) + p(T(151, 5)))
X(152, "Funções", "<p>Enquanto a água não chega ao cano de ligação, só o Reservatório 1 enche: h cresce em linha reta com V. Depois, toda a água passa para o Reservatório 2 e h fica parado. Quando o 2 atinge o mesmo nível, os dois enchem juntos: h volta a subir, em linha reta, com metade da inclinação, porque o volume se divide entre dois reservatórios iguais. Esse formato, reta, trecho horizontal e reta menos inclinada, é o da opção D. Alternativa <strong>D</strong>.</p><p>No gráfico C, a inclinação depois do trecho parado é igual à inicial, como se só um reservatório enchesse.</p>",
  figs(("q152", "Dois reservatórios iguais em forma de bloco retangular, lado a lado, ligados por um cano na metade da altura; o cano de entrada chega ao Reservatório 1 pelo alto."),
       ("q152a", "Gráfico A: h cresce em linha reta com V, do começo ao fim."),
       ("q152b", "Gráfico B: h sobe em curva, fica constante e depois sobe numa curva cada vez mais inclinada."),
       ("q152c", "Gráfico C: h sobe em linha reta, fica constante e depois sobe de novo com a mesma inclinação do começo."),
       ("q152d", "Gráfico D: h sobe em linha reta, fica constante e depois sobe de novo com inclinação menor que a do começo."),
       ("q152e", "Gráfico E: h sobe rápido no começo e vai crescendo cada vez mais devagar, sem trecho constante.")),
  ["função afim por partes", "volume"],
  enun=p(T(152, 0)) + "[[fig:1]]" + p(T(152, 3), T(152, 4).replace("altura h", "altura <em>h</em>").replace("volume V", "volume <em>V</em>")), alts=ALT(2))
X(153, "Geometria plana", "<p>Os centros dos três canos formam um triângulo equilátero de lado 1,2 m (dois raios). A altura desse triângulo é " + K("\\tfrac{1{,}2\\sqrt{3}}{2} = 0{,}6\\sqrt{3} \\approx 1{,}02") + " m.</p><p>Altura da pilha: 0,6 (raio de baixo) + 1,02 + 0,6 (raio de cima) = 2,22 m. Com a carroceria: 1,30 + 2,22 = 3,52 m. Somando a margem de 0,50 m: <strong>4,02 m</strong>. Alternativa <strong>D</strong>.</p><p>3,52 m (B) é a altura do caminhão sem a margem de segurança.</p>",
  figs(("q153a", "Foto de um caminhão carregando três grandes tubos empilhados, preso embaixo de um viaduto."),
       ("q153b", "Vista traseira: dois círculos lado a lado apoiados numa base e um terceiro círculo em cima, encaixado entre eles; raio indicado de 0,60 m.")),
  ["triângulo equilátero", "circunferências tangentes"],
  enun=p(T(153, 0)) + tit("Caminhão entala em viaduto no Centro") + ap(T(153, 2)) + "[[fig:1]]" + fonte(T(153, 4)) + p(T(153, 5)) + "[[fig:2]]" + p(T(153, 7), "Considere 1,7 como aproximação para √3.", T(153, 9)))
X(154, "Localização", "<p>O ponto X fica na Rua C, abaixo da Quadra 7. Andando para oeste, a primeira rua à direita é a Rua 3; virando à direita, segue-se para o norte. A próxima rua é a Rua B; virando à esquerda, segue-se para oeste, e o primeiro ponto é o <strong>1</strong>, entre as quadras 2 e 6. Alternativa <strong>A</strong>.</p><p>O ponto 2 fica a leste da Rua 3, no sentido contrário ao da última virada.</p>",
  figs(("q154", "Mapa com 16 quadras em quatro fileiras, separadas pelas ruas A a E (no sentido horizontal) e pelas ruas 1 a 5 (no sentido vertical), com rosa dos ventos (norte para cima). Na Rua B estão os pontos 1 (sob a Quadra 2), 2 (sob a Quadra 3) e 3 (sob a Quadra 4); X fica na Rua C, sob a Quadra 7; na Rua D estão os pontos 4 (sob a Quadra 11) e 5 (sob a Quadra 12).")),
  ["orientação", "pontos cardeais"], enun=p(T(154, 0).replace("letra X,", "letra X,")) + "[[fig:1]]" + p(PP(154)[-1]))
X(155, "Estatística", "<p>Médias das cinco provas:</p><ul><li>X: (5 + 5 + 5 + 10 + 6) ÷ 5 = 6,2;</li><li>Y: (4 + 9 + 3 + 9 + 5) ÷ 5 = 6,0;</li><li>Z: (5 + 5 + 8 + 5 + 6) ÷ 5 = 5,8.</li></ul><p>Só Z fica abaixo de 6: reprova <strong>apenas o aluno Z</strong>. Alternativa <strong>B</strong>.</p><p>Y tem exatamente 6, o que basta (“maior ou igual a 6”).</p>",
  tags=["média aritmética"],
  enun=p(T(155, 0)) + tabela(["Aluno", "1ª Prova", "2ª Prova", "3ª Prova", "4ª Prova", "5ª Prova"], [["X", "5", "5", "5", "10", "6"], ["Y", "4", "9", "3", "9", "5"], ["Z", "5", "5", "8", "5", "6"]]) + p(PP(155)[-1]))
X(156, "Trigonometria", "<p>O raio da tampa é a distância BC entre as pontas do compasso, que formam com a cabeça A um triângulo isósceles de lados 10 cm e ângulo de 120°. Pela lei dos cossenos: BC² = 10² + 10² − 2 · 10 · 10 · cos 120° = 300, então BC = 10√3 ≈ 17 cm.</p><p>17 está entre 15 e 21: material <strong>IV</strong>. Alternativa <strong>D</strong>.</p>",
  figs(("q156", "Plano cartesiano com um compasso: a ponta seca em C (3 ; 1), a ponta do grafite em B, sobre a circunferência traçada, e a cabeça em A, acima; o ângulo entre as hastes, em A, é de 120°.")),
  ["lei dos cossenos", "circunferência"],
  enun=p(T(156, 0).replace("ponto C,", "ponto <em>C</em>,").replace("ponto B e", "ponto <em>B</em> e").replace("ponto A conforme", "ponto <em>A</em> conforme")) + "[[fig:1]]" + p(PP(156)[1])
       + tabela(["Tipo de material", "Intervalo de valores do raio (cm)"], [["I", "0 &lt; <em>R</em> ≤ 5"], ["II", "5 &lt; <em>R</em> ≤ 10"], ["III", "10 &lt; <em>R</em> ≤ 15"], ["IV", "15 &lt; <em>R</em> ≤ 21"], ["V", "21 &lt; <em>R</em> ≤ 40"]]) + p("Considere 1,7 como aproximação para √3.", PP(156)[-1]))
X(157, "Números decimais", "<p>Diferenças em relação a 4 mm: 4,025 → 0,025; 4,100 → 0,100; 3,970 → 0,030; 4,080 → 0,080; 3,099 → 0,901. A mais próxima é a de <strong>4,025 mm</strong>. Alternativa <strong>C</strong>.</p><p>3,970 (B) está a 0,030, um pouco mais longe.</p>",
  figs(("q157", "Foto de uma pulseira de pérolas brancas e pedrinhas brilhantes, com uma seta apontando o espaço vazio onde falta uma pérola.")),
  ["comparação de decimais"], enun=EF(157, 1))
X(158, "Escala", "<p>Na escala 1 : 400, as medidas lineares do monumento são 400 vezes maiores, e o volume, 400³ = 64 000 000 vezes maior.</p><p>25 cm³ × 64 000 000 = 1 600 000 000 cm³. Como 1 m³ = 1 000 000 cm³: <strong>1 600 m³</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["escala de volume", "conversão de unidades"], enun=p(T(158, 0).replace("25 cm3", "25 cm<sup>3</sup>"), T(158, 1)))
X(159, "Razão e proporção", "<p>A bicicleta vai mais devagar quando a roda dá menos voltas por pedalada, ou seja, com a menor razão coroa ÷ catraca:</p><ul><li>I (46 ÷ 24) ≈ 1,92;</li><li>II (46 ÷ 14) ≈ 3,29;</li><li>III (36 ÷ 18) = 2;</li><li>IV (26 ÷ 24) ≈ 1,08;</li><li>V (26 ÷ 14) ≈ 1,86.</li></ul><p>A menor é a da combinação <strong>IV</strong>. Alternativa <strong>D</strong>.</p>",
  figs(("q159", "Ilustração de uma corrente de bicicleta ligando as coroas (engrenagens maiores, à esquerda) às catracas (engrenagens menores, à direita).")),
  ["razão", "engrenagens"],
  enun=p(T(159, 0).replace("mountain bike", "<em>mountain bike</em>")) + "[[fig:1]]" + p(T(159, 2))
       + tabela(["Engrenagens", "1ª", "2ª", "3ª", "4ª", "5ª", "6ª"], [["Nº de dentes da coroa", "46", "36", "26", "-", "-", "-"], ["Nº de dentes da catraca", "24", "22", "20", "18", "16", "14"]])
       + p(T(159, 4), T(159, 5)) + tabela(["I", "II", "III", "IV", "V"], [["1ª × 1ª", "1ª × 6ª", "2ª × 4ª", "3ª × 1ª", "3ª × 6ª"]]) + p(PP(159)[-1]))
X(160, "Análise combinatória", "<p>A logomarca tem seis regiões, e cada região, depois da primeira, faz fronteira com apenas uma região já pintada quando se pinta na ordem certa. A primeira pode receber qualquer das 4 cores, e cada uma das outras cinco, qualquer cor diferente da vizinha: 4 · 3 · 3 · 3 · 3 · 3 = <strong>972</strong>. Alternativa <strong>E</strong>.</p><p>É a resolução que leva ao gabarito oficial; ela não exige que as quatro cores apareçam todas.</p>",
  figs(("q160", "Logomarca da Copa de 2014: mãos estilizadas que se unem formando a taça, com a frase “Juntos num só ritmo”.")),
  ["princípio multiplicativo", "coloração de mapas"],
  enun=p(T(160, 0).replace("o slogan", "o <em>slogan</em>")) + "[[fig:1]]" + fonte(T(160, 2)) + p(T(160, 3)))
X(161, "Função quadrática", "<p>A tela cerca as quatro laterais: 2X + 2Y = 100, então Y = 50 − X. A área da base é A = X(50 − X), uma parábola com máximo no vértice, X = 25. Então Y = 25: <strong>25 e 25</strong>. Alternativa <strong>D</strong>.</p><p>Entre retângulos de mesmo perímetro, o quadrado tem a maior área.</p>",
  figs(("q161", "Viveiro em forma de bloco retangular, com a base de lados X e Y e o topo abaixo do nível do mar.")),
  ["máximo da parábola", "perímetro"], enun=p(T(161, 0)) + "[[fig:1]]" + p(T(161, 3).replace("de X e de Y", "de <em>X</em> e de <em>Y</em>")))
X(162, "Funções", "<p>De (p + a)(v + b) = K, com K &gt; 0, vem " + K("v = \\dfrac{K}{p + a} - b") + ": v é inversamente proporcional a (p + a), deslocada. O gráfico é um <strong>ramo de hipérbole</strong>. Alternativa <strong>E</strong>.</p>",
  tags=["hipérbole", "função racional"],
  enun=p("O fisiologista inglês Archibald Vivian Hill propôs, em seus estudos, que a velocidade <em>v</em> de contração de um músculo ao ser submetido a um peso <em>p</em> é dada pela equação (<em>p</em> + <em>a</em>) (<em>v</em> + <em>b</em>) = <em>K</em>, com <em>a</em>, <em>b</em> e <em>K</em> constantes.", T(162, 1))
       + tabela(["Tipo de curva"], [["Semirreta oblíqua"], ["Semirreta horizontal"], ["Ramo de parábola"], ["Arco de circunferência"], ["Ramo de hipérbole"]])
       + p("O fisioterapeuta analisou a dependência entre <em>v</em> e <em>p</em> na equação de Hill e a classificou de acordo com sua representação geométrica no plano cartesiano, utilizando o par de coordenadas (<em>p</em> ; <em>v</em>). Admita que <em>K</em> &gt; 0.") + fonte(T(162, 4)) + p(T(162, 5)))
X(163, "Otimização", "<p>Opções para visitar os dois topos e voltar ao solo:</p><ul><li>sobe o 1, teleférico 1→2, desce o 2: 0,15 + 2,00 + 2,30 = 4,45;</li><li>sobe o 2, teleférico 2→1, desce o 1: 1,80 + 2,50 + 0,10 = 4,40;</li><li>sobe e desce o 1, depois sobe e desce o 2, a pé entre eles: 0,15 + 0,10 + 1,80 + 2,30 = 4,35.</li></ul><p>O menor custo é <strong>R$ 4,35</strong>. Alternativa <strong>C</strong>.</p>",
  figs(("q163", "Dois mirantes cilíndricos, o 1 baixo e o 2 alto, ligados no topo por um cabo de teleférico.")),
  ["comparação de custos"], enun=p(T(163, 0)) + "[[fig:1]]" + p(T(163, 3)) + LISTA(T(163, 4)) + p(T(163, 5), T(163, 6)))
X(164, "Razão e proporção", "<p>Com a mesma velocidade, a distância às cegas é proporcional ao tempo olhando o celular. O tempo de X é 25% do de Y, isto é, 1/4. A razão entre as distâncias de X e Y é <strong>1/4</strong>. Alternativa <strong>B</strong>.</p>",
  tags=["grandezas proporcionais"], alts=FR("\\dfrac{5}{4}", "\\dfrac{1}{4}", "\\dfrac{4}{3}", "\\dfrac{4}{1}", "\\dfrac{3}{4}"))
X(165, "Gráficos", "<p>No Gráfico 1, que começa em zero, as alturas são 70 e 30: razão B/A = 30/70 = 3/7. No Gráfico 2, o eixo começa em 20, e as alturas visíveis são 50 e 10: razão 10/50 = 1/5.</p><p>Diferença: 3/7 − 1/5 = 15/35 − 7/35 = <strong>8/35</strong>. Alternativa <strong>E</strong>.</p>",
  figs(("q165a", "Gráfico 1: colunas de eleitores (%) com eixo começando em 0; candidato A com 70% e B com 30%."),
       ("q165b", "Gráfico 2: as mesmas colunas, com o eixo começando em 20; A chega a 70 e B a 30, mas a coluna de B parece muito menor.")),
  ["gráfico de colunas", "razão"], enun=p(T(165, 0)) + "[[fig:1]]" + p(T(165, 3)) + "[[fig:2]]" + p(T(165, 6), T(165, 7)),
  alts=FR("0", "\\dfrac{1}{2}", "\\dfrac{1}{5}", "\\dfrac{2}{15}", "\\dfrac{8}{35}"))
X(166, "Trigonometria", "<p>A = média entre a máxima e a mínima: (120 + 78) ÷ 2 = 99. B = metade da diferença: (120 − 78) ÷ 2 = 21.</p><p>São 90 batimentos por minuto, 1,5 por segundo: período de 2/3 s. Então k = 2π ÷ (2/3) = 3π. P(t) = 99 + 21 cos(3πt). Alternativa <strong>A</strong>.</p>",
  tags=["função cosseno", "período"],
  enun=p("Um cientista, em seus estudos para modelar a pressão arterial de uma pessoa, utiliza uma função do tipo <em>P</em>(<em>t</em>) = <em>A</em> + <em>B</em>cos(<em>kt</em>) em que <em>A</em>, <em>B</em> e <em>K</em> são constantes reais positivas e <em>t</em> representa a variável tempo, medida em segundo. Considere que um batimento cardíaco representa o intervalo de tempo entre duas sucessivas pressões máximas.", T(166, 1))
       + tabela(["Dado", "Valor"], [["Pressão mínima", "78"], ["Pressão máxima", "120"], ["Número de batimentos cardíacos por minuto", "90"]]) + p(T(166, 3)),
  alts=FR("P(t) = 99 + 21\\cos(3\\pi t)", "P(t) = 78 + 42\\cos(3\\pi t)", "P(t) = 99 + 21\\cos(2\\pi t)", "P(t) = 99 + 21\\cos(t)", "P(t) = 78 + 42\\cos(t)"))
X(167, "Geometria espacial", "<p>Para sobrar a maior área para os doces, a calota cortada deve ser a menor possível, com o raio de corte mínimo, r = 3 cm. O centro O, o centro A do corte e o ponto B da borda formam um triângulo retângulo com hipotenusa 5 (raio do melão): OA = √(25 − 9) = 4 cm.</p><p>A altura da calota é h = 5 − 4 = <strong>1 cm</strong>. Alternativa <strong>C</strong>.</p><p>4 cm (D) é a distância do centro ao corte, não a altura da calota.</p>",
  figs(("q167", "Esfera de centro O cortada por um plano horizontal perto da base: a seção circular tem centro A e raio r até o ponto B; a calota de altura h, abaixo do corte, será eliminada, e a parte de cima receberá os doces.")),
  ["calota esférica", "teorema de Pitágoras"], enun=p(T(167, 0).replace("raio r da", "raio <em>r</em> da")) + "[[fig:1]]" + p(T(167, 3).replace("altura h,", "altura <em>h</em>,")),
  alts={**FR("5 - \\dfrac{\\sqrt{91}}{2}", "10 - \\sqrt{91}"), "C": "1", "D": "4", "E": "5"})
X(168, "Função quadrática", "<p>Pondo o eixo de simetria da parábola em x = 0, ela é y = H − kx². Ela toca o chão nas pontas da base de 5 m: x = 2,5, y = 0. E passa a 3 m de altura em x = 2 (largura de 4 m):</p><p>H = 6,25k e H − 4k = 3 → 2,25k = 3 → k = 4/3 → H = 6,25 · 4/3 = <strong>25/3 m</strong>. Alternativa <strong>D</strong>.</p>",
  figs(("q168", "Figura 1: desenho da Igreja da Pampulha, com uma seta indicando uma das abóbadas. Figura 2: vista frontal da abóbada em forma de parábola, de altura H; a 3 metros do chão a largura é de 4 metros, e na base é de 5 metros.")),
  ["parábola", "sistema de equações"], enun=p(T(168, 0)) + "[[fig:1]]" + p(PP(168)[-1]),
  alts=FR("\\dfrac{16}{3}", "\\dfrac{31}{5}", "\\dfrac{25}{4}", "\\dfrac{25}{3}", "\\dfrac{75}{2}"))
X(169, "Porcentagem", "<p>Taxa de aumento de cada <em>site</em>:</p><ul><li>X: 12 → 21, aumento de 9/12 = 75%;</li><li>Y: 30 → 51, 21/30 = 70%;</li><li>Z: 10 → 11, 10%;</li><li>W: 38 → 57, 50%;</li><li>U: 40 → 56, 40%.</li></ul><p>A maior taxa é a do <em>site</em> <strong>X</strong>. Alternativa <strong>A</strong>.</p><p>O maior aumento absoluto é o de Y (21 minutos), mas a pergunta é sobre a taxa.</p>",
  figs(("q169", "Dois gráficos de setores, sexta-feira e sábado, com o tempo de acesso em minutos. Sexta: site X 12, Y 30, Z 10, W 38, U 40. Sábado: X 21, Y 51, Z 11, W 57, U 56.")),
  ["taxa de variação", "gráfico de setores"], enun=p(T(169, 0).replace("cinco sites", "cinco <em>sites</em>").replace("cinco sites", "cinco <em>sites</em>")) + "[[fig:1]]" + p(PP(169)[-1].replace("no site", "no <em>site</em>")))
X(170, "Leitura de escalas", "<p>A máxima é indicada pelo nível inferior do filete preto na coluna da direita, cuja escala cresce de baixo para cima. Nessa coluna, o filete preto vai do topo até pouco abaixo da marca de 20 °C: a leitura é de cerca de <strong>19 °C</strong>. Alternativa <strong>E</strong>.</p><p>Na coluna da esquerda, o fim do filete preto marca a mínima, perto de −5 °C.</p>",
  figs(("q170", "Termômetro de máxima e mínima com duas colunas. A da esquerda vai de −30 °C (em cima) a 50 °C (embaixo); a da direita, de 50 °C (em cima) a −30 °C (embaixo). Em cada coluna há um filete preto no alto e um filete cinza embaixo; o filete preto da direita termina logo abaixo da marca de 20.")),
  ["leitura de instrumento", "números negativos"],
  enun=p(T(170, 0)) + "[[fig:1]]" + p(T(170, 2), "A leitura é feita da seguinte maneira:") + LISTA(T(170, 3).split("maneira:")[1]) + fonte(T(170, 4)) + p(T(170, 5)))
X(171, "Circunferência", "<p>Em 25 h, cada torre dá uma volta, percorrendo o comprimento da sua circunferência, 2πr = 6r (π ≈ 3):</p><ul><li>T1 (r = 50 m): 300 m ÷ 25 h = 12 m/h;</li><li>T2 (r = 100 m): 600 ÷ 25 = 24 m/h;</li><li>T3 (r = 150 m): 900 ÷ 25 = 36 m/h.</li></ul><p>Alternativa <strong>A</strong>.</p><p>Usar r² em vez de r leva à alternativa E, com áreas em vez de comprimentos.</p>",
  figs(("q171a", "Foto de um pivô central de irrigação: uma torre metálica no centro de uma plantação, com um longo braço apoiado em torres sobre rodas."),
       ("q171b", "Vista de cima: três circunferências concêntricas tracejadas em torno da BASE, com as torres T1, T2 e T3 alinhadas num raio.")),
  ["comprimento da circunferência", "velocidade"],
  enun=p(T(171, 0)) + "[[fig:1]][[fig:2]]" + p("Um pivô de três torres (T<sub>1</sub>, T<sub>2</sub> e T<sub>3</sub>) será instalado em uma fazenda, sendo que as distâncias entre torres consecutivas bem como da base à torre T<sub>1</sub> são iguais a 50 m. O fazendeiro pretende ajustar as velocidades das torres, de tal forma que o pivô efetue uma volta completa em 25 horas. Use 3 como aproximação para π.", "Para atingir seu objetivo, as velocidades das torres T<sub>1</sub>, T<sub>2</sub> e T<sub>3</sub> devem ser, em metro por hora, de"))
X(172, "Gráficos", "<p>Atenção às escalas: o reservatório A é lido no eixo da esquerda (até 180 000 L), e o B, no da direita (até 90 000 L). Os dois só têm a mesma quantidade quando os valores lidos são iguais. De 8 h a 9 h, A está em 30 000 L (eixo esquerdo), e B também está em 30 000 L (eixo direito). Fora desse trecho, os valores não coincidem por um intervalo de tempo. São <strong>1 hora</strong>. Alternativa <strong>A</strong>.</p><p>Os pontos em que as linhas se cruzam no desenho não indicam quantidades iguais, porque as escalas são diferentes.</p>",
  figs(("q172", "Gráfico “Quantidade de água armazenada”, de 0 a 20 h, com dois eixos verticais: o da esquerda, do reservatório A, de 0 a 180 000 L; o da direita, do reservatório B, de 0 a 90 000 L. A (círculos) sobe até 60 000 L em 4 h, desce até 30 000 L em 8 h, fica assim até 9 h e depois sobe até 180 000 L em 19 h. B (triângulos) sobe até 30 000 L em 4 h, fica constante até 10 h, sobe até 75 000 L em 16 h, fica constante até 18 h e chega a 90 000 L em 20 h.")),
  ["leitura de gráfico", "escalas"], enun=p(T(172, 0)) + "[[fig:1]]" + p(PP(172)[-1]),
  alts=dict(D[172]["alternativas"], E="6."))  # o rótulo "Reservatório B" do eixo grudava na alternativa E
X(173, "Razão e proporção", "<p>O carro consumiu 4/10 de 100 kg = 40 kg; restaram 60 kg. A equipe pôs a terça parte disso: 20 kg. Com densidade de 750 g/L = 0,75 kg/L, o volume é " + K("\\dfrac{20}{0{,}75}") + " litros. Alternativa <strong>B</strong>.</p><p>Dividir por 7,5 ou por 0,075 (A e C) é errar a conversão de gramas para quilogramas.</p>",
  tags=["densidade", "frações"], alts=FR("\\dfrac{20}{0{,}075}", "\\dfrac{20}{0{,}75}", "\\dfrac{20}{7{,}5}", "20 \\times 0{,}075", "20 \\times 0{,}75"))
X(174, "Estatística", "<p>São 14 valores (março de 2008 a abril de 2009). Em ordem: 6,8; 7,5; 7,6; 7,6; 7,7; 7,9; 7,9; 8,1; 8,2; 8,5; 8,5; 8,6; 8,9; 9,0.</p><p>A mediana é a média do 7º e do 8º: (7,9 + 8,1) ÷ 2 = <strong>8,0%</strong>. Alternativa <strong>B</strong>.</p>",
  figs(("q174", "Gráfico de linha da taxa de desemprego (%), de março de 2008 a abril de 2009, com os valores: 8,6; 8,5; 7,9; 7,9; 8,1; 7,6; 7,7; 7,5; 7,6; 6,8; 8,2; 8,5; 9,0; 8,9.")),
  ["mediana"], enun=p(T(174, 0)) + "[[fig:1]]" + fonte("IBGE. <strong>Pesquisa mensal de emprego</strong>. Disponível em: www.ibge.gov.br. Acesso em: 30 jul. 2012 (adaptado).") + p(PP(174)[-1]))
X(175, "Probabilidade", "<p>Exatamente um verde entre 10: escolhe-se qual semáforo é o verde (10 maneiras), com probabilidade 2/3, e os outros 9 são vermelhos, (1/3)<sup>9</sup>:</p><p>" + K("10 \\cdot \\dfrac{2}{3} \\cdot \\left(\\dfrac{1}{3}\\right)^9 = \\dfrac{10 \\times 2}{3^{10}}") + ". Alternativa <strong>A</strong>.</p><p>Sem o fator 10 (E), conta-se só um semáforo específico como o verde.</p>",
  tags=["distribuição binomial"],
  enun=p("Numa avenida existem 10 semáforos. Por causa de uma pane no sistema, os semáforos ficaram sem controle durante uma hora, e fixaram suas luzes unicamente em verde ou vermelho. Os semáforos funcionam de forma independente; a probabilidade de acusar a cor verde é de " + K("\\tfrac{2}{3}") + " e a de acusar a cor vermelha é de " + K("\\tfrac{1}{3}") + ". Uma pessoa percorreu a pé toda essa avenida durante o período da pane, observando a cor da luz de cada um desses semáforos.", PP(175)[-1]),
  alts=FR("\\dfrac{10 \\times 2}{3^{10}}", "\\dfrac{10 \\times 2^9}{3^{10}}", "\\dfrac{2^{10}}{3^{100}}", "\\dfrac{2^{90}}{3^{100}}", "\\dfrac{2}{3^{10}}"))
X(176, "Porcentagem", "<p>Na 1ª fase: 200 m² elétricos × 1 = 200 kWh e 200 m² térmicos × 0,7 = 140 kWh; total 340 kWh por dia. O dobro é 680 kWh.</p><p>Na 2ª fase, a área elétrica sobe 75%: 350 m², 350 kWh. Faltam 680 − 350 = 330 kWh térmicos: 330 ÷ 0,7 ≈ <strong>472 m²</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["porcentagem", "equação"], enun=(p(*PP(176)[:3]) + fonte(T(176, 3)) + p(PP(176)[3])).replace("do campus de", "do <em>campus</em> de").replace("no campus,", "no <em>campus</em>,"))
X(177, "Análise combinatória", "<p>Número de senhas em cada formato (26 letras, 10 dígitos):</p><ul><li>I (LDDDDD): 26 · 10<sup>5</sup> = 2 600 000;</li><li>II (DDDDDD): 10<sup>6</sup> = 1 000 000;</li><li>III (LLDDDD): 26² · 10<sup>4</sup> = 6 760 000;</li><li>IV (DDDDD): 10<sup>5</sup> = 100 000;</li><li>V (LLLDD): 26³ · 10² = 1 757 600.</li></ul><p>Só a opção <strong>V</strong> fica entre 1 milhão (exclusive) e 2 milhões. Alternativa <strong>E</strong>.</p><p>A II dá exatamente 1 milhão, que não é superior ao número de clientes.</p>",
  tags=["princípio multiplicativo", "senhas"],
  enun=p(T(177, 0)) + tabela(["Opção", "Formato"], [["I", "LDDDDD"], ["II", "DDDDDD"], ["III", "LLDDDD"], ["IV", "DDDDD"], ["V", "LLLDD"]]) + p(*PP(177)[1:]))
X(178, "Análise combinatória", "<p>Cada partida é um par de jogadores, sem importar a ordem: com n jogadores, são n(n − 1)/2 partidas (o quadro confere: 7 jogadores dão 21). Com 8: 8 · 7 ÷ 2 = <strong>28</strong>. Alternativa <strong>E</strong>.</p><p>8 · 7 = 56 (B) contaria cada jogo duas vezes.</p>",
  tags=["combinação", "sequências"],
  enun=p(T(178, 0).replace("utilizando videogame", "utilizando <em>videogame</em>")) + tabela(["Quantidade de jogadores", "2", "3", "4", "5", "6", "7"], [["Número de partidas", "1", "3", "6", "10", "15", "21"]]) + p(PP(178)[-1]))
X(179, "Probabilidade", "<p>Soma das duas situações: chove e ele se atrasa, 0,3 × 0,5 = 0,15; não chove e ele se atrasa, 0,7 × 0,25 = 0,175.</p><p>Total: 0,15 + 0,175 = <strong>0,325</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["probabilidade total"])
X(180, "Taxa de variação", "<p>De 17 h 15 a 18 h (45 min), a chuva sobe o nível 20 cm: 4/9 cm/min. De 18 h a 18 h 40 (40 min), com chuva e ralo juntos, o nível cai 5 cm: −1/8 cm/min. Logo o ralo, sozinho, baixa 4/9 + 1/8 = 41/72 cm/min.</p><p>Depois que a chuva para, faltam 15 cm: 15 ÷ (41/72) = 1 080/41 ≈ 26,3 min. 18 h 40 + 26 min ≈ 19 h 06: entre <strong>19 h e 19 h 10 min</strong>. Alternativa <strong>D</strong>.</p>",
  tags=["vazão", "proporcionalidade"])

completar(Q, R)
