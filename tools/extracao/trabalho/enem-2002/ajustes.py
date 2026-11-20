# Enem 2002 (data não confirmada; dataExame omitida), Prova 1 — amarela: prova única de 63 questões (modelo antigo, sem divisão por áreas).
# Fonte do PDF: arquivo 'Provas_Gabaritos_ENEM_2002' do usuário. Gabarito: 'GABARITO ENEM 2002 – Amarela' do repositório do Inep (riep.inep.gov.br/server/api/core/bitstreams/dbc42061-d37d-41e5-8843-e416992db92a/content), lido duas vezes.
# Data: não encontrei fonte acessível; o campo dataExame fica de fora (é opcional).
# Layout misto (uma e duas colunas): extrator com COLS=4,5,11,15,17 COLX=300 YMIN=40 YMAX=795.
# O extrator padrão não lê este layout; as alternativas vêm de alts.json (extrator próprio) e os enunciados são escritos aqui.
# Cada questão leva a grande área mais próxima. Protegidos como imagem: poema de Carlos de Oliveira (Q46) e marchinha de Assis Valente (Q53).
# Em texto: prosa (Guimarães Rosa, Érico Veríssimo, Nelson Rodrigues, Marina Colasanti) e Monteiro Lobato e João do Rio, de domínio público.
import sys, pathlib, re, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar

ID = "enem-2002"
META = {"id": ID, "banca": "Enem", "ano": 2002, "titulo": "Enem 2002: Prova objetiva", "fonte": "Inep",
        "duracaoMinutos": 300, "area": "Prova objetiva (63 questões)", "caderno": "amarelo", "dia": 1, "fonteGabarito": {"oficial": True, "nome": "gabarito oficial no repositório do Inep", "url": "https://riep.inep.gov.br/server/api/core/bitstreams/dbc42061-d37d-41e5-8843-e416992db92a/content"}}
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
X(1, "L", "Literatura", "Foco narrativo", "<p>Em “O homem trouxe o cavalo cá bem junto”, o advérbio “cá” indica o lugar onde está Miguilim: o narrador, embora em terceira pessoa, se posiciona no espaço do menino. Alternativa <strong>A</strong>.</p><p>As outras frases descrevem o homem ou a casa sem marcar esse ponto de referência espacial.</p>",
  tit("Miguilim")
  + ap("“De repente lá vinha um homem a cavalo. Eram dois. Um senhor de fora, o claro de roupa. Miguilim saudou, pedindo a bênção. O homem trouxe o cavalo cá bem junto. Ele era de óculos, corado, alto, com um chapéu diferente, mesmo.",
       "— Deus te abençoe, pequenino. Como é teu nome?<br>— Miguilim. Eu sou irmão do Dito.<br>— E o seu irmão Dito é o dono daqui?<br>— Não, meu senhor. O Ditinho está em glória.",
       "O homem esbarrava o avanço do cavalo, que era zelado, manteúdo, formoso como nenhum outro. Redizia:<br>— Ah, não sabia, não. Deus o tenha em sua guarda... Mas que é que há, Miguilim?",
       "Miguilim queria ver se o homem estava mesmo sorrindo para ele, por isso é que o encarava.<br>— Por que você aperta os olhos assim? Você não é limpo de vista? Vamos até lá. Quem é que está em tua casa?<br>— É Mãe, e os meninos...",
       "Estava Mãe, estava tio Terez, estavam todos. O senhor alto e claro se apeou. O outro, que vinha com ele, era um camarada. O senhor perguntava à Mãe muitas coisas do Miguilim. Depois perguntava a ele mesmo: — ‘Miguilim, espia daí: quantos dedos da minha mão você está enxergando? E agora?”")
  + fonte("ROSA, João Guimarães. <em>Manuelzão e Miguilim</em>. 9ª ed. Rio de Janeiro: Nova Fronteira, 1984.")
  + p("Esta história, com narrador observador em terceira pessoa, apresenta os acontecimentos da perspectiva de Miguilim. O fato de o ponto de vista do narrador ter Miguilim como referência, inclusive espacial, fica explicitado em:"),
  tags=["Guimarães Rosa", "narrador"])

X(2, "H", "Geografia", "Fusos horários", "<p>As bolsas abrem às 9h locais, e o dia começa antes no leste. Pequim, bem a leste, abre primeiro; depois Londres; por último Nova Iorque, a oeste. A sequência certa é Pequim, Londres e Nova Iorque. Alternativa <strong>C</strong>.</p><p>Os horários indicados para cada bolsa são os mesmos em todas as alternativas; o que as distingue é a ordem em que as informações chegam ao investidor.</p>",
  p("O mercado financeiro mundial funciona 24 horas por dia. As bolsas de valores estão articuladas, mesmo abrindo e fechando em diferentes horários, como ocorre com as bolsas de Nova Iorque, Londres, Pequim e São Paulo. Todas as pessoas que, por exemplo, estão envolvidas com exportações e importações de mercadorias precisam conhecer os fusos horários para fazer o melhor uso dessas informações.")
  + "[[fig:1]]" + p("Considerando que as bolsas de valores começam a funcionar às 09:00 horas da manhã e que um investidor mora em Porto Alegre, pode-se afirmar que os horários em que ele deve consultar as bolsas e a seqüência em que as informações são obtidas estão corretos na alternativa:"),
  figs(("q02a", "Planisfério dividido por linhas verticais em 24 fusos, com a linha internacional de data no meio do Pacífico, centrado na Ásia e no Pacífico. Estão marcadas Pequim e Tóquio, à esquerda; Nova Iorque e Londres (na borda direita), e Porto Alegre, no sul do Brasil.")),
  ["fusos horários", "bolsas de valores"])

X(3, "M", "Matemática", "Leitura de gráficos", "<p>Pela tabela, o peso ideal para 1,59 m é 58,0 kg; o atleta tem 63 kg, ou seja, 5 kg acima do ideal. Pelo gráfico, na meia-maratona perde-se 0,67 minuto por quilo a mais: 5 × 0,67 = 3,35 minutos. Alternativa <strong>E</strong>.</p><p>0,67 (B) é a perda para apenas 1 kg acima do ideal.</p>",
  p("O excesso de peso pode prejudicar o desempenho de um atleta profissional em corridas de longa distância como a maratona (42,2 km), a meia-maratona (21,1 km) ou uma prova de 10 km. Para saber uma aproximação do intervalo de tempo a mais perdido para completar uma corrida devido ao excesso de peso, muitos atletas utilizam os dados apresentados na tabela e no gráfico:")
  + tabela(["Altura (m)", "Peso (kg) ideal para atleta masculino de ossatura grande, corredor de longa distância"], [["1,57", "56,9"], ["1,58", "57,4"], ["1,59", "58,0"], ["1,60", "58,5"], ["⋮", "⋮"]])
  + "[[fig:1]]"
  + p("Usando essas informações, um atleta de ossatura grande, pesando 63 kg e com altura igual a 1,59m, que tenha corrido uma meia-maratona, pode estimar que, em condições de peso ideal, teria melhorado seu tempo na prova em"),
  figs(("q03", "Gráfico “Tempo x Peso (Modelo Wilmore e Benke)”: tempo perdido (minutos) em função do peso acima do ideal (kg), com três retas pela origem. Para 1 kg acima do ideal: maratona, 1,33 minuto; meia-maratona, 0,67 minuto; prova de 10 km, 0,32 minuto.")),
  ["proporcionalidade", "leitura de tabela"], alts=A5("0,32 minuto.", "0,67 minuto.", "1,60 minuto.", "2,68 minutos.", "3,35 minutos."))

X(4, "N", "Química", "pH", "<p>Como [H<sup>+</sup>] = 10<sup>−pH</sup>, cada unidade a menos de pH multiplica a acidez por 10. I é falsa: da 6ª (pH 4) para a 14ª (pH 6) a acidez caiu 100 vezes. II é verdadeira (pH 7 é o maior). III é verdadeira: pH 5 contra pH 6, dez vezes mais ácida. IV é verdadeira: só a 6ª (pH 4) e a 8ª (pH 5) têm pH abaixo de 5,5. Alternativa <strong>E</strong>.</p>",
  p("A chuva em locais não poluídos é levemente ácida. Em locais onde os níveis de poluição são altos, os valores do pH da chuva podem ficar abaixo de 5,5, recebendo, então, a denominação de “chuva ácida”. Este tipo de chuva causa prejuízos nas mais diversas áreas: construção civil, agricultura, monumentos históricos, entre outras.",
    "A acidez da chuva está relacionada ao pH da seguinte forma: concentração de íons hidrogênio = 10<sup>-pH</sup>, sendo que o pH pode assumir valores entre 0 e 14.",
    "Ao realizar o monitoramento do pH da chuva em Campinas (SP) nos meses de março, abril e maio de 1998, um centro de pesquisa coletou 21 amostras, das quais quatro têm seus valores mostrados na tabela:")
  + tabela(["Mês", "Amostra", "pH"], [["Março", "6ª", "4"], ["Abril", "8ª", "5"], ["Abril", "14ª", "6"], ["Maio", "18ª", "7"]])
  + p("A análise da fórmula e da tabela permite afirmar que:")
  + '<ol type="I"><li>da 6ª para a 14ª amostra ocorreu um aumento de 50% na acidez.</li><li>a 18ª amostra é a menos ácida dentre as expostas.</li><li>a 8ª amostra é dez vezes mais ácida que a 14ª.</li><li>as únicas amostras de chuvas denominadas ácidas são a 6ª e a 8ª.</li></ol>'
  + p("São corretas apenas as afirmativas"),
  tags=["chuva ácida", "potências de 10"], alts=A5("I e II.", "II e IV.", "I, II e IV.", "I, III e IV.", "II, III e IV."))

X(5, "H", "Geografia", "Questão ambiental", "<p>A tabela mostra que a China, a Índia e o Brasil emitem muito menos CO2 por habitante (Índia e Brasil, entre 0,8 e 2,5 t por ano) e acumularam bem menos que os EUA desde 1950. Isso contradiz a ideia de que o acordo deveria ser mais duro com os países em desenvolvimento. Alternativa <strong>D</strong>.</p><p>B é falsa pela própria tabela, e A e C não respondem ao argumento sobre os países em desenvolvimento.</p>",
  ap("O Protocolo de Kyoto — uma convenção das Nações Unidas que é marco sobre mudanças climáticas, — estabelece que os países mais industrializados devem reduzir até 2012 a emissão dos gases causadores do efeito estufa em pelo menos 5% em relação aos níveis de 1990. Essa meta estabelece valores superiores ao exigido para países em desenvolvimento. Até 2001, mais de 120 países, incluindo nações industrializadas da Europa e da Ásia, já haviam ratificado o protocolo. No entanto, nos EUA, o presidente George W. Bush anunciou que o país não ratificaria “Kyoto”, com os argumentos de que os custos prejudicariam a economia americana e que o acordo era pouco rigoroso com os países em desenvolvimento.")
  + fonte("Adaptado do <em>Jornal do Brasil</em>, 11/04/2001.") + p("Na tabela encontram-se dados sobre a emissão de CO2.")
  + tabela(["País", "Emissões de CO2 desde 1950 (bilhões de toneladas)", "Emissões anuais de CO2 per capita (t)"],
           [["Estados Unidos", "186,1", "16 a 36"], ["União Européia", "127,8", "7 a 16"], ["Rússia", "68,4", "7 a 16"], ["China", "57,6", "2,5 a 7"], ["Japão", "31,2", "7 a 16"],
            ["Índia", "15,5", "0,8 a 2,5"], ["Polônia", "14,4", "7 a 16"], ["África do Sul", "8,5", "7 a 16"], ["México", "7,8", "2,5 a 7"], ["Brasil", "6,6", "0,8 a 2,5"]])
  + fonte("<em>World Resources</em> 2000/2001.")
  + p("Considerando os dados da tabela, assinale a alternativa que representa um argumento que se contrapõe à justificativa dos EUA de que o acordo de Kyoto foi pouco rigoroso com países em desenvolvimento."),
  tags=["Protocolo de Kyoto", "emissões de CO2"], quim=True)

