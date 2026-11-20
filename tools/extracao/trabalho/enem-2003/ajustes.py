# Enem 2003 (31/08/2003), Prova 1 — amarela: prova única de 63 questões (modelo antigo, sem divisão por áreas).
# Fonte do PDF: arquivo 'Provas_Gabaritos_ENEM_2003' do usuário. Gabarito: 'GABARITO ENEM 2003 – Prova Amarela' do repositório do Inep (riep.inep.gov.br), lido duas vezes.
# Data: notícia do Inep "Enem 2003: prova será no dia 31 de agosto".
# O extrator padrão não lê este layout; as alternativas vêm de alts.json (extrator próprio) e os enunciados são escritos aqui.
# Cada questão leva a grande área mais próxima. Versos protegidos (Drummond Q9, Chico Buarque Q34, Quintana Q13, poetas da Q63 exceto Pessoa
# — mantido como imagem junto com os outros para as alternativas ficarem uniformes) como imagem; Eugênio de Castro (Q10–11), de domínio público, em texto.
import sys, pathlib, re, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar

ID = "enem-2003"
META = {"id": ID, "banca": "Enem", "ano": 2003, "titulo": "Enem 2003: Prova objetiva", "fonte": "Inep", "dataExame": "2003-08-31",
        "duracaoMinutos": 300, "area": "Prova objetiva (63 questões)", "caderno": "amarelo", "dia": 1, "fonteGabarito": {"oficial": True, "nome": "gabarito oficial no repositório do Inep", "url": "https://riep.inep.gov.br/bitstreams/3d06d0ff-eb68-450c-ac55-d10ae0fe7dd7/download"}}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 64)}
D = {int(k): v for k, v in json.loads((pathlib.Path(__file__).resolve().parent / "alts.json").read_text(encoding="utf-8")).items()}
Q = {}
p = lambda *xs: "".join(f"<p>{x}</p>" for x in xs)
ap = lambda *xs: "".join(f'<p class="apoio">{x}</p>' for x in xs)
tit = lambda x: f'<p class="apoio"><strong>{x}</strong></p>'
fonte = lambda x: f'<p class="fonte">{x}</p>'
ALT = lambda ini: {k: f"[[fig:{i}]]" for i, k in enumerate("ABCDE", ini)}
A5 = lambda *xs: dict(zip("ABCDE", xs))
I3 = lambda *xs: '<ol type="I">' + "".join(f"<li>{x}</li>" for x in xs) + "</ol>"
AREAS = {"L": "Linguagens", "H": "Ciências Humanas", "N": "Ciências da Natureza", "M": "Matemática"}


def figs(*pares):
    return [{"arquivo": a, "alt": t} for a, t in pares]


def tabela(cab, linhas):
    return ('<table class="tabela"><thead><tr>' + "".join(f"<th>{c}</th>" for c in cab) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in l) + "</tr>" for l in linhas) + "</tbody></table>")


def QF(s):
    partes = re.split(r"(<[^>]+>)", s)
    return "".join(x if x.startswith("<") else re.sub(r"\b(CO|O|N|H|SO|NO)(\d)\b", r"\1<sub>\2</sub>", x) for x in partes)


def X(n, area, materia, assunto, expl, enun, imagens=(), tags=(), alts=None, quim=False):
    e = re.sub(r"<((?:www\.|http)[^<>]*)>", r"&lt;\1&gt;", enun)
    if quim: e = QF(e)
    al = dict(alts or D[n])
    assert sorted(al) == list("ABCDE"), (n, al)
    Q[n] = {"materia": materia, "assunto": assunto, "area": AREAS[area], "tags": list(tags), "numeroOriginal": n,
            "enunciado": e, "alternativas": {k: (QF(v) if quim else v) for k, v in al.items()},
            "imagens": list(imagens), "explicacao": expl}



# ----------------------------------------------------------------
X(1, "L", "Língua Portuguesa", "Ambiguidade", "<p>Na manchete, “do governo do Estado” pode ligar-se a “violência” (a violência praticada pelo governo) ou a “campanha” (a campanha feita pelo governo). Pondo o adjunto junto de “campanha”, como em “Campanha do governo do Estado contra a violência”, a ambiguidade desaparece. Alternativa <strong>E</strong>.</p><p>As demais mudam o sentido da notícia: campanha contra o governo (A, C) ou violência do governo (B, D).</p>",
  p("No ano passado, o governo promoveu uma campanha a fim de reduzir os índices de violência. Noticiando o fato, um jornal publicou a seguinte manchete:")
  + ap("<strong>CAMPANHA CONTRA A VIOLÊNCIA DO GOVERNO DO ESTADO ENTRA EM NOVA FASE</strong>")
  + p("A manchete tem um duplo sentido, e isso dificulta o entendimento. Considerando o objetivo da notícia, esse problema poderia ter sido evitado com a seguinte redação:"),
  tags=["ambiguidade", "manchete"])

X(2, "L", "Língua Portuguesa", "Interpretação de texto", "<p>O texto define a propaganda como divulgação intencional para criar uma imagem positiva ou negativa, ligada à manipulação de massas por pequenos grupos, com princípios de simplificação, deformação e parcialidade. Ela serve aos interesses de quem a promove, isto é, de quem vende. Alternativa <strong>D</strong>.</p><p>O texto diz o contrário de A (pequenos grupos manipulam a maioria) e de E (a propaganda não convida à reflexão, ela simplifica e deforma).</p>",
  ap("A Propaganda pode ser definida como divulgação intencional e constante de mensagens destinadas a um determinado auditório visando criar uma imagem positiva ou negativa de determinados fenômenos. A Propaganda está muitas vezes ligada à idéia de manipulação de grandes massas por parte de pequenos grupos. Alguns princípios da Propaganda são: o princípio da simplificação, da saturação, da deformação e da parcialidade.")
  + fonte("Adaptado de Norberto Bobbio, et al. <em>Dicionário de Política</em>.") + p("Segundo o texto, muitas vezes a propaganda"),
  tags=["propaganda"])

X(3, "M", "Matemática", "Razão e proporção", "<p>Por dia, 40% de 30.000 = 12.000 motoristas observam o painel; em 7 dias, são 84.000 observações. Como cada motorista passa 3 vezes por semana, o número de motoristas diferentes é 84.000/3 = 28.000. Alternativa <strong>B</strong>.</p><p>84.000 (E) conta cada passagem como um motorista diferente.</p>",
  p("A eficiência de anúncios num painel eletrônico localizado em uma certa avenida movimentada foi avaliada por uma empresa. Os resultados mostraram que, em média:")
  + "<ul><li>passam, por dia, 30000 motoristas em frente ao painel eletrônico;</li><li>40% dos motoristas que passam observam o painel;</li><li>um mesmo motorista passa três vezes por semana pelo local.</li></ul>"
  + p("Segundo os dados acima, se um anúncio de um produto ficar exposto durante sete dias nesse painel, é esperado que o número mínimo de motoristas diferentes que terão observado o painel seja:"),
  tags=["porcentagem"])

ONIBUS = "[[fig:1]]"
F_ONIBUS = figs(("q04", "Gráfico de linha do tempo de percurso (minutos) em função do horário de saída, das 6h00 às 11h00, de 10 em 10 minutos: 6h00 e 6h10, 50; sobe até 100 às 8h00; 110 às 8h10 e 8h20 (máximo); 105 às 8h30; 100 às 8h40 e 8h50; 95 às 9h00; 90 das 9h10 às 9h40; 85 às 9h50; 80 às 10h00 e 10h10; 75 das 10h20 às 10h50; 70 às 11h00."))
X(4, "M", "Matemática", "Leitura de gráficos", "<p>É preciso que horário de saída + duração ≤ 10h30. Saindo às 8h50, a viagem leva 100 minutos e chega exatamente às 10h30. Saindo às 9h00, leva 95 minutos e chega às 10h35; às 9h10, leva 90 e chega às 10h40, tarde demais. O último horário possível é 8h50. Alternativa <strong>E</strong>.</p><p>Saídas às 9h20 ou 9h30 (A, B), com 90 minutos de viagem, chegariam às 10h50 e às 11h00.</p>",
  p("O tempo que um ônibus gasta para ir do ponto inicial ao ponto final de uma linha varia, durante o dia, conforme as condições do trânsito, demorando mais nos horários de maior movimento. A empresa que opera essa linha forneceu, no gráfico abaixo, o tempo médio de duração da viagem conforme o horário de saída do ponto inicial, no período da manhã.") + ONIBUS
  + p("De acordo com as informações do gráfico, um passageiro que necessita chegar até as 10h30min ao ponto final dessa linha, deve tomar o ônibus no ponto inicial, no máximo, até as:"),
  F_ONIBUS, ["leitura de gráfico", "tempo"])
X(5, "M", "Matemática", "Leitura de gráficos", "<p>O menor tempo do gráfico é 50 minutos (6h00 e 6h10) e o maior, 110 minutos (8h10 e 8h20): diferença de 60 minutos por dia, só na ida. Em 20 dias, 20 × 60 = 1.200 minutos = 20 horas. Alternativa <strong>C</strong>.</p><p>Contar a diferença também na volta daria 40 horas (D), mas o enunciado diz que na volta os dois gastam o mesmo tempo.</p>",
  p("João e Antônio utilizam os ônibus da linha mencionada na questão anterior para ir trabalhar, no período considerado no gráfico, nas seguintes condições:")
  + "<ul><li>trabalham vinte dias por mês;</li><li>João viaja sempre no horário em que o ônibus faz o trajeto no menor tempo;</li><li>Antônio viaja sempre no horário em que o ônibus faz o trajeto no maior tempo;</li><li>na volta do trabalho, ambos fazem o trajeto no mesmo tempo de percurso.</li></ul>"
  + ONIBUS + p("Considerando-se a diferença de tempo de percurso, Antônio gasta, por mês, em média,"),
  F_ONIBUS, ["leitura de gráfico"])

