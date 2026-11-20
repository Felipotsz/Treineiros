# Enem 2025, 2º dia, caderno azul: Ciências da Natureza (questões 91 a 135 do caderno; no site, 1 a 45, com numeroOriginal).
# Texto dos blocos do PDF (tools/enem_rascunho.py); fórmulas com sub/sup; figuras recortadas pelas caixas do PDF (recortes.json).
# Questões 123 e 132 anuladas pelo Inep (com a 174, de Matemática) após relatos de antecipação de itens semelhantes.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, enunciado_enem, paragrafos_enem

ID = "enem-2025-natureza"
META = {"id": ID, "banca": "Enem", "ano": 2025, "titulo": "Enem 2025: Ciências da Natureza", "fonte": "Inep", "dataExame": "2025-11-16",
        "duracaoMinutos": 150, "area": "Ciências da Natureza", "caderno": "azul", "dia": 2}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2025-dia2-azul")
Q = {}
P = lambda n: paragrafos_enem(D[n])
p = lambda *xs: "".join(f"<p>{x}</p>" for x in xs)
ap = lambda *xs: "".join(f'<p class="apoio">{x}</p>' for x in xs)
fonte = lambda x: f'<p class="fonte">{x}</p>'
ANUL = ('<p>O Inep anulou esta questão e outras duas do 2º dia (no caderno azul, 123, 132 e 174) depois de relatos de que itens parecidos '
        'tinham sido divulgados nas redes sociais antes da prova. Segundo o Inep, nenhuma questão foi divulgada igual à da prova, só com '
        '“similaridades pontuais”, e o caso foi enviado à Polícia Federal. A anulação não aponta erro no conteúdo da questão.</p>')


def quim(s):
    """Índices de fórmulas químicas em subscrito (CO2 → CO<sub>2</sub>), cargas em sobrescrito."""
    s = re.sub(r"(?<=[A-Z\)a-z])(\d+)(?=[A-Z(\s,.;:)]|$|<)", r"<sub>\1</sub>", s)
    return s.replace("S2−", "S<sup>2−</sup>").replace("H+", "H<sup>+</sup>").replace("Al3+", "Al<sup>3+</sup>").replace("e−", "e<sup>−</sup>")


def figs(*pares):
    return [{"arquivo": a, "alt": t} for a, t in pares]


ALT_FIG = {k: f"[[fig:{i}]]" for i, k in enumerate("ABCDE", 2)}


def X(n, materia, assunto, expl, imagens=(), tags=(), enun=None, trocas=(), alts=None, q_=None, anulacao=None):
    q = {"materia": materia, "assunto": assunto, "area": "Ciências da Natureza", "tags": list(tags), "numeroOriginal": n,
         "enunciado": enun or enunciado_enem(D[n], trocas), "alternativas": dict(alts or D[n]["alternativas"]),
         "imagens": list(imagens), "explicacao": expl}
    if q_: q["enunciado"] = quim(q["enunciado"]); q["alternativas"] = {k: quim(v) for k, v in q["alternativas"].items()}
    if anulacao: q["anulacao"] = anulacao
    Q[n - 90] = q


X(91, "Química", "Separação de misturas", "<p>A adsorção acontece na superfície do sólido: as impurezas ficam presas nas paredes dos poros. A figura mostra que o carvão ativado tem muito mais poros (macro, meso e microporos) que o comum, ou seja, muito mais <strong>superfície</strong> de contato para reter contaminantes. Alternativa <strong>D</strong>.</p><p>Massa, dureza, densidade e condutividade (A, B, C e E) não determinam quanto material fica adsorvido.</p>",
  figs(("q91", "Dois círculos cinza comparando estruturas. Carvão comum: poucos poros pequenos, indicados como mesoporos. Carvão ativado: superfície recortada, com macroporos, mesoporos e microporos, e pontinhos pretos de “impureza adsorvida” presos nas paredes.")),
  ["adsorção", "carvão ativado"])
X(92, "Biologia", "Biotecnologia", "<p>A <em>E. coli</em> recebeu os genes do relógio circadiano da cianobactéria e manteve seu próprio genoma, inclusive os genes do metabolismo. Como a <em>E. coli</em> é “um organismo não circadiano”, ela não tinha genes de ciclo circadiano próprios. O organismo modificado tem os genes do <strong>ciclo circadiano de <em>S. elongatus</em> e do metabolismo de <em>E. coli</em></strong>. Alternativa <strong>D</strong>.</p><p>A e B ignoram os genes transferidos; C troca as origens; E supõe um ciclo circadiano da <em>E. coli</em>, que não existe.</p>",
  tags=["transgênicos", "ciclo circadiano"], trocas=[("cianobactéria Synechococcus elongatus", "cianobactéria <em>Synechococcus elongatus</em>"), ("bactéria Escherichia coli", "bactéria <em>Escherichia coli</em>")],
  alts={k: v.replace("E. coli", "<em>E. coli</em>").replace("S. elongatus", "<em>S. elongatus</em>") for k, v in D[92]["alternativas"].items()})
X(93, "Biologia", "Zoologia", "<p>As aves aquáticas espalham nas penas, com o bico, a secreção oleosa da <strong>glândula uropigial</strong>, que as impermeabiliza. Com menos secreção, as penas encharcam, a ave perde a flutuação e pode se afogar. Alternativa <strong>C</strong>.</p><p>Papo, troca de penas, membrana natatória e ossos pneumáticos (A, B, D e E) não explicam o encharcamento das penas.</p>",
  tags=["aves", "adaptações"])
