# Ajustes da conferência humana: Vestibular FATEC 2º semestre de 2018 (exame de 01/07/2018)
# Texto conferido com a imagem de cada página. Tema implícito: Resiliência (redação: o jeitinho brasileiro é resiliência ou falta de honestidade?).
# 54 questões; a prova tem 5 h no total, incluindo a redação (que fica fora do simulado).
# Matéria: a do gabarito oficial; nas "Multidisciplinar", a matéria principal + tag "multidisciplinar".
# Rascunho com colunas embaralhadas: enunciados e alternativas escritos aqui.
# Gabarito: oficial (2º SEM/18); Q32 e Q34 ANULADAS sem motivo publicado (justificativa por análise). Poema de Drummond (Q54) só como imagem.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import A, carregar, enun, tabela, colunas, completar, trecho

ID = "fatec-2018-2sem"
META = {
    "id": ID,
    "banca": "FATEC",
    "ano": 2018,
    "semestre": 2,
    "titulo": "Vestibular FATEC, 2º semestre de 2018",
    "fonte": "Centro Paula Souza",
    "dataExame": "2018-07-01",
    "duracaoMinutos": 300,
    "tema": "Resiliência",
}

R = carregar(ID)
MULTI = ["multidisciplinar"]


def T(pag, inicio, fim, paragrafos=()):
    fix = lambda x: x.replace("ﬀ ", "ff").replace("ﬃ ", "ffi").replace("ﬄ ", "ffl").replace("ﬀ", "ff").replace("ﬃ", "ffi").replace("ﬄ", "ffl")
    return [fix(x) for x in trecho(ID, pag, inicio, fix(fim) if False else fim, paragrafos)]


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

def AL(pag, inicio, fim):
    """Alternativas copiadas do texto do PDF: de '(A) ...' até o fim da (E)."""
    s = " ".join(T(pag, inicio, fim))
    partes = re.split(r"\(([A-E])\)\s*", s)
    d = {partes[i]: partes[i + 1].strip() for i in range(1, len(partes) - 1, 2)}
    assert list(d) == list("ABCDE"), (pag, inicio, list(d))
    return d


# ---------- textos compartilhados ----------
FGV = (chamada("Leia o texto para responder às questões de números 02 e 03.")
       + apoio(*T(2, "Um estudo com 3 707 alunos", "um grau elevado.", ["Nesse estudo, elaborou-se"]))
       + url("https://tinyurl.com/yd8z5kf8", "17.02.2018"))
P2 = p("Assinale a alternativa que apresenta o gráfico que melhor pode representar os dados obtidos pelo questionário aplicado no estudo da FGV.")

BARCARENA = (chamada("Leia o texto e a tabela para responder às questões de números 22 a 24.")
             + apoio(*[x.replace("Pb2+", "Pb<sup>2+</sup>").replace("Cd2+", "Cd<sup>2+</sup>").replace("Hg2+", "Hg<sup>2+</sup>") for x in T(11, "Barcarena, no nordeste do Pará", "Ministério da Saúde.", ["Em 2004, a Universidade"])])
             + url("https://tinyurl.com/ydhahee2", "06.03.2018")
             + p("<strong>Tabela de padrão de potabilidade para algumas substâncias químicas que representam risco à saúde</strong>")
             + tabela(["Parâmetro", "Número Atômico (Z)", "Valor máximo permitido (mg/L)"], [["Arsênio", "33", "0,010"], ["Bário", "56", "0,7"], ["Cádmio", "48", "0,005"], ["Chumbo", "82", "0,01"], ["Mercúrio", "80", "0,001"]])
             + url("https://tinyurl.com/zmxg7b9", "06.03.2018"))
P22 = p("Entre os elementos citados, o único pertencente ao grupo dos metais alcalino-terrosos é o")

STRESS = (chamada("Leia o texto para responder às questões de números 25 a 29.")
          + apoio("<strong>5 Ways to Boost Your Resilience at Work</strong>",
                  *T(12, "Since the pace and intensity", "stay motivated:", ["Resilience is built by", "The current and rising"]),
                  *T(12, "Exercise mindfulness –", "to decrease stress.", ["Compartmentalize your", "Take detachment", "Develop mental agility", "Cultivate compassion"]))
          + url("https://tinyurl.com/ycvtxc4v", "04.03.2018")
          + fonte("Glossário: (1) <em>Thrive</em>: prosperar, desenvolver, ter sucesso. (2) <em>Detachment</em>: descolamento, distanciamento, separação."))
STRESS = STRESS.replace("thrive1", "thrive<sup>1</sup>").replace("detachment2", "detachment<sup>2</sup>").replace("Detachment2", "Detachment<sup>2</sup>")
for t in ("Exercise mindfulness", "Compartmentalize your cognitive load", "Take detachment", "Develop mental agility", "Cultivate compassion"):
    STRESS = STRESS.replace(t, f"<strong>{t}</strong>", 1)
P25 = p("Na frase, “<em>I’ve seen over and over again ....</em>”, presente no primeiro parágrafo do texto, o autor refere-se a uma ação que")

PECA = (chamada("Leia o texto e considere as figuras para responder às questões de números 30 e 31.")
        + p("Utilizando um software de desenho 3D, um tecnólogo em Mecânica elaborou o projeto de uma peça de acordo com os seguintes procedimentos:",
            "(1º) no plano cartesiano, desenhou o polígono CDEFGHIJKLMN, conforme figura 1, adotando como unidade de cada eixo coordenado 1 cm.",
            "(2º) tendo esse polígono como base, construiu um prisma reto conforme a figura 2.")
        + "[[fig:1]]")
PECA_IMG = figs(("q30", "Figura 1: no plano cartesiano, o polígono CDEFGHIJKLMN, com coordenadas C (0, 0), D (0, 12), E (6, 12), F (6, 16), G (14, 16), H (14, 12), I (20, 12), J (20, 0), K (15, 0), L (15, 5), M (5, 5) e N (5, 0): um retângulo de 20 por 12 com um ressalto de 8 por 4 em cima, entre x = 6 e x = 14, e um recorte de 10 por 5 embaixo, entre x = 5 e x = 15. Figura 2: o prisma reto construído sobre esse polígono, em perspectiva."))
P30 = p("Nessas condições, o cosseno do ângulo ĈDN é, aproximadamente, igual a")

FARMA = (chamada("Analise os gráficos para responder às questões de números 32 e 33.") + "[[fig:1]]" + url("https://tinyurl.com/yaevl4u9", "25.02.2018"))
FARMA_IMG = figs(("q32", "Três gráficos sobre exportações brasileiras de produtos farmacêuticos, de 2010 a 2014. 1) Participação por tipo de produto (em %): medicamento de referência 46, 43, 42, 41, 40; genérico 12, 14, 12, 12, 13; similar 42, 43, 45, 47, 48. 2) Faturamento, em bilhões de reais: 27,71; 30,16; 32,73; 36,42; 40,35. 3) Doses comercializadas, em bilhões de unidades: 76,30; 88,04; 98,50; 111,11; 121,83."))
P32 = p("De acordo com as informações dos gráficos, pode-se concluir corretamente que")

VOYAGER = (chamada("Leia o texto para responder às questões de números 35 a 39.")
           + apoio("<strong>“O espaço, a fronteira final...”</strong><br><em>(Cap. James T. Kirk - USS Enterprise, 1966)</em>",
                   *T(15, "Em 2017, a missão Voyager sagrou-se", "http://voyager.jpl.nasa.gov.", ["A Voyager 1, uma espaçonave", "Cada nave continha", "Em 2017, a Voyager 1 encontrava", "A NASA estima", "Em homenagem aos 40 anos"])))
P35 = p("Em março de 1979, a Voyager 1 finalmente chegou ao primeiro planeta a ser estudado: Júpiter.",
        "É correto afirmar que a força gravitacional sofrida pela Voyager 1 no instante em que a espaçonave passava a uma distânica de 3,5 × 10<sup>5</sup> km do centro de Júpiter é, em newtons, igual a") \
      + apoio("Adote:<br>G ≅ 7 × 10<sup>–11</sup> N·m<sup>2</sup>/kg<sup>2</sup><br>M<sub>Júpiter</sub> = 2,0 × 10<sup>27</sup> kg (Massa de Júpiter)<br>Considere: \\(F = G\\,\\dfrac{m \\cdot M}{d^2}\\)")

SAF = (chamada("Leia o texto para responder às questões de números 45 a 47.")
       + apoio("<strong>Agroflorestas se espalham pelo país: cultivo sem desmatamento</strong>", *[it(x, "Homo sapiens") for x in T(18, "À primeira vista, pode parecer", "áreas intensamente arborizadas.", ["“Quando me falaram", "Os SAFs vêm ganhando"])])
       + url("https://tinyurl.com/yb8xauee", "06.03.2018"))