X(6, "M", "Matemática", "Volume", "<p>A caixa de 40 × 40 × 60 cm tem o dobro de cada dimensão do pacote de 20 × 20 × 30 cm, então cabem 2 × 2 × 2 = 8 pacotes por caixa. Para 100 pacotes: 100/8 = 12,5, ou seja, 13 caixas. Alternativa <strong>C</strong>.</p><p>12 caixas levariam só 96 pacotes.</p>",
  p("Uma editora pretende despachar um lote de livros, agrupados em 100 pacotes de 20 cm x 20 cm x 30 cm. A transportadora acondicionará esses pacotes em caixas com formato de bloco retangular de 40 cm x 40 cm x 60 cm. A quantidade mínima necessária de caixas para esse envio é:"),
  tags=["volume", "divisão"])

X(7, "M", "Matemática", "Geometria plana", "<p>No processo, uma folha dobrada duas vezes dá 4 folhas (8 páginas) de 10,5 × 15,5 cm: ela mede 21 × 31 cm. Para 32 páginas (16 folhas), é preciso dobrar duas vezes mais, quadruplicando a área: dobra-se cada dimensão, 42 × 62 cm. Alternativa <strong>D</strong>.</p><p>84 × 124 cm (B) dá 128 páginas, e 21 × 31 cm (E), só 8.</p>",
  p("Na literatura de cordel, os textos são impressos, em geral, com 8, 16, 24 ou 32 páginas de formato 10,5 cm x 15,5 cm. As razões históricas que explicam tal fato estão relacionadas à forma artesanal como são montadas as publicações e ao melhor aproveitamento possível do papel disponível.",
    "Considere, abaixo, a confecção de um texto de cordel com 8 páginas (4 folhas):") + "[[fig:1]]"
  + p("Utilizando o processo descrito acima, pode-se produzir um exemplar de cordel com 32 páginas de 10,5 cm x 15,5 cm, com o menor gasto possível de material, utilizando uma única folha de"),
  figs(("q07", "Sequência de desenhos: uma folha retangular é dobrada ao meio, depois dobrada ao meio de novo, recortada e montada como um livreto de 10,5 cm por 15,5 cm.")),
  ["cordel", "dobraduras"])

X(8, "L", "Literatura", "Interpretação de texto", "<p>Scliar compara a gaveta à adega: o texto amadurece guardado. Mas acrescenta que, “em certos casos, a cesta de papel é melhor ainda”, ou seja, há textos que nenhum tempo de maturação salva e devem ser jogados fora. Alternativa <strong>B</strong>.</p><p>As frases A, C e E defendem a maturação, e D fala do desejo de publicar.</p>",
  ap("Do pedacinho de papel ao livro impresso vai uma longa distância. Mas o que o escritor quer, mesmo, é isso: ver o seu texto em letra de forma. A gaveta é ótima para aplacar a fúria criativa; ela faz amadurecer o texto da mesma forma que a adega faz amadurecer o vinho. Em certos casos, a cesta de papel é melhor ainda. O período de maturação na gaveta é necessário, mas não deve se prolongar muito. ‘Textos guardados acabam cheirando mal’, disse Silvia Plath, (...) que, com esta frase, deu testemunho das dúvidas que atormentam o escritor: publicar ou não publicar? guardar ou jogar fora?")
  + fonte("Moacyr Scliar. <em>O escritor e seus desafios</em>.")
  + p("Nesse texto, o escritor Moacyr Scliar usa imagens para refletir sobre uma etapa da criação literária. A idéia de que o processo de maturação do texto nem sempre é o que garante bons resultados está sugerida na seguinte frase:"),
  tags=["Moacyr Scliar"])

X(9, "L", "Literatura", "Linguagem poética", "<p>Que um cão cheire algo é comum; o inesperado é o que ele cheira: o futuro, uma ideia abstrata, tratada como coisa concreta, com cheiro. O modo raro de tratar o “futuro” é o que renova a linguagem. Alternativa <strong>A</strong>.</p><p>A aproximação entre cão e “cheirar” (D) é usual, e o gerúndio e os artigos (C, E) não têm nada de incomum.</p>",
  ap("Eu começaria dizendo que poesia é uma questão de linguagem. A importância do poeta é que ele torna mais viva a linguagem. Carlos Drummond de Andrade escreveu um dos mais belos versos da língua portuguesa com duas palavras comuns: cão e cheirando.")
  + "[[fig:1]]" + fonte("Entrevista com Mário Carvalho. <em>Folha de SP</em>, 24/05/1988. Adaptação.")
  + p("O que deu ao verso de Drummond o caráter de inovador da língua foi"),
  figs(("q09", "Verso de Carlos Drummond de Andrade, em que um cão aparece cheirando o futuro.")),
  ["Drummond", "linguagem figurada"],
  alts=dict(D[9], E="o emprego do artigo indefinido “um” e do artigo definido “o” na mesma frase."))

EPIGRAFE = (tit("Texto para as questões 10 e 11.") + tit("Epígrafe*")
  + ap("Murmúrio de água na clepsidra** gotejante,<br>Lentas gotas de som no relógio da torre,<br>Fio de areia na ampulheta vigilante,<br>Leve sombra azulando a pedra do quadrante***<br>Assim se escoa a hora, assim se vive e morre...",
       "Homem, que fazes tu? Para que tanta lida,<br>Tão doidas ambições, tanto ódio e tanta ameaça?<br>Procuremos somente a Beleza, que a vida<br>É um punhado infantil de areia ressequida,<br>Um som de água ou de bronze e uma sombra que passa...")
  + fonte("Eugênio de Castro. <em>Antologia pessoal da poesia portuguesa</em>.")
  + fonte("(*) Epígrafe: inscrição colocada no ponto mais alto; tema. (**) Clepsidra: relógio de água. (***) Pedra do quadrante: parte superior de um relógio de sol."))
X(10, "L", "Literatura", "Interpretação de poema", "<p>As “lentas gotas de som no relógio da torre” são as badaladas do sino, de bronze, que marcam a passagem do tempo. Na segunda estrofe, “um som de água ou de bronze” retoma essa imagem (e também a da clepsidra). Alternativa <strong>B</strong>.</p><p>“Punhado de areia” (C) retoma a ampulheta, e “sombra que passa” (D), o relógio de sol.</p>",
  EPIGRAFE + p("A imagem contida em “lentas gotas de som” (verso 2) é retomada na segunda estrofe por meio da expressão:"), tags=["Eugênio de Castro", "imagem poética"])
X(11, "L", "Literatura", "Interpretação de poema", "<p>A primeira estrofe enumera relógios (de água, de sino, de areia, de sol) para mostrar como “se escoa a hora, assim se vive e morre”. É essa brevidade da vida que faz o poeta perguntar para que tanta lida, ambição e ódio. Alternativa <strong>E</strong>.</p><p>“Infantil” aparece só como imagem da fragilidade da vida (A), e não há menção à natureza ou à violência como causas (B, C).</p>",
  EPIGRAFE + p("Neste poema, o que leva o poeta a questionar determinadas ações humanas (versos 6 e 7) é a"), tags=["Eugênio de Castro", "passagem do tempo"])

X(12, "L", "Literatura", "Regionalismo", "<p>“Cor local” é a adaptação das histórias ao lugar de quem as conta. Transformar o Barba-Azul, personagem de conto europeu, num senhor de engenho de Pernambuco é exatamente isso. Alternativa <strong>A</strong>.</p><p>Rei, rainha e forca (B) são elementos tradicionais dos contos, e C, D e E falam do talento de Totonha como contadora.</p>",
  ap("A velha Totonha de quando em vez batia no engenho. E era um acontecimento para a meninada. (...) andava léguas e léguas a pé, de engenho a engenho, como uma edição viva das histórias de Mil e Uma Noites (...) era uma grande artista para dramatizar. Tinha uma memória de prodígio. Recitava contos inteiros em versos, intercalando pedaços de prosa, como notas explicativas. (...) Havia sempre rei e rainha, nos seus contos, e forca e adivinhações. O que fazia a velha Totonha mais curiosa era a cor local que ela punha nos seus descritivos. (...) Os rios e as florestas por onde andavam os seus personagens se pareciam muito com o Paraíba e a Mata do Rolo. O seu Barba-Azul era um senhor de engenho de Pernambuco.")
  + fonte("José Lins do Rego. <em>Menino de engenho</em>.")
  + p("A cor local que a personagem velha Totonha colocava em suas histórias é ilustrada, pelo autor, na seguinte passagem:"),
  tags=["José Lins do Rego", "cor local"])

X(13, "L", "Literatura", "Interpretação de texto", "<p>A aula é longa e monótona, mas o tédio faz a imaginação trabalhar: as nuvens viram uma história sem fim, e Margarida sonha com um avião que entrasse por uma janela e saísse pela outra. O tédio estimula a fantasia e a expectativa de um imprevisto mágico. Alternativa <strong>C</strong>.</p><p>Ele não impede a distração (D): é justamente o que provoca a fuga pela imaginação.</p>",
  "[[fig:1]]" + p("Na cena retratada no texto, o sentimento do tédio"),
  figs(("q13", "Texto “Pequenos tormentos da vida”, de Mário Quintana: numa sala de aula, o céu azul das janelas altas convida os meninos e as nuvens passam devagar, como uma história sem fim; a aula também parece não ter fim, só bocejos e moscas, até que Margarida pensa como seria bom se um avião entrasse por uma janela e saísse pela outra.")),
  ["Mário Quintana", "tédio"])

