# Enem 2014, 1º dia, caderno azul: Ciências da Natureza (questões 46 a 90; no site, 1 a 45). Em 2014 a Natureza era no 1º dia.
# Texto legível. Quadros das Q54, 59, 61, 79, 83 e 90 e equações da Q88 em HTML. Alternativas-imagem: Q64 e 65.
# Sem anuladas nesta área.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, paragrafos_enem

ID = "enem-2014-natureza"
META = {"id": ID, "banca": "Enem", "ano": 2014, "titulo": "Enem 2014: Ciências da Natureza", "fonte": "Inep", "dataExame": "2014-11-08",
        "duracaoMinutos": 150, "area": "Ciências da Natureza", "caderno": "azul", "dia": 1}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2014-dia1-azul")
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


X(46, "Física", "Oscilações", "<p>O período de um pêndulo simples, para pequenas oscilações, é \\(T = 2\\pi\\sqrt{L/g}\\): depende só do comprimento e da gravidade, e não da massa nem da amplitude. Com <em>g</em> constante, o relógio só marca o tempo certo se o <strong>comprimento da haste for mantido constante</strong>; por isso se usou uma liga que quase não dilata com a temperatura. Alternativa <strong>A</strong>.</p><p>A massa (B) e a amplitude (D) não alteram o período nas pequenas oscilações.</p>",
  tags=["pêndulo", "dilatação térmica"], trocas=[("Unrolling Time: Christiaan Huygens and the mathematization of nature", "<em>Unrolling Time: Christiaan Huygens and the mathematization of nature</em>")])
X(47, "Biologia", "Nutrição", "<p>Sem carne, ovos e leite, a dieta perde a principal fonte de proteínas completas. Arroz e feijão juntos fornecem os <strong>aminoácidos essenciais</strong>, que o corpo não produz e precisa obter dos alimentos. Alternativa <strong>D</strong>.</p><p>Aminoácidos “naturais” (C) não é uma categoria nutricional; o que importa é se o organismo consegue ou não sintetizá-los.</p>",
  tags=["aminoácidos essenciais", "proteínas"], trocas=[("O Hoje", "<em>O Hoje</em>")])
X(48, "Química", "Química ambiental", "<p>O esquema mostra a radiação ultravioleta quebrando o CFC e liberando um átomo de cloro. O cloro reage com o O<sub>3</sub> formando ClO e O<sub>2</sub>; o ClO reage com um átomo de O, forma O<sub>2</sub> e devolve o cloro, que volta a atacar outro ozônio. O cloro é um catalisador: há <strong>produção de oxigênio molecular a partir de ozônio, catalisada por átomos de cloro</strong>. Alternativa <strong>B</strong>.</p><p>O CFC não reage diretamente com o ozônio (D): é a luz que o quebra antes.</p>",
  figs(("q48", "Esquema do ciclo de destruição do ozônio: a luz do Sol (hν) quebra uma molécula de CFC e libera um átomo de cloro, que reage com moléculas de ozônio formando monóxido de cloro e oxigênio; o monóxido de cloro reage com um átomo de oxigênio e devolve o cloro. Legenda: C, F, Cl e O.")),
  ["camada de ozônio", "catálise"], enun=ap(T(48, 0).replace("(O3)", "(O<sub>3</sub>)")) + "[[fig:1]]" + p(T(48, 3)))
X(49, "Biologia", "Ecologia", "<p>Nos aterros sanitários, o lixo orgânico fica enterrado sem oxigênio e é decomposto por bactérias anaeróbias, que liberam biogás, rico em <strong>gás metano</strong>. Ele pode ser queimado para gerar energia, e evitar sua liberação rende créditos de carbono. Alternativa <strong>D</strong>.</p><p>O gás natural (B) é de origem fóssil, e o etanol (A) vem da fermentação de açúcares, não do lixo dos aterros.</p>",
  tags=["biogás", "decomposição anaeróbia"])
X(50, "Física", "Óptica", "<p>A luz tem verde em excesso, então o filtro deve barrar o verde e deixar passar o vermelho e o azul. O filtro que transmite vermelho + azul é o <strong>magenta</strong>. Alternativa <strong>D</strong>.</p><p>Ciano e amarelo (A e C) deixam passar o verde.</p>",
  tags=["cores-luz", "filtros"])
X(51, "Química", "Química ambiental", "<p>O carvão ativo é muito poroso e tem uma enorme superfície, onde as moléculas orgânicas ficam adsorvidas. A <strong>filtração com filtros de carvão ativo</strong> remove o clorofórmio e outros compostos orgânicos dissolvidos. Alternativa <strong>A</strong>.</p><p>Coagulação e floculação (C e E) removem partículas em suspensão, e não substâncias dissolvidas.</p>",
  tags=["tratamento de água", "adsorção"],
  enun=ap(T(51, 0), T(51, 1), T(51, 2) + " " + T(51, 3).replace("(CHCl3)", "(CHCl<sub>3</sub>)")) + fonte(T(51, 4).replace("Química ambiental", "<em>Química ambiental</em>")) + p(T(51, 5)))
