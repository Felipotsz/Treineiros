# Enem 2014, 1º dia, caderno azul: Ciências Humanas (questões 1 a 45; no 1º dia de 2014 vinham Humanas e Natureza).
# Texto legível (sem DECOD). Alternativas-imagem na Q16 (bens do patrimônio). Letra de canção (Q7) como imagem.
# Sem anuladas nesta área.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, enunciado_enem, paragrafos_enem

ID = "enem-2014-humanas"
META = {"id": ID, "banca": "Enem", "ano": 2014, "titulo": "Enem 2014: Ciências Humanas", "fonte": "Inep", "dataExame": "2014-11-08",
        "duracaoMinutos": 135, "area": "Ciências Humanas", "caderno": "azul", "dia": 1}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2014-dia1-azul")
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




X(1, "História", "Primeira República", "<p>Na charge, o índio estendido sobre o mapa tem a cabeça no Rio Grande e os pés no Amazonas, ligados por fios de telefone; a legenda diz que o Brasil “poderá esticar as canelas sem receio de não ser ouvido dos pés à cabeça”. A rede telefônica <strong>possibilitaria a integração das diferentes regiões do território nacional</strong>. Alternativa <strong>E</strong>.</p><p>O índio é uma alegoria do Brasil, e não um usuário real da telefonia (A e B).</p>",
  figs(("q01", "Charge “A rede telephonica”: um índio de cocar deitado, com o corpo sobre os nomes Rio Grande, Prata, Pará e Amazonas, fala ao telefone com fios que vão da cabeça aos pés. Legenda: “Em breve, já poderá o Brazil esticar as canellas sem receio de não ser ouvido dos pés á cabeça”.")),
  ["integração nacional", "charge"], enun="[[fig:1]]" + fonte("<em>Fon-Fon!</em>, ano IV, n. 36, 3 set. 1910. Disponível em: objdigital.bn.br. Acesso em: 4 abr. 2014.") + p(T(1, 1)))
X(2, "História", "Idade Média", "<p>A mulher dos versos não sabe ler, mas conhece o Paraíso e o Inferno pelas pinturas da igreja. Numa sociedade em que quase ninguém era alfabetizado, as imagens dos templos serviam para <strong>educar os fiéis através do olhar</strong>, transmitindo a doutrina. Alternativa <strong>C</strong>.</p><p>O objetivo era religioso e pedagógico, e não estético (A e E) ou de exaltar os artistas (D).</p>",
  tags=["arte medieval", "Igreja"],
  enun=ap("<br>".join([T(2, 0), T(2, 1), "Mostraram-me na igreja da minha terra", "Um Paraíso com harpas pintado", T(2, 3), T(2, 4)]))
  + fonte("VILLON, F. In: GOMBRICH, E. <em>História da arte</em>. Lisboa: LTC, 1999.") + p(T(2, 5)))
X(3, "Geografia", "Questões ambientais", "<p>A água dos rios foi desviada para irrigar algodão, e o Mar de Aral perdeu volume. Com a evaporação, os sais se concentraram no solo exposto e nas áreas irrigadas, que ficaram estéreis: é a <strong>salinização</strong>. Alternativa <strong>B</strong>.</p><p>Laterização (C) é o endurecimento do solo por óxidos de ferro e alumínio em climas úmidos, o que não tem relação com a irrigação excessiva.</p>",
  tags=["Mar de Aral", "irrigação"], trocas=[("Água no século XXI", "<em>Água no século XXI</em>")])
X(4, "Filosofia", "Filosofia moderna", "<p>Descartes duvida de tudo para encontrar algo que resista à dúvida. A certeza que sobra (“penso, logo existo”) nasce da própria dúvida e serve de base para o resto do saber. O caráter positivo é o <strong>surgimento do conhecimento inabalável</strong>. Alternativa <strong>D</strong>.</p><p>A dúvida é um método para fundar a ciência, e não para dissolvê-la (A) ou voltar aos juízos antigos (B).</p>",
  tags=["Descartes", "dúvida metódica"], trocas=[("Descartes: a metafísica da modernidade", "<em>Descartes: a metafísica da modernidade</em>")])