X(14, "M", "Matemática", "Raciocínio lógico", "<p>Dia 1: jogos 1 a 5. Dia 2: jogos 6, 7 e 8, mais 9 (vencedores de 1 e 2) e 10 (de 3 e 4), já que esses jogadores jogaram no dia 1. Dia 3: jogos 11 (vencedores de 5 e 6), 12 (de 7 e 8) e 13 (de 9 e 10). Dia 4: jogo 14 (de 11 e 12). Dia 5: final, jogo 15. São 5 dias. Alternativa <strong>D</strong>.</p><p>4 dias (E) exigiria que algum vencedor jogasse duas vezes no mesmo dia.</p>",
  p("Os alunos de uma escola organizaram um torneio individual de pingue-pongue nos horários dos recreios, disputado por 16 participantes, segundo o esquema abaixo:") + "[[fig:1]]"
  + p("Foram estabelecidas as seguintes regras:")
  + "<ul><li>Em todos os jogos, o perdedor será eliminado;</li><li>Ninguém poderá jogar duas vezes no mesmo dia;</li><li>Como há cinco mesas, serão realizados, no máximo, 5 jogos por dia.</li></ul>"
  + p("Com base nesses dados, é correto afirmar que o número mínimo de dias necessário para se chegar ao campeão do torneio é:"),
  figs(("q14", "Chave do torneio: jogos 1 a 8 com os 16 participantes; os vencedores dos jogos 1 e 2 vão ao jogo 9, de 3 e 4 ao 10, de 5 e 6 ao 11, de 7 e 8 ao 12; os vencedores de 9 e 10 vão ao jogo 13, de 11 e 12 ao 14; e os de 13 e 14 disputam o jogo 15, a final.")),
  ["torneio", "planejamento"])

X(15, "M", "Matemática", "Porcentagem", "<p>Dos 1.500 casos de câncer de pulmão, 90% estão ligados ao fumo: 1.350. Dos 500 casos de enfisema, 80%: 400. Estima-se 1.350 + 400 = 1.750 fumantes. Alternativa <strong>E</strong>.</p><p>Inverter as porcentagens (80% de 1.500 e 90% de 500) daria 1.650, que não está entre as opções.</p>",
  p("O tabagismo (vício do fumo) é responsável por uma grande quantidade de doenças e mortes prematuras na atualidade. O Instituto Nacional do Câncer divulgou que 90% dos casos diagnosticados de câncer de pulmão e 80% dos casos diagnosticados de enfisema pulmonar estão associados ao consumo de tabaco. Paralelamente, foram mostrados os resultados de uma pesquisa realizada em um grupo de 2000 pessoas com doenças de pulmão, das quais 1500 são casos diagnosticados de câncer, e 500 são casos diagnosticados de enfisema. Com base nessas informações, pode-se estimar que o número de fumantes desse grupo de 2000 pessoas é, aproximadamente:"),
  tags=["tabagismo"])

X(16, "N", "Biologia", "Saúde", "<p>Cada lata dá cerca de 0,3 g/L; três latas, 0,9 g/L. Esse valor está nas faixas 0,3–1,2 (queda da atenção) e 0,9–2,5 (queda da sensibilidade e das reações motoras). Alternativa <strong>A</strong>.</p><p>Aparente normalidade (B) só vai até 0,5 g/L, e confusão mental (C) começa em 1,8 g/L.</p>",
  p("Os acidentes de trânsito, no Brasil, em sua maior parte são causados por erro do motorista. Em boa parte deles, o motivo é o fato de dirigir após o consumo de bebida alcoólica. A ingestão de uma lata de cerveja provoca uma concentração de aproximadamente 0,3 g/L de álcool no sangue. A tabela abaixo mostra os efeitos sobre o corpo humano provocados por bebidas alcoólicas em função de níveis de concentração de álcool no sangue:")
  + tabela(["Concentração de álcool no sangue (g/L)", "Efeitos"],
           [["0,1 - 0,5", "Sem influência aparente, ainda que com alterações clínicas"], ["0,3 - 1,2", "Euforia suave, sociabilidade acentuada e queda da atenção"],
            ["0,9 - 2,5", "Excitação, perda de julgamento crítico, queda da sensibilidade e das reações motoras"], ["1,8 - 3,0", "Confusão mental e perda da coordenação motora"],
            ["2,7 - 4,0", "Estupor, apatia, vômitos e desequilíbrio ao andar"], ["3,5 - 5,0", "Coma e morte possível"]])
  + fonte("Revista <em>Pesquisa FAPESP</em> nº 57, setembro 2000.")
  + p("Uma pessoa que tenha tomado três latas de cerveja provavelmente apresenta"),
  tags=["álcool", "leitura de tabela"])

X(17, "N", "Biologia", "Saúde", "<p>No gráfico, a curva “após o jantar” chega a cerca de 0,7 g/L e cai abaixo de 0,6 g/L por volta de 3 horas. A curva “em jejum” sobe a 1,0 g/L e só fica abaixo de 0,6 g/L por volta de 4,5 horas. Alternativa <strong>C</strong>.</p><p>B inverte as situações e usa o momento em que a curva sobe, e não quando ela desce abaixo do limite.</p>",
  p("Após a ingestão de bebidas alcoólicas, o metabolismo do álcool e sua presença no sangue dependem de fatores como peso corporal, condições e tempo após a ingestão.") + "[[fig:1]]" + fonte("Revista <em>Pesquisa FAPESP</em> nº 57, setembro 2000.")
  + p("O gráfico mostra a variação da concentração de álcool no sangue de indivíduos de mesmo peso que beberam três latas de cerveja cada um, em diferentes condições: em jejum e após o jantar.",
      "Tendo em vista que a concentração máxima de álcool no sangue permitida pela legislação brasileira para motoristas é 0,6 g/L, o indivíduo que bebeu após o jantar e o que bebeu em jejum só poderão dirigir após, aproximadamente,"),
  figs(("q17", "Gráfico “Ingestão de álcool”: álcool no sangue (g/L, de 0 a 1,0) em função do tempo após a ingestão (0 a 7 horas). A curva “em jejum”, tracejada, sobe rápido a 1,0 g/L em cerca de 1 hora e cai devagar, passando por 0,6 g/L por volta de 4,5 horas. A curva “após o jantar”, contínua, sobe a cerca de 0,7 g/L em 1,5 hora e cai, passando por 0,6 g/L por volta de 3 horas e chegando a 0,2 g/L em 6 horas.")),
  ["álcool", "leitura de gráfico"], alts=dict(D[17], D="seis horas e três horas, respectivamente."))

X(18, "N", "Biologia", "Microbiologia", "<p>Inibir a síntese proteica é bloquear a produção de proteínas, essenciais para o funcionamento e a multiplicação das bactérias. Alternativa <strong>E</strong>.</p><p>Bactérias causadoras de doenças não fazem fotossíntese (A); o remédio não age sobre o DNA (B) nem sobre a membrana (C); e antibióticos não atuam sobre vírus (D).</p>",
  p("Na embalagem de um antibiótico, encontra-se uma bula que, entre outras informações, explica a ação do remédio do seguinte modo:")
  + ap("O medicamento atua por inibição da síntese protéica bacteriana.") + p("Essa afirmação permite concluir que o antibiótico"),
  tags=["antibióticos", "síntese proteica"])

X(19, "N", "Biologia", "Imunologia", "<p>O soro traz anticorpos prontos e age de imediato, por isso é usado quando o mal já está instalado, como na picada de cobra peçonhenta. Alternativa <strong>B</strong>.</p><p>As outras situações (gripe, poliomielite, sarampo, febre amarela) são de prevenção, feitas com vacina, que prepara a defesa com antecedência.</p>",
  p("Quando o corpo humano é invadido por elementos estranhos, o sistema imunológico reage. No entanto, muitas vezes o ataque é tão rápido que pode levar a pessoa à morte. A vacinação permite ao organismo preparar sua defesa com antecedência. Mas, se existe suspeita de mal já instalado, é recomendável o uso do soro, que combate de imediato os elementos estranhos, enquanto o sistema imunológico se mobiliza para entrar em ação.",
    "Considerando essas informações, o soro específico deve ser usado quando"),
  tags=["soro", "vacina"])

BOTUL = p("O botulismo, intoxicação alimentar que pode levar à morte, é causado por toxinas produzidas por certas bactérias, cuja reprodução ocorre nas seguintes condições: é inibida por pH inferior a 4,5 (meio ácido), temperaturas próximas a 100 °C, concentrações de sal superiores a 10% e presença de nitritos e nitratos como aditivos.")
X(20, "N", "Biologia", "Microbiologia", "<p>I tem relação: sal a 12% (acima de 10%) e ácido cítrico (que baixa o pH) inibem as bactérias. II também, pois as normas da Anvisa foram criadas contra o botulismo. III (“ecologicamente correto”) não tem relação. Alternativa <strong>C</strong>.</p>",
  BOTUL + p("A ocorrência de casos recentes de botulismo em consumidores de palmito em conserva levou a Agência Nacional de Vigilância Sanitária (ANVISA) a implementar normas para a fabricação e comercialização do produto. No rótulo de uma determinada marca de palmito em conserva, encontram-se as seguintes informações:")
  + I3("Ingredientes: Palmito açaí, sal diluído a 12% em água, ácido cítrico;", "Produto fabricado conforme as normas da ANVISA;", "Ecologicamente correto.")
  + p("As informações do rótulo que têm relação com as medidas contra o botulismo estão contidas em:"),
  tags=["botulismo", "conservas"])
X(21, "N", "Biologia", "Microbiologia", "<p>Uma conserva com 2 g de sal em 100 g de água tem cerca de 2% de sal, bem abaixo dos 10% que inibem as bactérias. Alternativa <strong>A</strong>.</p><p>Nitritos e nitratos (B), fervura (C), pH ácido do limão (D) e salga forte do charque (E) são justamente condições que inibem a reprodução.</p>",
  BOTUL + p("Levando-se em conta os fatores que favorecem a reprodução das bactérias responsáveis pelo botulismo, mencionadas no item anterior, conclui-se que as toxinas que o causam têm maior chance de ser encontradas"),
  tags=["botulismo"])

