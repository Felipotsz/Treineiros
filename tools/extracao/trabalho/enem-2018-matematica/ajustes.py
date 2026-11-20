# Enem 2018, 2º dia, caderno azul: Matemática (questões 136 a 180; no site, 1 a 45).
# Texto legível (sem DECOD), mas as Q139–141 vieram como uma página-imagem no rascunho: enunciados digitados a partir da prova.
# Frações, potências e matriz em KaTeX; quadros em tabela HTML. Alternativas-imagem nas Q159 e Q173.
# Anulada pelo Inep: Q163 (questão já usada no vestibular da UFPR).
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, paragrafos_enem

ID = "enem-2018-matematica"
META = {"id": ID, "banca": "Enem", "ano": 2018, "titulo": "Enem 2018: Matemática", "fonte": "Inep", "dataExame": "2018-11-11",
        "duracaoMinutos": 150, "area": "Matemática", "caderno": "azul", "dia": 2}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2018-dia2-azul")
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


K = lambda s: f"\\({s}\\)"
LI = lambda *xs: "<ul>" + "".join(f"<li>{x}</li>" for x in xs) + "</ul>"

X(136, "Matrizes", "<p>O total transferido pelo banco <em>i</em> é a soma da linha <em>i</em> da matriz (o banco <em>i</em> é a origem):</p><ul><li>banco 1: 0 + 2 + 0 + 2 + 2 = 6;</li><li>banco 2: 0 + 0 + 2 + 1 + 0 = 3;</li><li>banco 3: 1 + 2 + 0 + 1 + 1 = 5;</li><li>banco 4: 0 + 2 + 2 + 0 + 0 = 4;</li><li>banco 5: 3 + 0 + 1 + 1 + 0 = 5.</li></ul><p>O maior total é o do <strong>banco 1</strong>. Alternativa <strong>A</strong>.</p><p>Somar as colunas daria o que cada banco <em>recebeu</em>, não o que transferiu.</p>",
  tags=["matriz", "leitura de dados"],
  enun=p("A Transferência Eletrônica Disponível (TED) é uma transação financeira de valores entre diferentes bancos. Um economista decide analisar os valores enviados por meio de TEDs entre cinco bancos (1, 2, 3, 4 e 5) durante um mês. Para isso, ele dispõe esses valores em uma matriz " + K("A = [a_{ij}]") + ", em que " + K("1 \\le i \\le 5") + " e " + K("1 \\le j \\le 5") + ", e o elemento " + K("a_{ij}") + " corresponde ao total proveniente das operações feitas via TED, em milhão de real, transferidos do banco <em>i</em> para o banco <em>j</em> durante o mês. Observe que os elementos " + K("a_{ii} = 0") + ", uma vez que TED é uma transferência entre bancos distintos. Esta é a matriz obtida para essa análise:")
       + "<p>\\[A = \\begin{bmatrix} 0 & 2 & 0 & 2 & 2 \\\\ 0 & 0 & 2 & 1 & 0 \\\\ 1 & 2 & 0 & 1 & 1 \\\\ 0 & 2 & 2 & 0 & 0 \\\\ 3 & 0 & 1 & 1 & 0 \\end{bmatrix}\\]</p>" + p(T(136, 3)))
X(137, "Matemática financeira", "<p>Uma parcela de R$ 820,00 que vence daqui a <em>n</em> meses vale hoje " + K("P = \\dfrac{820}{(1{,}0132)^n}") + ". O desconto é 820 − P, e ele precisa passar de 25% de 820, ou seja, P &lt; 0,75 · 820:</p><p>" + K("(1{,}0132)^n > \\dfrac{4}{3} \\;\\Rightarrow\\; n \\cdot \\ln(1{,}0132) > \\ln\\tfrac{4}{3} \\;\\Rightarrow\\; n > \\dfrac{0{,}2877}{0{,}0131} \\approx 21{,}96") + "</p><p>O menor valor inteiro é n = 22: a parcela antecipada deve vencer 22 meses depois da 30ª, isto é, a <strong>52ª</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["juros compostos", "logaritmo"],
  enun=p(T(137, 0).replace("valor presente P", "valor presente <em>P</em>").replace("taxa i,", "taxa <em>i</em>,").replace("tempo n,", "tempo <em>n</em>,").replace("valor futuro V", "valor futuro <em>V</em>")) + "<p>\\[V = P \\cdot (1 + i)^n\\]</p>" + p(T(137, 2), "Utilize 0,2877 como aproximação para " + K("\\ln\\left(\\tfrac{4}{3}\\right)") + " e 0,0131 como aproximação para ln (1,0132).", "A primeira das parcelas que poderá ser antecipada junto com a 30ª é a"),
  alts={"A": "56ª", "B": "55ª", "C": "52ª", "D": "51ª", "E": "45ª"})
X(138, "Geometria analítica", "<p>Uma circunferência vale 2 pontos por ponto atingido. A circunferência " + K("(x-2)^2 + (y-2)^2 = 8") + " tem centro (2 ; 2) e raio " + K("2\\sqrt{2}") + ": passa pela origem e por A(0 ; 4), B(4 ; 4) e C(4 ; 0), pois a distância de cada um ao centro é " + K("\\sqrt{4+4} = 2\\sqrt{2}") + ". São 3 pontos × 2 = 6 pontos. Alternativa <strong>E</strong>.</p><p>A circunferência " + K("x^2 + (y-2)^2 = 4") + " passa por A e D: 4 pontos. A reta x = 0 passa por A e E, mas reta vale só 1 ponto por ponto: 2. As de y = 0 e " + K("x^2+y^2=16") + " nem passam por A.</p>",
  figs(("q138", "Plano cartesiano com malha tracejada e os pontos A(0 ; 4), B(4 ; 4), C(4 ; 0), D(2 ; 2) e E(0 ; 2).")),
  ["circunferência", "equação da reta"],
  enun=p(T(138, 0).replace("A(0 ; 4), B(4 ; 4), C(4 ; 0), D(2 ; 2) e E(0 ; 2)", "<em>A</em>(0 ; 4), <em>B</em>(4 ; 4), <em>C</em>(4 ; 0), <em>D</em>(2 ; 2) e <em>E</em>(0 ; 2)")) + "[[fig:1]]" + p("Passando pelo ponto <em>A</em>, qual equação forneceria a maior pontuação?"),
  alts=FR("x = 0", "y = 0", "x^2 + y^2 = 16", "x^2 + (y - 2)^2 = 4", "(x - 2)^2 + (y - 2)^2 = 8"))
