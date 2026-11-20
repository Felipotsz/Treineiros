# Enem 2012, 1º dia, caderno azul: Ciências Humanas (questões 1 a 45; no 1º dia de 2012 vinham Humanas e Natureza).
# Texto legível (sem DECOD). Letra de canção (Q43, Luiz Gonzaga) como imagem.
# Sem anuladas nesta área.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, enunciado_enem, paragrafos_enem

ID = "enem-2012-humanas"
META = {"id": ID, "banca": "Enem", "ano": 2012, "titulo": "Enem 2012: Ciências Humanas", "fonte": "Inep", "dataExame": "2012-11-03",
        "duracaoMinutos": 135, "area": "Ciências Humanas", "caderno": "azul", "dia": 1}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2012-dia1-azul")
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




X(1, "História", "Absolutismo", "<p>A charge mostra o rei com o manto, a peruca e o salto alto; sem eles, um homem baixo, magro e calvo; e o conjunto de roupas sozinho, num cabide, já parece um rei. A majestade é construída pela aparência: mostra <strong>a importância da vestimenta para a constituição simbólica do rei, pois o corpo político adornado esconde os defeitos do corpo pessoal</strong>. Alternativa <strong>E</strong>.</p><p>A charge não humaniza o rei (A): ela ironiza a fabricação de sua imagem.</p>",
  figs(("q01", "Charge em três partes: à esquerda, o traje real completo, com manto de arminho e peruca, montado sobre um suporte; no meio, um homem baixo, calvo e magro, de roupas simples, apoiado numa bengala; à direita, o mesmo homem vestido com o traje, como Luís XIV.")),
  ["Luís XIV", "imagem do rei"], trocas=[("A fabricação do rei", "<em>A fabricação do rei</em>")])
X(2, "Filosofia", "Iluminismo", "<p>Para Kant, a menoridade é não usar o próprio entendimento sem a direção de outro, por falta de coragem. O lema do Esclarecimento é “tem coragem de fazer uso de teu próprio entendimento”: é <strong>a reivindicação de autonomia da capacidade racional como expressão da maioridade</strong>. Alternativa <strong>A</strong>.</p><p>Aceitar verdades impostas por outros (C e D) é justamente a menoridade.</p>",
  tags=["Kant", "autonomia"], trocas=[("Resposta à pergunta: o que é esclarecimento?", "<em>Resposta à pergunta: o que é esclarecimento?</em>")])
X(3, "Sociologia", "Violência", "<p>Para Elias, toda sociedade precisa controlar as pulsões dos indivíduos. O texto I diz que, no Brasil, a cidadania é frágil e o Estado está ausente em vários territórios, e é aí que a violência cria raízes. Há <strong>dificuldade histórica da sociedade brasileira em institucionalizar formas de controle social compatíveis com valores democráticos</strong>. Alternativa <strong>D</strong>.</p><p>O texto não opõe democracia e polícia (A): fala da falta do Estado.</p>",
  tags=["Norbert Elias", "processo civilizador"], trocas=[("IstoÉ", "<em>IstoÉ</em>"), ("O Processo Civilizador", "<em>O Processo Civilizador</em>")])
X(4, "História", "Segunda Guerra Mundial", "<p>A capa de março de 1941 mostra o Capitão América, com o uniforme da bandeira americana, socando Hitler, e o texto fala do “sopapo no Führer”. A revista associava o herói à luta dos Estados Unidos contra <strong>os regimes totalitários, na Segunda Guerra Mundial</strong>. Alternativa <strong>B</strong>.</p>",
  figs(("q04", "Capa da revista Captain America Comics n. 1, de março: o Capitão América, com escudo e uniforme com estrelas e listras, invade uma sala cheia de soldados nazistas e dá um soco em Hitler.")),
  ["Capitão América", "propaganda"], trocas=[("Capitão América, o primeiro vingador: crítica", "<em>Capitão América, o primeiro vingador</em>: crítica"), ("no Fürer", "no <em>Führer</em>")])
