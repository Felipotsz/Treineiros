# Ajustes da conferência humana: Vestibulinho ETEC 1º semestre de 2019 (exame de 16/12/2018)
# Texto conferido com a imagem de cada página; trechos longos copiados do texto do PDF com trecho().
# Gabarito: oficial (1º SEM/19). Letras de canção e poemas recortados como imagem (alt descreve, não transcreve).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import A, carregar, enun, tabela, colunas, completar, trecho

ID = "etec-2019-1sem"
META = {
    "id": ID,
    "banca": "ETEC",
    "ano": 2019,
    "semestre": 1,
    "titulo": "Vestibulinho ETEC, 1º semestre de 2019",
    "fonte": "Centro Paula Souza",
    "dataExame": "2018-12-16",
    "duracaoMinutos": 240,
    "apresentacao": "<p>Prezado(a) candidato(a), esta prova engloba conceitos do passado, conceitos contemporâneos e temas gerais, explorando as diferentes áreas do conhecimento, competências e habilidades. Abordando saberes que permeiam o nosso mundo.</p><p>Boa prova!</p>",
    "pdf": f"assets/provas/{ID}.pdf",
}
EXTRAS = {"apresentacao": "Ilustração de um livro aberto do qual sobem círculos com ícones de várias áreas do conhecimento: capelo de formatura, frasco de laboratório, microscópio, globo, átomo, DNA, computador, música e esporte."}

R = carregar(ID)


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


# ---------- textos compartilhados ----------
NOIVA = (chamada("Leia o texto para responder às questões de números 03 e 04.")
         + apoio("Como filha de um homem abastado, a noiva fora instruída nos rudimentos da leitura e da escrita [...]. Só que a noiva era uma criatura histriônica*. Tudo que lia, poesia ou canção, era compartilhado com a Escrava; tudo que escrevia, em seguida lia em voz alta para a Escrava. Em segredo, a africana desconfiava daqueles sinais mágicos, tinha medo do papel que podia transportar vozes humanas. Porém, contanto que fosse a sua favorita quem dava voz às palavras, ela se sentia em segurança; contanto que fosse ela quem transformava em música os sinais no papel, a Escrava ficava contente. Agora, pela primeira vez, foi excluída. A mensagem do anjo tinha erguido uma barreira de escrita entre ambas.")
         + fonte("*histriônica: relativo a histrião, aquele que representava as farsas, logo, comediante, farsista.")
         + fonte("(Bahiyyih Nakhjavani, <em>O alforje</em>. Porto Alegre: Dublinense, 2018, p. 180.)"))
P3 = p("Na cena transcrita, a personagem Escrava vê, na linguagem escrita,")

MENDELEEV = (chamada("Leia o texto para responder às questões de números 06 a 08.")
             + "[[fig:1]]"
             + apoio(*T(4, "A Organização das Nações Unidas (ONU)", "o número atômico.",
                        ["Um dos principais motivos", "O mais impressionante", "Atualmente, a Tabela"]))
             + "[[fig:2]]"
             + apoio(*T(4, "Apesar de terem sofrido", "a esse grande cientista.", ["No ano de 1955"]))
             + url("https://tinyurl.com/y9pwfcuw", "21.10.2018", "Adaptado. Original colorido."))
MENDELEEV_IMG = [{"arquivo": "q06", "alt": "Foto antiga, em preto e branco, de Dmitry Mendeleev: homem de barba e cabelos longos, de pé, trabalhando em uma bancada de laboratório."},
                 {"arquivo": "q06b", "alt": "Peça em relevo, como um quadradinho da tabela periódica, com o símbolo Md, o número atômico 101, o nome Mendelévio e a massa (258)."}]
P6 = p("De acordo com o texto, assinale a alternativa correta.")

BAUDELAIRE = (chamada("Leia o texto e a charge de Alberto Montt para responder às questões de números 15 a 17.")
              + apoio(it("Charles Baudelaire, poeta do século XIX, é autor do livro As Flores do Mal. Nele, seus poemas abordam temas que questionam as convenções morais da sociedade francesa, sendo, por isso, tachado como obsceno, como um insulto aos bons costumes da época. A partir dele, originaram-se na França os chamados “poetas malditos”.", "As Flores do Mal"))
              + "[[fig:1]]" + url("https://tinyurl.com/ycuzcs6h", "27.10.2018", "Original colorido."))
BAUDELAIRE_IMG = {"arquivo": "q15", "alt": "Charge “Baudelaire e suas flores do mal”, de Alberto Montt. O poeta Charles Baudelaire, de casaco e cachecol, olha de lado, desconfiado, para um vaso com três flores sorridentes. Uma flor diz: “Quando te escreverem uma mensagem, visualize, mas não responda.” Outra: “Assista às maratonas de séries nos dias úteis.” A terceira: “Coma bacon.”"}
P15 = p("O título da charge retoma o título da obra de Baudelaire, <em>As Flores do Mal</em>. O autor, para construir o humor em seu texto, utiliza-se de")

FLUVIAL = (chamada("Leia o trecho da letra da música <em>Civilização Fluvial</em>, composta por Fauzi Beydoun e gravada pela banda Tribo de Jah, para responder às questões de números 25 e 26.")
           + "[[fig:1]]" + url("https://tinyurl.com/y8br779m", "08.10.2018"))
FLUVIAL_IMG = {"arquivo": "q25", "alt": "Trecho da letra da canção “Civilização Fluvial”, em quatro estrofes. A letra fala de um novo universo que floresce ao longo dos rios além de Belém, de um império verde que domina o horizonte da costa do Amapá até a cordilheira, e de uma nova cultura e civilização dentro da mesma nação. Na segunda estrofe, a palavra “istmos” está em negrito. Na quarta estrofe, que repete a palavra “Fluvial”, estão em negrito as palavras “Ocidental” e “Setentrional”."}
P25 = p("O singular da palavra escrita em negrito, na segunda estrofe, significa")

QUEBRA = (chamada("Considere a imagem, que apresenta algumas peças de um quebra-cabeça de cátions e ânions, para responder às questões de números 29 a 31.")
          + "[[fig:1]]")
QUEBRA_IMG = {"arquivo": "q29", "alt": "Peças de quebra-cabeça numeradas. Cátions (fila de cima): 1, duas peças K⁺ (potássio); 2, duas peças H⁺ (hidrogênio); 3, duas peças Na⁺ (sódio); 4, uma peça dupla Ba²⁺ (bário); 5, uma peça dupla Ca²⁺ (cálcio). Ânions (fila de baixo): 1, uma peça dupla SO₄²⁻ (sulfato); 2, uma peça dupla CO₃²⁻ (carbonato); 3, duas peças Br⁻ (brometo); 4, duas peças Cl⁻ (cloreto); 5, duas peças NO₃⁻ (nitrato). As peças de carga 2 ocupam o espaço de duas peças de carga 1."}
P29 = p("Sabendo que os compostos devem apresentar a neutralidade de cargas, um aluno do 9º ano do Ensino Fundamental está usando as peças do quebra-cabeça para descobrir as fórmulas de algumas substâncias químicas.",
        "Quando ele unir as peças que apresentam os íons K<sup>+</sup> e NO<sub>3</sub><sup>–</sup>, estará representando um composto")

CHARGE = (chamada("Analise a charge para responder às questões de números 37 a 39.")
          + "[[fig:1]]" + url("https://tinyurl.com/yaougao9", "12.10.2018", "Original colorido."))
CHARGE_IMG = {"arquivo": "q37", "alt": "Charge com o título “democracinhas”. Um homem sentado no chão, maltrapilho, com as mãos juntas, pede: “Candidato, me ajuda a comer, candidato!”. Um homem de óculos, bem vestido, curvado na direção dele, responde: “Mas é claro que te ajudo! Tem aí um sanduíche para a gente dividir?”"}
P37 = p("O verbo “ajudar”, utilizado nas falas das personagens, está conjugado em modo e tempo verbais diferentes.",
        "Identifique a alternativa em que o modo e o tempo desse verbo estão analisados correta e respectivamente.")

