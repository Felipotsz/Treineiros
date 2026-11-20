# Enem 2004 (29/08/2004), Prova 1 — amarela: prova única de 63 questões (modelo antigo, sem divisão por áreas).
# Fonte do PDF: arquivo 'Provas_Gabaritos_ENEM_2004' do usuário. Gabarito: o da USP não estava acessível; usado o 'Gabarito 2004'
# do SlideShare (coluna Amarela), lido duas vezes, e conferido com uma resolução independente das questões. Em 11/11/2026 o usuário enviou 'Gabarito_Caderno_Amarelo_2004.pdf' (tabela Amarela/Branca/Rosa/Verde): as 63 respostas da coluna Amarela batem com as publicadas.
# Data: Correio do Povo, 21/03/2004 ("O Enem será aplicado no dia 29 de agosto").
# O extrator padrão não lê este layout; as alternativas vêm de alts.json (extrator próprio) e os enunciados são escritos aqui.
# Cada questão leva a grande área mais próxima. Poemas protegidos (Pedro Xisto Q18, Drummond Q26–27) como imagem;
# Oswald de Andrade (Q20–21) e Alberto Caeiro (Q59), de domínio público, em texto; prosa (Rubem Braga, Portinari) em texto.
import sys, pathlib, re, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar

ID = "enem-2004"
META = {"id": ID, "banca": "Enem", "ano": 2004, "titulo": "Enem 2004: Prova objetiva", "fonte": "Inep", "dataExame": "2004-08-29",
        "duracaoMinutos": 300, "area": "Prova objetiva (63 questões)", "caderno": "amarelo", "dia": 1, "fonteGabarito": {"oficial": False, "nome": "cópia do gabarito do caderno amarelo publicada no SlideShare, conferida com uma segunda cópia"}}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 64)}
D = {int(k): v for k, v in json.loads((pathlib.Path(__file__).resolve().parent / "alts.json").read_text(encoding="utf-8")).items()}
Q = {}
p = lambda *xs: "".join(f"<p>{x}</p>" for x in xs)
ap = lambda *xs: "".join(f'<p class="apoio">{x}</p>' for x in xs)
tit = lambda x: f'<p class="apoio"><strong>{x}</strong></p>'
fonte = lambda x: f'<p class="fonte">{x}</p>'
ALT = lambda ini: {k: f"[[fig:{i}]]" for i, k in enumerate("ABCDE", ini)}
A5 = lambda *xs: dict(zip("ABCDE", xs))
I3 = lambda *xs: '<ol type="I">' + "".join(f"<li>{x}</li>" for x in xs) + "</ol>"
AREAS = {"L": "Linguagens", "H": "Ciências Humanas", "N": "Ciências da Natureza", "M": "Matemática"}


def figs(*pares):
    return [{"arquivo": a, "alt": t} for a, t in pares]


def tabela(cab, linhas):
    return ('<table class="tabela"><thead><tr>' + "".join(f"<th>{c}</th>" for c in cab) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in l) + "</tr>" for l in linhas) + "</tbody></table>")


def QF(s):
    partes = re.split(r"(<[^>]+>)", s)
    return "".join(x if x.startswith("<") else re.sub(r"\b(CO|O|N|H|SO|NO)(\d)\b", r"\1<sub>\2</sub>", x) for x in partes)


def X(n, area, materia, assunto, expl, enun, imagens=(), tags=(), alts=None, quim=False):
    e = re.sub(r"<((?:www\.|http)[^<>]*)>", r"&lt;\1&gt;", enun)
    if quim: e = QF(e)
    al = dict(alts or D[n])
    assert sorted(al) == list("ABCDE"), (n, al)
    Q[n] = {"materia": materia, "assunto": assunto, "area": AREAS[area], "tags": list(tags), "numeroOriginal": n,
            "enunciado": e, "alternativas": {k: (QF(v) if quim else v) for k, v in al.items()},
            "imagens": list(imagens), "explicacao": expl}



# ---------------------------------------------------------------- 1–4: Olimpíadas
X(1, "M", "Matemática", "Leitura de gráficos", "<p>EUA, Rússia e China somam 40 + 32 + 28 = 100 medalhas de ouro, um terço das 300. Alternativa <strong>B</strong>.</p><p>Os 40 ouros dos EUA são 13%, e não cerca de um quarto (E); 171 medalhas ficaram com “outros” países, mas com 196 participantes nem todos ganharam ouro (A); e a Índia, muito populosa, não está entre os primeiros (C).</p>",
  p("As Olimpíadas são uma oportunidade para o congraçamento de um grande número de países, sem discriminação política ou racial, ainda que seus resultados possam refletir características culturais, socioeconômicas e étnicas. Em 2000, nos Jogos Olímpicos de Sydney, o total de 300 medalhas de ouro conquistadas apresentou a seguinte distribuição entre os 196 países participantes como mostra o gráfico.") + "[[fig:1]]"
  + p("Esses resultados mostram que, na distribuição das medalhas de ouro em 2000,"),
  figs(("q01", "Gráfico de barras “Distribuição das Medalhas de Ouro, Olimpíadas de Sydney - 2000”: EUA, 40; Rússia, 32; China, 28; Austrália, 16; Alemanha, 13; Outros, 171.")),
  ["Olimpíadas", "frações"])

X(2, "H", "Geografia", "Leitura de gráficos", "<p>Nas últimas cinco Olimpíadas (1984 a 2000), o número de homens oscilou pouco (6.434, 6.983, 6.659, 7.075, 6.416), enquanto o de mulheres subiu de 1.498 para 3.905. O aumento do total veio das mulheres. Alternativa <strong>E</strong>.</p><p>A participação masculina não “vem diminuindo a cada Olimpíada” (D): ela sobe e desce em torno do mesmo valor.</p>",
  p("O número de atletas nas Olimpíadas vem aumentando nos últimos anos, como mostra o gráfico. Mais de 10.000 atletas participaram dos Jogos Olímpicos de Sydney, em 2000.") + "[[fig:1]]"
  + p("Nas <u>últimas cinco Olimpíadas</u>, esse aumento ocorreu devido ao crescimento da participação de"),
  figs(("q02", "Gráfico de linhas do número de atletas nas Olimpíadas de 1960 a 2000, com três curvas. Total: 5.348, 5.140, 5.531, 7.247, 6.085, 5.353, 7.932, 9.421, 9.364, 10.624 e 10.321. Homens: 4.738, 4.457, 4.750, 5.848, 4.834, 4.265, 6.434, 6.983, 6.659, 7.075 e 6.416. Mulheres: 610, 683, 781, 1.299, 1.251, 1.088, 1.498, 2.438, 2.705, 3.549 e 3.905.")),
  ["Olimpíadas", "participação feminina"])

X(3, "H", "História", "Século XX", "<p>Em 1964, em Tóquio, a tocha foi acesa por Yoshinori Sakai, nascido em Hiroshima no dia da bomba atômica: o gesto lembrava a Segunda Guerra (conflito armado) e afirmava a reconstrução e a paz. Alternativa <strong>B</strong>.</p><p>Os boicotes de 1980 e 1956 e a exclusão de 1948 são manifestações de conflito, sem superação; e o episódio de 1936 se refere ao racismo nazista, não a uma guerra.</p>",
  p("Os Jogos Olímpicos tiveram início na Grécia, em 776 a.C., para celebrar uma declaração de paz. Na sociedade contemporânea, embora mantenham como ideal o congraçamento entre os povos, os Jogos Olímpicos têm sido palco de manifestações de conflitos políticos. Dentre os acontecimentos apresentados abaixo, o único que evoca um conflito armado e <u>sugere sua superação</u>, reafirmando o ideal olímpico, ocorreu"),
  tags=["Olimpíadas", "Hiroshima"])

X(4, "M", "Matemática", "Ângulos", "<p>Uma volta completa tem 360°. Então 900° = 2 × 360° + 180°, isto é, duas voltas e meia. Alternativa <strong>D</strong>.</p><p>Uma volta e meia seria 540° (B), duas voltas, 720° (C), e cinco voltas, 1.800° (E). O nome da manobra vem justamente da soma dos ângulos girados no ar.</p>",
  p("Nos <em>X-Games Brasil</em>, em maio de 2004, o skatista brasileiro Sandro Dias, apelidado “Mineirinho”, conseguiu realizar a manobra denominada “900”, na modalidade <em>skate</em> vertical, tornando-se o segundo atleta no mundo a conseguir esse feito. A denominação “900” refere-se ao número de graus que o atleta gira no ar em torno de seu próprio corpo, que, no caso, corresponde a"),
  tags=["graus", "skate"])

X(5, "H", "Geografia", "Amazônia", "<p>Na Amazônia Ocidental, ainda preservada, a estratégia é tirar renda da floresta em pé (II: fármacos, extratos, couros vegetais). A Amazônia Central, cortada pelo rio Amazonas, serve ao escoamento da soja (I: pavimentar rodovias até o rio). E no Arco do Povoamento Adensado, já desmatado, a soja deve ocupar as áreas abandonadas (III). Alternativa <strong>D</strong>.</p>",
  p("Em 2003, deu-se início às discussões do Plano Amazônia Sustentável, que rebatiza o Arco do Desmatamento, uma extensa faixa que vai de Rondônia ao Maranhão, como Arco do Povoamento Adensado, a fim de reconhecer as demandas da população que vive na região. A Amazônia Ocidental, em contraste, é considerada nesse plano como uma área ainda amplamente preservada, na qual se pretende encontrar alternativas para tirar mais renda da floresta em pé do que por meio do desmatamento. O quadro apresenta as três macrorregiões e três estratégias que constam do Plano.")
  + "[[fig:1]]" + p("<strong>Estratégias:</strong>")
  + I3("Pavimentação de rodovias para levar a soja até o rio Amazonas, por onde será escoada.", "Apoio à produção de fármacos, extratos e couros vegetais.",
       "Orientação para a expansão do plantio de soja, atraindo os produtores para áreas já desmatadas e atualmente abandonadas.")
  + p("Considerando as características geográficas da Amazônia, aplicam-se às macrorregiões Amazônia Ocidental, Amazônia Central e Arco do Povoamento Adensado, <u>respectivamente</u>, as estratégias"),
  figs(("q05", "Mapa do Brasil com a Amazônia dividida em três macrorregiões: a Amazônia Ocidental, a oeste; a Amazônia Central, no meio, ao longo do rio Amazonas; e o Arco do Povoamento Adensado, uma grande faixa curva no sul e no leste da região, de Rondônia ao Maranhão.")),
  ["Plano Amazônia Sustentável"])

X(6, "H", "Geografia", "Espaço agrário", "<p>No gráfico, arroz e feijão, alimentos básicos dos brasileiros, ficam quase constantes (cerca de 10 e 3 milhões de toneladas) de 1992 a 2004, enquanto soja e milho crescem. Alternativa <strong>A</strong>.</p><p>A soja passou de 20 para 58 milhões de toneladas (quase o triplo), crescendo mais que o milho, de 30 para 46 (C); e a soja, voltada à exportação e à ração, cresceu (D, E).</p>",
  p("A produção agrícola brasileira evoluiu, na última década, de forma diferenciada. No caso da cultura de grãos, por exemplo, verifica-se nos últimos anos um crescimento significativo da produção da soja e do milho, como mostra o gráfico.") + "[[fig:1]]"
  + p("Pelos dados do gráfico é possível verificar que, no período considerado,"),
  figs(("q06", "Gráfico de linhas da produção, em milhões de toneladas, de 1992 a 2004. Soja: de 20 em 1992 para cerca de 31 em 1998, 38 em 2001 e 58 em 2004. Milho: oscila entre 30 e 37 até 2000 e chega a 46 em 2004. Arroz: quase constante, perto de 10. Feijão: quase constante, perto de 3. Fonte: Ministério da Agricultura e Produção Agropecuária.")),
  ["soja", "produção de grãos"])

