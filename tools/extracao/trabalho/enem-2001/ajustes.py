# Enem 2001 (data não confirmada; dataExame omitida), Prova 1 — amarela: prova única de 63 questões (modelo antigo, sem divisão por áreas).
# Fonte do PDF: arquivo 'Provas_Gabaritos_ENEM_2001' do usuário. Gabarito: cópia do gabarito oficial (cabeçalho Ministério da Educação/Inep, Prova 1 – Amarela) no acervo da USP: GABARITO_ENEM_2001_AMARELA.pdf, lido duas vezes.
# Data: não encontrei fonte acessível; o campo dataExame fica de fora (é opcional).
# Duas colunas em todas as páginas, números em FuturaBdCn: extrator com LINHAS=1 NXR=44-88,345-360 NFONT=FuturaBdCn COLS=3..12 COLX=300 YMIN=40 YMAX=800.
# O extrator padrão não lê este layout; as alternativas vêm de alts.json (extrator próprio) e os enunciados são escritos aqui.
# Cada questão leva a grande área mais próxima. Protegidos como imagem: Drummond (Q1), Murilo Mendes (Q12), versos de Vinicius de Moraes (alternativas da Q20)
# e letra de Gilberto Gil (Q63). Em texto: Castro Alves, Machado e Shakespeare (domínio público) e a prosa.
import sys, pathlib, re, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar

ID = "enem-2001"
META = {"id": ID, "banca": "Enem", "ano": 2001, "titulo": "Enem 2001: Prova objetiva", "fonte": "Inep",
        "duracaoMinutos": 300, "area": "Prova objetiva (63 questões)", "caderno": "amarelo", "dia": 1, "fonteGabarito": {"oficial": True, "nome": "gabarito oficial do Inep, em cópia guardada pelo Instituto de Física da USP", "url": "https://fep.if.usp.br/~profis/arquivo/avaliacao/enem/provas_gabaritos/2001/"}}
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



# ----------------------------------------------------------------
X(1, "L", "Língua Portuguesa", "Conjunções", "<p>Em “O mundo é grande e cabe / Nesta janela”, o “e” liga ideias que se contrariam: algo grande que, apesar disso, cabe num espaço pequeno. Ele tem valor adversativo, equivalente a “mas”: sentido de oposição. Alternativa <strong>A</strong>.</p><p>O “e” não compara (B), não conclui (C), não alterna (D) nem indica finalidade (E).</p>",
  "[[fig:1]]" + p("Neste poema, o poeta realizou uma opção estilística: a reiteração de determinadas construções e expressões lingüísticas, como o uso da mesma conjunção para estabelecer a relação entre as frases. Essa conjunção estabelece, entre as idéias relacionadas, um sentido de"),
  figs(("q01", "Poema “O mundo é grande”, de Carlos Drummond de Andrade, em seis versos que repetem a mesma estrutura: o mundo é grande e cabe numa janela sobre o mar; o mar é grande e cabe na cama de amar; o amor é grande e cabe no breve espaço de beijar.")),
  ["Drummond", "conjunção adversativa"])

X(2, "M", "Matemática", "Proporção", "<p>Como o papel é uniforme, a massa é proporcional à área. A praça (100 m × 100 m = 10.000 m²) pesa 0,08 g, e a planta toda, 40 g: 40/0,08 = 500 vezes mais. A área da cidade é 500 × 10.000 = 5.000.000 m². Alternativa <strong>E</strong>.</p><p>800 (A) é 40/0,08 × 1,6, sem relação com a área real.</p>",
  p("Um engenheiro, para calcular a área de uma cidade, copiou sua planta numa folha de papel de boa qualidade, recortou e pesou numa balança de precisão, obtendo 40 g. Em seguida, recortou, do mesmo desenho, uma praça de dimensões reais 100 m x 100 m, pesou o recorte na mesma balança e obteve 0,08 g. Com esses dados foi possível dizer que a área da cidade, em metros quadrados, é de, aproximadamente,") + "[[fig:1]]",
  figs(("q02", "Desenho da planta de uma cidade, de contorno irregular, com um pequeno quadrado indicado como “praça de área conhecida”.")),
  ["área", "proporcionalidade"])

X(3, "N", "Química", "Ácidos", "<p>I é possível: o ácido mata peixes perto do derrame. II também: a acidez varia com a distância e com a corrente, que dilui e arrasta o ácido. IV também: a diluição do ácido sulfúrico concentrado em água libera muito calor. III não: num curso d’água, o ácido é diluído e levado pela corrente, sem dano permanente. Alternativa <strong>D</strong>.</p>",
  p("Numa rodovia pavimentada, ocorreu o tombamento de um caminhão que transportava ácido sulfúrico concentrado. Parte da sua carga fluiu para um curso d'água não poluído que deve ter sofrido, como conseqüência,")
  + '<ol type="I"><li>mortandade de peixes acima da normal no local do derrame de ácido e em suas proximidades.</li><li>variação do pH em função da distância e da direção da corrente de água.</li><li>danos permanentes na qualidade de suas águas.</li><li>aumento momentâneo da temperatura da água no local do derrame.</li></ol>'
  + p("É correto afirmar que, dessas conseqüências, apenas podem ocorrer"),
  tags=["ácido sulfúrico", "diluição"])

X(4, "H", "História", "Revolução Industrial", "<p>Adam Smith descreve a divisão do trabalho na fabricação de alfinetes, e a tira mostra um operário que, depois de 30 anos na linha de montagem, não sabe o que fabrica: ambos retratam a divisão do trabalho (I) e o operário que não conhece o processo todo (III). Alternativa <strong>E</strong>.</p><p>II é falsa: o texto de Smith é do século XVIII, sem produção informatizada, e a tira mostra produção industrial, não artesanal.</p>",
  ap("“... Um operário desenrola o arame, o outro o endireita, um terceiro corta, um quarto o afia nas pontas para a colocação da cabeça do alfinete; para fazer a cabeça do alfinete requerem-se 3 ou 4 operações diferentes; ...”")
  + fonte("SMITH, Adam. <em>A Riqueza das Nações</em>. Investigação sobre a sua Natureza e suas Causas. Vol. I. São Paulo: Nova Cultural, 1985.")
  + "[[fig:1]]" + fonte("<em>Jornal do Brasil</em>, 19 de fevereiro de 1997.")
  + p("A respeito do texto e do quadrinho são feitas as seguintes afirmações:")
  + I3("Ambos retratam a intensa divisão do trabalho, à qual são submetidos os operários.", "O texto refere-se à produção informatizada e o quadrinho, à produção artesanal.", "Ambos contêm a idéia de que o produto da atividade industrial não depende do conhecimento de todo o processo por parte do operário.")
  + p("Dentre essas afirmações, apenas"),
  figs(("q04", "Tira “Frank e Ernest”, de Thaves: um operário velho, numa linha de montagem, diz: “Vou me aposentar amanhã e sabe o que vou fazer? Andar até o fim desta linha de montagem e descobrir o que estou fazendo há 30 anos!”")),
  ["divisão do trabalho", "Adam Smith"], alts=dict(D[4], E="I e III estão corretas."))

X(5, "M", "Matemática", "Probabilidade", "<p>O cartão tem 3, 4, 3, 3 e 2 espaços nas linhas 1 a 5. Com duas bolas na linha 4 e duas na linha 5, sobram 3 bolas, e para a chance não ser zero cada uma das linhas 1, 2 e 3 tem exatamente uma. A probabilidade é 1/3 × 1/4 × 1/3 × 2/3 × 2/2 = 2/108 = 1/54. Alternativa <strong>C</strong>.</p>",
  p("Uma empresa de alimentos imprimiu em suas embalagens um cartão de apostas do seguinte tipo:") + "[[fig:1]]"
  + p("Cada cartão de apostas possui 7 figuras de bolas de futebol e 8 sinais de “X” distribuídos entre os 15 espaços possíveis, de tal forma que a probabilidade de um cliente ganhar o prêmio nunca seja igual a zero. Em determinado cartão existem duas bolas na linha 4 e duas bolas na linha 5. Com esse cartão, a probabilidade de o cliente ganhar o prêmio é"),
  figs(("q05", "Frente do cartão: cinco linhas de círculos a raspar, com 3 círculos na linha 1, 4 na linha 2, 3 na linha 3, 3 na linha 4 e 2 na linha 5. Verso, “Como jogar”: inicie raspando apenas uma das alternativas da linha 1; se achar uma bola de futebol, vá para a linha 2 e raspe apenas uma das alternativas, e continue assim até o fim do jogo; se encontrar um “X” em qualquer linha, o jogo está encerrado e você não terá direito ao prêmio; se encontrar uma bola em cada uma das linhas, terá direito ao prêmio.")),
  ["probabilidade", "eventos sucessivos"], alts=A5(r"\(\frac{1}{27}\)", r"\(\frac{1}{36}\)", r"\(\frac{1}{54}\)", r"\(\frac{1}{72}\)", r"\(\frac{1}{108}\)"))

X(6, "H", "Geografia", "Oriente Médio", "<p>O corte mostra que a Cisjordânia tem o planalto central (até 880 m) sobre Israel e desce até o vale do Jordão, abaixo do nível do mar. Controlar a área dá vantagem militar pelo relevo e acesso aos recursos hídricos do Jordão, escassos na região. Alternativa <strong>E</strong>.</p><p>A área não é planície (A), não abrange as duas margens do Jordão (B) e não está junto ao Mediterrâneo (D).</p>",
  p("A figura apresenta as fronteiras entre os países envolvidos na Questão Palestina e um corte, no mapa, da área indicada.") + "[[fig:1]]" + fonte("Adaptado da revista <em>Hérodote</em>, números 29 e 30.")
  + p("Com base na análise dessa figura e considerando o conflito entre árabes e israelenses, pode-se afirmar que, para Israel, é importante manter ocupada a área litigiosa por tratar-se de uma região"),
  figs(("q06", "Mapa de Israel, Líbano, Síria, Cisjordânia, Jordânia e Egito, com a linha de um corte de oeste a leste. Abaixo, o perfil do relevo ao longo do corte: planície costeira de Israel junto ao Mediterrâneo; limite Israel/Cisjordânia a 210 m; planalto central da Cisjordânia, entre 650 e 880 m; vale do Jordão a −310 m, abaixo do nível do mar; e o lado jordaniano subindo a 890 e 1.040 m.")),
  ["Questão Palestina", "Cisjordânia"])

