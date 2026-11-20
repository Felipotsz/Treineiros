# Enem 2010, 1º dia, caderno azul: Ciências Humanas (questões 1 a 45; no 1º dia de 2010 vinham Humanas e Natureza).
# Texto legível. Brecht (Q20, ainda protegido no Brasil até 2027) e a canção Opinião, de Zé Keti (Q35), como imagem. Castro Alves (Q26) em texto.
# Sem anuladas nesta área.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, enunciado_enem, paragrafos_enem

ID = "enem-2010-humanas"
META = {"id": ID, "banca": "Enem", "ano": 2010, "titulo": "Enem 2010: Ciências Humanas", "fonte": "Inep", "dataExame": "2010-11-06",
        "duracaoMinutos": 135, "area": "Ciências Humanas", "caderno": "azul", "dia": 1}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2010-dia1-azul")
Q = {}
P = lambda n: paragrafos_enem(D[n])
T = lambda n, i: P(n)[i][1]
p = lambda *xs: "".join(f"<p>{x}</p>" for x in xs)
ap = lambda *xs: "".join(f'<p class="apoio">{x}</p>' for x in xs)
fonte = lambda x: f'<p class="fonte">{x}</p>'
ALT = lambda ini: {k: f"[[fig:{i}]]" for i, k in enumerate("ABCDE", ini)}
tit = lambda x: f'<p class="apoio"><strong>{x}</strong></p>'
LIMPA = lambda s: re.sub(r"fi ([a-zà-ú])", r"fi\1", re.sub(r"fl ([a-zà-ú])", r"fl\1", re.sub(r"(\w)- -(\w)", r"\1-\2", s)))


def figs(*pares):
    return [{"arquivo": a, "alt": t} for a, t in pares]


def X(n, materia, assunto, expl, imagens=(), tags=(), enun=None, trocas=(), alts=None):
    e = LIMPA(enun or enunciado_enem(D[n]))
    for a, b in trocas:
        assert a in e, a; e = e.replace(a, b)
    al = {k: LIMPA(v) for k, v in (alts or D[n]["alternativas"]).items()}
    Q[n] = {"materia": materia, "assunto": assunto, "area": "Ciências Humanas", "tags": list(tags), "numeroOriginal": n,
                 "enunciado": e, "alternativas": al, "imagens": list(imagens), "explicacao": expl}


def tabela(cab, linhas):
    return ('<table class="tabela"><thead><tr>' + "".join(f"<th>{c}</th>" for c in cab) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in l) + "</tr>" for l in linhas) + "</tbody></table>")


LISTA = lambda s: "<ul>" + "".join(f"<li>{x.strip()}</li>" for x in s.split("•") if x.strip()) + "</ul>"
semR = lambda n: {**D[n]["alternativas"], "E": re.sub(r"\s*(Rascunho|Figura para as questões 5 e 6)\s*$", "", D[n]["alternativas"]["E"])}
EROSAO = figs(("q05", "Esquema de uma encosta com vegetação no alto e solo exposto embaixo, cortado por sulcos ou ravinas que descem até uma boçoroca; na base, o nível d’água e uma zona temporariamente encharcada."))
EROSAO_E = tit("Figura para as questões 5 e 6") + "[[fig:1]]" + fonte("TEIXEIRA, W. et al. (Orgs.). <em>Decifrando a Terra</em>. São Paulo: Companhia Editora Nacional, 2009.")


X(1, "Geografia", "Questão agrária", "<p>O gráfico mostra que os imóveis com mais de 1 000 ha ocupam 53% da área rural, e os de até 10 ha, apenas 1,3%. Poucos imóveis muito grandes concentram a maior parte das terras: é <strong>a concentração de terras nas mãos de poucos</strong>. Alternativa <strong>A</strong>.</p><p>Os minifúndios (C) ocupam a menor parte da área, e o gráfico não fala de terras agricultáveis (B).</p>",
  figs(("q01", "Gráfico de setores da área dos imóveis rurais por tamanho: acima de 1 000 ha, 53%; de 100 a 1 000 ha, 30,5%; de 10 a 100 ha, 15,2%; até 10 ha, 1,3%.")), ["estrutura fundiária", "latifúndio"])
