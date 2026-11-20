# Enem 2010, 2º dia, caderno azul: Matemática (questões 136 a 180; no site, 1 a 45).
# Texto legível; quadros e tabelas em HTML; fórmulas em KaTeX. Alternativas-imagem nas Q136, Q138 e Q142. Gráficos com texto ilegível no PDF (Q141, Q143) recortados como imagem.
# Sem anuladas nesta área.

import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, paragrafos_enem

ID = "enem-2010-matematica"
META = {"id": ID, "banca": "Enem", "ano": 2010, "titulo": "Enem 2010: Matemática", "fonte": "Inep", "dataExame": "2010-11-07",
        "duracaoMinutos": 150, "area": "Matemática", "caderno": "azul", "dia": 2}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2010-dia2-azul")
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
LOUSA = lambda x: x


X(136, "Frações e porcentagem", "<p>A lousa tem quatro partes iguais, cada uma com 25% da área. 40% equivale a uma parte inteira (25%) mais 15%, ou seja, uma parte e pouco mais da metade da segunda (15/25 = 0,6 de uma parte). A representação certa é a da <strong>alternativa C</strong>. Alternativa <strong>C</strong>.</p><p>Duas partes inteiras seriam 50%, e uma parte só seria 25%.</p>",
  figs(("q136", "Lousa dividida em quatro partes iguais, com as três primeiras preenchidas de texto e a última em branco."),
       ("q136a", "Alternativa A: lousa com só a primeira das quatro partes preenchida."),
       ("q136b", "Alternativa B: lousa com as duas primeiras partes preenchidas."),
       ("q136c", "Alternativa C: lousa com a primeira parte inteira preenchida e cerca de metade da segunda."),
       ("q136d", "Alternativa D: lousa com as três primeiras partes preenchidas."),
       ("q136e", "Alternativa E: lousa com as quatro partes preenchidas.")),
  ["porcentagem", "representação de frações"], enun=EF(136, 1), alts=ALT(2))
X(137, "Razão e proporção", "<p>O espelho tem 42 m = 4 200 cm. A razão entre o olho (2,1 cm) e o espelho é 2,1 : 4 200 = 1 : 2 000. Alternativa <strong>E</strong>.</p><p>Quem esquece de converter metros em centímetros chega a 1 : 20 (A).</p>",
  tags=["razão", "conversão de unidades"], enun=p(T(137, 0)) + fonte(T(137, 1)) + p(T(137, 2)))
X(138, "Geometria espacial", "<p>O bebedouro 3 é meio cilindro deitado, sem tampa: a superfície curva aberta é um retângulo de 100 cm (comprimento) por meia circunferência, e as duas pontas são semicírculos de 60 cm de diâmetro. A planificação é um retângulo com um semicírculo em cada uma das pontas, como na <strong>figura D</strong>. Alternativa <strong>D</strong>.</p><p>As figuras com trapézio ou setor (A e B) planificam troncos de cone; as com círculo (C) planificam um cilindro inteiro.</p>",
  figs(("q138", "Bebedouros 1 e 2: troncos de cone de 60 cm de altura, com diâmetro superior de 120 cm e de 60 cm. Bebedouro 3: semicilindro de 100 cm de comprimento, 60 cm de largura e 30 cm de altura."),
       ("q138a", "Alternativa A: setor de coroa circular de 100 cm de lado curvo e 60 cm de altura, com um círculo de 60 cm de diâmetro embaixo."),
       ("q138b", "Alternativa B: trapézio com base maior de 100 cm e altura 60 cm, com um círculo embaixo."),
       ("q138c", "Alternativa C: retângulo de 100 cm por 60 cm com um círculo embaixo."),
       ("q138d", "Alternativa D: retângulo alto, de 100 cm por 60 cm, com um semicírculo de 60 cm de diâmetro embaixo."),
       ("q138e", "Alternativa E: retângulo de 100 cm de altura, com um semicírculo de 60 cm em cima e outro embaixo.")),
  ["planificação", "semicilindro"],
  enun=p(T(138, 0).split(" Os três estão")[0] + " Os três estão ilustrados na figura.") + "[[fig:1]]" + fonte("A escolha do bebedouro. In: <em>Biotemas</em>. V. 22, n°. 4, 2009 (adaptado).") + p("Considerando que nenhum dos recipientes tenha tampa, qual das figuras a seguir representa uma planificação para o bebedouro 3?"),
  alts=ALT(2))
X(139, "Geometria espacial", "<p>O paralelepípedo tem volume 3 × 18 × 4 = 216 cm³. O cubo de mesmo volume tem aresta \\(\\sqrt[3]{216} = 6\\) cm. Alternativa <strong>B</strong>.</p><p>Somar as arestas e dividir por três dá cerca de 8 cm, que não está nas opções: o certo é igualar os volumes.</p>",
  tags=["volume", "raiz cúbica"], enun=p(T(139, 0)))
