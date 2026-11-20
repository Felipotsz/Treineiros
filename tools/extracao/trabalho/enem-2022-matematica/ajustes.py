# Enem 2022, 2º dia, caderno azul: Matemática (questões 136 a 180 do caderno; no site, 1 a 45, com numeroOriginal).
# Frações, fórmulas e funções por partes em KaTeX; quadros em tabela HTML; alternativas-imagem nas Q143, 156, 160 e 180.
# Q157 anulada pelo Inep sem motivo publicado: pela análise, nenhuma alternativa está certa (a E traria 625 no lugar de 675).
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, paragrafos_enem

ID = "enem-2022-matematica"
META = {"id": ID, "banca": "Enem", "ano": 2022, "titulo": "Enem 2022: Matemática", "fonte": "Inep", "dataExame": "2022-11-20",
        "duracaoMinutos": 150, "area": "Matemática", "caderno": "azul", "dia": 2}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2022-dia2-azul")
Q = {}
P = lambda n: paragrafos_enem(D[n])
T = lambda n, i: P(n)[i][1]
p = lambda *xs: "".join(f"<p>{x}</p>" for x in xs)
ap = lambda *xs: "".join(f'<p class="apoio">{x}</p>' for x in xs)
fonte = lambda x: f'<p class="fonte">{x}</p>'
LISTA = lambda s: "<ul>" + "".join(f"<li>{x.strip()}</li>" for x in s.split("•") if x.strip()) + "</ul>"
ALT = lambda ini: {k: f"[[fig:{i}]]" for i, k in enumerate("ABCDE", ini)}
FR = lambda *xs: {k: f"\\({v}\\)" for k, v in zip("ABCDE", xs)}


def BL(s, marca):
    """Lista com marcadores colada ao parágrafo seguinte: separa em lista + parágrafo."""
    i = s.index(marca); return LISTA(s[:i]) + p(s[i:].strip())


def figs(*pares):
    return [{"arquivo": a, "alt": t} for a, t in pares]


def tabela(cab, linhas):
    return ('<table class="tabela"><thead><tr>' + "".join(f"<th>{c}</th>" for c in cab) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in l) + "</tr>" for l in linhas) + "</tbody></table>")


def E(n, pular=(), trocas=()):
    par = [x for i, x in enumerate(P(n)) if i not in pular]
    ult = max([i for i, (t, _) in enumerate(par) if t == "fonte"], default=-1)
    h = []
    for i, (t, x) in enumerate(par):
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


X(136, "Funções", "<p>V = T² − 4 se anula quando T = 2 ou T = −2. No gráfico, a curva começa perto de 3 °C, sobe a 4, desce cruzando T = 2 (1ª vez), encosta em −2 três vezes (2ª, 3ª e 4ª) e, na subida final, cruza T = 2 de novo (5ª). São <strong>5 vezes</strong>. Alternativa <strong>E</strong>.</p><p>Contar só os pontos em −2 (C) ou só os cruzamentos em 2 (B) esquece metade das soluções.</p>",
  figs(("q136", "Gráfico da temperatura T (°C) em função do tempo t (h), de 0 a 10 h, com linhas tracejadas em 4, 2 e −2: a curva começa em cerca de 3, sobe a 4, desce cruzando o 2, toca o −2 três vezes (com dois pequenos picos em 0 entre elas) e depois sobe, cruzando o 2 e chegando perto de 3,5 antes de cair um pouco em 10 h.")),
  ["equação do 2º grau", "leitura de gráfico"],
  enun=p(T(136, 0).replace("T 2 − 4", "T<sup>2</sup> − 4")) + "[[fig:1]]" + p(T(136, 4)))
X(137, "Probabilidade", "<p>O time que venceu o 1º jogo precisa de mais 3 vitórias antes de o outro fazer 4, em no máximo 6 jogos restantes. Equivale a ganhar pelo menos 3 de 6 jogos “completados”: P = [C(6,3) + C(6,4) + C(6,5) + C(6,6)] ÷ 2⁶ = (20 + 15 + 6 + 1) ÷ 64 = \\(\\frac{42}{64}\\). Alternativa <strong>C</strong>.</p><p>\\(\\frac{35}{64}\\) (A) conta só as séries até o fim, sem completar os jogos.</p>",
  tags=["distribuição binomial"],
  enun=ap(T(137, 0).replace("A World Series", "A <em>World Series</em>")) + p("Considere que, em todas as partidas, a probabilidade de qualquer um dos dois times vencer é sempre \\(\\frac{1}{2}\\).", T(137, 3).replace("da World Series", "da <em>World Series</em>")),
  alts=FR("\\frac{35}{64}", "\\frac{40}{64}", "\\frac{42}{64}", "\\frac{44}{64}", "\\frac{52}{64}"))
X(138, "Estatística", "<p>Lucro é só quando a receita supera a despesa. Pelo gráfico, os meses com lucro são: jan. (6 − 3 = 3), mar. (3 − 2 = 1), maio (6 − 1 = 5), jun. (5 − 2 = 3), jul. (6 − 4 = 2), set. (7 − 3 = 4), nov. (8 − 7 = 1) e dez. (6 − 2 = 4). Em ordem: 1, 1, 2, 3, 3, 4, 4, 5. A mediana é a média dos dois centrais: (3 + 3) ÷ 2 = <strong>3,0</strong>. Alternativa <strong>D</strong>.</p><p>Incluir os prejuízos como lucros negativos daria 1,5 (A).</p>",
  figs(("q138", "Gráfico de barras de receitas (pretas) e despesas (cinza), em milhão de reais, de janeiro a dezembro: jan. 6 e 3; fev. 4 e 5; mar. 3 e 2; abr. 5 e 6; maio 6 e 1; jun. 5 e 2; jul. 6 e 4; ago. 2 e 4; set. 7 e 3; out. 2 e 4; nov. 8 e 7; dez. 6 e 2.")),
  ["mediana", "leitura de gráfico"], enun=p(T(138, 0)) + "[[fig:1]]" + p(T(138, 4)))
