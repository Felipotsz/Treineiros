# Enem 2012, 1º dia, caderno azul: Ciências da Natureza (questões 46 a 90; no site, 1 a 45). Em 2012 a Natureza era no 1º dia.
# Texto legível. Equações da Q53 e quadros das Q69 e Q82 em HTML. Alternativas-imagem: Q55, 60, 66, 73 e 78.
# Sem anuladas nesta área.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, paragrafos_enem

ID = "enem-2012-natureza"
META = {"id": ID, "banca": "Enem", "ano": 2012, "titulo": "Enem 2012: Ciências da Natureza", "fonte": "Inep", "dataExame": "2012-11-03",
        "duracaoMinutos": 150, "area": "Ciências da Natureza", "caderno": "azul", "dia": 1}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2012-dia1-azul")
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


X(46, "Química", "Química ambiental", "<p>Reciclar é transformar o material descartado em matéria-prima para um novo produto. Fundir latas de alumínio para fazer lingotes, que voltam à indústria, é reciclagem. Alternativa <strong>B</strong>.</p><p>Garrafas retornáveis e embalagens reaproveitadas (A, C e D) são reutilização: o objeto é usado de novo sem ser transformado.</p>",
  tags=["três erres", "reciclagem"])
X(47, "Física", "Hidrostática", "<p>Pressão é força dividida por área. Com pneus mais largos, o peso do trator se distribui por uma área maior, e a pressão sobre o solo diminui, compactando menos. A resposta é pneus mais <strong>largos, reduzindo a pressão sobre o solo</strong>. Alternativa <strong>A</strong>.</p><p>Pneus estreitos (B e D) concentrariam o peso e aumentariam a pressão.</p>",
  tags=["pressão", "área de contato"])
X(48, "Biologia", "Biotecnologia", "<p>O gene transferido é transcrito em RNA mensageiro, que é traduzido em proteína; é a proteína que produz a característica de interesse. A característica aparece pela <strong>tradução do RNA mensageiro sintetizado a partir do DNA recombinante</strong>. Alternativa <strong>E</strong>.</p><p>O RNA transportador (B) leva aminoácidos ao ribossomo; ele não carrega a informação do gene.</p>",
  tags=["transgênicos", "expressão gênica"])
X(49, "Química", "Funções orgânicas", "<p>A piretrina tem uma cetona no anel de cinco carbonos (C=O entre carbonos) e um éster (C(=O)–O ligado ao anel). A coronopilina tem uma cetona no anel e um éster cíclico (lactona), além de um grupo OH. As funções presentes nas duas são <strong>cetona e éster</strong>. Alternativa <strong>B</strong>.</p><p>O álcool (C) só aparece na coronopilina.</p>",
  figs(("q49", "Fórmulas estruturais da piretrina, com um anel de três carbonos, uma ligação éster e um anel de cinco carbonos com cetona e cadeia lateral com duplas, e da coronopilina, com dois anéis fundidos, um grupo OH, uma cetona e um anel de lactona com dupla ligação exocíclica.")),
  ["cetona", "éster"], enun=p(T(49, 0)) + "[[fig:1]]" + p(T(49, 5)))
X(50, "Física", "Energia", "<p>No carrinho, a energia potencial elástica guardada na mola comprimida vira energia cinética quando ele é solto. O mesmo acontece no <strong>estilingue</strong>: o elástico esticado lança a pedra. Alternativa <strong>E</strong>.</p><p>O dínamo transforma energia mecânica em elétrica (A), e o freio, cinética em térmica (B).</p>",
  tags=["energia potencial elástica", "conversão de energia"])
X(51, "Biologia", "Biotecnologia", "<p>Na biorremediação, o microrganismo usa o poluente no seu metabolismo e o transforma em substâncias inofensivas. Ele deve ser capaz de <strong>metabolizar o contaminante, liberando subprodutos menos tóxicos ou atóxicos</strong>. Alternativa <strong>E</strong>.</p><p>Só absorver o contaminante (B) ou transferi-lo para a água (A) não o elimina.</p>",
  tags=["biorremediação", "microrganismos"])
X(52, "Biologia", "Saúde", "<p>A leptospirose é transmitida pela urina de ratos misturada à água de enchentes, comum onde falta esgoto, drenagem e coleta de lixo. Os sintomas incluem febre, dor de cabeça e dores musculares. O caso indica <strong>leptospirose</strong>. Alternativa <strong>D</strong>.</p><p>Difteria, tuberculose e meningite (A, C e E) são transmitidas pelo ar, e o botulismo, por alimentos contaminados.</p>",
  tags=["leptospirose", "saneamento"])
