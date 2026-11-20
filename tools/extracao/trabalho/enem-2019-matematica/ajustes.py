# Enem 2019, 2º dia, caderno azul: Matemática (questões 136 a 180; no site, 1 a 45).
# Texto legível (sem DECOD). Frações, potências e matriz em KaTeX; quadros em tabela HTML.
# Alternativas-imagem nas Q136 e Q139. Q179 (gráfico + planta) como imagem.
# Sem anuladas nesta área.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, paragrafos_enem

ID = "enem-2019-matematica"
META = {"id": ID, "banca": "Enem", "ano": 2019, "titulo": "Enem 2019: Matemática", "fonte": "Inep", "dataExame": "2019-11-10",
        "duracaoMinutos": 150, "area": "Matemática", "caderno": "azul", "dia": 2}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2019-dia2-azul")
Q = {}
P = lambda n: paragrafos_enem(D[n])
T = lambda n, i: P(n)[i][1]
p = lambda *xs: "".join(f"<p>{x}</p>" for x in xs)
fonte = lambda x: f'<p class="fonte">{x}</p>'
ALT = lambda ini: {k: f"[[fig:{i}]]" for i, k in enumerate("ABCDE", ini)}
FR = lambda *xs: {k: f"\\({v}\\)" for k, v in zip("ABCDE", xs)}
LISTA = lambda s: "<ul>" + "".join(f"<li>{x.strip()}</li>" for x in s.split("•") if x.strip()) + "</ul>"
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


X(136, "Geometria espacial", "<p>As letras são placas verticais, com o plano de cada uma perpendicular ao solo e de frente para quem olha a logomarca. Com o sol a pino, a sombra de uma placa vertical é só a sua base: um retângulo fino, com a largura da letra e a espessura da placa. Como as letras estão alinhadas lado a lado com o mesmo espaçamento, as sombras formam <strong>quatro retângulos alinhados, com os comprimentos das bases de P, I, N e E</strong>. Alternativa <strong>E</strong>.</p><p>A (uma faixa contínua) ignora os espaços entre as letras; B, C e D têm faixas de tamanhos que não correspondem às bases das letras.</p>",
  figs(("q136", "Logomarca com as letras PINE em preto."), ("q136f", "As letras PINE em três dimensões, suspensas na vertical sobre um piso cinza."),
       ("q136a", "Sombra: uma única faixa preta contínua sobre o piso."), ("q136b", "Sombra: quatro faixas pretas finas, alinhadas e quase do mesmo tamanho."),
       ("q136c", "Sombra: uma faixa curta isolada e, depois, três faixas mais longas alinhadas."), ("q136d", "Sombra: uma faixa curta e três faixas de tamanhos variados, separadas por espaços."),
       ("q136e", "Sombra: quatro faixas pretas alinhadas, de tamanhos diferentes, com pequenos espaços entre elas, formando uma linha quase contínua.")),
  ["projeção ortogonal"], enun=p(T(136, 0)) + "[[fig:1]]" + p(T(136, 2)) + "[[fig:2]]" + p(T(136, 4)), alts=ALT(3))
X(137, "Logaritmos", "<p>A flor é rosa com pH &gt; 7 e a mais valorizada tem pH &lt; 8: 7 &lt; −log x &lt; 8. Multiplicando por −1: −8 &lt; log x &lt; −7, ou seja, <strong>10<sup>−8</sup> &lt; x &lt; 10<sup>−7</sup></strong>. Alternativa <strong>E</strong>.</p><p>C e D confundem o pH com a concentração; A e B pegam só um dos limites.</p>",
  tags=["função logarítmica", "pH"],
  enun=p(T(137, 0).replace("A Hydrangea macrophylla", "A <em>Hydrangea macrophylla</em>").replace("a Hydrangea cor-de-rosa", "a <em>Hydrangea</em> cor-de-rosa").replace("pH < 7", "pH &lt; 7").replace("pH > 7", "pH &gt; 7").replace("pH = - log10x, em que x", "\\(pH = -\\log_{10} x\\), em que <em>x</em>").replace("(H+)", "(H<sup>+</sup>)"),
         T(137, 1).replace("a Hydrangea", "a <em>Hydrangea</em>").replace(" x assuma", " <em>x</em> assuma")),
  alts=FR("x > 10^{-8}", "0 < x < 10^{-7}", "7 < x < 8", "70 < x < 80", "10^{-8} < x < 10^{-7}"))
X(138, "Porcentagem", "<p>O transporte custa 1/5 do valor, ou 20%. O total das despesas (transporte + recompensa) não pode passar de 100% do valor do objeto: 20% + r ≤ 100%, então a recompensa máxima é <strong>80%</strong>. Alternativa <strong>E</strong>.</p><p>20% (A) é só o transporte; 5% é o mínimo legal, não o máximo.</p>",
  tags=["porcentagem"])
