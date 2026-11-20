# Enem 2009, 2º dia (06/12/2009), caderno azul: Linguagens, Códigos e suas Tecnologias (questões 91 a 135; no site, 1 a 45). Em 2009 não havia língua estrangeira: prova única.
# Textos compartilhados (Q96–97, Q100–101, Q107–108, Q116–117, Q121–122, Q126–127, Q132–133) montados à mão. Letra de Lobão (Q98) e poemas de Bandeira (Q116–117) e Drummond (Q135) como imagem; Cruz e Sousa (Q99) e Cuitelinho (folclore, Q111) em texto.
# Q101 anulada pelo Inep (sem motivo divulgado).
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, paragrafos_enem

ID = "enem-2009-linguagens"
META = {"id": ID, "banca": "Enem", "ano": 2009, "titulo": "Enem 2009: Linguagens", "fonte": "Inep", "dataExame": "2009-12-06",
        "duracaoMinutos": 150, "area": "Linguagens", "caderno": "azul", "dia": 2}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2009-dia2-azul")
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


def X(n, materia, assunto, expl, imagens=(), tags=(), enun=None, trocas=(), alts=None, anulacao=None, quim=False):
    e = LIMPA(enun or E(n))
    if quim: e = QF(e)
    for a, b in trocas:
        assert a in e, a; e = e.replace(a, b)
    Q[n - 90] = {"materia": materia, "assunto": assunto, "area": "Linguagens", "tags": list(tags), "numeroOriginal": n,
                 "enunciado": e, "alternativas": {k: (QF if quim else str)(LIMPA(v)) for k, v in dict(alts or D[n]["alternativas"]).items()},
                 "imagens": list(imagens), "explicacao": expl}
    if anulacao: Q[n - 90]["anulacao"] = anulacao


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

J = lambda *xs: " ".join(xs)
SEMHIF = lambda d: {k: re.sub(r"(\w)- (\w)", r"\1-\2", v) for k, v in d.items()}
CORTA = lambda n: {**D[n]["alternativas"], "E": re.split(r"\s+Textos? para as questões", D[n]["alternativas"]["E"])[0]}
ESC = lambda s: s.replace("<", "&lt;").replace(">", "&gt;")
VERSOS = lambda *estrofes: "".join('<p class="apoio">' + "<br>".join(e) + "</p>" for e in estrofes)

CAMP = ('<p class="apoio"><strong>Influenza A (Gripe Suína):</strong></p><p class="apoio">Se você esteve ou manteve contato com pessoas da área de risco e apresenta os seguintes sintomas:</p>'
        "<ul><li>Febre alta repentina e superior a 38 graus.</li><li>Tosse.</li><li>Dor de cabeça.</li><li>Dores musculares e nas articulações.</li><li>Dificuldade respiratória.</li></ul>"
        '<p class="apoio">Entre em contato imediatamente com o Disque Epidemiologia: <strong>0800-283-2255.</strong></p><p class="apoio"><strong>Evite a contaminação:</strong></p>'
        "<ul><li>Quando tossir ou espirrar, cubra sua boca e nariz com lenço descartável. Caso não o tenha utilize o antebraço. Se utilizar as mãos lave-as rapidamente com água e sabão.</li>"
        "<li>O uso de máscaras é indicado para prevenir contaminações.</li></ul>" + fonte("BRASIL. Ministério da Saúde, 2009 (adaptado)."))
TIRA = "[[fig:1]]" + fonte("XAVIER, C. <em>Quadrinho quadrado</em>. Disponível em: http://www.releituras.com. Acesso em: 5 jul. 2009.")
F_TIRA = figs(("q100", "Tira em três quadros com o título “Borges falou e disse:”. No primeiro, um entrevistador com microfone pergunta a um senhor de óculos: “Por que o senhor publicou esse livro? Qual foi sua maior motivação?”. No segundo, o senhor responde, exaltado: “Motivação? Meu filho, um escritor publica um livro para parar de escrevê-lo!”. No terceiro, entre pilhas de livros, ele desabafa: “Eu não aguentava mais escrever e reescrever e revisar e acrescentar e suprimir e reescrever e consertar palavrinhas e revisar e reescrever...”."))
PLAST = (tit("Texto I") + ap("É praticamente impossível imaginarmos nossas vidas sem o plástico. Ele está presente em embalagens de alimentos, bebidas e remédios, além de eletrodomésticos, automóveis etc. Esse uso ocorre devido à sua atoxicidade e à inércia, isto é: quando em contato com outras substâncias, o plástico não as contamina; ao contrário, protege o produto embalado. Outras duas grandes vantagens garantem o uso dos plásticos em larga escala: são leves, quase não alteram o peso do material embalado, e são 100% recicláveis, fato que, infelizmente, não é aproveitado, visto que, em todo o mundo, a percentagem de plástico reciclado, quando comparado ao total produzido, ainda é irrelevante.")
         + fonte("<em>Revista Mãe Terra</em>. Minuano, ano I, n. 6 (adaptado).") + tit("Texto II")
         + ap("Sacolas plásticas são leves e voam ao vento. Por isso, elas entopem esgotos e bueiros, causando enchentes. São encontradas até no estômago de tartarugas marinhas, baleias, focas e golfinhos, mortos por sufocamento.", "Sacolas plásticas descartáveis são gratuitas para os consumidores, mas têm um custo incalculável para o meio ambiente.")
         + fonte("<em>Veja</em>, 8 jul. 2009. Fragmentos de texto publicitário do Instituto Akatu pelo Consumo Consciente."))
