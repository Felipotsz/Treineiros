# Enem 2017, 1º dia, caderno azul: Ciências Humanas (questões 46 a 90; no site, 1 a 45).
# Texto legível (sem DECOD). Quadros das Q54 e Q87 (Figura 2) em tabela HTML. Sem letras de música ou poemas modernos.
# Sem anuladas nesta área.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, enunciado_enem, paragrafos_enem

ID = "enem-2017-humanas"
META = {"id": ID, "banca": "Enem", "ano": 2017, "titulo": "Enem 2017: Ciências Humanas", "fonte": "Inep", "dataExame": "2017-11-05",
        "duracaoMinutos": 135, "area": "Ciências Humanas", "caderno": "azul", "dia": 1}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2017-dia1-azul")
Q = {}
P = lambda n: paragrafos_enem(D[n])
T = lambda n, i: P(n)[i][1]
p = lambda *xs: "".join(f"<p>{x}</p>" for x in xs)
ap = lambda *xs: "".join(f'<p class="apoio">{x}</p>' for x in xs)
fonte = lambda x: f'<p class="fonte">{x}</p>'
ALT = lambda ini: {k: f"[[fig:{i}]]" for i, k in enumerate("ABCDE", ini)}
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


def tabela(cab, linhas):
    return ('<table class="tabela"><thead><tr>' + "".join(f"<th>{c}</th>" for c in cab) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in l) + "</tr>" for l in linhas) + "</tbody></table>")


X(46, "História", "África", "<p>Tombuctu ficava na borda sul do Saara, onde as caravanas que traziam sal do norte encontravam o ouro que vinha do sul. O provérbio citado (o sal vem do norte, o ouro do sul) mostra que a cidade era ponto de encontro de rotas comerciais e, por isso, também de livros e estudiosos. A explicação é sua <strong>posição relativa nas redes de circulação</strong>. Alternativa <strong>C</strong>.</p><p>A cidade não era isolada (A), e o tráfico transatlântico (D) é posterior e ligado à costa, não ao Sahel do século XIV.</p>",
  tags=["Mali", "comércio transaariano"], trocas=[("Desvendando a história da África", "<em>Desvendando a história da África</em>")])
X(47, "História", "Segunda Guerra Mundial", "<p>A Unesco reagiu, logo depois da guerra, às consequências das doutrinas racistas. O acontecimento recente ligado diretamente ao racismo foi o Holocausto: a <strong>execução de judeus e eslavos presos em guetos e campos de concentração nazistas</strong>, justificada pela ideia de superioridade racial. Alternativa <strong>D</strong>.</p><p>Pearl Harbor, a morte de soldados e as bombas atômicas (A, C e E) foram tragédias de guerra, mas não tinham fundamento racial.</p>",
  tags=["Holocausto", "racismo científico"])
X(48, "Filosofia", "Ética", "<p>Bentham é o pai do utilitarismo: a ação certa é a que produz “a maior quantidade de felicidade possível” para todos os afetados. A moral é julgada pelas consequências práticas, e não por regras abstratas ou pela vontade de Deus. É uma <strong>racionalidade de caráter pragmático</strong>. Alternativa <strong>D</strong>.</p><p>O texto rejeita expressamente a fidelidade a regras (B) e a moral religiosa (C).</p>",
  tags=["utilitarismo", "Bentham"])
X(49, "História", "Iluminismo", "<p>A Declaração dos Direitos do Homem e do Cidadão afirma que os homens nascem livres e iguais em direitos. O texto liga essa declaração ao Iluminismo, que defendia direitos naturais válidos para todos: a <strong>universalização do princípio da igualdade civil</strong>. Alternativa <strong>E</strong>.</p><p>O Iluminismo criticava a moral religiosa (B) e os privilégios aristocráticos (C).</p>",
  tags=["Revolução Francesa", "direitos do homem"], trocas=[("O Iluminismo e os reis filósofos", "<em>O Iluminismo e os reis filósofos</em>")])