X(6, "N", "Química", "Poluição do ar", "<p>No gráfico, a emissão média por veículo a álcool ficou abaixo da dos veículos a gasolina de 1992 até cerca de 1997, e a frota a álcool (bem menor) sempre emitiu menos no total (I). Por volta de 1997 as curvas se cruzam e o carro a gasolina passa a poluir menos (II). III é falsa: a emissão do carro a álcool ficou estável ou subiu um pouco, sem sinal de aprimoramento. Alternativa <strong>B</strong>.</p>",
  p("A tabela mostra a evolução da frota de veículos leves, e o gráfico, a emissão média do poluente monóxido de carbono (em g/km) por veículo da frota, na região metropolitana de São Paulo, no período de 1992 a 2000.")
  + tabela(["Ano", "Frota a Álcool (em milhares)", "Frota a Gasolina (em milhares)"],
           [["1992", "1250", "2500"], ["1993", "1300", "2750"], ["1994", "1350", "3000"], ["1995", "1400", "3350"], ["1996", "1350", "3700"], ["1997", "1250", "3950"], ["1998", "1200", "4100"], ["1999", "1100", "4400"], ["2000", "1050", "4800"]])
  + "[[fig:1]]"
  + p("Comparando-se a emissão média de monóxido de carbono dos veículos a gasolina e a álcool, pode-se afirmar que")
  + I3("no transcorrer do período 1992-2000, a frota a álcool emitiu menos monóxido de carbono.", "em meados de 1997, o veículo a gasolina passou a poluir menos que o veículo a álcool.", "o veículo a álcool passou por um aprimoramento tecnológico.")
  + p("É correto o que se afirma apenas em"),
  figs(("q06a", "Gráfico da emissão média de CO (g/km) por veículo, de 1992 a 2000. Gasolina: cai de cerca de 31 em 1992 para 13 em 2000. Álcool: oscila entre 15 e 19, com cerca de 18 em 1992, 16 entre 1993 e 1996 e 18 a 19 de 1998 a 2000. As curvas se cruzam por volta de 1997. Fonte: adaptado de Cetesb, relatório do ano de 2000.")),
  ["monóxido de carbono", "álcool combustível"], alts=A5("I.", "I e II.", "II.", "III.", "II e III."))

X(7, "L", "Literatura", "Função da literatura", "<p>Para Érico Veríssimo, o escritor deve “acender a sua lâmpada, fazer luz sobre a realidade de seu mundo”, numa época de atrocidades e injustiças. Iluminar a realidade é denunciá-la. Alternativa <strong>C</strong>.</p><p>O texto não fala em fantasia, sonho ou beleza, e a náusea é algo a superar, não a evitar (E).</p>",
  p("Érico Veríssimo relata, em suas memórias, um episódio da adolescência que teve influência significativa em sua carreira de escritor.")
  + ap("“Lembro-me de que certa noite – eu teria uns quatorze anos, quando muito – encarregaram-me de segurar uma lâmpada elétrica à cabeceira da mesa de operações, enquanto um médico fazia os primeiros curativos num pobre-diabo que soldados da Polícia Municipal haviam “carneado”. (...) Apesar do horror e da náusea, continuei firme onde estava, talvez pensando assim: se esse caboclo pode agüentar tudo isso sem gemer, por que não hei de poder ficar segurando esta lâmpada para ajudar o doutor a costurar esses talhos e salvar essa vida? (...)",
       "Desde que, adulto, comecei a escrever romances, tem-me animado até hoje a idéia de que o menos que o escritor pode fazer, numa época de atrocidades e injustiças como a nossa, é acender a sua lâmpada, fazer luz sobre a realidade de seu mundo, evitando que sobre ele caia a escuridão, propícia aos ladrões, aos assassinos e aos tiranos. Sim, segurar a lâmpada, a despeito da náusea e do horror. Se não tivermos uma lâmpada elétrica, acendamos o nosso toco de vela ou, em último caso, risquemos fósforos repetidamente, como um sinal de que não desertamos nosso posto.”")
  + fonte("VERÍSSIMO, Érico. <em>Solo de Clarineta</em>. Tomo I. Porto Alegre: Editora Globo, 1978.")
  + p("Neste texto, por meio da metáfora da lâmpada que ilumina a escuridão, Érico Veríssimo define como uma das funções do escritor e, por extensão, da literatura,"),
  tags=["Érico Veríssimo", "metáfora"], alts=A5("criar a fantasia.", "permitir o sonho.", "denunciar o real.", "criar o belo.", "fugir da náusea."))

X(8, "N", "Biologia", "Ecologia", "<p>I, II e IV estão corretas: a população de artemias, sensível ao ambiente, pode indicar poluição; por se alimentar de partículas em suspensão, ela pode ajudar a descontaminar a água; e seu alto teor de proteína a torna uma fonte de alimento. Alternativa <strong>C</strong>.</p><p>III é falsa: o texto diz que a eclosão dos ovos é ativada por fatores climáticos e ambientais em geral, sem relação específica com poluição química.</p>",
  ap("Artemia é um camarão primitivo que vive em águas salgadas, sendo considerado um fóssil vivo. Surpreendentemente, possui uma propriedade semelhante à dos vegetais que é a diapausa, isto é, a capacidade de manter ovos dormentes (embriões latentes) por muito tempo. Fatores climáticos ou alterações ambientais podem subitamente ativar a eclosão dos ovos, assim como, nos vegetais, tais alterações induzem a germinação de sementes.",
     "Vários estudos têm sido realizados com artemias, pois estes animais apresentam características que sugerem um potencial biológico: possuem alto teor de proteína e são capazes de se alimentar de partículas orgânicas e inorgânicas em suspensão. Tais características podem servir de parâmetro para uma avaliação do potencial econômico e ecológico da artemia.")
  + p("Em um estudo foram consideradas as seguintes possibilidades:")
  + '<ol type="I"><li>A variação da população de artemia pode ser usada como um indicador de poluição aquática.</li><li>A artemia pode ser utilizada como um agente de descontaminação ambiental, particularmente em ambientes aquáticos.</li><li>A eclosão dos ovos é um indicador de poluição química.</li><li>Os camarões podem ser utilizados como fonte alternativa de alimentos de alto teor nutritivo.</li></ol>'
  + p("É correto apenas o que se afirma em"),
  tags=["artemia", "bioindicadores"])

X(9, "L", "Literatura", "Recursos expressivos", "<p>Os gerúndios inventados (“camaronando”, “caranguejando”, “pequeninando”) transformam cada bicho numa ação em andamento: tudo se mexe ao mesmo tempo. O efeito é de dinamismo, de cenário cheio de movimento. Alternativa <strong>E</strong>.</p><p>O gerúndio indica ação contínua, o contrário de estaticidade (C) ou interrupção (D).</p>",
  ap("“Narizinho correu os olhos pela assistência. Não podia haver nada mais curioso. Besourinhos de fraque e flores na lapela conversavam com baratinhas de mantilha e miosótis nos cabelos. Abelhas douradas, verdes e azuis, falavam mal das vespas de cintura fina – achando que era exagero usarem coletes tão apertados. Sardinhas aos centos criticavam os cuidados excessivos que as borboletas de toucados de gaze tinham com o pó das suas asas. Mamangavas de ferrões amarrados para não morderem. E canários cantando, e beija-flores beijando flores, e camarões camaronando, e caranguejos caranguejando, tudo que é pequenino e não morde, pequeninando e não mordendo.”")
  + fonte("LOBATO, Monteiro. <em>Reinações de Narizinho</em>. São Paulo: Brasiliense, 1947.")
  + p("No último período do trecho, há uma série de verbos no gerúndio que contribuem para caracterizar o ambiente fantástico descrito. Expressões como “camaronando”, “caranguejando” e “pequeninando e não mordendo” criam, principalmente, efeitos de"),
  tags=["Monteiro Lobato", "gerúndio"], alts=dict(D[9], E="dinamicidade do cenário."))

FAVA = (tit("Texto para as questões 10 e 11.")
  + ap("Nativas do Brasil, as várias espécies das plantas conhecidas como fava-d’anta têm lugar garantido no mercado mundial de produtos cosméticos e farmacêuticos. Elas praticamente não têm concorrentes, pois apenas uma outra planta chinesa produz os elementos cobiçados pela indústria mundial. As plantas acham-se dispersas no cerrado e a sua exploração é feita pela coleta manual das favas ou, ainda, com instrumentos rústicos (garfos e forquilhas) que retiram os frutos das pontas dos galhos. Alguns catadores quebram galhos ou arbustos para facilitar a coleta. Depois da coleta, as vagens são vendidas aos atacadistas locais que as revendem a atacadistas regionais, estes sim, os revendedores de fava para as indústrias. Depois de processados, os produtos são exportados. Embora os moradores da região tenham um vasto conhecimento sobre hábitos e usos da fauna e flora locais, pouco ou nada sabem sobre a produção de mudas de espécies nativas e, ainda, sobre o destino e o aproveitamento da matéria-prima extraída da fava d’anta.")
  + fonte("Adaptado de: Extrativismo e biodiversidade: o caso da fava-d’anta. <em>Ciência Hoje</em>, junho, 2000."))
X(10, "N", "Biologia", "Conservação", "<p>A ameaça vem da coleta predatória e da pressão do mercado sobre plantas dispersas e nativas. Produzir mudas em viveiros (domesticar a espécie) garante a reposição das plantas, se for preciso. Alternativa <strong>C</strong>.</p><p>A mecanização (A) aumentaria a pressão sobre as plantas, e proibir a coleta (D) tiraria renda das famílias sem resolver a renovação.</p>",
  FAVA + p("Ainda que a extração das vagens não seja prejudicial às árvores, a estratégia usada na sua coleta, aliada à eventual pressão de mercado, são fatores que podem prejudicar a renovação natural da fava d’anta. Uma proposta viável para que estas plantas nativas não corram nenhum risco de extinção é"),
  tags=["fava-d’anta", "extrativismo"])
X(11, "H", "Geografia", "Extrativismo", "<p>I e III estão corretas: os coletores não sabem o destino nem o aproveitamento da fava, ficando só com o trabalho braçal; e a fava passa por atacadistas locais e regionais (atravessadores) antes da indústria, enquanto o pequi é vendido direto na estrada. Alternativa <strong>C</strong>.</p><p>II e IV são falsas: a fava rende só R$ 60 por ano (6,81% da renda), muito menos que o pequi (56,81%) ou a lenha.</p>",
  FAVA + p("A coleta de favas é feita por famílias inteiras de trabalhadores rurais (não-proprietários). Enquanto o jovem apanhador de favas pode ganhar até R$7,50 por dia, os demais trabalhadores adultos ganham, em média, R$5,12 por dia, podendo dedicar-se a outras atividades extrativistas: a coleta de pequis e panãs, frutos vendidos à beira da estrada, e de lenha, vendida a pequenos compradores. A tabela apresenta a renda média anual dos jovens e adolescentes de uma cidade de Minas Gerais, com essas atividades extrativistas.")
  + tabela(["Produto", "Renda média (R$)", "Renda anual (R$)", "Participação (%) na renda total"],
           [["Pequi", "25 (saca)", "500", "56,81"], ["Panã", "2 (unidade)", "80", "9,09"], ["Fava-d’anta", "5 (saca)", "60", "6,81"], ["Lenha", "5 (carroça)", "240", "27,29"], ["<strong>Total</strong>", "", "<strong>880</strong>", "<strong>100</strong>"]])
  + fonte("<em>Ciência Hoje</em>, junho de 2000.")
  + p("Foram feitas as seguintes afirmações sobre a importância socioeconômica do extrativismo da fava-d’anta:")
  + '<ol type="I"><li>A desinformação impede qualquer controle da situação por parte dos coletores, aos quais cabe apenas o papel de trabalhadores braçais.</li><li>O retorno financeiro para a população é compatível com a importância dos produtos derivados da fava.</li><li>A atividade é menos rentável porque, entre os compradores de favas, existem atravessadores, ao contrário do que acontece na venda do pequi.</li><li>A atividade eleva o salário diário do trabalhador, representando a fonte mais importante de sua renda anual.</li></ol>'
  + p("Está correto apenas o que se afirma em"),
  tags=["extrativismo", "atravessadores"], alts=A5("I, III e IV.", "II, III e IV.", "I e III.", "II e IV.", "I e IV."))

X(12, "N", "Física", "Conforto térmico", "<p>Curitiba em março (27 °C, 72%) fica acima da faixa “ideal” e dentro da faixa “ideal com vento”. Campo Grande em outubro (25 °C, 58%) fica dentro da faixa “ideal”. Alternativa <strong>A</strong>.</p><p>Campo Grande em março tem 82% de umidade, fora de todas as faixas (B, D), e Curitiba em maio tem 80%, também fora (E).</p>",
  p("Os seres humanos podem tolerar apenas certos intervalos de temperatura e umidade relativa (UR), e, nessas condições, outras variáveis, como os efeitos do sol e do vento, são necessárias para produzir condições confortáveis, nas quais as pessoas podem viver e trabalhar. O gráfico mostra esses intervalos:")
  + "[[fig:1]]" + p("A tabela mostra temperaturas e umidades relativas do ar de duas cidades, registradas em três meses do ano.")
  + tabela(["Cidade", "Março", "Maio", "Outubro"], [["Campo Grande", "25 °C; UR 82%", "20 °C; UR 60%", "25 °C; UR 58%"], ["Curitiba", "27 °C; UR 72%", "19 °C; UR 80%", "18 °C; UR 75%"]])
  + p("Com base nessas informações, pode-se afirmar que condições ideais são observadas em"),
  figs(("q12a", "Gráfico de temperatura (°C) por umidade relativa (%), com uma região fechada entre cerca de 17% e 78% de umidade, dividida em três faixas: “ideal com vento”, de cerca de 27 °C a 33 °C; “ideal”, de cerca de 21 °C a 27 °C (descendo para 20 °C a 24 °C com umidade alta); e “ideal com sol”, de cerca de 8 °C a 21 °C. Fonte: adaptado de The Random House Encyclopedias, 1990.")),
  ["umidade relativa", "leitura de gráfico"])