P45 = p("Assinale a alternativa que apresenta um trecho do texto em que o emprego dos SAFs está associado ao conceito ecológico de sustentabilidade.")

CAROLINA = (chamada("Leia o texto para responder às questões de números 50 a 53.")
            + apoio(*T(20, "13 de maio Hoje amanheceu", "Mas, as miserias são reais.", ["...Nas prisões", "Continua chovendo.", "...Eu tenho tanto dó", "– Viva a mamãe!", "A manifestação agrada-me.", "– “Dona Ida", "...Choveu, esfriou.", "E assim no dia 13", "29 de maio", "...Há de existir"]))
            + fonte("MARIA DE JESUS, Carolina. <em>Quarto de Despejo: Diário de uma favelada</em>. São Paulo: Editora Ática, 2017. Adaptado."))
CAROLINA = CAROLINA.replace("13 de maio Hoje", "<strong>13 de maio</strong> Hoje").replace("29 de maio [....]", "<strong>29 de maio</strong> [....]")
P50 = p("O texto foi retirado do livro <em>Quarto de Despejo</em>, diário escrito por Carolina Maria de Jesus, moradora da favela do Canindé, em São Paulo, na década de 1950. A edição reproduz fielmente os manuscritos originais.",
        "Analisando a linguagem apresentada no trecho, conclui-se corretamente que")

Q = {
1: {"materia": "Física", "assunto": "Energia", "tags": MULTI + ["resiliência", "deformação elástica"],
    "enunciado": p(" ".join(T(2, "Resiliência é um termo oriundo da Física", "ou, até mesmo, ruptura.")), "Assim, é correto afirmar que"),
    "alternativas": AL(2, "(A) quanto maior o ponto de resiliência de um material, menos", "mais energia o material acumulará durante a deformação."),
    "explicacao": "<p>O ponto de resiliência mede a energia máxima que o material acumula sem se deformar de vez. Quanto maior esse ponto, <strong>mais energia</strong> ele acumula durante a deformação. Alternativa <strong>E</strong>.</p><p>A diz o contrário. Um ponto de resiliência menor significa que o material se rompe ou se deforma com menos energia, não que resiste mais (B e D). E maior resiliência significa mais capacidade elástica, não menos (C).</p>"},
2: {"materia": "Matemática", "assunto": "Estatística", "tags": MULTI + ["gráficos"],
    "enunciado": FGV + P2,
    "imagens": figs(("q02a", "Gráfico A: setores com três fatias de tamanhos parecidos (Baixo, Moderado, Elevado)."), ("q02b", "Gráfico B: rosca com Baixo pequeno, Moderado maior e Elevado um pouco menor que Moderado."),
                    ("q02c", "Gráfico C: linha que sobe muito de Baixo para Moderado e pouco de Moderado para Elevado."), ("q02d", "Gráfico D: barras horizontais com Baixo a maior, Moderado quase igual e Elevado a menor."),
                    ("q02e", "Gráfico E: colunas 3D com Baixo baixa, Moderado e Elevado altas, Elevado um pouco menor.")),
    "alternativas": {"A": "[[fig:1]]", "B": "[[fig:2]]", "C": "[[fig:3]]", "D": "[[fig:4]]", "E": "[[fig:5]]"},
    "explicacao": "<p>Os dados são partes de um todo (16% + 44% + 40% = 100%), próprios de um gráfico de setores (pizza ou rosca). A rosca B mostra Baixo bem pequeno, Moderado o maior e Elevado pouco menor: proporções corretas. Alternativa <strong>B</strong>.</p><p>Em A as fatias parecem iguais. C usa linha, que indica evolução no tempo, e as categorias não são sequência temporal. D inverte as proporções (Baixo seria o maior). E até respeita a ordem dos valores, mas compara categorias como se fossem independentes, sem mostrar que formam um todo, e a perspectiva 3D atrapalha a leitura das proporções.</p>"},
3: {"materia": "Matemática", "assunto": "Porcentagem",
    "enunciado": p("Considere que 60% dos questionários foram respondidos por mulheres e que, dessas, 50% são formadas em Psicologia.", "Nessas condições, o número de mulheres que responderam ao questionário e que são formadas em Psicologia é"),
    "apoio_de": (2, P2),
    "alternativas": alts("450.", "750.", "900.", "1 112.", "2 224."),
    "explicacao": "<p>O questionário foi respondido por 1 500 alunos: 60% são mulheres (900), e metade delas, <strong>450</strong>, são formadas em Psicologia. Alternativa <strong>A</strong>.</p><p>900 é o total de mulheres (C). 1 112 e 2 224 usam os 3 707 alunos do estudo, mas só 1 500 responderam (D e E).</p>"},
4: {"materia": "História", "assunto": "Revolução Industrial", "tags": MULTI,
    "enunciado": apoio(*T(3, "No mundo atual, permeado pela lógica", "para a sociedade urbana.", ["[....]", "Na Revolução Industrial"]))
                 + url("https://tinyurl.com/y86wcuhe", "09.03.2017") + p("Assinale a alternativa que elenca corretamente as principais características da Primeira Revolução Industrial."),
    "alternativas": AL(3, "(A) Valorização do trabalho artesanal", "e surgimento do campesinato."),
    "explicacao": "<p>A Primeira Revolução Industrial (Inglaterra, séc. XVIII) trouxe as máquinas, movidas a <strong>vapor e carvão mineral</strong>, aprofundou a divisão do trabalho nas fábricas e fez surgir o <strong>proletariado</strong>. Alternativa <strong>D</strong>.</p><p>Ela desvalorizou o trabalho artesanal (A). Petróleo e tecnologia da informação são de fases posteriores (B). Biocombustíveis e leis trabalhistas também (C). E energia solar e eólica não fazem parte dela (E).</p>"},
5: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": MULTI + ["reforma trabalhista"],
    "enunciado": apoio(" ".join(T(3, "A resiliência hoje em dia é interpretada", "altamente estressante.")))
                 + url("https://tinyurl.com/ybfxjvgr", "01.03.2018")
                 + p("Um dos desafios para a classe trabalhadora brasileira é se adaptar à Reforma Trabalhista, aprovada pelo Congresso Nacional no ano de 2017.", "Essa Reforma institui uma nova regra sobre o trabalho intermitente, em que o contratado"),
    "alternativas": AL(3, "(A) deverá abrir uma empresa individual", "recebendo menos que um efetivo."),
    "explicacao": "<p>No trabalho intermitente, o empregado é chamado conforme a necessidade e <strong>recebe pelas horas ou pelos dias trabalhados</strong>. Alternativa <strong>B</strong>.</p><p>Ele não precisa abrir empresa nem morar no local (A). A reforma tornou a contribuição sindical opcional (C). Não há prorrogação sem acordo (D). E estatutário é o servidor público (E).</p>"},
6: {"materia": "Química", "assunto": "Funções orgânicas", "tags": MULTI + ["neurotransmissores"],
    "enunciado": p(*T(4, "A capacidade de resiliência dos indivíduos", "comportamento humano."), "Observe as fórmulas estruturais de algumas dessas moléculas.") + "[[fig:1]]"
                 + p("As funções orgânicas comuns às moléculas ilustradas são"),
    "imagens": figs(("q06", "Fórmulas estruturais de quatro moléculas. Dopamina (sensação de satisfação e prazer): anel benzênico com dois OH e uma cadeia CH₂–CH₂–NH₂. Adrenalina (reação de luta e fuga): anel benzênico com dois OH e uma cadeia CH(OH)–CH₂–NH–CH₃. Serotonina (regula humor, sono e atividade sexual): anel indol com OH ligados ao anel aromático, NH no anel e cadeia CH₂–CH₂–NH₂. Noradrenalina (comportamento diante de risco): anel benzênico com dois OH e uma cadeia CH(OH)–CH₂–NH₂.")),
    "alternativas": alts("álcool e amina.", "álcool e amida.", "fenol e amida.", "fenol e amina.", "fenol e nitrila."),
    "explicacao": "<p>As quatro moléculas têm OH ligado diretamente ao anel aromático (<strong>fenol</strong>) e nitrogênio ligado a carbonos sem C=O (<strong>amina</strong>). Alternativa <strong>D</strong>.</p><p>Só a adrenalina e a noradrenalina têm OH de álcool, então álcool não é comum a todas (A e B). Amida exige C=O ligado ao N (B e C). E nitrila é C≡N (E).</p>"},
