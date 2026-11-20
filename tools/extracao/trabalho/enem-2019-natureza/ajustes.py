# Enem 2019, 2º dia, caderno azul: Ciências da Natureza (questões 91 a 135; no site, 1 a 45).
# Texto legível (sem DECOD). Quadros das Q91, 96, 112, 117 e 129 em tabela HTML; equações das Q95 e 103 em HTML.
# Sem anuladas nesta área.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, paragrafos_enem

ID = "enem-2019-natureza"
META = {"id": ID, "banca": "Enem", "ano": 2019, "titulo": "Enem 2019: Ciências da Natureza", "fonte": "Inep", "dataExame": "2019-11-10",
        "duracaoMinutos": 150, "area": "Ciências da Natureza", "caderno": "azul", "dia": 2}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2019-dia2-azul")
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

X(91, "Química", "Eletroquímica", "<p>Para liberar H<sub>2</sub>, a água precisa ser reduzida (E° = −0,83 V). Isso só acontece se outra espécie for oxidada, e ela precisa ter potencial de redução menor que o da água. Na tabela, o único é o do alumínio (−2,33 V): 2 Al + 2 OH<sup>−</sup> + 6 H<sub>2</sub>O → 2 Al(OH)<sub>4</sub><sup>−</sup> + 3 H<sub>2</sub>, reação que ainda libera calor. A espécie é o <strong>Al</strong>. Alternativa <strong>A</strong>.</p><p>Co, Pb e os hidróxidos (B, C, D e E) têm potencial maior que o da água e não a reduziriam.</p>",
  tags=["potencial de redução", "desentupidor"],
  enun=p(T(91, 0).replace("(E )", "(<em>E</em>°)").replace("(NaOH)", "(NaOH)"))
       + tabela(["Semirreação de redução", "E° (V)"], [["2 H<sub>2</sub>O + 2 e<sup>−</sup> → H<sub>2</sub> + 2 OH<sup>−</sup>", "−0,83"], ["Co(OH)<sub>2</sub> + 2 e<sup>−</sup> → Co + 2 OH<sup>−</sup>", "−0,73"],
                                                     ["Cu(OH)<sub>2</sub> + 2 e<sup>−</sup> → Cu + 2 OH<sup>−</sup>", "−0,22"], ["PbO + H<sub>2</sub>O + 2 e<sup>−</sup> → Pb + 2 OH<sup>−</sup>", "−0,58"],
                                                     ["Al(OH)<sub>4</sub><sup>−</sup> + 3 e<sup>−</sup> → Al + 4 OH<sup>−</sup>", "−2,33"], ["Fe(OH)<sub>2</sub> + 2 e<sup>−</sup> → Fe + 2 OH<sup>−</sup>", "−0,88"]])
       + p(T(91, 2)),
  alts={"A": "Al", "B": "Co", "C": "Cu(OH)<sub>2</sub>", "D": "Fe(OH)<sub>2</sub>", "E": "Pb"})
X(92, "Física", "Eletromagnetismo", "<p>O campo magnético variável da rede induz corrente no arame da cerca, e quem toca nele vira caminho para essa corrente até o chão. Ligando o arame à terra, a corrente induzida escoa pelo fio terra, e o arame fica no mesmo potencial do solo: deve-se <strong>fazer o aterramento dos arames da cerca</strong>. Alternativa <strong>A</strong>.</p><p>Fusíveis (B e D) só atuam com correntes altas; isolar os fios da rede (E) não elimina o campo magnético.</p>",
  tags=["indução eletromagnética", "aterramento"])
X(93, "Biologia", "Parasitologia", "<p>O tratamento tradicional age depois da infecção, matando o verme que já está no corpo. A vacina leva o organismo a produzir anticorpos antes do contato; quando a larva entra, o sistema imune já está preparado e pode <strong>eliminar o esquistossomo dentro do organismo antes da manifestação de sintomas</strong>. Alternativa <strong>E</strong>.</p><p>A vacina não impede a penetração pela pele (A), não age no caramujo (B) e não atua antes do contato (D).</p>",
  tags=["esquistossomose", "vacina"], trocas=[("verme Schistosoma mansoni", "verme <em>Schistosoma mansoni</em>"), ("gênero Biomphalaria", "gênero <em>Biomphalaria</em>")])
X(94, "Física", "Termologia", "<p>Não existe “frio” que entra: o que existe é calor que sai do mais quente para o mais frio. A porta fechada e os cobertores não aquecem nada, só dificultam a saída do calor. A função de ambos é <strong>minimizar a perda de calor pela casa e pelos corpos</strong>. Alternativa <strong>C</strong>.</p><p>Cobertores não aquecem (A, D e E): quem produz calor é o próprio corpo.</p>",
  tags=["isolante térmico", "calor"], trocas=[("um jingle (vinheta", "um <em>jingle</em> (vinheta"), ("Jingle é a alma do negócio", "<em>Jingle é a alma do negócio</em>")])
