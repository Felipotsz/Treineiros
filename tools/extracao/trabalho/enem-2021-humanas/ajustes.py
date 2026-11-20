# Enem 2021, 1º dia, caderno azul: Ciências Humanas (questões 46 a 90 do caderno; no site, 1 a 45, com numeroOriginal).
# A camada de texto do PDF de 2021 vem embaralhada (fontes com nomes de glifo /gN e ToUnicode errado):
# o rascunho é feito com DECOD=1, que refaz o texto glifo a glifo (tools/enem_decod.py).
# Letra de Zé Ramalho (Q60) como imagem. Sem anuladas nesta área.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, enunciado_enem, paragrafos_enem

ID = "enem-2021-humanas"
META = {"id": ID, "banca": "Enem", "ano": 2021, "titulo": "Enem 2021: Ciências Humanas", "fonte": "Inep", "dataExame": "2021-11-21",
        "duracaoMinutos": 135, "area": "Ciências Humanas", "caderno": "azul", "dia": 1}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2021-dia1-azul")
Q = {}
P = lambda n: paragrafos_enem(D[n])
T = lambda n, i: P(n)[i][1]
p = lambda *xs: "".join(f"<p>{x}</p>" for x in xs)
ap = lambda *xs: "".join(f'<p class="apoio">{x}</p>' for x in xs)
fonte = lambda x: f'<p class="fonte">{x}</p>'
HIF = lambda s: re.sub(r"(\w)- -(\w)", r"\1-\2", s)          # hífen de quebra de linha duplicado ("anglo- -brasileiro")


def figs(*pares):
    return [{"arquivo": a, "alt": t} for a, t in pares]


def X(n, materia, assunto, expl, imagens=(), tags=(), enun=None, trocas=(), alts=None):
    e = HIF(enun or enunciado_enem(D[n]))
    for a, b in trocas:
        assert a in e, a; e = e.replace(a, b)
    al = {k: re.sub(r"\s*SOLSTÍCIO.*$", "", HIF(v)) for k, v in (alts or D[n]["alternativas"]).items()}
    Q[n - 45] = {"materia": materia, "assunto": assunto, "area": "Ciências Humanas", "tags": list(tags), "numeroOriginal": n,
                 "enunciado": e, "alternativas": al, "imagens": list(imagens), "explicacao": expl}


X(46, "Sociologia", "Trabalho", "<p>O texto mostra o trabalhador que, já em casa, no jantar com a família, fica pensando nas mensagens do trabalho e volta a ele pelo celular. A tecnologia leva o trabalho para dentro de casa e reduz o tempo livre: há uma <strong>ampliação de atividades extras</strong> fora do expediente. Alternativa <strong>B</strong>.</p><p>A vida privada é invadida, não protegida (A); não há burocracia (C), lazer (D) ou fuga das tarefas de casa (E).</p>",
  tags=["tecnologia", "jornada de trabalho"], trocas=[("grupo de WhatsApp", "grupo de <em>WhatsApp</em>")])
X(47, "Sociologia", "Desigualdade", "<p>As democracias liberais justificam as diferenças de renda pelo mérito: quem se esforça e trabalha mais ganha mais. Piketty mostra que, quando o capital rende mais que o crescimento da economia, a riqueza herdada supera a riqueza construída pelo trabalho. Isso enfraquece a <strong>ideologia do mérito</strong>. Alternativa <strong>A</strong>.</p><p>A herança fortalece, não enfraquece, o “direito de nascimento” (B); o texto não fala de leis, financeiras ou eficiência (C, D e E).</p>",
  tags=["Piketty", "meritocracia"])
X(48, "Geografia", "Agropecuária", "<p>O programa cria variedades de uva por seleção e cruzamento para atender regiões muito diferentes: o Semiárido nordestino, áreas tropicais e a Serra Gaúcha. As técnicas adaptam o cultivo aos <strong>elementos ambientais singulares</strong> (clima, solo, relevo) de cada lugar. Alternativa <strong>D</strong>.</p><p>O texto cita exportação (contra E) e não fala de espécies nativas ameaçadas (A), cadeias autônomas (B) ou estrutura fundiária (C).</p>",
  tags=["melhoramento genético", "vitivinicultura"])
