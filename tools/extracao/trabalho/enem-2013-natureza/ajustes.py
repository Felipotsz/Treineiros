# Enem 2013, 1º dia, caderno azul: Ciências da Natureza (questões 46 a 90; no site, 1 a 45). Em 2013 a Natureza era no 1º dia.
# Texto legível. Equações das Q49, 64 e 69 em HTML. Alternativas-imagem: Q55, 58, 68, 72 e 87.
# Sem anuladas nesta área.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, paragrafos_enem

ID = "enem-2013-natureza"
META = {"id": ID, "banca": "Enem", "ano": 2013, "titulo": "Enem 2013: Ciências da Natureza", "fonte": "Inep", "dataExame": "2013-10-26",
        "duracaoMinutos": 150, "area": "Ciências da Natureza", "caderno": "azul", "dia": 1}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2013-dia1-azul")
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


X(46, "Química", "Eletroquímica", "<p>Quando o polipirrol se oxida ou se reduz, precisa receber ou expulsar íons para compensar a carga. Esses íons vêm do eletrólito polimérico do meio, que contém um sal: ele <strong>permite a difusão dos íons promovida pela aplicação de diferença de potencial, fechando o circuito elétrico</strong>. Alternativa <strong>B</strong>.</p><p>No eletrólito, quem conduz são os íons, e não elétrons livres (D).</p>",
  figs(("q46", "Três esquemas de um sanduíche de três camadas: dois filmes escuros de polipirrol com um filme branco de eletrólito polimérico no meio. No do meio, sem corrente elétrica, ele fica reto. Nos outros dois, com corrente elétrica, ele se curva para um lado ou para o outro, conforme a polaridade (+ e −).")),
  ["polímeros condutores", "oxirredução"], enun=p(T(46, 0)) + "[[fig:1]]" + fonte("DE PAOLI, M. A. <em>Cadernos Temáticos de Química Nova na Escola</em>, São Paulo, maio 2001 (adaptado).") + p(T(46, 3)))
X(47, "Química", "Mol", "<p>A quantidade recomendada é o dobro de 500 mg, ou 1 000 mg = 1 g de cálcio. Isso equivale a 1 ÷ 40 = 0,025 mol, e o número de átomos é 0,025 × 6 × 10<sup>23</sup> = <strong>1,5 × 10<sup>22</sup></strong>. Alternativa <strong>B</strong>.</p><p>A opção A (7,5 × 10<sup>21</sup>) corresponde aos 500 mg que o brasileiro consome, e não ao recomendado.</p>",
  tags=["constante de Avogadro", "massa molar"],
  enun=ap(T(47, 0)) + fonte(T(47, 1)) + p("Considerando-se o valor de 6 × 10<sup>23</sup> mol<sup>−1</sup> para a constante de Avogadro e a massa molar do cálcio igual a 40 g/mol, qual a quantidade mínima diária de átomos de cálcio a ser ingerida para que uma pessoa supra suas necessidades?"),
  alts={"A": "7,5 × 10<sup>21</sup>", "B": "1,5 × 10<sup>22</sup>", "C": "7,5 × 10<sup>23</sup>", "D": "1,5 × 10<sup>25</sup>", "E": "4,8 × 10<sup>25</sup>"})
X(48, "Física", "Termologia", "<p>Superfícies escuras absorvem mais radiação e, pela mesma razão, também a emitem melhor. Com a lâmpada acesa, a garrafa preta esquenta mais rápido; depois de desligada, perde calor mais rápido. A taxa de variação foi <strong>maior no aquecimento e maior no resfriamento</strong>. Alternativa <strong>E</strong>.</p><p>Um bom absorvedor de radiação é sempre um bom emissor, então o resfriamento não pode ser igual (B).</p>",
  figs(("q48", "Duas garrafas sobre uma bancada, cada uma com um termômetro: à esquerda, uma garrafa branca; à direita, uma garrafa preta; no meio, a igual distância, uma lâmpada acesa.")),
  ["radiação térmica", "corpo negro"], enun=p(T(48, 0)) + "[[fig:1]]" + p(T(48, 2)))
X(49, "Química", "Radioatividade", "<p>A cada meia-vida, a massa cai pela metade. Depois de cinco meias-vidas, sobra \\(\\dfrac{1}{2^5} = \\dfrac{1}{32}\\) da massa: 1 000 mg ÷ 32 ≈ <strong>31,3 mg</strong>. Alternativa <strong>D</strong>.</p><p>A opção A (0,200) divide a massa por 5, como se a queda fosse linear.</p>",
  tags=["meia-vida", "decaimento"],
  enun=p(T(49, 0)) + ap("<sup>11</sup><sub>6</sub>C → <sup>11</sup><sub>5</sub>B + <sup>0</sup><sub>1</sub>e (pósitron)") + p(T(49, 3), T(49, 4)))
X(50, "Biologia", "Imunologia", "<p>O menino teve uma forma branda da doença, produziu defesas e não adoeceu quando recebeu o vírus humano. Jenner criou a primeira vacina, o que abriu caminho para a <strong>prevenção de diversas doenças infectocontagiosas em todo o mundo</strong>. Alternativa <strong>A</strong>.</p><p>A vacina previne a doença; não é tratamento (C).</p>",
  tags=["vacina", "varíola"])
