# Enem 2016, 2º dia, caderno azul: Matemática (questões 136 a 180; no site, 1 a 45).
# Texto legível. Frações em KaTeX nas alternativas curtas; quadros em tabela HTML. Alternativas-imagem nas Q155 e Q178.
# Sem anuladas nesta área.

import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, paragrafos_enem

ID = "enem-2016-matematica"
META = {"id": ID, "banca": "Enem", "ano": 2016, "titulo": "Enem 2016: Matemática", "fonte": "Inep", "dataExame": "2016-11-06",
        "duracaoMinutos": 150, "area": "Matemática", "caderno": "azul", "dia": 2}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2016-dia2-azul")
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


X(136, "Geometria espacial", "<p>O silo é um cilindro de raio 3 m e altura 12 m com um cone de altura 3 m em cima:</p><ul><li>cilindro: π · 3² · 12 = 3 · 9 · 12 = 324 m³;</li><li>cone: (1/3) · π · 3² · 3 = 27 m³.</li></ul><p>Total: 351 m³. Com 20 m³ por viagem: 351 ÷ 20 = 17,55, então são necessárias <strong>18 viagens</strong>. Alternativa <strong>D</strong>.</p><p>17 viagens (C) deixariam grãos no silo.</p>",
  figs(("q136", "Três silos iguais, cada um formado por um cilindro com um cone em cima; no da frente, a altura do cilindro é 12 m, a altura do cone é 3 m e o raio da base é 3 m.")),
  ["volume do cilindro", "volume do cone"], enun=p(T(136, 0).replace("20 m³", "20 m³")) + "[[fig:1]]" + p(T(136, 3).replace("para p.", "para π.")))
X(137, "Escala", "<p>Na escala 1 : 8, o desenho mede 220 ÷ 8 = 27,5 cm, 120 ÷ 8 = 15 cm e 50 ÷ 8 = 6,25 cm. Reduzindo 20%, multiplica-se por 0,8: <strong>22,00 cm, 12,00 cm e 5,00 cm</strong>. Alternativa <strong>A</strong>.</p><p>27,50; 15,00 e 6,25 (B) são as medidas antes da redução.</p>",
  tags=["escala", "porcentagem"])
X(138, "Grandezas e medidas", "<p>443 pés × 12 = 5 316 polegadas; × 2,54 = 13 502,64 cm ≈ 135 m. Alternativa <strong>D</strong>.</p><p>Esquecer o fator 12 (pés para polegadas) dá cerca de 11 m, muito abaixo de todas as opções. Convém lembrar que 1 pé ≈ 30,5 cm, então 443 pés ficam um pouco acima de 443 × 0,3 ≈ 133 m, o que confirma a ordem de grandeza.</p>",
  figs(("q138", "Foto da roda-gigante London Eye, com uma seta indicando o diâmetro da roda.")), ["conversão de unidades"],
  enun=p(T(138, 0)) + "[[fig:1]]" + fonte(T(138, 2)) + p(T(138, 3)))
X(139, "Função afim", "<p>Na primeira hora, só uma bomba baixou o volume de 6 000 para 5 000 L: vazão de 1 000 L/h. Nas duas horas seguintes, as duas juntas tiraram 5 000 L: 2 500 L/h. A segunda bomba tem vazão de 2 500 − 1 000 = <strong>1 500 L/h</strong>. Alternativa <strong>C</strong>.</p><p>2 500 L/h (E) é a vazão das duas bombas juntas.</p>",
  figs(("q139", "Gráfico do volume (L) em função do tempo (h): segmento de A (0; 6 000) a B (1; 5 000) e segmento de B a C (3; 0).")),
  ["taxa de variação", "vazão"], enun=p(T(139, 0)) + "[[fig:1]]" + p(T(139, 4)))
X(140, "Estatística", "<p>A regularidade dos “pesos” é medida pelo desvio padrão: quanto menor, mais regular. O mais regular é o atleta III (4,08) e o menos regular, o II (8,49). A primeira luta é entre <strong>II e III</strong>. Alternativa <strong>C</strong>.</p><p>Média e mediana não medem a regularidade.</p>",
  tags=["desvio padrão", "dispersão"],
  enun=p(T(140, 0)) + tabela(["Atleta", "1ª pesagem (kg)", "2ª pesagem (kg)", "3ª pesagem (kg)", "Média", "Mediana", "Desvio padrão"],
                             [["I", "78", "72", "66", "72", "72", "4,90"], ["II", "83", "65", "65", "71", "65", "8,49"], ["III", "75", "70", "65", "70", "70", "4,08"], ["IV", "80", "77", "62", "73", "77", "7,87"]]) + p(T(140, 2)),
  alts={"A": "I e III.", "B": "I e IV.", "C": "II e III.", "D": "II e IV.", "E": "III e IV."})
X(141, "Porcentagem", "<p>A altura é a largura × de ÷ 100:</p><ul><li>175/65: 113,75 mm;</li><li>175/75: 131,25 mm;</li><li>175/80: 140 mm;</li><li>185/60: 111 mm;</li><li>205/55: 112,75 mm.</li></ul><p>A menor altura é a do <strong>185/60R15</strong>. Alternativa <strong>E</strong>.</p><p>O menor “de” (55) não basta: a largura 205 aumenta a altura.</p>",
  figs(("q141", "Um pneu visto de frente, com a largura indicada, e o mesmo pneu de lado, com a altura da borracha e o diâmetro interno indicados.")),
  ["porcentagem", "leitura de código"],
  enun=p(T(141, 0).replace("tipo abc/deRfg,", "tipo <em>abc</em>/<em>de</em>R<em>fg</em>,")) + LISTA(T(141, 1).split(" A figura")[0]) + p("A figura" + T(141, 1).split(" A figura")[1]) + "[[fig:1]]" + p(T(141, 5), T(141, 6)))