X(94, "Física", "Eletrodinâmica", "<p>A régua suporta P = U · i = 110 · 20 = 2 200 W. Computador e ar-condicionado já somam 250 + 1 100 = 1 350 W.</p><ul><li>1º: impressora: 1 350 + 660 = 2 010 W ≤ 2 200 W, funciona.</li><li>2º: cafeteira: 1 350 + 900 = 2 250 W &gt; 2 200 W, o fusível queima.</li></ul><p>Depois disso a régua fica inutilizada. Só <strong>1</strong> atividade foi realizada. Alternativa <strong>D</strong>.</p><p>Quem não percebe que o fusível queimado inutiliza a régua conta também a luminária (3ª), chegando a 2 (C).</p>",
  figs(("q94", "Quadro de potências: luminária de LED, 5 W; computador, 250 W; impressora a laser, 660 W; secador de cabelos, 750 W; cafeteira, 900 W; condicionador de ar portátil, 1 100 W. Ao lado, a foto de uma régua com seis tomadas e um interruptor.")),
  ["potência elétrica", "fusível"])
X(95, "Física", "Termologia", "<p>Condução e convecção precisam de um meio material (a convecção, de um fluido). A transferência que acontece até no vácuo, por ondas eletromagnéticas (infravermelho), é a <strong>irradiação</strong>: é assim que a lâmpada aquece a mariposa. Alternativa <strong>C</strong>.</p><p>Reflexão, refração e dispersão (A, B e D) são fenômenos ópticos, não processos de transferência de calor; a convecção depende de fluido (E).</p>",
  tags=["irradiação térmica"], trocas=[("<strong>TEXTO I As mariposas</strong>", "<strong>TEXTO I</strong></p><p class=\"apoio\"><strong>As mariposas</strong>"),
                                       ("As mariposa, quando chega o frio Fica dando volta em volta da lâmpida pra se esquentá. [sic]", "As mariposa, quando chega o frio<br>Fica dando volta em volta da lâmpida<br>pra se esquentá. [sic]")])
X(96, "Biologia", "Ecologia", "<p>O texto diz que o veneno vem da dieta: os sapos o obtêm comendo formigas e cupins que se alimentam de plantas tóxicas. Em cativeiro, sem esse alimento, não acumulam a toxina. A causa é a <strong>ausência da alimentação natural</strong>. Alternativa <strong>B</strong>.</p><p>Umidade, adaptação, comportamento e genética (A, C, D e E) não explicam, já que os mesmos animais capturados também perdem a toxicidade.</p>",
  tags=["anfíbios", "cadeia alimentar"])
X(97, "Biologia", "Imunologia", "<p>A vacina usa o vírus inativado como antígeno. Ele não causa a doença, mas é reconhecido pelo sistema imune, que produz anticorpos, <strong>proteínas que neutralizam o vírus</strong>, e células de memória. Alternativa <strong>D</strong>.</p><p>O antígeno não mata nem aglutina o vírus (A e B): quem faz isso são os anticorpos. A vacina não contém imunoglobulinas (C; isso é soro), e ela induz anticorpos novos, não mantém os que já existiam (E).</p>",
  figs(("q97", "Esquema das etapas de uma vacina tradicional: 1, a partir da cultura de células infectadas com vírus, faz-se o isolamento dos vírus; 2, inativação dos vírus pelo calor ou por ação química; 3, aplicação da vacina numa pessoa; 4, no organismo, surgem anticorpos (em forma de Y) ligados aos vírus.")),
  ["vacinas", "anticorpos"])
X(98, "Biologia", "Ecologia", "<p>O capim-gordura é uma espécie exótica invasora, “agressiva” e competitiva, que se espalha e ocupa o espaço das plantas nativas. Em longo prazo, isso tende a <strong>diminuir as espécies nativas do bioma</strong>. Alternativa <strong>D</strong>.</p><p>Espécies invasoras reduzem nichos, não os diversificam (A), e o capim seco aumenta o risco de queimadas (E). Assoreamento e infiltração (B e C) não decorrem do texto.</p>",
  tags=["espécies invasoras", "Cerrado"])
X(99, "Biologia", "Ecologia", "<p>O monstro de gila vive num deserto, onde falta alimento. Se lagartos do mesmo grupo têm adaptações parecidas em ambientes parecidos, o mais provável é encontrá-los no bioma brasileiro mais seco, de clima semiárido e escassez sazonal de recursos: a <strong>Caatinga</strong>. Alternativa <strong>C</strong>.</p><p>Cerrado, Pampas, Restinga e Pantanal (A, B, D e E) não têm as condições quase desérticas descritas.</p>",
  tags=["biomas", "convergência adaptativa"])
X(100, "Química", "Soluções", "<p>A água sem sais dissolvidos, usada em laboratórios, como solvente e em baterias, é a <strong>água destilada</strong> (ou deionizada). Bebê-la com frequência pode causar falta de íons. Alternativa <strong>D</strong>.</p><p>Água dura tem muitos sais de cálcio e magnésio (A); pesada é a de deutério (B); sanitária é a solução de hipoclorito (C); e oxigenada é a de peróxido de hidrogênio (E).</p>",
  tags=["água destilada"])
X(101, "Física", "Óptica", "<p>No escuro, a pupila fica <strong>dilatada</strong> para captar mais luz. Quando o flash dispara, entra muita luz, que reflete no fundo do olho, rico em vasos sanguíneos, e sai vermelha na foto. Com a pupila aberta, <strong>chega mais luz à retina</strong>, e mais luz volta. Alternativa <strong>A</strong>.</p><p>Em ambiente escuro, a pupila não está retraída (B, C e D), e a cor vermelha vem do reflexo nos vasos, não de menos luz azul e verde nos bastonetes (E).</p>",
  tags=["pupila", "olho humano"], trocas=[("<p class=\"apoio\">Por que os olhos ficam vermelhos em algumas fotografias?</p>", "<p class=\"apoio\"><strong>Por que os olhos ficam vermelhos em algumas fotografias?</strong></p>")])