X(51, "Química", "Química ambiental", "<p>As termelétricas queimam carvão, óleo ou gás para gerar energia e liberam CO<sub>2</sub>, óxidos de enxofre e de nitrogênio e fuligem. A poluição do ar vem especialmente das <strong>termelétricas</strong>. Alternativa <strong>B</strong>.</p><p>Hidrelétricas, energia solar e eólica (A, D e E) causam impactos, mas praticamente não poluem o ar.</p>",
  tags=["Química Verde", "fontes de energia"], trocas=[("Química Verde: fundamentos e aplicações", "<em>Química Verde: fundamentos e aplicações</em>")])
X(52, "Física", "Ondas", "<p>Celulares e outros aparelhos emitem ondas de rádio com frequências próximas às usadas na comunicação dos pilotos. Ondas de <strong>frequências próximas</strong> podem interferir umas nas outras e atrapalhar a recepção. Alternativa <strong>E</strong>.</p><p>Ondas eletromagnéticas não são audíveis (B).</p>",
  tags=["interferência", "ondas de rádio"])
X(53, "Biologia", "Fisiologia", "<p>As vilosidades são dobras da parede do intestino; quanto mais vilosidades, maior a superfície em contato com o alimento digerido. Isso aumenta a <strong>área de contato com o conteúdo intestinal para absorção dos nutrientes</strong>. Alternativa <strong>B</strong>.</p><p>Vilosidades não aumentam o comprimento do intestino (A), nem atuam no estômago (D).</p>",
  tags=["vilosidades intestinais", "absorção"])
X(54, "Química", "Polímeros", "<p>O PET é um poliéster, formado pela reação entre um ácido e um álcool (o etilenoglicol) com saída de água. A reação inversa, com água, quebra as ligações éster e devolve o ácido e o álcool. A alternativa é a <strong>hidrólise dos objetos</strong>. Alternativa <strong>D</strong>.</p><p>Triturar ou fundir (C e E) só muda a forma do material, sem separar o etilenoglicol.</p>",
  figs(("q54", "Fórmula estrutural do PET: HO–C(=O)–anel benzênico–C(=O)–O–CH2–CH2–O–H, entre colchetes, repetida n vezes.")),
  ["poliéster", "reciclagem"], enun=p(T(54, 0)) + "[[fig:1]]" + fonte(T(54, 4)) + p(T(54, 5)))
X(55, "Biologia", "Fisiologia", "<p>A pílula fornece doses diárias e iguais de estrogênio e progesterona. Tomada sem interrupção, ela mantém as concentrações dos dois hormônios estáveis, sem o pico da ovulação: os níveis ficam <strong>constantes ao longo do tempo</strong>, como no gráfico A. Alternativa <strong>A</strong>.</p><p>Os gráficos B e C mostram variações típicas de um ciclo menstrual natural.</p>",
  figs(("q55a", "Alternativa A: duas retas horizontais, E e P, constantes ao longo do tempo."),
       ("q55b", "Alternativa B: as duas curvas sobem; P continua subindo e E sobe, cai e se estabiliza."),
       ("q55c", "Alternativa C: as duas curvas oscilam, com picos em momentos diferentes."),
       ("q55d", "Alternativa D: E e P crescem continuamente em linha reta."),
       ("q55e", "Alternativa E: E e P ficam constantes e depois crescem em linha reta.")),
  ["anticoncepcional", "hormônios"], enun=p(T(55, 0), T(55, 1)), alts=ALT(1))
X(56, "Biologia", "Fisiologia", "<p>Harvey pressionava a veia e empurrava o sangue em direção ao cotovelo; o trecho ficava vazio porque o sangue não conseguia voltar. Isso mostra que as veias têm <strong>válvulas</strong> que deixam o sangue correr num só sentido, de volta ao coração. Alternativa <strong>B</strong>.</p>",
  figs(("q56", "Ilustração antiga de dois antebraços com um torniquete no braço. No primeiro, as veias aparecem salientes com pontos marcados O e H. No segundo, os dedos de outra pessoa pressionam a veia no ponto H, deixando vazio o trecho entre H e O.")),
  ["circulação", "válvulas venosas"], trocas=[("livro De Motu Cordis", "livro <em>De Motu Cordis</em>")])
X(57, "Física", "Hidrostática", "<p>Tampada, a garrafa não deixa o ar entrar; quando um pouco de água sai, a pressão interna sobre a superfície cai, e a pressão atmosférica de fora, maior, segura a água. Destampada, o ar atua tanto na superfície quanto no furo, e o efeito dele se anula: a velocidade depende só da altura da coluna de água acima do furo. Por isso, a pressão atmosférica <strong>impede a saída de água, por ser maior que a pressão interna; não muda a velocidade de escoamento, que só depende da pressão da coluna de água</strong>. Alternativa <strong>A</strong>.</p>",
  figs(("q57", "Garrafa PET destampada com três furos na lateral, em alturas diferentes; jatos de água saem dos furos, e o de baixo vai mais longe.")),
  ["pressão atmosférica", "teorema de Stevin"], enun=p(T(57, 0)) + "[[fig:1]]" + p(T(57, 2)))
