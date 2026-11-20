# Enem 2011, 2º dia, caderno azul: Matemática (questões 136 a 180; no site, 1 a 45).
# Texto legível; quadros e tabelas em HTML; fórmulas em KaTeX. Alternativas-imagem nas Q152 e Q179.
# Sem anuladas nesta área.

import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, paragrafos_enem

ID = "enem-2011-matematica"
META = {"id": ID, "banca": "Enem", "ano": 2011, "titulo": "Enem 2011: Matemática", "fonte": "Inep", "dataExame": "2011-10-23",
        "duracaoMinutos": 150, "area": "Matemática", "caderno": "azul", "dia": 2}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2011-dia2-azul")
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


X(136, "Números decimais", "<p>Comparando a diferença de cada pistão para 68 mm: 68,21 (0,21), 68,102 (0,102), 68,02 (0,02), 68,012 (0,012) e 68,001 (0,001). O mais próximo é o de <strong>68,001 mm</strong>. Alternativa <strong>E</strong>.</p><p>Quem compara só o número de casas decimais pode achar que 68,012 é menor que 68,02 e errar a ordem; o importante é alinhar as casas.</p>",
  tags=["comparação de decimais"])
X(137, "Logaritmos", "<p>Com M<sub>W</sub> = 7,3: 7,3 = −10,7 + \\(\\frac{2}{3}\\)log<sub>10</sub>(M<sub>0</sub>). Então \\(\\frac{2}{3}\\)log M<sub>0</sub> = 18 e log M<sub>0</sub> = 27. O momento sísmico é <strong>10<sup>27</sup> dina·cm</strong>. Alternativa <strong>E</strong>.</p><p>Quem esquece de multiplicar por 3/2 chega a 10<sup>18</sup>, que não está nas opções.</p>",
  tags=["equação logarítmica", "escala de terremotos"],
  enun=p(T(137, 0).replace("Mw", "M<sub>w</sub>").replace("MW e M0", "M<sub>W</sub> e M<sub>0</sub>")) + p("\\(M_W = -10{,}7 + \\dfrac{2}{3}\\log_{10}(M_0)\\)") + p(T(137, 2).replace("M0", "M<sub>0</sub>"), T(137, 3).replace("MW", "M<sub>W</sub>"))
       + fonte(T(137, 4)) + p(T(137, 5).replace("M0", "M<sub>0</sub>")),
  alts={k: f"10<sup>{e}</sup>" for k, e in zip("ABCDE", ["−5,10", "−0,73", "12,00", "21,65", "27,00"])})
X(138, "Grandezas e medidas", "<p>a = 2 300 mm: como 1 m = 1 000 mm, a = 2,3 m. b = 160 cm: como 1 m = 100 cm, b = 1,6 m. Os valores são <strong>2,3 e 1,6</strong>. Alternativa <strong>B</strong>.</p><p>A opção A divide os dois por 10 000 e por 1 000, trocando as conversões.</p>",
  figs(("q138", "Desenho de um carro de corrida de perfil com a distância entre os eixos a = 2 300 mm e a altura do solo ao encosto do piloto b = 160 cm.")),
  ["conversão de unidades"], enun=p(T(138, 0)) + "<ol type=\"a\"><li>distância <strong>a</strong> entre os eixos dianteiro e traseiro;</li><li>altura <strong>b</strong> entre o solo e o encosto do piloto.</li></ol>" + "[[fig:1]]" + p(T(138, 4)))
X(139, "Sistema de numeração", "<p>Cada relógio mostra o último algarismo ultrapassado pelo ponteiro, respeitando o sentido de rotação indicado. No milhar o ponteiro passou do 2; na centena, do 6; na dezena, do 1; na unidade, do 4. A leitura é <strong>2 614 kWh</strong>. Alternativa <strong>A</strong>.</p><p>Os relógios giram em sentidos alternados; quem lê todos no sentido horário erra a leitura.</p>",
  figs(("q139", "Quatro relógios de ponteiro do medidor de luz, rotulados milhar, centena, dezena e unidade, com setas que indicam sentidos de rotação alternados; os ponteiros estão logo depois do 2, do 6, do 1 e do 4, respectivamente.")),
  ["leitura de instrumentos"], enun=EF(139, 1, fnt=T(139, 2)))
_t, _c = T(140, 1).split(" Para optar", 1)
X(140, "Áreas e perímetros", "<p>O perímetro não pode passar de 180 m. Terreno 1: 2(55 + 45) = 200; 2: 220; 3: 2(60 + 30) = 180; 4: 2(70 + 20) = 180; 5: 360. Só 3 e 4 servem. Áreas: 60 × 30 = 1 800 m² e 70 × 20 = 1 400 m². O de maior área é o <strong>terreno 3</strong>. Alternativa <strong>C</strong>.</p><p>O terreno 5 (E) tem a maior área, mas o perímetro estoura o limite.</p>",
  tags=["perímetro", "área do retângulo"], enun=p(T(140, 0)) + "<ul>" + "".join(f"<li>{x.strip()}</li>" for x in re.split(r"(?=Terreno \d)", _t) if x.strip()) + "</ul>" + p("Para optar" + _c))
