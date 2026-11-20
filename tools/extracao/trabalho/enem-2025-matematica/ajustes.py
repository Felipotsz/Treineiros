# Enem 2025, 2º dia, caderno azul: Matemática (questões 136 a 180 do caderno; no site, 1 a 45, com numeroOriginal).
# Texto dos blocos do PDF; frações e fórmulas das alternativas reescritas em KaTeX a partir do caderno; π no lugar do "p" da extração.
# Questão 174 anulada pelo Inep (com a 123 e a 132, de Natureza) após relatos de antecipação de itens semelhantes.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, enunciado_enem, paragrafos_enem

ID = "enem-2025-matematica"
META = {"id": ID, "banca": "Enem", "ano": 2025, "titulo": "Enem 2025: Matemática", "fonte": "Inep", "dataExame": "2025-11-16",
        "duracaoMinutos": 150, "area": "Matemática", "caderno": "azul", "dia": 2}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2025-dia2-azul")
Q = {}
P = lambda n: paragrafos_enem(D[n])
p = lambda *xs: "".join(f"<p>{x}</p>" for x in xs)
ap = lambda *xs: "".join(f'<p class="apoio">{x}</p>' for x in xs)
K = lambda s: f"\\({s}\\)"
FR = lambda a, b: K(f"\\dfrac{{{a}}}{{{b}}}")
ANUL = ('<p>O Inep anulou esta questão e outras duas do 2º dia (no caderno azul, 123, 132 e 174) depois de relatos de que itens parecidos '
        'tinham sido divulgados nas redes sociais antes da prova. Segundo o Inep, nenhuma questão foi divulgada igual à da prova, só com '
        '“similaridades pontuais”, e o caso foi enviado à Polícia Federal. A anulação não aponta erro no conteúdo da questão.</p>')
LISTA = lambda s: "<ul>" + "".join(f"<li>{x.strip()}</li>" for x in s.split("•") if x.strip()) + "</ul>"


def figs(*pares):
    return [{"arquivo": a, "alt": t} for a, t in pares]


def tabela(cab, linhas):
    return ('<table class="tabela"><thead><tr>' + "".join(f"<th>{c}</th>" for c in cab) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in l) + "</tr>" for l in linhas) + "</tbody></table>")


def X(n, assunto, expl, imagens=(), tags=(), enun=None, trocas=(), alts=None, anulacao=None):
    q = {"materia": "Matemática", "assunto": assunto, "area": "Matemática", "tags": list(tags), "numeroOriginal": n,
         "enunciado": enun or enunciado_enem(D[n], trocas), "alternativas": dict(alts or D[n]["alternativas"]),
         "imagens": list(imagens), "explicacao": expl}
    if anulacao: q["anulacao"] = anulacao
    Q[n - 135] = q


ALT5 = {k: f"[[fig:{i}]]" for i, k in enumerate("ABCDE", 2)}

X(136, "Razão e proporção", "<p>Por semana o carro roda 30 · 7 = 210 km. Com 1 m<sup>3</sup> a cada 13 km, gasta 210 ÷ 13 ≈ 16,2 m<sup>3</sup>. O menor cilindro que comporta isso é o de <strong>17 m<sup>3</sup></strong> (o de 14 m<sup>3</sup> não basta). Alternativa <strong>C</strong>.</p>",
  tags=["consumo"], trocas=[("1 m3", "1 m<sup>3</sup>")])
X(137, "Probabilidade", "<p>90% dos internautas acessam redes sociais, e desses, 60% são mulheres, logo 40% são homens. A probabilidade de um internauta ser homem e acessar redes é 0,90 · 0,40 = 0,36 = <strong>36/100</strong>. Alternativa <strong>B</strong>.</p><p>40/100 (C) esquece que só 90% acessam; 40/90 (D) confunde a ordem das porcentagens.</p>",
  figs(("q137", "Infográfico “Perfil dos brasileiros nas redes sociais”: “90% dos internautas brasileiros acessam redes sociais”, com uma fileira de dez bonecos, nove destacados; abaixo, “Mulheres × homens: 60% da quantidade de internautas brasileiros que acessam redes sociais são mulheres”, com bonecos em duas fileiras.")),
  ["probabilidade condicional", "porcentagem"],
  alts={"A": FR(30, 90), "B": FR(36, 100), "C": FR(40, 100), "D": FR(40, 90), "E": FR(46, 90)})
