# Enem 2016, 1º dia, caderno azul: Ciências da Natureza (questões 46 a 90; no site, 1 a 45). Em 2016 a Natureza era no 1º dia.
# Texto legível. Quadros das Q61, 66, 77 e 78 e equações das Q50, 58 e 64 em HTML. Alternativas-imagem: Q49, 63 e 85.
# Sem anuladas nesta área.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, paragrafos_enem

ID = "enem-2016-natureza"
META = {"id": ID, "banca": "Enem", "ano": 2016, "titulo": "Enem 2016: Ciências da Natureza", "fonte": "Inep", "dataExame": "2016-11-05",
        "duracaoMinutos": 150, "area": "Ciências da Natureza", "caderno": "azul", "dia": 1}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2016-dia1-azul")
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

X(46, "Química", "Polaridade e solubilidade", "<p>A capsaicina vem de uma oleorresina e está dissolvida em álcool: é uma molécula de baixa polaridade, pouco solúvel em água. Por isso a água não consegue retirá-la da pele ou dos olhos: a <strong>solubilidade do princípio ativo em água é muito baixa, dificultando a sua remoção</strong>. Alternativa <strong>B</strong>.</p><p>Etanol e água se misturam sem reação química que libere calor relevante (A).</p>",
  tags=["solubilidade", "capsaicina"], trocas=[("o spray de pimenta contém", "o <em>spray</em> de pimenta contém"), ("de Capsicum,", "de <em>Capsicum</em>,"), ("com o spray de pimenta", "com o <em>spray</em> de pimenta")])
X(47, "Física", "Energia", "<p>Potência teórica de cada unidade: P = ρ · Q · g · h = 1 000 × 690 × 10 × 118,4 = 816 960 000 W = 816,96 MW.</p><p>Potência instalada por unidade: 14 000 MW ÷ 20 = 700 MW. Não aproveitada: 816,96 − 700 = <strong>116,96 MW</strong>. Alternativa <strong>C</strong>.</p><p>816,96 MW (D) é a potência teórica, sem descontar a instalada.</p>",
  tags=["potência hidráulica", "hidrelétrica"], trocas=[("690 m3/s", "690 m<sup>3</sup>/s"), ("(10 m/s2)", "(10 m/s<sup>2</sup>)"), ("kg/m3)", "kg/m<sup>3</sup>)")])
X(48, "Biologia", "Questões ambientais", "<p>No lixo comum, as fezes se decompõem sem oxigênio e liberam metano para a atmosfera, um gás de efeito estufa (Figura 1). No projeto, o biodigestor coleta esse metano (biogás) e ele é queimado nos postes de iluminação do parque (Figura 2). A inovação é possibilitar a <strong>queima de gás metano</strong>, aproveitando sua energia. Alternativa <strong>A</strong>.</p><p>O biodigestor faz decomposição anaeróbica, não aeróbica (C).</p>",
  figs(("q48a", "Figura 1: uma pessoa recolhe as fezes de um cachorro num saco plástico e joga numa lixeira comum; o lixo vai para um monte que solta gases."),
       ("q48b", "Figura 2: a pessoa joga o saco com as fezes num biodigestor enterrado, ligado a um poste de luz do parque.")),
  ["biogás", "metano"], enun=p(T(48, 0)) + p("<strong>Figura 1</strong>") + "[[fig:1]]" + p(T(48, 3).replace("Projeto Park Spark", "Projeto <em>Park Spark</em>")) + p("<strong>Figura 2</strong>") + "[[fig:2]]" + fonte("Disponível em: http://parksparkproject.com. Acesso em: 30 ago. 2013 (adaptado).") + p(T(48, 7)))
X(49, "Física", "Ondulatória", "<p>Pelo efeito Doppler, enquanto a ambulância se aproxima, o observador percebe frequência maior que f<sub>A</sub>, constante (a velocidade é constante). Quando ela passa e se afasta, a frequência percebida cai para um valor menor que f<sub>A</sub>, também constante. Perto da passagem, a transição é rápida. É o gráfico que começa acima de f<sub>A</sub> e termina abaixo. Alternativa <strong>D</strong>.</p><p>No gráfico C, a ordem está invertida; em E, não haveria efeito Doppler.</p>",
  figs(("q49", "Frentes de onda circulares emitidas pela ambulância A, que se move para a direita: os círculos ficam mais juntos à direita, no sentido do observador O."),
       ("q49a", "Gráfico A: f_O(t) oscila em torno de f_A, como uma senoide."),
       ("q49b", "Gráfico B: f_O(t) igual a f_A, com um pico no meio e volta a f_A."),
       ("q49c", "Gráfico C: f_O(t) começa abaixo de f_A e sobe, terminando acima de f_A."),
       ("q49d", "Gráfico D: f_O(t) começa acima de f_A, constante, e cai, terminando abaixo de f_A."),
       ("q49e", "Gráfico E: f_O(t) constante, acima de f_A, o tempo todo.")),
  ["efeito Doppler"],
  enun=p(T(49, 0).replace("ambulância A ", "ambulância <strong>A</strong> ").replace("observador O,", "observador <strong>O</strong>,").replace("constante fA.", "constante <em>f</em><sub>A</sub>.").replace("tempo fO(t)", "tempo <em>f</em><sub>O</sub>(<em>t</em>)")) + "[[fig:1]]" + p("Qual esboço gráfico representa a frequência <em>f</em><sub>O</sub>(<em>t</em>) detectada pelo observador?"), alts=ALT(2))