X(102, "Biologia", "Doenças e saúde", "<p>A tetrodotoxina é <strong>termoestável</strong> (não se destrói com o calor) e fica nas gônadas e vísceras. O que evita a intoxicação é <strong>manusear o peixe sem romper os órgãos internos</strong>, para a toxina não contaminar o filé. Alternativa <strong>E</strong>.</p><p>Cozinhar ou fritar não adianta (C), porque a toxina resiste ao calor; higiene, criação em cativeiro ou tipo de rede (A, B e D) não impedem que a toxina chegue à carne.</p>",
  tags=["toxinas", "baiacu"])
X(103, "Biologia", "Citologia", "<p>A lipase ácida é uma enzima digestiva que atua em pH ácido, dentro dos <strong>lisossomos</strong>, organelas que degradam lipídios, proteínas e outras moléculas. Sem ela, colesterol esterificado e triglicerídeos se acumulam nas células. Alternativa <strong>A</strong>.</p><p>Ribossomos fazem proteínas (B), mitocôndrias fazem a respiração celular (C), peroxissomos degradam peróxidos e ácidos graxos de cadeia longa em pH neutro (D), e o retículo liso sintetiza lipídios (E).</p>",
  tags=["lisossomos", "doenças de depósito"])
X(104, "Biologia", "Ecologia", "<p>A pergunta é qual ação <strong>remove</strong> o CO<sub>2</sub> que já está na atmosfera. As árvores retiram CO<sub>2</sub> do ar pela fotossíntese e o fixam na biomassa: <strong>plantar mais árvores</strong>. Alternativa <strong>A</strong>.</p><p>Usinas eólicas, energia solar, deixar o petróleo no solo e produzir menos lixo (B, C, D e E) reduzem as emissões, mas não tiram da atmosfera o CO<sub>2</sub> que já está lá.</p>",
  tags=["efeito estufa", "sequestro de carbono"], q_=True)
X(105, "Química", "Química ambiental", "<p>Se a refrigeração é ineficiente, a água devolvida ao rio ou ao mar sai mais quente. Gases se dissolvem menos em água quente, e a <strong>solubilidade do gás oxigênio diminui</strong>, prejudicando peixes e outros organismos. É a poluição térmica. Alternativa <strong>E</strong>.</p><p>A água de refrigeração não entra em contato com o reator nem com o combustível, por isso não leva radioatividade nem combustível (C e D); a poluição térmica não libera gases (B) nem baixa o pH (A).</p>",
  figs(("q105", "Esquema de uma usina termonuclear: no vaso de contenção, o reator com o elemento combustível, o pressurizador e uma bomba formam o circuito primário (amarelo), que passa pelo gerador de vapor; o vapor do circuito secundário (azul) gira a turbina ligada ao gerador elétrico e à torre de transmissão, passa pelo condensador e volta pelo tanque de água de alimentação; o sistema de água de refrigeração (verde) traz água fria de um ecossistema aquático ao condensador e a devolve, havendo também uma torre de resfriamento.")),
  ["poluição térmica", "solubilidade de gases"])
X(106, "Química", "Funções inorgânicas", "<p>Basta trocar N por Az. Ácido nítrico, HNO<sub>3</sub>, vira <strong>HAzO<sub>3</sub></strong> (como NaNO<sub>3</sub> virava NaAzO<sub>3</sub>). O cloreto de cálcio não tem nitrogênio e continua <strong>CaCl<sub>2</sub></strong>. Alternativa <strong>A</strong>.</p><p>B e C erram as fórmulas; D e E trocam cálcio por potássio (K).</p>",
  figs(("q106", "Fotografia antiga de uma aula de química num colégio de Santos (1909), com alunos diante de uma lousa; ao lado, a ampliação do que está escrito na lousa: AzO + O = AzO², SO² + H²O = H²SO³, 2 H²SO³ + O² = 2 H²SO⁴, 2 HCl + MgO²H² = MgCl² + 2 H²O (os índices eram escritos no alto).")),
  ["nomenclatura", "história da química"], q_=True)
X(107, "Biologia", "Genética", "<p>Pais puros: macho de quatro pintas × fêmea de listra. A primeira geração tem as duas marcas ao mesmo tempo (pintas e listra): é <strong>codominância</strong>, e todos são heterozigotos. Cruzando F1 × F1, a proporção é 1 só pintas : 2 pintas e listra : 1 só listra. Entre quatro filhotes, isso dá um de pintas, um de listra e dois com as duas marcas. Alternativa <strong>E</strong>.</p><p>A e B mostram só um fenótipo; C e D mostram três de um tipo e um de outro (3 : 1), padrão de dominância completa, que não se vê na F1.</p>",
  figs(("q107", "Parentais: macho com quatro pintas pretas × fêmea com uma listra preta no meio das costas. Primeira geração: macho e fêmea com quatro pintas e a listra ao mesmo tempo."),
       ("q107a", "Alternativa A: quatro joaninhas, todas com quatro pintas (machos e fêmeas)."),
       ("q107b", "Alternativa B: quatro joaninhas, todas só com a listra."),
       ("q107c", "Alternativa C: quatro joaninhas, todas com pintas e listra."),
       ("q107d", "Alternativa D: duas com quatro pintas e duas só com a listra."),
       ("q107e", "Alternativa E: uma com quatro pintas, uma só com a listra e duas com pintas e listra.")),
  ["codominância", "proporção fenotípica"], enun=p(P(107)[1][1]) + "[[fig:1]]" + p(P(107)[2][1]), alts=ALT_FIG)