X(7, "N", "Química", "Estequiometria", "<p>Uma tonelada de carvão com 1% de enxofre tem 10 kg de S, que formam 20 kg de SO2 (32 g de S dão 64 g de SO2). Pela segunda reação, 64 g de SO2 reagem com 74 g de hidróxido de cálcio: 20 kg × 74/64 ≈ 23 kg. Alternativa <strong>A</strong>.</p><p>74 kg (D) seria para 64 kg de SO2, e não para 20 kg.</p>",
  p("Atualmente, sistemas de purificação de emissões poluidoras estão sendo exigidos por lei em um número cada vez maior de países. O controle das emissões de dióxido de enxofre gasoso, provenientes da queima de carvão que contém enxofre, pode ser feito pela reação desse gás com uma suspensão de hidróxido de cálcio em água, sendo formado um produto não poluidor do ar.",
    "A queima do enxofre e a reação do dióxido de enxofre com o hidróxido de cálcio, bem como as massas de algumas das substâncias envolvidas nessas reações, podem ser assim representadas:")
  + ap("enxofre (32 g) + oxigênio (32 g) → dióxido de enxofre (64 g)", "dióxido de enxofre (64 g) + hidróxido de cálcio (74 g) → produto não poluidor")
  + p("Dessa forma, para absorver todo o dióxido de enxofre produzido pela queima de uma tonelada de carvão (contendo 1% de enxofre), é suficiente a utilização de uma massa de hidróxido de cálcio de, aproximadamente,"),
  tags=["dióxido de enxofre", "proporção de massas"], alts=A5("23 kg.", "43 kg.", "64 kg.", "74 kg.", "138 kg."))

X(8, "L", "Língua Portuguesa", "Provérbios", "<p>“Devagar se vai ao longe” e “De grão em grão, a galinha enche o papo” ensinam a mesma coisa: paciência e persistência, com pequenos passos, levam ao resultado. Alternativa <strong>B</strong>.</p><p>Nos outros pares, os provérbios tratam de assuntos diferentes (por exemplo, consequências da fala e da aparência em A).</p>",
  p("Os provérbios constituem um produto da sabedoria popular e, em geral, pretendem transmitir um ensinamento. A alternativa em que os dois provérbios remetem a ensinamentos semelhantes é:"),
  tags=["provérbios"])

X(9, "M", "Matemática", "Volume do cilindro", "<p>Se o barbante mede a circunferência C, dobrado duas vezes fica C/4, e a estimativa é (C/4)² × L = C²L/16. O cilindro real tem raio C/(2π) e volume π(C/2π)² × L = C²L/(4π). A razão é (1/16)/(1/(4π)) = π/4 ≈ 0,785: a estimativa dá cerca de 78% do volume real, uma diferença de cerca de 22%. Alternativa <strong>B</strong>.</p>",
  p("Em muitas regiões do Estado do Amazonas, o volume de madeira de uma árvore cortada é avaliado de acordo com uma prática dessas regiões:")
  + p("I - Dá-se uma volta completa em torno do tronco com um barbante.") + "[[fig:1]]"
  + p("II - O barbante é dobrado duas vezes pela ponta e, em seguida, seu comprimento é medido com fita métrica.") + "[[fig:2]]"
  + p("III - O valor obtido com essa medida é multiplicado por ele mesmo e depois multiplicado pelo comprimento do tronco. Esse é o volume estimado de madeira.",
      "Outra estimativa pode ser obtida pelo cálculo formal do volume do tronco, considerando-o um cilindro perfeito.",
      "A diferença entre essas medidas é praticamente equivalente às perdas de madeira no processo de corte para comercialização.",
      "Pode-se afirmar que essas perdas são da ordem de"),
  figs(("q09a", "Desenho de um tronco de árvore deitado, com um barbante dando uma volta completa ao seu redor."), ("q09b", "Dois desenhos do barbante: dobrado uma vez (1ª dobra) e dobrado de novo (2ª dobra), ficando com um quarto do comprimento.")),
  ["cilindro", "estimativa"], alts=dict(D[9], E="5%."))

AGUA = tit("Texto para as questões 10 e 11.") + ap("A possível escassez de água é uma das maiores preocupações da atualidade, considerada por alguns especialistas como o desafio maior do novo século. No entanto, tão importante quanto aumentar a oferta é investir na preservação da qualidade e no reaproveitamento da água de que dispomos hoje.")
X(10, "H", "Geografia", "Recursos hídricos", "<p>A contaminação dos lençóis freáticos vem de fertilizantes e do chorume de aterros (I); a umidade do solo diminui com o desmatamento, que reduz a infiltração e aumenta a evaporação (II); e as enchentes urbanas resultam da impermeabilização do solo pelo asfalto e pelas construções (III). Alternativa <strong>C</strong>.</p>",
  AGUA + p("A ação humana tem provocado algumas alterações quantitativas e qualitativas da água:")
  + I3("Contaminação de lençóis freáticos.", "Diminuição da umidade do solo.", "Enchentes e inundações.")
  + p("Pode-se afirmar que as principais ações humanas associadas às alterações I, II e III são, <u>respectivamente</u>,"),
  tags=["lençol freático", "impermeabilização"])
X(11, "H", "Geografia", "Recursos hídricos", "<p>Para preservar a qualidade da água, o essencial é proteger os mananciais da ocupação urbana (II) e proibir o despejo de esgoto sem tratamento (III). Alternativa <strong>C</strong>.</p><p>Represar rios perto de cidades (I) e transferir água entre bacias (IV) aumentam a oferta, mas não preservam a qualidade.</p>",
  AGUA + p("Algumas medidas podem ser propostas com relação aos problemas da água:")
  + '<ol type="I"><li>Represamento de rios e córregos próximo às cidades de maior porte.</li><li>Controle da ocupação urbana, especialmente em torno dos mananciais.</li><li>Proibição do despejo de esgoto industrial e doméstico sem tratamento nos rios e represas.</li><li>Transferência de volume de água entre bacias hidrográficas para atender as cidades que já apresentam alto grau de poluição em seus mananciais.</li></ol>'
  + p("As duas ações que devem ser tratadas como prioridades para a preservação da qualidade dos recursos hídricos são"),
  tags=["mananciais", "esgoto"], alts=A5("I e II.", "I e IV.", "II e III.", "II e IV.", "III e IV."))

X(12, "L", "Literatura", "Modernismo", "<p>Em “A terra é mui graciosa”, o advérbio “mui” imita a linguagem antiga da carta de Caminha; em “Tem macaco até demais”, a construção é coloquial, com “tem” no lugar de “há”. O par junta arcaísmo e coloquialismo. Alternativa <strong>A</strong>.</p><p>Nos outros pares, os dois versos têm o mesmo registro.</p>",
  p("Murilo Mendes, em um de seus poemas, dialoga com a carta de Pero Vaz de Caminha:") + "[[fig:1]]"
  + p("Arcaísmos e termos coloquiais misturam-se nesse poema, criando um efeito de contraste, como ocorre em:"),
  figs(("q12", "Poema de Murilo Mendes que parodia a carta de Pero Vaz de Caminha, em 18 versos: elogia a terra fértil, onde um caniço espetado no chão vira bengala de ouro, as frutas, os bichos de plumagens vistosas, o excesso de macacos, diamantes e esmeraldas; pede ao rei que reforce a arca e termina dizendo que ficará saudoso se for embora. Mistura expressões antigas, como “mui” e “oiro”, com outras coloquiais.")),
  ["Murilo Mendes", "arcaísmo"])

X(13, "N", "Física", "Energia elétrica", "<p>As três explicações são corretas: a urbanização leva mais gente a usar eletricidade (I); a busca de conforto aumenta o uso de geladeiras, chuveiros e iluminação (II); e a eletricidade substitui fontes como a lenha (III). Alternativa <strong>E</strong>.</p>",
  p("O setor residencial brasileiro é, depois da indústria, o que mais consome energia elétrica. A participação do setor residencial no consumo total de energia cresceu de forma bastante acelerada nos últimos anos. Esse crescimento pode ser explicado")
  + I3("pelo processo de urbanização no país, com a migração da população rural para as cidades.", "pela busca por melhor qualidade de vida, com a maior utilização de sistemas de refrigeração, iluminação e aquecimento.", "pela substituição de determinadas fontes de energia - a lenha, por exemplo - pela energia elétrica.")
  + p("Dentre as explicações apresentadas"),
  tags=["consumo residencial"])

X(14, "M", "Matemática", "Probabilidade geométrica", "<p>Pela figura, cada antena cobre um quarto de círculo de raio 10 km dentro do município: π × 10²/4 ≈ 78,5 km² cada, ou cerca de 157 km² no total. Dividindo pela área do município, 157/628 = 0,25: 25%. Alternativa <strong>B</strong>.</p>",
  p("Um município de 628 km² é atendido por duas emissoras de rádio cujas antenas A e B alcançam um raio de 10 km do município, conforme mostra a figura:") + "[[fig:1]]"
  + p("Para orçar um contrato publicitário, uma agência precisa avaliar a probabilidade que um morador tem de, circulando livremente pelo município, encontrar-se na área de alcance de pelo menos uma das emissoras.", "Essa probabilidade é de, aproximadamente,"),
  figs(("q14", "Mapa do município com as antenas A e B em dois cantos à direita; a área de alcance de cada uma, dentro do município, é um quarto de círculo de raio 10 km, hachurado.")),
  ["área do círculo", "probabilidade"])

X(15, "N", "Biologia", "Sangue", "<p>Defesa: glóbulos brancos abaixo do normal (5 a 10 mil) só em Maria (3,5 mil). Transporte de gases: hemácias abaixo de 4,5 milhões só em José (3,2 milhões). Coagulação: plaquetas abaixo de 200 mil só em Roberto (80 mil). Alternativa <strong>A</strong>.</p><p>Luísa tem glóbulos brancos e plaquetas acima do normal, mas a pergunta trata de deficiência.</p>",
  p("O hemograma é um exame laboratorial que informa o número de hemácias, glóbulos brancos e plaquetas presentes no sangue. A tabela apresenta os valores considerados normais para adultos. Os gráficos mostram os resultados do hemograma de 5 estudantes adultos. Todos os resultados são expressos em número de elementos por mm<sup>3</sup> de sangue.")
  + "[[fig:1]]"
  + p("Podem estar ocorrendo deficiência no sistema de defesa do organismo, prejuízos no transporte de gases respiratórios e alterações no processo de coagulação sanguínea, <u>respectivamente</u>, com os estudantes"),
  figs(("q15", "Tabela de valores normais para adultos: hemácias, 4,5 a 5,9 milhões/mm³; glóbulos brancos, 5 a 10 mil/mm³; plaquetas, 200 a 400 mil/mm³. Três gráficos de barras com os resultados de Abel, Luísa, José, Maria e Roberto. Plaquetas (mil/mm³): 300, 450, 300, 250, 80. Glóbulos brancos (mil/mm³): 11, 13, 6, 3,5, 5,5. Hemácias (milhões/mm³): 7, 5,5, 3,2, 5,9, 5.")),
  ["hemograma"], alts=dict(D[15], E="Luísa, Roberto e Abel."))

