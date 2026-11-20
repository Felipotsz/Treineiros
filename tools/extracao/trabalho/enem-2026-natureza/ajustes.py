# Enem 2026, 2º dia, caderno AMARELO: Ciências da Natureza (questões 91 a 135 do caderno; no site, 1 a 45, com numeroOriginal).
# Texto dos blocos do PDF (tools/enem_rascunho.py com ESPACOS=1); expoentes, índices e cargas refeitos à mão (o PDF perde o sobrescrito).
# Quadros das Q92, Q113, Q133 e Q135 em HTML. Q91 com alternativas-imagem. Gabarito oficial do Inep (caderno amarelo).
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar, tabela
from enem_aj import carregar_enem, enunciado_enem, paragrafos_enem

ID = "enem-2026-natureza"
META = {"id": ID, "banca": "Enem", "ano": 2026, "titulo": "Enem 2026: Ciências da Natureza", "fonte": "Inep", "dataExame": "2026-11-15",
        "duracaoMinutos": 150, "area": "Ciências da Natureza", "caderno": "amarelo", "dia": 2}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2026-dia2-amarelo")
Q = {}
P = lambda n: paragrafos_enem(D[n])
p = lambda *xs: "".join(f"<p>{x}</p>" for x in xs)
ap = lambda *xs: "".join(f'<p class="apoio">{x}</p>' for x in xs)
fonte = lambda x: f'<p class="fonte">{x}</p>'
x10 = lambda m, e: f"{m} × 10<sup>{e}</sup>"


def figs(*pares):
    return [{"arquivo": a, "alt": t} for a, t in pares]


def X(n, materia, assunto, expl, imagens=(), tags=(), enun=None, trocas=(), alts=None):
    h = enun or enunciado_enem(D[n])
    for a, b in trocas:
        if a not in h: print(f"[troca não aplicada] Q{n}: {a[:50]!r} || {h[:220]!r}"); continue
        h = h.replace(a, b)
    Q[n - 90] = {"materia": materia, "assunto": assunto, "area": "Ciências da Natureza", "tags": list(tags), "numeroOriginal": n,
                 "enunciado": h, "alternativas": dict(D[n]["alternativas"], **(alts or {})), "imagens": list(imagens), "explicacao": expl}


X(91, "Física", "Eletrostática", "<p>Pela física clássica, o elétron acelerado irradia energia e descreve uma espiral até o núcleo: a distância <em>r</em> diminui com o tempo. Como a força de Coulomb é proporcional a 1/<em>r</em>², ela cresce, e cada vez mais depressa à medida que o elétron se aproxima do núcleo. O gráfico é uma curva que sobe e se torna cada vez mais íngreme: alternativa <strong>D</strong>.</p><p>Força constante (A) valeria para uma órbita circular estável; as que descem (B e E) supõem o elétron se afastando; e a reta (C) não acompanha o 1/<em>r</em>².</p>",
  figs(("q91-1", "Desenho de uma espiral azul que se fecha, do elétron “e”, na ponta externa, até o núcleo, um ponto preto no centro."),
       ("q91-2", "Gráfico A: força elétrica constante ao longo do tempo (reta horizontal)."),
       ("q91-4", "Gráfico B: força elétrica diminuindo em linha reta com o tempo."),
       ("q91-6", "Gráfico C: força elétrica aumentando em linha reta com o tempo."),
       ("q91-3", "Gráfico D: força elétrica começa baixa e cresce com o tempo, cada vez mais rápido (curva que se torna quase vertical)."),
       ("q91-5", "Gráfico E: força elétrica começa alta e diminui com o tempo, cada vez mais rápido (curva que cai quase na vertical).")),
  tags=["modelo de Rutherford", "lei de Coulomb"], alts={k: f"[[fig:{i}]]" for i, k in enumerate("ABCDE", 2)},
  enun=p(P(91)[0][1]) + "[[fig:1]]" + p(P(91)[2][1]))
X(92, "Física", "Calorimetria", "<p>O aparelho precisa retirar todo o calor dissipado: lâmpadas 10 × 100 = 1 000 W; computadores 20 × 150 = 3 000 W; geladeiras 2 × 500 = 1 000 W; pessoas 20 × 200 = 4 000 W. Total: 9 000 W. Com 1 Btu/h = 0,3 W, são 9 000 ÷ 0,3 = <strong>30 000 Btu/h</strong>, o menor aparelho que dá conta. Alternativa <strong>E</strong>.</p>",
  tags=["potência térmica", "ar-condicionado"],
  enun=p(P(92)[0][1]) + tabela(["Fonte de calor", "Quantidade", "Potência individual (W)"], [["Lâmpada", "10", "100"], ["Computador", "20", "150"], ["Geladeira", "2", "500"], ["Pessoa adulta", "20", "200"]]) + p(P(92)[-1][1]))
X(93, "Química", "Química ambiental", "<p>Orgânicos coletados: 45% de 196 mil t = 88,2 mil t = 88,2 × 10<sup>6</sup> kg por dia. Biogás: 88,2 × 10<sup>6</sup> ÷ 20 = 4,41 × 10<sup>6</sup> m³. Energia: 4,41 × 10<sup>6</sup> × 1,2 ≈ <strong>5,3 × 10<sup>6</sup> kWh</strong> por dia. Alternativa <strong>C</strong>.</p><p>Usar os 211 mil t gerados (em vez dos 196 mil coletados) ou todos os resíduos, e não só os orgânicos, leva às outras alternativas.</p>",
  tags=["biogás", "resíduos sólidos"],
  alts={"A": x10("1,2", 7) + " kWh", "B": x10("7,1", 6) + " kWh", "C": x10("5,3", 6) + " kWh", "D": x10("3,2", 6) + " kWh", "E": x10("2,1", 6) + " kWh"})
