# Enem 2006 (27/08/2006), Prova 1 — amarela: prova única de 63 questões (modelo antigo, sem divisão por áreas).
# Fonte do PDF: arquivo 'Provas_Gabaritos_ENEM_2007' do usuário (é esta prova). Gabarito: acervo da USP (GABARITO_ENEM_2006_AMARELA), lido duas vezes.
# Cada questão leva a grande área mais próxima. Poemas de Bandeira (Q1) e Drummond (Q5–6, Q7, Q39) como imagem; Oswald (Q3) em texto.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, paragrafos_enem

ID = "enem-2006"
META = {"id": ID, "banca": "Enem", "ano": 2006, "titulo": "Enem 2006: Prova objetiva", "fonte": "Inep", "dataExame": "2006-08-27",
        "duracaoMinutos": 300, "area": "Prova objetiva (63 questões)", "caderno": "amarelo", "dia": 1, "fonteGabarito": {"oficial": True, "nome": "gabarito oficial do Inep, em cópia guardada pelo Instituto de Física da USP", "url": "https://fep.if.usp.br/~profis/arquivo/avaliacao/enem/provas_gabaritos/2006/GABARITO_ENEM_2006_AMARELA.pdf"}}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 64)}
D = carregar_enem("enem-2006-amarela")
Q = {}
P = lambda n: paragrafos_enem(D[n])
T = lambda n, i: P(n)[i][1]
p = lambda *xs: "".join(f"<p>{x}</p>" for x in xs)
ap = lambda *xs: "".join(f'<p class="apoio">{x}</p>' for x in xs)
tit = lambda x: f'<p class="apoio"><strong>{x}</strong></p>'
fonte = lambda x: f'<p class="fonte">{x}</p>'
ALT = lambda ini: {k: f"[[fig:{i}]]" for i, k in enumerate("ABCDE", ini)}
LIMPA = lambda s: re.sub(r"fi ([a-zà-ú])", r"fi\1", re.sub(r"fl ([a-zà-ú])", r"fl\1", re.sub(r"(\w)- -(\w)", r"\1-\2", s)))
OL = lambda *xs: "<ol>" + "".join(f"<li>{x}</li>" for x in xs) + "</ol>"
FR = lambda *xs: {k: f"\\({v}\\)" for k, v in zip("ABCDE", xs)}


def figs(*pares):
    return [{"arquivo": a, "alt": t} for a, t in pares]


def tabela(cab, linhas):
    return ('<table class="tabela"><thead><tr>' + "".join(f"<th>{c}</th>" for c in cab) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in l) + "</tr>" for l in linhas) + "</tbody></table>")


def E(n, pular=(), trocas=()):
    par = [x for i, x in enumerate(P(n)) if i not in pular]
    ult = max([i for i, (t, _) in enumerate(par) if t == "fonte"], default=-1)
    h = []
    for i, (t, x) in enumerate(par):
        if t == "fig": h.append(f"[[fig:{x}]]")
        elif t == "fonte": h.append(fonte(x))
        elif t == "titulo": h.append(f'<p class="apoio"><strong>{x}</strong></p>' if i < ult else f"<p><strong>{x}</strong></p>")
        elif i < ult: h.append(ap(x))
        else: h.append(p(x))
    s = "".join(h)
    for a, b in trocas:
        assert a in s, a; s = s.replace(a, b)
    return s


def X(n, area, materia, assunto, expl, imagens=(), tags=(), enun=None, trocas=(), alts=None, anulacao=None, quim=False):
    e = LIMPA(enun or E(n))
    if quim: e = QF(e)
    e = re.sub(r"<((?:www\.|solar|http)[^<>]*)>", r"&lt;\1&gt;", e)
    for a, b in trocas:
        assert a in e, a; e = e.replace(a, b)
    Q[n] = {"materia": materia, "assunto": assunto, "area": AREAS[area], "tags": list(tags), "numeroOriginal": n,
                 "enunciado": e, "alternativas": {k: (QF if quim else str)(LIMPA(v)) for k, v in dict(alts or D[n]["alternativas"]).items()},
                 "imagens": list(imagens), "explicacao": expl}
    if anulacao: Q[n]["anulacao"] = anulacao


SUB = lambda s: re.sub(r"(?<=[A-Za-z\)])(\d+)", r"<sub>\1</sub>", s)
LISTA = lambda s: "<ul>" + "".join(f"<li>{x.strip()}</li>" for x in s.split("•") if x.strip()) + "</ul>"
EQ = lambda *xs: '<p class="apoio">' + "<br>".join(xs) + "</p>"
SUP = lambda s: s.replace("m/s2", "m/s<sup>2</sup>").replace("g/cm3", "g/cm<sup>3</sup>").replace("mm3", "mm<sup>3</sup>")

CAP = lambda x: f'<p class="apoio" style="text-align:center">{x}</p>'
L = lambda s: s.replace("m�", "mL").replace("mol/�", "mol/L").replace("mg/�", "mg/L")


NAO_QUIM = {"L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8", "E1", "E2", "E3"}


def QF(s):
    """Índices químicos: CO2 → CO<sub>2</sub>, Cu2+ → Cu<sup>2+</sup> (só em texto, fora de tags)."""
    s = re.sub(r"\b(Cu|Zn|Fe|Pb|Ni)2\+", r"\1<sup>2+</sup>", s)
    def tok(m):
        t = m.group(0)
        if t in NAO_QUIM or not re.fullmatch(r"(?:[A-Z][a-z]?\d*|\((?:[A-Z][a-z]?\d*)+\)\d*)+", t): return t
        return re.sub(r"(?<=[A-Za-z\)])(\d+)", r"<sub>\1</sub>", t)
    partes = re.split(r"(<[^>]+>)", s)
    return "".join(x if x.startswith("<") else re.sub(r"(?<![\w/])(?=[A-Z(])[A-Za-z0-9()]*\d[A-Za-z0-9()]*(?![\w])", tok, x) for x in partes)

AREAS = {"L": "Linguagens", "H": "Ciências Humanas", "N": "Ciências da Natureza", "M": "Matemática"}
J = lambda *xs: " ".join(xs)
K = lambda s: f"\\({s}\\)"
SEMHIF = lambda d: {k: re.sub(r"(\w)- (\w)", r"\1-\2", v) for k, v in d.items()}
A5 = lambda *xs: dict(zip("ABCDE", xs))
CAPA = lambda n: {k: f"[[fig:{i}]] {v}" for i, (k, v) in enumerate(zip("ABCDE", n), 1)}
ALTS = lambda n: SEMHIF(D[str(n)]["alternativas"] if str(n) in D else D[n]["alternativas"])


def SP(n, i, corte):
    """Parágrafo que juntou a referência e o comando: devolve (fonte, comando)."""
    a, b = T(n, i).split(corte, 1)
    return a + corte.strip(), b.strip()


J = lambda *xs: " ".join(xs)
K = lambda s: f"\\({s}\\)"
A5 = lambda *xs: dict(zip("ABCDE", xs))
CL = lambda s: re.split(r"\s+(?:E EE N NN|Textos? para as questões|Para responder às questões)", s)[0].strip()


def ALTS(n):
    return {k: re.sub(r"(\w)- (\w)", r"\1-\2", CL(v)) for k, v in D[n]["alternativas"].items()}


def SP(n, i, corte):
    a, b = T(n, i).split(corte, 1)
    return a + corte.strip(), b.strip()


I3 = lambda *xs: '<ol type="I">' + "".join(f"<li>{x}</li>" for x in xs) + "</ol>"

X(1, "L", "Literatura", "Modernismo", "<p>O poema reproduz uma conversa banal entre um rapaz e uma moça, com frases do dia a dia (“a gente fica olhando”, “você parece louca”). Trazer a linguagem falada e o cotidiano para a poesia é uma marca do Modernismo. Alternativa <strong>B</strong>.</p><p>Não há rimas ricas (A) nem amor romântico idealizado (D), e o diálogo não é exclusivo do Realismo (E).</p>",
  figs(("q01", "Poema narrativo de Manuel Bandeira em versos livres: um rapaz diz a Antônia que ainda não se acostumou com o corpo e o rosto dela, pergunta se ela se lembra de quando, criança, via uma lagarta listrada, compara a moça a uma lagarta listrada e conclui, diante do espanto dela, que ela é engraçada e parece louca.")),
  ["linguagem coloquial", "Manuel Bandeira"], enun="[[fig:1]]" + fonte("Manuel Bandeira. <em>Poesia completa &amp; prosa</em>. Rio de Janeiro: Nova Aguilar, 1985.") + p(T(1, 15)), alts=ALTS(1))
X(2, "L", "Artes", "Artes visuais", "<p>Na primeira figura, as linhas de perspectiva fazem a figura do fundo parecer maior que a da frente, embora as duas tenham o mesmo tamanho; na segunda, as linhas curvas fazem o quadrado parecer deformado. São ilusões de ótica: as aparências enganam. Alternativa <strong>D</strong>.</p>",
  figs(("q02", "Duas ilusões de ótica: à esquerda, duas figuras humanas de mesmo tamanho num corredor em perspectiva, a do fundo parecendo maior; à direita, um quadrado sobre linhas curvas concêntricas, parecendo ter os lados curvados.")),
  ["ilusão de ótica"], enun="[[fig:1]]" + p(T(2, 1)), alts=ALTS(2))
