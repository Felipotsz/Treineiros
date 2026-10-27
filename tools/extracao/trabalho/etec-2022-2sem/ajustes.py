# Ajustes da conferência humana: Vestibulinho ETEC 2º semestre de 2022 (exame de 03/07/2022)
# Texto conferido com a imagem de cada página (e com o texto extraído do PDF). Gabarito: oficial (2SEM22).
# Tema: profissões, projeto de vida e mundo do trabalho.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import A, carregar, enun, tabela, colunas, completar

META = {
    "id": "etec-2022-2sem",
    "banca": "ETEC",
    "ano": 2022,
    "semestre": 2,
    "titulo": "Vestibulinho ETEC, 2º semestre de 2022",
    "fonte": "Centro Paula Souza",
    "dataExame": "2022-07-03",
    "duracaoMinutos": 240,
    "tema": "Profissões e projeto de vida",
    "apresentacao": "<p>Prezado(a) candidato(a), nesta prova você vai se deparar com diversas áreas de atuação profissional e perspectivas de ações futuras.</p><p>Além disso, serão apresentadas situações sobre protagonismo e valores do pleno exercício da cidadania e do mundo do trabalho.</p><p>Boa prova!</p>",
    "pdf": "assets/provas/etec-2022-2sem.pdf",
}
EXTRAS = {"apresentacao": "Ilustração de uma pessoa diante de um globo, cercada de nuvens com as palavras metas, empatia, visão, habilidades, resiliência, interesses, educação, valores, autonomia e trabalho."}

R = carregar("etec-2022-2sem")
I = "interdisciplinar"


def p(*paragrafos, classe=None):
    abre = f'<p class="{classe}">' if classe else "<p>"
    return "".join(abre + x + "</p>" for x in paragrafos)


def apoio(*paragrafos):
    return '<p class="apoio">' + A.join(paragrafos) + "</p>"


def fonte(t):
    return f'<p class="fonte">{t}</p>'


EMICIDA = ('<p class="chamada">Leia a letra do rap do Emicida para responder às questões de 06 a 09.</p>[[fig:1]]'
           + fonte("<em>A cada vento</em>. Intérprete: Emicida. Compositor: Emicida. <em>In</em>: Pra quem já mordeu cachorro por comida, até que eu cheguei longe. Intérprete: Emicida. [<em>S.l.</em>]: Laboratório Fantasma, 2009. 1 CD, faixa 13.")
           + fonte("*dim: redução informal para “dinheiro”.<br>** <em>stand by</em>: em espera"))
EMICIDA_IMG = {"arquivo": "q06", "alt": "Letra do rap “A cada vento”, de Emicida, com 24 versos numerados de 5 em 5 e dois cortes [...]. Alguns versos estão em negrito. A letra fala de cada dia como uma nova chance de ser melhor, do sol que cruza o horizonte, da esperança levada na mochila, de quem troca sorriso por dinheiro, de não ser enxergado, da fé nos orixás, de quem volta cansado no ônibus, da paz ao deitar a cabeça no travesseiro, de manter perto quem faz bem, de deixar o sofrimento para trás, da paciência de quem junta latinha, focado no que tem, e termina com um alerta: quando eles perceberem o poder que têm, cuidado."}
P6 = p("No texto apresentado, o eu lírico tece reflexões sobre sua vida e sua realidade.", "Algumas delas evidenciam aspectos sociais relevantes, tais como")

JUNIOR = ('<p class="chamada">Leia ao texto para responder às questões 10 e 11.</p>'
          + apoio("O estresse do dia a dia pode incentivar mudanças de rumos na vida profissional.",
                  "É o caso de Júnior, administrador de empresas, que, depois de 10 anos de experiência em grandes companhias, decidiu apostar em seu sonho e se tornar instrutor de paraquedismo. Animado, ele realizou uma pesquisa para descobrir quanto ganha um profissional de paraquedismo, obtendo as informações do quadro.")
          + tabela(["Cidade", "Jornada de trabalho semanal (em horas)", "Valor da hora trabalhada (em reais)", "Salário mensal (em reais)"],
                   [["Boituva, SP", "43", "25", "x"], ["Rio de Janeiro, RJ", "42", "50", "y"], ["Fortaleza, CE", "44", "30", "z"]]))
P10 = p("Considere que um mês tem, em média, uma duração de 4,5 semanas, assim, é correto afirmar que")

EMPREENDER = ('<p class="chamada">Leia o texto para responder às questões de 14 a 16.</p>'
              + apoio("Há três tipos de empreendedorismo: o clássico, o social e o serviço social.",
                      "O empreendedorismo clássico é projetado <strong><u>para</u></strong> gerar lucro financeiro. Desde o início, a expectativa é que o empreendedor e seus investidores obtenham algum ganho financeiro pessoal.",
                      "Um segundo tipo de empreendedorismo é o social, que não tem como prioridade criar lucros financeiros substanciais para seus investidores. O empreendedor social encontra seu maior valor nos benefícios transformadores em maior ou menor escala, que possam ser gerados em um segmento significativo da sociedade ou na sociedade como um todo. Normalmente, a proposta de valor do empreendedorismo social é planejada para uma população carente ou altamente desfavorecida, sem recursos ou influência <strong><u>para</u></strong> conseguir transformar sua vida por conta própria. <strong><u>Porém</u></strong>, um empreendimento social pode gerar renda <strong><u>e</u></strong> pode ser organizado com fins lucrativos.",
                      "O serviço social é uma resposta a um problema social identificado e acolhido com coragem por alguém. Pode se transformar em uma solução para o problema, mas na maioria das vezes isso não acontece, <strong><u>uma vez que</u></strong> este é frequentemente complexo e é gerado fora do escopo da assistência. O serviço social normalmente precisa atrair recursos e sofre com sua vulnerabilidade, pois sem uma base forte de apoio contínuo que o mantenha, ele é naturalmente mais frágil. Ações como a visita de estudantes a lar de idosos, arrecadação de ração para animais abandonados, entre outras, são exemplos de práticas de serviço social.")
              + fonte("&lt;https://tinyurl.com/ncuu54zh&gt; Acesso em: 01.04.2022. Adaptado."))
P14 = p("Elementos de coesão são palavras e locuções utilizadas dentro de um texto para conectar expressões, orações, períodos e parágrafos.", "Sobre os elementos coesivos destacados no texto, é correto afirmar que")

PLASTICO = ('<p class="chamada">Leia o texto para responder às questões de 17 a 21.</p>'
            + apoio("O engenheiro de petróleo detém conhecimento amplo e específico de todas as etapas dos processos de extração de petróleo e de gás. Entre suas atividades principais, está a descoberta e exploração de jazidas de petróleo e de gás natural.",
                    "O petróleo passa por um processo de beneficiamento que leva à obtenção de combustíveis e de matéria-prima usada na produção de diversos materiais, como os plásticos – compostos pertencentes ao grupo dos polímeros (macromoléculas – moléculas muito grandes – com características especiais e variadas).",
                    "A palavra plástico tem origem grega e significa aquilo que pode ser moldado. Os plásticos são produzidos por meio de reações de polimerização e moldados em estruturas utilizáveis, pois “amolecem” facilmente com o aumento da temperatura.",
                    "O politereftalato de etileno (PET), usado em garrafas de refrigerantes, é um deles, e foi desenvolvido em 1941. No Brasil, o uso das embalagens PET está crescendo e substituindo embalagens como: latas de flandres (confeccionada em aço, liga metálica de ferro e carbono, revestido por estanho), vidros e multilaminados (tipo “caixinha longa vida”).")
            + fonte("&lt;https://tinyurl.com/yerezs35&gt; Acesso em: 26.03.2022. Adaptado."))
P17 = p("De acordo com o texto, os plásticos são")

PAINEL = ('<p class="chamada">Leia ao texto para responder às questões 30 e 31.</p>'
          + apoio("Fernanda estuda Design de Interiores na Etec Albert Einstein. Como parte de um trabalho desenvolvido em seu curso, ela planejou a fixação de um painel retangular decorativo composto por espelhos. As dimensões do painel estão indicadas na figura, sendo x e y positivos.")
          + "[[fig:1]]" + apoio("<strong>OBSERVAÇÃO</strong><br>Para todos os cálculos, despreze a necessidade de deixar espaços entre os espelhos ao formar o painel."))
PAINEL_IMG = {"arquivo": "q30", "alt": "Painel retangular de espelhos visto em perspectiva, formado por quatro fileiras de espelhos retangulares, encaixados como tijolos. A largura total do painel é indicada como 3x e a altura como y. A fileira de baixo tem quatro espelhos inteiros."}
P30 = p("Assinale a alternativa que apresenta as expressões algébricas da área e do perímetro do painel decorativo de espelhos.")