X(49, "História", "Patrimônio", "<p>A Carta de Veneza defende preservar os monumentos “na plenitude de sua autenticidade”, como bem comum da humanidade. Telles critica o tombamento, que congela o monumento, reduz seu valor e acaba levando ao abandono. Os textos divergem sobre as <strong>políticas de conservação de bens culturais</strong>. Alternativa <strong>C</strong>.</p><p>Os textos não falam de comércio de imagens (A), troca de materiais (B), privatização (D) ou museus (E).</p>",
  tags=["tombamento", "Carta de Veneza"])
X(50, "Geografia", "Globalização", "<p>Os países ricos geram cada vez mais lixo eletrônico e, em vez de reciclá-lo, mandam-no para países pobres como Gana, onde jovens o desmontam em condições perigosas. Os custos ambientais e de saúde ficam com a periferia: é um padrão da <strong>divisão internacional do trabalho</strong>. Alternativa <strong>B</strong>.</p><p>A prática não é sustentável (D) nem cidadã (A); não envolve toyotismo (C) ou barreiras alfandegárias (E).</p>",
  tags=["lixo eletrônico", "centro e periferia"])
X(51, "Geografia", "Recursos hídricos", "<p>A Unesco propõe preços justos e autorizações de uso para atender tanto a indústria e a irrigação em grande escala quanto a agricultura pequena e de subsistência. A segurança hídrica se baseia na <strong>distribuição equitativa do abastecimento</strong> entre usos e usuários. Alternativa <strong>A</strong>.</p><p>O texto não trata de abastecimento urbano (B), racionamento (C), solos (D) ou reciclagem (E).</p>",
  tags=["segurança hídrica", "gestão da água"])
X(52, "História", "Brasil Império", "<p>O governo brasileiro e os livre-cambistas queriam revogar a Lei Aberdeen, com que a Inglaterra reprimia navios negreiros. O governo britânico temia que, sem um tratado substituto, os brasileiros “voltassem aos velhos hábitos”, isto é, ao tráfico. O interesse britânico era <strong>manter a proibição comercial</strong> do tráfico de escravos. Alternativa <strong>D</strong>.</p><p>O texto não fala de conciliação (A), negócios conjuntos (B), higienismo (C) ou negócios familiares (E).</p>",
  tags=["Lei Aberdeen", "tráfico negreiro"], trocas=[("colunas do Daily News", "colunas do <em>Daily News</em>")])
X(53, "Geografia", "Cultura e região", "<p>Zé de Sila, contador de histórias como o Chicó, lembra a avó que emborcava pratos no terreiro e rezava para a chuva durar mais. São <strong>práticas místicas associadas ao patrimônio cultural</strong> nordestino. Alternativa <strong>B</strong>.</p><p>O “encantador de viúvas” é só um apelido (A); não há teatro político (C), filme (D) ou literatura sobre catástrofes (E).</p>",
  tags=["cultura popular", "religiosidade"], trocas=[("do Auto da Compadecida", "do <em>Auto da Compadecida</em>")])
X(54, "Sociologia", "Trabalho", "<p>O texto diz que as novas tecnologias vieram com uma nova forma de controle do capital, e que seus efeitos constantes são terceirização, precarização e flexibilização. A crítica é à <strong>fragilização das relações de trabalho</strong>. Alternativa <strong>C</strong>.</p><p>O texto não critica a organização da tarefa (A), a capacitação (B), cargos executivos (D) ou a ciência (E).</p>",
  tags=["reestruturação produtiva", "precarização"])
X(55, "Geografia", "Migrações", "<p>O refugiado vive entre dois mundos: não pertence plenamente à comunidade que o recebe (desenraizamento identitário) e perde o status de cidadão do país de origem, com só um status provisório no novo país (insegurança jurídica). A transitoriedade vem do <strong>desenraizamento cultural e da insegurança legal</strong>. Alternativa <strong>E</strong>.</p><p>O texto não fala de ascensão social (A), miscigenação (B), polícia (C) ou crise econômica (D).</p>",
  tags=["refugiados", "identidade"])
