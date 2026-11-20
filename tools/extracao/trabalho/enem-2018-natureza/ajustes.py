# Enem 2018, 2º dia, caderno azul: Ciências da Natureza (questões 91 a 135; no site, 1 a 45).
# Texto legível (sem DECOD). Quadros das Q92 e 115 em tabela HTML; equação da Q114 em HTML. Alternativas em imagem: Q95, 108 e 126.
# Sem anuladas nesta área.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, paragrafos_enem

ID = "enem-2018-natureza"
META = {"id": ID, "banca": "Enem", "ano": 2018, "titulo": "Enem 2018: Ciências da Natureza", "fonte": "Inep", "dataExame": "2018-11-11",
        "duracaoMinutos": 150, "area": "Ciências da Natureza", "caderno": "azul", "dia": 2}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2018-dia2-azul")
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
CH = lambda s: s.replace("CaCO3", "CaCO<sub>3</sub>").replace("NH2OH", "NH<sub>2</sub>OH").replace("TiO2", "TiO<sub>2</sub>")

X(91, "Química", "Isomeria", "<p>Na figura, a luz de 365 nm transforma as ligações N=N do azobenzeno da forma trans (cadeia esticada) para a forma cis (cadeia dobrada), e a luz de 420 nm faz o caminho inverso. Como a forma cis é mais compacta, a cadeia encolhe e a lâmina se curva. O movimento decorre da <strong>isomerização das ligações N=N, sendo a forma cis do polímero mais compacta que a trans</strong>. Alternativa <strong>B</strong>.</p><p>Não há tautomeria (C), que envolveria migração de hidrogênio, nem simples vibração das ligações (A).</p>",
  figs(("q91", "Lâmina de silício presa a um suporte, com uma cadeia de polímero de azobenzeno. Sob luz de 365 nm, as unidades N=N passam de uma forma esticada para uma forma dobrada e a lâmina se curva; sob luz de 420 nm, voltam à forma esticada e a lâmina se endireita. Legenda dos átomos: hidrogênio, carbono e nitrogênio.")),
  ["azobenzeno", "isomeria cis-trans"], enun=p(T(91, 0)) + "[[fig:1]]" + fonte(T(91, 5)) + p(T(91, 6)))
X(92, "Química", "Termoquímica", "<p>A energia liberada pela gasolina na ida é a mesma que o etanol deve liberar na volta.</p><p>Gasolina: 40 L × 0,7 kg/L = 28 kg = 28 000 g; energia = 28 000 g × 10 kcal/g = 280 000 kcal.</p><p>Etanol: massa = 280 000 kcal ÷ 6 kcal/g ≈ 46 700 g; volume = 46 700 g ÷ 0,8 g/mL ≈ 58 000 mL ≈ <strong>58 L</strong>. Alternativa <strong>D</strong>.</p>",
  tags=["combustíveis", "calor de combustão"],
  enun=p(T(92, 0).replace("carro flex", "carro <em>flex</em>").replace("veículo flex", "veículo <em>flex</em>"), T(92, 1)) + tabela(["Combustível", "Densidade (g mL<sup>−1</sup>)", "Calor de combustão (kcal g<sup>−1</sup>)"], [["Etanol", "0,8", "−6"], ["Gasolina", "0,7", "−10"]]) + p(T(92, 3)))
X(93, "Química", "Eletroquímica", "<p>Na pilha, o cátodo é onde ocorre a redução, isto é, o eletrodo de maior potencial de redução. Entre ferro (−0,44 V) e cobre (+0,34 V), o cobre tem o maior potencial: o ferro se oxida (por isso aparece corroído) e o <strong>tubo de cobre</strong> é o cátodo. Alternativa <strong>D</strong>.</p><p>O ácido é o eletrólito, e o betume e o barro são isolantes.</p>",
  figs(("q93", "Corte da suposta pilha de Bagdá: um vaso de barro, com vestígio de ácido no fundo, contém um tubo de cobre e, dentro dele, uma barra de ferro; uma tampa de betume fecha a boca do vaso.")),
  ["pilha", "potencial de redução"],
  enun=p(T(93, 0).replace("E (", "<em>E</em>° (").replace("Fe2+", "Fe<sup>2+</sup>").replace("H+|H2", "H<sup>+</sup>|H<sub>2</sub>").replace("Cu2+", "Cu<sup>2+</sup>")) + "[[fig:1]]" + fonte(T(93, 3)) + p(T(93, 4)))
X(94, "Biologia", "Fisiologia humana", "<p>Na hipoglicemia, o pâncreas libera glucagon, que age no fígado quebrando o glicogênio armazenado (glicogenólise) e liberando glicose no sangue. O glucagon vai <strong>estimular a utilização do glicogênio</strong>. Alternativa <strong>E</strong>.</p><p>Transformar substâncias em glicogênio (D) é anabolismo, papel da insulina.</p>",
  tags=["glucagon", "glicemia"])
