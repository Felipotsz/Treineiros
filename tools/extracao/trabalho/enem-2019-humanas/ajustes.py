# Enem 2019, 1º dia, caderno azul: Ciências Humanas (questões 46 a 90; no site, 1 a 45).
# Texto legível (sem DECOD). Letra de Marisa Monte (Q61) e poema de Orides Fontela (Q78) como imagem.
# Artigos da Constituição de 1824 (Q72) em lista. Sem anuladas nesta área.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, enunciado_enem, paragrafos_enem

ID = "enem-2019-humanas"
META = {"id": ID, "banca": "Enem", "ano": 2019, "titulo": "Enem 2019: Ciências Humanas", "fonte": "Inep", "dataExame": "2019-11-03",
        "duracaoMinutos": 135, "area": "Ciências Humanas", "caderno": "azul", "dia": 1}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2019-dia1-azul")
Q = {}
P = lambda n: paragrafos_enem(D[n])
T = lambda n, i: P(n)[i][1]
p = lambda *xs: "".join(f"<p>{x}</p>" for x in xs)
ap = lambda *xs: "".join(f'<p class="apoio">{x}</p>' for x in xs)
fonte = lambda x: f'<p class="fonte">{x}</p>'
LIMPA = lambda s: re.sub(r"fi ([a-zà-ú])", r"fi\1", re.sub(r"fl ([a-zà-ú])", r"fl\1", re.sub(r"(\w)- -(\w)", r"\1-\2", s)))


def figs(*pares):
    return [{"arquivo": a, "alt": t} for a, t in pares]


def X(n, materia, assunto, expl, imagens=(), tags=(), enun=None, trocas=(), alts=None):
    e = LIMPA(enun or enunciado_enem(D[n]))
    for a, b in trocas:
        assert a in e, a; e = e.replace(a, b)
    al = {k: LIMPA(v) for k, v in (alts or D[n]["alternativas"]).items()}
    Q[n - 45] = {"materia": materia, "assunto": assunto, "area": "Ciências Humanas", "tags": list(tags), "numeroOriginal": n,
                 "enunciado": e, "alternativas": al, "imagens": list(imagens), "explicacao": expl}


X(46, "Geografia", "Geologia", "<p>O Antropoceno é a ideia de que a ação humana passou a alterar o planeta em escala geológica. O ser humano não muda o magmatismo, o vulcanismo ou as placas, mas interfere fortemente nos processos da superfície (erosão, sedimentação, clima, ciclos da água): os processos <strong>exógenos</strong>. Alternativa <strong>B</strong>.</p><p>Erupções, tectonismo, magmatismo e metamorfismo (A, C, D e E) são processos internos, endógenos.</p>",
  tags=["Antropoceno", "agentes exógenos"], trocas=[("Antropoceno: e se formos", "<em>Antropoceno</em>: e se formos")])
X(47, "Geografia", "Cartografia", "<p>O esquema mostra o sensoriamento remoto: o satélite capta a energia solar refletida por florestas, rios, pastagens, rodovias e cidades. Cada superfície reflete uma parcela diferente da radiação, e é essa diferença que forma a imagem: depende da variação do <strong>albedo dos corpos físicos</strong>. Alternativa <strong>A</strong>.</p><p>O satélite não mede o lençol freático, o magnetismo ou os minérios diretamente (B, C e D).</p>",
  figs(("q47", "Esquema do sensoriamento remoto: o Sol envia energia solar incidente sobre floresta, rio, pastagens, rodovia e cidade; cada superfície reflete parte dessa energia, que é captada por um satélite na atmosfera.")),
  ["sensoriamento remoto", "albedo"])
X(48, "Filosofia", "Filosofia moderna", "<p>Humboldt via os habitantes como “mendigos sentados sobre um saco de ouro”: a natureza aparece como riqueza a ser explorada, um objeto separado do ser humano e dominado por ele. Essa separação entre sujeito pensante e natureza-objeto é marca do <strong>racionalismo cartesiano</strong>, que propunha tornar o homem “senhor e possuidor da natureza”. Alternativa <strong>C</strong>.</p><p>Relativismo e pluralismo (A e D) aceitariam outras formas de relação com a natureza, como o bem viver que o autor defende.</p>",
  tags=["Descartes", "dominação da natureza"], trocas=[("Bem viver: uma", "<em>Bem viver</em>: uma")])
