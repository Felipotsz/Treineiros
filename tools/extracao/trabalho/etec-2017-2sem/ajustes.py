# Ajustes da conferência humana: Vestibulinho ETEC 2º semestre de 2017 (exame de 11/06/2017)
# Texto conferido com a imagem de cada página; caixas de texto via trecho(). Tema: diversão.
# Gabarito: oficial RETIFICADO (2º SEM/17), com Q30 e Q31 ANULADAS. Não achamos o motivo oficial:
# a justificativa é análise do Treineiros (as duas questões mandam observar uma imagem da Tabela que não está na prova).
# A marchinha de 1950 (Q12) fica como imagem; a cantiga de roda (Q10), de domínio público, fica como texto.
import re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import A, carregar, enun, tabela, colunas, completar, trecho

ID = "etec-2017-2sem"
META = {
    "id": ID,
    "banca": "ETEC",
    "ano": 2017,
    "semestre": 2,
    "titulo": "Vestibulinho ETEC, 2º semestre de 2017",
    "fonte": "Centro Paula Souza",
    "dataExame": "2017-06-11",
    "duracaoMinutos": 240,
    "tema": "Diversão",
    "apresentacao": "<p>Prezado(a) candidato(a), nesta prova, você terá contato com diversas formas de diversão e sua relação com as áreas do conhecimento. Matemática e Geografia, por exemplo, estão presentes em jogos de tabuleiro. Linguagens, História e Ciências, em filmes. Assim como você pode se divertir de várias maneiras, também pode se divertir enquanto aprende.</p><p>Boa prova e divirta-se!</p>",
    "pdf": f"assets/provas/{ID}.pdf",
}
EXTRAS = {"apresentacao": "Ícones de pessoas se divertindo: uma família, um banco de praça, uma pipa, alguém passeando com o cachorro, uma criança com balão, pessoas jogando à mesa, alguém de bicicleta, uma criança correndo e outra no balanço."}

R = carregar(ID)
PAG_DM = 18


def T(pag, inicio, fim, paragrafos=()):
    return trecho(ID, pag, inicio, fim, paragrafos)


def p(*paragrafos, classe=None):
    abre = f'<p class="{classe}">' if classe else "<p>"
    return "".join(abre + x + "</p>" for x in paragrafos)


def apoio(*paragrafos):
    return '<p class="apoio">' + A.join(paragrafos) + "</p>"


def fonte(t):
    return f'<p class="fonte">{t}</p>'


def url(u, data, extra="Adaptado."):
    return fonte(f"&lt;{u}&gt; Acesso em: {data}." + (" " + extra if extra else ""))


def chamada(t):
    return f'<p class="chamada">{t}</p>'


def it(texto, *termos):
    for t in termos: texto = texto.replace(t, f"<em>{t}</em>")
    return texto


def figs_alt(primeira=1):
    return {l: f"[[fig:{primeira + i}]]" for i, l in enumerate("ABCDE")}


ANULADA_30_31 = ("O enunciado manda “observar a imagem” do jogo, mas a prova não traz nenhuma figura da Tabela Periódica usada pelos alumos. "
                 "Sem ela, as regras de deslocamento do jogo (casas, direções) não podem ser conferidas, e por isso as questões 30 e 31 foram anuladas. "
                 "O Centro Paula Souza não publicou o motivo; esta é a análise do Treineiros.").replace("alumos", "alunos")

# ---------- textos compartilhados ----------
PIADAS = (chamada("Leia o texto, que brinca com dois conceitos químicos, para responder às questões de números 02 e 03.")
          + apoio("• Por que tomar água no meio da aula prejudica o aprendizado?<br>Resposta: Porque ela diminui a concentração.",
                  "• Um nêutron entra num bar e pergunta: – Qual o valor da bebida?<br>O garçom responde: – Pra você? É zero!"))
P2 = p("A ideia química, no primeiro exemplo se refere ao conceito de")

CARTUM = (chamada("Leia o cartum e responda às questões de números 04 e 05.") + "[[fig:1]]" + url("https://tinyurl.com/jbakwyq", "10.02.2017", ""))
CARTUM_IMG = {"arquivo": "q04", "alt": "Cartum de A. J. Talber. Um aluno lê uma folha diante do quadro, onde está escrito “Aula de hoje: redação. Tema: a situação mais apavorante da sua vida”. No alto, o texto dele: “Tudo começou quando acordei e descobri que meu computador estava sem conexão com a internet e meu celular com o sinal fraco. Subi no telhado, e ao conseguir sinal pro celular, a bateria descarregou. O mesmo ocorreu com o celular do meu pai, da minha mãe, e da minha irmã. Quando fui recarregar a bateria, faltou energia elétrica, e então, sobreveio o pavor absoluto…”"}
P4 = p("O cartum lido trata de maneira cômica o problema vivenciado por um aluno.", "O humor está baseado no fato de o aluno")

ROSARIO = (chamada("Leia o texto e observe a imagem para responder às questões de números 06 e 07.")
           + apoio(T(4, "Segundo a historiadora Laura de Mello e Souza", "como se vê na imagem.")[0]) + "[[fig:1]]"
           + url("https://tinyurl.com/htna9r4", "09.02.2017", ""))
ROSARIO_IMG = {"arquivo": "q06", "alt": "Gravura de Rugendas: uma grande multidão de pessoas negras em festa ao ar livre, com bandeiras, tambores e dançarinos, cercando um casal coroado; à esquerda, homens a cavalo observam.", "legenda": "Festa de Nossa Senhora do Rosário, padroeira dos negros. Rugendas, c. 1835."}
P6 = p("Sobre o ato representado na imagem, é correto afirmar que se trata")

DIVERTIDA = (chamada("Leia o texto e responda às questões de números 40 e 41.")
             + apoio(*[it(x, "Toy Story", "Procurando Nemo", "Divertida Mente") for x in
                       T(18, "Ao longo dos anos, um estúdio", "jamais seja citado nominalmente no", ["A história gira em torno", "Há muito de psicologia"])[:-1]],
                     it(T(18, "Há muito de psicologia", "jamais seja citado nominalmente no")[0] + " " + T(PAG_DM, "longa-metragem, ele é claramente", "às vezes é necessário.")[0], "Divertida Mente"))
             + url("http://tinyurl.com/gvsksp3", "25.01.2017"))
P40 = p("De acordo com o texto, é correto afirmar que")

TANGRAM = (chamada("Leia o texto para responder às questões 34 e 35.")
           + apoio(*T(16, "O Tangram é um quebra-cabeça chinês", "própria dos mitos e lendas.", ["Lendas e histórias"]))
           + url("https://tinyurl.com/htszezr", "03.03.2017") + "[[fig:1]]"
           + url("https://tinyurl.com/gngjyue", "03.03.2017", "Original colorido."))
TANGRAM_IMG = {"arquivo": "q34", "alt": "Nove figuras montadas com as peças do Tangram: aves, um barco, pessoas e animais, cada uma formada por triângulos, um quadrado e um paralelogramo."}
P34 = p("A partir das informações do texto, as peças do Tangram são")

JOGO = (chamada("Leia o texto e observe a imagem para responder às questões de números 30 e 31.")
        + apoio(*T(14, "Em uma aula de Química", "uma peça colorida.", ["Grupos de quatro"]),
                "Algumas das regras do jogo são:",
                "• Para mover sua peça o aluno joga um dado e o número obtido é a quantidade de casas (elementos), que ele deve se deslocar na Tabela.<br>"
                "• O aluno só pode deslocar sua peça em uma única direção, vertical ou horizontal (a cada jogada).<br>"
                "• Vence o jogo quem chega com a sua peça no elemento químico de número atômico 118."))
P30 = p("Se o professor desse o comando: “Coloquem suas peças sobre os gases nobres”, os alunos deveriam colocá-las sobre elementos cujo grupo (ou família) na Tabela Periódica é identificado pelo número")

