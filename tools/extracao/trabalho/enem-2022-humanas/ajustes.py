# Enem 2022, 1º dia, caderno azul: Ciências Humanas (questões 46 a 90 do caderno; no site, 1 a 45, com numeroOriginal).
# Em 2022 o rótulo "QUESTÃO NN" vinha no mesmo bloco das alternativas da questão anterior: enem_rascunho.py parte o bloco ali.
# Letra de Vander Lee (Q52) como imagem. Sem anuladas nesta área.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, enunciado_enem, paragrafos_enem

ID = "enem-2022-humanas"
META = {"id": ID, "banca": "Enem", "ano": 2022, "titulo": "Enem 2022: Ciências Humanas", "fonte": "Inep", "dataExame": "2022-11-13",
        "duracaoMinutos": 135, "area": "Ciências Humanas", "caderno": "azul", "dia": 1}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2022-dia1-azul")
Q = {}
P = lambda n: paragrafos_enem(D[n])
p = lambda *xs: "".join(f"<p>{x}</p>" for x in xs)
ap = lambda *xs: "".join(f'<p class="apoio">{x}</p>' for x in xs)
fonte = lambda x: f'<p class="fonte">{x}</p>'


def figs(*pares):
    return [{"arquivo": a, "alt": t} for a, t in pares]


def E(n, pular=()):
    par = [x for i, x in enumerate(P(n)) if i not in pular]
    ult = max([i for i, (t, _) in enumerate(par) if t == "fonte"], default=-1)
    h = []
    for i, (t, x) in enumerate(par):
        if t == "fig": h.append(f"[[fig:{x}]]")
        elif t == "fonte": h.append(fonte(x))
        elif t == "titulo": h.append(f'<p class="apoio"><strong>{x}</strong></p>' if i < ult else f"<p><strong>{x}</strong></p>")
        elif i < ult: h.append(ap(x))
        else: h.append(p(x))
    return "".join(h)


def X(n, materia, assunto, expl, imagens=(), tags=(), enun=None, trocas=()):
    e = enun or enunciado_enem(D[n])
    for a, b in trocas:
        assert a in e, a; e = e.replace(a, b)
    Q[n - 45] = {"materia": materia, "assunto": assunto, "area": "Ciências Humanas", "tags": list(tags), "numeroOriginal": n,
                 "enunciado": e, "alternativas": dict(D[n]["alternativas"]), "imagens": list(imagens), "explicacao": expl}


X(46, "Geografia", "Clima e sociedade", "<p>O sertanejo põe seis pedrinhas de sal ao relento e observa quais se dissolvem com a umidade da madrugada para prever em que meses vai chover. É uma leitura do ambiente (umidade do ar, orvalho) misturada à tradição religiosa de Santa Luzia. Ele se mostra <strong>íntimo à Caatinga ao interpretar condições ambientais</strong>. Alternativa <strong>D</strong>.</p><p>O texto não fala de aceitar destinos (A), de pobreza (B), de solos (C) ou de vegetação (E).</p>",
  tags=["Euclides da Cunha", "saberes tradicionais"])
X(47, "Filosofia", "Filosofia política", "<p>Para Arendt, é o discurso que faz do homem um ser político: os homens no plural só dão sentido às coisas porque podem falar e ser entendidos uns pelos outros. A linguagem é base da <strong>construção da sociabilidade</strong>. Alternativa <strong>E</strong>.</p><p>O trecho opõe o homem no singular ao homem no plural; não trata de cultura em geral (A), criatividade (B), individualidade (C) ou técnica (D).</p>",
  tags=["Hannah Arendt", "linguagem"])
X(48, "Sociologia", "Desigualdade racial", "<p>Carolina Maria de Jesus conta que um guarda branco espancou um homem negro e o amarrou numa árvore, e pergunta se o guarda “ignora que já foi extinta a escravidão”. A violência contra pessoas negras, herdada da escravidão e repetida pelas instituições, é o <strong>racismo estrutural</strong>. Alternativa <strong>A</strong>.</p><p>Desemprego, renda, informação e educação (B a E) não são o tema do relato.</p>",
  tags=["Carolina Maria de Jesus", "racismo"])
