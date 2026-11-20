# Enem 2014, 2º dia, caderno azul: Matemática (questões 136 a 180; no site, 1 a 45).
# Texto legível. Frações em KaTeX nas alternativas curtas; quadros em tabela HTML. Alternativas-imagem nas Q143, Q144 e Q160.
# Sem anuladas nesta área.

import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, paragrafos_enem

ID = "enem-2014-matematica"
META = {"id": ID, "banca": "Enem", "ano": 2014, "titulo": "Enem 2014: Matemática", "fonte": "Inep", "dataExame": "2014-11-09",
        "duracaoMinutos": 150, "area": "Matemática", "caderno": "azul", "dia": 2}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2014-dia2-azul")
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


X(136, "Porcentagem", "<p>Em dezembro de 2011, a taxa total foi de 9,0%, então a de dezembro de 2012 também será 9,0%. Em junho de 2012, a taxa de desemprego oculto foi de 2,2%; a metade é 1,1%. O desemprego aberto é o total menos o oculto: 9,0 − 1,1 = <strong>7,9%</strong>. Alternativa <strong>E</strong>.</p>",
  figs(("q136", "Gráfico de colunas empilhadas e linha. Colunas de janeiro a junho de 2012, desemprego aberto e oculto: jan. 7,6 e 2,0; fev. 8,4 e 2,0; mar. 9,1 e 2,0; abr. 9,1 e 2,1; maio 8,8 e 2,1; jun. 9,0 e 2,2. Linha do total de 2011, de janeiro a dezembro: 10,5; 10,6; 11,3; 11,2; 10,7; 11,0; 11,1; 11,2; 10,6; 9,9; 9,5; 9,0 (em %).")),
  ["leitura de gráfico", "taxas"], enun=p(T(136, 0)) + "[[fig:1]]" + p(T(136, 4)) + fonte(T(136, 5)) + p(T(136, 6)))
X(137, "Porcentagem", "<p>De 2000 a 2010, a taxa passou de 2,38 para 1,90: o fator de variação foi \\(\\dfrac{1{,}90}{2{,}38} \\approx 0{,}798\\), uma queda de cerca de 20%. Repetindo o mesmo fator: 1,90 × 0,798 ≈ <strong>1,52</strong>. Alternativa <strong>C</strong>.</p><p>Subtrair a mesma quantidade (0,48) daria 1,42 (B), mas o enunciado pede a mesma variação percentual.</p>",
  tags=["variação percentual", "fecundidade"],
  enun=p(T(137, 0)) + tabela(["Ano", "Taxa de fecundidade no Brasil"], [["2000", "2,38"], ["2010", "1,90"]]) + fonte(T(137, 2)) + p(T(137, 3)))
X(138, "Porcentagem", "<p>A campanha deve ser intensificada onde o percentual de doadores é menor ou igual ao do país, 1,9%. Isso acontece no Nordeste (1,5%), no Norte (1,5%) e no Sudeste (1,9%). Alternativa <strong>B</strong>.</p><p>O Centro-Oeste (2,6%) e o Sul (2,5%) estão acima da média nacional.</p>",
  tags=["leitura de tabela", "comparação"],
  enun=p(T(138, 0)) + tabela(["Região", "Doadores", "Número de habitantes", "Doadores/habitantes"],
    [["Nordeste", "820 959", "53 081 950", "1,5%"], ["Norte", "232 079", "15 864 454", "1,5%"], ["Sudeste", "1 521 766", "80 364 410", "1,9%"], ["Centro-Oeste", "362 334", "14 058 094", "2,6%"], ["Sul", "690 391", "27 386 891", "2,5%"], ["Total", "3 627 529", "190 755 799", "1,9%"]])
  + '<p class="apoio">Taxa de doação de sangue, por região, em 2010.</p>' + p(T(138, 4), T(138, 5)) + fonte(T(138, 6)) + p(T(138, 7)))
X(139, "Proporcionalidade", "<p>O custo depende do volume de material, que é altura × largura × espessura. A altura aumentou \\(\\tfrac{1}{8}\\), ou seja, passou a ser \\(\\tfrac{9}{8}\\) da anterior, e a espessura não mudou. Para o volume ficar igual, a largura deve ser multiplicada pelo inverso: \\(\\tfrac{8}{9}\\). Alternativa <strong>D</strong>.</p><p>A opção \\(\\tfrac{7}{8}\\) (B) seria uma redução de \\(\\tfrac{1}{8}\\) na largura, o que não compensa o aumento.</p>",
  tags=["grandezas inversamente proporcionais", "volume"],
  enun=p("Um carpinteiro fabrica portas retangulares maciças, feitas de um mesmo material. Por ter recebido de seus clientes pedidos de portas mais altas, aumentou sua altura em \\(\\tfrac{1}{8}\\), preservando suas espessuras. A fim de manter o custo com o material de cada porta, precisou reduzir a largura.", T(139, 2)),
  alts=FR("\\dfrac{1}{8}", "\\dfrac{7}{8}", "\\dfrac{8}{7}", "\\dfrac{8}{9}", "\\dfrac{9}{8}"))