X(5, "Sociologia", "Trabalho e tecnologia", "<p>No cartum, robôs fazem todo o trabalho numa fábrica com uma placa de “Não há vagas”, enquanto um homem engraxa os sapatos de um robô. A tecnologia, em vez de libertar o homem, o deixa sem emprego e em posição servil: o pessimismo é com a <strong>ideia de progresso</strong>. Alternativa <strong>A</strong>.</p><p>Os equipamentos aparecem modernos, e não obsoletos (E).</p>",
  figs(("q05", "Cartum: numa fábrica cheia de máquinas, robôs trabalham; na porta, uma placa diz “Não há vagas”, e um homem agachado engraxa o pé de um robô.")),
  ["automação", "desemprego estrutural"])
X(6, "História", "Era Vargas", "<p>Com a crise de 1929, o café não tinha mercado nem crédito externo para financiar os estoques. O governo Vargas comprou e queimou café, e a crise da economia agroexportadora estimulou a produção interna de bens antes importados. A resposta do Estado foi o <strong>desenvolvimento de política industrial</strong>. Alternativa <strong>D</strong>.</p><p>A estrutura fundiária (B) não foi reformada; o latifúndio continuou.</p>",
  tags=["crise de 1929", "industrialização"], trocas=[("Formação econômica do Brasil", "<em>Formação econômica do Brasil</em>")])
X(7, "Geografia", "Espaço rural", "<p>O caboclo diz que trabalha na enxada, mas o que colhe “é dividido com quem não planta nada”, o dono da terra. Por isso pensa em migrar para o Rio. A queixa é contra a <strong>distribuição desigual da produção</strong>, típica da parceria e da meação. Alternativa <strong>A</strong>.</p><p>A canção diz que está chovendo no sertão: o problema não é a seca (D).</p>",
  figs(("q07", "Trecho da letra da canção “Sina de caboclo”, em que um trabalhador rural diz que não vai mais plantar para dividir a colheita com quem não planta e que pensa em ir para o Rio trabalhar na construção.")),
  ["meação", "concentração fundiária", "êxodo rural"], enun="[[fig:1]]" + fonte("VALE, J.; AQUINO, J. B. <em>Sina de caboclo</em>. São Paulo: Polygram, 1994 (fragmento).") + p(T(7, 2)))
X(8, "Sociologia", "Cultura", "<p>A cama do Oriente Próximo, o algodão da Índia, a cerâmica da China, o garfo da Itália: o dia comum do norte-americano é feito de elementos vindos de muitos povos. Os costumes resultam da <strong>fusão de elementos de tradições culturais diferentes</strong>. Alternativa <strong>D</strong>.</p><p>Chamar esses povos de “exóticos” (A) seria etnocêntrico, e o texto não fala de grupos privilegiados (E).</p>",
  tags=["difusão cultural", "Linton"], trocas=[("O homem: uma introdução à antropologia", "<em>O homem: uma introdução à antropologia</em>")])
X(9, "Geografia", "Globalização", "<p>O mapa mostra que há mais gente vivendo dentro do círculo sobre a Ásia do que fora dele, e o texto diz que a Índia atende ligações do mundo todo. Muita população significa muita oferta de trabalhadores e salários baixos: as empresas vão para lá pelo <strong>custo da mão de obra local</strong>. Alternativa <strong>E</strong>.</p><p>O teleatendimento não depende de posição geográfica (B), já que é feito por telefone.</p>",
  figs(("q09", "Mapa-múndi com um círculo sobre o Sul e o Leste da Ásia (Índia, China e vizinhos) e a frase “Há mais gente vivendo dentro desse círculo do que fora dele”.")),
  ["teleatendimento", "mão de obra barata"])
X(10, "Geografia", "Migrações", "<p>Daniel é desenhista industrial, fala inglês, e seu irmão é engenheiro-agrônomo; o desemprego entre jovens na Espanha passa de 52%, e a universidade chega a oferecer oficina para emigrar. A crise leva à <strong>exportação de mão de obra qualificada</strong>, a chamada fuga de cérebros. Alternativa <strong>C</strong>.</p><p>Os jovens saem para trabalhar, e não para estudar (E).</p>",
  tags=["crise europeia", "fuga de cérebros"], trocas=[("O Globo", "<em>O Globo</em>")])