X(94, "Física", "Física moderna", "<p>O momento total é nulo antes e depois: a partícula α (massa 4) e o nêutron (massa 1) saem com momentos de mesmo módulo e sentidos opostos. Como <em>E</em> = <em>p</em>²/2<em>m</em>, a energia cinética é inversamente proporcional à massa: o nêutron leva 4 partes e a α, 1 parte dos 20 MeV. Nêutron: 20 × 4/5 = <strong>16 MeV</strong>. Alternativa <strong>E</strong>.</p><p>Dividir igualmente (B) ou na proporção direta das massas (A) ignora a conservação do momento.</p>",
  tags=["fusão nuclear", "conservação do momento"],
  trocas=[("deutério D+ e trítio T +", "deutério D<sup>+</sup> e trítio T<sup>+</sup>"), ("partícula D+", "partícula D<sup>+</sup>"), ("partícula T +", "partícula T<sup>+</sup>"),
          ("<strong>D+ + T + → a + n</strong>", "D<sup>+</sup> + T<sup>+</sup> → α + n"), ("partícula a", "partícula α")])
X(95, "Física", "Eletrodinâmica", "<p>A 800 K, R<sub>S</sub> = 20[1 + 0,002(800 − 300)] = 20 × 2 = 40 Ω. No ramo da esquerda, 40 Ω e R<sub>S</sub> = 40 Ω dividem os 12 V ao meio: V<sub>A</sub> = 6 V. No ramo da direita, 40 Ω em cima e 20 Ω embaixo: V<sub>B</sub> = 12 × 20/60 = 4 V. A tensão entre A e B é 6 − 4 = <strong>2,0 V</strong>. Alternativa <strong>D</strong>.</p>",
  figs(("q95", "Circuito em ponte: uma bateria de 12 V, com o polo negativo aterrado, alimenta dois ramos em paralelo. No ramo da esquerda, um resistor de 40 Ω em cima e o sensor R<sub>S</sub> embaixo, com o ponto A entre eles; no ramo da direita, 40 Ω em cima e 20 Ω embaixo, com o ponto B entre eles.")),
  tags=["ponte de resistores", "termorresistor"], trocas=[("Rs = 20[1 + 0,002(T – 300)]", "R<sub>S</sub> = 20[1 + 0,002(T – 300)]"), ("resistência elétrica Rs varia", "resistência elétrica R<sub>S</sub> varia")])
X(96, "Física", "Ondas", "<p>A onda vai até o avião e volta: percorre 2 × 75 = 150 km. Com 300 000 km/s, o tempo é 150 ÷ 300 000 = <strong>5,0 × 10<sup>−4</sup> s</strong>. Alternativa <strong>E</strong>.</p><p>Esquecer a volta dá 2,5 × 10<sup>−4</sup> s, e inverter a divisão leva às alternativas A e B.</p>",
  figs(("q96", "Ilustração: uma torre de controle de aeroporto emite ondas em direção a um avião no céu, destacado num círculo vermelho, e recebe as ondas refletidas por ele.")),
  tags=["radar", "velocidade da luz"], alts={"A": x10("2,0", 3) + " s.", "B": x10("4,0", 0) + " s.", "C": x10("5,0", "−1") + " s.", "D": x10("1,5", "−3") + " s.", "E": x10("5,0", "−4") + " s."})
X(97, "Biologia", "Ecologia", "<p>As bactérias simbióticas dos nódulos (rizóbios, como as do gênero <em>Bradyrhizobium</em>) fazem a fixação biológica do nitrogênio: <strong>convertem o N<sub>2</sub> atmosférico em compostos assimiláveis pelas plantas</strong>, como a amônia. A planta precisa de menos adubo nitrogenado. Alternativa <strong>C</strong>.</p><p>Decompor matéria orgânica (D e E) é papel de decompositores; nitritos (A) são etapa da nitrificação; e as bactérias não “capturam íons” do solo (B).</p>",
  tags=["fixação de nitrogênio", "Mariangela Hungria"])
X(98, "Química", "Separação de misturas", "<p>Aquecer as folhas em água para tirar o princípio ativo é uma <strong>extração</strong> (infusão); passar por funil com algodão é <strong>filtração</strong>; e separar por rotação intensa é <strong>centrifugação</strong>. Alternativa <strong>B</strong>.</p>",
  tags=["extração", "centrifugação"])
X(99, "Física", "Eletrodinâmica", "<p>Pela fiação, as lâmpadas A e B estão em paralelo entre si, e esse conjunto está em série com C, D e as baterias. O amperímetro de i<sub>2</sub> mede a corrente total do circuito; o de i<sub>1</sub> mede só a corrente que passa pela lâmpada A. As duas leituras só ficam iguais quando toda a corrente passa por A, isto é, quando <strong>a lâmpada B está queimada</strong>. Alternativa <strong>C</strong>.</p><p>Com todas ligadas (A), a corrente se divide entre A e B, e i<sub>1</sub> é metade de i<sub>2</sub>; com A queimada (B), i<sub>1</sub> é zero; e com C ou D queimada (D e E), o circuito se abre e as duas correntes zeram.</p>",
  figs(("q99", "Maquete do circuito com duas baterias em série. As lâmpadas A e B, nas paredes, estão ligadas em paralelo: um fio liga as duas por cima e outro por baixo, e o amperímetro da corrente i<sub>1</sub> fica no fio de baixo, só no caminho da lâmpada A. As lâmpadas C e D, no teto, estão em série entre si e com o conjunto A–B; o amperímetro da corrente i<sub>2</sub> fica no fio que liga a lâmpada D às baterias.")),
  tags=["circuitos", "amperímetro"])