X(95, "Química", "Soluções", "<p>Considerando que os íons ocupam os espaços entre as moléculas de água, o volume continua 2 L = 2 000 cm³.</p><p>A: (2 000 g + 100 g) ÷ 2 000 cm³ = 1,05 g/cm³. B: (2 000 g + 200 g) ÷ 2 000 cm³ = 1,10 g/cm³.</p><p>Cada divisão vale 0,05 g/cm³; em relação à água pura (1,00 g/cm³), o densímetro deve subir uma divisão em A e duas em B, ficando menos imerso quanto mais densa for a solução. Esse é o desenho da opção D. Alternativa <strong>D</strong>.</p><p>Nas outras figuras, o densímetro afunda com o sal ou sobe a mesma altura nos dois recipientes.</p>",
  figs(("q95", "Densímetro em repouso na água pura: um tubo graduado com bulbo, flutuando num recipiente, com parte da escala acima da superfície."),
       ("q95a", "Alternativa A: o densímetro fica na mesma altura nos recipientes A e B, mais alto do que na água pura."),
       ("q95b", "Alternativa B: o densímetro afunda mais do que na água pura nos dois recipientes, e mais ainda em B."),
       ("q95c", "Alternativa C: o densímetro afunda um pouco mais do que na água pura, quase na mesma altura em A e B."),
       ("q95d", "Alternativa D: o densímetro sobe uma divisão em A e duas divisões em B em relação à água pura, ficando B menos imerso que A."),
       ("q95e", "Alternativa E: o densímetro sobe nos dois recipientes, com pouca diferença entre A e B.")),
  ["densidade", "densímetro"],
  enun=p(T(95, 0).replace("10−2 g cm−3", "10<sup>−2</sup> g cm<sup>−3</sup>")) + "[[fig:1]]" + p(T(95, 4), T(95, 5).replace("Na+", "Na<sup>+</sup>").replace("Cl−", "Cl<sup>−</sup>")), alts=ALT(2))
X(96, "Biologia", "Fisiologia humana", "<p>Os ácidos biliares têm uma parte polar e outra apolar. A parte apolar se liga às gotas de gordura e a polar fica voltada para a água, quebrando as gotas grandes em gotículas (emulsificação). Eles atuam como os sabões: <strong>agem como detergentes</strong>. Alternativa <strong>B</strong>.</p><p>Quem hidrolisa os lipídios são as lipases (A); a bile não é enzima.</p>",
  tags=["bile", "digestão de lipídios"])
X(97, "Física", "Eletromagnetismo", "<p>A bobina da etiqueta funciona como antena: o campo magnético variável da onda de rádio emitida pelo leitor atravessa a bobina e, pela lei de Faraday, induz nela uma corrente elétrica, que alimenta o microprocessador. O campo <strong>magnético da onda de rádio induz corrente na bobina</strong>. Alternativa <strong>C</strong>.</p><p>Aquecer os fios (D) não geraria energia útil para o circuito.</p>",
  tags=["indução eletromagnética", "RFID"])
X(98, "Biologia", "Ecologia", "<p>Ligando fragmentos de mata, os corredores permitem que animais se desloquem e sementes se dispersem entre populações antes isoladas. Os indivíduos de áreas diferentes passam a se cruzar, e a variabilidade genética aumenta: os corredores <strong>propiciam o fluxo gênico</strong>. Alternativa <strong>A</strong>.</p><p>Ilhas de proteção isoladas (E) são justamente o problema que os corredores tentam resolver.</p>",
  tags=["corredores ecológicos", "fragmentação"])
X(99, "Química", "Funções inorgânicas", "<p>O número de risco 268 indica um gás tóxico e corrosivo. Entre as opções, só a <strong>amônia (NH<sub>3</sub>)</strong> é ao mesmo tempo gás, tóxica e corrosiva (forma solução básica em contato com a umidade). Alternativa <strong>C</strong>.</p><p>Eteno e propano são inflamáveis (A e D); nitrogênio e gás carbônico não são corrosivos (B e E).</p>",
  figs(("q99", "Sinalização do caminhão: painel de segurança laranja com o número 268 em cima e 1005 embaixo, ao lado de um rótulo de risco em losango com uma caveira e os dizeres “gás tóxico” e o número 2.")),
  ["transporte de produtos perigosos", "amônia"], alts={k: SUB(v) for k, v in D[99]["alternativas"].items()})
X(100, "Biologia", "Citologia", "<p>A p53 detém o ciclo quando o DNA está danificado e, se o dano não é reparado, leva a célula à apoptose. Sem ela, células com mutações continuam se dividindo sem controle, o que pode levar a <strong>proliferação celular exagerada, resultando na formação de um tumor</strong>. Alternativa <strong>E</strong>.</p><p>A falta da p53 reduz a estabilidade genética, não a mantém (D).</p>",
  tags=["ciclo celular", "câncer"])
X(101, "Biologia", "Fisiologia comparada", "<p>Roedores, aves, répteis e artrópodes do deserto precisam economizar água. Uma adaptação comum a esses grupos é <strong>eliminar excretas nitrogenadas de forma concentrada</strong>: aves, répteis e insetos excretam ácido úrico, quase seco, e os roedores do deserto produzem urina muito concentrada. Alternativa <strong>B</strong>.</p><p>Répteis e artrópodes não têm glândulas sudoríparas (A) nem controlam a temperatura corporal (D).</p>",
  tags=["deserto", "excreção"])
X(102, "Química", "Cinética química", "<p>A hipótese diz que a decomposição “seria catalisada por íon cloreto”. Um catalisador acelera a reação sem ser consumido, <strong>diminuindo a energia de ativação</strong>. Alternativa <strong>C</strong>.</p><p>Catalisadores não deslocam equilíbrios (B), e o cloreto não é consumido como oxidante (A).</p>",
  tags=["catalisador", "energia de ativação"], trocas=[("conhecido como vermilion,", "conhecido como <em>vermilion</em>,"), ("hipótese de que o vermilion", "hipótese de que o <em>vermilion</em>"), ("fotoquímica do vermilion", "fotoquímica do <em>vermilion</em>")])
