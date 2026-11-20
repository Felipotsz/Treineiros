# Enem 2011, 1º dia, caderno azul: Ciências da Natureza (questões 46 a 90; no site, 1 a 45). Em 2011 a Natureza era no 1º dia.
# Texto legível. Quadros das Q49, Q50, Q54 e Q77 e equações das Q75 e Q81 em HTML. Poema da Q87 (Vinicius de Moraes) como imagem.
# Sem anuladas nesta área.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, paragrafos_enem

ID = "enem-2011-natureza"
META = {"id": ID, "banca": "Enem", "ano": 2011, "titulo": "Enem 2011: Ciências da Natureza", "fonte": "Inep", "dataExame": "2011-10-22",
        "duracaoMinutos": 150, "area": "Ciências da Natureza", "caderno": "azul", "dia": 1}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2011-dia1-azul")
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


def X(n, materia, assunto, expl, imagens=(), tags=(), enun=None, trocas=(), alts=None, anulacao=None):
    e = LIMPA(enun or E(n))
    for a, b in trocas:
        assert a in e, a; e = e.replace(a, b)
    Q[n - 45] = {"materia": materia, "assunto": assunto, "area": "Ciências da Natureza", "tags": list(tags), "numeroOriginal": n,
                 "enunciado": e, "alternativas": {k: LIMPA(v) for k, v in dict(alts or D[n]["alternativas"]).items()},
                 "imagens": list(imagens), "explicacao": expl}
    if anulacao: Q[n - 45]["anulacao"] = anulacao


SUB = lambda s: re.sub(r"(?<=[A-Za-z\)])(\d+)", r"<sub>\1</sub>", s)
LISTA = lambda s: "<ul>" + "".join(f"<li>{x.strip()}</li>" for x in s.split("•") if x.strip()) + "</ul>"
EQ = lambda *xs: '<p class="apoio">' + "<br>".join(xs) + "</p>"
SUP = lambda s: s.replace("m/s2", "m/s<sup>2</sup>").replace("g/cm3", "g/cm<sup>3</sup>").replace("mm3", "mm<sup>3</sup>")


X(46, "Física", "Termodinâmica", "<p>O movimento browniano é aleatório: as partículas empurram as palhetas tanto num sentido quanto no outro, e em média o eixo não giraria. A engrenagem com trava só deixa o eixo girar num sentido. Ela serve para <strong>a determinação do movimento, devido ao caráter aleatório, cuja tendência é o equilíbrio</strong>. Alternativa <strong>D</strong>.</p><p>A trava não controla a velocidade (B) nem mede ângulos (E).</p>",
  figs(("q46", "Esquema de um eixo com palhetas numa ponta, uma engrenagem com dentes assimétricos na outra e uma polia no meio, da qual pende um peso.")), ["movimento browniano", "catraca"])
X(47, "Biologia", "Ecologia", "<p>O homem comeu frutas e grãos, então é consumidor primário. O tigre que comer o homem será consumidor secundário, e os abutres que comerem o tigre, consumidores terciários. A resposta é <strong>consumidor secundário e consumidor terciário</strong>. Alternativa <strong>C</strong>.</p><p>Os abutres comem carniça, mas aqui se alimentam do tigre, que já é consumidor secundário.</p>",
  figs(("q47", "Desenho em que um tigre-dentes-de-sabre pensa em comer um homem das cavernas, o homem pensa em caçar o tigre, e abutres empoleirados numa rocha pensam em comer os dois.")), ["níveis tróficos", "cadeia alimentar"])
X(48, "Biologia", "Fisiologia humana", "<p>As hemácias têm hemoglobina, que leva o oxigênio dos pulmões aos tecidos. Se o cavalo perdesse muitas hemácias nas sangrias, ficaria anêmico e teria <strong>problemas no transporte de oxigênio</strong>. Por isso elas são devolvidas pela plasmaferese. Alternativa <strong>E</strong>.</p><p>A imunidade (B) depende dos glóbulos brancos e dos anticorpos, e não das hemácias.</p>",
  tags=["hemácias", "soro antiofídico"])
X(49, "Biologia", "Fisiologia humana", "<p>O paciente tem plaquetas abaixo do normal (200 000, contra 250 000 a 400 000). As plaquetas atuam na coagulação, por isso há sangramento nasal. Também tem menos glóbulos vermelhos, o que explica o cansaço. A afirmação correta é que <strong>o sangramento nasal é devido à baixa quantidade de plaquetas, que são responsáveis pela coagulação sanguínea</strong>. Alternativa <strong>A</strong>.</p><p>Os glóbulos brancos estão normais e cuidam da defesa (B e D).</p>",
  tags=["hemograma", "plaquetas"],
  enun=p(T(49, 0)) + tabela(["Constituinte", "Número normal", "Paciente"], [["Glóbulos vermelhos", "4,8 milhões/mm<sup>3</sup>", "4 milhões/mm<sup>3</sup>"], ["Glóbulos brancos", "(5 000 – 10 000)/mm<sup>3</sup>", "9 000/mm<sup>3</sup>"], ["Plaquetas", "(250 000 – 400 000)/mm<sup>3</sup>", "200 000/mm<sup>3</sup>"]])
       + fonte(T(49, 2).replace("Corpo Humano: fundamentos de anatomia e fisiologia", "<em>Corpo Humano: fundamentos de anatomia e fisiologia</em>")) + p(T(49, 3)))