X(108, "Física", "Dinâmica", "<p>A caixa está sempre deslizando, então o atrito é <strong>cinético</strong>: f = μ · N. No plano inclinado, N = m · g · cos θ, que é constante, e a rugosidade (μ) não muda. A força que o trabalhador faz não altera o atrito. No trecho do plano, a força de atrito é <strong>constante</strong>. Alternativa <strong>C</strong>.</p><p>Os gráficos que sobem ou descem acompanham a força do trabalhador (A, B, D e E), confusão comum: ela não muda a normal nem o atrito cinético.</p>",
  figs(("q108a", "Alternativa A: força de atrito × tempo que cai, depois sobe e fica constante num valor mais alto."),
       ("q108b", "Alternativa B: força de atrito que sobe, depois cai e fica constante num valor baixo."),
       ("q108c", "Alternativa C: força de atrito constante ao longo do tempo (reta horizontal)."),
       ("q108d", "Alternativa D: força de atrito constante e depois decrescente."),
       ("q108e", "Alternativa E: força de atrito que sobe e depois diminui aos poucos.")),
  ["atrito cinético", "plano inclinado"], enun=p(D[108]["paragrafos"][0][1].replace("arrasta-lá", "arrastá-la").split(" O comportamento")[0], "O comportamento" + D[108]["paragrafos"][0][1].split(" O comportamento")[1]),
  alts={k: f"[[fig:{i}]]" for i, k in enumerate("ABCDE", 1)})
X(109, "Química", "Reações orgânicas", "<p>No esquema, o ácido anacárdico (que tem o grupo –COOH) vira cardanol e <strong>CO<sub>2</sub></strong> sob aquecimento: o grupo carboxila sai como gás carbônico. É uma <strong>descarboxilação</strong>. Alternativa <strong>E</strong>.</p><p>Não há entrada de água (A), de fenila (B), de H<sub>2</sub> (D) nem formação de éster (C).</p>",
  figs(("q109", "Esquema: ácido anacárdico (anel benzênico com OH, COOH e uma cadeia C₁₅H₃₁), aquecido a 180–200 °C, forma cardanol (anel com OH e a cadeia C₁₅H₃₁) mais CO₂.")),
  ["descarboxilação", "LCC"])
X(110, "Química", "Radioatividade", "<p>26,5 anos ÷ 5,3 anos = 5 meias-vidas. A massa cai pela metade cinco vezes: 2,00 → 1,00 → 0,50 → 0,25 → 0,125 → <strong>0,0625 mg ≈ 0,06 mg</strong>. Alternativa <strong>E</strong>.</p><p>0,13 mg (D) corresponde a quatro meias-vidas; 0,40 mg (C) é dividir 2,00 por 5, como se o decaimento fosse linear.</p>",
  tags=["meia-vida", "cobalto-60"])
X(111, "Química", "Química ambiental", "<p>Na etapa 4, as sobras do biodigestor viram fertilizante. Usá-las assim evita que excrementos e restos ricos em nutrientes (nitrogênio e fósforo) sejam jogados em rios e lagos, onde provocariam a <strong>eutrofização</strong> (proliferação de algas e falta de oxigênio). Alternativa <strong>B</strong>.</p><p>Camada de ozônio, inversão térmica e chuva ácida (C, D e E) têm a ver com poluentes atmosféricos, e o texto não trata de toxinas em plantas (A).</p>",
  figs(("q111", "Esquema de um biodigestor: 1, excrementos de vacas e porcos e restos de alimentos são misturados com água no alimentador; 2, dentro do biodigestor, bactérias decompõem os resíduos em gás metano e adubo; 3, o metano pode ser encanado para um gerador ou aquecedor; 4, as sobras servem como fertilizante.")),
  ["biodigestor", "eutrofização"])
X(112, "Biologia", "Fisiologia humana", "<p>O betacaroteno é precursor da vitamina A, essencial para formar a rodopsina, pigmento dos bastonetes da retina. A falta dessa vitamina causa a <strong>cegueira noturna</strong>. Alternativa <strong>D</strong>.</p><p>Escorbuto é falta de vitamina C (B), raquitismo, de vitamina D (C), anemia perniciosa, de B12 (E), e hemofilia é genética (A).</p>",
  tags=["vitamina A", "transgênicos"])
X(113, "Física", "Eletrostática", "<p>Na região B, o campo elétrico aponta para cima. A força sobre uma carga negativa tem sentido oposto ao campo: o elétron é empurrado <strong>para baixo</strong> e atinge o ponto inferior da tela, o <strong>2</strong>. Alternativa <strong>B</strong>.</p><p>O ponto 1 seria a resposta para uma carga positiva; 3 e 4 exigiriam campo horizontal; 5 (centro), campo nulo.</p>",
  figs(("q113a", "Figura 1: tubo de imagem com o filamento na posição A, um conjunto de placas que acelera os elétrons, a região B com duas placas horizontais e a tela, onde estão marcados os pontos 1 (em cima), 2 (embaixo), 3 e 4 (dos lados) e 5 (no centro)."),
       ("q113b", "Figura 2: um elétron (carga negativa) com velocidade horizontal para a direita entre duas placas horizontais; as linhas do campo elétrico E apontam verticalmente para cima.")),
  ["força elétrica", "campo elétrico"], trocas=[("[[fig:2]]<p class=\"apoio\"><strong>Figura 2</strong></p>", "[[fig:2]]")])
X(114, "Física", "Ondas", "<p>Toda taça tem uma frequência natural de vibração. Se a voz da Mônica tiver <strong>a mesma frequência</strong>, a taça entra em <strong>ressonância</strong>: a amplitude da vibração cresce até o vidro quebrar. Alternativa <strong>B</strong>.</p><p>O texto avisa que não é a intensidade (amplitude), descartando E; o timbre não decide a ressonância (D); reflexão e interferência não quebram a taça (A e C).</p>",
  figs(("q114", "Tirinha da Turma da Mônica: num restaurante, Mônica grita com Cebolinha e Cascão à mesa, e as taças de cristal que o garçom segura se quebram; o garçom pergunta “E quem está gritando muito?”.")),
  ["ressonância", "frequência"])