X(13, "M", "Matemática", "Leitura de gráficos", "<p>Pelo gráfico, os placares (marcados × sofridos) foram: 2×0, 1×4, 3×3, 0×5, 2×1, 3×1, 2×2, 1×0, 0×0 e 3×0. São 5 vitórias (15 pontos), 3 empates (3 pontos) e 2 derrotas: 18 pontos. Alternativa <strong>C</strong>.</p>",
  p("No gráfico estão representados os gols marcados e os gols sofridos por uma equipe de futebol nas dez primeiras partidas de um determinado campeonato.") + "[[fig:1]]"
  + p("Considerando que, neste campeonato, as equipes ganham 3 pontos para cada vitória, 1 ponto por empate e 0 ponto em caso de derrota, a equipe em questão, ao final da décima partida, terá acumulado um número de pontos igual a"),
  figs(("q13a", "Gráfico de linhas com gols marcados e sofridos nas partidas de 28/01 a 01/04. Gols marcados: 2, 1, 3, 0, 2, 3, 2, 1, 0, 3. Gols sofridos: 0, 4, 3, 5, 1, 1, 2, 0, 0, 0.")),
  ["futebol", "leitura de gráfico"], alts=A5("15.", "17.", "18.", "20.", "24."))

X(14, "N", "Biologia", "Cadeias alimentares", "<p>Garfield acha “pouco glamuroso” a minhoca cavar para comer, mas, do ponto de vista biológico, ambos são consumidores e precisam obter o próprio alimento todo dia. Alternativa <strong>A</strong>.</p><p>Minhocas participam das cadeias como decompositoras (D); e um gato doméstico não é “superior” por ocupar outro nível (B, E).</p>",
  "[[fig:1]]" + fonte("<em>O Globo</em>, 01/09/2001.") + p("Na charge, a arrogância do gato com relação ao comportamento alimentar da minhoca, do ponto de vista biológico,"),
  figs(("q14a", "Tira de Garfield, de Jim Davis, em três quadros. Garfield pensa, olhando uma minhoca: “Você vive debaixo da terra e come porcarias?”; ela responde: “É isso aí.” Garfield: “E que faz pra conseguir comida?”; minhoca: “Cavo.” Garfield: “Isso não é muito glamuroso.”; minhoca: “Mas é assim que ganho a sujeira de cada dia...”")),
  ["Garfield", "consumidores"])

X(15, "M", "Matemática", "Polígonos", "<p>Para pavimentar sem falhas, os ângulos em cada vértice devem somar 360°. Com octógonos (135°): 135 + 135 = 270°, faltando 90°, o ângulo do quadrado. Alternativa <strong>B</strong>.</p><p>Nenhum outro polígono da tabela completa 90° ou combina com 135° para fechar 360°.</p>",
  p("Na construção civil, é muito comum a utilização de ladrilhos ou azulejos com a forma de polígonos para o revestimento de pisos ou paredes. Entretanto, não são todas as combinações de polígonos que se prestam a pavimentar uma superfície plana, sem que haja falhas ou superposições de ladrilhos, como ilustram as figuras:")
  + "[[fig:1]][[fig:2]]" + p("A tabela traz uma relação de alguns polígonos regulares, com as respectivas medidas de seus ângulos internos.")
  + tabela(["Polígono", "Ângulo interno"], [["Triângulo", "60°"], ["Quadrado", "90°"], ["Pentágono", "108°"], ["Hexágono", "120°"], ["Octógono", "135°"], ["Eneágono", "140°"]])
  + p("Se um arquiteto deseja utilizar uma combinação de dois tipos diferentes de ladrilhos entre os polígonos da tabela, sendo um deles octogonal, o outro tipo escolhido deverá ter a forma de um"),
  figs(("q15a", "Figura 1: ladrilhos retangulares pavimentando o plano, sem falhas."), ("q15b", "Figura 2: heptágonos regulares que não pavimentam o plano, deixando falhas ou superposições.")),
  ["ângulos internos", "pavimentação"])

X(16, "N", "Biologia", "Recursos hídricos", "<p>Reutilizar a água reduz a demanda sobre os mananciais e é viável em escala global. Alternativa <strong>A</strong>.</p><p>Explorar aquíferos, captar outros rios ou importar água (B, C, E) só transfere o problema, e a água da chuva (D) não é suficiente nem disponível em todo lugar.</p>",
  p("Segundo uma organização mundial de estudos ambientais, em 2025, “duas de cada três pessoas viverão situações de carência de água, caso não haja mudanças no padrão atual de consumo do produto.” Uma alternativa adequada e viável para prevenir a escassez, considerando-se a disponibilidade global, seria"),
  tags=["reúso de água"])

X(17, "N", "Biologia", "Enzimas", "<p>A conversão dos açúcares em amido é feita por enzimas, que são proteínas. A água fervente desnatura essas enzimas, e o resfriamento e a geladeira retardam qualquer atividade restante, preservando o sabor doce. Alternativa <strong>C</strong>.</p><p>Não há microrganismos envolvidos (D), e o calor não converte proteínas em amido (A).</p>",
  p("O milho verde recém-colhido tem um sabor adocicado. Já o milho verde comprado na feira, um ou dois dias depois de colhido, não é mais tão doce, pois cerca de 50% dos carboidratos responsáveis pelo sabor adocicado são convertidos em amido nas primeiras 24 horas.", "Para preservar o sabor do milho verde pode-se usar o seguinte procedimento em três etapas:")
  + "<ol><li>descascar e mergulhar as espigas em água fervente por alguns minutos;</li><li>resfriá-las em água corrente;</li><li>conservá-las na geladeira.</li></ol>"
  + p("A preservação do sabor original do milho verde pelo procedimento descrito pode ser explicada pelo seguinte argumento:"),
  tags=["desnaturação", "amido"])

X(18, "N", "Física", "Radiação ultravioleta", "<p>Com IUV maior que 8 (risco extremo), o tempo de exposição segura da pele desprotegida é no máximo 20 minutos (TPD). Para ficar das 12h às 14h, 120 minutos, o protetor precisa de FPS = TPP/TPD = 120/20 = 6. Alternativa <strong>B</strong>.</p><p>20 (E) confunde o FPS com o TES.</p>",
  p("Os níveis de irradiância ultravioleta efetiva (IUV) indicam o risco de exposição ao Sol para pessoas de pele do tipo II – pele de pigmentação clara. O tempo de exposição segura (TES) corresponde ao tempo de exposição aos raios solares sem que ocorram queimaduras de pele. A tabela mostra a correlação entre riscos de exposição, IUV e TES.")
  + tabela(["Riscos de exposição", "IUV", "TES (em minutos)"], [["Baixo", "0 a 2", "Máximo 60"], ["Médio", "3 a 5", "30 a 60"], ["Alto", "6 a 8", "20 a 30"], ["Extremo", "Acima de 8", "Máximo 20"]])
  + p("Uma das maneiras de se proteger contra queimaduras provocadas pela radiação ultravioleta é o uso dos cremes protetores solares, cujo Fator de Proteção Solar (FPS) é calculado da seguinte maneira:")
  + p(r"\(\text{FPS} = \dfrac{\text{TPP}}{\text{TPD}}\)")
  + p("TPP = tempo de exposição mínima para produção de vermelhidão na pele protegida (em minutos).<br>TPD = tempo de exposição mínima para produção de vermelhidão na pele desprotegida (em minutos).",
      "O FPS mínimo que uma pessoa de pele tipo II necessita para evitar queimaduras ao se expor ao Sol, considerando TPP o intervalo das 12:00 às 14:00 h, num dia em que a irradiância efetiva é maior que 8, de acordo com os dados fornecidos, é"),
  tags=["protetor solar", "razão"])

X(19, "M", "Matemática", "Raciocínio lógico", "<p>Se Z fechar, X fica com 45 e Y com 55 (25 + 30): Y lidera. Se Y fechar, X tem 45 e Z, 55 (25 + 30): Z lidera. Se X fechar, Y tem 70 (45 + 25) e Z, 30: Y lidera. X nunca lidera. Alternativa <strong>A</strong>.</p><p>Os 55 eleitores de Y e Z preferem qualquer um dos dois a X.</p>",
  p("Um estudo realizado com 100 indivíduos que abastecem seu carro uma vez por semana em um dos postos X, Y ou Z mostrou que:")
  + "<ul><li>45 preferem X a Y, e Y a Z.</li><li>25 preferem Y a Z, e Z a X.</li><li>30 preferem Z a Y, e Y a X.</li></ul>"
  + p("Se um dos postos encerrar suas atividades, e os 100 consumidores continuarem se orientando pelas preferências descritas, é possível afirmar que a liderança de preferência nunca pertencerá a"),
  tags=["preferências", "lógica"])

X(20, "L", "Artes", "Cubismo", "<p>A tira fala do cubismo: “o tradicional único ponto de vista foi abandonado, a perspectiva foi fraturada”. Na obra E, o rosto de Marie-Thérèse aparece ao mesmo tempo de frente e de perfil, mostrando vários pontos de vista simultâneos. Alternativa <strong>E</strong>.</p><p>As obras A, B, C e D seguem uma representação com um só ponto de vista.</p>",
  p("O autor da tira utilizou os princípios de composição de um conhecido movimento artístico para representar a necessidade de um mesmo observador aprender a considerar, simultaneamente, diferentes pontos de vista.") + "[[fig:1]]"
  + fonte("Adaptado de WATTERSON, Bill. <em>Os dez anos de Calvin e Haroldo</em>. V. 2, São Paulo: Best News, 1996.")
  + p("Das obras reproduzidas, todas de autoria do pintor espanhol Pablo Picasso, aquela em cuja composição foi adotado um procedimento semelhante é:"),
  figs(("q20", "Tira de Calvin e Haroldo em dois quadros desenhados de forma fragmentada, com ângulos tortos. Legenda do primeiro: “Tudo começou quando Calvin participou de um pequeno debate com o seu pai! Logo Calvin podia ver os dois lados da questão! Então o pobre Calvin começou a ver os dois lados de tudo!”. Segundo: Calvin, desenhado ao mesmo tempo de frente e de perfil, ao lado de uma cadeira e uma cômoda deformadas: “O tradicional único ponto de vista foi abandonado! A perspectiva foi fraturada!”"),
       ("q20a", "Picasso, “Os amantes”: um casal de pé, abraçado, em representação naturalista."),
       ("q20b", "Picasso, “Retrato de Françoise”: rosto de mulher de frente, emoldurado por cabelos longos."),
       ("q20c", "Picasso, “Os pobres na praia”: uma família de figuras alongadas, em pé, à beira-mar."),
       ("q20d", "Picasso, “Os dois saltimbancos”: um homem e uma mulher sentados a uma mesa, em traços figurativos."),
       ("q20e", "Picasso, “Marie-Thérèse apoiada no cotovelo”: rosto de mulher composto ao mesmo tempo de frente e de perfil, com formas fragmentadas.")),
  ["Picasso", "Calvin"], alts=ALT(2))

X(21, "L", "Literatura", "Crônica", "<p>Nelson Rodrigues diz que o brasileiro invejava a fineza e a polidez do inglês, mas que no Mundial “o único inglês que apareceu foi o brasileiro”, o único a se manter dentro da esportividade. Os jogadores mostraram ter as qualidades que o brasileiro admirava nos europeus. Alternativa <strong>B</strong>.</p><p>Foram os europeus que deram “botinadas”; os brasileiros não se comportaram como eles (E).</p>",
  p("Em 1958, a seleção brasileira foi campeã mundial pela primeira vez. O texto foi extraído da crônica “A alegria de ser brasileiro”, do dramaturgo Nelson Rodrigues, publicada naquele ano pelo jornal <em>Última Hora</em>.")
  + ap("“Agora, com a chegada da equipe imortal, as lágrimas rolam. Convenhamos que a seleção as merece. Merece por tudo: não só pelo futebol, que foi o mais belo que os olhos mortais já contemplaram, como também pelo seu maravilhoso índice disciplinar. Até este Campeonato, o brasileiro julgava-se um cafajeste nato e hereditário. Olhava o inglês e tinha-lhe inveja. Achava o inglês o sujeito mais fino, mais sóbrio, de uma polidez e de uma cerimônia inenarráveis. E, súbito, há o Mundial. Todo mundo baixou o sarrafo no Brasil. Suecos, britânicos, alemães, franceses, checos, russos, davam botinadas em penca. Só o brasileiro se mantinha ferozmente dentro dos limites rígidos da esportividade. Então, se verificou o seguinte: o inglês, tal como o concebíamos, não existe. O único inglês que apareceu no Mundial foi o brasileiro. Por tantos motivos, vamos perder a vergonha (...), vamos sentar no meio-fio e chorar. Porque é uma alegria ser brasileiro, amigos”.")
  + p("Além de destacar a beleza do futebol brasileiro, Nelson Rodrigues quis dizer que o comportamento dos jogadores dentro do campo"),
  tags=["Nelson Rodrigues", "Copa de 1958"])

