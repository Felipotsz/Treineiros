# Ajustes da conferência humana: Vestibulinho ETEC 2º semestre de 2019 (exame de 16/06/2019)
# Texto conferido com a imagem de cada página; trechos longos copiados do texto do PDF com trecho().
# Gabarito: oficial (2º SEM/19). Tema: biodiversidade.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import A, carregar, enun, tabela, colunas, completar, trecho

ID = "etec-2019-2sem"
META = {
    "id": ID,
    "banca": "ETEC",
    "ano": 2019,
    "semestre": 2,
    "titulo": "Vestibulinho ETEC, 2º semestre de 2019",
    "fonte": "Centro Paula Souza",
    "dataExame": "2019-06-16",
    "duracaoMinutos": 240,
    "tema": "Biodiversidade",
    "apresentacao": "<p>Prezado(a) candidato(a), a partir da Eco-92, a conservação da biodiversidade passou a ser um assunto constante nos jornais, revistas e TV. Biodiversidade é um conceito que se refere à variedade de espécies que coexistem em um ecossistema, participando de complexas interações ecológicas e dos ciclos da matéria desse ecossistema.</p><p>Boa prova!</p>",
    "pdf": f"assets/provas/{ID}.pdf",
}
EXTRAS = {"apresentacao": "Ilustração em tons de cinza de um globo terrestre cercado por pequenos ícones de seres vivos, plantas, objetos e atividades humanas, sugerindo a variedade de vida e suas relações."}

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
    """Põe em itálico termos que o texto do PDF perdeu (nomes científicos, estrangeirismos)."""
    for t in termos: texto = texto.replace(t, f"<em>{t}</em>")
    return texto


# ---------- textos compartilhados ----------
PECA = (chamada("Leia e analise a peça publicitária para responder às questões 01 e 02.")
        + "[[fig:1]]" + url("https://tinyurl.com/y5sxnz6h", "07.02.2019", "Original colorido."))
PECA_IMG = {"arquivo": "q01", "alt": "Cartaz da “Campanha do Meio Ambiente” da Prefeitura de Xaxim e do Comdema. Uma mão segura um galho fino, dobrado em ângulo, de cuja ponta brotam folhas novas. No alto, o texto: “Você está no meio desse ambiente. E não no fim.”, com “Meio” e “Ambiente” em letras grandes e cursivas. No rodapé, o brasão e os contatos da prefeitura."}
P1 = (p("Observe os períodos:")
      + p("<strong>I.</strong> Você está no meio desse ambiente.", "<strong>II.</strong> Campanha do meio ambiente.")
      + p("Sobre o vocábulo “meio”, destacado nos períodos, pode-se afirmar corretamente que:"))

QUIMICA_VERDE = (chamada("Leia os textos para responder às questões de 06 a 08.")
                 + apoio(*T(4, "A Química Verde (ou Sustentável) pode", "a toda biodiversidade.", ["Garantir a qualidade"]),
                         "Conheça os dez princípios básicos da Química Verde (ou Sustentável):")
                 + p("<strong>1.</strong> Minimizar a produção de resíduos.",
                     "<strong>2.</strong> Estimular a produção de materiais menos perigosos.",
                     "<strong>3.</strong> Reservar verbas para projetos de produtos seguros.",
                     "<strong>4.</strong> Utilizar solventes e auxiliares mais seguros.",
                     "<strong>5.</strong> Buscar eficiência energética.",
                     "<strong>6.</strong> Maximizar o uso de fontes renováveis.",
                     "<strong>7.</strong> Erradicar ou minimizar a formação de derivados.",
                     "<strong>8.</strong> Utilizar materiais que se degradem com facilidade.",
                     "<strong>9.</strong> Analisar em tempo real a prevenção da poluição.",
                     "<strong>10.</strong> Utilizar a química segura que auxilie na prevenção de acidentes químicos.", classe="apoio")
                 + fonte("&lt;tinyurl.com/y627vear&gt; Acesso em: 06.02.2019. Adaptado.")
                 + apoio(*T(4, "Uma rede mundial de lanchonetes", "nós somos parte dele!", ["Infelizmente o uso", "Por esse motivo"]),
                         "Para minimizar esse problema, uma empresa passou a confeccionar canudinhos de bambu, com o seguinte slogan:",
                         "“CANUDOS REUTILIZÁVEIS DE BAMBU – MENOS LIXO NO SEU DIA A DIA”")
                 + url("https://tinyurl.com/y3tqneyy", "07.02.2019"))
P6 = p("Os canudos reutilizáveis enquadram-se no princípio de número")

MINERACAO = (chamada("Leia o texto para responder às questões 12 e 13.")
             + apoio(*T(7, "A mineração, apesar de ser", "do espaço geográfico.", ["Os danos causados", "Além disso, há problemas"])))
P12 = p("Do ponto de vista econômico, social e ambiental, para minimizar a possibilidade de catástrofes ambientais, como a mencionada no texto, é adequado")

POVOS = (chamada("Leia o texto <em>Povos da Megadiversidade</em> para responder às questões de 15 a 18.")
         + apoio(*T(9, "Os conhecimentos e práticas dos povos", "Eles são, de fato, colecionadores.",
                    ["A arqueologia brasileira", "Os povos indígenas e as comunidades", "Foi a falta de diversidade", "As plantas e seus inimigos", "Povos indígenas e comunidades tradicionais mantêm"]))
         + url("https://tinyurl.com/ybyw32gw", "08.02.2019"))
P15 = p("De acordo com pesquisas arqueológicas, atribui-se às ações das populações indígenas")

HOTSPOTS = (chamada("Leia o texto para responder às questões de números 20 a 22.")
            + apoio(*[it(x, "hotspots", "hotspot") for x in T(11, "Não se sabe quantas espécies", "sua vegetação original preservada.", ["Em 1988, o ecologista"])])
            + url("https://tinyurl.com/yaofqe8z", "10.02.2019"))
P20 = (p("Observe a reta real:") + "[[fig:1]]"
       + p("De acordo com o texto, a porcentagem que se refere ao número de espécies identificadas pelos cientistas, até agora, é melhor representada, na reta real, pelo ponto"))
RETA_IMG = {"arquivo": "q20", "alt": "Reta real graduada de 0 a 20, com marcas de 1 em 1. Pontos destacados: P, quase sobre o 0 (cerca de 0,1); Q, perto de 4,5; T, sobre o 10; X, perto de 12,5; Y, perto de 18."}

CARTUM = (chamada("Analise o cartum para responder às questões 23 e 24.")
          + "[[fig:1]]" + fonte("Dan Piraro. Disponível em: &lt;https://tinyurl.com/y4uuwpx8&gt; Acesso em: 07.02.2019. Original colorido."))
CARTUM_IMG = {"arquivo": "q23", "alt": "Cartum “Bizarro”, de Dan Piraro, sem falas. Paródia da imagem clássica da evolução: da água de uma praia saem um peixe, uma foca, um macaco de quatro, macacos cada vez mais eretos e um homem andando. No fim da fila, um homem moderno, de calção, despeja um balde de lixo justamente na água de onde a fila começou."}
P23 = p("Após a leitura do cartum, pode-se concluir corretamente que ele")

