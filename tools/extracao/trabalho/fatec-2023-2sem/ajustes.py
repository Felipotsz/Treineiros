# Ajustes da conferência humana: Vestibular FATEC 2º semestre de 2023 (exame de 25/06/2023)
# Texto conferido com a imagem de cada página. Tema: Alimentação (a apresentação fala de "um cardápio diverso").
# 54 questões; a prova tem 5 h no total, incluindo a redação (que fica fora do simulado).
# Matéria: a do gabarito oficial; nas "Multidisciplinar", a matéria principal + tag "multidisciplinar".
# O rascunho embaralhou as alternativas das páginas em duas colunas e deslocou várias questões:
# todos os enunciados e alternativas foram escritos aqui, a partir do texto do PDF e da imagem da página.
# Gabarito: oficial (2SEM23); Q39 ANULADA sem motivo publicado (justificativa por análise).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import A, carregar, enun, tabela, colunas, completar, trecho

ID = "fatec-2023-2sem"
META = {
    "id": ID,
    "banca": "FATEC",
    "ano": 2023,
    "semestre": 2,
    "titulo": "Vestibular FATEC, 2º semestre de 2023",
    "fonte": "Centro Paula Souza",
    "dataExame": "2023-06-25",
    "duracaoMinutos": 300,
    "tema": "Alimentação",
    "apresentacao": "<p>Prezado(a) candidato(a), é possível traçar a história da humanidade, desde a pré-História até os dias de hoje, pela alimentação. Os alimentos dizem muito sobre nossa cultura, pois eles relacionam várias áreas de saber. Por isso, os temas aqui propostos, trazem à reflexão um cardápio diverso e importante para nossas vidas.</p>",
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
CANASTRA = (chamada("Leia o texto para responder às questões 06 e 07.")
            + apoio(*T(4, "Em Minas Gerais, os municípios da Serra", "para valorizar seu queijo.",
                       ["Os portugueses trouxeram", "Para que as bactérias", "Na etapa seguinte", "Ao longo do processo", "Na serra, nos sítios"]))
            + url("https://tinyurl.com/mr2brpfz", "09.03.2023"))
P6 = p("Segundo o texto,")

AGRO = (chamada("Leia o texto para responder às questões 09 e 10.")
        + apoio(*T(5, "Agroforestry is the interaction of agriculture", "provision of ecosystem services).", []),
                "Agroforestry is agricultural and forestry systems that try to balance various needs:",
                "1) to produce trees for timber and other commercial purposes;",
                "2) to produce a diverse, adequate supply of nutritious foods both to meet global demand and to satisfy the needs of the producers themselves; and",
                "3) <strong>to ensure the protection of the natural environment so that it continues to provide resources and environmental services</strong> to meet the needs of the present generations and those to come.")
        + url("https://tinyurl.com/pnv4wjx8", "04.03.2023", ""))
P9 = p("De acordo com o texto, o equilíbrio pretendido entre agricultura e floresta, no sistema chamado de <em>Agroforestry</em>, prevê")

PIZZA = (chamada("Leia o texto e o gráfico para responder às questões de 15 a 17.")
         + p("Segundo estudiosos, pode ter sido em São Paulo que a pizza assumiu a cara de um prato familiar que pode servir mais de uma pessoa, sendo caracterizado, normalmente, como um disco de 35 cm de diâmetro; ao contrário da pizza de Nápoles, sua ancestral, que é um prato individual feito com um diâmetro médio de 28,5 cm.",
             "O gráfico mostra as preferências dos paulistanos em relação à pizza.")
         + "[[fig:1]]" + fonte("Fonte dos dados do gráfico: &lt;https://tinyurl.com/ymw3m7p7&gt; Acesso em: 05.03.2023."))
PIZZA_IMG = figs(("q15", "Gráfico de barras “Cobertura de pizza predileta dos paulistanos”: quatro queijos, 24,3%; portuguesa, 17,7%; mussarela, 14,7%; calabresa, 14,7%; outras, 28,6%."))
P15 = p("Admita que, em um sábado, 45 % dos paulistanos pediram uma pizza da sua cobertura predileta.",
        "Pode-se dizer que, nesse dia, a cada 100 paulistanos, aproximadamente N pessoas pediram uma pizza cuja cobertura predileta é portuguesa.",
        "Assinale a alternativa que apresenta o número inteiro que mais se aproxima de N.")

ARADO = (chamada("Leia o texto para responder às questões de 21 a 23.")
         + apoio(*T(10, "Foi um tempo difícil.", "guisado no azeite de dendê.", ["Disputamos a palma"]))
         + fonte("Vieira Jr., Itamar. <em>Torto arado</em>. Todavia, pp. 67-68. [versão e-reader]. Adaptado."))
ARADO = troca(ARADO, [("como (I)", "<strong><u>como</u></strong> (I)"), ("por (II)", "<strong><u>por</u></strong> (II)"), ("para (III)", "<strong><u>para</u></strong> (III)"),
                      ("que (IV)", "<strong><u>que</u></strong> (IV)"), ("para (V)", "<strong><u>para</u></strong> (V)")])
P21 = p("Há, na passagem apresentada, diversos elementos de coesão responsáveis pela conexão das informações contidas no texto.",
        "É correto afirmar, após analisar os conectivos destacados no texto, que")

FAO = (chamada("Leia o texto para responder às questões de 26 a 28.")
       + apoio("<strong>What is hunger?</strong>",
               it(" ".join(T(12, "Hunger is an uncomfortable or painful", "referred to as undernourishment.")), "Prevalence of Undernourishment", "undernourishment."),
               "<strong>What is food insecurity?</strong>",
               "<strong>A person is food insecure when they lack regular access to enough safe and nutritious food</strong> " + " ".join(T(12, "for normal growth and development", "(FIES) shown below:")))
       + "[[fig:1]]" + fonte("Fonte de dados: &lt;https://tinyurl.com/4hbsa9yr&gt; Acesso em: 04.03.2023."))
FAO_IMG = figs(("q26", "Infográfico “Food insecurity based on the FIES: what does it mean?” (insegurança alimentar segundo a FIES: o que significa?). Uma seta em quatro etapas, de clara a escura: “Uncertainty regarding ability to obtain food” (incerteza sobre a capacidade de obter alimento); “Compromising on food quality and variety” (abrir mão da qualidade e da variedade); “Reducing food quantity, skipping meals” (reduzir a quantidade, pular refeições); “No food for a day or more” (ficar sem comida por um dia ou mais). Abaixo, as faixas: “Food security to mild food insecurity” (segurança a insegurança leve), sob as duas primeiras etapas; “Moderate food insecurity” (moderada), com a descrição “This person has: insufficient money or resources for a healthy diet; uncertainty about the ability to obtain food; probably skipped meals or run out of food occasionally”; e “Severe food insecurity” (grave), com “This person has: run out of food; gone an entire day without eating at times during the year”."))
P26 = p("Segundo a Organização das Nações Unidas para a Agricultura e Alimentação (FAO),")

MILHO = (chamada("Leia o texto para responder às questões 36 e 37.")
         + p(*T(16, "No Brasil, a Instrução Normativa", "porção do milho painço.", ["A tabela 2 apresenta"]))
         + tabela(["Tabela 1: Valores diários de referência de nutrientes – IN nº 75", ""], [["Carboidratos", "300 g"], ["Proteínas", "50 g"], ["Gorduras Totais", "65 g"]])
         + tabela(["Tabela 2: Milho painço – porção de 45 g", ""], [["Carboidratos", "30 g"], ["Proteínas", "5,4 g"], ["Gorduras Totais", "1,8 g"]]))
P36 = p("Leia o texto e assinale a alternativa cujos termos completam, correta e respectivamente, as lacunas.")

LASANHA = (chamada("Considere a imagem de uma embalagem para responder às questões de 39 a 41.")
           + p("<strong>Sample Label for Frozen Lasagna</strong>") + "[[fig:1]]"
           + fonte("Fontes dos dados: &lt;https://tinyurl.com/bp7b85js&gt; Acesso em: 04.03.2023.")
           + p("(1) Serving Information", "(2) Calories", "(3) Quick Guide to percent Daily Value (% DV)<br>• 5 % or less is <strong>low</strong><br>• 20 % or less is <strong>high</strong>", "(4) Nutrients"))
LASANHA_IMG = figs(("q39", "Rótulo “Nutrition Facts” de uma lasanha congelada, com chaves numeradas de 1 a 4 à direita. (1) 4 servings per container; serving size 1 cup (227 g). (2) Amount per serving: Calories 280. (3) % Daily Value. (4) Nutrientes, com a % do valor diário: Total Fat 9 g, 12%; Saturated Fat 4.5 g, 23%; Trans Fat 0 g; Cholesterol 35 mg, 12%; Sodium 850 mg, 37%; Total Carbohydrate 34 g, 12%; Dietary Fiber 4 g, 14%; Total Sugars 6 g; Includes 0 g Added Sugars, 0%; Protein 15 g; Vitamin D 0 mg, 0%; Calcium 320 mg, 25%; Iron 1.6 mg, 8%; Potassium 510 mg, 10%. Nota: “The % Daily Value (DV) tells you how much a nutrient in a serving of food contributes to a daily diet. 2,000 calories a day is used for general nutrition advice.”"))
P39 = p("A partir da leitura da imagem, pode concluir-se corretamente que uma porção desse produto")

CONSERVA = (chamada("Leia o texto para responder às questões 43 e 44.")
            + apoio("O sal e o <strong>açúcar</strong> são agentes <strong>conservantes</strong> utilizados em produtos que consumimos.",
                    "A conservação pelo uso do açúcar é empregada em frutas ao preparar geleias, conservas e cristalizações. Em alta concentração, esse composto possui efeito desidratante, pois ocasiona aumento da pressão <strong>osmótica</strong> no interior da fruta, o que dificulta o desenvolvimento de bactérias, bolores e leveduras.",
                    "Do mesmo modo, soluções com altas concentrações salinas fazem os micro-organismos presentes morrerem por <strong>desidratação</strong>. Este processo é conhecido por salga ou <strong>salmoura</strong> e é eficiente do ponto de vista microbiológico, porém não evita a degradação química. Em alguns alimentos, como na carne seca, com o passar do tempo, ocorrem reações de <strong>oxidação</strong> das gorduras que conferem sabor de ranço ao alimento.")
            + fonte("&lt;https://tinyurl.com/3mbdv42&gt;. Acesso em: 05.03.2023. Adaptado."))
P43 = p("De acordo com o texto, é correto afirmar que, quando entram em contato com soluções cujas concentrações salinas são altas, os micro-organismos")

ENTREGA = (chamada("Leia o texto para responder às questões 48 e 49.")
           + p(*T(20, "Para se aprofundar nos estudos, um estudante", "apresentadas no quadro.", ["A IA, então, retorna"]))
           + apoio("• Tempo médio percorrido para a entrega: t = 15 minutos = 900 segundos<br>• Velocidade escalar média da moto elétrica do entregador: v = 10 m/s<br>• Carga elétrica da bateria da moto: Q = 20 kWh"))
P48 = p("Após receber o exercício, o estudante identifica um erro.", "Analisando os dados, é correto afirmar que <strong>o erro identificado</strong> se refere")

Q = {
1: {"materia": "História", "assunto": "Pré-História", "tags": ["evolução humana", "fogo"],
    "enunciado": apoio(*[it(x, "Homo sapiens") for x in T(2, "Ao aprender a cozinhar, os homens", "pois mata potenciais patógenos.")])
                 + url("https://tinyurl.com/2p9c5w66", "09.03.2023")
                 + p("Assinale a alternativa que apresenta corretamente uma das conclusões do estudo citado no texto."),
    "alternativas": alts("As evidências disponíveis são insuficientes para identificar o período em que os hominídeos começaram a cozinhar os alimentos.",
                         "As evidências coletadas pelo estudo sugerem que a agricultura e a pecuária eram praticadas pelos hominídeos há 780 mil anos.",
                         "Os alimentos cozidos permitiram o crescimento do corpo e do cérebro humanos, contribuindo para a evolução de nossa espécie.",
                         "Os hominídeos cozinhavam alimentos há cerca de 780 mil anos, mas os <em>Homo sapiens</em> e os Neandertais preferiam os alimentos crus.",
                         "O tamanho do cérebro dos <em>Homo sapiens</em> e dos Neandertais é um fator evolutivo insignificante em relação aos primeiros hominídeos."),
    "explicacao": "<p>O texto diz que cozinhar torna os alimentos mais fáceis de digerir, “permitindo o crescimento do corpo e do cérebro de forma muito mais eficiente”, e chama isso de “um dos passos evolutivos mais importantes da nossa espécie”. Alternativa <strong>C</strong>.</p><p>O estudo identifica um período, cerca de 780 mil anos atrás (A). Agricultura e pecuária são muito mais recentes, do Neolítico (B). O texto diz que <em>Homo sapiens</em> e Neandertais usavam fogo para cozinhar (D). E o crescimento do cérebro é apresentado como importante, não insignificante (E).</p>"},
2: {"materia": "Biologia", "assunto": "Nutrição e saúde",
    "enunciado": p(*T(2, "Uma alimentação saudável e variada", "pode resultar em doenças graves.", ["Sem os nutrientes certos"]), "Com base no texto, pode-se afirmar corretamente que é benéfico à saúde"),
    "alternativas": alts("consumir defumados ou embutidos ricos em gorduras e em sódio, pois diminuem a pressão arterial, o colesterol e o risco de alguns tipos de câncer.",
                         "consumir, nas refeições, apenas alimentos industrializados e altamente processados, pois garantem o aumento da imunidade e a prevenção contra vírus e bactérias.",
                         "preferir suplementos alimentares industrializados de vitaminas ou de proteínas, pois são mais saudáveis e não colocam a saúde do corpo em risco, ao contrário da ingestão de alimentos naturais.",
                         "optar por temperos naturais, como ervas aromáticas e especiarias, que contêm vitaminas, minerais e antioxidantes, em vez de temperos industrializados, com alto teor de sódio e conservantes.",
                         "optar por alimentos ricos em gorduras trans, que não se depositam em nossas artérias e que foram desenvolvidas pela indústria alimentícia para manter alimentos mais tempo sem estragar."),
    "explicacao": "<p>Temperos naturais trazem vitaminas, minerais e antioxidantes e evitam o excesso de sódio e de conservantes dos temperos industrializados, ligado à hipertensão. Alternativa <strong>D</strong>.</p><p>Embutidos com muita gordura e sódio aumentam a pressão e o risco de câncer (A). Ultraprocessados não garantem imunidade (B). Suplementos não substituem uma dieta variada e podem fazer mal em excesso (C). E a gordura trans se deposita nas artérias (E).</p>"},
3: {"materia": "Biologia", "assunto": "Nutrição e saúde", "tags": MULTI + ["ferro", "anemia"],
    "enunciado": apoio(*T(3, "Existe o mito de que a beterraba", "logo após as refeições.", ["As melhores fontes de ferro", "Como a vitamina C", "Existem alimentos como"]))
                 + fonte("Fonte dos dados: &lt;https://tinyurl.com/4mvxer26&gt; Acesso em: 17.03.2023. Adaptado.")
                 + p("Com base no texto, é correto afirmar que"),
    "alternativas": alts("a carne vermelha e a carne de peixe <em>in natura</em> são excelentes fontes de vitamina C.",
                         "a absorção de ferro é inibida pelo consumo de café quando este é consumido logo após as refeições.",
                         "a coloração avermelhada da beterraba é uma evidência da abundância de ferro nesse vegetal.",
                         "o consumo de ovos, ricos em vitamina C, elimina a anemia, doença que afeta grande parte da humanidade.",
                         "o leite é um alimento rico em cálcio que potencializa a absorção de ferro pelo organismo quando consumido logo após as refeições."),
    "explicacao": "<p>O texto cita o café entre os alimentos que inibem a absorção de ferro e recomenda evitá-los “durante ou logo após as refeições”. Alternativa <strong>B</strong>.</p><p>Carnes não são fontes de vitamina C (A). O texto diz que a cor da beterraba não indica muito ferro (C). Ovos não são ricos em vitamina C (D). E o leite, rico em cálcio, inibe a absorção de ferro (E).</p>"},
4: {"materia": "Biologia", "assunto": "Fisiologia humana", "tags": ["sais minerais"],
    "enunciado": p("Os sais inorgânicos desempenham variadas funções nos organismos de todos os seres vivos.", "Assinale a alternativa que associa corretamente o elemento químico presente no sal às respectivas funções que desempenha nos organismos humanos."),
    "alternativas": alts("Cálcio: ajuda a formar o esqueleto, atua na contração muscular e na coagulação sanguínea.",
                         "Cloro: faz parte dos hormônios da tireoide, que controlam o metabolismo, e atua na formação dos ossos e dos dentes.",
                         "Ferro: está presente nas estruturas que realizam a transferência de energia dentro da célula (ATP e ADP) e nos ácidos nucleicos.",
                         "Fósforo: participa da constituição da hemoglobina e de enzimas da respiração celular.",
                         "Iodo: participa da produção da melanina, pigmento que dá cor à pele, e do funcionamento do sistema nervoso."),
    "explicacao": "<p>O <strong>cálcio</strong> forma ossos e dentes, é necessário para a contração dos músculos e participa da coagulação do sangue. Alternativa <strong>A</strong>.</p><p>Quem faz parte dos hormônios da tireoide é o iodo (B). O fósforo está no ATP, no ADP e nos ácidos nucleicos (C). O ferro forma a hemoglobina (D). E a melanina não depende do iodo (E): as alternativas B a E trocam as funções entre os elementos.</p>"},
5: {"materia": "Física", "assunto": "Pressão", "tags": ["conversão de unidades"],
    "enunciado": p("Durante a mastigação de um alimento sólido, os dentes molares de uma pessoa adulta podem exercer uma pressão aproximada de 5 kgf/cm<sup>2</sup> sobre o alimento.",
                   "Sabendo que <strong>kgf/cm<sup>2</sup></strong> equivale à unidade de medida <strong>bar</strong>, assinale a alternativa que apresenta corretamente a pressão exercida pelos molares de uma pessoa adulta em <strong>N/m<sup>2</sup></strong> (ou <strong>Pa</strong>).")
                 + apoio("<em>Considere:</em><br><em>1 bar = 100 000 Pa</em>"),
    "alternativas": alts("5,0 × 10<sup>6</sup>", "5,0 × 10<sup>5</sup>", "5,0 × 10<sup>4</sup>", "1,0 × 10<sup>5</sup>", "1,0 × 10<sup>6</sup>"),
    "explicacao": "<p>Como 1 kgf/cm² equivale a 1 bar, 5 kgf/cm² = 5 bar. E 5 bar = 5 · 100 000 Pa = <strong>5,0 × 10<sup>5</sup> Pa</strong>. Alternativa <strong>B</strong>.</p><p>1,0 × 10⁵ Pa é a pressão de 1 bar só (D). As demais erram a potência de dez.</p>"},
6: {"materia": "Geografia", "assunto": "Agropecuária", "tags": MULTI + ["queijo artesanal"],
    "enunciado": CANASTRA + P6,
    "alternativas": alts("o isolamento geográfico da Serra da Canastra, aliado a condições ambientais desfavoráveis, como a má qualidade do pasto, prejudicam a qualidade do queijo ali produzido e, consequentemente, diminuem as oportunidades econômicas da região.",
                         "as indústrias de pão de queijo instaladas na região provocaram a extinção dos modos de produção artesanal, o que valorizou o queijo da Serra da Canastra nos mercados interno e externo.",
                         "nos últimos anos, a produção de queijo, na Serra da Canastra, adotou tecnologia de ponta para mecanizar a indústria, o que provocou a valorização do produto no mercado internacional.",
                         "os saberes envolvidos na produção do queijo foram trazidos ao Brasil Colônia pelos portugueses e chegaram à Serra da Canastra há duzentos anos, sendo preservados principalmente pelas mulheres.",
                         "o diferencial do queijo da Serra da Canastra é a utilização de leite pasteurizado que, submetido aos processos tradicionais de fermentação, produz um queijo de sabor ímpar."),
    "explicacao": "<p>O texto diz que os portugueses trouxeram o conhecimento para o Brasil Colônia, que ele chegou à Canastra “há dois séculos” e que, nos sítios familiares, “quem em geral faz o queijo são as mulheres”. Alternativa <strong>D</strong>.</p><p>O pasto não é descrito como ruim, e sim como o que define o teor de proteína e gordura do leite (A). A produção artesanal não foi extinta, e as fábricas de pão de queijo compravam o queijo barato (B). O texto não fala em mecanização (C). E o leite é usado <em>sem</em> pasteurização (E).</p>"},
7: {"materia": "Biologia", "assunto": "Microbiologia", "tags": ["fermentação"],
    "enunciado": CANASTRA + p("A produção dos queijos da Serra da Canastra se caracteriza, principalmente,"),
    "alternativas": alts("pelo emprego de leite não pasteurizado e que, portanto, não apresenta os micro-organismos naturais responsáveis pelas reações bioquímicas de fabricação desses produtos.",
                         "pela adição do coalho, conhecido como “pingo”, cheio de bactérias que atuam na coagulação do leite devido à hidrólise das caseínas.",
                         "pela adição de sal no processo de cura, que acelera a multiplicação de bactérias e de leveduras no soro, o qual é totalmente eliminado da massa do queijo.",
                         "pela ação das leveduras, que são fungos autotróficos, responsáveis pela produção da lactose e de outros açúcares do leite.",
                         "pela degradação do açúcar do leite devido à ação das bactérias, que são micro-organismos fundamentais para a formação do sabor e do aroma característicos desse tipo de queijo."),
    "explicacao": "<p>O texto diz que, ao longo do processo, “as bactérias consomem o açúcar do leite” e que a morte delas libera substâncias “responsáveis por reforçar o aroma e o sabor”. Alternativa <strong>E</strong>.</p><p>O leite cru é usado justamente porque <em>tem</em> os micro-organismos naturais (A). O “pingo” é o fermento lácteo, não o coalho (B). O sal desidrata e extermina as bactérias, não acelera sua multiplicação (C). E leveduras são heterotróficas e consomem açúcares, não os produzem (D).</p>"},
8: {"materia": "Geografia", "assunto": "Agropecuária", "tags": ["pecuária extensiva"],
    "enunciado": apoio("A pecuária consiste na criação de animais para a comercialização, principalmente para a obtenção de matérias-primas, como a carne, o leite, o couro, entre outras. Dentro da pecuária, destaca-se a existência de dois sistemas de criação: o extensivo e o intensivo.")
                 + url("https://tinyurl.com/3y6rf989", "26.03.2023") + p("O sistema extensivo"),
    "alternativas": alts("consiste na criação do gado solto em grandes áreas, e a dieta dos animais é baseada majoritariamente em pastagem e suplementos minerais.",
                         "usa métodos avançados de preparo do solo e de cultivo das forrageiras de modo que a exploração deste recurso se dá por um tempo maior.",
                         "possui uma estratégia nutricional avançada, que, combinada a outras tecnologias alimentares, melhora a produtividade do rebanho.",
                         "cria os animais em um sistema de confinamento, colocando o maior número de cabeças de gado no menor espaço possível.",
                         "utiliza inseminação artificial, maquinários computadorizados, agrotóxicos e fertilizantes de alto desempenho."),
    "explicacao": "<p>Na pecuária <strong>extensiva</strong>, o gado é criado solto em grandes áreas e se alimenta sobretudo de pasto, com pouca tecnologia e baixa produtividade por área. Alternativa <strong>A</strong>.</p><p>Preparo avançado do solo, estratégia nutricional, confinamento e alta tecnologia caracterizam a pecuária <strong>intensiva</strong> (B, C, D e E).</p>"},
9: {"materia": "Inglês", "assunto": "Interpretação de texto",
    "enunciado": AGRO + P9,
    "alternativas": alts("mais árvores em fazendas para sombrear a cultura de café.", "reflorestamento e plantações, mas sem a produção de carne.", "proteção ambiental com a retirada do pasto e da criação de gado.",
                         "plantio de alimentos orgânicos, mas sem extração de madeira.", "proteção dos ecossistemas pela coexistência entre plantações e árvores."),
    "explicacao": "<p>O texto define <em>Agroforestry</em> como “a interação entre agricultura e árvores” e diz que o sistema busca equilibrar a produção de madeira, a de alimentos e a proteção do ambiente: plantações e árvores convivem, e os ecossistemas são protegidos. Alternativa <strong>E</strong>.</p><p>O café é só um exemplo, e sombrear não é o objetivo (A). O texto prevê árvores dando forragem para o gado, não a retirada da criação (B e C). E a produção de madeira (<em>timber</em>) é um dos objetivos (D).</p>"},
10: {"materia": "Inglês", "assunto": "Coesão e referência", "tags": ["conectivos"],
     "enunciado": p("Na sentença destacada em negrito no texto, a expressão “so that” expressa a ideia de"), "apoio_de": (9, P9),
     "alternativas": alts("causa.", "contrariedade.", "ênfase.", "exemplificação.", "finalidade."),
     "explicacao": "<p><em>So that</em> significa “para que”, “de modo que”: proteger o ambiente <em>para que</em> ele continue fornecendo recursos. Expressa <strong>finalidade</strong>. Alternativa <strong>E</strong>.</p><p>Causa seria <em>because</em> (A), contrariedade, <em>although</em> ou <em>but</em> (B), e exemplificação, <em>for example</em> ou <em>such as</em> (D). <em>So that</em> não é marca de ênfase (C).</p>"},
11: {"materia": "História", "assunto": "Brasil Colônia", "tags": ["ciclo do açúcar"],
     "enunciado": apoio(*T(6, "No Recife, em Pernambuco, há quase 500 anos", "infinidade de guloseimas.", ["Caju, umbu, ubaia", "O São João é o palco"]))
                  + url("https://tinyurl.com/mrywcm7k", "09.03.2023") + p("A partir das informações apresentadas no texto, é correto afirmar que"),
     "alternativas": alts("o consumo de açúcar em Pernambuco ocorre uma vez por ano, durante a celebração a São João, quando a população tem acesso aos doces de festa.",
                          "a “civilização do açúcar” surgiu após a abolição da mão de obra escravizada na Zona da Mata, devido ao volume de produção de frutas nativas.",
                          "a necessidade de produzir e de consumir doces fez com que os pernambucanos inventassem uma forma de extrair açúcar a partir das frutas nativas, como o caju e a guabiraba.",
                          "a “civilização do açúcar” foi construída a partir da utilização de mão de obra negra escravizada, que produzia o açúcar na região litorânea de Pernambuco, conhecida como Zona da Mata.",
                          "o cultivo de açúcar, na Zona da Mata, foi responsável pelo esgotamento do solo, que teve como consequência a extinção da guabiraba, fruta de safra curta cujo doce só se come uma vez por ano."),
     "explicacao": "<p>O texto diz que a “civilização do açúcar” foi “forjada na mão de obra de negros escravizados sobre os massapés da Zona da Mata”, a faixa litorânea de Pernambuco. Alternativa <strong>D</strong>.</p><p>Só o doce de guabiraba se come uma vez por ano (A e E), e a fruta está rara, não extinta (E). A civilização do açúcar começou no período colonial, com a escravidão, não depois da abolição (B). E o açúcar vem da cana; as frutas viram doces com ele (C).</p>"},
12: {"materia": "Matemática", "assunto": "Geometria espacial", "tags": ["tronco de pirâmide", "área total"],
     "enunciado": p("No comércio de alimentação, a embalagem compõe a identidade visual do produto. Um exemplo disso é a clássica caixinha de entrega de comida chinesa.",
                    "A figura apresenta a vista lateral, a vista da parte inferior e a vista da parte superior desse tipo de embalagem.") + "[[fig:1]]"
                  + p("Leia o texto e assinale a alternativa cujos termos completam, correta e respectivamente, as lacunas.")
                  + apoio("Com base nas vistas fornecidas, é correto afirmar que a embalagem tem o formato de um ____<strong>(I)</strong>____, e que a área total de material necessário para a confeccionar pode ser estimada em cerca de ____<strong>(II)</strong>____ cm<sup>2</sup>, sem levar em consideração as dobras de fechamento e de colagem."),
     "imagens": figs(("q12", "Três vistas da caixinha: vista lateral, um trapézio isósceles com a base maior em cima e o lado inclinado medindo 13 cm; vista da parte inferior, um quadrado de 10 cm de lado; vista da parte superior, um quadrado de 20 cm de lado.")),
     "alternativas": colunas(["I", "II"], [["prisma", "680"], ["tronco de pirâmide", "680"], ["prisma", "1 220"], ["tronco de pirâmide", "1 220"], ["prisma", "1 280"]]),
     "explicacao": "<p>As bases são quadrados de tamanhos diferentes (10 cm e 20 cm) ligados por faces em forma de trapézio: é um <strong>tronco de pirâmide</strong>. Para a área, o gabarito considera os 13 cm como a aresta lateral. Cada face é um trapézio isósceles de bases 10 e 20; a altura h da face sai de um triângulo retângulo de hipotenusa 13 e cateto (20 − 10) ÷ 2 = 5: h = √(13² − 5²) = 12 cm.</p><p>Área lateral: 4 · (10 + 20) ÷ 2 · 12 = 720 cm². Bases: 10² + 20² = 100 + 400 = 500 cm². Total: 720 + 500 = <strong>1 220 cm²</strong>. Alternativa <strong>D</strong>.</p><p>Um prisma teria as duas bases iguais (A, C e E). 680 cm² esquece as bases ou parte das faces (A e B). E 1 280 cm² vem de usar 13 cm como altura da face (E).</p>"},
13: {"materia": "Física", "assunto": "Ondas", "tags": ["espectro visível"],
     "enunciado": p("Três ex-alunas de marketing da FATEC montam um ensaio fotográfico com algumas frutas. Para isso, utilizam uma lâmpada de LED como iluminação de apoio. Essa lâmpada de LED tem um dispositivo eletrônico que permite controlar a emissão de luz em diferentes comprimentos de onda, apresentados em angström (Å), e diferentes frequências, apresentadas em terahertz, conforme apresentado no quadro.")
                  + tabela(["Cor", "Faixa de comprimento de onda “λ” (Å)", "Faixa de frequência “<em>f</em>” (THz)"],
                           [["<em>Violeta</em>", "3 900 ≤ λ &lt; 4 500", "769 ≥ <em>f</em> &gt; 665"], ["<em>Anil</em>", "4 500 ≤ λ &lt; 4 550", "665 ≥ <em>f</em> &gt; 659"], ["<em>Azul</em>", "4 550 ≤ λ &lt; 4 920", "659 ≥ <em>f</em> &gt; 610"],
                            ["<em>Verde</em>", "4 920 ≤ λ &lt; 5 770", "610 ≥ <em>f</em> &gt; 520"], ["<em>Amarelo</em>", "5 770 ≤ λ &lt; 5 970", "520 ≥ <em>f</em> &gt; 503"], ["<em>Alaranjado</em>", "5 970 ≤ λ &lt; 6 220", "503 ≥ <em>f</em> &gt; 482"], ["<em>Vermelho</em>", "6 220 ≤ λ ≤ 7 800", "482 ≥ <em>f</em> ≥ 384"]])
                  + p(*T(7, "Para esse ensaio fotográfico, as alunas", "nas imagens produzidas."),
                      "Assim, podemos afirmar corretamente que, durante a produção das diferentes imagens, a lâmpada emitiu ondas eletromagnéticas que"),
     "alternativas": alts("operavam na faixa de 384 THz a 659 THz.", "vibravam na faixa de 482 THz a 800 THz.", "oscilavam na faixa de 4 920 Å a 7 800 Å.", "estavam na faixa de 3 900 Å a 5 970 Å.", "giravam na faixa de 384 THz a 3 900 Å."),
     "explicacao": "<p>Os morangos são vermelhos, as bananas, amarelas, e os limões, verdes. A luz precisa ir do verde ao vermelho: de 4 920 Å (início do verde) a 7 800 Å (fim do vermelho). Alternativa <strong>C</strong>.</p><p>Em frequência, essa faixa iria de 384 THz a 610 THz; 659 THz já inclui o azul e o anil (A). B inclui violeta, anil e azul e passa do limite da tabela. D vai do violeta ao amarelo, sem o vermelho. E mistura frequência com comprimento de onda.</p>"},
14: {"materia": "História", "assunto": "América colonial", "tags": ["cacau", "trocas coloniais"],
     "enunciado": p("Observe o mapa que apresenta as rotas de difusão de um produto alimentício.") + "[[fig:1]]"
                  + fonte("Fonte das Informações: FERRÃO, J. E. M.; <em>A aventura das plantas e os descobrimentos portugueses</em>. Lisboa: Instituto de Investigação Científica Tropical, 2005. p.287.")
                  + p("O processo histórico que explica o fenômeno expresso no mapa é"),
     "imagens": figs(("q14", "Mapa-múndi com uma mancha sobre a América Central e o norte da América do Sul, de onde partem setas: para a Europa (Espanha e, dali, outros países), para o sul da América do Sul, para o Oceano Pacífico, para a costa ocidental da África e, por outra rota, até o Sudeste Asiático, nas Filipinas e na Indonésia.")),
     "alternativas": alts("a expansão chinesa no Sudeste da Ásia que, há cerca de 5 000 anos, resultou no desenvolvimento da cultura do arroz, principal alimento da região até a atualidade.",
                          "o transporte de pimenta, produzida na Índia, para as Américas e para a Europa, realizado pelas companhias comerciais holandesas e inglesas, no século XVIII.",
                          "o envio de mudas de café da Etiópia para o Iêmen, onde ele passou a ser produzido comercialmente por volta de 575 d.C., principalmente para consumo interno.",
                          "a ampliação da cultura persa, na Ásia e na África, levando à popularização do consumo de gergelim nas regiões da Malásia e da Indonésia, a partir de 4 300 a.C.",
                          "a difusão do cacau por grande parte do mundo a partir do século XVI, devido à atividade comercial realizada pelos colonizadores espanhóis da América."),
     "explicacao": "<p>As rotas partem da América Central e do norte da América do Sul, região de origem do <strong>cacau</strong>, cultivado por maias e astecas. Depois da conquista, no século XVI, os espanhóis o levaram à Europa, e dali ele se espalhou para a África e a Ásia. Alternativa <strong>E</strong>.</p><p>O arroz e o gergelim não partem da América (A e D). A pimenta saía da Índia, não da América (B). E o café se espalhou a partir da Etiópia, na África (C).</p>"},
15: {"materia": "Matemática", "assunto": "Porcentagem",
     "enunciado": PIZZA + P15, "imagens": PIZZA_IMG,
     "alternativas": alts("1", "5", "8", "11", "13"),
     "explicacao": "<p>A cada 100 paulistanos, 45 pediram pizza da cobertura predileta. Desses, 17,7% preferem portuguesa: 45 · 0,177 ≈ 7,97, ou seja, cerca de <strong>8</strong> pessoas. Alternativa <strong>C</strong>.</p><p>Tomar 17,7% de 100, sem considerar os 45%, daria 18. Os outros valores não saem da conta.</p>"},
16: {"materia": "Matemática", "assunto": "Estatística", "tags": ["média, moda e mediana"],
     "enunciado": p("Ao analisar os dados numéricos do gráfico, é correto afirmar, sobre eles, que a"), "apoio_de": (15, P15),
     "alternativas": alts("média é maior que a moda.", "moda é igual a 17,7 %.", "moda é maior que a mediana.", "mediana é igual a 14,7 %.", "mediana é maior que a média."),
     "explicacao": "<p>Os valores são 24,3; 17,7; 14,7; 14,7 e 28,6. A <strong>moda</strong> é 14,7 (aparece duas vezes). Em ordem, 14,7; 14,7; 17,7; 24,3; 28,6, a <strong>mediana</strong> é 17,7. A <strong>média</strong> é 100 ÷ 5 = 20. Como 20 &gt; 14,7, a média é maior que a moda. Alternativa <strong>A</strong>.</p><p>A moda é 14,7, não 17,7 (B), e é menor que a mediana (C). A mediana é 17,7 (D) e é menor que a média (E).</p>"},
17: {"materia": "Matemática", "assunto": "Geometria plana", "tags": ["área do círculo"],
     "enunciado": p("Ao se comparar a área de um disco de pizza de São Paulo à área de um disco de pizza de Nápoles, percebemos que o primeiro excede o segundo.",
                    "Adotando π = 3, é possível concluir corretamente que a diferença entre as áreas calculadas é, em cm<sup>2</sup>, aproximadamente, de"),
     "apoio_de": (15, P15),
     "alternativas": alts("6,51.", "9,75.", "19,50.", "103,19.", "309,56."),
     "explicacao": "<p>Os raios são 35 ÷ 2 = 17,5 cm e 28,5 ÷ 2 = 14,25 cm. A diferença das áreas é π(17,5² − 14,25²) = 3 · (306,25 − 203,0625) = 3 · 103,1875 ≈ <strong>309,56 cm²</strong>. Alternativa <strong>E</strong>.</p><p>103,19 é a conta sem multiplicar por π (D). 19,50 e 9,75 vêm de usar diâmetro ou raio sem elevar ao quadrado (C e B), e 6,51 é um valor sem relação com as áreas (A).</p>"},
18: {"materia": "Raciocínio lógico", "assunto": "Sequências", "tags": ["ordem alfabética"],
     "enunciado": p(*T(9, "Em uma feira livre, um cliente percebeu", "comercializados pela terceira barraca são", ["Na primeira barraca", "Considere que as barracas", "É correto afirmar que, dentre"])),
     "alternativas": alts("abacaxis.", "doces.", "hortaliças.", "legumes.", "tubérculos."),
     "explicacao": "<p>Os produtos seguem a ordem alfabética das iniciais: <strong>B</strong>anana, <strong>C</strong>oco, ?, <strong>E</strong>speciarias, <strong>F</strong>lores. A terceira barraca vende algo com a letra D: <strong>doces</strong>. Alternativa <strong>B</strong>.</p><p>Abacaxis (A), hortaliças (H), legumes (L) e tubérculos (T) não se encaixam entre C e E (A, C, D e E).</p>"},
19: {"materia": "História", "assunto": "Escravidão", "tags": ["cultura afro-brasileira"],
     "enunciado": apoio(*T(9, "Uma especialidade da gastronomia brasileira", "pelas filhas-de-santo."))
                  + url("https://tinyurl.com/5e7ydhww", "09.03.2023") + p("O bolinho e a religiosidade relacionada a ele remetem"),
     "alternativas": alts("à vinda de povos árabes que, no final do século XIX, fugiram de perseguições religiosas e tornaram-se mascates nas grandes cidades e nas fazendas do interior do país.",
                          "à chegada do primeiro grupo de imigrantes japoneses, no início do século XX, na fazenda Santo Antônio, onde se cultivava feijão para a produção de bolinhos doces e salgados.",
                          "aos deslocamentos dos tropeiros, que percorriam as estradas transportando carne seca para os moradores das regiões de extração de ouro e diamantes em Minas Gerais.",
                          "à escravização de pessoas africanas para a produção de açúcar, a mineração de ouro e o plantio de café, entre outros, nos períodos colonial e imperial da história do Brasil.",
                          "à intensa imigração de mexicanos, em 1848, motivada pelo Tratado de Guadalupe Hidalgo, que trouxe para o Brasil pratos típicos à base de feijão, como o taco."),
     "explicacao": "<p>O acarajé, frito no azeite de dendê e ligado às religiões de matriz africana (preparado pelas filhas-de-santo do candomblé), chegou com os <strong>africanos escravizados</strong> trazidos ao Brasil nos períodos colonial e imperial. Alternativa <strong>D</strong>.</p><p>O acarajé não tem origem árabe (A), japonesa (B), tropeira (C) nem mexicana (E).</p>"},
20: {"materia": "Raciocínio lógico", "assunto": "Sequências", "tags": ["calendário"],
     "enunciado": p(*T(10, "Todos os dias, Alex e sua família consomem", "consumir todas as unidades de leite da embalagem comprada.", ["Em uma segunda-feira, antes", "Assinale a alternativa que apresenta"])),
     "alternativas": alts("Sexta-feira", "Sábado", "Domingo", "Segunda-feira", "Terça-feira"),
     "explicacao": "<p>A família consome 500 + 250 = 750 mL por dia. Os 12 litros duram 12 000 ÷ 750 = 16 dias, começando na segunda-feira. O 16º dia é 15 dias depois da segunda: 15 = 2 · 7 + 1, então cai um dia depois da segunda, na <strong>terça-feira</strong>. Alternativa <strong>E</strong>.</p><p>Contar 16 dias <em>depois</em> da segunda, em vez de contar a segunda como o 1º dia, daria quarta-feira, que não está nas alternativas.</p>"},
21: {"materia": "Português", "assunto": "Conectivos",
     "enunciado": ARADO + P21,
     "alternativas": alts("“como” (I) é conjunção e expressa relação de causa, podendo ser substituída por “conforme”.",
                          "“por” (II) é preposição e expressa relação de consequência, podendo ser substituída por “por causa de”.",
                          "“para” (III) é preposição e expressa ideia de origem, podendo ser substituída por “de”.",
                          "“que” (IV) é pronome e retoma o substantivo “o cacto”, podendo ser substituído por “cujo”.",
                          "“para” (V) é preposição e expressa finalidade, podendo ser substituída por “a fim de”."),
     "explicacao": "<p>Em “contar com a solidariedade de um vizinho <strong>para</strong> garantir o cortado na mesa”, a preposição indica o objetivo: pode ser trocada por “a fim de” sem mudar o sentido. Alternativa <strong>E</strong>.</p><p>“Como” (I) significa “como sendo”, não causa (A). “Por” (II) indica causa, não consequência (B). “Para” (III) indica destino, não origem (C). E “que” (IV) é pronome relativo, mas não pode virar “cujo”, que indica posse (D).</p>"},
22: {"materia": "Português", "assunto": "Texto literário", "tags": ["narrativa"],
     "enunciado": p("Sobre o texto, é correto afirmar que"), "apoio_de": (21, P21),
     "alternativas": alts("o armazenamento de alimentos perecíveis, como grãos, junto à certeza da permanência no emprego, garantiu a sobrevivência e o bem-estar dos trabalhadores.",
                          "a crise enfrentada fez com que os moradores do local esgotassem as riquezas naturais da floresta, levando, consequentemente, à exaustão das águas de rios e mares.",
                          "a narrativa segue a ordem cronológica e retrata o agravamento da crise cujo ápice se dá quando se recorre ao consumo de alimento destinado aos animais.",
                          "o narrador, que não participa da história, retrata um momento difícil da vivência de sua comunidade devido à fome gerada pela seca.",
                          "a produção de feijão e umbu, por ser destinada ao consumo doméstico dos trabalhadores, resistiu ao período de estiagem."),
     "explicacao": "<p>Os fatos são narrados em sequência (“Depois secaram...”, “Depois veio o medo...”, “Agora, mais que antes...”) e a situação piora até o ponto em que as famílias disputam a palma com o gado. Alternativa <strong>C</strong>.</p><p>Grãos não são perecíveis, e havia o medo de perder o emprego (A). O texto não fala de floresta nem de mares (B). O narrador participa da história, em primeira pessoa (D). E o feijão e os umbuzeiros também secaram (E).</p>"},
23: {"materia": "Biologia", "assunto": "Botânica", "tags": MULTI + ["adaptações à seca", "palma"],
     "enunciado": p("No texto, o vegetal utilizado como alimento para humanos e animais, durante o período da estiagem, caracteriza-se por"), "apoio_de": (21, P21),
     "alternativas": alts("possuir hastes parecidas com as de outros grãos, como aveia, e se adaptar bem a ambientes aquáticos.",
                          "possuir folhas modificadas que evitam a perda de água por transpiração, adaptando-se bem a ambientes secos.",
                          "fornecer sombra devido à copa frondosa e armazenar, em suas raízes, até mil litros de água, sendo seu fruto conhecido como umbu.",
                          "ser um arbusto, cujas raízes, com tecido interno branco ou amarelado, podem ser consumidas ou utilizadas na fabricação de farinha.",
                          "ser uma gramínea com troncos fortes, que podem alcançar até cinco metros de altura e que podem ser utilizados na fabricação de açúcar."),
     "explicacao": "<p>O vegetal é a <strong>palma</strong>, um cacto. Nos cactos, as folhas são transformadas em espinhos, o que reduz a perda de água por transpiração e adapta a planta a ambientes secos. Alternativa <strong>B</strong>.</p><p>A descreve o arroz, C, o umbuzeiro, D, a mandioca, e E, a cana-de-açúcar, todas citadas no texto, mas nenhuma é o cacto.</p>"},
24: {"materia": "Português", "assunto": "Gêneros textuais", "tags": ["charge"],
     "enunciado": p("Analise a charge.") + "[[fig:1]]" + url("https://tinyurl.com/y2c99r6m", "10.03.2023", "Original colorido.")
                  + p("A charge utiliza a linguagem verbal e não verbal na construção de uma"),
     "imagens": figs(("q24", "Charge: a bandeira do Brasil desenhada como uma toalha de mesa. No lugar do círculo azul central há um prato vazio, com garfo e faca ao lado. Um homem magro, de olhos arregalados, sai por um buraco no meio do prato, olhando em volta com pontos de interrogação sobre a cabeça. Embaixo, uma mão esquelética agarra a ponta da toalha.")),
     "alternativas": alts("narrativa sintética, pois estão implícitas as ações desempenhadas pelo personagem cuja biografia representa o sucesso das políticas sociais do país.",
                          "crítica social, pois tematiza a fome na sociedade brasileira, evidenciada pelo prato vazio no lugar da esfera celeste da bandeira nacional.",
                          "descrição mimética, devido à caracterização fiel da realidade vivenciada por cidadãos pobres ao redor do mundo.",
                          "crônica reflexiva, já que o autor evidencia um posicionamento imparcial sobre o aumento da segurança alimentar no Brasil.",
                          "caricatura, pois há uma distorção exagerada de uma realidade individual amplificada grotescamente para gerar humor no leitor."),
     "explicacao": "<p>A charge troca o círculo da bandeira por um prato vazio e mostra um homem faminto: é uma <strong>crítica social</strong> à fome no Brasil. Alternativa <strong>B</strong>.</p><p>A imagem denuncia o fracasso, não o sucesso, das políticas sociais (A). Ela trata do Brasil, com recursos simbólicos, não de uma descrição fiel do mundo todo (C). A charge não é imparcial e fala de insegurança alimentar (D). E o foco é um problema coletivo, não a caricatura de uma pessoa (E).</p>"},
25: {"materia": "História", "assunto": "Idade Média", "tags": ["crise do século XIV"],
     "enunciado": apoio(*T(11, "A partir do século XIV, os períodos", "dado origem a pestes epidêmicas.", ["Em Flandres, cerca de 10"]))
                  + fonte("ARARIBÁ PLUS: <em>História</em>. 4ª ed. São Paulo: Moderna, 2014. p. 99-100. Adaptado.") + p("Segundo o texto,"),
     "trocar": [("da opulação", "da população")],
     "alternativas": alts("a estiagem ocorrida entre 1314 e 1319 possibilitou o aumento da produção e promoveu o desenvolvimento econômico do continente.",
                          "o início do século XIV marcou o fim dos períodos de más colheitas e as fortes chuvas provocaram um aumento da produção agrícola.",
                          "em Winchester, os efeitos da fome não foram sentidos, já que o número de mortos manteve-se o mesmo nos anos de 1310 e 1317.",
                          "em Flandres, um quinto da população morreu por inanição devido ao rápido aumento dos preços dos alimentos, principalmente do trigo.",
                          "na França, a falta de alimentos deu origem a epidemias, já que parte da população se alimentou de animais que morreram doentes."),
     "explicacao": "<p>O texto relata que, no Baixo Reno, na França, as populações chegaram a comer animais mortos por doenças, “o que teria dado origem a pestes epidêmicas”. Alternativa <strong>E</strong>.</p><p>O problema de 1314 a 1319 foram chuvas fortes, não estiagem, e a produção caiu (A e B). Em Winchester, as mortes de 1317 foram o dobro das de 1310 (C). E em Flandres morreram cerca de 10% da população, não um quinto (D).</p>"},
26: {"materia": "Inglês", "assunto": "Interpretação de texto",
     "enunciado": FAO + P26, "imagens": FAO_IMG,
     "alternativas": alts("a falta de alimentos nutritivos eleva a fome.", "“fome” e “insegurança alimentar” são sinônimos.", "“fome” e “desnutrição” definem o mesmo conceito.",
                          "a alimentação de baixa caloria leva à insegurança alimentar.", "o comprometimento alimentar implica acesso diário ao alimento."),
     "explicacao": "<p>O texto diz que “<em>hunger</em> may also be referred to as <em>undernourishment</em>”: fome e desnutrição (subnutrição) são tratadas como o mesmo conceito. Alternativa <strong>C</strong>.</p><p>A fome é definida pelo consumo insuficiente de calorias, não pela falta de alimentos nutritivos (A). Fome e insegurança alimentar são conceitos diferentes (B). A insegurança alimentar é a falta de acesso regular a alimentos, não a dieta de baixa caloria (D). E abrir mão da qualidade (<em>compromising</em>) é uma etapa da insegurança, não garante acesso diário (E).</p>"},
27: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": ["infográfico"],
     "enunciado": p("Considerando o infográfico, a insegurança alimentar severa se caracteriza por"), "apoio_de": (26, P26),
     "alternativas": alts("sensação de fome e de desconforto por um dia.", "sensação de desconforto e baixa ingestão de alimentos.", "falta de acesso ao alimento por um dia inteiro várias vezes ao ano.",
                          "baixa ingestão de calorias e ocorrência de apenas uma refeição diária.", "incerteza de ingestão de alimentos calóricos em horários padronizados."),
     "explicacao": "<p>Segundo o infográfico, na insegurança <em>severe</em> a pessoa “<em>has run out of food</em>” e “<em>gone an entire day without eating at times during the year</em>”: ficou sem comida por um dia inteiro algumas vezes no ano. Alternativa <strong>C</strong>.</p><p>A e B descrevem a fome, não a escala FIES. Pular refeições e incerteza sobre o acesso ao alimento são marcas da insegurança moderada (D e E).</p>"},
28: {"materia": "Inglês", "assunto": "Vocabulário",
     "enunciado": p("O vocábulo “lack”, na sentença destacada em negrito no texto, significa"), "apoio_de": (26, P26),
     "alternativas": alts("“ter”.", "“trazer”.", "“manter”.", "“penar”.", "“faltar”."),
     "explicacao": "<p><em>Lack</em> significa “faltar”, “não ter”: a pessoa está em insegurança alimentar quando lhe <strong>falta</strong> acesso regular a comida suficiente, segura e nutritiva. Alternativa <strong>E</strong>.</p><p>“Ter” seria <em>have</em> (A), “trazer”, <em>bring</em> (B), “manter”, <em>keep</em> (C), e “penar”, <em>suffer</em> (D).</p>"},
29: {"materia": "Português", "assunto": "Semântica", "tags": ["provérbios"],
     "enunciado": p("Leia os provérbios.")
                  + apoio("I. Resto de uns, comida de outros.<br>II. Quando a comida tarda, a fome é boa mostarda.<br>III. O amor morre mais de indigestão do que de fome.<br>IV. A fome é o melhor tempero.<br>V. A fome faz sair o lobo do covil.")
                  + p("Analisando-os, pode concluir-se corretamente que"),
     "alternativas": alts("são todos formados por construções nominais cujo sentido se articula por análise do contexto de ocorrência.",
                          "são todos construídos de forma prolixa, usando o presente do indicativo para expressar ações habituais do cotidiano brasileiro.",
                          "os provérbios I e III, embora usem vocabulário relacionado ao universo da alimentação, são metáforas sobre o excesso de expressões sentimentais.",
                          "o provérbio V pode ser parafraseado pela máxima “farinha pouca, meu pirão primeiro”, ambos expressando a cautela necessária em momentos de dificuldades.",
                          "os provérbios II e IV são semelhantes, pois a expressão “comida tarda” aproxima-se semanticamente de “fome” e “boa mostarda”, de “melhor tempero”."),
     "explicacao": "<p>Os provérbios II e IV dizem a mesma coisa: quem tem fome acha qualquer comida saborosa. Em II, a comida que tarda (que gera fome) corresponde à fome de IV, e a “boa mostarda” corresponde ao “melhor tempero”. Alternativa <strong>E</strong>.</p><p>Só o provérbio I é uma construção nominal, sem verbo (A). Provérbios são concisos, não prolixos (B). O provérbio I fala de aproveitar sobras, não de sentimentos (C). E o V fala de a necessidade obrigar a agir, enquanto “farinha pouca, meu pirão primeiro” fala de egoísmo (D).</p>"},
30: {"materia": "Matemática", "assunto": "Equações", "tags": ["sistema de equações", "oferta e demanda"],
     "enunciado": apoio("Considere que:<br>• oferta é a quantidade de um produto que está disponível para compra, e<br>• demanda é a quantidade desse mesmo produto que os consumidores estão dispostos a comprar.")
                  + p("Uma pesquisa de mercado definiu duas equações que descrevem matematicamente a oferta e a demanda por um determinado produto:",
                      "• a equação de oferta determinada foi q<sub>o</sub> = 3p + 50 e relaciona o número de unidades (q<sub>o</sub>) que vendedores estão dispostos a comercializar em função do preço (p), em reais, desse produto; e",
                      "• a equação de demanda foi descrita pela expressão por q<sub>d</sub> = –2p + 500 que relaciona o número de unidades (q<sub>d</sub>) que consumidores estão propensos a adquirir em função do mesmo preço (p), em reais, desse produto.",
                      "O preço que iguala a quantidade ofertada e a quantidade demandada de um produto é denominado preço de equilíbrio de mercado, ou seja, quando q<sub>o</sub> e q<sub>d</sub> se igualam.",
                      "Assinale a alternativa que apresenta, correta e respectivamente, o preço de equilíbrio de mercado do produto e sua quantidade nessa situação."),
     "alternativas": alts("R$ 90,00 e 280 unidades", "R$ 90,00 e 320 unidades", "R$ 90,00 e 380 unidades", "R$ 110,00 e 320 unidades", "R$ 110,00 e 380 unidades"),
     "explicacao": "<p>No equilíbrio, 3p + 50 = –2p + 500, então 5p = 450 e p = 90. A quantidade é q = 3 · 90 + 50 = 320 (confere: –2 · 90 + 500 = 320). Alternativa <strong>B</strong>.</p><p>Com p = 90, nenhuma das equações dá 280 nem 380 (A e C). E p = 110 não iguala as duas quantidades (D e E).</p>"},
31: {"materia": "Química", "assunto": "Substâncias e misturas", "tags": ["fórmula molecular", "cafeína"],
     "enunciado": p("Um dos componentes do café é a cafeína (fórmula: C<sub>8</sub>H<sub>10</sub>N<sub>4</sub>O<sub>2</sub>), cuja ingestão diária de 9,9 g é letal para adultos. Considere que um adulto ingere diariamente <strong><em>n</em></strong> xícaras de café e que cada xícara contém 180 mg de cafeína.",
                    "Com base no texto, é correto afirmar que o número de elementos químicos presentes na molécula de cafeína e o valor mínimo de <strong><em>n</em></strong>, para que a dose letal seja atingida, são, respectivamente,"),
     "alternativas": alts("4 e 55.", "4 e 125.", "24 e 55.", "24 e 125.", "24 e 160."),
     "explicacao": "<p>A cafeína tem 4 <strong>elementos</strong> diferentes: C, H, N e O (24 é o número de átomos: 8 + 10 + 4 + 2). A dose letal é 9,9 g = 9 900 mg, e 9 900 ÷ 180 = <strong>55</strong> xícaras. Alternativa <strong>A</strong>.</p><p>C, D e E confundem elementos com átomos. E 125 e 160 não saem da divisão (B, D e E).</p>"},
32: {"materia": "Química", "assunto": "Interpretação de dados", "tags": ["porcentagem em massa"],
     "enunciado": p("O quadro relaciona algumas variedades de café à quantidade de cafeína contida em cada uma.")
                  + tabela(["Variedade de café", "Quantidade média de cafeína no café em porcentagem em massa (%)"],
                           [["<em>Coffea arabica</em>", "1,1"], ["<em>Coffea excelsa</em>", "1,9"], ["<em>Coffea liberica</em>", "2,1"], ["<em>Coffea canephora</em>", "2,2"], ["<em>Coffea robusta</em>", "2,4"]])
                  + p("Considere que uma variedade de café de massa 500 g foi analisada e apresentou 11 g de cafeína.", "Com base no quadro fornecido, é correto afirmar que a variedade de café analisada é"),
     "alternativas": alts("<em>Coffea arabica.</em>", "<em>Coffea excelsa.</em>", "<em>Coffea liberica.</em>", "<em>Coffea canephora.</em>", "<em>Coffea robusta.</em>"),
     "explicacao": "<p>A porcentagem em massa é 11 ÷ 500 · 100 = <strong>2,2%</strong>, que corresponde à <em>Coffea canephora</em>. Alternativa <strong>D</strong>.</p><p>As outras variedades têm 1,1%, 1,9%, 2,1% e 2,4% de cafeína (A, B, C e E).</p>"},
33: {"materia": "Química", "assunto": "Ácidos e bases", "tags": ["pH"],
     "enunciado": p("A acidez é uma das características usadas para determinar a qualidade dos diferentes tipos de café. Para definir a acidez dessa bebida, pode-se usar o pH, denominado potencial hidrogeniônico.",
                    "A escala apresenta valores aproximados do pH de diversos materiais a 25 °C.") + "[[fig:1]]"
                  + p("Considere que:", "• pH = –log[H<sup>+</sup>]<br>• [H<sup>+</sup>] = 10<sup>–pH</sup>, sendo [H<sup>+</sup>] a concentração em mol/L dos íons [H<sup>+</sup>] em solução aquosa",
                      "Por exemplo: o ovo tem caráter básico, pois apresenta pH = 8,0. Logo, a [H<sup>+</sup>] = 10<sup>–8</sup> mol/L.",
                      "Analisando duas amostras de café A e B, constatou-se que a amostra A apresenta [H<sup>+</sup>] = 10<sup>–4,8</sup> mol/L, enquanto a amostra B apresenta [H<sup>+</sup>] = 10<sup>–4</sup> mol/L.",
                      "Diante do exposto, pode-se concluir corretamente que a amostra"),
     "imagens": figs(("q33", "Escala de pH com ilustrações: limão, 3,0; tomate, 4,0; abacaxi, 5,0; leite, 6,0; água pura, 7,0; ovo, 8,0; bicarbonato de sódio, 9,0; antiácidos, 10,0; solução amoniacal, 11,0; sabão, 12,0.")),
     "alternativas": alts("B possui pH = 4,0, sendo mais ácida que o limão.", "B possui pH = 4,8, sendo mais ácida que o tomate.", "A possui pH = 4,0, sendo mais ácida que o leite.",
                          "A possui pH = 4,8, sendo mais ácida que o tomate.", "A possui pH = 4,8, sendo mais ácida que o leite."),
     "explicacao": "<p>Pela relação [H⁺] = 10<sup>–pH</sup>, a amostra A tem pH = 4,8 e a B, pH = 4,0. Quanto menor o pH, mais ácida a solução. A amostra A (4,8) é mais ácida que o leite (6,0). Alternativa <strong>E</strong>.</p><p>B tem pH 4,0, menos ácida que o limão (3,0) (A), e não 4,8 (B). A não tem pH 4,0 (C), e com 4,8 é menos ácida que o tomate (4,0) (D).</p>"},
34: {"materia": "Biologia", "assunto": "Ecologia", "tags": ["algas"],
     "enunciado": apoio(*T(15, "As algas podem ser encontradas nos mais variados", "plantas terrestres, pois", ["Na alimentação, as algas", "No setor agroalimentar"]),
                        "• as algas crescem e se multiplicam rapidamente;<br>• não precisam de fertilizantes artificiais, já que absorvem nutrientes resultantes da decomposição de matéria orgânica existente na água;<br>• absorvem, por meio da fotossíntese, o dióxido de carbono da água, sendo uma das principais fontes do gás oxigênio presente na atmosfera; e<br>• ajudam a combater a acidificação dos oceanos.",
                        *T(15, "Umas das preocupações com o aumento", "chumbo, cádmio e mercúrio."))
                  + p("Baseado no texto, é correto afirmar que"),
     "alternativas": alts("as algas, apesar de seu elevado valor nutricional, não servem de alimento para os seres vivos, pois são tóxicas e atuam na decomposição da matéria orgânica dos oceanos.",
                          "as algas se multiplicam lentamente, dependem de fertilizantes artificiais para se desenvolverem e possuem grande capacidade de absorver dióxido de carbono do ar atmosférico.",
                          "o cultivo de algas oceânicas não precisa de terras férteis, ao contrário da agricultura tradicional, pois as algas obtêm da água os nutrientes necessários para o desenvolvimento delas.",
                          "as algas oceânicas usam os metais pesados, provenientes do meio ambiente, para realizar a síntese de compostos orgânicos de elevado valor nutricional e para liberar o gás oxigênio no ambiente.",
                          "o cultivo de algas ricas em metais pesados, cujo consumo é essencial ao organismo humano, tende a aumentar, porque elas são importantes fontes de vitaminas, minerais, arsênio, chumbo, mercúrio e ácidos graxos ômega–3."),
     "explicacao": "<p>O texto diz que as algas “não precisam de fertilizantes artificiais”, pois absorvem os nutrientes da matéria orgânica decomposta na água. Cultivadas no mar, dispensam terras férteis. Alternativa <strong>C</strong>.</p><p>As algas servem de alimento e são consideradas funcionais (A). Elas se multiplicam rápido, sem fertilizantes, e absorvem o CO₂ da água (B). Metais pesados são uma ameaça, não matéria-prima da fotossíntese (D). E arsênio, chumbo e mercúrio são tóxicos, não essenciais (E).</p>"},
35: {"materia": "Raciocínio lógico", "assunto": "Lógica", "tags": ["princípio da casa dos pombos"],
     "enunciado": p("Em uma cesta básica, há 10 itens:", "→ 4 tipos de grãos (feijão, arroz, milho e lentilha);<br>→ 3 tipos de farináceos (fubá, farinha de trigo e farinha de mandioca);<br>→ 2 doces (gelatina e goiabada); e<br>→ 1 sal.",
                    "É correto afirmar que, se uma pessoa retirar, ao acaso e sem olhar, apenas"),
     "alternativas": alts("4 itens, 2 pertencerão à categoria grãos.", "5 itens, pelo menos um deles será um farináceo.", "6 itens, teremos produtos de três categorias diferentes.",
                          "7 itens, pelo menos um deles será um grão.", "8 itens, pelo menos um deles será um doce."),
     "explicacao": "<p>Há 6 itens que não são grãos (3 farináceos, 2 doces e 1 sal). Mesmo no pior caso, ao retirar 7 itens, pelo menos um será um grão. Alternativa <strong>D</strong>.</p><p>Com 4 itens, pode não vir nenhum grão, ou vir os 4 (A). Com 5, podem vir 4 grãos e 1 doce, sem farináceo (B). Com 6, podem vir só grãos e farináceos, duas categorias (C). E com 8, podem vir 4 grãos, 3 farináceos e o sal, sem doce (E).</p>"},
36: {"materia": "Biologia", "assunto": "Nutrição e saúde", "tags": MULTI + ["lipídios"],
     "enunciado": MILHO + P36
                  + apoio("Ao consumir uma porção de milho painço, uma pessoa ingere substâncias relacionadas ao armazenamento de energia, ____<strong>(I)</strong>____, que agem como um importante isolante térmico. Nessa porção, elas correspondem a, aproximadamente, ____<strong>(II)</strong>____ % do total diário recomendado."),
     "alternativas": colunas(["I", "II"], [["Proteínas", "10,8"], ["Carboidratos", "10,0"], ["Gorduras", "10,8"], ["Carboidratos", "2,8"], ["Gorduras", "2,8"]]),
     "explicacao": "<p>As substâncias que armazenam energia e funcionam como isolante térmico são as <strong>gorduras</strong> (lipídios). A porção tem 1,8 g de gorduras, e o valor diário é 65 g: 1,8 ÷ 65 ≈ 0,0277, cerca de <strong>2,8%</strong>. Alternativa <strong>E</strong>.</p><p>Proteínas e carboidratos não fazem isolamento térmico (A, B e D). E 10,8% é a porcentagem das proteínas (5,4 ÷ 50), não das gorduras (A e C).</p>"},
37: {"materia": "Biologia", "assunto": "Nutrição e saúde", "tags": MULTI + ["calorias"],
     "enunciado": MILHO + p(*T(16, "A quantidade de energia que os alimentos digeridos", "corresponde a cerca de", ["Para o cálculo da quantidade", "Logo, a quantidade de energia"])),
     "alternativas": alts("158.", "176.", "185.", "299.", "308."),
     "explicacao": "<p>Carboidratos: 30 · 4 = 120 kcal. Proteínas: 5,4 · 4 = 21,6 kcal. Gorduras: 1,8 · 9 = 16,2 kcal. Total: 120 + 21,6 + 16,2 = 157,8 ≈ <strong>158 kcal</strong>. Alternativa <strong>A</strong>.</p><p>Trocar os fatores (9 kcal para carboidratos ou proteínas) ou somar as massas da Tabela 1 leva aos outros valores.</p>"},
38: {"materia": "Raciocínio lógico", "assunto": "Lógica", "tags": ["negação", "leis de De Morgan"],
     "enunciado": p("Em 2023, a Organização das Nações Unidas promove o Ano Internacional do Milho Painço (IYM 2023). Ele é fonte de alimentação para milhões de pessoas no mundo.",
                    "Espera-se que o IYM 2023 seja uma oportunidade para <strong>promover a produção do milho painço e destacar seu potencial para criar um mercado sustentável</strong>.",
                    "Assinale a alternativa que contém a negação lógica da frase destacada em negrito no texto."),
     "alternativas": alts("não promover a produção do milho painço ou não destacar seu potencial para criar um mercado sustentável.",
                          "não promover a produção do milho painço e não destacar seu potencial para criar um mercado sustentável.",
                          "não promover a produção do milho painço ou destacar seu potencial para criar um mercado sustentável.",
                          "não promover a produção do milho painço e destacar seu potencial para criar um mercado sustentável.",
                          "promover a produção do milho painço ou não destacar seu potencial para criar um mercado sustentável."),
     "explicacao": "<p>A frase é uma conjunção, “p <strong>e</strong> q”. Pela lei de De Morgan, a negação é “não p <strong>ou</strong> não q”: não promover a produção <em>ou</em> não destacar seu potencial. Alternativa <strong>A</strong>.</p><p>“Não p e não q” nega as duas partes ao mesmo tempo, o que é mais forte que a negação (B). C, D e E negam só uma das partes.</p>"},
39: {"materia": "Biologia", "assunto": "Nutrição e saúde", "tags": MULTI + ["rótulo nutricional"],
     "enunciado": LASANHA + P39, "imagens": LASANHA_IMG,
     "alternativas": alts("possui alto teor de açúcar, sódio e nutrientes.", "corresponde a 454 g do alimento.", "possui uma quantidade baixa de gorduras saturadas.",
                          "oferece todas as vitaminas para uma dieta diária saudável.", "possui teor de sódio superior ao recomendado."),
     "anulacao": {"fonte": "analise", "motivo": "O Centro Paula Souza anulou a questão sem publicar o motivo. Pela análise do Treineiros, o problema está no próprio rótulo: o guia rápido diz que “20 % or less is high” (20% ou menos é alto), quando o certo seria “20 % or more is high” (20% ou mais é alto). Com esse guia, quase todos os nutrientes da porção seriam “altos” e, ao mesmo tempo, os de 5% ou menos seriam “baixos”, uma contradição. Além disso, a alternativa que a banca provavelmente esperava (E) também é imprecisa: os 850 mg de sódio são 37% do valor diário, um teor alto, mas não “superior ao recomendado” para o dia."},
     "explicacao": "<p>Questão anulada. Se o guia estivesse certo (5% ou menos é baixo; 20% ou mais é alto), a leitura seria esta: o sódio (37%) e a gordura saturada (23%) estão altos, e os açúcares adicionados (0%) estão baixos. Não há alternativa totalmente correta.</p><p>O açúcar adicionado é 0%, então A está errada. A porção tem 227 g; 454 g seriam duas porções (B). A gordura saturada (23%) é alta, não baixa (C). Não há vitamina D (0%), então o produto não oferece todas as vitaminas (D). E o sódio é alto (37% do valor diário), mas não passa do recomendado para o dia (E).</p>"},
40: {"materia": "Física", "assunto": "Termologia", "tags": MULTI + ["calorimetria"],
     "enunciado": p("Em uma tabela nutricional, como a apresentada, a quantidade de energia expressa em calorias é obtida, experimentalmente, utilizando-se um recipiente denominado “calorímetro de combustão” (figura).") + "[[fig:2]]"
                  + p(*T(17, "Para que isso ocorra, uma certa amostra", "observada no termômetro.", ["Suponha que, para a construção", "Considerando as informações descritas"]))
                  + apoio("Lembre-se de que:<br>Q = m · c · ∆θ<br>c<sub>H<sub>2</sub>O</sub> = 1 cal/g · °C"),
     "apoio_de": (39, P39),
     "imagens": figs(("q40", "Ilustração de um calorímetro de combustão: um recipiente cilíndrico com água pura, com um termômetro mergulhado e, dentro, uma cápsula com a amostra do alimento. Setas indicam o termômetro, o calorímetro, a amostra e o recipiente com água pura. Legenda: Fig. – Calorímetro de Combustão.")),
     "trocar": [("(∆θ), em oC", "(∆θ), em °C")],
     "alternativas": alts("1,50", "1,23", "1,00", "0,81", "0,60"),
     "explicacao": "<p>A porção tem 227 g e fornece 280 Calorias; a massa de água também é de 227 g. A banca usa Q = 280 e c = 1: ∆θ = Q ÷ (m · c) = 280 ÷ 227 ≈ <strong>1,23</strong>. Alternativa <strong>B</strong>.</p><p>Observação do Treineiros: nos rótulos, “Calories”, com C maiúsculo, são quilocalorias. A rigor, 280 kcal = 280 000 cal aqueceriam 227 g de água em cerca de 1 233 °C, um valor impossível para a água líquida. O gabarito só fecha tratando as 280 Calorias como 280 cal.</p><p>As outras alternativas não saem de nenhuma combinação dos dados da tabela.</p>"},
41: {"materia": "Química", "assunto": "Estrutura atômica", "tags": ["íons"],
     "enunciado": p("A lasanha apresenta, em sua composição, os cátions sódio (Na<sup>+</sup>), cálcio (Ca<sup>2+</sup>), ferro (Fe<sup>3+</sup>) e potássio (K<sup>+</sup>).", "Considere que")
                  + tabela(["Elemento Químico", "Número Atômico (Z)", "Número de massa (A)"], [["Na", "11", "23"], ["Ca", "20", "40"], ["Fe", "26", "56"], ["K", "19", "40"]])
                  + p("A respeito desses cátions, é correto afirmar que"),
     "apoio_de": (39, P39),
     "alternativas": alts("o número de elétrons do Ca<sup>2+</sup> é o mesmo do K<sup>+</sup>.", "o número de nêutrons do Fe<sup>3+</sup> é 29.", "o número de elétrons do Na<sup>+</sup> é 11.",
                          "o número de massa do K<sup>+</sup> é 19.", "o número atômico do Ca<sup>2+</sup> é o mesmo do K<sup>+</sup>."),
     "explicacao": "<p>O Ca<sup>2+</sup> tem 20 − 2 = 18 elétrons, e o K<sup>+</sup>, 19 − 1 = 18. São iguais (os dois íons são isoeletrônicos). Alternativa <strong>A</strong>.</p><p>O Fe tem 56 − 26 = 30 nêutrons; perder elétrons não muda isso (B). O Na<sup>+</sup> tem 10 elétrons (C). O número de massa do K<sup>+</sup> é 40; 19 é o número atômico (D). E os números atômicos são 20 e 19, diferentes (E).</p>"},
42: {"materia": "Biologia", "assunto": "Microbiologia", "tags": ["conservação de alimentos"],
     "enunciado": apoio("Há uma variedade de técnicas, amplamente utilizadas na indústria, que conservam os alimentos por mais tempo. Essas técnicas são métodos de conservação, pois impedem as alterações microbianas, enzimáticas, químicas e físicas dos produtos nutricionais.")
                  + url("https://tinyurl.com/2p94rdkt", "07.03.2023") + p("Em relação a essas técnicas, é correto afirmar que"),
     "alternativas": alts("a pasteurização expõe os alimentos à fumaça, produzida pela combustão incompleta da madeira, a fim de inibir a ação de micro-organismos patogênicos.",
                          "o branqueamento reduz o pH, conferindo um gosto ácido aos alimentos, o que provoca a desnaturação das proteínas e dificulta o desenvolvimento microbiano.",
                          "a liofilização é a desidratação de alimentos por congelamento, processo em que o gelo formado é sublimado, aumentando o tempo de conservação do produto pela retirada da água.",
                          "a fermentação é um tratamento químico dos alimentos, no qual se eleva a temperatura a mais de 100 °C e, posteriormente, os alimentos são resfriados a fim de eliminar os micro-organismos.",
                          "a defumação consiste na imersão do alimento em água fervente para promover um cozimento rápido, e, em seguida, sua imersão em um recipiente com água gelada."),
     "explicacao": "<p>Na <strong>liofilização</strong>, o alimento é congelado e, sob baixa pressão, o gelo passa direto para vapor (sublimação). Sem água, os micro-organismos não se desenvolvem, e o produto dura muito mais. Alternativa <strong>C</strong>.</p><p>Expor à fumaça é a defumação (A). Baixar o pH é a acidificação; o branqueamento é o choque térmico em água fervente e depois gelada (B e E). E a fermentação é um processo biológico feito por micro-organismos; aquecer e resfriar é o que faz a pasteurização (D).</p>"},
43: {"materia": "Química", "assunto": "Soluções", "tags": ["osmose"],
     "enunciado": CONSERVA + P43,
     "alternativas": alts("perdem água por osmose, pois o meio externo é hipertônico.", "perdem água por osmose, pois o meio externo é hipotônico.", "perdem água por difusão, pois o meio externo é hipertônico.",
                          "ganham água por difusão, pois o meio externo é hipotônico.", "ganham água por difusão, pois o meio externo é hipertônico."),
     "explicacao": "<p>Uma solução com muito sal é <strong>hipertônica</strong> em relação às células dos micro-organismos. A água passa do meio menos concentrado para o mais concentrado através da membrana (<strong>osmose</strong>): sai das células, que se desidratam e morrem. Alternativa <strong>A</strong>.</p><p>O meio salgado é hipertônico, não hipotônico (B e D). E a passagem de água pela membrana chama-se osmose, não difusão (C, D e E); os micro-organismos perdem, não ganham, água (D e E).</p>"},
44: {"materia": "Inglês", "assunto": "Vocabulário", "tags": MULTI + ["enigma"],
     "enunciado": p("A imagem apresenta um enigma, no qual cada palavra destacada em negrito no texto está representada em uma linha horizontal; e, nele, os símbolos iguais indicam letras iguais.",
                    "Ao solucionar o enigma, uma palavra relacionada à alimentação surgirá na coluna em destaque.",
                    "Assinale a alternativa que contém a versão correta, em inglês, da palavra formada na coluna destacada.") + "[[fig:1]]",
     "apoio_de": (43, P43),
     "imagens": figs(("q44", "Enigma em grade com seis linhas de símbolos e uma coluna vertical em destaque. Linha 1, 12 casas, começando na coluna em destaque: ★ ● = ♪ 3 ¶ √ ▲ = † 3 ♪. Linha 2, 8 casas, começando na coluna em destaque: ● ♪ ■ ● † ! ★ ▲. Linha 3, 8 casas, a quarta na coluna em destaque: ♪ ▲ £ ■ ● ∩ ¶ ▲. Linha 4, 8 casas, a terceira na coluna em destaque: ● ※ ! ? ▲ Ç @ ●. Linha 5, 12 casas, a quinta na coluna em destaque: ? 3 ♪ ! ? ¶ ▲ † ▲ Ç @ ●. Linha 6, 6 casas, começando na coluna em destaque: ▲ Ç ∩ ★ ▲ ¶.")),
     "alternativas": alts("<em>comid</em>", "<em>food</em>", "<em>meet</em>", "<em>meat</em>", "<em>sugar</em>"),
     "explicacao": "<p>Pelo número de letras e pelas repetições, as linhas são: CONSERVANTES (12), OSMÓTICA (8), SALMOURA (8), OXIDAÇÃO (8), DESIDRATAÇÃO (12) e AÇÚCAR (6). As letras na coluna destacada são C, O, M, I, D, A: a palavra é <strong>comida</strong>, em inglês <em>food</em>. Alternativa <strong>B</strong>.</p><p>“Comid” é a palavra incompleta, em português (A). <em>Meat</em> é “carne”, e <em>meet</em>, “encontrar” (C e D). E <em>sugar</em> é “açúcar”, uma das linhas, não a coluna (E).</p>"},
45: {"materia": "Geografia", "assunto": "Agropecuária", "tags": ["agricultura de precisão"],
     "enunciado": apoio(*T(19, "As evoluções tecnológicas estão transformando", "fertilizantes para as próximas safras.", ["O monitoramento de pulverização", "Já se usam, no Brasil"]))
                  + url("https://tinyurl.com/7r7e47em", "24.03.2023") + p("Sobre o uso das tecnologias nos processos produtivos agrícolas, é correto afirmar que"),
     "alternativas": alts("o gado de corte, no Rio Grande do Sul, é abatido com base nos sensores de umidade do solo presos aos cascos dos animais.",
                          "o monitoramento da irrigação é fundamental para as plantações de trigo, no Acre, devido à escassez de água nesse estado.",
                          "já é possível, no Brasil, saber o quanto está sendo colhido em tempo real, utilizando-se de sensores de colheita.",
                          "as lavouras de subsistência, no interior do Nordeste, utilizam o GPS e os drones para a pulverização de agrotóxicos.",
                          "já se utilizavam, no Brasil Colônia, os sensores eletrônicos para pulverizar as lavouras de cana-de-açúcar."),
     "explicacao": "<p>O texto diz que “já se usam, no Brasil, sensores de colheita que monitoram a produtividade do que está sendo colhido em tempo real”. Alternativa <strong>C</strong>.</p><p>Sensores de umidade do solo não servem para abater gado (A). O Acre é chuvoso e não produz trigo (B). A agricultura de subsistência usa pouca tecnologia (D). E não existiam sensores eletrônicos no Brasil Colônia (E).</p>"},
46: {"materia": "Geografia", "assunto": "Agropecuária", "tags": ["solos", "calagem"],
     "enunciado": p("A técnica da calagem é utilizada para diminuir a acidez do solo, ou seja, aumentar seu pH, além de fornecer cálcio e magnésio para as plantas.", "Essa técnica consiste em"),
     "alternativas": alts("pulverizar as plantas com herbicidas.", "misturar cloreto de sódio ao adubo.", "aumentar o uso de cloro no solo.", "incorporar antioxidantes à terra.", "adicionar calcário ao solo."),
     "explicacao": "<p>A calagem é a aplicação de <strong>calcário</strong> (carbonato de cálcio e de magnésio) ao solo. O carbonato neutraliza a acidez, aumenta o pH e fornece cálcio e magnésio. Alternativa <strong>E</strong>.</p><p>Herbicidas matam plantas daninhas (A). O cloreto de sódio saliniza o solo (B). O cloro não corrige a acidez (C). E antioxidantes não têm esse papel (D).</p>"},
47: {"materia": "Física", "assunto": "Grandezas físicas", "tags": ["frequência", "unidades de medida"],
     "enunciado": apoio("<em>" + " ".join(T(20, "O Frontier é o novo computador", "de cálculos por segundo.")) + "</em>")
                  + url("https://tinyurl.com/yp67dtv8", "15.02.2023", "")
                  + p("Em computação e sistemas, flop/s ou FLOPS (<em>Floating-point Operations Per Second</em>) é uma unidade de medida usada para analisar desempenho de máquinas como a exemplificada no texto.",
                      "Com base nos conceitos da Física, é correto afirmar que a unidade de medida FLOPS refere-se à grandeza física conhecida como"),
     "alternativas": alts("aceleração.", "frequência.", "precisão.", "radiação.", "velocidade."),
     "explicacao": "<p>FLOPS conta quantas operações acontecem a cada segundo: é uma quantidade de eventos por unidade de tempo, a mesma ideia da <strong>frequência</strong> (medida em hertz, ciclos por segundo). Alternativa <strong>B</strong>.</p><p>Aceleração é variação de velocidade por tempo (A), e velocidade é distância por tempo (E). Precisão e radiação não são medidas em “algo por segundo” nesse sentido (C e D).</p>"},
48: {"materia": "Física", "assunto": "Eletricidade", "tags": ["energia elétrica", "unidades de medida"],
     "enunciado": ENTREGA + P48,
     "alternativas": alts("ao fato de que motos elétricas não usam baterias elétricas.", "à unidade de medida da carga elétrica da bateria.", "ao fato de que a velocidade de uma moto elétrica é medida em km/h.",
                          "à conversão da unidade de 15 minutos para 900 segundos.", "ao fato de entregadores não usarem motos."),
     "explicacao": "<p>O kWh (quilowatt-hora) é unidade de <strong>energia</strong>, não de carga elétrica. A carga se mede em coulombs (C) ou, em baterias, em ampère-hora (Ah). Alternativa <strong>B</strong>.</p><p>Motos elétricas usam baterias (A). A velocidade pode ser dada em m/s ou em km/h (C). 15 min = 15 · 60 = 900 s está certo (D). E entregadores usam motos (E).</p>"},
49: {"materia": "Física", "assunto": "Cinemática", "tags": ["velocidade média"],
     "enunciado": ENTREGA + p("O estudante percebeu que, apesar do erro, poderia ainda utilizar os dados fornecidos pela IA para determinar a distância percorrida pelo entregador.",
                              "Após fazer os cálculos, ele descobriu que, no tempo apresentado, o entregador percorreu, em km, a distância de"),
     "alternativas": alts("15,0.", "13,5.", "10,0.", "9,0.", "2,0."),
     "explicacao": "<p>d = v · t = 10 m/s · 900 s = 9 000 m = <strong>9,0 km</strong>. Alternativa <strong>D</strong>.</p><p>15,0 usa o tempo em minutos como se fosse a distância (A). 10,0 usa a velocidade (C). E 2,0 e 13,5 não saem dos dados (B e E).</p>"},
50: {"materia": "Geografia", "assunto": "Industrialização brasileira", "tags": ["ciência dos alimentos"],
     "enunciado": apoio(*T(21, "Ciência e Tecnologia de Alimentos (CTA)", "à regulamentação alimentícia.", ["Com o incremento cada vez maior"]))
                  + url("https://tinyurl.com/3x9vfcy2", "16.03.2023") + p("De acordo com o texto, é correto afirmar que a CTA"),
     "alternativas": alts("contribui para a diminuição do número de indústrias alimentícias presentes no Brasil.", "impede que produtos sem qualidade cheguem à mesa dos brasileiros, livrando-os da fome.",
                          "assumiu a responsabilidade sobre a saúde pública no Brasil, em substituição ao Ministério da Saúde.", "é uma área do conhecimento a qual pensa sobre a qualidade dos alimentos consumidos pelas pessoas.",
                          "rivaliza com a Medicina e com a Agronomia, pois questiona pesquisas consolidadas dessas áreas."),
     "explicacao": "<p>O texto define a CTA como a área do conhecimento voltada ao processamento dos alimentos, incluindo “a análise da qualidade dos alimentos”. Alternativa <strong>D</strong>.</p><p>O texto fala no crescimento das indústrias, não na diminuição (A). Garantir qualidade não acaba com a fome (B). A CTA é essencial à saúde pública, mas não substitui o Ministério da Saúde (C). E ela se relaciona com a Agronomia e a Medicina, não rivaliza com elas (E).</p>"},
51: {"materia": "Química", "assunto": "Química orgânica", "tags": MULTI + ["ácidos graxos", "Antiguidade"],
     "enunciado": p(*T(21, "O azeite de oliva é um óleo extraído", "cuja fórmula estrutural apresenta:", ["No azeite de oliva, encontramos", "Ácidos graxos insaturados são", "O principal ácido graxo"]),
                    "• 18 átomos de carbono; e<br>• uma insaturação entre os carbonos 9 e 10, contados a partir do átomo de carbono que está localizado na ponta da cadeia e que está ligado aos átomos de oxigênio.",
                    "Com base no texto, assinale a alternativa que apresenta corretamente o período histórico mencionado no texto e a fórmula estrutural do ácido oleico."),
     "alternativas": alts("Idade Antiga<br>CH<sub>3</sub>–(CH<sub>2</sub>)<sub>7</sub>–CH=CH–(CH<sub>2</sub>)<sub>7</sub>–COOH",
                          "Idade Antiga<br>CH<sub>3</sub>–CH=CH–(CH<sub>2</sub>)<sub>14</sub>–COOH",
                          "Idade Antiga<br>CH<sub>3</sub>–(CH<sub>2</sub>)<sub>5</sub>–CH=CH–(CH<sub>2</sub>)<sub>7</sub>–COOH",
                          "Idade Média<br>CH<sub>3</sub>–(CH<sub>2</sub>)<sub>6</sub>–CH=CH–(CH<sub>2</sub>)<sub>6</sub>–COOH",
                          "Idade Média<br>CH<sub>3</sub>–(CH<sub>2</sub>)<sub>7</sub>–CH=CH–(CH<sub>2</sub>)<sub>7</sub>–COOH"),
     "explicacao": "<p>Egípcios, gregos e romanos e o ano 3 500 a.C. situam o texto na <strong>Idade Antiga</strong>. Na fórmula A, contando a partir do carbono do grupo –COOH (carbono 1), há 7 CH₂ (carbonos 2 a 8), a dupla ligação entre os carbonos 9 e 10, mais 7 CH₂ e o CH₃ final: 1 + 7 + 2 + 7 + 1 = 18 carbonos. Alternativa <strong>A</strong>.</p><p>Na B, a dupla ligação fica entre os carbonos 16 e 17. A C tem só 16 carbonos, e a D, também 16, além de estar na Idade Média. A E tem a fórmula certa, mas o período errado.</p><p>Observação: na prova, as cadeias aparecem escritas por extenso, CH₂ por CH₂; aqui elas foram abreviadas, por exemplo (CH₂)₇ para sete grupos CH₂ seguidos.</p>"},
52: {"materia": "Geografia", "assunto": "Climatologia", "tags": ["latitude", "soja"],
     "enunciado": apoio(*T(22, "Para a produção de sementes de soja", "são mais propícias."))
                  + url("https://tinyurl.com/c583wypa", "24.03.2023") + p("Com base no texto, a região brasileira que melhor se encaixa nas especificações dadas é a"),
     "alternativas": alts("Centro-Oeste.", "Nordeste.", "Sudeste.", "Norte.", "Sul."),
     "explicacao": "<p>Latitudes maiores que 24° S ficam ao sul do Trópico de Capricórnio (cerca de 23° S), onde está quase toda a região <strong>Sul</strong>, de clima subtropical, com temperaturas médias mais baixas. Alternativa <strong>E</strong>.</p><p>Norte, Nordeste e Centro-Oeste ficam na zona tropical (A, B e D). O Sudeste é cortado pelo Trópico e tem só uma pequena parte, no sul de São Paulo, além de 24° S (C).</p>"},
53: {"materia": "Raciocínio lógico", "assunto": "Lógica", "tags": ["silogismos"],
     "enunciado": p("Em uma barraca de feira, há estas frutas: jaca, jabuticaba, morango e manga. Elas podem ser grandes ou pequenas, doces ou azedas. Sobre elas, pode constatar-se que:",
                    "• toda jaca é grande;<br>• algumas frutas pequenas são jabuticabas;<br>• alguns morangos são azedos;<br>• nenhuma fruta azeda é uma jabuticaba;<br>• toda manga é doce; e<br>• toda fruta grande é doce.",
                    "Com base nessas informações, assinale a alternativa correta."),
     "alternativas": alts("Alguma fruta azeda é uma manga.", "Algum morango é pequeno.", "Toda fruta grande é um jaca.", "Alguma jabuticaba é azeda.", "Toda manga é grande."),
     "explicacao": "<p>Toda fruta grande é doce, então nenhuma fruta azeda é grande: toda fruta azeda é pequena. Como alguns morangos são azedos, esses morangos são pequenos. Logo, algum morango é pequeno. Alternativa <strong>B</strong>.</p><p>Toda manga é doce, então nenhuma é azeda (A). Ser grande não obriga a ser jaca (C). Nenhuma jabuticaba é azeda (D). E nada diz que toda manga é grande (E).</p>"},
54: {"materia": "Português", "assunto": "Interpretação de texto", "tags": ["quadrinhos"],
     "enunciado": p("Leia os quadrinhos.") + "[[fig:1]]" + url("https://tinyurl.com/5ac5mb46", "10.03.2023", "Original colorido.")
                  + p("Analisando os quadrinhos, pode concluir-se corretamente que"),
     "imagens": figs(("q54", "Tirinha “Cientirinhas #174”, de Merlin, em quatro quadrinhos. No primeiro, uma mulher descasca um pêssego e um homem, lendo jornal, diz: “Num descasca não, criatura! A casca do pêssego é fonte de fibras.” No segundo, ela descasca uma maçã e ele aponta: “Olhaí o desperdício! É na casca da maçã que fica a maior parte das vitaminas!” No terceiro, ela descasca uma pera e ele cochicha no ouvido dela: “Psiu! Sabia que a casca da pera é cheinha de antioxidantes?” No quarto, ela, irritada e descascando um abacaxi com uma faca grande, responde: “Se abrir a boca, te faço engolir essa casca.”")),
     "alternativas": alts("os termos “fibras”, “vitaminas” e “antioxidantes” associam propriedades positivas à ação de descascar os alimentos.",
                          "as interjeições “criatura”, “olhaí” e “psiu” expressam a reação de ambos os personagens diante de uma situação inesperada.",
                          "o personagem usa de linguagem violenta para impor sua vontade à mulher, opondo-se ao tema abordado no texto: equidade de gênero.",
                          "o pronome “essa”, no último quadrinho, é empregado segundo a norma culta, pois aponta para a casca que está nas mãos do interlocutor.",
                          "a intromissão constante de um dos personagens, apesar de causar irritação, tematiza um tópico relevante à sociedade: o desperdício dos alimentos."),
     "explicacao": "<p>O homem interrompe a mulher várias vezes para lembrar que as cascas têm nutrientes. Ela se irrita, mas o tema é o <strong>desperdício de alimentos</strong>. Alternativa <strong>E</strong>.</p><p>Fibras, vitaminas e antioxidantes valorizam as cascas, ou seja, são argumentos contra descascar (A). “Criatura” é vocativo, não interjeição, e as falas são só do homem (B). Quem ameaça é a mulher, e o tema não é equidade de gênero (C). E a casca do abacaxi está nas mãos de quem fala, então a norma culta pediria “esta” (D).</p>"},
}
completar(Q, R)