NOBEL = (chamada("Leia o texto para responder às questões de números 47 a 49.")
         + apoio(*T(22, "O Prêmio Nobel foi criado", "de diâmetro e um diploma."))
         + "[[fig:1]]" + url("https://tinyurl.com/yc3mqe68", "07.10.2018", "Original colorido."))
NOBEL_IMG = {"arquivo": "q47", "alt": "Medalha circular do Prêmio Nobel, com o perfil de Alfred Nobel em relevo e as inscrições “ALFR. NOBEL” e as datas de nascimento e morte em algarismos romanos."}
P47 = p("Considerando y o valor do prêmio em 2017 e x o valor do prêmio em 2016, assinale a alternativa que apresenta a relação correta entre os dois valores.")

# ---------- questões ----------
Q = {
1: {"materia": "Biologia", "assunto": "Zoologia", "tags": ["artrópodes"],
    "enunciado": p(*T(2, "Os primeiros animais surgiram", "insetos que apareceram."), "Considerando os animais citados no texto, podemos afirmar que"),
    "explicacao": "<p>As libélulas são insetos: como todo artrópode, têm <strong>exoesqueleto</strong> e, como todo inseto, <strong>três pares de patas</strong> e corpo dividido em <strong>cabeça, tórax e abdome</strong>. Alternativa <strong>D</strong>.</p><p>Nem todos têm asas, e artrópodes não têm corpo mole (A). As lacraias têm exoesqueleto de quitina, não endoesqueleto (B). Aranhas não têm antenas, e gafanhotos e grilos têm três pares de patas (C). E baratas não têm glândulas de veneno, e o corpo dos artrópodes é segmentado (E).</p>"},
2: {"materia": "História", "assunto": "Antiguidade", "tags": ["escrita"],
    "enunciado": apoio(*T(2, "Em 1929, o arqueólogo", "os primeiros contratos.", ["As tábuas estavam", "As tábuas não haviam"]))
                 + url("https://tinyurl.com/ycuj8mq6", "26.10.2018")
                 + p("O texto faz referência a um período muito conhecido da história da Humanidade, no qual surgiram os primeiros registros escritos.",
                     "Assinale a alternativa que, corretamente, descreve o contexto em que surgiu a escrita na Mesopotâmia."),
    "explicacao": "<p>O texto diz que as tábuas de Uruk “foram empregadas para fazer contas – e também para elaborar os primeiros contratos”. A escrita cuneiforme surgiu ligada ao <strong>comércio e à administração</strong>. Alternativa <strong>E</strong>.</p><p>O texto afirma que as tábuas não serviam para poesia nem para mensagens a lugares distantes (C e D). Não há referência a comunicação com deuses (A) nem a educação universal, já que poucos sabiam escrever (B).</p>"},
3: {"materia": "Português", "assunto": "Texto literário",
    "enunciado": NOIVA + P3,
    "explicacao": "<p>A Escrava desconfiava daqueles “sinais mágicos” e temia o “papel que podia transportar vozes humanas”. Ao final, a escrita ergue “uma barreira” entre ela e a noiva. Ela vê na escrita um <strong>poder quase mágico</strong> que dá voz a quem não está presente e, ao mesmo tempo, <strong>constrói barreiras</strong>. Alternativa <strong>C</strong>.</p><p>A escrita acaba separando as duas, não unindo (A e E). O texto não fala de instruções divinas para teatro (B) nem de ideais religiosos ligados aos histriões (D).</p>"},
4: {"materia": "Português", "assunto": "Texto literário", "tags": ["foco narrativo"],
    "enunciado": p("Sobre o foco narrativo do trecho transcrito, é certo afirmar que se trata de um narrador"), "apoio_de": (3, P3),
    "explicacao": "<p>O narrador não participa da cena e conta o que se passa no íntimo da Escrava (“Em segredo, a africana desconfiava...”, “tinha medo”, “se sentia em segurança”). Ele conhece pensamentos e sentimentos da personagem: é <strong>onisciente</strong>, em terceira pessoa. Alternativa <strong>D</strong>.</p><p>O narrador não é personagem (A, B e E), e o observador não teria acesso aos sentimentos íntimos da Escrava (C).</p>"},
5: {"materia": "Matemática", "assunto": "Funções", "tags": ["função do 2º grau"],
    "enunciado": "[[fig:1]]" + url("https://tinyurl.com/ydbqzc47", "07.10.2018", "Original colorido.")
                 + p("O cartum brinca com a palavra <strong><em>parábola</em></strong>, que tem diferentes significados de acordo com o contexto em que é empregada.",
                     "Em Matemática, no estudo de funções, a parábola é uma curva que representa uma função polinomial"),
    "imagens": [{"arquivo": "q05", "alt": "Cartum: Jesus, de túnica, fala a dois discípulos sentados, e um balão sobre ele mostra o desenho de gráficos de parábolas, curvas em forma de U, uma voltada para baixo e outra para cima. Um discípulo pergunta: “Pedro, o que é isso?”, e o outro responde: “Ele fala por parábolas.”"}],
    "alternativas": {"E": "de 2º grau e sua expressão geral é dada por f(x) = ax<sup>2</sup> + bx + c, com a ≠ 0."},
    "explicacao": "<p>O gráfico de uma <strong>função polinomial de 2º grau</strong>, f(x) = ax² + bx + c, com a ≠ 0, é uma parábola. Alternativa <strong>E</strong>.</p><p>A função constante (A) tem como gráfico uma reta horizontal, e a de 1º grau (B), uma reta inclinada. C e D misturam o grau com a expressão errada.</p>"},
6: {"materia": "Química", "assunto": "Estrutura atômica", "tags": ["tabela periódica"],
    "enunciado": MENDELEEV + P6, "imagens": MENDELEEV_IMG,
    "explicacao": "<p>O texto diz que, em ordem crescente de massa atômica, “várias propriedades químicas se repetem em intervalos regulares (periódicos). Por isso, a sua descoberta recebeu o nome de Tabela Periódica”. Alternativa <strong>D</strong>.</p><p>Mendeleev usava um baralho para jogar paciência, mas não o construía para isso (A). Ele escreveu os elementos em fichas brancas, não no baralho (B). A tabela dele seguia a massa atômica, e a atual segue o número atômico (C e E).</p>"},
7: {"materia": "Química", "assunto": "Estrutura atômica", "tags": ["tabela periódica"],
    "enunciado": p("Mendeleev deixou, em sua Tabela, espaços vazios,"), "apoio_de": (6, P6),
    "explicacao": "<p>O texto diz que ele deixou espaços vagos para elementos “que ainda não haviam sido descobertos, mas que ainda seriam”, e que isso realmente aconteceu com o germânio, o gálio e o escândio. Alternativa <strong>B</strong>.</p><p>O sonho mostrou a tabela, não novos elementos (A). Os elementos descobertos tinham as propriedades previstas (C). E os espaços eram para elementos ainda não descobertos (D e E).</p>"},
8: {"materia": "Química", "assunto": "Estrutura atômica",
    "enunciado": p("O elemento químico, cujo nome é em homenagem a esse grande cientista, apresenta"), "apoio_de": (6, P6),
    "explicacao": "<p>O mendelévio tem número atômico 101, e o número atômico é o <strong>número de prótons</strong> do núcleo. Alternativa <strong>D</strong>.</p><p>258 é o número de massa, e 101, o atômico (A e B). O texto diz que ele é instável e sofre fissão nuclear espontânea (C e E).</p>"},
9: {"materia": "História", "assunto": "Antiguidade", "tags": ["Império Romano"],
    "enunciado": p("“Todos os caminhos levam a Roma”.") + "[[fig:1]]" + url("https://tinyurl.com/y8anvuh4", "26.10.2018", "Original colorido.")
                 + p("A frase e o mapa fazem referência a uma característica marcante do Império Romano (30 a.C. a 476 d.C.).", "Assinale a alternativa que apresenta essa característica."),
    "imagens": [{"arquivo": "q09", "alt": "Trecho de um mapa romano antigo, alongado na horizontal, com muitas linhas de estradas que ligam cidades, desenhadas como pequenos edifícios, com nomes e distâncias em latim."}],
    "explicacao": "<p>Os romanos construíram uma enorme rede de <strong>estradas pavimentadas</strong> que ligava as províncias à capital e entre si, usada por mensageiros, exércitos e comerciantes. Daí a frase “Todos os caminhos levam a Roma”. Alternativa <strong>C</strong>.</p><p>As estradas iam muito além da cidade de Roma (A). O Império não chegou aos cinco continentes (B). As estradas foram construídas na expansão, não para fugir dos germânicos (D). E o cristianismo só se tornou religião oficial no fim do Império (E).</p>"},
10: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["União Europeia"],
     "explicacao": "<p>Os critérios de adesão à União Europeia (critérios de Copenhague) exigem <strong>instituições estáveis que garantam a democracia, o Estado de direito e os direitos humanos</strong>, além de economia de mercado. Alternativa <strong>E</strong>.</p><p>Há monarquias e repúblicas no bloco (A e C), nem todos os membros são da OTAN (B), há países do leste europeu (D), os parlamentos nacionais continuam existindo (D), e nem todos usam o euro (C).</p>"},
