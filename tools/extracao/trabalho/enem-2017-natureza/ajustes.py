# Enem 2017, 2º dia, caderno azul: Ciências da Natureza (questões 91 a 135; no site, 1 a 45).
# Texto legível (sem DECOD). A Q118 saiu fundida com a Q117 no rascunho: enunciado e alternativas das duas digitados a partir da prova.
# Quadros das Q91, 98 e 121 e equações da Q124 em HTML. Alternativas-imagem: Q108, 121 e 125. Sem anuladas.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, paragrafos_enem

ID = "enem-2017-natureza"
META = {"id": ID, "banca": "Enem", "ano": 2017, "titulo": "Enem 2017: Ciências da Natureza", "fonte": "Inep", "dataExame": "2017-11-12",
        "duracaoMinutos": 150, "area": "Ciências da Natureza", "caderno": "azul", "dia": 2}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2017-dia2-azul")
Q = {}
P = lambda n: paragrafos_enem(D[n])
T = lambda n, i: P(n)[i][1]
p = lambda *xs: "".join(f"<p>{x}</p>" for x in xs)
ap = lambda *xs: "".join(f'<p class="apoio">{x}</p>' for x in xs)
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
    Q[n - 90] = {"materia": materia, "assunto": assunto, "area": "Ciências da Natureza", "tags": list(tags), "numeroOriginal": n,
                 "enunciado": e, "alternativas": {k: LIMPA(v) for k, v in dict(alts or D[n]["alternativas"]).items()},
                 "imagens": list(imagens), "explicacao": expl}
    if anulacao: Q[n - 90]["anulacao"] = anulacao


SUB = lambda s: re.sub(r"(?<=[A-Za-z\)])(\d+)", r"<sub>\1</sub>", s)
LISTA = lambda s: "<ul>" + "".join(f"<li>{x.strip()}</li>" for x in s.split("•") if x.strip()) + "</ul>"
CH = lambda s: s.replace("NH3", "NH<sub>3</sub>").replace("Na2CO3", "Na<sub>2</sub>CO<sub>3</sub>").replace("Na2SO4", "Na<sub>2</sub>SO<sub>4</sub>")

X(91, "Biologia", "Toxicologia", "<p>Cada rato (0,2 kg) comeu 100 g de ração com 3 mg de pesticida por grama: 300 mg. A dose foi 300 mg ÷ 0,2 kg = 1 500 mg/kg.</p><p>Uma mortalidade mínima de 10 ratos (50% dos 20) exige dose igual ou maior que a DL<sub>50</sub>. Isso vale para o diazinon (70 mg/kg) e o malation (1 000 mg/kg), mas não para a atrazina (3 100 mg/kg). Alternativa <strong>D</strong>.</p>",
  tags=["DL50", "dose por massa corporal"],
  enun=p(T(91, 0).replace("DL50", "DL<sub>50</sub>")) + tabela(["Pesticidas", "DL<sub>50</sub> (mg/kg)"], [["Diazinon", "70"], ["Malation", "1 000"], ["Atrazina", "3 100"]]) + p(T(91, 2), T(91, 3)))
X(92, "Biologia", "Microbiologia", "<p>Os antibióticos agem sobre estruturas que só as bactérias têm, ou que nelas são diferentes das nossas: a parede celular (como a penicilina), os ribossomos bacterianos ou enzimas próprias. Eles atuam <strong>danificando estruturas específicas da célula bacteriana</strong>. Alternativa <strong>E</strong>.</p><p>Antibióticos não ativam o sistema imune (A) nem atacam as células do hospedeiro (D).</p>",
  tags=["antibióticos"])
X(93, "Física", "Eletrodinâmica", "<p>Pelo gráfico, sem amônia, com 1,0 V passam 2,0 × 10<sup>−6</sup> A: R = U ÷ i = 1,0 ÷ (2,0 × 10<sup>−6</sup>) = 5,0 × 10<sup>5</sup> Ω.</p><p>Com muita amônia, a resistência quadruplica: 4 × 5,0 × 10<sup>5</sup> = <strong>2,0 × 10<sup>6</sup> Ω</strong>. Alternativa <strong>E</strong>.</p><p>5,0 × 10<sup>5</sup> Ω (D) é a resistência sem amônia.</p>",
  figs(("q93", "Gráfico da corrente (10⁻⁶ A) em função da diferença de potencial (V): pontos alinhados numa reta que passa pela origem, de (0,5 V; 1,0) a (3,0 V; 6,0).")),
  ["lei de Ohm", "sensores"], enun=p(T(93, 0)) + "[[fig:1]]" + p("O valor da resistência elétrica da polianilina na presença de altas concentrações de amônia, em ohm, é igual a"),
  alts={"A": "0,5 × 10<sup>0</sup>.", "B": "2,0 × 10<sup>0</sup>.", "C": "2,5 × 10<sup>5</sup>.", "D": "5,0 × 10<sup>5</sup>.", "E": "2,0 × 10<sup>6</sup>."})
X(94, "Biologia", "Fotossíntese", "<p>O texto diz que os nanotubos absorvem comprimentos de onda que os pigmentos dos cloroplastos não captam, funcionando como “antenas”. Eles promovem diretamente a <strong>absorção de fótons</strong>. Alternativa <strong>B</strong>.</p><p>Mais oxigênio e mais uso de CO<sub>2</sub> (C e E) são consequências, não o efeito direto.</p>",
  tags=["nanotecnologia", "fase luminosa"])
