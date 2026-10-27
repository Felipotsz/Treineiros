# Ajustes da conferência humana: Vestibulinho ETEC 1º semestre de 2026 (exame de 30/11/2025)
# Refeito em 23/10/2026 (a primeira versão se perdeu no reinício do ambiente). Texto conferido com as páginas.
# Tema implícito: a relação entre seres humanos e animais (sem texto de apresentação na prova).
# A letra de "Passaredo" (Q21 a Q24) fica como imagem; o alt descreve sem transcrever.
# Gabarito: oficial (1º SEM/26). Sem anuladas.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import A, carregar, enun, tabela, colunas, completar, trecho

ID = "etec-2026-1sem"
META = {
    "id": ID,
    "banca": "ETEC",
    "ano": 2026,
    "semestre": 1,
    "titulo": "Vestibulinho ETEC, 1º semestre de 2026",
    "fonte": "Centro Paula Souza",
    "dataExame": "2025-11-30",
    "duracaoMinutos": 240,
    "tema": "Seres humanos e animais",
    "pdf": f"assets/provas/{ID}.pdf",
}

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


def figs_alt(primeira=1):
    return {l: f"[[fig:{primeira + i}]]" for i, l in enumerate("ABCDE")}


def sem_fonte_em_apoio(h):
    """O rascunho às vezes põe o crédito da fonte dentro da caixa de apoio."""
    import re
    return re.sub(r'<p class="apoio">(&lt;https?://[^<]*)</p>', r'<p class="fonte">\1</p>', h)


# ---------- textos compartilhados ----------
CAES = (chamada("Leia o texto para responder às questões 02 e 03.")
        + apoio(T(2, "Cães-guia são treinados", "Golden Retriever (16).")[0])
        + url("https://tinyurl.com/4ts3d877", "05.04.2025"))
P2 = p("De acordo com o texto e considerando que existem atualmente, no Brasil, cerca de 6,5 milhões de pessoas com deficiência visual, assinale a alternativa que apresenta a melhor aproximação da razão entre o número de cães-guia em atividade e o número de pessoas com deficiência visual em nosso país, respectivamente.")

PASSAREDO = (chamada("Leia o trecho da canção <em>Passaredo</em>, de Chico Buarque de Hollanda e Francis Hime, para responder às questões de 21 a 24.")
             + "[[fig:1]]")
PASSAREDO_IMG = {"arquivo": "q21", "alt": "Trecho da letra da canção “Passaredo”, de Chico Buarque e Francis Hime, com 17 versos numerados de 5 em 5. O eu lírico chama, um a um, pássaros brasileiros (quero-quero, tico-tico, anum, pardal, chapim, cotovia, ave-fria, pescador-martim, rolinha, andorinha, bem-te-vi, bicudo, sanhaço, juriti) e lhes dá ordens como “Xô”, “Some”, “Anda”, “Te esconde”, “Voa”, pedindo bico calado e muito cuidado. No verso 15, a palavra “Que”, em negrito, introduz o aviso de que o homem vem aí, repetido nos últimos versos. Fonte: &lt;https://tinyurl.com/3ucpw292&gt;, acesso em 10.04.2025."}
P21 = p("A letra da canção nos remete à")

FEROMONIO = (chamada("Leia o texto para responder às questões 36 e 37.")
             + apoio(*T(17, "Os feromônios são substâncias", "dificultar sua proliferação.", ["Entre mulheres", "Na agricultura brasileira"]),
                     "Fórmula estrutural do feromônio do percevejo escuro:")
             + "[[fig:1]]" + url("https://tinyurl.com/2nyw4rb9", "10.04.2025"))
FEROMONIO_IMG = {"arquivo": "q36", "alt": "Fórmula estrutural do feromônio: cadeia CH₃–CH₂–CH(OH)–CH(CH₃)–C(=O)–CH₂–CH₃, com um grupo OH no terceiro carbono, um grupo CH₃ no quarto e um oxigênio em ligação dupla no quinto carbono."}
P36 = p("Baseando-se no texto, é correto afirmar que")

