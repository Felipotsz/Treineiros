# Ajustes da conferência humana: Vestibulinho ETEC 1º semestre de 2023 (exame de 18/12/2022)
# Prova com 40 questões, em 3 horas. Texto conferido com a imagem de cada página. Gabarito: oficial (1SEM23). Tema: oceanos.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import A, carregar, enun, tabela, colunas, completar

META = {
    "id": "etec-2023-1sem",
    "banca": "ETEC",
    "ano": 2023,
    "semestre": 1,
    "titulo": "Vestibulinho ETEC, 1º semestre de 2023",
    "fonte": "Centro Paula Souza",
    "dataExame": "2022-12-18",
    "duracaoMinutos": 180,
    "tema": "Oceanos",
    "pdf": "assets/provas/etec-2023-1sem.pdf",
}

R = carregar("etec-2023-1sem")
I = "interdisciplinar"

OCEANO = ('<p class="chamada">Leia o texto para responder às questões de 01 a 03.</p>'
          '<p class="apoio"><strong><u>Você</u></strong> sabia que o oceano desempenha um papel fundamental na regulação do clima no planeta? Vivemos em um planeta azul, com oceanos e mares cobrindo mais de 70% da superfície da Terra.' + A +
          'Os oceanos <strong><u>nos</u></strong> alimentam, regulam nosso clima e geram a maior parte do oxigênio <strong><u>que</u></strong> respiramos.' + A +
          'Apesar de <strong><u>sua</u></strong> importância, os oceanos estão enfrentando ameaças sem precedentes como resultado da atividade humana. Todos os anos, cerca de 8 milhões de toneladas de resíduo plástico acabam nos ecossistemas marinhos.' + A +
          'Ao mesmo tempo, a crise climática está danificando os recifes de coral e outros ecossistemas importantes, a pesca excessiva ameaça a estabilidade dos estoques de peixes, a poluição por nutrientes contribui para a criação de zonas mortas, e quase 80% das águas residuais do mundo são descartadas sem tratamento nos oceanos.' + A +
          'Cuidar dos oceanos é cuidar do clima e da vida.' + A +
          'Como as mudanças climáticas afetam você? Conte pra gente!' + A +
          '#HoraDeAgir #mudançadoclima #criseclimática #AçãoClimática</p>'
          '<p class="fonte">&lt;https://tinyurl.com/bdh8vhjk&gt; Acesso em: 14.09.2022. Adaptado.</p>')
P1 = ("<p>Os pronomes são importantes elementos textuais, pois auxiliam na construção de sentido do texto, evitando a repetição de informações e estabelecendo conexões entre os envolvidos no ato comunicativo.</p>"
      "<p>Isso ocorre com os pronomes destacados no texto, os quais se referem, respectivamente, a</p>")

AQUAMAN = ('<p class="chamada">Leia o texto para responder às questões 05 e 06.</p>'
           '<p class="apoio">Estamos longe de compreender a complexidade dos oceanos. Nesse sentido, Aquaman, herdeiro do trono de Atlantis, está entre os super-heróis que mais têm conhecimento sobre essa parte do nosso planeta. Além disso, o personagem já apareceu em filmes promovendo a coexistência entre diferentes povos, bem como a preservação do meio ambiente.' + A +
           'Nas suas histórias, existem relatos de que o herói é capaz de atingir a velocidade de 3 mil metros por segundo quando está nadando, o que exigiria um gasto de 240 milhões de quilocalorias a cada segundo.</p>')
P5 = "<p>Cada alternativa apresenta um resumo biográfico. Assinale aquela em que se identifica a mesma mensagem positiva defendida pelo Aquaman em filmes, conforme descrito no texto.</p>"

TEIA = '<p class="chamada">Analise o diagrama para responder às questões 08 e 09.</p>[[fig:1]]'
P8 = ("<p>As relações alimentares entre os diversos organismos de um ecossistema costumam ser representadas por meio de diagramas denominados teias alimentares, ou redes alimentares. Essas teias são compostas de diversas cadeias interligadas por meio de setas, que unem os componentes da comunidade entre si, evidenciando suas relações quanto aos diferentes níveis tróficos.</p>"
      "<p>Considerando a teia alimentar representada, é correto afirmar que</p>")

CARBONO = ('<p class="chamada">Leia o texto para responder às questões 13 e 14.</p>'
           '<p class="apoio">Uma das importâncias dos oceanos está no sequestro de carbono, que ocorre de forma natural quando o carbono é capturando a partir da absorção de CO<sub>2</sub>.' + A +
           'Essa absorção pode ser:' + A +
           '→ física: devido à circulação das águas oceânicas causada pela diferença de densidade entre as massas de água. Essa circulação é relacionada às alterações na densidade de uma massa de água por causa do seu aquecimento/resfriamento; e dos processos de evaporação, de precipitação (chuva, neve); da influência de descarga fluvial e da formação de gelo na superfície do oceano, que alteram a salinidade da água. Essa movimentação é predominante no oceano profundo e não transporta somente água, mas também calor, sal, oxigênio, dióxido de carbono, nutrientes e outras propriedades.' + A +
           '→ biológica: em que o fitoplâncton retira CO<sub>2</sub> da água do oceano para realizar o processo da fotossíntese. Alguns animais marinhos convertem o bicarbonato, formado pela reação do CO<sub>2</sub> com água, em carbonato de cálcio (CaCO<sub>3</sub>), presente em conchas e em recifes de corais.</p>'
           '<p class="fonte">&lt;https://tinyurl.com/89kypyvr&gt; Acesso em: 13.09.2022. Adaptado.</p>')
P13 = "<p>Sobre o processo de absorção física de sequestro de carbono, é correto afirmar que ocorre, predominantemente,</p>"

SAL = ('<p class="chamada">Leia o texto para responder às questões 21 e 22.</p>'
       + R[21]["enunciado"].split("[[FIG:p13-1]]")[-1].split("<p>De acordo")[0])
P21 = "<p>De acordo com o texto, é correto afirmar que</p>"