F_PIZZA = figs(("q16", "Gráfico de setores do consumo de energia elétrica nas residências: geladeira 30%, chuveiro 25%, lâmpadas incandescentes 20%, TV 10%, máquina de lavar 5%, ferro elétrico 5%, outros 5%."))
PIZZA = tit("Texto para as questões 16 e 17.") + p("A distribuição média, por tipo de equipamento, do consumo de energia elétrica nas residências no Brasil é apresentada no gráfico.") + "[[fig:1]]"
X(16, "N", "Física", "Energia elétrica", "<p>O consumo de cada tipo de equipamento é potência × tempo de uso × quantidade de aparelhos. As três variáveis influenciam a fração de cada um no total. Alternativa <strong>E</strong>.</p><p>Uma geladeira tem potência baixa, mas funciona o dia todo; um chuveiro tem potência alta e funciona pouco; e várias lâmpadas somam seu consumo.</p>",
  PIZZA + p("Em associação com os dados do gráfico, considere as variáveis:") + I3("Potência do equipamento.", "Horas de funcionamento.", "Número de equipamentos.")
  + p("O valor das frações percentuais do consumo de energia depende de"), F_PIZZA, ["consumo de energia"])
X(17, "N", "Física", "Energia elétrica", "<p>O chuveiro consome 25% de 300 kWh = 75 kWh por mês. Com 5 kW, isso dá 75/5 = 15 horas = 900 minutos por mês. Divididos por 30 dias e por 4 moradores: 900/120 = 7,5 minutos por banho. Alternativa <strong>C</strong>.</p>",
  PIZZA + p("Como medida de economia, em uma residência com 4 moradores, o consumo mensal médio de energia elétrica foi reduzido para 300 kWh. Se essa residência obedece à distribuição dada no gráfico, e se nela há um único chuveiro de 5000 W, pode-se concluir que <u>o banho diário de cada morador passou a ter uma duração média, em minutos</u>, de"),
  F_PIZZA, ["kWh", "potência"], alts=A5("2,5.", "5,0.", "7,5.", "10,0.", "12,0."))

X(18, "H", "História", "Idade Média", "<p>Roger Bacon imagina máquinas que permitiriam ao ser humano dominar a natureza (navios rápidos, carros sem animais, máquinas voadoras e submarinas) e valoriza o método experimental. Essas ideias anunciam o espírito do Renascimento. Alternativa <strong>E</strong>.</p><p>Bacon foi condenado justamente por se afastar da tradição teológica (A, D).</p>",
  p("O franciscano Roger Bacon foi condenado, entre 1277 e 1279, por dirigir ataques aos teólogos, por uma suposta crença na alquimia, na astrologia e no método experimental, e também por introduzir, no ensino, as idéias de Aristóteles. Em 1260, Roger Bacon escreveu:")
  + ap("“Pode ser que se fabriquem máquinas graças às quais os maiores navios, dirigidos por um único homem, se desloquem mais depressa do que se fossem cheios de remadores; que se construam carros que avancem a uma velocidade incrível sem a ajuda de animais; que se fabriquem máquinas voadoras nas quais um homem (...) bata o ar com asas como um pássaro. (...) Máquinas que permitam ir ao fundo dos mares e dos rios”")
  + fonte("Apud BRAUDEL, Fernand. <em>Civilização material, economia e capitalismo: séculos XV-XVIII</em>. São Paulo: Martins Fontes, 1996, vol. 3.")
  + p("Considerando a dinâmica do processo histórico, pode-se afirmar que as idéias de Roger Bacon"),
  tags=["Roger Bacon", "Renascimento"])

X(19, "N", "Biologia", "Evolução", "<p>Diabéticos e hemofílicos, que antes teriam menos chance de sobreviver e deixar filhos, passam a viver normalmente graças aos tratamentos. A medicina reduz a ação da seleção natural sobre essas características. Alternativa <strong>A</strong>.</p><p>Os remédios não alteram o genoma (B, D) nem impedem a transmissão dos genes (C), e a evolução humana não é interrompida (E).</p>",
  ap("“Os progressos da medicina condicionaram a sobrevivência de número cada vez maior de indivíduos com constituições genéticas que só permitem o bem-estar quando seus efeitos são devidamente controlados através de drogas ou procedimentos terapêuticos. São exemplos os diabéticos e os hemofílicos, que só sobrevivem e levam vida relativamente normal ao receberem suplementação de insulina ou do fator VIII da coagulação sanguínea”.")
  + fonte("SALZANO, M. Francisco. <em>Ciência Hoje</em>: SBPC: 21(125), 1996.")
  + p("Essas afirmações apontam para aspectos importantes que podem ser relacionados à evolução humana. Pode-se afirmar que, nos termos do texto,"),
  tags=["seleção natural", "medicina"])

X(20, "L", "Língua Portuguesa", "Figuras de linguagem", "<p>Em B, a casa que o operário construía “sendo a sua liberdade / era a sua escravidão”: liberdade e escravidão se excluem e aparecem juntas, como no oxímoro “feliz segunda-feira” de Garfield. Alternativa <strong>B</strong>.</p><p>D é um quiasmo (inversão de termos), sem significados que se excluam.</p>",
  p("<u>Oxímoro</u> (ou <u>paradoxo</u>) é uma construção textual que agrupa significados que se excluem mutuamente. Para Garfield, a frase de saudação de Jon (tirinha abaixo) expressa o maior de todos os oxímoros.") + "[[fig:1]]"
  + fonte("<em>Folha de S. Paulo</em>. 31 de julho de 2000.")
  + p("Nas alternativas abaixo, estão transcritos versos retirados do poema “O operário em construção”. Pode-se afirmar que ocorre um oxímoro em")
  + fonte("MORAES, Vinicius de. <em>Antologia Poética</em>. São Paulo: Companhia das Letras, 1992."),
  figs(("q20", "Tira de Garfield, de Jim Davis, em três quadros: Jon diz “Feliz segunda-feira!” e Garfield, com cara de tédio, pensa: “A mãe de todos os oxímoros...”."),
       ("q20a", "Dois versos de Vinicius de Moraes: o operário erguia casas onde antes só havia chão."),
       ("q20b", "Três versos de Vinicius de Moraes: a casa que o operário fazia, sendo a sua liberdade, era a sua escravidão."),
       ("q20c", "Quatro versos de Vinicius de Moraes: na casa vazia que ele mesmo levantara, nascia um mundo novo de que ele nem suspeitava."),
       ("q20d", "Dois versos de Vinicius de Moraes: o operário faz a coisa e a coisa faz o operário."),
       ("q20e", "Três versos de Vinicius de Moraes: ele, um humilde operário, que sabia exercer a profissão.")),
  ["oxímoro", "Vinicius de Moraes"], alts=ALT(2))

X(21, "N", "Química", "Densidade", "<p>Um litro com 96% de álcool (800 g/L) e 4% de água (1000 g/L) tem densidade 0,96 × 800 + 0,04 × 1000 = 768 + 40 = 808 g/L. Mais água aumenta a densidade. Dentro da norma (ou com menos água) estão só os postos com até 808 g/L: IV (808) e V (805). Alternativa <strong>E</strong>.</p>",
  p("Pelas normas vigentes, o litro do álcool hidratado que abastece os veículos deve ser constituído de 96% de álcool puro e 4% de água (em volume). As densidades desses componentes são dadas na tabela.")
  + tabela(["Substância", "Densidade (g/L)"], [["Água", "1000"], ["Álcool", "800"]])
  + p("Um técnico de um órgão de defesa do consumidor inspecionou cinco postos suspeitos de venderem álcool hidratado fora das normas. Colheu uma amostra do produto em cada posto, mediu a densidade de cada uma, obtendo:")
  + tabela(["Posto", "Densidade do combustível (g/L)"], [["I", "822"], ["II", "820"], ["III", "815"], ["IV", "808"], ["V", "805"]])
  + p("A partir desses dados, o técnico pôde concluir que estavam com o combustível adequado somente os postos"),
  tags=["densidade de misturas", "álcool combustível"], alts=dict(D[21], E="IV e V."))

ENXOFRE = (tit("Texto para as questões 22 e 23.") + p("O esquema representa o ciclo do enxofre na natureza, sem considerar a intervenção humana.") + "[[fig:1]]"
  + fonte("Adaptado de BRIMBLECOMBE, P. <em>Air Composition and Chemistry</em>. Cambridge: Cambridge University Press, 1996."))
F_ENX = figs(("q22", "Esquema do ciclo do enxofre: vulcões liberam SO2 e H2S para o ar; seres vivos da terra e do mar liberam compostos orgânicos de enxofre e H2S; no ar, SO2 vira SO3 e sulfatos, que voltam como chuva ácida; sulfatos ficam na litosfera e na água do mar; e há transferência de sulfatos do mar para a terra."))
X(22, "N", "Química", "Ciclo do enxofre", "<p>No esquema, atmosfera, litosfera, hidrosfera e biosfera recebem compostos de enxofre (II), os transportam (III) e também os liberam (IV). I é falsa: sem intervenção humana, a circulação de enxofre é natural e não se chama poluição. Alternativa <strong>E</strong>.</p>",
  ENXOFRE + p("O ciclo representado mostra que a atmosfera, a litosfera, a hidrosfera e a biosfera, naturalmente,")
  + '<ol type="I"><li>são poluídas por compostos de enxofre.</li><li>são destinos de compostos de enxofre.</li><li>transportam compostos de enxofre.</li><li>são fontes de compostos de enxofre.</li></ol>'
  + p("Dessas afirmações, estão corretas, apenas,"), F_ENX, ["ciclos biogeoquímicos"], quim=True)
X(23, "N", "Química", "Ciclo do enxofre", "<p>Diesel e outros combustíveis de veículos pesados contêm enxofre e liberam SO2 na queima; a obtenção de metais a partir de sulfetos (como a ustulação da pirita ou da blenda) também libera SO2. Alternativa <strong>A</strong>.</p><p>Óxidos metálicos (B, C) não contêm enxofre.</p>",
  ENXOFRE + p("Algumas atividades humanas interferiram significativamente no ciclo natural do enxofre, alterando as quantidades das substâncias indicadas no esquema. Ainda hoje isso ocorre, apesar do grande controle por legislação.", "Pode-se afirmar que duas dessas interferências são resultantes da"),
  F_ENX, ["dióxido de enxofre", "sulfetos"], quim=True)