X(3, "L", "Literatura", "Modernismo", "<p>O poema de Oswald, curto, irônico e com linguagem simples, revê a chegada dos portugueses pelo ponto de vista do índio: é o primitivismo da poesia Pau-Brasil (1924), que valorizava a cultura brasileira original. Alternativa <strong>C</strong>.</p><p>Concretismo e Tropicalismo são de décadas depois (B, E).</p>",
  tags=["Oswald de Andrade", "Pau-Brasil"],
  enun='<p class="apoio">Quando o português chegou<br>Debaixo de uma bruta chuva<br>Vestiu o índio<br>Que pena!<br>Fosse uma manhã de sol<br>O índio tinha despido<br>O português.</p>'
       + fonte("Oswald de Andrade. <em>Poesias reunidas</em>. Rio de Janeiro: Civilização Brasileira, 1978.") + p(T(3, 2)))
X(4, "L", "Língua Portuguesa", "Variação linguística", "<p>O narrador descreve o jantar e as atitudes de Nhô Tomé e de Tia Policena e reproduz a fala regional dela, sem julgar. Ele registra costumes da época sem juízos de valor. Alternativa <strong>A</strong>.</p><p>Reproduzir a fala regional não é desvalorizar a norma culta nem mostrar preconceito (B, E).</p>",
  tags=["regionalismo", "variação linguística"], enun=ap(T(4, 0), T(4, 1), T(4, 2)) + fonte("Cornélio Pires. <em>Conversas ao pé do fogo</em>. São Paulo: Imprensa Oficial do Estado de São Paulo, 1987.") + p(T(4, 4)), alts=ALTS(4))
F_AULA = figs(("q05", "Poema “Aula de português”, de Carlos Drummond de Andrade, com versos numerados de três em três (1 a 18). O eu lírico contrasta a linguagem falada, fácil, da infância (a língua em que pedia para ir lá fora, brigava e namorava a priminha) com a língua das letras e da gramática ensinada pelo professor Carlos Góis, cheia de figuras que o atordoam; termina dizendo que o português são dois, e o outro é mistério."))
AULA = "[[fig:1]]" + fonte("Carlos Drummond de Andrade. <em>Esquecer para lembrar</em>. Rio de Janeiro: José Olympio, 1979.")
X(5, "L", "Língua Portuguesa", "Variação linguística", "<p>O poeta opõe a língua falada no dia a dia, “tão fácil de falar e de entender”, à língua formal da gramática e das letras, que o “aturde”. É o contraste entre usos em situações informais e formais. Alternativa <strong>A</strong>.</p>",
  F_AULA, ["formal e informal", "Drummond"], enun=AULA + p(T(5, 0)), alts=ALTS(5))
X(6, "L", "Língua Portuguesa", "Variação linguística", "<p>A “superfície estrelada de letras”, que o menino não sabe o que quer dizer, é a língua escrita e formal ensinada na escola, a variedade padrão. Alternativa <strong>B</strong>.</p><p>Os trechos C, D e E falam da língua do cotidiano da infância.</p>",
  F_AULA, ["variedade padrão"], enun=AULA + p(T(6, 0)), alts=ALTS(6))
X(7, "L", "Literatura", "Modernismo", "<p>O poeta deve penetrar “no reino das palavras”, contemplá-las e descobrir suas “mil faces secretas”: é o trabalho quase artesanal com as palavras para despertar sentidos novos, como o escultor diante do mármore. Alternativa <strong>C</strong>.</p>",
  figs(("q07", "Fragmento do poema “Procura da poesia”, de Drummond, em versos livres: o poeta é convidado a penetrar no reino das palavras, onde estão os poemas que esperam ser escritos, e a contemplar cada palavra, que tem mil faces secretas e pergunta se ele trouxe a chave.")),
  ["metalinguagem", "Drummond"], enun=p(T(7, 0).replace("poema Procura da poesia", "poema <em>Procura da poesia</em>")) + "[[fig:1]]" + fonte("Carlos Drummond de Andrade. <em>A rosa do povo</em>. Rio de Janeiro: Record, 1997, p. 13-14.") + p(SP(7, 3, "p. 13-14.")[1]), alts=ALTS(7))
VS = ['Não se conformou: devia haver engano. (...)', 'Com certeza havia um erro no papel do branco. Não', 'se descobriu o erro, e Fabiano perdeu os estribos.', 'Passar a vida inteira assim no toco, entregando o', 'que era dele de mão beijada! Estava direito aquilo?', 'Trabalhar como negro e nunca arranjar carta de', 'alforria?',
      'O patrão zangou-se, repeliu a insolência,', 'achou bom que o vaqueiro fosse procurar serviço', 'noutra fazenda.', 'Aí Fabiano baixou a pancada e amunhecou.', 'Bem, bem. Não era preciso barulho não.']
X(8, "L", "Língua Portuguesa", "Variação linguística", "<p>“Não se conformou: devia haver engano” usa vocabulário e construção da norma formal. Os outros trechos trazem expressões regionais ou coloquiais: “perder os estribos”, “no toco”, “de mão beijada”, “baixar a pancada”, “amunhecar”. Alternativa <strong>A</strong>.</p>",
  tags=["norma formal", "regionalismo"],
  enun=p(T(8, 0).replace("romance Vidas Secas", "romance <em>Vidas Secas</em>")) + '<p class="apoio"><small>(Os números entre colchetes marcam as linhas do texto original.)</small></p>'
       + ap(" ".join(([f"<small>[{i}]</small>"] if i in (1, 4, 7) else []) + [l] for i, l in enumerate(VS[:7], 1) for _ in [0]).replace("] ", "] ") if False else " ".join((f"<small>[{i}]</small> " if i in (1, 4, 7) else "") + l for i, l in enumerate(VS[:7], 1)),
            " ".join((f"<small>[{i}]</small> " if i in (10,) else "") + l for i, l in enumerate(VS[7:10], 8)), " ".join(l for l in VS[10:]) + " <small>[11–12]</small>")
       + fonte("Graciliano Ramos. <em>Vidas Secas</em>. 91.ª ed. Rio de Janeiro: Record, 2003.") + p(T(8, 5)), alts=ALTS(8))
F_TERRA = figs(("q09", "Quadro da história da Terra com eras, períodos, milhões de anos, evolução biológica e paleogeografia. Do mais antigo ao mais recente: formação da Terra (4.600), primeiros vestígios de vida (3.500), organismos procariontes (3.100), oxigênio livre na atmosfera, aparecimento de eucariontes (2.000), reprodução sexuada (1.000), primeiros peixes (510), primeiras plantas e animais terrestres (439), anfíbios, répteis, primeiros dinossauros (245), aves e angiospermas (145), últimos dinossauros (65), primeiros primatas, hominídeos (5,3), primeiros utensílios de pedra, primeiras manifestações de arte e faunas e floras atuais (0,01). Na paleogeografia: constituição de Rodínia, da Pangeia, início da fragmentação da Pangeia (cerca de 208), abertura do Atlântico Sul, ligação das duas Américas e elevação dos Himalaias."))
INTRO_T = p("Para responder às questões 9 e 10, analise o quadro a seguir, que esquematiza a história da Terra.") + "[[fig:1]]"
X(9, "N", "Biologia", "Evolução", "<p>No quadro, os primeiros vestígios de vida aparecem no Pré-Cambriano (3.500 milhões de anos), quando a vida surgiu em meio líquido, nos oceanos. Alternativa <strong>C</strong>.</p><p>Os répteis surgiram cerca de 290 milhões de anos antes dos hominídeos, não 500 (A); quando o Homo sapiens surgiu, a América do Sul e a África já estavam separadas (B); o Mesozoico durou cerca de 180 milhões de anos, mais que o Cenozoico, de 65 (E).</p>",
  F_TERRA, ["tempo geológico", "origem da vida"], enun=INTRO_T + p(T(9, 0)), alts=ALTS(9))
X(10, "M", "Matemática", "Escala", "<p>Com a Terra formada há 4.600 milhões de anos, a posição de cada evento na escala de 0 a 100 é (4.600 − idade) ÷ 46. Vestígios de vida (3.500): 24; eucariontes (2.000): cerca de 57; primeiros peixes (510): cerca de 89. A régua que mostra isso é a B. Alternativa <strong>B</strong>.</p>",
  F_TERRA + figs(("q10a", "Régua A: primeiros peixes perto de 5, eucariontes perto de 55, vestígios de vida perto de 75."), ("q10b", "Régua B: vestígios de vida perto de 25, eucariontes perto de 57, primeiros peixes perto de 90."),
                 ("q10c", "Régua C: vestígios de vida perto de 5, eucariontes perto de 45, primeiros peixes perto de 75."), ("q10d", "Régua D: vestígios de vida perto de 5, eucariontes perto de 57, primeiros peixes perto de 95."),
                 ("q10e", "Régua E: vestígios de vida perto de 25, eucariontes perto de 45, primeiros peixes perto de 75.")),
  ["escala", "proporção"], enun=INTRO_T + p(T(10, 0)), alts=ALT(2))