GOLFINHO = ('<p class="chamada">Leia o texto para responder às questões 31 e 32.</p>'
            '<p class="apoio">Golfinhos são exemplos de animais que utilizam a ecolocalização para detectar obstáculos em ambientes pouco iluminados. Esses animais emitem ondas sonoras cuja frequência os seres humanos não conseguem ouvir. Essas ondas são refletidas quando surgem obstáculos à frente, possibilitando a estimativa de distância, tamanho, velocidade e até mesmo textura de objetos que possuam dimensões iguais ou maiores do que o comprimento de onda da onda emitida por eles.' + A +
            'Na propagação das ondas, verificamos que existe uma relação fundamental entre o comprimento de onda (λ), a frequência de vibração (f) e a velocidade de propagação (v): v = λ · f.' + A +
            'Se considerarmos uma onda sonora se propagando na água, a velocidade de propagação será de aproximadamente 1400 m/s. Por exemplo, uma onda cuja frequência de vibração seja de 7 000 Hz terá um comprimento de onda igual a 0,2 m, ou seja, 1400 : 7 000 = 0,2 m.</p>')
P31 = "<p>Se um golfinho emitir ondas sonoras com frequência de 100 000 Hz, ele será capaz de perceber objetos que tenham dimensões, em metros, a partir de</p>"

MANGUE = ('<p class="chamada">Leia o texto para responder às questões 34 e 35.</p>'
          '<p class="apoio"><strong>Texto I</strong><br>Tô enfiado na lama.<br>É um bairro sujo,<br>onde os urubus têm casas<br>e eu não tenho asas,<br>mas estou aqui em minha casa<br>onde os urubus têm asas.<br>Vou pintando, segurando a parede,<br>no mangue do meu quintal Manguetown.</p>'
          '<p class="fonte">CHICO SCIENCE &amp; NAÇÃO ZUMBI. “Manguetown”, in.: Afrociberdelia. Rio de Janeiro: Chaos, 1996. Adaptado.</p>'
          '<p class="apoio"><strong>Texto II</strong><br>Da lama ao caos, do caos à lama (...)<br>Eu vi um chié andando devagar,<br>e um aratu pra lá e pra cá,<br>e um caranguejo andando pro sul,<br>saiu do mangue, virou gabiru.<br>Ô Josué, eu nunca vi tamanha desgraça,<br>quanto mais miséria tem, mais urubu ameaça.</p>'
          '<p class="fonte">CHICO SCIENCE &amp; NAÇÃO ZUMBI. Da lama ao caos. Rio de Janeiro: Chaos, 1994. Adaptado.</p>'
          '<p class="fonte"><strong>Vocabulário</strong><br>Chié: pequeno caranguejo também conhecido como chama-maré.<br>Aratu: outra espécie de caranguejo.</p>')
P34 = "<p>Os trechos apresentados retratam um cenário caracterizado</p>"

CABOS = ('<p class="chamada">Leia o texto para responder às questões 36 e 37.</p>'
         '<p class="apoio">Existe, no fundo dos oceanos, uma rede de cabos submarinos que viabilizam serviços de comunicação. O primeiro cabo submarino transatlântico metálico data de 1858 e ligava a Inglaterra à América do Norte. Ele permitia o envio de duas palavras por minuto. Contudo, hoje existem cerca de 436 cabos espalhados pelos oceanos, somando aproximadamente 1,3 milhão de quilômetros, e que têm capacidade de transmitir até ⬤ trilhões de palavras por segundo.</p>')
P36 = ("<p>No texto, houve um erro de impressão, uma vez que, no lugar da mancha, deveria ter sido impresso um número.</p>"
       "<p>Admita que esse número é a solução da equação: 4(n + 6) = 5n – (28 – 3n)</p>"
       "<p>Assinale a alternativa que apresenta o valor que deveria estar no lugar onde aparece ⬤.</p>")

