# Enem 2010, 1º dia, caderno azul: Ciências da Natureza (questões 46 a 90; no site, 1 a 45). Em 2010 a Natureza era no 1º dia.
# Texto legível. Quadros das Q48, Q69 e Q70 e equações das Q65, Q73 e Q82 em HTML. Alternativas-imagem nas Q80 (fórmulas) e Q84 (raios de luz).
# Sem anuladas nesta área.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, paragrafos_enem

ID = "enem-2010-natureza"
META = {"id": ID, "banca": "Enem", "ano": 2010, "titulo": "Enem 2010: Ciências da Natureza", "fonte": "Inep", "dataExame": "2010-11-06",
        "duracaoMinutos": 150, "area": "Ciências da Natureza", "caderno": "azul", "dia": 1}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2010-dia1-azul")
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

CAP = lambda x: f'<p class="apoio" style="text-align:center">{x}</p>'
L = lambda s: s.replace("m�", "mL").replace("mol/�", "mol/L").replace("mg/�", "mg/L")


X(46, "Biologia", "Imunologia", "<p>A febre amarela se previne com vacina, que faz o corpo produzir anticorpos e memória antes da viagem. Contra o veneno de cobra, que age rápido, usa-se o soro antiofídico, com anticorpos prontos. A leptospirose é causada por uma bactéria e se trata com antibiótico. A resposta é <strong>vacina contra a febre amarela, soro antiofídico se for picado e antibiótico em caso de contato com a <em>Leptospira</em></strong>. Alternativa <strong>B</strong>.</p><p>Antibióticos não agem contra vírus (A e D).</p>",
  tags=["vacina e soro", "antibióticos"], alts={**D[46]["alternativas"], "B": D[46]["alternativas"]["B"].replace("Leptospira sp.", "<em>Leptospira</em> sp."), "E": D[46]["alternativas"]["E"].replace("Leptospira sp", "<em>Leptospira</em> sp")})
X(47, "Física", "Ondas", "<p>A ionosfera funciona como um espelho para as ondas de rádio de certas frequências: elas sobem, batem nessa camada e voltam para a Terra, alcançando lugares atrás da curvatura do planeta. O fenômeno é a <strong>reflexão</strong>. Alternativa <strong>A</strong>.</p><p>Na refração (B) a onda atravessa o meio e muda de direção, mas o que permite o retorno à superfície é a reflexão.</p>",
  tags=["ionosfera", "ondas de rádio"])
X(48, "Física", "Eletrodinâmica", "<p>Cada farol consome i = P/U = 55/36 ≈ 1,53 A. Ligados em paralelo com um só fusível, a corrente total é cerca de 3,06 A. O fusível precisa suportar pelo menos isso: o menor adequado é o de 5,0 A, o <strong>laranja</strong>. Alternativa <strong>C</strong>.</p><p>O amarelo (2,5 A) queimaria; o azul só serviria para um farol.</p>",
  tags=["potência elétrica", "associação em paralelo"],
  enun=p(T(48, 0)) + tabela(["Fusível", "Corrente Elétrica (A)"], [["Azul", "1,5"], ["Amarelo", "2,5"], ["Laranja", "5,0"], ["Preto", "7,5"], ["Vermelho", "10,0"]]) + p(T(48, 2)))
X(49, "Biologia", "Saúde e doenças", "<p>O texto explica que as bactérias da placa transformam os açúcares em ácidos que corroem o dente, e que a placa se forma quando não se escovam os dentes direito. O dicionário confirma: a cárie é a destruição do dente por bactérias. Ela resulta do <strong>consumo excessivo de açúcares na alimentação e má higienização bucal, que contribuem para a proliferação de bactérias</strong>. Alternativa <strong>E</strong>.</p><p>O flúor e o xilitol aparecem no texto como inibidores da cárie (A, B e D).</p>",
  tags=["cárie", "placa bacteriana"], trocas=[("Dicionário eletrônico", "<em>Dicionário eletrônico</em>")])
X(50, "Física", "Termologia", "<p>No senso comum, temperatura mede “quanto calor” um corpo tem. Mas a água fervendo recebe calor do fogo o tempo todo e sua temperatura fica em 100 °C: o calor vai para a mudança de estado. Isso mostra a limitação dos conceitos comuns: <strong>a temperatura da água pode ficar constante durante o tempo em que estiver fervendo</strong>. Alternativa <strong>A</strong>.</p><p>As outras situações são compatíveis com a ideia comum de calor e temperatura.</p>",
  tags=["calor latente", "mudança de estado"])
X(51, "Biologia", "Ecologia", "<p>O ngaura é a camada de folhas caídas no chão da floresta (a serapilheira). Ela é decomposta por fungos e pequenos animais, “enriquece a terra e alimenta as árvores”: devolve ao solo a matéria orgânica, feita de carbono, que as plantas captaram do ar na fotossíntese. É um produto do ciclo <strong>do carbono</strong>. Alternativa <strong>D</strong>.</p>",
  tags=["serapilheira", "ciclos biogeoquímicos"],
  enun=p(T(51, 0).replace("vôo", "voo")) + tit("O voo das Folhas") + ap(T(51, 1).replace("O vôo das Folhas ", "").replace("] ", " ").replace(".]", "."))
       + fonte("<em>A natureza segundo os Ticunas/Livro das Árvores</em>. Organização Geral dos Professores Bilíngues Ticunas, 2000.") + p(T(51, 3)))