X(11, "História", "Grécia Antiga", "<p>Escrever as leis torna-as conhecidas e fixas, “suscetíveis de serem aplicadas a todos da mesma maneira”. Isso é a <strong>isonomia, igualdade de tratamento aos cidadãos</strong> perante a lei. Alternativa <strong>A</strong>.</p><p>A igualdade de gênero (D) não existia na pólis, onde as mulheres não eram cidadãs.</p>",
  tags=["pólis", "isonomia"], trocas=[("As origens do pensamento grego", "<em>As origens do pensamento grego</em>")])
X(12, "Filosofia", "Bioética", "<p>A bioética discute os limites morais da pesquisa e da intervenção sobre a vida, como a clonagem humana: o que é possível fazer não é necessariamente o que se deve fazer. Ela se dedica a <strong>refletir sobre as relações entre o conhecimento da vida e os valores éticos do homem</strong>. Alternativa <strong>A</strong>.</p><p>A bioética não serve para legalizar (D) nem para justificar economicamente (E) as técnicas.</p>",
  tags=["clonagem", "ética"])
X(13, "Geografia", "Cartografia", "<p>A Terra gira em torno de si mesma de oeste para leste, então o Sol “nasce” antes nos lugares mais a leste. A França está a leste dos Estados Unidos e por isso vê o pôr do sol quando é meio-dia lá. A causa é o <strong>movimento em torno de seu próprio eixo</strong>, a rotação. Alternativa <strong>B</strong>.</p><p>A inclinação do eixo (E) explica as estações do ano, e não a diferença de horário.</p>",
  tags=["rotação", "fusos horários"], trocas=[("O Pequeno Príncipe", "<em>O Pequeno Príncipe</em>")])
X(14, "Filosofia", "Filosofia contemporânea", "<p>Para Habermas, uma norma é válida quando todos os afetados por ela chegam a um acordo num discurso prático, isto é, num diálogo racional. A validade vem da <strong>razão comunicativa, que requer um consenso</strong>. Alternativa <strong>B</strong>.</p><p>A norma não vale pela vontade de um indivíduo (A) nem pela força do poder político (E).</p>",
  tags=["Habermas", "ética do discurso"], trocas=[("Consciência moral e agir comunicativo", "<em>Consciência moral e agir comunicativo</em>")])
X(15, "História", "Brasil Colônia", "<p>Para catequizar povos de muitas línguas diferentes, os jesuítas aprenderam o tupi, escreveram gramáticas e difundiram uma língua franca, a língua geral (nheengatu), usada na catequese e no contato com os colonos. A aproximação foi mediada pela <strong>comunicação pela língua geral baseada no tupi</strong>. Alternativa <strong>E</strong>.</p><p>Os jesuítas combatiam os pajés (C) e reuniam os índios em aldeamentos, o que alterava a organização familiar e a moradia (B e D).</p>",
  tags=["jesuítas", "catequese"], trocas=[("A nação mercantilista", "<em>A nação mercantilista</em>")])
X(16, "Sociologia", "Cultura", "<p>O modo artesanal de fazer o queijo foi registrado como patrimônio <strong>imaterial</strong>: o que se protege é um saber, uma técnica. Entre as opções, o único bem dessa categoria é o <strong>ofício das paneleiras de Goiabeiras</strong>, técnica de fazer panelas de barro. Alternativa <strong>C</strong>.</p><p>Mosteiro, pintura, conjunto urbano e sítio arqueológico (A, B, D e E) são bens materiais.</p>",
  figs(("q16a", "Alternativa A: fachada de igreja branca com torre, árvores ao redor."), ("q16b", "Alternativa B: pintura de corpo esquartejado sobre um cadafalso de madeira."),
       ("q16c", "Alternativa C: mãos moldando uma panela de barro."), ("q16d", "Alternativa D: praça com calçamento de pedra, monumento ao centro e casarões coloniais."),
       ("q16e", "Alternativa E: praia de areia clara com pedras e morros ao fundo.")),
  ["patrimônio imaterial", "Iphan"],
  enun=tit(T(16, 0)) + ap(T(16, 1).replace(" Folha de S. Paulo, 15 maio 2008.", "")) + fonte("<em>Folha de S. Paulo</em>, 15 maio 2008.") + p(T(16, 2)),
  alts={"A": "[[fig:1]]Mosteiro de São Bento (RJ)", "B": "[[fig:2]]<em>Tiradentes esquartejado</em> (1893), de Pedro Américo", "C": "[[fig:3]]Ofício das paneleiras de Goiabeiras (ES)",
        "D": "[[fig:4]]Conjunto arquitetônico e urbanístico da cidade de Ouro Preto (MG)", "E": "[[fig:5]]Sítio arqueológico e paisagístico da Ilha do Campeche (SC)"})