X(49, "Geografia", "Hidrografia", "<p>O esquema mostra que, quanto mais o solo é impermeabilizado (de 0% a 100%), mais a água escoa pela superfície (de 10% para 55%) e menos infiltra e evapora. A urbanização muda os caminhos da água da chuva, isto é, o <strong>ciclo hidrológico</strong>, com efeitos imediatos como enchentes. Alternativa <strong>B</strong>.</p><p>Altitude, tectônica e rochas (A, D e E) não mudam com a ocupação; o clima (C) pode mudar, mas não de forma imediata.</p>",
  figs(("q49", "Quatro esquemas do destino da água da chuva conforme a superfície impermeável: cobertura natural do solo (evapotranspiração 40%, escoamento superficial 10%, infiltração subsuperficial 25%, percolação profunda 25%); 10–20% impermeável (38%, 20%, 21%, 21%); 35–50% impermeável (35%, 30%, 20%, 15%); 75–100% impermeável, numa cidade com prédios (30%, 55%, 10%, 5%).")),
  ["impermeabilização", "urbanização"])
X(50, "História", "Primeira República", "<p>O texto descreve o hospital moderníssimo da Madeira-Mamoré, “monumento ao progresso científico”, enquanto os trabalhadores doentes ficavam “na sombra”, “cobaias sem consolo, credores sem nome”. A crítica é a <strong>contradição entre desenvolvimento nacional e respeito aos trabalhadores</strong>. Alternativa <strong>E</strong>.</p><p>O texto não opõe engenharia e fauna (A), máquinas e floresta (B), investimento estatal e nativos (C) nem farmacologia e fitoterapia (D).</p>",
  tags=["Madeira-Mamoré", "trabalhadores"])
X(51, "Geografia", "Globalização", "<p>Castells descreve uma economia informacional, global e em rede: os componentes da produção ficam organizados em escala mundial, ligados por redes de empresas. Uma mesma mercadoria pode ser projetada num país, fabricada em outro e montada num terceiro: é a <strong>desterritorialização da produção</strong>. Alternativa <strong>E</strong>.</p><p>Produção em série, estoques grandes e padronização (A, B e D) são marcas do fordismo, anterior a essa economia; o texto não fala de cartéis (C).</p>",
  tags=["Castells", "economia em rede"])
X(52, "Geografia", "Espaço rural", "<p>A canção diz que o “gigante” urbano, “movido a tijolo e cimento”, precisa de “arroz com feijão”, e agradece a quem planta, colhe cacau e trabalha no milharal. Valoriza o campo por sua função de <strong>promover a produção alimentar</strong> para a cidade. Alternativa <strong>D</strong>.</p><p>A letra não fala de mão de obra qualificada (A), tecnologia (B), biodiversidade (C) ou moradia (E).</p>",
  figs(("q52", "Trecho da letra “Do Brasil”, de Vander Lee, como aparece na prova: os versos dizem que olhar o Brasil sem ver o sertão é negar sua base, que o país que cresce com tijolo e cimento precisa de comida na mesa, e agradecem a trabalhadores rurais que plantam, colhem cacau e trabalham no milharal.")),
  ["campo e cidade", "canção"], enun="[[fig:1]]" + fonte(P(52)[1][1]) + p(P(52)[2][1]))
X(53, "História", "Brasil Império", "<p>O texto mostra mulheres lendo folhetins, formando um público leitor e, depois, escrevendo e dirigindo uma imprensa feminina no Segundo Reinado. A inserção da mulher na leitura e na escrita se liga ao <strong>surgimento de novas práticas culturais</strong>. Alternativa <strong>A</strong>.</p><p>O texto não fala de contestar hábitos masculinos (B), de publicações juvenis (C), de manuais pedagógicos (D) ou de editoras comerciais (E).</p>",
  tags=["mulheres", "imprensa"])
