# Enem 2026, 2º dia, caderno AMARELO: Matemática (questões 136 a 180 do caderno; no site, 1 a 45, com numeroOriginal).
# Texto dos blocos do PDF (tools/enem_rascunho.py com ESPACOS=1); expoentes, índices e frações refeitos à mão (o PDF perde a formatação).
# Quadros das Q144, Q152, Q153 e Q165 em HTML. Q168 e Q175 com alternativas-imagem. Q153 anulada (caderno amarelo; 159 no azul).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar, tabela
from enem_aj import carregar_enem, enunciado_enem, paragrafos_enem

ID = "enem-2026-matematica"
META = {"id": ID, "banca": "Enem", "ano": 2026, "titulo": "Enem 2026: Matemática", "fonte": "Inep", "dataExame": "2026-11-15",
        "duracaoMinutos": 150, "area": "Matemática", "caderno": "amarelo", "dia": 2}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2026-dia2-amarelo")
Q = {}
P = lambda n: paragrafos_enem(D[n])
p = lambda *xs: "".join(f"<p>{x}</p>" for x in xs)
fonte = lambda x: f'<p class="fonte">{x}</p>'
fr = lambda a, b: f"<sup>{a}</sup>⁄<sub>{b}</sub>"


def bul(txt, corte=None):
    """'• a; • b; • c. Texto seguinte' -> <ul> + <p> (corte = início do texto que vem depois da lista)."""
    resto = ""
    if corte and corte in txt:
        txt, resto = txt.split(corte, 1)
        resto = corte + resto
    itens = [i.strip() for i in txt.split("•") if i.strip()]
    return "<ul>" + "".join(f"<li>{i}</li>" for i in itens) + "</ul>" + (p(resto) if resto else "")


def figs(*pares):
    return [{"arquivo": a, "alt": t} for a, t in pares]


def X(n, materia, assunto, expl, imagens=(), tags=(), enun=None, trocas=(), alts=None, anulacao=None):
    h = enun or enunciado_enem(D[n])
    for a, b in trocas:
        if a not in h: print(f"[troca não aplicada] Q{n}: {a[:50]!r} || {h[:220]!r}"); continue
        h = h.replace(a, b)
    Q[n - 135] = {"materia": "Matemática", "assunto": assunto, "area": "Matemática", "tags": list(tags), "numeroOriginal": n,
                  "enunciado": h, "alternativas": dict(D[n]["alternativas"], **(alts or {})), "imagens": list(imagens), "explicacao": expl}
    if anulacao: Q[n - 135]["anulacao"] = anulacao


M = "Matemática"
X(136, M, "Frações", "<p>O número misto 22 <sup>3</sup>⁄<sub>4</sub> significa 22 inteiros mais três quartos. Como 3 ÷ 4 = 0,75, fica 22 + 0,75 = <strong>22,75</strong>. Alternativa <strong>B</strong>.</p><p>Basta dividir 3 por 4; não é preciso converter polegada em outra unidade.</p>",
  figs(("q136", "Violão visto de frente, com o rastilho (perto da boca) e a pestana (no fim do braço) marcados; uma cota entre eles indica 22 3/4 polegadas.")),
  tags=["número misto", "representação decimal"])
X(137, M, "Porcentagem", "<p>No último ano, com F = <em>f</em>, M = 1,5<em>f</em> e o custo total era 2,5<em>f</em>. No ano atual, M = 0,7 × 1,5<em>f</em> = 1,05<em>f</em> e F = 1,45<em>f</em>; o custo total continua 1,05<em>f</em> + 1,45<em>f</em> = 2,5<em>f</em>. Como (M + F) não mudou, para V ficar igual (1 + L) também não muda: o lucro deve <strong>manter-se inalterado</strong>. Alternativa <strong>E</strong>.</p><p>Somar os percentuais (−30% + 45% = +15%) ignora que M e F têm pesos diferentes no custo.</p>",
  tags=["variação percentual", "média ponderada"])
X(138, M, "Porcentagem", "<p>Leite: 5% de 6,00 = 0,30. Margarina: 20% de 5,00 = 1,00. Refrigerante: 25% de 16,00 = 4,00. Total: 0,30 + 1,00 + 4,00 = <strong>R$ 5,30</strong>. Alternativa <strong>D</strong>.</p><p>Aplicar o percentual ao preço unitário do refrigerante (25% de 8,00) dá 3,30; somar os percentuais e aplicar ao total não faz sentido, pois cada produto tem sua alíquota.</p>",
  figs(("q138", "Cupom fiscal: Leite 1 L, 2 × 3,00 = 6,00 (5% imposto); Margarina 250 g, 1 × 5,00 = 5,00 (20% imposto); Refrigerante 2 L, 2 × 8,00 = 16,00 (25% imposto); Total R$ 27,00.")),
  tags=["porcentagem", "impostos"])
X(139, M, "Análise combinatória", "<p>Sejam T, S, F e X as quantidades de cápsulas tradicionais, suaves, fortes e extrafortes: T + S + F + X = 12, com T ≥ 2, S = F ≥ 1 e X ≥ 1. Então T + X = 12 − 2S, e para cada S contamos os pares (T, X) com T ≥ 2 e X ≥ 1:</p><ul><li>S = 1: T + X = 10 → T de 2 a 9: 8 kits;</li><li>S = 2: T + X = 8 → 6 kits;</li><li>S = 3: T + X = 6 → 4 kits;</li><li>S = 4: T + X = 4 → 2 kits;</li><li>S = 5: T + X = 2 → impossível.</li></ul><p>Total: 8 + 6 + 4 + 2 = <strong>20</strong>. Alternativa <strong>A</strong>.</p><p>Esquecer a condição S = F e contar todas as soluções leva a números bem maiores, como 286 ou 455.</p>",
  tags=["soluções inteiras", "contagem"],
  enun=p(P(139)[0][1]) + bul(P(139)[1][1]) + p(P(139)[2][1]))