11: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["União Europeia"],
     "explicacao": "<p>Desde 1974, a Turquia ocupa militarmente o norte do <strong>Chipre</strong>, que é membro da União Europeia. Essa disputa é um dos entraves à sua entrada. Alternativa <strong>A</strong>.</p><p>A Turquia não usa o euro (B). O problema com os curdos é a repressão, não a recusa em expulsá-los (C). Parte do território turco fica na Europa (D). E a Turquia é um Estado laico (E).</p>"},
12: {"materia": "Física", "assunto": "Cinemática", "tags": ["teorema de Pitágoras"],
     "enunciado": p("A Estrela da Morte é uma arma ícone da série cinematográfica <em>Star Wars</em>. De formato esférico ela era considerada similar a uma Lua. Essa arma/estação espacial podia se locomover pelo espaço na velocidade da luz, ou seja, 3,0 × 10<sup>5</sup> km/s.",
                    "Admita que a Estrela da Morte precisasse se posicionar de maneira a realizar um ataque de máxima eficiência ao Planeta C. Inicialmente, a estação espacial encontrava-se no ponto A e, entre ela e o Planeta C, havia um grande asteroide, por isso necessitou ir para o ponto B, de modo a poder visualizar perfeitamente o Planeta C, conforme a figura.")
                  + "[[fig:1]]" + p("Assinale a alternativa que contém o tempo que a Estrela da Morte demorou para se locomover do ponto A para o B."),
     "imagens": [{"arquivo": "q12", "alt": "Triângulo retângulo ABC com ângulo reto em B. A hipotenusa AC mede 1,7 × 10¹⁰ km e tem um asteroide no meio. O cateto BC, horizontal, mede 8,0 × 10⁹ km. A Estrela da Morte está em A e o Planeta C, no vértice C."}],
     "alternativas": {"A": "5,0 × 10<sup>4</sup> s", "B": "15,0 × 10<sup>4</sup> s", "C": "45,0 × 10<sup>4</sup> s", "D": "\\(\\sqrt{353} \\times 10^4\\) s", "E": "\\(\\dfrac{\\sqrt{353}}{3} \\times 10^4\\) s"},
     "explicacao": "<p>Pelo teorema de Pitágoras, AB² = AC² − BC² = (17 × 10⁹)² − (8 × 10⁹)² = (289 − 64) × 10¹⁸ = 225 × 10¹⁸. Então AB = 15 × 10⁹ km = 1,5 × 10¹⁰ km.</p><p>O tempo é t = AB ÷ v = 1,5 × 10¹⁰ ÷ 3,0 × 10⁵ = <strong>5,0 × 10⁴ s</strong>. Alternativa <strong>A</strong>.</p><p>D e E vêm de somar os quadrados (289 + 64 = 353), o que daria a hipotenusa, e não um cateto.</p>"},
13: {"materia": "Física", "assunto": "Movimentos da Terra", "tags": ["Lua"],
     "enunciado": p("Durante o ciclo lunar de aproximadamente quatro semanas, observa-se uma mudança no diâmetro da Lua, quando a vemos de um mesmo local da superfície da Terra e sob a mesma altura no céu, relativamente ao horizonte.",
                    "A imagem apresenta uma montagem que permite a comparação desses diferentes tamanhos no decorrer de um ciclo completo.")
                  + "[[fig:1]]" + fonte("&lt;https://tinyurl.com/ya2euf2z&gt; Acesso em: 11.11.2018.")
                  + p("Admitindo que:", "• a metade esquerda da imagem corresponde ao maior diâmetro observável da Lua; e", "• a metade direita da imagem corresponde ao menor diâmetro observável da Lua.",
                      "Podemos dizer que a parte esquerda e a parte direita da imagem correspondem, nesta ordem, ao momento em que a Lua se encontra em seu"),
     "imagens": [{"arquivo": "q13", "alt": "Montagem de duas fotos da Lua cheia lado a lado: a metade esquerda, de uma Lua maior, e a metade direita, de uma Lua menor."}],
     "explicacao": "<p>A órbita da Lua em torno da Terra é elíptica. Quando a Lua está mais perto da Terra (<strong>perigeu</strong>), parece maior; quando está mais longe (<strong>apogeu</strong>), parece menor. Esquerda (maior) = perigeu; direita (menor) = apogeu. Alternativa <strong>E</strong>.</p><p>A inverte a ordem. Afélio e periélio se referem à órbita em torno do Sol, não à da Lua em torno da Terra (B, C e D).</p>"},
14: {"materia": "História", "assunto": "Idade Média", "tags": ["peste negra"],
     "enunciado": apoio(*[it(x, "Yersinia pestis") for x in T(7, "Os Estados Unidos levaram", "Organização Mundial da Saúde (OMS).", ["No final da Idade Média", "A bactéria responsável"])])
                  + url("https://tinyurl.com/y8jqf3um", "26.10.2018")
                  + p("A bactéria chegou à Europa medieval"),
     "explicacao": "<p>A peste negra chegou à Europa no século XIV pelos navios mercantes que vinham do Oriente (pelo mar Negro e pelo Mediterrâneo), com o <strong>renascimento comercial</strong> iniciado por volta do século XII. As pulgas dos <strong>ratos</strong> a bordo transmitiam a bactéria. Alternativa <strong>D</strong>.</p><p>Cães de caça, mudanças climáticas no século XVI, baleias e peregrinos fugindo do Império Romano não têm relação com a chegada da peste (A, B, C e E).</p>"},
15: {"materia": "Português", "assunto": "Figuras de linguagem", "tags": ["ambiguidade"],
     "enunciado": BAUDELAIRE + P15, "imagens": [BAUDELAIRE_IMG],
     "explicacao": "<p>No livro de Baudelaire, “do mal” se refere aos temas dos poemas, considerados imorais. Na charge, as flores dão conselhos de pequenos “pecados” do dia a dia (ignorar mensagens, maratonar séries em dia útil, comer bacon). O humor vem da <strong>ambiguidade</strong> da locução “do mal”. Alternativa <strong>E</strong>.</p><p>As flores não recitam versos do poeta (A), não representam costumes do século XIX (B), não são uma metáfora do poeta (C), e a palavra com duplo sentido é “do mal”, não “flores” (D).</p>"},