X(139, "Escala", "<p>Na escala 1 : 50, o espaço tem 3,8 · 50 = 190 cm de altura e 1,6 · 50 = 80 cm de largura. Descontando 10 cm em cima, a altura máxima é 1,80 m; descontando 10 cm de cada lado, a largura máxima é 0,60 m. Alternativa <strong>A</strong>.</p><p>0,70 m (B) desconta só um dos lados.</p>",
  tags=["escala", "conversão de unidades"])
X(140, "Raciocínio lógico", "<p>Cada time joga 3 vezes na fase de grupos, com 3 dias de descanso: dias 1, 5 e 9. Depois, oitavas no dia 13, quartas no 17, semifinais no 21 e final no dia <strong>25</strong>. Alternativa <strong>B</strong>.</p><p>48 e 64 (D e E) não aproveitam os jogos simultâneos.</p>",
  tags=["contagem", "sequências"])
X(141, "Probabilidade", "<p>Pedro tem 03, 48 e 27 na 1ª linha (falta 12), 27 e 07 na 4ª coluna (faltam 05 e 45) e 03 e 07 na diagonal (faltam 11 e 19). Ganha se sair 12 na 5ª rodada (\\(\\frac{1}{46}\\)) ou se, sem o 12 na 5ª, ele vier na 6ª (\\(\\frac{45}{46} \\cdot \\frac{1}{45} = \\frac{45}{46 \\times 45}\\)), ou se saírem os dois números da coluna ou da diagonal (\\(\\frac{2+2}{46 \\times 45}\\)). Total: \\(\\frac{1}{46} + \\frac{49}{46 \\times 45}\\). Alternativa <strong>E</strong>.</p>",
  figs(("q141a", "Figura 1: três cartelas 4 × 4 mostrando o preenchimento em linha (quatro pontos numa linha), em coluna (quatro pontos numa coluna) e em diagonal (quatro pontos na diagonal)."),
       ("q141b", "Figura 2: a cartela de Pedro, com os números 03, 48, 12, 27 / 49, 11, 22, 05 / 29, 50, 19, 45 / 33, 23, 38, 07; estão circulados 03, 48, 27 e 07.")),
  ["probabilidade condicional", "bingo"],
  enun=p(T(141, 0)) + "[[fig:1]]" + p(T(141, 6)) + "[[fig:2]]" + p(T(141, 9)),
  alts=FR("\\frac{1}{46} + \\frac{1}{45}", "\\frac{1}{46} + \\frac{2}{46 \\times 45}", "\\frac{1}{46} + \\frac{8}{46 \\times 45}", "\\frac{1}{46} + \\frac{43}{46 \\times 45}", "\\frac{1}{46} + \\frac{49}{46 \\times 45}"))
X(142, "Análise combinatória", "<p>Opcionais: cada um dos 3 pode entrar ou não, 2³ = 8 escolhas. Sem as cores, há 7 · 2 · 8 = 112 configurações. Para passar de 1 000: 112 · c &gt; 1 000, c &gt; 8,9. São necessárias, no mínimo, <strong>9 cores</strong>. Alternativa <strong>B</strong>.</p><p>Com 8 cores (A) seriam 896 configurações.</p>",
  tags=["princípio multiplicativo"])
X(143, "Geometria espacial", "<p>Os três quadrados escuros ficam num mesmo vértice do cubo, em três faces que se encontram ali. Na planificação em escada, é preciso localizar as três faces vizinhas desse vértice e pôr cada quadrado no canto que toca o vértice comum. A planificação que faz isso é a <strong>D</strong>. Alternativa <strong>D</strong>.</p><p>Nas outras, pelo menos um quadrado escuro está num canto que não se encontra com os demais depois de montar o cubo.</p>",
  figs(("q143a", "Figura 1: planificação do cubo em forma de escada, com seis quadrados: dois na primeira linha, dois na segunda deslocados, e dois na terceira."),
       ("q143b", "Figura 2: cubo em perspectiva com um quadrado cinza escuro em cada uma de três faces (frontal, superior e lateral direita), ocupando um quarto da face e todos encostados no vértice comum dessas faces."),
       ("q143_a", "Planificação A, com quadrados escuros em cantos de três faces."),
       ("q143_b", "Planificação B, com quadrados escuros em cantos de três faces."),
       ("q143_c", "Planificação C, com quadrados escuros em cantos de três faces."),
       ("q143_d", "Planificação D, com quadrados escuros em cantos de três faces."),
       ("q143_e", "Planificação E, com quadrados escuros em cantos de três faces.")),
  ["planificação do cubo", "visualização espacial"], alts=ALT(3),
  enun=p(T(143, 0)) + "[[fig:1]]" + p(T(143, 3)) + "[[fig:2]]" + p(T(143, 6)))
X(144, "Aritmética", "<p>Com 0100: S = 5 · 0 + 4 · 1 + 3 · 0 + 2 · 0 = 4. O resto de 4 por 11 é R = 4, e N<sub>5</sub> = 11 − 4 = <strong>7</strong>. Alternativa <strong>C</strong>.</p><p>Usar o resto como dígito daria 4, que não está entre as alternativas.</p>",
  figs(("q144", "Cinco caixas com N₁, N₂, N₃, N₄, um traço e N₅.")),
  ["divisão e resto", "dígito verificador"],
  enun=p("Cada número que identifica uma agência bancária tem quatro dígitos: N<sub>1</sub>, N<sub>2</sub>, N<sub>3</sub>, N<sub>4</sub> mais um dígito verificador N<sub>5</sub>.") + "[[fig:1]]"
       + p("Todos esses dígitos são números naturais pertencentes ao conjunto {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}. Para a determinação de N<sub>5</sub>, primeiramente multiplica-se ordenadamente os quatro primeiros dígitos do número da agência por 5, 4, 3 e 2, respectivamente, somam-se os resultados e obtém-se S = 5 N<sub>1</sub> + 4 N<sub>2</sub> + 3 N<sub>3</sub> + 2 N<sub>4</sub>.",
           "Posteriormente, encontra-se o resto da divisão de S por 11, denotando por R esse resto. Dessa forma, N<sub>5</sub> é a diferença 11 − R.",
           "Considere o número de uma agência bancária cujos quatro primeiros dígitos são 0100. Qual é o dígito verificador N<sub>5</sub> dessa agência bancária?"))