X(140, "Raciocínio lógico", "<p>Com 4 ouros, 4 pratas e 10 bronzes a mais, o Brasil teria 9 ouros, 6 pratas e 13 bronzes. Entre os países com 9 ouros, a prata desempata: Coreia (12), Grã-Bretanha (9) e Cuba (7) ficam à frente; Ucrânia (5) fica atrás. O Brasil passaria para o <strong>12º lugar</strong>. Alternativa <strong>B</strong>.</p><p>O total de medalhas (C) não é critério de classificação.</p>",
  tags=["ordenação", "critérios de desempate"],
  enun=p(T(140, 0)) + tabela(["Classificação", "País", "Medalhas de ouro", "Medalhas de prata", "Medalhas de bronze", "Total de medalhas"],
    [["8º", "Itália", "10", "11", "11", "32"], ["9º", "Coreia do Sul", "9", "12", "9", "30"], ["10º", "Grã-Bretanha", "9", "9", "12", "30"], ["11º", "Cuba", "9", "7", "11", "27"], ["12º", "Ucrânia", "9", "5", "9", "23"], ["13º", "Hungria", "8", "6", "3", "17"]])
    + fonte("Disponível em: http://www.quadroademedalhas.com.br. Acesso em: 05 abr. 2010 (adaptado).") + p(T(140, 2).replace("das limpíadas de 2004? O", "das Olimpíadas de 2004?")))
X(141, "Porcentagem", "<p>No gráfico, 56% dos estudantes do Sudeste possuíam celular. De 14 900 entrevistados: 0,56 × 14 900 = <strong>8 344</strong>. Alternativa <strong>D</strong>.</p><p>A opção B (6 556) usa os 44% que não possuíam.</p>",
  figs(("q141", "Gráfico de colunas “Estudantes que possuem telefone móvel celular com idade de 10 anos ou mais”, por região, possuíam e não possuíam (%): Norte, 37 e 63; Nordeste, 36 e 64; Sudeste, 56 e 44; Sul, 62 e 38; Centro-Oeste, 58 e 42.")),
  ["porcentagem", "gráfico de colunas"], enun=p(T(141, 0)) + "[[fig:1]]" + fonte("Fonte: IBGE. Disponível em: http://www.ibge.gov.br. Acesso em: 28 abr. 2010 (adaptado).") + p(T(141, 2)))
X(142, "Funções", "<p>A altura cresce sempre (é uma função crescente e contínua): rápido de 0 a 10 anos, mais devagar de 10 a 17 e quase nada depois, até ficar constante. O gráfico que mostra isso, com inclinação cada vez menor, é o <strong>A</strong>. Alternativa <strong>A</strong>.</p><p>Os gráficos com degraus ou saltos (B, C, D e E) indicariam crescimento instantâneo ou paradas.</p>",
  figs(("q142a", "Gráfico A: altura sobe de 51 cm aos 0 anos até 148 aos 10, com inclinação forte; depois sobe menos até 171 aos 17; depois quase nada até 180."),
       ("q142b", "Gráfico B: sobe em reta até 148 aos 10, fica parado até perto dos 17, sobe em degrau até 171 e depois em degrau até 180."),
       ("q142c", "Gráfico C: segmentos verticais aos 10, 17 e mais adiante, sem crescimento contínuo."),
       ("q142d", "Gráfico D: sobe em reta até perto de 100 aos 10, salta para 148, sobe devagar até os 17, salta e depois fica quase constante."),
       ("q142e", "Gráfico E: em degraus: 51 até os 10, 148 até os 17, 171 depois e 180 no fim.")),
  ["gráfico de função", "taxa de variação"], enun=p(T(142, 0), T(142, 1)), alts=ALT(1))
X(143, "Estatística", "<p>Somando o desmatamento dos nove estados em 2004: 4 + 136 + 326 + 549 + 766 + 797 + 3 463 + 7 293 + 10 416 = 23 750 km². A média é 23 750 ÷ 9 ≈ 2 639 km². Com 10,5% a mais: 2 639 × 1,105 ≈ 2 916 km², entre <strong>2 800 km² e 3 200 km²</strong>. Alternativa <strong>C</strong>.</p>",
  figs(("q143", "Gráfico de barras “Ranking do Desmatamento em km²”: 1º Mato Grosso, 10 416; 2º Pará, 7 293; 3º Rondônia, 3 463; 4º Amazonas, 797; 5º Maranhão, 766; 6º Acre, 549; 7º Roraima, 326; 8º Tocantins, 136; 9º Amapá, 4.")),
  ["média aritmética", "porcentagem"], enun=p(T(143, 0).replace("ranking", "<em>ranking</em>")) + "[[fig:1]]" + fonte("Disponível em: www.folhaonline.com.br. Acesso em: 30 abr. 2010 (adaptado).") + p(T(143, 2)),
  alts={k: SUP(v) for k, v in D[143]["alternativas"].items()})
