# Ajustes da conferência humana: Vestibular FATEC 1º semestre de 2024 (exame de 07/01/2024)
# Texto conferido com a imagem de cada página. Tema implícito: Arte (a redação pede "A importância da representatividade na Arte para a sociedade").
# 54 questões; a prova tem 5 h no total, incluindo a redação (que fica fora do simulado).
# Matéria: a do gabarito oficial; nas "Multidisciplinar", a matéria principal + tag "multidisciplinar".
# O rascunho transformou as caixas de texto em figuras: os textos vêm do PDF via trecho(). Q14 sumiu do rascunho: escrita à mão.
# Letras de canção (Fotografia 3x4, O Pulso) ficam como imagem, com alt descritivo, sem transcrever.
# Gabarito: oficial (1SEM24), sem anuladas nem retificadas.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import A, carregar, enun, tabela, colunas, completar, trecho

ID = "fatec-2024-1sem"
META = {
    "id": ID,
    "banca": "FATEC",
    "ano": 2024,
    "semestre": 1,
    "titulo": "Vestibular FATEC, 1º semestre de 2024",
    "fonte": "Centro Paula Souza",
    "dataExame": "2024-01-07",
    "duracaoMinutos": 300,
    "tema": "Arte",
    "pdf": f"assets/provas/{ID}.pdf",
}

R = carregar(ID)
MULTI = ["multidisciplinar"]


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


def figs(*pares):
    return [{"arquivo": a, "alt": t} for a, t in pares]


def it(texto, *termos):
    for t in termos: texto = texto.replace(t, f"<em>{t}</em>")
    return texto


def alts(*textos):
    return dict(zip("ABCDE", textos))


def troca(html, pares):
    for a, b in pares:
        assert a in html, a
        html = html.replace(a, b, 1)
    return html


# ---------- textos compartilhados ----------
LOUVRE = (chamada("Leia o texto para responder às questões 06 e 07.")
          + p("O Museu do Louvre em Paris, na França, é atualmente o museu mais visitado do mundo.")
          + p("<strong>Número de visitantes ao Museu do Louvre de 2007 a 2022 (em milhões)</strong>") + "[[fig:1]]"
          + fonte("Fonte dos dados: &lt;https://tinyurl.com/8973c75k&gt; Acesso em: 19.10.2023."))
LOUVRE_IMG = figs(("q06", "Gráfico de barras do número de visitantes do Louvre, em milhões, por ano: 2007, 8,3; 2008, 8,5; 2009, 8,5; 2010, 8,5; 2011, 8,9; 2012, 9,7; 2013, 9,3; 2014, 9,3; 2015, 8,6; 2016, 7,3; 2017, 8,1; 2018, 10,2; 2019, 9,6; 2020, 2,7; 2021, 2,8; 2022, 7,7."))
P6 = p("Analisando os dados do número de visitantes ao Museu do Louvre, em milhões, assinale a alternativa que apresenta, correta e respectivamente, a moda e a mediana desse conjunto.")

BLOOD = (chamada("Leia o texto para responder às questões de 08 a 10.")
         + apoio(*T(5, "The longstanding mystery surrounding", "channels in the glacier.", ["Now, thanks to research", "The research team calculates"]))
         + url("https://tinyurl.com/22vb439j", "16.08.2023", ""))
BLOOD = troca(BLOOD, [("The longstanding", "The <u>longstanding</u>"), ("has finally been", "has <u>finally</u> been"), ("coloring is due to", "coloring is <strong>due to</strong>")])
P8 = p("As palavras <em>longstanding</em> e <em>finally</em>, sublinhadas no primeiro período do texto, evidenciam a")

MARAJO = (chamada("Leia o texto para responder às questões 13 e 14.")
          + apoio(*T(6, "Na ilha de Marajó, pertencente ao Pará", "e jenipapo."))
          + fonte("&lt;https://tinyurl.com/2s474vzp&gt; Acesso em: 23.08.23. Adaptado.")
          + p(*T(6, "No Pará, podemos visitar diversos museus", "base igual a 10 cm.")))
P13 = p(*T(6, "Um artista cria uma cópia exata", "com tinta de urucum."),
        "Para fazer essa tinta, ele usa uma receita própria que consiste em misturar, em um recipiente, 30 mL de azeite de oliva a 12 g de urucum em pó. A tintura obtida rende a pintura de uma área de 450 cm².",
        "Considere que 1000 mL de azeite custe R$ 60,00 e que 100 g de urucum em pó custe R$ 2,00.",
        "Assinale a alternativa que apresenta, corretamente, o custo com matéria-prima para a elaboração da receita de tinta de urucum na quantidade necessária para que o artista realize a pintura proposta. (Utilize π = 3)")

PORTINARI = (chamada("Leia o texto para responder às questões 15 e 16.")
             + apoio(*T(7, "Cândido Portinari, um dos principais pintores", "cádmio e selênio.", ["Uma das técnicas utilizadas"]))
             + url("https://tinyurl.com/ykp5t3zp", "20.08.2023"))
P15 = p("A emissão de luz, que ocorre na técnica de análise mencionada no texto, é explicada corretamente pelo modelo atômico de")

TIRA = (chamada("Leia a tirinha para responder às questões 18 e 19.") + "[[fig:1]]"
        + url("https://tinyurl.com/3yp3w7df", "25.08.2023", "Original colorido."))
TIRA_IMG = figs(("q18", "Tirinha “Cientirinhas #48”, de Merlin, em quatro quadrinhos. O primeiro traz o título, em inglês: “Songs to listen to doing scientific facepalm” (músicas para ouvir dando um tapa na testa científico). Nos outros três, uma pessoa diferente ouve uma música e cobre o rosto com a mão, constrangida com um erro científico na letra, citada em inglês no alto do quadrinho. No segundo, uma jovem com camiseta do Iron Maiden ouve uma letra que põe dinossauros e homens vivendo na mesma época. No terceiro, um rapaz com um disco de Joan Baez ouve uma letra que fala de uma voz conhecida “alguns anos-luz atrás” (light-years ago). No quarto, uma moça com um pôster de Sheryl Crow ouve uma letra segundo a qual o trovão é ouvido antes de o raio cair."))
P18 = p("Analisando a linguagem verbal e não verbal da tirinha, é correto afirmar que a frustração da personagem,")

MUNDANO = (chamada("Leia o texto para responder às questões 23 e 24.")
           + apoio(*T(10, "Pintado com terra e cinzas das florestas", "protagonista da intervenção.", ["A pintura foi uma iniciativa"]))
           + url("https://tinyurl.com/2s4f37v6", "25.08.2023"))
MUNDANO = troca(MUNDANO, [("Bananal", "<em>Bananal</em>")])
P23 = p("Com base no texto, pode-se concluir corretamente que")

CANUDOS = (chamada("Leia os textos para responder às questões 48 e 49.")
           + apoio(*T(20, "A Guerra de Canudos aconteceu", "homens, mulheres e crianças.", ["Teve caráter messiânico"]))
           + url("https://tinyurl.com/2p392kzv", "21.08.2023")
           + p("O jornalista Euclides da Cunha foi correspondente de um jornal de São Paulo na Guerra de Canudos. Com base na sua vivência, ele escreveu o livro <em>Os Sertões</em>, publicado pela primeira vez em 1902. Em uma passagem do livro, ele escreveu que")
           + apoio(*T(20, "“Canudos não se rendeu.", "cinco mil soldados.”"))
           + fonte("CUNHA, Euclides da. <em>Os Sertões</em>. Rio de Janeiro: Record, 1998."))

CANDIDO_TXT = (
    "<strong>Se</strong><sup>I</sup> fosse possível abstrair o sentido e pensar nas palavras como tijolos de uma construção, eu diria que esses tijolos representam um modo de organizar a matéria, e <strong>que</strong><sup>II</sup> enquanto organização eles exercem papel ordenador sobre a nossa mente. Quer percebamos claramente ou não, o caráter de coisa organizada da obra literária torna-se um fator <strong>que</strong><sup>III</sup> nos deixa mais capazes de ordenar a nossa própria mente e sentimentos; e, em consequência, mais capazes de organizar a visão que temos do mundo."
    + A +
    "<strong>Por isso</strong><sup>IV</sup>, um poema hermético, de entendimento difícil, sem nenhuma alusão tangível à realidade do espírito ou do mundo, pode funcionar neste sentido, pelo fato de ser um tipo de ordem, sugerindo um modelo de superação do caos. A produção literária tira as palavras do nada e <strong>as</strong><sup>V</sup> dispõe como todo articulado. Este é o primeiro nível humanizador, ao contrário do que geralmente <strong>se</strong><sup>VI</sup> pensa. A organização da palavra comunica-se ao nosso espírito e <strong>o</strong><sup>VII</sup> leva, primeiro, <strong>a</strong><sup>VIII</sup> se organizar; em seguida, a organizar o mundo. Isto ocorre desde <strong>as</strong><sup>IX</sup> formas mais simples, como a quadrinha, o provérbio, a história de bichos, que sintetizam a experiência e a reduzem a sugestão, norma, conselho ou simples espetáculo mental.")
