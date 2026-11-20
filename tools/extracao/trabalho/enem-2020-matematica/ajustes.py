# Enem 2020 (impresso, 1ª aplicação, jan. 2021), 2º dia, caderno azul: Matemática (questões 136 a 180; no site, 1 a 45).
# Texto legível (sem DECOD). Frações e potências das alternativas em KaTeX; quadros em tabela HTML.
# Página 27 (Q172 e Q173) veio inteira como imagem: enunciados escritos à mão. Alternativas-imagem nas Q166, 175, 176 e 177.
# Anulada: Q157 (Inep não deu motivo; enunciado admite mais de uma interpretação).
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, paragrafos_enem

ID = "enem-2020-matematica"
META = {"id": ID, "banca": "Enem", "ano": 2020, "titulo": "Enem 2020: Matemática", "fonte": "Inep", "dataExame": "2021-01-24",
        "duracaoMinutos": 150, "area": "Matemática", "caderno": "azul", "dia": 2}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2020-dia2-azul")
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


F1 = lambda alt: figs(*alt)
X(136, "Razão e proporção", "<p>A bandeira mede 20M × 14M. Com o tecido verde de 180 cm × 150 cm, o maior módulo possível é o menor entre 180/20 = 9 e 150/14 ≈ 10,7: M = 9 cm. O raio do círculo azul é 3,5M = 31,5 cm, então o diâmetro é 63 cm, e o menor quadrado de tecido azul que contém o círculo tem lado <strong>63 cm</strong>. Alternativa <strong>D</strong>.</p><p>31,5 ≈ 32 (B) é só o raio.</p>",
  figs(("q136", "Desenho da bandeira dentro do quadro externo: retângulo verde, losango amarelo e círculo azul no centro, com o comprimento e a largura do quadro externo indicados.")),
  ["escala", "módulo"],
  enun=p(T(136, 0)) + '<p class="apoio">' + T(136, 1) + "</p>" + OL("Comprimento será de vinte módulos (20 M);", "A distância dos vértices do losango amarelo ao quadro externo será de um módulo e sete décimos (1,7 M);",
         "O raio do círculo azul no meio do losango amarelo será de três módulos e meio (3,5 M).”").replace("<ol>", '<ol type="I">')
       + fonte(T(136, 6)) + p(T(136, 7)) + "[[fig:1]]" + p(T(136, 10)))
X(137, "Razão e proporção", "<p>Na imagem, os assentos vão de 01 a 42, e os vendidos (mais escuros) são 16. A razão entre vendidos e total é <strong>16/42</strong>. Alternativa <strong>A</strong>.</p><p>16/26 (B) compara vendidos com disponíveis, e 26/42 (C) é a fração dos assentos ainda livres.</p>",
  figs(("q137", "Mapa dos assentos do ônibus, numerados de 01 a 42 em quatro fileiras; 16 assentos estão em cor escura (vendidos) e os demais em cor clara.")),
  ["razão"], enun=p(T(137, 0), T(137, 1)) + "[[fig:1]]" + p(T(137, 3)),
  alts=FR("\\frac{16}{42}", "\\frac{16}{26}", "\\frac{26}{42}", "\\frac{42}{26}", "\\frac{42}{16}"))
X(138, "Escala", "<p>28 080 L = 28 080 dm<sup>3</sup> = 28,08 m<sup>3</sup>. A maquete tem 2 × 3,51 × 4 = 28,08 cm<sup>3</sup>. A razão entre os volumes é 28,08 cm<sup>3</sup> : 28,08 m<sup>3</sup> = 1 : 10<sup>6</sup>, e a escala linear é a raiz cúbica disso: <strong>1 : 100</strong>. Alternativa <strong>B</strong>.</p><p>1 : 1 000 000 seria a escala dos volumes, não das medidas.</p>",
  tags=["escala", "volume"])
X(139, "Estatística", "<p>Eficiência = peças/horas. Dia 1: 800/4 = 200; dia 2: 1 000/8 = 125; dia 3: 1 100/5 = <strong>220</strong>; dia 4: 1 800/9 = 200; dia 5: 1 400/10 = 140. A maior razão é a do <strong>dia 3</strong>. Alternativa <strong>C</strong>.</p><p>O dia 4 (D) produziu mais peças, mas com mais horas.</p>",
  figs(("q139", "Dois gráficos de barras por dia: peças produzidas (dia 1: 800; dia 2: 1 000; dia 3: 1 100; dia 4: 1 800; dia 5: 1 400) e horas trabalhadas (dia 1: 4; dia 2: 8; dia 3: 5; dia 4: 9; dia 5: 10).")),
  ["razão", "leitura de gráfico"], enun=p(T(139, 0)) + "[[fig:1]]" + p(T(139, 2)))
X(140, "Geometria plana", "<p>A sala tem 3,2 × 3,6 = 11,52 m<sup>2</sup>, e cada peça 0,8 × 0,8 = 0,64 m<sup>2</sup>: são 11,52/0,64 = 18 peças (aproveitando os recortes). As opções com 18 peças, sem sobra, são C (12 + 6 = 18, por 3 · 35 + 2 · 27 = R$ 159) e E (18, por 6 · 27 = R$ 162). A mais barata é <strong>3 caixas do tipo A e 2 do tipo B</strong>. Alternativa <strong>C</strong>.</p><p>B tem só 16 peças; A e D sobram peças.</p>",
  tags=["área", "otimização"], enun=p(T(140, 0)) + LISTA(T(140, 1).replace("<br>", " ")) + p(T(140, 2)))
X(141, "Contagem", "<p>Algarismo 2 na centena: os quartos de 200 a 299, 100 peças. Na dezena: em cada centena, 120 a 129 etc., 10 por centena, 30 no total. Na unidade: um a cada dez números, 10 por centena, 30. Total: 100 + 30 + 30 = <strong>160</strong>. Alternativa <strong>A</strong>.</p><p>Contar só os números que têm algum 2, sem repetir o algarismo, daria menos peças (como 120 ou 130).</p>",
  tags=["contagem de algarismos"])