X(144, "Grandezas proporcionais", "<p>Pelas figuras: dobrando o comprimento (2ℓ), a resistência dobra (2R), proporção direta. Dobrando a área (2A), com o mesmo comprimento, a resistência cai à metade (R/2), proporção inversa. Para manter a mesma resistência R, dobrar o comprimento exige dobrar a área: direta. A resposta é <strong>direta, inversa e direta</strong>. Alternativa <strong>C</strong>.</p>",
  figs(("q144", "Esquema com um fio condutor de área A, comprimento ℓ e resistência R. Abaixo, três casos de fios do mesmo material: comprimento 2ℓ e área A, resistência 2R; área 2A e comprimento ℓ, resistência R/2; área 2A e comprimento 2ℓ, resistência R.")),
  ["proporcionalidade direta e inversa", "resistência elétrica"],
  enun=tit("A resistência elétrica e as dimensões do condutor") + p("A relação da resistência elétrica com as dimensões do condutor foi estudada por um grupo de cientistas por meio de vários experimentos de eletricidade. Eles verificaram que existe proporcionalidade entre:")
       + "<ul><li>resistência (R) e comprimento (ℓ), dada a mesma secção transversal (A);</li><li>resistência (R) e área da secção transversal (A), dado o mesmo comprimento (ℓ) e</li><li>comprimento (ℓ) e área da secção transversal (A), dada a mesma resistência (R).</li></ul>"
       + p(T(144, 5)) + "[[fig:1]]" + fonte(T(144, 7)) + p(T(144, 8).replace("(�)", "(ℓ)")))
X(145, "Porcentagem", "<p>Pelo gráfico, a taxa de desemprego de Porto Alegre era 9,8%. De 250 000 pessoas: 0,098 × 250 000 = <strong>24 500</strong>. Alternativa <strong>A</strong>.</p><p>As opções C, D e E se aproximam do número de empregados, e não de desempregados.</p>",
  figs(("q145", "Gráfico de barras “Taxas de desemprego nas regiões metropolitanas março/2010”: São Paulo 13,1; Salvador 19,9; Recife 19,3; Porto Alegre 9,8; Belo Horizonte 10,2; Distrito Federal 14,7.")),
  ["porcentagem", "gráfico de barras"], enun=p(T(145, 0)) + "[[fig:1]]" + fonte("Disponível em: http://g1.globo.com. Acesso em: 28 abr. 2010 (adaptado).") + p(T(145, 2)))
X(146, "Grandezas e medidas", "<p>Multiplicar comprimento, largura e altura (2,5 m × 0,5 m × 1,3 m) dá uma medida em m³: o espaço que a peça ocupa, ou seja, o <strong>volume</strong>. Alternativa <strong>B</strong>.</p><p>Capacidade (D) é o que cabe dentro de um recipiente; a peça é maciça. A massa (A) dependeria também da densidade do ferro.</p>",
  figs(("q146", "Paralelepípedo com a inscrição “Metal Nobre”, de 2,5 m de comprimento, 0,5 m de largura e 1,3 m de altura.")), ["volume", "grandezas"], enun=EF(146, 1))
X(147, "Probabilidade", "<p>Pela figura II: E1 = 0,8, E2 = 0,7, E3 = 0,5, E4 = 0,3, E5 = 0,4 e E6 = 0,6. A chance de não pegar engarrafamento em duas vias é o produto das chances de cada uma: E1E3, 0,2 × 0,5 = 0,10; E1E4, 0,2 × 0,7 = 0,14; E2E5, 0,3 × 0,6 = 0,18; E2E6, 0,3 × 0,4 = 0,12. O maior é <strong>E2E5</strong>, o trajeto com menor probabilidade de engarrafamento. Alternativa <strong>D</strong>.</p><p>E2E4 (C) não é possível: E2 vai de A a D e E4 liga C a B.</p>",
  figs(("q147", "Figura I: cidades A e B ligadas por dois caminhos, A–C–B e A–D–B; de A a C, via E1; de A a D, via E2; de C a B, vias E3 e E4; de D a B, vias E5 e E6. Figura II: as probabilidades de engarrafamento: E1 0,8; E2 0,7; E3 0,5; E4 0,3; E5 0,4; E6 0,6.")),
  ["eventos independentes", "complementar"], enun=EF(147, 1) )
X(148, "Leitura de gráficos", "<p>A guerra no Iraque começou em 2003, marcado no gráfico como “Início da guerra no Iraque”, com 417,4 bilhões de dólares. 417,4 bilhões = 417 400 000 000: <strong>US$ 417.400.000.000,00</strong>. Alternativa <strong>E</strong>.</p><p>As outras opções erram a quantidade de zeros de “bilhões”.</p>",
  figs(("q148", "Gráfico de linha “O gasto militar dos Estados Unidos supera o do fim da Guerra Fria”, em bilhões de dólares, de 1988 a 2006: começa em 426,8, cai após a queda do Muro de Berlim até cerca de 290 no fim dos anos 1990 e sobe depois do atentado de 11 de setembro; no início da guerra no Iraque, em 2003, marca 417,4, chegando a 528,7 em 2006.")),
  ["leitura de gráfico", "notação numérica"], enun=EF(148, 1, fnt="<em>Almanaque Abril 2008</em>. Editora Abril."))
X(149, "Sequências", "<p>Figura I: 1 quadrado, 4 canudos. Figura II: 2 quadrados, 7 canudos. Figura III: 3 quadrados, 10 canudos. Cada quadrado novo acrescenta 3 canudos, pois aproveita um lado do anterior: C = 4 + 3(Q − 1) = <strong>3Q + 1</strong>. Alternativa <strong>B</strong>.</p><p>C = 4Q (A) contaria os lados comuns duas vezes.</p>",
  figs(("q149", "Três figuras feitas com canudos: um quadrado; dois quadrados lado a lado; três quadrados lado a lado.")), ["padrões", "função afim"], enun=EF(149, 1))