X(95, "Química", "Termoquímica", "<p>A glicose vira duas moléculas de ácido lático. Pela lei de Hess, a energia dessa transformação é a combustão da glicose menos a de dois ácidos láticos: −2 800 − 2 · (−1 344) = −2 800 + 2 688 = <strong>−112 kJ</strong>. O processo anaeróbico libera só 112 kJ por mol de glicose, contra 2 800 kJ da oxidação completa. Alternativa <strong>A</strong>.</p><p>2 688 kJ (C) é a energia que ainda fica guardada no ácido lático.</p>",
  tags=["lei de Hess", "fermentação lática"],
  enun=p(SUB(T(95, 0)).replace("O<sub>2</sub>", "O<sub>2</sub>"))
       + '<p class="centro">C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> (s) + 6 O<sub>2</sub> (g) → 6 CO<sub>2</sub> (g) + 6 H<sub>2</sub>O (l)&nbsp;&nbsp; Δ<sub>c</sub>H = −2 800 kJ</p>'
       + '<p class="centro">CH<sub>3</sub>CH(OH)COOH (s) + 3 O<sub>2</sub> (g) → 3 CO<sub>2</sub> (g) + 3 H<sub>2</sub>O (l)&nbsp;&nbsp; Δ<sub>c</sub>H = −1 344 kJ</p>' + p(T(95, 2)))
X(96, "Biologia", "Ecologia", "<p>Numa área desmatada, o ambiente é instável, e quem coloniza primeiro são espécies que se reproduzem cedo, têm muitos descendentes e crescem depressa. São as da estratégia 1: <strong>elas apresentam um elevado potencial biótico, o que facilita a rápida recolonização da área desmatada</strong>. Alternativa <strong>C</strong>.</p><p>A estratégia 2 é de ambientes estáveis (D), que a área desmatada não é.</p>",
  tags=["estrategistas r e K", "sucessão ecológica"],
  enun=p(T(96, 0)) + tabela(["", "Estratégia 1", "Estratégia 2"],
       [["<strong>Hábitat</strong>", "Mais instável e imprevisível", "Mais estável e previsível"], ["<strong>Potencial biótico</strong>", "Muito elevado", "Baixo"],
        ["<strong>Duração da vida</strong>", "Curta e com reprodução precoce", "Longa e com reprodução tardia"], ["<strong>Descendentes</strong>", "Muitos e com tamanho corporal pequeno", "Poucos e com tamanho corporal maior"],
        ["<strong>Tamanho populacional</strong>", "Variável", "Constante"]]) + p(T(96, 2)))
X(97, "Biologia", "Ecologia", "<p>As cutias são da mesma espécie e disputam o mesmo recurso, as sementes guardadas. Quando uma rouba a reserva da outra, há disputa entre indivíduos da mesma espécie por alimento: é uma relação de <strong>competição</strong> (intraespecífica). Alternativa <strong>D</strong>.</p><p>Não há uma cutia comendo a outra (B) nem vivendo às custas do corpo de outra (C).</p>",
  tags=["competição intraespecífica"])
X(98, "Biologia", "Fisiologia humana", "<p>Na protanopia faltam os cones do vermelho. A pessoa ainda percebe o azul com os cones do azul, que funcionam normalmente, e vê o cartão azul do mesmo jeito. Já as cores que dependem do vermelho (vermelho, magenta, amarelo e branco) parecem diferentes para ela. Os dois concordam no cartão <strong>azul</strong>. Alternativa <strong>E</strong>.</p><p>O branco (D) é a soma das três cores; sem o vermelho, a pessoa o percebe como ciano.</p>",
  figs(("q98", "Diagrama de três círculos sobrepostos, vermelho, verde e azul: vermelho e verde formam amarelo; verde e azul, ciano; azul e vermelho, magenta; o centro, onde os três se encontram, é branco.")),
  ["visão das cores", "daltonismo"], enun=p(T(98, 0)) + "[[fig:1]]" + p(T(98, 2), T(98, 3)))
X(99, "Biologia", "Ecologia", "<p>O resíduo do café tem açúcares e pectina (fontes de carbono) e alcaloides com nitrogênio. Ao se decompor no solo, ele devolve esses elementos aos ciclos: <strong>possibilita a reciclagem de carbono e nitrogênio</strong>, nutrientes para as plantas. Alternativa <strong>A</strong>.</p><p>O texto não fala de alumínio (B), pH (D) ou efeito inibidor (E); compactar o solo seria prejudicial (C).</p>",
  tags=["ciclos biogeoquímicos", "adubação orgânica"])
X(100, "Biologia", "Ecologia", "<p>Na agricultura orgânica não se usam agrotóxicos, então as pragas são controladas por meios naturais, como o controle biológico: <strong>utilização de predadores naturais</strong> dos insetos, como joaninhas contra pulgões. Alternativa <strong>D</strong>.</p><p>Adubação verde, compostagem e <em>Rhizobium</em> (A, B e E) servem para fertilizar o solo, não para controlar insetos.</p>",
  tags=["controle biológico", "agricultura orgânica"], alts={**D[100]["alternativas"], "E": "uso de sementes inoculadas com <em>Rhizobium</em>."})
X(101, "Biologia", "Fisiologia humana", "<p>A EPO estimula a produção de hemácias. Com mais hemácias, o sangue transporta mais <strong>oxigênio</strong> aos músculos, que fazem mais respiração celular e produzem mais ATP: <strong>transporte de oxigênio, para aumento da produção de ATP</strong>. Alternativa <strong>C</strong>.</p><p>As hemácias não transportam lipídios, proteínas ou vitamina C (A, D e E).</p>",
  tags=["eritropoetina", "doping"], trocas=[("considerado doping", "considerado <em>doping</em>"), ("esse doping", "esse <em>doping</em>")])
