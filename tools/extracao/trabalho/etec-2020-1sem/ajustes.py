# Ajustes da conferência humana: Vestibulinho ETEC 1º semestre de 2020 (exame de 15/12/2019)
# Texto conferido com a imagem de cada página (e com o texto extraído do PDF). Gabarito: oficial (1SEM20).
# Prova sem tema único. Questão 23 anulada (sem motivo oficial publicado: justificativa por análise).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import A, carregar, enun, tabela, colunas, completar

META = {
    "id": "etec-2020-1sem",
    "banca": "ETEC",
    "ano": 2020,
    "semestre": 1,
    "titulo": "Vestibulinho ETEC, 1º semestre de 2020",
    "fonte": "Centro Paula Souza",
    "dataExame": "2019-12-15",
    "duracaoMinutos": 240,
    "apresentacao": "<p>Prezado(a) candidato(a), nesta prova você vai se deparar com diversos temas nas diferentes áreas do conhecimento.</p><p>As questões abordarão conceitos e conteúdos que fizeram parte de sua formação escolar e do seu cotidiano.</p><p>Boa prova!</p>",
    "pdf": "assets/provas/etec-2020-1sem.pdf",
}
EXTRAS = {"apresentacao": "Desenho a lápis de estudantes sentados em carteiras, concentrados, fazendo uma prova."}

R = carregar("etec-2020-1sem")


def p(*paragrafos, classe=None):
    abre = f'<p class="{classe}">' if classe else "<p>"
    return "".join(abre + x + "</p>" for x in paragrafos)


def apoio(*paragrafos):
    return '<p class="apoio">' + A.join(paragrafos) + "</p>"


def fonte(t):
    return f'<p class="fonte">{t}</p>'


def chamada(t):
    return f'<p class="chamada">{t}</p>'


# ---------- textos compartilhados ----------
BATERIAS = (chamada("Leia o texto para responder às questões 11 e 12.")
            + apoio("John Goodenough, Stanley Whittingham e Akira Yoshino são os vencedores do Prêmio Nobel 2019 de Química pelo desenvolvimento de baterias de íons de lítio. Atualmente, celulares, notebooks e carros elétricos saem de fábrica com esse tipo de bateria.",
                    "Com essa descoberta, é possível armazenar uma grande quantidade de energia em baterias pequenas e leves. Se fôssemos utilizar outros tipos de bateria, como por exemplo, bateria de hidreto de níquel ou bateria de níquel cádmio, para armazenarmos a mesma quantidade de energia, teríamos baterias com o tamanho e massa duas ou até mesmo três vezes maiores que as baterias de íons de lítio. Outra vantagem desse tipo de bateria é o fato de não possuírem o efeito memória, conhecido popularmente como o vício da bateria. Devido a essa característica que facilita a vida do usuário, ela não requer tanta atenção nos processos de carga e descarga.",
                    "Contudo, com todos os avanços, as baterias continuam extremamente sensíveis à temperatura. Quando expostas ao calor, podem perder parte de sua capacidade total e se decompor mais rápido que o normal."))
P11 = p("De acordo com o texto, é correto afirmar que")

CBERS = (chamada("Leia o texto para responder às questões 14 e 15.")
         + apoio("A imagem mostra o satélite brasileiro CBERS–4 utilizado para monitoramento do nosso território e para desenvolvimento científico.")
         + "[[fig:1]]" + fonte("&lt;https://tinyurl.com/yxcamrb3&gt; Acesso em: 10.10.2019. Original colorido.")
         + apoio("Como a maioria dos objetos colocados no espaço, o CBERS–4 é completamente envolvido por uma manta térmica protetora (Isolamento de Múltiplas Camadas, sigla em inglês MLI). Esse material tem como função diminuir o fluxo de calor, que pode ser um grande problema para objetos colocados em órbita, uma vez que facilmente eles podem ser submetidos a temperaturas maiores que 100 °C e menores que –100 °C."))
CBERS_IMG = {"arquivo": "q14", "alt": "Foto do satélite CBERS-4 no espaço: um corpo em forma de caixa, revestido por manta térmica, com um longo painel solar retangular estendido para a direita."}
P14 = p("No CBERS–4, com respeito à absorção de energia térmica proveniente do Sol, o revestimento térmico feito com o MLI, tem como função inibir a absorção de energia apenas por ____<strong>I</strong>____, tendo em vista que no espaço não existe ou é muito rarefeita a presença de matéria que poderia auxiliar no processo de troca de calor por ____<strong>II</strong>____ com a transferência do calor de partícula para partícula ou mesmo por ____<strong>III</strong>____, em que porções de matéria aquecida trocam de posição com porções de matéria contendo menos calor.",
        "Assinale a alternativa que completa correta e respectivamente as lacunas da frase.")

AMAZONIA = (chamada("Leia o texto para responder às questões de 18 a 21.")
            + apoio("O que liga a floresta Amazônica, o aquecimento mundial e você?",
                    "Há muito tempo a floresta Amazônica é reconhecida como um repositório de serviços ecológicos, <strong><u>não só</u></strong> para os povos indígenas e as comunidades locais, <strong><u>mas também</u></strong> para o restante do mundo. <strong><u>Além disso</u></strong>, de todas as florestas tropicais do mundo, a Amazônia é a única que ainda está conservada, em termos de tamanho e de diversidade.",
                    "<strong><u>No entanto</u></strong>, <strong><u>à medida que</u></strong> as florestas são queimadas ou retiradas e o processo de aquecimento global é intensificado, o desmatamento da Amazônia gradualmente desmonta os frágeis processos ecológicos que levaram anos para serem construídos e refinados.")
            + apoio("A floresta amazônica pode curar você",
                    "Durante milênios, os seres humanos utilizaram insetos, plantas e outros organismos da região para várias finalidades, entre elas a agricultura, a vestimenta e, claro, a cura para doenças. Povos indígenas e outros grupos que vivem na floresta amazônica aperfeiçoaram o uso de compostos químicos encontrados em plantas e em animais. O conhecimento sobre o uso dessas plantas geralmente fica nas mãos de um curandeiro que, por sua vez, repassa a tradição para um aprendiz. Esse processo se mantém ao longo de séculos e compõe uma parte integral da identidade desses povos.")
            + apoio("O potencial inexplorado das plantas amazônicas",
                    "Os cientistas acreditam que menos de 0,5% das espécies da flora foram detalhadamente estudadas quanto ao seu potencial medicinal. Ao mesmo tempo em que o bioma Amazônia está encolhendo lentamente em tamanho, a riqueza da vida silvestre de suas florestas também tem se reduzido, <strong><u>bem como</u></strong> o uso potencial das plantas e dos animais que ainda não foram descobertos.")
            + fonte("&lt;https://tinyurl.com/y4bprxq8&gt; Acesso em: 10.10.2019. Adaptado."))
P18 = (p("Sobre o texto, analise as afirmações:")
       + p("<strong>I.</strong> O desmatamento da floresta põe em risco, para além de suas riquezas naturais, a continuidade de conhecimentos tradicionais.",
           "<strong>II.</strong> Apesar da biodiversidade existente na floresta Amazônica, o impacto gerado pelo seu desmatamento restringe-se às comunidades e aos povos locais.",
           "<strong>III.</strong> A não preservação do bioma Amazônia pode acarretar impactos no clima mundial e até mesmo na pesquisa médico-científica.")
       + p("É correto o que se afirma em"))

FEIRA = (chamada("Leia o texto para responder às questões 22 e 23.")
         + apoio("A Feira do Peixe Vivo, em Caxias do Sul, visa promover uma melhor qualidade de vida à população ao estimular o consumo de peixes.",
                 "A feira ocorre uma vez ao mês e comercializa espécies como carpa capim (11 reais o quilograma), carpa húngara (9 reais o quilograma) e o bagre (X reais o quilograma).")
         + fonte("&lt;https://tinyurl.com/y39spmdy&gt; Acesso em: 07.10.2019. Adaptado."))
P22 = p("Em sua barraca, um piscicultor comercializava bagres, cujas massas variavam de 1,3 kg a 1,6 kg. Um freguês comprou o bagre de maior massa por R$ 25,00.",
        "De acordo com as informações do texto, é correto afirmar que")