X(50, "Química", "Termoquímica", "<p>Pela lei de Hess, a trimerização é 3 vezes a combustão do acetileno menos a combustão do benzeno (invertida):</p><p>ΔH = 3 × (−310) − (−780) = −930 + 780 = <strong>−150 kcal</strong>. Alternativa <strong>B</strong>.</p><p>−1 090 (A) soma as duas entalpias, sem inverter a do benzeno.</p>",
  tags=["lei de Hess", "entalpia de combustão"],
  enun=p(T(50, 0)) + EQ("3 C<sub>2</sub>H<sub>2</sub> (g) → C<sub>6</sub>H<sub>6</sub> (l)") + p(T(50, 2))
       + EQ("I. C<sub>2</sub>H<sub>2</sub> (g) + 5/2 O<sub>2</sub> (g) → 2 CO<sub>2</sub> (g) + H<sub>2</sub>O (l) &nbsp; Δ<em>H</em><sub>c</sub>° = −310 kcal/mol", "II. C<sub>6</sub>H<sub>6</sub> (l) + 15/2 O<sub>2</sub> (g) → 6 CO<sub>2</sub> (g) + 3 H<sub>2</sub>O (l) &nbsp; Δ<em>H</em><sub>c</sub>° = −780 kcal/mol") + p(T(50, 4)),
  alts={"A": "−1 090.", "B": "−150.", "C": "−50.", "D": "+157.", "E": "+470."})
