# Ajustes da conferência humana: Vestibular FATEC 1º semestre de 2019 (exame de 09/12/2018)
# Texto conferido com a imagem de cada página. Tema implícito: Trabalho (redação: o papel da escola na formação do jovem para o mercado de trabalho do século XXI).
# 54 questões; a prova tem 5 h no total, incluindo a redação (que fica fora do simulado).
# Matéria: a do gabarito oficial; nas "Multidisciplinar", a matéria principal + tag "multidisciplinar".
# Rascunho com colunas embaralhadas: enunciados e alternativas escritos aqui.
# Gabarito: oficial (1º SEM/19); Q30 ANULADA sem motivo publicado (análise: o valor correto, R$ 864,00, não está nas alternativas).
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import A, carregar, enun, tabela, colunas, completar, trecho

ID = "fatec-2019-1sem"
META = {
    "id": ID,
    "banca": "FATEC",
    "ano": 2019,
    "semestre": 1,
    "titulo": "Vestibular FATEC, 1º semestre de 2019",
    "fonte": "Centro Paula Souza",
    "dataExame": "2018-12-09",
    "duracaoMinutos": 300,
    "tema": "Trabalho",
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

# ---------- textos compartilhados ----------
FOSFINA = (chamada("Leia o texto para responder às questões de números 20 e 21.")
           + apoio(*[x.replace("(A P)", "(AℓP)").replace("PH3", "PH<sub>3</sub>").replace("P2O5", "P<sub>2</sub>O<sub>5</sub>") for x in T(10, "Um incêndio atingiu uma fábrica", "formação de ácido fosfórico.")])
           + url("https://tinyurl.com/yafzufbo", "11.10.18"))
P20 = (p("A reação química da produção da fosfina pode ser representada pela equação")
       + apoio("AℓP (s) + 3 H<sub>2</sub>O (ℓ) → Aℓ(OH)<sub>3</sub> (s) + PH<sub>3</sub> (g)")
       + p("Considerando que toda a massa de fosfeto de alumínio reagiu com a água e que o rendimento da reação é 100%, o volume aproximado de fosfina produzido no local, em litros, é")
       + apoio("Dados:<br>Volume molar dos gases nas condições descritas: 30 L/mol<br>Massas molares em g/mol: Aℓ = 27, P = 31"))

SKILLS = (chamada("Leia o texto para responder às questões de números 25 a 29.")
          + apoio("<strong>The Skills You Need To Succeed In 2020</strong>", "By Avil Beckford – Aug 6, 2018.",
                  *T(11, "The World Economic Forum reports that you need", "you want to focus on", ["The ten skills on this list"])[:-1],
                  T(11, "The World Economic Forum reports that you need", "you want to focus on", ["The ten skills on this list"])[-1] + " " +
                  T(11, "creative work, because", "keep on top of it.", [])[0].split(" You might have started")[0],
                  *T(11, "You might have started", "keep on top of it.", ["In some instances", "In terms of work", "Learning how to learn.", "Analyzing information.", "Spotting patterns", "Communicating – written", "Understanding and leveraging"]))
          + url("https://tinyurl.com/y7pahnqf", "15.10.2018"))
SKILLS = SKILLS.replace("fo r the age", "for the age")
for t in ("Learning how to learn.", "Analyzing information.", "Spotting patterns and trends.", "Communicating – written and oral.", "Understanding and leveraging technology."):
    SKILLS = SKILLS.replace(t, f"<strong>{t}</strong>", 1)
P25 = p("Na frase, <em>The World Economic Forum reports that you need ten skills to thrive in 2020…</em>, presente no primeiro parágrafo do texto, a palavra <em>thrive</em> pode ser substituída por")

NAVIO = (chamada("Leia a notícia, divulgada em maio 2017, para responder às questões de números 35 a 36.")
         + apoio("Para todos os exercícios, considere situações ideais e g = 10 m/s<sup>2</sup>")
         + apoio("<strong>Navio autônomo e elétrico</strong>",
                 *T(14, "O primeiro navio autônomo", "mas deverá", ["O navio elétrico e autônomo"])[:-1],
                 T(14, "O primeiro navio autônomo", "mas deverá", ["O navio elétrico e autônomo"])[-1] + " " + T(14, "operar em velocidade de cruzeiro", "(6 nós).")[0],
                 *[it(x, "Radio Detection And Ranging", "Light Detection And Ranging", "Automatic Identification System") for x in T(14, "Ele será impulsionado", "tráfego de embarcações.", ["A navegação autônoma"])])
         + url("https://tinyurl.com/yapk5b5f", "10.10.2018")
         + fonte("¹Calado – distância vertical entre a superfície da água e a parte mais baixa do navio naquele ponto."))
NAVIO = NAVIO.replace("calado¹", "calado<sup>1</sup>")
P35 = p("Desconsiderando as acelerações de saída e de chegada do navio nos portos de Brevik e Larvik, é correto afirmar que")

FRANGO = (chamada("Leia o texto para responder às questões de números 46 e 47.")
          + apoio(" ".join(T(17, "Entre os diferentes sistemas pecuários", "frangos de corte.")))
          + fonte("TALLENTIRE, C. W.; LEINOREN, I; KYRIAZAKIS, I. Artificial selection for improved energy efficiency is reaching its limits in broiler chickens. <strong>Scientific Reports</strong>, v. 8, n. 1168, p. 1, 2018. Adaptado."))
P46 = p("Assinale a alternativa em que a relação entre a consequência ambiental e a técnica descritas no texto é feita corretamente.")

GRANDIN = (chamada("Leia o texto para responder às questões de números 50 a 53.")
           + apoio(*T(19, "Temple Grandin empacou diante da porteira.", "Universidade Estadual Paulista.", ["Grandin tem um parafuso", "Em julho passado", "A engenheira agrônoma", "[...]", "No auditório"]))
           + fonte("Monica Manin &lt;https://tinyurl.com/y8xeoqul&gt; Acesso em: 12.10.2018. Adaptado."))
P50 = p("Observe os elementos destacados na passagem: <em>“Sempre passo no curral antes do manejo, observo tudo, dizem <strong>que</strong> tenho olho biônico, e ela notou uma coisa <strong>que</strong> eu não tinha visto”</em>, presente no primeiro parágrafo.", "As palavras destacadas exercem")

Q = {
1: {"materia": "Matemática", "assunto": "Porcentagem", "tags": MULTI + ["trabalho voluntário"],
    "enunciado": apoio(" ".join(T(2, "O Instituto Brasileiro de Geografia", "na faixa etária citada.")))
                 + url("https://tinyurl.com/yc9myhl9", "04/10/2018")
                 + p("Considere que, em 2016, havia N milhões de brasileiros com 14 anos ou mais que realizaram algum tipo de trabalho.", "De acordo com o texto, é correto afirmar que o valor de N é"),
    "alternativas": alts("3,9.", "10,4.", "16,7.", "25,4.", "166,7."),
    "explicacao": "<p>Os 6,5 milhões de voluntários correspondem a 3,9% do total: N = 6,5 ÷ 0,039 ≈ <strong>166,7</strong> milhões. Alternativa <strong>E</strong>.</p><p>3,9 é a própria porcentagem (A). E 16,7 erra a casa decimal (C).</p>"},
2: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": MULTI + ["charge", "liderança"],
    "enunciado": p("Analise a charge.") + "[[fig:1]]" + url("https://tinyurl.com/yd6axzjp", "15.10.2018", "")
                 + p("As expressões <em>I’m not lacking leadership</em> e <em>Everyone else is lacking</em>, para expressar o sarcasmo da charge, demonstram que o profissional em questão"),
    "imagens": figs(("q02", "Cartum de Randy Glasbergen: um executivo de gravata, ao telefone, segurando um papel, diz: “I’m not lacking leadership skills. Everyone else is lacking followship skills!” (não me falta habilidade de liderança; é a todos os outros que falta habilidade de ser liderado!).")),
    "alternativas": alts("acredita ser um bom líder.", "sente falta de seus funcionários.", "se importa com seus funcionários.", "tem dificuldade de ser comandado.", "ignora a habilidade de liderança de seus funcionários."),
    "explicacao": "<p>O chefe diz que não lhe falta liderança; o problema seria dos outros, que não sabem ser liderados. Ele <strong>se considera um bom líder</strong> e culpa a equipe. Alternativa <strong>A</strong>.</p><p><em>Lacking</em> é “faltar”, não “sentir falta” (B). Ele não demonstra cuidado com os funcionários (C), não fala de ser comandado (D) nem da liderança deles (E).</p>"},
3: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": MULTI + ["doença ocupacional"],
    "enunciado": apoio("Segundo a Lei de Benefícios da Previdência Social, sancionada em 1991, um trabalhador poderá ser assegurado caso padeça de doença profissional, cuja definição, dada no Art. 20, inclui os seguintes aspectos:",
                       "• Doença profissional é aquela produzida ou desencadeada pelo exercício do trabalho peculiar a determinada atividade;<br>• Doenças profissionais não incluem as degenerativas, as inerentes a grupo etário, as que não produzam incapacidade laborativa, nem as endêmicas não resultantes de atividades profissionais.")
                 + p("Considerando apenas os termos dispostos no artigo 20 dessa lei, um programador de softwares em Goiás poderá receber amparo legal caso sofra de"),
    "alternativas": alts("pé-de-atleta.", "mal de Chagas.", "tendinite crônica.", "mal de Alzheimer.", "anemia falciforme."),
    "explicacao": "<p>O uso repetitivo do teclado e do mouse pode causar <strong>tendinite</strong>, uma lesão desencadeada pelo próprio trabalho do programador. Alternativa <strong>C</strong>.</p><p>Pé-de-atleta é uma micose que não tem relação com a atividade (A). O mal de Chagas é endêmico e não resulta do trabalho (B). O Alzheimer é degenerativo (D). E a anemia falciforme é genética (E).</p>"},
