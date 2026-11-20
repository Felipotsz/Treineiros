# Enem 2009, 1º dia (05/12/2009), caderno azul: Ciências Humanas (questões 46 a 90; no site, 1 a 45). Em 2009 as Humanas fechavam o 1º dia.
# Texto legível. Rankings de petróleo e gás da Q83 em HTML. Alternativas-imagem (fotos com legenda) na Q85. Trova popular da Q65 (c. 1820) em texto, domínio público.
# Sem anuladas nesta área.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, paragrafos_enem

ID = "enem-2009-humanas"
META = {"id": ID, "banca": "Enem", "ano": 2009, "titulo": "Enem 2009: Ciências Humanas", "fonte": "Inep", "dataExame": "2009-12-05",
        "duracaoMinutos": 135, "area": "Ciências Humanas", "caderno": "azul", "dia": 1}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2009-dia1-azul")
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
    Q[n - 45] = {"materia": materia, "assunto": assunto, "area": "Ciências Humanas", "tags": list(tags), "numeroOriginal": n,
                 "enunciado": e, "alternativas": {k: (QF if quim else str)(LIMPA(v)) for k, v in dict(alts or D[n]["alternativas"]).items()},
                 "imagens": list(imagens), "explicacao": expl}
    if anulacao: Q[n - 45]["anulacao"] = anulacao


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

X(46, "História", "Antiguidade", "<p>O texto contrapõe o olhar de hoje (atração turística) ao sentido que os monumentos tinham na época. Para o gabarito, pirâmides, tumbas e templos expressavam o poder dos faraós de mobilizar à força enormes contingentes de trabalhadores. Alternativa <strong>A</strong>.</p><p>Pesquisas mais recentes mostram que boa parte dos construtores das pirâmides eram trabalhadores recrutados e alimentados pelo Estado, e não escravos no sentido estrito; a ideia central da questão é a do poder faraônico sobre a população.</p>",
  tags=["Egito Antigo", "poder faraônico"])
X(47, "História", "Idade Moderna", "<p>O texto de Norbert Elias trata da Corte dos reis de França no Antigo Regime. A principal casa de habitação desses reis, e centro do poder absolutista de Luís XIV, foi o palácio de Versalhes, hoje patrimônio artístico e cultural. Alternativa <strong>A</strong>.</p><p>O Museu Britânico nunca foi residência real, e a Casa Branca abriga presidentes, não reis.</p>",
  tags=["absolutismo", "sociedade de corte"],
  enun=ap(J(T(47, 0), T(47, 1))) + fonte(T(47, 2).replace("A sociedade de corte", "<em>A sociedade de corte</em>")) + p(T(47, 3)))
X(48, "História", "Brasil Colônia", "<p>No Brasil colonial, os mortos eram enterrados dentro das igrejas, e o lugar dependia da posição social: os mais importantes ficavam perto do altar; os pobres e escravos, nos adros ou em covas comuns. O sepultamento reproduzia a hierarquia social. Alternativa <strong>C</strong>.</p><p>Na Idade Média a Igreja controlava os ritos fúnebres (B), e os gregos valorizavam muito os funerais (A).</p>",
  tags=["sepultamentos", "hierarquia social"])
X(49, "História", "Idade Média", "<p>O texto diz que cada época reinterpreta a Idade Média segundo os próprios interesses. Hitler fez isso ao apresentar o III Reich como herdeiro do Sacro Império Romano-Germânico (o “Primeiro Reich”), usando o passado medieval para legitimar o nazismo. Alternativa <strong>A</strong>.</p>",
  tags=["memória histórica", "usos do passado"])
X(50, "História", "Século XX", "<p>As duas guerras mundiais e as revoluções da primeira metade do século XX tiveram entre suas causas a crise do colonialismo (disputas imperialistas por colônias), o nacionalismo exaltado e a ascensão dos regimes totalitários. Alternativa <strong>A</strong>.</p><p>Corrida nuclear, Revolução Cubana e terceiro-mundismo são da Guerra Fria, depois de 1945 (B, C, D); a unificação alemã é de 1871 (E).</p>",
  tags=["Primeira e Segunda Guerras", "totalitarismo"])
