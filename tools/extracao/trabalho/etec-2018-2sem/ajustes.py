# Ajustes da conferência humana: Vestibulinho ETEC 2º semestre de 2018 (exame de 24/06/2018)
# Texto conferido com a imagem de cada página. As caixas de texto do PDF saem como figura no rascunho,
# então os textos de apoio vêm do texto do PDF com trecho(). Gabarito: oficial (2º SEM/18). Tema: sustentabilidade.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import A, carregar, enun, tabela, colunas, completar, trecho

ID = "etec-2018-2sem"
META = {
    "id": ID,
    "banca": "ETEC",
    "ano": 2018,
    "semestre": 2,
    "titulo": "Vestibulinho ETEC, 2º semestre de 2018",
    "fonte": "Centro Paula Souza",
    "dataExame": "2018-06-24",
    "duracaoMinutos": 240,
    "tema": "Sustentabilidade",
    "apresentacao": "<p>Prezado(a) candidato(a), nesta prova, vamos tratar de um tema atual, apresentando alguns problemas e algumas soluções, que levarão a reflexões e escolhas para uma prática consciente e sustentável.</p><p>Boa prova!</p>",
    "pdf": f"assets/provas/{ID}.pdf",
}
EXTRAS = {"apresentacao": "Ícone de uma mão aberta, desenhada em linhas, segurando o globo terrestre."}

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


def sub(texto, *pares):
    for a, b in pares: texto = texto.replace(a, b)
    return texto


# ---------- textos compartilhados ----------
MAFALDA = (chamada("Leia a tirinha para responder às questões de números 01 e 02.") + "[[fig:1]]"
           + fonte("QUINO (Joaquín Salvador Lavado), <strong><em>Toda Mafalda</em></strong>. São Paulo: Martins Fontes, 2008, p. 106."))
MAFALDA_IMG = {"arquivo": "q01", "alt": "Tirinha da Mafalda em cinco quadrinhos. 1: deitada, ela pensa: “Quando eu crescer, eu vou trabalhar de intérprete da O.N.U.” 2: sentada, imagina: “E quando um delegado disser ao outro: ‘Seu país é um nojo!’ vou traduzir: ‘Seu país é um encanto!’ E então, ninguém vai poder brigar, é claro!” 3: animada: “E os conflitos e as guerras vão acabar e o mundo vai estar salvo!” 4: ela olha em silêncio para o globo terrestre ao lado. 5: virada para o globo, pergunta: “Isso se você me prometer que vai durar até eu crescer, viu?”"}
P1 = p("A tirinha apresenta a personagem Mafalda contando ao globo terrestre seu projeto de vida.",
       "Para concretizá-lo, Mafalda, no último quadrinho, usa uma pergunta para pedir ao globo terrestre que")

TRESR = (chamada("Leia o texto para responder às questões de números 08 e 09.")
         + apoio(*T(5, "Embora reutilizar e reciclar", "mais de uma vez."))
         + url("https://tinyurl.com/ybclontb", "03.04.2018"))
P8 = p("Assinale a alternativa que apresenta corretamente ações associadas aos atos de reutilizar e reciclar.")

INFO = (chamada("Leia e analise o infográfico para responder às questões de números 10 e 11.") + "[[fig:1]]"
        + url("https://tinyurl.com/yc6hbpcg", "13.04.2018", "Original colorido."))
INFO_IMG = {"arquivo": "q10", "alt": "Infográfico “10 atividades ecorretas”, com um ícone e uma caixinha para marcar em cada item: “Me banhei por 5min.”, “Peguei carona ou fui de bike”, “Separei os meus lixos”, “Usei pilhas recarregáveis”, “Usei garrafa de água durável”, “Desliguei meu computador e a luz do quarto”, “Desliguei os eletrônicos inativos”, “Usei sacolas retornáveis no mercado”, “Troquei lâmpadas incandescentes por lâmpadas econômicas” e “Inspirei outra pessoa a unir-se a este compromisso”. Embaixo, “Em 1 ano:”: “Poupas luz e água: 1345 kwh, 54,750 lt”; “Reduzes: 255 kg de lixo”; “Salvas: 1 árvore”."}
P10 = p("Uma dentre as informações contidas na primeira parte do infográfico foge à variedade culta da língua portuguesa.", "Esse desvio ocorre em:")

CONSUMO = (chamada("Leia o texto para responder às questões de números 18 e 19.")
           + apoio("<strong>Consumo Sustentável</strong>", *T(9, "O Consumo Sustentável envolve", "no acumulado do consumo de todos os cidadãos.",
                                                               ["Mudança de comportamento", "Consumo consciente, consumo verde"]))
           + url("http://tinyurl.com/6nk85vr", "12.04.2018"))
P18 = p("De acordo com o texto, é correto afirmar que")

XPL = (chamada("Leia o texto para responder às questões de números 22 e 23.")
       + apoio(*[it(x, "Xplástico") for x in T(11, "Para reduzir o consumo de derivados", "por ano nessa empresa.", ["A Xplástico"])]))
P22 = p("Suponha que a razão anual entre as quantidades de eco-copos e o total de peças plásticas produzidas seja constante até 2 030, e que a quantidade de massa plástica utilizada na confecção de cada peça seja sempre igual.",
        "O número de toneladas de plástico comum que deixarão de ser utilizadas pela <em>Xplástico</em>, de 2 018 a 2 030, ao produzir as peças de eco-copos, é")

CARBONO = (chamada("Leia o texto para responder às questões de números 34 e 35.")
           + apoio(*[sub(it(x, "reciclagem", "ciclo biogeoquímico"), ("CO2", "CO<sub>2</sub>")) for x in
                     T(17, "O planeta tem um estoque fixo", "ação dos decompositores.",
                       ["No ciclo do carbono, por exemplo", "Parte substancial", "O carbono da biomassa", "Nos herbívoros"])])
           + fonte("José Mariano Amabis &amp; Gilberto Rodrigues Martho. <em>Biologia: vol 3</em>. 3º edição. Editora Moderna. 2009. Adaptado."))
P34 = p("O ciclo do carbono, descrito no texto, pode ser resumido no esquema:") + "[[fig:1]]" + p("Nesse esquema, os números 1 e 2 podem representar, correta e respectivamente, os processos denominados")

PUNK_T = T(21, "“O punk sempre teve", "não compensa.”", ["(...) O apresentador"])
PUNK_T = [sub(x, ("é &#%!,", "é <strong>&amp;#%!</strong>,")) for x in PUNK_T]
PUNK_T = [it(x, "Não Verás País Nenhum") for x in PUNK_T]
PUNK_T[1] = PUNK_T[1].replace("inglês free e vegan", "inglês <em>free</em> e <em>vegan</em>")
PUNK = (chamada("Leia o texto para responder às questões de número 46 e 47.")
        + apoio(*PUNK_T)
        + fonte("Júlio Lamas. <em>Punk Verde</em>. &lt;http://tinyurl.com/ycdmhocv&gt; Acesso em: 13.04.2018. Adaptado.")
        + apoio("*Distópico: relativo à distopia**.",
                "**Distopia: qualquer representação ou descrição de uma organização social futura caracterizada por condições de vida insuportáveis, com o objetivo de criticar tendências da sociedade atual, ou parodiar utopias, alertando para os seus perigos.")
        + fonte("Antonio Houaiss e Mauro de Salles Villar. <strong><em>Dicionário Houaiss da Língua Portuguesa</em></strong>. Rio de Janeiro: Objetiva, 2001."))