INTERNET = (chamada("Leia o texto e responda às questões de números 49 e 50.")
            + apoio(*[re.sub(r"\b(Facebook|Twitter|Whatsapp)\b", r"<em>\1</em>", x) for x in
                      T(22, "A internet é uma ferramenta", "procurar ajuda profissional.",
                        ["A funcionária pública Nicole", "Ela diz que, no trabalho", "Já a professora Fernanda", "A psicóloga Miriam", "A especialista conclui"])])
            + url("https://tinyurl.com/gw57v7l", "10.02.2017"))
P49 = p("De acordo com o texto, é possível afirmar corretamente que")

Q = {
1: {"materia": "Geografia", "assunto": "Hidrografia", "tags": ["rio Tietê"],
    "enunciado": p("Um dos grandes divertimentos na cidade de São Paulo, no início do século XX, era acompanhar as grandes regatas que aconteciam no rio Tietê.",
                   "Disputas de natação também ocorriam nesse rio, além das tradicionais pescarias em suas margens.")
                 + "[[fig:1]]" + url("https://tinyurl.com/k3k67v8", "13.02.2017", "") + p("Esse rio"),
    "imagens": [{"arquivo": "q01", "alt": "Foto antiga, em preto e branco, de barcos de remo no rio Tietê, com pessoas assistindo das margens e uma ponte e prédios ao fundo."}],
    "explicacao": "<p>O Tietê <strong>nasce na Serra do Mar</strong>, em Salesópolis, a poucos quilômetros do litoral, mas corre <strong>para o interior</strong>, atravessa o estado de São Paulo e <strong>deságua no rio Paraná</strong>. Alternativa <strong>B</strong>.</p><p>Ele não nasce na capital nem deságua em Santos (A). Não é afluente do rio Grande nem chega ao Pacífico (C). O Pinheiros é que é afluente do Tietê, e o Tietê não vai para o Vale do Paraíba (D). E o Piracicaba é afluente do Tietê, não o contrário (E).</p>"},
2: {"materia": "Química", "assunto": "Substâncias e misturas", "tags": ["concentração"],
    "enunciado": PIADAS + P2,
    "explicacao": "<p>A piada joga com dois sentidos de “concentração”: a atenção do aluno e a concentração de uma solução. Ao acrescentar água, a solução fica mais <strong>diluída</strong>, isto é, sua concentração diminui. Alternativa <strong>A</strong>.</p><p>Dissolução é o ato de dissolver um soluto (B). Evaporação aumentaria a concentração (C). E destilação e separação de misturas não se relacionam com a piada (D e E).</p>"},
3: {"materia": "Química", "assunto": "Estrutura atômica",
    "enunciado": p("No segundo exemplo, o valor da bebida faz analogia"), "apoio_de": (2, P2),
    "explicacao": "<p>O nêutron não tem carga elétrica: sua <strong>carga é zero</strong>. O garçom diz que, para ele, o valor “é zero”. Alternativa <strong>A</strong>.</p><p>A massa do nêutron não é zero; vale cerca de 1 u (B e D). Nêutron não é molécula (C). E ele não ocupa grupo na tabela periódica, que organiza elementos (E).</p>"},
4: {"materia": "Português", "assunto": "Interpretação de texto", "tags": ["cartum"],
    "enunciado": CARTUM + P4, "imagens": [CARTUM_IMG],
    "explicacao": "<p>O tema da redação é “a situação mais apavorante da sua vida”, e o aluno escreve sobre ficar sem internet, sem celular e sem energia. O humor está em <strong>tratar como apavorante ficar sem acesso a dispositivos tecnológicos</strong>. Alternativa <strong>D</strong>.</p><p>Ele entendeu o tema (A). Usou o celular dos familiares, que também descarregou (B). Não consertou o computador (C). E a falta de energia é parte da história, não o motivo de não terminar a redação (E).</p>"},
5: {"materia": "Português", "assunto": "Verbos", "tags": ["sujeito oculto"],
    "enunciado": p("Releia os períodos retirados do cartum.")
                 + apoio("\"[...] quando <strong>acordei</strong> e <strong>descobri</strong> que meu computador estava sem conexão com a internet [...]”")
                 + p("Ao analisarmos esses períodos, percebemos que o sujeito correspondente às formas verbais destacadas é oculto (ou desinencial), pois"),
    "apoio_de": (4, P4),
    "explicacao": "<p>Em “acordei” e “descobri”, o sujeito “eu” não aparece escrito, mas é <strong>indicado pela desinência verbal</strong> “-ei”/“-i”, da 1ª pessoa do singular. Alternativa <strong>E</strong>.</p><p>Os verbos não são impessoais (A). O sujeito não está exposto na frase, nem com um nem com vários núcleos (B e C). E os verbos estão na 1ª pessoa do singular (D).</p>"},
6: {"materia": "História", "assunto": "Brasil Colônia", "tags": ["Congada", "cultura afro-brasileira"],
    "enunciado": ROSARIO + P6, "imagens": [ROSARIO_IMG],
    "explicacao": "<p>A coroação de um rei e uma rainha negros, junto às festas católicas de Nossa Senhora do Rosário e ao som de tambores, é a <strong>Congada</strong>, que saudava o rei e a rainha do Congo. Alternativa <strong>C</strong>.</p><p>O maracatu é pernambucano, e a sociedade mineradora não era próspera para todos (A). O carnaval com rei Momo é muito posterior (B). A lavagem das escadarias é a festa do Bonfim, em Salvador (D). E a Folia de Reis acontece depois do Natal, com cantoria (E).</p>"},
7: {"materia": "História", "assunto": "Brasil Colônia", "tags": ["mineração", "barroco"],
    "enunciado": p("É correto afirmar que no século XVIII, a mineração"), "apoio_de": (6, P6),
    "explicacao": "<p>A riqueza do ouro em Minas Gerais financiou igrejas, esculturas e festas religiosas: é o <strong>barroco mineiro</strong>, de artistas como Aleijadinho. Alternativa <strong>E</strong>.</p><p>A mineração foi em Minas, Goiás e Mato Grosso, não no Pará, e a pobreza continuou (A). A Lei Áurea, de 1888, não tem relação com o ouro (B). A capital passou de Salvador para o Rio de Janeiro, não para Cuiabá (C). E o Nordeste colonial se estruturou no açúcar (D).</p>"},
8: {"materia": "Química", "assunto": "Substâncias e misturas", "tags": ["estados físicos"],
    "enunciado": enun(R, 8, figs={"p05-1": 1}).replace('<p>Na imagem temos', fonte("&lt;https://tinyurl.com/l9ml95o&gt; Acesso em 10.02.2017. Original colorido.") + '<p>Na imagem temos'),
    "imagens": [{"arquivo": "q08", "alt": "Ilustração de uma bateria e outros instrumentos musicais montados com vidrarias de laboratório, como balões, tubos de ensaio e suportes. Notas musicais saem do alto de um dos frascos, como um gás escapando."}],
    "explicacao": "<p>Em temperatura ambiente, o <strong>dióxido de carbono</strong> (CO<sub>2</sub>) é um gás e escaparia de um recipiente aberto, como as notas musicais da figura. Alternativa <strong>A</strong>.</p><p>Hidróxido de sódio, cloreto de sódio, dióxido de silício (areia) e zinco são sólidos à temperatura ambiente (B, C, D e E).</p>"},
9: {"materia": "Matemática", "assunto": "Razão e proporção", "tags": ["frações"],
    "enunciado": p("Numa partitura musical, figuras rítmicas são símbolos utilizados para representar a duração de cada nota ou acorde.",
                   "A tabela mostra o nome da figura rítmica, seu símbolo e o tempo de duração relativo.") + "[[fig:1]]"
                 + p("De acordo com a tabela, é correto afirmar que"),
    "imagens": [{"arquivo": "q09", "alt": "Tabela com o nome da figura rítmica, seu símbolo musical e o tempo de duração relativo: semibreve, 1; mínima, 1/2; semínima, 1/4; colcheia, 1/8; semicolcheia, 1/16; fusa, 1/32; semifusa, 1/64."}],
    "explicacao": "<p>Os tempos são 1, 1/2, 1/4, 1/8, 1/16, 1/32 e 1/64: a partir da mínima, cada figura dura <strong>metade da figura da linha anterior</strong>. Alternativa <strong>D</strong>.</p><p>A fusa (1/32) é metade da semicolcheia (1/16), não o dobro (A). A mínima (1/2) é o dobro da semínima (1/4) (B). Duas semínimas somam 1/2, que é uma mínima, não uma colcheia (C). E E inverte a relação.</p>"},
10: {"materia": "Português", "assunto": "Figuras de linguagem", "tags": ["anáfora"],
     "enunciado": p("Leia a cantiga de roda.")
                  + apoio("Se esta rua,<br>se esta rua fosse minha<br>eu mandava,<br>eu mandava ladrilhar<br>com pedrinhas,<br>com pedrinhas de brilhantes<br>para o meu,<br>para o meu amor passar.",
                          "Nesta rua,<br>nesta rua tem um bosque<br>que se chama,<br>que se chama solidão<br>dentro dele,<br>dentro dele mora um anjo<br>que roubou,<br>que roubou meu coração.",
                          "Se eu roubei,<br>se eu roubei teu coração<br>tu roubaste,<br>tu roubaste o meu também<br>se eu roubei,<br>se eu roubei teu coração<br>é porque,<br>é porque te quero bem.")
                  + url("http://tinyurl.com/hvt5m96", "25.01.2017", "")
                  + p("Na cantiga, há a presença de uma figura de linguagem de construção denominada anáfora.", "Assinale a alternativa que apresenta outro exemplo dessa mesma figura de linguagem."),
     "explicacao": "<p>Anáfora é a <strong>repetição de palavras no início</strong> de versos ou frases seguidas. Em “<strong>Passou um tempo.</strong> <strong>Passou um tempo.</strong> <strong>Passou um tempo</strong> desde que te vi.”, a mesma expressão abre as três frases. Alternativa <strong>E</strong>.</p><p>A é uma frase comum, sem repetição. B é uma comparação. C é uma personificação (as flores “dançam”). E D não repete termos no início das frases.</p>"},
11: {"materia": "História", "assunto": "História contemporânea", "tags": ["contracultura"],
     "explicacao": "<p>A contracultura dos anos 1960 contestou valores tradicionais (consumismo, guerra, costumes) e se aproximou de outras lutas da época, como a do <strong>movimento pelos direitos civis dos negros</strong> nos Estados Unidos. Alternativa <strong>C</strong>.</p><p>Woodstock aconteceu uma vez, em 1969, nos Estados Unidos (A). A contracultura não combatia influências musicais estrangeiras (B). A Guerra Fria só acabou por volta de 1991 (D). E o movimento era contra a Guerra do Vietnã (E).</p>"},
12: {"materia": "História", "assunto": "Era Vargas",
     "enunciado": p("A divulgação do samba e do carnaval pelo rádio, principal meio de informação e entretenimento antes da chegada da televisão, foi fundamental para que eles se tornassem símbolos da cultura brasileira.",
                    "Em 1950, uma marchinha relacionada a um evento político foi marcante. Vejamos a sua letra, composta por Haroldo Lobo e Marino Pinto.")
                  + "[[fig:1]]" + p("Essa marchinha diz respeito à"),
     "imagens": [{"arquivo": "q12", "alt": "Letra da marchinha de carnaval de 1950, de Haroldo Lobo e Marino Pinto, em três estrofes curtas. Ela pede para pôr de novo, no mesmo lugar, o retrato do “velho”, cujo sorriso “faz a gente trabalhar” e “faz a gente se animar”. Fonte: &lt;https://tinyurl.com/z3d76fp&gt;, acesso em 08.02.2017."}],
     "explicacao": "<p>Em 1950, Getúlio Vargas, o “velho”, foi eleito presidente pelo voto direto, depois de ter sido deposto em 1945. A marchinha fala em recolocar o retrato dele nas repartições e associa seu sorriso ao trabalho, lembrando o <strong>trabalhismo</strong>. Alternativa <strong>B</strong>.</p><p>O 13º salário é de 1962, no governo Goulart (A). A República é de 1889 (C). O Palácio da Alvorada só foi construído em Brasília, nos anos 1950 e 1960, e o retrato não é de D. Pedro II (D). E Deodoro não proibiu o carnaval (E).</p>"},
13: {"materia": "Biologia", "assunto": "Fisiologia humana", "tags": ["vitamina D", "pele"],
     "explicacao": "<p>A vitamina D ajuda o intestino a absorver cálcio e o fixa nos ossos. Sem ela, os ossos ficam fracos e podem se deformar, como no raquitismo. Alternativa <strong>D</strong>.</p><p>Quanto mais sensível a pele, maior deve ser o FPS (A). Os raios UV ativam a produção de vitamina D, e não provocam hemorragias (B). O texto diz que das 10 às 16 horas a radiação é mais intensa (C). E o bronzeado é a produção de melanina pela pele, não o dano às fibras da derme (E).</p>"},
14: {"materia": "Biologia", "assunto": "Zoologia", "tags": ["vertebrados", "Pantanal"],
     "enunciado": apoio(T(7, "O pantanal mato-grossense", "fez as seguintes anotações:")[0],
                        "• existem muitas espécies de mamíferos como, por exemplo, as onças-pintadas, as jaguatiricas e os tamanduás;<br>"
                        "• possui grande diversidade de aves como, por exemplo, as garças, os colhereiros, os tucanos, as emas e os jaburus;<br>"
                        "• há muitas espécies de peixes, entre os quais se destacam os pintados, os dourados, os pacus e os surubins;<br>"
                        "• e entre os répteis, há os jacarés-do-pantanal, as sucuris e os lagartos.")
                  + p("Considerando os animais observados pelos alunos é correto afirmar que"),
     "explicacao": "<p>Os mamíferos são <strong>endotérmicos</strong>: produzem calor pelo próprio metabolismo e mantêm a temperatura do corpo constante. Alternativa <strong>E</strong>.</p><p>Jacarés, sucuris e lagartos não são peçonhentos (A). As aves têm fecundação interna (B). O coração dos mamíferos tem quatro cavidades (C). E os répteis respiram por pulmões, não por brânquias (D).</p>"},
15: {"materia": "Geografia", "assunto": "Biomas brasileiros", "tags": ["Mata Atlântica"],
     "explicacao": "<p>A Mata Atlântica é uma floresta tropical <strong>densa</strong>, de folhas largas (<strong>latifoliada</strong>) e com grande variedade de espécies (<strong>heterogênea</strong>). Alternativa <strong>A</strong>.</p><p>Floresta aciculifoliada homogênea é a de coníferas, como a mata de araucárias (B). A tundra não tem cactos e não existe no Brasil (C). Arbustos de galhos retorcidos lembram o cerrado (D). E plantas esparsas e xerófitas são típicas da caatinga (E).</p>"},
16: {"materia": "Geografia", "assunto": "Cartografia", "tags": ["meridiano de Greenwich"],
     "enunciado": enun(R, 16, figs={"p08-1": 1}).replace("<p>Esse Meridiano", fonte("&lt;http://tinyurl.com/jxkcbaf&gt; Acesso em: 17.01.2017. Original colorido.") + "<p>Esse Meridiano"),
     "imagens": [{"arquivo": "q16", "alt": "Foto vista de cima de dois pés de tênis, um de cada lado da faixa metálica que marca o meridiano de Greenwich no chão."}],
     "explicacao": "<p>O meridiano de Greenwich é o 0º de longitude e divide a Terra em hemisférios <strong>oeste (ocidental) e leste (oriental)</strong>. Alternativa <strong>D</strong>.</p><p>Norte e sul, boreal e austral, são separados pela linha do Equador (C e E). Ártico e antártico são regiões polares (B). E tropical e temperado são zonas climáticas (A).</p>"},
17: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": ["febre amarela"],
     "explicacao": "<p>A febre amarela é transmitida pela picada de mosquitos infectados. <strong>Eliminar os mosquitos</strong> (e se vacinar) é um modo eficaz de prevenir. Alternativa <strong>E</strong>.</p><p>Ela não passa por objetos nem de pessoa para pessoa (A). Os dez dias são o prazo para a vacina proteger, não para a cura (B). A doença não depende da higiene pessoal (C). E não é transmitida por contato sexual (D).</p>"},