X(140, "Porcentagem", "<p>Dos 200 L diários, 25% (50 L) vão para banho, mãos e dentes; 33% (66 L) para a descarga; 27% (54 L) para beber e cozinhar. Com o consumo sugerido, essas atividades gastariam 24 + 3,2 + 2,4 = 29,6 L; 18 L; e 22 L. A economia é (50 − 29,6) + (66 − 18) + (54 − 22) = 20,4 + 48 + 32 = <strong>100,4 L</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["porcentagem", "consumo de água"],
  enun=p("De acordo com a ONU, da água utilizada diariamente,") + LISTA(T(140, 0).split("diariamente,", 1)[1].split("No Brasil")[0]) + p("No Brasil" + T(140, 0).split("No Brasil", 1)[1], T(140, 1))
  + tabela(["Atividade", "Consumo total de água na atividade (em litros)"], [["Tomar banho", "24,0"], ["Dar descarga", "18,0"], ["Lavar as mãos", "3,2"], ["Escovar os dentes", "2,4"], ["Beber e cozinhar", "22,0"]]) + p(T(140, 4)))
X(141, "Estatística", "<p>Ordenando as notas e tirando a média dos dois valores centrais: K (33, 33, 33, 34) tem mediana 33; L (32, 33, 34, 39), 33,5; M (34, 35, 35, 36), 35; N (24, 35, 37, 40), 36; P (16, 26, 36, 41), 31. A maior mediana é a de <strong>N</strong>. Alternativa <strong>D</strong>.</p><p>Pela média, o maior seria M; a mediana despreza as notas extremas, como o 24 de N.</p>",
  tags=["mediana", "tabela"],
  enun=p(T(141, 0)) + tabela(["Candidatos", "Português", "Matemática", "Direito", "Informática"], [["K", "33", "33", "33", "34"], ["L", "32", "39", "33", "34"], ["M", "35", "35", "36", "34"], ["N", "24", "37", "40", "35"], ["P", "36", "16", "26", "41"]])
  + p("Segundo o edital de seleção, o candidato aprovado será aquele para o qual a mediana das notas obtidas por ele nas quatro disciplinas for a maior.", T(141, 3)))
X(142, "Geometria espacial", "<p>O silo tem 2 m de altura, então o topo é 2 × 0,5 = 1 m mais largo que o fundo: o fundo mede 5 m. A área do trapézio é \\(\\dfrac{(6 + 5) \\cdot 2}{2} = 11\\) m², e o volume é 11 × 20 = 220 m³. Como cada tonelada ocupa 2 m³, cabem 220 ÷ 2 = <strong>110 toneladas</strong>. Alternativa <strong>A</strong>.</p><p>A opção D (220) esquece de dividir o volume por 2.</p>",
  figs(("q142", "Silo horizontal em forma de prisma reto de base trapezoidal, com a legenda: b, largura do fundo; B, largura do topo; C, comprimento do silo; h, altura do silo.")),
  ["prisma", "volume"], enun=p(T(142, 0)) + "[[fig:1]]" + p(T(142, 4).replace("2 m3", "2 m<sup>3</sup>")) + fonte(T(142, 5)) + p(T(142, 6)))
X(143, "Funções", "<p>Com vazão constante, a altura sobe mais rápido onde a escultura é estreita. Na parte de baixo, o tronco de cone se estreita para cima, e a altura sobe cada vez mais rápido; no cilindro do meio, sobe em ritmo constante (trecho reto); na parte de cima, o tronco se alarga, e a altura sobe cada vez mais devagar. O gráfico começa curvado para cima, tem um trecho reto e termina curvado para baixo: é o <strong>gráfico D</strong>. Alternativa <strong>D</strong>.</p>",
  figs(("q143", "Vista frontal da escultura: um tronco de cone na base, estreitando para cima; um cilindro estreito no meio; e um tronco de cone invertido no topo, alargando para cima, formando uma ampulheta."),
       ("q143a", "Alternativa A: a altura h cresce em linha reta com o tempo t."),
       ("q143b", "Alternativa B: h cresce rápido no começo, desacelera no meio e acelera no fim."),
       ("q143c", "Alternativa C: h cresce cada vez mais rápido, numa curva voltada para cima."),
       ("q143d", "Alternativa D: h começa crescendo devagar e acelerando, segue um trecho reto e termina desacelerando."),
       ("q143e", "Alternativa E: h cresce rápido e desacelera, tem um trecho reto e depois volta a crescer rápido e desacelerar.")),
  ["taxa de variação", "gráficos"], enun=p(T(143, 0)) + "[[fig:1]]" + p(T(143, 2), T(143, 3).replace(" é h", " é")), alts=ALT(2))