X(150, "Áreas e perímetros", "<p>Ao dobrar largura e altura, a área de tela fica 4 vezes maior e o perímetro de moldura 2 vezes maior. Primeira: tela 8 × 0,125 m² = 1 m² (R$ 20), moldura 8 × 1,5 m = 12 m (R$ 180), entrega R$ 10: total R$ 210. Segunda: tela 4 m² (R$ 80), moldura 24 m (R$ 360), entrega R$ 10: R$ 450. O valor é <strong>maior do que o da primeira encomenda, mas não o dobro</strong>. Alternativa <strong>B</strong>.</p>",
  tags=["área e perímetro", "custo"])
X(151, "Geometria espacial", "<p>Leiteira: π · 4² · 20 = 320π cm³. Copinho: π · 2² · 4 = 16π cm³; vinte copinhos pela metade: 20 × 8π = 160π cm³, a metade da leiteira. Dona Maria deve <strong>encher a leiteira até a metade, pois ela tem um volume 20 vezes maior que o volume do copo</strong>. Alternativa <strong>A</strong>.</p>",
  figs(("q151", "Leiteira cilíndrica de 8 cm de diâmetro e 20 cm de altura, ao lado de um copinho cilíndrico de 4 cm de diâmetro e 4 cm de altura.")), ["volume do cilindro"], enun=EF(151, 1))
X(152, "Trigonometria", "<p>O cosseno varia de −1 a 1. O maior r (apogeu) ocorre com o menor denominador, cos = −1: 5 865 ÷ 0,85 = 6 900 km. O menor r (perigeu), com cos = 1: 5 865 ÷ 1,15 = 5 100 km. A soma é S = 6 900 + 5 100 = <strong>12 000 km</strong>. Alternativa <strong>B</strong>.</p>",
  tags=["função cosseno", "máximo e mínimo"],
  enun=p(T(152, 0).split(" r(t)")[0].replace("apogeu", "<em>apogeu</em>").replace("perigeu", "<em>perigeu</em>")) + p("\\(r(t) = \\dfrac{5\\,865}{1 + 0{,}15 \\cdot \\cos(0{,}06t)}\\)") + p(T(152, 1).replace("apogeu", "<em>apogeu</em>").replace("perigeu", "<em>perigeu</em>"), T(152, 2)))
X(153, "Geometria espacial", "<p>Para um cilindro, área lateral ÷ volume = 2πrh ÷ (πr²h) = 2/r: quanto maior o raio, menor o custo por m³. Os tanques I e II têm 4 m de diâmetro (r = 2, razão 1); o III tem 6 m de diâmetro (r = 3, razão 2/3). O escolhido é o <strong>III, com relação 2/3</strong>. Alternativa <strong>D</strong>.</p><p>O comprimento do tanque não altera essa razão.</p>",
  figs(("q153", "Três tanques cilíndricos deitados: I, 4 m de diâmetro e 6 m de comprimento; II, 4 m de diâmetro e 8 m de comprimento; III, 6 m de diâmetro e 8 m de comprimento.")),
  ["área lateral", "volume do cilindro"], enun=p(T(153, 0)) + "[[fig:1]]" + p("Qual dos tanques deverá ser escolhido pelo dono do posto? (Considere π ≅ 3)"),
  alts={k: f"{t}, pela relação área/capacidade de armazenamento de \\(\\frac{{{a}}}{{{b}}}\\)." for k, t, a, b in zip("ABCDE", ["I", "I", "II", "III", "III"], [1, 4, 3, 2, 7], [3, 3, 4, 3, 12])})
X(154, "Porcentagem", "<p>O lucro passou de R$ 132 000 para R$ 145 000: aumento de 13 000. 13 000 ÷ 132 000 ≈ 0,0985, ou cerca de 9,85%. Como fica entre 5% e 10%, o desempenho é <strong>bom</strong>. Alternativa <strong>C</strong>.</p><p>Calcular sobre 145 000 daria cerca de 9%, a mesma classificação, mas o certo é usar o ano anterior como base.</p>",
  tags=["variação percentual"], enun=p(T(154, 0).replace("insuficiente", "<strong>insuficiente</strong>").replace("regular,", "<strong>regular</strong>,").replace("bom,", "<strong>bom</strong>,").replace("ótimo,", "<strong>ótimo</strong>,").replace("excelente,", "<strong>excelente</strong>,"), T(154, 1)))
X(155, "Equações", "<p>500 folhetos do segundo tipo custam 500 × (0,65 + 0,60 + 0,20) = R$ 725 e usam 500 selos de R$ 0,65. Sobram R$ 275, que compram 275 ÷ 0,65 ≈ 423 selos de R$ 0,65 para o primeiro tipo. Total de selos de R$ 0,65: 500 + 423 = <strong>923</strong>. Alternativa <strong>C</strong>.</p><p>A opção A (476) esquece os selos de 0,65 dos folhetos do segundo tipo e erra a sobra.</p>",
  tags=["problema com dinheiro", "divisão"])
