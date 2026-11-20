# Enem 2023, 2º dia, caderno azul: Matemática (questões 136 a 180 do caderno; no site, 1 a 45, com numeroOriginal).
# Frações, raízes e fórmulas reescritas em KaTeX (a camada de texto do PDF as quebra). Alternativas-imagem nas Q163, 177 e 178.
# Q164 anulada pelo Inep por falta de ineditismo (repetia questão do Enem PPL 2010).
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, paragrafos_enem

ID = "enem-2023-matematica"
META = {"id": ID, "banca": "Enem", "ano": 2023, "titulo": "Enem 2023: Matemática", "fonte": "Inep", "dataExame": "2023-11-12",
        "duracaoMinutos": 150, "area": "Matemática", "caderno": "azul", "dia": 2}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2023-dia2-azul")
Q = {}
P = lambda n: paragrafos_enem(D[n])
T = lambda n, i: P(n)[i][1]
p = lambda *xs: "".join(f"<p>{x}</p>" for x in xs)
ap = lambda *xs: "".join(f'<p class="apoio">{x}</p>' for x in xs)
fonte = lambda x: f'<p class="fonte">{x}</p>'
LISTA = lambda s: "<ul>" + "".join(f"<li>{x.strip()}</li>" for x in re.split(r"•|<br>", s) if x.strip()) + "</ul>"
ALT = lambda ini: {k: f"[[fig:{i}]]" for i, k in enumerate("ABCDE", ini)}
FR = lambda *xs: {k: f"\\({v}\\)" for k, v in zip("ABCDE", xs)}
ANUL = ('<p>O Inep anulou esta questão por falta de ineditismo: o enunciado, o gráfico e as alternativas repetiam uma questão do '
        'Enem PPL 2010 (aplicado a pessoas privadas de liberdade). O anúncio foi feito pelo ministro da Educação, Camilo Santana, '
        'no dia da prova. A anulação não aponta erro no conteúdo da questão.</p>')


def figs(*pares):
    return [{"arquivo": a, "alt": t} for a, t in pares]


def tabela(cab, linhas):
    return ('<table class="tabela"><thead><tr>' + "".join(f"<th>{c}</th>" for c in cab) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in l) + "</tr>" for l in linhas) + "</tbody></table>")


def E(n, pular=(), trocas=()):
    par = P(n)
    ult = max([i for i, (t, _) in enumerate(par) if t == "fonte" and i not in pular], default=-1)
    h = []
    for i, (t, x) in enumerate(par):
        if i in pular: continue
        if t == "fig": h.append(f"[[fig:{x}]]")
        elif t == "fonte": h.append(fonte(x))
        elif t == "titulo": h.append(f'<p class="apoio"><strong>{x}</strong></p>' if i < ult else f"<p><strong>{x}</strong></p>")
        elif i < ult: h.append(ap(x))
        else: h.append(p(x))
    s = "".join(h)
    for a, b in trocas:
        assert a in s, a; s = s.replace(a, b)
    return s


def X(n, assunto, expl, imagens=(), tags=(), enun=None, trocas=(), alts=None, anulacao=None):
    q = {"materia": "Matemática", "assunto": assunto, "area": "Matemática", "tags": list(tags), "numeroOriginal": n,
         "enunciado": enun or E(n, trocas=trocas), "alternativas": dict(alts or D[n]["alternativas"]),
         "imagens": list(imagens), "explicacao": expl}
    if anulacao: q["anulacao"] = anulacao
    Q[n - 135] = q


X(136, "Geometria espacial", "<p>O cone grande (raio 9, altura 36) tem volume ⅓ · 3 · 81 · 36 = 2 916 cm³. O cone retirado é semelhante, com raio 3, e portanto altura 12: ⅓ · 3 · 9 · 12 = 108 cm³. O tronco tem 2 916 − 108 = 2 808 cm³ e altura 24 cm. O furo cilíndrico (raio 3, altura 24) tem 3 · 9 · 24 = 648 cm³. Sobram 2 160 cm³, com massa 2 160 · 0,6 = <strong>1 296 g</strong>. Alternativa <strong>B</strong>.</p><p>1 360,8 g (C) esquece o cone menor ao calcular o furo; 4 860 g (E) é a massa do tronco sem o furo, usando volume errado.</p>",
  figs(("q136", "Um cone amarelo com 36 cm de altura e base de 18 cm de diâmetro, com um cone menor de 6 cm de diâmetro marcado no topo; uma seta leva ao tronco de cone resultante, atravessado por um cilindro escuro de base a base.")),
  ["tronco de cone", "volume"], enun=ap(T(136, 0)) + "[[fig:1]]" + ap(T(136, 5), T(136, 6)) + p(T(136, 7)))
X(137, "Estatística", "<p>A média ponderada é (75 · 2 000 + 25 · 7 000) ÷ 100 = (150 000 + 175 000) ÷ 100 = <strong>R$ 3 250,00</strong>. Alternativa <strong>C</strong>.</p><p>R$ 4 500,00 (D) é a média simples dos dois salários, sem considerar quantos funcionários recebem cada um; R$ 9 000,00 (E) é a soma dos salários.</p>",
  tags=["média ponderada"],
  enun=p(T(137, 0)) + tabela(["Setor", "Quantidade de funcionários", "Salário (em real)"], [["Produção", "75", "2 000,00"], ["Administração", "25", "7 000,00"]]) + p(T(137, 2)))
X(138, "Probabilidade", "<p>A chance de ganhar é P(preta em A) · P(preta em B) = 0,20 · P(B). Para ficar em no máximo 1%, P(B) ≤ 0,05. A urna B tem 4 pretas: 4 ÷ total ≤ 0,05 exige total ≥ 80. Hoje, com 25% de pretas, B tem 16 bolinhas (4 pretas e 12 brancas). Faltam 80 − 16 = <strong>64</strong> brancas. Alternativa <strong>C</strong>.</p><p>76 seria o total de brancas, não o acréscimo; 60 (B) deixaria a chance acima de 1%.</p>",
  tags=["eventos independentes"], trocas=[("um voucher", "um <em>voucher</em>"), ("seu voucher", "seu <em>voucher</em>"), ("ganhar o voucher", "ganhar o <em>voucher</em>"), ("Ganha o voucher", "Ganha o <em>voucher</em>")])
