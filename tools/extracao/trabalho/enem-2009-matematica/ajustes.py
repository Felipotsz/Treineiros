# Enem 2009, 2º dia (06/12/2009), caderno azul: Matemática (questões 136 a 180; no site, 1 a 45).
# Texto legível; tabelas das Q148, Q150, Q159, Q167, Q168 e Q172 em HTML; fórmulas em KaTeX. Alternativas-imagem na Q149 (anéis de Borromeo).
# Sem anuladas nesta área.

import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, paragrafos_enem

ID = "enem-2009-matematica"
META = {"id": ID, "banca": "Enem", "ano": 2009, "titulo": "Enem 2009: Matemática", "fonte": "Inep", "dataExame": "2009-12-06",
        "duracaoMinutos": 150, "area": "Matemática", "caderno": "azul", "dia": 2}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2009-dia2-azul")
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

SUP = lambda s: re.sub(r"\b(m|cm|km)([23])\b", lambda m: f"{m.group(1)}<sup>{m.group(2)}</sup>", s)
SUPD = lambda d: {k: SUP(v) for k, v in d.items()}
CORTA = lambda n, l="E": {**D[n]["alternativas"], l: re.split(r"\s+Textos? para as questões", D[n]["alternativas"][l])[0]}
POP = (ap("A população mundial está ficando mais velha, os índices de natalidade diminuíram e a expectativa de vida aumentou. No gráfico seguinte, são apresentados dados obtidos por pesquisa realizada pela Organização das Nações Unidas (ONU), a respeito da quantidade de pessoas com 60 anos ou mais em todo o mundo. Os números da coluna da direita representam as faixas percentuais. Por exemplo, em 1950 havia 95 milhões de pessoas com 60 anos ou mais nos países desenvolvidos, número entre 10% e 15% da população total nos países desenvolvidos.")
       + "[[fig:1]]" + fonte("Disponível em: www.economist.com. Acesso em: 9 jul. 2009 (adaptado)."))
F_POP = figs(("q138", "Gráfico de 1950 a 2050 (com estimativas a partir de 2010) da população com 60 anos ou mais, em milhões, e da faixa percentual da população total (eixo da direita, de 0 a 35%). Países desenvolvidos: 95 milhões em 1950, 269 em 2010 e 461 em 2050, chegando perto de 32% da população. Países em desenvolvimento: 110 milhões em 1950, 490 em 2010 e 1.592 em 2050, chegando a cerca de 20%."))

X(136, "Razão e proporção", "<p>O índice é passageiros por veículo, e a frota é a mesma em abril de 2001 e outubro de 2008. Então o total de passageiros é proporcional ao índice: em abril de 2001 o índice era 400 e foram 321,9 milhões de passageiros; em outubro de 2008 o índice é 441. Total: 321,9 × 441 ÷ 400 ≈ <strong>355 milhões</strong>. Alternativa <strong>A</strong>.</p>",
  figs(("q136", "Gráfico “Capitais brasileiras – Sistema de Ônibus Urbano: passageiros transportados por veículo/dia, 1995 a 2008”, em linha, de out/95 a out/08: começa em 631, cai para cerca de 500 em 1998 e oscila entre 391 e 463 depois de 2000; em abr/01 marca 400 e em out/08, 441.")),
  ["proporcionalidade", "leitura de gráfico"], enun=p(T(136, 0)) + "[[fig:1]]" + fonte(T(136, 2)) + p(T(136, 3)))
X(137, "Grandezas e medidas", "<p>Seguindo as mãos de tráfego, o caminho mais curto de X a Y percorre 5 lados de quadra: 5 × 200 m = 1 km. A 40 km/h, o tempo é 1/40 h = 60/40 min = <strong>1,5 min</strong>. Alternativa <strong>D</strong>.</p>",
  figs(("q137", "Mapa de um bairro em grade, com quarteirões quadrados e setas indicando o sentido das ruas. O ponto X fica numa rua do lado esquerdo e o ponto Y numa rua mais acima e à direita.")),
  ["velocidade", "trajeto"], enun=p(T(137, 0)) + "[[fig:1]]", alts=CORTA(137, "C"))
X(138, "Função exponencial", "<p>2030 corresponde a x = 30: y = 363 · e<sup>0,9</sup> = 363 · (e<sup>0,3</sup>)<sup>3</sup> = 363 · 1,35<sup>3</sup> ≈ 363 · 2,46 ≈ 893 milhões, entre 870 e 910 milhões. Alternativa <strong>E</strong>.</p>",
  F_POP, ["função exponencial", "potências"],
  enun=POP + p(T(138, 0).replace("y = 363e0,03x", K("y = 363e^{0{,}03x}")).replace("e0,3 = 1,35", K("e^{0{,}3} = 1{,}35"))))