# ---------- questões ----------
Q = {
1: {"materia": "Português", "assunto": "Classes de palavras",
    "enunciado": PECA + P1, "imagens": [PECA_IMG],
    "alternativas": {"A": "em I, exerce a função de predicativo do sujeito “você”.",
                     "B": "em I, é substantivo que forma uma locução adverbial indicando lugar.",
                     "C": "em II, está apresentando a circunstância de lugar onde a campanha ocorre.",
                     "D": "em II, é um advérbio de intensidade e pode ser substituído por “um pouco”.",
                     "E": "em I e II, são substantivos que formam locuções adjetivas qualificando “você” e “campanha”."},
    "explicacao": "<p>Em I, “meio” é substantivo (vem com o artigo: “n<strong>o</strong> meio”) e forma a locução adverbial “no meio desse ambiente”, que indica <strong>lugar</strong> (onde você está). Alternativa <strong>B</strong>.</p><p>O predicativo de “você” é a própria locução de lugar, não “meio” sozinho (A). Em II, “meio ambiente” é um substantivo composto, e “do meio ambiente” é locução adjetiva que qualifica “campanha”, sem ideia de lugar (C) nem de intensidade (D). E em I a locução é adverbial, não adjetiva (E).</p>"},
2: {"materia": "Português", "assunto": "Figuras de linguagem",
    "enunciado": p("No slogan da peça publicitária, “Você está no meio desse ambiente. E não no fim.”, o segundo período é construído utilizando a zeugma. Trata-se de figura de sintaxe baseada na omissão de um termo já empregado anteriormente no texto, no caso, o verbo estar: “E não [<strong>está</strong>] no fim”.",
                   "Assinale a alternativa em que a citação apresentada também se constrói por meio da zeugma."),
    "apoio_de": (1, P1),
    "alternativas": {"A": "“Seu rosto imóvel logrou / uma expressão que ninguém / chegou perto de imitar: / cômica e séria...” (Felipe Fortuna)",
                     "B": "“Como era dia de bacalhau, vovó mandou abrir três garrafas de vinho do Porto para o jantar.” (Helena Morley)",
                     "C": "“Perante a morte empalidece e treme, / treme perante a Morte, empalidece.” (Cruz e Sousa)",
                     "D": "“Vês?! Ninguém assistiu ao formidável / Enterro de tua última quimera.” (Augusto dos Anjos)",
                     "E": "“Viu uma lua no céu / Viu outra lua no mar.” (Alphonsus Guimarães)"},
    "explicacao": "<p>Em A, depois dos dois-pontos fica subentendido um termo já usado: “[uma expressão] cômica e séria”. As qualidades se apoiam no termo anterior sem repeti-lo: é a construção por <strong>omissão de um termo já empregado</strong>, como no slogan. Alternativa <strong>A</strong>.</p><p>B é uma frase completa, sem termo omitido. C repete os mesmos verbos em ordem inversa (quiasmo), em vez de omiti-los. D não omite nada. E repete o verbo “viu” no início dos versos (anáfora), em vez de omiti-lo.</p>"},
3: {"materia": "Química", "assunto": "Reações químicas", "tags": ["estequiometria", "fotossíntese"],
    "enunciado": apoio(*T(3, "O ano de 2010 foi o Ano", "com ênfase para as oxidações.", ["A vida na Terra"]))
                 + url("https://tinyurl.com/y6qvrjjy", "05.02.2019")
                 + p("A incorporação do gás carbônico (CO<sub>2</sub>), na fotossíntese representada, é um exemplo, onde as substâncias interagem numa proporção constante.")
                 + apoio("6 CO<sub>2</sub> + 6 H<sub>2</sub>O → C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> + 6 O<sub>2</sub>")
                 + tabela(["Substância", "CO<sub>2</sub>", "H<sub>2</sub>O", "C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>", "O<sub>2</sub>"], [["Massa indicada", "44 g", "18 g", "30 g", "32 g"]])
                 + p("De acordo com essa proporção e admitindo rendimento de 100 %, se uma planta absorver 66 g de CO<sub>2</sub>, a quantidade de glicose (C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>) produzida, em gramas, será"),
    "explicacao": "<p>Pela equação, 6 mol de CO<sub>2</sub> (6 × 44 = 264 g) formam 1 mol de glicose. A massa molar da glicose é 6 × 12 + 12 × 1 + 6 × 16 = 180 g (o “30 g” do quadro corresponde a cada uma das seis unidades CH<sub>2</sub>O: 6 × 30 = 180 g).</p><p>Então: 264 g de CO<sub>2</sub> → 180 g de glicose; 66 g de CO<sub>2</sub> → x. Como 66 é a quarta parte de 264, x = 180 ÷ 4 = <strong>45 g</strong>. Alternativa <strong>E</strong>.</p>"},
4: {"materia": "História", "assunto": "Escravidão", "tags": ["África"],
    "enunciado": apoio(*T(3, "Segunda maior floresta tropical do mundo", "ali vivem há séculos."))
                 + p("Sobre a região, é correto afirmar que ela"),
    "explicacao": "<p>A região do Congo e de Angola, de povos de línguas banto, foi a origem da <strong>maior parte dos africanos escravizados</strong> trazidos para a América do Sul, sobretudo para o Brasil. Alternativa <strong>E</strong>.</p><p>A colonização europeia da África Central é bem posterior ao século XIII e não foi feita por britânicos e espanhóis ali (A). As independências vieram no século XX (B). O texto não fala de migrações islâmicas, e o século II é anterior ao Islã (C). E o alto Nilo fica em outra região da África (D).</p>"},
5: {"materia": "Física", "assunto": "Ondas",
    "enunciado": p("Os morcegos não enxergam muito bem, entretanto, são mamíferos capazes de ouvir sons cujas frequências vão de 1 000 Hz a 120 000 Hz.",
                   "O maior comprimento de onda das ondas sonoras audíveis por morcegos é de")
                 + apoio("Lembre-se de que v = λ · f, em que:", "• v é a velocidade de propagação do som no ar, de valor 340 m/s;", "• λ é o comprimento de onda, em m;", "• f é a frequência da onda, em Hz."),
    "explicacao": "<p>Como λ = v ÷ f, o maior comprimento de onda corresponde à <strong>menor frequência</strong>: 1 000 Hz. Então λ = 340 ÷ 1 000 = <strong>0,34 m</strong>. Alternativa <strong>B</strong>.</p><p>Com a maior frequência (120 000 Hz), λ ≈ 0,003 m, que é o menor comprimento de onda. Os outros valores vêm de contas invertidas ou de erros de vírgula.</p>"},
6: {"materia": "Química", "assunto": "Química ambiental", "tags": ["química verde"],
    "enunciado": QUIMICA_VERDE + P6,
    "explicacao": "<p>O canudo de bambu é feito de uma <strong>matéria-prima renovável</strong> (o bambu cresce de novo), o que corresponde ao princípio 6: “Maximizar o uso de fontes renováveis”. Alternativa <strong>B</strong>.</p><p>A decomposição de qualquer material gera compostos químicos (A). Bambu não é solvente (C). O plástico é justamente o material que se quer evitar (D). E o canudo não tem relação com acidentes químicos (E).</p>"},
7: {"materia": "Química", "assunto": "Química ambiental", "tags": ["química verde"],
    "enunciado": p("As reações representadas são duas rotas de síntese distintas para o mesmo fim.") + "[[fig:1]]"
                 + apoio(*T(5, "Na reação “X”, apenas 25%", "preservando a biodiversidade."))
                 + url("http://tinyurl.com/y62uv26k", "06.02.2019", "Adaptado. Original colorido.")
                 + p("Três dos princípios básicos da Química Verde, nos quais o processo “verde” descrito no texto se enquadra, são"),
    "apoio_de": (6, P6),
    "imagens": [{"arquivo": "q07", "alt": "Duas reações representadas com modelos de bolas. Reação X: metiletileno + água + cloro, com Ca(OH)2, formam óxido de propileno + água + cloreto de cálcio (um íon 2+ e dois íons −); utilização atômica: 25%. Reação Y: metiletileno + água oxigenada formam óxido de propileno + água; utilização atômica: 76%."}],
    "explicacao": "<p>O texto dá três razões para a reação Y ser mais “verde”: gera só água como subproduto, aproveitando 76% da massa (princípio 1, <strong>minimizar resíduos</strong>); usa peróxido de hidrogênio, menos nocivo que o cloro, e não exige solvente extra na separação (princípio 4, <strong>solventes e auxiliares mais seguros</strong>); e economiza energia e tempo ao dispensar a separação do sal (princípio 5, <strong>eficiência energética</strong>). Alternativa <strong>D</strong>.</p><p>Fontes renováveis (6), materiais degradáveis (8), verbas (3) e análise em tempo real (9) não aparecem no texto (A, B, C e E).</p>"},
8: {"materia": "Química", "assunto": "Funções inorgânicas", "tags": ["ligação iônica"],
    "enunciado": p("Uma das rotas da produção do óxido de propileno leva à formação do subproduto cloreto de cálcio, um composto iônico em que seus íons, Ca<sup>2+</sup> e Cl<sup>1–</sup>, se encontram dissolvidos em água, como descrito na questão 07.",
                   "Assinale a alternativa que apresenta, corretamente, a fórmula desse composto."),
    "apoio_de": (6, P6),
    "explicacao": "<p>O composto é neutro: a carga +2 do Ca<sup>2+</sup> precisa ser equilibrada por dois íons Cl<sup>1–</sup>. A fórmula é <strong>CaCl<sub>2</sub></strong>. Alternativa <strong>A</strong>.</p><p>Nas outras fórmulas, as cargas não se anulam (C, D e E) ou a proporção não está simplificada (B: Ca<sub>2</sub>Cl<sub>2</sub> ainda teria carga +2).</p>"},
9: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["unidades de conservação"],
    "explicacao": "<p>As Reservas Extrativistas são unidades de conservação de domínio público: as terras pertencem à <strong>União</strong>, e o uso (usufruto) é concedido às <strong>populações tradicionais</strong> que vivem do extrativismo. Alternativa <strong>D</strong>.</p><p>As terras não são das comunidades nem de todos os brasileiros (A), não são de particulares (B e E) e não se destinam a latifundiários (C).</p>"},