X(142, "Probabilidade", "<p>Pela ordem de idade: Orlando (89), Gustavo e Luana (86), Teresa (85), Márcia (84) e Roberto (82) ocupam as seis primeiras posições. Os quatro de 75 anos (Heloísa, Marisa, Pedro e João) disputam por sorteio as posições 7 a 10. A chance de João ser o sétimo é <strong>1/4</strong>. Alternativa <strong>E</strong>.</p><p>1/12 (A) trataria todos os 12 idosos como empatados.</p>",
  tags=["probabilidade", "ordenação"],
  enun=p(T(142, 0)) + tabela(["Nome", "Idade (em ano)"], [["Orlando", "89"], ["Gustavo", "86"], ["Luana", "86"], ["Teresa", "85"], ["Márcia", "84"], ["Roberto", "82"],
                                                          ["Heloisa", "75"], ["Marisa", "75"], ["Pedro", "75"], ["João", "75"], ["Antônio", "72"], ["Fernanda", "70"]]) + p(T(142, 2)),
  alts=FR("\\frac{1}{12}", "\\frac{7}{12}", "\\frac{1}{8}", "\\frac{5}{6}", "\\frac{1}{4}"))
X(143, "Progressões", "<p>O tempo de estudo cresce 0,6 ano a cada 4 anos (5,2; 5,8; 6,4; 7,0). A meta é 70% de 16 = 11,2 anos. A partir de 7,0 (2007), faltam 4,2 anos de estudo, ou seja, 4,2/0,6 = 7 períodos de 4 anos = 28 anos: <strong>2035</strong>. Alternativa <strong>D</strong>.</p><p>2031 (C) contaria um período a menos.</p>",
  tags=["progressão aritmética"],
  enun=p(T(143, 0)) + '<p class="apoio"><strong>Tempo médio de estudo de pessoas acima de 14 anos</strong></p>'
       + tabela(["Ano da Pesquisa", "1995", "1999", "2003", "2007"], [["Tempo de estudo (em ano)", "5,2", "5,8", "6,4", "7,0"]]) + fonte(T(143, 3)) + p(T(143, 4), T(143, 5)))
X(144, "Grandezas e medidas", "<p>Falta encher metade do balde: 9 L = 9 000 mL. Por segundo caem 5 · 0,05 = 0,25 mL. Tempo: 9 000/0,25 = 36 000 s = 10 h = <strong>1 × 10<sup>1</sup> h</strong>. Alternativa <strong>B</strong>.</p><p>2 × 10<sup>1</sup> (A) seria o tempo para encher o balde inteiro.</p>",
  tags=["conversão de unidades", "notação científica"], enun=p(T(144, 0).replace("10−2", "10<sup>−2</sup>"), T(144, 1)),
  alts=FR("2 \\times 10^{1}", "1 \\times 10^{1}", "2 \\times 10^{-2}", "1 \\times 10^{-2}", "1 \\times 10^{-3}"))
X(145, "Escala", "<p>A base do troféu é um quadrado de 50 cm, e a caixa tem base de 8 cm × 10 cm, com 1 cm de folga de cada lado. O lado da base da miniatura é no máximo 8 − 2 = 6 cm, o que dá a escala 6/50 = 0,12. A altura da miniatura é 0,12 · 100 = 12 cm, e com os 2 cm até a tampa a caixa deve ter <strong>14 cm</strong>. Alternativa <strong>B</strong>.</p><p>12 (A) esquece a folga até a tampa; usar o lado de 10 cm não respeitaria a folga no lado de 8 cm.</p>",
  figs(("q145", "Figura 1: troféu com uma esfera escura sobre três hastes, presas a uma base de madeira quadrada de 50 cm × 50 cm. Figura 2: caixa de vidro com base de 8 cm × 10 cm e altura desconhecida, marcada com “?”.")),
  ["escala", "semelhança"], enun=p(T(145, 0)) + "[[fig:1]]" + p(T(145, 4)))
X(146, "Inequações", "<p>Com h = 16: |32 + b − 63,5| ≤ 1,5, ou |b − 31,5| ≤ 1,5. Isso equivale a −1,5 ≤ b − 31,5 ≤ 1,5, isto é, <strong>30 ≤ b ≤ 33</strong>. Alternativa <strong>C</strong>.</p><p>B e D pegam só metade do intervalo; A e E ignoram um dos limites do módulo.</p>",
  figs(("q146", "Perfil de uma escada com a altura do degrau h e a profundidade da pisada b indicadas.")),
  ["inequação modular"],
  enun=p(T(146, 0), "\\(|2h + b - 63{,}5| \\le 1{,}5\\) e \\(16 \\le h \\le 19\\), nas quais <em>h</em> é a altura do degrau (denominada espelho) e <em>b</em> é a profundidade da pisada, como mostra a figura. Por conveniência, escolheu-se a altura do degrau como sendo <em>h</em> = 16. As unidades de <em>h</em> e <em>b</em> estão em centímetro.")
       + "[[fig:1]]" + p(T(146, 3)),
  alts=FR("30 \\le b", "30 \\le b \\le 31{,}5", "30 \\le b \\le 33", "31{,}5 \\le b \\le 33", "b \\le 33"))
X(147, "Razão e proporção", "<p>O tipo A mostra X litros por 100 km. Então 1 litro rende 100/X quilômetros, que é o que o tipo B mostraria: <strong>100/X</strong>. Alternativa <strong>C</strong>.</p><p>X/100 (B) é o consumo em litros por quilômetro, o inverso do pedido.</p>",
  tags=["razão inversa"],
  enun=p(T(147, 0)) + LISTA(T(147, 1).split(" Um veículo")[0].replace("quantidade X", "quantidade <em>X</em>")) + p("Um veículo" + T(147, 1).split(" Um veículo")[1].replace("“X/100”", "“<em>X</em>/100”")),
  alts=FR("X \\cdot 100", "\\frac{X}{100}", "\\frac{100}{X}", "\\frac{1}{X}", "1 \\cdot X"))