X(52, "Química", "Isomeria", "<p>Enantiômeros têm as mesmas propriedades físicas e químicas comuns, mas são imagens especulares, e as moléculas do organismo (enzimas, receptores) também são quirais. Por isso cada enantiômero se encaixa de um jeito: os enantiômeros <strong>interagem de maneira distinta com o organismo</strong>. Alternativa <strong>D</strong>.</p><p>A mistura racêmica tem partes iguais dos dois (C), e os grupos funcionais são os mesmos (E).</p>",
  tags=["quiralidade", "talidomida"])
X(53, "Biologia", "Evolução", "<p>Para a biologia, evolução não significa progresso nem melhoria: é a mudança das populações ao longo das gerações. Os seres vivos passam por <strong>modificação de características</strong>, e a espécie humana não é o “ápice” de nada. Alternativa <strong>A</strong>.</p><p>As demais opções supõem uma direção ou finalidade (melhoria, complexidade, especialização), ideia que o texto rejeita.</p>",
  tags=["evolução", "senso comum"])
X(54, "Química", "Química orgânica", "<p>O texto diz que os ésteres saturados dão mais estabilidade frente à oxidação. Os ácidos saturados do quadro são o mirístico, o palmítico e o esteárico (o número depois dos dois-pontos é zero). Somando-os, a palma tem cerca de 1,0 + 42,8 + 4,5 = 48,3%, muito mais que as outras. A fonte é a <strong>palma</strong>. Alternativa <strong>B</strong>.</p><p>A canola (C) é rica em oleico e linolênico, insaturados, que se oxidam mais facilmente.</p>",
  tags=["biodiesel", "ácidos graxos saturados"],
  enun=ap(T(54, 0)) + tabela(["Fonte oleaginosa", "Mirístico (C14:0)", "Palmítico (C16:0)", "Esteárico (C18:0)", "Oleico (C18:1)", "Linoleico (C18:2)", "Linolênico (C18:3)"],
    [["Milho", "&lt; 0,1", "11,7", "1,9", "25,2", "60,6", "0,5"], ["Palma", "1,0", "42,8", "4,5", "40,5", "10,1", "0,2"], ["Canola", "&lt; 0,2", "3,5", "0,9", "64,4", "22,3", "8,2"],
     ["Algodão", "0,7", "20,1", "2,6", "19,2", "55,2", "0,6"], ["Amendoim", "&lt; 0,6", "11,4", "2,4", "48,3", "32,0", "0,9"]])
  + '<p class="apoio">Valores: teor médio do ácido graxo (% em massa).</p>' + fonte("MA, F.; HANNA, M. A. Biodiesel Production: a review. <em>Bioresource Technology</em>, Londres, v. 70, n. 1, jan. 1999 (adaptado).") + p(T(54, 5)))
X(55, "Física", "Hidrostática", "<p>A ducha fica 6 m abaixo do nível da água, então a pressão estática é de 6 mca. Pelo gráfico, a vazão nesse ponto é de 12 L/min. Cada banho gasta 8 × 12 = 96 L; por dia, 4 × 96 = 384 L; em 30 dias, 384 × 30 = <strong>11 520 L</strong>. Alternativa <strong>C</strong>.</p>",
  figs(("q55", "Gráfico da vazão (L/min) em função da pressão estática (mca), de 1 a 8 mca. A vazão cresce de cerca de 5 L/min a 1 mca para 9 L/min a 3 mca, 11 L/min a 5 mca, 12 L/min a 6 mca e 14 L/min a 8 mca.")),
  ["pressão hidrostática", "vazão"], enun=p(T(55, 0)) + "[[fig:1]]" + p(T(55, 3), T(55, 4)))
X(56, "Química", "Química ambiental", "<p>A emissão de SO<sub>3</sub> é proporcional ao teor de enxofre. Passar de 13 000 ppm para 50 ppm significa reduzir 12 950 ppm: \\(\\dfrac{12\\,950}{13\\,000} \\approx 0{,}996\\), ou seja, <strong>99,6%</strong>. Alternativa <strong>D</strong>.</p>",
  tags=["chuva ácida", "porcentagem"], trocas=[("emissão de SO3 de", "emissão de SO<sub>3</sub> de"), ("Os impactos da má qualidade do óleo diesel brasileiro", "<em>Os impactos da má qualidade do óleo diesel brasileiro</em>")])
X(57, "Física", "Eletrodinâmica", "<p>Seguindo os fios: as lâmpadas 1 e 3 estão sempre em paralelo entre si. Na posição A, a chave liga o gerador direto ao ponto depois delas, e a lâmpada 2 fica fora do circuito: a resistência equivalente é R/2, e a lâmpada 1 recebe a tensão inteira do gerador, U. Na posição B, a lâmpada 2 entra em série com o par 1–3: a resistência equivalente sobe para 3R/2, e a lâmpada 1 fica com só U/3. Com a <strong>resistência equivalente menor</strong> em A, a lâmpada 1 tem mais tensão e mais corrente e brilha mais. Alternativa <strong>C</strong>.</p><p>A tensão do gerador não muda com a chave (D), e a potência total é maior justamente em A, e não em B.</p>",
  figs(("q57", "Circuito com três lâmpadas iguais, 1, 2 e 3, marcadas com X, ligadas a um gerador G com polos + e −. Uma chave no gerador pode ligar na posição A ou na posição B, que conectam o circuito a pontos diferentes.")),
  ["associação de resistores", "potência"], enun=p(T(57, 0)) + "[[fig:1]]" + p(T(57, 8)))