X(2, "Geografia", "Agropecuária", "<p>Milton Santos diz que o campo também se tornou um “mundo artificial”, cheio de técnica. Com adubos, corretivos, irrigação e máquinas, é possível produzir em solos antes pouco aproveitados, como os do Cerrado. A consequência é <strong>o aumento do aproveitamento de solos menos férteis</strong>. Alternativa <strong>B</strong>.</p><p>A modernização não reduziu a concentração de terras (A) nem estagnou a fronteira agrícola (D).</p>",
  tags=["meio técnico-científico", "modernização do campo"], trocas=[("A Natureza do Espaço", "<em>A Natureza do Espaço</em>")])
X(3, "Geografia", "Agropecuária", "<p>Com a mecanização, o trabalhador rural perdeu o emprego fixo, foi para a cidade e passou a ser contratado como diarista (o boia-fria), viajando centenas de quilômetros por baixos salários. É uma consequência <strong>dos impactos sociais da modernização da agricultura</strong>. Alternativa <strong>A</strong>.</p><p>“Sete conto por dia” mostra salário baixo, e não recomposição salarial (B).</p>",
  tags=["boia-fria", "êxodo rural"], trocas=[("O migrante e a cidade: dilemas e conflitos", "<em>O migrante e a cidade: dilemas e conflitos</em>")])
X(4, "Geografia", "Questão ambiental", "<p>O lixo a céu aberto atrai ratos, baratas, moscas e mosquitos, que transmitem doenças, e o chorume contamina o solo e as águas. Os lixões são problema de saúde pública porque <strong>são locais propícios à proliferação de vetores de doenças, além de contaminarem o solo e as águas</strong>. Alternativa <strong>B</strong>.</p><p>A chuva ácida (C) vem de gases como óxidos de enxofre e nitrogênio, e não da decomposição do lixo.</p>",
  tags=["lixões", "chorume"], enun=ap(T(4, 0)) + fonte(T(4, 1).replace("Almanaque Brasil Socioambiental 2008", "<em>Almanaque Brasil Socioambiental 2008</em>")) + p(T(4, 2)), alts=semR(4))
X(5, "Geografia", "Solos", "<p>Arar o solo do topo ao vale cria sulcos no sentido da descida, por onde a água da chuva escorre com força, levando o solo. Isso acelera a erosão: é a <strong>aração do solo, do topo ao vale</strong>. Alternativa <strong>D</strong>.</p><p>Plantio direto, curvas de nível e terraceamento (A, C e E) são técnicas que reduzem a erosão.</p>",
  EROSAO, ["erosão", "conservação do solo"], enun=EROSAO_E + p(T(5, 0)))
X(6, "Geografia", "Solos", "<p>O solo erodido nas encostas desce com a água e se deposita no fundo dos rios das baixadas. Os rios ficam mais rasos (assoreados) e transbordam com mais facilidade. O reflexo nas cidades é <strong>a maior ocorrência de enchentes, já que os rios assoreados comportam menos água em seus leitos</strong>. Alternativa <strong>A</strong>.</p><p>Com a erosão, o escoamento superficial aumenta, e não diminui (C).</p>",
  EROSAO, ["assoreamento", "enchentes"], enun=EROSAO_E + p(T(6, 0)))
X(7, "Geografia", "Cartografia", "<p>A latitude (49º49’ N) e a longitude (23º49’ W) são as coordenadas geográficas: um sistema de linhas imaginárias, os paralelos e os meridianos, que permite localizar qualquer ponto da Terra. Coordenada geográfica é <strong>a informação de um conjunto de linhas imaginárias que permitem localizar um ponto ou acidente geográfico na superfície terrestre</strong>. Alternativa <strong>C</strong>.</p><p>A opção D troca as definições de latitude e longitude.</p>",
  tags=["coordenadas geográficas", "latitude e longitude"], trocas=[("Parati: entre dois pólos", "<em>Parati: entre dois pólos</em>")])