X(140, M, "Probabilidade", "<p>O grupo O é o que sobra: 100% − 25% − 25% − 30% = 20%. Receptor universal (AB+): 0,30 × 0,6 = 0,18. Doador universal (O−): 0,20 × 0,4 = 0,08. Os eventos são excludentes: 0,18 + 0,08 = <strong>0,26</strong>. Alternativa <strong>B</strong>.</p><p>Multiplicar as duas probabilidades (0,18 × 0,08 = 0,0144, E) seria o “e”, não o “ou”.</p>",
  tags=["probabilidade da união", "grupos sanguíneos"],
  enun=p(P(140)[0][1]) + bul(P(140)[1][1], "Além dos antígenos") + fonte(P(140)[2][1]) + p(*P(140)[3][1].split(" A probabilidade", 1)[:1], "A probabilidade" + P(140)[3][1].split(" A probabilidade", 1)[1]),
  trocas=[("“-”", "“−”"), ("AB-.", "AB−."), ("e O-, denominado", "e O−, denominado")])
X(141, M, "Grandezas e medidas", "<p>Mb/s é megabit por segundo: uma quantidade de dados dividida por um intervalo de tempo. A razão é <strong>volume de dados ÷ tempo</strong>. Alternativa <strong>A</strong>.</p><p>A unidade lembra km/h, mas não envolve distância nem velocidade (D e E); C é a razão invertida.</p>",
  tags=["unidades de medida", "taxa de transferência"],
  alts={"A": fr("volume de dados", "tempo"), "B": fr("distância", "volume de dados"), "C": fr("tempo", "volume de dados"), "D": fr("velocidade", "distância"), "E": fr("distância", "tempo")})
X(142, M, "Geometria espacial", "<p>Uma pirâmide de base com <em>n</em> lados tem 2<em>n</em> arestas: 2<em>n</em> = 10 dá <em>n</em> = 5 (base pentagonal). A pirâmide tem 5 faces laterais + 1 base = 6 faces; o prisma pentagonal tem 5 laterais + 2 bases = 7 faces. Ao colar, a base da pirâmide e uma base do prisma ficam dentro do sólido e deixam de ser faces: 6 + 7 − 2 = <strong>11</strong>. Alternativa <strong>A</strong>.</p><p>Somar 6 + 7 sem descontar as bases coladas dá 13 (B).</p>",
  tags=["poliedros", "faces e arestas"])
X(143, M, "Geometria analítica", "<p>C(7; 3) e D(5; 7) são vértices consecutivos: o lado DC = (2; −4) mede √20. Girando esse vetor 90°, chega-se aos outros vértices: A = (1; 5) e B = (3; 1). O menor círculo que contém o quadrado é o circunscrito: centro no ponto médio da diagonal AC, (4; 4), e raio igual à metade da diagonal, com <em>r</em>² = (7 − 4)² + (3 − 4)² = 10.</p><p>(<em>x</em> − 4)² + (<em>y</em> − 4)² = 10 → <strong><em>x</em>² + <em>y</em>² − 8<em>x</em> − 8<em>y</em> + 22 = 0</strong>. Alternativa <strong>B</strong>.</p><p>A alternativa E traz a mesma conta com os sinais trocados (centro em (−4; −4)); C usa o ponto médio de CD como se fosse o centro, com outra conta.</p>",
  figs(("q143", "Plano cartesiano com um quadrado verde ABCD inclinado: A à esquerda, B embaixo, C(7; 3) à direita e D(5; 7) em cima. Uma rosa dos ventos indica N para cima e L para a direita.")),
  tags=["equação da circunferência", "circunferência circunscrita"],
  alts={"A": "<em>x</em>² + <em>y</em>² − 10 = 0", "B": "<em>x</em>² + <em>y</em>² − 8<em>x</em> − 8<em>y</em> + 22 = 0", "C": "<em>x</em>² + <em>y</em>² − 16<em>x</em> − 12<em>y</em> + 90 = 0",
        "D": "<em>x</em>² + <em>y</em>² − 12<em>x</em> − 10<em>y</em> + 56 = 0", "E": "<em>x</em>² + <em>y</em>² + 8<em>x</em> + 8<em>y</em> + 32 − 10 = 0"})
X(144, M, "Estatística", "<p>Em ordem: 44, 44, 48, 52, 56, 62. Com seis valores, a mediana é a média dos dois centrais: (48 + 52) ÷ 2 = <strong>50</strong>. Alternativa <strong>C</strong>.</p><p>44 (A) é a moda; tomar a média dos centrais sem ordenar (44 e 48, de março e abril) dá 46 (B).</p>",
  tags=["mediana"],
  enun=p(P(144)[0][1]) + tabela(["Mês", "Quantidade de tablets vendidos"], [["Janeiro", "44"], ["Fevereiro", "56"], ["Março", "44"], ["Abril", "48"], ["Maio", "62"], ["Junho", "52"]]) + p(P(144)[2][1]))
X(145, M, "Áreas", "<p>A bancada tem 200 × 60 = 12 000 cm². O retângulo sombreado deve ter 35% disso: 4 200 cm². Como a altura dele é 60 cm, a largura passa a ser 4 200 ÷ 60 = 70 cm. Hoje é 5 cm: o aumento é 70 − 5 = <strong>65 cm</strong>. Alternativa <strong>D</strong>.</p><p>70 (E) é a nova distância, não o aumento.</p>",
  figs(("q145", "Bancada retangular de 200 cm por 60 cm, vista de cima: à esquerda o cooktop com cinco bocas, à direita a pia com a torneira. Entre os dois, um retângulo cinza de 5 cm de largura, que ocupa toda a profundidade da bancada.")),
  tags=["área do retângulo", "porcentagem"])
X(146, M, "Leitura de gráficos", "<p>A curva vermelha (T<sub>máx</sub>) atinge o ponto mais alto, perto de 19 °C, no dia <strong>4</strong>. A curva azul (T<sub>mín</sub>) atinge o ponto mais baixo, perto de 1 °C, no dia <strong>2</strong>. Alternativa <strong>E</strong>.</p><p>O dia 5 é o pico da mínima, não o vale; e o dia 10 é o vale da máxima.</p>",
  figs(("q146", "Gráfico de linhas da temperatura (°C) nos dias 1 a 15. A máxima (vermelha) fica entre 11 e 15 °C, com pico de quase 19 °C no dia 4 e outro de quase 18 °C no dia 14. A mínima (azul) cai para cerca de 1 °C no dia 2, sobe a quase 11 °C no dia 5 e volta a valores baixos, perto de 1,5 °C no dia 11.")),
  tags=["gráfico de linhas"], trocas=[("(Tmáx)", "(T<sub>máx</sub>)"), ("(Tmín)", "(T<sub>mín</sub>)")])