X(5, "História", "Escravidão", "<p>Africanos de povos diferentes, misturados na escravidão, perceberam que tinham elos culturais profundos, na língua e na religião, e “descobriram a África no Brasil”. O contato tornou possível a <strong>formação de uma identidade cultural afro-brasileira</strong>. Alternativa <strong>A</strong>.</p><p>O texto destaca o que os aproximava, e não os conflitos entre etnias (C).</p>",
  tags=["cultura afro-brasileira", "identidade"], trocas=[("Revista USP", "<em>Revista USP</em>")])
X(6, "História", "Guerra Fria", "<p>Martin Luther King liderou o movimento pelos direitos civis no sul dos Estados Unidos, onde havia segregação legal. O “cheque” do discurso é a promessa de liberdade e justiça para todos. O objetivo era <strong>a conquista de direitos civis para a população negra</strong>. Alternativa <strong>A</strong>.</p><p>King defendia a não violência (B).</p>",
  tags=["direitos civis", "Martin Luther King"], trocas=[("Eu tenho um sonho", "<em>Eu tenho um sonho</em>")])
X(7, "Filosofia", "Filosofia política", "<p>Montesquieu diz que liberdade política não é fazer o que se quer, mas “o direito de fazer tudo o que as leis permitem”. A liberdade depende da lei: é o <strong>condicionamento da liberdade dos cidadãos à conformidade às leis</strong>. Alternativa <strong>B</strong>.</p><p>Fazer o que é proibido (D) destruiria a liberdade de todos, segundo o texto.</p>",
  tags=["Montesquieu", "liberdade"], trocas=[("Do Espírito das Leis", "<em>Do Espírito das Leis</em>")])
X(8, "História", "Descolonização", "<p>No cartum, o vice-rei britânico tenta prender Gandhi numa cela, mas, atrás dele, há uma multidão enorme de seguidores, todos com o rosto de Gandhi. Prender um homem não resolve: mostra <strong>a impossibilidade de deter o movimento liderado por Gandhi</strong>. Alternativa <strong>D</strong>.</p>",
  figs(("q08", "Cartum “Lord Willingdon’s dilemma”: o vice-rei britânico, de costas, está à porta de uma prisão com Gandhi lá dentro; atrás dele, uma multidão imensa de pequenas figuras, todas parecidas com Gandhi.")),
  ["Gandhi", "independência da Índia"])
X(9, "Filosofia", "Filosofia contemporânea", "<p>Habermas mostra que as regras de uma cultura majoritária podem oprimir as minorias. Numa democracia, a saída é que cada grupo leve seus modos de vida ao debate público, onde vale a força do melhor argumento. Isso permite <strong>a coexistência das diferenças, considerando a possibilidade de os discursos de autoentendimento se submeterem ao debate público</strong>. Alternativa <strong>C</strong>.</p><p>A separação em territórios (A) e a assimilação pela cultura nacional (B) não respeitam a diferença.</p>",
  tags=["Habermas", "minorias"], trocas=[("A inclusão do outro", "<em>A inclusão do outro</em>")])
X(10, "História", "Colonização espanhola", "<p>Colombo destaca o ouro de Veragua e diz que lá se pode “extrair à vontade”. O interesse pelos metais levou os espanhóis a criar cidades para administrar a extração e controlar o caminho das riquezas até a Espanha: a <strong>fundação de cidades para controlar a circulação de riquezas</strong>. Alternativa <strong>E</strong>.</p><p>A América espanhola usou sobretudo trabalho indígena, e não africano, nas minas (C).</p>",
  tags=["metais preciosos", "cidades coloniais"], trocas=[("Colombo e a América: quinhentos anos depois", "<em>Colombo e a América: quinhentos anos depois</em>")])