X(100, "Biologia", "Evolução", "<p>A pele grossa e queratinizada é quase impermeável: impede a perda de água pelo corpo, um problema central para viver fora da água. Contribuiu para a <strong>diminuição do risco de ressecamento</strong>. Alternativa <strong>C</strong>.</p><p>A queratina atrapalha as trocas gasosas pela pele (D); os répteis são ectotérmicos (B); e locomoção e excreção (A e E) dependem de outras adaptações (membros e ácido úrico).</p>",
  tags=["répteis", "conquista do ambiente terrestre"])
X(101, "Química", "Química orgânica", "<p>As linamarases quebram a linamarina em glicose e acetona-cianidrina, que se decompõe em acetona e HCN. O ácido cianídrico é <strong>volátil e solúvel em água</strong>: na fervura, ele evapora ou fica na água descartada. Alternativa <strong>C</strong>.</p><p>O processo produz HCN, que é tóxico, e não compostos inofensivos (A); a linamarina é hidrolisada pela enzima, não evaporada (D); o aquecimento não é o catalisador (E); e o HCN não age sobre a enzima (B).</p>",
  figs(("q101", "Esquema reacional. (1) Linamarina + H<sub>2</sub>O, com linamarases armazenadas nos tecidos, aquecimento e pH 5,5, produz glicose + acetona-cianidrina. (2) Acetona-cianidrina, em equilíbrio, produz HCN (ácido cianídrico) + acetona.")),
  tags=["mandioca", "ácido cianídrico"], trocas=[('<p class="apoio">A química dos povos indígenas da América do Sul A mandioca,', '<p class="apoio"><strong>A química dos povos indígenas da América do Sul</strong></p><p class="apoio">A mandioca,'), ("Data M ining", "Data Mining")])
X(102, "Química", "Transformações químicas", "<p>Espalhamento, evaporação, emulsificação, dispersão, dissolução e sedimentação mudam o estado, a forma ou a distribuição do petróleo, sem criar substâncias novas. Na <strong>oxidação (III)</strong>, componentes do óleo reagem com o oxigênio e viram outras substâncias: é a transformação química. Alternativa <strong>C</strong>.</p><p>A biodegradação também é química, mas não tem número na figura.</p>",
  figs(("q102", "Ilustração de uma mancha de petróleo no mar, com os processos: espalhamento (I) para os lados, evaporação (II) e oxidação (III) para o ar, emulsificação e biodegradação na mancha, dispersão (IV) na água, dissolução e sedimentação (V) para o fundo.")),
  tags=["petróleo", "intemperismo"])
X(103, "Biologia", "Ecologia", "<p>Um bom bioindicador de metais pesados na água vive fixo no local e acumula os poluentes do ambiente. O <strong>sururu, molusco filtrador</strong>, filtra grandes volumes de água e concentra os metais em seus tecidos, além de ser consumido pela população. Alternativa <strong>C</strong>.</p><p>Peixes, aves e jacarés (A, B e E) se deslocam, e o caranguejo que come folhas e insetos (D) não filtra a água.</p>",
  tags=["bioindicadores", "manguezal"])
X(104, "Química", "Estados físicos", "<p>No diagrama, o tracejado de A para B fica abaixo do ponto triplo: a pressão é tão baixa que não existe líquido. A água passa direto do sólido para o gasoso: <strong>sublimação</strong>. Alternativa <strong>C</strong>.</p>",
  figs(("q104", "Diagrama de fases da água: pressão p (atm) no eixo vertical e temperatura T (°C) no horizontal. Três curvas vermelhas se encontram no ponto triplo. Abaixo dele, uma linha tracejada horizontal vai do ponto A, à esquerda (região do sólido), ao ponto B, à direita (região do gás), cruzando só a curva de sublimação.")),
  tags=["diagrama de fases"])
X(105, "Biologia", "Evolução", "<p>A seleção natural não cria as características: ela “julga” as que já existem. As possibilidades trazidas ao “júri” são as diferenças entre os indivíduos, isto é, a <strong>variação dos indivíduos</strong>, que vem de mutações e recombinação. Alternativa <strong>D</strong>.</p><p>Caracteres adquiridos (B) não são herdados; fluxo gênico (A) é uma das fontes de variação, não a variação em si; e hábitats (C) são o ambiente que seleciona.</p>",
  tags=["seleção natural", "variabilidade"])
X(106, "Química", "Oxirredução", "<p>O nitrogênio tem número de oxidação −3 no NH<sub>3</sub> (atmosfera) e no NH<sub>4</sub><sup>+</sup> (litosfera), o menor possível para ele. Nas outras espécies: N<sub>2</sub> 0, N<sub>2</sub>O +1, NO<sub>2</sub> +4, NO<sub>2</sub><sup>−</sup> +3, NO<sub>3</sub><sup>−</sup> +5. Alternativa <strong>A</strong>.</p>",
  figs(("q106", "Figura dividida em atmosfera (azul) e litosfera (laranja). Na atmosfera: N<sub>2</sub>O, NO<sub>2</sub>, N<sub>2</sub> e NH<sub>3</sub>. Na litosfera: NH<sub>4</sub><sup>+</sup>, NO<sub>2</sub><sup>−</sup> e NO<sub>3</sub><sup>−</sup>.")),
  tags=["ciclo do nitrogênio", "número de oxidação"], enun=p(P(106)[0][1]) + "[[fig:1]]" + fonte(P(106)[2][1]) + p(P(106)[3][1]),
  alts={"A": "NH<sub>3</sub> e NH<sub>4</sub><sup>+</sup>", "B": "NO<sub>2</sub> e NO<sub>2</sub><sup>−</sup>", "C": "N<sub>2</sub>O e NO<sub>3</sub><sup>−</sup>", "D": "NH<sub>3</sub> e NO<sub>3</sub><sup>−</sup>", "E": "NO<sub>2</sub> e NH<sub>4</sub><sup>+</sup>"})