10: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["unidades de conservação"],
     "explicacao": "<p>O texto diz que as reservas propostas pelos seringueiros têm um plano de manejo que “garanta a biodiversidade local e a dinâmica cultural do grupo”: <strong>conservar o ambiente e manter os modos de vida</strong>. Alternativa <strong>B</strong>.</p><p>As reservas valem para várias populações tradicionais, não só quilombolas (A). O texto não fala da Constituição (C) nem de Chico Mendes ministro (ele foi assassinado em 1988) (D). E a Rio+10 premiou o manejo de ostras do Mandira, não da castanha (E).</p>"},
11: {"materia": "Matemática", "assunto": "Funções", "tags": ["equação do 2º grau"],
     "enunciado": p("Suponha que um terreno retangular de área 4 225 km<sup>2</sup> será delimitado para se tornar uma nova Reserva Extrativista.",
                    "Se o comprimento do terreno excede em 100 km sua largura (<em>x</em>), uma equação que permite determinar essa largura (<em>x</em>) é"),
     "alternativas": {"A": "\\(x^2 + 100x + 4\\,225 = 0\\)", "B": "\\(x^2 - 100x + 4\\,225 = 0\\)", "C": "\\(x^2 + 100x - 4\\,225 = 0\\)",
                      "D": "\\(x^2 + 4\\,225x - 100 = 0\\)", "E": "\\(x^2 - 4\\,225x + 100 = 0\\)"},
     "explicacao": "<p>A largura é <em>x</em> e o comprimento é <em>x</em> + 100. A área é \\(x(x + 100) = 4\\,225\\), ou seja, \\(x^2 + 100x - 4\\,225 = 0\\). Alternativa <strong>C</strong>.</p><p>A e B erram o sinal do 4 225 ao passá-lo para o outro lado (e B também o do 100). D e E trocam a área com a diferença entre os lados.</p>"},
12: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["mineração"],
     "enunciado": MINERACAO + P12,
     "explicacao": "<p>Para reduzir o risco de novos desastres como os de Mariana e Brumadinho sem acabar com uma atividade econômica importante, o adequado é <strong>fiscalizar melhor e garantir o cumprimento das normas técnicas</strong>. Alternativa <strong>D</strong>.</p><p>Proibir toda a mineração (A) ignora sua importância econômica. Deslocar pessoas e a biodiversidade (B) é inviável. Barragens nos rios (C) ampliariam o dano. E desertos também têm biodiversidade, além de nem sempre haver minério por perto (E).</p>"},
13: {"materia": "Química", "assunto": "Funções inorgânicas", "tags": ["minérios"],
     "enunciado": p("O minério exportado pelo Brasil, em maior quantidade, é extraído, principalmente, em Minas Gerais e Pará.", "Esse minério vem da mineração de"),
     "apoio_de": (12, P12),
     "alternativas": {"A": "cromita, para obtenção de FeO · Cr<sub>2</sub>O<sub>3</sub> e posterior produção de cromo."},
     "explicacao": "<p>O minério que o Brasil mais exporta é o de <strong>ferro</strong>, extraído no Quadrilátero Ferrífero (MG) e em Carajás (PA). Seu principal mineral é a <strong>hematita</strong> (Fe<sub>2</sub>O<sub>3</sub>), usada na produção de ferro e aço. Alternativa <strong>B</strong>.</p><p>Cromita (cromo), galena (chumbo), cassiterita (estanho) e calcopirita (cobre) não são os principais minérios exportados pelo Brasil (A, C, D e E).</p>"},
14: {"materia": "Geografia", "assunto": "Movimentos da Terra", "tags": ["estações do ano"],
     "enunciado": p("Devido ao seu posicionamento no globo terrestre, a Mata Atlântica brasileira tem o bioma típico de áreas tropicais.", "Analise a imagem do planeta Terra.")
                  + "[[fig:1]]" + url("https://tinyurl.com/y3tm2wbu", "20.02.2019", "Original colorido.")
                  + apoio("Considerando as estações do ano no momento representado pela imagem, na Mata Atlântica brasileira é ____<strong>I</strong>____, e no Hemisfério Norte é ____<strong>II</strong>____.")
                  + p("Assinale a alternativa que completa corretamente as lacunas da frase."),
     "imagens": [{"arquivo": "q14", "alt": "Globo terrestre iluminado pela direita, com o eixo inclinado. O polo Norte (N) está todo iluminado, marcado como “Dia polar”, e o polo Sul (S) fica no escuro, marcado como “Noite polar”. Aparecem o Círculo Polar Ártico, o Trópico de Câncer, a Linha do Equador, o Trópico de Capricórnio e o Círculo Polar Antártico. Uma chave indica a faixa entre o Trópico de Câncer e o Equador como “Área de maior recebimento dos raios solares no período dos solstícios de verão. O oposto acontece no inverno.”"}],
     "alternativas": colunas(["I", "II"], [["primavera", "verão"], ["inverno", "inverno"], ["inverno", "verão"], ["verão", "primavera"], ["outono", "primavera"]]),
     "explicacao": "<p>Na imagem, o polo Norte tem dia polar e os raios solares atingem mais o Hemisfério Norte (perto do Trópico de Câncer): é o solstício de <strong>verão no Hemisfério Norte</strong>. Ao mesmo tempo, o Hemisfério Sul, onde está a Mata Atlântica, vive o <strong>inverno</strong> (noite polar no polo Sul). Alternativa <strong>C</strong>.</p><p>Os hemisférios têm estações opostas: não podem estar ambos no inverno (B), e a imagem mostra um solstício, não um equinócio, que marcaria primavera ou outono (A, D e E).</p>"},
