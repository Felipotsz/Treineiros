# Ajustes da conferência humana: Vestibular FATEC 1º semestre de 2026 (exame de 14/12/2025)
# Texto conferido com a imagem de cada página. Tema implícito: ciência e tecnologia.
# 60 questões; a prova tem 5 h no total, incluindo a redação (que fica fora do simulado).
# Matéria: a do gabarito oficial; nas "Multidisciplinar", a matéria principal + tag "multidisciplinar".
# O rascunho embaralhou as páginas 11, 15, 16, 17 e 18 (Q29-31, Q41-48, Q51): refeitas à mão.
# Letra de canção (Q29-30) como imagem; o alt descreve sem transcrever.
# Gabarito: oficial (1SEM26), sem anuladas, conferido com resolução própria nas 60.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import A, carregar, enun, tabela, colunas, completar, trecho

ID = "fatec-2026-1sem"
META = {
    "id": ID,
    "banca": "FATEC",
    "ano": 2026,
    "semestre": 1,
    "titulo": "Vestibular FATEC, 1º semestre de 2026",
    "fonte": "Centro Paula Souza",
    "dataExame": "2025-12-14",
    "duracaoMinutos": 300,
    "tema": "Ciência e tecnologia",
    "pdf": f"assets/provas/{ID}.pdf",
}

R = carregar(ID)
MULTI = ["multidisciplinar"]


def p(*paragrafos, classe=None):
    abre = f'<p class="{classe}">' if classe else "<p>"
    return "".join(abre + x + "</p>" for x in paragrafos)


def apoio(*paragrafos):
    return '<p class="apoio">' + A.join(paragrafos) + "</p>"


def fonte(t):
    return f'<p class="fonte">{t}</p>'


def url(u, data, extra="Adaptado."):
    return fonte(f"&lt;{u}&gt; Acesso em: {data}." + (" " + extra if extra else ""))


def chamada(t):
    return f'<p class="chamada">{t}</p>'


def figs(*pares):
    return [{"arquivo": a, "alt": t} for a, t in pares]


# ---------- textos compartilhados ----------
CODIGO = (chamada("Leia o texto para responder às questões 09 e 10.")
          + apoio("Código de barras lineares é formado por barras pretas e brancas paralelas. Para sua leitura, são utilizados “leitores ópticos”. Esses leitores utilizam um LED o qual emite feixes de luz, geralmente vermelha ou infravermelha, que, ao refletir, é captada por um fotodiodo e convertida em corrente elétrica. Essa corrente é amplificada e transformada em sinal digital (0 e 1) de acordo com as barras, que são decodificadas por um algoritmo no processador acoplado ao leitor óptico."))
P9 = p("Com base nessas informações, é correto afirmar que")

PEPINOS = (chamada("Leia o quadrinho para responder às questões 25 e 26.") + "[[fig:1]]"
           + url("https://tinyurl.com/45wd4hf5", "11.09.2025", "Original colorido."))
PEPINOS_IMG = figs(("q25", "Quadrinho à beira de uma piscina. Um pepino sai da água e diz: “WHAT?”. Dois outros pepinos, um deles com uma toalha, olham para ele assustados e um comenta: “OH NO. THIS MUST BE ONE OF THOSE SALT-WATER POOLS”. O pepino que saiu da água está enrugado, com aparência de picles."))
P25 = p("Os pepinos acreditam que seu amigo, ao sair da piscina, está")

ROCKET = (chamada("Leia o texto para responder às questões 29 e 30.") + "[[fig:1]]"
          + url("https://tinyurl.com/2b5acwut", "13.09.2025", ""))
ROCKET_IMG = figs(("q29", "Trecho da letra da canção “Rocket man”, de Elton John, em inglês e em itálico, com seis versos e uma supressão. O astronauta diz que sente falta da Terra e da esposa e que se sente sozinho no espaço; depois, diz que Marte não é lugar para criar filhos, que lá faz um frio terrível (verso com a expressão “in fact”) e que não haveria ninguém para criá-los."))
P29 = p("Na última estrofe, a expressão <em>in fact</em> reforça que")

RODA = (chamada("Leia o texto para responder às questões 32 e 33.")
        + apoio("Foi inaugurada, em dezembro de 2022, na zona Oeste da cidade de São Paulo, a maior roda-gigante da América Latina, que tem 80 metros de diâmetro.")
        + url("https://tinyurl.com/36bcbr2x", "28.09.2025"))
P32 = p("O comprimento, em metros, de uma circunferência que possua diâmetro igual ao da roda gigante mencionada no texto é de")

PFAS = (chamada("Leia o texto para responder às questões 41 e 42.")
        + p("Os compostos perfluoralquilados e polifluoroalquilados (PFAS) são produzidos por meio da substituição dos átomos de hidrogênio da cadeia carbônica pelo elemento mais eletronegativo conhecido.",
            "Considere as fórmulas estruturais de dois compostos orgânicos, dos quais apenas um deles pertence ao grupo dos PFAS.")
        + "[[fig:1]]")
PFAS_IMG = figs(("q41", "Duas fórmulas estruturais. À esquerda, uma cadeia de três carbonos ligada a um grupo COOH: o primeiro carbono tem um Cl à esquerda, um OH em cima e um Cl embaixo; o segundo tem Cl em cima e embaixo; o terceiro tem H em cima e embaixo. À direita, uma cadeia de três carbonos ligada a um grupo COOH em que todas as outras posições são ocupadas por F: o primeiro carbono tem F à esquerda, em cima e embaixo; o segundo e o terceiro têm F em cima e embaixo."))
P41 = p("Assinale a alternativa que contém o valor aproximado da porcentagem em massa de carbono do composto orgânico que pertence ao grupo dos PFAS.",
        "Massas molares em g/mol:", "C = 12; H = 1; O = 16; F = 19; Cℓ = 35,5; N = 14")

BALEIAS = (chamada("Leia o texto para responder às questões de 46 a 48.")
           + p("Em 1967, pesquisadores descobriram que jubartes machos emitem complexos padrões sonoros durante o cortejo de fêmeas. Cada canção dura até meia hora e é entoada por um grupo inteiro de uma só vez. As gravações dos cantos foram lançadas em LP com o título <em>Songs of the Humpback Whale</em>, em 1970, e ajudaram a impulsionar o movimento conservacionista. Entenda no infográfico mais sobre essas músicas.")
           + "[[fig:1]]" + url("https://tinyurl.com/uj53au", "30.08.2025"))
BALEIAS_IMG = figs(("q46", "Infográfico “A construção de uma música”: a unidade é um som individual; somadas, as unidades formam frases, que se agrupam em blocos maiores, os temas, e cada tema segue um padrão de repetições. Unidades: quadrado, estrela, triângulo, losango, círculo, hexágono e barra dupla. Frase: quadrado, triângulo, círculo, barra dupla. Tema: essa frase repetida 3 vezes. Música, formada por quatro temas, cada um com uma frase repetida 3 vezes. Tema 1: quadrado, triângulo, círculo, barra dupla. Tema 2: hexágono, barra dupla, barra dupla, losango. Tema 3: quadrado, estrela, triângulo, estrela. Tema 4: estrela, losango, círculo, hexágono."))
P46 = p("Suponha que uma canção, cuja duração máxima está indicada no texto, seja composta pelo encadeamento sequencial do Tema 2 e do Tema 3, nessa ordem. Considere a duração de cada unidade, em segundos, como:")
P46 += (tabela(["⬢", "‖", "◆", "●", "★", "■", "▲"], [["6 s", "4 s", "1 s", "8 s", "5 s", "3 s", "2 s"]])
        + p("Logo, a quantidade de vezes que cada um dos temas se repetirá completamente nessa canção é"))

TIRINHA = (chamada("Leia a tirinha para responder às questões 52 e 53.") + "[[fig:1]]"
           + url("https://tinyurl.com/59ts9bxu", "14.09.2025", "Original colorido."))