4: {"materia": "Química", "assunto": "Isomeria", "tags": MULTI + ["fórmula molecular"],
    "enunciado": apoio("• O estresse está se tornando um problema cada vez maior no mundo do trabalho. Situações e estímulos do ambiente de trabalho que pressionam o trabalhador, em diferentes contextos, provocam a produção de diversos hormônios em seu organismo como, por exemplo, o cortisol. O cortisol é responsável pela regulação de diversos processos metabólicos humanos. Sua forma sintética, a hidrocortisona, é usada no combate a inflamações e alergias.")
                 + "[[fig:1]]" + url("https://tinyurl.com/yd2f7wpt", "11.10.18")
                 + apoio("• Em química, isomeria é um fenômeno que ocorre quando duas ou mais moléculas apresentam a mesma fórmula molecular.")
                 + p("Observando as fórmulas estruturais do cortisol e da hidrocortisona, pode-se concluir corretamente que estes compostos"),
    "imagens": figs(("q04", "Fórmulas estruturais em linhas de dois esteroides, cada um com quatro anéis fundidos e uma cadeia lateral –C(=O)–CH₂OH com um OH no mesmo carbono. Cortisol: uma carbonila (C=O) no primeiro anel, uma dupla ligação C=C no primeiro anel e um grupo OH no terceiro anel. Hidrocortisona, como desenhada na prova: uma carbonila no primeiro anel, sem a dupla ligação, e uma carbonila no lugar do OH do terceiro anel.")),
    "alternativas": alts("são isômeros de fórmula molecular C<sub>21</sub>H<sub>30</sub>O<sub>5</sub>.", "são isômeros de fórmula molecular C<sub>21</sub>H<sub>29</sub>O<sub>5</sub>.", "são isômeros de fórmula molecular C<sub>21</sub>H<sub>6</sub>O<sub>5</sub>.",
                         "não são isômeros pois suas fórmulas moleculares são diferentes.", "não são isômeros pois suas fórmulas estruturais são diferentes."),
    "explicacao": "<p>Contando os átomos, as duas estruturas têm 21 carbonos, 30 hidrogênios e 5 oxigênios: a dupla ligação e o OH do cortisol equivalem, em número de átomos, à carbonila extra e à ausência da dupla na outra estrutura. Mesma fórmula molecular, estruturas diferentes: são <strong>isômeros</strong>, C<sub>21</sub>H<sub>30</sub>O<sub>5</sub>. Alternativa <strong>A</strong>.</p><p>Uma molécula orgânica neutra com C, H e O tem sempre um número par de hidrogênios, o que já descarta C<sub>21</sub>H<sub>29</sub>O<sub>5</sub> (B), e 6 hidrogênios é pouquíssimo (C). As fórmulas moleculares são iguais (D), e estruturas diferentes são justamente o que define isômeros (E).</p><p>Observação do Treineiros: na química real, cortisol e hidrocortisona são o mesmo composto; a prova desenhou uma estrutura diferente para a hidrocortisona, e a questão deve ser respondida com base no desenho.</p>"},
5: {"materia": "História", "assunto": "Brasil República", "tags": MULTI + ["trabalho infantil", "industrialização"],
    "enunciado": p("Leia o texto.") + apoio(" ".join(T(3, "Assistimos ontem à entrada de cerca de 60 menores", "de 12, 13 e 14 anos.")))
                 + fonte("Jornal <em>O Combate</em>, São Paulo, 4/09/1917. Apud CENPEC; <em>Ensinar e aprender História</em>. V.3: ficha 10, 1998.")
                 + p("Considerando o contexto da industrialização de São Paulo, no início da Primeira República, assinale a alternativa correta."),
    "explicacao": "<p>No início da industrialização, sem leis trabalhistas, os salários dos operários eram tão baixos que mulheres e crianças também precisavam trabalhar, cumprindo jornadas longas e recebendo menos que os homens. Alternativa <strong>D</strong>.</p><p>Nenhuma lei obrigava o trabalho infantil (A). O Brasil não participou da Guerra Franco-Prussiana (B). A CLT é de 1943 e proibiu o trabalho infantil (C). E os anarquistas lutavam contra a exploração de crianças (E).</p>"},
6: {"materia": "Física", "assunto": "Ondas", "tags": MULTI + ["superposição"],
    "enunciado": p("No curso de “Big Data no Agronegócio” da FATEC, o aluno estuda sobre eletrônica, circuitos eletrônicos e suas propriedades, tais como ondas que podem ser registradas em um osciloscópio.",
                   "A figura representa duas dessas ondas que se propagam em sentidos opostos e com mesma velocidade de módulo 2 × 10<sup>–6</sup> m/s") + "[[fig:1]]"
                 + p("Considerando a situação apresentada pela figura no instante t = 0, podemos afirmar que, após"),
    "imagens": figs(("q06", "Gráfico de tensão (volt) por posição (×10⁻⁶ m), de 0 a 10. Onda 1 (linha contínua), entre 0 e cerca de 4,4, com amplitude 2 V, propaga-se para a direita (V₁). Onda 2 (tracejada), entre cerca de 5,6 e 10, com amplitude 1 V, propaga-se para a esquerda (V₂). Uma chave sob o gráfico indica que o trecho de 0 a 2 corresponde a 1 s.")),
    "alternativas": alts("1 segundo, a superposição das ondas 1 e 2 apresenta uma nova onda com amplitude de 1 volt.", "1 segundo, ocorre uma interferência destrutiva total.", "o cruzamento das ondas, a onda 2 é completamente amortecida.",
                         "o cruzamento das ondas, a amplitude da onda 2 fica maior que a da onda 1.", "o cruzamento das ondas, a frequência da onda 1 fica maior que a da onda 2."),
    "explicacao": "<p>Em 1 s, cada onda anda 2 × 10⁻⁶ m e elas passam a se sobrepor. Onde uma crista de 2 V da onda 1 encontra um vale de –1 V da onda 2, a superposição dá 2 – 1 = <strong>1 V</strong>. Alternativa <strong>A</strong>.</p><p>Como as amplitudes são diferentes (2 V e 1 V), a interferência destrutiva nunca é total (B). E, depois do cruzamento, cada onda segue com sua amplitude e sua frequência originais, sem se alterar (C, D e E).</p>"},
7: {"materia": "Português", "assunto": "Interpretação de texto", "tags": MULTI + ["quadrinhos", "tecnologia"],
    "enunciado": p("Analise o quadrinho") + "[[fig:1]]" + url("https://tinyurl.com/ycovkfc9", "20.10.2018", "Original colorido.")
                 + p("O quadrinho de Laerte representa uma crítica à realidade atual, visto que nele a personagem"),
    "imagens": figs(("q07", "Quadrinho de Laerte, em quatro cenas, sem falas, sobre a rotina de uma pessoa cuja cabeça é sempre substituída por um objeto: um rádio-relógio, ao acordar na cama; uma torneira, ao escovar os dentes; um bule de café, ao tomar café lendo o jornal; um semáforo de pedestres, ao andar na rua.")),
    "explicacao": "<p>A cada momento do dia, a cabeça da personagem vira o objeto que comanda aquela tarefa (despertador, torneira, bule, semáforo). Ela perde a identidade e vive no automático, presa a uma <strong>rotina maçante e repetitiva</strong>. Alternativa <strong>B</strong>.</p><p>A personagem não perde a função social nem fica obsoleta (A), não é substituída por máquinas (C), não há referência ao campo (D), e não há atividades coletivas (E).</p>"},
8: {"materia": "Matemática", "assunto": "Equações", "tags": MULTI + ["problema de Diofanto"],
    "enunciado": p("Entre as tarefas de um professor, está a elaboração de exercícios. Professores de Matemática ainda hoje se inspiram em Diofanto, matemático grego do século III, para criar desafios para seus alunos. Um exemplo de problema diofantino é: “Para o nascimento do primeiro filho, o pai esperou um sexto de sua vida; para o nascimento do segundo, a espera foi de um terço de sua vida. Quando o pai morreu, a soma das idades do pai e dos dois filhos era de 240 anos. Com quantos anos o pai morreu?”",
                   "Considerando que, quando o pai morreu, ele tinha x anos, assinale a equação matemática que permite resolver esse problema."),
    "alternativas": alts("\\(x + \\dfrac{5x}{6} + \\dfrac{2x}{3} = 240\\)", "\\(x + \\dfrac{x}{6} + \\dfrac{x}{3} = 240\\)", "\\(x + \\dfrac{4x}{5} + \\dfrac{3x}{4} = 240\\)", "\\(x + \\dfrac{x}{6} + \\dfrac{3x}{2} = 240\\)", "\\(x + \\dfrac{6x}{5} + \\dfrac{3x}{4} = 240\\)"),
    "explicacao": "<p>O primeiro filho nasceu quando o pai tinha x/6 anos; na morte do pai, tinha x − x/6 = 5x/6. O segundo nasceu com o pai aos x/3; tinha x − x/3 = 2x/3. A soma é \\(x + \\dfrac{5x}{6} + \\dfrac{2x}{3} = 240\\). Alternativa <strong>A</strong>.</p><p>B usa as idades do pai nos nascimentos, não as dos filhos. As demais frações não saem do enunciado.</p>"},