X(139, "Funções", "<p>Até 6 m<sup>3</sup> paga-se R$ 12 fixos (trecho horizontal). De 6 a 10 m<sup>3</sup>, mais R$ 3 por m<sup>3</sup>: chega a 12 + 12 = R$ 24 (reta inclinada). De 10 a 15 m<sup>3</sup>, mais R$ 6 por m<sup>3</sup>: chega a 24 + 30 = R$ 54 (reta com o dobro da inclinação). O gráfico é horizontal, depois sobe e depois sobe mais rápido: o da alternativa <strong>A</strong>. Alternativa <strong>A</strong>.</p><p>B fica menos inclinado no fim; C fica constante; D tem uma inclinação só; E não começa com valor fixo.</p>",
  figs(("q139a", "Gráfico A: horizontal até 6, depois sobe com uma inclinação até 10 e, de 10 a 15, sobe com inclinação maior."),
       ("q139b", "Gráfico B: horizontal até 6, sobe até 10 e depois sobe com inclinação menor até 15."),
       ("q139c", "Gráfico C: horizontal até 6, sobe até 10 e depois fica horizontal até 15."),
       ("q139d", "Gráfico D: horizontal até 6 e depois uma única reta inclinada até 15."),
       ("q139e", "Gráfico E: começa inclinado desde zero, com inclinação crescente em três trechos.")),
  ["função definida por partes"],
  enun=p(T(139, 0)) + LISTA(T(139, 1).split(" Sabe-se")[0].replace("m3", "m<sup>3</sup>")) + p("Sabe-se" + T(139, 1).split(" Sabe-se")[1].replace("m3", "m<sup>3</sup>"), T(139, 2).replace("valor P,", "valor <em>P</em>,").replace("volume V de", "volume <em>V</em> de")),
  alts=ALT(1))
X(140, "Notação científica", "<p>0,00011 mm: andando a vírgula quatro casas para a direita, fica 1,1. Então 0,00011 = <strong>1,1 × 10<sup>−4</sup></strong>. Alternativa <strong>D</strong>.</p><p>1,1 × 10<sup>−3</sup> (C) e 1,1 × 10<sup>−5</sup> (E) erram a contagem de casas.</p>",
  tags=["potências de 10"], enun=p(T(140, 0).replace("vírus influenza", "vírus <em>influenza</em>"), T(140, 1).replace("vírus influenza", "vírus <em>influenza</em>")) + fonte(T(140, 2)) + p(T(140, 3).replace("vírus influenza", "vírus <em>influenza</em>")),
  alts=FR(*[f"1{{,}}1 \\times 10^{{-{i}}}" for i in range(1, 6)]))
X(141, "Razão e proporção", "<p>Defesa = k<sub>d</sub> · N · E<sup>2</sup> e ataque = k<sub>a</sub> · E · N<sup>2</sup>. No início (N = 1, E = 1), defesa 1 e ataque 2: k<sub>d</sub> = 1 e k<sub>a</sub> = 2. Ataque de J<sub>1</sub> (N = 4, E = 5): 2 · 5 · 16 = 160. Defesa de J<sub>2</sub> (N = 2, E = 6): 1 · 2 · 36 = 72. Diferença: <strong>88</strong>. Alternativa <strong>B</strong>.</p><p>Esquecer a constante 2 do ataque daria 80 − 72 = 8, que não está entre as opções; 112 (A) somaria em vez de subtrair as forças de outro modo.</p>",
  tags=["grandezas diretamente proporcionais"],
  enun=p(T(141, 0), T(141, 1).replace("J1", "J<sub>1</sub>").replace("J2", "J<sub>2</sub>"), T(141, 2).replace("J1", "J<sub>1</sub>")))
X(142, "Geometria plana", "<p>O novo diâmetro é 6 + 8 = 14 m (raio 7). A área nova a pavimentar é a coroa circular: 3 · 7<sup>2</sup> − 3 · 3<sup>2</sup> = 147 − 27 = 120 m<sup>2</sup>. Como só há material para 100 m<sup>2</sup>, <strong>não será suficiente, pois a área mede 120 m<sup>2</sup></strong>. Alternativa <strong>E</strong>.</p><p>108 m<sup>2</sup> (D) somaria 8 ao raio, não ao diâmetro, de outro jeito; 48 m<sup>2</sup> (C) usa os diâmetros como raios de forma errada.</p>",
  tags=["área do círculo", "coroa circular"], enun=p(T(142, 0).replace("100 m2", "100 m<sup>2</sup>"), T(142, 1).replace("para π", "para π"), T(142, 2)),
  alts={k: v.replace(" m2", " m<sup>2</sup>") for k, v in D[142]["alternativas"].items()})
X(143, "Razão e proporção", "<p>Consumo por minuto = kcal ÷ tempo. I: 20/10 = 2; II: 100/15 ≈ 6,7; III: 120/20 = 6; IV: 100/25 = 4; V: 80/30 ≈ 2,7. O maior é o da atividade <strong>II</strong>. Alternativa <strong>B</strong>.</p><p>A III (C) gasta mais calorias no total, mas leva mais tempo.</p>",
  figs(("q143", "Gráfico de pontos do gasto calórico (kcal) em função do tempo (min): I, 20 kcal em 10 min; II, 100 kcal em 15 min; III, 120 kcal em 20 min; IV, 100 kcal em 25 min; V, 80 kcal em 30 min.")),
  ["taxa", "leitura de gráfico"], enun=p(T(143, 0)) + "[[fig:1]]" + p(T(143, 4)))
X(144, "Matrizes", "<p>Cada coluna é um dia; o total de acertos do dia é a soma da coluna. Segunda: 3 + 3 + 2 + 3 + 0 = <strong>11</strong>; terça: 2 + 2 + 2 + 2 + 2 = 10; quarta: 0 + 4 + 2 + 4 + 0 = 10; quinta: 1 + 1 + 3 + 1 + 4 = 10; sexta: 2 + 2 + 2 + 0 + 4 = 10. O maior total foi na <strong>segunda-feira</strong>. Alternativa <strong>A</strong>.</p><p>Somar as linhas daria o desempenho dos alunos, não dos dias.</p>",
  tags=["matriz", "soma de colunas"],
  enun=p(T(144, 0)) + '<p class="centro">\\(\\begin{bmatrix} 3 & 2 & 0 & 1 & 2 \\\\ 3 & 2 & 4 & 1 & 2 \\\\ 2 & 2 & 2 & 3 & 2 \\\\ 3 & 2 & 4 & 1 & 0 \\\\ 0 & 2 & 0 & 4 & 4 \\end{bmatrix}\\)</p>' + p(T(144, 1), T(144, 2)))