X(147, M, "Grandezas e medidas", "<p>7,5 dL = 0,75 L por dia. Em 30 dias: 0,75 × 30 = 22,5 L. Custo: 22,5 × 1,98 = <strong>R$ 44,55</strong>. Alternativa <strong>C</strong>.</p><p>Ler 7,5 dL como 7,5 L leva a 445,50 (E); como 0,075 L, a 4,46.</p>",
  tags=["conversão de unidades", "decilitro"])
X(148, M, "Probabilidade", "<p>Os centros formam um quadrado de lado 20 cm. A região verde é esse quadrado menos quatro quartos de círculo: 400 − 3 × 100 = 100 cm². O tabuleiro tem 4 × 3 × 10² + 100 = 1 300 cm².</p><p>O disco cai inteiro sobre um círculo quando seu centro está a menos de 10 − <em>r</em> do centro desse círculo. A área favorável é 4 × 3 × (10 − <em>r</em>)². Queremos 12(10 − <em>r</em>)² ÷ 1 300 &lt; 0,6, isto é, (10 − <em>r</em>)² &lt; 65, ou 10 − <em>r</em> &lt; 8,06, ou <em>r</em> &gt; 1,94. O menor inteiro é <strong>2</strong>. Alternativa <strong>A</strong>.</p>",
  figs(("q148", "Tabuleiro formado por quatro círculos lilás de raio 10 cm, tangentes dois a dois, com centros nos vértices de um quadrado; a região verde fica no meio, entre os quatro. Ao lado, um disco laranja de raio r.")),
  tags=["probabilidade geométrica", "área do círculo"])
X(149, M, "Razão e proporção", "<p>Carro I: cidade 1 200 ÷ 48 × 20 = 500 MJ; estrada 1 800 ÷ 32 × 20 = 1 125 MJ; total 1 625 MJ. Carro II: cidade 1 200 ÷ 50 × 25 = 600 MJ; estrada 1 800 ÷ 45 × 25 = 1 000 MJ; total <strong>1 600 MJ</strong>. O carro II gasta menos. Alternativa <strong>E</strong>.</p><p>O carro I é mais econômico na cidade, mas a maior parte do percurso é estrada, onde o II ganha com folga.</p>",
  tags=["regra de três", "consumo de energia"],
  enun=p(P(149)[0][1]) + bul(P(149)[1][1]) + p(P(149)[2][1], P(149)[3][1]))
X(150, M, "Razão e proporção", "<p>Tempo = distância ÷ velocidade. Trajeto I: 100 ÷ 50 = 2 h. Trajeto II: 120 ÷ 80 = 1,5 h = <strong>90 minutos</strong>. O II é mais rápido. Alternativa <strong>E</strong>.</p><p>O trajeto mais curto (I) não é o mais rápido, porque a velocidade média nele é bem menor.</p>",
  tags=["velocidade média"],
  enun=p(P(150)[0][1]) + bul(P(150)[1][1]) + p(P(150)[2][1], P(150)[3][1]))
X(151, M, "Razão e proporção", "<p>A parte de cada sócio é proporcional a investimento × tempo: 5 000 × 6 = 30 000; 4 000 × 18 = 72 000; 6 000 × 18 = 108 000. Soma: 210 000. O sócio que saiu recebe 30 000/210 000 de 21 000 = <strong>R$ 3 000,00</strong>. Alternativa <strong>C</strong>.</p><p>Dividir só pelo investimento, sem o tempo, daria 7 000,00 (E).</p>",
  tags=["divisão proporcional"])
TAB152 = tabela(["Nível de segurança", "D<sub>1</sub>", "D<sub>2</sub>"],
                [["1", "D<sub>1</sub> &lt; 23", "D<sub>2</sub> &lt; 23"], ["2", "23 ≤ D<sub>1</sub> &lt; 25", "D<sub>2</sub> &lt; 23"], ["3", "23 ≤ D<sub>1</sub> &lt; 25", "23 ≤ D<sub>2</sub> &lt; 25"],
                 ["4", "D<sub>1</sub> ≥ 25", "23 ≤ D<sub>2</sub> &lt; 25"], ["5", "D<sub>1</sub> ≥ 25", "D<sub>2</sub> ≥ 25"]])
X(152, M, "Função quadrática", "<p>O vértice de <em>y</em> = −0,24<em>x</em>² + 4,8<em>x</em> está em <em>x</em> = −4,8 ÷ (2 × (−0,24)) = 10, com <em>y</em> = −24 + 48 = 24. D<sub>1</sub> = √(10² + 24²) = √676 = 26.</p><p>No ponto de explosão, <em>x</em> = <em>k</em> = 15 e <em>y</em> = −0,24 × 225 + 72 = 18. D<sub>2</sub> = √(15² + 18²) = √549 ≈ 23,4.</p><p>D<sub>1</sub> ≥ 25 e 23 ≤ D<sub>2</sub> &lt; 25: nível <strong>4</strong>. Alternativa <strong>D</strong>.</p><p>Usar a altura do vértice (24) como D<sub>1</sub> leva ao nível 3 (C): D<sub>1</sub> é a distância em linha reta, não a altura.</p>",
  figs(("q152", "Plano cartesiano com a trajetória parabólica vermelha do projétil, saindo da origem (ponto de lançamento), passando pelo ponto de altura máxima e terminando no ponto de explosão, de abscissa k. Segmentos azuis ligam a origem ao ponto de altura máxima (D1) e ao ponto de explosão (D2).")),
  tags=["vértice da parábola", "distância entre pontos"],
  enun=p(P(152)[0][1]) + "[[fig:1]]" + p(P(152)[2][1]) + TAB152 + p("Em um teste de segurança, a trajetória do projétil lançado por um sinalizador foi modelada pela função <em>y</em> = −0,24<em>x</em>² + 4,8<em>x</em> e apurou-se que <em>k</em> = 15.", P(152)[5][1]),
  trocas=[("D1 (distância", "D<sub>1</sub> (distância"), ("D2 (distância", "D<sub>2</sub> (distância"), ("valores apurados para D1 e D2", "valores apurados para D<sub>1</sub> e D<sub>2</sub>")])