X(102, "Física", "Termologia", "<p>Área interna de A: 6 · 40 · 40 = 9 600 cm<sup>2</sup>. De B: 2 · 40 · 40 + 4 · 60 · 40 = 12 800 cm<sup>2</sup>. O calor que entra é proporcional a k · área; em B derreteu o dobro do gelo: k<sub>B</sub> · 12 800 = 2 · k<sub>A</sub> · 9 600. Então k<sub>A</sub>/k<sub>B</sub> = 12 800/19 200 ≈ <strong>0,67</strong>. Alternativa <strong>B</strong>.</p><p>0,50 (A) ignora a diferença das áreas; 1,33 (D) inverte a razão.</p>",
  tags=["condução térmica", "lei de Fourier"],
  enun=p(T(102, 0).replace("condutividade térmica k", "condutividade térmica <em>k</em>"), T(102, 1).replace("kA e kB", "<em>k</em><sub>A</sub> e <em>k</em><sub>B</sub>"))
       + p("A razão \\(\\frac{k_A}{k_B}\\) é mais próxima de"))
X(103, "Química", "Oxirredução", "<p>Na primeira reação, a glicose é oxidada a ácido glucônico e o O<sub>2</sub> é reduzido a H<sub>2</sub>O<sub>2</sub>. Na segunda, o iodeto é oxidado a tri-iodeto e o oxigênio do peróxido é reduzido. Nas duas há transferência de elétrons: o tipo de reação é de <strong>oxirredução</strong>. Alternativa <strong>C</strong>.</p><p>Não são reações de síntese, análise, complexação ou ácido-base (A, B, D e E).</p>",
  figs(("q103", "Esquema do biochip: (i) antes do soro, um canal com três círculos, onde ficam as enzimas e o KI; (ii) depois de adicionado o soro à esquerda, o fluxo segue para a direita e o último círculo fica colorido.")),
  ["número de oxidação", "biossensor"],
  enun=p(T(103, 0)) + "[[fig:1]]" + p(T(103, 2).replace("desloca- -se", "desloca-se"))
       + '<p class="centro">Equação 1: C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> (aq) + O<sub>2</sub> (g) + H<sub>2</sub>O (l) → C<sub>6</sub>H<sub>12</sub>O<sub>7</sub> (aq) + H<sub>2</sub>O<sub>2</sub> (aq) (enzimas)</p>'
       + p(T(103, 4)) + '<p class="centro">Equação 2: 2 H<sub>2</sub>O<sub>2</sub> (aq) + 3 I<sup>−</sup> (aq) → I<sub>3</sub><sup>−</sup> (aq) + 2 H<sub>2</sub>O (l) + O<sub>2</sub> (g)</p>'
       + fonte(T(103, 6)) + p(T(103, 7)))
X(104, "Química", "Química ambiental", "<p>Os fármacos foram feitos para ser estáveis e passam pelas estações de tratamento sem ser destruídos. Ampliar a coleta de esgoto não basta, porque o tratamento atual não os remove. A ação que minimiza o problema é o <strong>desenvolvimento de novos processos nas estações de tratamento de efluentes</strong>. Alternativa <strong>D</strong>.</p><p>Esterco, lixões e reúso de lodo (A, C e E) espalhariam ainda mais os resíduos.</p>",
  tags=["fármacos no ambiente", "tratamento de efluentes"])
X(105, "Química", "Atomística", "<p>A chama fornece energia e os elétrons saltam para níveis mais externos. Ao voltar, eles liberam essa energia como luz, com cor característica de cada elemento. A emissão ocorre na <strong>transição eletrônica de um nível mais externo para outro mais interno</strong>. Alternativa <strong>D</strong>.</p><p>A promoção para níveis maiores (E) absorve energia; a luz vem da volta.</p>",
  tags=["teste de chama", "modelo de Bohr"])
X(106, "Física", "Estática", "<p>No ponto da atleta, as duas metades da fita a puxam para cima: 2T · sen 10° = peso = 800 N. Então T = 800/(2 · 0,17) ≈ 2 353 N ≈ <strong>2,4 × 10<sup>3</sup> N</strong>, que é a força em cada árvore. Alternativa <strong>D</strong>.</p><p>Usar o cosseno no lugar do seno daria cerca de 4,1 × 10<sup>2</sup> N (B); com ângulo pequeno, a força é muito maior que o peso.</p>",
  figs(("q106", "Atleta equilibrada no meio de uma fita de slackline presa entre duas árvores; a fita forma um pequeno ângulo de 10° com a horizontal de cada lado.")),
  ["equilíbrio", "decomposição de forças"],
  enun=p(T(106, 0).replace("Slackline é", "<em>Slackline</em> é").replace("10 m s−2", "10 m s<sup>−2</sup>")) + "[[fig:1]]" + p(T(106, 2)),
  alts={k: re.sub(r"10(\d)", r"10<sup>\1</sup>", v) for k, v in D[106]["alternativas"].items()})