X(139, "Sequências", "<p>As vendas de I sobem 10 por mês (80, 90, 100) e as de II caem 20 (190, 170, 150). Em julho: I = 110, II = 130. Em agosto: I = 120, II = 110, e I supera II pela primeira vez. A produção de II para no mês seguinte, <strong>setembro</strong>. Alternativa <strong>D</strong>.</p><p>Agosto (C) é o mês em que I passa II, não o mês em que II deixa de ser produzido.</p>",
  tags=["progressão aritmética"],
  enun=p(T(139, 0)) + tabela(["Produto", "Vendas em abril (unidade)", "Vendas em maio (unidade)", "Vendas em junho (unidade)"], [["I", "80", "90", "100"], ["II", "190", "170", "150"]]) + p(T(139, 2), T(139, 3), T(139, 4)))
X(140, "Estatística", "<p>Pelo gráfico: 10 motoristas com 1 viagem, 10 com 2, 55 com 3, 25 com 4, nenhum com 5, 50 com 6 e 10 com 7 (total 160). A <strong>moda</strong> é 3. A mediana é a média do 80º e do 81º valores: até 3 viagens há 75 motoristas e até 4 há 100, então a <strong>mediana</strong> é 4. A <strong>média</strong> é (10 + 20 + 165 + 100 + 300 + 70) ÷ 160 = 665 ÷ 160 ≈ 4,16. Logo, moda &lt; mediana &lt; média. Alternativa <strong>E</strong>.</p>",
  figs(("q140", "Gráfico de barras horizontais: quantidade de viagens realizadas (eixo vertical, de 1 a 7) por quantidade de motoristas (eixo horizontal). 1 viagem: 10 motoristas; 2: 10; 3: 55; 4: 25; 5: nenhum; 6: 50; 7: 10.")),
  ["média, mediana e moda"], enun=p(T(140, 0)) + "[[fig:1]]" + p(T(140, 4)))
X(141, "Probabilidade", "<p>Os cartões na urna são: 200 · 1 = 200 (primeiro ano), 150 · 2 = 300 (segundo ano) e 100 · 3 = 300 (terceiro ano), num total de 800. A probabilidade de sair um cartão de estudante do terceiro ano é 300 ÷ 800 = \\(\\frac{3}{8}\\). Alternativa <strong>E</strong>.</p><p>\\(\\frac{2}{9}\\) (D) conta pessoas (100 de 450), sem considerar o número de cartões de cada uma.</p>",
  tags=["probabilidade"], enun=p(T(141, 0), T(141, 1)), alts=FR("\\frac{1}{2}", "\\frac{1}{3}", "\\frac{1}{8}", "\\frac{2}{9}", "\\frac{3}{8}"))
X(142, "Geometria espacial", "<p>Restam no reservatório 3 · 5² · 1,5 = 112,5 m³ = 112 500 L para 10 dias e 75 moradores: 112 500 ÷ (10 · 75) = 150 L por morador por dia. Como o consumo normal é 200 L, cada um precisa economizar, no mínimo, <strong>50 L</strong> por dia. Alternativa <strong>A</strong>.</p><p>150 L (E) é o que cada um pode gastar, não o que precisa economizar.</p>",
  tags=["volume do cilindro"], trocas=[("aproximação para p.", "aproximação para π.")])
X(143, "Porcentagem", "<p>A lista deste ano tem 400 + 10% = 440 nomes, e a do próximo ano também teria 440. Para ficar 25% menor, deve cair para 330: é preciso atender 110 crianças a mais. Com 10 crianças por sala, são <strong>11 salas</strong>. Alternativa <strong>B</strong>.</p><p>10 salas (A) calcula 25% de 400, a lista do ano passado; 33 (E) confunde 25% com o total que sobra na lista.</p>",
  tags=["porcentagem"])
X(144, "Funções", "<p>O nível sobe 0,6 m em 2 h (das 6h às 8h), 1,2 m em 4 h (das 8h às 12h) e 0,9 m em 3 h (das 12h às 15h): sempre 0,3 m por hora. Com 3 m² de base, entram 0,3 · 3 = <strong>0,9 m³ por hora</strong>. Alternativa <strong>C</strong>.</p><p>0,3 (A) é a velocidade de subida do nível em metro por hora, sem multiplicar pela área da base.</p>",
  figs(("q144", "Foto em preto e branco de uma cisterna circular em construção, num buraco cavado no chão, com trabalhadores ao redor e uma casa ao fundo.")),
  ["função afim", "vazão"],
  enun=p(T(144, 0).replace("3 m²", "3 m<sup>2</sup>")) + tabela(["Horário (h)", "Nível da água (m)"], [["6:00", "0,5"], ["8:00", "1,1"], ["12:00", "2,3"], ["15:00", "3,2"]]) + "[[fig:1]]" + fonte(T(144, 3)) + p(T(144, 4)))
X(145, "Geometria plana", "<p>Ângulos inscritos que “enxergam” a mesma corda AB têm a mesma medida quando os vértices estão no mesmo arco da mesma circunferência. Na figura, a circunferência que passa por A, B e Q<sub>1</sub> também passa por <strong>Q<sub>3</sub></strong>; então o ângulo AQ<sub>3</sub>B mede α. Alternativa <strong>B</strong>.</p><p>Os outros jogadores estão em circunferências diferentes (dentro ou fora dela), onde o ângulo é maior ou menor que α.</p>",
  figs(("q145", "Campo de futebol visto de cima. À esquerda, os pés da trave A e B. Várias circunferências tracejadas passam por A e B. O jogador Q₁, com a bola, vê a trave sob o ângulo α. Os jogadores Q₂, Q₃, Q₄, Q₅ e Q₆ estão espalhados; Q₃ está sobre a mesma circunferência que passa por A, B e Q₁.")),
  ["ângulo inscrito", "circunferência"],
  enun=p("Num certo momento de um jogo digital, a tela apresenta a imagem representada na figura. O ponto Q<sub>1</sub> representa a posição de um jogador que está com a bola, os pontos Q<sub>2</sub>, Q<sub>3</sub>, Q<sub>4</sub>, Q<sub>5</sub> e Q<sub>6</sub> também indicam posições de jogadores da mesma equipe, e os pontos <em>A</em> e <em>B</em> indicam os dois pés da trave mais próxima deles. No momento da partida retratado, o jogador Q<sub>1</sub> tem a posse da bola, que será passada para um dos outros jogadores das posições \\(Q_n,\\ n \\in \\{2, 3, 4, 5, 6\\}\\), cujo ângulo \\(A\\widehat{Q_n}B\\) tenha a mesma medida do ângulo \\(\\alpha = A\\widehat{Q_1}B\\).")
       + "[[fig:1]]" + p(T(145, 3)),
  alts={k: f"Q<sub>{i}</sub>" for k, i in zip("ABCDE", range(2, 7))})