X(103, "Física", "Ondulatória", "<p>108 km/h ÷ 3,6 = 30 m/s. As faixas estão a 8 cm = 0,08 m. A frequência é o número de faixas por segundo:</p><p>f = v ÷ d = 30 ÷ 0,08 = <strong>375 Hz</strong>. Alternativa <strong>C</strong>.</p><p>Usar a velocidade em km/h, sem converter, dá 1 350 Hz (D), que é o erro mais comum.</p>",
  tags=["frequência", "velocidade"], trocas=[("108 km h", "108 km/h")])
X(104, "Física", "Estática", "<p>A força potente é maior que a resistente quando ela é aplicada mais perto do apoio do que a resistente (alavanca interpotente). Na <strong>pinça</strong>, os dedos apertam no meio, a ponta segura o objeto e o apoio fica na outra extremidade: o braço da potente é menor. Alternativa <strong>A</strong>.</p><p>No alicate, no quebra-nozes, no carrinho de mão e no abridor, a força é aplicada longe do apoio e é ampliada.</p>",
  figs(("q104", "Fotos de cinco objetos: alicate, pinça, quebra-nozes, carrinho de mão e abridor de garrafa.")),
  ["alavancas", "torque"])
X(105, "Química", "Tabela periódica", "<p>Nióbio (Z = 41) e tântalo (Z = 73) estão no mesmo grupo, o 5, da tabela periódica: têm a mesma configuração eletrônica na camada de valência (d³s²), e por isso propriedades químicas tão parecidas. A semelhança vem de <strong>pertencerem ao mesmo grupo na tabela periódica</strong>. Alternativa <strong>C</strong>.</p><p>São metais de transição externa, não interna (A e B), e seus elétrons mais externos estão nos níveis 5 e 6 (D).</p>",
  tags=["nióbio", "grupos da tabela"])
X(106, "Biologia", "Evolução", "<p>Especiação evidente é quando populações não conseguem mais cruzar entre si, em nenhum sentido. No diagrama, as setas pontilhadas (polinização inviável) aparecem nos dois sentidos entre Itirapina e Peti e entre Alcobaça e Marambaia. Alternativa <strong>D</strong>.</p><p>Nos outros pares há pelo menos um sentido de cruzamento bem-sucedido.</p>",
  figs(("q106", "Diagrama de cruzamentos entre nove populações de orquídea: Pão de Açúcar, Peti, Itirapina, Alcobaça, Itapeva, Bertioga, Olivença, Marambaia e Massambaba, ligadas por setas do doador para o receptor. Setas contínuas indicam polinização bem-sucedida, e pontilhadas, polinização inviável ou nula. Folhas pretas marcam populações da Mata Atlântica, e cinza, do Cerrado.")),
  ["especiação", "isolamento reprodutivo"],
  enun=p(T(106, 0).replace("(Epidendrum denticulatum)", "(<em>Epidendrum denticulatum</em>)")) + "[[fig:1]]" + fonte("FIORAVANTI, C. Os primeiros passos de novas espécies: plantas e animais se diferenciam por meio de mecanismos surpreendentes. <strong>Pesquisa Fapesp</strong>, out. 2013 (adaptado).") + p(T(106, 4)))
X(107, "Biologia", "Botânica", "<p>A enxertia é reprodução assexuada: o galho enxertado continua com o mesmo DNA da planta de onde veio. Para a atemoia, um híbrido, isso garante que todas as mudas tenham as mesmas características: a <strong>manutenção do genótipo da planta híbrida</strong>. Alternativa <strong>C</strong>.</p><p>Plantar por sementes, ao contrário, misturaria os genes e aumentaria a variabilidade (A).</p>",
  tags=["enxertia", "reprodução assexuada"],
  enun=p(T(107, 0).replace("(Annona cherimola)", "(<em>Annona cherimola</em>)").replace("(Annona squamosa)", "(<em>Annona squamosa</em>)")))
X(108, "Física", "Eletrodinâmica", "<p>A resistência é R = V ÷ i. Com V = 10i + i²:</p><p>R = (10i + i²) ÷ i = 10 + i.</p><p>É uma reta que começa em 10 Ω (i = 0) e chega a 17 Ω para i = 7 A. Alternativa <strong>D</strong>.</p><p>O resistor não é ôhmico: R muda com a corrente, então as retas horizontais (A e B) estão erradas, e a reta da C esquece o termo constante 10.</p>",
  figs(("q108", "Gráfico de tensão (V) em função da corrente (A): uma curva que começa na origem e sobe cada vez mais inclinada, até 7 A e cerca de 120 V."),
       ("q108a", "Alternativa A: reta horizontal em R = 10 Ω, de 0 a 7 A."),
       ("q108b", "Alternativa B: reta horizontal em R ≈ 17 Ω, de 0 a 7 A."),
       ("q108c", "Alternativa C: reta que sai da origem e chega a R = 7 Ω em i = 7 A."),
       ("q108d", "Alternativa D: reta que começa em R = 10 Ω para i = 0 e chega a cerca de 17 Ω em i = 7 A."),
       ("q108e", "Alternativa E: curva que começa em R = 10 Ω e sobe cada vez mais rápido, chegando a cerca de 60 Ω em i = 7 A.")),
  ["resistência elétrica", "resistor não ôhmico"],
  enun=p(T(108, 0).replace("versus", "<em>versus</em>")) + "[[fig:1]]" + p("Após a análise do gráfico, ele concluiu que a tensão em função da corrente é dada pela equação <em>V</em> = 10 <em>i</em> + <em>i</em><sup>2</sup>.", "O gráfico da resistência elétrica (<em>R</em>) do resistor em função da corrente (<em>i</em>) é"), alts=ALT(2))
