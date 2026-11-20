# Ajustes da conferência humana: Vestibular FATEC 2º semestre de 2017 (exame de 02/07/2017)
# Texto conferido com a imagem de cada página. Tema implícito: Imigração (redação: impactos da imigração no mercado de trabalho).
# 54 questões; a prova tem 5 h no total, incluindo a redação (que fica fora do simulado).
# Matéria: a do gabarito oficial; nas "Multidisciplinar", a matéria principal + tag "multidisciplinar".
# Rascunho com colunas embaralhadas: enunciados e alternativas escritos aqui.
# Gabarito: oficial (2º SEM/17), sem anuladas. Q3 e Q24 (estruturas) e Q35 (circuitos) com alternativas descritas em texto. Soneto de Bilac (domínio público) transcrito.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import A, carregar, enun, tabela, colunas, completar, trecho

ID = "fatec-2017-2sem"
META = {
    "id": ID,
    "banca": "FATEC",
    "ano": 2017,
    "semestre": 2,
    "titulo": "Vestibular FATEC, 2º semestre de 2017",
    "fonte": "Centro Paula Souza",
    "dataExame": "2017-07-02",
    "duracaoMinutos": 300,
    "tema": "Imigração",
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
VILLEN = (chamada("Leia o texto e os gráficos para responder às questões de números 07 e 08.")
          + apoio(*T(4, "Segundo a pesquisadora e socióloga Patrícia Villen", "agressivas em relação aos imigrantes”.", ["Atualmente, com a crise"])) + "[[fig:1]]"
          + url("https://tinyurl.com/h6om6by", "03.02.2017"))
VILLEN_IMG = figs(("q07", "Dois gráficos. “Número de imigrantes que chegaram ao Brasil, por ano”: 45 124 em 2006 e 117 745 em 2015. “Ranking dos dez países com maior número de imigrantes que chegaram ao Brasil, em 2015”: Haiti 14 535; Bolívia 8 407; Colômbia 7 653; Argentina 6 147; China 5 798; Portugal 4 861; Paraguai 4 841; Estados Unidos 4 747; Uruguai 4 598; Peru 4 403."))
P7 = p("Dentre os países listados no ranking, o número de imigrantes que chegaram ao Brasil provenientes de países localizados fora do continente americano é igual a")

DICLORO = (chamada("Leia o texto para responder às questões de números 20 e 21.")
           + apoio(" ".join(T(9, "Um vazamento de gás dentro do complexo", "a informação não se confirmou.")).replace("(C3O3N3NaCl2)", "(C<sub>3</sub>O<sub>3</sub>N<sub>3</sub>NaC<em>ℓ</em><sub>2</sub>)"))
           + url("http://tinyurl.com/ha6rab6", "28.01.2017"))
P20 = p("No dicloroisocianurato de sódio, a porcentagem de cloro, em massa, é aproximadamente igual a") + apoio("Massas molares em g/mol:<br>C = 12,0<br>N = 14,0<br>O = 16,0<br>Na = 23,0<br>C<em>ℓ</em> = 35,5")

ASIMOV = (chamada("<em>Eu, Robô</em> (<em>I, Robot</em>) é uma coletânea de contos escritos por Isaac Asimov que procura descrever, sob o ponto de vista do autor, o hipotético aumento da presença e da atuação dos robôs na sociedade. Leia o texto, que apresenta uma entrevista com a personagem Susan Calvin, uma “robopsicóloga”, e responda às questões de números 25 a 29.")
          + apoio(*T(11, "Susan Calvin had been born in the year 1982", "better breed than we are.”", ["She went back to her desk", "“How old are you?”", "“Thirty-two,”", "“Then you don’t remember", "“I’m afraid I haven’t.", "“You may. To you"]))
          + fonte("(ASIMOV, I. <em>I, Robot</em>. Greenwich, Conn: Fawcett Publications,1950. p. 2-3.)"))
P25 = p("De acordo com o texto, pode-se afirmar corretamente que")

REFUG = (chamada("Leia o texto e o infográfico, relacionados a dados referentes ao ano de 2015, para responder às questões de números 30 a 32.")
         + apoio(*T(12, "O relatório anual “Tendências Globais”", "dentro de seus países.", ["O universo de 65,3 milhões"])) + "[[fig:1]]"
         + url("http://tinyurl.com/k2q6v9y", "03.02.2017", "Original colorido. Adaptado."))
REFUG_IMG = figs(("q30", "Infográfico do ACNUR: “1 em cada 113 pessoas no planeta é solicitante de refúgio, deslocada interna ou refugiada”, com 113 bonequinhos, um deles destacado andando."))
P30 = p("Durante o vestibular da FATEC, um candidato levou exatos 40 segundos para ler o texto sobre os refugiados.",
        "Do início ao término da leitura desse texto pelo candidato, o número de pessoas que foram deslocadas de modo forçado no planeta Terra é igual a") + apoio("Para responder a essa questão, considere a média de deslocados por minuto em 2015.")

CRIME = (chamada("Leia o texto para responder às questões de números 50 e 51.")
         + apoio(*T(20, "“Não havia um segundo a perder.", "levar as mãos à cabeça.”", ["A velha estava com a cabeça"]))
         + fonte("(DOSTOIÉVSKI, F. <em>Crime e Castigo</em>. São Paulo: Abril, 2010. p.111.)"))
P50 = p("Na passagem “Entretanto, readquiriu-<strong>as</strong> assim que vibrou o primeiro golpe.”, a palavra <strong>as</strong>")

BILAC = (chamada("Leia o texto de Olavo Bilac para responder às questões de números 52 a 54.")
         + apoio("<strong><u>Incontentado</u></strong>",
                 "Paixão sem grita, amor sem agonia,<br>Que não oprime nem magoa o peito,<br>Que nada mais do que possui queria,<br>E com tão pouco vive satisfeito...",
                 "Amor, que os exageros repudia,<br>Misturado de estima e de respeito,<br>E, tirando das mágoas alegria,<br>Fica farto, ficando sem proveito...",
                 "Viva sempre a paixão que me consome,<br>Sem uma queixa, sem um só lamento!<br>Arda sempre este amor que desanimas!",
                 "Eu, eu tenha sempre, ao murmurar teu nome,<br>O coração, malgrado o sofrimento,<br>Como um rosal desabrochado em rimas.")
         + url("https://tinyurl.com/nxwg9mp", "17.02.2017", ""))
P52 = p("Dentre as características do texto <u>Incontentado</u>, de Olavo Bilac, temos")

Q = {
1: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": MULTI + ["diabetes", "genes poupadores"],
    "enunciado": p(" ".join(T(2, "Em populações humanas com menos acesso", "reservas energéticas no corpo.")), " ".join(T(2, "Indivíduos dessas populações", "tendem a apresentar doenças como a"))),
    "alternativas": AL(2, "(A) diabetes melito tipo II", "consumo excessivo de gorduras insaturadas."),
    "explicacao": "<p>Genes que favorecem acumular reservas são vantagem em tempos de fome, mas, com dieta calórica farta, levam a obesidade e <strong>diabetes tipo II</strong>, marcada pela resistência à insulina. Alternativa <strong>A</strong>.</p><p>O diabetes tipo I é autoimune, com falta de produção de insulina, e não tem relação com álcoois (B). A artrite reumatoide é autoimune (C), a séptica é infecciosa (D), e a gota vem do excesso de ácido úrico, ligado a purinas, não a gorduras insaturadas (E).</p>"},
2: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": MULTI + ["imigração"],
    "enunciado": p("Leia o trecho do relato de um imigrante ao jornal britânico <em>The Guardian</em>.") + apoio(*T(2, "I’ve never thought of myself as an immigrant", "to study classics in Oxford.", ["I left Israel for the first time"]))
                 + url("https://tinyurl.com/zemyaac", "15.02.2017") + p("De acordo com o texto, o imigrante"),
    "alternativas": AL(2, "(A) se queixa de não ter uma família.", "não foi aceito para estudar em Oxford."),
    "explicacao": "<p>“<em>I left Israel for the first time as a boy, in 1967</em>”: ele saiu de Israel pela primeira vez ainda garoto. Alternativa <strong>B</strong>.</p><p>Ele diz que é dedicado à família (A) e a certos valores morais (C). Depois de Berkeley, voltou a Israel (“<em>came back to Israel</em>”) (D). E foi estudar em Oxford (E).</p>"},