X(50, "Geografia", "Questão indígena", "<p>O artigo 231 garante aos indígenas as terras que tradicionalmente ocupam. Para esses povos, a terra é a base da organização social, das crenças e do modo de vida: sem território, a cultura não se mantém. A luta pela demarcação vincula <strong>espaço e sobrevivência cultural</strong>. Alternativa <strong>C</strong>.</p><p>A Constituição reconhece a diferença cultural, e não a miscigenação (A) ou a modernização econômica (E).</p>",
  tags=["demarcação de terras", "Constituição de 1988"])
X(51, "História", "Brasil Império", "<p>Na foto, a ama de leite Mônica, uma escravizada, posa ao lado do menino que amamentou, bem-vestida e com a mão sobre ele. Ela convivia de perto com a família senhorial, criava os filhos dos senhores, mas continuava escravizada. A foto expressa a <strong>ambiguidade do trabalho doméstico exercido pela ama de leite, desenvolvendo uma relação de proximidade e subordinação em relação aos senhores</strong>. Alternativa <strong>A</strong>.</p><p>A roupa da foto era encenação do status da família, não sinal de melhoria de vida dos escravizados (C).</p>",
  figs(("q51", "Fotografia antiga, em preto e branco: uma mulher negra, sentada, com vestido escuro e longo, tem ao lado um menino branco, de pé, com a mão dela pousada sobre ele.")),
  ["escravidão doméstica", "ama de leite"], trocas=[("Amas mercenárias", "<em>Amas mercenárias</em>")])
X(52, "Geografia", "Urbanização", "<p>O texto descreve um centro rico, com empregos e serviços, cercado por uma periferia de população pobre e com acesso restrito a eles. A separação das classes sociais em áreas diferentes da cidade é a <strong>segregação socioespacial</strong>. Alternativa <strong>D</strong>.</p><p>Não se trata de verticalização (A) nem de criação de municípios (C).</p>",
  tags=["periferia", "Distrito Federal"], trocas=[("Migração e ambiente nas aglomerações urbanas", "<em>Migração e ambiente nas aglomerações urbanas</em>")])
X(53, "Geografia", "Blocos econômicos", "<p>Ao zerar tarifas de 90% dos produtos entre si, os países da Aliança do Pacífico baratearam insumos e ganharam escala, formando um bloco voltado ao comércio com a Ásia. O objetivo é <strong>fomentar a competitividade no mercado externo</strong>. Alternativa <strong>B</strong>.</p><p>O acordo trata de mercadorias, não da circulação de trabalhadores (A), e busca atrair investimentos, não restringi-los (C).</p>",
  tags=["Aliança do Pacífico", "integração regional"])
X(54, "Geografia", "Hidrografia", "<p>Pela tabela, nas bacias com florestas 80% a 100% da chuva fica retida no local e só 0% a 20% escoa. A água retida infiltra no solo e abastece os lençóis subterrâneos: a vegetação favorece a <strong>recarga dos aquíferos</strong>. Alternativa <strong>E</strong>.</p><p>Erosão e enchentes (A e C) dependem do escoamento, que é maior nas áreas urbanas.</p>",
  tags=["infiltração", "escoamento superficial"],
  enun=tabela(["Tipologia de área", "% de chuva retida no local", "% de chuva escoada"], [["Bacias naturais/florestas", "80 a 100", "0 a 20"], ["Bacias com ocupação agrícola/cultivos", "40 a 60", "40 a 60"], ["Bacias com ocupação residencial", "40 a 50", "50 a 60"], ["Bacias com ocupação urbana pesada", "0 a 10", "90 a 100"]])
       + fonte(T(54, 1).replace("Introdução à hidrogeografia", "<em>Introdução à hidrogeografia</em>")) + p(T(54, 2)))
X(55, "Geografia", "Solos", "<p>A lixiviação retira do solo nutrientes como cálcio, magnésio e potássio, que são bases, e o texto diz que eles são substituídos por elementos tóxicos como o alumínio. Com menos bases e mais alumínio, o solo fica mais ácido: há <strong>elevação da acidez</strong>. Alternativa <strong>A</strong>.</p><p>Voçorocas e remoção da camada superior (C e D) são erosão, outro processo.</p>",
  tags=["lixiviação", "acidez do solo"], trocas=[("Formação e conservação dos solos", "<em>Formação e conservação dos solos</em>")])