X(141, "Razão e proporção", "<p>Para gastar 200 calorias: agachamentos, 40 min em vez de 20 (+20); supermercado, 60 min em vez de 30 (+30); tirar o pó, 40 min em vez de 30 (+10); jardim, cachorro e roupas já gastam 200 em 30 min (+0). O tempo a mais é 20 + 30 + 10 = <strong>60 minutos</strong>. Alternativa <strong>B</strong>.</p>",
  tags=["proporcionalidade direta"],
  enun=p(T(141, 0)) + "<ul><li>Enquanto você fala ao telefone, faça agachamentos: 100 calorias gastas em 20 minutos.</li><li>Meia hora de supermercado: 100 calorias.</li><li>Cuidar do jardim por 30 minutos: 200 calorias.</li><li>Passear com o cachorro: 200 calorias em 30 minutos.</li><li>Tirar o pó dos móveis: 150 calorias em 30 minutos.</li><li>Lavar roupas por 30 minutos: 200 calorias.</li></ul>"
       + fonte(T(141, 3)) + p(T(141, 4), T(141, 5)))
X(142, "Estatística", "<p>As 15 temperaturas somam 255, e a média é 255 ÷ 15 = 17 °C. Em ordem: 13,5; 13,5; 13,5; 13,5; 14; 15,5; 16; <strong>18</strong>; 18; 18,5; 19,5; 20; 20; 20; 21,5 — a mediana é o 8º valor, 18 °C. A moda é 13,5 °C, que aparece 4 vezes. Resposta: 17 °C, 18 °C e 13,5 °C. Alternativa <strong>B</strong>.</p>",
  tags=["média", "mediana", "moda"],
  enun=p(T(142, 0), T(142, 1)) + tabela(["Dia do mês", "Temperatura (em °C)"], [[str(d), t] for d, t in zip(range(1, 30, 2), ["15,5", "14", "13,5", "18", "19,5", "20", "13,5", "13,5", "18", "20", "18,5", "13,5", "21,5", "20", "16"])]) + p(T(142, 3)))
X(143, "Escala", "<p>Na escala 1 : 250, cada medida real é dividida por 250. Em centímetros: 28 m = 2 800 cm → 2 800 ÷ 250 = 11,2 cm; 12 m = 1 200 cm → 1 200 ÷ 250 = 4,8 cm. As medidas são <strong>11,2 e 4,8</strong>. Alternativa <strong>C</strong>.</p><p>A opção A inverte comprimento e largura.</p>",
  tags=["escala", "maquete"])
X(144, "Geometria espacial", "<p>Os cortes de O às arestas AD e BC (faces laterais opostas) retiram dois sólidos iguais entre si; os cortes de O a AB e CD retiram outros dois, também iguais entre si, mas diferentes dos primeiros, porque são feitos depois e já encontram o cubo cortado. Os sólidos descartados são <strong>iguais dois a dois</strong>. Alternativa <strong>E</strong>.</p>",
  figs(("q144", "À esquerda, um cubo com os vértices da base A, B, C, D e o ponto O no centro da face superior; à direita, a pirâmide de base ABCD e vértice O obtida dele.")),
  ["cortes", "pirâmide"], enun=p(T(144, 0)) + "[[fig:1]]" + p("Os pontos A, B, C, D e O do cubo e da pirâmide são os mesmos. O ponto O é central na face superior do cubo. Os quatro cortes saem de O em direção às arestas \\(\\overline{AD}\\), \\(\\overline{BC}\\), \\(\\overline{AB}\\) e \\(\\overline{CD}\\), nessa ordem. Após os cortes, são descartados quatro sólidos.", T(144, 5)))
X(145, "Porcentagem", "<p>Em 2009 foram 331 bilhões de xícaras de 120 mL: 331 × 0,12 ≈ 39,7 bilhões de litros. Com aumento de 1/5 (20%): 39,7 × 1,2 ≈ 47,7 bilhões. A previsão mais próxima é <strong>48 bilhões de litros</strong>. Alternativa <strong>E</strong>.</p><p>A opção D (40) é o consumo de 2009, sem o aumento.</p>",
  tags=["fração", "conversão de unidades"],
  enun=tit("Café no Brasil") + ap(T(145, 1)) + fonte("<em>Veja</em>. Ed. 2158, 31 mar. 2010.") + p("Considere que a xícara citada na notícia seja equivalente a, aproximadamente, 120 mL de café. Suponha que em 2010 os brasileiros bebam ainda mais café, aumentando o consumo em \\(\\frac{1}{5}\\) do que foi consumido no ano anterior.", T(145, 5)))
