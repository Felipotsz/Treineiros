# Enem 2021, 2º dia, caderno azul: Matemática (questões 136 a 180 do caderno; no site, 1 a 45, com numeroOriginal).
# Texto do PDF embaralhado: rascunho feito com DECOD=1. Símbolos matemáticos (φ, π, √, frações, ·) não decodificam:
# fórmulas das Q136, 141, 142, 146, 152, 156, 157, 163, 169, 170, 171, 177 e 179 escritas à mão.
# Quadros em tabela HTML. Q138 (brasões de clubes) sem imagem: os campeões viram tabela.
# Anulada: Q138 (Inep não deu motivo; pela análise, nenhuma alternativa está certa).
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, paragrafos_enem

ID = "enem-2021-matematica"
META = {"id": ID, "banca": "Enem", "ano": 2021, "titulo": "Enem 2021: Matemática", "fonte": "Inep", "dataExame": "2021-11-28",
        "duracaoMinutos": 150, "area": "Matemática", "caderno": "azul", "dia": 2}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2021-dia2-azul")
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


X(136, "Sequências", "<p>Multiplicando por φ e usando φ<sup>2</sup> = φ + 1: φ<sup>7</sup> = φ · φ<sup>6</sup> = φ(8φ + 5) = 8φ<sup>2</sup> + 5φ = 8(φ + 1) + 5φ = <strong>13φ + 8</strong>. Repare no padrão: os coeficientes seguem a sequência de Fibonacci (1, 1, 2, 3, 5, 8, 13…). Alternativa <strong>E</strong>.</p><p>11φ + 7 (D) somaria os coeficientes de forma errada; 9φ + 6 (C) não segue a regra.</p>",
  tags=["proporção áurea", "Fibonacci"],
  enun=p("Um segmento de reta está dividido em duas partes na proporção áurea quando o todo está para uma das partes na mesma razão em que essa parte está para a outra. Essa constante de proporcionalidade é comumente representada pela letra grega φ, e seu valor é dado pela solução positiva da equação φ<sup>2</sup> = φ + 1.",
         "Assim como a potência φ<sup>2</sup>, as potências superiores de φ podem ser expressas da forma <em>a</em>φ + <em>b</em>, em que <em>a</em> e <em>b</em> são inteiros positivos, como apresentado no quadro.")
       + tabela(["φ<sup>2</sup>", "φ<sup>3</sup>", "φ<sup>4</sup>", "φ<sup>5</sup>", "φ<sup>6</sup>", "φ<sup>7</sup>"], [["φ + 1", "2φ + 1", "3φ + 2", "5φ + 3", "8φ + 5", "…"]])
       + p("A potência φ<sup>7</sup>, escrita na forma <em>a</em>φ + <em>b</em> (<em>a</em> e <em>b</em> são inteiros positivos), é"),
  alts={"A": "5φ + 3", "B": "7φ + 2", "C": "9φ + 6", "D": "11φ + 7", "E": "13φ + 8"})
X(137, "Geometria espacial", "<p>O cubo está apoiado num vértice, com a diagonal que passa por ele perpendicular ao solo. Olhando de cima, essa diagonal vira um ponto (o centro), os seis vértices restantes formam um <strong>hexágono regular</strong>, e as arestas que saem do vértice de cima e do de baixo viram segmentos do centro até os vértices do hexágono. As outras três diagonais também passam pelo centro e ligam vértices opostos do hexágono. O desenho é um hexágono com os seis “raios” ligando o centro aos vértices. Alternativa <strong>E</strong>.</p><p>A e B mostram projeções com o cubo em outras posições; C e D, apoiado numa face.</p>",
  figs(("q137", "Foto do Atomium, em Bruxelas: esferas metálicas nos vértices de um cubo apoiado em um vértice, ligadas por tubos, com uma esfera no centro."),
       ("q137a", "Hexágono com um losango interno e várias diagonais cruzadas formando um padrão estrelado."),
       ("q137b", "Losango com as duas diagonais."),
       ("q137c", "Retângulo com as duas diagonais e um segmento vertical no meio."),
       ("q137d", "Retângulo dividido ao meio por um segmento vertical."),
       ("q137e", "Hexágono regular com segmentos ligando o centro a cada um dos seis vértices.")),
  ["projeção ortogonal", "cubo"],
  enun=p(T(137, 0), T(137, 1), T(137, 2), T(137, 3)) + "[[fig:1]]" + fonte(T(137, 5)) + p(T(137, 6)), alts=ALT(2))
X(138, "Análise combinatória", "<p>As placas são todas diferentes (cada uma tem o ano do título), então em cada linha a ordem importa. Linha 1, gaúchos: Grêmio 5 + Internacional 1 + Juventude 1 = 7 placas para 5 posições: 7!/2!. Linha 2, cariocas: Flamengo 3 + Vasco 1 + Fluminense 1 = 5 placas: 5!. Linha 3, mineiros: Cruzeiro 6 + Atlético 1 = 7 placas: 7!/2!. Linha 4, paulistas: 3 + 3 + 1 + 1 + 1 = 9 placas: 9!/4!. As 10 placas que sobram ocupam as duas últimas linhas: 10!. Total: \\(\\frac{7!}{2!} \\cdot 5! \\cdot \\frac{7!}{2!} \\cdot \\frac{9!}{4!} \\cdot 10!\\).</p><p>A alternativa E traz todos esses fatores, menos o primeiro: escreve 9!/3! no lugar de 7!/2!. Nenhuma alternativa está certa. A resposta esperada seria a E, com 7!/2! no primeiro fator. Alternativa <strong>E</strong>, se a questão não tivesse sido anulada.</p>",
  tags=["arranjo", "princípio multiplicativo"],
  anulacao={"fonte": "analise", "motivo": "O Inep anulou a questão no gabarito oficial sem divulgar o motivo. Pela análise, nenhuma alternativa traz a expressão correta: a mais próxima (E) usa 9!/3! para a linha dos clubes gaúchos, que têm 7 títulos (o certo seria 7!/2!)."},
  enun=p(T(138, 0).replace("conforme apresentado na imagem", "conforme apresentado no quadro"))
       + tabela(["Clube", "Estado", "Títulos"],
                [["Cruzeiro", "Minas Gerais", "06"], ["Grêmio", "Rio Grande do Sul", "05"], ["Corinthians", "São Paulo", "03"], ["Flamengo", "Rio de Janeiro", "03"],
                 ["Palmeiras", "São Paulo", "03"], ["Internacional", "Rio Grande do Sul", "01"], ["Criciúma", "Santa Catarina", "01"], ["Vasco da Gama", "Rio de Janeiro", "01"],
                 ["Atlético Mineiro", "Minas Gerais", "01"], ["Santos", "São Paulo", "01"], ["Fluminense", "Rio de Janeiro", "01"], ["Sport", "Pernambuco", "01"],
                 ["Paulista FC", "São Paulo", "01"], ["Santo André", "São Paulo", "01"], ["Juventude", "Rio Grande do Sul", "01"]])
       + fonte("Disponível em: http://campeoesdofutebol.com.br. Acesso em: 1 nov. 2018 (adaptado). No original, cada clube aparece com seu brasão.")
       + p(T(138, 11)),
  alts=FR("\\frac{7!}{5!} \\cdot \\frac{5!}{3!} \\cdot \\frac{7!}{6!} \\cdot \\frac{9!}{3!\\,3!} \\cdot 10!", "7! \\cdot 5! \\cdot 7! \\cdot 9! \\cdot 10!", "30!",
          "\\frac{7!}{5!\\,5!} \\cdot \\frac{7!}{5!\\,2!} \\cdot \\frac{9!}{5!\\,4!}", "\\frac{9!}{3!} \\cdot 5! \\cdot \\frac{7!}{2!} \\cdot \\frac{9!}{4!} \\cdot 10!"))