X(95, "Química", "Eletroquímica", "<p>Na eletrólise da salmoura, o cloro é oxidado no ânodo (2 Cl<sup>−</sup> → Cl<sub>2</sub>). No cátodo, a água é reduzida: 2 H<sub>2</sub>O + 2 e<sup>−</sup> → H<sub>2</sub> + 2 OH<sup>−</sup>. O produto que sai junto ao cátodo, além da solução alcalina de NaOH, é o <strong>hidrogênio molecular</strong>. Alternativa <strong>D</strong>.</p><p>O diafragma impede que o cloro encontre o NaOH, o que formaria hipoclorito (C).</p>",
  figs(("q95", "Célula eletroquímica ligada a uma bateria: solução aquosa de NaCl entra por cima; no ânodo de carbono (+) sai Cl₂ gasoso; um diafragma de amianto separa os compartimentos; no cátodo de carbono (−) sai o “produto secundário”, e embaixo há um dreno para a solução aquosa alcalina.")),
  ["eletrólise", "cloro-soda"], enun=p(T(95, 0)) + "[[fig:1]]" + fonte(T(95, 4)) + p(T(95, 5)))
X(96, "Biologia", "Ciclos biogeoquímicos", "<p>No ciclo do nitrogênio, a nitrificação acontece em duas etapas: a nitrosação, em que bactérias transformam amônia em nitrito, e a nitratação, em que o nitrito vira nitrato. O nitrato, componente dos fertilizantes, é produzido na <strong>nitratação</strong>. Alternativa <strong>A</strong>.</p><p>A desnitrificação (D) faz o contrário: devolve o nitrogênio à atmosfera.</p>",
  tags=["nitrificação", "fertilizantes"])
X(97, "Química", "Atomística", "<p>O calor da chama excita os elétrons do sódio do sal; ao voltarem ao nível de origem, eles liberam a energia como luz de comprimento de onda característico, amarela. É o teste da chama: a <strong>emissão de fótons pelo sódio, excitado por causa da chama</strong>. Alternativa <strong>B</strong>.</p>",
  tags=["teste de chama", "modelo de Bohr"], trocas=[("sal de cozinha (NaCl)", "sal de cozinha (NaCl)")])
X(98, "Biologia", "Classificação dos seres vivos", "<p>Whittaker classificava os seres pela organização celular e pelo modo de nutrição. Woese comparou sequências do RNA ribossômico para estabelecer relações de ancestralidade, dividindo os seres em Archaea, Bacteria e Eukarya. A classificação mais recente se baseia em <strong>relações filogenéticas</strong>. Alternativa <strong>C</strong>.</p><p>Tipos de células e morfologia (A e E) são os critérios de Whittaker.</p>",
  tags=["três domínios", "Woese"],
  enun=p(T(98, 0)) + tabela(["Whittaker (1969) – Cinco reinos", "Woese (1990) – Três domínios"], [["Monera", "Archaea e Eubacteria"], ["Protista, Fungi, Plantae e Animalia", "Eukarya"]]) + p(T(98, 2)))
X(99, "Física", "Dinâmica", "<p>Pela segunda lei de Newton, a força do cinto sobre o corpo é proporcional à aceleração. Como todas as colisões levam o boneco da mesma velocidade ao repouso, o cinto mais seguro é o que distribui a frenagem ao longo do tempo, com o menor pico de aceleração. No gráfico, é o cinto 2 (curva pontilhada), que não passa de cerca de 65 m/s². Alternativa <strong>B</strong>.</p><p>Os cintos 3 e 5 têm picos próximos de 200 e 170 m/s².</p>",
  figs(("q99", "Gráfico da aceleração (m/s²) em função do tempo (s), de 0 a 0,30 s, para cinco cintos. Cinto 1 (traço e ponto): pico estreito de cerca de 150 m/s² perto de 0,07 s. Cinto 2 (pontilhado): curva larga e baixa, com máximo de cerca de 65 m/s² perto de 0,15 s. Cinto 3 (cinza): pico estreito de quase 200 m/s² em 0,15 s. Cinto 4 (preto): pico de cerca de 85 m/s² em 0,21 s. Cinto 5 (tracejado): pico de cerca de 170 m/s² perto de 0,28 s.")),
  ["impulso", "segunda lei de Newton"], enun=p(T(99, 0)) + "[[fig:1]]" + p(T(99, 6)))
X(100, "Biologia", "Fisiologia humana", "<p>A plaqueta artificial acelera a coagulação. Quem mais se beneficia é quem tem dificuldade de coagular o sangue: os pacientes com <strong>hemofilia</strong>, doença genética que reduz os fatores de coagulação. Alternativa <strong>B</strong>.</p><p>Na aterosclerose (C), acelerar a coagulação aumentaria o risco de trombose.</p>",
  tags=["coagulação", "hemofilia"])
X(101, "Física", "Ondulatória", "<p>O arquiteto quer luz visível sem aquecer o ambiente, isto é, com pouca emissão no infravermelho. A lâmpada de LED tem quase toda a energia dentro da faixa visível, sobre a curva de sensibilidade do olho, e praticamente nada no IV. Alternativa <strong>E</strong>.</p><p>A de tungstênio (B) emite muito no infravermelho e esquenta.</p>",
  figs(("q101", "Espectros de emissão de cinco lâmpadas, de 200 a 900 nm, com as regiões UV, visível e IV marcadas e, em pontilhado, a sensibilidade do olho. Haleto metálico: picos espalhados pelo visível. Tungstênio: emissão que cresce continuamente para o infravermelho. Mercúrio: picos estreitos no UV e no visível. Xênon: emissão no visível com picos fortes no infravermelho. LED: emissão concentrada no visível, entre cerca de 430 e 700 nm.")),
  ["espectro eletromagnético", "eficiência luminosa"], enun=p(T(101, 0), T(101, 1), T(101, 2)) + "[[fig:1]]" + fonte(T(101, 5)) + p(T(101, 6)))
