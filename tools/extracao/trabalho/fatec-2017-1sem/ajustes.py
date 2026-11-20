# Ajustes da conferência humana: Vestibular FATEC 1º semestre de 2017 (exame de 08/01/2017)
# Texto conferido com a imagem de cada página. Tema implícito: Mulheres e trabalho (redação: perspectivas de igualdade entre mulheres e homens no mundo do trabalho).
# 54 questões; a prova tem 5 h no total, incluindo a redação (que fica fora do simulado).
# Matéria: a do gabarito oficial; nas "Multidisciplinar", a matéria principal + tag "multidisciplinar".
# Rascunho com colunas embaralhadas: enunciados e alternativas escritos aqui.
# Gabarito: oficial RETIFICADO (1º SEM/17; o documento não diz qual questão mudou), sem anuladas. Q12 alternativas-imagem (roleta). Poema de Camilo Pessanha (m. 1926, domínio público) transcrito.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import A, carregar, enun, tabela, colunas, completar, trecho

ID = "fatec-2017-1sem"
META = {
    "id": ID,
    "banca": "FATEC",
    "ano": 2017,
    "semestre": 1,
    "titulo": "Vestibular FATEC, 1º semestre de 2017",
    "fonte": "Centro Paula Souza",
    "dataExame": "2017-01-08",
    "duracaoMinutos": 300,
    "tema": "Mulheres e trabalho",
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
GENERO = (p("Leia os textos.")
          + apoio("<strong>Mais escolarizadas, mulheres ainda ganham menos e têm dificuldades de subir na carreira</strong>", " ".join(T(2, "As mulheres brasileiras já engravidam menos", "dificuldades em ascender na carreira.")))
          + url("http://tinyurl.com/gnbsmbs", "29.08.2016")
          + apoio("<strong>Homens recebem salários 30% maiores do que as mulheres no Brasil</strong>", " ".join(T(2, "O Brasil apresenta um grande nível de disparidade", "de instrução que eles.")))
          + url("http://tinyurl.com/zuzfenl", "29.08.2016"))
P1 = p("Dentre os motivos que explicam essa disparidade, podemos destacar corretamente")

BH = (chamada("Leia o gráfico referente ao rendimento médio mensal na Região Metropolitana de Belo Horizonte (BH), no período de 2010 a 2013, para responder às questões de números 03 e 04.")
      + "[[fig:1]]" + fonte("Fonte dos dados: &lt;http://tinyurl.com/h3qt2mo&gt; Acesso em: 01.09.2016."))
BH_IMG = figs(("q03", "Gráfico “Rendimento médio mensal, em reais, por sexo”, de 2010 a 2013. Homens: R$ 1.912,00 (2010), R$ 1.809,00 (2011), R$ 1.784,00 (2012) e R$ 2.022,00 (2013). Mulheres: R$ 1.312,00 (2010), R$ 1.323,00 (2011), R$ 1.278,00 (2012) e R$ 1.410,00 (2013)."))
P3 = p("Sobre os dados do gráfico, podemos afirmar corretamente que a média do rendimento médio mensal das mulheres, no período de 2010 a 2013 foi, em reais, de")

AMIGOS = (chamada("Leia o texto para responder às questões de números 20 a 22.")
          + apoio("Cinco amigos estavam estudando para a prova de Química e decidiram fazer um jogo com os elementos da Tabela Periódica:<br>• cada participante selecionou um isótopo dos elementos da Tabela Periódica e anotou sua escolha em um cartão de papel;<br>• os jogadores Fernanda, Gabriela, Júlia, Paulo e Pedro decidiram que o vencedor seria aquele que apresentasse o cartão contendo o isótopo com o maior número de nêutrons.",
                  "Os cartões foram, então, mostrados pelos jogadores.")
          + tabela(["Fernanda", "Gabriela", "Júlia", "Paulo", "Pedro"], [["\\({}^{56}_{26}\\text{Fe}\\)", "\\({}^{16}_{8}\\text{O}\\)", "\\({}^{40}_{20}\\text{Ca}\\)", "\\({}^{7}_{3}\\text{Li}\\)", "\\({}^{35}_{17}\\text{C}\\ell\\)"]]))
P20 = p("Observando os cartões, é correto afirmar que o(a) vencedor(a) foi")

WORK = (chamada("Leia o texto para responder às questões de números 25 a 29.")
        + apoio("<strong>Here’s how long you can work before your brain <sup>1</sup>shuts down</strong>",
                *T(11, "I’m having a hard time starting this article.", "both men and women.", ["Tell us something we didn’t know.", "For some employees, of course", "So how much is too much?"]))
        + url("http://tinyurl.com/j4os8ck", "24.08.2016")
        + apoio("<strong>Glossário</strong><br><sup>1</sup><em>to shut down</em>: parar de operar/funcionar.<br><sup>2</sup> <em>physician</em>: médico.<br><sup>3</sup><em>gig economy</em>: ambiente de trabalho baseado em empregos temporários e contratos de curta duração."))
WORK = WORK.replace("resident 2 physician", "resident <sup>2</sup>physician").replace("“3gig economy”", "“<sup>3</sup>gig economy”").replace("dumber.” Our study", "dumber. “Our study")
P25 = p("Ao escrever, no início do texto, “<em>I’m having a hard time starting this article</em>”, o autor")

PIXEL = (chamada("Leia o texto para responder às questões de números 30 e 31.")
         + p("Uma tela de computador pode ser representada por uma matriz de cores, de forma que cada elemento da matriz corresponda a um <em>pixel</em>* na tela.",
             "Numa tela em escala de cinza, por exemplo, podemos atribuir 256 cores diferentes para cada <em>pixel</em>, do preto absoluto (código da cor: 0) passando pelo cinza intermediário (código da cor: 127) ao branco absoluto (código da cor: 255).")
         + p("*Menor elemento em uma tela ao qual é possível atribuir-se uma cor.", classe="fonte")
         + p("Suponha que na figura estejam representados 25 <em>pixels</em> de uma tela.") + "[[fig:1]]"
         + p("A matriz numérica correspondente às cores da figura apresentada é dada por")
         + apoio("\\[\\begin{bmatrix} 255 & 0 & 127 & 0 & 255\\\\ 0 & 127 & 0 & 255 & 0\\\\ 127 & 0 & 255 & 0 & 127\\\\ 0 & 255 & 0 & 127 & 0\\\\ 255 & 0 & 127 & 0 & 255 \\end{bmatrix}\\]"))
PIXEL_IMG = figs(("q30", "Quadrado de 5 × 5 pixels em branco, preto e cinza, conforme a matriz: linha 1 branco, preto, cinza, preto, branco; linha 2 preto, cinza, preto, branco, preto; linha 3 cinza, preto, branco, preto, cinza; linha 4 preto, branco, preto, cinza, preto; linha 5 branco, preto, cinza, preto, branco."))
P30 = p("Uma matriz M = (a<sub><em>ij</em></sub>), quadrada de ordem 5, em que <em>i</em> representa o número da linha e <em>j</em> representa o número da coluna, é definida da seguinte forma:") \
      + apoio("\\[a_{ij} = \\begin{cases} 0, & \\text{se } i = j\\\\ 127, & \\text{se } i > j\\\\ 255, & \\text{se } i < j \\end{cases}\\]") \
      + p("A matriz M corresponde a uma matriz de cores em escala de cinza, descrita pelo texto, em uma tela.", "Sobre essa matriz de cores, pode-se afirmar que ela")

CIGARRA = (chamada("Leia o texto publicado em maio de 2013 para responder às questões de números 32 a 34.")
           + apoio("<strong>Os Estados Unidos se preparam para uma invasão de insetos após 17 anos</strong>",
                   *T(14, "Elas vivem a pelo menos 20 centímetros", "estratégia de sobrevivência para as cigarras.", ["Há mais de 170 espécies", "Um estudo brasileiro"]))
           + url("http://tinyurl.com/zh8daj6", "30.08.2016"))
CIGARRA = CIGARRA.replace("(Magicicada septendecim)", "(<em>Magicicada septendecim</em>)").replace("Brood II", "<em>Brood II</em>")
P32 = p(*T(14, "Suponha a existência de uma espécie C1", "elas emergirão juntas novamente no ano de", ["Se essas duas espécies"]))
P32 = P32.replace("C1", "C<sub>1</sub>").replace("C2", "C<sub>2</sub>")

GUO = (chamada("Leia o texto para responder às questões de números 45 a 47.")
       + apoio("<strong>Hormônio do crescimento de plantas é alvo de pesquisa chinesa</strong>",
               *T(19, "Um grupo de pesquisadores tem como principal objetivo", "outros fitormônios”, disse Guo.", ["“Um desses fitormônios", "“Temos estudado fatores", "“Identificamos que os fatores"]))
       + url("http://tinyurl.com/jrz82hw", "24.08.2016"))
P45 = p("Na caatinga brasileira, plantas como os mulungus (<em>Erythrina</em> spp.) são classificadas como caducifólias porque apresentam a perda sazonal das folhas.",
        "O hormônio e a adaptação diretamente relacionados a esse mecanismo fisiológico são, respectivamente,")

FUX = (chamada("Leia o texto de Jacques Fux para responder às questões de números 50 a 52.")
       + apoio("<strong>Literatura e Matemática</strong>", *T(20, "Letras e números costumam ser vistos", "poéticas e matemáticas.", ["A utilização da matemática", "Muitas passagens de Alice", "Explorar as relações"]))
       + url("http://tinyurl.com/h9z7jot", "17.08.2016"))
FUX = FUX.replace("Alice no País das Maravilhas", "<em>Alice no País das Maravilhas</em>").replace("Alice através do espelho", "<em>Alice através do espelho</em>")
P50 = p("Segundo o texto, pode-se afirmar que")

PESSANHA = (chamada("Leia o poema de Camilo Pessanha para responder às questões de números 53 e 54.")
            + apoio("<strong>INTERROGAÇÃO</strong>",
                    "Não sei se isto é amor. Procuro o teu olhar,<br>Se alguma dor me fere, em busca de um abrigo;<br>E apesar disso, crês? nunca pensei num lar<br>Onde fosses feliz, e eu feliz contigo.",
                    "Por ti nunca chorei nenhum ideal desfeito.<br>E nunca te escrevi nenhuns versos românticos.<br>Nem depois de acordar te procurei no leito,<br>Como a esposa sensual do Cântico dos Cânticos.",
                    "Se é amar-te não sei. Não sei se te idealizo<br>A tua cor sadia, o teu sorriso terno...<br>Mas sinto-me sorrir de ver esse sorriso<br>Que me penetra bem, como este sol de Inverno.",
                    "Passo contigo a tarde e sempre sem receio<br>Da luz crepuscular, que enerva, que provoca.<br>Eu não demoro o olhar na curva do teu seio<br>Nem me lembrei jamais de te beijar na boca.",
                    "Eu não sei se é amor. Será talvez começo.<br>Eu não sei que mudança a minha alma pressente...<br>Amor não sei se o é, mas sei que te estremeço,<br>Que adoecia talvez de te saber doente.")
            + fonte("(PESSANHA, Camilo. <em>Clepsidra</em>. São Paulo: Núcleo, 1989.)"))
P53 = p("O escritor português Camilo Pessanha faz parte da escola literária denominada Simbolismo.", "Assinale a alternativa que possui uma característica desse movimento artístico presente no poema.")

Q = {
1: {"materia": "Geografia", "assunto": "Trabalho e sociedade", "tags": MULTI + ["desigualdade de gênero"],
    "enunciado": GENERO + P1,
    "alternativas": AL(2, "(A) a recente incorporação das mulheres", "quando as funcionárias saem de licença."),
    "explicacao": "<p>Parte dos gestores ainda vê as mulheres como responsáveis pelo cuidado da família e supõe que elas faltam mais ao trabalho. Esse preconceito pesa em salários e promoções. Alternativa <strong>D</strong>.</p><p>As mulheres trabalham há muito tempo, e nenhuma Constituição “legalizou” isso (A). Elas são minoria na construção civil (B). A CLT não manda pôr a luta das mulheres em segundo plano (C). E a cultura brasileira é patriarcal, não matriarcal, e a licença não gera ganho ao empregador (E).</p>"},
2: {"materia": "Português", "assunto": "Coesão e referência", "tags": MULTI + ["conectivos", "reescrita"],
    "enunciado": p("O título do artigo – <em>Mais escolarizadas, mulheres ainda ganham menos e têm dificuldades de subir na carreira</em> – poderia ser substituído, sem causar prejuízo de sentido, por:"), "apoio_de": (1, P1),
    "alternativas": AL(2, "(A) Mulheres, mais escolarizadas, porventura", "porquanto já ganham mais."),
    "explicacao": "<p>B mantém tudo: “ainda ganham menos” e “bem como” (que soma, como o “e” original) “enfrentam obstáculos” (= têm dificuldades). Alternativa <strong>B</strong>.</p><p>A e D dizem que elas ganham mais ou o mesmo. C troca “ainda” por “às vezes” e cria uma relação de consequência (“por conseguinte”). E diz que já ganham mais e inverte a ideia.</p>"},
3: {"materia": "Matemática", "assunto": "Estatística", "tags": MULTI + ["média aritmética", "gráficos"],
    "enunciado": BH + P3, "imagens": BH_IMG,
    "alternativas": alts("1.378,05", "1.366,15", "1.354,25", "1.342,55", "1.330,75"),
    "explicacao": "<p>Média das mulheres: (1 312 + 1 323 + 1 278 + 1 410) ÷ 4 = 5 323 ÷ 4 = <strong>R$ 1.330,75</strong>. Alternativa <strong>E</strong>.</p>"},
4: {"materia": "Matemática", "assunto": "Operações e problemas", "tags": MULTI + ["fórmulas", "razão"],
    "enunciado": p("Índices ou coeficientes como o IDH ou o de Gini servem para que a comparação dos dados de países ou regiões seja realizada de modo mais objetivo.",
                   "Suponha que seja criado o Coeficiente de Desigualdade do Rendimento entre os Sexos, o CDRS. Quando o CDRS é igual a zero, há ausência de desigualdade de rendimento entre os sexos; quando o CDRS é igual a 1, a desigualdade é dita plena e, nesse caso, o rendimento dos homens supera em muito o rendimento das mulheres.",
                   "Para calcular o CDRS deve-se utilizar a seguinte fórmula:")
                 + apoio("\\[CDRS = 1 - \\left(\\frac{M \\cdot R_M}{H \\cdot R_H}\\right),\\]sendo:<br>• <em>M</em>, o número de mulheres de uma determinada região;<br>• <em>R<sub>M</sub></em>, a média mensal dos rendimentos das mulheres dessa região;<br>• <em>H</em>, o número de homens dessa mesma região; e<br>• <em>R<sub>H</sub></em>, a média mensal dos rendimentos dos homens dessa região.")
                 + p("Com base na série histórica dos rendimentos de homens e de mulheres, observou-se que a razão \\(\\dfrac{M \\cdot R_M}{H \\cdot R_H}\\) pertence ao intervalo real [0,1].",
                     "Admita que na região metropolitana de BH, em 2013, havia 1 200 000 mulheres e 1 000 000 de homens.", "O valor do CDRS para a região metropolitana de BH em 2013 é, aproximadamente, igual a"),
    "apoio_de": (3, P3),
    "alternativas": alts("0,12", "0,16", "0,20", "0,24", "0,28"),
    "explicacao": "<p>Em 2013: (1 200 000 × 1 410) ÷ (1 000 000 × 2 022) = 1,2 × 1 410 ÷ 2 022 ≈ 1 692 ÷ 2 022 ≈ 0,837. CDRS = 1 − 0,837 ≈ <strong>0,16</strong>. Alternativa <strong>B</strong>.</p><p>Esquecer o número de pessoas e usar só os salários dá 1 − 1 410/2 022 ≈ 0,30, fora das alternativas.</p>"},
5: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": MULTI + ["cartum"],
    "enunciado": p("Considere o cartum.") + "[[fig:1]]" + p("De acordo com o texto do cartum,"),
    "imagens": figs(("q05", "Cartum de Randy Glasbergen (2008): um chefe, sentado à mesa com um papel na mão, fala a um funcionário de pé: “The local business journal wants to do an article on the 10 most powerful women in our company. Quick, go hire 7 more women!” (O jornal de negócios local quer fazer uma matéria sobre as 10 mulheres mais poderosas da nossa empresa. Rápido, vá contratar mais 7 mulheres!)")),
    "alternativas": AL(4, "(A) a companhia demitiu sete mulheres.", "(E) a companhia contratou sete mulheres para o jornal."),
    "explicacao": "<p>O chefe manda “<em>go hire 7 more women</em>”: a empresa precisa contratar mais sete mulheres para ter dez a apresentar. O humor está em revelar que hoje ela tem só três. Alternativa <strong>B</strong>.</p><p>Ninguém foi demitido (A), o jornal não recusou nada (C), não compara mulheres e homens (D), e as contratações seriam para a empresa, não para o jornal (E).</p>"},
6: {"materia": "História", "assunto": "História contemporânea", "tags": MULTI + ["sufragismo"],
    "enunciado": p(" ".join(T(4, "A relação entre as mulheres e a política", "ao movimento sufragista.")), "A principal reivindicação das integrantes do movimento sufragista era o direito"),
    "alternativas": alts("à liberdade de culto.", "à guarda dos filhos.", "ao voto feminino.", "ao divórcio.", "ao aborto."),
    "explicacao": "<p>“Sufrágio” é voto. As sufragistas lutavam pelo <strong>direito de votar</strong>; no Reino Unido, ele veio em parte em 1918 e por completo em 1928. Alternativa <strong>C</strong>.</p>"},
7: {"materia": "Biologia", "assunto": "Fisiologia humana", "tags": MULTI + ["amamentação", "imunidade passiva"],
    "enunciado": p(" ".join(T(4, "No Brasil, as mulheres assalariadas", "para os mamíferos em geral, já que ela"))),
    "alternativas": {k: v.replace("Ca2+", "Ca<sup>2+</sup>") for k, v in AL(4, "(A) garante que as fêmeas engravidem", "que fortalecem o sistema imune dele.").items()},
    "explicacao": "<p>O leite materno transfere <strong>anticorpos</strong> (como a IgA) ao filhote: é a imunidade passiva natural, que o protege enquanto o sistema imune dele amadurece. Alternativa <strong>E</strong>.</p><p>A amamentação não garante gravidez nem impede ovulação de forma certa (A). Não previne doenças autoimunes com garantia (B). Não fornece organelas (C). E antígenos não digerem cátions (D).</p>"},
8: {"materia": "Química", "assunto": "Radioatividade", "tags": MULTI + ["fissão nuclear", "Lise Meitner"],
    "enunciado": p("Leia o texto.") + apoio(*T(5, "Lise Meitner, nascida na Áustria em 1878", "principal mulher cientista deste século”.", ["Embora Meitner não tenha"]))
                 + fonte("Fonte dos dados: KOTZ, J. e TREICHEL, P. <em>Química e Reações Químicas</em>. Rio de Janeiro. Editora LTC,1998. Adaptado.<br>FRANCO, Dalton. <em>Química, Cotidiano e Transformações</em>. São Paulo. Editora FTD,2015. Adaptado.")
                 + p("O número atômico do outro núcleo formado na fissão nuclear mencionada no texto é"),
    "alternativas": alts("34", "35", "36", "37", "38"),
    "explicacao": "<p>A carga se conserva: o nêutron não tem carga, então 92 = 56 + Z. Logo Z = <strong>36</strong> (criptônio). Alternativa <strong>C</strong>.</p><p>Pela massa: 235 + 1 = 141 + A + 3, então A = 92: o outro núcleo é o Kr-92.</p>"},
9: {"materia": "Física", "assunto": "Física moderna", "tags": MULTI + ["mulheres na ciência"],
    "enunciado": p("Leia o texto.") + apoio(*T(5, "A polonesa Maria Skodovska Curie", "elétrons e radiações eletromagnéticas.", ["No Brasil, na primeira metade"]))
                 + p("Podemos afirmar que algumas áreas da Física contempladas pelos estudos citados no texto são"),
    "alternativas": AL(5, "(A) Termologia e Radioatividade", "das radiações eletromagnéticas."),
    "explicacao": "<p>Raios cósmicos são estudados pela <strong>Astrofísica</strong>; radioatividade, mésons e elétrons pertencem à <strong>Física de Partículas</strong>. Alternativa <strong>D</strong>.</p><p>Raios cósmicos não são estudados pela temperatura (A). O texto não trata de magnetismo (B). Rádio e polônio são metais sólidos, não gases (C). E não houve observação astronômica com Óptica Geométrica (E).</p>"},
10: {"materia": "Raciocínio lógico", "assunto": "Sequências", "tags": ["padrões cíclicos"],
     "enunciado": p(" ".join(T(6, "Os números naturais de 0 a 3 000", "que mostra o começo do processo."))) + "[[fig:1]]" + p("Nessas condições, o número 2 017 está na"),
     "imagens": figs(("q10", "Tabela de 5 linhas em que os números descem e sobem em zigue-zague: 0 na 1ª linha, 1 na 2ª, 2 na 3ª, 3 na 4ª, 4 na 5ª, 5 na 4ª, 6 na 3ª, 7 na 2ª, 8 na 1ª, 9 na 2ª, 10 na 3ª, 11 na 4ª, 12 na 5ª, 13 na 4ª, 14 na 3ª, 15 na 2ª, 16 na 1ª, 17 na 2ª, 18 na 3ª, 19 na 4ª, 20 na 5ª, 21 na 4ª, 22 na 3ª, e assim por diante.")),
     "alternativas": alts("1ª linha.", "2ª linha.", "3ª linha.", "4ª linha.", "5ª linha."),
     "explicacao": "<p>O padrão se repete a cada 8 números (0 e 8 e 16 na 1ª linha). Os restos da divisão por 8 indicam a linha: resto 0 → 1ª; 1 ou 7 → 2ª; 2 ou 6 → 3ª; 3 ou 5 → 4ª; 4 → 5ª.</p><p>2 017 = 8 × 252 + 1: resto 1, então 2 017 fica na <strong>2ª linha</strong>, como o 1, o 9 e o 17. Alternativa <strong>B</strong>.</p>"},
11: {"materia": "Raciocínio lógico", "assunto": "Lógica", "tags": ["criptografia", "codificação"],
     "enunciado": apoio("Maria, aluna da Fatec Mococa, para garantir a segurança das mensagens que pretende transmitir, criou um sistema de criptografia da seguinte forma:<br>• montou uma tabela de 2 linhas e 13 colunas para colocar as 26 letras do alfabeto, sem repetição de letra;<br>• nas cinco células iniciais da 1ª linha, da esquerda para a direita, escreveu, uma a uma, as letras F, A, T, E, C, nessa ordem;<br>• ainda na 1ª linha, na 6ª célula, da esquerda para a direita, obedecendo a ordem alfabética (de A a Z), colocou a primeira letra ainda não utilizada nas células anteriores;<br>• da 7ª célula a 13ª célula da 1ª linha, inseriu sete letras, da esquerda para a direita, sem repetir letra, seguindo a ordem alfabética, começando pela primeira letra ainda não utilizada nas células anteriores;<br>• preencheu a 2ª linha, da esquerda para a direita, com as letras restantes do alfabeto, também em ordem alfabética e sem repetição de qualquer letra já utilizada anteriormente.")
                  + p("A tabela mostra o início do processo, com as seis primeiras letras.")
                  + tabela(["F", "A", "T", "E", "C", "B", "", "", "", "", "", "", ""], [["", "", "", "", "", "", "", "", "", "", "", "", ""]])
                  + p("Tendo construído a tabela conforme o descrito, para criptografar uma mensagem, Maria substitui cada letra da 1ª linha pela que está na 2ª linha, na mesma coluna, e vice-versa. A acentuação, a pontuação e o espaço entre as palavras são desconsiderados.",
                      "Assim, para desejar <strong>BOA PROVA</strong> para uma colega, que sabia fazer a decodificação, escreveu <strong>RTNEBTHN</strong>.", "Para João, que também sabia decodificar a mensagem, Maria escreveu:")
                  + apoio("<strong>A G A Q N E N B P S P N E B P A S P B</strong>") + p("A partir da decodificação, João entendeu que a mensagem de Maria foi"),
     "alternativas": alts("Nunca pare de aprender", "Nunca deixe de estudar", "Nunca faça isso de novo", "Sempre tire boas notas", "Sempre faça boas ações"),
     "explicacao": "<p>A tabela completa fica: 1ª linha F A T E C B D G H I J K L; 2ª linha M N O P Q R S U V W X Y Z. Trocando cada letra pela da mesma coluna: A↔N, G↔U, Q↔C, E↔P, B↔R, P↔E, S↔D.</p><p>AGAQN → NUNCA; EN → PA; BP → RE; SP → DE; NEBPASPB → APRENDER. Mensagem: “Nunca pare de aprender”. Alternativa <strong>A</strong>.</p>"},
12: {"materia": "Raciocínio lógico", "assunto": "Raciocínio espacial", "tags": ["rotação"],
     "enunciado": p(" ".join(T(7, "Em um círculo recortado em papel cartão", "permanece fixo na parede."))) + "[[fig:1]]"
                  + p("Considerando, inicialmente, a imagem do homem na posição da figura 1, obtém-se, após a roleta realizar uma rotação de três quartos de volta, no sentido horário, a figura representada em"),
     "imagens": figs(("q12", "Figura 1: roleta circular com um triângulo indicador fixo no alto e, no círculo, um homem estilizado em pé, feito de traços retos: cabeça quadrada vazada no alto, braços dobrados e pernas dobradas."),
                     ("q12a", "Alternativa A: o homem estilizado aparece deitado, girado de um quarto de volta."), ("q12b", "Alternativa B: o homem estilizado aparece deitado, girado de um quarto de volta, em outra disposição."),
                     ("q12c", "Alternativa C: o homem estilizado aparece deitado, girado de um quarto de volta, em outra disposição."), ("q12d", "Alternativa D: o homem estilizado aparece deitado, girado de um quarto de volta, em outra disposição."),
                     ("q12e", "Alternativa E: o homem estilizado aparece deitado, girado de um quarto de volta, em outra disposição.")),
     "alternativas": {"A": "[[fig:2]]", "B": "[[fig:3]]", "C": "[[fig:4]]", "D": "[[fig:5]]", "E": "[[fig:6]]"},
     "explicacao": "<p>Três quartos de volta no sentido horário levam ao mesmo lugar que um quarto de volta no sentido anti-horário. A cabeça, que estava no alto, vai para a <strong>esquerda</strong>, e os pés para a direita, sem espelhar o desenho. Alternativa <strong>E</strong> (gabarito oficial).</p><p>As outras alternativas mostram o giro no sentido oposto ou o desenho espelhado. Dica: gire o papel (ou a tela) um quarto de volta para a esquerda e compare.</p>"},
13: {"materia": "Raciocínio lógico", "assunto": "Lógica", "tags": ["negação", "quantificadores"],
     "enunciado": p("Considere que:") + apoio("• a sentença “Nenhum A é B” é equivalente a “Todo A é não B”;<br>• a negação da sentença “Todo A é B” é “Algum A é não B”;<br>• a negação da sentença “Algum A é B” é “Todo A é não B”.")
                  + p("Assim sendo, a negação da sentença “Nenhum nefelibata é pragmático” é"),
     "alternativas": AL(7, "(A) Todo nefelibata é não pragmático.", "(E) Algum não nefelibata é não pragmático."),
     "explicacao": "<p>“Nenhum nefelibata é pragmático” equivale a “Todo nefelibata é não pragmático”. Pela terceira regra, essa é a negação de “Algum nefelibata é pragmático”. Logo, a negação de “Nenhum...” é <strong>“Algum nefelibata é pragmático”</strong>. Alternativa <strong>C</strong>.</p><p>A é a própria sentença reescrita, não a negação. As outras falam de “não nefelibatas”, que a sentença original nem menciona.</p>"},
14: {"materia": "Raciocínio lógico", "assunto": "Operações e problemas", "tags": ["sistema de numeração decimal"],
     "enunciado": p(" ".join(T(7, "Seja N um número natural de dois algarismos", "de modo que N – M = 63.")), "A soma de todos os números naturais N que satisfazem as condições dadas é"),
     "alternativas": alts("156", "164", "173", "187", "198"),
     "explicacao": "<p>Se N = 10a + b e M = 10b + a, então N − M = 9(a − b) = 63, e a − b = 7. Com algarismos não nulos: N = 81 ou N = 92. Soma: 81 + 92 = <strong>173</strong>. Alternativa <strong>C</strong>.</p><p>O 70 não vale, porque o 0 é um algarismo nulo.</p>"},
15: {"materia": "História", "assunto": "América pré-colombiana", "tags": ["maias"],
     "enunciado": p(" ".join(T(8, "As misteriosas cidades e edificações", "dessa civilização, no século X.")), "Assinale a alternativa que apresenta corretamente as principais características da civilização maia."),
     "alternativas": AL(8, "(A) Desenvolveu-se na floresta Amazônica", "e da Lua (Anúbis)."),
     "explicacao": "<p>Os maias viveram no sul do México (Iucatã), na Guatemala e em Honduras, e desenvolveram calendário, matemática com o zero, astronomia e grandes pirâmides. Alternativa <strong>B</strong>.</p><p>A Amazônia não foi área maia (A). Machu Picchu e o imperador divino são incas (C). O Rio da Prata não tem relação com eles (D). E Rá e Anúbis são deuses egípcios (E).</p>"},
16: {"materia": "História", "assunto": "Idade Média", "tags": ["presença árabe na Península Ibérica"],
     "enunciado": p(" ".join(T(8, "No século VIII, tropas muçulmanas", "quase toda a península Ibérica.")), "Sobre o período de domínio muçulmano na península Ibérica, é correto afirmar que"),
     "alternativas": AL(8, "(A) contribuiu para a consolidação do feudalismo", "manifestações literárias e musicais pagãs."),
     "explicacao": "<p>A Al-Andalus muçulmana foi um centro de comércio e de cultura: Córdoba e Toledo cresceram, com bibliotecas, poetas, médicos e tradutores. Alternativa <strong>B</strong>.</p><p>O domínio muçulmano estimulou cidades e comércio, ao contrário do feudalismo (A). Durou quase oito séculos (até 1492, em Granada), e não meio século ou trinta anos (C e D). E estimulou a ciência e as artes (E).</p>"},
17: {"materia": "História", "assunto": "História contemporânea", "tags": ["descolonização da África"],
     "enunciado": p(" ".join(T(8, "Após ser repartida e colonizada", "maior parte dos países do continente.")), "Esses processos, no contexto da Descolonização da África, têm como características comuns e principais"),
     "alternativas": AL(8, "(A) o desenvolvimento de teorias raciais", "perda do controle europeu sobre as colônias na África."),
     "explicacao": "<p>Depois da Segunda Guerra, as metrópoles europeias saíram enfraquecidas, enquanto cresciam os movimentos de libertação na África. Alternativa <strong>E</strong>.</p><p>Não houve guerra contra os EUA (A). A URSS apoiou alguns movimentos, mas não houve industrialização rápida (B). Missionários e a ONU não foram o motor principal (C). E não havia mercado internacional de escravos no século XX (D).</p>"},
18: {"materia": "História", "assunto": "Brasil Império", "tags": ["Período Regencial"],
     "enunciado": p("Leia o texto.") + apoio(" ".join(T(9, "Em abril de 1831, Dom Pedro I abdicou", "pudesse ser coroado."))) + p("Durante o Período Regencial, a política brasileira foi marcada"),
     "alternativas": AL(9, "(A) pela intensificação da política expansionista", "(caso da Guerra dos Farrapos)."),
     "explicacao": "<p>O Ato Adicional (1834) criou as <strong>Assembleias Legislativas Provinciais</strong>, e o período teve várias revoltas: Cabanagem (popular), Farroupilha (elites gaúchas), Sabinada, Balaiada. Alternativa <strong>E</strong>.</p><p>A Guerra do Paraguai é de 1864–70 (A). A Cisplatina se separou em 1828, ainda no Primeiro Reinado (B). O imperador era criança e não governava (C). E a Constituição é de 1824, sem voto para analfabetos (D).</p>"},
19: {"materia": "História", "assunto": "Entreguerras", "tags": ["crise de 1929"],
     "enunciado": p("Leia o texto.") + apoio(" ".join(T(9, "O dia 24 de outubro de 1929 marca", "a crise se espalhou para diversos países."))) + p("Entre os fatores causadores da crise destacam-se"),
     "alternativas": AL(9, "(A) a ascensão de regimes nazifascistas", "por parte dos integrantes da Zona do Euro."),
     "explicacao": "<p>A crise de 1929 nasceu da superprodução: a economia dos EUA produzia mais do que o mercado consumia, e a Europa recuperada passou a comprar menos. Os estoques cresceram, os lucros caíram, e a especulação na bolsa estourou. Alternativa <strong>B</strong>.</p><p>O nazismo chegou ao poder depois da crise, e os BRICS são do século XXI (A). Os EUA saíram fortalecidos da Primeira Guerra (C). D e E são anacrônicas (Zona do Euro, substituição de importações asiática).</p>"},
20: {"materia": "Química", "assunto": "Estrutura atômica", "tags": ["nêutrons", "isótopos"],
     "enunciado": AMIGOS + P20,
     "alternativas": alts("Júlia.", "Paulo.", "Pedro.", "Gabriela.", "Fernanda."),
     "explicacao": "<p>Nêutrons = massa − número atômico. Fe: 56 − 26 = <strong>30</strong>; O: 8; Ca: 20; Li: 4; Cℓ: 18. Venceu Fernanda. Alternativa <strong>E</strong>.</p>"},
21: {"materia": "Química", "assunto": "Cálculos químicos", "tags": ["estequiometria"],
     "enunciado": p("Os isótopos representados contidos nos cartões de Paulo e Gabriela podem reagir entre si para formar óxido de lítio, segundo a reação balanceada")
                  + apoio("\\[4\\,\\text{Li}(\\text{s}) + \\text{O}_2(\\text{g}) \\rightarrow 2\\,\\text{Li}_2\\text{O}(\\text{s})\\]") + p("A massa de lítio necessária para reagir completamente com 3,2 kg de oxigênio é, em quilogramas,")
                  + apoio("Massas molares:<br>Li: 7 g/mol<br>O: 16 g/mol"),
     "apoio_de": (20, P20),
     "alternativas": alts("1,4", "1,8", "2,8", "4,3", "7,1"),
     "explicacao": "<p>3,2 kg de O₂ = 3 200 g ÷ 32 g/mol = 100 mol de O₂. A proporção é 4 Li para 1 O₂: 400 mol de Li × 7 g/mol = 2 800 g = <strong>2,8 kg</strong>. Alternativa <strong>C</strong>.</p><p>Usar a massa molar do O (16) em vez da do O₂ (32) dá 5,6 kg; esquecer o fator 4 dá 0,7 kg.</p>"},
22: {"materia": "Química", "assunto": "Ligações químicas", "tags": ["ligação iônica"],
     "enunciado": p("A ligação química que ocorre na combinação entre os isótopos apresentados por Júlia e Pedro é"), "apoio_de": (20, P20),
     "alternativas": alts("iônica, e a fórmula do composto formado é CaC<em>ℓ</em>.", "iônica, e a fórmula do composto formado é CaC<em>ℓ</em><sub>2</sub>.", "covalente, e a fórmula do composto formado é C<em>ℓ</em>Ca.",
                          "covalente, e a fórmula do composto formado é Ca<sub>2</sub>C<em>ℓ</em>.", "covalente, e a fórmula do composto formado é CaC<em>ℓ</em><sub>2</sub>."),
     "explicacao": "<p>Cálcio (metal, grupo 2) perde 2 elétrons: Ca²⁺. Cloro (não metal, grupo 17) ganha 1: Cℓ⁻. Metal com não metal forma ligação <strong>iônica</strong>, e as cargas pedem dois cloros para cada cálcio: <strong>CaCℓ₂</strong>. Alternativa <strong>B</strong>.</p>"},
23: {"materia": "Química", "assunto": "Radioatividade", "tags": ["meia-vida"],
     "enunciado": p("Leia o texto.") + apoio(*T(10, "Um dos piores acidentes nucleares", "eliminação pelo corpo humano.", ["O Sr–90 é um beta emissor"])) + url("http://tinyurl.com/jzljzwc", "30.08.2016")
                  + p("Em 2016, em relação à quantidade de Sr–90 liberada no acidente, a quantidade de Sr–90 que se transformou em Y–90 foi, aproximadamente, de"),
     "alternativas": alts("\\(\\dfrac{1}{8}\\)", "\\(\\dfrac{1}{6}\\)", "\\(\\dfrac{1}{5}\\)", "\\(\\dfrac{1}{4}\\)", "\\(\\dfrac{1}{2}\\)"),
     "explicacao": "<p>De 1986 a 2016 passaram 30 anos, cerca de uma meia-vida (28 anos). Em uma meia-vida, <strong>metade</strong> do Sr-90 se transforma em Y-90. Alternativa <strong>E</strong>.</p>"},
24: {"materia": "Química", "assunto": "Funções orgânicas", "tags": ["feromônios"],
     "enunciado": p("Leia o texto.") + apoio(" ".join(T(11, "Feromônios são substâncias químicas secretadas", "atuam como feromônios."))) + url("http://tinyurl.com/hqfrxbb", "17.09.2016")
                  + p("As fórmulas estruturais do androstenol e da copulina encontram-se representadas") + "[[fig:1]]"
                  + p("As funções orgânicas oxigenadas encontradas no androstenol e na copulina são, respectivamente,"),
     "imagens": figs(("q24", "Fórmulas estruturais. Androstenol: esqueleto de esteroide (quatro anéis fundidos, um deles com ligação dupla) com um grupo OH ligado a um carbono do primeiro anel, que não é aromático. Copulina: cadeia CH₃–CH₂–CH₂–C(=O)–OH.")),
     "alternativas": alts("fenol e ácido carboxílico.", "álcool e ácido carboxílico.", "álcool e aldeído.", "álcool e cetona.", "fenol e éster."),
     "explicacao": "<p>No androstenol, o OH está num carbono saturado de anel não aromático: <strong>álcool</strong>. Na copulina, o grupo C(=O)OH é de <strong>ácido carboxílico</strong>. Alternativa <strong>B</strong>.</p><p>Fenol exige OH em anel aromático (A e E). Aldeído e cetona não têm OH no carbono da carbonila (C e D).</p>"},
25: {"materia": "Inglês", "assunto": "Interpretação de texto",
     "enunciado": WORK + P25,
     "alternativas": AL(12, "(A) afirma discordar de pesquisas", "que trabalham na indústria de óleo."),
     "explicacao": "<p>“<em>I’m having a hard time starting this article</em>” = “Estou com dificuldade para começar este artigo”. Alternativa <strong>C</strong>.</p><p>“<em>Burning the midnight oil</em>” é expressão idiomática para “trabalhar até tarde”, não tem a ver com petróleo (D e E) nem com trabalhar melhor à meia-noite (B).</p>"},
26: {"materia": "Inglês", "assunto": "Interpretação de texto",
     "enunciado": p("A respeito do autor, o primeiro parágrafo nos informa que ele"), "apoio_de": (25, P25),
     "alternativas": AL(12, "(A) trabalha pouco para a idade dele.", "na metade do ano."),
     "explicacao": "<p>“<em>I’m middle-aged and work too much</em>”: ele é de meia-idade e trabalha demais. Alternativa <strong>B</strong>.</p><p><em>Middle-aged</em> é “de meia-idade”, não “Idade Média” (D) nem “metade do ano” (E).</p>"},
27: {"materia": "Inglês", "assunto": "Interpretação de texto",
     "enunciado": p("Considere a afirmação: “<em>Our study highlights that too much work can have adverse effects on cognitive functioning.</em>”", "Um dos efeitos adversos do trabalho excessivo apresentado pelo autor é"), "apoio_de": (25, P25),
     "alternativas": AL(12, "(A) não lembrar do que almoçara.", "pelo uso prolongado do computador."),
     "explicacao": "<p>O autor fala de quem fica olhando para a tela “<em>unable to remember what they had for lunch</em>”, sem lembrar o que almoçou. Alternativa <strong>A</strong>.</p><p>O texto não fala de solidão (B e C), escrita à mão (D) nem luz forte (E).</p>"},
28: {"materia": "Inglês", "assunto": "Interpretação de texto",
     "enunciado": p("Afirma-se, no terceiro parágrafo, que"), "apoio_de": (25, P25),
     "alternativas": AL(12, "(A) o tratamento de doenças decorrentes", "afetam a saúde física e mental dos empregados."),
     "explicacao": "<p>“<em>For some employees, of course – the average resident physician (...) – long hours are a fact of modern working life</em>”: para médicos residentes, jornadas longas fazem parte do trabalho. Alternativa <strong>D</strong>.</p><p>O texto não compara custos de tratamento (A) nem jornadas de médicos e economistas (B). E diz que o excesso de trabalho afeta a saúde física e mental (C e E).</p>"},
29: {"materia": "Inglês", "assunto": "Pronomes", "tags": ["pronomes relativos"],
     "enunciado": p("O pronome relativo <em>that</em>, em “<em>that tracks the well-being of 6,000 Australians</em>”, pode ser corretamente substituído, sem alteração do sentido original, por"), "apoio_de": (25, P25),
     "alternativas": {k: f"<em>{v[:-1]}</em>." for k, v in alts("wit.", "with.", "wish.", "witch.", "which.").items()},
     "explicacao": "<p>O <em>that</em> retoma “<em>survey</em>” (uma coisa) e pode ser trocado por <strong><em>which</em></strong>, o pronome relativo para coisas. Alternativa <strong>E</strong>.</p><p>As outras palavras só se parecem na grafia: <em>wit</em> (perspicácia), <em>with</em> (com), <em>wish</em> (desejo), <em>witch</em> (bruxa).</p>"},
}