X(146, "Raciocínio lógico", "<p>Os vértices em PA de razão 2 só podem ser 1, 3, 5 ou 2, 4, 6. Com 1, 3 e 5 nos vértices, os meios recebem 2, 4 e 6: as somas iguais (1 + x + 3 = 3 + y + 5 = 5 + z + 1) dão x = 6, y = 2, z = 4, e cada lado soma 10. Com 2, 4 e 6 nos vértices, os meios recebem 1, 3 e 5: x = 5, y = 1, z = 3, e cada lado soma 11. Há <strong>duas soluções, com somas 10 e 11</strong>. Alternativa <strong>E</strong>.</p>",
  figs(("q146", "Triângulo com seis círculos vazios: um em cada vértice e um no meio de cada lado.")),
  ["progressão aritmética", "quadrado mágico"])
X(147, "Razão e proporção", "<p>Cada pessoa precisa de 30 g de carboidrato por dia (1 g por minuto). O casal, em 30 dias, precisa de 2 · 30 · 30 = 1 800 g. Cada pacote tem 18 · 15 = 270 g. Como 1 800 ÷ 270 ≈ 6,67, são necessários, no mínimo, <strong>7 pacotes</strong>. Alternativa <strong>D</strong>.</p><p>6 pacotes (C) arredonda para baixo e não bastam; 4 pacotes (B) considera só uma pessoa.</p>",
  tags=["proporção", "arredondamento"],
  trocas=[("Revista Saúde! É Vital", "<em>Revista Saúde! É Vital</em>")])
X(148, "Trigonometria", "<p>O cabo é a hipotenusa do triângulo retângulo com o mastro: cabo = h ÷ sen α. Opção I: 11 ÷ 0,5 = 22 m. Opção II: 12 ÷ \\(\\frac{\\sqrt{2}}{2}\\) = 12√2 ≈ 17,0 m. Opção III: 18 ÷ \\(\\frac{\\sqrt{3}}{2}\\) = 12√3 ≈ 20,8 m. A menor é a da opção II: <strong>12√2 m</strong>. Alternativa <strong>C</strong>.</p>",
  figs(("q148", "Mastro vertical com uma bandeira no alto, fincado num chão plano. Do ponto P, à altura h, saem três cabos de aço até o chão, cada um formando um ângulo α com o solo.")),
  ["seno", "triângulo retângulo"],
  enun=p(T(148, 0)) + "[[fig:1]]" + p("Os cabos de aço formam um ângulo α com o plano do chão.", T(148, 3)) + LISTA("opção I: <em>h</em> = 11 m e α = 30°•opção II: <em>h</em> = 12 m e α = 45°•opção III: <em>h</em> = 18 m e α = 60°") + p(T(148, 5), T(148, 6)),
  alts=FR("\\frac{22\\sqrt{3}}{3}", "11\\sqrt{2}", "12\\sqrt{2}", "12\\sqrt{3}", "22"))
X(149, "Escala", "<p>Na tela, a maior altitude do voo corresponde a 1 quadradinho, ou seja, 1 cm. Esse 1 cm representa 5 km = 500 000 cm. A escala é <strong>1 : 500 000</strong>. Alternativa <strong>E</strong>.</p><p>1 : 5 (A) não converte km em cm; 1 : 5 000 (D) converte só até metros.</p>",
  figs(("q149", "Tela quadriculada com eixos “Altitude” e “Distância”. A linha do voo sai da origem, sobe até a altura de 1 quadradinho, segue na horizontal, desce um pouco, segue mais um trecho e volta ao solo no destino.")),
  ["escala", "conversão de unidades"])
X(150, "Funções", "<p>Ao fim da primeira hora, a concentração é 90% da quantidade ingerida: C = 0,9 · q, ou <strong>C = 0,9q</strong>. Alternativa <strong>A</strong>.</p><p>C = 0,1q (B) seria a parte que não está no sangue; as outras expressões não representam uma porcentagem de q.</p>",
  tags=["função linear", "porcentagem"],
  alts={k: v.replace("q", "<em>q</em>").replace("C =", "<em>C</em> =") for k, v in D[150]["alternativas"].items()})
X(151, "Gráficos", "<p>Cada ponto tem coordenadas (valor de A, valor de B). A está mais valorizada quando a abscissa é maior que a ordenada. Lendo o gráfico: 9 h (3; 0,5), 12 h (5,5; 3), 13 h (6; 1,5) e 14 h (3,5; 2) têm A &gt; B. Às 10 h (2; 2) e às 11 h (4; 4) os valores são iguais, e às 15 h, 16 h e 17 h B é maior. São <strong>4 instantes</strong>. Alternativa <strong>B</strong>.</p>",
  figs(("q151", "Gráfico com o valor da criptomoeda A (milhar de real) no eixo horizontal e o da criptomoeda B no vertical. Uma curva liga nove pontos: 9 h (3; 0,5), 10 h (2; 2), 11 h (4; 4), 12 h (5,5; 3), 13 h (6; 1,5), 14 h (3,5; 2), 15 h (2,5; 4), 16 h (1; 5) e 17 h (0,5; 3,5).")),
  ["leitura de gráfico", "plano cartesiano"],
  enun=p(T(151, 0)) + "[[fig:1]]" + p(T(151, 3).replace("Criptomoeda A (milhar de real) ", ""), T(151, 4)))