MILHO = (chamada("Leia o texto para responder às questões 24 e 25.")
         + apoio("Vários estudiosos consideram que nenhum país do mundo é tão social, cultural e economicamente ligado ao milho quanto o México. Para começar, ele surgiu por lá. Há cerca de nove mil anos, povos que moravam onde hoje fica o México encontraram uma versão primitiva do milho, com uma espiga de uns 2,5 centímetros, e começaram a cultivá-lo. Até hoje, esse é um dos principais plantios do país.",
                 "No México, além do milho amarelo, que estamos acostumados a consumir no Brasil, podemos encontrar milhos de outras cores. Há o branco, que é muito comum, e também variedades vermelhas, azuis e pretas, por exemplo.",
                 "O maior número de variedades de milho no mundo se encontra no México: são 64 tipos (sendo 59 nativos do país) dentre as 220 variedades existentes em toda a América Latina. E o mais interessante é que, enquanto em outros países americanos as espécies primitivas desse cereal são consideradas “relíquias”, no México muitas delas continuam sendo usadas no dia a dia.",
                 "O México tem o maior consumo <em>per capita</em> de milho no mundo: são 63 kg anuais, contra uma média de 18 kg no Brasil, por exemplo. Em algumas comunidades, estima-se que esse alimento sozinho ofereça cerca de 70% das calorias e 50% das proteínas consumidas diariamente pela população.",
                 "Cerca de 75% da composição desse cereal é amido, substância muito usada pela indústria alimentícia e em produtos tão variados quanto resinas para a pintura de carros, sabão, pasta de dentes e plásticos biodegradáveis.",
                 "A glicose que vem do amido também é usada como meio de cultura de bactérias que produzem a penicilina e para revestir comprimidos, por exemplo.",
                 "Recentemente, pesquisadores descobriram que a jornada histórica do milho até chegar à versão atual foi mais complexa do que se imaginava, passando inclusive pelo Brasil. Seja como for, o certo é que, sem o trabalho humano, o milho provavelmente não existiria hoje. Isso decorre das características da planta que dificultam muito que ela espalhe suas sementes espontaneamente. Afinal, elas ficam bem presas à espiga e cobertas por folhas resistentes. Assim, os seres humanos são muito importantes para fazer com que o milho se reproduza de forma significativa. Isso, de certa forma, torna o vínculo entre homem e planta ainda mais forte.",
                 "Para algumas civilizações, no entanto, o laço é tão forte que é basicamente uma coisa só. Os maias, por exemplo, acreditavam que o homem veio do milho. No <em>Popol Vuh</em>, livro mais importante da mitologia Maia, encontra-se o seguinte: “De milho amarelo e milho branco se fez sua carne”. Existe, também, o mito de que o milho teria sido criado a partir das unhas do deus Cintéotl. Até hoje, muitos povos indígenas mexicanos consideram o milho uma divindade e dão a ele um caráter sagrado. Afinal, é dele que depende, em grande parte, a subsistência dessas comunidades. O grão é considerado precioso por assegurar a continuidade do ciclo da vida.",
                 "Mais recentemente, a luta dos indígenas mexicanos tem sido contra o cultivo de milho transgênico, que apesar de ser proibido, vem acontecendo há décadas. Usado para aumentar a produtividade e a resistência a pragas e a inseticidas, entre outros fins, o cereal transgênico provoca o desaparecimento de espécies nativas, além de prejudicar a agricultura familiar. Portanto, a forte relação com o milho vai muito além da planta em si, e além do próprio México. Ela traz também uma mensagem universal: nós, seres humanos, fazemos parte da terra. Dela dependemos, e dela devemos cuidar.")
         + fonte("&lt;https://tinyurl.com/y4y2a8hr&gt; Acesso em: 03.10.2019. Adaptado."))
P24 = p("De acordo com o texto, é correto afirmar que")

CALOR = (chamada("Leia o texto para responder às questões 26 e 27.")
         + apoio("Uma das consequências das trocas de calor, que ocorrem durante uma transformação química realizada em meio aquoso, é a variação de temperatura do sistema. Se o sistema receber calor, esse sofrerá um aumento de temperatura e, se ceder calor, terá queda de temperatura.",
                 "Durante uma reação química realizada em meio aquoso, observa-se a variação da temperatura do sistema de 22 °C para 28 °C."))
P26 = p("Conclui-se, corretamente, que se trata de uma reação")

DIALOGO = (chamada("Leia o diálogo entre Menipo e Hermes para responder às questões de 30 a 32.")
           + apoio("O diálogo, desenvolvido entre as personagens Menipo e Hermes, faz parte do livro <em>Diálogo dos Mortos</em>, do escritor Luciano de Samósata.",
                   "<strong>Menipo</strong> – Onde estão os belos e as belas, Hermes<sup>1</sup>? Leva-me até eles, pois eu sou novato aqui.",
                   "<strong>Hermes</strong> – Não tenho tempo, Menipo. Mas, olha aquilo ali, à direita: ali está Jacinto, também Narciso e Nireu e Aquiles<sup>2</sup>; e ainda Tiró, Helena<sup>3</sup>, Leda, em suma, todas as beldades antigas.",
                   "<strong>Menipo</strong> – Eu estou vendo só ossos e crânios desprovidos de carnes, a maioria desses semelhantes.",
                   "<strong>Hermes</strong> – Contudo, aqueles são os ossos que todos os poetas admiram e que tu pareces desprezar.",
                   "<strong>Menipo</strong> – Mesmo assim, mostra-me Helena, pois eu não saberia reconhecê-la.",
                   "<strong>Hermes</strong> – Esse crânio aí é Helena.",
                   "<strong>Menipo</strong> – Então é por causa disso aí que foram lotados milhares de navios da Grécia inteira e tombaram tantos gregos e bárbaros, e tantas cidades foram arrasadas!",
                   "<strong>Hermes</strong> – Mas, Menipo, tu não viste essa mulher em vida; senão tu também terias dito que não merece castigo “sofrer dores por muito tempo por uma mulher”, porque também as flores secas, se alguém as contempla depois que elas perdem o viço, é evidente que lhe parecerão murchas; mas enquanto florescem e mantêm o colorido, elas são muito belas.",
                   "<strong>Menipo</strong> – Pois é isso mesmo que me causa admiração, Hermes: que os Aqueus<sup>4</sup> não perceberam que estavam sofrendo por uma coisa tão efêmera e tão facilmente perecível.")
           + fonte("Luciano de Samósata, Diálogo dos Mortos. Trad. Henrique G. Murachco. Edusp: São Paulo, p. 67.")
           + fonte("1. Hermes: divindade grega posteriormente assimilada à representação do deus Mercúrio, pela mitologia romana. Na cena, Hermes entrega as almas a Caronte, que se encarrega de fazê-las atravessar o Aqueronte, rio que separa o mundo dos vivos e dos mortos.<br>"
                   "2. Aquiles: filho de Peleu e Tétis, o mais valente dos heróis na guerra de Troia, de cabeleira dourada. É jovem, forte e belo. Morre em plena juventude; por isso ele está ao lado de beldades, tais como Jacinto e Narciso.<br>"
                   "3. Helena: mulher de Menelau, raptada por Páris, filho de Príamo, rei de Troia, foi a causa da guerra que levou ao Hades milhares de almas de heróis, segundo Homero.<br>"
                   "4. Aqueu: relativo aos aqueus, um dos quatro ramos do povo grego antigo, ou indivíduo dos aqueus, relativo à Acaia (antiga Grécia), ou ao seu natural ou habitante."))
P30 = p("Luciano de Samósata, escritor grego do século II, mistura em sua obra dois gêneros diferentes: a Comédia, destinada ao riso; e o Diálogo, destinado às reflexões filosóficas.",
        "Sobre o conteúdo reflexivo-filosófico do diálogo transcrito, depreende-se corretamente que")

APOLLO = (chamada("Leia o texto para responder às questões 36 e 37.")
          + apoio("Em suas últimas viagens o programa Apollo levou um veículo capaz de mover-se sobre a superfície lunar com uma velocidade máxima de 13 km/h. As baterias desse veículo permitiam uma autonomia para 92 km.",
                  "O veículo era muito leve. Na Terra, seu peso era aproximadamente 2 100 N, enquanto que, na Lua, pesava cerca de 350 N."))
P36 = p("Admita que os astronautas, ao utilizarem o veículo lunar, mantiveram velocidade constante igual à velocidade máxima. Assim sendo, a expectativa do tempo de uso do veículo, até o total esgotamento de suas baterias, seria de aproximadamente")

SORO = (chamada("Leia o texto para responder às questões 40 e 41.")
        + apoio("O soro fisiológico é uma solução utilizada para diversos fins, dentre os quais: limpar olhos e nariz, lavar queimaduras e feridas, hidratações e nebulizações. É uma solução de cloreto de sódio de concentração 0,9% (massa/volume). Essa concentração corresponde à razão entre à massa de cloreto de sódio, em gramas, e o volume de 100 mL da solução."))
P40 = p("Um paciente desidratado, em que é administrado 500 mL de soro na veia, receberá uma massa de sal correspondente a")

BOTAS = (chamada("Leia os quadrinhos e o quadro “VOCÊ SABIA?” para responder às questões 43 e 44.")
         + "[[fig:1]]" + fonte("&lt;https://tinyurl.com/y4kfnoc3&gt; Acesso em: 07.10.2019. Original colorido.")
         + apoio("<strong>VOCÊ SABIA?</strong>",
                 "O Sistema Métrico é um sistema de medição reconhecido internacionalmente. Ele surgiu durante a Revolução Francesa em virtude da existência de diversos padrões de medida que dificultavam o funcionamento do comércio e da indústria.",
                 "A légua é uma unidade de comprimento que não pertence ao Sistema Métrico, cuja ideia base era de que corresponderia aproximadamente ao caminho percorrido por um homem caminhando a pé durante uma hora.",
                 "No Brasil, de acordo com o dicionário Houaiss, uma légua equivale a 6,6 km.",
                 "As Botas de Sete Léguas, da fábula, permitem à pessoa que as usa conseguir dar passos que valem sete léguas cada um."))
BOTAS_IMG = {"arquivo": "q43", "alt": "Tirinha “Cientirinhas #123”, em quatro quadros. Uma avó, sentada numa poltrona com um livro, diz à neta: “Vou te contar a fábula da corrida entre a lebre e a tartaruga.” A menina corrige: “Jabuti.” No segundo quadro, a avó diz “Oi, meu bem?” e a menina explica: “Tartarugas são aquáticas, vovó. Se a corrida for em terra, tem que ser um jabuti.” No terceiro, a avó diz: “Melhor mudar de história. Vou te contar a fábula das Botas de Sete Léguas.” No último, a menina pergunta, sorrindo: “Tá. Mas dá pra ser no sistema métrico?”, e a avó apoia a cabeça na mão, desanimada."}