X(139, "Comprimento de arco", "<p>B está na circunferência de raio 4, na semirreta de 30°; A está na de raio 6, na semirreta de 150°. O ângulo entre as duas semirretas é 120° = " + K("\\tfrac{2\\pi}{3}") + " rad. Como não se pode passar pela origem, o caminho é: descer pela semirreta de B até uma circunferência de raio <em>r</em>, andar o arco e subir pela semirreta de A.</p><p>Comprimento: " + K("(4 - r) + \\tfrac{2\\pi}{3} r + (6 - r) = 10 + r\\left(\\tfrac{2\\pi}{3} - 2\\right)") + ". Com π ≈ 3,1 (ou 3,14), " + K("\\tfrac{2\\pi}{3} > 2") + ", então o caminho fica mais curto com o menor raio possível, r = 1:</p><p>" + K("\\tfrac{2 \\cdot \\pi \\cdot 1}{3} + 3 + 5 = \\tfrac{2 \\cdot \\pi \\cdot 1}{3} + 8") + ". Alternativa <strong>A</strong>.</p><p>As outras opções fazem o arco em circunferências maiores (raios 2, 3, 4 e 5), mais longas.</p>",
  figs(("q139", "Malha polar: circunferências tracejadas de raios 1 a 6 centradas na origem e 12 semirretas que partem da origem, separadas por 30°. O ponto A está na circunferência de raio 6, na semirreta de 150°; o ponto B está na de raio 4, na semirreta de 30°.")),
  ["arco de circunferência", "menor caminho"],
  enun=p("Sobre um sistema cartesiano considera-se uma malha formada por circunferências de raios com medidas dadas por números naturais e por 12 semirretas com extremidades na origem, separadas por ângulos de " + K("\\tfrac{\\pi}{6}") + " rad, conforme a figura.") + "[[fig:1]]" + p("Suponha que os objetos se desloquem apenas pelas semirretas e pelas circunferências dessa malha, não podendo passar pela origem (0 ; 0).", "Considere o valor de π com aproximação de, pelo menos, uma casa decimal.", "Para realizar o percurso mais curto possível ao longo da malha, do ponto <em>B</em> até o ponto <em>A</em>, um objeto deve percorrer uma distância igual a"),
  alts=FR("\\dfrac{2 \\cdot \\pi \\cdot 1}{3} + 8", "\\dfrac{2 \\cdot \\pi \\cdot 2}{3} + 6", "\\dfrac{2 \\cdot \\pi \\cdot 3}{3} + 4", "\\dfrac{2 \\cdot \\pi \\cdot 4}{3} + 2", "\\dfrac{2 \\cdot \\pi \\cdot 5}{3} + 2"))
X(140, "Geometria espacial", "<p>Cada pote ocupa um quadrado de 4 cm × 4 cm na base e 6 cm de altura. Em cada caixa, divide-se cada dimensão pela do pote e se fica com a parte inteira:</p><ul><li>I: 2 × 2 × 6 = 24;</li><li>II: 2 × 5 × 2 = 20;</li><li>III: 4 × 1 × 5 = 20;</li><li>IV: 5 × 3 × 2 = 30;</li><li>V: 6 × 2 × 2 = 24.</li></ul><p>O modelo <strong>IV</strong> guarda mais potes. Alternativa <strong>D</strong>.</p><p>Dividir o volume da caixa pelo volume do pote não funciona: sobram espaços onde um pote inteiro não cabe.</p>",
  tags=["paralelepípedo", "cilindro"],
  enun=p("Um artesão possui potes cilíndricos de tinta cujas medidas externas são 4 cm de diâmetro e 6 cm de altura. Ele pretende adquirir caixas organizadoras para armazenar seus potes de tinta, empilhados verticalmente com tampas voltadas para cima, de forma que as caixas possam ser fechadas.", "No mercado, existem cinco opções de caixas organizadoras, com tampa, em formato de paralelepípedo reto retângulo, vendidas pelo mesmo preço, possuindo as seguintes dimensões internas:")
       + tabela(["Modelo", "Comprimento (cm)", "Largura (cm)", "Altura (cm)"], [["I", "8", "8", "40"], ["II", "8", "20", "14"], ["III", "18", "5", "35"], ["IV", "20", "12", "12"], ["V", "24", "8", "14"]])
       + p("Qual desses modelos o artesão deve adquirir para conseguir armazenar o maior número de potes por caixa?"),
  alts={"A": "I", "B": "II", "C": "III", "D": "IV", "E": "V"})
X(141, "Progressão aritmética", "<p>As distâncias dos postes formam uma PA: 80, 100, 120, …, 1 380, de razão 20. O número de postes é " + K("n = \\dfrac{1380 - 80}{20} + 1 = 66") + ".</p><p>Gasto máximo: 66 × R$ 8 000,00 = <strong>R$ 528 000,00</strong>. Alternativa <strong>C</strong>.</p><p>Esquecer o “+ 1” dá 65 postes e R$ 520 000,00 (B).</p>",
  tags=["PA", "contagem"],
  enun=p("A prefeitura de um pequeno município do interior decide colocar postes para iluminação ao longo de uma estrada retilínea, que inicia em uma praça central e termina numa fazenda na zona rural. Como a praça já possui iluminação, o primeiro poste será colocado a 80 metros da praça, o segundo, a 100 metros, o terceiro, a 120 metros, e assim sucessivamente, mantendo-se sempre uma distância de vinte metros entre os postes, até que o último poste seja colocado a uma distância de 1 380 metros da praça.", "Se a prefeitura pode pagar, no máximo, R$ 8 000,00 por poste colocado, o maior valor que poderá gastar com a colocação desses postes é"),
  alts={"A": "R$ 512 000,00.", "B": "R$ 520 000,00.", "C": "R$ 528 000,00.", "D": "R$ 552 000,00.", "E": "R$ 584 000,00."})
X(142, "Proporcionalidade", "<p>Pela fórmula " + K("F = \\tfrac{km}{r^2}") + ", F cresce com a massa e diminui com o raio.</p><ul><li>A e B têm o mesmo raio, e B tem massa maior: F<sub>A</sub> &lt; F<sub>B</sub>.</li><li>A e C têm a mesma massa, e C tem raio maior: F<sub>C</sub> &lt; F<sub>A</sub>.</li></ul><p>Logo, F<sub>C</sub> &lt; F<sub>A</sub> &lt; F<sub>B</sub>. Alternativa <strong>E</strong>.</p>",
  figs(("q142", "Gráfico com o raio (r) no eixo vertical e a massa (m) no horizontal. A e B estão na mesma altura (mesmo raio), com B mais à direita (massa maior). C está acima de A, na mesma vertical (mesma massa, raio maior).")),
  ["grandezas inversamente proporcionais", "gravitação"],
  enun=p(T(142, 0).replace("força gravitacional F", "força gravitacional <em>F</em>").replace("massa m do", "massa <em>m</em> do").replace("raio r da", "raio <em>r</em> da")) + "<p>\\[F = \\frac{km}{r^2}\\]</p>" + p(T(142, 2)) + "[[fig:1]]" + p("Com base nas posições relativas dos pontos no gráfico, deseja-se comparar as intensidades <em>F</em><sub>A</sub>, <em>F</em><sub>B</sub> e <em>F</em><sub>C</sub> da força gravitacional que a Terra exerce sobre os satélites <em>A</em>, <em>B</em> e <em>C</em>, respectivamente.", "As intensidades <em>F</em><sub>A</sub>, <em>F</em><sub>B</sub> e <em>F</em><sub>C</sub> expressas no gráfico satisfazem a relação"),
  alts=FR("F_C = F_A < F_B", "F_A = F_B < F_C", "F_A < F_B < F_C", "F_A < F_C < F_B", "F_C < F_A < F_B"))