X(145, "Razão e proporção", "<p>No pacote básico há 100 000 ÷ 2 000 = 50 moedas por gema. O gabarito oficial considera um pacote especial com 2 000 + 6 000 = 8 000 gemas, o que exige 8 000 · 50 = <strong>400 000</strong> moedas. Alternativa <strong>E</strong>.</p><p>Pela análise do Treineiros, a leitura literal do enunciado (6 000 gemas a mais que os 4 000 de dois pacotes básicos) levaria a 10 000 gemas e 500 000 moedas, valor que não aparece nas alternativas; a resposta oficial só sai tomando um pacote básico como base.</p>",
  tags=["proporção"], trocas=[("jogo para smartphone", "jogo para <em>smartphone</em>")])
X(146, "Sistemas lineares", "<p>Sejam M e m as voltas dos circuitos maior e menor: 3M + 2m = 1 800 e 2M + m = 1 100. Da segunda, m = 1 100 − 2M; na primeira, 3M + 2 200 − 4M = 1 800, M = 400 e m = 300. Para 5 000 m com o maior número de voltas, usa-se o circuito menor ao máximo: 400a + 300b = 5 000 com a + b máximo dá a = 2, b = 14, total <strong>16</strong> voltas. Alternativa <strong>E</strong>.</p><p>Só com o menor, 5 000 ÷ 300 não é inteiro; a = 2 é o menor valor que resolve.</p>",
  tags=["sistema de equações", "números inteiros"])
X(147, "Porcentagem", "<p>Compradores na 1ª divulgação: rede A, 3 000 · 10% · 3% = 9; rede B, 1 000 · 30% · 2% = 6; total 15. Investindo mais R$ 300 em cada rede, o novo público é proporcional: A recebe 3 vezes o investimento inicial (9 · 3 = 27 novos compradores) e B, 1,5 vez (6 · 1,5 = 9). A segunda divulgação gera 27 + 9 = 36 compradores, contra 15 da primeira: um aumento de (36 − 15) ÷ 15 = 140%, classificado como <strong>bom</strong>. Alternativa <strong>C</strong>.</p><p>Dividir 36 por 15 sem descontar a base daria 240%, fora de todas as faixas.</p>",
  tags=["proporcionalidade", "porcentagem"],
  enun=p(T(147, 0)) + BL(T(147, 1), "Por experiência") + p(T(147, 2)) + BL(T(147, 3), "O aumento na quantidade"))
X(148, "Potências", "<p>L = c · R² · T⁴. Com R<sub>E</sub> = R<sub>F</sub>/2 e T<sub>E</sub> = 2T<sub>F</sub>: L<sub>E</sub> = c · (R<sub>F</sub>/2)² · (2T<sub>F</sub>)⁴ = c · R<sub>F</sub>² · T<sub>F</sub>⁴ · (1/4) · 16 = <strong>4L<sub>F</sub></strong>. Alternativa <strong>D</strong>.</p><p>8L<sub>F</sub> (E) esquece de elevar o raio ao quadrado.</p>",
  tags=["proporcionalidade", "potências"],
  enun=p("A luminosidade <em>L</em> de uma estrela está relacionada com o raio <em>R</em> e com a temperatura <em>T</em> dessa estrela segundo a Lei de Stefan-Boltzmann: \\(L = c \\cdot R^2 \\cdot T^4\\), em que <em>c</em> é uma constante igual para todas as estrelas.") + fonte(T(148, 1))
       + p("Considere duas estrelas <em>E</em> e <em>F</em>, sendo que a estrela <em>E</em> tem metade do raio da estrela <em>F</em> e o dobro da temperatura de <em>F</em>.", "Indique por \\(L_E\\) e \\(L_F\\) suas respectivas luminosidades.", "A relação entre as luminosidades dessas duas estrelas é dada por"),
  alts=FR("L_E = \\frac{L_F}{2}", "L_E = \\frac{L_F}{4}", "L_E = L_F", "L_E = 4L_F", "L_E = 8L_F"))
X(149, "Estatística", "<p>São 100 + 400 + 200 + 150 + 100 + 50 = 1 000 famílias. A mediana é a média do 500º e do 501º valores. Acumulando: 0 criança até a 100ª família, 1 criança até a 500ª, 2 crianças da 501ª à 700ª. Então a mediana é (1 + 2) ÷ 2 = <strong>1,5</strong>. Alternativa <strong>B</strong>.</p><p>1,9 (C) é a média; 1 (A) é a moda.</p>",
  tags=["mediana", "tabela de frequências"],
  enun=p(T(149, 0)) + tabela(["Número de crianças por família", "Frequência"], [["0", "100"], ["1", "400"], ["2", "200"], ["3", "150"], ["4", "100"], ["5", "50"]]) + p(T(149, 2)))