X(145, "Razão e proporção", "<p>A cada volta dos pedais a corrente percorre o mesmo comprimento; a catraca dá mais voltas quanto menor ela for. O avanço da bicicleta é inversamente proporcional ao diâmetro da catraca. Para avançar 1,5 vez mais, o diâmetro deve ser 7 ÷ 1,5 ≈ <strong>4,7 cm</strong>. Alternativa <strong>C</strong>.</p><p>10,5 (E) multiplicaria em vez de dividir; 3,5 (B) seria metade do diâmetro.</p>",
  figs(("q145", "Disco dentado de uma catraca, com o diâmetro indicado de ponta a ponta dos dentes.")),
  ["grandezas inversamente proporcionais"], enun=p(T(145, 0)) + "[[fig:1]]" + p(T(145, 3), T(145, 4)))
X(146, "Estatística", "<p>Dia 1: temperatura perto de 6 °C (&lt; 10) e umidade perto de 35% (&lt; 40): alerta cinza correto. Dia 12: umidade de 20%, mas temperatura de exatamente 40 °C; o laranja exige temperatura <em>entre</em> 35 e 40 °C, e o gabarito oficial só fecha se o 40 não estiver incluído. Dia 13: temperatura acima de 40 °C, mas umidade de 40%, acima dos 25% exigidos: alerta vermelho errado. Só o dia <strong>1</strong> está correto. Alternativa <strong>A</strong>.</p><p>Considerar o 40 °C incluído no intervalo levaria a “1 e 12” (C); a questão adota o intervalo aberto.</p>",
  figs(("q146", "Gráfico de temperatura (linha cheia, °C) e umidade relativa do ar (linha pontilhada, %) nos dias 1 a 15: no dia 1, cerca de 6 °C e 35%; no dia 12, 40 °C e 20%; no dia 13, cerca de 41 °C e 40%.")),
  ["leitura de gráfico", "intervalos"],
  enun=p(T(146, 0)) + LISTA(T(146, 1).split(" Um resumo")[0]) + p("Um resumo" + T(146, 1).split(" Um resumo")[1]) + "[[fig:1]]" + p(T(146, 4)) + LISTA(T(146, 5).split(" Em qual")[0]) + p("Em qual" + T(146, 5).split(" Em qual")[1]))
X(147, "Geometria plana", "<p>Cada placa é formada por um semicírculo de diâmetro 40 cm no alto e um retângulo de 40 cm de largura e 60 − 20 = 40 cm de altura embaixo. Área: 3,14 · 20<sup>2</sup>/2 + 40 · 40 = 628 + 1 600 = 2 228 cm<sup>2</sup>. Dez placas: <strong>22 280 cm<sup>2</sup></strong>. Alternativa <strong>B</strong>.</p><p>Somar o círculo inteiro ao retângulo de 40 × 60 daria 3 656 por placa; usar o retângulo inteiro de 40 × 60 daria 24 000 por placa.</p>",
  figs(("q147", "Placa “Proibido estacionar”: um círculo de diâmetro d no alto, tangente aos lados de um retângulo; a placa tem comprimento total h.")),
  ["área do círculo", "área do retângulo"], enun=p(T(147, 0), T(147, 1).replace("d = 40 cm", "<em>d</em> = 40 cm").replace("h = 60 cm", "<em>h</em> = 60 cm")) + "[[fig:1]]" + p(T(147, 5)))
X(148, "Grandezas e medidas", "<p>A banheira tem 0,3 m<sup>3</sup> = 300 L, e será preenchida em 80%: 240 L. Cada embalagem rende 2,7 L: 240 ÷ 2,7 ≈ 88,9. São necessárias <strong>89 embalagens</strong>. Alternativa <strong>C</strong>.</p><p>112 (D) usaria a capacidade total, sem os 80%.</p>",
  tags=["volume", "arredondamento"], enun=p(T(148, 0).replace("0,3 m3", "0,3 m<sup>3</sup>"), T(148, 1)))
X(149, "Progressões", "<p>De 2014 para 2015, os acidentes caíram 900 − 850 = 50. Mantida essa redução por ano: 2016, 800; 2017, 750; 2018, <strong>700</strong>. Alternativa <strong>D</strong>.</p><p>Usar a queda de 2013 para 2014 (150 por ano) daria 400, que não está entre as opções.</p>",
  tags=["progressão aritmética"],
  enun=p(T(149, 0).replace("O slogan", "O <em>slogan</em>")) + tabela(["Ano", "2013", "2014", "2015"], [["Número total de acidentes", "1 050", "900", "850"]]) + p(T(149, 2), T(149, 3)))
X(150, "Matemática financeira", "<p>O valor à vista é a soma dos pagamentos trazidos para a data da compra: 202,00/1,01 + 204,02/1,01<sup>2</sup> = 200 + 204,02/1,0201 = 200 + 200 = <strong>R$ 400,00</strong>. Alternativa <strong>B</strong>.</p><p>406,02 (E) é a soma das parcelas, sem descontar os juros.</p>",
  tags=["juros compostos", "valor presente"])
X(151, "Razão e proporção", "<p>Cada sócio inicial investiu 1 000 000/3 + 800 000/4 ≈ 333 333 + 200 000 = 533 333. O quarto investiu 200 000. Sobre o total de 1 800 000: 533 333/1 800 000 ≈ <strong>29,60%</strong> e 200 000/1 800 000 ≈ <strong>11,11%</strong>. Alternativa <strong>A</strong>.</p><p>25% para todos (C) ignoraria que os três primeiros investiram mais.</p>",
  tags=["divisão proporcional"])