X(152, "Logaritmos", "<p>N = log I¹⁰ − log I₀¹⁰ = 10 · log(I ÷ I₀) = 10 · log(8 · 10⁻⁸ ÷ 10⁻¹²) = 10 · log(8 · 10⁴) = 10 · (3 · 0,3 + 4) = 10 · 4,9 = 49 dB. Como 49 está entre 48 e 55, o som é moderado, e a medida é a <strong>II</strong>. Alternativa <strong>B</strong>.</p>",
  tags=["propriedades dos logaritmos", "decibel"],
  enun=ap("A exposição a alguns níveis sonoros pode causar lesões auditivas. Por isso, em uma indústria, são adotadas medidas preventivas de acordo com a máquina que o funcionário opera e o nível <em>N</em> de intensidade do som, medido em decibel (dB), a que o operário é exposto, sendo \\(N = \\log_{10} I^{10} - \\log_{10} I_0^{10}\\), <em>I</em> a intensidade do som e \\(I_0 = 10^{-12}\\ \\text{W/m}^2\\).")
       + fonte(T(152, 2)) + p(T(152, 3).replace("nível N", "nível <em>N</em>"), "Uma nova máquina, com \\(I = 8 \\times 10^{-8}\\ \\text{W/m}^2\\), foi adquirida e será classificada de acordo com o nível de ruído que produz.", "Considere 0,3 como aproximação para \\(\\log_{10} 2\\).", T(152, 6)))
X(153, "Razão e proporção", "<p>O tempo de espera em cada caixa é o número de pessoas na fila vezes o tempo de atendimento: I = 5 · 12 = 60 min; II = 9 · 6 = 54 min; III = 6 · 5 = 30 min; IV = 2 · 15 = 30 min; V = 3 · 9 = 27 min. O menor tempo é o do caixa <strong>V</strong>. Alternativa <strong>E</strong>.</p><p>O caixa IV tem a menor fila e o III o atendimento mais rápido, mas nenhum dos dois dá a menor espera.</p>",
  tags=["multiplicação", "otimização"],
  enun=p(T(153, 0)) + LISTA(T(153, 1)) + p(T(153, 2)))
X(154, "Geometria plana", "<p>O centro da lua coincide com um vértice do telhado, e os dois lados do triângulo que saem desse vértice são raios da circunferência. A parte escondida é limitada por dois raios e um arco: é um <strong>setor circular</strong> (de 60°, o ângulo do triângulo equilátero). Alternativa <strong>B</strong>.</p><p>O segmento circular (C) seria limitado por uma corda e um arco; o arco (E) é só a linha curva.</p>",
  figs(("q154", "Quadro com a silhueta cinza de três torres de castelo com telhados triangulares; atrás da torre mais alta, uma lua cheia circular, com o centro no vértice superior do telhado dessa torre.")),
  ["setor circular"], enun=p(T(154, 0)) + "[[fig:1]]" + p(T(154, 2)))
X(155, "Geometria plana", "<p>A piscina tem 400 m², ou seja, lado 20 m. Com a calçada de 5 m de cada lado, o quadrado total tem lado 30 m e área 900 m². A calçada ocupa 900 − 400 = <strong>500 m²</strong>. Alternativa <strong>D</strong>.</p><p>900 m² (B) é a área total; 400 m² (E) somaria só 4 faixas de 20 m × 5 m, esquecendo os cantos.</p>",
  figs(("q155", "Planta baixa: piscina quadrada azul no centro, cercada por uma calçada cinza de 5 m de largura em todos os lados.")),
  ["área de quadrados"], enun=p(T(155, 0).replace("400 m²", "400 m<sup>2</sup>")) + "[[fig:1]]" + p(T(155, 3).replace("metro quadrado", "metro quadrado")),
  alts=D[155]["alternativas"])
X(156, "Gráficos", "<p>O celular fica sem sinal nos trechos em que o gráfico está no zero: de 10 a 12 min (2 min) e de 16 a 20 min (4 min). No total, <strong>6 minutos</strong>. Alternativa <strong>A</strong>.</p><p>Em 14 min o sinal volta rapidamente (pico), então não se pode juntar os dois trechos num só de 10 min (C).</p>",
  figs(("q156", "Gráfico da intensidade do sinal de internet em função do tempo (0 a 30 min): começa alta, cai até zero em 10 min, fica zero até 12 min, sobe num pico em 14 min, volta a zero de 16 a 20 min, sobe de novo com oscilações e termina alta em 30 min.")),
  ["leitura de gráfico"], enun=p(T(156, 0)) + "[[fig:1]]" + p(T(156, 3)))
X(157, "Estatística", "<p>Procuramos pontos à esquerda de 80 kg (massa abaixo da média) e acima de 1,65 m (altura acima da média). No gráfico, só 2 dos 10 estudantes estão nessa região (cerca de 65 kg e 1,68 m; 68 kg e 1,70 m). São 2 de 10 = <strong>20%</strong>. Alternativa <strong>B</strong>.</p><p>Os pontos exatamente em 1,65 m não estão acima da média, e os de 105 kg e 120 kg, embora altos, têm massa acima da média.</p>",
  figs(("q157", "Gráfico de dispersão “Massa corporal e altura de estudantes”: massa (kg) no eixo horizontal, de 0 a 140, e altura (m) no vertical, de 1,45 a 1,8. Dez pontos: cerca de (50; 1,60), (55; 1,65), (60; 1,65), (65; 1,68), (68; 1,70), (85; 1,65), (90; 1,63), (85; 1,50), (105; 1,75) e (120; 1,70).")),
  ["gráfico de dispersão", "média"])
X(158, "Funções", "<p>Com k ajudantes (k ≥ 1), a pesca é 300 + 100(k − 1) = 200 + 100k kg, e a receita é 5(200 + 100k). O lucro é 96% da receita menos 900 e menos 250k: 4,8(200 + 100k) − 900 − 250k = 60 + 230k. Para lucro ≥ 800: 230k ≥ 740, k ≥ 3,2. O mínimo é <strong>4 ajudantes</strong>. Alternativa <strong>D</strong>.</p><p>Com 3 ajudantes o lucro seria 750 reais, abaixo da meta.</p>",
  tags=["função afim", "lucro"])
X(159, "Funções", "<p>Os 5 litros devem ser aplicados de uma vez numa população de 5 · 200 000 = 1 000 000 de larvas. Partindo de 100 e multiplicando por 10 a cada 3 dias: 100 → 1 000 (3 dias) → 10 000 (6) → 100 000 (9) → 1 000 000 (12 dias). Alternativa <strong>D</strong>.</p><p>6 dias (C) dá só 10 000 larvas; 18 dias (E) passaria de 1 milhão.</p>",
  tags=["função exponencial"])