TIRINHA_IMG = figs(("q52", "Tirinha em quatro quadros com dois cachorros, um pug e um bassê. 1: “Para acreditarem em uma mentira, ela tem que estar envolta de verdades.”, com o desenho de uma bolinha escrita “mentira” embrulhada numa massa escrita “verdades”. 2: “É como dar remédio para cães.”: alguém joga petiscos, e os dois cães olham animados. 3: “Alguns conseguem identificar o conteúdo suspeito.”: o bassê cospe o comprimido. 4: “Já outros...”: o pug, de olhos arregalados, diz: “Você sabia que pulgas illuminatis colocam chips em nós quando nos mordem?”, e o bassê o olha desconfiado."))
P52 = p("Na tirinha, o autor se vale de uma comparação para")

MEME = (chamada("Leia o <em>meme</em> para responder às questões 54 e 55.") + "[[fig:1]]"
        + url("https://tinyurl.com/4h8xdakw", "14.09.2025", "Original colorido."))
MEME_IMG = figs(("q54", "Meme com a foto de uma árvore grande e isolada num campo, com o símbolo de sinal de Wi-Fi ao lado. Texto em cima: “Imagine se árvores dessem Wi-Fi. Estaríamos plantando como loucos.” Texto embaixo: “É uma pena que elas apenas dão o oxigênio que respiramos.”"))
P54 = p("Na frase “É uma pena que elas apenas dão o oxigênio que respiramos.”, ocorre a figura de linguagem chamada")

VACINAS = (chamada("Leia o texto e o infográfico para responder às questões 56 e 57.")
           + p("Na pesquisa <em>Noções sobre a Ciência</em>, de 2023, foi mensurado o nível de familiaridade dos entrevistados com noções elementares de Ciência. Os dados refletem a necessidade de se ampliarem políticas de disseminação de conhecimentos científicos, visando reforçar a educação científica da população.")
           + "[[fig:1]]" + url("https://tinyurl.com/3ra4ded4", "14.09.2025"))
VACINAS_IMG = figs(("q56", "Infográfico: resultado da pesquisa Noções sobre a Ciência para a afirmação “algumas vacinas podem causar autismo”. Gráfico de rosca com uma seringa no centro. Concordo em partes: 14%. Concordo totalmente: 21%. Discordo em partes: 12%. Discordo totalmente: 36%. Não responderam (NR): 0%. Não souberam (NS): 17%."))
P56 = p("A partir do texto e do infográfico, afirma-se corretamente que")

DEEP = (chamada("Leia o texto para responder às questões 59 e 60.")
        + apoio("As startups do tipo <em>deep techs</em> são empresas inovadoras que objetivam fornecer soluções tecnológicas baseadas em conhecimentos científicos. Essas soluções buscam resolver problemas complexos e de alto impacto. Exemplos de <em>deep techs</em> podem ser encontrados nos segmentos de biotecnologia, em desenvolvimento de hardware e na adoção de inteligência artificial para resolver problemas complexos.")
        + url("https://tinyurl.com/5d42brfe", "14.09.2025"))
P59 = p("O texto apresentado tem por objetivo")

Q = {
1: {"materia": "Biologia", "assunto": "Genética", "tags": ["sistema ABO", "transfusão"],
    "enunciado": enun(R, 1, trocas=[("[[FIG:p02-1]]", tabela(["Grupo sanguíneo", "Aglutinogênio ou Antígeno (nas hemácias)", "Aglutinina ou Anticorpo (no plasma)"],
                                                             [["<strong><em>A</em></strong>", "<em>A</em>", "<em>anti-B</em>"], ["<strong><em>B</em></strong>", "<em>B</em>", "<em>anti-A</em>"],
                                                              ["<strong><em>AB</em></strong>", "<em>A</em> e <em>B</em>", "--"], ["<strong><em>O</em></strong>", "--", "<em>anti-A</em> e <em>anti-B</em>"]]))]),
    "explicacao": "<p>Quem é do grupo AB não tem anticorpos anti-A nem anti-B no plasma, então pode receber de todos. Mas suas hemácias têm os antígenos A e B, que seriam atacados pelos anticorpos de qualquer outro grupo. Por isso o AB <strong>só pode doar para AB</strong>. Alternativa <strong>C</strong>.</p><p>O grupo O tem anti-A e anti-B e só recebe de O (A). O AB recebe de todos, não só de O (B). O sangue A seria atacado pelo anti-A de quem é B (D). E quem é B tem anti-A, que atacaria as hemácias AB (E).</p>"},
2: {"materia": "Biologia", "assunto": "Botânica", "tags": ["fotossíntese", "ponto de compensação"],
    "enunciado": enun(R, 2, figs={"p02-2": 1}),
    "imagens": figs(("q02", "Gráfico “Ponto de compensação fótico”: taxa do processo em função da intensidade luminosa. A respiração celular é uma linha horizontal. A fotossíntese começa em zero, sobe em linha reta, cruza a linha da respiração e depois fica constante, acima dela. O cruzamento das duas linhas é o ponto de compensação fótico.")),
    "explicacao": "<p>Abaixo do PCF, a fotossíntese produz menos açúcar do que a respiração consome. A planta passa a gastar suas reservas e, se a situação durar muito, <strong>morre quando elas acabam</strong>. Alternativa <strong>A</strong>.</p><p>A respiração consome matéria orgânica, não produz (B). A planta não morre de imediato nem perde a capacidade de absorver nutrientes (C). Nutrientes do solo não substituem a fotossíntese como fonte de energia (D). E abaixo do PCF a fotossíntese produz menos, não mais, do que a respiração consome (E).</p>"},
3: {"materia": "Biologia", "assunto": "Genética", "tags": ["heredograma", "herança recessiva"],
    "enunciado": enun(R, 3, figs={"p03-1": 1}),
    "imagens": figs(("q03", "Heredograma. Geração 1: homem normal (1) e mulher normal (2). Filhos do casal: mulher normal (3), mulher com anomalia (4) e homem normal (5). O homem 5 se casa com a mulher normal 6, e eles têm um filho com anomalia (7).")),
    "explicacao": "<p>Os pais 1 e 2 são normais e têm uma filha afetada (4). Então a anomalia é recessiva, e os dois pais carregam o alelo sem manifestá-lo: <strong>são heterozigotos (Aa)</strong>. Alternativa <strong>B</strong>.</p><p>O indivíduo 3 pode ser AA ou Aa (A). Se a anomalia fosse dominante, pais normais não teriam filha afetada (C). Os afetados, numa herança recessiva, são homozigotos aa (D). E os normais podem ser AA ou Aa (E).</p>"},
4: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": ["verminoses"],
    "explicacao": "<p>A <strong>ascaridíase</strong> (lombriga) se pega ao engolir ovos do verme em água, alimentos ou mãos contaminados com fezes: é a via fecal-oral. Alternativa <strong>C</strong>.</p><p>Na esquistossomose, a larva entra pela pele em água contaminada (A). A leptospirose é causada por bactéria, não por verme, e vem da urina de ratos (B). A teníase se pega comendo carne de boi ou porco malpassada com larvas (D). E a filariose é transmitida pela picada de mosquito (E).</p>"},
5: {"materia": "Biologia", "assunto": "Zoologia", "tags": ["animais peçonhentos", "artrópodes"],
    "explicacao": "<p>O ferrão do escorpião fica na ponta da cauda e injeta veneno, que causa dor local e pode exigir atendimento médico. Alternativa <strong>E</strong>.</p><p>Esses animais não são parasitas: picam para se defender ou caçar (A). Serpentes não têm exoesqueleto de quitina (B). Escorpiões e aranhas são aracnídeos, não insetos, e são predadores (C). E quelíceras são de aracnídeos; serpentes têm presas (D).</p>"},
6: {"materia": "Biologia", "assunto": "Genética", "tags": MULTI + ["biotecnologia", "DNA recombinante"],
    "explicacao": "<p>O gene humano da insulina é inserido na bactéria, que passa a produzir a <strong>mesma insulina</strong> que o pâncreas humano produz. Alternativa <strong>C</strong>.</p><p>A insulina trata o diabetes, não o cura, e não é vacina (A). Bactérias são unicelulares (B). A insulina humana recombinante reduz, e não aumenta, as reações imunológicas, comuns na antiga insulina de origem animal (D). E o texto fala de genes normais inseridos em bactérias, não de genes mutantes em animais (E).</p>"},