X(11, "História", "Revoluções inglesas", "<p>A Declaração de Direitos de 1689 proíbe o rei de suspender leis e de cobrar impostos sem o Parlamento: é a <strong>limitação do poder do soberano</strong>. No resto da Europa, predominava o <strong>absolutismo</strong>, com o rei acima das leis. Alternativa <strong>B</strong>.</p>",
  tags=["Bill of Rights", "monarquia parlamentar"])
X(12, "História", "Era Vargas", "<p>O cartaz põe em primeiro plano um bandeirante com a bandeira paulista e o lema “Abaixo a dictadura”. Os paulistas associavam a revolução de 1932 <strong>ao bandeirantismo, símbolo paulista apresentado em primeiro plano</strong>, como herança de coragem e pioneirismo. Alternativa <strong>D</strong>.</p><p>A figura é um bandeirante, e não um militar (C).</p>",
  figs(("q12", "Cartaz com as palavras “Abaixo a dictadura”: um bandeirante de chapéu, barba e roupas coloniais segura a bandeira de São Paulo.")),
  ["Revolução Constitucionalista", "bandeirantes"])
X(13, "História", "Era Vargas", "<p>O texto defende salvar do “perecimento e da evasão” as obras de arte e os bens históricos, que são patrimônio comum. O SPHAN foi criado para <strong>resguardar da destruição as obras representativas da cultura nacional, por meio de políticas públicas preservacionistas</strong>. Alternativa <strong>D</strong>.</p><p>O texto não fala em incentivos privados (B) nem em punição (E).</p>",
  tags=["SPHAN", "patrimônio"],
  enun=ap(T(13, 0)) + fonte(T(13, 1).replace("O Jornal", "<em>O Jornal</em>").replace("Brasil, 500 anos em documentos", "<em>Brasil, 500 anos em documentos</em>")) + p("A criação no Brasil do Serviço do Patrimônio Histórico e " + T(13, 3)))
X(14, "Geografia", "Transportes", "<p>Navios esperando anos somados para atracar em Santos mostram um gargalo na infraestrutura de exportação. Isso encarece e atrasa o escoamento da produção agrícola, gerando a <strong>redução da exportação de gêneros agrícolas em função da dificuldade para o escoamento</strong>. Alternativa <strong>C</strong>.</p><p>O modal aéreo (A) é caro demais para grãos e minérios.</p>",
  tags=["portos", "logística"], trocas=[("Folha de S. Paulo", "<em>Folha de S. Paulo</em>")])
X(15, "História", "Ditadura militar", "<p>Os jornalistas pedem que a Justiça faça “novas diligências capazes de levar à completa elucidação desses fatos”. A versão oficial de suicídio de Herzog era contestada, e eles queriam que a morte fosse investigada: há <strong>expectativa da investigação dos culpados</strong>. Alternativa <strong>E</strong>.</p><p>Em 1976 o regime ainda estava em vigor (B), e ninguém foi punido (D).</p>",
  tags=["Vladimir Herzog", "imprensa"], trocas=[("O Estado de São Paulo", "<em>O Estado de São Paulo</em>"), ("Brasil, 500 anos em documentos", "<em>Brasil, 500 anos em documentos</em>"), ("abaixoassinado", "abaixo-assinado")])
X(16, "História", "Roma Antiga", "<p>O mosaico de Lod mostra elefantes, girafas, leões e outros animais de regiões distantes, como a África e a Ásia. Os animais exóticos evocam a extensão do império e os territórios submetidos: <strong>expansionismo – diversidade dos territórios conquistados</strong>. Alternativa <strong>E</strong>.</p><p>As Cruzadas (A) só aconteceriam na Idade Média.</p>",
  figs(("q16", "Mosaico romano de Lod com moldura octogonal decorada com peixes: no centro, um elefante, uma girafa, um tigre, leões, um rinoceronte e outros animais, alguns lutando.")),
  ["Império Romano", "mosaico"])