X(156, "Geometria analítica", "<p>Partindo de (20; 60): 0,8° L → (20,8; 60); 0,5° N → (20,8; 60,5); 0,2° O → (20,6; 60,5); 0,1° S → (20,6; 60,4); 0,4° N → (20,6; 60,8); 0,3° L → (20,9; 60,8). Nesse ponto fica a pequena mancha preta perto do canto superior direito do mapa. Na legenda, preto é 100 m (quanto mais escuro, mais baixo): altitude <strong>menor ou igual a 200 m</strong>. Alternativa <strong>A</strong>.</p><p>Leste e oeste mudam a longitude (horizontal); norte e sul, a latitude (vertical).</p>",
  figs(("q156", "Mapa de curvas de nível em tons de cinza, com longitude de 20,0 a 21,2 no eixo horizontal e latitude de 60,0 a 70,0 no vertical, legenda de altitudes de 100 m a 800 m e rosa dos ventos; o ponto X fica em (20; 60), no canto inferior esquerdo.")),
  ["coordenadas", "curvas de nível"], enun=EF(156, 1, depois=[T(156, 2), "0,8° L → 0,5° N → 0,2° O → 0,1° S → 0,4° N → 0,3° L.", T(156, 4), T(156, 5)]))
X(157, "Geometria espacial", "<p>O concreto forma um tubo entre o raio 1 m e o raio 1,2 m, com 4 m de altura: V = π(1,2² − 1²) · 4 = 3,1 × 0,44 × 4 = 5,456 m³. A R$ 10 o m³: <strong>R$ 54,56</strong>. Alternativa <strong>D</strong>.</p><p>Quem usa os diâmetros no lugar dos raios chega a valores muito maiores.</p>",
  tags=["volume do cilindro", "coroa circular"], enun=p(T(157, 0), T(157, 1).replace("de �", "de π")))
X(158, "Geometria espacial", "<p>Espécie I: V = 3² × 12 × 0,06 = 6,48 m³ por tora; 3 toras = 19,44 m³ × 0,77 ≈ 14,97 t. Espécie II: V = 4² × 10 × 0,06 = 9,6 m³ por tora; 2 toras = 19,2 m³ × 0,78 ≈ 14,98 t. Total ≈ <strong>29,9 toneladas</strong>. Alternativa <strong>A</strong>.</p>",
  figs(("q158", "Desenho de um homem medindo a circunferência de uma árvore na altura do peito, dizendo “Tem 2 metros de rodo”; ao lado, o quadro: o volume da tora em m³ é dado por V = rodo² × altura × 0,06; o rodo e a altura devem ser medidos em metros; o coeficiente 0,06 foi obtido experimentalmente.")),
  ["fórmula", "densidade"], enun=SUP(p(T(158, 0).replace("cubar", "<em>cubar</em>"))) + "[[fig:1]]" + p(T(158, 4)) + SUP(LISTA(T(158, 5))) + p(T(158, 6)))
X(159, "Funções", "<p>Com IMC = 25 e massa 64 kg: altura² = 64 ÷ 25 = 2,56, altura = 1,6 m = 160 cm. RIP = 160 ÷ \\(\\sqrt[3]{64}\\) = 160 ÷ 4 = <strong>40 cm/kg<sup>1/3</sup></strong>. Alternativa <strong>E</strong>.</p><p>Usar a altura em metros (1,6) daria 0,4 (A).</p>",
  tags=["fórmulas", "raiz cúbica"],
  enun=p(T(159, 0)) + p("\\(IMC = \\dfrac{\\text{massa (kg)}}{[\\text{altura (m)}]^2}\\) e \\(RIP = \\dfrac{\\text{altura (cm)}}{\\sqrt[3]{\\text{massa (kg)}}}\\)")
       + fonte("ARAUJO, C. G. S.; RICARDO, D. R. Índice de Massa Corporal: Um Questionamento Científico Baseado em Evidências. <em>Arq. Bras. Cardiologia</em>, volume 79, nº 1, 2002 (adaptado).") + p("Se uma menina, com 64 kg de massa, apresenta IMC igual a 25 kg/m<sup>2</sup>, então ela possui RIP igual a"),
  alts={k: f"{v} cm/kg<sup>1/3</sup>." for k, v in zip("ABCDE", ["0,4", "2,5", "8", "20", "40"])})
X(160, "Trigonometria", "<p>A primeira pessoa está a 1,8 km da vertical do balão e o vê a 60°: h = 1,8 · tg 60° = 1,8 × 1,73 ≈ <strong>3,1 km</strong>. Alternativa <strong>C</strong>.</p><p>A segunda pessoa confirma: tg 30° × 5,5 ≈ 0,577 × 5,5 ≈ 3,2 km, valor próximo.</p>",
  figs(("q160", "Triângulo retângulo com o balão no vértice de cima; na base, o ponto A a 1,8 km da vertical, com ângulo de 60°, e o ponto B, 3,7 km depois de A, com ângulo de 30°.")),
  ["tangente", "triângulo retângulo"], enun=p(T(160, 0)) + fonte(T(160, 1)) + "[[fig:1]]" + p(T(160, 3)))