16: {"materia": "Português", "assunto": "Verbos", "tags": ["norma-padrão"],
     "enunciado": p("Leia os trechos seguintes:")
                  + apoio("<strong>I.</strong> “Quando te escreverem uma mensagem, visualize, mas não responda.”", "<strong>II.</strong> “Assista às maratonas de séries nos dias úteis.”", "<strong>III.</strong> “Coma bacon.”")
                  + p("Sobre os períodos apresentados, é correto afirmar que"),
     "apoio_de": (15, P15),
     "explicacao": "<p>Em I, “visualize” e “responda” estão no imperativo de terceira pessoa (você), mas o pronome “te” é de segunda pessoa (tu). A norma-padrão pede uniformidade de tratamento (“Quando lhe escreverem...”), mas a mistura é comum e adequada à fala informal. Alternativa <strong>A</strong>.</p><p>As falas não têm teor religioso (B). Comer bacon não é hábito saudável (C). As falas são informais, não da variedade culta (D). E os verbos estão no imperativo, não no subjuntivo (E).</p>"},
17: {"materia": "Português", "assunto": "Verbos", "tags": ["discurso indireto"],
     "enunciado": p("Se as falas das flores fossem transpostas para o discurso indireto, teríamos: <strong>As flores do mal aconselharam a Baudelaire que...</strong>",
                    "Assinale a alternativa que completa corretamente a frase com as falas transpostas."),
     "apoio_de": (15, P15),
     "explicacao": "<p>No discurso indireto, depois de um verbo no passado (“aconselharam”), o imperativo vira <strong>pretérito imperfeito do subjuntivo</strong> (“visualizasse”, “respondesse”, “assistisse”, “comesse”), o futuro do subjuntivo “escreverem” vira “escrevessem”, e “te” vira “lhe”. Alternativa <strong>B</strong>.</p><p>A, C e D usam futuro do pretérito (“responderia”, “comeria”) ou mantêm o futuro do subjuntivo. E mantém o discurso direto (“te”, “visualize”).</p>"},
18: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": ["verminoses"],
     "enunciado": p("Em uma região com alta incidência de doenças parasitárias, os alunos de uma escola técnica, na tentativa de diminuir a ocorrência de novos casos e colaborar com o Centro de Saúde local, elaboraram uma lista de medidas de prevenção e combate a essas doenças.", "Entre essas medidas, constavam as seguintes:")
                  + p("<strong>I.</strong> Andar sempre calçado.", "<strong>II.</strong> Ferver e filtrar a água antes de tomá-la.", "<strong>III.</strong> Promover uma campanha de vacinação.",
                      "<strong>IV.</strong> Aconselhar o uso controlado de inseticidas.", "<strong>V.</strong> Lavar muito bem frutas e verduras antes de as ingerir.", classe="apoio")
                  + p("Assinale a alternativa que associa corretamente a medida mais eficiente para prevenir, respectivamente, ascaridíase e ancilostomíase."),
     "explicacao": "<p>A <strong>ascaridíase</strong> (lombriga) se pega ao ingerir ovos do verme em água ou alimentos contaminados: ferver e filtrar a água (II) previne. A <strong>ancilostomíase</strong> (amarelão) se pega quando a larva do solo penetra pela pele dos pés: andar calçado (I) previne. Alternativa <strong>B</strong>.</p><p>Não há vacina contra essas verminoses (C e D), e inseticidas não as combatem, porque não são transmitidas por insetos (A e E). Lavar frutas e verduras (V) também ajuda contra a ascaridíase, mas não contra a ancilostomíase.</p>"},
19: {"materia": "Matemática", "assunto": "Razão e proporção",
     "explicacao": "<p>As 25 folhas de 30 cm somam 25 × 0,3 = 7,5 m. A 3 metros por minuto, o tempo é 7,5 ÷ 3 = 2,5 min = <strong>2 min 30 s</strong>. Alternativa <strong>C</strong>.</p><p>Cuidado com a conversão: 0,5 min são 30 s, e não 50 s.</p>"},
20: {"materia": "Biologia", "assunto": "Botânica", "tags": ["plantas tóxicas"],
     "enunciado": apoio(*T(10, "A planta comigo-ninguém-pode", "o processo alérgico.", ["A mastigação, ainda", "A irritação e o inchaço"]))
                  + fonte("(LOPES, SÔNIA. Bio: Volume 2. Saraiva, 2006. Adaptado)")
                  + "[[fig:1]]" + p("De acordo com o texto, é correto afirmar sobre a planta citada que"),
     "imagens": [{"arquivo": "q20", "alt": "Foto de uma comigo-ninguém-pode em um vaso: planta de caule ereto com folhas grandes, ovais, com manchas claras.", "legenda": "Planta comigo-ninguém-pode"}],
     "explicacao": "<p>O texto diz que, ao mastigar as folhas, os cristais de <strong>oxalato de cálcio</strong>, com pontas cortantes, perfuram a mucosa da boca, e a proteína do suco vacuolar penetra e causa lesões e alergia. Alternativa <strong>C</strong>.</p><p>As folhas manchadas sinalizam toxicidade, e a planta não serve de alimento (A). O texto fala de folhas e pecíolos, não de flores e raízes (B). Os componentes estão “apenas em certas células” (D). E a histamina é liberada pelas células da mucosa da pessoa, não pela planta (E).</p>"},
21: {"materia": "Biologia", "assunto": "Fisiologia humana", "tags": ["pele"],
     "explicacao": "<p>Os raios ultravioleta podem causar vermelhidão e queimaduras, e a exposição estimula a produção de <strong>melanina</strong>, pigmento que absorve parte da radiação e protege a pele. Alternativa <strong>E</strong>.</p><p>A camada de queratina protege contra atrito e perda de água, não é reserva nutritiva (A). O suor resfria o corpo ao evaporar (B). No frio, os vasos da pele se contraem para perder menos calor (C); no calor, eles se dilatam para perder mais (D).</p>"},
22: {"materia": "Física", "assunto": "Termologia", "tags": ["propagação do calor"],
     "enunciado": p("É possível utilizar a energia proveniente do Sol para aquecimento de água.")
                  + apoio("Um projeto simples e de baixo custo, que atinge esse objetivo, consiste em dispor uma mangueira muito longa e de cor preta, enrolada em espiral e cheia de água, sobre a superfície de uma laje exposta ao Sol. As extremidades dessa mangueira estão conectadas a um reservatório de água.",
                          "Por ser de cor preta, a mangueira é capaz de ____<strong>I</strong>____ a energia solar, que é transferida para a água contida na mangueira por ____<strong>II</strong>____. Uma bomba d’água é acionada automaticamente, de tempos em tempos, forçando a água aquecida para o interior do reservatório de onde foi retirada. Como a água aquecida é menos densa que a água fria, elas não se misturam. Assim sendo, a água aquecida permanece na parte ____<strong>III</strong>____ do reservatório.")
                  + p("Assinale a alternativa que apresenta as palavras que completam corretamente o texto."),
     "alternativas": colunas(["I", "II", "III"], [["absorver", "condução", "superior"], ["absorver", "convecção", "inferior"], ["refletir", "condução", "superior"], ["refletir", "condução", "inferior"], ["refratar", "convecção", "superior"]]),
     "explicacao": "<p>Superfícies pretas <strong>absorvem</strong> bem a radiação (I). O calor passa da parede da mangueira para a água em contato com ela por <strong>condução</strong> (II). E a água quente, menos densa, fica na parte <strong>superior</strong> do reservatório (III). Alternativa <strong>A</strong>.</p><p>Superfícies pretas não refletem nem refratam a luz (C, D e E), e a água quente não fica embaixo (B e D).</p>"},