X(107, "Química", "Soluções", "<p>Um litro de água tem 1 000 g. A massa molar da água é 2 × 1 + 16 = 18 g/mol: 1 000 ÷ 18 ≈ <strong>56 mol/L</strong>, o mesmo em qualquer volume, porque a concentração é intensiva. Alternativa <strong>E</strong>.</p><p>18 mol/L (C) confunde com a massa molar, e 0,055 (A) inverte a conta.</p>",
  tags=["concentração molar", "propriedades intensivas"])
X(108, "Química", "Forças intermoleculares", "<p>O texto diz que, “inicialmente”, as moléculas se agrupam por interações apolares. Na molécula, a parte apolar é a longa cadeia de carbonos da região I: o início é feito por <strong>interações de van der Waals da parte alquílica hidrofóbica da região I</strong>. Depois, os grupos polares e iônicos interagem com o cálcio e as células. Alternativa <strong>C</strong>.</p><p>A região II tem grupos polares (A e E); a ligação com o cálcio é etapa posterior (B); e o agregado não se forma por ligações covalentes (D).</p>",
  figs(("q108", "Fórmula estrutural de uma molécula longa dividida em três regiões: I, uma cadeia de carbonos em zigue-zague, sem grupos polares; II, uma sequência de ligações amida com grupos SH e um grupo fosfato; III, a ponta com grupos amina, guanidina e ácido carboxílico.")),
  tags=["nanotecnologia", "interações apolares"])
X(109, "Química", "Química ambiental", "<p>O CO<sub>2</sub> liberado na queima do etanol é absorvido pela cana na fotossíntese durante o crescimento da safra seguinte: <strong>as emissões são incorporadas ao ciclo do carbono</strong>, e o balanço é bem menor que o dos combustíveis fósseis. Alternativa <strong>E</strong>.</p><p>A queima produz CO<sub>2</sub>, um gás de efeito estufa (C); a cana esgota nutrientes (A); queimar a palha empobrece o solo (B); e a cana não é nativa do Brasil, e a monocultura afeta a biodiversidade (D).</p>",
  tags=["etanol", "ciclo do carbono"], trocas=[('<p class="apoio">Etanol: crise e oportunidades No cenário', '<p class="apoio"><strong>Etanol: crise e oportunidades</strong></p><p class="apoio">No cenário')])
X(110, "Química", "Química orgânica", "<p>A lavagem com água retira o que é solúvel nela: o álcool (I), a glicerina (III) e o sabão (IV), que têm grupos polares ou iônicos. O biodiesel (V, o éster) é o próprio produto e fica, e entre as impurezas resiste à lavagem o <strong>monoglicerídeo (II)</strong>: a longa cadeia apolar o torna pouco solúvel em água. Alternativa <strong>B</strong>.</p>",
  figs(("q110", "Cinco fórmulas estruturais. I: etanol. II: monoglicerídeo, uma longa cadeia de carbonos ligada por éster a um resto de glicerol com dois grupos OH. III: glicerol, três carbonos com três OH. IV: sal de ácido graxo (sabão), longa cadeia terminada em COONa. V: éster etílico de cadeia longa (biodiesel).")),
  tags=["biodiesel", "solubilidade"])
X(111, "Física", "Energia", "<p>Das fontes citadas, só a <strong>nuclear</strong> vem de um recurso não renovável (o urânio) e funciona dia e noite, faça sol, chova ou venta. Alternativa <strong>A</strong>.</p><p>Hidrelétrica, solar, biomassa e eólica (B a E) são renováveis, e as três primeiras dependem das chuvas, do sol ou da safra, assim como a eólica depende do vento.</p>",
  figs(("q111", "Cinco ilustrações lado a lado: energia nuclear (usina com torres de resfriamento), hidrelétrica (barragem com água), solar (painéis sob o sol), termelétrica (usina e caminhão com biomassa) e eólica (aerogeradores).")),
  tags=["fontes de energia"])
X(112, "Biologia", "Biotecnologia", "<p>O milho com o gene Bt produz uma proteína tóxica para as lagartas que o comem. Com menos perdas pela praga, a lavoura <strong>aumenta a produtividade</strong>. Alternativa <strong>B</strong>.</p><p>O transgênico é o milho, não as lagartas (C); a técnica reduz o uso de praguicidas (D); e não tem relação com replantio ou adubação (A e E).</p>",
  figs(("q112", "Ilustração: a bactéria <em>Bacillus thuringiensis</em> (Bt) fornece um gene, representado por uma fita de DNA, inserido na lavoura. À esquerda, uma lagarta saudável come o milho sem o gene Bt; à direita, a lagarta morre junto ao milho com o gene Bt.")),
  tags=["transgênicos", "milho Bt"])