X(150, "Funções", "<p>A altura máxima da parábola \\(y = -\\frac{x^2}{6} + \\frac{7x}{3} + 12\\) está no vértice: x = \\(\\frac{7/3}{2 \\cdot 1/6}\\) = 7, e y = −49/6 + 49/3 + 12 = 49/6 + 12 ≈ 20,17 m acima do eixo. Somando 1,5 m até o piso: ≈ 21,67 m. O saque bate no teto dos ginásios de 17, 18, 19 e 21 m, mas não no de 40 m: <strong>apenas nos ginásios I, II, III e IV</strong>. Alternativa <strong>D</strong>.</p><p>Esquecer de somar 1,5 m (≈ 20,17 m) levaria a C.</p>",
  figs(("q150", "Quadra de vôlei em perspectiva com a rede no meio; um jogador saca de uma ponta. A trajetória da bola é uma parábola tracejada que sobe acima da rede e desce do outro lado. O eixo x fica 1,5 m acima do piso e o eixo y passa pelo meio da quadra.")),
  ["função quadrática", "vértice da parábola"],
  enun=p("Em jogos de voleibol, um saque é invalidado se a bola atingir o teto do ginásio onde ocorre o jogo. Um jogador de uma equipe tem um saque que atinge uma grande altura. Seu recorde foi quando a batida do saque se iniciou a uma altura de 1,5 m do piso da quadra, e a trajetória da bola foi descrita pela parábola \\(y = -\\frac{x^2}{6} + \\frac{7x}{3} + 12\\), em que <em>y</em> representa a altura da bola em relação ao eixo <em>x</em> (das abscissas) que está localizado a 1,5 m do piso da quadra, como representado na figura. Suponha que em todas as partidas algum saque desse jogador atinja a mesma altura do seu recorde.")
       + "[[fig:1]]" + p(T(150, 4)) + BL(T(150, 5), "O saque desse atleta"))
X(151, "Porcentagem", "<p>A água recomendada é 1,4 vez a massa perdida. Com 1,7 L ingeridos: massa perdida = 1,7 ÷ 1,4 ≈ 1,21 kg. A 1,5 kg por hora, isso é 1,21 ÷ 1,5 ≈ 0,81 h ≈ 48,6 minutos: <strong>mais de 45 e menos de 55 minutos</strong>. Alternativa <strong>C</strong>.</p><p>Calcular 40% a menos, em vez de 40% a mais, daria cerca de 75 minutos (E).</p>",
  tags=["porcentagem", "proporção"])
X(152, "Grandezas e medidas", "<p>Com L = 12 m, a primeira fileira fica a 0,6 · 12 = 7,2 m da tela. O limite aceitável é 2,9 · 12 = 34,8 m. Com 1 m entre fileiras, cabem fileiras em 7,2; 8,2; …; até 34,2 m: são (34,2 − 7,2) + 1 = <strong>28 fileiras</strong>. Alternativa <strong>C</strong>.</p><p>27 (B) esquece de contar a primeira fileira; 35 (E) usa 2,9L sem descontar a distância mínima.</p>",
  figs(("q152", "À esquerda, a planta da sala de cinema em forma de trapézio: a tela de largura L embaixo, a primeira fileira a D_mín = 0,6L, a última a D_máx = 2L e, nos fundos, a “área de instalação de novas poltronas”, até D_aceitável = 2,9L. À direita, três fileiras de poltronas separadas por 1 m.")),
  ["sequências", "medidas"],
  enun=p(T(152, 0)) + BL(T(152, 1), "Para o espaçamento").replace("(Dmín)", "(D<sub>mín</sub>)").replace("(Dmáx)", "(D<sub>máx</sub>)") + fonte(T(152, 2)) + p(T(152, 3)) + "[[fig:1]]" + p(T(152, 7)))
X(153, "Geometria espacial", "<p>Com a mesma altura, o volume do cone é proporcional ao quadrado do raio. Volume 19% menor: r² = 0,81 · 4², r = 0,9 · 4 = <strong>3,60 cm</strong>. Alternativa <strong>C</strong>.</p><p>3,24 (B) aplica 0,81 ao raio, sem a raiz; 7,20 (E) usa o diâmetro.</p>",
  figs(("q153", "Cone circular reto de ponta para baixo, com diâmetro da base de 8 cm e altura de 10 cm.")),
  ["volume do cone", "semelhança"], enun=p(T(153, 0)) + "[[fig:1]]" + p(T(153, 4)))
X(154, "Porcentagem", "<p>Uma queda de 75% significa que as 28 900 vagas de 2013 correspondem a 25% das de 2012. Então 2012 teve 28 900 ÷ 0,25 = <strong>115 600</strong> vagas. Alternativa <strong>C</strong>.</p><p>86 700 (B) soma 75% sobre o valor de 2013, em vez de partir do valor de 2012.</p>",
  tags=["porcentagem"])
X(155, "Análise combinatória", "<p>Em cada andar, pelo menos um quarto recebe sol de manhã nos apartamentos de final 1 e 2 (os dois quartos) e 3, 4, 5 e 6 (um quarto); os finais 7 e 8 ficam de fora. São 6 apartamentos por andar; escolher 2 deles: \\(\\frac{6!}{(6-2)! \\cdot 2!}\\) = 15. Em 9 andares: \\(9 \\times \\frac{6!}{(6-2)! \\times 2!}\\). Alternativa <strong>B</strong>.</p><p>A (sem o 2!) conta a ordem da escolha; C usa só os 4 apartamentos de um quarto com sol.</p>",
  tags=["combinação"],
  enun=p(T(155, 0)) + BL(T(155, 1), "Uma pessoa pretende"),
  alts=FR("9 \\times \\frac{6!}{(6-2)!}", "9 \\times \\frac{6!}{(6-2)! \\times 2!}", "9 \\times \\frac{4!}{(4-2)! \\times 2!}", "9 \\times \\frac{2!}{(2-2)! \\times 2!}", "9 \\times \\left(\\frac{8!}{(8-2)! \\times 2!} - 1\\right)"))