X(107, "Biologia", "Zoologia", "<p>Os náuplios se movem em direção à luz da lâmpada. Movimento de um organismo inteiro orientado pela luz se chama fototaxia, mas, entre as alternativas, a que descreve esse deslocamento em direção à luz é o <strong>fototropismo positivo</strong>. Alternativa <strong>B</strong>.</p><p>Eles sobem por causa da luz, não por gravidade, água, calor ou substâncias (A, C, D e E).</p>",
  tags=["comportamento animal", "fototaxia"], trocas=[("larvas de Artemia", "larvas de <em>Artemia</em>"), ("Ovos de Artemia", "Ovos de <em>Artemia</em>")])
X(108, "Química", "Ligações químicas", "<p>O composto citado é o difluoreto de xenônio, XeF<sub>2</sub>. O xenônio tem 8 elétrons de valência; ao fazer duas ligações covalentes com o flúor, compartilha mais 2 elétrons. Na fórmula de Lewis, fica com 3 pares não ligantes e 2 pares ligantes: <strong>10 elétrons</strong> na camada de valência, mais que o octeto. Alternativa <strong>C</strong>.</p><p>8 (B) seria o octeto, que o texto mostra não valer para o xenônio.</p>",
  tags=["regra do octeto", "gases nobres"], trocas=[("5s25p6", "5<em>s</em><sup>2</sup>5<em>p</em><sup>6</sup>"), ("2s22p5", "2<em>s</em><sup>2</sup>2<em>p</em><sup>5</sup>")])
X(109, "Física", "Movimento circular", "<p>Se a reentrada tivesse ocorrido minutos depois, os destroços cairiam na cidade, a oeste do oceano. A Terra gira de oeste para leste e o foguete, que estava sobre o oceano, ainda não tinha alcançado o Rio: ele se movia no mesmo sentido da rotação, mas mais rápido, “ultrapassando” a superfície. A velocidade angular era <strong>superior à da Terra e no mesmo sentido</strong>. Alternativa <strong>B</strong>.</p><p>Com velocidade igual (A), o foguete ficaria parado sobre o mesmo ponto da Terra.</p>",
  figs(("q109", "Globo terrestre com a linha do Equador, a América do Sul, o Oceano Atlântico e o Rio de Janeiro marcado; no polo, uma seta indica o sentido de rotação da Terra.")),
  ["velocidade angular", "referencial"], enun=p(T(109, 0)) + "[[fig:1]]" + fonte(T(109, 2).replace("Lixo espacial", "<em>Lixo espacial</em>")) + p(T(109, 3)))
X(110, "Biologia", "Genética", "<p>A segregação independente vale para genes em cromossomos diferentes. Genes próximos num mesmo cromossomo tendem a ir juntos para o gameta, a não ser que ocorra crossing-over entre eles: é a ligação gênica. Por isso, <strong>os genes localizados fisicamente próximos no mesmo cromossomo tendem a ser herdados juntos</strong>. Alternativa <strong>D</strong>.</p><p>Dominância (A) não altera a segregação; não disjunção (C e E) é exceção rara, não o motivo geral.</p>",
  tags=["linkage", "segunda lei de Mendel"], trocas=[("Genética médica", "<em>Genética médica</em>")])
X(111, "Física", "Dinâmica", "<p>Caindo 5 m, o tijolo chega a v = √(2gh) = √100 = 10 m/s. Seu momento linear é 2,5 · 10 = 25 kg m/s, anulado em 0,5 s: F = 25/0,5 = 50 N. O peso do tijolo é 25 N; a força equivale ao peso de <strong>2 tijolos</strong>. Alternativa <strong>A</strong>.</p><p>Dividir pelo tempo sem achar a velocidade, ou esquecer o peso como unidade, leva a 10 ou 50 (C e E).</p>",
  tags=["impulso", "quantidade de movimento"], trocas=[("10 m s−2", "10 m s<sup>−2</sup>")])
X(112, "Química", "Forças intermoleculares", "<p>Os hidrocarbonetos são apolares e se atraem por forças de dispersão (London), que ficam mais fortes conforme a cadeia cresce. A fração 4 tem as maiores cadeias (C<sub>14</sub> a C<sub>18</sub>): para separar essas moléculas é preciso mais energia, porque <strong>as forças intermoleculares são mais intensas</strong>. Alternativa <strong>D</strong>.</p><p>Na destilação as moléculas só se separam, não se quebram (E).</p>",
  tags=["destilação fracionada", "petróleo"],
  enun=p(T(112, 0)) + tabela(["Fração", "Faixa de temperatura (°C)", "Exemplos de produto(s)", "Número de átomos de carbono (hidrocarboneto de fórmula geral C<sub>n</sub>H<sub>2n+2</sub>)"],
       [["1", "Até 20", "Gás natural e gás de cozinha (GLP)", "C<sub>1</sub> a C<sub>4</sub>"], ["2", "30 a 180", "Gasolina", "C<sub>6</sub> a C<sub>12</sub>"],
        ["3", "170 a 290", "Querosene", "C<sub>11</sub> a C<sub>16</sub>"], ["4", "260 a 350", "Óleo diesel", "C<sub>14</sub> a C<sub>18</sub>"]])
       + fonte(T(112, 2)) + p(T(112, 3)))