NOTAS = tabela(["Oitava", "Dó", "Ré", "Mi", "Fá", "Sol", "Lá", "Si"],
               [["3ª", "130", "147", "165", "175", "196", "220", "248"], ["4ª", "260", "294", "330", "349", "392", "440", "495"],
                ["5ª", "520", "587", "660", "698", "784", "880", "990"], ["6ª", "1 040", "1 174", "1 320", "1 397", "1 568", "1 760", "1 980"]])
X(113, "Física", "Ondas", "<p>A frequência é inversamente proporcional ao comprimento: <em>f</em> = 660 × 60/45 = 880 Hz. No quadro, 880 Hz é o <strong>Lá</strong> da 5ª oitava. Alternativa <strong>D</strong>.</p><p>Fazer a conta direta (660 × 45/60 = 495 Hz) daria Si (E).</p>",
  figs(("q113", "Desenho de um violão: o comprimento vibrante total L<sub>T</sub> = 60 cm vai da pestana ao cavalete; uma corda pressionada num traste tem parte oscilante L = 45 cm, medida até o cavalete.")),
  tags=["frequência", "cordas vibrantes"],
  enun=p(P(113)[0][1]) + "[[fig:1]]" + '<p class="apoio"><strong>Frequência das notas musicais, em hertz, no sistema temperado</strong></p>' + NOTAS + fonte(P(113)[4][1]) + p(P(113)[5][1]))
X(114, "Física", "Energia", "<p>O protótipo gasta 1 kWh = 3,6 × 10<sup>6</sup> J a cada 10 km = 10<sup>4</sup> m com quatro pessoas: 3,6 × 10<sup>6</sup> ÷ (10<sup>4</sup> × 4) = 90 J por metro passageiro. No gráfico, só o velomóvel (18) e a bicicleta (60) gastam menos: <strong>2</strong> meios de transporte. Alternativa <strong>B</strong>.</p><p>Esquecer de dividir pelos quatro passageiros (360 J) levaria a 5 meios.</p>",
  figs(("q114", "Gráfico de barras “Gasto energético dos transportes”, em joule por metro passageiro (menor = mais eficiente): velomóvel 18; bicicleta 60; pedonalidade 132; ferrovia eletrificada 200; bonde 432; carro elétrico (marca 1) 517; carro elétrico (marca 2) 560; ônibus 920; ferrovia não eletrificada 1 650; metropolitano de Londres 1 690; motociclo 1 730; carro com motor de combustão 1 750; aeronave 2 940.")),
  tags=["eficiência energética", "transportes"], trocas=[('<p class="apoio"><strong>Gasto energético dos transportes</strong></p>', '<p class="apoio"><strong>Gasto energético dos transportes</strong></p>')])
X(115, "Biologia", "Genética", "<p>Pela via, o gene A (dominante) é preciso para sair do branco, e o gene B (dominante) leva do rosa ao vermelho. Uma flor rosa tem o pigmento rosa, mas não o vermelho: precisa de pelo menos um A e de bb. O genótipo <strong>Aabb</strong> serve. Alternativa <strong>D</strong>.</p><p>AaBb e AABB (A e C) são vermelhas; aabb e aaBb (B e E) são brancas, porque aa bloqueia tudo.</p>",
  figs(("q115", "Esquema da via metabólica: precursor branco → pigmento rosa → pigmento vermelho. O gene A produz a enzima X, que faz a primeira etapa; o gene B produz a enzima Y, que faz a segunda.")),
  tags=["epistasia", "via metabólica"])
X(116, "Química", "Química ambiental", "<p>Pilhas e baterias descartadas no lixo comum liberam metais pesados (mercúrio, cádmio, chumbo) que a chuva leva para dentro do solo até o <strong>lençol freático</strong>. Alternativa <strong>C</strong>.</p><p>Combustíveis fósseis, enxofre e queimadas (A, B e E) poluem sobretudo o ar, e o derramamento em alto-mar (D) atinge o oceano.</p>",
  tags=["pilhas", "águas subterrâneas"])
X(117, "Química", "Estequiometria", "<p>5,2 g de Cr<sup>3+</sup> ÷ 52 g/mol = 0,10 mol de Cr. Cada Cr<sub>2</sub>O<sub>3</sub> tem 2 Cr: 0,05 mol × 152 g/mol = 7,6 g. Com rendimento de 90%: 7,6 × 0,9 ≈ <strong>6,8 g</strong>. Alternativa <strong>B</strong>.</p><p>7,6 g (C) é o rendimento teórico, sem os 90%.</p>",
  tags=["rendimento", "cromo"],
  trocas=[("5,2 g de Cr3+", "5,2 g de Cr<sup>3+</sup>"),
          ("<p><strong>Cr3+(aq) + 3 NaOH (aq) →Cr(OH)3 (s) + 3 Na+(aq) 2 Cr(OH)3 (s) →Cr2O3 (s) + 3 H2O (g)</strong></p>",
           "<p>Cr<sup>3+</sup>(aq) + 3 NaOH(aq) → Cr(OH)<sub>3</sub>(s) + 3 Na<sup>+</sup>(aq)<br>2 Cr(OH)<sub>3</sub>(s) → Cr<sub>2</sub>O<sub>3</sub>(s) + 3 H<sub>2</sub>O(g)</p>"),
          ("(g⋅mol-1)", "(g⋅mol<sup>−1</sup>)"), ("composto Cr2O3", "composto Cr<sub>2</sub>O<sub>3</sub>")])