3: {"materia": "Química", "assunto": "Química orgânica", "tags": MULTI + ["CFC", "fórmulas estruturais"],
    "enunciado": p("Leia o texto") + apoio(*T(2, "Albert Henne nasceu em Bruxelas", "características de gases refrigerantes.", ["Em 1930, Henne"]))
                 + fonte("(Fonte dos dados: BURRESON, J. e LE COUTEUR, P. <strong>Os botões de Napoleão</strong>. Rio de Janeiro: ZAHAR, 2006.)")
                 + p("Assinale a alternativa que apresenta uma molécula que possui as características de um CFC, conforme a descrição apresentada no texto."),
    "alternativas": alts("CC<em>ℓ</em><sub>3</sub>–CH<sub>3</sub> (dois carbonos: um com três átomos de cloro, outro com três hidrogênios).",
                         "CF<sub>3</sub>–CH<sub>3</sub> (dois carbonos: um com três átomos de flúor, outro com três hidrogênios).",
                         "CHFC<em>ℓ</em><sub>2</sub> (um carbono ligado a um H, um F e dois C<em>ℓ</em>).",
                         "CH<sub>2</sub>C<em>ℓ</em><sub>2</sub> (um carbono ligado a dois H e dois C<em>ℓ</em>).",
                         "CH<sub>4</sub> (um carbono ligado a quatro H)."),
    "explicacao": "<p>O texto define CFC como molécula com um ou dois carbonos, <strong>pelo menos um flúor e pelo menos um cloro</strong>. Só CHFCℓ₂ tem os dois halogênios. Alternativa <strong>C</strong>.</p><p>A e D não têm flúor, B não tem cloro, e E não tem nenhum dos dois.</p><p>Observação: na prova, as alternativas são fórmulas estruturais desenhadas; aqui foram escritas como fórmulas condensadas.</p>"},
4: {"materia": "História", "assunto": "Brasil República", "tags": MULTI + ["imigração japonesa"],
    "enunciado": p(" ".join(T(3, "Em 1908, o navio Kasato Maru", "fora do Japão.")), " ".join(T(3, "Considerando os contextos brasileiro e japonês", "assinale a alternativa correta."))).replace("Kasato Maru", "<em>Kasato Maru</em>"),
    "alternativas": AL(3, "(A) Refugiados da Guerra Civil Meiji", "fugindo dos horrores da Segunda Guerra Mundial."),
    "explicacao": "<p>O Japão da Era Meiji vivia superpopulação e crise no campo, e as fazendas de café paulistas precisavam de braços depois da abolição e da queda da imigração italiana. Alternativa <strong>D</strong>.</p><p>Os japoneses vieram como colonos para as lavouras, não como desempregados urbanos (A). Não houve acordo de mecanização (B) nem imposição de Hirohito, que só assumiu em 1926 (C). E a imigração começou em 1908, décadas antes de Hiroshima (E).</p>"},
5: {"materia": "Física", "assunto": "Cinemática", "tags": MULTI + ["velocidade média", "conversão de unidades"],
    "enunciado": p(" ".join(T(3, "Suponha que a velocidade média do Kasato Maru", "aproximadamente, a distância de")).replace("Kasato Maru", "<em>Kasato Maru</em>")) + apoio("Dado:<br>1 milha náutica ≅ 1,85 km"),
    "alternativas": alts("14 000.", "13 000.", "12 000.", "11 000.", "10 000."),
    "explicacao": "<p>Tempo: 52 dias × 24 h = 1 248 h. Distância: 15 × 1 248 = 18 720 km. Em milhas náuticas: 18 720 ÷ 1,85 ≈ 10 119, ou seja, cerca de <strong>10 000</strong>. Alternativa <strong>E</strong>.</p><p>Multiplicar por 1,85 em vez de dividir dá cerca de 34 600, fora das alternativas.</p>"},
6: {"materia": "Geografia", "assunto": "População", "tags": MULTI + ["dekasseguis", "migração"],
    "enunciado": p(*T(3, "Tradicionalmente, o termo dekassegui", "emigravam para o Japão.", ["No fim dos anos 1980"])).replace("dekassegui", "<em>dekassegui</em>") + p("No caso brasileiro, o principal fator que impulsionou o movimento migratório para o Japão foi a"),
    "alternativas": AL(3, "(A) ausência de direitos civis durante a transição", "nas décadas de 1980 e 1990."),
    "explicacao": "<p>A “década perdida” (1980) e a hiperinflação levaram muitos descendentes de japoneses a buscar trabalho no Japão, que vivia forte crescimento e facilitou a entrada deles em 1990. Alternativa <strong>E</strong>.</p><p>Os direitos civis já se restabeleciam na redemocratização (A). Os dekasseguis foram, em geral, para fábricas, não escritórios (B), nem universidades (C). E no Japão o salário é pago em iene (D).</p>"},
7: {"materia": "Matemática", "assunto": "Estatística", "tags": MULTI + ["gráficos", "imigração"],
    "enunciado": VILLEN + P7, "imagens": VILLEN_IMG,
    "alternativas": alts("9 001.", "9 608.", "10 659.", "15 406.", "18 312."),
    "explicacao": "<p>No ranking, os países fora da América são China (Ásia) e Portugal (Europa): 5 798 + 4 861 = <strong>10 659</strong>. Alternativa <strong>C</strong>.</p><p>Os Estados Unidos estão na América do Norte, e o Haiti, na América Central.</p>"},
8: {"materia": "Matemática", "assunto": "Probabilidade", "tags": MULTI + ["gráficos"],
    "enunciado": p("Suponha que seja realizado o sorteio de uma casa para um imigrante que chegou ao Brasil em 2015.", "A probabilidade de que o ganhador desse sorteio seja argentino ou chinês é, aproximadamente, igual a"),
    "apoio_de": (7, P7),
    "alternativas": alts("10%.", "15%.", "20%.", "25%.", "30%."),
    "explicacao": "<p>Argentinos e chineses: 6 147 + 5 798 = 11 945, num total de 117 745 imigrantes em 2015. 11 945 ÷ 117 745 ≈ 0,10 = <strong>10%</strong>. Alternativa <strong>A</strong>.</p><p>O total é o de todos os imigrantes de 2015, não só a soma dos dez países do ranking.</p>"},
9: {"materia": "Português", "assunto": "Sintaxe", "tags": MULTI + ["orações subordinadas", "gerúndio"],
    "enunciado": p("Recentemente, a agência de notícias BBC publicou uma reportagem sobre o controle imigratório no Canadá, com o seguinte título:") + apoio("Atraindo cada vez mais brasileiros, Canadá se firma como destino global de imigrantes") + url("https://tinyurl.com/m83b8bg", "17.02.2017", "")
                 + p("A relação entre as duas orações que compõem o título da notícia é de"),
    "alternativas": AL(5, "(A) subordinação, porque ambas as orações", "pois ambas as orações são dependentes."),
    "explicacao": "<p>“Atraindo cada vez mais brasileiros” é uma oração reduzida de gerúndio que depende da principal, “Canadá se firma como destino global de imigrantes”. Há <strong>subordinação</strong>, e a primeira oração depende da segunda. Alternativa <strong>B</strong>.</p><p>Na subordinação, uma oração depende da outra (A). A dependente é a primeira, não a segunda (C e D). E na coordenação as orações são independentes (D e E).</p>"},
10: {"materia": "Raciocínio lógico", "assunto": "Conjuntos", "tags": ["diagrama de Venn"],
     "enunciado": apoio("Uma pesquisa foi realizada com alguns alunos da Fatec–São Paulo sobre a participação em um Projeto de Iniciação Científica (PIC) e a participação na reunião anual da Sociedade Brasileira para o Progresso da Ciência (SBPC).<br>Dos 75 alunos entrevistados:<br>• 17 não participaram de nenhuma dessas duas atividades;<br>• 36 participaram da reunião da SBPC e<br>• 42 participaram do PIC.")
                  + p("Nessas condições, o número de alunos entrevistados que participaram do PIC e da reunião da SBPC é"),
     "alternativas": alts("10.", "12.", "16.", "20.", "22."),
     "explicacao": "<p>Participaram de pelo menos uma atividade 75 − 17 = 58 alunos. Somando os grupos, 36 + 42 = 78, e quem fez as duas foi contado duas vezes: 78 − 58 = <strong>20</strong>. Alternativa <strong>D</strong>.</p>"},