X(56, "História", "Ciência e gênero", "<p>As mulheres do século XIX só participavam de expedições como esposas, acompanhando os maridos, e não com projetos científicos próprios. O papel delas na ciência repetia a posição de subordinação que tinham na sociedade: <strong>incorporação das estratificações sociais</strong>. Alternativa <strong>D</strong>.</p><p>O texto mostra o contrário de igualdade de gênero ou superação do patriarcado (A e C).</p>",
  tags=["mulheres na ciência"])
X(57, "Filosofia", "Escola de Frankfurt", "<p>Para Marcuse, a sociedade industrial transforma necessidades sociais em individuais de forma tão eficaz que as pessoas “se reconhecem em suas mercadorias” e encontram “sua alma em seu automóvel”. Os desejos pessoais são moldados por <strong>mecanismos subjetivos de identificação</strong> com os objetos de consumo. Alternativa <strong>D</strong>.</p><p>O controle não vem do Estado (A) nem de regras coletivas (C), mas da própria subjetividade.</p>",
  tags=["Marcuse", "consumo"])
X(58, "Geografia", "Espaço urbano", "<p>O texto descreve a cidade em transformação constante: praças viram concreto, árvores são derrubadas, guindastes e betoneiras por toda parte, e os moradores perdem suas referências. É a <strong>alteração da organização da paisagem geográfica</strong>. Alternativa <strong>E</strong>.</p><p>O texto mostra o desaparecimento, não a manutenção, do convívio e do espaço público (A e B).</p>",
  tags=["paisagem urbana", "produção do espaço"])
X(59, "Geografia", "Clima", "<p>O sertanejo prevê chuva ou seca observando a cor da lua cheia, as nuvens e os astros, conhecimento acumulado ao longo do tempo. É um saber construído pela <strong>experiência perceptiva</strong>. Alternativa <strong>B</strong>.</p><p>Não é técnica científica (A); o saber vem da tradição (contra C), e não há padronização (D e E).</p>",
  tags=["saberes tradicionais"])
X(60, "Sociologia", "Cultura e política", "<p>A canção chama o povo de “massa” que “passa nos projetos do futuro”, que dá “muito mais do que recebe” e vive uma “vida de gado”, “povo marcado”, mas “feliz”. A crítica é à <strong>passividade social</strong>, à aceitação conformada da exploração. Alternativa <strong>B</strong>.</p><p>A letra critica a falta, e não o excesso, de militância e inconformismo (A e E).</p>",
  figs(("q60", "Trecho da letra “Admirável gado novo”, de Zé Ramalho, como aparece na prova: os versos se dirigem à massa que passa nos projetos do futuro, que caminha muito e dá mais do que recebe, e comparam esse povo a gado marcado, chamado ironicamente de feliz.")),
  ["Zé Ramalho", "alienação"], enun="[[fig:1]]" + fonte(T(60, 1).replace("A peleja do diabo com o dono do céu.", "<em>A peleja do diabo com o dono do céu</em>.")) + p(T(60, 2)))
X(61, "Geografia", "Espaço urbano", "<p>O Porto Maravilha quer transformar o Rio num polo internacional de serviços, com torres comerciais e áreas de consumo, como os <em>waterfronts</em> de Baltimore e Barcelona. A intervenção busca a <strong>intensificação da participação na competitividade global</strong>. Alternativa <strong>A</strong>.</p><p>A “revitalização” valoriza o solo (contra B), expulsa moradores pobres (contra C) e apaga as funções tradicionais (D).</p>",
  tags=["Porto Maravilha", "cidade global"], trocas=[("dos waterfronts de", "dos <em>waterfronts</em> de")])
X(62, "Geografia", "Industrialização", "<p>A indústria brasileira quase não entrou nas tecnologias da microeletrônica e depende de commodities e de setores fordistas antigos. Sem inovar, o país fica dependente das tecnologias e decisões de fora: <strong>subordinação aos fluxos globais</strong>. Alternativa <strong>D</strong>.</p><p>O texto não fala de cesta básica (A), estatização (B), consumo (C) ou de política de modernização (E).</p>",
  tags=["divisão internacional do trabalho", "indústria"], trocas=[("relacionados a commodities", "relacionados a <em>commodities</em>")])