CANDIDO = (chamada("Leia o texto para responder às questões de 51 a 53.")
           + apoio(CANDIDO_TXT)
           + fonte("Antonio Candido, Direito à Literatura. In: <em>Vários Escritos</em>. Rio de Janeiro: Ouro sobre Azul, 2011, 179 p."))
P51 = p("Entre os elementos destacados em negrito no texto, exercem a função de retomar uma informação anteriormente enunciada")

Q = {
1: {"materia": "Raciocínio lógico", "assunto": "Lógica", "tags": ["conectivos lógicos"],
    "enunciado": apoio("<strong>Se a realidade virtual é entendida como a capacidade de criar ambientes que não existem na natureza, então ela foi uma criação do paleolítico</strong>, um exemplo são as pinturas rupestres. Entretanto, por volta de 3 500 a.C., surgiu a forma mais poderosa de realidade virtual: a escrita, que transformava o registro oral em algo concreto, capaz de durar para sempre.")
                 + fonte("<em>Revista Super Interessante</em>, edição 453, julho 2023, p.5. Adaptado.")
                 + p("Ao considerar a frase destacada em negrito no texto, é correto afirmar que o conectivo lógico utilizado"),
    "explicacao": "<p>A frase tem a estrutura “<strong>se</strong> p, <strong>então</strong> q”: a segunda proposição (“ela foi uma criação do paleolítico”) fica subordinada à primeira (“a realidade virtual é entendida como...”). É a operação <strong>condicional</strong>. Alternativa <strong>D</strong>.</p><p>A negação inverte o valor de uma proposição, não opõe duas (A). A conjunção usa “e” (B). A disjunção usa “ou” e admite que as duas ocorram juntas (C). E a bicondicional seria “se, e somente se” (E).</p>"},
2: {"materia": "História", "assunto": "Pré-História", "tags": ["arte rupestre"],
    "enunciado": apoio(*T(2, "A diversidade do registro gráfico rupestre", "políticas e socioculturais."))
                 + fonte("JUSTAMAND, M.; MARTINELLI, S. A.; OLIVEIRA, G. F.; SILVA, S. D. B. “A arte rupestre em perspectiva histórica: uma história escrita nas rochas”. In: <strong>Revista Arqueologia Pública</strong>. Campinas, SP. V. 11, n. 1, p.130-172, julho/2017.")
                 + p("De acordo com o texto, é correto afirmar que"),
    "explicacao": "<p>O texto destaca a “multiplicidade de suas temáticas” e diz que os registros foram feitos “por uma multiplicidade de grupos”, cada um com “seus inúmeros interesses” e complexidades. O significado varia conforme o contexto, a tecnologia e a organização de cada povo. Alternativa <strong>C</strong>.</p><p>O texto fala em diversidade “impressionante”, não em poucos registros (A), nem em um padrão repetitivo (B). Ele menciona alto grau de abstração intelectual (D) e vários grupos, não um único povo (E).</p>"},
3: {"materia": "Biologia", "assunto": "Evolução", "tags": ["arte rupestre", "pré-história"],
    "enunciado": apoio(*T(2, "No Brasil, o Parque Nacional da Serra da Capivara", "cervos, entre outros.", ["Essas pinturas retratavam"]))
                 + url("https://tinyurl.com/yx3cab3y", "21.08.2023")
                 + p("De acordo com o texto, esse importante patrimônio cultural brasileiro auxilia os pesquisadores nos estudos sobre"),
    "explicacao": "<p>O texto diz que as pinturas retratavam “o cotidiano da época, os rituais religiosos” e “representações de danças coletivas, de caças ou de lutas”. Elas ajudam a estudar as <strong>práticas sociais e culturais do ser humano pré-histórico</strong>. Alternativa <strong>C</strong>.</p><p>O Pré-Cambriano é muito anterior ao ser humano, e o texto não fala em comércio de tintas (A). Não há referência a domesticação nem a tração animal (B). As pinturas são anteriores à colonização europeia (D). E dinossauros e seres humanos nunca conviveram (E).</p>"},
4: {"materia": "História", "assunto": "América pré-colombiana", "tags": MULTI + ["astecas", "porcentagem"],
    "enunciado": apoio("O <em>atlatl</em> é um artefato manual asteca que encaixa na parte traseira de uma lança e pode impulsioná-la a uma velocidade de 150 km/h, além de fazê-la gerar uma pressão que chega a 75 kgf/cm<sup>2</sup> em seu alvo. Trata-se de uma estrutura capaz de intensificar o arremesso da lança por seu usuário, tornando-a mais letal que um leão e mais veloz que um guepardo, uma vez que a pressão da mordida de um leão gera 50 kgf/cm<sup>2</sup> e que um guepardo, perseguindo uma presa, chega a 130 km/h.")
                 + fonte("Fonte dos dados: <em>Revista Super Interessante</em>, edição 453, julho 2023, p.5.")
                 + p("Ao ler o texto, é correto afirmar que o <em>atlatl</em> provavelmente poderia ser encontrado em sítios arqueológicos localizados na região do atual ____<strong>I</strong>____, que se situa no hemisfério ____<strong>II</strong>____, dado ser esta a região habitada pela civilização referida no texto, antes da chegada de Cristóvão Colombo ao continente americano em 1492. Além disso, esse artefato intensifica o arremesso da lança por seu usuário em cerca de ____<strong>III</strong>____% no que se refere à ____<strong>IV</strong>____ do felino.",
                     "Assinale a alternativa que completa corretamente os espaços numerados."),
    "alternativas": colunas(["I", "II", "III", "IV"], [["México", "Norte", "15", "velocidade"], ["Peru", "Norte", "15", "velocidade"], ["México", "Sul", "25", "velocidade"], ["Peru", "Sul", "25", "pressão"], ["México", "Norte", "15", "pressão"]]),
    "explicacao": "<p>Os astecas viviam no atual <strong>México</strong>, no hemisfério <strong>Norte</strong>. Na comparação com o felino que vale para o <em>atlatl</em>, o guepardo, a lança vai a 150 km/h contra 130 km/h: 150 ÷ 130 ≈ 1,15, cerca de <strong>15%</strong> a mais de <strong>velocidade</strong>. Alternativa <strong>A</strong>.</p><p>O Peru foi a região dos incas, no hemisfério Sul (B e D). Na pressão, a comparação seria com o leão: 75 ÷ 50 = 1,5, ou 50% a mais, não 15% nem 25% (D e E). E 25% não corresponde a nenhuma das comparações (C).</p>"},
5: {"materia": "Geografia", "assunto": "Cartografia",
    "enunciado": apoio("A prática de traçar mapas é antiga. O mais antigo mapa que representa um Estado, foi produzido na Suméria, em uma pequena tábua de argila. Já os gregos, por volta do século VI a.C. elaboraram mapas decorrentes de navegações e de expedições militares.",
                       "Com o início das Grandes Navegações, a Cartografia ressurge como meio de representação das novas descobertas.",
                       "O processo de representação de uma superfície esférica em uma superfície plana recebe a denominação de projeção cartográfica.",
                       "Cartografia, portanto, é a arte e a ciência de, graficamente, representar uma área geográfica em uma superfície plana.")
                 + url("https://tinyurl.com/45pke5xp", "22.08.2023") + p("Com base no texto, é correto afirmar que"),
    "explicacao": "<p>O texto define projeção cartográfica como “o processo de representação de uma superfície esférica em uma superfície plana”. Alternativa <strong>D</strong>.</p><p>O texto diz que a Cartografia é ao mesmo tempo arte e ciência (A). O sensoriamento remoto (satélites) é recente (B). O mapa mais antigo é sumério, não grego (C e E), e os gregos vêm depois dos sumérios, não antes (E).</p>"},
6: {"materia": "Matemática", "assunto": "Estatística", "tags": ["moda e mediana"],
    "enunciado": LOUVRE + P6, "imagens": LOUVRE_IMG,
    "explicacao": "<p>A <strong>moda</strong> é o valor que mais se repete: 8,5 aparece três vezes (2008, 2009 e 2010). Para a <strong>mediana</strong>, os 16 valores em ordem crescente são 2,7; 2,8; 7,3; 7,7; 8,1; 8,3; 8,5; 8,5; 8,5; 8,6; 8,9; 9,3; 9,3; 9,6; 9,7; 10,2. Com 16 valores, a mediana é a média do 8º e do 9º: (8,5 + 8,5) ÷ 2 = 8,5. Alternativa <strong>C</strong>.</p><p>10,2 é o maior valor, não a moda (D e E). E 8,6 e 9,3 não estão no meio da lista ordenada (A, B e D).</p>"},
7: {"materia": "História", "assunto": "História contemporânea", "tags": MULTI + ["pandemia de covid-19"],
    "enunciado": LOUVRE + p("A análise do gráfico permite notar variações quanto ao número de visitantes ano a ano.", "Em relação ao ano anterior, é correto afirmar que, no ano de"),
    "imagens": LOUVRE_IMG,
    "explicacao": "<p>Em 2020, o número de visitantes caiu de 9,6 para 2,7 milhões: a pandemia de covid-19 fechou o museu por meses e quase parou o turismo internacional. Alternativa <strong>D</strong>.</p><p>Em 2009, o número se manteve em 8,5 milhões (A). Em 2015, houve queda, e o roubo da Monalisa aconteceu em 1911 (B). Em 2019, houve queda, mas o Louvre não pegou fogo; o incêndio foi na catedral de Notre-Dame (C). E quem saiu da União Europeia foi o Reino Unido, não a França (E).</p>"},
8: {"materia": "Inglês", "assunto": "Vocabulário",
    "enunciado": BLOOD + P8,
    "explicacao": "<p><em>Longstanding</em> significa “de longa data”, e <em>finally</em>, “finalmente”: o mistério das Blood Falls, descobertas em 1911 na Antártida, levou muito tempo para ser resolvido. Há uma <strong>longa busca por respostas para as manchas vermelhas</strong> no gelo do Polo Sul. Alternativa <strong>D</strong>.</p><p>O texto não critica os pesquisadores (A) nem demonstra impaciência do autor (C). A Antártida fica no Polo Sul, e o texto não fala de aquecimento global (B). E o mistério foi resolvido, não paralisou a comunidade científica (E).</p>"},
9: {"materia": "Inglês", "assunto": "Coesão e referência", "tags": ["conectivos"],
    "enunciado": p("A expressão <em>due to</em>, em negrito, introduz"), "apoio_de": (8, P8),
    "explicacao": "<p><em>Due to</em> significa “devido a”: “a coloração vermelha é <em>devida ao</em> ferro oxidado”. A expressão introduz a <strong>causa</strong>. Alternativa <strong>A</strong>.</p><p>Obrigação seria <em>must</em> ou <em>have to</em> (B), contestação, <em>however</em> ou <em>but</em> (C), e finalidade, <em>in order to</em> ou <em>so that</em> (E). Determinação não corresponde ao sentido de <em>due to</em> (D).</p>"},
10: {"materia": "Química", "assunto": "Reações químicas", "tags": MULTI + ["oxidação"],
     "enunciado": p("Segundo o texto, o que explica corretamente o aparecimento da coloração vermelho-escura na água é"), "apoio_de": (8, P8),
     "explicacao": "<p>O texto diz que a cor vem do ferro oxidado na salmoura: quando a água salgada que contém ferro entra em contato com o oxigênio, o ferro sofre <strong>oxidação</strong> e fica vermelho, como na ferrugem. Alternativa <strong>C</strong>.</p><p>A hipótese das algas nunca foi comprovada (A e B). A densidade da água não explica a cor (D). E o texto não fala em sangue de animais; o nome Blood Falls (cachoeiras de sangue) vem só da cor (E).</p>"},
11: {"materia": "Raciocínio lógico", "assunto": "Sequências", "tags": ["calendário"],
     "explicacao": "<p>Do dia 3 de janeiro até 15 de abril, num ano bissexto, passam 28 dias (até 31 de janeiro) + 29 (fevereiro) + 31 (março) + 15 (abril) = 103 dias. Como 103 = 7 × 14 + 5, o dia da semana avança 5 posições a partir de quarta-feira: quinta, sexta, sábado, domingo, <strong>segunda-feira</strong>. Alternativa <strong>A</strong>.</p><p>Esquecer que fevereiro tem 29 dias no ano bissexto daria um dia a menos, domingo, que não está entre as alternativas.</p>"},
12: {"materia": "Biologia", "assunto": "Botânica", "tags": MULTI + ["classificação das plantas"],
     "enunciado": p(*T(6, "Ao longo da história da humanidade", "como as plantas frutíferas.", ["Nas Ciências Biológicas", "Na Grécia Antiga", "Na Idade Contemporânea"]))
                  + url("https://tinyurl.com/yc42tmdr", "25.08.2023")
                  + p("Assinale a alternativa que associa, corretamente, as informações contidas no texto aos avanços tecnológicos e aos conhecimentos científicos relativos a cada período histórico mencionado."),
     "explicacao": "<p>Hoje as plantas são classificadas pela morfologia (vasos condutores, sementes, flores e frutos) e pelas <strong>relações evolutivas</strong> entre os grupos, como o texto sugere ao ir dos musgos às plantas frutíferas. Alternativa <strong>E</strong>.</p><p>Os microscópios só surgiram no fim do século XVI (A), genes e ácidos nucleicos foram descobertos nos séculos XIX e XX (B), e a microscopia eletrônica é do século XX (C). E musgos, samambaias e pinheiros não têm flores nem frutos (D).</p>"},
13: {"materia": "Matemática", "assunto": "Geometria espacial", "tags": ["cilindro", "área lateral"],
     "enunciado": MARAJO + P13,
     "explicacao": "<p>A área lateral do cilindro é 2πrh = 2 · 3 · 10 · 30 = 1 800 cm². Cada receita pinta 450 cm², então são 1 800 ÷ 450 = 4 receitas: 120 mL de azeite e 48 g de urucum.</p><p>Custo do azeite: 120 · (60 ÷ 1 000) = R$ 7,20. Custo do urucum: 48 · (2 ÷ 100) = R$ 0,96. Total: <strong>R$ 8,16</strong>. Alternativa <strong>A</strong>.</p><p>R$ 7,20 e R$ 0,96 são só uma das partes (B e E). R$ 4,50 e R$ 1,68 vêm de contas com outras áreas ou outro número de receitas (C e D).</p>"},
14: {"materia": "Matemática", "assunto": "Geometria espacial", "tags": ["cilindro", "semelhança"],
     "enunciado": MARAJO + p("Um artesão quer criar miniaturas proporcionais ao vaso de cerâmica mencionado no texto para vender aos turistas.", "Sabendo que o raio da base da miniatura é de 2 cm, o volume desta, em cm³, será de"),
     "alternativas": alts("30 π.", "24 π.", "18 π.", "12 π.", "6 π."),
     "explicacao": "<p>A miniatura é proporcional: o raio passa de 10 cm para 2 cm, uma razão de 1/5. A altura também se divide por 5: 30 ÷ 5 = 6 cm. O volume é V = πr²h = π · 2² · 6 = <strong>24π cm³</strong>. Alternativa <strong>B</strong>.</p><p>Manter a altura de 30 cm daria 120π, e usar o raio no lugar do raio ao quadrado daria 12π (D). Os outros valores não respeitam a proporção.</p>"},
15: {"materia": "Química", "assunto": "Estrutura atômica", "tags": ["modelo de Bohr"],
     "enunciado": PORTINARI + P15,
     "explicacao": "<p>No modelo de <strong>Bohr</strong>, os elétrons ocupam níveis de energia definidos. Ao receber energia (aqui, dos raios X), o elétron salta para um nível mais alto; ao voltar ao estado fundamental, libera a diferença de energia em forma de luz, com cor característica de cada elemento. Alternativa <strong>E</strong>.</p><p>Demócrito e Leucipo eram filósofos gregos que propuseram o átomo indivisível, sem elétrons (A e B). O modelo de Dalton é uma esfera maciça (C), e o de Thomson, o “pudim de passas”, não tem níveis de energia (D).</p>"},
16: {"materia": "Química", "assunto": "Funções inorgânicas", "tags": ["óxidos"],
     "enunciado": p("Assinale a alternativa que contém a fórmula química correta do composto que confere cor branca à tinta utilizada por Portinari."), "apoio_de": (15, P15),
     "alternativas": alts("ZnO", "OZn", "MnO<sub>2</sub>", "OFe", "ZrO"),
     "explicacao": "<p>O texto diz que o branco vem do <strong>óxido de zinco</strong>. O zinco forma o íon Zn²⁺, e o óxido, O²⁻: a fórmula é ZnO, com o metal escrito antes do oxigênio. Alternativa <strong>A</strong>.</p><p>OZn inverte a ordem dos símbolos (B). MnO₂ é óxido de manganês, e OFe seria óxido de ferro, também com a ordem trocada (C e D). E Zr é o zircônio, não o zinco (E).</p>"},
17: {"materia": "Biologia", "assunto": "Zoologia", "tags": ["artrópodes"],
     "enunciado": p(*T(8, "As teias de seda das aranhas são obras de arte", "estrutural ao corpo dos animais.", ["A seda dessas teias", "Além disso, as aranhas"]), "De acordo com o texto, é correto afirmar que as aranhas"),
     "explicacao": "<p>O texto diz que as aranhas se alimentam de insetos e de outros pequenos animais, “ajudando a controlar a população desses seres”: elas fazem o <strong>controle natural das populações de insetos</strong>. Alternativa <strong>D</strong>.</p><p>As aranhas têm exoesqueleto, não esqueleto interno (A). As fiandeiras produzem seda; o veneno sai das quelíceras (B). A seda é feita de proteínas, e aranhas são carnívoras (C). E o texto destaca que as teias são elásticas e resistentes (E).</p>"},
18: {"materia": "Física", "assunto": "Cinemática", "tags": MULTI + ["ano-luz"],
     "enunciado": TIRA + P18, "imagens": TIRA_IMG,
     "explicacao": "<p>No terceiro quadrinho, a letra fala de uma voz ouvida “alguns anos-luz atrás”, como se o ano-luz medisse tempo. Mas o <strong>ano-luz é uma unidade de distância</strong>: é quanto a luz percorre em um ano. Daí a frustração do personagem. Alternativa <strong>D</strong>.</p><p>Dinossauros e seres humanos não viveram na mesma época, e o Cambriano é anterior aos dois (A e B). O erro é científico, não gramatical (C). E a luz é muito mais rápida que o som; o erro da letra do quarto quadrinho é dizer que o trovão chega antes do raio (E).</p>"},
19: {"materia": "Física", "assunto": "Cinemática", "tags": ["ano-luz", "notação científica"],
     "enunciado": p("A expressão “anos-luz” é utilizada em muitas representações artísticas, de tirinhas a quadros, de músicas a poemas entre outras. Entretanto, qual é, realmente, o valor <u>aproximado</u> de 1 ano-luz?",
                    "Adote: velocidade da luz <strong>c = 3,0 × 10<sup>8</sup> m/s</strong> e <strong>1 ano = 3,2 × 10<sup>7</sup> s</strong>.",
                    "Podemos afirmar que a resposta correta a essa pergunta é, aproximadamente,"),
     "apoio_de": (18, P18),
     "alternativas": alts("1,0 × 10<sup>9</sup> m/s.", "1,1 × 10<sup>11</sup> s.", "2,6 × 10<sup>12</sup> s.", "6,1 × 10<sup>13</sup> m.", "9,6 × 10<sup>15</sup> m."),
     "explicacao": "<p>O ano-luz é a distância percorrida pela luz em um ano: d = c · t = 3,0 × 10⁸ · 3,2 × 10⁷ = <strong>9,6 × 10¹⁵ m</strong>. Alternativa <strong>E</strong>.</p><p>Como é uma distância, a resposta tem de estar em metros: as alternativas em m/s ou em segundos já estão erradas pela unidade (A, B e C). E 6,1 × 10¹³ m não resulta da conta (D).</p>"},
20: {"materia": "Inglês", "assunto": "Interpretação de texto",
     "enunciado": apoio(*T(9, "Graffiti provides a platform for individuals", "may not have one otherwise.", ["In marginalized communities"]))
                  + url("https://tinyurl.com/5ff8bpsu", "24.08.2023", "")
                  + p("De acordo com o texto, a manifestação artística em questão alia"),
     "explicacao": "<p>O texto diz que o grafite é uma forma de se expressar (<em>express themselves</em>, <em>self-expression</em>) e de “criar um sentimento de pertencimento” (<em>create a sense of belonging</em>) à comunidade. Alternativa <strong>A</strong>.</p><p>O texto opõe o grafite às formas tradicionais de comunicação (B), não fala em vandalismo (C), associa o grafite à resistência, não ao conformismo (D), e não menciona o Impressionismo (E).</p>"},
21: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": ["linguagem não verbal"],
     "enunciado": p("Analise a intervenção artística de Banksy.") + "[[fig:1]]"
                  + url("https://tinyurl.com/4z2wpr4u", "24.08.2023", "Original colorido.")
                  + p("A linguagem verbal e a não-verbal denotam que"),
     "imagens": figs(("q21", "Grafite de Banksy num muro: em letras grandes e escorridas, a frase “Follow your dreams” (siga seus sonhos), com uma faixa “Cancelled” (cancelado) colada por cima da palavra “your”. Ao lado, um homem idoso de boné e roupa de trabalho, com um pincel, um balde e rolos de papel nas mãos, olha para cima.")),
     "explicacao": "<p>A frase “Siga seus sonhos” recebeu o carimbo “cancelado”, colado por um trabalhador comum, como um aviso de evento suspenso. A obra critica a ideia de que todos podem seguir seus sonhos: <strong>a busca pelos sonhos deixou de ser uma opção</strong>. Alternativa <strong>C</strong>.</p><p>A obra não fala de imprensa (A) nem de polícia (B). Não culpa os sonhadores pela falta de iniciativa (D). E o “cancelado” é o de um aviso, não o cancelamento nas redes sociais (E).</p>"},