X(52, "Física", "Termologia", "<p>Eficiência é aproveitar bem a energia em pouco tempo. Todos os fornos aqueceram as amostras em 10 °C, mas o melhor é o que entrega mais energia por unidade de tempo, ou seja, o que <strong>forneceu a maior quantidade de energia em menos tempo</strong>. Alternativa <strong>C</strong>.</p><p>Dar muita energia em muito tempo (A e B) não indica eficiência.</p>",
  tags=["potência", "energia"])
X(53, "Química", "Química ambiental", "<p>O fósforo das minas está acabando, e o dos dejetos e restos de cultura acaba no lixo ou nos rios. Transformar esses resíduos em adubo devolve o fósforo ao solo e diminui a extração. A medida seria <strong>incentivar a reciclagem de resíduos biológicos, utilizando dejetos animais e restos de culturas para produção de adubo</strong>. Alternativa <strong>A</strong>.</p><p>Não existe “íon sintético” que reponha o fósforo (B), e nenhum elemento o substitui na vida (D).</p>",
  tags=["fósforo", "reciclagem de nutrientes"], enun=ap("O fósforo, geralmente representado pelo íon de fosfato (PO<sub>4</sub><sup>3−</sup>)" + T(53, 1)) + p(T(53, 2)))
X(54, "Física", "Óptica", "<p>A faixa é vista pela luz do Sol refletida nas nuvens. Se a faixa escura sumiu, as nuvens daquela região passaram a refletir a luz de outro jeito: uma mudança na concentração das nuvens daquela camada. O desaparecimento pode ter sido causado por uma alteração <strong>na densidade das nuvens que compõem o planeta</strong>. Alternativa <strong>E</strong>.</p><p>O texto liga o fenômeno ao movimento das camadas de nuvens, e não à temperatura da superfície (A) ou ao campo gravitacional (C).</p>",
  figs(("q54", "Duas fotos de Júpiter: na primeira, aparecem as duas faixas escuras, uma em cada hemisfério; na segunda, uma seta aponta a região do hemisfério sul onde a faixa sumiu.")), ["Júpiter", "reflexão da luz"])
X(55, "Química", "Separação de misturas", "<p>Etapa 1: o eletroímã retira os metais da cana, uma separação magnética. Etapa 2: a cana é esmagada para retirar o caldo, uma extração (a queima do bagaço é combustão, que é transformação química, e não separação). Etapa 3: o caldo passa por filtros, uma filtração. As operações físicas são <strong>separação magnética, extração e filtração</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["separação magnética", "filtração"],
  enun=p(T(55, 0)) + "<ol>" + "".join(f"<li>{x.strip()}</li>" for x in re.split(r"\d\. ", T(55, 1)) if x.strip()) + "</ol>" + p(T(55, 2).replace("canade-açúcar", "cana-de-açúcar")))
X(56, "Geografia", "Energia", "<p>A figura mostra uma usina geotérmica, como as da Islândia: a água subterrânea é aquecida pelo magma, perto da superfície nas regiões de encontro de placas, e o vapor move turbinas. O calor vem <strong>da circulação do magma no subsolo</strong>. Alternativa <strong>A</strong>.</p><p>Não depende de erupções (B) nem de combustíveis (D).</p>",
  figs(("q56", "Ilustração de uma usina geotérmica: (1) ao escavar um quilômetro em direção ao centro da Terra, a temperatura chega a 250 °C; (2) a água aquecida gera vapor que impulsiona turbinas e gera energia elétrica; a água subterrânea escapa por fissuras, formando piscinas termais e gêiseres; nas regiões onde as placas tectônicas se encontram, como na Islândia, o magma está mais próximo da superfície.")),
  ["energia geotérmica"], trocas=[("Revista IstoÉ", "<em>Revista IstoÉ</em>")])
X(57, "Biologia", "Ecologia", "<p>Na eutrofização, o excesso de nutrientes faz algas e bactérias crescerem muito; a decomposição aeróbia consome o oxigênio da água. Tirando os nutrientes do esgoto antes de chegar ao rio, o crescimento excessivo não acontece. A maneira é <strong>retirar do esgoto os materiais ricos em nutrientes para diminuir a sua concentração nos rios</strong>. Alternativa <strong>B</strong>.</p><p>Aquecer a água (A) diminui ainda mais a solubilidade do oxigênio.</p>",
  tags=["eutrofização", "tratamento de esgoto"])
X(58, "Física", "Termologia", "<p>Com a seringa tampada, puxar o êmbolo aumenta o volume para o mesmo ar e vapor, e a pressão lá dentro cai. Com pressão menor, a água ferve a temperatura mais baixa: a água, ainda quente, volta a ferver. O deslocamento <strong>proporciona uma queda de pressão no interior da seringa que diminui o ponto de ebulição da água</strong>. Alternativa <strong>D</strong>.</p>",
  tags=["pressão e ebulição"], enun=p(T(58, 0).replace("100 oC", "100 °C")) + LISTA(T(58, 1)) + p(T(58, 2)))
X(59, "Física", "Termologia", "<p>Com o efeito estufa e as ilhas de calor, as cidades ficam mais quentes. Indústrias e casas usam mais ar-condicionado e refrigeração, e o consumo de energia elétrica <strong>aumenta devido à necessidade de maior refrigeração de indústrias e residências</strong>. Alternativa <strong>D</strong>.</p><p>Os gases do efeito estufa não bloqueiam a luz visível (B); eles retêm a radiação infravermelha.</p>",
  tags=["ilha de calor", "consumo de energia"], trocas=[("CO2", "CO<sub>2</sub>")])