23: {"materia": "Biologia", "assunto": "Botânica", "tags": ["fotossíntese"],
     "enunciado": p("Leia o trecho da letra da música <em>Luz do Sol</em>, de Caetano Veloso.") + "[[fig:1]]"
                  + p("Nessa letra, é possível notar um processo da biologia, importante para a sobrevivência dos seres vivos.",
                      "Assinale a alternativa que apresenta, corretamente, o nome e as principais características desse processo."),
     "imagens": [{"arquivo": "q23", "alt": "Trecho da letra da canção “Luz do Sol”, de Caetano Veloso, em duas estrofes, em itálico. A letra fala da luz do sol que a folha recebe e transforma em vida verde nova, e do céu azul que chega até a terra, que inspira e expira."}],
     "alternativas": colunas(["Nome do processo", "Principais características"], [
         ["Fotossíntese", "Oxidação de compostos orgânicos na presença de energia luminosa, formando moléculas de gás carbônico (CO<sub>2</sub>), de água (H<sub>2</sub>O) e liberando energia química que será usada pelos seres vivos."],
         ["Respiração", "Transformação de energia luminosa em energia potencial química, armazenada nas moléculas de glicídios (açúcares) produzidas no processo."],
         ["Fermentação", "Degradação completa de moléculas orgânicas liberando energia luminosa para a formação de moléculas de ATP (adenosina trifosfato)."],
         ["Fotossíntese", "Produção de compostos orgânicos, como, por exemplo, os açúcares, a partir de moléculas de gás carbônico (CO<sub>2</sub>) e de água (H<sub>2</sub>O), na presença de energia luminosa."],
         ["Respiração", "Liberação de energia química a partir da combustão da matéria orgânica, principalmente glicose, na presença de energia luminosa, gás carbônico (CO<sub>2</sub>) e água (H<sub>2</sub>O)."]]),
     "explicacao": "<p>A folha que “traduz” a luz do sol “em verde novo, em folha, em vida” remete à <strong>fotossíntese</strong>: produção de açúcares a partir de gás carbônico e água, usando a energia da luz. Alternativa <strong>D</strong>.</p><p>A descreve a respiração com o nome de fotossíntese. B descreve a fotossíntese com o nome de respiração. A fermentação é uma degradação parcial e não libera luz (C). E a respiração não depende de luz nem consome gás carbônico (E).</p>"},
24: {"materia": "Química", "assunto": "Reações químicas", "tags": ["termoquímica"],
     "enunciado": p("Leia o trecho da letra da música <em>Química</em>, de João Bosco e Vinícius de Moraes.") + "[[fig:1]]"
                  + p("Na segunda estrofe, a faísca desencadeia uma transformação"),
     "imagens": [{"arquivo": "q24", "alt": "Trecho da letra da canção “Química”, de João Bosco e Vinícius de Moraes, em duas estrofes. A primeira fala da química que uniu um casal desde o primeiro dia e de um amor cada vez mais intenso. A segunda fala de faróis que iluminavam o coração, de uma faísca que virou uma explosão e de uma paixão cada vez mais intensa."}],
     "explicacao": "<p>Uma explosão é uma reação de combustão: forma substâncias novas (transformação <strong>química</strong>) e <strong>libera</strong> muita energia, na forma de calor e luz (<strong>exotérmica</strong>). Alternativa <strong>A</strong>.</p><p>Na explosão há liberação, não absorção, de energia (B e C). E ela não é uma transformação física (C, D e E).</p>"},
25: {"materia": "Geografia", "assunto": "Cartografia", "tags": ["formas do relevo litorâneo"],
     "enunciado": FLUVIAL + P25, "imagens": [FLUVIAL_IMG],
     "explicacao": "<p>O singular de “istmos” é <strong>istmo</strong>: uma faixa estreita de terra que liga duas grandes porções de terra, como o istmo do Panamá, entre as Américas do Norte e do Sul. Alternativa <strong>E</strong>.</p><p>A descreve a restinga. B, a península (ou cabo). C, um cânion ou vale. D, uma baía ou enseada.</p>"},
26: {"materia": "Geografia", "assunto": "Cartografia", "tags": ["pontos cardeais"],
     "enunciado": p("As palavras escritas em negrito, na quarta estrofe, podem ser substituídas correta e respectivamente pelos termos"), "apoio_de": (25, P25),
     "alternativas": {"B": "leste e norte."},
     "explicacao": "<p><strong>Ocidental</strong> se refere ao ocidente, o <strong>oeste</strong>. <strong>Setentrional</strong> se refere ao norte. Alternativa <strong>D</strong>.</p><p>Oriental seria leste, e meridional, sul (A, B, C e E).</p>"},
27: {"materia": "Física", "assunto": "Energia", "tags": ["trabalho"],
     "enunciado": p("O gráfico indica como varia a intensidade de uma força aplicada ininterruptamente sobre um corpo enquanto é realizado um deslocamento na mesma direção e no mesmo sentido das forças aplicadas.",
                    "Na Física, existe uma grandeza denominada trabalho. O trabalho de uma força, durante a realização de um deslocamento, é determinado pelo produto entre essas duas grandezas quando ambas têm a mesma direção e sentido.")
                  + "[[fig:1]]" + p("Considerando o gráfico dado, o trabalho total realizado no deslocamento de 8 m, em joules, corresponde a"),
     "imagens": [{"arquivo": "q27", "alt": "Gráfico de força (N) por deslocamento (m), em degraus: força de 60 N de 0 a 2 m, de 40 N de 2 a 6 m e de 20 N de 6 a 8 m."}],
     "explicacao": "<p>O trabalho é a área sob o gráfico, trecho a trecho: 60 × 2 = 120 J; 40 × 4 = 160 J; 20 × 2 = 40 J. Total: 120 + 160 + 40 = <strong>320 J</strong>. Alternativa <strong>D</strong>.</p><p>Usar só um dos trechos, ou errar a largura do trecho de 40 N (que vai de 2 a 6 m), leva aos outros valores.</p>"},
28: {"materia": "História", "assunto": "Escravidão", "tags": ["Palmares"],
     "enunciado": p("Leia o trecho do poema <em>Quilombo</em>, de José Carlos Limeira.") + "[[fig:1]]"
                  + fonte("(LIMEIRA, José Carlos; “Quilombos”. In: Atabaques. Rio de Janeiro: Max, 1979. p.19-24)")
                  + p("O poema faz referência a Palmares e à ideia de liberdade, os quais caracterizam"),
     "imagens": [{"arquivo": "q28", "alt": "Trecho do poema “Quilombo”, de José Carlos Limeira, em versos curtos. O eu lírico se dirige a uma pessoa negra, diz que, se Palmares ainda vivesse, queria viver lá, e fala do gosto da liberdade cravado no peito, de correr, sentir os campos e ter a vida."}],
     "explicacao": "<p>Palmares, na serra da Barriga, em Alagoas, foi o <strong>maior e mais duradouro quilombo</strong> do Brasil colonial: resistiu por quase todo o século XVII e abrigou milhares de pessoas escravizadas que fugiam. Alternativa <strong>D</strong>.</p><p>As outras alternativas tratam de episódios sem relação com Palmares: a Inconfidência Mineira (A), terras indígenas (B), o Carandiru (C) e as reformas de Pereira Passos (E).</p>"},
29: {"materia": "Química", "assunto": "Funções inorgânicas", "tags": ["ligação iônica"],
     "enunciado": QUEBRA + P29, "imagens": [QUEBRA_IMG],
     "explicacao": "<p>K<sup>+</sup> (metal) e NO<sub>3</sub><sup>–</sup> formam um composto por atração entre íons: <strong>iônico</strong>. O nome vem do ânion e depois do cátion: <strong>nitrato de potássio</strong> (KNO<sub>3</sub>). Alternativa <strong>A</strong>.</p><p>“Potássico de nitrogênio” e “potássio de nitrogênio” não seguem a nomenclatura (B e D). E o composto não é molecular nem metálico (C, D e E).</p>"},