7: {"materia": "Física", "assunto": "Eletricidade", "tags": ["potência elétrica"],
    "enunciado": p("Analise a placa de identificação de dados técnicos colocada no produto denominado escova secadora rotativa da marca Physics:")
                 + "[[fig:1]]" + p("A partir das informações apresentadas na placa e desprezando as possíveis perdas de energia, é correto afirmar que"),
    "imagens": figs(("q07", "Placa de identificação “Physics – Escova secadora rotativa”: 127 V ~; 1270 W; 60 Hz. Tabela de temperaturas: frio ≈ 25 ºC, baixa ≈ 70 ºC, média ≈ 120 ºC, alta ≈ 150 ºC.")),
    "explicacao": "<p>Como P = U · i, a corrente é i = P ÷ U = 1 270 ÷ 127 = <strong>10 A</strong>. Alternativa <strong>A</strong>.</p><p>127 V é a tensão, não a potência (B), e 1 270 W é a potência, não a tensão (C). 60 Hz é a frequência da corrente alternada da rede, não da rotação da escova (D). E 25 ºC a 150 ºC são as temperaturas do ar que sai da escova, não do ambiente (E).</p>"},
8: {"materia": "Física", "assunto": "Dinâmica", "tags": ["atrito"],
    "explicacao": "<p>As ranhuras escoam a água e deixam o pneu em contato direto com o piso, o que aumenta o atrito e a tração. Alternativa <strong>A</strong>.</p><p>Há atrito entre a água e a borracha, só que bem menor (B). As ranhuras drenam a água, não a acumulam (C). Na hidroplanagem, a lâmina de água separa o pneu do piso e o atrito cai (D). E drenar a água diminui, não aumenta, a chance de derrapar (E).</p>"},
9: {"materia": "Física", "assunto": "Ondas", "tags": ["luz", "ondas eletromagnéticas"],
    "enunciado": CODIGO + P9,
    "explicacao": "<p>A luz vermelha ou infravermelha emitida pelo LED é uma <strong>onda eletromagnética</strong>, e toda onda eletromagnética é transversal. É dela que vem a energia captada pelo fotodiodo. Alternativa <strong>E</strong>.</p><p>As barras pretas absorvem a luz, e as brancas refletem (A). O ar não absorve o infravermelho a ponto de impedir a leitura (B). O algoritmo decodifica as barras, não define a impressão (C). E é a corrente que gera o sinal digital, não o contrário (D).</p>"},
10: {"materia": "Física", "assunto": "Ondas", "tags": ["frequência", "notação científica"],
     "enunciado": p("Suponha que, em uma leitura de código de barras, um leitor óptico emite um feixe de laser na faixa do espectro infravermelho. Considere que \\(c \\cong 3{,}0 \\times 10^8\\) m/s; e que \\(\\lambda \\cong 1\\,000\\) nm \\(= 1\\,000 \\times 10^{-9}\\) m.",
                    "Sendo \\(c = \\lambda \\cdot f\\), podemos afirmar corretamente que a ordem de grandeza da frequência f, em Hz, é"),
     "apoio_de": (9, P9),
     "alternativas": {"E": "10<sup>8</sup>"},
     "explicacao": "<p>λ = 1 000 × 10⁻⁹ m = 10⁻⁶ m. Então f = c ÷ λ = 3,0 × 10⁸ ÷ 10⁻⁶ = 3,0 × 10¹⁴ Hz. Como 3 é menor que 3,16 (√10), a ordem de grandeza é <strong>10¹⁴</strong>. Alternativa <strong>B</strong>.</p><p>10⁸ é a ordem de grandeza da velocidade da luz, não da frequência (E). As outras vêm de errar o expoente ao dividir pelas potências de 10.</p>"},
11: {"materia": "Física", "assunto": "Cinemática", "tags": ["lançamento oblíquo"],
     "enunciado": p("Observe a imagem que tem circulado nas mídias sociais:") + "[[fig:1]]"
                  + fonte("&lt;https://tinyurl.com/yfrddjc4&gt; Acesso em 21.08.2025. Original colorido.")
                  + p("Suponhamos que a bailarina esteja saltando no cabo de uma colher com a finalidade de jogar o cubo de açúcar, localizado na outra extremidade da colher, dentro da caneca, de forma certeira.",
                      "No momento exato em que a bailarina atingir completamente o cabo, o açúcar será lançado.",
                      "Nesse caso, desprezando a resistência do ar, é correto afirmar que"),
     "imagens": figs(("q11", "Desenho com os textos “Vamos mergulhar em um novo dia!” e “bom dia!”. Uma bailarina pequena salta, de braços erguidos, sobre o cabo de uma colher deitada; na outra ponta da colher está um cubo de açúcar. Ao lado, uma caneca grande de café fumegante.")),
     "explicacao": "<p>Depois de lançado, o cubo só sofre a ação do peso (a resistência do ar é desprezada). Com velocidade inicial inclinada e aceleração constante para baixo, ele descreve uma <strong>parábola</strong> até a caneca. Alternativa <strong>E</strong>.</p><p>Depois do lançamento, a bailarina não age mais sobre o cubo (A). O peso curva a trajetória, que não é reta (B). A bailarina continua sob a ação da gravidade (C). E o cubo sobe porque a colher o empurra para cima, não por uma força para baixo (D).</p>"},
12: {"materia": "Física", "assunto": "Magnetismo", "tags": MULTI + ["ímãs", "terras-raras"],
     "enunciado": p("O termo terras-raras se refere, na verdade, a um grupo de 17 elementos químicos. Desses elementos, destaca-se o Neodímio (Nd). Sua combinação de propriedades magnéticas e ópticas o torna muito importante para equipamentos eletrônicos e sistemas de defesa. Quando associado ao Ferro (Fe) e ao Boro (B), forma uma liga que se torna um poderoso ímã permanente.",
                    "Com base nas informações do texto sobre esse ímã criado e feito da liga descrita, é correto afirmar que"),
     "explicacao": "<p>O ímã de neodímio-ferro-boro é um ímã permanente muito forte. Como todo ímã, fora dele as linhas de campo <strong>saem do polo norte e entram no polo sul</strong>. Alternativa <strong>D</strong>.</p><p>O neodímio é essencial na liga (A). A liga é produzida pelo ser humano, e o campo da Terra vem do seu núcleo (B). Não existe monopolo magnético: todo ímã tem norte e sul (C). E o campo é intenso, e os polos são norte e sul, não leste e oeste (E).</p>"},
13: {"materia": "Geografia", "assunto": "Geopolítica", "tags": ["Guerra Fria"],
     "explicacao": "<p>Em 1947, os Estados Unidos lançaram o <strong>Plano Marshall</strong>, de ajuda econômica à reconstrução da Europa Ocidental depois da Segunda Guerra, também para conter a influência soviética. Alternativa <strong>C</strong>.</p><p>O primeiro ser humano no espaço foi o soviético Yuri Gagarin (A). As bombas atômicas dos EUA caíram no Japão, não na Europa (B). O Pacto de Varsóvia era a aliança dos socialistas, e a OTAN, a dos capitalistas (D). E o COMECON foi criado pela URSS, depois da Segunda Guerra (E).</p>"},
14: {"materia": "Geografia", "assunto": "Clima", "tags": ["intemperismo"],
     "explicacao": "<p>O intemperismo físico predomina onde há grande variação de temperatura e pouca água, como no clima semiárido do <strong>Sahel</strong>, na borda sul do Saara. Alternativa <strong>B</strong>.</p><p>Na floresta do Congo, quente e úmida, predomina o químico (A). Nas regiões polares e nos desertos, como o Atacama, a água líquida é escassa e predomina o físico (C e E). E a caatinga, semiárida, também tem predomínio do físico (D).</p>"},
15: {"materia": "Geografia", "assunto": "Clima", "tags": ["tipos de chuva"],
     "explicacao": "<p>As chuvas <strong>orográficas</strong> (ou de relevo) acontecem quando o ar úmido sobe ao encontrar uma montanha, esfria e condensa. Alternativa <strong>E</strong>.</p><p>Chuva ácida é a que tem poluentes dissolvidos (A). Saraiva é granizo (B). Chuvas frontais vêm do encontro de massas de ar (C). E as convectivas vêm do ar quente que sobe por aquecimento da superfície, comuns nas tardes de verão (D).</p>"},