9: {"materia": "Geografia", "assunto": "População", "tags": MULTI + ["desalento", "desemprego"],
    "enunciado": p("Leia os textos.") + apoio("• " + " ".join(T(5, "Francisco tem pouca esperança no futuro.", "brasileiros: os desalentados.")),
                                              "• Um indicador fundamental para observar o nível da confiança do trabalhador no mercado de trabalho é a taxa de desalento.",
                                              "• " + " ".join(T(5, "O Brasil iniciou o terceiro trimestre", "trimestre maio – julho.")))
                 + url("https://tinyurl.com/yactn5rh", "03.10.2018") + p("De acordo com os textos, o cidadão desalentado é aquele que"),
    "explicacao": "<p>Francisco “decidiu parar de procurar” emprego depois de várias tentativas: o desalentado quer e precisa trabalhar, mas <strong>desiste de procurar</strong> por achar que não vai encontrar vaga. Por isso não entra na taxa de desemprego. Alternativa <strong>B</strong>.</p><p>O desalentado não tem emprego, formal ou não (A, D e E), nem troca de trabalho por vontade própria (C).</p>"},
10: {"materia": "Raciocínio lógico", "assunto": "Razão e proporção", "tags": ["regra de três"],
     "enunciado": p(*T(6, "Um grupo de alunos do curso de Jogos Digitais", "o tempo total de produção do jogo.", ["Assinale a alternativa"])),
     "alternativas": alts("9 h 30 min", "9 h 50 min", "12 h 30 min", "15 h 30 min", "15 h 50 min"),
     "explicacao": "<p>O grupo faz 24% em 6 h, ou 4% por hora. Com a equipe dobrada, passa a 8% por hora. Faltam 76%: 76 ÷ 8 = 9,5 h. O total é 6 + 9,5 = 15,5 h = <strong>15 h 30 min</strong>. Alternativa <strong>D</strong>.</p><p>9 h 30 min é só o tempo da segunda etapa (A). E 0,5 h são 30 min, não 50 (B e E).</p>"},
11: {"materia": "Raciocínio lógico", "assunto": "Lógica", "tags": ["negação"],
     "enunciado": p("São proposições equivalentes para a negação da proposição “todo homem ama lógica”:", "• “pelo menos um homem não ama lógica”;<br>• “algum homem não ama lógica”;<br>• “existe um homem que não ama lógica”.",
                    "Assim, a forma correta de negar a proposição “todas as vagas deste vestibular são de ensino superior” é"),
     "alternativas": alts("“algumas vagas deste vestibular são de ensino superior”.", "“existem vagas deste vestibular que não são de ensino superior”.", "“nenhuma das vagas deste vestibular é de ensino superior”.",
                          "“pelo menos uma vaga deste vestibular é de ensino superior”.", "“todas as vagas deste vestibular não são de ensino superior”."),
     "explicacao": "<p>A negação de “todas são” é “pelo menos uma não é”: <strong>existem vagas que não são de ensino superior</strong>. Alternativa <strong>B</strong>.</p><p>A e D não negam nada; são até compatíveis com a frase original. C e E exageram: dizem que nenhuma vaga é de ensino superior, o que é mais forte que a negação.</p>"},
12: {"materia": "Raciocínio lógico", "assunto": "Lógica", "tags": ["diagramas de Venn"],
     "enunciado": p(*T(6, "Entre as pessoas que compareceram à festa", "à festa de inauguração.", ["Além disso"]), "Considere:")
                  + apoio("<strong>F</strong>: conjunto das pessoas que foram à festa de inauguração.<br><strong>E</strong>: conjunto dos amigos de Eduardo.<br><strong>M</strong>: conjunto dos melhores amigos de Eduardo.")
                  + p("Com base nessas informações assinale a alternativa que contém o diagrama de Euler-Venn que descreve corretamente a relação entre os conjuntos."),
     "imagens": figs(("q12a", "Diagrama A: E e F, separados, dentro de M."), ("q12b", "Diagrama B: E e M, separados, dentro de F."), ("q12c", "Diagrama C: E e F se cruzam, e M está dentro da interseção de E e F."),
                     ("q12d", "Diagrama D: F dentro de E, e E cruza M."), ("q12e", "Diagrama E: F e E se cruzam, e M está dentro de E, com uma parte dentro de F e outra fora.")),
     "alternativas": {"A": "[[fig:1]]", "B": "[[fig:2]]", "C": "[[fig:3]]", "D": "[[fig:4]]", "E": "[[fig:5]]"},
     "explicacao": "<p>Todo melhor amigo é amigo, então M está dentro de E. Alguns amigos foram à festa: E e F se cruzam. E nem todos os melhores amigos foram: M tem uma parte fora de F. O diagrama E mostra exatamente isso. Alternativa <strong>E</strong>.</p><p>Em A, E e F não se cruzam, ou seja, nenhum amigo teria ido à festa. Em B, todos os melhores amigos foram à festa. Em C, M está inteiro em F. Em D, M não está dentro de E.</p>"},
13: {"materia": "Raciocínio lógico", "assunto": "Geometria plana", "tags": ["semelhança", "papel A4"],
     "enunciado": p(*T(7, "Um formato de papel usado para impress", "pode-se afirmar que", ["Essa série criou", "Considerando uma folha"])) + "[[fig:1]]",
     "trocar": [("impressõ es", "impressões"), ("fotocó pias", "fotocópias")],
     "imagens": figs(("q13", "Retângulo de lados x (horizontal, o maior) e y (vertical), com uma linha tracejada vertical no meio, marcada como “Dobra”.")),
     "alternativas": alts("\\(x = 2y\\)", "\\(x = y\\sqrt{2}\\)", "\\(x = y\\)", "\\(y = x\\sqrt{2}\\)", "\\(y = 2x\\)"),
     "explicacao": "<p>Dobrado ao meio, o retângulo x × y vira y × x/2. Para os dois serem semelhantes, \\(\\dfrac{x}{y} = \\dfrac{y}{x/2}\\), ou seja, x² = 2y² e \\(x = y\\sqrt{2}\\). Alternativa <strong>B</strong>.</p><p>Com x = 2y, a metade seria um quadrado (A). x = y já é um quadrado (C). E D e E fariam y maior que x, contra a figura.</p>"},
14: {"materia": "Raciocínio lógico", "assunto": "Sequências", "tags": ["sistemas de numeração", "criptografia"],
     "enunciado": p(*T(7, "A criptografia pode ser descrita", "corresponder a um número.", ["Considere que uma empresa"]))
                  + "".join(tabela([chr(65 + i) for i in range(k, min(k + 7, 26))], [[str(i) for i in range(k, min(k + 7, 26))]]) for k in range(0, 26, 7))
                  + p("Assim, qualquer informação numérica é traduzida como “palavras”. Com elas é possível realizar operações de modo semelhante ao que se faz no sistema posicional de base 10. No exemplo DIA + SOL, temos:")
                  + tabela(["", "1ª letra", "2ª letra", "3ª letra"], [["DIA", "D = 3", "I = 8", "A = 0"], ["+ SOL", "S = 18", "O = 14", "L = 11"], ["= VWL", "V = 21", "W = 22", "L = 11"]])
                  + p("Assinale a alternativa que apresenta, nesse sistema, o valor correto da soma QUERO + FATEC."),
     "alternativas": alts("VUXVQ", "VUVYQ", "VVXVR", "UVYZR", "UVYZQ"),
     "explicacao": "<p>QUERO = 16, 20, 4, 17, 14 e FATEC = 5, 0, 19, 4, 2. Somando da direita para a esquerda: O + C = 16 (Q); R + E = 21 (V); E + T = 23 (X); U + A = 20 (U); Q + F = 21 (V). Nenhuma soma passa de 25, então não há “vai um”. Resultado: <strong>VUXVQ</strong>. Alternativa <strong>A</strong>.</p><p>As outras alternativas erram pelo menos uma das letras.</p>"},
15: {"materia": "História", "assunto": "Pré-História", "tags": ["Luzia", "povoamento da América"],
     "enunciado": p(*[it(x, "Santanaraptor placidus") for x in T(8, "No dia 2 de setembro de 2018", "estudo da pré-história brasileira, pois", ["Em 19 de outubro", "O crânio é considerado"])]),
     "explicacao": "<p>Luzia, com cerca de 11 mil anos, é um dos fósseis humanos mais antigos da América e é usada nas pesquisas sobre <strong>quem foram os primeiros povoadores do continente</strong> e de onde vieram. Alternativa <strong>B</strong>.</p><p>O crânio não indica dieta exclusivamente herbívora (A). Seres humanos nunca conviveram com dinossauros não avianos (C). A América foi povoada há dezenas de milhares de anos, não milhões (D). E não há conclusão sobre expectativa de vida maior (E).</p>"},
16: {"materia": "História", "assunto": "Antiguidade", "tags": ["helenismo"],
     "enunciado": p("A figura mostra uma tapeçaria funerária produzida no Egito, durante o chamado Período Helenístico, retratatando um homem vestido como grego, posicionado entre dois deuses egípcios, Osíris e Anúbis.") + "[[fig:1]]"
                  + fonte("Tapeçaria funerária, linho, 1,75m x 1,25m. Sacara, Egito, séc. I a.C. Aegyptisches Museum, Berlim. Apud DOMINGUES, Joelza Esther. <em>História em Documento. Imagem e texto</em>. 6. 2ªed. São Paulo: FTD, 2013. Original colorido.")
                  + p("Assinale a alternativa que explica, corretamente, a fusão das culturas grega e egípcia representada na tapeçaria."),
     "imagens": figs(("q16", "Tapeçaria funerária egípcia: no centro, um homem jovem com túnica grega; à esquerda, o deus Osíris, com coroa alta; à direita, o deus Anúbis, com cabeça de chacal, pousa a mão no ombro do homem.")),
     "explicacao": "<p>As conquistas de <strong>Alexandre, o Grande</strong>, no século IV a.C., levaram a cultura grega ao Egito, à Ásia e a outras regiões, e a mistura com as culturas locais formou a cultura helenística. Alternativa <strong>C</strong>.</p><p>Cleópatra não invadiu a Grécia (A e E), e Alexandre não se casou com ela, que viveu três séculos depois (E). Menés unificou o Egito por volta de 3100 a.C., muito antes de Aristóteles (B). E visigodos, ostrogodos e vikings são muito posteriores e não levaram o helenismo ao Egito (D).</p>"},