X(53, "Química", "Química ambiental", "<p>O CFC, quebrado pela radiação ultravioleta, libera cloro, que destrói o ozônio. Isobutano, butano e propano não liberam cloro e não reagem com o ozônio: servem para <strong>substituir o CFC, pois não reagem com o ozônio, servindo como gases propelentes em aerossóis</strong>. Alternativa <strong>A</strong>.</p><p>Os hidrocarbonetos não capturam nem destroem o CFC (B e E).</p>",
  tags=["camada de ozônio", "propelentes"],
  enun=p(T(53, 0)) + ap("I) CF<sub>2</sub>Cℓ<sub>2</sub> → (UV) CF<sub>2</sub>Cℓ<sup>•</sup> + Cℓ<sup>•</sup>", "II) Cℓ<sup>•</sup> + O<sub>3</sub> → O<sub>2</sub> + CℓO<sup>•</sup>") + p(T(53, 4).replace("(O3)", "(O<sub>3</sub>)"), T(53, 5)),
  alts={k: SUB(v) for k, v in D[53]["alternativas"].items()})
X(54, "Física", "Ondas", "<p>A velocidade da onda depende só do meio, a água da piscina, e continua 1,0 m/s. A frequência cai de 2 Hz para 1 Hz e, como v = λ·f, o comprimento de onda dobra, de 25 cm para 50 cm. A distância entre as cristas fica <strong>maior que 25 cm e a velocidade, igual a 1,0 m/s</strong>. Alternativa <strong>B</strong>.</p>",
  tags=["equação fundamental da ondulatória", "frequência"], trocas=[("respectivamemente", "respectivamente")])
X(55, "Física", "Estática", "<p>As dobradiças sustentam o peso da porta, então as forças delas têm componentes verticais para cima. Como o peso fica no centro da porta, ele tende a girá-la; para equilibrar esse giro, a dobradiça de cima puxa a porta em direção ao batente e a de baixo a empurra para fora. As forças são inclinadas para cima, uma para cada lado, como na <strong>figura D</strong>. Alternativa <strong>D</strong>.</p><p>Em A e B só há forças horizontais, e nada segura o peso.</p>",
  figs(("q55a", "Alternativa A: porta com uma força horizontal para a esquerda na dobradiça de cima e uma para a direita na de baixo."),
       ("q55b", "Alternativa B: força horizontal para a direita em cima e para a esquerda embaixo."),
       ("q55c", "Alternativa C: as duas forças verticais, para cima."),
       ("q55d", "Alternativa D: força inclinada para cima e para a esquerda (para fora da porta) em cima, e inclinada para cima e para a direita (para dentro) embaixo."),
       ("q55e", "Alternativa E: força inclinada para cima e para a direita em cima, e para cima e para a esquerda embaixo.")),
  ["equilíbrio de corpo extenso", "torque"], enun=p(T(55, 0), T(55, 1)), alts=ALT(1))
X(56, "Biologia", "Ecologia", "<p>No esquema, as plantas (P<sub>1</sub>) e o herbívoro (P<sub>2</sub>) se juntam na interação I, que alimenta o onívoro (P<sub>3</sub>). O onívoro come plantas e herbívoros, então I representa a proporção de <strong>P<sub>1</sub> ou P<sub>2</sub> utilizada na alimentação de P<sub>3</sub></strong>. Alternativa <strong>D</strong>.</p><p>A herbivoria entre P<sub>1</sub> e P<sub>2</sub> (A) é o fluxo F<sub>2</sub>.</p>",
  figs(("q56", "Diagrama de fluxos: uma fonte de energia E envia o fluxo F1 para P1; P1 envia F2 para P2 e F3 para a interação I; P2 envia F4 para I; I envia F5 para P3, que tem a saída F6. Legenda: E, função motriz; P, propriedades; F, fluxos; I, interações.")),
  ["cadeia alimentar", "onívoro"],
  enun=p("A figura representa um dos modelos de um sistema de interações entre seres vivos. Ela apresenta duas propriedades, <em>P</em><sub>1</sub> e <em>P</em><sub>2</sub>, que interagem em <em>I</em>, para afetar uma terceira propriedade, <em>P</em><sub>3</sub>, quando o sistema é alimentado por uma fonte de energia, <em>E</em>. Essa figura pode simular um sistema de campo em que <em>P</em><sub>1</sub> representa as plantas verdes; <em>P</em><sub>2</sub>, um animal herbívoro e <em>P</em><sub>3</sub>, um animal onívoro.")
  + "[[fig:1]]" + fonte("ODUM, E. P. <em>Ecologia</em>. Rio de Janeiro: Guanabara Koogan, 1988.") + p("A função interativa <em>I</em> representa a proporção de"),
  alts={"A": "herbivoria entre <em>P</em><sub>1</sub> e <em>P</em><sub>2</sub>.", "B": "polinização entre <em>P</em><sub>1</sub> e <em>P</em><sub>2</sub>.", "C": "<em>P</em><sub>3</sub> utilizada na alimentação de <em>P</em><sub>1</sub> e <em>P</em><sub>2</sub>.",
        "D": "<em>P</em><sub>1</sub> ou <em>P</em><sub>2</sub> utilizada na alimentação de <em>P</em><sub>3</sub>.", "E": "energia de <em>P</em><sub>1</sub> e de <em>P</em><sub>2</sub> que saem do sistema."})