X(153, M, "Estatística", "<p>Pela análise do Treineiros, a conta esperada seria esta. Média de gols marcados 25 com 6 times: total 150, então 31 + 27 + 34 + 22 + 26 + <em>x</em> = 150 e <em>x</em> = 10. Gols sofridos sem <em>y</em>, em ordem: 21, 22, 23, 26, 28. Para a mediana dos seis valores ser 24, <em>y</em> tem de ficar entre 23 e 26 e (23 + <em>y</em>) ÷ 2 = 24, o que dá <em>y</em> = 25. Então <em>x</em> + <em>y</em> = <strong>35</strong>, alternativa <strong>C</strong>, se a questão não tivesse sido anulada.</p><p>O problema: num campeonato disputado só entre esses times, todo gol marcado por um é sofrido por outro, então os dois totais têm de ser iguais. Com esses valores, foram 150 gols marcados e 165 sofridos.</p>",
  tags=["média", "mediana"],
  enun=p(P(153)[0][1]) + tabela(["Posição", "Time", "Gols marcados", "Gols sofridos"],
                                [["1ª", "I", "31", "23"], ["2ª", "II", "27", "21"], ["3ª", "III", "34", "<em>y</em>"], ["4ª", "IV", "22", "26"], ["5ª", "V", "26", "22"], ["6ª", "VI", "<em>x</em>", "28"]])
       + p(P(153)[2][1], "A soma <em>x</em> + <em>y</em> é igual a"),
  anulacao={"fonte": "oficial", "motivo": "<p>O Inep anulou esta questão (159 no caderno azul) no gabarito oficial, sem publicar o motivo. A explicação mais citada, apontada por cursinhos como o Objetivo, é uma inconsistência nos dados: num campeonato entre esses seis times, o total de gols marcados tem de ser igual ao de gols sofridos, mas, com a média e a mediana do enunciado, dão 150 e 165.</p>"})
X(154, M, "Matemática financeira", "<p>No dia da compra, o saldo é R$ 90 000,00.</p><ul><li>À vista: sobram 1 000,00, que rendem 2 meses: 1 000 × 1,01² = <strong>1 020,10</strong>.</li><li>Parcelado: paga 30 000 e sobram 60 000; após 1 mês, 60 600 − 30 000 = 30 600; após 2 meses, 30 906 − 30 000 = 906,00.</li></ul><p>O à vista deixa o maior saldo: R$ 1 020,10. Alternativa <strong>C</strong>.</p><p>1 000,00 (A) esquece o rendimento; 1 010,00 (B) conta só um mês.</p>",
  tags=["juros compostos", "comparação de pagamentos"],
  enun=p(P(154)[0][1]) + bul(P(154)[1][1]) + p(P(154)[2][1], P(154)[3][1]))
X(155, M, "Função exponencial", "<p>Ao sair da concessionária, o carro já vale 80 000 × 0,9 = 72 000. Depois, perde 12% ao ano, ou seja, a cada ano vale 88% do ano anterior: <strong>V = 72 000 · 0,88<sup><em>t</em></sup></strong>. Alternativa <strong>A</strong>.</p><p>Usar 0,12<sup><em>t</em></sup> (B) multiplicaria pelo que se perde, não pelo que sobra; somar 10% + 12% (D) mistura uma perda única com a perda anual.</p>",
  tags=["depreciação", "decrescimento exponencial"],
  alts={"A": "V = 72 000 · 0,88<sup><em>t</em></sup>", "B": "V = 72 000 · 0,12<sup><em>t</em></sup>", "C": "V = 80 000 · 0,78<sup><em>t</em></sup>", "D": "V = 80 000 · 0,22<sup><em>t</em></sup>", "E": "V = 80 000 · 0,12<sup><em>t</em></sup>"})
X(156, M, "Notação científica", "<p>1 micrômetro = 10<sup>−6</sup> m = 10<sup>−3</sup> mm. Então 0,75 µm = 0,75 × 10<sup>−3</sup> mm = <strong>7,5 × 10<sup>−4</sup> mm</strong>. Alternativa <strong>C</strong>.</p><p>7,5 × 10<sup>−7</sup> (E) é a medida em metro, não em milímetro.</p>",
  tags=["conversão de unidades", "potências de 10"],
  alts={k: f"7,5 × 10<sup>−{e}</sup>" for k, e in zip("ABCDE", (1, 2, 4, 5, 7))})
X(157, M, "Potenciação", "<p>Um trilhão é 10<sup>12</sup> = 1 000 000 000 000. Um trilionésimo é 1/10<sup>12</sup>: o denominador tem <strong>12 zeros</strong> depois do 1. Alternativa <strong>C</strong>.</p><p>9 zeros (A) seria um bilionésimo.</p>",
  tags=["potências de 10", "escala numérica"])
X(158, M, "Matrizes", "<p>A coluna <em>j</em> traz as notas dadas pelo diretor D<sub><em>j</em></sub>. Seguindo a ordem:</p><ul><li>D<sub>1</sub> (coluna 3, 2, 4, 1, 0): maior nota para C<sub>3</sub>;</li><li>D<sub>2</sub>, entre C<sub>1</sub>, C<sub>2</sub>, C<sub>4</sub> e C<sub>5</sub> (4, 3, 2, 2): escolhe C<sub>1</sub>;</li><li>D<sub>3</sub>, entre C<sub>2</sub>, C<sub>4</sub> e C<sub>5</sub> (2, 2, 3): escolhe C<sub>5</sub>;</li><li>D<sub>4</sub>, entre C<sub>2</sub> e C<sub>4</sub> (4, 2): escolhe C<sub>2</sub>;</li><li>D<sub>5</sub> fica com quem sobrou: <strong>C<sub>4</sub></strong>.</li></ul><p>Alternativa <strong>D</strong>. Olhar a coluna 5 sem tirar os já escolhidos levaria a C<sub>5</sub> (nota 5).</p>",
  figs(("q158", "Tabela de notas com 5 linhas e 5 colunas. Linha 1: 3, 4, 0, 5, 1. Linha 2: 2, 3, 2, 4, 3. Linha 3: 4, 3, 1, 0, 2. Linha 4: 1, 2, 2, 2, 4. Linha 5: 0, 2, 3, 3, 5. A segunda linha está destacada como “notas recebidas pelo candidato C2”, a quarta coluna como “notas atribuídas pelo diretor D4”, e o 4 no cruzamento das duas está circulado.")),
  tags=["leitura de matriz", "algoritmo de escolha"],
  trocas=[("C1, C2, C3, C4 e C5", "C<sub>1</sub>, C<sub>2</sub>, C<sub>3</sub>, C<sub>4</sub> e C<sub>5</sub>"), ("D1, D2, D3, D4 e D5", "D<sub>1</sub>, D<sub>2</sub>, D<sub>3</sub>, D<sub>4</sub> e D<sub>5</sub>"),
          ("candidato Ci, atribuída pelo diretor Dj", "candidato C<sub><em>i</em></sub>, atribuída pelo diretor D<sub><em>j</em></sub>"), ("candidato C2 pelo diretor D4", "candidato C<sub>2</sub> pelo diretor D<sub>4</sub>"),
          ("o diretor D1 escolherá", "o diretor D<sub>1</sub> escolherá"), ("o diretor D2 escolherá", "o diretor D<sub>2</sub> escolherá"), ("pelo diretor D5 é", "pelo diretor D<sub>5</sub> é"),
          ("maior nota; e assim sucessivamente. O candidato", "maior nota; e assim sucessivamente.</p><p>O candidato")],
  alts={k: f"C<sub>{i}</sub>." for i, k in enumerate("ABCDE", 1)})