X(160, "Análise combinatória", "<p>São 10 + 26 + 26 + 6 = 68 caracteres e 52 letras. Tipo I: 68 · 67 · 66 · 65 ≈ 19,5 milhões de senhas. Tipo II: 52 · 51 · 50 · 10 · 6 ≈ 8 milhões. Tipo III: 52 · 51 · 10 · 9 · 6 · 5 ≈ 716 mil. Quanto mais senhas possíveis, menor a chance de acertar: p<sub>1</sub> &lt; p<sub>2</sub> &lt; p<sub>3</sub>, e o tipo I é o mais seguro. Alternativa <strong>A</strong>.</p><p>Ter mais caracteres (E) não basta: as restrições do tipo III reduzem muito as possibilidades.</p>",
  tags=["princípio multiplicativo", "probabilidade"],
  enun=p(T(160, 0)) + LISTA("algarismos de 0 a 9;•26 letras minúsculas do alfabeto;•26 letras maiúsculas do alfabeto;•6 caracteres especiais !, @, #, $, ★, &amp;.") + p(T(160, 2)) + LISTA(T(160, 3))
       + p("Considere <em>p</em><sub>1</sub>, <em>p</em><sub>2</sub> e <em>p</em><sub>3</sub> as probabilidades de se descobrirem ao acaso, na primeira tentativa, as senhas dos tipos I, II e III, respectivamente.", T(160, 5)),
  alts={k: re.sub(r"p(\d)", r"<em>p</em><sub>\1</sub>", v).replace(" < ", " &lt; ") for k, v in D[160]["alternativas"].items()})
X(161, "Matemática financeira", "<p>A prazo, o produto custa 1,2 · 1 500 = 1 800, em 3 parcelas de 600. A primeira é paga à vista; então 1 500 − 600 = 900 equivalem às outras duas trazidas ao presente: 900 = \\(\\frac{600}{1+i} + \\frac{600}{(1+i)^2}\\). Com u = \\(\\frac{1}{1+i}\\): 2u² + 2u − 3 = 0, u = \\(\\frac{-2 + \\sqrt{28}}{4}\\) ≈ \\(\\frac{3{,}29}{4}\\) ≈ 0,8225. Então 1 + i ≈ 1,215, e i ≈ <strong>21,5%</strong>. Alternativa <strong>D</strong>.</p><p>20% (C) é o acréscimo total, não a taxa mensal de juros compostos.</p>",
  tags=["juros compostos", "equação do 2º grau"],
  enun=p(T(161, 0), T(161, 1), "Utilize 5,29 como aproximação para \\(\\sqrt{28}\\).", T(161, 3)))
X(162, "Funções", "<p>O preço tem uma parte fixa (taxa de bombeamento, R$ 500,00) e uma parte proporcional ao volume (R$ 250,00 por m³): <strong>y = 250x + 500</strong>. Alternativa <strong>D</strong>.</p><p>E inverte os papéis do valor fixo e do valor por metro cúbico; A, B e C não têm parte fixa.</p>",
  tags=["função afim"], alts={k: re.sub(r"([xy])", r"<em>\1</em>", v) for k, v in D[162]["alternativas"].items()},
  trocas=[("preço y do", "preço <em>y</em> do"), ("volume x de", "volume <em>x</em> de"), ("preço y em função do volume x,", "preço <em>y</em> em função do volume <em>x</em>,")])
X(163, "Funções", "<p>Pelo gráfico, a distância à base cresce de 0 a 3 km nos primeiros 10 minutos (o vigilante se afasta em linha reta), fica constante em 3 km por 10 minutos (ele anda sobre um arco de circunferência de raio 3 km com centro na base) e volta a 0 nos últimos 10 minutos (retorno em linha reta). A trajetória é um setor circular: a representação <strong>A</strong>. Alternativa <strong>A</strong>.</p><p>Em B e D há trechos retos em que a distância à base não seria constante; em C e E o trajeto não começa e termina na base do mesmo jeito.</p>",
  figs(("q163", "Gráfico “Distância do vigilante em relação à base em função do tempo”: a distância (km) sobe em linha reta de 0 a 3 km entre 0 e 10 min, fica em 3 km de 10 a 20 min e desce em linha reta até 0 em 30 min."),
       ("q163a", "Trajeto A: setor circular — um segmento reto saindo de um ponto, um arco de circunferência e outro segmento reto de volta ao ponto, com setas indicando o sentido."),
       ("q163b", "Trajeto B: triângulo com o vértice embaixo — um segmento reto subindo, um segmento horizontal em cima e outro descendo de volta ao vértice."),
       ("q163c", "Trajeto C: um “V” invertido — um segmento subindo até o topo e outro descendo, sem voltar ao ponto de partida."),
       ("q163d", "Trajeto D: um trapézio aberto — segmento subindo, segmento horizontal em cima e segmento descendo, sem fechar."),
       ("q163e", "Trajeto E: semicírculo — o arco de cima percorrido e o diâmetro embaixo, com setas e um ponto no meio do diâmetro.")),
  ["leitura de gráfico", "circunferência"], alts=ALT(2),
  enun=p(T(163, 0)) + "[[fig:1]]" + p(T(163, 4)))
X(164, "Estatística", "<p>Pela análise do Treineiros, a categoria mais exposta ao vírus seria a menos imunizada. No gráfico, a menor barra (fora os trabalhadores da saúde, já com 100%) é a dos <strong>adultos entre 20 e 29 anos</strong>, com cerca de 41%. Alternativa <strong>D</strong>, se a questão não tivesse sido anulada.</p>",
  figs(("q164", "Gráfico de barras horizontais “Números da campanha contra a gripe A-H1N1”, com o percentual de imunização de 0% a 100%: adultos entre 20 e 29 anos, cerca de 41%; gestantes, cerca de 53%; doentes crônicos, cerca de 55%; indígenas, cerca de 64%; crianças de 6 meses a 2 anos, cerca de 86%; trabalhadores da saúde, 100%.")),
  ["leitura de gráfico"], anulacao={"fonte": "oficial", "motivo": ANUL},
  enun=p(T(164, 0)) + "[[fig:1]]" + fonte("<em>Época</em>, 26 abr. 2010 (adaptado).") + p(T(164, 5)))