X(11, "H", "História", "Pré-história", "<p>Se há vestígios humanos de até 50 mil anos no Piauí, a presença humana na América é muito anterior aos 18 mil anos da teoria mais difundida. As provas contestam essa datação. Alternativa <strong>E</strong>.</p><p>Elas não dizem de onde vieram esses grupos (A, D) nem que o homem surgiu na América (B).</p>",
  tags=["povoamento da América", "Serra da Capivara"], enun=ap(T(11, 0).split(" Validadas,")[0]) + p("Validadas," + T(11, 0).split(" Validadas,")[1]), alts=ALTS(11))
X(12, "N", "Biologia", "Ecologia", "<p>II é aceitável: o clima mais úmido fez florestas fechadas tomarem o lugar das savanas abertas, como mostram os mapas, e os grandes mamíferos perderam as áreas abertas de que precisavam. I é falsa: havia humanos na América antes disso. III é falsa: não há registro de asteroide nesse período (a queda famosa é a de 65 milhões de anos atrás). Alternativa <strong>B</strong>.</p>",
  figs(("q12", "Dois mapas da vegetação da América do Sul. Entre 20 mil e 13 mil anos atrás: grande parte coberta por savana aberta, com floresta aberta com enclaves de savana, gramínea e estepe, deserto e estepe fria no sul. Entre 8 mil e 3 mil anos: predomínio de floresta fechada e savana fechada, savanas temperadas e Patagônia no sul.")),
  ["mudança climática", "extinção da megafauna"],
  enun=ap(T(12, 0)) + "[[fig:1]]" + p("As hipóteses a seguir foram levantadas para explicar o desaparecimento dos grandes mamíferos na América do Sul.")
       + I3("Os seres humanos, que só puderam ocupar a América do Sul depois que o clima se tornou mais úmido, mataram os grandes animais.", "Os maiores mamíferos atuais precisam de vastas áreas abertas para manterem o seu modo de vida, áreas essas que desapareceram da América do Sul com a mudança climática, o que pode ter provocado a extinção dos grandes mamíferos sul-americanos.", "A mudança climática foi desencadeada pela queda de um grande asteróide, a qual causou o desaparecimento dos grandes mamíferos e das aves.")
       + p("É cientificamente aceitável o que se afirma"), alts=ALTS(12))
X(13, "H", "História", "Idade Média", "<p>I: os dois textos tratam das Cruzadas, mas um mostra a violência muçulmana contra cristãos e o outro a violência dos cruzados, vista pelos árabes. II: os dois narram violência contra mulheres e crianças. III é falsa: os textos mostram massacres, não tolerância. Alternativa <strong>D</strong>.</p>",
  tags=["Cruzadas", "pontos de vista"],
  enun=ap(T(13, 0)) + fonte("J. F. Michaud. <em>História das cruzadas</em>. São Paulo: Editora das Américas, 1956 (com adaptações).") + ap(T(13, 2)) + fonte("*franj = cruzados.")
       + fonte("Amin Maalouf. <em>As Cruzadas vistas pelos árabes</em>. 2.ª ed. São Paulo: Brasiliense, 1989 (com adaptações).") + p("Avalie as seguintes afirmações a respeito dos textos acima, que tratam das Cruzadas.")
       + I3("Os textos referem-se ao mesmo assunto — as Cruzadas, ocorridas no período medieval —, mas apresentam visões distintas sobre a realidade dos conflitos religiosos desse período histórico.", "Ambos os textos narram partes de conflitos ocorridos entre cristãos e muçulmanos durante a Idade Média e revelam como a violência contra mulheres e crianças era prática comum entre adversários.", "Ambos narram conflitos ocorridos durante as Cruzadas medievais e revelam como as disputas dessa época, apesar de ter havido alguns confrontos militares, foram resolvidas com base na idéia do respeito e da tolerância cultural e religiosa.")
       + p("É correto apenas o que se afirma em"), alts=ALTS(13))
X(14, "H", "História", "Antigo Regime", "<p>Os músicos da corte eram “criados de libré”, como pasteleiros e cozinheiros: plebeus, do 3.º Estado. Ao chamá-los de “classe média”, o autor mostra que estavam na mesma condição dos demais membros do 3.º Estado, servindo à nobreza. Alternativa <strong>C</strong>.</p>",
  tags=["sociedade de corte", "estamentos"], enun=ap(T(14, 0)) + fonte("Norbert Elias. <em>Mozart: sociologia de um gênio</em>. Ed. Jorge Zahar, 1995, p. 18 (com adaptações).") + p(T(14, 2)), alts=ALTS(14))
X(15, "H", "História", "Brasil Colônia", "<p>São Paulo cresceu com uma sequência de ciclos econômicos no Sudeste: a mineração (os bandeirantes paulistas e o abastecimento das minas), depois o café e, por fim, a indústria, que fez dela a maior metrópole do país. Alternativa <strong>D</strong>.</p><p>A cana prosperou no Nordeste, não no planalto (A), e havia escravidão em São Paulo também (B).</p>",
  tags=["ciclos econômicos", "São Paulo"],
  enun=ap(T(15, 0).replace("davalhe", "dava-lhe")) + fonte("*homiziados: escondidos da justiça. Nelson Werneck Sodré. <em>Formação histórica do Brasil</em>. São Paulo: Brasiliense, 1964.") + ap(T(15, 2)) + fonte("Hildegard Féist. <em>Pequena história do Brasil holandês</em>. São Paulo: Moderna, 1998 (com adaptações).") + p(T(15, 4)), alts=ALTS(15))
X(16, "H", "História", "Século XIX", "<p>Von Martius descreve o indígena como “em grau inferior da humanidade”, “moralmente na infância”, a ser conciliado com a “Europa vencedora”. Ele desvaloriza as culturas indígenas e reforça a missão “civilizadora” europeia, típica do século XIX. Alternativa <strong>E</strong>.</p><p>O texto não defende o extermínio (B).</p>",
  tags=["eurocentrismo", "visão sobre os indígenas"], enun=p(T(16, 0)) + ap(T(16, 1)) + fonte("Carl Von Martius. <em>O estado do direito entre os autóctones do Brasil</em>. Belo Horizonte/São Paulo: Itatiaia/EDUSP, 1982.") + p(T(16, 3)), alts=ALTS(16))
X(17, "H", "História", "República", "<p>O texto lista, em ordem: Vargas morreu (suicídio, 1954), JK teve a posse contestada (1955), Jânio renunciou (1961) e Jango foi deposto (1964). Alternativa <strong>E</strong>.</p><p>JK governou antes de Jango (A), e o fim do regime militar não trouxe Vargas de volta (C).</p>",
  tags=["República de 1946", "crises políticas"], enun=ap(T(17, 0).split(" A partir dessas")[0]) + p("A partir dessas" + T(17, 0).split(" A partir dessas")[1]), alts=ALTS(17))
X(18, "H", "História", "Ditadura militar", "<p>I: os dois falam da explosão de alegria popular. II: Danton Jobim cita o general Médici e o momento político; Rubem Braga lembra terroristas e torturas. III é falsa: o regime militar torturou e perseguiu opositores, como o próprio texto de Rubem Braga sugere. Alternativa <strong>D</strong>.</p>",
  tags=["Copa de 1970", "regime militar"],
  enun=p(T(18, 0)) + ap(T(18, 1)) + fonte("Danton Jobim. <em>Última Hora</em>, 23/6/1970 (com adaptações).") + ap(T(18, 3)) + fonte("Rubem Braga. <em>Última Hora</em>, 25/6/1970 (com adaptações).") + p(T(18, 5))
       + I3("Para os dois autores, a conquista do tricampeonato mundial de futebol provocou uma explosão de alegria popular.", "Os dois textos salientam o momento político que o país atravessava ao mesmo tempo em que conquistava o tricampeonato.", "À época da conquista do tricampeonato mundial de futebol, o Brasil vivia sob regime militar, que, embora politicamente autoritário, não chegou a fazer uso de métodos violentos contra seus opositores.")
       + p("É correto apenas o que se afirma em"), alts=ALTS(18))
X(19, "M", "Matemática", "Probabilidade", "<p>2004 (●): B fica à frente de A e de C; C à frente de A; D à frente de A e de C; e D não fica à frente de B. Ordem: B, D, C, A. 2005 (*): B e C ficam à frente de A; C à frente de B; D não fica à frente de ninguém. Ordem: C, B, A, D. Nenhum time repete a posição, então a probabilidade é 0,00. Alternativa <strong>A</strong>.</p><p>Uma casa vazia significa que o time da linha não ficou à frente do time da coluna naquele ano.</p>",
  figs(("q19", "Tabela com os times A, B, C e D nas linhas e A, B e C nas colunas (a diagonal sombreada). Linha A: vazia. Linha B: ● e * na coluna A; ● na coluna C. Linha C: ● e * na coluna A; * na coluna B. Linha D: ● na coluna A; ● na coluna C.")),
  ["probabilidade", "ordenação"], enun=p(T(19, 0).replace("cIassificação", "classificação")) + "[[fig:1]]" + p(T(19, 3)), alts=ALTS(19))