X(56, "Geografia", "Transportes", "<p>O problema descrito são as filas de navios, caminhões e trens à espera para embarcar a soja. Faltam terminais nos portos para carregar os navios: a solução é a <strong>construção de terminais atracadouros</strong>. Alternativa <strong>B</strong>.</p><p>Isentar impostos ou mudar de parceiros comerciais (A e C) não reduz as filas.</p>",
  tags=["logística", "exportação de soja"])
X(57, "Geografia", "Globalização", "<p>Os países desenvolvidos se desindustrializam, transferindo fábricas para outros países, mas não perdem o comando da economia. Eles mantêm os serviços avançados: pesquisa, finanças, projeto e gestão. O resultado é a <strong>consolidação do domínio tecnológico</strong>. Alternativa <strong>D</strong>.</p><p>A desindustrialização não satura o setor secundário (A) e não divide o poder em dois polos (C).</p>",
  tags=["divisão internacional do trabalho", "setor terciário"], trocas=[("Olhares geográficos", "<em>Olhares geográficos</em>")])
X(58, "Sociologia", "Diversidade cultural", "<p>Numa sociedade com várias etnias, a democracia precisa garantir os mesmos direitos a todos e, ao mesmo tempo, aceitar que os grupos mantenham suas culturas. Ela demanda <strong>universalização de direitos e respeito à diversidade</strong>. Alternativa <strong>B</strong>.</p><p>As outras propõem homogeneizar ou segregar (A, C, D e E), o que contraria o pluralismo democrático.</p>",
  tags=["multiculturalismo", "democracia"], trocas=[("Sociologia. Porto", "<em>Sociologia</em>. Porto")])
X(59, "Geografia", "Climatologia", "<p>No climograma, as temperaturas ficam abaixo de 0 °C de novembro a março, chegando a −10 °C, e acima de 15 °C só no verão (junho a agosto). Os invernos muito frios e a grande amplitude térmica, com verão no meio do ano, indicam o Hemisfério Norte e alta latitude: <strong>Moscou</strong>. Alternativa <strong>E</strong>.</p><p>Cidade do Cabo e Sydney estão no Hemisfério Sul, com verão no fim do ano (A e B); Mumbai e Barcelona não têm temperaturas negativas (C e D).</p>",
  figs(("q59a", "Climograma: barras de pluviosidade entre 15 e 45 mm por mês, maiores em junho e julho; a linha de temperatura começa em cerca de −8 °C em janeiro, sobe até perto de 18 °C em julho e volta a cerca de −7 °C em dezembro."),
       ("q59b", "Mapa-múndi com as cidades Moscou, Barcelona, Mumbai, Cidade do Cabo e Sydney.")),
  ["climograma", "clima continental"],
  enun=p("<strong>Figura 1</strong>") + "[[fig:1]]" + p("<strong>Figura 2</strong>") + "[[fig:2]]" + fonte(T(59, 4)) + p(T(59, 5)))
X(60, "Sociologia", "Desenvolvimento", "<p>Amartya Sen diz que o desenvolvimento é a expansão das liberdades reais das pessoas. O crescimento do PIB é um meio, mas as liberdades dependem também de serviços de educação e saúde e de direitos civis. O vínculo é entre <strong>garantia da cidadania e ascensão econômica</strong>. Alternativa <strong>D</strong>.</p><p>Indústria, impostos e incentivos (A, C e E) são justamente as visões restritas que o texto critica.</p>",
  tags=["Amartya Sen", "liberdade"], trocas=[("Desenvolvimento como liberdade", "<em>Desenvolvimento como liberdade</em>")])