X(50, "Química", "Termoquímica", "<p>Divide-se o CO<sub>2</sub> liberado (número de carbonos) pela energia: benzeno 6/3 268 ≈ 1,84 × 10<sup>−3</sup>; etanol 2/1 368 ≈ 1,46 × 10<sup>−3</sup>; glicose 6/2 808 ≈ 2,14 × 10<sup>−3</sup>; metano 1/890 ≈ 1,12 × 10<sup>−3</sup>; octano 8/5 471 ≈ 1,46 × 10<sup>−3</sup> mol de CO<sub>2</sub> por kJ. A que mais libera é a <strong>glicose</strong>. Alternativa <strong>C</strong>.</p><p>O metano (B) é o que menos emite por energia.</p>",
  tags=["calor de combustão", "CO2"],
  enun=p(T(50, 0).replace("(∆Hcº)", "(∆H<sub>c</sub>º)").replace("seu ∆Hcº", "seu ∆H<sub>c</sub>º")) + tabela(["Substância", "Fórmula", "∆H<sub>c</sub>º (kJ/mol)"], [["benzeno", "C<sub>6</sub>H<sub>6</sub> (l)", "−3 268"], ["etanol", "C<sub>2</sub>H<sub>5</sub>OH (l)", "−1 368"], ["glicose", "C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> (s)", "−2 808"], ["metano", "CH<sub>4</sub> (g)", "−890"], ["octano", "C<sub>8</sub>H<sub>18</sub> (l)", "−5 471"]])
       + fonte("ATKINS, P. <em>Princípios de Química</em>. Bookman, 2007 (adaptado).") + p(T(50, 3)))
X(51, "Biologia", "Questão ambiental", "<p>O biodigestor transforma restos orgânicos (cascas de mandioca, esterco) em biogás, um combustível barato produzido na própria região. É uma solução rápida que não usa lenha da mata nem encarece a farinha: <strong>construção de biodigestores, para a produção de gás combustível a partir de resíduos orgânicos da região</strong>. Alternativa <strong>D</strong>.</p><p>Plantar árvores (B) demora anos para dar lenha, e fornos elétricos grandes (A) são caros.</p>",
  tags=["biogás", "Mata Atlântica"])
X(52, "Biologia", "Saúde e saneamento", "<p>A diarreia vem de microrganismos na água do rio. Para eliminá-los, é preciso desinfetar a água, e o procedimento adequado é a <strong>cloração</strong>: o cloro mata bactérias e outros patógenos. Alternativa <strong>B</strong>.</p><p>Filtração, coagulação e decantação (A, C e E) retiram partículas, mas não garantem a morte dos microrganismos. A fluoretação (D) previne cáries.</p>",
  tags=["tratamento de água", "cloro"], trocas=[("O Liberal", "<em>O Liberal</em>")])
X(53, "Biologia", "Imunologia", "<p>A vacina estimula o organismo a produzir anticorpos e células de memória contra o HPV, sem causar a doença. Quando o vírus de verdade aparece, a resposta é rápida e forte. O benefício vem da <strong>presença de células de memória que atuam na resposta secundária</strong>. Alternativa <strong>E</strong>.</p><p>Os anticorpos (B) caem com o tempo; o que garante a proteção duradoura é a memória imunológica.</p>",
  tags=["vacina", "HPV"])
X(54, "Química", "Misturas", "<p>Fazendo a média das densidades pela porcentagem em massa: I, 0,60 × 7,3 + 0,40 × 11,3 = 8,90; II, 0,62 × 7,3 + 0,38 × 11,3 = 8,82; III, 8,70; IV, 0,63 × 7,3 + 0,37 × 11,3 = 8,78; V, 8,94. Só <strong>II e IV</strong> ficam entre 8,74 e 8,82 g/mL. Alternativa <strong>C</strong>.</p><p>A questão supõe que a densidade da liga é a média ponderada pelas massas; é uma simplificação, mas é o cálculo esperado.</p>",
  tags=["densidade", "ligas metálicas"],
  enun=p(T(54, 0).replace("estanhochumbo", "estanho-chumbo")) + tabela(["Amostra", "Porcentagem de Sn (%)", "Porcentagem de Pb (%)"], [["I", "60", "40"], ["II", "62", "38"], ["III", "65", "35"], ["IV", "63", "37"], ["V", "59", "41"]])
       + fonte("Disponível em: http://www.eletrica.ufpr.br.") + p("Com base no texto e na análise realizada pelo técnico, as amostras que atendem às normas internacionais são"))