X(63, "Geografia", "Conflitos territoriais", "<p>A mineração na Amazônia impede que extrativistas, quilombolas, ribeirinhos e indígenas mantenham suas dinâmicas territoriais e provoca o “esgarçamento das relações sociais” desses grupos. A marca é o <strong>rompimento de vínculos locais</strong>. Alternativa <strong>B</strong>.</p><p>Os grupos são empobrecidos, não enriquecidos (E); o problema não é falta de investimento (C).</p>",
  tags=["mineração", "povos tradicionais"])
X(64, "Filosofia", "Filosofia contemporânea", "<p>Para Deleuze e Guattari, maioria não é a quantidade maior, mas um padrão de dominação; mulheres e crianças são “minoritárias” por estarem fora desse padrão. A minoria decorre de <strong>relações de natureza arbitrária</strong>, de poder, e não numéricas. Alternativa <strong>C</strong>.</p><p>O critério não é biológico (E) nem estatal (B).</p>",
  tags=["Deleuze", "minorias"], trocas=[("Mil platôs.", "<em>Mil platôs</em>.")])
X(65, "Filosofia", "Marxismo", "<p>Engels diz aos trabalhadores que a classe média é sua “adversária”, com interesses “diametralmente opostos” aos deles, mesmo que finja simpatia. A orientação corresponde ao <strong>conceito de luta de classes</strong>. Alternativa <strong>A</strong>.</p><p>Mais-valia e fetichismo (B e E) são outros conceitos marxistas, não tratados no trecho.</p>",
  tags=["Engels", "luta de classes"])
X(66, "Sociologia", "Violência e desigualdade", "<p>Os presos são, em geral, homens jovens, negros, com ensino fundamental incompleto, acusados de crimes contra o patrimônio. O perfil aponta para exclusão social e falta de oportunidades; as políticas devem privilegiar a <strong>promoção da inclusão social</strong>. Alternativa <strong>B</strong>.</p><p>Reduzir a maioridade ou aumentar a reclusão (C e E) aumentaria o encarceramento, que já cresceu 74%.</p>",
  tags=["encarceramento", "políticas públicas"])
X(67, "História", "Idade Média", "<p>O texto diz que o impacto dos incêndios “prolongava-se para além da destruição material” e que as autoridades, ao reconstruir, convertiam a devastação em mudança. A catástrofe levava à <strong>reconfiguração dos espaços ocupados e das dinâmicas comunitárias</strong>. Alternativa <strong>E</strong>.</p><p>O texto não fala de regras sanitárias (A), descaso (B) ou mudanças nas crenças (C).</p>",
  tags=["cidades medievais", "catástrofes"], trocas=[("no Regnum Italicum.", "no <em>Regnum Italicum</em>.")])
X(68, "Sociologia", "Movimentos sociais", "<p>Os Guarani-Kaiowá divulgaram uma carta na internet, e milhares de pessoas aderiram à hashtag e ao sobrenome Guarani-Kaiowá nas redes. A estratégia conseguiu <strong>angariar o apoio de segmentos étnicos externos</strong> à causa indígena. Alternativa <strong>E</strong>.</p><p>A ação fortaleceu a militância e a identidade (contra A e B), sem objetivo comercial (C).</p>",
  tags=["Guarani-Kaiowá", "redes sociais"], trocas=[("divulgando a hashtag", "divulgando a <em>hashtag</em>")])
X(69, "História", "Era Vargas", "<p>Para construir um Estado forte e planejar a ocupação do território, o governo Vargas criou o IBGE e os conselhos de geografia, cartografia e estatística. A estratégia era <strong>obter conhecimento científico das diversidades regionais</strong> para orientar a ação do governo. Alternativa <strong>C</strong>.</p><p>O objetivo não era preservar a paisagem (A), controlar a população (B) ou conter migrações (D).</p>",
  tags=["Estado Novo", "IBGE"])