X(61, "História", "Mundo pós-Guerra Fria", "<p>Depois do fim da URSS, os Estados Unidos ficaram como única superpotência. Na Guerra do Golfo e na reação ao 11 de Setembro, mostraram capacidade de agir militarmente em qualquer parte do mundo, apoiados numa rede de <strong>bases militares espalhadas ao redor do mundo</strong>. Alternativa <strong>A</strong>.</p><p>A China não entrou na Otan (E), e o Irã não é aliado dos EUA (D).</p>",
  tags=["unipolaridade", "Estados Unidos"], trocas=[("Globalização, democracia e terrorismo", "<em>Globalização, democracia e terrorismo</em>")])
X(62, "História", "Crise de 1929", "<p>O <em>New Deal</em>, de Roosevelt, respondeu à Grande Depressão com controle de preços e da produção, valorização de salários e regras para o emprego. O Estado passou a intervir na economia para reativar o mercado interno: o objetivo era <strong>recompor os mecanismos de acumulação econômica por meio da intervenção estatal</strong>. Alternativa <strong>E</strong>.</p><p>Flexibilizar o mercado (A) é o oposto do que o <em>New Deal</em> fez.</p>",
  tags=["New Deal", "keynesianismo"], trocas=[("O New Deal visa", "O <em>New Deal</em> visa"), ("História geral das civilizações", "<em>História geral das civilizações</em>")])
X(63, "História", "Vanguardas", "<p>Marinetti manda queimar bibliotecas, inundar museus e derrubar as cidades antigas. O passado é visto como peso a ser destruído para dar lugar ao novo. O princípio é que <strong>a modernidade é a superação decisiva da história</strong>. Alternativa <strong>C</strong>.</p><p>O texto ataca a tradição e a memória (A, B e E), em vez de valorizá-las.</p>",
  tags=["Futurismo", "Marinetti"], trocas=[("Manifesto futurista", "<em>Manifesto futurista</em>")])
X(64, "Filosofia", "Filosofia política", "<p>Rawls fala de pessoas que aceitam regras comuns e de uma sociedade regulada por uma concepção pública de justiça, que todos aceitam e sabem que os outros aceitam. A ideia retoma o liberalismo moderno: indivíduos livres que se dão as próprias regras. É <strong>a relação entre liberdade e autonomia do Liberalismo</strong>. Alternativa <strong>A</strong>.</p><p>Não há soberano absoluto (C) nem governo autocrata (D) no texto.</p>",
  tags=["Rawls", "justiça"], trocas=[("Uma teoria da justiça", "<em>Uma teoria da justiça</em>")])
X(65, "Filosofia", "Pré-socráticos", "<p>Demócrito é o filósofo do atomismo: tudo é formado por partículas indivisíveis, os átomos, que se combinam no vazio. Hegel compara essa ideia às “partículas” de Anaxágoras. Para Demócrito, o princípio constitutivo é o <strong>átomo, que explica o surgimento dos entes</strong>. Alternativa <strong>E</strong>.</p><p>Número, devir, água e imobilidade são os princípios de Pitágoras, Heráclito, Tales e Parmênides (A, B, C e D).</p>",
  tags=["Demócrito", "atomismo"], trocas=[("Os pré-socráticos: vida e obra", "<em>Os pré-socráticos: vida e obra</em>")])
X(66, "Filosofia", "Sócrates", "<p>O texto descreve a conversa de Sócrates, que leva o ouvinte a refletir sobre si mesmo e a perceber o que não sabe. Esse diálogo de perguntas e respostas é o <strong>método dialético</strong>. Alternativa <strong>B</strong>.</p><p>Sócrates buscava a verdade, não a relativizava (C), e criticava a retórica dos sofistas (D).</p>",
  tags=["maiêutica", "diálogo"], trocas=[("História da filosofia", "<em>História da filosofia</em>")])
X(67, "Sociologia", "Poderes do Estado", "<p>Com tribunais constitucionais controlando o que o governo e o Parlamento fazem, muitas questões políticas passam a ser decididas no Judiciário. No Brasil, o STF passou a julgar temas que seriam do Congresso: é a <strong>judicialização de questões próprias da esfera legislativa</strong>. Alternativa <strong>D</strong>.</p><p>O controle constitucional reforça os freios e contrapesos (C), não os suspende.</p>",
  tags=["judicialização da política", "STF"])