Q = {
1: {"materia": "Português", "assunto": "Coesão e referência", "tags": [I],
    "enunciado": OCEANO + P1,
    "explicacao": "<p>“<strong>Você</strong>” se dirige a quem lê: o <strong>leitor</strong>. Em “Os oceanos <strong>nos</strong> alimentam”, “nos” inclui quem escreve e quem lê: <strong>leitores e autor</strong>. Em “o oxigênio <strong>que</strong> respiramos”, o “que” retoma <strong>oxigênio</strong>. E em “Apesar de <strong>sua</strong> importância”, “sua” se refere aos <strong>oceanos</strong>. Alternativa <strong>A</strong>.</p><p>As outras alternativas erram pelo menos um referente: “você” não é o oceano nem o autor (B e E), “que” não retoma “clima” nem “parte” (C e D), e “sua” não se refere a “ameaças” nem à “Terra”.</p>"},
2: {"materia": "Português", "assunto": "Gêneros textuais",
    "apoio_de": (1, P1),
    "enunciado": "<p>Para alcançar o objetivo comunicativo de um texto, várias estratégias são utilizadas. Elas são escolhidas levando-se em consideração os elementos formadores do ato de comunicação, como o público-alvo, o contexto social, o código de composição e o canal de circulação da mensagem.</p><p>Com base nessas informações, assinale a alternativa que apresenta uma análise correta sobre o texto lido.</p>",
    "explicacao": "<p>O texto faz perguntas diretas ao leitor (“Você sabia...?”, “Como as mudanças climáticas afetam você?”) e usa linguagem próxima, informal (“Conte pra gente!”). Isso chama a atenção e faz o leitor refletir. Alternativa <strong>C</strong>.</p><p>O presente indica fatos atuais, não verdades imutáveis (A). A linguagem é simples e acessível, para o público em geral (B). O texto informa e convida à ação; não narra (D). E as hashtags são próprias das redes sociais, onde o texto circula (E).</p>"},
3: {"materia": "Português", "assunto": "Gêneros textuais",
    "apoio_de": (1, P1),
    "enunciado": "<p>Gênero textual é um conceito adotado para definir os textos que circulam em nossa sociedade. Cada gênero cumpre uma função diferente e deve se adequar ao contexto comunicativo em que está inserido.</p><p>Analisando o texto apresentado, conclui-se corretamente que se trata de</p>",
    "explicacao": "<p>O texto apresenta dados sobre os oceanos e convida o público a agir (“#HoraDeAgir”, “Cuidar dos oceanos é cuidar do clima e da vida”). É uma <strong>campanha social</strong>, que quer mobilizar as pessoas para proteger os oceanos. Alternativa <strong>E</strong>.</p><p>Ele não narra um fato recente, como a notícia (A); não tem a linguagem objetiva de uma enciclopédia, já que conversa com o leitor (B); não é uma crônica com comentários pessoais (C); e não vende nenhum produto (D).</p>"},
4: {"materia": "Geografia", "assunto": "Hidrografia",
    "explicacao": "<p>O texto diz que “a diferença entre os mares e os oceanos está na sua extensão territorial”: os mares “são menores” e os oceanos “ocupam grandes extensões”. Alternativa <strong>E</strong>.</p><p>Fechados, continentais e abertos são tipos de <strong>mares</strong> (A). Os oceanos são mais profundos, e o ponto mais fundo nunca foi alcançado (B). O texto afirma que mar e oceano <strong>não</strong> são sinônimos (C). E são os oceanos que concentram a maior parte da água da Terra (D).</p>"},
5: {"materia": "Projeto de vida", "assunto": "Ética e cidadania", "tags": [I],
    "enunciado": AQUAMAN + P5,
    "explicacao": "<p>O texto diz que o Aquaman promove a <strong>coexistência entre diferentes povos</strong> e a <strong>preservação do meio ambiente</strong>. Bruno Pereira dedicou-se aos povos indígenas e à Floresta Amazônica, unindo as duas causas. Alternativa <strong>E</strong>.</p><p>Getúlio Vargas é lembrado pelos direitos trabalhistas (A); Maria Esther Bueno, pela superação no esporte (B); César Cielo, pelas medalhas na natação (C); e a Princesa Isabel, pelas leis abolicionistas (D). Nenhum deles une a convivência entre povos à preservação ambiental.</p>"},
6: {"materia": "Matemática", "assunto": "Razão e proporção", "tags": [I],
    "apoio_de": (5, P5),
    "explicacao": "<p>Primeiro, a velocidade do marlim em m/s: \\(129\\ \\text{km/h} \\div 3{,}6 \\approx 35{,}8\\) m/s.</p><p>Se a 3 000 m/s o gasto é de 240 milhões de kcal por segundo, a proporção direta dá: \\(\\dfrac{240}{3000} \\times 35{,}8 = 0{,}08 \\times 35{,}8 \\approx 2{,}9\\) milhões de kcal por segundo. Alternativa <strong>A</strong>.</p><p>Esquecer de converter km/h para m/s leva a \\(0{,}08 \\times 129 \\approx 10{,}3\\) (C).</p>"},
7: {"materia": "Física", "assunto": "Pressão", "tags": [I],
    "explicacao": "<p>A força de arrasto aumenta com a densidade da água, e a densidade aumenta com a profundidade. Para sofrer menos arrasto e gastar menos energia na mesma velocidade, o Aquaman deve nadar onde a água é menos densa: <strong>perto da superfície</strong>. Alternativa <strong>B</strong>.</p><p>Perto do fundo (A) ou no meio do caminho (D), a água é mais densa. E o jeito de bater pés e braços (C e E) não muda a densidade da água, que é o fator citado no enunciado.</p>"},
8: {"materia": "Biologia", "assunto": "Ecologia",
    "enunciado": TEIA + P8,
    "imagens": [{"arquivo": "q08", "alt": "Diagrama “Teia alimentar marinha”, com setas indo de quem é comido para quem come. Fitoplâncton → zooplâncton, copépodes e krill. Zooplâncton → peixes pequenos. Peixes pequenos → lulas, leões-marinhos e focas. Lulas → leões-marinhos, orcas e pinguins. Krill → focas e baleia-azul. Leões-marinhos → orcas. Focas → orcas."}],
    "explicacao": "<p>As focas comem <strong>krill</strong>, que se alimenta do fitoplâncton: nessa cadeia, elas são consumidoras secundárias. Mas também comem <strong>peixes pequenos</strong>, que comem zooplâncton: nessa outra cadeia, são consumidoras terciárias. Elas ocupam <strong>diferentes níveis tróficos</strong>. Alternativa <strong>C</strong>.</p><p>As lulas são comidas por leões-marinhos, orcas e pinguins, e não o contrário (A). O primeiro nível trófico é o fitoplâncton, que faz fotossíntese (B). Os peixes pequenos comem zooplâncton, não fitoplâncton (D). E pinguins são aves, e no diagrama as orcas não se alimentam deles (E).</p>"},
9: {"materia": "Biologia", "assunto": "Zoologia",
    "enunciado": TEIA + "<p>Em relação aos seres vivos da teia alimentar marinha apresentada, é correto afirmar que</p>",
    "imagens": [{"arquivo": "q08", "alt": "Diagrama “Teia alimentar marinha”, com setas indo de quem é comido para quem come. Fitoplâncton → zooplâncton, copépodes e krill. Zooplâncton → peixes pequenos. Peixes pequenos → lulas, leões-marinhos e focas. Lulas → leões-marinhos, orcas e pinguins. Krill → focas e baleia-azul. Leões-marinhos → orcas. Focas → orcas."}],
    "explicacao": "<p>A baleia-azul é um mamífero <strong>sem dentes</strong>: tem barbatanas na boca que funcionam como um filtro. Ela engole muita água e <strong>filtra</strong> o krill, retirando grandes quantidades de alimento. Alternativa <strong>C</strong>.</p><p>Zooplâncton e copépodes são microscópicos e não produzem o próprio alimento (A). O fitoplâncton faz fotossíntese e precisa de luz, por isso vive perto da superfície (B). Peixes pequenos e lulas não disputam o krill com a baleia e as focas no diagrama (D). E os pinguins comem lulas, segundo a teia (E).</p>"},
10: {"materia": "Projeto de vida", "assunto": "Ética e cidadania",
     "enunciado": enun(R, 10, figs={"p06-1": 1}),
     "imagens": [{"arquivo": "q10", "alt": "Tirinha do Armandinho em três quadros. Ao lado das pernas do pai, o menino, de cabeça baixa, diz: “Às vezes tenho vergonha do meu tênis...”. O pai pergunta: “Na escola, filho?”, e ele responde: “Não, na rua...”. No último quadro, completa: “...quando vejo crianças descalças...”."}],
     "explicacao": "<p>Armandinho sente vergonha de ter tênis quando vê crianças sem nenhum calçado. Ele se coloca no lugar de quem vive em condições piores que as suas: isso é <strong>empatia</strong>. Alternativa <strong>C</strong>.</p><p>Ele se importa com os mais necessitados (A). A vergonha não é de andar diante dos colegas (B) nem de usar um tênis velho (D). E a tirinha não mostra ele doando o tênis (E).</p>"},
11: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade",
     "enunciado": enun(R, 11, figs={"p07-1": 1}),
     "imagens": [{"arquivo": "q11", "alt": "Charge do site Caricatura.ru. Embaixo d'água, um cano despeja esgoto no mar. Peixes com aparência doente nadam entre lixo e pneus no fundo. Um mergulhador com escafandro e uma bolsa do Greenpeace coloca máscaras de oxigênio nos peixes; um deles já nada com uma máscara."}],
     "explicacao": "<p>A charge mostra esgoto sendo despejado na água, lixo no fundo e peixes doentes, que precisam de máscaras de oxigênio colocadas por um ativista do Greenpeace. Ela representa a <strong>poluição</strong> que ameaça a vida aquática e a necessidade de <strong>intervenções de proteção</strong>. Alternativa <strong>D</strong>.</p><p>Os peixes não estão em segurança (A). Não há sinais de vazamento nuclear, e há uma ONG atuando (B). A cena não é de uma sociedade sustentável (C). E a charge não fala em alterar o curso de rios nem em poluição do ar (E).</p>"},