X(146, "Escala", "<p>2 000 km = 200 000 000 cm. Se 8 cm no mapa valem 200 000 000 cm, 1 cm vale 25 000 000 cm. A escala é <strong>1 : 25 000 000</strong>. Alternativa <strong>E</strong>.</p><p>Quem converte km para metros, e não para centímetros, encontra 1 : 250 000 (D).</p>",
  tags=["escala de mapa"])
X(147, "Geometria espacial", "<p>A sombrinha tem uma ponta no centro e se abre em uma superfície inclinada até a borda circular, como a lateral de um cone. Girando um segmento inclinado em torno do cabo, obtém-se a superfície de um <strong>cone</strong>. Alternativa <strong>E</strong>.</p><p>Não há corte no topo, por isso não é tronco de cone (D).</p>",
  figs(("q147", "Sombrinha oriental: varetas saem de um ponto no topo e se abrem formando uma superfície cônica com borda circular; o cabo sai do vértice.")),
  ["sólidos de revolução"], enun=EF(147, 1, fnt=T(147, 2)))
X(148, "Grandezas e medidas", "<p>6 000 m × 3,3 = 19 800 pés. Na Finlândia, só acima de 31 000 pés. A diferença é 31 000 − 19 800 = <strong>11 200 pés</strong>. Alternativa <strong>C</strong>.</p><p>A opção D (19 800) é só a conversão dos 6 000 m.</p>",
  tags=["conversão de unidades"])
X(149, "Funções", "<p>Com IMC = 20 e massa 60 kg: altura² = 60 ÷ 20 = 3, então altura = √3 ≈ 1,7 m. Altura × √altura ≈ 1,7 × 1,3 = 2,21. IAC = 100 ÷ 2,21 − 18 ≈ 45,2 − 18 ≈ 27%. A faixa normal vai de 19% a 26%, então ela deve <strong>reduzir seu excesso de gordura em cerca de 1%</strong>. Alternativa <strong>A</strong>.</p><p>A opção B confunde o próprio IAC (27%) com o excesso.</p>",
  figs(("q149", "Duas silhuetas. O velho IMC: Índice de Massa Corporal = massa (kg) ÷ (altura × altura, em m). O novo IAC: % de gordura corporal = circunferência do quadril (cm) ÷ (altura × √altura, em m) − 18.")),
  ["índice de adiposidade", "radicais"],
  enun=p(T(149, 0)) + "[[fig:1]]" + fonte(T(149, 5)) + p(T(149, 6), "(Use \\(\\sqrt{3} = 1{,}7\\) e \\(\\sqrt{1{,}7} = 1{,}3\\))"))
X(150, "Geometria analítica", "<p>A estação tem de estar sobre a reta y = x + 4. (−5, 0): −5 + 4 = −1, não está; (−2, 1): −2 + 4 = 2, não está. Das que estão: (−3, 1) dista √(2² + 4²) = √20 ≈ 4,5 km de P(−5, 5); (0, 4) dista √(25 + 1) ≈ 5,1 km; (2, 6) dista √(49 + 1) ≈ 7,1 km. A única a até 5 km é <strong>(−3, 1)</strong>. Alternativa <strong>B</strong>.</p>",
  figs(("q150", "Plano cartesiano com eixos de −8 a 8 e a reta tracejada y = x + 4, que corta o eixo y em 4 e o eixo x em −4.")),
  ["distância entre pontos", "equação da reta"], enun=p(T(150, 0)) + "[[fig:1]]" + p(T(150, 2), T(150, 3)))
X(151, "Simetria", "<p>Cada peça da calçada tem três “braços” iguais, distribuídos em volta do centro a cada terço de volta. Girando a peça 120° em torno do centro, ela coincide consigo mesma. A resposta é <strong>120°</strong>. Alternativa <strong>D</strong>.</p><p>A peça não é um hexágono regular; por isso não se mantém com uma rotação de 60° (B).</p>",
  figs(("q151", "Foto de uma calçada de blocos de concreto encaixados, com peças em forma de hexágono irregular.")), ["rotação", "polígonos"], enun="[[fig:1]]" + fonte(T(151, 1)) + p(T(151, 2)))