11: {"materia": "Raciocínio lógico", "assunto": "Raciocínio espacial", "tags": ["cilindro", "cortes"],
     "enunciado": p(" ".join(T(5, "Um cilindro circular reto é dividido em N partes", "com essas intersecções."))) + "[[fig:1]]" + p("Assim sendo, de acordo com a figura, o valor de N é"),
     "imagens": figs(("q11", "Cilindro cortado por um plano horizontal no meio da altura e por três planos verticais. Na tampa de cima, os três cortes verticais aparecem como três segmentos que se cruzam, dividindo o círculo em 7 regiões.")),
     "alternativas": alts("10.", "12.", "14.", "15.", "17."),
     "explicacao": "<p>Os três planos verticais dividem a base em 7 regiões (as três retas formam um pequeno triângulo no meio e mais seis regiões em volta, como se vê na tampa). O plano horizontal corta cada uma dessas peças em duas: 7 × 2 = <strong>14</strong>. Alternativa <strong>C</strong>.</p>"},
12: {"materia": "Raciocínio lógico", "assunto": "Operações e problemas", "tags": ["sistema de numeração decimal"],
     "enunciado": p("Leia o texto e siga as orientações:") + apoio("• pense em um número inteiro positivo N, de três algarismos distintos e não nulos;<br>• com os algarismos de N, forme todos os possíveis números de dois algarismos distintos;<br>• obtenha a soma (S) de todos esses números de dois algarismos;<br>• obtenha a soma (R) dos três algarismos do número N;<br>• finalmente, divida S por R.")
                  + p("O quociente da divisão de S por R é igual a"),
     "alternativas": alts("21.", "22.", "23.", "24.", "25."),
     "explicacao": "<p>Com algarismos a, b e c formam-se 6 números de dois algarismos distintos. Cada algarismo aparece 2 vezes como dezena e 2 vezes como unidade: S = 20(a + b + c) + 2(a + b + c) = 22R. Logo S ÷ R = <strong>22</strong>. Alternativa <strong>B</strong>.</p><p>Teste: com 123, os números são 12, 13, 21, 23, 31, 32, cuja soma é 132, e 132 ÷ 6 = 22.</p>"},
13: {"materia": "Raciocínio lógico", "assunto": "Sequências", "tags": ["frações"],
     "enunciado": p("Os termos da sequência \\(\\left(\\dfrac{11}{2};\\ \\dfrac{17}{3};\\ \\dfrac{35}{6};\\ 6;\\ \\dfrac{37}{6};\\ \\dfrac{19}{3};\\ \\dfrac{13}{2};\\ \\ldots\\right)\\) obedecem a um critério de formação.", "O oitavo termo dessa sequência é"),
     "alternativas": alts("\\(\\dfrac{23}{2}\\).", "\\(\\dfrac{21}{2}\\).", "\\(\\dfrac{23}{3}\\).", "\\(\\dfrac{22}{3}\\).", "\\(\\dfrac{20}{3}\\)."),
     "explicacao": "<p>Escrevendo tudo com denominador 6: 33/6, 34/6, 35/6, 36/6, 37/6, 38/6, 39/6. Os numeradores crescem de 1 em 1, então o oitavo termo é 40/6 = <strong>20/3</strong>. Alternativa <strong>E</strong>.</p>"},
14: {"materia": "Raciocínio lógico", "assunto": "Operações e problemas", "tags": ["MMC", "restos"],
     "enunciado": p(*T(6, "Para a realização de uma atividade, um professor", "maior que o número de homens.", ["Considere que nessa turma"]), "Nessas condições, o menor valor de N é um número"),
     "alternativas": AL(6, "(A) primo e não par.", "(E) cubo perfeito."),
     "explicacao": "<p>N deixa resto 1 na divisão por 3 e por 4, então deixa resto 1 na divisão por 12: N = 13, 25, 37, 49... Como há 17 homens e mais mulheres que homens, N ≥ 17 + 18 = 35. O menor valor é <strong>37</strong>, que é primo e ímpar. Alternativa <strong>A</strong>.</p><p>Esquecer a condição das mulheres levaria a 25, que é quadrado perfeito (D).</p>"},
15: {"materia": "História", "assunto": "Antiguidade", "tags": ["Egito antigo", "rio Nilo"],
     "enunciado": p("No século V a.C., Heródoto, historiador grego, afirmou que “O Egito é uma dádiva do Nilo”.", "Assinale a alternativa que apresenta, corretamente, a principal razão de se atribuir ao rio Nilo uma importância tão grande para o desenvolvimento do Egito Antigo."),
     "alternativas": AL(7, "(A) Nos períodos de cheias, as águas desse rio", "entre o Saara e o deserto da Namíbia."),
     "explicacao": "<p>As cheias anuais do Nilo depositavam limo fértil nas margens, permitindo a agricultura em pleno deserto. Alternativa <strong>A</strong>.</p><p>Não havia eletricidade (B), o Egito não conquistou o sul da Europa (C), as pirâmides são de pedra (D), e o Nilo não atravessa a África até a Namíbia (E).</p>"},
16: {"materia": "História", "assunto": "Brasil Império", "tags": ["Lei de Terras"],
     "enunciado": p(" ".join(T(7, "Promulgada em 1850, a chamada Lei de Terras", "relações fundiárias no Brasil.")), "A partir desta data, ficou estabelecido que as terras"),
     "alternativas": AL(7, "(A) seriam tomadas pelo Estado e transformadas", "Agrária (Incra)."),
     "explicacao": "<p>A Lei de Terras (1850) determinou que terras devolutas só poderiam ser obtidas por <strong>compra</strong>, proibindo a posse por ocupação. Isso dificultou o acesso à terra para pobres, ex-escravizados e imigrantes. Alternativa <strong>C</strong>.</p><p>Não houve cooperativas (A). Capitanias hereditárias são do século XVI (B). O colonato não distribuía lotes (D). E o Incra é de 1970 (E).</p>"},
17: {"materia": "História", "assunto": "Brasil Império", "tags": ["Proclamação da República", "charge"],
     "enunciado": p("Observe a imagem.") + "[[fig:1]]"
                  + p(" ".join(T(7, "A charge faz referência ao cenário político", "na década seguinte.")), "Sobre o contexto político que culminou na Proclamação da República no Brasil, é correto afirmar que"),
     "imagens": figs(("q17", "Charge do fim do Império: D. Pedro II, idoso, de barba branca, coroa e manto, escorrega do trono e cai para trás, com as pernas para o alto. Um homem de óculos espia por trás do trono; ao fundo, um papel com o título “Falla do Throno” e, num camarote, figuras de bobo e de indígena riem da cena.")),
     "alternativas": AL(7, "(A) a República foi proclamada por representantes", "da Igreja Católica e dos militares."),
     "explicacao": "<p>A monarquia ruiu ao perder suas bases: os cafeicultores (sobretudo depois da abolição sem indenização), a Igreja (Questão Religiosa) e o Exército (Questão Militar). Alternativa <strong>E</strong>.</p><p>A República foi um golpe militar, sem participação popular (A). A abolição enfraqueceu a monarquia (B). Isabel era herdeira do trono, não republicana (C). E os militares, fortalecidos após a Guerra do Paraguai, se voltaram contra a monarquia (D).</p>"},
18: {"materia": "História", "assunto": "Idade Moderna", "tags": ["Renascimento", "Michelangelo"],
     "enunciado": p("Leia o texto e relacione-o à imagem.") + apoio(" ".join(T(8, "Em um mundo ainda fortemente marcado", "aproximação com o plano divino.")))
                  + fonte("(CAMPOS, F.; CLARO, R.; DOLHNIKOFF, M. <strong>Jogo da História nos dias de hoje</strong>.7. São Paulo: Leya, 2015. p.65.)") + "[[fig:1]]"
                  + p("O texto e a imagem remetem a um movimento artístico e filosófico ocorrido na Europa entre os séculos XIII e XVII.", "Assinale a alternativa que apresenta o nome dado a esse movimento."),
     "imagens": figs(("q18", "Afresco “A Criação de Adão”, de Michelangelo, no teto da Capela Sistina: à esquerda, Adão, nu e reclinado, estende o braço; à direita, Deus, envolto por um manto e cercado de anjos, estende o dedo quase tocando o de Adão.")),
     "alternativas": alts("Esclarecimento", "Renascimento", "Romantismo", "Iluminismo", "Dadaísmo"),
     "explicacao": "<p>O <strong>Renascimento</strong> valorizou o ser humano e a natureza sem abandonar a religiosidade. Na “Criação de Adão”, de Michelangelo, o corpo humano é retratado com realismo anatômico numa cena bíblica. Alternativa <strong>B</strong>.</p><p>Esclarecimento e Iluminismo são o mesmo movimento do século XVIII (A e D). O Romantismo é do século XIX (C) e o Dadaísmo, do XX (E).</p>"},