16: {"materia": "Geografia", "assunto": "Urbanização", "tags": ["favelas", "direito à cidade"],
     "explicacao": "<p>As favelas e comunidades urbanas surgem quando a população de baixa renda não tem acesso à moradia formal e resolve o problema por conta própria. A causa é a <strong>insuficiência de políticas públicas e de investimentos</strong> em moradia e infraestrutura. Alternativa <strong>E</strong>.</p><p>Há leis que permitem e incentivam moradias populares (A). Muitas favelas ocupam justamente morros e fundos de vale (B). Existem muitos imóveis vazios nas grandes cidades, inacessíveis pelo preço (C). E o poder público não proíbe a verticalização nas regiões centrais (D).</p>"},
17: {"materia": "Geografia", "assunto": "População", "tags": ["crescimento demográfico", "fecundidade"],
     "explicacao": "<p>Um aumento de 0,39% ao ano é baixo. A população brasileira ainda cresce, mas cada vez mais devagar, porque a <strong>taxa de fecundidade vem caindo</strong> há décadas. Alternativa <strong>B</strong>.</p><p>A natalidade está em queda, não acelerando (A e E). O crescimento vegetativo diminui, não aumenta (C). E a fecundidade cai desde antes de 2010, não está em ascensão (D).</p>"},
18: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": MULTI + ["aquecimento global", "negacionismo"],
     "explicacao": "<p>A pergunta pede uma evidência científica que o negacionismo ignora. Medições mostram que <strong>a temperatura média global está subindo</strong>, e a última década foi a mais quente já registrada. Alternativa <strong>B</strong>.</p><p>As outras alternativas não são evidências científicas, mas ideias do próprio negacionismo: que a causa é só natural (A), que virá uma Era do Gelo (C), que tudo se adapta ou já há solução técnica (D), e que os gases de efeito estufa não são os responsáveis (E).</p>"},
19: {"materia": "História", "assunto": "Antiguidade", "tags": MULTI + ["período helenístico", "Eratóstenes"],
     "explicacao": "<p>Eratóstenes usou as sombras em duas cidades e a distância entre elas para medir a circunferência da Terra. O cálculo só faz sentido se a Terra for curva, e <strong>reforçou a ideia de uma Terra esférica</strong>. Alternativa <strong>E</strong>.</p><p>A América só chegou ao conhecimento europeu com as Grandes Navegações (A). O cálculo usava geometria e observação, não mitos (B). Eratóstenes viveu no século III a.C., antes de Júlio César (C). E o período helenístico justamente misturou a cultura grega com a de outros povos (D).</p>"},
20: {"materia": "História", "assunto": "Revolução Industrial", "tags": ["máquina a vapor"],
     "explicacao": "<p>O condensador de Watt deixou a máquina a vapor mais eficiente e econômica no uso do carvão, o que a tornou <strong>viável</strong> para fábricas, minas e transportes e impulsionou a Revolução Industrial. Alternativa <strong>D</strong>.</p><p>A energia elétrica só se difundiu no fim do século XIX (A). A máquina de Watt era mais eficiente que a de Newcomen (B). Ela aperfeiçoou máquinas já existentes (C). E continuou usando carvão (E).</p>"},
21: {"materia": "História", "assunto": "História contemporânea", "tags": ["Belle Époque"],
     "explicacao": "<p>Os novos inventos aceleraram o ritmo de vida, modernizaram as casas de quem podia pagar e criaram uma <strong>cultura urbana de consumo e entretenimento</strong>. Alternativa <strong>B</strong>.</p><p>Os espetáculos públicos, como cinema e cafés-concerto, cresceram (A). A época valorizava o moderno, não o medieval (C). As novidades chegavam a “uma parcela da sociedade”, não a todos (D). E a produção era industrial e urbana, não da aristocracia rural (E).</p>"},
22: {"materia": "História", "assunto": "História contemporânea", "tags": ["Guerra Fria"],
     "explicacao": "<p>Nas guerras por procuração, EUA e URSS forneciam armas e tecnologia aos aliados e usavam esses conflitos para <strong>testar seus equipamentos e suas doutrinas</strong>. Alternativa <strong>A</strong>.</p><p>A tecnologia foi decisiva, e não irrelevante (B). As armas eram modernas (C). Nenhuma bomba atômica foi usada em combate depois de 1945 (D). E as duas superpotências nunca lutaram diretamente uma contra a outra (E).</p>"},
23: {"materia": "História", "assunto": "Povos indígenas", "tags": ["coivara"],
     "explicacao": "<p>O texto diz que a coivara derruba áreas pequenas, usa o fogo para limpar a roça e, depois de alguns anos, abandona a área para a floresta voltar a crescer. Por isso o impacto é pequeno. Alternativa <strong>C</strong>.</p><p>O texto diz que nunca se derruba uma área grande (A) e que a floresta volta a crescer (B). A técnica é indígena, anterior aos portugueses (D). E o objetivo é produzir alimentos (E).</p>"},
24: {"materia": "História", "assunto": "Era Vargas", "tags": ["industrialização", "estatais"],
     "enunciado": p("A Era Vargas foi um período marcado pela centralização política e por uma forte intervenção do Estado na economia. Vargas entendia que a industrialização e o desenvolvimento tecnológico eram fundamentais para garantir a soberania e a modernização do país. Seu governo criou empresas estatais e implementou medidas e políticas para impulsionar setores estratégicos, como mostra o quadro.")
                  + tabela(["Área", "Medida implementada"], [["Siderurgia", "Criação da Companhia Siderúrgica Nacional (CSN)"], ["Combustíveis", "Criação do Conselho Nacional do Petróleo"], ["Ciência &amp; Tecnologia", "Criação do Conselho Nacional de Pesquisas (CNPq)"]])
                  + p("Ao adotar tais medidas, Vargas pretendia"),
     "explicacao": "<p>CSN, Conselho do Petróleo e CNPq mostram o Estado investindo em setores de base para que o Brasil produzisse o que antes importava: é a <strong>substituição de importações</strong>, com o Estado como planejador e investidor. Alternativa <strong>E</strong>.</p><p>Vargas não isolou o país nem proibiu importações (A). Ele aumentou, e não reduziu, a presença do Estado (B). O foco era a indústria, não só o café (C). E ele criou estatais, não as privatizou (D).</p>"},
25: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": ["quadrinho"],
     "enunciado": PEPINOS + P25, "imagens": PEPINOS_IMG,
     "explicacao": "<p>Um pepino em água salgada perde água por osmose e fica enrugado, virando picles. Os amigos acham que a piscina era de água salgada (<em>salt-water pool</em>) e que o amigo saiu <strong>desidratado</strong>. Alternativa <strong>C</strong>.</p><p>O quadrinho não fala de temperatura (A), vinagre (B), água ionizada (D) ou água sem sal (E).</p>"},
26: {"materia": "Inglês", "assunto": "Vocabulário", "tags": ["verbos modais"],
     "enunciado": p("A ocorrência do verbo <em>must</em> no quadrinho expressa"), "apoio_de": (25, P25),
     "explicacao": "<p>Em “this <em>must</em> be one of those salt-water pools”, o pepino conclui algo a partir do que vê: <em>must</em> indica <strong>dedução</strong> (“deve ser”). Alternativa <strong>A</strong>.</p><p>Permissão seria <em>may</em> ou <em>can</em> (B), habilidade, <em>can</em> (C), e conselho, <em>should</em> (E). <em>Must</em> também pode indicar obrigação, mas não nessa frase (D).</p>"},
