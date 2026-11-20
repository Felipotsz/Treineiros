# Enem 2012, 2º dia, caderno azul: Matemática (questões 136 a 180; no site, 1 a 45).
# Texto legível; quadros e tabelas em HTML; fórmulas e matrizes em KaTeX. Alternativas-imagem nas Q153, Q156, Q165 e Q170.
# Sem anuladas nesta área. Q157: gabarito oficial 88 (a contagem estrita dá 89; a explicação registra isso).

import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, paragrafos_enem

ID = "enem-2012-matematica"
META = {"id": ID, "banca": "Enem", "ano": 2012, "titulo": "Enem 2012: Matemática", "fonte": "Inep", "dataExame": "2012-11-04",
        "duracaoMinutos": 150, "area": "Matemática", "caderno": "azul", "dia": 2}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2012-dia2-azul")
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

CAP = lambda x: f'<p class="apoio" style="text-align:center">{x}</p>'
SUP = lambda s: re.sub(r"\b(m|cm|km)([23])\b", lambda m: f"{m.group(1)}<sup>{m.group(2)}</sup>", s)


X(136, "Escala", "<p>Karnazes correu dez vezes 42 km, ou seja, 420 km = 42 000 000 cm. A pista do professor tem 60 cm. A escala é 60 : 42 000 000, que, dividindo por 60, dá <strong>1 : 700 000</strong>. Alternativa <strong>D</strong>.</p><p>Quem usa 42 km, e não 420 km, chega a 1 : 70 000 (C).</p>",
  tags=["escala", "conversão de unidades"], enun=p(T(136, 0), T(136, 1)) + fonte(T(136, 2)) + p(T(136, 3)))
X(137, "Geometria plana", "<p>Na Figura 1, as quatro circunferências têm raio r, e cada lado do losango liga dois centros tangentes: lado 2r, perímetro 8r. Na Figura 2, duas circunferências opostas passam a ter raio 2r, e cada lado liga uma de raio r a uma de raio 2r: lado 3r, perímetro 12r. O aumento é de 4r sobre 8r, ou seja, <strong>50%</strong>. Alternativa <strong>E</strong>.</p>",
  figs(("q137a", "Figura 1: quatro circunferências iguais, tangentes duas a duas, dispostas em cruz; seus centros são os vértices de um losango."),
       ("q137b", "Figura 2: as duas circunferências da esquerda e da direita ficaram maiores (raio dobrado), e as de cima e de baixo continuam pequenas; o losango dos centros ficou maior.")),
  ["perímetro", "circunferências tangentes"], enun=p(T(137, 0)) + "[[fig:1]]" + CAP("Figura 1") + p(T(137, 3)) + "[[fig:2]]" + CAP("Figura 2") + p(T(137, 6)))
X(138, "Razão e proporção", "<p>Na primeira parte, a divisão 6 : 5 : 4 tem 15 partes. Na segunda, 4 : 4 : 2 tem 10 partes, o que equivale a 6 : 6 : 3 em 15 partes. José fica com 6 partes, Carlos passa de 5 para 6 e Paulo cai de 4 para 3. Quem levou 50 a mais foi Carlos, com uma parte a mais: cada parte vale 50 e o total é 750 laranjas. Na segunda parte: 300, 300 e 150. Alternativa <strong>B</strong>.</p>",
  tags=["divisão proporcional"])
X(139, "Probabilidade", "<p>Pelo gráfico, 21% não opinaram, então 79% dos 500 visitantes opinaram, e 12% acharam o conto “Chato”. A probabilidade, entre os que opinaram, é \\(\\dfrac{12}{79} \\approx 0{,}15\\). Alternativa <strong>D</strong>.</p><p>A opção 0,12 (B) usa todos os visitantes, inclusive os que não opinaram.</p>",
  figs(("q139", "Gráfico de barras horizontais “Contos de Halloween: opinião dos visitantes”: Divertido 52%, Assustador 15%, Chato 12%, Não opinaram 21%.")),
  ["probabilidade condicional", "leitura de gráfico"], enun=EF(139, 2), trocas=[("blog", "<em>blog</em>")])
_o, _r = T(140, 1).split(" Arthur tem", 1)
X(140, "Matemática financeira", "<p>Com o dinheiro aplicado a 10% ao semestre, cada pagamento futuro vale hoje o valor dividido por 1,1 (6 meses) ou 1,21 (12 meses). Opção 2: 30 000 + 26 000 ÷ 1,1 ≈ 53 636. Opção 3: 20 000 + 18 182 + 14 876 ≈ 53 058. Opção 4: 15 000 + 39 000 ÷ 1,21 ≈ 47 231. Opção 5: 60 000 ÷ 1,21 ≈ 49 587. À vista: 55 000. A mais vantajosa é a <strong>opção 4</strong>. Alternativa <strong>D</strong>.</p>",
  tags=["valor presente", "juros compostos"], enun=p(T(140, 0)) + LISTA(_o) + p("Arthur tem" + _r, T(140, 2)))