12: {"materia": "Geografia", "assunto": "Tectônica de placas",
     "enunciado": "<p>Leia a definição de tsunâmi, extraída do site da Comissão Brasileira de Sítios Geológicos (SIGEP).</p>"
                  '<p class="apoio">Grande onda ou sucessão de ondas marinhas que se deslocam através do oceano por milhares de quilômetros em alta velocidade (podem viajar a mais de 700 km/h). Caracteriza-se por ter grande extensão, chegando a ter mais de 100 km de comprimento, nas linhas da costa pode elevar-se a grande altura, (de 30 metros a 40 metros), e invadir violentamente as praias.' + A +
                  'Tsunâmi é um dos desastres naturais que podem, com frequência, atingir dimensões catastróficas ao provocar a morte de milhares de pessoas. Um tsunâmi pode ter várias origens.</p>'
                  '<p class="fonte">&lt;https://tinyurl.com/2p8txr42&gt; Acesso em: 10.09.2022. Adaptado.</p><p>Dentre as origens desse fenômeno, é correto citar</p>',
     "explicacao": "<p>Tsunâmis são causados por grandes deslocamentos de água, provocados principalmente por <strong>terremotos no fundo do mar</strong> e por <strong>erupções vulcânicas</strong>. Alternativa <strong>D</strong>.</p><p>O aquecimento das águas (A), a rotação e a translação da Terra (B) e as correntes marítimas (C) não produzem ondas desse tipo. E não existem oceanos no núcleo da Terra (E).</p>"},
13: {"materia": "Geografia", "assunto": "Climatologia", "tags": [I],
     "enunciado": CARBONO + P13,
     "alternativas": {"E": "em águas profundas, devido à circulação da água junto a outras com subâncias como NaCℓ, O<sub>2</sub>, CO<sub>2</sub> e CaCO<sub>3</sub>, em temperatura constante."},
     "explicacao": "<p>O texto diz que a absorção física se deve à circulação causada pela <strong>diferença de densidade</strong> das massas de água, que muda com o aquecimento ou o resfriamento (<strong>temperatura</strong>) e com tudo o que altera a <strong>salinidade</strong>. E que essa movimentação “é predominante no oceano profundo”. Alternativa <strong>D</strong>.</p><p>Ela predomina em águas profundas, não perto da costa (A e C). O transporte de nutrientes é uma consequência da circulação, não sua causa (B). E a temperatura varia; não é constante (E).</p>"},
14: {"materia": "Biologia", "assunto": "Ecologia", "tags": [I],
     "apoio_de": (13, P13),
     "explicacao": "<p>Na absorção biológica, o <strong>fitoplâncton</strong> retira CO<sub>2</sub> da água para fazer <strong>fotossíntese</strong>, processo que produz glicose. Alternativa <strong>A</strong>.</p><p>Os animais convertem bicarbonato <strong>em</strong> carbonato de cálcio, não o contrário (B). Salinidade, gelo, chuva e descarga dos rios fazem parte da absorção física (C e E). E o zooplâncton não faz fotossíntese (D).</p>"},
15: {"materia": "Biologia", "assunto": "Ecologia",
     "enunciado": "<p>Leia a reportagem.</p>"
                  '<p class="apoio">Em 2018, apareceu no oceano Atlântico uma grande faixa de algas marrons que foi chamada de grande cinturão de sargassum (sargaço). Os pesquisadores acreditam que esse fenômeno se deve a uma combinação de vários fatores, dentre os quais podemos citar as mudanças nas correntes marítimas e os padrões de ventos anormais ligados às mudanças climáticas.' + A +
                  'O sargaço — às vezes chamado de floresta tropical dourada flutuante —, quando se dispersa em águas abertas, serve como um importante viveiro para filhotes de tartarugas e um refúgio para centenas de espécies de peixes.' + A +
                  'No entanto, ele chega a prejudicar a passagem dos navios, tanto pelos problemas que acarreta para suas hélices e para seus motores, como pelo bloqueio ao deslizamento dos cascos.' + A +
                  'Outro problema surge quando o sargaço chega às praias e começa a apodrecer, emitindo sulfeto de hidrogênio, um gás que cheira a ovo podre e cuja exposição tem sido associada a sintomas neurológicos, digestivos e respiratórios.' + A +
                  'Em partes do México e do Caribe, moradores da região estão transformando o sargaço em papel, sabão, cosméticos, material de construção e biocombustíveis.</p>'
                  '<p class="fonte">&lt;https://tinyurl.com/h9p4f3f8&gt; Acesso em: 17.09.2022. Adaptado.</p>'
                  "<p>Sobre o fenômeno descrito no texto, é correto afirmar que</p>",
     "explicacao": "<p>O texto diz que o sargaço prejudica os navios, “pelos problemas que acarreta para suas hélices e para seus motores”, e que, ao apodrecer nas praias, emite um gás com cheiro de ovo podre. Alternativa <strong>C</strong>.</p><p>O texto cita correntes marítimas e ventos, e a fotossíntese consome gás carbônico, em vez de produzi-lo (A). Algas não têm caules, raízes e folhas verdadeiros (B). O texto não fala em antibióticos, vinho ou saquê (D). E a maré vermelha é causada por outras algas, microscópicas (E).</p>"},