X(113, "Física", "Eletromagnetismo", "<p>No movimento circular, a força magnética é a resultante centrípeta: qvB = mv<sup>2</sup>/r, logo ω = v/r = qB/m, que não depende da velocidade. O período de uma volta é 2π/ω = 2πm/(qB). Em N voltas, t = 2πNm/(qB), e a massa é <strong>m = qBt/(2πN)</strong>. Alternativa <strong>A</strong>.</p><p>qBt/(πN) (B) usaria meia volta como período.</p>",
  figs(("q113", "Eixos x, y e z; linhas de campo magnético B paralelas ao eixo x; um íon positivo +q descreve uma trajetória helicoidal em torno das linhas de campo, avançando ao longo de x.")),
  ["força magnética", "movimento helicoidal"],
  enun=p(T(113, 0).replace("carga elétrica q", "carga elétrica <em>q</em>").replace("constante B,", "constante \\(\\vec{B}\\),").replace("tempo t de", "tempo <em>t</em> de").replace("para N voltas", "para <em>N</em> voltas").replace("valores q, B, N e t", "valores <em>q</em>, <em>B</em>, <em>N</em> e <em>t</em>")) + "[[fig:1]]" + p(T(113, 4)),
  alts=FR("\\frac{qBt}{2\\pi N}", "\\frac{qBt}{\\pi N}", "\\frac{2qBt}{\\pi N}", "\\frac{qBt}{N}", "\\frac{2qBt}{N}"))
X(114, "Biologia", "Virologia", "<p>Os retrovírus (como o HIV) usam a transcriptase reversa para fazer DNA a partir do seu RNA, e infectam só humanos, sem vetores. Os medicamentos desenvolvidos são os <strong>antirretrovirais, que dificultam a reprodução desses vírus</strong>, bloqueando etapas como a transcrição reversa. Alternativa <strong>E</strong>.</p><p>Não há vetores para controlar (A), e o texto fala em tratamento, não em prevenção por vacina (D).</p>",
  tags=["retrovírus", "HIV"], trocas=[("família Retroviridae", "família <em>Retroviridae</em>")])
X(115, "Química", "Química ambiental", "<p>A proposta é usar o concreto reciclado moído no lugar do “particulado rochoso”, isto é, da brita, que vem da fragmentação de rochas. O benefício é a <strong>redução da extração da brita</strong>, além do aproveitamento do entulho. Alternativa <strong>A</strong>.</p><p>A areia, a água e o cimento (B, C e E) continuam sendo usados no novo concreto.</p>",
  tags=["reciclagem", "construção civil"])
X(116, "Biologia", "Citologia", "<p>O texto diz que, quanto maiores as interações entre os fosfolipídios, menor a fluidez. Caudas curtas e com insaturações (dobras) se encaixam mal e interagem menos. Na bicamada II as caudas são curtas e quase todas têm dobras de insaturação: é a de <strong>maior fluidez</strong>. Alternativa <strong>B</strong>.</p><p>I e IV têm caudas retas, que se empacotam bem; III e V misturam caudas longas ou retas.</p>",
  figs(("q116", "Representação simplificada de um fosfolipídio: cabeça polar redonda e duas caudas hidrocarbônicas, uma reta e outra com uma dobra que indica insaturação."),
       ("q116b", "Cinco bicamadas lipídicas: I, caudas longas e retas; II, caudas curtas com dobras de insaturação; III, caudas curtas com algumas dobras; IV, caudas longas e retas, bem juntas; V, caudas longas com dobras.")),
  ["membrana plasmática", "fosfolipídios"], enun=p(T(116, 0)) + "[[fig:1]]" + p(T(116, 4)) + "[[fig:2]]" + p(T(116, 11)))
X(117, "Física", "Calorimetria", "<p>Pela tabela, 10 g de castanha têm 70 kcal; então 2,5 g têm 17,5 kcal. Com 50% aproveitado, a água recebe 8 750 cal. ΔT = Q/(mc) = 8 750/(350 · 1) = 25 °C. A temperatura final é 20 + 25 = <strong>45 °C</strong>. Alternativa <strong>C</strong>.</p><p>25 (A) é só a variação; 70 °C (E) usaria toda a energia.</p>",
  tags=["calor sensível", "valor energético"],
  enun=p(T(117, 0).replace("1 cal g−1 °C−1", "1 cal g<sup>−1</sup> °C<sup>−1</sup>"))
       + tabela(["Quantidade por porção de 10 g (2 castanhas)", ""], [["Valor energético", "70 kcal"], ["Carboidratos", "0,8 g"], ["Proteínas", "3,5 g"], ["Gorduras totais", "3,5 g"]]) + p(T(117, 2)))
X(118, "Química", "Eletroquímica", "<p>No ânodo ocorre a oxidação. O zinco perde elétrons e, em meio básico, forma o íon zincato: Zn + 4 OH<sup>−</sup> → Zn(OH)<sub>4</sub><sup>2−</sup> + 2 e<sup>−</sup>. A espécie formada no ânodo é <strong>Zn(OH)<sub>4</sub><sup>2−</sup></strong>. Alternativa <strong>E</strong>.</p><p>OH<sup>−</sup> (D) se forma no cátodo, pela redução do O<sub>2</sub>.</p>",
  figs(("q118", "Bateria zinco-ar: à esquerda, um eletrodo poroso por onde entra o O₂ do ar e se forma OH⁻; no meio, uma membrana separadora; à direita, o eletrodo de zinco, onde se forma Zn(OH)₄²⁻; os eletrodos estão ligados a uma lâmpada acesa.")),
  ["pilhas", "ânodo"], enun=p(T(118, 0)) + "[[fig:1]]" + fonte(T(118, 3)) + p(T(118, 4)),
  alts={"A": "H<sub>2</sub> (g).", "B": "O<sub>2</sub> (g).", "C": "H<sub>2</sub>O (l).", "D": "OH<sup>−</sup> (aq).", "E": "Zn(OH)<sub>4</sub><sup>2−</sup> (aq)."})