X(159, M, "Expressões algébricas", "<p>São <em>x</em> blusas e 1 800 − <em>x</em> vestidos. Blusas, todas em dinheiro: 10<em>x</em>. Vestidos: um terço em dinheiro (lucro 30) e dois terços no cartão (lucro 10% menor, 27). Lucro médio por vestido: (30 + 2 × 27) ÷ 3 = 28. Lucro total: 10<em>x</em> + 28(1 800 − <em>x</em>) = <strong>50 400 − 18<em>x</em></strong>. Alternativa <strong>C</strong>.</p><p>Supor todos os vestidos no cartão dá 48 600 − 17<em>x</em>; todos em dinheiro, 54 000 − 20<em>x</em> (E).</p>",
  tags=["expressão algébrica", "porcentagem"],
  alts={"A": "21 600 − 2<em>x</em>", "B": "48 600 − 18<em>x</em>", "C": "50 400 − 18<em>x</em>", "D": "52 200 − 19<em>x</em>", "E": "54 000 − 20<em>x</em>"})
X(160, M, "Semelhança", "<p>O canteiro I tem lado maior 10 m e área 80 m², então o menor mede 8 m: a razão entre os lados de cada retângulo é 10 : 8 = 5 : 4.</p><p>O triângulo é retângulo, com hipotenusa 10 (lado do canteiro I) e um cateto 8 (lado maior do canteiro II); o outro cateto mede √(100 − 64) = 6, e é o lado maior do canteiro III.</p><p>Canteiro II: 8 × 6,4 = 51,2 m². Canteiro III: 6 × 4,8 = 28,8 m². Diferença: <strong>22,40 m²</strong>. Alternativa <strong>D</strong>.</p>",
  figs(("q160", "Triângulo retângulo laranja cercado por três retângulos: o canteiro I, verde-claro e inclinado, apoiado na hipotenusa, com o lado maior de 10 m; o canteiro II, amarelo, embaixo, com o lado maior de 8 m; e o canteiro III, verde-escuro, à esquerda. O ângulo reto fica no canto entre os canteiros II e III.")),
  tags=["retângulos semelhantes", "teorema de Pitágoras"], trocas=[("80 m2", "80 m²")])
X(161, M, "Estatística", "<p>Como todas têm quatro semestres, a menor média é a da menor soma: I 25; II 25; III 26; <strong>IV 24</strong>; V 26. Criança IV. Alternativa <strong>D</strong>.</p><p>Comparar só o 1º semestre levaria à criança I, e olhar o último semestre, à IV ou à V empatadas: a média exige somar tudo.</p>",
  tags=["média aritmética"],
  enun=p(P(161)[0][1]) + bul(P(161)[1][1], "A diretora fará") + p(P(161)[2][1]))
X(162, M, "Função quadrática", "<p>Com <em>f</em>(<em>t</em>) = <em>at</em>² + <em>bt</em> + <em>c</em> e os pontos (0; 30), (1; 31,5) e (2; 32): <em>c</em> = 30; <em>a</em> + <em>b</em> = 1,5; 4<em>a</em> + 2<em>b</em> = 2. Daí <em>a</em> = −0,5 e <em>b</em> = 2.</p><p>2026 corresponde a <em>t</em> = 5: <em>f</em>(5) = −12,5 + 10 + 30 = <strong>27,5</strong>. Alternativa <strong>B</strong>.</p><p>Quem prolonga a tendência de alta, sem perceber que a parábola é côncava para baixo, marca 33,5 ou 35,0.</p>",
  figs(("q162", "Gráfico com o eixo t (ano) de 0 a 5 e o eixo CTB (%) de 29,5 a 32,5. Três pontos: (0; 30,0), (1; 31,5) e (2; 32,0).")),
  tags=["interpolação", "função quadrática por três pontos"])
X(163, M, "Sistemas lineares", "<p>Com <em>c</em> e <em>f</em> os preços: 6<em>c</em> + 15<em>f</em> = 780 e 5<em>c</em> + 8<em>f</em> = 470. Da primeira, 2<em>c</em> + 5<em>f</em> = 260. Resolvendo, <em>f</em> = 40 e <em>c</em> = 30. José: 4 × 30 = 120 em calabresa; sobram 400, que são 10 pizzas de frango. Total: 4 + 10 = <strong>14</strong>. Alternativa <strong>D</strong>.</p><p>10 (só as de frango) não está entre as alternativas; 13 e 18 vêm de erros nos preços.</p>",
  tags=["sistema de equações"])
X(164, M, "Geometria plana", "<p>Use as coordenadas do centro da bola: ela se move num quadrado de 3 a 203 cm (206 − 3). A bola branca está em (103; 143), na mesma vertical da amarela, que está encostada no lado de cima, em (103; 203).</p><p>Pelo princípio da reflexão, “desdobra-se” a mesa: refletindo a amarela no lado esquerdo (<em>x</em> = 3), depois no de baixo (<em>y</em> = 3) e depois no da direita (<em>x</em> = 203), ela vai para (503; −197). A trajetória vira uma reta da branca até esse ponto. Ela cruza <em>x</em> = 203 em um quarto do caminho horizontal (100 de 400), na altura 143 − ¼ × 340 = <strong>58 cm</strong>. Alternativa <strong>C</strong>.</p>",
  figs(("q164", "Mesa quadrada de bilhar com 206 cm de lado. A bola branca está a 63 cm da borda de cima e na mesma vertical da bola amarela, que fica junto à borda de cima, a 103 cm da borda direita. A trajetória pontilhada vai da branca à borda direita, numa altura d acima da borda de baixo, depois à borda de baixo, depois à esquerda e por fim à amarela, com ângulos iguais (α, β, γ) em cada rebatida.")),
  tags=["reflexão", "semelhança de triângulos"])