X(7, "H", "Geografia", "Cerrado", "<p>A soja ocupa grandes extensões de terra em monocultura, substituindo a vegetação nativa do Cerrado, um dos biomas mais ricos em espécies do país. A preocupação é ambiental: perda de biodiversidade. Alternativa <strong>E</strong>.</p><p>A soja é altamente mecanizada (A), expulsa e não atrai população para o campo (B) e é voltada justamente ao mercado externo (D).</p>",
  p("A grande produção brasileira de soja, com expressiva participação na economia do país, vem avançando nas regiões do Cerrado brasileiro. Esse tipo de produção demanda grandes extensões de terra, o que gera preocupação, sobretudo"),
  tags=["soja", "biodiversidade"])

X(8, "M", "Matemática", "Áreas", "<p>500 m de tecido com 1,40 m de largura são 700 m². A comissão é 700 × 0,50 = R$ 350, e o salário, 300 + 350 = R$ 650. No segundo mês, com o dobro (1.400 m²), a comissão é R$ 700, e o salário, R$ 1.000 (o fixo não dobra). Alternativa <strong>C</strong>.</p><p>D dobra também o salário fixo, e B usa os 500 m como se fossem metros quadrados.</p>",
  ap("<strong>VENDEDORES JOVENS</strong><br>Fábrica de LONAS – Vendas no Atacado<br>10 vagas para estudantes, 18 a 20 anos, sem experiência.<br>Salário: R$ 300,00 fixo + comissão de R$ 0,50 por m<sup>2</sup> vendido.<br>Contato: 0xx97-43421167 ou atacadista@lonaboa.com.br")
  + p("Na seleção para as vagas deste anúncio, feita por telefone ou correio eletrônico, propunha-se aos candidatos uma questão a ser resolvida na hora. Deveriam calcular seu salário no primeiro mês, se vendessem 500 m de tecido com largura de 1,40 m, e no segundo mês, se vendessem o dobro. Foram bem sucedidos os jovens que responderam, respectivamente,"),
  tags=["porcentagem", "área"])

X(9, "M", "Matemática", "Raciocínio lógico", "<p>Com D = 1,2%: D &gt; 5,0%? Não. D &gt; 3,0%? Não. Então escolhe a cor azul. D &gt; 1,0%? Sim: escreve “2ª Classe”. O selo sai “2ª Classe”, em azul. Alternativa <strong>D</strong>.</p><p>“1ª Classe” (E) só sairia para D ≤ 1,0%.</p>",
  p("Em uma fábrica de equipamentos eletrônicos, cada componente, ao final da linha de montagem, é submetido a um rigoroso controle de qualidade, que mede o desvio percentual (D) de seu desempenho em relação a um padrão ideal. O fluxograma a seguir descreve, passo a passo, os procedimentos executados por um computador para imprimir um selo em cada componente testado, classificando-o de acordo com o resultado do teste:")
  + "[[fig:1]]" + p("Os símbolos usados no fluxograma têm os seguintes significados:") + "[[fig:2]]"
  + p("Segundo essa rotina, se D = 1,2%, o componente receberá um selo com a classificação"),
  figs(("q09a", "Fluxograma: Início; entrar D; “D > 5,0%?”: se sim, escolher a cor vermelha e escrever “Rejeitado”; se não, “D > 3,0%?”: se sim, escolher a cor amarela e escrever “3ª Classe”; se não, escolher a cor azul e testar “D > 1,0%?”: se sim, escrever “2ª Classe”; se não, escrever “1ª Classe”. Todos os caminhos terminam em imprimir selo e Fim."),
       ("q09b", "Legenda dos símbolos: trapézio, entrada e saída de dados; losango, decisão (testa uma condição, executando operações diferentes caso essa condição seja verdadeira ou falsa); retângulo, operação.")),
  ["fluxograma"])

X(10, "M", "Matemática", "Razão e proporção", "<p>O valor cobrado é proporcional ao preço do quilo. Para corrigir, multiplica-se pela razão entre o preço certo e o errado: 12,80/18,20 ≈ 0,703, ou seja, cerca de 0,70. Alternativa <strong>C</strong>.</p><p>1,42 (E) é a razão inversa, que aumentaria ainda mais a conta.</p>",
  p("Em quase todo o Brasil existem restaurantes em que o cliente, após se servir, pesa o prato de comida e paga o valor correspondente, registrado na nota pela balança. Em um restaurante desse tipo, o preço do quilo era R$ 12,80. Certa vez a funcionária digitou por engano na balança eletrônica o valor R$ 18,20 e só percebeu o erro algum tempo depois, quando vários clientes já estavam almoçando. Ela fez alguns cálculos e verificou que o erro seria corrigido se o valor incorreto indicado na nota dos clientes fosse multiplicado por"),
  tags=["proporcionalidade"])

X(11, "N", "Química", "Lipídios", "<p>A margarina tem 65% de lipídios, e o creme vegetal, 35%. Em 200 g, são 130 g contra 70 g: 70/130 ≈ 0,54, aproximadamente a metade. Alternativa <strong>C</strong>.</p><p>Um terço (D) e um quarto (E) subestimam o teor de gordura do creme vegetal.</p>",
  p("As “margarinas” e os chamados “cremes vegetais” são produtos diferentes, comercializados em embalagens quase idênticas. O consumidor, para diferenciar um produto do outro, deve ler com atenção os dizeres do rótulo, geralmente em letras muito pequenas. As figuras que seguem representam rótulos desses dois produtos.") + "[[fig:1]]"
  + p("Uma função dos lipídios no preparo das massas alimentícias é torná-las mais macias. Uma pessoa que, por desatenção, use 200 g de creme vegetal para preparar uma massa cuja receita pede 200 g de margarina, não obterá a consistência desejada, pois estará utilizando uma quantidade de lipídios que é, em relação à recomendada, aproximadamente"),
  figs(("q11", "Dois rótulos lado a lado. Margarina: peso líquido 500 g, 65% de lipídios, valor energético por porção de 10 g: 59 kcal. Creme vegetal: peso líquido 500 g, 35% de lipídios, valor energético por porção de 10 g: 32 kcal, não recomendado para uso culinário.")),
  ["rótulos", "porcentagem"])

X(12, "M", "Matemática", "Escala e orientação", "<p>O anúncio pede 200 m² e frente voltada para o sol da manhã, isto é, para o leste. Pela escala, o terreno IV mede 20 m × 10 m = 200 m² e sua frente dá para a Rua das Rosas, a leste dele. Alternativa <strong>D</strong>.</p><p>O terreno II também fica junto à Rua das Rosas, mas tem outra área; I, III e V não têm frente para o leste ou não somam 200 m².</p>",
  p("Um leitor encontra o seguinte anúncio entre os classificados de um jornal:")
  + ap("<strong>VILA DAS FLORES</strong><br>Vende-se terreno plano medindo 200 m<sup>2</sup>. Frente voltada para o sol no período da manhã. Fácil acesso.<br>(443)0677-0032")
  + p("Interessado no terreno, o leitor vai ao endereço indicado e, lá chegando, observa um painel com a planta a seguir, onde estavam destacados os terrenos ainda não vendidos, numerados de I a V:")
  + "[[fig:1]]" + p("Considerando as informações do jornal, é possível afirmar que o terreno anunciado é o"),
  figs(("q12", "Planta de duas quadras com o norte para cima e escala de 0, 10 e 20 m. Ruas: dos Cravos (norte), das Hortênsias (sul), dos Jasmins (oeste), das Rosas (entre as quadras) e das Margaridas (leste). Na quadra da esquerda: terreno I, quadrado, junto à Rua dos Jasmins; terreno II, junto à Rua das Rosas, mais alto que largo; terreno IV, junto à Rua das Rosas, perto da Rua das Hortênsias, mais largo que alto (cerca de 20 m por 10 m). Na quadra da direita: terreno III, estreito, junto à Rua das Rosas no alto; terreno V, junto à Rua das Margaridas.")),
  ["escala", "pontos cardeais"])

X(13, "M", "Matemática", "Análise combinatória", "<p>Fundo azul: a casa pode ser verde ou amarela (2) e a palmeira, cinza ou verde (2): 4 variações. Fundo cinza: a casa pode ser azul, verde ou amarela (3) e a palmeira só verde (1): 3 variações. Total: 4 + 3 = 7. Alternativa <strong>B</strong>.</p><p>Sem a restrição de contraste, seriam 2 × 3 × 2 = 12.</p>",
  p("No Nordeste brasileiro, é comum encontrarmos peças de artesanato constituídas por garrafas preenchidas com areia de diferentes cores, formando desenhos. Um artesão deseja fazer peças com areia de cores cinza, azul, verde e amarela, mantendo o mesmo desenho, mas variando as cores da paisagem (casa, palmeira e fundo), conforme a figura.") + "[[fig:1]]"
  + p("O fundo pode ser representado nas cores azul ou cinza; a casa, nas cores azul, verde ou amarela; e a palmeira, nas cores cinza ou verde. Se o fundo não pode ter a mesma cor nem da casa nem da palmeira, por uma questão de contraste, então o número de variações que podem ser obtidas para a paisagem é"),
  figs(("q13", "Desenho de uma garrafa com areia formando uma paisagem: uma palmeira, uma casinha e o fundo, indicado com a palavra “fundo”.")),
  ["princípio multiplicativo"])

X(14, "M", "Matemática", "Vasos comunicantes", "<p>Pelo princípio dos vasos comunicantes, a água fica no mesmo nível nas duas varas, e a diferença das leituras (L<sub>I</sub> − L<sub>II</sub>) é quanto o segundo ponto está acima do primeiro. P2 está 75 cm acima de P1; P3, 25 cm abaixo de P2; P4, 55 cm acima de P3. Tomando P1 = 0: P2 = 75, P3 = 50, P4 = 105. O perfil sobe, desce um pouco e sobe acima do primeiro pico. Alternativa <strong>A</strong>.</p>",
  p("Para medir o perfil de um terreno, um mestre-de-obras utilizou duas varas (V<sub>I</sub> e V<sub>II</sub>), iguais e igualmente graduadas em centímetros, às quais foi acoplada uma mangueira plástica transparente, parcialmente preenchida por água (figura abaixo). Ele fez 3 medições que permitiram levantar o perfil da linha que contém, em seqüência, os pontos P<sub>1</sub>, P<sub>2</sub>, P<sub>3</sub> e P<sub>4</sub>. Em cada medição, colocou as varas em dois diferentes pontos e anotou suas leituras na tabela a seguir. A figura representa a primeira medição entre P<sub>1</sub> e P<sub>2</sub>.")
  + "[[fig:1]]"
  + tabela(["Medição", "Vara I", "L<sub>I</sub>", "Vara II", "L<sub>II</sub>", "L<sub>I</sub> − L<sub>II</sub>"],
           [["1ª", "P<sub>1</sub>", "239", "P<sub>2</sub>", "164", "75"], ["2ª", "P<sub>2</sub>", "189", "P<sub>3</sub>", "214", "−25"], ["3ª", "P<sub>3</sub>", "229", "P<sub>4</sub>", "174", "55"]])
  + fonte("Leituras e diferença em centímetros.") + p("Ao preencher completamente a tabela, o mestre-de-obras determinou o seguinte perfil para o terreno:"),
  figs(("q14", "Figura da primeira medição: duas varas verticais, V1 em P1 e V2 em P2, ligadas por uma mangueira com água; o nível de água na mangueira marca 239 cm na vara de P1 e 164 cm na de P2, que está num ponto mais alto do terreno. Mais adiante, P3 e P4, com a indicação “terreno fora de escala”."),
       ("q14a", "Perfil de P1 a P4: sobe até um pico em P2, desce um pouco até P3 e sobe até P4, acima do primeiro pico."),
       ("q14b", "Perfil de P1 a P4: sobe até o ponto mais alto perto de P3 e desce até P4."),
       ("q14c", "Perfil de P1 a P4: quase plano até P2, sobe até um pico em P3 e desce um pouco até P4."),
       ("q14d", "Perfil de P1 a P4: sobe até P2, desce muito até P3 e sobe bastante até P4."),
       ("q14e", "Perfil de P1 a P4: sobe até P2, fica quase plano até P3 e sobe até P4.")),
  ["vasos comunicantes", "perfil topográfico"], alts=ALT(2))