X(148, "Porcentagem", "<p>Trabalham os jovens que “somente trabalham” (45,2%) e os que “trabalham e estudam” (13,6%): 58,8%. Então 0,588 · 363 000 = <strong>213 444</strong>. Alternativa <strong>C</strong>.</p><p>164 076 (B) usa só os 45,2% que somente trabalham.</p>",
  figs(("q148", "Gráfico de barras “Jovens em atividade entre 15 e 29 anos (%)”: somente estuda 21,6; trabalha e estuda 13,6; somente trabalha 45,2; não trabalha nem estuda 19,6.")),
  ["porcentagem", "leitura de gráfico"], enun=p(T(148, 0)) + "[[fig:1]]" + p(T(148, 4)))
X(149, "Logaritmos", "<p>Aplicando logaritmo a f = A/r<sup>B</sup>: log f = log A − log(r<sup>B</sup>) = log A − B · log r. Com Y = log f e X = log r: <strong>Y = log(A) − B · X</strong>, uma reta. Alternativa <strong>A</strong>.</p><p>As outras alternativas não aplicam corretamente as propriedades do logaritmo do quociente e da potência.</p>",
  tags=["propriedades dos logaritmos", "Lei de Zipf"],
  enun=p("A Lei de Zipf, batizada com o nome do linguista americano George Zipf, é uma lei empírica que relaciona a frequência (<em>f</em>) de uma palavra em um dado texto com o seu <em>ranking</em> (<em>r</em>). Ela é dada por \\(f = \\dfrac{A}{r^B}\\).",
         T(149, 3).replace("ranking", "<em>ranking</em>"))
       + fonte("Disponível em: http://klein.sbm.org.br. Acesso em: 12 ago. 2020 (adaptado).")
       + p("Com base nos valores de \\(X = \\log(r)\\) e \\(Y = \\log(f)\\), é possível estimar valores para <em>A</em> e <em>B</em>. No caso hipotético em que a lei é verificada exatamente, a relação entre <em>Y</em> e <em>X</em> é"),
  alts=FR("Y = \\log(A) - B \\cdot X", "Y = \\dfrac{\\log(A)}{X + \\log(B)}", "Y = \\dfrac{\\log(A)}{B} - X", "Y = \\dfrac{\\log(A)}{B \\cdot X}", "Y = \\dfrac{\\log(A)}{X^B}"))
X(150, "Função exponencial", "<p>A razão Q(t)/Q<sub>0</sub> = 2<sup>−t/5 730</sup> mostra quantas meias-vidas se passaram. Fóssil 1: 32/128 = 1/4 (2 meias-vidas); 2: 8/256 = 1/32 (5); 3: 64/512 = 1/8 (3); 4: 512/1 024 = 1/2 (1); 5: 128/2 048 = 1/16 (4). O mais antigo é o <strong>fóssil 2</strong>. Alternativa <strong>B</strong>.</p><p>O fóssil 3 (C) tem o maior Q<sub>0</sub>, mas isso não indica idade.</p>",
  tags=["meia-vida", "datação por carbono 14"],
  enun=p("Enquanto um ser está vivo, a quantidade de carbono 14 nele existente não se altera. Quando ele morre, essa quantidade vai diminuindo. Sabe-se que a meia-vida do carbono 14 é de 5 730 anos, ou seja, num fóssil de um organismo que morreu há 5 730 anos haverá metade do carbono 14 que existia quando ele estava vivo. Assim, cientistas e arqueólogos usam a seguinte fórmula para saber a idade de um fóssil encontrado: \\(Q(t) = Q_0 \\cdot 2^{-\\frac{t}{5730}}\\), em que <em>t</em> é o tempo, medido em ano, <em>Q</em>(<em>t</em>) é a quantidade de carbono 14 medida no instante <em>t</em> e <em>Q</em><sub>0</sub> é a quantidade de carbono 14 no ser vivo correspondente.",
         T(150, 4))
       + tabela(["Fóssil", "<em>Q</em><sub>0</sub>", "<em>Q</em>(<em>t</em>)"], [["1", "128", "32"], ["2", "256", "8"], ["3", "512", "64"], ["4", "1 024", "512"], ["5", "2 048", "128"]]) + p(T(150, 6)))
X(151, "Geometria espacial", "<p>Um tronco de pirâmide de base quadrada tem duas bases quadradas (a maior embaixo, a menor em cima) e quatro faces laterais. Como é reto, as faces laterais são congruentes: trapézios isósceles. O tronco é formado por <strong>2 quadrados e 4 trapézios isósceles</strong>. Alternativa <strong>C</strong>.</p><p>Com 4 retângulos (A) seria um prisma; com triângulos (B), uma pirâmide inteira.</p>",
  tags=["tronco de pirâmide"])
X(152, "Geometria espacial", "<p>Sai de T1 o volume c · L · x. Os aeradores multiplicam o volume por 1,15 · 1,10 = 1,265. Em T2, a base tem área (c/2) · 2L = c · L, a mesma de T1. Então c · L · y = 1,265 · c · L · x, ou seja, <strong>y = 1,265x</strong>. Alternativa <strong>A</strong>.</p><p>1,250 (B) somaria os percentuais (15% + 10%) em vez de compô-los.</p>",
  figs(("q152", "Esquema: um tanque T1, uma bomba B, dois aeradores A1 e A2 ligados por canos e um tanque T2, mais baixo e mais largo.")),
  ["aumentos sucessivos", "volume do prisma"],
  enun=p(T(152, 0)) + "[[fig:1]]" + p("Os tanques T1 e T2 são prismas retos de bases retangulares, sendo que a base de T1 tem comprimento <em>c</em> e largura <em>L</em>, e a base de T2 tem comprimento \\(\\frac{c}{2}\\) e largura 2<em>L</em>.",
                                      T(152, 4).replace("denotada por X", "denotada por <em>x</em>").replace("denotada por y", "denotada por <em>y</em>")) + fonte(T(152, 5)) + p(T(152, 6)))