X(24, "M", "Matemática", "Geometria espacial", "<p>Pela planificação, a abertura da tampa permite passar sólidos de até cerca de 5 cm × 2 cm de seção. O cone (base de 3 cm de diâmetro e 1 cm de altura), o cubo de 2 cm, o paralelepípedo (passando pela face de 2 cm × 3 cm, no sentido certo) e o cilindro (2 cm de diâmetro) passam; a esfera, de 3 cm de diâmetro em todas as direções, não. Alternativa <strong>C</strong>.</p>",
  p("Um fabricante de brinquedos recebeu o projeto de uma caixa que deverá conter cinco pequenos sólidos, colocados na caixa por uma abertura em sua tampa. A figura representa a planificação da caixa, com as medidas dadas em centímetros.") + "[[fig:1]]"
  + p("Os sólidos são fabricados nas formas de")
  + '<ol type="I"><li>um cone reto de altura 1 cm e raio da base 1,5 cm.</li><li>um cubo de aresta 2 cm.</li><li>uma esfera de raio 1,5 cm.</li><li>um paralelepípedo retangular reto, de dimensões 2 cm, 3 cm e 4 cm.</li><li>um cilindro reto de altura 3 cm e raio da base 1 cm.</li></ol>'
  + p("O fabricante não aceitou o projeto, pois percebeu que, pela abertura dessa caixa, só poderia colocar os sólidos dos tipos"),
  figs(("q24", "Planificação de uma caixa com medidas em centímetros: fundo de 15 por 10; laterais de altura 5 e 6; e abas de 4 e 5, que formam a tampa com uma abertura.")),
  ["planificação", "sólidos"])

X(25, "N", "Química", "Chuva ácida", "<p>I e II podem ocorrer: a água ácida que chega ao manancial pode matar peixes, e a chuva ácida no campo acidifica o solo, que pode ser corrigido com calcário (calagem). III não: a transpiração das plantas não neutraliza ácidos. Alternativa <strong>C</strong>.</p>",
  p("Uma região industrial lança ao ar gases como o dióxido de enxofre e óxidos de nitrogênio, causadores da chuva ácida. A figura mostra a dispersão desses gases poluentes.") + "[[fig:1]]"
  + p("Considerando o ciclo da água e a dispersão dos gases, analise as seguintes possibilidades:")
  + I3("As águas de escoamento superficial e de precipitação que atingem o manancial poderiam causar aumento de acidez da água do manancial e provocar a morte de peixes.",
       "A precipitação na região rural poderia causar aumento de acidez do solo e exigir procedimentos corretivos, como a calagem.",
       "A precipitação na região rural, embora ácida, não afetaria o ecossistema, pois a transpiração dos vegetais neutralizaria o excesso de ácido.")
  + p("Dessas possibilidades,"),
  figs(("q25", "Desenho de uma paisagem com fábricas soltando fumaça à esquerda; a nuvem de poluentes se espalha sobre uma floresta, uma região rural e um manancial com peixes, à direita, onde cai chuva.")),
  ["chuva ácida", "calagem"])

X(26, "N", "Biologia", "Biodiversidade", "<p>Para recuperar a diversidade biológica, é preciso criar muitas espécies e, em cada uma, indivíduos suficientes para manter a diversidade genética. Alternativa <strong>D</strong>.</p><p>Cruzar espécies diferentes (A) não gera novas espécies viáveis, e concentrar-se em uma ou poucas espécies (B, C, E) não recupera a diversidade.</p>",
  p("Várias estratégias estão sendo consideradas para a recuperação da diversidade biológica de um ambiente degradado, dentre elas, a criação de vertebrados em cativeiro. Com esse objetivo, a iniciativa mais adequada, dentre as alternativas abaixo, seria criar"),
  tags=["diversidade genética", "cativeiro"], alts=dict(D[26], E="vários indivíduos de poucas espécies, de modo a garantir, para cada espécie, uma população geneticamente homogênea."))

X(27, "L", "Língua Portuguesa", "Sinonímia", "<p>Em I, “estilo próprio” é estilo peculiar, só dela. Em II, “próprio para adolescente” é adequado. Em III, “próprio da idade” é característico da idade. Alternativa <strong>B</strong>.</p><p>“Adequado” não serve para I (o estilo não é adequado, é só dela), e “exclusivo” não serve para II (o filme não é só para adolescentes).</p>",
  p("Nas conversas diárias, utiliza-se freqüentemente a palavra “próprio” e ela se ajusta a várias situações. Leia os exemplos de diálogos:")
  + ap("I<br>– A Vera se veste diferente!<br>– É mesmo, é que ela tem um estilo <u>próprio</u>.", "II<br>– A Lena já viu esse filme uma dezena de vezes! Eu não consigo ver o que ele tem de tão maravilhoso assim.<br>– É que ele é <u>próprio</u> para adolescente.",
       "III<br>– Dora, o que eu faço? Ando tão preocupada com o Fabinho! Meu filho está impossível!<br>– Relaxa, Tânia! É <u>próprio</u> da idade. Com o tempo, ele se acomoda.")
  + p("Nas ocorrências I, II e III, “próprio” é sinônimo de, respectivamente,"),
  tags=["polissemia", "sinônimos"])

X(28, "N", "Biologia", "Ecologia", "<p>No gráfico, durante o uso do veneno as populações oscilam muito; depois que ele é suspenso, as oscilações de larvas e parasitas diminuem e as populações se estabilizam. Isso mostra que as interações negativas perdem efeito com o tempo, e o veneno não é necessário. Alternativa <strong>E</strong>.</p><p>O veneno afeta as populações (A), e elas não mudam o tipo de interação (C).</p>",
  p("Um produtor de larvas aquáticas para alimentação de peixes ornamentais usou veneno para combater parasitas, mas suspendeu o uso do produto quando os custos se revelaram antieconômicos. O gráfico registra a evolução das populações de larvas e parasitas.") + "[[fig:1]]"
  + p("O aspecto <u>biológico</u>, ressaltado a partir da leitura do gráfico, que pode ser considerado o melhor argumento para que o produtor não retome o uso do veneno é:"),
  figs(("q28", "Gráfico do número de indivíduos de larvas e parasitas ao longo de 36 meses, com fases marcadas: antes do surgimento do parasita (0 a 6), aparecimento do parasita (6 a 12), controle com veneno (12 a 18) e sem veneno (depois de 18). Com o parasita e durante o controle, as curvas oscilam muito; sem veneno, as oscilações diminuem e as duas populações se estabilizam, com as larvas acima dos parasitas.")),
  ["parasitismo", "controle de pragas"])

X(29, "M", "Matemática", "Probabilidade", "<p>Os ônibus saem às 6h00 (ANDABEM), 6h10 (BOMPASSEIO), 6h30 (ANDABEM), 6h40 (BOMPASSEIO) e assim por diante. Quem chega entre 6h10 e 6h30 (20 minutos) pega o ANDABEM; quem chega entre 6h30 e 6h40 (10 minutos), o BOMPASSEIO. A probabilidade do ANDABEM é o dobro. Alternativa <strong>D</strong>.</p>",
  p("Num determinado bairro há duas empresas de ônibus, ANDABEM e BOMPASSEIO, que fazem o trajeto levando e trazendo passageiros do subúrbio ao centro da cidade. Um ônibus de cada uma dessas empresas parte do terminal a cada 30 minutos, nos horários indicados na tabela.")
  + tabela(["ANDABEM", "BOMPASSEIO"], [["…", "…"], ["6h00min", "6h10min"], ["6h30min", "6h40min"], ["7h00min", "7h10min"], ["7h30min", "7h40min"], ["…", "…"]])
  + p("Carlos mora próximo ao terminal de ônibus e trabalha na cidade. Como não tem hora certa para chegar ao trabalho e nem preferência por qualquer das empresas, toma sempre o primeiro ônibus que sai do terminal. Nessa situação, pode-se afirmar que a probabilidade de Carlos viajar num ônibus da empresa ANDABEM é"),
  tags=["probabilidade", "intervalos de tempo"], alts=dict(D[29], E="três vezes maior do que a probabilidade de ele viajar num ônibus da empresa BOMPASSEIO."))

HOBBES = (tit("Texto para as questões 30 e 31.")
  + ap("I - Para o filósofo inglês Thomas Hobbes (1588-1679), o <em>estado de natureza</em> é um <em>estado de guerra</em> universal e perpétua. Contraposto ao estado de natureza, entendido como estado de guerra, o <em>estado de paz</em> é a sociedade civilizada.")
  + p("Dentre outras tendências que dialogam com as idéias de Hobbes, destaca-se a definida pelo texto abaixo.")
  + ap("II - <em>Nem todas as guerras são injustas e correlativamente, nem toda paz é justa, razão pela qual a guerra nem sempre é um desvalor, e a paz nem sempre um valor.</em>")
  + fonte("BOBBIO, N.; MATTEUCCI, N.; PASQUINO, G. <em>Dicionário de Política</em>, 5ª ed. Brasília: Universidade de Brasília; São Paulo: Imprensa Oficial do Estado, 2000."))
X(30, "H", "Filosofia", "Hobbes", "<p>Para Hobbes, a paz é o estado da sociedade civilizada, oposto à guerra do estado de natureza. Para o texto II, a paz nem sempre é justa, logo não é um valor absoluto. Alternativa <strong>B</strong>.</p><p>Hobbes não vê a guerra como valor (C) e associa a paz à civilização, não à natureza (E).</p>",
  HOBBES + p("Comparando as idéias de Hobbes (texto I) com a tendência citada no texto II, pode-se afirmar que"), tags=["Hobbes", "guerra e paz"])
X(31, "H", "Filosofia", "Guerra justa", "<p>Para justificar as ações militares no Iraque e na Sérvia, a OTAN argumentaria que se tratava de guerras justas, por fins justos (defesa do Kuwait, proteção de populações): é a ideia do texto II. Alternativa <strong>D</strong>.</p><p>A teoria de Hobbes descreve o estado de natureza, não justifica guerras entre Estados (A, B).</p>",
  HOBBES + p("Tropas da Aliança do Tratado do Atlântico Norte (OTAN) invadiram o Iraque em 1991 e atacaram a Sérvia em 1999.", "Para responder aos críticos dessas ações, a OTAN usaria, possivelmente, argumentos baseados"),
  tags=["OTAN", "guerra justa"])