X(68, "Geografia", "Biomas", "<p>Árvores de troncos retorcidos, arbustos ásperos, solos ácidos e cupinzeiros são marcas do Cerrado, onde avançou a soja levada por gaúchos ao oeste da Bahia. O Cerrado tem vegetação tropófila (adaptada a uma estação seca e outra chuvosa) e clima tropical. Alternativa <strong>A</strong>.</p><p>Xerófila e semiárido (B) descrevem a Caatinga.</p>",
  tags=["Cerrado", "fronteira agrícola"])
X(69, "Geografia", "Indústria", "<p>O texto diz que a refinaria deve ficar perto dos centros de consumo e das áreas de produção. Isso exige transporte para receber petróleo e distribuir derivados: dutos, portos, rodovias. O fator determinante é a proximidade a <strong>espaços com infraestrutura de circulação</strong>. Alternativa <strong>E</strong>.</p><p>Importação de derivados (B) é o que a refinaria evita, e mão de obra (D) não é citada.</p>",
  tags=["refinarias", "fatores locacionais"])
X(70, "História", "Idade Média", "<p>A lã era procurada por compradores de Flandres e da Itália, regiões de manufatura têxtil nas cidades. O aperfeiçoamento da criação de ovelhas atendia ao comércio com esses centros: resultou do <strong>desenvolvimento da vida urbana</strong> na Baixa Idade Média. Alternativa <strong>B</strong>.</p><p>O trabalho no feudo era servil, não escravo (A).</p>",
  tags=["renascimento comercial", "Cister"], trocas=[("Economia rural e vida no campo no Ocidente medieval", "<em>Economia rural e vida no campo no Ocidente medieval</em>")])
X(71, "Geografia", "Energia", "<p>Belo Monte tem a segunda maior potência (11,2 mil MW), mas alaga só 0,5 mil km², menos que Itaipu (1,4), Tucuruí (3,5) ou Sobradinho (4,1). A vantagem é o <strong>reduzido espaço relativo inundado</strong>. Alternativa <strong>A</strong>.</p><p>A usina fica na Amazônia, longe de parques industriais e fronteiras (D e E).</p>",
  figs(("q71", "Infográfico “Ranking da eficiência”, que compara as dez maiores usinas do Brasil. Área alagada (mil km²) e potência (mil MW): Itaipu 1,4 e 14; Belo Monte 0,5 e 11,2; Tucuruí 3,5 e 8,7; Jirau 0,3 e 3,8; Ilha Solteira 1,2 e 3,4; Xingó 0,1 e 3,2; Santo Antônio 0,4 e 3,2; Marimbondo 0,4 e 1,4; Serra da Mesa 1,8 e 1,3; Sobradinho 4,1 e 1,1. Localização: PR, PA, PA, RO, SP e MS, AL e SE, RO, SP e MG, GO, BA.")),
  ["hidrelétricas", "Belo Monte"])
X(72, "Geografia", "Questões ambientais", "<p>O texto fala da perda de produtividade dos solos em áreas subúmidas e semiáridas, causada por desmatamento, superpastoreio e mineração, até que a vegetação não consegue se recompor. É a <strong>desertificação de ecossistemas</strong>. Alternativa <strong>E</strong>.</p>",
  tags=["desertificação", "degradação"], trocas=[("Novos caminhos da geografia", "<em>Novos caminhos da geografia</em>")])
X(73, "Geografia", "Migrações", "<p>Os migrantes passaram a ir mais para as cidades médias e menos para as metrópoles. Isso acompanha a saída de fábricas dos grandes centros para o interior e outras regiões, em busca de mão de obra mais barata e incentivos: a <strong>desconcentração da atividade industrial</strong>. Alternativa <strong>D</strong>.</p>",
  tags=["cidades médias", "fluxos migratórios"], trocas=[("Reflexões sobre os deslocamentos populacionais no Brasil", "<em>Reflexões sobre os deslocamentos populacionais no Brasil</em>")])