X(54, "História", "Brasil Império", "<p>Na década de 1880, os caixeiros se organizaram, exigiram direitos e foram às ruas ao lado de republicanos e abolicionistas. Na capital do Império, essa atuação foi um momento de <strong>contestação dos princípios monárquicos</strong>, num período de crise da monarquia. Alternativa <strong>E</strong>.</p><p>Eles questionavam as regras patronais (A); sindicatos e contratos de trabalho estáveis (C e D) ainda não existiam; e não se afastaram das ideias liberais (B).</p>",
  tags=["movimentos sociais", "crise do Império"])
X(55, "Geografia", "Solos", "<p>A salinização acontece quando a água evapora antes de infiltrar e deixa os sais na superfície. A irrigação no Semiárido, sem drenagem que leve o excesso de água e sais embora, repete esse processo a cada rega. As atividades agrícolas agravam o problema ao <strong>utilizar sistemas de irrigação, desprezando uma drenagem adequada</strong>. Alternativa <strong>B</strong>.</p><p>Pinus, açudes, desmatamento e adubo orgânico (A, C, D e E) não explicam o acúmulo de sais descrito.</p>",
  tags=["salinização", "irrigação"])
X(56, "Sociologia", "Desigualdade social", "<p>Na charge, o menino sobe no telhado de uma casa precária tentando “achar um sinal de wi-fi” para estudar; o texto diz que muitos estudantes não têm internet, computador ou pacote de dados para as aulas remotas da pandemia. Os dois mostram a <strong>exclusão social</strong>, que a pandemia só deixou visível. Alternativa <strong>A</strong>.</p><p>A falta de acesso é o oposto de expansão digital (B); não há manifestação cultural, organização espacial ou valorização intelectual (C, D e E) em jogo.</p>",
  figs(("q56", "Charge: numa favela de casas de madeira amontoadas, uma voz pergunta “Tá estudando, Júnior?” e o menino, em cima do telhado segurando o celular preso a uma vara, responde: “Calma, tô tentando achar um sinal de wi-fi!”.")),
  ["exclusão digital", "pandemia"])
X(57, "Filosofia", "Poder", "<p>Foucault compara dois modelos: a lepra, tratada pela exclusão em massa, e a peste, tratada por um controle minucioso, que observa, separa e treina cada indivíduo. Esse “bom treinamento”, o poder que se multiplica e se subdivide, é a base da <strong>sociedade disciplinar</strong>. Alternativa <strong>A</strong>.</p><p>O texto mostra regras mais rígidas, não flexíveis (B), não fala de abolir a autoridade (C), de condenar a degradação (D) ou de burocracia (E).</p>",
  tags=["Foucault", "disciplina"])
X(58, "História", "Religiosidade", "<p>O texto I mostra Juazeiro se tornando centro de romarias, como Aparecida: a <strong>criação de um lugar místico</strong>. O texto II narra o milagre da hóstia que sangrou na boca da beata Maria de Araújo, proclamado sem autorização do bispo: uma <strong>experiência do catolicismo popular</strong>. Alternativa <strong>E</strong>.</p><p>Não há abandono do espiritual (A), elementos judaicos (B), cristianismo medieval (C) ou cerimônias ecumênicas (D).</p>",
  tags=["Padre Cícero", "catolicismo popular"])
X(59, "Geografia", "Agricultura familiar", "<p>O Programa de Aquisição de Alimentos é uma compra pública destinada só à agricultura familiar: o governo compra o que esses pequenos produtores plantam. A conquista é a <strong>comercialização garantida</strong>. Alternativa <strong>C</strong>.</p><p>O programa não trata de tecnologia (A), reforma agrária (B), frete (D) ou bolsa de valores (E).</p>",
  tags=["PAA", "políticas públicas"])
X(60, "Sociologia", "Tecnologia e sociedade", "<p>No FunFit, se a pessoa andava mais, eram seus conhecidos que ganhavam dinheiro, e o esquema foi muito mais eficaz que o incentivo individual. Ao contrário da ideia de que o celular isola, ele teve uma função <strong>social, estimulando a reciprocidade por meios digitais</strong>. Alternativa <strong>B</strong>.</p><p>O texto não fala de lazer (A), trabalho (C), consumo (D) ou aprendizagem (E).</p>",
  tags=["redes", "reciprocidade"])