X(51, "História", "Totalitarismo", "<p>As juventudes nazista e fascista eram organizações fechadas, que exigiam obediência cega ao líder e partiam para a violência contra os opositores do regime. Sectarismo e radicalismo violento eram sua marca. Alternativa <strong>A</strong>.</p><p>Esses regimes não promoviam direitos de cidadania (B) nem diálogo (D).</p>",
  tags=["nazismo e fascismo", "juventude"], enun=ap(J(T(51, 0), T(51, 1))) + p(T(51, 2)))
X(52, "História", "Guerra Fria", "<p>A divisão política, econômica e militar da Europa entre o bloco capitalista e o socialista ficou conhecida pela expressão de Churchill, a “Cortina de Ferro”. Alternativa <strong>A</strong>.</p><p>O Muro de Berlim (B) dividiu apenas uma cidade e foi um símbolo dessa divisão maior.</p>",
  tags=["bipolaridade", "OTAN e Pacto de Varsóvia"])
X(53, "História", "Século XX", "<p>Os movimentos de 1968 (estudantes em Paris, protestos contra a Guerra do Vietnã, contracultura) questionaram costumes e autoridades e abriram caminho para o pacifismo, o ambientalismo, o feminismo e a luta pelos direitos das minorias. Alternativa <strong>E</strong>.</p><p>O próprio texto citado mostra a conotação política (A), e houve 1968 também em países pobres, como as passeatas no Brasil e o massacre de Tlatelolco no México (B).</p>",
  tags=["1968", "movimentos sociais"])
X(54, "Sociologia", "Cultura indígena", "<p>Para os Yanomami, a floresta tem um sopro vital (<em>wixia</em>) que a mantém viva: graças a ele as plantas crescem, ela não se decompõe e não morre se não for desmatada. Wixia é essa capacidade de a floresta se sustentar por processos vitais. Alternativa <strong>E</strong>.</p><p>O texto não fala em decompositores (A) e diz que urihi não é objeto de exploração econômica (B).</p>",
  tags=["Yanomami", "cosmologia indígena"], trocas=[("urihi", "<em>urihi</em>"), ("wixia", "<em>wixia</em>"), ("Almanaque Brasil Socioambiental", "<em>Almanaque Brasil Socioambiental</em>")],
  alts={**D[54]["alternativas"], "C": D[54]["alternativas"]["C"].replace("urihi", "<em>urihi</em>"), "E": D[54]["alternativas"]["E"].replace("Wixia", "<em>Wixia</em>")})
X(55, "Geografia", "Geopolítica", "<p>Com o fim da Guerra Fria, a expectativa de paz não se cumpriu: multiplicaram-se os conflitos internos, étnicos e nacionalistas (ex-Iugoslávia, Ruanda), o extremismo religioso e ameaças como o terrorismo, o tráfico e o crime organizado. Alternativa <strong>A</strong>.</p><p>Os EUA agiram sem aval da ONU, como no Iraque em 2003 (E).</p>",
  tags=["pós-Guerra Fria", "conflitos contemporâneos"])
X(56, "Sociologia", "Cidadania", "<p>O texto diz que, nos EUA, o cidadão se sente incluído pelos direitos políticos e pelo direito de propriedade, mesmo que pequena. A democracia está ligada às possibilidades econômicas de cada indivíduo. Alternativa <strong>D</strong>.</p><p>O texto não fala em obrigar todos a terem propriedade (E) nem em hierarquia pela posse (B).</p>",
  tags=["democracia liberal", "propriedade"])
X(57, "Filosofia", "Ética e política", "<p>Tocqueville diz que a falta de moral é condenada porque atrapalha o bem-estar e a harmonia doméstica, “tão essencial ao sucesso dos negócios”. Ou seja, os norte-americanos ligavam a conduta moral ao progresso econômico. Alternativa <strong>D</strong>.</p><p>Não há promessa de enriquecimento rápido (B), e a castidade ajudaria a harmonia doméstica, não a perturbaria (E).</p>",
  tags=["Tocqueville", "moral e economia"],
  enun=ap(J(T(57, 0), T(57, 1), T(57, 2))) + fonte(T(57, 3).replace("Democracy in America", "<em>Democracy in America</em>")) + p(T(57, 4).replace("norte- americanos", "norte-americanos")))