X(143, "Porcentagem", "<p>Os 40 g de prata 950 devem ter 0,95 × 40 = 38 g de prata pura e 2 g de cobre. Os 10 g de prata 925 já trazem 9,25 g de prata e 0,75 g de cobre.</p><p>Faltam 38 − 9,25 = 28,75 g de prata e 2 − 0,75 = 1,25 g de cobre. Alternativa <strong>B</strong>.</p><p>Conferindo: 10 + 28,75 + 1,25 = 40 g.</p>",
  tags=["mistura", "proporção"])
X(144, "Razão", "<p>O tempo de espera em cada máquina é o tempo por passageiro vezes o número de pessoas na fila:</p><ul><li>1: 35 × 5 = 175 s;</li><li>2: 25 × 6 = 150 s;</li><li>3: 22 × 7 = 154 s;</li><li>4: 40 × 4 = 160 s;</li><li>5: 20 × 8 = 160 s.</li></ul><p>A menor espera é na <strong>máquina 2</strong>. Alternativa <strong>B</strong>.</p>",
  figs(("q144", "Painel com cinco máquinas: máquina 1, 35 segundos e 5 pessoas; máquina 2, 25 segundos e 6 pessoas; máquina 3, 22 segundos e 7 pessoas; máquina 4, 40 segundos e 4 pessoas; máquina 5, 20 segundos e 8 pessoas.")),
  ["multiplicação", "otimização"], enun=p(T(144, 0)) + "[[fig:1]]" + p(T(144, 7)))
X(145, "Estatística", "<p>Média ponderada: soma dos acidentes ÷ número de funcionários.</p><p>0 × 50 + 1 × 17 + 2 × 15 + 3 × 10 + 4 × 6 + 5 × 2 = 0 + 17 + 30 + 30 + 24 + 10 = 111.</p><p>111 ÷ 100 = <strong>1,11</strong>. Alternativa <strong>D</strong>.</p>",
  tags=["média ponderada"],
  enun=p(T(145, 0), T(145, 1)) + tabela(["Número de acidentes sofridos", "Número de trabalhadores"], [["0", "50"], ["1", "17"], ["2", "15"], ["3", "10"], ["4", "6"], ["5", "2"]]) + p("A média do número de acidentes por funcionário na amostra que a CIPA apresentará à diretoria da empresa é"))
X(146, "Grandezas e medidas", "<p>Distância = velocidade × tempo:</p><ul><li>Alpha: 6,0 km/h × 1,5 h = 9,0 km;</li><li>Beta: 5,0 km/h × 1,5 h = 7,5 km;</li><li>Gama: 6,5 km/h × 1 h = 6,5 km.</li></ul><p>Logo, d<sub>Gama</sub> &lt; d<sub>Beta</sub> &lt; d<sub>Alpha</sub>. Alternativa <strong>A</strong>.</p>",
  tags=["velocidade média"],
  enun=p(T(146, 0)) + LISTA(T(146, 1).replace("<br>", "")) + p("Com base nesses dados, foram comparadas as distâncias " + K("d_{Beta}") + ", " + K("d_{Alpha}") + " e " + K("d_{Gama}") + " percorridas pelas três equipes.", "A ordem das distâncias percorridas pelas equipes Alpha, Beta e Gama é"),
  alts=FR("d_{Gama} < d_{Beta} < d_{Alpha}", "d_{Alpha} = d_{Beta} < d_{Gama}", "d_{Gama} < d_{Beta} = d_{Alpha}", "d_{Beta} < d_{Alpha} < d_{Gama}", "d_{Gama} < d_{Alpha} < d_{Beta}"))
X(147, "Porcentagem", "<p>Reduções sucessivas se multiplicam: 280 × 0,75 = 210 mg/dL no primeiro exame; 210 × 0,80 = 168 mg/dL no segundo.</p><p>168 está entre 160 e 189: taxa <strong>alta</strong>. Alternativa <strong>D</strong>.</p><p>Somar as reduções (45%) daria 154 mg/dL, “limite” (C), o que está errado.</p>",
  tags=["descontos sucessivos"],
  enun=p(T(147, 0), T(147, 1)) + tabela(["Taxa de LDL (mg/dL)", ""], [["Ótima", "Menor do que 100"], ["Próxima de ótima", "De 100 a 129"], ["Limite", "De 130 a 159"], ["Alta", "De 160 a 189"], ["Muito alta", "190 ou mais"]]) + fonte(T(147, 3)) + p(T(147, 4), T(147, 5)))
X(148, "Função afim", "<p>Rádio: cada R$ 120,00 alcança 1 500 pessoas, então X reais alcançam " + K("\\tfrac{1500}{120}X = \\tfrac{25X}{2} = \\tfrac{50X}{4}") + ".</p><p>Panfletos: cada R$ 180,00 alcança 1 000 pessoas, então Y reais alcançam " + K("\\tfrac{1000}{180}Y = \\tfrac{50Y}{9}") + ".</p><p>Total: " + K("\\tfrac{50X}{4} + \\tfrac{50Y}{9}") + ". Alternativa <strong>A</strong>.</p>",
  tags=["razão", "expressão algébrica"],
  enun=p(T(148, 0), T(148, 1).replace("Considere X e Y", "Considere <em>X</em> e <em>Y</em>"), T(148, 2)),
  alts=FR("\\dfrac{50X}{4} + \\dfrac{50Y}{9}", "\\dfrac{50X}{9} + \\dfrac{50Y}{4}", "\\dfrac{4X}{50} + \\dfrac{4Y}{50}", "\\dfrac{50}{4X} + \\dfrac{50}{9Y}", "\\dfrac{50}{9X} + \\dfrac{50Y}{4Y}"))
X(149, "Porcentagem", "<p>A rampa projetada desce 2 m em 8 m de base: 200 cm ÷ 8 m = 25 cm por metro, inclinação de 25%, acima do permitido.</p><p>Com 20%, a altura máxima em 8 m é 8 × 20 = 160 cm. A garagem precisa ficar 200 − 160 = 40 cm mais alta: deve ser <strong>elevada em 40 cm</strong>. Alternativa <strong>A</strong>.</p>",
  figs(("q149a", "Exemplo: triângulo retângulo com 1 m de base e 20 cm de altura, com a indicação “inclinação = 20%”."),
       ("q149b", "Corte da rampa: o nível da rua, com o portão, fica 2 m acima do nível da base da garagem; a rampa desce em linha reta ao longo de 8 m de base até a garagem.")),
  ["inclinação", "proporção"],
  enun=p(T(149, 0).replace("mede-se x centímetros", "mede-se <em>x</em> centímetros").replace("inclinação de x%", "inclinação de <em>x</em>%")) + "[[fig:1]]" + p("A figura apresenta um projeto de uma rampa de acesso a uma garagem residencial cuja base, situada 2 metros abaixo do nível da rua, tem 8 metros de comprimento.") + "[[fig:2]]" + p("Depois de projetada a rampa, o responsável pela obra foi informado de que as normas técnicas do município onde ela está localizada exigem que a inclinação máxima de uma rampa de acesso a uma garagem residencial seja de 20%.", "Se a rampa projetada tiver inclinação superior a 20%, o nível da garagem deverá ser alterado para diminuir o percentual de inclinação, mantendo o comprimento da base da rampa.", "Para atender às normas técnicas do município, o nível da garagem deverá ser"),
  alts={**D[149]["alternativas"], "E": "rebaixado em 50 cm."})