BAND = "[[fig:1]]" + fonte("BANDEIRA, M. <em>Poesia completa e prosa</em>. Rio de Janeiro: José Aguilar, 1967.")
F_BAND = figs(("q116", "Poema “Canção do vento e da minha vida”, de Manuel Bandeira, em três estrofes com cortes indicados por reticências entre colchetes. Em versos paralelos, o poema repete que o vento varria coisas (primeiro elementos da natureza, depois sonhos, amizades e amores, por fim o tempo e tudo) e, logo em seguida, que a vida do eu lírico ficava cada vez mais cheia justamente daquilo que o vento levava."))
TERENA = (ap("Quando eu falo com vocês, procuro usar o código de vocês. A figura do índio no Brasil de hoje não pode ser aquela de 500 anos atrás, do passado, que representa aquele primeiro contato. Da mesma forma que o Brasil de hoje não é o Brasil de ontem, tem 160 milhões de pessoas com diferentes sobrenomes. Vieram para cá asiáticos, europeus, africanos, e todo mundo quer ser brasileiro. A importante pergunta que nós fazemos é: qual é o pedaço de índio que vocês têm? O seu cabelo? São seus olhos? Ou é o nome da sua rua? O nome da sua praça? Enfim, vocês devem ter um pedaço de índio dentro de vocês. Para nós, o importante é que vocês olhem para a gente como seres humanos, como pessoas que nem precisam de paternalismos, nem precisam ser tratadas com privilégios. Nós não queremos tomar o Brasil de vocês, nós queremos compartilhar esse Brasil com vocês.")
          + fonte("TERENA, M. Debate. MORIN, E. <em>Saberes globais e saberes locais</em>. Rio de Janeiro: Garamond, 2000 (adaptado)."))
DENGUE = ('<p class="apoio"><strong>Sr. Prefeito, junte-se a nós na luta contra a dengue. A sua participação é fundamental.</strong></p>'
          + ap("A dengue é um dos grandes desafios que enfrentamos na área de saúde no Brasil, mas, felizmente, é possível controlá-la. Para isso, é necessário que os governos estaduais e municipais e o governo federal trabalhem juntos. Nesse sentido, a sua atuação como prefeito é fundamental. Organize mutirões, envolvendo líderes comunitários da sua cidade, para lutar contra a dengue. No site <strong>www.combatadengue.com.br</strong> há todas as informações necessárias para auxiliá-lo, inclusive com materiais para <em>download</em> de uso livre. A mobilização social é a chave para o sucesso no cambate à dengue.",
               "Secretarias Estaduais e Municipais de Saúde · SUS · Ministério da Saúde · Governo Federal")
          + fonte("BRASIL. Ministério da Saúde. <em>Revista Nordeste</em>, João Pessoa, ano 3, n. 35, maio/jun. 2009."))
NASSAR = (tit("Texto I") + ap("[...] já foi o tempo em que via a convivência como viável, só exigindo deste bem comum, piedosamente, o meu quinhão, já foi o tempo em que consentia num contrato, deixando muitas coisas de fora sem ceder contudo no que me era vital, já foi o tempo em que reconhecia a existência escandalosa de imaginados valores, coluna vertebral de toda ‘ordem’; mas não tive sequer o sopro necessário, e, negado o respiro, me foi imposto o sufoco; é esta consciência que me libera, é ela hoje que me empurra, são outras agora minhas preocupações, é hoje outro o meu universo de problemas; num mundo estapafúrdio — definitivamente fora de foco — cedo ou tarde tudo acaba se reduzindo a um ponto de vista, e você que vive paparicando as ciências humanas, nem suspeita que paparica uma piada: impossível ordenar o mundo dos valores, ninguém arruma a casa do capeta; me recuso pois a pensar naquilo em que não mais acredito, seja o amor, a amizade, a família, a igreja, a humanidade; me lixo com tudo isso! me apavora ainda a existência, mas não tenho medo de ficar sozinho, foi conscientemente que escolhi o exílio, me bastando hoje o cinismo dos grandes indiferentes [...].")
          + fonte("NASSAR, R. <em>Um copo de cólera</em>. São Paulo: Companhia das Letras, 1992.") + tit("Texto II")
          + ap("Raduan Nassar lançou a novela <em>Um Copo de Cólera</em> em 1978, fervilhante narrativa de um confronto verbal entre amantes, em que a fúria das palavras cortantes se estilhaçava no ar. O embate conjugal ecoava o autoritário discurso do poder e da submissão de um Brasil que vivia sob o jugo da ditadura militar.")
          + fonte("COMODO, R. Um silêncio inquietante. <em>IstoÉ</em>. Disponível em: http://www.terra.com.br. Acesso em: 15 jul. 2009."))
import json as _json
_L128 = _json.load(open("/tmp/claude-0/q128.json"))
PARTIDA = '<p class="apoio"><strong>A partida</strong></p><p class="apoio"><small>(Os números entre colchetes marcam as linhas do texto original.)</small></p><p class="apoio">' + " ".join((f"<small>[{i}]</small> " if i % 3 == 1 else "") + l for i, l in enumerate(_L128, 1)).replace("amor. <small>[10]</small> ", "amor.</p><p class=\"apoio\"><small>[10]</small> ") + "</p>"

X(91, "Artes", "Artes visuais", "<p>Rubem Valentim criou emblemas inspirados em símbolos das religiões afro-brasileiras, como os oxês de Xangô e as ferramentas dos orixás. A obra A é a que representa a arte de origem negro-africana. Alternativa <strong>A</strong>.</p><p>Athos Bulcão (azulejos), Gerchman (pop), Vasarely (op art) e o mosaico de inspiração clássica não têm essa matriz.</p>",
  figs(("q91a", "Obra de Rubem Valentim: emblemas geométricos em preto e cinza, que lembram ferramentas e símbolos de orixás, dispostos em fileiras sobre fundo branco."),
       ("q91b", "Obra de Athos Bulcão: painel de azulejos com padrão repetido de curvas entrelaçadas, cobrindo uma parede longa."),
       ("q91c", "Obra de Rubens Gerchman: composição pop com multidão de rostos dentro de um carro e placas com letras."),
       ("q91d", "Obra de Victor Vasarely: grade de quadrados em preto e branco que se deformam, criando ilusão de volume (op art)."),
       ("q91e", "Mosaico de pastilhas coloridas formando um rosto feminino de olhos grandes, em estilo clássico.")),
  ["arte afro-brasileira", "Rubem Valentim"], trocas=[("trataramna", "trataram-na"), ("O Brasil na visão do artista: o país e sua cultura", "<em>O Brasil na visão do artista: o país e sua cultura</em>")],
  enun=ap(T(91, 0)) + fonte(T(91, 1)) + p(T(91, 2)) + fonte("Obras: " + "; ".join(f"{k}) " + T(91, 2 + 2 * i).replace("em:http", "em: http") for i, k in enumerate("ABCDE", 1))),
  alts={k: f"[[fig:{i}]] {T(91, 2 + 2 * i).split('.')[0]}." for i, k in enumerate("ABCDE", 1)})