X(152, "Função afim", "<p>O preço é m = 1,75n: uma função linear, cujo gráfico é uma reta que passa pela origem (0 kg custa R$ 0) e pelo ponto (1; 1,75). Esse é o gráfico <strong>E</strong>. Alternativa <strong>E</strong>.</p><p>No gráfico D a reta começa em n = 1, e no B começa acima de zero; A e C são curvas.</p>",
  figs(("q152a", "Gráfico A: curva que sobe rápido no início e depois mais devagar, passando por (1; 1,75)."),
       ("q152b", "Gráfico B: reta que começa acima de zero no eixo m e passa por (1; 1,75)."),
       ("q152c", "Gráfico C: curva que sobe cada vez mais rápido, quase vertical, passando por (1; 1,75)."),
       ("q152d", "Gráfico D: reta que começa no ponto (1; 0) do eixo n e sobe."),
       ("q152e", "Gráfico E: reta que sai da origem e passa por (1; 1,75).")),
  ["proporcionalidade", "gráfico"], enun=p(T(152, 0), T(152, 1)), alts=ALT(1))
_d, _q = T(153, 0).split(" Quem organiza", 1)
X(153, "Razão e proporção", "<p>Para 30 convidados: carne, 30 × 250 g = 7,5 kg; arroz, 30 ÷ 4 = 7,5 copos; farofa, 30 × 4 = 120 colheres; vinho, 30 ÷ 6 = 5 garrafas; cerveja, 30 ÷ 2 = 15; espumante, 30 ÷ 3 = 10. A resposta é a <strong>alternativa E</strong>. Alternativa <strong>E</strong>.</p><p>A opção D erra o arroz (7 copos) e a cerveja (30).</p>",
  tags=["proporcionalidade", "unidades"], enun=p(_d.split("•")[0].strip()) + LISTA("•" + _d.split("•", 1)[1]) + p("Quem organiza" + _q) + fonte(T(153, 1)) + p(T(153, 2)))
X(154, "Estatística", "<p>Os percentuais do Nordeste são 18%, 19%, 21%, 15% e 19%. A soma é 92%, e a média é 92 ÷ 5 = <strong>18,4%</strong>. Alternativa <strong>C</strong>.</p><p>A opção D (19%) é a moda, e não a média.</p>",
  tags=["média aritmética", "tabela"],
  enun=p(T(154, 0)) + tabela(["Região", "2005", "2006", "2007", "2008", "2009"], [["Norte", "2%", "2%", "1%", "2%", "1%"], ["Nordeste", "18%", "19%", "21%", "15%", "19%"], ["Centro-Oeste", "5%", "6%", "7%", "8%", "9%"], ["Sudeste", "55%", "61%", "58%", "66%", "60%"], ["Sul", "21%", "12%", "13%", "9%", "11%"]])
       + fonte(T(154, 3)) + p(T(154, 4)))
X(155, "Trigonometria", "<p>Com α = 30°, o ângulo externo em B é 60°, e o ângulo em P vale 60° − 30° = 30°. O triângulo ABP é isósceles: BP = AB = 2 000 m. A menor distância até P é a perpendicular à trajetória: BP · sen 60° = 2 000 × \\(\\frac{\\sqrt{3}}{2}\\) = <strong>1 000√3 m</strong>. Alternativa <strong>B</strong>.</p>",
  figs(("q155", "Triângulo com os pontos A e B sobre a trajetória do barco (seta horizontal) e P acima, na praia; em A o ângulo é α e em B, o ângulo externo, 2α.")),
  ["triângulo isósceles", "seno"], enun=p(T(155, 0)) + "[[fig:1]]" + p(T(155, 2).replace("medido o ângulo e,", "medido o ângulo α = 30° e,")),
  alts={"A": "1 000 m.", "B": "1 000\\(\\sqrt{3}\\) m.", "C": "2 000\\(\\dfrac{\\sqrt{3}}{3}\\) m.", "D": "2 000 m.", "E": "2 000\\(\\sqrt{3}\\) m."})
X(156, "Função afim", "<p>Em fevereiro (x = 2) eram 880 605 trabalhadores, com aumento de 4 300 por mês. Em janeiro (x = 1): 876 305. Para valer y = a + 4 300x em x = 1, a = 876 305 − 4 300 = 872 005. A expressão é <strong>y = 872 005 + 4 300x</strong>. Alternativa <strong>C</strong>.</p><p>Confira: x = 2 dá 872 005 + 8 600 = 880 605.</p>",
  tags=["função afim", "modelagem"])
X(157, "Matemática financeira", "<p>Poupança: 500 × 0,560% = R$ 2,80, montante R$ 502,80. CDB: 500 × 0,876% = R$ 4,38; descontando 4% de IR sobre o ganho, 4,38 × 0,96 ≈ R$ 4,20, montante R$ 504,20. O CDB é melhor, com cerca de <strong>R$ 504,21</strong>. Alternativa <strong>D</strong>.</p><p>A opção C esquece o imposto.</p>",
  tags=["juros", "imposto"],
  enun=p(T(157, 0)) + tabela(["", "Rendimento mensal (%)", "IR (imposto de renda)"], [["POUPANÇA", "0,560", "ISENTO"], ["CDB", "0,876", "4% (sobre o ganho)"]]) + p(T(157, 2)))