X(118, "Física", "Hidrostática", "<p>No nível da linha de separação, a pressão é a mesma nos dois ramos: ρ<sub>A</sub>·h<sub>A</sub> = ρ<sub>B</sub>·h<sub>B</sub>. O líquido B não muda de volume e o tubo tem seção constante, então h<sub>B</sub> continua igual; pela equação, h<sub>A</sub> também. O líquido A a mais só desloca a interface: <strong>h<sub>A2</sub> = h<sub>A1</sub> e h<sub>B2</sub> = h<sub>B1</sub></strong>. Alternativa <strong>A</strong>.</p>",
  figs(("q118", "Tubo em U com dois líquidos imiscíveis: A (azul) ocupa a base e o ramo esquerdo; B (amarelo), menos denso, fica sobre A no ramo direito. As alturas h<sub>A1</sub> e h<sub>B1</sub> são medidas da superfície de cada líquido até o nível da separação entre eles. Um copo despeja mais líquido A no ramo esquerdo.")),
  tags=["vasos comunicantes", "pressão hidrostática"],
  trocas=[("hA1 e hB1", "h<sub>A1</sub> e h<sub>B1</sub>"), ("hA2 e hB2", "h<sub>A2</sub> e h<sub>B2</sub>")],
  alts={"A": "h<sub>A2</sub> = h<sub>A1</sub> e h<sub>B2</sub> = h<sub>B1</sub>.", "B": "h<sub>A2</sub> &gt; h<sub>A1</sub> e h<sub>B2</sub> = h<sub>B1</sub>.", "C": "h<sub>A2</sub> &gt; h<sub>A1</sub> e h<sub>B2</sub> &gt; h<sub>B1</sub>.",
        "D": "h<sub>A2</sub> &lt; h<sub>A1</sub> e h<sub>B2</sub> &gt; h<sub>B1</sub>.", "E": "h<sub>A2</sub> = h<sub>A1</sub> e h<sub>B2</sub> &gt; h<sub>B1</sub>."})
X(119, "Biologia", "Biotecnologia", "<p>O algodoeiro faz celulose com glicose que ele mesmo produz na fotossíntese, a partir do CO<sub>2</sub> do ar. A bactéria é heterotrófica: precisa receber açúcares no meio de cultura e <strong>utiliza carboidratos como fonte primária de carbono</strong>. Alternativa <strong>D</strong>.</p><p>Sequestrar carbono e liberar O<sub>2</sub> (A e B) é coisa da planta; polissacarídeos se formam por desidratação, não hidratação (C); e síntese é anabolismo, não catabolismo (E).</p>",
  tags=["celulose bacteriana", "nutrição"], alts={"B": "acelera a liberação de O<sub>2</sub> pela fotólise da água."})
X(120, "Biologia", "Fisiologia vegetal", "<p>A gema apical produz auxina, que inibe as gemas laterais (dominância apical). Sem ela, as gemas laterais se desenvolvem, e em sete dias a planta estará <strong>com brotações laterais</strong>. Alternativa <strong>C</strong>.</p><p>A planta não morre nem murcha (A e B), uma nova gema apical não se forma (D), e ela continua crescendo pelos ramos laterais (E).</p>",
  tags=["dominância apical", "auxina"])
X(121, "Física", "Óptica", "<p>Intensidade a 1 m: 6 W ÷ (4 × 3 × 1²) = 0,5 W/m². Na folha (4 cm² = 4 × 10<sup>−4</sup> m²) chegam 0,5 × 4 × 10<sup>−4</sup> = 2,0 × 10<sup>−4</sup> W. Em 650 nm, o gráfico mostra cerca de 60% de absorção: 0,6 × 2,0 × 10<sup>−4</sup> = <strong>1,2 × 10<sup>−4</sup> J</strong> por segundo. Alternativa <strong>E</strong>.</p><p>2,0 × 10<sup>−4</sup> J (C) é a energia que chega à folha, sem descontar a parte que não é absorvida.</p>",
  figs(("q121", "Gráfico de absorção (%) por comprimento de onda (nm), de 400 a 750 nm: cerca de 37% em 400 nm, um pico de quase 90% perto de 480 nm, quase zero entre 550 e 600 nm e outro pico de cerca de 60% em 650 nm, caindo depois.")),
  tags=["intensidade luminosa", "fotossíntese"], trocas=[("4,0 cm2", "4,0 cm²")],
  alts={"A": x10("3,8", "−4") + " J", "B": x10("4,8", "−4") + " J", "C": x10("2,0", "−4") + " J", "D": x10("1,8", "−4") + " J", "E": x10("1,2", "−4") + " J"})
X(122, "Biologia", "Biotecnologia", "<p>Todo o material genético nuclear do clone vem do núcleo diploide da célula somática da <strong>ovelha B</strong>; a ovelha A doa só o óvulo sem núcleo, e a C apenas gesta. Alelos recessivos em homozigose estão no núcleo: vêm de B. Alternativa <strong>B</strong>.</p><p>A contribui só com DNA mitocondrial (A, D e E), e a barriga de aluguel não passa genes (C).</p>",
  tags=["clonagem", "transferência nuclear"])
X(123, "Química", "Propriedades da matéria", "<p>Água no leite baixa a densidade, que é um dos testes de qualidade. O amido dissolvido ou disperso aumenta a massa por volume e compensa essa queda: o objetivo é mascarar o <strong>teste de densidade</strong>. Alternativa <strong>A</strong>.</p><p>O amido é um carboidrato, não lipídeo (B), não é básico (C), antimicrobiano (D) ou antioxidante (E).</p>",
  tags=["adulteração de alimentos", "densidade"])