X(92, "Língua Portuguesa", "Variação linguística", "<p>A conversa começa formal (“O senhor é nosso cliente?”). Quando o cliente diz o nome e que é funcionário, a gerente reconhece um conhecido e passa a falar de modo informal (“Julinho, é você, cara?”, “Cê tá”, “pra gente”). Ela adequa a fala à conversa com um amigo. Alternativa <strong>A</strong>.</p><p>O que provoca a mudança é o reconhecimento, não o fato de ele ser funcionário (B) ou a origem dos dois (C).</p>",
  tags=["registro formal e informal", "adequação"], enun=ap(T(92, 0), T(92, 1), T(92, 2), T(92, 3), T(92, 4)) + fonte(T(92, 5).replace("Educação em língua materna", "<em>Educação em língua materna</em>")) + p(T(92, 6)))
X(93, "Língua Portuguesa", "Gêneros textuais", "<p>O perfil “b” (o fanático) recebe a recomendação: “Procure sair mais de casa e encontrar seus amigos pessoalmente”. O teste se preocupa com quem dedica mais tempo aos sites de relacionamento do que ao convívio pessoal. Alternativa <strong>D</strong>.</p><p>Usar os sites como complemento às amizades (C) é o perfil “a”, que não recebe nenhuma recomendação de mudança.</p>",
  figs(("q93", "Quadro de resultado de um teste. À esquerda, “Resultado”: campos para o total de respostas a, b e c; em caso de empate, a pergunta “Quando alguém, na vida real, pede os seus contatos, você: a) dá o número do telefone e o endereço de e-mail; b) dá a URL da sua rede social; c) O que é URL?”. À direita, “Avaliação”: mais respostas a, “O pragmático – você consegue usar as redes sociais on-line como um complemento às amizades e à vida profissional sem que isso afete sua intimidade”; mais respostas b, “O fanático – sua presença na internet está predominando sobre sua vida real. Procure sair mais de casa e encontrar seus amigos pessoalmente”; mais respostas c, “O aprendiz – você é um novato nos sites de relacionamentos ou ainda não descobriu como usá-los inteiramente”. Fonte: Rita Khater, psicóloga e professora da PUC-Campinas.")),
  ["leitura de teste", "redes sociais"], enun=p(T(93, 0)) + "[[fig:1]]" + fonte("<em>Veja</em>. 8 jul. 2009. p. 102 (adaptado).") + p(T(93, 2).split("(adaptado). ", 1)[1]))
X(94, "Artes", "Música", "<p>A figura 1 mostra um grupo com violões, cavaquinho e pandeiro, a formação típica do chorinho, gênero característico da música brasileira. Alternativa <strong>A</strong>.</p><p>A figura 2 é um conjunto de câmara (música erudita, que não é a de Tom Jobim); a 3 é um grupo de jazz, gênero americano; a 4 é uma banda de rock, com instrumentos elétricos e som alto.</p>",
  figs(("q94", "Quatro fotografias numeradas. Figura 1: grupo de homens vestidos de branco tocando violões, cavaquinho e pandeiro. Figura 2: conjunto de câmara com violinos, viola e violoncelo, músicos sentados com partituras. Figura 3: quarteto de jazz com saxofone, piano, contrabaixo e bateria. Figura 4: banda de rock no palco, com guitarras e bateria.")),
  ["gêneros musicais", "chorinho"], enun=p(T(94, 0)) + "[[fig:1]]" + fonte(T(94, 6).replace("figura 3 figura 4 ", "")) + p(T(94, 7)))
X(95, "Artes", "Dança e teatro", "<p>O texto descreve um balé com cenário e figurinos de Picasso, música que mistura jazz, sons de tiros, máquina de escrever, sirene e aviões, e uma coreografia feita de colagens de ações. Tudo isso reflete as inovações tecnológicas do começo do século XX transpostas para o cenário, a música, a coreografia e o figurino. Alternativa <strong>D</strong>.</p><p>O balé é de 1917, antes da Segunda Guerra (B), e a colagem é o oposto de uma narrativa linear (E).</p>",
  tags=["balé Parade", "vanguardas"],
  enun=ap(J(T(95, 0), T(95, 1)).replace("balé Parade", "balé <em>Parade</em>").replace("sur-realisme", "<em>sur-realisme</em>")) + fonte(T(95, 2).replace("O surrealismo. São", "<em>O surrealismo</em>. São")) + p(T(95, 3).replace("balé Parade", "balé <em>Parade</em>")),
  alts=CORTA(95))
X(96, "Língua Portuguesa", "Gêneros textuais", "<p>A campanha fala diretamente com o leitor: “Se você esteve...”, “cubra sua boca”, “Entre em contato”, “lave-as”. Os pronomes “você” e “sua” e os verbos no imperativo envolvem o leitor e pedem que ele aja. Alternativa <strong>C</strong>.</p><p>A enumeração (A) organiza as informações, mas não é o que cria a adesão; o telefone (E) não é um recurso linguístico.</p>",
  tags=["função apelativa", "imperativo"], enun=CAMP + p(T(96, 0)))