X(144, "Geometria espacial", "<p>A superfície lateral de um cone, planificada, é um setor circular. Do cone tira-se a parte de cima (outro cone menor), então o adesivo, que vai da base até a metade da altura, é a superfície lateral de um tronco de cone: um setor circular sem a ponta, limitado por dois arcos. Essa é a <strong>figura E</strong>. Alternativa <strong>E</strong>.</p><p>O trapézio (B) teria lados retos em cima e embaixo, e as bordas do adesivo são circunferências.</p>",
  figs(("q144a", "Alternativa A: triângulo."), ("q144b", "Alternativa B: trapézio."), ("q144c", "Alternativa C: figura com topo reto e base em arco."),
       ("q144d", "Alternativa D: setor circular, com vértice em ponta e base em arco."), ("q144e", "Alternativa E: setor de coroa circular, limitado por dois arcos concêntricos.")),
  ["tronco de cone", "planificação"], enun=p(T(144, 0), T(144, 1)), alts=ALT(1))
X(145, "Funções", "<p>Como f(0) = 0, a função é f(x) = ax² + bx. Com f(10) = 10: 100a + 10b = 10. Com f(5) = 6: 25a + 5b = 6, ou 50a + 10b = 12. Subtraindo: 50a = −2, então \\(a = -\\tfrac{1}{25}\\), e \\(b = \\tfrac{6 + 1}{5} = \\tfrac{7}{5}\\). A função é \\(y = -\\tfrac{1}{25}x^2 + \\tfrac{7}{5}x\\). Alternativa <strong>A</strong>.</p>",
  tags=["função quadrática", "sistema linear"],
  enun=p(T(145, 0)) + "<ul><li>A nota zero permanece zero.</li><li>A nota 10 permanece 10.</li><li>A nota 5 passa a ser 6.</li></ul>" + p("A expressão da função <em>y</em> = <em>f</em>(<em>x</em>) a ser utilizada pelo professor é"),
  alts=FR("y = -\\dfrac{1}{25}x^2 + \\dfrac{7}{5}x", "y = -\\dfrac{1}{10}x^2 + 2x", "y = \\dfrac{1}{24}x^2 + \\dfrac{7}{12}x", "y = \\dfrac{4}{5}x + 2", "y = x"))
X(146, "Aritmética", "<p>Se N é múltiplo de 10, tem os fatores 2 e 5 (x ≥ 1 e y ≥ 1); se não é múltiplo de 7, z = 0. O número de divisores de 2<sup>x</sup> · 5<sup>y</sup> é (x + 1)(y + 1); tirando o próprio N, sobram (x + 1)(y + 1) − 1. Como z = 0, isso é igual a <strong>(x + 1) · (y + 1) · (z + 1) − 1</strong>. Alternativa <strong>E</strong>.</p><p>A opção B conta também o próprio N.</p>",
  tags=["número de divisores", "fatoração"],
  enun=p("Durante a Segunda Guerra Mundial, para decifrarem as mensagens secretas, foi utilizada a técnica de decomposição em fatores primos. Um número <em>N</em> é dado pela expressão 2<sup><em>x</em></sup> ⋅ 5<sup><em>y</em></sup> ⋅ 7<sup><em>z</em></sup>, na qual <em>x</em>, <em>y</em> e <em>z</em> são números inteiros não negativos. Sabe-se que <em>N</em> é múltiplo de 10 e não é múltiplo de 7.", T(146, 1)))
X(147, "Geometria plana", "<p>Um lado tem 6 palitos, então os outros dois somam 11. Pela desigualdade triangular, cada lado deve ser menor que a metade do perímetro (8,5), ou seja, no máximo 8; então o menor é pelo menos 3. As possibilidades são (6, 3, 8), (6, 4, 7) e (6, 5, 6): <strong>3 triângulos</strong>. Alternativa <strong>A</strong>.</p>",
  figs(("q147", "Triângulo formado por palitos de fósforo enfileirados nos três lados.")),
  ["desigualdade triangular", "contagem"], enun=p(T(147, 0)) + "[[fig:1]]" + p(T(147, 2)))
X(148, "Geometria analítica", "<p>O assento descreve um arco de circunferência com centro no topo do suporte (a origem) e raio igual à corda, 2 m: x² + y² = 4. Como o assento fica abaixo do topo, y é negativo: \\(y = -\\sqrt{4 - x^2}\\). Alternativa <strong>D</strong>.</p><p>Em A e B o raio seria \\(\\sqrt{2}\\), e em E a curva ficaria acima do suporte.</p>",
  figs(("q148", "Criança num balanço: a corda de 2 metros vai do topo do suporte ao assento; uma linha tracejada mostra o arco percorrido pelo assento abaixo do topo; embaixo, o chão do parque.")),
  ["circunferência", "função"], enun=p(T(148, 0)) + "[[fig:1]]" + p(T(148, 3).replace("eixo X", "eixo <em>X</em>").replace("eixo Y", "eixo <em>Y</em>"), T(148, 4)),
  alts=FR("f(x) = -\\sqrt{2 - x^2}", "f(x) = \\sqrt{2 - x^2}", "f(x) = x^2 - 2", "f(x) = -\\sqrt{4 - x^2}", "f(x) = \\sqrt{4 - x^2}"))
X(149, "Proporcionalidade", "<p>São 5 × 4 = 20 catracas, e cada uma recebe 45 000 ÷ 20 = 2 250 pessoas. A 2 segundos por pessoa, isso leva 4 500 s = 75 minutos = <strong>1 hora e 15 minutos</strong>. Alternativa <strong>B</strong>.</p>",
  tags=["divisão", "unidades de tempo"])
