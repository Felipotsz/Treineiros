# Ajustes da conferência humana: Vestibular FATEC 2º semestre de 2019 (exame de 30/06/2019)
# Texto conferido com a imagem de cada página. Tema implícito: tecnologia e trabalho (redação: como transformar opinião em conhecimento).
# 54 questões; a prova tem 5 h no total, incluindo a redação (que fica fora do simulado).
# Matéria: a do gabarito oficial; nas "Multidisciplinar", a matéria principal + tag "multidisciplinar".
# Rascunho com colunas embaralhadas: todos os enunciados e alternativas foram escritos aqui.
# Gabarito: oficial RETIFICADO (2º SEM/19); Q34 ANULADA (justificativa por análise: unidade das alternativas).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import A, carregar, enun, tabela, colunas, completar, trecho

ID = "fatec-2019-2sem"
META = {
    "id": ID,
    "banca": "FATEC",
    "ano": 2019,
    "semestre": 2,
    "titulo": "Vestibular FATEC, 2º semestre de 2019",
    "fonte": "Centro Paula Souza",
    "dataExame": "2019-06-30",
    "duracaoMinutos": 300,
    "tema": "Tecnologia",
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
PINTEC = (chamada("Leia o texto e os gráficos para responder às questões 08 e 09.")
          + apoio(*T(5, "A Pesquisa de Inovação (Pintec), realizada", "conforme o gráfico.", ["A Pintec, do triênio", "A Pintec 2014 apresentou"]))
          + "[[fig:1]]" + url("https://tinyurl.com/y5mjvjho", "17.06.2019"))
PINTEC_IMG = figs(("q08", "Três gráficos de setores com o número de pesquisadores em P&D por sexo, em 2014. Indústria: 51 573 homens e 14 543 mulheres (78,0% e 22,0%). Eletricidade e gás: 831 homens e 159 mulheres (83,9% e 16,1%). Serviços selecionados: 22 213 homens e 4 958 mulheres (81,8% e 18,2%). Fonte: IBGE, Pesquisa de Inovação 2014."))
P8 = p("De acordo com o texto, a amostra correspondeu a cerca de N% da população estudada.", "Nessas condições, o valor de N é")

CONST = (chamada("Leia o texto e considere a charge do cartunista Henfil para responder às questões 17 e 18.")
         + apoio("Em outubro de 2018, a Constituição brasileira completou trinta anos.",
                 "Promulgado após quase dois anos de trabalho, o texto que lançava as bases para a nova legislação máxima do país foi resultado do grande envolvimento da sociedade – que enviou cartas, organizou-se em movimentos sociais e realizou eventos – e dos parlamentares eleitos após o término do regime militar.",
                 "As demandas da população foram consideradas para a construção de uma Constituição que ampliou direitos e liberdades, o que contribuiu para que ela fosse chamada de “Cidadã”.")
         + "[[fig:1]]" + url("https://tinyurl.com/ya42xtrr", "30.05.2018", ""))
CONST_IMG = figs(("q17", "Charge de Henfil: a bandeira do Brasil, desenhada no chão, cercada de tocos de árvores cortadas. Muitos homenzinhos trabalham sobre ela: uns sobem uma escada até o círculo central, onde está escrito “Constituinte” na faixa, outros repintam e reconstroem as bordas, empurram carrinhos e plantam árvores."))
P17 = p("A Constituição Federal de 1988 revogou a de 1967 que, ao lado dos Atos Institucionais, serviu de base legal para as ações do regime militar.", "O primeiro Ato, assinado dias após o início do regime, em 1964")

LAVOISIER = (chamada("Leia o texto para responder às questões 23 e 24.")
             + apoio("Em seu livro <em>Tratado Elementar de Química</em>, publicado em 1789, Antonie Lavoisier estabeleceu uma nova nomenclatura para diversas substâncias químicas. Alguns exemplos, extraídos desse livro, são dados no quadro.")
             + tabela(["Nome antigo", "Nome proposto por Lavoisier", "Nome atual"],
                      [["ar vital", "oxigênio", "oxigênio"], ["ar inflamável", "hidrogênio", "hidrogênio"], ["ar fixo", "ácido carbônico", "dióxido de carbono"], ["ácido vitriólico", "ácido sulfúrico", "ácido sulfúrico"],
                       ["vitríolo azul; vitríolo de cobre", "sulfato de cobre", "sulfato de cobre(II)"], ["ácido marinho", "ácido muriático", "ácido clorídrico"], ["sal marinho", "muriato de soda", "cloreto de sódio"], ["soda aerada; soda efervescente", "carbonato de soda", "carbonato de sódio"]]))
P23 = p("Examinando o quadro, identifique as duas substâncias simples nele presentes pelos seus nomes antigos.")

SKILL = (chamada("Leia o texto para responder às questões de 25 a 29.")
         + apoio("<strong>The Most Important Skill For 21st–Century Success</strong>", "By <u>Kevin H. Johnson</u>")
         + "[[fig:1]]"
         + apoio(*T(11, "The world of work is changing so rapidly", "maintain momentum and productivity.", ["It’s one thing to keep up", "There’s so much uncertainty", "When people embrace lifelong", "A learning mindset also"]))
         + url("https://tinyurl.com/ya42xtrr", "15.03.2019", "Adaptado. Original colorido."))
SKILL_IMG = figs(("q25", "Foto de uma jovem sorrindo, sentada diante de um notebook e de uma xícara de café. Na parede, desenhos em giz ligados por setas a um círculo central “your career” (sua carreira): “learn and research” (aprenda e pesquise), “think different” (pense diferente), “define career goals” (defina metas de carreira), “build professional relationships” (construa relações profissionais) e “be positive” (seja positivo)."))
P25 = p("Para o autor, devido à contínua evolução da tecnologia e às mudanças constantes no mundo do trabalho, os profissionais do século XXI precisam permanecer em modo de aprendizagem para")

LAPTOP = (chamada("Leia o texto para responder às questões de 51 a 54.")
          + apoio("<strong>Empresa transforma seu laptop escolar em ‘e-book’</strong>",
                  *[it(x, "Classmate", "Valor Econômico") for x in T(20, "Os fabricantes de produtos eletrônicos deram", "nas prateleiras nos próximos meses.", ["A bateria do equipamento", "Enquanto olha para licitações"])])
          + fonte("BORGES, André. <em>Valor Econômico</em>, 07.03.2010. Adaptado."))
P51 = p("De acordo com as informações do texto, é correto afirmar que")

Q = {
1: {"materia": "História", "assunto": "América colonial", "tags": MULTI + ["mercantilismo", "mineração"],
    "enunciado": p(*T(2, "Potosi e Vila Rica foram duas cidades", "política econômica à qual o texto se refere.", ["Assinale a alternativa"])),
    "alternativas": colunas(["Metais extraídos", "Política econômica"], [["Diamante e cobre", "Monetarismo"], ["Ouro e diamante", "Monetarismo"], ["Cobre e níquel", "Metalismo"], ["Prata e ouro", "Mercantilismo"], ["Níquel e prata", "Mercantilismo"]]),
    "explicacao": "<p>Em Potosí (atual Bolívia) explorava-se <strong>prata</strong>; em Vila Rica (atual Ouro Preto), <strong>ouro</strong>. Acumular metais (metalismo), manter a balança comercial favorável e o monopólio colonial são as práticas do <strong>mercantilismo</strong>. Alternativa <strong>D</strong>.</p><p>Monetarismo é uma teoria econômica do século XX (A e B). Metalismo é só uma das práticas mercantilistas, e cobre e níquel não eram o foco (C). Níquel não era explorado nessas cidades (E).</p>"},
2: {"materia": "Química", "assunto": "Química ambiental", "tags": MULTI + ["efeito estufa"],
    "enunciado": p(T(2, "Durante o século XX, a temperatura global", "mudanças climáticas")[0]),
    "explicacao": "<p>O principal responsável pela intensificação do efeito estufa é o <strong>aumento do CO₂</strong> na atmosfera, emitido sobretudo pela queima de combustíveis fósseis e pelo desmatamento. Alternativa <strong>C</strong>.</p><p>O oxigênio não é gás estufa (A). O metano é gás estufa, e o problema é seu aumento, não a diminuição (B). O petróleo no mar polui os oceanos, mas não é a causa principal (D). E a redução dos CFCs ajuda a recuperar a camada de ozônio (E).</p>"},
3: {"materia": "Química", "assunto": "Reações químicas", "tags": MULTI + ["hidrogênio", "eletrólise"],
    "enunciado": p(*T(2, "As duas maiores esperanças para as fontes", "assinale a alternativa correta.", ["Esta é a chamada", "Sobre o processo descrito"])),
    "explicacao": "<p>O texto descreve o uso da energia solar para quebrar moléculas de água e produzir hidrogênio, que depois abastece células a combustível. Alternativa <strong>D</strong>.</p><p>A fotossíntese natural produz glicose; a artificial descrita produz hidrogênio (A e E). O processo é considerado limpo, sem metais pesados (B). E quebrar a água exige energia: o processo é endotérmico (C).</p>"},
4: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": MULTI + ["quadrinhos"],
    "enunciado": "[[fig:1]]" + url("https://tinyurl.com/y6fbtptu", "15.03.2019", "Original colorido.")
                 + p("Nos quadrinhos, pode-se observar que Alice se sente um tanto quanto decepcionada com a formação do novo líder porque ele"),
    "imagens": figs(("q04", "Tirinha de Dilbert, em inglês, em oito quadros. O chefe apresenta a Alice o novo gerente, Keith, “altamente qualificado”, com mestrado em Administração. Alice pergunta se ele aprendeu a motivar funcionários (“No, not really”), a identificar e contratar boas pessoas (“That might have been optional reading”), negociação, pensamento estratégico, escrita de negócios (“No”, “No”, “No”). Ele diz que o curso foi mais de finanças, contabilidade e economia. Alice conclui: “So, you're a highly qualified leader because… you're good at math?”. No último quadro, Keith pergunta “What should I do here?” e o chefe responde: “In these situations I like to use swearing” (nessas situações eu gosto de xingar).")),
    "explicacao": "<p>Keith tem mestrado em Administração e estudou finanças, contabilidade e economia, mas não sabe motivar pessoas, contratar, negociar nem pensar estrategicamente. Ele tem formação técnica, mas não as <strong>habilidades socioemocionais</strong> de um líder. Alternativa <strong>E</strong>.</p><p>Não é só competência linguística (A) nem só comunicativa (D). Ele não domina a motivação (B) e não sabe contratar (C).</p>"},
5: {"materia": "Física", "assunto": "Dinâmica", "tags": MULTI + ["quantidade de movimento"],
    "enunciado": p("Em uma aula do curso de Logística Aeroportuária, o professor propõe aos alunos que determinem a quantidade de movimento da aeronave tipo 737–800 em voo de cruzeiro, considerando condições ideais. Para isso ele apresenta valores aproximados, fornecidos pelo fabricante da aeronave.")
                 + tabela(["INFORMAÇÃO", "DADO"], [["Massa Máxima de Decolagem", "79 000 kg"], ["Velocidade média de cruzeiro", "720 km/h"]])
                 + p("Com base nos dados apresentados no quadro, o resultado aproximado esperado é, em kg·m/s,"),
    "alternativas": alts("1,6 × 10<sup>7</sup>", "2,0 × 10<sup>7</sup>", "2,6 × 10<sup>7</sup>", "3,0 × 10<sup>7</sup>", "3,6 × 10<sup>7</sup>"),
    "explicacao": "<p>v = 720 ÷ 3,6 = 200 m/s. Q = m · v = 79 000 · 200 = 15 800 000 ≈ <strong>1,6 × 10⁷ kg·m/s</strong>. Alternativa <strong>A</strong>.</p><p>Os outros valores vêm de erros na conversão de km/h para m/s.</p>"},
6: {"materia": "Português", "assunto": "Figuras de linguagem", "tags": MULTI + ["prosopopeia"],
    "enunciado": "[[fig:1]]" + url("https://tinyurl.com/yynj49zv", "20.06.2019", "Original colorido.") + p("O humor dos quadrinhos apresentados constrói-se por meio de"),
    "alternativas": alts("antítese, constituída pela oposição entre “corpo” e “mente”.", "catacrese, presente na caracterização do cérebro como “mente saudável”.",
                         "aliteração, decorrente da incoerência entre o conceito de “movimento” e “observação”.", "prosopopeia, decorrente da representação da mente como um ser animado.",
                         "silepse, composta pela repetição do termo “vai” na mesma posição."),
    "imagens": figs(("q06", "Quadrinhos de Guilherme Bandeira, em quatro quadros: um cérebro de óculos, com braços e pernas, corre suando numa esteira, com uma toalha pendurada. No segundo quadro, ele grita para o leitor: “Vai ficar aí só olhando? Exercite essa mente também!”. Depois, ofega (“Uf! Uf!”) e, no último quadro, grita “Vai!”.")),
    "explicacao": "<p>O cérebro (a mente) aparece com braços, pernas, óculos e fala, correndo numa esteira e cobrando o leitor: é a <strong>prosopopeia</strong> (personificação), que dá vida e traços humanos a algo que não os tem. Alternativa <strong>D</strong>.</p><p>Não há oposição entre corpo e mente (A), nem catacrese (B). Aliteração é repetição de sons consonantais (C). E a repetição de “vai” não é silepse (E).</p>"},
7: {"materia": "Geografia", "assunto": "Globalização", "tags": MULTI + ["mercado de trabalho"],
    "enunciado": apoio(*[it(x, "e-commerce", "e-learning") for x in T(4, "Mais de três mil gerentes de operações", "se destacam pelo volume de vagas.", ["Além do impacto", "Multinacionais e empresas", "No Brasil, funções"])])
                 + url("https://tinyurl.com/y5co327k", "17.06.2019") + p("De acordo com o texto, é correto afirmar que no Brasil"),
    "explicacao": "<p>O texto diz que há “dificuldade de recrutamento, sobretudo no Brasil”, porque “a oferta de pessoas qualificadas e bem preparadas é baixa”. Alternativa <strong>D</strong>.</p><p>As vagas ligadas à internet estão crescendo, e falta mão de obra (A e E). Os avanços tecnológicos criam novas funções (B). E o texto não diz que o desemprego atinge os qualificados (C).</p>"},
8: {"materia": "Matemática", "assunto": "Porcentagem", "tags": MULTI + ["amostragem"],
    "enunciado": PINTEC + P8, "imagens": PINTEC_IMG,
    "explicacao": "<p>A amostra de 17 mil empresas sobre um universo de 130 mil: 17 ÷ 130 ≈ 0,13, ou <strong>13%</strong>. Alternativa <strong>B</strong>.</p><p>Os outros valores não saem dessa razão.</p>"},
9: {"materia": "Matemática", "assunto": "Interpretação de dados", "tags": MULTI + ["gráfico de setores"],
    "enunciado": p("Analisando os gráficos, é correto afirmar que,"), "apoio_de": (8, P8),
    "explicacao": "<p>Em Eletricidade e gás há 831 homens e 159 mulheres: 831 ÷ 159 ≈ 5,2, cerca de <strong>cinco homens para cada mulher</strong>. Alternativa <strong>E</strong>.</p><p>A participação masculina na Indústria (78,0%) é a menor dos três setores (A). Nos Serviços, as mulheres são 18,2%, e 16,1% é o valor de Eletricidade e gás (B). 159 é um número de pessoas, não uma porcentagem (C). E as mulheres somam 14 543 + 159 + 4 958 = 19 660, menos de 20 000 (D).</p>"},
10: {"materia": "Raciocínio lógico", "assunto": "Lógica", "tags": ["proposição"],
     "explicacao": "<p>Uma proposição é uma oração declarativa que pode ser verdadeira ou falsa. “Toda prova de raciocínio lógico é fabulosa” afirma algo que pode ser julgado: é uma proposição. Alternativa <strong>C</strong>.</p><p>Exclamações (A), frases sem verbo (B), perguntas (D) e ordens (E) não podem ser classificadas como verdadeiras ou falsas.</p>"},
11: {"materia": "Raciocínio lógico", "assunto": "Operações e problemas", "tags": ["divisão euclidiana"],
     "enunciado": p("A divisão é uma das quatro operações fundamentais da Aritmética e pode ser representada utilizando o algoritmo:")
                  + apoio("Dividendo | Divisor<br>Resto &nbsp; &nbsp; Quociente")
                  + p("Considere que, no conjunto dos números naturais, a divisão de 43 por 5 tem quociente q. Seja N o número natural tal que (N + 43) dividido por 5 tem como quociente (q + 500).", "Nessas condições, o menor valor de N é"),
     "alternativas": alts("2 497.", "2 498.", "2 499.", "2 500.", "2 501."),
     "explicacao": "<p>43 ÷ 5 tem quociente q = 8. Então (N + 43) ÷ 5 tem quociente 508, ou seja, N + 43 fica entre 5 · 508 = 2 540 e 2 544. O menor valor é N + 43 = 2 540, então N = <strong>2 497</strong>. Alternativa <strong>A</strong>.</p><p>2 500 viria de somar 500 · 5 sem considerar o resto da divisão de 43 (D).</p>"},
12: {"materia": "Raciocínio lógico", "assunto": "Sequências", "tags": ["progressão aritmética"],
     "enunciado": p("Uma fábrica deve produzir diariamente 523 canetas. Contudo, o encarregado da linha de produção, após analisar os resultados de 5 dias consecutivos, notou as seguintes quantidades produzidas por dia, apresentadas no quadro.")
                  + tabela(["Dia 1", "Dia 2", "Dia 3", "Dia 4", "Dia 5"], [["523", "520", "517", "514", "511"]])
                  + p(*T(6, "A partir da análise desses dados, o encarregado", "atividades, será", ["Se nenhuma providência"])),
     "alternativas": alts("0.", "1.", "2.", "3.", "4."),
     "explicacao": "<p>A produção cai 3 canetas por dia: 523, 520, 517, ... Como 523 = 3 · 174 + 1, os termos deixam resto 1 na divisão por 3: ..., 7, 4, <strong>1</strong>. O próximo seria −2, impossível, e as máquinas param. Alternativa <strong>B</strong>.</p><p>0 só apareceria se 523 fosse múltiplo de 3 (A).</p>"},
13: {"materia": "Raciocínio lógico", "assunto": "Lógica", "tags": ["relógio"],
     "explicacao": "<p>Ariel achava que o relógio estava 3 min atrasado, então somava 3 ao que via. Ela julgou estar 8 min atrasada: o relógio marcava 8 − 3 = 5 min depois do horário da prova. Mas o relógio estava 12 min adiantado, então a hora real era 12 − 5 = 7 min antes do horário: ela estava <strong>7 minutos adiantada</strong>. Alternativa <strong>D</strong>.</p><p>Os outros valores vêm de somar ou subtrair os atrasos de forma errada.</p>"},
14: {"materia": "Raciocínio lógico", "assunto": "Lógica", "tags": ["silogismo"],
     "enunciado": p("Silogismo é uma estrutura lógica que designa uma forma de raciocínio dedutivo, que é exemplificado no cartum.") + "[[fig:1]]"
                  + url("https://tinyurl.com/y47qc39c", "17.06.2019", "") + p("Assinale a alternativa que apresenta a estrutura tradicional pela qual o silogismo é formado."),
     "imagens": figs(("q14", "Cartum de Glasbergen: um pinguim pensa “O pinguim é branco e preto. Alguns filmes antigos são branco e preto. Portanto, alguns pinguins são filmes antigos.” Legenda: “Lógica: Outro ponto fraco dos pinguins.”")),
     "explicacao": "<p>O silogismo clássico tem <strong>duas premissas</strong> (uma maior e uma menor) e <strong>uma conclusão</strong> que decorre delas, como no pensamento do pinguim (ainda que o raciocínio dele seja inválido). Alternativa <strong>C</strong>.</p><p>Uma premissa só não forma silogismo (A e B), e sem conclusão não há dedução (D e E).</p>"},
15: {"materia": "História", "assunto": "Brasil Império", "tags": ["tráfico de escravizados", "café"],
     "enunciado": p(*T(7, "O Brasil foi o principal destino dos africanos", "corresponde corretamente ao contexto apresentado no texto.", ["Assinale a alternativa"])),
     "explicacao": "<p>No século XIX, a cafeicultura do Sudeste (Rio de Janeiro, Minas Gerais e São Paulo) foi o principal destino dos africanos escravizados, chegando por portos muitas vezes clandestinos. Alternativa <strong>B</strong>.</p><p>O tráfico foi proibido em 1850 (Lei Eusébio de Queirós), e a abolição veio em 1888 (A). Os EUA aboliram a escravidão em 1865 (C). A mão de obra predominante era africana (D). E a maioria vinha da África centro-ocidental, como Angola e Congo, não do Chifre da África (E).</p>"},
16: {"materia": "História", "assunto": "América colonial", "tags": ["independências", "Bolívar"],
     "enunciado": apoio(T(7, "O nome com que foi batizado o maior torneio", "independência de diversos países.")[0])
                  + url("https://tinyurl.com/y72ma2xo", "31.05.2018") + p("Sobre esses processos de independência, é correto afirmar que"),
     "explicacao": "<p>Bolívar sonhava unir as ex-colônias espanholas numa grande nação. Chegou a criar a Grã-Colômbia (Venezuela, Colômbia, Equador e Panamá), que se desfez em 1831, e o Congresso do Panamá (1826) não levou à união. Alternativa <strong>C</strong>.</p><p>Bolívar era republicano (A). Venezuela, Bolívia e Panamá são países distintos (B). Os países do Prata não se uniram ao Brasil (D). E San Martín atuou na Argentina, no Chile e no Peru, não na Guatemala (E).</p>"},
17: {"materia": "História", "assunto": "Ditadura militar", "tags": ["Atos Institucionais"],
     "enunciado": CONST + P17, "imagens": CONST_IMG,
     "explicacao": "<p>O AI-1 (abril de 1964) permitiu cassar mandatos e suspender direitos políticos e estabeleceu a eleição indireta do presidente pelo Congresso. Alternativa <strong>C</strong>.</p><p>A anistia veio em 1979 (A). O fim do <em>habeas corpus</em> para crimes políticos e o fechamento do Congresso vieram com o AI-5, de 1968 (B). O bipartidarismo veio com o AI-2, de 1965, e as eleições para prefeitos das capitais ficaram indiretas (D). E a tortura nunca foi legalizada (E).</p>"},
18: {"materia": "História", "assunto": "Brasil República", "tags": ["Constituição de 1988", "charge"],
     "enunciado": p("A Assembleia Nacional Constituinte de 1987–1988, que elaborou as novas leis do Brasil, foi representada por Henfil, na charge, como"), "apoio_de": (17, P17),
     "explicacao": "<p>Na charge, o povo trabalha para reconstruir a bandeira, cercada de tocos de árvores, enquanto outros sobem até a faixa “Constituinte”. É a <strong>reconstrução do país pela população</strong> depois do regime militar. Alternativa <strong>D</strong>.</p><p>A charge não trata de proteção ambiental nas constituições anteriores (A), nem da mudança da bandeira (B) ou dos governadores (C). E quem trabalha é o povo, não intelectuais (E).</p>"},
19: {"materia": "História", "assunto": "História contemporânea", "tags": ["nazifascismo"],
     "enunciado": apoio(T(9, "As condições ideais para o triunfo do nazifascismo", "nazistas de Hitler.")[0])
                  + fonte("HOBSBAWN, Eric. <em>Era dos Extremos: o breve século XX (1914-1991)</em>. 2ª ed. São Paulo: Companhia das Letras, 1995, p.130. Adaptado.")
                  + p("De acordo com o texto e com o contexto ao qual o autor se refere, é correto afirmar que"),
     "explicacao": "<p>A ascensão do nazismo e do fascismo levou à <strong>Segunda Guerra Mundial</strong> e ao <strong>Holocausto</strong>. Alternativa <strong>E</strong>.</p><p>Depois da Primeira Guerra houve crise, não prosperidade (A). Os nazifascistas se aliaram às elites liberais e perseguiram socialistas e comunistas (B). A Grande Depressão foi causada pela crise de 1929, e não pelo descontentamento com a ultradireita (C). E o texto fala de instituições que “não mais funcionavam” (D).</p>"},
20: {"materia": "Química", "assunto": "Substâncias e misturas", "tags": ["siderurgia"],
     "enunciado": apoio("A produção do aço ocorre nas usinas siderúrgicas em ____<strong>I</strong>____, e tem como principais matérias-primas minérios de ____<strong>II</strong>____ e ____<strong>III</strong>____.")
                  + p("Assinale a alternativa que completa, corretamente, o texto."),
     "alternativas": colunas(["I", "II", "III"], [["altos-fornos", "ferro", "carvão"], ["altos-fornos", "ferro", "cobre"], ["altos-fornos", "cobre", "zinco"], ["cubas eletrolíticas", "ferro", "carvão"], ["cubas eletrolíticas", "cobre", "zinco"]]),
     "explicacao": "<p>O aço é uma liga de ferro com pouco carbono, produzida em <strong>altos-fornos</strong> a partir do minério de <strong>ferro</strong> e do <strong>carvão</strong> (coque), que fornece calor e retira o oxigênio do minério. Alternativa <strong>A</strong>.</p><p>Cobre e zinco formam o latão, não o aço (B, C e E). E cubas eletrolíticas são usadas na produção do alumínio, por exemplo (D e E).</p>"},
21: {"materia": "Química", "assunto": "Estequiometria", "tags": ["combustão"],
     "enunciado": p("Hidrocarbonetos podem ser usados como combustível, por exemplo o gás but-1-eno.", "Assinale a alternativa que apresenta a fórmula molecular e a quantidade mínima, em kg, de gás oxigênio necessária para a combustão completa de 5,6 kg desse combustível.")
                  + apoio("Massas Molares:<br>H = 1 g/mol<br>O = 16 g/mol<br>C = 12 g/mol"),
     "alternativas": colunas(["Fórmula", "Massa (kg)"], [["C<sub>3</sub>H<sub>6</sub>", "19,2"], ["C<sub>4</sub>H<sub>8</sub>", "19,2"], ["C<sub>4</sub>H<sub>8</sub>", "3,2"], ["C<sub>3</sub>H<sub>6</sub>", "3,2"], ["C<sub>4</sub>H<sub>10</sub>", "19,2"]]),
     "explicacao": "<p>O but-1-eno tem 4 carbonos (“but”) e uma dupla ligação (“eno”): <strong>C₄H₈</strong> (56 g/mol). A combustão é C₄H₈ + 6 O₂ → 4 CO₂ + 4 H₂O. 5,6 kg são 100 mol, que precisam de 600 mol de O₂ = 600 · 32 g = <strong>19,2 kg</strong>. Alternativa <strong>B</strong>.</p><p>C₃H₆ é o propeno, e C₄H₁₀, o butano (A, D e E). 3,2 kg corresponderia a apenas 1 mol de O₂ por mol de combustível (C e D).</p>"},
22: {"materia": "Química", "assunto": "Ácidos e bases", "tags": ["pH", "Kw"],
     "enunciado": p("A escala de pH que varia de 0 a 14 é válida apenas para sistemas aquosos a 25 °C. Variando-se a temperatura, a escala de pH também varia.", "O quadro fornece valores de Kw e de pH da água pura em diferentes temperaturas.")
                  + tabela(["Temperatura (°C)", "Kw", "pH"], [["0", "1,14 × 10<sup>–15</sup>", "7,47"], ["10", "2,95 × 10<sup>–15</sup>", "7,27"], ["20", "1,00 × 10<sup>–14</sup>", "7,00"], ["30", "1,47 × 10<sup>–14</sup>", "6,83"], ["50", "5,30 × 10<sup>–14</sup>", "6,27"]])
                  + p("Analisando-se os dados, pode-se afirmar, corretamente, que a"),
     "alternativas": alts("concentração de íons OH<sup>–</sup>(aq) na água pura diminui com o aumento de temperatura.", "concentração de íons H<sup>+</sup>(aq) na água pura diminui com o aumento de temperatura.",
                          "água pura é ácida em temperaturas superiores a 25 °C.", "água pura é ácida em temperaturas inferiores a 25 °C.", "água pura é neutra em qualquer temperatura."),
     "explicacao": "<p>Na água pura, [H⁺] = [OH⁻] em qualquer temperatura, porque cada molécula que se ioniza forma um H⁺ e um OH⁻. Por isso ela é sempre <strong>neutra</strong>, ainda que o pH de neutralidade mude com a temperatura. Alternativa <strong>E</strong>.</p><p>Kw aumenta com a temperatura, então [H⁺] e [OH⁻] aumentam (A e B). Um pH abaixo de 7 acima de 25 °C não significa acidez, porque [H⁺] continua igual a [OH⁻] (C e D).</p>"},
23: {"materia": "Química", "assunto": "Substâncias e misturas", "tags": ["substâncias simples", "nomenclatura"],
     "enunciado": LAVOISIER + P23,
     "alternativas": alts("ar vital e ar fixo", "ar vital e ar inflamável", "sal marinho e soda aerada", "ácido vitriólico e ácido muriático", "vitríolo azul e soda efervescente"),
     "explicacao": "<p>Substâncias simples são formadas por um só elemento. No quadro, só o oxigênio (O₂, “ar vital”) e o hidrogênio (H₂, “ar inflamável”). Alternativa <strong>B</strong>.</p><p>O “ar fixo” é o CO₂ (A). Sal marinho, soda aerada, os ácidos e o vitríolo azul são substâncias compostas (C, D e E).</p>"},
24: {"materia": "Química", "assunto": "Reações químicas", "tags": ["dióxido de carbono"],
     "enunciado": p("A reação química que ocorre entre as substâncias denominadas por Lavoisier como carbonato de soda e ácido muriático é evidenciada pela formação rápida de um gás que é muito conhecido por ser um dos responsáveis pela intensificação do efeito estufa e por ser indispensável à realização da fotossíntese vegetal.",
                    "Esse gás é o que, antigamente, era chamado de"),
     "apoio_de": (23, P23),
     "alternativas": alts("ácido vitriólico.", "vitríolo azul.", "sal marinho.", "ar inflamável.", "ar fixo."),
     "explicacao": "<p>Carbonato de sódio + ácido clorídrico → cloreto de sódio + água + <strong>CO₂</strong>. O gás estufa usado na fotossíntese é o dióxido de carbono, antigamente chamado de “ar fixo”. Alternativa <strong>E</strong>.</p><p>Ácido vitriólico é o ácido sulfúrico (A), vitríolo azul é o sulfato de cobre (B), sal marinho é o cloreto de sódio (C) e ar inflamável é o hidrogênio (D).</p>"},
25: {"materia": "Inglês", "assunto": "Interpretação de texto",
     "enunciado": SKILL + P25, "imagens": SKILL_IMG,
     "alternativas": alts("automatizar suas habilidades.", "evitar o trabalho em <em>home office</em>.", "estratificar suas habilidades correntes.", "continuar imprescindíveis no mercado.", "compreender melhor o pensamento dos engenheiros."),
     "explicacao": "<p>O autor diz que os profissionais precisam continuar aprendendo “so their skills don’t lose currency” (para que suas habilidades não percam valor): para <strong>continuarem necessários</strong> no mercado. Alternativa <strong>D</strong>.</p><p>O texto não fala em automatizar habilidades (A), evitar o <em>home office</em> (B) nem estratificar habilidades (C). Os engenheiros são citados por imaginarem tecnologias futuras (E).</p>"},
26: {"materia": "Inglês", "assunto": "Verbos", "tags": ["verbos modais"],
     "enunciado": p("O verbo <em>may</em>, na oração do segundo parágrafo “<em>It’s a whole different challenge to prepare yourself for tools and technologies that may exist only in the minds of engineers, if at all</em>”, indica"),
     "apoio_de": (25, P25),
     "alternativas": alts("recomendação.", "probabilidade.", "habilidade.", "obrigação.", "conclusão."),
     "explicacao": "<p><em>May</em> indica possibilidade ou <strong>probabilidade</strong>: tecnologias que “talvez existam” só na cabeça dos engenheiros. Alternativa <strong>B</strong>.</p><p>Recomendação seria <em>should</em> (A), habilidade, <em>can</em> (C), obrigação, <em>must</em> (D), e conclusão, <em>therefore</em> (E).</p>"},
27: {"materia": "Inglês", "assunto": "Vocabulário",
     "enunciado": p("Na oração do terceiro parágrafo “<em>... when anyone asks what the next <u>‘hot’ skill</u> will be</em>”, entende-se a expressão grifada como"), "apoio_de": (25, P25),
     "alternativas": alts("experiência resultante de muito investimento em formação acadêmica.", "certificação capaz de abrir portas para a pesquisa.", "conhecimento das novas tecnologias.", "tendência de forte apelo emocional.", "habilidade inovadora e desejada."),
     "explicacao": "<p><em>Hot</em>, em sentido figurado, significa “em alta”, “muito procurado”. A <em>hot skill</em> é uma <strong>habilidade nova e desejada</strong> pelo mercado. Alternativa <strong>E</strong>.</p><p>A expressão não trata de formação acadêmica (A), certificação (B) ou apelo emocional (D). E o autor diz que a habilidade em alta é aprender, não conhecer tecnologias específicas (C).</p>"},
28: {"materia": "Inglês", "assunto": "Vocabulário",
     "enunciado": p("No texto, a expressão <em>lifelong learning</em>, presente no quarto parágrafo do texto, significa a habilidade de"), "apoio_de": (25, P25),
     "alternativas": alts("separar o processo do resultado.", "adaptar-se ao medo e ao estresse.", "aprender continuamente ao longo da vida.", "ter longevidade devido às novas tecnologias.", "fixar-se no domínio imediato de conhecimento."),
     "explicacao": "<p><em>Lifelong</em> significa “que dura a vida toda”, e <em>learning</em>, “aprendizagem”: <strong>aprender continuamente ao longo da vida</strong>. Alternativa <strong>C</strong>.</p><p>Separar processo e resultado é uma consequência citada (A). O texto diz que, para quem aprende sempre, aprender não é fonte de medo e estresse (B). Não fala de longevidade (D). E diz que é bom ficar menos fixado no domínio imediato (E).</p>"},
29: {"materia": "Inglês", "assunto": "Interpretação de texto",
     "enunciado": p("Na oração “<em>A learning mindset also makes it less likely you’ll be thrown off or immobilized when a project changes scope or a job function undergoes transformation</em>”, presente no quinto parágrafo do texto, o autor afirma que as pessoas que têm disposição para aprender têm menor chance de"),
     "apoio_de": (25, P25),
     "alternativas": alts("gostar de mudanças em suas funções.", "ter novos projetos e funções atribuídas.", "projetar mudanças no escopo de um projeto.", "aceitar transformações no escopo de um projeto.", "sair da equipe no caso de mudanças no escopo de um projeto."),
     "explicacao": "<p><em>Thrown off</em> é “ser tirado do rumo”, “ficar desnorteado”, e <em>immobilized</em>, “paralisado”. Quem tem disposição para aprender tem menos chance de ser afastado ou travado quando o projeto muda: de <strong>sair da equipe</strong>. Alternativa <strong>E</strong>.</p><p>A frase fala do que fica menos provável; gostar de mudanças, receber novas funções, projetar e aceitar transformações seriam mais prováveis, não menos (A, B, C e D).</p>"},
30: {"materia": "Matemática", "assunto": "Operações e problemas", "tags": ["despesas de viagem"],
     "enunciado": p("Um grupo de cinco amigos resolveu passar o final de semana em um hotel fazenda no interior do estado de São Paulo. Todos foram juntos no mesmo carro e decidiram dividir, igualmente, a despesa total da viagem entre os cinco participantes.")
                  + apoio("Dados da viagem de carro:<br>• a distância percorrida ida e volta foi de 432 km;<br>• o consumo de gasolina do veículo foi de 9 km/L;<br>• o preço da gasolina foi de R$ 4,50/L;<br>• o valor de cada pedágio foi de<br>&nbsp; &nbsp; P1: R$ 10,00<br>&nbsp; &nbsp; P2: R$ 2,50<br>&nbsp; &nbsp; P3: R$ 4,40<br>&nbsp; &nbsp; P4: R$ 2,70")
                  + p("Sabendo que todos os pedágios foram pagos na ida e na volta, cada amigo gastou em transporte, considerando apenas a gasolina e os pedágios, a quantia de"),
     "alternativas": alts("R$ 43,20.", "R$ 45,24.", "R$ 47,12.", "R$ 51,04.", "R$ 53,08."),
     "explicacao": "<p>Gasolina: 432 ÷ 9 = 48 L · 4,50 = R$ 216,00. Pedágios: (10 + 2,50 + 4,40 + 2,70) · 2 = 19,60 · 2 = R$ 39,20. Total: R$ 255,20, dividido por 5: <strong>R$ 51,04</strong>. Alternativa <strong>D</strong>.</p><p>Só a gasolina daria R$ 43,20 (A). E contar os pedágios só na ida daria R$ 47,12 (C).</p>"},
31: {"materia": "Matemática", "assunto": "Geometria espacial", "tags": ["volume", "cilindro"],
     "enunciado": p("De um paralelepípedo retorretângulo de 30 cm, 4 cm e 15 cm, é removido um semicilindro circular reto de altura 4 cm e base de diâmetro 20 cm, obtendo-se uma peça como mostra a figura.") + "[[fig:1]]"
                  + apoio("Adote π = 3.") + p("Assim sendo, o volume da peça é, em centímetros cúbicos,"),
     "imagens": figs(("q31", "Bloco em forma de paralelepípedo de 30 cm de comprimento, 15 cm de altura e 4 cm de espessura, com um arco semicircular de 20 cm de diâmetro recortado na base, como um túnel.")),
     "alternativas": alts("1 100.", "1 200.", "1 300.", "1 400.", "1 500."),
     "explicacao": "<p>Paralelepípedo: 30 · 15 · 4 = 1 800 cm³. Semicilindro de raio 10 cm e altura 4 cm: (π · 10² ÷ 2) · 4 = (3 · 100 ÷ 2) · 4 = 600 cm³. Peça: 1 800 − 600 = <strong>1 200 cm³</strong>. Alternativa <strong>B</strong>.</p><p>Tirar o cilindro inteiro daria 600 cm³, e esquecer de dividir por 2 o semicilindro leva a valores errados.</p>"},
32: {"materia": "Matemática", "assunto": "Probabilidade", "tags": ["divisores"],
     "enunciado": p("De uma caixa com 50 cartões numerados de 1 a 50, sorteia-se aleatoriamente um cartão. A probabilidade de que o número sorteado seja divisor de 30 é um valor"),
     "alternativas": alts("entre \\(\\tfrac{1}{7}\\) e \\(\\tfrac{1}{5}\\).", "igual a \\(\\tfrac{1}{5}\\).", "entre \\(\\tfrac{1}{5}\\) e \\(\\tfrac{1}{2}\\).", "igual a \\(\\tfrac{1}{2}\\).", "maior que \\(\\tfrac{1}{2}\\)."),
     "explicacao": "<p>Os divisores de 30 são 1, 2, 3, 5, 6, 10, 15 e 30: 8 números. A probabilidade é 8 ÷ 50 = 0,16. Como 1/7 ≈ 0,143 e 1/5 = 0,2, ela fica <strong>entre 1/7 e 1/5</strong>. Alternativa <strong>A</strong>.</p><p>Os demais intervalos não contêm 0,16.</p>"},
33: {"materia": "Física", "assunto": "Hidrostática", "tags": ["Teorema de Stevin", "função do 1º grau"],
     "enunciado": p(*T(14, "O Teorema de Stevin relaciona a pressão atmosférica", "é dada por uma função polinomial do 1º grau."),
                    "O gráfico apresenta a variação da pressão (P) em função da altura da coluna de líquido (h) em um tanque de combustível.") + "[[fig:1]]"
                  + p("Nessas condições, a pressão (P) exercida em um ponto desse líquido que se encontra a 4 m de profundidade é, em Pa,"),
     "imagens": figs(("q33", "Gráfico de P (× 10⁵ Pa) por h (m): uma reta que parte de 1,00 em h = 0 e chega a 1,75 em h = 10.")),
     "alternativas": alts("1,3 × 10<sup>0</sup>", "1,6 × 10<sup>0</sup>", "1,3 × 10<sup>3</sup>", "1,3 × 10<sup>5</sup>", "1,6 × 10<sup>5</sup>"),
     "explicacao": "<p>A reta sobe 0,75 × 10⁵ Pa em 10 m, ou 0,075 × 10⁵ Pa por metro. A 4 m: P = 1,00 × 10⁵ + 4 · 0,075 × 10⁵ = 1,30 × 10⁵ Pa. Alternativa <strong>D</strong>.</p><p>Esquecer o fator 10⁵ do eixo dá A e C. E 1,6 × 10⁵ viria de calcular com 8 m (E).</p>"},
34: {"materia": "Matemática", "assunto": "Razão e proporção", "tags": ["escada"],
     "enunciado": p("Considere que será construída uma escada para vencer uma distância vertical de 126 cm. No projeto, todos os degraus têm as mesmas dimensões, conforme a figura 1. A figura 2 apresenta um esquema da escada.") + "[[fig:1]]" + "[[fig:2]]"
                  + p("Assim sendo, o comprimento horizontal da escada (x) é, em metros,"),
     "imagens": figs(("q34a", "Figura 1: perfil de degraus, cada um com 18 cm de altura (espelho) e 28 cm de profundidade (piso)."),
                     ("q34b", "Figura 2: esquema da escada, de um patamar superior a um piso inferior, com desnível total de 126 cm; o comprimento horizontal x vai do primeiro degrau ao último.")),
     "alternativas": alts("140.", "156.", "168.", "184.", "192."),
     "anulacao": {"fonte": "analise", "motivo": "O Centro Paula Souza anulou a questão no gabarito retificado sem publicar o motivo. Pela análise do Treineiros, o problema está na unidade: o enunciado pede o comprimento “em metros”, mas os valores das alternativas (140, 156, 168...) só fazem sentido em centímetros. Uma escada de 168 metros para subir 1,26 m é absurda, então nenhuma alternativa está correta como foi escrita."},
     "explicacao": "<p>Questão anulada. Se a unidade fosse centímetros: são 126 ÷ 18 = 7 espelhos. Pela figura 2, x vai do início do primeiro degrau até o último espelho, o que corresponde a 6 pisos: 6 · 28 = 168 cm, a alternativa C.</p><p>Contar 7 pisos daria 196 cm, que não está nas alternativas. E as demais opções não saem da conta.</p>"},
35: {"materia": "Física", "assunto": "Cinemática", "tags": ["velocidade média"],
     "enunciado": p(*T(15, "A linha 1 (Azul) do metrô de São Paulo", "é, mais próxima de", ["Se um passageiro entra"])),
     "alternativas": alts("20.", "30.", "40.", "50.", "60."),
     "explicacao": "<p>21 000 m = 21 km em 45 min = 0,75 h: v = 21 ÷ 0,75 = 28 km/h, mais próximo de <strong>30</strong>. Alternativa <strong>B</strong>.</p><p>Usar 45 min como se fosse 1 h dá 21 km/h, perto de A. E as demais vêm de erros de conversão.</p>"},
36: {"materia": "Física", "assunto": "Termologia", "tags": ["calor específico", "potência elétrica"],
     "enunciado": p(*T(15, "Em uma aula de laboratório de calorimetria", "em J/kg·K, foi de", ["Considerando que o forno"])) + apoio("Lembre que:<br>Q = m · c · ∆θ"),
     "alternativas": alts("4,2 × 10<sup>3</sup>", "8,4 × 10<sup>2</sup>", "6,0 × 10<sup>2</sup>", "4,9 × 10<sup>2</sup>", "1,5 × 10<sup>2</sup>"),
     "explicacao": "<p>A potência do forno é P = U · i = 220 · 10 = 2 200 W. Em 60 s: Q = 2 200 · 60 = 132 000 J. Então c = Q ÷ (m · ∆θ) = 132 000 ÷ (1 · 220) = <strong>600 J/kg·K</strong> (uma variação de 220 °C equivale a 220 K). Alternativa <strong>C</strong>.</p><p>4,2 × 10³ é o calor específico da água (A). E os outros valores vêm de usar o tempo em minutos ou de errar a potência.</p>"},
37: {"materia": "Física", "assunto": "Óptica", "tags": ["reflexão total", "fibra óptica"],
     "enunciado": p("Um professor do curso de Materiais da Fatec apresentou aos alunos a seguinte citação:")
                  + apoio(T(15, "“As fibras ópticas podem ser usadas", "mesmo que ela esteja curva”.")[0])
                  + fonte("KIRK, Tim. <em>Physics for the IB Diploma</em>. Oxford University Press, 2003. Livre tradução.")
                  + p("Em seguida, pediu para que os alunos respondessem, de maneira assertiva, à qual conceito físico a citação se refere.", "A resposta correta esperada pelo professor é"),
     "alternativas": alts("difração.", "polarização.", "ângulo limite.", "espalhamento.", "dispersão luminosa."),
     "explicacao": "<p>A fibra óptica funciona por reflexão total: quando o ângulo de incidência é maior que o <strong>ângulo limite</strong> (ou crítico), a luz não sai da fibra e é totalmente refletida. Alternativa <strong>C</strong>.</p><p>Difração é a luz contornando obstáculos (A), polarização é a orientação da vibração da onda (B), espalhamento é o desvio por partículas (D), e dispersão é a separação das cores (E).</p>"},
38: {"materia": "Física", "assunto": "Ondas", "tags": ["efeito Doppler"],
     "enunciado": p(*T(16, "Para explicar o efeito Doppler, um professor", "emitidas pela sirene.", ["Na figura ainda"])) + "[[fig:1]]"
                  + p("Considere que as observadoras Betty Rubble e Wilma Flintstone estejam em repouso na posição apresentada na figura.", "Em relação ao som emitido do carro de Fred e Barney, é correto afirmar que"),
     "trocar": [("Filntstone", "Flintstone")],
     "imagens": figs(("q38", "Vista de cima do carro com uma sirene, rodeado por círculos de frentes de onda que não são concêntricos: estão mais juntos à direita, para onde o carro se move, e mais espaçados à esquerda. Betty Rubble está à esquerda, atrás do carro, e Wilma Flintstone à direita, à frente dele.")),
     "explicacao": "<p>O carro vai para a direita, aproximando-se de Wilma: as frentes de onda chegam mais juntas a ela, e Wilma ouve uma <strong>frequência maior</strong> (som mais agudo) que Betty, de quem o carro se afasta. Alternativa <strong>B</strong>.</p><p>Wilma ouve frequência maior, não menor (A), e Betty ouve o som mais grave (D). O efeito Doppler muda a frequência, não a intensidade (C e E).</p>"},
39: {"materia": "Física", "assunto": "Magnetismo", "tags": ["força entre fios paralelos"],
     "explicacao": "<p>Fios paralelos com correntes de <strong>mesmo sentido se atraem</strong>; com sentidos opostos, se repelem. Alternativa <strong>E</strong>.</p><p>Com os fios perpendiculares ao papel, os campos são circulares e ficam no plano do papel, não perpendiculares a ele (A e B). Campos não são “repulsivos” (C). E a força é de atração, não de repulsão (D).</p>"},
40: {"materia": "Geografia", "assunto": "Biomas brasileiros", "tags": ["Pantanal"],
     "enunciado": apoio(*T(17, "Com uma área de cerca de 250 mil km²", "a declividade é quase nula.", ["É caracterizado pela alternância"]))
                  + url("https://tinyurl.com/y23jnyg9", "16.06.2019") + p("Essa descrição caracteriza corretamente o bioma"),
     "explicacao": "<p>Planície alagável na bacia do Alto Paraguai, dividida entre Brasil, Bolívia e Paraguai, com cheias e secas alternadas e altitudes abaixo de 200 m: é o <strong>Pantanal</strong>. Alternativa <strong>E</strong>.</p><p>A Amazônia, o Cerrado, a Caatinga e o Pampa não ficam na bacia do Alto Paraguai nem têm esse regime de cheias (A, B, C e D).</p>"},
41: {"materia": "Geografia", "assunto": "Globalização", "tags": ["commodities"],
     "explicacao": "<p><em>Commodities</em> são produtos primários, padronizados e negociados em grande escala no mercado mundial, como soja, café, minério de ferro e petróleo: produtos de base <strong>agrícola e de extração mineral</strong>. Alternativa <strong>B</strong>.</p><p>Pesca e têxteis não são as principais (A). Produtos industriais e serviços não são <em>commodities</em> nesse sentido (C, D e E).</p>"},
42: {"materia": "Geografia", "assunto": "Fontes de energia", "tags": ["carvão mineral"],
     "explicacao": "<p>O carvão mineral é uma rocha <strong>sedimentar</strong> formada ao longo de milhões de anos a partir de restos de florestas soterradas, sob pressão e calor. Alternativa <strong>E</strong>.</p><p>Não vem do petróleo (A), não é obtido por fissão nuclear nem é limpo (B), e a queima de madeira produz carvão vegetal (C). A origem é orgânica, não inorgânica (D).</p>"},
43: {"materia": "História", "assunto": "Brasil Império", "tags": ["imigração europeia"],
     "explicacao": "<p>No Primeiro Reinado e na Regência, o governo trouxe colonos alemães e depois italianos para o Sul e lhes deu <strong>pequenas propriedades</strong>, para povoar uma região de fronteira e garantir o território. Alternativa <strong>B</strong>.</p><p>O sistema de colonato e os latifúndios de café são de São Paulo, no fim do século XIX (A e C). O Sul não era região de cana (D). E a soja só se expandiu no século XX (E).</p>"},
44: {"materia": "História", "assunto": "História contemporânea", "tags": ["Muro de Berlim", "Guerra Fria"],
     "explicacao": "<p>O Muro de Berlim (1961) separou Berlim Oriental da Ocidental e foi erguido pela Alemanha Oriental para impedir a fuga de sua população para o lado ocidental. Alternativa <strong>D</strong>.</p><p>Os adversários da Guerra Fria eram EUA e URSS (A). A Europa do Leste era aliada da URSS, e a do Oeste, dos EUA (B). O objetivo não era o contrabando (C). E o nazismo já tinha acabado em 1945 (E).</p>"},
45: {"materia": "Biologia", "assunto": "Genética", "tags": ["heredograma"],
     "enunciado": p("No heredograma, os símbolos preenchidos representam pessoas afetadas por uma doença hereditária. Os homens são representados pelos quadrados e as mulheres, pelos círculos.") + "[[fig:1]]"
                  + p("O padrão de herança observado por essa doença é"),
     "imagens": figs(("q45", "Heredograma em três gerações. Geração I: homem afetado (1) e mulher afetada (2). Geração II, filhos do casal: mulher normal (2), casada com homem normal (1); homem afetado (3); mulher afetada (4), casada com homem normal (5). Geração III: filho normal (1) do casal II-1 e II-2; duas filhas normais (2 e 3) do casal II-4 e II-5.")),
     "explicacao": "<p>Os pais I-1 e I-2 são afetados e têm uma filha normal (II-2). Se a doença fosse recessiva, pais afetados (aa) só teriam filhos afetados. Logo, ela é dominante e os pais são heterozigotos (Aa). Como a filha de um homem afetado é normal, ela não está no cromossomo X: é <strong>dominante autossômica</strong>. Alternativa <strong>D</strong>.</p><p>Pais afetados com filha normal descartam a herança recessiva (A e B). Há mulheres afetadas, o que descarta o cromossomo Y (C). E, se fosse dominante ligada ao X, a filha II-2 do homem afetado I-1 seria afetada (E).</p>"},
46: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": ["leishmaniose"],
     "enunciado": apoio(*T(19, "A leishmaniose é uma doença não contagiosa", "as populações mais pobres.", ["Existem dois tipos", "A leishmaniose tegumentar", "A leishmaniose visceral", "Atualmente, existem cerca"]))
                  + url("https://tinyurl.com/y3elt26u", "17.06.2019") + p("Em relação a essa doença, é correto que"),
     "explicacao": "<p>A leishmaniose é transmitida pela picada do mosquito-palha. Evitar a proliferação do vetor e usar mosquiteiros e telas impedem a picada e previnem a doença. Alternativa <strong>B</strong>.</p><p>O agente é um protozoário (<em>Leishmania</em>), não vírus nem bactéria (A e C), e a ruptura de células com febre periódica é típica da malária (A). Não se transmite por água ou alimentos (D). E o <em>Trypanosoma</em> causa a doença de Chagas (E).</p>"},