SABAO = ('<p class="chamada">Leia o texto para responder às questões 40 e 41.</p>'
         + apoio("Uma excelente medida de higienização é lavar as mãos com água e sabão.",
                 "O segredo está nas características de cada uma das extremidades das estruturas do sabão, denominadas de cabeça e cauda (no infográfico, indicadas como moléculas de sabão). A cabeça tem afinidade com água, enquanto a cauda tem afinidade com gordura. Em outras palavras, a estrutura do sabão é atraída pela água de um lado, e por óleo ou gordura do outro.",
                 "Quando ensaboamos as mãos, as estruturas do sabão atraem a gordura da superfície das mãos, a qual será completamente cercada por outras estruturas desse sabão. A gordura é, então, separada em pedaços cada vez menores que serão arrastados pela água corrente.",
                 "Temos, agora, mãos limpas e higienizadas!",
                 "No caso do coronavírus, que apresenta uma “capa” protetora lipídica (uma membrana de gordura) e proteínas, a ação do sabão promove o rompimento dessa “capa”, fragmentando o vírus, conforme apresentado no infográfico. Assim, a água arrasta os “pedaços” do vírus, evitando que sejamos infeccionados.")
         + "[[fig:1]]" + fonte("Fonte do infográfico: &lt;https://tinyurl.com/yz3xmp43&gt; Acesso em: 30.03.2022. Original colorido."))
SABAO_IMG = {"arquivo": "q40", "alt": "Infográfico “Como o sabão destrói o coronavírus”, da BBC, em três partes. 1: o vírus, uma esfera envolta em uma membrana lipídica (de gordura) que protege seu material genético, com proteínas na superfície que o ajudam a infectar as células humanas. 2: moléculas de sabão, cada uma com uma cabeça hidrofílica, que interage com a água, e uma cauda hidrofóbica, que interage com os óleos e a gordura. 3: as caudas das moléculas de sabão se conectam com a membrana lipídica do vírus e a rompem; as proteínas e outros fragmentos do vírus são arrastados pela água."}
P40 = p("Sobre a ação do sabão, é correto afirmar que")

POTTER = ('<p class="chamada">Leia o texto para responder às questões de 42 a 44.</p>'
          + apoio("– Sente-se, Potter – disse a Prof.ª McGonagall <strong><u>secamente</u></strong>.",
                  "– Bom, Potter, esta reunião é para discutirmos as ideias <strong><u>sobre</u></strong> carreiras que você já tenha, e ajudá-lo a decidir que disciplinas você deve fazer no sexto e sétimo anos – começou McGonagall.",
                  "– Você já pensou no que gostaria de fazer quando terminasse Hogwarts?",
                  "– Bom, pensei, <strong><u>talvez</u></strong>, em ser auror – murmurou Harry.",
                  "– Você precisaria de notas excelentes para isso – disse a Prof.ª McGonagall – Exige-se um mínimo de cinco N.I.E.M.s (os Níveis Incrivelmente Exaustivos em Magia), e nenhuma nota abaixo de “Excepcional”, pelo que vejo. Depois você teria de passar por uma série de testes rigorosos de <strong><u>caráter</u></strong> e <strong><u>aptidão</u></strong>, na Seção de Aurores. É uma carreira difícil, Potter, em que somente se aceitam os melhores.")
          + fonte("ROWLING, J. K. <em>Harry Potter e a Ordem da Fênix</em>. Rio de Janeiro, Rocco, 2003, p. 365. Adaptado."))
P42 = p("Releia atentamente a passagem apresentada, observando o contexto de ocorrência dos termos em destaque.", "Assinale a alternativa que apresenta, respectivamente, sinônimos adequados às palavras destacadas.")

POTE = ('<p class="chamada">Leia a resenha do livro <em>O Pote Vazio</em>, de Demi, publicado pela editora Martins Fontes, para responder às questões 49 e 50.</p>'
        + apoio("<em>O Pote Vazio</em>, de Demi é uma fábula voltada para crianças, porém é válida para pessoas de todas as idades. Nela, descreve-se que, há muito tempo na China, vivia um menino chamado Ping, que adorava flores e tudo que plantava floria lindamente.",
                "O imperador, em busca de um herdeiro para seu trono, dá uma semente de flor a cada menino do reino com esta orientação:",
                "“Quem provar que fez o melhor possível dentro de um ano, será meu sucessor!”",
                "Ping cuida de sua semente o ano todo, mas a planta não brota e seu pai o conforta dizendo:",
                "“Você fez o melhor que pôde e o possível deve ser apresentado ao imperador”.",
                "Quando se apresentou ao imperador, declarou que fez o melhor possível, mas a planta não brotou, por isso trouxe o pote vazio. Enquanto ouvia o garoto que envergonhado falava, um sorriso brotava no rosto do imperador, que no final o abraçou e declarou:",
                "“Encontrei, encontrei alguém que merece ser imperador, não sei onde vocês encontraram essas sementes, mas as sementes que dei a vocês estavam todas queimadas e nenhuma poderia ter brotado. Admiro sua coragem de aparecer na frente do imperador trazendo a verdade e vou recompensá-lo tornando-o imperador”.")
        + fonte("&lt;https://tinyurl.com/yc8k8bxn&gt; Acesso em: 25.03.2022. Adaptado."))
P49 = p("De acordo com a fábula,")

PIZZA = "Gráfico de pizza dividido em {n} partes iguais, com {s} partes pintadas (N.I.E.M.s cursados) e {b} em branco (não cursados)."