X(15, "M", "Matemática", "Áreas", "<p>Na chapa de 2 m, a tampa grande tem raio 1 m (área π); as 4 médias têm raio 0,5 m (área 4 × π/4 = π); as 16 pequenas, raio 0,25 m (área 16 × π/16 = π). Em todos os casos a chapa de 4 m² perde 4 − π ≈ 0,86 m². Como se produz 1 grande para 4 médias e 16 pequenas (uma chapa de cada), as sobras são iguais. Alternativa <strong>E</strong>.</p>",
  p("Uma empresa produz tampas circulares de alumínio para tanques cilíndricos a partir de chapas quadradas de 2 metros de lado, conforme a figura. Para 1 tampa grande, a empresa produz 4 tampas médias e 16 tampas pequenas.") + "[[fig:1]]"
  + p("As sobras de material da produção diária das tampas grandes, médias e pequenas dessa empresa são doadas, respectivamente, a três entidades: I, II e III, para efetuarem reciclagem do material. A partir dessas informações, pode-se concluir que"),
  figs(("q15", "Três chapas quadradas de 2 m de lado: a “grande” com um círculo que toca os quatro lados; a “média” com 4 círculos iguais (2 por 2); a “pequena” com 16 círculos iguais (4 por 4). Ao lado, “Área do círculo: πr²”.")),
  ["área do círculo"])

X(16, "M", "Matemática", "Conjuntos", "<p>Pelo princípio da inclusão e exclusão: 50 + 45 + 40 − 10 − 6 − 5 + 4 = 118 originais. As páginas comuns aos pares foram subtraídas, e as 4 comuns aos três, que tinham sido descontadas três vezes, voltam uma vez. Alternativa <strong>C</strong>.</p><p>Somando tudo dá 135 (A); subtraindo as interseções sem devolver as 4, 114 (D).</p>",
  p("Um fabricante de cosméticos decide produzir três diferentes catálogos de seus produtos, visando a públicos distintos. Como alguns produtos estarão presentes em mais de um catálogo e ocupam uma página inteira, ele resolve fazer uma contagem para diminuir os gastos com originais de impressão. Os catálogos C<sub>1</sub>, C<sub>2</sub> e C<sub>3</sub> terão, respectivamente, 50, 45 e 40 páginas. Comparando os projetos de cada catálogo, ele verifica que C<sub>1</sub> e C<sub>2</sub> terão 10 páginas em comum; C<sub>1</sub> e C<sub>3</sub> terão 6 páginas em comum; C<sub>2</sub> e C<sub>3</sub> terão 5 páginas em comum, das quais 4 também estarão em C<sub>1</sub>.",
    "Efetuando os cálculos correspondentes, o fabricante concluiu que, para a montagem dos três catálogos, necessitará de um total de originais de impressão igual a:"),
  tags=["inclusão e exclusão"])

X(17, "M", "Matemática", "Estatística", "<p>Com margem de 3 pontos, X pode ter de 33% a 39%; Y, de 30% a 36%; Z, de 28% a 34%. Z vence no máximo com 34% contra 33% de X, uma diferença de 1 ponto. Alternativa <strong>D</strong>.</p><p>Os três têm chance, porque os intervalos se sobrepõem (A, B); Y vence X por no máximo 3 pontos (C), e Z vence Y por no máximo 4 pontos (E).</p>",
  p("Antes de uma eleição para prefeito, certo instituto realizou uma pesquisa em que foi consultado um número significativo de eleitores, dos quais 36% responderam que iriam votar no candidato X; 33%, no candidato Y e 31%, no candidato Z. A margem de erro estimada para cada um desses valores é de 3% para mais ou para menos. Os técnicos do instituto concluíram que, se confirmado o resultado da pesquisa,"),
  tags=["margem de erro", "pesquisa eleitoral"])

X(18, "L", "Literatura", "Poesia concreta", "<p>O poema usa letras e o “&amp;” como símbolos: “he” (ele), “&amp;” (e) e “She” (ela) formam o casal, e a forma do S lembra a serpente, com o “h” do homem e o “e” de Eva, retomando o mito do Gênesis. Os sinais deixam de ser só objetivos e ganham novos sentidos. Alternativa <strong>A</strong>.</p><p>Eles não eliminam a subjetividade (B) nem contrariam o tema do casamento (C).</p>",
  p("O poema abaixo pertence à poesia concreta brasileira. O termo latino de seu título significa “epitalâmio”, poema ou canto em homenagem aos que se casam.") + "[[fig:1]]"
  + p("Considerando que símbolos e sinais são utilizados geralmente para demonstrações objetivas, ao serem incorporados no poema “Epithalamium - II”,"),
  figs(("q18", "Poema concreto “Epithalamium – II”, de Pedro Xisto: um grande sinal “&amp;” desenhado de modo que contém um “h” na curva de cima e um “e” na de baixo, formando também um “S”. Abaixo, as chaves de leitura: “he = ele”, “&amp; = e”, “She = ela”, “S = serpens”, “h = homo”, “e = eva”.")),
  ["Pedro Xisto", "poesia concreta"])

X(19, "L", "Língua Portuguesa", "Interpretação de tirinha", "<p>Os amigos concordam que a humanidade deve ir “para a frente”, mas, ao apontar a direção, cada um indica um lado diferente e começam a brigar. A concordância era só aparente: a tira revela a dificuldade de entendimento entre posições que pareciam convergir. Alternativa <strong>A</strong>.</p><p>Não há entendimento ao final (C, D), e o conflito não é entre visões masculina e feminina (E).</p>",
  "[[fig:1]]" + p("A conversa entre Mafalda e seus amigos"),
  figs(("q19", "Tira de Mafalda, de Quino, em quatro quadros. Mafalda pergunta: “Para onde vocês acham que a humanidade está indo?”. Um menino responde: “Para a frente, é cla...”; outro o interrompe, apontando para outro lado: “A frente é pra lá!”. No último quadro, os dois discutem (“Lá não é frente!”, “Mas é a minha frente!”, “A tua frente não é a minha frente!”, “Não!”), e Mafalda, à parte, pensa: “Estou começando a entender por que é tão difícil a humanidade ir para a frente”.")),
  ["Mafalda"])

BRASIL = (tit("Texto para as questões 20 e 21.") + tit("Brasil")
  + ap("O Zé Pereira chegou de caravela<br>E preguntou pro guarani da mata virgem<br>― Sois cristão?<br>― Não. Sou bravo, sou forte, sou filho da Morte<br>Teterê tetê Quizá Quizá Quecê!<br>Lá longe a onça resmungava Uu! ua! uu!<br>O negro zonzo saído da fornalha<br>Tomou a palavra e respondeu<br>― Sim pela graça de Deus<br>Canhem Babá Canhem Babá Cum Cum!<br>E fizeram o Carnaval")
  + fonte("Oswald de Andrade."))
X(20, "L", "Literatura", "Modernismo", "<p>O poema mostra a formação do Brasil como uma mistura desencontrada (o português pergunta, o índio recusa, o negro responde “zonzo”), mas termina em festa: “E fizeram o Carnaval”. A visão é ambígua: aponta o caráter desconjuntado e sugere que, apesar de tudo, o processo acaba bem. Alternativa <strong>A</strong>.</p><p>O texto não diz que as três raças pouco contribuíram (B), não é moralizante (C) nem trata a mistura como anarquia (E).</p>",
  BRASIL + p("Este texto apresenta uma versão humorística da formação do Brasil, mostrando-a como uma junção de elementos diferentes. Considerando-se esse aspecto, é correto afirmar que a visão apresentada pelo texto é"),
  tags=["Oswald de Andrade", "identidade nacional"])
X(21, "L", "Literatura", "Modernismo", "<p>Falam no poema o narrador (o poeta, que conta a cena e conclui “E fizeram o Carnaval”), o colonizador (Zé Pereira: “Sois cristão?”), o índio (“Não. Sou bravo...”) e o negro (“Sim pela graça de Deus”). São quatro vozes. Alternativa <strong>E</strong>.</p><p>A onça também “resmunga”, mas não é uma das vozes humanas da polifonia.</p>",
  BRASIL + p("A polifonia, variedade de vozes, presente no poema resulta da manifestação do"),
  tags=["polifonia", "Oswald de Andrade"])

X(22, "L", "Literatura", "Crônica", "<p>O assunto é uma informação colhida (a conversa contada pelo Sr. Matter a um jornal); o modo é a narrativa sugestiva, que mostra a cena e deixa o leitor tirar a conclusão; e a finalidade é a reflexão, pois a resposta do índio inverte quem parece “selvagem” e questiona a moral do explorador. Alternativa <strong>B</strong>.</p><p>O texto tem humor, mas o riso leva a pensar sobre a violência e a hipocrisia.</p>",
  tit("O jivaro") + ap("Um Sr. Matter, que fez uma viagem de exploração à América do Sul, conta a um jornal sua conversa com um índio jivaro, desses que sabem reduzir a cabeça de um morto até ela ficar bem pequenina. Queria assistir a uma dessas operações, e o índio lhe disse que exatamente ele tinha contas a acertar com um inimigo.",
     "O Sr. Matter:<br>― Não, não! Um homem, não. Faça isso com a cabeça de um macaco.<br>E o índio:<br>― Por que um macaco? Ele não me fez nenhum mal!") + fonte("Rubem Braga.")
  + p("O assunto de uma crônica pode ser uma experiência pessoal do cronista, uma informação obtida por ele ou um caso imaginário. O modo de apresentar o assunto também varia: pode ser uma descrição objetiva, uma exposição argumentativa ou uma narrativa sugestiva. Quanto à finalidade pretendida, pode-se promover uma reflexão, definir um sentimento ou tão-somente provocar o riso. Na crônica <em>O jivaro</em>, escrita a partir da reportagem de um jornal, Rubem Braga se vale dos seguintes elementos:"),
  tags=["Rubem Braga", "crônica"],
  alts={k: f"Assunto: {a}; modo de apresentar: {b}; finalidade: {c}." for k, (a, b, c) in {
      "A": ("caso imaginário", "descrição objetiva", "provocar o riso"), "B": ("informação colhida", "narrativa sugestiva", "promover reflexão"),
      "C": ("informação colhida", "descrição objetiva", "definir um sentimento"), "D": ("experiência pessoal", "narrativa sugestiva", "provocar o riso"),
      "E": ("experiência pessoal", "exposição argumentativa", "promover reflexão")}.items()})