X(17, "História", "Primeiro Reinado", "<p>D. Pedro I foi recebido com frieza em Minas e, no Rio, “brasileiros” atacaram as comemorações dos “portugueses” que o apoiavam. Ele havia dissolvido a Constituinte e outorgado uma Constituição com o Poder Moderador, e a oposição crescia. Os episódios revelam <strong>questionamentos ao autoritarismo</strong>. Alternativa <strong>E</strong>.</p><p>Havia antilusitanismo, mas os conflitos eram contra o imperador e seu governo, e não um movimento de apoio ao xenofobismo (B).</p>",
  tags=["Noite das Garrafadas", "abdicação"], trocas=[("Dicionário do Brasil Imperial", "<em>Dicionário do Brasil Imperial</em>")])
X(18, "Geografia", "Paisagem", "<p>O texto diz que a paisagem é “portadora de memória” e constrói “sentimentos de pertencimento”, ligada às festas e aos momentos fortes da vida. Além de forma concreta, ela tem uma dimensão <strong>simbólica de relação subjetiva do indivíduo com o espaço</strong>. Alternativa <strong>E</strong>.</p>",
  tags=["paisagem", "lugar"], trocas=[("Terra dos homens: a geografia", "<em>Terra dos homens: a geografia</em>")])
X(19, "História", "Industrialização", "<p>A foto mostra operários enfileirados ao longo de uma esteira, cada um repetindo a mesma tarefa: é a linha de montagem fordista. O modelo se baseava na <strong>exploração do trabalho repetitivo</strong>. Alternativa <strong>C</strong>.</p><p>No fordismo, o trabalhador perde autonomia (A) e não precisa ser qualificado (D).</p>",
  figs(("q19", "Foto antiga de uma fábrica: operários de boné, lado a lado ao longo de uma esteira, montando peças iguais em série.")),
  ["fordismo", "linha de montagem"])
X(20, "Geografia", "Questão agrária", "<p>Na África colonial, os colonos brancos tomaram as melhores terras, e, mesmo após a independência, a terra continuou concentrada. As áreas férteis ficaram com a agricultura de exportação, e a população pobre foi empurrada para terras ruins: <strong>concentração das áreas cultiváveis no setor agroexportador – aumento da ocupação da população pobre em territórios agrícolas marginais</strong>. Alternativa <strong>E</strong>.</p>",
  tags=["África subsaariana", "concentração fundiária"], trocas=[("Geografia agrária: teoria e poder", "<em>Geografia agrária: teoria e poder</em>")])
X(21, "História", "Crise de 1929", "<p>A crise de 1929 veio da superprodução industrial nos Estados Unidos, sem consumo suficiente, que levou ao crash da Bolsa. A crise atual (2008) nasceu no setor financeiro, com especulação e crédito sem controle, como mostra o texto I. Alternativa <strong>B</strong>.</p><p>A crise atual resultou da desregulamentação, e não do excesso de regulação (E).</p>",
  tags=["crise de 2008", "superprodução"], trocas=[("Folha de São Paulo", "<em>Folha de São Paulo</em>"), ("do crash de 1929", "do <em>crash</em> de 1929")])
X(22, "História", "Contracultura", "<p>“Faça amor, não faça guerra” e “quando penso em revolução quero fazer amor” juntam a política com a vida pessoal: o corpo e o desejo viram forma de protesto. A inovação estava na <strong>unificação das noções de libertação social e libertação individual, fornecendo um significado político ao uso do corpo</strong>. Alternativa <strong>C</strong>.</p>",
  figs(("q22", "Foto de jovens numa manifestação; uma moça segura um cartaz escrito “Love not war”, com o símbolo da paz.")),
  ["anos 1960", "Guerra do Vietnã"],
  enun="[[fig:1]]" + ap("Texto do cartaz: “Amor e não guerra”") + fonte(T(22, 2)) + p(T(22, 3).replace("Seus slogans", "Seus <em>slogans</em>")))