X(153, "Razão e proporção", "<p>Tempo = distância/velocidade. Segunda: ônibus 2/9 ≈ 0,22 h, bicicleta 3/15 = 0,20 h. Terça: 2/20 = 0,10 contra 3/22 ≈ 0,14. Quarta: 2/15 ≈ 0,133 contra 3/24 = 0,125. Quinta: 2/12 ≈ 0,17 contra 3/15 = 0,20. Sexta: 2/10 = 0,20 contra 3/18 ≈ 0,17. Sábado: 2/30 ≈ 0,07 contra 3/16 ≈ 0,19. A bicicleta é mais rápida às <strong>segundas, quartas e sextas-feiras</strong>. Alternativa <strong>C</strong>.</p><p>Comparar só as velocidades, sem as distâncias diferentes, daria outros dias.</p>",
  tags=["velocidade média", "comparação"],
  enun=p(T(153, 0)) + LISTA(T(153, 1).replace("<br>", " ")) + p(T(153, 2))
       + tabela(["Dia da semana", "Ônibus (km/h)", "Bicicleta (km/h)"], [["Segunda-feira", "9", "15"], ["Terça-feira", "20", "22"], ["Quarta-feira", "15", "24"], ["Quinta-feira", "12", "15"], ["Sexta-feira", "10", "18"], ["Sábado", "30", "16"]])
       + p(T(153, 4)))
X(154, "Notação científica", "<p>1 micrômetro = 10<sup>−6</sup> m. Então 100 micrômetros = 10<sup>2</sup> · 10<sup>−6</sup> = <strong>1,0 × 10<sup>−4</sup> m</strong>. Alternativa <strong>C</strong>.</p><p>1,0 × 10<sup>−6</sup> (D) é o valor de um único micrômetro.</p>",
  figs(("q154", "Imagem ampliada de microscópio de uma miniatura de carro de Fórmula 1 feita em impressora 3D.")),
  ["potências de 10"], enun=p(T(154, 0)) + "[[fig:1]]" + p(T(154, 2)),
  alts=FR("1{,}0 \\times 10^{-1}", "1{,}0 \\times 10^{-3}", "1{,}0 \\times 10^{-4}", "1{,}0 \\times 10^{-6}", "1{,}0 \\times 10^{-7}"))
X(155, "Progressões", "<p>Os lados formam uma progressão geométrica: 1, 1/2, 1/4, … O n-ésimo quadrado tem lado (1/2)<sup>n−1</sup>. O centésimo tem lado <strong>(1/2)<sup>99</sup></strong>. Alternativa <strong>B</strong>.</p><p>(1/2)<sup>100</sup> (A) esquece que o primeiro termo é 1 = (1/2)<sup>0</sup>.</p>",
  figs(("q155", "Quadrado PRST de lado 1 e, abaixo dele, uma sequência de quadrados cada vez menores, de lados 1/2, 1/4 e assim por diante, com reticências indicando a continuação.")),
  ["progressão geométrica"], enun=p(T(155, 0)) + "[[fig:1]]" + p(T(155, 4).replace("PRST", "<em>PRST</em>")),
  alts=FR("\\left(\\frac{1}{2}\\right)^{100}", "\\left(\\frac{1}{2}\\right)^{99}", "\\left(\\frac{1}{2}\\right)^{97}", "\\left(\\frac{1}{2}\\right)^{-98}", "\\left(\\frac{1}{2}\\right)^{-99}"))
X(156, "Estatística", "<p>Como o estoque inicial era igual para todos, a arrecadação é proporcional a preço × percentual vendido. I: 200 · 13 = 2 600; II: 170 · 10 = 1 700; III: 150 · 16 = 2 400; IV: 100 · 29 = <strong>2 900</strong>; V: 80 · 32 = 2 560. O perfume IV arrecadou mais. Alternativa <strong>D</strong>.</p><p>O V (E) foi o mais vendido, mas é o mais barato; o I (A) é o mais caro, mas vendeu pouco.</p>",
  figs(("q156", "Gráfico de barras do preço por unidade: perfume I R$ 200, II R$ 170, III R$ 150, IV R$ 100, V R$ 80. Gráfico de setores da porcentagem vendida: I 13%, II 10%, III 16%, IV 29%, V 32%.")),
  ["média ponderada", "leitura de gráfico"], enun=p(T(156, 0)) + "[[fig:1]]" + p(T(156, 9)))
X(157, "Probabilidade", "<p>Pela análise do Treineiros: se a primeira pessoa a revelar e a última presenteada forem tratadas como duas pessoas distintas escolhidas ao acaso entre as dez, a chance de serem o casal (em qualquer ordem) é 2/(10 · 9) = 1/45. Mas, quando os presentes fecham um único ciclo, a última presenteada é a própria pessoa que começou, e o enunciado não diz como a brincadeira recomeça se o ciclo se fecha antes. Essas leituras levam a respostas diferentes. A resposta esperada seria provavelmente a B. Alternativa <strong>B</strong>, se a questão não tivesse sido anulada.</p>",
  tags=["probabilidade"],
  anulacao={"fonte": "analise", "motivo": "O Inep anulou a questão sem divulgar o motivo. Pela análise, o enunciado permite mais de uma interpretação: se o ciclo de presentes se fecha, a última presenteada é a própria pessoa que começou, e não fica claro como a brincadeira continua; cada leitura leva a uma probabilidade diferente."},
  alts=FR("\\frac{1}{5}", "\\frac{1}{45}", "\\frac{1}{50}", "\\frac{1}{90}", "\\frac{1}{100}"))
X(158, "Análise combinatória", "<p>Pelo quadriculado, B está 4 quadras à direita e 3 acima de A, e C está 2 à direita e 2 acima de A. Caminhos de A a B: C(7, 3) = 35. Caminhos que passam por C: C(4, 2) · C(3, 1) = 6 · 3 = 18. Sem passar por C: 35 − 18 = <strong>17</strong>. Alternativa <strong>C</strong>.</p><p>35 (D) é o total, sem excluir os caminhos por C; 18 é o número dos que passam por C.</p>",
  figs(("q158", "Quadriculado de ruas com o ponto A embaixo à esquerda, C mais acima e à direita, e B no alto à direita: B fica 4 quadras à direita e 3 acima de A; C, 2 à direita e 2 acima de A.")),
  ["permutação com repetição", "caminhos em grade"], enun=p(T(158, 0)) + "[[fig:1]]" + p(T(158, 2)))