X(150, "Probabilidade", "<p>Probabilidade de tirar duas pretas em cada opção:</p><ul><li>Opção 1 (A: 2 pretas em 6): " + K("\\tfrac{2}{6}\\cdot\\tfrac{1}{5} = \\tfrac{1}{15} \\approx 0{,}067") + ";</li><li>Opção 2 (B: 3 em 10): " + K("\\tfrac{3}{10}\\cdot\\tfrac{2}{9} = \\tfrac{1}{15}") + ";</li><li>Opção 3 (C → A): com metade de chance, A fica com 3 pretas em 7 ou com 2 em 7: " + K("\\tfrac{1}{2}\\left(\\tfrac{3}{7}\\cdot\\tfrac{2}{6}\\right) + \\tfrac{1}{2}\\left(\\tfrac{2}{7}\\cdot\\tfrac{1}{6}\\right) = \\tfrac{2}{21} \\approx 0{,}095") + ";</li><li>Opção 4 (D → C): C fica com 3 pretas em 5 ou 2 em 5: " + K("\\tfrac{1}{2}\\cdot\\tfrac{3}{10} + \\tfrac{1}{2}\\cdot\\tfrac{1}{10} = \\tfrac{1}{5} = 0{,}2") + ";</li><li>Opção 5 (C → D): D fica com 4 pretas em 7 ou 3 em 7: " + K("\\tfrac{1}{2}\\cdot\\tfrac{2}{7} + \\tfrac{1}{2}\\cdot\\tfrac{1}{7} = \\tfrac{3}{14} \\approx 0{,}214") + ".</li></ul><p>A maior é a da <strong>opção 5</strong>. Alternativa <strong>E</strong>.</p>",
  tags=["probabilidade condicional", "sem reposição"],
  enun=p(T(150, 0), T(150, 1)) + LISTA(T(150, 2).split(" A pessoa deve")[0]) + p("A pessoa deve escolher uma entre as cinco opções apresentadas:") + LISTA(T(150, 2).split("apresentadas:<br>")[1].split(" Com o objetivo")[0]) + p("Com o objetivo" + T(150, 2).split(" Com o objetivo")[1]))
X(151, "Semelhança", "<p>Mudar o tamanho da fonte muda as medidas lineares na mesma proporção, e as áreas mudam com o quadrado dessa proporção. Para a área pintada ficar " + K("\\tfrac{1}{16}") + " da inicial, as medidas lineares devem ficar " + K("\\sqrt{\\tfrac{1}{16}} = \\tfrac{1}{4}") + " das originais.</p><p>Novo tamanho: 192 ÷ 4 = <strong>48</strong>. Alternativa <strong>B</strong>.</p><p>Dividir 192 por 16 (E) seria tratar a área como se variasse linearmente.</p>",
  figs(("q151", "A palavra “ecofont” escrita em tamanhos crescentes e, embaixo, as letras E, C e O formadas por quadrados de lado x, cada um com um furo circular.")),
  ["razão de semelhança", "área"],
  enun=p(T(151, 0).replace("possui design", "possui <em>design</em>")) + "[[fig:1]]" + fonte(T(151, 2)) + p("Suponha que a palavra ECO esteja escrita nessa fonte, com tamanho 192, e que seja composta por letras formadas por quadrados de lados <em>x</em> com furos circulares de raio " + K("r = \\tfrac{x}{3}") + ". Para que a área a ser pintada seja reduzida a " + K("\\tfrac{1}{16}") + " da área inicial, pretende-se reduzir o tamanho da fonte. Sabe-se que, ao alterar o tamanho da fonte, o tamanho da letra é alterado na mesma proporção.", "Nessas condições, o tamanho adequado da fonte será"))
X(152, "Inequações", "<p>Os pontos estão no primeiro quadrante, com x de 0 a 10, e em cada coluna vão de y = 0 até y = x (abaixo da reta y = x). Assim, 0 ≤ y ≤ x ≤ 10. Alternativa <strong>B</strong>.</p><p>A condição 0 ≤ x ≤ y ≤ 10 (A) daria o triângulo acima da reta y = x, encostado no eixo y.</p>",
  figs(("q152", "Plano cartesiano com pontos de coordenadas inteiras formando um triângulo: vértices em (0 ; 0), (10 ; 0) e (10 ; 10), preenchido por pontos abaixo da reta y = x.")),
  ["plano cartesiano", "desigualdades"],
  enun=p(T(152, 0).replace("área de design", "área de <em>design</em>")) + "[[fig:1]]" + p("Para construir tal imagem utilizando uma ferramenta gráfica, será necessário escrever algebricamente o conjunto que representa os pontos desse gráfico.", "Esse conjunto é dado pelos pares ordenados (<em>x</em> ; <em>y</em>) ∈ ℕ × ℕ, tais que"))
X(153, "Geometria plana", "<p>A trena AB é tangente ao chafariz, então o raio do chafariz (r) que vai ao ponto de tangência é perpendicular a AB e o divide ao meio (8 m para cada lado). O triângulo formado pelo centro, o ponto de tangência e A tem hipotenusa R (raio da praça):</p><p>" + K("R^2 = r^2 + 8^2 \\Rightarrow R^2 - r^2 = 64") + ".</p><p>Área do passeio: " + K("\\pi R^2 - \\pi r^2 = \\pi (R^2 - r^2) = 64\\pi") + " m². Alternativa <strong>D</strong>.</p>",
  figs(("q153a", "Praça circular vista de cima, com o chafariz circular no centro e o passeio entre os dois círculos."),
       ("q153b", "A mesma praça com uma corda AB de 16 m do círculo externo, tangente ao círculo do chafariz.")),
  ["coroa circular", "teorema de Pitágoras"],
  enun=p(T(153, 0)) + "[[fig:1]]" + p(T(153, 2).replace("pontos A e B", "pontos <em>A</em> e <em>B</em>").replace("segmento de reta AB", "segmento de reta <em>AB</em>")) + "[[fig:2]]" + p(T(153, 4)),
  alts=FR("4\\pi", "8\\pi", "48\\pi", "64\\pi", "192\\pi"))