X(150, "Geometria espacial", "<p>Pela planificação, a caixa tem uma dimensão de 24 cm e a altura de 90 cm corresponde à face central mais duas faces de 24 cm: a outra dimensão é 90 − 2 × 24 = 42 cm. A soma das três dimensões não pode passar de 115: 24 + 42 + x ≤ 115, então x ≤ <strong>49</strong>. Alternativa <strong>E</strong>.</p>",
  figs(("q150", "Planificação de uma caixa em forma de paralelepípedo: uma faixa horizontal de quatro faces, a última com 24 cm de largura e uma delas com largura x; acima e abaixo de uma das faces, duas abas; a altura total da planificação é de 90 cm.")),
  ["planificação", "paralelepípedo"], enun=p(T(150, 0), T(150, 1)) + "[[fig:1]]" + p(T(150, 4)))
X(151, "Geometria espacial", "<p>As dimensões da base aumentam 25%, então a área da base é multiplicada por 1,25² = 1,5625. Para o volume não mudar, a altura deve ser dividida por 1,5625, isto é, multiplicada por 0,64: uma redução de <strong>36%</strong>. Alternativa <strong>D</strong>.</p><p>Uma redução de 20% (B) só compensaria o aumento de uma das dimensões.</p>",
  figs(("q151", "Lata em forma de paralelepípedo com tampa circular, base de 24 cm por 24 cm e altura de 40 cm.")),
  ["volume", "porcentagem"], enun=p(T(151, 0)) + "[[fig:1]]" + p(T(151, 2), T(151, 3)))
X(152, "Porcentagem", "<p>Se só 36% é tratado, os 8 bilhões de litros sem tratamento são 64% do total, que é 8 ÷ 0,64 = 12,5 bilhões de litros. Com a meta, 4 bilhões continuam sem tratamento, que são 4 ÷ 12,5 = 32% do total. O tratado passa a ser 100% − 32% = <strong>68%</strong>. Alternativa <strong>B</strong>.</p><p>Dobrar o percentual (72%, A) não tem relação com reduzir pela metade o volume não tratado.</p>",
  tags=["porcentagem", "regra de três"])
X(153, "Estatística", "<p>Pelo gráfico 1, a folha de R$ 400 000 se divide em 12,5% para o ensino fundamental (R$ 50 000), 75% para o médio (R$ 300 000) e 12,5% para o superior (R$ 50 000). Com 50, 150 e 10 funcionários em 2013, os salários são R$ 1 000, R$ 2 000 e R$ 5 000. Em 2014 serão 70, 180 e 20: o aumento da folha é 20 × 1 000 + 30 × 2 000 + 10 × 5 000 = <strong>R$ 130 000</strong>, que a receita precisa crescer para manter o lucro. Alternativa <strong>B</strong>.</p>",
  figs(("q153", "Gráfico 1, de setores, “Distribuição da folha salarial”: ensino fundamental 12,5%, ensino médio 75% e ensino superior 12,5%. Gráfico 2, de colunas, “Número de funcionários por grau de instrução”: ensino fundamental, 50 em 2013 e 70 em 2014; ensino médio, 150 em 2013 e 180 em 2014; ensino superior, 10 em 2013 e 20 em 2014.")),
  ["gráficos", "média salarial"], enun=p(T(153, 0)) + "[[fig:1]]" + p(T(153, 6)))
X(154, "Razão e proporção", "<p>O desempenho é a razão entre os <em>strikes</em> e as jogadas: I, 50/85 ≈ 0,59; II, 40/65 ≈ 0,62; III, 20/65 ≈ 0,31; IV, 30/40 = 0,75; V, 48/90 ≈ 0,53. O maior é o do <strong>jogador IV</strong>. Alternativa <strong>D</strong>.</p><p>O jogador I tem mais acertos absolutos, mas também mais jogadas.</p>",
  tags=["razão", "comparação de frações"],
  enun=p(T(154, 0), T(154, 1)) + "<ul>" + "".join(f"<li>{T(154, i)} {T(154, i + 1)}</li>" for i in (2, 4, 6, 8, 10)) + "</ul>" + p(T(154, 12)))
X(155, "Estatística", "<p>As médias ponderadas são: I, \\(\\dfrac{4 \\cdot 20 + 6 \\cdot 23}{10} = 21{,}8\\); III, \\(\\dfrac{4 \\cdot 21 + 6 \\cdot 18}{10} = 19{,}2\\). Para vencer, II precisa de \\(\\dfrac{4X + 6 \\cdot 25}{10} > 21{,}8\\), ou 4X > 68, X > 17. Como as notas são inteiras, a menor é <strong>18</strong>. Alternativa <strong>A</strong>.</p>",
  tags=["média ponderada", "inequação"],
  enun=p(T(155, 0), T(155, 1)) + tabela(["Candidato", "Química", "Física"], [["I", "20", "23"], ["II", "X", "25"], ["III", "21", "18"]]) + p(T(155, 3)))