X(58, "Filosofia", "Filosofia antiga", "<p>Para Aristóteles, quem trabalha (comerciantes, agricultores) não deve ser cidadão, porque a cidadania exige lazer para desenvolver as virtudes e fazer política. A cidadania era vista como dignidade dos grupos superiores, numa sociedade hierarquizada. Alternativa <strong>B</strong>.</p><p>Na Grécia, mulheres, estrangeiros e escravos não eram cidadãos, então não “todos os habitantes” participavam (C).</p>",
  tags=["Aristóteles", "cidadania grega"], trocas=[("obra Política", "obra <em>Política</em>")])
X(59, "Sociologia", "Pensamento social brasileiro", "<p>Para os três autores, a formação do Brasil se completaria no futuro, quando certos problemas fossem superados; e esse futuro parece cada vez mais distante. A frase que resume isso é “Brasil, a eterna esperança”. Alternativa <strong>B</strong>.</p><p>“Gigante pela própria natureza” (E) é verso do Hino Nacional e fala de grandeza, não de expectativa adiada.</p>",
  tags=["formação do Brasil", "intérpretes do Brasil"], trocas=[("Sequências brasileiras", "<em>Sequências brasileiras</em>")])
X(60, "História", "República Velha", "<p>A Constituição de 1934 precisou dizer “de um e de outro sexo” porque a de 1891, ao falar só em “cidadãos”, era entendida como excluindo as mulheres. Na prática, só homens votavam até o Código Eleitoral de 1932. Alternativa <strong>E</strong>.</p><p>A redução da idade (A) é verdade, mas a pergunta trata do gênero.</p>",
  tags=["voto feminino", "Constituições brasileiras"], enun=p(T(60, 0)) + ap(T(60, 1)) + p(T(60, 2)) + ap(T(60, 3)) + p(T(60, 4)))
X(61, "História", "Era Vargas", "<p>Francisco Campos desqualifica eleitores, partidos e Judiciário e diz que só o Executivo, centralizado em Vargas, daria racionalidade ao Estado, porque Vargas teria intuição do bem e da verdade e seria um gênio político. Ou seja, Vargas exerceria o poder de modo inteligente e correto. Alternativa <strong>E</strong>.</p><p>Para ele os eleitores são apáticos, não mal-intencionados (A), e não há promessa de democracia futura (C, D).</p>",
  tags=["Estado Novo", "autoritarismo"], trocas=[("livro, O Estado Nacional,", "livro, <em>O Estado Nacional</em>,"), ("O Estado nacional", "<em>O Estado nacional</em>")], alts=SEMHIF(D[61]["alternativas"]))
X(62, "História", "Era Vargas", "<p>O programa de rádio apresentava as leis trabalhistas como presentes do governo aos trabalhadores. Isso reforçava a imagem de Vargas como protetor das massas, base do trabalhismo e do populismo. Alternativa <strong>D</strong>.</p><p>O governo não queria estimular greves (C) nem lembrar as lutas sindicais anteriores (A).</p>",
  tags=["Estado Novo", "propaganda", "trabalhismo"], trocas=[("A invenção do trabalhismo", "<em>A invenção do trabalhismo</em>")])
X(63, "História", "Brasil Colônia", "<p>Para a Inquisição, o casamento era sacramento e só a Igreja podia orientar a vida conjugal. Recorrer a poções e “coisas diabólicas” para ter um bom casamento era heresia. Os cristãos deviam preservar o casamento só com os ensinamentos da Igreja. Alternativa <strong>E</strong>.</p><p>“Feminismo” (D) é um conceito anacrônico para o século XVI.</p>",
  tags=["Inquisição", "religiosidade colonial"], trocas=[("O teatro dos vícios", "<em>O teatro dos vícios</em>")])