X(23, "Sociologia", "Corpo e sociedade", "<p>O texto diz que “engordamos quando somos gulosos” e fala em “pecado da gula”: a obesidade vira falha moral da pessoa. A consequência é <strong>a culpabilização individual, associando obesidade à fraqueza de caráter</strong>. Alternativa <strong>D</strong>.</p><p>O discurso não democratiza a beleza (B): culpa quem não se encaixa.</p>",
  tags=["padrão corporal", "culpa"])
X(24, "Geografia", "População", "<p>As pirâmides mostram que, de 1991 para 2010, a base se estreitou nas duas áreas, mas a pirâmide urbana tem a base mais estreita, com menos crianças. A cidade tem <strong>menor proporção de fecundidade na área urbana</strong>. Alternativa <strong>A</strong>.</p><p>A pirâmide rural tem mais homens que mulheres, e não menos (B).</p>",
  figs(("q24", "Duas pirâmides etárias por sexo, de 1991 (linha preta) e 2010 (linha cinza). Na urbana, a base fica estreita em 2010 e há mais mulheres que homens nas idades mais altas. Na rural, a base é mais larga e há mais homens que mulheres na maior parte das faixas.")),
  ["pirâmide etária", "fecundidade"], enun="[[fig:1]]" + fonte("BRASIL. IBGE. <em>Censo demográfico 1991-2010</em>. Rio de Janeiro, 2011.") + p(T(24, 5)))
X(25, "Filosofia", "Filosofia antiga", "<p>Platão aceita de Parmênides que o objeto do conhecimento é racional, e não sensível, e privilegia o racional. Ele afirma <strong>que a razão é capaz de gerar conhecimento, mas a sensação não</strong>: os sentidos só dão opinião. Alternativa <strong>D</strong>.</p><p>Para Parmênides, a razão é superior aos sentidos, e não o contrário (E).</p>",
  tags=["Platão", "Parmênides"], enun=ap(T(25, 0)) + fonte(T(25, 1).replace("Platão e Aristóteles", "<em>Platão e Aristóteles</em>")) + p(T(25, 2) + " " + T(25, 3)))
X(26, "Geografia", "Questões ambientais", "<p>Os motores a combustão queimam derivados de petróleo e emitem gás carbônico, que agrava o efeito estufa e o aquecimento global, com o <strong>derretimento das calotas polares</strong>. Uma medida para reduzir esse uso é o <strong>incentivo aos transportes de massa</strong>, que levam mais gente por litro de combustível. Alternativa <strong>C</strong>.</p><p>Remédios grátis (D) tratam o efeito, sem reduzir o consumo.</p>",
  tags=["combustíveis fósseis", "transporte coletivo"], trocas=[("Energia: o vício da civilização", "<em>Energia: o vício da civilização</em>")])
X(27, "Geografia", "Questão agrária", "<p>As quebradeiras lutam “pela libertação dos babaçuais” e pela terra: as palmeiras ficam dentro de fazendas cercadas, e o acesso ao coco é negado. O movimento resulta da <strong>dificuldade imposta pelos fazendeiros e posseiros no acesso aos babaçuais localizados no interior de suas propriedades</strong>. Alternativa <strong>E</strong>.</p><p>O texto diz que elas têm, sim, identidade coletiva (B).</p>",
  tags=["quebradeiras de coco", "movimentos sociais"],
  enun=ap("As mulheres quebradeiras de coco-babaçu dos " + T(27, 1)) + fonte(T(27, 2)) + p(T(27, 3)))
X(28, "Filosofia", "Filosofia antiga", "<p>Anaxímenes diz que o ar é o elemento originário de tudo; Basílio diz que Deus está no princípio do mundo. As explicações são diferentes, mas ambas <strong>postulavam um princípio originário para o mundo</strong>. Alternativa <strong>D</strong>.</p><p>Só Basílio coloca Deus como princípio (E).</p>",
  tags=["arché", "pré-socráticos"], trocas=[("A aurora da filosofia grega", "<em>A aurora da filosofia grega</em>"), ("História da Filosofia Cristã", "<em>História da Filosofia Cristã</em>"), ("transformase", "transforma-se")])