X(109, "Química", "Reações orgânicas", "<p>O produto A, muito favorecido, mostra que a hidroxilamina ataca o anidrido pelo oxigênio do grupo OH, que depois perde o hidrogênio; o ataque pelo nitrogênio (produto B) é bem menos importante. Para reagir, a molécula precisa ter um OH livre ou, na falta dele, um nitrogênio com hidrogênio. A molécula <strong>4</strong> não tem nenhum dos dois: o oxigênio está ligado a um metil e o nitrogênio a dois metis. Alternativa <strong>D</strong>.</p><p>As moléculas 1, 3 e 5 têm OH livre; a 2 tem o grupo NH<sub>2</sub>.</p>",
  figs(("q109", "Reação do anidrido acético com NH₂OH, que forma dois conjuntos de produtos: produto A, ácido acético mais o composto em que o grupo acetil está ligado ao oxigênio, O–NH₂; e produto B, ácido acético mais o composto em que o acetil está ligado ao nitrogênio, NH–OH."),
       ("q109b", "Moléculas testadas: 1, HO–NH–CH₃; 2, CH₃–O–NH₂; 3, HO–NH–CH₂CH₃; 4, CH₃–O–N(CH₃)₂; 5, HO–N(CH₃)₂.")),
  ["substituição nucleofílica", "hidroxilamina"],
  enun=p(CH(T(109, 0))) + "[[fig:1]]" + p(T(109, 4).replace("fator de 105", "fator de 10<sup>5</sup>").replace("móleculas", "moléculas")) + "[[fig:2]]" + p(T(109, 6)))
X(110, "Biologia", "Genética", "<p>O estudante confundiu código genético com genoma. Cientificamente, o código genético é a correspondência entre as <strong>trincas de nucleotídeos (códons) e os aminoácidos</strong> que elas codificam, praticamente igual em todos os seres vivos. Alternativa <strong>A</strong>.</p><p>Localização de genes e conjunto das sequências (B e E) descrevem o genoma ou seu mapeamento.</p>",
  tags=["código genético", "genoma"])
X(111, "Biologia", "Botânica", "<p>O vento espalha o pólen ao acaso, e a maior parte se perde. As plantas polinizadas pelo vento compensam produzindo muito pólen, o que se consegue com o <strong>aumento do número de estames</strong>. Alternativa <strong>E</strong>.</p><p>Néctar e pétalas coloridas (C e D) atraem animais, inúteis para quem depende do vento.</p>",
  tags=["anemofilia", "polinização"])
X(112, "Física", "Eletrodinâmica", "<p>No circuito, os dois resistores de cima (4 kΩ cada) estão ligados à fonte. O toque em A fecha o contato no ramo da direita: os dois resistores de cima ficam em paralelo, e o conjunto fica em série com o resistor de 4 kΩ de baixo à esquerda, que leva de volta à fonte. O ramo que passa por B continua aberto.</p><p>R = (4 × 4) ÷ (4 + 4) + 4 = 2 + 4 = <strong>6,0 kΩ</strong>. Alternativa <strong>C</strong>.</p>",
  figs(("q112", "Esquema de uma tela resistiva tocada por um dedo e do circuito equivalente: uma fonte ε ligada a quatro resistores de 4 kΩ, dois em cima e dois embaixo; à direita, os pontos A e B, onde o circuito pode ser fechado pelo toque.")),
  ["associação de resistores", "tela resistiva"],
  enun=p(T(112, 0).replace("smartphones", "<em>smartphones</em>").replace("tablets", "<em>tablets</em>").replace("que A e B", "que <strong>A</strong> e <strong>B</strong>")) + "[[fig:1]]" + p(T(112, 4).replace("ponto A?", "ponto <strong>A</strong>?")))
X(113, "Biologia", "Biotecnologia", "<p>As leveduras modificadas produzem peroxidases, que degradam os peróxidos usados no clareamento. Assim, a água que sai da lavagem leva menos substâncias nocivas: o objetivo é <strong>reduzir a quantidade de resíduos tóxicos nos efluentes da lavagem</strong>. Alternativa <strong>A</strong>.</p><p>As enzimas destroem os peróxidos, por isso não aumentam o clareamento (C).</p>",
  tags=["peroxidase", "organismos geneticamente modificados"], trocas=[("fabricam jeans", "fabricam <em>jeans</em>"), ("lavagem dos jeans", "lavagem dos <em>jeans</em>")],
  alts={**D[113]["alternativas"], "C": "elevar a capacidade de clareamento dos <em>jeans</em>.", "D": "aumentar a resistência do <em>jeans</em> a peróxidos."})