P46 = p("O texto constrói uma relação entre o movimento Punk e o “Freeganismo”.", "Essa relação se estabelece por meio de")

MAMIRAUA = (chamada("Leia o texto para responder às questões de números 49 e 50.")
            + apoio(*T(22, "Mamirauá é a primeira Reserva", "fica por conta das águas.", ["A reserva Mamirauá está", "Uma característica fundamental"]))
            + url("https://tinyurl.com/yast296f", "10.04.2018"))
P49 = p("A cobertura vegetal, onde a reserva Mamirauá está inserida, é composta por vegetação")

# ---------- questões ----------
Q = {
1: {"materia": "Português", "assunto": "Interpretação de texto", "tags": ["tirinha"],
    "enunciado": MAFALDA + P1, "imagens": [MAFALDA_IMG],
    "explicacao": "<p>Mafalda planeja ser intérprete da ONU e “salvar o mundo” trocando ofensas por elogios nas traduções. No último quadrinho, ela pede ao globo que prometa “durar até eu crescer”, ou seja, que o mundo <strong>não acabe antes de ela realizar o seu plano</strong>. Alternativa <strong>C</strong>.</p><p>Ela não pede emprego ao globo (A), não quer que a crise continue (B), não pede para o mundo conservá-la viva (D) e, ao contrário de E, quer acabar com os conflitos e as guerras.</p>"},
2: {"materia": "Português", "assunto": "Pronomes", "tags": ["pronome oblíquo"],
    "enunciado": p("Considere o trecho: “E quando um delegado disser <u>ao outro</u>”.",
                   "Substituindo, de acordo com a variedade padrão da língua, a expressão grifada por um pronome oblíquo correspondente, obtém-se:"),
    "apoio_de": (1, P1),
    "explicacao": "<p>“Disser” pede objeto indireto (dizer algo <em>a alguém</em>), e “ao outro” é esse objeto indireto. O pronome oblíquo que substitui objeto indireto é <strong>lhe</strong>. Como “quando” atrai o pronome para antes do verbo (próclise), fica “E quando um delegado lhe disser”. Alternativa <strong>D</strong>.</p><p>“O” substitui objeto direto (A). “Lo” só aparece depois de verbo terminado em r, s ou z, ligado por hífen (B). “No” é usado depois de verbo terminado em som nasal (C). E “lho” junta dois pronomes, “lhe” + “o”, o que não corresponde ao trecho (E).</p>"},
3: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["sustentabilidade"],
    "enunciado": apoio(*T(3, "Sustentabilidade é um conceito", "soluções ecológicas de desenvolvimento.", ["A sustentabilidade serve"]))
                 + url("https://tinyurl.com/y8t6j2zh", "07.04.2018") + p("Assinale a alternativa que apresenta uma ideia coerente ao texto."),
    "explicacao": "<p>O texto define a sustentabilidade como ideias e atitudes “ecologicamente corretas, economicamente viáveis”. <strong>Reutilizar recipientes plásticos</strong> evita produzir novos e diminui o lixo, o que é uma atitude ecologicamente correta. Alternativa <strong>C</strong>.</p><p>Extrair minério para fazer aço consome recursos naturais, em vez de preservá-los (A). Desmatar para formar pasto não é ecologicamente correto (B). O vidro deve, sim, ser reciclado (D). E aumentar o consumo de derivados do petróleo, um recurso não renovável e poluente, não é sustentável (E).</p>"},
4: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["biocombustíveis", "sustentabilidade"],
    "enunciado": enun(R, 4, figs={"p03-2": 1}),
    "imagens": [{"arquivo": "q04", "alt": "Diagrama do tripé da sustentabilidade: três círculos sobrepostos, “econômico” (com um saco de dinheiro), “social” (com uma família) e “ambiental” (com árvores), e o globo terrestre no centro, onde os três se encontram."}],
    "explicacao": "<p>Biocombustíveis, como o etanol e o biodiesel, vêm de plantas cultivadas e por isso são <strong>renováveis</strong>. Eles já <strong>suprem parte da demanda de energia</strong> do mundo, substituindo combustíveis fósseis. Alternativa <strong>D</strong>.</p><p>Quem leva milhares de anos para se formar é o petróleo (A). Os biocombustíveis são renováveis (B). O biodiesel é feito de óleos vegetais ou gordura animal, não de petróleo (C). E a queima deles também polui, só que menos (E).</p>"},
5: {"materia": "História", "assunto": "Idade Média", "tags": ["agricultura medieval"],
    "enunciado": enun(R, 5, trocas=[("[[FIG:p04-1]]", tabela(["Campo", "Primeiro ano", "Segundo ano", "Terceiro ano"], [
        ["1", "Plantação de cevada", "<em>Campo em repouso</em>", "Plantação de trigo"],
        ["2", "Plantação de trigo", "Plantação de cevada", "<em>Campo em repouso</em>"],
        ["3", "<em>Campo em repouso</em>", "Plantação de trigo", "Plantação de cevada"]]))]),
    "explicacao": "<p>Entre os séculos X e XII, a agricultura europeia produziu mais graças à rotação trienal e a outras inovações: o <strong>arado de ferro</strong> (com rodas, que revolvia a terra mais fundo), a <strong>ferradura</strong> e novas formas de <strong>atrelar os animais</strong> (como o peitoral para cavalos), que aumentaram a força de tração. Alternativa <strong>C</strong>.</p><p>Manufaturas e cercamentos são da Idade Moderna (A). Trator e colheitadeira surgiram nos séculos XIX e XX (B). Sementes geneticamente modificadas são do fim do século XX (D). E a monocultura em larga escala não marca a agricultura medieval (E).</p>"},
6: {"materia": "Química", "assunto": "Substâncias e misturas",
    "enunciado": apoio(*[sub(x, ("((NH4)2SO4)", "((NH<sub>4</sub>)<sub>2</sub>SO<sub>4</sub>)"), ("(KCl)", "(KCℓ)")) for x in
                         T(4, "A agricultura sustentável é aquela", "fixação biológica de nitrogênio.", ["Um dos princípios"])])
                 + url("https://tinyurl.com/y8fbtz6c", "11.04.2018") + p("A substância, cloreto de potássio, mencionada no texto, é classificada como"),
    "explicacao": "<p>O cloreto de potássio (KCℓ) é formado por um único tipo de substância, que reúne <strong>dois elementos químicos</strong> diferentes, o potássio e o cloro. Por isso é uma <strong>substância composta</strong>. Alternativa <strong>A</strong>.</p><p>Substância simples tem um só elemento, como O<sub>2</sub> (B). Elemento químico é um tipo de átomo, não uma substância (C). E o KCℓ puro não é mistura (D e E).</p>"},
7: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["consumo consciente"],
    "enunciado": apoio(*T(4, "As mudanças climáticas globais", "num futuro próximo.", ["A adoção de pequenas"]))
                 + url("https://tinyurl.com/y8kbrdmu", "12.04.208")
                 + p("Assinale a alternativa que apresenta uma ação individual, condizente com o tema apresentado no texto, e que pode iniciar uma mudança de consciência na população."),
    "explicacao": "<p><strong>Usar cartuchos recarregáveis</strong> é uma ação simples que reduz o lixo e o consumo de recursos para fabricar cartuchos novos. Alternativa <strong>E</strong>.</p><p>As lâmpadas fluorescentes duram mais e gastam menos que as incandescentes, então a troca seria um retrocesso (A). Equipamentos sem regulagem de fluxo desperdiçam água (B). Deixar aparelhos ligados desperdiça energia (C). E pilhas e baterias no lixo comum contaminam o solo e a água (D).</p>"},