X(156, "Geometria plana", "<p>O papel foi dobrado duas vezes, ficando com 4 camadas; o ponto O é o centro do quadrado original. O arco, de centro R (a 1/4 de OM) e raio OM/2, corta uma região que vai de O até um pouco além do meio de OM. Ao desdobrar, esse corte se repete 4 vezes por simetria em torno do centro, formando um buraco com 4 lóbulos arredondados (uma “flor” de 4 pétalas encostadas). É a figura <strong>C</strong>. Alternativa <strong>C</strong>.</p><p>B seria um único círculo (corte centrado em O); A tem lóbulos maiores e vãos estreitos; E corta só duas regiões.</p>",
  figs(("q156a", "Figuras 1, 2 e 3: um quadrado é dobrado ao meio pela diagonal (formando um triângulo) e depois de novo ao meio, formando um triângulo menor com vértice O no centro do quadrado original."),
       ("q156b", "Figura 4: no triângulo dobrado, o ponto O, o ponto R sobre o segmento OM e um arco de circunferência com centro em R. Figura 5: o papel depois de retirada a parte do arco, com um recorte curvo."),
       ("q156_a", "Alternativa A: quadrado cinza com um buraco branco formado por quatro lóbulos grandes e arredondados."),
       ("q156_b", "Alternativa B: quadrado cinza com um buraco branco circular."),
       ("q156_c", "Alternativa C: quadrado cinza com um buraco branco em forma de flor de quatro pétalas arredondadas."),
       ("q156_d", "Alternativa D: quadrado cinza com um buraco branco em forma de elipse."),
       ("q156_e", "Alternativa E: quadrado cinza com dois setores brancos opostos pelo vértice, como uma ampulheta deitada.")),
  ["simetria", "dobraduras"], alts=ALT(3),
  enun=p(T(156, 0)) + LISTA("Dobrar uma folha de papel em formato quadrado duas vezes, em sequência, ao longo das linhas tracejadas, conforme ilustrado nas figuras 1 e 2, para obter o papel dobrado, conforme Figura 3.") + "[[fig:1]]"
       + LISTA("Em seguida, no papel dobrado da Figura 3, considerar o ponto R, sobre o segmento OM, sendo M o ponto médio do lado do quadrado original, de modo que \\(OR = \\frac{1}{4} OM\\), traçar um arco de circunferência de raio medindo \\(\\frac{1}{2} OM\\) com centro no ponto R, obtendo a Figura 4. Por último, recortar o papel ao longo do arco de circunferência e excluir a parte que contém o setor circular, obtendo o papel dobrado, conforme Figura 5.")
       + "[[fig:2]]" + p("Após desdobrado o papel que restou na Figura 5, a figura plana que os estudantes obterão será"))
X(157, "Funções", "<p>Pela análise do Treineiros, o salário correto é: até 50 peças, S(q) = 675 + 5q; acima de 50, S(q) = 675 + 5 · 50 + 7(q − 50) = 575 + 7q. A alternativa E traz 575 + 7q, mas escreve 625 + 5q na primeira parte; nenhuma alternativa está certa. A resposta esperada seria a E, com 675 no lugar de 625. Alternativa <strong>E</strong>, se a questão não tivesse sido anulada.</p>",
  tags=["função definida por partes"],
  anulacao={"fonte": "analise", "motivo": "O Inep anulou a questão sem divulgar o motivo; disse apenas que os candidatos não seriam prejudicados nem beneficiados. Pela análise, nenhuma alternativa traz a função correta: a mais próxima (E) tem 625 no lugar de 675 na parcela de até 50 peças."},
  enun=p(T(157, 0)) + BL(T(157, 1), "Represente por q").replace("Represente por q", "Represente por <em>q</em>").replace("e por S(q)", "e por <em>S</em>(<em>q</em>)").replace("descreve S(q) em função de q", "descreve <em>S</em>(<em>q</em>) em função de <em>q</em>"),
  alts=FR("S(q) = 675 + 12q", "S(q) = 325 + 12q", "S(q) = 675 + 7q", "S(q) = \\begin{cases} 625 + 5q, & \\text{se } q \\le 50 \\\\ 925 + 7q, & \\text{se } q > 50 \\end{cases}", "S(q) = \\begin{cases} 625 + 5q, & \\text{se } q \\le 50 \\\\ 575 + 7q, & \\text{se } q > 50 \\end{cases}"))
X(158, "Funções", "<p>p(t) = −t² + 10t + 24 tem o máximo no vértice, t = −10 ÷ (2 · (−1)) = 5: o mês 5 tem o maior número de infectados (49). A proposta que inclui t = 5 é a <strong>III</strong> (5 ≤ t ≤ 6). Alternativa <strong>C</strong>.</p><p>As raízes da função (−2 e 12) não indicam o máximo.</p>",
  tags=["função quadrática", "vértice"],
  enun=p(T(158, 0).replace("−t 2 +", "−t<sup>2</sup> +")) + BL(T(158, 1), "A sugestão dos peritos"))
X(159, "Sequências", "<p>A sequência tem 13 dias e se repete. 24 semanas são 168 dias, e a 24ª semana vai do dia 162 ao 168. Como 156 = 12 · 13, o dia 162 é o 6º da sequência e o dia 168 é o 12º. Do 6º ao 12º: R, T<sub>3</sub>, R, T<sub>4</sub>, R, R, T<sub>5</sub>. Alternativa <strong>B</strong>.</p>",
  tags=["sequência periódica", "divisão e resto"],
  enun=p(T(159, 0).replace("treino T1, treino T2, treino T3, treino T4 e treino T5", "treino T<sub>1</sub>, treino T<sub>2</sub>, treino T<sub>3</sub>, treino T<sub>4</sub> e treino T<sub>5</sub>"))
       + tabela(["Dia"] + [f"{i}º" for i in range(1, 14)], [["Treino", "T<sub>1</sub>", "R", "R", "T<sub>2</sub>", "R", "R", "T<sub>3</sub>", "R", "T<sub>4</sub>", "R", "R", "T<sub>5</sub>", "R"]])
       + p(T(159, 1).replace("treino T1", "treino T<sub>1</sub>")),
  alts={k: re.sub(r"T(\d)", r"T<sub>\1</sub>", v) for k, v in D[159]["alternativas"].items()})