X(141, "Expressões algébricas", "<p>A área original é 5 · 3 = 15, e depois da lavagem é (5 − x)(3 − y) = 15 − 5y − 3x + xy. A área perdida é a diferença: 15 − (15 − 5y − 3x + xy) = <strong>5y + 3x − xy</strong>. Alternativa <strong>E</strong>.</p><p>O termo xy é subtraído porque o cantinho x por y foi contado duas vezes nas faixas 5y e 3x.</p>",
  figs(("q141", "Retângulo de comprimento 5 e largura 3; uma faixa de largura x na direita e uma faixa de altura y embaixo indicam o encolhimento.")),
  ["produto notável", "área"], enun=p(T(141, 0)) + "[[fig:1]]" + p(T(141, 3)))
_l, _s = T(142, 1).split(" Será instalado", 1)
X(142, "Grandezas e medidas", "<p>A sala tem 4 × 5 = 20 m², então 20 × 600 = 12 000 BTU/h, valendo para até duas pessoas. Há duas pessoas a mais: + 1 200. A televisão: + 600. Total: <strong>13 800 BTU/h</strong>. Alternativa <strong>D</strong>.</p><p>Quem soma 600 para cada uma das quatro pessoas chega a 15 000 (E).</p>",
  tags=["área", "interpretação de regras"], enun=p(T(142, 0)) + LISTA(_l.replace("m2", "m²")) + p("Será instalado" + _s, T(142, 2).replace("ar- condicionado", "ar-condicionado")))
X(143, "Grandezas proporcionais", "<p>S é diretamente proporcional a b e a d² (vão para o numerador) e inversamente proporcional a x² (vai para o denominador), com constante k: \\(S = \\dfrac{k \\cdot b \\cdot d^2}{x^2}\\). Alternativa <strong>A</strong>.</p><p>As outras opções esquecem algum quadrado ou o colocam na grandeza errada.</p>",
  figs(("q143", "Viga em forma de paralelepípedo retângulo, com largura b, altura d e comprimento x indicados.")),
  ["proporcionalidade direta e inversa"], enun=p(T(143, 0)) + "[[fig:1]]" + fonte(T(143, 2).replace("Aplicações da matemática escolar", "<em>Aplicações da matemática escolar</em>")) + p(T(143, 3)),
  alts=FR("S = \\dfrac{k \\cdot b \\cdot d^2}{x^2}", "S = \\dfrac{k \\cdot b \\cdot d}{x^2}", "S = \\dfrac{k \\cdot b \\cdot d^2}{x}", "S = \\dfrac{k \\cdot b^2 \\cdot d}{x}", "S = \\dfrac{k \\cdot b \\cdot 2d}{2x}"))
X(144, "Análise combinatória", "<p>Uma resposta combina um objeto, um personagem e um cômodo: 5 × 6 × 9 = 270 respostas possíveis. Como as respostas não se repetem e há 280 alunos, em algum momento a resposta certa será dada. Há <strong>10 alunos a mais do que possíveis respostas distintas</strong>. Alternativa <strong>A</strong>.</p>",
  tags=["princípio multiplicativo"])
X(145, "Escala", "<p>Na escala a : b, cada unidade do desenho vale b ÷ a na realidade. Contando os quadradinhos, as alturas no desenho são cerca de 9 (I), 9 (II), 6 (III), 4,5 (IV) e 4,5 (V). Reais: I, 9 × 100 = 900; II, 9 × 50 = 450; III, 6 × 150 = 900; IV, 4,5 × 300 = 1 350; V, 4,5 × 150 = 675. A maior é a <strong>árvore IV</strong>. Alternativa <strong>D</strong>.</p><p>IV e V têm o mesmo tamanho no desenho, mas a escala de IV (1 : 300) reduz o dobro da de V (2 : 300). A conclusão não depende da contagem exata: IV é a única com mais de 1 000 em qualquer leitura razoável.</p>",
  figs(("q145", "Malha quadriculada com cinco árvores desenhadas: I e II altas (cerca de 10 quadradinhos), III média (cerca de 6), IV e V baixas (cerca de 4). Escalas: I, 1:100; II, 2:100; III, 2:300; IV, 1:300; V, 2:300.")),
  ["escala", "comparação"], enun=p(T(145, 0)) + "[[fig:1]]" + p(T(145, 3)))
X(146, "Probabilidade", "<p>Depois de passar uma bola da urna 1 para a 2, a urna 2 tem 11 bolas. Para cada cor, a chance é (bolas dessa cor na urna 2 + chance de ter vindo uma dessa cor da urna 1) ÷ 11: amarela (0 + 0,4) ÷ 11; azul (1 + 0,3) ÷ 11; branca (2 + 0,2) ÷ 11; verde (3 + 0,1) ÷ 11; vermelha (4 + 0) ÷ 11. A maior é a <strong>vermelha</strong>. Alternativa <strong>E</strong>.</p>",
  tags=["probabilidade total", "urnas"],
  enun=p(T(146, 0)) + tabela(["Cor", "Urna 1", "Urna 2"], [["Amarela", "4", "0"], ["Azul", "3", "1"], ["Branca", "2", "2"], ["Verde", "1", "3"], ["Vermelha", "0", "4"]]) + p(T(146, 2)) + OL(*[T(146, i)[4:] for i in range(3, 7)]) + p(T(146, 7)))