X(158, "Razão e proporção", "<p>Depois da redução: o consumidor de baixa renda que gastou 100 kWh paga R$ 16,73, ou R$ 0,1673 por kWh; o residencial de 185 kWh paga R$ 85,56, ou R$ 0,4625 por kWh. A diferença é cerca de 0,4625 − 0,1673 ≈ <strong>R$ 0,29</strong>. Alternativa <strong>B</strong>.</p>",
  figs(("q158", "Tabela “Como fica a tarifa”. Residencial, consumo mensal em kWh (antes, depois, economia): 140 kWh, R$ 71,04, R$ 64,75, R$ 6,29; 185 kWh, R$ 93,87, R$ 85,56, R$ 8,32; 350 kWh, R$ 177,60, R$ 161,86, R$ 15,74; 500 kWh, R$ 253,72, R$ 231,24, R$ 22,48. Baixa renda: 30 kWh, R$ 3,80, R$ 3,35, R$ 0,45; 65 kWh, R$ 11,53, R$ 10,04, R$ 1,49; 80 kWh, R$ 14,84, R$ 12,90, R$ 1,94; 100 kWh, R$ 19,31, R$ 16,73, R$ 2,59; 140 kWh, R$ 32,72, R$ 28,20, R$ 4,53. Fonte: Celpe.")),
  ["preço unitário", "tabela"], enun=p(T(158, 0)) + "[[fig:1]]" + fonte("<em>Diário de Pernambuco</em>. 28 abr. 2010 (adaptado).") + p(T(158, 3)))
X(159, "Função afim", "<p>Em milhares de reais, a primeira empresa cobra 100n + 350 e a segunda, 120n + 150. É indiferente quando os custos são iguais: <strong>100n + 350 = 120n + 150</strong>. Alternativa <strong>A</strong>.</p><p>Resolvendo, n = 10 km. A opção B troca os valores fixos das empresas.</p>",
  tags=["equação do 1º grau", "comparação de propostas"])
X(160, "Porcentagem", "<p>Seja x o valor aplicado. No primeiro mês sobrou 0,7x (perdeu 0,3x). No segundo, recuperou 20% do que perdeu: 0,2 × 0,3x = 0,06x. Ficou com 0,76x = 3 800, então x = <strong>R$ 5 000,00</strong>. Alternativa <strong>C</strong>.</p><p>Quem aplica os 20% sobre o que sobrou (0,7x × 1,2 = 0,84x) chega a R$ 4 523,80 (B).</p>",
  tags=["porcentagem", "equação"])
X(161, "Razão e proporção", "<p>Densidade demográfica = população ÷ área = 20 000 000 ÷ 800 000 = <strong>25 habitantes por km²</strong>. Alternativa <strong>B</strong>.</p><p>Cuidado com os zeros: 20 milhões têm 7 zeros e 800 mil têm 5, mais o 8.</p>",
  tags=["densidade demográfica"], enun=SUP(p(T(161, 0)) + fonte(T(161, 1)) + p(T(161, 2))))
X(162, "Progressão aritmética", "<p>As vendas aumentam 1 500 por mês: 33 000, 34 500, 36 000... Julho é o 7º termo: 33 000 + 6 × 1 500 = <strong>42 000</strong>. Alternativa <strong>D</strong>.</p><p>A opção B (40 500) é junho. O termo geral é a<sub>n</sub> = 33 000 + (n − 1) × 1 500; com n = 7, a<sub>7</sub> = 42 000.</p>",
  tags=["termo geral da PA"])
X(163, "Probabilidade", "<p>Pela escala em °C do gráfico, Rural, Residencial Urbano e Residencial Suburbano ficam abaixo de 31 °C; só a região Comercial passa disso. Das 4 regiões (sem contar o Centro), 3 são adequadas: probabilidade <strong>3/4</strong>. Alternativa <strong>E</strong>.</p><p>Quem conta o Centro entre as opções chega a 3/5 (D).</p>",
  figs(("q163", "Gráfico “Perfil da ilha de calor urbana”, com temperaturas em °F à esquerda (85 a 92) e em °C à direita (30 a 33) sobre um perfil de cidade: Rural, cerca de 30 °C; Comercial, cerca de 31,5 °C; Centro, o pico, cerca de 33 °C; Residencial Urbano, cerca de 30,5 °C; Residencial Suburbano, cerca de 29,5 °C.")),
  ["probabilidade simples", "leitura de gráfico"], enun=p(T(163, 0)) + "[[fig:1]]" + p(T(163, 2)), alts=FR("\\dfrac{1}{5}", "\\dfrac{1}{4}", "\\dfrac{2}{5}", "\\dfrac{3}{5}", "\\dfrac{3}{4}"))