X(97, "Língua Portuguesa", "Gêneros textuais", "<p>O texto lista os sintomas que exigem contato com o Disque Epidemiologia e dá instruções para evitar a contaminação (cobrir a boca, lavar as mãos, usar máscara). Ele orienta a população sobre sintomas e procedimentos. Alternativa <strong>D</strong>.</p><p>Não fala em risco de morte (B) nem convoca todos a fazer exames (E).</p>",
  tags=["campanha de saúde", "gripe suína"], enun=CAMP + p(T(97, 0)))
X(98, "Literatura", "Linguagem poética", "<p>Em “lobo-bolo / Tipo pra rimar com ouro de tolo?”, o compositor brinca com o som das palavras (a inversão sonora lobo/bolo e a rima com “tolo”) e usa uma expressão coloquial, “tipo pra”. Os dois recursos aparecem juntos. Alternativa <strong>D</strong>.</p><p>“Brada a toda brida” (A) tem aliteração, mas vocabulário erudito; “tease me” (E) é estrangeirismo.</p>",
  figs(("q98", "Letra da canção “Para o Mano Caetano”, de Lobão, com os versos numerados de três em três (1 a 16) e trechos omitidos. O eu lírico se dirige a um “doce bardo” e critica, com ironia, rimas rebuscadas e uma imagem idealizada do Brasil tropical. A letra mistura palavras eruditas, gírias, trocadilhos sonoros e expressões em espanhol e em inglês; uma nota de rodapé traduz “tease me” como “caçoe de mim, importune-me”.")),
  ["recursos sonoros", "coloquialismo"],
  enun="[[fig:1]]" + fonte("LOBÃO. Disponível em: http://vagalume.uol.com.br. Acesso em: 14 ago. 2009 (adaptado).") + p(D[98]["paragrafos"][-1][1]))
X(99, "Literatura", "Simbolismo", "<p>O soneto tem forma rigorosa (rimas, métrica e vocabulário raro) e trata de temas universais e metafísicos: a alma presa, o Mistério, o etéreo, a Dor. Refinamento formal e tema metafísico são marcas do Simbolismo. Alternativa <strong>C</strong>.</p><p>A linguagem não é simples (A), não há tema social (D) e a forma é fixa (E).</p>",
  tags=["Cruz e Sousa", "soneto"],
  enun=tit("Cárcere das almas") + VERSOS(["Ah! Toda a alma num cárcere anda presa,", "Soluçando nas trevas, entre as grades", "Do calabouço olhando imensidades,", "Mares, estrelas, tardes, natureza."],
                                         ["Tudo se veste de uma igual grandeza", "Quando a alma entre grilhões as liberdades", "Sonha e, sonhando, as imortalidades", "Rasga no etéreo o Espaço da Pureza."],
                                         ["Ó almas presas, mudas e fechadas", "Nas prisões colossais e abandonadas,", "Da Dor no calabouço, atroz, funéreo!"],
                                         ["Nesses silêncios solitários, graves,", "que chaveiro do Céu possui as chaves", "para abrir-vos as portas do Mistério?!"])
       + fonte("CRUZ E SOUSA, J. <em>Poesia completa</em>. Florianópolis: Fundação Catarinense de Cultura / Fundação Banco do Brasil, 1993.")
       + p("Os elementos formais e temáticos relacionados ao contexto cultural do Simbolismo encontrados no poema <em>Cárcere das almas</em>, de Cruz e Sousa, são"),
  alts=CORTA(99))
X(100, "Língua Portuguesa", "Funções da linguagem", "<p>Na segunda fala, o escritor responde com exaltação que publica para “parar de escrevê-lo” e, no último quadro, desabafa sobre o cansaço de reescrever sem fim. O foco está no sentimento dele em relação ao processo de produção do livro (função emotiva). Alternativa <strong>E</strong>.</p><p>Ele não explica o sentido de “motivação” (B) nem descreve objetivamente as etapas (D).</p>",
  F_TIRA, ["função emotiva", "quadrinhos"], enun=TIRA + p(T(100, 0)))
X(101, "Língua Portuguesa", "Norma-padrão", "<p>O Inep anulou esta questão. Pela norma-padrão, mais de uma alternativa está correta: a ênclise em “escrevê-lo” (B) segue a regra, e o possessivo “sua” em “Qual foi sua maior motivação?” (C) concorda com o tratamento “o senhor”, que é de terceira pessoa. O uso de “esse” (A) para o livro do interlocutor também é aceito.</p><p>D e E estão erradas: o vocativo “Meu filho” aproxima, em vez de distanciar, e a repetição do “e” no último quadro é um recurso expressivo, não uma exigência da norma.</p>",
  F_TIRA, ["norma-padrão", "pronomes", "anulada"], enun=TIRA + p(T(101, 0)),
  anulacao={"fonte": "analise", "motivo": "O Inep anulou a questão no gabarito oficial sem divulgar o motivo. Pela análise, mais de uma alternativa obedece à norma-padrão: a ênclise em “escrevê-lo” (B) e o possessivo “sua” com o tratamento “o senhor” (C) estão corretos, e o demonstrativo “esse” (A) também é aceitável."})
X(102, "Artes", "Teatro", "<p>O texto diz que o texto dramático é completado pela atuação e fala em personagens, ação, ambiente e tema. Hoje o espetáculo teatral pode nascer de contos, lendas, poemas, notícias, imagens e outros gêneros, adaptados para a cena. Alternativa <strong>C</strong>.</p><p>O teatro é uma arte coletiva (A), em que cenário, luz e som dialogam com a peça (B, E) e o corpo do ator é essencial (D).</p>",
  tags=["gênero dramático", "espetáculo teatral"], trocas=[("drao", "<em>drao</em>"), ("Notas de teoria literária", "<em>Notas de teoria literária</em>")])
X(103, "Educação Física", "Saúde e qualidade de vida", "<p>O texto define aptidão física como a capacidade de usar o corpo de forma eficiente nas atividades cotidianas. Tem boa aptidão quem consegue fazer as atividades físicas do dia a dia, em qualquer idade. Alternativa <strong>C</strong>.</p><p>Fadiga de moderada a intensa (D) indica baixa aptidão, e conseguir se exercitar só por pouco tempo (B) também.</p>",
  tags=["aptidão física", "saúde"])