X(147, "Sistema de numeração", "<p>O mostrador indica 3534 m³ = 3 534 000 litros, mais 8 centenas e 5 dezenas de litros: 3 534 850 L. O relógio dos litros marca 9 e o dos décimos marca 3,5, somando 9,35 L. Total: <strong>3 534 859,35 litros</strong>. Alternativa <strong>D</strong>.</p><p>A opção C ignora os dois relógios de ponteiro.</p>",
  figs(("q147", "Hidrômetro com mostrador 3 5 3 4 8 5 (quatro primeiros algarismos em m³, depois centenas e dezenas de litros; 1 m³ = 1 000 litros) e dois relógios de ponteiro: o de litros aponta para 9, e o de décimos de litro, entre 3 e 4.")),
  ["leitura de instrumentos", "conversão de unidades"], enun=SUP(p(T(147, 0))) + "[[fig:1]]" + fonte(T(147, 2)) + p(T(147, 3)))
X(148, "Leitura de gráficos", "<p>No gráfico de linha das vendas de 2011, o ponto mais alto é o de junho e o mais baixo é o de agosto. Setembro tem um pico alto, mas abaixo de junho. A maior e a menor venda foram em <strong>junho e agosto</strong>. Alternativa <strong>E</strong>.</p><p>Os meses em que há quedas ou subidas bruscas (março, abril) não são os extremos absolutos.</p>",
  figs(("q148", "Gráfico de linha das vendas em reais, de janeiro a dezembro de 2011, sem valores no eixo: a linha sobe até março, cai em abril, sobe até o ponto mais alto em junho, cai em julho até o ponto mais baixo em agosto, sobe muito em setembro, cai em outubro, sobe em novembro e cai um pouco em dezembro.")),
  ["gráfico de linha", "máximo e mínimo"], enun=p(T(148, 0)) + "[[fig:1]]" + p(T(148, 4)))
X(149, "Geometria espacial", "<p>A primeira planificação tem um retângulo e dois círculos: cilindro. A segunda tem cinco retângulos em fila e dois pentágonos: prisma de base pentagonal. A terceira é um triângulo com três triângulos em volta: pirâmide de base triangular. São <strong>cilindro, prisma de base pentagonal e pirâmide</strong>. Alternativa <strong>A</strong>.</p>",
  figs(("q149a", "Planificação 1: um retângulo com um círculo encostado em cima e outro embaixo."),
       ("q149b", "Planificação 2: cinco retângulos lado a lado, com um pentágono em cima e outro embaixo do retângulo central."),
       ("q149c", "Planificação 3: um grande triângulo dividido em quatro triângulos, o central mais claro.")),
  ["planificação", "sólidos"], enun=p(T(149, 0)) + "[[fig:1]][[fig:2]][[fig:3]]" + p(T(149, 4)))
X(150, "Progressão aritmética", "<p>As colunas têm 1, 2, 3, ..., 7 cartas: 1 + 2 + ... + 7 = \\(\\dfrac{7 \\cdot 8}{2} = 28\\) cartas. Sobram 52 − 28 = <strong>24 cartas</strong> no monte. Alternativa <strong>B</strong>.</p><p>A opção D (28) é o total das colunas, e não o monte.</p>",
  tags=["soma de PA"])
X(151, "Leitura de gráficos", "<p>O texto diz que, com menos gelo, o oceano escuro absorve mais luz e o aquecimento aumenta. No gráfico, a curva de 2007 é a que fica mais baixa em todos os meses, com a menor extensão de gelo. O maior aquecimento foi em <strong>2007</strong>. Alternativa <strong>E</strong>.</p>",
  figs(("q151", "Gráfico de linhas da extensão de gelo marítimo, em milhões de km², de junho a setembro, para 1995, 1998, 2000, 2005 e 2007: todas as curvas caem ao longo dos meses; 1995 fica no alto, e 2007 é a mais baixa de todas, chegando perto de 4 em setembro.")),
  ["gráfico de linhas", "aquecimento global"], enun=p(T(151, 0)) + "[[fig:1]]" + fonte("Disponível em: http://sustentabilidade.allianz.com.br. Acesso em: fev. 2012 (adaptado).") + p("Com base no gráfico e nas informações do texto, é possível inferir que houve maior aquecimento global em"))
X(152, "Geometria plana", "<p>Para o quadrado caber inteiro no círculo, a diagonal L√2 não pode passar do diâmetro 2R: 2R ≥ L√2, ou seja, \\(R \\geq \\dfrac{L}{\\sqrt{2}}\\). Alternativa <strong>A</strong>.</p><p>R ≥ L/2 (D) só garante que o círculo alcança o meio dos lados; os cantos ficariam para fora.</p>",
  tags=["quadrado inscrito", "diagonal"], trocas=[(" R ", " <em>R</em> "), (" L ", " <em>L</em> ")],
  alts=FR("R \\geq \\dfrac{L}{\\sqrt{2}}", "R \\geq \\dfrac{2L}{\\pi}", "R \\geq \\dfrac{L}{\\sqrt{\\pi}}", "R \\geq \\dfrac{L}{2}", "R \\geq \\dfrac{L}{2\\sqrt{2}}"))