X(165, "Geometria plana", "<p>Pisos: 3 retângulos de 1,0 m × 0,25 m = 0,75 m². Espelhos: 3 retângulos de 1,0 m × 0,20 m = 0,60 m². Cada parede lateral é a “escadinha” formada por retângulos de 0,25 m de largura e alturas 0,60, 0,40 e 0,20 m: 0,25 · 1,20 = 0,30 m²; as duas paredes somam 0,60 m². Total: 0,75 + 0,60 + 0,60 = <strong>1,95 m²</strong>. Alternativa <strong>E</strong>.</p><p>1,35 m² (B) esquece as paredes laterais; 1,65 m² (C) conta só uma delas.</p>",
  figs(("q165", "Escada de concreto com três degraus encostada numa parede, junto a uma porta. Cada degrau tem piso de 0,25 m de profundidade e espelho de 0,20 m de altura; a largura da escada é 1,0 m. As paredes laterais da escada têm forma de escadinha.")),
  ["área de retângulos"], enun=p(T(165, 0)) + "[[fig:1]]" + p(T(165, 2), T(165, 3)))
X(166, "Matrizes e tabelas", "<p>Gasto de cada dia (horas × cal/h): segunda: 0,5 · 764 + 2 · 492 + 1 · 248 = 1 614; terça: 0,5 · 248 + 764 + 0,5 · 356 + 492 = 1 558; quarta: 1,5 · 764 + 356 + 0,5 · 492 = 1 748; quinta: 2 · 764 = 1 528; sexta: 0,5 · 764 + 2,5 · 492 = 1 612. O maior gasto é na <strong>quarta-feira</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["produto de matrizes", "tabelas"],
  enun=p(T(166, 0)) + tabela(["Dias da semana", "Caminhar", "Correr", "Andar de bicicleta", "Jogar futebol"],
                              [["Segunda-feira", "1,0", "0,5", "0,0", "2,0"], ["Terça-feira", "0,5", "1,0", "0,5", "1,0"], ["Quarta-feira", "0,0", "1,5", "1,0", "0,5"], ["Quinta-feira", "0,0", "2,0", "0,0", "0,0"], ["Sexta-feira", "0,0", "0,5", "0,0", "2,5"]])
       + p(T(166, 2)) + tabela(["Atividade física", "Caminhar", "Correr", "Andar de bicicleta", "Jogar futebol"], [["Gasto calórico (cal/h)", "248", "764", "356", "492"]]) + p(T(166, 4)))
X(167, "Porcentagem", "<p>Pela proporção, são 5 folhas por aluno: 1 150 · 5 = 5 750 folhas, ou 57,5 embalagens. Como só se vendem embalagens inteiras, são 58, ao preço de 58 · 4 = R$ 232,00. Com R$ 220,00, o desconto precisa ser de 12 ÷ 232 ≈ 5,17%, no intervalo <strong>(5,0; 5,5)</strong>. Alternativa <strong>A</strong>.</p><p>Usar 57,5 embalagens (R$ 230,00) daria cerca de 4,3%, fora de todos os intervalos.</p>",
  tags=["proporção", "desconto"])
X(168, "Probabilidade", "<p>Para o número 50: a unidade 0 sai com chance \\(\\frac{1}{10}\\); depois, as dezenas possíveis com unidade 0 (10, 20, 30, 40, 50) são 1 a 5, e a chance do 5 é \\(\\frac{1}{5}\\): total \\(\\frac{1}{50}\\). Para o 02: a unidade 2 sai com \\(\\frac{1}{10}\\); as dezenas possíveis (02, 12, 22, 32, 42, 52) são 0 a 5, e a chance do 0 é \\(\\frac{1}{6}\\): total \\(\\frac{1}{60}\\). Alternativa <strong>A</strong>.</p>",
  tags=["probabilidade condicional"], enun=p(T(168, 0), T(168, 1)),
  alts=FR("\\frac{1}{50} \\text{ e } \\frac{1}{60}", "\\frac{1}{50} \\text{ e } \\frac{1}{50}", "\\frac{1}{50} \\text{ e } \\frac{1}{10}", "\\frac{1}{55} \\text{ e } \\frac{1}{54}", "\\frac{1}{100} \\text{ e } \\frac{1}{100}"))
X(169, "Progressões", "<p>A cada metro, a intensidade é multiplicada por \\(\\frac{2}{3}\\): L<sub>0</sub>, \\(\\frac{2}{3}\\)L<sub>0</sub>, \\(\\frac{4}{9}\\)L<sub>0</sub>, \\(\\frac{8}{27}\\)L<sub>0</sub>… É uma PG de razão \\(\\frac{2}{3}\\). A 6 m: \\(\\left(\\frac{2}{3}\\right)^6 L_0 = \\frac{64}{729} L_0\\). Alternativa <strong>D</strong>.</p><p>\\(\\frac{128}{2187}\\) (E) seria a 7 m; \\(\\frac{32}{243}\\) (C), a 5 m.</p>",
  figs(("q169", "Esquema com setas para baixo: à profundidade 0 m, intensidade L₀; a 1 m, (2/3)L₀; a 2 m, (4/9)L₀; a 3 m, (8/27)L₀. As setas ficam mais curtas com a profundidade.")),
  ["progressão geométrica"],
  enun=p("O esquema mostra como a intensidade luminosa decresce com o aumento da profundidade em um rio, sendo L<sub>0</sub> a intensidade na sua superfície.") + "[[fig:1]]" + p(T(169, 4), T(169, 5)),
  alts=FR("\\frac{1}{9} L_0", "\\frac{16}{27} L_0", "\\frac{32}{243} L_0", "\\frac{64}{729} L_0", "\\frac{128}{2187} L_0"))