X(61, "Sociologia", "Trabalho", "<p>A inteligência artificial passa a fazer a dublagem, automatizando um trabalho antes humano e tornando “mais escassas as oportunidades” para dubladores e atores. É a <strong>ampliação do desemprego estrutural</strong>, causado por mudanças na forma de produzir. Alternativa <strong>E</strong>.</p><p>O texto não fala de economia nacional (A), cultura tradicional (B), formação acadêmica (C) ou estagnação artística (D).</p>",
  tags=["automação", "desemprego estrutural"])
X(62, "Geografia", "Blocos econômicos", "<p>A Tarifa Externa Comum é o imposto de importação igual que os membros do Mercosul cobram de países de fora do bloco. Por ser comum, um país não pode mudá-la sozinho: Brasil e Argentina tiveram de negociar e levar o acordo a Paraguai e Uruguai. Isso decorre do <strong>funcionamento da união aduaneira</strong>. Alternativa <strong>C</strong>.</p><p>O Mercosul não tem moeda ou política monetária comum (B) nem legislação trabalhista igual (E).</p>",
  tags=["Mercosul", "TEC"])
X(63, "História", "Idade Média", "<p>O texto diz que, no início da Idade Média, o socorro aos famintos era parte da gestão pública, mesmo quando apresentado como caridade. Na monarquia cristã merovíngia, governar incluía proteger os súditos: o dever cabia à <strong>realeza, decorrente do conceito de governo subjacente à monarquia cristã</strong>. Alternativa <strong>B</strong>.</p><p>Nobreza, mosteiros, bispados e corporações (A, C, D e E) agiam por caridade individual, que o texto diz ser só a forma como as fontes apresentam a ação.</p>",
  tags=["merovíngios", "monarquia cristã"])
X(64, "Geografia", "Geologia", "<p>As forças internas trazem material novo à superfície (vulcanismo) e as externas (chuva, erosão) o decompõem. Os <strong>solos vulcânicos</strong>, formados pelo intemperismo de rochas como o basalto, são muito férteis e atraem ocupação humana, como a terra roxa no Brasil ou as encostas vulcânicas da Itália e da Indonésia. Alternativa <strong>A</strong>.</p><p>Dorsais oceânicas ficam no fundo do mar (B); relevos escarpados e dobramentos (C e E) dificultam a ocupação; solos lateríticos (D) são pobres.</p>",
  tags=["vulcanismo", "intemperismo"])
X(65, "Sociologia", "Violência de gênero", "<p>A ilustração mostra o ciclo da violência doméstica: tensão, agressão e “lua de mel” (promessas e reconciliação) se repetem numa espiral cada vez mais grave, até chegar à cruz e à palavra “morte” no topo. O ápice é a <strong>prática do feminicídio</strong>. Alternativa <strong>B</strong>.</p><p>Cancelamento, negacionismo e “defesa da honra” (A, C e E) não correspondem ao topo da espiral; a violência não é involuntária (D).</p>",
  figs(("q65", "Espiral subindo, com três momentos que se repetem em ciclos cada vez maiores: Tensão (insulto, humilhação, intimidação, gritos, ameaça, controle, isolamento, medo, conflitos), Agressão (empurrão, beliscão, puxão de cabelo, sufocamento, arremesso de objetos, tapa, chute, espancamento) e Lua de mel (carinho, paixão, presentes, promessas, reconciliação, liberdade). No topo da espiral, uma cruz e a palavra “Morte”.")),
  ["ciclo da violência", "feminicídio"])