X(55, "Química", "Polaridade", "<p>O óleo de mamona é apolar (lipofílico). Se as substâncias tóxicas não se dissolvem nele, é porque são polares: têm afinidade pela água. A característica é a <strong>hidrofilia</strong>. Alternativa <strong>B</strong>.</p><p>“Semelhante dissolve semelhante”: substâncias lipofílicas (A) se dissolveriam no óleo.</p>",
  tags=["solubilidade", "mamona"],
  enun=ap(T(55, 0)) + fonte("<em>Revista Química Nova na Escola</em>. V. 32, n<sup>o</sup> 1, 2010 (adaptado).") + p(T(55, 1).split("(adaptado). ", 1)[1]))
X(56, "Física", "Eletromagnetismo", "<p>O captador funciona porque o ímã magnetiza a corda de aço, e a vibração da corda muda o fluxo magnético na bobina, induzindo corrente. O náilon não é ferromagnético: ele <strong>apresenta uma magnetização desprezível sob a ação do ímã permanente</strong>, e sua vibração não muda o fluxo. Alternativa <strong>C</strong>.</p><p>A corrente não passa pela corda (A): ela é induzida na bobina.</p>",
  tags=["indução eletromagnética", "guitarra"])
X(57, "Biologia", "Ecologia", "<p>A microvespa põe seus ovos dentro dos ovos da borboleta, e as larvas dela consomem o conteúdo, impedindo o nascimento da lagarta. É uma relação de parasitismo usada no controle: a <strong>introdução de um parasita no ambiente da espécie que se deseja combater</strong>. Alternativa <strong>A</strong>.</p><p>Não há genes letais (B) nem inseticidas (E), e a vespa não compete com a borboleta (C).</p>",
  tags=["controle biológico", "parasitismo"], trocas=[("Trichogramma sp.", "<em>Trichogramma</em> sp.")])
X(58, "Química", "Interações intermoleculares", "<p>A glicerina e o polietilenoglicol têm grupos OH. O hidrogênio ligado ao oxigênio forma ligações de hidrogênio com as moléculas de água do ar, que ficam retidas na pele. A interação é por <strong>ligações de hidrogênio</strong>. Alternativa <strong>E</strong>.</p><p>Forças de London (B) são as interações fracas entre moléculas apolares.</p>",
  figs(("q58a", "Fórmula estrutural da glicerina: cadeia de três carbonos, H2C–CH–CH2, cada um com um grupo OH."),
       ("q58b", "Fórmula do polietilenoglicol: HO–CH2–CH2–[O–CH2–CH2]n–O–CH2–CH2–OH.")),
  ["ligação de hidrogênio", "umectantes"], enun=E(58, pular=(2, 4)))
X(59, "Biologia", "Fisiologia celular", "<p>A cal em suspensão deixa o meio muito concentrado. Os microrganismos do tronco perdem água para esse meio por osmose e morrem desidratados. O processo é a <strong>osmose, pois a cal retira água do microambiente</strong>. Alternativa <strong>B</strong>.</p><p>A cal não precisa de luz (C e D) para agir.</p>",
  tags=["osmose", "caiação"])
X(60, "Física", "Eletrodinâmica", "<p>Com a mesma potência, P = U²/R, então R = U²/P. A razão é R<sub>A</sub>/R<sub>B</sub> = (127/220)² ≈ 0,33, ou seja, <strong>0,3</strong>. Alternativa <strong>A</strong>.</p><p>O modelo de 127 V precisa de mais corrente para a mesma potência, por isso o disjuntor de 50 A, enquanto o de 220 V usa 30 A, 40% a menos.</p>",
  figs(("q60", "Quadro “Características técnicas”: modelo A, 127 V; modelo B, 220 V. Potências pelo seletor de temperatura: desligado, 0 e 0 W; uma bolinha, 2 440 e 2 540 W; duas, 4 400 e 4 400 W; três, 5 500 e 6 000 W. Disjuntor ou fusível: 50 A e 30 A. Seção dos condutores: 10 mm² e 4 mm².")),
  ["potência elétrica", "resistência"], trocas=[("RA e RB", "R<sub>A</sub> e R<sub>B</sub>")])
X(61, "Biologia", "Genética molecular", "<p>Meselson e Stahl cultivaram bactérias em nitrogênio pesado e depois em nitrogênio leve. Após uma geração, todo o DNA tinha densidade intermediária: cada molécula nova tinha uma fita antiga e uma nova. A replicação é <strong>semiconservativa, isto é, as fitas filhas consistem de uma fita parental e uma recém-sintetizada</strong>. Alternativa <strong>C</strong>.</p><p>A opção E usa termos errados: nenhuma das fitas é “codificadora” nesse sentido.</p>",
  tags=["replicação", "Meselson e Stahl"], trocas=[("Introdução à Genética", "<em>Introdução à Genética</em>")])