X(74, "Sociologia", "Participação política", "<p>A lei eleitoral brasileira obriga cada partido a reservar ao menos 30% das candidaturas para cada gênero. A medida busca reverter a sub-representação das mulheres no Legislativo: são as <strong>cotas de gênero nas candidaturas partidárias</strong>. Alternativa <strong>B</strong>.</p><p>A Lei Maria da Penha (A) combate a violência doméstica, não a sub-representação política.</p>",
  tags=["mulheres na política", "cotas"], trocas=[("Mulheres públicas", "<em>Mulheres públicas</em>")])
X(75, "Geografia", "Conflitos", "<p>A ONU elevou a Palestina a Estado observador não membro, um reconhecimento ao menos formal de que ela é um Estado. A resolução foi aprovada pela Assembleia Geral com o voto da maioria dos países: referendou o <strong>apoio da comunidade internacional à demanda nacional</strong> palestina. Alternativa <strong>D</strong>.</p><p>A resolução não definiu fronteiras (A) nem deu à Palestina os mesmos direitos de um Estado membro (E).</p>",
  tags=["Palestina", "ONU"])
X(76, "História", "Escravidão", "<p>Luiz Gama descreve a mãe, Luiza Mahin, como africana livre, altiva, que recusou o batismo cristão, trabalhava por conta própria e foi presa mais de uma vez por suspeita de envolvimento em revoltas de escravizados. São <strong>estratégias de resistência cultural</strong> à sociedade escravista. Alternativa <strong>B</strong>.</p><p>Ela rejeitou a religião imposta, em vez de ser dominada por ela (D).</p>",
  tags=["Luiz Gama", "Luiza Mahin"], trocas=[("A história contada", "<em>A história contada</em>")])
X(77, "Geografia", "Climatologia", "<p>De dia, a terra esquenta mais rápido que o mar: o ar sobre ela sobe (baixa pressão) e o vento sopra do mar para a terra, a brisa marinha. À noite, a terra esfria mais rápido, e o vento sopra da terra para o mar, o terral. As duas brisas vêm do <strong>aquecimento diferencial da superfície</strong>. Alternativa <strong>B</strong>.</p><p>Se a pressão fosse uniforme (A), não haveria vento.</p>",
  figs(("q77a", "Figura 1, formação da brisa marinha: a terra quente tem baixa pressão, e o ar sobe sobre ela; o mar morno tem alta pressão, e setas mostram o vento indo do mar para a terra."),
       ("q77b", "Figura 2, formação do terral: a terra fria tem alta pressão; o mar morno tem baixa pressão, e o ar sobe sobre ele; setas mostram o vento indo da terra para o mar.")),
  ["brisas", "pressão atmosférica"],
  enun=p("<strong>Figura 1</strong>") + "[[fig:1]]" + p("<strong>Figura 2</strong>") + "[[fig:2]]" + fonte(T(77, 6).replace("História ecológica da Terra", "<em>História ecológica da Terra</em>")) + p(T(77, 7)))
X(78, "História", "Era Vargas", "<p>A propaganda do Estado Novo, inspirada na nazista, buscava empolgar as multidões com mensagens de efeito, e o DIP controlava jornais e rádio. O objetivo era <strong>conquistar o apoio popular na legitimação do novo governo</strong>, uma ditadura sem eleições. Alternativa <strong>A</strong>.</p><p>Era uma ditadura: não buscava ampliar a participação nas decisões (B) nem a democracia (D).</p>",
  tags=["Estado Novo", "propaganda"], trocas=[("Repensando o Estado Novo", "<em>Repensando o Estado Novo</em>")])
X(79, "História", "Antiguidade clássica", "<p>Em Atenas, Sólon foi chamado para atender à pressão por terras e pelo fim das dívidas; em Roma, a Lei das Doze Tábuas tornou públicas as regras, limitando o arbítrio dos poderosos. Nos dois casos, a <strong>criação de normas coletivas diminuiu as desigualdades de tratamento</strong>. Alternativa <strong>E</strong>.</p><p>As leis não acabaram com as aristocracias nem com os conflitos (B e D); só os limitaram.</p>",
  tags=["Sólon", "Lei das Doze Tábuas"], trocas=[("Economia e sociedade na Grécia antiga", "<em>Economia e sociedade na Grécia antiga</em>"), ("Grécia e Roma. São Paulo", "<em>Grécia e Roma</em>. São Paulo")])