X(152, "Razão e proporção", "<p>Inversamente proporcional às idades 2, 3 e 5: os valores são k/2, k/3 e k/5. A soma é k · (15 + 10 + 6)/30 = 31k/30 = 31 000, logo k = 30 000. A máquina de 5 anos recebe 30 000/5 = <strong>R$ 6 000,00</strong>. Alternativa <strong>B</strong>.</p><p>R$ 15 500 (E) seria a fatia diretamente proporcional à idade de 5 anos.</p>",
  tags=["grandezas inversamente proporcionais"], enun=p(T(152, 0)) + LISTA(T(152, 1).replace("<br>", " ")) + p(T(152, 2), T(152, 3)))
X(153, "Porcentagem", "<p>Em 2010: 1 250 · 1,072 = 1 340. Em 2020: 1 340 · 1,10 = <strong>R$ 1 474,00</strong>. Alternativa <strong>E</strong>.</p><p>Somar 7,2% + 10% sobre 1 250 daria 1 465 (D), mas os aumentos são sucessivos.</p>",
  tags=["aumentos sucessivos"])
X(154, "Logaritmos", "<p>M<sub>s</sub> = 3,30 + log(2 000 · 0,2) = 3,30 + log 400 = 3,30 + log 4 + 2 = 3,30 + 0,6 + 2 = <strong>5,9</strong>. Pelo quadro, 5,0 ≤ 5,9 ≤ 5,9: terremoto <strong>moderado</strong>. Alternativa <strong>C</strong>.</p><p>Esquecer o 0,2 da frequência daria 3,30 + log 2 000 = 6,6 (grande, D).</p>",
  tags=["função logarítmica", "escala Richter"],
  enun=p(T(154, 0).replace("(Ms)", "(M<sub>s</sub>)")) + tabela(["Descrição", "Magnitude local (M<sub>s</sub>) (µm · Hz)"],
       [["Pequeno", "0 ≤ M<sub>s</sub> ≤ 3,9"], ["Ligeiro", "4,0 ≤ M<sub>s</sub> ≤ 4,9"], ["Moderado", "5,0 ≤ M<sub>s</sub> ≤ 5,9"], ["Grande", "6,0 ≤ M<sub>s</sub> ≤ 9,9"], ["Extremo", "M<sub>s</sub> ≥ 10,0"]])
       + p("Para se calcular a magnitude local, usa-se a fórmula \\(M_s = 3{,}30 + \\log(A \\cdot f)\\), em que <em>A</em> representa a amplitude máxima da onda registrada por um sismógrafo em micrômetro (µm) e <em>f</em> representa a frequência da onda, em hertz (Hz). Ocorreu um terremoto com amplitude máxima de 2 000 µm e frequência de 0,2 Hz.")
       + fonte(T(154, 3)) + p(T(154, 4), T(154, 5)))
X(155, "Sequências", "<p>O bloco que se repete é 5, 4, 3, 2, 1, 2, 3, 4 (8 termos). 2 015 = 8 · 251 + 7: o 2 015º item é o 7º termo do bloco, o número 3, que corresponde à <strong>caixa de direção</strong>. Alternativa <strong>E</strong>.</p><p>Usar um bloco de 9 termos (até o 5 seguinte) mudaria a posição e daria outra peça.</p>",
  tags=["sequência periódica", "resto da divisão"],
  enun=p(T(155, 0), T(155, 1)) + fonte(T(155, 2)) + p(T(155, 3), T(155, 4), T(155, 5)))
X(156, "Análise combinatória", "<p>Total de formas de dividir 8 pessoas em 4 duplas: 7 · 5 · 3 · 1 = 105. Formas em que os dois canhotos ficam juntos: eles formam uma dupla e os outros 6 se dividem em 3 duplas, 5 · 3 · 1 = 15. Sem canhotos juntos: 105 − 15 = <strong>90</strong>. Alternativa <strong>C</strong>.</p><p>105 (E) é o total, sem a restrição.</p>",
  tags=["formação de grupos", "princípio da contagem"])
X(157, "Geometria espacial", "<p>Cortando os quatro cantos do tetraedro, cada face triangular perde suas três pontas e vira um hexágono; como se remove um terço de cada aresta, os seis lados ficam iguais e o hexágono é regular. Cada corte cria um triângulo equilátero novo. São <strong>4 hexágonos regulares e 4 triângulos equiláteros</strong>. Alternativa <strong>A</strong>.</p><p>O tetraedro tem 4 faces e 4 vértices, por isso 4 de cada; B e E erram a contagem.</p>",
  figs(("q157", "Um tetraedro regular de aresta a com um plano cortando um de seus vértices a um terço da aresta (a/3) e, ao lado, o sólido depois do corte, com a ponta removida.")),
  ["tetraedro truncado", "poliedros"], enun=p(T(157, 0)) + "[[fig:1]]" + p(T(157, 4)))
X(158, "Escala", "<p>Na escala 1 : 200, os volumes ficam em 1 : 200<sup>3</sup> = 1 : 8 000 000. O reservatório real tem 45 · 8 000 000 = 360 000 000 cm<sup>3</sup> = 360 000 L. Com consumo de 30 000 L por dia: 360 000/30 000 = <strong>12 dias</strong>. Alternativa <strong>C</strong>.</p><p>Usar a escala linear no volume daria 9 000 cm<sup>3</sup> e menos de um dia.</p>",
  tags=["escala", "volume"], enun=p(T(158, 0), T(158, 1).replace("45 cm3", "45 cm<sup>3</sup>"), T(158, 2), T(158, 3)))