X(62, "Química", "Química ambiental", "<p>Os produtores assimilam C, N e P na razão 106 : 16 : 1. Dividindo as concentrações por esses números: C, 21,2/106 = 0,2; N, 1,2/16 = 0,075; P, 0,2/1 = 0,2. O menor valor é o do nitrogênio, que acaba primeiro: o nutriente limítrofe é o <strong>N</strong>. Alternativa <strong>B</strong>.</p><p>Olhar só as concentrações absolutas levaria a escolher o fósforo (C).</p>",
  figs(("q62", "Esquema do ciclo de nutrientes num lago: fósforo de fosfatos (solo, detergentes, esgoto), nitrogênio da atmosfera e de nitratos e carbono do CO2 entram nos produtores primários, que os assimilam nas razões 106 : 16 : 1 de C, N e P. Os produtores alimentam peixes; restos vegetais e animais sofrem decomposição bacteriana, que devolve CO2, nitrato e fosfato, ou se sedimentam.")),
  ["eutrofização", "razão de Redfield"], alts={**D[62]["alternativas"], "D": "CO<sub>2</sub>.", "E": "PO<sub>4</sub><sup>3−</sup>."})
X(63, "Química", "Espectroscopia", "<p>No gráfico, a absorção máxima é perto de 500 nm. Na roda de cores, a faixa de 490 a 560 nm é o verde. A cor percebida é a oposta na roda, o <strong>vermelho</strong>. Alternativa <strong>E</strong>.</p><p>Verde (B) é a cor absorvida, e não a vista.</p>",
  figs(("q63a", "Figura 1: espectro de absorção, com intensidade de luz absorvida no eixo vertical e comprimento de onda de 400 a 700 nm no horizontal; a curva tem um máximo perto de 500 nm."),
       ("q63b", "Figura 2: roda de cores dividida em seis setores: vermelho (650 a 750 nm), laranja (580 a 650), amarelo (560 a 580), verde (490 a 560), azul (430 a 490) e violeta (400 a 430). Uma seta indica que, se a substância absorve numa região, apresenta a cor do setor oposto.")),
  ["cor", "absorção de luz"])
X(64, "Biologia", "Saúde e doenças", "<p>Na América do Sul, o mapa mostra a malária concentrada na região amazônica, onde ela ocorre de forma constante. Uma doença que se mantém numa área restrita, ano após ano, é uma <strong>endemia</strong>. Alternativa <strong>A</strong>.</p><p>Epidemia (C) é um aumento repentino de casos, e pandemia (E) é a difusão por vários continentes.</p>",
  figs(("q64", "Mapa-múndi da malária (OMS, 2004): áreas de transmissão em grande parte da África, no sul da Ásia e, na América do Sul, sobretudo na região amazônica; áreas de risco limitado em volta; o resto do mundo sem malária.")),
  ["malária", "endemia"])
X(65, "Biologia", "Genética", "<p>A epigenética estuda mudanças na expressão dos genes sem alterar a sequência de DNA, como a metilação de bases, que silencia genes. Os cânceres epigenéticos acontecem pela <strong>inativação de genes por meio de modificações nas bases nitrogenadas</strong>. Alternativa <strong>E</strong>.</p><p>Aneuploidias e mutações (A, B, C e D) mudam o material genético, e não só sua expressão.</p>",
  tags=["epigenética", "metilação"], trocas=[("A reabilitação do herege", "<em>A reabilitação do herege</em>"), ("Época", "<em>Época</em>")])
X(66, "Física", "Termodinâmica", "<p>O texto diz que parte da energia da combustão não pode ser usada para trabalho: “há vazamento da energia em outra forma”, como calor. É a segunda lei da termodinâmica: a <strong>conversão integral de calor em trabalho é impossível</strong>. Alternativa <strong>C</strong>.</p><p>A liberação de calor (A) é justamente o que acontece.</p>",
  tags=["segunda lei", "rendimento"], trocas=[("Física Térmica", "<em>Física Térmica</em>")])
X(67, "Física", "Ondas", "<p>Para distinguir os alvos, a banda deve ser aquela em que as curvas ficam mais separadas. Entre 0,8 e 0,9 µm, a grama reflete cerca de 50%, o concreto 35%, o solo arenoso de 20% a 25%, o asfalto 8% e a água quase nada. A melhor banda é <strong>0,8 a 0,9</strong>. Alternativa <strong>E</strong>.</p><p>Na faixa de 0,6 a 0,7 (C), várias curvas se cruzam.</p>",
  figs(("q67", "Gráfico de refletância (%) por comprimento de onda de 0,4 a 0,9 µm para grama, concreto, solo arenoso, asfalto e água. A grama tem um pico pequeno perto de 0,55 e sobe muito depois de 0,7, chegando a 50%; o concreto fica por volta de 35%; o solo arenoso sobe aos poucos até cerca de 30%; o asfalto fica perto de 8%; a água cai a quase zero.")),
  ["sensoriamento remoto", "refletância"])