22: {"materia": "Inglês", "assunto": "Interpretação de texto",
     "enunciado": apoio("“The aim of art is to represent not the outward appearance of things, but their inward significance.” ― Aristotle")
                  + url("https://tinyurl.com/mrh8t4wh", "22.08.2023", "")
                  + p("De acordo com a citação do filósofo grego Aristóteles, o objetivo da arte é"),
     "explicacao": "<p>A frase diz que o objetivo da arte é representar “não a aparência exterior das coisas, mas o seu significado interior”: <strong>exprimir a essência das coisas</strong>. Alternativa <strong>E</strong>.</p><p>A, B e C valorizam justamente a aparência física, que a frase rejeita. E a citação não fala de pequenas coisas da natureza (D).</p>"},
23: {"materia": "Português", "assunto": "Interpretação de texto",
     "enunciado": MUNDANO + P23,
     "explicacao": "<p>O mural, pintado com terra e cinzas das florestas, homenageia um ativista indígena que defendia sua terra. A obra dá visibilidade a um povo e chama a atenção para a destruição das florestas: a arte é <strong>espaço de representatividade</strong> e engaja o público em causas socioambientais. Alternativa <strong>E</strong>.</p><p>O grafite é arte urbana contemporânea, não sacra nem barroca (A). O texto não fala de Muralismo nem de Classicismo (B). Terra e cinzas não são matérias-primas descartáveis, e o texto não trata disso (C). E a obra aproxima natureza e cidade, não as distancia (D).</p>"},