X(153, "Geometria espacial", "<p>A circunferência do motoqueiro passa por A e B, então está num plano vertical que contém AB. A luz sai de B: os raios que passam pelos pontos desse plano continuam no mesmo plano e atingem o chão na reta em que ele corta o chão. A sombra do trajeto é um <strong>segmento de reta</strong>. Alternativa <strong>E</strong>.</p><p>O círculo (A) seria a sombra de uma trajetória horizontal.</p>",
  figs(("q153", "Figura 1: foto de um globo da morte, uma esfera de grade de aço. Figura 2: esfera com o ponto B no topo e o ponto A embaixo, ligados por um diâmetro vertical, e um círculo horizontal no meio."),
       ("q153a", "Alternativa A: uma circunferência."),
       ("q153b", "Alternativa B: um arco de circunferência aberto à direita."),
       ("q153c", "Alternativa C: dois arcos formando uma figura de lente."),
       ("q153d", "Alternativa D: um círculo preto pequeno, cheio."),
       ("q153e", "Alternativa E: um segmento de reta vertical.")),
  ["projeção", "esfera"], enun=p(T(153, 0) + " " + T(153, 1)) + "[[fig:1]]" + p(T(153, 7), T(153, 8)) + fonte(T(153, 9)) + p(T(153, 10)), alts=ALT(2))
X(154, "Grandezas e medidas", "<p>Pela figura, o cadeirante alcança alturas de 0,40 m (mínimo) a 1,35 m (máximo). A tomada a 0,20 m está baixa demais, e o interruptor a 1,47 m, alto demais. A única proposta com as duas alturas dentro da faixa é <strong>0,45 m e 1,20 m</strong>. Alternativa <strong>E</strong>.</p><p>As opções A a D mantêm a tomada abaixo de 0,40 m.</p>",
  figs(("q154", "Pessoa em cadeira de rodas estendendo o braço, com uma régua de alturas ao lado: 0,40 m mínimo, faixa confortável de 0,80 m a 1,00 m, 1,20 m e 1,35 m máximo.")),
  ["intervalos", "acessibilidade"], enun=p(T(154, 0)) + "[[fig:1]]" + p(T(154, 2)))
X(155, "Leitura de tabelas", "<p>As atividades escolares tomam 5 horas por dia útil e 1 hora por dia de fim de semana: 5 × 5 + 2 × 1 = <strong>27 horas</strong>. Alternativa <strong>E</strong>.</p><p>Quem multiplica por 7 só um dos valores, ou soma 5 + 1 sem considerar a quantidade de dias, chega a outra opção.</p>",
  tags=["tabela", "operações"],
  enun=p(T(155, 0)) + tabela(["Rotina Juvenil", "Durante a semana", "No fim de semana"], [["Assistir à televisão", "3", "3"], ["Atividades domésticas", "1", "1"], ["Atividades escolares", "5", "1"], ["Atividades de lazer", "2", "4"], ["Descanso, higiene e alimentação", "10", "12"], ["Outras atividades", "3", "3"]]) + p(T(155, 3) + " " + T(155, 4)))
X(156, "Funções", "<p>O salário é 750 + 3n até 100 produtos (750 a 1 050) e, a partir daí, aumenta 9 por produto: com 200 produtos, 1 050 + 100 × 9 = 1 950. O gráfico tem dois trechos de reta, o segundo mais inclinado, começando em 750: é o da <strong>alternativa E</strong>. Alternativa <strong>E</strong>.</p><p>No gráfico B a inclinação diminui depois de 100, e no C o salário fica parado no início.</p>",
  figs(("q156a", "Alternativa A: uma única reta subindo devagar, de 750 em 0 produto até cerca de 1 400 em 200."),
       ("q156b", "Alternativa B: reta subindo de 750 até cerca de 1 600 em 100 produtos e depois subindo mais devagar até 2 000 em 200."),
       ("q156c", "Alternativa C: segmento horizontal em 750 de 0 a 100 produtos e depois subindo até cerca de 1 650 em 200."),
       ("q156d", "Alternativa D: segmento horizontal em 750 de 0 a 200 produtos."),
       ("q156e", "Alternativa E: reta subindo devagar de 750 até cerca de 1 050 em 100 produtos e depois mais inclinada até cerca de 1 950 em 200.")),
  ["função definida por partes", "gráfico"], enun=p(T(156, 0) + " " + T(156, 1), T(156, 2)), alts=ALT(1))
X(157, "Sequências", "<p>O raciocínio do gabarito: viajando a cada 4 dias, ele faria cerca de 365 ÷ 4 ≈ 91 viagens no ano. As férias, de 1º a 10 de junho, coincidem com 3 viagens (nos dias 153, 157 e 161 do ano), que ele perde: 91 − 3 = <strong>88 viagens</strong>. Alternativa <strong>C</strong>.</p><p>Uma contagem estrita dá outro número: as viagens nos dias 1, 5, ..., 149 somam 38, e, voltando no dia 162, as dos dias 162, 166, ..., 362 somam 51, num total de 89 (D). O gabarito oficial do Inep é 88.</p>",
  tags=["progressão aritmética", "calendário"])