X(154, "Probabilidade", "<p>Depois da primeira peça, sobram n² − 1 casas vazias. A zona de combate tem n − 1 casas na linha e n − 1 na coluna: 2(n − 1).</p><p>" + K("P = \\dfrac{2(n-1)}{n^2 - 1} = \\dfrac{2(n-1)}{(n-1)(n+1)} = \\dfrac{2}{n+1}") + "</p><p>Para " + K("\\tfrac{2}{n+1} < \\tfrac{1}{5}") + ", é preciso n + 1 &gt; 10, ou seja, n &gt; 9. A dimensão mínima é <strong>10 × 10</strong>. Alternativa <strong>D</strong>.</p><p>Com 9 × 9, a probabilidade é exatamente 1/5, e não inferior.</p>",
  figs(("q154", "Tabuleiro 8 × 8 com uma peça numa das casas; as casas da mesma linha e da mesma coluna estão destacadas, formando a zona de combate.")),
  ["probabilidade", "inequação"],
  enun=p(T(154, 0).replace("Um designer", "Um <em>designer</em>").replace("dimensão n × n, com n ≥ 2", "dimensão <em>n</em> × <em>n</em>, com <em>n</em> ≥ 2")) + "[[fig:1]]" + p("O tabuleiro deve ser dimensionado de forma que a probabilidade de se posicionar a segunda peça aleatoriamente, seguindo a regra do jogo, e esta ficar sobre a zona de combate da primeira, seja inferior a " + K("\\tfrac{1}{5}") + ".", "A dimensão mínima que o <em>designer</em> deve adotar para esse tabuleiro é"),
  alts={**D[154]["alternativas"], "E": "11 × 11."})
X(155, "Geometria plana", "<p>Os dois remos têm o mesmo tamanho: AB = AC, e o triângulo é isósceles. O ângulo em A mede 170°, maior que 90°: o triângulo é obtusângulo. É um triângulo <strong>obtusângulo isósceles</strong>. Alternativa <strong>E</strong>.</p>",
  figs(("q155", "Foto de um remador num barco estreito, com os dois remos abertos: as mãos se encontram no ponto A, e as pontas dos remos estão nos pontos B e C, quase alinhados com A.")),
  ["classificação de triângulos"],
  enun=p(T(155, 0), T(155, 1)) + "[[fig:1]]" + fonte(T(155, 3)) + p(T(155, 4).replace("ponto A e", "ponto <em>A</em> e").replace("pontos B e C", "pontos <em>B</em> e <em>C</em>").replace("triângulo ABC cujo ângulo BÂC", "triângulo <em>ABC</em> cujo ângulo <em>BÂC</em>").replace("pontos A, B e C", "pontos <em>A</em>, <em>B</em> e <em>C</em>")))
X(156, "Estatística", "<p>São 21 dados; a mediana (6 h 22 min) é o 11º. Então no máximo 10 horários são anteriores a 6 h 22 min, e entre eles estão as ocorrências de 6 h 21 min, a moda.</p><p>Os horários antes de 6 h 21 min só podem ser 6 h 15, 16, 17, 18, 19 ou 20 (seis valores), e cada um precisa aparecer menos vezes que 6 h 21 min. Se 6 h 21 min aparece k vezes, cabem no máximo 10 − k dias antes:</p><ul><li>k = 2: cada horário anterior só 1 vez, no máximo 6 dias;</li><li>k = 3: até 7 dias (os seis horários podem se repetir até 2 vezes);</li><li>k = 4: 6 dias.</li></ul><p>O máximo é 7 dias: " + K("\\tfrac{7}{21}") + ". Alternativa <strong>D</strong>.</p>",
  tags=["moda", "mediana", "probabilidade"], alts=FR("\\dfrac{4}{21}", "\\dfrac{5}{21}", "\\dfrac{6}{21}", "\\dfrac{7}{21}", "\\dfrac{8}{21}"))
X(157, "Escala", "<p>Na escala 1 : 58 000 000, 1 cm no mapa vale 58 000 000 cm = 580 km.</p><p>7,6 × 580 = <strong>4 408 km</strong>. Alternativa <strong>A</strong>.</p><p>Esquecer de converter centímetros em quilômetros leva às opções com zeros a mais (C e E).</p>",
  figs(("q157", "Mapa do tesouro desenhado num pergaminho, com uma rosa dos ventos e um segmento de reta ligando um navio à marca do tesouro.")),
  ["escala", "conversão de unidades"], enun=p(T(157, 0), T(157, 1)) + "[[fig:1]]" + fonte(T(157, 3)) + p(T(157, 4)))
X(158, "Razão e proporção", "<p>Seja p a produtividade da área de 120 ha; a de 40 ha tem 2,5p. Produção atual: 120p + 40 · 2,5p = 220p.</p><p>Aumento de 15%: 0,15 · 220p = 33p. A terra nova tem produtividade p, então precisa de 33p ÷ p = <strong>33 hectares</strong>. Alternativa <strong>B</strong>.</p>",
  tags=["produtividade", "porcentagem"])
X(159, "Geometria espacial", "<p>As duas camadas de baixo estão completas. Os cubinhos que faltam ficam nas duas camadas de cima, junto à frente e ao lado direito da montagem: uma fileira na frente e outra que segue para trás pela direita, na camada mais alta, com um cubinho descendo para a terceira camada no canto. A peça com esse formato, e com o número certo de cubinhos em cada fileira, é a primeira. Alternativa <strong>A</strong>.</p><p>Nas outras, a fileira lateral é curta ou longa demais, ou o cubinho que desce está em outro lugar.</p>",
  figs(("q159", "Quatro camadas de cubinhos que, empilhadas, formam uma construção quase cúbica 4 × 4 × 4: as duas de baixo são completas (4 × 4), a terceira tem um cubinho a menos e a de cima tem menos cubinhos, faltando a frente e a lateral direita."),
       ("q159a", "Alternativa A: fileira de quatro cubinhos na frente, com uma fileira de três para trás à direita e um cubinho embaixo do quarto cubinho da frente."),
       ("q159b", "Alternativa B: parecida com a A, mas com a fileira de trás mais longa."),
       ("q159c", "Alternativa C: parecida com a A, com outra disposição da fileira de trás e do cubinho de baixo."),
       ("q159d", "Alternativa D: duas fileiras de quatro cubinhos lado a lado e dois cubinhos embaixo à direita."),
       ("q159e", "Alternativa E: fileira de quatro cubinhos na frente, com dois cubinhos embaixo no meio e uma fileira para trás à direita.")),
  ["visão espacial", "cubos"],
  enun=p(T(159, 0).replace("Minecraft é", "<em>Minecraft</em> é"), T(159, 1)) + "[[fig:1]]" + p(T(159, 9)), alts=ALT(2))
X(160, "Estatística", "<p>No gráfico, 2014 tem 1 ícone, 2015 tem 2 e 2016 tem 5. A diferença de 2016 para 2015 é de 3 ícones, que valem 360 carros: cada ícone vale 120.</p><p>Total: (1 + 2 + 5) × 120 = 960 carros em 3 anos. Média: 960 ÷ 3 = <strong>320</strong>. Alternativa <strong>D</strong>.</p>",
  figs(("q160", "Pictograma de carros elétricos vendidos pela marca A: 2014 com 1 ícone, 2015 com 2 ícones e 2016 com 5 ícones.")),
  ["pictograma", "média"], enun=p(T(160, 0), T(160, 1)) + "[[fig:1]]" + fonte(T(160, 3)) + p(T(160, 4)))