X(114, "Química", "Termoquímica", "<p>Massa molar da glicose: 6 × 12 + 12 × 1 + 6 × 16 = 180 g/mol.</p><p>1 mol (180 g) libera 2 800 kJ; 1 g libera 2 800 ÷ 180 ≈ 15,6 kJ. Para a atividade muscular vão 40%: 0,4 × 15,6 ≈ <strong>6,2 kJ</strong>. Alternativa <strong>A</strong>.</p><p>15,6 kJ (B) é a energia total, sem descontar os 60% que não vão para os músculos.</p>",
  tags=["entalpia", "glicose"],
  enun=p(T(114, 0)) + '<p class="apoio">C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> (s) + 6 O<sub>2</sub> (g) → 6 CO<sub>2</sub> (g) + 6 H<sub>2</sub>O (l) &nbsp; Δ<sub>c</sub><em>H</em> = −2 800 kJ</p>' + ap("Considere as massas molares (em g mol<sup>−1</sup>): H = 1; C = 12; O = 16.") + fonte(T(114, 3)) + p(T(114, 4)))
X(115, "Física", "Eletrodinâmica", "<p>P = U × i = 600 V × 2 A = 1 200 W. O equipamento com essa potência é a <strong>churrasqueira elétrica</strong>. Alternativa <strong>D</strong>.</p><p>O exaustor (150 W), o computador (300 W) e o aspirador (600 W) ficam abaixo, e a secadora (3 600 W), três vezes acima.</p>",
  tags=["potência elétrica"],
  enun=p(T(115, 0), T(115, 1)) + tabela(["Equipamento elétrico", "Potência aproximada (watt)"], [["Exaustor", "150"], ["Computador", "300"], ["Aspirador de pó", "600"], ["Churrasqueira elétrica", "1 200"], ["Secadora de roupas", "3 600"]]) + p(T(115, 3)))
X(116, "Química", "Eletroquímica", "<p>Na reação 2, o corante excitado perde um elétron e fica oxidado (S<sup>+</sup>). Na reação 3, o íon iodeto (I<sup>−</sup>) doa elétrons ao corante, que volta à forma S e pode absorver luz de novo. Sem essa etapa, o corante se esgotaria. A reação 3 <strong>regenera o corante</strong>. Alternativa <strong>B</strong>.</p><p>Na reação 3, o I<sup>−</sup> é oxidado a I<sub>3</sub><sup>−</sup>, não reduzido (A), e o corante é reduzido, não oxidado (D).</p>",
  figs(("q116", "Esquema da célula solar: a luz (hν) atinge o eletrodo de TiO₂ com corante; elétrons saem do corante excitado para o TiO₂, percorrem o circuito externo até o eletrodo de platina e voltam pelo mediador de carga (I₃⁻/I⁻). Ao lado, as reações: (1) TiO₂|S + hν → TiO₂|S*; (2) TiO₂|S* → TiO₂|S⁺ + e⁻; (3) TiO₂|S⁺ + 3/2 I⁻ → TiO₂|S + 1/2 I₃⁻; (4) 1/2 I₃⁻ + e⁻ → 3/2 I⁻.")),
  ["célula solar", "oxirredução"],
  enun=p(CH(T(116, 0)).replace("(hν)", "(<em>hν</em>)")) + "[[fig:1]]" + fonte(T(116, 3).replace("hv e− e− e− e− ", "")) + p(T(116, 4)),
  alts={"A": "reduz íons I<sup>−</sup> a I<sub>3</sub><sup>−</sup>.", "B": "regenera o corante.", "C": "garante que a reação 4 ocorra.", "D": "promove a oxidação do corante.", "E": "transfere elétrons para o eletrodo de TiO<sub>2</sub>."})
X(117, "Biologia", "Citologia", "<p>Células que produzem muita proteína têm muitas mitocôndrias (energia), retículo endoplasmático rugoso desenvolvido (síntese das proteínas), nucléolo grande (produção de ribossomos) e cromatina descondensada, a eucromatina (genes sendo transcritos). A linhagem <strong>IV</strong> reúne essas características. Alternativa <strong>D</strong>.</p><p>Linhagens com pouca organela e muita heterocromatina (I e V) têm metabolismo baixo.</p>",
  figs(("q117", "Legenda com uma célula mostrando mitocôndria, retículo endoplasmático rugoso, heterocromatina, eucromatina e nucléolo. Abaixo, cinco linhagens, de I a V, desenhadas com quantidades diferentes de mitocôndrias e de retículo endoplasmático rugoso, e com núcleos de aspecto diferente (mais ou menos heterocromatina, nucléolo maior ou menor). A linhagem IV é a que tem mais organelas, nucléolo grande e núcleo claro, de eucromatina.")),
  ["organelas", "síntese de proteínas"], alts={"A": "I", "B": "II", "C": "III", "D": "IV", "E": "V"})
X(118, "Física", "Termologia", "<p>No gráfico, a curva de energia é assimétrica: com o aumento da temperatura (de T<sub>1</sub> a T<sub>4</sub>), os átomos oscilam com mais energia, e o ponto médio de cada oscilação (círculos) se desloca para distâncias maiores. Os átomos ficam, em média, mais afastados: é a <strong>dilatação</strong> térmica. Alternativa <strong>B</strong>.</p><p>As ligações continuam existindo (C, D e E); só aumenta a distância média.</p>",
  figs(("q118", "Gráfico da energia de ligação em função da distância interatômica: uma curva em forma de poço, com mínimo em R₀ para T = 0 K. Segmentos horizontais em T₁, T₂, T₃ e T₄, cada vez mais altos, têm seus pontos médios marcados por círculos que se deslocam para a direita.")),
  ["dilatação térmica", "energia potencial"],
  enun=p(T(118, 0).replace("(R0)", "(<em>R</em><sub>0</sub>)").replace("T1 a T4", "<em>T</em><sub>1</sub> a <em>T</em><sub>4</sub>")) + "[[fig:1]]" + p(T(118, 3)))