X(115, "Química", "Química orgânica", "<p>Pela estrutura, o borneol tem 10 carbonos e fórmula C<sub>10</sub>H<sub>18</sub>O. A oxidação de um álcool secundário a cetona retira dois hidrogênios (o do OH e o do carbono ligado a ele) e forma C=O. A cânfora é <strong>C<sub>10</sub>H<sub>16</sub>O</strong>. Alternativa <strong>C</strong>.</p><p>A e B têm um carbono a menos; D e E têm dois oxigênios.</p>",
  figs(("q115", "Fórmula estrutural do borneol: sistema bicíclico de carbonos com três grupos metila (CH₃) e um grupo OH num carbono do anel.")),
  ["oxidação de álcoois", "cânfora"], trocas=[("[[fig:1]]<p class=\"apoio\"><strong>Borneol</strong></p>", "[[fig:1]]")], q_=True)
X(116, "Biologia", "Ecologia", "<p>As cangas têm condições extremas (solo ácido e pobre, quase 70 °C na superfície) e abrigam espécies com “distribuição restrita”. O ambiente seleciona organismos muito especializados, que só existem ali: espécies <strong>endêmicas</strong>. Alternativa <strong>C</strong>.</p><p>Exóticas vêm de fora (A), migratórias se deslocam (B), dominantes e generalistas ocupam áreas amplas (D e E).</p>",
  tags=["endemismo", "cangas"])
X(117, "Química", "Equilíbrio químico", "<p>Pelo princípio de Le Chatelier, aumentar a concentração (pressão parcial) de um reagente desloca o equilíbrio para os produtos: <strong>aumentar a pressão parcial de Cl<sub>2</sub></strong> favorece a formação de TiCl<sub>4</sub>. Alternativa <strong>D</strong>.</p><p>Há 2 mols de gás de cada lado, então a pressão total não desloca o equilíbrio (A). A reação é endotérmica (ΔH &gt; 0), e esfriar favorece os reagentes (B). Mais O<sub>2</sub> desloca para os reagentes (C), e o TiO<sub>2</sub> é sólido, sem efeito no equilíbrio (E).</p>",
  tags=["Le Chatelier"], q_=True,
  trocas=[("<p><strong>TiO2 (s) + 2 Cl2 (g) TiCl4 (g) + O2 (g) ΔH = +175 kJ/mol</strong></p>", "<p>\\(\\text{TiO}_2\\text{ (s)} + 2\\,\\text{Cl}_2\\text{ (g)} \\rightleftharpoons \\text{TiCl}_4\\text{ (g)} + \\text{O}_2\\text{ (g)} \\qquad \\Delta H = +175\\ \\text{kJ/mol}\\)</p>")])
X(118, "Física", "Hidrostática", "<p>A pressão da pilha sobre a laje é p = ρ · g · h. Com p máximo de 10<sup>4</sup> Pa: h = 10<sup>4</sup> ÷ (1 250 · 10) = 10 000 ÷ 12 500 = <strong>0,80 m</strong>. Alternativa <strong>C</strong>.</p><p>A área de 50 m<sup>2</sup> não entra na conta, porque a pressão não depende dela. Usá-la leva a valores errados, como 0,16 m (A) ou 8,00 m (E).</p>",
  tags=["pressão"], trocas=[("50 m2", "50 m<sup>2</sup>"), ("até 104 Pa", "até 10<sup>4</sup> Pa"), ("kg/m3", "kg/m<sup>3</sup>"), ("10 m/s2", "10 m/s<sup>2</sup>")])
X(119, "Física", "Eletrodinâmica", "<p>Cada placa tem fem de 40 V e, operando, 34 V com 7,5 A. A resistência interna é r = (40 − 34) ÷ 7,5 = 0,8 Ω. Para chegar perto de 100 V (aceitando 95 V a 105 V), as placas vão em <strong>série</strong>: três placas dão fem de 3 · 40 = <strong>120 V</strong>, resistência interna 3 · 0,8 = <strong>2,4 Ω</strong> e tensão de operação 3 · 34 = 102 V, dentro da faixa. Duas placas dariam só 68 V. Alternativa <strong>B</strong>.</p><p>136 V e 3,2 Ω (A) são quatro placas, que não é o menor número; 102 V (D e E) é a tensão de operação, não a fem do gerador equivalente; 5,3 Ω (C e E) não corresponde à associação.</p>",
  figs(("q119", "Símbolo de gerador não ideal: fonte com ε = 40 V em série com um resistor r."),
       ("q119a", "Alternativa A: gerador de 136 V com resistência interna de 3,2 Ω ligado à bomba."),
       ("q119b", "Alternativa B: gerador de 120 V com resistência interna de 2,4 Ω ligado à bomba."),
       ("q119c", "Alternativa C: gerador de 120 V com resistência interna de 5,3 Ω ligado à bomba."),
       ("q119d", "Alternativa D: gerador de 102 V com resistência interna de 2,4 Ω ligado à bomba."),
       ("q119e", "Alternativa E: gerador de 102 V com resistência interna de 5,3 Ω ligado à bomba.")),
  ["geradores", "associação em série"], alts=ALT_FIG)
X(120, "Física", "Cinemática", "<p>O feixe só “vê” o invasor enquanto o corpo o atravessa. Para isso, o corpo percorre a espessura (20 cm) mais o diâmetro do feixe (15 cm): 0,35 m. O caso crítico é o mais rápido, 5,0 m/s: t = 0,35 ÷ 5,0 = 0,07 s = <strong>70 ms</strong>. Se o tempo de resposta for maior que isso, quem corre passa sem ser detectado. Alternativa <strong>B</strong>.</p><p>700 ms (E) usa a velocidade mais lenta (0,5 m/s); 30 ms (A) desconta o feixe em vez de somá-lo; 300 e 400 ms (C e D) não correspondem a nenhum caso crítico.</p>",
  figs(("q120", "Esquema de um sensor de barreira: um transmissor emite um feixe até um receptor; o diâmetro do feixe é d. Abaixo, cinco movimentos de um invasor e velocidades típicas: escalando um muro para cima, 0,5 m/s; descendo, 0,7 m/s; andando, 1,0 m/s; andando rápido, 2,0 m/s; correndo, 5,0 m/s.")),
  ["velocidade média", "sensores"])