X(161, "Geometria analítica", "<p>Os pontos em que a distância a A é o dobro da distância a B formam uma circunferência (de Apolônio). Ela corta a reta AB em dois pontos:</p><ul><li>entre A e B: d + 2d = 30, d = 10 m de B;</li><li>além de B: 2d − d = 30, d = 30 m de B.</li></ul><p>Esses dois pontos são as pontas de um diâmetro: 10 + 30 = 40 m. A maior distância entre dois bombeiros é o diâmetro, <strong>40 m</strong>. Alternativa <strong>B</strong>.</p>",
  tags=["lugar geométrico", "circunferência"])
X(162, "Progressão geométrica", "<p>Na 1ª fase, 128 tenistas fazem 64 partidas; depois, 32, 16, 8, 4, 2 e 1 (a final). Total: 64 + 32 + 16 + 8 + 4 + 2 + 1 = 127 partidas. Alternativa <strong>E</strong>.</p><p>Outro jeito: cada partida elimina um tenista, e é preciso eliminar 127 para sobrar o campeão.</p>",
  tags=["PG", "contagem"], enun=p(T(162, 0).replace("1a fase", "1ª fase").replace("2n competidores", "2<em>n</em> competidores").replace("2a fase restarão n", "2ª fase restarão <em>n</em>"), T(162, 1)))
X(163, "Frações", "<p>A pena mínima fica menor com a maior redução: 5 anos menos " + K("\\tfrac{2}{3}") + " = " + K("\\tfrac{1}{3}") + " de 60 meses = 20 meses = 1 ano e 8 meses. A máxima fica maior com a menor redução: 15 anos menos " + K("\\tfrac{1}{6}") + " = " + K("\\tfrac{5}{6}") + " de 180 meses = 150 meses = 12 anos e 6 meses. A pena varia de 1 ano e 8 meses a 12 anos e 6 meses.</p><p>Alternativa <strong>A</strong>, se a questão não tivesse sido anulada.</p><p>O Inep anulou a questão porque ela já tinha sido usada no vestibular da UFPR para ingresso em 2014, o que fere a regra de ineditismo do Enem.</p>",
  tags=["frações", "anulada"],
  anulacao={"fonte": "oficial", "motivo": "O Inep anulou a questão porque ela já tinha sido usada no vestibular da UFPR (ingresso em 2014), o que fere o sigilo e o ineditismo exigidos no Enem."})
X(164, "Números inteiros", "<p>Seja s o andar onde a criança entrou: s + 7 − 10 − 13 + 9 − 4 = 5, então s − 11 = 5 e s = 16.</p><p>Os andares visitados foram 16, 23, 13, 0 (térreo), 9, 5. O mais alto foi o 23º; como o elevador parou uma vez no último andar, ele é o <strong>23º</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["operações com inteiros"], enun=p(T(164, 0).replace("térreo (T )", "térreo (<em>T</em>)")),
  alts={"A": "16º", "B": "22º", "C": "23º", "D": "25º", "E": "32º"})
X(165, "Análise combinatória", "<p>Escolhem-se 2 dos 4 compactos (" + K("C_4^2") + ") e 2 das 6 caminhonetes (" + K("C_6^2") + "). Depois, decide-se qual compacto vai para a entrada (2 maneiras) e qual caminhonete vai para a entrada (2 maneiras): " + K("C_4^2 \\times C_6^2 \\times 2 \\times 2") + ". Alternativa <strong>C</strong>.</p><p>Os estandes são diferentes (entrada e centro), por isso não basta escolher os carros (E).</p>",
  tags=["combinação", "princípio multiplicativo"], enun=p(T(165, 0).replace("inovações em design", "inovações em <em>design</em>")) + fonte(T(165, 1)) + p(T(165, 2), T(165, 3)),
  alts=FR("A_{10}^{4}", "C_{10}^{4}", "C_4^2 \\times C_6^2 \\times 2 \\times 2", "A_4^2 \\times A_6^2 \\times 2 \\times 2", "C_4^2 \\times C_6^2"))
X(166, "Estatística", "<p>Média ponderada: 0,2 · 46 + 0,1 · 60 + 0,3 · 50 + 0,4 · x ≥ 60.</p><p>9,2 + 6 + 15 + 0,4x ≥ 60 → 0,4x ≥ 29,8 → x ≥ <strong>74,5</strong>. Alternativa <strong>C</strong>.</p><p>29,8 (A) é o que falta na soma ponderada, antes de dividir pelo peso 0,4.</p>",
  tags=["média ponderada"])
X(167, "Probabilidade", "<p>Das 20 perguntas, 25% são fáceis: 5. Acrescentando x fáceis:</p><p>" + K("\\dfrac{5 + x}{20 + x} = \\dfrac{3}{4} \\Rightarrow 20 + 4x = 60 + 3x \\Rightarrow x = 40") + ". Alternativa <strong>D</strong>.</p><p>Conferindo: 45 fáceis em 60 perguntas = 75%.</p>",
  tags=["probabilidade", "equação"])
X(168, "Função afim", "<p>Entre 2013 (67%) e 2015 (59%), a variação é linear: −8 pontos em 2 anos, −4 por ano. Em 2014: 67 − 4 = <strong>63,0%</strong>. Alternativa <strong>B</strong>.</p><p>A média entre 2013 e 2015 dá o mesmo resultado: (67 + 59) ÷ 2 = 63. O dado de 2017 não entra nessa conta.</p>",
  figs(("q168", "Gráfico de linha da cobertura vacinal: 67% em 2013, 59% em 2015 e 61% em 2017, ligados por segmentos de reta.")),
  ["interpolação linear"], enun=p(T(168, 0)) + "[[fig:1]]" + fonte("Disponível em: http://pni.datasus.gov.br. Acesso em: 5 nov. 2017.") + p(T(168, 4)))
X(169, "Escala", "<p>Guindaste: 15 m = 1 500 cm. Para o desenho medir entre 0,5 e 1 cm: " + K("0{,}5 < \\tfrac{1500}{X} < 1") + ", logo 1 500 &lt; X &lt; 3 000.</p><p>Esteira: 90 m = 9 000 cm. " + K("\\tfrac{9000}{X} > 4") + " → X &lt; 2 250.</p><p>As duas condições juntas: 1 500 &lt; X &lt; 2 250. Alternativa <strong>C</strong>.</p>",
  tags=["escala", "inequação"], enun=p(T(169, 0).replace("escala 1 : X", "escala 1 : <em>X</em>").replace("para X são", "para <em>X</em> são")))