47: {"materia": "Biologia", "assunto": "Fisiologia humana", "tags": ["enzimas"],
     "explicacao": "<p>A papaína quebra proteínas. Como a carne é rica em proteínas, o “leite” do mamão é usado para <strong>amaciar a carne</strong>. Alternativa <strong>E</strong>.</p><p>Acentuar cores, cozinhar macarrão, temperar saladas e fazer bolos não dependem da quebra de proteínas (A, B, C e D).</p>"},
48: {"materia": "Biologia", "assunto": "Fisiologia humana", "tags": ["coração", "circulação"],
     "enunciado": p(T(19, "Quando analisamos as paredes abertas de um coração", "comunicação entre os dois ventrículos.")[0], "A consequência imediata que esse defeito trará para a circulação sanguínea da criança será"),
     "explicacao": "<p>O ventrículo esquerdo recebe sangue arterial (rico em O₂), e o direito, sangue venoso. Uma abertura entre eles <strong>mistura os dois sangues</strong>, e o corpo recebe sangue menos oxigenado. Alternativa <strong>B</strong>.</p><p>O defeito é no coração, não nas vias respiratórias (A e E). O sangue ainda é oxigenado nos pulmões (C). E o coração continua recebendo sangue dos pulmões (D).</p>"},
49: {"materia": "Biologia", "assunto": "Ecologia", "tags": ["cadeia alimentar"],
     "explicacao": "<p>Mais gaviões comem mais passarinhos. Com menos passarinhos, os gafanhotos aumentam e comem mais plantas, que diminuem. Alternativa <strong>B</strong>.</p><p>Os passarinhos comem gafanhotos, consumidores primários, então são consumidores secundários (A). Quem fixa nitrogênio são bactérias, não gafanhotos (C). Menos passarinhos significa <em>mais</em> gafanhotos (D). E os decompositores transformam a matéria orgânica em substâncias minerais, não em carboidratos (E).</p>"},