X(104, "Língua Portuguesa", "Gêneros digitais", "<p>No hipertexto, cada leitor escolhe seus caminhos, pode inserir informações e “dificilmente dois leitores farão os mesmos caminhos”. Assim, é o leitor que constrói a versão final do texto que lê, o que muda a noção tradicional de autoria. Alternativa <strong>A</strong>.</p><p>O texto diz o contrário de B, C e D: o leitor fica mais ativo e a fronteira entre autor e leitor se torna menos nítida.</p>",
  tags=["hipertexto", "autoria"], trocas=[("moveremse", "moverem-se"), ("leitornavegador", "leitor-navegador"), ("Cognição, linguagem e práticas interacionais", "<em>Cognição, linguagem e práticas interacionais</em>")])
X(105, "Língua Portuguesa", "Gêneros textuais", "<p>No segundo quadrinho, o personagem cumprimenta (“Fala, HTML! Como vão as coisas?”) e o outro responde com códigos, como numa conversa ao vivo, com saudação e réplica. A tirinha imita uma conversação face a face. Alternativa <strong>D</strong>.</p><p>A imagem é essencial para entender a piada (A), e a fala em código HTML não é clara para o leitor comum (B).</p>",
  figs(("q105", "Tira “La Vie en Rose” em três quadros. No primeiro, um personagem avisa: “Olha quem vem lá... o HTML!”. No segundo, outro o cumprimenta: “Fala, HTML! Como vão as coisas?”, e ele responde com uma sequência de códigos de HTML. No terceiro, o primeiro personagem também fala em códigos, misturando a pergunta “Numa boa, e vocês?”.")),
  ["quadrinhos", "oralidade"], enun=tit("La Vie en Rose") + "[[fig:1]]" + fonte("ITURRUSGARAI, A. La Vie en Rose. <em>Folha de S.Paulo</em>, 11 ago. 2007.") + p(T(105, -1) if False else D[105]["paragrafos"][-1][1]),
  alts={**D[105]["alternativas"], "B": ESC(D[105]["alternativas"]["B"])})
X(106, "Língua Portuguesa", "Tecnologias da informação", "<p>O texto diz que a informática e a internet geram novas formas de pensamento e aceleram as trocas entre sociedades e culturas. Essas tecnologias contribuem para o desenvolvimento social porque registram e espalham o conhecimento de forma mais democrática e interativa. Alternativa <strong>D</strong>.</p><p>A história sempre foi registrada sem elas (A), e o texto fala de influência nas trocas culturais, não só na tecnologia (B).</p>",
  tags=["explosão da informação", "globalização"], enun=ap(T(106, 0), T(106, 1).replace("pós- modernidade", "pós-modernidade")) + fonte(T(106, 2)) + p(T(106, 3)), alts=CORTA(106))
X(107, "Língua Portuguesa", "Argumentação", "<p>O texto II não faz previsões nem dá instruções: constata fatos (as sacolas entopem bueiros, causam enchentes, matam animais marinhos, têm custo ambiental) para convencer o leitor a evitá-las. Alternativa <strong>E</strong>.</p><p>Os animais mortos aparecem como fato informado, não como apelo emotivo central (B).</p>",
  tags=["estratégias argumentativas", "texto publicitário"], enun=PLAST + p(T(107, 0)))
X(108, "Língua Portuguesa", "Argumentação", "<p>O texto I destaca a versatilidade e as vantagens do plástico (atóxico, inerte, leve, reciclável), lamentando só que pouco se recicla. O texto II alerta para os danos ambientais das sacolas descartáveis. Alternativa <strong>B</strong>.</p><p>O texto I tem uma ressalva sobre a reciclagem, então não é “sem qualquer ressalva” (C).</p>",
  tags=["comparação de textos", "plástico"], enun=PLAST + p(T(108, 0)))
X(109, "Língua Portuguesa", "Variação linguística", "<p>No segundo quadrinho, a fala “Pensei que você tinha consertado” usa o mais-que-perfeito composto (“tinha consertado”), forma típica da fala do dia a dia, no lugar do mais-que-perfeito simples (“consertara”), mais formal. É o caráter coloquial do tempo verbal. Alternativa <strong>C</strong>.</p>",
  figs(("q109", "Tira de Hagar em dois quadros. No primeiro, Hagar pergunta a Eddie Sortudo: “Você consertou o vazamento do barco?”, e ele responde: “Não!”. No segundo, com o barco afundando e os vikings com água até o pescoço, Eddie diz: “Pensei que você tinha consertado!”.")),
  ["coloquialidade", "tempos verbais"], enun="[[fig:1]]" + fonte("BROWNE, C. Hagar, o horrível. <em>O Globo</em>, Segundo Caderno. 20 fev. 2009.") + p(T(109, 2)))
X(110, "Língua Portuguesa", "Tecnologias da informação", "<p>O portal oferece, de graça e a todos, obras literárias, artísticas e científicas em domínio público ou autorizadas. Isso é democratização da informação. Alternativa <strong>C</strong>.</p><p>O acesso é gratuito, não comercializado (D), e é aberto a toda a população, não só a acadêmicos (E).</p>",
  tags=["domínio público", "democratização da informação"])