27: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": ["tirinha"],
     "enunciado": p("Leia a tirinha.") + "[[fig:1]]" + url("https://tinyurl.com/4htnsnbb", "12.09.2025", "")
                  + p("A: Could you please... B: I already helped you once, so now be an independent woman. / A: What a sweetheart / A: Yes, Sir…independent, very independent, creative, strong, and … fearless! C: Can I help…? A: Not now, Henry, I’m busy being a woman!", classe="fonte")
                  + p("De acordo com a garota da tirinha, pressupõe-se que uma mulher é"),
     "imagens": figs(("q27", "Tirinha em três quadros, numa cozinha. 1: uma menina tenta alcançar um pote numa prateleira alta e pede ajuda a um homem adulto, que se recusa e diz que ela deve ser uma mulher independente. 2: a menina, sozinha, comenta com ironia “What a sweetheart”. 3: a menina sobe numa cadeira com rodinhas, equilibrando-se para pegar o pote, e repete as palavras do homem; um menino oferece ajuda, e ela recusa, dizendo que está ocupada sendo uma mulher.")),
     "explicacao": "<p>No último quadro, a garota repete o que o homem disse: <em>independent, creative, strong, and fearless</em>. Pressupõe-se que a mulher é <strong>criativa, independente e forte</strong>. Alternativa <strong>B</strong>.</p><p>Ela não fala em sincera, dócil, frágil ou teimosa (A, C, D e E). “Fearless” (destemida) lembra “audaciosa”, mas essas alternativas trazem também uma qualidade que a garota não cita.</p>"},
28: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": MULTI + ["urna eletrônica"],
     "explicacao": "<p>O texto diz que o Brasil foi o primeiro país a fazer eleições totalmente eletrônicas e “has since remained at the forefront” (continua na dianteira). É um caso de <strong>vanguarda</strong>. Alternativa <strong>D</strong>.</p><p><em>Thriving</em> quer dizer próspero, bem-sucedido. O texto não fala de disputas demoradas (A), de país subdesenvolvido (B), de atraso (C) nem de risco (E).</p>"},
29: {"materia": "Inglês", "assunto": "Coesão e referência", "tags": ["conectivos", "canção"],
     "enunciado": ROCKET + P29, "imagens": ROCKET_IMG,
     "explicacao": "<p>A estrofe diz que Marte não é lugar para criar filhos e, em seguida, <em>in fact</em> (“na verdade”, “de fato”) reforça o motivo: <strong>lá é frio demais</strong>. Alternativa <strong>E</strong>.</p><p>A conclusão sobre os filhos está no verso anterior, não na expressão (A). A canção diz que Marte não serve de lar (B, C e D).</p>"},
30: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": ["canção"],
     "enunciado": p("A música de Elton John foi composta em 1972 e refere-se ao desenvolvimento da"), "apoio_de": (29, P29),
     "alternativas": {"A": "clonagem de seres humanos.", "B": "inteligência artificial.", "C": "engenharia genética.", "D": "exploração espacial.", "E": "internet."},
     "explicacao": "<p>O título (“homem-foguete”) e os versos sobre a solidão no espaço e sobre Marte falam de um astronauta. Em 1972, a corrida espacial estava no auge: foi o ano da última missão tripulada à Lua. A canção se refere à <strong>exploração espacial</strong>. Alternativa <strong>D</strong>.</p><p>A letra não trata de clonagem, inteligência artificial, engenharia genética ou internet (A, B, C e E).</p>"},
}

SIMB = {"hex": "⬢ (hexágono)", "bar": "‖ (barra dupla)", "los": "◆ (losango)", "cir": "● (círculo)", "est": "★ (estrela)", "qua": "■ (quadrado)", "tri": "▲ (triângulo)"}