17: {"materia": "História", "assunto": "Grandes Navegações", "tags": ["circum-navegação"],
     "enunciado": p("Em 1519, os navegadores Fernão de Magalhães e Sebastião del Cano partiram de Cádiz, na Espanha, para uma viagem que entraria para a história por"),
     "alternativas": alts("estabelecer um caminho terrestre para as Índias ocidentais.", "descobrir uma rota segura para atravessar o Polo Norte.", "comprovar o formato esférico do planeta Terra.", "desbravar o canal do Panamá.", "explorar o istmo de Suez."),
     "explicacao": "<p>A expedição foi a primeira a dar a volta ao mundo (1519–1522): partindo para o oeste, voltou à Espanha pelo leste, o que comprovou na prática que a Terra é <strong>esférica</strong>. Alternativa <strong>C</strong>.</p><p>A viagem foi marítima e buscava as Índias orientais (A). Não passou pelo Polo Norte (B). E os canais do Panamá e de Suez só foram abertos nos séculos XIX e XX (D e E).</p>"},
18: {"materia": "História", "assunto": "Revolução Industrial",
     "enunciado": p("Leia o texto.") + apoio(*T(9, "Muitas invenções e descobertas dessa fase", "explosivos [...], entre outros.", ["A indústria química"]))
                  + fonte("DOMINGUES, Joelza Esther. <em>História em Documento. Imagem e texto</em>. 8. 2ªed. São Paulo: FTD, 2013. p.192.")
                  + p("O texto descreve a relação entre ciência e indústria característica da"),
     "alternativas": alts("Revolução Agrícola Brasileira (séc. XVI).", "Revolução Agrícola Europeia (séc. XII–XIII).", "Primeira Revolução Industrial (séc. XVIII).", "Segunda Revolução Industrial (séc. XIX–XX).", "Terceira Revolução Industrial (séc. XXI)."),
     "explicacao": "<p>A união entre pesquisa científica em laboratórios e indústria, com a química produzindo fibras sintéticas, corantes, adubos e explosivos, marca a <strong>Segunda Revolução Industrial</strong>. Alternativa <strong>D</strong>.</p><p>As revoluções agrícolas não envolviam laboratórios (A e B). A Primeira Revolução Industrial foi baseada no vapor e em inventores práticos, mais que na ciência de laboratório (C). E a Terceira começou na segunda metade do século XX (E).</p>"},
19: {"materia": "História", "assunto": "Brasil Colônia", "tags": ["irmandades religiosas", "Minas Gerais"],
     "enunciado": p("Observe a imagem.") + "[[fig:1]]"
                  + fonte("Johann Moritz Rugendas. Festa de Nossa Senhora do Rosário, Patrona dos Negros, c.1835. &lt;https://tinyurl.com/ybj66a52&gt; Acesso em: 20/10/2018. Original colorido.")
                  + p(*T(9, "A imagem retrata a festa em homenagem", "essas associações se caracterizavam pela", ["Na região das Minas Gerais"])),
     "imagens": figs(("q19", "Gravura de Rugendas: uma grande festa ao ar livre, com uma multidão de pessoas negras dançando, tocando instrumentos e carregando estandartes, em frente a casas e a uma igreja, entre palmeiras. Legenda: “Fête de Ste Rosalie, patrone des nègres”.")),
     "explicacao": "<p>Nas Minas do século XVIII, as irmandades organizavam a vida social: construíam igrejas e cemitérios, promoviam festas, ajudavam os necessitados e formavam artífices, ensinando ofícios e artes. Alternativa <strong>A</strong>.</p><p>Estradas, impostos e fiscalização eram da Coroa (B e E). Elas não administravam patrimônio do Vaticano nem escolas de educação básica (C), não faziam leis nem ministravam sacramentos, que eram atribuição dos padres (D), e não regulamentavam o candomblé (E).</p>"},
20: {"materia": "Química", "assunto": "Reações químicas", "tags": ["estequiometria"],
     "enunciado": FOSFINA + P20,
     "alternativas": alts("3,33 × 10<sup>2</sup>.", "3,33 × 10<sup>3</sup>.", "3,33 × 10<sup>6</sup>.", "1,55 × 10<sup>3</sup>.", "1,55 × 10<sup>6</sup>."),
     "explicacao": "<p>A massa molar do AℓP é 27 + 31 = 58 g/mol. Três toneladas = 3 × 10⁶ g, ou 3 × 10⁶ ÷ 58 ≈ 5,17 × 10⁴ mol. Pela equação, 1 mol de AℓP dá 1 mol de PH₃: o volume é 5,17 × 10⁴ · 30 ≈ <strong>1,55 × 10⁶ L</strong>. Alternativa <strong>E</strong>.</p><p>1,55 × 10³ esquece de converter toneladas em gramas (D). Os valores com 3,33 usam a massa molar errada.</p>"},
21: {"materia": "Química", "assunto": "Termoquímica", "tags": ["entalpia"],
     "enunciado": p("Os gráficos 1, 2 e 3 representam a variação da energia em função do caminho da reação para três transformações químicas, sendo R o reagente e P o produto de cada reação.") + "[[fig:1]]"
                  + p("Entre os gráficos 1, 2 e 3, aquele que representa corretamente a reação da fosfina com o oxigênio, descrita no texto, é o"),
     "apoio_de": (20, P20),
     "imagens": figs(("q21", "Três gráficos de entalpia H (kJ) pelo caminho da reação. Gráfico 1: o reagente R está mais alto que o produto P. Gráfico 2: R está mais baixo que P. Gráfico 3: R e P estão na mesma altura, com um pico entre eles.")),
     "alternativas": alts("gráfico 1, pois a reação é endotérmica e apresenta ΔrH<sup>0</sup> &lt; 0.", "gráfico 1, pois a reação é exotérmica e apresenta ΔrH<sup>0</sup> &lt; 0.", "gráfico 2, pois a reação é endotérmica e apresenta ΔrH<sup>0</sup> &gt; 0.",
                          "gráfico 2, pois a reação é exotérmica e apresenta ΔrH<sup>0</sup> &lt; 0.", "gráfico 3, pois a reação é endotérmica e apresenta ΔrH<sup>0</sup> &gt; 0."),
     "explicacao": "<p>O texto diz que a fosfina reage com o oxigênio “liberando calor”: a reação é <strong>exotérmica</strong>, com ΔH &lt; 0, e o produto fica com menos energia que o reagente, como no gráfico 1. Alternativa <strong>B</strong>.</p><p>Reação com ΔH &lt; 0 não é endotérmica (A). O gráfico 2 é de uma reação endotérmica, mas a da fosfina é exotérmica (C e D). E o gráfico 3 mostra ΔH = 0 (E).</p>"},
22: {"materia": "Química", "assunto": "Funções inorgânicas", "tags": ["neutralização", "balanceamento"],
     "enunciado": p("Uma das substâncias que pode neutralizar o ácido fosfórico é o hidróxido de magnésio, Mg(OH)<sub>2</sub>.", "A equação química balanceada que representa a reação de neutralização total que ocorre entre essas substâncias é"),
     "alternativas": alts("H<sub>3</sub>PO<sub>4</sub> (aq) + Mg(OH)<sub>2</sub> (s) → MgPO<sub>4</sub> (s) + H<sub>2</sub>O (ℓ).", "2 H<sub>3</sub>PO<sub>4</sub> (aq) + 3 Mg(OH)<sub>2</sub> (s) → Mg<sub>3</sub>(PO<sub>4</sub>)<sub>2</sub> (s) + 6 H<sub>2</sub>O (ℓ).",
                          "3 H<sub>3</sub>PO<sub>3</sub> (aq) + 2 Mg(OH)<sub>2</sub> (s) → Mg<sub>2</sub>(PO<sub>3</sub>)<sub>3</sub> (s) + 6 H<sub>2</sub>O (ℓ).", "2 H<sub>3</sub>PO<sub>3</sub> (aq) + 3 Mg(OH)<sub>2</sub> (s) → Mg<sub>3</sub>(PO<sub>3</sub>)<sub>2</sub> (s) + 6 H<sub>2</sub>O (ℓ).",
                          "H<sub>3</sub>PO<sub>3</sub> (aq) + Mg(OH)<sub>2</sub> (s) → MgPO<sub>3</sub> (s) + H<sub>2</sub>O (ℓ)."),
     "explicacao": "<p>O ácido fosfórico é H₃PO₄ (3 H⁺) e o hidróxido de magnésio tem 2 OH⁻. Para neutralizar tudo, 2 H₃PO₄ (6 H⁺) reagem com 3 Mg(OH)₂ (6 OH⁻), formando Mg₃(PO₄)₂ (3 Mg²⁺ e 2 PO₄³⁻) e 6 H₂O. Alternativa <strong>B</strong>.</p><p>MgPO₄ não tem cargas equilibradas e a equação A não está balanceada. C, D e E usam H₃PO₃, que é o ácido fosforoso, não o fosfórico.</p>"},
23: {"materia": "Química", "assunto": "Reações químicas", "tags": ["oxirredução"],
     "enunciado": p("A reação que ocorre entre a fosfina e o oxigênio é representada pela equação química") + apoio("2 PH<sub>3</sub> (g) + 4 O<sub>2</sub> (g) → P<sub>2</sub>O<sub>5</sub> (g) + 3 H<sub>2</sub>O (g)")
                  + p("As substâncias que atuam como agente oxidante e agente redutor desse processo são, respectivamente,"),
     "alternativas": alts("O<sub>2</sub> e PH<sub>3</sub>.", "O<sub>2</sub> e H<sub>2</sub>O.", "O<sub>2</sub> e P<sub>2</sub>O<sub>5</sub>.", "PH<sub>3</sub> e H<sub>2</sub>O.", "PH<sub>3</sub> e P<sub>2</sub>O<sub>5</sub>."),
     "explicacao": "<p>O oxigênio passa de 0 para −2: sofre redução e é o <strong>agente oxidante</strong>. O fósforo passa de −3, no PH₃, para +5, no P₂O₅: o PH₃ sofre oxidação e é o <strong>agente redutor</strong>. Alternativa <strong>A</strong>.</p><p>Agentes oxidante e redutor são sempre reagentes, nunca produtos como H₂O e P₂O₅ (B, C, D e E).</p>"},