X(139, "Probabilidade", "<p>Pelo gráfico, em 2050 cerca de 32% da população dos países desenvolvidos terá 60 anos ou mais. A probabilidade é próxima de 0,32 = " + K("\\tfrac{8}{25}") + ". Alternativa <strong>C</strong>.</p><p>A faixa percentual é lida no eixo da direita.</p>",
  F_POP, ["probabilidade", "leitura de gráfico"], enun=POP + p(T(139, 0)), alts=FR("\\dfrac{1}{2}", "\\dfrac{7}{20}", "\\dfrac{8}{25}", "\\dfrac{1}{5}", "\\dfrac{3}{25}"))
X(140, "Áreas", "<p>Com AB = a, BC = 2a: o terreno tem 2a². O quadrado tem lado AE = a/5 e área a²/25, que é 1/50 = 2% do terreno. O limite é 100% − 94% = 6%, o triplo de 2%: ele pode triplicar a área do quadrado. Alternativa <strong>C</strong>.</p><p>Triplicar o lado (B) multiplicaria a área por 9 (18%).</p>",
  figs(("q140", "Retângulo ABCD com AB na vertical (lado esquerdo) e BC na horizontal; no canto A, um pequeno quadrado de lado AE, com E sobre AD.")),
  ["área do retângulo", "porcentagem"],
  enun=p("O governo cedeu terrenos para que famílias construíssem suas residências com a condição de que no mínimo 94% da área do terreno fosse mantida como área de preservação ambiental. Ao receber o terreno retangular ABCD, em que " + K("AB = \\dfrac{BC}{2}") + ", Antônio demarcou uma área quadrada no vértice A, para a construção de sua residência, de acordo com o desenho, no qual " + K("AE = \\dfrac{AB}{5}") + " é lado do quadrado.") + "[[fig:1]]" + p(T(140, 3)))
X(141, "Porcentagem", "<p>Se 4% da mistura são 925 milhões de litros, a mistura total é 925 ÷ 0,04 = 23 125 milhões de litros. Com 3%: 0,03 × 23 125 = <strong>693,75 milhões de litros</strong>. Alternativa <strong>D</strong>.</p><p>Outra forma: 925 × 3/4 = 693,75.</p>",
  tags=["porcentagem", "proporção"],
  enun=ap(T(141, 0)) + fonte(T(141, 1).split("(adaptado). ")[0] + "(adaptado).") + p(T(141, 1).split("(adaptado). ")[1], T(141, 2)))
X(142, "Funções", "<p>O gráfico tem degraus: até 14 cigarros por dia o número de casos fica constante (cerca de 20), e acima disso salta e fica constante de novo (cerca de 50). As grandezas estão relacionadas (mais cigarros, mais casos), mas não há proporção constante entre elas. Alternativa <strong>E</strong>.</p><p>Há casos mesmo com 0 cigarros, então D é falsa.</p>",
  figs(("q142", "Gráfico “Casos de câncer pulmonar dado o número de cigarros consumidos diariamente”: com 0 cigarros, cerca de 2 casos; de 1 a 14 cigarros, constante em cerca de 20 casos; de 15 a 25 cigarros, constante em cerca de 52 casos.")),
  ["grandezas proporcionais", "leitura de gráfico"], enun=ap(T(142, 0)) + "[[fig:1]]" + fonte(T(142, 2)) + p(T(142, 3)))
X(143, "Porcentagem", "<p>Em 05/09 o gráfico marca 23.020 mil pessoas, ou 23 020 000. Com 4% de crescimento: 23 020 000 × 1,04 = <strong>23 940 800</strong>. Alternativa <strong>D</strong>.</p><p>A opção A esquece que os valores estão em milhares.</p>",
  figs(("q143", "Gráfico de linha “População economicamente ativa (em mil pessoas)”, de 04/08 a 05/09: começa em 22.811, cai para 22.741 em 05/08, sobe até cerca de 23.300 em 10/08, oscila e termina com 22.959 em 04/09 e 23.020 em 05/09.")),
  ["aumento percentual", "leitura de gráfico"], enun=p(T(143, 0)) + "[[fig:1]]" + fonte(T(143, 2)) + p(T(143, 3)))
X(144, "Frações", "<p>Cada compasso de fórmula 3/4 soma 3/4; oito compassos somam 8 × 3/4 = 6, o equivalente a 24 semínimas (1/4). A opção D dá 24 × 1/8 + 12 × 1/4 = 3 + 3 = 6. Alternativa <strong>D</strong>.</p><p>16 semínimas e 8 semicolcheias (E) somam 4 + 1/2 = 4,5.</p>",
  figs(("q144", "Quadro com as figuras musicais e suas durações: semibreve 1, mínima 1/2, semínima 1/4, colcheia 1/8, semicolcheia 1/16, fusa 1/32 e semifusa 1/64.")),
  ["soma de frações", "música"],
  enun=p(T(144, 0)) + "[[fig:1]]" + p("Um compasso é uma unidade musical composta por determinada quantidade de notas musicais em que a soma das durações coincide com a fração indicada como fórmula do compasso. Por exemplo, se a fórmula de compasso for " + K("\\tfrac{1}{2}") + ", poderia ter um compasso ou com duas semínimas ou uma mínima ou quatro colcheias, sendo possível a combinação de diferentes figuras.",
                                     "Um trecho musical de oito compassos, cuja fórmula é " + K("\\tfrac{3}{4}") + ", poderia ser preenchido com"))