X(22, "N", "Biologia", "Parasitoses", "<p>A malária é transmitida pelo mosquito <em>Anopheles</em>, que se reproduz em águas paradas e limpas. O calor e as chuvas abundantes da floresta equatorial favorecem sua proliferação. Alternativa <strong>D</strong>.</p><p>O mosquito da malária não se cria em esgotos (B), e não há explicação genética para os casos (A).</p>",
  p("A malária é uma doença típica de regiões tropicais. De acordo com dados do Ministério da Saúde, no final do século XX, foram registrados mais de 600 mil casos de malária no Brasil, 99% dos quais na região amazônica. Os altos índices de malária nessa região podem ser explicados por várias razões, entre as quais:"),
  tags=["malária", "clima equatorial"])
X(23, "H", "Geografia", "Amazônia", "<p>Nas décadas de 1970 a 1990, a ocupação da Amazônia levou muitos migrantes para fazendas, obras, assentamentos e garimpos em áreas de floresta, onde passaram a ter contato com o mosquito transmissor. Alternativa <strong>C</strong>.</p><p>A camada de ozônio não tem relação com a malária (A), e o agente não migrou para as cidades (E).</p>",
  p("Houve uma grande elevação do número de casos de malária na Amazônia que, de 30 mil casos na década de 1970, chegou a cerca de 600 mil na década de 1990. Esse aumento pode ser relacionado a mudanças na região, como"),
  tags=["malária", "migração"])

LIMPEZA = (p("Produtos de limpeza, indevidamente guardados ou manipulados, estão entre as principais causas de acidentes domésticos. Leia o relato de uma pessoa que perdeu o olfato por ter misturado água sanitária, amoníaco e sabão em pó para limpar um banheiro:")
  + ap("<u>A mistura ferveu e começou a sair uma fumaça asfixiante.</u> Não conseguia respirar e meus olhos, nariz e garganta começaram a arder de maneira insuportável. Saí correndo à procura de uma janela aberta para poder voltar a respirar."))
X(24, "N", "Química", "Transformações químicas", "<p>A mistura “ferveu” (liberou gás) e soltou “fumaça asfixiante”: houve reação química entre os produtos, formando rapidamente gases tóxicos (como a cloramina, da água sanitária com amoníaco). Alternativa <strong>D</strong>.</p><p>Não foi simples evaporação (A) nem formação de solução aquosa (B), e o oxigênio do ar não é o responsável (C).</p>",
  LIMPEZA + p("O trecho sublinhado poderia ser reescrito, em linguagem científica, da seguinte forma:"), tags=["reação química", "produtos de limpeza"])
X(25, "N", "Química", "Segurança química", "<p>O acidente aconteceu porque a pessoa misturou água sanitária, amoníaco e sabão sem saber o resultado. A regra descumprida é a de ler os rótulos e evitar misturas de resultado desconhecido. Alternativa <strong>B</strong>.</p><p>O relato não fala de embalagens trocadas, de alimentos, de primeiros socorros ou de crianças.</p>",
  LIMPEZA + p("Entre os procedimentos recomendados para reduzir acidentes com produtos de limpeza, aquele que deixou de ser cumprido, na situação discutida na questão anterior, foi:"), tags=["produtos de limpeza"])

X(26, "N", "Biologia", "Biodiversidade", "<p>I e III estão corretas: bancos de sementes e gametas guardam poucos indivíduos, sem a variabilidade genética das populações, e não reproduzem as interações nem a heterogeneidade dos habitats. Alternativa <strong>C</strong>.</p><p>II é falsa: técnicas de preservação de embriões já existiam e não são o centro da crítica ecológico-evolutiva.</p>",
  p("A biodiversidade é garantida por interações das várias formas de vida e pela estrutura heterogênea dos habitats. Diante da perda acelerada de biodiversidade, tem sido discutida a possibilidade de se preservarem espécies por meio da construção de “bancos genéticos” de sementes, óvulos e espermatozóides. Apesar de os “bancos” preservarem espécimes (indivíduos), sua construção é considerada questionável do ponto de vista ecológico-evolutivo, pois se argumenta que esse tipo de estratégia")
  + I3("não preservaria a variabilidade genética das populações;", "dependeria de técnicas de preservação de embriões, ainda desconhecidas;", "não reproduziria a heterogeneidade dos ecossistemas.")
  + p("Está correto o que se afirma em"),
  tags=["bancos genéticos", "variabilidade genética"])

X(27, "H", "Geografia", "Questão ambiental", "<p>O texto lista três sentidos de proteger a biodiversidade: afastar a ação humana (ecologia radical), proteger as populações que vivem do ecossistema e defender interesses comerciais. Há visões diferentes em jogo, ecológicas, sociais e econômicas. Alternativa <strong>E</strong>.</p><p>O texto não toma partido de nenhuma visão, como fazem B, C e D.</p>",
  ap("A biodiversidade diz respeito tanto a genes, espécies, ecossistemas, como a funções, e coloca problemas de gestão muito diferenciados. É carregada de normas de valor. Proteger a biodiversidade pode significar:<br>– a eliminação da ação humana, como é a proposta da ecologia radical;<br>– a proteção das populações cujos sistemas de produção e cultura repousam num dado ecossistema;<br>– a defesa dos interesses comerciais de firmas que utilizam a biodiversidade como matéria-prima, para produzir mercadorias.")
  + fonte("Adaptado de GARAY, I. &amp; DIAS, B. <em>Conservação da biodiversidade em ecossistemas tropicais</em>.")
  + p("De acordo com o texto, no tratamento da questão da biodiversidade no Planeta,"),
  tags=["biodiversidade"])

X(28, "N", "Biologia", "Biomas", "<p>Nas florestas tropicais há muita luz e umidade o ano todo, com pouca variação climática entre as estações. Essas condições estáveis permitem grande produtividade e a coexistência de muitas espécies. Alternativa <strong>D</strong>.</p><p>Secas prolongadas (E) e altitudes elevadas (A) não caracterizam as florestas tropicais úmidas.</p>",
  p("Sabe-se que uma área de quatro hectares de floresta, na região tropical, pode conter cerca de 375 espécies de plantas enquanto uma área florestal do mesmo tamanho, em região temperada, pode apresentar entre 10 e 15 espécies. O notável padrão de diversidade das florestas tropicais se deve a vários fatores, entre os quais é possível citar"),
  tags=["florestas tropicais"])

X(29, "N", "Biologia", "Ciclo da água", "<p>As atividades humanas poluem a água (alteram sua qualidade) e retiram, desviam ou desperdiçam água doce (alteram a quantidade disponível para o consumo). Alternativa <strong>B</strong>.</p><p>A quantidade total de água no planeta praticamente não muda (A, E); o que muda é a parcela disponível e de boa qualidade.</p>",
  p("A falta de água doce no Planeta será, possivelmente, um dos mais graves problemas deste século. Prevê-se que, nos próximos vinte anos, a quantidade de água doce disponível para cada habitante será drasticamente reduzida. Por meio de seus diferentes usos e consumos, as atividades humanas interferem no ciclo da água, alterando"),
  tags=["água doce"])
X(30, "H", "Geografia", "Recursos hídricos", "<p>O Brasil tem muitos rios, grandes bacias e aquíferos. Uma crise de água no país viria da degradação dos mananciais (poluição, desmatamento) e do desperdício no consumo. Alternativa <strong>E</strong>.</p><p>As demais contradizem a “riqueza dos recursos hídricos brasileiros” citada no enunciado.</p>",
  p("Considerando a riqueza dos recursos hídricos brasileiros, uma grave crise de água em nosso país poderia ser motivada por"), tags=["mananciais"])
X(31, "N", "Física", "Energia elétrica", "<p>A maior parte da eletricidade brasileira vem de hidrelétricas, que dependem do nível dos reservatórios. As chuvas de março, fim do período chuvoso, definem quanta água haverá nas barragens para o resto do ano. Alternativa <strong>A</strong>.</p><p>As termelétricas eram pequena parte da geração em 2001 (C), e o consumo de água dos chuveiros não afeta a geração (E).</p>",
  ap("“Águas de março definem se falta luz este ano”.")
  + p("Esse foi o título de uma reportagem em jornal de circulação nacional, pouco antes do início do racionamento do consumo de energia elétrica, em 2001. No Brasil, a relação entre a produção de eletricidade e a utilização de recursos hídricos, estabelecida nessa manchete, se justifica porque"),
  tags=["hidrelétricas", "apagão de 2001"])
X(32, "N", "Química", "Água", "<p>Reutilizar parte da água faz a indústria comprar menos água e devolver menos água contaminada. Isso economiza dinheiro e protege os recursos hídricos. Alternativa <strong>B</strong>.</p><p>Reúso não aumenta o consumo (C) nem faz toda a água voltar limpa ao manancial (A).</p>",
  p("Considerando os custos e a importância da preservação dos recursos hídricos, uma indústria decidiu purificar parte da água que consome para reutilizá-la no processo industrial. De uma perspectiva econômica e ambiental, a iniciativa é importante porque esse processo"),
  tags=["reúso de água"])

X(33, "M", "Matemática", "Razão e proporção", "<p>A eficiência é a fração da água suja que sai purificada: I, 15/45 = 1/3; II, 10/40 = 1/4; III, 5/40 = 1/8; IV, 10/20 = 1/2; V, 5/20 = 1/4. A maior é a do sistema IV. Alternativa <strong>D</strong>.</p><p>O sistema I tem a maior saída em litros, mas aproveita só um terço da água que entra.</p>",
  p("Visando adotar um sistema de reutilização de água, uma indústria testou cinco sistemas com diferentes fluxos de entrada de água suja e fluxos de saída de água purificada.")
  + tabela(["Sistema", "Fluxo de entrada (água suja)", "Fluxo de saída (água purificada)"], [["I", "45 L/h", "15 L/h"], ["II", "40 L/h", "10 L/h"], ["III", "40 L/h", "5 L/h"], ["IV", "20 L/h", "10 L/h"], ["V", "20 L/h", "5 L/h"]])
  + p("Supondo que o custo por litro de água purificada seja o mesmo, obtém-se maior eficiência na purificação por meio do sistema"),
  tags=["eficiência", "razão"], alts=A5("I.", "II.", "III.", "IV.", "V."))