X(159, "Funções", "<p>Custo = 15 · preço do saco + frete por km · distância. A: 345 + 10 = 355; B: 322,50 + 36 = 358,50; C: 330 + 21 = <strong>351</strong>; D: 315 + 63 = 378; E: 360 + 5 = 365. O mais econômico é o <strong>C</strong>. Alternativa <strong>C</strong>.</p><p>O D (D) tem o saco mais barato, mas o frete mais caro.</p>",
  tags=["custo total"],
  enun=p(T(159, 0)) + tabela(["Depósito", "Valor do saco de cimento (R$)", "Valor do frete para cada quilômetro (R$)", "Distância entre a casa e o depósito (km)"],
                             [["A", "23,00", "1,00", "10"], ["B", "21,50", "3,00", "12"], ["C", "22,00", "1,50", "14"], ["D", "21,00", "3,50", "18"], ["E", "24,00", "2,50", "2"]]) + p(T(159, 2)))
X(160, "Razão e proporção", "<p>A moto gasta 0,05 L/km. Até o posto Estrela são 420 km: gasta 21 L dos 22 e chega com 1 L. Depois precisa ir 80 km ao destino, rodar 200 km lá e voltar 80 km até o Estrela: 360 km = 18 L. Como já tem 1 L, deve abastecer <strong>17 L</strong>. Alternativa <strong>C</strong>.</p><p>18 (D) esquece o litro que sobrou no tanque.</p>",
  tags=["consumo", "proporção"])
X(161, "Geometria espacial", "<p>Os volumes são iguais: πR<sup>2</sup>h = πr<sup>2</sup>(h/4). Então r<sup>2</sup> = 4R<sup>2</sup> e <strong>r = 2R</strong>. Alternativa <strong>B</strong>.</p><p>4R (C) esquece a raiz quadrada; R/2 (A) inverte a relação.</p>",
  tags=["volume do cilindro"], enun=p(T(161, 0).replace("Se R denota", "Se <em>R</em> denota")),
  alts=FR("\\frac{R}{2}", "2R", "4R", "5R", "16R"))
X(162, "Geometria plana", "<p>Cada lote tem 10 m × 20 m = 200 m², e a casa deve ter entre 80 e 100 m². Casa 1: 5 × 15 = 75 m² (pequena). Casa 2: 8 × 15 = 120 m² (grande). Casa 3: 5 × 12 = 60 m². Casa 4: fica a só 2 m da rua. Casa 5: 4 m da rua, 1 m das divisas e 5 × 18 = 90 m² (45%). Só a <strong>casa 5</strong> é aprovada. Alternativa <strong>E</strong>.</p><p>A casa 4 tem área adequada (96 m²), mas não respeita o afastamento da rua.</p>",
  figs(("q162", "Esquema de lotes de 10 m × 20 m junto a duas ruas, com as casas 1 a 5 e os afastamentos em metro: casa 1 (4 da rua lateral, 1 das divisas laterais, 1 do fundo, 4 da rua de baixo); casa 2 (1, 1, 1 e 4); casa 3 (4, 1, 4 e 4); casa 4 (2, 2, 2 da rua e 2); casa 5 (4 da rua, 1, 1 e 1).")),
  ["área", "porcentagem"],
  enun=p(T(162, 0)) + LISTA(T(162, 1).split(" Um construtor")[0]) + p("Um construtor" + T(162, 1).split(" Um construtor")[1], T(162, 2)) + "[[fig:1]]" + p(T(162, 4)))
X(163, "Análise combinatória", "<p>“I AM POTTER” tem 4 vogais (I, A, O, E) e 5 consoantes (M, P, T, T, R). Com 9 letras intercaladas, a única forma é C V C V C V C V C. As vogais se permutam de 4! modos; as consoantes, com o T repetido, de 5!/2! modos. Total: <strong>4! · 5!/2</strong>. Alternativa <strong>E</strong>.</p><p>4! 5! (B) esquece a repetição do T; 2 × 4! 5! (C) supõe que a palavra possa começar por vogal.</p>",
  tags=["anagramas", "permutação com repetição"], enun=p(T(163, 0).replace("livros Harry Potter", "livros <em>Harry Potter</em>"), T(163, 1)),
  alts=FR("9!", "4!\\,5!", "2 \\times 4!\\,5!", "\\frac{9!}{2}", "\\frac{4!\\,5!}{2}"))
X(164, "Funções", "<p>Somando os intervalos em que a curva fica acima da linha de 55 dB: a curva cruza os 55 dB sempre em cima de linhas da grade. Fica acima de 2 h a 5 h, de 6 h a 9 h, de 11 h a 14 h, de 16 h a 17 h e de 19 h a 22 h: 3 + 3 + 3 + 1 + 3 = <strong>13 horas</strong>. Alternativa <strong>E</strong>.</p><p>Contar só os picos (5) ou alguns trechos leva às outras alternativas.</p>",
  figs(("q164", "Gráfico do ruído (decibel) ao longo das 24 horas, com uma linha horizontal em 55: a curva fica acima dela aproximadamente de 2 h a 5 h, de 5,5 h a 9 h, de 11 h a 14 h, de 16 h a 17 h e de 19 h a 22 h.")),
  ["leitura de gráfico"], enun=p(T(164, 0)) + "[[fig:1]]" + fonte("Disponível em: www.revistaencontro.com.br. Acesso em: 12 ago. 2020 (adaptado).") + p(T(164, 4)))