X(161, "Geometria plana", "<p>M e N são pontos médios de BC e AC, então MN é base média: o triângulo MNC é semelhante a ABC com razão 1/2 e tem 1/4 da área. A região ABMN é o resto: 3/4 da área de ABC, ou seja, o <strong>triplo da área do triângulo MNC</strong>. Alternativa <strong>E</strong>.</p>",
  figs(("q161", "Triângulo retângulo ABC, com ângulo reto em A, B em cima e C à direita; P é o ponto médio de AB, M o de BC e N o de AC; a região ABMN está sombreada.")),
  ["base média", "semelhança"], enun=EF(161, 1))
X(162, "Áreas", "<p>A página tem 260 mm × 400 mm = 104 000 mm². Os 4% correspondem a 0,04 × 104 000 = 4 160 mm². Com largura de 26 mm: x = 4 160 ÷ 26 = <strong>160 mm</strong>. Alternativa <strong>D</strong>.</p><p>A figura desenha esse retângulo bem menor do que deveria; por isso a pergunta sobre fidedignidade.</p>",
  figs(("q162", "Página de jornal de 260 mm por 400 mm, quase toda escura com “96% Pessoas que consultam nossos classificados”; no canto superior esquerdo, um retângulo branco de 26 mm de largura e altura x mm com “4% outros jornais”.")),
  ["porcentagem", "área do retângulo"], enun=EF(162, 1))
X(163, "Geometria plana", "<p>Numa volta completa sem deslizar, o rolo avança 2πR em relação ao chão. O bloco, apoiado no topo do rolo, avança 2πR em relação ao rolo, que já se moveu 2πR: no total, y = <strong>4πR</strong>. Alternativa <strong>E</strong>.</p><p>2πR (D) seria o avanço do centro do rolo, e não do bloco.</p>",
  figs(("q163", "Desenho de trabalhadores empurrando um grande bloco de pedra apoiado sobre rolos cilíndricos de raio R.")), ["comprimento da circunferência", "rolamento"],
  enun=EF(163, 1, fnt="BOLT, Brian. <em>Atividades matemáticas</em>. Ed. Gradiva."), alts={k: f"y = {v}." for k, v in zip("ABCDE", ["R", "2R", "πR", "2πR", "4πR"])})
X(164, "Geometria plana", "<p>O cilindro tangente às faces laterais tem base inscrita no triângulo 6-8-10, que é retângulo (6² + 8² = 10²). O raio do círculo inscrito num triângulo retângulo é r = (6 + 8 − 10) ÷ 2 = <strong>2 cm</strong>. Alternativa <strong>B</strong>.</p><p>Outra conta: área ÷ semiperímetro = 24 ÷ 12 = 2.</p>",
  figs(("q164", "Prisma reto de base triangular, com lados da base de 6 cm, 8 cm e 10 cm, atravessado por um cilindro vertical tangente às três faces laterais.")), ["círculo inscrito", "triângulo retângulo"], enun=EF(164, 1) + p("O raio da perfuração da peça é igual a"))
X(165, "Funções", "<p>A temperatura chega a 48 °C no primeiro trecho: \\(\\frac{7}{5}t + 20 = 48\\), então t = 20 min. Chega a 200 °C no segundo trecho: \\(\\frac{2}{125}t^2 - \\frac{16}{5}t + 320 = 200\\), que dá t² − 200t + 7 500 = 0, com raízes 50 e 150; como t ≥ 100, t = 150. A peça fica 150 − 20 = <strong>130 minutos</strong>. Alternativa <strong>D</strong>.</p>",
  tags=["função definida por partes", "equação do 2º grau"],
  enun=p(T(165, 0)) + p("\\(T(t) = \\begin{cases} \\dfrac{7}{5}t + 20, & \\text{para } 0 \\le t < 100 \\\\ \\dfrac{2}{125}t^2 - \\dfrac{16}{5}t + 320, & \\text{para } t \\ge 100 \\end{cases}\\)") + p(T(165, 2)))
X(166, "Função afim", "<p>De 2004 (750) a 2010 (968) o número de favelas cresceu 218 em 6 anos. Mantendo o padrão, de 2010 a 2016 cresce mais 218: 968 + 218 = 1 186, que está entre 1 150 e 1 200. Alternativa <strong>C</strong>.</p><p>A opção B confunde: 218 a mais que 2010, e não que 2004.</p>",
  figs(("q166", "Gráfico de segmentos do número de favelas no Rio de Janeiro: 372 em 1980, 573 em 1992 e 750 em 2004.")), ["variação linear"],
  enun=EF(166, 1, fnt="Favela Tem Memória. <em>Época</em>. Nº 621, 12 abr. 2010 (adaptado)."))
X(167, "Estatística", "<p>São 18 Copas no gráfico. Em ordem, os gols dos artilheiros: 4, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 8, 8, 9, 9, 10, 11, 13. A mediana é a média do 9º e do 10º valores: (6 + 7) ÷ 2 = <strong>6,5 gols</strong>. Alternativa <strong>B</strong>.</p><p>A moda é 6 (A), e a média, cerca de 7,3 (D).</p>",
  figs(("q167", "Gráfico de pontos “Quantidades de Gols dos Artilheiros das Copas do Mundo”, de 1930 a 2006: 8, 5, 7, 9, 11, 13, 4, 9, 10, 7, 6, 6, 6, 6, 6, 6, 8 e 5 gols.")), ["mediana"],
  enun=p(T(167, 0)) + tit("Quantidades de Gols dos Artilheiros das Copas do Mundo") + "[[fig:1]]" + fonte(T(167, 3)) + p(T(167, 4)))