X(156, "Escalas", "<p>Na escala 1 : 100, cada centímetro do projeto vale 100 cm. As dimensões reais são 300 cm, 100 cm e 200 cm, e o volume é 300 × 100 × 200 = <strong>6 000 000 cm³</strong>. Alternativa <strong>E</strong>.</p><p>Multiplicar o volume do projeto (6 cm³) só por 100 ou 1 000 (B e C) esquece que a escala se aplica a cada uma das três dimensões: o fator do volume é 100³.</p>",
  tags=["escala", "volume"])
X(157, "Estatística", "<p>A numeração com mais reclamações é a moda, <strong>38</strong>. Para a cor, a média dos zeros (branco) e uns (preto) é 0,45: 45% dos sapatos com defeito eram pretos e 55% eram brancos, então a cor com mais reclamações é a <strong>branca</strong>. Alternativa <strong>A</strong>.</p><p>A mediana (37) e a média (36) não indicam a numeração mais frequente.</p>",
  tags=["moda", "média"],
  enun=p(T(157, 0), T(157, 1)) + tabela(["Estatísticas sobre as numerações dos sapatos com defeito", "Média", "Mediana", "Moda"], [["Numerações dos sapatos com defeito", "36", "37", "38"]]) + p(T(157, 4), T(157, 5), T(157, 6)))
X(158, "Probabilidade", "<p>A sensibilidade é a probabilidade de o teste dar positivo entre os que têm a doença. Dos 95 + 5 = 100 doentes, 95 tiveram resultado positivo: \\(\\dfrac{95}{100} = \\) <strong>95%</strong>. Alternativa <strong>E</strong>.</p><p>A opção A (47,5%) divide 95 pelos 200 indivíduos, mas a condição é estar doente.</p>",
  tags=["probabilidade condicional", "tabela"],
  enun=p(*PP(158)[:-1]) + tabela(["Resultado do teste", "Doença A presente", "Doença A ausente"], [["Positivo", "95", "15"], ["Negativo", "5", "85"]]) + fonte(T(158, 9)) + p(PP(158)[-1]))
X(159, "Geometria plana", "<p>Descontando 3 m de cada lateral, sobra uma área útil de 8 m por 5,5 m para as covas. Nas filas paralelas ao lado maior, com covas a cada 3 m, cabem 3 mudas (em 0, 3 e 6 m). Se as filas forem intercaladas, com as mudas formando triângulos equiláteros de lado 3 m, a distância entre filas é \\(\\dfrac{3\\sqrt{3}}{2} \\approx 2{,}6\\) m, e cabem 3 filas em 5,5 m (em 0; 2,6 e 5,2 m). As filas deslocadas ficam em 1,5; 4,5 e 7,5 m, ainda dentro dos 8 m. Total: 3 × 3 = <strong>9 mudas</strong>. Alternativa <strong>C</strong>.</p><p>Com as covas em grade quadrada, caberiam só 2 filas de 3, ou 6 mudas, valor que não está entre as opções.</p>",
  tags=["otimização", "triângulo equilátero"])
X(160, "Geometria espacial", "<p>Os pontos A, B, C, D e E estão igualmente espaçados e E fica exatamente acima de A: de A a E o corrimão dá uma volta completa, dividida em 4 partes iguais. De A a D a mão percorre 3 dessas partes, ou seja, 3/4 de volta. Projetado no piso, o caminho é um arco de 3/4 de circunferência, como na <strong>figura C</strong>. Alternativa <strong>C</strong>.</p><p>A figura A é 1/4 de volta, a B é meia volta e a E passa de uma volta.</p>",
  figs(("q160", "Escada caracol em perspectiva, com o corrimão em espiral e os pontos A, B, C, D e E marcados nele; E fica acima de A, e P está no piso, alinhado com A e E."),
       ("q160a", "Alternativa A: arco de um quarto de circunferência."), ("q160b", "Alternativa B: arco de meia circunferência."),
       ("q160c", "Alternativa C: arco de três quartos de circunferência."), ("q160d", "Alternativa D: arco em espiral de pouco mais de meia volta."),
       ("q160e", "Alternativa E: curva que dá mais de uma volta e se cruza.")),
  ["projeção ortogonal", "hélice"], enun=p(T(160, 0)) + "[[fig:1]]" + p(T(160, 4)), alts=ALT(2))
X(161, "Estatística", "<p>Calculando a média de cada reagente e contando os resultados acima dela: reagente 1 (1, 6, 6, 6, 11), média 6, só 1 acima; reagente 2 (0, 6, 7, 6, 5), média 4,8, <strong>4 acima</strong>; reagente 3 (2, 3, 8, 10, 11), média 6,8, 3 acima; reagente 4 (2, 4, 7, 8, 12), média 6,6, 3 acima; reagente 5 (1, 2, 9, 10, 11), média 6,6, 3 acima. O melhor é o <strong>reagente 2</strong>. Alternativa <strong>B</strong>.</p>",
  tags=["média aritmética", "tabela"],
  enun=p(T(161, 0)) + tabela(["", "Reagente 1", "Reagente 2", "Reagente 3", "Reagente 4", "Reagente 5"],
    [["Experimento 1", "1", "0", "2", "2", "1"], ["Experimento 2", "6", "6", "3", "4", "2"], ["Experimento 3", "6", "7", "8", "7", "9"], ["Experimento 4", "6", "6", "10", "8", "10"], ["Experimento 5", "11", "5", "11", "12", "11"]]) + p(T(161, 2)))