15: {"materia": "História", "assunto": "Povos indígenas",
     "enunciado": POVOS + P15,
     "explicacao": "<p>O texto diz que “a arqueologia brasileira tem posto em evidência que o enriquecimento da cobertura e dos solos da floresta – as fertilíssimas ‘terras pretas’ – é fruto das práticas de populações indígenas”. Alternativa <strong>D</strong>.</p><p>IPCC e IPBES são fóruns internacionais que reconheceram esses saberes, não criações indígenas (A). O texto fala em enriquecimento do solo, não em extinção (B e E). E a manutenção das variedades é feita “por conta própria”, sem apoio governamental (C).</p>"},
16: {"materia": "Português", "assunto": "Interpretação de texto",
     "enunciado": p("O quarto parágrafo relata a Grande Fome ocorrida na Irlanda entre 1845 e 1849.", "Esse relato, dentro da estrutura textual, tem por objetivo"),
     "apoio_de": (15, P15),
     "explicacao": "<p>O parágrafo anterior afirma que a agrobiodiversidade é “fundamental para a segurança alimentar”. O caso da Irlanda, onde a falta de variedades de batata permitiu que um fungo destruísse as plantações e causasse fome, serve de <strong>prova</strong> dessa ideia. Alternativa <strong>E</strong>.</p><p>Os europeus selecionaram poucas variedades, não muitas (A). O texto valoriza as práticas indígenas, não as considera menos eficientes (B). Os indígenas não cultivam fungos (C). E o assunto é a flora cultivada, não a fauna (D).</p>"},
17: {"materia": "Biologia", "assunto": "Evolução",
     "enunciado": p("De acordo com o texto, pode-se definir o processo de “coevolução” como o desenvolvimento de espécies por meio de"),
     "apoio_de": (15, P15),
     "explicacao": "<p>O texto descreve plantas e fungos numa “perpétua corrida armamentista”: a cada ataque, as plantas desenvolvem novas defesas. A coevolução é o desenvolvimento das espécies pela <strong>competição para superar as ameaças</strong>. Alternativa <strong>D</strong>.</p><p>Não há resignação nem submissão (B e C), e o processo não é exploração do solo (A) nem extinção (E).</p>"},
18: {"materia": "Português", "assunto": "Interpretação de texto", "tags": ["reescrita"],
     "enunciado": p("Observe a frase:")
                  + apoio("Povos indígenas e comunidades tradicionais mantêm por conta própria, por gosto e tradição, as variedades em cultivo e observam as novidades.")
                  + p("Assinale a alternativa em que a frase apresentada foi reescrita preservando o sentido original."),
     "apoio_de": (15, P15),
     "explicacao": "<p>A frase diz que, por gosto e tradição, os povos mantêm as variedades em cultivo e também observam as novidades. E preserva isso: “Devido ao gosto e à tradição, <strong>não só</strong> as variedades em cultivo são preservadas [...] <strong>como também</strong> novidades são observadas”. Alternativa <strong>E</strong>.</p><p>A diz que as novidades superam o cultivo. B fala em isolamento dos povos. C diz que as variedades eram vistas como novidades. D inverte causa e consequência e acrescenta “aleatoriamente”.</p>"},
19: {"materia": "Geografia", "assunto": "Agropecuária e meio ambiente", "tags": ["solos"],
     "explicacao": "<p>Plantar em <strong>curvas de nível</strong>, acompanhando as cotas do relevo, freia a enxurrada e reduz a erosão. É uma medida de conservação do solo. Alternativa <strong>D</strong>.</p><p>A monocultura esgota os mesmos nutrientes (A). Voçorocas são grandes erosões, que devem ser contidas (B). A lixiviação lava os nutrientes e empobrece o solo (C). E a salinização torna o solo improdutivo (E).</p>"},
20: {"materia": "Matemática", "assunto": "Porcentagem", "tags": ["reta real"],
     "enunciado": HOTSPOTS + P20, "imagens": [RETA_IMG],
     "explicacao": "<p>Os cientistas identificaram entre 1% e 10% das espécies. Como número, isso vai de 1% = 0,01 a 10% = 0,1. Na reta, esses valores ficam praticamente sobre o 0, e o ponto que melhor os representa é o <strong>P</strong>. Alternativa <strong>A</strong>.</p><p>Os pontos Q, T, X e Y valem cerca de 4,5, 10, 12,5 e 18, ou seja, 450%, 1 000% e assim por diante (B a E). Cuidado: o ponto T marca o número 10, e não 10%.</p>"},
21: {"materia": "Geografia", "assunto": "Biomas brasileiros", "tags": ["hotspots"],
     "enunciado": p("Considere o quadro que apresenta dados do Projeto de Monitoramento do Desmatamento dos Biomas Brasileiros por Satélite, em seu relatório de 2009.")
                  + tabela(["Biomas Extra-amazônicos", "Área Original (km<sup>2</sup>)", "Área Desmatada até 2009 (%)"],
                           [["Cerrado", "2 039 386", "48,22"], ["Mata Atlântica", "1 103 961", "75,88"], ["Caatinga", "826 411", "45,92"], ["Pampa", "177 767", "54,17"], ["Pantanal", "151 313", "15,43"]])
                  + fonte("Fonte dos dados: &lt;https://tinyurl.com/y6xl583m&gt; Acesso em: 05.02.2019. Adaptado.")
                  + p("A partir da definição de <em>hotspot</em> apresentada no texto e dos dados do quadro, e considerando apenas a porcentagem de área desmatada até 2009, o Bioma Extra-amazônico que pode ser classificado como <em>hotspot</em> é"),
     "apoio_de": (20, P20),
     "alternativas": {"A": "o Cerrado."},
     "explicacao": "<p>Um <em>hotspot</em> deve ter 30% ou menos da vegetação original preservada, ou seja, pelo menos 70% desmatados. Só a <strong>Mata Atlântica</strong> (75,88% desmatada, cerca de 24% preservada) atende ao critério. Alternativa <strong>B</strong>.</p><p>Cerrado, Caatinga, Pampa e Pantanal ainda preservam mais de 30% da vegetação original (A, C, D e E).</p>"},
22: {"materia": "Matemática", "assunto": "Notação científica",
     "enunciado": p("Admita que a área da superfície do planeta Terra seja de 500 milhões de km<sup>2</sup>.",
                    "Logo, pode-se estimar que o tamanho médio de cada <em>hotspot</em> identificado em 1999 seria, em km<sup>2</sup>,"),
     "apoio_de": (20, P20),
     "alternativas": {"A": "28 × 10<sup>6</sup>", "B": "28 × 10<sup>4</sup>", "C": "28 × 10<sup>3</sup>", "D": "28 × 10<sup>1</sup>", "E": "28 × 10<sup>0</sup>"},
     "explicacao": "<p>Os 25 <em>hotspots</em> ocupavam 1,4% da área do planeta: 0,014 × 500 000 000 = 7 000 000 km². Dividindo por 25: 7 000 000 ÷ 25 = 280 000 = <strong>28 × 10<sup>4</sup></strong> km². Alternativa <strong>B</strong>.</p><p>28 × 10<sup>6</sup> seria cem vezes maior, como se a porcentagem fosse 140% (A); os demais valores são pequenos demais.</p>"},