# ---------- questões ----------
Q = {
1: {"materia": "Matemática", "assunto": "Operações e problemas", "tags": ["números primos"],
    "enunciado": p("Um número natural, diferente de zero e diferente de um, pode ser classificado como primo ou composto.",
                   "Os quadrinhos fornecem algumas pistas sobre o que permite caracterizar um número para que ele seja dito primo.")
                 + "[[fig:1]]" + fonte("&lt;https://tinyurl.com/y2xxx63q&gt; Acesso em: 07.10.2019. Original colorido.")
                 + p("Analise as alternativas e assinale a correta."),
    "imagens": [{"arquivo": "q01", "alt": "Tirinha “Cientirinhas #143”, em quatro quadros, sob a faixa “Encontro anual de primos”. Personagens usam camisetas com números primos. O de camiseta 2 diz ao de camiseta 23: “Saudades, primo. Você é um cara ímpar!”, e ouve: “Você diz isso pra todo mundo aqui na festa.” Os de camisetas 37 e 73 comentam: “Bacana ver que a turma continua unida.” “Verdade! É uma galera que não se deixa dividir por qualquer fator.” Os de camisetas 61 e 137 perguntam: “Você sabe quem é aquele sujeito?” “Também não conheço. É um primo distante.” No último quadro, um rapaz afastado, de óculos e celular na mão, usa a camiseta 6056 52931 6217, e alguém comenta: “Ouvi dizer que ele trabalha com criptografia.”"}],
    "explicacao": "<p>Os números primos menores que 10 são <strong>2, 3, 5 e 7</strong>: apenas quatro. Alternativa <strong>E</strong>.</p><p>Na tirinha, o número 6 056 529 316 217 está “distante” por ser um primo muito grande, usado em criptografia, e não por deixar de ser primo (A). 16 é par e 61 é primo, mas 16 = 2 × 8 não é (B). 237 = 3 × 79, logo não é primo (C). E o 2 é primo e par, e o 5 termina em 5 (D).</p>"},
2: {"materia": "Biologia", "assunto": "Fisiologia humana",
    "explicacao": "<p>No frio, o corpo precisa <strong>perder menos calor</strong>. Os vasos sanguíneos da pele se contraem (vasoconstrição), levando menos sangue quente para a superfície, e as glândulas sudoríparas eliminam menos suor, que resfriaria a pele ao evaporar. Alternativa <strong>D</strong>.</p><p>A dilatação dos vasos (A, B e C) aumenta a perda de calor, e é o que acontece no calor. Suor é produzido pelas glândulas sudoríparas, não pelas sebáceas, que produzem oleosidade (C e E).</p>"},
3: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["fome"],
    "enunciado": apoio("Sabemos que a humanidade é capaz de produzir o necessário para banir do planeta o problema da subalimentação. Apesar disso, a fome no mundo concentra-se em países da África subsaariana (e, em menor proporção, na Índia e no Paquistão) e persiste por causa do protecionismo econômico dos países ricos. A esmagadora maioria dos que não conseguem preencher suas necessidades básicas vive em regiões rurais, e a escassa renda que obtêm deriva da agricultura. Aumentar a produção agropecuária é fundamental, como bem sublinhou o secretário-geral da ONU, mas o mais importante é criar condições para que os que vivem em situação de pobreza absoluta conquistem o direito de produzir a própria alimentação.")
                 + fonte("&lt;https://tinyurl.com/y3837qsq&gt; Acesso em: 01.10.2019. Adaptado.")
                 + p("De acordo com o texto, é correto afirmar que"),
    "explicacao": "<p>O texto começa dizendo que “a humanidade é capaz de produzir o necessário para banir do planeta o problema da subalimentação”. Ou seja, é possível acabar com ela. Alternativa <strong>D</strong>.</p><p>A fome se concentra justamente em países pobres (A) e atinge sobretudo moradores de regiões rurais (B). O texto fala em produção agropecuária, não industrial (C). E a causa apontada é o protecionismo econômico dos países ricos, não uma proteção militar (E).</p>"},
4: {"materia": "Química", "assunto": "Substâncias e misturas",
    "enunciado": p("No estudo de substâncias puras e misturas, a professora apresentou dois sistemas a seus alunos, conforme representado nas figuras.")
                 + "[[fig:1]]"
                 + p("Ela solicitou que analisassem e fizessem duas afirmações sobre cada sistema. Nas alternativas, encontram-se algumas das afirmações feitas pelos alunos.",
                     "Analise-as e assinale a alternativa que apresenta apenas a afirmação correta sobre um dos sistemas representados."),
    "imagens": [{"arquivo": "q04", "alt": "Dois recipientes. Sistema 1: cinco moléculas, cada uma formada por duas esferas iguais: três moléculas de duas esferas escuras e duas moléculas de duas esferas claras. Sistema 2: duas moléculas iguais, cada uma com uma esfera grande clara ligada a duas esferas pequenas escuras."}],
    "explicacao": "<p>No sistema 1 há dois tipos de molécula: uma formada por dois átomos escuros e outra por dois átomos claros. Cada uma tem átomos de um só elemento, então são <strong>duas substâncias simples</strong>. Alternativa <strong>A</strong>.</p><p>Por ter dois tipos de molécula, o sistema 1 é uma mistura, e não uma substância pura (B); e tem dois componentes, não cinco (C). O sistema 2 tem só um tipo de molécula: é uma substância pura (D), com um único componente (E).</p>"},
5: {"materia": "História", "assunto": "Povos indígenas", "tags": ["fontes históricas"],
    "enunciado": apoio("Eu herdei da minha mãe esse trabalho de artesanato com barro. E, desde a minha bisavó, já se fazia desse jeito. Ela era índia. Então, a minha mãe fazia pote, bilha, qualquer tipo de louça. A gente faz assim: pega o barro mole, mistura com caraipé*, amassa até ele ficar mesmo bem ligado e, depois que ele já está bem ligado, a gente já vai começar a formar a louça. Agora, tem que ter uma coisa, tem que saber a temperatura e a quantia que o barro pega do caraipé. Se estiver bem areadinho, ele já tá bom. E eu tenho esperança que meu filho também vai continuar a trabalhar e alguém além dele vai também. Vai aprender um filho dele, um sobrinho, porque toda criança sempre mostra logo uma coisa que ela quer ser, que ela quer fazer. Eu acho que vai ter alguém assim, não vai ficar parado, não. Vão continuar a fazer essas panelas aqui.")
                 + fonte("&lt;https://tinyurl.com/y6lw6rbu&gt; Acesso em: 09.10.2019.")
                 + fonte("* Árvore cujas cinzas são utilizadas pelos oleiros da região Amazônica para misturar com o barro, também denominada caripé-verdadeiro (<em>Licania floribunda</em>).")
                 + p("O depoimento de Maria da Saúde de Souza, artesã do Pará, foi gravado em vídeo e transcrito pelo Museu da Pessoa, <em>website</em> dedicado a coletar e a publicar as histórias de vida de milhares de brasileiros.",
                     "Os depoimentos orais são considerados fontes"),
    "explicacao": "<p>O depoimento de Maria registra um saber passado de geração a geração (da bisavó para a mãe, dela para o filho). Relatos orais como esse são <strong>fontes históricas</strong>: guardam conhecimentos tradicionais e a visão de quem viveu os fatos. Alternativa <strong>A</strong>.</p><p>Fontes orais não servem para fortalecer preconceitos (B), não dependem de repórteres de grandes portais (C) nem de certificação por organismos diplomáticos (D). E não são “mitológicas” nem dependem de ratificação de cientistas (E).</p>"},
6: {"materia": "Física", "assunto": "Dinâmica", "tags": ["leis de Newton"],
    "enunciado": p("Com a promessa de tornar economicamente mais viáveis os voos espaciais, uma empresa demonstrou ser capaz de fazer retornarem os propulsores de seu foguete. A recuperação desses propulsores possibilita que eles sejam reparados para serem reutilizados em novos lançamentos.",
                   "Após terem cumprido sua função, os propulsores do foguete se desprendem, caindo aceleradamente em direção ao planeta. Ao se aproximarem da superfície, retropropulsores são acionados, imprimindo uma força vertical e para cima de intensidade ____<strong>I</strong>____ que a do peso dos propulsores, diminuindo contínua e drasticamente a velocidade de queda, até próximo ao toque no solo. Nesse momento, os retropropulsores imprimem uma força vertical e para cima de intensidade ____<strong>II</strong>____ a do peso dos propulsores, o que os mantém pairando, sem velocidade, enquanto os computadores avaliam a telemetria para, finalmente, diminuírem até zero a retropropulsão.",
                   "Assinale a alternativa que completa correta e respectivamente as lacunas da frase."),
    "alternativas": colunas(["I", "II"], [["maior", "menor que"], ["maior", "igual"], ["maior", "maior que"], ["menor", "igual"], ["menor", "maior que"]]),
    "explicacao": "<p>Para frear uma queda, a força resultante precisa apontar para cima: a força dos retropropulsores tem de ser <strong>maior</strong> que o peso (I). Para ficar pairando parado, a resultante deve ser nula (primeira lei de Newton): a força tem de ser <strong>igual</strong> ao peso (II). Alternativa <strong>B</strong>.</p><p>Com força menor que o peso, o propulsor continuaria acelerando para baixo (D e E). E, pairando, uma força maior ou menor que o peso faria o propulsor subir ou cair (A e C).</p>"},