X(158, "Geometria espacial", "<p>A base do tanque mede 40 × 30 = 1 200 cm². Um objeto de 2 400 cm³ faz o nível subir 2 400 ÷ 1 200 = 2 cm. A água tinha 25 − 5 = 20 cm e passa a 22 cm, abaixo dos 25 cm do tanque. Alternativa <strong>C</strong>.</p><p>Quem usa a base 40 × 25 ou outra face chega a valores diferentes.</p>",
  figs(("q158", "Tanque em forma de paralelepípedo de 40 cm por 30 cm de base e 25 cm de altura, com água até 5 cm abaixo da borda.")),
  ["volume", "deslocamento de líquido"], enun=p(T(158, 0)) + "[[fig:1]]" + SUP(p(T(158, 3))))
X(159, "Áreas", "<p>Pela planta: I = 5 × 8 = 40 m²; II = 5 × 6 = 30 m²; III = 4 × 6 = 24 m²; IV é um trapézio de bases 6 e 4 e altura 7: (6 + 4) × 7 ÷ 2 = 35 m². O modelo A só serve para áreas menores que 35 m² (II e III); I e IV (35 não é menor que 35) precisam do modelo B. São <strong>duas unidades do tipo A e duas do tipo B</strong>. Alternativa <strong>C</strong>.</p>",
  figs(("q159", "Planta em forma de L: ambiente I embaixo à esquerda, 5 m por 8 m; acima dele, ambientes II e III, com 9 m juntos e altura total da planta de 14 m; à direita, o ambiente IV, um trapézio de 7 m de largura com lados de 6 m e 4 m.")),
  ["área de trapézio", "otimização"], enun=SUP(p(T(159, 0))) + "[[fig:1]]" + p(T(159, 4)))
X(160, "Áreas", "<p>O losango ABCD tem diagonais 1 e 1: área 1/2. As regiões claras ABPD e BCDQ são, cada uma, dois triângulos de base 1/4 (AP ou QC) e altura 1/2: área 2 × (1/2 × 1/4 × 1/2) = 1/8. A parte clara tem 1/4 m² e a sombreada, 3/4 m². Custo: 1/4 × 50 + 3/4 × 30 = 12,50 + 22,50 = <strong>R$ 35,00</strong>. Alternativa <strong>B</strong>.</p>",
  figs(("q160", "Quadrado com A, B, C e D nos pontos médios dos lados (esquerda, cima, direita, baixo). O losango ABCD é dividido: perto de A e de C há regiões claras em forma de seta, com P e Q sobre a diagonal AC; o restante do quadrado e o losango central PBQD são sombreados.")),
  ["área de triângulo", "custo"], enun=p(T(160, 0)) + "[[fig:1]]" + p(T(160, 4).replace("m2", "m²").replace("1/4", "\\(\\frac{1}{4}\\)"), T(160, 5)))
X(161, "Sistema de numeração", "<p>O número tem 8 algarismos: 1 3 _ 9 8 2 0 7. Da direita para a esquerda: 7 unidades, 0 dezenas, 2 centenas, 8 unidades de milhar, 9 dezenas de milhar e o espaço vazio na <strong>centena de milhar</strong>. Alternativa <strong>C</strong>.</p><p>O 3 ocupa o milhão e o 1, a dezena de milhão.</p>",
  tags=["valor posicional"], trocas=[("1 3 9 8 2 0 7", "1 3 __ 9 8 2 0 7")])
X(162, "Leitura de gráficos", "<p>Pelo gráfico, a ação valia 150 às 10h, 380 às 13h, 460 às 15h, 100 às 16h e 200 às 17h. Ganho por ação: investidor 1, 460 − 150 = 310; 2, 200 − 150 = 50; 3, 460 − 380 = 80; 4, 100 − 460 = −360; 5, 200 − 100 = 100. O melhor negócio foi do <strong>investidor 1</strong>. Alternativa <strong>A</strong>.</p>",
  figs(("q162", "Gráfico do valor da ação, em reais, das 10h às 17h: 150 às 10h, sobe a 280 às 11h, cai a 200 às 12h, sobe a 380 às 13h, cai a 330 às 14h, chega ao máximo de 460 às 15h, despenca para 100 às 16h e volta a 200 às 17h.")),
  ["leitura de gráfico", "lucro"], enun=p(T(162, 0).replace("XPN", "<em>XPN</em>")) + "[[fig:1]]" + p(T(162, 4))
  + tabela(["Investidor", "Hora da Compra", "Hora da Venda"], [["1", "10:00", "15:00"], ["2", "10:00", "17:00"], ["3", "13:00", "15:00"], ["4", "15:00", "16:00"], ["5", "16:00", "17:00"]]) + p(T(162, 6)))
X(163, "Leitura de gráficos", "<p>A eficiência é muito boa quando a linha contínua (resolvidas) fica acima da tracejada (recebidas). Isso acontece na terça (cerca de 27 contra 20) e na quarta (cerca de 9 contra 5). Na quinta, na sexta e na segunda, a tracejada está acima, e no sábado e no domingo as duas estão em zero. Alternativa <strong>B</strong>.</p>",
  figs(("q163", "Gráfico de linhas de quinta a quarta. Recebidas (tracejada): Qui 17, Sex 15, Sáb 0, Dom 0, Seg 14, Ter 20, Qua 5. Resolvidas (contínua): Qui 16, Sex 11, Sáb 0, Dom 0, Seg 2, Ter 27, Qua 9.")),
  ["comparação de gráficos"], enun=p(T(163, 0)) + "[[fig:1]]" + p(T(163, 3)) + fonte(T(163, 4)) + p(T(163, 5)))