X(49, "Geografia", "Agropecuária", "<p>As abelhas morrem por causa dos agrotóxicos, e sem elas a polinização das lavouras fica ameaçada. Uma solução que mantém a produtividade sem o veneno é a <strong>utilização da técnica de controle biológico</strong>, que combate as pragas com seus inimigos naturais. Alternativa <strong>C</strong>.</p><p>Monocultura e adubação química (B e D) não resolvem o uso de inseticidas; mata ciliar e drenagem (A e E) não tratam do problema.</p>",
  tags=["agrotóxicos", "polinização"])
X(50, "Filosofia", "Ética", "<p>Para Derrida, a hospitalidade pura acolhe quem chega antes de lhe impor condições e se dirige a ele como alguém singular. No contexto das migrações, isso exige acolher o outro em sua diferença: a <strong>incorporação da alteridade</strong>. Alternativa <strong>C</strong>.</p><p>Exigir documentos e origem (E) é justamente o que a hospitalidade pura dispensa; ela não anula a diferença (A).</p>",
  tags=["Derrida", "hospitalidade"])
X(51, "Filosofia", "Filosofia do direito", "<p>Abbagnano define o Direito como “a técnica da coexistência humana”, um conjunto de regras sobre o comportamento recíproco dos homens. O sentido fundamental do Direito é a <strong>regulação do convívio social</strong>. Alternativa <strong>B</strong>.</p><p>Aplicar códigos (A) é um meio; o texto não fala de decisões políticas, conflitos econômicos ou autoridade (C, D e E).</p>",
  tags=["Direito", "normas sociais"])
X(52, "História", "Brasil Colônia", "<p>A farinha de mandioca, de origem indígena, foi aperfeiçoada na Colônia e, pelo comércio atlântico, chegou aos mercados africanos. O produto mostra a <strong>difusão de hábitos alimentares</strong> entre as margens do Atlântico. Alternativa <strong>A</strong>.</p><p>O texto não fala de rituais, festas, guerras ou oferendas (B, D e E), e o saber indígena foi apropriado, não ampliado entre os nativos (C).</p>",
  tags=["mandioca", "comércio atlântico"])
X(53, "Geografia", "Geopolítica", "<p>Brasil, Alemanha, Índia e Japão são potências de peso em suas regiões (América do Sul, Europa e Ásia) e pedem vagas permanentes num Conselho que, segundo eles, não reflete o século XXI. A pretensão se apoia no <strong>protagonismo em escala regional</strong>. Alternativa <strong>B</strong>.</p><p>Japão e Alemanha não são grandes em território (A), e Brasil, Alemanha e Japão não têm armas nucleares (D).</p>",
  tags=["ONU", "Conselho de Segurança"])
X(54, "História", "Revolução Industrial", "<p>A revolta do Capitão Swing (1830) foi feita por trabalhadores rurais ingleses que queimavam celeiros e máquinas. Ela reagia ao empobrecimento causado pelos cercamentos, que transformaram terras de uso coletivo em propriedade privada: a <strong>expropriação das terras comunais</strong>. Alternativa <strong>B</strong>.</p><p>Houve ampliação, e não restrição, da propriedade privada (A); não houve estatização (C).</p>",
  tags=["cercamentos", "revoltas rurais"], trocas=[("ao The Times", "ao <em>The Times</em>")])
X(55, "História", "Independência do Brasil", "<p>Maria Quitéria só conseguiu lutar porque se disfarçou de homem: cortou os cabelos, amarrou os seios e usou um nome masculino. O caso evidencia a <strong>rigidez hierárquica da estrutura social</strong>, que proibia mulheres nos batalhões e reservava papéis diferentes a homens e mulheres. Alternativa <strong>A</strong>.</p><p>Não houve abertura às mulheres no exército (B): ela precisou esconder quem era.</p>",
  tags=["Maria Quitéria", "papéis de gênero"])
X(56, "Geografia", "Indústria", "<p>As transnacionais espalharam fábricas pelo mundo, mas o ganho dos países em desenvolvimento foi desigual: concentrou-se no Leste Asiático. A dispersão das plantas industriais convive com a <strong>concentração econômica</strong> nas grandes empresas e em poucos países. Alternativa <strong>D</strong>.</p><p>O texto não fala em autonomia tecnológica (A) nem em divisão de lucros (E).</p>",
  tags=["globalização", "transnacionais"])