7: {"materia": "Português", "assunto": "Figuras de linguagem",
    "enunciado": p("Leia a charge.") + "[[fig:1]]"
                 + apoio("Lutei toda uma vida contra tudo e contra todos! Batalhei! Caí! Levantei! Criei filhos e família!",
                         "Heroicamente! Denodadamente! Como um mártir",
                         "agora ficam me cobrando: paga imposto de renda! Paga taxa!",
                         "paga ICM! Corro pra lá: olha o fiscal me cobrando...!",
                         "não pago! Não pago! Não pago! Não pago! Não pago!",
                         "é este aí o famoso herói cobrado retumbante!")
                 + fonte("Antologia do Pasquim, v.2: 1972-1973. Desiderata: Rio de Janeiro, 2007, p. 90.")
                 + p("A charge de Ziraldo foi publicada na década de 1970 e, apesar da diferença histórico-cultural com o contexto atual, é possível apreender seu efeito de humor.",
                     "A expressão responsável pela construção do humor no texto é"),
    "imagens": [{"arquivo": "q07", "alt": "Charge de Ziraldo em seis quadros, em preto e branco, com o mesmo homem magro em poses dramáticas: braços erguidos, mão no peito, gritando. As falas dos balões estão transcritas logo abaixo da imagem. No último quadro, o homem, curvado e cansado, segura papéis, e alguém o apresenta como o famoso “herói cobrado retumbante”."}],
    "explicacao": "<p>“Herói cobrado retumbante” imita o som de um verso famoso do Hino Nacional (“de um povo heroico o brado retumbante”), trocando “brado” por “cobrado”. Esse jogo com palavras de som parecido e sentido diferente é a <strong>paronomásia</strong>, e é dele que vem o humor. Alternativa <strong>D</strong>.</p><p>Repetir “não pago!” não suaviza nada, então não é eufemismo (A). “Contra tudo e contra todos” não é ironia (B). Os verbos de C não se contradizem. E as expressões de E exaltam a personagem, em vez de atingir sua autoestima.</p>"},
8: {"materia": "Matemática", "assunto": "Geometria plana",
    "explicacao": "<p>Um polígono convexo com quatro ângulos é um quadrilátero. Com <strong>todos os lados iguais</strong> e dois ângulos agudos e dois obtusos, é um <strong>losango</strong> (que não é quadrado). Alternativa <strong>A</strong>.</p><p>O pentágono tem cinco ângulos e o triângulo, três (B e E). O quadrado e o retângulo têm quatro ângulos retos, nenhum agudo nem obtuso (C e D).</p>"},
9: {"materia": "Biologia", "assunto": "Ecologia", "tags": ["ciclo do carbono"],
    "enunciado": p("Fundamental à manutenção da vida na Terra, o ciclo biogeoquímico do carbono na natureza está representado simplificadamente no esquema.")
                 + "[[fig:1]]" + p("Sobre esse esquema é correto afirmar que"),
    "imagens": [{"arquivo": "q09", "alt": "Esquema com dois processos. Processo 1: entram água e gás carbônico; saem oxigênio e compostos orgânicos (exemplo: glicose). Processo 2: entram oxigênio e compostos orgânicos; saem gás carbônico e água."}],
    "explicacao": "<p>O processo 1 consome água e gás carbônico e libera oxigênio e glicose: é a <strong>fotossíntese</strong>, feita pelos vegetais, que produzem matéria orgânica. O processo 2 faz o caminho inverso: é a respiração. Alternativa <strong>E</strong>.</p><p>Animais não fazem fotossíntese (B, C e D). A decomposição (A) libera gás carbônico, e não oxigênio. E a respiração (processo 2) é feita por animais e vegetais, mas consome compostos orgânicos em vez de produzi-los.</p>"},
10: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["globalização"],
     "enunciado": apoio("Na América do Sul, ninguém gasta mais em <em>fast-food</em> do que os brasileiros. Aliás, segundo um estudo realizado pela <em>EAE Business School</em>, que analisou os hábitos de consumo nesse setor em 2014, apenas os Estados Unidos (290,2 bilhões de reais), o Japão (162,3 bilhões de reais) e a China (130,2 bilhões de reais) estão à frente do Brasil (53,7 bilhões de reais) em gastos no setor. De acordo com o levantamento, o gasto com <em>fast-food</em> por habitante no Brasil em 2014 foi de 265 reais, e o consumo deve crescer em 30,88% até 2019 — uma das maiores expectativas entre os países estudados, junto com Espanha (48,61%) e China (23,99%). Os espanhóis, aliás, estão entre os europeus que menos gastam com <em>fast-food</em>. Cada habitante investe em média 42,6 euros por ano. Essa cifra os situa somente atrás dos italianos.")
                  + fonte("&lt;https://tinyurl.com/y4o9to83&gt; Acesso em: 03.10.2019. Adaptado.")
                  + p("O crescimento do tipo de restaurante retratado no texto se deve ao"),
     "explicacao": "<p>As redes de <em>fast-food</em> se espalharam pelo mundo junto com a <strong>globalização</strong>, que padroniza produtos e muda hábitos de consumo, inclusive os alimentares, em vários países ao mesmo tempo. Alternativa <strong>D</strong>.</p><p>O texto não liga o fenômeno ao desemprego, e <em>fast-food</em> não é sinônimo de comida mais nutritiva (A). O <em>slow food</em> é justamente o movimento contrário (B). A comida local de vilarejos não é o que essas redes vendem (C). E o <em>fast-food</em> é um fenômeno do século XX, não das feiras medievais (E).</p>"},
11: {"materia": "Química", "assunto": "Interpretação de dados", "tags": ["baterias"],
     "enunciado": BATERIAS + P11,
     "explicacao": "<p>O texto diz que as baterias de íons de lítio, usadas hoje em celulares, notebooks e carros elétricos, guardam muita energia em “baterias pequenas e leves” e, sem efeito memória, “não requer tanta atenção nos processos de carga e descarga”. Alternativa <strong>D</strong>.</p><p>Os carros elétricos usam baterias de íons de lítio (A). As de hidreto de níquel é que seriam maiores e mais pesadas (B). As de lítio não têm efeito memória (C). E elas continuam sensíveis ao calor (E).</p>"},
12: {"materia": "Química", "assunto": "Funções inorgânicas", "tags": ["ligação iônica"],
     "enunciado": p("Os íons de lítio, usados em baterias, são provenientes de compostos iônicos. Um exemplo de composto iônico é o sal cloreto de sódio, no qual átomos de sódio se ligam a átomos de cloro por meio de ligação iônica, na razão de 1:1, como todos os cloretos de metais alcalinos.",
                    "Sabendo que o lítio também é um metal alcalino, podemos afirmar que os átomos de lítio se ligam a átomos de cloro formando o composto cloreto de lítio, representado, corretamente, por"),
     "apoio_de": (11, P11),
     "alternativas": {"A": "Li<sub>2</sub>Cℓ", "B": "Li<sub>2</sub>Cℓ<sub>2</sub>", "C": "CℓLi<sub>2</sub>", "D": "Cℓ<sub>2</sub>Li<sub>2</sub>", "E": "LiCℓ"},
     "explicacao": "<p>Como o sódio, o lítio é um metal alcalino e forma o íon Li<sup>+</sup>; o cloro forma Cℓ<sup>–</sup>. Eles se combinam na razão 1:1, como no NaCℓ. Na fórmula, o cátion vem primeiro: <strong>LiCℓ</strong>. Alternativa <strong>E</strong>.</p><p>As fórmulas A e C têm razão 2:1. As de B e D usam índices desnecessários (a fórmula de um composto iônico usa a menor proporção) e, em C e D, o ânion aparece antes do cátion.</p>"},
13: {"materia": "História", "assunto": "Brasil Colônia",
     "explicacao": "<p>O sistema de <em>plantation</em> combinava <strong>monocultura</strong> (cana-de-açúcar), produção para o <strong>mercado externo</strong> (a Europa), grandes propriedades (<strong>latifúndios</strong>) e <strong>mão de obra escravizada</strong>. Alternativa <strong>C</strong>.</p><p>A agricultura diversificada e familiar (A) e o extrativismo para o mercado interno (B) são o oposto. A mão de obra era escrava, não livre (D). E a produção não era mecanizada nem voltada para o mercado interno (E).</p>"},
14: {"materia": "Física", "assunto": "Termologia", "tags": ["propagação do calor"],
     "enunciado": CBERS + P14, "imagens": [CBERS_IMG],
     "alternativas": colunas(["I", "II", "III"], [["condução", "convecção", "irradiação"], ["condução", "irradiação", "convecção"], ["convecção", "condução", "irradiação"], ["irradiação", "condução", "convecção"], ["irradiação", "convecção", "condução"]]),
     "explicacao": "<p>No vácuo do espaço, o calor do Sol só chega por <strong>irradiação</strong> (ondas eletromagnéticas), que é o que a manta precisa barrar (I). A troca “de partícula para partícula” é a <strong>condução</strong> (II), e a troca de posição entre porções quentes e frias de matéria é a <strong>convecção</strong> (III). As duas precisam de matéria, quase inexistente no espaço. Alternativa <strong>D</strong>.</p><p>As outras alternativas trocam a ordem dos três processos.</p>"},
15: {"materia": "Física", "assunto": "Termologia", "tags": ["escalas termométricas"],
     "enunciado": p("Se o texto desta questão fosse direcionado a leitores estadunidenses, ele teria que sofrer não apenas uma tradução para a língua inglesa como também uma conversão da escala termométrica utilizada. Isso ocorre porque os estadunidenses utilizam cotidianamente a unidade de temperatura denominada Fahrenheit.",
                    "A conversão de valores expressos na escala Celsius para a escala Fahrenheit é feita utilizando-se a expressão de conversão, \\(\\dfrac{t_C}{5} = \\dfrac{t_F - 32}{9}\\), em que <strong>t<sub>C</sub></strong> é um valor de temperatura expresso na escala Celsius e <strong>t<sub>F</sub></strong>, o valor correspondente de temperatura expresso na escala Fahrenheit.",
                    "Nessas condições, a menor temperatura que apareceria no texto em língua inglesa é"),
     "apoio_de": (14, P14),
     "explicacao": "<p>A menor temperatura do texto é –100 °C. Na fórmula: \\(\\dfrac{-100}{5} = \\dfrac{t_F - 32}{9}\\), ou seja, \\(-20 \\times 9 = t_F - 32\\), e \\(t_F = -180 + 32 = -148\\) °F. Alternativa <strong>C</strong>.</p><p>212 °F corresponde a 100 °C, a maior temperatura do texto (E). Os demais valores vêm de erros de sinal ou de conta.</p>"},