X(121, "Química", "Funções orgânicas", "<p>A dimetilamina é uma <strong>base</strong> orgânica volátil. O vinagre (ácido acético) reage com ela e forma um sal de amônio, iônico e não volátil, que não evapora com o calor do dia. Usar <strong>vinagre</strong> é o tratamento correto. Alternativa <strong>B</strong>.</p><p>Água só dilui (A); óleo não reage (C); sal de cozinha é neutro (D); e o bicarbonato também é básico, sem efeito (E).</p>",
  tags=["aminas", "neutralização"])
X(122, "Física", "Eletromagnetismo", "<p>O campo magnético variável da bobina gera, por indução eletromagnética (lei de Faraday), <strong>correntes elétricas no fundo da panela</strong> metálica (correntes de Foucault). Essas correntes dissipam energia e <strong>aquecem a panela por efeito Joule</strong>. Alternativa <strong>D</strong>.</p><p>A panela não precisa ser imantada (A), os átomos não são “movimentados” (B), o vidro não é aquecido por radiação (C), e não há convecção no ar (E).</p>",
  figs(("q122", "Esquema de um fogão de indução: uma panela com conteúdo aquecido apoiada sobre o vidro cerâmico; abaixo, a bobina de indução cria um campo magnético (linhas vermelhas); setas indicam a transferência do calor gerado na própria panela.")),
  ["indução eletromagnética", "efeito Joule"])
X(123, "Biologia", "Fotossíntese", "<p>Pela análise do Treineiros, a resposta esperada seria a <strong>água</strong>: na fotossíntese anoxigênica, o H<sub>2</sub>S doa os elétrons (e libera enxofre); na oxigênica, quem doa elétrons é a H<sub>2</sub>O, que libera O<sub>2</sub>. Alternativa <strong>E</strong>, se a questão não tivesse sido anulada.</p>",
  tags=["fotossíntese", "bactérias"], q_=True, anulacao={"fonte": "oficial", "motivo": ANUL})
X(124, "Química", "Eletroquímica", "<p>Escurecimento: a prata é oxidada a Ag<sub>2</sub>S pelo O<sub>2</sub>, que é reduzido. ΔE° = E°(O<sub>2</sub>) − E°(Ag<sub>2</sub>S) = +1,23 − (−0,69) = <strong>+1,92 V</strong>.</p><p>Clareamento: o alumínio se oxida e reduz o Ag<sub>2</sub>S de volta a prata. ΔE° = E°(Ag<sub>2</sub>S) − E°(Al) = −0,69 − (−1,68) = <strong>+0,99 V</strong>. Alternativa <strong>B</strong>.</p><p>As demais trocam os pares ou subtraem na ordem errada.</p>",
  tags=["pilhas", "potencial de redução"], q_=True,
  trocas=[("<p class=\"apoio\"><strong>Ag2S (s) + 2 e− → 2 Ag (s) + S2− (aq) −0,69 V O2 (g) + 4 H+ (aq) + 4 e− → 2 H2O (l) +1,23 V Al3+ (aq) + 3 e− → Al (s) −1,68 V</strong></p>",
           "<p class=\"apoio\">Ag2S (s) + 2 e− → 2 Ag (s) + S2− (aq) &nbsp; E° = −0,69 V<br>O2 (g) + 4 H+ (aq) + 4 e− → 2 H2O (l) &nbsp; E° = +1,23 V<br>Al3+ (aq) + 3 e− → Al (s) &nbsp; E° = −1,68 V</p>")])
X(125, "Química", "Estequiometria", "<p>Mols de gás necessários: n = PV ÷ RT = (1,00 · 4,00) ÷ (0,082 · 453) ≈ 0,108 mol. Cada mol de NH<sub>4</sub>HCO<sub>3</sub> produz 3 mols de gás (NH<sub>3</sub>, CO<sub>2</sub> e H<sub>2</sub>O), então seriam 0,036 mol de bicarbonato. Com rendimento de 80%: 0,036 ÷ 0,80 ≈ 0,045 mol. Massa: 0,045 · 79 ≈ <strong>3,5 g</strong>. Alternativa <strong>B</strong>.</p><p>Esquecer o rendimento dá 2,8 g; esquecer que são 3 gases leva a valores como 8,9 g (E) ou 6,8 g (D).</p>",
  tags=["gases ideais", "rendimento"], q_=True,
  trocas=[("<strong>NH4HCO3 (s) → NH3 (g) + CO2 (g) + H2O (g)</strong>", "NH4HCO3 (s) → NH3 (g) + CO2 (g) + H2O (g)"), ("g ⋅ mol−1", "g ⋅ mol<sup>−1</sup>"), ("mol−1 ⋅ K−1", "mol<sup>−1</sup> ⋅ K<sup>−1</sup>")])
X(126, "Física", "Cinemática", "<p>Em relação ao solo, o avião precisa percorrer 20 km para Leste, 20 km para Norte e 1 km para cima em 6 min = 0,1 h: velocidade de 200 km/h L, 200 km/h N e 10 km/h para cima. Velocidade em relação ao solo = velocidade em relação ao ar + vento, então v<sub>ar</sub> = v<sub>solo</sub> − vento:</p><ul><li>Leste: 200 − 30 = <strong>170 km/h</strong>;</li><li>Norte: 200 − (−20) = <strong>220 km/h</strong>;</li><li>vertical: 10 − (−1) = <strong>11 km/h para cima</strong>.</li></ul><p>Alternativa <strong>D</strong>.</p><p>C ignora o vento; A e B somam o vento em vez de compensá-lo; E erra só a componente Norte.</p>",
  figs(("q126", "Eixos cardeais (Norte, Sul, Leste, Oeste) e vertical, com um avião na origem e o vetor velocidade v apontando para a “posição a ser atingida”, acima e a nordeste (fora de escala).")),
  ["composição de movimentos", "velocidade relativa"])