X(29, "Geografia", "Geologia", "<p>Terremotos acontecem quando a tensão acumulada nas rochas, sobretudo nos limites entre placas, é liberada de repente. Atingem com força quem vive perto das áreas de <strong>alívio da tensão geológica</strong>. Alternativa <strong>A</strong>.</p><p>Erosão, intemperismo e sedimentação (B, C e E) são processos lentos da superfície.</p>",
  tags=["terremotos", "tectônica de placas"], trocas=[("ComCiência", "<em>ComCiência</em>")])
X(30, "Filosofia", "Filosofia moderna", "<p>Descartes desconfia dos sentidos, que “já nos enganaram”; Hume diz que uma ideia só tem sentido se derivar de uma impressão sensorial. Um racionalista e um empirista: eles <strong>atribuem diferentes lugares ao papel dos sentidos no processo de obtenção do conhecimento</strong>. Alternativa <strong>E</strong>.</p><p>O criticismo (C) é a posição de Kant.</p>",
  tags=["racionalismo", "empirismo"], trocas=[("Meditações Metafísicas", "<em>Meditações Metafísicas</em>"), ("Uma investigação sobre o entendimento", "<em>Uma investigação sobre o entendimento</em>")])
X(31, "Filosofia", "Renascimento", "<p>Maquiavel aceita que a sorte decida metade dos nossos atos, mas diz que o livre-arbítrio controla a outra metade: o homem não está entregue a Deus e ao acaso. Ele demonstra o vínculo com o humanismo ao <strong>afirmar a confiança na razão autônoma como fundamento da ação humana</strong>. Alternativa <strong>C</strong>.</p><p>Ele não rejeita o acaso por completo (B): limita-o a uma parte.</p>",
  tags=["Maquiavel", "fortuna"], trocas=[("O Príncipe. Brasília", "<em>O Príncipe</em>. Brasília"), ("Em O Príncipe", "Em <em>O Príncipe</em>")])
X(32, "Geografia", "Clima", "<p>Uma sociedade fica mais vulnerável ao clima quanto mais depende de atividades sujeitas a ele, como a agricultura, a pecuária e o extrativismo. Ela é mais vulnerável quando <strong>concentra suas atividades no setor primário</strong>. Alternativa <strong>A</strong>.</p><p>Estoques, transportes, diversificação da energia e tecnologia (B a E) reduzem a vulnerabilidade.</p>",
  tags=["vulnerabilidade", "setor primário"], trocas=[("Introdução a climatologia para os trópicos", "<em>Introdução à climatologia para os trópicos</em>")])
X(33, "Geografia", "Globalização", "<p>As empresas espalham cada atividade onde for mais vantajoso: sede num lugar, fábrica em outro, executivos em outro. Com isso, as pessoas precisam mudar de lugar e de função conforme as empresas se movem: há <strong>aumento da mobilidade ocupacional</strong>. Alternativa <strong>B</strong>.</p><p>As empresas buscam impostos menores, o que pressiona a carga tributária para baixo (A).</p>",
  tags=["empresas transnacionais", "trabalho"], trocas=[("A corrida para o século XXI: no loop da montanha russa", "<em>A corrida para o século XXI: no loop da montanha-russa</em>")])
X(34, "Geografia", "Amazônia", "<p>Da colônia até o século XIX, a ocupação seguiu de leste a oeste pelos rios, como o Amazonas, que eram as vias de circulação. Formaram-se <strong>povoados interligados próximos a grandes rios</strong>. Alternativa <strong>E</strong>.</p><p>As faixas ao longo das estradas (D) são do segundo eixo, Sul-Norte, a partir dos anos 1960.</p>",
  tags=["ocupação da Amazônia", "rios"], trocas=[("Jornal Mundo", "<em>Jornal Mundo</em>")])