8: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["3 Rs"],
    "enunciado": TRESR + P8,
    "alternativas": colunas(["Reutilizar", "Reciclar"], [
        ["Eliminar perdas e combater o desperdício, envolvendo em sua totalidade funcionários de empresas, para acabar com qualquer tipo de perdas.", "Diminuir a posse de objetos e ter apenas o necessário e em quantidades necessárias para trabalhar e viver."],
        ["Acabar com a sujeira no local de habitação e sempre primar pela limpeza do ambiente dos arredores das fábricas.", "Melhorar a qualidade de vida para que as pessoas tenham saúde mental e física adequadas a fim de poderem exercer atividades físicas e laborais por mais tempo."],
        ["Possuir autodisciplina e desprendimento para desapegar de materiais que serão transformados em outros produtos, diminuindo a exploração do meio ambiente.", "Atribuir a cada cidadão alguma função que contribua para a limpeza do meio ambiente, como rotinas programadas com periodicidade a serem definidas pela comunidade."],
        ["Transformar hábitos e ações em uma nova filosofia de vida que beneficie o meio ambiente, melhorando a organização do trabalho.", "Organizar cada utensílio em um local apropriado e identificado para que não haja desperdício de tempo quando o procurar."],
        ["Utilizar materiais o maior tempo possível, até o limite de sua vida útil, realizando manutenções pontuais.", "Colocar objetos em um novo ciclo de produção de forma que o considerado lixo seja transformado em outro material que, por sua vez, é usado na confecção de novos produtos."]]),
    "explicacao": "<p><strong>Reutilizar</strong> é usar o mesmo objeto por mais tempo, consertando quando preciso. <strong>Reciclar</strong> é transformar o que seria lixo em matéria-prima de novos produtos. As duas definições aparecem juntas só na alternativa <strong>E</strong>.</p><p>Nas outras, as ações descritas falam de combater perdas, limpeza, organização ou qualidade de vida, que não correspondem a reutilizar nem a reciclar. Em C, a coluna “Reutilizar” descreve, na verdade, a reciclagem (materiais “que serão transformados em outros produtos”).</p>"},
9: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["3 Rs"],
    "enunciado": p("Uma das propostas presente no texto para reduzir o desperdício é"), "apoio_de": (8, P8),
    "alternativas": {"E": "abolir o ato de comprar."},
    "explicacao": "<p>O texto diz que o consumidor deve “analisar a real necessidade de adquirir algum produto ou serviço, abolindo a compra por impulso e os desperdícios”. Isso é <strong>diminuir o consumismo</strong>. Alternativa <strong>D</strong>.</p><p>O texto não fala de compras pela internet (A), sugere consertar em vez de comprar um produto novo (B e C) e propõe abolir a compra por impulso, não toda compra (E).</p>"},
10: {"materia": "Português", "assunto": "Pronomes", "tags": ["colocação pronominal", "infográfico"],
     "enunciado": INFO + P10, "imagens": [INFO_IMG],
     "explicacao": "<p>Pela norma-padrão, não se começa uma frase com pronome oblíquo átono. “<strong>Me banhei</strong> por 5 min” deveria ser “Banhei-me por 5 min”. Alternativa <strong>B</strong>.</p><p>As outras frases começam pelo verbo e seguem a norma culta: “Separei os meus lixos” (A), “Usei garrafa de água durável” (C), “Desliguei os eletrônicos inativos” (D) e “Troquei lâmpadas incandescentes por lâmpadas econômicas” (E).</p>"},
11: {"materia": "Português", "assunto": "Interpretação de texto", "tags": ["infográfico"],
     "enunciado": p("Com o intuito de convencer o maior número possível de pessoas a adotar atividades ecologicamente corretas, o autor do infográfico utiliza vários recursos diferentes para se aproximar do leitor.",
                    "Essa aproximação ocorre, principalmente, por meio do uso de"),
     "apoio_de": (10, P10),
     "explicacao": "<p>O infográfico fala como quem relata o que fez, na primeira pessoa do singular (“Me banhei”, “Separei”), e depois se dirige ao leitor na segunda pessoa (“poupas”, “reduzes”, “salvas”). Isso aproxima o texto de quem lê. Alternativa <strong>A</strong>.</p><p>Os verbos não estão no imperativo (B). “Ecorretas” e “fui de bike” são informais (C). Os ícones são simples e incentivam, não desestimulam, as ações (D). E as atitudes apresentadas não são irrelevantes (E).</p>"},
12: {"materia": "Biologia", "assunto": "Fisiologia humana", "tags": ["hormônios"],
     "enunciado": apoio(*T(7, "A sustentabilidade pessoal", "auxiliam no combate de inflamações.", ["Além disso, passear", "Enquanto isso, o sol", "Além desses exemplos"]))
                  + url("https://tinyurl.com/ya4yemoo", "14.04.2018") + P18,
     "explicacao": "<p>O texto diz que o sol eleva a produção de <strong>serotonina</strong>, que regula o humor, o sono e o apetite. Sem luz solar, cai a serotonina e podem surgir <strong>perda de apetite, mau humor e dificuldade para dormir</strong>. Alternativa <strong>E</strong>.</p><p>As bactérias do solo ajudam a combater inflamações, e quem estimula a vitamina D é o sol (A). Cortisol alto prejudica a memória (B). Estresse alto está ligado a muito cortisol, não a pouco (C). E o sol estimula a vitamina D, que ajuda a resposta imune (D).</p>"},
13: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["poluição do ar"],
     "explicacao": "<p><strong>Catalisadores</strong> nos escapamentos transformam gases tóxicos em gases menos nocivos, e <strong>filtros nas chaminés</strong> retêm partículas e gases das fábricas. As duas medidas reduzem a poluição do ar. Alternativa <strong>E</strong>.</p><p>A energia eólica não funciona “deslocando poluentes” (A). Não se armazena poluente do ar em minas, e combustível fóssil no metrô poluiria mais (B). Levar poluentes por dutos só muda o problema de lugar, e termelétricas poluem mais que hidrelétricas (C). Tirar trens de circulação e usar mais diesel aumentaria a poluição (D).</p>"},
14: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["saneamento"],
     "explicacao": "<p>A solução adequada é <strong>tratar os esgotos e efluentes</strong>, residenciais e industriais, antes de devolver a água à natureza. Alternativa <strong>D</strong>.</p><p>Guardar esgoto em tanques em cada casa e indústria não resolve e é inviável (A). Cisternas guardam água da chuva, não evitam poluição (B). Proibir o uso da água e fechar indústrias não é plausível (C). E parar o consumo de madrugada não limpa a água (E).</p>"},
15: {"materia": "História", "assunto": "História contemporânea", "tags": ["Segunda Guerra Mundial"],
     "explicacao": "<p>As bombas de Hiroshima (6 de agosto de 1945) e Nagasaki foram dos últimos episódios da <strong>Segunda Guerra Mundial</strong>. Na Europa, a guerra já tinha terminado: a Itália havia se rendido, Hitler morrera em abril e a Alemanha se rendera em maio de 1945. Alternativa <strong>D</strong>.</p><p>O Japão foi derrotado e ocupado, não se tornou potência hegemônica (A). A Guerra Fria ainda estava começando, e os Sudetos ficam na Europa (B). Não houve acordo mediado pela Coreia do Norte, que nem existia como país (C). E a dominação europeia na Ásia e na África é bem anterior (E).</p>"},