X(162, "Funções", "<p>Hoje a conta é 150 × 0,50 + 4,50 = R$ 79,50. Reduzir pelo menos 10% significa pagar no máximo 0,9 × 79,50 = R$ 71,55. Se o consumo cair para a faixa de 100 a 140 kWh, a Cosip é R$ 3,00: 0,50c + 3 ≤ 71,55, então c ≤ <strong>137,1 kWh</strong>, que está na faixa. Alternativa <strong>C</strong>.</p><p>Mantendo a Cosip de R$ 4,50 (faixa acima de 140), o consumo teria de ser 134,1 (A), que não pertence a essa faixa.</p>",
  tags=["função afim por partes", "porcentagem"],
  enun=p(T(162, 0)) + p("<em>Valor do kWh (com tributos) × consumo (em kWh) + Cosip</em>") + p(T(162, 2))
  + tabela(["Faixa de consumo mensal (kWh)", "Valor da Cosip (R$)"], [["Até 80", "0,00"], ["Superior a 80 até 100", "2,00"], ["Superior a 100 até 140", "3,00"], ["Superior a 140 até 200", "4,50"]]) + p(T(162, 4), T(162, 5)))
X(163, "Análise combinatória", "<p>A estratégia fica definida pela ordem em que cada filme é visto. Os 8 filmes de ação podem ser vistos em 8! ordens; os 5 de comédia, em 5! ordens (eles formam par com os 5 primeiros de ação); e os 3 de drama, em 3! ordens (com os 3 últimos de ação). Pelo princípio multiplicativo: <strong>8! × 5! × 3!</strong>. Alternativa <strong>B</strong>.</p><p>Não há divisão por 2: em cada aluguel os dois filmes são de tipos diferentes, então não há pares repetidos a descontar.</p>",
  tags=["princípio multiplicativo", "permutação"],
  alts=FR("20 \\times 8! + (3!)^2", "8! \\times 5! \\times 3!", "\\dfrac{8! \\times 5! \\times 3!}{2^8}", "\\dfrac{8! \\times 5! \\times 3!}{2^2}", "\\dfrac{16!}{2^8}"))
X(164, "Probabilidade", "<p>O teste termina na 5ª pergunta se o candidato errar exatamente uma das 4 primeiras e errar a 5ª. A probabilidade é \\(4 \\cdot 0{,}2 \\cdot 0{,}8^3 \\cdot 0{,}2 = 4 \\cdot 0{,}04 \\cdot 0{,}512 = 0{,}08192\\). O fator 4 conta em qual das quatro primeiras está o primeiro erro. Alternativa <strong>B</strong>.</p><p>Sem esse fator, o resultado seria 0,02048 (A).</p>",
  tags=["probabilidade binomial", "eventos independentes"])
X(165, "Grandezas e medidas", "<p>O tempo mínimo é 1 min 24 s = 84 s, e a distância é 2,1 km = 2 100 m. A velocidade média máxima é 2 100 ÷ 84 = 25 m/s; multiplicando por 3,6: <strong>90 km/h</strong>. Alternativa <strong>C</strong>.</p><p>A opção A (25) é o valor em m/s, mas as placas usam km/h.</p>",
  figs(("q165", "Ilustração de dois radares instalados em postes, cada um sobre uma faixa de uma avenida, com dois carros passando. Texto: “O sistema mede o tempo decorrido entre um radar e outro e calcula a velocidade média. No teste feito pela CET, os dois radares ficavam a uma distância de 2,1 km um do outro.”")),
  ["velocidade média", "conversão de unidades"], enun=p(T(165, 0)) + "[[fig:1]]" + p(T(165, 2), T(165, 3)) + fonte(T(165, 4)) + p(T(165, 5)),
  alts={"A": "25 km/h", "B": "69 km/h", "C": "90 km/h", "D": "102 km/h", "E": "110 km/h"})
X(166, "Funções", "<p>Para gastar R$ 30,00, o melhor plano é o que permite mais minutos com esse valor: a reta que cruza o nível de R$ 30 mais à direita. O plano B custa cerca de R$ 49 fixos e o D já começa em R$ 30. A reta A chega a R$ 30 por volta de 20 minutos; a E, perto de 23; a C, perto de 30 minutos. O mais vantajoso é o <strong>plano C</strong>. Alternativa <strong>C</strong>.</p>",
  figs(("q166", "Gráfico do valor mensal (em reais) em função do tempo mensal (em minutos), de 0 a 60 minutos, para cinco planos. A: começa em cerca de 23 reais e chega a cerca de 43. B: reta horizontal em cerca de 49 reais. C: começa em cerca de 5 reais e chega a cerca de 56. D: começa em 30 reais e chega a cerca de 62. E: começa em 0 e chega a cerca de 78.")),
  ["função afim", "leitura de gráfico"], enun=p(T(166, 0), T(166, 1)) + "[[fig:1]]" + p(T(166, 5), T(166, 6)))