X(23, "L", "Artes", "Artes visuais", "<p>O texto de Portinari descreve pés de trabalhadores, deformados, sofridos, “como alicerces”. A imagem E, uma fotografia de pés calejados e deformados em chinelos, mostra exatamente isso. Alternativa <strong>E</strong>.</p><p>A e B remetem às fantasias e ao homem americano dos cronistas e viajantes; C mostra trabalhadores numa composição estilizada, sem o foco no corpo sofrido; e D mostra pernas e pés de pessoas sentadas, sem as marcas do trabalho.</p>",
  p("Cândido Portinari (1903-1962), em seu livro <em>Retalhos de Minha Vida de Infância</em>, descreve os pés dos trabalhadores.")
  + ap("Pés disformes. Pés que podem contar uma história. Confundiam-se com as pedras e os espinhos. Pés semelhantes aos mapas: com montes e vales, vincos como rios. (...) Pés sofridos com muitos e muitos quilômetros de marcha. Pés que só os santos têm. Sobre a terra, difícil era distingui-los. Agarrados ao solo, eram como alicerces, muitas vezes suportavam apenas um corpo franzino e doente.")
  + fonte("Cândido Portinari, <em>Retrospectiva</em>, Catálogo MASP.")
  + p("As fantasias sobre o Novo Mundo, a diversidade da natureza e do homem americano e a crítica social foram temas que inspiraram muitos artistas ao longo de nossa História. Dentre estas imagens, a que melhor caracteriza a crítica social contida no texto de Portinari é"),
  figs(("q23a", "Gravura antiga: uma figura nua deitada, retorcida, numa paisagem de mata."),
       ("q23b", "Gravura de viajante: um indígena deitado de costas atira com um grande arco preso pelos pés, numa paisagem com cactos."),
       ("q23c", "Pintura estilizada em tons de cinza: dois trabalhadores, um homem e uma mulher, carregam baldes junto a uma máquina."),
       ("q23d", "Fotografia de pernas e pés de pessoas sentadas em banquinhos, de roupas simples."),
       ("q23e", "Fotografia em close de pés descalços em chinelos, grossos, calejados e deformados, sobre o chão de terra e pedras.")),
  ["Portinari", "crítica social"], alts=ALT(1))

X(24, "L", "Artes", "Cultura popular", "<p>O texto apresenta o hip-hop como discurso “a favor dos excluídos, sobretudo dos negros” e como movimento formado por três linguagens (música, artes plásticas e dança), que no Brasil se mistura a samba e capoeira. Alternativa <strong>C</strong>.</p><p>O movimento é político e de resistência, não alienado (B); não integra classes nem exalta o progresso (D); e não se baseia em nacionalismo ou em ideais norte-americanos (A, E).</p>",
  ap("O movimento hip-hop é tão urbano quanto as grandes construções de concreto e as estações de metrô, e cada dia se torna mais presente nas grandes metrópoles mundiais. Nasceu na periferia dos bairros pobres de Nova Iorque. É formado por três elementos: a música (o <em>rap</em>), as artes plásticas (o grafite) e a dança (o <em>break</em>). No hip-hop os jovens usam as expressões artísticas como uma forma de resistência política.",
     "Enraizado nas camadas populares urbanas, o hip-hop afirmou-se no Brasil e no mundo com um discurso político a favor dos excluídos, sobretudo dos negros. Apesar de ser um movimento originário das periferias norte-americanas, não encontrou barreiras no Brasil, onde se instalou com certa naturalidade – o que, no entanto, não significa que o hip-hop brasileiro não tenha sofrido influências locais. O movimento no Brasil é híbrido: <em>rap</em> com um pouco de samba, <em>break</em> parecido com capoeira e grafite de cores muito vivas.")
  + fonte("Adaptado de <em>Ciência e Cultura</em>, 2004.")
  + p("De acordo com o texto, o hip-hop é uma manifestação artística tipicamente urbana, que tem como principais características"),
  tags=["hip-hop"])

X(25, "L", "Língua Portuguesa", "Figuras de linguagem", "<p>O menino diz que o pai pedala a bicicleta ergométrica “mas nunca vai a lugar nenhum” e conclui: “Deve ser uma metáfora da existência dele”. A metáfora critica a vida sem rumo, sem perspectiva, do pai. Alternativa <strong>E</strong>.</p><p>A tira não condena o exercício (A) nem desestimula a bicicleta (C); o humor está na crítica ao pai.</p>",
  "[[fig:1]]" + p("Nesta tirinha, a personagem faz referência a uma das mais conhecidas figuras de linguagem para"),
  figs(("q25", "Tira “Frank e Ernest”, de Bob Thaves: ao lado de uma bicicleta ergométrica, um menino comenta com outro: “Meu pai fica pedalando essa bicicleta, mas nunca vai a lugar nenhum. Deve ser uma metáfora da existência dele.”")),
  ["metáfora", "tirinha"], alts=dict(D[25], E="criticar a falta de perspectiva do pai."))

CIDADE = tit("Texto para as questões 26 e 27.") + "[[fig:1]]"
F_CIDADE = figs(("q26", "Poema “Cidade grande”, de Carlos Drummond de Andrade, em oito versos: o eu lírico exalta a beleza, o crescimento e a indústria de Montes Claros e diz que a cidade cresceu tanto, ficou tão notória, prima-rica do Rio de Janeiro, que já tem cinco favelas, “por enquanto, e mais promete”."))
X(26, "L", "Literatura", "Figuras de linguagem", "<p>O poema elogia o crescimento de Montes Claros para concluir que a cidade “já tem cinco favelas / por enquanto, e mais promete”: o elogio esconde uma crítica ao crescimento desigual. É ironia. Alternativa <strong>C</strong>.</p><p>O texto não fala da própria linguagem (A), não retoma outro texto (B), não é só denotativo (D) e não personifica a cidade (E).</p>",
  CIDADE + p("Entre os recursos expressivos empregados no texto, destaca-se a"), F_CIDADE, ["ironia", "Drummond"])
X(27, "L", "Língua Portuguesa", "Orações consecutivas", "<p>Em D, “tão pegada, aconchegada nos meus braços, / que rio e danço” tem a mesma estrutura de “cresceu tanto... que já tem”: intensidade (tão/tanto) seguida de oração introduzida por “que” com a consequência. Alternativa <strong>D</strong>.</p><p>Nas outras, “que” é integrante (A), relativo (B, E) ou comparativo (C, “mais que”).</p>",
  CIDADE + p("No trecho “Montes Claros cresceu tanto,/ (...),/ que já tem cinco favelas”, a palavra <u>que</u> contribui para estabelecer uma relação de conseqüência. Dos seguintes versos, todos de Carlos Drummond de Andrade, apresentam esse mesmo tipo de relação:"),
  F_CIDADE + figs(("q27a", "“Meu Deus, por que me abandonaste / se sabias que eu não era Deus / se sabias que eu era fraco.”, com o primeiro “que” sublinhado."),
                  ("q27b", "“No meio-dia branco de luz uma voz que aprendeu / a ninar nos longes da senzala – e nunca se esqueceu / chamava para o café.”, com o “que” sublinhado."),
                  ("q27c", "“Teus ombros suportam o mundo / e ele não pesa mais que a mão de uma criança.”, com o “que” sublinhado."),
                  ("q27d", "“A ausência é um estar em mim. / E sinto-a, branca, tão pegada, aconchegada nos meus braços, / que rio e danço e invento exclamações alegres.”, com o “que” sublinhado."),
                  ("q27e", "“Penetra surdamente no reino das palavras. / Lá estão os poemas que esperam ser escritos.”, com o “que” sublinhado.")),
  ["conjunção consecutiva", "Drummond"], alts=ALT(2))

X(28, "H", "Geografia", "Demografia", "<p>Os gráficos mostram a população urbana passando a superar a rural e chegando a cerca de 80% em 2000, enquanto a fecundidade cai de cerca de 6 para cerca de 2 filhos por mulher. Urbanização e queda da fecundidade andam juntas. Alternativa <strong>E</strong>.</p><p>As demais invertem a relação: quando predominava a população rural, as mulheres tinham cerca de três vezes mais filhos, e não menos (B).</p>",
  p("Ao longo do século XX, as características da população brasileira mudaram muito. Os gráficos mostram as alterações na distribuição da população da cidade e do campo e na taxa de fecundidade (número de filhos por mulher) no período entre 1940 e 2000.") + "[[fig:1]]" + fonte("IBGE")
  + p("Comparando-se os dados dos gráficos, pode-se concluir que"),
  figs(("q28", "Dois gráficos de barras. “População urbana e rural no Brasil (%)”: 1940, 30% urbana e 70% rural; 1950, 40% e 62%; 1960, 47% e 55%; 1970, 60% e 41%; 1980, 70% e 32%; 1991, 72% e 30%; 2000, 82% e 18%. “Taxa de fecundidade no Brasil”: 6,2 filhos por mulher em 1940 e 1950, 6,3 em 1960, 5,8 em 1970, 4,5 em 1980, 3,0 em 1990 e 2,1 em 2000.")),
  ["urbanização", "fecundidade"])

X(29, "N", "Biologia", "Saúde pública", "<p>No diagrama, as doenças infecto-parasitárias caem de 45,6% das mortes em 1930 para 4,6% em 2002, graças ao saneamento, às vacinas e aos antibióticos. Alternativa <strong>B</strong>.</p><p>O êxodo rural não as eliminou (A); as digestivas sempre foram pequena parcela (C, D); e as respiratórias caíram pouco, de 11,5% para 9,6%, sem nunca terem sido predominantes (E).</p>",
  p("Algumas doenças que, durante várias décadas do século XX, foram responsáveis pelas maiores percentagens das mortes no Brasil, não são mais significativas neste início do século XXI. No entanto, aumentou o percentual de mortalidade devida a outras doenças, conforme se pode observar no diagrama:") + "[[fig:1]]"
  + p("No período considerado no diagrama, deixaram de ser predominantes, como causas de morte, as doenças"),
  figs(("q29", "Diagrama em faixas da porcentagem das causas de morte no Brasil de 1930 a 2002: infecto-parasitárias, de 45,6% para 4,6%; outras causas, de 21,3% para 27,8%; circulatórias, de 11,8% para 27,2%; respiratórias, de 11,5% para 9,6%; digestivas, de 4,5% para 4,7%; câncer, de 2,7% para 13,2%; causas externas, de 2,6% para 12,9%. Fonte: MS/SVS/DASIS.")),
  ["mortalidade", "doenças infecciosas"])

X(30, "H", "Geografia", "População economicamente ativa", "<p>O gráfico mostra a PEA agropecuária caindo de cerca de 70% em 1940 para pouco mais de 20% em 2000, enquanto crescem a indústria e, sobretudo, o comércio e serviços. A urbanização e a mecanização do campo deslocaram os postos de trabalho. Alternativa <strong>D</strong>.</p><p>A produção agrícola não caiu (A), e o setor terciário cresceu em vez de perder postos (C, E).</p>",
  "[[fig:1]]" + p("A distribuição da População Economicamente Ativa (PEA) no Brasil variou muito ao longo do século XX. O gráfico representa a distribuição por setores de atividades (em %) da PEA brasileira em diferentes décadas.",
                  "As transformações socioeconômicas ocorridas ao longo do século XX, no Brasil, mudaram a distribuição dos postos de trabalho do setor"),
  figs(("q30", "Gráfico de barras do percentual da PEA por setor em 1940, 1960, 1980 e 2000. Agropecuária: cerca de 70%, 54%, 30% e 24%. Indústria: cerca de 10%, 13%, 25% e 20%. Comércio e serviços: cerca de 20%, 33%, 45% e 58%. Fonte: IBGE.")),
  ["setores da economia"])