24: {"materia": "Química", "assunto": "Ácidos e bases", "tags": ["constante de basicidade"],
     "enunciado": p("A amônia (NH<sub>3</sub>), molécula de estrutura semelhante à da fosfina, reage com água produzindo uma solução de caráter básico. A reação que ocorre pode ser representada pela equação química")
                  + apoio("NH<sub>3</sub> (g) + H<sub>2</sub>O (ℓ) ⇌ NH<sub>4</sub><sup>+</sup> (aq) + OH<sup>–</sup> (aq)")
                  + p("Uma solução aquosa de NH<sub>3</sub> apresenta concentração inicial de 0,02 mol/L a 25 °C.", "Nessas condições, o valor da concentração de íons OH<sup>–</sup>, em mol/L, é")
                  + apoio("Dado:<br>Constante de basicidade da amônia a 25 °C: K<sub>b</sub> = 1,8 × 10<sup>–5</sup>"),
     "alternativas": alts("2 × 10<sup>–4</sup>", "3 × 10<sup>–4</sup>", "4 × 10<sup>–4</sup>", "5 × 10<sup>–4</sup>", "6 × 10<sup>–4</sup>"),
     "explicacao": "<p>Como a amônia é uma base fraca, \\(K_b \\approx \\dfrac{[\\text{OH}^-]^2}{[\\text{NH}_3]}\\): [OH⁻]² = 1,8 × 10⁻⁵ · 0,02 = 3,6 × 10⁻⁷, e [OH⁻] = <strong>6 × 10⁻⁴ mol/L</strong>. Alternativa <strong>E</strong>.</p><p>Os outros valores vêm de errar a raiz ou a multiplicação.</p>"},
25: {"materia": "Inglês", "assunto": "Vocabulário",
     "enunciado": SKILLS + P25,
     "alternativas": alts("<em>fail</em>", "<em>languish</em>", "<em>prosper</em>", "<em>retreat</em>", "<em>retrogress</em>"),
     "explicacao": "<p><em>Thrive</em> significa “prosperar”, “ter sucesso”: o sinônimo é <strong><em>prosper</em></strong>. Alternativa <strong>C</strong>.</p><p><em>Fail</em> (fracassar), <em>languish</em> (definhar), <em>retreat</em> (recuar) e <em>retrogress</em> (retroceder) têm sentidos opostos (A, B, D e E).</p>"},
26: {"materia": "Inglês", "assunto": "Interpretação de texto",
     "enunciado": p("De acordo com o texto, dentre as dez habilidades apontadas como necessárias para os profissionais prosperarem em 2020, a habilidade que apresenta maior probabilidade para que uma pessoa se mantenha empregada é"),
     "apoio_de": (25, P25),
     "alternativas": alts("o trabalho criativo.", "a gestão de pessoas.", "o pensamento crítico.", "a inteligência emocional.", "a resolução de problemas complexos."),
     "explicacao": "<p>O texto diz: “<em>you want to focus on creative work, because that is where you are likely to remain employable</em>” (concentre-se no trabalho criativo, porque é nele que você provavelmente continuará empregável). Alternativa <strong>A</strong>.</p><p>As outras habilidades estão na lista, mas o texto não as destaca para manter o emprego (B, C, D e E).</p>"},
27: {"materia": "Inglês", "assunto": "Interpretação de texto",
     "enunciado": p("Na oração <em>The illiterate of the 21st century will not be those who cannot read and write, but those who cannot learn, unlearn, and relearn</em>, presente no terceiro parágrafo do texto, Toffler afirma que, no século 21, serão consideradas letradas as pessoas que souberem"),
     "apoio_de": (25, P25),
     "alternativas": alts("ler, reescrever e aprender.", "ler, escrever e desaprender.", "reaprender, reler e reescrever.", "escrever, desaprender e reaprender.", "aprender, desaprender e reaprender."),
     "explicacao": "<p>Para Toffler, os analfabetos do século XXI serão os que não sabem <em>learn, unlearn and relearn</em>: os letrados serão os que sabem <strong>aprender, desaprender e reaprender</strong>. Alternativa <strong>E</strong>.</p><p>Ler e escrever é justamente o critério que deixa de ser o principal (A, B, C e D).</p>"},
28: {"materia": "Inglês", "assunto": "Verbos", "tags": ["modais"],
     "enunciado": p("Na oração <em>In terms of work, you will have to adapt some of your skills to the jobs of the future, and you will also have to learn new skills</em>, presente no quinto parágrafo do texto, a expressão <em>will have to</em> indica"),
     "apoio_de": (25, P25),
     "alternativas": alts("opção.", "proibição.", "obrigação.", "permissão.", "possibilidade."),
     "explicacao": "<p><em>Have to</em> expressa necessidade, <strong>obrigação</strong>: “você <em>terá de</em> adaptar suas habilidades”. Alternativa <strong>C</strong>.</p><p>Opção e possibilidade seriam <em>may</em> ou <em>might</em> (A e E), proibição, <em>must not</em> (B), e permissão, <em>can</em> ou <em>may</em> (D).</p>"},
29: {"materia": "Inglês", "assunto": "Interpretação de texto",
     "enunciado": p("De acordo com o texto, algumas habilidades adicionais serão necessárias para os empregos do futuro.", "A capacidade de fazer anotações detalhadas, selecionar ideias principais, entender e dar sentido às informações refere-se à habilidade de"),
     "apoio_de": (25, P25),
     "alternativas": alts("aprender a aprender.", "analisar informação.", "identificar padrões e tendências.", "se comunicar oralmente e por escrito.", "entender e acompanhar avanços tecnológicos."),
     "explicacao": "<p>O item <em>Analyzing information</em> diz: “<em>When you take good and detailed notes, you can review them to pick out the big ideas, understand, and make sense of information</em>”. Alternativa <strong>B</strong>.</p><p>As outras habilidades têm descrições diferentes no texto (A, C, D e E).</p>"},
30: {"materia": "Matemática", "assunto": "Matrizes", "tags": ["multiplicação de matrizes"],
     "enunciado": p("João, Sílvia e Pedro são funcionários de uma empresa.", "Considere as matrizes:")
                  + "\\[A = \\begin{pmatrix} 10 & 12 & 8 \\end{pmatrix} \\quad \\text{e} \\quad B = \\begin{pmatrix} 25 & 40 & 12 & 32 \\\\ 15 & 22 & 30 & 30 \\\\ 30 & 25 & 25 & 18 \\end{pmatrix}\\]"
                  + p("em que:", "• a matriz A representa o valor, em reais, recebido por hora trabalhada de João, Sílvia e Pedro, respectivamente;<br>• a matriz B representa a quantidade de horas trabalhadas por semana dos mesmos funcionários, em cada uma das quatro primeiras semanas no mês de julho de 2018;<br>• na matriz B, as linhas 1 a 3 são para João, Sílvia e Pedro, respectivamente; e as colunas de 1 a 4 são, nessa ordem, para as quatro primeiras semanas do mês de julho, de modo que, por exemplo, o elemento b<sub>13</sub> é a quantidade de horas que João trabalhou na terceira semana desse mês.",
                      "O valor pago pela empresa pelas horas trabalhadas por esses três funcionários na segunda semana de julho de 2018 será"),
     "alternativas": alts("R$ 670,00.", "R$ 680,00.", "R$ 824,00.", "R$ 980,00.", "R$ 984,00."),
     "anulacao": {"fonte": "analise", "motivo": "O Centro Paula Souza anulou a questão sem publicar o motivo. Pela análise do Treineiros, o valor correto não está entre as alternativas: na segunda semana (coluna 2 de B), João trabalhou 40 h, Sílvia 22 h e Pedro 25 h, e o total pago é 10 · 40 + 12 · 22 + 8 · 25 = 400 + 264 + 200 = R$ 864,00."},
     "explicacao": "<p>Questão anulada. A resolução esperada: multiplica-se a matriz A pela coluna da segunda semana de B. João: 10 · 40 = 400; Sílvia: 12 · 22 = 264; Pedro: 8 · 25 = 200. Total: R$ 864,00, valor que não aparece nas alternativas.</p><p>Um erro comum seria usar a segunda <em>linha</em> de B (as horas de Sílvia) em vez da segunda coluna.</p>"},
31: {"materia": "Matemática", "assunto": "Geometria espacial", "tags": ["cilindro", "volume"],
     "enunciado": p(*T(12, "Uma garrafa térmica tem formato", "em cm3, aproximadamente,", ["O suco é despejado", "Nessas condições"])) + "[[fig:1]]"
                  + apoio("Adote π = 3.<br>Despreze a espessura do material da garrafa e do copo."),
     "trocar": [("em cm3", "em cm<sup>3</sup>")],
     "imagens": figs(("q31", "Garrafa térmica cilíndrica de 8 cm de diâmetro, com o nível do suco marcado a 13 cm da base.")),
     "alternativas": alts("250.", "380.", "540.", "620.", "800."),
     "explicacao": "<p>Na garrafa (raio 4 cm, altura 13 cm): V = 3 · 4² · 13 = 624 cm³. No copo (raio 2 cm, altura 7 cm): V = 3 · 2² · 7 = 84 cm³. Restam 624 − 84 = <strong>540 cm³</strong>. Alternativa <strong>C</strong>.</p><p>Usar o diâmetro no lugar do raio leva a valores muito maiores (E). E 620 é quase o volume inicial (D).</p>"},