X(145, "Probabilidade", "<p>Há " + K("\\binom{4}{2} = 6") + " maneiras de escolher quais 2 dos 4 aparelhos são defeituosos. Cada uma tem probabilidade (0,2%)² × (99,8%)². Total: 6 × (0,2%)² × (99,8%)². Alternativa <strong>C</strong>.</p>",
  tags=["distribuição binomial", "combinação"], alts={k: v for k, v in zip("ABCDE", ["2 × (0,2%)<sup>4</sup>.", "4 × (0,2%)<sup>2</sup>.", "6 × (0,2%)<sup>2</sup> × (99,8%)<sup>2</sup>.", "4 × (0,2%).", "6 × (0,2%) × (99,8%)."])})
X(146, "Funções", "<p>Sete dias fora da promoção: 7 × 150 = R$ 1.050. Pacote de oito dias: 3 × 150 + 130 + 110 + 90 + 2 × 90 = 450 + 330 + 180 = R$ 960. Economia: 1 050 − 960 = <strong>R$ 90,00</strong>. Alternativa <strong>A</strong>.</p>",
  figs(("q146", "Gráfico do valor da diária em função do tempo (dias 1 a 8): constante em 150 até o dia 3, decrescendo em linha reta até o dia 6 e constante do dia 6 ao dia 8.")),
  ["função afim por partes"], enun=p(T(146, 0)) + "[[fig:1]]" + p(T(146, 2)))
X(147, "Geometria plana", "<p>A posição indicada pela seta precisa de uma peça que continue os desenhos das peças vizinhas. A peça 2, girada 90° no sentido anti-horário, encaixa os desenhos nos lados certos. Alternativa <strong>C</strong>.</p><p>Girar 270° no sentido anti-horário (E) equivale a 90° no horário, o que deixa o desenho invertido.</p>",
  figs(("q147a", "Figura A: tabuleiro 4 × 4 com 8 peças quadradas decoradas, formando faixas de desenhos; uma seta aponta para uma casa vazia na parte de baixo."),
       ("q147b", "Figura B: tabuleiro 4 × 4 com 8 peças decoradas; duas delas, na fileira de baixo, são indicadas como peça 1 e peça 2.")),
  ["rotação", "visualização"],
  enun=p(T(147, 0).replace("quebracabeças", "quebra-cabeças")) + "[[fig:1]]" + p("<strong>Figura A</strong>") + "[[fig:2]]" + p("<strong>Figura B</strong>") + fonte(T(147, 5)) + p(T(147, 6)))
X(148, "Funções", "<p>Taxa média de variação = (4,00 − 2,14) ÷ (2,0 − 1,1) = 1,86 ÷ 0,9 ≈ 2,07 ppm por tonelada, entre 1,50 e 2,80. Alternativa <strong>D</strong>.</p><p>A taxa média de variação é a inclinação da reta que liga o primeiro ao último ponto da tabela: variação da emissão dividida pela variação da produção.</p>",
  tags=["taxa média de variação"],
  enun=p(T(148, 0)) + tabela(["Produção (em toneladas)", "Emissão de dióxido de carbono (em partes por milhão – ppm)"],
                             [[a, b] for a, b in zip(["1,1", "1,2", "1,3", "1,4", "1,5", "1,6", "1,7", "1,8", "1,9", "2,0"], ["2,14", "2,30", "2,46", "2,64", "2,83", "3,03", "3,25", "3,48", "3,73", "4,00"])])
       + fonte(T(148, 3)) + p(T(148, 4)))
X(149, "Geometria plana", "<p>Nos anéis de Borromeo, os três anéis ficam presos juntos, mas nenhum par está entrelaçado: cada anel passa por cima de um e por baixo do outro, de modo que, se qualquer um for retirado, os outros dois se soltam. É o que mostra o esboço E. Alternativa <strong>E</strong>.</p><p>Nos outros esboços, algum par de anéis fica entrelaçado ou os três ficam soltos.</p>",
  figs(("q149", "Fotografia de um portão de ferro ornamentado com três anéis entrelaçados no centro."),
       ("q149a", "Esboço A: três círculos sobrepostos; os cruzamentos se alternam de modo que dois dos anéis ficam entrelaçados entre si."),
       ("q149b", "Esboço B: três círculos sobrepostos com outra combinação de cruzamentos por cima e por baixo."),
       ("q149c", "Esboço C: três círculos sobrepostos com outra combinação de cruzamentos."),
       ("q149d", "Esboço D: três círculos sobrepostos com outra combinação de cruzamentos."),
       ("q149e", "Esboço E: três círculos sobrepostos em que cada anel passa por cima de um dos outros e por baixo do terceiro.")),
  ["anéis de Borromeo", "visualização"], enun=p(T(149, 0)) + "[[fig:1]]" + fonte("<em>Scientific American</em>, ago. 2008.") + p(T(149, 3)), alts=ALT(2))