X(160, "Geometria espacial", "<p>Seguindo as regras (centro da face, alternando esquerda e direita), o robô passa pelas seis faces e volta a P. Projetando o trajeto no plano da base, os segmentos sobre as faces laterais viram linhas nas bordas da base, e os da face superior e inferior se sobrepõem no centro, formando a figura <strong>A</strong>. Alternativa <strong>A</strong>.</p>",
  figs(("q160", "Cubo em perspectiva com o trajeto inicial do robô: parte de P, no centro da face superior, vai até a borda, desce pela face lateral direita até o centro dela, vira e segue para a face frontal, e continua descendo."),
       ("q160_a", "Projeção A: um paralelogramo dividido em quatro partes por uma linha horizontal e uma vertical, com uma das partes sem a borda externa."),
       ("q160_b", "Projeção B: um paralelogramo dividido em quatro partes iguais, todo contornado."),
       ("q160_c", "Projeção C: apenas metade do paralelogramo, dividida em duas partes."),
       ("q160_d", "Projeção D: um paralelogramo dividido ao meio por uma única linha."),
       ("q160_e", "Projeção E: um paralelogramo dividido em quatro partes, com outro conjunto de bordas faltando.")),
  ["projeção ortogonal", "visualização espacial"], alts=ALT(2),
  enun=p(T(160, 0)) + "[[fig:1]]" + p(T(160, 2)))
X(161, "Escala", "<p>Na planta, a varanda em L tem uma faixa de 16 cm × 5 cm e outra de 4 cm × (18,4 − 5) cm = 4 × 13,4 cm. Área na planta: 80 + 53,6 = 133,6 cm². Na escala 1 : 50, as áreas se multiplicam por 50² = 2 500: 334 000 cm² = <strong>33,40 m²</strong>. Alternativa <strong>A</strong>.</p><p>133,60 (D) é a área na planta, em cm², sem aplicar a escala; 66,80 (B) é o dobro da área certa; 534,40 (E) é o quádruplo de 133,60.</p>",
  figs(("q161", "Planta baixa de uma casa retangular (cozinha, banheiros, suíte, sala e dois quartos), com uma varanda cinza em forma de L ao redor: no alto, 16 cm de comprimento por 5 cm de largura; à esquerda, 4 cm de largura e 18,4 cm de altura total. Escala 1 : 50.")),
  ["escala", "área"], enun=p(T(161, 0)) + "[[fig:1]]" + p(T(161, 4)))
X(162, "Funções", "<p>Pelo gráfico, as vendas do setor adulto caem de 18 000 (dias 1 a 10) para 15 000 (dias 11 a 20); mantendo a queda linear de 3 000, serão 12 000 nos últimos dez dias. O setor infantil cai de 8 000 para 7 000 e irá para 6 000. Total do mês: 18 000 + 15 000 + 12 000 + 8 000 + 7 000 + 6 000 = 66 000. Faltarão 77 000 − 66 000 = <strong>11 000</strong>. Alternativa <strong>C</strong>.</p>",
  figs(("q162", "Gráfico de vendas (em real) por dia: o setor adulto vai de 18 000 (dia 0) a 15 000 (dia 20) em linha reta; o setor infantil, tracejado, vai de 8 000 (dia 0) a 7 000 (dia 20); o eixo dos dias vai até 30.")),
  ["função afim", "leitura de gráfico"],
  enun=p(T(162, 0).replace(" 18 000", "")) + "[[fig:1]]" + p(T(162, 5)))
X(163, "Porcentagem", "<p>Com 25% de aumento, cada mestre passa a ganhar 10 000, e os 60 somam 600 000. O total máximo é 100 · 12 240 = 1 224 000. Para os 40 doutores sobram 624 000, ou 15 600 cada: um aumento de 3 600 sobre 12 000, isto é, <strong>30%</strong>. Alternativa <strong>D</strong>.</p>",
  tags=["média ponderada", "porcentagem"])
X(164, "Razão e proporção", "<p>Em 60 dias há 60 · 24 · 60 = 86 400 minutos; com um acionamento a cada 48 minutos, são 1 800 acionamentos. Cada um libera 360 ÷ 1 800 = <strong>0,200 mL</strong>. Alternativa <strong>B</strong>.</p><p>6,000 mL (D) é o gasto por dia, não por acionamento.</p>",
  tags=["conversão de unidades", "divisão"])
X(165, "Razão e proporção", "<p>Dois anos de Z valem um ano terrestre: o ano de Z tem 365 ÷ 2 = 182,5 dias terrestres. Cada dia de Z tem 73 dias terrestres. Então o ano de Z tem 182,5 ÷ 73 = <strong>2,5</strong> dias de Z. Alternativa <strong>A</strong>.</p><p>730 (C) inverte a relação entre os anos.</p>",
  tags=["razão", "unidades de tempo"])
X(166, "Funções", "<p>O último a chegar é o carro cuja curva chega a 100 m por último: a reta preta, que só alcança 100 m em 15 s. Ele anda com velocidade constante e larga na frente dos dois carros que começam devagar e aceleram (as curvas que saem “deitadas” da origem). Esses dois depois cruzam a reta por cima, ou seja, ultrapassam o carro preto. A reta preta, porém, nunca passa por cima de nenhuma curva: esse carro fez <strong>0</strong> ultrapassagens. Alternativa <strong>A</strong>.</p>",
  figs(("q166", "Gráfico da distância (m), de 0 a 100, em função do tempo (s), de 0 a 15, com cinco curvas saindo da origem: duas côncavas (aceleração diminuindo) que chegam a 100 m antes, uma reta, e duas convexas (aceleração crescente), uma delas cinza-clara chegando a 100 m por último.")),
  ["leitura de gráfico", "taxa de variação"], enun=p(T(166, 0)) + "[[fig:1]]" + p(T(166, 3)))