X(35, "História", "Brasil Colônia", "<p>O governador diz que os índios nunca confiam nos brancos, nem os “civilizados”. Os aldeamentos pombalinos reuniam os indígenas sob controle do Estado, para integrá-los à economia colonial como trabalhadores: havia <strong>necessidade de controle dos brancos sobre a população indígena, objetivando sua adaptação às exigências do trabalho regular</strong>. Alternativa <strong>E</strong>.</p><p>Pombal incentivou a miscigenação (D) e expulsou os jesuítas (C).</p>",
  tags=["política pombalina", "aldeamentos"], trocas=[("Aldeamentos indígenas", "<em>Aldeamentos indígenas</em>")])
X(36, "Geografia", "Indústria", "<p>Para a indústria se espalhar para outras regiões sem perder o controle a partir dos centros, era preciso comunicar-se rapidamente entre sedes e fábricas. Um fator que contribuiu foi o <strong>desenvolvimento dos meios de comunicação</strong>. Alternativa <strong>E</strong>.</p><p>A desconcentração foi estimulada por incentivos fiscais, e não pela eliminação deles (C).</p>",
  tags=["desconcentração industrial", "meio técnico-científico"], trocas=[("O Brasil: território e sociedade no início do século XXI", "<em>O Brasil: território e sociedade no início do século XXI</em>")])
X(37, "Geografia", "Geologia", "<p>Os escudos cristalinos são formados por rochas antigas, magmáticas e metamórficas, com intrusões de granito, onde se formaram jazidas como as de ferro e manganês de Carajás e da Serra do Navio. Eles se destacam por <strong>apresentarem áreas de intrusões graníticas, ricas em jazidas minerais</strong>. Alternativa <strong>A</strong>.</p><p>Petróleo e gás (D) estão em bacias sedimentares, e não em terrenos cristalinos.</p>",
  tags=["escudos cristalinos", "recursos minerais"], trocas=[("Geografia do Brasil", "<em>Geografia do Brasil</em>")])
X(38, "Geografia", "Recursos hídricos", "<p>Para irrigar grandes lavouras, retira-se muita água dos rios, com canais, barragens e desvios, como na transposição do São Francisco. Isso altera o curso natural das águas e gera disputas com outros usos: um impacto é o <strong>redirecionamento dos cursos fluviais</strong>. Alternativa <strong>E</strong>.</p><p>A redução de custos (A) é um efeito econômico, e não um impacto socioambiental.</p>",
  tags=["irrigação", "uso da água"], trocas=[("O desencanto da terra", "<em>O desencanto da terra</em>")])
X(39, "Geografia", "Espaço rural", "<p>Na Europa do século XIX, os camponeses perderam a terra e viraram trabalhadores volantes; hoje, o agronegócio expande a fronteira agrícola e muda o controle da terra. Nos dois casos, as mudanças <strong>desorganizam o modo tradicional de vida impelindo-as à busca por melhores condições no espaço urbano ou em outros países</strong>. Alternativa <strong>E</strong>.</p><p>A alternativa D descreve a mudança técnica, mas não o efeito sobre a população local.</p>",
  tags=["êxodo rural", "agronegócio"], trocas=[("Política e colonização no Império", "<em>Política e colonização no Império</em>"), ("Enciclopédia Contemporânea da América Latina e do Caribe", "<em>Enciclopédia Contemporânea da América Latina e do Caribe</em>")],
  alts={**D[39]["alternativas"], "E": "desorganizam o modo tradicional de vida impelindo-as à busca por melhores condições no espaço urbano ou em outros países em situações muitas vezes precárias."})
X(40, "História", "Brasil Colônia", "<p>Vieira compara o sofrimento no engenho à Paixão de Cristo: noites sem dormir, fome, ferros, açoites e chagas. Ele se dirige aos escravizados e lhes promete que, com paciência, terão o merecimento do martírio. A relação é com <strong>o trabalho dos escravos na produção de açúcar</strong>. Alternativa <strong>E</strong>.</p><p>O sermão justifica o sofrimento pela religião, em vez de condenar a escravidão.</p>",
  tags=["Padre Vieira", "engenho"], trocas=[("Sermões", "<em>Sermões</em>")])