18: {"materia": "Geografia", "assunto": "Geografia da Ásia", "tags": ["turismo religioso"],
     "explicacao": "<p>Meca, na Arábia Saudita, é a cidade mais sagrada do islamismo. Lá fica a <strong>Caaba</strong>, destino da peregrinação (hajj) que todo muçulmano deve fazer ao menos uma vez na vida. É turismo <strong>religioso</strong>. Alternativa <strong>D</strong>.</p><p>Meca não é conhecida por negócios de petróleo, ecossistema tropical, cassinos ou corridas de automóvel (A, B, C e E). A Arábia Saudita é desértica, e jogos de azar são proibidos no país.</p>"},
19: {"materia": "Física", "assunto": "Circuitos elétricos",
     "enunciado": p("Uma brincadeira consiste em passar um anel condutor, de um extremo a outro de um fio retorcido, também condutor de eletricidade. Durante a brincadeira a chave deve permanecer fechada conectando a pilha ao circuito. O anel deve ser passado por toda a extensão do fio retorcido sem toca-lo, pois quando a lâmpada acende a brincadeira acaba.",
                    "Assinale a alternativa que apresenta um esquema de construção de um dispositivo de acordo com a descrição apresentada para a brincadeira."),
     "imagens": [{"arquivo": "q19a", "alt": "Alternativa A: o fio retorcido está ligado à lâmpada e também diretamente ao cabo do anel; a lâmpada, a pilha e a chave estão ligadas em sequência até o anel."},
                 {"arquivo": "q19b", "alt": "Alternativa B: o anel está ligado à pilha; o fio retorcido está ligado à lâmpada, e a lâmpada à pilha; os dois terminais da chave estão ligados à pilha."},
                 {"arquivo": "q19c", "alt": "Alternativa C: o fio retorcido está ligado à lâmpada, a lâmpada à chave, a chave à pilha e a pilha ao anel, tudo em sequência; o circuito só se fecha se o anel tocar o fio."},
                 {"arquivo": "q19d", "alt": "Alternativa D: o anel está ligado à chave, a chave à pilha, a pilha à lâmpada e a lâmpada ao fio retorcido; o fio retorcido também está ligado diretamente à pilha."},
                 {"arquivo": "q19e", "alt": "Alternativa E: o anel está ligado só ao fio retorcido; o fio está ligado à lâmpada, a lâmpada à pilha, e a pilha à chave, cujos dois terminais voltam à pilha."}],
     "alternativas": figs_alt(1),
     "explicacao": "<p>A lâmpada deve acender só quando o anel tocar o fio. Para isso, pilha, chave e lâmpada ficam em série num caminho que vai do anel até o fio retorcido, e o único ponto aberto do circuito é o espaço entre o anel e o fio. É o que mostra a alternativa <strong>C</strong>.</p><p>Em A e E, o anel já está ligado diretamente ao fio, então o circuito fica sempre fechado (ou a lâmpada nunca participa dele). Em B e D, as ligações extras com a pilha criam outro caminho para a corrente, e o toque do anel não é o que acende a lâmpada.</p>"},