Q = {
1: {"materia": "Matemática", "assunto": "Porcentagem", "tags": [I],
    "enunciado": p("Leia a reportagem.")
                 + apoio("Entre as vantagens listadas por estudantes, ao optar pelo ensino técnico, estão o tempo de formação mais rápido; seu excelente nível de especialização; e a preparação voltada às necessidades do mercado de trabalho. Além disso, há o fato de que essa modalidade de educação promove habilidades socioemocionais, como a empatia, e também estreita laços com professores.",
                         "“São professores que nos levam para escolhas além das nossas vidas”, diz um aluno de uma escola técnica com 600 alunos matriculados no momento da entrevista. Contudo a luta dos professores, dessa unidade, é contra a evasão escolar acentuada pela pandemia da COVID–19.")
                 + fonte("&lt;https://tinyurl.com/khuns23z&gt; Acesso em: 26.03.2022. Adaptado.")
                 + p("Suponha que, no momento da entrevista, a unidade escolar mencionada no texto registrava um índice de evasão escolar de cerca de 30 % em relação aos alunos matriculados no início do ano letivo.",
                     "Logo, o número de alunos matriculados no início do mesmo ano, nessa unidade escolar, era aproximadamente"),
    "explicacao": "<p>Se 30% dos alunos saíram, os 600 que ficaram correspondem a 70% dos matriculados no início do ano. Então: \\(0{,}7 \\times N = 600 \\Rightarrow N = \\dfrac{600}{0{,}7} \\approx 857\\), cerca de <strong>860</strong> alunos. Alternativa <strong>D</strong>.</p><p>O erro mais comum é somar 30% a 600 (600 × 1,3 = 780) ou calcular 30% de 600 e subtrair, chegando a valores que não estão nas alternativas. 630 (E) seria 600 + 30.</p>"},
2: {"materia": "Geografia", "assunto": "Industrialização brasileira",
    "explicacao": "<p>Pelo próprio texto, o desemprego <strong>estrutural</strong> é causado pela introdução de novas tecnologias para reduzir custos: máquinas e robôs passam a fazer o trabalho de pessoas. Alternativa <strong>B</strong>.</p><p>O desemprego que vai e volta com a situação da economia é o conjuntural, não o estrutural (A). O conjuntural <strong>aumenta</strong> nas crises e diminui quando a economia vai bem (C). Ele não depende da destruição de máquinas (D). E os dois tipos são diferentes, como o texto mostra (E).</p>"},
3: {"materia": "Biologia", "assunto": "Ecologia",
    "enunciado": apoio("Os agrônomos e os técnicos em agronomia podem trabalhar no acompanhamento do cultivo e da colheita de safras a fim de aumentar a produtividade por meio da seleção de sementes, do emprego de fertilizantes e do combate a pragas.",
                       "O controle biológico de pragas é uma técnica que cresce com bastante eficiência dentro do meio agrícola visando diminuir a necessidade de utilização de agrotóxicos a fim de evitar a contaminação do solo, da água e dos próprios seres humanos.",
                       "Um exemplo de controle biológico é a utilização de joaninhas, insetos predadores que se alimentam de pulgões e cochonilhas, pragas presentes em algumas culturas de hortaliças e árvores frutíferas.")
                 + p("A técnica de controle biológico descrita no texto consiste na"),
    "explicacao": "<p>No controle biológico, usam-se <strong>inimigos naturais</strong> das pragas: no exemplo, as joaninhas, que são <strong>predadoras</strong> de pulgões e cochonilhas. Alternativa <strong>D</strong>.</p><p>As joaninhas comem as pragas, não as plantas (A). O objetivo é justamente reduzir os inseticidas (B). Sementes selecionadas e fertilizantes não são controle biológico (C). E o exemplo é de predadores, não de parasitas (E).</p>"},
4: {"materia": "Matemática", "assunto": "Razão e proporção", "tags": [I],
    "enunciado": apoio("O agrônomo também será responsável pela adubação da área a ser cultivada.",
                       "A quantidade de adubo recomendada é um número expresso na unidade kg/ha (kilograma por hectare).",
                       "A adubação é, geralmente, realizada em sulcos, neste caso, transforma-se a quantidade Q de adubo de kg/ha para g/m (grama por metro).",
                       "Para cada sulco, a fórmula utilizada é: \\(\\dfrac{Q \\cdot E}{10}\\) g/m, em que: Q = quantidade de adubo em kg/ha; E = espaçamento em metros entre os sulcos (m).",
                       "Veja o exemplo de cálculo da quantidade de adubo, considerando-se a recomendação de 350 kg/ha e um espaçamento entre sulcos de 45 cm.",
                       "Primeiramente, deve-se fazer a conversão de centímetro para metro: 45 cm = 0,45 m.",
                       "Depois, usando a fórmula apresentada, temos, por sulco: \\(\\dfrac{350 \\cdot 0{,}45}{10}\\) g/m = 15,75 g/m.",
                       "Logo, a quantidade de adubo, para um sulco de 100 m de comprimento será: (15,75 g/m) x 100 m = 1 575 g ou 1,575 kg.")
                 + fonte("&lt;https://tinyurl.com/cs2m2pf8&gt; Acesso em: 28.03.2022. Adaptado.")
                 + p("Considere uma recomendação para adubação de 500 kg/ha, sendo o espaçamento entre os sulcos de 60 cm. A massa de adubo que deverá ser utilizada, em kg, em um sulco com 150 m de comprimento, é de"),
    "explicacao": "<p>Convertendo: 60 cm = 0,6 m. Por metro de sulco: \\(\\dfrac{500 \\cdot 0{,}6}{10} = 30\\) g/m. Para 150 m: \\(30 \\times 150 = 4\\,500\\) g = <strong>4,5 kg</strong>. Alternativa <strong>B</strong>.</p><p>4 500 (E) é o resultado em gramas, sem converter para quilogramas. E 30 (C) é a quantidade por metro.</p>"},
5: {"materia": "História", "assunto": "Antiguidade",
    "enunciado": apoio("Durante dezenas de milhares de anos, os grupos pré-históricos viveram exclusivamente da caça, da pesca e da coleta usando armas de pedras talhadas. Para suprir suas necessidades básicas de sobrevivência, eles melhoraram técnicas de caça e de pesca, inventaram ferramentas eficientes, descobriram meios para produzir e conservar o fogo, aprenderam a reconhecer vegetais comestíveis e ervas curativas, desenvolveram técnicas e instrumentos para preparar a pele de animais para roupas e tendas. Tais atividades exigiam planejamento, organização, divisão do trabalho, troca de informações – evidências de que os caçadores paleolíticos já tinham um modo de vida em sociedade.")
                 + fonte("DOMINGUES, Joelza Esther. <em>História em documento. Imagem e texto</em>. 6. 2ª edição. São Paulo: FTD, 2013. p.30. Adaptado.")
                 + p("No período abordado pelo texto, os humanos"),
    "explicacao": "<p>O texto diz que esses grupos desenvolveram técnicas e ferramentas, e que suas atividades exigiam planejamento, organização e divisão do trabalho, “evidências de que os caçadores paleolíticos já tinham um modo de vida em sociedade”. Alternativa <strong>E</strong>.</p><p>Eles conseguiram suprir suas necessidades (A) e desenvolveram técnicas, ao contrário dos outros animais (B). Reconheceram vegetais comestíveis, mas a agricultura só surgiria depois, no Neolítico (C). E conheciam os recursos naturais (D).</p>"},
6: {"materia": "Português", "assunto": "Texto literário", "tags": [I],
    "enunciado": EMICIDA + P6, "imagens": [EMICIDA_IMG],
    "explicacao": "<p>No verso 24, “Quando eles perceber o poder que têm, cuidado!” aponta para a força que as pessoas desfavorecidas, os “cansados dentro dos busão” e quem “junta latinha”, têm para mudar a própria realidade. Alternativa <strong>E</strong>.</p><p>No verso 8, trocar sorriso por dinheiro é criticado, não visto como garantia de felicidade (A). O verso 9 diz justamente que eles “não pode me enxergar”: a classe trabalhadora fica <strong>invisível</strong> (B). O verso 12 homenageia quem volta cansado no ônibus, sem falar em vantagens (C). E o verso 22 fala de gente que deixou a alegria em espera, não de consumo (D).</p>"},
7: {"materia": "Português", "assunto": "Variação linguística",
    "apoio_de": (6, P6),
    "explicacao": "<p>“Cê” (você), “tô” (estou), “pra” (para) e “busão” (ônibus) são formas da fala informal, da <strong>linguagem coloquial</strong>. Alternativa <strong>B</strong>.</p><p>Nas outras alternativas, há palavras da norma padrão misturadas às coloquiais, como “ser”, “ontem” e “menina” (A), “horizonte” e “esperança” (C), “chance” e “paz” (D), e todas as palavras da (E).</p>"},
8: {"materia": "Português", "assunto": "Interpretação de texto",
    "apoio_de": (6, P6),
    "explicacao": "<p>Juntar latinhas exige paciência, e o eu lírico está “focado no que tenho, não no que vou ter ou tinha”: ele se concentra no <strong>presente</strong>, um dia de cada vez, apesar das dificuldades. Alternativa <strong>B</strong>.</p><p>Ele não está dividido entre passado e futuro (A), nem inquieto revendo o passado (C). Não diz que trabalha para esquecer o passado (D). E a paciência é apresentada como virtude, não como imprudência (E).</p>"},
9: {"materia": "Português", "assunto": "Interpretação de texto",
    "apoio_de": (6, P6),
    "explicacao": "<p>“Cada dia é uma chance pra ser melhor que ontem / O sol prova isso quando cruza o horizonte”: o sol nascendo é o <strong>amanhecer</strong>, e cada novo dia é uma <strong>nova chance de sermos melhores</strong>. Alternativa <strong>C</strong>.</p><p>O tom é de esperança, não de frustração (A). Não há uma interrogação nos versos 1 e 2 (B). E o sol que cruza o horizonte nascendo, “fonte que aquece, ilumina”, não é o anoitecer (D e E).</p>"},
10: {"materia": "Matemática", "assunto": "Operações e problemas",
     "enunciado": JUNIOR + P10,
     "explicacao": "<p>Salário mensal = horas por semana × valor da hora × 4,5 semanas:</p><p>x (Boituva) = 43 × 25 × 4,5 = 4 837,50</p><p>y (Rio de Janeiro) = 42 × 50 × 4,5 = 9 450,00</p><p>z (Fortaleza) = 44 × 30 × 4,5 = 5 940,00</p><p>Então <strong>y &gt; z &gt; x</strong>. Alternativa <strong>E</strong>.</p><p>Comparar só a jornada semanal daria z &gt; x &gt; y (C), mas o valor da hora muda muito de uma cidade para outra.</p>"},
11: {"materia": "Matemática", "assunto": "Geometria plana",
     "enunciado": p("Júnior optou por se mudar para a cidade de Boituva nas proximidades de um centro de treinamento <strong>T</strong>.",
                    "Nessa cidade, ele encontrou algumas opções de imóveis, que denominou <strong>A</strong>, <strong>B</strong>, <strong>C</strong> e <strong>D</strong>. Além disso, ele descobriu que o ruído gerado pelas aeronaves do centro de treinamento podia ser ouvido em uma região com centro em <strong>T</strong> e raio de 6 km.",
                    "Ao representar esses imóveis e o centro de treinamento em um plano cartesiano, cujos eixos têm escalas em kilômetros, ele obteve as coordenadas:",
                    "<strong>T</strong>(0,0)   <strong>A</strong>(0,7)   <strong>B</strong>(1,6)   <strong>C</strong>(2,5)   <strong>D</strong>(3,4)",
                    "Com base nessas informações, são imóveis que estão fora da zona de ruído"),
     "apoio_de": (10, P10),
     "explicacao": "<p>A distância de cada imóvel até T(0,0) é \\(\\sqrt{x^2 + y^2}\\):</p><p>A: \\(\\sqrt{0 + 49} = 7\\); B: \\(\\sqrt{1 + 36} = \\sqrt{37} \\approx 6{,}1\\); C: \\(\\sqrt{4 + 25} = \\sqrt{29} \\approx 5{,}4\\); D: \\(\\sqrt{9 + 16} = 5\\).</p><p>Ficam fora do raio de 6 km os imóveis <strong>A e B</strong>. Alternativa <strong>A</strong>.</p><p>Somar as coordenadas, em vez de usar o teorema de Pitágoras, daria 7 para todos, e nenhum ficaria dentro.</p>"},
12: {"materia": "História", "assunto": "História contemporânea", "tags": [I],
     "enunciado": apoio("A origem do fordismo remonta à Segunda Revolução Industrial, implementada a partir do final do século XIX nos países mais desenvolvidos do globo. O avanço da industrialização resultou na necessidade da criação de técnicas de produção que abrangessem uma qualidade produtiva atrelada à rapidez do processo de produção fabril. Portanto, foram desenhados modelos de produção industrial para a época.")
                  + fonte("&lt;https://tinyurl.com/56y83zaw&gt; Acesso em: 10.04.2022. Adaptado.")
                  + p("Entre as principais características do sistema de produção mencionado no texto, podemos apontar corretamente"),
     "explicacao": "<p>O fordismo, criado por Henry Ford na fabricação de automóveis, usava a <strong>linha de montagem</strong> com esteiras rolantes: o produto passava pelo trabalhador, que fazia sempre a mesma tarefa, só uma parte da produção. Alternativa <strong>D</strong>.</p><p>Informatização e robôs (A) vieram depois, com a automação. O fordismo não reduziu jornadas nem incentivou o ócio (B). A produção artesanal e doméstica (C) é anterior às fábricas. E no fordismo o trabalhador <strong>não</strong> conhecia todas as etapas da produção (E).</p>"},
13: {"materia": "Geografia", "assunto": "População",
     "explicacao": "<p>Malthus não previu o avanço tecnológico no campo: máquinas, fertilizantes e novas técnicas, a partir da Revolução Industrial, aumentaram muito a <strong>produção de alimentos</strong>. Alternativa <strong>C</strong>.</p><p>A população mundial não diminuiu: cresceu muito (A). Os operários não acabaram com a fome cultivando hortas (B). Na Revolução Industrial, as pessoas foram do campo para as <strong>cidades</strong> (D). E não houve distribuição de cestas básicas pelos donos de fábricas (E).</p>"},
14: {"materia": "Português", "assunto": "Conectivos",
     "enunciado": EMPREENDER + P14,
     "explicacao": "<p>Em “é projetado <strong>para</strong> gerar lucro”, o “para” indica a <strong>finalidade</strong> do empreendimento clássico e pode ser trocado por “a fim de”. Alternativa <strong>A</strong>.</p><p>No terceiro parágrafo, “para conseguir transformar” também indica finalidade, e não direção (B). “Porém” indica oposição, não consequência (C). O “e”, em “pode gerar renda e pode ser organizado”, soma as duas ideias, com sentido de adição (D). E “uma vez que” explica por que o serviço social <strong>não</strong> costuma resolver o problema, e não sua eficácia (E).</p>"},
15: {"materia": "Projeto de vida", "assunto": "Projeto de vida e carreira",
     "apoio_de": (14, P14),
     "explicacao": "<p>O texto diz que o empreendedorismo social busca benefícios para a sociedade, “porém, um empreendimento social pode gerar renda e pode ser organizado com fins lucrativos”. Alternativa <strong>C</strong>.</p><p>Só o empreendedorismo clássico tem o lucro como objetivo principal (A). O serviço social é frágil pela <strong>falta</strong> de apoio contínuo (B). O texto não fala em bolsa de valores (D) nem em agremiações políticas (E).</p>"},
16: {"materia": "Projeto de vida", "assunto": "Projeto de vida e carreira",
     "enunciado": p("Considere os exemplos:") + p("<strong>I</strong> Capacitação de produtores familiares do semiárido para o cultivo e a comercialização de produtos orgânicos.",
                                                  "<strong>II</strong> Construção de sistemas de iluminação utilizando garrafas PET e energia solar disponibilizados a preços acessíveis.",
                                                  "<strong>III</strong> Organização de campanhas de doação de alimentos e de roupas para vítimas de desastres naturais.")
                  + p("Segundo as definições apresentadas no texto, são exemplos de empreendedorismo social as ações presentes em"),
     "apoio_de": (14, P14),
     "explicacao": "<p>O empreendedorismo social transforma a realidade de populações desfavorecidas e pode gerar renda. A capacitação de produtores (I) e a iluminação vendida a preço acessível (II) se encaixam nisso. Já a campanha de doações (III) é uma resposta pontual a um problema, que depende de recursos de fora: é <strong>serviço social</strong>, como a arrecadação de ração citada no texto. São exemplos de empreendedorismo social I e II. Alternativa <strong>D</strong>.</p>"},
17: {"materia": "Química", "assunto": "Funções orgânicas", "tags": [I],
     "enunciado": PLASTICO + P17,
     "explicacao": "<p>O texto diz que o beneficiamento do petróleo fornece matéria-prima para os plásticos, que “são produzidos por meio de reações de polimerização”. Ou seja, são obtidos por reações que usam matéria-prima do petróleo. Alternativa <strong>B</strong>.</p><p>Os plásticos não saem diretamente do petróleo, e são moléculas grandes, não pequenas (A). Eles podem ser moldados (C). São as embalagens de vidro e de lata que estão sendo substituídas pelo PET, e não o contrário (D). E os plásticos vêm do petróleo, não o originam (E).</p>"},
18: {"materia": "Química", "assunto": "Substâncias e misturas", "tags": [I],
     "enunciado": p("Os plásticos podem ser moldados, pois “amolecem” com o calor, chegando a sofrer fusão em determinadas temperaturas.", "O quadro apresenta o ponto de fusão de alguns tipos de plásticos.")
                  + tabela(["Plástico", "Ponto de fusão"], [["PE (polietileno)", "220 °C"], ["PET (politereftalato de etileno)", "260 °C"], ["PP (polipropileno)", "160 °C"], ["PS (poliestireno)", "145 °C"], ["PVC (policloreto de vinila)", "115 °C"]])
                  + p("Um técnico de laboratório aquece separada e simultaneamente amostras, com massas iguais, de cada um dos cinco plásticos do quadro, que estão à mesma temperatura inicial.", "O primeiro plástico que sofrerá fusão será o"),
     "apoio_de": (17, P17),
     "explicacao": "<p>Aquecendo todos ao mesmo tempo, a partir da mesma temperatura, o primeiro a derreter é o de <strong>menor ponto de fusão</strong>: o PVC, a 115 °C. Alternativa <strong>E</strong>.</p><p>O PET (D) tem o maior ponto de fusão (260 °C) e seria o último a derreter.</p>"},
19: {"materia": "Química", "assunto": "Substâncias e misturas", "tags": [I],
     "enunciado": p("Em uma usina de reciclagem, os plásticos são separados por diferença de densidade para, posteriormente, serem fundidos e remoldados em novos objetos. O quadro apresenta a densidade de alguns plásticos.")
                  + tabela(["Plástico", "Densidade"], [["PE (polietileno)", "0,92 g/cm³"], ["PET (politereftalato de etileno)", "1,38 g/cm³"], ["PP (polipropileno)", "0,90 g/cm³"], ["PS (poliestireno)", "1,07 g/cm³"], ["PVC (policloreto de vinila)", "1,40 g/cm³"]])
                  + p("Dado: densidade da água = 1,00 g/cm³", "Em um tanque com água, colocamos objetos maciços confeccionados com os plásticos mencionados.", "Os objetos que ficam flutuando na superfície da água são confeccionados com"),
     "apoio_de": (17, P17),
     "alternativas": {"D": "PET, PS e PVC."},
     "explicacao": "<p>Flutua na água o que é <strong>menos denso</strong> que ela (1,00 g/cm³). Só o PP (0,90) e o PE (0,92) têm densidade menor que 1. Alternativa <strong>B</strong>.</p><p>PET, PS e PVC têm densidade maior que 1 e afundam (A, C, D e E).</p>"},
20: {"materia": "Química", "assunto": "Interpretação de dados",
     "enunciado": p("De acordo com o texto, é correto afirmar que"), "apoio_de": (17, P17),
     "explicacao": "<p>O texto diz que o beneficiamento do petróleo “leva à obtenção de combustíveis e de matéria-prima usada na produção de diversos materiais”. Alternativa <strong>E</strong>.</p><p>É o PET que vem substituindo latas, vidros e multilaminados (A). O PET foi desenvolvido em 1941, sem relação com o Brasil (B). Os plásticos vêm do petróleo, não o contrário (C). E eles “amolecem” com o calor (D).</p>"},
21: {"materia": "Química", "assunto": "Substâncias e misturas",
     "enunciado": p("As latas de flandres, mencionadas no texto, são feitas de uma"), "apoio_de": (17, P17),
     "explicacao": "<p>O texto diz que a lata de flandres é feita de aço, “liga metálica de ferro e carbono, revestido por estanho”. Uma liga é uma <strong>mistura</strong>; portanto, é uma mistura revestida de estanho. Alternativa <strong>A</strong>.</p><p>O aço não é substância pura nem composta: é uma mistura (B, D e E). E o revestimento é de estanho, não de ferro e carbono (C).</p>"},
22: {"materia": "História", "assunto": "História contemporânea",
     "enunciado": apoio("Durante a I Guerra Mundial, a economia estadunidense estava em pleno desenvolvimento; suas indústrias produziam e exportavam em grandes quantidades, principalmente para os países europeus. No final da década de 1920, as nações europeias, recuperando-se dos efeitos negativos da guerra, diminuíram drasticamente a importação de produtos industrializados e agrícolas dos Estados Unidos.",
                        "Com a diminuição das exportações para a Europa, os estoques das indústrias dos Estados Unidos passaram a aumentar, já que essas empresas não conseguiam vender como antes. Grande parte delas tinha ações na Bolsa de Valores de Nova Iorque e os milhões de estadunidenses que haviam investido nessas ações correram para tentar vendê-las, enquanto seus valores foram caindo gradativamente até o zero.")
                  + p("Essa crise econômica"),
     "explicacao": "<p>O texto descreve a <strong>Crise de 1929</strong>, com a quebra da Bolsa de Nova York. Ela se espalhou pelo mundo, levou empresas à falência e causou desemprego em massa: foi a Grande Depressão. Alternativa <strong>B</strong>.</p><p>As economias já eram interligadas, e a crise atingiu vários países (A e C). No Brasil, o preço do café despencou, e o governo chegou a queimar sacas (D). E os governos precisaram intervir na economia, como no New Deal dos Estados Unidos (E).</p>"},
23: {"materia": "Biologia", "assunto": "Doenças e saúde",
     "enunciado": apoio("A pandemia de COVID–19, causada pelo novo coronavírus (SARSCoV–2), evidenciou que desenvolver uma vacina é um processo que demanda muita pesquisa e exige um trabalho conjunto de diferentes profissionais da área da saúde, tais como médicos, farmacêuticos, biomédicos, engenheiros químicos, entre muitos outros.",
                        "Após ser desenvolvida, uma vacina é encaminhada para registro sanitário e, se aprovada pelas agências reguladoras, é distribuída para a população.",
                        "A produção de uma vacina se baseia no agente causador da doença, o qual estará inativado, atenuado ou presente apenas em fragmentos. Dessa maneira, uma vacina possui os antígenos capazes de estimular no organismo humano a produção de anticorpos ao simular uma doença infecciosa, garantindo assim a imunização contra a doença.")
                  + p("Com base nas informações do texto, pode-se concluir corretamente que"),
     "explicacao": "<p>O texto diz que, aprovada pelas agências reguladoras, a vacina é distribuída à população e estimula o organismo a <strong>produzir anticorpos</strong>, prevenindo a doença. Alternativa <strong>B</strong>.</p><p>Desenvolver vacinas não deixa os profissionais imunes (A). Pandemia é a doença espalhada por vários países e continentes (C). A vacina tem <strong>antígenos</strong>, não anticorpos, e serve para prevenir, não tratar (D). E a COVID-19 é causada por um vírus, não por uma bactéria (E).</p>"},
24: {"materia": "Projeto de vida", "assunto": "Projeto de vida e carreira", "tags": [I],
     "enunciado": apoio("<strong>TEXTO 1</strong>", "Na Idade Média (476 a 1453), tanto a infância quanto a adolescência não eram reconhecidas como fases do desenvolvimento humano. No período de transição para a vida adulta, as maiores preocupações da comunidade eram a castidade e o casamento. Esse período não aparentava ser fonte de maiores preocupações: “os filhos de artesãos seguiriam artesãos, os pertencentes à aristocracia feudal se encaminhavam para a vida militar ou religiosa e o camponês seguiria camponês”.")
                  + fonte("&lt;https://tinyurl.com/2p8yjwxx&gt; Acesso em: 10.04.2022. Adaptado.")
                  + apoio("<strong>TEXTO 2</strong>", "Segundo a Base Nacional Comum Curricular (BNCC), documento que regulamenta a educação básica no Brasil do século XXI, os estudantes devem aprender a valorizar a diversidade de saberes e vivências culturais e apropriar-se de conhecimentos e experiências, entender as relações próprias do mundo do trabalho e fazer escolhas alinhadas ao exercício da cidadania e ao seu projeto de vida, com liberdade, autonomia, consciência crítica e responsabilidade. Os estudantes devem conseguir refletir sobre seus desejos e objetivos, aprendendo a se organizar, estabelecer metas, planejar e perseguir com determinação, esforço, autoconfiança e persistência seus projetos presentes e futuros.")
                  + fonte("&lt;https://tinyurl.com/mutxk679&gt; Acesso em: 10.04.2022. Adaptado.")
                  + p("A análise dos textos nos permite concluir corretamente que"),
     "explicacao": "<p>Na Idade Média, o futuro já estava definido pelo grupo social: filho de artesão seria artesão, e assim por diante. Hoje, a BNCC fala em escolhas feitas “com liberdade, autonomia” e de acordo com os desejos e objetivos de cada estudante. Alternativa <strong>A</strong>.</p><p>A BNCC fala em esforço e planejamento, não em ser sustentado pelo Estado (B). Na Idade Média não havia escolha (C e E), e hoje a infância e a adolescência <strong>são</strong> reconhecidas (D).</p>"},
25: {"materia": "Biologia", "assunto": "Nutrição e saúde",
     "explicacao": "<p>A celulose das fibras não é digerida pelo nosso corpo e não fornece calorias, mas ajuda o <strong>funcionamento do intestino</strong>. Alternativa <strong>B</strong>.</p><p>Alimentos industrializados e gordurosos favorecem a obesidade e a hipertensão (A). Uma boa dieta tem <strong>pouca</strong> gordura saturada e sal (C). “Zero lactose” só indica que o alimento não tem o açúcar do leite: ele continua tendo calorias (D). E arroz, macarrão e batata fornecem energia ao corpo (E).</p>"},
26: {"materia": "Química", "assunto": "Reações químicas", "tags": [I],
     "enunciado": p("Quando se fala em comida, já pensamos em calorias!",
                    "Quando ingerimos um alimento, este será “queimado” pelo nosso metabolismo e a energia produzida será usada nas nossas atividades do dia a dia. Para calcularmos essa energia produzida por certa quantidade de um alimento, devemos queimá-lo em um calorímetro. A reação é realizada dentro de um recipiente que está imerso em água e essa energia é expressa na unidade de medida “calorias”.",
                    "Leia a frase e complete as lacunas.")
                  + apoio("Durante a reação, a temperatura da água ....<strong>I</strong>...., pois temos uma reação ....<strong>II</strong>...., ou seja, que ....<strong>III</strong>.... energia.")
                  + p("Assinale a alternativa que completa, correta e respectivamente, a frase"),
     "alternativas": colunas(["I", "II", "III"], [["diminui", "exotérmica", "libera"], ["diminui", "endotérmica", "absorve"], ["aumenta", "endotérmica", "libera"], ["aumenta", "endotérmica", "absorve"], ["aumenta", "exotérmica", "libera"]]),
     "explicacao": "<p>Queimar o alimento é uma combustão: a reação <strong>libera</strong> energia (III), ou seja, é <strong>exotérmica</strong> (II). Essa energia aquece a água, cuja temperatura <strong>aumenta</strong> (I). Alternativa <strong>E</strong>.</p><p>Se a água esfriasse (A e B), a reação estaria absorvendo calor. E reação endotérmica absorve energia; não libera (C e D).</p>"},
27: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": [I],
     "enunciado": apoio("No saneamento básico, a demanda por profissionais especializados é crescente, porque, entre outras funções, eles são responsáveis por viabilizarem tanto o tratamento da água quanto a coleta, o tratamento e a destinação final dos esgotos.",
                        "O saneamento precário cria o ambiente propício a muitas doenças, como diarreia, hepatite e verminoses, causadas pela ingestão de água e/ou alimentos contaminados.",
                        "A incidência de casos de dengue, por sua vez, segundo informações do Ministério da Saúde, tem aumentado muito devido à presença de água parada em muitos locais. Nesse caso, o saneamento básico é essencial a fim de evitar as chances da ocorrência de surto de dengue.")
                  + p("Sobre esta doença, pode-se afirmar corretamente que é"),
     "explicacao": "<p>A dengue é causada por um <strong>vírus</strong> transmitido pela picada do mosquito <em>Aedes aegypti</em> infectado. Os sintomas mais comuns são febre, dores no corpo e manchas vermelhas na pele. Alternativa <strong>E</strong>.</p><p>Ela não passa de pessoa para pessoa nem pela água contaminada (A). Não é causada por protozoário (B). Higienizar alimentos e mãos não evita a dengue: o que evita é eliminar a água parada (C). E o inseto que vive em paredes de barro é o barbeiro, da doença de Chagas (D).</p>"},