16: {"materia": "Matemática", "assunto": "Geometria espacial", "tags": ["volume do cilindro"],
     "enunciado": p("Uma questão ambiental relevante, na atualidade, remete ao acúmulo e ao descarte de resíduos sólidos. A indústria nuclear é responsável pelo armazenamento e controle dos rejeitos que produz.",
                    "Suponha que uma indústria nuclear armazene seus resíduos em recipientes cilíndricos, cuja altura é igual a 4 m e o diâmetro da base igual a 12 m. Contudo, devido a mudanças operacionais, decide-se alterar a altura e o raio destes recipientes cilíndricos de tal maneira que o novo recipiente:",
                    "• tenha volume igual a 62,5% do volume do recipiente anterior;", "• e possua raio da base igual à metade do raio da base do recipiente anterior;")
                  + apoio("Lembre que: \\(V = \\pi r^2 \\cdot h\\), em que <em>V</em> é o volume do cilindro; <em>r</em> é o raio do círculo da base; <em>h</em> é a altura do cilindro.")
                  + p("Desta forma, a altura do novo recipiente cilíndrico deve ser, em metros, igual a"),
     "explicacao": "<p>O recipiente antigo tem raio 6 m e altura 4 m: V = π · 6² · 4 = 144π m³. O novo tem 62,5% desse volume, 0,625 · 144π = 90π m³, e raio 3 m. Então π · 3² · h = 90π, ou seja, 9h = 90 e <strong>h = 10 m</strong>. Alternativa <strong>B</strong>.</p><p>Usar o diâmetro (12 m) no lugar do raio, ou esquecer de reduzir o volume para 62,5%, leva aos outros valores. Sem a redução de volume, por exemplo, a altura seria 144π ÷ 9π = 16 m (C).</p>"},
17: {"materia": "História", "assunto": "Revolução Industrial", "tags": ["impactos ambientais"],
     "enunciado": apoio(it(T(9, "Em 1848, na região de Manchester", "enegrecidos pelo carvão.")[0], "Biston betularia"))
                  + fonte("TIEZZI, Enzo. <strong><em>Tempos históricos, tempos biológicos</em></strong>. <em>A terra ou a morte: os problemas da nova ecologia</em>. São Paulo: Nobel, 1988. p.67. Adaptado.")
                  + p("Além do caso das mariposas de Manchester, a Revolução Industrial gerou outros efeitos ambientais na Inglaterra. Entre eles, a"),
     "explicacao": "<p>A indústria inglesa do século XIX dependia do <strong>carvão mineral</strong>, e as florestas foram derrubadas para abrir minas e obter lenha. As cidades industriais cresceram sem saneamento, e <strong>esgoto e resíduos industriais</strong> iam direto para os rios. Alternativa <strong>E</strong>.</p><p>A poluição aumentou, e a burguesia não adotou modelos agroecológicos (A). As máquinas eram movidas a vapor, não por animais de grande porte (B). Milho e cana não eram monoculturas inglesas (C). E os “desertos verdes” de eucalipto não são um efeito da Revolução Industrial na Inglaterra (D).</p>"},
18: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["consumo consciente"],
     "enunciado": CONSUMO + P18,
     "explicacao": "<p>O texto diz que consumimos de maneira sustentável quando nossas compras são “conscientes, responsáveis, com a compreensão de que terão consequências ambientais e sociais”. Ou seja, o consumidor <strong>avalia criticamente os impactos</strong> do que compra. Alternativa <strong>C</strong>.</p><p>É a sociedade que pede ao setor produtivo produtos menos nocivos, e não o contrário (A). A mudança de comportamento “leva tempo” e vem de novos valores (B). Os valores de sustentabilidade é que estão crescendo, não os hábitos nocivos (D). E consumo consciente não é compra desenfreada (E).</p>"},
19: {"materia": "Português", "assunto": "Funções da linguagem",
     "apoio_de": (18, P18),
     "explicacao": "<p>Um texto que quer <strong>informar</strong> com objetividade, centrado no assunto (o consumo sustentável), tem predomínio da função <strong>referencial</strong>. Alternativa <strong>E</strong>.</p><p>A função fática testa o canal de comunicação (A). A metalinguística explica a própria linguagem (B). A conativa tenta convencer o leitor, com imperativos e vocativos, o que não predomina no texto (C). E a emotiva se centra no emissor, em primeira pessoa (D).</p>"},
20: {"materia": "História", "assunto": "Era Vargas",
     "enunciado": apoio(*T(10, "Em 1953, instituiu-se", "mais poluída do mundo."))
                  + url("https://tinyurl.com/yccqej4c", "16.04.2018")
                  + p("A criação da Petrobrás foi resultado da implementação da política econômica do governo de Getúlio Vargas, caracterizada pela"),
     "explicacao": "<p>Vargas usou o <strong>Estado para conduzir a industrialização</strong>: criou estatais em setores estratégicos, como a Companhia Siderúrgica Nacional, a Vale do Rio Doce e a Petrobras (1953, com a campanha “O petróleo é nosso”), e consolidou as leis trabalhistas (CLT, 1943). Alternativa <strong>E</strong>.</p><p>O incentivo ao etanol veio com o Proálcool, nos anos 1970 (A). A Guerra Fria e intervenções militares não definem essa política (B). Vargas foi nacionalista e intervencionista, o oposto de liberal (C). E a expansão de empreiteiras na África é muito posterior (D).</p>"},
21: {"materia": "História", "assunto": "Pré-História",
     "enunciado": apoio(*T(10, "Uma fornalha de 300 mil anos", "aconteceu muito depois.", ["Apesar de o fogo"]))
                  + url("https://tinyurl.com/yal2ab2b", "10.04.2018")
                  + p("Assinale a alternativa que explica, corretamente, por que o uso do fogo é considerado um dos fatores que contribuíram para o desenvolvimento dos homens pré-históricos."),
     "explicacao": "<p>O fogo servia para <strong>caçar</strong> (afugentar e cercar animais), dava <strong>calor</strong> e proteção, permitia <strong>cozinhar</strong> os alimentos e, muito depois, possibilitou a <strong>fundição de metais</strong>. Alternativa <strong>B</strong>.</p><p>A pólvora e as armas de longo alcance são muito posteriores (A). Não havia motores na Pré-História (C). A sedentarização veio com a agricultura, não com o fogo (D). E o teatro é uma criação de sociedades bem posteriores (E).</p>"},
22: {"materia": "Matemática", "assunto": "Porcentagem",
     "enunciado": XPL + P22,
     "explicacao": "<p>Como cada peça usa a mesma massa de plástico, os eco-copos (2% das peças) correspondem a 2% das 6 000 toneladas: 0,02 · 6 000 = 120 toneladas por ano. De 2018 a 2030, contando os dois anos, são 13 anos: 13 · 120 = <strong>1 560 toneladas</strong>. Alternativa <strong>E</strong>.</p><p>120 é a economia de um só ano (B). 1 440 corresponde a 12 anos, esquecendo de contar um dos extremos (D), e 1 320, a 11 anos (C).</p>"},