X(31, "N", "Biologia", "Evolução", "<p>As mutações que dão resistência surgem ao acaso. O antibiótico mata as bactérias sensíveis e deixa as resistentes se multiplicarem: é seleção natural. O uso incorreto do remédio acelera esse processo. Alternativa <strong>B</strong>.</p><p>O antibiótico não causa a mutação “para” a bactéria se adaptar (C), e as bactérias não transformam o antibiótico em alimento (A).</p>",
  p("O que têm em comum Noel Rosa, Castro Alves, Franz Kafka, Álvares de Azevedo, José de Alencar e Frédéric Chopin?",
    "Todos eles morreram de tuberculose, doença que ao longo dos séculos fez mais de 100 milhões de vítimas. Aparentemente controlada durante algumas décadas, a tuberculose voltou a matar. O principal obstáculo para seu controle é o aumento do número de linhagens de bactérias resistentes aos antibióticos usados para combatê-la. Esse aumento do número de linhagens resistentes se deve a"),
  tags=["resistência bacteriana", "tuberculose"])

X(32, "H", "Geografia", "IDH", "<p>De 1991 para 2000, o IDH-Longevidade e o IDH-Educação subiram nos três municípios, mas o IDH-Renda caiu em X (0,431 → 0,402) e em Z (0,501 → 0,420). Só as políticas de saúde (II) e educação (III) são compatíveis com os resultados nos três. Alternativa <strong>D</strong>.</p>",
  p("O Índice de Desenvolvimento Humano (IDH) permite avaliar as condições de qualidade de vida e de desenvolvimento de um país, de uma região ou de uma cidade, a partir de seus indicadores de renda, longevidade e educação. Cada indicador varia de 0 (nenhum desenvolvimento) a 1 (desenvolvimento máximo). A tabela apresenta os valores de IDH de três municípios brasileiros, X, Y e Z, medidos nos anos de 1991 e 2000.")
  + tabela(["Indicador", "Município", "1991", "2000"], [['IDH – Renda', 'X', '0,431', '0,402'], ['IDH – Renda', 'Y', '0,374', '0,379'], ['IDH – Renda', 'Z', '0,501', '0,420'], ['IDH – Longevidade', 'X', '0,456', '0,551'], ['IDH – Longevidade', 'Y', '0,459', '0,548'], ['IDH – Longevidade', 'Z', '0,611', '0,648'], ['IDH – Educação', 'X', '0,328', '0,568'], ['IDH – Educação', 'Y', '0,422', '0,634'], ['IDH – Educação', 'Z', '0,188', '0,448']])
  + fonte("Atlas do Desenvolvimento Humano no Brasil.")
  + p("Mudanças desses indicadores de IDH podem ser obtidas com a implantação de políticas públicas tais como:")
  + I3("Expansão dos empregos com melhoria de renda média.", "Ações de promoção de saúde e de prevenção de doenças.", "Ampliação de escolas de ensino básico e de educação de jovens e adultos.")
  + p("Os resultados apresentados em 2000 são compatíveis com a implementação bem sucedida em todos esses três municípios, ao longo da década de noventa, das políticas"),
  tags=["IDH", "leitura de tabela"])

X(33, "M", "Matemática", "Porcentagem", "<p>A família de menor renda gasta 33% de R$ 400 com alimentação: R$ 132. A de maior renda gasta 9% de R$ 6.000: R$ 540. Como 540/132 ≈ 4,1, o gasto é cerca de quatro vezes maior. Alternativa <strong>B</strong>.</p><p>Comparar só as porcentagens (9% contra 33%) leva a crer, erradamente, que a família rica gasta menos (D).</p>",
  p("Uma pesquisa sobre orçamentos familiares, realizada recentemente pelo IBGE, mostra alguns itens de despesa na distribuição de gastos de dois grupos de famílias com rendas mensais bem diferentes.")
  + tabela(["Tipo de despesa", "Renda até R$ 400,00", "Renda maior ou igual a R$ 6.000,00"],
           [["Habitação", "37%", "23%"], ["Alimentação", "33%", "9%"], ["Transporte", "8%", "17%"], ["Saúde", "4%", "6%"], ["Educação", "0,3%", "5%"], ["Outros", "17,7%", "40%"]])
  + p("Considere duas famílias com rendas de R$ 400,00 e R$ 6.000,00, respectivamente, cujas despesas variam de acordo com os valores das faixas apresentadas. Nesse caso, os valores, em R$, gastos com alimentação pela família de maior renda, em relação aos da família de menor renda, são, aproximadamente,"),
  tags=["porcentagem", "orçamento familiar"])

X(34, "N", "Química", "Água", "<p>A água de reuso não é potável, então não deve ser ingerida nem ter contato direto com o corpo ou com alimentos e remédios. O uso adequado é o urbano, em lavagem de ruas e áreas públicas. Alternativa <strong>E</strong>.</p><p>Lançá-la em mananciais (C) contaminaria fontes de água potável.</p>",
  p("A necessidade de água tem tornado cada vez mais importante a reutilização planejada desse recurso. Entretanto, os processos de tratamento de águas para seu reaproveitamento nem sempre as tornam potáveis, o que leva a restrições em sua utilização. Assim, dentre os possíveis empregos para a denominada “água de reuso”, recomenda-se"),
  tags=["água de reuso"])

X(35, "H", "Geografia", "Recursos hídricos", "<p>O aquífero é contaminado nas áreas de recarga, onde o arenito aflora e absorve a água da chuva com os agrotóxicos. Controlar a atividade agrícola nessas áreas protege o aquífero sem paralisar a economia. Alternativa <strong>E</strong>.</p><p>Proibir a agricultura em toda a região (B) ou impermeabilizar as áreas de afloramento (C) desconsideraria as necessidades econômicas e impediria a recarga.</p>",
  "[[fig:1]]" + p("O Aqüífero Guarani se estende por 1,2 milhão de km<sup>2</sup> e é um dos maiores reservatórios de águas subterrâneas do mundo. O aqüífero é como uma “esponja gigante” de arenito, uma rocha porosa e absorvente, quase totalmente confinada sob centenas de metros de rochas impermeáveis. Ele é recarregado nas áreas em que o arenito aflora à superfície, absorvendo água da chuva. Uma pesquisa realizada em 2002 pela Embrapa apontou cinco pontos de contaminação do aqüífero por agrotóxico, conforme a figura.",
                  "Considerando as conseqüências socioambientais e respeitando as necessidades econômicas, pode-se afirmar que, diante do problema apresentado, políticas públicas adequadas deveriam"),
  figs(("q35", "Mapa do Aquífero Guarani, que se estende pelo centro-sul do Brasil e por partes do Paraguai, da Argentina e do Uruguai. Faixas escuras, nas bordas do aquífero em território brasileiro, marcam as áreas de recarga, e cinco círculos com X marcam as áreas com risco de contaminação, todas sobre ou junto a essas faixas.")),
  ["Aquífero Guarani", "agrotóxicos"])

X(36, "N", "Física", "Ciclo da água", "<p>A água que os rios despejam é compensada pela evaporação nos oceanos; o vapor forma nuvens que se deslocam e chovem sobre os continentes, alimentando os rios: é o ciclo da água. Alternativa <strong>A</strong>.</p><p>A água doce não “diminui de volume” com sal (D) nem afunda e é comprimida (E); e as geleiras não crescem continuamente (B).</p>",
  p("Por que o nível dos mares não sobe, mesmo recebendo continuamente as águas dos rios?", "Essa questão já foi formulada por sábios da Grécia antiga. Hoje responderíamos que"),
  tags=["ciclo hidrológico"])

X(37, "M", "Matemática", "Progressão aritmética", "<p>Com 150 litros por pessoa por dia, os 6 milhões de litros atendem até 6.000.000/150 = 40.000 habitantes. A população cresce cerca de 2.000 por ano a partir de 27.990 em 2003: 29.990 (2004), ..., 37.990 (2008), 39.990 (2009) e 41.990 (2010). Os mananciais bastam até o final de 2009. Alternativa <strong>E</strong>.</p>",
  p("O jornal de uma pequena cidade publicou a seguinte notícia:")
  + ap("<strong>CORREIO DA CIDADE</strong><br><strong>ABASTECIMENTO COMPROMETIDO</strong>",
       "O novo pólo agroindustrial em nossa cidade tem atraído um enorme e constante fluxo migratório, resultando em um aumento da população em torno de 2000 habitantes por ano, conforme dados do nosso censo:")
  + tabela(["Ano", "População"], [["1995", "11.965"], ["1997", "15.970"], ["1999", "19.985"], ["2001", "23.980"], ["2003", "27.990"]])
  + ap("Esse crescimento tem ameaçado nosso fornecimento de água, pois os mananciais que abastecem a cidade têm capacidade para fornecer até 6 milhões de litros de água por dia. A prefeitura, preocupada com essa situação, vai iniciar uma campanha visando estabelecer um consumo médio de 150 litros por dia, por habitante.")
  + p("A análise da notícia permite concluir que a medida é oportuna. Mantido esse fluxo migratório e bem sucedida a campanha, os mananciais serão suficientes para abastecer a cidade até o final de"),
  tags=["crescimento linear", "abastecimento de água"])

X(38, "N", "Física", "Fontes de energia", "<p>Usinas termoelétricas podem queimar recursos muito diversos (carvão, gás natural, óleo, biomassa), o que é o argumento P2, e emitem poluentes na queima, o argumento N2. Alternativa <strong>D</strong>.</p><p>N1 (alagar lavouras e deslocar populações) é típico das hidrelétricas, e N3 (condições climáticas), das usinas eólicas e solares; e a maioria das termoelétricas não usa fonte renovável (P3).</p>",
  p("O crescimento da demanda por energia elétrica no Brasil tem provocado discussões sobre o uso de diferentes processos para sua geração e sobre benefícios e problemas a eles associados. Estão apresentados no quadro alguns argumentos favoráveis (ou positivos, P1, P2 e P3) e outros desfavoráveis (ou negativos, N1, N2 e N3) relacionados a diferentes opções energéticas.")
  + tabela(["", "Argumentos favoráveis", "", "Argumentos desfavoráveis"],
           [["P1", "Elevado potencial no país do recurso utilizado para a geração de energia.", "N1", "Destruição de áreas de lavoura e deslocamento de populações."],
            ["P2", "Diversidade dos recursos naturais que pode utilizar para a geração de energia.", "N2", "Emissão de poluentes."],
            ["P3", "Fonte renovável de energia.", "N3", "Necessidade de condições climáticas adequadas para sua instalação."]])
  + p("Ao se discutir a opção pela instalação, em uma dada região, de uma usina termoelétrica, os argumentos que se aplicam são"),
  tags=["termoelétrica"])

X(39, "N", "Física", "Energia", "<p>No esquema, o bagaço queimado gera calor para os processos da indústria e eletricidade, que abastece a própria usina e ainda é exportada. É o aproveitamento máximo da energia contida no combustível. Alternativa <strong>A</strong>.</p><p>O bagaço não aumenta a produção de açúcar e álcool como insumo (B), não vira álcool no processo (C), e a usina não queima álcool para gerar calor (D).</p>",
  "[[fig:1]]" + p("Os sistemas de cogeração representam uma prática de utilização racional de combustíveis e de produção de energia. Isto já se pratica em algumas indústrias de açúcar e de álcool, nas quais se aproveita o bagaço da cana, um de seus subprodutos, para produção de energia. Esse processo está ilustrado no esquema acima.",
                  "Entre os argumentos favoráveis a esse sistema de cogeração pode-se destacar que ele"),
  figs(("q39", "Esquema “Indústria sucro-alcooleira”: a cana-de-açúcar entra no processo industrial, que produz açúcar, álcool e bagaço. O bagaço é queimado como combustível e gera calor, que volta ao processo industrial, e eletricidade, que alimenta a indústria e sai também para fora da usina.")),
  ["cogeração", "bagaço de cana"])