20: {"materia": "Matemática", "assunto": "Operações e problemas", "tags": ["quadrado mágico"],
     "enunciado": p("O Quadrado Mágico é uma tabela quadrada composta por números inteiros consecutivos a partir do 1, em que a soma de cada coluna, de cada linha e de cada diagonal são iguais. Essa soma é chamada de número mágico.",
                    "Aprenda a encontrar o número mágico de um quadrado 3x3, como o da figura.")
                  + tabela(["", "", ""], [["8", "1", "6"], ["3", "5", "7"], ["4", "9", "2"]]).replace("<thead><tr><th scope=\"col\"></th><th scope=\"col\"></th><th scope=\"col\"></th></tr></thead>", "")
                  + p("O quadrado mágico 3x3 possui 9 posições, portanto deve ser preenchido com os números de 1 até 9, sem repetição.", "O número mágico pode ser encontrado seguindo dois passos.")
                  + apoio("<strong>Passo 1</strong> – Encontrar a soma total dos números.<br>1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45",
                          "<strong>Passo 2</strong> – Dividir a soma encontrada pelo número de colunas existentes no quadrado.<br>No caso do quadrado mágico 3x3, os 9 números estão agrupados em 3 colunas.<br>Logo o número mágico será 45:3 = 15")
                  + p("Em condições semelhantes, o número mágico de um quadrado 4x4 será"),
     "explicacao": "<p>Um quadrado 4x4 usa os números de 1 a 16. A soma é 1 + 2 + … + 16 = 16 · 17 ÷ 2 = 136. Dividindo pelas 4 colunas: 136 ÷ 4 = <strong>34</strong>. Alternativa <strong>C</strong>.</p><p>136 é só a soma total, sem dividir (E). 16 e 64 confundem a quantidade de casas com a soma (A e D).</p>"},
21: {"materia": "Português", "assunto": "Conectivos", "tags": ["tirinha"],
     "enunciado": p("Leia a tirinha.") + "[[fig:1]]" + url("https://tinyurl.com/k34rtjp", "10.02.2017", "")
                  + p("No quarto quadrinho, a menina utiliza o termo “aí” como elemento coesivo para dar continuidade às ações que começou a descrever no terceiro quadrinho.",
                      "Assinale a alternativa que contenha um elemento coesivo que possa substituir corretamente o termo “aí”, preservando o mesmo sentido da fala da personagem."),
     "imagens": [{"arquivo": "q21", "alt": "Tirinha de Calvin em quatro quadrinhos. 1: Susie pergunta: “Ei, Calvin, quer brincar de papai e mamãe?” 2: Calvin, brincando com carrinhos: “Sei lá. Como é que se brinca disso?” 3: Susie explica: “Primeiro, você chega do trabalho. Depois eu chego do trabalho.” 4: Susie continua: “Aí a gente reclama dos nossos empregos e briga pra ver quem usa o micro-ondas primeiro.”"}],
     "explicacao": "<p>“Aí” indica o que acontece em seguida, numa sequência de ações: “primeiro… depois… aí”. A palavra com o mesmo sentido de sequência é <strong>então</strong>. Alternativa <strong>D</strong>.</p><p>“Entretanto” e “todavia” indicam oposição (A e C). “Portanto” indica conclusão (B). E “afinal” indica fechamento ou conclusão final (E).</p>"},
22: {"materia": "História", "assunto": "Antiguidade", "tags": ["Roma Antiga"],
     "enunciado": apoio(T(10, "Imagine um só lugar", "podiam frequentar.")[0]) + url("https://tinyurl.com/cynbuy", "08.02.2017")
                  + p("De acordo com o texto, é correto afirmar que as construções citadas"),
     "explicacao": "<p>O texto diz que nas termas se podia “fazer compras, alugar livros, fazer ginástica”, ver arte e comer, e que o banho era “mais uma atividade social do que de higiene”. Eram <strong>grandes edificações com diversas atividades sociais</strong>. Alternativa <strong>A</strong>.</p><p>As termas são da Roma Antiga, não da Idade Média (B). Os banhos tinham horários separados para homens e mulheres e abrigavam milhares de pessoas (C). A unificação italiana é do século XIX (D). E os edifícios eram enormes e abertos a vários grupos sociais (E).</p>"},