X(20, "M", "Matemática", "Probabilidade", "<p>Com dois dados há 36 resultados. Soma 6 (Pedro): 5 resultados; soma 2 (Tadeu): 1; soma 12 (Ricardo): 1. Tadeu e Ricardo juntos têm 2/36, menos que os 5/36 de Pedro. Os dois tinham razão. Alternativa <strong>D</strong>.</p>",
  tags=["soma de dois dados"], enun=p(T(20, 0)) + ap(T(20, 1), T(20, 2), T(20, 3).split(" Desse diálogo")[0]) + p("Desse diálogo conclui-se que"), alts={k: re.sub(r"\s+D$", "", v) for k, v in ALTS(20).items()})
X(21, "H", "Geografia", "Migrações", "<p>Os países em preto no mapa são ricos (EUA, Canadá, Europa Ocidental, Austrália), membros da OCDE; os migrantes vêm de países mais pobres (China, Filipinas, Rússia, Ucrânia, América Latina). O motivo principal é a busca de emprego e de melhores condições de vida. Alternativa <strong>E</strong>.</p><p>Os países ricos costumam restringir a imigração, não incentivá-la (B).</p>",
  figs(("q21", "Planisfério com os países que mais receberam imigrantes em 2002 em preto: Estados Unidos, Canadá, países da Europa Ocidental, Austrália, Nova Zelândia e Japão, entre outros.")),
  ["migrações internacionais", "OCDE"], enun=ap(T(21, 0).replace("paísesmembros", "países-membros")) + fonte("<em>Trends in international migration — 2002</em>. Internet: &lt;www.ocde.org&gt; (com adaptações).") + p(SP(21, 1, "(com adaptações).")[1]) + "[[fig:1]]" + p(T(21, 3)), alts=ALTS(21))
X(22, "H", "Geografia", "Geopolítica", "<p>As novas fronteiras surgem com o fim do bloco socialista: a queda dos regimes comunistas, a dissolução da URSS, a reunificação alemã e a fragmentação da Iugoslávia e da Tchecoslováquia. Por trás disso, direta ou indiretamente, está o avanço do capitalismo e da ideologia neoliberal, vitoriosos no fim da Guerra Fria. Alternativa <strong>D</strong>.</p><p>A URSS se desfez, não se fortaleceu (A); a queda do Muro de Berlim foi uma crise do socialismo, não do capitalismo (B). Os nacionalismos (C) tiveram papel, mas os Estados como a Iugoslávia surgiram ou foram refeitos depois da Segunda Guerra.</p>",
  figs(("q22", "Dois mapas da Europa Oriental. Guerra Fria (1945-1989): Alemanha, Polônia, Tchecoslováquia, URSS, Hungria, Áustria e Iugoslávia. Pós-Guerra Fria: Alemanha unificada, Polônia, República Tcheca, Eslováquia, Ucrânia, Hungria, Eslovênia, Croácia, Bósnia-Herzegovina, Sérvia e Montenegro.")),
  ["fim da Guerra Fria", "nacionalismos"], enun=p(T(22, 0)) + "[[fig:1]]" + p(T(22, 4)), alts=ALTS(22))
POPS = (ap("Nos últimos anos, ocorreu redução gradativa da taxa de crescimento populacional em quase todos os continentes. A seguir, são apresentados dados relativos aos países mais populosos em 2000 e também as projeções para 2050.") + "[[fig:1]]" + fonte("Internet: &lt;www.ibge.gov.br&gt;."))
F_POPS = figs(("q23", "Dois gráficos de barras. Países mais populosos em 2000 (milhões de habitantes): China 1.275; Índia 1.008; EUA 283; Indonésia 212; Brasil 170. Previsão para 2050: Índia 1.572; China 1.462; EUA 397; Paquistão 344; Indonésia 311."))
X(23, "H", "Geografia", "População", "<p>O Paquistão não aparece entre os cinco maiores em 2000, logo tinha menos de 170 milhões de habitantes; em 2050, terá 344 milhões, mais que o dobro. Sua população crescerá mais de 100%. Alternativa <strong>D</strong>.</p><p>A China cresce de 1.275 para 1.462, taxa positiva (A); a Indonésia cresce cerca de 47% e os EUA cerca de 40% (C).</p>",
  F_POPS, ["crescimento populacional", "leitura de gráfico"], enun=POPS + p(T(23, 0)), alts=ALTS(23))
X(24, "M", "Matemática", "Porcentagem", "<p>De 2000 a 2050, a Índia passa de 1.008 para 1.572 milhões: fator 1.572 ÷ 1.008 ≈ 1,56. Mantida a taxa, em 2100: 1.572 × 1,56 ≈ 2.452 milhões, ou cerca de 2,45 bilhões, superior a 2,3. Alternativa <strong>E</strong>.</p>",
  F_POPS, ["crescimento percentual"], enun=POPS + p(T(24, 0)), alts=ALTS(24))
X(25, "M", "Matemática", "Funções", "<p>Em 2004, as vendas cresceram em ritmo constante: cerca de 0,1 milhão por mês (o gráfico 1 é uma reta). A meta de 2005 era crescer mais rápido que isso. No gráfico 2, os saltos claramente maiores que esse ritmo são os de abril (de cerca de 6,45 para 6,8), agosto (de 7,0 para 7,7) e novembro (de 7,6 para 8,0). Nos outros meses, as vendas sobem pouco, no ritmo de 2004, ficam paradas ou até caem (outubro). Alternativa <strong>D</strong>.</p>",
  figs(("q25", "Gráfico 1, vendas em 2004 (milhões de reais), de janeiro a dezembro: cresce de forma quase linear, de cerca de 5,0 a 6,2. Gráfico 2, vendas em 2005: cresce em degraus, com aumentos maiores em alguns meses e quase nenhum em outros, de cerca de 6,2 a 8,0.")),
  ["taxa de variação", "leitura de gráfico"], enun=p(T(25, 0)) + "[[fig:1]]" + ap(T(25, 2).split(" Pela análise")[0]) + p("Pela análise" + T(25, 2).split(" Pela análise")[1]), alts=ALTS(25))
X(26, "M", "Matemática", "Porcentagem", "<p>A meta é que no máximo 5% das chamadas fiquem sem atendimento em 15 minutos. Proporções acumuladas: 6/100 = 6%; 11/200 = 5,5%; 17/300 ≈ 5,7%; 21/400 = 5,25%; 24/482 ≈ 4,98%. Só ao final do dia a taxa ficou abaixo de 5%. Alternativa <strong>E</strong>.</p>",
  tags=["porcentagem", "leitura de tabela"],
  enun=p(T(26, 0)) + tabela(["total acumulado de chamadas", "100", "200", "300", "400", "482"], [["número acumulado de chamadas não atendidas em 15 minutos", "6", "11", "17", "21", "24"]]) + p(T(26, 3)), alts=ALTS(26))
X(27, "H", "Geografia", "Economia", "<p>No gráfico, a inflação brasileira despenca depois do pico de 2003 e, em 2006, fecha em 2,57%, abaixo dos 3,55% dos EUA. O título adequado é “Brasil: inflação acumulada em 12 meses menor que a dos EUA”. Alternativa <strong>A</strong>.</p><p>A inflação brasileira oscilou muito, com pico de cerca de 14% em 2003, então não foi estável (C), e nada no gráfico indica hiperinflação nos EUA (E).</p>",
  figs(("q27", "Gráfico “Inflação acumulada em 12 meses no Brasil e nos EUA, segundo índices de preços ao consumidor”, de 2001 a 2006: o Brasil (linha contínua) sobe até cerca de 14% em 2003 e cai até 2,57% em 2006; os EUA (linha pontilhada) oscilam entre 1% e 4%, terminando em 3,55%.")),
  ["inflação", "leitura de gráfico"], enun=p(T(27, 0).replace("caderno Economia & Negócios", "caderno <em>Economia &amp; Negócios</em>").replace("jornal O Estado de S. Paulo", "jornal <em>O Estado de S. Paulo</em>")) + "[[fig:1]]" + p(T(27, 2)), alts=ALTS(27))
X(28, "N", "Física", "Astronomia", "<p>Vista do hemisfério sul, a Lua com a metade esquerda iluminada está no quarto crescente. Pelo padrão do texto (nova: nasce às 6 h; cheia: nasce às 18 h), a crescente nasce por volta do meio-dia e se põe por volta da meia-noite. O ponto mais alto fica no meio desse percurso, por volta das seis horas da tarde. Alternativa <strong>E</strong>.</p><p>No hemisfério norte, a mesma fase aparece iluminada do lado direito.</p>",
  figs(("q28", "Fotografia da Lua com metade do disco iluminada, em forma de meia-lua.")), ["fases da Lua"], enun="[[fig:1]]" + ap(T(28, 1).split(" Sendo assim,")[0]) + p("Sendo assim," + T(28, 1).split(" Sendo assim,")[1]), alts=ALTS(28))