X(40, "N", "Física", "Energia nuclear", "<p>Os dois argumentos são válidos: a fissão do urânio não queima combustível nem emite CO2, e os acidentes, embora raros, podem ser gravíssimos (como Chernobyl, em 1986). Juntos, servem para pesar vantagens e riscos. Alternativa <strong>D</strong>.</p><p>Já ocorreram acidentes nucleares (A); não há queima na geração nuclear (B); e há formas de gerar eletricidade que emitem gases do efeito estufa, como as termoelétricas (C).</p>",
  p("O debate em torno do uso da energia nuclear para produção de eletricidade permanece atual. Em um encontro internacional para a discussão desse tema, foram colocados os seguintes argumentos:")
  + '<ol type="I"><li>Uma grande vantagem das usinas nucleares é o fato de não contribuírem para o aumento do efeito estufa, uma vez que o urânio, utilizado como “combustível”, não é queimado mas sofre fissão.</li><li>Ainda que sejam raros os acidentes com usinas nucleares, seus efeitos podem ser tão graves que essa alternativa de geração de eletricidade não nos permite ficar tranqüilos.</li></ol>'
  + p("A respeito desses argumentos, pode-se afirmar que"),
  tags=["fissão nuclear", "efeito estufa"])

X(41, "N", "Física", "Energia elétrica", "<p>No verão os dias são mais longos. Adiantar os relógios faz o fim da tarde, quando o consumo é maior (pessoas chegam em casa e acendem as luzes), coincidir com luz natural, reduzindo o pico de consumo. Alternativa <strong>A</strong>.</p><p>A medida não reduz o consumo em todas as horas (B) e não tem relação com o regime de chuvas (C), o turismo (D) ou as férias nas indústrias (E).</p>",
  p("Entre outubro e fevereiro, a cada ano, em alguns estados das regiões Sul, Sudeste e Centro-Oeste, os relógios permanecem adiantados em uma hora, passando a vigorar o chamado horário de verão. Essa medida, que se repete todos os anos, visa"),
  tags=["horário de verão"])

X(42, "N", "Química", "Combustíveis", "<p>O gás natural tem grandes jazidas novas em exploração e, na queima, emite menos poluentes (menos CO2, quase nenhum enxofre e particulado) que o petróleo. Alternativa <strong>B</strong>.</p><p>O gás natural é combustível fóssil, não renovável (A, D), não vem do carvão (C) e produz CO2 na queima (E).</p>",
  p("Há estudos que apontam razões econômicas e ambientais para que o gás natural possa vir a tornar-se, ao longo deste século, a principal fonte de energia em lugar do petróleo. Justifica-se essa previsão, entre outros motivos, porque o gás natural"),
  tags=["gás natural"], quim=True)

X(43, "N", "Química", "Combustíveis", "<p>O biodiesel, feito de óleos vegetais (como mamona e soja) ou gorduras, é renovável e pode substituir o diesel de petróleo; em 2004 o Brasil testava sua produção. Alternativa <strong>C</strong>.</p><p>Gasolina e gás natural são fósseis (A, E), e o carvão mineral também (D).</p>",
  p("As previsões de que, em poucas décadas, a produção mundial de petróleo possa vir a cair têm gerado preocupação, dado seu caráter estratégico. Por essa razão, em especial no setor de transportes, intensificou-se a busca por alternativas para a substituição do petróleo por combustíveis renováveis. Nesse sentido, além da utilização de álcool, vem se propondo, no Brasil, ainda que de forma experimental,"),
  tags=["biodiesel"])

X(44, "M", "Matemática", "Razão e proporção", "<p>A regra diz que o álcool compensa se custar menos de 0,7 do preço da gasolina, ou seja, o álcool rende 70% da gasolina. Se com um volume de álcool o carro roda 10 km, com igual volume de gasolina roda 10/0,7 ≈ 14 km. Alternativa <strong>C</strong>.</p><p>7 km (A) inverte a relação.</p>",
  p("Já são comercializados no Brasil veículos com motores que podem funcionar com o chamado combustível flexível, ou seja, com gasolina ou álcool em qualquer proporção. Uma orientação prática para o abastecimento mais econômico é que o motorista multiplique o preço do litro da gasolina por 0,7 e compare o resultado com o preço do litro de álcool. Se for maior, deve optar pelo álcool. A razão dessa orientação deve-se ao fato de que, em média, se com um certo volume de álcool o veículo roda dez quilômetros, com igual volume de gasolina rodaria cerca de"),
  tags=["carro flex", "proporção"])

X(45, "N", "Física", "Energia", "<p>Os menores consumos de energia por passageiro por quilômetro estão nos transportes coletivos com ocupação máxima: ônibus (cerca de 250), metrô (cerca de 300) e trem (cerca de 400). O automóvel, mesmo cheio, gasta cerca de 1.250. Alternativa <strong>C</strong>.</p><p>Automóvel com poucos passageiros é o pior caso (B), cerca de 3.100.</p>",
  p("O excesso de veículos e os congestionamentos em grandes cidades são temas de freqüentes reportagens. Os meios de transportes utilizados e a forma como são ocupados têm reflexos nesses congestionamentos, além de problemas ambientais e econômicos. No gráfico a seguir, podem-se observar valores médios do consumo de energia por passageiro e por quilômetro rodado, em diferentes meios de transporte, para veículos em duas condições de ocupação (número de passageiros): ocupação típica e ocupação máxima.")
  + "[[fig:1]]" + p("Esses dados indicam que políticas de transporte urbano devem também levar em conta que a maior eficiência no uso de energia ocorre para os"),
  figs(("q45", "Gráfico de barras da energia consumida por passageiro por km (MJ/km), em ocupação típica e máxima: automóvel, cerca de 3.100 e 1.250; metrô, cerca de 450 e 300; trem, cerca de 550 e 400; ônibus, cerca de 600 e 250.")),
  ["eficiência energética", "transporte coletivo"])

X(46, "N", "Biologia", "Ecologia", "<p>No gráfico, os animais nascidos em cativeiro ficam em número pequeno e quase estável, enquanto os nascidos na natureza aumentam ano a ano e passam a ser a maioria. Isso mostra que os reintroduzidos se adaptaram e se reproduziram no ambiente natural. Alternativa <strong>A</strong>.</p><p>O aumento não vem de reintroduzir cada vez mais animais (B), e as duas populações convivem, sem eliminação (C, D).</p>",
  p("Programas de reintrodução de animais consistem em soltar indivíduos, criados em cativeiro, em ambientes onde sua espécie se encontra ameaçada ou extinta.",
    "O mico-leão-dourado da Mata Atlântica faz parte de um desses programas. Como faltam aos micos criados em cativeiro habilidades para sobreviver em seu habitat, são formados grupos sociais desses micos com outros capturados na natureza, antes de soltá-los coletivamente. O gráfico mostra o número total de animais, em uma certa região, a cada ano, ao longo de um programa de reintrodução desse tipo.")
  + "[[fig:1]]" + p("A análise do gráfico permite concluir que o sucesso do programa deveu-se"),
  figs(("q46", "Gráfico de barras empilhadas do número total de animais por ano, de 1984 a 1996. A parte dos nascidos em cativeiro varia entre cerca de 5 e 40 animais, sem tendência de alta, e fica perto de 20 nos últimos anos; a parte dos nascidos na natureza cresce de quase zero para cerca de 180, e o total passa de cerca de 10 para 200. Fonte: Primack e Rodrigues, Biologia da Conservação.")),
  ["mico-leão-dourado", "reintrodução"])

X(47, "N", "Biologia", "Controle de pragas", "<p>A armadilha com feromônio mostra quando o inseto chega, e o agrotóxico pode ser aplicado só no momento certo, em menor quantidade. Isso reduz custo e contaminação ambiental. Alternativa <strong>A</strong>.</p><p>A armadilha não captura todos os machos (C) nem espanta o inseto (E); seu papel é de monitoramento.</p>",
  p("O bicho-furão-dos-citros causa prejuízos anuais de US$ 50 milhões à citricultura brasileira, mas pode ser combatido eficazmente se um certo agrotóxico for aplicado à plantação no momento adequado. É possível determinar esse momento utilizando-se uma armadilha constituída de uma caixinha de papelão, contendo uma pastilha com o feromônio da fêmea e um adesivo para prender o macho. Verificando periodicamente a armadilha, percebe-se a época da chegada do inseto. Uma vantagem do uso dessas armadilhas, tanto do ponto de vista ambiental como econômico, seria"),
  tags=["feromônio", "agrotóxicos"])

X(48, "N", "Química", "Resíduos sólidos", "<p>A tabela mostra que quase 90% dos itens são plásticos, e o texto explica que as latas sumiram do lixo porque há mercado para reciclar alumínio. A mesma lógica aplicada ao plástico (incentivar sua reciclagem e recolhimento) atende aos comerciantes, aos frequentadores e ao ambiente. Alternativa <strong>E</strong>.</p><p>Proibir o consumo ou as embalagens (A, C) prejudica comerciantes e banhistas, e trocar plástico por vidro (D) traz risco de cortes.</p>",
  p("No verão de 2000 foram realizadas, para análise, duas coletas do lixo deixado pelos freqüentadores em uma praia no litoral brasileiro. O lixo foi pesado, separado e classificado. Os resultados das coletas feitas estão na tabela a seguir.")
  + tit("Dados obtidos (em área de cerca de 1900 m<sup>2</sup>)")
  + tabela(["Coleta de lixo", "1ª coleta", "2ª coleta"], [["Peso total", "8,3 kg", "3,2 kg"], ["Itens de plástico", "399 (86,4%)", "174 (88,8%)"], ["Itens de vidro", "10 (2,1%)", "03 (1,6%)"],
           ["Itens de metal", "14 (3,0%)", "07 (3,6%)"], ["Itens de papel", "17 (3,7%)", "06 (3,0%)"], ["Número de pessoas na praia", "270", "80"]])
  + fonte("Adaptado de <em>Ciência Hoje</em>.")
  + p("Embora fosse grande a venda de bebidas em latas nessa praia, não se encontrou a quantidade esperada dessas embalagens no lixo coletado, o que foi atribuído à existência de um bom mercado para a reciclagem de alumínio. Considerada essa hipótese, para reduzir o lixo nessa praia, a iniciativa que mais diretamente atende à variedade de interesses envolvidos, respeitando a preservação ambiental, seria"),
  tags=["reciclagem", "lixo"],
  alts=A5("proibir o consumo de bebidas e de outros alimentos nas praias.", "realizar a coleta de lixo somente no período noturno.", "proibir a comercialização apenas de produtos com embalagem.",
          "substituir embalagens plásticas por embalagens de vidro.", "incentivar a reciclagem de plásticos, estimulando seu recolhimento."))