X(64, "História", "Colonização", "<p>O texto compara a formação dos Estados na América Latina, na África e na Ásia, mas em todas elas o elemento decisivo é a relação com o colonizador europeu: instituições transplantadas, fronteiras traçadas por europeus ou superpostas às locais. A maior distinção é entre colonizador e colonizados. Alternativa <strong>B</strong>.</p><p>O texto diz que no Brasil as instituições locais eram frágeis, não eliminadas (D), e que a Ásia conservou formas anteriores, diferente do Brasil (E).</p>",
  tags=["formação dos Estados", "colonialismo"],
  enun=ap(J(T(64, 0), T(64, 1))) + fonte(T(64, 2).replace("jan.- abr.", "jan.-abr.").replace("Estudos Avançados", "<em>Estudos Avançados</em>")) + p(T(64, 3)), alts=SEMHIF(D[64]["alternativas"]))
X(65, "História", "Independência do Brasil", "<p>A trova circulava entre as classes populares do Recife e falava em acabar com marinheiros (portugueses) e caiados (brancos), para que só pardos e pretos habitassem o país. Os rumores da revolta do Haiti alimentavam, entre escravos e mestiços pobres, o desejo de mudança. Alternativa <strong>A</strong>.</p><p>A Noite das Garrafadas (B) é de 1831, depois da independência.</p>",
  tags=["Haiti", "conflitos raciais"],
  enun=p(T(65, 0)) + '<p class="apoio">Marinheiros e caiados<br>Todos devem se acabar,<br>Porque só pardos e pretos<br>O país hão de habitar.</p>' + fonte(T(65, 3).replace("Estudos pernambucanos", "<em>Estudos pernambucanos</em>")) + p(T(65, 4)))
X(66, "História", "Política externa", "<p>O texto descreve uma política externa com “inteligência de longo prazo”, teoria própria, busca de autonomia decisória e pragmatismo mantido em diferentes regimes. Isso indica que o Brasil tem capacidade decisória própria, mesmo diante dos constrangimentos internacionais. Alternativa <strong>E</strong>.</p><p>O texto fala em debates entre as elites, não em consultas à população (D).</p>",
  tags=["política externa brasileira", "autonomia"], trocas=[("Correio Braziliense", "<em>Correio Braziliense</em>")])
X(67, "História", "Revolução Industrial", "<p>Thompson conta que pequenos fazendeiros-tecelões abandonaram suas propriedades para só tecer. Antes da mecanização, portanto, os artesãos combinavam a tecelagem com a agricultura de subsistência; a mudança tecnológica acabou com esse arranjo e os deixou dependentes. Alternativa <strong>D</strong>.</p><p>O texto fala de teares manuais competindo com os mecânicos, não de treinamento especializado (C).</p>",
  tags=["Revolução Industrial", "trabalho artesanal"], trocas=[("The making of the english working class", "<em>The making of the english working class</em>")])
X(68, "Geografia", "Agropecuária", "<p>A modernização agrícola depois da Revolução Industrial aumentou a produção, mas também o uso de máquinas, combustíveis, fertilizantes e água, isto é, a demanda por recursos naturais, inclusive energéticos. Alternativa <strong>C</strong>.</p><p>A fome não foi erradicada (A), as cidades cresceram (B) e a mecanização reduziu o emprego no campo (E).</p>",
  tags=["modernização agrícola", "recursos naturais"])
X(69, "História", "Literatura e sociedade", "<p>A casa dos Meneses ainda guarda móveis, cristais, pratas e marfins de um passado ilustre, mas agora em desordem, empoeirados e corroídos por “um mal oculto”. É um espaço em ruína onde a vida é lembrança de um passado prestes a desaparecer. Alternativa <strong>E</strong>.</p><p>O texto fala em conforto (A) e desordem, não em asseio (D).</p>",
  tags=["decadência da aristocracia rural", "Lúcio Cardoso"],
  enun=ap(T(69, 0).replace("semi- empoeiradas", "semi-empoeiradas")) + fonte(T(69, 1).replace("Crônica da casa assassinada", "<em>Crônica da casa assassinada</em>")) + p(J(T(69, 2), T(69, 3))))