X(58, "Química", "Química orgânica", "<p>O sabão é um sal de ácido graxo: tem uma longa cadeia de carbono, apolar, que interage com a gordura, e uma ponta iônica (COO<sup>−</sup>Na<sup>+</sup>), polar, que interage com a água. Entre as opções, só o <strong>C<sub>17</sub>H<sub>33</sub>COONa</strong> tem as duas partes. Alternativa <strong>B</strong>.</p><p>O CH<sub>3</sub>CH<sub>2</sub>COONa (C) tem cadeia curta demais para formar micelas.</p>",
  tags=["sabão", "micelas"], trocas=[("Química e sociedade", "<em>Química e sociedade</em>")],
  alts={k: SUB(v) for k, v in D[58]["alternativas"].items()})
X(59, "Química", "Eletroquímica", "<p>Para reduzir a prata a Ag metálica, é preciso uma espécie que se oxide com facilidade, ou seja, um metal com potencial de redução menor que o da prata (+0,02 V). As opções que são metais sólidos e podem se oxidar são Cu, Pt e Sn; só o Sn tem potencial menor (−0,14 V). A espécie adequada é <strong>Sn (s)</strong>. Alternativa <strong>D</strong>.</p><p>Al<sup>3+</sup> e Zn<sup>2+</sup> (C e E) já estão oxidados e não podem doar elétrons.</p>",
  tags=["potencial de redução", "pilhas"],
  enun=p("A revelação das chapas de raios X gera uma solução que contém íons prata na forma de Ag(S<sub>2</sub>O<sub>3</sub>)<sub>2</sub><sup>3−</sup>. Para evitar a descarga desse metal no ambiente, a recuperação de prata metálica pode ser feita tratando eletroquimicamente essa solução com uma espécie adequada. O quadro apresenta semirreações de redução de alguns íons metálicos.")
  + tabela(["Semirreação de redução", "<em>E</em>⁰ (V)"], [["Ag(S<sub>2</sub>O<sub>3</sub>)<sub>2</sub><sup>3−</sup> (aq) + e<sup>−</sup> ⇌ Ag (s) + 2 S<sub>2</sub>O<sub>3</sub><sup>2−</sup> (aq)", "+0,02"],
    ["Cu<sup>2+</sup> (aq) + 2 e<sup>−</sup> ⇌ Cu (s)", "+0,34"], ["Pt<sup>2+</sup> (aq) + 2 e<sup>−</sup> ⇌ Pt (s)", "+1,20"], ["Al<sup>3+</sup> (aq) + 3 e<sup>−</sup> ⇌ Al (s)", "−1,66"],
    ["Sn<sup>2+</sup> (aq) + 2 e<sup>−</sup> ⇌ Sn (s)", "−0,14"], ["Zn<sup>2+</sup> (aq) + 2 e<sup>−</sup> ⇌ Zn (s)", "−0,76"]])
  + fonte("BENDASSOLLI, J. A. et al. Procedimentos para a recuperação de Ag de resíduos líquidos e sólidos. <em>Química Nova</em>, v. 26, n. 4, 2003 (adaptado).") + p(T(59, 4)),
  alts={"A": "Cu (s).", "B": "Pt (s).", "C": "Al<sup>3+</sup> (aq).", "D": "Sn (s).", "E": "Zn<sup>2+</sup> (aq)."})
X(60, "Biologia", "Ecologia", "<p>Competição é a disputa entre organismos por um mesmo recurso limitado. As bactérias consomem o ferro do meio e deixam o fungo sem ele: há <strong>diminuição da quantidade de ferro disponível para o fungo</strong>. Alternativa <strong>C</strong>.</p><p>Liberar substâncias que inibem o outro (D) é amensalismo (antibiose), não competição.</p>",
  tags=["competição", "relações ecológicas"], trocas=[("Tropical Plant Pathology", "<em>Tropical Plant Pathology</em>")])
X(61, "Biologia", "Botânica", "<p>No Cerrado, o lençol freático é profundo e a seca é longa: a árvore precisa de <strong>raízes profundas</strong> para alcançar a água e de folhas que percam pouca água, como as cobertas de <strong>cera</strong>, que reduzem a transpiração e refletem a luz. A árvore 2 reúne as duas características. Alternativa <strong>B</strong>.</p><p>A árvore 5 também tem raízes profundas, mas espinhos não são o que protege do excesso de insolação.</p>",
  tags=["Cerrado", "adaptações das plantas"],
  enun=p(T(61, 0)) + tabela(["Característica", "Árvore 1", "Árvore 2", "Árvore 3", "Árvore 4", "Árvore 5"],
    [["Superfície foliar", "Coberta por tricomas", "Coberta por cera", "Coberta por cera", "Coberta por espinhos", "Coberta por espinhos"],
     ["Profundidade das raízes", "Baixa", "Alta", "Baixa", "Baixa", "Alta"]]) + p(T(61, 3)))