28: {"materia": "Química", "assunto": "Separação de misturas", "tags": [I],
     "enunciado": apoio("No tratamento de água, usamos processos físicos e químicos para obtenção de água potável que será distribuída à população.",
                        "Entre os processos físicos, temos:",
                        "→ separação de partículas com maior densidade, que irão para o fundo do tanque e, posteriormente, serão extraídas;",
                        "→ retenção de pequenas partículas, quando a água passa por tanques que possuem diferentes camadas de cascalho, areia e carvão.")
                  + p("Os processos físicos descritos são denominados, respectivamente, de"),
     "alternativas": {"A": "floculação e decantação.", "B": "decantação e filtração.", "C": "filtração e cloração.", "D": "floculação e filtração.", "E": "decantação e cloração."},
     "explicacao": "<p>Partículas mais densas que vão para o fundo: <strong>decantação</strong>. Água passando por camadas de cascalho, areia e carvão, que retêm partículas: <strong>filtração</strong>. Alternativa <strong>B</strong>.</p><p>A floculação (A e D) é a etapa química em que se forma os flocos. E a cloração (C e E) também é um processo químico, de desinfecção.</p>"},
29: {"materia": "Biologia", "assunto": "Fisiologia humana",
     "enunciado": p("O hemograma, exame que demonstra as variações quantitativas e morfológicas das células do sangue, pode ser realizado por biomédicos especialistas em análises clínicas.",
                    "Pedro, após uma consulta de rotina, realizou um hemograma solicitado por um médico, que evidenciou alteração na taxa de hemácias (glóbulos vermelhos), a qual estava muito abaixo do normal.",
                    "Considerando esse hemograma, pode-se concluir que Pedro tem"),
     "explicacao": "<p>As hemácias transportam o <strong>oxigênio</strong> pelo sangue. Com poucas hemácias (anemia), esse transporte fica prejudicado. Alternativa <strong>C</strong>.</p><p>Infecções são indicadas pelos leucócitos (A). A coagulação depende das plaquetas (B). Alergias envolvem o sistema imunológico (D). E a insulina está ligada ao diabetes (E).</p>"},