X(170, "Funções", "<p>V(x) = \\(\\frac{x^2}{4}\\) − 10x + 105 é uma parábola com concavidade para cima; o mínimo está no vértice, x = \\(\\frac{10}{2 \\cdot \\frac{1}{4}}\\) = 20, dentro do mês. V(20) = 100 − 200 + 105 = 5. Como 4 ≤ 5 &lt; 10, o desempenho é <strong>ruim</strong>. Alternativa <strong>D</strong>.</p><p>Calcular só V(1) ou V(30) (que dão valores maiores) leva a classificações melhores, porque o mínimo está no meio do mês.</p>",
  tags=["função quadrática", "vértice da parábola"],
  enun=p("Analisando as vendas de uma empresa, o gerente concluiu que o montante diário arrecadado, em milhar de real, poderia ser calculado pela expressão \\(V(x) = \\frac{x^2}{4} - 10x + 105\\), em que os valores de <em>x</em> representam os dias do mês, variando de 1 a 30.",
           "Um dos fatores para avaliar o desempenho mensal da empresa é verificar qual é o menor montante diário V<sub>0</sub> arrecadado ao longo do mês e classificar o desempenho conforme as categorias apresentadas a seguir, em que as quantidades estão expressas em milhar de real.")
       + LISTA("Ótimo: V<sub>0</sub> ≥ 24•Bom: 20 ≤ V<sub>0</sub> &lt; 24•Normal: 10 ≤ V<sub>0</sub> &lt; 20•Ruim: 4 ≤ V<sub>0</sub> &lt; 10•Péssimo: V<sub>0</sub> &lt; 4") + p(T(170, 4)))
X(171, "Razão e proporção", "<p>20 ciclos de 52 anos Haab são 1 040 anos Haab, ou 1 040 · 365 = 379 600 dias. Em anos Tzolkim, de 260 dias: 379 600 ÷ 260 = <strong>1 460</strong>. Alternativa <strong>C</strong>.</p><p>1 040 (B) é o número de anos Haab, sem converter.</p>",
  tags=["conversão de unidades"])
X(172, "Geometria plana", "<p>Pela lei dos cossenos, a² = b² + c² − 2bc · cos α. A área de um círculo é proporcional ao quadrado do diâmetro. A pizza do professor é maior que a soma das outras quando a² &gt; b² + c², isto é, quando cos α &lt; 0. Num triângulo, isso acontece com o ângulo obtuso: <strong>90° &lt; α &lt; 180°</strong>. Alternativa <strong>C</strong>.</p><p>α = 90° (B) daria igualdade (teorema de Pitágoras), e ângulo agudo (A) daria área menor.</p>",
  figs(("q172a", "Triângulo retângulo cinza com hipotenusa a e catetos b e c; sobre cada lado há um círculo com aquele lado como diâmetro: círculo C₁ (sobre a), C₂ (sobre b) e C₃ (sobre c)."),
       ("q172b", "Três meias pizzas encostadas formando um triângulo com seus diâmetros: a meia pizza do professor de matemática no lado maior e as dos amigos 1 e 2 nos outros lados; α é o ângulo do triângulo oposto ao diâmetro da pizza do professor.")),
  ["lei dos cossenos", "área do círculo"],
  enun=p("Sejam <em>a</em>, <em>b</em> e <em>c</em> as medidas dos lados de um triângulo retângulo, tendo <em>a</em> como medida da hipotenusa. Esses valores <em>a</em>, <em>b</em> e <em>c</em> são, respectivamente, os diâmetros dos círculos C<sub>1</sub>, C<sub>2</sub> e C<sub>3</sub>, como apresentados na figura.")
       + "[[fig:1]]" + p("Observe que essa construção assegura, pelo teorema de Pitágoras, que área (C<sub>1</sub>) = área (C<sub>2</sub>) + área (C<sub>3</sub>).", T(172, 5)) + "[[fig:2]]"
       + p(T(172, 9).replace("ângulo a,", "ângulo α,"), T(172, 10)),
  alts={"A": "0° &lt; α &lt; 90°", "B": "α = 90°", "C": "90° &lt; α &lt; 180°", "D": "α = 180°", "E": "180° &lt; α &lt; 360°"})
X(173, "Grandezas e medidas", "<p>A economia de corrida é o consumo de oxigênio por minuto (mL/min) dividido pela massa (kg): \\(\\frac{\\text{mL/min}}{\\text{kg}} = \\frac{\\text{mL}}{\\text{min} \\cdot \\text{kg}}\\). Alternativa <strong>B</strong>.</p><p>As outras alternativas invertem a razão ou põem o minuto ou a massa no lugar errado da fração.</p>",
  tags=["unidades de medida", "razão"],
  trocas=[("visando melhorar sua performance", "visando melhorar sua <em>performance</em>")],
  alts=FR("\\frac{\\text{min}}{\\text{mL} \\cdot \\text{kg}}", "\\frac{\\text{mL}}{\\text{min} \\cdot \\text{kg}}", "\\frac{\\text{min} \\cdot \\text{mL}}{\\text{kg}}", "\\frac{\\text{min} \\cdot \\text{kg}}{\\text{mL}}", "\\frac{\\text{mL} \\cdot \\text{kg}}{\\text{min}}"))
X(174, "Geometria plana", "<p>A estrela está na escada da esquerda, na altura da fileira E. Subindo mais quatro fileiras para o norte, a pessoa chega à fileira I. Olhando para a direita (leste), a primeira poltrona depois da escada é a 4, a segunda a 5 e a terceira a <strong>6</strong>: a poltrona é a <strong>I6</strong>. Alternativa <strong>E</strong>.</p><p>H (B e C) é contar a fileira da estrela como uma das quatro; I1 (D) olha para a esquerda.</p>",
  figs(("q174", "Mapa do cinema: fileiras A a J de baixo para cima, a tela embaixo e a entrada à esquerda. As poltronas 1 a 3 ficam à esquerda de uma escada; 4 a 9 entre duas escadas; 10 a 12 à direita da segunda escada. Uma estrela marca uma posição na primeira escada, na altura da fileira E. Uma rosa dos ventos indica o norte para cima e o leste para a direita.")),
  ["localização", "pontos cardeais"], enun=p(T(174, 0)) + "[[fig:1]]" + p(T(174, 2), T(174, 3)))