23: {"materia": "Matemática", "assunto": "Notação científica",
     "apoio_de": (22, P22),
     "explicacao": "<p>São 20 bilhões de peças por ano, ou 2,0 · 10<sup>10</sup>. Um ano tem 365 · 24 = 8 760 horas, cerca de 10<sup>4</sup>. Então, por hora: 2,0 · 10<sup>10</sup> ÷ 8 760 ≈ 2,3 · 10<sup>6</sup>, mais próximo de <strong>2,0 · 10<sup>6</sup></strong>. Alternativa <strong>C</strong>.</p><p>2,0 · 10<sup>9</sup> seria a produção de um dia dividida por 10, um erro de três ordens de grandeza (B). As demais estão ainda mais longe.</p>"},
24: {"materia": "História", "assunto": "Ditadura militar",
     "enunciado": apoio(*T(11, "A industrialização no período", "dignidade humana merece."))
                  + fonte("&lt;https://tinyurl.com/y8usc7nn&gt; Acesso em: 17.04.2018 Adaptado.") + "[[fig:1]]"
                  + url("https://tinyurl.com/y9n8h4sa", "21.04.2018", "Original colorido.")
                  + p("O trecho faz referência ao período da ditadura militar brasileira, mencionando o surto de industrialização verificado no governo do general Emílio Garrastazu Médici.",
                      "Considerado por muitos historiadores o auge da ditadura civil-militar, o governo Médici se caracterizou por"),
     "imagens": [{"arquivo": "q24", "alt": "Adesivo da época da ditadura com a bandeira do Brasil à esquerda e os dizeres “Brasil: ame-o ou deixe-o”."}],
     "explicacao": "<p>O governo Médici (1969-1974) foi o do “milagre econômico”: <strong>crescimento acelerado</strong>, com <strong>incentivos fiscais às grandes empresas</strong> e endividamento externo. Foi também o período de maior <strong>repressão</strong>, sob o AI-5, contra quem lutava contra a ditadura. Alternativa <strong>C</strong>.</p><p>O governo combateu, e não conciliou com, a guerrilha (A). O Brasil era alinhado aos Estados Unidos, não à Cortina de Ferro (B). Não houve reforma agrária, e a Lei de Anistia é de 1979, no governo Figueiredo (D). E a usina de Volta Redonda é da Era Vargas (E).</p>"},
25: {"materia": "Física", "assunto": "Pressão",
     "enunciado": enun(R, 25, trocas=[("[[FIG:p12-1]]", "[[fig:1]]"),
                                    ("[[FIG:p12-2]]", apoio("Considere que: \\(\\text{pressão} = \\dfrac{\\text{força}}{\\text{área de aplicação}}\\)"))],
                       tirar_figs=False),
     "imagens": [{"arquivo": "q25", "alt": "Quadro comparando os dois protótipos. Em cada um, um copo cilíndrico (peça 1) com água suja embaixo e, encaixado nele, um cilindro (peça 2) com um filtro na base e água purificada acima do filtro. O segundo protótipo é maior e tem filtro de área maior que o primeiro."}],
     "alternativas": {"A": "menor que <em>p</em>, demorando menos tempo para filtrar 500 mL de água."},
     "explicacao": "<p>Pressão é força dividida pela área. Com a mesma força sobre um filtro de área maior, a pressão na água suja fica <strong>menor que <em>p</em></strong>. Por outro lado, o filtro maior tem mais orifícios, e a água passa por mais caminhos ao mesmo tempo, então os 500 mL são filtrados em <strong>menos tempo</strong>. Alternativa <strong>A</strong>.</p><p>A pressão não pode ser maior, porque a área aumentou e a força é a mesma (D e E). E, com mais orifícios filtrantes, o tempo não fica igual nem maior (B e C).</p>"},
26: {"materia": "Química", "assunto": "Química ambiental", "tags": ["química verde"],
     "enunciado": apoio(*[it(x, "perigosas") for x in T(13, "A Química Verde é definida", "custo dos processos químicos.",
                                                        ["A invenção, o desenvolvimento", "Nessa definição", "Foram propostos"])])
                  .replace("A invenção, o desenvolvimento e a aplicação de produtos e processos químicos para reduzir ou eliminar o uso e a geração de substâncias <em>perigosas</em>.",
                           "<em>A invenção, o desenvolvimento e a aplicação de produtos e processos químicos para reduzir ou eliminar o uso e a geração de substâncias perigosas</em>.")
                  + url("https://tinyurl.com/y7t7jb2o", "10.04.2018")
                  + p("Um desses princípios é o uso de matérias-primas de fontes renováveis, logo, segundo esse conceito, uma reação química deve ser feita por meio da utilização de matérias-primas renováveis.",
                      "Assinale a alternativa que apresenta um produto obtido obedecendo ao princípio descrito."),
     "explicacao": "<p>O <strong>etanol</strong> é produzido pela fermentação do caldo da cana-de-açúcar (ou do milho), uma matéria-prima renovável, que pode ser plantada de novo. Alternativa <strong>D</strong>.</p><p>Óleo diesel e gasolina vêm do petróleo, que não é renovável (A e C). O alumínio vem da bauxita, e o aço, do minério de ferro, recursos minerais que não se renovam (B e E).</p>"},
27: {"materia": "Física", "assunto": "Cinemática", "tags": ["velocidade média"],
     "enunciado": enun(R, 27, figs={"p13-2": 1}),
     "imagens": [{"arquivo": "q27", "alt": "Gráfico de velocidade (km/h) por tempo (min): a velocidade sobe quase na hora para 20 km/h e fica constante em 20 km/h de 0 a 45 minutos."}],
     "explicacao": "<p>O ciclista anda a 20 km/h durante 45 min, que são 0,75 h. A distância é 20 · 0,75 = 15 km. Com autonomia de 60 km, ainda dá para percorrer 60 − 15 = <strong>45 km</strong>. Alternativa <strong>E</strong>.</p><p>Usar 45 como se fossem horas, ou confundir a distância percorrida com a que falta, leva aos outros valores.</p>"},
28: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": ["verminoses"],
     "enunciado": enun(R, 28),
     "alternativas": colunas(["Verminose", "Medida preventiva específica"], [
         ["Ascaridíase", "Andar somente calçado"], ["Teníase", "Comer apenas carne bem passada"],
         ["Amebíase", "Conservar as mãos sempre limpas e evitar colocar a mão na boca"],
         ["Ancilostomose", "Morar em habitações de alvenaria e não em casa de pau-a-pique ou barro cru"],
         ["Dengue", "Manter a casa limpa, bem como o terreno ao seu redor, a fim de evitar a presença de moscas"]]),
     "explicacao": "<p>A <strong>teníase</strong> (solitária) se pega ao comer carne de porco ou de boi mal cozida com larvas da tênia (cisticercos). <strong>Comer carne bem passada</strong> mata essas larvas. Alternativa <strong>B</strong>.</p><p>Andar calçado previne a ancilostomose, não a ascaridíase (A). A amebíase é causada por um protozoário, não é verminose (C). Casa de alvenaria previne a doença de Chagas (D). E a dengue é um vírus transmitido por mosquito, não por moscas (E).</p>"},
29: {"materia": "Física", "assunto": "Movimento circular", "tags": ["polias"],
     "enunciado": enun(R, 29, figs={"p14-2": 1}),
     "imagens": [{"arquivo": "q29", "alt": "Desenho de uma mini-hidrelétrica: uma calha leva água até uma grande roda d’água com pás. Presa à roda há uma polia grande, ligada por uma correia a uma polia pequena no eixo de um dínamo."}],
     "alternativas": {"D": "maior que o tempo gasto pela a polia menor, sendo que ambas giram no mesmo sentido."},
     "explicacao": "<p>Sem escorregamento, a correia faz as bordas das duas polias andarem com a mesma velocidade. A polia grande tem uma circunferência maior, então leva <strong>mais tempo</strong> para dar uma volta. E, ligadas por uma correia não cruzada, as duas giram <strong>no mesmo sentido</strong>. Alternativa <strong>D</strong>.</p><p>A polia grande não pode ser mais rápida nem igual à pequena (A, B e C). E só giraria em sentido oposto se a correia fosse cruzada, o que não acontece no desenho (E).</p>"},