X(142, "Geometria analítica", "<p>Só se anda na vertical e na horizontal, e a distância é a soma dos quarteirões nas duas direções. No cruzamento da rua 4 com a rua D:</p><ul><li>até rua 6 com E: 2 + 1 = 3;</li><li>até rua 2 com E: 2 + 1 = 3;</li><li>até rua 4 com A: 0 + 3 = 3.</li></ul><p>As três distâncias são iguais: <strong>4 e D</strong>. Alternativa <strong>C</strong>.</p><p>Em 4 e C (B), a escola fica a 2 quarteirões e os outros dois locais a 4.</p>",
  figs(("q142", "Malha de ruas: seis ruas horizontais, de A (em cima) a F (embaixo), cruzando seis ruas verticais, de 1 (à esquerda) a 6 (à direita), formando quarteirões quadrados iguais.")),
  ["distância na malha", "plano cartesiano"], enun=p(T(142, 0)) + "[[fig:1]]" + p(T(142, 3)))
X(143, "Equação do 2º grau", "<p>A Figura B é o triângulo retângulo de catetos 15 e 15 (área 112,5 m²) mais um triângulo retângulo de catetos 21 e 3, encostado na hipotenusa (área 31,5 m²): 144 m². Confere: 15² + 15² = 450 = 21² + 3².</p><p>Para o retângulo: x(x + 7) = 144 → x² + 7x − 144 = 0 → x = 9. Medidas: <strong>9,0 e 16,0</strong>. Alternativa <strong>B</strong>.</p>",
  figs(("q143", "Figura A: retângulo de lados x e x + 7. Figura B: quadrilátero com um lado vertical de 15 m, a base de 15 m formando ângulo reto com ele, um lado de 3 m e um lado inclinado de 21 m, com ângulo reto entre os lados de 21 m e 3 m.")),
  ["área", "teorema de Pitágoras"], enun=p(T(143, 0)) + "[[fig:1]]" + p(T(143, 4)))
X(144, "Estatística", "<p>Média: (37 + 33 + 35 + 22 + 30 + 35 + 25) ÷ 7 = 217 ÷ 7 = 31 milhões. O lucro mais próximo de 31 é o de 30, no mês <strong>V</strong>. Alternativa <strong>D</strong>.</p><p>Os meses II (33) e VII (25) ficam a 2 e 6 milhões da média, mais longe que o mês V.</p>",
  tags=["média aritmética"],
  enun=p(T(144, 0)) + tabela(["Mês", "I", "II", "III", "IV", "V", "VI", "VII"], [["Lucro (em milhões de reais)", "37", "33", "35", "22", "30", "35", "25"]]) + p(T(144, 3)))
X(145, "Porcentagem", "<p>A empresa tem mais de 1 001 empregados: precisa de 5%. Mas cada contratação aumenta o total de funcionários. Com n contratados: 10 + n ≥ 0,05 · (1 200 + n) → 0,95n ≥ 50 → n ≥ 52,6. O mínimo é <strong>53</strong>. Alternativa <strong>E</strong>.</p><p>50 (5% de 1 200 menos os 10 atuais) não basta, porque o total passa a ser 1 250.</p>",
  tags=["porcentagem", "inequação"],
  enun=p(T(145, 0)) + ap("<em>" + T(145, 1) + "</em>", "<em>" + "<br>".join(re.sub(r"\.{3,}", " … ", T(145, i)) for i in range(2, 6)) + "</em>") + fonte(T(145, 6)) + p(T(145, 7), T(145, 8), T(145, 9)))