16: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade",
     "enunciado": '<p class="apoio">A segunda Conferência dos Oceanos das Nações Unidas (UNOC), que ocorreu de 27 de junho a 01 de julho de 2022, em Lisboa, teve como objetivo mobilizar o apoio global para conservar e utilizar, de uma forma sustentável, os mares, os oceanos e os recursos marinhos.' + A +
                  'Entre as inúmeras preocupações dos cientistas e dos participantes dessa conferência, destacaram-se:' + A +
                  '→ a restauração e a manutenção dos estoques de peixes, reconhecendo que um oceano saudável é uma parte importante do sistema alimentar; e' + A +
                  '→ a prevenção, a redução e o controle da poluição marinha de todos os tipos, incluindo a poluição plástica e os riscos relacionados à mineração em alto-mar.</p>'
                  "<p>A partir das informações apresentadas, pode-se concluir corretamente que</p>",
     "explicacao": "<p>A conferência se preocupou em manter os <strong>estoques de peixes</strong>. A pesca predatória é justamente retirar peixes mais rápido do que eles conseguem se reproduzir e repor a população. Alternativa <strong>D</strong>.</p><p>Crustáceos e ostras retiram carbono da água ao formar suas carapaças e conchas, sem acelerar as mudanças climáticas (A). Metais pesados se acumulam e prejudicam os animais (B). A poluição da mineração é nociva, não benéfica (C). E os plásticos permanecem centenas de anos no ambiente (E).</p>"},
17: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade",
     "explicacao": "<p>O problema é o esgoto <strong>sem tratamento</strong>. A melhor solução é <strong>tratar o esgoto</strong> antes de lançá-lo no mar. Alternativa <strong>E</strong>.</p><p>Despejar o esgoto em rios (A), lençóis freáticos (B), lagoas costeiras (C) ou lagos de hidrelétricas (D) só leva a poluição para outro lugar, e muitas vezes ela acaba chegando ao mar do mesmo jeito.</p>"},
18: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade",
     "explicacao": "<p>Trocar descartáveis por produtos <strong>reutilizáveis</strong> diminui o lixo, inclusive o plástico, que acaba no mar. Alternativa <strong>C</strong>.</p><p>Microplásticos não servem de alimento: intoxicam os animais (A). Descartar recicláveis em locais inadequados atrapalha a reciclagem (B). Sacolas plásticas poluem os mares (D). E mais descartáveis significam mais lixo (E).</p>"},
19: {"materia": "História", "assunto": "Grandes Navegações",
     "enunciado": '<p class="apoio">“Grandes Navegações” é a expressão usada para se falar da exploração do Oceano Atlântico, feita de maneira pioneira por Portugal e Espanha ao longo dos séculos XV e XVI. O pioneirismo foi resultado de condições políticas, comerciais e geográficas específicas destes países. Com o tempo, outros países da Europa também se lançaram à exploração do Oceano Atlântico.</p>'
                  '<p class="fonte">&lt;https://tinyurl.com/yuxyeapk&gt; Acesso em: 16.09.2022. Adaptado.</p><p>Entre as consequências das Grandes Navegações, estão</p>',
     "explicacao": "<p>As Grandes Navegações levaram Portugal e Espanha a dividir as terras descobertas pelo <strong>Tratado de Tordesilhas</strong> (1494) e trouxeram os portugueses ao território do atual Brasil, em 1500. Alternativa <strong>E</strong>.</p><p>Portugal também dominava rotas no Atlântico, e as condições específicas citadas são as dos países ibéricos, não impostas às colônias (A). A Antártida não foi colonizada, e a Oceania era habitada (B). O Tratado de Madri é de 1750 (C). E a Guerra dos Cem Anos foi antes das Grandes Navegações (D).</p>"},
20: {"materia": "Matemática", "assunto": "Porcentagem", "tags": [I],
     "enunciado": "<p>Há milhares de anos, o transporte marítimo tem sido fundamental para o comércio. Hoje a maior parte do comércio internacional é feita por vias marítimas.</p>[[fig:1]]"
                  '<p class="fonte">&lt;https://tinyurl.com/3rscaf7z&gt; Acesso em: 11.09.2022. Original colorido.</p>'
                  "<p>Os gráficos apresentam a participação dos meios de transporte no comércio mundial. Esses dados são obtidos de acordo com o uso de cada um deles no translado das exportações.</p>"
                  "<p>Analisando os gráficos, o percentual do comércio mundial realizado por meio de transporte marítimo,</p>",
     "imagens": [{"arquivo": "q20", "alt": "Gráfico de barras empilhadas “Comércio mundial por meio de transporte (participação nos serviços de transporte de exportação)”. Em 2010: marítimo 67,5%, aéreo 10,3% e outros 22,2%. Em 2019: marítimo 57,0%, aéreo 11,9% e outros 31,1%. Fonte: World Trade Statistical Review 2020."}],
     "explicacao": "<p>Em 2010, o marítimo foi 67,5%. A soma do aéreo e dos outros foi 10,3 + 22,2 = 32,5%, e o dobro disso é 65%. Como 67,5 &gt; 65, o marítimo foi <strong>maior que o dobro</strong>. Alternativa <strong>A</strong>.</p><p>O triplo dos outros transportes em 2010 seria 66,6%, e não 67,5% (B). De 2010 para 2019, o marítimo <strong>diminuiu</strong> 10,5 pontos (C). Em 2019, o quíntuplo do aéreo seria 59,5%, mais que os 57% do marítimo (D). E a soma dos outros em 2019 foi 43%: o marítimo foi 14 pontos <strong>maior</strong>, não menor (E).</p>"},