Q.update({
30: {"materia": "Matemática", "assunto": "Matrizes", "tags": ["lei de formação"],
     "enunciado": PIXEL + P30, "imagens": PIXEL_IMG,
     "alternativas": {k: v.replace("pixels", "<em>pixels</em>") for k, v in AL(13, "(A) terá o mesmo número de pixels brancos e cinzas.", "(E) terá uma diagonal com cinco pixels cinzas.").items()},
     "explicacao": "<p>Na matriz 5 × 5: a diagonal principal (i = j) tem 5 elementos iguais a 0 (pretos). Acima dela (i &lt; j) há 10 elementos iguais a 255 (brancos) e abaixo (i &gt; j) há 10 iguais a 127 (cinzas). Então há o mesmo número de brancos e cinzas: 10 e 10. Alternativa <strong>A</strong>.</p><p>A diagonal principal tem cinco pretos, não brancos nem cinzas (D e E).</p>"},
31: {"materia": "Matemática", "assunto": "Análise combinatória", "tags": ["princípio multiplicativo", "potências"],
     "enunciado": p("O número máximo de matrizes distintas que podem ser formadas com 25 <em>pixels</em> de tamanho, em que se possa preencher cada pixel com qualquer uma dentre as 256 cores da escala de cinza, é igual a"),
     "apoio_de": (30, P30),
     "alternativas": alts("255<sup>256</sup>", "127<sup>25</sup>", "25<sup>25</sup>", "256<sup>25</sup>", "0<sup>256</sup>"),
     "explicacao": "<p>Cada um dos 25 <em>pixels</em> tem 256 opções de cor, independentes: 256 × 256 × ... (25 vezes) = <strong>256<sup>25</sup></strong>. Alternativa <strong>D</strong>.</p><p>A inverte base e expoente (e ainda usa 255). E 0<sup>256</sup> = 0 (E).</p>"},
32: {"materia": "Matemática", "assunto": "Operações e problemas", "tags": ["MMC", "números primos"],
     "enunciado": CIGARRA + P32,
     "alternativas": alts("2271.", "2237.", "2145.", "2033.", "2029."),
     "explicacao": "<p>Como 13 e 17 são primos entre si, o MMC é 13 × 17 = 221. As espécies voltam a emergir juntas 221 anos depois: 2016 + 221 = <strong>2237</strong>. Alternativa <strong>B</strong>.</p><p>2033 e 2029 são só o próximo ano de cada espécie isolada (D e E).</p>"},
33: {"materia": "Matemática", "assunto": "Geometria plana", "tags": ["área", "notação científica"],
     "enunciado": p(*T(14, "O texto afirma que os habitantes das áreas", "sem sobreposição de indivíduos.", ["Imagine que 30 bilhões"]),
                    "Considerando que a área ocupada por uma cigarra dessa espécie é igual a 7 × 10<sup>–4</sup> metros quadrados, então N quilômetros dessa estrada ficarão ocupados por essa população.", "O menor valor de N será igual a"),
     "apoio_de": (32, P32),
     "alternativas": alts("2,1", "21", "210", "2 100", "21 000"),
     "explicacao": "<p>Área total: 3 × 10¹⁰ × 7 × 10⁻⁴ = 2,1 × 10⁷ m². Com 10 m de largura, o comprimento é 2,1 × 10⁶ m = <strong>2 100 km</strong>. Alternativa <strong>D</strong>.</p><p>Esquecer de converter metros em quilômetros dá 2,1 milhões.</p>"},
34: {"materia": "Matemática", "assunto": "Sequências", "tags": ["progressão aritmética"],
     "enunciado": p("Com relação à Ninhada II, e adotando o ano de 1996 como o 1º termo (a<sub>1</sub>) de uma Progressão Aritmética, a expressão algébrica que melhor representa o termo geral (a<sub>n</sub>) da sequência de anos em que essas cigarras sairão à superfície, com \\(n \\in \\mathbb{N}^*\\), é dada por"),
     "apoio_de": (32, P32),
     "alternativas": alts("a<sub>n</sub> = 17 n + 1979", "a<sub>n</sub> = 17 n + 1998", "a<sub>n</sub> = 17 n + 2013", "a<sub>n</sub> = 1996 n + 17", "a<sub>n</sub> = 1979 n + 17"),
     "explicacao": "<p>a<sub>n</sub> = a<sub>1</sub> + (n − 1)r = 1996 + 17(n − 1) = <strong>17n + 1979</strong>. Alternativa <strong>A</strong>.</p><p>Confira: n = 1 dá 1996, e n = 2 dá 2013, o ano da reportagem.</p>"},
35: {"materia": "Física", "assunto": "Cinemática", "tags": ["velocidade média"],
     "enunciado": p(" ".join(T(15, "A tabela apresenta dados extraídos", "Jogos Olímpicos Modernos no Rio de Janeiro.")))
                  + tabela(["Revezamento da Tocha Olímpica", ""], [["Duração", "95 dias"], ["Percurso Terrestre Total", "20 000 km"], ["Percurso Aéreo Total", "10 000 milhas (≅ 16 000 km)"]])
                  + fonte("Fonte dos dados: &lt;http://tinyurl.com/zf326a5&gt; Acesso em: 23.09.2016.")
                  + p("Utilizando como base apenas as informações fornecidas na tabela, podemos dizer que a velocidade média da Tocha Olímpica ao longo de todo percurso é, em km/h, aproximadamente, igual a") + apoio("Dado:<br>1 dia = 24 h"),
     "alternativas": alts("3,2 × 10<sup>2</sup>", "1,6 × 10<sup>1</sup>", "8,8 × 10<sup>0</sup>", "7,0 × 10<sup>0</sup>", "4,4 × 10<sup>0</sup>"),
     "explicacao": "<p>Distância total: 20 000 + 16 000 = 36 000 km. Tempo: 95 × 24 = 2 280 h. v = 36 000 ÷ 2 280 ≈ 15,8 ≈ <strong>1,6 × 10¹ km/h</strong>. Alternativa <strong>B</strong>.</p><p>Usar só o percurso terrestre dá 8,8 km/h (C), e só o aéreo, 7,0 km/h (D).</p>"},
36: {"materia": "Física", "assunto": "Energia", "tags": ["análise dimensional", "potência"],
     "enunciado": p(" ".join(T(15, "Sabe-se que a grandeza física potência", "a fórmula dimensional da potência é"))),
     "alternativas": alts("M L T", "M L<sup>2</sup> T", "M L<sup>2</sup> T<sup>2</sup>", "M L<sup>2</sup> T<sup>–2</sup>", "M L<sup>2</sup> T<sup>–3</sup>"),
     "explicacao": "<p>Energia (trabalho) = força × distância = (M L T⁻²) × L = M L² T⁻². Potência = energia ÷ tempo = <strong>M L² T⁻³</strong>. Alternativa <strong>E</strong>.</p><p>M L² T⁻² é a fórmula da energia, não da potência (D).</p>"},
37: {"materia": "Física", "assunto": "Eletrodinâmica", "tags": ["lei de Ohm", "gráficos"],
     "enunciado": p(" ".join(T(16, "Em uma disciplina de circuitos elétricos", "apresentada na figura."))) + "[[fig:1]]"
                  + p("Com os dados obtidos pelos alunos, e considerando apenas o trecho com comportamento ôhmico, podemos afirmar que o valor encontrado para a resistência elétrica foi, em kΩ, de"),
     "imagens": figs(("q37", "Gráfico “Curva Característica de Dispositivo Resistivo”: U (V) × i (mA). De 0 a 10 mA é uma reta: (2; 6), (4; 12), (6; 18), (8; 24), (10; 30). Depois a curva se achata: (12; 34), (14; 36), (16; 37), (18; 38), (20; 38).")),
     "alternativas": alts("3,0", "1,5", "0,8", "0,3", "0,1"),
     "explicacao": "<p>No trecho reto (ôhmico): R = U ÷ i = 30 V ÷ 10 mA = 30 ÷ 0,010 = 3 000 Ω = <strong>3,0 kΩ</strong>. Alternativa <strong>A</strong>.</p><p>Esquecer que a corrente está em miliampères dá 3 Ω.</p>"},
38: {"materia": "Física", "assunto": "Cinemática", "tags": ["lançamento oblíquo"],
     "enunciado": p(" ".join(T(16, "Em um jogo de futebol, o goleiro", "em 4 segundos."))) + "[[fig:1]]"
                  + p("Desprezando a resistência do ar e com base nas informações apresentadas, podemos concluir que os módulos da velocidade \\(\\vec{V}\\), de lançamento, e da velocidade \\(\\vec{V}_H\\), na altura máxima, são, em metros por segundos, iguais a, respectivamente,")
                  + apoio("Dados:<br>sen β = 0,8;<br>cos β = 0,6."),
     "imagens": figs(("q38", "Goleiro lança a bola com velocidade V, formando o ângulo β com a horizontal. A bola descreve uma parábola e cai 60 m adiante; no ponto mais alto, a velocidade é horizontal, V_H.")),
     "alternativas": alts("15 e 25.", "15 e 50.", "25 e 15.", "25 e 25.", "25 e 50."),
     "explicacao": "<p>Na horizontal o movimento é uniforme: V<sub>H</sub> = 60 m ÷ 4 s = <strong>15 m/s</strong>. Essa é a componente horizontal: V · cos β = 15, então V = 15 ÷ 0,6 = <strong>25 m/s</strong>. No ponto mais alto, só resta a componente horizontal: 15 m/s. Alternativa <strong>C</strong>.</p><p>A inverte a ordem pedida.</p>"},
39: {"materia": "Física", "assunto": "Energia", "tags": ["rendimento"],
     "enunciado": p(*T(17, "Um professor do curso de Eletrônica Industrial", "o valor da dissipação de energia.", ["Os dados são apresentados"])).replace("smartphone", "<em>smartphone</em>").replace("Bluetooth", "<em>Bluetooth</em>").replace("Near Field Communication", "<em>Near Field Communication</em>") + "[[fig:1]]"
                  + p("Desprezando quaisquer outras perdas do sistema, e considerando apenas as informações apresentadas no texto e no infográfico, é correto afirmar que"),
     "imagens": figs(("q39", "Infográfico “Consumo de Energia em Celular”: uma bateria de 15 Wh alimenta um celular que usa 12 Wh (com ícones de WiFi, Bluetooth, brilho, NFC, 3G, 4G, GPS, vibração e apps); setas mostram 3 Wh dissipados.")),
     "alternativas": {k: v.replace("Bluetooth", "<em>Bluetooth</em>").replace("NFC", "<em>NFC</em>") for k, v in AL(17, "(A) o rendimento do sistema é de 25%.", "são as maiores consumidoras de energia.").items()},
     "explicacao": "<p>Rendimento = energia útil ÷ energia fornecida = 12 Wh ÷ 15 Wh = 0,8 = <strong>80%</strong>. Alternativa <strong>B</strong>.</p><p>25% seria 3 ÷ 12, a razão entre dissipação e uso (A). O infográfico não informa potência em 1,5 h (C). A dissipação depende das funções usadas (D). E o infográfico não compara o consumo de cada função (E).</p>"},
40: {"materia": "Geografia", "assunto": "Industrialização", "tags": ["CSN", "Era Vargas"],
     "enunciado": p(" ".join(T(17, "A Companhia Siderúrgica Nacional (CSN)", "Segunda Guerra Mundial.")), "Essa siderúrgica foi construída no município de"),
     "alternativas": AL(17, "(A) Cubatão, localizado no estado de São Paulo", "que abasteciam os fornos da companhia."),
     "explicacao": "<p>A CSN foi instalada em <strong>Volta Redonda</strong> (RJ), no vale do Paraíba, entre Rio e São Paulo e com acesso ao minério de Minas Gerais. Alternativa <strong>C</strong>.</p><p>Em Cubatão foi construída a Cosipa, nos anos 1960 (A). Carajás só foi explorado a partir dos anos 1980 (B). E a capital em 1941 era o Rio de Janeiro, não Salvador (E).</p>"},
41: {"materia": "Geografia", "assunto": "Cartografia", "tags": ["mapa de uso do solo"],
     "enunciado": p(" ".join(T(17, "A cartografia temática trata da representação", "determinado espaço geográfico.")), " ".join(T(17, "O mapa de uso e ocupação do solo é elaborado", "amplamente empregado no planejamento"))),
     "alternativas": AL(17, "(A) agrícola, pois nesse mapa está indicada", "no subsolo de uma determinada área."),
     "explicacao": "<p>O mapa de uso e ocupação do solo mostra como o território está sendo usado (áreas urbanas, agrícolas, matas etc.) e serve para orientar a <strong>expansão das cidades</strong>. Alternativa <strong>D</strong>.</p><p>Profundidade e fertilidade do solo são temas de mapas pedológicos (A e B). Chuva é tema de mapa climático (C). E equipamentos no subsolo não aparecem em imagens de satélite (E).</p>"},
42: {"materia": "Geografia", "assunto": "Geopolítica", "tags": ["Brexit", "União Europeia"],
     "enunciado": p("Leia o texto.") + apoio(*T(18, "No dia 23 de junho de 2016, o Reino Unido", "direitos e obrigações que daí decorrem.“", ["Representantes de diversos órgãos", "“...trata-se de uma situação", "Aguardamos agora que", "Estamos prontos para lançar"]))
                  + url("http://tinyurl.com/h5szb75", "05.10.2016")
                  + p("Oficialmente, o referendo não torna obrigatória a saída do Reino Unido da UE. Caso esse processo se concretize, pode-se afirmar corretamente que a UE"),
     "alternativas": AL(18, "(A) retirará do Reino Unido as prerrogativas", "Estados-Membros que ainda compõem a UE."),
     "explicacao": "<p>Saindo, o Reino Unido perde os direitos de membro, como o comércio sem tarifas com os demais países do bloco. Alternativa <strong>A</strong>.</p><p>A UE continua como mercado comum entre os 27 (B). O Reino Unido nunca adotou o euro, e o marco alemão não existe mais (C). A Escócia faz parte do Reino Unido e não é república (D). E o Banco Central Europeu e o euro continuam (E).</p>"},
43: {"materia": "Geografia", "assunto": "Geopolítica", "tags": ["Estado Islâmico", "Oriente Médio"],
     "enunciado": p("Leia o texto.") + apoio(*T(18, "O Estado Islâmico no Iraque e no Levante", "ter atingido a sua meta.", ["Em 29 de junho de 2014"]))
                  + fonte("(FOTTORINO, Éric (org.). <em>Quem é o Estado Islâmico?</em> Belo Horizonte: Autêntica Editora, 2016. p. 115 e 116. Adaptado.)")
                  + p("Atualmente, essa organização possui o controle territorial de"),
     "alternativas": AL(18, "(A) cidades isoladas, em sua maioria no vale", "comercializado no mercado paralelo."),
     "explicacao": "<p>Em 2016, o Estado Islâmico controlava cidades e áreas no vale do Eufrates, entre Síria e Iraque, mas não era reconhecido como país. Alternativa <strong>A</strong>.</p><p>Os EUA combatiam o grupo (B). Nenhum país o reconheceu (C), nem a ONU (D). E Irã e China não tinham áreas sob seu controle (E).</p><p>Observação: a questão é de 2016. O Estado Islâmico perdeu seus últimos territórios na Síria e no Iraque em 2019.</p>"},
44: {"materia": "Geografia", "assunto": "Climatologia", "tags": ["climograma", "domínios morfoclimáticos"],
     "enunciado": p("Analise o climograma.") + "[[fig:1]]" + p("Assinale a alternativa que apresenta corretamente o nome do domínio morfoclimático com as características representadas no climograma."),
     "imagens": figs(("q44", "Climograma: barras de pluviosidade mensal entre cerca de 220 mm (fevereiro e novembro) e 420 mm (maio), sempre acima de 200 mm; linha de temperatura quase constante, em torno de 25 °C o ano inteiro.")),
     "alternativas": alts("Pradaria", "Cerrado", "Caatinga", "Araucária", "Amazônico"),
     "explicacao": "<p>Chuva alta o ano todo (mais de 200 mm em todos os meses) e temperatura quase constante perto de 25 °C: clima equatorial, do domínio <strong>Amazônico</strong>. Alternativa <strong>E</strong>.</p><p>Cerrado e Caatinga têm estação seca marcada (B e C). Pradaria e Araucária têm temperaturas mais baixas e variação maior ao longo do ano (A e D).</p>"},
45: {"materia": "Biologia", "assunto": "Botânica", "tags": ["fitormônios", "caducifólia"],
     "enunciado": GUO + P45,
     "alternativas": AL(19, "(A) ácido abcísico e aumento da transpiração.", "(E) giberelina e aumento da fotossíntese."),
     "explicacao": "<p>O <strong>etileno</strong> promove a abscisão (queda) das folhas. Sem folhas na estação seca, a planta <strong>perde menos água por transpiração</strong>. Alternativa <strong>D</strong>.</p><p>A perda de folhas diminui a transpiração, não aumenta (A e C). Auxina retarda a queda das folhas (B). E sem folhas a fotossíntese cai (E).</p>"},
46: {"materia": "Biologia", "assunto": "Genética", "tags": ["transcrição", "fatores de transcrição"],
     "enunciado": p(*T(19, "Fatores de transcrição como o EIN3 e EIL1", "quando comparadas às demais células,", ["Caso a equipe de pesquisadores"])), "apoio_de": (45, P45),
     "alternativas": AL(19, "(A) maior concentração de DNA.", "(E) menor concentração de RNA."),
     "explicacao": "<p>Sem os fatores de transcrição, a RNA-polimerase não se liga a certos genes, e eles deixam de ser transcritos: a célula passa a ter <strong>menos RNA</strong>. Alternativa <strong>E</strong>.</p><p>A quantidade de DNA não muda (A). E não há base para prever mais clorofila, mais cloroplastos ou menos celulose (B, C e D).</p>"},
47: {"materia": "Biologia", "assunto": "Evolução", "tags": ["cladograma", "algas"],
     "enunciado": p("Considere o cladograma a seguir.") + "[[fig:1]]"
                  + p("Suponha que uma via bioquímica relacionada ao etileno tenha sido encontrada em diversas ordens de plantas terrestres e algas vermelhas, mas não em algas pardas.", "De acordo com o cladograma, essa via bioquímica deveria ser encontrada em algas verdes, dado que essas algas são"),
     "apoio_de": (45, P45),
     "imagens": figs(("q47", "Cladograma com quatro ramos: algas pardas (separam-se primeiro), algas vermelhas, algas verdes e plantas terrestres. Algas verdes e plantas terrestres saem do último nó em comum.")),
     "alternativas": AL(20, "(A) mais aparentadas às algas pardas", "(E) mais evoluídas que as algas pardas."),
     "explicacao": "<p>No cladograma, as algas verdes estão no grupo que reúne algas vermelhas e plantas terrestres, e não as pardas. Se a via existe nas vermelhas e nas plantas terrestres, ela provavelmente surgiu num ancestral comum que também deu origem às algas verdes. Alternativa <strong>B</strong>.</p><p>As algas pardas são as mais distantes (A). Grupos atuais não são intermediários nem ancestrais de outros atuais (C e D). E não existe “mais evoluído” (E).</p>"},
48: {"materia": "Biologia", "assunto": "Seres vivos", "tags": ["artrópodes", "aracnídeos"],
     "enunciado": p(" ".join(T(20, "Após a detecção de animais de uma determinada espécie", "tratar-se de um gênero hematófago.")), "O laudo dos técnicos indicou que os animais encontrados no galpão fazem parte de uma espécie de"),
     "alternativas": alts("aranhas.", "baratas.", "carrapatos.", "morcegos.", "pernilongos."),
     "explicacao": "<p>Exoesqueleto, quelíceras e quatro pares de patas são características de aracnídeos. Do tamanho de uma lentilha e hematófago (alimenta-se de sangue): <strong>carrapato</strong>. Alternativa <strong>C</strong>.</p><p>Aranhas não são hematófagas (A). Baratas e pernilongos são insetos, com três pares de patas e sem quelíceras (B e E). Morcegos são mamíferos (D).</p>"},
49: {"materia": "Biologia", "assunto": "Genética", "tags": ["herança ligada ao sexo"],
     "enunciado": p("Leia o texto para responder à questão de número 49.") + apoio(*T(20, "Em uma espécie de felídeos, uma alteração", "da mesma espécie de felídeos.", ["Em um determinado zoológico"]))
                  + p(" ".join(T(20, "A probabilidade de que o filhote desse acasalamento", "recombinações gênicas, é de"))),
     "alternativas": alts("0%", "25%", "50%", "75%", "100%"),
     "explicacao": "<p>A fêmea é X<sup>R</sup>X<sup>r</sup> e o macho, X<sup>r</sup>Y. Filhotes possíveis, com a mesma chance: X<sup>R</sup>X<sup>r</sup> (fêmea rugidora), X<sup>r</sup>X<sup>r</sup> (fêmea que não ruge), X<sup>R</sup>Y (macho rugidor), X<sup>r</sup>Y (macho que não ruge). Fêmea rugidora: 1 em 4 = <strong>25%</strong>. Alternativa <strong>B</strong>.</p><p>50% seria a chance de uma <em>fêmea</em> ser rugidora (sabendo que é fêmea), não a de o filhote ser fêmea e rugidora (C).</p>"},
50: {"materia": "Português", "assunto": "Interpretação de texto",
     "enunciado": FUX + P50,
     "alternativas": AL(21, "(A) a separação entre Literatura e Matemática tem origem", "de maneira integrada e produtiva."),
     "explicacao": "<p>O texto diz que a matemática amplia as possibilidades criativas da literatura e fala no “encontro de todas as ciências”: uma relação integrada e produtiva. Alternativa <strong>E</strong>.</p><p>O romantismo grego é citado como ideal de encontro, não de separação (A). O texto rejeita a separação (B), valoriza os enigmas (C) e recusa a ideia de que letras e números são opostos (D).</p>"},
51: {"materia": "Português", "assunto": "Classes de palavras", "tags": ["preposição", "regência"],
     "enunciado": p("No trecho “correspondentes <strong>a</strong> sistemas de pensamento e linguagens”, a palavra destacada é"), "apoio_de": (50, P50),
     "alternativas": AL(21, "(A) um artigo definido feminino que concorda", "para destacar o advérbio linguagens."),
     "explicacao": "<p>“Correspondente” pede complemento com a preposição “a” (correspondente <em>a</em> algo). O “a” é <strong>preposição</strong> exigida pelo adjetivo. Alternativa <strong>D</strong>.</p><p>Não pode ser artigo feminino diante de “sistemas”, masculino plural (A). Não é pronome possessivo (B), forma do verbo haver (C) nem adjetivo (E), e “linguagens” é substantivo.</p>"},
52: {"materia": "Português", "assunto": "Semântica", "tags": ["denotação e conotação"],
     "enunciado": p("No texto, entende-se que"), "apoio_de": (50, P50),
     "alternativas": AL(21, "(A) o substantivo literatura, no primeiro parágrafo", "remete ao sentido de absorver intelectualmente."),
     "explicacao": "<p>Autores que “beberam” de fontes científicas não beberam líquido: absorveram ideias. É sentido <strong>conotativo</strong> (figurado). Alternativa <strong>E</strong>.</p><p>“Literatura” não se refere a produção informal (A). “O texto não diz nada” é figurado, pois texto não fala (B). Não há letras gregas no texto (C). E “exaustivamente” significa “de forma completa”, em sentido literal, sem relação com cansaço (D).</p>"},
53: {"materia": "Português", "assunto": "Literatura", "tags": ["Simbolismo", "aliteração"],
     "enunciado": PESSANHA + P53,
     "alternativas": AL(21, "(A) Elipse, pois o autor omite", "exclusividade de rimas ricas."),
     "explicacao": "<p>O Simbolismo valoriza a musicalidade, e o poema a constrói com repetição de sons consonantais, como em “Passo contigo a tarde e sempre sem receio”: <strong>aliteração</strong>. Alternativa <strong>C</strong>.</p><p>Há vários pronomes pessoais no poema (A). Não há bucolismo (B). Determinismo é do Realismo/Naturalismo (D). E ornamentação exagerada e rimas ricas exclusivas são marcas parnasianas (E).</p>"},
54: {"materia": "Português", "assunto": "Interpretação de texto", "tags": ["eu lírico"],
     "enunciado": p("No poema, o eu-lírico demonstra que"), "apoio_de": (53, P53),
     "alternativas": AL(21, "(A) apresenta uma atração explicitamente física", "o qual apresenta uma série de contradições."),
     "explicacao": "<p>O poema se chama “Interrogação” e repete “Não sei se isto é amor”, “Se é amar-te não sei”: o eu lírico duvida do que sente, e o sentimento é cheio de contradições (não idealiza, mas sorri ao ver o sorriso; não deseja, mas adoeceria com a doença do outro). Alternativa <strong>E</strong>.</p><p>Ele nega a atração carnal (A). Diz que nunca escreveu versos românticos, mas não demonstra antipatia (B). Admite pressentir uma mudança (C). E procura o olhar quando sente dor, não quando está curado (D).</p>"},
})
completar(Q, R)