X(165, M, "Geometria espacial", "<p>O cilindro interno tem raio 10 cm e altura 100 cm. O volume da manta é π[(10 + <em>e</em>)² − 10²] × 100.</p><ul><li>Material I (<em>e</em> = 1): 3 × 21 × 100 = 6 300 cm³ → 6,3 × 26 = R$ 163,80.</li><li>Material II (<em>e</em> = 2): 3 × 44 × 100 = 13 200 cm³ → 13,2 × 12 = R$ 158,40.</li></ul><p>O II sai R$ 5,40 mais barato. Alternativa <strong>E</strong>.</p><p>Comparar só espessura ou só preço por volume (A e C) ignora que a manta mais grossa usa mais material.</p>",
  figs(("q165-1", "Cilindro azul de raio 10 cm e altura 100 cm, envolvido por um cilindro cinza translúcido de mesma altura; a diferença entre os raios é indicada como a espessura da manta.")),
  tags=["volume do cilindro", "coroa circular"],
  enun=p(P(165)[0][1]) + "[[fig:1]]" + p(P(165)[2][1]) + tabela(["Material", "Espessura da manta (cm)", "Preço (a cada 1 000 cm³)"], [["I", "1,0", "R$ 26,00"], ["II", "2,0", "R$ 12,00"]]) + p(P(165)[5][1], P(165)[6][1]))
X(166, M, "Escalas", "<p>Cada quadradinho tem 10 cm no desenho; na escala 1 : 80, isso é 800 cm = 8 m no real. O refeitório ocupa 1 × 2 quadradinhos, ou 8 m × 16 m = 128 m². Reduzido em 25%: 0,75 × 128 = <strong>96 m²</strong>. Alternativa <strong>D</strong>.</p><p>Aplicar a redução de 25% duas vezes (96 × 0,75 = 72, E) confunde a área atual com a nova.</p>",
  figs(("q166", "Planta baixa de uma escola sobre malha quadriculada, com biblioteca, auditório, centro de convivência, salas de aula, bosque e quadra. O refeitório, em amarelo, ocupa uma faixa vertical de 1 quadradinho de largura por 2 de altura. Indicação: cada quadradinho tem 10 cm; escala 1 : 80.")),
  tags=["escala", "área"])
X(167, M, "Probabilidade", "<p>A data tem o mesmo registro nos dois formatos quando DD = MM: 01/01, 02/02, …, 12/12, ou seja, 12 datas. Em um ano não bissexto há 365 datas: probabilidade <strong>12/365</strong>. Alternativa <strong>A</strong>.</p><p>144/365 (C) conta as datas que <em>podem</em> ser lidas nos dois formatos (dia até 12), não as que ficam iguais.</p>",
  tags=["probabilidade clássica", "datas"],
  alts={"A": fr(12, 365), "B": fr(30, 365), "C": fr(144, 365), "D": fr(1, 12), "E": fr(12, 30)})
X(168, M, "Geometria espacial", "<p>Projetar sobre o plano α é olhar o empilhamento de frente para α: cada bloco vira um retângulo, e as faces de mesma cor no mesmo plano se alinham. Reconstruindo de baixo para cima a silhueta (os blocos que avançam e recuam em cada camada), a figura correta é a última da coluna da direita. Alternativa <strong>E</strong>.</p><p>As outras deslocam os recuos de lado ou trocam a ordem das camadas.</p>",
  figs(("q168-1", "Pilha de blocos retangulares iguais em várias camadas, alternando a direção, sobre o plano β (chão azul) e encostada ao plano α (parede azul-clara). As faces verticais têm cores diferentes conforme o plano em que estão."),
       ("q168-2", "Alternativa A: silhueta cinza com um bloco estreito no alto, uma faixa larga com recortes dos dois lados no meio e uma base larga."),
       ("q168-5", "Alternativa B: silhueta cinza com recortes do lado direito, um no meio e outro embaixo."),
       ("q168-6", "Alternativa C: silhueta cinza com um recorte à esquerda no alto e uma abertura embaixo, entre dois pés."),
       ("q168-3", "Alternativa D: silhueta cinza com um bloco largo no alto, deslocado para a direita, um degrau à esquerda e uma base com uma abertura embaixo."),
       ("q168-4", "Alternativa E: silhueta cinza com um bloco no alto, recortes dos dois lados no meio e uma base com uma abertura embaixo, entre dois pés.")),
  tags=["projeção ortogonal", "vistas"], alts={k: f"[[fig:{i}]]" for i, k in enumerate("ABCDE", 2)},
  trocas=[("plano a,", "plano α,"), ("plano b da base", "plano β da base"), ("sobre o plano a é", "sobre o plano α é")])
X(169, M, "Estatística", "<p>A alternativa correta da questão 1 é a D: é a escolhida pelos grupos de nota alta. Os percentuais de cada grupo somam 100%, então: N4 marcou D em 100 − (0 + 5 + 20 + 15) = 60%; N5 marcou D em 100%.</p><p>Acertos ponderados pelo tamanho de cada grupo: N0 0% × 20% = 0; N1 10% × 15% = 1,5; N2 20% × 15% = 3; N3 25% × 30% = 7,5; N4 60% × 10% = 6; N5 100% × 10% = 10. Total: <strong>28%</strong>. Alternativa <strong>E</strong>.</p><p>Fazer a média simples dos percentuais de D, sem ponderar pelos grupos, dá outro resultado.</p>",
  figs(("q169-1", "Gráfico de linhas com os grupos N0 a N5 no eixo horizontal e porcentagens de 0% a 35%. Alternativa A: 30, 20, 15, 20, 0, 0. B: 20, 25, 20, 15, 5, 0. C: 25, 30, 25, 30, 20, 0. D: 0, 10, 20, 25 (sem dados em N4 e N5). E: 25, 15, 20, 10, 15, 0."),
       ("q169-2", "Gráfico de semicírculo com a distribuição dos candidatos: N0 20%, N1 15%, N2 15%, N3 30%, N4 10%, N5 10%.")),
  tags=["média ponderada", "leitura de gráficos"],
  enun=p(P(169)[0][1]) + bul(P(169)[1][1], "Todos os candidatos") + p(P(169)[2][1]) + f"<p><strong>{P(169)[3][1]}</strong></p>[[fig:1]]" + p(P(169)[5][1]) + f"<p><strong>{P(169)[6][1]}</strong></p>[[fig:2]]" + p(P(169)[8][1]),
  )