16: {"materia": "Biologia", "assunto": "Fisiologia humana", "tags": ["sistema circulatório"],
     "enunciado": p("O coração de um mamífero possui uma completa separação entre os ventrículos. Essa separação não permite a mistura do sangue venoso com o sangue arterial.",
                    "O esquema refere-se ao sistema circulatório dos mamíferos.")
                  + "[[fig:1]]" + p("Sobre esse esquema, podemos afirmar, corretamente, que os números I, II, III e IV representam, respectivamente,"),
     "imagens": [{"arquivo": "q16", "alt": "Esquema “Mamíferos”: três caixas, Tecidos, Coração e Pulmões. A seta I vai dos tecidos ao coração; a seta II vai dos pulmões ao coração; a seta III vai do coração aos tecidos; a seta IV vai do coração aos pulmões."}],
     "alternativas": colunas(["I", "II", "III", "IV"], [["veias cavas", "veias pulmonares", "artéria pulmonar", "artéria aorta"],
                                                       ["veias cavas", "veias pulmonares", "artéria aorta", "artéria pulmonar"],
                                                       ["artéria aorta", "artéria pulmonar", "veias cavas", "veias pulmonares"],
                                                       ["artéria aorta", "veias pulmonares", "artéria pulmonar", "veias cavas"],
                                                       ["veias pulmonares", "veias cavas", "artéria aorta", "artéria pulmonar"]]),
     "explicacao": "<p>Veias chegam ao coração e artérias saem dele. Do corpo (tecidos) para o coração, o sangue volta pelas <strong>veias cavas</strong> (I); dos pulmões, pelas <strong>veias pulmonares</strong> (II). Do coração para o corpo, sai pela <strong>artéria aorta</strong> (III); para os pulmões, pela <strong>artéria pulmonar</strong> (IV). Alternativa <strong>B</strong>.</p><p>A troca III e IV entre aorta e pulmonar. C e D chamam de artéria vasos que chegam ao coração. E E inverte as veias.</p>"},
17: {"materia": "Geografia", "assunto": "Agropecuária e meio ambiente",
     "enunciado": apoio("A atividade pecuária possui grande representatividade na economia brasileira. Não é novidade que o Brasil possui um dos maiores rebanhos comerciais de bovinos do mundo. Essa atividade gera milhões de empregos diretos e indiretos, e 20% do território nacional é ocupado com pastagens que são destinadas à criação do gado.")
                  + fonte("&lt;https://tinyurl.com/y3h9zq4o&gt; Acesso em: 07.10.2019. Adaptado.")
                  + p("Assim como na agricultura, a atividade pecuária se diferencia em extensiva e intensiva.", "A pecuária intensiva é um sistema"),
     "explicacao": "<p>Na pecuária <strong>intensiva</strong>, os animais são criados em áreas menores, com muito investimento e tecnologia (ração, confinamento, <strong>melhoramento genético e inseminação artificial</strong>), o que dá alta produtividade. Alternativa <strong>D</strong>.</p><p>Criação solta em grandes áreas, alimentada pelo pasto, com técnicas tradicionais e suplementos baratos (A, B, C e E) descreve a pecuária extensiva.</p>"},
18: {"materia": "Português", "assunto": "Interpretação de texto",
     "enunciado": AMAZONIA + P18,
     "explicacao": "<p>I está correta: o texto diz que o conhecimento sobre as plantas, passado de curandeiro para aprendiz, faz parte da identidade dos povos da floresta, e o desmatamento ameaça isso. III também: o desmatamento se liga ao aquecimento global e à perda de plantas de potencial medicinal ainda não estudadas. Alternativa <strong>D</strong>.</p><p>II está errada: o texto diz que os serviços ecológicos da floresta servem “para o restante do mundo”, e não só aos povos locais.</p>"},
19: {"materia": "Português", "assunto": "Conectivos",
     "enunciado": p("Observe os elementos de coesão destacados no texto.",
                    "Analisando seu contexto de ocorrência, assim como suas funções sintático-semânticas, afirma-se corretamente que"),
     "apoio_de": (18, P18),
     "explicacao": "<p>“Não só... mas também”, “além disso” e “bem como” acrescentam informações: são locuções conjuntivas (ou conectivos) de <strong>adição</strong>. Alternativa <strong>B</strong>.</p><p>“Não só” não nega nada; faz parte da adição (A). “No entanto” é adversativo e não pode virar “porque”, que é causal (C). “À medida que” indica proporção e está bem empregado (D). E “mas também” soma, não opõe (E).</p>"},
20: {"materia": "Português", "assunto": "Funções da linguagem",
     "enunciado": p("A função referencial ou informativa, predominante no texto apresentado e uma das mais frequentes no cotidiano, tem por objetivo informar o leitor.",
                    "Para alcançar seu intento, o autor recorre a determinadas construções linguísticas, tal como"),
     "apoio_de": (18, P18),
     "explicacao": "<p>O texto usa verbos no presente para descrever a situação atual da floresta (“é reconhecida”, “está encolhendo”) e no pretérito perfeito para o uso tradicional das plantas (“utilizaram”, “aperfeiçoaram”). Alternativa <strong>B</strong>.</p><p>Não há verbos no subjuntivo para hipóteses (A), nem imperativos e vocativos dirigidos ao leitor, típicos da função apelativa (C). O texto não é narrativo (D), e a linguagem conotativa não traz objetividade (E).</p>"},
21: {"materia": "Português", "assunto": "Coesão e referência", "tags": ["pronome relativo"],
     "enunciado": p("Antecedente é a palavra empregada pela gramática tradicional para identificar o termo ao qual o pronome relativo se refere em uma oração.",
                    "Assinale a alternativa cujo antecedente do pronome relativo está corretamente destacado."),
     "apoio_de": (18, P18),
     "alternativas": {"A": "“...o desmatamento da Amazônia gradualmente desmonta <strong><u>os frágeis processos ecológicos</u></strong> que levaram anos para serem construídos e refinados.”",
                      "B": "“O conhecimento sobre o uso dessas plantas geralmente fica nas <strong><u>mãos</u></strong> de um curandeiro, que por sua vez repassa a tradição para um aprendiz...”",
                      "C": "“Além disso, de todas as florestas tropicais do <strong><u>mundo</u></strong>, a Amazônia é a única que ainda está conservada, em termos de tamanho e diversidade.”",
                      "D": "“Os cientistas <strong><u>acreditam</u></strong> que menos de 0,5% das espécies da flora foram detalhadamente estudadas...”",
                      "E": "“Ao mesmo tempo em que o <strong><u>bioma</u></strong> Amazônia está encolhendo lentamente em tamanho...”"},
     "explicacao": "<p>Em A, “que” é pronome relativo e retoma “os frágeis processos ecológicos”: são eles que “levaram anos para serem construídos”. Alternativa <strong>A</strong>.</p><p>Em B, o “que” retoma “um curandeiro”, não “mãos”. Em C, retoma “a única” (a Amazônia), não “mundo”. Em D, “que” é conjunção integrante, sem antecedente. E em E, “em que” faz parte da locução “ao mesmo tempo em que”, que indica tempo.</p>"},
22: {"materia": "Matemática", "assunto": "Razão e proporção",
     "enunciado": FEIRA + P22,
     "alternativas": {"A": "X &lt; 15.", "B": "15 &lt; X &lt; 20.", "C": "15 &gt; X &gt; 20.", "D": "15 &lt; X &gt; 20.", "E": "X &gt; 20."},
     "explicacao": "<p>O bagre de maior massa tem 1,6 kg e custou R$ 25,00. O preço do quilograma é \\(X = 25 \\div 1{,}6 = 15{,}625\\) reais. Então <strong>15 &lt; X &lt; 20</strong>. Alternativa <strong>B</strong>.</p><p>A e E ficam fora do valor encontrado. C e D são desigualdades impossíveis ou mal escritas: nenhum número é ao mesmo tempo menor que 15 e maior que 20.</p>"},
23: {"materia": "Matemática", "assunto": "Operações e problemas", "tags": ["sistemas de equações"],
     "enunciado": p("Suponha que um dos piscicultores comercialize apenas carpas capim e carpas húngaras. Em março, esse piscicultor levou à feira 1 200 carpas e conseguiu vender 90% delas, obtendo um faturamento de R$ 11.380,00.",
                    "Nessas condições, o número de carpas húngaras que o piscicultor vendeu foi igual a"),
     "apoio_de": (22, P22),
     "anulacao": {"fonte": "analise",
                  "motivo": "O Centro Paula Souza anulou a questão sem divulgar o motivo. Pela nossa análise, faltam dados: o texto dá os preços das carpas por quilograma (R$ 11 e R$ 9), mas a questão não informa a massa dos peixes vendidos. Sem as massas, não dá para saber quantas carpas de cada tipo foram vendidas. A conta só fecha se os preços forem lidos como preço por peixe, o que contradiz o texto."},
     "explicacao": "<p>Questão anulada. Veja como ela teria sido resolvida se os preços fossem <strong>por peixe</strong>, e não por quilograma.</p><p>Foram vendidas 90% de 1 200 = 1 080 carpas. Chamando de h as húngaras, as carpas capim são 1 080 − h. Então \\(11(1080 - h) + 9h = 11\\,380\\), ou seja, \\(11\\,880 - 2h = 11\\,380\\), e \\(h = 250\\). Seria a alternativa A.</p><p>Como o texto dá o preço por quilograma e não informa as massas, essa conta não vale para o enunciado como ele foi escrito, e por isso nenhuma alternativa pode ser considerada correta.</p>"},