X(124, "Biologia", "Ecologia", "<p>As comunidades continuam pescando o pirarucu, mas com regras: só num período, respeitando o defeso da reprodução e com acompanhamento técnico. A população cresceu 620% e os peixes ficaram maiores. É <strong>extrativismo sustentável</strong>, o manejo de um recurso natural sem esgotá-lo. Alternativa <strong>A</strong>.</p><p>Não há criação de ambientes, seleção artificial, eliminação de predadores ou cativeiro (B a E).</p>",
  figs(("q124", "Fotografia: quatro homens carregam na mata, sobre uma maca de madeira apoiada nos ombros, um pirarucu enorme, de escamas avermelhadas, quase do tamanho da maca.")),
  tags=["pirarucu", "manejo sustentável"], trocas=[('<p class="apoio">Estratégia de conservação recupera estoque natural de peixes na região do Médio Solimões</p>', '<p class="apoio"><strong>Estratégia de conservação recupera estoque natural de peixes na região do Médio Solimões</strong></p>')])
X(125, "Biologia", "Ecologia", "<p>Para saber o que se perdeu com o alagamento e manejar o ambiente depois, é preciso conhecer o que existia: os estudos prévios servem para <strong>monitorar a biodiversidade local</strong>, sobretudo as espécies endêmicas. Alternativa <strong>B</strong>.</p><p>Potabilidade (A) não trata do impacto sobre a fauna e a flora; introduzir espécies exóticas (C) ou lacustres (D) e forçar a saída dos animais (E) agravaria o desequilíbrio.</p>",
  tags=["hidrelétricas", "impacto ambiental"])
X(126, "Biologia", "Saúde e doenças", "<p>A água parada entre as folhas da bromélia é onde o <em>Aedes aegypti</em> põe os ovos e onde as larvas se desenvolvem. Eliminar o criadouro reduz a população do mosquito. Alternativa <strong>C</strong>.</p><p>Abrigo, acasalamento e alimentação dos adultos (A, B e D) não dependem da bromélia, e o vírus passa entre pessoas pelo mosquito, não de mosquito para mosquito pela água (E).</p>",
  tags=["dengue", "Aedes aegypti"])
X(127, "Biologia", "Imunologia", "<p>Na figura, a célula 1, um linfócito B com anticorpos na superfície, reconhece a bactéria e é ativada; a célula 2 solta muitos anticorpos (os “Y”), que atingem as bactérias. A célula que produz anticorpos é o <strong>plasmócito</strong>. Alternativa <strong>E</strong>.</p><p>Basófilos liberam histamina (A); linfócitos T auxiliares e citotóxicos não produzem anticorpos (B e D); e macrófagos fagocitam (C).</p>",
  figs(("q127", "Ilustração em fundo rosa: a célula 1, redonda e azul, com anticorpos em Y na superfície, encontra bactérias; uma seta “Ativação” leva à célula 2, maior, que solta muitos anticorpos em Y; os anticorpos grudam nas bactérias, e uma delas diz “Fui atingida. Fujam!”.")),
  tags=["resposta imune secundária", "anticorpos"])
X(128, "Física", "Óptica", "<p>As gotículas da neblina espalham a luz dos faróis em todas as direções (espalhamento ou dispersão): parte volta para o motorista e forma um véu claro, e pouca luz chega à pista e volta. A visibilidade cai pela <strong>dispersão da luz pelas gotículas suspensas</strong>. Alternativa <strong>A</strong>.</p><p>Polarização (B) não reduz a visibilidade desse modo; a condensação no farol (C) e a potência da lâmpada (E) não mudam com a neblina; e a água não se dissolve no ar (D).</p>",
  tags=["neblina", "espalhamento da luz"])
X(129, "Química", "Funções orgânicas", "<p>O grupo 1 é o carbono ligado ao anel, com dupla ligação com O e um H: <strong>aldeído</strong>. O grupo 2 é um O entre o anel e um CH<sub>3</sub>: <strong>éter</strong> (metoxila). O grupo 3 é um OH ligado direto ao anel aromático: <strong>fenol</strong>. Alternativa <strong>A</strong>.</p><p>Cetona exigiria a carbonila entre dois carbonos; éster, um O ligado à carbonila; álcool, o OH em carbono saturado.</p>",
  figs(("q129", "Modelo de esferas da vanilina: carbonos cinza, oxigênios vermelhos e hidrogênios brancos. Num anel aromático estão ligados: o grupo 1, um carbono com dupla ligação a um oxigênio e um hidrogênio; o grupo 2, um oxigênio ligado a um carbono com três hidrogênios; e o grupo 3, um oxigênio com um hidrogênio.")),
  tags=["vanilina"], trocas=[("A vanilina, C8H8O3,", "A vanilina, C<sub>8</sub>H<sub>8</sub>O<sub>3</sub>,")])
X(130, "Física", "Hidrodinâmica", "<p>Ao tapar parte da saída com o polegar, a área por onde a água passa diminui. Como a vazão da mangueira continua praticamente a mesma (<em>Q</em> = <em>A</em>·<em>v</em>), a <strong>velocidade da água lançada</strong> aumenta, e o jato vai mais longe. Alternativa <strong>A</strong>.</p><p>Densidade e massa (B e D) não mudam; o volume por segundo, isto é, a vazão (C e E), não aumenta.</p>",
  tags=["equação da continuidade"])