Q = {
1: {"materia": "Biologia", "assunto": "Evolução", "tags": ["domesticação"],
    "enunciado": sem_fonte_em_apoio(R[1]["enunciado"]),
    "alternativas": {"A": "ocorreu recentemente, no período medieval, e foi possível devido à invenção da linguagem e das ferramentas de pedra.",
                     "B": "causou danos à saúde humana, que não estava preparada para o consumo de leite na vida adulta, diminuindo a expectativa média de vida do homem contemporâneo.",
                     "C": "aumentou os níveis naturais de intolerância a lactose no homem pré-histórico devido às diferenças entre o leite materno e o leite de vaca.",
                     "D": "contribuiu para o desenvolvimento de aspectos culturais que favoreceram a evolução humana, como a criação de ferramentas e da linguagem.",
                     "E": "provocou saltos evolutivos que atrasaram o desenvolvimento da linguagem e da tecnologia."},
    "explicacao": "<p>O texto diz que a domesticação “conecta grandes saltos evolutivos, como o desenvolvimento de ferramentas e até da linguagem”. Ela <strong>contribuiu para aspectos culturais que favoreceram a evolução humana</strong>. Alternativa <strong>D</strong>.</p><p>A domesticação é pré-histórica, muito anterior à Idade Média (A). O texto diz que o corpo se adaptou ao leite, sem falar em danos à saúde (B). A convivência com o gado reduziu, e não aumentou, a intolerância à lactose (C). E os saltos evolutivos favoreceram, não atrasaram, a linguagem e as ferramentas (E).</p>"},
2: {"materia": "Matemática", "assunto": "Razão e proporção",
    "enunciado": CAES + P2,
    "alternativas": {"A": "1 para cada 29 000", "B": "1 para cada 30 500", "C": "1 para cada 31 400", "D": "1 para cada 31 800", "E": "1 para cada 32 700"},
    "explicacao": "<p>São 207 cães-guia para 6,5 milhões de pessoas: 6 500 000 ÷ 207 ≈ 31 401. Há cerca de <strong>1 cão-guia para cada 31 400</strong> pessoas com deficiência visual. Alternativa <strong>C</strong>.</p><p>Os outros valores vêm de arredondar errado o número de cães ou de pessoas.</p>"},
3: {"materia": "Matemática", "assunto": "Estatística", "tags": ["gráfico de setores", "porcentagem"],
    "enunciado": p("Com base nos dados sobre as raças, assinale a alternativa que apresenta o gráfico de setor que melhor representa a distribuição de cães-guia."),
    "apoio_de": (2, P2),
    "imagens": [{"arquivo": f"q03{l}", "alt": a} for l, a in zip("abcde", [
        "Gráfico de setores A: Labradores 77 %, Outras raças 16 %, Golden Retriever 8 %.",
        "Gráfico de setores B: Labradores 77 %, Golden Retriever 16 %, Outras raças 8 %.",
        "Gráfico de setores C: Labradores 33 %, Golden Retriever 33 %, Outras raças 33 %.",
        "Gráfico de setores D: Labradores 74 %, Outras raças 18 %, Golden Retriever 8 %.",
        "Gráfico de setores E: Labradores 74 %, Golden Retriever 18 %, Outras raças 8 %."])],
    "alternativas": figs_alt(1),
    "explicacao": "<p>Labradores: 153 ÷ 207 ≈ 74 %. Golden Retriever: 16 ÷ 207 ≈ 8 %. Outras raças: 207 − 153 − 16 = 38, e 38 ÷ 207 ≈ 18 %. O gráfico com <strong>74 %, 8 % e 18 %</strong> é o da alternativa <strong>D</strong>.</p><p>A e B têm 77 % de Labradores, e a soma passaria de 100 %. C divide em partes iguais. E troca os valores de Golden Retriever e outras raças.</p>"},
4: {"materia": "Português", "assunto": "Texto literário",
    "enunciado": R[4]["enunciado"].replace('<p class="apoio">LISPECTOR', '<p class="fonte">LISPECTOR'),
    "explicacao": "<p>Para a narradora, o cão “só fica ‘sendo’. ‘Ser’ é a sua atividade”. Ele <strong>vive plenamente</strong>, sem angústias, e por isso “ensina a viver”. Alternativa <strong>E</strong>.</p><p>O texto não fala de submissão (A e B), de inquietação (C), nem de deixar alguém tenso; ao contrário, o cão “revigora” (D).</p>"},
5: {"materia": "História", "assunto": "Antiguidade", "tags": ["Egito"],
    "explicacao": "<p>O texto diz que os egípcios admiravam nos felinos “graça, fertilidade e cuidado suave com agressão, rapidez e perigo”, e que os deuses ligados a essas qualidades eram representados com características felinas. Alternativa <strong>A</strong>.</p><p>Os felinos também tinham valor simbólico, não só prático (B). Os felinos maiores é que eram símbolos da realeza (C). A natureza dual era admirada, não evitada (D). E o texto não fala em superioridade humana (E).</p>"},
6: {"materia": "Biologia", "assunto": "Fisiologia humana", "tags": ["saúde mental"],
    "explicacao": "<p>O texto diz que as intervenções com animais destinadas a crianças trazem “melhora na convivência social, na capacidade de concentração e nas habilidades de comunicação”, e que a convivência com pets ajuda no desenvolvimento afetivo e psicológico. Alternativa <strong>E</strong>.</p><p>O texto não diz que o acompanhamento emocional fica dispensável (A), nem fala de isolamento (B), de dispensar remédios, exercícios e dieta (C) ou de prejuízo à organização (D).</p>"},
7: {"materia": "História", "assunto": "História contemporânea", "tags": ["Guerra Fria", "corrida espacial"],
    "enunciado": R[7]["enunciado"].replace('<p class="apoio">&lt;https://tinyurl.com/3c27jds9&gt;.', '<p class="fonte">&lt;https://tinyurl.com/3c27jds9&gt;.'),
    "explicacao": "<p>O envio de animais e depois de pessoas ao espaço, por URSS e Estados Unidos, entre 1948 e 1961, fez parte da <strong>corrida espacial</strong>, uma das disputas da <strong>Guerra Fria</strong>. Alternativa <strong>E</strong>.</p><p>A Primeira Revolução Industrial é do século XVIII (A). A Segunda Guerra terminou em 1945 (B). A Reconstrução Europeia não trata de viagens espaciais (C). E as Grandes Navegações são dos séculos XV e XVI (D).</p>"},
8: {"materia": "Português", "assunto": "Interpretação de texto",
    "explicacao": "<p>O texto diz que, na aldeia das irmãs, a relação com os animais é “baseada no cuidado mútuo” e que “sem natureza e animais, nada progride”. A relação com a fauna e a flora é <strong>essencial para uma vivência harmônica</strong>. Alternativa <strong>D</strong>.</p><p>“Xerimbabos” são os animais queridos, não as crianças (A). O bicho-preguiça provocou encanto, não trauma (B). O texto não fala de desequilíbrio ecológico (C). E nas aldeias “não há pets do jeito como vemos nas cidades” (E).</p>"},
9: {"materia": "Biologia", "assunto": "Ecologia", "tags": ["cadeia alimentar"],
    "explicacao": "<p>A onça é um predador de topo: come herbívoros maiores e predadores menores e, assim, controla essas populações, mantendo o <strong>equilíbrio ambiental</strong>. Alternativa <strong>D</strong>.</p><p>Aves não têm pelos, e nem todas são carnívoras (A). Os xerimbabos não são criados para abate (B) nem ficam em cativeiro (C). E cobras e tartarugas não mantêm a temperatura do corpo constante, e sabiás não são carnívoros (E).</p>"},
10: {"materia": "Português", "assunto": "Classes de palavras", "tags": ["adjuntos adverbiais"],
     "explicacao": "<p>“Certa manhã” indica <strong>tempo</strong>; “no Pará”, <strong>lugar</strong>; “com as meninas”, <strong>companhia</strong>; e “Nas aldeias”, <strong>lugar</strong>. Alternativa <strong>E</strong>.</p><p>“No Pará” não indica origem (A e C) nem destino (B e D). “Com as meninas” não é causa, instrumento nem ferramenta (A, B e D). E “Certa manhã” não é condição nem consequência (B, C e D).</p>"},
11: {"materia": "Português", "assunto": "Verbos", "tags": ["locução verbal"],
     "explicacao": "<p>Em “acabou indo com o seu bando”, o verbo “acabar” mostra que a ação de ir aconteceu ao final de um processo, como desfecho. É <strong>uma ação finalizada</strong>, destacada como conclusão. Alternativa <strong>C</strong>.</p><p>A ação não se repete (A) nem se prolonga sem fim (B). Não indica início (D). E a ação se concretizou: a capivara foi com o bando (E).</p>"},
12: {"materia": "Português", "assunto": "Coesão e referência", "tags": ["pronomes"],
     "enunciado": R[12]["enunciado"].replace("A relação com eles é de cuidado", "A relação com <u>eles</u> é de cuidado")
                  .replace("O pronome eles, sublinhado", "O pronome <u>eles</u>, sublinhado"),
     "alternativas": {"A": "“territórios” e “<em>pets</em>”.", "B": "“<em>pets</em>” e “adultos”.", "C": "“indígenas” e “animais”.", "D": "“<em>pets</em>” e “animais”.", "E": "“territórios” e “adultos”."},
     "explicacao": "<p>No quarto parágrafo, o texto fala que não há <em>pets</em> nas aldeias e que “os animais vivem soltos na floresta” e “podem voltar para a mata”. Em seguida, “a relação com <u>eles</u>” retoma esses seres: os <strong><em>pets</em></strong> (no sentido de bichos de estimação) e os <strong>animais</strong>. Alternativa <strong>D</strong>.</p><p>“Territórios”, “adultos” e “indígenas” não são aquilo com que se tem uma relação de cuidado no trecho (A, B, C e E).</p>"},
13: {"materia": "Matemática", "assunto": "Operações e problemas",
     "explicacao": "<p>Cada cavalo trabalha até 3 h por dia, em 4 dias (terça a sexta): 12 cavalos · 3 h · 4 dias = 144 h por semana. Cada sessão dura 0,5 h, então são 288 sessões. Como cada pessoa faz 2 sessões por semana, o máximo é 288 ÷ 2 = <strong>144 pessoas</strong>. Alternativa <strong>A</strong>.</p><p>288 é o número de sessões, não de pessoas (C). Contar 5 dias de atendimento daria 180 pessoas (B).</p>"},
14: {"materia": "Biologia", "assunto": "Evolução", "tags": ["dinossauros", "tirinha"],
     "enunciado": enun(R, 14, figs={"p08-1": 1}).replace("<p>Criado por", url("https://tinyurl.com/muvuuzb", "24.05.2025", "") + "<p>Criado por"),
     "imagens": [{"arquivo": "q14", "alt": "Tirinha “Piteco”, de Mauricio de Sousa, em quatro quadrinhos. Uma mulher pré-histórica vê uma pedra estalando e se pergunta que maluquice é aquela. Piteco percebe que é um ovo de dinossauro semienterrado, que está picando. Do ovo nasce um filhote de dinossauro, e ela diz: “Bem, ‘seu’ bebê, até a vista… e felicidades!” O filhote pergunta onde estava e se encanta por ela, que acha que ele tem um modo de assustar."}],
     "explicacao": "<p>A tirinha mostra homens das cavernas convivendo com um filhote de dinossauro. Mas os dinossauros (não aves) <strong>foram extintos há cerca de 66 milhões de anos</strong>, muito antes do surgimento dos primeiros hominídeos, há poucos milhões de anos. Alternativa <strong>D</strong>.</p><p>Dinossauros punham ovos (A). Eles nunca conviveram com seres humanos (B). O texto não fala de ovos inteiramente enterrados (C). E dinossauros não eram animais domésticos (E).</p>"},
15: {"materia": "Biologia", "assunto": "Citologia", "tags": ["respiração celular"],
     "explicacao": "<p>Na respiração aeróbica, a glicose reage com o oxigênio e libera energia, formando <strong>gás carbônico (CO<sub>2</sub>)</strong> e água. Alternativa <strong>A</strong>.</p><p>Monóxido de carbono se forma na combustão incompleta, não na respiração (B). Nitrogênio, hidrogênio e ozônio não são produtos desse processo (C, D e E).</p>"},
16: {"materia": "Química", "assunto": "Substâncias e misturas",
     "explicacao": "<p>O oxigênio (O<sub>2</sub>) tem um só elemento: é <strong>substância simples</strong>. A glicose (C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>) tem três elementos: é <strong>substância composta</strong>. Alternativa <strong>B</strong>.</p><p>A inverte a classificação. O O<sub>2</sub> não é composto (C e D). E a glicose pura não é mistura (D e E).</p>"},
17: {"materia": "Geografia", "assunto": "Tectônica de placas", "tags": ["deriva continental"],
     "explicacao": "<p>O argumento <strong>paleontológico</strong> de Wegener é a existência de <strong>fósseis iguais</strong> (como o do réptil <em>Mesosaurus</em>) em continentes hoje separados por oceanos, como a América do Sul e a África. Alternativa <strong>C</strong>.</p><p>Formações geomorfológicas semelhantes são um argumento geológico, não paleontológico (B). E a água doce, os navios e o encaixe entre Ásia e América do Sul não sustentam a teoria (A, D e E); o encaixe citado por Wegener é entre América do Sul e África.</p>"},
18: {"materia": "Física", "assunto": "Magnetismo", "tags": ["campo magnético terrestre"],
     "explicacao": "<p>O texto diz que o polo Sul magnético fica perto do polo Norte geográfico. O Canadá fica perto do polo Norte geográfico, portanto perto do <strong>polo Sul magnético</strong>; e, ao ir para o Brasil, a ave segue no <strong>sentido do polo Sul geográfico</strong>. Alternativa <strong>A</strong>.</p><p>Não existem “linhas de campo geográfico” (B). Ir do Canadá ao Brasil é cruzar latitudes, não seguir paralelo a elas (C). As estruturas percebem o campo magnético, não funcionam como bússolas elétricas (D). E as aves não usam GPS (E).</p>"},
19: {"materia": "Matemática", "assunto": "Notação científica",
     "enunciado": sem_fonte_em_apoio(R[19]["enunciado"]).split("<p>–")[0]
                  + p("Sabendo que 1 µT = 1 × 10<sup>–6</sup> T, assinale a alternativa que apresenta corretamente, em notação científica, a densidade média de fluxo magnético de um imã de geladeira, em T."),
     "alternativas": {"A": "5,0 × 10<sup>–9</sup>", "B": "0,5 × 10<sup>–6</sup>", "C": "5,0 × 10<sup>–6</sup>", "D": "0,5 × 10<sup>–3</sup>", "E": "5,0 × 10<sup>–3</sup>"},
     "explicacao": "<p>O campo da Terra (50 µT) é um centésimo do ímã de geladeira, então o ímã tem 100 · 50 µT = 5 000 µT = 5 000 · 10<sup>–6</sup> T = <strong>5,0 · 10<sup>–3</sup> T</strong>. Alternativa <strong>E</strong>.</p><p>C é o valor do campo da Terra mal convertido. B e D não estão em notação científica (o número deve ficar entre 1 e 10). E A divide em vez de multiplicar por 100.</p>"},
20: {"materia": "Geografia", "assunto": "Cartografia", "tags": ["pontos cardeais"],
     "enunciado": enun(R, 20, figs={"p11-1": 1}).replace("<p>km</p>", ""),
     "imagens": [{"arquivo": "q20", "alt": "Mapa político do Brasil com a sigla de cada estado, a escala (0 a 1 000 km) e a rosa dos ventos indicando o norte. Sergipe fica no litoral do Nordeste, a leste; Goiás fica no Centro-Oeste, a sudoeste de Sergipe."}],
     "explicacao": "<p>Sergipe fica no litoral do Nordeste, e Goiás, no Centro-Oeste, mais ao sul e mais a oeste. Indo de Sergipe para Goiás, o beija-flor voa para o <strong>sudoeste</strong>. Alternativa <strong>C</strong>.</p><p>Noroeste levaria ao norte do país (A). Nordeste e leste levariam ao oceano (B e E). E sudeste levaria ao litoral do Sudeste (D).</p>"},
21: {"materia": "Português", "assunto": "Interpretação de texto", "tags": ["canção"],
     "enunciado": PASSAREDO + P21, "imagens": [PASSAREDO_IMG],
     "explicacao": "<p>A canção manda os pássaros fugirem e se esconderem, “Que o homem vem aí”. Ela remete à <strong>destruição da natureza causada pelos seres humanos</strong>. Alternativa <strong>D</strong>.</p><p>A ameaça vem do homem, não dos pássaros (A e C). A relação não é harmoniosa (B). E a canção não fala de viveiros (E).</p>"},
22: {"materia": "Português", "assunto": "Figuras de linguagem", "tags": ["canção"],
     "enunciado": p("O título da canção apresentada se justifica pela"), "apoio_de": (21, P21),
     "explicacao": "<p>“Passaredo” é um conjunto de pássaros, e a letra é uma longa <strong>enumeração de nomes de aves</strong> (quero-quero, tico-tico, anum, pardal…), mostrando a diversidade delas. Alternativa <strong>E</strong>.</p><p>Quem é expulso são os pássaros, não os humanos (A). O tamanho dos versos e as vogais fechadas não explicam o título (B e C). E as repetições não indicam a posição dos animais nas árvores (D).</p>"},
23: {"materia": "Português", "assunto": "Conectivos",
     "enunciado": p("Assinale a alternativa que apresenta um sinônimo para o termo destacado em negrito na canção."), "apoio_de": (21, P21),
     "alternativas": {"A": "<strong>porque</strong>", "B": "<strong>ainda que</strong>", "C": "<strong>desde que</strong>", "D": "<strong>contanto que</strong>", "E": "<strong>à medida que</strong>"},
     "explicacao": "<p>Em “Muito cuidado / <strong>Que</strong> o homem vem aí”, o “que” explica o motivo do cuidado: equivale a <strong>porque</strong>. Alternativa <strong>A</strong>.</p><p>“Ainda que” indica concessão (B). “Desde que” e “contanto que” indicam condição (C e D). E “à medida que” indica proporção (E).</p>"},
24: {"materia": "Português", "assunto": "Funções da linguagem", "tags": ["imperativo", "vocativo"],
     "enunciado": p("A canção apresentada se utiliza tanto de imperativos, como em “some”, “anda” e “te esconde”, quanto de vocativos, como em “rolinha”, “andorinha” e “ bem-te-vi”, com o objetivo de"),
     "apoio_de": (21, P21),
     "explicacao": "<p>Os vocativos chamam os pássaros e os imperativos dão ordens a eles (“some”, “te esconde”). O eu lírico quer <strong>convencer os pássaros a fugir para se proteger</strong> do homem que vem aí. Alternativa <strong>C</strong>.</p><p>O foco não está nas emoções do eu lírico (A) nem na preservação da humanidade (B). A sonoridade existe, mas não é o objetivo dos imperativos e vocativos (D). E pássaros são fauna, não flora (E).</p>"},
25: {"materia": "Biologia", "assunto": "Fisiologia animal", "tags": ["visão"],
     "explicacao": "<p>A águia tem cerca de 1 milhão de cones por mm², contra 200 000 no ser humano, e enxerga quatro cores primárias e ainda o ultravioleta. Ela <strong>enxerga mais cores e com melhor definição</strong> que o ser humano. Alternativa <strong>E</strong>.</p><p>Ela distingue cores (A e B). O texto fala em UV, não em infravermelho, e não diz que o ser humano tem vantagem (C). E sua acuidade é cerca de cinco vezes maior, não menor (D).</p>"},
26: {"materia": "Geografia", "assunto": "Climatologia", "tags": ["correntes marítimas"],
     "explicacao": "<p>No litoral do Chile e do Peru, no Pacífico, atua a <strong>corrente fria de Humboldt</strong>, também chamada <strong>corrente do Peru</strong>. Ela provoca a ressurgência (muitos peixes) e deixa a costa muito seca, como no deserto do Atacama. Alternativa <strong>E</strong>.</p><p>A corrente da Califórnia fica na América do Norte (A). A Antártica circula o continente gelado (B). A de Benguela fica na costa da África (C). E a do Brasil é quente e fica no Atlântico (D).</p>"},
27: {"materia": "Matemática", "assunto": "Geometria espacial", "tags": ["volume do cilindro"],
     "enunciado": apoio("Em algumas espécies de aves, o design das penas permite alterar a trajetória da luz devido à presença de conjuntos de nanoestruturas semelhantes a cristais. Esse fenômeno é chamado iridescência ou coloração estrutural e está ligado a estruturas denominadas melanossomos.")
                  + url("https://tinyurl.com/3wc2mwes", "05.04.2025")
                  + p("Considere que as penas de um tipo de ave possui melanossomos cilíndricos cujo diâmetro mede 300 nm e altura 500 nm.",
                      "Assinale a alternativa que apresenta a expressão matemática que deve ser multiplicada pelo número irracional π para calcular o volume desse melanossomo, em nm<sup>3</sup>."),
     "alternativas": {"A": "150<sup>2</sup> × 500", "B": "250<sup>2</sup> × 300", "C": "300<sup>2</sup> × 500", "D": "500<sup>2</sup> × 300", "E": "600<sup>2</sup> × 500"},
     "explicacao": "<p>O volume do cilindro é V = π · r² · h. O raio é metade do diâmetro: 300 ÷ 2 = 150 nm, e a altura é 500 nm. Então V = π · <strong>150² × 500</strong>. Alternativa <strong>A</strong>.</p><p>C usa o diâmetro no lugar do raio. E usa o dobro do diâmetro. B e D trocam ou inventam as medidas.</p>"},
28: {"materia": "Química", "assunto": "Substâncias e misturas",
     "explicacao": "<p>A água (H<sub>2</sub>O) é uma substância composta: cada molécula tem <strong>2 átomos de hidrogênio ligados a 1 de oxigênio</strong>. Alternativa <strong>E</strong>.</p><p>Água não é mistura de átomos nem de gases (A e B). Tem 2 elementos, não 3 (C). E não contém moléculas de H<sub>2</sub> e O<sub>2</sub> (D).</p>"},
29: {"materia": "Biologia", "assunto": "Zoologia", "tags": ["mamíferos", "espécies invasoras"],
     "explicacao": "<p>O texto diz que os ratões-do-banhado são usados na produção de carne (fonte de proteína) e têm patas palmeadas e são ágeis na água: <strong>adaptações para nadar</strong>, apesar de serem mamíferos que vivem em terra firme. Alternativa <strong>B</strong>.</p><p>São roedores, não primatas, e como invasores causam desequilíbrio (A). Os dentes alaranjados são incisivos de roedor herbívoro, não caninos de carnívoro (C). Não são ruminantes (D). E fora de sua região causam desequilíbrio (E).</p>"},
30: {"materia": "Química", "assunto": "Ácidos e bases", "tags": ["pH", "indicadores"],
     "enunciado": enun(R, 30, figs={"p15-1": 1}),
     "imagens": [{"arquivo": "q30", "alt": "Escala de pH de 0 a 14. De 0 a 7, pH ácido, em que o indicador fica vermelho; em 7, neutro, verde; de 7 a 14, pH básico, azul."}],
     "explicacao": "<p>pH 2 é bem menor que 7, ou seja, <strong>ácido</strong>. Pela escala, nessa faixa o indicador fica <strong>vermelho</strong>. Alternativa <strong>D</strong>.</p><p>Azul é a cor em meio básico (A e B). Verde é a cor no neutro, pH 7 (C). E pH 2 não é básico (E).</p>"},
31: {"materia": "Matemática", "assunto": "Razão e proporção", "tags": ["velocidade média"],
     "explicacao": "<p>A manada fez 240 ÷ 4 = 60 km/dia, e os humanos, 240 ÷ 6 = 40 km/dia. A <strong>manada foi 20 km/dia mais rápida</strong>. Alternativa <strong>A</strong>.</p><p>A diferença é de 20 km/dia, não 40 (B e D). E os humanos foram mais lentos, não mais rápidos (C e E).</p>"},
32: {"materia": "Geografia", "assunto": "Climatologia", "tags": ["ciclo da água"],
     "explicacao": "<p>O ciclo da água é movido pela <strong>energia do Sol</strong>, que provoca a <strong>evaporação</strong>; o vapor sobe, esfria e sofre <strong>condensação</strong>, formando nuvens e chuva. Alternativa <strong>E</strong>.</p><p>Os ventos, a pressão atmosférica, as rochas vulcânicas e a umidade dos desertos não são o princípio que move o ciclo (A, B, C e D).</p>"},
33: {"materia": "Biologia", "assunto": "Nutrição e saúde",
     "explicacao": "<p>O texto diz que a tilápia tem vitaminas A, B e D e minerais (cálcio, ferro e zinco), e que sua pele é usada como curativo para queimaduras. É <strong>rica em vitaminas e minerais e pode ser usada na medicina</strong>. Alternativa <strong>B</strong>.</p><p>A primeira tilápia chegou ao Ceará vinda do Sudeste, ou seja, não é nativa do Nordeste (A). É criada em água doce (C). O texto não fala de exportação (D). E o DNOCS fez o povoamento dos reservatórios, não a venda (E).</p>"},
34: {"materia": "Biologia", "assunto": "Nutrição e saúde", "tags": ["sais minerais"],
     "explicacao": "<p>O <strong>ferro</strong> é parte da hemoglobina, e por isso é importante para a <strong>formação dos glóbulos vermelhos</strong>. Alternativa <strong>A</strong>.</p><p>A pele de tilápia ajuda a cicatrização (B). Escorbuto vem da falta de vitamina C, e sarampo é uma virose (C). O texto diz que a tilápia é rica, não pobre, em proteínas (D). E cálcio e zinco não previnem febre amarela (E).</p>"},
35: {"materia": "Química", "assunto": "Estrutura atômica",
     "enunciado": p("A hemoglobina é uma proteína presente no sangue de animais vertebrados. Ela contém ferro, que é responsável pelo transporte de oxigênio e é representado por: \\({}^{56}_{26}\\text{Fe}\\).",
                    "Sobre esse elemento, é correto afirmar que apresenta"),
     "explicacao": "<p>Na representação, o número de cima (56) é o <strong>número de massa</strong> e o de baixo (26), o número atômico. Alternativa <strong>A</strong>.</p><p>O número atômico é 26, não 30 (B), e por isso há 26 prótons (C) e, no átomo neutro, 26 elétrons (D). Os nêutrons são 56 − 26 = 30, não 26 (E).</p>"},
36: {"materia": "Química", "assunto": "Funções orgânicas", "tags": ["fórmula molecular", "feromônios"],
     "enunciado": FEROMONIO + P36, "imagens": [FEROMONIO_IMG],
     "alternativas": {"D": "o feromônio sintetizado para controlar pragas no milho apresenta fórmula molecular C<sub>8</sub>H<sub>16</sub>O<sub>2</sub>."},
     "explicacao": "<p>Contando na estrutura: carbonos, 2 + 1 + 1 + 1 (do grupo CH<sub>3</sub> lateral) + 1 + 2 = <strong>8</strong>; hidrogênios, 3 + 2 + 1 + 1 (do OH) + 1 + 3 + 2 + 3 = <strong>16</strong>; oxigênios, <strong>2</strong> (do OH e do C=O). Fórmula: C<sub>8</sub>H<sub>16</sub>O<sub>2</sub>. Alternativa <strong>D</strong>.</p><p>O texto cita feromônios em mulheres (A) e produzidos em laboratório (B). O feromônio usado é o sexual, para atrair o próprio percevejo (C). E a molécula tem 16 hidrogênios e 2 oxigênios (E).</p>"},
37: {"materia": "Química", "assunto": "Química ambiental", "tags": ["controle de pragas"],
     "enunciado": p("O uso desses compostos, na agricultura, está associado"), "apoio_de": (36, P36),
     "explicacao": "<p>Os feromônios atraem só a espécie que os produz, então funcionam como iscas <strong>específicas para a praga</strong>, sem matar outros insetos nem contaminar o ambiente como os agrotóxicos. São <strong>alternativas sustentáveis</strong>. Alternativa <strong>C</strong>.</p><p>Eles não contaminam o solo nem a água (A), não exterminam todos os insetos (B), não são tóxicos para humanos e animais (D) e são usados em pequenas quantidades (E).</p>"},
38: {"materia": "Biologia", "assunto": "Ecologia", "tags": ["polinização"],
     "explicacao": "<p>O texto cita o uso de agrotóxicos entre as causas do risco de extinção das abelhas. Com menos abelhas, há <strong>menos polinização natural</strong>. Alternativa <strong>E</strong>.</p><p>Agrotóxicos não melhoram a polinização (A). O desmatamento reduz o alimento das abelhas (B). Mais flores ajudam as abelhas (C). E doenças diminuem, não aumentam, sua capacidade de voltar à colmeia (D).</p>"},
39: {"materia": "Física", "assunto": "Termologia", "tags": ["isolamento térmico"],
     "explicacao": "<p>A pele de caribu, com pelos que prendem ar, funciona como <strong>isolante térmico</strong>: dificulta a perda de calor do corpo, principalmente pela <strong>convecção</strong> do ar frio junto à pele, e mantém o corpo aquecido. Alternativa <strong>C</strong>.</p><p>A roupa não serve para absorver suor (A). Perder calor esfriaria o corpo (B). Refletir a radiação não aumenta a temperatura (D). E um isolante dificulta, e não facilita, a transferência de calor (E).</p>"},
40: {"materia": "Física", "assunto": "Pressão",
     "explicacao": "<p>Pressão é força dividida pela área. Os cascos largos do camelo <strong>distribuem seu peso por uma área maior</strong>, diminuindo a pressão sobre a areia, e por isso ele não afunda. Alternativa <strong>E</strong>.</p><p>A areia do deserto é seca, e a radiação solar não sustenta o animal (A). A gravidade não diminui nos desertos (B). Condutividade térmica e resistividade elétrica não explicam por que ele não afunda (C e D).</p>"},
41: {"materia": "História", "assunto": "Idade Média", "tags": ["cartografia"],
     "explicacao": "<p>O texto diz que os monstros marinhos dos mapas medievais refletiam “o medo” e a “fascinação pelo desconhecido”, e que foram substituídos por estudos precisos com o avanço da ciência, das navegações e da biologia marinha. Alternativa <strong>B</strong>.</p><p>A visão medieval não era científica (A e D). Os animais marinhos passaram a ser estudados (C). E a cartografia não tem o objetivo de impedir viagens pelo mar (E).</p>"},
42: {"materia": "Geografia", "assunto": "Movimentos da Terra", "tags": ["equinócio", "fake news"],
     "explicacao": "<p>O equinócio é o momento em que o Sol fica sobre o Equador e o <strong>dia e a noite têm cerca de 12 horas</strong> em todo o planeta, por causa da inclinação do eixo da Terra. Ele marca o início da primavera ou do outono e <strong>não causa ondas de calor</strong>. Alternativa <strong>C</strong>.</p><p>As outras alternativas repetem as afirmações falsas da mensagem: calor intenso no hemisfério sul (A), 40 °C às 16 h (B), aumento da atividade solar (D) e necessidade de ficar em casa (E).</p>"},
43: {"materia": "Matemática", "assunto": "Razão e proporção",
     "explicacao": "<p>A massa total é 900 · 250 = 225 000 kg, que correspondem a 225 000 ÷ 450 = 500 UA. Taxa de lotação = 500 UA ÷ 100 ha = <strong>5,0 UA/ha</strong>. Alternativa <strong>B</strong>.</p><p>Usar 900 animais como se fossem 900 UA daria 9,0, que não é alternativa. 2,5 vem de dividir 250 por 100 (A).</p>"},
44: {"materia": "Geografia", "assunto": "Agropecuária e meio ambiente", "tags": ["desmatamento"],
     "explicacao": "<p>O texto diz que grande parte das áreas desmatadas na Amazônia vira pastagem. A <strong>criação de gado é uma das principais causas do desmatamento</strong>, que contribui para as mudanças climáticas, já que as florestas retiram carbono do ar. Alternativa <strong>C</strong>.</p><p>O Brasil é o maior exportador, não importador (A). O desmatamento vem da pastagem, e trigo e feijão não são ração de gado (B). O Brasil responde por quase um quinto das exportações, não 50 % (D). E os 40 % do rebanho estão nos nove estados da Amazônia, não só no Amazonas (E).</p>"},
45: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": ["verminoses"],
     "enunciado": p("Ao consumir a carne suína ou bovina contaminada com cisticercos – quando não ocorre o cozimento adequado – o ser humano pode adquirir uma doença denominada ____<strong>I</strong>____ causada pelo parasita conhecido como ____<strong>II</strong>____.",
                    "Assinale a alternativa que preenche correta e respectivamente os espaços numerados I e II."),
     "alternativas": colunas(["I", "II"], [["ascaridíase", "lombriga"], ["teníase", "solitária"], ["mal de Chagas", "barbeiro"], ["amebíase", "ameba"], ["toxoplasmose", "salmonella"]]),
     "explicacao": "<p>Os cisticercos são larvas da tênia. Ao comer carne mal cozida com essas larvas, a pessoa desenvolve a <strong>teníase</strong>, causada pela <strong>tênia</strong>, conhecida como <strong>solitária</strong>. Alternativa <strong>B</strong>.</p><p>A lombriga causa ascaridíase e é adquirida pela ingestão de ovos (A). O barbeiro transmite a doença de Chagas, causada por um protozoário (C). A ameba é transmitida por água e alimentos contaminados (D). E salmonela é uma bactéria, que não causa toxoplasmose (E).</p>"},