23: {"materia": "Biologia", "assunto": "Evolução",
     "enunciado": CARTUM + P23, "imagens": [CARTUM_IMG],
     "explicacao": "<p>O cartum usa a conhecida imagem da evolução, que começa na água, para mostrar o ser humano “mais evoluído” <strong>jogando lixo no ambiente de onde a vida se originou</strong>. A crítica é ao comportamento destrutivo humano. Alternativa <strong>E</strong>.</p><p>O cartum não mostra hábitos compartilhados entre espécies (A), não corrige nem distorce a teoria da evolução (B e C) e não diz que a vida surge do lixo (D).</p>"},
24: {"materia": "Português", "assunto": "Gêneros textuais",
     "enunciado": p("Gênero textual define-se como composições socialmente estáveis que têm o objetivo de passar determinadas informações. Cada gênero textual tem peculiaridades que variam de acordo com seus objetivos (informar, criticar, convencer, relatar...), com seu público alvo (adultos, crianças, escritores, professores...), com seu canal de veiculação (mídia impressa, revistas on-line...) e assim por diante. Para atingir seus objetivos, os gêneros textuais podem utilizar tanto a linguagem verbal quanto a não verbal.",
                    "Sobre o cartum apresentado, assinale a alternativa que identifique, corretamente, as características desse gênero, seu objetivo e a linguagem predominantes."),
     "apoio_de": (23, P23),
     "alternativas": colunas(["Características", "Objetivo", "Linguagem"], [
         ["Desenho humorístico ou caricatural, espécie de anedota gráfica que satiriza comportamentos humanos.", "Criticar", "Não verbal"],
         ["Desenho humorístico, com ou sem legenda ou balão, que tem por tema algum acontecimento atual, que comporta crítica e focaliza, por meio de caricatura, uma ou mais personagens envolvidas.", "Informar", "Verbal"],
         ["Segmento de história em quadrinhos, apresentado em jornais ou revistas numa só faixa horizontal.", "Ironizar", "Verbal e não verbal"],
         ["Desenhos em sequência, inicialmente sobre cartão e depois em papel ou afim, em preto ou em cores, para fins caricaturais ou humorísticos de amplo espectro de percepção e aceitação.", "Entreter", "Verbal"],
         ["Narração de particularidade curiosa ou jocosa que acontece à margem dos eventos mais importantes, e por isso pouco divulgada, de uma determinada personagem ou passagem histórica.", "Comover", "Não verbal"]]),
     "explicacao": "<p>O cartum é um desenho humorístico que <strong>satiriza comportamentos humanos</strong>, sem se prender a um fato do dia. Este tem o objetivo de <strong>criticar</strong> e usa linguagem <strong>não verbal</strong> (não há falas, só a imagem). Alternativa <strong>A</strong>.</p><p>B define a charge, ligada a um acontecimento atual. C define a tirinha. D descreve desenhos em sequência, como quadrinhos. E define a anedota ou curiosidade histórica. Além disso, o cartum apresentado não usa linguagem verbal.</p>"},
25: {"materia": "Física", "assunto": "Cinemática", "tags": ["velocidade média"],
     "enunciado": p("O agulhão bandeira é um recordista em velocidade, podendo chegar a surpreendentes 110 km/h devido a sua forma hidrodinâmica e força física.")
                  + "[[fig:1]]" + url("https://tinyurl.com/y5qpnz3t", "17.02.2019", "Original colorido.")
                  + apoio("Lembre-se de que velocidade escalar média é a razão entre distância percorrida e tempo necessário para se percorrer tal distância.")
                  + p("Considerando essa velocidade escalar média constante durante 3 minutos, a distância que esse peixe é capaz de se deslocar é, em metros, de"),
     "imagens": [{"arquivo": "q25", "alt": "Desenho de um agulhão-bandeira: peixe alongado, com o focinho em forma de lança e uma grande nadadeira dorsal em forma de vela."}],
     "alternativas": {"D": "2 000."},
     "explicacao": "<p>3 minutos são 3/60 = 0,05 h. A distância é d = v × t = 110 km/h × 0,05 h = 5,5 km = <strong>5 500 m</strong>. Alternativa <strong>E</strong>.</p><p>Outro caminho: 110 km/h ÷ 3,6 ≈ 30,6 m/s, e 30,6 × 180 s ≈ 5 500 m. 330 resulta de multiplicar 110 por 3 sem converter as unidades (B).</p>"},
26: {"materia": "Biologia", "assunto": "Ecologia", "tags": ["espécies exóticas"],
     "enunciado": apoio(*[it(x, "Lates niloticus") for x in T(13, "O lago Vitória é o maior lago", "200 espécies diferentes de peixes.", ["Com alimentos em abundância", "O período de abundância", "Atualmente, as percas"])])
                  + url("http://tinyurl.com/y2ysbhd9", "01.02.2019")
                  + p("Analisando o texto, é correto afirmar que a espécie exótica dos peixes percas-do-nilo"),
     "explicacao": "<p>A perca-do-nilo foi levada ao lago Vitória, onde não existia: dizimou quase todas as espécies de peixes e, por causa da defumação, provocou desmatamento ao redor do lago, afetando a pesca e a renda das comunidades. Alternativa <strong>D</strong>.</p><p>Ela reduziu a biodiversidade, em vez de aumentá-la (A), e se alimenta só de peixes (B). A pesca cresceu só por um tempo (C). E o texto não fala de introdução fora da África (E).</p>"},
27: {"materia": "Física", "assunto": "Circuitos elétricos", "tags": ["gerador elétrico"],
     "enunciado": p(it("O Electrophorus electricus, popularmente conhecido por poraquê ou treme-treme, é um peixe carnívoro de água doce encontrado na Bacia Amazônica.", "Electrophorus electricus"),
                    "Esse peixe é capaz de liberar uma forte descarga elétrica, imobilizando e até matando suas presas ou agressores. Isso é possível porque, logo após sua cabeça, estende-se uma série de células, conectadas entre si, até a cauda. Essa série de células permite que a cabeça desse peixe tenha carga positiva enquanto a extremidade de sua cauda tenha carga negativa.")
                  + "[[fig:1]]" + url("https://tinyurl.com/yy5lj9jn", "17.02.2019", "Original colorido.")
                  + p("Assinale a alternativa que apresenta um objeto do cotidiano que tem características comparáveis às desse peixe."),
     "alternativas": {"D": "Ferro de passar roupas"},
     "imagens": [{"arquivo": "q27", "alt": "Foto de um poraquê, peixe longo e escuro parecido com uma enguia, nadando em curvas na superfície da água."}],
     "explicacao": "<p>O poraquê tem uma série de células ligadas entre si, com um polo positivo (cabeça) e um negativo (cauda): funciona como pilhas em série, que geram tensão elétrica. É o que faz uma <strong>bateria de carro</strong>, formada por células ligadas em série. Alternativa <strong>C</strong>.</p><p>Alto-falante, motor, ferro de passar e lâmpada consomem energia elétrica, em vez de gerá-la (A, B, D e E).</p>"},