32: {"materia": "Matemática", "assunto": "Porcentagem", "tags": ["frequência cardíaca"],
     "enunciado": p("Considere que:") + apoio("• a frequência cardíaca máxima de uma pessoa, em batimentos por minuto (bpm), é a diferença entre uma constante K e a idade da pessoa. O valor de K para um homem é 220 e, para uma mulher, K é 226.<br>• a frequência cardíaca ideal para queimar gordura e emagrecer durante um treino é de 60% a 75% da frequência cardíaca máxima.")
                  + p("Dessa forma, a frequência cardíaca ideal para queimar gordura e emagrecer durante um treino para um homem de 40 anos, em bpm, varia de"),
     "alternativas": alts("114 a 143.", "111 a 139.", "108 a 135.", "105 a 132.", "102 a 128."),
     "explicacao": "<p>A frequência máxima é 220 − 40 = 180 bpm. A faixa ideal vai de 0,60 · 180 = 108 a 0,75 · 180 = 135 bpm. Alternativa <strong>C</strong>.</p><p>Usar K = 226, o valor das mulheres, daria de 111,6 a 139,5 (B).</p>"},
33: {"materia": "Matemática", "assunto": "Probabilidade", "tags": ["gráficos"],
     "enunciado": p("O artesão brasileiro é um agente de produção nas áreas cultural e econômica do país, gerando empregos e contribuindo para a identidade regional. Observe os gráficos e admita distribuição homogênea de dados.") + "[[fig:1]]"
                  + fonte("Fonte de dados: &lt;https://tinyurl.com/ycgl2ljx&gt; Acesso em: 09/10/2018. Adaptado.")
                  + p("Suponha que uma viagem será sorteada entre todos os artesãos brasileiros, a probabilidade de que o ganhador da viagem seja uma mulher de 65 anos ou mais é de"),
     "imagens": figs(("q33", "Dois gráficos sobre os artesãos brasileiros. Barras por faixa etária: 18 a 24 anos, 1%; 25 a 29, 2%; 30 a 34, 6%; 35 a 39, 10%; 40 a 49, 27%; 50 a 64, 41%; 65 anos ou mais, 12%. Setores por sexo: feminino, 77%; masculino, 23%.")),
     "alternativas": alts("31,57%.", "20,79%.", "12,43%.", "9,24%.", "4,85%."),
     "explicacao": "<p>Com distribuição homogênea, a probabilidade é o produto: 0,77 (mulher) · 0,12 (65 anos ou mais) = 0,0924 = <strong>9,24%</strong>. Alternativa <strong>D</strong>.</p><p>Os outros valores combinam faixas ou porcentagens erradas.</p>"},
34: {"materia": "Matemática", "assunto": "Geometria plana", "tags": ["área", "triângulos"],
     "enunciado": p(*T(14, "Uma artesã borda, com lã, tapetes", "conforme a figura.")) + "[[fig:1]]"
                  + p("Cada triângulo preto é retângulo e isósceles com hipotenusa \\(12\\sqrt{2}\\) cm. Cada triângulo cinza é semelhante a um triângulo preto e possui dois lados de medida 10 cm.", "Assim posto, a área no padrão bordada em branco é, em cm<sup>2</sup>,"),
     "imagens": figs(("q34", "Retângulo de 40 cm por 20 cm. Nos quatro cantos, triângulos cinza; no centro, dois triângulos pretos, um apontando para a esquerda e outro para a direita; o resto é branco.")),
     "alternativas": alts("344.", "456.", "582.", "628.", "780."),
     "explicacao": "<p>Um triângulo retângulo isósceles com hipotenusa \\(12\\sqrt{2}\\) tem catetos de 12 cm: área 12 · 12 ÷ 2 = 72 cm²; os dois pretos somam 144 cm². Os cinza têm catetos de 10 cm: 50 cm² cada, 200 cm² os quatro. O retângulo tem 800 cm²: branco = 800 − 144 − 200 = <strong>456 cm²</strong>. Alternativa <strong>B</strong>.</p><p>344 é a soma das áreas coloridas, não a branca (A).</p>"},
35: {"materia": "Física", "assunto": "Cinemática", "tags": ["velocidade média"],
     "enunciado": NAVIO + P35,
     "alternativas": alts("1 nó é igual a aproximadamente 1,85 km.", "milha náutica é também unidade de medida pertencente ao SI.", "a velocidade média do navio nessa rota seria, obrigatoriamente, 8 nós.",
                          "o menor tempo possível da viagem nesse percurso seria exatamente 1 h.", "o navio, mantendo a velocidade de cruzeiro, levaria aproximadamente 2 h no percurso."),
     "explicacao": "<p>Na velocidade de cruzeiro de 11 km/h, os 22 km da rota levam 22 ÷ 11 = <strong>2 h</strong>. Alternativa <strong>E</strong>.</p><p>Nó é unidade de velocidade: 1 nó ≈ 1,85 km/h, não km (A). A milha náutica não é do SI (B). Nada obriga a média a ser 8 nós (C). E na velocidade máxima, 18,5 km/h, a viagem levaria cerca de 1,2 h, não exatamente 1 h (D).</p>"},
36: {"materia": "Física", "assunto": "Dinâmica", "tags": ["quantidade de movimento"],
     "enunciado": p("Se o navio, considerado estável, percorre um trecho qualquer em velocidade de cruzeiro, podemos concluir que a quantidade de movimento, em <strong>kg·m/s</strong>, nesse trecho especificado é, aproximadamente,"),
     "apoio_de": (35, P35),
     "alternativas": alts("1,37 × 10<sup>4</sup>", "4,95 × 10<sup>4</sup>", "8,32 × 10<sup>4</sup>", "1,37 × 10<sup>7</sup>", "4,95 × 10<sup>7</sup>"),
     "explicacao": "<p>A massa é 4 500 t = 4,5 × 10⁶ kg, e a velocidade de cruzeiro, 11 km/h ≈ 3,06 m/s. Q = m · v ≈ 4,5 × 10⁶ · 3,06 ≈ <strong>1,37 × 10⁷ kg·m/s</strong>. Alternativa <strong>D</strong>.</p><p>4,95 × 10⁷ esquece de converter km/h em m/s (E). As alternativas com 10⁴ erram a conversão de toneladas em quilogramas (A, B e C).</p>"},
37: {"materia": "Física", "assunto": "Hidrostática", "tags": MULTI + ["empuxo", "ondas eletromagnéticas"],
     "enunciado": p("Relacionando as informações do texto com os respectivos conceitos físicos, está correto afirmar que"), "apoio_de": (35, P35),
     "alternativas": alts("4 MWh equivale à potência máxima da bateria em condições normais.", "podemos considerar que, em condições de estabilidade estática e repouso, o empuxo aplicado no navio equivale a 4,5 × 10<sup>7</sup> N.",
                          "as “câmeras no visível e no infravermelho” referem-se a câmeras que operam com ondas eletromagnéticas nas frequências do visível e do infravermelho e, portanto, não funcionam à noite.",
                          "o sistema de detecção RADAR funciona por emissão de ondas mecânicas de rádio na frequência da luz visível.", "o sistema de detecção LIDAR torna-se mais lento e menos preciso em comparação a outros métodos por operar com pulsos de luz laser."),
     "explicacao": "<p>Em repouso, o navio flutua em equilíbrio: o empuxo é igual ao peso, E = m · g = 4,5 × 10⁶ kg · 10 m/s² = <strong>4,5 × 10⁷ N</strong>. Alternativa <strong>B</strong>.</p><p>MWh é unidade de energia, não de potência (A). Câmeras infravermelhas funcionam à noite, porque captam o calor (C). Ondas de rádio são eletromagnéticas e não têm a frequência da luz visível (D). E o LIDAR é rápido e muito preciso (E).</p>"},
38: {"materia": "Física", "assunto": "Óptica", "tags": ["espelho convexo"],
     "enunciado": p("A figura apresenta a obra de litogravura “Mão com esfera refletora” (1935), do artista gráfico holandês Maurits Cornelis Escher (1898–1972), que se representou por uma imagem refletida em uma esfera.") + "[[fig:1]]"
                  + url("https://tinyurl.com/yardzola", "15.10.2018", "")
                  + p("Sendo o artista o objeto refletido na superfície dessa esfera, podemos afirmar corretamente, sobre essa imagem formada, que se"),
     "imagens": figs(("q38", "Litogravura “Mão com esfera refletora”, de Escher: uma mão segura uma esfera espelhada na qual aparece, deformado, o próprio artista sentado em sua sala, com móveis e estantes ao redor.")),
     "alternativas": alts("assemelha à classificação exata de uma imagem observada em uma lente delgada convergente.", "assemelha à classificação exata de uma imagem observada em um espelho côncavo.", "classifica em menor, direita e real.",
                          "posiciona entre o foco e o vértice da face refletora.", "posiciona entre o raio de curvatura e o vértice da face refletora."),
     "explicacao": "<p>A face externa da esfera é um <strong>espelho convexo</strong>. Ele forma sempre imagem virtual, direita e menor, situada atrás do espelho, <strong>entre o foco e o vértice</strong>. Alternativa <strong>D</strong>.</p><p>Lentes convergentes e espelhos côncavos formam imagens de outros tipos, dependendo da posição do objeto (A e B). A imagem do espelho convexo é virtual, não real (C). E ela não chega à região do centro de curvatura (E).</p>"},