X(138, "Geometria espacial", "<p>Os movimentos mudam as coordenadas do cubo: aproximar-se 3 unidades do plano <em>yz</em> diminui <em>x</em> em 3; afastar-se 5 do plano <em>xz</em> aumenta <em>y</em> em 5; aproximar-se 4 do plano <em>xy</em> diminui <em>z</em> em 4. Nas projeções, isso significa:</p><ul><li>no plano <em>yz</em> (parede do fundo), o quadrado anda 5 casas para a direita e 4 para baixo;</li><li>no plano <em>xz</em> (parede da esquerda), anda 3 casas em direção ao eixo <em>z</em> e 4 para baixo;</li><li>no plano <em>xy</em> (chão), anda 3 casas em direção ao eixo <em>y</em> e 5 para a direita.</li></ul><p>Na figura inicial, a projeção no fundo está na 2ª coluna e na 7ª linha da malha; depois do movimento, vai para a 7ª coluna e a 3ª linha, como na figura da Alternativa <strong>E</strong>, que também tem as outras duas projeções coerentes com esses deslocamentos.</p>",
  figs(("q138", "Malha 3D com eixos x, y e z: um cubo azul flutua perto do plano xz, com suas três projeções em azul: na parede do fundo (plano yz), perto do alto e à esquerda; na parede lateral (plano xz); e no chão (plano xy)."),
       ("q138a", "Alternativa A: projeções em vermelho, a do fundo à direita e bem no alto, a da parede lateral no meio e a do chão perto do eixo y."),
       ("q138b", "Alternativa B: projeções em vermelho, a do fundo no meio da altura, a lateral no alto, junto ao eixo z, e a do chão perto do eixo y."),
       ("q138c", "Alternativa C: projeções em vermelho, a do fundo à direita e na metade de cima, a lateral no meio e a do chão mais para fora."),
       ("q138d", "Alternativa D: projeções em vermelho, a do fundo à direita e na metade de cima, a lateral no meio e a do chão perto do canto."),
       ("q138e", "Alternativa E: projeções em vermelho, a do fundo mais à direita e mais baixa que nas outras, a lateral no meio e a do chão perto do eixo y.")),
  ["projeção ortogonal", "coordenadas no espaço"], enun=p(P(138)[0][1]) + "[[fig:1]]" + p(P(138)[2][1].replace("plano yz", "plano <em>yz</em>").replace("plano xz", "plano <em>xz</em>").replace("plano xy", "plano <em>xy</em>"), P(138)[3][1]),
  alts={"A": "[[fig:2]]", "B": "[[fig:3]]", "C": "[[fig:4]]", "D": "[[fig:5]]", "E": "[[fig:6]]"})
X(139, "Geometria plana", "<p>Cada policial protege 200 m para cada lado, ou 400 m de ciclovia. O comprimento da ciclovia é 2 · π · 1 000 ≈ 2 · 3 · 1 000 = 6 000 m. São necessários 6 000 ÷ 400 = <strong>15</strong> policiais. Alternativa <strong>C</strong>.</p><p>Contar só 200 m por policial dá 30 (D).</p>",
  figs(("q139", "Lagoa circular azul cercada por um anel branco (a ciclovia). Num ponto P da ciclovia, uma faixa cinza escura se estende 200 m para cada lado de P.")),
  ["comprimento da circunferência"], trocas=[("há um uma ciclovia", "há uma ciclovia"), ("aproximação para p.", "aproximação para π.")])
X(140, "Porcentagem", "<p>A quantidade de S<sub>2</sub> não muda: 0,05% de 10 L = 0,005 L. Na nova solução, esses 0,005 L devem ser 0,10%: o total passa a ser 0,005 ÷ 0,001 = 5 L. Saem 10 − 5 = <strong>5 L</strong> de S<sub>1</sub>. Alternativa <strong>E</strong>.</p><p>O resultado surpreende porque a fração de S<sub>2</sub> dobra (de 0,05% para 0,10%), e para isso o volume total precisa cair pela metade.</p>",
  tags=["misturas"], trocas=[("S1 e S2", "S<sub>1</sub> e S<sub>2</sub>"), ("é de S1. Uma quantidade de S1", "é de S<sub>1</sub>. Uma quantidade de S<sub>1</sub>"), ("de S2, de modo", "de S<sub>2</sub>, de modo"), ("seja de S1.", "seja de S<sub>1</sub>."), ("quantidade de S1, em litro", "quantidade de S<sub>1</sub>, em litro")])
X(141, "Operações", "<p>Na primeira entrega, foram enviados 10 200 L e chegaram 9 900 L: o descarte é de 300 L, fixo. O novo pedido é o dobro do anterior, 2 · 10 000 = 20 000 L. A distribuidora precisa enviar 20 000 + 300 = <strong>20 300 L</strong>. Alternativa <strong>C</strong>.</p><p>Dobrar o volume entregue (9 900) dá 20 100 (A); dobrar o enviado dá 20 400 (D).</p>",
  tags=["problema"])
X(142, "Estatística", "<p>Em ordem: 320, 340, 350, 360, 380, 380, 390, 390, 390, 400. Com dez valores, a mediana é a média dos dois centrais (5º e 6º): (380 + 380) ÷ 2 = <strong>380</strong>. Alternativa <strong>C</strong>.</p><p>390 (D) é a moda; 370 (B) é a média dos valores.</p>",
  tags=["mediana"], enun=p(P(142)[0][1]) + tabela(["Cidade", "Velocidade de referência (MB/s)"], [[f"C{i}", v] for i, v in enumerate([390, 380, 320, 390, 340, 380, 390, 400, 350, 360], 1)]) + p(P(142)[-1][1]))
X(143, "Operações", "<p>Sódio total por pacote = porções × sódio por porção:</p><ul><li>batata chips: 3 · 170 = <strong>510 mg</strong>;</li><li>palitos salgados: 4 · 501 = 2 004 mg;</li><li>biscoito multigrãos: 8 · 264 = 2 112 mg;</li><li>biscoito de polvilho: 6 · 175 = 1 050 mg;</li><li>biscoito de água e sal: 5 · 166 = 830 mg.</li></ul><p>O menor é o da batata chips. Alternativa <strong>A</strong>.</p><p>Olhar só o sódio por porção levaria ao biscoito de água e sal (E).</p>",
  figs(("q143", "Cinco rótulos coloridos. Batata chips: pacote com 3 porções de 50 g, 170 mg de sódio por porção. Palitos salgados: 4 porções de 20 g, 501 mg por porção. Biscoito multigrãos: 8 porções de 25 g, 264 mg por porção. Biscoito de polvilho: 6 porções de 15 g, 175 mg por porção. Biscoito de água e sal: 5 porções de 40 g, 166 mg por porção.")),
  ["leitura de rótulos"])