X(146, "Porcentagem", "<p>No primeiro dia: 4 caixas × R$ 16,00 = R$ 64,00 por 80 picolés; com lucro de R$ 40,00, a receita foi R$ 104,00. No segundo dia, o lucro deve ser 20% maior: R$ 48,00, e a receita, 64 + 48 = R$ 112,00.</p><p>112 ÷ 80 = <strong>R$ 1,40</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["lucro", "porcentagem"])
X(147, "Análise combinatória", "<p>Total de duplas: " + K("C_{10,2} = \\tfrac{10!}{2! \\times 8!} = 45") + ". Duplas só de canhotos: " + K("C_{4,2} = \\tfrac{4!}{2! \\times 2!} = 6") + ". As possibilidades são 45 − 6 = 39: " + K("\\tfrac{10!}{2! \\times 8!} - \\tfrac{4!}{2! \\times 2!}") + ". Alternativa <strong>A</strong>.</p><p>A expressão de B conta a ordem dos jogadores, como se A × B fosse diferente de B × A.</p>",
  tags=["combinação", "complementar"], enun=p(T(147, 0), T(147, 1)),
  alts=FR("\\dfrac{10!}{2! \\times 8!} - \\dfrac{4!}{2! \\times 2!}", "\\dfrac{10!}{8!} - \\dfrac{4!}{2!}", "\\dfrac{10!}{2! \\times 8!} - 2", "\\dfrac{6!}{4!} + 4 \\times 4", "\\dfrac{6!}{4!} + 6 \\times 4"))
X(148, "Sistema de numeração", "<p>Lendo as argolas de cada haste, da esquerda para a direita: U = 1, CM = 4, D = 7, M = 0, C = 1, DM = 6. Montando o número na ordem certa (CM, DM, M, C, D, U): 4, 6, 0, 1, 7, 1 → <strong>460 171</strong>. Alternativa <strong>D</strong>.</p>",
  figs(("q148", "Ábaco com seis hastes, cujas etiquetas, da esquerda para a direita, são U, CM, D, M, C e DM. Argolas em cada haste, na mesma ordem: 1, 4, 7, 0, 1 e 6.")),
  ["valor posicional", "ábaco"], enun=p(T(148, 0), T(148, 1)) + "[[fig:1]]" + p(T(148, 3)))
X(149, "Função afim", "<p>A parábola (projétil A) atinge a altura máxima de 16 m em t = 4 s. A reta B passa pela origem e, em t = 4 s, está a 8 m: coeficiente angular 2. Para passar por (4; 16), a reta precisa ter coeficiente 4: deve <strong>aumentar em 2 unidades</strong>. Alternativa <strong>C</strong>.</p>",
  figs(("q149", "Gráfico da altura (m) em função do tempo (s): a curva A é uma parábola que sai da origem, chega a 16 m em t = 4 s e desce até −12 m em t = 9 s; a reta B sai da origem e sobe, passando por 8 m em t = 4 s e por 18 m em t = 9 s.")),
  ["coeficiente angular", "vértice da parábola"], enun=p(T(149, 0)) + "[[fig:1]]" + p(T(149, 6)))
X(150, "Grandezas proporcionais", "<p>A espessura é k ÷ D² e o custo é proporcional ao volume, A · k ÷ D². Assim, custo = c · A ÷ D². Para A = 9 e D = 3: 500 = c · 9 ÷ 9, logo c = 500. Custo = " + K("\\dfrac{500 \\cdot A}{D^2}") + ". Alternativa <strong>B</strong>.</p>",
  tags=["proporcionalidade inversa", "expressão algébrica"], enun=p(T(150, 0)),
  alts=FR("\\dfrac{500 \\cdot 81}{A \\cdot D^2}", "\\dfrac{500 \\cdot A}{D^2}", "\\dfrac{500 \\cdot D^2}{A}", "\\dfrac{500 \\cdot A \\cdot D^2}{81}", "\\dfrac{500 \\cdot 3 \\cdot D^2}{A}"))
X(151, "Porcentagem", "<p>Pelo gráfico, aos 4 anos e 4 meses, a curva p50 está em 105 cm. A menina foi de 85 para 105 cm: aumento de 20 cm. 20 ÷ 85 ≈ 0,235 = <strong>23,5%</strong>. Alternativa <strong>A</strong>.</p><p>Dividir por 105 em vez de 85 dá 19,0% (C).</p>",
  figs(("q151", "Gráfico de crescimento de meninas: comprimento (cm), de 80 a 120, em função da idade, de 3 a 5 anos, com cinco curvas crescentes, p3, p15, p50, p85 e p97. Aos 4 anos e 4 meses, a curva p50 passa por 105 cm.")),
  ["aumento percentual", "leitura de gráfico"], enun=p(T(151, 0), T(151, 1)) + "[[fig:1]]" + fonte(T(151, 8)) + p(T(151, 9)))
X(152, "Probabilidade", "<p>Na entrada há dois caminhos (1/2 cada).</p><ul><li>Caminho de cima: na bifurcação com a área III, segue em frente (1/2); no cruzamento do alto, escolhe entre I, V e IV (1/3): 1/2 · 1/2 · 1/3 = 1/12.</li><li>Caminho de baixo: passa pela bifurcação da área II (segue, 1/2) e pela da área III (segue, 1/2) e chega a IV: 1/2 · 1/2 · 1/2 = 1/8.</li></ul><p>Total: 1/12 + 1/8 = 2/24 + 3/24 = " + K("\\tfrac{5}{24}") + ". Alternativa <strong>C</strong>.</p>",
  figs(("q152", "Mapa do parque: da entrada sai um caminho que se divide em dois. O de cima sobe, tem uma derivação para a área III no meio e chega a um cruzamento com caminhos para as áreas I, V e IV. O de baixo tem uma derivação para a área II, faz uma curva, tem outra derivação para a área III e chega à área IV.")),
  ["árvore de probabilidades"], enun=p(T(152, 0)) + "[[fig:1]]" + p(T(152, 2)), alts=FR("\\dfrac{1}{96}", "\\dfrac{1}{64}", "\\dfrac{5}{24}", "\\dfrac{1}{4}", "\\dfrac{5}{12}"))
X(153, "Estatística", "<p>Média: (237 + 262 + 158 + 159 + 160 + 278 + 300 + 278) ÷ 8 = 1 832 ÷ 8 = 229. Acima da média: Oeste, Centro, Leste, Centro-Oeste e Centro-Sul (5 regiões × 10 = 50). Até a média: Norte, Sul e Noroeste (3 × 7 = 21). Total: <strong>71</strong>. Alternativa <strong>D</strong>.</p>",
  tags=["média aritmética"],
  enun=p(T(153, 0).replace("Aedes aegypti", "<em>Aedes aegypti</em>")) + tabela(["Região", "Casos confirmados"], [["Oeste", "237"], ["Centro", "262"], ["Norte", "158"], ["Sul", "159"], ["Noroeste", "160"], ["Leste", "278"], ["Centro-Oeste", "300"], ["Centro-Sul", "278"]])
       + p(T(153, 2)) + OL(*[x.strip() for x in re.split(r"I+\. ", T(153, 3).split(" Quantos")[0]) if x.strip()]) + p("Quantos" + T(153, 3).split(" Quantos")[1]))
X(154, "Razão", "<p>Fibra por grama de pão: A 2/50 = 0,04; B 5/40 = 0,125; C 5/100 = 0,05; D 6/90 ≈ 0,067; E 7/70 = 0,1. A maior é a da marca <strong>B</strong>. Alternativa <strong>B</strong>.</p><p>A marca E tem mais fibra em números absolutos (7 g), mas numa porção maior de pão.</p>",
  tags=["razão", "comparação"], enun=p(T(154, 0)) + LISTA(T(154, 1).split(" Recomenda")[0]) + p("Recomenda" + T(154, 1).split(" Recomenda")[1]) + fonte(T(154, 2)) + p(T(154, 3)))
X(155, "Geometria espacial", "<p>Fechada, a cadeira tem os pés cruzados juntos, formando uma só faixa vertical; o assento de lona dobra e fica pendurado, e o encosto continua em cima. De lado, vê-se um retângulo alto e estreito, com o encosto preto em cima, os braços como pequenos traços e o assento como um bloco preto. É o esboço C. Alternativa <strong>C</strong>.</p><p>Os esboços com o “X” dos pés (B, D e E) mostram a cadeira ainda aberta.</p>",
  figs(("q155", "Cadeira dobrável de diretor, aberta: assento e encosto de lona preta, braços e pés de madeira cruzados em X."),
       ("q155a", "Esboço A: perfil com encosto em cima, assento preto e pés retos, com o braço curto."),
       ("q155b", "Esboço B: perfil com encosto, assento preto e pés cruzados em X embaixo."),
       ("q155c", "Esboço C: perfil estreito com encosto em cima, braço, assento preto e pés retos e paralelos."),
       ("q155d", "Esboço D: perfil com encosto, assento preto e um X entre os pés, ocupando a parte de baixo."),
       ("q155e", "Esboço E: perfil com encosto, assento preto e um quadrado com X entre os pés.")),
  ["vistas", "visão espacial"], enun=p(T(155, 0)) + "[[fig:1]]" + p(T(155, 2)), alts=ALT(2))
X(156, "Grandezas e medidas", "<p>Às 10 h, a área ocupada é 500 × 500 = 250 000 m², com 4 pessoas por m²: 1 000 000 de pessoas. Das 10 h às 16 h, chegam mais 6 × 120 000 = 720 000. Total: 1 720 000 pessoas ÷ 2 000 = <strong>860 policiais</strong>. Alternativa <strong>E</strong>.</p>",
  tags=["densidade demográfica", "taxa"])
X(157, "Estatística", "<p>Para a média dos seis meses ser pelo menos 30, a soma deve ser 180. De janeiro a maio: 21 + 35 + 21 + 30 + 38 = 145. Junho: 180 − 145 = <strong>35</strong>. Alternativa <strong>E</strong>.</p><p>A média dos cinco primeiros meses é 29; por isso junho precisa compensar com um valor acima de 30.</p>",
  tags=["média aritmética"], enun=p(T(157, 0)) + tabela(["Janeiro", "Fevereiro", "Março", "Abril", "Maio"], [["21", "35", "21", "30", "38"]]) + p(T(157, 2)))
X(158, "Função afim", "<p>No gráfico, o nível cai de 30% no mês 1 para 10% no mês 6: 20 pontos em 5 meses, 4% por mês. Depois do sexto mês faltam 10%, que levam 10 ÷ 4 = 2,5 meses: <strong>2 meses e meio</strong>. Alternativa <strong>A</strong>.</p>",
  figs(("q158", "Gráfico “Nível do reservatório”: porcentagem em relação à capacidade máxima, em função do mês, de 1 a 6; pontos alinhados numa reta que desce de 30% no mês 1 para 10% no mês 6.")),
  ["taxa de variação", "função afim"], enun=p(T(158, 0)) + "[[fig:1]]" + p(T(158, 4)))
X(159, "Estatística", "<p>Total aplicado em 5 meses: 21 + 22 + 25 + 31 + 21 = 120 (média 24). O estoque deve ficar em 12 × 24 = 288. Restam 228 − 120 = 108 vacinas, então é preciso comprar 288 − 108 = <strong>180</strong>. Alternativa <strong>B</strong>.</p><p>288 (E) é o estoque total desejado, sem descontar o que sobrou.</p>",
  tags=["média aritmética"], enun=p(T(159, 0)) + LISTA(T(159, 1).replace("o mês", "º mês")) + p(T(159, 2), T(159, 3)))
X(160, "Logaritmo", "<p>Depois de n períodos de 30 min: 3 000 · 0,99<sup>n</sup> = 30 → 0,99<sup>n</sup> = 0,01. Como 0,99 = 9 · 11 ÷ 100: log 0,99 = 2 · 0,477 + 1,041 − 2 = −0,005. Então n · (−0,005) = −2 → n = 400 períodos de meia hora = <strong>200 horas</strong>. Alternativa <strong>D</strong>.</p><p>400 (E) é o número de meias horas.</p>",
  tags=["função exponencial", "logaritmo"], enun=p(T(160, 0).replace("log10(3)", "log<sub>10</sub>(3)").replace("log10(11)", "log<sub>10</sub>(11)")))
X(161, "Geometria espacial", "<p>Cada compartimento tem 20 × 10 × 10 = 2 000 m³. Com o furo no fundo de C, todo o petróleo de C vaza (2 000 m³). As placas têm só 7 m de altura, então o petróleo de A e B que está acima delas também escoa para C: 2 × 20 × 10 × 3 = 1 200 m³. Total: 3 200 m³ = <strong>3,2 × 10³ m³</strong>. Alternativa <strong>D</strong>.</p>",
  figs(("q161", "Paralelepípedo de 60 m de comprimento, 10 m de largura e 10 m de altura, dividido em três compartimentos A, B e C por duas placas de 7 m de altura.")),
  ["volume do paralelepípedo"], enun=p(T(161, 0)) + "[[fig:1]]" + p(T(161, 3), T(161, 4), T(161, 5)),
  alts={k: v.replace("103 m3", "10<sup>3</sup> m<sup>3</sup>") for k, v in D[161]["alternativas"].items()})
X(162, "Gráficos", "<p>É preciso um mês e o seguinte com: variação de chuva de até 50 mm, mínima acima de 15 °C nos dois e aumento da máxima de no máximo 5 °C. De janeiro para fevereiro: a chuva vai de cerca de 145 para 130 mm (variação de 15 mm), as mínimas ficam em torno de 20 °C e 21 °C, e a máxima sobe de cerca de 27 °C para cerca de 28,5 °C. As outras opções falham: em fevereiro–março a máxima cai, em agosto as mínimas estão abaixo de 15 °C, em novembro–dezembro a máxima cai e em dezembro–janeiro a chuva varia mais de 50 mm. Alternativa <strong>A</strong>.</p>",
  figs(("q162", "Gráfico de maio de 2012 a maio de 2013 com barras de pluviosidade (mm) e linhas de temperatura máxima e mínima (°C). Chuva baixa de maio a agosto, sobe a partir de setembro, com picos de cerca de 200 mm em novembro e dezembro, cerca de 145 em janeiro, 130 em fevereiro e 150 em março, caindo depois. Máximas entre cerca de 22 e 30 °C; mínimas entre 10 °C (julho) e cerca de 21 °C (de novembro a março).")),
  ["leitura de gráfico", "condições"], enun=p(T(162, 0)) + LISTA(T(162, 1).split(" Um floricultor")[0]) + p("Um floricultor" + T(162, 1).split(" Um floricultor")[1]) + "[[fig:1]]" + p(T(162, 4), T(162, 5)),
  alts=dict(D[162]["alternativas"], E="dezembro."))  # a legenda do gráfico grudava na alternativa E
X(163, "Razão e proporção", "<p>Tomando m<sub>C</sub> = 1 e V<sub>C</sub> = 1: m<sub>B</sub> = 3/4, m<sub>A</sub> = 1,5 · 3/4 = 1,125; V<sub>A</sub> = V<sub>B</sub> = 1,2.</p><p>d<sub>A</sub> = 1,125 ÷ 1,2 ≈ 0,94; d<sub>B</sub> = 0,75 ÷ 1,2 = 0,625; d<sub>C</sub> = 1. Logo d<sub>B</sub> &lt; d<sub>A</sub> &lt; d<sub>C</sub>. Alternativa <strong>A</strong>.</p>",
  tags=["densidade", "proporção"],
  enun=p("Densidade absoluta (<em>d</em>) é a razão entre a massa de um corpo e o volume por ele ocupado. Um professor propôs à sua turma que os alunos analisassem a densidade de três corpos: <em>d</em><sub>A</sub>, <em>d</em><sub>B</sub>, <em>d</em><sub>C</sub>. Os alunos verificaram que o corpo A possuía 1,5 vez a massa do corpo B e esse, por sua vez, tinha " + K("\\tfrac{3}{4}") + " da massa do corpo C. Observaram, ainda, que o volume do corpo A era o mesmo do corpo B e 20% maior do que o volume do corpo C. Após a análise, os alunos ordenaram corretamente as densidades desses corpos da seguinte maneira"),
  alts={k: re.sub(r"d([ABC])", r"<em>d</em><sub>\1</sub>", v).replace("<", "&lt;").replace("&lt;em>", "<em>").replace("&lt;/em>", "</em>").replace("&lt;sub>", "<sub>").replace("&lt;/sub>", "</sub>") for k, v in D[163]["alternativas"].items()})
X(164, "Frações", "<p>O ponteiro está na marca de 3/4 do tanque: 3/4 × 50 = 37,5 L. Com 15 km/L, o carro anda 37,5 × 15 = 562,5 km. O último posto antes disso fica a <strong>500 km</strong>: é o mais longe que dá para ir antes de abastecer. Alternativa <strong>B</strong>.</p><p>O posto de 570 km (A) já estaria fora do alcance.</p>",
  figs(("q164", "Marcador de combustível com escala de 0 a 1/1, com a marca 1/2 no meio; o ponteiro está sobre a marca entre 1/2 e 1/1, a de 3/4.")),
  ["frações", "proporcionalidade"], enun=p(T(164, 0)) + "[[fig:1]]" + p(T(164, 2)))
X(165, "Progressão aritmética", "<p>João trabalhou nos andares ímpares (1, 3, 5, …) e Pedro nos andares 1, 4, 7, … Os dois coincidem nos andares 1, 7, 13, …, de 6 em 6. A 20ª coincidência é 1 + 19 × 6 = 115. Como ambos terminaram no último andar, o edifício tem <strong>115 andares</strong>. Alternativa <strong>D</strong>.</p>",
  tags=["PA", "múltiplos comuns"])
X(166, "Geometria analítica", "<p>Segmento de F(−1, 1) a B(1, −1): comprimento √(2² + 2²) = 2√2 ≈ 2,8 km = 2 800 m → 2 800 h.</p><p>Semicircunferência de diâmetro 2,8 km (raio 1,4 km): comprimento π · 1,4 = 4,2 km = 4 200 m → 4 200 × 0,6 = 2 520 h.</p><p>O menor tempo é <strong>2 520 h</strong>. Alternativa <strong>B</strong>.</p>",
  figs(("q166", "Plano cartesiano em quilômetros com F = (−1, 1) e B = (1, −1), ligados por um segmento que passa pela origem e por uma semicircunferência que contorna pela direita.")),
  ["distância entre pontos", "comprimento da circunferência"],
  enun=p(T(166, 0), T(166, 1).replace("coordenadas xOy", "coordenadas <em>xOy</em>")) + "[[fig:1]]" + p(T(166, 5), T(166, 6).replace("para p e", "para π e")))
X(167, "Função quadrática", "<p>A parábola y = 9 − x² corta o chão em x = −3 e x = 3: base 6 m. A altura é 9 m (em x = 0). Retângulo: 6 × 9 = 54 m². A área sob a parábola é 2/3 disso: <strong>36 m²</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["parábola", "área"],
  enun=p(T(167, 0), "<em>y</em> = 9 − <em>x</em><sup>2</sup>, sendo <em>x</em> e <em>y</em> medidos em metros.", "Sabe-se que a área sob uma parábola como esta é igual a " + K("\\tfrac{2}{3}") + " da área do retângulo cujas dimensões são, respectivamente, iguais à base e à altura da entrada do túnel.", T(167, 4)))
X(168, "Análise combinatória", "<p>Escolhem-se os 2 algarismos (10 · 10 = 10²) e as 2 letras entre 52 (maiúsculas e minúsculas: 52²). Depois, as posições: permutação de 4 símbolos com 2 repetições de “algarismo” e 2 de “letra”, " + K("\\tfrac{4!}{2! \\cdot 2!} = 6") + ". Total: " + K("10^2 \\cdot 52^2 \\cdot \\tfrac{4!}{2! \\cdot 2!}") + ". Alternativa <strong>E</strong>.</p><p>Usar 26 (D) ignora a diferença entre maiúsculas e minúsculas.</p>",
  tags=["princípio multiplicativo", "permutação com repetição"], enun=p(T(168, 0).replace("em um site,", "em um <em>site</em>,")) + fonte(T(168, 1)) + p(T(168, 2).replace("nesse site", "nesse <em>site</em>")),
  alts=FR("10^2 \\cdot 26^2", "10^2 \\cdot 52^2", "10^2 \\cdot 52^2 \\cdot \\dfrac{4!}{2!}", "10^2 \\cdot 26^2 \\cdot \\dfrac{4!}{2! \\cdot 2!}", "10^2 \\cdot 52^2 \\cdot \\dfrac{4!}{2! \\cdot 2!}"))
X(169, "Geometria analítica", "<p>A + B é a metade do quadrado 100 × 100: 5 000. Com Gini 0,3, A = 1 500 e B = 3 500. Se P = (90, y), a área B (sob a linha de (0, 0) a P e de P a (100, 100)) vale 90y/2 + 10(y + 100)/2 = 50y + 500. Então 50y + 500 = 3 500 → y = 60. Os 90% mais pobres ficam com 60%, e os 10% mais ricos com <strong>40%</strong>. Alternativa <strong>A</strong>.</p><p>60% (C) é a parcela dos 90% de menores salários.</p>",
  figs(("q169", "Gráfico com a quantidade de funcionários (%) no eixo horizontal e a massa salarial acumulada (%) no vertical, de 0 a 100. Uma linha reta vai de (0, 0) a (100, 100); abaixo dela, uma linha quebrada vai de (0, 0) até o ponto P, de abscissa 90, e daí a (100, 100). A área entre as duas linhas é A, e a área abaixo da linha quebrada é B.")),
  ["índice de Gini", "área de figuras planas"],
  enun=p(T(169, 0).replace("ponto P,", "ponto <em>P</em>,"), T(169, 1)) + "[[fig:1]]" + p("O Índice de Gini, que mede o grau de concentração de renda de um determinado grupo, pode ser calculado pela razão " + K("\\tfrac{A}{A + B}") + ", em que <em>A</em> e <em>B</em> são as medidas das áreas indicadas no gráfico.", T(169, 7)) + fonte(T(169, 8)) + p(T(169, 9)))
X(170, "Estatística", "<p>Pessoas no elevador depois de cada parada: térreo 4; 1º andar 4 + 4 − 3 = 5; 2º 5 + 1 − 1 = 5; 3º 5 + 2 − 2 = 5; 4º 5 + 2 − 0 = 7; 5º 7 + 2 − 6 = 3. O valor que mais se repete é <strong>5</strong>. Alternativa <strong>D</strong>.</p>",
  tags=["moda"],
  enun=p(T(170, 0)) + tabela(["Número de pessoas", "Térreo", "1º andar", "2º andar", "3º andar", "4º andar", "5º andar"], [["que entram no elevador", "4", "4", "1", "2", "2", "2"], ["que saem do elevador", "0", "3", "1", "2", "0", "6"]]) + p(T(170, 2)))
X(171, "Porcentagem", "<p>Capitais do Nordeste: de 1 270 729 (1940) para 10 162 346 (2000). 10 162 346 ÷ 1 270 729 ≈ 8,0: a população ficou 8 vezes maior, um aumento de cerca de <strong>700%</strong>. Alternativa <strong>D</strong>.</p><p>800% (E) confunde o fator (8 vezes) com o aumento (7 vezes o valor inicial).</p>",
  tags=["aumento percentual"],
  enun=p(T(171, 0)) + tit("População residente, na capital e interior segundo as Grandes Regiões 1940/2000")
       + tabela(["Grandes regiões", "Total 1940", "Total 2000", "Capital 1940", "Capital 2000", "Interior 1940", "Interior 2000"],
                [["Norte", "1 632 917", "12 900 704", "368 528", "3 895 400", "1 264 389", "9 005 304"], ["Nordeste", "14 434 080", "47 741 711", "1 270 729", "10 162 346", "13 163 351", "37 579 365"],
                 ["Sudeste", "18 278 837", "72 412 411", "3 346 991", "18 822 986", "14 931 846", "53 589 425"], ["Sul", "5 735 305", "25 107 616", "459 659", "3 290 220", "5 275 646", "21 817 396"],
                 ["Centro-Oeste", "1 088 182", "11 636 728", "152 189", "4 291 120", "935 993", "7 345 608"]]) + fonte(T(171, 4)) + p(T(171, 5)))
X(172, "Geometria plana", "<p>Para que nenhuma outra peça passe pelo furo circular, o diâmetro deve ser menor que a diagonal do retângulo (5 cm), a do quadrado (4√2 ≈ 5,6 cm) e o diâmetro do círculo que contém o triângulo (6,8 ÷ √3 · 2 = 8 cm). Logo, menor que 5 cm.</p><p>Para que o cilindro não passe nos outros furos, o diâmetro deve ser maior que o lado do quadrado (4 cm), que o lado menor do retângulo (3 cm) e que o diâmetro do círculo inscrito no triângulo (4 cm). Logo, maior que 4 cm.</p><p>Entre 4 e 5 cm só está a serra de <strong>4,7 cm (II)</strong>. Alternativa <strong>B</strong>.</p>",
  figs(("q172", "Bloco de madeira com quatro furos: um retangular (R), um triangular (T), um quadrado (Q) e um circular tracejado (C), ainda por fazer.")),
  ["círculo inscrito e circunscrito", "diagonal"], enun=p(T(172, 0), T(172, 1)) + "[[fig:1]]" + p(T(172, 5)))
X(173, "Funções periódicas", "<p>Em 24 h, as curvas se encontram quatro vezes. Duas vezes isso acontece exatamente no mínimo de A (na linha tracejada), o que não conta. As outras duas são acima do mínimo de A: logo depois de cada pico de B, enquanto A está descendo. São 2 por dia, 14 por semana. Alternativa <strong>E</strong>.</p>",
  figs(("q173", "Gráfico do nível em função do tempo, de 0 a 24 h. A substância A (linha grossa) oscila com mínimos numa linha tracejada horizontal; a B (linha fina) oscila em torno dessa linha. As curvas se cruzam quatro vezes: duas sobre a linha tracejada, nos mínimos de A, e duas acima dela.")),
  ["periodicidade", "leitura de gráfico"], enun=p(T(173, 0)) + "[[fig:1]]" + p(T(173, 4)))
X(174, "Razão e proporção", "<p>Total: 5 × 800 = 4 000 mL. Nas 4 primeiras horas vão 40%: 1 600 mL. Restam 2 400 mL em 20 h = 1 200 min: 2 mL/min × 12 gotas = <strong>24 gotas por minuto</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["proporção", "unidades"])
X(175, "Geometria espacial", "<p>Cortando uma pirâmide de base quadrada com um plano: paralelo à base, sai um quadrado; passando pelo vértice, um triângulo; cortando duas faces laterais e a base, trapézios ou outros quadriláteros; e um plano inclinado que corta as quatro faces laterais e a base dá um pentágono. Alternativa <strong>E</strong>.</p><p>A pirâmide tem 5 faces, então o corte pode ter até 5 lados.</p>",
  tags=["secções planas", "pirâmide"])
X(176, "Gráficos", "<p>A vazão de enchimento é a da torneira menos a do ralo. De 5 a 10 min, a torneira dá 20 L/min e o ralo tira 5 L/min: 15 L/min, constante. Alternativa <strong>B</strong>.</p><p>De 0 a 5 min o ralo ainda está aumentando, e de 10 a 15 min a torneira está diminuindo.</p>",
  figs(("q176", "Dois gráficos de vazão Q (L/min) em função do tempo t (min). Torneira: 20 de 0 a 10 min, cai até 5 em 15 min, fica em 5 até 20 min e cai a 0 em 25 min. Ralo: sobe de 0 a 5 entre 0 e 5 min, fica em 5 até 15 min, sobe até 20 em 20 min e fica em 20 até 25 min.")),
  ["vazão", "leitura de gráfico"], enun=p(T(176, 0).replace("vazões Q,", "vazões <em>Q</em>,").replace("tempo t,", "tempo <em>t</em>,")) + "[[fig:1]]" + p(T(176, 2)))
X(177, "Porcentagem", "<p>Índices: I 14/400 = 3,5%; II 6/500 = 1,2%; III 13/520 = 2,5%; IV 9/360 = 2,5%; V 15/500 = 3%. O maior é o do bairro <strong>I</strong>. Alternativa <strong>A</strong>.</p><p>O bairro V tem mais imóveis com focos, mas em proporção menor.</p>",
  tags=["porcentagem", "comparação"],
  enun=p(T(177, 0).replace("Aedes aegypti", "<em>Aedes aegypti</em>"), T(177, 1)) + OL(*[re.sub(r"^[IV]+\. ", "", T(177, i)) for i in range(2, 7)]) + p(T(177, 7)) + fonte(T(177, 8)) + p(T(177, 9)))
X(178, "Geometria espacial", "<p>O plano α é paralelo ao equador. O trecho AB, sobre um paralelo, projeta-se como um arco de circunferência. O trecho BC fica sobre um meridiano, cujo plano contém o eixo da Terra e é perpendicular a α: ele se projeta como um segmento na direção do centro. O resultado é um arco seguido de um segmento curto, como em E. Alternativa <strong>E</strong>.</p><p>BC não se reduz a um ponto (C e D), porque B e C estão a distâncias diferentes do eixo: C, mais perto do polo, projeta-se mais perto do centro.</p>",
  figs(("q178", "Globo terrestre com os pontos A e B sobre um mesmo paralelo e C acima de B, sobre o mesmo meridiano; o caminho A–B–C está desenhado; abaixo do globo, um plano α paralelo à linha do equador."),
       ("q178a", "Alternativa A: um arco de A a B e uma curva longa subindo de B a C."),
       ("q178b", "Alternativa B: um segmento horizontal de A a B e um segmento vertical de B a C."),
       ("q178c", "Alternativa C: um segmento de A a B, com B e C no mesmo ponto."),
       ("q178d", "Alternativa D: um arco de A a B, com B e C no mesmo ponto."),
       ("q178e", "Alternativa E: um arco de A a B e um segmento curto de B a C, apontando para dentro do arco.")),
  ["projeção ortogonal", "esfera"],
  enun=p(T(178, 0).replace("plano a é", "plano α é")) + "[[fig:1]]" + p(T(178, 2).replace("plano a,", "plano α,")), alts=ALT(2))
X(179, "Razão", "<p>Contaminantes não capturados por dia: F1 18/6 = 3; F2 15/3 = 5; F3 18/4 = 4,5; F4 6/3 = 2; F5 3/2 = 1,5. A maior razão, o pior filtro, é a do <strong>F2</strong>. Alternativa <strong>B</strong>.</p>",
  tags=["razão", "comparação"], enun=p(T(179, 0), T(179, 1), T(179, 2)) + LISTA(T(179, 3)) + p(T(179, 4)) + fonte(T(179, 5)) + p(T(179, 6)))
X(180, "Logaritmo", "<p>Subtraindo as magnitudes: 9 − 7 = (2/3)[log(E<sub>1</sub>/E<sub>0</sub>) − log(E<sub>2</sub>/E<sub>0</sub>)] = (2/3) log(E<sub>1</sub>/E<sub>2</sub>). Então log(E<sub>1</sub>/E<sub>2</sub>) = 3 e E<sub>1</sub> = 10³ · E<sub>2</sub>. Alternativa <strong>C</strong>.</p>",
  tags=["escala Richter", "propriedades do logaritmo"],
  enun=p(T(180, 0).replace("devastador tsunami", "devastador <em>tsunami</em>")) + "<p>\\[M = \\frac{2}{3}\\log\\left(\\frac{E}{E_0}\\right),\\]</p>" + p("sendo <em>E</em> a energia, em kWh, liberada pelo terremoto e <em>E</em><sub>0</sub> uma constante real positiva. Considere que <em>E</em><sub>1</sub> e <em>E</em><sub>2</sub> representam as energias liberadas nos terremotos ocorridos no Japão e na China, respectivamente.") + fonte(T(180, 4)) + p("Qual a relação entre <em>E</em><sub>1</sub> e <em>E</em><sub>2</sub>?"),
  alts=FR("E_1 = E_2 + 2", "E_1 = 10^2 \\cdot E_2", "E_1 = 10^3 \\cdot E_2", "E_1 = 10^{\\frac{9}{7}} \\cdot E_2", "E_1 = \\dfrac{9}{7} \\cdot E_2"))

completar(Q, R)