24: {"materia": "Português", "assunto": "Classes de palavras", "tags": ["preposições"],
     "enunciado": p("As preposições assumem diferentes sentidos, dependendo do contexto em que são empregadas.",
                    "Isso pode ser observado nas expressões “<strong>com</strong> terra e cinzas”, “<strong>com</strong> outros artistas” e “<strong>em</strong> um paredão”, cujas preposições denotam, respectivamente,"),
     "apoio_de": (23, P23),
     "explicacao": "<p>“Pintado com terra e cinzas” indica o material da pintura (<strong>matéria</strong>). “Junto com outros artistas” indica <strong>companhia</strong>. E “gravada em um paredão” indica <strong>lugar</strong>. Alternativa <strong>D</strong>.</p><p>“Com outros artistas” não expressa conformidade nem comparação (A e B). “Em um paredão” não indica valor, modo, matéria nem origem (A, B, C e E).</p>"},
25: {"materia": "História", "assunto": "Idade Média", "tags": MULTI + ["medicina islâmica"],
     "enunciado": apoio(*T(10, "A medicina ocidental herdou do islã medieval", "a partir da década de 1980."))
                  + url("https://tinyurl.com/2tj5ys2w", "14.09.2023") + p("Segundo o texto,"),
     "explicacao": "<p>O texto diz que a medicina islâmica se baseou no “estudo e no aprofundamento da tradição greco-latina” e foi “pioneira” do movimento das “cidades saudáveis”, que só ganhou expressão global nos anos 1980: ela <strong>retomou os antigos e lançou as bases de uma concepção contemporânea de saúde</strong>. Alternativa <strong>E</strong>.</p><p>Ela aproveitou saberes de outros povos e é vista como pioneira, não como equivocada (A). O texto não fala em remédios baseados na intuição (B), em exames periódicos (C) nem em substâncias dos três reinos (D).</p>"},
26: {"materia": "Matemática", "assunto": "Análise combinatória", "tags": ["princípio multiplicativo"],
     "enunciado": p(*T(11, "A mandala é uma representação circular", "comumente usada como passatempo.")) + "[[fig:1]]"
                  + p("Considere que, para pintar a mandala apresentada, uma pessoa tem, à sua disposição, somente as cores vermelho, azul, verde e amarelo. Cada espaço delimitado entre linhas, nessa mandala, será pintado com uma única cor, entre as disponíveis, e nenhum de seus espaços ficará sem ser colorido.",
                      "Ao fixar a mandala na posição indicada pela figura, assinale a alternativa que apresenta, corretamente, o número total de formas diferentes de pintá-la."),
     "imagens": figs(("q26", "Mandala circular, pendurada por um cordão, com desenho de simetria de seis pontas: no centro, seis pétalas que se encontram num ponto; em volta, anéis de figuras curvas; na borda, uma faixa dividida em arcos. Contando todos os espaços delimitados pelas linhas, são 36.")),
     "alternativas": alts("4<sup>1</sup>", "4<sup>12</sup>", "4<sup>24</sup>", "4<sup>36</sup>", "4<sup>48</sup>"),
     "explicacao": "<p>A mandala tem simetria de seis partes, e cada sexto tem 6 espaços: são 6 × 6 = 36 espaços. Cada espaço pode receber qualquer uma das 4 cores, sem restrição (cores vizinhas podem se repetir). Pelo princípio multiplicativo, são 4 · 4 · ... · 4 (36 vezes) = <strong>4<sup>36</sup></strong> formas. Alternativa <strong>D</strong>.</p><p>4¹ seria pintar a mandala inteira com uma cor só (A). 4¹² e 4²⁴ deixam de contar parte dos espaços, e 4⁴⁸ conta espaços a mais (B, C e E).</p>"},