X(57, "Geografia", "Climatologia", "<p>Perto do Trópico de Capricórnio há desertos no Chile, na Namíbia e na Austrália, mas não no Brasil. Aqui, a umidade que vem da Amazônia pelos ventos (os “rios voadores”) e a do Atlântico levam chuva ao Centro-Sul: há <strong>influência de umidade das áreas florestais</strong>. Alternativa <strong>C</strong>.</p><p>Altas pressões e correntes frias (B e D) favorecem os desertos, não os impedem.</p>",
  figs(("q57", "Mapa-múndi “Regiões áridas e semiáridas do mundo”, com as linhas de 30° N, Trópico de Câncer, Equador, Trópico de Capricórnio e 30° S: as áreas áridas aparecem perto dos trópicos (Saara, Arábia, Austrália, Namíbia, deserto do Atacama), mas não no Brasil.")),
  ["desertos", "rios voadores"], trocas=[("História ecológica da Terra", "<em>História ecológica da Terra</em>")])
X(58, "Filosofia", "Filosofia medieval", "<p>Agostinho diz que Deus deu ao homem a vontade livre para agir corretamente; quem a usa para pecar merece a punição, que seria injusta se não houvesse livre escolha. A punição se funda no mau uso da liberdade, isto é, na <strong>insuficiência da autonomia moral</strong> de quem escolhe o pecado. Alternativa <strong>B</strong>.</p><p>O texto não fala de celibato, desapego, sacrifício ou Velho Testamento (A, C, D e E).</p>",
  tags=["Agostinho", "livre-arbítrio"])
X(59, "Geografia", "Geologia", "<p>A imagem mostra os países atuais desenhados sobre a Pangeia, o supercontinente que existiu há cerca de 250 milhões de anos. Essa divisão política só seria possível se os continentes não tivessem se separado, ou seja, com a estabilidade da <strong>estrutura geológica</strong> (sem deriva das placas). Alternativa <strong>C</strong>.</p><p>Chuvas, erosão e pressão (A, B, D e E) não mudam a posição dos continentes.</p>",
  figs(("q59", "Globo com o supercontinente Pangeia, os continentes juntos, mas com as fronteiras dos países atuais desenhadas sobre ele.")),
  ["Pangeia", "deriva continental"])
X(60, "História", "Idade Média", "<p>Le Goff descreve a cidade medieval como lugar de abundância, artesanato, comércio e dinheiro. Ao mesmo tempo, ela continuava protegida por muralhas, portas e torres: a ampliação das atividades urbanas se associa à <strong>permanência dos elementos arquitetônicos de proteção</strong>. Alternativa <strong>E</strong>.</p><p>As corporações de ofício estavam em pleno vigor (contra D), e a cidade dependia dos campos para se alimentar (C).</p>",
  tags=["cidade medieval", "renascimento comercial"], trocas=[("Dicionário temático do Ocidente Medieval", "<em>Dicionário temático do Ocidente Medieval</em>")])
X(61, "Geografia", "Meio ambiente", "<p>A canção do texto I trata o rio com reverência, como fonte de consolo, e pede que se faça dele uma “oração”: a natureza é idealizada. O texto II mostra o ecoturismo transformando a natureza em espetáculo para consumo dos turistas: <strong>idealização e mercantilização</strong>. Alternativa <strong>E</strong>.</p><p>O texto I não explora a natureza (A), e o II não fala de degradação ou profanação (B e C).</p>",
  figs(("q61", "Trecho da letra “O rio”, de Marisa Monte e parceiros, como aparece na prova: alguém pede ao filho que ouça o barulho do rio e deixe o som embalá-lo, lembra que as folhas que caem nele chegam ao mar e diz que, quando faltar alegria, ele deve fazer do rio sua oração.")),
  ["natureza", "ecoturismo"],
  enun='<p class="apoio"><strong>TEXTO I</strong></p>[[fig:1]]' + fonte(T(61, 2).replace("Infinito particular", "<em>Infinito particular</em>")) + '<p class="apoio"><strong>TEXTO II</strong></p>' + ap(T(61, 4)) + fonte(T(61, 5)) + p(T(61, 6)))
X(62, "Sociologia", "Religião", "<p>Os adeptos das religiões de matriz africana são agredidos na rua e no transporte público, sobretudo quando usam suas vestes religiosas. Numa sociedade laica e democrática o Estado garante que todos pratiquem sua fé; essas agressões <strong>restringem a liberdade de credo</strong>. Alternativa <strong>E</strong>.</p><p>As agressões vão contra a diversidade (A e B), não a favor dela.</p>",
  tags=["intolerância religiosa", "laicidade"])