23: {"materia": "Física", "assunto": "Dinâmica", "tags": ["equilíbrio de forças"],
     "enunciado": p("Há muitos conceitos físicos no ato de empinar pipas. Talvez por isso essa brincadeira seja tão divertida.",
                    "Uma questão física importante para que uma pipa ganhe altura está na escolha certa do ponto em que a linha do carretel é amarrada ao estirante (ponto P), conforme a figura.")
                  + "[[fig:1]]" + apoio("Na figura, a malha quadriculada coincide com o plano que contém a linha, o estirante e a vareta maior da pipa.")
                  + p("O estirante é um pedaço de fio amarrado à pipa com um pouco de folga e em dois pontos: no ponto em que as duas varetas maiores se cruzam e no extremo inferior da vareta maior, junto à rabiola.",
                      "Admitindo que a pipa esteja pairando no ar, imóvel em relação ao solo, e tendo como base a figura, os vetores que indicam as forças atuantes sobre o ponto P estão melhor representados em"),
     "imagens": [{"arquivo": "q23", "alt": "Pipa no ar sobre uma malha quadriculada. Do ponto P saem três fios: o fio do carretel, para baixo e à esquerda; um trecho do estirante, para cima e à direita, até o cruzamento das varetas; e outro trecho do estirante, para baixo e à direita, até o pé da vareta, junto à rabiola."},
                 {"arquivo": "q23a", "alt": "Alternativa A: três vetores partindo de P, cada um apontando para fora ao longo de um dos três fios (para baixo à esquerda, para cima à direita e para baixo à direita)."},
                 {"arquivo": "q23b", "alt": "Alternativa B: o vetor do fio de cima aponta para P; os outros dois apontam para fora de P."},
                 {"arquivo": "q23c", "alt": "Alternativa C: o vetor do fio de baixo à direita aponta para P; os outros dois apontam para fora de P."},
                 {"arquivo": "q23d", "alt": "Alternativa D: o vetor do fio do carretel aponta para P; os outros dois apontam para fora de P."},
                 {"arquivo": "q23e", "alt": "Alternativa E: os três vetores apontam para P."}],
     "alternativas": figs_alt(2),
     "explicacao": "<p>Um fio só consegue puxar, nunca empurrar. Então cada um dos três fios ligados a P exerce sobre ele uma tração <strong>apontando para fora de P</strong>, ao longo do próprio fio. Com a pipa parada, essas três forças se equilibram. Alternativa <strong>A</strong>.</p><p>Nas outras, pelo menos um vetor aponta para P, como se o fio empurrasse o ponto, o que não acontece (B, C, D e E).</p>"},
24: {"materia": "Matemática", "assunto": "Equações", "tags": ["fatoração"],
     "enunciado": enun(R, 24, trocas=[("[[FIG:p12-1]]", apoio("\\(x^3 + 6x^2 + 5x - 12 = 0 \\Leftrightarrow (x - 1) \\cdot (x + 3) \\cdot (x + 4) = 0\\)"))], tirar_figs=False).replace("[[FIG:p11-6]]", ""),
     "explicacao": "<p>O produto (x − 1)(x + 3)(x + 4) é zero quando algum fator é zero: x = 1, x = −3 ou x = −4. São <strong>três raízes inteiras distintas</strong>. Alternativa <strong>B</strong>.</p><p>−3 e −4 não são naturais (A e C). Não há raiz irracional (C e D). E há raízes reais (E).</p>"},
25: {"materia": "Biologia", "assunto": "Fisiologia humana", "tags": ["respiração"],
     "enunciado": apoio(T(12, "Praticar uma atividade física", "solicitado pela musculatura.")[0]) + url("http://tinyurl.com/m94o229", "08.04.2017")
                  + p("O músculo a que o texto se refere é denominado"),
     "explicacao": "<p>O músculo que participa da respiração e fica entre o tórax e o abdome é o <strong>diafragma</strong>. Alternativa <strong>D</strong>.</p><p>Bíceps fica no braço (A). Deltoide, no ombro (B). Trapézio, nas costas e no pescoço (C). E o miocárdio é o músculo do coração (E).</p>"},
26: {"materia": "Física", "assunto": "Dinâmica", "tags": ["alavanca", "torque"],
     "enunciado": enun(R, 26, trocas=[("[[FIG:p12-3]]", apoio("Despreze o peso da tábua, bem como as dimensões dos corpos de Marcelo e de seu filho"))], tirar_figs=False),
     "explicacao": "<p>Na gangorra equilibrada, peso × distância ao apoio é igual dos dois lados. Se o filho pesa P e Marcelo 3P: P · d<sub>filho</sub> = 3P · d<sub>pai</sub>, ou d<sub>filho</sub> = 3 d<sub>pai</sub>. Como d<sub>filho</sub> + d<sub>pai</sub> = 3,2 m, então 4 d<sub>pai</sub> = 3,2, d<sub>pai</sub> = 0,8 m e d<sub>filho</sub> = <strong>2,4 m</strong>. Alternativa <strong>E</strong>.</p><p>0,8 m é a distância de Marcelo ao apoio (A). 1,6 m seria o apoio no meio, como se tivessem o mesmo peso (C).</p>"},
27: {"materia": "Matemática", "assunto": "Operações e problemas", "tags": ["potências de 2"],
     "enunciado": p("Uma antiga lenda da Índia afirma que o jogo de xadrez foi criado a pedido de um rei e, como recompensa, o criador do jogo recebeu grãos de trigo de acordo com o número de casas do tabuleiro, seguindo o procedimento descrito.",
                    "• O criador do jogo escolhe uma casa e recebe 2 grãos por ela.", "• Para a próxima casa escolhida, ele recebe o dobro da casa anterior.",
                    "• O processo continua até que todas as casas do tabuleiro sejam escolhidas exatamente uma vez.",
                    "Observando o processo podemos perceber que, para a décima casa do tabuleiro, o rei entrega 1 024 grãos.")
                  + "[[fig:1]]" + apoio("O tabuleiro de xadrez conta com 64 casas distribuídas em 8 colunas verticais e 8 fileiras horizontais, cada uma com 8 casas. As casas são alternadamente escuras e claras.")
                  + p("É correto afirmar que, o número de grãos a ser entregue pela vigésima casa seria"),
     "imagens": [{"arquivo": "q27", "alt": "Tabuleiro de xadrez com 8 por 8 casas, alternadamente pretas e brancas."}],
     "explicacao": "<p>A casa <em>n</em> rende 2<sup><em>n</em></sup> grãos (a 10ª rende 2<sup>10</sup> = 1 024). A 20ª rende 2<sup>20</sup> = 1 024 · 1 024 = 1 048 576 grãos, que está <strong>entre 1 000 000 e 10 000 000</strong>. Alternativa <strong>D</strong>.</p><p>Dobrar só o resultado da 10ª casa (2 048) ou multiplicar 1 024 por 10 leva às faixas menores (A e B). E 2<sup>20</sup> ainda não chega a 10 milhões (E).</p>"},
28: {"materia": "Geografia", "assunto": "Climatologia", "tags": ["altitude", "América do Sul"],
     "enunciado": p("O futebol faz parte do cotidiano de grande parte dos brasileiros. É um dos assuntos nas rodas de conversa nos mais variados locais, além de ser um grande divertimento para quem vai aos estádios para assistir às partidas.",
                    "Um torneio de futebol importante é a Copa Libertadores da América, da qual participam equipes de quase todos os países da América do Sul.",
                    "Uma das preocupações das equipes brasileiras participantes da Copa é jogar na cidade de La Paz, na Bolívia.",
                    "Essa preocupação existe, pois essa cidade está situada"),
     "explicacao": "<p>La Paz fica a cerca de 3 600 m de altitude, na <strong>Cordilheira dos Andes</strong>. Em grande altitude o ar é <strong>rarefeito</strong>, com menos oxigênio, e os atletas se cansam mais. Alternativa <strong>B</strong>.</p><p>O Himalaia fica na Ásia (A). La Paz não fica no nível do mar nem no litoral, pois a Bolívia nem tem saída para o mar (C, D e E).</p>"},