27: {"materia": "História", "assunto": "Brasil Colônia", "tags": ["barroco mineiro", "Aleijadinho"],
     "enunciado": chamada("Leia o excerto de um texto escrito por Mário de Andrade em 1928.")
                  + apoio(*T(11, "Esse tipo de igreja, fixado imortalmente", "que nem na cantiga nordestina.", ["As igrejas do Aleijadinho"]))
                  + fonte("ANDRADE, M. “O Aleijadinho”. In: MOURA, R. (ed.). <em>Imagens do Aleijadinho</em>. São Paulo: Museu de Arte de São Paulo Assis Chateaubriand (MASP), 2018. p.181-197. Adaptado.")
                  + p("Segundo o texto,"),
     "explicacao": "<p>Mário de Andrade diz que as igrejas refletem “as bases portuguesas da colônia”, mas já se distinguem das “soluções barrocas lusocoloniais” por uma graça e uma delicadeza “eminentemente brasileiras”: uma <strong>adaptação brasileira e original</strong> do estilo trazido da Europa. Alternativa <strong>B</strong>.</p><p>O texto diz que as igrejas <em>não</em> se acomodam ao “belo” de São Pedro e de Reims (A). Elas são “muito lindas”, e a cantiga nordestina é citada como exemplo de afeto, não de aridez (C). O estilo é barroco, não neoclássico, e o texto diz que elas vão além do gosto do tempo (D). E não há referência a incompatibilidade com o cristianismo (E).</p>"},
28: {"materia": "Raciocínio lógico", "assunto": "Lógica", "tags": ["tabelas"],
     "enunciado": p(*T(12, "Não faltam opções de “rolês” na cidade", "apenas uma vez em cada quadro.", ["Suponha que um site"]))
                  + tabela(["Grau de Satisfação", "N.º de “rolês” avaliados"], [["★★★★★", "9"], ["★★★★", "14"], ["★★★", "10"], ["★★", "5"], ["★", "2"]])
                  + tabela(["Custo por pessoa", "N.º de “rolês” avaliados"], [["$$$ (alto)", "3"], ["$$ (mediano)", "16"], ["$ (baixo)", "9"], ["Gratuito", "12"]])
                  + p("Com base nessas informações, é correto afirmar que"),
     "alternativas": alts("pelo menos um “rolê” foi classificado como gratuito, quando se tomam apenas aqueles com 3 ou mais estrelas.",
                          "foram classificados como custo mediano todos os “rolês” com exatamente 4 estrelas.",
                          "nenhum “rolê” é classificado como custo alto, ao considerar unicamente aqueles com 3 ou menos estrelas.",
                          "foram classificados como custo baixo pelo menos dois “rolês” com exatamente 4 estrelas.",
                          "existem “rolês” com exatamente 5 estrelas em todas as quatro categorias de custo por pessoa."),
     "explicacao": "<p>Os “rolês” com 3 ou mais estrelas são 9 + 14 + 10 = 33. Os que não são gratuitos somam 3 + 16 + 9 = 28. Como 33 > 28, mesmo que todos os pagos estivessem entre os de 3 ou mais estrelas, sobrariam pelo menos 5 gratuitos nesse grupo. Alternativa <strong>A</strong>.</p><p>As outras não são <em>necessariamente</em> verdadeiras: os 14 “rolês” de 4 estrelas podem estar distribuídos entre as categorias de custo de muitas formas, então nada obriga que sejam todos de custo mediano (B) nem que dois deles sejam de custo baixo (D). Os 3 de custo alto podem estar entre os de 3 ou menos estrelas (C). E nada garante 5 estrelas nas quatro categorias (E).</p>"},
29: {"materia": "História", "assunto": "Renascimento", "tags": ["Leonardo da Vinci", "antropocentrismo"],
     "enunciado": p("O Homem Vitruviano foi desenhado por Leonardo da Vinci em um de seus diários, conforme a imagem.") + "[[fig:1]]"
                  + p("A imagem é parte de um conjunto de estudos, chamado de Cânone das Proporções por alguns especialistas, e sobre ela é correto afirmar que"),
     "imagens": figs(("q29", "O Homem Vitruviano, de Leonardo da Vinci: desenho a tinta de um homem nu de braços abertos, em duas posições sobrepostas, inscrito ao mesmo tempo em um círculo e em um quadrado. Acima e abaixo do desenho, linhas de anotações manuscritas.")),
     "alternativas": alts("explora a dor, a angústia, a aflição e a tristeza, investigando a universalidade dos sentimentos humanos e antecipando ideias que, posteriormente, seriam exploradas pelas ciências da mente, como a psicologia e a psicanálise.",
                          "apresenta estilo ousado, vanguardista e libertador que combina imagens bizarras, representações ilógicas e conjuntos irreais de composição da imagem com a destreza técnica acadêmica e tradicional.",
                          "representa a emancipação do homem simples, empregando um estilo realista de fácil compreensão, evitando a abstração e o elitismo em favor da acessibilidade, em linguagem simples, para defender os valores do socialismo.",
                          "faz referência ao fazer científico racional e, simultaneamente, indica como, na modernidade, o homem passa a se colocar no centro das medições e do próprio universo, apresentando a ideia do antropocentrismo.",
                          "demonstra aversão aos conceitos de autoridade e de poder, fazendo críticas comportamentais e políticas, expressas em questões que atravessam a realidade social pelo uso de formas, cores e traços em suportes inusitados, como muros e paredes."),
     "explicacao": "<p>O desenho estuda as proporções ideais do corpo humano com base em medidas e figuras geométricas: une arte e ciência e põe o ser humano como medida de todas as coisas, a ideia renascentista do <strong>antropocentrismo</strong>. Alternativa <strong>D</strong>.</p><p>A descreve o Expressionismo, B, o Surrealismo, C, o Realismo socialista, e E, a arte urbana, como o grafite.</p>"},
30: {"materia": "Geografia", "assunto": "Conceitos geográficos", "tags": ["lugar"],
     "enunciado": apoio(*T(13, "A música, como expressão, forma e sentido da Arte", "adquiridas em sua experiência."))
                  + fonte("MARTINS, DANILO H. O diálogo entre a geografia e a arte: aproximações possíveis a partir de um categorial geográfico. <em>Revista Espaço Acadêmico</em>, n.º 192, (maio/2017). p. 98.")
                  + p("Segundo o texto, podemos afirmar corretamente que"),
     "explicacao": "<p>O texto liga a música “ao conceito de Lugar”: as pessoas percebem os sons dos lugares em que vivem a partir das sensações e experiências que têm ali. Lugar é o espaço vivido, carregado de afeto. Alternativa <strong>E</strong>.</p><p>O texto não trata de relações de poder (Território) nem de Região (A e B). E a experiência humana aproxima a música do espaço geográfico, não a afasta (C e D).</p>"},
31: {"materia": "Geografia", "assunto": "População", "tags": ["migração"],
     "enunciado": p("Leia o trecho da canção <em>Fotografia 3x4</em>, composta por Belchior.") + "[[fig:1]]" + p("O trecho da canção retrata a"),
     "imagens": figs(("q31", "Trecho da letra da canção “Fotografia 3x4”, de Belchior, em versos. O eu lírico, um jovem que veio do norte para a cidade grande, lembra o dia da chegada: os pés cansados e feridos da viagem, as lágrimas nos olhos, os guardas que o paravam em cada esquina para examinar seus documentos e estranhavam o nome do lugar de onde ele vinha. Depois, diz que sua história talvez seja igual à de outros jovens que desceram do norte e viveram na rua no sul. Fonte: &lt;https://tinyurl.com/54b3bvc8&gt; Acesso em: 13.08.2023. Adaptado.")),
     "explicacao": "<p>A canção fala de um jovem que deixa o norte (o Nordeste) rumo à cidade grande do sul (o Sudeste), chega cansado, é tratado com desconfiança pelos guardas e acaba vivendo na rua: é a <strong>migração</strong> nordestina para o Sudeste e as <strong>dificuldades dos migrantes</strong>. Alternativa <strong>A</strong>.</p><p>O jovem vai para outra região do Brasil, não para o exterior (B). A migração pendular é a ida e volta diária entre cidades (C). O poeta Fernando Pessoa é citado, mas ninguém volta de Portugal (D). E a transumância é o deslocamento sazonal, ligado ao gado ou às colheitas, não a ida ao Japão (E).</p>"},