X(164, "Razão e proporção", "<p>São 5 gotas para cada 2 kg. Com 30 gotas, são 30 ÷ 5 = 6 grupos de 2 kg: 6 × 2 = <strong>12 kg</strong>. Alternativa <strong>A</strong>.</p><p>O intervalo de 8 horas é o mesmo da bula e não muda a conta. A opção E (75) multiplica em vez de dividir.</p>",
  tags=["regra de três", "dosagem"])
X(165, "Geometria espacial", "<p>Projetando na base: A fica em A; E, o vértice da pirâmide, vai para o centro do quadrado; M, ponto médio de BC, fica no meio do lado BC; C fica em C. O desenho é um segmento de A ao centro, outro do centro ao meio de BC e outro até C, como no <strong>desenho C</strong>. Alternativa <strong>C</strong>.</p><p>No desenho D a projeção vai direto de A a C, ignorando o desvio até M.</p>",
  figs(("q165", "Pirâmide de base quadrada ABCD e vértice E no alto; o ponto M fica no meio da aresta BC."),
       ("q165a", "Alternativa A: no quadrado ABCD, linha de A para a direita pela base, sobe até a metade, segue para a direita até o lado BC e sobe até C."),
       ("q165b", "Alternativa B: linha de A até um ponto do lado BC, um pouco abaixo da metade, e depois subindo pelo lado até C."),
       ("q165c", "Alternativa C: linha de A subindo na diagonal até o centro do quadrado, depois horizontal até o meio do lado BC e depois subindo até C."),
       ("q165d", "Alternativa D: uma única linha diagonal de A até C."),
       ("q165e", "Alternativa E: linha de A subindo na diagonal até perto do meio, depois vertical até o lado DC e horizontal até C.")),
  ["projeção ortogonal", "pirâmide"], enun=p(T(165, 0)) + "[[fig:1]]" + p(T(165, 2), T(165, 3)), alts=ALT(2))
X(166, "Função afim", "<p>No equilíbrio, Q<sub>O</sub> = Q<sub>D</sub>: −20 + 4P = 46 − 2P, então 6P = 66 e <strong>P = 11</strong>. Alternativa <strong>B</strong>.</p><p>Com P = 11, Q<sub>O</sub> = −20 + 44 = 24 e Q<sub>D</sub> = 46 − 22 = 24: as quantidades se igualam.</p>",
  tags=["equação do 1º grau", "oferta e demanda"],
  enun=p(T(166, 0)) + p("\\(Q_O = -20 + 4P\\)", "\\(Q_D = 46 - 2P\\)") + p("em que Q<sub>O</sub> é quantidade de oferta, Q<sub>D</sub> é a quantidade de demanda e P é o preço do produto.", "A partir dessas equações, de oferta e de demanda, os economistas encontram o preço de equilíbrio de mercado, ou seja, quando Q<sub>O</sub> e Q<sub>D</sub> se igualam.", T(166, 4)))
X(167, "Razão e proporção", "<p>A bicicleta custa 9 200 tíquetes, e a criança ganha 20 por período: 9 200 ÷ 20 = 460 períodos. Cada período custa R$ 3,00: 460 × 3 = <strong>R$ 1 380</strong>. Alternativa <strong>D</strong>.</p><p>A opção B (460) é o número de períodos, e não o valor em reais.</p>",
  tags=["regra de três", "custo"], trocas=[("shopping centers", "<em>shopping centers</em>"), ("certo shopping", "certo <em>shopping</em>")])
X(168, "Potenciação", "<p>Se a massa vira 8m, a área vira \\(k (8m)^{2/3} = 8^{2/3} \\cdot k m^{2/3}\\). Como \\(8^{2/3} = (\\sqrt[3]{8})^2 = 2^2 = 4\\), a área é multiplicada por <strong>4</strong>. Alternativa <strong>B</strong>.</p><p>A opção D (8) supõe que a área cresce na mesma proporção que a massa.</p>",
  tags=["expoente fracionário"],
  enun=p("Dentre outros objetos de pesquisa, a Alometria estuda a relação entre medidas de diferentes partes do corpo humano. Por exemplo, segundo a Alometria, a área <em>A</em> da superfície corporal de uma pessoa relaciona-se com a sua massa <em>m</em> pela fórmula \\(A = k \\cdot m^{\\frac{2}{3}}\\), em que <em>k</em> é uma constante positiva.",
         "Se no período que vai da infância até a maioridade de um indivíduo sua massa é multiplicada por 8, por quanto será multiplicada a área da superfície corporal?"),
  alts=FR("\\sqrt[3]{16}", "4", "\\sqrt{24}", "8", "64"))