29: {"materia": "Física", "assunto": "Óptica", "tags": ["sombra", "semelhança de triângulos"],
     "explicacao": "<p>A luz se propaga em linha reta, e a mão e a sombra formam triângulos semelhantes com vértice na chama. Se a sombra é 5 vezes maior que a mão, a parede está 5 vezes mais longe da chama que a mão: 5 · 0,5 m = <strong>2,5 m</strong>. Alternativa <strong>D</strong>.</p><p>2,0 m seria a distância entre a mão e a parede (C). E 5,0 m vem de multiplicar 5 por 1 m (E).</p>"},
30: {"materia": "Química", "assunto": "Estrutura atômica", "tags": ["tabela periódica"],
     "enunciado": JOGO + P30,
     "anulacao": {"fonte": "analise", "motivo": ANULADA_30_31},
     "explicacao": "<p>Questão anulada. Pela nomenclatura atual da IUPAC, os gases nobres (hélio, neônio, argônio, criptônio, xenônio, radônio e oganessônio, de número atômico 118) formam o <strong>grupo 18</strong> da Tabela Periódica, o que corresponderia à alternativa E.</p><p>Os grupos 1 e 2 são os metais alcalinos e alcalinoterrosos, o 16 é o dos calcogênios e o 17, o dos halogênios.</p>"},
31: {"materia": "Química", "assunto": "Estrutura atômica", "tags": ["tabela periódica"],
     "enunciado": p("Suponha que um aluno esteja com sua peça no elemento químico sódio, localizado no grupo 1 da Tabela Periódica.",
                    "Ao jogar o dado, tira o número três e decide deslocar sua peça no mesmo grupo, de modo a se aproximar do elemento químico de número atômico 118.",
                    "Nessas condições, ele deve se deslocar no sentido"),
     "apoio_de": (30, P30),
     "anulacao": {"fonte": "analise", "motivo": ANULADA_30_31},
     "explicacao": "<p>Questão anulada. O elemento 118 (oganessônio) fica no 7º período, embaixo na Tabela. Andando no grupo 1 a partir do sódio (3º período) para se aproximar dele, a peça desceria pelo grupo, passando pelo <strong>potássio</strong>, rubídio e césio, o que corresponderia à alternativa B.</p><p>Cloro e gases nobres ficam em outros grupos, e as regras do jogo só permitem movimentos verticais ou horizontais, nunca em diagonal. “Horizontal” não manteria a peça no mesmo grupo.</p>"},
32: {"materia": "Matemática", "assunto": "Funções", "tags": ["função do 2º grau"],
     "enunciado": p("Em um famoso jogo eletrônico de arremessar pássaros, a trajetória do lançamento corresponde a parte de uma parábola, como a da figura.") + "[[fig:1]]"
                  + url("https://tinyurl.com/zx74hnz", "03.03.2017", "Original colorido.")
                  + p("Considere que um jogador fez um lançamento de um pássaro virtual cuja trajetória pode ser descrita pela função h(x) = − x² + 4x, com x variando entre 0 e 4.",
                      "O gráfico mostra essa trajetória. O ponto de lançamento do pássaro coincide com a origem do plano cartesiano.")
                  + "[[fig:2]]" + p("Analisando o gráfico, é correto afirmar que o pássaro começa a"),
     "imagens": [{"arquivo": "q32a", "alt": "Tela de um jogo eletrônico com uma trajetória pontilhada em forma de arco, saindo de um estilingue à esquerda até estruturas à direita."},
                 {"arquivo": "q32b", "alt": "Gráfico de uma parábola voltada para baixo, que sai da origem (0, 0), sobe até o ponto mais alto (2, 4) e desce até (4, 0)."}],
     "explicacao": "<p>O vértice da parábola h(x) = −x² + 4x está em x = −4 ÷ (2 · (−1)) = 2, com h(2) = −4 + 8 = 4. Até esse ponto o pássaro sobe; depois dele, <strong>começa a cair a partir de (2, 4)</strong>. Alternativa <strong>A</strong>.</p><p>(4, 2) não pertence à parábola, pois h(4) = 0 (B e D). O pássaro sobe a partir da origem, não de (2, 4) (C). E (3, 3) está na descida (E).</p>"},
33: {"materia": "Geografia", "assunto": "Cartografia", "tags": ["continentes"],
     "enunciado": enun(R, 33, trocas=[("[[FIG:p15-3]]", "")]).replace("<p>Asiático,</p><p>Europeu e Africano, nessa ordem.</p>", "").replace("conquistar os continentes</p>", "conquistar os continentes Asiático, Europeu e Africano, nessa ordem.</p>")
                  + "[[fig:1]]" + url("http://tinyurl.com/hf7n72g", "20.01.2017", ""),
     "imagens": [{"arquivo": "q33", "alt": "Mapa-múndi em contorno com seis números: 1 sobre a América, 2 sobre a Europa, 3 sobre a África, 4 sobre a Ásia, 5 sobre a Oceania e 6 sobre a Antártida."}],
     "explicacao": "<p>No mapa, a Ásia é o <strong>4</strong>, a Europa é o <strong>2</strong> e a África é o <strong>3</strong>. Na ordem pedida (Asiático, Europeu, Africano): 4, 2 e 3. Alternativa <strong>B</strong>.</p><p>As outras trocam a ordem ou os números dos continentes. O 1 é a América, o 5 é a Oceania e o 6, a Antártida.</p>"},
34: {"materia": "Matemática", "assunto": "Geometria plana", "tags": ["polígonos", "Tangram"],
     "enunciado": TANGRAM + P34, "imagens": [TANGRAM_IMG],
     "explicacao": "<p>O texto diz que a tábua foi cortada em “um quadrado, um paralelogramo e cinco triângulos”. O quadrado e o paralelogramo têm quatro lados: são <strong>dois quadriláteros e cinco triângulos</strong>. Alternativa <strong>E</strong>.</p><p>Todas as peças são convexas (A). Há peças que não são triângulos (B). Só o quadrado é um quadrilátero regular (C). E não há trapézios (D).</p>"},
35: {"materia": "Matemática", "assunto": "Geometria plana", "tags": ["área", "Tangram"],
     "enunciado": p("Observe o Tangram, em uma possível disposição de suas peças.") + "[[fig:2]]"
                  + apoio("Na figura, tem-se que: \\(\\overline{QS}\\) é paralelo a \\(\\overline{BD}\\); os polígonos ABCD e OPQR são quadrados; <strong>S</strong> é ponto médio de \\(\\overline{CD}\\); <strong>P</strong> é ponto médio de \\(\\overline{OB}\\); <strong>O</strong> é ponto médio de \\(\\overline{BD}\\).")
                  + p("Se a área do triângulo ABO é 16 cm², a área do quadrado OPQR é, em centímetros quadrados,"),
     "apoio_de": (34, P34),
     "imagens": [{"arquivo": "q35", "alt": "Quadrado ABCD dividido nas peças do Tangram: as diagonais se cruzam no centro O; há um quadradinho OPQR abaixo de O, um paralelogramo e triângulos de vários tamanhos, com os pontos T, S, P, Q e R marcados."}],
     "explicacao": "<p>As diagonais dividem o quadrado ABCD em 4 triângulos iguais a ABO. Então a área de ABCD é 4 · 16 = 64 cm². No Tangram, o quadradinho OPQR vale 1/8 do quadrado todo: seu lado é metade de OB, e sua diagonal é metade da diagonal do quadrado grande. Área: 64 ÷ 8 = <strong>8 cm²</strong>. Alternativa <strong>D</strong>.</p><p>4 cm² seria 1/16 do total, a área de cada triângulo pequeno (B).</p>"},