X(60, "Biologia", "Fisiologia vegetal", "<p>A raiz absorve água por osmose, do meio menos concentrado para o mais concentrado. Se o solo tem mais sais que as células da raiz, a água não entra (e pode até sair), mesmo com o solo úmido: é a seca fisiológica. Ela se caracteriza pelo <strong>aumento da salinidade, em que a água do solo atinge uma concentração de sais maior que a das células das raízes das plantas, impedindo, assim, que a água seja absorvida</strong>. Alternativa <strong>A</strong>.</p>",
  tags=["osmose", "salinização"], trocas=[("Cultura do arroz: salinização de solos em cultivos de arroz", "<em>Cultura do arroz: salinização de solos em cultivos de arroz</em>")])
X(61, "Biologia", "Ecologia", "<p>O óleo atingiu primeiro as algas, base da cadeia alimentar, e depois os peixes, as aves e a atividade pesqueira. O desequilíbrio de uma parte afetou o todo. A situação <strong>ilustra a interdependência das diversas formas de vida (animal, vegetal e outras) e o seu habitat</strong>. Alternativa <strong>C</strong>.</p><p>O petróleo na água não tem relação direta com o efeito estufa (B).</p>",
  tags=["derramamento de petróleo", "cadeia alimentar"], trocas=[("Scientific American Brasil", "<em>Scientific American Brasil</em>")])
X(62, "Biologia", "Fisiologia humana", "<p>Os dois papéis tinham o mesmo tamanho (10 cm por 5 cm), mas o dobrado tinha mais área em contato com a água e absorveu 12 mL, contra 8 mL do liso. As microvilosidades fazem o mesmo no intestino: <strong>aumentar a superfície de absorção</strong>. Alternativa <strong>B</strong>.</p>",
  figs(("q62", "Figura 1: retângulo de papel liso de 10 cm por 5 cm. Figura 2: papel do mesmo tamanho dobrado em sanfona.")), ["microvilosidades", "intestino delgado"],
  enun=L(p(T(62, 0))) + "[[fig:1]]" + p(T(62, 3)))
X(63, "Química", "Eletroquímica", "<p>Na célula a combustível, o hidrogênio e o oxigênio reagem e geram corrente elétrica diretamente, e o produto é água, sem os gases poluentes da queima de combustíveis fósseis. Ela <strong>transforma energia química em energia elétrica, sem causar danos ao meio ambiente, porque o principal subproduto formado é a água</strong>. Alternativa <strong>A</strong>.</p><p>Não há conversão em energia térmica como finalidade (B), e não há emissão de poluentes (C).</p>",
  figs(("q63", "Esquema de uma célula a combustível: H2 entra pelo ânodo, à esquerda, e libera elétrons (2e−) que passam pelo circuito externo; íons 2H+ atravessam o eletrólito no centro; à direita, no cátodo, O2 entra e sai H2O.")), ["célula a combustível", "hidrogênio"],
  trocas=[("Química Nova Na Escola", "<em>Química Nova Na Escola</em>"), ("hidrogênio/ oxigênio", "hidrogênio/oxigênio")])
X(64, "Biologia", "Evolução", "<p>Lamarck explicava a evolução pela lei do uso e desuso (órgãos pouco usados se atrofiam) e pela herança dos caracteres adquiridos. Num ambiente subterrâneo escuro, os olhos não seriam usados e atrofiariam: <strong>a ausência de olhos teria sido causada pela falta de uso dos mesmos, segundo a lei do uso e desuso</strong>. Alternativa <strong>B</strong>.</p><p>Seleção natural e mutações (A e E) são ideias de Darwin e da teoria sintética; “patrimônio genético” (D) não existia no vocabulário de Lamarck.</p>",
  tags=["Lamarck", "uso e desuso"])
X(65, "Química", "Funções inorgânicas", "<p>Ionização é o ácido liberando H<sup>+</sup> na água (IV, ácido cítrico). Dissociação iônica é um sal separando seus íons (I, bicarbonato de sódio). A formação do ácido carbônico vem da união de HCO<sub>3</sub><sup>−</sup> e H<sup>+</sup> (III). A liberação do gás é a decomposição do H<sub>2</sub>CO<sub>3</sub> em água e CO<sub>2</sub> (II). A ordem é <strong>IV, I, III e II</strong>. Alternativa <strong>E</strong>.</p>",
  tags=["ionização e dissociação", "efervescência"],
  enun=ap(T(65, 0).replace("(NaHCO3)", "(NaHCO<sub>3</sub>)")) + p(T(65, 1).replace("H3A", "H<sub>3</sub>A"))
       + EQ("I – NaHCO<sub>3</sub> → Na<sup>+</sup> + HCO<sub>3</sub><sup>−</sup>", "II – H<sub>2</sub>CO<sub>3</sub> ⇌ H<sub>2</sub>O + CO<sub>2</sub>", "III – HCO<sub>3</sub><sup>−</sup> + H<sup>+</sup> ⇌ H<sub>2</sub>CO<sub>3</sub>", "IV – H<sub>3</sub>A ⇌ 3H<sup>+</sup> + A<sup>−</sup>") + p(T(65, 3)))