7: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": MULTI + ["OMS"],
    "enunciado": apoio(" ".join(T(5, "Os aspectos físicos e psicossociais", "disponível para eles.")))
                 + fonte("SHAIN, M.; KRAMER, D. M. Health promotion in the workplace: framing the concept; reviewing the evidence. <strong>Occupational and Environmental Medicine</strong>, v. 61, n. 7, p. 643, 2004. Traduzido e adaptado.")
                 + p("Esse texto está relacionado a uma concepção de saúde formalizada em 1948 pela Organização Mundial de Saúde (OMS). Segundo essa concepção, saúde consiste"),
    "alternativas": alts("na ausência de doenças agudas.", "no bem-estar social, físico e mental.", "no acesso a hospitais especializados.", "na ausência de doenças infectocontagiosas.", "no bem-estar nutricional, respiratório e mental."),
    "explicacao": "<p>Para a OMS, saúde é “um estado de completo <strong>bem-estar físico, mental e social</strong>, e não apenas a ausência de doença”. Alternativa <strong>B</strong>.</p><p>A definição vai além da ausência de doenças (A e D) e do acesso a hospitais (C), e não cita bem-estar nutricional e respiratório (E).</p>"},
8: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": MULTI + ["charge"],
    "enunciado": p("Considere a charge.") + "[[fig:1]]" + url("https://tinyurl.com/ybguaefn", "04.03.2018", "")
                 + p("A charge, referente ao ambiente de trabalho, mostra um chefe sugerindo que seu funcionário"),
    "imagens": figs(("q08", "Charge: um funcionário está sentado em posição de lótus sobre a mesa do escritório, meditando, e o chefe, de gravata, irritado, diz: “I know I said I wanted the staff to relax during the day but couldn’t you just close your eyes and take 3 deep breaths like everyone else?” (eu sei que disse que queria que a equipe relaxasse durante o dia, mas você não podia só fechar os olhos e respirar fundo três vezes, como todo mundo?).")),
    "alternativas": AL(5, "(A) mude a estratégia de meditação", "cuidar da saúde física e mental."),
    "explicacao": "<p>O chefe reclama que o funcionário exagerou: em vez de meditar em cima da mesa, ele deveria só fechar os olhos e respirar fundo três vezes, como os outros, e voltar ao trabalho. É <strong>simplificar o relaxamento</strong>. Alternativa <strong>D</strong>.</p><p>Ele não fala de estratégia contra o estresse (A), nem de doenças (B), nem de reunir funcionários (C), e quer menos tempo de pausa, não mais (E).</p>"},
9: {"materia": "Geografia", "assunto": "População", "tags": MULTI + ["desemprego", "gráficos"],
    "enunciado": p(" ".join(T(6, "Nos últimos anos, ser resiliente", "apresentados nos gráficos."))) + "[[fig:1]]"
                 + url("https://tinyurl.com/yby34khb", "09.03.2018", "Original colorido.") + p("Analisando as informações apresentadas, é correto afirmar que, no período"),
    "imagens": figs(("q09", "Dois gráficos de barras, de 2012 a 2017 (2017: saldo do trimestre encerrado em novembro; fonte: PNAD Contínua do IBGE). “A miragem da reativação do mercado de trabalho” – taxa de desocupação dos brasileiros com 14 anos ou mais, em %: 7,4; 7,1; 6,8; 8,5; 11,3; 12. “O país perde 1 milhão de empregos formais por ano” – trabalhadores com carteira assinada no setor privado (exceto domésticos), em milhões: 34,3; 35,4; 36,6; 35,7; 34,3; 33,2.")),
    "alternativas": AL(6, "(A) de 2012 a 2014, o aumento anual", "índice médio de desemprego de 6,8%."),
    "explicacao": "<p>Os trabalhadores com carteira assinada passaram de 36,6 milhões em 2014 para 33,2 milhões em 2017: queda de <strong>3,4 milhões</strong>. Alternativa <strong>B</strong>.</p><p>Os aumentos de 2012 a 2014 foram de 1,1 e 1,2 milhão, não idênticos (A). 4,6 é a variação da taxa de desocupação em pontos percentuais, não do número de empregados (C). De 2016 a 2017 a desocupação subiu (D). E a média de 2012 a 2014 é (7,4 + 7,1 + 6,8) ÷ 3 ≈ 7,1% (E).</p>"},
10: {"materia": "Raciocínio lógico", "assunto": "Lógica", "tags": ["dilema construtivo"],
     "enunciado": p("Um grupo de quatro amigos — Ana, Beto, Caio e Denise — deseja participar do vestibular da FATEC optando por cursos distintos. Considere verdadeiras as proposições:")
                  + apoio("<strong>I.</strong> Caso Ana se inscreva em Soldagem, então Beto se inscreverá para Eventos.", "<strong>II.</strong> Se Denise fizer a inscrição para Polímeros, então Caio se inscreverá em Cosméticos.", "<strong>III.</strong> Ana fará sua inscrição em Soldagem ou Denise em Polímeros.")
                  + p("Segue-se, necessariamente, que"),
     "alternativas": AL(7, "(A) Ana não se inscrever em Soldagem implica", "e Beto se inscreverá em Eventos."),
     "explicacao": "<p>Por III, acontece pelo menos uma das duas: Ana em Soldagem ou Denise em Polímeros. Se for a primeira, por I, Beto vai para Eventos; se for a segunda, por II, Caio vai para Cosméticos. Então, necessariamente, <strong>Caio em Cosméticos ou Beto em Eventos</strong>. Alternativa <strong>C</strong>.</p><p>B e E exigem que as duas coisas aconteçam, o que não é garantido. A não decorre: se Ana não fizer Soldagem, Denise faz Polímeros e Caio <em>vai</em> para Cosméticos. D também não é garantida.</p>"},
11: {"materia": "Raciocínio lógico", "assunto": "Raciocínio espacial", "tags": ["simetria central"],
     "enunciado": p("Isometrias são transformações de uma figura em outra nas quais a forma, as medidas lineares e os ângulos são preservados. A reflexão em relação a um ponto é uma isometria.",
                    "A figura apresenta a letra <strong>P</strong> e o centro de reflexão, representado pelo ponto <strong>C</strong>.") + "[[fig:1]]"
                  + p("Observando a letra apresentada e o centro de reflexão, a imagem obtida, após a reflexão, é"),
     "imagens": figs(("q11", "Um quadrado com a letra p minúscula no canto superior esquerdo e o ponto C mais abaixo e à direita.")),
     "alternativas": alts("a letra q, menor que a letra p original.", "a letra d, do mesmo tamanho da letra p original.", "a letra p, menor que a original.", "a letra q, do mesmo tamanho da letra p original.", "a letra d em itálico (inclinada)."),
     "explicacao": "<p>Reflexão em relação a um ponto equivale a girar a figura 180°: o “p” de cabeça para baixo vira um <strong>d</strong>. Como é uma isometria, o tamanho e a forma não mudam. Alternativa <strong>B</strong>.</p><p>A letra q seria o resultado de uma reflexão em relação a uma reta horizontal (A e D). Mudar o tamanho (A e C) ou inclinar a letra (E) não preserva medidas e ângulos.</p><p>Observação: na prova, as alternativas são as próprias letras desenhadas em tamanhos e estilos diferentes; aqui foram descritas em palavras.</p>"},