X(70, "História", "Brasil Império", "<p>Antes das ferrovias, a viagem de Santos ao interior levava mais de dois dias por estradas precárias. Com os trilhos, o café pôde avançar para áreas cada vez mais distantes do porto, e os fazendeiros puderam levar imigrantes europeus até lá. Alternativa <strong>B</strong>.</p><p>Os colonos chegavam pobres; não traziam capital (C) nem compravam grandes propriedades (E).</p>",
  tags=["café", "imigração", "ferrovias"], trocas=[("Memórias de um colono no Brasil", "<em>Memórias de um colono no Brasil</em>")])
X(71, "Geografia", "Urbanização", "<p>Cidades globais (Nova York, Londres, Tóquio, São Paulo) concentram sedes de empresas, finanças e serviços que comandam a economia mundial. Elas surgem com a internacionalização da economia a partir do fim dos anos 1970. Alternativa <strong>D</strong>.</p><p>Elas têm níveis de influência diferentes (A) e costumam acentuar a desigualdade e a segregação (C).</p>",
  tags=["cidades globais", "globalização"])
X(72, "Sociologia", "Globalização", "<p>O texto diz que a tecnologia digital põe culturas diferentes em contato, o que pode gerar apreço ou ressentimento, e defende uma “alfabetização eletrônica” como novo modelo de educação. É a ideia de que é preciso reformular as concepções tradicionais de educação. Alternativa <strong>A</strong>.</p><p>O texto quer somar a cultura tradicional à eletrônica, não declará-la obsoleta (C).</p>",
  tags=["tecnologias de informação", "educação"])
X(73, "Geografia", "Economia brasileira", "<p>O mapa mostra PIB por habitante acima da média também em estados do Centro-Oeste e do Norte, como Mato Grosso. Isso reflete o avanço da fronteira econômica (agronegócio, mineração, indústria e serviços) sobre essas regiões nas últimas décadas. Alternativa <strong>D</strong>.</p><p>As desigualdades regionais continuam visíveis no mapa (A), e o Sudeste segue com o maior PIB industrial (C).</p>",
  figs(("q73", "Mapa do Brasil com o PIB por habitante em 2004, por estado, em cinco faixas: 4 000, 6 000, 9 730 (a média), 13 000 e acima. Os tons mais escuros (maiores valores) aparecem no Distrito Federal, em São Paulo, no Rio de Janeiro, nos estados do Sul e em Mato Grosso; os mais claros, na maior parte do Nordeste e em parte do Norte.")),
  ["PIB por habitante", "desconcentração econômica"], enun="[[fig:1]]" + fonte(T(73, 1).replace("Géographie. L’espace mondial", "<em>Géographie. L’espace mondial</em>")) + p(T(73, 2)))
X(74, "História", "Antiguidade", "<p>As cidades-Estado gregas eram independentes umas das outras, e o texto descreve quinze cidades no Xingu, cada uma cercada por muros e com sua própria população, ligadas por estradas. Nas duas civilizações havia cidades autônomas. Alternativa <strong>C</strong>.</p><p>O texto não fala em democracia nem em língua comum no Xingu (B, D), e as epidemias só são citadas para o Xingu (A).</p>",
  tags=["cidades-Estado", "povos indígenas"], trocas=[("Folha de S. Paulo", "<em>Folha de S. Paulo</em>")])
X(75, "Geografia", "Migrações", "<p>Os migrantes que chegam ao Sudeste ocupam, em sua maioria, trabalhos manuais não qualificados e têm nível de vida abaixo do da população local. A chegada contínua de pessoas sem infraestrutura e emprego suficientes alimenta o inchaço urbano, com favelas e subemprego. Alternativa <strong>C</strong>.</p>",
  tags=["migração Nordeste–Sudeste", "inchaço urbano"])
X(76, "Geografia", "Questão agrária", "<p>Mesmo com o aumento da produção, persiste a concentração de terras em latifúndios improdutivos, o que limita o acesso à terra de quem produziria alimentos e alimenta os conflitos. A estrutura agrária arcaica explica parte da subalimentação. Alternativa <strong>C</strong>.</p><p>A agricultura sul-americana é muito exportadora (A), e há mão de obra sobrando no campo (B).</p>",
  tags=["latifúndio", "fome"])