X(22, "M", "Matemática", "Áreas", "<p>O terreno é um paralelogramo. Em A, faixas de bases iguais e mesma altura; em B, as diagonais dividem o paralelogramo em quatro triângulos de áreas iguais; em C, os triângulos têm bases iguais e a mesma altura; em D, os pontos médios dos lados formam quatro paralelogramos iguais. Em E, os segmentos internos marcados como iguais não garantem que as quatro partes tenham a mesma área. Alternativa <strong>E</strong>.</p>",
  p("Um terreno com o formato mostrado na figura foi herdado por quatro irmãos e deverá ser dividido em quatro lotes de mesma área.") + "[[fig:1]]"
  + p("Um dos irmãos fez algumas propostas de divisão para que fossem analisadas pelos demais herdeiros.",
      "Dos esquemas abaixo, onde lados de mesma medida têm símbolos iguais, o único em que os quatro lotes não possuem, necessariamente, a mesma área é:"),
  figs(("q22", "Terreno em forma de paralelogramo entre as ruas A e B (paralelas) e as ruas C e D (paralelas)."),
       ("q22a", "Paralelogramo dividido em quatro faixas por segmentos paralelos aos lados inclinados, com as bases marcadas como iguais."),
       ("q22b", "Paralelogramo dividido pelas duas diagonais em quatro triângulos."),
       ("q22c", "Paralelogramo dividido em quatro triângulos por segmentos que partem de um mesmo vértice, com as bases marcadas como iguais nos lados opostos."),
       ("q22d", "Paralelogramo dividido em quatro paralelogramos por segmentos que ligam os pontos médios dos lados opostos."),
       ("q22e", "Paralelogramo com um quadrilátero interno ligado aos lados por segmentos, formando quatro partes; só alguns segmentos internos estão marcados como iguais.")),
  ["paralelogramo", "divisão de áreas"], alts=ALT(2))

X(23, "H", "História", "Cultura", "<p>I e III estão corretas: João do Rio descreve a tatuagem no Rio de 1904 entre grupos específicos (negros, turcos, meretrizes, rufiões), e mostra que ela muda de sentido conforme o tempo e o grupo (honra, ignomínia, amor, ódio). Alternativa <strong>E</strong>.</p><p>II é falsa: o texto mostra justamente funções variadas, e não apenas estética entre jovens.</p>",
  ap("“A palavra tatuagem é relativamente recente. Toda a gente sabe que foi o navegador Cook que a introduziu no Ocidente, e esse escrevia <em>tattou</em>, termo da Polinésia de <em>tatou</em> ou <em>tu tahou</em>, ‘desenho’. (...) Desde os mais remotos tempos, vemo-la a transformar-se: distintivo honorífico entre uns homens, ferrete de ignomínia entre outros, meio de assustar o adversário para os bretões, marca de uma classe de selvagens das ilhas marquesas (...) sinal de amor, de desprezo, de ódio (...). Há três casos de tatuagem no Rio, completamente diversos na sua significação moral: os negros, os turcos com o fundo religioso e o bando de meretrizes, dos rufiões e dos humildes, que se marcam por crime ou por ociosidade.”")
  + fonte("RIO, João do. Os Tatuadores. <em>Revista Kosmos</em>. 1904, apud: <em>A alma encantadora das ruas</em>, SP: Cia das Letras, 1999.")
  + p("Com base no texto são feitas as seguintes afirmações:")
  + I3("João do Rio revela como a tatuagem já estava presente na cidade do Rio de Janeiro, pelo menos desde o início do século XX, e era mais utilizada por alguns setores da população.",
       "A tatuagem, de origem polinésia, difundiu-se no ocidente com a característica que permanece até hoje: utilização entre os jovens com função estritamente estética.",
       "O texto mostra como a tatuagem é uma prática que se transforma no tempo e que alcança inúmeros sentidos nos diversos setores das sociedades e para as diferentes culturas.")
  + p("Está correto o que se afirma apenas em"),
  tags=["João do Rio", "tatuagem"])

X(24, "N", "Química", "Modelo atômico", "<p>A visão substancialista atribui a átomos e moléculas isolados propriedades do conjunto. I (átomos dourados), II (moléculas “rígidas” não formam algo macio) e IV (os átomos se expandem) fazem isso. III está de acordo com o texto: os pontos de fusão e ebulição vêm das interações entre as moléculas. Alternativa <strong>D</strong>.</p>",
  ap("Quando definem moléculas, os livros geralmente apresentam conceitos como: “a menor parte da substância capaz de guardar suas propriedades”. A partir de definições desse tipo, a idéia transmitida ao estudante é a de que o constituinte isolado (moléculas) contém os atributos do todo.",
     "É como dizer que uma molécula de água possui densidade, pressão de vapor, tensão superficial, ponto de fusão, ponto de ebulição, etc. Tais propriedades pertencem ao conjunto, isto é, manifestam-se nas relações que as moléculas mantêm entre si.")
  + fonte("Adaptado de OLIVEIRA, R. J. O Mito da Substância. <em>Química Nova na Escola</em>, n.º 1, 1995.")
  + p("O texto evidencia a chamada visão substancialista que ainda se encontra presente no ensino da Química. Abaixo estão relacionadas algumas afirmativas pertinentes ao assunto.")
  + '<ol type="I"><li>O ouro é dourado, pois seus átomos são dourados.</li><li>Uma substância “macia” não pode ser feita de moléculas “rígidas”.</li><li>Uma substância pura possui pontos de ebulição e fusão constantes, em virtude das interações entre suas moléculas.</li><li>A expansão dos objetos com a temperatura ocorre porque os átomos se expandem.</li></ol>'
  + p("Dessas afirmativas, estão apoiadas na visão substancialista criticada pelo autor apenas"),
  tags=["propriedades das substâncias"])

X(25, "H", "Geografia", "Demografia", "<p>O único grupo que cresce em todos os anos do gráfico é o de mais de 65 anos: 3,1% (1970), 4,9% (1995), 8,8% (2000) e 18,4% (2050). O título adequado fala do envelhecimento: “O Brasil de cabelos brancos”. Alternativa <strong>E</strong>.</p><p>Os menores de 15 anos diminuem (A, B), e o grupo de 15 a 65 cai de 2000 para 2050 (C).</p>",
  p("Em reportagem sobre crescimento da população brasileira, uma revista de divulgação científica publicou tabela com a participação relativa de grupos etários na população brasileira, no período de 1970 a 2050 (projeção), em três faixas de idade: abaixo de 15 anos; entre 15 e 65 anos; e acima de 65 anos.") + "[[fig:1]]"
  + p("Admitindo-se que o título da reportagem se refira ao grupo etário cuja população cresceu sempre, ao longo do período registrado, um título adequado poderia ser:"),
  figs(("q25a", "Gráfico de barras da participação (%) dos grupos etários. 1970: abaixo de 15 anos, 42,1; de 15 a 65, 54,8; acima de 65, 3,1. 1995: 31,8; 63,3; 4,9. 2000: 21,5; 69,7; 8,8. 2050: 17,2; 64,4; 18,4.")),
  ["envelhecimento", "estrutura etária"])

X(26, "N", "Física", "Rendimento", "<p>O rendimento global é o produto dos rendimentos de cada etapa. P1 (direto): 0,95 × 0,70 ≈ 0,67. P2 (indireto): 0,40 × 0,90 × 0,95 ≈ 0,34. P2 é menos eficiente, sobretudo pelo baixo rendimento da termoelétrica (40%). Alternativa <strong>A</strong>.</p><p>A distribuição elétrica tem rendimento alto, 90% (B).</p>",
  p("Na comparação entre diferentes processos de geração de energia, devem ser considerados aspectos econômicos, sociais e ambientais. Um fator economicamente relevante nessa comparação é a eficiência do processo. Eis um exemplo: a utilização do gás natural como fonte de aquecimento pode ser feita pela simples queima num fogão (uso direto), ou pela produção de eletricidade em uma termoelétrica e uso de aquecimento elétrico (uso indireto). Os rendimentos correspondentes a cada etapa de dois desses processos estão indicados entre parênteses no esquema.")
  + "[[fig:1]]" + p("Na comparação das eficiências, em termos globais, entre esses dois processos (direto e indireto), verifica-se que"),
  figs(("q26a", "Esquema de dois processos. P1 (uso direto): gás → distribuição por gasoduto (0,95) → fornalha de gás (0,70) → calor liberado. P2 (uso indireto): gás liberado → termoelétrica (0,40) → distribuição elétrica (0,90) → aquecedor elétrico (0,95) → calor.")),
  ["eficiência", "gás natural"])

X(27, "M", "Matemática", "Análise combinatória", "<p>Um código de 5 barras que se lê igual nos dois sentidos fica determinado pelas 3 primeiras barras (a 4ª repete a 2ª e a 5ª, a 1ª): 2<sup>3</sup> = 8 códigos. Tirando os dois de barras todas claras ou todas escuras, restam 6. Alternativa <strong>D</strong>.</p>",
  p("O código de barras, contido na maior parte dos produtos industrializados, consiste num conjunto de várias barras que podem estar preenchidas com cor escura ou não. Quando um leitor óptico passa sobre essas barras, a leitura de uma barra clara é convertida no número 0 e a de uma barra escura, no número 1. Observe abaixo um exemplo simplificado de um código em um sistema de código com 20 barras.")
  + "[[fig:1]]"
  + p("Se o leitor óptico for passado da esquerda para a direita irá ler: 01011010111010110001",
      "Se o leitor óptico for passado da direita para a esquerda irá ler: 10001101011101011010",
      "No sistema de código de barras, para se organizar o processo de leitura óptica de cada código, deve-se levar em consideração que alguns códigos podem ter leitura da esquerda para a direita igual à da direita para a esquerda, como o código 00000000111100000000, no sistema descrito acima.",
      "Em um sistema de códigos que utilize apenas cinco barras, a quantidade de códigos com leitura da esquerda para a direita igual à da direita para a esquerda, desconsiderando-se todas as barras claras ou todas as escuras, é"),
  figs(("q27a", "Código de 20 barras claras e escuras, correspondente à leitura 01011010111010110001.")),
  ["palíndromos", "contagem"])

X(28, "H", "História", "Terrorismo", "<p>O primeiro caso é o de grupos que lutam para derrubar um governo; o segundo, o de quem combate um Estado do qual não faz parte, sem limites territoriais. Os movimentos de libertação dos anos 1950–70 se encaixam no primeiro (I), e os ataques dos anos 1990 e de 2001, no segundo (II). Alternativa <strong>C</strong>.</p><p>III põe os dois tipos de evento no primeiro caso, contrariando a distinção.</p>",
  ap("1 - “(...) O recurso ao terror por parte de quem já detém o poder dentro do Estado não pode ser arrolado entre as formas de terrorismo político, porque este se qualifica, ao contrário, como o instrumento ao qual recorrem determinados grupos para derrubar um governo acusado de manter-se por meio do terror”.",
     "2 - Em outros casos “os terroristas combatem contra um Estado de que não fazem parte e não contra um governo (o que faz com que sua ação seja conotada como uma forma de guerra), mesmo quando por sua vez não representam um outro Estado. Sua ação aparece então como irregular, no sentido de que não podem organizar um exército e não conhecem limites territoriais, já que não provêm de um Estado”.")
  + fonte("<em>Dicionário de Política</em> (org.) BOBBIO, N., MATTEUCCI, N. e PASQUINO, G., Brasília: Edunb, 1986.")
  + p("De acordo com as duas afirmações, é possível comparar e distinguir os seguintes eventos históricos:")
  + I3("Os movimentos guerrilheiros e de libertação nacional realizados em alguns países da África e do sudeste asiático entre as décadas de 1950 e 70 são exemplos do primeiro caso.",
       "Os ataques ocorridos na década de 1990, como às embaixadas de Israel, em Buenos Aires, dos EUA, no Quênia e Tanzânia, e ao World Trade Center em 2001, são exemplos do segundo caso.",
       "Os movimentos de libertação nacional dos anos 50 a 70 na África e sudeste asiático, e o terrorismo dos anos 90 e 2001 foram ações contra um inimigo invasor e opressor, e são exemplos do primeiro caso.")
  + p("É correto o que se afirma apenas em"),
  tags=["terrorismo", "descolonização"])

X(29, "N", "Física", "Ordem de grandeza", "<p>200 mil MWh = 2 × 10<sup>8</sup> kWh. Com 10 kWh por kg, são necessários 2 × 10<sup>7</sup> kg = 20.000 toneladas de carvão por dia. Com 10 toneladas por caminhão: 2.000 caminhões. Alternativa <strong>D</strong>.</p><p>Esquecer que 1 MWh = 1.000 kWh leva a 2 caminhões, valor que nem aparece entre as opções.</p>",
  p("Os números e cifras envolvidos, quando lidamos com dados sobre produção e consumo de energia em nosso país, são sempre muito grandes. Apenas no setor residencial, em um único dia, o consumo de energia elétrica é da ordem de 200 mil MWh. Para avaliar esse consumo, imagine uma situação em que o Brasil não dispusesse de hidrelétricas e tivesse de depender somente de termoelétricas, onde cada kg de carvão, ao ser queimado, permite obter uma quantidade de energia da ordem de 10 kWh. Considerando que um caminhão transporta, em média, 10 toneladas de carvão, a quantidade de caminhões de carvão necessária para abastecer as termoelétricas, a cada dia, seria da ordem de"),
  tags=["unidades de energia", "termelétricas"])