X(170, M, "Estatística", "<p>Pelo critério de Fry, ganha quem tem notas mais dispersas. O usuário 2 recebeu metade das notas −1 e metade 1: todas a distância 1 da média (0), desvio padrão 1, o máximo possível na escala de −1 a 1. Alternativa <strong>B</strong>.</p><p>O usuário 1 (todas as notas 0) tem desvio zero; o 3 (notas uniformes) e o 5 (concentradas nos extremos, mas com notas no meio) ficam abaixo de 1.</p>",
  figs(("q170-1", "Quadro de notas de −1 a 1 com emojis: −1 “se te acharem muito desinteressante”, −0,5 “desinteressante”, 0 “indiferente”, 0,5 “interessante” e 1 “muito interessante”."),
       ("q170-2", "Cinco gráficos de barras de frequência das notas −1, −0,5, 0, 0,5 e 1. Usuário 1: frequência 1,0 na nota 0. Usuário 2: 0,5 em −1 e 0,5 em 1. Usuário 3: 0,2 em cada nota. Usuário 4: 0,1; 0,2; 0,4; 0,2; 0,1. Usuário 5: 0,3; 0,15; 0,1; 0,15; 0,3.")),
  tags=["desvio padrão", "dispersão"])
X(171, M, "Geometria plana", "<p>O tampo é um triângulo de Reuleaux de largura 1,20 m; com 20 cm de sobra em todo o contorno, a toalha precisa cobrir uma figura de largura constante 1,60 m.</p><ul><li>Círculo: o mais afastado do centro são os vértices, a 1,2/√3 ≈ 1,2 × 1,7 ÷ 3 = 0,68 m; com a sobra, raio 0,88 m e diâmetro 1,76 m. O modelo II serve; o I não.</li><li>Quadrado: uma figura de largura constante 1,60 m cabe num quadrado de lado 1,60 m, então o III também serve.</li><li>Triângulo de lado 1,60 m: sua altura é só 1,36 m, não cabe.</li></ul><p>Entre II (π × 0,88² ≈ 2,43 m²) e III (2,56 m²), o círculo tem menor área. Alternativa <strong>B</strong>.</p>",
  figs(("q171", "Região amarela em forma de triângulo de lados curvos com vértices A, B e C, formada pela interseção de três círculos tracejados de mesmo raio, cada um centrado em um dos vértices.")),
  tags=["triângulo de Reuleaux", "área do círculo"],
  enun=p(P(171)[0][1]) + "[[fig:1]]" + p(P(171)[2][1], P(171)[3][1]) + "<ul>" + "".join(f"<li>{i.strip()}</li>" for i in ["I. círculo com diâmetro de medida 1,60 m;", "II. círculo com diâmetro de medida 1,76 m;", "III. quadrado com lados de medida 1,60 m;", "IV. quadrado com lados de medida 1,76 m;", "V. triângulo equilátero com lados de medida 1,60 m."]) + "</ul>" + p("Utilize 1,7 como aproximação para √3.", P(171)[6][1]))
X(172, M, "Razão e proporção", "<p>Hoje o reservatório tem 480 + 30 = 510 milhões de m³, gastos em 30 dias: 17 milhões por dia. Para sobrar 25% do volume útil (120) e a reserva toda, só podem sair 360 milhões em 30 dias: 12 por dia. Redução: 17 − 12 = <strong>5,00</strong> milhões de m³ por dia. Alternativa <strong>B</strong>.</p><p>Esquecer a reserva técnica no consumo atual dá 16 − 12 = 4,00 (D).</p>",
  tags=["taxa média", "porcentagem"])
X(173, M, "Áreas", "<p>Com comprimento <em>c</em>, altura 2,8 e largura 3: paredes 2 × 2,8 × (<em>c</em> + 3) = 5,6<em>c</em> + 16,8; teto 3<em>c</em>. Descontos: porta 2,2 m² e janelas 2 × 1,5 = 3 m². Então 8,6<em>c</em> + 16,8 − 5,2 = 41,7, o que dá 8,6<em>c</em> = 30,1 e <em>c</em> = <strong>3,5 m</strong>. Alternativa <strong>B</strong>.</p><p>Esquecer o teto ou os descontos leva às outras alternativas.</p>",
  tags=["área de paralelepípedo", "equação do 1º grau"], trocas=[("41,7 m2", "41,7 m²")])
X(174, M, "Logaritmos", "<p>No gráfico, janeiro teve 2 000 unidades e fevereiro, 3 000: média de 2 500.</p><p>Último bimestre: E(11) = 1 500 + 2 000 × log 12 = 1 500 + 2 158 = 3 658; E(12) = 1 500 + 2 000 × log 13 = 1 500 + 2 228 = 3 728. Média: 3 693.</p><p>Diferença: 3 693 − 2 500 = <strong>1 193</strong>. Alternativa <strong>B</strong>.</p><p>Os valores de E(11) e E(12) saem direto dos logaritmos dados (log 12 e log 13), porque 1 + <em>n</em> vale 12 e 13.</p>",
  figs(("q174", "Gráfico sobre malha quadriculada: barras azuis para janeiro (cerca de 2 000 unidades) e fevereiro (cerca de 3 000), e uma curva vermelha de estimativa de junho a dezembro, levemente crescente, que passa por 3 500 em setembro.")),
  tags=["função logarítmica", "média"],
  enun=p(P(174)[0][1]) + p("E(<em>n</em>) = 1 500 + 2 000 × log<sub>10</sub>(1 + <em>n</em>), com 6 ≤ <em>n</em> ≤ 12, sendo <em>n</em> o número que identifica o mês. Por exemplo, a estimativa da quantidade de unidades vendidas ao longo do mês de agosto é E(8) = 1 500 + 2 000 × log<sub>10</sub>(1 + 8).")
       + "[[fig:1]]" + p(P(174)[3][1], "Utilize log<sub>10</sub> 12 = 1,079 e log<sub>10</sub> 13 = 1,114.", P(174)[5][1]))