X(167, "Geometria espacial", "<p>A pílula é um cilindro de 10 mm mais duas semiesferas, que juntas formam uma esfera: V = πr² · 10 + \\(\\tfrac{4}{3}\\)πr³. Com π = 3: para r = 5, V = 3 · 25 · 10 + 4 · 125 = 750 + 500 = 1 250 mm³; para r = 4, V = 3 · 16 · 10 + 4 · 64 = 480 + 256 = 736 mm³. A redução é 1 250 − 736 = <strong>514 mm³</strong>. Alternativa <strong>E</strong>.</p>",
  tags=["cilindro", "esfera"], enun=p(*PP(167)[:2], "Use 3 como valor aproximado para π.", PP(167)[3]))
X(168, "Porcentagem", "<p>A área usada na agricultura é de 80 milhões de hectares, e o território tem 853 milhões. A razão é 80 ÷ 853 ≈ 0,094, ou <strong>9,4%</strong>. Alternativa <strong>D</strong>.</p><p>Os 280 milhões (32,8%, A) incluem as pastagens.</p>",
  tags=["porcentagem", "leitura de texto"], enun=p(PP(168)[0]) + fonte(T(168, 1).replace("Folha de S. Paulo", "<em>Folha de S. Paulo</em>")) + p(PP(168)[1]))
X(169, "Escalas", "<p>A região disponível mede 42 − 6 = 36 cm por 30 − 6 = 24 cm. A gravura tem proporção 8 : 6 = 4 : 3. Se ocupar toda a altura de 24 cm, o comprimento será 32 cm, que cabe nos 36 cm. Então 6 m = 600 cm viram 24 cm: a escala é 24 : 600 = <strong>1 : 25</strong>. Alternativa <strong>D</strong>.</p><p>Usar os 36 cm de comprimento daria 27 cm de altura, que não cabe nos 24 cm disponíveis.</p>",
  figs(("q169a", "Figura 1: gravura retangular de 8 metros de comprimento por 6 metros de altura, com um desenho pixelado de um monstrinho preto."),
       ("q169b", "Figura 2: folha de papel de 42 cm por 30 cm com margens de 3 cm em cada lado; a região central é a disponível para reproduzir a gravura, e as margens são a região proibida.")),
  ["escala", "proporcionalidade"], enun=p(T(169, 0)) + "[[fig:1]]" + p(T(169, 4)) + "[[fig:2]]" + p(T(169, 9)) + fonte(T(169, 10).replace("Superinteressante", "<em>Superinteressante</em>")) + p(T(169, 11)))
X(170, "Geometria plana", "<p>Cada volta da folha em torno do cilindro usa um comprimento igual à circunferência, πd. Com 5 voltas, o lado da folha mede <strong>5πd</strong>. Alternativa <strong>D</strong>.</p><p>A espessura do papel é desprezível, então todas as voltas têm o mesmo comprimento.</p>",
  figs(("q170", "Diploma enrolado em forma de canudo, amarrado no meio com um cordão.")),
  ["comprimento da circunferência", "cilindro"], enun=p(T(170, 0).replace("diâmetro d em", "diâmetro <em>d</em> em")) + "[[fig:1]]" + p(T(170, 2), T(170, 3)),
  alts=FR("\\pi d", "2\\pi d", "4\\pi d", "5\\pi d", "10\\pi d"))