X(34, "N", "Física", "Energia nuclear", "<p>Em funcionamento normal, a usina usa água do mar para refrigerar o reator e a devolve mais quente. Esse aquecimento altera a fauna marinha nas proximidades e pode prejudicar a pesca. Alternativa <strong>A</strong>.</p><p>Usinas não lançam rejeitos radioativos nem lixo atômico no mar em operação normal (C, E), e o enriquecimento do urânio não é feito na usina (D).</p>",
  p("Na música “Bye, bye, Brasil”, de Chico Buarque de Holanda e Roberto Menescal, os versos") + "[[fig:1]]"
  + p("poderiam estar se referindo à usina nuclear de Angra dos Reis, no litoral do Estado do Rio de Janeiro. No caso de tratar-se dessa usina, em funcionamento normal, dificuldades para a pesca nas proximidades poderiam ser causadas"),
  figs(("q34", "Dois versos da canção, que falam de uma usina posta no mar e de como isso talvez atrapalhe a pesca.")),
  ["Angra dos Reis", "poluição térmica"])

X(35, "M", "Matemática", "Volume", "<p>Somando as chuvas do gráfico no período chuvoso: 100 + 100 + 300 + 100 + 50 + 50 = 700 mm, ou 700 litros por m². O telhado tem 8 m × 10 m = 80 m², e acumula 80 × 700 = 56.000 litros = 56 m³. O reservatório de 2 m × 4 m × p deve ter 8p = 56, logo p = 7 m. Alternativa <strong>D</strong>.</p>",
  p("Prevenindo-se contra o período anual de seca, um agricultor pretende construir um reservatório fechado, que acumule toda a água proveniente da chuva que cair no telhado de sua casa, ao longo de um período anual chuvoso. As ilustrações a seguir apresentam as dimensões da casa, a quantidade média mensal de chuva na região, em milímetros, e a forma do reservatório a ser construído.") + "[[fig:1]]"
  + p("Sabendo que 100 milímetros de chuva equivalem ao acúmulo de 100 litros de água em uma superfície plana horizontal de um metro quadrado, a profundidade (p) do reservatório deverá medir"),
  figs(("q35", "À esquerda, desenho de uma casa de 8 m por 10 m e, ao lado, um reservatório em forma de bloco de 2 m por 4 m por p m. À direita, gráfico de barras da chuva mensal (mm): janeiro 100, fevereiro 100, março 300, abril 100, maio 50, de junho a novembro zero e dezembro 50.")),
  ["volume", "chuva"], alts=A5("4 m.", "5 m.", "6 m.", "7 m.", "8 m."))

X(36, "M", "Matemática", "Notação científica", "<p>Um campo a cada 8 segundos dá, em um ano, 32 × 10<sup>6</sup>/8 = 4 × 10<sup>6</sup> campos. Cada um tem 10<sup>−2</sup> km², então a área é 4 × 10<sup>4</sup> = 40.000 km², o dobro dos 20.000 km² medidos pelo Inpe. O fato é grave, mas a comparação exagerou. Alternativa <strong>E</strong>.</p><p>Desmatamento não é fenômeno natural (D).</p>",
  p("Dados divulgados pelo Instituto Nacional de Pesquisas Espaciais mostraram o processo de devastação sofrido pela Região Amazônica entre agosto de 1999 e agosto de 2000. Analisando fotos de satélites, os especialistas concluíram que, nesse período, sumiu do mapa um total de 20 000 quilômetros quadrados de floresta. Um órgão de imprensa noticiou o fato com o seguinte texto:")
  + ap("<em>O assustador ritmo de destruição é de um campo de futebol a cada oito segundos.</em>")
  + p("Considerando que um ano tem aproximadamente 32 x 10<sup>6</sup> s (trinta e dois milhões de segundos) e que a medida da área oficial de um campo de futebol é aproximadamente 10<sup>-2</sup> km<sup>2</sup> (um centésimo de quilômetro quadrado), as informações apresentadas nessa notícia permitem concluir que tal ritmo de desmatamento, em um ano, implica a destruição de uma área de"),
  tags=["desmatamento", "ordem de grandeza"],
  alts=A5("10 000 km<sup>2</sup>, e a comparação dá a idéia de que a devastação não é tão grave quanto o dado numérico nos indica.",
          "10 000 km<sup>2</sup>, e a comparação dá a idéia de que a devastação é mais grave do que o dado numérico nos indica.",
          "20 000 km<sup>2</sup>, e a comparação retrata exatamente o ritmo da destruição.",
          "40 000 km<sup>2</sup>, e o autor da notícia exagerou na comparação, dando a falsa impressão de gravidade a um fenômeno natural.",
          "40 000 km<sup>2</sup> e, ao chamar a atenção para um fato realmente grave, o autor da notícia exagerou na comparação."))

X(37, "N", "Física", "Eficiência energética", "<p>Pelo gráfico, o fogão a lenha tem eficiência de cerca de 29% e o fogão a gás, de cerca de 57%: quase o dobro. Alternativa <strong>C</strong>.</p><p>Do gás para o elétrico (cerca de 62%) o ganho é pequeno (D), e os combustíveis sólidos (lenha e carvão) são os menos eficientes (E).</p>",
  p("A eficiência do fogão de cozinha pode ser analisada em relação ao tipo de energia que ele utiliza. O gráfico abaixo mostra a eficiência de diferentes tipos de fogão.") + "[[fig:1]]"
  + p("Pode-se verificar que a eficiência dos fogões aumenta"),
  figs(("q37", "Gráfico de barras “Eficiência do fogão (%)”: fogões a lenha, cerca de 29; a carvão, cerca de 30; a querosene, cerca de 50; a gás, cerca de 57; elétricos, cerca de 62.")),
  ["eficiência", "fogões"])

X(38, "N", "Química", "Resíduos sólidos", "<p>A embalagem longa vida é reciclável: com coleta seletiva, o papel, o plástico e o alumínio podem ser reaproveitados, em vez de ficarem cem anos num aterro. Alternativa <strong>B</strong>.</p><p>Soda cáustica (A) criaria outro resíduo perigoso, e aterros específicos (D) apenas acumulam o problema.</p>",
  p("A caixinha utilizada em embalagens como as de leite “longa vida” é chamada de “tetra brick”, por ser composta de quatro camadas de diferentes materiais, incluindo alumínio e plástico, e ter a forma de um tijolo (<em>brick</em>, em inglês). Esse material, quando descartado, pode levar até cem anos para se decompor.",
    "Considerando os impactos ambientais, seria mais adequado"),
  tags=["coleta seletiva", "embalagens"])

X(39, "H", "Geografia", "Questão ambiental", "<p>II e III estão corretas: há desequilíbrio do ser humano com a natureza (lixo nas ruas) e entre os seres humanos (desemprego, catação para sobreviver); e essas atividades se refletem na economia, abastecendo a reciclagem de alumínio. Alternativa <strong>C</strong>.</p><p>I é falsa: a catação fornece sucata à indústria de alumínio, e não a prejudica.</p>",
  p("Um grupo de estudantes, saindo de uma escola, observou uma pessoa catando latinhas de alumínio jogadas na calçada. Um deles considerou curioso que a falta de civilidade de quem deixa lixo pelas ruas acaba sendo útil para a subsistência de um desempregado. Outro estudante comentou o significado econômico da sucata recolhida, pois ouvira dizer que a maior parte do alumínio das latas estaria sendo reciclada. Tentando sintetizar o que estava sendo observado, um terceiro estudante fez três anotações, que apresentou em aula no dia seguinte:")
  + I3("A catação de latinhas é prejudicial à indústria de alumínio;", "A situação observada nas ruas revela uma condição de duplo desequilíbrio: do ser humano com a natureza e dos seres humanos entre si;", "Atividades humanas resultantes de problemas sociais e ambientais podem gerar reflexos (refletir) na economia.")
  + p("Dessas afirmações, você tenderia a concordar, apenas, com"),
  tags=["reciclagem", "catadores"])

X(40, "N", "Física", "Energia", "<p>Se o trator roda mais tempo com um litro de óleo de girassol, nas mesmas condições, é porque esse litro libera mais energia que um litro de diesel. Alternativa <strong>E</strong>.</p><p>Rodar mais com o mesmo volume significa consumo menor por km (A) e combustível que dura mais (C).</p>",
  p("O setor de transporte, que concentra uma grande parcela da demanda de energia no país, continuamente busca alternativas de combustíveis. Investigando alternativas ao óleo diesel, alguns especialistas apontam para o uso do óleo de girassol, menos poluente e de fonte renovável, ainda em fase experimental. Foi constatado que um trator pode rodar, nas mesmas condições, mais tempo com um litro de óleo de girassol, que com um litro de óleo diesel. Essa constatação significaria, portanto, que usando óleo de girassol,"),
  tags=["biocombustíveis", "energia"])
X(41, "N", "Física", "Termodinâmica", "<p>A energia química do combustível vira energia térmica na combustão, e os gases quentes se expandem e empurram os pistões, produzindo trabalho mecânico. Alternativa <strong>A</strong>.</p><p>Os eixos só transmitem a energia mecânica já produzida (B), a ignição apenas inicia a queima (C), e a exaustão expele gases já usados (D).</p>",
  p("No Brasil, o sistema de transporte depende do uso de combustíveis fósseis e de biomassa, cuja energia é convertida em movimento de veículos. Para esses combustíveis, a transformação de energia química em energia mecânica acontece"),
  tags=["motor a combustão"])