PA = lambda s: re.sub(r"([pm])([AB])", r"<em>\1</em><sub>\2</sub>", s).replace(" < ", " &lt; ").replace(" > ", " &gt; ")
X(119, "Física", "Hidrostática", "<p>O pneu A deforma muito menos sob o mesmo esforço: está mais duro, com pressão maior, p<sub>A</sub> &gt; p<sub>B</sub>. Como os pneus de A são mais estreitos, têm volume menor; e as massas de ar são proporcionais aos volumes: m<sub>A</sub> &lt; m<sub>B</sub>. Alternativa <strong>B</strong>.</p><p>Pressão maior não significa mais ar: o pneu estreito guarda menos.</p>",
  tags=["pressão", "volume"], enun=p(PA(T(119, 0)), T(119, 1)), alts={k: PA(v) for k, v in D[119]["alternativas"].items()})
X(120, "Química", "Química orgânica", "<p>Bixina, licopeno e β-caroteno têm longas sequências de ligações duplas alternadas com simples. Essa <strong>cadeia conjugada</strong> deixa os elétrons espalhados pela molécula e faz com que ela absorva luz visível, o que dá a cor. Alternativa <strong>A</strong>.</p><p>Ramificações, carbonos terciários e sp<sup>3</sup> (B, C e E) não produzem cor; as duplas são principalmente trans (contra D).</p>",
  figs(("q120", "Fórmulas estruturais de três corantes naturais: bixina (presente no urucum), com grupos COOH e COOCH₃ nas pontas; licopeno (presente no tomate); e β-caroteno (presente na cenoura e na laranja), com anéis nas duas pontas. Todos têm longas cadeias de ligações duplas alternadas.")),
  ["cadeia conjugada", "corantes"], enun=p(T(120, 0)) + "[[fig:1]]" + fonte(T(120, 7)) + p(T(120, 8)))
X(121, "Física", "Energia", "<p>A haste tem h = 410 mm. Pela figura, o disco desce 2h/3 = 0,273 m. Com o sistema conservativo e a translação desprezível, toda a energia potencial perdida vira energia de rotação: E = mgΔh = 0,030 · 10 · 0,273 ≈ <strong>8,20 × 10<sup>−2</sup> J</strong>. Alternativa <strong>B</strong>.</p><p>Usar h/3 daria 4,10 × 10<sup>−2</sup> J (A), e a altura inteira, 1,23 × 10<sup>−1</sup> J (C); D e E esquecem de converter gramas e milímetros.</p>",
  figs(("q121", "Brinquedo disco de Maxwell: estrutura com barra superior, disco de metal pendurado por dois fios; cotas mostram a altura h da haste e a descida 2h/3 do disco. Recorte do manual: conteúdo (base de metal, hastes metálicas, barra superior, disco de metal); tamanho (C × L × A): 300 mm × 100 mm × 410 mm; massa do disco de metal: 30 g.")),
  ["conservação da energia", "energia de rotação"],
  enun=p(T(121, 0)) + p(T(121, 1), T(121, 2)) + p(T(121, 3).replace("10 m s−2", "10 m s<sup>−2</sup>")[:-1] + " \\(\\frac{1}{3}\\) da altura da haste do brinquedo.") + p(T(121, 5)) + "[[fig:1]]" + p(T(121, 8)),
  alts=FR("4{,}10 \\times 10^{-2}", "8{,}20 \\times 10^{-2}", "1{,}23 \\times 10^{-1}", "8{,}20 \\times 10^{4}", "1{,}23 \\times 10^{5}"))
X(122, "Química", "Cinética química", "<p>Para sair da estrutura I (alicina) para a II, a molécula perde o oxigênio ligado ao enxofre. O “sabonete” de aço participa dessa transformação, mas, como diz o texto, não se desgasta com o uso: sai inalterado no fim. Uma substância que favorece a reação sem ser consumida atua como <strong>catalisador</strong>. Alternativa <strong>E</strong>.</p><p>Um redutor (B) se oxidaria e seria gasto, o que o texto descarta.</p>",
  figs(("q122", "Estrutura I, a alicina: CH₂=CH–CH₂–S(=O)–S–CH₂–CH=CH₂, com o oxigênio ligado a um dos enxofres. Estrutura II: CH₂=CH–CH₂–S–S–CH₂–CH=CH₂, sem o oxigênio.")),
  ["catalisador", "alicina"], enun=p(T(122, 0)) + "[[fig:1]]" + p(T(122, 2)))
X(123, "Biologia", "Ecologia", "<p>O texto diz que o estrôncio-90 é quimicamente parecido com o cálcio e pode substituí-lo em processos biológicos. No corpo humano, o cálcio se concentra nos ossos; por isso o estrôncio-90 se acumula no tecido <strong>ósseo</strong>. Alternativa <strong>E</strong>.</p><p>Os outros tecidos (A a D) não armazenam cálcio de forma significativa.</p>",
  tags=["radioatividade", "bioacumulação"])