X(66, "Biologia", "Metabolismo energético", "<p>Na respiração anaeróbia, outra substância faz o papel do O<sub>2</sub> como aceptor final de elétrons. As bactérias anaeróbias usam, por exemplo, o enxofre (S) e o nitrato (NO<sub>3</sub><sup>−</sup>), que recebem elétrons e são reduzidos. A resposta é <strong>S e NO<sub>3</sub><sup>−</sup></strong>. Alternativa <strong>B</strong>.</p><p>H<sub>2</sub> e CH<sub>4</sub> são doadores de elétrons, e não aceptores (A, C e D).</p>",
  tags=["respiração anaeróbia", "aceptor de elétrons"], enun=ap(T(66, 0)) + fonte(T(66, 1).replace("Italianos descobrem animal que vive em água sem oxigênio", "<em>Italianos descobrem animal que vive em água sem oxigênio</em>")) + p("Que substâncias poderiam ter a mesma função do O<sub>2</sub> na respiração celular realizada pelos loricíferos?"),
  alts={"A": "S e CH<sub>4</sub>", "B": "S e NO<sub>3</sub><sup>−</sup>", "C": "H<sub>2</sub> e NO<sub>3</sub><sup>−</sup>", "D": "CO<sub>2</sub> e CH<sub>4</sub>", "E": "H<sub>2</sub> e CO<sub>2</sub>"})
X(67, "Química", "Termoquímica", "<p>A reação direta absorve calor (é endotérmica): a energia do Sol é guardada nas ligações do CO e do H<sub>2</sub>, que são combustíveis. Depois, queimá-los (ou inverter a reação) libera essa energia. É uma estratégia <strong>satisfatória, uma vez que a reação direta ocorre com absorção de calor e promove a formação das substâncias combustíveis que poderão ser utilizadas posteriormente</strong>. Alternativa <strong>D</strong>.</p><p>A opção E diz que a reação libera calor, o que contradiz a equação.</p>",
  tags=["reação endotérmica", "energia solar"],
  enun=ap(T(67, 0)) + fonte("BROWN, T. <em>Química a Ciência Central</em>. São Paulo: Pearson Prentice Hall, 2005.")
       + p("Atualmente, uma das formas de se utilizar a energia solar tem sido armazená-la por meio de processos químicos endotérmicos que mais tarde podem ser revertidos para liberar calor. Considerando a reação: CH<sub>4(g)</sub> + H<sub>2</sub>O<sub>(v)</sub> + calor ⇌ CO<sub>(g)</sub> + 3 H<sub>2(g)</sub> e analisando-a como potencial mecanismo para o aproveitamento posterior da energia solar, conclui-se que se trata de uma estratégia"))
X(68, "Física", "Eletrodinâmica", "<p>Lendo o último número ultrapassado em cada relógio: leitura atual 2 7 8 2 kWh; mês passado 2 5 6 2 kWh. O consumo foi 2 782 − 2 562 = 220 kWh. A R$ 0,20 o kWh: 220 × 0,20 = <strong>R$ 44,00</strong>. Alternativa <strong>E</strong>.</p><p>Os relógios giram em sentidos alternados; quem lê todos no mesmo sentido chega a outros valores.</p>",
  figs(("q68", "Dois conjuntos de quatro relógios de ponteiro de um medidor de energia, com a foto de um medidor ao lado. Leitura atual: os ponteiros estão logo depois do 2, do 7, do 8 e do 2. Leitura do mês passado: logo depois do 2, do 5, do 6 e do 2.")),
  ["leitura de medidor", "consumo de energia"], trocas=[("Instalação Elétrica", "<em>Instalação Elétrica</em>")])
X(69, "Química", "Termoquímica", "<p>Um litro de cada álcool tem 790 g. Metanol (32 g/mol): 790/32 ≈ 24,7 mol × 726 kJ ≈ 17,9 MJ. Etanol (46 g/mol): 790/46 ≈ 17,2 mol × 1 367 kJ ≈ 23,5 MJ. Com o mesmo custo, o mais vantajoso é o <strong>etanol, que fornece cerca de 23,5 MJ por litro</strong>. Alternativa <strong>D</strong>.</p><p>As opções A e B usam kJ no lugar de MJ.</p>",
  tags=["calor de combustão", "densidade"],
  enun=p(T(69, 0)) + tabela(["Álcool", "Densidade a 25 ºC (g/mL)", "Calor de Combustão (kJ/mol)"], [["Metanol (CH<sub>3</sub>OH)", "0,79", "−726,0"], ["Etanol (CH<sub>3</sub>CH<sub>2</sub>OH)", "0,79", "−1367,0"]])
       + fonte("BAIRD, C. <em>Química Ambiental</em>. São Paulo: Artmed, 1995 (adaptado).") + p(T(69, 3), T(69, 4)))