32: {"materia": "Física", "assunto": "Ondas", "tags": ["frequência", "som"],
     "enunciado": p(*[it(x, "spalla") for x in T(13, "As notas musicais são uma convenção", "estão representadas no gráfico.", ["Antes de iniciar uma apresentação", "Em uma certa apresentação"])])
                  + p("<strong>Gráfico de Frequência x Período</strong>") + "[[fig:1]]"
                  + p("Assinale a alternativa que apresenta, corretamente, a nota tocada."),
     "imagens": figs(("q32", "Gráfico de frequência (Hz) por período (ms), com cinco pontos ligados por uma curva descendente: Lá, cerca de 440 Hz e 2,3 ms; Sol, cerca de 390 Hz e 2,6 ms; Fá, cerca de 350 Hz e 2,9 ms; Mi, cerca de 330 Hz e 3,0 ms; Ré, cerca de 295 Hz e 3,4 ms.")),
     "alternativas": alts("Ré", "Mi", "Fá", "Sol", "Lá"),
     "explicacao": "<p>A altura de um som depende da frequência: quanto maior a frequência, mais <strong>agudo</strong> é o som. No gráfico, a maior frequência (cerca de 440 Hz, com o menor período) é a do <strong>Lá</strong>. Alternativa <strong>E</strong>.</p><p>Ré tem a menor frequência e é a nota mais grave do gráfico (A). Mi, Fá e Sol têm frequências intermediárias (B, C e D).</p>"},
33: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": ["doenças infecciosas"],
     "enunciado": p("Leia o trecho da canção <em>O Pulso</em>, composta por Arnaldo Antunes, Marcelo Fromer e Tony Bellotto.") + "[[fig:1]]"
                  + p("Sobre as doenças citadas no texto, é correto afirmar que"),
     "imagens": figs(("q33", "Trecho da letra da canção “O Pulso”, em 13 versos numerados. Os versos 1, 2, 7 e 8 repetem um refrão sobre o pulso que ainda pulsa. Os demais versos enumeram doenças e males, de infecções e câncer a sentimentos e transtornos mentais; o verso 13 fala do corpo. Fonte: &lt;https://tinyurl.com/28dn845&gt; Acesso em: 21.08.2023. Adaptado.")),
     "explicacao": "<p>No verso 10, só a toxoplasmose é causada por um micro-organismo parasita (o protozoário <em>Toxoplasma gondii</em>), transmitido por água e alimentos contaminados, como carne malpassada e verduras mal lavadas. O sarampo é causado por vírus e se transmite pelo ar, e a esquizofrenia não é infecciosa. Alternativa <strong>D</strong>.</p><p>No verso 3, só o câncer vem do crescimento desordenado de células; peste bubônica e pneumonia são infecções (A). No verso 4, nenhuma doença é transmitida por picada de inseto (a raiva vem da mordida de mamíferos, e a anemia não é transmissível) (B). No verso 6, a gripe e a faringite passam de pessoa para pessoa (C). E, no verso 11, a coqueluche se transmite por gotículas de saliva (E).</p>"},
34: {"materia": "Raciocínio lógico", "assunto": "Raciocínio espacial", "tags": ["posições em roda"],
     "explicacao": "<p>Numa roda, contando a partir de Gustavo para a esquerda, Letícia é a 6ª: há 5 crianças entre os dois desse lado. Contando para a direita, ela é a 7ª: há 6 crianças entre eles do outro lado. O total é Gustavo + Letícia + 5 + 6 = <strong>13</strong> crianças. Alternativa <strong>C</strong>.</p><p>Um jeito rápido: as duas contagens dão a volta completa na roda, então o total é 6 + 7 = 13. Somar ou tirar Gustavo e Letícia de novo leva a 11, 12, 14 ou 15 (A, B, D e E).</p>"},
35: {"materia": "Geografia", "assunto": "Regionalização do Brasil", "tags": ["cinema"],
     "enunciado": apoio(*[it(x, "Bye Bye Brasil") for x in T(14, "O filme brasileiro Bye Bye Brasil", "até a rodovia Transamazônica.")])
                  + url("https://tinyurl.com/2fyfh49k", "13.08.2023") + p("Com base no texto, é correto afirmar que o filme"),
     "alternativas": alts("revela a intencionalidade da ditadura Varguista no Brasil de levar espetáculos de qualidade para as famílias assentadas ao longo da rodovia Transamazônica, construída na década de 1980.",
                          "conta a história de um grupo de artistas mambembes que transita pela porção setentrional do território brasileiro numa época em que a televisão se massificava no Brasil.",
                          "retrata um período da história brasileira em que os artistas, remunerados pelo Estado, deslocavam-se pela porção meridional do Brasil para proporcionar espetáculos gratuitos à população.",
                          "narra a saga de uma trupe de artistas que resolve encenar espetáculos em todo o trajeto da Bacia do Rio São Francisco, cujo rio principal nasce na Bahia e deságua no rio Amazonas.",
                          "descreve, com bom humor, a viagem de um grupo de comediantes que rouba um caminhão para poder se deslocar pelo interior do Brasil encenando espetáculos circenses."),
     "explicacao": "<p>A trupe é de artistas ambulantes (<strong>mambembes</strong>) que atravessa o Nordeste e o Norte, a porção <strong>setentrional</strong> (norte) do país, fugindo da concorrência da televisão, que se espalhava pelo Brasil. Alternativa <strong>B</strong>.</p><p>A Transamazônica foi construída na década de 1970, na ditadura militar, não na Era Vargas (A). Os artistas não eram pagos pelo Estado, e meridional significa sul (C). O rio São Francisco nasce em Minas Gerais e deságua no oceano Atlântico (D). E o texto não fala em roubo de caminhão (E).</p>"},
36: {"materia": "História", "assunto": "Brasil República", "tags": ["Cinema Novo"],
     "explicacao": "<p>O <strong>Cinema Novo</strong>, de diretores como Glauber Rocha e Nelson Pereira dos Santos, defendia filmes baratos (“uma câmera na mão e uma ideia na cabeça”), com estética nova e crítica social, em oposição ao modelo de Hollywood. Alternativa <strong>D</strong>.</p><p>A Bossa Nova foi um movimento musical (A). A chanchada era a comédia popular, muitas vezes musical, que o Cinema Novo criticava (B). O cinema cantado e o cinema mudo são fases técnicas do começo do século XX (C e E).</p>"},
37: {"materia": "Biologia", "assunto": "Genética", "tags": ["DNA"],
     "enunciado": apoio(*T(15, "Em uma cena do filme Jurassic Park", "causas de morte dos seres humanos.", ["Em um comentário sobre o filme", "Em suas pesquisas, a bióloga", "Essas amostras conservaram-se", "A partir das análises de amostras"]))
                  + url("https://tinyurl.com/2dhr57s7", "21.08.2023") + p("Com base no texto, é correto afirmar que"),
     "explicacao": "<p>O texto diz que o DNA encontrado no “cimento” que as fêmeas dos piolhos usam para colar as lêndeas forneceu informações sobre os hospedeiros: rotas de migração, sexo das múmias e possíveis causas de morte. As análises <strong>permitiram caracterizar os hospedeiros</strong>. Alternativa <strong>D</strong>.</p><p>Segundo a bióloga, não é possível extrair DNA preservado em âmbar (A). Piolhos não transmitem malária, que é transmitida por mosquitos (B). O texto não fala de minerais da mumificação (C) nem de substâncias tóxicas das lêndeas (E).</p>"},
38: {"materia": "História", "assunto": "Antiguidade", "tags": ["Egito Antigo"],
     "explicacao": "<p>Os egípcios acreditavam na vida após a morte e que o corpo precisava ser preservado para o reencontro com a alma. Retirar e tratar os órgãos deu a eles um bom <strong>conhecimento de anatomia</strong>, aproveitado na medicina. Alternativa <strong>C</strong>.</p><p>A mumificação era cara e reservada sobretudo ao faraó e às elites (A). Ela não surgiu por causa de uma epidemia (B), era conduzida por sacerdotes e embalsamadores especializados, não pela família (E), e fazia parte da religião, não era condenada por ela (D).</p>"},
39: {"materia": "Química", "assunto": "Química ambiental", "tags": ["mercúrio", "razão"],
     "enunciado": chamada("Leia o texto para responder às questões 39 e 40.")
                  + apoio(*T(16, "Os indígenas Yanomami desempenham", "em médio e longo prazo.", ["No entanto, a presença", "Porém, para separar", "A análise de amostras"]))
                  + url("https://tinyurl.com/uyypkzjn", "23.08.2023")
                  + p("De acordo com o texto, a quantidade de mercúrio por grama de cabelo encontrada nos indígenas é N vezes a quantidade tolerada pela OMS.", "Assinale a alternativa que contém o correto valor de N."),
     "explicacao": "<p>A concentração encontrada é 25,2 µg ÷ 4,2 g = 6 µg de mercúrio por grama de cabelo. O limite da OMS é 2 µg/g. Então N = 6 ÷ 2 = <strong>3</strong>. Alternativa <strong>C</strong>.</p><p>Comparar os 25,2 µg diretamente com o limite, sem dividir pela massa de cabelo, daria cerca de 12,6, que não está nas alternativas.</p>"},