X(62, "Física", "Termodinâmica", "<p>Os gases recebem o mesmo calor, e o gás M eleva o objeto mais que o V. A pressão é a mesma (o peso do objeto não muda), então quem se expande mais é quem aquece mais. Para a mesma quantidade de calor, aquece mais o gás com <strong>menor capacidade calorífica</strong>. Alternativa <strong>E</strong>.</p><p>Como as quantidades são equimolares e a pressão é a mesma, a massa molecular (B) não muda o volume ocupado.</p>",
  figs(("q62", "À esquerda, um cilindro com um êmbolo que sustenta um objeto, um manômetro ligado ao cilindro e uma chapa de aquecimento embaixo; o êmbolo sobe uma altura Δh. À direita, um gráfico de Δh em função do calor fornecido com duas retas partindo da origem: a do gás M é mais inclinada que a do gás V.")),
  ["primeira lei da termodinâmica", "capacidade térmica"], enun=p(T(62, 0)) + "[[fig:1]]" + p(T(62, 6)))
X(63, "Química", "Ciclos biogeoquímicos", "<p>A forma mais oxidada do nitrogênio é o nitrato, NO<sub>3</sub><sup>−</sup> (número de oxidação +5). Na desnitrificação, bactérias o reduzem a N<sub>2</sub>, que volta para a atmosfera. No esquema, essa é a <strong>etapa V</strong>. Alternativa <strong>E</strong>.</p><p>A etapa I é a fixação (N<sub>2</sub> a NH<sub>3</sub>), e as etapas III e IV são a nitrificação.</p>",
  figs(("q63", "Esquema do ciclo do nitrogênio: N2 passa a NH3 (etapa I), NH3 a NH4+ (etapa II), NH4+ a NO2− (etapa III), NO2− a NO3− (etapa IV) e NO3− volta a N2 (etapa V).")),
  ["ciclo do nitrogênio", "desnitrificação"], enun=p(T(63, 0)) + "[[fig:1]]" + p(T(63, 9)))
X(64, "Física", "Quantidade de movimento", "<p>Numa colisão elástica entre esferas iguais, a quantidade de movimento e a energia se conservam: se três esferas batem, três esferas saem do outro lado com a mesma velocidade. As duas primeiras ficam paradas e as três últimas sobem para a direita, como mostra a <strong>figura C</strong>. Alternativa <strong>C</strong>.</p><p>Em D e E saem só duas ou uma esfera, o que não conserva ao mesmo tempo o momento e a energia.</p>",
  figs(("q64", "Pêndulo de Newton com cinco esferas: as três da esquerda afastadas para a esquerda e vindo para a direita; as duas da direita paradas."),
       ("q64a", "Alternativa A: duas esferas sobem para a esquerda, uma fica parada no centro e duas sobem para a direita."),
       ("q64b", "Alternativa B: duas esferas sobem para a esquerda e três sobem para a direita."),
       ("q64c", "Alternativa C: duas esferas ficam paradas à esquerda e três sobem para a direita."),
       ("q64d", "Alternativa D: três esferas ficam paradas e duas sobem para a direita."),
       ("q64e", "Alternativa E: quatro esferas ficam paradas e uma sobe para a direita.")),
  ["colisão elástica", "conservação do momento"], enun=p(T(64, 0)) + "[[fig:1]]" + p(T(64, 2)), alts=ALT(2))
X(65, "Química", "Química orgânica", "<p>Anéis aromáticos e anéis com ligações duplas, como o benzeno, o tiofeno e o ciclobutadieno, são planos, porque os carbonos com dupla têm geometria trigonal plana; o grupo aldeído também é plano. Já o cicloexano só tem carbonos com ligações simples (tetraédricos) e se dobra em forma de cadeira: é o grupo não planar, o <strong>cicloexil</strong>. Alternativa <strong>A</strong>.</p>",
  figs(("q65a", "Alternativa A: anel de seis carbonos só com ligações simples (cicloexano) ligado à cadeia."),
       ("q65b", "Alternativa B: anel de cinco átomos com enxofre e duas ligações duplas (tiofeno)."),
       ("q65c", "Alternativa C: anel de quatro carbonos com duas ligações duplas."),
       ("q65d", "Alternativa D: anel benzênico, representado com um círculo dentro do hexágono."),
       ("q65e", "Alternativa E: grupo aldeído, um carbono com dupla ligação com oxigênio e ligado a um hidrogênio.")),
  ["geometria molecular", "hibridização"], enun=p(T(65, 0), T(65, 1)), alts=ALT(1))