X(124, "Química", "Reações orgânicas", "<p>Na transesterificação, um éster reage com um álcool e troca o grupo álcool. O PET é éster de etanodiol; para gerar o tereftalato de <strong>metila</strong> (com grupos –COOCH<sub>3</sub>) e liberar o etanodiol, o reagente A tem de ser o álcool que fornece o grupo metila: o <strong>metanol</strong>. Alternativa <strong>B</strong>.</p><p>Metano e éter (A e C) não fazem transesterificação; ácido e anidrido (D e E) dariam outras reações.</p>",
  figs(("q124", "Esquema: o PET, unidade de repetição com anel benzênico entre dois grupos éster ligados a –CH₂–CH₂–, reage com 2n A, a altas temperaturas e pressão, formando n tereftalato de metila (anel com dois –COOCH₃) e n etanodiol (HO–CH₂–CH₂–OH).")),
  ["transesterificação", "reciclagem do PET"], enun=p(T(124, 0)) + "[[fig:1]]" + p(T(124, 3)))
X(125, "Biologia", "Botânica", "<p>Briófitas e pteridófitas dependem de água para que o gameta masculino nade até a oosfera. Com o <strong>tubo polínico</strong> (número 3), surgido nas espermatófitas, o gameta chega à oosfera por dentro da planta, sem precisar de água: foi a conquista definitiva do ambiente terrestre. Alternativa <strong>C</strong>.</p><p>Vasos condutores (2) ajudaram, mas as pteridófitas continuaram presas à água para a fecundação.</p>",
  figs(("q125", "Árvore filogenética das plantas ao longo de milhões de anos (de 500 até hoje), a partir de uma alga verde ancestral: hepáticas, antóceros e musgos; licófitas e pteridófitas; gimnospermas e angiospermas. Legenda: 1, embriões protegidos no gametófito; 2, tecidos condutores verdadeiros; 3, formação de tubo polínico; 4, polinização pelo vento; 5, produção de frutos.")),
  ["evolução das plantas", "tubo polínico"], enun=p(T(125, 0)) + "[[fig:1]]" + fonte("CAMPBELL, N. et al. <em>Biologia</em>. São Paulo: Artmed, 2010 (adaptado).") + p(T(125, 3)),
  alts=dict(D[125]["alternativas"], E="5."))  # restos de outra figura grudavam na alternativa E
X(126, "Física", "Eletrodinâmica", "<p>A TV precisa de pelo menos 90 V, então o cabo pode “perder” no máximo 30 V: a corrente total vai até 30/10 = 3 A, e a resistência do conjunto TV + lâmpadas deve ser de pelo menos 90/3 = 30 Ω. Com n lâmpadas de 200 Ω em paralelo com a TV de 50 Ω: 1/R = 1/50 + n/200 = (4 + n)/200, R = 200/(4 + n) ≥ 30, logo n ≤ 2,67. O máximo é <strong>2 lâmpadas</strong>. Alternativa <strong>B</strong>.</p><p>Com 3 lâmpadas, R ≈ 28,6 Ω e a TV receberia cerca de 89 V.</p>",
  figs(("q126", "Circuito: fonte de 120 V, um resistor de 10 Ω em série (o cabo) e, em paralelo, cinco lâmpadas de 200 Ω, cada uma com seu interruptor, e uma televisão de 50 Ω.")),
  ["associação de resistores", "queda de tensão"], enun=p(T(126, 0)) + "[[fig:1]]" + p(T(126, 4)))
X(127, "Biologia", "Metabolismo energético", "<p>O DNP devolve os prótons à matriz sem passar pela ATP-sintase. Assim, a cadeia respiratória continua funcionando, mas o gradiente de prótons não gera ATP. A célula precisa queimar mais nutrientes para produzir a mesma energia, e o excesso vira calor: há <strong>redução da produção de ATP, resultando em maior gasto celular de nutrientes</strong>. Alternativa <strong>E</strong>.</p><p>A cadeia respiratória e o ciclo de Krebs não são bloqueados (A e B): eles trabalham mais.</p>",
  tags=["fosforilação oxidativa", "desacoplador"])
X(128, "Química", "Modelos atômicos", "<p>Hoje sabemos que o átomo é divisível (1), que há isótopos de massas diferentes no mesmo elemento (2) e que núcleos podem se transformar em reações nucleares (4). O postulado 3 também tem exceções (isóbaros). Mas continua valendo que os átomos se combinam em proporções de números inteiros pequenos para formar compostos: o postulado <strong>5</strong>. Alternativa <strong>E</strong>.</p>",
  tags=["Dalton", "teoria atômica"],
  enun=p(T(128, 0).replace("intitulado Um novo sistema de filosofia química", "intitulado <em>Um novo sistema de filosofia química</em>").replace("original A New System of Chemical Philosophy", "original <em>A New System of Chemical Philosophy</em>"))
       + OL(*[T(128, i).split(". ", 1)[1] for i in range(1, 6)]) + p(T(128, 6)) + fonte(T(128, 7)) + p(T(128, 8)))