30: {"materia": "Matemática", "assunto": "Geometria plana",
     "enunciado": PAINEL + P30, "imagens": [PAINEL_IMG],
     "alternativas": colunas(["Área", "Perímetro"], [["3xy", "3x + y"], ["3 + xy", "6x + 2y"], ["3x<sup>2</sup>y<sup>2</sup>", "6x + y<sup>2</sup>"], ["3xy", "6x + 2y"], ["3x<sup>2</sup>y<sup>2</sup>", "3x + y"]]),
     "explicacao": "<p>O painel é um retângulo de lados 3x e y. Área: \\(3x \\cdot y = 3xy\\). Perímetro: \\(3x + y + 3x + y = 6x + 2y\\). Alternativa <strong>D</strong>.</p><p>3x + y (A e E) é só metade do perímetro. E 3x²y² (C e E) eleva os lados ao quadrado sem motivo.</p>"},
31: {"materia": "Matemática", "assunto": "Razão e proporção",
     "enunciado": p("No painel decorativo, a primeira fileira de baixo para cima é toda formada por espelhos retangulares de mesmo comprimento.", "Se o painel tiver um total de 3 metros de comprimento, então a medida do comprimento de cada espelho, em centímetros, é"),
     "apoio_de": (30, P30),
     "explicacao": "<p>Na figura, a fileira de baixo tem <strong>4 espelhos</strong> inteiros. O painel tem 3 m = 300 cm: \\(\\dfrac{300}{4} = 75\\) cm. Alternativa <strong>C</strong>.</p><p>100 cm (B) seria dividir por 3, confundindo o “3” de 3x com o número de espelhos.</p>"},