X(159, "Probabilidade", "<p>Com n placas, a chance de não ver nenhuma é (1/2)<sup>n</sup>. Queremos 1 − (1/2)<sup>n</sup> &gt; 99/100, ou 2<sup>n</sup> &gt; 100: n ≥ 7 (2<sup>7</sup> = 128). Como já existe uma placa, é preciso instalar <strong>6 novas</strong>. Alternativa <strong>D</strong>.</p><p>7 seria o total de placas, não o número de novas.</p>",
  tags=["evento complementar"],
  enun=p(T(159, 0)[:-2] + " \\(\\frac{1}{2}\\). Com isso, após autorização do órgão competente, decidiu instalar novas placas com anúncios de seu restaurante ao longo dessa rodovia, de maneira que a probabilidade de um motorista perceber pelo menos uma das placas instaladas fosse superior a \\(\\frac{99}{100}\\).", T(159, 3)))
X(160, "Estatística", "<p>A soma das alturas era 20 · 1,80 = 36 m. Trocar um jogador por outro 0,20 m mais baixo reduz a soma para 35,80 m. Nova média: 35,80/20 = <strong>1,79 m</strong>. Alternativa <strong>C</strong>.</p><p>Subtrair 0,20 da média (A) esquece que a redução se divide pelos 20 jogadores.</p>",
  tags=["média aritmética"])
X(161, "Estatística", "<p>Média ponderada: (0 · 52 + 1 · 5 + 2 · 2 + 3 · 1) ÷ 60 = (0 + 5 + 4 + 3)/60 = 12/60 = <strong>0,2</strong>. Alternativa <strong>B</strong>.</p><p>1,5 (C) é a média simples dos valores 0, 1, 2 e 3, sem as frequências.</p>",
  tags=["média ponderada"],
  enun=p(T(161, 0), T(161, 1)) + tabela(["Quantidade de garrafas fora das especificações por dia", "Quantidade de dias"], [["0", "52"], ["1", "5"], ["2", "2"], ["3", "1"]]) + p(T(161, 3)))
X(162, "Grandezas e medidas", "<p>1 jarda = 3 pés = 0,9144 m, então 1 pé = 0,3048 m = 30,48 cm. Como 1 polegada = 2,54 cm, 1 pé = 30,48/2,54 = <strong>12 polegadas</strong>. Alternativa <strong>D</strong>.</p><p>0,3048 (B) é o pé em metro, não em polegada.</p>",
  tags=["conversão de unidades"],
  enun=p(T(162, 0)) + tabela(["Unidade", "Equivalência"], [["Polegada", "2,54 centímetros"], ["Jarda", "3 pés"], ["Jarda", "0,9144 metro"]]) + p(T(162, 2)))
X(163, "Funções", "<p>Para 0 &lt; X &lt; 1, as potências com expoente maior que 1 ficam menores que X (X<sup>2</sup>, X<sup>3</sup>), e as com expoente entre 0 e 1 ficam maiores. Entre √X = X<sup>1/2</sup> e X<sup>1/3</sup>, o menor expoente dá o maior valor: X<sup>1/3</sup> &gt; X<sup>1/2</sup> &gt; X. O maior IDH é o do <strong>terceiro</strong> país. Alternativa <strong>C</strong>.</p><p>Para números maiores que 1 seria o contrário, e o quinto (X<sup>3</sup>) ganharia.</p>",
  tags=["potências de base entre 0 e 1"],
  enun=p(T(163, 0).rsplit(" o primeiro país recebeu um", 1)[0] + " o primeiro país recebeu um valor <em>X</em>, o segundo \\(\\sqrt{X}\\), o terceiro \\(X^{\\frac{1}{3}}\\), o quarto \\(X^2\\) e o último \\(X^3\\). Nenhum desses países zerou ou atingiu o índice máximo.", T(163, 2)))
X(164, "Geometria espacial", "<p>Dividindo a laje em retângulos: 8 m × 8 m (altura total 5 + 2 + 1 = 8), 3 m × 7 m e 3 m × 5 m. Área: 64 + 21 + 15 = 100 m<sup>2</sup>. Com 5 cm de espessura: 100 · 0,05 = 5 m<sup>3</sup>. Basta <strong>um caminhão de 5 m<sup>3</sup></strong>. Alternativa <strong>C</strong>.</p><p>Usar a espessura em centímetros sem converter daria 500 m<sup>3</sup>, o que leva a A ou B.</p>",
  figs(("q164", "Planta da laje em forma de escada: base de 14 m; à esquerda, um trecho de 8 m de largura com a altura máxima; depois degraus que descem 1 m e 2 m, com patamares de 3 m; à direita, a altura é de 5 m.")),
  ["área", "volume"], enun=p(T(164, 0).replace("m3", "m<sup>3</sup>")) + "[[fig:1]]" + p(T(164, 4).replace("14 m ", "")),
  alts={k: v.replace("m3", "m<sup>3</sup>") for k, v in D[164]["alternativas"].items()})
X(165, "Funções", "<p>O volume de sangue é 8% da massa: 0,08m litros. A concentração é q/(0,08m), e é prejudicial quando passa de 0,4 g/L: <strong>q/(0,08m) &gt; 0,4</strong>. Alternativa <strong>E</strong>.</p><p>Usar 0,8 em vez de 0,08 (A) confunde 8% com 80%; B, C e D invertem a razão ou os números.</p>",
  tags=["expressão algébrica", "porcentagem"],
  enun=p(T(165, 0).replace("quantidade q de", "quantidade <em>q</em> de").replace("corporal m desse", "corporal <em>m</em> desse"), T(165, 1)) + fonte(T(165, 2)) + p(T(165, 3).replace("relacionando q e m", "relacionando <em>q</em> e <em>m</em>")),
  alts=FR("\\frac{q}{0{,}8m} > 0{,}4", "\\frac{0{,}4m}{q} > 0{,}8", "\\frac{q}{0{,}4m} > 0{,}8", "\\frac{0{,}08m}{q} > 0{,}4", "\\frac{q}{0{,}08m} > 0{,}4"))