X(42, "N", "Química", "Combustíveis", "<p>Um metro cúbico de GNV libera 0,8 × 50.200 ≈ 40 mil kJ; um de gasolina, 738 × 46.900 ≈ 34,6 milhões de kJ. Para a mesma energia, o volume de gás é cerca de 860 vezes maior, por isso ele precisa ser armazenado comprimido, a alta pressão. Alternativa <strong>B</strong>.</p><p>Um motor mais potente (A) não resolve o problema do volume.</p>",
  p("Nos últimos anos, o gás natural (GNV: gás natural veicular) vem sendo utilizado pela frota de veículos nacional, por ser viável economicamente e menos agressivo do ponto de vista ambiental. O quadro compara algumas características do gás natural e da gasolina em condições ambiente.")
  + tabela(["", "Densidade (kg/m<sup>3</sup>)", "Poder Calorífico (kJ/kg)"], [["GNV", "0,8", "50.200"], ["Gasolina", "738", "46.900"]])
  + p("Apesar das vantagens no uso de GNV, sua utilização implica algumas adaptações técnicas, pois, em condições ambiente, o volume de combustível necessário, em relação ao de gasolina, para produzir a mesma energia, seria"),
  tags=["GNV", "densidade"])

X(43, "N", "Química", "Ciclo do enxofre", "<p>I e III estão corretas: o H2S é um gás tóxico produzido naturalmente na decomposição, e esse processo faz parte do ciclo do enxofre. Alternativa <strong>D</strong>.</p><p>II é falsa: o esterco é um adubo valioso, e o fato de liberar H2S não justifica abandoná-lo.</p>",
  p("Os gases liberados pelo esterco e por alimentos em decomposição podem conter sulfeto de hidrogênio (H2S), gás com cheiro de ovo podre, que é tóxico para muitos seres vivos. Com base em tal fato, foram feitas as seguintes afirmações:")
  + I3("Gases tóxicos podem ser produzidos em processos naturais;", "Deve-se evitar o uso de esterco como adubo porque polui o ar das zonas rurais;", "Esterco e alimentos em decomposição podem fazer parte no ciclo natural do enxofre (S).")
  + p("Está correto, apenas, o que se afirma em"),
  tags=["sulfeto de hidrogênio"], quim=True, alts=A5("I.", "II.", "III.", "I e III.", "II e III."))

X(44, "H", "Geografia", "Transporte urbano", "<p>Trocar o transporte individual pelo coletivo reduz congestionamentos e melhora a mobilidade de quem depende dele (implicação social), e diminui a queima de combustível e a poluição por passageiro (implicação ambiental). Alternativa <strong>C</strong>.</p><p>Trocar diesel por gasolina (B) ou álcool por diesel (D) não resolve o trânsito e pode piorar a poluição.</p>",
  p("Em um debate sobre o futuro do setor de transporte de uma grande cidade brasileira com trânsito intenso, foi apresentado um conjunto de propostas. Entre as propostas reproduzidas abaixo, aquela que atende, ao mesmo tempo, a implicações sociais e ambientais presentes nesse setor é"),
  tags=["transporte coletivo"])
X(45, "N", "Química", "Combustíveis", "<p>A cana se renova a cada safra, em cerca de um ano, enquanto o petróleo levou milhões de anos (escala geológica) para se formar. Essa diferença de tempo de formação é o que define o álcool como renovável e o petróleo como não renovável. Alternativa <strong>A</strong>.</p><p>Os tempos de combustão ou de refino (D, E) não têm relação com a renovabilidade.</p>",
  p("Do ponto de vista ambiental, uma distinção importante que se faz entre os combustíveis é serem provenientes ou não de fontes renováveis. No caso dos derivados de petróleo e do álcool de cana, essa distinção se caracteriza"),
  tags=["fontes renováveis"])

X(46, "H", "História", "Tempo histórico", "<p>A vida surgiu há cerca de 3,5 bilhões de anos: precisa de uma escala de bilhões de anos. A escrita surgiu há cerca de 5 mil anos, na Mesopotâmia: escala de milhares de anos. Alternativa <strong>E</strong>.</p><p>Milhões de anos (D) seria escala grande demais para a escrita, e centenas de anos (A, B), pequena demais.</p>",
  p("Para o registro de processos naturais e sociais devem ser utilizadas diferentes escalas de tempo. Por exemplo, para a datação do sistema solar é necessária uma escala de bilhões de anos, enquanto que, para a história do Brasil, basta uma escala de centenas de anos. Assim, para os estudos relativos ao surgimento da vida no Planeta e para os estudos relativos ao surgimento da escrita, seria adequado utilizar, respectivamente, escalas de"),
  tags=["escalas de tempo"],
  alts={k: f"vida no Planeta: {a}; escrita: {b}." for k, (a, b) in {"A": ("milhares de anos", "centenas de anos"), "B": ("milhões de anos", "centenas de anos"),
        "C": ("milhões de anos", "milhares de anos"), "D": ("bilhões de anos", "milhões de anos"), "E": ("bilhões de anos", "milhares de anos")}.items()})

X(47, "H", "História", "Ciência e religião", "<p>O Documento I calcula a idade da Terra somando períodos narrados na Bíblia (da Criação ao Dilúvio, a Abraão, ao Êxodo, a Jesus Cristo): pensamento religioso. O Documento II usa a abundância de isótopos de urânio e suas meias-vidas: pensamento científico. Alternativa <strong>C</strong>.</p><p>A soma de anos do Documento I não faz dele um texto “matemático” (E): sua base são as escrituras.</p>",
  tit("Documento I e Documento II") + "[[fig:1]]"
  + p("Considerando os dois documentos, podemos afirmar que a natureza do pensamento que permite a datação da Terra é de natureza"),
  figs(("q47", "Documento I, num pergaminho: “O cômputo da Idade da Terra”: da Criação até o Dilúvio, 1.656 anos; do Dilúvio até Abraão, 292; do nascimento de Abraão até o Êxodo do Egito, 503; do Êxodo até a construção do Templo, 481; do Templo até o Cativeiro, 414; do Cativeiro até o nascimento de Jesus Cristo, 614; do nascimento de Jesus Cristo até hoje, 1.560; Idade da Terra, 5.520 anos. Documento II: “Avalia-se em cerca de quatro e meio bilhões de anos a idade da Terra, pela comparação entre a abundância relativa de diferentes isótopos de urânio com suas diferentes meias-vidas radiativas.”")),
  ["idade da Terra", "pensamento científico"])

X(48, "H", "Filosofia", "Iluminismo", "<p>No primeiro trecho, Montesquieu condena a escravidão no plano moral; no segundo, admite defendê-la por razões econômicas (exterminados os povos da América, a Europa “precisava” dos africanos, e o açúcar ficaria caro sem eles). O fundamento moral cede diante das razões econômicas. Alternativa <strong>E</strong>.</p><p>Ele não diz que a moral justificou a escravidão (B); pelo contrário, a moral a condena.</p>",
  p("Observe as duas afirmações de Montesquieu (1689-1755), a respeito da escravidão:")
  + ap("A escravidão não é boa por natureza; não é útil nem ao senhor, nem ao escravo: a este porque nada pode fazer por virtude; àquele, porque contrai com seus escravos toda sorte de maus hábitos e se acostuma insensivelmente a faltar contra todas as virtudes morais: torna-se orgulhoso, brusco, duro, colérico, voluptuoso, cruel.",
       "Se eu tivesse que defender o direito que tivemos de tornar escravos os negros, eis o que eu diria: tendo os povos da Europa exterminado os da América, tiveram que escravizar os da África para utilizá-los para abrir tantas terras. O açúcar seria muito caro se não fizéssemos que escravos cultivassem a planta que o produz.")
  + fonte("Montesquieu. <em>O espírito das leis</em>.") + p("Com base nos textos, podemos afirmar que, para Montesquieu,"),
  tags=["Montesquieu", "escravidão"])

X(49, "H", "História", "Brasil Colônia", "<p>O mapa mostra os fortes espalhados ao longo do rio Amazonas e de seus afluentes, muito a oeste da linha de Tordesilhas. Os portugueses fortificavam os rios para controlar militarmente a bacia e garantir a posse da região, reconhecida depois pelo Tratado de Madri. Alternativa <strong>A</strong>.</p><p>Os fortes não protegiam rotas comerciais, produção agrícola ou pesca (B, D, E).</p>",
  p("O mapa abaixo apresenta parte do contorno da América do Sul destacando a bacia amazônica. Os pontos assinalados representam fortificações militares instaladas no século XVIII pelos portugueses. A linha indica o Tratado de Tordesilhas revogado pelo Tratado de Madri, apenas em 1750.")
  + "[[fig:1]]" + fonte("Adaptado de Carlos de Meira Mattos. <em>Geopolítica e teoria de fronteiras</em>.")
  + p("Pode-se afirmar que a construção dos fortes pelos portugueses visava, principalmente, dominar"),
  figs(("q49", "Mapa do norte da América do Sul com o rio Amazonas e seus afluentes. Uma linha vertical à direita marca o meridiano de Tordesilhas. Pontos pretos, a maioria a oeste dessa linha, indicam fortes portugueses à beira dos rios, desde a foz até o interior da bacia.")),
  ["Tratado de Madri", "fortes"])

X(50, "H", "História", "Brasília", "<p>José Bonifácio fala em proteger a Corte de ataques externos (estratégia militar) e em abrir estradas e povoar o interior (economia). Dutra fala da segurança do Estado (militar) e da ocupação da Terra Central (econômica e territorial). As duas veem importância militar e econômica na capital no interior. Alternativa <strong>C</strong>.</p><p>Bonifácio também pensa em defesa militar, o que elimina B.</p>",
  p("A seguir são apresentadas declarações de duas personalidades da História do Brasil a respeito da localização da capital do país, respectivamente um século e uma década antes da proposta de construção de Brasília como novo Distrito Federal.")
  + tit("Declaração I: José Bonifácio") + ap("Com a mudança da capital para o interior, fica a Corte livre de qualquer assalto de surpresa externa, e se chama para as províncias centrais o excesso de população vadia das cidades marítimas. Desta Corte central dever-se-ão logo abrir estradas para as diversas províncias e portos de mar.")
  + fonte("Carlos de Meira Matos. <em>Geopolítica e modernidade: geopolítica brasileira</em>.")
  + tit("Declaração II: Eurico Gaspar Dutra") + ap("Na América do Sul, o Brasil possui uma grande área que se pode chamar também de Terra Central. Do ponto de vista da geopolítica sul-americana, sob a qual devemos encarar a segurança do Estado brasileiro, o que precisamos fazer quanto antes é realizar a ocupação da nossa Terra Central, mediante a interiorização da Capital.")
  + fonte("Adaptado de José W. Vesentini. <em>A Capital da geopolítica</em>.")
  + p("Considerando o contexto histórico que envolve as duas declarações e comparando as idéias nelas contidas, podemos dizer que"),
  tags=["interiorização da capital"])