39: {"materia": "Física", "assunto": "Circuitos elétricos", "tags": ["associação de resistores"],
     "enunciado": p("Um circuito eletrônico utilizado pelos alunos da FATEC possui resistores, medidos em ohm, e uma ddp de 12 V entre os pontos A–B, conforme a figura.") + "[[fig:1]]"
                  + p("O valor da corrente elétrica da associação de resistores no circuito apresentado na figura, em ampère, é"),
     "imagens": figs(("q39", "Circuito formado por dois círculos sobrepostos, que se cruzam em dois nós, à esquerda e à direita. O ponto A liga-se ao nó da esquerda e o ponto B ao nó da direita. Entre os dois nós há quatro caminhos: o arco externo de cima, com três resistores de 8 Ω; o arco interno de cima, com dois resistores de 12 Ω; o arco interno de baixo, com dois resistores de 12 Ω; e o arco externo de baixo, com três resistores de 8 Ω.")),
     "alternativas": alts("6", "5", "4", "3", "2"),
     "explicacao": "<p>Entre os nós ligados a A e a B há quatro caminhos em paralelo: dois externos, cada um com 8 + 8 + 8 = 24 Ω, e dois internos, cada um com 12 + 12 = 24 Ω. Quatro resistências iguais de 24 Ω em paralelo dão 24 ÷ 4 = 6 Ω. A corrente é i = U ÷ R = 12 ÷ 6 = <strong>2 A</strong>. Alternativa <strong>E</strong>.</p><p>Somar todos os resistores, ou considerar só parte dos caminhos, leva aos outros valores.</p>"},
40: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["florestas", "desmatamento"],
     "enunciado": p("Leia o texto.") + apoio(*T(15, "“Há 8 mil anos, o espaço geográfico", "e a Ásia, 5,5%.", ["No início do século XXI"]))
                  + fonte("Fonte dos dados: MIRANDA, Evaristo Eduardo de. <em>Quando o Amazonas corria para o Pacífico: uma história desconhecida da Amazônia</em>. Petrópolis, RJ. 2 ed.: VOZES, 2007.")
                  + p("Relacionando as informações dos dois períodos históricos citados no texto, é correto afirmar que"),
     "explicacao": "<p>A participação do Brasil nas florestas do mundo subiu de 9,8% para 28,3%, enquanto a da Europa, da África e da Ásia caiu muito. Ou seja, proporcionalmente, o desmatamento no território brasileiro foi <strong>menor</strong> que nesses continentes. Alternativa <strong>B</strong>.</p><p>A Europa tinha 7%, menos que a África e a Ásia (A). A Ásia e a Europa perderam florestas (C). A África caiu de 11% para 3,4% e a Ásia, de 23,6% para 5,5%, ritmos diferentes (D). E houve desmatamento no Brasil, apenas proporcionalmente menor (E).</p>"},
41: {"materia": "Geografia", "assunto": "Geopolítica", "tags": ["terras-raras", "recursos minerais"],
     "enunciado": p(*T(16, "Terras-raras é o nome dado ao conjunto", "podemos afirmar corretamente que", ["Sobre esses elementos"])),
     "explicacao": "<p>As terras-raras aparecem em pequenas concentrações misturadas a outros minerais, o que torna a separação difícil e cara. A <strong>China</strong> tem as maiores reservas e domina a produção mundial. Alternativa <strong>C</strong>.</p><p>Elas são usadas sobretudo em eletrônicos, ímãs e baterias (A e B). Não são de fácil extração (D). E a bateia é usada para ouro, não para terras-raras (E). Os países citados nessas alternativas também não concentram as reservas.</p>"},
42: {"materia": "Geografia", "assunto": "Tectônica de placas", "tags": ["Círculo de Fogo"],
     "enunciado": p(*T(16, "Centenas de pessoas morreram e milhares", "pois esse país se localiza", ["O fenômeno relatado"])),
     "explicacao": "<p>A Indonésia fica no <strong>Círculo de Fogo do Pacífico</strong>, área de encontro de placas tectônicas, com fossas oceânicas e arcos vulcânicos, onde terremotos e erupções são frequentes. Alternativa <strong>B</strong>.</p><p>A placa Africana não está no Pacífico (A). Epirogênese é um movimento lento, que não causa terremotos súbitos (C). Grabens e horsts não explicam a sismicidade da Indonésia (D). E a Dorsal Meso-Atlântica fica no Atlântico (E).</p>"},
43: {"materia": "Geografia", "assunto": "Transportes e logística", "tags": ["ferrovias paulistas"],
     "enunciado": p(*T(16, "Alguns municípios do estado de São Paulo", "dos municípios de", ["A Estrada de Ferro Noroeste"])),
     "alternativas": alts("Bauru, Lins e Penápolis.", "Sorocaba, Botucatu, e Avaré.", "Campinas, Limeira e Rio Claro.", "Araraquara, Catanduva e Votuporanga.", "Jaguariúna, Mogi Mirim e Ribeirão Preto."),
     "explicacao": "<p>A Estrada de Ferro Noroeste do Brasil partia de <strong>Bauru</strong> rumo ao Mato Grosso e impulsionou cidades do noroeste paulista, como <strong>Lins e Penápolis</strong>. Alternativa <strong>A</strong>.</p><p>As outras cidades foram servidas por outras ferrovias, como a Sorocabana (B), a Paulista (C), a Araraquarense (D) e a Mogiana (E).</p>"},
44: {"materia": "Geografia", "assunto": "Industrialização brasileira", "tags": ["4ª Revolução Industrial"],
     "enunciado": p("Leia o texto.") + apoio(*T(16, "Klaus Schwab, fundador do Fórum", "física, digital e biológica.", ["A 1a revolução", "A 2a revolução", "A 3a revolução", "Agora, no século XXI"]))
                  + url("https://tinyurl.com/y72sm8v5", "17.09.2018")
                  + p("De acordo com a tendência expressa no texto, a última revolução industrial citada pelo autor caracteriza-se por"),
     "trocar": [("A 1a revolução", "A 1ª revolução"), ("A 2a revolução", "A 2ª revolução"), ("A 3a revolução", "A 3ª revolução"), ("a 4a revolução", "a 4ª revolução")],
     "alternativas": alts("redes aéreas de comunicação e pela intensificação do uso do fordismo.", "viagens interespaciais e pelo grande emprego de carvão mineral.", "cabeamento telegráfico submarino e pela adoção do taylorismo.",
                          "computadores a válvula e pela utilização de linhas de produção.", "internet móvel e pela inteligência artificial."),
     "explicacao": "<p>A 4ª Revolução Industrial funde as esferas física, digital e biológica, com <strong>internet móvel, inteligência artificial</strong>, robótica e internet das coisas. Alternativa <strong>E</strong>.</p><p>Fordismo, taylorismo, carvão, telégrafo e computadores a válvula são marcas das revoluções anteriores (A, B, C e D).</p>"},
45: {"materia": "Biologia", "assunto": "Ecologia", "tags": ["conferências ambientais"],
     "enunciado": p(*T(17, "A fim de controlar os diversos problemas", "a respeito dessas conferências.", ["Assinale a alternativa"])),
     "alternativas": alts("Durante a Eco–92 foram levantados recursos para a recuperação de pelo menos 92% da camada de ozônio nas regiões de clima temperado.",
                          "Um produto da Eco–92 foi a Agenda–21, documento em que constam programas para um desenvolvimento mais sustentável durante o século XXI.",
                          "Na Rio+20, mais vinte bacias hidrográficas (incluindo a do Uruguai) entraram para o regime especial de proteção de águas continentais da ONU.",
                          "A Rio+20 determinou maior fiscalização em usinas nucleares, a fim de evitar acidentes atômicos como os de Chernobyl, Goiânia e Fukushima.",
                          "Após a Rio+20, Canadá, Rússia e China deixaram a ONU, alegando discordâncias com políticas que interfeririam na autonomia dos países desenvolvidos."),
     "explicacao": "<p>A <strong>Agenda 21</strong>, aprovada na Eco-92, no Rio de Janeiro, reúne programas para o desenvolvimento sustentável no século XXI. Alternativa <strong>B</strong>.</p><p>O “92” é o ano da conferência, não uma porcentagem (A). O “+20” indica os 20 anos desde a Eco-92, não 20 bacias (C). A Rio+20 não tratou de usinas nucleares, e o acidente de Goiânia foi com césio-137 de um aparelho médico (D). E nenhum desses países deixou a ONU (E).</p>"},
46: {"materia": "Biologia", "assunto": "Evolução", "tags": ["seleção artificial"],
     "enunciado": FRANGO + P46,
     "explicacao": "<p>O texto fala de <strong>seleção artificial</strong>: ao longo das gerações, cruzaram-se as aves mais eficientes no uso da energia e de crescimento mais rápido, o que reduziu o consumo de ração e o custo da criação. Alternativa <strong>E</strong>.</p><p>A seleção não foi feita nas aves mais fracas nem aumentou o envelhecimento (A), não envolveu transgênicos (B), não aumentou a população das aves (C), e não houve seleção natural por risco de extinção (D).</p>"},
47: {"materia": "Biologia", "assunto": "Zoologia", "tags": ["embriologia", "amniotas"],
     "enunciado": p(*T(17, "Estudos evolutivos sobre os padrões", "desenvolvimento de", ["Para a ampliação da eficiência"])),
     "apoio_de": (46, P46),
     "explicacao": "<p>Aves, jacarés e porcos são vertebrados: são <strong>deuterostômios</strong>, passam pela neurulação (formação do tubo neural) e são <strong>amniotas</strong>, com âmnio no desenvolvimento embrionário. Alternativa <strong>B</strong>.</p><p>Rãs e sapos são anfíbios: não produzem ovos com casca nem amnióticos (A e D). E nenhum vertebrado é protostômio (C, D e E).</p>"},
48: {"materia": "Biologia", "assunto": "Genética", "tags": ["aneuploidias"],
     "explicacao": "<p>Os autossomos 13, 18 e 21 estão em pares normais, mas há só um X e nenhum Y (cariótipo 45,X0). Sem o cromossomo Y, o sexo biológico é <strong>feminino</strong>, com <strong>síndrome de Turner</strong>. Alternativa <strong>A</strong>.</p><p>Klinefelter é XXY, de sexo masculino (B). E as síndromes de Edwards, Down e Patau são trissomias dos cromossomos 18, 21 e 13, que aqui estão em pares (C, D e E).</p>"},