X(57, "Biologia", "Botânica", "<p>No cerrado, há fogo periódico. As gemas apicais, de onde a planta volta a crescer, protegidas por pelos densos, resistem ao calor e permitem a rebrota. A estrutura mais apropriada é a de <strong>gemas apicais com densa pilosidade</strong>. Alternativa <strong>D</strong>.</p><p>As plantas do cerrado têm cascas grossas e sulcadas, e raízes profundas, o contrário de A e E.</p>",
  tags=["cerrado", "adaptações"])
X(58, "Química", "Química orgânica", "<p>O éster C<sub>6</sub>H<sub>5</sub>–COO–CH<sub>2</sub>CH<sub>3</sub> vem da reação de um ácido com um álcool. A parte C<sub>6</sub>H<sub>5</sub>–CO vem do <strong>ácido benzoico</strong>, e a parte O–CH<sub>2</sub>CH<sub>3</sub>, do <strong>etanol</strong>. Alternativa <strong>A</strong>.</p><p>O ácido fenilacético (C) tem um CH<sub>2</sub> a mais entre o anel e o grupo carboxila.</p>",
  figs(("q58", "Fórmula estrutural do benzoato de etila: anel benzênico ligado a um carbono com dupla ligação com oxigênio e ligado a O–CH2CH3.")),
  ["esterificação", "nomenclatura"],
  enun=p(T(58, 0).replace("C6H5CO2CH2CH3", "C<sub>6</sub>H<sub>5</sub>CO<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub>")) + "[[fig:1]]" + p(T(58, 3)))
X(59, "Química", "Estequiometria", "<p>Na combustão completa, C<sub>4</sub>H<sub>10</sub> + 13/2 O<sub>2</sub> → 4 CO<sub>2</sub> + 5 H<sub>2</sub>O: cada 58 g de butano formam 4 × 44 = 176 g de CO<sub>2</sub>. Para deixar de emitir 1 kg de CO<sub>2</sub>: 1 000 × 58 ÷ 176 ≈ 330 g = <strong>0,33 kg</strong>. Alternativa <strong>B</strong>.</p><p>Esquecer o coeficiente 4 daria 1,3 kg (D).</p>",
  tags=["combustão", "proporção em massa"],
  enun=p("No Japão, um movimento nacional para a promoção da luta contra o aquecimento global leva o <em>slogan</em>: <strong>1 pessoa, 1 dia, 1 kg de CO<sub>2</sub> a menos!</strong> A ideia é cada pessoa reduzir em 1 kg a quantidade de CO<sub>2</sub> emitida todo dia, por meio de pequenos gestos ecológicos, como diminuir a queima de gás de cozinha.")
  + fonte(T(59, 1)) + p(T(59, 2).replace("(C4H10)", "(C<sub>4</sub>H<sub>10</sub>)"), "Dados: CO<sub>2</sub> (44 g/mol); C<sub>4</sub>H<sub>10</sub> (58 g/mol)"))
X(60, "Física", "Cinemática", "<p>No primeiro terço, com aceleração constante, a posição cresce como uma parábola com concavidade para cima. No segundo, com velocidade constante, cresce em linha reta. No último, com desaceleração até parar, a curva se curva para baixo e fica horizontal no fim. É o <strong>gráfico C</strong>. Alternativa <strong>C</strong>.</p><p>Nos gráficos A, D e E há trechos horizontais no meio, que indicariam o trem parado.</p>",
  figs(("q60a", "Alternativa A: posição cresce em curva até o primeiro terço, fica constante no meio e depois diminui em curva até zero."),
       ("q60b", "Alternativa B: posição cresce quase em linha reta até dois terços e depois cresce mais rápido, em curva para cima."),
       ("q60c", "Alternativa C: curva para cima no primeiro terço, reta inclinada no segundo e curva que se achata até ficar horizontal no terceiro."),
       ("q60d", "Alternativa D: curva para cima no primeiro terço, trecho horizontal no meio e curva para cima no final."),
       ("q60e", "Alternativa E: reta inclinada, trecho horizontal e outra reta inclinada.")),
  ["MUV", "gráfico posição-tempo"], enun=p(T(60, 0), T(60, 1)), alts=ALT(1))
X(61, "Física", "Eletrodinâmica", "<p>A incandescente de 40 W emite 600 lm: 15 lm/W. A fluorescente emite 3 000 lm com 40 W: 75 lm/W, cinco vezes mais. Uma fluorescente de 8 W produz 8 × 75 = 600 lm, a mesma luz da incandescente. Então a eficiência da incandescente é <strong>menor que a de uma lâmpada fluorescente de 8 W, que produz a mesma quantidade de luz</strong>. Alternativa <strong>C</strong>.</p><p>A opção D erra a justificativa: as duas de 40 W consomem a mesma energia.</p>",
  tags=["eficiência luminosa", "potência"], enun=p(T(61, 0), T(61, 1) + " " + T(61, 2)) + fonte(T(61, 3)) + p(T(61, 4)))