19: {"materia": "História", "assunto": "História contemporânea", "tags": ["Revolução Russa", "NEP"],
     "enunciado": p(" ".join(T(8, "O ano de 2017 marca o centenário", "governo socialista soviético.")), "Assinale a alternativa que apresenta, corretamente, o cenário político e econômico dos primeiros anos do governo socialista (1917–1924)."),
     "alternativas": AL(8, "(A) Leon Trotsky coordenou o programa", "promoção do Estado de Bem-Estar Social."),
     "explicacao": "<p>Sob Lênin (1917–1924), a Rússia enfrentou a guerra civil entre vermelhos e brancos, adotou o comunismo de guerra e, depois, a <strong>Nova Política Econômica</strong> (NEP, 1921), com algumas práticas de mercado. Alternativa <strong>C</strong>.</p><p>Os bolcheviques tiraram a Rússia da Primeira Guerra (A). Gorbachev governou nos anos 1980 (B), Kruschev nos anos 1950 (D), e Stálin assumiu depois de 1924, sem conciliação de classes (E).</p>"},
20: {"materia": "Química", "assunto": "Cálculos químicos", "tags": ["porcentagem em massa", "massa molar"],
     "enunciado": DICLORO + P20,
     "alternativas": alts("24%.", "32%.", "45%.", "72%.", "81%."),
     "explicacao": "<p>Massa molar de C₃O₃N₃NaCℓ₂: 3(12) + 3(16) + 3(14) + 23 + 2(35,5) = 36 + 48 + 42 + 23 + 71 = 220 g/mol. Cloro: 71 ÷ 220 ≈ 0,32 = <strong>32%</strong>. Alternativa <strong>B</strong>.</p><p>Usar só um átomo de cloro dá cerca de 16%.</p>"},
21: {"materia": "Química", "assunto": "Reações químicas", "tags": ["cloro", "ácido hipocloroso"],
     "enunciado": p("Assinale a alternativa que mostra a equação química balanceada que representa corretamente a dissolução do gás cloro em água."), "apoio_de": (20, P20),
     "alternativas": alts("\\(\\text{C}\\ell(\\ell) + \\text{H}_2\\text{O}(\\ell) \\rightleftharpoons \\text{HC}\\ell(\\text{aq}) + \\text{O}(\\text{g})\\)",
                          "\\(\\text{C}\\ell_2(\\text{g}) + 2\\,\\text{H}_2\\text{O}(\\ell) \\rightleftharpoons 4\\,\\text{HC}\\ell(\\text{aq}) + \\text{O}_2(\\text{g})\\)",
                          "\\(\\text{C}\\ell_2(\\text{g}) + 2\\,\\text{H}_2\\text{O}(\\ell) \\rightleftharpoons 2\\,\\text{H}_2(\\text{g}) + \\text{C}\\ell_2\\text{O}(\\text{g})\\)",
                          "\\(\\text{C}\\ell_2(\\text{g}) + \\text{H}_2\\text{O}(\\ell) \\rightleftharpoons \\text{HC}\\ell(\\text{aq}) + \\text{HC}\\ell\\text{O}(\\text{aq})\\)",
                          "\\(2\\,\\text{C}\\ell(\\text{g}) + \\text{H}_2\\text{O}(\\ell) \\rightleftharpoons \\text{HC}\\ell(\\text{aq}) + \\text{HC}\\ell\\text{O}(\\text{aq})\\)"),
     "explicacao": "<p>O cloro é gás diatômico (Cℓ₂) e, na água, forma ácido clorídrico e <strong>ácido hipocloroso</strong> (citado no texto): Cℓ₂ + H₂O ⇌ HCℓ + HCℓO. A equação está balanceada. Alternativa <strong>D</strong>.</p><p>A e E usam cloro monoatômico. B não está balanceada (há 2 Cℓ à esquerda e 4 à direita). C não forma o ácido hipocloroso e também não está balanceada.</p>"},
22: {"materia": "Química", "assunto": "Funções inorgânicas", "tags": ["Arrhenius", "bases"],
     "enunciado": p("O gás amônia se dissolve em água segundo a reação em equilíbrio") + apoio("\\[\\text{NH}_3(\\text{g}) + \\text{H}_2\\text{O}(\\ell) \\rightleftharpoons \\text{NH}_4^{+}(\\text{aq}) + \\text{OH}^{-}(\\text{aq}) \\qquad \\Delta H^0 < 0\\]")
                  + p("Segundo a teoria proposta por Arrhenius, a solução aquosa resultante da dissolução da amônia em água é classificada como"),
     "alternativas": alts("básica, pois absorve calor do meio ambiente.", "básica, pois apresenta íons OH<sup>–</sup> (aq) como único ânion.", "ácida, pois apresenta íons H<sup>+</sup> (aq) não representados no equilíbrio.", "ácida, pois apresenta íons NH<sub>4</sub><sup>+</sup> (aq) como único cátion.", "ácida, pois absorve calor do meio ambiente."),
     "explicacao": "<p>Para Arrhenius, base é o que libera <strong>OH⁻</strong> como único ânion em água: é o caso da amônia. Alternativa <strong>B</strong>.</p><p>ΔH &lt; 0 indica que a reação libera calor, não absorve (A e E). E a classificação de ácido exige H⁺ como único cátion (C e D).</p>"},
23: {"materia": "Química", "assunto": "Eletroquímica", "tags": ["eletrólise", "galvanoplastia"],
     "enunciado": p("Para a cromação de um anel de aço, um estudante montou o circuito eletrolítico representado na figura, utilizando uma fonte de corrente contínua.") + "[[fig:1]]"
                  + p("Durante o funcionamento do circuito, é correto afirmar que ocorre"),
     "imagens": figs(("q23", "Cuba com solução aquosa de CrCℓ₃, com íons Cℓ⁻ e Cr³⁺. Uma peça de platina, ligada ao polo positivo da fonte, e um anel de aço, ligado ao polo negativo, estão mergulhados na solução.")),
     "alternativas": AL(9, "(A) liberação de gás cloro no anodo", "corrosão do aço metálico no anodo."),
     "explicacao": "<p>O anel de aço, no polo negativo, é o <strong>catodo</strong>: ali o Cr³⁺ recebe elétrons e se deposita como cromo metálico. Na platina, o <strong>anodo</strong>, o Cℓ⁻ perde elétrons e forma gás cloro. Alternativa <strong>A</strong>.</p><p>B troca os eletrodos. A platina é inerte: não se deposita nem sofre corrosão (C e D). E o aço é o catodo, não o anodo (E).</p>"},
24: {"materia": "Química", "assunto": "Reações orgânicas", "tags": ["eliminação", "alcenos"],
     "enunciado": p(*T(10, "As reações de eliminação são reações orgânicas", "um exemplo de dehidrohalogenação.", ["A dehidrohalogenação é um exemplo", "A reação entre o hidróxido"])) + "[[fig:1]]"
                  + p("Agora, considere a reação entre o 1–clorobutano e o hidróxido de potássio.") + "[[fig:2]]"
                  + p("Assinale a alternativa que apresenta a fórmula estrutural correta do composto orgânico obtido na reação entre o 1–clorobutano e o hidróxido de potássio, representada na figura."),
     "imagens": figs(("q24a", "Reação: cloroetano (CH₂Cℓ–CH₃) + NaOH → eteno (CH₂=CH₂) + NaCℓ + H₂O."),
                     ("q24b", "Reação: 1-clorobutano (CH₃–CH₂–CH₂–CH₂Cℓ) + KOH → ? (produto a descobrir).")),
     "alternativas": alts("CH<sub>3</sub>–CH=CH<sub>2</sub> (três carbonos, com ligação dupla na ponta).", "CH<sub>3</sub>–CH=CH–CH<sub>3</sub> (quatro carbonos, com ligação dupla no meio).",
                          "CH<sub>3</sub>–CH<sub>2</sub>–CH=CH<sub>2</sub> (quatro carbonos, com ligação dupla na ponta).", "CH<sub>3</sub>–CH=CH–CH<sub>2</sub>–CH<sub>3</sub> (cinco carbonos, com ligação dupla entre o 2º e o 3º).",
                          "CH<sub>3</sub>–CH<sub>2</sub>–CH<sub>2</sub>–CH=CH<sub>2</sub> (cinco carbonos, com ligação dupla na ponta)."),
     "explicacao": "<p>Sai o Cℓ do carbono 1 e um H do carbono vizinho (o 2), e surge a dupla entre eles: <strong>but-1-eno</strong>, CH₃–CH₂–CH=CH₂, com os mesmos quatro carbonos. Alternativa <strong>C</strong>.</p><p>A eliminação não muda o número de carbonos (A, D e E). E B poria a dupla entre os carbonos 2 e 3, longe do carbono que tinha o cloro.</p><p>Observação: na prova, as alternativas são fórmulas estruturais desenhadas; aqui foram escritas como fórmulas condensadas.</p>"},