X(30, "L", "Língua Portuguesa", "Variação linguística", "<p>Daniel Piza finge apoiar o projeto contra estrangeirismos e propõe proibir também o “tu vai” gaúcho, o “me vê dois pastel” e outros usos regionais e populares. O exagero mostra o absurdo de legislar sobre a língua: é ironia. Alternativa <strong>B</strong>.</p><p>O título (“Uma proposta imodesta”) e a própria lista de proibições mostram que o autor não é favorável à proposta (A) nem preconceituoso (D).</p>",
  ap("Só falta o Senado aprovar o projeto de lei [sobre o uso de termos estrangeiros no Brasil] para que palavras como <em>shopping center</em>, <em>delivery</em> e <em>drive-through</em> sejam proibidas em nomes de estabelecimentos e marcas. Engajado nessa valorosa luta contra o inimigo ianque, que quer fazer área de livre comércio com nosso inculto e belo idioma, venho sugerir algumas outras medidas que serão de extrema importância para a preservação da soberania nacional, a saber: (...)")
  + "<ul><li>Nenhum cidadão carioca ou gaúcho poderá dizer “Tu vai” em espaços públicos do território nacional;</li><li>Nenhum cidadão paulista poderá dizer “Eu lhe amo” e retirar ou acrescentar o plural em sentenças como “Me vê um chopps e dois pastel”; (...)</li><li>Nenhum dono de borracharia poderá escrever cartaz com a palavra “borraxaria” e nenhum dono de banca de jornal anunciará “Vende-se cigarros”; (...)</li><li>Nenhum livro de gramática obrigará os alunos a utilizar colocações pronominais como “casar-me-ei” ou “ver-se-ão”.</li></ul>"
  + fonte("PIZA, Daniel. Uma proposta imodesta. <em>O Estado de S. Paulo</em>, São Paulo, 8/04/2001.") + p("No texto acima, o autor"),
  tags=["estrangeirismos", "ironia"], alts=dict(D[30], E="defende o ensino rigoroso da gramática para que todos aprendam a empregar corretamente os pronomes."))

CORVINA = (tit("Texto para as questões 31 e 32.")
  + p("A corvina é um peixe carnívoro que se alimenta de crustáceos, moluscos e pequenos peixes que vivem no fundo do mar. É bastante utilizada na alimentação humana, sendo encontrada em toda a costa brasileira, embora seja mais abundante no sul do País. A tabela registra a concentração média anual de mercúrio no tecido muscular de corvinas capturadas em quatro áreas.")
  + tabela(["Área de coleta", "Mercúrio no músculo (ng/g)", "Características da área"],
           [["Baía de Guanabara (RJ)", "193,6", "Área de intensa atividade portuária, que recebe esgotos domésticos não tratados e rejeitos industriais de cerca de 6.000 fontes."],
            ["Baía de Ilha Grande (RJ)", "153,8", "Recebe rejeitos de parque industrial ainda em fase de crescimento e é uma das principais fontes de pescado do estado."],
            ["Baía de Sepetiba (RJ)", "124,0", "Área sujeita a eficientes efeitos de maré e com baixa atividade pesqueira, sem fontes industriais de contaminação por mercúrio."],
            ["Lagoa da Conceição (SC)", "90,6*", "Importante fonte de pescado no litoral catarinense, na qual praticamente inexiste contaminação industrial por mercúrio."]])
  + fonte("*Concentração natural de mercúrio, característica de local não contaminado. KEHRIG, H. A. &amp; MALM, O. Mercúrio: uma avaliação na costa brasileira. <em>Ciência Hoje</em>, outubro, 1997."))
X(31, "N", "Química", "Poluição", "<p>Em geral, quanto mais atividade industrial, mais mercúrio: Guanabara (193,6) &gt; Ilha Grande (153,8) &gt; Lagoa da Conceição (90,6, nível natural). A exceção é a Baía de Sepetiba, que não tem fontes industriais de mercúrio e ainda assim apresenta 124,0 ng/g, valor que pede investigação sobre o papel das marés. Alternativa <strong>E</strong>.</p><p>A Lagoa da Conceição tem exatamente o valor esperado para local não contaminado (B, C).</p>",
  CORVINA + p("Comparando as características das quatro áreas de coleta às respectivas concentrações médias anuais de mercúrio nas corvinas capturadas, pode-se considerar que, à primeira vista, os resultados"),
  tags=["mercúrio", "leitura de tabela"])
X(32, "N", "Biologia", "Bioacumulação", "<p>O mercúrio se acumula nos organismos e aumenta a cada nível da cadeia alimentar (magnificação trófica). Mesmo abaixo do limite legal, o mercúrio ingerido com as corvinas soma-se ao já acumulado no corpo humano. Alternativa <strong>E</strong>.</p><p>A concentração aumenta, e não diminui, ao longo da cadeia (B), e isso torna o consumo mais perigoso, não menos (C).</p>",
  CORVINA + p("Segundo a legislação brasileira, o limite máximo permitido para as concentrações de mercúrio total é de 500 nanogramas por grama de peso úmido. Ainda levando em conta os dados da tabela e o tipo de circulação do mercúrio ao longo da cadeia alimentar, pode-se considerar que a ingestão, pelo ser humano, de corvinas capturadas nessas regiões,"),
  tags=["mercúrio", "cadeia alimentar"])

X(33, "N", "Física", "Fontes de energia", "<p>A celulignina é um combustível sólido: queimado, gera calor para produzir vapor e mover as turbinas, como o gás natural numa termoelétrica. Alternativa <strong>A</strong>.</p><p>O vapor (B), a queda d’água (C) e as pás (D) são partes do processo de conversão, e não o combustível; e não há reação nuclear (E).</p>",
  p("Segundo matéria publicada em um jornal brasileiro, “Todo o lixo (orgânico) produzido pelo Brasil hoje – cerca de 20 milhões de toneladas por ano – seria capaz de aumentar em 15% a oferta de energia elétrica. Isso representa a metade da energia produzida pela hidrelétrica de Itaipu. O segredo está na celulignina, combustível sólido gerado a partir de um processo químico a que são submetidos os resíduos orgânicos”.")
  + fonte("<em>O Estado de São Paulo</em>, 01/01/2001.")
  + p("Independentemente da viabilidade econômica desse processo, ainda em fase de pesquisa, na produção de energia pela técnica citada nessa matéria, a celulignina faria o mesmo papel"),
  tags=["biomassa", "termelétrica"])

X(34, "N", "Física", "Calor e brisas", "<p>À noite o solo esfria rápido e o mar continua mais quente. O ar sobre a água fica mais quente, sobe e cria baixa pressão, e o ar do continente se desloca para o mar: é a brisa terrestre. Alternativa <strong>A</strong>.</p><p>Ar quente sobe, não desce (B), e o ar não se “dissolve” na água (C).</p>",
  p("Numa área de praia, a brisa marítima é uma conseqüência da diferença no tempo de aquecimento do solo e da água, apesar de ambos estarem submetidos às mesmas condições de irradiação solar. No local (solo) que se aquece mais rapidamente, o ar fica mais quente e sobe, deixando uma área de baixa pressão, provocando o deslocamento do ar da superfície que está mais fria (mar).")
  + "[[fig:1]]" + p("À noite, ocorre um processo inverso ao que se verifica durante o dia") + "[[fig:2]]"
  + p("Como a água leva mais tempo para esquentar (de dia), mas também leva mais tempo para esfriar (à noite), o fenômeno noturno (brisa terrestre) pode ser explicado da seguinte maneira:"),
  figs(("q34a", "Esquema de dia: o sol aquece o continente, onde o ar sobe (“menor pressão”, “maior temperatura”); uma seta mostra a brisa marítima vindo do mar, de menor temperatura, para a terra."),
       ("q34b", "Esquema de noite, com a lua: uma seta mostra a brisa terrestre indo do continente para o mar.")),
  ["brisa marítima", "calor específico"])

X(35, "N", "Física", "Efeito Joule", "<p>Lâmpadas incandescentes, chuveiro na posição “quente”, ferro elétrico, tomadas sobrecarregadas e fios finos demais têm em comum a transformação de energia elétrica em calor, desperdiçado ou excessivo. As recomendações buscam reduzir essa conversão. Alternativa <strong>C</strong>.</p><p>Nem todas reduzem a potência (A) ou o tempo de uso (B).</p>",
  p("Entre as inúmeras recomendações dadas para a economia de energia elétrica em uma residência, destacamos as seguintes:")
  + "<ul><li>Substitua lâmpadas incandescentes por fluorescentes compactas.</li><li>Evite usar o chuveiro elétrico com a chave na posição “inverno” ou “quente”.</li><li>Acumule uma quantidade de roupa para ser passada a ferro elétrico de uma só vez.</li><li>Evite o uso de tomadas múltiplas para ligar vários aparelhos simultaneamente.</li><li>Utilize, na instalação elétrica, fios de diâmetros recomendados às suas finalidades.</li></ul>"
  + p("A característica comum a todas essas recomendações é a proposta de economizar energia através da tentativa de, no dia-a-dia, reduzir"),
  tags=["economia de energia"],
  alts=dict(D[35], D="o consumo de energia térmica convertida em energia elétrica.", E="o consumo de energia elétrica através de correntes de fuga."))

X(36, "H", "Geografia", "Relevo e clima", "<p>I está correta: as linhas de precipitação são mais altas nas encostas voltadas para o oceano, de onde vêm os ventos úmidos. II também: depois do topo da serra a chuva cai muito, criando uma área sujeita a desertificação (sombra de chuva). E III também: por volta de 25 km e de 100 km estão as maiores precipitações anuais, junto às encostas, onde a água é mais abundante para plantas e animais. Alternativa <strong>E</strong>.</p>",
  p("A chuva é determinada, em grande parte, pela topografia e pelo padrão dos grandes movimentos atmosféricos ou meteorológicos. O gráfico mostra a precipitação anual média (linhas verticais) em relação à altitude (curvas) em uma região em estudo.")
  + "[[fig:1]]" + p("De uma análise ambiental desta região concluiu-se que:")
  + I3("Ventos oceânicos carregados de umidade depositam a maior parte desta umidade, sob a forma de chuva, nas encostas da serra voltadas para o oceano.",
       "Como resultado da maior precipitação nas encostas da serra, surge uma região de possível desertificação do outro lado dessa serra.",
       "Os animais e as plantas encontram melhores condições de vida, sem períodos prolongados de seca, nas áreas distantes 25km e 100km, aproximadamente, do oceano.")
  + p("É correto o que se afirma em:"),
  figs(("q36a", "Gráfico com a distância do oceano (0 a 150 km) no eixo horizontal, a precipitação anual (linhas verticais) e a altitude (curva). Ventos oceânicos sopram da esquerda para a direita. A curva de altitude forma uma pequena elevação perto de 25 km, um vale até cerca de 70 km e uma serra que sobe a partir de 100 km até o topo perto de 125 km, descendo depois. As linhas de precipitação são altas perto de 25 km e muito altas entre 100 e 110 km, nas encostas voltadas para o oceano, e caem bastante após o topo da serra. Fonte: modificado de Odum, Ecologia, 1988.")),
  ["chuvas orográficas", "sombra de chuva"])

X(37, "H", "História", "Neocolonialismo", "<p>As fronteiras africanas, traçadas em linhas retas, meridianos e paralelos, resultam da partilha do continente pelas potências europeias no fim do século XIX, interessadas em seus recursos naturais, sem respeitar os povos. Alternativa <strong>B</strong>.</p><p>Não se trata de técnica cartográfica (A), desertos (C), nomadismo (D) ou custo de demarcação (E).</p>",
  ap("“O continente africano em seu conjunto apresenta 44% de suas fronteiras apoiadas em meridianos e paralelos; 30% por linhas retas e arqueadas, e apenas 26% se referem a limites naturais que geralmente coincidem com os de locais de habitação dos grupos étnicos”")
  + fonte("MARTIN, A. R. <em>Fronteiras e Nações</em>. Contexto, São Paulo, 1998.")
  + p("Diferente do continente americano, onde quase que a totalidade das fronteiras obedecem a limites naturais, a África apresenta as características citadas em virtude, principalmente,"),
  tags=["partilha da África", "fronteiras"])