X(62, "Biologia", "Ecologia", "<p>Os híbridos que escapam podem se reproduzir com as espécies nativas e competir com elas. Com o tempo, os genes híbridos podem tomar o lugar dos originais na população natural: eles podem <strong>substituir geneticamente a espécie natural</strong>. Alternativa <strong>B</strong>.</p><p>Peixes não são produtores (C), e a hibridação não modifica o código genético (E).</p>",
  tags=["hibridação", "espécies invasoras"], trocas=[("Terra da Gente", "<em>Terra da Gente</em>")])
X(63, "Biologia", "Metabolismo", "<p>As leveduras fazem fermentação alcoólica: transformam o açúcar da massa em álcool e gás carbônico. As bolhas de CO<sub>2</sub> ficam presas na massa e a fazem crescer. O crescimento resulta da <strong>liberação de gás carbônico</strong>. Alternativa <strong>A</strong>.</p><p>O ácido lático (B) é produzido por bactérias, como na fabricação de iogurte.</p>",
  tags=["fermentação", "leveduras"])
X(64, "Física", "Óptica", "<p>A luz que sai do peixe muda de direção ao passar da água para o ar (refração). O olho do índio vê o peixe na direção do raio que chega, e a imagem parece mais alta que a posição real. Por isso ele mira abaixo: os raios <strong>refletidos pelo peixe desviam sua trajetória quando passam da água para o ar</strong>. Alternativa <strong>E</strong>.</p><p>Os olhos não emitem luz (B e D).</p>",
  tags=["refração", "profundidade aparente"])
X(65, "Biologia", "Genética", "<p>Todas as células têm os mesmos genes ao longo da vida, mas eles não estão sempre ativos. A planta liga ou desliga genes conforme a época e a necessidade: o material genético <strong>possui genes transcritos diferentemente de acordo com cada necessidade</strong>. Alternativa <strong>E</strong>.</p><p>O DNA não muda (B e D) nem cria genes (C) ao longo do ano.</p>",
  tags=["expressão gênica", "regulação"], enun=p(T(65, 0) + " " + T(65, 1), T(65, 2)))
X(66, "Química", "Química orgânica", "<p>O Br<sup>+</sup> se liga ao anel e forma o carbocátion I, em que um carbono passa a ter H e Br e o anel fica com carga positiva. A partir dele, há dois caminhos: a adição, que forma o produto II, um dibromocicloexadieno, de energia maior; e a substituição, que forma o produto III, o bromobenzeno, de energia menor, porque recupera a aromaticidade. As estruturas certas estão na <strong>alternativa A</strong>. Alternativa <strong>A</strong>.</p><p>Nas outras opções, o carbocátion ou os produtos não têm o anel aromático onde deveriam.</p>",
  figs(("q66", "Gráfico de energia livre em função do progresso da reação de benzeno com Br2 e catalisador: a curva sobe até um máximo, desce ao carbocátion (I) num vale, sobe de novo e se divide em dois caminhos, um que termina mais alto, no produto (II), e outro que termina mais baixo, no produto (III)."),
       ("q66a", "Alternativa A: I, anel com carga positiva e um carbono com H e Br; II, anel com duas ligações duplas e dois Br em carbonos vizinhos; III, bromobenzeno (anel aromático com um Br)."),
       ("q66b", "Alternativa B: I, carbocátion com H e Br; II, anel com dois Br vizinhos e duas duplas; III, anel com uma dupla e um Br."),
       ("q66c", "Alternativa C: I, anel com uma dupla, carga positiva e um carbono com H e Br; II, anel aromático com dois Br; III, bromobenzeno."),
       ("q66d", "Alternativa D: I, anel com uma dupla e carbocátion; II, anel com dois Br e duas duplas; III, anel com duas duplas e um Br."),
       ("q66e", "Alternativa E: I, anel com uma dupla e carbocátion; II, anel aromático com dois Br; III, anel com duas duplas e um Br.")),
  ["substituição eletrofílica", "diagrama de energia"],
  enun=p(T(66, 0)) + fonte(T(66, 1)) + "[[fig:1]]" + fonte("Disponível em: www.qmc.ufsc.br. Acesso em: 1 mar. 2012 (adaptado).") + p(T(66, 4)), alts=ALT(2))