X(66, "Física", "Termodinâmica", "<p>Numa usina nuclear, depois de passar pelas turbinas o vapor precisa ser condensado para voltar ao ciclo, e para isso usa-se água de rios ou do mar, que é devolvida aquecida. A poluição térmica vem da <strong>condensação do vapor-d’água no final do processo</strong>. Alternativa <strong>B</strong>.</p><p>A fissão (A) aquece a água de um circuito fechado, sem contato com o ambiente.</p>",
  tags=["usina nuclear", "poluição térmica"])
X(67, "Física", "Leis de Newton", "<p>Sem atrito, a esfera sobe até a mesma altura de onde saiu. Se o plano de subida tiver ângulo zero, ela nunca alcança essa altura e continua indefinidamente: como nenhuma força horizontal atua, o impulso resultante é nulo e ela <strong>mantém sua velocidade constante</strong>. É o princípio da inércia. Alternativa <strong>A</strong>.</p><p>Não existe um “impulso da descida” que continue empurrando a esfera (B): o movimento se mantém sem força.</p>",
  figs(("q67", "Dois planos inclinados unidos pela base: a esfera é abandonada no alto de um deles e sobe pelo outro até uma linha tracejada na mesma altura, chamada “nível de abandono da esfera”. Estão marcados o ângulo do plano de descida e o ângulo do plano de subida.")),
  ["inércia", "Galileu"],
  enun=p(T(67, 0)) + "[[fig:1]]" + fonte("<em>Galileu e o plano inclinado</em>. Disponível em: www.fisica.ufpb.br. Acesso em: 21 ago. 2012 (adaptado).") + p(T(67, 3)))
X(68, "Física", "Óptica", "<p>A razão entre os senos é \\(\\dfrac{\\operatorname{sen} i}{\\operatorname{sen} r} = n\\). Com o ângulo de incidência fixo, se a razão aumentou de 1,4 para 1,9, então sen <em>r</em> diminuiu: o ângulo de refração ficou menor, e o raio <strong>se aproximou da normal</strong>. Alternativa <strong>E</strong>.</p><p>A reflexão total (B) só ocorre quando a luz passa de um meio mais refringente para um menos refringente, e aqui ela vem do ar.</p>",
  tags=["refração", "lei de Snell"])
X(69, "Biologia", "Biotecnologia", "<p>Os pesquisadores isolaram um gene de uma bactéria e o inseriram nas células de uma planta, que passou a ter DNA de outra espécie. Um organismo que recebe gene de outra espécie é <strong>transgênico</strong>. Alternativa <strong>E</strong>.</p><p>Um clone (A) é uma cópia genética de um organismo, e um híbrido (B) vem do cruzamento entre variedades ou espécies.</p>",
  figs(("q69", "Esquema em sete passos: 1, bactéria; 2, isolamento do DNA bacteriano; 3, clonagem do DNA; 4, extração do gene de interesse; 5, fabricação do gene; 6, inserção do gene nas células do tecido da planta; 7, planta.")),
  ["transgênicos", "DNA recombinante"],
  enun=p(T(69, 0), T(69, 1)) + "[[fig:1]]" + fonte("Disponível em: http://ciencia.hsw.uol.com.br. Acesso em: 22 nov. 2013 (adaptado).") + p(T(69, 7)))
X(70, "Química", "pH", "<p>Com [OH<sup>−</sup>] = 1,0 × 10<sup>−10</sup> mol/L, o pOH é 10 e o pH é 4: o resíduo é ácido demais e precisa ter o pH aumentado até pelo menos 5. É preciso uma substância de caráter básico. O K<sub>2</sub>CO<sub>3</sub> é um sal de base forte e ácido fraco, que, em água, deixa a solução básica. A resposta é o <strong>K<sub>2</sub>CO<sub>3</sub></strong>. Alternativa <strong>D</strong>.</p><p>O ácido acético e o NH<sub>4</sub>Cl (A e E) baixariam ainda mais o pH, e o Na<sub>2</sub>SO<sub>4</sub> e o metanol (B e C) são praticamente neutros.</p>",
  tags=["hidrólise salina", "pH e pOH"],
  enun=p(T(70, 0)) + p("Um resíduo líquido aquoso gerado em um processo industrial tem concentração de íons hidroxila igual a 1,0 × 10<sup>−10</sup> mol/L. Para atender a legislação, um químico separou as seguintes substâncias, disponibilizadas no almoxarifado da empresa: CH<sub>3</sub>COOH, Na<sub>2</sub>SO<sub>4</sub>, CH<sub>3</sub>OH, K<sub>2</sub>CO<sub>3</sub> e NH<sub>4</sub>Cl.") + p(T(70, 4)),
  alts={k: SUB(v) for k, v in D[70]["alternativas"].items()})