X(168, "Geometria espacial", "<p>A taça hemisférica de raio 3 cm tem volume \\(\\frac{1}{2} \\cdot \\frac{4}{3}\\pi \\cdot 3^3 = 18\\pi\\) cm³. A cônica, com raio 3: \\(\\frac{1}{3}\\pi \\cdot 9 \\cdot h = 3\\pi h\\). Igualando, 3πh = 18π e h = <strong>6 cm</strong>. Alternativa <strong>B</strong>.</p><p>Quem esquece que a taça é meia esfera chega a 12 (C).</p>",
  figs(("q168", "Figura 1: taça em forma de hemisfério de raio 3 cm. Figura 2: taça em forma de cone de raio 3 cm e altura h.")), ["volume do cone", "volume da esfera"],
  enun=p(T(168, 0)) + "[[fig:1]]" + p("Considere: \\(V_{esfera} = \\dfrac{4}{3}\\pi R^3\\) e \\(V_{cone} = \\dfrac{1}{3}\\pi R^2 h\\)", T(168, 3)))
X(169, "Equações", "<p>Se o primeiro salto é x, o segundo é x − 1,2 e o terceiro, x − 1,2 − 1,5 = x − 2,7. Somando: 3x − 3,9 = 17,4, então x = 7,1 m, entre <strong>7,0 m e 8,0 m</strong>. Alternativa <strong>D</strong>.</p>",
  tags=["equação do 1º grau"], enun=ap(T(169, 0)) + fonte(T(169, 1)) + p(T(169, 2)))
X(170, "Estatística", "<p>Os dois têm média 15. O desempate vai para a pontuação mais regular, isto é, a de menor dispersão: o desvio padrão de Marco (0,32) é muito menor que o de Paulo (4,97). O mais bem classificado é <strong>Marco, pois obteve menor desvio padrão</strong>. Alternativa <strong>B</strong>.</p>",
  tags=["desvio padrão", "regularidade"],
  enun=p(T(170, 0).replace(" Dados dos candidatos no concurso", "")) + tit("Dados dos candidatos no concurso")
       + tabela(["", "Matemática", "Português", "Conhecimentos Gerais", "Média", "Mediana", "Desvio Padrão"], [["Marco", "14", "15", "16", "15", "15", "0,32"], ["Paulo", "8", "19", "18", "15", "18", "4,97"]]) + p(T(170, 2)))
X(171, "Porcentagem", "<p>De 100 pacientes, 60 não foram curados e foram divididos em dois grupos de 30. No primeiro, 35% de 30 = 10,5; no segundo, 45% de 30 = 13,5. Os tratamentos inovadores curaram 24 dos 100 iniciais: <strong>24%</strong>. Alternativa <strong>B</strong>.</p><p>Somar 35% e 45% e dividir por 2 dá 40%, mas isso vale só para os 60%.</p>",
  tags=["porcentagem de porcentagem"])
X(172, "Porcentagem", "<p>Em 2006 o Brasil produziu 43% de 40 bilhões = 17,2 bilhões, e os EUA 45% = 18 bilhões. Em 2009 os EUA produzem 9 bilhões. Para manter 88% (35,2 bilhões), o Brasil deve produzir 26,2 bilhões: aumento de 9 ÷ 17,2 ≈ <strong>52,3%</strong>. Alternativa <strong>C</strong>.</p><p>Os 9 bilhões perdidos pelos EUA representam 22,5% da produção mundial (A), e não o aumento brasileiro.</p>",
  tags=["porcentagem", "variação percentual"])
X(173, "Análise combinatória", "<p>A partida e a chegada são em A; as outras cinco cidades podem ser visitadas em 5! = 120 ordens. Como cada trajeto e seu inverso têm o mesmo custo, basta examinar 60. A 1min30s cada: 60 × 1,5 = <strong>90 min</strong>. Alternativa <strong>B</strong>.</p><p>Examinar todas as 120 daria 180 min (D).</p>",
  figs(("q173", "Grafo com seis cidades, A, B, C, D, E e F, todas ligadas entre si, com o custo de cada deslocamento indicado nas arestas.")), ["permutação"], enun=EF(173, 1))
X(174, "Probabilidade", "<p>Calçam mais que 36,0: 39,0 (1), 38,0 (10) e 37,0 (3), total de 14 funcionárias. Das 14, 10 calçam 38: probabilidade \\(\\frac{10}{14} = \\frac{5}{7}\\). Alternativa <strong>D</strong>.</p><p>Usar as 25 funcionárias como total daria 2/5 (C).</p>",
  tags=["probabilidade condicional"],
  enun=p(T(174, 0)) + tabela(["Tamanho dos calçados", "Número de funcionárias"], [["39,0", "1"], ["38,0", "10"], ["37,0", "3"], ["36,0", "5"], ["35,0", "6"]]) + p(T(174, 2)),
  alts=FR("\\dfrac{1}{3}", "\\dfrac{1}{5}", "\\dfrac{2}{5}", "\\dfrac{5}{7}", "\\dfrac{5}{14}"))