X(67, "Física", "Hidrostática", "<p>A pressão da água num ponto depende da altura da coluna de água acima dele, contada a partir da superfície livre da água na caixa. A ducha fica na saída do cano, então a altura que importa vai da superfície da água até esse ponto: <strong>h3</strong>. Alternativa <strong>C</strong>.</p><p>h4 e h5 são medidas a partir do fundo ou do topo da caixa, e não da superfície da água.</p>",
  figs(("q67", "Esquema de uma caixa-d’água com água, presa no alto de uma parede, e um cano que desce e faz uma curva perto do chão, onde se liga a ducha. Setas indicam cinco alturas: h1 e h2 partem do fundo da caixa, h3 parte da superfície da água até a saída do cano, h4 e h5 vão até o piso.")),
  ["teorema de Stevin", "pressão hidrostática"], enun=p(T(67, 0)) + "[[fig:1]]" + p(T(67, 3)))
X(68, "Biologia", "Ecologia", "<p>O texto descreve o modo de vida do tamanduá: hábitos noturnos, onde descansa, como se locomove, como se reproduz e cuida do filhote, como usa o território. O conjunto de atividades e relações de uma espécie no ambiente é o seu <strong>nicho ecológico</strong>. Alternativa <strong>D</strong>.</p><p>Hábitat (A) é só o lugar onde vive.</p>",
  tags=["nicho ecológico", "hábitat"], trocas=[("Ciência Hoje das Crianças", "<em>Ciência Hoje das Crianças</em>")])
X(69, "Química", "Ácidos e bases", "<p>O cheiro de peixe vem das aminas, que são bases. Para neutralizá-las, usa-se um material ácido, com [H<sub>3</sub>O<sup>+</sup>] maior que 10<sup>−7</sup> mol/L. Os mais ácidos da tabela são o <strong>suco de limão</strong> (10<sup>−2</sup>) e o <strong>vinagre</strong> (10<sup>−3</sup>). Alternativa <strong>C</strong>.</p><p>Sabão e barrilha (E) são básicos e não neutralizariam as aminas.</p>",
  tags=["neutralização", "pH"],
  enun=p(T(69, 0), T(69, 1).replace("hidrogeniônicas", "hidrogeniônicas")) + tabela(["Material", "Concentração de H<sub>3</sub>O<sup>+</sup> (mol/L)"],
    [["Suco de limão", "10<sup>−2</sup>"], ["Leite", "10<sup>−6</sup>"], ["Vinagre", "10<sup>−3</sup>"], ["Álcool", "10<sup>−8</sup>"], ["Sabão", "10<sup>−12</sup>"], ["Carbonato de sódio/barrilha", "10<sup>−12</sup>"]]) + p(T(69, 3)))
X(70, "Química", "Química orgânica", "<p>O para-dodecil-benzenossulfonato de sódio é um detergente: tem uma cauda apolar, que interage com o hidrocarboneto, e uma cabeça iônica, que interage com a água. Ele forma micelas que envolvem o hidrocarboneto e o dispersam na água: a solução <strong>possibilita a solubilização do hidrocarboneto</strong>. Alternativa <strong>D</strong>.</p><p>O detergente não reage quimicamente com o hidrocarboneto (A, C e E).</p>",
  tags=["tensoativos", "micelas"])
X(71, "Física", "Energia", "<p>O país tem ventos constantes, relevo plano, poucos rios e nenhum combustível fóssil. A melhor escolha é a energia <strong>eólica, pelas características do país e por não gerar gases do efeito estufa nem resíduos de operação</strong>. Alternativa <strong>E</strong>.</p><p>A hidráulica (D) exige rios e desníveis, e o país é chuvoso, o que reduz a eficiência da solar (B).</p>",
  tags=["matriz energética", "energia eólica"])
X(72, "Física", "Cinemática", "<p>No primeiro trecho, 80 km a 80 km/h levam 1 h. No segundo, 60 km a 120 km/h levam 0,5 h. O tempo total é <strong>1,5 h</strong>. Alternativa <strong>C</strong>.</p><p>Usar a média das velocidades (100 km/h) daria 1,4 h (B), mas cada trecho tem um tempo diferente.</p>",
  tags=["velocidade média", "tempo"])
X(73, "Física", "Eletrodinâmica", "<p>Na ligação de interruptores paralelos (three-way), a lâmpada fica em série entre a rede e o polo de um interruptor, os dois terminais de um interruptor são ligados aos dois terminais do outro, e o polo do segundo vai para a rede. Assim, mudar qualquer chave abre ou fecha o caminho. Só o <strong>circuito E</strong> liga os terminais de forma cruzada entre os dois interruptores, com a lâmpada ligada ao polo de um deles. Alternativa <strong>E</strong>.</p><p>Nos outros, alguma posição deixa a lâmpada sempre acesa, sempre apagada ou em curto.</p>",
  figs(("q73", "Interruptor com um polo e dois terminais em duas posições: na posição I, a chave liga o polo ao terminal superior; na posição II, ao terminal inferior."),
       ("q73a", "Alternativa A: dois interruptores lado a lado, com a lâmpada ligada à direita e os fios cruzando de modo que um dos terminais do primeiro fica sem ligação."),
       ("q73b", "Alternativa B: dois interruptores, a lâmpada no alto à direita, com os fios ligando o polo do primeiro ao terminal do segundo."),
       ("q73c", "Alternativa C: lâmpada no alto entre dois interruptores, com os terminais ligados por fios que passam por baixo."),
       ("q73d", "Alternativa D: lâmpada entre os dois interruptores, ligada a um terminal de cada um."),
       ("q73e", "Alternativa E: lâmpada ligada ao polo do primeiro interruptor; os dois terminais do primeiro estão ligados aos dois terminais do segundo; o polo do segundo vai para a rede.")),
  ["interruptor paralelo", "circuitos"], enun=p(T(73, 0)) + "[[fig:1]]" + p(T(73, 3)), alts=ALT(2))