X(29, "H", "Geografia", "Meio ambiente", "<p>No gráfico, a União Europeia emite entre 5 e 10 toneladas de CO<sub>2</sub> per capita, faixa em que também estão emergentes como China, México, Chile e Argentina. Alternativa <strong>A</strong>.</p><p>Os EUA emitem bem mais por pessoa que a China (B), e somar emissões per capita de países diferentes não dá o total de nenhum deles (C).</p>",
  figs(("q29", "Gráfico de barras horizontais das emissões médias anuais de CO2 per capita (toneladas), em faixas: Brasil, Índia, Indonésia, países da América Central e Caribe, de 0 a 2; China, México, Chile, Argentina, países da União Europeia e Venezuela, de 2 a 7; Japão, Canadá, Rússia, Ucrânia, Polônia e África do Sul, de 7 a 15; EUA e Austrália, de 15 a 30.")),
  ["emissões de CO2", "leitura de gráfico"], quim=True,
  enun=p(T(29, 0)) + "[[fig:1]]" + fonte("<em>O Estado de S. Paulo</em>, 22/7/2004 (com adaptações).") + p(SP(29, 3, "(com adaptações).")[1]), alts=ALTS(29))
X(30, "N", "Biologia", "Ecologia", "<p>Mais calor intensifica a evaporação e altera condensação e precipitação, com mais enchentes em uns lugares e secas em outros, como diz o texto. As mudanças climáticas interferem nos processos do ciclo da água que envolvem mudanças de estado físico. Alternativa <strong>B</strong>.</p><p>O aquecimento aumenta a evaporação, não reduz (A).</p>",
  tags=["aquecimento global", "ciclo da água"], enun=ap(T(30, 0).split(" As mudanças climáticas previstas")[0]) + p("As mudanças climáticas previstas" + T(30, 0).split(" As mudanças climáticas previstas")[1]), alts=ALTS(30))
X(31, "N", "Física", "Calorimetria", "<p>Massa de gelo derretida = energia ÷ calor latente = 1,6 × 10<sup>22</sup> ÷ 3,2 × 10<sup>5</sup> = 5 × 10<sup>16</sup> kg = 5 × 10<sup>13</sup> t = 50 trilhões de toneladas, entre 40 e 60. Alternativa <strong>B</strong>.</p><p>1 trilhão = 10<sup>12</sup>, e 1 tonelada = 10<sup>3</sup> kg.</p>",
  tags=["calor latente", "notação científica"],
  enun=ap(T(31, 0).replace("1 W/m2", "1 W/m<sup>2</sup>").replace("1,6 × 1022 J", "1,6 × 10<sup>22</sup> J")) + p(T(31, 1).replace("3,2 × 105 J", "3,2 × 10<sup>5</sup> J")), alts=ALTS(31))
X(32, "N", "Química", "Química ambiental", "<p>Os óxidos de nitrogênio e enxofre são levados pelos ventos para longe das fontes antes de virarem chuva. O alcance dos efeitos depende da circulação atmosférica e da quantidade de fontes emissoras. Alternativa <strong>A</strong>.</p><p>Rios e lençóis freáticos não transportam os poluentes atmosféricos para outros países (B, C, D, E).</p>",
  tags=["chuva ácida", "circulação atmosférica"], enun=ap(T(32, 0).split(" A amplitude")[0]) + p("A amplitude" + T(32, 0).split(" A amplitude")[1]), alts=ALTS(32))
X(33, "N", "Biologia", "Ecologia", "<p>As florestas absorvem CO<sub>2</sub> na fotossíntese e guardam o carbono na biomassa. Assim, ajudam a controlar o efeito estufa causado pelo acúmulo de carbono vindo da queima de combustíveis fósseis. Alternativa <strong>D</strong>.</p><p>O CO<sub>2</sub> não é a causa da chuva ácida, da destruição do ozônio nem da eutrofização (A, C, E).</p>",
  tags=["sequestro de carbono", "efeito estufa"], enun=ap(T(33, 0).split(" Conclui-se, portanto,")[0]) + p("Conclui-se, portanto," + T(33, 0).split(" Conclui-se, portanto,")[1]), alts=ALTS(33))
X(34, "N", "Biologia", "Reprodução", "<p>I está certa: na partenogênese só nascem fêmeas, e nas bissexuadas cerca de metade são fêmeas. III está certa: como todas as fêmeas põem ovos, x fêmeas produzem o dobro de descendentes de x indivíduos bissexuados (metade machos). II é falsa: o texto não diz isso, e nada garante que a população partenogenética desapareça. Alternativa <strong>C</strong>.</p>",
  tags=["partenogênese"],
  enun=ap(T(34, 0).split(" Avalie as afirmações")[0]) + p("Avalie as afirmações seguintes, relativas a esse processo de reprodução.")
       + I3("Na partenogênese, as fêmeas dão origem apenas a fêmeas, enquanto, nas populações bissexuadas, cerca de 50% dos filhotes são fêmeas.", "Se uma população bissexuada se mistura com uma que se reproduz por partenogênese, esta última desaparece.", "Na partenogênese, um número x de fêmeas é capaz de produzir o dobro do número de descendentes de uma população bissexuada de x indivíduos, uma vez que, nesta, só a fêmea põe ovos.")
       + p("É correto o que se afirma"), alts=ALTS(34))
X(35, "N", "Biologia", "Fisiologia vegetal", "<p>A Mata Atlântica é úmida o ano todo e não tem seca intensa. A planta pode manter os estômatos abertos tanto no tempo chuvoso quanto na seca, fechando-os apenas no horário mais quente (14 h). É a tabela E. Alternativa <strong>E</strong>.</p><p>As tabelas com linha de seca intensa (A, B, D) descrevem ambientes como a caatinga.</p>",
  figs(("q35", "Tabela da planta da caatinga, com as horas do dia (8 h, 10 h, 12 h, 14 h, 16 h, 17 h): tempo chuvoso 2, 2, 2, 0, 2, 2; seca 1, 1, 0, 0, 0, 0; seca intensa 0 em todos os horários. Legenda: 0 = estômatos completamente fechados; 1 = parcialmente abertos; 2 = completamente abertos."),
       ("q35a", "Tabela A: tempo chuvoso 2, 2, 2, 0, 2, 2; seca 1, 1, 0, 0, 1, 1; seca intensa 1, 1, 0, 0, 0, 0."), ("q35b", "Tabela B: tempo chuvoso 1 em todos os horários; seca 1, 1, 0, 0, 1, 1; seca intensa 0 em todos."),
       ("q35c", "Tabela C: tempo chuvoso 1, 1, 0, 0, 0, 0; seca 1, 1, 0, 0, 0, 0."), ("q35d", "Tabela D: seca 1, 1, 0, 0, 0, 0; seca intensa 0 em todos os horários."),
       ("q35e", "Tabela E: tempo chuvoso 2, 2, 2, 0, 2, 2; seca 2, 2, 2, 0, 2, 2.")),
  ["estômatos", "transpiração"],
  enun=p(T(35, 0)) + "[[fig:1]]" + p("Considerando a mesma legenda dessa tabela, assinale a opção que melhor representa o comportamento dos estômatos de uma planta típica da Mata Atlântica."), alts=ALT(2))
X(36, "N", "Biologia", "Ecologia", "<p>Lendo da camada mais antiga (embaixo) para a mais recente (em cima): esporos de samambaias e pólen de cipós e epífitas indicam floresta úmida; depois, pólen de gramíneas indica campos cerrados; por fim, pólen de cactos indica caatinga. Alternativa <strong>A</strong>.</p>",
  figs(("q36", "Esquema de camadas de sedimentos: nas mais antigas (embaixo), muitos esporos de samambaias e pólen de cipós e epífitas; no meio, predomínio de pólen de gramíneas e quase nenhum de epífitas; nas mais recentes (em cima), abundância de pólen de cactos.")),
  ["paleobotânica", "biomas"], enun=p(T(36, 0)) + "[[fig:1]]" + p(T(36, 2)), alts=ALTS(36))
X(37, "N", "Biologia", "Ecologia", "<p>I é falsa: perder 3% ao ano não transforma o cerrado em deserto até 2030 (e o desmatamento não equivale a desertificação imediata). II é falsa: o cerrado tem grande biodiversidade e abriga nascentes de bacias importantes, então sua perda afetaria outros biomas. III é verdadeira: bioinseticidas poluem menos a água que os agrotóxicos. Alternativa <strong>B</strong>.</p>",
  tags=["cerrado", "impacto ambiental"],
  enun=ap(T(37, 0).split(" A respeito desse assunto")[0]) + p("A respeito desse assunto, analise as afirmações abaixo.")
       + I3("Considerando-se que, em 2006, restem apenas 25% da cobertura vegetal original do cerrado e que, desse percentual, 3% sejam derrubados a cada ano, estima-se que, em 2030, o cerrado brasileiro se transformará em deserto.", "Sabe-se que a eventual extinção do bioma cerrado, dada a pobreza que o caracteriza, não causará impacto sistêmico no conjunto dos biomas brasileiros.", "A substituição de agrotóxicos por bioinseticidas reduz a contaminação dos recursos hídricos no bioma cerrado.")
       + p("É correto o que se afirma"), alts=ALTS(37))