X(68, "Biologia", "Biotecnologia", "<p>Os cientistas sintetizaram um cromossomo inteiro e o puseram para comandar outra célula. Se é possível montar genomas no laboratório, abre-se a <strong>possibilidade de programar geneticamente microrganismos ou seres mais complexos para produzir medicamentos, vacinas e combustíveis</strong>. Alternativa <strong>D</strong>.</p><p>Não se criou vida a partir de carboidratos e lipídios (B): usou-se uma célula existente.</p>",
  tags=["célula sintética", "genoma"], trocas=[("Mycoplasma mycoides", "<em>Mycoplasma mycoides</em>"), ("Mycoplasma capricolum", "<em>Mycoplasma capricolum</em>"), ("M. capricolum", "<em>M. capricolum</em>"), ("M. mycoides", "<em>M. mycoides</em>")])
X(69, "Biologia", "Imunologia", "<p>A vacina contém o agente atenuado, inativado ou partes dele. O corpo reconhece esses antígenos e produz anticorpos e células de memória. Ela <strong>estimula a produção de anticorpos contra o agente causador da doença</strong>. Alternativa <strong>E</strong>.</p><p>Quem já contém anticorpos prontos é o soro (A).</p>",
  tags=["vacina", "H1N1"])
X(70, "Física", "Eletrodinâmica", "<p>A lâmpada só acende se a corrente passar por ela: um polo da pilha precisa tocar a ponta de baixo da lâmpada e o outro, a rosca lateral, fechando o circuito. Isso acontece nos esquemas <strong>(1), (3) e (7)</strong>. Alternativa <strong>D</strong>.</p><p>Nos demais, os dois contatos vão para o mesmo ponto da lâmpada, ou a pilha fica em curto, sem passar corrente pelo filamento.</p>",
  figs(("q70", "Sete esquemas numerados de uma pilha, uma lâmpada e um fio, em posições diferentes: em alguns, a ponta da lâmpada toca um polo e o fio liga a rosca ao outro polo; em outros, o fio liga os dois polos da pilha ou a lâmpada toca a pilha só por um contato.")),
  ["circuito elétrico", "lâmpada"], trocas=[("Instalação Elétrica: investigando e aprendendo", "<em>Instalação Elétrica: investigando e aprendendo</em>")])
X(71, "Química", "Energia", "<p>O texto apresenta os biocombustíveis de segunda geração como alternativa aos de primeira, por usarem matérias-primas baratas e abundantes. Eles poluem menos e geram empregos, mas a tecnologia de quebra da celulose precisa ser eficiente para baixar o custo. Alternativa <strong>A</strong>.</p><p>As alternativas B, C e E dizem que eles não geram empregos ou destroem empregos, o que o texto não afirma.</p>",
  tags=["biocombustíveis", "celulose"], trocas=[("Scientific American Brasil", "<em>Scientific American Brasil</em>")])
X(72, "Química", "Funções orgânicas", "<p>A amida se forma quando o grupo amina (–NH<sub>2</sub>) reage com uma carboxila (–COOH), liberando água. No ácido cólico, o único grupo carboxila está na ponta da cadeia lateral. A reação é com o grupo <strong>carboxila do ácido cólico</strong>. Alternativa <strong>A</strong>.</p><p>As hidroxilas (C) do ácido cólico formariam ésteres, e não amidas.</p>",
  figs(("q72", "Fórmula estrutural do ácido cólico: quatro anéis fundidos (núcleo esteroide), com três grupos OH e uma cadeia lateral terminada em carboxila (–COOH).")),
  ["amida", "sais biliares"], enun=E(72, pular=(2,)), trocas=[("prefixo glico-", "prefixo <em>glico-</em>"), ("prefixo tauro-", "prefixo <em>tauro-</em>")])
X(73, "Física", "Hidrostática", "<p>No ar, o dinamômetro marca 30 N; com meio cubo na água, 24 N. O empuxo é 30 − 24 = 6 N. O volume submerso é metade de 1 000 cm³, ou 5 × 10<sup>−4</sup> m³. Empuxo = d · V · g: 6 = d × 5 × 10<sup>−4</sup> × 10, então d = 1 200 kg/m³ = <strong>1,2 g/cm³</strong>. Alternativa <strong>B</strong>.</p>",
  figs(("q73", "Dinamômetro D segurando um cubo mergulhado até a metade na água de um lago.")), ["empuxo", "densidade"], enun=SUP(E(73)))