X(170, "Trigonometria", "<p>Pelo gráfico, a altura oscila entre 8 m (88 − 80) e 168 m, com centro em 88 m: amplitude 80. Em t = 0 a altura é 88 (A está na altura do centro), e ela sobe primeiro, chegando a 168 em t = π/2. É o comportamento do seno: f(t) = 80 sen(t) + 88. Alternativa <strong>A</strong>.</p><p>Com cosseno (B), a altura começaria no máximo, 168.</p>",
  figs(("q170a", "Esboço da roda-gigante: um círculo de centro O com raios, apoiado no solo, e o ponto A na extremidade direita, na altura do centro. Uma seta indica rotação no sentido anti-horário."),
       ("q170b", "Gráfico de f (metro) em função de t (radiano), de 0 a 4π: começa em 88, sobe até 168 em π/2, desce e volta a 88 em 2π, completando duas oscilações.")),
  ["função seno", "periodicidade"],
  enun=p(T(170, 0).replace("a High Roller", "a <em>High Roller</em>").replace("o ponto A", "o ponto <em>A</em>")) + "[[fig:1]]" + fonte(T(170, 3)) + p("A partir da posição indicada, em que o segmento <em>OA</em> se encontra paralelo ao plano do solo, rotaciona-se a <em>High Roller</em> no sentido anti-horário, em torno do ponto <em>O</em>. Sejam <em>t</em> o ângulo determinado pelo segmento <em>OA</em> em relação à sua posição inicial, e <em>f</em> a função que descreve a altura do ponto <em>A</em>, em relação ao solo, em função de <em>t</em>.", "Após duas voltas completas, <em>f</em> tem o seguinte gráfico:") + "[[fig:2]]" + p("A expressão da função altura é dada por"),
  alts=FR("f(t) = 80\\,\\text{sen}(t) + 88", "f(t) = 80\\cos(t) + 88", "f(t) = 88\\cos(t) + 168", "f(t) = 168\\,\\text{sen}(t) + 88\\cos(t)", "f(t) = 88\\,\\text{sen}(t) + 168\\cos(t)"))
X(171, "Ângulos", "<p>Medindo os rumos em graus no sentido horário a partir do Norte: Oeste = 270°.</p><ul><li>1ª mudança, 135° anti-horário: 270° − 135° = 135° (Sudeste);</li><li>2ª, 60° horário: 135° + 60° = 195°;</li><li>3ª, 45° anti-horário: 195° − 45° = 150°.</li></ul><p>Noroeste é 315°. De 150° até 315° são 165° no sentido horário (ou 195° no anti-horário). A menor mudança é de <strong>165° no sentido horário</strong>. Alternativa <strong>E</strong>.</p>",
  figs(("q171", "Rosa dos ventos com oito sentidos: N, NE, L, SE, S, SO, O e NO, separados por 45°.")),
  ["rotação", "rosa dos ventos"],
  enun=p(T(171, 0)) + "[[fig:1]]" + p(T(171, 2).replace("teto de um shopping", "teto de um <em>shopping</em>")) + LI("1ª mudança: 135° no sentido anti-horário;", "2ª mudança: 60° no sentido horário;", "3ª mudança: 45° no sentido anti-horário.") + p("Após a 3ª mudança, ele é orientado a reposicionar a câmera, com a menor amplitude possível, no sentido Noroeste (<em>NO</em>) devido a um movimento suspeito de um cliente.", T(171, 4)),
  alts={k: v.replace("º", "°") for k, v in D[171]["alternativas"].items()})
X(172, "Estatística", "<p>Pontos: 5 para o 1º, 4 para o 2º, …, 1 para o 5º, multiplicados pela frequência de cada ranking (I: 4, II: 9, III: 7, IV: 5).</p><ul><li>Ana: 5·4 + 2·9 + 4·7 + 4·5 = 20 + 18 + 28 + 20 = 86;</li><li>Bia: 4·4 + 1·9 + 5·7 + 2·5 = 16 + 9 + 35 + 10 = 70;</li><li>Caio: 3·4 + 4·9 + 3·7 + 1·5 = 12 + 36 + 21 + 5 = 74;</li><li>Dani: 2·4 + 5·9 + 1·7 + 3·5 = 8 + 45 + 7 + 15 = 75;</li><li>Edu: 1·4 + 3·9 + 2·7 + 5·5 = 4 + 27 + 14 + 25 = 70.</li></ul><p>A vencedora é <strong>Ana</strong>. Alternativa <strong>E</strong>.</p><p>Contar só os primeiros lugares daria a vitória a Dani (9 juízes), mas o método de Borda soma todas as posições.</p>",
  tags=["método de Borda", "média ponderada"],
  enun=p(T(172, 0).replace("um ranking", "um <em>ranking</em>").replace("este ranking", "este <em>ranking</em>").replace("no ranking", "no <em>ranking</em>"), T(172, 1).replace("os rankings", "os <em>rankings</em>").replace("cada ranking", "cada <em>ranking</em>"))
       + tabela(["Colocação", "<em>Ranking</em> I", "II", "III", "IV"], [["1º", "Ana", "Dani", "Bia", "Edu"], ["2º", "Bia", "Caio", "Ana", "Ana"], ["3º", "Caio", "Edu", "Caio", "Dani"], ["4º", "Dani", "Ana", "Edu", "Bia"], ["5º", "Edu", "Bia", "Dani", "Caio"]])
       + tabela(["<em>Ranking</em>", "Frequência"], [["I", "4"], ["II", "9"], ["III", "7"], ["IV", "5"]]) + p(T(172, 4)))
X(173, "Geometria plana", "<p>Durante o içamento, a viga, o chão e o cabo formam um triângulo retângulo com o ângulo reto em O, e a viga é a hipotenusa. Em todo triângulo retângulo, o ponto médio da hipotenusa fica à mesma distância dos três vértices: OM é sempre metade do comprimento da viga. A distância é constante, e o gráfico é uma reta horizontal. Alternativa <strong>A</strong>.</p>",
  figs(("q173", "Três estágios do içamento: no estágio 1, a viga está deitada no chão, com uma ponta em O, sob o cabo; no estágio 2, essa ponta sobe pelo cabo e a outra desliza no chão em direção a O; no estágio 3, a viga fica de pé, na vertical. M é o ponto médio da viga."),
       ("q173a", "Gráfico A: distância constante de 0 a t_f (reta horizontal)."),
       ("q173b", "Gráfico B: distância crescendo em linha reta."),
       ("q173c", "Gráfico C: distância diminuindo em linha reta."),
       ("q173d", "Gráfico D: distância sobe e depois desce, formando uma curva em arco."),
       ("q173e", "Gráfico E: distância desce e depois sobe, formando uma curva em U.")),
  ["triângulo retângulo", "mediana"],
  enun=p(T(173, 0)) + "[[fig:1]]" + p(T(173, 4).replace("tempo tf", "tempo <em>t</em><sub>f</sub>").replace("ponto O", "ponto <em>O</em>").replace("ponto M", "ponto <em>M</em>"), "O gráfico que descreve a distância do ponto <em>M</em> ao ponto <em>O</em>, em função do tempo, entre <em>t</em> = 0 e <em>t</em><sub>f</sub>, é"), alts=ALT(2))
X(174, "Logaritmo", "<p>Densidade em 1986: 100 000 ÷ 0,25 = 4 × 10<sup>5</sup> transistores/cm². Ela dobra a cada 2 anos: depois de n dobras, vale 4 × 10<sup>5</sup> × 2<sup>n</sup>.</p><p>" + K("4 \\times 10^5 \\times 2^n = 10^{11} \\Rightarrow 2^n = 2{,}5 \\times 10^5") + ". Aplicando log: n · 0,30 = log 2,5 + 5 = (1 − 2 · 0,30) + 5 = 5,4, logo n = 18 dobras.</p><p>18 × 2 = 36 anos: 1986 + 36 = <strong>2022</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["função exponencial", "Lei de Moore"],
  enun=p(T(174, 0), T(174, 1).replace("0,25 cm2", "0,25 cm<sup>2</sup>")) + fonte(T(174, 2)) + p("Considere 0,30 como aproximação para log<sub>10</sub> 2.", "Em que ano a empresa atingiu ou atingirá a densidade de 100 bilhões de transistores?"))