X(8, "Geografia", "Geologia", "<p>Fósseis se preservam em rochas sedimentares: os restos dos animais são cobertos por sedimentos, que se compactam e endurecem (litificação). O esquema mostra camadas sobrepostas, típicas dessas rochas. As rochas são <strong>sedimentares, pois os restos podem ter sido soterrados e litificados com o restante dos sedimentos</strong>. Alternativa <strong>B</strong>.</p><p>Cada camada representa deposição, e não erosão (D).</p>",
  figs(("q08", "Esquema de dois morros com camadas de rocha sobrepostas, cortadas por um vale; nas camadas aparecem fósseis de animais, como ossos, conchas e esqueletos.")), ["rochas sedimentares", "fósseis"],
  trocas=[("Decifrando a Terra", "<em>Decifrando a Terra</em>")])
X(9, "Geografia", "Globalização", "<p>A sigla BRIC foi criada em 2001 por um economista do banco Goldman Sachs para indicar os países emergentes com grande potencial de crescimento: grandes territórios, populações e mercados. Eles <strong>apresentam características econômicas promissoras para as próximas décadas</strong>. Alternativa <strong>A</strong>.</p><p>Esses países têm grande desigualdade social (C) e culturas muito diferentes (E).</p>",
  tags=["BRIC", "G-20"])
X(10, "História", "Revolução Industrial", "<p>O texto diz que tudo virava lucro, até a sujeira, as favelas e a miséria, e compara as fábricas às pirâmides, que mostram “mais a escravização do homem que seu poder”. A relação é que <strong>o alto nível de exploração dos trabalhadores industriais ocasionava o surgimento de aglomerados urbanos marcados por péssimas condições de moradia, saúde e higiene</strong>. Alternativa <strong>E</strong>.</p>",
  tags=["cidades industriais", "exploração do trabalho"], trocas=[("A Revolução Industrial", "<em>A Revolução Industrial</em>")])
X(11, "História", "Revolução Industrial", "<p>No artesanato, o artesão fazia o produto inteiro com as próprias mãos e ferramentas simples, no seu ritmo, e cada peça era única. Ele <strong>trabalhava geralmente sem o uso de máquinas e de modo diferente do modelo de produção em série</strong>. Alternativa <strong>B</strong>.</p><p>O ritmo das máquinas e a padronização (A) são da maquinofatura; a divisão do trabalho com assalariados (D) é da manufatura.</p>",
  tags=["artesanato", "manufatura e maquinofatura"], trocas=[("matériasprimas", "matérias-primas")])