12: {"materia": "Raciocínio lógico", "assunto": "Sequências", "tags": ["padrões cíclicos"],
     "enunciado": p("Ansioso para o início da prova do vestibular, um candidato, tentando se acalmar, escreveu a palavra <strong>FATEC</strong> 10 000 vezes. Colocou as letras da palavra FATEC em linha reta e enumerou a posição delas, conforme a tabela:")
                  + tabela(["F", "A", "T", "E", "C", "F", "A", "T", "E", "C", "..."], [["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "..."]])
                  + p("Assim sendo, a letra que ocupa a posição de número 2 018 é"),
     "alternativas": alts("F .", "A .", "T .", "E .", "C ."),
     "explicacao": "<p>As letras se repetem a cada 5 posições, começando em 0: F (0), A (1), T (2), E (3), C (4). O resto de 2 018 por 5 é 3, então a posição 2 018 tem a mesma letra da posição 3: <strong>E</strong>. Alternativa <strong>D</strong>.</p><p>Esquecer que a contagem começa em 0 levaria a T (C).</p>"},
13: {"materia": "Raciocínio lógico", "assunto": "Operações e problemas", "tags": ["MMC"],
     "enunciado": p("Uma empresa decide contratar três funcionários, cada qual com uma jornada de trabalho distinta.")
                  + apoio("<strong>I.</strong> O primeiro deles deve seguir uma escala de trabalho <strong>12 × 36</strong> — a cada <strong>12 horas</strong> consecutivas de trabalho, o funcionário tem direito a <strong>36 horas</strong> consecutivas de descanso.",
                          "<strong>II.</strong> O segundo, por sua vez, se enquadrará em uma escala de trabalho <strong>18 × 36</strong> — a cada <strong>18 horas</strong> consecutivas de trabalho, o funcionário tem direito a <strong>36 horas</strong> consecutivas de descanso.",
                          "<strong>III.</strong> O terceiro, e último, estará subordinado a uma escala de trabalho <strong>24 × 48</strong> — a cada <strong>24 horas</strong> consecutivas de trabalho, o funcionário tem direito a <strong>48 horas</strong> consecutivas de descanso.")
                  + p("Supondo que os três comecem a trabalhar ao mesmo tempo e no mesmo dia, bem como cumpram a jornada estabelecida, respeitando inclusive as horas de descanso, eles irão iniciar o trabalho juntos novamente depois de"),
     "alternativas": alts("54 dias.", "36 dias.", "24 dias.", "18 dias.", "6 dias."),
     "explicacao": "<p>Os ciclos completos (trabalho + descanso) duram 48 h, 54 h e 72 h. Eles recomeçam juntos no MMC: MMC(48, 54, 72) = 432 h = 432 ÷ 24 = <strong>18 dias</strong>. Alternativa <strong>D</strong>.</p><p>Usar só as horas de trabalho ou só as de descanso dá outros resultados.</p>"},
14: {"materia": "Raciocínio lógico", "assunto": "Análise combinatória", "tags": ["permutação caótica"],
     "enunciado": p(*T(8, "Ao ser contratado para trabalhar", "aleatoriamente, a senha", ["Para os seus primeiros dias"]))
                  + apoio("<strong># F a 1</strong>")
                  + p("Sem tempo de repensar uma senha, o Sr. Cavalcante decidiu que",
                      "• obrigatoriamente utilizaria apenas os caracteres: <strong>#</strong>, <strong>F</strong>, <strong>a</strong>, <strong>1</strong>;<br>• e que nenhum desses caracteres, em sua nova senha, deveria ocupar a mesma posição da senha gerada pelo sistema.",
                      "Nessas condições, o número total de senhas distintas que o Sr. Cavalcante poderá criar é"),
     "alternativas": alts("4.", "9.", "10.", "23.", "24."),
     "explicacao": "<p>É preciso rearranjar 4 caracteres sem que nenhum fique na posição original: uma permutação caótica. D₄ = 4! (1 − 1 + 1/2 − 1/6 + 1/24) = 24 − 24 + 12 − 4 + 1 = <strong>9</strong>. Alternativa <strong>B</strong>.</p><p>24 são todas as permutações, inclusive a original (E), e 23 só tira a senha original (D).</p>"},
15: {"materia": "História", "assunto": "Pré-História", "tags": ["Neolítico"],
     "enunciado": p(" ".join(T(9, "Aproximadamente 12 mil anos atrás", "chamamos de Neolítico.")), "Esse período é caracterizado principalmente pela"),
     "alternativas": AL(9, "(A) descoberta do fogo e pela invenção", "pelo surgimento do capitalismo."),
     "explicacao": "<p>O Neolítico é marcado pela <strong>agricultura</strong>, pela domesticação de animais e pela <strong>sedentarização</strong> dos grupos humanos. Alternativa <strong>C</strong>.</p><p>O fogo é do Paleolítico, e a escrita marca o fim da Pré-História (A). Metais e cidades vêm na Idade dos Metais (B). Não houve mecanização agrícola (D) nem capitalismo (E).</p>"},
16: {"materia": "História", "assunto": "Idade Média", "tags": ["presença árabe na Península Ibérica"],
     "enunciado": p(" ".join(T(9, "O idioma árabe exerceu forte influência", "azeitona, entre outras.")), "Assinale a alternativa correta sobre os contatos entre árabes e portugueses que possibilitaram essa influência."),
     "alternativas": AL(9, "(A) No início do século XXI, a eclosão", "marcando, também, a formação da língua portuguesa."),
     "explicacao": "<p>A partir de 711 (século VIII), os muçulmanos conquistaram a maior parte da Península Ibérica e ficaram ali por séculos, influenciando a arquitetura, a ciência e o vocabulário do português em formação. Alternativa <strong>E</strong>.</p><p>A Primavera Árabe é de 2011 (A). As Grandes Navegações são dos séculos XV e XVI (B). A Conferência de Berlim (1884–85) dividiu a África (C). E o Império Turco é posterior e não provocou essa migração (D).</p>"},
17: {"materia": "História", "assunto": "América colonial", "tags": ["colonização espanhola"],
     "enunciado": p(" ".join(T(9, "Muitos povos indígenas resistiram", "dos indígenas peruanos.")), "A colonização espanhola da América se caracterizou pela"),
     "alternativas": AL(9, "(A) criação de quatro grandes vice-reinados", "como a batata e o milho."),
     "explicacao": "<p>A Espanha dividiu a América em <strong>vice-reinados</strong> (Nova Espanha, Peru, Nova Granada e Rio da Prata), extraiu ouro e prata e explorou o trabalho indígena, como na mita e na encomienda. Alternativa <strong>A</strong>.</p><p>Os órgãos não eram independentes, e não havia trabalho assalariado (B). As instituições incas foram desmontadas, e não houve industrialização (C). Não havia condados (D). E a batata e o milho são americanos, não asiáticos (E).</p>"},
18: {"materia": "História", "assunto": "História contemporânea", "tags": ["Revolução Francesa"],
     "enunciado": apoio(*T(10, "Em agosto de 1789, a Assembleia", "sagrados do homem.", ["A Declaração estabeleceu"])) + fonte("ARARIBÁ Plus: <em>História</em>. 4ªed. São Paulo: Moderna, 2014. p.102.")
                  + p("O texto se refere aos acontecimentos da"),
     "alternativas": alts("Confederação do Equador.", "Independência do México.", "Guerra Civil Americana.", "Inconfidência Mineira.", "Revolução Francesa."),
     "explicacao": "<p>A Assembleia Nacional Constituinte de 1789, o fim dos privilégios feudais e a <strong>Declaração dos Direitos do Homem e do Cidadão</strong> são marcos da <strong>Revolução Francesa</strong>. Alternativa <strong>E</strong>.</p><p>A Confederação do Equador (1824), a Independência do México (1821) e a Guerra Civil Americana (1861–65) são posteriores. A Inconfidência Mineira (1789) não aprovou leis (A, B, C e D).</p>"},
19: {"materia": "História", "assunto": "Brasil República", "tags": ["Plano de Metas", "JK"],
     "enunciado": p(" ".join(T(10, "Na década de 1950, o presidente Juscelino", "como Plano de Metas.")), "Sob o lema “50 anos em 5”, esse plano se caracterizou pela"),
     "alternativas": AL(10, "(A) adoção de uma política econômica liberal", "redistribuição de renda e da terra."),
     "explicacao": "<p>JK abriu o país ao capital estrangeiro (sobretudo à indústria automobilística), mas manteve o monopólio estatal do petróleo, criado com a Petrobras em 1953. Alternativa <strong>B</strong>.</p><p>O plano não privatizou serviços (A), concentrou as indústrias no Sudeste (C), não houve aproximação com a URSS (D), e não houve redistribuição de terra nem de renda (E).</p>"},
20: {"materia": "Química", "assunto": "Substâncias e misturas", "tags": ["mudanças de estado físico"],
     "enunciado": p("Leia o trecho do soneto “Como eu te amo”, de Gonçalves Dias, para responder a questão.")
                  + apoio("Como se ama o silêncio, a luz, o aroma, (1)<br>O orvalho numa flor, nos céus a estrela, (2)<br>No largo mar a sombra de uma vela, (3)<br>Que lá na extrema do horizonte assoma; (4)",
                          "Como se ama o clarão da branca lua, (5)<br>Da noite na mudez os sons da flauta, (6)<br>As canções saudosíssimas do nauta, (7)<br>Quando em mole vaivém a nau flutua. (8)")
                  + url("https://tinyurl.com/y6uoquu5", "17.03.2018")
                  + p("A condensação, passagem de uma substância do estado gasoso para o estado líquido, pode ocorrer quando vapores de um material entram em contato com uma superfície fria.", "O verso que cita um fenômeno resultante da condensação do vapor de água é o"),
     "alternativas": alts("1", "2", "3", "4", "5"),
     "explicacao": "<p>O <strong>orvalho</strong> (verso 2) se forma quando o vapor de água do ar se condensa ao tocar superfícies frias, como as pétalas de uma flor à noite. Alternativa <strong>B</strong>.</p><p>Os outros versos falam de silêncio, luz, aroma, sombra, horizonte e luar, sem relação com condensação.</p>"},
21: {"materia": "Química", "assunto": "Reações químicas", "tags": ["combustão", "balanceamento"],
     "enunciado": p("Considere uma vela composta de um hidrocarboneto (fórmula molecular C<sub>22</sub>H<sub>46</sub>) cuja combustão completa libera apenas gás carbônico e água.",
                    "Pode-se concluir corretamente que, na combustão completa de 1 mol desse hidrocarboneto, as quantidades de matéria, e CO<sub>2</sub> e de H<sub>2</sub>O produzidas são, em mol, respectivamente, iguais a"),
     "alternativas": alts("11 e 13.", "11 e 20.", "22 e 23.", "22 e 25.", "22 e 46."),
     "explicacao": "<p>Cada carbono vira um CO₂: 22 mol de CO₂. Os 46 hidrogênios formam 46 ÷ 2 = 23 mol de H₂O. Alternativa <strong>C</strong>.</p><p>46 é o número de átomos de H, não de moléculas de água (E). As outras dividem ou somam de forma errada.</p>"},
22: {"materia": "Química", "assunto": "Estrutura atômica", "tags": ["tabela periódica"],
     "enunciado": BARCARENA + P22,
     "alternativas": alts("arsênio.", "bário.", "cádmio.", "chumbo.", "mercúrio."),
     "explicacao": "<p>Os metais alcalino-terrosos formam o grupo 2 da tabela: Be, Mg, Ca, Sr, <strong>Ba</strong> e Ra. Alternativa <strong>B</strong>.</p><p>O arsênio é um semimetal do grupo 15 (A). Cádmio e mercúrio são metais de transição do grupo 12 (C e E). E o chumbo é do grupo 14 (D).</p>"},
23: {"materia": "Química", "assunto": "Estrutura atômica", "tags": ["íons"],
     "enunciado": p("Os íons cádmio, \\({}^{112}_{48}\\text{Cd}^{2+}\\), presentes na água contaminada apresentam"), "apoio_de": (22, P22),
     "alternativas": alts("46 prótons e 63 nêutrons.", "46 prótons e 64 nêutrons.", "48 prótons e 67 nêutrons.", "48 prótons e 48 elétrons.", "48 prótons e 46 elétrons."),
     "explicacao": "<p>O número atômico 48 é o número de prótons. O íon 2+ perdeu 2 elétrons: 48 − 2 = <strong>46 elétrons</strong>. Alternativa <strong>E</strong>.</p><p>O número de prótons não muda ao formar o íon (A e B). Os nêutrons são 112 − 48 = 64, não 67 (C). E 48 elétrons seria o átomo neutro (D).</p>"},
24: {"materia": "Química", "assunto": "Soluções", "tags": ["concentração"],
     "enunciado": p("No atendimento a um morador de Vila Nova, o médico calculou a quantidade de chumbo ingerida pelo paciente que havia bebido 500 mL da água contaminada na cidade.", "Assinale a alternativa que apresenta a massa total de chumbo ingerida pelo paciente, em miligramas."),
     "apoio_de": (22, P22),
     "alternativas": alts("1 × 10<sup>–3</sup>", "5 × 10<sup>–3</sup>", "3 × 10<sup>–2</sup>", "6 × 10<sup>–2</sup>", "9 × 10<sup>–2</sup>"),
     "explicacao": "<p>Em Vila Nova, o chumbo estava 12 vezes acima do limite de 0,01 mg/L: 0,12 mg/L. Em 0,5 L: 0,12 · 0,5 = 0,06 mg = <strong>6 × 10⁻² mg</strong>. Alternativa <strong>D</strong>.</p><p>5 × 10⁻³ mg é o limite em 0,5 L, sem as 12 vezes (B).</p>"},
25: {"materia": "Inglês", "assunto": "Verbos", "tags": ["present perfect"],
     "enunciado": STRESS + P25,
     "alternativas": AL(12, "(A) ocorrerá somente no futuro.", "não tem conexão com o passado."),
     "explicacao": "<p><em>I’ve seen</em> está no <em>present perfect</em>: uma experiência que começou no passado e continua valendo até hoje (“tenho visto, repetidas vezes”). Alternativa <strong>D</strong>.</p><p>Não é futuro (A), nem um passado encerrado ou remoto, que seria <em>I saw</em> (B e C), nem um presente sem ligação com o passado (E).</p>"},
26: {"materia": "Inglês", "assunto": "Coesão e referência",
     "enunciado": p("No segundo parágrafo do texto, o trecho “<em>.... can be extremely onerous.</em>” refere-se a"), "apoio_de": (25, P25),
     "alternativas": AL(12, "(A) desenvolver a resiliência no trabalho.", "disponível às demandas do trabalho."),
     "explicacao": "<p>A frase é “<em>Being hyperconnected and responsive to work anytime, anywhere, can be extremely onerous</em>”: o que é penoso é <strong>estar sempre conectado e disponível ao trabalho</strong>. Alternativa <strong>E</strong>.</p><p>O sujeito de “can be onerous” não é desenvolver resiliência (A), aumentar o estresse (B), fazer pausas (C) nem compreender o estresse (D).</p>"},
27: {"materia": "Inglês", "assunto": "Interpretação de texto",
     "enunciado": p("De acordo com o texto, a resiliência no mundo do trabalho"), "apoio_de": (25, P25),
     "alternativas": AL(12, "(A) é uma habilidade que poucas pessoas", "constante conexão e disponibilidade para o trabalho."),
     "explicacao": "<p>O texto diz: “<em>To build resilience skills at work it’s important to understand and manage some of the factors that cause us to feel so stressed</em>”. Alternativa <strong>D</strong>.</p><p>A resiliência “<em>can be adopted and cultivated by anyone</em>” (A). Ela ajuda a enfrentar o estresse, não o causa (B). A relação entre estresse, bem-estar e produtividade é do estresse, não da resiliência (C). E a conexão constante é um fator de estresse (E).</p>"},
28: {"materia": "Inglês", "assunto": "Interpretação de texto",
     "enunciado": p("Segundo o texto, o crescente nível de estresse no trabalho"), "apoio_de": (25, P25),
     "alternativas": AL(12, "(A) deve ser motivo de preocupação", "consequentemente, aumenta a produtividade."),
     "explicacao": "<p>O texto diz: “<em>The current and rising levels of stress in the workplace should be cause for concern</em>”. Alternativa <strong>A</strong>.</p><p>O estresse prejudica o bem-estar e a produtividade, não favorece cooperação, sucesso ou produtividade (B, C, D e E).</p>"},
29: {"materia": "Inglês", "assunto": "Interpretação de texto",
     "enunciado": p("Assinale a alternativa que apresenta a sugestão ligada aos benefícios das pausas durante o trabalho."), "apoio_de": (25, P25),
     "alternativas": alts("Exercise mindfulness", "Compartmentalize your cognitive load", "Take detachment breaks", "Develop mental agility", "Cultivate compassion"),
     "explicacao": "<p>“<em>Take detachment breaks – Step away from work for even a few minutes to reset energy and attention</em>”: são as pausas para se afastar do trabalho. Alternativa <strong>C</strong>.</p><p>As outras dicas tratam de atenção plena (A), organização das tarefas (B), flexibilidade mental (D) e boas relações (E).</p>"},
}

Q.update({
30: {"materia": "Matemática", "assunto": "Trigonometria", "tags": ["geometria analítica", "teorema de Pitágoras"],
     "enunciado": PECA + P30, "imagens": PECA_IMG,
     "alternativas": alts("0,38.", "0,42.", "0,56.", "0,74.", "0,92."),
     "explicacao": "<p>No triângulo CDN, retângulo em C, os catetos são CD = 12 e CN = 5, e a hipotenusa é DN = √(144 + 25) = 13. O cosseno do ângulo em D é o cateto adjacente sobre a hipotenusa: 12/13 ≈ <strong>0,92</strong>. Alternativa <strong>E</strong>.</p><p>5/13 ≈ 0,38 é o cosseno do outro ângulo agudo, em N (A).</p>"},
31: {"materia": "Matemática", "assunto": "Geometria espacial", "tags": ["prisma", "volume"],
     "enunciado": p("Se a altura do prisma é de 20 cm, então o volume do prisma é, em centímetros cúbicos, igual a"), "apoio_de": (30, P30),
     "alternativas": alts("4 600.", "4 440.", "3 680.", "3 552.", "3 256."),
     "explicacao": "<p>Área da base: retângulo 20 × 12 = 240, mais o ressalto de cima, 8 × 4 = 32, menos o recorte de baixo, 10 × 5 = 50: 240 + 32 − 50 = 222 cm². Volume: 222 × 20 = <strong>4 440 cm³</strong>. Alternativa <strong>B</strong>.</p><p>Esquecer o recorte dá 272 × 20 = 5 440; esquecer o ressalto dá 190 × 20 = 3 800.</p>"},
32: {"materia": "Matemática", "assunto": "Estatística", "tags": ["gráficos", "porcentagem"],
     "enunciado": FARMA + P32, "imagens": FARMA_IMG,
     "alternativas": AL(14, "(A) de 2010 a 2014, o aumento do número", "medicamentos de referência."),
     "anulacao": {"fonte": "analise", "motivo": "O Centro Paula Souza anulou a questão sem publicar o motivo. Pela análise do Treineiros, nenhuma alternativa está correta: a E, provável resposta pretendida, dá 40% de 121,83 = 48,732 bilhões de doses, não 48,652."},
     "explicacao": "<p>Questão anulada. Conferindo cada alternativa:</p><p>A: as doses foram de 76,30 para 121,83 bilhões, aumento de cerca de 59,7%, bem acima de 30%. B: a participação do similar subiu (42, 43, 45, 47, 48%). C: 30,16 bilhões de reais é o faturamento <em>total</em> de 2011; a parte dos genéricos é 14% disso, cerca de 4,22 bilhões. D: em 2012, 32,73 ÷ 98,50 ≈ R$ 0,33 por dose. E: 40% de 121,83 = <strong>48,732</strong> bilhões, e não 48,652 — por isso nenhuma alternativa fecha.</p>"},
33: {"materia": "Matemática", "assunto": "Funções", "tags": ["função afim", "gráficos"],
     "enunciado": p("No período de 2010 a 2014, o crescimento no número de doses comercializadas, em bilhões de unidades, é aproximadamente linear.",
                    "Se o crescimento observado de 2010 a 2014 se mantiver nos próximos anos, o número de doses comercializadas em 2018, em bilhões de unidades, será, aproximadamente,"),
     "apoio_de": (32, P32),
     "alternativas": alts("144,29.", "155,62.", "166,96.", "197,93.", "243,26."),
     "explicacao": "<p>De 2010 a 2014 as doses passaram de 76,30 para 121,83 bilhões: aumento de 45,53 em 4 anos, cerca de 11,38 por ano. Mais 4 anos até 2018: 121,83 + 45,53 ≈ 167,4 bilhões, mais próximo de <strong>166,96</strong>. Alternativa <strong>C</strong>.</p><p>243,26 seria dobrar o valor de 2014, como se o crescimento fosse percentual e não linear (E).</p>"},
34: {"materia": "Matemática", "assunto": "Probabilidade", "tags": ["eventos independentes", "tabelas"],
     "enunciado": p("Considere os dados divulgados pelo Ministério do Turismo do Brasil em relação à demanda turística internacional em 2016.")
                  + tabela(["Motivo da viagem", "Frequência relativa"], [["Lazer", "57%"], ["Visita a amigos e parentes", "21%"], ["Negócios, eventos e convenções", "19%"], ["Outros motivos", "3%"]])
                  + tabela(["Nível de satisfação com a viagem", "Frequência relativa"], [["Superou as expectativas", "46%"], ["Atendeu plenamente as expectativas", "45%"], ["Atendeu em parte as expectativas", "8%"], ["Não atendeu as expectativas", "1%"]])
                  + url("https://tinyurl.com/ycsskm72", "17.02.2018")
                  + p("A probabilidade de que um turista estrangeiro de 2016, escolhido ao acaso, tenha viajado ao Brasil por “outros motivos” ou que tenha avaliado o seu nível de satisfação com a viagem na categoria “não atendeu as expectativas”, admitindo que esses eventos sejam independentes, é")
                  + apoio("Lembre-se de que:<br>• sendo A e B eventos de um espaço amostral, então p(A ∪ B) = p(A) + p(B) – p(A ∩ B).<br>• se os eventos A e B são independentes, então p(A ∪ B) = p(A) · p(B)."),
     "alternativas": alts("1,00%.", "2,56%.", "3,45%", "3,97%.", "4,00%."),
     "anulacao": {"fonte": "analise", "motivo": "O Centro Paula Souza anulou a questão sem publicar o motivo. Pela análise do Treineiros, o quadro “Lembre-se” traz uma fórmula errada: para eventos independentes vale p(A ∩ B) = p(A) · p(B), e não p(A ∪ B) = p(A) · p(B). Quem seguisse o quadro chegaria a 0,03%, valor fora das alternativas."},
     "explicacao": "<p>Questão anulada. A conta correta: p(A) = 3% e p(B) = 1%; sendo independentes, p(A ∩ B) = 0,03 · 0,01 = 0,0003. Então p(A ∪ B) = 0,03 + 0,01 − 0,0003 = 0,0397 = <strong>3,97%</strong> (alternativa D).</p><p>O problema está no quadro de apoio, que troca ∩ por ∪ na regra dos eventos independentes. Guarde a regra certa: <strong>independentes → p(A ∩ B) = p(A) · p(B)</strong>.</p>"},
35: {"materia": "Física", "assunto": "Gravitação", "tags": ["lei da gravitação universal"],
     "enunciado": VOYAGER + P35,
     "alternativas": alts("800 000.", "80 000.", "800.", "80.", "8."),
     "explicacao": "<p>Com m = 700 kg e d = 3,5 × 10⁵ km = 3,5 × 10⁸ m:</p><p>\\[F = \\frac{7\\times10^{-11}\\cdot 700\\cdot 2\\times10^{27}}{(3{,}5\\times10^{8})^2} = \\frac{9{,}8\\times10^{19}}{1{,}225\\times10^{17}} = 800\\ \\text{N}\\]</p><p>Alternativa <strong>C</strong>. Esquecer de converter km para m multiplica o resultado por 10⁶.</p>"},
36: {"materia": "Física", "assunto": "Cinemática", "tags": ["velocidade média"],
     "enunciado": p(*T(16, "Considere que a Voyager 1 continuará", "em UA, de", ["Podemos concluir"])), "apoio_de": (35, P35),
     "alternativas": alts("175.", "165.", "150.", "143.", "142."),
     "explicacao": "<p>Em 40 anos (1977–2017), a Voyager 1 chegou a 140 UA: 3,5 UA por ano. As baterias duram mais 10 anos: 140 + 10 · 3,5 = <strong>175 UA</strong>. Alternativa <strong>A</strong>.</p><p>O 175 também aparece no texto (o alinhamento dos planetas a cada 175 anos), mas é coincidência: a conta é a de velocidade constante.</p>"},
37: {"materia": "Física", "assunto": "Eletromagnetismo", "tags": ["vento solar"],
     "enunciado": p(*T(16, "Estudo sobre os ventos solares", "corretamente que são", ["Em relação aos ventos"])), "apoio_de": (35, P35),
     "alternativas": AL(16, "(A) responsáveis pela geração de Auroras", "até à superfície terrestre devido à atmosfera."),
     "explicacao": "<p>O vento solar é um fluxo de partículas carregadas; em tempestades solares, essas partículas perturbam o campo magnético da Terra e interferem em satélites, GPS e comunicações. Alternativa <strong>D</strong>.</p><p>Auroras ocorrem perto dos polos, não em países tropicais (A). As partículas vêm do Sol, não são “partículas de ar” do campo interestelar (B). Quem protege a Terra é o campo magnético dela, não o vento solar (C). E E atribui a proteção à atmosfera, quando o principal escudo é a magnetosfera.</p>"},
38: {"materia": "Física", "assunto": "Energia", "tags": ["potência"],
     "enunciado": p(" ".join(T(16, "Considerando um fornecimento constante", "aproximadamente:"))) + apoio("Considere:<br>1 ano = 365 dias<br>\\(P = \\dfrac{E}{\\Delta t}\\)"),
     "apoio_de": (35, P35),
     "alternativas": alts("9,5 × 10<sup>10</sup>", "4,0 × 10<sup>9</sup>", "9,5 × 10<sup>8</sup>", "4,0 × 10<sup>7</sup>", "9,5 × 10<sup>6</sup>"),
     "explicacao": "<p>Δt = 10 · 365 · 24 · 3 600 s ≈ 3,15 × 10⁸ s. E = P · Δt = 300 · 3,15 × 10⁸ ≈ <strong>9,5 × 10¹⁰ J</strong>. Alternativa <strong>A</strong>.</p><p>Usar o tempo em horas, e não em segundos, dá cerca de 2,6 × 10⁷.</p>"},
39: {"materia": "Física", "assunto": "Ondas", "tags": ["ondas eletromagnéticas"],
     "enunciado": p("Segundo o texto, a emissão de sinais da Voyager 1 leva de 12 a 14 horas para chegar à Terra.", "Isto se deve ao fato de que esses sinais são ondas"), "apoio_de": (35, P35),
     "alternativas": AL(16, "(A) mecânicas, que viajam a velocidades", "velocidades próximas da Voyager 1."),
     "explicacao": "<p>Ondas de rádio são <strong>eletromagnéticas</strong>, viajam no vácuo à velocidade da luz (cerca de 300 000 km/s) e, mesmo assim, levam horas pela distância de mais de 20 bilhões de km. Alternativa <strong>C</strong>.</p><p>Ondas mecânicas, como o som, não se propagam no vácuo (A e B). E as ondas eletromagnéticas não viajam à velocidade do som nem da nave (D e E).</p>"},
40: {"materia": "Geografia", "assunto": "Biomas", "tags": ["febre-amarela"],
     "enunciado": p(" ".join(T(16, "Um surto de febre-amarela", "habitam e circulam em"))),
     "alternativas": alts("florestas boreais e áreas desérticas.", "florestas tropicais e áreas de cerrado.", "florestas de coníferas e áreas de tundra.", "florestas mediterrâneas e áreas montanhosas.", "florestas temperadas e áreas de picos gelados."),
     "explicacao": "<p>Os mosquitos transmissores (<em>Haemagogus</em> e <em>Sabethes</em> na forma silvestre, <em>Aedes aegypti</em> na urbana) vivem em ambientes quentes e úmidos: no Brasil, <strong>florestas tropicais e cerrado</strong>. Alternativa <strong>B</strong>.</p><p>As outras opções citam biomas frios, secos ou temperados que não existem no Brasil.</p>"},
41: {"materia": "Geografia", "assunto": "Economia brasileira", "tags": ["setor terciário"],
     "enunciado": p(" ".join(T(16, "O estado de São Paulo contribui", "esse setor se caracteriza por"))),
     "alternativas": AL(16, "(A) englobar a maior rede bancária", "pelo Brasil."),
     "explicacao": "<p>O setor terciário é o de comércio e serviços, que inclui os bancos. São Paulo concentra a <strong>maior rede bancária do país</strong> e as sedes do sistema financeiro. Alternativa <strong>A</strong>.</p><p>Rebanhos e cultivo de alimentos são do setor primário (B e D). Indústrias de base, do secundário (C). E a extração mineral é primária e se concentra em MG e PA (E).</p>"},
42: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["mineração"],
     "enunciado": p(" ".join(T(17, "Tendo em vista a legislação ambiental", "Uma barragem de rejeitos consiste em"))),
     "alternativas": AL(17, "(A) uma área de depósito de resíduos vegetais", "energia para o empreendimento."),
     "explicacao": "<p>Rejeito é o resíduo que sobra do <strong>beneficiamento do minério</strong> (lavagem, separação). A barragem de rejeitos é a estrutura construída para armazená-lo, como as de Mariana (2015) e Brumadinho (2019). Alternativa <strong>D</strong>.</p><p>Não guarda restos vegetais (A), entulho ou máquinas (B), nem minério para venda (C), e não é represa para gerar energia (E).</p>"},
43: {"materia": "Geografia", "assunto": "Hidrografia", "tags": ["bacias hidrográficas", "mapas"],
     "enunciado": p("Leia o texto e considere a figura.", " ".join(T(17, "Um tecnólogo em Meio Ambiente", "vistoriá-las nessa ordem."))) + "[[fig:1]]"
                  + p("É correto afirmar que, para vistoriar essas nascentes, o tecnólogo em questão visitará, na ordem estabelecida, os estados de"),
     "imagens": figs(("q43", "Mapa “Bacias hidrográficas brasileiras”, sem divisão por estados: Amazônica, Tocantins Araguaia, Atlântico NE Ocidental, Parnaíba, Atlântico NE Oriental, São Francisco, Atlântico Leste, Paraguai, Paraná, Atlântico Sudeste, Uruguai e Atlântico Sul.")),
     "alternativas": colunas(["Rio São Francisco", "Rio Tocantins", "Rio Paraguai"], [["Minas Gerais", "Goiás", "Mato Grosso"], ["Minas Gerais", "Mato Grosso", "Goiás"], ["Goiás", "Mato Grosso", "Minas Gerais"], ["Goiás", "Minas Gerais", "Mato Grosso"], ["Mato Grosso", "Goiás", "Minas Gerais"]]),
     "explicacao": "<p>O São Francisco nasce na Serra da Canastra, em <strong>Minas Gerais</strong>. O Tocantins se forma no planalto de <strong>Goiás</strong> (rios das Almas e Maranhão). O Paraguai nasce na Chapada dos Parecis, em <strong>Mato Grosso</strong>. Alternativa <strong>A</strong>.</p><p>As outras trocam a ordem dos estados.</p>"},
44: {"materia": "História", "assunto": "Guerra Fria", "tags": ["ordem bipolar"],
     "enunciado": p(" ".join(T(17, "Guerra Fria foi o nome dado", "a qualquer momento.")), "Durante esse período, a disputa pela hegemonia planetária se caracterizou por uma Ordem Mundial"),
     "alternativas": AL(17, "(A) multipolar, na qual o poder mundial", "domínio geopolítico mundial."),
     "explicacao": "<p>A Guerra Fria teve ordem <strong>bipolar</strong>: Estados Unidos (capitalismo) e União Soviética (socialismo) disputavam a hegemonia global. Alternativa <strong>D</strong>.</p><p>Não era multipolar nem dominada por um só país, pela ONU ou por potências europeias (A, B e C). E os dois polos eram EUA e URSS, não Reino Unido e Rússia (E).</p>"},
45: {"materia": "Biologia", "assunto": "Ecologia", "tags": ["sustentabilidade", "agrofloresta"],
     "enunciado": SAF + P45,
     "alternativas": AL(18, "(A) “À primeira vista, pode parecer", "estimativas da ONU”"),
     "explicacao": "<p>Sustentabilidade é atender às necessidades de hoje sem comprometer as das gerações futuras. “As coisas vão estar aqui <strong>para nossos netos</strong>” expressa exatamente isso. Alternativa <strong>D</strong>.</p><p>Os outros trechos descrevem a aparência da área (A, B e C) ou dão um dado de população (E).</p>"},
46: {"materia": "Biologia", "assunto": "Ecologia", "tags": ["agrofloresta", "monocultura"],
     "enunciado": p(" ".join(T(18, "Comparando a produtividade agrícola", "tem a vantagem de aumentar"))), "apoio_de": (45, P45),
     "alternativas": AL(18, "(A) a frequência de anemofilia", "quantidades de agrotóxicos."),
     "explicacao": "<p>Com plantas da mesma espécie afastadas entre si, uma praga específica tem mais dificuldade de se espalhar: as outras espécies funcionam como <strong>barreira</strong>. A desvantagem é o plantio mais trabalhoso e caro. Alternativa <strong>C</strong>.</p><p>A mistura de espécies diminui a insolação e o escoamento de água (A e B), protege o solo (D) e reduz a necessidade de agrotóxicos (E).</p>"},
47: {"materia": "Biologia", "assunto": "Classificação dos seres vivos", "tags": ["nomenclatura binomial"],
     "enunciado": p(" ".join(T(18, "Nomes vernáculos, como os das plantas", "práticas científicas e tecnológicas.")), " ".join(T(18, "Suponha que o autor do texto", "nomenclatura biológica.")), "Para isso, ele deveria se referir a duas das espécies do texto como"),
     "apoio_de": (45, P45),
     "alternativas": {k: it(v, *[t for t in ("Plantae Arbusta", "Plantae Arborum", "arbusti Planta", "arboris Planta", "Anacardicum occidentale", "Mangifera indica", "Anacardicum Anacardicum", "Mangifera Mangifera") if t in v]) for k, v in AL(18, "(A) Plantae Arbusta L.", "Mangifera Mangifera L. (mangueiras).").items()},
     "explicacao": "<p>A nomenclatura binomial usa o gênero (inicial maiúscula) seguido do epíteto específico (minúscula), em itálico, com o autor abreviado opcional: <em>Mangifera indica</em> L. Alternativa <strong>D</strong>.</p><p>“Plantae” é reino, não gênero, e arbusto e árvore não são espécies (A e B). Nomes em inglês são vernáculos (C). E repetir o gênero como epíteto, com maiúsculas, não segue as regras da botânica (E).</p><p>Observação: o nome correto do gênero do cajueiro é <em>Anacardium</em>; a prova grafou “Anacardicum”.</p>"},
48: {"materia": "Biologia", "assunto": "Citologia", "tags": ["membrana plasmática", "bicamada lipídica"],
     "enunciado": p(*T(19, "As membranas celulares são estruturas", "procedimento similar ao da tabela.", ["Sabendo disso"]))
                  + tabela(["Etapa", "Controle", "Experimental"], [["Coletas de material", "Hemácias extraídas (volume: V)", "Hemácias extraídas (volume: V)"], ["Tratamentos", "Nada realizado", "Lipídios extraídos das hemácias"],
                                                                 ["Testes", "Deposição das hemácias na superfície da água", "Deposição dos lipídios extraídos na superfície da água"], ["Resultados", "Área ocupada pelas hemácias na superfície da água (área: A)", "Área ocupada pelos lipídios na superfície da água (área: 2A)"]])
                  + p("Assinale a alternativa cuja conclusão seja válida para os resultados apresentados e para a teoria referente a eles."),
     "alternativas": AL(19, "(A) Dado que a razão entre as áreas", "entre lipídios e hemácias nos dois procedimentos."),
     "explicacao": "<p>Na água, os lipídios se espalham numa camada única, com a extremidade hidrofílica voltada para a água. Se essa camada ocupa o dobro da área das hemácias, a membrana original tinha <strong>duas camadas</strong> de lipídios. Foi assim que Gorter e Grendel propuseram a bicamada lipídica. Alternativa <strong>C</strong>.</p><p>A razão é 2:1, não 1:2 (A). O experimento não mostra água no interior das células (B), as hemácias do controle não perderam lipídios (D), e não há erro de procedimento (E).</p>"},
49: {"materia": "Biologia", "assunto": "Classificação dos seres vivos", "tags": ["filogenia", "reinos"],
     "enunciado": p(" ".join(T(19, "Os numerosos sistemas de classificação", "a partir da década de 1990.")), "Ambos os sistemas se encontram representados simplificadamente nas figuras.") + "[[fig:1]]"
                  + p("Comparando as figuras apresentadas, pode-se afirmar corretamente que o sistema de cinco reinos é artificial, dado que"),
     "imagens": figs(("q49", "Duas representações. Sistema de Whittaker: um tronco com cinco áreas sombreadas — na base, bactérias e arqueias; acima, algas verdes, vermelhas e pardas, flagelados, amebas e ciliados; no topo, três ramos separados para plantas terrestres, fungos e animais. Sistema de Woese: uma árvore de parentesco (cladograma) em que bactérias e arqueias saem de ramos distintos e próximos da base, e, entre os eucariontes, fungos ficam junto de animais, algas pardas junto de ciliados, e plantas terrestres junto de algas verdes e vermelhas.")),
     "alternativas": AL(19, "(A) se refere mais às espécies fósseis", "maior biodiversidade na Terra."),
     "explicacao": "<p>O sistema de Whittaker agrupa os seres por critérios como organização celular e modo de nutrição (fotossíntese, absorção, ingestão), e não só por parentesco. Na árvore de Woese, fungos aparecem mais próximos dos animais e as algas se espalham por ramos diferentes, o que mostra que reinos como Protista reúnem seres pouco aparentados. Por isso é considerado artificial. Alternativa <strong>C</strong>.</p><p>Ele trata de seres vivos atuais (A) e é evolucionista, não fixista (B). As análises moleculares são a base do sistema de Woese, não do de Whittaker (D). E não há recorte geográfico (E).</p>"},
50: {"materia": "Português", "assunto": "Variação linguística", "tags": ["Carolina Maria de Jesus"],
     "enunciado": CAROLINA + P50,
     "alternativas": AL(20, "(A) a autora não apresenta reflexão crítica", "como fome e pobreza."),
     "explicacao": "<p>Em linguagem informal, com desvios da norma-padrão, Carolina faz uma crítica forte: “no dia 13 de maio de 1958 eu lutava contra a escravatura atual – a fome!”. Alternativa <strong>E</strong>.</p><p>Há reflexão crítica (A). Ela pretendia, sim, que o diário fosse lido (“Há de existir alguém que lendo o que eu escrevo...”) (B). Desvios de ortografia e concordância não têm relação com denotação (C). E “amanheceu chovendo” e “a chuva passou” são expressões denotativas (D).</p>"},
51: {"materia": "Português", "assunto": "Figuras de linguagem", "tags": ["metáfora"],
     "enunciado": p("Assinale a alternativa que, de acordo com o contexto, apresenta a figura de linguagem metáfora."), "apoio_de": (50, P50),
     "alternativas": AL(20, "(A) Dona Ida peço-te se pode arranjar", "não pude ir catar papel."),
     "explicacao": "<p>Ao chamar a fome de “escravatura atual”, a autora aproxima as duas coisas sem usar conectivo de comparação: é uma <strong>metáfora</strong>. Alternativa <strong>B</strong>.</p><p>As outras frases têm sentido literal.</p>"},
52: {"materia": "Português", "assunto": "Interpretação de texto", "tags": ["charge", "intertextualidade"],
     "enunciado": p("Considere a charge.") + "[[fig:1]]" + url("https://tinyurl.com/y9y5og93", "09.03.2018", "Original colorido.")
                  + p("Comparando a charge ao texto de Carolina Maria de Jesus, conclui-se corretamente que ambos se relacionam à temática"),
     "imagens": figs(("q52", "Charge assinada por Salvador: um catador de boné puxa uma carroça cheia de sacos, garrafas e materiais recicláveis e diz a uma moça, que o olha com um ponto de interrogação: “Eu prefiro usar o termo ‘agente ambiental freelancer’.”")),
     "apoio_de": (50, P50),
     "alternativas": AL(21, "(A) do subemprego, a exemplo das passagens", "É o inverno que chega”."),
     "explicacao": "<p>Tanto a charge quanto o diário mostram o <strong>subemprego</strong>: Carolina sobrevive vendendo ferro-velho e catando papel, como o catador da charge. Alternativa <strong>A</strong>.</p><p>Os trechos citados em B, C, D e E não tratam de racismo, solidariedade, violência urbana ou clima como tema comum aos dois textos.</p>"},
53: {"materia": "Português", "assunto": "Gramática", "tags": ["coesão", "reescrita"],
     "enunciado": p("Assinale a alternativa em que o trecho do diário foi reescrito, mantendo-se as correlações semânticas originais e respeitando-se a variedade culta da língua portuguesa."), "apoio_de": (50, P50),
     "alternativas": AL(21, "(A) Hoje amanheceu chovendo por ser", "o hábito de sorrir."),
     "explicacao": "<p>B mantém o sentido (o dó dos filhos explicado pela reação deles à comida) e corrige a concordância: “eles <strong>veem</strong>”, “eles <strong>bradam</strong>”. Alternativa <strong>B</strong>.</p><p>A cria uma causa absurda para a chuva. C transforma a chuva em causa de ter só feijão e sal, e o “logo” muda o sentido. D troca “até passar” por “mesmo que passe”. E usa “desde que” (condição) onde o original tem oposição (“Mas”).</p>"},
54: {"materia": "Português", "assunto": "Literatura", "tags": ["Modernismo", "Drummond"],
     "enunciado": p("Leia um trecho do poema <em>A Flor e a Náusea</em>.") + "[[fig:1]]" + fonte("ANDRADE, C. D. <em>Antologia Poética</em>. Rio de Janeiro. José Olympio, 1978.")
                  + p("A partir da leitura do trecho de <em>A Flor e a Náusea</em>, poema do modernista Carlos Drummond de Andrade, assinale a alternativa em que o conceito é adequado à temática apresentada nos versos."),
     "imagens": figs(("q54", "Trecho do poema “A Flor e a Náusea”, de Carlos Drummond de Andrade, reproduzido da prova. O eu lírico caminha preso à sua classe por uma rua cinzenta, sente-se cercado de melancolia e diz que o tempo de completa justiça ainda não chegou. Em seguida anuncia, com espanto, que uma flor nasceu na rua, rompendo o asfalto: desbotada, feia, sem nome nos livros, mas realmente uma flor, que “furou o asfalto, o tédio, o nojo e o ódio”.")),
     "alternativas": AL(21, "(A) Disciplina: obediência às regras", "alienado e indiferente."),
     "explicacao": "<p>A flor feia que fura o asfalto simboliza a <strong>esperança</strong>: em meio ao tédio, ao nojo e ao ódio da cidade, algo novo consegue nascer, e o eu lírico acredita na mudança. Alternativa <strong>C</strong>.</p><p>O eu lírico questiona a ordem, não a defende (A). Ele não esconde sua reação: pede silêncio para anunciar a flor (B). Não há saudade da terra natal (D). E ele é inquieto e revoltado, não resignado nem indiferente (E).</p>"},
})
completar(Q, R)