X(150, "Estatística", "<p>Média da França no Brasil: (825 + 485 + 1 458 + 744 + 1 214) ÷ 5 = 945,2. Média do Brasil na França: (367 + 357 + 354 + 539 + 280) ÷ 5 = 379,4. Diferença: 565,8 milhões de dólares, entre 500 e 600 milhões. Alternativa <strong>D</strong>.</p>",
  tags=["média aritmética"],
  enun=p(T(150, 0)) + tit("Investimentos Bilaterais (em milhões de dólares)") + tabela(["Ano", "Brasil na França", "França no Brasil"], [["2003", "367", "825"], ["2004", "357", "485"], ["2005", "354", "1.458"], ["2006", "539", "744"], ["2007", "280", "1.214"]])
       + fonte(T(150, 2)) + p(T(150, 3)))
X(151, "Equações", "<p>Seja c a cota final. A despesa total é 55c. Cada um dos 50 já tinha pago c − 7, e faltavam R$ 510: 50(c − 7) + 510 = 55c. Então 50c − 350 + 510 = 55c, 5c = 160 e c = <strong>R$ 32,00</strong>. Alternativa <strong>D</strong>.</p>",
  tags=["equação do 1º grau"])
X(152, "Grandezas e medidas", "<p>30 mil km³ = 3 × 10<sup>4</sup> × 10<sup>9</sup> m³ = 3 × 10<sup>13</sup> m³ = 3 × 10<sup>16</sup> litros. O reservatório tem 2 × 10<sup>7</sup> litros. Razão: 3 × 10<sup>16</sup> ÷ (2 × 10<sup>7</sup>) = 1,5 × 10<sup>9</sup>. Alternativa <strong>E</strong>.</p><p>Lembre: 1 km³ = 10<sup>9</sup> m³ e 1 m³ = 10<sup>3</sup> L.</p>",
  tags=["conversão de unidades", "notação científica"],
  enun=tit("Técnicos concluem mapeamento do aquífero Guarani") + ap(T(152, 0).replace("Técnicos concluem mapeamento do aquífero Guarani ", "", 1)) + fonte(T(152, 1)) + p(T(152, 2)),
  alts={k: re.sub(r"10(\d)", r"10<sup>\1</sup>", v).replace(" x ", " × ") for k, v in D[152]["alternativas"].items()})
X(153, "Geometria espacial", "<p>O plano paralelo à face α passa pelo ponto P e corta os prismas I e III, que são perpendiculares ao plano da face α do prisma I e iguais entre si. As seções são cópias da base triangular desses prismas: dois triângulos congruentes com lados correspondentes paralelos. Alternativa <strong>A</strong>.</p>",
  figs(("q153", "Fotografia de uma escultura de Emanoel Araújo formada por prismas escuros de base triangular encaixados; estão marcados os prismas I, III e IV, o poliedro II, a face α do prisma I e o ponto P numa aresta do poliedro II.")),
  ["seções planas", "prismas"], enun=p(T(153, 0)) + "[[fig:1]]" + fonte(T(153, 2)) + p(T(153, 3)))
X(154, "Semelhança de triângulos", "<p>A rampa é a hipotenusa de triângulos semelhantes: andar 3,2 m faz subir 0,8 m, então cada metro de rampa sobe 0,25 m. Para subir 2,2 m é preciso andar 2,2 ÷ 0,25 = 8,8 m. Faltam 8,8 − 3,2 = <strong>5,6 m</strong>. Alternativa <strong>D</strong>.</p>",
  tags=["semelhança", "proporção"])
X(155, "Função quadrática", "<p>Com desconto de x centavos, o preço é (1,50 − 0,01x) reais e a venda é (10 000 + 100x) litros. V = (1,50 − 0,01x)(10 000 + 100x) = 15 000 + 150x − 100x − x² = 15 000 + 50x − x². Alternativa <strong>D</strong>.</p>",
  tags=["função quadrática", "modelagem"], alts={k: v.replace("x2", "x<sup>2</sup>") for k, v in D[155]["alternativas"].items()})
X(156, "Números", "<p>d<sub>1</sub>: 1·10 + 2·9 + 3·8 + 4·7 + 5·6 + 6·5 + 7·4 + 8·3 + 9·2 = 210; 210 = 11 × 19 + 1, resto 1, então d<sub>1</sub> = 0. d<sub>2</sub>: 2·10 + 3·9 + 4·8 + 5·7 + 6·6 + 7·5 + 8·4 + 9·3 + 0·2 = 244; 244 = 11 × 22 + 2, resto 2, então d<sub>2</sub> = 11 − 2 = 9. Alternativa <strong>A</strong>.</p>",
  tags=["divisão e resto", "dígito verificador"], trocas=[("d1d2", "d<sub>1</sub>d<sub>2</sub>"), ("dígitos d1 e d2", "dígitos d<sub>1</sub> e d<sub>2</sub>"), ("d1 é zero", "d<sub>1</sub> é zero"), ("d1 = (11 – r)", "d<sub>1</sub> = (11 – r)"), ("dígito d2", "dígito d<sub>2</sub>"), ("sendo d1 o", "sendo d<sub>1</sub> o"), ("d2 é zero", "d<sub>2</sub> é zero"), ("d2 = (11 – s)", "d<sub>2</sub> = (11 – s)"), ("verificadores d1 e d2", "verificadores d<sub>1</sub> e d<sub>2</sub>")])