X(38, "N", "Química", "Química ambiental", "<p>O principal problema descrito são os compostos organoclorados despejados nos rios com a água industrial. Tratar essa água antes de devolvê-la, degradando esses compostos, ataca a causa. Alternativa <strong>D</strong>.</p><p>Legislação mais branda (A) e menos reflorestamento (B) piorariam a situação.</p>",
  tags=["indústria de papel", "organoclorados"],
  enun=ap(T(38, 0)) + fonte("Celênia P. Santos et al. Papel: como se fabrica? In: <em>Química nova na escola</em>, n.° 14, nov./2001, p. 3-7 (com adaptações).") + p(SP(38, 2, "(com adaptações).")[1]), alts=ALTS(38))
X(39, "H", "Geografia", "Mineração", "<p>O poema mostra uma serra inteira triturada e levada pelo trem de minério, deixando “pó de ferro”. As três medidas respondem a isso: controlar novas mineradoras (I), reduzir o impacto na área degradada (II) e reaproveitar materiais para extrair menos (III). Alternativa <strong>E</strong>.</p>",
  figs(("q39", "Fragmento de poema de Carlos Drummond de Andrade, em versos livres: o eu lírico acorda e não encontra mais a sua serra, que foi britada em bilhões de lascas e levada em vagões pelo maior trem do mundo, deixando no seu corpo apenas um pó de ferro que não passa.")),
  ["mineração", "impacto ambiental"],
  enun="[[fig:1]]" + fonte("Carlos Drummond de Andrade. <em>Antologia poética</em>. Rio de Janeiro: Record, 2000.") + p("A situação poeticamente descrita acima sinaliza, do ponto de vista ambiental, para a necessidade de")
       + I3("manter-se rigoroso controle sobre os processos de instalação de novas mineradoras.", "criarem-se estratégias para reduzir o impacto ambiental no ambiente degradado.", "reaproveitarem-se materiais, reduzindo-se a necessidade de extração de minérios.") + p("É correto o que se afirma"), alts=ALTS(39))
X(40, "H", "Geografia", "Recursos hídricos", "<p>O texto mostra que o aquífero é muito desigual: em algumas áreas a água é ótima, em outras é inacessível, salina ou não potável. Para aproveitá-lo como reservatório de água potável, é preciso conhecê-lo em detalhe. Alternativa <strong>C</strong>.</p><p>A água do compartimento Norte-Alto Uruguai não é potável e alcaliniza o solo, não o acidifica (D, E).</p>",
  figs(("q40", "Mapa do Sistema Aquífero Guarani no Centro-Sul do Brasil e em partes do Paraguai, Argentina e Uruguai, com as áreas de afloramento e de confinamento e cidades como Campo Grande, São Paulo, Curitiba, Florianópolis, Porto Alegre, Assunção, Buenos Aires e Montevidéu.")),
  ["aquífero Guarani", "água subterrânea"], enun=ap(T(40, 0).replace("km2", "km<sup>2</sup>")) + "[[fig:1]]" + fonte("<em>Scientific American Brasil</em>, n.º 47, abr./2006 (com adaptações).") + p(T(40, 3)), alts=ALTS(40))
X(41, "H", "Geografia", "Recursos hídricos", "<p>Reciclar a água industrial (I) e fazer saneamento e tratamento de esgoto (III) reduzem a poluição na origem. Transpor água de outros mananciais (II) só dilui o problema e prejudica outras bacias. Alternativa <strong>C</strong>.</p>",
  tags=["poluição dos rios", "saneamento"],
  enun=ap(T(41, 0).split(" Avalie se")[0]) + p("Avalie se as ações apresentadas abaixo são adequadas para se reduzir a poluição desses rios.")
       + I3("Investir em mecanismos de reciclagem da água utilizada nos processos industriais.", "Investir em obras que viabilizem a transposição de águas de mananciais adjacentes para os rios poluídos.", "Implementar obras de saneamento básico e construir estações de tratamento de esgotos.") + p("É adequado o que se propõe"), alts=ALTS(41))
X(42, "H", "Geografia", "Indicadores sociais", "<p>Em todos os países, a mortalidade infantil cai quanto maior a escolaridade da mãe, mesmo onde o saneamento é precário (como no país I, com 33% de esgotamento). A educação tem relação direta com a saúde. Alternativa <strong>A</strong>.</p><p>No país I, com abastecimento abaixo de 50%, a escolaridade também reduz a mortalidade (B).</p>",
  tags=["mortalidade infantil", "escolaridade"],
  enun=p(T(42, 0)) + tabela(["país", "esgotamento sanitário adequado (%)", "abastecimento de água (%)", "mortalidade infantil (por mil): mães com até 3 anos na escola", "de 4 a 7 anos", "8 ou mais anos"],
                            [["I", "33", "47", "45,1", "29,6", "21,4"], ["II", "36", "65", "70,3", "41,2", "28,0"], ["III", "81", "88", "34,8", "27,4", "17,7"], ["IV", "62", "79", "33,9", "22,5", "16,4"], ["V", "40", "73", "37,9", "25,1", "19,3"]])
       + p("Com base nessas informações, infere-se que"), alts=ALTS(42))
X(43, "N", "Biologia", "Ecologia", "<p>No sistema convencional, os pés de cacau ficam muito próximos uns dos outros. Como o fungo se espalha por esporos no ar, a proximidade facilita a disseminação da doença. Alternativa <strong>B</strong>.</p><p>O fungo se reproduz em ambiente quente e úmido, não em ambiente seco e ensolarado (A).</p>",
  tags=["vassoura-de-bruxa", "monocultura"], enun=ap(T(43, 0), T(43, 1)) + p(T(43, 2).replace("vassoura-debruxa", "vassoura-de-bruxa")), alts=ALTS(43))
X(44, "N", "Química", "Química e ambiente", "<p>A substância sintética é usada como isca para atrair os besouros para longe da plantação. A finalidade é afastar a praga da cana, e a vantagem ambiental é reduzir a necessidade de agrotóxicos. Alternativa <strong>B</strong>.</p><p>A isca não elimina nem extermina os besouros (A, C), e não há como garantir o fim do uso de agrotóxicos.</p>",
  tags=["feromônio", "controle biológico"],
  enun=ap(T(44, 0)) + fonte("Folha Ciência. In: <em>Folha de S. Paulo</em>, 25/5/2004 (com adaptações).") + p(T(44, 2)),
  alts=A5("finalidade: eliminar os besouros; vantagem ambiental: reduzir as espécies que se alimentam da cana-de-açúcar.", "finalidade: afastar os predadores da plantação; vantagem ambiental: reduzir a necessidade de uso de agrotóxicos.",
          "finalidade: exterminar os besouros; vantagem ambiental: eliminar o uso de agrotóxicos.", "finalidade: dispersar os besouros; vantagem ambiental: evitar a incidência de novas pragas.", "finalidade: afastar os predadores da plantação; vantagem ambiental: aumentar a resistência dos canaviais."))
X(45, "N", "Biologia", "Fisiologia humana", "<p>No esquema, quanto mais alto, maior a afinidade pela COX-1, e quanto mais baixo, maior a afinidade pela COX-2. O piroxicam está no topo: é o que mais inibe a COX-1, responsável pelas prostaglandinas que protegem a mucosa gástrica. Alternativa <strong>A</strong>.</p><p>O rofecoxibe, embaixo, tem a maior afinidade pela COX-2 (B).</p>",
  figs(("q45", "Esquema com anti-inflamatórios em coluna, de cima para baixo: piroxicam, aspirina, ibuprofeno, meloxicam, diclofenaco, naproxeno, nimesulide, celecoxibe e rofecoxibe. Uma seta indica que a afinidade por COX-1 aumenta para cima e a afinidade por COX-2 aumenta para baixo.")),
  ["anti-inflamatórios", "enzimas"], enun=ap(T(45, 0).replace("antiinflamatórios", "anti-inflamatórios"), T(45, 1).replace("antiinflamatórios", "anti-inflamatórios"), T(45, 2).replace("antiinflamatórios", "anti-inflamatórios")) + "[[fig:1]]" + p(T(45, 4)), alts=ALTS(45))
X(46, "N", "Biologia", "Saúde", "<p>I: com mais prevenção, os novos casos caem de cerca de 1.900 mil (2005) para cerca de 1.420 mil (2008): uma queda de cerca de 25%, mais de 20%. II é falsa: a curva com maior prevenção cai cerca de 6% a 15% por ano, não 25%. III é falsa: sem mais prevenção, os casos vão de cerca de 1.980 mil (2005) para cerca de 2.390 mil (2010), um aumento de cerca de 20%, bem menor que 50%. Alternativa <strong>A</strong>.</p>",
  figs(("q46", "Gráfico do número de novas infecções por HIV entre jovens (em milhares), de 2005 a 2010: com a prevenção atual, a curva sobe devagar de cerca de 2.000 para 2.400; com maior prevenção, cai de cerca de 1.900 para 1.100.")),
  ["prevenção de HIV", "leitura de gráfico"],
  enun=p(T(46, 0).replace("relatório Salvando vidas: o direito das crianças ao tratamento de HIV e AIDS", "relatório <em>Salvando vidas: o direito das crianças ao tratamento de HIV e AIDS</em>")) + "[[fig:1]]" + p("Com base nesses dados, analise as seguintes afirmações.")
       + I3("Ações educativas de prevenção da transmissão do vírus HIV poderão contribuir para a redução, em 2008, de mais de 20% dos novos casos de infecção entre os jovens, em relação ao ano de 2005.", "Ações educativas relativas à utilização de preservativos nas relações sexuais reduzirão em 25% ao ano os novos casos de AIDS entre os jovens.", "Sem o aumento de medidas de prevenção primária, estima-se que, em 2010, o aumento de novos casos de infecção por HIV entre os jovens será, em relação ao ano de 2005, 50% maior.")
       + p("É correto apenas o que se afirma em"), alts=ALTS(46))