X(175, "Estatística", "<p>São 20 jogos e 45 gols: média X = 2,25. Em ordem, os 10º e 11º valores são 2 e 2: mediana Y = 2. O valor mais frequente é 0 (5 jogos): moda Z = 0. Logo <strong>Z &lt; Y &lt; X</strong>. Alternativa <strong>E</strong>.</p>",
  tags=["média", "mediana", "moda"],
  enun=p(T(175, 0)) + tabela(["Gols marcados", "Quantidade de partidas"], [["0", "5"], ["1", "3"], ["2", "4"], ["3", "3"], ["4", "2"], ["5", "2"], ["7", "1"]]) + p(T(175, 2)),
  alts={k: v.replace("<", "&lt;") for k, v in D[175]["alternativas"].items()})
X(176, "Razão e proporção", "<p>Em Júpiter cabem 23 Netunos, e em cada Netuno cabem 58 Terras: 23 × 58 = <strong>1 334 Terras</strong>. Alternativa <strong>B</strong>.</p><p>Mercúrio e Marte não entram na conta, porque a pergunta compara Júpiter com a Terra.</p>",
  tags=["multiplicação", "proporção"], enun=ap(T(176, 0)) + fonte("<em>Revista Veja</em>. Ano 41, nº 25, 25 jun. 2008 (adaptado).") + p("Seguindo o raciocínio proposto, quantas Terras cabem dentro de Júpiter?"))
X(177, "Potenciação", "<p>10 L de óleo contaminam 10<sup>7</sup> L de água, ou seja, 1 L contamina 10<sup>6</sup> L. Com 1 000 = 10<sup>3</sup> L de óleo por semana: 10<sup>3</sup> × 10<sup>6</sup> = <strong>10<sup>9</sup> litros</strong>. Alternativa <strong>E</strong>.</p>",
  tags=["potências de 10"],
  enun=ap("Um dos grandes problemas da poluição dos mananciais (rios, córregos e outros) ocorre pelo hábito de jogar óleo utilizado em frituras nos encanamentos que estão interligados com o sistema de esgoto. Se isso ocorrer, cada 10 litros de óleo poderão contaminar 10 milhões (10<sup>7</sup>) de litros de água potável.")
       + fonte("Manual de etiqueta. Parte integrante das revistas <em>Veja</em> (ed. 2055), <em>Cláudia</em> (ed. 555), <em>National Geographic</em> (ed. 93) e <em>Nova Escola</em> (ed. 208) (adaptado).")
       + p(T(177, 2).split("(adaptado). ", 1)[1], T(177, 3)),
  alts={k: f"10<sup>{e}</sup>" for k, e in zip("ABCDE", ["−2", "3", "4", "6", "9"])})
X(178, "Geometria espacial", "<p>Volume de madeira = cubo maior − cubo interno vazio = 12³ − 8³ = 1 728 − 512 = <strong>1 216 cm³</strong>. Alternativa <strong>D</strong>.</p><p>A opção E (1 728) é o volume do cubo maior inteiro.</p>",
  figs(("q178", "Desenho em perspectiva de um cubo grande com um cubo menor dentro.")), ["volume do cubo"], enun=p(T(178, 0)) + "[[fig:1]]" + p(T(178, 1)),
  alts={k: SUP(v) for k, v in D[178]["alternativas"].items()})
X(179, "Sequências", "<p>As somas das linhas são 1, 1 + 2 + 1 = 4, 1 + 2 + 3 + 2 + 1 = 9, 1 + 2 + 3 + 4 + 3 + 2 + 1 = 16: quadrados perfeitos. A linha n soma n². A 9ª linha soma 9² = <strong>81</strong>. Alternativa <strong>D</strong>.</p>",
  tags=["padrões", "quadrados perfeitos"],
  enun=p("Ronaldo é um garoto que adora brincar com números. Numa dessas brincadeiras, empilhou caixas numeradas de acordo com a sequência conforme mostrada no esquema a seguir.")
       + '<p class="apoio" style="text-align:center">1<br>1 2 1<br>1 2 3 2 1<br>1 2 3 4 3 2 1<br>...</p>'
       + p("Ele percebeu que a soma dos números em cada linha tinha uma propriedade e que, por meio dessa propriedade, era possível prever a soma de qualquer linha posterior às já construídas.", "A partir dessa propriedade, qual será a soma da 9ª linha da sequência de caixas empilhadas por Ronaldo?"))
X(180, "Leitura de gráficos", "<p>Pelo gráfico: 2005, 90 milhões; 2006, 94; 2007, 99; 2008, 107; 2009, 113. Biênios: 2005-2006, 184; 2006-2007, 193; 2007-2008, 206; 2008-2009, 220 milhões. O maior é <strong>2008-2009</strong>. Alternativa <strong>E</strong>.</p><p>2004-2005 (A) nem tem os dois anos no gráfico.</p>",
  figs(("q180", "Gráfico de linha “Produção recorde”, do número de ovos de Páscoa produzidos no Brasil: 90 milhões em 2005, 94 em 2006, 99 em 2007, 107 em 2008 e 113 em 2009.")), ["leitura de gráfico", "soma"],
  enun=EF(180, 1, fnt="<em>Revista Veja</em>. São Paulo: Abril, ed. 2107, nº 14, ano 42."))

completar(Q, R)