X(111, "Língua Portuguesa", "Variação linguística", "<p>Cuitelinho é uma canção popular passada de geração em geração, que registra o falar do interior (“bera”, “espaia”, “bataia”) e um fato histórico (a Guerra do Paraguai). Preservá-la é preservar a formação da identidade nacional pela tradição oral. Alternativa <strong>C</strong>.</p><p>Essas formas são variantes, não “incorreções” (D).</p>",
  tags=["tradição oral", "identidade cultural"],
  enun=tit("Cuitelinho") + VERSOS(["Cheguei na bera do porto", "Onde as onda se espaia.", "As garça dá meia volta,", "Senta na bera da praia.", "E o cuitelinho não gosta", "Que o botão da rosa caia."],
                                  ["Quando eu vim da minha terra,", "Despedi da parentaia.", "Eu entrei em Mato Grosso,", "Dei em terras paraguaia.", "Lá tinha revolução,", "Enfrentei fortes bataia."],
                                  ["A tua saudade corta", "Como o aço de navaia.", "O coração fica aflito,", "Bate uma e outra faia.", "E os oio se enche d´água", "Que até a vista se atrapaia."])
       + fonte("Folclore recolhido por Paulo Vanzolini e Antônio Xandó. BORTONI-RICARDO, S. M. <em>Educação em língua materna</em>. São Paulo: Parábola, 2004.")
       + p(T(111, -2) if False else D[111]["paragrafos"][-2][1].replace("canção Cuitelinho", "canção <em>Cuitelinho</em>"), D[111]["paragrafos"][-1][1].replace("canção Cuitelinho", "canção <em>Cuitelinho</em>")))
X(112, "Artes", "Artes visuais", "<p>A pintura de Eckhout e a carta de Caminha retratam o indígena que vivia nas terras que seriam colonizadas: a carta descreve a aparência e a nudez dos nativos; a pintura mostra um índio tapuia com suas armas. Representar o habitante da terra é o ponto em comum. Alternativa <strong>C</strong>.</p><p>As obras são dos séculos XVI e XVII, bem antes do Romantismo (A).</p>",
  figs(("q112", "Pintura de Albert Eckhout, “Índio Tapuia”: homem indígena nu, de corpo inteiro, com cocar de penas, carregando lanças e uma clava, numa paisagem com vegetação tropical.")),
  ["Eckhout", "carta de Caminha"],
  enun="[[fig:1]]" + fonte(T(112, 1)) + ap(T(112, 2), T(112, 3)) + fonte("CAMINHA, P. V. <em>A carta</em>. Disponível em: www.dominiopublico.gov.br. Acesso em: 12 ago. 2009.") + p(T(112, 5)))
X(113, "Língua Portuguesa", "Tecnologias da informação", "<p>Divisão (ou exclusão) digital é a diferença entre quem tem e quem não tem acesso às novas tecnologias. Como elas estão em todos os meios produtivos, quem fica de fora tem mais dificuldade de adquirir conhecimentos e habilidades, o que aprofunda as diferenças sociais. Alternativa <strong>D</strong>.</p>",
  tags=["exclusão digital"], trocas=[("Digital Divide, Digital Gap ou Digital Exclusion", "<em>Digital Divide</em>, <em>Digital Gap</em> ou <em>Digital Exclusion</em>")],
  enun=ap(J(T(113, 0), T(113, 1), T(113, 2)).split(" Nesse contexto,")[0]) + p("Nesse contexto," + J(T(113, 0), T(113, 1), T(113, 2)).split(" Nesse contexto,")[1]))
X(114, "Língua Portuguesa", "Gêneros textuais", "<p>O texto pede que o leitor compre produtos com selos de certificação, que garantem que foram feitos segundo 10 princípios éticos (legislação ambiental, direitos dos povos indígenas). A mudança de comportamento é verificar essa certificação. Alternativa <strong>D</strong>.</p><p>Não se trata de consumir mais produtos da Amazônia (A) nem de selos de padronização industrial (C).</p>",
  figs(("q114", "Ilustração com frutas, garrafas e embalagens desenhadas em branco sobre fundo escuro, rodeadas por vários selos de certificação ambiental e de produtos orgânicos.")),
  ["consumo consciente", "certificação"], enun="[[fig:1]]" + ap(T(114, 1)) + fonte("<em>Vida simples</em>. Ed. 74, dez. 2008.") + p(T(114, 3)))
X(115, "Educação Física", "Dança", "<p>O texto mostra que as danças vêm “dos primeiros xavantes” e se mantêm até hoje, mas os cantos são renovados: o padrinho sonha com um canto novo e o ensina a todos. Há uma ligação entre os gestos ancestrais e a novidade dos cantos. Alternativa <strong>E</strong>.</p><p>A prática é coletiva e obrigatória, não iniciativa individual (A), e é planejada pelos padrinhos (D).</p>",
  tags=["dança indígena", "tradição"],
  enun=ap(J(T(115, 0), T(115, 1), T(115, 2)), T(115, 3)) + fonte(T(115, 4).replace("A dança e o canto-celebração da existência xavante", "<em>A dança e o canto-celebração da existência xavante</em>")) + p(T(115, 5).replace("conclui- se", "conclui-se")),
  alts=CORTA(115))
X(116, "Literatura", "Funções da linguagem", "<p>O poema chama a atenção para a própria construção: versos repetidos e paralelos, enumerações e o contraste entre o que o vento leva e o que enche a vida. Predomina a função poética. Alternativa <strong>E</strong>.</p><p>Não há relato de fatos reais (D), explicação de termos (B) nem apelo ao leitor (C).</p>",
  F_BAND, ["função poética", "Manuel Bandeira"], enun=BAND + p(T(116, 0)))
X(117, "Literatura", "Linguagem poética", "<p>O poema se estrutura pela repetição: “O vento varria...” abre vários versos, e o refrão sobre a vida que ficava cada vez mais cheia volta em cada estrofe. Há repetição de sons e de construções sintáticas semelhantes. Alternativa <strong>D</strong>.</p><p>Existe a oposição vento/vida cheia (A), mas o que estrutura o texto é o paralelismo.</p>",
  F_BAND, ["paralelismo", "repetição"], enun=BAND + p(T(117, 0)))
X(118, "Artes", "Teatro", "<p>Para Boal, a linguagem teatral não deve ser diferente da usada pelo cidadão comum, e todos podem fazer teatro; o espectador pode até substituir o protagonista. A linguagem é democratizada e dá ao cidadão autonomia crítica. Alternativa <strong>C</strong>.</p><p>O método rompe com a separação entre palco e plateia (B) e com o teatro tradicional e aristotélico (D, E).</p>",
  tags=["Teatro do Oprimido", "Augusto Boal"], trocas=[("Trata- se", "Trata-se")])