X(70, "Física", "Eletrodinâmica", "<p>O modelo de maior potência da versão 220 V tem 5 500 W: R = U²/P = 220²/5 500 = 8,8 Ω. Ligada em 127 V, a resistência é a mesma: P = 127²/8,8 ≈ 16 129/8,8 ≈ <strong>1 830 W</strong>. Alternativa <strong>A</strong>.</p><p>A potência não cai na mesma proporção da tensão: ela depende do quadrado da tensão.</p>",
  tags=["potência elétrica", "resistência"],
  enun=p(T(70, 0)) + tit("Especificações Técnicas") + tabela(["Modelo", "Torneira 127 V", "", "Torneira 220 V", ""],
    [["Potência Nominal (Watts) — Desligado", "—", "—", "—", "—"], ["Potência Nominal (Watts) — Morno", "2 800", "3 200", "2 800", "3 200"], ["Potência Nominal (Watts) — Quente", "4 500", "5 500", "4 500", "5 500"],
     ["Corrente Nominal (Ampères)", "35,4", "43,3", "20,4", "25,0"], ["Fiação Mínima (Até 30 m)", "6 mm²", "10 mm²", "4 mm²", "4 mm²"], ["Fiação Mínima (Acima 30 m)", "10 mm²", "16 mm²", "6 mm²", "6 mm²"], ["Disjuntor (Ampères)", "40", "50", "25", "30"]])
    + fonte("Disponível em: http://www.cardal.com.br/manualprod/Manuais/Torneira%20Suprema/Manual_Torneira_Suprema_roo.pdf") + p(T(70, 3)))
X(71, "Biologia", "Microbiologia", "<p>As bactérias se reproduzem por divisão binária muito rápida, gerando clones idênticos, e têm metabolismo variado: algumas respiram oxigênio, outras vivem sem ele. Com menos oxigênio na córnea, as que fazem processos anaeróbios conseguem se instalar. As características são o <strong>alto poder de reprodução, originando milhares de descendentes geneticamente idênticos entre si e a diversidade metabólica, considerando processos aeróbicos e anaeróbicos</strong>. Alternativa <strong>E</strong>.</p>",
  tags=["bactérias", "metabolismo"], trocas=[("Revista Sinopse de Oftalmologia", "<em>Revista Sinopse de Oftalmologia</em>")], alts={**D[71]["alternativas"], "D": D[71]["alternativas"]["D"].replace("matéria- prima", "matéria-prima")})
X(72, "Química", "Estequiometria", "<p>A oxidação do açúcar é CH<sub>2</sub>O + O<sub>2</sub> → CO<sub>2</sub> + H<sub>2</sub>O: 1 mol de O<sub>2</sub> (32 g) para cada 30 g de CH<sub>2</sub>O. Para 10 mg: 10 × 32/30 ≈ <strong>10,7 mg de O<sub>2</sub> por litro</strong>. Alternativa <strong>E</strong>.</p><p>A DBO é sempre um pouco maior que a massa de açúcar, porque a massa molar do O<sub>2</sub> é maior.</p>",
  tags=["DBO", "proporção estequiométrica"], enun=L(ap(T(72, 0).replace("O2", "O<sub>2</sub>"))) + fonte("BAIRD, C. <em>Química Ambiental</em>. Ed. Bookman, 2005 (adaptado).") + p(T(72, 2), T(72, 3).replace("CH2O", "CH<sub>2</sub>O")),
  alts={k: f"{v} mg de O<sub>2</sub>/litro" for k, v in zip("ABCDE", ["0,4", "1,7", "2,7", "9,4", "10,7"])})
X(73, "Química", "Estequiometria", "<p>A pasta tem 60% de PbSO<sub>4</sub>: 0,6 × 6 kg = 3,6 kg. PbSO<sub>4</sub> = 303 g/mol e PbCO<sub>3</sub> = 267 g/mol, na proporção 1 : 1: 3,6 × 267/303 ≈ 3,17 kg. Com rendimento de 91%: 3,17 × 0,91 ≈ <strong>2,9 kg</strong>. Alternativa <strong>C</strong>.</p><p>Sem o rendimento, chega-se a 3,3 kg (D).</p>",
  tags=["rendimento", "massa molar"],
  enun=ap(SUB(T(73, 0)).replace("SO<sub>2</sub>(g)", "SO<sub>2(g)</sub>")) + EQ("PbSO<sub>4</sub> + Na<sub>2</sub>CO<sub>3</sub> → PbCO<sub>3</sub> + Na<sub>2</sub>SO<sub>4</sub>") + ap("Dados: Massas molares em g/mol: Pb = 207; S = 32; Na = 23; O = 16; C = 12")
       + fonte(T(73, 2).replace("Reciclagem de chumbo de bateria automotiva: estudo de caso", "<em>Reciclagem de chumbo de bateria automotiva: estudo de caso</em>")) + p(T(73, 3).replace("PbCO3", "PbCO<sub>3</sub>")))
X(74, "Química", "Eletroquímica", "<p>Carga: Q = i · t = 10 A × 10 800 s = 108 000 C, ou 108 000/96 500 ≈ 1,12 mol de elétrons. Cada Cu<sup>2+</sup> precisa de 2 elétrons: 0,56 mol de Cu × 63,5 g/mol ≈ <strong>35,5 g</strong>. Alternativa <strong>D</strong>.</p><p>Quem esquece a carga 2+ chega a 71,0 g (E); quem usa o tempo em horas chega a valores muito pequenos (A e B).</p>",
  tags=["eletrólise", "lei de Faraday"], enun=ap(T(74, 0)) + p(T(74, 1).replace("(CuSO4)", "(CuSO<sub>4</sub>)"), T(74, 2)))