X(49, "N", "Biologia", "Ecologia", "<p>I está correta: no esquema, a vida aquática superior (peixes) reaparece na zona de águas limpas, longe do lançamento. II também: na zona de degradação e de decomposição ativa, com muita matéria orgânica e pouco oxigênio, sobrevivem bactérias e fungos decompositores, inclusive anaeróbicos. III é falsa: as comunidades mudam em cada zona. Alternativa <strong>D</strong>.</p>",
  p("Um rio que é localmente degradado por dejetos orgânicos nele lançados pode passar por um processo de autodepuração. No entanto, a recuperação depende, entre outros fatores, da carga de dejetos recebida, da extensão e do volume do rio. Nesse processo, a distribuição das populações de organismos consumidores e decompositores varia, conforme mostra o esquema:")
  + "[[fig:1]]" + fonte("B. Braga et al. <em>Introdução à Engenharia Ambiental</em>.")
  + p("Com base nas informações fornecidas pelo esquema, são feitas as seguintes considerações sobre o processo de depuração do rio:")
  + I3("a vida aquática superior pode voltar a existir a partir de uma certa distância do ponto de lançamento dos dejetos;",
       "os organismos decompositores são os que sobrevivem onde a oferta de oxigênio é baixa ou inexistente e a matéria orgânica é abundante;",
       "as comunidades biológicas, apesar da poluição, não se alteram ao longo do processo de recuperação.")
  + p("Está correto o que se afirma em"),
  figs(("q49", "Esquema de um rio, no sentido da correnteza, a partir do ponto de lançamento de dejetos, dividido em zonas: águas limpas, degradação, decomposição ativa, recuperação e águas limpas. Abaixo, os tipos de organismos em cada zona: vida aquática superior (peixes) nas águas limpas; organismos mais resistentes na degradação; bactérias e fungos (anaeróbicos) na decomposição ativa; organismos mais resistentes na recuperação; e novamente vida aquática superior nas águas limpas. Uma seta indica “tempo ou distância”.")),
  ["autodepuração", "poluição orgânica"])

X(50, "N", "Química", "Estequiometria", "<p>Pela equação, 1 tonelada de H2SO4 reage com cerca de 1 tonelada de CaCO3. Para 10.000 t de ácido, são 10.000 t de CaCO3. Como o calcário tem 80% de CaCO3, são necessárias 10.000/0,8 = 12.500 t de calcário, e 12.500/30 ≈ 417 caminhões, perto de 400. Alternativa <strong>D</strong>.</p><p>Ignorando a pureza de 80% chega-se a cerca de 333 caminhões (C).</p>",
  p("Em setembro de 1998, cerca de 10.000 toneladas de ácido sulfúrico (H2SO4) foram derramadas pelo navio Bahamas no litoral do Rio Grande do Sul. Para minimizar o impacto ambiental de um desastre desse tipo, é preciso neutralizar a acidez resultante. Para isso pode-se, por exemplo, lançar calcário, minério rico em carbonato de cálcio (CaCO3), na região atingida.",
    "A equação química que representa a neutralização do H2SO4 por CaCO3, com a proporção aproximada entre as massas dessas substâncias é:")
  + "[[fig:1]]"
  + p("Pode-se avaliar o esforço de mobilização que deveria ser empreendido para enfrentar tal situação, estimando a quantidade de caminhões necessária para carregar o material neutralizante. Para transportar certo calcário que tem 80% de CaCO3, esse número de caminhões, cada um com carga de 30 toneladas, seria próximo de"),
  figs(("q50", "Equação: H₂SO₄ (1 tonelada) + CaCO₃ (reage com 1 tonelada) → CaSO₄ (sólido sedimentado) + H₂O + CO₂ (gás).")),
  ["neutralização", "pureza"], quim=True)

X(51, "H", "Sociologia", "Direitos humanos", "<p>Ao assinar a Declaração, os Estados se comprometem a respeitá-la sempre: a soberania deve estar em conformidade com os direitos humanos, inclusive em guerras. Alternativa <strong>B</strong>.</p><p>As demais admitem exceções (conflito, retaliação, limites de tolerância, autodefesa) que a proibição absoluta da tortura no artigo 5º não permite.</p>",
  p("Em conflitos regionais e na guerra entre nações tem sido observada a ocorrência de seqüestros, execuções sumárias, torturas e outras violações de direitos. Em 10 de dezembro de 1948, a Assembléia Geral das Nações Unidas adotou a Declaração Universal dos Direitos do Homem, que, em seu artigo 5º, afirma:")
  + ap("Ninguém será submetido a tortura nem a penas ou tratamentos cruéis, desumanos ou degradantes.")
  + p("Assim, entre nações que assinaram essa Declaração, é coerente esperar que"),
  tags=["Declaração Universal dos Direitos Humanos"])

X(52, "H", "Geografia", "Globalização", "<p>O carro sofisticado é projetado e financiado nos países ricos, enquanto as roupas são feitas em maquiladoras de países pobres, sem direitos trabalhistas garantidos. Essa divisão reafirma as diferenças entre centro rico e periferia pobre, e também dentro dos próprios países. Alternativa <strong>E</strong>.</p><p>Esse tipo de globalização não diminui disparidades (A, D) nem fortalece igualmente os Estados (C); as roupas nem trazem a origem real (B).</p>",
  ap("Um certo carro esporte é desenhado na Califórnia, financiado por Tóquio, o protótipo criado em Worthing (Inglaterra) e a montagem é feita nos EUA e México, com componentes eletrônicos inventados em Nova Jérsei (EUA), fabricados no Japão. (…). Já a indústria de confecção norte-americana, quando inscreve em seus produtos ‘made in USA’, esquece de mencionar que eles foram produzidos no México, Caribe ou Filipinas.")
  + fonte("Renato Ortiz, <em>Mundialização e Cultura</em>.")
  + p("O texto ilustra como em certos países produz-se tanto um carro esporte caro e sofisticado, quanto roupas que nem sequer levam uma etiqueta identificando o país produtor. De fato, tais roupas costumam ser feitas em fábricas – chamadas “maquiladoras” – situadas em zonas-francas, onde os trabalhadores nem sempre têm direitos trabalhistas garantidos. A produção nessas condições indicaria um processo de globalização que"),
  tags=["maquiladoras", "divisão internacional do trabalho"])

X(53, "H", "História", "Primeiro Reinado", "<p>Frei Caneca chama o Poder Moderador de “chave mestra da opressão” e “garrote mais forte da liberdade”, porque permitia ao imperador dissolver a Câmara dos Deputados, a representação do povo, preservando o Senado de seus “apaniguados”. Para ele, era um poder arbitrário. Alternativa <strong>C</strong>.</p><p>Frei Caneca o via como forte e opressor, não neutro (D) nem garantidor da liberdade (B, E).</p>",
  p("<strong>Constituição de 1824:</strong>") + ap("“Art. 98. O Poder Moderador é a chave de toda a organização política, e é delegado privativamente ao Imperador (…) para que incessantemente vele sobre a manutenção da Independência, equilíbrio, e harmonia dos demais poderes políticos (...) dissolvendo a Câmara dos Deputados nos casos em que o exigir a salvação do Estado.”")
  + p("<strong>Frei Caneca:</strong>") + ap("“O Poder Moderador da nova invenção maquiavélica é a chave mestra da opressão da nação brasileira e o garrote mais forte da liberdade dos povos. Por ele, o imperador pode dissolver a Câmara dos Deputados, que é a representante do povo, ficando sempre no gozo de seus direitos o Senado, que é o representante dos apaniguados do imperador.”")
  + fonte("Voto sobre o juramento do projeto de Constituição.")
  + p("Para Frei Caneca, o Poder Moderador definido pela Constituição outorgada pelo Imperador em 1824 era"),
  tags=["Poder Moderador", "Frei Caneca"])

X(54, "H", "Sociologia", "Questão racial", "<p>A atitude I (o Dia da Consciência Negra como crítica à segregação e à exclusão) se aproxima de Florestan Fernandes, para quem a miscigenação não trouxe integração em igualdade. A atitude II (a impressão de convivência harmoniosa entre as etnias) se aproxima de Gilberto Freyre, que via a mistura como algo que “adoçou” o Brasil. Alternativa <strong>C</strong>.</p><p>B inverte as aproximações.</p>",
  p("A questão étnica no Brasil tem provocado diferentes atitudes:")
  + '<ol type="I"><li>Instituiu-se o “Dia Nacional da Consciência Negra” em 20 de novembro, ao invés da tradicional celebração do 13 de maio. Essa nova data é o aniversário da morte de Zumbi, que hoje simboliza a crítica à segregação e à exclusão social.</li><li>Um turista estrangeiro que veio ao Brasil, no carnaval, afirmou que nunca viu tanta convivência harmoniosa entre as diversas etnias.</li></ol>'
  + p("Também sobre essa questão, estudiosos fazem diferentes reflexões:")
  + ap("Entre nós [brasileiros], (...) a separação imposta pelo sistema de produção foi a mais fluida possível. Permitiu constante mobilidade de classe para classe e até de uma raça para outra. Esse amor, acima de preconceitos de raça e de convenções de classe, do branco pela cabocla, pela cunhã, pela índia (...) agiu poderosamente na formação do Brasil, adoçando-o.")
  + fonte("Gilberto Freire. <em>O mundo que o português criou</em>.")
  + ap("[Porém] o fato é que ainda hoje a miscigenação não faz parte de um processo de integração das “raças” em condições de igualdade social. O resultado foi que (...) ainda são pouco numerosos os segmentos da “população de cor” que conseguiram se integrar, efetivamente, na sociedade competitiva.")
  + fonte("Florestan Fernandes. <em>O negro no mundo dos brancos</em>.")
  + p("Considerando as atitudes expostas acima e os pontos de vista dos estudiosos, é correto aproximar"),
  tags=["Gilberto Freyre", "Florestan Fernandes"])

X(55, "H", "História", "Revolução Francesa", "<p>O caldo popular “restaurant” virou estabelecimento com pratos requintados, cardápios e mesas individuais, frequentado pela burguesia, e depois da Revolução os cozinheiros da nobreza passaram a servir esse público. A burguesia se apropriou de hábitos populares e de valores da nobreza, transformando-os. Alternativa <strong>B</strong>.</p><p>As classes populares não ascenderam ao padrão da nobreza (A), e a nobreza perdeu espaço, sem institucionalizar práticas igualitárias (C, E).</p>",
  p("Algumas transformações que antecederam a Revolução Francesa podem ser exemplificadas pela mudança de significado da palavra “restaurante”. Desde o final da Idade Média, a palavra <em>restaurant</em> designava caldos ricos, com carne de aves e de boi, legumes, raízes e ervas. Em 1765 surgiu, em Paris, um local onde se vendiam esses caldos, usados para restaurar as forças dos trabalhadores. Nos anos que precederam a Revolução, em 1789, multiplicaram-se diversos <em>restaurateurs</em>, que serviam pratos requintados, descritos em páginas emolduradas e servidos não mais em mesas coletivas e mal cuidadas, mas individuais e com toalhas limpas. Com a Revolução, cozinheiros da corte e da nobreza perderam seus patrões, refugiados no exterior ou guilhotinados, e abriram seus restaurantes por conta própria. Apenas em 1835, o Dicionário da Academia Francesa oficializou a utilização da palavra restaurante com o sentido atual.",
    "A mudança do significado da palavra restaurante ilustra"),
  tags=["burguesia", "Revolução Francesa"])