50: {"materia": "Português", "assunto": "Gêneros textuais", "tags": ["cartum", "ironia"],
     "enunciado": "[[fig:1]]" + url("https://tinyurl.com/ya42xtrr", "20.06.2019", "Original colorido.") + p("Ao analisar o cartum, conclui-se corretamente que"),
     "imagens": figs(("q50", "Cartum com o título “Como era o meu país em 2019” e o subtítulo “Nessa época, a tecnologia aproximava as pessoas.” No primeiro quadro, uma jovem sorridente diz: “Graças ao WhatsApp, eu troco mensagens com a minha mãe o dia inteiro.” No segundo, de braços abertos, completa: “De forma que ela nem reclama que eu estou há sete meses sem visitá-la.”")),
     "explicacao": "<p>O título diz que “a tecnologia aproximava as pessoas”, mas a moça conta que, por conversar com a mãe pelo WhatsApp, está há sete meses sem visitá-la. A ironia está nessa <strong>oposição</strong>: a tecnologia afasta em vez de aproximar. Alternativa <strong>B</strong>.</p><p>O WhatsApp já existia em 2019 (A). A moça não fala com o seu eu do futuro (C). A proximidade é virtual, não real (D). E o cartum não trata de consumo (E).</p>"},
51: {"materia": "Português", "assunto": "Interpretação de texto",
     "enunciado": LAPTOP + P51,
     "alternativas": alts("a empresa criadora do <em>Classmate</em> é pioneira na comercialização de apostilas escolares.", "o <em>Classmate</em> é um computador exclusivo do jornal <em>Valor Econômico</em>.",
                          "o novo laptop foi projetado para ser também um bloco de anotações.", "a principal diferença entre as duas versões do laptop é a duração da bateria.", "o diferencial do <em>Classmate</em> é que o aluno poderá converter livros impressos em digitais."),
     "explicacao": "<p>O texto diz que o aluno “pode também fazer anotações usando uma caneta acoplada ao computador”: o laptop funciona também como bloco de anotações. Alternativa <strong>C</strong>.</p><p>A empresa fabrica computadores, não apostilas (A). O jornal só teve acesso exclusivo ao protótipo (B). A principal novidade é a conversão em suporte de livros digitais, não a bateria (D). E o equipamento vira suporte de livros digitais, não converte livros impressos (E).</p>"},