X(166, "Geometria plana", "<p>Na figura, E fica no lado de baixo da folha, a 12 cm de C. Como o lado mede 18 cm, E está a 18 − 12 = 6 cm do canto inferior esquerdo da folha, que fica 12 cm abaixo de A. A dobra leva esse canto até D, e AE é a hipotenusa do triângulo retângulo formado por A, esse canto e E, de catetos 12 cm e 6 cm: AE = √(6<sup>2</sup> + 12<sup>2</sup>) = √180 = <strong>6√5 cm</strong>. Alternativa <strong>D</strong>.</p><p>12√2 (E) seria a diagonal de um quadrado de 12 cm.</p>",
  figs(("q166", "Folha retangular ABCE de 18 cm por 12 cm, com o canto dobrado: o vértice A no alto à esquerda, B no alto à direita, C embaixo à direita, E embaixo, a 12 cm de C, e D o ponto onde o canto dobrado encosta, formando um ângulo reto.")),
  ["teorema de Pitágoras", "dobradura"], enun=p(T(166, 0).replace("do origami", "do <em>origami</em>").replace("(ori = dobrar; kami = papel)", "(<em>ori</em> = dobrar; <em>kami</em> = papel)").replace("técnica do origami", "técnica do <em>origami</em>")) + "[[fig:1]]" + p(T(166, 4)),
  alts=FR("2\\sqrt{22}\\text{ cm}", "6\\sqrt{3}\\text{ cm}", "12\\text{ cm}", "6\\sqrt{5}\\text{ cm}", "12\\sqrt{2}\\text{ cm}"))
X(167, "Estatística", "<p>O grupo de basquete tem um aluno a mais, então a turma tem número ímpar de alunos e a mediana (1,67 m) é a altura de um aluno: F. Ordenando, o aluno do meio e todos os mais altos formam o grupo maior, o de basquete. F (1,67) e M (1,68) jogam basquete; P (1,65) e J (1,66), mais baixos que a mediana, jogam futebol. Alternativa <strong>C</strong>.</p><p>A média e a moda não decidem a divisão: o que importa é a posição de cada um em relação à mediana.</p>",
  tags=["mediana"],
  enun=p(T(167, 0)) + tabela(["Média", "Mediana", "Moda"], [["1,65", "1,67", "1,70"]]) + p(T(167, 2), T(167, 3)))
X(168, "Funções", "<p>Dos X funcionários, um é o gerente (R$ 1 000) e X − 1 são diaristas, cada um recebendo 2 · 80 = R$ 160 por semana. Y = 1 000 + 160(X − 1) = <strong>160X + 840</strong>. Alternativa <strong>D</strong>.</p><p>160X + 1 000 (E) contaria o gerente também como diarista.</p>",
  tags=["função afim"], enun=p(T(168, 0), T(168, 1).replace("de X a", "de <em>X</em> a").replace("quantia Y,", "quantia <em>Y</em>,")))
X(169, "Geometria analítica", "<p>No bar, P alcança 3 km, e cada outro usuário alcança o seu próprio raio. Para haver <em>match</em>, a distância entre os dois precisa caber nos dois raios: até 3 km de Q (3, 7), até 2 km de R (6, 7) e até 3 km de S (5, 3), porque o raio de P é menor que os 5 km de S. O bar I (5, 6) fica a √5 ≈ 2,2 km de Q, a √2 ≈ 1,4 km de R e a exatamente 3 km de S: atende aos três. Os outros bares ficam a mais de 2 km de R. Alternativa <strong>A</strong>.</p><p>O bar IV (4,6), por exemplo, fica a √5 ≈ 2,2 km de R, mais que os 2 km do raio de R.</p>",
  figs(("q169", "Plano cartesiano em km com os usuários P (0,0), Q (3,7), R (6,7) e S (5,3) e os bares I (5,6), II (4,5), III (5,5), IV (4,6) e V (3,4).")),
  ["distância entre pontos"],
  enun=p(T(169, 0).replace("chamado de match", "chamado de <em>match</em>"), T(169, 1).replace("obter um match", "obter um <em>match</em>")) + "[[fig:1]]" + p(T(169, 4).replace("de um match", "de um <em>match</em>")))
X(170, "Razão e proporção", "<p>Dose diária máxima: 500 mg · 20 kg = 10 000 mg = 10 g. Em 5 dias: 50 g, que ocupam 50 cm<sup>3</sup> = 50 mL. Os pais devem comprar o frasco de <strong>50 mL</strong>. Alternativa <strong>B</strong>.</p><p>10 mL (A) daria só para um dia.</p>",
  tags=["dosagem", "conversão de unidades"], enun=p(T(170, 0).replace("1 cm3", "1 cm<sup>3</sup>"), T(170, 1)))