X(165, "Estatística", "<p>A soma atual é 15 · 1,93 = 28,95 m; a desejada, 15 · 1,99 = 29,85 m. Sem os quatro mais baixos (7,30 m), sobram 21,65 m; com o novo de 2,02 m, 23,67 m. Os outros três devem somar pelo menos 29,85 − 23,67 = 6,18 m: média de <strong>2,06 m</strong>. Alternativa <strong>D</strong>.</p><p>1,99 (próximo de B) é a média pretendida para o time, não para os três novos.</p>",
  tags=["média aritmética"])
X(166, "Funções", "<p>A vazão é constante. No corpo da garrafa, de seção larga e constante, a altura sobe devagar e de forma linear. No gargalo, que vai se estreitando, o mesmo volume ocupa uma altura cada vez maior, e a curva fica mais inclinada. O gráfico é uma reta seguida de uma curva que sobe cada vez mais rápido. Alternativa <strong>B</strong>.</p><p>A seria uma garrafa cilíndrica; C e E, recipientes que se alargam para cima.</p>",
  figs(("q166", "Silhueta de uma garrafa de espumante com corpo cilíndrico e gargalo estreito; uma linha marca o nível de envasamento, no início do gargalo."),
       ("q166a", "Gráfico da altura em função do tempo: uma reta."),
       ("q166b", "Gráfico da altura em função do tempo: uma reta que, no final, vira uma curva cada vez mais inclinada."),
       ("q166c", "Gráfico da altura em função do tempo: reta no início e depois uma curva que vai ficando menos inclinada."),
       ("q166d", "Gráfico da altura em função do tempo: curva que começa quase horizontal e vai ficando cada vez mais inclinada."),
       ("q166e", "Gráfico da altura em função do tempo: curva que começa muito inclinada e vai ficando menos inclinada.")),
  ["taxa de variação"], enun=p(T(166, 0)) + "[[fig:1]]" + p(T(166, 3)), alts=ALT(2))
X(167, "Porcentagem", "<p>Os aumentos são 20% de 120 = 24 e 10% de 700 = 70: R$ 94 a mais. Para manter o total, a mesada de R$ 400 deve cair R$ 94: 94/400 = <strong>23,5%</strong>. Alternativa <strong>B</strong>.</p><p>30% (C) somaria os percentuais dos dois aumentos.</p>",
  tags=["porcentagem"], enun=p(T(167, 0)) + tabela(["Internet", "Mensalidade escolar", "Mesada do filho"], [["120", "700", "400"]]) + p(T(167, 2)))
X(168, "Geometria espacial", "<p>A água deve subir de 8 cm para 15 cm, num recipiente de base 3 cm × 4 cm. O volume a ocupar é 7 · 3 · 4 = 84 cm<sup>3</sup>. Com bolinhas de 6 cm<sup>3</sup>: 84/6 = <strong>14 bolinhas</strong>. Alternativa <strong>A</strong>.</p><p>O objeto flutuando já está considerado no nível de 8 cm; a altura total de 17 cm (E: 34 bolinhas, até 17) não é o que se pede.</p>",
  figs(("q168", "Recipiente em forma de paralelepípedo de base 4 cm × 3 cm e altura 17 cm, com água até 8 cm e um objeto flutuando na superfície.")),
  ["volume", "deslocamento"], enun=p(T(168, 0), T(168, 1).replace("6 cm³", "6 cm<sup>3</sup>")) + "[[fig:1]]" + p(T(168, 4)))
X(169, "Conjuntos", "<p>Das 200 pessoas, 20 não têm antígeno: 180 têm A ou B. Pela união de conjuntos, 100 + 110 − n(A ∩ B) = 180, então 30 têm os dois (tipo AB). As do tipo A (só o antígeno A) são 100 − 30 = <strong>70</strong>. Alternativa <strong>C</strong>.</p><p>100 (E) inclui as 30 pessoas do tipo AB.</p>",
  tags=["união de conjuntos", "diagrama de Venn"],
  enun=p(T(169, 0)) + LISTA(T(169, 1)) + fonte(T(169, 2)) + p(T(169, 3)))
X(170, "Razão e proporção", "<p>O capital tem 4 + 6 + 6 = 16 partes; para igualar, cada um deve ficar com 16/3. Antônio precisa de 16/3 − 4 = 4/3, comprando 2/3 de cada sócio. Em relação às 6 partes de cada um, isso é (2/3)/6 = <strong>1/9</strong>. Alternativa <strong>C</strong>.</p><p>1/3 (B) seria a fração do capital total que cada um deve ter no fim.</p>",
  tags=["divisão proporcional", "frações"],
  alts=FR("\\frac{1}{2}", "\\frac{1}{3}", "\\frac{1}{9}", "\\frac{2}{3}", "\\frac{4}{3}"))
X(171, "Geometria plana", "<p>O ângulo interno do octógono regular é 135°. Onde quatro octógonos se encontram, sobra 360° − 2 · 135° = 90° em cada canto: os espaços internos são <strong>quadrados</strong>. Na borda, entre dois octógonos, o espaço tem um ângulo de 90° e lados iguais: <strong>triângulos retângulos isósceles</strong>. São necessários os formatos 1 e 3. Alternativa <strong>D</strong>.</p><p>Triângulos equiláteros (2) têm ângulos de 60°, que não encaixam.</p>",
  figs(("q171", "Painel retangular coberto por oito octógonos cinza em duas fileiras, com pequenos espaços brancos entre eles: quadrados no meio e triângulos nas bordas.")),
  ["polígonos regulares", "ladrilhamento"], enun=p(T(171, 0)) + fonte(T(171, 1)) + p(T(171, 2)) + "[[fig:1]]" + p(T(171, 4)))