52: {"materia": "Português", "assunto": "Coesão e referência", "tags": ["pronome relativo"],
     "enunciado": p("No trecho “O jornal <em>Valor Econômico</em> teve acesso com exclusividade ao equipamento, <u>que</u> começará a chegar ao mercado no segundo trimestre de 2010”, a palavra grifada refere-se à seguinte informação:"), "apoio_de": (51, P51),
     "alternativas": alts("mercado", "equipamento", "segundo trimestre", "jornal <em>Valor Econômico</em>", "acesso com exclusividade"),
     "explicacao": "<p>O pronome relativo “que” retoma o termo que vem logo antes, “equipamento”: é o equipamento que começará a chegar ao mercado. Alternativa <strong>B</strong>.</p><p>“Mercado” e “segundo trimestre” vêm depois do pronome (A e C). Nem o jornal nem o acesso chegarão ao mercado (D e E).</p>"},
53: {"materia": "Português", "assunto": "Semântica", "tags": ["aspas", "conotação"],
     "enunciado": p("Observe o trecho:") + apoio("O aluno pode girar a tela e, com a ponta do dedo, “folhear” as páginas do livro...")
                  + p("A intenção do autor, ao destacar a palavra “folhear” com aspas, é"), "apoio_de": (51, P51),
     "alternativas": alts("gerar o sentido de ação repetitiva.", "impor um sentido pejorativo.", "indicar o erro gráfico.", "sinalizar o sentido conotativo.", "assinalar seu valor onomatopaico."),
     "explicacao": "<p>Numa tela não há folhas de papel: o aluno “folheia” em sentido figurado, deslizando o dedo. As aspas marcam esse <strong>sentido conotativo</strong>. Alternativa <strong>D</strong>.</p><p>As aspas não indicam repetição (A), crítica (B), erro (C) nem imitação de som (E).</p>"},