X(75, "Biologia", "Biomas", "<p>I: pinheiros e gralha-azul são da Mata de Araucárias, no Sul. II: árvores de troncos tortuosos e casca grossa, usadas em carvoarias, são do Cerrado. III: palmeiras que dão produtos para a economia regional (babaçu, carnaúba) são da Zona dos Cocais. IV: aridez e plantas espinhosas são da Caatinga. A resposta é <strong>Mata de Araucárias, Cerrado, Zona dos Cocais e Caatinga</strong>. Alternativa <strong>B</strong>.</p>",
  figs(("q75", "Mapa do Brasil com os ecossistemas em tons de cinza e dois trajetos marcados por setas: o trajeto 1 vai do norte ao sul, passando pelo interior até o Sul; o trajeto 2 sai do Nordeste e faz uma curva pelo interior da região.")),
  ["ecossistemas brasileiros"], enun="[[fig:1]]" + p(T(75, 1)) + ap(*[x.strip() for x in re.split(r"(?=I\. |II\. )", T(75, 2)) if x.strip()]) + ap(*[x.strip() for x in re.split(r"(?=III\. |IV\. )", T(75, 3)) if x.strip()])
       + fonte(T(75, 4).replace("Ecossistemas brasileiros: mapa da distribuição dos ecossistemas", "<em>Ecossistemas brasileiros: mapa da distribuição dos ecossistemas</em>")) + p(T(75, 5)))
X(76, "Biologia", "Biotecnologia", "<p>Os machos transgênicos cruzam com fêmeas selvagens e passam o gene dominante. As filhas que o herdam não voam, então não picam pessoas nem se reproduzem direito. Com o tempo, a população de vetores cai. A liberação <strong>dificultaria a contaminação e reprodução do vetor natural da doença</strong>. Alternativa <strong>C</strong>.</p><p>O sucesso dos machos em cruzar é essencial ao método (A).</p>",
  tags=["dengue", "transgênicos"], trocas=[("Aedes aegypti", "<em>Aedes aegypti</em>"), ("Female-specific flightless phenotype for mosquito control", "<em>Female-specific flightless phenotype for mosquito control</em>")])
X(77, "Química", "Funções inorgânicas", "<p>O monofluoracetato de sódio é um sal: o H ácido do grupo COOH do ácido monofluoracético foi trocado por Na<sup>+</sup>. Sal se forma pela reação de um ácido com uma base: FCH<sub>2</sub>COOH + NaOH → FCH<sub>2</sub>COONa + H<sub>2</sub>O. É a <strong>neutralização do ácido monofluoracético usando hidróxido de sódio, com liberação de água</strong>. Alternativa <strong>D</strong>.</p>",
  figs(("q77", "Fórmula estrutural do monofluoracetato de sódio: F–CH2–C(=O)–O− Na+.")), ["sais", "neutralização"],
  enun=p(T(77, 0)) + "[[fig:1]]" + CAP("monofluoracetato de sódio.") + fonte(T(77, 3)) + p(T(77, 4)))
X(78, "Física", "Eletrostática", "<p>Uma caixa de metal fechada funciona como uma gaiola de Faraday: as cargas se distribuem na superfície externa e o campo elétrico das ondas não chega ao interior. O celular perdeu o sinal na caixa de <strong>metal, devido à blindagem eletrostática que o metal proporcionava</strong>. Alternativa <strong>B</strong>.</p><p>O tamanho da área lateral ou a espessura (D e E) não explicam o efeito.</p>",
  tags=["gaiola de Faraday", "blindagem"])
X(79, "Química", "Estequiometria", "<p>A combustão completa do octano é C<sub>8</sub>H<sub>18</sub> + 25/2 O<sub>2</sub> → 8 CO<sub>2</sub> + 9 H<sub>2</sub>O. Para 1 octano, são 8 CO<sub>2</sub>, 9 H<sub>2</sub>O e <strong>12,5 O<sub>2</sub></strong>. Alternativa <strong>D</strong>.</p><p>O oxigênio é consumido, e não liberado (A); a água é produto (C); o CO<sub>2</sub> tem coeficiente 8, e não 9 (E).</p>",
  tags=["combustão", "balanceamento"], trocas=[("(C8H18)", "(C<sub>8</sub>H<sub>18</sub>)"), ("Revista Aquecimento Global", "<em>Revista Aquecimento Global</em>")],
  alts={**D[79]["alternativas"], "A": "no processo há liberação de oxigênio, sob a forma de O<sub>2</sub>."})
X(80, "Química", "Química orgânica", "<p>O Tipo B tem o enxofre no lugar do oxigênio ligado ao fósforo por ligação dupla (P=S), e os outros grupos com oxigênio. Além disso, o pesticida deve ter grupo etoxi (–OCH<sub>2</sub>CH<sub>3</sub>). A única estrutura com P=S, sem enxofre na cadeia simples e com etoxi é a da <strong>alternativa E</strong> (paration). Alternativa <strong>E</strong>.</p><p>A estrutura B também é Tipo B, mas tem grupos metoxi (–OCH<sub>3</sub>).</p>",
  figs(("q80a", "Alternativa A: fósforo com O em ligação dupla, ligado a R–O e a dois grupos O–CH3."),
       ("q80b", "Alternativa B: fósforo com S em ligação dupla, ligado a R–O e a dois grupos O–CH3."),
       ("q80c", "Alternativa C: fósforo com S em ligação dupla, ligado a R–S e a dois grupos O–CH3."),
       ("q80d", "Alternativa D: fósforo com S em ligação dupla, ligado a NH2, a CH3O e a um oxigênio ligado a um anel benzênico com CH3 e um grupo éster."),
       ("q80e", "Alternativa E: fósforo com S em ligação dupla, ligado a dois grupos OCH2CH3 e a um oxigênio ligado a um anel benzênico com o grupo O2N na outra ponta.")),
  ["organofosforados", "grupo etoxi"], enun=ap(T(80, 0).replace("Tipo A", "<strong>Tipo A</strong>").replace("Tipo B", "<strong>Tipo B</strong>").replace("Tipo C", "<strong>Tipo C</strong>")) + fonte("BAIRD, C. <em>Química Ambiental</em>. Bookman, 2005.") + p(T(80, 2).replace("Tipo B", "<strong>Tipo B</strong>")),
  alts=ALT(1))