X(77, "Geografia", "Questão agrária", "<p>No mapa, os maiores círculos (mais assassinatos) se concentram no sudeste do Pará, norte do Tocantins e oeste do Maranhão, região conhecida como Bico do Papagaio. Alternativa <strong>B</strong>.</p>",
  figs(("q77", "Mapa “Brasil – Vítimas fatais de conflitos ocorridos no campo 1985-1996”, com círculos proporcionais ao número de assassinatos (de 1 a 83). A maior concentração de círculos grandes fica no sudeste do Pará, no norte do Tocantins e no oeste do Maranhão; há círculos menores espalhados pelo resto do país.")),
  ["conflitos agrários", "violência no campo"],
  enun=ap(T(77, 0)) + "[[fig:1]]" + fonte(T(77, 2).replace("Revista Estudos Avançados", "<em>Revista Estudos Avançados</em>")) + p(T(77, 3)))
X(78, "Geografia", "Questão agrária", "<p>No Brasil, 63,8% da área ocupada é de imóveis improdutivos, mais que os produtivos (28,7%) e os minifúndios (7,5%) somados. O mesmo ocorre no Norte, no Nordeste, no Sudeste e no Centro-Oeste; só no Sul os produtivos lideram. Alternativa <strong>A</strong>.</p><p>Improdutivo não significa solo infértil (B): é terra que não cumpre a função produtiva.</p>",
  figs(("q78", "Gráfico de barras com tabela da área ocupada pelos imóveis rurais em 2006 (%), em minifúndio, imóveis improdutivos e imóveis produtivos: Brasil 7,5; 63,8; 28,7. Norte 5,3; 82,6; 12,1. Nordeste 14,3; 69,7; 16,0. Sudeste 9,0; 48,4; 42,6. Sul 14,5; 38,3; 47,2. Centro-Oeste 2,0; 63,5; 34,5.")),
  ["estrutura fundiária", "leitura de gráfico"], enun=p(T(78, 0)) + tit(T(78, 1)) + "[[fig:1]]" + fonte(T(78, 3)) + p(T(78, 4)))
X(79, "Sociologia", "Direitos humanos", "<p>O texto diz que ONGs e a Pastoral da Terra acionam as autoridades públicas (denúncias) e dão aulas sobre direitos sociais e trabalhistas aos trabalhadores. Alternativa <strong>D</strong>.</p><p>Eles não substituem a polícia e a Justiça (C); acionam essas instituições.</p>",
  tags=["trabalho escravo", "movimentos sociais"])
X(80, "Geografia", "Meio ambiente", "<p>A tecnologia permitiu explorar recursos em escala cada vez maior, como o petróleo extraído e transportado por grandes navios. Um efeito disso são desastres ambientais de grandes proporções, como os derramamentos de óleo. Alternativa <strong>B</strong>.</p><p>As desigualdades não foram eliminadas (C), e o crescimento vegetativo é maior nos países pobres (E).</p>",
  tags=["exploração de recursos", "desastres ambientais"])
X(81, "Geografia", "Meio ambiente", "<p>A definição clássica de desenvolvimento sustentável (Relatório Brundtland, 1987) é atender às necessidades do presente sem comprometer a capacidade das gerações futuras de atenderem às suas, nas dimensões econômica, social e ambiental. Alternativa <strong>E</strong>.</p><p>A proteção da biodiversidade (D) é uma parte disso, não a definição.</p>",
  tags=["desenvolvimento sustentável"])
X(82, "Geografia", "Geopolítica", "<p>O Ártico atrai as potências também por ser uma região sem guerras e instabilidade política, ao contrário do Oriente Médio, de onde vem grande parte do petróleo mundial. Alternativa <strong>A</strong>.</p><p>A matriz energética mundial é dominada por fontes fósseis, não renováveis (E), e quem disputa o Ártico são as potências, não os países em desenvolvimento (C).</p>",
  tags=["Ártico", "recursos energéticos"], trocas=[("Le monde diplomatique Brasil", "<em>Le Monde Diplomatique Brasil</em>")])