X(63, "História", "Mercantilismo e liberalismo", "<p>O texto I descreve o mercantilismo: centralização, protecionismo e fortalecimento do Estado, com monopólios concedidos pelo rei. Adam Smith, no texto II, critica as práticas exclusivistas que atrapalham a “lei natural” da economia. A oposição é entre a <strong>defesa dos monopólios régios — apoio à livre concorrência</strong>. Alternativa <strong>B</strong>.</p><p>O mercantilismo valorizava o metalismo (contra D) e criava tarifas, não as eliminava (E).</p>",
  tags=["Adam Smith", "mercantilismo"], trocas=[("O mercantilismo. Lisboa", "<em>O mercantilismo</em>. Lisboa"), ("A riqueza das Nações", "<em>A riqueza das Nações</em>")],
  alts={**D[63]["alternativas"], "A": "valorização do pacto colonial — combate à livre-iniciativa."})
X(64, "Filosofia", "Filosofia da ciência", "<p>A lenda costuma apresentar a descoberta como um estalo, mas no texto Newton observa a maçã, descarta explicações (pássaro, esquilo) e formula uma suposição: alguma força externa a fez cair. Essa é a dimensão da ciência moderna que o texto destaca: a <strong>proposição de hipóteses</strong>. Alternativa <strong>C</strong>.</p><p>A observação é usada, não negada (B), e não há falsificação ou universalização (A e E) no trecho.</p>",
  tags=["método científico", "Newton"])
X(65, "Filosofia", "Filosofia política", "<p>Para Maquiavel, o que vale para a vida privada não serve ao governante: o chefe de Estado pode mentir se isso for melhor para o bem comum. É a distinção entre a moral ideal (o que se deve fazer) e a moral efetiva da política (o que se precisa fazer): <strong>idealidade e efetividade da moral</strong>. Alternativa <strong>A</strong>.</p><p>O texto não trata de legalidade, liberdade ou verdade como conhecimento (B, C, D e E).</p>",
  tags=["Maquiavel", "realismo político"])
X(66, "Sociologia", "Políticas públicas", "<p>O SUS foi criado como “uma política para todos”, que protege os cidadãos e reduz desigualdades. As duas características são o acesso para todos e a busca de igualdade: <strong>universalismo e igualitarismo</strong>. Alternativa <strong>C</strong>.</p><p>O SUS é um direito, não filantropia (A), e não se baseia em mérito (B).</p>",
  tags=["SUS", "direitos sociais"])
X(67, "Filosofia", "Filosofia moderna", "<p>Descartes contempla Deus pela razão, e Rachels pergunta se há boa razão para acreditar num criador, dizendo que a crença em Deus não é “apenas” fé. Os dois textos mostram a modernidade examinando as questões a partir de um modelo <strong>centrado na razão humana</strong>. Alternativa <strong>A</strong>.</p><p>O modelo moderno rejeita a explicação mitológica (B), e os textos não tratam de contrato social (D).</p>",
  tags=["racionalismo", "Descartes"], trocas=[("Meditações. São Paulo", "<em>Meditações</em>. São Paulo"), ("Problemas da filosofia", "<em>Problemas da filosofia</em>")])
X(68, "Geografia", "Espaço rural", "<p>Os quilombolas de Mumbuca abastecem a cidade com a feira, e os de Campinho vendem artesanato e comida aos turistas. As estratégias visam garantir a <strong>inserção econômica regional</strong> dessas comunidades. Alternativa <strong>C</strong>.</p><p>O texto não fala em dívidas, tarifas ou benefícios do Estado (A, D e E), nem em reserva de mercado (B).</p>",
  tags=["quilombolas", "economia local"])
X(69, "Geografia", "Amazônia", "<p>A vila surgiu da invasão de terras por camponeses, madeireiros, pecuaristas e grileiros, sem planejamento do Estado, avançando sobre reservas e terras indígenas. É a dinâmica da <strong>expansão de frentes pioneiras</strong>, típica da fronteira agrícola amazônica. Alternativa <strong>E</strong>.</p><p>Não foi colonização dirigida nem reforma agrária (B e C), que dependeriam do governo.</p>",
  tags=["fronteira agrícola", "Rondônia"])