X(175, "Sistemas lineares", "<p>Seja p o valor de cada parcela. O total é o mesmo nos três planos:</p><p>Np = (N + 5)(p − 200) → 5p − 200N = 1 000 → p = 40N + 200.</p><p>Np = (N − 4)(p + 232) → −4p + 232N = 928 → p = 58N − 232.</p><p>40N + 200 = 58N − 232 → 18N = 432 → N = <strong>24</strong>. Alternativa <strong>B</strong>.</p><p>Conferindo: p = 1 160; 24 × 1 160 = 29 × 960 = 20 × 1 392 = 27 840.</p>",
  tags=["sistema de equações"], enun=p(T(175, 0).replace("em N parcelas", "em <em>N</em> parcelas"), T(175, 1).replace("quantidade N", "quantidade <em>N</em>")))
X(176, "Probabilidade", "<p>O atleta 10 tem 687,5 e o 1º lugar tem 829,0: precisa de mais de 829,0 − 687,5 = 141,5 no último salto. Nota estimada = nota de partida × soma dos juízes:</p><ul><li>T1: 2,2 × 57 = 125,4;</li><li>T2: 2,4 × 58 = 139,2;</li><li>T3: 2,6 × 55 = 143,0;</li><li>T4: 2,8 × 50 = 140,0;</li><li>T5: 3,0 × 53 = 159,0.</li></ul><p>Só T3 e T5 passam de 141,5. Entre eles, T3 tem a maior probabilidade (91,88% contra 87,34%). Alternativa <strong>C</strong>.</p>",
  tags=["tabela", "tomada de decisão"],
  enun=p(T(176, 0), T(176, 1)) + "<p><strong>Quadro 1</strong></p>" + tabela(["Classificação", "Atleta", "6º Salto", "Total"], [["1º", "3", "135,0", "829,0"], ["2º", "4", "140,0", "825,2"], ["3º", "8", "140,4", "824,2"], ["6º", "10", "", "687,5"]])
       + p(T(176, 4)) + "<p><strong>Quadro 2</strong></p>" + tabela(["Tipo de salto", "Nota de partida", "Estimativa da soma das notas dos juízes", "Probabilidade de obter a nota"], [["T1", "2,2", "57", "89,76%"], ["T2", "2,4", "58", "93,74%"], ["T3", "2,6", "55", "91,88%"], ["T4", "2,8", "50", "95,38%"], ["T5", "3,0", "53", "87,34%"]]) + p(T(176, 7)))
X(177, "Porcentagem", "<p>Total da população dos grupos: 4,5 + 2,0 + 2,5 + 0,5 + 20,5 = 30 milhões. Vacinados: 0,9 + 1,0 + 1,5 + 0,4 + 8,2 = 12 milhões.</p><p>12 ÷ 30 = 0,4 = <strong>40%</strong>. Alternativa <strong>D</strong>.</p><p>A média simples das porcentagens dos grupos (50%, E) não serve, porque os grupos têm tamanhos muito diferentes.</p>",
  tags=["porcentagem", "tabela"],
  enun=p(T(177, 0)) + tabela(["Grupo de risco", "População (milhão)", "População já vacinada (milhão)", "População já vacinada (%)"], [["Crianças", "4,5", "0,9", "20"], ["Profissionais de saúde", "2,0", "1,0", "50"], ["Gestantes", "2,5", "1,5", "60"], ["Indígenas", "0,5", "0,4", "80"], ["Idosos", "20,5", "8,2", "40"]]) + fonte(T(177, 2)) + p(T(177, 3)))
X(178, "Equações", "<p>Sejam a os alunos que compraram 3 bilhetes e u os que compraram 1. Total de bilhetes: B = 3a + 90 + u. Total de alunos do colégio: 80 + a + 45 + u.</p><p>B = alunos + 33 → 3a + 90 + u = a + u + 158 → a = 34. Então B = 192 + u.</p><p>u = 0,2B → u = 0,2(192 + u) → 0,8u = 38,4 → u = <strong>48</strong>. Alternativa <strong>D</strong>.</p>",
  tags=["equação do 1º grau", "porcentagem"])
X(179, "Geometria plana", "<p>No quebra-cabeça, cada triângulo tem como cateto a hipotenusa do triângulo menor seguinte: catetos de 2, " + K("2\\sqrt{2}") + ", 4, " + K("4\\sqrt{2}") + " e 8 cm. No lado direito do quadrado se encaixam, de baixo para cima, os catetos de 2 cm (o menor), 4 cm e 8 cm.</p><p>Lado do quadrado: 2 + 4 + 8 = <strong>14 cm</strong>. Alternativa <strong>A</strong>.</p><p>Conferindo: o triângulo maior, metade do quadrado, tem catetos de 14 cm.</p>",
  figs(("q179", "Quadrado dividido por uma diagonal: a metade de cima à esquerda é um único triângulo grande; a outra metade é recoberta por triângulos retângulos isósceles cada vez menores, até um pequeno triângulo preto no canto inferior direito.")),
  ["triângulo retângulo isósceles", "teorema de Pitágoras"], enun=p(T(179, 0)) + "[[fig:1]]" + p(T(179, 2)),
  alts=FR("14", "12", "7\\sqrt{2}", "6 + 4\\sqrt{2}", "6 + 2\\sqrt{2}"))
X(180, "Geometria espacial", "<p>A circunferência da base mede " + K("2\\pi \\cdot \\tfrac{6}{\\pi} = 12") + " cm. Na figura, a hélice dá 6 voltas no cilindro, então o comprimento horizontal da faixa é 6 × 12 = 72 cm.</p><p>A diagonal forma 30° com a borda inferior: altura = 72 · tg 30° = " + K("72 \\cdot \\tfrac{\\sqrt{3}}{3} = 24\\sqrt{3}") + " cm. Alternativa <strong>B</strong>.</p>",
  figs(("q180", "Faixa retangular de papel com uma diagonal que forma 30° com a borda inferior, sendo enrolada num cilindro; ao lado, o cilindro já envolvido, com a diagonal formando uma hélice de seis voltas.")),
  ["cilindro", "trigonometria"],
  enun=p("Para decorar um cilindro circular reto será usada uma faixa retangular de papel transparente, na qual está desenhada em negrito uma diagonal que forma 30° com a borda inferior. O raio da base do cilindro mede " + K("\\tfrac{6}{\\pi}") + " cm, e ao enrolar a faixa obtém-se uma linha em formato de hélice, como na figura.") + "[[fig:1]]" + p(T(180, 3)),
  alts=FR("36\\sqrt{3}", "24\\sqrt{3}", "4\\sqrt{3}", "36", "72"))

completar(Q, R)