X(175, M, "Trigonometria", "<p>O ângulo de visão de 90° tem um lado na direção de PO e o outro perpendicular a ele, isto é, tangente ao trilho em P. Esse lado tangente corta a semirreta <em>s</em> no ponto T. Se θ é o ângulo percorrido a partir de M, OT = 2/sen θ.</p><p>No começo (θ perto de 0), OT é enorme; depois diminui cada vez mais devagar, até OT = 2 m quando P chega a N (θ = 90°, em 30 s). A curva desce e vai se achatando até 2. Alternativa <strong>E</strong>.</p><p>D termina em zero, e B e C são retas, mas a relação não é linear.</p>",
  figs(("q175-1", "Três esquemas do trilho em quarto de circunferência de M a N, centro O, com a semirreta s horizontal. Em 0 segundo a câmera P está em M. Em 10 segundos e em 15 segundos, P avançou e o segmento OT, em vermelho, vai de O até T, além de N; em 15 segundos T está mais perto de N."),
       ("q175-2", "Gráfico A: reta vertical em t = 30, de c = 2 para cima."),
       ("q175-3", "Gráfico B: reta decrescente que chega a c = 0 em t = 30."),
       ("q175-4", "Gráfico C: reta decrescente que chega a c = 2 em t = 30."),
       ("q175-5", "Gráfico D: curva que desce rapidamente e se achata até c = 0 em t = 30."),
       ("q175-6", "Gráfico E: curva que desce rapidamente e se achata até c = 2 em t = 30.")),
  tags=["razões trigonométricas", "gráfico de funções"], alts={k: f"[[fig:{i}]]" for i, k in enumerate("ABCDE", 2)})
X(176, M, "Áreas", "<p>Na planta, a cozinha (2 m × 2 m) ocupa o canto de cima à direita; a sala, à esquerda, tem 4 m de altura e 6,5 m de largura, com o quarto (4 m × 4 m) encaixado embaixo da cozinha, avançando 2 m sobre a parte de baixo da sala. A sala tem 6,5 × 4 − 2 × 2 = 22 m².</p><p>A cozinha precisa virar 3,5 m × 3,5 m: avança 1,5 m para a esquerda (sobre a sala) e 1,5 m para baixo (sobre o quarto). O quarto, para continuar retangular, fica com 4 × 2,5 = <strong>10,00 m²</strong>. A sala perde 1,5 × 2 = 3 m² para a cozinha e ganha a faixa de 0,5 × 1,5 = 0,75 m² que saiu do quarto: 22 − 3 + 0,75 = <strong>19,75 m²</strong>. Alternativa <strong>D</strong>.</p>",
  figs(("q176-1", "Figura 1: mobiliário em L visto de cima, com 3,5 m de largura e 3,5 m de altura; o braço vertical tem um fogão e o horizontal, uma bancada."),
       ("q176-2", "Figura 2: planta do apartamento. Em cima, a sala (6,5 m de largura e 4 m de altura) e a cozinha (2 m × 2 m) à direita. Embaixo da cozinha, o quarto (4 m × 4 m), que avança sobre a sala; à esquerda do quarto, o banheiro, com 1 m de largura.")),
  tags=["área de retângulos", "planta baixa"])
X(177, M, "Escalas", "<p>A área da obra é 85 × 73 = 6 205 cm². A figurinha tem 62,05 cm², ou seja, 1/100 da área. Como a área varia com o quadrado da escala, a razão entre os lados é √(1/100) = 1/10: escala <strong>1 : 10</strong>. Alternativa <strong>D</strong>.</p><p>1 : 100 (E) é a razão das áreas, não a escala.</p>",
  figs(("q177", "Reprodução do quadro Abaporu, de Tarsila do Amaral: uma figura de pés e mãos enormes sentada ao lado de um cacto, sob um sol amarelo, com as dimensões de 85 cm de altura e 73 cm de largura.")),
  tags=["razão entre áreas", "semelhança"], trocas=[("62,05 cm2", "62,05 cm²")])
X(178, M, "Circunferência", "<p>Com π ≈ 3, a roda traseira percorre 3 × 0,6 = 1,8 m por volta: 3 600 ÷ 1,8 = 2 000 voltas. A dianteira, 3 × 0,8 = 2,4 m por volta: 3 600 ÷ 2,4 = 1 500 voltas. Diferença: <strong>500</strong>. Alternativa <strong>A</strong>.</p><p>Usar o diâmetro como se fosse o raio dobra as circunferências e reduz as voltas à metade (diferença de 250).</p>",
  tags=["comprimento da circunferência"])
X(179, M, "Análise combinatória", "<p>No esquema há 3 estradas de P a Q e 2 de S a T. Com <em>a</em> estradas de Q a R e <em>b</em> de R a S, o princípio multiplicativo dá 3 · <em>a</em> · <em>b</em> · 2 = 30, isto é, <em>a</em> · <em>b</em> = 5. Como 5 é primo e <em>a</em> &gt; <em>b</em>, <em>a</em> = 5 e <em>b</em> = 1. E 5 = 30/(3 × 2). Alternativa <strong>A</strong>.</p><p>B soma os caminhos em vez de multiplicar; D e E subtraem.</p>",
  figs(("q179", "Esquema com as cidades P, Q, R, S e T. Três estradas ligam P a Q e duas ligam S a T; R aparece isolada, sem as estradas que a ligam a Q e a S.")),
  tags=["princípio multiplicativo"],
  alts={"A": fr(30, "3 × 2"), "B": fr(30, "3 + 2"), "C": fr(30, 2), "D": "30 − (3 × 2)", "E": "30 − (3 + 2)"})
X(180, M, "Leitura de tabelas", "<p>71 kg está na faixa de 71 a 80 kg, e 1,71 m na coluna de 1,71 a 1,80 m. Nessa célula aparece “<strong>D-30</strong> ou D-33”, com D-30 em negrito, a mais adequada. Alternativa <strong>C</strong>.</p><p>Pegar a linha de 61 a 70 kg (D-28) ou a coluna de 1,61 a 1,70 m leva a B.</p>",
  figs(("q180", "Quadro de densidades recomendadas por massa (linhas: até 50, 51 a 60, 61 a 70, 71 a 80, 81 a 90, 91 a 100 kg) e altura (colunas: até 1,50; 1,51 a 1,60; 1,61 a 1,70; 1,71 a 1,80; 1,81 a 1,90; acima de 1,90 m). Na linha de 71 a 80 kg: –, D-28, D-28 (negrito) ou D-30, D-30 (negrito) ou D-33, D-30 (negrito) ou D-33, D-33.")),
  tags=["leitura de tabela de dupla entrada"])

completar(Q, R)