25: {"materia": "Inglês", "assunto": "Interpretação de texto",
     "enunciado": ASIMOV + P25,
     "alternativas": AL(11, "(A) a “robopsicóloga” Susan Calvin", "a conhece há trinta e dois anos."),
     "explicacao": "<p>Susan pergunta “<em>How old are you?</em>” e o entrevistador responde “<em>Thirty-two</em>”: quem tem 32 anos é a pessoa que conversa com ela. Alternativa <strong>C</strong>.</p><p>Susan tem 75 anos (A). O texto não fala da duração da entrevista (B), de robôs criados por ela (D) nem de quanto tempo os dois se conhecem (E).</p>"},
26: {"materia": "Inglês", "assunto": "Interpretação de texto",
     "enunciado": p("A respeito da U. S. Robot and Mechanical Men, Inc. é correto afirmar, de acordo com o texto, que essa companhia"), "apoio_de": (25, P25),
     "alternativas": AL(11, "(A) desenvolveu o primeiro robô", "(E) foi fundada por Susan Calvin."),
     "explicacao": "<p>“<em>U. S. Robot and Mechanical Men, Inc. was seventy-five also</em>”: a empresa tem 75 anos, a mesma idade de Susan. Alternativa <strong>D</strong>.</p><p>Lawrence Robertson é o fundador, não um robô (A e E). O texto não fala de tipos de robôs (B) nem de filiais (C).</p>"},
27: {"materia": "Inglês", "assunto": "Interpretação de texto",
     "enunciado": p("Comparando o “mundo sem robôs” com o estágio da história da humanidade em que a entrevista é concedida, o texto afirma que"), "apoio_de": (25, P25),
     "alternativas": AL(11, "(A) na época da entrevista, os seres humanos são as", "assim como na época da entrevista."),
     "explicacao": "<p>“<em>Now he has creatures to help him</em> (...) <em>Mankind is no longer alone</em>”: hoje os humanos têm os robôs para ajudá-los. Alternativa <strong>B</strong>.</p><p>Os robôs são “<em>stronger creatures than himself</em>” (A). A humanidade não está mais sozinha (C e E). E o texto não diz que se pensava que os robôs seriam indestrutíveis (D).</p>"},
}