21: {"materia": "Biologia", "assunto": "Fisiologia humana", "tags": [I],
     "enunciado": SAL + P21,
     "alternativas": {"A": "glândula tireoide sintetiza hormônios sem a utilização do micronutriente iodo, a fim de garantir a manutenção da temperatura corporal e a ocorrência de bócio ou papo.",
                      "B": "os hormônios T<sub>3</sub> e T<sub>4</sub>, produzidos pela tireoide, prejudicam o crescimento físico e neurológico, assim como a manutenção do fluxo normal de energia no corpo.",
                      "C": "a iodação do sal para consumo humano no Brasil deve ser suspensa, principalmente para crianças e idosos, a fim de manter a baixa prevalência de DDI.",
                      "E": "uma criança com deficiência de iodo pode apresentar, em seu desenvolvimento, baixo crescimento dos ossos e deficiência intelectual."},
     "explicacao": "<p>O texto diz que, em crianças, a falta de iodo pode causar “deficiência intelectual, desenvolvimento físico prejudicado e surdez”. O baixo crescimento dos ossos faz parte do desenvolvimento físico prejudicado. Alternativa <strong>E</strong>.</p><p>A tireoide <strong>precisa</strong> do iodo para fazer seus hormônios, e o bócio é um sintoma da falta dele (A). Os hormônios T<sub>3</sub> e T<sub>4</sub> <strong>atuam</strong> no crescimento e no metabolismo, sem prejudicá-los (B). A iodação é obrigatória justamente para diminuir os casos de DDI (C e D).</p>"},
22: {"materia": "Química", "assunto": "Separação de misturas",
     "apoio_de": (21, P21),
     "explicacao": "<p>Nas salinas, a água do mar passa para o estado gasoso e deixa o sal: é uma mudança de estado, um processo <strong>físico</strong>, chamado <strong>vaporização</strong> (no caso, uma evaporação lenta, pelo sol e pelo vento). Alternativa <strong>A</strong>.</p><p>Filtração (B) e decantação (C) separam sólidos que não estão dissolvidos. Evaporação e ebulição (D e E) são tipos de vaporização, mas são processos físicos, não químicos.</p>"},
23: {"materia": "Química", "assunto": "Interpretação de dados", "tags": [I],
     "enunciado": '<p class="apoio">A Agência Nacional de Vigilância Sanitária (Anvisa) é quem estabelece a faixa de iodação do sal de cozinha no Brasil. Essa adição deve ficar entre 15 e 45 miligramas por quilograma de sal de cozinha, NaCℓ.</p>'
                  '<p class="fonte">&lt;https://tinyurl.com/46svyad9&gt; Acesso em: 15.09.2022. Adaptado.</p>'
                  "<p>No preparo de um alimento, foi adicionado 1,5 g de NaCℓ. De acordo com o valor estabelecido pela Anvisa para a iodação do sal de cozinha, a quantidade mínima de iodo, em mg, adicionada ao alimento, foi</p>",
     "explicacao": "<p>O mínimo é 15 mg de iodo por quilograma de sal. 1,5 g = 0,0015 kg. Então: \\(15 \\times 0{,}0015 = 0{,}0225\\) mg, cerca de <strong>0,02 mg</strong>. Alternativa <strong>B</strong>.</p><p>1,50 (C) e 4,50 (E) não convertem gramas em quilogramas. E 0,01 (A) não corresponde à conta.</p>"},
24: {"materia": "Química", "assunto": "Estrutura atômica",
     "enunciado": '<p class="apoio">O iodo é um elemento químico que apresenta número de massa 127 e número atômico 53.' + A +
                  "Na Química, pode ser representado da seguinte maneira: \\({}^{127}_{53}I\\).</p>"
                  "<p>A partir das informações dadas para o elemento iodo, pode-se afirmar, corretamente, que apresenta</p>",
     "explicacao": "<p>O número atômico (53) é o número de <strong>prótons</strong>. Alternativa <strong>A</strong>.</p><p>O número de nêutrons é 127 − 53 = 74, e não 53 (B) nem 127 (E). Num átomo neutro, o número de elétrons é igual ao de prótons: 53, e não 74 (C). E são 53 prótons, não 74 (D).</p>"},
25: {"materia": "Português", "assunto": "Figuras de linguagem", "tags": [I],
     "enunciado": enun(R, 25, figs={"p15-1": 1}).replace("e no, sentido conotativo", "e no, sentido conotativo"),
     "imagens": [{"arquivo": "q25", "alt": "Quadrinho “Cientirinhas #249”, em quatro quadros. 1: um peixe-gota, mole e caído, numa bancada de peixaria: “O peixe-gota não é tão feio como dizem.” 2: “Ele só fica com essa aparência inchada e gelatinosa depois que é trazido à superfície.” 3: o peixe nadando no fundo do mar, com forma normal de peixe: “Onde ele vive, nas profundezas oceânicas, é um peixe bem bonito.” 4: o peixe, com cara séria, diz: “A gente vive sob muita pressão para conseguir se adequar a seus padrões de beleza.”"}],
     "explicacao": "<p>No sentido literal, “pressão” é a força da água sobre o peixe no fundo do mar, que o deixa com forma de peixe. No sentido figurado, a fala “A gente vive sob muita pressão para conseguir se adequar a seus padrões de beleza” critica a cobrança da sociedade sobre a aparência. Alternativa <strong>D</strong>.</p><p>A aparência do peixe dentro ou fora da água (A e B) e a dilatação no fundo do mar (E) não são sentidos figurados. E a aparência gelatinosa não é uma defesa contra predadores (C).</p>"},
26: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade",
     "explicacao": "<p>O texto termina dizendo que “o conhecimento sobre o maior ambiente da Terra deve ser amplamente disseminado para que a sociedade entenda sua importância”. Alternativa <strong>D</strong>.</p><p>O texto destaca a segurança de quem trabalha no oceano (A). Diz que os benefícios devem ser compartilhados “com a sociedade”, sem falar da ONU (B), de empresas privadas (C) ou de guardar o conhecimento nas universidades (E).</p>"},
27: {"materia": "História", "assunto": "Antiguidade",
     "explicacao": "<p>O texto diz que o Mediterrâneo “era o principal meio de interação” entre os povos antigos, que se deslocavam mais pelo mar do que por terra, e que suas culturas são “frutos de um conjunto de intersecções”. Alternativa <strong>D</strong>.</p><p>“Cimento líquido” significa que o mar <strong>unia</strong> os povos, e não que os separava (A e B). Eles preferiam o mar às rotas terrestres (C). E o texto diz que as culturas <strong>não</strong> são “puras” (E).</p>"},
28: {"materia": "Física", "assunto": "Pressão",
     "explicacao": "<p>A pressão aumenta 1 atm a cada 10 m: a 40 m, são 4 atm da água. Somando a pressão atmosférica ao nível do mar (1 atm): 4 + 1 = <strong>5 atm</strong>. Alternativa <strong>C</strong>.</p><p>4 atm (B) esquece de somar a pressão atmosférica.</p>"},