24: {"materia": "História", "assunto": "Povos indígenas", "tags": ["milho"],
     "enunciado": MILHO + P24,
     "explicacao": "<p>O texto conta que, há cerca de nove mil anos, povos que viviam onde hoje é o México começaram a cultivar o milho, e que ele é até hoje um dos principais plantios do país: a relação é <strong>histórica</strong>. Alternativa <strong>B</strong>.</p><p>Os indígenas lutam <strong>contra</strong> o milho transgênico (A). Quem tem o maior consumo <em>per capita</em> é o México, não o Brasil (C). O texto diz que o milho depende do ser humano para espalhar suas sementes, não do vento (D). E o deus Cintéotl, dos mitos mexicanos, não é cristão (E).</p>"},
25: {"materia": "Português", "assunto": "Interpretação de texto",
     "enunciado": p("Ainda de acordo com o texto, é correto afirmar que"), "apoio_de": (24, P24),
     "explicacao": "<p>O texto diz: “A glicose que vem do amido também é usada como meio de cultura de bactérias que produzem a penicilina e para revestir comprimidos”. Alternativa <strong>C</strong>.</p><p>O maior número de variedades está no México (A). O milho branco é “muito comum” lá (B). O amido, e não a palha, aparece na pasta de dentes; pneus nem são citados (D). E a penicilina é produzida por bactérias cultivadas com glicose, sem relação com os maias (E).</p>"},
26: {"materia": "Química", "assunto": "Reações químicas", "tags": ["termoquímica"],
     "enunciado": CALOR + P26,
     "explicacao": "<p>A temperatura do sistema subiu de 22 °C para 28 °C: ele recebeu calor. Esse calor veio da reação, que liberou energia. Reação que <strong>libera calor</strong> é <strong>exotérmica</strong>. Alternativa <strong>A</strong>.</p><p>Uma reação endotérmica absorveria calor e a temperatura cairia (C e D). B diz que a reação absorveu calor, o que contradiz “exotérmica”. E houve troca de energia, já que a temperatura mudou (E).</p>"},
27: {"materia": "Física", "assunto": "Termologia", "tags": ["calorimetria"],
     "enunciado": p("É possível calcular a quantidade de calor trocada em um sistema por meio da relação matemática: <strong>Q = m · c · ΔT</strong>. Essa relação é conhecida como a Equação Fundamental da Calorimetria e mostra que o calor trocado (<strong>Q</strong>) depende da massa (<strong>m</strong>), do calor específico (<strong>c</strong>) e da variação de temperatura do corpo (Δ<strong>T</strong>).",
                    "Sabendo que a massa da solução referida no texto é 100 g e considerando o calor específico como 1 cal/g · °C, a quantidade de calor trocada nesse processo é"),
     "apoio_de": (26, P26),
     "alternativas": {"A": "60 calorias.", "B": "600 calorias.", "C": "2 200 calorias.", "D": "2 800 calorias.", "E": "5 000 calorias."},
     "explicacao": "<p>A variação de temperatura é ΔT = 28 − 22 = 6 °C. Então Q = 100 × 1 × 6 = <strong>600 calorias</strong>. Alternativa <strong>B</strong>.</p><p>60 cal esquece um fator 10 (A). 2 200 e 2 800 cal usam as temperaturas inicial e final no lugar da variação (C e D). E 5 000 cal usa a soma 22 + 28 = 50 (E).</p>"},
28: {"materia": "Biologia", "assunto": "Nutrição e saúde",
     "explicacao": "<p>Aminoácidos vêm da digestão das <strong>proteínas</strong>. Entre as opções, o alimento rico em proteína é a carne: o <strong>contrafilé</strong>. Alternativa <strong>E</strong>.</p><p>Batata, mandioca, arroz, macarrão e polenta são ricos em carboidratos (amido), que viram glicose na digestão (A, B, C e D). Salada de folhas fornece sobretudo fibras, vitaminas e sais minerais.</p>"},
29: {"materia": "História", "assunto": "História contemporânea", "tags": ["Revolução Francesa"],
     "explicacao": "<p>Antes de 1789, a sociedade francesa era dividida em três estados: o clero (Primeiro), a nobreza (Segundo), ambos privilegiados e somando cerca de 3% da população, e o <strong>Terceiro Estado</strong> (burguesia, trabalhadores urbanos e camponeses), que pagava sozinho os impostos. Alternativa <strong>D</strong>.</p><p>Robespierre e Napoleão foram figuras da revolução, não do período anterior (A). Clero e nobreza tinham grande peso político (B). Girondinos e sans-culottes surgiram durante a revolução (C). E clero e nobreza eram isentos de impostos, não seus pagadores (E).</p>"},
30: {"materia": "Português", "assunto": "Texto literário",
     "enunciado": DIALOGO + P30,
     "explicacao": "<p>Diante dos crânios de Helena e de outras “beldades”, Menipo se espanta que tantos tenham sofrido e morrido por algo tão passageiro. O diálogo <strong>reflete sobre o valor de buscar beleza e reconhecimento</strong>, que se perdem com a morte. Alternativa <strong>D</strong>.</p><p>Aquiles também virou ossos, então ninguém mantém beleza ou poder na morte (A). O texto não exalta a guerra (B). Hermes é um deus, não um líder guerreiro (C). E a morte não aumenta riqueza nenhuma (E).</p>"},
31: {"materia": "Português", "assunto": "Classes de palavras", "tags": ["sinônimos"],
     "enunciado": p("Observe a passagem:")
                  + apoio("“...os Aqueus não perceberam que estavam sofrendo por uma coisa tão <strong><u>efêmera</u></strong> e tão facilmente <strong><u>perecível</u></strong>.”")
                  + p("São sinônimas dos termos destacados, respectivamente, as palavras"),
     "apoio_de": (30, P30),
     "explicacao": "<p>“Efêmera” é o que dura pouco: <strong>passageira</strong>. “Perecível” é o que pode acabar ou se estragar: <strong>extinguível</strong>. Alternativa <strong>E</strong>.</p><p>“Permanente”, “perene”, “infinita” e “vitalícia” têm sentido oposto ao de “efêmera” ou de “perecível” (A, B, C e D).</p>"},
32: {"materia": "Português", "assunto": "Verbos", "tags": ["discurso indireto"],
     "enunciado": p("Analise a passagem:")
                  + apoio("“Onde estão os belos e as belas, Hermes? Leva-me até eles, pois eu sou novato aqui.”")
                  + p("Assinale a alternativa em que o excerto esteja corretamente transposto para o discurso indireto."),
     "apoio_de": (30, P30),
     "explicacao": "<p>No discurso indireto, quem fala é Menipo, e o narrador relata: o presente “estão” vira “estavam”, o imperativo “leva-me” vira “que o levasse”, “eu sou” vira “ele era” e “aqui” vira “naquele lugar”. Alternativa <strong>B</strong>.</p><p>A mantém “aqui”, que no discurso indireto vira “ali” ou “naquele lugar”. C e D trocam quem fala (Hermes, em vez de Menipo). E E distorce o sentido da fala.</p>"},
33: {"materia": "Matemática", "assunto": "Geometria espacial", "tags": ["poliedros"],
     "enunciado": p("Carlos Rogério, empresário do ramo de festas e eventos, decidiu oferecer a seus clientes embalagens diferenciadas para as populares lembrancinhas. Segundo o empresário, a introdução de uma embalagem em formato de poliedro convexo regular (apresentada na imagem, com sua planificação) aumentou seu faturamento no último mês.")
                  + "[[fig:1]]"
                  + apoio("<strong>Lembre-se de que:</strong>", "Um poliedro convexo é chamado de regular se suas faces são polígonos regulares, e cada um desses polígonos regulares tem o mesmo número de lados.")
                  + p("Sabendo que todas as faces da embalagem de Carlos Rogério são polígonos regulares, pode-se afirmar que um ângulo interno de uma dessas faces mede"),
     "imagens": [{"arquivo": "q33", "alt": "Um dodecaedro (poliedro de faces pentagonais) e, abaixo, sua planificação: doze pentágonos regulares em dois grupos de seis, cada grupo com um pentágono central cercado por cinco."}],
     "explicacao": "<p>As faces são pentágonos regulares. A soma dos ângulos internos de um polígono de n lados é (n − 2) × 180°. Para n = 5: 3 × 180° = 540°. Cada um dos 5 ângulos mede 540° ÷ 5 = <strong>108°</strong>. Alternativa <strong>A</strong>.</p><p>540° é a soma de todos os ângulos internos, não um só (E). 180° e 360° são as somas dos ângulos do triângulo e do quadrilátero (B e C).</p>"},
34: {"materia": "Biologia", "assunto": "Zoologia", "tags": ["artrópodes"],
     "enunciado": p("Em um jardim, um grupo de estudantes coletou alguns animais para realizar um trabalho de pesquisa, cujo objetivo era agrupar os seres vivos capturados de acordo, principalmente, com suas semelhanças anatômicas. Um dos aspectos a ser observado na pesquisa eram as quelíceras, que correspondem ao primeiro par de apêndices articulados localizados na região bucal dos animais e podem ter várias funções, como por exemplo: inocular veneno, rasgar ou triturar alimentos, carregar ovos e até cavar buracos.",
                    "Após a coleta, foi possível organizar dois grupos de animais cujas características são:")
                  + tabela(["Grupo", "Quantidade de Patas", "Divisão Corporal", "Antenas", "Quelíceras"],
                           [["Grupo 1", "04 pares de patas", "cefalotórax e abdome", "sem antenas", "com quelíceras"],
                            ["Grupo 2", "03 pares de patas", "cabeça, tórax e abdome", "01 par de antenas", "sem quelíceras"]])
                  + p("Considerando as características descritas dos animais coletados, é correto afirmar que os animais do <strong>Grupo 1</strong> e do <strong>Grupo 2</strong> são, respectivamente,"),
     "alternativas": colunas(["Grupo 1", "Grupo 2"], [["Insetos", "Aracnídeos"], ["Crustáceos", "Insetos"], ["Aracnídeos", "Insetos"], ["Insetos", "Crustáceos"], ["Aracnídeos", "Crustáceos"]]),
     "explicacao": "<p>Quatro pares de patas, corpo em cefalotórax e abdome, sem antenas e com quelíceras: <strong>aracnídeos</strong> (aranhas, escorpiões). Três pares de patas, corpo em cabeça, tórax e abdome e um par de antenas: <strong>insetos</strong>. Alternativa <strong>C</strong>.</p><p>Crustáceos têm dois pares de antenas e, em geral, mais de quatro pares de patas, e não aparecem nos grupos (B, D e E). A inverte aracnídeos e insetos.</p>"},