X(70, "Sociologia", "Cultura e mídia", "<p>A mídia associa o corpo magro à saúde e o corpo gordo ao descontrole e à doença. Os autores contestam essa ideia citando Marilyn Wann: é possível ser gordo e saudável, e muitos gordos adoecem pelo estresse e pela opressão, não pela gordura. A crítica é a <strong>contestação dos estereótipos consolidados</strong>. Alternativa <strong>E</strong>.</p><p>Reiterar discursos hegemônicos (D) é o que a mídia faz, e o texto critica, não a crítica em si.</p>",
  tags=["padrão de beleza", "mídia"])
X(71, "Geografia", "Trabalho", "<p>Harvey mostra que cada crise leva o capitalismo a se reorganizar num nível “novo e superior”, com nova tecnologia e novos modos de produzir. Para entrar nesse processo, o trabalhador precisa dominar as novas exigências: a condição é a <strong>qualificação profissional</strong>. Alternativa <strong>D</strong>.</p><p>Sindicato, voto e migração (A, B e C) não são exigências do novo processo produtivo.</p>",
  tags=["reestruturação produtiva", "Harvey"])
X(72, "História", "Brasil Império", "<p>A Constituição de 1824 estabelecia eleições em dois graus: os cidadãos escolhiam eleitores, que depois escolhiam os deputados (voto indireto). E excluía quem não tivesse renda mínima anual de cem mil réis (voto censitário). O sistema é marcado pelo <strong>voto indireto e perfil censitário</strong>. Alternativa <strong>B</strong>.</p><p>O voto não era secreto (A), e a exclusão de pobres e dependentes contraria a ideia de abertura (C).</p>",
  tags=["Constituição de 1824", "voto censitário"],
  enun=ap(T(72, 0), T(72, 1))
       + '<ol type="I">' + "".join(f"<li>{x.strip()}</li>" for x in re.split(r"\s*\b(?:I|II|III|IV|V)\.\s+", T(72, 2).split(" BRASIL.")[0]) if x.strip()) + "</ol>"
       + fonte("BRASIL. <em>Constituição de 1824</em>. Disponível em: www.planalto.gov.br. Acesso em: 4 abr. 2015 (adaptado).") + p(T(72, 4)))
X(73, "História", "Idade Média", "<p>A Igreja aproveitou as festas pagãs do solstício de verão europeu, com suas fogueiras, e as transformou nas “fogueiras de São João”, associando-as à doutrina cristã. Para se fortalecer, fez a <strong>apropriação de cerimônias seculares</strong>, dando-lhes sentido religioso. Alternativa <strong>C</strong>.</p><p>Não houve ecumenismo (A), e as festas não eram de origem bíblica ou apostólica (B e D).</p>",
  tags=["sincretismo", "festas juninas"])
X(74, "Filosofia", "Filosofia contemporânea", "<p>Foucault nega um sujeito universal e soberano: o sujeito se constitui pelas práticas de sujeição ou de liberdade, a partir das regras e estilos do meio cultural. A subjetivação é <strong>contingencial, processada em interações sociais</strong>. Alternativa <strong>C</strong>.</p><p>Ele rejeita uma essência fixa (E) e um fundamento transcendental (D).</p>",
  tags=["Foucault", "subjetivação"])
X(75, "Geografia", "Meio ambiente", "<p>Bacon propõe arrancar os segredos da natureza “sob a tortura dos experimentos”, e Guimarães mostra o ser humano desintegrado do todo, agindo sem equilíbrio sobre o ambiente. Os dois textos mostram a natureza tratada como coisa a ser dominada: a <strong>objetificação do espaço físico</strong>. Alternativa <strong>A</strong>.</p><p>A visão holística (E) é o que falta segundo o texto II, não o que ele descreve.</p>",
  tags=["Bacon", "relação sociedade-natureza"], trocas=[("Novum Organum", "<em>Novum Organum</em>")])
X(76, "Filosofia", "Filosofia política", "<p>Arendt mostra que os campos de concentração tornaram os detentos “irreais”, como se sua vida estivesse fora deste mundo, o que levou à aceitação do extermínio. A crítica é à naturalização da <strong>segregação humana, que fundamenta os projetos biopolíticos</strong> de controle e eliminação de grupos. Alternativa <strong>D</strong>.</p><p>O texto trata do totalitarismo, não do nacionalismo em geral (A) ou da religião (C).</p>",
  tags=["Hannah Arendt", "totalitarismo"], trocas=[("Origens do totalitarismo", "<em>Origens do totalitarismo</em>")])