X(80, "História", "Brasil Império", "<p>A Lei de Terras de 1850 determinou que só se teria terra comprando-a. Libertos e pobres, sem dinheiro, ficaram de fora, e as terras continuaram nas mãos dos grandes proprietários. A lei acentuou a <strong>concentração fundiária</strong>. Alternativa <strong>C</strong>.</p><p>Ela dificultou, e não promoveu, a reforma agrária (A).</p>",
  tags=["Lei de Terras", "estrutura fundiária"], trocas=[("Geografia do Brasil", "<em>Geografia do Brasil</em>")])
X(81, "História", "Era Vargas", "<p>Em 1945, o queremismo (“Queremos Getúlio”) pedia que Vargas continuasse no poder e que uma Constituinte fosse convocada com ele no governo. O movimento buscava <strong>reivindicar a transição constitucional sob influência do governante</strong>. Alternativa <strong>D</strong>.</p><p>Não defendia manter a ditadura do Estado Novo (B), mas uma saída democrática conduzida por Vargas.</p>",
  tags=["queremismo", "redemocratização"], trocas=[("Getulismo e trabalhismo", "<em>Getulismo e trabalhismo</em>")])
X(82, "História", "República", "<p>Machado descreve Tiradentes como aquele que carregou os pecados dos outros, foi enforcado e esquartejado sozinho: uma imagem de Cristo. Ao mesmo tempo, o povo o escolheu como herói da pátria republicana. A narrativa associa <strong>redenção cristã e cultura cívica</strong>. Alternativa <strong>A</strong>.</p><p>Não há radicalismo militar nem regionalismo no texto (B e D).</p>",
  tags=["Tiradentes", "Machado de Assis"])
X(83, "História", "Ditadura militar", "<p>Os bispos acreditavam que a pobreza no campo facilitaria a pregação comunista entre os camponeses; por isso apoiaram o golpe, que prometia desenvolvimento. O entendimento era de que a <strong>manipulação ideológica é favorecida pela privação material</strong>. Alternativa <strong>E</strong>.</p><p>A Igreja não via no livre mercado a causa da luta de classes (A).</p>",
  tags=["Igreja Católica", "golpe de 1964"], trocas=[("A política do Brasil: lúmpen e místico", "<em>A política do Brasil: lúmpen e místico</em>")])
X(84, "Filosofia", "Filosofia política", "<p>Para Habermas, a decisão democrática só é legítima se vier depois de uma ampla discussão pública, em que os argumentos são pesados por todos. A inclusão depende do <strong>debate livre e racional entre cidadãos e Estado</strong>. Alternativa <strong>B</strong>.</p><p>Restringir o poder aos “mais esclarecidos” (E) exclui, em vez de incluir.</p>",
  tags=["Habermas", "democracia deliberativa"])
X(85, "Filosofia", "Ética", "<p>Kant manda testar se a máxima da ação pode virar lei universal. Se todos prometessem falsamente quando precisassem, ninguém mais acreditaria em promessas, e a própria máxima se destruiria. A falsa promessa <strong>opõe-se ao princípio de que toda ação do homem possa valer como norma universal</strong>. Alternativa <strong>C</strong>.</p><p>Justificar os meios pelos fins (D) e buscar a maior felicidade (E) são ideias que Kant rejeita.</p>",
  tags=["Kant", "imperativo categórico"], trocas=[("Fundamentação da metafísica dos costumes", "<em>Fundamentação da metafísica dos costumes</em>")])
X(86, "Geografia", "Geologia", "<p>O terremoto do Chile ocorreu na borda oeste da América do Sul, onde a placa de Nazca mergulha sob a Sul-Americana, região dos Andes, um dobramento moderno. Terremotos se concentram em <strong>estreitas faixas de intensidade sísmica, no contato das placas tectônicas, próximas a dobramentos modernos</strong>. Alternativa <strong>C</strong>.</p><p>Escudos cristalinos e centros de placas (D e E) são áreas estáveis.</p>",
  tags=["terremotos", "placas tectônicas"])