Q.update({
31: {"materia": "Matemática", "assunto": "Análise combinatória", "tags": ["princípio multiplicativo"],
     "enunciado": p("Em 2018, o Brasil adotou um novo sistema de placas de veículos, o Mercosul, com o formato LLL NL NN, em que L representa uma letra do alfabeto romano (de 26 letras); e N representa um algarismo (de 0 a 9).",
                    "Assinale a alternativa que indica corretamente quantas placas diferentes, seguindo o padrão Mercosul, podem ser formadas utilizando apenas as vogais do alfabeto romano."),
     "alternativas": {"A": "125 000 placas", "B": "200 000 placas", "C": "456 976 placas", "D": "625 000 placas", "E": "676 000 placas"},
     "explicacao": "<p>São 4 letras (5 vogais possíveis cada) e 3 algarismos (10 possibilidades cada): 5 · 5 · 5 · 10 · 5 · 10 · 10 = 5⁴ · 10³ = 625 · 1 000 = <strong>625 000</strong>. Alternativa <strong>D</strong>.</p><p>Esquecer a letra do meio (LLL NL NN tem quatro letras) dá 125 000 (A). E 456 976 = 26⁴ usa o alfabeto inteiro e esquece os algarismos (C).</p>"},
32: {"materia": "Matemática", "assunto": "Geometria plana", "tags": ["circunferência"],
     "enunciado": RODA + P32,
     "alternativas": {"A": "80π.", "B": "160π.", "C": "320π.", "D": "3 200π.", "E": "6 400π."},
     "explicacao": "<p>O comprimento da circunferência é C = 2πr = π · d. Com d = 80 m, C = <strong>80π</strong> m. Alternativa <strong>A</strong>.</p><p>160π vem de usar 2π · 80, tomando o diâmetro como raio (B). 6 400π é π · 80², que nem é fórmula de comprimento (E).</p>"},
33: {"materia": "Matemática", "assunto": "Trigonometria", "tags": ["função cosseno"],
     "enunciado": p("Suponha que, durante o passeio na roda gigante mencionada no texto, a altura de uma cabine possa ser modelada pela função:",
                    "\\[h(t) = 51 - 40\\cos\\left(\\frac{\\pi}{15}\\,t\\right)\\]",
                    "em que h(t) é a altura, em metros, da cabine em relação ao solo e t é o tempo, em minutos, desde o início do passeio no ponto mais baixo da roda gigante (t ≥ 0).",
                    "Assinale a alternativa que apresenta, respectivamente, a maior altura atingida pela cabine e o instante de tempo em que isso ocorre pela primeira vez."),
     "apoio_de": (32, P32),
     "explicacao": "<p>A altura é máxima quando o cosseno vale −1: h = 51 − 40 · (−1) = <strong>91 m</strong>. Isso acontece pela primeira vez quando \\(\\frac{\\pi}{15}t = \\pi\\), ou seja, t = <strong>15 min</strong>. Alternativa <strong>B</strong>.</p><p>30 min é o instante em que a cabine volta ao ponto mais baixo (A). 51 m é a altura do centro da roda (C e D), e 11 m, a do ponto mais baixo (E).</p>"},
34: {"materia": "Matemática", "assunto": "Funções", "tags": ["logaritmo", "pH"],
     "enunciado": p("O pH de uma solução pode ser calculado por meio da expressão, pH = –log[H<sup>+</sup>], em que [H<sup>+</sup>] é a concentração em mol/L de íons de hidrogênio.",
                    "Dessa forma, adotando log 2 = 0,3, uma solução que tenha [H<sup>+</sup>] = 2 × 10<sup>–7</sup> mol/L terá pH igual a"),
     "explicacao": "<p>pH = −log(2 × 10⁻⁷) = −(log 2 + log 10⁻⁷) = −(0,3 − 7) = <strong>6,7</strong>. Alternativa <strong>C</strong>.</p><p>7,3 viria de somar o log 2 em vez de subtrair, e não está nas alternativas. Os outros valores não saem da propriedade do logaritmo do produto.</p>"},
35: {"materia": "Matemática", "assunto": "Sequências", "tags": ["progressão aritmética"],
     "explicacao": "<p>A instalação forma uma progressão aritmética com a₁ = 50 e razão 15. O décimo termo é a₁₀ = 50 + 9 · 15 = <strong>185 km</strong>. Alternativa <strong>C</strong>.</p><p>Usar 10 · 15 em vez de 9 · 15 daria 200 km, que não está nas alternativas. 155 km seria o oitavo ano (B).</p>"},
36: {"materia": "Matemática", "assunto": "Funções", "tags": ["função exponencial"],
     "enunciado": p("Suponha que um laboratório estime o crescimento de uma cultura bacteriana utilizando a fórmula \\(N(t) = 1\\,000 \\cdot 2^{\\frac{t}{g}}\\), em que <em>N(t)</em> é o número de bactérias no tempo t (em minutos) e g é o tempo de geração, ou seja, o tempo para a população bacteriana duplicar.",
                    "Em determinado experimento, após 45 minutos, uma população de bactérias chegou a 8 000 bactérias.",
                    "O tempo de geração, g, dessa cultura bacteriana é de"),
     "explicacao": "<p>8 000 = 1 000 · 2^(45/g), então 2^(45/g) = 8 = 2³. Logo 45/g = 3 e g = <strong>15 minutos</strong>. Alternativa <strong>A</strong>.</p><p>A população dobrou três vezes (1 000 → 2 000 → 4 000 → 8 000) em 45 minutos: 15 minutos para cada duplicação. Os outros valores não dão um número inteiro de duplicações.</p>"},
37: {"materia": "Matemática", "assunto": "Operações e problemas", "tags": ["matrizes"],
     "enunciado": enun(R, 37, figs={"p13-1": 1}, trocas=[("multiplica cada número da matriz <em>A</em> por ,", "multiplica cada número da matriz <em>A</em> por \\(\\frac{1}{2}\\),")]),
     "imagens": figs(("q37", "Mosaico de 3 × 3 quadrados em tons de cinza, ao lado da mesma grade com os números de cada tom e da matriz A correspondente. Linha 1: 50, 248, 126. Linha 2: 10, 30, 168. Linha 3: 8, 84, 158.")),
     "explicacao": "<p>O elemento da linha 2 e coluna 3 da matriz A é 168. Multiplicado por 1/2, fica <strong>84</strong>. Alternativa <strong>E</strong>.</p><p>15 é a metade de 30, da linha 2 e coluna 2 (A). 79 é a metade de 158, da linha 3 (D). E 42 é a metade de 84, da linha 3 e coluna 2 (C).</p>"},
38: {"materia": "Matemática", "assunto": "Trigonometria", "tags": ["triângulo retângulo"],
     "enunciado": enun(R, 38, figs={"p14-1": 1}),
     "imagens": figs(("q38", "Triângulo retângulo: o drone parte do ponto A, no solo, e sobe em linha reta 20 km até o ponto B, formando o ângulo θ com o solo. A altura h vai de B até o solo, na vertical, formando um ângulo reto.")),
     "explicacao": "<p>A altura h é o cateto oposto ao ângulo θ, e os 20 km são a hipotenusa: h = 20 · sen θ = 20 · 0,8 = <strong>16 km</strong>. Alternativa <strong>D</strong>.</p><p>Usar o cosseno dá 12 km, que é a distância horizontal, não a altura (B).</p>"},
39: {"materia": "Matemática", "assunto": "Notação científica", "tags": MULTI + ["inglês"],
     "enunciado": enun(R, 39) + p("Assinale a alternativa que contém os termos, em ordem, que completam corretamente as lacunas no texto."),
     "alternativas": {"A": "4,1 × 10<sup>10</sup> — muito popular"},
     "explicacao": "<p>O texto diz que a estrela mais próxima está 7 000 vezes mais longe que Plutão: 7 × 10³ · 5,9 × 10⁹ = 41,3 × 10¹² ≈ <strong>4,1 × 10¹³ km</strong>. E diz que a ideia de os ETs virem até aqui “is not a popular idea among most scientists”: é <strong>pouco popular</strong>. Alternativa <strong>E</strong>.</p><p>“Not a popular idea” não é “muito popular” (A e B). E 10⁹ e 10¹⁰ vêm de errar a soma dos expoentes (C e D).</p>"},
40: {"materia": "Química", "assunto": "Separação de misturas",
     "explicacao": "<p>As nanopartículas magnéticas grudam no plástico, e o conjunto é retirado da água com um ímã: <strong>separação magnética</strong>. Alternativa <strong>E</strong>.</p><p>Filtração usa um filtro poroso (A), catação separa à mão (B), decantação usa a diferença de densidade e a gravidade (C), e destilação usa a diferença de ponto de ebulição (D).</p>"},
41: {"materia": "Química", "assunto": "Química orgânica", "tags": ["porcentagem em massa"],
     "enunciado": PFAS + P41, "imagens": PFAS_IMG,
     "explicacao": "<p>O PFAS é o composto com flúor, o elemento mais eletronegativo, no lugar dos hidrogênios da cadeia: C₄HF₇O₂ (CF₃–CF₂–CF₂–COOH). Massa molar: 4 · 12 + 1 + 7 · 19 + 2 · 16 = 48 + 1 + 133 + 32 = 214 g/mol. Porcentagem de carbono: 48 ÷ 214 ≈ <strong>22,4%</strong>. Alternativa <strong>B</strong>.</p><p>O composto com cloro não é um PFAS, porque o cloro não é o elemento mais eletronegativo. Contar só três carbonos, esquecendo o do COOH, daria cerca de 17%, que não está nas alternativas.</p>"},
42: {"materia": "Química", "assunto": "Reações químicas", "tags": ["meia-vida"],
     "enunciado": p("A estimativa da meia-vida (\\(t_{\\frac{1}{2}}\\)) das PFAS é essencial para quantificar sua persistência, toxicidade e mecanismo de ação em humanos. Meia-vida é o intervalo de tempo necessário para a quantidade de um reagente diminuir a metade do seu valor. Suponha que um indivíduo ingeriu água contaminada com 200 mg de PFOA (ácido perfluorooctanóico) e que, após 12 anos, foram encontrados 12,5 mg de PFOA em seu organismo.",
                    "Considerando as informações apresentadas, assinale a alternativa que contém o tempo de meia-vida correto do PFOA."),
     "apoio_de": (41, P41),
     "alternativas": {"A": "1 ano", "B": "2 anos", "C": "3 anos", "D": "4 anos", "E": "5 anos"},
     "explicacao": "<p>200 → 100 → 50 → 25 → 12,5 mg: são 4 meias-vidas em 12 anos. Cada meia-vida dura 12 ÷ 4 = <strong>3 anos</strong>. Alternativa <strong>C</strong>.</p><p>Dividir 200 por 12,5 dá 16 (que é 2⁴), não o número de meias-vidas. Usar 16 ou 6 meias-vidas leva aos outros valores.</p>"},
43: {"materia": "Química", "assunto": "Funções inorgânicas", "tags": MULTI + ["ligação iônica", "sais"],
     "enunciado": p("Circulou um boato em mídias sociais de que o sal light é tóxico, pois contém cloreto de potássio. No entanto, o cloreto de potássio (KCℓ), nas quantidades em que comumente é usado no sal light, não é considerado tóxico. Ele é um composto químico inorgânico muito semelhante ao cloreto de sódio (NaCℓ), um dos componentes do sal de cozinha.",
                    "Analisando a fórmula do cloreto de sódio e do cloreto de potássio, pode-se afirmar corretamente que uma das semelhanças entre esses dois compostos ocorre"),
     "alternativas": {"A": "na classificação como macronutrientes, já que ambos são carboidratos.", "B": "na classificação como macronutrientes, já que ambos são proteínas.",
                      "C": "na classificação como macronutrientes, já que ambos são lipídeos.", "D": "na ligação química, já que ambos apresentam ligações iônicas.",
                      "E": "na ligação química, já que ambos apresentam ligações covalentes."},
     "explicacao": "<p>Sódio e potássio são metais alcalinos que perdem um elétron, e o cloro recebe esse elétron. Nos dois compostos a ligação é <strong>iônica</strong>. Alternativa <strong>D</strong>.</p><p>São sais minerais, não carboidratos, proteínas ou lipídeos (A, B e C). E a ligação covalente é entre não metais (E).</p>"},
44: {"materia": "Química", "assunto": "Funções orgânicas", "tags": ["fórmula molecular", "polímeros"],
     "enunciado": p("Quando o poli(tereftalato de etileno), denominado PET, sofre degradação, são liberados ácido tereftálico e etano-1,2-diol, conforme a equação química representada.")
                  + "[[fig:1]]" + p("Considerando as fórmulas estruturais apresentadas na equação química, assinale a alternativa que contém, respectivamente, o nome da função orgânica presente na molécula de etano-1,2-diol e a fórmula molecular correta do ácido tereftálico, respectivamente."),
     "imagens": figs(("q44", "Equação química: o polímero PET (unidade com um anel benzênico entre dois grupos C=O, ligada a O–CH₂–CH₂–O, repetida n vezes) mais 2n H₂O produz n moléculas de ácido tereftálico (HOOC–C₆H₄–COOH, anel benzênico com um grupo COOH em cada lado) e n moléculas de etano-1,2-diol (HO–CH₂–CH₂–OH).")),
     "explicacao": "<p>O etano-1,2-diol tem dois grupos OH ligados a carbonos saturados: é um <strong>álcool</strong> (o sufixo “-ol” confirma). O ácido tereftálico tem um anel benzênico (6 C e 4 H) e dois grupos COOH (2 C, 2 H e 4 O): <strong>C₈H₆O₄</strong>. Alternativa <strong>C</strong>.</p><p>C₂H₆O₂ é a fórmula do etano-1,2-diol, não do ácido (A). C₂H₂O₄ é o ácido oxálico (B e E). E o etano-1,2-diol não tem o grupo CHO dos aldeídos (D e E).</p>"},
45: {"materia": "Química", "assunto": "Reações químicas", "tags": ["pilhas e baterias"],
     "enunciado": enun(R, 45, figs={"p16-2": 1}),
     "imagens": figs(("q45", "Esquema de uma bateria de íons-lítio. À esquerda, o polo negativo: lâmina de cobre e grafite (LiyC), com camadas hexagonais. À direita, o polo positivo: lâmina de alumínio e LizCoO₂. No meio, o eletrólito contendo X e uma membrana. Uma seta X vai do grafite para o LizCoO₂ por dentro da bateria. Por fora, um fio liga os dois polos passando por uma lâmpada, com setas T indo do polo negativo para o positivo.")),
     "explicacao": "<p>Pelo fio externo, que acende a lâmpada, passam os <strong>elétrons</strong> (T), do polo negativo para o positivo. Por dentro, pelo eletrólito, os <strong>íons Li⁺</strong> (X) vão do grafite para o cátodo de cobaltato de lítio. X e T são, nessa ordem, íons Li⁺ e elétrons. Alternativa <strong>D</strong>.</p><p>A, B e C invertem os papéis: elétrons não atravessam o eletrólito. E o íon que se move é o Li⁺, não o Co²⁺ nem o O²⁻ (B, C e E).</p>"},
46: {"materia": "Raciocínio lógico", "assunto": "Sequências", "tags": ["padrões"],
     "enunciado": BALEIAS + P46,
     "imagens": BALEIAS_IMG,
     "alternativas": {"A": "20.", "B": "40.", "C": "60.", "D": "90.", "E": "120."},
     "explicacao": "<p>O Tema 2 é a frase ⬢ ‖ ‖ ◆ (6 + 4 + 4 + 1 = 15 s) repetida 3 vezes: 45 s. O Tema 3 é ■ ★ ▲ ★ (3 + 5 + 2 + 5 = 15 s) repetida 3 vezes: 45 s. Os dois juntos duram 90 s. Em meia hora (1 800 s), eles se repetem 1 800 ÷ 90 = <strong>20 vezes</strong>. Alternativa <strong>A</strong>.</p><p>Contar só uma frase de cada tema (30 s) daria 60 (C). E 40 vem de dividir 1 800 pelos 45 s de um tema só (B).</p>"},
47: {"materia": "Raciocínio lógico", "assunto": "Sequências",
     "enunciado": p("A construção de uma música é feita a partir blocos sonoros. Ao ordenarmos esses blocos, conforme sua complexidade, obtemos a sequência"),
     "apoio_de": (46, P46),
     "alternativas": {"A": "Frase → Unidade → Tema → Música.", "B": "Unidade → Tema → Música → Frase.", "C": "Música → Tema → Frase → Unidade.", "D": "Unidade → Frase → Tema → Música.", "E": "Tema → Frase → Música → Unidade."},
     "explicacao": "<p>O infográfico diz que a unidade é um som individual, que unidades formam frases, que frases formam temas e que temas formam a música: <strong>Unidade → Frase → Tema → Música</strong>. Alternativa <strong>D</strong>.</p><p>C traz a mesma ordem ao contrário, da mais complexa para a mais simples. As outras misturam os níveis (A, B e E).</p>"},
48: {"materia": "Raciocínio lógico", "assunto": "Sequências", "tags": ["padrões", "divisibilidade"],
     "enunciado": p("Suponha que o Tema 4 repita-se indefinidamente. Desse modo, a unidade que ocupa, nessa sequência, a posição correspondente ao ano de lançamento do LP mencionado no texto deve ser"),
     "apoio_de": (46, P46),
     "alternativas": {"A": SIMB["cir"], "B": SIMB["hex"], "C": SIMB["los"], "D": SIMB["est"], "E": SIMB["qua"]},
     "explicacao": "<p>O Tema 4 repete o bloco ★ ◆ ● ⬢, de 4 unidades. O LP saiu em 1970, e 1970 = 4 · 492 + 2. A posição 1970 é a 2ª do bloco: <strong>◆</strong>. Alternativa <strong>C</strong>.</p><p>Com resto 1, seria ★ (D); com resto 3, ● (A); e com resto 0, ⬢ (B). O quadrado não aparece no Tema 4 (E).</p>"},
49: {"materia": "Raciocínio lógico", "assunto": "Lógica", "tags": ["média aritmética"],
     "explicacao": "<p>O total é 850 + 530 + 490 + 450 = 2 320 doses, e cada hospital deve ficar com 2 320 ÷ 4 = 580. A perde 270; B ganha 50; C ganha 90; D ganha 130. Existe um hospital que <strong>ganhou 90 doses</strong> (o C). Alternativa <strong>A</strong>.</p><p>130 doses foi o que D ganhou, não perdeu (B). 270 foi o que A perdeu, não ganhou (C). E 580 é a quantidade final de cada um (E).</p>"},
50: {"materia": "Raciocínio lógico", "assunto": "Lógica", "tags": ["silogismo"],
     "enunciado": p("Considere as seguintes afirmações", "• Todas as filhas de Rose são pesquisadoras; e", "• Todas as filhas de Alfredo não são pesquisadoras.",
                    "Com base nessas premissas, assinale a dedução lógica correta."),
     "explicacao": "<p>Toda filha de Rose é pesquisadora, e nenhuma filha de Alfredo é pesquisadora. Se alguém fosse filha dos dois, seria e não seria pesquisadora ao mesmo tempo. Logo, <strong>nenhuma filha de Alfredo é filha de Rose</strong>. Alternativa <strong>E</strong>.</p><p>A e C contradizem a primeira premissa, e B, a segunda. D é justamente o que as premissas impedem.</p>"},
51: {"materia": "Raciocínio lógico", "assunto": "Lógica", "tags": MULTI + ["geografia"],
     "enunciado": apoio("As histórias de Júlio Verne impactaram na criação de tecnologias que utilizamos hoje, pois inspiraram inventores como o estadunidense Simon Lake, o brasileiro Santos Dumont e o russo Konstantin Tsiolkovsky.")
                  + url("https://tinyurl.com/489jpjss", "05.09.2025")
                  + p("Sobre os inventores mencionados, sabe-se que",
                      "<strong>I.</strong> um deles projetou alguns dos primeiros submarinos e é natural de um país que está no Hemisfério Ocidental;",
                      "<strong>II.</strong> somente um deles foi pioneiro da astronáutica e dos foguetes modernos, tendo nascido em um país, cujo nome da capital tem 6 letras;",
                      "<strong>III.</strong> o único nascido em um país do Hemisfério Sul não projetou alguns dos primeiros submarinos.",
                      "Fundamentado apenas nas informações apresentadas, marque a alternativa que associa corretamente o inventor com aquilo que realizou."),
     "explicacao": "<p>Brasília tem 8 letras, Washington tem 10 e Moscou tem 6: pela informação II, o pioneiro da astronáutica é o russo <strong>Tsiolkovsky</strong>. Alternativa <strong>E</strong>.</p><p>Pela III, Dumont (Hemisfério Sul) não projetou submarinos (C). Então quem projetou foi Lake, dos Estados Unidos, no Hemisfério Ocidental, como diz a I. Tsiolkovsky já é o da astronáutica, e a II diz que só um deles foi (A e D). E nada nas informações fala de aeronaves, que foram obra de Dumont (B).</p>"},
52: {"materia": "Português", "assunto": "Interpretação de texto", "tags": ["tirinha", "fake news"],
     "enunciado": TIRINHA + P52, "imagens": TIRINHA_IMG,
     "explicacao": "<p>Assim como se esconde o remédio do cão dentro de um petisco, uma mentira é escondida no meio de verdades para ser “engolida”. Alguns percebem e cospem; outros engolem e passam a repetir teorias absurdas. A comparação <strong>explica como as informações falsas se espalham</strong>. Alternativa <strong>E</strong>.</p><p>A tirinha não ensina cuidados com animais (A e D), não discute se verdade é subjetiva (B) e não fala de brindes (C).</p>"},
53: {"materia": "Português", "assunto": "Semântica", "tags": ["provérbios"],
     "enunciado": p("Assinale o provérbio que expressa de forma concisa a ideia apresentada na tirinha."), "apoio_de": (52, P52),
     "alternativas": {"E": "De grão em grão, a galinha enche o papo."},
     "explicacao": "<p>“Cara de mel, coração de fel” fala de algo que parece doce por fora e esconde o amargo por dentro, como a mentira envolta em verdades ou o remédio no petisco. Alternativa <strong>A</strong>.</p><p>“Quem não arrisca, não petisca” fala de coragem (B). “Casa de ferreiro, espeto de pau”, de quem não usa o que oferece aos outros (C). “Em boca fechada não entra mosca”, de ficar calado (D). E “De grão em grão...”, de juntar aos poucos (E).</p>"},
54: {"materia": "Português", "assunto": "Figuras de linguagem", "tags": ["ironia", "meme"],
     "enunciado": MEME + P54, "imagens": MEME_IMG,
     "explicacao": "<p>Dizer que as árvores “apenas” dão o oxigênio que respiramos é dizer o contrário do que se pensa: o oxigênio é muito mais importante que o Wi-Fi. É <strong>ironia</strong>. Alternativa <strong>A</strong>.</p><p>Não há repetição de palavras no início das frases (B), não se suaviza uma ideia desagradável (C), não há palavra usada fora do sentido original por falta de outra (D) e não há imitação de som (E).</p>"},
55: {"materia": "Português", "assunto": "Gêneros textuais", "tags": ["meme"],
     "enunciado": p("O <em>meme</em> apresentado, além de gerar humor, cumpre também a finalidade de"), "apoio_de": (54, P54),
     "explicacao": "<p>Pela ironia, o <em>meme</em> leva a pensar que damos mais valor à tecnologia do que às árvores, que nos dão o oxigênio. Ele busca <strong>conscientizar</strong> sobre a preservação ambiental. Alternativa <strong>A</strong>.</p><p>Ele não vende produto (B), não traz dados (C), não ensina receita (D) e não narra uma história (E).</p>"},
56: {"materia": "Português", "assunto": "Interpretação de texto", "tags": ["infográfico", "letramento científico"],
     "enunciado": VACINAS + P56, "imagens": VACINAS_IMG,
     "explicacao": "<p>Somando “concordo em partes” e “concordo totalmente”, 35% acreditam que vacinas podem causar autismo, e outros 17% não souberam responder. O texto liga isso à falta de educação científica: o <strong>baixo letramento científico favorece a circulação de fake news</strong>. Alternativa <strong>D</strong>.</p><p>Quem discorda soma 12% + 36% = 48%, não 47% (A). Os 36% discordam totalmente de que vacinas causam autismo, o que não tem a ver com descrença na eficácia (B). A pesquisa não fala de senso comum (C). E os 21% concordam totalmente com a afirmação falsa; a pesquisa não trata de meios de informação (E).</p>"},
57: {"materia": "Português", "assunto": "Conectivos", "tags": ["oração de finalidade", "reescrita"],
     "enunciado": p("A passagem “visando reforçar a educação científica da população” pode ser substituída, sem prejuízo de sentido para o texto, por"), "apoio_de": (56, P56),
     "explicacao": "<p>“Visando” indica a finalidade das políticas: o objetivo é reforçar a educação científica. A locução “<strong>a fim de que</strong>” mantém essa ideia de finalidade. Alternativa <strong>B</strong>.</p><p>“Porque” e “uma vez que” indicam causa (A e C), e C ainda põe a ação no passado. D muda quem reforça: a população, e não as políticas. E “enquanto” indica tempo ou proporção (E).</p>"},
58: {"materia": "Geografia", "assunto": "Regionalização do Brasil", "tags": MULTI + ["interpretação de gráficos", "tecnologia"],
     "enunciado": p("Analise os gráficos apresentados.") + "[[fig:1]]"
                  + fonte("*Correspondem aos setores de alta e média alta intensidade tecnológica propostos pela OCDE")
                  + url("https://tinyurl.com/3bhkpz8y", "14.09.2025", "Original colorido.") + "[[fig:2]]"
                  + fonte("Fonte dos dados: &lt;https://tinyurl.com/5tez5bfw&gt; Acesso em: 14.09.2025.")
                  + p("A partir da análise dos gráficos, conclui-se corretamente que, no Brasil,"),
     "imagens": figs(("q58a", "Gráfico de barras “Distribuição pelo país”: participação de cada estado nos vínculos empregatícios dos setores intensivos em conhecimento, em %, em 2023. São Paulo 44,2; Minas Gerais 9,3; Rio Grande do Sul 8,5; Paraná 7,7; Santa Catarina 7,4; Rio de Janeiro 4,9; Amazonas 3,0; Ceará 2,8; Goiás 2,2; Pernambuco 2,0."),
                     ("q58b", "Gráfico de barras “Percentual de docentes em exercício com pós-graduação stricto sensu, por região, Brasil, 2023”, com eixo de 72 a 90%. Norte cerca de 79%; Nordeste cerca de 85%; Sudeste cerca de 87%; Sul cerca de 88%; Centro-Oeste cerca de 83%.")),
     "explicacao": "<p>O Sudeste tem um dos maiores percentuais de docentes com pós-graduação (cerca de 87%) e concentra os empregos de alta tecnologia: São Paulo sozinho tem 44,2%, e Minas Gerais e Rio de Janeiro também estão entre os dez. Alternativa <strong>D</strong>.</p><p>O Norte tem o menor percentual de docentes com pós (A). Ceará e Pernambuco, do Nordeste, estão entre os dez (B). O gráfico não mostra que um percentual baixo cause muitos empregos, e o Centro-Oeste tem só Goiás na lista (C). E o Sul tem três estados na lista, não quatro, e os gráficos não provam relação de causa (E).</p>"},
59: {"materia": "Português", "assunto": "Gêneros textuais", "tags": ["texto expositivo"],
     "enunciado": DEEP + P59,
     "explicacao": "<p>O texto define o que são as <em>deep techs</em>, diz o que buscam e dá exemplos de áreas: é um texto expositivo, que <strong>apresenta o conceito</strong> de um novo tipo de empresa. Alternativa <strong>A</strong>.</p><p>Ele não conta a história de uma empresa (B), não defende superioridade (C), não fala da comunicação entre startups (D) e não pede seguidores (E).</p>"},
60: {"materia": "Português", "assunto": "Interpretação de texto",
     "enunciado": DEEP + p("De acordo com o texto,"),
     "explicacao": "<p>O texto diz que as <em>deep techs</em> fornecem soluções tecnológicas para “resolver problemas complexos e de alto impacto”: elas <strong>usam tecnologia para solucionar problemas desafiadores</strong>. Alternativa <strong>B</strong>.</p><p>O texto não fala em conectar empresas a consumidores (A), diz que os problemas são de alto impacto, não irrelevantes (C), cita várias áreas além de aplicativos (D) e não fala de poucas áreas nem de limite de investimento (E).</p>"},
})
completar(Q, R)