X(119, "Biologia", "Parasitologia", "<p>Produtos que combatem insetos ajudam a controlar doenças transmitidas por insetos vetores. Das opções, só a <strong>leishmaniose</strong> tem vetor inseto: o mosquito-palha (flebotomíneo). Alternativa <strong>C</strong>.</p><p>A esquistossomose é transmitida por caramujo (A), a leptospirose pela urina de ratos (B), e a hanseníase e a aids, de pessoa para pessoa (D e E).</p>",
  tags=["vetores", "leishmaniose"])
X(120, "Física", "Ondulatória", "<p>Com a polaridade invertida, o cone do alto-falante D se move para trás quando o de E se move para frente: as duas caixas emitem ondas iguais, mas em oposição de fase. Nos pontos à mesma distância das duas caixas, as ondas se anulam. O alto-falante E <strong>emite ondas sonoras em oposição de fase às emitidas pelo alto-falante D provocando o fenômeno de interferência destrutiva nos pontos equidistantes aos alto-falantes</strong>. Alternativa <strong>E</strong>.</p><p>A frequência não muda (B e C), e não há curto-circuito (A).</p>",
  figs(("q120a", "Polaridade correta: as saídas E e D do equipamento, cada uma com terminais + e −, ligadas às caixas de som E e D com + no + e − no −."),
       ("q120b", "Polaridade invertida: a caixa E ligada corretamente; na caixa D, os fios estão cruzados, com o + da saída no − da caixa e vice-versa.")),
  ["interferência", "fase"], enun=p(T(120, 0)) + "[[fig:1]][[fig:2]]" + p(T(120, 6).replace("alto-falantes E e D", "alto-falantes <strong>E</strong> e <strong>D</strong>")),
  alts={k: v.replace("alto-falante E", "alto-falante <strong>E</strong>").replace("alto-falante D", "alto-falante <strong>D</strong>").replace("alto- -falante D", "alto-falante <strong>D</strong>").replace("o D entra", "o <strong>D</strong> entra") for k, v in D[120]["alternativas"].items()})
X(121, "Química", "Equilíbrio químico", "<p>O calcário (CaCO<sub>3</sub>) é um sal básico: o carbonato reage com H<sup>+</sup> e o pH do solo sobe. Em meio menos ácido, o alumínio forma Al(OH)<sub>3</sub>, insolúvel, e deixa de ficar disponível para as plantas. A calagem promove o <strong>aumento da sua alcalinidade, tornando os íons alumínio menos disponíveis</strong>. Alternativa <strong>E</strong>.</p><p>O pH aumenta, não diminui (A), e não se forma alumínio metálico nem liga (C e D).</p>",
  tags=["calagem", "pH do solo"], trocas=[("calcário (CaCO3)", "calcário (CaCO<sub>3</sub>)")])
X(122, "Física", "Cinemática", "<p>A roda maior levanta o carro: o centro de massa sobe e o veículo fica mais instável. Além disso, o velocímetro mede a velocidade pelo número de voltas da roda: a cada volta, a roda maior percorre uma distância maior, então o carro anda mais rápido do que o velocímetro indica. Alternativa <strong>A</strong>.</p><p>A roda maior nunca abaixa o centro de massa (B e D), e um centro de massa mais alto não deixa o carro mais estável (C e E).</p>",
  tags=["centro de massa", "velocidade angular"])
X(123, "Biologia", "Metabolismo energético", "<p>No ciclo, o processo 1 transforma CO<sub>2</sub> e H<sub>2</sub>O em combustíveis reduzidos e O<sub>2</sub>: é a fotossíntese, que usa a luz do Sol para produzir glicose. A formação de combustíveis converte energia <strong>eletromagnética em química</strong>. Alternativa <strong>E</strong>.</p><p>O processo 2, a respiração, faz o caminho inverso, de energia química em outras formas (B).</p>",
  figs(("q123", "Ciclo com quatro caixas ligadas por setas: “CO₂ e H₂O” leva ao “Processo 1”, que leva a “Combustíveis reduzidos e O₂”, que leva ao “Processo 2”, que volta a “CO₂ e H₂O”.")),
  ["fotossíntese", "transformação de energia"])
X(124, "Química", "Petróleo", "<p>O craqueamento quebra moléculas grandes do petróleo, de pouco valor comercial, em moléculas menores, como as da gasolina e do GLP. Ocorre a <strong>transformação das frações do petróleo em outras moléculas menores</strong>. Alternativa <strong>A</strong>.</p><p>Separar por temperatura de ebulição (E) é a destilação fracionada, outro processo.</p>",
  tags=["craqueamento", "petróleo"])
X(125, "Física", "Óptica", "<p>O índice de refração cresce com a frequência: o azul (maior frequência) é o mais desviado pelo prisma, e o vermelho, o menos. Depois da reflexão no espelho, os raios se cruzam e a ordem se inverte no filme. Seguindo os raios da figura, de baixo para cima, as cores são <strong>vermelha, verde, azul</strong>. Alternativa <strong>A</strong>.</p>",
  figs(("q125", "No alto, uma faixa do espectro de 400 a 750 nm, com violeta, azul, verde, amarelo, laranja e vermelho. Embaixo, um feixe incidente atinge a face A de um prisma, sai pela face B separado em três raios, que se refletem num espelho horizontal e chegam a um filme vertical.")),
  ["dispersão da luz", "refração"], enun=p(T(125, 0)) + "[[fig:1]]" + p(T(125, 5)))