30: {"materia": "Geografia", "assunto": "Fontes de energia",
     "explicacao": "<p>O <strong>etanol</strong> vem da cana, que é replantada, e a <strong>energia eólica</strong> vem dos ventos, que não se esgotam. As duas são renováveis. Alternativa <strong>B</strong>.</p><p>Petróleo, carvão mineral, gás natural e os combustíveis fósseis em geral não são renováveis, e a energia nuclear usa urânio, que também se esgota (A, C, D e E).</p>"},
31: {"materia": "Matemática", "assunto": "Trigonometria",
     "enunciado": p("Um técnico em edificações irá acompanhar a instalação de painéis solares em uma laje plana e horizontal. Após os cálculos necessários, ele determina que, para ocupar menos espaço nos telhados e obter melhor ângulo solar:",
                    "• cada painel deve ter uma inclinação constante e igual a 20º; e", "• a distância entre os dois painéis deve ser 3,5 vezes a altura <strong>h</strong> dos painéis.")
                  + "[[fig:1]]" + apoio("Dado: sen 20º = 0,34; cos 20º = 0,94; tg 20º = 0,36")
                  + p("Sabendo que cada placa solar é quadrada e tem 1 m<sup>2</sup> de superfície, a distância entre dois painéis é, em metros, de"),
     "imagens": [{"arquivo": "q31", "alt": "Desenho de dois painéis solares inclinados 20º sobre uma laje. Um raio solar passa pela borda de cima do primeiro painel e toca a laje no pé do segundo. A altura h do painel está marcada à esquerda, e a “distância entre dois painéis” vai do fim do primeiro ao começo do segundo."}],
     "explicacao": "<p>A placa é quadrada com 1 m², então tem 1 m de lado. Inclinada 20º, sua altura é h = 1 · sen 20º = 0,34 m. A distância entre os painéis é 3,5 · 0,34 = <strong>1,19 m</strong>. Alternativa <strong>D</strong>.</p><p>0,34 é só a altura (A). 0,94 e 0,36 são o cosseno e a tangente de 20º (B e C). E 1,26 vem de usar a tangente no lugar do seno (3,5 · 0,36) (E).</p>"},
32: {"materia": "Física", "assunto": "Energia", "tags": ["consumo de energia elétrica"],
     "enunciado": enun(R, 32, trocas=[("[[FIG:p15-3]]", apoio("Considere que: \\(\\text{potência} = \\dfrac{\\text{energia}}{\\text{tempo}}\\)"))], tirar_figs=False),
     "explicacao": "<p>A lâmpada de LED gasta E = P · t = 10 W · 8 h = 80 Wh. A incandescente gasta essa energia em t = 80 ÷ 75 ≈ 1,07 h, ou seja, cerca de <strong>1 h</strong>. Alternativa <strong>A</strong>.</p><p>Os outros tempos dariam muito mais energia que a do LED: em 2 h, por exemplo, a incandescente já gastaria 150 Wh (B).</p>"},
33: {"materia": "Física", "assunto": "Hidrostática", "tags": ["vasos comunicantes"],
     "enunciado": enun(R, 33, figs={"p16-1": 1}),
     "imagens": [{"arquivo": "q33", "alt": "Cisterna com três caixas cúbicas lado a lado. Um cano de entrada da água da chuva chega à primeira caixa. A primeira e a segunda estão ligadas por um cano no meio da altura; a segunda e a terceira, por um cano rente ao fundo. Na terceira há uma torneira perto do fundo. Abaixo, o modelo esquemático vazio, visto de frente."},
                 {"arquivo": "q33a", "alt": "Alternativa A: as três caixas com uma camada fina de água no fundo, na altura da torneira."},
                 {"arquivo": "q33b", "alt": "Alternativa B: a primeira caixa com água até a altura do cano que a liga à segunda; a segunda e a terceira com uma camada fina de água, na altura da torneira."},
                 {"arquivo": "q33c", "alt": "Alternativa C: a primeira e a segunda caixas com água até a altura do cano entre elas; a terceira vazia."},
                 {"arquivo": "q33d", "alt": "Alternativa D: a primeira caixa com uma camada fina de água; a segunda e a terceira com água até a metade."},
                 {"arquivo": "q33e", "alt": "Alternativa E: as três caixas com água até a altura do cano entre a primeira e a segunda."}],
     "alternativas": {"A": "[[fig:2]]", "B": "[[fig:3]]", "C": "[[fig:4]]", "D": "[[fig:5]]", "E": "[[fig:6]]"},
     "explicacao": "<p>A segunda e a terceira caixas estão ligadas pelo fundo e funcionam como vasos comunicantes: a água das duas desce junto até a altura da torneira. Já a primeira só se liga à segunda por um cano no meio da altura. Quando o nível da segunda cai abaixo desse cano, a primeira para de escoar e fica com água <strong>até a altura do cano</strong>. Alternativa <strong>B</strong>.</p><p>A primeira caixa não pode esvaziar abaixo do cano de ligação (A e D). A segunda e a terceira têm sempre o mesmo nível, porque se ligam pelo fundo (C). E, com a torneira aberta, a segunda e a terceira não ficam com água até o meio (E).</p>"},
34: {"materia": "Biologia", "assunto": "Ecologia", "tags": ["ciclo do carbono"],
     "enunciado": CARBONO + P34,
     "imagens": [{"arquivo": "q34", "alt": "Esquema circular com dois quadros, “Gás carbônico” em cima e “Matéria orgânica” embaixo. A seta 1, à esquerda, vai do gás carbônico para a matéria orgânica; a seta 2, à direita, vai da matéria orgânica para o gás carbônico."}],
     "explicacao": "<p>A seta 1 leva o carbono do gás carbônico para a matéria orgânica: é a <strong>fotossíntese</strong>, feita pelos autótrofos. A seta 2 devolve o carbono da matéria orgânica ao ambiente como gás carbônico: é a <strong>respiração</strong> (dos próprios produtores, dos consumidores e dos decompositores). Alternativa <strong>C</strong>.</p><p>A decomposição também libera CO<sub>2</sub>, mas não transforma CO<sub>2</sub> em matéria orgânica (A). A fermentação não fixa carbono (B e D). E E inverte o sentido da seta 1.</p>"},
35: {"materia": "Biologia", "assunto": "Ecologia", "tags": ["ciclo do carbono"],
     "enunciado": p("De acordo com o texto, é correto afirmar que"), "apoio_de": (34, P34),
     "explicacao": "<p>O texto diz que, com a morte do organismo, o carbono volta ao ambiente na forma de CO<sub>2</sub> pela “degradação de sua matéria orgânica pelos decompositores”. A <strong>degradação da matéria orgânica pelos seres vivos</strong> devolve o carbono ao meio. Alternativa <strong>C</strong>.</p><p>As plantas usam o gás carbônico na fotossíntese, não na decomposição (A). A fixação do carbono ocorre nos cloroplastos, só em células de autótrofos (B). O aumento atual do carbono na atmosfera vem da queima de combustíveis e do desmatamento, e a fotossíntese retira carbono do ar (D). E a fotossíntese transforma carbono inorgânico em orgânico, não o contrário (E).</p>"},