X(171, "Análise combinatória", "<p>Os vagões têm posições fixas (1 a 12); o que varia é a cor de cada um. Escolhem-se as 4 posições vermelhas entre 12, depois 3 azuis entre as 8 restantes, 3 verdes entre as 5 que sobram e as 2 últimas ficam amarelas: \\(C_{12}^{4} \\times C_{8}^{3} \\times C_{5}^{3} \\times C_{2}^{2}\\). Alternativa <strong>E</strong>.</p><p>A escolhe sempre entre os 12 vagões, contando posições já ocupadas; B soma em vez de multiplicar.</p>",
  figs(("q171", "Brinquedo: uma locomotiva preta seguida de 12 vagões numerados de 1 a 12, em ordem.")),
  ["combinação"], enun=p(T(171, 0)) + "[[fig:1]]" + p(T(171, 2)),
  alts=FR("C_{12}^{4} \\times C_{12}^{3} \\times C_{12}^{3} \\times C_{12}^{2}", "C_{12}^{4} + C_{8}^{3} + C_{5}^{3} + C_{2}^{2}", "C_{12}^{4} \\times 2 \\times C_{8}^{3} \\times C_{5}^{2}",
          "C_{12}^{4} + 2 \\times C_{12}^{3} + C_{12}^{2}", "C_{12}^{4} \\times C_{8}^{3} \\times C_{5}^{3} \\times C_{2}^{2}"))
X(172, "Progressões", "<p>Média de julho a novembro: (700 + 2 500 + 2 500 + 2 800 + 2 700)/5 = 11 200/5 = 2 240 em dezembro. A redução de novembro para dezembro foi 2 700 − 2 240 = 460. Mantida: janeiro 1 780, fevereiro 1 320, março 860, <strong>abril</strong> 400, abaixo dos 700 de julho. Alternativa <strong>D</strong>.</p><p>Em março (C) as vendas ainda seriam 860, acima de 700.</p>",
  figs(("q172", "Gráfico de linha das unidades vendidas de julho a novembro de 2011: 700 em julho, 2 500 em agosto e setembro, 2 800 em outubro e 2 700 em novembro.")),
  ["progressão aritmética", "média"], enun=p(T(172, 0)) + "[[fig:1]]" + p(T(172, 4), T(172, 5), T(172, 6)))
X(173, "Probabilidade", "<p>Fraudulentas e inconsistentes: 20% · 25% = 5% do total. Fraudulentas e consistentes: 80% · 6,25% = 5%. Fraudulentas no total: 10%. A probabilidade condicional pedida é 5%/10% = <strong>0,5</strong>. Alternativa <strong>E</strong>.</p><p>0,05 (A) é a probabilidade da interseção, sem dividir pelo total de fraudulentas.</p>",
  tags=["probabilidade condicional"])
X(174, "Razão e proporção", "<p>Taxa = urbana/(urbana + rural). I: 8 000/12 000 ≈ 0,67; II: 10 000/18 000 ≈ 0,56; III: 11 000/16 000 ≈ 0,69; IV: 18 000/28 000 ≈ 0,64; V: 17 000/29 000 ≈ 0,59. A maior é a do município <strong>III</strong>. Alternativa <strong>C</strong>.</p><p>O IV (D) tem a maior população urbana, mas também muita população rural.</p>",
  figs(("q174", "Dois gráficos de barras por município: população urbana (I 8 000, II 10 000, III 11 000, IV 18 000, V 17 000) e população rural (I 4 000, II 8 000, III 5 000, IV 10 000, V 12 000).")),
  ["razão", "leitura de gráfico"], enun=p(T(174, 0)) + "[[fig:1]]" + p(T(174, 4)))
X(175, "Geometria espacial", "<p>O volume do central é π · 2<sup>2</sup> · 3,30 = 13,2π m<sup>3</sup>. Os canos ficam cheios e guardam 4 · π · 0,05<sup>2</sup> · 20 = 0,2π m<sup>3</sup>. Sobram 13π m<sup>3</sup> para os cinco reservatórios, que terminam com a mesma altura h: π(4 + 4 · 2,25)h = 13πh. Então h = <strong>1,00 m</strong>. Alternativa <strong>D</strong>.</p><p>Esquecer a água dos canos daria h ≈ 1,02 m, perto de 1,00, mas sem justificar a conta exata; 1,10 e 1,16 vêm de erros na área das bases.</p>",
  figs(("q175", "Reservatório central cilíndrico Rc ligado por canos a quatro reservatórios menores, R1, R2, R3 e R4.")),
  ["volume do cilindro", "vasos comunicantes"],
  enun=p(T(175, 0).replace("(Rc)", "(R<sub>c</sub>)").replace("(R1, R2, R3 e R4)", "(R<sub>1</sub>, R<sub>2</sub>, R<sub>3</sub> e R<sub>4</sub>)")) + "[[fig:1]]" + p(T(175, 2), T(175, 3), T(175, 4)))
X(176, "Porcentagem", "<p>Orçamento inicial: 10 000 + 40 000 + 40 · 2 500 = 150 000. O novo deve ser 90% disso: 135 000. Projeto: 5 000; construção: 40 · 3 125 = 125 000. Sobram 135 000 − 130 000 = 5 000 para os custos fixos, que eram 40 000: desconto de 35 000/40 000 = <strong>87,5%</strong>. Alternativa <strong>D</strong>.</p><p>Aplicar os percentuais só sobre um item leva a 25% ou 50% (B e C).</p>",
  tags=["porcentagem", "orçamento"],
  enun=p(T(176, 0).replace("40 m2", "40 m<sup>2</sup>")) + LISTA(T(176, 1).split(" Após a apresentação")[0]) + p("Após a apresentação" + T(176, 1).split(" Após a apresentação")[1], T(176, 2)))