32: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade",
     "explicacao": "<p>Áreas verdes deixam a água da chuva <strong>infiltrar no solo</strong>, diminuindo a quantidade que escorre pelas ruas e causa enchentes. Alternativa <strong>E</strong>.</p><p>Lixo entope bueiros e canais (A). Impermeabilizar o solo aumenta o escoamento (B). O assoreamento deixa os rios mais rasos, e eles transbordam mais fácil (C). E piorar a drenagem aumenta as enchentes (D).</p>"},
33: {"materia": "Geografia", "assunto": "Industrialização brasileira",
     "explicacao": "<p>O texto explica que, na “pejotização”, o funcionário é contratado como pessoa jurídica (PJ), e “a empresa deixa de arcar com alguns encargos previdenciários e trabalhistas”. O nome vem de “PJ”. Alternativa <strong>C</strong>.</p><p>Quem constitui a empresa é o funcionário, e não há registro em carteira (A). Não é uma norma da Constituição (B), não transfere encargos para os municípios (D) e o texto não fala de entregadores de aplicativo (E).</p>"},
34: {"materia": "Física", "assunto": "Pressão",
     "enunciado": p("O princípio dos vasos comunicantes, pelo fato de os líquidos se nivelarem em recipientes que se interligam, é usado em diferentes situações.",
                    "Por exemplo, para acertar o nível entre dois pontos em uma obra, os pedreiros utilizam uma mangueira transparente com água, conforme a imagem.")
                  + "[[fig:1]]" + fonte("Fonte de dados &lt;https://tinyurl.com/udhhjxyu&gt; Acesso em: 30.04.2022.")
                  + p("Dentre as alternativas, assinale aquela que melhor representa esse princípio."),
     "imagens": [{"arquivo": "q34", "alt": "Ilustração de uma mangueira transparente com água, presa a duas estacas fincadas em um terreno inclinado. Os detalhes ampliados das duas pontas da mangueira mostram que a água fica na mesma altura dos dois lados, marcada por uma linha tracejada (“Nível de água”)."},
                 {"arquivo": "q34a", "alt": "Cinco recipientes de formatos diferentes, separados uns dos outros, com água na mesma altura em todos."},
                 {"arquivo": "q34b", "alt": "Cinco recipientes de formatos diferentes, separados uns dos outros, com água em alturas diferentes."},
                 {"arquivo": "q34c", "alt": "Cinco recipientes de formatos diferentes, ligados pela base por um tubo, com a água em alturas diferentes em cada um."},
                 {"arquivo": "q34d", "alt": "Cinco recipientes de formatos diferentes, ligados pela base por um tubo, com a água em alturas diferentes em cada um."},
                 {"arquivo": "q34e", "alt": "Cinco recipientes de formatos diferentes, ligados pela base por um tubo, com a água na mesma altura em todos."}],
     "alternativas": {"A": "[[fig:2]]", "B": "[[fig:3]]", "C": "[[fig:4]]", "D": "[[fig:5]]", "E": "[[fig:6]]"},
     "explicacao": "<p>Nos vasos comunicantes, os recipientes estão <strong>ligados entre si</strong>, e o líquido fica <strong>na mesma altura</strong> em todos, qualquer que seja o formato de cada um. Só a figura da alternativa <strong>E</strong> mostra as duas coisas.</p><p>Em A e B, os recipientes estão separados, então não são vasos comunicantes (em A, a água está na mesma altura por acaso). Em C e D, eles estão ligados, mas a água está em alturas diferentes, o que não acontece na realidade.</p>"},
35: {"materia": "História", "assunto": "Brasil Colônia", "tags": [I],
     "enunciado": p("O mapa representa os caminhos percorridos nos séculos XVII e XVIII pelas bandeiras, expedições armadas por particulares, chamados de bandeirantes. Estes percorriam o território da América para, entre outros objetivos, aprisionar e escravizar indígenas e procurar por fontes de metais preciosos.")
                  + "[[fig:1]]" + fonte("Fonte dos dados: MONTEIRO, John M. <em>Negros da terra – índios e bandeirantes nas origens de São Paulo</em>. São Paulo, Companhia das Letras, 1994, p. 13.")
                  + p("A partir da leitura do mapa, pode-se afirmar corretamente que"),
     "alternativas": {"A": "os bandeirantes, em suas expedições, respeitaram os limites territoriais definidos pelo Tratado de Tordesilhas, em 1494.",
                      "B": "as bandeiras se originaram nos territórios espanhóis do atual Uruguai e, de lá, percorreram a América do Sul em todas as direções.",
                      "C": "a ação das bandeiras contribuiu para a ampliação dos limites territoriais do Brasil para além daqueles definidos, em 1494, pelo Tratado de Tordesilhas.",
                      "D": "o processo de colonização do Brasil se iniciou na região de Olinda e Recife, de onde partiram as principais rotas dos bandeirantes.",
                      "E": "as fronteiras atuais do Brasil foram definidas no final do século XVIII, quando as expedições bandeirantes terminaram."},
     "imagens": [{"arquivo": "q35", "alt": "Mapa “Esquema geral das expedições de apresamento, 1550-1720”, com o território do Brasil e partes vizinhas. Setas saem de São Paulo em várias direções: para o sul (Missões do Guairá, do Tape, Sertão dos Patos, Laguna), para o oeste (Missões do Paraguai, Assunção, Sertão do Mato Grosso), para o centro (Sertão dos Goiazes, dos Cataguazes) e para o norte, até Belém (rota de Raposo Tavares). Outras rotas ligam Salvador, Recife e Natal aos sertões do Nordeste. A legenda diferencia expedições de resgate e apresamento dos Guarani (por mar e por terra), de outros grupos, de mercenários paulistas nas guerras do Nordeste e as rotas de Raposo Tavares e de Sebastião Pais de Barros."}],
     "explicacao": "<p>O mapa mostra os bandeirantes avançando muito para o oeste, o sul e o norte, por terras que, pelo Tratado de Tordesilhas, eram da Espanha. Essas expedições ajudaram a <strong>ampliar o território do Brasil</strong> além da linha de 1494. Alternativa <strong>C</strong>.</p><p>Os bandeirantes não respeitaram a linha de Tordesilhas (A). As bandeiras saíam principalmente de São Paulo, não do Uruguai (B) nem de Olinda e Recife (D). E as fronteiras atuais só se definiram no início do século XX, com a compra do Acre, por exemplo (E).</p>"},
36: {"materia": "Química", "assunto": "Substâncias e misturas",
     "enunciado": p("As cooperativas de catadores são responsáveis por buscar e receber os descartes de materiais possíveis de reutilização.",
                    "Nas usinas de reciclagem, os materiais recebidos são separados por meio de processos que se baseiam nas propriedades dos materiais, como densidade, imantação e outros.",
                    "A propriedade física densidade é a razão entre a massa e o volume de uma amostra de um mesmo material. Por exemplo, a razão entre a massa de uma barra de alumínio e o volume ocupado por essa mesma barra é 2,7 g/cm³, portanto dizemos que essa é a densidade do alumínio (d<sub>Aℓ</sub> = 2,7 g/cm³).",
                    "Aplicando o conceito de densidade, a massa de alumínio, em gramas, que será reciclada de uma escultura que ocupa o volume de 50 cm³, é"),
     "explicacao": "<p>De \\(d = \\dfrac{m}{V}\\), temos \\(m = d \\cdot V = 2{,}7 \\times 50 = 135\\) g. Alternativa <strong>D</strong>.</p><p>13,5 (B) e 27,0 (C) erram a vírgula. E 2,7 (A) é a densidade, não a massa.</p>"},