X(17, "Sociologia", "Cidadania", "<p>Na charge, o rapaz lê a Constituição e diz que todo brasileiro tem direito à moradia, e a moça responde para ele ler a parte “de comida, saúde”. Os dois estão sentados na rua, sem casa. Moradia, alimentação e saúde são <strong>direitos sociais</strong>, previstos no papel e não garantidos na prática. Alternativa <strong>B</strong>.</p><p>Direitos civis (A) e políticos (E) são outros grupos de direitos.</p>",
  figs(("q17", "Charge: um homem e uma mulher com um bebê, sentados na calçada, ao lado de um cachorro. Ele lê um livro escrito “Constituição” e diz: “Todo brasileiro tem direito à moradia...”. Ela responde: “Agora lê aquele pedaço bonito que fala de comida, saúde...”.")),
  ["Constituição de 1988", "direitos sociais"])
X(18, "História", "Grandes Navegações", "<p>O relato diz que é “um milagre manifesto” escapar de todos os perigos das viagens e que seria “coisa pavorosa” enumerar os acidentes possíveis. No imaginário das navegações, o mar era cheio de perigos e monstros: o sentimento é de <strong>temor do desconhecido</strong>. Alternativa <strong>C</strong>.</p><p>O texto fala de medo, e não de gosto pela aventura (A).</p>",
  tags=["navegações", "medo"], trocas=[("História do medo no Ocidente", "<em>História do medo no Ocidente</em>")])
X(19, "Filosofia", "Filosofia antiga", "<p>Tucídides diz que quem não cuida das questões públicas é um inútil, e Aristóteles define o cidadão pelo direito de administrar a justiça e exercer funções públicas. Para os dois, a cidadania era definida pela <strong>participação política</strong>. Alternativa <strong>C</strong>.</p><p>Embora em Atenas fosse preciso ser filho de atenienses (D), os textos destacam o exercício das funções públicas.</p>",
  tags=["cidadania grega", "Aristóteles"], trocas=[("História da Guerra do Peloponeso", "<em>História da Guerra do Peloponeso</em>"), ("Política. Brasília", "<em>Política</em>. Brasília")])
X(20, "Geografia", "Questões ambientais", "<p>A Grande Muralha Verde é uma barreira de vegetação na borda sul do Saara, plantada para segurar o avanço do deserto sobre o Sahel. A consequência imediata é que ela <strong>evita a expansão da desertificação</strong>. Alternativa <strong>E</strong>.</p><p>Plantar vegetação aumenta, e não restringe, a diversidade biológica (C).</p>",
  tags=["Sahel", "desertificação"], trocas=[("Folha de S. Paulo", "<em>Folha de S. Paulo</em>")])
X(21, "História", "Era Vargas", "<p>O estatuto define a FNB como “união política e social da Gente Negra Nacional”, para afirmar e reivindicar direitos sociais e políticos. Ela chegou a se registrar como partido e foi fechada com os demais partidos no Estado Novo. Era uma organização <strong>política, engajada na luta por direitos sociais para a população negra</strong>. Alternativa <strong>A</strong>.</p><p>O estatuto fala da “comunhão brasileira”, e não de um movimento internacionalista (E).</p>",
  tags=["Frente Negra Brasileira", "movimento negro"])