X(175, "Sistemas lineares", "<p>Sejam a e v os preços de um tíquete azul e de um vermelho. Duas cartelas azuis e uma vermelha: 18a + 9v = 32,40. E a − v = v + 0,05, ou a = 2v + 0,05. Substituindo: 18(2v + 0,05) + 9v = 32,40 → 45v + 0,90 = 32,40 → v = 0,70. Uma cartela vermelha custa 9 · 0,70 = <strong>R$ 6,30</strong>. Alternativa <strong>B</strong>.</p><p>R$ 13,05 seria a cartela azul (a = 1,45), que não está entre as alternativas.</p>",
  tags=["sistema de equações"], enun=p(T(175, 0), T(175, 1)), alts={**D[175]["alternativas"], "E": "10,65"})
X(176, "Sequências", "<p>Os números pentagonais são 1, 5, 12, 22, 35, 51…, e as diferenças entre termos seguidos são 4, 7, 10, 13, 16, crescendo de 3 em 3. As próximas diferenças são 19 e 22: o 7º é 51 + 19 = 70 e o 8º é 70 + 22 = <strong>92</strong>. (Pela fórmula, \\(\\frac{n(3n-1)}{2} = \\frac{8 \\cdot 23}{2} = 92\\).) Alternativa <strong>E</strong>.</p>",
  figs(("q176", "Números pentagonais desenhados com pontos formando pentágonos encaixados: 1 (um ponto), 5, 12, 22, 35 e 51.")),
  ["números figurados", "progressão aritmética de 2ª ordem"],
  enun=p(T(176, 0)) + "[[fig:1]]" + p("O oitavo número pentagonal é"))
X(177, "Trigonometria", "<p>A roda gira com velocidade angular constante, e a altura da cadeira varia como uma função cosseno: começa no máximo (topo), desce suavemente até o mínimo e volta, repetidamente, com curvas arredondadas tanto no topo quanto embaixo. Esse é o gráfico <strong>A</strong>. Alternativa <strong>A</strong>.</p><p>B e C têm trechos retos (velocidade vertical constante); D e E têm “bicos” em cima ou embaixo, o que não acontece num movimento circular uniforme.</p>",
  figs(("q177", "Roda-gigante com oito cadeiras vermelhas, apoiada no solo; a pessoa P está na cadeira do ponto mais alto, e uma seta indica a rotação no sentido horário."),
       ("q177a", "Gráfico A: altura em função do tempo, curva ondulada suave (senoidal), começando no topo."),
       ("q177b", "Gráfico B: altura em função do tempo em zigue-zague de retas, começando no topo."),
       ("q177c", "Gráfico C: altura em função do tempo em retas que descem, ficam um pouco no fundo, sobem e ficam um pouco no topo."),
       ("q177d", "Gráfico D: altura em função do tempo com arcos arredondados em cima e bicos embaixo."),
       ("q177e", "Gráfico E: altura em função do tempo com arcos arredondados embaixo e bicos em cima.")),
  ["funções trigonométricas", "movimento circular"], alts=ALT(2),
  enun=p(T(177, 0)) + "[[fig:1]]" + p(T(177, 3), "O gráfico que melhor representa a variação dessa altura, em função do tempo, contado a partir do instante em que a cadeira da pessoa P se encontra na posição mais alta da roda-gigante, é"))
X(178, "Funções", "<p>Com vazão constante, o volume acumulado cresce em linha reta enquanto a água corre (0 a 3 s), fica constante (sem cair) enquanto a torneira está fechada (3 a 8 s) e volta a crescer com a mesma inclinação de 8 a 11 s. Esse é o gráfico <strong>B</strong>. Alternativa <strong>B</strong>.</p><p>A, C e E mostram o volume acumulado voltando a zero, o que é impossível; D cresce sem parar.</p>",
  figs(("q178a", "Gráfico A: o volume sobe de 0 a 3 s, cai a zero e fica em zero de 3 a 8 s, e volta a subir, a partir de um valor alto, de 8 a 11 s."),
       ("q178b", "Gráfico B: o volume sobe em linha reta de 0 a 3 s, fica constante de 3 a 8 s e volta a subir com a mesma inclinação de 8 a 11 s."),
       ("q178c", "Gráfico C: o volume fica constante num valor de 0 a 3 s, zero de 3 a 8 s e de novo constante no mesmo valor de 8 a 11 s."),
       ("q178d", "Gráfico D: o volume sobe em linha reta de 0 a 11 s, sem pausa."),
       ("q178e", "Gráfico E: o volume sobe de 0 a 3 s, cai a zero de 3 a 8 s e sobe de 8 a 11 s, partindo de zero, com inclinação maior.")),
  ["leitura de gráfico", "taxa de variação"], alts=ALT(1),
  enun=p(T(178, 0).replace("( t )", "(<em>t</em>)"), T(178, 1).replace("( t )", "(<em>t</em>)")))
X(179, "Sistemas de numeração", "<p>No quadrinho: 1 = urapum, 2 = okosa, 3 = okosa urapum, 4 = okosa okosa, 6 = okosa okosa okosa. A contagem é feita de dois em dois (okosa) e um (urapum). Então 5 = <strong>okosa okosa urapum</strong> e 7 = <strong>okosa okosa okosa urapum</strong>. Alternativa <strong>C</strong>.</p><p>B e E erram o 7 (8 = okosa okosa okosa okosa); A e D usam vários urapum, o que o padrão não faz.</p>",
  figs(("q179", "Quadrinho em preto e branco: seis figuras dançando sobre os números 1 a 6, cada uma com um balão: 1, “Urapum!”; 2, “Okosa!”; 3, “Okosa urapum!”; 4, “Okosa okosa!”; 5, “?”; 6, “Okosa okosa okosa!”.")),
  ["sistemas de numeração", "padrões"])
X(180, "Estatística", "<p>Médias de dois meses seguidos: out–nov (250 + 150) ÷ 2 = 200; nov–dez 175; dez–jan (200 + 450) ÷ 2 = 325; jan–fev 275; fev–mar 150. A maior média é a de dezembro e janeiro, então o plantio deve ser no início de <strong>dezembro</strong>. Alternativa <strong>C</strong>.</p><p>Janeiro (D) é o mês mais chuvoso, mas fevereiro, o seguinte, é o mais seco.</p>",
  tags=["média aritmética"],
  enun=p(T(180, 0)) + LISTA(T(180, 1).split(" Com base")[0]) + p("Com base" + T(180, 1).split(" Com base")[1], T(180, 2)))

completar(Q, R)