X(71, "Química", "Equilíbrio químico", "<p>O CO<sub>2</sub> dissolvido forma ácido carbônico, que libera H<sup>+</sup>. Esses íons reagem com o carbonato (CO<sub>3</sub><sup>2−</sup>), deslocando o equilíbrio para o bicarbonato, e falta carbonato para os corais formarem o esqueleto de CaCO<sub>3</sub>. O esquema fala em “conchas deformadas”: há <strong>dano à estrutura dos esqueletos calcários, diminuindo o tamanho das populações</strong>. Alternativa <strong>E</strong>.</p><p>O branqueamento (A) está ligado ao aquecimento da água, e não à acidificação mostrada no esquema.</p>",
  figs(("q71", "Esquema das reações no mar: o dióxido de carbono atmosférico (CO2) se dissolve na água, reage com ela formando ácido carbônico (H2CO3), que se separa em íons hidrogênio (H+) e íons bicarbonato (HCO3−); os íons hidrogênio reagem com os íons carbonato (CO3 2−). Uma barra de cores vai de “menos ácido” a “mais ácido”, e ao fundo aparecem conchas deformadas.")),
  ["acidificação dos oceanos", "corais"])
X(72, "Física", "Eletromagnetismo", "<p>Na figura, ímã e espira se afastam. O sentido da corrente induzida se inverte quando se troca o tipo de movimento relativo (afastar ou aproximar) e também quando se inverte a polaridade do ímã. Trocando as duas coisas ao mesmo tempo, as inversões se cancelam e a corrente mantém o sentido: mover a <strong>espira para a esquerda e o ímã para a direita com polaridade invertida</strong>, aproximando-os. Alternativa <strong>A</strong>.</p><p>Em B, eles continuam se afastando, mas com a polaridade invertida, o que inverte a corrente. Em C, os dois andam juntos para a esquerda e o movimento relativo some.</p>",
  figs(("q72", "Um ímã com polos S e N à esquerda, com velocidade v para a esquerda, e uma bobina à direita, com velocidade v para a direita; as linhas de campo B saem do polo N e atravessam a bobina, ligada a um amperímetro A; a corrente i indicada vai para a direita.")),
  ["indução eletromagnética", "lei de Lenz"], enun=p(T(72, 0)) + "[[fig:1]]" + p("A fim de se obter uma corrente com o mesmo sentido da apresentada na figura, utilizando os mesmos materiais, outra possibilidade é mover a espira para a"))
X(73, "Biologia", "Citologia", "<p>A teoria endossimbiótica diz que mitocôndrias e cloroplastos eram bactérias englobadas por outra célula. A evidência é que eles têm <strong>DNA circular próprio, semelhante ao bacteriano, e se autoduplicam</strong>, além de ribossomos parecidos com os das bactérias. Alternativa <strong>D</strong>.</p><p>Mitocôndrias não têm parede celular (B), e produzir ATP (A) não indica origem bacteriana.</p>",
  tags=["endossimbiose", "mitocôndria"])
X(74, "Biologia", "Genética", "<p>No heredograma, todos os homens afetados têm todas as filhas afetadas e nenhum filho afetado, e a doença aparece em todas as gerações. Isso indica herança <strong>dominante ligada ao X</strong>: o pai passa o X para todas as filhas e o Y para os filhos. Alternativa <strong>D</strong>.</p><p>Se fosse autossômica (A), homens afetados também teriam filhos homens afetados.</p>",
  figs(("q74", "Heredograma de três gerações com quadrados (homens) e círculos (mulheres); os símbolos preenchidos são afetados. Os homens afetados têm todas as filhas afetadas e todos os filhos homens normais; mulheres afetadas têm filhos e filhas afetados e normais.")),
  ["heredograma", "herança ligada ao X"], enun="[[fig:1]]" + p(T(74, 0), T(74, 1)))
X(75, "Biologia", "Fisiologia", "<p>Uma protease gástrica (a pepsina) digere proteínas em meio ácido. Para confirmar a hipótese, a enzima precisa agir num alimento proteico em pH ácido: o <strong>pedaço de carne em solução com pH = 5</strong>. Alternativa <strong>B</strong>.</p><p>A clara de ovo (C) é proteica, mas está em pH básico, onde a pepsina não age.</p>",
  tags=["enzimas digestivas", "pepsina"])
X(76, "Física", "Ondas", "<p>O corpo humano, a cerca de 37 °C, emite radiação térmica principalmente na faixa do <strong>infravermelho</strong>. É ela que os sensores de presença captam. Alternativa <strong>C</strong>.</p><p>O corpo não emite luz visível (A): só a reflete.</p>",
  tags=["espectro eletromagnético", "radiação térmica"])
X(77, "Química", "Química orgânica", "<p>A molécula precisa ser quiral (carbono com quatro ligantes diferentes), insaturada (com dupla), heterogênea (heteroátomo entre carbonos) e ramificada. A opção B tem dupla em CH=CH, o N entre carbonos em –CO–NH–CH<sub>3</sub>, a ramificação CH<sub>3</sub> e um carbono quiral, o CH(CH<sub>3</sub>), ligado a H, CH<sub>3</sub>, ao grupo vinil e à amida. Alternativa <strong>B</strong>.</p><p>A opção C não é heterogênea (o N fica na ponta, como NH<sub>2</sub>), e a D é saturada.</p>",
  tags=["quiralidade", "classificação de cadeias"], alts={k: SUB(v) for k, v in D[77]["alternativas"].items()})