X(41, "História", "Era Vargas", "<p>O documento diz que o sindicalismo do Estado Novo foge à luta de classes e é “instrumento de harmonia e de cooperação entre o capital e o trabalho”. É o corporativismo, que <strong>orienta a busca do consenso entre trabalhadores e patrões</strong>, sob a tutela do Estado. Alternativa <strong>C</strong>.</p><p>Os conflitos não desapareceram (A): o Estado buscava controlá-los.</p>",
  tags=["corporativismo", "sindicalismo"], trocas=[("(1937- 1945)", "(1937-1945)"), ("Boletim do Ministério do Trabalho, Indústria e Comércio", "<em>Boletim do Ministério do Trabalho, Indústria e Comércio</em>")])
X(42, "Geografia", "Recursos hídricos", "<p>O consumo de água cresce mais rápido que a população, ou seja, cada pessoa usa cada vez mais. Para mudar essa lógica, é preciso usar a mesma água mais de uma vez: a <strong>ampliação de sistemas de reutilização hídrica</strong>. Alternativa <strong>A</strong>.</p><p>A irrigação por aspersão (B) aumenta o consumo.</p>",
  tags=["reúso da água", "consumo"], trocas=[("Decifrando a Terra", "<em>Decifrando a Terra</em>")])
X(43, "Geografia", "Migrações", "<p>A canção fala de quem vive andando pelo país, guardando as lembranças das terras por onde passou e dos amigos que deixou. Ela reflete a <strong>experiência de deslocamento vivenciada pelo migrante</strong>. Alternativa <strong>C</strong>.</p><p>A letra não fala da seca (B) nem de discriminação nas cidades (E).</p>",
  figs(("q43", "Trecho da letra de “A vida de viajante”, de Luiz Gonzaga e Hervê Cordovil, como aparece na prova: o eu lírico diz que vive andando pelo país, na esperança de um dia descansar feliz, guardando as recordações das terras e dos sertões por onde passou e dos amigos que deixou.")),
  ["migração nordestina", "música popular"], enun="[[fig:1]]" + fonte("GONZAGA, L.; CORDOVIL, H. <em>A vida de viajante</em>, 1953. Disponível em: www.recife.pe.gov.br. Acesso em: 20 fev. 2012 (fragmento).") + p(T(43, 2)))
X(44, "História", "Brasil Colônia", "<p>O francês se espanta ao ver o vice-rei obrigado a dançar e padres, mulheres, frades, cavalheiros e escravos dançando juntos na igreja. Nas festas religiosas coloniais, a devoção era vivida em conjunto e misturava camadas sociais: a festa <strong>afirmava um sentido comunitário de partilha da devoção</strong>. Alternativa <strong>D</strong>.</p><p>A festa não seguia a hierarquia romana (A): era justamente isso que estranhava.</p>",
  tags=["festas religiosas", "religiosidade popular"], trocas=[("Vice- Rei", "Vice-Rei"), ("Noveau Voyage autour du monde", "<em>Nouveau Voyage autour du monde</em>"), ("As festas no Brasil Colonial", "<em>As festas no Brasil Colonial</em>")])
X(45, "Geografia", "Espaço rural", "<p>Uma planta transgênica diz que os transgênicos iam acabar com a fome, e a outra responde que não está sabendo. A produção agrícola cresceu com a biotecnologia, mas a fome continuou: há <strong>expansão das terras agricultáveis, com manutenção de desigualdades sociais</strong>. Alternativa <strong>A</strong>.</p><p>A fome não vem da falta de produção, mas da desigualdade no acesso aos alimentos.</p>",
  figs(("q45", "Charge: duas plantinhas conversam. Uma diz: “Oh, transgênico... dizem que está faltando alimento no mundo. Mas não tinham inventado um tipo de planta que ia acabar com a fome?”. A outra responde: “Ahn... não tô sabendo...”.")),
  ["transgênicos", "fome"])

completar(Q, R)