37: {"materia": "Projeto de vida", "assunto": "Projeto de vida e carreira",
     "enunciado": p("Há momentos que exigem sermos fortes para enfrentarmos dificuldades.", "Leia os quadrinhos.")
                  + "[[fig:1]]" + fonte("&lt;https://tinyurl.com/3ydj6wwm&gt; Acesso em: 28.03.2022. Original colorida.")
                  + p("Com base na interpretação dos quadrinhos, pode-se concluir corretamente que"),
     "imagens": [{"arquivo": "q37", "alt": "Quadrinho de The Awkward Yeti em quatro quadros. Um coração escala uma montanha, preso por cordas a um cérebro pendurado embaixo. 1: o coração pergunta: “Por que é tão difícil seguir em frente com nossa vida?”. 2: ele vê que o cérebro segura um saco chamado “Erros do passado” e grita: “Meu Deus, Cérebro! Largue isso!”; o cérebro: “Oh, desculpe”, e solta o saco. 3: o coração pergunta: “Pera, por que continua tão difícil?”. 4: agora o cérebro segura um saco chamado “Medo de errar”; o coração: “Por que você trouxe isso?”; o cérebro: “foi mal”, e solta o saco."}],
     "explicacao": "<p>O coração (a emoção) e o cérebro (a razão) sobem juntos, presos um ao outro. Só conseguem avançar quando o cérebro solta os “erros do passado” e o “medo de errar”. A mensagem é que razão e emoção devem seguir juntas, livrando-se desses pesos. Alternativa <strong>E</strong>.</p><p>Quem carrega os pesos é o cérebro, e o coração não se liberta sozinho (A). O cérebro só larga os sacos quando o coração pede, nos dois casos (B). Os dois agem juntos, sem um deles ser o único responsável (C) ou ter um papel menor (D).</p>"},
38: {"materia": "Projeto de vida", "assunto": "Ética e cidadania",
     "enunciado": apoio("O trabalho infantil é ilegal e priva as crianças de uma infância normal, impedindo-as não só de frequentar a escola e estudar normalmente, mas também de desenvolver de maneira saudável todas as suas capacidades e habilidades. Antes de tudo, o trabalho infantil é uma grave violação dos direitos humanos e dos direitos e princípios fundamentais no trabalho.")
                  + fonte("&lt;https://tinyurl.com/236rm22x&gt; Acesso em: 10.04.2022. Adaptado.")
                  + apoio("De acordo com o Fundo das Nações Unidas para a Infância (UNICEF), o número de crianças e adolescentes em situação de trabalho infantil chegou a 160 milhões em todo o mundo – um aumento de 8,4 milhões de meninas e meninos nos últimos quatro anos, de 2016 a 2020. Dados coletados pelo UNICEF em São Paulo apontam para o agravamento da situação de trabalho infantil durante a pandemia.")
                  + fonte("&lt;https://tinyurl.com/bdfufhnf&gt; Acesso em: 02.04.2022. Adaptado.")
                  + p("De acordo com os textos, o trabalho infantil"),
     "explicacao": "<p>O primeiro texto diz que o trabalho infantil “é ilegal” e impede as crianças de “frequentar a escola e estudar normalmente” e de se desenvolver de forma saudável. Alternativa <strong>E</strong>.</p><p>Nem a ONU nem o UNICEF liberam ou regularizam o trabalho infantil (A e B). O Estado não o incentiva (C). E ele não foi eliminado no Brasil: piorou em São Paulo durante a pandemia (D).</p>"},
39: {"materia": "Projeto de vida", "assunto": "Projeto de vida e carreira",
     "enunciado": p("Leia o texto.") + "[[fig:1]]" + fonte("&lt;https://tinyurl.com/ykkzds8n&gt; Acesso em: 20.03.2022. Original colorido.")
                  + p("Assinale a frase que é um contraponto ao posicionamento da personagem sobre o medo."),
     "imagens": [{"arquivo": "q39", "alt": "Tirinha de Willtirando em seis quadros. Um homem conversa com um amigo num bar; no ombro do amigo há uma pequena criatura. O homem fala do amigo: “Ele só viaja de ônibus. Aviões caem.”; “Um novo relacionamento? Antes só que mal acompanhado.”; “O trabalho dele é um lixo, mas pagam bem.”. O homem pergunta: “Quem é este no seu ombro?”, e o amigo responde: “É meu medo.”. O homem: “Ele fica inventando desculpas pra tudo.”. A criatura responde: “Não são desculpas. Lembre-se: você é um cara precavido.”"}],
     "alternativas": {"A": "“Aprendi que a coragem não é a ausência do medo, mas o triunfo sobre ele”. (Nelson Mandela)",
                      "B": "“Um dos efeitos do medo é perturbar os sentidos e fazer que as coisas não pareçam o que são”. (Miguel de Cervantes).",
                      "C": "“O medo é, dos sentimentos humanos, o mais dissolvente, porque nos leva a fazer muita coisa que não queremos fazer, e deixar de fazer muita coisa que queríamos e necessitávamos fazer”. (Josué de Castro)",
                      "D": "“O medo é a extrema ignorância em momento muito agudo”. (João Guimarães Rosa)",
                      "E": "“Os homens se dividem em duas espécies: os que têm medo de viajar de avião e os que fingem que não têm”. (Fernando Sabino)"},
     "explicacao": "<p>Na tirinha, o medo se apresenta como prudência (“você é um cara precavido”) e justifica deixar de viver: não viajar de avião, não começar um relacionamento, não mudar de emprego. O contraponto é a frase de Mandela: coragem não é não ter medo, mas <strong>vencê-lo</strong>. Alternativa <strong>A</strong>.</p><p>As frases de Cervantes (B), Josué de Castro (C) e Guimarães Rosa (D) descrevem os efeitos negativos do medo, o que <strong>confirma</strong> o que a tirinha mostra, sem se opor ao que o personagem medo diz sobre si. E a de Fernando Sabino (E) trata o medo de avião como algo geral, sem propor superá-lo.</p>"},
40: {"materia": "Química", "assunto": "Polaridade e solubilidade", "tags": [I],
     "enunciado": SABAO + P40, "imagens": [SABAO_IMG],
     "explicacao": "<p>O texto explica que a molécula de sabão tem uma cabeça com afinidade com a água e uma cauda com afinidade com a gordura: ela interage com <strong>as duas</strong>. Por isso consegue arrastar a gordura com a água. Alternativa <strong>E</strong>.</p><p>O sabão não transforma a gordura em outras substâncias: ele a separa em pedaços menores (A). É a <strong>cauda</strong> que interage com a gordura (B), e a <strong>cabeça</strong> que interage com a água (C). E o sabão remove a gordura, não a água (D).</p>"},
41: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": [I],
     "enunciado": p("Analisando o infográfico, podemos concluir corretamente que"), "apoio_de": (40, P40),
     "explicacao": "<p>No infográfico, a cauda do sabão se liga à membrana de gordura do vírus e a rompe; o material genético e os pedaços do vírus são levados pela água. Alternativa <strong>C</strong>.</p><p>A membrana de gordura <strong>protege</strong> o material genético; quem ajuda a infectar as células são as proteínas (A). O material genético fica dentro do vírus, não nas proteínas (B). A parte que interage com a água é a hidro<strong>fílica</strong> (D). E quem rompe a membrana é a cauda hidro<strong>fóbica</strong> (E).</p>"},
42: {"materia": "Português", "assunto": "Classes de palavras",
     "enunciado": POTTER + P42,
     "explicacao": "<p>No contexto: “secamente” = <strong>seriamente</strong>, sem simpatia; “sobre” = <strong>acerca das</strong> carreiras; “talvez” = <strong>possivelmente</strong>; “caráter” = <strong>índole</strong>; “aptidão” = <strong>habilidade</strong>. Alternativa <strong>E</strong>.</p><p>“Afetuosamente” (B) e “avidamente” (C) mudam o tom da fala. “Em cima das” (A) e “durante” (D) não equivalem a “sobre” nesse sentido. E “incapacidade” (D) é o oposto de aptidão.</p>"},
43: {"materia": "Projeto de vida", "assunto": "Projeto de vida e carreira",
     "enunciado": p("O trecho apresentado mostra o personagem Harry Potter, protagonista de uma série de livros infantojuvenis, no momento de escolha de sua carreira.", "Com base nas informações do trecho, depreende-se corretamente que a escolha de uma profissão"),
     "apoio_de": (42, P42),
     "explicacao": "<p>Na reunião, a professora ajuda Harry a pensar na carreira e a escolher as disciplinas certas para chegar lá, mostrando o que ele precisa fazer. A escola <strong>auxilia o estudante</strong> a se conhecer e a planejar seus objetivos. Alternativa <strong>E</strong>.</p><p>A escola trata do assunto, na própria reunião (A). O desempenho importa: são exigidas notas excelentes (B). A professora orienta, sem impor nada (C). E as disciplinas são escolhidas de acordo com a carreira desejada (D).</p>"},