X(58, "Química", "Química orgânica", "<p>Numerando a partir do carbono do aldeído (C1): a cadeia tem oito carbonos, duplas em C2 e C6 e metilas em C3 e C7; o isômero que mais contribui para o odor é o <em>trans</em>. A estrutura A tem as duplas nas posições certas, as metilas em 3 e 7, e o grupo aldeído do lado oposto à cadeia na dupla C2=C3, que é o <em>trans</em>. Alternativa <strong>A</strong>.</p><p>Em B, a metila está no C2, e não no C3; em C, D e E, a geometria ou as posições das duplas e metilas não correspondem à descrição.</p>",
  figs(("q58a", "Alternativa A: cadeia em zigue-zague terminada em aldeído, com duplas nas posições 2 e 6, metilas nas posições 3 e 7, e o aldeído do lado oposto à cadeia na dupla 2 (trans)."),
       ("q58b", "Alternativa B: cadeia com aldeído e duas duplas, mas com a metila no carbono 2, ao lado do aldeído."),
       ("q58c", "Alternativa C: cadeia com aldeído e duas duplas, com o aldeído do mesmo lado da cadeia na dupla 2 (cis)."),
       ("q58d", "Alternativa D: cadeia com aldeído e duas duplas, com a dupla distante deslocada para a posição 5."),
       ("q58e", "Alternativa E: cadeia com aldeído na posição cis e a dupla distante deslocada.")),
  ["isomeria geométrica", "nomenclatura"],
  enun=p(SUB(T(58, 0)).replace("gênero Apis", "gênero <em>Apis</em>").replace("o trans o", "o <em>trans</em> o"), T(58, 1)), alts=ALT(1))
X(59, "Biologia", "Ecologia", "<p>Quando uma árvore morre e cai, deixa de fazer fotossíntese, e seu corpo passa a ser decomposto por fungos e bactérias, que respiram e consomem O<sub>2</sub>. No local, a concentração de O<sub>2</sub> será <strong>menor, pois haverá consumo de O<sub>2</sub> durante a decomposição dessas árvores</strong>. Alternativa <strong>A</strong>.</p><p>A opção E fala da falta de fotossíntese, mas numa floresta madura a árvore já consumia o que produzia; o que pesa é a decomposição.</p>",
  tags=["decomposição", "ciclo do oxigênio"], trocas=[("CO2", "CO<sub>2</sub>"), ("O2", "O<sub>2</sub>")],
  alts={k: v.replace("O2", "O<sub>2</sub>") for k, v in D[59]["alternativas"].items()})
X(60, "Biologia", "Evolução", "<p>A fêmea bem nutrida produz mais ovos, e esses ovos carregam os genes do macho. Mesmo morrendo, o macho deixa mais descendentes do que deixaria de outra forma: o comportamento <strong>favorece o sucesso reprodutivo individual de ambos os parentais</strong>. Alternativa <strong>B</strong>.</p><p>A cópula acontece antes, então os genes do macho passam para a prole (C).</p>",
  tags=["seleção natural", "canibalismo sexual"], trocas=[("Tenodera aridofolia", "<em>Tenodera aridofolia</em>")])
X(61, "Física", "Hidrostática", "<p>O peso total é (65 + 15 + 20) × 10 = 1 000 N. Pelo princípio de Pascal, a pressão é a mesma nos dois lados: \\(\\dfrac{F}{A} = \\dfrac{1\\,000}{5A}\\), então F = <strong>200 N</strong>. Com velocidade constante, a força resultante é nula. Alternativa <strong>C</strong>.</p><p>A opção A (20 N) usa só o peso da plataforma.</p>",
  tags=["princípio de Pascal", "prensa hidráulica"], enun=p(T(61, 0) + " 10 m/s<sup>2</sup>, " + T(61, 1).replace("10 m/s2, ", ""), T(61, 2)))
X(62, "Biologia", "Biotecnologia", "<p>O cloroplasto tem DNA próprio e muitas cópias por célula, por isso produz muita proteína recombinante. Em leveduras, que não fazem fotossíntese, a organela equivalente, com DNA próprio, é a <strong>mitocôndria</strong>. Alternativa <strong>B</strong>.</p><p>Lisossomo, peroxissomo, golgiense e retículo (A, C, D e E) não têm material genético.</p>",
  tags=["DNA mitocondrial", "transgênicos"])