X(32, "H", "Geografia", "Cartografia", "<p>As projeções de Mercator e de Peters são cilíndricas: a superfície da Terra é projetada sobre um cilindro tangente ao Equador, depois desenrolado. A figura C mostra o cilindro envolvendo o globo nessa posição. Alternativa <strong>C</strong>.</p><p>A é a projeção plana (azimutal) e B, a cônica.</p>",
  p("Existem diferentes formas de representação plana da superfície da Terra (planisfério). Os planisférios de Mercator e de Peters são atualmente os mais utilizados.") + "[[fig:1]]"
  + p("Apesar de usarem projeções, respectivamente, conforme e equivalente, ambas utilizam como base da projeção o modelo:"),
  figs(("q32", "Dois planisférios lado a lado: o de Mercator, em que as regiões de alta latitude aparecem muito ampliadas, e o de Peters, em que os continentes aparecem alongados no sentido norte-sul."),
       ("q32a", "Globo com um plano tangente apoiado no polo."), ("q32b", "Globo dentro de um cone."),
       ("q32c", "Globo dentro de um cilindro vertical, tangente ao Equador."), ("q32d", "Globo dentro de um cilindro deitado, tangente a um meridiano."), ("q32e", "Globo com um plano vertical tangente ao lado.")),
  ["projeções cartográficas", "Mercator e Peters"], alts=ALT(2))

X(33, "N", "Biologia", "Ecologia", "<p>Nos fragmentos degradados, a floresta perdeu estrutura e variedade de ambientes. Com menos hábitats e menos diversos, as espécies mais exigentes desaparecem, e só duas das cinco resistem. Alternativa <strong>B</strong>.</p><p>Isolamento reprodutivo entre espécies (E) é normal e não explica o desaparecimento.</p>",
  p("Numa região, originalmente ocupada por Mata Atlântica, havia, no passado, cinco espécies de pássaros de um mesmo gênero. Nos dias atuais, essa região se reduz a uma reserva de floresta primária, onde ainda ocorrem as cinco espécies, e a fragmentos de floresta degradada, onde só se encontram duas das cinco espécies.",
    "O desaparecimento das três espécies nas regiões degradadas pode ser explicado pelo fato de que, nessas regiões, ocorreu"),
  tags=["fragmentação de hábitats"], alts=dict(D[33], E="aumento do grau de isolamento reprodutivo interespecífico."))

X(34, "L", "Literatura", "Romantismo", "<p>No dístico final, a voz sombria anuncia: “Terás o sono sob a lájea fria”. O “sono” sob a lápide é a imagem da morte. Alternativa <strong>E</strong>.</p><p>“Dormir à tarde à sombra da palmeira” (D) é um sono de prazer, ligado ao desejo de viver.</p>",
  p("O trecho a seguir é parte do poema “Mocidade e morte”, do poeta romântico Castro Alves:")
  + ap("Oh! eu quero viver, beber perfumes<br>Na flor silvestre, que embalsama os ares;<br>Ver minh'alma adejar pelo infinito,<br>Qual branca vela n'amplidão dos mares.<br>No seio da mulher há tanto aroma...<br>Nos seus beijos de fogo há tanta vida...<br>— Árabe errante, vou dormir à tarde<br>À sombra fresca da palmeira erguida.",
       "Mas uma voz responde-me sombria:<br>Terás o sono sob a lájea fria.")
  + fonte("ALVES, Castro. <em>Os melhores poemas de Castro Alves</em>. Seleção de Lêdo Ivo. São Paulo: Global, 1983.")
  + p("Esse poema, como o próprio título sugere, aborda o inconformismo do poeta com a antevisão da morte prematura, ainda na juventude. A imagem da morte aparece na palavra"),
  tags=["Castro Alves", "metáfora"])

X(35, "N", "Química", "Segurança química", "<p>Materiais radioativos e gases como o cloro são úteis (medicina, tratamento de água), então proibi-los (I) não é adequado. O que evita acidentes é controlar compra, uso e destino (II), instruir os usuários (III) e informar a população sobre os riscos (IV). Alternativa <strong>E</strong>.</p>",
  p("Considere os seguintes acontecimentos ocorridos no Brasil:")
  + "<ul><li>Goiás, 1987 - Um equipamento contendo césio radioativo, utilizado em medicina nuclear, foi encontrado em um depósito de sucatas e aberto por pessoa que desconhecia o seu conteúdo. Resultado: mortes e conseqüências ambientais sentidas até hoje.</li><li>Distrito Federal, 1999 - Cilindros contendo cloro, gás bactericida utilizado em tratamento de água, encontrados em um depósito de sucatas, foram abertos por pessoa que desconhecia o seu conteúdo. Resultado: mortes, intoxicações e conseqüências ambientais sentidas por várias horas.</li></ul>"
  + p("Para evitar que novos acontecimentos dessa natureza venham a ocorrer, foram feitas as seguintes propostas para a atuação do Estado:")
  + '<ol type="I"><li>Proibir o uso de materiais radioativos e gases tóxicos.</li><li>Controlar rigorosamente a compra, uso e destino de materiais radioativos e de recipientes contendo gases tóxicos.</li><li>Instruir usuários sobre a utilização e descarte destes materiais.</li><li>Realizar campanhas de esclarecimentos à população sobre os riscos da radiação e da toxicidade de determinadas substâncias.</li></ol>'
  + p("Dessas propostas, são adequadas apenas"),
  tags=["césio-137", "lixo perigoso"])

X(36, "N", "Física", "Leitura de gráficos", "<p>Em 1970, a energia elétrica era cerca de 2 de um total de cerca de 23 (×10<sup>6</sup> tep): perto de 10%. Em 1995, era cerca de 20 de um total de cerca de 33: perto de 60%. Alternativa <strong>B</strong>.</p>",
  p("O consumo total de energia nas residências brasileiras envolve diversas fontes, como eletricidade, gás de cozinha, lenha, etc. O gráfico mostra a evolução do consumo de energia elétrica residencial, comparada com o consumo total de energia residencial, de 1970 a 1995.") + "[[fig:1]]"
  + fonte("*tep = toneladas equivalentes de petróleo. Fonte: valores calculados através dos dados obtidos de: http://infoener.iee.usp.br/1999.")
  + p("Verifica-se que a participação <u>percentual</u> da energia elétrica no total de energia gasto nas residências brasileiras cresceu entre 1970 e 1995, passando, aproximadamente, de"),
  figs(("q36", "Gráfico de linhas do consumo de energia (×10⁶ tep) de 1970 a 1995. Energia total: cerca de 23, 24, 25, 26, 27 e 33. Energia elétrica: cerca de 2, 4, 6, 9, 13 e 20.")),
  ["porcentagem", "leitura de gráfico"], alts=dict(D[36], E="40% para 80%."))

X(37, "N", "Física", "Fontes de energia", "<p>Pelo gráfico, a energia nuclear representa cerca de 7% do total e o gás natural, cerca de 21%. Para cobrir 7 pontos, o gás precisaria crescer 7/21 ≈ 33%. Alternativa <strong>D</strong>.</p><p>7% (perto de A) seria o aumento em pontos percentuais do total, e não o aumento da produção de gás.</p>",
  p("Segundo um especialista em petróleo (<em>Estado de S. Paulo</em>, 5 de março de 2000), o consumo total de energia mundial foi estimado em 8,3 bilhões de toneladas equivalentes de petróleo (tep) para 2001. A porcentagem das diversas fontes da energia consumida no globo é representada no gráfico.") + "[[fig:1]]"
  + p("Segundo as informações apresentadas, para substituir a energia nuclear utilizada é necessário, por exemplo, aumentar a energia proveniente do gás natural em cerca de"),
  figs(("q37", "Gráfico de barras da porcentagem da energia mundial por fonte: petróleo, cerca de 40%; carvão, cerca de 26%; gás, cerca de 21%; nuclear, cerca de 7%; hidrelétrica, cerca de 4%; outros, cerca de 2%.")),
  ["porcentagem", "matriz energética"])

X(38, "H", "Geografia", "Migração", "<p>Na tira, o migrante nordestino é expulso da cidade (“Cai fora da minha city!”), um caso de discriminação; e ele responde que é ele quem dá “a sustança”, isto é, quem sustenta a cidade com seu trabalho. Alternativa <strong>B</strong>.</p>",
  "[[fig:1]]" + fonte("<em>Folha de S. Paulo</em>. 06 de outubro de 1992.")
  + p("O <u>problema enfrentado</u> pelo migrante e o <u>sentido da expressão “sustança”</u> expressos nos quadrinhos, podem ser, respectivamente, relacionados a"),
  figs(("q38", "Tira “Piratas do Tietê”, de Laerte, em dois quadros. Um homem grita para um migrante nordestino, de chapéu de couro: “Cai fora da minha city!”, e o migrante responde: “Apois, tá certo, só vou levar o que é meu...”. No segundo quadro, o migrante vai embora carregando nas costas um grande volume, com a legenda “a sustança”.")),
  ["migração nordestina", "Laerte"])

X(39, "H", "Geografia", "Demografia", "<p>A queda da fecundidade no Brasil (de 7 filhos no século XIX para 2,3 em 1996) está ligada à urbanização, ao maior acesso à informação e a métodos contraceptivos e à entrada das mulheres no mercado de trabalho. Alternativa <strong>E</strong>.</p><p>O Brasil não teve política demográfica oficial nem leis que limitassem filhos ou casamentos (A, B, C).</p>",
  p("Os dados da tabela mostram uma tendência de diminuição, no Brasil, do número de filhos por mulher.")
  + tabela(["Época", "Número de filhos por mulher"], [["Século XIX", "7"], ["1960", "6,2"], ["1980", "4,01"], ["1991", "2,9"], ["1996", "2,32"]])
  + fonte("Fonte: IBGE, contagem da população de 1996.") + p("Dentre as alternativas, a que melhor explica essa tendência é:"),
  tags=["fecundidade"])

X(40, "M", "Matemática", "Porcentagem", "<p>Brancos e nulos somam 9% + 11% = 20%, então os votos válidos são 80% dos eleitores. O vencedor teve 51% de 80%: 0,51 × 0,80 = 40,8%, cerca de 41%. Alternativa <strong>B</strong>.</p><p>51% (perto de E) seria o percentual sobre os votos válidos, e não sobre todos os eleitores.</p>",
  p("Nas últimas eleições presidenciais de um determinado país, onde 9% dos eleitores votaram em branco e 11% anularam o voto, o vencedor obteve 51% dos votos válidos. Não são considerados válidos os votos em branco e nulos.", "Pode-se afirmar que o vencedor, de fato, obteve de todos os eleitores um percentual de votos da ordem de"),
  tags=["votos válidos"])