X(144, "Geometria espacial", "<p>O prisma hexagonal tem duas bases hexagonais e 6 faces laterais retangulares iguais. Uma de suas bases fica colada à base maior do tronco, por isso não é pintada. O tronco acrescenta a base menor (hexágono menor) e 6 trapézios iguais. As faces visíveis são de quatro tipos: o hexágono grande da base do prisma, os retângulos, os trapézios e o hexágono pequeno. São <strong>4</strong> cores. Alternativa <strong>D</strong>.</p>",
  tags=["poliedros", "prisma", "tronco de pirâmide"])
X(145, "Funções", "<p>No gráfico, a frequência fica em f<sub>1</sub> até t<sub>1</sub>, depois <strong>diminui</strong> até t<sub>2</sub> e, a partir daí, fica constante em f<sub>2</sub>. Alternativa <strong>D</strong>.</p><p>A curva entre t<sub>1</sub> e t<sub>2</sub> não é uma reta nem uma hipérbole, logo não há proporcionalidade (B, C e E).</p>",
  figs(("q145", "Gráfico frequência respiratória (rpm) × tempo (min): uma linha horizontal no nível f₁ até o instante t₁ (início da prática meditativa); depois a curva desce suavemente até o nível f₂, no instante t₂, e segue horizontal.")),
  ["leitura de gráfico"], trocas=[("(f1)", "(f<sub>1</sub>)"), ("instante t1", "instante t<sub>1</sub>"), ("(f2)", "(f<sub>2</sub>)"), ("instante t2", "instante t<sub>2</sub>")])
X(146, "Operações", "<p>10,00 − 9,58 = <strong>0,42 s</strong>. Alternativa <strong>B</strong>.</p><p>Alinhar as casas decimais evita os erros comuns: 0,52 (C) vem de errar o “empresta um” na subtração, e 1,42 (E), de somar 1 a mais na casa das unidades.</p>", tags=["números decimais"])
X(147, "Porcentagem", "<p>Total de 2024: 280 + 80 + 20 + 20 = 400 matrículas. Em 2023, o francês tinha 10% do total. A estimativa é 10% de 400 = <strong>40</strong>. Alternativa <strong>E</strong>.</p><p>20 (C) é o número de 2024; 2 (A) é 10% de 20.</p>",
  figs(("q147", "À esquerda, gráfico de setores “Porcentagem de matrículas por idioma – 2023”: inglês 60%, espanhol 25%, francês 10%, alemão 5%. À direita, gráfico de barras “Quantidade de matrículas por idioma – 2024”: inglês 280, espanhol 80, francês 20, alemão 20.")),
  ["gráficos"])
X(148, "Escala", "<p>Comprimento real = medida na tela × fator da escala:</p><ul><li>I: 9 · 100 = 900 cm;</li><li>II: 5 · 300 = 1 500 cm;</li><li>III: 5 · 600 = <strong>3 000 cm</strong>;</li><li>IV: 3 · 700 = 2 100 cm;</li><li>V: 2 · 1 000 = 2 000 cm.</li></ul><p>O maior é o III. Alternativa <strong>C</strong>.</p>",
  figs(("q148", "Cinco telas do controle remoto. I: segmento AB de 9 cm, escala 1 : 100. II: segmento CB de 5 cm, escala 1 : 300. III: segmento CD de 5 cm, escala 1 : 600. IV: segmento DE de 3 cm, escala 1 : 700. V: segmento EF de 2 cm, escala 1 : 1 000.")),
  ["escala"])
X(149, "Geometria espacial", "<p>O poliedro é formado por uma cúpula pentagonal (pentágono no topo, 5 vértices, e decágono embaixo, 10 vértices) colada a um antiprisma decagonal, que acrescenta outro decágono, de 10 vértices. Total: 5 + 10 + 10 = <strong>25</strong> vértices. Alternativa <strong>B</strong>.</p><p>Outra forma: pela planificação, há 1 decágono, 5 quadrados, 1 pentágono e 25 triângulos, ou 32 faces e 55 arestas. Por Euler, V = 2 + A − F = 2 + 55 − 32 = 25. Quem confunde vértices com arestas marca 55 (C).</p>",
  figs(("q149", "Duas vistas da cúpula pentagonal giralongada, com faces triangulares azuis, quadrados amarelos, um pentágono verde e um decágono vermelho; abaixo, sua planificação: o decágono vermelho no centro, cercado de triângulos azuis, quadrados amarelos e um pentágono verde.")),
  ["poliedros", "relação de Euler"])
X(150, "Razão e proporção", "<p>Cada funcionário produz 720 ÷ (3 · 6) = 40 tijolos por hora. Depois: 5 · 9 · 40 = <strong>1 800</strong> tijolos por dia. Alternativa <strong>D</strong>.</p><p>Outra forma: a produção é proporcional a funcionários × horas, que passa de 3 · 6 = 18 para 5 · 9 = 45, multiplicando por 2,5: 720 · 2,5 = 1 800. Considerar só os funcionários dá 1 200 (C), e só as horas, 1 080 (B).</p>",
  tags=["regra de três composta"])
X(151, "Operações", "<p>Seguindo a ordem da regra: andar 2 (1 dígito); setor 08 (2 dígitos); funcionário 109 (3 dígitos); chegada às 10 h, de manhã, dígito 0. O código é <strong>2 08 109 0 = 2081090</strong>. Alternativa <strong>D</strong>.</p><p>As demais alternativas trocam a ordem dos campos ou o número de dígitos de cada um.</p>",
  tags=["códigos"], enun=ap(P(151)[0][1]) + LISTA(P(151)[1][1]).replace("<ul>", '<ul class="apoio">') + p(P(151)[2][1], P(151)[3][1]))