X(66, "História", "Brasil Império", "<p>O Visconde de Cayru defende um currículo mínimo de matemática para as meninas, por julgar que não tinham capacidade (exclusão de competências). O Marquês de Santo Amaro defende o mesmo currículo para meninos e meninas, conforme “as luzes do tempo” (igualdade). A oposição é entre <strong>dominação de corpos e igualdade humana</strong>. Alternativa <strong>C</strong>.</p><p>O debate não é de liberdade de gênero (A), escolha (B), carreira (D) ou participação política (E).</p>",
  tags=["educação feminina", "lei de 1827"])
X(67, "Sociologia", "Movimentos sociais", "<p>O movimento ocupou um terreno abandonado e reivindicou seu uso para moradia, citando a Constituição, que no art. 6º garante o direito à moradia. Depois de sete anos, os condomínios foram inaugurados. A estratégia serviu para <strong>garantir o preceito constitucional</strong>. Alternativa <strong>D</strong>.</p><p>A conquista contou com o poder público (A); não houve economia solidária (B), controle de propriedade estatal (C) ou especulação (E).</p>",
  tags=["direito à moradia", "ocupação"])
X(68, "Geografia", "Geopolítica", "<p>O texto e o mapa mostram a preocupação dos EUA com regiões “insubmissas” às regras do FMI, da OMC e do Banco Mundial, muitas delas ricas em petróleo, gás e biodiversidade. A estratégia é garantir acesso a esses recursos e às regras do mercado: <strong>ampliação de influência econômica</strong>. Alternativa <strong>D</strong>.</p><p>Não se trata de compartilhar tecnologia (A), promover independência (B), intercâmbio cultural (C) ou preservação (E).</p>",
  figs(("q68", "Mapa-múndi com manchas de “alta densidade e variedade germoplásmica” e de “petróleo e gás”, e uma linha tracejada contornando a “brecha” crítica do “Novo Mapa do Pentágono”: parte da América Latina, a África, o Oriente Médio e partes da Ásia.")),
  ["Estados Unidos", "hegemonia"],
  trocas=[(" TEXTO II</p>", '</p><p class="apoio"><strong>TEXTO II</strong></p>')])
X(69, "Geografia", "Geopolítica", "<p>Putin diz que a Crimeia sempre foi “parte inseparável da Rússia” no coração do povo, convicção passada de geração em geração. A maioria da população da península fala russo e se identifica com a Rússia: o argumento é que <strong>populações com idioma comum devem estar submetidas à mesma autoridade estatal</strong>. Alternativa <strong>A</strong>.</p><p>O discurso não fala de imperialismo soviético (B), organismos internacionais (C), integração regional (D) ou forças navais ocidentais (E).</p>",
  tags=["Crimeia", "Rússia"])
X(70, "Sociologia", "Desigualdade social", "<p>A interseccionalidade é o cruzamento de desigualdades. O gráfico mostra que mulheres sem cônjuge e com filhos têm 56,9% de pobreza; entre as pretas ou pardas, 64,4%; entre as brancas, 41,5%. O cruzamento de <strong>raça e gênero</strong> intensifica a discriminação. Alternativa <strong>A</strong>.</p><p>Os dados não tratam de etnia e habitação (B), idade e nupcialidade (C), profissão e sexualidade (D) ou escolaridade e fecundidade (E).</p>",
  figs(("q70", "Gráfico de barras “Proporção de pessoas abaixo da linha de pobreza, por arranjo domiciliar no Brasil — 2017”: mulher sem cônjuge e com filho(s) até 14 anos, 56,9%; mulher preta ou parda nessa situação, 64,4%; mulher branca nessa situação, 41,5%; casal com filho(s), 30,4%; outros, 21,0%; unipessoal, 11,6%; casal sem filho, 10,0%.")),
  ["interseccionalidade", "pobreza"],
  trocas=[('<p class="apoio">TEXTO I Interseccionalidade:', '<p class="apoio"><strong>TEXTO I</strong></p><p class="apoio">Interseccionalidade:')])