X(74, "Física", "Gravitação", "<p>Visto da Terra, Marte às vezes parece andar para trás e faz um laço no céu. Isso acontece porque a Terra, mais perto do Sol, anda mais rápido na órbita e, em certas épocas, ultrapassa Marte: <strong>a maior velocidade orbital da Terra faz com que, em certas épocas, ela ultrapasse Marte</strong>. Alternativa <strong>A</strong>.</p><p>O laço é um efeito de perspectiva, e não uma mudança real na órbita de Marte (C, D e E).</p>",
  figs(("q74", "Gráfico do céu com graduação de 155° a 130° na parte de cima: as posições de Marte, marcadas a cada 10 dias, formam uma linha que avança, faz um laço para trás e volta a avançar; há estrelas espalhadas ao redor e uma linha tracejada embaixo.")),
  ["movimento retrógrado", "órbitas"], enun=p(T(74, 0)) + "[[fig:1]]" + fonte("<em>Projecto Física</em>. Lisboa: Fundação Calouste Gulbenkian, 1980 (adaptado).") + p(T(74, 4)))
X(75, "Biologia", "Origem da vida", "<p>Redi mostrou que larvas só aparecem na carne quando moscas põem ovos nela, e Pasteur, com os frascos de pescoço de cisne, mostrou que microrganismos vêm de outros microrganismos. Ambos indicaram que <strong>o ser vivo é oriundo da reprodução de outro ser vivo pré-existente</strong> (biogênese). Alternativa <strong>C</strong>.</p><p>A alternativa E é a própria geração espontânea, que eles refutaram.</p>",
  tags=["biogênese", "Redi e Pasteur"])
X(76, "Química", "Ácidos e bases", "<p>O HCℓ é um gás ácido. Para retê-lo, borbulha-se o gás numa solução básica, que o neutraliza. A água de cal, solução de Ca(OH)<sub>2</sub>, reage com o HCℓ formando sal e água. A resposta é <strong>água de cal</strong>. Alternativa <strong>B</strong>.</p><p>Água destilada ou desmineralizada (D e E) só dissolveria o gás, formando ácido clorídrico.</p>",
  tags=["neutralização", "poluição"])
X(77, "Física", "Hidrostática", "<p>A água subiu de 1,0 L para 1,5 L: o volume submerso dos legumes é 0,5 L. Como 1/3 ficou fora, a parte submersa é 2/3 do total, e o volume total é 0,5 ÷ (2/3) = 0,75 L = 750 cm³. Com densidade 0,5 g/cm³, a massa é 375 g = <strong>0,375 kg</strong>. Alternativa <strong>D</strong>.</p><p>Usar só o volume submerso daria 0,250 kg (C).</p>",
  tags=["densidade", "empuxo"],
  enun=p(T(77, 0), "Ele coloca uma porção dos legumes que comprou dentro do recipiente e observa que a água atinge a marca de 1,5 litro e também que a porção não ficara totalmente submersa, com \\(\\tfrac{1}{3}\\) de seu volume fora d’água. Para concluir o teste, o consumidor, com ajuda da internet, verifica que a densidade dos legumes, em questão, é a metade da densidade da água, onde \\(\\rho_{\\text{água}} = 1\\ \\dfrac{\\text{g}}{\\text{cm}^3}\\).", T(77, 5), T(77, 6)))
X(78, "Física", "Leis de Newton", "<p>Sem ABS, o atrito estático cresce com a pressão no pedal até o máximo; quando a roda trava, passa a valer o atrito cinético, menor e constante. Com ABS, o sistema solta a roda sempre que ela está perto de travar, e o atrito fica oscilando perto do máximo estático, em forma de serra. Essa combinação está na <strong>alternativa A</strong>. Alternativa <strong>A</strong>.</p><p>Na E, o gráfico do carro com ABS é constante, o que não mostra a liberação repetida das rodas.</p>",
  figs(("q78a", "Alternativa A: sem ABS, o atrito sobe em reta e cai para um valor constante menor; com ABS, sobe em reta e cai várias vezes, como uma serra."),
       ("q78b", "Alternativa B: sem ABS, reta pouco inclinada; com ABS, reta mais inclinada."),
       ("q78c", "Alternativa C: sem ABS, reta crescente; com ABS, valor constante."),
       ("q78d", "Alternativa D: sem ABS, sobe e desce em forma de triângulo; com ABS, serra."),
       ("q78e", "Alternativa E: sem ABS, sobe e cai para um valor constante; com ABS, valor constante.")),
  ["atrito estático e cinético", "freios ABS"],
  enun=p(T(78, 0), "As representações esquemáticas da força de atrito <em>f</em><sub>at</sub> entre os pneus e a pista, em função da pressão <em>p</em> aplicada no pedal de freio, para carros sem ABS e com ABS, respectivamente, são:"), alts=ALT(1))