X(177, "Trigonometria", "<p>h(t) = 4 + 4 sen(βt/2 − π/2) = 4 − 4 cos(βt/2). h = 6 quando cos(βt/2) = −1/2, isto é, βt/2 = 2π/3, 4π/3, 8π/3, … A terceira vez é em βt/2 = 8π/3, ou t = 16π/(3β) = 16/β (com π = 3). Para t &lt; 4: β &gt; 4, e o menor inteiro é <strong>5</strong>. Alternativa <strong>D</strong>.</p><p>Com β = 4 (C), a terceira vez seria exatamente em 4 s, e o enunciado pede menos de 4 s.</p>",
  figs(("q177", "Esquema de um motor: no instante t = 0, o pistão está na base da câmara de combustão, com h(0) = 0; num instante t ≠ 0, a biela gira e o pistão sobe a uma altura h(t).")),
  ["função seno", "equação trigonométrica"],
  enun=p(T(177, 0)) + "[[fig:1]]" + p("A função \\(h(t) = 4 + 4\\,\\text{sen}\\left(\\frac{\\beta t}{2} - \\frac{\\pi}{2}\\right)\\) definida para \\(t \\ge 0\\) descreve como varia a altura <em>h</em>, medida em centímetro, da parte superior do pistão dentro da câmara de combustão, em função do tempo <em>t</em>, medido em segundo. Nas figuras estão indicadas as alturas do pistão em dois instantes distintos.",
                                      T(177, 6), T(177, 7)))
X(178, "Estatística", "<p>Lendo o gráfico, na semana passada foram vendidos 45 pastéis (10 + 2 + 4 + 4 + 7 + 8 + 10), 44 refrigerantes (7 + 4 + 4 + 5 + 8 + 8 + 8) e 28 copos de caldo (4 + 3 + 1 + 2 + 4 + 7 + 7). Na próxima semana, os pastéis serão iguais aos refrigerantes previstos, que são refrigerante + caldo: 44 + 28 = 72. A mais: 72 − 45 = <strong>27</strong>. Alternativa <strong>B</strong>.</p><p>44 (C) é só o total de refrigerantes; 71 (E) não desconta os pastéis já vendidos.</p>",
  figs(("q178", "Gráfico de radar “Vendas na última semana”, de domingo a sábado, com três linhas: pastel (domingo 10, segunda 2, terça 4, quarta 4, quinta 7, sexta 8, sábado 10), refrigerante (7, 4, 4, 5, 8, 8, 8) e caldo de cana (4, 3, 1, 2, 4, 7, 7).")),
  ["leitura de gráfico"], enun=p(T(178, 0)) + "[[fig:1]]" + p(T(178, 4), T(178, 5)))
X(179, "Funções", "<p>Cada minuto, o consumo aumenta a potência da lâmpada do cômodo visitado. Pelo gráfico, os acréscimos são 20, 15, 5, 15, 20, 10, 20 e 15. Pela planta, são os cômodos 1 (sala, 20 W), 4 (suíte, 15 W), 5 (banho, 5 W), 4, 1, 6 (cozinha, 10 W), 1 e 4. A sequência é <strong>1 → 4 → 5 → 4 → 1 → 6 → 1 → 4</strong>. Alternativa <strong>A</strong>.</p><p>C acrescenta um nono minuto (passando por 2 e 3), que o gráfico não mostra.</p>",
  figs(("q179", "À esquerda, gráfico do consumo acumulado de energia (W·min) em função do tempo (min), passando pelos pontos (0;0), (1;20), (2;35), (3;40), (4;55), (5;75), (6;85), (7;105) e (8;120). À direita, planta da casa: 1, sala (20 W), junto à entrada; 2, quarto (13 W); 3, banho (2 W); 4, suíte (15 W); 5, banho da suíte (5 W); 6, cozinha (10 W).")),
  ["taxa de variação", "leitura de gráfico"], enun=p(T(179, 0), T(179, 1)) + "[[fig:1]]" + p(T(179, 5)),
  alts={"A": "1 → 4 → 5 → 4 → 1 → 6 → 1 → 4", "B": "1 → 2 → 3 → 1 → 4 → 1 → 4 → 4", "C": "1 → 4 → 5 → 4 → 1 → 6 → 1 → 2 → 3", "D": "1 → 2 → 3 → 5 → 4 → 1 → 6 → 1 → 4", "E": "1 → 4 → 2 → 3 → 5 → 1 → 6 → 1 → 4"})
X(180, "Razão e proporção", "<p>Custo diário em real = gasto em moeda local × taxa de câmbio. França: 315 · 3,14 = 989,10; EUA: 390 · 2,78 = 1 084,20; Austrália: 400 · 2,14 = 856,00; Canadá: 410 · 2,10 = 861,00; Reino Unido: 290 · 4,24 = 1 229,60. O menor custo é o da <strong>Austrália</strong>. Alternativa <strong>A</strong>.</p><p>O Canadá (B) fica muito perto, mas é R$ 5 mais caro por dia.</p>",
  tags=["câmbio", "comparação"],
  enun=p(T(180, 0), T(180, 1)) + tabela(["País de destino", "Moeda local", "Taxa de câmbio", "Gasto diário"],
       [["França", "Euro (€)", "R$ 3,14", "315,00 €"], ["EUA", "Dólar (US$)", "R$ 2,78", "US$ 390,00"], ["Austrália", "Dólar australiano (A$)", "R$ 2,14", "A$ 400,00"],
        ["Canadá", "Dólar canadense (C$)", "R$ 2,10", "C$ 410,00"], ["Reino Unido", "Libra esterlina (£)", "R$ 4,24", "£ 290,00"]]) + p(T(180, 3)))

# Revisão (12/11): a alternativa E da Q39 tinha grudado o eixo do gráfico "População rural".
Q[39]["alternativas"]["E"] = "V"

completar(Q, R)