X(127, "Química", "Cinética química", "<p>A enzima é um catalisador: <strong>abaixa a energia de ativação</strong> (o pico) sem mudar a energia dos reagentes e dos produtos. No gráfico certo, as duas curvas começam em A e terminam em B no mesmo nível, e a pontilhada tem pico mais baixo. Alternativa <strong>C</strong>.</p><p>A, B e E mudam a energia dos reagentes ou dos produtos; D mostra a enzima aumentando a energia de ativação.</p>",
  figs(("q127a", "Alternativa A: a curva pontilhada começa mais alta que a contínua (reagentes A em níveis diferentes), as duas têm o mesmo pico e terminam em B no mesmo nível."),
       ("q127b", "Alternativa B: as duas começam em A no mesmo nível e têm o mesmo pico, mas a pontilhada termina mais alta que a contínua."),
       ("q127c", "Alternativa C: as duas começam em A e terminam em B nos mesmos níveis; a pontilhada tem o pico mais baixo."),
       ("q127d", "Alternativa D: mesmos níveis de A e B; a pontilhada tem o pico mais alto."),
       ("q127e", "Alternativa E: a pontilhada começa e termina mais alta que a contínua, com o mesmo pico.")),
  ["catalisadores", "energia de ativação"], alts={k: f"[[fig:{i}]]" for i, k in enumerate("ABCDE", 1)}, q_=False,
  enun=enunciado_enem(D[127]).split("[[fig:1]]")[0])
X(128, "Física", "Eletrodinâmica", "<p>Sensibilidade é quanto a resistência muda por grau: a inclinação da reta (B em R = A + BT). Pelo gráfico, as retas mais inclinadas são a do <strong>sensor 2</strong> (de cerca de 75 para 225 Ω) e a do <strong>sensor 5</strong> (de cerca de 65 para 145 Ω). Alternativa <strong>E</strong>.</p><p>O sensor 1 tem a maior resistência, mas quase não varia (A e B); o 3 e o 4 têm inclinações menores que a do 5 (C e D).</p>",
  figs(("q128", "Gráfico resistência (ohm) × temperatura (°C), de −50 a 320 °C, com cinco retas: sensor 1 quase horizontal em cerca de 225 Ω; sensor 2 subindo muito, de cerca de 75 a 225 Ω; sensor 3 pouco inclinado, de 145 a 168 Ω; sensor 4 de 90 a 148 Ω; sensor 5 de 65 a 145 Ω.")),
  ["termômetro de resistência", "função afim"])
X(129, "Biologia", "Doenças e saúde", "<p>O quadro mostra <strong>alta eficiência</strong> só contra moluscos aquáticos. O caramujo aquático (<em>Biomphalaria</em>) é o hospedeiro intermediário do <em>Schistosoma</em>: controlá-lo controla a <strong>esquistossomose</strong>. Alternativa <strong>A</strong>.</p><p>Contra larvas de <em>Aedes aegypti</em> (febre amarela e dengue, B e E) a eficiência é baixa; contra o bacilo de Koch (tuberculose, D), média; e a coqueluche (C) é causada por bactéria que não está no quadro.</p>",
  tags=["esquistossomose", "controle biológico"],
  enun=p(P(129)[0][1]) + '<table class="tabela"><thead><tr><th>Teste</th><th>Resultado</th></tr></thead><tbody><tr><td><em>Aedes aegypti</em> (larvas)</td><td>Baixa eficiência</td></tr><tr><td>Bacilo de Koch</td><td>Média eficiência</td></tr><tr><td>Moluscos aquáticos (adultos)</td><td>Alta eficiência</td></tr><tr><td>Pernilongo (larvas)</td><td>Média eficiência</td></tr><tr><td>Vermes platelmintos</td><td>Ineficiente</td></tr></tbody></table>' + p(P(129)[-1][1]))
X(130, "Física", "Eletrodinâmica", "<p>A fonte dá 1,2 U, e o equipamento precisa de U. O resistor de proteção deve ficar em <strong>série</strong> e “segurar” 0,2 U. Em série a corrente é a mesma, então a tensão se divide na razão das resistências: R<sub>P</sub> ÷ R<sub>C</sub> = 0,2 U ÷ U, ou seja, <strong>R<sub>P</sub> = 0,2 R<sub>C</sub></strong>. Alternativa <strong>E</strong>.</p><p>Em paralelo (A e B), o equipamento continuaria recebendo a tensão total da fonte. Em série com 1,2 R<sub>C</sub> ou 2,2 R<sub>C</sub> (C e D), ele receberia menos que a tensão certa.</p>",
  figs(("q130a", "Alternativa A: fonte ligada a R_C e R_P em paralelo, com R_P = 0,2 R_C."),
       ("q130b", "Alternativa B: R_C e R_P em paralelo, com R_P = 1,2 R_C."),
       ("q130c", "Alternativa C: R_P e R_C em série, com R_P = 1,2 R_C."),
       ("q130d", "Alternativa D: R_P e R_C em série, com R_P = 2,2 R_C."),
       ("q130e", "Alternativa E: R_P e R_C em série, com R_P = 0,2 R_C.")),
  ["associação de resistores", "divisor de tensão"], alts={k: f"[[fig:{i}]]" for i, k in enumerate("ABCDE", 1)},
  enun=ap(P(130)[0][1]) + p(P(130)[1][1].replace("resistência elétrica RC", "resistência elétrica R<sub>C</sub>").replace("resistor de proteção RP", "resistor de proteção R<sub>P</sub>") + P(130)[2][1], P(130)[3][1]))