X(157, "Geometria espacial", "<p>A aresta do cubo é " + K("\\sqrt[3]{13\\,824} = 24") + " cm. Cada esfera tem 12 cm de diâmetro, então cabem 24 ÷ 12 = 2 esferas em cada direção: 2 × 2 × 2 = <strong>8</strong>. Alternativa <strong>B</strong>.</p><p>Dividir volumes (E, 32) ignora os espaços vazios entre as esferas.</p>",
  tags=["volume do cubo", "raiz cúbica"], trocas=[("13.824 cm3", "13.824 cm<sup>3</sup>")])
X(158, "Escala", "<p>Na escala 1:150, 28,5 m = 2 850 cm vira 19 cm e 36 m = 3 600 cm vira 24 cm. Com 1 cm de margem de cada lado: 21 cm × 26 cm. Alternativa <strong>D</strong>.</p><p>A opção C esquece as margens.</p><p>Escala 1:150 significa que cada 1 cm no papel representa 150 cm reais.</p>",
  figs(("q158", "Desenho de um avião visto de cima, com envergadura de 28,5 metros e comprimento de 36 metros.")), ["escala"], enun=p(T(158, 0)) + "[[fig:1]]" + p(T(158, 2)))
X(159, "Função afim", "<p>A cada 5 bolas, o nível sobe 0,35 cm: a taxa é 0,07 cm por bola. Com 5 bolas, y = 6,35, então o nível inicial é 6,35 − 5 × 0,07 = 6. Logo y = 0,07x + 6. Alternativa <strong>E</strong>.</p><p>Confira com 15 bolas: 0,07 × 15 + 6 = 7,05 cm, como no quadro.</p>",
  figs(("q159", "Copo cilíndrico com água e bolas de vidro no fundo, ao lado de uma régua; y indica a altura do nível da água.")), ["função afim"],
  enun=p(T(159, 0)) + "[[fig:1]]" + p(T(159, 2)) + tabela(["número de bolas (x)", "nível da água (y)"], [["5", "6,35 cm"], ["10", "6,70 cm"], ["15", "7,05 cm"]]) + fonte(T(159, 4)) + p(T(159, 5)))
X(160, "Razão e proporção", "<p>Hoje a cooperativa colhe 20 ha por dia, ou 120 ha em 6 dias; são necessários 180 ha, 1,5 vez mais. Aumentar a jornada de 6 para 9 horas (1,5 vez) resolve sem mudar o custo diário: 12 × 10 × 6 + 4 × 1 000 × 6 = R$ 24.720, abaixo de R$ 25.000. Alternativa <strong>D</strong>.</p><p>Mais 4 máquinas (B) dobraria o aluguel e passaria de R$ 48 mil.</p>",
  tags=["regra de três composta", "custo"])
X(161, "Estatística", "<p>Notas da Gama em ordem: 0; 6; 6,5; 6,5; 7; 7; 8; 8; 10; 10. Mediana = (7 + 7) ÷ 2 = 7. Se o aluno faltoso tirasse 10, a lista seria 6; 6,5; 6,5; 7; 7; 8; 8; 10; 10; 10, com mediana (7 + 8) ÷ 2 = 7,5, ainda abaixo de 7,6. A mediana nunca passa de 7,5, então a Gama continua em terceiro, qualquer que seja a nota. Alternativa <strong>D</strong>.</p>",
  tags=["mediana"])
X(162, "Razão e proporção", "<p>Nos 10 primeiros dias: 12 kg/dia, total de 120 kg, com 20 alunos × 3 h = 60 horas-aluno por dia, ou 0,2 kg por hora-aluno. Nos 20 dias seguintes: 50 alunos × 4 h = 200 horas-aluno por dia, ou 40 kg/dia, total de 800 kg. Total: 120 + 800 = <strong>920 kg</strong>. Alternativa <strong>A</strong>.</p>",
  tags=["regra de três composta"])
X(163, "Grandezas e medidas", "<p>16 voltas × 7 km = 112 km. Consumo: 112 × 0,75 = 84 L. Massa da gasolina: 84 × 0,75 kg = 63 kg. Peso mínimo: 605 + 63 = <strong>668 kg</strong>. Alternativa <strong>B</strong>.</p><p>O peso mínimo do carro com o piloto (605 kg) já é dado com o tanque vazio; basta somar a gasolina necessária para as 16 voltas.</p>",
  tags=["densidade", "proporção"])