36: {"materia": "Física", "assunto": "Termologia", "tags": ["escalas termométricas"],
     "enunciado": enun(R, 36, trocas=[("[[FIG:p18-1]]", apoio("Considere que: \\(\\dfrac{\\theta_C}{5} = \\dfrac{\\theta_F - 32}{9}\\), em que \\(\\theta_C\\) é a temperatura medida na escala Celsius e \\(\\theta_F\\) é a temperatura medida na escala Fahrenheit."))], tirar_figs=False),
     "explicacao": "<p>Para 50 ºC: 50/5 = 10, então θ<sub>F</sub> − 32 = 90 e θ<sub>F</sub> = 122 ºF. Para 60 ºC: 60/5 = 12, então θ<sub>F</sub> − 32 = 108 e θ<sub>F</sub> = 140 ºF. Alternativa <strong>D</strong>.</p><p>58 e 68 vêm de somar 8 em vez de usar a fórmula (A e B). 132 ºF corresponderia a cerca de 55,6 ºC (C e E).</p>"},
37: {"materia": "Química", "assunto": "Química ambiental", "tags": ["fertilizantes"],
     "enunciado": apoio(sub(T(18, "Os adubos e fertilizantes", "8% de K2O.")[0], ("P2O5", "P<sub>2</sub>O<sub>5</sub>"), ("K2O", "K<sub>2</sub>O")))
                  + url("https://tinyurl.com/y8qlsygj", "11.04.2018")
                  + p("Por meio da análise do texto, pode-se concluir, corretamente, que o adubo mineral NPK 4–30–16 possui"),
     "explicacao": "<p>No exemplo do texto, NPK 4–14–8 fornece 4% de nitrogênio, 14% de P<sub>2</sub>O<sub>5</sub> e 8% de K<sub>2</sub>O, nessa ordem. Seguindo a mesma regra, NPK 4–30–16 tem <strong>4% de nitrogênio, 30% de P<sub>2</sub>O<sub>5</sub> e 16% de K<sub>2</sub>O</strong>. Alternativa <strong>B</strong>.</p><p>A repete os números do exemplo do texto. C, D e E trocam a ordem dos componentes.</p>"},
38: {"materia": "Física", "assunto": "Termologia", "tags": ["propagação do calor"],
     "enunciado": p("O fogão à lenha possibilita que restos de madeira e de cortes de árvores possam ser utilizados para cozinhar alimentos.",
                    "O calor gerado pela queima da lenha é levado para o interior do fogão em direção a uma chapa de metal devido à ____<strong>I</strong>____. Se um bule descansa sobre a chapa aquecida pelo fogo, sem que receba diretamente a chama da lenha em combustão, o calor é transferido a ele por ____<strong>II</strong>____. Objetos deixados à frente da boca do fogão, como, por exemplo, a própria lenha que será utilizada futuramente como combustível, aquecem-se devido à ____<strong>III</strong>____.")
                  + "[[fig:1]]" + url("https://tinyurl.com/y859ktgc", "21.04.2018", "Original colorido.")
                  + p("As palavras que preenchem, correta e respectivamente, as lacunas estão indicadas na alternativa"),
     "imagens": [{"arquivo": "q38", "alt": "Foto de um fogão à lenha de alvenaria, com a lenha queimando embaixo e, em cima, uma chapa de ferro com bocas, onde estão um bule e duas chaleiras."}],
     "alternativas": colunas(["I", "II", "III"], [["condução", "convecção", "irradiação"], ["convecção", "condução", "irradiação"],
                                                 ["convecção", "irradiação", "condução"], ["irradiação", "condução", "convecção"], ["irradiação", "convecção", "condução"]]),
     "explicacao": "<p>O ar quente da queima sobe e circula dentro do fogão até a chapa: é <strong>convecção</strong> (I). O bule encostado na chapa quente recebe calor pelo contato: é <strong>condução</strong> (II). E a lenha à frente da boca do fogão se aquece pela radiação do fogo, sem contato e sem depender do ar: é <strong>irradiação</strong> (III). Alternativa <strong>B</strong>.</p><p>As outras combinações trocam a ordem desses processos: o contato com a chapa é sempre condução, e o aquecimento à distância diante do fogo é irradiação.</p>"},
39: {"materia": "Química", "assunto": "Substâncias e misturas",
     "enunciado": apoio(sub(T(19, "O alumínio não é encontrado", "maiores do mundo.")[0], ("(Al2O3)", "(Aℓ<sub>2</sub>O<sub>3</sub>)")))
                  + url("https://tinyurl.com/ychwg994", "10.04.2018")
                  + p("O composto presente na bauxita, que leva à produção de alumínio, apresenta"),
     "explicacao": "<p>O composto é o óxido de alumínio, Aℓ<sub>2</sub>O<sub>3</sub>. Ele é formado por <strong>dois elementos químicos</strong>: alumínio (Aℓ) e oxigênio (O). Alternativa <strong>B</strong>.</p><p>Cada unidade de Aℓ<sub>2</sub>O<sub>3</sub> tem cinco átomos, não dois (A), mas só dois elementos (C). E o composto não contém moléculas de alumínio nem de ozônio, O<sub>3</sub> (D e E).</p>"},
40: {"materia": "Matemática", "assunto": "Estatística", "tags": ["média"],
     "enunciado": p("A matemática pode mostrar o porquê reciclar uma latinha de alumínio é importante para o meio ambiente e para a economia no Brasil, pois cada tonelada de latas de alumínio reaproveitada economiza até 95% da energia gasta na sua produção. Isso pode explicar o fato de a lata de alumínio estar entre os materiais recicláveis com maior valor de comércio, bem como os altos índices de reciclagem, que podem ser vistos no quadro:")
                  + p("<strong>Reciclagem – Latas de Alumínio – Brasil</strong>")
                  + tabela(["Anos", "Material Reciclado (em %)"], [["2007", "96,5"], ["2008", "91,5"], ["2009", "98,2"], ["2010", "98,0"], ["2011", "98,3"], ["2012", "97,9"]])
                  + fonte("Fonte dos dados: &lt;https://tinyurl.com/ybobnx7n&gt; Acesso em: 05.03.2018.")
                  + p("A média das porcentagens de reciclagem de latinhas no período demonstrado na tabela é de, aproximadamente,"),
     "explicacao": "<p>Soma: 96,5 + 91,5 + 98,2 + 98,0 + 98,3 + 97,9 = 580,4. Dividindo pelos 6 anos: 580,4 ÷ 6 ≈ <strong>96,7%</strong>. Alternativa <strong>C</strong>.</p><p>91,5% e 98,3% são o menor e o maior valor da tabela (A e E), e 97,9% é o último ano (D).</p>"},
41: {"materia": "Geografia", "assunto": "Globalização", "tags": ["sustentabilidade corporativa"],
     "enunciado": apoio(*[it(x, "The Global 100") for x in T(19, "A Corporate Knights, publicação", "figuravam no levantamento.", ["O levantamento foi criado", "Cinco companhias"])])
                  + url("https://tinyurl.com/y7c3u555", "09.04.2018")
                  + p("Baseando-se no texto, é possível afirmar corretamente que"),
     "explicacao": "<p>Em 2017 havia duas empresas brasileiras na lista, e em 2018 passaram a ser cinco. O aumento foi de 3 sobre 2, ou seja, <strong>150%</strong>, mais de cem por cento. Alternativa <strong>B</strong>.</p><p>O texto diz que a lista inclui empresas “de todos os setores” (A). Emitir muito carbono piora a avaliação (C). O ranking é anunciado no Fórum Econômico Mundial, não no Fórum Social, e é feito pela Corporate Knights (D). E a publicação é canadense, não europeia (E).</p>"},