X(81, "Física", "Hidrostática", "<p>Dentro da água, a escultura recebe o empuxo, uma força para cima igual ao peso da água deslocada, ou seja, proporcional ao seu volume. Essa força se soma à dos trabalhadores e pode vencer o peso. A resposta é que a <strong>água exercerá uma força na escultura proporcional ao seu volume, e para cima</strong>. Alternativa <strong>E</strong>.</p><p>O peso da escultura não muda (B), e o ferro maciço não flutua (A).</p>",
  tags=["empuxo", "Arquimedes"])
X(82, "Química", "Separação de misturas", "<p>Na reação, o extrator HR libera H<sup>+</sup> e recebe o cátion metálico, formando MR<sub>2</sub>. Quem faz a troca é o grupo –PO<sub>2</sub>H, a parte polar da molécula; a cadeia carbônica longa (apolar) leva o complexo para a fase orgânica. X e Y <strong>atuam como extratores catiônicos, uma vez que a parte polar da molécula troca o íon H<sup>+</sup> pelo cátion do metal</strong>. Alternativa <strong>A</strong>.</p>",
  figs(("q82", "Gráfico da extração (%) em função do pH de equilíbrio, de 0 a 7, para Cd, Co e Ni com os solventes X e Y. Com X, as curvas sobem em pH mais baixo, entre 2 e 4; com Y, sobem entre 3,5 e 6. Em cada grupo, o cádmio é extraído primeiro, depois o cobalto e por último o níquel.")),
  ["extração líquido-líquido", "troca iônica"],
  enun=ap(T(82, 0).replace("Cd(OH)2(s)", "Cd(OH)<sub>2(s)</sub>").replace("Ni(OH)2(s)", "Ni(OH)<sub>2(s)</sub>").replace("Co(OH)2(s)", "Co(OH)<sub>2(s)</sub>"))
       + EQ("M<sup>2+</sup><sub>(aq)</sub> + 2 HR<sub>(org)</sub> ⇌ MR<sub>2(org)</sub> + 2 H<sup>+</sup><sub>(aq)</sub>")
       + ap("Onde: M<sup>2+</sup> = Cd<sup>2+</sup>, Ni<sup>2+</sup> ou Co<sup>2+</sup><br>HR = C<sub>16</sub>H<sub>34</sub>–PO<sub>2</sub>H: identificado no gráfico por <strong>X</strong><br>HR = C<sub>12</sub>H<sub>12</sub>–PO<sub>2</sub>H: identificado no gráfico por <strong>Y</strong>", T(82, 4))
       + "[[fig:1]]" + fonte(T(82, 6)) + p(T(82, 7)),
  alts={"A": "as moléculas <strong>X</strong> e <strong>Y</strong> atuam como extratores catiônicos uma vez que a parte polar da molécula troca o íon H<sup>+</sup> pelo cátion do metal.",
        "B": "as moléculas <strong>X</strong> e <strong>Y</strong> atuam como extratores aniônicos uma vez que a parte polar da molécula troca o íon H<sup>+</sup> pelo cátion do metal.",
        "C": "as moléculas <strong>X</strong> e <strong>Y</strong> atuam como extratores catiônicos uma vez que a parte apolar da molécula troca o íon PO<sub>2</sub><sup>2−</sup> pelo cátion do metal.",
        "D": "as moléculas <strong>X</strong> e <strong>Y</strong> atuam como extratores aniônicos uma vez que a parte polar da molécula troca o íon PO<sub>2</sub><sup>2−</sup> pelo cátion do metal.",
        "E": "as moléculas <strong>X</strong> e <strong>Y</strong> fazem ligações com os íons metálicos resultando em compostos com caráter apolar o que justifica a eficácia da extração."})
X(83, "Química", "Soluções", "<p>3,42 g de sacarose ÷ 342 g/mol = 0,01 mol. Em 50 mL = 0,05 L: 0,01/0,05 = <strong>0,2 mol/L</strong>. Alternativa <strong>B</strong>.</p><p>Quem esquece de converter mL em litros chega a 0,0002 ou a valores grandes como 200 (D).</p>",
  figs(("q83", "Ilustração: uma mão coloca uma colher de soluto num béquer com solvente; uma seta leva a outro béquer com a solução.")), ["concentração molar"],
  enun=L(E(83)))