X(70, "Geografia", "Povos indígenas", "<p>Os Xavante sabiam como quebrar a dormência de cada semente (pelo fogo ou pela digestão dos animais) e, unindo esse saber ao dos cientistas da cidade, a área do Cerrado foi recuperada. O texto mostra a importância do <strong>saber tradicional para a conservação ambiental</strong>. Alternativa <strong>C</strong>.</p><p>Não se fala de logística, hortaliças, gado ou produção comercial (A, B, D e E).</p>",
  tags=["Xavante", "recuperação do Cerrado"])
X(71, "Geografia", "Geologia", "<p>O texto descreve rochas sendo destruídas, os fragmentos transportados por água, vento e gelo e depositados nas partes baixas, onde formam novos pacotes rochosos. É o <strong>ciclo sedimentar</strong>: intemperismo, erosão, transporte e deposição. Alternativa <strong>A</strong>.</p><p>Não há sismos (B), ação de seres vivos (C), lava (D) ou compactação apenas superficial (E).</p>",
  tags=["rochas sedimentares", "erosão"])
X(72, "Geografia", "Planejamento urbano", "<p>O texto diz que os planos diretores deveriam representar todos os segmentos da sociedade, mas as camadas menos favorecidas ficam de fora. Para incluí-las, é preciso fortalecer as formas de organização popular, como o <strong>fortalecimento das associações de bairro</strong>. Alternativa <strong>E</strong>.</p><p>As outras medidas favorecem grupos privados ou não envolvem participação (A a D).</p>",
  tags=["Estatuto da Cidade", "participação social"])
X(73, "História", "República Populista", "<p>O texto diz que, ao contrário do que esperavam os inimigos, o suicídio de Vargas não foi seguido do “silêncio que cerca a derrota”. A comoção levou multidões às ruas, que atacaram jornais e sedes de opositores: a repercussão imediata foi a <strong>reação popular</strong>. Alternativa <strong>A</strong>.</p><p>A comoção adiou o golpe que a oposição tramava (contra B e E).</p>",
  tags=["Getúlio Vargas", "suicídio de Vargas"])
X(74, "História", "Brasil Colônia", "<p>Dom João V bane ciganos para o Brasil e proíbe que usem e ensinem a seus filhos a própria língua, “de maneira que daqui por diante o seu uso desapareça”. A ordem queria <strong>suprimir formas divergentes de interação social</strong>, apagando a identidade cigana. Alternativa <strong>B</strong>.</p><p>O texto não fala de religião (A), economia (C), revoltas (D) ou arte (E).</p>",
  tags=["ciganos", "assimilação forçada"])
X(75, "História", "Brasil Colônia", "<p>Os jesuítas juntaram a prática médica europeia à terapêutica indígena com plantas nativas, e a maioria aprendeu a curar na prática diária. A medicina colonial se construiu pela <strong>conjugação de saberes empíricos</strong>. Alternativa <strong>E</strong>.</p><p>Não houve rejeição dos dogmas (B) nem imposição de um só saber (D); a tradição popular foi incorporada (C).</p>",
  tags=["jesuítas", "medicina colonial"])
X(76, "História", "Idade Média", "<p>Francisco de Assis falava às pessoas na língua do povo, com uma mensagem simples, numa Igreja rica e distante, de cultura em latim. A mesma crítica à riqueza da Igreja e às desigualdades aparecia nos <strong>movimentos heréticos</strong> da época, como valdenses e cátaros. Alternativa <strong>B</strong>.</p><p>Senhores feudais, cruzados, corporações e universidades (A, C, D e E) não tinham essa pauta.</p>",
  tags=["Francisco de Assis", "heresias"])
X(77, "História", "Independências", "<p>Carvalho atribui a unidade do Brasil à falta de universidades na colônia, que formou uma elite coesa em Coimbra; Rueda diz que as universidades hispano-americanas eram reacionárias e que a imprensa livre pesou mais na formação de regionalismos. Eles divergem sobre o <strong>papel desempenhado pelas instituições de ensino na criação das múltiplas identidades</strong>. Alternativa <strong>A</strong>.</p>",
  tags=["unidade territorial", "independências"])