54: {"materia": "Português", "assunto": "Interpretação de texto",
     "enunciado": p("Assinale a alternativa em que o trecho do último parágrafo do texto esteja corretamente interpretado."), "apoio_de": (51, P51),
     "alternativas": alts("“Enquanto olha para licitações públicas...” equivale a: ao mesmo tempo em que a empresa americana faz suas compras no setor público.",
                          "“Enquanto olha para licitações públicas, a empresa também corre para fechar acordo com fabricantes...” equivale a: a empresa americana tem vendido o <em>Classmate</em> ao governo e “por isso” quer buscar novas fábricas para aumentar a produção.",
                          "“...a empresa também corre para fechar acordo...” equivale a: a empresa americana planeja encerrar alguns contratos, por não mais possuir produtos disponíveis para venda.",
                          "“...que deverão colocar os novos laptops da empresa...” equivale a: o governo deverá adquirir os computadores portáteis da empresa.",
                          "“...colocar os novos laptops da empresa nas prateleiras...” equivale a: colocar à venda os computadores portáteis fabricados pela referida empresa."),
     "explicacao": "<p>“Colocar nas prateleiras” significa pôr os laptops <strong>à venda</strong> nas lojas. Alternativa <strong>E</strong>.</p><p>Nas licitações, a empresa quer vender ao setor público, não comprar dele (A), e o texto não diz que ela já vende ao governo (B). “Fechar acordo” é firmar contrato, não encerrar (C). E quem colocará os laptops à venda são os fabricantes e as redes varejistas, não o governo (D).</p>"},
}
completar(Q, R)