X(51, "H", "História", "Alteridade", "<p>As três afirmações estão corretas: os artistas registraram práticas que ocorreram no Brasil (I); a antropofagia fazia parte do universo cultural indígena e o esquartejamento era uma pena da justiça portuguesa (II); e pôr lado a lado o ritual “bárbaro” e a execução “civilizada” mostra como essa distinção é relativa (III). Alternativa <strong>E</strong>.</p>",
  p("A primeira imagem abaixo (publicada no século XVI) mostra um ritual antropofágico dos índios do Brasil. A segunda mostra Tiradentes esquartejado por ordem dos representantes da Coroa portuguesa.") + "[[fig:1]][[fig:2]]"
  + fonte("Theodor De Bry, século XVI; Pedro Américo, <em>Tiradentes esquartejado</em>, 1893.")
  + p("A comparação entre as reproduções possibilita as seguintes afirmações:")
  + I3("Os artistas registraram a antropofagia e o esquartejamento praticados no Brasil.", "A antropofagia era parte do universo cultural indígena e o esquartejamento era uma forma de se fazer justiça entre luso-brasileiros.", "A comparação das imagens faz ver como é relativa a diferença entre “bárbaros” e “civilizados”, indígenas e europeus.")
  + p("Está correto o que se afirma em:"),
  figs(("q51a", "Gravura de Theodor De Bry: indígenas reunidos em torno de uma fogueira sobre a qual há uma grelha com partes de corpos humanos, num ritual antropofágico."),
       ("q51b", "Pintura de Pedro Américo: partes do corpo esquartejado de Tiradentes expostas sobre um patíbulo de madeira, com a cabeça e um crucifixo ao lado.")),
  ["antropofagia", "Tiradentes"])

X(52, "H", "História", "Encontro de culturas", "<p>Léry, que viveu entre os indígenas, adotou a rede (“à maneira dos selvagens americanos”) e destacou suas vantagens contra vermes e para manter as roupas limpas. Ele valoriza um elemento da cultura indígena e o adapta às suas necessidades. Alternativa <strong>D</strong>.</p><p>Não há desprezo nem constrangimento (A, B), e ele não afirma que os indígenas sejam superiores (C).</p>",
  p("Jean de Léry viveu na França na segunda metade do século XVI, época em que as chamadas guerras de religião opuseram católicos e protestantes. No texto abaixo, ele relata o cerco da cidade de Sancerre por tropas católicas.")
  + ap("(…) desde que os canhões começaram a atirar sobre nós com maior freqüência, tornou-se necessário que todos dormissem nas casernas. Eu logo providenciei para mim um leito feito de um lençol atado pelas suas duas pontas e assim fiquei suspenso no ar, à maneira dos selvagens americanos (entre os quais eu estive durante dez meses) o que foi imediatamente imitado por todos os nossos soldados, de tal maneira que a caserna logo ficou cheia deles. Aqueles que dormiram assim puderam confirmar o quanto esta maneira é apropriada tanto para evitar os vermes quanto para manter as roupas limpas (...).")
  + p("Neste texto, Jean de Léry"),
  tags=["Jean de Léry", "rede"])

X(53, "H", "Geografia", "Geopolítica", "<p>Os cinco membros permanentes pertencem a só três das nove civilizações do mapa: EUA, França e Inglaterra à Ocidental; Rússia à Ortodoxa; China à Sínica. Alternativa <strong>A</strong>.</p><p>Três de nove é um terço, e não dois terços (B); e Rússia e China não são da civilização Ocidental (C).</p>",
  p("Segundo Samuel Huntington (autor do livro, <em>O choque das civilizações e a recomposição da ordem mundial</em>), o mundo está dividido em nove “civilizações” conforme o mapa abaixo. Na opinião do autor, o ideal seria que cada civilização principal tivesse pelo menos um assento no Conselho de Segurança das Nações Unidas.")
  + "[[fig:1]]" + p("Sabendo-se que apenas EUA, China, Rússia, França e Inglaterra são membros permanentes do Conselho de Segurança, e analisando o mapa acima pode-se concluir que"),
  figs(("q53", "Mapa-múndi “O Mundo das Civilizações Pós-1990”, com nove civilizações: Ocidental (América do Norte, Europa Ocidental, Austrália), Latino-Americana, Africana (África subsaariana), Islâmica (Norte da África, Oriente Médio, Ásia Central, Indonésia), Sínica (China), Hindu (Índia), Ortodoxa (Rússia e Leste Europeu), Budista e Japonesa.")),
  ["Huntington", "Conselho de Segurança"])

X(54, "H", "História", "Mundo contemporâneo", "<p>Bush fala em “rezar muito” e pede que “Deus continue a abençoar os Estados Unidos”; Bin Laden diz que “Deus abençoou” a vanguarda muçulmana e divide o mundo entre fiéis e infiéis. Os dois usam um discurso religioso para justificar o sacrifício e a guerra. Alternativa <strong>C</strong>.</p><p>Nenhum dissocia a justiça da religião (D, E).</p>",
  p("No dia 7 de outubro de 2001, Estados Unidos e Grã-Bretanha declararam guerra ao regime Talibã, no Afeganistão.", "Leia trechos das declarações do presidente dos Estados Unidos, George W. Bush, e de Osama Bin Laden, líder muçulmano, nessa ocasião:")
  + tit("George Bush:") + ap("Um comandante-chefe envia os filhos e filhas dos Estados Unidos à batalha em território estrangeiro somente depois de tomar o maior cuidado e depois de rezar muito. Pedimos-lhes que estejam preparados para o sacrifício das próprias vidas. A partir de 11 de setembro, uma geração inteira de jovens americanos teve uma nova percepção do valor da liberdade, do seu preço, do seu dever e do seu sacrifício. Que Deus continue a abençoar os Estados Unidos.")
  + tit("Osama Bin Laden:") + ap("Deus abençoou um grupo de vanguarda de muçulmanos, a linha de frente do Islã, para destruir os Estados Unidos. Um milhão de crianças foram mortas no Iraque, e para eles isso não é uma questão clara. Mas quando pouco mais de dez foram mortos em Nairóbi e Dar-es-Salaam, o Afeganistão e o Iraque foram bombardeados e a hipocrisia ficou atrás da cabeça dos infiéis internacionais. Digo a eles que esses acontecimentos dividiram o mundo em dois campos, o campo dos fiéis e o campo dos infiéis. Que Deus nos proteja deles.")
  + fonte("Adaptados de <em>O Estado de S. Paulo</em>, 8/10/2001.") + p("Pode-se afirmar que"),
  tags=["11 de setembro", "discurso religioso"],
  alts=A5("a justificativa das ações militares encontra sentido apenas nos argumentos de George W. Bush.", "a justificativa das ações militares encontra sentido apenas nos argumentos de Osama Bin Laden.",
          "ambos apóiam-se num discurso de fundo religioso para justificar o sacrifício e reivindicar a justiça.", "ambos tentam associar a noção de justiça a valores de ordem política, dissociando-a de princípios religiosos.",
          "ambos tentam separar a noção de justiça das justificativas de ordem religiosa, fundamentando-a numa estratégia militar."))

X(55, "H", "História", "Mundo contemporâneo", "<p>Blair destaca que o ataque afetou “os meios de vida”, as empresas aéreas, o turismo, a confiança econômica, os empregos e os negócios, e conclui que “nossa prosperidade e padrão de vida requerem uma resposta”. O interesse em destaque é econômico. Alternativa <strong>E</strong>.</p><p>Há menção às religiões, mas só para dizer que o ataque atingiu pessoas de todas elas (D).</p>",
  p("O texto abaixo é um trecho do discurso do primeiro-ministro britânico, Tony Blair, pronunciado quando da declaração de guerra ao regime Talibã:")
  + ap("<em>Essa atrocidade</em> [o atentado de 11 de setembro, em Nova York] <em>foi um ataque contra todos nós, contra pessoas de todas e nenhuma religião. Sabemos que a Al-Qaeda ameaça a Europa, incluindo a Grã-Bretanha, e qualquer nação que não compartilhe de seu fanatismo. Foi um ataque à vida e aos meios de vida. As empresas aéreas, o turismo e outras indústrias foram afetadas e a confiança econômica sofreu, afetando empregos e negócios britânicos. Nossa prosperidade e padrão de vida requerem uma resposta aos ataques terroristas.</em>")
  + fonte("<em>O Estado de S. Paulo</em>, 8/10/2001.") + p("Nesta declaração, destacaram-se <u>principalmente</u> os interesses de ordem"),
  tags=["Tony Blair"], alts=A5("moral.", "militar.", "jurídica.", "religiosa.", "econômica."))

X(56, "H", "Geografia", "Fontes de energia", "<p>A produção interna passou de cerca de 55% do consumo em 1990 para cerca de 80% em 2002. E as importações, antes vindas da Arábia Saudita, do Iraque, do Irã e do Catar, passaram a vir principalmente da Nigéria e da Argélia, com Arábia Saudita e Iraque em quantidades menores. Alternativa <strong>D</strong>.</p><p>A produção nacional aumentou, e não diminuiu (B, C).</p>",
  p("Os dados abaixo referem-se à origem do petróleo consumido no Brasil em dois diferentes anos.") + "[[fig:1]]"
  + p("Analisando os dados, pode-se perceber que o Brasil adotou determinadas estratégias energéticas, dentre as quais podemos citar:"),
  figs(("q56", "Quatro gráficos. “Origens do consumo em 1990 (em %)”: produção interna cerca de 55, importação cerca de 45. “Origens do consumo em 2002 (em %)”: produção interna cerca de 80, importação cerca de 20. “Origens das importações em 1990 (milhares de barris)”: Arábia Saudita 158, Iraque 150, Irã 100, Catar 37. “Origens das importações em 2002”: Nigéria 114, Argélia 77, Arábia Saudita 60, Iraque 33.")),
  ["petróleo", "dependência externa"])