X(22, "Geografia", "Urbanização", "<p>O preço alto dos terrenos centrais empurra os mais pobres para a periferia, longe de onde estão os empregos e os serviços. A consequência é a <strong>ampliação do tempo de deslocamento diário da população</strong>. Alternativa <strong>D</strong>.</p><p>A expulsão para a periferia favorece, e não contém, a ocupação de áreas sem infraestrutura (E).</p>",
  tags=["segregação socioespacial", "periferização"], trocas=[("O século XIX", "<em>O século XIX</em>")])
X(23, "História", "Imperialismo", "<p>Entre 1884 e 1914, as potências europeias dividiram a África e disputaram a Ásia. A corrida por colônias criou rivalidades, como as crises do Marrocos, que alimentaram as alianças e a guerra: o imperialismo <strong>acirrou as disputas territoriais</strong>. Alternativa <strong>B</strong>.</p><p>O nacionalismo e a xenofobia cresceram, e não foram contidos (E).</p>",
  tags=["neocolonialismo", "Primeira Guerra"], trocas=[("As origens do totalitarismo", "<em>As origens do totalitarismo</em>")])
X(24, "Filosofia", "Filosofia antiga", "<p>Epicuro separa os desejos naturais e necessários dos que nascem de “vã opinião” e recomenda abandonar estes quando trazem dor. A felicidade está no prazer moderado, na ausência de dor e de perturbação. O fim do homem é <strong>alcançar o prazer moderado e a felicidade</strong>. Alternativa <strong>A</strong>.</p><p>Aceitar o sofrimento com resignação (C) se parece mais com o estoicismo.</p>",
  tags=["Epicuro", "hedonismo"], trocas=[("Doutrinas principais", "<em>Doutrinas principais</em>"), ("Textos de filosofia", "<em>Textos de filosofia</em>")])
X(25, "Filosofia", "Filosofia antiga", "<p>Platão aponta para o alto porque, para ele, o conhecimento verdadeiro está no mundo das ideias, acima do mundo sensível. Chega-se a ele pela razão, por meio do diálogo: o homem descobre a <strong>realidade inteligível por meio do método dialético</strong>. Alternativa <strong>B</strong>.</p><p>Os sentidos (E) só dão acesso às aparências, segundo Platão.</p>",
  figs(("q25", "Detalhe do afresco “A Escola de Atenas”, de Rafael: no centro, Platão, de barba branca, aponta para cima, ao lado de Aristóteles, que estende a mão para a frente; outros filósofos ao redor.")),
  ["Platão", "mundo das ideias"], trocas=[("A Escola de Atenas", "<em>A Escola de Atenas</em>")])
X(26, "Geografia", "Urbanização", "<p>O mapa mostra que muita gente de Ribeirão das Neves, Santa Luzia, Contagem e outros municípios vizinhos vai trabalhar todo dia em Belo Horizonte e volta. São cidades cujas manchas urbanas se juntaram: o fluxo está associado à <strong>conurbação entre municípios contíguos</strong>. Alternativa <strong>D</strong>.</p><p>O fluxo vai para a capital, o que confirma, e não inverte, a hierarquia urbana (B).</p>",
  figs(("q26", "Mapa da Região Metropolitana de Belo Horizonte com o saldo de deslocamento diário para o trabalho. Setas grossas levam pessoas de Ribeirão das Neves, Santa Luzia, Contagem, Vespasiano, Ibirité e Sabará para Belo Horizonte. Os municípios do entorno têm saldo negativo, e Belo Horizonte, saldo positivo (19 169 a 293 119).")),
  ["movimento pendular", "região metropolitana"],
  enun="[[fig:1]]" + fonte(T(26, 1) + " BRASIL. IBGE. <em>Atlas do censo demográfico 2010</em> (adaptado).") + p(T(26, 2)))