X(131, "Química", "Eletroquímica", "<p>Na célula, o H<sub>2</sub> perde elétrons e vira H<sup>+</sup>, que atravessa a membrana; do outro lado, o O<sub>2</sub> recebe os elétrons e se junta ao H<sup>+</sup> formando água. Somando as semirreações, a equação global é <strong>2 H<sub>2</sub> + O<sub>2</sub> → 2 H<sub>2</sub>O</strong>. Alternativa <strong>E</strong>.</p><p>As outras não se balanceiam ou deixam íons e elétrons sobrando, que numa reação global se cancelam.</p>",
  figs(("q131", "Ilustração de uma célula a combustível: um cilindro de H<sub>2</sub> à esquerda e um de O<sub>2</sub> à direita alimentam uma caixa dividida por uma membrana; íons H<sup>+</sup> atravessam a membrana; elétrons (e<sup>−</sup>) passam por um fio por cima e acendem uma lâmpada; sai água pela base.")),
  tags=["célula a combustível"],
  alts={"A": "H<sub>2</sub>O → H<sup>+</sup> + OH<sup>−</sup>", "B": "H<sub>2</sub> + 2 O<sub>2</sub> → 2 H<sup>+</sup> + 4 O<sup>2−</sup>", "C": "2 H<sub>2</sub>O → O<sub>2</sub> + 2 H<sup>+</sup> + H<sub>2</sub> + 2 e<sup>−</sup>",
        "D": "6 H<sup>+</sup> + O<sub>2</sub> → 2 H<sub>2</sub>O + H<sub>2</sub>", "E": "2 H<sub>2</sub> + O<sub>2</sub> → 2 H<sub>2</sub>O"})
X(132, "Biologia", "Reprodução", "<p>Os dois embriões vieram de fecundações diferentes, de óvulos e espermatozoides diferentes: os gêmeos são <strong>dizigóticos</strong>, e cada um pode ser de qualquer sexo, <strong>do mesmo sexo ou de sexos diferentes</strong>. Alternativa <strong>D</strong>.</p><p>Monozigóticos (B e E) vêm de um único zigoto que se divide; e nada obriga gêmeos fraternos a terem o mesmo sexo ou sexos diferentes (A e C).</p>",
  tags=["gêmeos", "fertilização in vitro"])
X(133, "Física", "Energia", "<p>Em uso: 4 h × 158 W = 632 Wh. Em espera: 20 h × 1 W = 20 Wh. Total: 652 Wh. A espera representa 20 ÷ 652 ≈ <strong>3,0%</strong>. Alternativa <strong>D</strong>.</p><p>Dividir 1 W por 158 W (0,6%, B) compara potências, não energias.</p>",
  tags=["consumo de energia", "modo de espera"],
  enun=p(P(133)[0][1]) + '<div class="tabela-rola"><table><tbody><tr><th scope="row">Alimentação</th><td colspan="2">110-220 V e 50-60 Hz</td></tr><tr><th scope="rowgroup" rowspan="2">Potência</th><td>Média em uso</td><td>158 W</td></tr><tr><td>Em espera</td><td>1 W</td></tr></tbody></table></div>' + p(P(133)[-1][1]))
X(134, "Biologia", "Metabolismo energético", "<p>Se o treino em altitude der certo, os músculos passam a obter mais energia pela respiração aeróbica e menos pela anaeróbica, que forma lactato. No teste, o sangue deve mostrar <strong>redução nos níveis de lactato</strong>. Alternativa <strong>C</strong>.</p><p>A altitude aumenta o número de hemácias, não reduz (D); o piruvato é levado às mitocôndrias, sem se acumular (E); e glicemia e proteínas (A e B) não medem esse efeito.</p>",
  tags=["respiração celular", "treino em altitude"])
TAB135 = tabela(["Combustível", "Equação da reação de combustão", "Entalpia de reação (kJ mol<sup>−1</sup>)"],
                [["Etanol", "C<sub>2</sub>H<sub>6</sub>O + 3 O<sub>2</sub> → 2 CO<sub>2</sub> + 3 H<sub>2</sub>O", "−1 368"],
                 ["Metano", "CH<sub>4</sub> + 2 O<sub>2</sub> → CO<sub>2</sub> + 2 H<sub>2</sub>O", "−890"],
                 ["Metanol", "CH<sub>4</sub>O + <sup>3</sup>⁄<sub>2</sub> O<sub>2</sub> → CO<sub>2</sub> + 2 H<sub>2</sub>O", "−726"],
                 ["Acetileno (etino)", "C<sub>2</sub>H<sub>2</sub> + <sup>5</sup>⁄<sub>2</sub> O<sub>2</sub> → 2 CO<sub>2</sub> + H<sub>2</sub>O", "−1 301"],
                 ["Carvão (antracito)", "C + O<sub>2</sub> → CO<sub>2</sub>", "−355"]])
X(135, "Química", "Termoquímica", "<p>Divide-se a energia de cada combustão pelo número de mols de carbono queimados (= mols de CO<sub>2</sub>): etanol 1 368/2 = 684 kJ; <strong>metano 890 kJ</strong>; metanol 726 kJ; acetileno 1 301/2 ≈ 650 kJ; carvão 355 kJ. O mais eficiente é o metano. Alternativa <strong>B</strong>.</p><p>Olhar só a entalpia total levaria ao etanol (A), que tem dois carbonos.</p>",
  tags=["entalpia de combustão", "combustíveis"],
  enun=p(P(135)[0][1].replace("CO, NOx e SOx", "CO, NO<sub>x</sub> e SO<sub>x</sub>")) + TAB135 + fonte(P(135)[4][1]) + p(P(135)[5][1]),
  alts={"E": "Carvão (antracito)."})

completar(Q, R)