X(172, "Geometria espacial", "<p>As 20 mangueiras ligam o ponto do poste a 3 m de altura a 20 pontos da circunferência, e todas têm o mesmo comprimento. Usando exatamente 100 m, cada uma mede 5 m. Ela é a hipotenusa de um triângulo retângulo com altura 3 m e raio r: r<sup>2</sup> + 3<sup>2</sup> = 5<sup>2</sup>, <strong>r = 4,00 m</strong>. Alternativa <strong>A</strong>.</p><p>5,00 (C) seria o comprimento de cada mangueira, não o raio.</p>",
  figs(("q172", "Figura 1: foto noturna de uma árvore de Natal em forma de cone feita de luzes presas a um poste. Figura 2: esquema do cone, com o poste no centro C da circunferência no chão, segmentos de um ponto do poste a 3 m de altura até a circunferência.")),
  ["teorema de Pitágoras", "cone"],
  enun=p("No período de fim de ano, o síndico de um condomínio resolveu colocar, em um poste, uma iluminação natalina em formato de cone, lembrando uma árvore de Natal, conforme as figuras 1 e 2.")
       + "[[fig:1]]" + p("A árvore deverá ser feita colocando-se mangueiras de iluminação, consideradas segmentos de reta de mesmo comprimento, a partir de um ponto situado a 3 m de altura no poste até um ponto de uma circunferência de fixação, no chão, de tal forma que esta fique dividida em 20 arcos iguais. O poste está fixado no ponto <em>C</em> (centro da circunferência) perpendicularmente ao plano do chão.",
                         "Para economizar, ele utilizará mangueiras de iluminação aproveitadas de anos anteriores, que juntas totalizaram pouco mais de 100 m de comprimento, dos quais ele decide usar exatamente 100 m e deixar o restante como reserva.",
                         "Para que ele atinja seu objetivo, o raio, em metro, da circunferência deverá ser de"),
  alts={"A": "4,00.", "B": "4,87.", "C": "5,00.", "D": "5,83.", "E": "6,26."})
X(173, "Trigonometria", "<p>Ao meio-dia a luz passa pelos 30 cm do vão. Com os raios a 30° da vertical, cada viga de altura h faz uma sombra de h · tg 30° sobre o vão. Para passar metade da luz, a sombra deve ser 15 cm: h = 15/tg 30° = 15√3 ≈ <strong>26 cm</strong>. Alternativa <strong>C</strong>.</p><p>Usar o seno ou o cosseno no lugar da tangente leva a 15 cm, 30 cm ou 52 cm.</p>",
  figs(("q173", "Ilustração de um pergolado: vigas iguais, paralelas e alinhadas, com um detalhe ampliado mostrando o vão de 30 cm entre duas vigas.")),
  ["tangente", "triângulo retângulo"],
  enun=p("Pergolado é o nome que se dá a um tipo de cobertura projetada por arquitetos, comumente em praças e jardins, para criar um ambiente para pessoas ou plantas, no qual há uma quebra da quantidade de luz, dependendo da posição do sol. É feito como um estrado de vigas iguais, postas paralelas e perfeitamente em fila, como ilustra a figura.")
       + "[[fig:1]]" + p("Um arquiteto projeta um pergolado com vãos de 30 cm de distância entre suas vigas, de modo que, no solstício de verão, a trajetória do sol durante o dia seja realizada num plano perpendicular à direção das vigas, e que o sol da tarde, no momento em que seus raios fizerem 30° com a posição a pino, gere a metade da luz que passa no pergolado ao meio-dia.",
                         "Para atender à proposta do projeto elaborado pelo arquiteto, as vigas do pergolado devem ser construídas de maneira que a altura, em centímetro, seja a mais próxima possível de"),
  alts={"A": "9.", "B": "15.", "C": "26.", "D": "52.", "E": "60."})
X(174, "Geometria plana", "<p>Todas as vias têm 30 m de largura. MN (100 m, andando): 3 000 m<sup>2</sup> · 4 = 12 000. NO (300 m, parados): 9 000 m<sup>2</sup> · 6 = 54 000. OP (200 m, movimentando sem sair): 6 000 m<sup>2</sup> · 5 = 30 000. QR (100 m, andando): 3 000 · 4 = 12 000. Total: 108 000; descontando 4 carros de som (4 000): <strong>104 000</strong>. Alternativa <strong>B</strong>.</p><p>110 000 (A) não desconta os carros e inclui outro erro de densidade.</p>",
  figs(("q174", "Esboço da manifestação: via principal de 30 m de largura com os trechos MN (100 m, pessoas andando na mesma direção), NO (300 m, pessoas paradas) e OP (200 m, pessoas se movimentando sem deixar o local), e a via afluente QR (100 m de comprimento, 30 m de largura, pessoas andando); quatro carros de som aparecem como retângulos cinza.")),
  ["área", "densidade"],
  enun=p(T(174, 0)) + LISTA(T(174, 1)) + p(T(174, 2), T(174, 3).replace("MN, NO e OP", "<em>MN</em>, <em>NO</em> e <em>OP</em>").replace("QR .", "<em>QR</em>.")) + "[[fig:1]]" + p(T(174, 6), T(174, 7)))
X(175, "Funções", "<p>Pelo gráfico, até cerca de 13 itens o custo é maior que a receita (lucro negativo), com o maior prejuízo perto de 10 itens; depois a receita supera o custo, e o lucro chega perto de 40 reais por volta de 25 itens, caindo no fim. O gráfico de Receita − Custo começa negativo, desce, cruza o zero e forma um pico positivo: é o da alternativa <strong>A</strong>. Alternativa <strong>A</strong>.</p><p>B inverte o sinal (seria Custo − Receita); D e E repetem a curva do custo ou da receita.</p>",
  figs(("q175", "Gráfico de receita e custo (R$) em função da quantidade de itens produzidos (0 a 30): o custo sobe rápido até cerca de 45 perto de 10 itens, cai até cerca de 10 perto de 25 itens e volta a subir; a receita cresce de forma suave até cerca de 50 perto de 28 itens; as curvas se cruzam perto de 13 itens."),
       ("q175a", "Gráfico de lucro: começa perto de zero, desce até cerca de −20 perto de 10 itens, sobe cruzando o zero perto de 14 itens, chega a cerca de 40 perto de 24 itens e cai para cerca de 10 em 30 itens."),
       ("q175b", "Gráfico de lucro: sobe até cerca de 20 perto de 8 itens, desce até cerca de −40 perto de 25 itens e volta a subir."),
       ("q175c", "Gráfico de lucro sempre positivo: um arco até cerca de 20, volta a zero perto de 15 itens e outro arco até cerca de 40 perto de 24 itens."),
       ("q175d", "Gráfico igual à curva do custo: sobe até cerca de 45 perto de 10 itens, cai até cerca de 10 perto de 25 e volta a subir."),
       ("q175e", "Gráfico igual à curva da receita: sobe de forma suave até cerca de 50 perto de 27 itens.")),
  ["gráfico de funções", "lucro"], enun=p(T(175, 0)) + "[[fig:1]]" + p(T(175, 3)), alts=ALT(2))