X(102, "Química", "Forças intermoleculares", "<p>Os núcleos de condensação são sais de amônio (NH<sub>4</sub>X), sólidos iônicos. As moléculas de água, polares, se prendem aos íons NH<sub>4</sub><sup>+</sup> e X<sup>−</sup> por <strong>interações íon-dipolo</strong>. Alternativa <strong>D</strong>.</p><p>Não se formam ligações novas entre água e sal (A e E): é uma atração intermolecular.</p>",
  tags=["íon-dipolo", "nuvens"],
  enun=p(T(102, 0).replace("NH3", "NH<sub>3</sub>").replace("(NH4X)", "(NH<sub>4</sub><em>X</em>)").replace("(HX)", "(H<em>X</em>)")) + '<p class="apoio">H<em>X</em> (g) + NH<sub>3</sub> (g) → NH<sub>4</sub><em>X</em> (s)</p>' + fonte(T(102, 2)) + p(T(102, 3)))
X(103, "Física", "Ondulatória", "<p>O sinal pode perder no máximo de 100 dB (o máximo transmitido) até 10 dB (quando precisa ser retransmitido): 90 dB. A distância é máxima com a menor perda por quilômetro, que no gráfico é 1 dB/km, perto de 1,5 µm. Assim, 90 dB ÷ 1 dB/km = <strong>90 km</strong>. Alternativa <strong>D</strong>.</p>",
  figs(("q103", "Gráfico da perda óptica (dB/km) em função do comprimento de onda (µm), de 0,8 a 1,8: a curva desce de 6, tem picos em cerca de 1,0 µm e 1,4 µm (cerca de 5 dB/km) e o menor valor, 1 dB/km, perto de 1,5 µm, antes de subir de novo.")),
  ["decibel", "fibra óptica"], enun=p(T(103, 0)) + "[[fig:1]]" + fonte(T(103, 5)) + p(T(103, 6)))