X(77, "Geografia", "Espaço urbano", "<p>A foto mostra grafites no Beco do Batman, em São Paulo, e o texto fala de uma arte “criada nas ruas e para as ruas”, fora das instituições tradicionais. O movimento é de <strong>apropriação dos espaços públicos</strong> pela arte urbana. Alternativa <strong>B</strong>.</p><p>O grafite rompe com os formalismos (contra D) e não restaura patrimônios (E).</p>",
  figs(("q77", "Foto de um muro coberto de grafites coloridos numa rua de pedras; na mureta do primeiro plano aparece a palavra “veracidade” pintada.")),
  ["grafite", "arte urbana"])
X(78, "Filosofia", "Filosofia moderna", "<p>Kant admira “o céu estrelado sobre mim e a lei moral em mim”: a lei moral é interior (vem da razão) e o mundo físico é exterior, conhecido como fenômeno. Orides Fontela inverte: “a dura lei cobrindo-me e o estrelado céu dentro de mim”. A poeta inverte a <strong>interioridade da norma e fenomenalidade do mundo</strong>. Alternativa <strong>E</strong>.</p><p>O jogo do poema é trocar o “sobre mim” pelo “em mim”, não discutir liberdade ou boa vontade (A e C).</p>",
  figs(("q78", "Poema “Kant (relido)”, de Orides Fontela, como aparece na prova: em dois versos curtos, inverte a frase de Kant, pondo a lei moral do lado de fora, sobre a poeta, e o céu estrelado dentro dela.")),
  ["Kant", "lei moral"],
  enun='<p class="apoio"><strong>TEXTO I</strong></p>' + ap(T(78, 1)) + fonte(T(78, 2).replace("Crítica da razão prática", "<em>Crítica da razão prática</em>"))
       + '<p class="apoio"><strong>TEXTO II</strong></p>[[fig:1]]' + fonte(T(78, 5).replace("Poesia completa", "<em>Poesia completa</em>")) + p(T(78, 6)))
X(79, "História", "Grécia antiga", "<p>Nas cidades-estado clássicas, a cidadania plena estava ligada à posse de terra no território da cidade: poucos proprietários nas oligarquias, mais nas democracias. O critério é o <strong>controle da terra</strong>. Alternativa <strong>A</strong>.</p><p>Mulheres não participavam (contra C), e os cidadãos eram justamente os que combatiam (contra D).</p>",
  tags=["cidade-estado", "cidadania antiga"])
X(80, "História", "Brasil República", "<p>Na Revolta da Vacina (1904), a população do Rio reagiu à vacinação obrigatória imposta com invasão de casas e sem explicação. O povo não queria governar, mas defendia direitos que via acima do Estado. A revolta questionava o <strong>arbítrio governamental</strong>. Alternativa <strong>D</strong>.</p><p>O texto diz que não se reivindicava participação política (contra B e E).</p>",
  tags=["Revolta da Vacina", "Primeira República"], trocas=[("Os bestializados", "<em>Os bestializados</em>")])
X(81, "História", "Brasil Colônia", "<p>No século XVIII, o centro da economia colonial passou para as minas de ouro e diamantes de Minas Gerais, e o Rio de Janeiro virou o porto de entrada de escravizados e de saída do ouro. A mudança está ligada à <strong>extração de metais preciosos</strong>. Alternativa <strong>B</strong>.</p><p>Drogas do sertão, pecuária, madeira e tabaco (A, C, D e E) não explicam a guinada para o Rio.</p>",
  tags=["mineração", "tráfico negreiro"])
X(82, "História", "Brasil República", "<p>O texto convoca “todas as forças vivas da Nação” para construir “um novo Tempo”, num apelo patriótico; e mostra trabalhadores de todos os cantos do país chegando a Brasília, os candangos. Os elementos são o <strong>apelo simbólico e a migração inter-regional</strong>. Alternativa <strong>A</strong>.</p><p>O texto não fala de sindicatos, partidos ou segurança territorial (B, C e D).</p>",
  tags=["Brasília", "JK"])
X(83, "Geografia", "Globalização", "<p>O papa contrapõe a “globalização da esperança”, que nasce dos pobres, à “globalização da exclusão e da indiferença”. A crítica é à concentração de riqueza e à exclusão que acompanham a globalização: a <strong>disparidade econômica</strong>. Alternativa <strong>D</strong>.</p><p>Liberdade, mobilidade e conectividade (A, B e C) não são o alvo da crítica.</p>",
  tags=["exclusão social", "globalização"])