36: {"materia": "Física", "assunto": "Pressão",
     "explicacao": "<p>Pressão é força dividida pela área. O peso da criança é o mesmo, mas apoiada num pé só a área de contato cai pela metade, então a pressão fica <strong>duas vezes maior</strong>. Alternativa <strong>B</strong>.</p><p>A área cai pela metade, não para um quarto (A). E a pressão não fica igual nem menor (C, D e E).</p>"},
37: {"materia": "História", "assunto": "Brasil República", "tags": ["movimento operário"],
     "enunciado": apoio(*T(17, "Nas primeiras décadas do século passado", "melhoria das condições de trabalho.", ["Primeiramente fundados"]))
                  + url("https://tinyurl.com/z76arjw", "10.02.2017") + p("De acordo com o texto, é correto afirmar que"),
     "explicacao": "<p>O texto diz que, nas primeiras décadas do século XX, “a reunião proporcionada pelo futebol no ambiente industrial possibilitava a discussão e a mobilização pela melhoria das condições de trabalho”. Alternativa <strong>D</strong>.</p><p>O perfil democrático dos times contrastava com a sociedade da época (A). Os times são do século XX, não do XIX (B e C). E eles foram fundados com apoio dos patrões, não proibidos por eles (E).</p>"},
38: {"materia": "História", "assunto": "Povos indígenas", "tags": ["Sateré Mawé"],
     "enunciado": p("Você já deve ter experimentado algum refrigerante de guaraná, presença quase certa nas festas de aniversário. Mas você já parou para imaginar qual a origem do fruto?")
                  + apoio(*T(17, "O guaraná é originário da Amazônia", "mais uma rodada da bebida.", ["Entre eles, o guaraná"]))
                  + url("https://tinyurl.com/zy6cmm6", "10.02.2017") + "[[fig:1]]" + url("https://tinyurl.com/zwrvvpj", "10.02.2017", "Original colorido.")
                  + p("Conforme o texto, é correto afirmar que"),
     "imagens": [{"arquivo": "q38", "alt": "Foto de um cacho de frutos de guaraná abertos, com sementes escuras envoltas por uma parte branca, lembrando olhos.", "legenda": "Frutos de guaraná"}],
     "explicacao": "<p>O texto diz que a colheita, no período das chuvas, “é um período de vida social intensa, quando os Sateré Mawé restauram as suas forças”. Alternativa <strong>A</strong>.</p><p>A bebida é tomada por adultos e crianças (B). Os Sateré Mawé vivem no Amazonas, e o texto não diz que inventaram o refrigerante (C). Quem prepara a bebida é uma mulher (D). E a colheita é no período das chuvas, de novembro a março (E).</p>"},
39: {"materia": "Biologia", "assunto": "Nutrição e saúde",
     "explicacao": "<p>As <strong>proteínas</strong>, que constroem e reparam o corpo, estão no <strong>frango</strong> e no <strong>feijão</strong>. Alternativa <strong>E</strong>.</p><p>A salada de alface e o suco quase não têm gordura (A). A celulose não é digerida pelo ser humano, então não fornece energia (B). Também há amido na batata e no feijão (C). E salada, tomate e suco têm vitaminas (D).</p>"},
40: {"materia": "Português", "assunto": "Interpretação de texto",
     "enunciado": DIVERTIDA + P40,
     "explicacao": "<p>O texto diz que cada uma das cinco emoções de Riley tem “cor e temperamentos próprios, claramente infantilizados para facilitar a compreensão do público menor, mas ainda assim de uma profundidade impressionante”. Alternativa <strong>A</strong>.</p><p>O filme evita a vilanização da tristeza (B). A depressão “jamais” é citada pelo nome e não é uma das emoções (C). O filme facilita a compreensão do público infantil (D). E o texto não diz que a depressão está em todos os filmes do estúdio (E).</p>"},
41: {"materia": "Português", "assunto": "Classes de palavras", "tags": ["porquês"],
     "enunciado": p("Releia o trecho.")
                  + apoio("Vários são os conceitos adaptados nesta grande alegoria emocional, como o <strong>porquê</strong> de se esquecer fatos antigos de sua vida [...]")
                  + p("Há diversos usos dos porquês e cada um deles exige uma determinada grafia. Uma das grafias existentes para essa palavra foi destacada no trecho selecionado em que o porquê exerce função de um substantivo.",
                      "Tendo isso em vista, assinale a alternativa em que a palavra “porquê” é grafada corretamente e é classificada como um substantivo."),
     "apoio_de": (40, P40),
     "explicacao": "<p>“Porquê”, junto e com acento, é substantivo e significa “o motivo”; vem acompanhado de artigo. Em “é <strong>o porquê</strong> da fama do estúdio”, ele é usado assim. Alternativa <strong>E</strong>.</p><p>Em início de pergunta, usa-se “por que” separado e sem acento (A). No fim de pergunta, “por quê” separado e com acento (B). Para explicar uma causa, usa-se “porque” junto e sem acento (C e D).</p>"},
42: {"materia": "Física", "assunto": "Magnetismo", "tags": ["ímãs"],
     "enunciado": enun(R, 42, figs={"p19-2": 1, "p19-3": 2}),
     "imagens": [{"arquivo": "q42a", "alt": "Figura 1: um ímã em forma de bastão, visto de lado; a metade esquerda é branca (polo Sul) e a direita é escura (polo Norte)."},
                 {"arquivo": "q42b", "alt": "Figura 2: seis ímãs formando dois quadrados lado a lado, com ímãs horizontais em cima e embaixo e ímãs verticais nas laterais e no meio."},
                 {"arquivo": "q42c", "alt": "Alternativa A: um arranjo dos ímãs na forma da figura 2, com os polos escuros e claros numa disposição própria."},
                 {"arquivo": "q42d", "alt": "Alternativa B: um arranjo dos ímãs na forma da figura 2, com os polos escuros e claros numa disposição própria."},
                 {"arquivo": "q42e", "alt": "Alternativa C: um arranjo dos ímãs na forma da figura 2, com os polos escuros e claros numa disposição própria."},
                 {"arquivo": "q42f", "alt": "Alternativa D: um arranjo dos ímãs na forma da figura 2, com os polos escuros e claros numa disposição própria."},
                 {"arquivo": "q42g", "alt": "Alternativa E: um arranjo dos ímãs na forma da figura 2, com os polos escuros e claros numa disposição própria."}],
     "alternativas": figs_alt(3),
     "explicacao": "<p>Polos diferentes se atraem e polos iguais se repelem. Para os ímãs ficarem unidos só pela força magnética, <strong>em cada ponto de contato um polo Norte (escuro) precisa encostar num polo Sul (claro)</strong>. Isso acontece em todos os encontros apenas no arranjo da alternativa <strong>B</strong>.</p><p>Nas outras, pelo menos um encontro junta dois polos iguais, e esses ímãs se repeliriam.</p>"},
43: {"materia": "Química", "assunto": "Estrutura atômica", "tags": ["símbolos dos elementos"],
     "enunciado": enun(R, 43, figs={"p19-1": 1}).replace("<p>Nessa imagem", fonte("&lt;https://tinyurl.com/mvvnsx8&gt; Acesso em: 26.01.2017. Original colorido.") + "<p>Nessa imagem"),
     "imagens": [{"arquivo": "q43", "alt": "Silhueta de um corpo humano preenchida com quadradinhos da tabela periódica. Na cabeça aparecem C e Si; no tronco, Ge, As, In, Sn, Sb, Pb e Uuq; nos braços e pernas, Cr, Fe, Co, Rh, Ir e outros."}],
     "explicacao": "<p>Na figura aparecem os símbolos <strong>C</strong> (carbono), <strong>Pb</strong> (chumbo) e <strong>Fe</strong> (ferro). Alternativa <strong>D</strong>.</p><p>Os símbolos do cálcio (Ca), enxofre (S), níquel (Ni), cloro (Cℓ) e flúor (F) não aparecem na imagem (A, B, C e E).</p>"},