X(41, "N", "Biologia", "Saúde pública", "<p>Combater o mosquito (II) e vacinar nas áreas endêmicas e vizinhas (III) são ações eficazes e possíveis. Exterminar os animais silvestres que servem de reservatório do vírus (I), como os macacos, não é viável nem desejável. Alternativa <strong>D</strong>.</p>",
  p("A partir do primeiro semestre de 2000, a ocorrência de casos humanos de febre amarela silvestre extrapolou as áreas endêmicas, com registro de casos em São Paulo e na Bahia, onde os últimos casos tinham ocorrido em 1953 e 1948. Para controlar a febre amarela silvestre e prevenir o risco de uma reurbanização da doença, foram propostas as seguintes ações:")
  + I3("Exterminar os animais que servem de reservatório do vírus causador da doença.", "Combater a proliferação do mosquito transmissor.", "Intensificar a vacinação nas áreas onde a febre amarela é endêmica e em suas regiões limítrofes.")
  + p("É efetiva e possível de ser implementada uma estratégia envolvendo"),
  tags=["febre amarela"])

X(42, "L", "Literatura", "Realismo", "<p>O narrador diz que “isto não é romance, em que o autor sobredoura a realidade e fecha os olhos às sardas e espinhas”: critica a idealização romântica, que esconde os defeitos da realidade. Alternativa <strong>A</strong>.</p><p>As outras frases descrevem a personagem, sem comentar o estilo de época.</p>",
  p("No trecho abaixo, o narrador, ao descrever a personagem, critica sutilmente um outro estilo de época: o romantismo.")
  + ap("“Naquele tempo contava apenas uns quinze ou dezesseis anos; era talvez a mais atrevida criatura da nossa raça, e, com certeza, a mais voluntariosa. Não digo que já lhe coubesse a primazia da beleza, entre as mocinhas do tempo, porque isto não é romance, em que o autor sobredoura a realidade e fecha os olhos às sardas e espinhas; mas também não digo que lhe maculasse o rosto nenhuma sarda ou espinha, não. Era bonita, fresca, saía das mãos da natureza, cheia daquele feitiço, precário e eterno, que o indivíduo passa a outro indivíduo, para os fins secretos da criação.”")
  + fonte("ASSIS, Machado de. <em>Memórias Póstumas de Brás Cubas</em>. Rio de Janeiro: Jackson, 1957.")
  + p("A frase do texto em que se percebe a crítica do narrador ao romantismo está transcrita na alternativa:"),
  tags=["Machado de Assis", "crítica ao Romantismo"])

X(43, "N", "Biologia", "Recursos hídricos", "<p>Pelo gráfico, a água restituída sem qualidade soma cerca de 1.800 bilhões de m³ por ano, dos quais cerca de 1.550 vêm da agricultura, que usa adubos e agrotóxicos. Mais da metade dessa água vem da agricultura. Alternativa <strong>C</strong>.</p><p>A indústria e a energia restituem bem menos água sem qualidade que a agricultura (B, D). E A é falsa: a água usada volta ao ciclo hidrológico, ainda que sem qualidade.</p>",
  p("Boa parte da água utilizada nas mais diversas atividades humanas não retorna ao ambiente com qualidade para ser novamente consumida. O gráfico mostra alguns dados sobre esse fato, em termos dos setores de consumo.") + "[[fig:1]]"
  + fonte("Fonte: adaptado de MARGAT, Jean-François. A água ameaçada pelas atividades humanas. In WIKOWSKI, N. (Coord.). <em>Ciência e tecnologia hoje</em>. São Paulo: Ensaio, 1994.")
  + p("Com base nesses dados, é possível afirmar que"),
  figs(("q43", "Gráfico de barras “Consumo e restituição de água no mundo (em bilhões de m³/ano)”. Consumo: coletividade cerca de 200, indústria e energia cerca de 700, agricultura cerca de 2.300, total cerca de 3.200. Restituição sem qualidade: coletividade cerca de 100, indústria e energia cerca de 150, agricultura cerca de 1.550, total cerca de 1.800.")),
  ["uso da água", "agricultura"])

X(44, "H", "Sociologia", "Violência", "<p>Em todos os anos, de 1995 a 1998, as barras dos estados com pena de morte são mais altas que as dos estados sem pena de morte. Alternativa <strong>C</strong>.</p><p>A taxa caiu nos dois grupos (A) e não caiu pela metade (E): passou de cerca de 37 para cerca de 30.</p>",
  p("O gráfico compara o número de homicídios por grupo de 100.000 habitantes entre 1995 e 1998 nos EUA, em estados com e sem pena de morte.") + "[[fig:1]]" + fonte("<em>Carta Capital</em>, 6 de dezembro de 2000.")
  + p("Com base no gráfico, pode-se afirmar que"),
  figs(("q44", "Gráfico de barras de homicídios por 100.000 habitantes, de 1995 a 1998. Estados com pena de morte: cerca de 37, 35, 32 e 30. Estados sem pena de morte: cerca de 32, 27, 27 e 25.")),
  ["pena de morte", "leitura de gráfico"])

X(45, "H", "História", "Tempo histórico", "<p>Na escala do texto, cada hora vale cem anos a partir do nascimento de Cristo. As Grandes Navegações começaram no século XV e ganharam força por volta de 1500, o que corresponde às 15 horas. Alternativa <strong>A</strong>.</p><p>A Idade Moderna começa por volta de 1450, às 14h30, e não às 10h (B); as escolas dos mosteiros perderam o monopólio por volta de 1000–1100, no meio da Idade Média (E).</p>",
  p("O texto abaixo reproduz parte de um diálogo entre dois personagens de um romance.")
  + ap("– Quer dizer que a Idade Média durou dez horas? – Perguntou Sofia.<br>– Se cada hora valer cem anos, então sua conta está certa. Podemos imaginar que Jesus nasceu à meia-noite, que Paulo saiu em peregrinação missionária pouco antes da meia-noite e meia e morreu quinze minutos depois, em Roma. Até as três da manhã a fé cristã foi mais ou menos proibida. (...) Até as dez horas as escolas dos mosteiros detiveram o monopólio da educação. Entre dez e onze horas são fundadas as primeiras universidades.")
  + fonte("Adaptado de GAARDER, Jostein. <em>O Mundo de Sofia</em>, Romance da História da Filosofia. São Paulo: Cia das Letras, 1997.")
  + p("O ano de 476 d.C., época da queda do Império Romano do Ocidente, tem sido usado como marco para o início da Idade Média. De acordo com a escala de tempo apresentada no texto, que considera como ponto de partida o início da Era Cristã, pode-se afirmar que"),
  tags=["escala de tempo", "O Mundo de Sofia"])

X(46, "H", "Geografia", "Demografia", "<p>Os Estados Unidos, país desenvolvido de baixa natalidade, continuam crescendo porque atraem muitos imigrantes. Alternativa <strong>C</strong>.</p><p>A Europa tem crescimento vegetativo baixo (A); nos países citados, o crescimento vem da natalidade alta, associada a baixos índices de desenvolvimento (D), e não a condições de vida favoráveis (E).</p>",
  ap("“... a população mundial deverá ser de 9,3 bilhões de pessoas em 2050. Ou seja, será 50% maior que os 6,1 bilhões de meados do ano 2000. (...) Essas são as principais conclusões do relatório Perspectivas da População Mundial – Revisão 2000, preparado pela Organização das Nações Unidas (ONU). (...) Apenas seis países respondem por quase metade desse aumento: Índia (21%), China (12%), Paquistão (5%), Nigéria (4%), Bangladesh (4%) e Indonésia (3%).",
     "Esses elevados índices de expansão contrastam com os dos países mais desenvolvidos. Em 2000, por exemplo, a população da União Européia teve um aumento de 343 mil pessoas, enquanto a Índia alcançou esse mesmo crescimento na primeira semana de 2001. (...)",
     "Os Estados Unidos serão uma exceção no grupo dos países desenvolvidos. O país se tornará o único desenvolvido entre os 20 mais populosos do mundo.”")
  + fonte("<em>O Estado de S. Paulo</em>, 03 de março de 2001.") + p("Considerando as causas determinantes de crescimento populacional, pode-se afirmar que,"),
  tags=["crescimento populacional", "imigração"])

X(47, "N", "Física", "Unidades de medida", "<p>Megawatt (MW) é unidade de potência, energia por tempo. “Megawatt por hora” não tem sentido físico: o certo seria falar em megawatts de potência ou em megawatts-hora de energia. Alternativa <strong>D</strong>.</p><p>Usar megawatt para potência (B) está correto, e não há problema nos valores numéricos (A, E).</p>",
  ap("“...O Brasil tem potencial para produzir pelo menos 15 mil megawatts por hora de energia a partir de fontes alternativas.",
     "Somente nos Estados da região Sul, o potencial de geração de energia por intermédio das sobras agrícolas e florestais é de 5.000 megawatts por hora.",
     "Para se ter uma idéia do que isso representa, a usina hidrelétrica de Ita, uma das maiores do país, na divisa entre o Rio Grande do Sul e Santa Catarina, gera 1.450 megawatts de energia por hora.”")
  + p("Esse texto, transcrito de um jornal de grande circulação, contém, pelo menos, <u>um erro conceitual</u> ao apresentar valores de produção e de potencial de geração de energia. Esse erro consiste em"),
  tags=["potência", "unidades"])

X(48, "N", "Biologia", "Ecologia", "<p>As variações anuais de peso são 0,6; 0,9; 1,3; 1,2; 1,0; 0,9; 0,8... A maior (1,3 kg) ocorre entre 3 e 4 anos, quando o peixe chega a 3,9 kg. Depois disso ele já procriou, e a pesca pode ser autorizada a partir de cerca de 4 kg. Alternativa <strong>A</strong>.</p>",
  p("A pesca não predatória pressupõe que cada peixe retirado de seu hábitat já tenha procriado, pelo menos uma vez. Para algumas espécies, isso ocorre depois dos peixes apresentarem a máxima variação anual de seu peso.", "O controle de pesca no Pantanal é feito com base no peso de cada espécie.", "A tabela fornece o peso do <em>pacu</em>, uma dessas espécies, em cada ano.")
  + tabela(["Idade (anos)", "Peso (kg)"], [["1", "1,1"], ["2", "1,7"], ["3", "2,6"], ["4", "3,9"], ["5", "5,1"], ["6", "6,1"], ["7", "7"], ["8", "7,8"], ["9", "8,5"], ["10", "8,9"], ["11", "9,1"], ["12", "9,3"], ["13", "9,4"]])
  + p("Considerando esses dados, a pesca do pacu deve ser autorizada para espécimes com peso de, no mínimo,"),
  tags=["pesca sustentável", "taxa de variação"], alts=dict(D[48], E="11 kg."))