X(78, "Química", "Polímeros", "<p>O amido é um carboidrato que fungos e bactérias conseguem digerir. Quando os decompositores consomem o amido, a resina fica cheia de buracos e se fragmenta em pedaços menores. Isso acontece porque os carboidratos <strong>são digeridos por organismos decompositores</strong>. Alternativa <strong>D</strong>.</p><p>O amido não se decompõe sozinho em contato com água e gás carbônico (E).</p>",
  tags=["plástico biodegradável", "amido"], trocas=[("Pesquisa Fapesp", "<em>Pesquisa Fapesp</em>")])
X(79, "Biologia", "Genética", "<p>Quem é do tipo A tem aglutinogênio A nas hemácias e aglutina só com o soro anti-A. No quadro, o único lote que aglutinou com anti-A e não com anti-B é o II, com <strong>25 litros</strong>. Alternativa <strong>B</strong>.</p><p>O lote III (30 L) aglutinou com os dois soros: é do tipo AB.</p>",
  tags=["sistema ABO", "tipagem sanguínea"],
  enun=p(T(79, 0)) + tabela(["Código dos lotes", "Volume de sangue (L)", "Soro anti-A", "Soro anti-B"],
    [["I", "22", "Não aglutinou", "Aglutinou"], ["II", "25", "Aglutinou", "Não aglutinou"], ["III", "30", "Aglutinou", "Aglutinou"], ["IV", "15", "Não aglutinou", "Não aglutinou"], ["V", "33", "Não aglutinou", "Aglutinou"]]) + p(T(79, 3)))
X(80, "Química", "Separação de misturas", "<p>Fenol e acetona são líquidos miscíveis, com temperaturas de ebulição bem diferentes (a acetona ferve a cerca de 56 °C, e o fenol, a cerca de 182 °C). A mistura homogênea de líquidos é separada por <strong>destilação fracionada</strong>. Alternativa <strong>E</strong>.</p><p>Filtração e decantação (A e C) servem para misturas heterogêneas.</p>",
  figs(("q80", "Equação: cumeno + O2, com catalisador, forma hidroperóxido de cumila; este, com H2O/H2SO4, forma fenol + acetona. As moléculas aparecem em fórmula estrutural.")),
  ["destilação", "fenol e acetona"], enun=ap(T(80, 0)) + "[[fig:1]]" + p(T(80, 4)))
X(81, "Biologia", "Ecologia", "<p>A larva do parasitoide vive dentro da lagarta e come seus tecidos. A lagarta é herbívora (consumidor primário), então quem se alimenta dela é <strong>consumidor secundário</strong>. Alternativa <strong>B</strong>.</p><p>A larva mata um animal vivo, então não é decompositora (E).</p>",
  figs(("q81", "Ciclo de vida de um inseto parasitoide de lagartas: (A) a fêmea adulta põe ovos dentro de uma lagarta; (B) o ovo eclode e a larva se desenvolve dentro dela; (C) a larva vira pupa e mata o hospedeiro; (D) o parasitoide, após a metamorfose, cava um túnel nos tecidos do hospedeiro e emerge adulto.")),
  ["cadeia alimentar", "controle biológico"], trocas=[("Ciência Hoje", "<em>Ciência Hoje</em>")])
X(82, "Física", "Movimento circular", "<p>O coelhinho dá a volta na Terra com velocidade de módulo constante, como um satélite. Em movimento circular uniforme, a aceleração tangencial (que muda o módulo da velocidade) é <strong>nula</strong>; só existe a aceleração centrípeta, apontada para o centro. Alternativa <strong>A</strong>.</p><p>A opção D descreve a aceleração centrípeta, e não a tangencial.</p>",
  figs(("q82", "História em quadrinhos do Cebolinha. Ele chuta o coelhinho de pelúcia, que sai voando; o coelhinho dá uma volta inteira ao redor da Terra, vista do espaço; volta pelo outro lado e atinge o Cebolinha pelas costas, derrubando-o.")),
  ["movimento circular uniforme", "aceleração tangencial"], trocas=[("Cebolinha, n.", "<em>Cebolinha</em>, n.")])
X(83, "Química", "Soluções", "<p>Os limites são 30 mg/kg para o solo e 0,14 mg/L para a água. Em 500 g de solo, o limite é 15 mg = 1,5 × 10<sup>−2</sup> g; em 100 mL de água, 0,014 mg = 1,4 × 10<sup>−5</sup> g. O solo I (1,0 × 10<sup>−2</sup> g) está dentro do limite, o <strong>solo II</strong> (2,0 × 10<sup>−2</sup> g) está acima, e todas as águas estão abaixo. Alternativa <strong>B</strong>.</p>",
  tags=["concentração", "biorremediação"],
  enun=p(T(83, 0)) + tabela(["Ambiente", "Resíduo de naftaleno (g)"], [["Solo I", "1,0 × 10<sup>−2</sup>"], ["Solo II", "2,0 × 10<sup>−2</sup>"], ["Água I", "7,0 × 10<sup>−6</sup>"], ["Água II", "8,0 × 10<sup>−6</sup>"], ["Água III", "9,0 × 10<sup>−6</sup>"]]) + p(T(83, 2)))