X(38, "M", "Matemática", "Porcentagem", "<p>Com o mesmo número de homens e mulheres, a porcentagem geral é a média: (35% + 12%)/2 = 23,5%, cerca de 24%. A manchete (47%) somou as duas porcentagens, o que não faz sentido para grupos de mesmo tamanho. Alternativa <strong>B</strong>.</p><p>Com 100 homens e 100 mulheres, por exemplo: 12 + 35 = 47 pessoas sem desejo em 200, ou seja, 23,5%.</p>",
  p("A capa de uma revista de grande circulação trazia a seguinte informação, relativa a uma reportagem daquela edição:")
  + ap("“O brasileiro diz que é feliz na cama, mas debaixo dos lençóis 47% não sentem vontade de fazer sexo”.")
  + p("O texto abaixo, no entanto, adaptado da mesma reportagem, mostra que o dado acima está errado:")
  + ap("“Outro problema predominantemente feminino é a falta de desejo − 35% das mulheres não sentem nenhuma vontade de ter relações. Já entre os homens, apenas 12% se queixam de falta de desejo”.")
  + p("Considerando que o número de homens na população seja igual ao de mulheres, a porcentagem aproximada de brasileiros que não sentem vontade de fazer sexo, de acordo com a reportagem, é"),
  tags=["média", "porcentagem"])

X(39, "H", "Sociologia", "Técnica e sociedade", "<p>I e II estão corretas: o arco e flecha ampliou a ação dos braços e mudou a caça e a organização social; a locomotiva transformou o transporte e a percepção do espaço e do tempo. III é falsa: a televisão mudou profundamente a forma de conceber o mundo, e não é só lazer passivo. Alternativa <strong>B</strong>.</p>",
  p("Considere o papel da técnica no desenvolvimento da constituição de sociedades e três invenções tecnológicas que marcaram esse processo: invenção do arco e flecha nas civilizações primitivas, locomotiva nas civilizações do século XIX e televisão nas civilizações modernas.", "A respeito dessas invenções são feitas as seguintes afirmações:")
  + I3("A primeira ampliou a capacidade de ação dos braços, provocando mudanças na forma de organização social e na utilização de fontes de alimentação.",
       "A segunda tornou mais eficiente o sistema de transporte, ampliando possibilidades de locomoção e provocando mudanças na visão de espaço e de tempo.",
       "A terceira possibilitou um novo tipo de lazer que, envolvendo apenas participação passiva do ser humano, não provocou mudanças na sua forma de conceber o mundo.")
  + p("Está correto o que se afirma em:"),
  tags=["tecnologia"])

X(40, "N", "Química", "Concentração", "<p>50 g de íons cobre em 20.000 L dão 50.000 mg/20.000 L = 2,5 mg/L. Pelo Gráfico II, a concentração que mata 50% dos camarões em 24 horas é cerca de 2,5 mg/L. Então, após 24 horas, cerca de metade estaria viva. Alternativa <strong>C</strong>.</p><p>O Gráfico I vale para 14 horas de exposição, e não para 24.</p>",
  p("Para testar o uso do algicida sulfato de cobre em tanques para criação de camarões, estudou-se, em aquário, a resistência desses organismos a diferentes concentrações de íons cobre (representados por Cu<sup>2+</sup>). Os gráficos relacionam a mortandade de camarões com a concentração de Cu<sup>2+</sup> e com o tempo de exposição a esses íons.")
  + "[[fig:1]]" + p("Se os camarões utilizados na experiência fossem introduzidos num tanque de criação contendo 20.000 L de água tratada com sulfato de cobre, em quantidade suficiente para fornecer 50 g de íons cobre, estariam vivos, após 24 horas, cerca de"),
  figs(("q40a", "Gráfico I: porcentagem de camarões mortos em função da concentração de Cu2+ (mg/L, escala logarítmica), para 14 horas de exposição: cerca de 0% com 1 mg/L, 22% com 2, 52% com 3,5, 78% com 6,5 e 100% com 12 mg/L. Gráfico II: tempo de exposição (horas, escala logarítmica, marcas em 1,7, 24, 96 e 167) em função da concentração de Cu2+ que causa 50% de mortalidade: a curva cai de cerca de 96 horas perto de 1,7 mg/L para 24 horas perto de 2,5 mg/L e para menos de 1,7 hora acima de 7 mg/L. Fonte: Vowles e Connell, 1980.")),
  ["concentração", "toxicidade"], alts=dict(D[40], E="3/4."))

CALEND = (tit("Texto para as questões 41 e 42.")
  + ap("Existem muitas diferenças entre as culturas cristã e islâmica. Uma das principais diz respeito ao Calendário. Enquanto o Calendário Cristão (Gregoriano) considera um ano como o período correspondente ao movimento de translação da Terra em torno do Sol – aproximadamente 365 dias, o Calendário Muçulmano se baseia nos movimentos de translação da Lua em torno da Terra – aproximadamente 12 por ano, o que corresponde a anos intercalados de 254 e 255 dias."))
X(41, "M", "Matemática", "Funções", "<p>O ano muçulmano é mais curto: 33 anos muçulmanos valem 32 cristãos, então cada M anos muçulmanos correspondem a M − M/33 anos cristãos. Somando o início do calendário, em 622: C = M + 622 − M/33. Alternativa <strong>A</strong>.</p><p>Subtrair 622 (C, D) faria o ano cristão ser menor que o muçulmano.</p>",
  CALEND + p("Considerando que o Calendário Muçulmano teve início em 622 da era cristã e que cada 33 anos muçulmanos correspondem a 32 anos cristãos, é possível estabelecer uma correspondência aproximada de anos entre os dois calendários, dada por:", "(C = Anos Cristãos e M = Anos Muçulmanos)"),
  tags=["calendário muçulmano"],
  alts=A5(r"\(C = M + 622 - \frac{M}{33}\)", r"\(C = M - 622 + \left(C - \frac{622}{32}\right)\)", r"\(C = M - 622 - \frac{M}{33}\)", r"\(C = M - 622 + \left(C - \frac{622}{33}\right)\)", r"\(C = M + 622 - \frac{M}{32}\)"))
X(42, "N", "Física", "Fases da Lua", "<p>O mês muçulmano começa com a lua nova, quando aparece o primeiro fino crescente. Pelo calendário de novembro de 2001, a lua nova foi em 15 de novembro, e o Ramadã começou no dia seguinte, 16. Alternativa <strong>C</strong>.</p><p>8 e 22 de novembro são quarto minguante e crescente, e 1º de novembro, a lua cheia.</p>",
  CALEND + p("O ano muçulmano é composto de 12 meses, dentre eles o Ramadã, mês sagrado para os muçulmanos que, em 2001, teve início no mês de novembro do Calendário Cristão, conforme a figura que segue.") + "[[fig:1]]"
  + p("Considerando as características do Calendário Muçulmano, é possível afirmar que, em 2001, o mês Ramadã teve início, para o Ocidente, em"),
  figs(("q42a", "Calendário de novembro de 2001, que começa numa quinta-feira, com as fases da Lua: minguante em 8, nova em 15, crescente em 22 e cheia em 1º e em 30.")),
  ["Ramadã", "lua nova"])

X(43, "N", "Física", "Fontes de energia", "<p>Água em queda, vento e luz solar são fontes que se renovam continuamente: os três processos usam energia renovável. Alternativa <strong>D</strong>.</p><p>Todos têm algum impacto ambiental (A), dependem do clima (B) e não armazenam por si a energia gerada (C).</p>",
  p("Em usinas hidrelétricas, a queda d’água move turbinas que acionam geradores. Em usinas eólicas, os geradores são acionados por hélices movidas pelo vento. Na conversão direta solar-elétrica são células fotovoltaicas que produzem tensão elétrica. Além de todos produzirem eletricidade, esses processos têm em comum o fato de"),
  tags=["energia renovável"])

X(44, "N", "Biologia", "Saúde", "<p>I e III estão corretas: o sucesso dos coquetéis pode ter levado ao descuido na prevenção; e, com vírus cada vez mais resistentes, os infectados também precisam usar camisinha. II é falsa: o texto diz que 20% dos casos não respondem às duas principais drogas, não que não haja tratamento nem prevenção. Alternativa <strong>C</strong>.</p>",
  p("Uma nova preocupação atinge os profissionais que trabalham na prevenção da AIDS no Brasil. Tem-se observado um aumento crescente, principalmente entre os jovens, de novos casos de AIDS, questionando-se, inclusive, se a prevenção vem sendo ou não relaxada. Essa temática vem sendo abordada pela mídia:")
  + ap("“Medicamentos já não fazem efeito em 20% dos infectados pelo vírus HIV. Análises revelam que um quinto das pessoas recém-infectadas não haviam sido submetidas a nenhum tratamento e, mesmo assim, não responderam às duas principais drogas anti-AIDS. Dos pacientes estudados, 50% apresentavam o vírus FB, uma combinação dos dois subtipos mais prevalentes no país, F e B”.")
  + fonte("Adaptado do <em>Jornal do Brasil</em>, 02/10/2001.")
  + p("Dadas as afirmações acima, considerando o enfoque da prevenção, e devido ao aumento de casos da doença em adolescentes, afirma-se que")
  + I3("O sucesso inicial dos coquetéis anti-HIV talvez tenha levado a população a se descuidar e não utilizar medidas de proteção, pois se criou a idéia de que estes remédios sempre funcionam.",
       "Os vários tipos de vírus estão tão resistentes que não há nenhum tipo de tratamento eficaz e nem mesmo qualquer medida de prevenção adequada.",
       "Os vírus estão cada vez mais resistentes e, para evitar sua disseminação, os infectados também devem usar camisinhas e não apenas administrar coquetéis.")
  + p("Está correto o que se afirma em"),
  tags=["AIDS", "prevenção"])

X(45, "H", "Geografia", "Globalização", "<p>As perguntas do autor apontam a miséria, as guerras e o sofrimento espalhados pelo mundo, ligados à ação das potências “civilizadas”. A resposta é que “ao longo da história, o homem civilizado globalizou todas as suas mazelas”. Alternativa <strong>B</strong>.</p><p>As outras frases tratam de pontos isolados (Nova Iorque, Europa, mercado, armas), sem responder ao conjunto das perguntas.</p>",
  p("Um jornalista publicou um texto do qual estão transcritos trechos do primeiro e do último parágrafos:")
  + ap("“‘Mamãezinha, minhas mãozinhas vão crescer de novo?’ Jamais esquecerei a cena que vi, na TV francesa, de uma menina da Costa do Marfim falando com a enfermeira que trocava os curativos de seus dois cotos de braços. (...)”",
       "(...)", "“Como manter a paz num planeta onde boa parte da humanidade não tem acesso às necessidade básicas mais elementares? (...) Como reduzir o abismo entre o camponês afegão, a criança faminta do Sudão, o Severino da cesta básica e o corretor de Wall Street? Como explicar ao menino de Bagdá que morre por falta de remédios, bloqueados pelo Ocidente, que o mal se abateu sobre Manhattan? Como dizer aos chechenos que o que aconteceu nos Estados Unidos é um absurdo? Vejam Grozny, a capital da Chechênia, arrasada pelos russos. Alguém se incomodou com os sofrimentos e as milhares de vítimas civis, inocentes, desse massacre? Ou como explicar à menina da Costa do Marfim o sentido da palavra ‘civilização’ quando ela descobrir que suas mãos não crescerão jamais?”")
  + fonte("UTZERI, Fritz. <em>Jornal do Brasil</em>, 17/09/2001.")
  + p("Apresentam-se, abaixo, algumas afirmações também retiradas do mesmo texto. Aquela que explicita uma resposta do autor para as perguntas feitas no trecho citado é:"),
  tags=["11 de setembro", "desigualdade"], alts=dict(D[45], E="“os negócios das indústrias de armas continuam de vento em popa”."))

X(46, "L", "Artes", "Pintura e poesia", "<p>O poema descreve o “anjo camponês” que entra pela janela com “a terceira luz na mão” e “planta no ar” a chama do candeeiro. No quadro, essa figura entra pela janela em e1, estende o braço em d1 e segura a lamparina em c1, na faixa de cima. Alternativa <strong>C</strong>.</p>",
  p("A leitura do poema <em>Descrição da guerra em Guernica</em> traz à lembrança o famoso quadro de Picasso.") + "[[fig:1]]"
  + fonte("Carlos de Oliveira in ANDRADE, Eugénio. <em>Antologia Pessoal da Poesia Portuguesa</em>. Porto: Campo das Letras, 1999.")
  + p("Uma análise cuidadosa do quadro permite que se identifiquem as cenas referidas nos trechos do poema.") + "[[fig:2]]"
  + p("Podem ser relacionadas ao texto lido as partes:"),
  figs(("q46b", "Trecho do poema de Carlos de Oliveira: um anjo camponês entra pela janela com uma luz na mão; acostumado aos interiores rurais, não entende os símbolos daquela colheita (hélices, motores furiosos), estende o braço e planta no ar, como uma árvore, a chama do candeeiro."),
       ("q46", "Reprodução de “Guernica”, de Picasso (1937), dividida em uma grade com colunas a até f e linhas 1 a 3. Na faixa de cima, uma figura entra por uma janela (e1) e estende o braço (d1) segurando uma lamparina acesa (c1), perto de uma lâmpada no teto e da cabeça de um cavalo. À esquerda, o touro (a1) e uma mulher com uma criança morta (a2); embaixo, um guerreiro caído (a3 a c3); à direita, uma figura com os braços erguidos (f1 e f2).")),
  ["Guernica", "Picasso"],
  alts=A5("a1, a2, a3.", "f1, e1, d1.", "e1, d1, c1.", "c1, c2, c3.", "e1, e2, e3."))