X(27, "Geografia", "Urbanização", "<p>O texto diz que, com a urbanização, ruas foram alargadas e viadutos construídos, enquanto o bonde e o trem foram abandonados: “o transporte coletivo saiu dos trilhos”. Isso coincide com a chegada das montadoras ao Brasil nos anos 1950: há <strong>predominância do transporte rodoviário associado à penetração das multinacionais automobilísticas</strong>. Alternativa <strong>E</strong>.</p><p>O texto não fala do transporte alternativo das periferias (C).</p>",
  tags=["rodoviarismo", "indústria automobilística"],
  enun=ap(T(27, 0) + " " + T(27, 1)) + fonte(T(27, 2).replace("A caminho de Guaratiba", "<em>A caminho de Guaratiba</em>")) + p(T(27, 3)),
  alts={**D[27]["alternativas"], "E": "predominância do transporte rodoviário associado à penetração das multinacionais automobilísticas."})
X(28, "História", "Ditadura militar", "<p>A Comissão Nacional da Verdade, criada em 2011, examinou documentos e ouviu testemunhas sobre mortes, torturas e desaparecimentos cometidos por agentes do Estado. Seu objetivo foi <strong>esclarecer as circunstâncias de violações aos direitos humanos</strong>. Alternativa <strong>E</strong>.</p><p>A comissão não tinha poder de punir nem de anular a Lei da Anistia (A).</p>",
  tags=["Comissão da Verdade", "direitos humanos"],
  enun=ap(T(28, 0)) + fonte("Disponível em: www.jb.com.br. Acesso em: 2 mar. 2013 (adaptado).") + p("A notícia descreve uma iniciativa do Estado que resultou da ação de diversos movimentos sociais no Brasil diante de eventos ocorridos entre 1964 e 1988. O objetivo dessa iniciativa é"))
X(29, "Filosofia", "Revolução Científica", "<p>Para Galileu, a natureza está escrita em linguagem matemática, e só se entende quem conhece triângulos e círculos. Isso se opunha à física escolástica, de base aristotélica, que explicava a natureza por qualidades e finalidades. Era a <strong>oposição da nova física quantitativa aos pressupostos da filosofia escolástica</strong>. Alternativa <strong>C</strong>.</p><p>Galileu defendia a matemática, e não sua inadequação (E).</p>",
  tags=["Galileu", "método científico"], trocas=[("O ensaiador", "<em>O ensaiador</em>")])
X(30, "Sociologia", "Desigualdade racial", "<p>O parecer quer formar cidadãos “orgulhosos de seu pertencimento étnico-racial” e responder às demandas da população afrodescendente com ações afirmativas. A inclusão social é associada a <strong>práticas de valorização identitária</strong>. Alternativa <strong>A</strong>.</p><p>O texto trata de educação e conhecimento, e não de compensação econômica (B).</p>",
  tags=["ações afirmativas", "identidade"])
X(31, "História", "Memória e patrimônio", "<p>A praça já teve a estátua de Luís XV, foi palco das execuções da Revolução e recebeu o obelisco egípcio no século XIX. Cada época deixou ali suas marcas, e o espaço guarda essas camadas: manifesta o <strong>lugar da memória na história nacional</strong>. Alternativa <strong>A</strong>.</p><p>O obelisco foi um presente do Egito, e não um troféu de vitória sobre a África (D).</p>",
  tags=["lugares de memória", "Paris"])
X(32, "História", "Segundo Reinado", "<p>A Revolta do Vintém foi reprimida a tiros porque desafiava o governo; o ministério acabou caindo. A violência contra a multidão foi uma tentativa de <strong>conservar o exercício do poder</strong>. Alternativa <strong>D</strong>.</p><p>O Brasil era uma monarquia com voto restrito, não um regime democrático (E).</p>",
  tags=["Revolta do Vintém", "repressão"])
X(33, "Sociologia", "Política", "<p>O autor diz que o sistema político se mantém conservador porque convence a sociedade de que ela é conservadora, o que justifica a lentidão na redistribuição da renda. A legitimidade vem da <strong>sustentação ideológica das desigualdades existentes</strong>. Alternativa <strong>E</strong>.</p><p>O texto não fala de polarização partidária (B): diz que direita e esquerda partilham o mesmo argumento.</p>",
  tags=["conservadorismo", "ideologia"])