X(129, "Química", "Titulação", "<p>Foram gastos 24 mL de NaOH 0,01 mol/L: 2,4 × 10<sup>−4</sup> mol de OH<sup>−</sup>. Como o ácido cítrico é triprótico, há 0,8 × 10<sup>−4</sup> mol de ácido, ou 0,8 × 10<sup>−4</sup> · 192 ≈ 0,0154 g em 2,2 g de polpa. Em 100 g: 0,0154 · 100/2,2 ≈ 0,70 g. Pelo quadro, esse valor atende ao mínimo do caju (0,3) e da graviola (0,6), mas não da acerola, do cupuaçu ou do maracujá: <strong>caju ou graviola</strong>. Alternativa <strong>C</strong>.</p><p>Esquecer que o ácido é triprótico daria 2,1 g/100 g e incluiria o cupuaçu.</p>",
  tags=["titulação", "estequiometria"],
  enun=p(T(129, 0).replace("192 g mol−1", "192 g mol<sup>−1</sup>"))
       + tabela(["Polpa de fruta", "Valor mínimo da acidez total expressa em ácido cítrico (g/100 g)"], [["Acerola", "0,8"], ["Caju", "0,3"], ["Cupuaçu", "1,5"], ["Graviola", "0,6"], ["Maracujá", "2,5"]])
       + p(T(129, 2).replace("0,01 mol L−1", "0,01 mol L<sup>−1</sup>")) + fonte(T(129, 3)) + p(T(129, 4)))
X(130, "Biologia", "Citologia", "<p>O caldo estava muito salgado e a batata, sem sal. O sal passou do meio mais concentrado (caldo) para o menos concentrado (batata), sem gasto de energia: foi <strong>difusão, porque o transporte ocorreu a favor do gradiente de concentração</strong>. Alternativa <strong>E</strong>.</p><p>Na osmose (A) só a água passa; fagocitose, pinocitose e exocitose (B, C e D) envolvem vesículas e não explicam a entrada de sal na batata cozida.</p>",
  tags=["difusão", "transporte passivo"])
X(131, "Física", "Óptica geométrica", "<p>Com abertura de 90° e altura de 1 000 m, cada foto cobre no solo 2 · H · tg 45° = 2 000 m. Com sobreposição de 20%, cada nova foto avança 80% disso: 1 600 m. A 50 m/s, o intervalo é 1 600/50 = <strong>32 segundos</strong>. Alternativa <strong>B</strong>.</p><p>40 s (A) não considera a sobreposição; 8 s (E) usa só os 20%.</p>",
  figs(("q131", "Esquema de um vant com câmera voando à altura H sobre o solo, com abertura de 45° para cada lado; três fotos consecutivas cobrem faixas do solo que se sobrepõem em 20% (ΔS).")),
  ["campo de visão", "movimento uniforme"],
  enun=p(T(131, 0)) + "[[fig:1]]" + p(T(131, 4).replace("50 m s−1", "50 m s<sup>−1</sup>")) + fonte(T(131, 5)) + p(T(131, 6)))
X(132, "Física", "Óptica", "<p>Debaixo d’água, o olho perde boa parte do poder de focalizar da córnea, e a imagem fica borrada. Com a pupila menor, só entram os raios que passam pelo centro do sistema óptico, quase sem desvio: o borrão diminui, como numa câmera de abertura pequena. A acuidade melhora pela diminuição <strong>do desvio dos feixes luminosos refratados no interior do olho</strong>. Alternativa <strong>D</strong>.</p><p>Menos luz (A) não melhora a nitidez por si; pupila menor aumentaria a difração (B), não a diminuiria.</p>",
  tags=["pupila", "refração"])
X(133, "Biologia", "Fisiologia humana", "<p>A hemodiálise substitui a principal função do rim, filtrar o sangue e eliminar as excretas nitrogenadas. Um rim biônico que substitua a hemodiálise vai promover diretamente a <strong>remoção de ureia</strong>. Alternativa <strong>A</strong>.</p><p>O rim não excreta lipídios (B), não produz vasopressina nem aldosterona (C e E), e a amônia é transformada no fígado (D).</p>",
  tags=["excreção", "hemodiálise"], trocas=[("O “The Kidney Project”", "O “<em>The Kidney Project</em>”")])
X(134, "Física", "Hidrostática", "<p>O papel de filtro tem poros finíssimos. O etanol é atraído pelas fibras (adesão) e sobe pelos canais estreitos, vencendo a gravidade, como a água sobe num tubo fino. É a <strong>capilaridade nos poros do papel</strong>. Alternativa <strong>D</strong>.</p><p>Não há reação com o papel (C), e a evaporação (A) faria o líquido sumir, não subir.</p>",
  figs(("q134", "Copo de vidro com etanol no fundo e uma folha de papel de filtro de pé dentro dele; o líquido molha o papel acima do nível do etanol.")),
  ["capilaridade", "adesão"], enun=p(T(134, 0)) + "[[fig:1]]" + p(T(134, 4)))
X(135, "Física", "Óptica", "<p>Huygens argumenta que os raios de luz se cruzam sem se atrapalhar, o que não aconteceria se a luz fosse feita de matéria que viaja do objeto até nós, “como uma flecha ou bala”. Ele contesta <strong>o modelo corpuscular defendido por Newton, que descreve a luz como um feixe de partículas</strong>. Alternativa <strong>C</strong>.</p><p>Huygens defendia o modelo ondulatório (B), não o atacava.</p>",
  tags=["natureza da luz", "Huygens"])

completar(Q, R)