X(56, "M", "Matemática", "Leitura de gráficos", "<p>O lucro é L = (L/n) × n. Em 2000: 20 × 20 = 400; em 2001: 40 × 16 = 640; em 2002: 45 × 12 = 540; em 2003: 40 × 10 = 400 (em centenas de reais). O maior lucro foi em 2001, e não em 2002, quando a produtividade foi máxima com menos operários. Alternativa <strong>B</strong>.</p><p>Reduzir operários aumentou a produtividade, mas não necessariamente o lucro.</p>",
  ap("As empresas querem a metade das pessoas trabalhando o dobro para produzir o triplo.") + fonte("Revista <em>Você S/A</em>, 2004.")
  + p("Preocupado em otimizar seus ganhos, um empresário encomendou um estudo sobre a produtividade de seus funcionários nos últimos quatro anos, entendida por ele, de forma simplificada, como a relação direta entre seu lucro anual (L) e o número de operários envolvidos na produção (n). Do estudo, resultou o gráfico abaixo.") + "[[fig:1]]"
  + p("Ao procurar, no gráfico, uma relação entre seu lucro, produtividade e número de operários, o empresário concluiu que a maior produtividade ocorreu em 2002, e o maior lucro"),
  figs(("q56", "Gráfico de barras de 2000 a 2003 com dois eixos. Produtividade L/n (em R$ 100,00): 20 em 2000, 40 em 2001, 45 em 2002 e 40 em 2003. Número de operários n: 20 em 2000, 16 em 2001, 12 em 2002 e 10 em 2003.")),
  ["produtividade"])

X(57, "N", "Biologia", "DNA", "<p>Em todos os materiais, a porcentagem de adenina é quase igual à de timina, e a de guanina, quase igual à de citosina: A pareia com T e G com C. Isso vale para humanos, rato, ouriço, trigo e bactéria, mostrando a universalidade da estrutura do DNA. Alternativa <strong>A</strong>.</p><p>As proporções entre as espécies mudam, mas os pares são os mesmos (B, C).</p>",
  p("A identificação da estrutura do DNA foi fundamental para compreender seu papel na continuidade da vida. Na década de 1950, um estudo pioneiro determinou a proporção das bases nitrogenadas que compõem moléculas de DNA de várias espécies.")
  + tabela(["Material analisado", "A", "G", "C", "T"],
           [["Espermatozóide humano", "30,7%", "19,3%", "18,8%", "31,2%"], ["Fígado humano", "30,4%", "19,5%", "19,9%", "30,2%"], ["Medula óssea de rato", "28,6%", "21,4%", "21,5%", "28,5%"],
            ["Espermatozóide de ouriço-do-mar", "32,8%", "17,7%", "18,4%", "32,1%"], ["Plântulas de trigo", "27,9%", "21,8%", "22,7%", "27,6%"], ["Bactéria <em>E. coli</em>", "26,1%", "24,8%", "23,9%", "25,1%"]])
  + fonte("Bases nitrogenadas: A, adenina; G, guanina; C, citosina; T, timina.")
  + p("A comparação das proporções permitiu concluir que ocorre emparelhamento entre as bases nitrogenadas e que elas formam"),
  tags=["bases nitrogenadas", "Chargaff"])

X(58, "N", "Biologia", "Origem da vida", "<p>A água líquida é indispensável a todas as formas de vida conhecidas. Encontrar água em Marte indicaria a possibilidade de existir, ou ter existido, alguma forma de vida semelhante à da Terra. Alternativa <strong>C</strong>.</p><p>Agricultura, extração de água para a Terra ou colônias humanas (A, D, E) estão muito distantes da realidade das missões.</p>",
  p("Nas recentes expedições espaciais que chegaram ao solo de Marte, e através dos sinais fornecidos por diferentes sondas e formas de análise, vem sendo investigada a possibilidade da existência de água naquele planeta. A motivação principal dessas investigações, que ocupam freqüentemente o noticiário sobre Marte, deve-se ao fato de que a presença de água indicaria, naquele planeta,"),
  tags=["Marte", "água"])

X(59, "L", "Literatura", "Intertextualidade", "<p>Hagar não aceita que o mundo seja redondo porque, olhando em volta, só vê uma planície: sua compreensão do mundo se limita ao que a experiência e o conhecimento do seu meio lhe mostram, enquanto o filho aprendeu nos livros. Caeiro afirma algo parecido: a aldeia é grande como qualquer outra porque “sou do tamanho do que vejo”. A compreensão do mundo depende do alcance da cultura de cada um. Alternativa <strong>A</strong>.</p><p>O poema descarta a altura física (“E não do tamanho da minha altura”, E), e o problema de Hagar não é de visão, apesar da piada do oculista (B).</p>",
  "[[fig:1]]"
  + ap("Da minha aldeia vejo quanto da terra se pode ver no Universo...<br>Por isso minha aldeia é grande como outra qualquer<br>Porque sou do tamanho do que vejo<br>E não do tamanho da minha altura...")
  + fonte("Alberto Caeiro.")
  + p("A tira “Hagar” e o poema de Alberto Caeiro (um dos heterônimos de Fernando Pessoa) expressam, com linguagens diferentes, uma mesma idéia: a de que a compreensão que temos do mundo é condicionada, essencialmente,"),
  figs(("q59", "Tira “Hagar”, de Dik Browne, em três quadros. O filho de Hagar, lendo um livro, diz: “Acho que o mundo é redondo.”, e Hagar pergunta: “É mesmo?”. No segundo quadro, Hagar olha em volta numa planície plana e vazia, com um ponto de interrogação. No terceiro, de volta ao filho, diz: “Vou levar você a um oculista.”")),
  ["Alberto Caeiro", "Fernando Pessoa"])

X(60, "N", "Química", "Metalurgia", "<p>O quadro mostra que o ferro só passou a ser usado depois do fole e do aumento da temperatura de queima: o ferro exige temperaturas mais altas para ser extraído do minério e moldado do que o cobre e o estanho. Alternativa <strong>B</strong>.</p><p>O fogo já era usado (A), a extração de metais de minérios já era conhecida desde o quarto milênio (C), e o ferro não depende do cobre (D).</p>",
  p("Na fabricação de qualquer objeto metálico, seja um parafuso, uma panela, uma jóia, um carro ou um foguete, a metalurgia está presente na extração de metais a partir dos minérios correspondentes, na sua transformação e sua moldagem. Muitos dos processos metalúrgicos atuais têm em sua base conhecimentos desenvolvidos há milhares de anos, como mostra o quadro:")
  + tabela(["Milênio antes de Cristo", "Métodos de extração e operação"],
           [["quinto milênio a.C.", "Conhecimento do ouro e do cobre nativos<br>Conhecimento da prata e das ligas de ouro e prata"],
            ["quarto milênio a.C.", "Obtenção do cobre e chumbo a partir de seus minérios<br>Técnicas de fundição<br>Obtenção do estanho a partir do minério"],
            ["terceiro milênio a.C.", "Uso do bronze<br>Introdução do fole e aumento da temperatura de queima"],
            ["segundo milênio a.C.", "Início do uso do ferro<br>Obtenção do mercúrio e dos amálgamas"], ["primeiro milênio a.C.", "Cunhagem de moedas"]])
  + fonte("J. A. Vanin, <em>Alquimistas e Químicos</em>.")
  + p("Podemos observar que a extração e o uso de diferentes metais ocorreram a partir de diferentes épocas. Uma das razões para que a extração e o uso do ferro tenham ocorrido após a do cobre ou estanho é"),
  tags=["metalurgia", "ferro"])

X(61, "N", "Química", "Corrosão", "<p>As equações mostram que a ferrugem exige ferro, água e oxigênio. A graxa forma uma camada que impermeabiliza a superfície e reduz o contato com o ar úmido. Alternativa <strong>B</strong>.</p><p>A graxa não galvaniza o metal (D), que exige revestimento de zinco, nem atua como isolante térmico (C).</p>",
  p("Ferramentas de aço podem sofrer corrosão e enferrujar. As etapas químicas que correspondem a esses processos podem ser representadas pelas equações:") + "[[fig:1]]"
  + p("Uma forma de tornar mais lento esse processo de corrosão e formação de ferrugem é engraxar as ferramentas. Isso se justifica porque a graxa proporciona"),
  figs(("q61", "Três equações: Fe + H₂O + ½ O₂ → Fe(OH)₂; Fe(OH)₂ + ½ H₂O + ¼ O₂ → Fe(OH)₃; Fe(OH)₃ + n H₂O → Fe(OH)₃ · nH₂O (ferrugem).")),
  ["ferrugem", "oxidação"])

X(62, "N", "Biologia", "Tempo geológico", "<p>Na escala, 4,5 bilhões de anos valem 365 dias: cada dia equivale a cerca de 12,3 milhões de anos, e cada segundo a cerca de 143 anos. A chegada de Cabral, há cerca de 500 anos, cai uns 3,5 segundos antes da meia-noite de 31 de dezembro. Alternativa <strong>E</strong>.</p>",
  ap("Comprimam-se todos os 4,5 bilhões de anos de tempo geológico em um só ano. Nesta escala, as rochas mais antigas reconhecidas datam de março. Os seres vivos apareceram inicialmente nos mares, em maio. As plantas e animais terrestres surgiram no final de novembro.")
  + fonte("Don L. Eicher, <em>Tempo Geológico</em>.")
  + tabela(["Mês", "Milhões de anos atrás"], [['JAN', '4500'], ['FEV', '4125'], ['MAR', '3750'], ['ABR', '3375'], ['MAI', '3000'], ['JUN', '2625'], ['JUL', '2250'], ['AGO', '1875'], ['SET', '1500'], ['OUT', '1125'], ['NOV', '750'], ['DEZ', '375']])
  + p("Na escala de tempo acima, o sistema solar surgiu no início de janeiro e vivemos hoje à meia-noite de 31 de dezembro. Nessa mesma escala, Pedro Álvares Cabral chegou ao Brasil também no mês de dezembro, mais precisamente na"),
  tags=["escala de tempo", "proporção"])

X(63, "H", "História", "Energia e sociedade", "<p>Do fim do século XIX (inglês, cerca de 8 mil kcal por dia) ao século XX (norte-americano, cerca de 23 mil kcal), o consumo quase triplicou em cerca de um século. Nas outras passagens, aumentos menores levaram milhares de anos. A taxa mais acentuada é a da Segunda Revolução Industrial aos dias atuais. Alternativa <strong>E</strong>.</p>",
  p("O consumo diário de energia pelo ser humano vem crescendo e se diversificando ao longo da História, de acordo com as formas de organização da vida social. O esquema apresenta o consumo típico de energia de um habitante de diferentes lugares e em diferentes épocas.") + "[[fig:1]]"
  + fonte("E. Cooks, <em>Man, Energy and Society</em>.")
  + p("Segundo esse esquema, do estágio primitivo ao tecnológico, o consumo de energia <em>per capita</em> no mundo cresceu mais de 100 vezes, variando muito as taxas de crescimento, ou seja, a razão entre o aumento do consumo e o intervalo de tempo em que esse aumento ocorreu. O período em que essa taxa de crescimento foi mais acentuada está associado à passagem"),
  figs(("q63", "Gráfico de barras horizontais “Consumo de energia em diferentes lugares e épocas” (escala não linear de tempo), em mil kcal per capita por dia, dividido em alimentação, indústria e agricultura, moradia e comércio, e transporte. Habitante do leste da África há 500 mil anos: cerca de 0,2. Nômade europeu há 100 mil anos: cerca de 0,5. Habitante da Mesopotâmia em 5000 a.C.: cerca de 1,2. Europeu em 1400 d.C.: cerca de 2,7. Inglês no final do século XIX: cerca de 8. Norte-americano no século XX: cerca de 23.")),
  ["consumo de energia", "Revolução Industrial"])

# Revisão geral (12/11): o texto comum do grupo seguinte vazava para a alternativa E anterior.
for _q in Q.values():
    for _l, _v in list(_q["alternativas"].items()):
        _q["alternativas"][_l] = re.split(r"\s*(?:Texto para as questões \d|Instruções: As questões de números)", _v)[0]

completar(Q, R)