_c = lambda v: "\\def\\arraystretch{1.6}\\begin{bmatrix}" + "\\\\".join([v] * 4) + "\\end{bmatrix}"
_l4 = lambda v: "\\begin{bmatrix}" + "&".join([v] * 4) + "\\end{bmatrix}"
X(169, "Matrizes", "<p>A tabela é uma matriz 4 × 4 (disciplinas nas linhas, bimestres nas colunas). A média de cada linha é a soma das quatro notas dividida por 4, que é o produto da linha por uma matriz coluna 4 × 1 com todos os elementos iguais a \\(\\frac{1}{4}\\). Alternativa <strong>E</strong>.</p><p>Matrizes linha (A e B) não podem multiplicar uma 4 × 4 pela direita, e a coluna de 1/2 (D) daria o dobro da média.</p>",
  tags=["produto de matrizes", "média"],
  enun=p(T(169, 0)) + tabela(["", "1º bimestre", "2º bimestre", "3º bimestre", "4º bimestre"], [["Matemática", "5,9", "6,2", "4,5", "5,5"], ["Português", "6,6", "7,1", "6,5", "8,4"], ["Geografia", "8,6", "6,8", "7,8", "9,0"], ["História", "6,2", "5,6", "5,9", "7,7"]]) + p(T(169, 3)),
  alts=FR(_l4("\\frac{1}{2}"), _l4("\\frac{1}{4}"), _c("1"), _c("\\frac{1}{2}"), _c("\\frac{1}{4}")))
X(170, "Funções", "<p>P = R · i², e E é proporcional a P, então E = c · i², com c constante positiva. É uma função quadrática que passa pela origem e cresce cada vez mais rápido: um ramo de <strong>parábola com concavidade para cima</strong>, como no gráfico D. Alternativa <strong>D</strong>.</p><p>O gráfico A (reta) valeria se E fosse proporcional a i, e não a i².</p>",
  figs(("q170a", "Alternativa A: reta saindo da origem e subindo."),
       ("q170b", "Alternativa B: curva começando alta no eixo E e descendo cada vez mais devagar até tocar o eixo i."),
       ("q170c", "Alternativa C: segmento horizontal, E constante."),
       ("q170d", "Alternativa D: curva saindo da origem e subindo cada vez mais rápido, como meia parábola."),
       ("q170e", "Alternativa E: reta descendo do eixo E até o eixo i.")),
  ["função quadrática", "proporcionalidade"], enun=p(T(170, 0), T(170, 1)), alts=ALT(1))
X(171, "Grandezas e medidas", "<p>A longitude é 124° 3′ 0″. Como 1° = 60′, 3′ = 3 ÷ 60 = 0,05°. Na forma decimal: <strong>124,05°</strong>. Alternativa <strong>B</strong>.</p><p>A opção D (124,30°) confunde 3′ com 0,3°, como se o sistema fosse decimal.</p>",
  tags=["conversão de ângulos"], enun=p(T(171, 0), T(171, 1)) + fonte(T(171, 2).replace("Galileu", "<em>Galileu</em>")) + p(T(171, 3)))
X(172, "Notação científica", "<p>A figura indica “Proximidade da Terra: 325 mil km”, ou seja, 325 000 km = 3,25 × 10<sup>5</sup> km. Alternativa <strong>D</strong>.</p><p>Para escrever em notação científica, desloca-se a vírgula cinco casas: 325 000 = 3,25 × 100 000. O tamanho do asteroide (400 m) não entra na conta.</p>",
  figs(("q172", "Ilustração da NASA: a Terra, a Lua e a trajetória do asteroide YU 55. Textos: “O asteroide se aproximará o suficiente para que cientistas possam observar detalhes de sua superfície”; “Proximidade da Terra: 325 mil km”; “Asteroide YU 55. Tamanho: 400 m de diâmetro, equivalente ao tamanho de um porta-aviões”; “Passagem: 8 de novembro às 21h28min (horário de Brasília)”.")),
  ["notação científica"], enun=p(T(172, 0)) + "[[fig:1]]" + fonte(T(172, 2)) + p(T(172, 3)),
  alts={k: f"3,25 × 10<sup>{e}</sup> km." for k, e in zip("ABCDE", "23456")})
X(173, "Razão e proporção", "<p>A bacia comum gasta 15 L por descarga; 60 L por dia são 60 ÷ 15 = 4 descargas. A ecológica gastaria 4 × 6 = 24 L. A economia é 60 − 24 = <strong>36 litros</strong>. Alternativa <strong>B</strong>.</p><p>A opção A (24) é o consumo da bacia ecológica, e não a economia.</p>",
  tags=["proporcionalidade", "economia de água"])
X(174, "Estatística", "<p>Médias de 2009 a 2011, em milhares de reais: Alfinetes V, 660 ÷ 3 = 220; Balas W, 630 ÷ 3 = 210; Chocolates X, 675 ÷ 3 = 225; Pizzaria Y, 230; Tecelagem Z, 615 ÷ 3 = 205. As duas maiores são <strong>Pizzaria Y e Chocolates X</strong>. Alternativa <strong>D</strong>.</p>",
  tags=["média aritmética", "tabela"],
  enun=p(T(174, 0)) + tabela(["ME", "2009 (em milhares de reais)", "2010 (em milhares de reais)", "2011 (em milhares de reais)"],
    [["Alfinetes V", "200", "220", "240"], ["Balas W", "200", "230", "200"], ["Chocolates X", "250", "210", "215"], ["Pizzaria Y", "230", "230", "230"], ["Tecelagem Z", "160", "210", "245"]]) + p(T(174, 3), T(174, 4)))