X(176, "Geometria espacial", "<p>O sólido tem quatro cubos: dois empilhados à esquerda, ao lado de um em baixo, e um em cima recuado. As projeções certas devem mostrar, no chão e em cada parede, as formas coerentes com a mesma posição do sólido. Só na alternativa <strong>E</strong> as três sombras (as duas paredes e o piso) correspondem à posição desenhada. Alternativa <strong>E</strong>.</p><p>Nas outras, pelo menos uma projeção tem um quadrado a mais, a menos ou deslocado.</p>",
  figs(("q176", "Sólido formado por quatro cubos iguais: três em forma de L e um quarto sobre um deles."),
       ("q176a", "Alternativa A: o sólido num canto entre duas paredes e um piso quadriculados, com as projeções em cinza em cada plano."),
       ("q176b", "Alternativa B: o sólido em outra posição, com projeções em cinza nas paredes e no piso."),
       ("q176c", "Alternativa C: o sólido em outra posição, com projeções em cinza nas paredes e no piso."),
       ("q176d", "Alternativa D: o sólido em outra posição, com projeções em cinza nas paredes e no piso."),
       ("q176e", "Alternativa E: o sólido em pé, com projeções em cinza nas duas paredes e no piso coerentes com sua posição.")),
  ["projeção ortogonal", "vistas"], enun=p(T(176, 0)) + "[[fig:1]]" + p(T(176, 2), T(176, 3)), alts=ALT(2))
X(177, "Geometria espacial", "<p>O telhado da Figura 2 tem duas águas principais e uma terceira caída numa das extremidades (um lado em forma de triângulo). Na planta, isso aparece como o retângulo dividido pela cumeeira, com duas setas para os lados maiores, e um triângulo numa ponta com a seta para fora, sem ultrapassar o contorno da casa. É a planta da alternativa <strong>B</strong>. Alternativa <strong>B</strong>.</p><p>A tem a terceira água sem seta; D e E representam quatro caídas; C desenha a terceira água para fora da casa.</p>",
  figs(("q177", "Figura 1: (a) casa com telhado de duas águas e (b) a planta do telhado, um retângulo com a cumeeira no meio e setas apontando para os dois lados maiores. Figura 2: casa com telhado de três águas, com uma caída a mais numa das extremidades."),
       ("q177a", "Planta A: retângulo com a cumeeira e duas linhas inclinadas formando um triângulo numa ponta; setas para cima e para baixo, sem seta no triângulo."),
       ("q177b", "Planta B: retângulo com a cumeeira e duas linhas inclinadas formando um triângulo numa ponta; setas para cima, para baixo e, no triângulo, para fora."),
       ("q177c", "Planta C: retângulo com um triângulo saindo para fora da casa numa ponta, com seta para fora, e setas para cima e para baixo."),
       ("q177d", "Planta D: retângulo com cumeeira e triângulos nas duas pontas (quatro águas), com setas para cima e para baixo."),
       ("q177e", "Planta E: losango alongado com triângulos para fora dos dois lados e setas cruzadas no centro.")),
  ["vistas", "planta"], enun=p(T(177, 0)) + "[[fig:1]]" + p(T(177, 4)), alts=ALT(2))
X(178, "Estatística", "<p>CRC = 0,7 · EC com chuva + 0,3 · EC sem chuva. I: 4,2 + 0,9 = <strong>5,1</strong>; II: 4,9 − 1,2 = 3,7; III: −1,4 + 3,0 = 1,6; IV: 1,4 + 2,4 = 3,8; V: −4,2 + 2,1 = −2,1. O maior CRC é o do pneu <strong>I</strong>. Alternativa <strong>A</strong>.</p><p>O II (B) é o melhor só na chuva; o III (C), só no seco.</p>",
  tags=["média ponderada", "probabilidade"],
  enun=p(T(178, 0)) + LISTA(T(178, 1).split(" O coeficiente")[0]) + p("O coeficiente" + T(178, 1).split(" O coeficiente")[1], T(178, 2)))
X(179, "Grandezas e medidas", "<p>Massa de uma folha: 75 g/m<sup>2</sup> · 0,062 m<sup>2</sup> = 4,65 g. Em 20 mil folhas: 20 000 · 4,65 = 93 000 g = <strong>93 kg</strong>. Alternativa <strong>E</strong>.</p><p>930 (C) erra a conversão de grama para quilograma.</p>",
  tags=["densidade superficial", "conversão de unidades"])
X(180, "Estatística", "<p>Pesos 3, 5 e 2 (soma 10). X: (15 + 5 + 4)/10 = 2,4; Y: (3 + 20 + 4)/10 = 2,7; Z: (12 + 15 + 4)/10 = <strong>3,1</strong>; W: (9 + 15 + 6)/10 = 3,0; T: (12 + 10 + 8)/10 = 3,0. A maior média é a da empresa <strong>Z</strong>. Alternativa <strong>C</strong>.</p><p>Pela média simples, W e T empatariam com Z ou ficariam na frente; o peso da clareza (5) decide.</p>",
  tags=["média ponderada"],
  enun=p(T(180, 0)) + tabela(["Procedimento", "Peso", "X", "Y", "Z", "W", "T"],
                             [["Rapidez no atendimento", "3", "5", "1", "4", "3", "4"], ["Clareza nas informações passadas aos clientes", "5", "1", "4", "3", "3", "2"], ["Cortesia no atendimento", "2", "2", "2", "2", "3", "4"]])
       + p(T(180, 2)))

completar(Q, R)