X(131, "Química", "Estequiometria", "<p>9,3 kg de Nb = 9 300 ÷ 93 = 100 mol. Pela equação, 6 mol de Nb exigem 10 mol de Al: 100 · 10 ÷ 6 ≈ 166,7 mol de Al, ou 166,7 · 27 ≈ 4 500 g = 4,5 kg. Com 10% de excesso: 4,5 · 1,1 ≈ <strong>5,0 kg</strong>. Alternativa <strong>E</strong>.</p><p>4,5 kg (D) esquece o excesso; 2,7 kg (A) usa a proporção 1 : 1.</p>",
  tags=["excesso de reagente", "nióbio"], q_=True,
  trocas=[("<strong>3 Nb2O5 (s) + 10 Al (s) → 6 Nb (s) + 5 Al2O3 (s)</strong>", "3 Nb2O5 (s) + 10 Al (s) → 6 Nb (s) + 5 Al2O3 (s)"), ("g mol−1", "g mol<sup>−1</sup>")])
X(132, "Física", "Ondas", "<p>Pela análise do Treineiros, a conta esperada seria esta: uma pessoa gera intensidade I<sub>1</sub> com 100 dB; 10 000 pessoas geram 10<sup>4</sup> · I<sub>1</sub>, e o nível sobe 10 · log 10<sup>4</sup> = 40 dB, chegando a <strong>140 dB</strong>. Alternativa <strong>C</strong>, se a questão não tivesse sido anulada.</p>",
  tags=["nível sonoro", "logaritmo"], anulacao={"fonte": "oficial", "motivo": ANUL},
  enun=p(P(132)[0][1]) + '<p class="apoio">\\( n = 10 \\log_{10}\\left(\\dfrac{I}{I_0}\\right) \\)</p>' + p(P(132)[2][1], P(132)[3][1]))
X(133, "Química", "Interações intermoleculares", "<p>O filtro deixa passar a água e segura o óleo. A camada que fica em contato com a mistura é a de cima, o <strong>surfactante</strong> com cadeias fluoradas, que repele o óleo (é oleofóbico) e deixa a água atravessar. O óleo fica retido ali. Alternativa <strong>A</strong>.</p><p>As camadas de baixo (polímero, sílica e malha, B a E) dão sustentação e afinidade com a água, mas o óleo não chega até elas.</p>",
  figs(("q133", "Esquema das camadas do filtro, de cima para baixo: surfactante (cadeias com átomos de flúor e cabeças negativas), camada superior de polímero (com cargas positivas), nanopartículas de sílica (SiO₂, com carga negativa), camada inferior de polímero e malha de aço.")),
  ["polaridade", "separação óleo-água"], q_=True, trocas=[("<p class=\"apoio\"><strong>Representação esquemática do dispositivo</strong></p>", "")])
X(134, "Química", "Interações intermoleculares", "<p>Os hormônios são pouco polares, e a solubilidade em água aumenta com os grupos que fazem ligações de hidrogênio (–OH). Pelas estruturas, o <strong>estriol</strong> tem três grupos –OH, mais que todos os outros. Alternativa <strong>B</strong>.</p><p>Estradiol e novestrol têm dois –OH (A e D), e estrona e noretindrona têm um –OH e um grupo C=O (C e E).</p>",
  figs(("q134", "Estruturas de cinco hormônios esteroides (quatro anéis): estradiol, com dois OH; estriol, com três OH; estrona, com um OH e uma carbonila (C=O); novestrol, com dois OH e uma tripla ligação C≡CH; noretindrona, com uma carbonila, um OH e C≡CH.")),
  ["ligações de hidrogênio", "solubilidade"])
X(135, "Física", "Ondas", "<p>O texto diz que, com o tempo, a frequência da luz emitida pelo sensor <strong>aumenta</strong> (do vermelho-laranja ao verde). Frequência maior é comprimento de onda menor: no fim do tratamento, o pico sai de cerca de 600 nm e vai para perto de 550 nm, que é o verde. O gráfico certo tem a curva final deslocada para a esquerda. Alternativa <strong>A</strong>.</p><p>Em B o pico vai para a direita (frequência menor); em C, D e E ele fica em 600 nm, só mudando de altura.</p>",
  figs(("q135", "À esquerda, o gráfico de fotoluminescência do sensor × comprimento de onda (de 525 a 725 nm), com pico em 600 nm. Abaixo, a Figura 1, um bebê sob luz azul com o sensor vermelho na fralda, e a Figura 2, uma escala de tempo de exposição (0 h a 12 h) em que a cor do sensor passa de vermelho a laranja, amarelo e verde, com a frequência aumentando."),
       ("q135a", "Alternativa A: a curva do fim do tratamento (tracejada) tem o pico deslocado para a esquerda, em cerca de 555 nm; a do início tem pico em 600 nm."),
       ("q135b", "Alternativa B: o pico do fim do tratamento vai para a direita, em cerca de 635 nm."),
       ("q135c", "Alternativa C: as duas curvas têm pico em 600 nm; a do fim é um pouco mais baixa."),
       ("q135d", "Alternativa D: as duas têm pico em 600 nm; a do fim é um pouco mais alta."),
       ("q135e", "Alternativa E: as duas curvas são praticamente iguais, com pico em 600 nm.")),
  ["espectro eletromagnético", "frequência e comprimento de onda"], alts=ALT_FIG,
  enun=ap(P(135)[0][1], P(135)[1][1]) + "[[fig:1]]" + fonte(P(135)[3][1]) + p(P(135)[4][1]))

# questão 29: as figuras das alternativas também apareciam no fim do enunciado
Q[29]["enunciado"] = Q[29]["enunciado"].replace("[[fig:2]][[fig:3]][[fig:4]][[fig:5]][[fig:6]]", "")
completar(Q, R)