X(152, "Probabilidade", "<p>Há 4! = 24 maneiras de distribuir os 4 envelopes, e só uma devolve cada celular ao dono. A probabilidade é <strong>1/24</strong>. Alternativa <strong>D</strong>.</p><p>1/256 (E) seria 4<sup>4</sup>, como se um mesmo envelope pudesse ir para mais de uma pessoa.</p>",
  tags=["permutação"], alts={"A": FR(1, 2), "B": FR(1, 10), "C": FR(1, 16), "D": FR(1, 24), "E": FR(1, 256)})
X(153, "Geometria analítica", "<p>Os pontos equidistantes de T e V formam a mediatriz de TV. Num quadrado STUV, T e V são vértices opostos, e a mediatriz da diagonal TV é a outra diagonal, SU. Com S(6, 2) e V(8, 6), o lado SV = (2, 4), e girando 90° obtém-se ST = (−4, 2), então T = (2, 4) e U = T + (2, 4) = (4, 8). A reta SU tem inclinação (8 − 2) ÷ (4 − 6) = −3: y − 2 = −3(x − 6), ou <strong>y = −3x + 20</strong>. Alternativa <strong>A</strong>.</p><p>Conferência: o ponto médio de TV, (5, 5), satisfaz y = −3 · 5 + 20 = 5.</p>",
  figs(("q153", "Plano cartesiano com um quadrado azul-claro STUV inclinado: S(6; 2) embaixo, V(8; 6) à direita, U em cima e T à esquerda.")),
  ["mediatriz", "equação da reta"])
X(154, "Estatística", "<p>Estoque total por gênero (brasileiros + estrangeiros) comparado com a demanda:</p><ul><li>ficção: 80 + 120 = 200 &gt; 160;</li><li>autoajuda: 50 + 80 = 130 &lt; cerca de 136;</li><li>romance: 40 + 105 = 145 &gt; 140;</li><li>biografia: cerca de 46 + 50 = 96 &gt; 80.</li></ul><p>Só a autoajuda tem estoque menor que a demanda. Alternativa <strong>C</strong>.</p>",
  figs(("q154", "Gráfico “Estoque e demanda por livros”: barras de autores brasileiros e estrangeiros e uma linha de demanda. Ficção: 80 brasileiros, 120 estrangeiros, demanda 160. Autoajuda: 50 e 80, demanda cerca de 136. Romance: 40 e 105, demanda 140. Biografia: cerca de 46 e 50, demanda 80.")),
  ["gráfico de barras"])
X(155, "Análise combinatória", "<p>Presidente: 20 pessoas possíveis. Secretário: não pode ser a pessoa escolhida nem seu cônjuge, sobram 18. Tesoureiro: sobram 16. Total: <strong>20 × 18 × 16</strong>. Alternativa <strong>B</strong>.</p><p>20 × 19 × 18 (C) ignora a restrição dos casais; 10 × 9 × 8 × 2 (D) escolhe os casais, mas multiplica por 2 uma vez só, em vez de 2 para cada cargo.</p>",
  tags=["princípio multiplicativo"])
X(156, "Escala", "<p>20 cm no desenho correspondem a 30 m = 3 000 cm na areia. A escala é 20 : 3 000 = <strong>1 : 150</strong>. Alternativa <strong>E</strong>.</p><p>1 : 1,5 (A) esquece a conversão de metro para centímetro; 1 : 2,25 (B) compara áreas.</p>",
  figs(("q156", "Desenho de um sol amarelo com oito raios triangulares, contido num quadrado de 20 cm de largura por 20 cm de altura.")),
  ["escala", "conversão de unidades"])
X(157, "Álgebra", "<p>“T era 1,59 vezes F” significa T = 1,59 · F, ou <strong>T/F = 1,59</strong>. Alternativa <strong>C</strong>.</p><p>A e B trocam produto por soma; D inverte a razão; E multiplica as duas concentrações.</p>",
  tags=["razão"], trocas=[("denotada por T,", "denotada por <em>T</em>,"), ("denotada por F.", "denotada por <em>F</em>."), ("entre T e F", "entre <em>T</em> e <em>F</em>")],
  alts={"A": K("T = 1{,}59 + F"), "B": K("F = 1{,}59 + T"), "C": K("\\dfrac{T}{F} = 1{,}59"), "D": K("\\dfrac{F}{T} = 1{,}59"), "E": K("F \\cdot T = 1{,}59")})