X(12, "História", "Primeira República", "<p>A serraria Lumber e a ferrovia destruíram os ervais nativos, de onde os posseiros tiravam a erva-mate, e tomaram as terras para a colonização. Quem vivia da economia tradicional perdeu o sustento e a terra. Entre os impactos estava <strong>a desorganização da economia tradicional, que sustentava os posseiros e os trabalhadores rurais da região</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["Guerra do Contestado", "posseiros"], trocas=[("Lideranças do Contestado", "<em>Lideranças do Contestado</em>")], alts={**D[12]["alternativas"], "E": D[12]["alternativas"]["E"].replace(" .", ".")})
X(13, "História", "Primeira República", "<p>Os seringueiros nordestinos ocuparam o Acre, que pertencia à Bolívia, e não aceitavam a autoridade boliviana. A presença maciça de brasileiros levou ao conflito e, depois, ao Tratado de Petrópolis (1903), em que o Brasil comprou a região. O Acre se tornou brasileiro <strong>devido à crescente emigração de brasileiros que exploravam os seringais</strong>. Alternativa <strong>C</strong>.</p><p>No tratado, foi o Brasil que indenizou a Bolívia (A e E).</p>",
  tags=["Acre", "ciclo da borracha"])
X(14, "Geografia", "Indústria e mineração", "<p>A Estrada de Ferro Carajás leva ao porto de São Luís o minério de ferro da Serra dos Carajás, no Pará, uma das maiores reservas do mundo, além de manganês e cobre. A importância estratégica está na <strong>capacidade de produção de minerais metálicos</strong>. Alternativa <strong>C</strong>.</p><p>O minério é exportado, e não importado (D), e não é recurso energético (E).</p>",
  tags=["Carajás", "minério de ferro"])
X(15, "Geografia", "Energia", "<p>Belo Monte traz energia para o crescimento do país, mas inunda terras, afeta indígenas e agricultores e altera o rio Xingu. Os impasses estão ligados <strong>à necessidade de equilibrar e compatibilizar o investimento no crescimento do país com os esforços para a conservação ambiental</strong>. Alternativa <strong>B</strong>.</p><p>O texto não compara o potencial das bacias (A).</p>",
  tags=["Belo Monte", "hidrelétricas"], trocas=[("Istoé Dinheiro", "<em>Istoé Dinheiro</em>")])
X(16, "História", "América pré-colombiana", "<p>O texto descreve uma sociedade fortemente estratificada, com imperador, nobres e sacerdotes no topo e camponeses e escravos na base, sem mobilidade: a posição era herdada. A característica era a <strong>impossibilidade de se mudar de extrato social e a existência de uma aristocracia hereditária</strong>. Alternativa <strong>E</strong>.</p><p>Não havia igualdade social (A e B).</p>",
  tags=["incas", "estratificação social"])
X(17, "Geografia", "Questão agrária", "<p>Os Xavante e os Timbira protestaram em São Paulo contra o cerco de suas terras pelo agronegócio. A tensão é entre <strong>a expansão territorial do agronegócio, em especial nas regiões Centro-Oeste e Norte, e as leis de proteção indígena e ambiental</strong>. Alternativa <strong>A</strong>.</p><p>Os indígenas mostraram organização ao levar o protesto à Avenida Paulista (B).</p>",
  tags=["povos indígenas", "agronegócio"], trocas=[("Povos indígenas do Brasil: 2001-2005", "<em>Povos indígenas do Brasil: 2001-2005</em>")])
X(18, "História", "Brasil pré-cabralino", "<p>Os Tupi-guarani viviam em aldeias que se mudavam de tempos em tempos (seminômades, com agricultura de coivara) e faziam guerras rituais entre tribos, com captura de prisioneiros e antropofagia ritual. Destacava-se <strong>a ritualização da guerra entre as tribos e o caráter semissedentário de sua organização social</strong>. Alternativa <strong>B</strong>.</p><p>Eles praticavam a antropofagia (E) e a agricultura (D).</p>",
  tags=["tupi-guarani", "guerra ritual"], trocas=[("O Brasil antes dos brasileiros", "<em>O Brasil antes dos brasileiros</em>")])
X(19, "História", "Brasil Colônia", "<p>Os tropeiros levavam gado e mercadorias em longas viagens no lombo de mulas e precisavam de comida que durasse: feijão, farinha, toucinho e carne seca. O prato nasceu da <strong>atividade mercantil exercida pelos homens que transportavam gado e mercadoria</strong>. Alternativa <strong>C</strong>.</p><p>Os tropeiros não eram mineradores (E) nem agricultores (D).</p>",
  tags=["tropeirismo", "mineração"], alts=semR(19))
X(20, "História", "Memória e história", "<p>O poema pergunta quem construiu Tebas, a Babilônia, a Muralha da China e os arcos de Roma, já que os livros só registram nomes de reis e césares. A crítica é que <strong>os grandes monumentos históricos foram construídos por trabalhadores, mas sua memória está vinculada aos governantes das sociedades que os construíram</strong>. Alternativa <strong>C</strong>.</p>",
  figs(("q20", "Trecho do poema “Perguntas de um trabalhador que lê”, de Bertolt Brecht: uma série de perguntas sobre quem construiu Tebas, a Babilônia, as casas de Lima e a Muralha da China, e sobre quem ergueu os arcos de triunfo de Roma, já que os livros só trazem nomes de reis.")),
  ["Brecht", "história vista de baixo"], enun="[[fig:1]]" + p(T(20, 2)))
X(21, "História", "Patrimônio cultural", "<p>As ruínas de Canudos são vestígios materiais (restos de construções, objetos) e estão inseridas na paisagem do sertão, útil para pesquisar a guerra e o modo de vida. Elas reúnem <strong>objetos arqueológicos e paisagísticos</strong>. Alternativa <strong>A</strong>.</p><p>Práticas e representações (D e E) são patrimônio imaterial.</p>",
  tags=["Canudos", "Iphan"])
X(22, "História", "Brasil Império", "<p>Chiavenatto atribui a guerra ao imperialismo inglês; Doratioto diz que essa “teoria conspiratória” não tem provas. As duas narrativas divergem justamente sobre as causas: elas refletem sobre <strong>a dificuldade de elaborar explicações convincentes sobre os motivos dessa Guerra</strong>. Alternativa <strong>D</strong>.</p><p>Não se trata de falta de fontes (A): Doratioto se apoia em documentos.</p>",
  tags=["Guerra do Paraguai", "historiografia"], trocas=[("status quo", "<em>status quo</em>"), ("Genocídio americano: A Guerra do Paraguai", "<em>Genocídio americano: A Guerra do Paraguai</em>"), ("Maldita guerra: nova história da Guerra do Paraguai", "<em>Maldita guerra: nova história da Guerra do Paraguai</em>")])
X(23, "História", "Brasil Império", "<p>Luiz Gama, filho de escrava, foi vendido ilegalmente, conquistou a liberdade e virou advogado sem diploma, defendendo escravizados nos tribunais. Sua biografia mostra a <strong>extrema dificuldade de projeção dos intelectuais negros nesse contexto e a utilização do Direito como canal de luta pela liberdade</strong>. Alternativa <strong>B</strong>.</p><p>Ele ascendeu, então não era impossível (A e C), e não teve apoio das elites (D).</p>",
  tags=["Luiz Gama", "abolicionismo"], trocas=[("Revista de História", "<em>Revista de História</em>")])
X(24, "História", "Período Joanino", "<p>Em 1810, os tratados com a Inglaterra deram aos produtos ingleses taxas menores que as dos próprios portugueses. Sem proteção, as manufaturas da colônia não podiam competir com a indústria inglesa. A explicação é <strong>a dependência portuguesa da Inglaterra e o predomínio industrial inglês sobre suas redes de comércio</strong>. Alternativa <strong>B</strong>.</p>",
  tags=["alvará de 1808", "tratados de 1810"], trocas=[("Textos políticos da História do Brasil", "<em>Textos políticos da História do Brasil</em>")])
X(25, "História", "Período Joanino", "<p>Entre os eventos de 1808-1821 está a conquista da Banda Oriental (Cisplatina, atual Uruguai), em 1816-1821. Dom João atacou a região do Prata em represália à Espanha, aliada de Napoleão. Uma consequência foi <strong>a conquista da região do rio da Prata em represália à aliança entre a Espanha e a França de Napoleão</strong>. Alternativa <strong>C</strong>.</p><p>O tráfico de escravos para o Brasil só terminou em 1850 (B).</p>",
  tags=["família real", "Cisplatina"],
  enun=ap(T(25, 0), T(25, 1)) + LISTA(T(25, 2)) + fonte(T(25, 3).replace("1808: como uma rainha louca, um príncipe medroso e uma corte corrupta enganaram Napoleão e mudaram a história de Portugal e do Brasil", "<em>1808: como uma rainha louca, um príncipe medroso e uma corte corrupta enganaram Napoleão e mudaram a história de Portugal e do Brasil</em>")) + p(T(25, 4)))
X(26, "História", "Primeira República", "<p>A República nasceu de um golpe militar, sem participação popular, e precisava de símbolos que a legitimassem. Tiradentes, mártir “cívico-religioso”, parecido com Cristo e capaz de unir todos, servia a isso. O esforço estava ligado <strong>ao fato de a proclamação da República ter sido um movimento de poucas raízes populares, que precisava de legitimação</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["Tiradentes", "símbolos da República"],
  enun=ap("<strong>I</strong> – " + T(26, 0)[4:].replace("cívicoreligioso", "cívico-religioso")) + fonte(T(26, 1).replace("A formação das almas: O imaginário da República no Brasil", "<em>A formação das almas: O imaginário da República no Brasil</em>"))
       + ap("<strong>II</strong> – Ei-lo, o gigante da praça,<br>O Cristo da multidão!<br>É Tiradentes quem passa<br>Deixem passar o Titão.")
       + fonte("ALVES, C. Gonzaga ou a revolução de Minas. In: CARVALHO, J. M. C. <em>A formação das almas: O imaginário da República no Brasil</em>. São Paulo: Companhia das Letras, 1990.") + p(T(26, 4)))
X(27, "História", "Primeira República", "<p>A capoeira era prática cultural de origem africana, ligada aos negros e pobres. Ao tratá-la como crime, logo após a abolição, o Código Penal mostrava <strong>a criminalização de práticas culturais e a persistência de valores que vinculavam certos grupos ao passado de escravidão</strong>. Alternativa <strong>D</strong>.</p><p>Em 1890 a escravidão já tinha acabado (B e E).</p>",
  tags=["capoeira", "Código Penal de 1890"], trocas=[("A Negregada instituição: os capoeiras no Rio de Janeiro: 1850-1890", "<em>A Negregada instituição: os capoeiras no Rio de Janeiro: 1850-1890</em>")])
X(28, "História", "Revolução Francesa", "<p>Robespierre era líder jacobino, no período do Terror. Os jacobinos representavam a pequena e média burguesia e as camadas populares (os <em>sans-culottes</em>) e queriam uma república virtuosa, com justiça social. O discurso se liga <strong>aos representantes da pequena e média burguesia e das camadas populares, que desejavam justiça social e direitos políticos</strong>. Alternativa <strong>E</strong>.</p>",
  tags=["jacobinos", "Robespierre"], trocas=[("História da Vida Privada: da Revolução Francesa à Primeira Guerra", "<em>História da Vida Privada: da Revolução Francesa à Primeira Guerra</em>")])
X(29, "Filosofia", "Política", "<p>No primeiro momento, a política impedia o povo de decidir; no segundo, obriga o povo a decidir sobre o que não entende. Nos dois casos, quem realmente decide é um grupo pequeno, que concentra o conhecimento e o poder. O elemento comum é <strong>o controle das decisões por uma minoria</strong>. Alternativa <strong>C</strong>.</p><p>No segundo momento há participação (B), mas sem compreensão.</p>",
  tags=["Paul Valéry", "democracia"], trocas=[("A cidadania ativa", "<em>A cidadania ativa</em>")])
X(30, "Filosofia", "Maquiavel", "<p>Para Maquiavel, o príncipe pode ser cruel se isso mantiver o povo unido e leal: “uns poucos exemplos duros” evitam desordens maiores. A ordem dependia de ajustar o uso da força às necessidades de governar, da <strong>conveniência entre o poder tirânico e a moral do príncipe</strong>. Alternativa <strong>E</strong>.</p><p>Maquiavel defende o contrário de bondade e compaixão (B e C).</p>",
  tags=["O Príncipe", "realismo político"], trocas=[("O Príncipe. São Paulo", "<em>O Príncipe</em>. São Paulo"), ("escreveu O Príncipe", "escreveu <em>O Príncipe</em>")])
X(31, "História", "Período Regencial", "<p>O texto descreve crises, revoltas e disputas pelo poder (convulsão política) e a expansão do café com os “barões do café” (nova realidade econômica), mas a escravidão e o latifúndio continuaram. O período foi marcado <strong>pela convulsão política e por novas realidades econômicas que exigiam o reforço de velhas realidades sociais</strong>. Alternativa <strong>E</strong>.</p>",
  tags=["Regências", "café"])
X(32, "História", "Era Vargas", "<p>Vargas criou leis trabalhistas (salário mínimo, férias, jornada de oito horas, carteira de trabalho), apresentadas como “dádiva”, mas que respondiam a reivindicações antigas dos operários. Resultou a <strong>legislação trabalhista que atendeu reivindicações dos operários, garantindo-lhes vários direitos e formas de proteção</strong>. Alternativa <strong>D</strong>.</p><p>Os sindicatos ficaram atrelados ao Estado, sem autonomia (A e E).</p>",
  tags=["trabalhismo", "Estado Novo"], trocas=[("A força nacionalizadora do Estado Novo", "<em>A força nacionalizadora do Estado Novo</em>"), ("Nos tempos de Getúlio: da revolução de 30 ao fim do Estado Novo", "<em>Nos tempos de Getúlio: da revolução de 30 ao fim do Estado Novo</em>")],
  alts={**D[32]["alternativas"], "D": "legislação trabalhista que atendeu reivindicações dos operários, garantindo-lhes vários direitos e formas de proteção."})
X(33, "História", "República Populista", "<p>O texto diz que a inflação, a queda dos salários e a menor oferta de empregos, “sobras” do modelo de desenvolvimento, provocaram greves e mobilização. Os conflitos decorreram <strong>das contradições econômicas do modelo desenvolvimentista</strong>. Alternativa <strong>B</strong>.</p><p>O texto não atribui os conflitos à manipulação do governo (A).</p>",
  tags=["golpe de 1964", "desenvolvimentismo"], trocas=[("A Industrialização Brasileira", "<em>A Industrialização Brasileira</em>")])
X(34, "Filosofia", "Foucault", "<p>Para Foucault, a lei não nasce de uma natureza pacífica, mas das batalhas e das conquistas: é a continuação da guerra por outros meios. As leis servem para <strong>organizar as relações de poder na sociedade e entre os Estados</strong>. Alternativa <strong>E</strong>.</p><p>Foucault não vê a lei como instrumento ético (D), e sim como expressão de forças.</p>",
  tags=["poder", "lei"], trocas=[("Em defesa da sociedade", "<em>Em defesa da sociedade</em>")])
X(35, "História", "Ditadura Militar", "<p>O show <em>Opinião</em> estreou em dezembro de 1964, logo depois do golpe. A canção mostra o morador do morro que não muda de opinião, resiste à pobreza e à repressão. A MPB serviu de <strong>denúncia da situação social e política do país</strong>. Alternativa <strong>D</strong>.</p><p>A canção afirma resistência, e não passividade (C).</p>",
  figs(("q35", "Letra da canção “Opinião”, de Zé Keti: o morador do morro diz que podem prendê-lo, bater nele e deixá-lo sem comer, mas ele não muda de opinião e não sai do morro; se falta água ou carne, ele dá um jeito; ali não paga aluguel e, se morrer, está pertinho do céu.")),
  ["MPB", "show Opinião"], enun="[[fig:1]]" + fonte("ZÉ KETTI. <em>Opinião</em>. Disponível em: http://www.mpbnet.com.br. Acesso em: 28 abr. 2010.") + p(T(35, 6).replace("tea- tral", "teatral").replace("pa- pel", "papel")))
X(36, "História", "Brasil contemporâneo", "<p>A imprensa na TV ajudou a democracia ao mostrar escândalos de corrupção, como no caso Collor e em vários governos, levando o público a cobrar providências. A TV foi útil à democracia porque <strong>revelou para o país casos de corrupção na esfera política de vários governos</strong>. Alternativa <strong>B</strong>.</p><p>As outras alternativas descrevem usos a favor de governos autoritários.</p>",
  tags=["televisão", "imprensa"], trocas=[("História da Vida Privada no Brasil 3", "<em>História da Vida Privada no Brasil 3</em>")])
X(37, "Sociologia", "Meios de comunicação", "<p>O texto fala de um meio que supera os demais e permite “mecanismos eletrônicos para a efetiva participação política e disseminação de informações”: uma rede informacional. O exemplo mais expressivo é a <strong>Internet</strong>. Alternativa <strong>A</strong>.</p><p>Fibra ótica (B) é um suporte físico, e não um meio de comunicação.</p>",
  tags=["internet", "democracia"])
X(38, "História", "Revolução Industrial", "<p>Milton Santos compara os luditas, que quebravam máquinas, aos ambientalistas de hoje. Eles reagiam à perda de empregos e à degradação das cidades e do campo. Os movimentos se expressaram por meio <strong>da contestação à degradação do trabalho, das tradições e da natureza</strong>. Alternativa <strong>E</strong>.</p><p>Os luditas não eram ideólogos conservacionistas (A) nem agiam por políticas de governo (B).</p>",
  tags=["ludismo", "ambientalismo"], trocas=[("A natureza do espaço: técnica e tempo, razão e emoção", "<em>A natureza do espaço: técnica e tempo, razão e emoção</em>")])
X(39, "Filosofia", "Ética", "<p>O texto diz que a ética é um “empreendimento coletivo”, que cada grupo deve se sentir “responsável por todos” e que a ética se liga à política e à educação. Ela é <strong>instrumento de garantia da cidadania, porque através dela os cidadãos passam a pensar e agir de acordo com valores coletivos</strong>. Alternativa <strong>A</strong>.</p><p>O texto prioriza o coletivo, e não interesses privados (D).</p>",
  tags=["ética", "cidadania"], trocas=[("Para filosofar", "<em>Para filosofar</em>")])
X(40, "História", "Revolução Industrial", "<p>Shelley pergunta aos trabalhadores por que aram, tecem e alimentam os “parasitas” que os mantêm na miséria. Quem trabalha produz a riqueza, mas não a desfruta. A contradição está <strong>na riqueza, que não era usufruída por aqueles que a produziam</strong>. Alternativa <strong>E</strong>.</p>",
  tags=["Shelley", "exploração do trabalho"], trocas=[("História da Riqueza do Homem", "<em>História da Riqueza do Homem</em>")])
X(41, "Sociologia", "Diversidade", "<p>O primeiro texto mostra que, desde o período colonial, a Igreja chamava a homossexualidade de “pecado nefando”. O segundo mostra recorde de assassinatos por homofobia em 2009. A violência atual se liga <strong>a um passado histórico marcado pela demonização do corpo e por formas recorrentes de tabus e intolerância</strong>. Alternativa <strong>D</strong>.</p><p>A Constituição de 1988 não exclui os homossexuais (C).</p>",
  tags=["homofobia", "Inquisição"],
  enun=ap(T(41, 0)) + fonte("NOVAIS, F.; MELLO E SOUZA, L. <em>História da Vida Privada no Brasil</em>. V. 1. São Paulo: Companhia das Letras, 1997 (adaptado).")
       + ap("O número de homossexuais assassinados no Brasil bateu o recorde histórico em 2009. " + T(41, 2).replace("Travestis )", "Travestis)")) + fonte(T(41, 3)) + p(T(41, 4)))
X(42, "História", "América Latina", "<p>O juiz diz que as cortes rejeitaram mais de 10 mil <em>habeas corpus</em> e que os casos de desaparecidos só tiveram “trâmite formal”, deixando os agentes do Estado impunes. A relação era de <strong>subordinação do poder judiciário aos interesses políticos dominantes</strong>. Alternativa <strong>E</strong>.</p>",
  tags=["ditadura chilena", "Pinochet"],
  enun=tit("Judiciário contribuiu com ditadura no Chile, diz Juiz Guzmán Tapia") + ap(T(42, 1).replace("Guzmán Tapia ", "", 1).replace("habeas corpus", "<em>habeas corpus</em>")) + fonte(T(42, 2)) + p(T(42, 3)))
X(43, "Sociologia", "Trabalho", "<p>O banco cobra para atender no guichê, empurrando o cliente para as máquinas, e assim pode fechar agências e demitir. O argumento das empresas é reduzir custos, e a consequência para o trabalhador é perder o emprego: <strong>diminuição dos custos e insegurança no emprego</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["automação", "desemprego estrutural"], trocas=[("O novo século", "<em>O novo século</em>")], alts=semR(43))
X(44, "Filosofia", "Ética", "<p>Severino diz que o sujeito é “histórico-social” e que a ação humana não pode ser avaliada fora da relação social: a ética se entrelaça com a política. O texto ressalta <strong>o sentido coletivo e político das ações humanas individuais</strong>. Alternativa <strong>D</strong>.</p><p>O texto recusa preceitos metafísicos (B).</p>",
  tags=["ética", "política"])
X(45, "Filosofia", "Política", "<p>Na tirinha, as crianças fazem fila para tomar uma “vacina contra o despotismo”. Numa democracia, em que o povo exerce a soberania, essa vacina serviria para que o povo não escolhesse ou aceitasse governantes que concentram o poder: <strong>evitar a escolha de governantes autoritários</strong>. Alternativa <strong>D</strong>.</p>",
  figs(("q45", "Tirinha da Mafalda: crianças em fila diante de uma enfermeira com uma mesa de vacinas, e uma delas diz: “Viemos nos vacinar contra o despotismo!”.")), ["democracia", "Mafalda"],
  alts=semR(45), trocas=[("Toda Mafalda", "<em>Toda Mafalda</em>"), ("Dicionário Básico de Filosofia", "<em>Dicionário Básico de Filosofia</em>")])

completar(Q, R)