Q.update({
28: {"materia": "Inglês", "assunto": "Interpretação de texto",
     "enunciado": p("Na visão de Susan Calvin, e segundo as informações presentes no texto, os robôs"), "apoio_de": (25, P25),
     "alternativas": alts("não foram projetados para auxiliar os homens.", "não possuem uma mente própria.", "não são adeptos da limpeza.", "são capazes de destruir os seres humanos.", "são uma raça melhor que os seres humanos."),
     "explicacao": "<p>“<em>They’re a cleaner, better breed than we are</em>”: para Susan, os robôs são uma raça melhor que a humana. Alternativa <strong>E</strong>.</p><p>Eles foram feitos para ajudar (A). “<em>Mind and iron!</em>” indica que têm mente (B). “<em>Cleaner</em>” aqui é “mais pura”, não limpeza (C). E “<em>human-destroyed</em>” quer dizer que os humanos podem destruí-los, não o contrário (D).</p>"},
29: {"materia": "Inglês", "assunto": "Verbos", "tags": ["verbos modais"],
     "enunciado": p("O termo <strong><em>may</em></strong> em <em>May I quote you?</em> expressa a ideia de"), "apoio_de": (25, P25),
     "alternativas": alts("permissão.", "obrigação.", "comando.", "conselho.", "previsão."),
     "explicacao": "<p><em>May I...?</em> é a forma educada de <strong>pedir permissão</strong>: “Posso citar você?”. E ela responde “<em>You may</em>” (pode). Alternativa <strong>A</strong>.</p><p>Obrigação seria <em>must</em>/<em>have to</em> (B), conselho seria <em>should</em> (D), e previsão seria <em>will</em> (E).</p>"},
30: {"materia": "Matemática", "assunto": "Proporcionalidade", "tags": ["regra de três", "refugiados"],
     "enunciado": REFUG + P30, "imagens": REFUG_IMG,
     "alternativas": alts("12.", "16.", "20.", "24.", "28."),
     "explicacao": "<p>Em 2015 foram 24 deslocados por minuto. Em 40 segundos (2/3 de minuto): 24 × 2/3 = <strong>16</strong>. Alternativa <strong>B</strong>.</p><p>24 seria o número de um minuto inteiro (D).</p>"},
31: {"materia": "Matemática", "assunto": "Proporcionalidade", "tags": ["razão"],
     "enunciado": p("Com os dados apresentados, podemos afirmar corretamente que o número de habitantes da Terra em 2015, em bilhões, era aproximadamente igual a"), "apoio_de": (30, P30),
     "alternativas": alts("7,14.", "7,20.", "7,26.", "7,32.", "7,38."),
     "explicacao": "<p>Se 1 em cada 113 pessoas é deslocada e os deslocados são 65,3 milhões, a população é 65,3 × 113 ≈ 7 379 milhões ≈ <strong>7,38 bilhões</strong>. Alternativa <strong>E</strong>.</p>"},
32: {"materia": "Matemática", "assunto": "Logaritmos", "tags": ["função exponencial", "juros compostos"],
     "enunciado": p(" ".join(T(13, "Suponha um aumento exato de 10%", "a essa mesma taxa anualmente.")), "O número de pessoas deslocadas, em relação a 2014, dobrará no ano") + apoio("Adote:<br>log 2 = 0,30<br>log 1,1 = 0,04"),
     "apoio_de": (30, P30),
     "alternativas": alts("2018.", "2020.", "2022.", "2024.", "2026."),
     "explicacao": "<p>Depois de n anos a partir de 2014, o número é multiplicado por 1,1ⁿ. Dobrar: 1,1ⁿ = 2, então n · log 1,1 = log 2, e n = 0,30 ÷ 0,04 = 7,5 anos.</p><p>2014 + 7,5 = 2021,5: o número dobra ao longo de 2021 para 2022, ou seja, em <strong>2022</strong> ele já terá dobrado. Alternativa <strong>C</strong>.</p><p>Somar 10% ao ano de forma simples daria 10 anos (2024), o que ignora o crescimento composto (D).</p>"},
33: {"materia": "Matemática", "assunto": "Funções", "tags": ["função afim"],
     "enunciado": p(*T(13, "Admita que a população da Síria em 2010", "em número de anos.", ["Considere que durante esse período"]),
                    "Assinale a alternativa que apresenta a lei da função h(x), para 0 ≤ x ≤ 6, adotando o ano de 2010 como x = 0 e o ano de 2016 como x = 6.").replace("1o grau", "1º grau"),
     "alternativas": alts("h(x) = – 0,1 x + 17,7", "h(x) = – 0,1 x + 20,7", "h(x) = – 0,25 x + 17,7", "h(x) = – 0,5 x + 20,7", "h(x) = – 0,5 x + 17,7"),
     "explicacao": "<p>Em x = 0, h = 20,7 (coeficiente linear). A queda foi de 3 milhões em 6 anos: taxa de −0,5 por ano. h(x) = <strong>−0,5x + 20,7</strong>. Alternativa <strong>D</strong>.</p><p>Usar 17,7 como valor inicial inverte o sentido do tempo (E).</p>"},
34: {"materia": "Matemática", "assunto": "Trigonometria", "tags": ["lei dos senos"],
     "enunciado": p(*T(13, "A maior parte dos refugiados sírios", "Campinas, no Brasil.", ["Considere o triângulo ABC"])) + "[[fig:1]]"
                  + p("Nesse triângulo, a distância entre <strong>A</strong> e <strong>B</strong> é de 3 700 km, a medida de <strong>AĈB</strong> é igual a 18º e a medida de <strong>AB̂C</strong> é igual a 81º.",
                      "Com base nos dados apresentados, se um refugiado sírio viaja de Aleppo a Berlim e, em seguida, de Berlim a Campinas, terá percorrido no mínimo <strong>x</strong> quilômetros em todo o trajeto.", "O valor de <strong>x</strong> é mais próximo de")
                  + apoio("Adote:<br>sen 18º = 0,31<br>cos 18º = 0,95<br>sen 81º = 0,98<br>cos 81º = 0,16"),
     "imagens": figs(("q34", "Triângulo ABC fora de escala: B e A no alto, próximos entre si, e C bem abaixo, à esquerda, com os lados BC e AC longos.")),
     "alternativas": alts("11 300.", "12 300.", "13 300.", "14 300.", "15 300."),
     "explicacao": "<p>O ângulo em A mede 180° − 18° − 81° = 81°. Pela lei dos senos: BC / sen A = AB / sen C, então BC = 3 700 × 0,98 ÷ 0,31 ≈ 11 697 km.</p><p>Trajeto: AB + BC ≈ 3 700 + 11 697 = 15 397 km, mais próximo de <strong>15 300</strong>. Alternativa <strong>E</strong>.</p><p>11 300 se aproxima só de BC, esquecendo o trecho Aleppo–Berlim (A).</p>"},
35: {"materia": "Física", "assunto": "Eletrodinâmica", "tags": ["diodo", "LED"],
     "enunciado": p(*T(14, "Semicondutores são peças-chave", "ligado aos terminais de uma bateria.", ["Considere um diodo emissor"]),
                    "Baseando-se nas informações descritas acima, assinale a alternativa que apresenta o desenho que melhor ilustra uma situação hipotética do correto funcionamento de um LED em dois momentos distintos (I) e (II).") + "[[fig:1]]",
     "imagens": figs(("q35", "Quadro com cinco linhas (A a E) e duas colunas (I e II). Cada célula mostra um circuito com bateria, resistor R e LED, indicando se o LED emite luz e os valores de U e i. A: (I) LED aceso, U ≠ 0, i ≠ 0; (II) LED apagado, U ≠ 0, i = 0. B: (I) aceso, U = 0, i ≠ 0; (II) aceso, U ≠ 0, i ≠ 0. C: (I) apagado, U ≠ 0, i ≠ 0; (II) apagado, U = 0, i ≠ 0. D: (I) aceso, U = 0, i ≠ 0; (II) apagado, U ≠ 0, i = 0. E: (I) aceso, U ≠ 0, i = 0; (II) apagado, U ≠ 0, i = 0.")),
     "alternativas": alts("(I) LED aceso, U ≠ 0 e i ≠ 0; (II) LED apagado, U ≠ 0 e i = 0.", "(I) LED aceso, U = 0 e i ≠ 0; (II) LED aceso, U ≠ 0 e i ≠ 0.", "(I) LED apagado, U ≠ 0 e i ≠ 0; (II) LED apagado, U = 0 e i ≠ 0.",
                          "(I) LED aceso, U = 0 e i ≠ 0; (II) LED apagado, U ≠ 0 e i = 0.", "(I) LED aceso, U ≠ 0 e i = 0; (II) LED apagado, U ≠ 0 e i = 0."),
     "explicacao": "<p>O LED só acende quando passa corrente (i ≠ 0), e só passa corrente se houver tensão (U ≠ 0) no sentido de condução. No sentido oposto, há tensão mas o diodo bloqueia: i = 0 e o LED fica apagado. Os dois momentos são: (I) U ≠ 0, i ≠ 0, aceso; (II) U ≠ 0, i = 0, apagado. Alternativa <strong>A</strong>.</p><p>Corrente sem tensão é impossível (B, C e D). LED aceso sem corrente também (E).</p><p>Observação: na prova, as alternativas são desenhos de circuitos; aqui foram descritas em palavras.</p>"},
36: {"materia": "Física", "assunto": "Óptica", "tags": ["refração", "lei de Snell"],
     "enunciado": p(" ".join(T(15, "Durante um ensaio com uma amostra", "conforme a figura."))) + "[[fig:1]]"
                  + tabela(["Material", "n"], [["ar", "1,00"], ["resina", "1,50"], ["policarbonato", "1,59"], ["cristal dopado", "1,60"], ["cristal de titânio", "1,71"], ["cristal de lantânio", "1,80"]])
                  + apoio("Lembre-se de que:<br>n<sub>I</sub> · sen θ<sub>I</sub> = n<sub>R</sub> · sen θ<sub>R</sub>")
                  + p("Utilizando os dados da figura e as informações apresentadas na tabela de referência, podemos concluir corretamente que o material da amostra é"),
     "imagens": figs(("q36", "Amostra semicircular de raio r (metade de cima, sombreada) sobre o ar (metade de baixo, tracejada). O feixe entra pela amostra, chega ao centro e passa para o ar. Na amostra, o raio forma o ângulo θI com a normal e seu ponto na circunferência está a 2 cm da normal; no ar, forma θR com a normal e está a 3 cm dela.")),
     "alternativas": alts("cristal de lantânio.", "cristal de titânio.", "cristal dopado.", "policarbonato.", "resina."),
     "explicacao": "<p>Os dois raios têm o mesmo comprimento r, então sen θ<sub>I</sub> = 2/r e sen θ<sub>R</sub> = 3/r. Pela lei de Snell: n · 2/r = 1,00 · 3/r, logo n = 3/2 = <strong>1,50</strong>, a resina. Alternativa <strong>E</strong>.</p><p>Inverter a razão daria n ≈ 0,67, menor que o do ar, o que é impossível para um sólido.</p>"},
37: {"materia": "Física", "assunto": "Ondas", "tags": ["radiação ultravioleta", "frequência e comprimento de onda"],
     "enunciado": p(" ".join(T(15, "Um aluno do curso de Cosméticos da FATEC", "montando um quadro esquemático."))) + "[[fig:1]]"
                  + p("Baseando-se nas informações apresentadas no quadro, é certo afirmar que"),
     "imagens": figs(("q37", "Quadro com colunas Onda, Penetração, Efeito, FSF e FSQ. UVA: no mesmo intervalo Δt aparecem 3 oscilações; penetra epiderme, derme e hipoderme; efeitos: bronzeamento, envelhecimento, manchas, câncer; FSF: radiação bloqueada por reflexão; FSQ: radiação bloqueada por absorção. UVB: no mesmo Δt aparecem cerca de 6 oscilações; penetra só a epiderme; efeitos: vermelhidão, queimadura, envelhecimento, manchas, câncer; FSF: bloqueada por reflexão; FSQ: bloqueada por absorção.")),
     "alternativas": AL(15, "(A) a radiação UVA possui menor comprimento", "menor comprimento de onda que a UVA."),
     "explicacao": "<p>No mesmo intervalo Δt, a UVB faz mais oscilações: tem <strong>maior frequência</strong> e, como v = λf, <strong>menor comprimento de onda</strong>. Alternativa <strong>E</strong>.</p><p>A UVA tem maior comprimento de onda e efeitos diferentes (A). Ambas são refletidas pelo FSF (B). Penetram camadas diferentes (C). E a UVA tem menor frequência, embora seja mais penetrante (D).</p>"},
38: {"materia": "Física", "assunto": "Energia", "tags": ["trabalho", "área sob o gráfico"],
     "enunciado": p(*T(16, "Durante o estágio realizado por uma aluna", "com as duas grandezas.", ["Para saber o módulo"])) + "[[fig:1]]"
                  + p("De acordo com a leitura dos dados apresentados pelo gráfico podemos afirmar que o trabalho realizado pela força tensora até atingir a deformação máxima de 10 mm é, em joules, de"),
     "imagens": figs(("q38", "Gráfico “Comportamento de tensão-deformação de material para análise”: tensão (N) × deformação (mm), uma reta que sai da origem e passa por (2; 100), (4; 200), (6; 300), (8; 400) até (10; 500), marcado como (D_máx, T_máx).")),
     "alternativas": alts("5,0 × 10<sup>–1</sup>", "2,5 × 10<sup>0</sup>", "5,0 × 10<sup>1</sup>", "2,5 × 10<sup>2</sup>", "5,0 × 10<sup>3</sup>"),
     "explicacao": "<p>O trabalho é a área sob o gráfico: um triângulo de base 10 mm = 0,01 m e altura 500 N. W = 0,01 × 500 ÷ 2 = <strong>2,5 J</strong>. Alternativa <strong>B</strong>.</p><p>Esquecer de converter mm em m dá 2 500 J (D).</p>"},
39: {"materia": "Física", "assunto": "Termologia", "tags": ["dilatação", "lâmina bimetálica"],
     "enunciado": p(*T(16, "Numa aula de laboratório do curso de Soldagem", "conforme a figura.", ["Para isso, os alunos"])) + "[[fig:1]]"
                  + p("Considere que ambas as lâminas estão inicialmente sujeitas à mesma temperatura T<sub>0</sub>, e que a relação entre os coeficientes de dilatação linear seja α<sub>A</sub> &gt; α<sub>B</sub>.", "Ao aumentar a temperatura da lâmina bimetálica, é correto afirmar que"),
     "imagens": figs(("q39", "Lâmina bimetálica horizontal presa por uma extremidade a um suporte, à esquerda, com a outra extremidade livre. A lâmina A fica em cima e a lâmina B embaixo, soldadas.")),
     "alternativas": {k: v.replace("lâmina A", "<strong>lâmina A</strong>").replace("lâmina B", "<strong>lâmina B</strong>") for k, v in AL(16, "(A) a lâmina A e a lâmina B continuam", "se curvam para cima.").items()},
     "explicacao": "<p>Aquecida, a lâmina A (em cima) dilata mais que a B. Como estão soldadas, o conjunto se curva para o lado da que dilata menos: a ponta livre desce, e <strong>as duas curvam para baixo</strong>, juntas. Alternativa <strong>D</strong>.</p><p>Dilatações diferentes impedem que fiquem retas (A), e soldadas elas não podem se curvar em sentidos opostos (B e C).</p>"},
40: {"materia": "Geografia", "assunto": "População", "tags": ["pirâmide etária"],
     "enunciado": p(" ".join(T(17, "A pirâmide etária é um gráfico", "grupos populacionais específicos.")), "Considere a pirâmide etária.") + "[[fig:1]]"
                  + p("Analisando essa pirâmide etária, podemos afirmar corretamente que"),
     "imagens": figs(("q40", "Pirâmide etária do Brasil em 2010, homens à esquerda e mulheres à direita, por faixas de 5 anos, com número de pessoas e % da população. Algumas faixas: 0 a 4 anos, 7 016 987 homens (3,7%) e 6 779 172 mulheres (3,6%); 5 a 9, 7 624 144 (4,0%) e 7 345 231 (3,9%); 10 a 14, 8 725 413 (4,6%) e 8 441 348 (4,4%); 15 a 19, 8 558 868 (4,5%) e 8 432 002 (4,4%); 20 a 24, 8 630 227 (4,5%) e 8 614 963 (4,5%); 25 a 29, 8 460 995 (4,4%) e 8 643 418 (4,5%); 30 a 34, 7 717 657 (4,0%) e 8 026 855 (4,2%); 60 a 64, 3 041 034 (1,6%) e 3 468 085 (1,8%); 65 a 69, 2 224 065 (1,2%) e 2 616 745 (1,4%). A partir de 25 a 29 anos, todas as faixas têm mais mulheres que homens.")),
     "alternativas": AL(17, "(A) as crianças entre 0 e 9 anos correspondem", "a pequena expectativa de vida do país."),
     "explicacao": "<p>De 25 a 29 anos em diante, as barras das mulheres são maiores (por exemplo, 8 643 418 contra 8 460 995), reflexo da maior mortalidade masculina, inclusive por violência e acidentes. Alternativa <strong>D</strong>.</p><p>As crianças de 0 a 9 anos são cerca de 28,8 milhões (A). Não existe ingresso “obrigatório” no trabalho, muito menos informal com carteira (B). Os adultos de 20 a 59 anos são bem mais de 52 milhões (C). E 1,2% é só a fatia dos homens de 65 a 69 anos (E).</p>"},
41: {"materia": "Geografia", "assunto": "Geopolítica", "tags": ["globalização", "Brexit"],
     "enunciado": p("Leia o texto publicado no jornal eletrônico <em>Observador On Time</em>, de Portugal, em 19 de janeiro de 2017, que apresenta as ideias de Helena Garrido.")
                  + apoio(" ".join(T(18, "“O mundo está mudando", "mercadorias e serviços.”"))) + url("http://tinyurl.com/hdkb5nu", "25.01.2017")
                  + p("Esse texto expõe uma contradição que é"),
     "alternativas": AL(18, "(A) o fato de o governo comunista chinês", "que rechaça tal ideia estadunidense."),
     "explicacao": "<p>A contradição: a China, governada por um partido comunista, defende a globalização capitalista, enquanto os EUA (saída da Parceria Transpacífico) e o Reino Unido (Brexit), países capitalistas, se afastam de blocos econômicos. Alternativa <strong>A</strong>.</p><p>Os blocos não acabaram (B). A Parceria Transpacífico não era liderada pela China nem pela Rússia (C). Os EUA não aderiram ao comunismo (D). E Trump não propôs bloco com a China (E).</p>"},
42: {"materia": "Geografia", "assunto": "Biomas", "tags": ["Mata dos Cocais"],
     "enunciado": p(*T(18, "A Mata dos Cocais é um tipo de cobertura", "dentre os quais se destacam", ["Nessa área de transição"])),
     "alternativas": alts("as seringueiras e as bananeiras.", "as laranjeiras e os pinheiros.", "as carnaúbas e os babaçus.", "as catuabas e os juazeiros.", "as perobas e os jatobás."),
     "explicacao": "<p>A Mata dos Cocais é dominada por palmeiras, principalmente o <strong>babaçu</strong> e a <strong>carnaúba</strong>, base do extrativismo da região. Alternativa <strong>C</strong>.</p><p>Seringueiras são amazônicas (A), pinheiros são da Mata de Araucárias (B), juazeiros são da Caatinga (D), e perobas e jatobás aparecem na Mata Atlântica e no Cerrado (E).</p>"},
43: {"materia": "Geografia", "assunto": "Geografia regional", "tags": ["Austrália", "desertos"],
     "enunciado": p(" ".join(T(18, "A Austrália é, em extensão territorial", "24 milhões de habitantes.")), "As maiores concentrações populacionais da Austrália ocorrem nas proximidades do seu vasto litoral leste e sudeste, pois"),
     "alternativas": AL(18, "(A) na porção centro-noroeste existem dobramentos", "dificulta a ocupação humana dessas áreas."),
     "explicacao": "<p>O interior e o oeste da Austrália são ocupados por grandes <strong>desertos</strong> (como o Grande Deserto de Areia e o Gibson), enquanto o leste e o sudeste têm clima mais úmido e ameno. Alternativa <strong>E</strong>.</p><p>A Austrália é geologicamente estável (A). A colonização foi inglesa, não holandesa (B). Não há ursos nativos (o coala não é urso) (C). E o centro-norte não é dos lugares mais chuvosos do planeta (D).</p>"},
44: {"materia": "Geografia", "assunto": "Geopolítica", "tags": ["Canal de Suez", "transportes"],
     "enunciado": p("A navegação oceânica ainda é o principal modo de transporte de carga no planeta Terra.", "No século XIX, com o intuito de estabelecer uma via de acesso rápido ligando a Europa à Ásia, foi construído o Canal de Suez, que faz a ligação entre os mares"),
     "alternativas": alts("Cáspio e Aral.", "Negro e Morto.", "Jônico e Tirreno.", "Báltico e Adriático.", "Mediterrâneo e Vermelho."),
     "explicacao": "<p>O Canal de Suez (1869), no Egito, liga o mar <strong>Mediterrâneo</strong> ao mar <strong>Vermelho</strong>, evitando a volta pela África. Alternativa <strong>E</strong>.</p>"},
45: {"materia": "Biologia", "assunto": "Evolução", "tags": ["cladograma", "ancestral comum"],
     "enunciado": p("A afirmação “os humanos descendem dos chimpanzés” é contrariada pelo cladograma apresentado, segundo o qual") + "[[fig:1]]",
     "imagens": figs(("q45", "Cladograma com quatro ramos: <em>Hylobates</em> (gibões), <em>Gorilla</em> (gorilas), <em>Pan</em> (chimpanzés) e <em>Homo</em> (humanos). Os gibões se separam primeiro, depois os gorilas; chimpanzés e humanos saem do último ponto de ramificação, em comum.")),
     "alternativas": AL(19, "(A) os chimpanzés são humanos menos evoluídos.", "aparentados aos gorilas que aos humanos."),
     "explicacao": "<p>No cladograma, chimpanzés e humanos saem de um mesmo nó exclusivo: têm um <strong>ancestral comum</strong> que não é ancestral de nenhum outro grupo. Ninguém descende do outro; são “primos”. Alternativa <strong>D</strong>.</p><p>Nenhuma espécie atual é “menos evoluída” (A). Nenhuma atual descende de outra atual (B e C). E os chimpanzés são mais próximos dos humanos que dos gorilas (E).</p>"},
46: {"materia": "Biologia", "assunto": "Reprodução", "tags": ["métodos contraceptivos"],
     "enunciado": p(" ".join(T(19, "Como parte do planejamento familiar", "métodos contraceptivos mais comuns.")).replace("cartaz informativo sobre alguns dos métodos", "cartaz informativo sobre alguns dos métodos"),
                    "Assinale a alternativa que apresente uma afirmação que possa fazer parte do texto do cartaz, por estar biologicamente correta."),
     "alternativas": AL(19, "(A) O diafragma é um instrumento contraceptivo", "deixam de produzir espermatozoides temporariamente."),
     "explicacao": "<p>Na vasectomia, os ductos deferentes são cortados, e os espermatozoides não chegam à uretra. Alternativa <strong>B</strong>.</p><p>O diafragma é de uso feminino (A). A tabelinha não causa esterilidade (C). Inseminação artificial serve para engravidar (D). E a pílula do dia seguinte é de uso feminino (E).</p>"},
47: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": ["verminoses", "nematódeos"],
     "enunciado": p(" ".join(T(19, "Segundo dados de 2017 da Organização Mundial", "tratamento das doenças.")), "As doenças em questão são causadas por"),
     "alternativas": AL(19, "(A) nematódeos, que absorvem nutrientes", "músculos esqueléticos dos hospedeiros."),
     "explicacao": "<p>Lombriga (<em>Ascaris</em>), ancilóstomo e tricúris são <strong>nematódeos</strong> (vermes cilíndricos) que vivem no intestino e roubam nutrientes ou sangue, causando anemia e diarreia. Alternativa <strong>A</strong>.</p><p>Não são bactérias (B), cnidários (C), anelídeos (D) nem equinodermos (E).</p>"},
48: {"materia": "Biologia", "assunto": "Seres vivos", "tags": ["fungos", "mofo"],
     "enunciado": p(" ".join(T(20, "Uma estante de um escritório ficou fechada", "manchas escuras e aveludadas.")), "Para evitar que outros livros apresentem o mesmo problema, recomenda-se que as demais estantes do escritório sejam"),
     "alternativas": AL(20, "(A) umedecidas, dado que os germes", "germinação de esporos de fungos nas capas dos livros."),
     "explicacao": "<p>As manchas aveludadas e o cheiro são de <strong>mofo</strong>, um fungo que cresce em lugares fechados e úmidos. Arejar diminui a umidade e dificulta a germinação dos esporos. Alternativa <strong>E</strong>.</p><p>Umidade favorece o mofo (A). Fungos não são autótrofos nem musgos (B e C). E ácaros não causam essas manchas (D).</p>"},
49: {"materia": "Biologia", "assunto": "Classificação dos seres vivos", "tags": ["taxonomia", "biodiversidade"],
     "enunciado": p("Leia o texto.") + apoio(*T(20, "Estamos presenciando uma inédita crise", "conservação da biodiversidade.", ["Esse desconhecimento, chamado"])) + url("https://tinyurl.com/ycltn6pb", "24.03.2017")
                  + p("Assinale a alternativa correta considerando o que foi apresentado no texto."),
     "alternativas": AL(20, "(A) A Taxonomia é dispensável", "a causa principal do impedimento taxonômico atual."),
     "explicacao": "<p>O texto diz que o impedimento taxonômico, causado pela falta de taxonomistas, “limita severamente as estratégias de conservação”. Formar taxonomistas ajuda a conhecer e a conservar a biodiversidade. Alternativa <strong>D</strong>.</p><p>A Taxonomia é indispensável (A). Quem limita a conservação é a falta de taxonomistas, não eles (B). O impedimento é uma falta de conhecimento, não uma linha de pensamento (C). E a crise é atual, não passada (E).</p>"},
50: {"materia": "Português", "assunto": "Coesão e referência", "tags": ["pronome oblíquo"],
     "enunciado": CRIME + P50,
     "alternativas": AL(20, "(A) é objeto indireto do verbo readquirir", "foi o local atingido pelo golpe."),
     "explicacao": "<p>“Suas mãos pareciam-lhe não ter mais <strong>forças</strong>. Entretanto, readquiriu-<strong>as</strong>”: o pronome retoma “forças”, evitando a repetição. Alternativa <strong>D</strong>.</p><p>“As” é objeto direto, não junção de artigo e preposição (A). Não retoma o machado (B) nem as têmporas (E), e pronome não “rege” substantivo (C).</p>"},
51: {"materia": "Português", "assunto": "Sintaxe", "tags": ["sujeito oculto"],
     "enunciado": p("No trecho “<strong>Deu</strong> um grito fraco e <strong>caiu</strong>.”, o sujeito dos verbos destacados é"), "apoio_de": (50, P50),
     "alternativas": AL(20, "(A) indeterminado, pois não se pode", "porque o pronome pessoal ela está no singular."),
     "explicacao": "<p>O sujeito (“ela”, a velha) não aparece, mas é identificado pela desinência dos verbos e pelo contexto: sujeito <strong>desinencial</strong> (oculto). Alternativa <strong>B</strong>.</p><p>Sabemos quem é, então não é indeterminado (A). Composto teria dois núcleos (C). Inexistente é o de verbos impessoais (D). E E ignora que o pronome nem está escrito.</p>"},
52: {"materia": "Português", "assunto": "Literatura", "tags": ["soneto", "Parnasianismo"],
     "enunciado": BILAC + P52,
     "alternativas": AL(21, "(A) todas as estrofes com o mesmo número", "expressando uma crítica social."),
     "explicacao": "<p>O poema é um <strong>soneto</strong> (dois quartetos e dois tercetos, 14 versos) de tema <strong>amoroso</strong>. Alternativa <strong>D</strong>.</p><p>As estrofes têm 4 e 3 versos e o tema não é religioso (A). Não há suicídio (B), os versos são metrificados, com vocabulário culto (C), e não há crítica social (E).</p>"},
53: {"materia": "Português", "assunto": "Literatura", "tags": ["rima rica", "Parnasianismo"],
     "enunciado": p(" ".join(T(21, "Olavo Bilac foi poeta brasileiro", "classes gramaticais diferentes.")), "Assinale a alternativa que apresenta uma rima rica entre um verbo e um substantivo."), "apoio_de": (52, P52),
     "alternativas": AL(21, "(A) “Que não oprime nem magoa o peito", "malgrado o sofrimento.”"),
     "explicacao": "<p>“Cons<strong>ome</strong>” é verbo e “n<strong>ome</strong>” é substantivo: rima rica entre verbo e substantivo. Alternativa <strong>C</strong>.</p><p>“Peito/respeito” (A) e “lamento/sofrimento” (E) são substantivo com substantivo. “Queria/repudia” são dois verbos (B). E “satisfeito/respeito” é adjetivo com substantivo (D).</p>"},
54: {"materia": "Português", "assunto": "Interpretação de texto", "tags": ["eu lírico"],
     "enunciado": p("O eu lírico do poema está em busca de um amor específico.", "Esse amor deve"), "apoio_de": (52, P52),
     "alternativas": AL(21, "(A) estar em chamas, a ponto de matar", "todas as mágoas do eu lírico em alegria."),
     "explicacao": "<p>O eu lírico rejeita o amor calmo e sem sofrimento dos quartetos e quer uma paixão que o consuma, “malgrado o sofrimento”, mas que faça o coração ser “como um rosal desabrochado em rimas”: um amor belo, ainda que doa. Alternativa <strong>B</strong>.</p><p>Não há desejo de morrer (A). O amor calmo é justamente o que ele recusa (C e D). E transformar mágoa em alegria é característica do amor que ele rejeita (E).</p>"},
})
completar(Q, R)