_GAS = [["Rússia", "47.570.000.000.000"], ["Irã", "26.370.000.000.000"], ["Catar", "25.790.000.000.000"], ["Arábia Saudita", "6.568.000.000.000"], ["Emirados Árabes Unidos", "5.823.000.000.000"],
        ["Estados Unidos", "5.551.000.000.000"], ["Nigéria", "5.015.000.000.000"], ["Argélia", "4.359.000.000.000"], ["Venezuela", "4.112.000.000.000"], ["Iraque", "3.170.000.000.000"]]
_PET = [["Arábia Saudita", "266.800.000.000"], ["Canadá", "178.800.000.000"], ["Irã", "132.500.000.000"], ["Iraque", "115.000.000.000"], ["Kuwait", "104.000.000.000"],
        ["Emirados Árabes Unidos", "97.800.000.000"], ["Venezuela", "79.730.000.000"], ["Rússia", "60.000.000.000"], ["Líbia", "39.130.000.000"], ["Nigéria", "35.880.000.000"]]
X(83, "Geografia", "Recursos energéticos", "<p>A Venezuela aparece entre os dez maiores em reservas de gás natural (9º) e de petróleo (7º). Ter reservas tão grandes das duas fontes faz dela uma grande potência energética mundial. Alternativa <strong>E</strong>.</p><p>Em 2009 a Venezuela ainda não era membro pleno do MERCOSUL (A), e suas reservas já eram exploradas (B).</p>",
  tags=["petróleo e gás natural", "Venezuela"],
  enun=p(T(83, 0)) + tit("Gás natural – reservas provadas (metros cúbicos)") + tabela(["Posição", "País", "Reservas (m<sup>3</sup>)"], [[str(i), a, b] for i, (a, b) in enumerate(_GAS, 1)])
       + tit("Petróleo – reservas provadas (barris)") + tabela(["Posição", "País", "Reservas (barris)"], [[str(i), a, b] for i, (a, b) in enumerate(_PET, 1)])
       + fonte("Disponível em: http://indexmundi.com. Acesso em: 12 ago. 2009 (adaptado).") + p(T(83, 3)))
X(84, "História", "Brasil Colônia", "<p>No mapa, o território português com base no Tratado de Madri (1750) vai muito além da linha de Tordesilhas, para o oeste. O tratado reconheceu a expansão portuguesa pelo princípio do <em>uti possidetis</em> (a terra é de quem a ocupa). Alternativa <strong>C</strong>.</p><p>A foz do Amazonas ficava do lado espanhol de Tordesilhas (A), e Tordesilhas era uma linha imaginária, não um rio (B).</p>",
  figs(("q84", "Mapa da América do Sul com a fronteira do Tratado de Tordesilhas (1494), uma linha norte-sul que passa perto de Belém e de Laguna; o território português conforme Tordesilhas, a leste dessa linha; o território português com base no Tratado de Madri (1750), que se estende muito mais para o oeste; e a fronteira do Tratado de Santo Ildefonso (1777). Um detalhe ampliado mostra o sul, entre os rios Paraná e Uruguai.")),
  ["Tratado de Tordesilhas", "Tratado de Madri"],
  enun="[[fig:1]]" + fonte("BETHEL, L. <em>História da América</em>. V. I. São Paulo: Edusp, 1997.") + p(J(T(84, 2), T(84, 3))))
X(85, "Geografia", "Clima", "<p>A Arábia Saudita tem clima desértico, com chuva escassa. A irrigação por aspersão em pivôs centrais é uma tecnologia que contorna essa restrição climática e permite produzir no deserto. Alternativa <strong>D</strong>.</p><p>O parque eólico (E) usa o clima para gerar energia, mas não supera uma restrição para produzir; a agricultura andina (B) é tradicional.</p>",
  figs(("q85a", "Fotografia de uma plantação de videiras em fileiras, com duas pessoas caminhando entre elas."),
       ("q85b", "Fotografia de camponeses andinos trabalhando a terra com ferramentas manuais numa pequena roça, com montanhas ao fundo."),
       ("q85c", "Fotografia aérea de grandes currais com bois confinados para engorda."),
       ("q85d", "Fotografia aérea de grandes círculos verdes de plantação irrigada por pivô central em meio à areia do deserto."),
       ("q85e", "Fotografia de muitas turbinas eólicas enfileiradas em colinas secas.")),
  ["clima e produção", "irrigação"], enun=p(T(85, 0)), alts={k: f"[[fig:{i}]] {D[85]['alternativas'][k]}" for i, k in enumerate("ABCDE", 1)})