35: {"materia": "História", "assunto": "Imperialismo e neocolonialismo",
     "explicacao": "<p>A Conferência de Berlim (1884-1885) serviu para as potências europeias <strong>resolverem suas disputas e dividirem a África</strong>, rica em recursos naturais e matérias-primas para a indústria. Alternativa <strong>B</strong>.</p><p>Portugal não teve garantido o território entre Angola e Moçambique (o “mapa cor-de-rosa” foi barrado pela Inglaterra) (A). Lutero é do século XVI (C) e o Partido Nazista, do século XX (D). E países sul-americanos não eram o alvo da conferência (E).</p>"},
36: {"materia": "Física", "assunto": "Cinemática", "tags": ["velocidade média"],
     "enunciado": APOLLO + P36,
     "explicacao": "<p>Com velocidade constante, tempo = distância ÷ velocidade = 92 km ÷ 13 km/h ≈ 7,1 h, ou seja, aproximadamente <strong>7 h</strong>. Alternativa <strong>D</strong>.</p><p>Os outros valores não correspondem à divisão da autonomia pela velocidade máxima.</p>"},
37: {"materia": "Física", "assunto": "Dinâmica", "tags": ["força peso", "gravidade"],
     "enunciado": p("A força gravitacional, quando nos referimos a objetos próximos à superfície de corpos celestes, recebe o nome de força peso. A força peso é calculada pelo produto da massa do objeto, cujo peso se deseja conhecer, pelo valor da aceleração da gravidade do local em que esse objeto se encontra.",
                    "Considerando que o valor da aceleração da gravidade no planeta Terra seja 10 m/s<sup>2</sup>, o valor da aceleração da gravidade na Lua corresponde à"),
     "apoio_de": (36, P36),
     "explicacao": "<p>A massa do veículo é a mesma na Terra e na Lua. Como P = m · g, a razão entre os pesos é a razão entre as gravidades: 2 100 N ÷ 350 N = 6. A gravidade da Lua é a <strong>sexta parte</strong> da gravidade da Terra (cerca de 1,7 m/s²). Alternativa <strong>E</strong>.</p><p>As outras frações (metade, terça, quarta e quinta parte) não correspondem à razão entre os pesos.</p>"},
38: {"materia": "Geografia", "assunto": "Geografia da Ásia", "tags": ["monções"],
     "enunciado": apoio("A estação chuvosa na Índia e em todo o sul da Ásia é chamada de monções e é sempre muito esperada. É um período de chuva frequente e volumosa que se estende por cerca de quatro meses. Antes de a chuva começar, o calor é intenso no continente, com temperaturas que superam os 40 ºC. A chuva de monção (ou chuva de monções) ocorre no verão do hemisfério Norte. Só que diferente de diversas áreas do globo, os volumes acumulados de chuva sobre algumas áreas em quatro meses, como nas proximidades do Himalaia, podem chegar aos 3 000 mm.")
                  + fonte("&lt;https://tinyurl.com/yxcdgj63&gt; Acesso em: 01.10.2019. Adaptado.")
                  + p("As chuvas mencionadas no texto são esperadas, pois ajudam no plantio de"),
     "explicacao": "<p>O arroz, base da alimentação no sul e no sudeste da Ásia, precisa de muita água e é plantado em áreas alagadas, muitas vezes em encostas cortadas em degraus: o <strong>terraceamento</strong>. As chuvas de monção irrigam essas plantações. Alternativa <strong>A</strong>.</p><p>Azeitona e uva são típicas de clima mediterrâneo (B e D). Pecuária não é sistema de plantio (C e D). E a mandioca não é a cultura ligada às monções (E).</p>"},
39: {"materia": "História", "assunto": "Antiguidade",
     "enunciado": apoio("Na Antiguidade, o desenvolvimento de povoações, aldeias e cidades que se utilizaram dos rios para a sua constituição gerou sociedades mais complexas em diversas regiões do mundo, como o Oriente Médio, a Ásia e a África. Nessas sociedades, a vida coletiva era marcada pelo trabalho que modificava a natureza e estabelecia divisões de tarefas entre os seres humanos. Nelas, o trabalho coletivo de irrigação era necessário para controlar as cheias dos rios e para cultivar as terras de suas margens.")
                  + fonte("CAMPOS, Flavio de; CLARO, Regina; DOLHNIKOFF, Miriam. <em>Jogo da História nos dias de Hoje</em>. 6. 2ªed. São Paulo: Leya, 2015. p.58. Adaptado.")
                  + p("O texto se refere às chamadas sociedades"),
     "explicacao": "<p>Sociedades que se formaram às margens de rios e dependiam do controle das cheias e da irrigação, como as do Egito (Nilo), da Mesopotâmia (Tigre e Eufrates), da Índia e da China, são chamadas <strong>sociedades fluviais</strong> (ou hidráulicas). Alternativa <strong>B</strong>.</p><p>O feudalismo é medieval (A). Povos nômades não se fixam junto aos rios (C). “Patriarcal” descreve a organização familiar, não a relação com os rios (D). E essas sociedades já conheciam a escrita, então não eram pré-históricas (E).</p>"},
40: {"materia": "Química", "assunto": "Interpretação de dados", "tags": ["concentração"],
     "enunciado": SORO + P40,
     "alternativas": {"A": "0,45 g.", "B": "4,50 g.", "C": "45,00 g.", "D": "9,00 g.", "E": "0,90 g."},
     "explicacao": "<p>Concentração de 0,9% (m/V) significa 0,9 g de sal a cada 100 mL. Em 500 mL (5 vezes mais): 5 × 0,9 = <strong>4,5 g</strong>. Alternativa <strong>B</strong>.</p><p>0,90 g é a massa em 100 mL (E). 9,00 g seria a massa em 1 L (D). 0,45 g e 45,00 g erram a vírgula (A e C).</p>"},
41: {"materia": "Química", "assunto": "Funções inorgânicas", "tags": ["nomenclatura de sais"],
     "enunciado": p("A nomenclatura dos sais é derivada da nomenclatura do respectivo ácido de origem.",
                    "Por exemplo, o sal usado no soro fisiológico, <strong>cloreto</strong> de sódio, é derivado do ácido <strong>clorídrico</strong>, e pode ser obtido por meio da reação de neutralização:")
                  + apoio("HCℓ + NaOH → NaCℓ + H<sub>2</sub>O")
                  + tabela(["Fórmula", "Nome"], [["HCℓ", "ácido clorí<strong><u>drico</u></strong>"], ["NaOH", "hidróxido de sódio"], ["NaCℓ", "clor<strong><u>eto</u></strong> de sódio"]])
                  + p("Desse modo, o sal derivado do ácido sulfídrico, na reação de neutralização total com hidróxido de cálcio, será"),
     "apoio_de": (40, P40),
     "alternativas": {"A": "CaS: sulfeto de cálcio.", "B": "CaS: sulfato de cálcio.", "C": "CaS: sulfito de cálcio.", "D": "NaS: sulfato de sódio.", "E": "NaS: sulfeto de sódio."},
     "explicacao": "<p>Ácido terminado em <strong>-ídrico</strong> forma sal terminado em <strong>-eto</strong>: ácido sulfídrico (H<sub>2</sub>S) dá <strong>sulfeto</strong>. Com hidróxido de cálcio, Ca(OH)<sub>2</sub>, o cátion é Ca<sup>2+</sup> e o ânion é S<sup>2–</sup>, então o sal é <strong>CaS, sulfeto de cálcio</strong>. Alternativa <strong>A</strong>.</p><p>Sulfato vem do ácido sulfúrico e sulfito, do ácido sulfuroso (B, C e D). E não há sódio na reação, só cálcio (D e E).</p>"},
42: {"materia": "Física", "assunto": "Magnetismo",
     "enunciado": p("Leia as afirmações e a imagem.")
                  + apoio("Todo ímã possui dois polos magnéticos, conhecidos como norte e sul.",
                         "Nos ímãs, as linhas de campo magnético saem do polo norte, circundam externamente o ímã e entram no polo sul.",
                         "Quando dois ímãs são aproximados, os polos de nomes diferentes se atraem enquanto que os polos de nomes iguais se repelem.",
                         "A agulha de uma bússola é um ímã. A ponta dessa agulha corresponde ao polo norte desse ímã.",
                         "O interior do planeta Terra pode ser comparado a um grande ímã, mantendo um forte campo magnético em torno do planeta.",
                         "O Polo Norte Geográfico se encontra no hemisfério do planeta que abriga o Polo Sul Magnético. Do mesmo modo, o Polo Sul Geográfico se encontra no hemisfério do planeta que abriga o Polo Norte Magnético.")
                  + "[[fig:1]]" + fonte("&lt;https://tinyurl.com/y6b3ourg&gt; Acesso em: 26.10.2019. Original colorido.")
                  + p("Considerando cada afirmações e tendo como referência a posição do planeta na imagem apresentada, o ímã que poderia substituir o interior da Terra é"),
     "imagens": [{"arquivo": "q42", "alt": "A Terra vista do espaço, com o polo Norte geográfico para cima, cercada por linhas de campo magnético curvas, com setas, que saem de um hemisfério, contornam o planeta e entram no outro."},
                 {"arquivo": "q42a", "alt": "Ímã em barra na vertical: polo N em cima e polo S embaixo."},
                 {"arquivo": "q42b", "alt": "Ímã em barra na vertical: polo S em cima e polo N embaixo."},
                 {"arquivo": "q42c", "alt": "Ímã em barra na horizontal: polo S à esquerda e polo N à direita."},
                 {"arquivo": "q42d", "alt": "Ímã em forma de U com as pontas para cima: polo N na ponta esquerda e polo S na ponta direita."},
                 {"arquivo": "q42e", "alt": "Ímã em forma de U deitado, com as pontas para a direita: polo N na ponta de cima e polo S na ponta de baixo."}],
     "alternativas": {"A": "[[fig:2]]", "B": "[[fig:3]]", "C": "[[fig:4]]", "D": "[[fig:5]]", "E": "[[fig:6]]"},
     "explicacao": "<p>Na imagem, o Polo Norte geográfico está em cima. Pela última afirmação, o hemisfério norte abriga o <strong>polo sul magnético</strong>; o polo norte magnético fica embaixo, no hemisfério sul. É por isso que a ponta norte da bússola aponta para o norte geográfico: polos diferentes se atraem. O ímã deve ficar em pé, com <strong>S em cima e N embaixo</strong>. Alternativa <strong>B</strong>.</p><p>A inverte os polos. C, D e E deitam ou dobram o ímã, sem um polo em cada hemisfério, alinhado ao eixo norte-sul.</p>"},