46: {"materia": "História", "assunto": "Imperialismo e neocolonialismo",
     "explicacao": "<p>O texto liga os zoológicos modernos ao imperialismo dos séculos XVIII e XIX, quando potências europeias levavam animais exóticos de suas colônias. Esse processo foi a <strong>expansão territorial, econômica, política e cultural europeia sobre outros continentes</strong>, o <strong>neocolonialismo</strong>. Alternativa <strong>C</strong>.</p><p>Não se trata de revolução cultural educacional (A), de “pão e circo”, que é da Roma Antiga (B), de absolutismo (D) nem de democracia com três poderes (E).</p>"},
47: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["bem-estar animal"],
     "explicacao": "<p>O santuário resgata elefantes de circos, zoológicos e propriedades particulares e cuida da sua recuperação. Isso <strong>promove a empatia e o respeito</strong> pelos elefantes e pelo bem-estar dos animais em geral. Alternativa <strong>D</strong>.</p><p>O santuário não aproxima as pessoas do circo (A), não quer aumentar os elefantes em zoológicos (B), não é causa de desmatamento, pois a área está se regenerando (C), e não incentiva o uso de elefantes em eventos (E).</p>"},
48: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["projeto TAMAR"],
     "explicacao": "<p>O texto diz que o TAMAR envolveu os pescadores na proteção, dialoga “com as práticas e o conhecimento tradicionais” e engaja a comunidade em “questões de cidadania”. Por isso é <strong>bem-sucedido</strong>. Alternativa <strong>D</strong>.</p><p>A preservação foi conciliada com a vida dos pescadores (A). O projeto os capacita para proteger, não para consumir as tartarugas (B). Os pescadores foram convidados a trabalhar, não a sair (C). E o texto diz que os resultados ajudaram a mudar comportamentos (E).</p>"},
49: {"materia": "Biologia", "assunto": "Ecologia", "tags": ["tartarugas marinhas"],
     "explicacao": "<p>A fotopoluição (luz artificial nas praias) é uma das ameaças: os filhotes, que se guiam pela claridade do horizonte sobre o mar, <strong>se desorientam e vão para o continente</strong>, onde morrem. Alternativa <strong>C</strong>.</p><p>As tartarugas passam a maior parte da vida no mar (A). Respiram por pulmões, e por isso morrem afogadas presas em redes (B). A subida do mar destrói ninhos (D). E não há cuidado parental após a desova (E).</p>"},
50: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["cidadania"],
     "explicacao": "<p>Agir com responsabilidade pelo meio ambiente e pelos animais inclui <strong>denunciar maus-tratos, cativeiro ilegal, desmatamentos e queimadas</strong> às autoridades. Alternativa <strong>E</strong>.</p><p>Introduzir espécies invasoras (A), comprar produtos de animais ameaçados (B), combater o reflorestamento (C) e vender animais traficados (D) prejudicam os animais e o ambiente.</p>"},
}
completar(Q, R)