X(47, "N", "Física", "Termodinâmica", "<p>Usinas nucleares e termelétricas transformam calor em trabalho, e esse processo tem perdas de calor sempre elevadas, por limites da própria termodinâmica. Por isso só cerca de 10% da energia primária chega como eletricidade útil. Alternativa <strong>D</strong>.</p><p>As temperaturas citadas em A e B estão erradas, e hidrelétricas não usam calor (E).</p>",
  "[[fig:1]]" + p("O diagrama mostra a utilização das diferentes fontes de energia no cenário mundial. Embora aproximadamente um terço de toda energia primária seja orientada à produção de eletricidade, apenas 10% do total são obtidos em forma de energia elétrica útil.",
                  "A pouca eficiência do processo de produção de eletricidade deve-se, sobretudo, ao fato de as usinas"),
  figs(("q47a", "Diagrama em barra da energia primária mundial (escala de 10% a 90%): cerca de 30% são destinados à produção de eletricidade; desses, cerca de 20% são calor perdido na produção e só cerca de 10% resultam em energia elétrica útil.")),
  ["rendimento", "usinas térmicas"])

X(48, "H", "Geografia", "Questão ambiental", "<p>Pelo gráfico, os EUA emitiram cerca de 186 bilhões de toneladas de CO2 desde 1950. O Brasil, com emissão máxima de 2,5 t por habitante e 160 milhões de habitantes, emite 2,5 × 160 milhões = 0,4 bilhão de toneladas por ano. Para chegar a 186 bilhões: 186/0,4 ≈ 465 anos, cerca de 460. Alternativa <strong>C</strong>.</p>",
  p("Em março de 2001, o presidente dos Estados Unidos da América, George W. Bush, causou polêmica ao contestar o pacto de Kyoto, dizendo que o acordo é prejudicial à economia norte-americana em um momento em que o país passa por uma crise de energia (...) O protocolo de Kyoto prevê que os países industrializados reduzam suas emissões de CO2 até 2012 em 5,2%, em relação aos níveis de 1990.")
  + fonte("Adaptado da <em>Folha de São Paulo</em>, 11/04/2001.") + "[[fig:1]]"
  + p("O gráfico mostra o total de CO2 emitido nos últimos 50 anos por alguns países, juntamente com os valores de emissão máxima de CO2 por habitante no ano de 1999.",
      "Dados populacionais aproximados (nº de habitantes): EUA: 240 milhões; BRASIL: 160 milhões.",
      "Se o Brasil mantivesse constante a sua população e o seu índice anual máximo de emissão de CO2, o tempo necessário para o Brasil atingir o acumulado atual dos EUA seria, aproximadamente, igual a"),
  figs(("q48a", "Gráfico de barras do total de emissões de CO2 desde 1950 (bilhões de toneladas): EUA, cerca de 186; China, cerca de 58; Austrália, cerca de 7; Brasil, cerca de 7. A legenda indica a emissão anual máxima por habitante (toneladas): EUA, 36; China, 7; Austrália e Brasil, 2,5. Fonte: adaptado da revista Veja, 18/04/2001.")),
  ["Protocolo de Kyoto", "estimativa"], quim=True)

X(49, "N", "Biologia", "Ecologia", "<p>Repor peixes não corrige a causa da perda de qualidade da água: as populações nativas diminuíram por causa da poluição. A sentença confunde quantidade de peixes com qualidade ambiental, e por isso o peixamento precisa ser repetido muitas vezes. Alternativa <strong>D</strong>.</p><p>A penalidade não reverte nem impede a poluição (C, E).</p>",
  p("Nos peixamentos – designação dada à introdução de peixes em sistemas aquáticos, nos quais a qualidade da água reduziu as populações nativas de peixes – podem ser utilizados peixes importados de outros países, peixes produzidos em unidades de piscicultura ou, como é o caso da grande maioria dos peixamentos no Brasil, de peixes capturados em algum ambiente natural e liberados em outro. Recentemente começaram a ser utilizados peixes híbridos, como os “paquis”, obtidos por cruzamentos entre pacu e tambaqui; também é híbrida a espécie conhecida como surubim ou pintado, piscívoro de grande porte.",
    "Em alguns julgamentos de crimes ambientais, as sentenças, de modo geral, condenam empresas culpadas pela redução da qualidade de cursos d’água a realizarem peixamentos. Em geral, os peixamentos tendem a ser repetidos muitas vezes numa mesma área.",
    "A respeito da realização de peixamentos pelas empresas infratoras, pode-se considerar que essa penalidade"),
  tags=["peixamento", "qualidade da água"])

X(50, "H", "História", "Cultura brasileira", "<p>Os viajantes descrevem o hábito de comer com as mãos, aprendido com os indígenas e difundido entre portugueses e brasileiros de todas as classes: uma fusão de elementos culturais diferentes, o sincretismo. Alternativa <strong>E</strong>.</p><p>O hábito estava em todo o Brasil, e não em uma região (A), e os autores o descrevem com curiosidade, sem intolerância ou racismo (B, D).</p>",
  ap("Comer com as mãos era um hábito comum na Europa, no século XVI. A técnica empregada pelo índio no Brasil e por um português de Portugal era, aliás, a mesma: apanhavam o alimento com três dedos da mão direita (polegar, indicador e médio) e atiravam-no para dentro da boca.",
     "Um viajante europeu de nome Freireyss, de passagem pelo Rio de Janeiro, já no século XIX, conta como “nas casas das roças despejam-se simplesmente alguns pratos de farinha sobre a mesa ou num balainho, donde cada um se serve com os dedos, arremessando, com um movimento rápido, a farinha na boca, sem que a mínima parcela caia para fora”. Outros viajantes oitocentistas, como John Luccock, Carl Seidler, Tollenare e Maria Graham descrevem esse hábito em todo o Brasil e entre todas as classes sociais. Mas para Saint-Hilaire, os brasileiros “lançam a [farinha de mandioca] à boca com uma destreza adquirida, na origem, dos indígenas, e que ao europeu muito custa imitar”.",
     "Aluísio de Azevedo, em seu romance <em>Girândola de amores</em> (1882), descreve com realismo os hábitos de uma senhora abastada que só saboreava a moqueca de peixe “sem talher, à mão”.")
  + p("Dentre as palavras listadas abaixo, assinale a que traduz o elemento comum às descrições das práticas alimentares dos brasileiros feitas pelos diferentes autores do século XIX citados no texto."),
  tags=["sincretismo", "hábitos alimentares"])

X(51, "N", "Física", "Fases da Lua", "<p>A lua mais iluminada e que fica mais tempo no céu à noite é a cheia, que nasce ao pôr do sol e se põe ao amanhecer, e a gibosa próxima dela. Pela sequência de fases da figura, a lua cheia cai em 2 de outubro; o fim de semana de 29 e 30 de setembro, logo antes, tem a lua quase cheia iluminando a maior parte da noite. Alternativa <strong>D</strong>.</p><p>Por volta de 17 de setembro (B) é lua nova, sem luz à noite.</p>",
  p("Um grupo de pescadores pretende passar um final de semana do mês de setembro, embarcado, pescando em um rio. Uma das exigências do grupo é que, no final de semana a ser escolhido, as noites estejam iluminadas pela lua o maior tempo possível.", "A figura representa as fases da lua no período proposto.")
  + "[[fig:1]]"
  + p("Considerando-se as características de cada uma das fases da lua e o comportamento desta no período delimitado, pode-se afirmar que, dentre os fins de semana, o que melhor atenderia às exigências dos pescadores corresponde aos dias"),
  figs(("q51a", "Esquema da órbita da Lua em torno da Terra com quatro posições e as datas: 10 de setembro (embaixo), 17 de setembro (à direita), 24 de setembro (em cima) e 02 de outubro (à esquerda), com a Lua de lados iluminados diferentes em cada posição.")),
  ["fases da Lua"])

X(52, "N", "Biologia", "Origem da vida", "<p>O “avanço criativo” é o momento em que ácidos nucleicos passam a orientar a síntese de proteínas que os copiam, antes das primeiras células. No esquema, os primeiros ácidos nucleicos surgem antes de 4 bilhões de anos e as primeiras células, entre 4 e 3 bilhões de anos: o intervalo é de 4,5 a 3,5 bilhões. Alternativa <strong>B</strong>.</p><p>A fotossíntese e a respiração aeróbia (C, D) vêm depois.</p>",
  ap("Na solução aquosa das substâncias orgânicas prebióticas (antes da vida), a catálise produziu a síntese de moléculas complexas de toda classe, inclusive proteínas e ácidos nucléicos. A natureza dos catalisadores primitivos que agiam antes não é conhecida. É quase certo que as argilas desempenharam papel importante: cadeias de aminoácidos podem ser produzidas no tubo de ensaio mediante a presença de certos tipos de argila. (...) Mas o avanço verdadeiramente criativo – que pode, na realidade, ter ocorrido apenas uma vez – ocorreu quando uma molécula de ácido nucléico “aprendeu” a orientar a reunião de uma proteína, que, por sua vez, ajudou a copiar o próprio ácido nucléico. Em outros termos, um ácido nucléico serviu como modelo para a reunião de uma enzima que poderia então auxiliar na produção de mais ácido nucléico. Com este desenvolvimento apareceu o primeiro mecanismo potente de realização. A vida tinha começado.")
  + fonte("Adaptado de: LURIA, S.E. <em>Vida: experiência inacabada</em>. Belo Horizonte: Editora Itatiaia; São Paulo: EDUSP, 1979.")
  + p("Considere o esquema:") + "[[fig:1]]"
  + fonte("Adaptado de GEPEQ – Grupo de Pesquisa em Educação Química. USP – <em>Interações e Transformações III</em>. São Paulo: EDUSP, 1998.")
  + p("O “avanço verdadeiramente criativo” citado no texto deve ter ocorrido no período (em bilhões de anos) compreendido aproximadamente entre"),
  figs(("q52a", "Escala de tempo de 5 bilhões de anos até hoje, com eventos importantes: formação da Terra e primeiros ácidos nucleicos (entre 5 e 4 bilhões); primeiras células (entre 4 e 3 bilhões); fotossíntese e produção de oxigênio nas células (entre 3 e 2 bilhões); respiração aeróbia e consumo de oxigênio nas células (entre 2 e 1 bilhão); plantas, répteis, pássaros e peixes (entre 1 e 0,5 bilhão); seres humanos (perto da atualidade).")),
  ["ácidos nucleicos", "tempo geológico"])

X(53, "H", "História", "Era Vargas", "<p>A marchinha mostra a chegada da modernidade ao morro (a luz elétrica da Light no lugar do lampião, as palavras em inglês), mas o cenário continua sendo a favela, onde a desigualdade permanece. Alternativa <strong>B</strong>.</p><p>A canção não fala de racionamento (A) nem afirma que a exclusão acabou (C).</p>",
  tit("Good-bye") + "[[fig:1]]"
  + p("A marchinha <em>Good-bye</em>, composta por Assis Valente há cerca de 50 anos, refere-se ao ambiente das favelas dos morros cariocas. A estrofe citada mostra"),
  figs(("q53", "Estrofe da marchinha “Good-bye”, de Assis Valente: no morro já não se diz boa noite nem bom dia, só good morning e good night; o lampião de querosene foi desprezado e só se usa a luz da Light; “Oh yes!”.")),
  ["anglicismos", "modernização"])

X(54, "H", "Sociologia", "Violência", "<p>I é verdadeira: há agressores da família em todas as faixas. III também: as adolescentes foram vítimas de quase todos os tipos de agressor. IV também: pai biológico (21,7%), padrasto (16,7%) e pai adotivo (1,6%) somam 40% dos casos com crianças, mais de 1/3. II é falsa: os principais agressores das adultas são vizinhos, parceiros e outros conhecidos. Alternativa <strong>D</strong>.</p>",
  p("A tabela refere-se a um estudo realizado entre 1994 e 1999 sobre violência sexual com pessoas do sexo feminino no Brasil.") + "[[fig:1]]"
  + p("A partir dos dados da tabela e para o grupo feminino estudado, são feitas as seguintes afirmações:")
  + '<ol type="I"><li>A mulher não é poupada da violência sexual doméstica em nenhuma das faixas etárias indicadas.</li><li>A maior parte das mulheres adultas é agredida por parentes consangüíneos.</li><li>As adolescentes são vítimas de quase todos os tipos de agressores.</li><li>Os pais, biológicos, adotivos e padrastos, são autores de mais de 1/3 dos casos de violência sexual envolvendo crianças.</li></ol>'
  + p("É verdadeiro apenas o que se afirma em"),
  figs(("q54a", "Tabela “Levantamento dos casos de violência sexual por faixa etária”, com quantidade e porcentagem por tipo de agressor. Crianças (60 casos): pai biológico 13 (21,7%), padrasto 10 (16,7%), pai adotivo 1 (1,6%), tio 7 (11,6%), avô 6 (10%), vizinho 10 (16,7%), outro conhecido 13 (21,7%). Adolescentes (151): pai biológico 21 (13,9%), padrasto 16 (10,6%), tio 14 (9,4%), irmão 7 (4,6%), primo 5 (3,4%), vizinho 42 (27,8%), parceiro e ex-parceiro 13 (7,5%), conhecido do trabalho 8 (5,3%), outro conhecido 25 (16,5%). Adultas (68): pai biológico 6 (6%), tio 1 (1,4%), avô 1 (1,4%), primo 1 (1,4%), vizinho 19 (27,9%), parceiro e ex-parceiro 17 (25,2%), conhecido do trabalho 5 (7,3%), outro conhecido 18 (26,5%). Fonte: Jornal da Unicamp, nº 162, maio de 2001.")),
  ["violência sexual", "leitura de tabela"])