X(51, "Química", "Reações inorgânicas", "<p>O HCl dissolve o carbonato de bário, liberando íons Ba<sup>2+</sup>. Depois da filtração, o H<sub>2</sub>SO<sub>4</sub> reage com esses íons formando sulfato de bário, insolúvel: Ba<sup>2+</sup> + SO<sub>4</sub><sup>2−</sup> → BaSO<sub>4</sub>. A presença de bário solúvel é indicada pela <strong>precipitação de um sólido branco</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["precipitação", "sulfato de bário"], trocas=[("Química Nova, n.", "<strong>Química Nova</strong>, n."), ("solução aquosa de H2SO4", "solução aquosa de H<sub>2</sub>SO<sub>4</sub>")])
X(52, "Química", "Isomeria", "<p>O bombicol tem duas ligações duplas entre carbonos com ligantes diferentes: apresenta isomeria geométrica (cis-trans). Entre os feromônios do quadro, o usado contra <em>Scrobipalpuloides absoluta</em> também tem ligações duplas na cadeia, cada carbono com ligantes diferentes. Alternativa <strong>E</strong>.</p><p>Os de <em>Sitophilus</em> e <em>Migdolus</em> (A e B) têm carbonos quirais (isomeria óptica), e o de <em>Anthonomus</em> (C) tem uma dupla sem isomeria geométrica.</p>",
  figs(("q52a", "Estrutura do bombicol: uma cadeia longa de carbonos com duas ligações duplas no meio e um grupo OH na ponta."),
       ("q52b", "Quadro com cinco feromônios. Sitophilus spp (milho): cadeia curta com OH e C=O e ramificações metila. Migdolus fryanus (cana-de-açúcar): amida com ramificações metila. Anthonomus rubi (morango): cadeia com uma dupla ligação ligada a dois metis e um grupo CH₂OH. Grapholita molesta (frutas): cadeia longa com OH na ponta. Scrobipalpuloides absoluta (tomate): cadeia longa com duas duplas ligações no meio e um grupo OCOCH₃ na ponta.")),
  ["isomeria geométrica", "feromônios"],
  enun=p(T(52, 0)) + "[[fig:1]]" + p(T(52, 2)) + "[[fig:2]]" + fonte(T(52, 4).replace("Química Nova na Escola", "<strong>Química Nova na Escola</strong>")) + p(T(52, 5)),
  alts={k: f"<em>{v[:-1]}</em>." for k, v in D[52]["alternativas"].items()})
X(53, "Biologia", "Bioquímica", "<p>O milho guarda energia como amido, um polissacarídeo que a levedura não consegue fermentar. A hidrólise quebra o amido em glicose, que a levedura transforma em etanol e CO<sub>2</sub>. A etapa é fundamental para que <strong>o amido seja transformado em substratos utilizáveis pela levedura</strong>. Alternativa <strong>D</strong>.</p>",
  figs(("q53", "Esquema: o milho entra num tanque de hidrólise; o produto segue para um tanque de fermentação que recebe levedura e de onde saem CO₂, etanol e água.")),
  ["fermentação", "hidrólise do amido"], enun=p(T(53, 0)) + "[[fig:1]]" + p(T(53, 5)))
X(54, "Física", "Calorimetria", "<p>A usina gera 1,0 MW elétrico e dissipa o dobro, 2,0 MW = 2 000 kJ/s, como calor para a água. Com aquecimento máximo de 3 °C:</p><p>fluxo = P ÷ (c · ΔT) = 2 000 ÷ (4 × 3) ≈ <strong>167 kg/s</strong>. Alternativa <strong>C</strong>.</p><p>Usar 1 MW em vez de 2 MW dá 84 kg/s (B).</p>",
  tags=["calor específico", "potência térmica"])
X(55, "Física", "Ondulatória", "<p>No gráfico, as curvas para distâncias maiores ficam bem mais baixas nas frequências de 20 Hz a cerca de 250 Hz (até 20 dB a menos), e quase se juntam acima de 1 000 Hz. Pela Figura 2, essa faixa baixa é a dos graves. A intensidade <strong>diminui na faixa das frequências graves</strong>. Alternativa <strong>C</strong>.</p>",
  figs(("q55a", "Figura 1, “Resposta de Frequência”: intensidade (dB) em função da frequência (de 20 a 20 000 Hz) para 3 mm, 25 mm, 51 mm e 60 mm. Nas baixas frequências, a curva de 3 mm está perto de +10 dB e a de 60 mm perto de −10 dB; acima de cerca de 1 000 Hz, as quatro curvas se juntam."),
       ("q55b", "Figura 2, “Faixas do espectro de frequência sonora”: subgrave (20 a 63 Hz), grave (63 a 250 Hz), média baixa (250 a 640 Hz), média (640 Hz a 2,5 kHz), média alta (2,5 a 5 kHz) e aguda (5 a 20 kHz).")),
  ["intensidade sonora", "frequência"], enun=p(T(55, 0)) + "[[fig:1]][[fig:2]]" + p(T(55, 9)))
X(56, "Biologia", "Citologia", "<p>O ciclo de Krebs acontece na matriz da mitocôndria. Para que a proteína bloqueadora funcione, ela precisa ser endereçada a essa organela: o pesquisador deve usar o peptídeo sinal da <strong>mitocôndria</strong>. Alternativa <strong>B</strong>.</p>",
  tags=["ciclo de Krebs", "endereçamento de proteínas"], trocas=[("Krebs in vitro", "Krebs <em>in vitro</em>")])
X(57, "Física", "Ondulatória", "<p>A mariposa se afasta: está cada vez mais longe, então o eco volta mais fraco (intensidade diminuída) e demora mais (tempo de retorno aumentado). Como a fonte refletora se afasta, o efeito Doppler reduz a frequência percebida. Alternativa <strong>A</strong>.</p>",
  tags=["eco", "efeito Doppler"])
X(58, "Química", "Estequiometria", "<p>Mols: CH<sub>3</sub>Br (95 g/mol): 142,5 ÷ 95 = 1,5 mol; NaOH (40 g/mol): 80 ÷ 40 = 2 mol. A proporção é 1 : 1, então o limitante é o CH<sub>3</sub>Br. Metanol (32 g/mol): 32 ÷ 32 = 1 mol.</p><p>R = 1 ÷ 1,5 × 100 ≈ <strong>67%</strong>. Alternativa <strong>D</strong>.</p><p>Dividir pelo NaOH, que está em excesso, dá 50% (C).</p>",
  tags=["rendimento", "reagente limitante"],
  enun=p("A minimização do tempo e custo de uma reação química, bem como o aumento na sua taxa de conversão, caracterizam a eficiência de um processo químico. Como consequência, produtos podem chegar ao consumidor mais baratos. Um dos parâmetros que mede a eficiência de uma reação química é o seu rendimento molar (<em>R</em>, em %), definido como")
       + "<p>\\[R = \\frac{n_{\\text{produto}}}{n_{\\text{reagente limitante}}} \\times 100\\]</p>" + p("em que <em>n</em> corresponde ao número de mols. O metanol pode ser obtido pela reação entre brometo de metila e hidróxido de sódio, conforme a equação química:")
       + EQ("CH<sub>3</sub>Br + NaOH → CH<sub>3</sub>OH + NaBr") + p(T(58, 3), T(58, 4)))
X(59, "Física", "Eletrodinâmica", "<p>No desenho, entre A e B há o traço de 5 kΩ (arco) em paralelo com o de 20 kΩ: 4 kΩ. De A e de B saem os dois lados de 10 kΩ até C.</p><p>R<sub>AB</sub>: 4 kΩ em paralelo com o caminho A–C–B (10 + 10 = 20 kΩ): 4 · 20 ÷ 24 = 10/3 kΩ.</p><p>R<sub>BC</sub>: 10 kΩ em paralelo com o caminho B–A–C (4 + 10 = 14 kΩ): 10 · 14 ÷ 24 = 35/6 kΩ.</p><p>Razão: (10/3) ÷ (35/6) = 20/35 = <strong>4/7</strong>. Alternativa <strong>B</strong>.</p>",
  figs(("q59a", "Três traçados de lápis: um zigue-zague (2H), uma linha reta (HB) e um arco grosso (6B)."),
       ("q59b", "Desenho de um sorvete de casquinha: entre os pontos A e B, um arco de 5 kΩ por cima e um zigue-zague de 20 kΩ por baixo; de A e de B descem dois traços de 10 kΩ que se encontram no ponto C, a ponta da casquinha.")),
  ["associação de resistores", "lei de Ohm"],
  enun=p(T(59, 0)) + "[[fig:1]]" + p(T(59, 3)) + "[[fig:2]]" + p("Na sequência, conectou o ohmímetro nos terminais A e B do desenho e, em seguida, conectou-o nos terminais B e C, anotando as leituras <em>R</em><sub>AB</sub> e <em>R</em><sub>BC</sub>, respectivamente.", "Ao estabelecer a razão " + "\\(\\dfrac{R_{AB}}{R_{BC}}\\)" + ", qual resultado o estudante obteve?"),
  alts={"A": "1", **{k: v for k, v in FR("", "\\dfrac{4}{7}", "\\dfrac{10}{27}", "\\dfrac{14}{81}", "\\dfrac{4}{81}").items() if k != "A"}})
X(60, "Química", "Forças intermoleculares", "<p>O benzeno é apolar, e a superfície do carvão (carbono) também. Entre moléculas apolares, as únicas atrações são as forças de London: <strong>interações dipolo induzido – dipolo induzido</strong>. Alternativa <strong>D</strong>.</p><p>A adsorção física não forma ligações covalentes (B), e o benzeno não faz ligações de hidrogênio (C).</p>",
  tags=["adsorção", "forças de London"])
X(61, "Biologia", "Ecologia", "<p>Onde os peixes têm acesso (sem tela), a densidade dos mexilhões cai de 380 para 200 por m² e o tamanho médio sobe de 3 para 6 cm: os peixes comem os mexilhões pequenos e reduzem a população. Os peixes controlam a densidade dos <strong>mexilhões, predando especialmente animais pequenos</strong>. Alternativa <strong>C</strong>.</p><p>As cracas também diminuem, mas o tamanho médio cai (de 2 para 1,5 cm): os peixes comem as maiores (B). Algas e ascídias quase não mudam.</p>",
  tags=["predação", "espécies exóticas"],
  enun=p(T(61, 0)) + tabela(["Espécie exótica", "Com tela: densidade (indivíduos/m²)", "Com tela: tamanho médio (cm)", "Sem tela: densidade (indivíduos/m²)", "Sem tela: tamanho médio (cm)"],
                             [["Alga", "100", "15", "110", "18"], ["Craca", "300", "2", "150", "1,5"], ["Mexilhão", "380", "3", "200", "6"], ["Ascídia", "55", "4", "58", "3,8"]]) + p(T(61, 3)))
X(62, "Biologia", "Ecologia", "<p>O carbono passa da forma inorgânica (CO<sub>2</sub>) para a orgânica na fotossíntese, feita pelos produtores. Na cadeia citada, o produtor é o <strong>fitoplâncton</strong>. Alternativa <strong>A</strong>.</p><p>Os outros grupos são consumidores: recebem o carbono já na forma orgânica.</p>",
  tags=["ciclo do carbono", "produtores"])
X(63, "Física", "Cinemática", "<p>Na primeira etapa (tempo de reação), o carro segue com velocidade constante: trecho horizontal. Na segunda, a desaceleração é constante, e pela equação de Torricelli v² = v<sub>0</sub>² − 2ad: a velocidade cai com a distância numa curva, cada vez mais inclinada até zero. É o gráfico com um trecho horizontal seguido de uma curva descendente. Alternativa <strong>D</strong>.</p><p>O gráfico B usa uma reta na frenagem, o que valeria para velocidade em função do tempo, não da distância.</p>",
  figs(("q63a", "Gráfico A: velocidade diminuindo em linha reta desde o início até zero."),
       ("q63b", "Gráfico B: velocidade constante e depois diminuindo em linha reta até zero."),
       ("q63c", "Gráfico C: velocidade diminuindo numa curva desde o início até zero."),
       ("q63d", "Gráfico D: velocidade constante e depois diminuindo numa curva cada vez mais inclinada até zero."),
       ("q63e", "Gráfico E: velocidade subindo e depois descendo, em forma de arco.")),
  ["equação de Torricelli", "tempo de reação"], enun=p(T(63, 0), T(63, 1)), alts=ALT(1))
X(64, "Química", "Eletroquímica", "<p>Cada biocélula fornece a diferença entre os potenciais: 0,8 − (−0,3) = 1,1 V. Em série, as tensões se somam: 4,4 ÷ 1,1 = <strong>4 biocélulas</strong>. Alternativa <strong>B</strong>.</p><p>Somar os módulos dos potenciais de outro jeito, como 0,8 − 0,3 = 0,5 V, levaria a 9 células (D), o que está errado: a diferença de potencial é o maior menos o menor.</p>",
  tags=["pilhas em série", "potencial de redução"],
  enun=tit("TEXTO I") + ap(T(64, 1)) + fonte(T(64, 2)) + tit("TEXTO II") + ap(T(64, 4).replace("(E°’)", "(<em>E</em>°’)"))
       + EQ("2 CO<sub>2</sub> + 7 H<sup>+</sup> + 8 e<sup>−</sup> → CH<sub>3</sub>COO<sup>−</sup> + 2 H<sub>2</sub>O &nbsp; <em>E</em>°’ = −0,3 V", "O<sub>2</sub> + 4 H<sup>+</sup> + 4 e<sup>−</sup> → 2 H<sub>2</sub>O &nbsp; <em>E</em>°’ = 0,8 V") + fonte(T(64, 6)) + p(T(64, 7)))
X(65, "Biologia", "Zoologia", "<p>Animais que se alimentam de sangue precisam impedir a coagulação enquanto sugam: sua saliva tem substâncias anticoagulantes. São os <strong>mosquitos hematófagos</strong>. Alternativa <strong>E</strong>.</p>",
  tags=["anticoagulantes", "hematofagia"])
X(66, "Física", "Movimento circular", "<p>A engrenagem A (24 dentes) está no eixo do motor, a 18 RPM, e move a B (72 dentes): f<sub>B</sub> = 18 × 24 ÷ 72 = 6 RPM. A C gira junto com a B (mesmo eixo), a 6 RPM, e move a D (108 dentes), que leva o ponteiro: f<sub>D</sub> = 6 × 36 ÷ 108 = <strong>2 RPM</strong>. Alternativa <strong>B</strong>.</p>",
  figs(("q66", "Sistema de engrenagens: o eixo do motor gira a engrenagem A, que engrena na B; a C está no mesmo eixo da B e engrena na D, que leva o ponteiro.")),
  ["engrenagens", "frequência"],
  enun=p(T(66, 0)) + tabela(["Engrenagem", "Dentes"], [["A", "24"], ["B", "72"], ["C", "36"], ["D", "108"]]) + "[[fig:1]]" + p(T(66, 3)))
X(67, "Química", "Estados físicos", "<p>Nas mudanças de estado, as moléculas não mudam: só muda a forma como elas se arranjam e se movimentam (organizadas no sólido, mais livres no líquido, muito afastadas no gás). As transformações estão associadas a uma <strong>mudança na estrutura espacial formada pelos diferentes constituintes do material</strong>. Alternativa <strong>D</strong>.</p><p>Troca de átomos, transmutação ou mudança de isótopos (A, B, C e E) seriam transformações químicas ou nucleares.</p>",
  tags=["mudanças de estado", "modelo cinético"], trocas=[("Timeu-Crítias", "<em>Timeu-Crítias</em>")])
X(68, "Química", "Soluções", "<p>27 000 L de etanol geram 27 000 × 18 = 486 000 L de vinhaça. Com 60 mg/L de fósforo: 486 000 × 60 = 29 160 000 mg ≈ <strong>29 kg</strong>. Alternativa <strong>B</strong>.</p><p>Esquecer os 18 L de vinhaça por litro de etanol dá cerca de 1,6 kg.</p>",
  tags=["concentração", "vinhaça"], trocas=[("Revista Brasileira de Engenharia Agrícola e Ambiental", "<strong>Revista Brasileira de Engenharia Agrícola e Ambiental</strong>")])
X(69, "Biologia", "Fisiologia vegetal", "<p>O nitrato é a principal fonte de nitrogênio das plantas, usado para produzir aminoácidos. Com menos nitrato absorvido, o grão terá menos <strong>proteínas</strong>. Alternativa <strong>E</strong>.</p><p>Amido, frutose, lipídios e celulose (A a D) não contêm nitrogênio.</p>",
  tags=["nitrogênio", "CO2"], trocas=[("Nature Climate Change", "<strong>Nature Climate Change</strong>"), ("elevated CO2", "elevated CO<sub>2</sub>")])
X(70, "Química", "Radioatividade", "<p>Os seres vivos mantêm a mesma proporção de carbono-14 em relação ao carbono-12 que existe na atmosfera. Depois da morte, o C-14 decai e a proporção diminui. Medindo quanto ela caiu, calcula-se o tempo. Isso só funciona porque se conhece a <strong>proporção entre carbono-14 e carbono-12 na atmosfera ao longo dos anos</strong>. Alternativa <strong>A</strong>.</p><p>O C-12 é estável: não se decompõe nem é emitido (B e D).</p>",
  tags=["carbono-14", "datação"], trocas=[("(Mammuthus primigenius)", "(<em>Mammuthus primigenius</em>)")])
X(71, "Biologia", "Biomas", "<p>Substrato lamacento e pouco oxigenado, raízes respiratórias que crescem para cima, glândulas para eliminar sal: são adaptações das plantas do <strong>manguezal</strong>, que vivem no encontro do rio com o mar. Alternativa <strong>D</strong>.</p>",
  tags=["manguezal", "adaptações vegetais"])
X(72, "Química", "Separação de misturas", "<p>O vapor de água passa pelas folhas e carrega consigo as substâncias aromáticas voláteis, os óleos essenciais. É a <strong>extração por arraste</strong> a vapor. Alternativa <strong>C</strong>.</p><p>Não há destilação (B), porque nada é condensado e separado: o vapor perfumado vai direto para o ambiente.</p>",
  figs(("q72", "Esquema de uma sauna úmida: atrás da parede, um gerador de vapor; o vapor sai por um cano para dentro da sauna, onde há folhas colocadas na saída do vapor.")),
  ["arraste a vapor", "óleos essenciais"], enun=p(T(72, 0)) + "[[fig:1]]" + p(T(72, 4)))
X(73, "Biologia", "Ecologia", "<p>As árvores acrescentam folhas e galhos ao solo, aumentando a matéria orgânica, que alimenta fungos, bactérias e pequenos animais. Isso recupera o solo e ao mesmo tempo mantém a produção. A estratégia <strong>promove maior diversidade de vida no solo com o aumento da matéria orgânica</strong>. Alternativa <strong>C</strong>.</p><p>Os sistemas agroflorestais não substituem as culturas por árvores (A) nem usam biocidas (B).</p>",
  tags=["sistemas agroflorestais", "sucessão ecológica"])
X(74, "Física", "Eletrodinâmica", "<p>As três lâmpadas estão em paralelo, cada uma com corrente i. A e E estão no fio principal, ligado à bateria: I<sub>A</sub> = I<sub>E</sub> = 3i. C está no fio que vem só de L1, e D no fio que vem só de L2: I<sub>C</sub> = I<sub>D</sub> = i. B, no fio da esquerda acima da ligação de L3, leva a corrente de L1 e L2: 2i. Então I<sub>A</sub> = I<sub>E</sub> e I<sub>C</sub> = I<sub>D</sub>. Alternativa <strong>A</strong>.</p>",
  figs(("q74", "Circuito com três lâmpadas L1, L2 e L3, uma abaixo da outra, cada uma ligada entre o fio vertical da esquerda e o fio vertical da direita. No fio da esquerda estão os pontos B (entre as ligações de L2 e L3) e A (abaixo de L3, perto da bateria V). No ramo de saída de L1 está o ponto C, no de L2 o ponto D, e no fio da direita, perto da bateria, o ponto E.")),
  ["circuito em paralelo", "corrente elétrica"],
  enun=p(T(74, 0).replace("IA, IB, IC, ID e IE", "<em>I</em><sub>A</sub>, <em>I</em><sub>B</sub>, <em>I</em><sub>C</sub>, <em>I</em><sub>D</sub> e <em>I</em><sub>E</sub>")) + "[[fig:1]]" + p(T(74, 4)),
  alts={k: re.sub(r"I([A-E])", r"<em>I</em><sub>\1</sub>", v) for k, v in D[74]["alternativas"].items()})
X(75, "Biologia", "Fisiologia vegetal", "<p>A seiva bruta sobe pelo xilema puxada pela perda de água nas folhas: a transpiração cria uma tensão que, com a coesão entre as moléculas de água, arrasta a coluna líquida desde as raízes. Isso funciona em qualquer posição da copa. Quem garante o transporte é a <strong>transpiração</strong>. Alternativa <strong>E</strong>.</p><p>A gravidade (B) atrapalharia a subida, e a gutação (A) é só a perda de gotas pelas folhas.</p>",
  figs(("q75", "Ilustração de uma árvore com setas mostrando a água entrando pelas raízes, subindo pelo vaso do xilema e saindo como vapor pelos estômatos das folhas; detalhes ampliados das raízes com água do solo e de uma folha com estômato.")),
  ["teoria da coesão-tensão", "xilema"], enun=p(T(75, 0)) + "[[fig:1]]" + fonte(T(75, 2).replace("Revista de Ciência Elementar", "<strong>Revista de Ciência Elementar</strong>")) + p(T(75, 3), T(75, 4)))
X(76, "Química", "Reações orgânicas", "<p>O metóxido (CH<sub>3</sub>O<sup>−</sup>) substitui o bromo no brometo de metila: CH<sub>3</sub>Br + CH<sub>3</sub>O<sup>−</sup> → CH<sub>3</sub>–O–CH<sub>3</sub> + Br<sup>−</sup>. O produto, com o oxigênio entre dois carbonos, é um <strong>éter</strong> (dimetil éter). Alternativa <strong>A</strong>.</p>",
  tags=["substituição nucleofílica", "éteres"],
  enun=p("Nucleófilos (Nu<sup>−</sup>) são bases de Lewis que reagem com haletos de alquila, por meio de uma reação chamada substituição nucleofílica (S<sub>N</sub>), como mostrado no esquema:") + EQ("R–X + Nu<sup>−</sup> → R–Nu + X<sup>−</sup> &nbsp; (R = grupo alquila e X = halogênio)")
       + p("A reação de S<sub>N</sub> entre metóxido de sódio (Nu<sup>−</sup> = CH<sub>3</sub>O<sup>−</sup>) e brometo de metila fornece um composto orgânico pertencente à função"))
X(77, "Física", "Dinâmica", "<p>Antes do choque, o carrinho 1 vai de 15 cm a 30 cm em 1 s: v = 15 cm/s. Depois, os dois juntos vão de 75 cm a 90 cm em 3 s: v = 5 cm/s. Pela conservação da quantidade de movimento:</p><p>150 × 15 = (150 + m) × 5 → 150 + m = 450 → m = <strong>300 g</strong>. Alternativa <strong>C</strong>.</p><p>450 g (D) é a massa dos dois carrinhos juntos.</p>",
  figs(("q77", "Trilho de ar horizontal com o carrinho 1 à esquerda, movendo-se para a direita, e o carrinho 2 parado mais adiante; quatro sensores ao longo do trilho.")),
  ["quantidade de movimento", "colisão inelástica"],
  enun=p(T(77, 0)) + "[[fig:1]]" + tabela(["Carrinho 1: posição (cm)", "Carrinho 1: instante (s)", "Carrinho 2: posição (cm)", "Carrinho 2: instante (s)"],
                                          [["15,0", "0,0", "45,0", "0,0"], ["30,0", "1,0", "45,0", "1,0"], ["75,0", "8,0", "75,0", "8,0"], ["90,0", "11,0", "90,0", "11,0"]]) + p(T(77, 5)))
X(78, "Química", "Equilíbrio químico", "<p>A queima da borracha vulcanizada (com enxofre) libera SO<sub>2</sub>, gás ácido. Para retê-lo, a solução deve ser básica, e quanto maior a constante de formação de OH<sup>−</sup>, melhor. Entre as bases do quadro, o hidrogenofosfato de potássio tem a maior constante (2,8 × 10<sup>−2</sup>). Alternativa <strong>D</strong>.</p><p>O hidrogenossulfato (E) tem constante alta, mas produz H<sub>3</sub>O<sup>+</sup>: é ácido.</p>",
  tags=["chuva ácida", "constante de basicidade"],
  enun=p(T(78, 0)) + tabela(["Substância", "Equilíbrio em solução aquosa", "Valor da constante de equilíbrio"], [
      ["Fenol", "C<sub>6</sub>H<sub>5</sub>OH + H<sub>2</sub>O ⇄ C<sub>6</sub>H<sub>5</sub>O<sup>−</sup> + H<sub>3</sub>O<sup>+</sup>", "1,3 × 10<sup>−10</sup>"],
      ["Piridina", "C<sub>5</sub>H<sub>5</sub>N + H<sub>2</sub>O ⇄ C<sub>5</sub>H<sub>5</sub>NH<sup>+</sup> + OH<sup>−</sup>", "1,7 × 10<sup>−9</sup>"],
      ["Metilamina", "CH<sub>3</sub>NH<sub>2</sub> + H<sub>2</sub>O ⇄ CH<sub>3</sub>NH<sub>3</sub><sup>+</sup> + OH<sup>−</sup>", "4,4 × 10<sup>−4</sup>"],
      ["Hidrogenofosfato de potássio", "HPO<sub>4</sub><sup>2−</sup> + H<sub>2</sub>O ⇄ H<sub>2</sub>PO<sub>4</sub><sup>−</sup> + OH<sup>−</sup>", "2,8 × 10<sup>−2</sup>"],
      ["Hidrogenossulfato de potássio", "HSO<sub>4</sub><sup>−</sup> + H<sub>2</sub>O ⇄ SO<sub>4</sub><sup>2−</sup> + H<sub>3</sub>O<sup>+</sup>", "3,1 × 10<sup>−2</sup>"]]) + p(T(78, 3)))
X(79, "Biologia", "Imunologia", "<p>A vacina age estimulando o sistema imune a produzir anticorpos. Entre os mecanismos dos probióticos, o que faz o mesmo é o número 4, “estímulo à produção de imunoglobulinas”. Alternativa <strong>B</strong>.</p><p>Os outros mecanismos (competição, substâncias antimicrobianas, disputa por adesão, integridade do epitélio) não envolvem o sistema imune.</p>",
  figs(("q79", "Esquema do epitélio intestinal com probióticos e patógenos e cinco mecanismos numerados: 1, competição por nutrientes; 2, produção de substâncias antimicrobianas; 3, disputa por sítio de adesão; 4, estímulo à produção de imunoglobulinas; 5, manutenção da integridade epitelial. Aparecem também células dendríticas e células intestinais.")),
  ["probióticos", "vacinas"], enun=p(T(79, 0)) + "[[fig:1]]" + fonte(T(79, 2)) + p(T(79, 3)))
X(80, "Biologia", "Questões ambientais", "<p>Adaptação é preparar-se para os efeitos já em andamento, como a subida do nível do mar. Construir <strong>diques de contenção em regiões costeiras</strong> protege as cidades desse efeito. Alternativa <strong>E</strong>.</p><p>Usinas eólicas, tratamento de resíduos, veículos eficientes e agricultura de baixo carbono (A a D) reduzem emissões: são mitigação.</p>",
  tags=["mudanças climáticas", "adaptação e mitigação"], trocas=[("As estratégias de mitigação", "As <em>estratégias de mitigação</em>"), ("As estratégias de adaptação", "As <em>estratégias de adaptação</em>")])
X(81, "Química", "Polaridade", "<p>A testosterona tem um grupo OH, polar, que interage com a água. No composto 1 o OH é trocado por H, e no composto 2 por CH<sub>3</sub>: os dois perdem esse grupo polar e ficam mais afins a ambientes apolares. As lipofilias são <strong>maior e maior que a lipofilia da testosterona</strong>. Alternativa <strong>D</strong>.</p>",
  figs(("q81", "Estrutura esteroide da testosterona, com quatro anéis, um grupo C=O num anel e um substituinte X no outro: X = OH (testosterona), X = H (composto 1), X = CH₃ (composto 2).")),
  ["lipofilia", "polaridade"], enun=p(T(81, 0)) + "[[fig:1]]" + fonte(T(81, 4).replace("Revista Virtual de Química", "<strong>Revista Virtual de Química</strong>")) + p(T(81, 5)))
X(82, "Física", "Estática", "<p>Para mover o navio, Arquimedes precisa vencer o atrito estático: 0,8 × 3 000 × 10 = 24 000 N. Com polias móveis ideais, cada uma divide a força por 2: 400 × 2<sup>n</sup> ≥ 24 000 → 2<sup>n</sup> ≥ 60. Com 5 polias, 32 não basta; com <strong>6</strong>, 64 basta. Alternativa <strong>B</strong>.</p>",
  figs(("q82", "Esquema de polias: uma polia fixa presa a uma parede e polias móveis em série, ligadas a um bloco; a força F puxa a ponta da corda.")),
  ["polias", "atrito"],
  enun=p(T(82, 0) + " força <em>F</em>, paralela à direção do movimento e de módulo igual a 400 N. Considere os fios e as polias ideais, a aceleração da gravidade igual a 10 m/s<sup>2</sup> e que a superfície da praia é perfeitamente horizontal.") + "[[fig:1]]" + fonte(T(82, 5)) + p(T(82, 6)))
X(83, "Biologia", "Genética", "<p>A permutação (<em>crossing-over</em>) troca trechos entre cromátides homólogas na prófase I da meiose, criando cromossomos com novas combinações de alelos. Ela é determinante na <strong>recombinação genética na formação dos gametas</strong>. Alternativa <strong>C</strong>.</p><p>Não muda o número de cromossomos (E) e não transmite características adquiridas (B).</p>",
  tags=["crossing-over", "meiose"])
X(84, "Física", "Termologia", "<p>As duas bandejas estão na mesma temperatura (a do ambiente). O alumínio parece mais frio ao toque porque conduz calor muito melhor e o tira da mão mais depressa. Pelo mesmo motivo, ele leva calor ao gelo mais rápido: o gelo derrete <strong>mais rapidamente na bandeja de alumínio, pois ela tem uma maior condutividade térmica que a de plástico</strong>. Alternativa <strong>A</strong>.</p><p>As temperaturas iniciais são iguais (B); o que muda é a condução.</p>",
  tags=["condutividade térmica", "sensação térmica"])
X(85, "Química", "Química orgânica", "<p>A parte iônica (carboxilato) é polar e fica na água; a cadeia de carbono, apolar, fica fora dela, no ar. Na superfície, as moléculas formam uma camada com as “cabeças” no nível da água e as “caudas” para cima. É o arranjo C. Alternativa <strong>C</strong>.</p><p>Nos outros desenhos, as cadeias ficam dentro da água, ou as cabeças ficam fora dela.</p>",
  figs(("q85", "Fórmula estrutural do tensoativo, uma cadeia de carbonos terminando num grupo carboxilato, e sua representação esquemática: uma linha ondulada (a cadeia) com uma bola preta na ponta (a parte iônica)."),
       ("q85a", "Alternativa A: camada de bolas pretas no nível da água, com as caudas para baixo, dentro da água."),
       ("q85b", "Alternativa B: camada de bolas pretas acima do nível da água, com as caudas para baixo, entre a água e as bolas."),
       ("q85c", "Alternativa C: camada de bolas pretas no nível da água, com as caudas para cima, fora da água."),
       ("q85d", "Alternativa D: camada de bolas pretas no fundo do béquer, com as caudas para cima, dentro da água."),
       ("q85e", "Alternativa E: camada de bolas pretas abaixo do nível da água, com as caudas para cima, ainda dentro da água.")),
  ["tensoativos", "polaridade"], enun=p(T(85, 0)) + "[[fig:1]]" + p(T(85, 3), T(85, 4)), alts=ALT(2))
X(86, "Física", "Ondulatória", "<p>A manteiga derrete onde a energia é máxima, nos ventres (antinós) da onda estacionária. Na figura, os ventres estão nas posições I, III e V; os nós, em II e IV. Dois pontos consecutivos de manteiga derretida são <strong>I e III</strong>. Alternativa <strong>A</strong>.</p><p>II e IV são nós, onde a amplitude é nula.</p>",
  figs(("q86", "Trecho de onda estacionária com setas marcando cinco posições: I, III e V nos pontos de amplitude máxima (ventres) e II e IV nos pontos onde as curvas se cruzam (nós).")),
  ["onda estacionária", "micro-ondas"], enun=p(T(86, 0)) + "[[fig:1]]" + p(T(86, 3)),
  alts={"A": "I e III", "B": "I e V", "C": "II e III", "D": "II e IV", "E": "II e V"})
X(87, "Biologia", "Fisiologia humana", "<p>O ADH faz os rins reabsorverem água. No diabetes insípido, falta ADH ou ele não age: o paciente elimina muita urina diluída e perde água. O sintoma clássico é a <strong>desidratação</strong>, com muita sede. Alternativa <strong>E</strong>.</p><p>Glicose alta (A) é sintoma do diabetes melito.</p>",
  tags=["ADH", "diabetes insípido"], trocas=[("diabetes insipidus reclamam", "diabetes <em>insipidus</em> reclamam"), ("diabetes: mellitus e insipidus.", "diabetes: <em>mellitus</em> e <em>insipidus</em>."), ("diabetes insipidus é", "diabetes <em>insipidus</em> é"), ("diabetes insipidus?", "diabetes <em>insipidus</em>?")])
X(88, "Física", "Eletromagnetismo", "<p>O campo magnético alternado faz as nanopartículas, que são pequenos ímãs, girarem para acompanhar a inversão do campo. Esse movimento dentro da célula gera calor por atrito: <strong>o campo magnético alternado faz as nanopartículas girarem, transferindo calor por atrito</strong>. Alternativa <strong>B</strong>.</p><p>O campo não “contém” calor para fornecer (D), e com o campo alternado as partículas não seguem num só sentido (E).</p>",
  tags=["magnetismo", "hipertermia"])
X(89, "Química", "Polaridade", "<p>No gráfico, a temperatura do n-hexano praticamente não muda: fica perto de 30 °C de 0 s a 40 s. O hexano é apolar, não tem dipolo para interagir com as micro-ondas. Sua taxa média de aquecimento é a mais próxima de zero. Alternativa <strong>E</strong>.</p>",
  figs(("q89", "Gráfico da temperatura (°C) em função do tempo (s), de 0 a 80 s, para água, metanol, etanol, propanol e n-hexano. Propanol, etanol e metanol aquecem mais rápido; a água aquece de forma constante; o n-hexano fica praticamente em 30 °C.")),
  ["micro-ondas", "moléculas polares"], enun=p(T(89, 0)) + "[[fig:1]]" + fonte("BARBOZA, A. C. R. N. et al. Aquecimento em forno de micro-ondas. Desenvolvimento de alguns conceitos fundamentais. <strong>Química Nova</strong>, n. 6, 2001 (adaptado).") + p(T(89, 3)),
  alts={k: SUB(v) for k, v in D[89]["alternativas"].items()})
X(90, "Biologia", "Evolução", "<p>Todos os seres vivos, de bactérias a animais, fabricam proteínas do mesmo modo: o DNA é transcrito em RNA, que é traduzido nos ribossomos usando praticamente o mesmo código genético. A <strong>síntese proteica</strong> universal é evidência de uma origem comum. Alternativa <strong>E</strong>.</p><p>Muitos seres não têm desenvolvimento embrionário, reprodução sexuada, respiração aeróbica ou excreção urinária (A a D).</p>",
  tags=["origem da vida", "código genético"])

completar(Q, R)