X(74, "Física", "Ondas", "<p>A luz é muito atenuada pelos sedimentos: não os atravessa. O som, por sua vez, penetra nessas camadas e é refletido, formando imagens. O sonar é melhor porque a <strong>atenuação da luz nos materiais analisados é distinta da atenuação de som nestes mesmos materiais</strong>. Alternativa <strong>D</strong>.</p><p>A velocidade da luz (A) não importa aqui: o que importa é o quanto cada onda atravessa.</p>",
  tags=["sonar", "atenuação"], trocas=[("O Estado de São Paulo", "<em>O Estado de São Paulo</em>")])
X(75, "Química", "Equilíbrio químico", "<p>O açúcar do refrigerante é fermentado pelas bactérias da placa, que produzem ácido. O aumento de H<sup>+</sup> consome os íons OH<sup>−</sup> (formando água), e o equilíbrio se desloca para a direita, dissolvendo a hidroxiapatita. É o aumento de <strong>H<sup>+</sup>, que reage com as hidroxilas OH<sup>−</sup>, deslocando o equilíbrio para a direita</strong>. Alternativa <strong>B</strong>.</p>",
  tags=["Le Chatelier", "cárie"],
  enun=ap(T(75, 0).replace("Sabese", "Sabe-se")) + EQ("Ca<sub>5</sub>(PO<sub>4</sub>)<sub>3</sub>OH (s) ⇄ 5 Ca<sup>2+</sup> (aq) + 3 PO<sub>4</sub><sup>3−</sup> (aq) + OH<sup>−</sup> (aq)", "(Hidroxiapatita; sentido direto: desmineralização; sentido inverso: mineralização)")
       + fonte(T(75, 2)) + p(T(75, 3)),
  alts={"A": "OH<sup>−</sup>, que reage com os íons Ca<sup>2+</sup>, deslocando o equilíbrio para a direita.", "B": "H<sup>+</sup>, que reage com as hidroxilas OH<sup>−</sup>, deslocando o equilíbrio para a direita.",
        "C": "OH<sup>−</sup>, que reage com os íons Ca<sup>2+</sup>, deslocando o equilíbrio para a esquerda.", "D": "H<sup>+</sup>, que reage com as hidroxilas OH<sup>−</sup>, deslocando o equilíbrio para a esquerda.",
        "E": "Ca<sup>2+</sup>, que reage com as hidroxilas OH<sup>−</sup>, deslocando o equilíbrio para a esquerda."})
X(76, "Biologia", "Ecologia", "<p>O senso comum diz que lagartas comem de tudo. O texto mostra que as larvas das Ithomiinae comem sobretudo plantas da família Solanaceae, a do tomate, depois de seus ancestrais terem comido Apocinaceae. Elas apresentam <strong>especificidade pelas plantas da família Solanaceae existentes nesses locais</strong>. Alternativa <strong>E</strong>.</p><p>A relação com as Apocinaceae (B) era dos ancestrais.</p>",
  tags=["herbivoria", "especificidade alimentar"], trocas=[("Revista Pesquisa FAPESP", "<em>Revista Pesquisa FAPESP</em>")])
X(77, "Física", "Cinemática", "<p>A régua cai em queda livre: sua velocidade aumenta, porque o peso é constante e produz aceleração constante (g). A distância cresce com o quadrado do tempo (d = gt²/2): dobrar o tempo quadruplica a distância. A razão é que a <strong>força peso da régua tem valor constante, o que gera um movimento acelerado</strong>. Alternativa <strong>D</strong>.</p><p>A aceleração não varia (C), e a velocidade não é constante (E).</p>",
  tags=["queda livre", "tempo de reação"],
  enun=p(T(77, 0)) + "<ol type=\"I\"><li>" + "</li><li>".join(x.strip() for x in re.split(r"\b(?:I|II|III)\. ", T(77, 1).split(" O quadro seguinte")[0]) if x.strip()) + "</li></ol>"
       + p("O quadro seguinte" + T(77, 1).split(" O quadro seguinte")[1]) + tabela(["Distância percorrida pela régua durante a queda (metro)", "Tempo de reação (segundo)"], [["0,30", "0,24"], ["0,15", "0,17"], ["0,10", "0,14"]]) + fonte(T(77, 3)) + p(T(77, 4)))
X(78, "Física", "Hidrostática", "<p>Na válvula de descarga, a água sai enquanto o botão está apertado, e muita gente segura por mais tempo do que o necessário. Na caixa acoplada, cada acionamento libera só a água do tanque, um volume fixo. A economia se deve <strong>ao volume do tanque de água</strong>. Alternativa <strong>B</strong>.</p>",
  figs(("q78", "Esquema de um vaso sanitário com caixa acoplada: válvula de enchimento, boia, tubo de transbordo, alavanca, tanque, válvula de descarga, assento, distribuidor de água, vaso e sifão.")),
  ["caixa acoplada", "economia de água"])