X(164, "Trigonometria", "<p>As divisas partem do canto e dividem o quarto de círculo em três ângulos de 30°. A parte de João é o triângulo junto ao lado de 2 km, com catetos 2 km e 2 · tg 30° = 2 · " + K("\\tfrac{\\sqrt3}{3}") + " ≈ 1,16 km. Área: 2 × 1,16 ÷ 2 = 1,16 km², de um terreno de 6 km²: 1,16 ÷ 6 ≈ 19%. Alternativa <strong>E</strong>.</p>",
  figs(("q164", "Retângulo de 3 km por 2 km com um quarto de círculo de raio 1 km sombreado no canto inferior esquerdo; duas retas partem desse canto e dividem o terreno em três partes: João (junto ao lado esquerdo), Pedro (no meio) e José (embaixo, à direita).")),
  ["tangente", "área de triângulo"], enun=p(T(164, 0)) + "[[fig:1]]" + p(T(164, 2), "(considere " + K("\\dfrac{\\sqrt{3}}{3} = 0{,}58") + ")"))
X(165, "Análise combinatória", "<p>Escolher 4 times para o Grupo A não depende da ordem: combinação C(12, 4). Escolher os 2 times do jogo de abertura depende da ordem (o primeiro joga em casa, o segundo é visitante): arranjo A(4, 2). Alternativa <strong>A</strong>.</p>",
  tags=["combinação", "arranjo"])
X(166, "Geometria plana", "<p>A rota Brasília–Belém aponta para o norte. Girando 135° no sentido horário, o avião A<sub>II</sub> segue para o sudeste e chega a Belo Horizonte. Dali, o A<sub>III</sub> segue um ângulo reto no sentido anti-horário em relação à direção sudeste, ou seja, para o nordeste: Salvador. Alternativa <strong>B</strong>.</p>",
  figs(("q166", "Mapa do Brasil com estados e capitais numeradas: 1 Manaus, 2 Boa Vista, 3 Macapá, 4 Belém, 5 São Luís, 6 Teresina, 7 Fortaleza, 8 Natal, 9 Salvador, 10 Rio de Janeiro, 11 São Paulo, 12 Curitiba, 13 Belo Horizonte, 14 Goiânia, 15 Cuiabá, 16 Campo Grande, 17 Porto Velho e 18 Rio Branco; um segmento liga o Distrito Federal (DF) a Belém (4), para o norte.")),
  ["ângulos", "orientação"], enun=p(T(166, 0)) + "[[fig:1]]" + fonte(T(166, 2)) + p(T(166, 3).replace("135o graus", "135°").replace("AIII", "A<sub>III</sub>").replace("AII", "A<sub>II</sub>")))
X(167, "Grandezas e medidas", "<p>Pantanal: 150 355 km² = 1,50355 × 10<sup>11</sup> m². Campo: 120 × 90 = 10 800 m². Número de campos: 1,50355 × 10<sup>11</sup> ÷ 10 800 ≈ 1,39 × 10<sup>7</sup> ≈ <strong>14.000.000</strong>. Alternativa <strong>E</strong>.</p><p>1 km² = 10<sup>6</sup> m².</p>",
  tags=["conversão de unidades de área"],
  enun=p(T(167, 0)) + tabela(["Biomas continentais brasileiros", "Área aproximada (km<sup>2</sup>)", "Área / total Brasil"],
                             [["Amazônia", "4.196.943", "49,29%"], ["Cerrado", "2.036.448", "23,92%"], ["Mata Atlântica", "1.110.182", "13,04%"], ["Caatinga", "844.453", "9,92%"], ["Pampa", "176.496", "2,07%"], ["Pantanal", "150.355", "1,76%"], ["Área Total Brasil", "8.514.877", ""]])
       + fonte(T(167, 3)) + p(T(167, 4)))
X(168, "Estatística", "<p>Em ordem: 73,10; 81,60; 82,00; 83,00; 84,00; 84,60; 85,30. São 7 valores, e a mediana é o 4º: <strong>R$ 83,00</strong>. Alternativa <strong>D</strong>.</p><p>Com uma quantidade ímpar de valores, a mediana é o valor central depois de colocar os dados em ordem; a média seria cerca de R$ 81,94.</p>",
  tags=["mediana"],
  enun=p(T(168, 0)) + tabela(["Mês", "Cotação", "Ano"], [["Outubro", "R$ 83,00", "2007"], ["Novembro", "R$ 73,10", "2007"], ["Dezembro", "R$ 81,60", "2007"], ["Janeiro", "R$ 82,00", "2008"], ["Fevereiro", "R$ 85,30", "2008"], ["Março", "R$ 84,00", "2008"], ["Abril", "R$ 84,60", "2008"]]) + p(T(168, 2)))