X(87, "Geografia", "Climatologia", "<p>Nesse dia, o Sul teve mínimas muito baixas (4 °C a 11 °C) e umidade de 90% a 100%; o litoral do Nordeste, também úmido, recebia ventos do oceano. Frio, umidade alta e chuva no Sul indicam a chegada de uma massa polar, e a umidade do litoral nordestino vem da massa tropical atlântica. O fator determinante são as <strong>massas de ar, que provocam precipitações</strong>. Alternativa <strong>C</strong>.</p><p>A umidade alta nessas regiões não se explica pelo relevo ou pela vegetação (A e B).</p>",
  figs(("q87", "Mapa do Brasil com as temperaturas mínimas de 28/08/2014: entre 22 °C e 24 °C no Norte e no Nordeste, 17 °C a 23 °C no Centro-Oeste e no Sudeste, e 4 °C a 11 °C no Sul.")),
  ["massas de ar", "umidade relativa"],
  enun=p("<strong>Figura 1</strong>") + "[[fig:1]]" + fonte(T(87, 2)) + p("<strong>Figura 2</strong>")
       + tabela(["Regiões", "Umidade relativa (intervalo médio)"], [["Norte", "60 - 70%"], ["Nordeste", "90 - 100%"], ["Centro-Oeste", "55 - 65%"], ["Sudeste", "65 - 75%"], ["Sul", "90 - 100%"]])
       + fonte(T(87, 5)) + p(T(87, 6)))
X(88, "Filosofia", "Filosofia antiga", "<p>Aristóteles diz que o sumo bem é estudado pela ciência “mais prestigiosa e que mais verdadeiramente pode ser chamada a arte mestra”: a política, que determina quais ciências devem ser estudadas na cidade e legisla sobre o que fazer. Para ele, <strong>a política é a ciência que precede todas as demais na organização da cidade</strong>. Alternativa <strong>C</strong>.</p><p>Aristóteles subordina o bem do indivíduo ao bem da cidade (A).</p>",
  tags=["Aristóteles", "sumo bem"], trocas=[("Ética a Nicômaco", "<em>Ética a Nicômaco</em>")], alts={**D[88]["alternativas"], "B": D[88]["alternativas"]["B"]})
X(89, "Sociologia", "Cultura de massa", "<p>A tecnologia permite traçar o perfil de interesses de cada usuário e usar a oferta como “isca” para o desejo de consumo. Com isso, a propaganda passa a mostrar a cada pessoa o que combina com ela: a <strong>individualização das mensagens publicitárias</strong>. Alternativa <strong>D</strong>.</p>",
  tags=["publicidade", "internet"], trocas=[("Culturas e artes do pós-humano", "<em>Culturas e artes do pós-humano</em>")])
X(90, "História", "Ditadura militar", "<p>Zuzu Angel, estilista, levou para a moda elementos do cangaço, como o chapéu de couro de Maria Bonita. Depois que seu filho foi morto pela ditadura, em 1971, usou as roupas para denunciar o regime. Sua obra se dedicou à <strong>criação de uma estética de resistência</strong>. Alternativa <strong>E</strong>.</p><p>Ela valorizava o folclore nordestino (B) e a mulher forte do cangaço, não a representação tradicional (A).</p>",
  figs(("q90a", "Figura 1: foto antiga de Maria Bonita, de chapéu de couro com abas largas e vestido estampado."),
       ("q90b", "Figura 2: modelo com uma roupa da coleção de Zuzu Angel: chapéu de abas largas, como os do cangaço, conjunto estampado e botas.")),
  ["Zuzu Angel", "moda e política"],
  enun="[[fig:1]][[fig:2]]" + fonte("ABRAÃO, B. Disponível em: www.brasilcult.pro.br. Acesso em: 18 maio 2013 (Figura 1). Disponível em: www.zuzuangel.com.br. Acesso em: 18 maio 2013 (Figura 2).") + p(T(90, 6)))

completar(Q, R)