X(119, "Língua Portuguesa", "Variação linguística", "<p>O texto I chama a “língua brasileira” de confissão de ignorância e defende o padrão rígido; o texto II explica que a gramática usa construções do padrão atual brasileiro, como as de textos técnicos e jornalísticos. Um prega a rigidez; o outro, a adequação ao uso atual. Alternativa <strong>E</strong>.</p><p>O texto II não diz que o jornalismo deve criar regras próprias (D).</p>",
  tags=["norma-padrão", "português brasileiro"])
X(120, "Literatura", "Regionalismo", "<p>O romance regionalista do Nordeste (Graciliano Ramos, José Lins do Rego, Rachel de Queiroz) tem vocabulário realista, temas locais, mostra o homem diante da natureza dura do sertão e costuma adotar o ponto de vista dos mais pobres. Alternativa <strong>C</strong>.</p><p>O romance do Sul é muito rural (A), Alencar também escreveu romances regionalistas (B), e Simões Lopes Neto não é da geração de 30 (E).</p>",
  tags=["romance de 30", "regionalismo"], enun=ap(T(120, 0)) + fonte(T(120, 1).replace("A educação pela noite e outros ensaios", "<em>A educação pela noite e outros ensaios</em>")) + p(T(120, 2)), alts=CORTA(120))
X(121, "Língua Portuguesa", "Argumentação", "<p>Marcos Terena fala a “vocês” que têm “um pedaço de índio dentro”, que vieram de vários lugares e “querem ser brasileiros”, e diz: “nós não queremos tomar o Brasil de vocês”. O ouvinte é o brasileiro não índio. Alternativa <strong>B</strong>.</p>",
  tags=["interlocução", "identidade indígena"], enun=TERENA + p(T(121, 0)))
X(122, "Língua Portuguesa", "Variação linguística", "<p>Terena diz: “Quando eu falo com vocês, procuro usar o código de vocês”. Usar a norma-padrão do português é uma forma de se colocar em pé de igualdade com o interlocutor, numa posição simétrica, sem paternalismo nem privilégios. Alternativa <strong>B</strong>.</p>",
  tags=["norma-padrão", "interlocução"], enun=TERENA + p(T(122, 0)))
X(123, "Literatura", "Literatura e sociedade", "<p>A hipótese de tubarões “humanos” descreve uma sociedade em que os fortes educam os fracos para obedecer, se sacrificar e servir de alimento, com escolas, moral e condecorações. Brecht questiona a organização das sociedades capitalistas, baseada na exploração dos mais fracos pelos mais fortes. Alternativa <strong>D</strong>.</p><p>O texto é irônico: não retrata a opressão de modo positivo (A).</p>",
  tags=["Brecht", "crítica social"], trocas=[("Histórias do Sr. Keuner", "<em>Histórias do Sr. Keuner</em>")])
X(124, "Literatura", "Figuras de linguagem", "<p>O oxímoro junta ideias opostas que se reforçam. Em “E me deixa viver nessa que morre”, viver e morrer aparecem juntos, e “matança de quem só te deu vida” também opõe morte e vida. Alternativa <strong>D</strong>.</p><p>As outras trazem enumeração (B), metáfora (C) ou pares que não se excluem (A, E).</p>",
  tags=["oxímoro", "Hilda Hilst"], trocas=[("obra Cantares", "obra <em>Cantares</em>"), ("Dicionário Eletrônico Houaiss da Língua Portuguesa", "<em>Dicionário Eletrônico Houaiss da Língua Portuguesa</em>")])
X(125, "Língua Portuguesa", "Fala e escrita", "<p>O comentário à mão diz, em linguagem bem informal, que o filho que escrever como fala “tá ferrado”. Ele defende que, na escrita, é preciso usar vocabulário adequado e a norma-padrão. Alternativa <strong>D</strong>.</p><p>O comentário trata da escrita, não de melhorar a fala (A).</p>",
  figs(("q125", "Anúncio de uma revista de educação. No alto, escrito à mão: “Cara, se, tipo assim, o seu filho escrever como fala ele tá ferrado.” Abaixo, a capa da revista e as letras αβ.")),
  ["modalidade escrita", "norma-padrão"], enun="[[fig:1]]" + fonte("<em>Veja</em>, 7 maio 1997.") + p(T(125, 2)), alts=CORTA(125))
X(126, "Língua Portuguesa", "Gêneros textuais", "<p>A carta se dirige ao prefeito, mas o site com materiais para <em>download</em> e a mobilização de líderes comunitários mostram que o emissor quer alcançar públicos diferentes, usando vários meios para espalhar as informações. Alternativa <strong>D</strong>.</p><p>O <em>download</em> amplia o acesso, não o restringe (A, C).</p>",
  tags=["gêneros híbridos", "campanha oficial"], enun=DENGUE + p(T(126, 0).replace("termo download", "termo <em>download</em>")),
  alts={k: v.replace("termo download", "termo <em>download</em>").replace("para download", "para <em>download</em>") for k, v in D[126]["alternativas"].items()})
X(127, "Língua Portuguesa", "Argumentação", "<p>O título é “Sr. Prefeito, junte-se a nós” e o texto diz “a sua atuação como prefeito é fundamental”. A carta se dirige aos prefeitos, pedindo que organizem mutirões contra a dengue. Alternativa <strong>C</strong>.</p><p>Os líderes comunitários são parceiros que o prefeito deve envolver, não os destinatários (A).</p>",
  tags=["interlocutor", "campanha oficial"], enun=DENGUE + p(T(127, 0).replace("depreendese", "depreende-se")))
X(128, "Literatura", "Narrativa", "<p>A pergunta “Deveria fugir ou falar com ela?” e a reflexão seguinte mostram o narrador dividido entre partir em silêncio e se despedir da avó: é a hesitação, o sentimento contraditório. Alternativa <strong>E</strong>.</p><p>Os outros trechos descrevem ações ou o desejo de partir, sem dúvida (D).</p>",
  tags=["Osman Lins", "conflito interior"], enun=PARTIDA + fonte(T(128, 2).replace("A partida. Melhores contos", "A partida. <em>Melhores contos</em>")) + p(T(128, 3)))