X(169, "Áreas", "<p>Figura I: trapézio com bases 30 e 20 e altura 2,5: área (30 + 20) × 2,5 ÷ 2 = 62,5 m². Figura II: bases 49 e 41 e altura 2: (49 + 41) × 2 ÷ 2 = 90 m². Com a mesma velocidade, a vazão cresce na razão 90 ÷ 62,5 = 1,44: 1 050 × 1,44 = <strong>1 512 m³/s</strong>. Alternativa <strong>D</strong>.</p>",
  figs(("q169", "Figura I: corte de canaleta em forma de trapézio isósceles com base maior (superior) de 30 m, base menor de 20 m e altura de 2,5 m. Figura II: trapézio com base maior de 49 m, base menor de 41 m e altura de 2,0 m.")),
  ["área do trapézio", "proporção"], enun=SUP(p(T(169, 0), T(169, 1))) + "[[fig:1]]" + fonte(T(169, 3)) + p(T(169, 4)), alts={k: v.replace("m3/s", "m<sup>3</sup>/s") for k, v in D[169]["alternativas"].items()})
X(170, "Grandezas e medidas", "<p>Cada foto: 2 milhões de pontos × 3 bytes = 6 MB; com compressão de 95%, sobram 5%: 0,3 MB. 150 fotos: 45 MB. O dispositivo que cabe com menor sobra é o cartão de 64 MB. Alternativa <strong>E</strong>.</p><p>O memory stick de 16 MB (D) não comporta as fotos.</p>",
  tags=["porcentagem", "unidades de informação"])
X(171, "Probabilidade", "<p>Uma aposta de 6 dezenas tem C(6, 5) × 54 = 324 combinações que dão quina; 84 apostas sem cinco números em comum: 84 × 324 = 27 216. Uma aposta de 9 dezenas tem C(9, 5) × 51 = 126 × 51 = 6 426. Razão: 27 216 ÷ 6 426 ≈ 4,2: a chance com nove dezenas é cerca de 4 vezes menor. Alternativa <strong>C</strong>.</p><p>As duas opções custam R$ 126: 84 × 1,50 e C(9, 6) = 84 apostas simples.</p>",
  tags=["combinação", "probabilidade"], enun=ap(T(171, 0)) + fonte(T(171, 1)) + p(T(171, 2)),
  alts={**D[171]["alternativas"], "A": K("1\\tfrac{1}{2}") + " vez menor.", "B": K("2\\tfrac{1}{2}") + " vezes menor."})
X(172, "Porcentagem", "<p>De junho a dezembro: importação 7/5 × 9 = 12,6 milhões de m³ × 340 = 4,284 bilhões; exportação 7/5 × 11 = 15,4 milhões de m³ × 230 = 3,542 bilhões. Somando janeiro a maio: importações 2,84 + 4,284 = 7,124 bilhões; exportações 2,24 + 3,542 = 5,782 bilhões. Diferença ≈ <strong>1,34 bilhão de dólares</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["proporção", "operações com decimais"],
  enun=ap(T(172, 0)) + tit("Comércio exterior de petróleo (milhões de metros cúbicos)")
       + tabela(["Ano", "Importação", "Exportação"], [["2001", "24,19", "6,43"], ["2002", "22,06", "13,63"], ["2003", "19,96", "14,03"], ["2004", "26,91", "13,39"], ["2005", "21,97", "15,93"], ["2006", "20,91", "21,36"], ["2007", "25,38", "24,45"], ["2008", "23,53", "25,14"], ["2009*", "9,00", "11,00"]])
       + fonte("*Valores apurados de janeiro a maio de 2009.") + fonte(T(172, 3))
       + p("Considere que as importações e exportações de petróleo de junho a dezembro de 2009 sejam iguais a " + K("\\tfrac{7}{5}") + " das importações e exportações, respectivamente, ocorridas de janeiro a maio de 2009. Nesse caso, supondo que os preços para importação e exportação não sofram alterações, qual seria o valor mais aproximado da diferença entre os recursos despendidos com as importações e os recursos gerados com as exportações em 2009?"))
X(173, "Geometria espacial", "<p>4 blocos de altura h e 3 espaços de 1 cm: 4h + 3 = 19, então h = 4 cm. Sem os espaços, os blocos formam uma pirâmide de 16 cm de altura e base 6 cm: V = 36 × 16 ÷ 3 = 192 cm³. A pirâmide do topo tem base 1,5 cm e altura 4 cm: 2,25 × 4 ÷ 3 = 3 cm³. Sem ela: 192 − 3 = <strong>189 cm³</strong>. Alternativa <strong>B</strong>.</p>",
  figs(("q173", "Vela em forma de pirâmide quadrangular de base 6 cm por 6 cm, formada por quatro blocos empilhados com pequenos espaços entre eles e um pavio no topo.")),
  ["volume da pirâmide", "tronco de pirâmide"], enun=p(T(173, 0)) + "[[fig:1]]" + p(T(173, 2)), alts=SUPD(D[173]["alternativas"]))