X(63, "Biologia", "Ecologia", "<p>Os peixes exóticos (mapará e corvina) têm nichos semelhantes aos dos cascudos e passaram a disputar os mesmos recursos. Disputa entre espécies diferentes é competição interespecífica: o desaparecimento se explica pelo <strong>aumento da competição interespecífica</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["espécies exóticas", "competição"], trocas=[("Ciência Hoje", "<em>Ciência Hoje</em>")])
X(64, "Química", "Equilíbrio químico", "<p>O HClO desinfeta cerca de 80 vezes melhor que o ClO<sup>−</sup>, então queremos que ele fique na forma não ionizada. Com pK<sub>a</sub> = 7,53, em pH abaixo desse valor predomina o HClO. Entre as opções, o pH mais adequado e possível de usar é <strong>5</strong>. Alternativa <strong>B</strong>.</p><p>pH 0 (A) é ácido demais e deslocaria o primeiro equilíbrio, liberando gás cloro; pH 9 e 14 favoreceriam o ClO<sup>−</sup>.</p>",
  tags=["pKa", "ácido hipocloroso"],
  enun=p(T(64, 0)) + ap("Cl<sub>2</sub> (g) + 2 H<sub>2</sub>O (l) ⇌ HClO (aq) + H<sub>3</sub>O<sup>+</sup> (aq) + Cl<sup>−</sup> (aq)", "HClO (aq) + H<sub>2</sub>O (l) ⇌ H<sub>3</sub>O<sup>+</sup> (aq) + ClO<sup>−</sup> (aq) &nbsp; pK<sub>a</sub> = −log K<sub>a</sub> = 7,53") + p(T(64, 2), T(64, 3)))
X(65, "Física", "Ondas", "<p>A velocidade é 45 km/h = 12,5 m/s. O comprimento de onda é 16 pessoas × 0,8 m = 12,8 m. Como v = λ·f, f = 12,5 ÷ 12,8 ≈ <strong>1,0 Hz</strong>. Alternativa <strong>C</strong>.</p><p>O período é o tempo que a onda leva para percorrer um comprimento de onda: 12,8 ÷ 12,5 ≈ 1 s, que dá a mesma frequência.</p>",
  figs(("q65", "Ilustração de uma fileira de pessoas na arquibancada: algumas sentadas, outras se levantando e uma em pé com os braços para cima, formando uma curva em forma de onda; uma seta indica o sentido de propagação.")),
  ["equação fundamental da ondulatória", "frequência"], enun=p(T(65, 0).replace("a ola mexicana", "a <em>ola</em> mexicana")) + "[[fig:1]]" + p(T(65, 2)) + fonte(T(65, 3)) + p(T(65, 4).replace("Nessa ola", "Nessa <em>ola</em>")))
X(66, "Física", "Movimento circular", "<p>Polias ligadas pela mesma correia têm a mesma velocidade linear na borda; a maior gira com menor frequência. Na montagem Q, o motor (polia 1) liga direto na polia 3, a maior, que gira devagar e move a serra mais lentamente. Por isso, Q, <strong>pois as polias 1 e 3 giram com velocidades lineares iguais em pontos periféricos e a que tiver maior raio terá menor frequência</strong>. Alternativa <strong>A</strong>.</p><p>Polias ligadas por correia não giram com frequências iguais (B).</p>",
  figs(("q66", "Duas montagens com um motor (polia 1, pequena) e uma serra de fita presa às polias 2 e 3, que são concêntricas. Na montagem P, a correia liga a polia 1 à polia 2, a menor das concêntricas. Na montagem Q, a correia liga a polia 1 à polia 3, a maior.")),
  ["polias", "transmissão de movimento"], enun=p(T(66, 0)) + "[[fig:1]]" + p(T(66, 6)))
X(67, "Química", "Química ambiental", "<p>A matéria orgânica do solo guarda carbono. Mantendo palha e restos de culturas, fazendo plantio direto e evitando queimadas, mais carbono fica no solo, e menos CO<sub>2</sub> vai para o ar. A prática que ajuda é <strong>aumentar a quantidade de matéria orgânica do solo</strong>. Alternativa <strong>C</strong>.</p><p>Queimar a matéria orgânica (D) libera CO<sub>2</sub>.</p>",
  tags=["sequestro de carbono", "efeito estufa"], trocas=[("CO2, CH4 e N2O", "CO<sub>2</sub>, CH<sub>4</sub> e N<sub>2</sub>O"), ("Cadernos Temáticos de Química Nova na Escola", "<em>Cadernos Temáticos de Química Nova na Escola</em>")],
  alts={k: v.replace("CO2", "CO<sub>2</sub>") for k, v in D[67]["alternativas"].items()})
X(68, "Química", "Química orgânica", "<p>A degradação gera sarcosina (CH<sub>3</sub>–NH–CH<sub>2</sub>–COOH) e AMPA (H<sub>2</sub>N–CH<sub>2</sub>–PO<sub>3</sub>H<sub>2</sub>). O glifosato junta os dois pelo nitrogênio: HOOC–CH<sub>2</sub>–NH–CH<sub>2</sub>–PO<sub>3</sub>H<sub>2</sub>. Ele tem os grupos carboxila, amino e fosfonato (com o fósforo ligado direto ao carbono) e a fórmula C<sub>3</sub>H<sub>8</sub>NO<sub>5</sub>P. É a <strong>estrutura B</strong>. Alternativa <strong>B</strong>.</p><p>Em A, D e E o fósforo está ligado a um oxigênio (fosfato), e não ao carbono.</p>",
  figs(("q68", "Esquema: a molécula de glifosato se degrada em sarcosina (H3C–NH–CH2–COOH) e AMPA (H2N–CH2–P(=O)(OH)2)."),
       ("q68a", "Alternativa A: H2N–CH(CH3)–C(=O)–O–P(=O)(OH)2."),
       ("q68b", "Alternativa B: HO–C(=O)–CH2–NH–CH2–P(=O)(OH)2."),
       ("q68c", "Alternativa C: HO–C(=O)–CH2–CH(NH2)–CH2–P(=O)(OH)2."),
       ("q68d", "Alternativa D: H2N–CH2–C(=O)–O–P(=O)(OH)2."),
       ("q68e", "Alternativa E: H2N–C(=O)–CH2–CH2–O–P(=O)(OH)2.")),
  ["funções orgânicas", "herbicidas"],
  enun=p(SUB(T(68, 0)).replace("(C3H8NO5P)", "(C<sub>3</sub>H<sub>8</sub>NO<sub>5</sub>P)")) + "[[fig:1]]" + fonte(T(68, 4).replace("Química Nova", "<em>Química Nova</em>")) + p(T(68, 5)), alts=ALT(2))
X(69, "Química", "Química ambiental", "<p>A reação produz ácido sulfúrico, que deixa a água ácida. Para corrigir, adiciona-se uma substância básica que neutralize o ácido sem poluir: o <strong>carbonato de cálcio</strong> (calcário), que reage com o ácido formando sal, água e CO<sub>2</sub>. Alternativa <strong>E</strong>.</p><p>Cloreto de amônio, dióxido de enxofre e dióxido de carbono (B, C e D) são ácidos ou formam ácidos.</p>",
  tags=["drenagem ácida", "neutralização"],
  enun=p("A formação frequente de grandes volumes de pirita (FeS<sub>2</sub>)" + T(69, 1).replace("(FeS2)", "", 1)) + ap("4 FeS<sub>2</sub> (s) + 15 O<sub>2</sub> (g) + 2 H<sub>2</sub>O (l) → 2 Fe<sub>2</sub>(SO<sub>4</sub>)<sub>3</sub> (aq) + 2 H<sub>2</sub>SO<sub>4</sub> (aq)")
  + fonte("FIGUEIREDO, B. R. <em>Minérios e ambiente</em>. Campinas: Unicamp, 2000.") + p(T(69, 4)))
X(70, "Biologia", "Genética", "<p>Cada banda do bebê tem de vir do pai ou da mãe. Comparando as faixas, só no casal 3 todas as bandas pretas do bebê aparecem no pai ou na mãe. É o <strong>casal 3</strong>. Alternativa <strong>C</strong>.</p><p>Nos outros casais, o bebê tem bandas que não aparecem em nenhum dos dois.</p>",
  figs(("q70", "Esquema de bandas de DNA: uma coluna para o bebê e, ao lado, cinco casais numerados de 1 a 5, cada um com uma coluna para o pai e outra para a mãe. As bandas aparecem como retângulos pretos (presentes) ou brancos (ausentes) em 16 linhas.")),
  ["teste de paternidade", "DNA"], enun=p(T(70, 0)) + "[[fig:1]]" + p(T(70, 7)))
X(71, "Química", "Soluções", "<p>O plasma é 60% de 5,0 L, ou 3,0 L. Para não passar de 4,0 mg/L, a massa máxima de varfarina é 4,0 × 3,0 = 12 mg. Com a solução a 3,0 mg/mL, isso corresponde a 12 ÷ 3,0 = <strong>4,0 mL</strong>. Alternativa <strong>D</strong>.</p><p>Usar o volume total de sangue (5,0 L) daria 6,7 mL (E), mas o fármaco fica só no plasma.</p>",
  tags=["concentração", "diluição"])
X(72, "Física", "Eletrodinâmica", "<p>O voltímetro mede tensão e deve ficar em paralelo com a geladeira. O amperímetro da corrente total fica no fio comum, antes de todas as derivações; o da lâmpada fica em série com ela, no mesmo ramo. O único esquema com as três ligações certas é o <strong>E</strong>: voltímetro em paralelo com G, um amperímetro no neutro e outro em série com L. Alternativa <strong>E</strong>.</p><p>Nos esquemas B, C e D, o voltímetro aparece em série com algum aparelho ou os amperímetros ficam em paralelo.</p>",
  figs(("q72", "Diagrama: fios Fase e Neutro e, entre eles, três ramos em paralelo com G (geladeira), T (tomada) e L (lâmpada). Ao lado, os símbolos de voltímetro (V) e amperímetro (A)."),
       ("q72a", "Alternativa A: um amperímetro no fio de fase, antes de tudo; um voltímetro em série com a geladeira; outro amperímetro em série com a lâmpada."),
       ("q72b", "Alternativa B: um amperímetro em série no ramo da geladeira; um voltímetro em série com a geladeira; um amperímetro em paralelo com a lâmpada."),
       ("q72c", "Alternativa C: amperímetro em série com a geladeira, voltímetro em paralelo com ela e outro amperímetro em paralelo com a lâmpada."),
       ("q72d", "Alternativa D: amperímetro em série com a geladeira e voltímetro em paralelo com ela; outro amperímetro em série com a lâmpada."),
       ("q72e", "Alternativa E: voltímetro ligado entre fase e neutro, em paralelo com a geladeira; um amperímetro no fio neutro, antes das derivações; outro amperímetro em série com a lâmpada.")),
  ["voltímetro e amperímetro", "circuitos"], enun=p(T(72, 0)) + "[[fig:1]]" + p(T(72, 5)), alts=ALT(2))
X(73, "Biologia", "Citologia", "<p>Os polímeros são secretados para fora da célula. A organela que empacota e secreta substâncias é o complexo golgiense. A linhagem I tem a maior proporção dele, 50%. A melhor é a <strong>linhagem I</strong>. Alternativa <strong>A</strong>.</p><p>A linhagem IV tem mais retículo endoplasmático (40%), mas pouco golgiense (20%).</p>",
  figs(("q73", "Gráfico de barras empilhadas “Perfil celular das linhagens de microalgas”, com a proporção das organelas em cada linhagem (núcleo, retículo endoplasmático, complexo golgiense e mitocôndrias, em %): I, 20, 20, 50 e 10; II, 20, 35, 40 e 5; III, 20, 15, 35 e 30; IV, 20, 40, 20 e 20; V, 20, 35, 15 e 30.")),
  ["complexo golgiense", "secreção celular"], enun=p(T(73, 0)) + "[[fig:1]]" + p(T(73, 6)))
X(74, "Química", "Eletroquímica", "<p>O texto descreve a eletrólise: a corrente elétrica decompõe a água em seus elementos. Na indústria, o alumínio é obtido por eletrólise da alumina (Al<sub>2</sub>O<sub>3</sub>) extraída da bauxita. É a <strong>obtenção de alumínio a partir da bauxita</strong>. Alternativa <strong>C</strong>.</p><p>O ferro (D) é obtido por redução com carvão no alto-forno, sem eletrólise.</p>",
  tags=["eletrólise", "alumínio"], trocas=[("Tio Tungstênio: memórias de uma infância química", "<em>Tio Tungstênio: memórias de uma infância química</em>")])
X(75, "Física", "Eletrodinâmica", "<p>A potência é \\(P = \\dfrac{U^2}{R}\\). Se a tensão dobra (de 110 V para 220 V), U² fica 4 vezes maior; para manter a potência, R também deve ficar 4 vezes maior. Como \\(R = \\rho\\dfrac{L}{A}\\), basta usar a <strong>quarta parte da área da seção reta do fio</strong>. Alternativa <strong>E</strong>.</p><p>Dobrar o comprimento (A) só dobraria a resistência.</p>",
  tags=["leis de Ohm", "potência elétrica"])
X(76, "Física", "Leis de Newton", "<p>Ao andar, o pé empurra o chão para trás, e o chão empurra o pé para a frente (ação e reação). O atrito no pé é <strong>paralelo ao plano e no mesmo sentido do movimento</strong>, rampa acima. Alternativa <strong>C</strong>.</p><p>A força perpendicular ao plano (A) é a normal, e não o atrito.</p>",
  tags=["força de atrito", "ação e reação"])
X(77, "Química", "Estequiometria", "<p>O ferro-gusa tem 3,3% de carbono e o aço doce, 0,3%: sai 3% da massa como carbono. Em 2 500 kg, isso é 75 kg de C. Cada 12 g de C formam 44 g de CO<sub>2</sub>: 75 × 44 ÷ 12 = <strong>275 kg</strong>. Alternativa <strong>D</strong>.</p><p>A opção B (75) é a massa de carbono, e não a de CO<sub>2</sub>.</p>",
  tags=["estequiometria", "siderurgia"], trocas=[("Química Inorgânica não tão concisa", "<em>Química Inorgânica não tão concisa</em>")])
X(78, "Biologia", "Saúde", "<p>A síndrome da rubéola congênita atinge o feto quando a gestante se infecta. Se os homens estiverem vacinados, deixam de pegar e de <strong>transmitir o vírus a mulheres gestantes</strong>. Alternativa <strong>B</strong>.</p><p>O homem não passa a infecção direto para o feto (C), e imunidade não se transfere entre parceiros (D).</p>",
  tags=["rubéola", "vacinação"], trocas=[("Brasil livre da rubéola", "<em>Brasil livre da rubéola</em>")])
X(79, "Física", "Eletrodinâmica", "<p>Os elétrons se deslocam devagar no fio, a poucos milímetros por segundo. A lâmpada acende quase na hora porque, ao fechar a chave, o campo elétrico se espalha pelo circuito perto da velocidade da luz, e todos os elétrons livres começam a se mover ao mesmo tempo. A rapidez é a com que <strong>o campo elétrico se estabelece em todos os pontos do circuito</strong>. Alternativa <strong>D</strong>.</p>",
  tags=["corrente elétrica", "campo elétrico"])
X(80, "Biologia", "Ecologia", "<p>A produção primária é feita pelos seres que fazem fotossíntese. Entre os citados, os produtores são as <strong>algas</strong>. Alternativa <strong>B</strong>.</p><p>Aves, peixes, insetos e caranguejos (A, C, D e E) são consumidores.</p>",
  tags=["produtores", "manguezal"])
X(81, "Química", "Separação de misturas", "<p>No tratamento de água, as partículas com impurezas podem ser removidas por flotação: bolhas de ar se prendem aos flocos e os levam para a superfície, de onde são retirados. A resposta é a <strong>flotação</strong>. Alternativa <strong>A</strong>.</p><p>Levigação e peneiração (B e D) separam sólidos, e ventilação (C) separa sólidos com o ar.</p>",
  tags=["flotação", "tratamento de água"])
X(82, "Física", "Acústica", "<p>No mesmo intervalo T, o Dó maior completa o dobro de ciclos que o Dó central: sua frequência é o dobro. A razão entre a frequência do Dó central e a do Dó maior é \\(\\dfrac{1}{2}\\). Alternativa <strong>A</strong>.</p><p>A opção B (2) é a razão invertida, do Dó maior para o Dó central.</p>",
  figs(("q82", "Duas formas de onda no mesmo intervalo de tempo T: à esquerda, a do Dó central; à direita, a do Dó maior, que repete o padrão duas vezes mais.")),
  ["frequência", "oitava"], enun=p(T(82, 0)) + "[[fig:1]]" + p(T(82, 3)),
  alts=FR("\\dfrac{1}{2}", "2", "1", "\\dfrac{1}{4}", "4"))
X(83, "Física", "Eletrodinâmica", "<p>Os dois lados da ponte são divisores de tensão ligados a 10 V. No lado esquerdo (470 Ω em cima e R<sub>S</sub> = 100 Ω embaixo), o ponto do meio fica em 10 × 100/570 ≈ 1,75 V. No lado direito (470 Ω e 120 Ω), fica em 10 × 120/590 ≈ 2,03 V. O voltímetro lê o terminal + menos o −: 1,75 − 2,03 ≈ <strong>−0,3 V</strong>. Alternativa <strong>D</strong>.</p><p>A opção C (+0,3 V) inverte a polaridade do voltímetro.</p>",
  figs(("q83", "Ponte de resistores alimentada por uma fonte de 10 V: lado esquerdo com 470 Ω em cima e Rs = 100 Ω embaixo; lado direito com 470 Ω em cima e 120 Ω embaixo. Um voltímetro liga os pontos do meio, com o terminal + à esquerda e o − à direita; a parte de baixo está aterrada.")),
  ["ponte de Wheatstone", "divisor de tensão"], enun=p(T(83, 0).replace("(Rs)", "(<em>R</em><sub>S</sub>)")) + "[[fig:1]]" + p("Para um valor de temperatura em que <em>R</em><sub>S</sub> = 100 Ω, a leitura apresentada pelo voltímetro será de"))
X(84, "Biologia", "Ecologia", "<p>No ambiente novo, a espécie invasora chega sem os parasitas e predadores que controlavam sua população no lugar de origem. Por isso cresce muito, por <strong>não possuírem parasitas e predadores naturais presentes no ambiente exótico</strong>. Alternativa <strong>B</strong>.</p><p>Nenhuma espécie se adapta a qualquer clima (C).</p>",
  tags=["espécies invasoras", "controle populacional"], alts={**D[84]["alternativas"], "A": D[84]["alternativas"]["A"].replace("pool", "<em>pool</em>")})
X(85, "Física", "Eletromagnetismo", "<p>A barra se desloca até a catraca com velocidade média de 5 m/s em 6 ms: x = 5 × 0,006 = 0,03 m = 3 cm. Na nova posição de equilíbrio, a força magnética equilibra a mola: B·i·L = k·x. Com k = 5 × 10<sup>−2</sup> N/cm, k·x = 0,15 N, e B = 0,15 ÷ (6 × 0,05) = 0,5 T = <strong>5 × 10<sup>−1</sup> T</strong>. Alternativa <strong>A</strong>.</p>",
  figs(("q85", "Esquema: uma barra condutora vertical de comprimento L, com corrente i para cima, presa pelo meio a uma mola de constante k por um isolante; a mola está fixa numa parede à direita. A região tem campo magnético entrando no plano (símbolos ×). À esquerda, uma catraca e um fio; a barra se move com velocidade v para a esquerda. Embaixo, um eixo x (cm) com a origem 0 e o ponto C, onde fica a catraca.")),
  ["força magnética", "lei de Hooke"],
  enun=p("Desenvolve-se um dispositivo para abrir automaticamente uma porta no qual um botão, quando acionado, faz com que uma corrente elétrica <em>i</em> = 6 A percorra uma barra condutora de comprimento <em>L</em> = 5 cm, cujo ponto médio está preso a uma mola de constante elástica <em>k</em> = 5 × 10<sup>−2</sup> N/cm. O sistema mola-condutor está imerso em um campo magnético uniforme perpendicular ao plano. Quando acionado o botão, a barra sairá da posição de equilíbrio a uma velocidade média de 5 m/s e atingirá a catraca em 6 milisegundos, abrindo a porta.")
  + "[[fig:1]]" + p(T(85, 6).replace("dispostivo", "dispositivo")),
  alts={"A": "5 × 10<sup>−1</sup> T.", "B": "5 × 10<sup>−2</sup> T.", "C": "5 × 10<sup>1</sup> T.", "D": "2 × 10<sup>−2</sup> T.", "E": "2 × 10<sup>0</sup> T."})
X(86, "Química", "Forças intermoleculares", "<p>O poliacrilato de sódio tem cargas (COO<sup>−</sup> e Na<sup>+</sup>), que atraem fortemente as moléculas polares de água: são interações íon-dipolo. A celulose, sem cargas, interage com a água por ligações de hidrogênio, mais fracas. A eficiência vem das <strong>interações íon-dipolo mais fortes entre o poliacrilato e as moléculas de água, em relação às ligações de hidrogênio entre a celulose e as moléculas de água</strong>. Alternativa <strong>E</strong>.</p><p>A água não é íon, então não há interação íon-íon (B).</p>",
  figs(("q86", "Fórmulas estruturais: (1) poliacrilato de sódio, uma cadeia de carbonos com o grupo COO−Na+, repetida n vezes; (2) celulose, anéis de glicose com grupos OH ligados por oxigênio, repetidos n vezes.")),
  ["íon-dipolo", "polímeros"], enun=p(T(86, 0)) + "[[fig:1]]" + fonte("CURI, D. <em>Química Nova na Escola</em>, São Paulo, n. 23, maio 2006 (adaptado).") + p(T(86, 6)))
X(87, "Física", "Leis de Newton", "<p>No começo, a força resultante é o peso, que vai diminuindo à medida que a resistência do ar cresce, até zerar na velocidade limite. Ao abrir o paraquedas (T<sub>A</sub>), a resistência do ar fica muito maior que o peso: a resultante passa a ser grande e para cima (negativa) e diminui até zerar de novo, quando a velocidade fica constante. Esse comportamento está no <strong>gráfico B</strong>. Alternativa <strong>B</strong>.</p><p>O gráfico A não volta a zero depois de T<sub>A</sub>, e D ignora o efeito da abertura.</p>",
  figs(("q87a", "Alternativa A: a força começa positiva, diminui até zero em TA e depois cai para valores negativos cada vez maiores."),
       ("q87b", "Alternativa B: a força começa positiva e diminui até zero; em TA salta para um valor negativo grande e volta a se aproximar de zero."),
       ("q87c", "Alternativa C: a força cresce de zero até um máximo em TA e depois diminui até zero."),
       ("q87d", "Alternativa D: a força começa positiva, diminui até zero antes de TA e fica em zero."),
       ("q87e", "Alternativa E: a força cresce a partir de zero e se estabiliza num valor positivo.")),
  ["força resultante", "velocidade limite"], enun=p(T(87, 0).replace("(instante TA)", "(instante T<sub>A</sub>)"), T(87, 1)), alts=ALT(1))
X(88, "Biologia", "Genética", "<p>O DNA mitocondrial é herdado só da mãe. O rapaz recebeu o DNA mitocondrial da mãe, que o recebeu da mãe dela, a avó materna. Pai, avô materno e filhos não o compartilham com ele (os filhos o herdam da mãe deles). A comparação deve ser com a <strong>avó materna</strong>. Alternativa <strong>D</strong>.</p>",
  tags=["DNA mitocondrial", "herança materna"], enun=p(T(88, 0) + " " + T(88, 1), T(88, 2)))
X(89, "Física", "Calorimetria", "<p>O calor que a água quente perde é o que a fria ganha: m<sub>q</sub> · (70 − 30) = m<sub>f</sub> · (30 − 25). Então 40 m<sub>q</sub> = 5 m<sub>f</sub>, e \\(\\dfrac{m_q}{m_f} = \\dfrac{5}{40} = \\) <strong>0,125</strong>. Alternativa <strong>B</strong>.</p><p>A opção E (0,833) usa as temperaturas sem as diferenças.</p>",
  tags=["trocas de calor", "equilíbrio térmico"], enun=p(T(89, 0) + " " + T(89, 1), T(89, 2)))
X(90, "Química", "Química orgânica", "<p>Carbono quaternário é o que está ligado a quatro outros carbonos. Na figura, isso acontece nos grupos terc-butila, nas pontas das duas “mãos”: cada um está ligado a três metilas e ao carbono da tripla ligação. A resposta é <strong>mãos</strong>. Alternativa <strong>A</strong>.</p><p>Na cabeça há um carbono ligado a dois oxigênios, e nos pés as cadeias são lineares.</p>",
  figs(("q90", "Fórmula estrutural do NanoKid: na cabeça, um anel de cinco átomos com dois oxigênios; o tórax é um anel benzênico, com dois “braços” de tripla ligação terminados em grupos com um carbono ligado a três metilas (as mãos); uma tripla ligação liga ao abdômen, outro anel benzênico, de onde saem duas “pernas” com tripla ligação e cadeias de três carbonos (os pés).")),
  ["classificação do carbono", "fórmulas estruturais"],
  enun=p(T(90, 0).replace("de nanoputians", "de <em>nanoputians</em>")) + "[[fig:1]]" + fonte("CHANTEAU, S. H.; TOUR, J. M. <em>The Journal of Organic Chemistry</em>, v. 68, n. 23, 2003 (adaptado).") + p(T(90, 4)))

completar(Q, R)