X(167, "Porcentagem", "<p>Preço normal: 1 000 + 10% = 1 100. No cartão, 2% de desconto: 1 100 · 0,98 = 1 078. A cliente calculou 1 000 + 8% = 1 080. O valor da loja foi <strong>R$ 2,00 menor</strong>. Alternativa <strong>A</strong>.</p><p>Porcentagens sucessivas não se somam: +10% e −2% não dão +8%.</p>",
  tags=["porcentagens sucessivas"])
X(168, "Geometria plana", "<p>Partindo de P para cima e seguindo o caminho destacado, a cada cruzamento: vira à direita (D), segue em frente (F), vira à esquerda (E), segue (F), vira à direita (D), vira à direita (D), vira à esquerda (E), vira à esquerda (E), segue (F), segue (F) e vira à direita (D) para chegar a Q: <strong>DFEFDDEEFFD</strong>. Alternativa <strong>C</strong>.</p><p>A diferença para B está no 7º cruzamento (E, não D).</p>",
  figs(("q168", "Malha quadriculada de ruas com um caminho poligonal destacado de P (embaixo, à esquerda, saindo para cima) até Q (no alto, à direita), em degraus com subidas e uma descida.")),
  ["localização", "orientação"])
X(169, "Geometria espacial", "<p>Volume do cilindro = área da base × profundidade. Modelo I: A · P. II: (A/2) · 2P = AP. III: raio pela metade dá área A/4: (A/4) · 2P = AP/2. IV: 2A · P/2 = AP. V: raio dobrado dá área 4A: 4A · P/2 = <strong>2AP</strong>, o maior. Alternativa <strong>E</strong>.</p><p>Confundir dobrar o raio com dobrar a área daria IV (D).</p>",
  tags=["volume do cilindro"],
  enun=p(T(169, 0).replace("área da base é Ab", "área da base é A<sub>b</sub>")) + LISTA(T(169, 1)) + p(T(169, 2)))
X(170, "Razão e proporção", "<p>Rentabilidade = aluguel ÷ valor do imóvel: 2005: 630 ÷ 90 000 = 0,70%; 2007: 960 ÷ 120 000 = <strong>0,80%</strong>; 2009: 1 350 ÷ 270 000 = 0,50%; 2011: 1 800 ÷ 450 000 = 0,40%; 2013: 3 240 ÷ 540 000 = 0,60%. A maior é a de <strong>2007</strong>. Alternativa <strong>B</strong>.</p><p>2013 (E) tem o maior aluguel, mas o imóvel também valia muito mais.</p>",
  figs(("q170", "Dois gráficos de barras de 2005 a 2013. Aluguel mensal (R$): 630, 960, 1 350, 1 800 e 3 240. Valor de mercado do imóvel (milhar de R$): 90, 120, 270, 450 e 540.")),
  ["razão", "leitura de gráfico"], enun=p(T(170, 0)) + "[[fig:1]]" + p(T(170, 3)))
X(171, "Estatística", "<p>Para média 18 em 5 jogos, o total precisa ser 90. Somas dos 4 jogos: I: 12 + 25 + 20 + 20 = 77 (faltam 13); II: 71 (faltam 19); III: 71 (19); IV: 75 (15); V: 75 (15). Quem precisa de menos pontos é o jogador <strong>I</strong>. Alternativa <strong>A</strong>.</p>",
  tags=["média aritmética"],
  enun=p(T(171, 0)) + tabela(["Jogadores", "Jogo 1", "Jogo 2", "Jogo 3", "Jogo 4"], [["I", "12", "25", "20", "20"], ["II", "12", "12", "27", "20"], ["III", "14", "14", "17", "26"], ["IV", "15", "18", "21", "21"], ["V", "22", "15", "23", "15"]]) + p(T(171, 2)))
X(172, "Geometria espacial", "<p>Área a revestir = fundo + 4 paredes = c·l + 2p(c + l). I: 50 + 2·1,8·27 = 147,2 m²; II: 45 + 2·2·14 = 101 m²; III: 90 + 2·1·21 = 132 m²; IV: 60 + 2·1,5·19 = 117 m²; V: 36 + 2·2,5·15 = 111 m². A menor é a do projeto <strong>II</strong>. Alternativa <strong>B</strong>.</p>",
  tags=["área de superfície", "paralelepípedo"], enun=p(T(172, 0), T(172, 1)) + BL(T(172, 2), "O projeto que"))
X(173, "Aritmética", "<p>Candidatos = vagas × candidatos por vaga: 30·6 + 40·6 + 50·7 + 30·8 + 25·4 + 25·5 = 180 + 240 + 350 + 240 + 100 + 125 = <strong>1 235</strong>. Alternativa <strong>D</strong>.</p><p>200 (A) é o total de vagas; 7 200 (E) multiplica o total de vagas pelo total de candidatos por vaga.</p>",
  tags=["multiplicação", "tabela"],
  enun=p(T(173, 0)) + tabela(["Curso", "Número de vagas oferecidas", "Número de candidatos por vaga"], [["Administração", "30", "6"], ["Ciências Contábeis", "40", "6"], ["Engenharia Elétrica", "50", "7"], ["História", "30", "8"], ["Letras", "25", "4"], ["Pedagogia", "25", "5"]]) + p(T(173, 3)))