30: {"materia": "Química", "assunto": "Funções inorgânicas", "tags": ["ligação iônica"],
     "enunciado": p("Unindo as peças do quebra-cabeça de cátions e ânions, o aluno pode concluir, corretamente, que o cloreto de bário apresenta a fórmula"), "apoio_de": (29, P29),
     "alternativas": {"A": "BaCℓ.", "B": "BaCℓ<sub>2</sub>.", "C": "CℓBa.", "D": "CℓBa<sub>2</sub>.", "E": "Ba<sub>2</sub>Cℓ<sub>2</sub>."},
     "explicacao": "<p>A peça do Ba<sup>2+</sup> tem carga +2 e ocupa o lugar de duas peças de Cl<sup>–</sup> (carga −1 cada). Para neutralizar, são dois cloretos para um bário: <strong>BaCℓ<sub>2</sub></strong>. Alternativa <strong>B</strong>.</p><p>A não neutraliza as cargas. C e D põem o ânion antes do cátion. E não está na menor proporção e também não neutraliza as cargas.</p>"},
31: {"materia": "Química", "assunto": "Funções inorgânicas", "tags": ["sal de cozinha"],
     "enunciado": p("Leia o trecho do poema <em>A Arte de Cozinhar</em>, de Vânia Jesus.") + "[[fig:2]]" + url("https://tinyurl.com/ybs2sxe8", "23.10.2018")
                  + p("Na segunda linha, a autora faz referência a um tempero muito utilizado em nossas cozinhas.",
                      "Assinale a alternativa que apresenta, corretamente, os números das peças do quebra-cabeça que representam a fórmula do principal componente desse tempero."),
     "apoio_de": (29, P29),
     "imagens": [{"arquivo": "q31", "alt": "Trecho do poema “A Arte de Cozinhar”, de Vânia Jesus. Os versos falam de pôr mais um pouco de alecrim, de uma pitada de sal (na segunda linha), de provar o gosto, conferir os temperos e acrescentar batata, cenoura, coentro, azeite e tomate, até que a magia da cozinha acontece."}],
     "alternativas": colunas(["Cátion", "Ânion"], [["4", "3"], ["5", "4"], ["5", "2"], ["3", "3"], ["3", "4"]]),
     "explicacao": "<p>O tempero da segunda linha é o <strong>sal</strong>, cujo principal componente é o cloreto de sódio, NaCℓ. Na fila de cátions, Na<sup>+</sup> é a peça <strong>3</strong>; na fila de ânions, Cl<sup>–</sup> é a peça <strong>4</strong>. Alternativa <strong>E</strong>.</p><p>As outras combinações formam brometo de bário (A), cloreto de cálcio (B), carbonato de cálcio (C) e brometo de sódio (D).</p>"},
32: {"materia": "Física", "assunto": "Circuitos elétricos",
     "enunciado": p("Quatro lâmpadas de filamento, idênticas, são conectadas a duas pilhas obedecendo ao circuito elétrico. Inicialmente, as quatro lâmpadas encontram-se acesas.")
                  + "[[fig:1]]"
                  + apoio("Admita que, se apenas uma dessas lâmpadas fosse ligada às duas pilhas, ela não se queimaria por sobrecarga.")
                  + p("Se, em dado momento, somente a lâmpada L<sub>4</sub> tiver seu filamento rompido, apagando-se, é correto concluir que"),
     "imagens": [{"arquivo": "q32", "alt": "Circuito com duas pilhas em série, embaixo, e quatro lâmpadas: L1 e L2 ligadas em série no ramo de cima; L3 e L4 ligadas em série no ramo do meio. Os dois ramos estão ligados em paralelo às pilhas."}],
     "explicacao": "<p>L<sub>3</sub> e L<sub>4</sub> estão em série no mesmo ramo: se o filamento de L<sub>4</sub> rompe, o ramo fica aberto e L<sub>3</sub> também apaga. O ramo de L<sub>1</sub> e L<sub>2</sub>, ligado em paralelo, continua recebendo corrente. Alternativa <strong>B</strong>.</p><p>L<sub>3</sub> não pode ficar acesa sem L<sub>4</sub> (A, C e D), e o outro ramo não é afetado (E).</p>"},
33: {"materia": "Biologia", "assunto": "Ecologia", "tags": ["teia alimentar"],
     "enunciado": p("As relações alimentares entre os diversos organismos de um ecossistema são denominadas teias alimentares. Essas teias são formadas por diversas cadeias alimentares interligadas entre si, por meio de linhas, que unem os diversos componentes da comunidade, evidenciando suas relações quanto ao aspecto alimentar.")
                  + "[[fig:1]]" + p("Considerando a teia alimentar representada na figura, pode-se afirmar corretamente que os organismos"),
     "imagens": [{"arquivo": "q33", "alt": "Teia alimentar com setas que indicam quem serve de alimento a quem: I → II, II → III, I → IV, IV → V, IV → VI, V → III, V → VI, V → VII e VII → VI."}],
     "explicacao": "<p>I é o produtor (as setas só saem dele). III come II, que comeu I (cadeia I → II → III): é consumidor de <strong>segunda ordem</strong>. III também come V, que comeu IV, que comeu I (I → IV → V → III): aí é consumidor de <strong>terceira ordem</strong>. Alternativa <strong>D</strong>.</p><p>III não é só consumidor primário (A). V come IV, que é consumidor primário, então V é de segunda ordem, e VII come V, sendo de terceira (B). IV e VII são consumidores, não decompositores (C). E I é produtor, não parasita (E).</p>"},
34: {"materia": "Física", "assunto": "Energia", "tags": ["consumo de energia elétrica"],
     "enunciado": p("Um estudante avaliou o tempo diário do uso do chuveiro em sua casa no decorrer de trinta dias consecutivos, o que permitiu a construção do quadro.")
                  + tabela(["Morador", "Tempo diário em minutos"], [["Mãe", "20"], ["Pai", "15"], ["Irmã", "20"], ["Irmão", "5"], ["Ele próprio", "30"]])
                  + p("Sabendo que o chuveiro de sua casa tem potência de 2 800 W, o estudante calculou que, no período avaliado, o consumo de energia em sua casa, devido ao uso do chuveiro, foi, aproximadamente, de"),
     "explicacao": "<p>Por dia, o chuveiro fica ligado 20 + 15 + 20 + 5 + 30 = 90 min = 1,5 h. Em 30 dias: 45 h. A energia é E = P × t = 2,8 kW × 45 h = 126 kWh ≈ <strong>125 kWh</strong>. Alternativa <strong>C</strong>.</p><p>Esquecer de converter os minutos em horas ou de multiplicar pelos 30 dias leva a valores bem diferentes.</p>"},
35: {"materia": "História", "assunto": "História contemporânea", "tags": ["Iluminismo"],
     "enunciado": apoio("Quando na mesma pessoa, ou no mesmo órgão de governo, o poder Legislativo está unido ao poder Executivo, não existe liberdade […] E também não existe liberdade se o poder Judiciário (poder de julgar) não estiver separado do poder Legislativo (poder de fazer as leis) e do poder Executivo (poder de executar, de por em prática as leis.)")
                  + fonte("Montesquieu, O espírito das leis, 1748. <em>In</em>: FREITAS, G. de; <em>900 textos e documentos de História</em>. Lisboa: Plátano, 1978. V. III, p.24")
                  + p("Político, filósofo e escritor, o Barão de Montesquieu (1689–1755) se notabilizou por sua teoria sobre a separação dos poderes, que organiza o funcionamento de muitos dos Estados modernos até a atualidade.",
                      "Ao formular sua teoria, Montesquieu criticou o regime absolutista e defendeu a divisão do governo em três poderes – Executivo, Legislativo e Judiciário – como forma de"),
     "explicacao": "<p>Para Montesquieu, quando os poderes se concentram nas mesmas mãos “não existe liberdade”. A separação dos poderes serve para <strong>evitar a concentração de poder e os abusos</strong> e proteger as liberdades individuais. Alternativa <strong>C</strong>.</p><p>Ele criticava o absolutismo, não queria fortalecê-lo (A e D). A teoria busca equilíbrio entre os poderes, não enfraquecer o Judiciário (B) nem eliminar governos (E).</p>"},