X(79, "Química", "Forças intermoleculares", "<p>As vitaminas que precisam ser repostas todo dia são as hidrossolúveis, que o corpo não armazena e elimina na urina. A vitamina III (ácido ascórbico, vitamina C) tem vários grupos OH, que fazem ligações de hidrogênio com a água. As outras têm longas cadeias de carbono e são lipossolúveis. A resposta é a <strong>III</strong>. Alternativa <strong>C</strong>.</p>",
  figs(("q79", "Fórmulas estruturais de cinco vitaminas: I, com anel e longa cadeia de carbonos terminada em OH (vitamina A); II, com dois anéis e longa cadeia ramificada (vitamina K); III, anel pequeno com vários grupos OH e uma cadeia curta com OH (vitamina C); IV, estrutura de vários anéis com cadeia de carbonos e um OH (vitamina D); V, anel com OH e longa cadeia ramificada (vitamina E).")),
  ["vitaminas", "polaridade"], enun=p(T(79, 0).replace("estuturas", "estruturas")) + "[[fig:1]]" + p(T(79, 6)))
X(80, "Biologia", "Saúde", "<p>O Garfield está acima do peso. A obesidade é fator de risco para o diabetes tipo 2, por causar resistência à insulina, além de hipertensão e doenças cardíacas. A doença é o <strong>diabetes</strong>. Alternativa <strong>C</strong>.</p><p>Beribéri e escorbuto (B e D) vêm da falta de vitaminas, e a fenilcetonúria (E) é genética.</p>",
  figs(("q80", "Tirinha do Garfield em três quadros: ele se olha no espelho e pensa “Puxa, como estou fora de forma!”; depois, “Só há uma coisa a fazer!”; por fim, empurra o espelho e pensa “Se não pode perder as banhas, amarre-as!”.")),
  ["obesidade", "diabetes"], enun="[[fig:1]]" + fonte("DAVIS, J. <em>Garfield está de dieta</em>. Porto Alegre: L&amp;PM, 2006.") + p(T(80, 1)),
  alts={**D[80]["alternativas"], "E": "fenilcetonúria."})
X(81, "Biologia", "Ecologia", "<p>A poeira levantada pelo asteroide bloqueou a luz do Sol. Sem luz, as plantas e algas fizeram menos fotossíntese, e a falta de alimento passou para herbívoros e carnívoros. A extinção veio porque as modificações <strong>reduziram a penetração da luz solar até a superfície da Terra, interferindo no fluxo energético das teias tróficas</strong>. Alternativa <strong>B</strong>.</p>",
  tags=["extinção dos dinossauros", "fotossíntese"])
X(82, "Química", "Eletroquímica", "<p>O magnésio protege o alumínio porque se oxida antes dele: tem potencial de redução menor (−2,36 V contra −1,66 V). Os metais com potencial menor que o do alumínio, e que poderiam cumprir a mesma função, são o lítio (−3,05 V) e o potássio (−2,93 V). Alternativa <strong>E</strong>.</p><p>Cobre e zinco (B e D) têm potencial maior que o do alumínio e se oxidariam depois dele.</p>",
  tags=["metal de sacrifício", "potencial de redução"],
  enun=p(T(82, 0)) + tabela(["Semirreação", "Potencial padrão de redução (V)"], [["Li<sup>+</sup> + e<sup>−</sup> → Li", "−3,05"], ["K<sup>+</sup> + e<sup>−</sup> → K", "−2,93"], ["Mg<sup>2+</sup> + 2 e<sup>−</sup> → Mg", "−2,36"], ["Al<sup>3+</sup> + 3 e<sup>−</sup> → Al", "−1,66"], ["Zn<sup>2+</sup> + 2 e<sup>−</sup> → Zn", "−0,76"], ["Cu<sup>2+</sup> + 2 e<sup>−</sup> → Cu", "+0,34"]])
  + fonte(T(82, 3)) + p(T(82, 4)))
X(83, "Física", "Termodinâmica", "<p>Um motor a combustão é uma máquina térmica. Pela segunda lei da termodinâmica, parte do calor sempre tem de ser rejeitada para uma fonte fria, e o rendimento nunca chega a 100%. O limite é <strong>um dos princípios da termodinâmica, segundo o qual o rendimento de uma máquina térmica nunca atinge o ideal</strong>. Alternativa <strong>B</strong>.</p><p>O tipo de combustível (A) não limita a eficiência, mas a disponibilidade.</p>",
  tags=["segunda lei da termodinâmica", "rendimento"])