X(86, "Geografia", "Meio ambiente", "<p>A primeira charge mostra pinguins no Polo Sul em 2100 cercados de cactos e ossos, como num sertão: o aquecimento chegou aos polos. A segunda mostra uma floresta derrubada e queimada. Juntas, indicam que a destruição das florestas tropicais contribui para o aumento da temperatura até em lugares distantes, como os polos. Alternativa <strong>D</strong>.</p>",
  figs(("q86a", "Charge “Polo Sul 2100”: dois pinguins suados, num chão seco com cacto, sol forte e ossos, e um deles exclama “Óxente!”."),
       ("q86b", "Charge de uma floresta derrubada e em chamas, com tocos de árvores; um menino indígena diz ao pai: “Pai?!! Agora que consegui crescer entendo porque precisamos de cesta básica para sobreviver”.")),
  ["aquecimento global", "desmatamento"], enun="[[fig:1]]" + fonte(T(86, 1)) + "[[fig:2]]" + fonte(T(86, 4).replace("images/ charge", "images/charge")) + p(T(86, 5)))
X(87, "Geografia", "Clima", "<p>O semiárido do Nordeste brasileiro e outras áreas secas da América do Sul tiveram partes integradas ao comércio internacional pela agricultura irrigada, como a fruticultura do vale do São Francisco (Petrolina e Juazeiro). Alternativa <strong>B</strong>.</p><p>As áreas áridas e semiáridas são, em grande parte, naturais, causadas pelo clima (A); o Atacama e a Patagônia, secos, nem são tropicais (D).</p>",
  figs(("q87", "Mapa da América do Sul classificando as regiões pelo grau de aridez: superárido na costa do Peru e do norte do Chile (Atacama); faixas de árido e semiárido ao longo dos Andes, na Patagônia argentina e no Nordeste brasileiro; subúmido em volta dessas áreas; demais áreas (úmidas) no restante.")),
  ["aridez", "irrigação"], trocas=[("http:// www", "http://www")])
X(88, "Geografia", "Clima", "<p>A chuva depende da evaporação e da condensação do vapor, processos ligados à temperatura do ar. Como as atividades humanas alteram a temperatura em escala local (ilhas de calor) e global (aquecimento), elas podem mudar os padrões de chuva. Alternativa <strong>E</strong>.</p><p>Mais calor aumenta a evaporação e pode trazer mais chuva em algumas regiões, então não há aumento da aridez em todo o planeta (A, C).</p>",
  tags=["mudanças climáticas", "precipitação"])
X(89, "Sociologia", "Cultura brasileira", "<p>A primeira ideia diz que uma cidade criada, como Brasília, nunca teria desenvolvimento natural, porque a vida social não pode ser construída. A segunda responde que o Brasil e toda a América foram criados pelo homem ocidental. A primeira vê as cidades como organismos espontâneos; a segunda mostra exemplos históricos do contrário. Alternativa <strong>E</strong>.</p>",
  tags=["Brasília", "urbanismo"], trocas=[("Vis – Revista", "<em>Vis</em> – Revista")])
X(90, "Geografia", "Biomas", "<p>O texto diz que as águas do Pantanal dependem das cabeceiras dos rios no planalto do cerrado, cujo volume vem diminuindo. Controlar o desmatamento e a erosão nas nascentes protege a planície pantaneira e sua biodiversidade. Alternativa <strong>D</strong>.</p><p>Barragens (E) alterariam o regime de cheias de que o Pantanal depende.</p>",
  tags=["Pantanal", "nascentes"], enun=ap(J(T(90, 0), T(90, 1))) + fonte(T(90, 2).replace("Ciência Hoje", "<em>Ciência Hoje</em>")) + p(T(90, 3)))

completar(Q, R)