X(84, "Física", "Óptica", "<p>Com índice de refração negativo, o raio refratado fica do mesmo lado da normal que o raio incidente, em vez de cruzar para o outro lado. Entrando por baixo à esquerda, ele deve seguir para baixo à direita, dentro do metamaterial. É a <strong>figura D</strong>. Alternativa <strong>D</strong>.</p><p>A figura B mostra a refração comum, com o raio passando para o outro lado da normal.</p>",
  figs(("q84a", "Alternativa A: o raio incidente chega ao metamaterial pela esquerda, de baixo para cima, e um raio sai para cima e para a esquerda, do mesmo lado de onde veio."),
       ("q84b", "Alternativa B: o raio incidente chega pela esquerda, de baixo para cima, e continua para cima e para a direita, atravessando a normal, como na refração comum."),
       ("q84c", "Alternativa C: o raio incidente chega pela esquerda e sai para a direita quase na horizontal, rente à normal tracejada."),
       ("q84d", "Alternativa D: o raio incidente chega pela esquerda, de baixo para cima, e o raio refratado segue para a direita e para baixo, do mesmo lado da normal que o incidente."),
       ("q84e", "Alternativa E: o raio incidente chega pela esquerda e para na superfície do metamaterial, sem raio refratado.")),
  ["refração", "índice negativo"], enun=E(84, pular=(3, 4)), alts=ALT(1))
X(85, "Química", "Química ambiental", "<p>O cálcio do cimento-solo tem caráter básico: eleva o pH do solo. Em pH mais alto, o alumínio precipita e deixa de ser tóxico. Assim, plantas invasoras que não suportariam o alumínio passam a crescer à margem da rodovia. A mistura <strong>inibe a toxicidade do alumínio, elevando o pH dessas áreas</strong>. Alternativa <strong>A</strong>.</p><p>O cálcio não reduz o pH (B, D e E).</p>",
  tags=["acidez do solo", "alumínio"], trocas=[("Scientific American. Brasil", "<em>Scientific American Brasil</em>")])
X(86, "Biologia", "Saúde e doenças", "<p>Teste I: o animal que recebe tecido com príons adoece e morre (animal B, marcado com X). Teste II: a lâmina com príons fica marcada pelo anticorpo (lâmina A, com a mancha). Teste III: a protease destrói as proteínas normais, e o marcador revela o príon resistente (gel B, com bandas). A resposta é <strong>Animal B, lâmina A e gel B</strong>. Alternativa <strong>C</strong>.</p>",
  figs(("q86", "Três testes de detecção de príons em cérebro bovino. Teste I: uma amostra é injetada num camundongo; o animal A está vivo e o animal B aparece marcado com X, morto. Teste II: a amostra numa lâmina recebe um anticorpo que reconhece o príon patogênico e vai ao microscópio; a lâmina A mostra uma mancha escura e a lâmina B, não. Teste III: a amostra recebe protease e passa por um gel com marcador específico para o príon; o gel A fica vazio e o gel B mostra bandas escuras.")),
  ["príons", "doença da vaca louca"], enun=p(T(86, 0)) + "[[fig:1]]" + fonte("Legenda: PrP<sup>SC</sup> – proteínas do Príon. <em>Scientific American Brasil</em>, ago. 2004 (adaptado).") + p(T(86, 3)))
X(87, "Biologia", "Ecologia", "<p>As leguminosas têm bactérias nas raízes que fixam o nitrogênio do ar no solo, um adubo natural para a cana. Além disso, soja, amendoim e feijão são vendidos, gerando renda. O benefício econômico está em que <strong>a soja, o amendoim e o feijão, além de possibilitarem a incorporação ao solo de determinadas moléculas disponíveis na atmosfera, são grãos comercializados</strong>. Alternativa <strong>E</strong>.</p><p>O texto não fala de queima de restos de cana (D).</p>",
  tags=["rotação de culturas", "fixação de nitrogênio"], trocas=[("Planeta.", "<em>Planeta</em>.")], alts={**D[87]["alternativas"], "D": D[87]["alternativas"]["D"].replace("cana- de-açúcar", "cana-de-açúcar")})
X(88, "Biologia", "Fisiologia humana", "<p>O ritmo circadiano é ajustado pelas pistas ambientais de claro e escuro. Sem luz e sem contato com o mundo externo, a pessoa perde a referência do dia e seu ritmo se desajusta. Ela <strong>teve seu ritmo biológico alterado devido à ausência de luz e de contato com o mundo externo</strong>. Alternativa <strong>D</strong>.</p><p>O texto diz que o ritmo depende do ambiente, e não que se mantém sozinho (E).</p>",
  tags=["ritmo circadiano"], trocas=[("Psicofisiologia", "<em>Psicofisiologia</em>")])
X(89, "Física", "Energia", "<p>O município é pequeno, cercado de montanhas, tem alta incidência solar o ano todo e um rio que serve para consumo, irrigação e pesca. Uma hidrelétrica alagaria o vale e afetaria o rio; uma termelétrica ou nuclear aqueceria a água e traria riscos. A opção de menor impacto é a <strong>fotovoltaica, aproveitando a energia solar que chega à superfície</strong>. Alternativa <strong>D</strong>.</p><p>Nada no texto indica ventos fortes para a eólica (B).</p>",
  tags=["matriz energética", "energia solar"])
X(90, "Química", "Química ambiental", "<p>No aterro sanitário, o lixo é compactado e coberto com terra, e o fundo é impermeabilizado; o chorume é coletado por drenos e tratado, sem contaminar o solo e a água. O que o torna mais vantajoso é que <strong>o lixo orgânico e inorgânico é encoberto, e o chorume canalizado para ser tratado e neutralizado</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["aterro sanitário", "chorume"], trocas=[("Revista Promoção da Saúde da Secretaria de Políticas de Saúde", "<em>Revista Promoção da Saúde da Secretaria de Políticas de Saúde</em>")])

completar(Q, R)