40: {"materia": "Química", "assunto": "Separação de misturas",
     "enunciado": p("Assinale a alternativa que apresenta o nome correto do processo de separação de misturas empregado para separar pequenas partículas de ouro da areia."),
     "apoio_de": (39, p("De acordo com o texto, a quantidade de mercúrio por grama de cabelo encontrada nos indígenas é N vezes a quantidade tolerada pela OMS.", "Assinale a alternativa que contém o correto valor de N.")),
     "explicacao": "<p>Na bateia, a água corrente arrasta a areia, mais leve, e o ouro, muito mais denso, fica no fundo. Separar sólidos de densidades diferentes com uma corrente de água é a <strong>levigação</strong>. Alternativa <strong>A</strong>.</p><p>A dissolução fracionada usa um solvente que dissolve só um dos componentes (B). A sublimação é uma mudança de estado físico (C). A decantação separa por repouso, sem corrente de água (D). E a filtração separa sólidos de líquidos por um filtro (E).</p>"},
41: {"materia": "Física", "assunto": "Energia", "tags": ["potência", "consumo de energia elétrica"],
     "enunciado": chamada("Leia o texto para responder às questões 41 e 42.")
                  + apoio("<strong>NFT X Sustentabilidade</strong>",
                          *[it(x, "Non-Fungible Token", "blockchain") for x in T(17, "Bens não fungíveis são aqueles", "ao redor desses rios.", ["NFT (Non-Fungible Token", "Apesar do avanço", "Para manter essas operações"])])
                  + p("De acordo com as informações apresentadas no texto, podemos afirmar corretamente que"),
     "trocar": [("120×109 kWh", "120 × 10<sup>9</sup> kWh")],
     "explicacao": "<p>Consumir 50 kWh de energia em 1 hora corresponde a uma potência de P = E ÷ t = 50 kWh ÷ 1 h = 50 kW = <strong>50 000 W</strong>. Alternativa <strong>E</strong>.</p><p>A “mineração de dados” é o processamento dos computadores, não a extração de minérios (A). A NFT envolve criptografia e computação, não só eletrônica quântica (B). A Argentina consome 120 × 10⁹ kWh, ou 120 bilhões, não 120 milhões (C). E o texto diz que o consumo do <em>blockchain</em> pode ser até maior que o da Argentina (D).</p>"},
42: {"materia": "Química", "assunto": "Soluções", "tags": ["solubilidade de gases"],
     "enunciado": p("O problema gerado pela liberação da água quente nos rios e nos oceanos é a alteração na quantidade de oxigênio dissolvido na água, uma vez que a solubilidade do oxigênio na água é inversamente proporcional à temperatura.",
                    "Diante disso, assinale a alternativa que apresenta corretamente o esboço do gráfico que mostra a solubilidade do oxigênio na água (mg/L) em função da temperatura (<sup>o</sup>C)."),
     "apoio_de": (41, p("De acordo com as informações apresentadas no texto, podemos afirmar corretamente que")),
     "imagens": figs(("q42a", "Gráfico A: solubilidade de O₂ (mg/L) por temperatura (°C), uma reta que sobe."),
                     ("q42b", "Gráfico B: a curva sobe até um máximo e depois desce."),
                     ("q42c", "Gráfico C: a curva desce até um mínimo e depois sobe."),
                     ("q42d", "Gráfico D: a curva desce rapidamente no começo e depois cada vez mais devagar, como uma hipérbole."),
                     ("q42e", "Gráfico E: uma reta horizontal, a solubilidade não muda com a temperatura.")),
     "alternativas": {"A": "[[fig:1]]", "B": "[[fig:2]]", "C": "[[fig:3]]", "D": "[[fig:4]]", "E": "[[fig:5]]"},
     "explicacao": "<p>Se a solubilidade é inversamente proporcional à temperatura, quando uma aumenta a outra diminui, numa curva que desce cada vez mais devagar, como a de y = k/x. É o gráfico D. Alternativa <strong>D</strong>.</p><p>A mostra a solubilidade aumentando com a temperatura. B e C mudam de sentido no meio do caminho, e E mostra a solubilidade constante. Nenhuma delas é uma relação inversa.</p>"},
43: {"materia": "Biologia", "assunto": "Fisiologia humana", "tags": ["digestão", "enzimas"],
     "enunciado": p(*T(18, "As Ciências e a Tecnologia têm um papel", "em agitação constante.", ["Com o objetivo de estudar", "Em cada um desses tubos", "Os tubos foram tampados"]))
                  + p("Tubo 1: carne + solução aquosa de HCℓ 3,5 % + pepsina.", "Tubo 2: carne + suco gástrico.", "Tubo 3: carne + suco pancreático.", "Tubo 4: carne + suco gástrico fervido.")
                  + p("Após o tempo necessário para a digestão enzimática da carne, fragmentos menores de proteínas dessa carne podem ser encontrados"),
     "trocar": [("37 o C", "37 °C")],
     "explicacao": "<p>A pepsina digere proteínas em meio ácido: está no tubo 1 (com HCℓ) e no suco gástrico do tubo 2. O suco pancreático do tubo 3 tem tripsina, que também digere proteínas. No tubo 4, a fervura desnaturou as enzimas do suco gástrico, que deixaram de funcionar. Há digestão <strong>apenas nos tubos 1, 2 e 3</strong>. Alternativa <strong>D</strong>.</p><p>O tubo 4 não tem enzimas ativas (A, B e E). E o tubo 3 também digere proteínas (C).</p>"},
44: {"materia": "Raciocínio lógico", "assunto": "Lógica", "tags": ["dedução"],
     "enunciado": p(*T(18, "O futebol pode ser visto como uma arte", "sendo 2 delas zagueiras e 2 atacantes.", ["Suponha que um técnico"]))
                  + tabela(["1º Amistoso", "2º Amistoso", "3º Amistoso"], [["Lúcia", "Sônia", "Maria"], ["Carol", "Carol", "Lúcia"], ["Maria", "Maria", "Alice"], ["Alice", "Francisca", "Sônia"]])
                  + p("Sabendo que Francisca é atacante, é necessariamente correto afirmar que"),
     "explicacao": "<p>O 1º e o 3º amistosos têm em comum Lúcia, Maria e Alice; o 1º tem ainda Carol, e o 3º, Sônia. Como cada jogo tem exatamente 2 zagueiras, Carol e Sônia precisam ter a mesma posição. No 2º amistoso (Sônia, Carol, Maria e Francisca), Francisca é atacante, então só falta uma atacante. Se Carol e Sônia fossem atacantes, seriam três: impossível. Logo, Carol e Sônia são zagueiras, e Maria é atacante. Alternativa <strong>B</strong>.</p><p>Maria é atacante, não zagueira (C), e Sônia é zagueira, não atacante (E). Já Alice e Lúcia ficam indefinidas: uma é zagueira e a outra atacante, mas não dá para saber qual (A e D).</p>"},
45: {"materia": "Física", "assunto": "Energia", "tags": ["conservação de energia"],
     "explicacao": "<p>No ponto de deflexão máxima, a corda está esticada ao máximo (<strong>energia potencial elástica máxima</strong>) e o artista para por um instante antes de voltar a subir (velocidade nula, <strong>energia cinética mínima</strong>). Alternativa <strong>D</strong>.</p><p>Há energia potencial, elástica e gravitacional (A, B e E). E as energias cinética e elástica não podem ser máximas ao mesmo tempo: uma se transforma na outra (C).</p>"},
46: {"materia": "Física", "assunto": "Movimento circular", "tags": ["velocidade angular"],
     "explicacao": "<p>O <em>fouetté</em> é uma rotação em torno do eixo do corpo. Para quem observa de fora, o que caracteriza e mantém esse giro é a <strong>velocidade angular</strong>, o quanto o corpo gira por unidade de tempo. A perna que abre e fecha ajuda a controlar essa velocidade. Alternativa <strong>D</strong>.</p><p>Massa é uma grandeza escalar, não vetorial (A). A força centrífuga só aparece para quem gira junto com a bailarina, não para um observador externo (B). A perna não é uma mola, e a força elástica não mantém o giro (C). E a temperatura não tem relação com a rotação (E).</p>"},