44: {"materia": "Física", "assunto": "Óptica", "tags": ["associação de espelhos"],
     "enunciado": enun(R, 44, figs={"p20-2": 1, "p20-3": 2}, trocas=[("[[FIG:p20-1]]", apoio("O número de imagens distintas (N) que se formam de um objeto colocado entre dois espelhos pode ser calculado pela relação \\[N = \\dfrac{360^\\circ}{\\begin{array}{c}\\text{medida do ângulo entre}\\\\ \\text{as superfícies refletoras}\\end{array}} - 1\\]"))]),
     "imagens": [{"arquivo": "q44a", "alt": "Desenho 1: um prisma comprido de base triangular; na base aparente, um triângulo com ângulos de 60º e um furo no centro."},
                 {"arquivo": "q44b", "alt": "Desenho 2: molde de papel cartão com três retângulos “cole o espelho aqui” lado a lado, abas de colagem nas laterais, um triângulo com furo de um lado e um triângulo de material translúcido do outro."}],
     "explicacao": "<p>As bases são triângulos equiláteros, então os dois espelhos colados formam um ângulo de 60º. Pela relação dada: N = 360º ÷ 60º − 1 = 6 − 1 = <strong>5</strong> imagens. Alternativa <strong>D</strong>.</p><p>6 vem de esquecer de subtrair 1 (E). E três, duas ou uma imagem corresponderiam a ângulos maiores, de 90º, 120º ou 180º (A, B e C).</p>"},
45: {"materia": "Biologia", "assunto": "Ecologia", "tags": ["relações ecológicas"],
     "enunciado": enun(R, 45, figs={"p20-4": 1}).replace("<p>É correto", fonte("&lt;https://tinyurl.com/k9s33lr&gt; Acesso em: 17.03.2017. Original colorido.") + "<p>É correto"),
     "imagens": [{"arquivo": "q45", "alt": "Foto de um peixe-palhaço, com faixas brancas, nadando entre os tentáculos de uma anêmona-do-mar.", "legenda": "Peixe-palhaço entre os tentáculos da anêmona."}],
     "explicacao": "<p>O peixe-palhaço ganha proteção e alimento, e a anêmona aproveita os restos de comida deixados por ele. As duas espécies se beneficiam, mas poderiam viver separadas: é <strong>protocooperação</strong>. Alternativa <strong>E</strong>.</p><p>Não há disputa por recurso (A). Mimetismo é imitar outra espécie (B). No parasitismo e na predação, uma espécie é prejudicada (C e D).</p>"},
46: {"materia": "Geografia", "assunto": "Globalização", "tags": ["tecnologia"],
     "explicacao": "<p>Com a TV a cabo, os DVDs e, depois, o streaming pela internet, ficou <strong>mais prático e barato assistir a filmes em casa</strong>, e muitas salas de cinema fecharam. Alternativa <strong>D</strong>.</p><p>Os filmes estreiam primeiro no cinema, não na TV aberta (A). As salas não foram estatizadas (B). Na verdade, os cinemas saíram das ruas para os shopping centers (C). E as salas não viraram teatros em massa (E).</p>"},
47: {"materia": "Química", "assunto": "Funções inorgânicas",
     "enunciado": p("Em um trabalho interdisciplinar, o professor de redação pede aos alunos que façam um poema que seria denominado “Cienciando”, usando o estudo de Ciências.",
                    "Observe um desses poemas, em que o aluno cita algumas funções químicas.")
                  + apoio("<strong>Cienciando</strong>", "Periódica a nossa reação<br>Com ácido e base<br>Sem óxidos<br>A produzir um sal",
                          "A perfeita neutralização<br>Com ácido clorídrico e soda cáustica<br>Que não forme precipitado<br>Nem par conjugado.")
                  + p("Um exemplo de cada função, na ordem em que aparecem na primeira estrofe do poema, está presente na alternativa"),
     "alternativas": colunas(["1ª", "2ª", "3ª", "4ª"], [["NaOH", "HCℓ", "CO<sub>2</sub>", "NaCℓ"], ["NaOH", "NaCℓ", "CO<sub>2</sub>", "HCℓ"],
                                                     ["HCℓ", "NaOH", "CO<sub>2</sub>", "NaCℓ"], ["HCℓ", "NaOH", "NaCℓ", "CO<sub>2</sub>"], ["HCℓ", "NaCℓ", "NaOH", "CO<sub>2</sub>"]]),
     "explicacao": "<p>A primeira estrofe cita, nesta ordem, <strong>ácido</strong>, <strong>base</strong>, <strong>óxido</strong> e <strong>sal</strong>. Um exemplo de cada: HCℓ (ácido clorídrico), NaOH (hidróxido de sódio, a soda cáustica), CO<sub>2</sub> (óxido) e NaCℓ (sal). Alternativa <strong>C</strong>.</p><p>A e B começam pela base. D e E põem o sal ou a base fora de ordem e deixam o óxido por último.</p>"},
48: {"materia": "Biologia", "assunto": "Fisiologia humana", "tags": ["pele"],
     "explicacao": "<p>A <strong>epiderme</strong> é a camada mais externa da pele e funciona como barreira contra a entrada de micro-organismos e outros agentes. Alternativa <strong>D</strong>.</p><p>A pele não absorve toda a luz nem fica resistente à radiação (A). O sebo lubrifica e evita o ressecamento (B). A gordura sob a derme isola o calor e guarda energia, não produz sangue nem pigmento (C). E o suor, ao evaporar, diminui a temperatura do corpo (E).</p>"},
49: {"materia": "Português", "assunto": "Interpretação de texto",
     "enunciado": INTERNET + P49,
     "explicacao": "<p>A psicóloga Miriam diz que, “para controlar o vício, é preciso ser moderado”. Ou seja, o uso da internet e das redes sociais <strong>pode virar vício sem moderação</strong>. Alternativa <strong>C</strong>.</p><p>Fernanda tem dificuldade porque os alunos querem “facebookar”, não pesquisar o conteúdo (A). Nicole se diz “viciada” (B). O texto não fala da maioria das pessoas (D). E o perigo não se limita às empresas (E).</p>"},
50: {"materia": "Português", "assunto": "Formação de palavras",
     "enunciado": p("A formação e surgimento de palavras no português acontece por meio de vários processos.",
                    "As palavras “facebookar” e “desenvolvimento”, presentes no texto, exemplificam dois desses processos: o neologismo e a derivação sufixal.")
                  + apoio("<strong>(I)</strong> Facebookar ⇒ Neologismo", "<strong>(II)</strong> Desenvolvimento ⇒ Derivação sufixal")
                  + p("Esses dois processos acontecem quando"),
     "apoio_de": (49, P49),
     "alternativas": colunas(["(I)", "(II)"], [["há a junção de dois ou mais radicais", "há anexação de sufixo na palavra de origem"],
                                              ["há anexação de sufixo na palavra de origem", "há a criação de novas palavras"],
                                              ["há a criação de novas palavras", "a palavra é constituída por radicais de diferentes línguas"],
                                              ["a palavra é constituída por radicais de diferentes línguas", "as palavras imitam um som, como ruídos e gritos"],
                                              ["há a criação de novas palavras", "há anexação de sufixo na palavra de origem"]]),
     "explicacao": "<p><strong>Neologismo</strong> é a <strong>criação de uma palavra nova</strong>, como “facebookar”. <strong>Derivação sufixal</strong> é o acréscimo de um <strong>sufixo</strong> a uma palavra já existente: desenvolver + -mento. Alternativa <strong>E</strong>.</p><p>Juntar radicais é composição (A). B inverte os dois processos. Radicais de línguas diferentes formam hibridismos (C e D). E imitar sons é onomatopeia (D).</p>"},
}
completar(Q, R)