X(34, "Geografia", "Energia", "<p>O mapa marca pontos no Pará, em Rondônia e no Rio de Janeiro, onde estão Belo Monte, as usinas do Rio Madeira (Jirau e Santo Antônio) e Angra. São grandes obras de energia financiadas por bancos, com impacto sobre rios e florestas: <strong>ampliação da capacidade de geração de energia, com alteração do ecossistema local</strong>. Alternativa <strong>C</strong>.</p>",
  figs(("q34", "Mapa do Brasil com a divisão dos estados e três pontos pretos: um no Pará, um em Rondônia, perto da divisa com o Acre, e um no litoral do Rio de Janeiro.")),
  ["hidrelétricas", "impacto ambiental"])
X(35, "Geografia", "Clima", "<p>Convecção é a subida do ar quente e úmido, que forma nuvens e chuvas. Na Amazônia, ela é reforçada pelo encontro dos ventos alísios dos dois hemisférios na Zona de Convergência Intertropical. O mecanismo está associado à <strong>convergência de fluxos de ar</strong>. Alternativa <strong>E</strong>.</p><p>A Amazônia tem pequena amplitude térmica (B) e relevo baixo (D).</p>",
  tags=["Zona de Convergência Intertropical", "chuvas convectivas"], trocas=[("Acta Amazônica", "<em>Acta Amazônica</em>")])
X(36, "Geografia", "Geologia", "<p>A Dorsal Mesoatlântica é a cordilheira submarina no meio do Atlântico, onde as placas sul-americana e africana se afastam. Nos mapas, a América do Sul e a África ainda estão juntas no Jurássico e aparecem separadas no Cretáceo: a dorsal está associada à <strong>formação do Atlântico Sul no período Cretáceo</strong>. Alternativa <strong>D</strong>.</p><p>A Europa (C) se afastou da América do Norte, no Atlântico Norte.</p>",
  figs(("q36", "Cinco mapas-múndi da deriva continental: Permiano (225 milhões de anos, a Pangeia unida), Triássico (200 milhões, Laurásia e Gondwana), Jurássico (135 milhões, Gondwana começando a se fragmentar), Cretáceo (65 milhões, América do Sul e África separadas por uma fratura) e Quaternário (presente), com a legenda “Fraturas”.")),
  ["tectônica de placas", "dorsal oceânica"])
X(37, "Geografia", "Geopolítica", "<p>Os países em destaque são Brasil, Rússia, Índia, China e África do Sul: o grupo dos BRICS. São economias emergentes que fazem reuniões de cúpula para discutir comércio e finanças, como a criação de um banco próprio. Eles têm em comum <strong>instituírem fóruns de discussão sobre intercâmbio multilateral de economias emergentes</strong>. Alternativa <strong>C</strong>.</p><p>Os regimes políticos dos cinco são muito diferentes (A e B).</p>",
  figs(("q37", "Mapa-múndi em tons de cinza com Brasil, Rússia, Índia, China e África do Sul destacados em cinza-escuro.")),
  ["BRICS", "emergentes"])
X(38, "Geografia", "Recursos hídricos", "<p>O Aquífero Alter do Chão fica sob vários municípios do Pará e do Amazonas e teria mais água que o Guarani. Um aquífero compartilhado só é preservado se quem o usa combina regras de uso: é preciso <strong>introduzir a gestão participativa entre os municípios</strong>. Alternativa <strong>E</strong>.</p><p>Proibir poços (A) ou o uso residencial (B) seria impedir o uso, e não geri-lo de forma sustentável.</p>",
  figs(("q38", "Mapa do Norte do Brasil com a área do Aquífero Alter do Chão no Pará e no Amazonas e um quadro: a extensão do Alter do Chão é menor que a do Guarani, mas teria maior volume de água, superior a 86 mil km³; o Guarani tem cerca de 45 mil km³.")),
  ["aquíferos", "gestão de recursos hídricos"])