29: {"materia": "Biologia", "assunto": "Fisiologia humana", "tags": [I],
     "explicacao": "<p>O texto diz que o problema aparece quando a pressão diminui de forma <strong>muito rápida</strong>. Por isso, o mais seguro é <strong>subir devagar</strong>, para a pressão variar pouco ao longo do tempo e os gases saírem do sangue aos poucos. Alternativa <strong>E</strong>.</p><p>Mergulhar mais fundo aumenta a quantidade de gás acumulada (A). Exames de pressão sanguínea não evitam a doença (B). Acelerar a subida, mesmo na metade final, aumenta o risco (C e D).</p>"},
30: {"materia": "História", "assunto": "História contemporânea",
     "enunciado": '<p class="apoio">Não é na manufatura e, sim, na indústria do transporte que iremos encontrar os resultados mais expressivos da influência concentradora da maquinaria. A substituição da carroça e da diligência pela estrada de ferro, do barco à vela pelo navio a vapor, evidencia o maior avanço do capitalismo moderno.</p>'
                  '<p class="fonte">HOBSON, John A.; A evolução do capitalismo moderno: um estudo da produção mecanizada. São Paulo: Ed. Nova Cultural, 1996. P. 130.</p>'
                  "<p>No contexto da Segunda Revolução Industrial, o desenvolvimento dos navios a vapor</p>",
     "explicacao": "<p>Os navios a vapor eram mais rápidos e transportavam mais carga do que os barcos a vela. Isso <strong>reduziu o tempo e o custo do transporte</strong> e permitiu levar matérias-primas e mercadorias a mercados distantes. Alternativa <strong>B</strong>.</p><p>O período foi de urbanização, não de ruralização (A). A indústria se concentrou na Europa e nos Estados Unidos, não na África (C). Operários não eram escravizados, e férias não eram um direito comum na época (D). E a Inglaterra não abandonou a produção de tecidos (E).</p>"},
31: {"materia": "Física", "assunto": "Ondas", "tags": [I],
     "enunciado": GOLFINHO + P31,
     "explicacao": "<p>Pelo texto, o golfinho percebe objetos com dimensões iguais ou maiores que o comprimento de onda. Com \\(v = \\lambda \\cdot f\\): \\(\\lambda = \\dfrac{v}{f} = \\dfrac{1400}{100\\,000} = 0{,}014\\) m. Alternativa <strong>A</strong>.</p><p>0,2 m (D) é o comprimento da onda de 7 000 Hz, dado como exemplo no texto.</p>"},
32: {"materia": "Física", "assunto": "Ondas",
     "enunciado": enun(R, 32, figs={"p19-1": 1}).replace("um id d d ã d d á i t l d golfinho", "um golfinho").replace("um id d d ã d d á i t l d golﬁnho", "um golﬁnho"),
     "apoio_de": (31, P31),
     "imagens": [{"arquivo": "q32", "alt": "Desenho de um golfinho emitindo ondas sonoras, representadas por arcos que se espalham em direção a um pequeno peixe à direita."}],
     "explicacao": "<p>O som vai até o peixe e volta: percorre 2 × 140 = 280 m. Na água, a 1 400 m/s: \\(t = \\dfrac{280}{1400} = 0{,}2\\) s. Alternativa <strong>B</strong>.</p><p>0,1 s (A) é o tempo só da ida, sem a volta do eco.</p>"},
33: {"materia": "História", "assunto": "Escravidão",
     "enunciado": enun(R, 33, ["Em terras brasileiras"]),
     "explicacao": "<p>As culturas africanas, como o culto a Iemanjá, chegaram ao Brasil com os africanos <strong>escravizados</strong>, trazidos à força pelo tráfico negreiro do século XVI ao XIX. Alternativa <strong>E</strong>.</p><p>Não houve migração de brasileiros para a África no século XVI (A). O oceano não impediu o contato, já que o tráfico atravessava o Atlântico (B). A (C) inverte a história e culpa a divindade pela escravidão. E Iemanjá é uma divindade, não governou o Brasil (D).</p>"},
34: {"materia": "Português", "assunto": "Texto literário", "tags": [I],
     "enunciado": MANGUE + P34,
     "explicacao": "<p>Os textos mostram um “bairro sujo”, onde os urubus têm casas, “miséria” e “desgraça”. O urubu e a sujeira reforçam a imagem de <strong>pobreza</strong>. Alternativa <strong>B</strong>.</p><p>Não há prosperidade (A), indústria (C), desenvolvimento (D) nem riqueza de oportunidades (E) no cenário descrito.</p>"},
35: {"materia": "Português", "assunto": "Classes de palavras",
     "apoio_de": (34, P34),
     "explicacao": "<p>Em “<strong>da</strong> lama <strong>ao</strong> caos”, “de” (em “da”) indica o ponto de partida, a <strong>origem</strong>, e “a” (em “ao”) indica o ponto de chegada, o <strong>destino</strong>. Alternativa <strong>C</strong>.</p><p>Os textos estão em primeira pessoa (“Tô enfiado”, “Eu vi”) (A). Os urubus têm asas, o que representa liberdade, e o eu lírico não tem (B). “Quanto mais..., mais...” indica proporção; “embora” indicaria concessão (D). E o gerúndio indica ações em andamento, não concluídas (E).</p>"},
36: {"materia": "Matemática", "assunto": "Operações e problemas",
     "enunciado": CABOS + P36,
     "explicacao": "<p>\\(4(n + 6) = 5n - (28 - 3n)\\)</p><p>\\(4n + 24 = 5n - 28 + 3n\\)</p><p>\\(4n + 24 = 8n - 28\\)</p><p>\\(52 = 4n \\Rightarrow n = 13\\). Alternativa <strong>B</strong>.</p><p>Errar o sinal ao tirar os parênteses (\\(5n - 28 - 3n\\)) leva a \\(4n + 24 = 2n - 28\\), que não dá nenhuma das alternativas positivas.</p>"},