X(78, "História", "Revolução Inglesa", "<p>O texto I vê a Revolução Inglesa como a luta do Parlamento pela liberdade política e religiosa, um só conflito entre liberdade e tirania. O texto II mostra camponeses contra cercamentos, tecelões contra a miséria e crentes à espera do reino de Cristo: a <strong>pluralidade das demandas sociais</strong>. Alternativa <strong>A</strong>.</p><p>O texto II mostra diversidade, não homogeneidade (B e C).</p>",
  tags=["Revolução Inglesa", "historiografia"])
X(79, "Geografia", "Indústria", "<p>A ideia de enclave descreve fábricas com poucas relações com o entorno: não usam fornecedores nem trabalhadores locais, mas influem na economia de fora. Um exemplo é a <strong>importação de mão de obra qualificada</strong>, em vez de empregar a população local. Alternativa <strong>E</strong>.</p><p>Vilas operárias, eventos, recuperação de áreas e saberes locais (A a D) criam vínculos com o entorno.</p>",
  tags=["enclave", "território"])
X(80, "Sociologia", "Pensamento social brasileiro", "<p>Costa Pinto descreve a sociedade em transição, em que o padrão tradicional em declínio convive com o novo em expansão, gerando ambivalência, adiamento de decisões e alternância entre inércia e convulsão. O desenvolvimento foi marcado por <strong>descompassos na construção de quadros institucionais modernos</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["Costa Pinto", "modernização"])
X(81, "História", "Educação", "<p>O Manifesto defende que a escola, aberta a todos os grupos sociais, forme a “hierarquia democrática” pela “hierarquia das capacidades”, contra a sociedade oligárquica. Liga o <strong>acesso à escola e a valorização do mérito</strong>. Alternativa <strong>B</strong>.</p><p>O trecho não fala de ensino técnico (A), gestores (C), pesquisa (D) ou salários (E).</p>",
  tags=["Escola Nova", "educação pública"])
X(82, "Filosofia", "Filosofia antiga", "<p>Sócrates pergunta a Mênon o que é a virtude antes de discutir se ela pode ser ensinada, examinando definições por perguntas e respostas. É o <strong>método dialético</strong> socrático. Alternativa <strong>B</strong>.</p><p>O diálogo não é carta (A), tragédia (C), física (D) ou suspensão do juízo cética (E).</p>",
  tags=["Sócrates", "dialética"], trocas=[("PLATÃO. Mênon.", "PLATÃO. <em>Mênon</em>.")])
X(83, "História", "África", "<p>Os pais Woyo davam aos filhos tampas de panela entalhadas com recados codificados sobre a boa relação conjugal e a escolha do cônjuge. Esses objetos funcionavam como uma <strong>pedagogia dos costumes sociais</strong>. Alternativa <strong>A</strong>.</p><p>Os artefatos valorizam o casamento (contra D) e não são imposição (B), nem desvalorização da juventude (C).</p>",
  tags=["Woyo", "escrita africana"])
X(84, "História", "Povos indígenas", "<p>O torém era brincado por parentes e vizinhos, no tempo do caju, com o mocororó, e chamava pessoas da região. A manifestação tinha a função de <strong>estimular a coesão social</strong> do grupo. Alternativa <strong>B</strong>.</p><p>O ritual não celebra a história oficial (A) nem trata de artesanato ou comércio (C e E).</p>",
  tags=["torém", "cultura indígena"])
X(85, "História", "Escravidão", "<p>O anúncio diz que o escravo José, quando fugiu da primeira vez, “esteve contratado como camarada em uma fazenda em Capivary”, apresentando-se como forro. A estratégia de resistência foi a <strong>criação de relações de trabalho</strong> como homem livre. Alternativa <strong>A</strong>.</p><p>O anúncio não fala de quilombo (B) nem de economia de subsistência (E).</p>",
  figs(("q85", "Anúncio de jornal “Escravo fugido”: “No dia 8 de Outubro do anno proximo passado fugio da fazenda do Bom Retiro, propriedade do dr. Francisco Antonio de Araújo, o escravo José, pardo claro, de 22 annos de idade, estatura regular, cheio de corpo, com a falta de um dente na frente do lado superior, cabellos avermelhados, orelha roxa, falla macia, e andar vagaroso. Intitula-se forro, e quando fugio a primeira vez esteve contratado como camarada em uma fazenda em Capivary. Quem o aprehender e entregar ao seu senhor no Amparo, ou o recolher a cadêa em qualquer parte será bem gratificado, e protesta-se com todo o rigor da lei contra quem o ac outar.”")),
  ["resistência escrava", "anúncios de fuga"])
X(86, "Filosofia", "Filosofia moderna", "<p>Na árvore de Descartes, a metafísica é a raiz, a física o tronco e as outras ciências os ramos: todas saem de um mesmo fundamento. A alegoria quer <strong>sustentar a unidade essencial do conhecimento</strong>. Alternativa <strong>A</strong>.</p><p>Descartes não refuta crenças (B), não defende o método experimental (D) nem a suspensão dos juízos (E) nesse trecho.</p>",
  tags=["Descartes", "árvore do saber"], trocas=[("Princípios da filosofia.", "<em>Princípios da filosofia</em>.")])
X(87, "Filosofia", "Filosofia contemporânea", "<p>O <em>amor fati</em> de Nietzsche é amar a vida como ela é, sem desejar nada além dela. A crítica é ao cristianismo, que <strong>consagra a realização humana ao campo transcendental</strong>, ao além, desvalorizando a vida terrena. Alternativa <strong>E</strong>.</p><p>A crítica não é sobre afeto (A), ciência (B), paganismo (C) ou filosofia antiga (D).</p>",
  tags=["Nietzsche", "amor fati"], trocas=[("é amor fati:", "é <em>amor fati</em>:")])
X(88, "História", "Idade Média", "<p>O texto pede para “castigar” e “curvar” a carne, sujeitando-a ao espírito, e contentar-se com pouco. O ascetismo medieval destaca a <strong>desvalorização da materialidade corpórea</strong>. Alternativa <strong>E</strong>.</p><p>O texto não fala de liturgia (A), razão (B), trabalho (C) ou alimentos impuros (D).</p>",
  tags=["ascetismo", "Imitação de Cristo"], trocas=[("Imitação de Cristo.", "<em>Imitação de Cristo</em>.")])
X(89, "Geografia", "Cartografia e astronomia", "<p>Em 21 de junho é o solstício de inverno no hemisfério sul: ao meio-dia, o Sol está a pino no Trópico de Câncer, ao norte de Brasília. A luz vem do norte, e a sombra do prédio aponta para o <strong>sul</strong>. Alternativa <strong>B</strong>.</p><p>Leste e oeste (C e D) seriam as sombras de manhã e à tarde, não ao meio-dia.</p>",
  figs(("q89", "Esquema “Movimento de translação da Terra”: a órbita em torno do Sol com a Terra em quatro posições — equinócio em 21 de março, solstício em 21 de dezembro, equinócio em 23 de setembro e solstício em 21 de junho —, com o eixo sempre inclinado.")),
  ["solstício", "sombra"], enun="[[fig:1]]" + fonte(T(89, 2)) + p(T(89, 3)))
X(90, "História", "Brasil Império", "<p>A gravura mostra escravizados carregando barris na cabeça, e o texto diz que os “tigres” levavam o lixo e os dejetos das casas, tarefa repugnante dada ao escravo de menor valor. A prática evidencia a <strong>reiteração das hierarquias sociais</strong>. Alternativa <strong>B</strong>.</p><p>O trabalho braçal era desprezado, não valorizado (A).</p>",
  figs(("q90", "Gravura de uma rua do Rio de Janeiro: homens escravizados carregam barris de madeira na cabeça, enquanto um homem de cartola e bengala passa ao lado.")),
  ["escravidão urbana", "tigres"],
  enun='<p class="apoio"><strong>TEXTO I</strong></p>[[fig:1]]' + fonte(T(90, 2).replace("Lixo: a limpeza", "<em>Lixo</em>: a limpeza")) + '<p class="apoio"><strong>TEXTO II</strong></p>'
       + ap(T(90, 4)) + fonte("KARASCH, M. C. <em>A vida dos escravos no Rio de Janeiro, 1808-1850</em>. Rio de Janeiro: Cia. das Letras, 2000.") + p(T(90, 6).split("2000. ", 1)[1]))

completar(Q, R)