X(174, "Trigonometria", "<p>P parte do ponto mais à esquerda da circunferência, com Q à distância r à esquerda do centro. Andar d sobre a circunferência corresponde ao ângulo central d/r. A projeção do novo ponto fica a r·cos(d/r) à esquerda do centro, então Q se desloca r − r·cos(d/r) = " + K("r\\left(1 - \\cos\\tfrac{d}{r}\\right)") + ". Alternativa <strong>B</strong>.</p>",
  figs(("q174", "Plano cartesiano com uma circunferência de raio r; P é o ponto mais à esquerda da circunferência, e Q é sua projeção no eixo x.")),
  ["ciclo trigonométrico", "projeção"], enun=p(T(174, 0)) + "[[fig:1]]" + p("Então, o ponto Q percorrerá, no eixo x, uma distância dada por"),
  alts=FR("r\\left(1 - \\operatorname{sen}\\dfrac{d}{r}\\right)", "r\\left(1 - \\cos\\dfrac{d}{r}\\right)", "r\\left(1 - \\operatorname{tg}\\dfrac{d}{r}\\right)", "r\\operatorname{sen}\\left(\\dfrac{r}{d}\\right)", "r\\cos\\left(\\dfrac{r}{d}\\right)"))
X(175, "Sistemas de equações", "<p>Seja a = NV/NF e b = NA/NV. Pelo enunciado, (a + b)/2 = 0,6, ou a + b = 1,2. Dobrando NF, a vira a/2: a/2 + b = 1,0. Subtraindo, a/2 = 0,2, então a = 0,4 e b = 0,8. NA = 0,8 NV e NA + NV = 1,8 NV = 3 600, então NV = 2 000 e NF = 2 000 ÷ 0,4 = <strong>5 000</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["sistema linear", "razões"],
  enun=p(T(175, 0).rstrip(",") + ", em que " + K("TC = \\dfrac{NV}{NF}") + ", " + K("TA = \\dfrac{NA}{NV}") + ", NV é o número de cadastros domiciliares válidos no perfil do CadÚnico, NF é o número de famílias estimadas como público alvo do CadÚnico e NA é o número de cadastros domiciliares atualizados no perfil do CadÚnico.")
       + fonte(T(175, 2)) + p(T(175, 3)))
X(176, "Grandezas e medidas", "<p>Das 10h30 às 11h07 são 37 min = 2 220 s. Aquecimento 600 s + descanso 60 s = 660 s. 18 séries (3 × 6) de 30 s = 540 s. Entre as 18 séries há 17 descansos de 60 s = 1 020 s. Total: 660 + 540 + 1 020 = 2 220 s: dá exatamente para cumprir tudo. Alternativa <strong>B</strong>.</p>",
  tags=["unidades de tempo"])
X(177, "Geometria espacial", "<p>A pirâmide de base quadrada tem 5 faces (4 triângulos e a base). Um plano corta cada face em no máximo um segmento; se cortar as 5 faces, a seção é um polígono de 5 lados, um pentágono. Alternativa <strong>C</strong>.</p><p>A e E dizem que o resultado sempre tem 4 lados, o que contradiz a conclusão do artesão.</p>",
  tags=["seções planas", "pirâmide"])
X(178, "Matemática financeira", "<p>Custos: renegociar, 18 × 125 = R$ 2.250; pagar tudo no prazo, 1 800 + 400 = R$ 2.200; empréstimo para as duas quitações, (1 500 + 300) × 1,25 = R$ 2.250; só para o cheque especial, 1 500 × 1,25 + 400 = R$ 2.275; só para o cartão, 300 × 1,25 + 1 800 = <strong>R$ 2.175</strong>, o menor. Alternativa <strong>E</strong>.</p><p>Quitar o cheque com desconto de 2 parcelas custa 1 500; o cartão com 25% de desconto, 300.</p>",
  tags=["juros", "comparação de opções"])
X(179, "Grandezas e medidas", "<p>Volume da cisterna: 2 000 L × 15 dias = 30 000 L, mais 10%: 33 000 L. Área do telhado: 33 000 ÷ 110 = 300 m². Dimensões: 15 m × 20 m. Alternativa <strong>B</strong>.</p><p>O que importa é a área de 300 m²; entre as opções, só 15 m × 20 m tem exatamente essa área. Lembre que 1 mm de chuva sobre 1 m² dá 1 litro.</p>",
  tags=["volume", "área"], enun=SUP(ap(T(179, 0))) + fonte(T(179, 1)) + p(T(179, 2)), alts=SUPD(D[179]["alternativas"]))
X(180, "Probabilidade", "<p>A chance de não ter efeito colateral em n doses é 0,9<sup>n</sup>; o risco é 1 − 0,9<sup>n</sup> ≤ 0,35, ou 0,9<sup>n</sup> ≥ 0,65. 0,9<sup>4</sup> = 0,6561 (serve); 0,9<sup>6</sup> ≈ 0,531 (não serve). O maior número entre as opções é <strong>4 doses</strong>. Alternativa <strong>B</strong>.</p>",
  tags=["probabilidade do evento complementar", "potências"])

completar(Q, R)