X(71, "Sociologia", "Estado e democracia", "<p>No Estado de direito, ninguém, nem o governo, está acima da lei, e os poderes são exercidos de acordo com ela. Suprimir eleições é o governo se colocar acima das regras e dos direitos dos cidadãos: a <strong>supressão de eleições de representantes políticos</strong> viola o princípio. Alternativa <strong>A</strong>.</p><p>Ação da Igreja, projetos sociais e leis trabalhistas (B, C e E) não violam a lei; a concentração de renda (D) é um problema social, não uma violação do Estado de direito.</p>",
  tags=["Estado de direito", "democracia"])
X(72, "Geografia", "População", "<p>Marcelo sai de casa às 5 h, pega trem e ônibus e chega ao trabalho às 7 h 10; no fim do dia, volta. Esse deslocamento diário de ida e volta entre a casa e o trabalho, típico de regiões metropolitanas, é o <strong>movimento pendular</strong>. Alternativa <strong>D</strong>.</p><p>Não há mudança de residência (A e B), deslocamento por estação do ano (C) ou forçado (E).</p>",
  tags=["movimento pendular", "metrópoles"])
X(73, "História", "Movimento operário", "<p>Perrot diz que o Primeiro de Maio foi criado por um ato político deliberado dos socialistas, para dar “unidade política e cultural” à classe operária por meio da festa. O objetivo era <strong>afirmar uma identidade coletiva</strong>, a de classe. Alternativa <strong>B</strong>.</p><p>A data não é burguesa (A), nacional (C) ou cívica (D), e foi criada, não herdada de uma tradição popular (E).</p>",
  tags=["Primeiro de Maio", "classe operária"])
X(74, "Geografia", "Clima", "<p>O mapa mostra a maior radiação solar média no interior do Nordeste, especialmente no Semiárido. Essa região tem chuvas escassas e, por isso, céu limpo na maior parte do ano: a reduzida <strong>nebulosidade atmosférica</strong> deixa passar mais radiação. Alternativa <strong>C</strong>.</p><p>Relevo, longitude e continentalidade (A, B e E) não explicam o padrão; a irregularidade das chuvas (D) é alta, não reduzida, no Semiárido.</p>",
  figs(("q74", "Mapa do Brasil “Radiação solar global horizontal média anual”, em tons de cinza de 3,15 a 6,65 kWh/m²: os valores mais altos aparecem no interior do Nordeste e no Centro-Oeste; os mais baixos, no litoral Sul e em partes da Amazônia.")),
  ["energia solar", "nebulosidade"])
X(75, "Geografia", "Povos indígenas", "<p>Para os Kambeba, o povo nasceu de uma gota-d’água; a escritora aprendeu com o pai a “ouvir o rio” e a reconhecer sua “sabedoria milenar”. O rio é parte da cosmologia, da memória e dos laços familiares: um <strong>patrimônio cultural e afetivo</strong>. Alternativa <strong>E</strong>.</p><p>O rio não é tombado (A), não é objeto de religião institucional (B), não é só paisagem (C) e não é riqueza individual (D).</p>",
  tags=["Kambeba", "cosmologia indígena"])
X(76, "História", "Nordeste e seca", "<p>O texto descreve milhares de sertanejos cavando o açude, com as famílias morando em casas de taipa ao redor: “embrião de futura cidade”. A obra mostra <strong>trabalhadores na formação de novos espaços</strong>. Alternativa <strong>D</strong>.</p><p>Não há canais fluviais (A), coronéis (B), distribuição de água (C) nem comércio (E) no trecho.</p>",
  tags=["açudes", "trabalhadores"])
X(77, "História", "Brasil Colônia", "<p>O texto diz que os manuais de administração de escravos e o saber médico serviam a uma “moderna gestão da mão de obra escravista” e ao desenvolvimento colonial. A medicina atendia aos <strong>objetivos econômicos das elites</strong>: manter os escravizados vivos e produtivos. Alternativa <strong>A</strong>.</p><p>O texto não fala de viajantes (B), abolicionistas (C), nativos (D) ou emancipação (E).</p>",
  tags=["escravidão", "medicina colonial"])