28: {"materia": "História", "assunto": "Antiguidade", "tags": ["rio Nilo"],
     "enunciado": p("Considere o texto e a imagem de satélite.")
                  + apoio(*T(14, "Um desenho de 4 200 anos", "matando peixes de água doce."))
                  + url("https://tinyurl.com/yanwnb8m", "08.02.2019")
                  + "[[fig:1]]" + fonte("&lt;https://tinyurl.com/yxz5aae8&gt;. Acesso em: 10.02.2019. Original colorido.")
                  + p("O mar que está avançando Nilo adentro é o"),
     "imagens": [{"arquivo": "q28", "alt": "Imagem de satélite do nordeste da África e do Oriente Médio. Ao norte, o Mar Mediterrâneo, onde o rio Nilo deságua formando um delta. O Nilo atravessa o Egito de sul a norte; ao sul, está marcada a Represa de Assuã. A leste, o Mar Vermelho, e aparecem também Líbia, Chipre, Líbano, Síria, Israel, Jordânia, Iraque, Kuwait e Arábia Saudita."}],
     "explicacao": "<p>O delta do Nilo fica no norte do Egito e deságua no <strong>Mar Mediterrâneo</strong>, que avança rio adentro com a erosão do delta. Foi em torno do Mediterrâneo que se formou o Império Romano. Alternativa <strong>D</strong>.</p><p>O Mar Vermelho fica a leste e não recebe o Nilo (A). O Mar Morto é um lago salgado longe do delta (B). Não existe “mar Mesopotâmico” (C). E o mar da Arábia fica muito distante (E).</p>"},
29: {"materia": "Biologia", "assunto": "Zoologia",
     "explicacao": "<p>As esponjas (poríferos) são animais aquáticos, com o corpo cheio de poros. A água entra por eles e circula pelas cavidades internas, de onde a esponja <strong>filtra partículas de alimento</strong>. Alternativa <strong>B</strong>.</p><p>Cetáceos são mamíferos e não põem ovos com casca (A). Crustáceos têm carapaça e apêndices, e estrelas-do-mar e ouriços não têm antenas (C). As algas citadas são clorofiladas e dependem de luz (D). E cetáceos, tartarugas e focas respiram por pulmões (E).</p>"},
30: {"materia": "Física", "assunto": "Pressão", "tags": ["empuxo"],
     "enunciado": p(*T(15, "Os estudos de hidrostática de Arquimedes", "tendendo a ficar no fundo.", ["Para obter o empuxo"]))
                  + "[[fig:1]]" + p("Para o peixe, nessas condições, podemos concluir corretamente que o"),
     "imagens": [{"arquivo": "q30", "alt": "Desenho de um peixe com uma seta para cima, legendada “direção e sentido do empuxo”, e uma seta para baixo, legendada “direção e sentido do peso”."}],
     "explicacao": "<p>Sem o gás da bexiga natatória, o peixe fica mais denso que a água e tende a afundar. Se a resultante aponta para baixo, o <strong>empuxo é menor que o peso</strong>. Alternativa <strong>E</strong>.</p><p>Peso e empuxo continuam existindo (A e B). Empuxo maior faria o peixe subir (C), e igual o manteria parado na mesma profundidade (D).</p>"},
31: {"materia": "Geografia", "assunto": "Hidrografia", "tags": ["Mar de Aral"],
     "enunciado": apoio(*T(16, "O desaparecimento do Mar de Aral", "se transformar em um deserto.", ["Em meados do século XX", "O que antes eram", "Os dois maiores rios", "Como o mar encolheu", "O clima também", "Marjan, uma mulher"]))
                  + url("https://tinyurl.com/y2wausz9", "10.02.2019")
                  + p("De acordo com o texto, podemos afirmar corretamente que"),
     "explicacao": "<p>O texto diz que o desastre foi “provocado pelo homem”: a partir de meados do século XX, os rios que alimentavam o Mar de Aral foram desviados para irrigar o algodão. É uma <strong>ação antrópica</strong> que começou no século passado. Alternativa <strong>B</strong>.</p><p>Os peixes morreram, e a vida dos pescadores piorou (A). O volume de água diminuiu (C). Os pesticidas mataram os peixes (D). E a chuva parou (E).</p>"},
32: {"materia": "Biologia", "assunto": "Ecologia", "tags": ["eutrofização"],
     "enunciado": apoio(*T(16, "Nos ecossistemas aquáticos, o despejo", "biota aquática.", ["Esse tipo de poluição", "As algas, que vivem", "A decomposição"]))
                  + p("Sobre o processo de poluição descrito, é correto afirmar que"),
     "explicacao": "<p>Na eutrofização, as algas mortas alimentam bactérias decompositoras aeróbias, que consomem o oxigênio da água. Sem oxigênio, morrem peixes e outros seres aeróbios, <strong>inclusive as próprias bactérias aeróbias</strong>, e a decomposição passa a ser anaeróbia. Alternativa <strong>E</strong>.</p><p>A camada de algas impede a passagem de luz (A). A decomposição aumenta, pelo excesso de nutrientes (B). Bactérias decompositoras não são produtoras (C). E quem decompõe é a bactéria, não a alga, e a matéria decomposta é orgânica (D).</p>"},
33: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["conferências ambientais"],
     "enunciado": apoio(*T(17, "A Conferência de Estocolmo, em 1972", "sistemas de proteção social.", ["Mais tarde, em 1992", "A Eco-92 também", "A Agenda 21, especificamente", "Essas ações prioritárias"]))
                  + url("https://tinyurl.com/y4bgh6xb", "05.02.2019")
                  + p("De acordo com o texto, é correto afirmar que"),
     "explicacao": "<p>O texto diz que a Conferência de Estocolmo (1972) foi a primeira da ONU sobre meio ambiente e “chamou a atenção internacional” para a degradação ambiental e a poluição. Alternativa <strong>D</strong>.</p><p>A Cúpula de Joanesburgo (2002) reforçou ações já existentes (A). A Agenda 21 tratou também de planejamento participativo, ética e política (B e C). E ela nasceu na Eco-92, não em Estocolmo (E).</p>"},
34: {"materia": "Física", "assunto": "Pressão",
     "enunciado": p("É surpreendente como a vida pode ocorrer mesmo em locais inóspitos como, por exemplo, nas fossas das Marianas, grande depressão oceânica localizada na fronteira entre as placas tectônicas do Pacífico e das Filipinas. Nesse local, o leito oceânico atinge cerca de 11 000 metros de profundidade. A pressão é tão grande que os seres que lá habitam tiveram de desenvolver condições especiais para sua sobrevivência, o que torna impossível trazê-los vivos para a superfície.",
                    "Considerando que para cada 10 metros de profundidade sob a água, a pressão é acrescida de 1 atm, é correto afirmar que a pressão total suportada pelos seres que vivem no fundo das fossas das Marianas equivale a")
                  + apoio("Lembre-se de que a pressão exercida pelo ar atmosférico, quando se está ao nível do mar, é de uma atmosfera (1 atm)."),
     "alternativas": {"A": "110 atm.", "B": "111 atm.", "C": "1 100 atm.", "D": "1 101 atm.", "E": "1 110 atm."},
     "explicacao": "<p>A água acrescenta 11 000 ÷ 10 = 1 100 atm. Somando a pressão do ar na superfície (1 atm), a pressão total é <strong>1 101 atm</strong>. Alternativa <strong>D</strong>.</p><p>1 100 atm esquece a pressão atmosférica (C). 110 e 111 atm erram a divisão por 10 (A e B).</p>"},