49: {"materia": "Biologia", "assunto": "Ecologia", "tags": ["fluxo de energia"],
     "enunciado": p(*T(18, "Atualmente os ecólogos tendem a considerar", "associadas a transações comerciais.")) + "[[fig:1]]" + p("Nesse contexto, é correto afirmar que, de acordo com o esquema,"),
     "imagens": figs(("q49", "Esquema de fluxo de energia: o Sol fornece energia à plantação, que produz alimentos, consumidos pelos trabalhadores da zona rural e da zona urbana. O Sol também origina os combustíveis fósseis, que fornecem energia aos dois grupos de trabalhadores. Há trocas entre os trabalhadores: os da zona urbana prestam serviços e os da zona rural fazem o manejo da fazenda, com pagamentos em dinheiro (linhas tracejadas) em troca de bens e serviços (linhas cheias).")),
     "alternativas": alts("serviços ecossistêmicos, tais como o comprado dos trabalhadores da zona urbana, dificultam o fluxo energético.", "o dinheiro recebido pelos trabalhadores da zona rural é convertido em energia que prejudica os meios de produção fótica.",
                          "trabalhadores das zonas rural e urbana negociam a energia disponibilizadas por produtores presentes no primeiro nível trófico.", "os combustíveis fósseis resultam da ação dos decompositores sobre o excedente produzido pelos consumidores terciários.",
                          "o trabalho vendido pelos trabalhadores da zona urbana tão barato quanto o trabalho vendido pelos trabalhadores da zona rural."),
     "explicacao": "<p>A plantação é o produtor, o primeiro nível trófico. A energia que ela fixa vira alimentos, que os trabalhadores rurais e urbanos negociam entre si. Alternativa <strong>C</strong>.</p><p>Os serviços urbanos alimentam o fluxo, não o dificultam (A). O dinheiro não prejudica a produção fotossintética (B). Os combustíveis fósseis vêm da matéria orgânica de seres antigos, não do excedente de consumidores terciários (D). E o esquema não compara preços de trabalho (E).</p>"},
50: {"materia": "Português", "assunto": "Classes de palavras", "tags": ["“que”"],
     "enunciado": GRANDIN + P50,
     "explicacao": "<p>O primeiro “que” liga “dizem” à oração “tenho olho biônico”, que funciona como objeto direto: é <strong>conjunção subordinativa integrante</strong>. O segundo retoma “coisa” (“uma coisa que eu não tinha visto”): é <strong>pronome relativo</strong>. Alternativa <strong>B</strong>.</p><p>A oração do primeiro “que” é subordinada, não coordenada, e a do segundo é restritiva, não explicativa (A). As funções são diferentes (C, D e E), e o primeiro “que” não retoma o verbo (D).</p>"},
51: {"materia": "Português", "assunto": "Semântica", "tags": ["paráfrase"],
     "enunciado": p("Assinale a alternativa em que a paráfrase corresponda ao sentido do período original apresentado, mantendo as mesmas relações sintático-semânticas."), "apoio_de": (50, P50),
     "alternativas": colunas(["Texto original", "Paráfrase"], [
         ["<em>“Grandin tem um parafuso a mais quando se trata do bem-estar dos bichos.”</em>", "Grandin não tem juízo ao tratar bem os animais."],
         ["<em>“Grandin traduziu esse entendimento em projetos que propunham mudanças no manejo.”</em>", "Tal entendimento era traduzido a Grandin por projetos propostos para mudar o manejo."],
         ["<em>“Hoje, instalações criadas por ela são familiares a quase metade dos bovinos nos Estados Unidos.”</em>", "Frequentemente, ela cria instalações que são íntimas de metade das criações da América do Norte."],
         ["<em>“Professora de ciência animal, ela é autista e dona de uma hipersensibilidade visual e auditiva.”</em>", "Ela é autista e, embora seja professora de ciência animal, apresenta pouca sensibilidade visual e auditiva."],
         ["<em>“Tocada pelas angústias do gado desde a juventude, ela compreendia por que a rês recuava na hora da vacinação...”</em>", "Por ter se sensibilizado pelo sofrimento animal na juventude, ela entendia quais motivos faziam o animal recuar durante a vacinação..."]]),
     "explicacao": "<p>Em E, a oração “Tocada pelas angústias do gado” tem valor de causa, mantido em “Por ter se sensibilizado”, e “compreendia por que a rês recuava” vira “entendia quais motivos faziam o animal recuar”. Alternativa <strong>E</strong>.</p><p>A transforma um elogio (ela tem uma habilidade especial) em crítica. B inverte o agente: era Grandin quem traduzia o entendimento. C troca “hoje” por “frequentemente” e “quase metade dos bovinos” por “metade das criações”. D diz o contrário: ela tem <em>hipersensibilidade</em>.</p>"},
52: {"materia": "Português", "assunto": "Figuras de linguagem", "tags": ["metáfora"],
     "enunciado": p("Sobre a expressão <em>“parafuso a mais”</em> presente na passagem <em>“Grandin tem um parafuso a mais quando se trata do bem-estar dos bichos.”</em>, é correto afirmar que se trata de"), "apoio_de": (50, P50),
     "explicacao": "<p>A expressão popular é “ter um parafuso a menos” (ser louco). O autor a inverte, “um parafuso a mais”, numa <strong>metáfora</strong> para a habilidade especial de Grandin com os animais (e brinca com os parafusos da porteira do início do texto). Alternativa <strong>D</strong>.</p><p>Não há jogo com o nome dela (A), nem repetição de sons (B e C), e “trata-se” fica no singular porque tem sujeito indeterminado (E).</p>"},
53: {"materia": "Português", "assunto": "Interpretação de texto",
     "enunciado": p("De acordo com as informações apresentadas no texto sobre os trabalhos da professora Temple Grandin, a mudança proposta por ela no tratamento dos animais acarreta"), "apoio_de": (50, P50),
     "explicacao": "<p>O texto diz que o tempo de manejo cai pela metade e que os vaqueiros “sofrem menos acidentes no trabalho” e têm relações mais harmoniosas: “A melhoria do bem-estar animal melhora o bem-estar humano”. Alternativa <strong>A</strong>.</p><p>O texto não fala em encarecimento (B), em prejuízo aos tratadores (C), em criadores de pequeno porte (D) nem em prejuízo aos animais (E).</p>"},
54: {"materia": "Português", "assunto": "Texto literário", "tags": ["educação"],
     "enunciado": chamada("Leia o texto para responder à questão de número 54.")
                  + apoio(*T(21, "A denúncia de uma crise de sentido", "o direito à cidadania.", ["[...]", "A reflexão sobre o sentido"]))
                  + fonte("(ROCHA, J. Design thinking na formação de professores: novos olhares para os desafios da educação. <em>In: Metodologias ativas para uma educação inovadora</em>. Porto Alegre: Penso, 2018, p.154.)")
                  + p("O excerto apresenta, brevemente, uma crítica ao modelo vigente da educação na sociedade brasileira nos anos 1950.", "Assinale a alternativa em que o trecho literário retrata uma situação semelhante à abordada no texto."),
     "alternativas": alts(*[re.sub(r"\s*\([A-E]\)$", "", x).replace("Caminhos Cruzados", "<em>Caminhos Cruzados</em>").replace("Minha Vida de Menina", "<em>Minha Vida de Menina</em>").replace("Vidas Secas", "<em>Vidas Secas</em>").replace("São Bernardo", "<em>São Bernardo</em>").replace("Memórias de um Sargento de Milícias", "<em>Memórias de um Sargento de Milícias</em>")
                           for x in T(21, "“E ele, Clarimundo, o homem do relógio", "Memórias de um Sargento de Milícias.", ["“As primas já estão", "“Fabiano estava contente", "“Dirigi-me a alguns amigos", "“Na segunda-feira, voltou"])]),
     "explicacao": "<p>O texto fala da pressão pelo acesso à escola ligada ao direito à cidadania, num Brasil ainda pouco urbanizado. Em <em>Vidas Secas</em>, a família de retirantes sonha com a cidade grande e com “os meninos em escolas, aprendendo coisas difíceis e necessárias”: a escola como caminho para uma vida melhor. Alternativa <strong>C</strong>.</p><p>Os outros trechos tratam de um intelectual solitário (A), da saúde de uma aluna interna (B), da criação de um jornal (D) e de castigos na escola de outra época, sem ligação com o acesso à educação (E).</p>"},
}
# Revisão (12/11): a legenda da figura (Rugendas) tinha vazado para o meio da alternativa C da Q19.
Q[19]["alternativas"] = {"A": "organização da vida social, construção de igrejas e de cemitérios, organização de festas, cuidados com os necessitados e formação profissional com o ensino dos ofícios mecânicos e das artes.", "B": "organização da vida econômica, construção e manutenção de estradas, criação dos órgãos de fiscalização e cobrança de impostos, e administração dos seminários coloniais, responsáveis pela formação de novos padres.", "C": "organização da vida política, construção de hospitais e de escolas de educação básica, administração do patrimônio do Vaticano no Brasil e organização de bazares e feiras para arrecadação de donativos para os necessitados.", "D": "criação e fiscalização do cumprimento das leis referentes à moral e aos costumes dos moradores de Minas Gerais, celebração semanal do rito da missa e administração de sacramentos, como o batismo, o casamento e a extrema unção.", "E": "criação dos órgãos de controle metropolitano sobre a população de escravos e libertos, regulamentação das práticas do Candomblé, construção de casas para os irmãos de baixa renda e desenvolvimento de sistemas de ensino religioso ecumênico."}
completar(Q, R)