X(164, "Grandezas e medidas", "<p>Dois banhos de 10 min são 20 min = 1/3 h por dia. Em sete dias: 7/3 h. Energia = 4,8 × 7/3 = <strong>11,2</strong> (kWh, chamado de kW na questão). Alternativa <strong>D</strong>.</p><p>A opção B (1,6) é o consumo de um único dia.</p>",
  tags=["energia elétrica", "proporção"])
X(165, "Geometria plana", "<p>Numa volta completa, cada raia percorre as duas retas (iguais para todos) e uma circunferência inteira. A raia 1, mais interna, tem o menor raio e, portanto, o menor percurso. Saindo do mesmo ponto, o corredor da <strong>raia 1</strong> seria beneficiado. Alternativa <strong>A</strong>.</p>",
  figs(("q165", "Pista de atletismo vista de cima: dois trechos retos de 84,39 m ligados por dois semicírculos de raio 36,5 m.")),
  ["comprimento da circunferência"], enun=p(T(165, 0)) + "[[fig:1]]" + fonte(T(165, 2)) + p(T(165, 3)))
X(166, "Razão e proporção", "<p>As mulheres passam de 32 mil para 40 mil, aumento de 8/32 = 25%. Aplicando 25% aos homens: 28 mil × 1,25 = <strong>35 mil</strong>. Alternativa <strong>D</strong>.</p><p>A opção B (9 mil) soma 8 mil e 1 mil sem proporção; a opção A (4 mil) não considera o total.</p>",
  tags=["proporcionalidade", "porcentagem"], enun=p(T(166, 0)) + fonte("<em>Época</em>. 26 abr. 2010 (adaptado).") + p(T(166, 2), T(166, 3)))
X(167, "Geometria espacial", "<p>O copo tem raio 2 cm e altura 10 cm: V = π r² h = 3 × 4 × 10 = 120 cm³ = 120 mL. A mistura é 1 parte de açúcar para 5 de água, então a água é 5/6 do volume: 120 × 5/6 = <strong>100 mL</strong>. Alternativa <strong>C</strong>.</p><p>A opção D (120) é o volume total do copo.</p>",
  tags=["volume do cilindro", "proporção"], trocas=[("deixála", "deixá-la"), ("(utilize p = 3)", "(utilize π = 3)")])
X(168, "Probabilidade", "<p>Contando pares de bolas diferentes de 1 a 15: soma 12 tem 5 pares (1+11, 2+10, 3+9, 4+8, 5+7); soma 17 tem 7 (2+15 até 8+9); soma 22 tem 4 (7+15, 8+14, 9+13, 10+12). Quem tem mais chance é <strong>Bernardo, com 7 possibilidades, contra 5 de Arthur e 4 de Caio</strong>. Alternativa <strong>C</strong>.</p><p>Na opção B, a contagem de Arthur está errada.</p>",
  tags=["contagem", "probabilidade"])
X(169, "Funções", "<p>IMC de Duílio: 96,4 ÷ 1,88² = 96,4 ÷ 3,5344 ≈ 27,3. IMC de Sandra: 84 ÷ 1,70² = 84 ÷ 2,89 ≈ 29,1. Os dois ficam entre 25 e 29,9: <strong>ambos na categoria de sobrepeso</strong>. Alternativa <strong>B</strong>.</p><p>Quem usa o peso ideal, e não o peso atual, chega a outros valores.</p>",
  figs(("q169", "Fichas “O perfil dos novos corredores”: Duílio Saba, 50 anos, altura 1,88 metro, peso 96,4 quilos, peso ideal 94,5 quilos; Sandra Tescari, 42 anos, altura 1,70 metro, peso 84 quilos, peso ideal 77 quilos.")),
  ["IMC", "potenciação"],
  enun=p(T(169, 0).replace("IMC = m/h²", "\\(IMC = \\dfrac{m}{h^2}\\)")) + "[[fig:1]]" + fonte("<em>Veja</em>. Ed. 2055 (adaptado).") + p(T(169, 3))
       + tabela(["Categorias", "IMC (kg/m²)"], [["Desnutrição", "Abaixo de 14,5"], ["Peso abaixo do normal", "14,5 a 20"], ["Peso normal", "20 a 24,9"], ["Sobrepeso", "25 a 29,9"], ["Obesidade", "30 a 39,9"], ["Obesidade mórbida", "Igual ou acima de 40"]])
       + fonte("<em>Nova Escola</em>. N° 172, maio 2004.") + p(T(169, 6)))