X(139, "Estatística", "<p>Como são as mesmas três franquias para todos os lanches, a maior média é a da maior soma. I: 415 + 415 + 415 = 1 245; II: 395 + 445 + 390 = 1 230; III: 425 + 370 + 425 = 1 220; IV: 430 + 370 + 433 = 1 233; V: 435 + 425 + 420 = <strong>1 280</strong> (média ≈ 426,7). O escolhido é o lanche <strong>V</strong>. Alternativa <strong>E</strong>.</p><p>O lanche II (B) tem a maior venda isolada (445), mas não a maior média.</p>",
  tags=["média aritmética"],
  enun=p(T(139, 0)) + tabela(["", "Lanche I", "Lanche II", "Lanche III", "Lanche IV", "Lanche V"],
                             [["<strong>Franquia I</strong>", "415", "395", "425", "430", "435"], ["<strong>Franquia II</strong>", "415", "445", "370", "370", "425"],
                              ["<strong>Franquia III</strong>", "415", "390", "425", "433", "420"]]) + p(T(139, 2)))
X(140, "Estatística", "<p>A média mensal é a média ponderada pelos meses: (3,5 · 3 + 2,5 · 2 + 5 · 2 + 3 · 4 + 7,5 · 1) ÷ 12 = (10,5 + 5 + 10 + 12 + 7,5) ÷ 12 = 45 ÷ 12 = <strong>3,75 milhões</strong>. Como 2 ≤ 3,75 &lt; 4, a comissão é do tipo <strong>II</strong>. Alternativa <strong>B</strong>.</p><p>A média simples dos cinco valores (4,3) daria tipo III (C), mas ignora quantos meses cada faturamento ocorreu.</p>",
  tags=["média ponderada"],
  enun=p(T(140, 0).replace("(M)", "(<em>M</em>)")) + tabela(["Comissão", "Média de faturamento mensal (<em>M</em>)"],
                             [["I", "1 ≤ <em>M</em> &lt; 2"], ["II", "2 ≤ <em>M</em> &lt; 4"], ["III", "4 ≤ <em>M</em> &lt; 5"], ["IV", "5 ≤ <em>M</em> &lt; 6"], ["V", "<em>M</em> ≥ 6"]])
       + p(T(140, 2)) + tabela(["Faturamento mensal (em milhão de real)", "Quantidade de meses"], [["3,5", "3"], ["2,5", "2"], ["5", "2"], ["3", "4"], ["7,5", "1"]]) + p(T(140, 4)))
X(141, "Funções", "<p>O total das diárias é <em>d</em> · <em>n</em>. A taxa de serviço é o percentual <em>s</em> sobre esse total: <em>d</em> · <em>n</em> · <em>s</em>. Somando a taxa fixa de limpeza: <strong><em>P</em> = <em>d</em> · <em>n</em> + <em>L</em> + <em>d</em> · <em>n</em> · <em>s</em></strong>. Alternativa <strong>A</strong>.</p><p>B aplica a taxa sobre uma diária só; E soma o percentual como se fosse um valor em reais; D esquece o valor das diárias.</p>",
  tags=["expressão algébrica", "porcentagem"],
  enun=p(T(141, 0).replace("preço P", "preço <em>P</em>").replace("diária d,", "diária <em>d</em>,").replace("limpeza L", "limpeza <em>L</em>").replace("percentual s", "percentual <em>s</em>"),
         T(141, 1).replace(" n diárias", " <em>n</em> diárias")),
  alts=FR("P = d \\cdot n + L + d \\cdot n \\cdot s", "P = d \\cdot n + L + d \\cdot s", "P = d + L + s", "P = d \\cdot n \\cdot s + L", "P = d \\cdot n + L + s"))
X(142, "Probabilidade", "<p>O jogador não pontua só se errar todos os dardos. Com <em>n</em> dardos, P(pontuar) = 1 − (1/2)<sup><em>n</em></sup>. Queremos 1 − (1/2)<sup><em>n</em></sup> ≥ 9/10, isto é, (1/2)<sup><em>n</em></sup> ≤ 1/10, ou 2<sup><em>n</em></sup> ≥ 10. Como 2<sup>3</sup> = 8 e 2<sup>4</sup> = 16, o mínimo é <strong>4 dardos</strong>. Alternativa <strong>B</strong>.</p><p>Com 3 dardos, a chance é 7/8 = 0,875, ainda abaixo de 0,9.</p>",
  tags=["evento complementar"],
  enun=p(T(142, 0)[:-2] + " \\(\\frac{1}{2}\\) de probabilidade de acertar um dardo no alvo.",
         T(142, 2)[:-2] + " \\(\\frac{9}{10}\\). Para isso, decide aumentar a quantidade de dardos a serem lançados em cada rodada.", T(142, 4)))
X(143, "Estatística", "<p>O volume de água é a capacidade vezes o nível de ocupação. I: 105 × 20% = 21; II: 100 × 30% = 30; III: 20 × 50% = 10; IV: 80 × 40% = <strong>32</strong>; V: 40 × 60% = 24 (em bilhão de litros). O maior volume está no reservatório <strong>IV</strong>. Alternativa <strong>D</strong>.</p><p>O V (E) tem o maior percentual, mas é pequeno; o I (A) é o maior, mas está quase vazio.</p>",
  figs(("q143", "Gráfico de barras “Nível dos reservatórios em 2 fev. 2015”, com a capacidade de cada um no topo: I, 105 bilhões de litros, nível 20%; II, 100, nível 30%; III, 20, nível 50%; IV, 80, nível 40%; V, 40, nível 60%.")),
  ["porcentagem", "leitura de gráfico"], enun=p(T(143, 0)) + "[[fig:1]]" + p(T(143, 6)))