36: {"materia": "Matemática", "assunto": "Razão e proporção",
     "explicacao": "<p>A razão é 12 milhões de habitantes para 9 milhões de eleitores, ou seja, 12 : 9 = 4 : 3. Para cada 3 eleitores existem <strong>4 habitantes</strong>. Alternativa <strong>D</strong>.</p><p>3 habitantes seria igualar o número de habitantes ao de eleitores (E). Os demais valores não respeitam a proporção 4 : 3.</p>"},
37: {"materia": "Português", "assunto": "Verbos",
     "enunciado": CHARGE + P37, "imagens": [CHARGE_IMG],
     "alternativas": {"A": "<em>Ajuda</em>, presente do indicativo, <em>ajudo</em>, pretérito perfeito do indicativo.",
                      "B": "<em>Ajuda</em>, presente do subjuntivo, <em>ajudo</em>, presente do subjuntivo.",
                      "C": "<em>Ajuda</em>, pretérito do subjuntivo, <em>ajudo</em>, presente do indicativo.",
                      "D": "<em>Ajuda</em>, imperativo afirmativo, <em>ajudo</em>, presente do indicativo.",
                      "E": "<em>Ajuda</em>, imperativo afirmativo, <em>ajudo</em>, futuro do indicativo."},
     "explicacao": "<p>“Me ajuda a comer” é um pedido, uma ordem dirigida ao candidato: <strong>imperativo afirmativo</strong>. “Te ajudo” indica uma ação no momento da fala, na 1ª pessoa: <strong>presente do indicativo</strong>. Alternativa <strong>D</strong>.</p><p>“Ajuda” aqui não descreve um fato (A), e o subjuntivo seria “ajude” (B e C). “Ajudo” não é pretérito (que seria “ajudei”) nem futuro (“ajudarei”) (A e E).</p>"},
38: {"materia": "Português", "assunto": "Classes de palavras", "tags": ["formação de palavras"],
     "enunciado": p("O título da charge “democracinhas” é um neologismo composto pelo mesmo processo de formação presente no termo"), "apoio_de": (37, P37),
     "alternativas": {"A": "<em>desanuviar</em>, derivação sufixal.", "B": "<em>inativo</em>, derivação parassintética.", "C": "<em>girassol</em>, composição por hibridismo.", "D": "<em>fidalgo</em>, composição por aglutinação.", "E": "<em>televisão</em>, derivação prefixal e sufixal."},
     "explicacao": "<p>“Democracinhas” junta “democracia” e “gracinhas” (ou “cracinhas”) numa só palavra, com perda de sons: é <strong>composição por aglutinação</strong>, como “fidalgo” (filho + de + algo). Alternativa <strong>D</strong>.</p><p>“Desanuviar” não é formada por sufixo, e sim pelo prefixo des- (A). “Inativo” é derivação prefixal (B). “Girassol” é composição por justaposição, e não hibridismo (C). E “televisão” é hibridismo (grego + latim) (E). Em todas, o processo e o nome não combinam.</p>"},
39: {"materia": "Português", "assunto": "Classes de palavras",
     "enunciado": p("Observe as passagens:")
                  + apoio("<strong>I.</strong> “Candidato, <strong>me</strong> ajuda <strong>a</strong> comer, candidato!”",
                          "<strong>II.</strong> “<strong>Mas</strong> é claro <strong>que</strong> te ajudo! Tem <strong>aí</strong> um sanduíche para <strong>a</strong> gente dividir?”")
                  + p("Assinale a alternativa que apresenta a análise correta da função morfológica dos termos destacados nas passagens."),
     "apoio_de": (37, P37),
     "alternativas": colunas(["I – me", "I – a", "II – Mas", "II – que", "II – aí", "II – a"], [
         ["Pronome pessoal", "Preposição", "Conjunção", "Conjunção", "Advérbio", "Artigo"],
         ["Pronome indefinido", "Artigo", "Preposição", "Pronome relativo", "Advérbio", "Preposição"],
         ["Pronome reflexivo", "Conjunção", "Conjunção", "Pronome relativo", "Advérbio", "Pronome pessoal"],
         ["Pronome pessoal reto", "Preposição", "Preposição", "Pronome relativo", "Pronome pessoal", "Artigo"],
         ["Pronome pessoal", "Pronome pessoal", "Conjunção", "Conjunção", "Pronome demonstrativo", "Preposição"]]),
     "explicacao": "<p>Em I, “me” é pronome pessoal (oblíquo) e “a” liga “ajuda” a “comer”: preposição. Em II, “Mas” é conjunção; “que” introduz a oração “que te ajudo” (conjunção integrante); “aí” indica lugar (advérbio); e “a”, em “a gente”, é artigo. Alternativa <strong>A</strong>.</p><p>As outras classificam errado ao menos um termo: “me” não é indefinido nem reto (B e D), o primeiro “a” não é artigo nem conjunção (B e C), e “aí” não é pronome (D e E).</p>"},
40: {"materia": "Matemática", "assunto": "Operações e problemas",
     "explicacao": "<p>Os 450 eleitores se dividem igualmente entre as 6 seções: 450 ÷ 6 = 75 por seção. As seções funcionam ao mesmo tempo, então o tempo total é o de uma seção: 75 × 3 = 225 min = <strong>3 h 45 min</strong>. Alternativa <strong>B</strong>.</p><p>Somar o tempo de todos os eleitores, como se houvesse uma só urna, daria 1 350 min, mais de 22 horas.</p>"},
41: {"materia": "História", "assunto": "História contemporânea", "tags": ["Primeira Guerra Mundial"],
     "enunciado": p("Leia um trecho do Tratado de Versalhes.")
                  + apoio("Os governos aliados e associados afirmam e a Alemanha aceita a sua responsabilidade e a dos que lutaram a seu lado por ter causado todas as perdas e prejuízos que os governos aliados e seus associados sofreram, assim como seus habitantes, em consequência da guerra, imposta a eles pela agressão da Alemanha e dos que lutaram a seu lado.")
                  + fonte("Tratado de Versalhes, artigo 231, 1919. <em>In</em>: DOMINGUES, Joelza Esther. <em>História em documento. Imagem e texto</em>. 9. 2ªed. São Paulo: FTD, 2013. p.89.")
                  + p("O Tratado foi assinado após a derrota alemã na"),
     "explicacao": "<p>O Tratado de Versalhes (1919) encerrou a <strong>Primeira Guerra Mundial</strong>. A Alemanha foi declarada culpada, perdeu suas colônias e parte do território, foi desmilitarizada e teve de pagar pesadas indenizações, o que agravou sua crise econômica. Alternativa <strong>E</strong>.</p><p>A divisão da Alemanha e o Muro de Berlim vieram depois da Segunda Guerra (A). As guerras Franco-Prussiana, Austro-Prussiana e da Crimeia são do século XIX e não terminaram com esse tratado (B, C e D).</p>"},
42: {"materia": "Geografia", "assunto": "Regionalização do Brasil",
     "explicacao": "<p>A Constituição de 1988 transformou os territórios federais de Roraima e Amapá em estados (Rondônia já virara estado em 1981), todos na região <strong>Norte</strong>. Alternativa <strong>B</strong>.</p><p>Tocantins foi criado em 1988, mas incorporado à região Norte (A). Fernando de Noronha passou a Pernambuco (C). Mato Grosso e Mato Grosso do Sul são do Centro-Oeste (D). E a Guanabara foi fundida ao Rio de Janeiro em 1975, no Sudeste (E).</p>"},