35: {"materia": "História", "assunto": "Brasil Colônia", "tags": ["família real"],
     "explicacao": "<p>O Jardim Botânico foi criado em 1808, ano em que a <strong>Corte portuguesa se transferiu para o Brasil</strong>, fugindo das tropas de Napoleão. O Rio de Janeiro virou a sede do império português, e D. João criou várias instituições. Alternativa <strong>B</strong>.</p><p>D. Pedro II só reinou a partir de 1840 (A). A Independência é de 1822 e criou um império, não uma república (C). O Rio foi fundado em 1565 (D). E Brasília só virou capital em 1960 (E).</p>"},
36: {"materia": "História", "assunto": "Povos indígenas", "tags": ["milho"],
     "enunciado": apoio(*T(18, "Antigos agricultores da Amazônia", "público mais amplo.", ["Segundo os pesquisadores"]))
                  + url("https://tinyurl.com/yb476wne", "31.01.2019")
                  + p("De acordo com o texto, é correto afirmar que"),
     "explicacao": "<p>O texto diz que a análise das variedades tradicionais de milho cultivadas por povos como os Guarani “é crucial para preservar a <strong>diversidade genética</strong> da planta”. Alternativa <strong>A</strong>.</p><p>O milho surgiu no México, não nos Andes (B e C). O texto não diz que mandioca, goiaba e feijão vieram da América do Norte; eles foram domesticados no sudoeste amazônico (D). E a floresta amazônica é tropical, não boreal (E).</p>"},
37: {"materia": "Matemática", "assunto": "Operações e problemas", "tags": ["sistemas de equações"],
     "explicacao": "<p>Sendo P as plantas e V os vertebrados: P + V = 8 732 e P − V = 7 268. Somando as equações, 2P = 16 000, então P = <strong>8 000</strong>. Alternativa <strong>D</strong>.</p><p>732 é o número de vertebrados (A). 16 000 é o dobro das plantas, antes de dividir por 2 (E).</p>"},
38: {"materia": "Biologia", "assunto": "Ecologia", "tags": ["relações ecológicas"],
     "explicacao": "<p>As epífitas usam outras plantas apenas como <strong>suporte</strong>, sem prejudicá-las nem retirar nutrientes delas. Essa relação, em que uma espécie se beneficia e a outra não é afetada, é o <strong>inquilinismo</strong>. Alternativa <strong>C</strong>.</p><p>Na simbiose (mutualismo), as duas espécies se beneficiam (A). Na predação e no parasitismo, uma espécie é prejudicada (B e E). E o canibalismo ocorre entre indivíduos da mesma espécie (D).</p>"},
39: {"materia": "Geografia", "assunto": "Biomas brasileiros", "tags": ["florestas tropicais"],
     "explicacao": "<p>As florestas tropicais úmidas ficam perto do Equador, onde há <strong>muita luz, muita umidade e temperaturas altas</strong> o ano todo. Essas condições favorecem o crescimento das plantas e sustentam muitas espécies. Alternativa <strong>B</strong>.</p><p>Tundra e vegetação xerófita são de climas frios ou secos (A). As florestas tropicais têm temperaturas médias altas e pequena amplitude térmica (C e D). E têm rios perenes e pouca luz no chão da mata, por causa das copas (E).</p>"},
40: {"materia": "Matemática", "assunto": "Geometria plana", "tags": ["áreas"],
     "enunciado": apoio("O papel das doenças na conservação da vida selvagem é por vezes subestimado. Durante expedições no Polo Sul, acredita-se que os cães utilizados para o transporte de trenós tenham transmitido o vírus da cinomose canina a uma espécie de foca que habitava essa região, levando à ocorrência de extensa mortalidade desses animais.")
                  + fonte("&lt;https://tinyurl.com/y23ykngw&gt; Adaptado. Acesso em: 10.02.2019")
                  + "[[fig:1]]"
                  + p("Suponha que, em determinado período de uma expedição esse vírus tenha se propagado na região delimitada pelo triângulo ABC, da figura, em que:")
                  + p("• a medida de \\(\\overline{AC}\\) é igual a 70 km;", "• o ângulo \\(B\\hat{A}C\\) é reto;", "• o ângulo \\(A\\hat{B}C\\) mede 45°.")
                  + p("Após um mês, essa doença atingiu a área correspondente ao triângulo DEF, em que:")
                  + p("• a medida de \\(\\overline{DF}\\) é igual a 140 km;", "• o ângulo \\(E\\hat{D}F\\) é reto;", "• o ângulo \\(D\\hat{E}F\\) mede 45°.")
                  + p("Sobre a área do triângulo DEF, é correto afirmar que ela é"),
     "imagens": [{"arquivo": "q40", "alt": "Mancha clara de contorno irregular sobre fundo escuro, com dois triângulos desenhados: um triângulo menor, ABC, dentro de um triângulo maior, DEF, com lados paralelos aos do menor."}],
     "explicacao": "<p>Os dois triângulos são retângulos com um ângulo de 45°: são isósceles, com catetos iguais. Área de ABC = 70 × 70 ÷ 2 = 2 450 km². Área de DEF = 140 × 140 ÷ 2 = 9 800 km². Como 9 800 ÷ 2 450 = 4, a área de DEF é o <strong>quádruplo</strong> da de ABC. Alternativa <strong>D</strong>.</p><p>Os lados dobraram, mas a área cresce com o quadrado da razão: 2² = 4. Por isso “o dobro” está errado (C).</p>"},
41: {"materia": "Física", "assunto": "Ondas", "tags": ["espectro eletromagnético"],
     "enunciado": p(*[it(x, "Aedes aegypti") for x in T(19, "O acidente nuclear de Chernobyl", "comprimentos de onda em metros.", ["Há estudos sobre", "A figura apresenta"])])
                  + "[[fig:1]]" + url("http://tinyurl.com/yyg6we75", "30.03.19", "Original colorido.")
                  + p("De acordo com o texto, o tipo de radiação potencialmente capaz de combater o mosquito citado é"),
     "imagens": [{"arquivo": "q41", "alt": "Espectro eletromagnético em faixa horizontal, da esquerda para a direita: rádio, micro-ondas, infravermelho, luz visível, ultravioleta, raios X e raios gama. Abaixo, uma onda que fica cada vez mais curta para a direita e uma escala de comprimentos de onda em metros: 10³, 1, 10⁻³, 10⁻⁵, 10⁻⁷, 10⁻⁹, 10⁻¹¹ e 10⁻¹³. Os raios gama ficam na ponta dos menores comprimentos de onda."}],
     "explicacao": "<p>O texto diz que a principal emissão de Chernobyl são ondas eletromagnéticas “com os menores comprimentos de onda e, portanto, maiores energias”, e que os mosquitos são expostos a radiações semelhantes. No espectro, os menores comprimentos de onda são os dos <strong>raios gama</strong>. Alternativa <strong>E</strong>.</p><p>Micro-ondas, infravermelho, ultravioleta e raios X têm comprimentos de onda maiores (A, B, C e D).</p>"},
42: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["biopirataria"],
     "enunciado": apoio(*T(20, "Biopirataria é crime.", "aos índios da Amazônia.", ["Não bastasse a apropriação", "No Brasil, a biopirataria", "Podemos encontrar alguns", "Outro caso é"]))
                  + url("https://tinyurl.com/y8heaay5", "27.01.2019")
                  + p("De acordo com o texto, podemos afirmar corretamente que a biopirataria"),
     "explicacao": "<p>O texto diz que a biopirataria “também se apropria de conhecimentos acumulados por comunidades tradicionais, como a medicina da floresta e as práticas da cultura indígena”. Alternativa <strong>C</strong>.</p><p>Ela é praticada desde o Descobrimento, antes da indústria farmacêutica (A). Hipertensão não é causada por vírus (B). O cupuaçu quase foi patenteado no Japão, sem relação com importações (D). E a biopirataria é crime (E).</p>"},