X(104, "Química", "Radioatividade", "<p>6 750 emissões por hora ÷ 60 = 112,5 por minuto; ÷ 30 g = 3,75 emissões/(min g).</p><p>De 15 para 3,75, a atividade caiu à quarta parte: passaram-se duas meias-vidas, 2 × 5 730 = <strong>11 460 anos</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["meia-vida", "carbono-14"], enun=p(T(104, 0).replace("14C", "<sup>14</sup>C")) + fonte(T(104, 1)) + p(T(104, 2)))
X(105, "Física", "Energia", "<p>Quando há vento, a eletricidade das turbinas também produz hidrogênio, que fica armazenado. Sem vento, o hidrogênio é misturado ao biogás e queimado na planta mista, que gera calor e eletricidade para a rede. O <strong>hidrogênio produzido e armazenado é utilizado na combustão com o biogás para gerar calor e eletricidade</strong>. Alternativa <strong>B</strong>.</p><p>A eletrólise (A) é a etapa que produz hidrogênio, e nenhuma usina térmica transforma todo o calor em eletricidade (E).</p>",
  figs(("q105", "Esquema da estação híbrida: turbinas eólicas mandam eletricidade para a rede de distribuição e para a produção de hidrogênio; o hidrogênio é armazenado e vai para um posto de combustível e para uma válvula de mistura com biogás; a mistura alimenta a planta mista de geração de energia, que manda eletricidade à rede e calor para um destino de energia térmica.")),
  ["energia eólica", "hidrogênio"], enun=p(T(105, 0)) + "[[fig:1]]" + fonte("Disponível em: www.enertrag.com. Acesso em: 24 abr. 2015 (adaptado).") + p(T(105, 4)))
X(106, "Química", "Propriedades físicas", "<p>Os óleos essenciais são voláteis. Com o calor do sol, ao longo do dia, eles evaporam das folhas; colhendo de madrugada, a planta ainda tem mais óleo. A explicação é a <strong>volatilização das substâncias de interesse</strong>. Alternativa <strong>A</strong>.</p>",
  tags=["volatilidade", "óleos essenciais"])
X(107, "Física", "Ondulatória", "<p>O comprimento ideal precisa ser bem absorvido pela melanina e pouco pela oxi-hemoglobina e pela água. Em 700 nm, a melanina absorve cerca de 35%, enquanto a oxi-hemoglobina chega perto de zero e a água ainda não absorve (só a partir de 900 nm). Alternativa <strong>B</strong>.</p><p>Em 400 e 500 nm a oxi-hemoglobina absorve muito (A e E); em 900 e 1 100 nm a água começa a absorver (C e D).</p>",
  figs(("q107", "Gráfico da absorção (%) em função do comprimento de onda (nm), de 400 a 1 100. A melanina começa perto de 45% e cai devagar até cerca de 22%. A oxi-hemoglobina começa alta, cai quase a zero perto de 700 nm e volta a subir um pouco depois. A água só aparece a partir de 900 nm, crescendo até cerca de 20%.")),
  ["laser", "absorção da luz"], trocas=[("A epilação a laser", "A epilação a <em>laser</em>"), ("depilação a laser)", "depilação a <em>laser</em>)")],
  enun=p(T(107, 0)) + "[[fig:1]]" + fonte(T(107, 6).replace("Revista Brasileira de Medicina", "<strong>Revista Brasileira de Medicina</strong>").replace("com laser", "com <em>laser</em>")) + p(T(107, 7).replace("laser?", "<em>laser</em>?")))
X(108, "Física", "Energia", "<p>Acima da lona (h &gt; 0), a criança está em queda livre: E<sub>c</sub> = E − mgh, que diminui em linha reta com a altura até zerar em h<sub>máx</sub>. Abaixo de h = 0, a lona age como mola: a energia elástica cresce com o quadrado da deformação, e o trecho do gráfico é curvo, até E<sub>c</sub> zerar em h<sub>mín</sub>. A energia cinética máxima fica pouco abaixo de h = 0, onde a força da lona iguala o peso. É o gráfico da alternativa C: uma curva que sobe de h<sub>mín</sub> e uma reta que desce até h<sub>máx</sub>. Alternativa <strong>C</strong>.</p><p>No gráfico B, o trecho de baixo seria reto, o que não acontece com uma força elástica.</p>",
  figs(("q108a", "Alternativa A: E_c cai em linha reta de h_mín até zero em h = 0 e depois sobe em linha reta até h_máx."),
       ("q108b", "Alternativa B: E_c sobe em linha reta de zero em h_mín até o máximo em h = 0 e depois desce em linha reta até zero em h_máx."),
       ("q108c", "Alternativa C: E_c sobe numa curva de zero em h_mín até o máximo perto de h = 0 e depois desce em linha reta até zero em h_máx."),
       ("q108d", "Alternativa D: E_c sobe em linha reta de h_mín até h = 0 e depois desce numa curva até zero em h_máx."),
       ("q108e", "Alternativa E: E_c em forma de curva em U, mínima perto de h = 0 e máxima em h_máx.")),
  ["conservação de energia", "energia elástica"],
  enun=p(T(108, 0).replace("(h = 0)", "(<em>h</em> = 0)").replace("hmáx e hmín", "<em>h</em><sub>máx</sub> e <em>h</em><sub>mín</sub>"), T(108, 1)), alts=ALT(1))
X(109, "Biologia", "Ecologia", "<p>Na piracema, os peixes sobem o rio até as cabeceiras para se reproduzir. A barragem fica no caminho e corta o trajeto: reduz o <strong>percurso da migração</strong>. Alternativa <strong>A</strong>.</p><p>O período da migração (D) depende das chuvas, não da barragem.</p>",
  tags=["piracema", "barragens"])
X(110, "Física", "Eletrodinâmica", "<p>A fonte está ligada entre os nós da esquerda (L) e da direita (R). Em cima: de L ao topo, 60 Ω; do topo a R, 60 Ω em paralelo com 30 Ω = 20 Ω; ramo superior = 80 Ω. Embaixo: de L ao nó de baixo, 60 Ω em paralelo com o ramo de 120 Ω + fusível = 40 Ω; desse nó a R, 40 Ω; ramo inferior = 80 Ω.</p><p>No ramo inferior, os dois trechos de 40 Ω dividem a tensão ao meio: U/2 fica sobre o resistor de 120 Ω com o fusível. A corrente no fusível é (U/2) ÷ 120 ≤ 0,5 A, logo U ≤ <strong>120 V</strong>. Alternativa <strong>D</strong>.</p>",
  figs(("q110", "Circuito em losango alimentado pela fonte U, ligada aos vértices da esquerda e da direita. Lado superior esquerdo: 60 Ω; superior direito: 60 Ω, com um resistor de 30 Ω ligando o vértice de cima à direita. Lado inferior esquerdo: 60 Ω, com um ramo paralelo de 120 Ω em série com o fusível ligando o vértice da esquerda ao de baixo. Lado inferior direito: 40 Ω.")),
  ["associação de resistores", "fusível"], enun=p(T(110, 0).replace("tensão U", "tensão <em>U</em>")) + "[[fig:1]]" + p("Qual é o máximo valor da tensão <em>U</em> para que o fusível não queime?"))
X(111, "Biologia", "Ecologia", "<p>O mercúrio não é eliminado pelo organismo e se acumula ao longo da cadeia alimentar: cada nível concentra o que comeu do anterior. Os botos, predadores de peixes, <strong>estão no topo da cadeia alimentar</strong> e acumulam mais. Alternativa <strong>E</strong>.</p>",
  tags=["magnificação trófica", "mercúrio"], trocas=[("(Sotalia guianensis)", "(<em>Sotalia guianensis</em>)")])
X(112, "Física", "Ondulatória", "<p>O som fica nulo quando as duas ondas chegam em oposição de fase: a diferença de caminho é meio comprimento de onda. Pela figura, a parte móvel se deslocou 40 − 30 = 10 cm, e o trajeto ADC aumentou 2 × 10 = 20 cm (ida e volta).</p><p>λ/2 = 0,20 m → λ = 0,40 m. f = v ÷ λ = 320 ÷ 0,40 = <strong>800 Hz</strong>. Alternativa <strong>C</strong>.</p>",
  figs(("q112", "Trombone de Quincke: um tubo em forma de pista oval; a fonte sonora fica no ponto A, em cima, e o detector no ponto C, embaixo; o som segue pelos ramos ADC (esquerdo, que pode ser alongado) e AEC (direito). Cotas: 40 cm do lado esquerdo e 30 cm do lado direito, medidos a partir de A.")),
  ["interferência", "comprimento de onda"], enun=p(T(112, 0)) + "[[fig:1]]" + p(T(112, 4)))
X(113, "Química", "Separação de misturas", "<p>O óleo é lipossolúvel: sai da farinha junto com o éter, no extrato etéreo. Na destilação desse extrato, o éter, volátil, vai para o Destilado 1, e o óleo, de massa molecular alta, fica no <strong>Resíduo 4</strong>. Alternativa <strong>E</strong>.</p><p>No extrato aquoso (Destilado 2 e Resíduo 3) ficam as substâncias solúveis em água.</p>",
  figs(("q113", "Esquema: farinha de linhaça + éter etílico, agitação e filtração → Resíduo 1 e extrato etéreo (fase orgânica); o extrato etéreo é destilado em Destilado 1 e Resíduo 4. O Resíduo 1 + água, agitação e filtração → Resíduo 2 e extrato aquoso, que é destilado em Destilado 2 e Resíduo 3.")),
  ["extração", "destilação"], enun=p(T(113, 0), T(113, 1)) + "[[fig:1]]" + p(T(113, 3)))
X(114, "Química", "Funções orgânicas", "<p>Na transesterificação, o triglicerídeo reage com metanol e forma glicerol e ésteres metílicos (CH<sub>3</sub>–O–CO–R). O biodiesel tem o grupo –COO– ligado a carbonos dos dois lados: é um <strong>éster</strong>. Alternativa <strong>B</strong>.</p><p>O glicerol, o outro produto, é um álcool (C).</p>",
  figs(("q114", "Equação: um triglicerídeo (três grupos –O–CO–R ligados a uma cadeia de três carbonos) + 3 CH₃OH, com catalisador, forma três moléculas CH₃–O–CO–R (com R₁, R₂ e R₃) + glicerol (três carbonos, cada um com OH).")),
  ["biodiesel", "transesterificação"], enun=p(T(114, 0)) + "[[fig:1]]" + p(T(114, 4)))
X(115, "Física", "Dinâmica", "<p>Na rotação, todos os componentes giram com a mesma velocidade angular, mas os mais densos tendem a se afastar do eixo e se depositam no fundo do tubo, e os menos densos ficam mais perto do centro. A separação ocorre em função <strong>das diferentes densidades</strong>. Alternativa <strong>A</strong>.</p>",
  tags=["centrifugação", "movimento circular"], trocas=[("Dicionário Houaiss de física", "<em>Dicionário Houaiss de física</em>")])
X(116, "Biologia", "Citologia", "<p>Logo após a fusão, as proteínas de camundongo e humanas ficam cada uma de um lado. Depois de 40 minutos a 37 °C, as duas marcações aparecem misturadas por toda a célula. Isso mostra que as proteínas <strong>movimentam-se livremente no plano da bicamada lipídica</strong>, como diz o modelo do mosaico fluido. Alternativa <strong>A</strong>.</p><p>Os anticorpos só marcam as proteínas (D e E); a mistura vem da fluidez da membrana.</p>",
  figs(("q116", "Etapa 1: uma célula de camundongo e uma célula humana, cada uma com suas proteínas de membrana. Etapa 2: fusão celular, formando uma célula híbrida. Etapa 3 (tempo 0): anticorpos marcados com fluoresceína ligados às proteínas de camundongo numa metade e anticorpos com rodamina às proteínas humanas na outra. Etapa 4 (40 minutos, a 37 °C): as duas marcações espalhadas e misturadas por toda a membrana.")),
  ["mosaico fluido", "membrana plasmática"], enun=p(T(116, 0)) + "[[fig:1]]" + fonte("ALBERTS, B. et al. <strong>Biologia molecular da célula</strong>. Porto Alegre: Artes Médicas, 1997 (adaptado).") + p(T(116, 4)))
X(117, "Biologia", "Genética", "<p>Nas mulheres, um dos cromossomos X de cada célula é inativado ao acaso no início do desenvolvimento embrionário. Se isso ocorre depois da divisão que forma as gêmeas, cada uma pode ter um padrão diferente: em uma, ficou ativo principalmente o X com o alelo mutante, e ela manifesta a DMD; na outra, o X normal. A explicação é a <strong>inativação aleatória de um dos cromossomos X em fase posterior à divisão que resulta nos dois embriões</strong>. Alternativa <strong>D</strong>.</p><p>As gêmeas são monozigóticas: têm os mesmos cromossomos, com a mesma origem paterna e materna (E).</p>",
  tags=["inativação do X", "gêmeos monozigóticos"],
  enun=p(T(117, 0)) + fonte(T(117, 1).replace("The American Journal of Human Genetics", "<strong>The American Journal of Human Genetics</strong>")) + p(T(117, 2)),
  alts={"A": "dominância incompleta do alelo mutante em relação ao alelo normal.", "B": "falha na separação dos cromossomos X no momento da separação dos dois embriões.",
        "C": "recombinação cromossômica em uma divisão celular embrionária anterior à separação dos dois embriões.", "D": "inativação aleatória de um dos cromossomos X em fase posterior à divisão que resulta nos dois embriões.",
        "E": "origem paterna do cromossomo portador do alelo mutante em uma das gêmeas e origem materna na outra."})
X(118, "Biologia", "Questões ambientais", "<p>O piso de concreto comum cobre todo o solo, e a água da chuva escorre em vez de infiltrar. O concregrama tem espaços com grama por onde a água penetra. O objetivo é evitar a <strong>impermeabilização</strong> do solo. Alternativa <strong>A</strong>.</p>",
  figs(("q118", "Duas peças de piso: à esquerda, o piso tradicional de concreto, uma superfície contínua; à direita, o piso concregrama, uma placa de concreto com quatro aberturas preenchidas com grama.")),
  ["impermeabilização do solo", "drenagem urbana"],
  enun=p("Para se adequar às normas ambientais atuais, as construtoras precisam prever em suas obras a questão do uso de materiais de modo a minimizar os impactos causados no local. Entre esses materiais está o chamado concregrama ou pisograma, que é um tipo de revestimento composto por peças de concreto com áreas vazadas, preenchidas com solo gramado. As figuras apresentam essas duas formas de piso feitos de concreto.")
       + "[[fig:1]]" + fonte(D[117]["paragrafos"][-1][1]) + p("A utilização desse tipo de piso em uma obra tem o objetivo de evitar, no solo, a"),
  alts={"A": "impermeabilização.", "B": "diminuição da temperatura.", "C": "acumulação de matéria orgânica.", "D": "alteração do pH.", "E": "salinização."})
X(119, "Química", "Ácidos e bases", "<p>O lapachol é um ácido fraco (pK<sub>a</sub> = 6,0). Numa solução básica, ele perde o H<sup>+</sup> da hidroxila e vira um sal, solúvel em água, que sai da serragem e passa pelo filtro. O carbonato de sódio é básico: a melhor opção é a <strong>solução de Na<sub>2</sub>CO<sub>3</sub> para formar um sal de lapachol</strong>. Alternativa <strong>A</strong>.</p><p>Em pH 4,5 ou com HCl (B e E), o meio ácido mantém o lapachol na forma neutra, pouco solúvel.</p>",
  figs(("q119", "Estrutura do lapachol: uma naftoquinona (dois anéis fundidos, com dois grupos C=O no anel da direita), com uma hidroxila e uma cadeia lateral com uma dupla ligação.")),
  ["pKa", "extração ácido-base"], enun=p(T(119, 0).replace("(pKa = 6,0)", "(p<em>K</em><sub>a</sub> = 6,0)").replace("pKa = −log Ka, em que Ka", "p<em>K</em><sub>a</sub> = −log <em>K</em><sub>a</sub>, em que <em>K</em><sub>a</sub>")) + "[[fig:1]]" + fonte("COSTA, P. R. R. et al. <strong>Ácidos e bases em química orgânica</strong>. Porto Alegre: Bookman, 2005 (adaptado).") + p(T(119, 4)),
  alts={k: CH(v) for k, v in D[119]["alternativas"].items()})
X(120, "Química", "Propriedades coligativas", "<p>Naturalmente, a água iria do lado puro para o salgado (osmose). Para que ela faça o caminho inverso, a pressão mecânica tem de atuar em sentido contrário ao da pressão osmótica e ser maior que ela. As resultantes têm <strong>sentidos opostos e maior intensidade da pressão mecânica</strong>. Alternativa <strong>E</strong>.</p><p>Com intensidades iguais (B), não haveria fluxo resultante.</p>",
  tags=["osmose reversa", "dessalinização"])
X(121, "Química", "Eletroquímica", "<p>Cada pilha dá a diferença entre os potenciais de redução dos seus dois eletrodos. As melhores combinações são Ce<sup>4+</sup>/Ce<sup>3+</sup> com zinco (1,61 + 0,76 = 2,37 V) e dicromato com níquel (1,33 + 0,25 = 1,58 V): juntas, 3,95 V, acima dos 3,6 V. Para as tensões se somarem, o polo negativo de uma pilha deve ser ligado ao positivo da outra. Na montagem C, o zinco (polo negativo da primeira pilha) está ligado ao grafite do dicromato (polo positivo da segunda), e o LED fica entre o grafite do cério e o níquel. Alternativa <strong>C</strong>.</p><p>Em A e B, as pilhas estão ligadas pelos polos de mesmo sinal, e as tensões se subtraem; em D e E, cério e dicromato estão na mesma pilha, que dá só 0,28 V.</p>",
  figs(("q121a", "Alternativa A: pilha de grafite em Ce⁴⁺/Ce³⁺ com níquel em Ni²⁺, ligada pelo níquel ao zinco de uma pilha de zinco em Zn²⁺ com grafite em dicromato; o LED liga os dois grafites."),
       ("q121b", "Alternativa B: pilha de grafite em Ce⁴⁺/Ce³⁺ com zinco em Zn²⁺, ligada pelo zinco ao níquel de uma pilha de níquel em Ni²⁺ com grafite em dicromato; o LED liga os dois grafites."),
       ("q121c", "Alternativa C: pilha de grafite em Ce⁴⁺/Ce³⁺ com zinco em Zn²⁺, ligada pelo zinco ao grafite de uma pilha de grafite em dicromato com níquel em Ni²⁺; o LED liga o grafite do cério ao níquel."),
       ("q121d", "Alternativa D: pilha de grafite em Ce⁴⁺/Ce³⁺ com grafite em dicromato, ligada a uma pilha de níquel em Ni²⁺ com zinco em Zn²⁺; o LED liga o grafite do cério ao zinco."),
       ("q121e", "Alternativa E: pilha de grafite em Ce⁴⁺/Ce³⁺ com grafite em dicromato, ligada a uma pilha de zinco em Zn²⁺ com níquel em Ni²⁺; o LED liga o grafite do cério ao níquel.")),
  ["pilhas em série", "potencial padrão"],
  enun=p(T(121, 0)) + tabela(["Semirreação de redução", "<em>E</em>° (V)"], [["Ce<sup>4+</sup> (aq) + e<sup>−</sup> → Ce<sup>3+</sup> (aq)", "+1,61"], ["Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> (aq) + 14 H<sup>+</sup> (aq) + 6 e<sup>−</sup> → 2 Cr<sup>3+</sup> (aq) + 7 H<sub>2</sub>O (l)", "+1,33"], ["Ni<sup>2+</sup> (aq) + 2 e<sup>−</sup> → Ni (s)", "−0,25"], ["Zn<sup>2+</sup> (aq) + 2 e<sup>−</sup> → Zn (s)", "−0,76"]]) + p(T(121, 2)), alts=ALT(1))
X(122, "Química", "Estequiometria", "<p>Massa de AAS: 900 000 × 0,5 g = 450 000 g → 450 000 ÷ 180 = 2 500 mol. A proporção é 1 mol de ácido salicílico para 1 mol de AAS, mas o rendimento é de 50%: são necessários 5 000 mol de ácido salicílico.</p><p>5 000 × 138 g = 690 000 g = <strong>690 kg</strong>. Alternativa <strong>D</strong>.</p><p>Esquecer o rendimento dá a metade, 345 kg (B).</p>",
  figs(("q122", "Equação: ácido salicílico + anidrido acético, com H₂SO₄ como catalisador, formam ácido acetilsalicílico + ácido acético.")),
  ["rendimento", "massa molar"], enun=p(T(122, 0)) + "[[fig:1]]" + p(T(122, 7), T(122, 8)))
X(123, "Biologia", "Botânica", "<p>As bromélias vivem sobre os galhos, sem raízes no solo e sem tirar seiva da árvore (não são parasitas). Suas folhas em roseta formam um tanque que acumula água: elas captam água da <strong>chuva acumulada entre suas folhas</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["epífitas", "bromélias"])
X(124, "Química", "Termoquímica", "<p>Pela lei de Hess, combinam-se as equações para obter 6 FeO + 6 CO → 6 Fe + 6 CO<sub>2</sub>:</p><ul><li>2 × (3 FeO + CO<sub>2</sub> → Fe<sub>3</sub>O<sub>4</sub> + CO): −72 kJ;</li><li>2 Fe<sub>3</sub>O<sub>4</sub> + CO<sub>2</sub> → 3 Fe<sub>2</sub>O<sub>3</sub> + CO: +47 kJ;</li><li>3 × (Fe<sub>2</sub>O<sub>3</sub> + 3 CO → 2 Fe + 3 CO<sub>2</sub>): −75 kJ.</li></ul><p>Somando, ΔH = −100 kJ para 6 mol de FeO: −100 ÷ 6 ≈ <strong>−17 kJ/mol</strong>. Alternativa <strong>B</strong>.</p><p>−100 (E) é o valor para 6 mol, sem dividir.</p>",
  tags=["lei de Hess", "siderurgia"],
  enun=p(T(124, 0).replace("(α-Fe2O3)", "(α-Fe<sub>2</sub>O<sub>3</sub>)").replace("(Fe3O4)", "(Fe<sub>3</sub>O<sub>4</sub>)"))
       + '<p class="apoio">FeO (s) + CO (g) → Fe (s) + CO<sub>2</sub> (g)</p>' + p(T(124, 2))
       + '<p class="apoio">Fe<sub>2</sub>O<sub>3</sub> (s) + 3 CO (g) → 2 Fe (s) + 3 CO<sub>2</sub> (g) &nbsp; Δ<sub>r</sub><em>H</em>° = −25 kJ/mol de Fe<sub>2</sub>O<sub>3</sub><br>3 FeO (s) + CO<sub>2</sub> (g) → Fe<sub>3</sub>O<sub>4</sub> (s) + CO (g) &nbsp; Δ<sub>r</sub><em>H</em>° = −36 kJ/mol de CO<sub>2</sub><br>2 Fe<sub>3</sub>O<sub>4</sub> (s) + CO<sub>2</sub> (g) → 3 Fe<sub>2</sub>O<sub>3</sub> (s) + CO (g) &nbsp; Δ<sub>r</sub><em>H</em>° = +47 kJ/mol de CO<sub>2</sub></p>'
       + p("O valor mais próximo de Δ<sub>r</sub><em>H</em>°, em kJ/mol de FeO, para a reação indicada do FeO (sólido) com o CO (gasoso) é"))
X(125, "Biologia", "Genética", "<p>Pares A–T têm duas ligações de hidrogênio, e G–C, três. Desnatura primeiro o segmento com menos pares G–C. Contando: A (GGCCTTCG) tem 6 pares G–C; B (CCTCGACT), 5; C (AATTCCTA), 2; D (TTACGGCG), 5; E (CCTAGGAA), 4. O segmento C é o primeiro. Alternativa <strong>C</strong>.</p>",
  figs(("q125a", "Segmento A: fita GGCCTTCG pareada com CCGGAAGC."), ("q125b", "Segmento B: fita CCTCGACT pareada com GGAGCTGA."), ("q125c", "Segmento C: fita AATTCCTA pareada com TTAAGGAT."),
       ("q125d", "Segmento D: fita TTACGGCG pareada com AATGCCGC."), ("q125e", "Segmento E: fita CCTAGGAA pareada com GGATCCTT.")),
  ["PCR", "ligações de hidrogênio"], enun=p(T(125, 0).replace("in vitro", "<em>in vitro</em>"), T(125, 1)), alts=ALT(1))
X(126, "Química", "Tabela periódica", "<p>Para tirar o xenônio da inércia foi preciso o elemento mais ávido por elétrons: o flúor, o mais eletronegativo da tabela, que consegue atrair elétrons até de um gás nobre. A propriedade é a <strong>eletronegatividade</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["gases nobres", "flúor"], trocas=[("A tabela periódica.", "<em>A tabela periódica</em>.")])
X(127, "Física", "Termologia", "<p>A potência que aquece a água é P = m c ΔT por tempo = (densidade × vazão) × c × ΔT. Para uma mesma vazão, a potência é proporcional à elevação de temperatura. No gráfico, para qualquer vazão, a elevação na curva 1 (morno) é 3/8 da elevação na curva 3 (superquente). Alternativa <strong>D</strong>.</p><p>Comparar vazões diferentes não serve, porque a potência depende do produto vazão × ΔT.</p>",
  figs(("q127", "Gráfico “Elevação de temperatura × Curva vazão”: ΔT (°C) em função da vazão (L/min), de 3 a 9 L/min, com três curvas decrescentes, 1 (morno) embaixo, 2 (quente) no meio e 3 (superquente) em cima, começando perto de 37 °C.")),
  ["potência", "calor específico"], enun=p(T(127, 0)) + "[[fig:1]]" + p(T(127, 5)),
  alts=FR("\\dfrac{1}{3}", "\\dfrac{1}{5}", "\\dfrac{3}{5}", "\\dfrac{3}{8}", "\\dfrac{5}{8}"))
X(128, "Biologia", "Fisiologia humana", "<p>Os cones são as células da retina sensíveis às cores: há cones para o vermelho, o verde e o azul. Sua degeneração vai <strong>comprometer a capacidade de visão em cores</strong>. Alternativa <strong>A</strong>.</p><p>A projeção dos raios, a inversão da imagem e o foco de perto (B, C e D) dependem da córnea e do cristalino; o diâmetro da pupila (E), da íris.</p>",
  tags=["cones", "retina"])
X(129, "Física", "Eletrodinâmica", "<p>Para a corrente não passar de 0,01 A com 10 000 V, a resistência total deve ser de pelo menos 10 000 ÷ 0,01 = 1 000 000 Ω. Como o corpo tem só 1 000 Ω, a resistência interna do gerador deve ser de cerca de 999 000 Ω, isto é, <strong>milhares de vezes maior</strong> que a do corpo. Alternativa <strong>C</strong>.</p>",
  tags=["resistência interna", "cerca elétrica"])
X(130, "Química", "Forças intermoleculares", "<p>A fase estacionária é a água, polar; a móvel, hexano com pouca acetona, é quase apolar. Migra mais devagar a substância que interage mais com a água: a mais polar. Licopeno e carotenos são hidrocarbonetos; a α-criptoxantina tem uma hidroxila; a <strong>capsorubina</strong> tem duas hidroxilas e duas carbonilas, e é a mais polar. Alternativa <strong>D</strong>.</p>",
  figs(("q130", "Estruturas de cinco pigmentos com longas cadeias de duplas ligações alternadas: licopeno (só carbono e hidrogênio, sem anéis), α-caroteno e γ-caroteno (com anéis nas pontas, sem oxigênio), α-criptoxantina (com um anel com OH) e capsorubina (com dois anéis, cada um com OH e um grupo C=O).")),
  ["cromatografia", "polaridade"], enun=p(T(130, 0), T(130, 1)) + "[[fig:1]]" + fonte("RIBEIRO, N. M.; NUNES, C. R. Análise de pigmentos de pimentões por cromatografia em papel. <strong>Química Nova na Escola</strong>, n. 29, ago. 2008 (adaptado).") + p("A substância presente na mistura que migra mais lentamente é o(a)"))
X(131, "Física", "Cinemática", "<p>Motorista atento: freia a 14 m/s; distância de frenagem = 14² ÷ (2 × 5) = 19,6 m.</p><p>Desatento: acelera mais 1 s a 1 m/s². Nesse segundo, percorre 14 × 1 + 0,5 × 1 × 1² = 14,5 m e chega a 15 m/s; depois freia em 15² ÷ (2 × 5) = 22,5 m.</p><p>Diferença: 14,5 + 22,5 − 19,6 = <strong>17,4 m</strong>. Alternativa <strong>E</strong>.</p><p>14,5 m (C) é só o trecho percorrido durante o segundo de atraso.</p>",
  tags=["MUV", "tempo de reação"], trocas=[("1,00 m/s2", "1,00 m/s<sup>2</sup>"), ("5,00 m/s2", "5,00 m/s<sup>2</sup>")])
X(132, "Biologia", "Citologia", "<p>O sal deixa o meio externo muito concentrado. Por osmose, a água sai das células (e dos micro-organismos) para o meio, que fica hipertônico. Sem água, as bactérias não se reproduzem e o alimento se conserva. <strong>A grande concentração de sal no meio extracelular provoca a saída de água de dentro delas</strong>. Alternativa <strong>E</strong>.</p>",
  tags=["osmose", "conservação de alimentos"], alts={**D[132]["alternativas"], "D": "Os íons Na<sup>+</sup> e Cl<sup>−</sup> provenientes da dissociação do sal entram livremente nelas."})
X(133, "Física", "Eletromagnetismo", "<p>A tensão máxima de um gerador é V = N B A ω, proporcional ao número de espiras, ao campo, à área e à frequência. A corrente de curto é V ÷ R, e a resistência do fio cresce com o comprimento. Dobrando o número de espiras, dobram a tensão e o comprimento do fio (e a resistência): a corrente fica igual. Alternativa <strong>A</strong>.</p><p>Dobrar a frequência, o campo ou a área (B, C e D) dobra a tensão sem mudar a resistência, e a corrente dobra.</p>",
  tags=["gerador", "lei de Faraday"],
  enun=p(T(133, 0)) + LISTA(T(133, 1).split(" Ao fazer")[0].replace("diâmetro D", "diâmetro <em>D</em>").replace("N espiras", "<em>N</em> espiras").replace("área A;", "área <em>A</em>;").replace("intensidade B;", "intensidade <em>B</em>;").replace("frequência f.", "frequência <em>f</em>.")) + p("Ao fazer" + T(133, 1).split(" Ao fazer")[1].replace("tensão máxima V", "tensão máxima <em>V</em>").replace("curto-circuito i.", "curto-circuito <em>i</em>."), T(133, 2).replace("máxima V do", "máxima <em>V</em> do").replace("curto i,", "curto <em>i</em>,")))
X(134, "Química", "Reações orgânicas", "<p>No 1-fenil-2-metilprop-1-eno, a dupla liga um carbono com o anel benzênico (e um H) a outro carbono com duas metilas. A ozonólise quebra a dupla: o lado monossubstituído vira aldeído (benzaldeído, C<sub>6</sub>H<sub>5</sub>–CHO), e o lado dissubstituído vira cetona (propanona). Alternativa <strong>A</strong>.</p>",
  figs(("q134a", "Esquema: but-1-eno, com O₃, H₂O e Zn, forma propanal + metanal."), ("q134b", "Estrutura do 1-fenil-2-metilprop-1-eno: um anel benzênico ligado a um carbono de dupla ligação, cujo outro carbono tem duas metilas.")),
  ["ozonólise", "aldeídos e cetonas"], enun=p(T(134, 0).replace("(O3)", "(O<sub>3</sub>)")) + "[[fig:1]]" + p(T(134, 4)) + "[[fig:2]]" + fonte("MARTINO, A. <strong>Química, a ciência global</strong>. Goiânia: Editora W, 2014 (adaptado).") + p(T(134, 8)))
X(135, "Biologia", "Fisiologia humana", "<p>A técnica antiga e rotineira de introduzir células novas num paciente é a <strong>transfusão de sangue</strong>, que repõe hemácias, plaquetas e outras células. Alternativa <strong>E</strong>.</p><p>Na vacina (A) entram antígenos, não células para regenerar tecidos; na hemodiálise (C), o sangue é filtrado e volta ao corpo.</p>",
  tags=["terapia celular", "transfusão"])

completar(Q, R)