43: {"materia": "História", "assunto": "Brasil Colônia", "tags": ["invasões holandesas"],
     "enunciado": p("Frans Post, pintor, desenhista e gravador holandês, documentou paisagens e cenas do cotidiano do chamado “Brasil Holandês”, sob o governo de Maurício de Nassau (1630–1654).")
                  + "[[fig:1]]" + url("https://tinyurl.com/y7dtz4c8", "26.10.2018", "Original colorido.")
                  + p("Entre as características da presença holandesa em Pernambuco, pode-se citar, corretamente,"),
     "imagens": [{"arquivo": "q43", "alt": "Pintura de paisagem: à esquerda, coqueiros e um conjunto de casas brancas, com pessoas reunidas em um terreiro; ao fundo, à direita, a água de um porto e a silhueta de uma cidade no horizonte.", "legenda": "Vista da Cidade Maurícia, Recife. Frans Post, 1657."}],
     "explicacao": "<p>Sob Maurício de Nassau, houve <strong>tolerância religiosa</strong> (inclusive com a primeira sinagoga das Américas), vieram cientistas e artistas para estudar a fauna e a flora, e Recife ganhou obras como a drenagem de áreas alagadas e a primeira grande ponte do Brasil. Alternativa <strong>E</strong>.</p><p>Os holandeses mantiveram a escravidão e o açúcar (A). Havia tolerância, e não perseguição, e eles não mineraram ouro (B). Não implantaram absolutismo e valorizaram artistas (C). E as pesquisas eram sobre a natureza tropical, não sobre geologia e astronomia (D).</p>"},
44: {"materia": "Matemática", "assunto": "Geometria plana", "tags": ["semelhança de triângulos"],
     "enunciado": p("Sem dispor de uma trena de comprimento suficiente, um pedreiro determinou a medida do desnível (d) de um terreno, valendo-se da propriedade da propagação retilínea da luz.",
                    "Observou que, em determinado momento do dia, um muro vertical de 1,5 m de altura, construído na parte alta do terreno, projetava uma sombra de 0,4 m sobre a parte superior do terreno, que era plana e horizontal. No mesmo instante, o desnível do terreno projetava sobre a parte mais baixa, igualmente horizontal, uma sombra de 1,6 m, conforme a figura.")
                  + "[[fig:1]]" + p("Com suas observações, foi capaz de deduzir corretamente que o desnível do terreno era de"),
     "imagens": [{"arquivo": "q44", "alt": "Corte de um terreno em dois níveis. Na parte alta, um muro vertical projeta uma sombra de 0,4 m. Raios de sol paralelos e inclinados passam pelo topo do muro e pela borda do desnível. O desnível vertical d projeta, na parte baixa, uma sombra de 1,6 m."}],
     "explicacao": "<p>Os raios de sol são paralelos, então o muro e o desnível formam triângulos semelhantes com suas sombras: \\(\\dfrac{1{,}5}{0{,}4} = \\dfrac{d}{1{,}6}\\). Então \\(d = \\dfrac{1{,}5 \\times 1{,}6}{0{,}4} = 6{,}0\\) m. Alternativa <strong>A</strong>.</p><p>Os outros valores vêm de montar a proporção de forma errada.</p>"},
45: {"materia": "Geografia", "assunto": "Regionalização do Brasil", "tags": ["América do Sul"],
     "explicacao": "<p>O Suriname foi <strong>colônia holandesa</strong> (a Guiana Holandesa) e se tornou independente em <strong>1975</strong>. Alternativa <strong>B</strong>.</p><p>Houve escravidão no Suriname (A). A língua oficial é o holandês (C). O país é banhado pelo Atlântico e não tem Andes (D). E sua economia depende sobretudo de minérios, como bauxita, ouro e petróleo (E).</p>"},
46: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": ["soro e vacina"],
     "explicacao": "<p>O soro traz <strong>anticorpos prontos</strong>, que agem logo, mas desaparecem em poucos dias e não geram memória. Por isso serve para <strong>tratar</strong>, não para prevenir. Alternativa <strong>D</strong>.</p><p>O soro contém anticorpos, não antígenos (A). A vacina contém antígenos e previne, enquanto o soro trata (B). Os anticorpos do soro somem em poucos dias (C). E quem atua na defesa são os leucócitos, não as hemácias (E).</p>"},
47: {"materia": "Matemática", "assunto": "Porcentagem",
     "enunciado": NOBEL + P47, "imagens": [NOBEL_IMG],
     "alternativas": {"A": "y = x + 0,12", "B": "y = 1,12x", "C": "y = 12x", "D": "x = 1,12y", "E": "x = y + 0,12"},
     "explicacao": "<p>Aumentar 12% é multiplicar por 1 + 0,12 = 1,12. Se o valor de 2016 é x, o de 2017 é <strong>y = 1,12x</strong>. Alternativa <strong>B</strong>.</p><p>Somar 0,12 (A e E) não é aumentar 12%. Multiplicar por 12 seria aumentar 1 100% (C). E D inverte os anos.</p>"},
48: {"materia": "Matemática", "assunto": "Porcentagem",
     "enunciado": p("Com base nas informações contidas no texto e assumindo que, em 2016, uma coroa sueca era equivalente a R$ 0,42, pode-se afirmar que o valor aproximado do Prêmio Nobel, para cada modalidade de premiação, em 2016 era, em milhões de reais, de cerca de"),
     "apoio_de": (47, P47),
     "explicacao": "<p>O prêmio de 2017 (9 milhões de coroas) é o de 2016 com 12% de aumento, então x = 9 ÷ 1,12 ≈ 8,04 milhões de coroas. Em reais: 8,04 × 0,42 ≈ 3,38 milhões. A alternativa mais próxima é <strong>3,33</strong>. Alternativa <strong>A</strong>.</p><p>O valor exato 3,33 sai de tirar 12% de 9 milhões (9 × 0,88 = 7,92) e converter (7,92 × 0,42 ≈ 3,33). Esse atalho não é exato, porque desfazer um aumento de 12% é dividir por 1,12, e não tirar 12%. Mesmo assim, a resposta é a A. 3,78 é o prêmio de 2017 em reais (9 × 0,42), sem desfazer o aumento (C). 7,92 está em coroas, não em reais (E). E 5,04 corresponde a 12 × 0,42, sem relação com o texto (D).</p>"},
49: {"materia": "Matemática", "assunto": "Geometria espacial", "tags": ["volume"],
     "enunciado": p("Um vencedor do Prêmio Nobel deseja encomendar a construção de uma caixa para acomodar a medalha que recebeu como parte da premiação. A caixa terá a forma de um paralelepípedo de base quadrada, sobre a qual sabe-se que:",
                    "• a medida do lado da base é 4 mm maior do que o diâmetro da medalha;", "• o volume total é igual a 147 cm<sup>3</sup>;", "• o material do qual a caixa será feita tem espessura desprezível.")
                  + "[[fig:2]]" + p("A altura da caixa, em centímetros, será igual a"),
     "apoio_de": (47, P47),
     "imagens": [{"arquivo": "q49", "alt": "Desenho em perspectiva de uma caixa em forma de paralelepípedo, larga e baixa."}],
     "explicacao": "<p>O lado da base mede 66 + 4 = 70 mm = 7 cm, e a área da base é 7 × 7 = 49 cm². Como V = área da base × altura, a altura é 147 ÷ 49 = <strong>3,0 cm</strong>. Alternativa <strong>C</strong>.</p><p>Esquecer de somar os 4 mm (base de 6,6 cm) daria cerca de 3,4 cm, que não está entre as alternativas.</p>"},
50: {"materia": "Geografia", "assunto": "Tectônica de placas", "tags": ["rochas"],
     "explicacao": "<p>Rochas formadas pela transformação de outras, sob altas pressões e temperaturas no interior da Terra, sem chegar a derreter, são as <strong>metamórficas</strong> (como o mármore, que vem do calcário). Alternativa <strong>E</strong>.</p><p>Ígneas, plutônicas e magmáticas se formam pelo resfriamento do magma (A, B e C). Sedimentares se formam pelo acúmulo e compactação de sedimentos na superfície (D).</p>"},
}
completar(Q, R)