X(129, "Língua Portuguesa", "Variação linguística", "<p>Serafim da Silva Neto defende que no Brasil as divisões dialetais geográficas não são marcadas; Teyssier diz que as diferenças são mais socioculturais que geográficas. Os dois concordam que as delimitações geográficas são pouco marcadas, embora enfatizem aspectos diferentes. Alternativa <strong>E</strong>.</p>",
  tags=["variação diatópica e diastrática"],
  enun=ap(J(T(129, 0), T(129, 1)).replace("isoglossas1", "isoglossas<sup>1</sup>").replace("História da Língua Portuguesa", "<em>História da Língua Portuguesa</em>"), T(129, 2)) + fonte(T(129, 3))
       + fonte("<sup>1</sup> isoglossa – linha imaginária que, em um mapa, une os pontos de ocorrência de traços e fenômenos linguísticos idênticos.") + fonte(T(129, 5)) + p(J(T(129, 6), T(129, 7))),
  alts=SEMHIF(D[129]["alternativas"]))
X(130, "Literatura", "Identidade cultural", "<p>A autora diz que o Brasil, “normalizado”, já não parece mítico “no bem e no mal” e se tornou um país polifônico, em que cada região desenvolve sua tradição. No início do século XXI há maior reconhecimento do Brasil por ele mesmo, com aspectos positivos e negativos. Alternativa <strong>C</strong>.</p><p>O texto diz que o eixo Rio-São Paulo já não é determinante (D).</p>",
  tags=["literatura brasileira", "identidade nacional"], trocas=[("História da literatura brasileira", "<em>História da literatura brasileira</em>")])
X(131, "Língua Portuguesa", "Variação linguística", "<p>João de Barros diz que os povos dominados “barbarizam” quando imitam o português, ou seja, vê a língua como algo fixo, que só os portugueses falariam corretamente. É uma concepção de língua homogênea e invariável, que nega que o português pertença também a outros povos. Alternativa <strong>D</strong>.</p>",
  tags=["preconceito linguístico", "João de Barros"],
  enun=p(T(131, 0).split(" Texto I ")[0]) + tit("Texto I") + ap(T(131, 0).split(" Texto I ")[1]) + fonte(T(131, 1)) + tit("Texto II") + ap(T(131, 2).replace("Texto II ", "", 1))
       + fonte(T(131, 3).replace("Gramática da língua portuguesa", "<em>Gramática da língua portuguesa</em>")) + p(T(131, 4)),
  alts=CORTA(131))
X(132, "Literatura", "Prosa contemporânea", "<p>O texto I é um fluxo verbal contínuo, em primeira pessoa, sem pausas, com tom agressivo (“me lixo com tudo isso!”), em que o narrador ataca valores como a família, a igreja e a humanidade. Há crítica à sociedade por meio de um discurso furioso. Alternativa <strong>D</strong>.</p><p>O narrador fala em primeira pessoa (A), e a linguagem não é simples nem objetiva (B, C).</p>",
  tags=["Raduan Nassar", "fluxo de consciência"], enun=NASSAR + p(T(132, 0).replace("novela Um Copo de Cólera", "novela <em>Um Copo de Cólera</em>")))
X(133, "Literatura", "Prosa contemporânea", "<p>O narrador desmonta, com ironia e agressividade, os valores que a parceira defende: diz que ela “paparica as ciências humanas” sem perceber que “paparica uma piada”. É um discurso desmistificador, ágil e contundente, contra princípios humanitários que ela supostamente defende. Alternativa <strong>C</strong>.</p><p>Ele recusa as instituições, não as defende (A), e não apela ao engajamento (D).</p>",
  tags=["Raduan Nassar", "ditadura militar"], enun=NASSAR + p(T(133, 0).replace("obra Um Copo de Cólera", "obra <em>Um Copo de Cólera</em>")))
X(134, "Educação Física", "Corpo e sociedade", "<p>O texto compara o culto ao corpo a uma religião. A ideia é que a corpolatria é uma religião “pelo avesso”: antes a felicidade eterna exigia renunciar ao prazer; agora a busca da felicidade passa pelo culto ao prazer e ao corpo. Alternativa <strong>A</strong>.</p><p>O fenômeno é recente (E) e aparece também nos países ricos (C).</p>",
  tags=["culto ao corpo", "corpolatria"], trocas=[("O que é corpo(latria)", "<em>O que é corpo(latria)</em>")])
X(135, "Literatura", "Modernismo", "<p>O poema liga o “eu” à cidade natal: o ferro de Itabira explica a tristeza, o orgulho e a dureza do poeta, e a lembrança da terra dói. Há tensão entre o indivíduo e sua comunidade, com imagens que mostram como o lugar e a sociedade ajudam a formar o sujeito. Alternativa <strong>C</strong>.</p><p>O poema não é da fase heroica de 1922 (A), não é objetivo (B) nem pomposo (E).</p>",
  figs(("q135", "Poema “Confidência do Itabirano”, de Carlos Drummond de Andrade, em versos livres. O eu lírico conta que viveu e nasceu em Itabira, cidade de mineração de ferro, e atribui a ela traços do seu jeito de ser, como a tristeza, o orgulho, a dureza e o hábito de sofrer. Lista objetos trazidos de lá que oferece ao leitor, lembra que teve riquezas e hoje é funcionário público, e termina dizendo que Itabira é só uma fotografia na parede, mas que a lembrança dói.")),
  ["Drummond", "eu e mundo"], enun="[[fig:1]]" + fonte("ANDRADE, C. D. <em>Poesia completa</em>. Rio de Janeiro: Nova Aguilar, 2003.") + p(T(135, 4).replace("poema Confidência do Itabirano", "poema <em>Confidência do Itabirano</em>")))

completar(Q, R)