X(47, "N", "Biologia", "Nutrição", "<p>I é falsa: o consumo de proteínas e grãos (ovos, peixes, feijão, arroz) diminuiu, e o que aumentou foram biscoitos, refrigerantes, salsichas e refeições prontas. II e III são verdadeiras: o aumento de alimentos calóricos leva à obesidade, que reduz a expectativa de vida e favorece doenças cardiovasculares. Alternativa <strong>E</strong>.</p>",
  figs(("q47", "Infográfico “Dieta de engorda – em 30 anos, a alimentação piorou muito”. Aumento no consumo por família: biscoitos 400%, refrigerantes 400%, salsichas e linguiças 300%, refeições prontas 80%. Diminuição no consumo: ovos 84%, peixes 50%, feijão e leguminosas 30%, arroz 23%.")),
  ["alimentação", "obesidade"],
  enun="[[fig:1]]" + fonte("<em>Época</em>, 8/5/2006 (com adaptações).") + p("A partir desses dados, foram feitas as afirmações abaixo.")
       + I3("As famílias brasileiras, em 30 anos, aumentaram muito o consumo de proteínas e grãos, que, por seu alto valor calórico, não são recomendáveis.", "O aumento do consumo de alimentos muito calóricos deve ser considerado indicador de alerta para a saúde, já que a obesidade pode reduzir a expectativa de vida humana.", "Doenças cardiovasculares podem ser desencadeadas pela obesidade decorrente das novas dietas alimentares.")
       + p("É correto apenas o que se afirma em"), alts=ALTS(47))
X(48, "H", "Geografia", "Urbanização", "<p>Pelas datas do infográfico: Cingapura (1975), Noruega (1990), Coreia do Sul (1996) e Inglaterra (2003). Se a cidade brasileira adotar o pedágio, dará sequência a essas experiências, nessa ordem. Alternativa <strong>C</strong>.</p><p>A pioneira foi Cingapura, na Ásia (B), e a Noruega adotou o pedágio para aumentar a receita, mas os outros visavam o trânsito (A).</p>",
  figs(("q48", "Infográfico “Os benefícios do pedágio dentro da cidade”: a prefeitura de uma grande cidade brasileira estuda implantar pedágio urbano. Cingapura: adotado em 1975, reduziu 15% do tráfego e elevou a velocidade média em 10 km/h. Inglaterra: desde 2003, Londres cobra o equivalente a 35 reais por dia e reduziu o tráfego em 30%. Noruega: em 1990, Oslo instalou pedágio para aumentar a receita, que hoje é de 70 milhões de dólares por ano. Coreia do Sul: desde 1996, Seul cobra o equivalente a 4,80 reais; a quantidade de veículos caiu 34% e a velocidade subiu 10 km/h.")),
  ["pedágio urbano", "trânsito"], enun="[[fig:1]]" + fonte("<em>Veja</em>, 28/6/2006 (com adaptações).") + p(T(48, 2)), alts=ALTS(48))
X(49, "N", "Química", "Cálculos químicos", "<p>Rendimento = 1,5 kg ÷ 1.000 kg = 0,0015 = 0,15%. Alternativa <strong>B</strong>.</p><p>Uma tonelada tem 1.000 kg; quem esquece a conversão chega a 1,5% (D).</p><p>Esse rendimento tão baixo explica a grande quantidade de rejeito gerada na mineração de urânio.</p>",
  tags=["porcentagem em massa", "urânio"], enun=p(T(49, 0).split(" A 0,10%")[0].replace("matériaprima", "matéria-prima")), alts=A5("0,10%.", "0,15%.", "0,20%.", "1,5%.", "2,0%."))
X(50, "N", "Física", "Física nuclear", "<p>O texto diz que o plutônio, usado em grande parte das armas nucleares, é produzido nos reatores das usinas. Logo, um subproduto das usinas pode virar material bélico. Alternativa <strong>C</strong>.</p><p>As usinas usam urânio pouco enriquecido (4%), não produzem urânio para bombas (D).</p>",
  tags=["fissão nuclear", "plutônio"], enun=ap(T(50, 0).split(" Considerando-se essas")[0]) + p("Considerando-se essas" + T(50, 0).split(" Considerando-se essas")[1]), alts=ALTS(50))
X(51, "N", "Física", "Energia", "<p>I é falsa: Itaipu gera mais por ano (93 contra 84 bilhões de kWh), mas tem potência instalada menor (12.600 contra 18.200 MW). II é verdadeira: Itaipu produz mais energia com menos potência. III é verdadeira: Três Gargantas tem 18,2 MW por km² inundado, contra 9 MW/km² de Itaipu. Alternativa <strong>E</strong>.</p>",
  tags=["hidrelétricas", "eficiência"],
  enun=p(T(51, 0)) + tabela(["parâmetros", "Itaipu", "Três Gargantas"], [["potência instalada", "12.600 MW", "18.200 MW"], ["produção efetiva de energia elétrica", "93 bilhões de kWh/ano", "84 bilhões de kWh/ano"], ["área inundada pelo reservatório", "1.400 km<sup>2</sup>", "1.000 km<sup>2</sup>"]])
       + fonte("Internet: &lt;www.itaipu.gov.br&gt;.") + p("Com base nessas informações, avalie as afirmativas que se seguem.")
       + I3("A energia elétrica gerada anualmente e a capacidade nominal máxima de geração da hidrelétrica de Itaipu são maiores que as da hidrelétrica de Três Gargantas.", "Itaipu é mais eficiente que Três Gargantas no uso da potência instalada na produção de energia elétrica.", "A razão entre potência instalada e área inundada pelo reservatório é mais favorável na hidrelétrica Três Gargantas do que em Itaipu.")
       + p("É correto apenas o que se afirma em"), alts=ALTS(51))
CARN = (ap("O carneiro hidráulico ou aríete, dispositivo usado para bombear água, não requer combustível ou energia elétrica para funcionar, visto que usa a energia da vazão de água de uma fonte. A figura a seguir ilustra uma instalação típica de carneiro em um sítio, e a tabela apresenta dados de seu funcionamento.") + "[[fig:1]]"
        + tabela(["h/H (altura da fonte dividida pela altura da caixa)", "V<sub>f</sub> (água da fonte necessária para o funcionamento do sistema, litros/hora)", "V<sub>b</sub> (água bombeada para a caixa, litros/hora)"],
                 [["1/3", "720 a 1.200", "180 a 300"], ["1/4", "720 a 1.200", "120 a 210"], ["1/6", "720 a 1.200", "80 a 140"], ["1/8", "720 a 1.200", "60 a 105"], ["1/10", "720 a 1.200", "45 a 85"]])
        + p("A eficiência energética " + K("\\varepsilon") + " de um carneiro pode ser obtida pela expressão " + K("\\varepsilon = \\dfrac{H}{h} \\times \\dfrac{V_b}{V_f}") + ", cujas variáveis estão definidas na tabela e na figura."))
F_CARN = figs(("q52", "Ilustração de um sítio: a água desce de uma fonte, à altura h, até o carneiro, no ponto mais baixo, que a bombeia para uma caixa d’água elevada, à altura H."))
X(52, "N", "Física", "Energia", "<p>Com H = 4h, h/H = 1/4: V<sub>b</sub> de 120 a 210 L/h para V<sub>f</sub> de 720 a 1.200 L/h. A eficiência é 4 × V<sub>b</sub>/V<sub>f</sub> ≈ 4 × 120/720 ≈ 67% (ou 4 × 210/1.200 = 70%), maior que os 36% da motobomba, e sem combustível. Alternativa <strong>E</strong>.</p>",
  F_CARN, ["eficiência energética", "razão"], enun=CARN + p(T(52, 0)), alts=ALTS(52))
X(53, "M", "Matemática", "Razão e proporção", "<p>H = 5h dá h/H = 1/5, entre 1/4 (120 a 210 L/h) e 1/6 (80 a 140 L/h). O volume bombeado em 1 hora deve ficar entre esses intervalos, algo como de 100 a 175 litros. Alternativa <strong>D</strong>.</p><p>Os limites de D ficam aproximadamente no meio dos intervalos de 1/4 e 1/6.</p>",
  F_CARN, ["interpolação", "leitura de tabela"], enun=CARN + p(T(53, 0)), alts=ALTS(53))