X(171, "Porcentagem", "<p>O ponto central recebe 60% de 12 t = 7,2 t. Os outros 40% (4,8 t) se dividem igualmente: 2,4 t para cada extremidade. As cargas são <strong>2,4 t; 7,2 t; 2,4 t</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["porcentagem", "divisão"])
X(172, "Aritmética", "<p>Na Figura 2, a corda pendente tem 3 nós na posição dos milhares, nenhum nas centenas, 6 nas dezenas e 4 nas unidades. Como a ausência de nós representa o zero, o número é <strong>3 064</strong>. Alternativa <strong>C</strong>.</p><p>A opção 364 (A) ignora o zero das centenas.</p>",
  figs(("q172", "Quipus: uma corda principal horizontal com cordas pendentes. Na Figura 1, a corda pendente tem nós agrupados nas posições de milhares (2), centenas (4), dezenas (5) e unidades (3). Na Figura 2, a corda tem 3 nós nos milhares, nenhum nas centenas, 6 nas dezenas e 4 nas unidades.")),
  ["sistema de numeração posicional", "zero"], enun=p(T(172, 0).replace("denominado quipus", "denominado <em>quipus</em>").replace("O quipus", "O <em>quipus</em>").replace("Figura 1, o quipus", "Figura 1, o <em>quipus</em>")) + "[[fig:1]]" + fonte("Disponível em: www.culturaperuana.com.br. Acesso em: 13 dez. 2012.") + p(T(172, 4).replace("do quipus", "do <em>quipus</em>")))
X(173, "Grandezas e medidas", "<p>1 hectômetro = 100 m, então 1 hm² = 100 × 100 = 10 000 m². Os 8 hectares valem 8 × 10 000 = <strong>80 000 m²</strong>. Alternativa <strong>E</strong>.</p><p>Converter como se fosse medida linear (× 100) daria 800 (C).</p>",
  tags=["unidades de área", "conversão"])
X(174, "Aritmética", "<p>São 16 × 4 = 64 L de gel para 10 escolas: 6,4 L por escola. Divididos em 20 recipientes iguais, cada um deve ter 6,4 ÷ 20 = 0,32 L, o <strong>recipiente III</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["divisão", "decimais"], enun=p(T(174, 0)) + LISTA(T(174, 1)) + p(T(174, 2), T(174, 3)))
X(175, "Porcentagem", "<p>A luz que passa pelo vidro e pela película é o produto das transparências. O menor valor é 0,70 × 0,50 = 0,35, e o maior é 0,90 × 0,70 = 0,63. P varia em <strong>[35 ; 63]</strong>. Alternativa <strong>A</strong>.</p><p>As porcentagens se multiplicam, não se somam nem se mantêm, porque a película atua sobre a luz que já passou pelo vidro.</p>",
  tags=["porcentagens sucessivas", "intervalos"], enun=p(T(175, 0).replace("porcentagem P da", "porcentagem <em>P</em> da"), T(175, 1).replace("possível de P é", "possível de <em>P</em> é")))
X(176, "Estatística", "<p>Somando as duas espécies em cada dia: segunda, 350 + 1 250 = 1 600; terça, 800 + 1 100 = 1 900; quarta, 1 450 + 300 = 1 750; quinta, 650 + 850 = 1 500; sexta, 300 + 1 400 = 1 700; sábado, 290 + 1 000 = 1 290; domingo, 0 + 1 350 = 1 350. O máximo foi na <strong>terça-feira</strong>. Alternativa <strong>A</strong>.</p><p>Na quarta (B), a espécie I atinge seu máximo, mas a II está no mínimo.</p>",
  figs(("q176", "Gráfico de linhas “Bactérias das espécies I e II”, quantidade por dia. Espécie I: seg. 350, ter. 800, qua. 1 450, qui. 650, sex. 300, sáb. 300, dom. 0. Espécie II: seg. 1 250, ter. 1 100, qua. 300, qui. 850, sex. 1 400, sáb. 1 000, dom. 1 350.")),
  ["leitura de gráfico", "soma"], enun=p(T(176, 0)) + "[[fig:1]]" + p(T(176, 6)))
X(177, "Geometria espacial", "<p>Se a aresta de cima é a, a de baixo é 2a: os volumes são a³ e 8a³. Metade da parte de baixo, 4a³, encheu em 8 minutos: 2 minutos por a³. Falta encher 4a³ (a outra metade de baixo) + a³ (a parte de cima) = 5a³, o que leva 5 × 2 = <strong>10 minutos</strong>. Alternativa <strong>B</strong>.</p><p>Achar que dobrar a aresta dobra o volume levaria a uma resposta errada: o volume é multiplicado por 2³ = 8.</p>",
  figs(("q177", "Depósito formado por dois cubos: um cubo menor apoiado sobre um cubo maior, ligados por uma abertura; o cubo de baixo está cheio de leite até a metade.")),
  ["volume do cubo", "razão de semelhança"], enun=p(T(177, 0)) + "[[fig:1]]" + p(T(177, 2)))
X(178, "Geometria plana", "<p>A diagonal de uma célula de 6 cm × 8 cm é \\(\\sqrt{36 + 64} = 10\\) cm, então cada célula produz 24 × 10 = 240 Wh por dia. Para produzir 20 160 Wh são necessárias 20 160 ÷ 240 = 84 células. Como há 100, o proprietário deve <strong>retirar 16 células</strong>. Alternativa <strong>A</strong>.</p>",
  tags=["teorema de Pitágoras", "proporcionalidade"])
X(179, "Equações", "<p>Seja n a quantidade habitual. O dinheiro levado é 10n + 6. Com o aumento de 20%, o preço passa a R$ 12,00, e esse dinheiro compra exatamente n − 2 unidades: 10n + 6 = 12(n − 2), então 2n = 30 e n = 15. A pessoa levava 10 × 15 + 6 = <strong>R$ 156,00</strong>. Alternativa <strong>B</strong>.</p>",
  tags=["equação do 1º grau", "porcentagem"])
X(180, "Grandezas e medidas", "<p>O voo de A para B dura 6 horas, sai às 15h de A e chega às 18h de B. Se fosse no horário de A, chegaria às 21h: B está 3 horas atrás de A. Para chegar a A às 13h, o executivo deve sair de B às 13h − 6h = 7h no horário de A, que corresponde a <strong>4h</strong> no horário de B. Alternativa <strong>D</strong>.</p><p>A opção 7h (C) é o horário de saída no fuso de A.</p>",
  tags=["fusos horários", "tempo"])

completar(Q, R)