X(170, "Probabilidade", "<p>O posto vacinou 42 + 22 + 56 + 30 + 50 = 200 pessoas. Portadores de doenças crônicas foram 22. A probabilidade é 22/200 = <strong>11%</strong>. Alternativa <strong>C</strong>.</p><p>A opção E (22%) usa o número absoluto como se fosse porcentagem.</p>",
  tags=["probabilidade simples", "tabela"],
  enun=p(T(170, 0)) + tit("Campanha de vacinação contra a gripe suína") + tabela(["Datas da vacinação", "Público-alvo", "Quantidade de pessoas vacinadas"],
    [["8 a 19 de março", "Trabalhadores da saúde e indígenas", "42"], ["22 de março a 2 de abril", "Portadores de doenças crônicas", "22"], ["5 a 23 de abril", "Adultos saudáveis entre 20 e 29 anos", "56"], ["24 de abril a 7 de maio", "População com mais de 60 anos", "30"], ["10 a 21 de maio", "Adultos saudáveis entre 30 e 39 anos", "50"]])
    + fonte("Disponível em: http://img.terra.com.br. Acesso em: 26 abr. 2010 (adaptado).") + p(T(170, 3)))
X(171, "Probabilidade", "<p>Pelo menos 1 Mbps: de 1 a 2 Mbps (15%), de 2 a 4 (5%), de 4 a 8 (1%) e acima de 8 (1%). Somando, 22%: chance de <strong>0,22</strong>. Alternativa <strong>D</strong>.</p><p>Os 24% que não sabem ou não responderam não entram.</p>",
  figs(("q171", "Gráfico de colunas “% domicílios segundo a velocidade de conexão à internet”: até 256 kbps, 34; de 256 kbps a 1 Mbps, 20; de 1 a 2 Mbps, 15; de 2 a 4 Mbps, 5; de 4 a 8 Mbps, 1; acima de 8 Mbps, 1; não sabe ou não responde, 24.")),
  ["probabilidade", "gráfico de colunas"], enun=EF(171, 1, fnt=T(171, 2)))
X(172, "Grafos", "<p>É preciso ir de K a F passando por todos os pontos uma única vez, seguindo as tubulações. O caminho K, L, G, I, J, H, F usa só ligações existentes e passa pelos sete pontos. Alternativa <strong>C</strong>.</p><p>A opção A pula pontos, e as opções B, D e E usam ligações que não existem na figura ou deixam pontos de fora.</p>",
  figs(("q172", "Esquema de tubulações como um prisma em perspectiva: pontos L, G e F em cima, I e H no meio, K e J embaixo, ligados por segmentos.")),
  ["caminho", "grafo"], enun=p(T(172, 0), T(172, 1)) + "[[fig:1]]" + p(T(172, 3)))
X(173, "Leitura de gráficos", "<p>O gráfico tem o máximo em 2003 (28,28%), cai em 2004 (27,79%), 2005 (25,83%) e 2006 (23,92%), e volta a subir em 2007 (24,74%) e 2008 (26,46%). A queda foi entre <strong>2003 e 2006</strong>. Alternativa <strong>C</strong>.</p>",
  figs(("q173", "Gráfico de linha da participação do agronegócio no PIB, em %: 1998, 21,33; 1999, 22,24; 2000, 22,87; 2001, 23,26; 2002, 25,31; 2003, 28,28; 2004, 27,79; 2005, 25,83; 2006, 23,92; 2007, 24,74; 2008, 26,46.")),
  ["gráfico de linha"], enun=p(T(173, 0), T(173, 1)) + "[[fig:1]]" + fonte(T(173, 3)) + p(T(173, 4)))
X(174, "Análise combinatória", "<p>Os números usam os algarismos 1, 3, 5, 7, 9, todos diferentes. Começando por 1, 3 ou 5: 3 × 24 = 72. Começando por 71 ou 73: 2 × 6 = 12 (total 84). Começando por 751 e 753: 2 + 2 = 4 (total 88). O próximo é 75 913, o menor começado por 759. Ele é o <strong>89º</strong>. Alternativa <strong>E</strong>.</p>",
  tags=["permutação", "ordem"])
X(175, "Porcentagem", "<p>O gráfico mostra 25% de “NÃO”. Dos 279 internautas: 0,25 × 279 ≈ 69,75, ou cerca de 70 pessoas. O número fica <strong>entre 50 e 75</strong>. Alternativa <strong>C</strong>.</p><p>A opção B confunde 25% com 25 pessoas.</p>",
  figs(("q175", "Gráfico de colunas: Sim, 67%; Não, 25%; Não sei avaliar, 8%.")),
  ["porcentagem", "gráfico"], enun=p(T(175, 0)) + "[[fig:1]]" + fonte("<em>Época</em>. Ed. 619, 29 mar. 2010 (adaptado).") + p(T(175, 2).split("(adaptado). ", 1)[1]))