X(78, "Geografia", "Cartografia", "<p>No mapa, a distância entre o local dos destroços e Perth é de 2 500 km e, na representação, mede 2 cm. Então 1 cm representa 1 250 km = 125 000 000 cm. A escala é <strong>1 : 125 000 000</strong>. Alternativa <strong>E</strong>.</p><p>1 : 12 500 000 (D) erra a conversão de km para cm por um fator 10.</p>",
  figs(("q78", "Mapa “Possível trajeto do voo MH370 da Malaysia Airlines antes da queda, em 2014”: do último contato, perto da Malásia, uma linha tracejada desce pelo Oceano Índico até o local onde os destroços foram avistados; desse ponto até a cidade de Perth, na Austrália, uma linha indica 2 500 km.")),
  ["escala"], enun=E(78, pular=(0,)))
X(79, "História", "Patrimônio", "<p>O tamborete de baiana diz que sua história está ligada às mãos que o fizeram e às mulheres que o usaram, “aos dons individuais das pessoas e suas práticas sociais”, como o conhecimento de modelos e a destreza nos desenhos. Associa-se às <strong>habilidades artísticas e culturais dos sujeitos</strong>. Alternativa <strong>A</strong>.</p><p>O texto não fala de religião (B), expositores (C), arquitetura (D) ou finanças (E).</p>",
  tags=["museu", "patrimônio imaterial"])
X(80, "Filosofia", "Filosofia antiga", "<p>Vernant liga o nascimento da filosofia à <em>polis</em>: a razão grega nasce do debate público da cidade. Os <strong>sofistas</strong>, que ensinavam retórica a quem queria falar nas assembleias, fortaleceram esse laço entre pensamento e vida política. Alternativa <strong>C</strong>.</p><p>Epicuristas e estoicos (A e B) vêm depois, num mundo helenístico sem a <em>polis</em> autônoma; os peripatéticos (D) são a escola de Aristóteles; os rapsodos (E) representam o mito, não a razão.</p>",
  tags=["pólis", "sofistas"])
X(81, "História", "Era Vargas", "<p>O DIP, criado no Estado Novo, coordenava a relação da imprensa com o governo e decidia, “a seu juízo”, quais jornais recebiam a devolução do depósito para importar papel. Com isso o governo controlava a imprensa e premiava os jornais alinhados: <strong>cerceamento da liberdade de expressão</strong>. Alternativa <strong>D</strong>.</p><p>O DIP não diversificava a opinião (A), não privatizava (E) e não cuidava de sindicatos (C).</p>",
  tags=["Estado Novo", "DIP"])
X(82, "Geografia", "Geologia", "<p>Rochas ígneas (magmáticas) são associadas a escudos cristalinos antigos, onde se formam <strong>jazidas de minerais metálicos</strong>, como ferro, ouro e manganês, por exemplo em Carajás (Pará). Alternativa <strong>B</strong>.</p><p>Combustíveis fósseis e aquíferos profundos (C e D) se ligam a bacias sedimentares; o Brasil não tem abalos sísmicos frequentes (A); rochas metamórficas (E) são outro tipo.</p>",
  figs(("q82", "Mapa “Rochas ígneas da Amazônia Legal”, entre 5°N e 15°S e 70°W e 50°W: manchas escuras de rochas ígneas espalhadas, principalmente no Pará, em Rondônia, em Mato Grosso, em Roraima e no Amapá.")),
  ["escudos cristalinos", "recursos minerais"], enun=E(82, pular=(0, 2, 3)))
X(83, "Sociologia", "Cidadania", "<p>As irmãs não puderam ser registradas nem no Líbano, onde nasceram, nem na Síria, país dos pais. Sem nacionalidade reconhecida por nenhum Estado, são <strong>apátridas</strong>. Alternativa <strong>B</strong>.</p><p>Exilado, refugiado e foragido (A, C e D) são pessoas que deixaram seu país; clandestino (E) é quem está irregular num país.</p>",
  tags=["apatridia", "nacionalidade"])