X(158, "Porcentagem", "<p>Seguro reajustado: 36 · 1,20 = R$ 43,20 por veículo, ou 43,20 · 120 = R$ 5 184,00. Despesas: 14 240 + 5 184 = R$ 19 424,00. Para lucrar R$ 10 000,00, é preciso arrecadar 29 424, e a mensalidade fica em 29 424 ÷ 120 = <strong>R$ 245,20</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["lucro", "aumento percentual"])
X(159, "Grandezas e medidas", "<p>1 cm<sup>3</sup> = 1 mL, logo o pote tem 20 000 mL. São 20 000 ÷ 250 = <strong>80</strong> taças. Alternativa <strong>D</strong>.</p><p>Tratar 250 mL como 0,25 L e o pote como 20 L dá o mesmo resultado (20 ÷ 0,25 = 80). Errar a conversão por um fator de 10 leva a 8 (B) ou 800 (E).</p>",
  tags=["volume", "conversão de unidades"], trocas=[("20 000 cm3", "20 000 cm<sup>3</sup>")])
X(160, "Trigonometria", "<p>A tangente tem assíntotas separadas por um período, π/p. No gráfico, elas estão em (5 − 2π)/2 e (5 + 2π)/2, distantes 2π: π/p = 2π, logo <strong>p = 1/2</strong>. O ponto central entre as assíntotas é T = 2,5, onde a tangente vale zero e D = 30: <strong>k = 30</strong> e T + m = 0 em T = 5/2, logo m = −5/2. Então D = 30 + tg[½(T − 5/2)]. Alternativa <strong>E</strong>.</p><p>D usa T − 5, que poria o centro em T = 5.</p>",
  figs(("q160", "À esquerda, um recipiente em forma de taça sobre o tampo da mesa. À direita, o gráfico de D em função de T: curva crescente em forma de tangente, que passa por D = 30 em T = 2,5 e vai até T = 4, com assíntotas verticais em T = (5 − 2π)/2 e T = (5 + 2π)/2.")),
  ["função tangente", "período"],
  enun=p(P(160)[0][1].replace("distância D", "distância <em>D</em>").replace("tempo T", "tempo <em>T</em>")) + p(K("D = k + \\text{tg}[p(T + m)]") + ", sendo os parâmetros <em>k</em>, <em>p</em> e <em>m</em> números reais, para <em>T</em> variando entre 0 e 4 minutos, conforme ilustrado na figura, na qual estão apresentadas assíntotas verticais da função tangente utilizada na definição de <em>D</em>.") + "[[fig:1]]" + p("A expressão algébrica que representa a relação entre <em>D</em> e <em>T</em> é"),
  alts={"A": K("D = 2{,}5 + \\text{tg}\\left[30\\left(T - \\dfrac{5 - 2\\pi}{2}\\right)\\right]"), "B": K("D = 4 + \\text{tg}\\left[30\\left(T + \\dfrac{5}{2}\\right)\\right]"),
        "C": K("D = 4 + \\text{tg}\\left[2{,}5\\left(T + \\dfrac{5 + 2\\pi}{2}\\right)\\right]"), "D": K("D = 30 + \\text{tg}\\left[\\dfrac{1}{2}(T - 5)\\right]"),
        "E": K("D = 30 + \\text{tg}\\left[\\dfrac{1}{2}\\left(T - \\dfrac{5}{2}\\right)\\right]")})
X(161, "Localização", "<p>Fazendo o caminho de trás para a frente: a casa do amigo (A) está no segundo quarteirão a oeste do ponto onde João dobrou à esquerda. Esse ponto fica na rua acima da linha de A, entre a 4ª e a 5ª coluna. João chegou ali depois de subir três quarteirões para o norte pela rua a oeste do seu quarteirão. Descendo três quarteirões a partir da linha de A (4ª linha), chega-se à 7ª linha, e o quarteirão de João é o da 5ª coluna, logo a leste dessa rua: o <strong>P</strong>. Alternativa <strong>A</strong>.</p>",
  figs(("q161", "Malha de quarteirões cinza com 7 linhas e 6 colunas e uma rosa dos ventos (N em cima, L à direita). O quadradinho preto A está no canto superior esquerdo do quarteirão da 4ª linha, 3ª coluna. Aparecem letras em alguns quarteirões: Q (1ª linha, 5ª coluna), S (4ª linha, 5ª coluna), R (7ª linha, 1ª coluna), P (7ª linha, 5ª coluna) e T (7ª linha, 6ª coluna).")),
  ["orientação", "pontos cardeais"])
X(162, "Inequações", "<p>Reciclar custa R$ 500 por tonelada, que é 5% do custo com petróleo: R$ 10 000 por tonelada. O custo atual é 110 · 10 000 + 80 · 500 = R$ 1 140 000. A meta é no máximo metade: R$ 570 000 para as mesmas 190 t. Com x toneladas recicladas: 500x + 10 000(190 − x) ≤ 570 000, ou seja, 1 900 000 − 9 500x ≤ 570 000, logo x ≥ 140. Alternativa <strong>B</strong>.</p>",
  tags=["porcentagem", "inequação do 1º grau"])
X(163, "Estatística", "<p>Pelas barras (em unidades da grade): 1ª série, futebol 7, vôlei 3, basquete 1; 2ª série, 6, 3 e 3; 3ª série, 5, 4 e 4. Totais: futebol 18, vôlei 10, basquete 8. O setor do futebol é metade do círculo, e de fato 18 = 10 + 8. O basquete (8 unidades) tem 80 estudantes, então cada unidade vale 10. Total: 36 · 10 = <strong>360</strong>. Alternativa <strong>B</strong>.</p>",
  figs(("q163", "Dois gráficos. Em cima, barras “Modalidades esportivas no ensino médio, por série”, sem escala numérica: na 1ª série, futebol bem alto, vôlei médio e basquete baixo; na 2ª, futebol alto e vôlei e basquete iguais; na 3ª, as três barras próximas, com futebol um pouco mais alto. Embaixo, setores “Quantidade de estudantes, por modalidade esportiva”: futebol ocupa metade do círculo, vôlei e basquete dividem a outra metade, e o setor do basquete indica 80.")),
  ["gráficos", "proporção"])
X(164, "Trigonometria", "<p>Como QR e ST são iguais (mesma direção, mesmo tempo), o deslocamento de T até R é igual ao de S até Q, isto é, PQ − PS. PQ e PS têm o mesmo tamanho (4 h de viagem) e formam ângulo de 340° − 110° = 230°, ou seja, 130°. Pela lei dos cossenos, em horas de viagem: d<sup>2</sup> = 4<sup>2</sup> + 4<sup>2</sup> − 2 · 4 · 4 · cos 130° = 32 + 32 · 0,64 = 52,48, logo d ≈ 7,24 h ≈ <strong>7 h 15 min</strong>. Para a direção, decompondo em leste e norte: PQ − PS = 4(sen 110° − sen 340°; cos 110° − cos 340°) ≈ 4(1,28; −1,28), com componentes iguais para leste e para sul, isto é, a direção <strong>135</strong>. Alternativa <strong>A</strong>.</p>",
  figs(("q164", "Bússola graduada de 0 a 340 (N em 0, L em 90, S em 180, O em 270). Abaixo, as rotas: de P, a planejada vai para sudeste até Q e depois para leste até R; a executada vai para noroeste até S e depois para leste até T; uma linha tracejada liga T a R.")),
  ["lei dos cossenos", "vetores"], enun=p(P(164)[0][1]) + '<ul class="apoio"><li>' + P(164)[1][1] + "</li><li>" + P(164)[2][1] + "</li></ul>" + p(P(164)[3][1]) + '<ul class="apoio"><li>' + P(164)[4][1] + "</li><li>" + P(164)[5][1] + "</li></ul>" + p(P(164)[6][1]) + "[[fig:1]]" + p(P(164)[8][1], P(164)[9][1], P(164)[10][1]))
X(165, "Estatística", "<p>O grupo 4 tem média 25 anos e desvio padrão de só 1 ano: as idades estão muito concentradas perto de 25. Para alguém ter menos de 20 ou mais de 30, precisaria estar 5 anos longe da média, o que, com desvio padrão 1, permite no máximo 1/25 do grupo (desigualdade de Chebyshev), menos de uma pessoa entre 11. A maioria, na verdade todas, tem entre 20 e 30 anos. Alternativa <strong>D</strong>.</p><p>No grupo 1, desvio padrão 10 permite idades muito espalhadas; mediana ou moda 25 (grupos 2 e 3) não garantem a maioria na faixa; e o grupo 5 tem idades de 20 a 35, sem saber quantas passam de 30.</p>",
  figs(("q165", "Quadro parcialmente preenchido com as idades dos grupos: Grupo 1, média 25 e desvio padrão 10. Grupo 2, mediana 25 e desvio padrão 9. Grupo 3, moda 25. Grupo 4, média 25 e desvio padrão 1. Grupo 5, menor idade 20 e maior idade 35. As demais células estão vazias.")),
  ["desvio padrão", "medidas de tendência central"])
X(166, "Operações", "<p>Para ter pace de 281 s/km em 5 km, o tempo total deve ser 281 · 5 = 1 405 s. Até o 4º km ele gastou 1 132 s, então o 5º trecho precisa de 1 405 − 1 132 = 273 s. O 4º trecho levou 288 s: são <strong>15 s</strong> a menos. Alternativa <strong>E</strong>.</p>",
  figs(("q166", "Linha de 0 a 5 km. Tempo de corrida ao cruzar cada marca: 0 s, 272 s (1 km), 556 s (2 km), 844 s (3 km) e 1 132 s (4 km). Tempo de cada trecho: 1º, 272 s; 2º, 284 s; 3º, 288 s; 4º, 288 s; o 5º trecho ainda está por fazer.")),
  ["média", "tempo"])
X(167, "Funções", "<p>Pelos gráficos, a 60 km/h o rendimento é de 10 km/m<sup>3</sup> com GNV e 8 km/L com gasolina. Cada metade tem 120 km:</p><ul><li>GNV: 120 ÷ 10 = 12 m<sup>3</sup> · R$ 2,00 = R$ 24,00;</li><li>gasolina: 120 ÷ 8 = 15 L · R$ 3,00 = R$ 45,00.</li></ul><p>Diferença: 45 − 24 = <strong>R$ 21,00</strong>. Alternativa <strong>D</strong>.</p>",
  figs(("q167", "Dois gráficos de rendimento × velocidade (km/h, de 20 a 140). GNV (km/m³): começa em 8 a 20 km/h, passa por 10 a 60 km/h, chega a 12 perto de 100 km/h e cai até cerca de 10 em 140 km/h. Gasolina (km/L): começa em 6 a 20 km/h, passa por 8 a 60 km/h, chega a 11 perto de 100 km/h e cai até cerca de 9 em 140 km/h.")),
  ["leitura de gráfico", "consumo"])
X(168, "Operações", "<p>Custo = 20 aulas teóricas + 10 práticas + aluguel:</p><ul><li>I: 20 · 10 + 10 · 80 + 400 = R$ 1 400;</li><li>II: 20 · 30 + 10 · 50 + 200 = R$ 1 300;</li><li>III: 20 · 20 + 10 · 40 + 400 = <strong>R$ 1 200</strong>.</li></ul><p>Alternativa <strong>E</strong>.</p><p>B e D somam só uma aula de cada tipo.</p>",
  tags=["custo"], enun=ap(P(168)[0][1]) + LISTA(P(168)[1][1]).replace("<ul>", '<ul class="apoio">') + p(P(168)[2][1]) + tabela(["Autoescola", "Aula teórica (R$)", "Aula prática (R$)", "Aluguel do veículo (R$)"], [["I", 10, 80, 400], ["II", 30, 50, 200], ["III", 20, 40, 400]]) + p(P(168)[-2][1], P(168)[-1][1]))
X(169, "Estatística", "<p>Produção (t) = área × produtividade × 50 kg ÷ 1 000:</p><ul><li>11-12: 200 · 40 · 0,05 = 400 t;</li><li>12-13: 220 · 30 · 0,05 = 330 t;</li><li>13-14: 250 · 45 · 0,05 = 562,5 t;</li><li>14-15: 562,5 t;</li><li>15-16: 200 · 50 · 0,05 = 500 t.</li></ul><p>Esses valores aparecem no gráfico da Alternativa <strong>A</strong>.</p><p>B mostra só a produtividade; C mostra só a área; D e E usam fatores errados.</p>",
  figs(("q169a", "Alternativa A: produção (t) por safra: 400, 330, 562,5, 562,5 e 500."),
       ("q169b", "Alternativa B: 40, 30, 45, 45 e 50."),
       ("q169c", "Alternativa C: 200, 220, 250, 250 e 200."),
       ("q169d", "Alternativa D: 240, 250, 295, 295 e 250."),
       ("q169e", "Alternativa E: 8, 6,6, 11,25, 11,25 e 10.")),
  ["gráfico de linhas", "conversão de unidades"],
  enun=p(P(169)[0][1]) + tabela(["Safra", "Área cultivada (hectare)", "Produtividade (sacas de 50 kg por hectare)"], [["11-12", 200, 40], ["12-13", 220, 30], ["13-14", 250, 45], ["14-15", 250, 45], ["15-16", 200, 50]]) + p(P(169)[2][1]),
  alts={k: f"[[fig:{i}]]" for i, k in enumerate("ABCDE", 1)})
X(170, "Geometria espacial", "<p>Volume de água com a caixa cheia: 2,5 · 1,5 · 2 = 7,5 dm<sup>3</sup> = 7,5 L. Para sobrar pelo menos 5 L, as garrafas podem ocupar até 2,5 L = 2 500 mL: 2 500 ÷ 300 ≈ 8,3, ou seja, no máximo <strong>8</strong> garrafas. Alternativa <strong>B</strong>.</p>",
  figs(("q170a", "Caixa de descarga em forma de paralelepípedo, com base de 2,5 dm por 1,5 dm, pouca água no fundo e a boia abaixada."),
       ("q170b", "A mesma caixa cheia de água até 2 dm de altura, com a boia no alto, interrompendo o abastecimento.")),
  ["volume do paralelepípedo"])
X(171, "Geometria espacial", "<p>A maior torta tem raio 16 cm, ou 32 cm de diâmetro. Com 1 cm de folga de cada lado, a base da caixa precisa de 32 + 2 = 34 cm. A altura (6 + 1 = 7 cm) já serve. A nova aresta deve ser 34 − 14 = <strong>20 cm</strong> maior. Alternativa <strong>E</strong>.</p><p>Esquecer a folga dá 18 (D); usar o raio em vez do diâmetro dá 4 (A).</p>",
  tags=["cilindro", "prisma"])
X(172, "Logaritmos", "<p>P ≤ 10 significa 4 · log[...] ≤ 10, ou log[−K(t + 1)(t − 19)] ≤ 2,5, ou seja, K(t + 1)(19 − t) ≤ 10<sup>2,5</sup>. A expressão (t + 1)(19 − t) é uma parábola com máximo em t = 9, que está dentro das 10 horas de uso: (9 + 1)(19 − 9) = 100. Então 100K ≤ 10<sup>2,5</sup>, e K ≤ 10<sup>2,5</sup> ÷ 10<sup>2</sup> = <strong>10<sup>0,5</sup></strong>. Alternativa <strong>A</strong>.</p><p>Calcular só em t = 10 (11 · 9 = 99) dá 10<sup>2,5</sup>/99 (D), mas a pressão passa do limite antes, em t = 9.</p>",
  tags=["função logarítmica", "função quadrática"],
  enun=p(P(172)[0][1].replace("pressão interna P", "pressão interna <em>P</em>").replace("utilização t", "utilização <em>t</em>").replace("parâmetro positivo K", "parâmetro positivo <em>K</em>")) + p(K("P = 4 \\cdot \\log[-K \\cdot (t + 1) \\cdot (t - 19)]")) + p(P(172)[2][1].replace("parâmetro K", "parâmetro <em>K</em>"), "O maior valor a ser escolhido para <em>K</em> é"),
  alts={"A": K("10^{0,5}"), "B": K("10^{8}"), "C": K("\\dfrac{10^{2,5}}{84}"), "D": K("\\dfrac{10^{2,5}}{99}"), "E": K("25 \\times 10^{-2}")})
X(173, "Geometria plana", "<p>Área de um semicírculo: π r<sup>2</sup> ÷ 2, com π ≈ 3.</p><ul><li>Projeto 1: raios 6 m e 3 m: (3 · 36 + 3 · 9) ÷ 2 = (108 + 27) ÷ 2 = <strong>67,5 m<sup>2</sup></strong>.</li><li>Projeto 2: largura total 3 + 6 + 6 + 3 = 18 m, raio 9 m: 3 · 81 ÷ 2 = 121,5 m<sup>2</sup>.</li></ul><p>O projeto 1 tem a menor área. Alternativa <strong>A</strong>.</p><p>135 m<sup>2</sup> e 243 m<sup>2</sup> (C e D) usam o círculo inteiro.</p>",
  figs(("q173", "Vistas frontais. Projeto 1: dois túneis semicirculares lado a lado, um para automóveis com 12 m de largura (volta e ida) e outro para bicicletas com 6 m (volta e ida). Projeto 2: um único túnel semicircular com faixas de 3 m (volta, bicicletas), 6 m (volta, automóveis), 6 m (ida, automóveis) e 3 m (ida, bicicletas).")),
  ["área do círculo"], trocas=[("aproximação para p", "aproximação para π")],
  alts={k: v.replace(" m2", " m<sup>2</sup>") for k, v in D[173]["alternativas"].items()})
X(174, "Equações", "<p>Pela análise do Treineiros, a conta esperada seria: 60 000/n − 60 000/(n + 6) = 500, que leva a n(n + 6) = 720, isto é, n² + 6n − 720 = 0, com raiz positiva n = <strong>24</strong>. Alternativa <strong>B</strong>, se a questão não tivesse sido anulada.</p>",
  tags=["equação do 2º grau"], anulacao={"fonte": "oficial", "motivo": ANUL},
  enun=p(P(174)[0][1]) + LISTA(P(174)[1][1]).replace("<ul>", '<ul class="apoio">') + p(P(174)[2][1], P(174)[3][1]))
X(175, "Análise combinatória", "<p>O mais velho recebe exatamente um entre bicicleta e celular: 2 escolhas. Os outros 2 presentes dele saem dos 6 restantes que não são nem bicicleta nem celular: C(6, 2) = 15. Sobram 5 presentes (entre eles o outro da dupla): o mais novo escolhe 3, C(5, 3) = 10, e o do meio fica com os 2 restantes. Total: 2 · 15 · 10 = <strong>300</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["combinação"])
X(176, "Razão e proporção", "<p>No segundo tempo, ele percorreu 4,5 km em 45 min. Na prorrogação, com a mesma velocidade, em 30 min percorre 4,5 · 30/45 = 3 km. Total: 4,5 + 3 = <strong>7,5 km</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["velocidade média"])
X(177, "Geometria espacial", "<p>Área do disco: π · 3<sup>2</sup> = 3,1 · 9 = 27,9 cm<sup>2</sup>. O quadrado está inscrito, com diagonal 6 cm: área 6<sup>2</sup> ÷ 2 = 18 cm<sup>2</sup>. Área de ouro: 27,9 − 18 = 9,9 cm<sup>2</sup>. Volume por medalha: 9,9 · 0,3 = 2,97 cm<sup>3</sup>. Para 100 medalhas: <strong>297 cm<sup>3</sup></strong>. Alternativa <strong>B</strong>.</p><p>Esquecer de converter 3 mm em 0,3 cm multiplica o resultado por 10 (D).</p>",
  figs(("q177", "Medalha circular dourada de 6 cm de diâmetro, com um quadrado cinza ABCD inscrito (vértices A em cima, B à direita, C embaixo, D à esquerda); ao lado, a medalha em perspectiva com espessura de 3 mm.")),
  ["cilindro", "quadrado inscrito"], trocas=[("aproximado para p", "aproximado para π")])
X(178, "Probabilidade", "<p>João vence se o maior número de Artur for menor ou igual ao dele. Se João tira j, a chance de os dois dados de Artur serem ≤ j é (j/6)<sup>2</sup>. Somando para j de 1 a 6, cada caso com chance 1/6: (1 + 4 + 9 + 16 + 25 + 36) ÷ 216 = 91/216. Artur vence com 1 − 91/216 = <strong>125/216</strong>, a maior probabilidade. Alternativa <strong>E</strong>.</p>",
  tags=["probabilidade", "eventos independentes"],
  alts={"A": "Artur, com probabilidade de " + FR(2, 3), "B": "João, com probabilidade de " + FR(4, 9), "C": "Artur, com probabilidade de " + FR(91, 216), "D": "João, com probabilidade de " + FR(91, 216), "E": "Artur, com probabilidade de " + FR(125, 216)})
X(179, "Grandezas e medidas", "<p>A luminância é definida como a razão entre a intensidade luminosa (em candela) e o quadrado da distância (em metro). A unidade é a da intensidade dividida pela da distância ao quadrado: <strong>cd/m<sup>2</sup></strong>. Alternativa <strong>A</strong>.</p><p>B e D invertem a razão; C esquece o quadrado da distância; E eleva ao quadrado a grandeza errada.</p>",
  tags=["unidades de medida"], alts={"A": FR("\\text{cd}", "\\text{m}^2"), "B": FR("\\text{m}^2", "\\text{cd}"), "C": FR("\\text{cd}", "\\text{m}"), "D": FR("\\text{m}", "\\text{cd}"), "E": FR("\\text{m}", "\\text{cd}^2")})
X(180, "Sequências", "<p>Em cada rodada, o jogador 1 dá 1 moeda ao jogador 2 e recebe 4 do jogador 4: ganha 3 por rodada. Depois de n rodadas: <strong>100 + 3n</strong>. Alternativa <strong>D</strong>.</p><p>100 + 4n (C) esquece a moeda que ele dá; 103 + 3n (B) soma o ganho de uma rodada a mais.</p>",
  figs(("q180", "Quatro círculos numerados de 1 a 4 dispostos num anel (1 em cima, 2 à direita, 3 embaixo, 4 à esquerda), com setas no sentido horário: de 1 para 2, de 2 para 3, de 3 para 4 e de 4 para 1.")),
  ["progressão aritmética", "expressão algébrica"], enun=ap(P(180)[0][1]) + "[[fig:1]]" + p(P(180)[2][1]) + LISTA(P(180)[3][1]) + p(P(180)[4][1].replace("rodada n", "rodada <em>n</em>")))

completar(Q, R)