GELAD = tit("Texto para as questões 49 e 50.") + p("A refrigeração e o congelamento de alimentos são responsáveis por uma parte significativa do consumo de energia elétrica numa residência típica.")
X(49, "N", "Física", "Transmissão de calor", "<p>I está correta: deixar espaço entre os alimentos permite a convecção do ar dentro da geladeira. III também: o radiador sujo troca menos calor com o ambiente. II é falsa: o gelo é isolante térmico e dificulta a troca de calor no congelador. Alternativa <strong>D</strong>.</p>",
  GELAD + p("Para diminuir as perdas térmicas de uma geladeira, podem ser tomados alguns cuidados operacionais:")
  + I3("Distribuir os alimentos nas prateleiras deixando espaços vazios entre eles, para que ocorra a circulação do ar frio para baixo e do quente para cima.",
       "Manter as paredes do congelador com camada bem espessa de gelo, para que o aumento da massa de gelo aumente a troca de calor no congelador.",
       "Limpar o radiador (“grade” na parte de trás) periodicamente, para que a gordura e a poeira que nele se depositam não reduzam a transferência de calor para o ambiente.")
  + p("Para uma geladeira tradicional é correto indicar, apenas,"),
  tags=["geladeira", "convecção"])
X(50, "N", "Física", "Transmissão de calor", "<p>Com paredes de 4 cm a perda é de 35 kWh por mês; com 10 cm, 15 kWh. A diferença, 20 kWh, é 20/200 = 10% do consumo da família. Alternativa <strong>C</strong>.</p><p>35/200 ≈ 17,5% (perto de B) seria a perda total da geladeira de 4 cm, e não a perda a mais em relação à de 10 cm.</p>",
  GELAD + p("A padronização insuficiente e a ausência de controle na fabricação podem também resultar em perdas significativas de energia através das paredes da geladeira. Essas perdas, em função da espessura das paredes, para geladeiras e condições de uso típicas, são apresentadas na tabela.")
  + tabela(["Espessura das paredes (cm)", "Perda térmica mensal (kWh)"], [["2", "65"], ["4", "35"], ["6", "25"], ["10", "15"]])
  + p("Considerando uma família típica, com consumo médio mensal de 200 kWh, a perda térmica pelas paredes de uma geladeira com 4 cm de espessura, relativamente a outra de 10 cm, corresponde a uma porcentagem do consumo total de eletricidade da ordem de"),
  tags=["isolamento térmico", "porcentagem"], alts=A5("30%.", "20%.", "10%.", "5%.", "1%."))

X(51, "N", "Física", "Eletromagnetismo", "<p>Dentro do televisor há tensões de milhares de volts, que oferecem risco de choque (I). E aparelhos com motores ou ímãs criam campos magnéticos que desviam o feixe de elétrons e deformam a imagem (II). Alternativa <strong>A</strong>.</p>",
  p("A figura mostra o tubo de imagens dos aparelhos de televisão usado para produzir as imagens sobre a tela. Os elétrons do feixe emitido pelo canhão eletrônico são acelerados por uma tensão de milhares de volts e passam por um espaço entre bobinas onde são defletidos por campos magnéticos variáveis, de forma a fazerem a varredura da tela.") + "[[fig:1]]"
  + p("Nos manuais que acompanham os televisores é comum encontrar, entre outras, as seguintes recomendações:")
  + I3("Nunca abra o gabinete ou toque as peças no interior do televisor.", "Não coloque seu televisor próximo de aparelhos domésticos com motores elétricos ou ímãs.")
  + p("Estas recomendações estão associadas, respectivamente, aos aspectos de"),
  figs(("q51", "Esquema do tubo de imagem: o canhão eletrônico emite um feixe de elétrons que passa entre bobinas para a deflexão vertical e horizontal e atinge a tela.")),
  ["tubo de imagem", "campo magnético"])

X(52, "H", "Geografia", "Mercado de trabalho", "<p>A maior taxa de desemprego da tabela é a de mulheres com 8 a 10 anos de estudo (27,8%, ensino médio incompleto), e o Sudeste tem a maior taxa feminina por região (25,7%). Mulheres com ensino médio incompleto em Belo Horizonte teriam menor chance. Alternativa <strong>E</strong>.</p><p>Homens com pós-graduação (C) e com poucos anos de estudo (D) têm taxas baixas.</p>",
  p("A tabela apresenta a taxa de desemprego dos jovens entre 15 e 24 anos estratificada com base em diferentes categorias.")
  + tabela(["Categoria", "Homens (%)", "Mulheres (%)"],
           [["<strong>Região</strong>", "", ""], ["Norte", "15,3", "23,8"], ["Nordeste", "10,7", "18,8"], ["Centro-Oeste", "13,3", "20,6"], ["Sul", "11,6", "19,4"], ["Sudeste", "16,9", "25,7"],
            ["<strong>Grau de instrução</strong>", "", ""], ["Menos de 1 ano", "7,4", "16,1"], ["De 1 a 3 anos", "8,9", "16,4"], ["De 4 a 7 anos", "15,1", "22,8"], ["De 8 a 10 anos", "17,8", "27,8"], ["De 11 a 14 anos", "12,6", "19,6"], ["Mais de 15 anos", "11,0", "7,3"]])
  + fonte("Fonte: PNAD/IBGE, 1998.")
  + p("Considerando <strong>apenas</strong> os dados acima e analisando as características de candidatos a emprego, é possível concluir que teriam <strong>menor</strong> chance de consegui-lo,"),
  tags=["desemprego", "leitura de tabela"])

X(53, "M", "Matemática", "Porcentagem", "<p>Se a arrecadação total é A, os salários são 0,4A. Um reajuste de 5% nos salários custa 0,05 × 0,4A = 0,02A. Já 5% de aumento em todas as mensalidades rende 0,05A, mais que o dobro do necessário (bastaria cerca de 2%). A associação tem razão. Alternativa <strong>C</strong>.</p><p>O desconto dos alunos carentes já está embutido na arrecadação A (D, E).</p>",
  p("Em um colégio, 40% da arrecadação das mensalidades correspondem ao pagamento dos salários dos seus professores. A metade dos alunos desse colégio é de estudantes carentes, que pagam mensalidades reduzidas. O diretor propôs um aumento de 5% nas mensalidades de todos os alunos para cobrir os gastos gerados por reajuste de 5% na folha de pagamento dos professores. A associação de pais e mestres concorda com o aumento nas mensalidades mas não com o índice proposto. Pode-se afirmar que"),
  tags=["porcentagem de porcentagem"])

X(54, "H", "História", "Questão indígena", "<p>Terena pede que os índios sejam escutados em sua língua e em seus costumes, isto é, que a sociedade respeite sua cultura. Jaguaribe afirma que “o Brasil não terá índios no final do século XXI”, por um processo civilizatório inevitável de aculturação. Alternativa <strong>D</strong>.</p><p>Jaguaribe não propõe limpeza étnica (C) nem decisão autônoma das comunidades (E).</p>",
  p("Os textos referem-se à integração do índio à chamada civilização brasileira.")
  + ap("I - “Mais uma vez, nós, os povos indígenas, somos vítimas de um pensamento que separa e que tenta nos eliminar cultural, social e até fisicamente. A justificativa é a de que somos apenas 250 mil pessoas e o Brasil não pode suportar esse ônus. (...) É preciso congelar essas idéias colonizadoras, porque elas são irreais e hipócritas e também genocidas. (...) Nós, índios, queremos falar, mas queremos ser escutados na nossa língua, nos nossos costumes.”")
  + fonte("Marcos Terena, presidente do Comitê Intertribal Articulador dos Direitos Indígenas na ONU e fundador das Nações Indígenas, <em>Folha de S. Paulo</em>, 31 de agosto de 1994.")
  + ap("II - “O Brasil não terá índios no final do século XXI (...) E por que isso? Pela razão muito simples que consiste no fato de o índio brasileiro não ser distinto das demais comunidades primitivas que existiram no mundo. A história não é outra coisa senão um processo civilizatório, que conduz o homem, por conta própria ou por difusão da cultura, a passar do paleolítico ao neolítico e do neolítico a um estágio civilizatório.”")
  + fonte("Hélio Jaguaribe, cientista político, <em>Folha de S. Paulo</em>, 2 de setembro de 1994.")
  + p("Pode-se afirmar, segundo os textos, que"),
  tags=["questão indígena", "aculturação"])

X(55, "H", "Geografia", "Urbanização", "<p>Em 1900, as maiores cidades eram de países hoje desenvolvidos (Londres, Nova York, Paris); em 2015, a lista é dominada por cidades de países subdesenvolvidos (Bombaim, Lagos, São Paulo, Karachi, Dacar). O crescimento das grandes cidades no século XXI ocorrerá principalmente nesses países. Alternativa <strong>E</strong>.</p><p>Tóquio já tinha 1,5 milhão em 1900 (C), e Wuhan, na China, e São Petersburgo, na Rússia, estavam na lista de 1900 (D).</p>",
  p("O quadro apresenta as 10 cidades mais populosas do mundo em 1900 e os resultados de projeções das populações para 2001 e 2015.")
  + "".join(p(f"<strong>{ano}</strong>") + tabela(["Cidade", "População*"], [l.split("|") for l in linhas.split(";")]) for ano, linhas in [
      ("1900", "Londres|6,6;Nova York|3,4;Paris|2,7;Berlim|1,9;Chicago|1,7;Viena|1,7;Tóquio|1,5;Wuhan, China|1,5;Filadélfia|1,3;São Petersburgo|1,3"),
      ("2001", "Tóquio|29;Cidade do México|18;São Paulo|17;Bombaim|17;Nova York|16;Xangai|14;Los Angeles|13;Lagos, Nigéria|13;Calcutá|13;Buenos Aires|12"),
      ("2015", "Tóquio|29;Bombaim|26;Lagos, Nigéria|25;São Paulo|20;Karachi, Paquistão|19;Dacar, Bangladesh|19;Cidade do México|19;Xangai|18;Nova York|18;Calcutá|17")])
  + fonte("* em milhões de habitantes. <em>Revista Veja</em>, 24 de janeiro de 2001.")
  + p("As variações populacionais apresentadas no quadro permitem observar que"),
  tags=["metrópoles", "urbanização"])