47: {"materia": "Matemática", "assunto": "Funções", "tags": ["função do 2º grau"],
     "enunciado": p("<em>Emojis</em> são elementos visuais que representam conceitos, emoções e objetos em forma de ícones e estão intrinsecamente ligados à cultura digital por facilitarem a comunicação on-line.",
                    "Equações matemáticas podem ser utilizadas para modelar fenômenos e situações.",
                    "Na imagem, o plano cartesiano ilustra o uso de 4 curvas para modelar um <em>emoji</em>. Por exemplo, a curva 2 (<em>c</em>2) é descrita pela função y = x<sup>2</sup> – 8x + 18, definida no intervalo real [2 ; 6].")
                  + "[[fig:1]]" + p("Assinale a alternativa que apresenta, corretamente, a função correspondente à curva 4 (<em>c</em>4) e o intervalo real no qual ela deve ser definida."),
     "imagens": figs(("q47", "Plano cartesiano com um rosto sorridente formado por 4 curvas. c1: circunferência de centro na origem e raio 10. c3: circunferência pequena de centro (–4, 4) e raio 2, o olho esquerdo. c2: parábola voltada para cima com vértice em (4, 2), de x = 2 a x = 6, onde y = 6, o olho direito piscando. c4: parábola voltada para cima com vértice em (0, –8), de x = –4 a x = 4, onde y = –4, a boca.")),
     "alternativas": colunas(["Função", "Intervalo"], [["\\(y = \\dfrac{x^2}{4} - 8\\)", "[–4 ; 4]"], ["\\(y = \\dfrac{x^2}{2} - 8\\)", "[–4 ; 4]"], ["\\(y = \\dfrac{x^2}{4} - 8\\)", "[–6 ; –4]"], ["\\(y = \\dfrac{x^2}{2} - 8\\)", "[–6 ; –4]"], ["\\(y = \\dfrac{x^2}{4} - 8\\)", "[–4 ; 6]"]]),
     "explicacao": "<p>A curva c4 é uma parábola com vértice em (0, –8), então y = ax² – 8. Ela passa por (4, –4): –4 = a · 16 – 8, ou seja, 16a = 4 e a = 1/4. A função é \\(y = \\dfrac{x^2}{4} - 8\\), e a curva vai de x = –4 a x = 4. Alternativa <strong>A</strong>.</p><p>Com x²/2, em x = 4 teríamos y = 0, fora do desenho (B e D). E os intervalos [–6 ; –4] e [–4 ; 6] não correspondem às pontas da boca (C, D e E).</p>"},
48: {"materia": "História", "assunto": "Brasil República", "tags": MULTI + ["Guerra de Canudos"],
     "enunciado": CANUDOS + p("Com base nos textos, é correto afirmar que essa guerra ocorreu durante o"),
     "explicacao": "<p>A Guerra de Canudos (1896–1897) aconteceu no início da <strong>República</strong>, proclamada em 1889. Euclides da Cunha escreve que Canudos “não se rendeu” e resistiu até o último defensor, e o primeiro texto fala em cerca de 25 mil mortos, gente pobre que fugia da seca, da fome e da falta de terras. Alternativa <strong>E</strong>.</p><p>Em 1896 o Brasil já não era um Império (A, B e C). E Dom Pedro II já tinha sido deposto, além de o exército só ter vencido na quarta tentativa (D).</p>"},
49: {"materia": "Física", "assunto": "Cinemática", "tags": MULTI + ["lançamento oblíquo"],
     "enunciado": CANUDOS + p(*T(20, "“A Matadeira” era o apelido", "estava posicionada a aproximadamente", ["Nas mesmas condições", "Desprezando quaisquer forças"])),
     "explicacao": "<p>A questão espera que se use a velocidade horizontal do tiro, que é constante sem resistência do ar: 3 800 m em 10 s dão 380 m/s. Em 0,5 s, a bala avança 380 · 0,5 = <strong>190 m</strong>. Alternativa <strong>A</strong>.</p><p>380 m seria o deslocamento em 1 s (B), e 760 m, em 2 s (C). 1,6 km e 3,8 km correspondem a tempos ainda maiores (D e E).</p><p>Observação do Treineiros: a rigor, com o mesmo ângulo e a mesma velocidade de lançamento, o tempo de voo seria sempre o mesmo, e a bala só poderia cair em 0,5 s se fosse disparada de outro jeito. A banca considerou apenas o movimento horizontal uniforme.</p>"},
50: {"materia": "Geografia", "assunto": "Climatologia", "tags": ["semiárido", "Caatinga"],
     "enunciado": apoio("“Sabe o senhor: sertão é onde o pensamento da gente se forma mais forte do que o poder do lugar”.")
                  + fonte("ROSA, Guimarães. <em>Grande Sertão: veredas</em>. 12ª edição. São Paulo: Livraria J. Olímpio Editora, 1978. 22p.")
                  + p("Para a Geografia, o Sertão também é o nome de uma sub-região do Nordeste brasileiro onde predomina o clima"),
     "explicacao": "<p>O Sertão tem clima <strong>semiárido</strong>, quente, com chuvas escassas e irregulares. A vegetação é a Caatinga, com plantas <strong>xeromórficas</strong>, adaptadas à seca: folhas pequenas ou transformadas em espinhos, caules que armazenam água e raízes profundas. Alternativa <strong>E</strong>.</p><p>O clima não é subtropical, e plantas halófitas vivem em solos salinos, como os mangues (A). Não há deserto no Brasil (B e C). E plantas ombrófilas são as de florestas úmidas, como a Amazônica (D).</p>"},
51: {"materia": "Português", "assunto": "Coesão e referência", "tags": ["anáfora"],
     "enunciado": CANDIDO + P51,
     "explicacao": "<p>Retomam algo já dito: <strong>III</strong>, o pronome relativo “que”, retoma “um fator”; <strong>IV</strong>, “Por isso”, retoma a ideia do parágrafo anterior; <strong>V</strong>, “as”, retoma “as palavras”; e <strong>VII</strong>, “o”, retoma “nosso espírito”. Alternativa <strong>D</strong>.</p><p>I (“Se”) introduz uma condição, II (“que”) é conjunção integrante, VI (“se”) é índice de indeterminação, VIII (“a”) é preposição e IX (“as”) é artigo. Nenhum deles retoma informação, e todas as outras alternativas incluem algum desses (A, B, C e E).</p>"},
52: {"materia": "Português", "assunto": "Sintaxe", "tags": ["período composto"],
     "enunciado": p("Analisando a estrutura do texto, pode-se afirmar corretamente que há,"), "apoio_de": (51, P51),
     "explicacao": "<p>O segundo parágrafo tem cinco períodos (cinco frases terminadas em ponto). O segundo deles, “A produção literária tira as palavras do nada e as dispõe como todo articulado”, tem duas orações ligadas por “e”: a segunda é uma <strong>coordenada sindética aditiva</strong>. Alternativa <strong>E</strong>.</p><p>O primeiro parágrafo tem dois períodos, não quatro nem três (A e B), e o primeiro período começa com uma oração condicional (“Se fosse possível...”), não concessiva (C). E o segundo parágrafo tem cinco períodos, não quatro (D).</p>"},
53: {"materia": "Português", "assunto": "Interpretação de texto",
     "enunciado": p("Com base nas informações apresentadas no texto, pode-se inferir corretamente que"), "apoio_de": (51, P51),
     "explicacao": "<p>Para Candido, a organização da obra literária “nos deixa mais capazes de ordenar a nossa própria mente e sentimentos” e “de organizar a visão que temos do mundo”: a leitura <strong>torna a pessoa mais apta a entender sua realidade</strong>. Alternativa <strong>B</strong>.</p><p>O texto não diz que a linguagem é fixa nem que impõe uma visão única (A). Ele cita formas simples, como a quadrinha e o provérbio, como capazes de organizar a experiência (C). Não fala da formação da sociedade (D). E diz que a palavra organiza primeiro o próprio leitor e depois o mundo, não o outro antes de si (E).</p>"},
54: {"materia": "Português", "assunto": "Figuras de linguagem", "tags": MULTI + ["hipérbole"],
     "enunciado": p("Analise a tirinha de <em>Calvin e Haroldo</em> (<em>Calvin and Hobbes</em>) do cartunista Bill Watterson.") + "[[fig:1]]"
                  + url("https://tinyurl.com/3zew9e7x", "22.08.2023", "") + p("O tigre aconselha o menino a"),
     "imagens": figs(("q54", "Tirinha de Calvin e Haroldo, em inglês, em três quadrinhos. No primeiro, Calvin chega em casa e diz que teve um dia tão ruim que se sente como se tivesse sido atropelado por um trem. No segundo, o tigre Haroldo pula sobre ele com um grande “KAPOW!”, e os dois rolam pelo chão. No terceiro, Calvin, caído e tonto, diz que agora, sim, se sente assim; Haroldo, sorrindo, responde que ele deveria sempre guardar a hipérbole para quando realmente precisasse dela.")),
     "explicacao": "<p>Calvin exagera ao dizer que se sente atropelado por um trem. Depois que Haroldo o derruba, ele passa a se sentir assim de verdade, e o tigre o aconselha a guardar a hipérbole para quando realmente precisar: <strong>poupar a figura de linguagem para o momento adequado</strong>. Alternativa <strong>C</strong>.</p><p>Haroldo não fala em compaixão do ouvinte (A) nem em mascarar o sentido (B). A hipérbole é um recurso conotativo, não denotativo (D). E o conselho é usá-la na hora certa, não sempre (E).</p>"},
}
completar(Q, R)