X(84, "Física", "Física moderna", "<p>Na esterilização, a radiação atravessa o material e mata os microrganismos, mas não o torna radioativo. Ele não acumula radiação: <strong>o material é incapaz de acumular radiação, não se tornando radioativo por ter sido irradiado</strong>. Alternativa <strong>A</strong>.</p><p>As opções B, D e E supõem que o material emite radiação, o que não acontece.</p>",
  tags=["irradiação", "radioatividade"], trocas=[("Física na Escola", "<em>Física na Escola</em>")])
X(85, "Biologia", "Botânica", "<p>O grão de pólen leva o gameta masculino de uma planta para outra, pelo vento ou por animais, sem depender de água. A polinização cruzada mistura genes de indivíduos diferentes e aumenta a variabilidade. São <strong>os grãos de pólen, que garantem a polinização cruzada</strong>. Alternativa <strong>C</strong>.</p><p>Sementes e frutos (A e D) ajudam na dispersão, mas a mistura de genes acontece na fecundação.</p>",
  figs(("q85", "Cladograma das embriófitas (Reino Plantae): a partir de uma alga verde ancestral, saem briófitas, pteridófitas, gimnospermas e angiospermas, com as novidades marcadas no tronco: gametófito dominante e arquegônio; esporófito dominante e vasos condutores; sementes aladas e grãos de pólen; flores e frutos.")),
  ["evolução das plantas", "polinização"])
X(86, "Biologia", "Citologia", "<p>A solução de 0,20 mol/L é hipertônica em relação à célula (equivalente a 0,15 mol/L). Por osmose, a água passa do meio menos concentrado para o mais concentrado: há <strong>transferência de moléculas de água do interior da célula para a solução</strong>, e a célula murcha. Alternativa <strong>E</strong>.</p><p>Na osmose quem se move é o solvente, a água, e não os íons (B e D).</p>",
  tags=["osmose", "solução hipertônica"])
X(87, "Biologia", "Saúde", "<p>O barbeiro se alimenta de sangue de animais silvestres. Com o desmatamento, esses animais somem ou migram, e o inseto passa a buscar sangue humano nas casas próximas: <strong>o desmatamento que provoca a migração ou o desaparecimento dos animais silvestres dos quais o barbeiro se alimenta</strong>. Alternativa <strong>E</strong>.</p><p>A doença é transmitida pelo inseto, e não pela falta de saneamento (C).</p>",
  tags=["doença de Chagas", "desmatamento"], trocas=[("Trypanosoma cruzi", "<em>Trypanosoma cruzi</em>")])
X(88, "Física", "Ondas", "<p>O bronzeamento é causado pela radiação ultravioleta, de alta frequência. A lâmpada incandescente emite sobretudo luz visível e infravermelho, de frequências mais baixas. Ela não bronzeia porque sua luz é de <strong>baixa frequência</strong>. Alternativa <strong>B</strong>.</p><p>Curto comprimento de onda (E) seria o caso do ultravioleta, o oposto.</p>",
  tags=["ultravioleta", "espectro eletromagnético"], trocas=[("O bronzeamente", "O bronzeamento")])
X(89, "Química", "Forças intermoleculares", "<p>Cada fosfolipídio tem uma cabeça polar, que interage com a água, e duas caudas apolares, que fogem dela. Na bicamada, as cabeças ficam voltadas para a água e as caudas, escondidas no meio. Isso ocorre porque eles têm natureza <strong>anfifílica, ou seja, possuem uma parte hidrofílica e outra hidrofóbica</strong>. Alternativa <strong>E</strong>.</p>",
  figs(("q89", "Esquema de um lipossomo: uma esfera formada por duas camadas de fosfolipídios, com as cabeças circulares voltadas para o meio aquoso de dentro e de fora e as caudas voltadas para o interior da bicamada.")),
  ["fosfolipídios", "bicamada lipídica"])
X(90, "Química", "Mol", "<p>O IDA é 40 mg por kg: para 70 kg, 2 800 mg = 2,8 g por dia. Em mol: 2,8 ÷ 294 ≈ <strong>9,5 × 10<sup>−3</sup> mol</strong>. Alternativa <strong>B</strong>.</p><p>A opção A divide 40 mg (sem multiplicar pela massa da pessoa) pela massa molar.</p>",
  tags=["quantidade de matéria", "IDA"], trocas=[("refrigerantes diet", "refrigerantes <em>diet</em>")],
  alts={"A": "1,3 × 10<sup>−4</sup>.", "B": "9,5 × 10<sup>−3</sup>.", "C": "4 × 10<sup>−2</sup>.", "D": "2,6.", "E": "823."})

completar(Q, R)