X(144, "Estatística", "<p>Pelo gráfico, 6 alunos têm 9 anos, 12 têm 18 e 9 têm 27. Média ponderada: (6 · 9 + 12 · 18 + 9 · 27) ÷ (6 + 12 + 9) = (54 + 216 + 243) ÷ 27 = 513 ÷ 27 = <strong>19 anos</strong>. Alternativa <strong>D</strong>.</p><p>A média simples das idades (9 + 18 + 27)/3 = 18 (C) ignora as frequências; 9 e 12 (A e B) são frequências.</p>",
  figs(("q144", "Gráfico de barras da frequência de ocorrência por idade (ano): 9 anos, frequência 6; 18 anos, frequência 12; 27 anos, frequência 9.")),
  ["média ponderada"], enun=p(T(144, 0)) + "[[fig:1]]" + p(T(144, 3)))
X(145, "Estatística", "<p>A média geral (6 min) é a média ponderada das faixas: 3<em>x</em> + 5<em>y</em> + 12<em>x</em> = 6 · 100, ou seja, 15<em>x</em> + 5<em>y</em> = 600. Os percentuais somam 100: 2<em>x</em> + <em>y</em> = 100, então <em>y</em> = 100 − 2<em>x</em>. Substituindo: 15<em>x</em> + 500 − 10<em>x</em> = 600, <em>x</em> = <strong>20</strong> e <em>y</em> = <strong>60</strong>. Alternativa <strong>C</strong>.</p><p>Os pares 10 e 80 e 25 e 50 (A e E) somam 100%, mas dão médias diferentes de 6 minutos.</p>",
  tags=["média ponderada", "sistema linear"],
  enun=p(T(145, 0)) + tabela(["Faixa etária", "Percentual de entrevistados"], [["De 10 a 24 anos", "<em>x</em>"], ["Entre 24 e 60 anos", "<em>y</em>"], ["A partir de 60 anos", "<em>x</em>"]])
       + fonte(T(145, 2)) + p(T(145, 3).replace(" x e y ", " <em>x</em> e <em>y</em> ")))
X(146, "Estatística", "<p>CV da ração atual: 1/10 = 0,1. Com a nova, CV = 1,5/<em>x̄</em>. A troca acontece se 1,5/<em>x̄</em> &lt; 0,1, ou seja, <em>x̄</em> &gt; 1,5/0,1 = <strong>15 kg</strong>. Alternativa <strong>E</strong>.</p><p>10,0 (C) é a média atual; com média 10 e desvio 1,5, o CV seria 0,15, maior que 0,1.</p>",
  tags=["coeficiente de variação", "desvio padrão"],
  enun=p(T(146, 0), T(146, 1),
         "Para avaliar a eficiência dessa ração, ele utilizará o coeficiente de variação (<em>CV</em>) que é uma medida de dispersão definida por \\(CV = \\frac{s}{\\bar{x}}\\), em que <em>s</em> representa o desvio padrão e \\(\\bar{x}\\), a média das massas dos coelhos que foram alimentados com uma determinada ração.",
         T(146, 3)))
X(147, "Raciocínio lógico", "<p>No gráfico, as quatro letras mais frequentes do texto original são A (cerca de 70 mil), E (cerca de 64 mil), O (cerca de 52 mil) e S (cerca de 39 mil). A codificação troca cada letra pela que está três posições à frente: A → D, E → H, O → R e S → V. No texto codificado, as mais frequentes são <strong>D, H, R e V</strong>. Alternativa <strong>C</strong>.</p><p>A, E, O e S (A) são as letras do original, antes da codificação.</p>",
  figs(("q147", "Gráfico de barras da frequência de cada letra de A a Z em O guarani: as mais altas são A (cerca de 70 000), E (cerca de 64 000), O (cerca de 52 000), S (cerca de 39 000), R (cerca de 33 000) e I (cerca de 32 000); K, W e Y quase não aparecem.")),
  ["cifra de César", "leitura de gráfico"],
  enun=p(T(147, 0), T(147, 1)) + tabela(["Original"] + list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), [["Codificado"] + list("DEFGHIJKLMNOPQRSTUVWXYZABC")])
       + p(T(147, 3).replace("O guarani", "<em>O guarani</em>")) + "[[fig:1]]" + fonte(T(147, 6)) + p(T(147, 7), T(147, 8)))