X(56, "H", "Geografia", "Migração", "<p>Nos anos 1990, os migrantes deixaram de se dirigir só a São Paulo e ao Rio e passaram a buscar cidades médias e grandes de outras regiões, onde as favelas cresceram. Alternativa <strong>E</strong>.</p><p>Não houve declínio acentuado da indústria do Sudeste (A) nem instalação de muitas empresas de alta tecnologia no Nordeste (D).</p>",
  p("Dados do Censo Brasileiro 2000 mostram que, na última década, o número de favelas tem crescido consideravelmente, com significativa alteração na sua distribuição pelas regiões do País.", "Considerando a dinâmica migratória do período, pode-se afirmar que esse processo está relacionado"),
  tags=["favelas", "cidades médias"], alts=dict(D[56], E="à mudança no destino das correntes migratórias, que passaram a buscar as cidades de médio e grande portes, além de São Paulo e Rio de Janeiro."))

X(57, "N", "Física", "Astronomia", "<p>Shakespeare descreve o “glorioso astro Sol” “entronizado e centralizado no meio dos outros”, comandando os planetas. O Sol no centro é a ideia do modelo heliocêntrico de Copérnico. Alternativa <strong>C</strong>.</p><p>No modelo de Ptolomeu (A), o centro era a Terra.</p>",
  p("O texto foi extraído da peça <em>Tróilo e Créssida</em> de William Shakespeare, escrita, provavelmente, em 1601.")
  + ap("“Os próprios céus, os planetas, e este centro<br>reconhecem graus, prioridade, classe,<br>constância, marcha, distância, estação, forma,<br>função e regularidade, sempre iguais;<br>eis porque o glorioso astro Sol<br>está em nobre eminência entronizado<br>e centralizado no meio dos outros,<br>e o seu olhar benfazejo corrige<br>os maus aspectos dos planetas malfazejos,<br>e, qual rei que comanda, ordena<br>sem entraves aos bons e aos maus.”")
  + fonte("(personagem Ulysses, Ato I, cena III). SHAKESPEARE, W. <em>Tróilo e Créssida</em>. Porto: Lello &amp; Irmão, 1948.")
  + p("A descrição feita pelo dramaturgo renascentista inglês se aproxima da teoria"),
  tags=["heliocentrismo", "Shakespeare"])

X(58, "M", "Matemática", "Funções", "<p>Área plantada = produção ÷ produtividade. 1995: 30.000 t ÷ 1,5 t/ha = 20 mil ha; 1996: 40.000 ÷ 2,5 = 16 mil; 1997: 50.000 ÷ 2,5 = 20 mil; 1998: 60.000 ÷ 2,5 = 24 mil; 1999: 80.000 ÷ 4 = 20 mil. A área cai, sobe duas vezes e volta a cair, como no gráfico A. Alternativa <strong>A</strong>.</p>",
  p("O quadro apresenta a produção de algodão de uma cooperativa de agricultores entre 1995 e 1999.")
  + tabela(["Safra", "Produção (mil t)", "Produtividade (kg/ha)"], [["1995", "30", "1.500"], ["1996", "40", "2.500"], ["1997", "50", "2.500"], ["1998", "60", "2.500"], ["1999", "80", "4.000"]])
  + p("O gráfico que melhor representa a área plantada (AP) no período considerado é:"),
  figs(("q58a", "Gráfico de AP de 95 a 99: desce de 95 a 96, sobe até 98 e desce em 99."), ("q58b", "Gráfico de AP: sobe de 95 a 96, fica constante até 98 e sobe em 99."),
       ("q58c", "Gráfico de AP: sobe devagar de 95 a 98 e mais rápido em 99."), ("q58d", "Gráfico de AP: reta crescente de 95 a 99."), ("q58e", "Gráfico de AP: sobe de 95 a 96, fica constante até 98 e desce em 99.")),
  ["razão", "gráficos"], alts=ALT(1))

X(59, "H", "Geografia", "População economicamente ativa", "<p>Pelo gráfico, de 1960 a 1980 os serviços passaram de cerca de 33% para 44% e a indústria/mineração, de cerca de 17% para 28%: os dois cresceram cerca de 11 pontos percentuais. Alternativa <strong>E</strong>.</p><p>Em 1980 a agricultura ainda tinha cerca de 30% (D), e a queda mais acentuada da agricultura foi de 1960 a 1980 (B).</p>",
  p("O gráfico mostra a porcentagem da força de trabalho brasileira em 40 anos, com relação aos setores agrícola, de serviços e industrial/mineral.") + "[[fig:1]]" + p("A leitura do gráfico permite constatar que:"),
  figs(("q59", "Gráfico de linhas da força de trabalho (%) de 1940 a 1980. Agricultura: cerca de 67% em 1940, 52% em 1960 e 30% em 1980. Serviços: cerca de 17%, 33% e 44%. Indústria/mineração: cerca de 12%, 17% e 28%.")),
  ["setores da economia"], alts=dict(D[59], E="De 1960 a 1980, foi equivalente o crescimento percentual de trabalhadores nos setores industrial/mineral e de serviços."))

X(60, "H", "Geografia", "Mata Atlântica", "<p>Desde a colônia, a Mata Atlântica foi derrubada pela extração do pau-brasil e de madeira e pela expansão de lavouras (cana, café) e pastagens. As figuras mostram a mata desaparecendo ao longo de todo o litoral. Alternativa <strong>C</strong>.</p><p>A devastação acompanhou a ocupação humana, e não mudanças climáticas (A) ou só a indústria dos anos 1950 (E).</p>",
  p("A Mata Atlântica, que originalmente se estendia por todo o litoral brasileiro, do Ceará ao Rio Grande do Sul, ostenta hoje o triste título de uma das florestas mais devastadas do mundo. Com mais de 1 milhão de quilômetros quadrados, hoje restam apenas 5% da vegetação original, como mostram as figuras.") + "[[fig:1]]"
  + fonte("Adaptado <em>Atlas Nacional do Brasil</em>, IBGE, 1992; &lt;http://www.sosmatatlantica.org.br&gt;.")
  + p("Considerando as características histórico-geográficas do Brasil e a partir da análise das figuras é correto afirmar que"),
  figs(("q60", "Sequência de seis mapas do Brasil mostrando a Mata Atlântica, em preto, ao longo do litoral: cobertura original contínua do Nordeste ao Sul e, nos mapas de 1950-1960, 1960-1970, 1970-1980, 1980-1990 e 1990-2000, uma faixa cada vez mais fina e fragmentada.")),
  ["Mata Atlântica", "devastação"])

X(61, "H", "Geografia", "Espaço agrário", "<p>No gráfico, a área cultivada fica quase constante (perto do índice 100) entre 1980 e 1998, enquanto a produção sobe para cerca de 140. Produzir mais na mesma área significa aumento de produtividade, com novas tecnologias. Alternativa <strong>D</strong>.</p><p>A área não aumentou (A, B), e a população rural caiu, o que contraria C.</p>",
  p("A população rural do Brasil tem decrescido nas últimas décadas. De acordo com dados do IBGE, na década de 80, a população rural era de aproximadamente 37 milhões; no ano 2000 havia cerca de 31 milhões de brasileiros morando no campo. O gráfico apresenta o comportamento da agricultura no Brasil nas duas últimas décadas em relação à produção e à área cultivada.")
  + "[[fig:1]]" + fonte("Adaptado de Boletim Técnico <em>O agrônomo</em>, Instituto Agronômico de Campinas, Volume 51, nº 213, 1999.")
  + p("Levando em consideração as mudanças ocorridas no campo nas últimas duas décadas e analisando o comportamento do gráfico, é correto afirmar que"),
  figs(("q61", "Gráfico do crescimento (%) em relação ao ano de 1980, de 1980 a 1998: a produção oscila e sobe de 100 para cerca de 140; a área cultivada fica perto de 100 o tempo todo, entre cerca de 90 e 112.")),
  ["produtividade agrícola"])

X(62, "H", "História", "Brasil holandês", "<p>A peça põe em dúvida a reputação de traidor de Calabar; o texto I, de Varnhagen, o condena como “infiel, desertor e traidor”; e o texto II, de Calmon, mostra ações positivas (sertanista, ferido na defesa do Arraial) e negativas (crimes, deserção). Alternativa <strong>E</strong>.</p><p>O texto I não é tolerante (B), e a peça não é indiferente (C).</p>",
  p("Rui Guerra e Chico Buarque de Holanda escreveram uma peça para teatro chamada <em>Calabar</em>, pondo em dúvida a reputação de traidor que foi atribuída a Calabar, pernambucano que ajudou decisivamente os holandeses na invasão do Nordeste brasileiro, em 1632.",
    "– Calabar traiu o Brasil que ainda não existia? Traiu Portugal, nação que explorava a colônia onde Calabar havia nascido? Calabar, mulato em uma sociedade escravista e discriminatória, traiu a elite branca?", "Os textos referem-se também a esta personagem.")
  + ap("Texto I: “...dos males que causou à Pátria, a História, a inflexível História, lhe chamará infiel, desertor e traidor, por todos os séculos”")
  + fonte("Visconde de Porto Seguro, in: SOUZA JÚNIOR, A. <em>Do Recôncavo aos Guararapes</em>. Rio de Janeiro: Bibliex, 1949.")
  + ap("Texto II: “Sertanista experimentado, em 1627 procurava as minas de Belchior Dias com a gente da Casa da Torre; ajudara Matias de Albuquerque na defesa do Arraial, onde fora ferido, e desertara em conseqüência de vários crimes praticados...” (os crimes referidos são o de contrabando e roubo).")
  + fonte("CALMON, P. <em>História do Brasil</em>. Rio de Janeiro: José Olympio, 1959.") + p("Pode-se afirmar que:"),
  tags=["Calabar", "historiografia"])

X(63, "N", "Física", "Ano-luz", "<p>Um ano-luz é a distância que a luz percorre no vácuo em um ano (cerca de 9,5 trilhões de km). Apesar do nome, é uma unidade de distância. Alternativa <strong>C</strong>.</p><p>Ele relaciona velocidade e tempo, mas o resultado (velocidade × tempo) é distância, e não tempo (A) ou velocidade (D).</p>",
  "[[fig:1]]" + p("Gilberto Gil usa na letra da música a palavra composta <strong>anos-luz</strong>. O sentido prático, em geral, não é obrigatoriamente o mesmo que na ciência. Na Física, um ano luz é uma medida que relaciona a velocidade da luz e o tempo de um ano e que, portanto, se refere a"),
  figs(("q63", "Letra da canção “Seu olhar”, de Gilberto Gil (1984): o eu lírico quisera ter, na eternidade, tantos anos-luz quantos fossem precisos para cruzar o túnel do tempo do olhar da pessoa amada.")),
  ["ano-luz", "Gilberto Gil"])

completar(Q, R)