44: {"materia": "Matemática", "assunto": "Porcentagem", "tags": [I],
     "enunciado": p("Considerando que exista um total de 12 N.I.E.M.s, a alternativa cujo esquema representa o percentual mais próximo do número mínimo de N.I.E.M.s que um estudante de Hogwarts deve ter cursado para estar apto a seguir a carreira de auror é"),
     "apoio_de": (42, P42),
     "imagens": [{"arquivo": "q44a", "alt": PIZZA.format(n=10, s=4, b=6)}, {"arquivo": "q44b", "alt": PIZZA.format(n=4, s=3, b=1)},
                 {"arquivo": "q44c", "alt": PIZZA.format(n=8, s=5, b=3)}, {"arquivo": "q44d", "alt": PIZZA.format(n=10, s=6, b=4)},
                 {"arquivo": "q44e", "alt": PIZZA.format(n=4, s=1, b=3)}],
     "alternativas": {"A": "[[fig:1]]", "B": "[[fig:2]]", "C": "[[fig:3]]", "D": "[[fig:4]]", "E": "[[fig:5]]"},
     "explicacao": "<p>O mínimo é de 5 N.I.E.M.s em 12: \\(\\dfrac{5}{12} \\approx 41{,}7\\%\\). Nos gráficos: A tem 4 de 10 partes pintadas (40%); B, 3 de 4 (75%); C, 5 de 8 (62,5%); D, 6 de 10 (60%); E, 1 de 4 (25%). O mais próximo de 41,7% é o da alternativa <strong>A</strong>.</p><p>O gráfico C tem 5 partes pintadas, como os 5 N.I.E.M.s, mas em 8 partes, e não em 12: ele representa 62,5%.</p>"},
45: {"materia": "História", "assunto": "Escravidão",
     "enunciado": p("O cotidiano da escravidão foi marcado por diversas formas de violências perpetradas por senhores e feitores, cujo intuito era submeter as pessoas escravizadas e evitar a rebelião contra este regime de trabalho. Muitas estratégias de resistência, porém, foram articuladas por escravizados.", "Entre elas, é correto mencionar"),
     "explicacao": "<p>Os <strong>quilombos</strong>, como o de Palmares, eram comunidades formadas por escravizados que fugiam, em várias regiões do Brasil. Foram uma das principais formas de resistência à escravidão. Alternativa <strong>E</strong>.</p><p>A Greve Geral de 1917 foi de operários, depois da abolição (A). Mandela lutou contra o apartheid no século XX, e não contra a escravidão no Brasil (B). Não havia fazendas de café na Amazônia nem no Rio Grande do Sul (C). E o Haiti era colônia francesa, e se tornou uma república, a primeira independente da América Latina (D).</p>"},
46: {"materia": "História", "assunto": "Brasil Império",
     "enunciado": apoio("Em 07 de setembro de 2022, o Brasil celebra os 200 anos de sua Independência, ocorrida em 1822. Entretanto, grande parte dos historiadores afirma que o processo de Independência começou anos antes, em 1808, quando a família real portuguesa chegou ao Brasil.",
                        "Sua chegada provocou transformações radicais na colônia e, principalmente, na cidade do Rio de Janeiro. Foram construídos chafarizes, pontes e calçadas; ruas e estradas foram abertas e pavimentadas. Entre 1808 e 1822, o número de habitantes da capital da colônia dobrou, chegando a cerca de 100 mil pessoas, muitos deles europeus que vinham tentar ganhar a vida no Brasil. Eram médicos, professores, alfaiates, farmacêuticos, modistas, cozinheiros, padeiros e formavam um grande contingente de mão de obra qualificada.",
                        "Por outro lado, os trabalhos mais duros continuavam sendo exercidos pelos escravizados, que eram utilizados nos serviços domésticos, no comércio e no transporte de todo o tipo de produtos pelas ruas da cidade.")
                  + fonte("&lt;https://tinyurl.com/exrp5ft5&gt; Acesso em: 28.05.2022. Adaptado.")
                  + p("Os eventos descritos no texto"),
     "explicacao": "<p>O texto mostra obras e a chegada de profissionais europeus qualificados ao Rio de Janeiro, mas diz que “os trabalhos mais duros continuavam sendo exercidos pelos escravizados”. Houve modernização sem mudar a estrutura escravista. Alternativa <strong>E</strong>.</p><p>A abolição só veio em 1888 (A). As obras ocorreram e a população dobrou (B e C). E a industrialização de São Paulo é do fim do século XIX e do século XX (D).</p>"},
47: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade",
     "enunciado": p("Leia a reportagem.")
                  + apoio("Na sexta-feira, 18 de março de 2022, a Operação Andrápodon resgatou oito vítimas de trabalho análogo ao escravo, na cidade de São Paulo. Durante a ação, oito imigrantes bolivianos foram libertados em uma confecção no Bom Retiro, na região central da capital.",
                          "Duas pessoas foram presas por tráfico de pessoas e organização criminosa. As vítimas trabalhavam até 14 horas por dia e ficavam 24 horas no mesmo local, dormindo ao lado da máquina de costura.",
                          "[...] “Essa operação é composta por três etapas: a primeira é de acolhimento; a segunda é um trabalho relacionado à capacitação, no qual as pessoas farão cursos de português e profissionalizantes, para inclusão social e profissional; a terceira etapa é de regularização, por meio do Centro de Integração da Cidadania do Imigrante (CIC) e do Núcleo de Enfrentamento ao Tráfico de Pessoas”, afirmou o Secretário de Justiça e Cidadania.")
                  + fonte("&lt;https://tinyurl.com/3968kkjw&gt; Acesso em: 26.03.2022. Adaptado.")
                  + p("De acordo com a reportagem, é correto afirmar que"),
     "explicacao": "<p>Os trabalhadores ficavam até 14 horas por dia trabalhando e dormiam ao lado da máquina de costura: <strong>condições degradantes</strong>, que caracterizam o trabalho análogo ao escravo. Alternativa <strong>E</strong>.</p><p>As vítimas serão acolhidas, capacitadas e regularizadas, não deportadas (A). A escravidão foi abolida em 1888, no século XIX (B). Os imigrantes podem entrar no Bom Retiro (C). E eles não tinham carteira assinada nem jornada legal (D).</p>"},
48: {"materia": "Geografia", "assunto": "Agropecuária e meio ambiente",
     "enunciado": apoio("Desde 1964, o Brasil comemora no dia 25 de maio o Dia do Trabalhador Rural. O país tem atualmente mais de 18 milhões de trabalhadores rurais. Esses trabalhadores somente conseguiram ter seus direitos equiparados aos demais em 1988, com a promulgação da Constituição da República atualmente em vigor. As conquistas, no entanto, convivem com diversos desafios, como a mecanização, a informalidade e o trabalho análogo à escravidão.",
                        "Em 1988, a Constituição da República equiparou os direitos trabalhistas e previdenciários de trabalhadores rurais aos dos urbanos, entre eles a extensão do Fundo de Garantia do Tempo de Serviço (FGTS).")
                  + fonte("&lt;https://tinyurl.com/bdfzmny5&gt; Acesso em: 26.03.2022. Adaptado.")
                  + p("De acordo com o texto, é correto afirmar que os trabalhadores rurais"),
     "explicacao": "<p>O texto diz que, em 1988, “a Constituição da República equiparou os direitos trabalhistas e previdenciários de trabalhadores rurais aos dos urbanos”. Alternativa <strong>C</strong>.</p><p>1964 é o ano em que começou a comemoração do Dia do Trabalhador Rural (A). O texto não compara o número de trabalhadores rurais e urbanos (B). Eles já eram trabalhadores antes de 1988; a Constituição igualou seus direitos (D). E o texto fala em extensão do FGTS, não em obrigação de previdência privada (E).</p>"},
49: {"materia": "Português", "assunto": "Interpretação de texto",
     "enunciado": POTE + P49,
     "explicacao": "<p>O pai disse a Ping: “Você fez o melhor que pôde e o possível deve ser apresentado ao imperador”. Esse conselho o encorajou a levar o pote vazio, sendo honesto mesmo com um resultado negativo. Alternativa <strong>C</strong>.</p><p>O imperador queria encontrar alguém honesto, não astuto (A). Os outros meninos trocaram as sementes queimadas, que nunca brotariam (B e E). E a fábula ensina o contrário de se omitir (D).</p>"},
50: {"materia": "Projeto de vida", "assunto": "Ética e cidadania",
     "enunciado": p("Com base no texto, uma atitude semelhante à do personagem Ping é"), "apoio_de": (49, P49),
     "explicacao": "<p>Ping levou o pote vazio e disse a verdade, mesmo envergonhado e sem saber o que aconteceria. A atitude semelhante é <strong>dizer a verdade independentemente das consequências</strong>. Alternativa <strong>C</strong>.</p><p>Deslealdade (A), esconder os fatos (D) e ficar com o troco a mais (E) são atitudes desonestas. E empatia (B) é uma qualidade, mas não é a que a fábula destaca em Ping.</p>"},
}
completar(Q, R)