X(54, "N", "Física", "Energia", "<p>Cada turbina tem 240 ÷ 24 = 10 MW. Aos domingos a demanda cai 40%: 0,6 × 240 = 144 MW. I: 24 × 6 = 144. II: 12 × 10 + 12 × 2 = 144. III: 14 × 10 + 4 = 144. As três dão 144 MW. Alternativa <strong>E</strong>.</p>",
  tags=["potência", "porcentagem"],
  enun=ap(T(54, 0), T(54, 1).split(" I todas")[0]) + I3("todas as turbinas em funcionamento, com 60% da capacidade máxima de produção de cada uma delas.", "a metade das turbinas funcionando em capacidade máxima e o restante, com 20% da capacidade máxima.", "quatorze turbinas funcionando em capacidade máxima, uma com 40% da capacidade máxima e as demais desligadas.") + p("Está correta a situação descrita"), alts=ALTS(54))
X(55, "H", "Geografia", "Clima", "<p>A evaporação é favorecida por pouca chuva (que diluiria a água) e muito vento (que retira o vapor), e o terreno plano permite formar as salinas. Alternativa <strong>B</strong>.</p><p>É o caso das salinas do litoral do Rio Grande do Norte.</p>",
  tags=["salinas", "evaporação"], enun=p(T(55, 0)), alts=ALTS(55))
OIE = (ap("Para se discutirem políticas energéticas, é importante que se analise a evolução da Oferta Interna de Energia (OIE) do país. Essa oferta expressa as contribuições relativas das fontes de energia utilizadas em todos os setores de atividade. O gráfico a seguir apresenta a evolução da OIE no Brasil, de 1970 a 2002.") + "[[fig:1]]" + fonte("Ministério de Minas e Energia – MME/Brasil."))
F_OIE = figs(("q56", "Gráfico de áreas “Oferta Interna de Energia (%)”, de 1970 a 2002: petróleo e derivados crescem de cerca de 40% para cerca de 45%; lenha e carvão vegetal caem de cerca de 45% para cerca de 12%; hidrelétrica cresce de cerca de 5% para cerca de 14%; derivados da cana-de-açúcar crescem de cerca de 5% para cerca de 12%; gás natural e carvão mineral aumentam um pouco; outras fontes ocupam uma faixa fina no topo."))
X(56, "N", "Física", "Energia", "<p>Em 1970, lenha e carvão vegetal eram quase metade da oferta; em 2002, caíram muito. Hidreletricidade e derivados da cana cresceram, mas não o suficiente para compensar: a fatia renovável diminuiu. Alternativa <strong>B</strong>.</p><p>Carvão mineral não é renovável (A), e gás natural também não (E).</p>",
  F_OIE, ["matriz energética", "fontes renováveis"], enun=OIE + p(T(56, 0)), alts=ALTS(56))
X(57, "N", "Física", "Energia", "<p>A tendência de 1970 a 2002 é: petróleo e derivados estáveis ou crescendo, lenha e carvão vegetal diminuindo, hidrelétrica e derivados da cana aumentando. A projeção que continua essas faixas com a mesma tendência é a do gráfico C. Alternativa <strong>C</strong>.</p><p>As cinco projeções são parecidas, e a imagem da prova original tem pouca resolução: a diferença entre elas está na largura relativa das faixas. O gabarito oficial é C.</p>",
  F_OIE + figs(("q57a", "Projeção A para 2002-2010, com mudança brusca nas faixas."), ("q57b", "Projeção B para 2002-2010."), ("q57c", "Projeção C para 2002-2010, que prolonga as faixas com as tendências do período anterior."), ("q57d", "Projeção D para 2002-2010."), ("q57e", "Projeção E para 2002-2010.")),
  ["matriz energética", "tendência"], enun=OIE + p(T(57, 0)), alts=ALT(2))
X(58, "N", "Física", "Energia", "<p>A combustão da parafina (processo químico) derrete e faz pingar a ponta mais baixa, que fica mais leve; a vela gira, mudando a energia potencial gravitacional das pontas, e esse movimento é energia cinética. Sequência: química → potencial gravitacional → cinética. Alternativa <strong>A</strong>.</p>",
  figs(("q58", "Desenho de uma vela deitada, apoiada pelo meio sobre um suporte, com as duas pontas acesas, sobre uma bandeja.")), ["transformação de energia"], enun=p(T(58, 0)) + "[[fig:1]]", alts=ALTS(58))
X(59, "M", "Matemática", "Geometria espacial", "<p>Tipo I: perímetro da base 20 cm, então r = 10/π e altura 10 cm; V = π(10/π)² × 10 = 1.000/π. Tipo II: perímetro 10 cm, r = 5/π, altura 20 cm; V = π(5/π)² × 20 = 500/π. A vela do tipo I tem o dobro do volume e custa o dobro. Alternativa <strong>B</strong>.</p>",
  figs(("q59a", "Tipo I: cilindro largo e baixo, formado unindo os lados de 10 cm do cartão (altura 10 cm, contorno de 20 cm)."), ("q59b", "Tipo II: cilindro estreito e alto, formado unindo os lados de 20 cm do cartão (altura 20 cm, contorno de 10 cm).")),
  ["volume do cilindro"], enun=p(T(59, 0)) + "[[fig:1]]" + p("<strong>Tipo I</strong>") + "[[fig:2]]" + p("<strong>Tipo II</strong>") + p(T(59, 5)), alts=ALTS(59))
X(60, "M", "Matemática", "Grandezas e medidas", "<p>O desnível entre o nível alto e a jusante é de 20 m. Volume a esvaziar: 200 × 17 × 20 = 68.000 m³. A 4.200 m³/min: 68.000 ÷ 4.200 ≈ 16 minutos. Alternativa <strong>D</strong>.</p><p>O desnível de 20 m está marcado no esquema, entre o nível de cima e o nível da jusante. Os 6 m de baixo continuam com água, por isso não entram na conta.</p>",
  figs(("q60", "Esquema da eclusa em corte: a câmara entre a porta 1 (lado do nível alto) e a porta 2 (lado da jusante), com desnível de 20 m entre o nível de cima e o da jusante e 6 m de profundidade abaixo da jusante; válvula de enchimento e válvula de dreno embaixo. Abaixo, desenho da câmara em forma de bloco e o texto: enquanto a válvula de enchimento está fechada e a de dreno aberta, a água sai e a câmara esvazia até o nível da jusante; então a porta 2 é aberta e a embarcação segue rio abaixo.")),
  ["volume", "vazão"], enun=p(T(60, 0)) + "[[fig:1]]" + p(T(60, 3).replace("m3", "m<sup>3</sup>")), alts=ALTS(60))
X(61, "N", "Física", "Mecânica", "<p>Para empurrar a prancha de A para B, as lixas em contato com ela devem se mover nesse sentido. Os grupos de cima (1 e 2) tocam a prancha pela parte de baixo da correia e precisam girar no sentido anti-horário; os de baixo (3 e 4) tocam pela parte de cima e giram no sentido horário. Alternativa <strong>C</strong>.</p>",
  figs(("q61", "Esquema de lixadeira com quatro grupos de polias: grupos 1 e 2 em cima e 3 e 4 embaixo, cada um com duas polias ligadas por correia; a prancha passa entre os grupos de cima e de baixo, da esquerda (A) para a direita (B).")),
  ["movimento circular", "polias"], enun=p(T(61, 0).replace("utilizase", "utiliza-se")) + "[[fig:1]]" + p(T(61, 3)), alts=ALTS(61))
X(62, "M", "Matemática", "Geometria plana", "<p>Cada degrau tem 24 cm de profundidade e 90 ÷ 5 = 18 cm de altura. O trecho inclinado do corrimão acompanha os 5 degraus: 5 × 24 = 120 cm na horizontal e 90 cm na vertical. Pelo teorema de Pitágoras, mede √(120² + 90²) = 150 cm. Somando os dois trechos horizontais de 30 cm: 150 + 30 + 30 = 210 cm = <strong>2,1 m</strong>. Alternativa <strong>D</strong>.</p>",
  figs(("q62", "Projeto de escada de 5 degraus de mesma altura, cada um com 24 cm de profundidade; altura total de 90 cm; corrimão com um trecho horizontal de 30 cm em cima, um trecho inclinado acompanhando os degraus e outro trecho horizontal de 30 cm embaixo, a 90 cm de altura.")),
  ["teorema de Pitágoras"], enun="[[fig:1]]" + p(T(62, 1)), alts=ALTS(62))
X(63, "N", "Química", "Química orgânica", "<p>Com o amadurecimento, a concentração de açúcares sobe e a dos ácidos tartárico e málico cai. Colhidas mais tarde, as uvas dão vinhos mais alcoólicos (mais açúcar para fermentar) e menos ácidos. Alternativa <strong>C</strong>.</p>",
  figs(("q63", "Gráfico da concentração em função do tempo: açúcares aumentam; ácido tartárico e ácido málico diminuem.")), ["fermentação", "leitura de gráfico"],
  enun=p(T(63, 0)) + "[[fig:1]]" + p(T(63, 2), T(63, 3)), alts=ALTS(63))

completar(Q, R)