X(84, "História", "Mundo contemporâneo", "<p>A Declaração de 1948 afirmou, pela primeira vez em escala mundial, que todo ser humano tem direitos, independentemente do Estado a que pertence. Isso possibilitou a <strong>defesa dos grupos vulneráveis</strong> no plano internacional. Alternativa <strong>B</strong>.</p><p>Os Estados continuaram soberanos (A), e a declaração busca o contrário da impunidade (D).</p>",
  tags=["direitos humanos", "ONU"], trocas=[("História da paz", "<em>História da paz</em>")])
X(85, "História", "Patrimônio cultural", "<p>O mural chileno diz “Nuestra cultura no cabe en sus museos”, ao lado de retratos de indígenas. Ele denuncia que os museus escolhem o que guardar e expor segundo critérios de quem tem poder, deixando de fora a cultura viva dos povos originários. O conflito decorre da <strong>definição dos critérios de criação de acervos</strong>. Alternativa <strong>B</strong>.</p><p>O mural não trata de mercado de arte (A), de mais museus (C) ou de burocracia no acesso (D).</p>",
  figs(("q85", "Mural pintado num muro, com a frase “Nuestra cultura no cabe en sus museos” entre dois retratos emoldurados de pessoas indígenas.")),
  ["museus", "povos indígenas"])
X(86, "História", "Expansão marítima", "<p>Drake, com apoio da rainha Elizabeth I, saqueava as tropas de mulas com o ouro do Peru e as costas do Chile e do Peru. A pirataria foi o meio de a Inglaterra, sem colônias próprias, <strong>conquistar as riquezas dos territórios americanos</strong> que estavam nas mãos dos espanhóis. Alternativa <strong>B</strong>.</p><p>A pirataria não legalizava ocupações (C) nem buscava apoio das potências europeias (D).</p>",
  tags=["pirataria", "Francis Drake"], trocas=[("História das colonizações", "<em>História das colonizações</em>")])
X(87, "Sociologia", "Trabalho", "<p>O texto destaca “parcerias inéditas”: ações do Ministério do Trabalho com o Ministério da Defesa, o Exército, o Ibama e o ICMBio. A estratégia para combater o trabalho análogo à escravidão é <strong>articular os órgãos públicos</strong>. Alternativa <strong>A</strong>.</p><p>O texto não fala de Legislativo, multas ou pesquisas (B, C e E).</p>",
  tags=["trabalho escravo", "fiscalização"])
X(88, "Geografia", "População", "<p>O bônus demográfico é o período em que há muita gente em idade de trabalhar e poucas crianças e idosos dependentes. Para aproveitá-lo, essa população ativa precisa ser produtiva: o Estado deve estimular a <strong>qualificação da mão de obra</strong>. Alternativa <strong>C</strong>.</p><p>Aumentar impostos ou aposentadorias (B e E) não aproveita o bônus.</p>",
  tags=["bônus demográfico", "transição demográfica"])
X(89, "Geografia", "Cartografia", "<p>Utqiagvik fica acima do Círculo Polar Ártico. Por causa da inclinação do eixo da Terra, perto do solstício de dezembro o Sol não aparece no horizonte por semanas: é a noite polar. O fenômeno se deve à <strong>latitude</strong>. Alternativa <strong>D</strong>.</p><p>Longitude (C) define fuso horário, não a duração do dia; altitude e maritimidade (B e E) influem na temperatura.</p>",
  tags=["noite polar", "latitude"],
  enun=f'<p class="apoio"><strong>{T(89, 0)}</strong></p>' + ap(T(89, 1)) + fonte(T(89, 2)) + p(T(89, 3)))
X(90, "Geografia", "Fome", "<p>O texto diz que a fome não é problema técnico, porque já existem alimentos e meios para acabar com ela. Se há comida e ainda há fome, o problema é que muitas pessoas não têm como comprá-la: o <strong>padrão de distribuição de renda</strong>. Alternativa <strong>B</strong>.</p><p>Produtividade, armazenamento, escoamento e crescimento populacional (A, C, D e E) são justamente as explicações técnicas que o texto rejeita.</p>",
  tags=["fome", "desigualdade"])

completar(Q, R)