X(148, "Estatística", "<p>Ordenando os 12 valores: 11, 11, 12, 13, 15, 15, 16, 16, 17, 18, 20, 24. Com quantidade par, a mediana é a média dos dois centrais (6º e 7º): (15 + 16) ÷ 2 = <strong>15,5</strong>. Alternativa <strong>C</strong>.</p><p>15,7 (D) é a média aritmética (188 ÷ 12); 15 e 11 (B e A) são modas.</p>",
  tags=["mediana"],
  enun=p(T(148, 0)) + tabela(["Ano", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011"],
                             [["Terremotos", "15", "16", "13", "15", "16", "11", "11", "18", "12", "17", "24", "20"]]) + fonte(T(148, 2)) + p(T(148, 3), T(148, 4)))
X(149, "Estatística", "<p>Lucro = receita − despesa. Pelo gráfico: janeiro 10 − 5 = 5; fevereiro 20 − 10 = <strong>10</strong>; março 15 − 10 = 5; abril 20 − 15 = 5; maio 28 − 25 = 3 (em milhão). O maior lucro foi o de <strong>fevereiro</strong>. Alternativa <strong>B</strong>.</p><p>Maio (E) tem a maior receita, mas também a maior despesa, e o menor lucro.</p>",
  figs(("q149", "Gráfico “Receitas e despesas”, em milhão de real: receita (linha cheia) de 10 em janeiro, 20 em fevereiro, 15 em março, 20 em abril e 28 em maio; despesa (linha tracejada) de 5 em janeiro, 10 em fevereiro, 10 em março, 15 em abril e 25 em maio.")),
  ["leitura de gráfico"], enun=p(T(149, 0).replace("receita R", "receita <em>R</em>").replace("despesa D", "despesa <em>D</em>")) + "[[fig:1]]" + p(T(149, 3)))
X(150, "Porcentagem", "<p>As vendas foram de 236 (2005) para 519,2 milhões (2009). Aumento: 519,2 − 236 = 283,2. Em relação ao valor inicial: 283,2 ÷ 236 = 1,2, ou seja, <strong>120%</strong>. Alternativa <strong>C</strong>.</p><p>283,2 (E) é o aumento absoluto; 220 (D) seria o valor final em relação ao inicial (220%), não o aumento.</p>",
  figs(("q150", "Gráfico de linha do volume de vendas (em milhão) por ano: 236 em 2005, 294 em 2006, 370 em 2007, 465 em 2008 e 519,2 em 2009.")),
  ["variação percentual"], enun=p(T(150, 0)) + "[[fig:1]]" + fonte(T(150, 2)) + p(T(150, 3)))
X(151, "Estatística", "<p>Pelo histograma, as faixas têm 5, 10, 5, 15, 20, 15, 15, 10, 5 e 5 imóveis (total 105). Metade é 52,5. Acumulando: até 400 → 5; até 500 → 15; até 600 → 20; até 700 → 35; até 800 → <strong>55</strong>. Só a partir de 800 mil reais pelo menos 50% dos imóveis custam menos. Alternativa <strong>C</strong>.</p><p>Até 600 mil (A) há só 20 imóveis, 19% do total, o que mostra que o anúncio de 50% abaixo de 550 mil não era compatível.</p>",
  figs(("q151", "Histograma “Distribuição dos preços”: número de imóveis por faixa de preço (em mil reais): 300–400: 5; 400–500: 10; 500–600: 5; 600–700: 15; 700–800: 20; 800–900: 15; 900–1 000: 15; 1 000–1 100: 10; 1 100–1 200: 5; 1 200–1 300: 5.")),
  ["histograma", "frequência acumulada"],
  enun=p(T(151, 0), T(151, 1), T(151, 2)) + "[[fig:1]]" + p("Com base no gráfico obtido, o menor preço, <em>p</em> (em mil reais), para o qual pelo menos 50% dos apartamentos apresenta preço inferior a <em>p</em> é"))
X(152, "Equações", "<p>Com <em>b</em> = 1: <em>a</em>Δ1 = <em>a</em><sup>2</sup> + <em>a</em> − 1 e 1Δ<em>a</em> = 1 + <em>a</em> − <em>a</em><sup>2</sup>. Como <em>x</em> * <em>y</em> = <em>x</em>(<em>y</em> + 1), a equação vira (<em>a</em><sup>2</sup> + <em>a</em> − 1)(2 + <em>a</em> − <em>a</em><sup>2</sup>) = 0. Primeiro fator: <em>a</em> = (−1 ± √5)/2. Segundo: <em>a</em><sup>2</sup> − <em>a</em> − 2 = 0, <em>a</em> = 2 ou <em>a</em> = −1. As duas maiores soluções são 2 e (−1 + √5)/2, que somam <strong>(3 + √5)/2</strong>. Alternativa <strong>E</strong>.</p><p>(−1 + √5)/2 (D) é só uma das soluções.</p>",
  tags=["operações definidas", "equação do 2º grau"],
  enun=p("Para a comunicação entre dois navios é utilizado um sistema de codificação com base em valores numéricos. Para isso, são consideradas as operações triângulo Δ e estrela ∗, definidas sobre o conjunto dos números reais por \\(x \\Delta y = x^2 + xy - y^2\\) e \\(x * y = xy + x\\).",
         "O navio que deseja enviar uma mensagem deve fornecer um valor de entrada <em>b</em>, que irá gerar um valor de saída, a ser enviado ao navio receptor, dado pela soma das duas maiores soluções da equação \\((a \\Delta b) * (b \\Delta a) = 0\\). Cada valor possível de entrada e saída representa uma mensagem diferente já conhecida pelos dois navios.",
         "Um navio deseja enviar ao outro a mensagem “ATENÇÃO!”. Para isso, deve utilizar o valor de entrada <em>b</em> = 1.", "Dessa forma, o valor recebido pelo navio receptor será"),
  alts=FR("\\sqrt{5}", "\\sqrt{3}", "\\sqrt{1}", "\\frac{-1 + \\sqrt{5}}{2}", "\\frac{3 + \\sqrt{5}}{2}"))
X(153, "Razão e proporção", "<p>Escala = medida da réplica ÷ medida real, nas mesmas unidades. Comprimento: 160 cm ÷ 3 840 cm = 1/24. Largura: 7 cm ÷ 168 cm = 1/24. A escala é <strong>1 : 24</strong>. Alternativa <strong>C</strong>.</p><p>1 : 240 (B) e 1 : 2,4 (E) vêm de erro na conversão de metro para centímetro; 1 : 576 (A) é a razão entre áreas (24<sup>2</sup>).</p>",
  figs(("q153", "Foto do castelo de Liechtenstein, com torres brancas sobre um rochedo cercado de árvores e uma ponte de acesso.")),
  ["escala"], enun=p(T(153, 0)) + "[[fig:1]]" + p(T(153, 2), T(153, 3)))
X(154, "Razão e proporção", "<p>Médicos: de 1990 a 2000 e de 2000 a 2010 a variação foi de 73 000; a média é 73 000, e em 2020 seriam 365 000 + 73 000 = 438 000. População (em milhar): variações de 23 000 e 21 000, média 22 000; em 2020, 191 000 + 22 000 = 213 000 mil = 213 milhões. Médicos por mil habitantes: 438 000 ÷ 213 000 ≈ <strong>2,06</strong>. Alternativa <strong>D</strong>.</p><p>1,71 (C) é o valor de 2010 (365 000 ÷ 191 000), sem a projeção.</p>",
  tags=["taxa", "projeção"],
  enun=p(T(154, 0)) + tabela(["Ano", "Médicos", "População brasileira (em milhar)"], [["1990", "219 000", "147 000"], ["2000", "292 000", "170 000"], ["2010", "365 000", "191 000"]])
       + p(T(154, 2) + " " + T(154, 3)) + fonte(T(154, 4)) + p(T(154, 5)))
X(155, "Porcentagem", "<p>Custo atual: frango 0,4 × 12,50 = 5,00; batata-doce 0,6 × 5,00 = 3,00; hortaliça 2,00; total R$ 10,00. Com o aumento de 50%, a batata custa 7,50/kg e os 600 g passam a 4,50. Sobram 10 − 4,50 − 2,00 = R$ 3,50 para o frango: 3,50 ÷ 12,50 = 0,28 kg = 280 g. A redução é de 120 g sobre 400 g: <strong>30%</strong>. Alternativa <strong>C</strong>.</p><p>28,0 (B) é a nova quantidade em centenas de gramas, não a redução.</p>",
  tags=["porcentagem", "custo"],
  enun=p(T(155, 0)) + tabela(["Refeição", "Frango (kg)", "Batata-doce (kg)", "Hortaliças (unidade)"], [["", "R$ 12,50", "R$ 5,00", "R$ 2,00"]]) + p(T(155, 2), T(155, 3)))
X(156, "Trigonometria", "<p>No gráfico, a curva começa em <em>P</em> = −3 (a mola solta na posição distendida, abaixo do equilíbrio), então a amplitude é 3 e a função é do tipo −3 cos(ω<em>t</em>), que vale −3 em <em>t</em> = 0. O primeiro máximo aparece em π/2 e a curva volta a −3 em π: o período é <em>T</em> = π, então ω = 2π/π = 2. A expressão é <strong>−3 cos(2<em>t</em>)</strong>. Alternativa <strong>A</strong>.</p><p>−3 sen(2<em>t</em>) (B) começaria em zero; −6 cos (D) teria amplitude 6.</p>",
  figs(("q156", "À esquerda, uma mola com uma massa m na posição de equilíbrio e a mesma mola distendida, com a massa mais abaixo. À direita, o gráfico de P em função de t: a curva começa em −3 em t = 0, sobe a 3 em π/2, desce a −3 em π, e repete esse ciclo em 3π/2, 2π, 5π/2 e 3π.")),
  ["função cosseno", "período"],
  enun=p("Uma mola é solta da posição distendida conforme a figura. A figura à direita representa o gráfico da posição <em>P</em> (em cm) da massa <em>m</em> em função do tempo <em>t</em> (em segundo) em um sistema de coordenadas cartesianas. Esse movimento periódico é descrito por uma expressão do tipo \\(P(t) = \\pm A \\cos(\\omega t)\\) ou \\(P(t) = \\pm A \\,\\text{sen}(\\omega t)\\), em que <em>A</em> &gt; 0 é a amplitude de deslocamento máximo e ω é a frequência, que se relaciona com o período <em>T</em> pela fórmula \\(\\omega = \\frac{2\\pi}{T}\\).",
         T(156, 1)) + "[[fig:1]]" + p(T(156, 4).replace("P(t)", "<em>P</em>(<em>t</em>)").replace("massa m", "massa <em>m</em>")),
  alts=FR("-3\\cos(2t)", "-3\\,\\text{sen}(2t)", "3\\cos(2t)", "-6\\cos(2t)", "6\\,\\text{sen}(2t)"))
X(157, "Matrizes", "<p>O elemento <em>a<sub>ij</sub></em> conta famílias que foram de <em>i</em> para <em>j</em>. O fluxo que chega a uma região é a soma da sua <strong>coluna</strong>. Coluna 1: 0 + 0 + 2 + 1 + 1 = 4; coluna 2: 4 + 0 + 2 + 0 + 2 = 8; coluna 3: 2 + 6 + 0 + 2 + 0 = 10; coluna 4: 2 + 2 + 3 + 0 + 4 = 11; coluna 5: 5 + 3 + 0 + 4 + 0 = <strong>12</strong>. A região escolhida é a <strong>5</strong>. Alternativa <strong>E</strong>.</p><p>Somar as linhas (famílias que saíram) daria a região 1 ou 2 (A e B), justamente o que o texto manda não considerar.</p>",
  tags=["matriz", "interpretação de elementos"],
  enun=p("Uma construtora, pretendendo investir na construção de imóveis em uma metrópole com cinco grandes regiões, fez uma pesquisa sobre a quantidade de famílias que mudaram de uma região para outra, de modo a determinar qual região foi o destino do maior fluxo de famílias, sem levar em consideração o número de famílias que deixaram a região. Os valores da pesquisa estão dispostos em uma matriz \\(A = [a_{ij}],\\ i, j \\in \\{1, 2, 3, 4, 5\\}\\), em que o elemento \\(a_{ij}\\) corresponde ao total de famílias (em dezena) que se mudaram da região <em>i</em> para a região <em>j</em> durante um certo período, e o elemento \\(a_{ii}\\) é considerado nulo, uma vez que somente são consideradas mudanças entre regiões distintas. A seguir, está apresentada a matriz com os dados da pesquisa.")
       + '<p class="centro">\\(A = \\begin{pmatrix} 0 & 4 & 2 & 2 & 5 \\\\ 0 & 0 & 6 & 2 & 3 \\\\ 2 & 2 & 0 & 3 & 0 \\\\ 1 & 0 & 2 & 0 & 4 \\\\ 1 & 2 & 0 & 4 & 0 \\end{pmatrix}\\)</p>' + p(T(157, 2)))
X(158, "Porcentagem", "<p>Consumo do avião lotado = consumo por km e por passageiro × passageiros × distância. No modelo B, o número de passageiros é multiplicado por 1,1 e o consumo por passageiro por 0,9: 1,1 × 0,9 = 0,99. O consumo total de B é 99% do de A, ou seja, <strong>1% menor</strong>. Alternativa <strong>B</strong>.</p><p>Achar que +10% e −10% se anulam leva a “igual” (C), mas as porcentagens incidem sobre bases diferentes.</p>",
  tags=["porcentagens sucessivas"])
X(159, "Razão e proporção", "<p>O tempo é inversamente proporcional ao número de pessoas: com 3 pessoas, 4 s; com 2 pessoas, <em>t</em> = 4 × 3/2 = 6 s. Os grupos trabalham ao mesmo tempo, então a troca dos quatro pneus termina quando o grupo mais lento acaba: <strong>6,0 s</strong>. Alternativa <strong>A</strong>.</p><p>Fazer uma média entre os grupos (4,5 s, D) não faz sentido, porque o carro só sai quando todos os pneus estão trocados.</p>",
  tags=["grandezas inversamente proporcionais"])
X(160, "Raciocínio lógico", "<p>Para cada suplemento, o número de sachês é o maior entre as necessidades de A (800), B (1 000) e C (1 200). I: 16 sachês (por causa do A) × R$ 2 = R$ 32; II: 6 (C) × R$ 3 = R$ 18; III: 4 (A e C) × R$ 5 = R$ 20; IV: 2 (os três) × R$ 6 = <strong>R$ 12</strong>; V: 2 (A) × R$ 8 = R$ 16. O mais barato é o <strong>IV</strong>. Alternativa <strong>D</strong>.</p><p>O suplemento I é o de menor preço por sachê, mas exige muitos sachês.</p>",
  tags=["otimização", "arredondamento para cima"],
  enun=p(T(160, 0), T(160, 1)) + LISTA(T(160, 2)) + p(T(160, 3), T(160, 4)))
X(161, "Funções", "<p>Com desconto <em>x</em> (inteiro), o ingresso custa 20 − <em>x</em> e vão 200 + 40<em>x</em> pessoas. Arrecadação: (20 − <em>x</em>)(200 + 40<em>x</em>), uma função do 2º grau com concavidade para baixo: vale 4 000 em <em>x</em> = 0, chega ao máximo de 6 250 em <em>x</em> = 7,5 e zera em <em>x</em> = 20. Como só valem descontos inteiros, o gráfico é formado por <strong>pontos isolados sobre uma parábola</strong>. Alternativa <strong>E</strong>.</p><p>D tem a forma certa, mas é uma curva contínua, que admitiria descontos não inteiros.</p>",
  figs(("q161a", "Gráfico de arrecadação em função do desconto (0 a 23): uma reta crescente de 4 000 até cerca de 5 600 em 20."),
       ("q161b", "Gráfico de arrecadação em função do desconto: pontos isolados em linha crescente, de 4 000 em 0 até cerca de 5 600 em 20."),
       ("q161c", "Gráfico de arrecadação em função do desconto: uma reta levemente decrescente, de 4 000 até cerca de 3 700 em 20."),
       ("q161d", "Gráfico de arrecadação em função do desconto: uma curva contínua em forma de parábola, começando em 4 000, com máximo de cerca de 6 250 perto de 7,5 e chegando a zero em 20."),
       ("q161e", "Gráfico de arrecadação em função do desconto: pontos isolados formando uma parábola, começando em 4 000, com máximo de cerca de 6 250 entre 7 e 8 e chegando a zero em 20.")),
  ["função quadrática", "domínio discreto"], enun=p(T(161, 0), T(161, 1)), alts=ALT(1))
X(162, "Funções", "<p>Até 5 000 o imposto é zero. Em <em>R</em> = 10 000: 10% de 5 000 = 500. Em <em>R</em> = 15 000: 500 + 30% de 5 000 = 500 + 1 500 = <strong>2 000</strong>. O gráfico é nulo até 5 000, sobe em linha reta até 500 em 10 000 e depois sobe mais inclinado até 2 000 em 15 000. Alternativa <strong>A</strong>.</p><p>B e E param em 1 000, como se a alíquota fosse 10% também na última faixa; D desenha degraus, mas o imposto cresce continuamente.</p>",
  figs(("q162a", "Gráfico de I em função de R: zero até 5 000, segmento até 500 em 10 000 e segmento mais inclinado até 2 000 em 15 000."),
       ("q162b", "Gráfico de I em função de R: zero até 5 000, depois uma única reta até 500 em 10 000 e 1 000 em 15 000."),
       ("q162c", "Gráfico de I em função de R: reta desde a origem até 500 em 10 000, depois segmento até 1 000 em 15 000."),
       ("q162d", "Gráfico de I em função de R em degraus: zero até 5 000, constante igual a 500 entre 5 000 e 10 000, constante igual a 2 000 entre 10 000 e 15 000."),
       ("q162e", "Gráfico de I em função de R: reta começando em 5 000 no zero, passando por 500 em 10 000 e chegando a 1 000 em 15 000.")),
  ["função definida por partes"],
  enun=p("O quadro representa a relação entre o preço de um produto (<em>R</em>) e seu respectivo imposto devido (<em>I</em>).")
       + tabela(["Preço do produto (<em>R</em>)", "Imposto devido (<em>I</em>)"],
                [["<em>R</em> ≤ 5 000", "isento"], ["5 000 &lt; <em>R</em> ≤ 10 000", "10% de (<em>R</em> − 5 000)"], ["10 000 &lt; <em>R</em> ≤ 15 000", "500 + 30% de (<em>R</em> − 10 000)"]])
       + p("O gráfico que melhor representa essa relação é"), alts=ALT(1))
X(163, "Grandezas e medidas", "<p>A relação é <em>K</em> = <em>c</em> · <em>v</em><sup>2</sup> · ρ, com <em>c</em> adimensional. Unidades: (m/s)<sup>2</sup> · kg/m<sup>3</sup> = m<sup>2</sup> · s<sup>−2</sup> · kg · m<sup>−3</sup> = <strong>kg · m<sup>−1</sup> · s<sup>−2</sup></strong>, que é a unidade de pressão (pascal). Alternativa <strong>B</strong>.</p><p>Usar a velocidade sem elevar ao quadrado daria kg · m<sup>−2</sup> · s<sup>−1</sup> (A).</p>",
  tags=["análise dimensional"],
  alts=FR("kg \\cdot m^{-2} \\cdot s^{-1}", "kg \\cdot m^{-1} \\cdot s^{-2}", "kg \\cdot m^{-5} \\cdot s^{2}", "kg^{-1} \\cdot m^{1} \\cdot s^{2}", "kg^{-1} \\cdot m^{5} \\cdot s^{-2}"))
X(164, "Sistemas lineares", "<p>Sejam <em>c</em>, <em>p</em> e <em>s</em> as massas de camiseta, calça e sapato: 12<em>c</em> + 4<em>p</em> + 3<em>s</em> = 10 e 18<em>c</em> + 3<em>p</em> + 2<em>s</em> = 10. Fazendo 2 × (2ª) − (1ª): 24<em>c</em> + 2<em>p</em> + <em>s</em> = 10. Ou seja, duas calças e um sapato deixam espaço para exatamente <strong>24 camisetas</strong>. Alternativa <strong>B</strong>.</p><p>Não é preciso achar cada massa: a combinação das equações já dá a resposta.</p>",
  tags=["sistema linear", "combinação de equações"],
  enun=p(T(164, 0)) + tabela(["Viagem", "Camisetas", "Calças", "Sapatos"], [["I", "12", "4", "3"], ["II", "18", "3", "2"]]) + p(T(164, 2), T(164, 3)))
X(165, "Razão e proporção", "<p>Com 16 km/L, em 20 km o carro gasta 20/16 = 1,25 L. O novo motor economiza 0,1 L nesse trecho: 1,15 L. Desempenho: 20 ÷ 1,15 ≈ <strong>17,4 km/L</strong>. Alternativa <strong>D</strong>.</p><p>16,1 (B) somaria 0,1 ao desempenho, confundindo litros economizados com km/L.</p>",
  tags=["consumo", "razão"])
X(166, "Geometria plana", "<p>Dobrar comprimento e largura com a mesma altura: a área de cada parede é (lado) × altura, e cada lado dobrou, então a área das paredes <strong>dobra</strong>. O piso é comprimento × largura: 2 × 2 = <strong>4 vezes</strong>. Só o fornecedor II acertou. Alternativa <strong>B</strong>.</p><p>Quatro vezes para as paredes (C e D) aplicaria o fator de área a figuras que só mudaram em uma dimensão.</p>",
  tags=["área", "semelhança"],
  enun=p(T(166, 0), T(166, 1)) + LISTA(T(166, 2).split(" Analisando")[0])
       + p("Analisando" + T(166, 2).split(" Analisando")[1].split(" Qual dos")[0], "Qual dos" + T(166, 2).split(" Qual dos")[1]))
X(167, "Geometria espacial", "<p>Consumo em 7 dias: 100 × 120 × 7 = 84 000 L = 84 m<sup>3</sup>. Área da base (raio 2,5 m): 3 × 2,5<sup>2</sup> = 18,75 m<sup>2</sup>. Altura: 84 ÷ 18,75 = <strong>4,48 m</strong>. Alternativa <strong>D</strong>.</p><p>1,12 m (A) usaria o diâmetro como raio.</p>",
  tags=["volume do cilindro"], enun=p(T(167, 0), T(167, 1).replace("para p.", "para π.")))
X(168, "Geometria espacial", "<p>Ao montar o octaedro, as faces 1, 2 e 3 se fecham com a face cinza em torno de um mesmo vértice, e as faces vizinhas da cinza na planificação também se encostam nela. Seguindo as colagens, a face cinza fica com uma aresta em comum com 1, com 3 e com a face branca ao seu lado, e um vértice em comum com 2 e com as outras duas faces brancas. A única que não toca a face cinza é a <strong>4</strong>. Alternativa <strong>E</strong>.</p><p>No octaedro, cada face tem exatamente uma oposta, por isso as alternativas com mais de uma face (A e B) estão erradas.</p>",
  figs(("q168", "À esquerda, um octaedro regular. À direita, a planificação: uma tira de oito triângulos; na linha de cima, as faces 1, 2 e 3; abaixo da 2, a face 4; mais abaixo, outros triângulos, um deles cinza escuro, no canto inferior direito.")),
  ["octaedro", "planificação"], enun=p(T(168, 0)) + "[[fig:1]]" + p(T(168, 3)))
X(169, "Geometria plana", "<p>No triângulo equilátero, <em>h</em> = <em>L</em>√3/2, então <em>L</em> = 2<em>h</em>/√3 = 16/√3 = 16√3/3 ≈ 16 × 1,7/3 ≈ 9,06 cm. A barra tem o comprimento do perímetro: 3<em>L</em> = 16√3 ≈ 16 × 1,7 = 27,2 cm. Entre as alternativas, o valor mais próximo é <strong>27,18 cm</strong>, que é 3 × 9,06. Alternativa <strong>D</strong>.</p><p>9,07 (A) é só um lado, e 36,24 (E) soma quatro lados. 13,60 (B) é a metade do perímetro, e 20,40 (C) usa 12 no lugar de 16.</p>",
  figs(("q169", "Figura 1: um triângulo de percussão de metal, com uma abertura num canto e uma haste. Figura 2: um triângulo equilátero com a altura h = 8 cm indicada.")),
  ["triângulo equilátero", "perímetro"],
  enun=p(T(169, 0)) + "[[fig:1]]" + p(T(169, 4), "Considere 1,7 como valor aproximado para \\(\\sqrt{3}\\).", T(169, 6)))
X(170, "Geometria espacial", "<p>A caneca é um tronco de cone com raios <em>R</em> = 5 cm e <em>r</em> = 4 cm e altura 12 cm. V = (π<em>h</em>/3)(<em>R</em><sup>2</sup> + <em>Rr</em> + <em>r</em><sup>2</sup>) = (3 × 12/3)(25 + 20 + 16) = 12 × 61 = <strong>732 cm<sup>3</sup> = 732 mL</strong>. Alternativa <strong>C</strong>.</p><p>2 196 e 2 928 (D e E) usam os diâmetros no lugar dos raios.</p>",
  figs(("q170", "Caneca em forma de tronco de cone, com o diâmetro D do topo, o diâmetro d da base e a altura h indicados.")),
  ["tronco de cone", "volume"],
  enun=p(T(170, 0)) + "[[fig:1]]" + p(T(170, 2).replace("1 cm� = 1 mL", "1 cm<sup>3</sup> = 1 mL").replace("(D)", "(<em>D</em>)").replace("(d)", "(<em>d</em>)").replace("(h)", "(<em>h</em>)"),
                                       "Utilize 3 como aproximação para π.", T(170, 4)))
X(171, "Geometria plana", "<p>Com R$ 0,80 e R$ 0,01 por cm<sup>2</sup>, a área máxima é 80 cm<sup>2</sup>. Triângulo: 12<sup>2</sup> × 1,7/4 = 61,2; quadrado: 64; retângulo: 88 (passa do limite); hexágono: 6 × 6<sup>2</sup> × 1,7/4 = 91,8 (passa); círculo: 3 × 5<sup>2</sup> = <strong>75</strong>. Dentro do limite, a maior área é a do <strong>círculo</strong>. Alternativa <strong>E</strong>.</p><p>O hexágono e o retângulo (D e C) têm áreas maiores, mas custariam mais de R$ 0,80.</p>",
  tags=["áreas de figuras planas"],
  enun=p(T(171, 0)) + LISTA(T(171, 1)) + p(T(171, 2), "Use 3 como aproximação para π e use 1,7 como aproximação para \\(\\sqrt{3}\\).", T(171, 4)))
X(172, "Porcentagem", "<p>Fc máx. = 220 − 61 = 159 bpm. Faixa ideal: 65% de 159 ≈ 103,4 e 85% de 159 ≈ 135,2 bpm. Entre os trechos, ficam na faixa o <strong>forte no plano (120)</strong> e a <strong>subida moderada (130)</strong>; o leve no plano (90) fica abaixo e a subida forte (140), acima. Alternativa <strong>D</strong>.</p><p>Calcular a Fc máx. com 220 bpm sem descontar a idade faria a subida forte entrar na faixa (C).</p>",
  tags=["porcentagem", "intervalo"],
  enun=p(T(172, 0)) + tabela(["Trechos do percurso", "Frequências cardíacas máximas (bpm)"], [["Leve no plano", "90"], ["Forte no plano", "120"], ["Subida moderada", "130"], ["Subida forte", "140"]])
       + p(T(172, 2)) + '<p class="centro">Fc máx. = 220 – idade,</p>' + p(T(172, 3).replace("Fc máx. = 220 – idade, em", "em"), T(172, 4)))
X(173, "Inequações", "<p>Para fazer o menor número de lavagens, todas devem ser completas (R$ 35). 8 × 35 = 280, abaixo de 300; 9 × 35 = 315 ≥ 300. O mínimo é de <strong>9 lavagens</strong>. Alternativa <strong>C</strong>.</p><p>15 (D) é o mínimo só com lavagens simples (15 × 20 = 300).</p>",
  tags=["inequação", "valor mínimo"])
X(174, "Porcentagem", "<p>Opções: Farmácia 1 inteira, 45 + 40 + 50 = 135; Farmácia 3 inteira com 20%: 0,8 × 145 = 116; X e Y na Farmácia 2 com 20% (0,8 × 100 = 80) e Z onde é mais barato, na Farmácia 3 (35), sem o desconto de compra completa: 80 + 35 = <strong>115</strong>. É o menor valor. Alternativa <strong>C</strong>.</p><p>B daria 85 + 35 = 120 e D, 50 + 80 = 130 (sem desconto para X sozinho na Farmácia 2 e sem os três itens na Farmácia 3).</p>",
  tags=["desconto", "comparação de preços"],
  enun=p(T(174, 0)) + tabela(["", "X", "Y", "Z"], [["<strong>Farmácia 1</strong>", "R$ 45,00", "R$ 40,00", "R$ 50,00"], ["<strong>Farmácia 2</strong>", "R$ 50,00", "R$ 50,00", "R$ 40,00"],
                                                     ["<strong>Farmácia 3</strong>", "R$ 65,00", "R$ 45,00", "R$ 35,00"]])
       + p("Dessas farmácias, algumas oferecem descontos:") + LISTA(T(174, 2).split(":", 1)[1] + " " + T(174, 3)) + p(T(174, 4), T(174, 5)))
X(175, "Geometria espacial", "<p>A estrutura tem um cubo pequeno (hastes pretas) dentro de um cubo grande (hastes cinza claro), com cada vértice interno ligado ao vértice externo correspondente. Os dois cubos têm 6 faces cada: <strong>12 quadrados</strong>. Entre cada aresta do cubo interno e a aresta paralela do externo forma-se um trapézio com as bases paralelas e os lados (hastes de ligação) congruentes: um <strong>trapézio isósceles</strong> para cada uma das 12 arestas. Alternativa <strong>A</strong>.</p><p>24 trapézios (B) contariam cada um duas vezes; as faces não são retângulos nem paralelogramos (C e E), porque as bases têm tamanhos diferentes.</p>",
  figs(("q175", "Estrutura de hastes: um cubo grande de hastes cinza claro com um cubo menor de hastes pretas no centro; hastes cinza escuro ligam cada vértice do cubo menor ao vértice correspondente do cubo maior.")),
  ["poliedros", "trapézio isósceles"], enun=p(T(175, 0)) + "[[fig:1]]" + p(T(175, 2)))
X(176, "Sistemas de numeração", "<p>MCDLXIX = M (1 000) + CD (500 − 100 = 400) + L (50) + X (10) + IX (10 − 1 = 9) = 1 469. Em 2050, a cidade fará 2 050 − 1 469 = <strong>581 anos</strong>. Alternativa <strong>D</strong>.</p><p>Ler CD como 600 (somando em vez de subtrair) daria 1 669 e 381 anos (B).</p>",
  tags=["números romanos"],
  enun=p(T(176, 0).replace(" Quatro fundamentais", "</p><p>Quatro fundamentais").replace(" Três secundárias", "</p><p>Três secundárias"), "As regras para escrever números romanos são:")
       + OL("Não existe símbolo correspondente ao zero;", "Os símbolos fundamentais podem ser repetidos até três vezes e seus valores são adicionados. Exemplo: XXX = 30;",
            "Uma letra posta à esquerda de outra de maior valor indica subtração dos respectivos valores. Exemplo: IX = 10 − 1 = 9;",
            "Uma letra posta à direita de outra de maior valor indica adição dos respectivos valores. Exemplo: XI = 10 + 1 = 11.")
       + p(T(176, 5)))
X(177, "Sistemas de numeração", "<p>9 + 12 = 21 na base decimal. Em binário: 21 = 16 + 4 + 1 = 1 · 2<sup>4</sup> + 0 · 2<sup>3</sup> + 1 · 2<sup>2</sup> + 0 · 2<sup>1</sup> + 1 · 2<sup>0</sup> = <strong>10101</strong>. Somando direto: 1001 + 1100 = 10101. Alternativa <strong>D</strong>.</p><p>1101 (B) é 13 e 11001 (E) é 25.</p>",
  tags=["base binária"],
  enun=p(T(177, 0)) + tabela(["<em>a</em>", "<em>b</em>", "<em>a</em> + <em>b</em>"], [["0", "0", "0"], ["0", "1", "1"], ["1", "0", "1"], ["1", "1", "10"]])
       + p("Por exemplo, na base binária, a soma dos números 10 e 10 é 100, como apresentado:")
       + '<p class="centro">\\(\\begin{array}{r} 10 \\\\ +\\,10 \\\\ \\hline 100 \\end{array}\\)</p>'
       + p("Considerando as informações do texto, o resultado da adição 9 + 12 será representado, na base binária, por"))
X(178, "Grandezas e medidas", "<p>Área dos terrenos: 3 − 0,9 = 2,1 hectares = 21 000 m<sup>2</sup>, ou seja, 21 000 ÷ 300 = 70 terrenos. Os 20 primeiros rendem 20 × 20 000 = 400 000, e os outros 50 rendem 50 × 30 000 = 1 500 000. Total: <strong>R$ 1 900 000</strong>. Alternativa <strong>C</strong>.</p><p>2 200 000 (D) usaria os 3 hectares inteiros, sem descontar ruas e calçadas.</p>",
  tags=["hectare", "área"], enun=p(T(178, 0).replace(" m2", " m<sup>2</sup>")))
X(179, "Análise combinatória", "<p>A ordem não importa: escolher 2 de 6 tecidos é C(6, 2) = 6!/(4! 2!) e escolher 5 de 15 pedras é C(15, 5) = 15!/(10! 5!). As escolhas são independentes, então se multiplicam: \\(\\frac{6!}{4!\\,2!} \\cdot \\frac{15!}{10!\\,5!}\\). Alternativa <strong>A</strong>.</p><p>Somar (B) trataria as escolhas como alternativas excludentes; C e D omitem os fatoriais do denominador; E mistura tecidos e pedras num único grupo.</p>",
  tags=["combinação", "princípio multiplicativo"], enun=p(T(179, 0)),
  alts=FR("\\frac{6!}{4!\\,2!} \\cdot \\frac{15!}{10!\\,5!}", "\\frac{6!}{4!\\,2!} + \\frac{15!}{10!\\,5!}", "\\frac{6!}{2!} + \\frac{15!}{5!}", "\\frac{6!}{2!} \\cdot \\frac{15!}{5!}", "\\frac{21!}{7!\\,14!}"))
X(180, "Razão e proporção", "<p>Em 4 anos, o laboratório A custa 180 + 4 × 60 = 420 mil reais para 100 usuários: 4,20 mil por usuário. O B custa 120 + 4 × 16 = 184 mil para 80 usuários: 2,30 mil por usuário. Economia por usuário: 4,20 − 2,30 = <strong>1,90 mil reais</strong>. Alternativa <strong>B</strong>.</p><p>2,30 (C) é o custo por usuário do B, não a economia.</p>",
  tags=["custo por usuário"],
  enun=p(T(180, 0)) + p(T(180, 1), T(180, 2), T(180, 3)))

completar(Q, R)