43: {"materia": "História", "assunto": "Grandes Navegações", "tags": ["especiarias"],
     "enunciado": apoio(*T(20, "A Indonésia, um dos países", "produtor comercial desse item.", ["Hoje, a ilha de Zanzibar"]))
                  + url("https://tinyurl.com/y9johgqz", "03.02.2019")
                  + p("Assinale a alternativa que apresenta o processo histórico que pôs os lugares citados no texto em contato."),
     "explicacao": "<p>Molucas (Indonésia), Zanzibar e Madagascar (África) e a Bahia (Brasil) foram ligados pelas <strong>navegações ibéricas do século XV</strong> (e XVI), que buscavam especiarias como o cravo e acabaram levando-as a outros continentes. Alternativa <strong>C</strong>.</p><p>As cruzadas são da Idade Média, não do século II a.C. (A). Caravanas indianas e a rota da seda eram terrestres e não chegavam ao Brasil (B e D). E as migrações islâmicas não envolveram a América (E).</p>"},
44: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": ["parasitoses"],
     "enunciado": p("A construção de instalações sanitárias adequadas, tais como privadas, esgotos e fossas sépticas, que diminuem a eutrofização e impedem a contaminação da água e de alimentos, são formas de prevenção da doença descrita:")
                  + apoio(*T(20, "parasitose humana adquirida", "pode tornar-se anêmica."))
                  + p("A doença parasitária descrita é denominada"),
     "explicacao": "<p>Cistos ingeridos com água ou alimentos contaminados por fezes, que se rompem no intestino e liberam parasitas que causam diarreia, às vezes com sangue: é a <strong>amebíase</strong>, causada pela <em>Entamoeba histolytica</em>. Alternativa <strong>A</strong>.</p><p>Dengue e malária são transmitidas por mosquitos (B e D). A hepatite é causada por vírus (C). E a teníase vem da carne mal cozida com larvas (cisticercos) da tênia (E).</p>"},
45: {"materia": "Biologia", "assunto": "Botânica",
     "enunciado": apoio(*T(21, "Depois de sete anos de trabalho", "semelhante a uma taça.", ["Esse levantamento destaca que", "Esse levantamento destaca, também"]))
                  + url("http://tinyurl.com/yynu7h8/", "27.01.2019")
                  + p("A partir das informações do texto, é correto afirmar que"),
     "explicacao": "<p>As angiospermas têm sementes protegidas por frutos, e as gimnospermas, sementes expostas. O que os dois grupos têm em comum é a <strong>presença de sementes</strong>. Alternativa <strong>E</strong>.</p><p>As plantas endêmicas são exclusivas do Brasil, não vindas de fora (A). Angiospermas têm folhas, frutos e vasos condutores, e incluem árvores (B). A araucária é gimnosperma, típica do Sul, e não tem fruto (C). E feijão, amendoim e banana têm frutos; o pinhão é semente de gimnosperma (D).</p>"},
46: {"materia": "Matemática", "assunto": "Razão e proporção", "tags": ["grandezas proporcionais"],
     "enunciado": p(*T(21, "Segundo pesquisas, na história do planeta", "constante de proporcionalidade.",
                       ["Suponha que um desses", "Considere que a energia", "Assinale a expressão"])),
     "alternativas": {"A": "E = k · 15", "B": "E = k · 200", "C": "E = k · 3 000", "D": "E = k · 3 3750", "E": "E = k · 8 000 000"},
     "explicacao": "<p>A energia é proporcional ao <strong>cubo do diâmetro da cratera</strong>: E = k · 200³ = k · 200 × 200 × 200 = <strong>k · 8 000 000</strong>. Alternativa <strong>E</strong>.</p><p>A e B não elevam ao cubo. D vem de usar o diâmetro do asteroide (15³ = 3 375), que não é a grandeza indicada. E C não corresponde a nenhum cubo das medidas dadas.</p>"},
47: {"materia": "Química", "assunto": "Química ambiental",
     "enunciado": apoio(*T(21, "A Química Ambiental estuda todo", "Agronomia, Biologia e Toxicologia.", ["Sem sombra de dúvidas"]))
                  + url("https://tinyurl.com/y6r2ca35", "04.02.2019")
                  + p("Assinale a alternativa correta sobre o conteúdo baseado no texto."),
     "explicacao": "<p>O texto diz que a Química Ambiental estuda processos que ocorrem de forma natural ou provocados pelo ser humano (origem antropogênica) e “está diretamente relacionada com diversas outras ciências”. Alternativa <strong>C</strong>.</p><p>O texto não diz que ela resolve problemas industriais (A), nem que a Química age sozinha (B), nem que interrompe o ciclo da água (D). Seu alvo é esclarecer os mecanismos naturais, não só remover poluentes (E).</p>"},
48: {"materia": "Geografia", "assunto": "Climatologia", "tags": ["aquecimento global"],
     "enunciado": apoio(*T(22, "Embora o clima tenha apresentado", "nos últimos cem anos.", ["Outro aspecto distinto", "A principal evidência", "Atualmente, as temperaturas"]))
                  + url("https://tinyurl.com/y72aq8tf", "21.01.2019")
                  + p("De acordo com o texto, é correto afirmar que"),
     "explicacao": "<p>O texto diz que a principal evidência da mudança do clima é o aquecimento global, detectado no aumento da temperatura média do ar e dos oceanos, no derretimento da neve e do gelo e na elevação do nível do mar, “fato que não pode mais ser negado”. Alternativa <strong>A</strong>.</p><p>O texto afirma que há evidências (B), atribui a mudança atual às atividades humanas (C e D) e registra aumento de cerca de 0,74 °C em cem anos, não esfriamento (E).</p>"},
49: {"materia": "História", "assunto": "Idade Média",
     "enunciado": apoio(*T(22, "Para o homem europeu medieval", "num mundo do Além."))
                  + fonte("FRANCO JÚNIOR, Hilário. <em>A Idade Média, nascimento do Ocidente</em>. São Paulo: Brasiliense, 2006, p. 139. Adaptado.")
                  + p("De acordo com o autor, é correto afirmar que"),
     "explicacao": "<p>O autor diz que, à mercê de forças que não controlava (colheitas ruins, epidemias), o europeu medieval sentia insegurança e buscava as origens e as saídas “num mundo do Além”: o <strong>sobrenatural</strong>. Alternativa <strong>D</strong>.</p><p>As colheitas eram imprevisíveis e “quase sempre pobres” (A). A ciência não substituiu o sagrado na Idade Média (B). A relação com a natureza era de medo, não pacífica nem racionalista (C). E os valores medievais eram teocêntricos, não antropocêntricos (E).</p>"},
50: {"materia": "Geografia", "assunto": "Agropecuária e meio ambiente", "tags": ["desmatamento"],
     "explicacao": "<p>As pressões econômicas convertem florestas tropicais em áreas alteradas principalmente pela <strong>expansão desordenada da fronteira agropecuária</strong>, que desmata para abrir pastos e lavouras. Alternativa <strong>A</strong>.</p><p>Pesquisa de fontes alternativas, fiscalização, uso sustentável e criação de áreas de proteção ajudam a conservar a biodiversidade, em vez de reduzi-la (B, C, D e E).</p>"},
}
completar(Q, R)