37: {"materia": "Matemática", "assunto": "Notação científica", "tags": [I],
     "apoio_de": (36, P36),
     "alternativas": {"A": "3,0×10<sup>4</sup>.", "B": "3,0×10<sup>3</sup>.", "C": "3,0×10<sup>2</sup>.", "D": "3,0×10<sup>1</sup>.", "E": "3,0×10<sup>0</sup>."},
     "explicacao": "<p>São 1,3 milhão de quilômetros divididos por 436 cabos: \\(\\dfrac{1\\,300\\,000}{436} \\approx 2\\,982\\) km, cerca de \\(3{,}0 \\times 10^3\\) km. Alternativa <strong>B</strong>.</p>"},
38: {"materia": "Biologia", "assunto": "Ecologia", "tags": [I],
     "enunciado": '<p class="apoio">Manguezais são ecossistemas de transição entre ambientes terrestre e aquático, específicos de regiões tropicais e subtropicais, sujeitos aos regimes das marés. No Brasil, ocupam uma área superior a 1 200 000 hectares, que se estendem do litoral do Amapá até o de Santa Catarina.' + A +
                  'A salinidade do solo provocada pelo encontro de águas do mar e do rio, assim como as cheias e as vazantes das marés trazem características singulares para essa vegetação. Em nosso litoral, os manguezais são formados basicamente por três espécies de mangue:' + A +
                  '→ O mangue-vermelho, ou sapateiro. Seu caule, se raspado, apresenta a cor vermelha, vindo daí o nome. É a espécie mais conhecida e de fácil identificação do litoral brasileiro. Foi muito utilizado em curtumes para tingimento de couros.' + A +
                  '→ O mangue-branco, chamado também de tinteira, localiza-se mais para o interior dos manguezais. A casca e as folhas dessa espécie podem ser usadas na medicina popular para tratar de diarreias.' + A +
                  '→ O mangue-preto, canoé, siriúba ou sereíba. É também conhecido pelo uso em construção de canoas de um único tronco.' + A +
                  'Em comum, eles têm raízes pneumatóforas, ou respiratórias, ocorrem em áreas alagadiças e crescem verticalmente para que haja a troca gasosa com a atmosfera, quer dizer, para que as árvores respirem.' + A +
                  'A importância da vegetação dos manguezais está, entre outros fatores, na redução de erosão marinha, uma vez que diminui o impacto de ondas maiores na costa litorânea, além de servir de berçário para a reprodução de muitas espécies marinhas.' + A +
                  'Desde 1965, os manguezais são considerados áreas de preservação permanente em razão de sua importância ecológica. Desde o ano 2000, o dia 26 de julho foi escolhido como Dia Mundial de Proteção aos Manguezais.</p>'
                  '<p class="fonte">&lt;https://tinyurl.com/2vuzbv94&gt; Acesso em: 17.09.2022. Adaptado.</p>'
                  "<p>Em relação aos ecossistemas citados no texto, é correto afirmar que são</p>",
     "explicacao": "<p>O texto diz que os manguezais são “áreas de preservação permanente” desde 1965 e servem de “berçário para a reprodução de muitas espécies marinhas”. Alternativa <strong>D</strong>.</p><p>O mais conhecido é o mangue-vermelho, usado para tingir couros (A). Os manguezais <strong>reduzem</strong> a erosão (B). Eles vão do Amapá até Santa Catarina, passando por todo o litoral entre os dois (C). E Tocantins e Goiás não têm litoral (E).</p>"},
39: {"materia": "História", "assunto": "História contemporânea", "tags": [I],
     "enunciado": "<p>Considere o mapa.</p>[[fig:1]]"
                  '<p class="fonte">&lt;https://tinyurl.com/ync3h8u2&gt; Acesso em: 16.09.2022. Original colorido.</p><p>O evento histórico retratado no mapa é</p>',
     "imagens": [{"arquivo": "q39", "alt": "Mapa do litoral norte da França, no Canal da Mancha. Setas mostram “Tropas americanas” chegando às praias Utah e Omaha e “Tropas inglesas e canadianas” chegando às praias Gold, Juno e Sword. Aparecem as cidades de Cherbourg, Carentan, Bayeux e Caen, linhas da frente dos Aliados com datas (7 junho, 17 junho, 17 julho, 1 agosto), portos artificiais ativados depois do Dia D e as baterias costeiras alemãs da Muralha do Atlântico. Fonte: Reuters."}],
     "explicacao": "<p>O mapa mostra tropas americanas, inglesas e canadenses chegando às praias Utah, Omaha, Gold, Juno e Sword, na Normandia, e cita o “Dia D” e a Muralha do Atlântico alemã. É o <strong>Desembarque na Normandia</strong>, em junho de 1944, na Segunda Guerra Mundial. Alternativa <strong>D</strong>.</p><p>O Bloqueio Continental (A), a Revolução Francesa (C) e a Guerra Franco-Prussiana (E) são do século XVIII ou XIX e não envolveram tropas americanas e canadenses. E a Guerra da Argélia (B) aconteceu no norte da África.</p>"},
40: {"materia": "Matemática", "assunto": "Análise combinatória",
     "enunciado": "<p>Leia a tirinha.</p>[[fig:1]]"
                  '<p class="fonte">&lt;https://tinyurl.com/ys3sz8w5&gt; Acesso em: 14.09.2022. Original colorido.</p>'
                  "<p>No último quadro da tirinha, é possível observar um grupo de peixes de tamanhos diversos, duas plantas aquáticas e duas conchas de formatos diferentes.</p>"
                  "<p>Considere que você irá retirar do aquário um único peixe, uma única planta e uma única concha nessa ordem. Diante disso, então o total de maneiras de realizar essa ação é</p>",
     "imagens": [{"arquivo": "q40", "alt": "Tirinha em três quadros com peixes nadando. 1: “A minha turma me faz bem. Não me sinto um peixe fora d'água quando estou com meu cardume.” 2: “Mas não tenho certeza se nado livremente pelo oceano...” 3: “...ou se estou preso em um aquário que me protege como uma bolha.” No último quadro, o cardume aparece dentro de um aquário redondo, com plantas e conchas no fundo."}],
     "explicacao": "<p>Pelo princípio multiplicativo: (número de peixes) × 2 plantas × 2 conchas. No aquário do último quadro há <strong>8 peixes</strong>, então: \\(8 \\times 2 \\times 2 = 32\\) maneiras. Alternativa <strong>B</strong>.</p><p>Somar em vez de multiplicar (8 + 2 + 2 = 12) leva à (C).</p>"},
}
completar(Q, R)