X(84, "Física", "Ondas", "<p>O circuito do receptor tem uma frequência natural. Quando a onda que chega oscila nessa mesma frequência, a absorção de energia é máxima: é a <strong>ressonância</strong>. Sintonizar é ajustar a frequência natural do circuito à da estação. Alternativa <strong>E</strong>.</p>",
  tags=["ressonância", "rádio"])
X(85, "Biologia", "Imunologia", "<p>O imunobiológico I é aplicado numa pessoa e leva vírus ou bactérias (é uma vacina); o II é aplicado no cavalo, que depois produz o imunobiológico III, o soro. Tanto I quanto II levam antígenos ao organismo, que <strong>estimulam a produção de anticorpos</strong>. Alternativa <strong>D</strong>.</p><p>Quem confere imunidade passiva (A) é o soro, o imunobiológico III, que já traz os anticorpos prontos.</p>",
  figs(("q85", "Esquema “Imunobiológicos: diferentes formas de produção, diferentes aplicações”. Em A, uma profissional de saúde aplica numa mulher o imunobiológico I, feito com vírus ou bactérias. Em B, aplica-se o imunobiológico II, feito a partir do veneno de uma cobra, num cavalo; do sangue do cavalo se produz o imunobiológico III, que é aplicado numa pessoa picada por uma cobra.")),
  ["vacina", "soro"], enun="[[fig:1]]" + p(T(85, 5)))
X(86, "Química", "Ácidos e bases", "<p>A piridina tem caráter básico, pelo par de elétrons livre do nitrogênio. O ácido acético do vinagre reage com ela formando um sal, que não é volátil e não tem cheiro. É uma <strong>reação de neutralização entre o ácido acético e a piridina</strong>. Alternativa <strong>E</strong>.</p><p>O texto diz que os maus odores vêm de compostos alcalinos, então a piridina não tem caráter ácido (B).</p>",
  tags=["neutralização", "aminas"], trocas=[("(C5H5N)", "(C<sub>5</sub>H<sub>5</sub>N)"), ("Química Nova na Escola", "<em>Química Nova na Escola</em>")])
X(87, "Física", "Acústica", "<p>O que diferencia uma nota musical de outra (dó, ré, mi…) é a altura do som, que depende da <strong>frequência</strong> da onda. Quem tem ouvido absoluto reconhece a frequência de uma nota isolada. Alternativa <strong>A</strong>.</p><p>A intensidade (B) define se o som é forte ou fraco, e a forma da onda (C), o timbre.</p>",
  tags=["altura do som", "frequência"])
X(88, "Química", "Estequiometria", "<p>Pelas equações, 1 mol de SO<sub>2</sub> retido forma 1 mol de CaSO<sub>3</sub>, que forma 1 mol de CaSO<sub>4</sub>. A massa molar do gesso é 40 + 32 + 4 × 16 = 136 g/mol. Com rendimento de 90%: 0,9 × 136 ≈ <strong>122 g</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["rendimento", "dessulfurização"],
  enun=ap(T(88, 0)) + ap("CaCO<sub>3</sub> (s) + SO<sub>2</sub> (g) → CaSO<sub>3</sub> (s) + CO<sub>2</sub> (g) &nbsp; (1)") + ap(T(88, 2))
  + ap("2 CaSO<sub>3</sub> (s) + O<sub>2</sub> (g) → 2 CaSO<sub>4</sub> (s) &nbsp; (2)") + ap(T(88, 4)) + fonte("BAIRD, C. <em>Química ambiental</em>. Porto Alegre: Bookman, 2002 (adaptado).") + p(T(88, 6)))
X(89, "Biologia", "Biotecnologia", "<p>O cordão umbilical tem células-tronco, que ainda não são especializadas e podem originar vários tipos de células. O poder terapêutico vem da sua capacidade de <strong>diferenciação em células especializadas</strong>, que podem repor tecidos doentes. Alternativa <strong>D</strong>.</p>",
  tags=["células-tronco", "diferenciação celular"])
X(90, "Química", "Cinética química", "<p>A melhor lente escurece bastante (transmitância baixa), escurece rápido e clareia rápido. A amostra 3 tem a transmitância mais baixa empatada (50%) com a 4, mas escurece em 20 s e esmaece em 30 s, mais rápido que a 4 (50 s e 50 s). A melhor é a <strong>amostra 3</strong>. Alternativa <strong>C</strong>.</p><p>A amostra 1 é rápida para escurecer, mas deixa passar 80% da luz, quase não escurece.</p>",
  tags=["reações reversíveis", "fotocromismo"],
  enun=p(T(90, 0), T(90, 1)) + tabela(["Amostra", "Tempo de escurecimento (segundo)", "Tempo de esmaecimento (segundo)", "Transmitância média da lente quando exposta à luz solar (%)"],
    [["1", "20", "50", "80"], ["2", "40", "30", "90"], ["3", "20", "30", "50"], ["4", "50", "50", "50"], ["5", "40", "20", "95"]]) + p(T(90, 4)))

completar(Q, R)