42: {"materia": "Matemática", "assunto": "Razão e proporção",
     "explicacao": "<p>50 kg de vidro viram 125 garrafas. Como 5 garrafas viram 40 copos, cada garrafa equivale a 8 copos. Então 125 garrafas equivalem a 125 · 8 = <strong>1 000 copos</strong>. Alternativa <strong>C</strong>.</p><p>15 625 vem de multiplicar 125 por 125 (A). 1 600 vem de multiplicar 40 por 40 (B). E 160 e 100 não usam todas as garrafas (D e E).</p>"},
43: {"materia": "Matemática", "assunto": "Equações", "tags": ["equação do 2º grau"],
     "explicacao": "<p>Seja <em>t</em> o tempo habitual. A velocidade habitual é 630/<em>t</em>, e no dia diferente ela foi 630/(<em>t</em> − 4). A diferença é 10 km/h: 630/(<em>t</em> − 4) − 630/<em>t</em> = 10. Isso dá 630 · 4 = 10 · <em>t</em>(<em>t</em> − 4), ou <em>t</em>² − 4<em>t</em> − 252 = 0, cuja raiz positiva é <em>t</em> = <strong>18 h</strong>. Conferindo: 630 ÷ 18 = 35 km/h e 630 ÷ 14 = 45 km/h, 10 km/h a mais. Alternativa <strong>E</strong>.</p><p>14 h é o tempo do dia excepcional, não o habitual (A). Os outros valores não dão diferença de 10 km/h.</p>"},
44: {"materia": "História", "assunto": "Brasil Colônia", "tags": ["mercantilismo"],
     "explicacao": "<p>A política econômica das monarquias europeias dos séculos XVI a XVIII foi o <strong>mercantilismo</strong>: acumular metais preciosos (metalismo), proteger a produção nacional e controlar as colônias pelo pacto colonial. Alternativa <strong>E</strong>.</p><p>Materialismo, autoritarismo e maniqueísmo não são políticas econômicas (A, B e C). E o liberalismo, de livre concorrência, surgiu no século XVIII justamente como crítica ao mercantilismo (D).</p>"},
45: {"materia": "Química", "assunto": "Estrutura atômica", "tags": ["símbolos dos elementos"],
     "enunciado": p("Os símbolos dos elementos químicos ouro e prata são"),
     "alternativas": colunas(["Ouro", "Prata"], [["O", "P"], ["Ou", "Ag"], ["Au", "Ag"], ["Ou", "Pt"], ["Au", "Pt"]]),
     "explicacao": "<p>Os símbolos vêm dos nomes em latim: ouro é <em>aurum</em>, <strong>Au</strong>; prata é <em>argentum</em>, <strong>Ag</strong>. Alternativa <strong>C</strong>.</p><p>O é o oxigênio e P, o fósforo (A). “Ou” não é símbolo de nenhum elemento (B e D). E Pt é a platina (D e E).</p>"},
46: {"materia": "Português", "assunto": "Interpretação de texto",
     "enunciado": PUNK + P46,
     "explicacao": "<p>João Gordo diz que o punk “vai contra a lógica burguesa de consumir”, e os “freeganos” evitam o desperdício reaproveitando alimentos descartados. Os dois têm <strong>atitudes contrárias à lógica do consumo</strong>. Alternativa <strong>E</strong>.</p><p>O texto não fala em rejeitar lutas de minorias (A). Os dois se preocupam com o meio ambiente, não o combatem (B). Os punks são contra a lógica burguesa, não a apoiam (C). E ambos questionam o consumo atual, não querem mantê-lo (D).</p>"},
47: {"materia": "Português", "assunto": "Formação de palavras",
     "enunciado": p("Os termos “freeganismo” e “freegano” são neologismos formados a partir da junção de dois radicas: “free” e “vegan”.", "O processo de formação dessa palavra também ocorre em"),
     "apoio_de": (46, P46),
     "explicacao": "<p>“Freegano” junta duas palavras e perde parte delas (<em>free</em> + <em>vegan</em>): é composição por <strong>aglutinação</strong>. “<strong>Embora</strong>” também se formou assim, de “em boa hora”. Alternativa <strong>A</strong>.</p><p>“Vocalista” (vocal + -ista) e “climáticas” (clima + -ático) são derivações por sufixo (B e C). “Desmatamento” tem prefixo e sufixo (D). E “refrigerado” vem do verbo “refrigerar”, com sufixo de particípio (E).</p>"},
48: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["Constituição de 1988"],
     "enunciado": apoio(*T(22, "O princípio de desenvolvimento sustentável", "local, regional e mundial.", ["Todos têm o direito", "No artigo, é possível", "No entanto, o efetivo"]))
                  .replace("Todos têm o direito", "<em>Todos têm o direito").replace("e futuras gerações.", "e futuras gerações.</em>")
                  + url("https://tinyurl.com/ybt4efsu", "09.04.2018")
                  + p("De acordo com o texto, é correto afirmar que"),
     "explicacao": "<p>O texto diz que a Constituição de 1988 dedicou, “pela primeira vez, um capítulo inteiro ao tema Meio Ambiente”, e que seu artigo 225 afirma: “Todos têm o direito ao meio ambiente ecologicamente equilibrado”. Alternativa <strong>E</strong>.</p><p>A Constituição de 1988 está em vigor até hoje (A). O texto não diz que o uso dos recursos naturais contraria a sustentabilidade (B). Ele afirma que o modelo sustentável ainda “pressupõe” ações efetivas, e não que a Constituição já o garanta (C). E o artigo impõe o dever ao poder público e à coletividade (D).</p>"},
49: {"materia": "Geografia", "assunto": "Biomas brasileiros", "tags": ["Floresta Amazônica"],
     "enunciado": MAMIRAUA + P49,
     "explicacao": "<p>A reserva Mamirauá fica na Amazônia, na várzea do rio Solimões. A Floresta Amazônica é uma vegetação <strong>heterogênea</strong> (muitas espécies), <strong>com árvores altas</strong> e em clima quente e <strong>úmido</strong>. Alternativa <strong>D</strong>.</p><p>Coníferas formam a Mata de Araucárias, no Sul (A). Vegetação rasteira em ambiente seco lembra campos e o semiárido (B e C). E a vegetação arbustiva de ambiente seco é a caatinga ou parte do cerrado (E).</p>"},
50: {"materia": "Geografia", "assunto": "Biomas brasileiros", "tags": ["unidades de conservação"],
     "enunciado": p("De acordo com o texto, um dos objetivos da reserva Mamirauá é"), "apoio_de": (49, P49),
     "explicacao": "<p>A reserva quer “conciliar a conservação da biodiversidade com o desenvolvimento sustentável”, e o texto destaca a várzea e a dinâmica das águas como o componente mais importante do ecossistema. <strong>Proteger as áreas de várzea</strong> é um dos objetivos. Alternativa <strong>B</strong>.</p><p>A reserva concilia desenvolvimento e conservação, não desmatamento (A). A diversidade de habitats é sua característica fundamental, não algo a reduzir (C). A variação de seca e cheia é natural e determina a vida na várzea (D). E a reserva é “habitada também por populações humanas” (E).</p>"},
}
completar(Q, R)