X(39, "História", "Primeira República", "<p>Campos Sales diz que “é dos estados que se governa a República” e que a política dos estados é a política nacional. É a política dos governadores: o presidente apoiava as oligarquias estaduais, que elegiam bancadas fiéis a ele. A estratégia era <strong>atrair o apoio das oligarquias regionais</strong>. Alternativa <strong>B</strong>.</p><p>Ele quer governar “por cima das multidões”, e não com adesão popular (A).</p>",
  tags=["política dos governadores", "Campos Sales"], trocas=[("Os Bestializados", "<em>Os Bestializados</em>")])
X(40, "História", "Primeira República", "<p>A Noroeste foi uma ferrovia de penetração, feita para abrir novas áreas para a agricultura e o povoamento, e não para servir a zonas de café já produtoras. O objetivo era a <strong>valorização de regiões de baixa densidade demográfica</strong>. Alternativa <strong>D</strong>.</p><p>Articular polos produtores para exportação (A) era o padrão anterior, ditado pelo café.</p>",
  tags=["ferrovias", "ocupação do território"])
X(41, "História", "Meios de comunicação", "<p>De Gaulle falou pelo rádio aos soldados contra o golpe, e as fitas de Khomeini espalharam a revolução no Irã. Nos dois casos, os meios de comunicação levaram a mensagem de um líder às pessoas e as fizeram agir: <strong>promoção da mobilização política</strong>. Alternativa <strong>B</strong>.</p><p>Os soldados franceses obedeceram ao presidente, e não se insubordinaram contra ele (C).</p>",
  tags=["rádio", "Revolução Iraniana"], trocas=[("Era dos extremos", "<em>Era dos extremos</em>")])
X(42, "História", "Ditadura militar", "<p>O texto I justifica o golpe pela necessidade de “manutenção da democracia”, em nome da ordem e da segurança: são <strong>razões de Estado</strong>. O texto II diz que nada compensa a perda das liberdades, ou seja, defende a <strong>soberania popular</strong>. Alternativa <strong>A</strong>.</p><p>Nenhum dos textos menciona religião ou moral (B e D).</p>",
  tags=["golpe de 1964", "imprensa"])
X(43, "História", "Brasil Império", "<p>Com a vinda da corte, o Rio virou sede do governo português, com ministérios, tribunais e a abertura dos portos. O Brasil deixou de ser uma colônia comum: os fatos <strong>enfraqueceram o pacto de dominação metropolitana</strong>. Alternativa <strong>B</strong>.</p><p>Os constitucionalistas do Porto (D) queriam a volta do rei e a recolonização, e se opuseram à autonomia do Brasil.</p>",
  tags=["vinda da família real", "independência"], trocas=[("História da vida privada no Brasil", "<em>História da vida privada no Brasil</em>")])
X(44, "História", "Segundo Reinado", "<p>Tavares Bastos defende que cada povoação e cada província tenham suas leis, respeitando suas diferenças: “administrar-se-ia de perto, governar-se-ia de longe”. É a defesa da autonomia provincial contra a centralização do Império, ou seja, de um <strong>modelo territorial federalista</strong>. Alternativa <strong>C</strong>.</p><p>O texto trata da organização do território, e não da educação (B).</p>",
  tags=["federalismo", "centralização"], trocas=[("A província (1870)", "<em>A província</em> (1870)")])
X(45, "História", "Segundo Reinado", "<p>O soldado negro volta da Guerra do Paraguai, onde lutou pela pátria e “libertou um povo da escravidão”, e encontra a mãe amarrada a um tronco. Ele ganhou a liberdade pelo serviço militar, mas sua família continuava escravizada. A contradição está na <strong>negação da cidadania aos familiares cativos</strong>. Alternativa <strong>A</strong>.</p>",
  figs(("q45", "Charge: um soldado com uniforme da Guerra do Paraguai, condecorado, leva a mão à testa espantado; ao fundo, uma mulher negra amarrada a um tronco é açoitada.")),
  ["Guerra do Paraguai", "escravidão"],
  enun="[[fig:1]]" + tit(T(45, 1)) + ap(T(45, 2)) + fonte(T(45, 3).replace("A vida fluminense", "<em>A vida fluminense</em>").replace("Uma história do Brasil através da caricatura (1840-2001)", "<em>Uma história do Brasil através da caricatura (1840-2001)</em>")) + p(T(45, 4)))

completar(Q, R)