43: {"materia": "Matemática", "assunto": "Geometria plana", "tags": ["teorema de Pitágoras"],
     "enunciado": BOTAS
                  + p("Admita que a menina dos quadrinhos esteja visitando a avó que mora em outra cidade.",
                      "A fim de voltar da casa de sua avó para o prédio onde mora, usando a bota de 7 léguas da história, a menina dá 3 passos para leste e 4 passos para o norte.",
                      "A figura representa de modo esquemático esse trajeto realizado pela garota.")
                  + "[[fig:2]]" + fonte("Figura fora de escala.")
                  + p("A distância entre a casa da avó e o prédio no qual a menina mora é, em quilômetros, igual a"),
     "imagens": [BOTAS_IMG,
                 {"arquivo": "q43b", "alt": "Esquema do trajeto, com rosa dos ventos: da casa da avó, à esquerda, uma linha tracejada segue para leste e depois vira para o norte até o prédio, contornando um rio. A casa da avó e o prédio ficam nos extremos desse caminho em L."}],
     "alternativas": {"A": "323,4.", "B": "231,0.", "C": "142,6.", "D": "46,2.", "E": "35,0."},
     "explicacao": "<p>Cada passo vale 7 léguas, e cada légua, 6,6 km: um passo = 7 × 6,6 = 46,2 km. Os trechos de 3 passos (leste) e 4 passos (norte) formam os catetos de um triângulo retângulo; a distância em linha reta é a hipotenusa: \\(\\sqrt{3^2 + 4^2} = 5\\) passos. Então 5 × 46,2 = <strong>231 km</strong>. Alternativa <strong>B</strong>.</p><p>323,4 km é o caminho percorrido (3 + 4 = 7 passos), não a distância entre os pontos (A). 46,2 km é um só passo (D). E 35 km é 5 passos de 7 km, esquecendo a conversão de léguas (E).</p>"},
44: {"materia": "Matemática", "assunto": "Porcentagem",
     "enunciado": BOTAS
                  + p("A légua é uma medida de comprimento que varia de acordo com o período histórico e o país em que é usada. Segundo o dicionário Priberam, por exemplo, ela equivale a 5 km em Portugal.",
                      "Pode-se, portanto, estimar que a légua brasileira é maior que a portuguesa em cerca de"),
     "imagens": [BOTAS_IMG],
     "explicacao": "<p>A légua brasileira mede 6,6 km e a portuguesa, 5 km. A diferença é 1,6 km, e 1,6 ÷ 5 = 0,32, ou seja, a brasileira é <strong>32%</strong> maior. Alternativa <strong>C</strong>.</p><p>24% compara a diferença com a légua brasileira (1,6 ÷ 6,6), e não com a portuguesa (D). Os demais valores não saem dessas medidas.</p>"},
45: {"materia": "História", "assunto": "Grandes Navegações",
     "explicacao": "<p>As Grandes Navegações dependeram de avanços técnicos, como a <strong>caravela</strong>, embarcação leve e manobrável que, com velas triangulares, navegava até contra o vento. Alternativa <strong>C</strong>.</p><p>O mar Egeu fica na Grécia, longe do contexto português (A). A ideia da Terra esférica já era aceita pelos estudiosos e a ciência ajudou os navegadores (B). Cientistas participaram do projeto, como os da chamada Escola de Sagres (D). E os instrumentos vinham da tradição europeia, árabe e chinesa, não dos povos americanos, que os europeus ainda não conheciam (E).</p>"},
46: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": ["vacinas"],
     "explicacao": "<p>Sarampo, caxumba, rubéola e poliomielite são causadas por <strong>vírus</strong>. As vacinas usam esses vírus enfraquecidos ou inativados (mortos) para estimular o corpo a produzir anticorpos e células de memória: é a <strong>imunização ativa</strong>. Alternativa <strong>B</strong>.</p><p>Essas vacinas são gratuitas no SUS (A). Os agentes não são bactérias (C). Soros, e não vacinas, é que são produzidos em cavalos (D). E o texto diz justamente que os agentes continuam circulando (E).</p>"},
47: {"materia": "Geografia", "assunto": "Regionalização do Brasil", "tags": ["irrigação"],
     "enunciado": apoio("“No Brasil, o Vale do rio São Francisco é o único lugar que produz uva até três vezes ao ano.",
                        "As parreiras são divididas em grandes áreas. Enquanto em uma parte elas estão prontas para a colheita, na outra a fase é de poda e, logo ao lado, as uvas ainda estão começando a aparecer. Esse não é o milagre da multiplicação. É o milagre da irrigação. Controlando a água, é possível controlar todo o ciclo de vida da parreira.”")
                  + fonte("&lt;https://tinyurl.com/3893ebn&gt; Acesso em: 01.10.2019. Adaptado.")
                  + p("A localização geográfica do cenário descrito no texto situa-se na região"),
     "explicacao": "<p>O Vale do São Francisco irrigado, com polos como Petrolina (PE) e Juazeiro (BA), fica no <strong>Nordeste</strong>, em área de clima <strong>semiárido</strong>: quente, com pouca chuva. Por isso a irrigação é decisiva. Alternativa <strong>C</strong>.</p><p>O trecho citado do rio não fica no Sul nem no Centro-Oeste (A, B e E), e o clima subtropical é típico do Sul (B e D).</p>"},
48: {"materia": "Física", "assunto": "Óptica", "tags": ["eclipses"],
     "enunciado": apoio("SOHO, abreviação de Solar &amp; Heliospheric Observatory, é uma sonda que orbita o Sol e coleta informações de nossa estrela utilizando vários instrumentos. Um deles registra o comportamento da coroa solar e, para isso, conta com um pequeno disco opaco que fica estrategicamente posicionado à frente da câmera, ocultando a visão do disco solar.")
                  + p("Esse instrumento simula o que acontece quando, devidamente protegidos, estamos observando, daqui da Terra, o Sol no momento em que ocorre um eclipse"),
     "explicacao": "<p>O disco opaco cobre todo o disco do Sol e deixa ver só a coroa. É o que acontece num <strong>eclipse solar total</strong>: a <strong>Lua se põe entre a Terra e o Sol</strong> e o cobre por completo. Alternativa <strong>C</strong>.</p><p>No eclipse lunar, quem fica no meio é a Terra, e o que escurece é a Lua (A, B e D). No eclipse parcial, parte do Sol continua visível, e a coroa não aparece (E).</p>"},
49: {"materia": "Biologia", "assunto": "Citologia", "tags": ["divisão celular"],
     "explicacao": "<p>Novas células do corpo surgem por <strong>mitose</strong>. Se a quimioterapia bloqueia a produção de novas células, ela inibe as mitoses. Isso freia o tumor, mas também afeta tecidos que se renovam muito (cabelo, mucosas). Alternativa <strong>E</strong>.</p><p>Digestão celular (A), respiração celular (B) e eliminação de toxinas (C) não são os mecanismos de produção de células. E ela não acelera a renovação dos tecidos sadios; prejudica-a (D).</p>"},
50: {"materia": "História", "assunto": "Antiguidade", "tags": ["cidadania"],
     "enunciado": apoio("A palavra <em>idiota</em> tem sua origem no grego antigo <em>idiótes</em>, que significava “homem privado da vida pública, que não vive a política, que não participa das coisas públicas”. Enquanto o homem livre era aquele que participava ativamente da <em>polis</em>, da vida em sociedade, do público, porque vivia a política, o escravizado estava na vida privada, vivia limitado ao mundo privado, era um idiota porque não tinha acesso à vida política.",
                        "Nesse sentido, para os gregos, cidadania (o pertencimento à cidade) dizia respeito àquele que vivia a política. Portanto, o cidadão construía os direitos e os deveres, enquanto o idiota estava à margem desse processo.")
                  + fonte("&lt;https://tinyurl.com/yy8pgxg3&gt; Acesso em: 05.10.2019. Adaptado.")
                  + p("Segundo o texto,"),
     "explicacao": "<p>O texto diz que o homem livre era o que “participava ativamente da <em>polis</em>” e que a cidadania pertencia a quem “vivia a política”. <strong>Liberdade e cidadania estavam ligadas à participação</strong> nos assuntos da cidade. Alternativa <strong>D</strong>.</p><p>Quem recusava a política era o idiota, não o cidadão (A e E). O texto não fala de uma lei que obrigasse a participar (B) nem associa a política à corrupção (C).</p>"},
}
completar(Q, R)