X(175, "Porcentagem", "<p>A taxa era 300 mg/dL. Após reduzir 30%: 300 × 0,7 = 210. Após reduzir mais 10%: 210 × 0,9 = 189 mg/dL. Como 189 está entre 125 e 250, o paciente ficou na categoria de <strong>diabetes melito</strong>. Alternativa <strong>D</strong>.</p><p>Somar as reduções (40%) daria 180, que também é diabetes, mas o certo é aplicá-las em sequência.</p>",
  tags=["descontos sucessivos"],
  enun=p(T(175, 0)) + tabela(["Classificação", "Taxa de glicose"], [["Hipoglicemia", "menor ou igual a 70 mg/dL"], ["Normal", "maior que 70 mg/dL e menor ou igual a 100 mg/dL"], ["Pré-diabetes", "maior que 100 mg/dL e menor ou igual a 125 mg/dL"],
    ["Diabetes Melito", "maior que 125 mg/dL e menor ou igual a 250 mg/dL"], ["Hiperglicemia", "maior que 250 mg/dL"]]) + p(T(175, 2), T(175, 3)))
X(176, "Estatística", "<p>Cada talhão tem 30 000 m² = 3 hectares. O desvio padrão de 90 kg/talhão equivale a 90 ÷ 60 = 1,5 saca por talhão, ou 1,5 ÷ 3 = 0,5 saca por hectare. A variância é o quadrado do desvio padrão: 0,5² = <strong>0,25</strong> (sacas/hectare)². Alternativa <strong>E</strong>.</p><p>A opção D (0,50) é o desvio padrão, e não a variância.</p>",
  tags=["variância", "desvio padrão"], enun=SUP(p(T(176, 0), T(176, 1).replace("(sacas/hectare)2", "(sacas/hectare)<sup>2</sup>"))))
X(177, "Análise combinatória", "<p>Há 3 cores primárias e 3 secundárias (combinações de duas primárias): 6 cores. Cada uma pode aparecer sozinha, com o símbolo do branco (clara) ou com o do preto (escura): 6 × 3 = 18. Somando o preto e o branco: 18 + 2 = <strong>20 cores</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["contagem"], trocas=[("designer", "<em>designer</em>")], enun=p(T(177, 0)) + fonte(T(177, 1).replace("Folha de São Paulo", "<em>Folha de São Paulo</em>")) + p(T(177, 2)))
X(178, "Probabilidade", "<p>Com dois dados há 36 resultados. Soma 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1), ou seja, 6 casos. Soma 8: (2,6), (3,5), (4,4), (5,3), (6,2), 5 casos. Soma 4: (1,3), (2,2), (3,1), 3 casos. Quem tem mais chance é <strong>José</strong>. Alternativa <strong>D</strong>.</p><p>A opção C conta só os pares sem ordem, mas (1,6) e (6,1) são resultados diferentes.</p>",
  tags=["dois dados", "espaço amostral"])
X(179, "Estatística", "<p>Os dez valores em ordem: 181 419; 181 796; 204 804; 209 425; 212 952; 246 875; 266 415; 298 041; 299 415; 305 068. A mediana é a média do 5º e do 6º: (212 952 + 246 875) ÷ 2 = 229 913,5. A parte inteira é <strong>229 913</strong>. Alternativa <strong>B</strong>.</p>",
  figs(("q179", "Gráfico de linha “Brasil: comportamento do emprego formal no período de janeiro a outubro de 2010 (Caged)”, com os valores: jan 181.419; fev 209.425; mar 266.415; abr 305.068; maio 298.041; jun 212.952; jul 181.796; ago 299.415; set 246.875; out 204.804.")),
  ["mediana", "leitura de gráfico"], enun=p(T(179, 0)) + "[[fig:1]]" + fonte(T(179, 3)) + p(T(179, 4)))
X(180, "Geometria espacial", "<p>Cada aresta encolhe 20% e vira 0,8a. O volume passa de a³ para (0,8a)³ = 0,512a³, ou seja, 51,2% do original. A redução é de 100% − 51,2% = <strong>48,8%</strong>, porque o volume diminui de a³ para (0,8a)³. Alternativa <strong>C</strong>.</p><p>A opção D confunde o volume final (51,2%) com a redução.</p>",
  tags=["volume do cubo", "porcentagem"], enun=p(T(180, 0)) + fonte(T(180, 1)) + p(T(180, 2)),
  alts={"A": "20% menor que V, uma vez que o volume do cubo é diretamente proporcional ao comprimento de seu lado.", "B": "36% menor que V, porque a área da base diminui de <em>a</em><sup>2</sup> para ((1 − 0,2)<em>a</em>)<sup>2</sup>.",
        "C": "48,8% menor que V, porque o volume diminui de <em>a</em><sup>3</sup> para (0,8<em>a</em>)<sup>3</sup>.", "D": "51,2% menor que V, porque cada lado diminui para 80% do comprimento original.", "E": "60% menor que V, porque cada lado diminui 20%."})

completar(Q, R)