X(79, "Biologia", "Ecologia", "<p>No lixão enterrado, a matéria orgânica fica sem oxigênio. Bactérias anaeróbias a decompõem e produzem metano (biogás), que pode se acumular e explodir. O metano é produzido <strong>pela degradação anaeróbia de matéria orgânica por bactérias</strong>. Alternativa <strong>B</strong>.</p><p>A respiração aeróbia (A) produz CO<sub>2</sub>, e não metano.</p>",
  tags=["metano", "decomposição"])
X(80, "Química", "Química ambiental", "<p>O texto lembra que estudos indicam que as hidrelétricas emitem metano (da decomposição da vegetação alagada) em quantidades comparáveis às emissões de CO<sub>2</sub> das termelétricas. Como elas respondem por 80% da matriz, seriam uma fonte <strong>poluidora, colaborando com níveis altos de gases de efeito estufa em função de seu potencial de oferta</strong>. Alternativa <strong>D</strong>.</p><p>O texto contradiz a ideia de energia “limpa” (A e C).</p>",
  tags=["hidrelétricas", "metano"], trocas=[("Revista Ciência Hoje", "<em>Revista Ciência Hoje</em>")])
X(81, "Química", "Estequiometria", "<p>A solução tem 0,020 L × 0,1 mol/L = 2,0 × 10<sup>−3</sup> mol de H<sub>2</sub>O<sub>2</sub>. Pela equação, 5 mol de H<sub>2</sub>O<sub>2</sub> reagem com 2 mol de KMnO<sub>4</sub>: 2,0 × 10<sup>−3</sup> × 2/5 = <strong>8,0 × 10<sup>−4</sup> mol</strong>. Alternativa <strong>D</strong>.</p><p>A opção B (2,0 × 10<sup>−3</sup>) é a quantidade de peróxido, e não de permanganato.</p>",
  tags=["proporção estequiométrica", "concentração"],
  enun=p(T(81, 0)) + EQ("5 H<sub>2</sub>O<sub>2</sub> (aq) + 2 KMnO<sub>4</sub> (aq) + 3 H<sub>2</sub>SO<sub>4</sub> (aq) → 5 O<sub>2</sub> (g) + 2 MnSO<sub>4</sub> (aq) + K<sub>2</sub>SO<sub>4</sub> (aq) + 8 H<sub>2</sub>O (l)")
       + fonte("ROCHA-FILHO, R. C. R.; SILVA, R. R. <em>Introdução aos Cálculos da Química</em>. São Paulo: McGraw-Hill, 1992.") + p(T(81, 3)),
  alts={k: f"{a}×10<sup>{e}</sup> mol." for k, a, e in zip("ABCDE", ["2,0", "2,0", "8,0", "8,0", "5,0"], ["0", "−3", "−1", "−4", "−3"])})
X(82, "Biologia", "Ecologia", "<p>A fêmea de <em>Photuris</em> imita o sinal das fêmeas de <em>Photinus</em> para atrair os machos e devorá-los. Um organismo mata e come outro de espécie diferente: é <strong>predatismo</strong>. Alternativa <strong>D</strong>.</p><p>No comensalismo e no mutualismo (A e E), nenhuma das espécies é prejudicada.</p>",
  tags=["relações ecológicas", "mimetismo"], trocas=[("Photuris", "<em>Photuris</em>"), ("Photinus", "<em>Photinus</em>"), ("a relação descrita", "A relação descrita")])
X(83, "Química", "Química ambiental", "<p>O nitrogênio dos adubos vira íons como nitrato (NO<sub>3</sub><sup>−</sup>) e amônio (NH<sub>4</sub><sup>+</sup>), muito solúveis em água. A chuva os leva para rios e lagos, causando eutrofização. A consequência é <strong>a contaminação de rios e lagos devido à alta solubilidade de íons como NO<sub>3</sub><sup>−</sup> e NH<sub>4</sub><sup>+</sup> em água</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["adubação", "ciclo do nitrogênio"], trocas=[("canade-açúcar", "cana-de-açúcar"), ("Revista Química Nova na Escola", "<em>Revista Química Nova na Escola</em>")],
  alts={**D[83]["alternativas"], "C": "a contaminação de rios e lagos devido à alta solubilidade de íons como NO<sub>3</sub><sup>−</sup> e NH<sub>4</sub><sup>+</sup> em água.", "D": "a diminuição do pH do solo pela presença de NH<sub>3</sub>, que reage com a água, formando o NH<sub>4</sub>OH (aq).",
        "E": "a diminuição da oxigenação do solo, uma vez que o nitrogênio ativo forma espécies químicas do tipo NO<sub>2</sub>, NO<sub>3</sub><sup>−</sup>, N<sub>2</sub>O."})