CRESC = tabela(["Período", "Taxa anual média de crescimento natural (%)"], [["1920-1940", "1,90"], ["1940-1950", "2,40"], ["1950-1960", "2,99"], ["1960-1970", "2,89"], ["1970-1980", "2,48"], ["1980-1991", "1,93"], ["1991-2000", "1,64"]]) + fonte("Fonte: IBGE, Anuários Estatísticos do Brasil.")
X(57, "H", "Geografia", "Demografia", "<p>As maiores taxas do século ocorreram entre 1950 e 1970 (2,99% e 2,89% ao ano), período de queda da mortalidade com natalidade ainda alta: a explosão demográfica. Alternativa <strong>B</strong>.</p><p>Entre 1980 e 2000 as taxas continuaram caindo, e não se estabilizaram (E); e a densidade demográfica não diminuiu (D), porque a população seguiu crescendo.</p>",
  p("O quadro abaixo mostra a taxa de crescimento natural da população brasileira no século XX.") + CRESC + p("Analisando os dados podemos caracterizar o período entre"),
  tags=["explosão demográfica"])
X(58, "H", "Geografia", "Demografia", "<p>As taxas caem de 2,99% (1950-1960) para 1,64% (1991-2000): nas últimas décadas a população cresceu a um ritmo percentual menor. Alternativa <strong>A</strong>.</p><p>Taxas positivas significam que a população continuou aumentando, então ela não decresceu nem ficou inalterada (C, E).</p>",
  p("Ainda com base na tabela da questão anterior, é correto afirmar que a população brasileira") + CRESC, tags=["crescimento demográfico"])

X(59, "H", "Sociologia", "Trabalho feminino", "<p>No gráfico, a participação feminina cai de cerca de 20% em 1940 para 15% em 1950 e depois cresce sem parar até cerca de 42% em 2000, enquanto a masculina cai para cerca de 58%. Mantida a tendência, as duas devem se igualar em pouco tempo. Alternativa <strong>E</strong>.</p><p>O mínimo feminino foi em 1950, e não em 1940 (D); e o crescimento feminino foi maior justamente nas três últimas décadas (B).</p>",
  p("Um dos aspectos utilizados para avaliar a posição ocupada pela mulher na sociedade é a sua participação no mercado de trabalho. O gráfico mostra a evolução da presença de homens e mulheres no mercado de trabalho entre os anos de 1940 e 2000.")
  + "[[fig:1]]" + fonte("Fonte: IBGE, Anuários Estatísticos do Brasil.")
  + p("Da leitura do gráfico, pode-se afirmar que a participação percentual do trabalho feminino no Brasil"),
  figs(("q59", "Gráfico de linhas da participação no mercado de trabalho (%) de 1940 a 2000. Homens: cerca de 80, 83, 80, 78, 72, 65 e 58. Mulheres: cerca de 20, 15, 18, 20, 27, 35 e 42.")),
  ["mulher no mercado de trabalho"])

X(60, "H", "Geografia", "Fome", "<p>O texto II, mais recente, diz que o problema não é a produção de alimentos, mas o descompasso entre o poder aquisitivo da população e o custo dos alimentos. A fome persiste principalmente pela renda insuficiente dos trabalhadores. Alternativa <strong>A</strong>.</p><p>A baixa produtividade agrícola, citada em 1947 (E), já não explica o problema segundo o texto de 2001.</p>",
  p("Leia o texto I de Josué de Castro, publicado em 1947.")
  + ap("O Brasil, como país subdesenvolvido, em fase de acelerado processo de industrialização não conseguiu ainda se libertar da fome. Os baixos índices de produtividade agrícola se constituíram como fatores de base no condicionamento de um abastecimento alimentar insuficiente e inadequado às necessidades alimentares do nosso povo.")
  + fonte("Adaptado de Josué de Castro. <em>Geografia da Fome</em>.") + p("Leia o texto II sobre a fome no Brasil, publicado em 2001.")
  + ap("Uma das evidências contidas no mapa da fome consiste na constatação de que o problema alimentar no Brasil não reside na disponibilidade e produção interna de grãos e dos produtos tradicionalmente consumidos no País, mas antes no descompasso entre o poder aquisitivo de ampla parcela da população e o custo de aquisição de uma quantidade de alimentos compatível com as necessidades do trabalhador e de sua família.")
  + fonte("&lt;http://www.mct.gov.br&gt;") + p("Comparando os textos I e II podemos concluir que a persistência da fome no Brasil resulta principalmente"),
  tags=["Josué de Castro", "fome"])

X(61, "H", "Geografia", "Violência urbana", "<p>No gráfico, a participação do interior nos roubos do Estado subiu de 23,5% (1995) para 33,9% (2003), enquanto a da capital caiu de 49,2% para 38,3%. Com a frase “A rota do crime segue na esteira da rota da riqueza”, conclui-se que o interior enriqueceu e passou a atrair roubos. Alternativa <strong>B</strong>.</p><p>O gráfico mostra porcentagens da distribuição dos roubos, e não o total, por isso não permite dizer que a criminalidade caiu (D, E).</p>",
  "[[fig:1]]" + fonte("<em>Folha de SP</em>, 29/06/03.")
  + p("O gráfico e a frase acima, tirados de um jornal, estão ambos relacionados à evolução média da violência no Estado de São Paulo. A associação entre estas duas linguagens – a gráfica e a escrita – permite concluir que, percentualmente,"),
  figs(("q61", "Gráfico “Percentual de roubos por região”, de 1995 a 2003, com a frase ao lado “A rota do crime segue na esteira da rota da riqueza”. Capital: de 49,2% para 38,3%. Região metropolitana: de 27,3% para 26,8%. Interior: de 23,5% para 33,9%.")),
  ["roubos", "interiorização da riqueza"])

X(62, "L", "Língua Portuguesa", "Polissemia", "<p>Mafalda ouve falar do “indicador de desemprego” (um índice econômico) e entende “indicador” como o dedo indicador, o mesmo que ela admirava no primeiro quadrinho e que o patrão usa para mandar operários embora. O humor vem de dar o mesmo sentido (o dedo) à palavra nos dois momentos. Alternativa <strong>C</strong>.</p><p>Ela não usa corretamente a expressão (D): justamente a entende mal.</p>",
  "[[fig:1]]" + fonte("Quino. <em>Mafalda</em>.") + p("O humor presente na tirinha decorre <u>principalmente</u> do fato de a personagem Mafalda"),
  figs(("q62", "Tira de Mafalda em quatro quadros. 1: Mafalda, olhando o dedo indicador erguido: “É incrível a importância do dedo indicador!”. 2: apontando: “Um patrão faz assim com o indicador... e três mil operários vão para a rua!”. 3: assustada, com um balão: “AAAAAH!”. 4: olhando o dedo, pensa: “Esse deve ser o tal indicador de desemprego, de que tanto se fala!”.")),
  ["Mafalda", "duplo sentido"])

X(63, "L", "Literatura", "Intertextualidade", "<p>O texto de Nádia Gotlib destaca, no quadro “Operários”, pessoas diferentes que são iguais enquanto força de trabalho, amontoadas como mercadoria. Os versos de João Cabral (“Somos muitos severinos / iguais em tudo e na sina”) tratam também de trabalhadores tornados iguais pela dureza do trabalho. Alternativa <strong>B</strong>.</p><p>Gullar fala de um funcionário isolado (C), Pessoa, de uma angústia individual (D), e Drummond, da alienação dos ricos (E).</p>",
  "[[fig:1]]" + fonte("Tarsila do Amaral, <em>Operários</em>.")
  + ap("<em>Desiguais na fisionomia, na cor e na raça, o que lhes assegura identidade peculiar, são iguais enquanto frente de trabalho. Num dos cantos, as chaminés das indústrias se alçam verticalmente. No mais, em todo o quadro, rostos colados, um ao lado do outro, em pirâmide que tende a se prolongar infinitamente, como mercadoria que se acumula, pelo quadro afora.</em>")
  + fonte("Nádia Gotlib. <em>Tarsila do Amaral, a modernista</em>.")
  + p("O texto aponta no quadro de Tarsila do Amaral um tema que também se encontra nos versos transcritos em:"),
  figs(("q63", "Pintura “Operários”, de Tarsila do Amaral: dezenas de rostos de homens e mulheres de diferentes cores e traços, colados uns aos outros em pirâmide, e chaminés de fábrica ao fundo, no canto esquerdo."),
       ("q63a", "Quatro versos de Vinícius de Moraes que pedem que se pense nas meninas e nas mulheres de rotas alteradas."),
       ("q63b", "Quatro versos de João Cabral de Melo Neto: muitos severinos, iguais em tudo e na sina de abrandar pedras suando muito."),
       ("q63c", "Quatro versos de Ferreira Gullar sobre o funcionário público que não cabe no poema, com seu salário de fome e sua vida fechada em arquivos."),
       ("q63d", "Versos de Fernando Pessoa: “Não sou nada. / Nunca serei nada. / Não posso querer ser nada. / À parte isso, tenho em mim todos os sonhos do mundo.”"),
       ("q63e", "Versos de Carlos Drummond de Andrade sobre os inocentes do Leblon, que não viram o navio entrar, ignoravam tudo e passam óleo nas costas na areia quente.")),
  ["Tarsila do Amaral", "João Cabral"], alts=ALT(2))

completar(Q, R)