X(174, "Geometria espacial", "<p>Volume do cilindro: π · 4² · 50 = 800π cm³. Cada esfera (raio 0,5 cm): \\(\\frac{4}{3}\\)π · 0,125 = \\(\\frac{\\pi}{6}\\) cm³. Número de esferas: 800π ÷ (π/6) = <strong>4 800</strong>. Alternativa <strong>D</strong>.</p><p>600 esferas sairiam usando o diâmetro como raio; 2 400 (C) esquece o fator 1/2 do raio em algum passo.</p>",
  tags=["volume da esfera", "volume do cilindro"])
X(175, "Aritmética", "<p>1,35 bilhão = 1,35 × 1 000 000 000 = <strong>1 350 000 000,00</strong>. Alternativa <strong>E</strong>.</p><p>Um bilhão tem nove zeros; multiplicar por 1,35 desloca a vírgula duas casas: 1 350 000 000. Os valores de B, C e D seriam 1,35 milhão, 13,5 milhões e 135 milhões, e A seria apenas 135 mil reais.</p>",
  tags=["notação numérica"])
X(176, "Geometria analítica", "<p>Para minimizar a soma das distâncias até um ponto da Rodovia 003 (o eixo x), reflete-se a cidade A = (20, 40) no eixo: A' = (20, −40). O melhor ponto é onde o segmento A'B, com B = (50, 20), cruza o eixo: a reta sobe 60 em 30 de x, e cruza y = 0 em x = 20 + 40 · 30/60 = 40 km, exatamente a localização <strong>IV</strong>. Alternativa <strong>D</strong>.</p>",
  figs(("q176", "Plano cartesiano com o eixo x sobre a Rodovia 003 (0 a 55 km) e y até 40 km: a Cidade A em (15, 40) e a Cidade B em (50, 20). Segmentos ligam A e B a cinco pontos sugeridos no eixo x: I (cerca de 20), II (30), III (35), IV (cerca de 38) e V (50).")),
  ["reflexão", "distância mínima"], enun=p(T(176, 0)) + "[[fig:1]]" + p(T(176, 3)))
X(177, "Aritmética", "<p>Custo = preço por hora × horas + transporte × dias (8 horas por dia). I: 120 · 8 = 960, sem transporte = 960. II: 180 · 6 = 1 080. III: 170 · 6 + 20 · 1 = 1 040. IV: 110 · 9 + 10 · 2 = 1 010. V: 110 · 10 = 1 100. O menor custo é o do operário <strong>I</strong>. Alternativa <strong>A</strong>.</p><p>IV e V têm o menor preço por hora, mas levam mais tempo.</p>",
  tags=["custo", "tabela"],
  enun=p(T(177, 0), T(177, 1)) + tabela(["Operário", "Preço por hora (real)", "Preço do transporte (real)", "Tempo até conclusão (hora)"], [["I", "120", "0,00", "8"], ["II", "180", "0,00", "6"], ["III", "170", "20,00", "6"], ["IV", "110", "10,00", "9"], ["V", "110", "0,00", "10"]]) + p(T(177, 3)))
X(178, "Geometria espacial", "<p>Dobrar o diâmetro multiplica o volume por 2³ = 8. Cada docinho novo gasta massa de 8 docinhos antigos; 150 docinhos novos equivalem a 1 200 antigos. Como uma porção rende 50, são 1 200 ÷ 50 = <strong>24 porções</strong>. Alternativa <strong>E</strong>.</p><p>6 porções (C) dobram o volume por 2 em vez de 8; 12 (D) usam o fator 4 (área).</p>",
  tags=["volume da esfera", "semelhança"])
X(179, "Sequências", "<p>Se a esperança de 2013 (74,23) for a média das de 2012 (73,95) e 2014 (x): 74,23 = (73,95 + x) ÷ 2, x = 148,46 − 73,95 = <strong>74,51</strong>. Alternativa <strong>B</strong>.</p><p>É o mesmo que continuar a progressão aritmética: aumento de 0,28 por ano.</p>",
  figs(("q179", "Gráfico “Esperança de vida ao nascer”, de 2008 a 2013, em linha crescente: 72,78; 73,09; 73,4; 73,67; 73,95 e 74,23.")),
  ["progressão aritmética", "média"],
  enun=p(T(179, 0)) + "[[fig:1]]" + fonte("Disponível em: http://cod.ibge.gov.br. Acesso em: 6 mar. 2014 (adaptado).") + p(T(179, 3).split("(adaptado). ", 1)[1], T(179, 4)))
X(180, "Geometria espacial", "<p>Visto de cima, o plano do Equador aparece como a circunferência do contorno, e os meridianos (perpendiculares entre si) aparecem como dois diâmetros perpendiculares. Cada trajetória vai do polo (centro) até o Equador por um meridiano e segue um quarto do Equador. As duas trajetórias, em quadrantes opostos, formam dois setores de um quarto de círculo opostos pelo centro: a figura <strong>E</strong>. Alternativa <strong>E</strong>.</p>",
  figs(("q180", "Globo terrestre com os polos N e S, o meridiano 1, o meridiano 2 (perpendiculares) e a Linha do Equador, com duas trajetórias destacadas em traço grosso; abaixo, o plano α paralelo ao Equador."),
       ("q180_a", "Alternativa A: círculo dividido por arcos curvos em formato de cata-vento."),
       ("q180_b", "Alternativa B: três pétalas curvas em torno de um centro, sem o contorno completo."),
       ("q180_c", "Alternativa C: duas pétalas curvas e arcos parciais."),
       ("q180_d", "Alternativa D: círculo inteiro dividido em quatro por dois diâmetros perpendiculares."),
       ("q180_e", "Alternativa E: dois quartos de círculo opostos pelo centro, cada um formado por dois raios perpendiculares e um arco.")),
  ["projeção ortogonal", "esfera"], alts=ALT(2),
  enun=p(T(180, 0).replace("plano α", "plano α")) + "[[fig:1]]" + p(T(180, 5)))

completar(Q, R)