X(84, "Filosofia", "Estética", "<p>Merleau-Ponty diz que uma filosofia da percepção devolve à pintura seu lugar, e Deleuze diz que os cineastas “pensam com imagens, em vez de conceitos”. Os dois tratam a arte e o ver como formas de pensar: <strong>o olhar como experiência de conhecimento</strong>. Alternativa <strong>C</strong>.</p><p>Os textos não falam do belo transcendental (A), de juízo de gosto (B), de arte como auxiliar da razão (D) ou de inteligência derivada de representações (E).</p>",
  tags=["Merleau-Ponty", "Deleuze"])
X(85, "História", "Inquisição", "<p>O edital fixa regras para o público durante o auto de fé, e Bethencourt explica que lugares, posturas, gestos e palavras eram previamente definidos. O rito ensinava como cada um devia se comportar diante do poder da Igreja: ela mostrava capacidade de <strong>produzir padrões de conduta</strong>. Alternativa <strong>D</strong>.</p><p>O edital proíbe atirar objetos nos réus, então não favorece a violência (B); o rito é de punição, não a abranda (A).</p>",
  tags=["auto de fé", "Inquisição"])
X(86, "Filosofia", "Pré-socráticos", "<p>Empédocles explica a origem e a transformação do mundo por quatro elementos eternos movidos por Amor e Ódio. Buscar o princípio (<em>arché</em>) de todas as coisas é discutir a origem e a ordem do cosmos: o texto <strong>evoca a discussão cosmogônica</strong>. Alternativa <strong>C</strong>.</p><p>Amor e Ódio são forças cósmicas, não paixões humanas (D), e a explicação é racional, não mitológica (E).</p>",
  tags=["Empédocles", "arché"],
  enun=ap(P(86)[0][1]) + fonte("SIMPLÍCIO. Física, 25, 21. In: <em>Os pré-socráticos</em>. São Paulo: Nova Cultural, 1996.") + p(P(86)[1][1].split("1996. ", 1)[1].replace("arché", "<em>arché</em>")))
X(87, "Geografia", "Urbanização", "<p>A macrocefalia urbana é a concentração excessiva de pessoas e atividades em poucas metrópoles. No Brasil, ela foi estimulada pelo <strong>êxodo da população do campo</strong>, que, com a mecanização e a concentração de terras, migrou em massa para as grandes cidades. Alternativa <strong>B</strong>.</p><p>Os outros fatores são consequência (C) ou não explicam a concentração (A, D e E).</p>",
  tags=["êxodo rural", "metropolização"])
X(88, "Filosofia", "Filosofia helenística", "<p>Sêneca, estoico, elogia Basso por estar alegre diante da morte e firme qualquer que seja o estado do corpo. Para os estoicos, a filosofia ensina a dominar as emoções e aceitar o que não depende de nós: a <strong>moderação das paixões</strong>. Alternativa <strong>E</strong>.</p><p>O trecho não fala de debate (A), de rejeição social (B), de religião (C) e não exalta o sofrimento (D), mas a serenidade diante dele.</p>",
  tags=["Sêneca", "estoicismo"])
X(89, "História", "América pré-colombiana", "<p>Galeano cita a organização política dos incas e astecas, a astronomia e o zero dos maias e as cirurgias incas. São conhecimentos desenvolvidos pelos próprios povos: <strong>heranças culturais constituídas em saberes próprios</strong>. Alternativa <strong>C</strong>.</p><p>O texto é anterior à influência cristã e europeia (A e D); não fala de armas pilhadas (B); e a medicina inca não era ciência no sentido moderno (E).</p>",
  tags=["incas, astecas e maias", "Galeano"])
X(90, "Geografia", "Comunidades tradicionais", "<p>As paneleiras de Goiabeiras usam argila do barreiro, madeira e tinta do mangue, num saber passado de mãe para filha há cerca de 400 anos. A ligação entre recursos naturais e saber tradicional garante a <strong>manutenção dos modos de vida</strong> da comunidade. Alternativa <strong>A</strong>.</p><p>O texto não fala de roça (B), gestão (C), consumo (D) ou especialização (E).</p>",
  tags=["paneleiras de Goiabeiras", "patrimônio imaterial"])

completar(Q, R)