X(126, "Química", "Química orgânica", "<p>O texto descreve um tensoativo aniônico com vários carbonos terciários na cadeia hidrofóbica, isto é, uma cadeia ramificada. A alternativa B é o alquilbenzenossulfonato ramificado: tem o grupo SO<sub>3</sub><sup>−</sup> Na<sup>+</sup> (aniônico) e uma cadeia cheia de ramificações. Alternativa <strong>B</strong>.</p><p>A C também é aniônica, mas tem cadeia linear, a versão biodegradável. A é não iônica, e D e E são catiônicas.</p>",
  figs(("q126a", "Alternativa A: cadeia de 15 grupos CH₂ ligada a 20 unidades de óxido de etileno, terminando em OH."),
       ("q126b", "Alternativa B: anel benzênico com SO₃⁻ Na⁺ ligado a uma cadeia carbônica ramificada, com vários grupos metila."),
       ("q126c", "Alternativa C: anel benzênico com SO₃⁻ Na⁺ ligado a uma cadeia carbônica linear e longa."),
       ("q126d", "Alternativa D: cadeia carbônica linear e longa ligada a um nitrogênio com três metilas e carga positiva, com o contraíon Cl⁻."),
       ("q126e", "Alternativa E: cadeia carbônica ramificada ligada ao nitrogênio positivo de um anel piridínico, com o contraíon Cl⁻.")),
  ["tensoativos", "biodegradabilidade"], enun=p(T(126, 0)) + fonte(T(126, 1)) + p(T(126, 2)), alts=ALT(1))
X(127, "Biologia", "Genética", "<p>Em cada loco, a semente recebe um alelo da matriz e outro do pai. No loco A, a matriz tem os alelos 1 e 3, e S1 tem 1 e 2: o alelo 2 veio do pai. No loco B, a matriz tem 3 e 4, e S1 só tem o 3: o pai também passou o alelo 3. A única doadora com o alelo 2 no loco A e o alelo 3 no loco B é a <strong>DP5</strong>. Alternativa <strong>E</strong>.</p><p>DP2 também tem o alelo 2 no loco A, mas não tem o 3 no loco B.</p>",
  figs(("q127", "Esquema de dois géis com as bandas de DNA da matriz (M), da semente (S1) e das doadoras DP1 a DP5. Gel 1, loco A: M tem alelos 1 e 3; S1, 1 e 2; DP1, 3; DP2, 2 e 3; DP3, 1; DP4, 3 e 4; DP5, 2. Gel 2, loco B: M tem alelos 3 e 4; S1, 3; DP1, 2 e 4; DP2, 2 e 5; DP3, 1 e 5; DP4, 5; DP5, 3.")),
  ["marcadores moleculares", "paternidade"],
  enun=p(T(127, 0)) + "[[fig:1]]" + fonte("COLLEVATTI, R. G.; TELLES, M. P.; SOARES, T. N. Dispersão do pólen entre pequizeiros: uma atividade para a genética do ensino superior. <strong>Genética na Escola</strong>, n. 1, 2013 (adaptado).") + p(T(127, 6)))
X(128, "Física", "Dinâmica", "<p>No carro B, a ventoinha empurra o ar para trás, e o carro vai para frente, como um ventilador-foguete. No carro A, o ar soprado contra a vela é a força interna; o que conta é para onde o ar sai. A vela parabólica devolve o ar para trás (para a esquerda), então o carro A também se move, para a direita, mas com perdas no choque do ar com a vela. Assim, 0 &lt; V<sub>A</sub> &lt; V<sub>B</sub>, e o carro A vai para a direita. Alternativa <strong>B</strong>.</p>",
  figs(("q128", "Carro A: uma ventoinha à esquerda sopra para a direita, contra uma vela curva de cartolina presa ao carro. Carro B: a ventoinha está virada ao contrário, soprando para a esquerda, para fora do carro, com a vela à direita.")),
  ["conservação da quantidade de movimento", "ação e reação"],
  enun=p(T(128, 0).replace("carros de plástico, A e B,", "carros de plástico, <strong>A</strong> e <strong>B</strong>,").replace("No carro B ", "No carro <strong>B</strong> ").replace("montagem do carro A ", "montagem do carro <strong>A</strong> ")) + "[[fig:1]]" + p(T(128, 4).replace("(VA)", "(<em>V</em><sub>A</sub>)").replace("(VB)", "(<em>V</em><sub>B</sub>)")),
  alts={"A": "<em>V</em><sub>A</sub> = 0; <em>V</em><sub>B</sub> &gt; 0; o carro <strong>A</strong> não se move.", "B": "0 &lt; <em>V</em><sub>A</sub> &lt; <em>V</em><sub>B</sub>; o carro <strong>A</strong> se move para a direita.", "C": "0 &lt; <em>V</em><sub>A</sub> &lt; <em>V</em><sub>B</sub>; o carro <strong>A</strong> se move para a esquerda.", "D": "0 &lt; <em>V</em><sub>B</sub> &lt; <em>V</em><sub>A</sub>; o carro <strong>A</strong> se move para a direita.", "E": "0 &lt; <em>V</em><sub>B</sub> &lt; <em>V</em><sub>A</sub>; o carro <strong>A</strong> se move para a esquerda."})