X(176, "Notação científica", "<p>O Sol (classe G2) tem 5 770 K. Cinco vezes isso é cerca de 28 850 K, temperatura próxima à da classe B0 (28 000 K), cuja luminosidade é 2 × 10<sup>4</sup> = <strong>20 000 vezes a do Sol</strong>. Alternativa <strong>A</strong>.</p><p>As opções B e C confundem temperatura com luminosidade.</p>",
  tags=["leitura de tabela", "ordem de grandeza"],
  enun=p(T(176, 0), T(176, 1)) + tit("Estrelas da Sequência Principal") + tabela(["Classe Espectral", "Temperatura", "Luminosidade", "Massa", "Raio"],
    [["O5", "40 000", "5 × 10<sup>5</sup>", "40", "18"], ["B0", "28 000", "2 × 10<sup>4</sup>", "18", "7"], ["A0", "9 900", "80", "3", "2,5"], ["G2", "5 770", "1", "1", "1"], ["M0", "3 480", "0,06", "0,5", "0,6"]])
    + fonte("Temperatura em Kelvin. Luminosidade, massa e raio, tomando o Sol como unidade. Disponível em: http://www.zenite.nu. Acesso em: 1 maio 2010 (adaptado).") + p(T(176, 5)))
_i = T(177, 0).split(": Investimento A", 1)
X(177, "Matemática financeira", "<p>Juros compostos em um ano: A, 1,03<sup>12</sup> ≈ 1,426, ou 42,6%; B, 36%; C, 1,18² = 1,3924, ou cerca de 39,2%. O maior rendimento é o do <strong>investimento A</strong>. Alternativa <strong>C</strong>.</p><p>Somar as taxas (3% × 12 = 36%) ignora os juros sobre juros (A).</p>",
  tags=["juros compostos", "comparação"],
  enun=p(_i[0] + ":") + "<ul><li>Investimento A: 3% ao mês</li><li>Investimento B: 36% ao ano</li><li>Investimento C: 18% ao semestre</li></ul>" + p(T(177, 1))
       + tabela(["n", "1,03<sup>n</sup>"], [["3", "1,093"], ["6", "1,194"], ["9", "1,305"], ["12", "1,426"]]) + p(T(177, 3)))
X(178, "Grandezas proporcionais", "<p>S é diretamente proporcional a b e a d², com constante k: \\(S = k \\cdot b \\cdot d^2\\). Alternativa <strong>C</strong>.</p><p>A opção A esquece o quadrado; a B esquece a constante; D e E colocam grandezas no denominador, como se fossem inversamente proporcionais.</p>",
  figs(("q178", "Viga em perspectiva com a altura d e a largura b indicadas.")), ["proporcionalidade direta"],
  enun=p(T(178, 0)) + "[[fig:1]]" + p(T(178, 2)), alts=FR("S = k \\cdot b \\cdot d", "S = b \\cdot d^2", "S = k \\cdot b \\cdot d^2", "S = \\dfrac{k \\cdot b}{d^2}", "S = \\dfrac{k \\cdot d^2}{b}"))
X(179, "Funções", "<p>Plano K: R$ 29,90 fixo até 200 min e depois sobe R$ 0,20 por minuto, chegando a R$ 89,90 em 500 min. Plano Z: R$ 49,90 fixo até 300 min e depois sobe R$ 0,10 por minuto, chegando a R$ 69,90 em 500 min. O gráfico com esses pontos é o <strong>D</strong>. Alternativa <strong>D</strong>.</p><p>Os dois planos custam o mesmo em 300 min (R$ 49,90), onde as linhas se cruzam.</p>",
  figs(("q179a", "Gráfico A: K constante em 29,90 até 200 min e depois subindo; Z constante em 49,90 até 300 min e depois subindo, sempre acima de K."),
       ("q179b", "Gráfico B: K em 29,90 até 200 min, Z em 49,90 até 200 min; as duas sobem e se cruzam perto de 400 min."),
       ("q179c", "Gráfico C: K em 29,90 até 200 min e Z em 49,90 até 300 min; as duas sobem juntas pela mesma reta depois de 300 min."),
       ("q179d", "Gráfico D: K em 29,90 até 200 min e depois sobe até 89,90 em 500 min; Z em 49,90 até 300 min e depois sobe até 69,90 em 500 min; cruzam-se em 300 min."),
       ("q179e", "Gráfico E: K em 29,90 até 300 min, Z em 49,90 até 300 min; as duas sobem e se cruzam perto de 500 min.")),
  ["função definida por partes", "gráfico"], enun=p(T(179, 0), T(179, 1)), alts=ALT(1))
X(180, "Função afim", "<p>Lucro: LT(q) = 5q − (2q + 12) = 3q − 12. Para não ter prejuízo, LT ≥ 0: 3q ≥ 12, ou seja, q ≥ 4. A quantidade mínima é <strong>4</strong>. Alternativa <strong>D</strong>.</p><p>Com 3 produtos (C), o lucro seria −3, prejuízo.</p>",
  tags=["inequação", "lucro"])

completar(Q, R)