X(84, "Física", "Ondas", "<p>As figuras mostram a difração: quando o orifício é pequeno, a luz se espalha ao passar por ele, contornando as bordas. Com o som, isso acontece com facilidade, porque seu comprimento de onda é grande: por isso <strong>um menino escondido atrás de um muro ouve a conversa dos colegas</strong>. Alternativa <strong>A</strong>.</p><p>O eco (B) é reflexão, e a ambulância (D) é efeito Doppler.</p>",
  figs(("q84", "Três desenhos de uma lâmpada diante de uma parede com um buraco e um anteparo: com o buraco grande, os raios passam em linha reta; menor, passam num feixe estreito; muito pequeno, as ondas se espalham em arcos depois do buraco.")),
  ["difração", "som"], enun=p(T(84, 0)) + "[[fig:1]]" + fonte("FIOLHAIS, C. <em>Física divertida</em>. Brasília: UnB, 2000 (adaptado).") + p(T(84, 6)))
X(85, "Química", "Química ambiental", "<p>A desvantagem destacada é a emissão de poluentes na atmosfera. Filtros nas chaminés retêm partículas e gases antes da saída. A forma de minimizar é <strong>fomentar o uso de filtros nas chaminés dos incineradores para diminuir a poluição do ar</strong>. Alternativa <strong>B</strong>.</p><p>Aumentar o volume de lixo queimado (A, C e D) aumentaria a poluição.</p>",
  tags=["incineração", "poluição do ar"])
X(86, "Física", "Energia", "<p>Sem atrito, o atleta corre (energia cinética, etapa I), e essa energia passa pela vara (elástica) até virar energia potencial gravitacional no ponto mais alto (etapa III). Para a altura máxima, <strong>a energia cinética da etapa I deve ser totalmente convertida em energia potencial gravitacional na etapa III</strong>. Alternativa <strong>C</strong>.</p><p>Na etapa IV o atleta já está caindo no colchão.</p>",
  figs(("q86", "Quatro quadros do salto com vara: etapa I, atleta corre com a vara; etapa II, apoia a vara no chão; etapa III, atinge certa altura sobre o sarrafo; etapa IV, cai num colchão.")),
  ["conservação de energia", "salto com vara"])
X(87, "Biologia", "Classificação dos seres vivos", "<p>O poema chama de irmãos a mosca, o besouro, a barata, a borboleta e o grilo, que são insetos. Entre humanos e insetos, a categoria comum mais próxima é o <strong>reino</strong> animal: são de filos diferentes (cordados e artrópodes). Alternativa <strong>B</strong>.</p><p>Filo, classe, família e espécie (A, C, D e E) já separam humanos de insetos.</p>",
  figs(("q87", "Poema “Os bichinhos e o homem”, da Arca de Noé, de Toquinho e Vinicius de Moraes: o eu lírico chama de irmãos a mosca, o mosquito, o besouro, a barata, a borboleta e o grilo, com comentários bem-humorados sobre cada um.")),
  ["taxonomia", "reino Animalia"], enun="[[fig:1]]" + p(T(87, 2).replace("ente os animais", "entre os animais")))
X(88, "Biologia", "Ecologia", "<p>Os animais liberam resíduos nitrogenados, que poluem a água. As algas os absorvem como nutrientes e, na fotossíntese, produzem matéria orgânica e liberam oxigênio, usado pelos animais. A proposta é boa porque <strong>as algas usam os resíduos nitrogenados provenientes do metabolismo dos animais e, durante a síntese de compostos orgânicos, liberam oxigênio para o ambiente</strong>. Alternativa <strong>D</strong>.</p><p>As algas fazem fotossíntese, e não quimiossíntese (E).</p>",
  tags=["biofiltros", "fotossíntese"], trocas=[("Revista Ciência Hoje", "<em>Revista Ciência Hoje</em>")])
X(89, "Biologia", "Saúde e doenças", "<p>O <em>Aedes aegypti</em> põe ovos em água parada e limpa, e as larvas se desenvolvem nela. A medida eficaz é a <strong>remoção dos recipientes que possam acumular água</strong>, como pneus, vasos e garrafas. Alternativa <strong>C</strong>.</p><p>O barbeiro, transmissor da doença de Chagas, é que vive nas paredes de barro (B).</p>",
  tags=["dengue", "Aedes aegypti"],
  enun=p(T(89, 0) + " " + T(89, 1) + " <em>Aedes aegypti</em>, transmissor do vírus da dengue.", T(89, 3)))
X(90, "Biologia", "Questão ambiental", "<p>Os bovinos são ruminantes: no estômago, microrganismos fermentam o capim e produzem metano, que o animal libera ao arrotar. O metano é um gás de efeito estufa muito mais potente que o CO<sub>2</sub>. A contribuição é pela emissão de <strong>metano durante o processo de digestão</strong>. Alternativa <strong>A</strong>.</p>",
  figs(("q90", "Tirinha de quatro quadros com vacas: “Colocaram a culpa do aquecimento global nas vacas.” “E o que faremos?” “Culparemos as galinhas.”")),
  ["metano", "pecuária"])

completar(Q, R)