X(129, "Biologia", "Fisiologia humana", "<p>Pelo gráfico, o pigmento “vermelho” é ativado cerca de 75% tanto em 530 nm quanto em 600 nm, e o “azul” não responde a nenhuma das duas. O que diferencia as cores, para uma pessoa normal, é o “verde”: máximo em 530 nm e baixo em 600 nm. Sem ele, as duas luzes produzem o mesmo estímulo, e a pessoa não consegue <strong>distinguir os dois comprimentos de onda, pois ambos estimulam o pigmento “vermelho” na mesma intensidade</strong>. Alternativa <strong>E</strong>.</p><p>Ela enxerga as duas luzes (B e C), só não as diferencia.</p>",
  figs(("q129", "Gráfico da ativação (%) dos pigmentos “azul”, “verde” e “vermelho” em função do comprimento de onda, de 400 a 650 nm. O “azul” tem pico perto de 420 nm; o “verde”, perto de 530 nm; o “vermelho”, perto de 560 nm. O retângulo I marca 530 nm e o retângulo II, 600 nm; nas duas faixas, a curva do “vermelho” está em cerca de 75%.")),
  ["visão", "daltonismo"], enun=p(T(129, 0)) + "[[fig:1]]" + fonte(T(129, 6)) + p(T(129, 7)))
X(130, "Química", "Hibridação", "<p>No grafeno, cada carbono está ligado a outros três, no mesmo plano, formando hexágonos, com ângulos de 120°. Três ligações σ e uma ligação π: hibridação <strong>sp<sup>2</sup> de geometria trigonal planar</strong>, como no grafite. Alternativa <strong>B</strong>.</p>",
  figs(("q130", "Estrutura do grafeno: átomos de carbono, representados por esferas, ligados em hexágonos lado a lado, formando uma folha plana como uma colmeia.")),
  ["grafeno", "alotropia"],
  alts={"A": "<em>sp</em> de geometria linear.", "B": "<em>sp</em><sup>2</sup> de geometria trigonal planar.", "C": "<em>sp</em><sup>3</sup> alternados com carbonos com hibridação <em>sp</em> de geometria linear.", "D": "<em>sp</em><sup>3</sup><em>d</em> de geometria planar.", "E": "<em>sp</em><sup>3</sup><em>d</em><sup>2</sup> com geometria hexagonal planar."})
X(131, "Física", "Energia", "<p>Sem atrito, a energia elástica vira cinética: kx²/2 = mv²/2, então v = x√(k/m). A velocidade é proporcional à deformação. Para quadruplicar v, mantendo a mola, basta <strong>aumentar quatro vezes a deformação</strong>. Alternativa <strong>B</strong>.</p><p>Trocando a mola, seria preciso uma constante 16 vezes maior, porque v depende da raiz de k (D e E).</p>",
  figs(("q131", "Um trilho horizontal com uma mola comprimida em uma das pontas, empurrando um pequeno cubo.")),
  ["energia potencial elástica", "conservação de energia"])
X(132, "Química", "Isomeria", "<p>Os dois ácidos têm 10 carbonos, uma dupla na posição 2, um grupo carboxila e uma hidroxila. A diferença é só a posição da hidroxila: carbono 9 na rainha e carbono 10 na operária. São isômeros de posição, com a mesma fórmula molecular e <strong>fórmula estrutural</strong> diferente. Alternativa <strong>A</strong>.</p><p>O número de carbonos, os tipos de ligação e os grupos funcionais são os mesmos (C, D e E).</p>",
  tags=["isomeria de posição", "feromônios"])
X(133, "Biologia", "Zoologia", "<p>Na holometabolia, larva e adulto são muito diferentes e vivem e se alimentam em ambientes distintos (a lagarta come folhas, a borboleta bebe néctar). Sem competir com os adultos da própria espécie, as larvas exploram outros recursos. A vantagem é a <strong>exploração de diferentes nichos, evitando a competição entre as fases da vida</strong>. Alternativa <strong>C</strong>.</p><p>Na pupa, o inseto não se alimenta (D), e o alimento muda entre as fases (E).</p>",
  tags=["metamorfose", "nicho ecológico"])
X(134, "Física", "Hidrostática", "<p>Ao sugar, a pessoa reduz a pressão na boca, e a pressão atmosférica sobre o suco o empurra canudo acima. Com um canudo fora do líquido, o ar entra por ele e a pressão na boca não cai: <strong>a pressão no interior da boca assume praticamente o mesmo valor daquela que atua sobre o suco</strong>. Sem diferença de pressão, o suco não sobe. Alternativa <strong>E</strong>.</p>",
  tags=["pressão atmosférica", "canudo"])
X(135, "Química", "Ciclo do nitrogênio", "<p>Haber diz que, na economia agrícola, o nitrogênio voltava ao solo; com a era industrial, os produtos da colheita são levados “para lugares distantes, onde são consumidos”, e o nitrogênio não retorna à terra. Isso acompanha a urbanização: <strong>a intensificação no fluxo de pessoas do campo para as cidades</strong>. Alternativa <strong>D</strong>.</p><p>O esgotamento do salitre (A) é uma consequência futura, não a causa do desequilíbrio.</p>",
  tags=["Fritz Haber", "fertilizantes"], trocas=[("da amônia (NH3)", "da amônia (NH<sub>3</sub>)")])

completar(Q, R)