X(55, "M", "Matemática", "Circunferência", "<p>Pontos diametralmente opostos no Equador estão separados por meia circunferência: π × 6.370 ≈ 20.000 km. A 800 km/h, o voo leva 20.000/800 = 25 horas. Alternativa <strong>C</strong>.</p><p>Usar o diâmetro em linha reta (12.740 km) daria cerca de 16 horas (A), mas o avião não atravessa a Terra.</p>",
  p("As cidades de Quito e Cingapura encontram-se próximas à linha do equador e em pontos diametralmente opostos no globo terrestre. Considerando o raio da Terra igual a 6370 km, pode-se afirmar que um avião saindo de Quito, voando em média 800 km/h, descontando as paradas de escala, chega a Cingapura em aproximadamente"),
  tags=["comprimento da circunferência", "velocidade"])

X(56, "L", "Língua Portuguesa", "Preposições", "<p>“Menino de rua” usa “de” como característica, quase um rótulo (qualidade). “Menino na rua” usa “em”, que indica só o lugar onde ele está, posto lá por alguém. A troca muda a relação para localização, e não qualidade. Alternativa <strong>A</strong>.</p><p>O texto não trata de posse nem de origem.</p>",
  p("A crônica muitas vezes constitui um espaço para reflexão sobre aspectos da sociedade em que vivemos.")
  + ap("“Eu, na rua, com pressa, e o menino segurou no meu braço, falou qualquer coisa que não entendi. Fui logo dizendo que não tinha, certa de que ele estava pedindo dinheiro. Não estava. Queria saber a hora.",
       "Talvez não fosse um Menino De Família, mas também não era um Menino De Rua. É assim que a gente divide. Menino De Família é aquele bem-vestido com tênis da moda e camiseta de marca, que usa relógio e a mãe dá outro se o dele for roubado por um Menino De Rua. Menino De Rua é aquele que quando a gente passa perto segura a bolsa com força porque pensa que ele é pivete, trombadinha, ladrão. (...)",
       "Na verdade não existem meninos De rua. Existem meninos NA rua. E toda vez que um menino está NA rua é porque alguém o botou lá. Os meninos não vão sozinhos aos lugares. Assim como são postos no mundo, durante muitos anos também são postos onde quer que estejam. Resta ver quem os põe na rua. E por quê.”")
  + fonte("COLASSANTI, Marina. In: <em>Eu sei, mas não devia</em>. Rio de Janeiro: Rocco, 1999.")
  + p("No terceiro parágrafo em “... não existem meninos De rua. Existem meninos NA rua.”, a troca de De pelo Na determina que a relação de sentido entre “menino” e “rua” seja"),
  tags=["Marina Colasanti", "preposições"])

X(57, "N", "Biologia", "Biogeografia", "<p>O mapa mostra o puma da Patagônia ao Canadá, passando por climas frios, temperados e tropicais e por florestas, campos e desertos. Isso indica tolerância a climas diversos (III) e ocupação de vários tipos de vegetação (IV). Alternativa <strong>C</strong>.</p><p>A distribuição não informa nada sobre resistência a doenças (I) ou domesticação (II).</p>",
  p("O <em>Puma concolor</em> (suçuarana, puma, leão da montanha) é o maior felino das Américas, com uma distribuição biogeográfica que se estende da Patagônia ao Canadá.") + "[[fig:1]]"
  + p("O padrão de distribuição mostrado na figura está associado a possíveis características desse felino:")
  + '<ol type="I"><li>É muito resistente a doenças.</li><li>É facilmente domesticável e criado em cativeiro.</li><li>É tolerante a condições climáticas diversas.</li><li>Ocupa diversos tipos de formações vegetais.</li></ol>'
  + p("Características desse felino compatíveis com sua distribuição biogeográfica estão evidenciadas apenas em"),
  figs(("q57a", "Mapa das Américas com a distribuição do Puma concolor em preto: oeste do Canadá e dos Estados Unidos, México, América Central e quase toda a América do Sul, até a Patagônia.")),
  ["puma", "distribuição geográfica"])

X(58, "H", "Filosofia", "Relativismo cultural", "<p>Montaigne diz que “cada qual considera bárbaro o que não se pratica em sua terra” e que os europeus, que esquartejam e queimam por motivos religiosos, superam os indígenas em barbaridade. A diferença de costumes não é critério válido para julgar uma sociedade inferior. Alternativa <strong>B</strong>.</p><p>Ele não diz que os indígenas são mais bárbaros (C) nem que os costumes sejam iguais (E).</p>",
  p("Michel Eyquem de Montaigne (1533-1592) compara, nos trechos, as guerras das sociedades Tupinambá com as chamadas “guerras de religião” dos franceses que, na segunda metade do século XVI, opunham católicos e protestantes.")
  + ap("“(…) não vejo nada de bárbaro ou selvagem no que dizem daqueles povos; e, na verdade, cada qual considera bárbaro o que não se pratica em sua terra. (…) Não me parece excessivo julgar bárbaros tais atos de crueldade [o canibalismo], mas que o fato de condenar tais defeitos não nos leve à cegueira acerca dos nossos. Estimo que é mais bárbaro comer um homem vivo do que o comer depois de morto; e é pior esquartejar um homem entre suplícios e tormentos e o queimar aos poucos, ou entregá-lo a cães e porcos, a pretexto de devoção e fé, como não somente o lemos mas vimos ocorrer entre vizinhos nossos conterrâneos; e isso em verdade é bem mais grave do que assar e comer um homem previamente executado. (…) Podemos portanto qualificar esses povos como bárbaros em dando apenas ouvidos à inteligência, mas nunca se compararmos a nós mesmos, que os excedemos em toda sorte de barbaridades.”")
  + fonte("MONTAIGNE, Michel Eyquem de. <em>Ensaios</em>. São Paulo: Nova Cultural, 1984.")
  + p("De acordo com o texto, pode-se afirmar que, para Montaigne,"),
  tags=["Montaigne", "Tupinambá"])

X(59, "N", "Física", "Estados físicos", "<p>A temperatura média de Marte, −55 °C, está muito abaixo do ponto de congelamento da água: nessas condições, a água fica no estado sólido, e não líquido. Alternativa <strong>E</strong>.</p><p>A distância ao Sol (A) influencia a temperatura, mas o fator diretamente adverso à água líquida é o frio; massa, gravidade e CO2 (B, C, D) não impedem por si a água líquida.</p>",
  p("Nas discussões sobre a existência de vida fora da Terra, Marte tem sido um forte candidato a hospedar vida. No entanto, há ainda uma enorme variação de critérios e considerações sobre a habitabilidade de Marte, especialmente no que diz respeito à existência ou não de água líquida. Alguns dados comparativos entre a Terra e Marte estão apresentados na tabela.")
  + tabela(["", "Terra", "Marte"], [["Distância ao Sol (km)", "149 milhões", "228 milhões"], ["Massa (em relação à terrestre)", "1,00", "0,18"], ["Aceleração da gravidade (m/s²)", "9,8", "3,7"],
           ["Composição da atmosfera", "Gases predominantes: nitrogênio (N) e oxigênio (O2)", "Gás predominante: dióxido de carbono (CO2)"], ["Temperatura média", "288 K (+15 °C)", "218 K (−55 °C)"]])
  + p("Com base nesses dados, é possível afirmar que, dentre os fatores abaixo, aquele mais adverso à existência de água líquida em Marte é sua"),
  tags=["Marte", "água líquida"], quim=True, alts=dict(D[59], D="atmosfera rica em CO2.", E="temperatura média muito baixa."))

ATM = (tit("Texto para as questões 60 e 61.") + p("As áreas numeradas no gráfico mostram a composição em volume, aproximada, dos gases na atmosfera terrestre, desde a sua formação até os dias atuais.") + "[[fig:1]]"
  + fonte("Adaptado de <em>The Random House Encyclopedias</em>, 3ª ed., 1990."))
F_ATM = figs(("q60", "Gráfico de áreas da composição da atmosfera (%) de 5 bilhões de anos atrás até hoje: (I) metano e hidrogênio, só no início; (II) vapor d’água, logo depois; (III) amônia, pequena faixa inicial; (IV) nitrogênio, que cresce a partir de cerca de 4 bilhões de anos e chega a cerca de 78%; (V) gás carbônico, que domina por volta de 4 bilhões de anos e depois diminui muito; (VI) oxigênio, que surge por volta de 2,9 bilhões de anos e cresce até cerca de 21% hoje, com cerca de 5% há 2,5 bilhões de anos."))
X(60, "N", "Biologia", "Evolução da atmosfera", "<p>Pelo gráfico, o oxigênio (VI) só aparece por volta de 2,9 bilhões de anos: antes disso não há como existirem seres aeróbicos (I). Florestas há 3,5 bilhões de anos (II) e seres humanos há 2,5 bilhões (III) não são compatíveis com a composição atmosférica da época, quase sem oxigênio. Alternativa <strong>A</strong>.</p>",
  ATM + p("Considerando apenas a composição atmosférica, isolando outros fatores, pode-se afirmar que:")
  + I3("não podem ser detectados fósseis de seres aeróbicos anteriores a 2,9 bilhões de anos.", "as grandes florestas poderiam ter existido há aproximadamente 3,5 bilhões de anos.", "o ser humano poderia existir há aproximadamente 2,5 bilhões de anos.")
  + p("É correto o que se afirma em"),
  F_ATM, ["atmosfera primitiva", "oxigênio"])
X(61, "N", "Biologia", "Evolução da atmosfera", "<p>No gráfico, há 2,5 bilhões de anos a área do oxigênio (VI) ainda é estreita, com cerca de 5% do volume. Alternativa <strong>E</strong>.</p><p>21% (D) é a proporção atual, e 77% (B) corresponde ao nitrogênio.</p>",
  ATM + p("No que se refere à composição em volume da atmosfera terrestre há 2,5 bilhões de anos, pode-se afirmar que o volume de oxigênio, em valores percentuais, era de, aproximadamente,"),
  F_ATM, ["atmosfera primitiva", "leitura de gráfico"])

X(62, "H", "Geografia", "Fontes de energia", "<p>A Idade da Pedra não acabou por falta de pedras, mas porque surgiram técnicas e materiais melhores (os metais). Do mesmo modo, para Yamani, a era do petróleo acabará pelo desenvolvimento tecnológico e por novas fontes de energia. Alternativa <strong>B</strong>.</p><p>A frase diz expressamente que o fim não virá por falta de petróleo (A).</p>",
  ap("“A idade da pedra chegou ao fim, não porque faltassem pedras; a era do petróleo chegará igualmente ao fim, mas não por falta de petróleo”.")
  + fonte("Xeque Yamani, Ex-ministro do Petróleo da Arábia Saudita. <em>O Estado de S. Paulo</em>, 20/08/2001.")
  + p("Considerando as características que envolvem a utilização das matérias-primas citadas no texto em diferentes contextos histórico-geográficos, é correto afirmar que, de acordo com o autor, a exemplo do que aconteceu na Idade da Pedra, o fim da era do Petróleo estaria relacionado"),
  tags=["petróleo", "inovação tecnológica"])

X(63, "H", "Sociologia", "Etnocentrismo", "<p>Hagar divide o mundo em “navegantes e não-navegantes” e, perguntado sobre quem fez essa divisão, responde: “com os navegantes!”. Ele impõe o ponto de vista do seu grupo como única explicação, desvalorizando a diversidade. Alternativa <strong>B</strong>.</p><p>Ele não considera o mundo habitado apenas por navegantes (E): reconhece os não-navegantes, mas pelo critério do seu grupo.</p>",
  "[[fig:1]]" + p("De acordo com a história em quadrinhos protagonizada por Hagar e seu filho Hamlet, pode-se afirmar que a postura de Hagar"),
  figs(("q63a", "Tira de Hagar, de Dik Browne, em três quadros. Hagar diz ao filho: “Hamlet, existem apenas dois tipos de pessoas neste mundo...”; depois: “Navegantes e não-navegantes!”. Hamlet pergunta: “De acordo com quem, papai?”, e Hagar responde, de braços cruzados: “Com os navegantes!”")),
  ["Hagar", "etnocentrismo"])

Q.setdefault(52, {})["alternativas"] = {'A': '5,0 e 4,5.', 'B': '4,5 e 3,5.', 'C': '3,5 e 2,0.', 'D': '2,0 e 1,5.', 'E': '1,0 e 0,5.'}  # texto vizinho grudava na alternativa E
completar(Q, R)
