# Enem 2000 (data não confirmada; dataExame omitida), caderno amarelo: prova única de 63 questões (modelo antigo, sem divisão por áreas).
# Fonte do PDF: arquivo 'Prova_Caderno_Amarelo_2000' do usuário (rodapé "AMARELA"; tema de redação de 2000, direitos da criança e do adolescente).
# Gabarito: tabela "GABARITO ENEM 2000" do Curso Objetivo (colunas Amarela/Branca/Rosa/Verde), coluna Amarela, lida duas vezes e conferida
# com a resolução própria das questões de cálculo (Q5, Q8, Q9, Q13, Q14, Q25, Q26, Q38–Q40, Q42–Q44, Q49, Q50, Q58). Não achei cópia oficial acessível.
# Duas colunas em todas as páginas; números das questões em fontes variadas (até Courier): extrator com LINHAS=1 NXR=27-30,304-306 NFONT="" COLS=3..13 COLX=300 YMIN=40 YMAX=805.
# Linhas no pé das colunas (y > 805) digitadas à mão. Protegidos como imagem: Ferreira Gullar (Q1, poema e alternativas), Manuel Bandeira (Q20) e
# os poemas das alternativas da Q46 (João Cabral, Mário Chamie, Gullar; Álvares de Azevedo e Machado também, por uniformidade).
# Em texto: Mário de Andrade, Machado, Oswald de Andrade (domínio público desde 2025), Locke e a prosa (Millôr, Q31–33).
import sys, pathlib, re, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar

ID = "enem-2000"
META = {"id": ID, "banca": "Enem", "ano": 2000, "titulo": "Enem 2000: Prova objetiva", "fonte": "Inep",
        "duracaoMinutos": 300, "area": "Prova objetiva (63 questões)", "caderno": "amarelo", "dia": 1, "fonteGabarito": {"oficial": False, "nome": "Curso Objetivo", "url": "https://www.curso-objetivo.br/vestibular/resolucao-comentada/enem/2000/ENEM2000_gabarito.pdf"}}
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
I4 = lambda *xs: '<ol type="I">' + "".join(f"<li>{x}</li>" for x in xs) + "</ol>"

X(1, "L", "Literatura", "Sinestesia", "<p>Em “e o pão preserve aquele branco / sabor de alvorada”, uma impressão visual (a cor branca) se mistura a uma impressão do paladar (o sabor): é a sinestesia. Alternativa <strong>A</strong>.</p><p>Nos outros trechos há imagens e sentimentos (o orvalho, o medo da natureza, o abismo do céu), mas sem mistura de sentidos diferentes.</p>",
  p("Ferreira Gullar, um dos grandes poetas brasileiros da atualidade, é autor de “Bicho urbano”, poema sobre a sua relação com as pequenas e grandes cidades.") + "[[fig:1]]"
  + fonte("(GULLAR, Ferreira. <em>Toda poesia</em>. Rio de Janeiro: José Olympio Editora, 1991)")
  + p("Embora não opte por viver numa pequena cidade, o poeta reconhece elementos de valor no cotidiano das pequenas comunidades. Para expressar a relação do homem com alguns desses elementos, ele recorre à sinestesia, construção de linguagem em que se mesclam impressões sensoriais diversas. Assinale a opção em que se observa esse recurso."),
  figs(("q01", "Trecho do poema “Bicho urbano”, de Ferreira Gullar, em versos: o poeta diz que mentiria se dissesse preferir morar numa cidade pequena como Pirapemas, ainda que lá se lave o rosto no orvalho e o pão tenha um sabor branco de alvorada; depois diz que a natureza, com matos sombrios, águas e aves como aparições, o assusta quase tanto quanto o abismo de gases e estrelas sobre sua cabeça."),
       ("q01a", "Versos de Gullar sobre o pão que preserva um sabor branco de alvorada."), ("q01b", "Versos de Gullar sobre lavar o rosto no orvalho de manhã."),
       ("q01c", "Versos de Gullar: a natureza assusta, com seus matos sombrios e suas águas."), ("q01d", "Versos de Gullar sobre as aves que são como aparições e assustam."),
       ("q01e", "Versos de Gullar sobre o susto diante do abismo de gases e de estrelas.")),
  ["Ferreira Gullar", "sinestesia"], alts=ALT(2))

X(2, "N", "Química", "Fermentação", "<p>Só II está correta: a fermentação produz gás carbônico, que fica preso em bolhas na massa, aumenta o volume, diminui a densidade e faz a bola subir. Alternativa <strong>B</strong>.</p><p>I é falsa: a fermentação depende de seres vivos, as leveduras do fermento biológico. III é falsa: o álcool é menos denso que a água, e não é ele que faz a massa subir.</p>",
  p("No processo de fabricação de pão, os padeiros, após prepararem a massa utilizando fermento biológico, separam uma porção de massa em forma de “bola” e a mergulham num recipiente com água, aguardando que ela suba, como pode ser observado, respectivamente, em I e II do esquema abaixo. Quando isso acontece, a massa está pronta para ir ao forno.")
  + "[[fig:1]]" + p("Um professor de Química explicaria esse procedimento da seguinte maneira:")
  + ap("“A bola de massa torna-se menos densa que o líquido e sobe. A alteração da densidade deve-se à fermentação, processo que pode ser resumido pela equação", "C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> (glicose) → 2 C<sub>2</sub>H<sub>5</sub>OH (álcool comum) + 2 CO<sub>2</sub> (gás carbônico) + energia.”")
  + p("Considere as afirmações abaixo.")
  + I3("A fermentação dos carboidratos da massa de pão ocorre de maneira espontânea e não depende da existência de qualquer organismo vivo.", "Durante a fermentação, ocorre produção de gás carbônico, que se vai acumulando em cavidades no interior da massa, o que faz a bola subir.", "A fermentação transforma a glicose em álcool. Como o álcool tem maior densidade do que a água, a bola de massa sobe.")
  + p("Dentre as afirmativas, apenas:"),
  figs(("q02", "Dois recipientes com água: em I, a bola de massa está no fundo; em II, depois de algum tempo, a bola flutua na superfície.")),
  ["fermentação", "densidade"])

X(3, "N", "Física", "Calor", "<p>O barro não esmaltado é poroso: um pouco de água atravessa a parede e evapora do lado de fora. A evaporação retira calor da moringa e da água de dentro, que esfriam. Alternativa <strong>C</strong>.</p><p>O barro não “gela” por reação química (B) nem isola como isopor (A): sem a evaporação, a água ficaria à temperatura ambiente.</p>",
  p("Ainda hoje, é muito comum as pessoas utilizarem vasilhames de barro (moringas ou potes de cerâmica não esmaltada) para conservar água a uma temperatura menor do que a do ambiente. Isso ocorre porque:"),
  tags=["evaporação", "moringa"])

X(4, "H", "História", "Roma Antiga", "<p>Para Cícero, na República, todos se submetem à lei e é ela que garante a liberdade: os direitos de um cidadão terminam onde começam os de outro (III). Para Ulpiano, no Império, a vontade do príncipe vale como lei, ou seja, há um poder acima da legislação (IV). Alternativa <strong>E</strong>.</p><p>I é falsa, porque os romanos valorizavam o direito; II também, porque no Império a lei não vinha de representantes do povo.</p>",
  ap("“Somos servos da lei para podermos ser livres.” — Cícero", "“O que apraz ao príncipe tem força de lei.” — Ulpiano")
  + p("As frases acima são de dois cidadãos da Roma Clássica que viveram praticamente no mesmo século, quando ocorreu a transição da República (Cícero) para o Império (Ulpiano).", "Tendo como base as sentenças acima, considere as afirmações:")
  + I4("A diferença nos significados da lei é apenas aparente, uma vez que os romanos não levavam em consideração as normas jurídicas.", "Tanto na República como no Império, a lei era o resultado de discussões entre os representantes escolhidos pelo povo romano.",
       "A lei republicana definia que os direitos de um cidadão acabavam quando começavam os direitos de outro cidadão.", "Existia, na época imperial, um poder acima da legislação romana.")
  + p("Estão corretas, apenas:"),
  tags=["República romana", "Império romano"])

X(5, "H", "Geografia", "Orientação", "<p>A via 1 contorna o centro (é perimetral) e a via 2 vai em direção ao centro (é radial). Sem pontos cardeais, vale só a posição relativa: no esquema, a via 2 fica 90° no sentido horário a partir da via 1. Se a via 1 estiver ao sul do centro, a via 2 estará a oeste. Alternativa <strong>B</strong>.</p><p>Em A e C, a via radial ficaria 90° no sentido anti-horário, o que não corresponde ao esquema.</p>",
  p("Em certa cidade, algumas de suas principais vias têm a designação “radial” ou “perimetral”, acrescentando-se ao nome da via uma referência ao ponto cardeal correspondente.", "As ruas 1 e 2 estão indicadas no esquema abaixo, em que não estão explicitados os pontos cardeais.") + "[[fig:1]]"
  + p("Os nomes corretos das vias 1 e 2 podem, respectivamente, ser:"),
  figs(("q05", "Esquema de ruas em torno de um círculo marcado “CENTRO”: a via 1, em destaque, é um arco que contorna o centro pelo lado direito; a via 2, também em destaque, é uma reta que sai de baixo em direção ao centro.")),
  ["radial e perimetral", "pontos cardeais"])

X(6, "L", "Língua Portuguesa", "Ambiguidade", "<p>No primeiro quadrinho, Rosinha diz “Olha o passarinho!”, expressão que os fotógrafos usam para que a pessoa olhe para a câmera. Chico Bento entende ao pé da letra e procura um passarinho de verdade. O humor nasce desse sentido inadequado. Alternativa <strong>D</strong>.</p>",
  p("Em uma conversa ou leitura de um texto, corre-se o risco de atribuir um significado inadequado a um termo ou expressão, e isso pode levar a certos resultados inesperados, como se vê nos quadrinhos abaixo.") + "[[fig:1]]"
  + fonte("(SOUZA, Maurício de. <em>Chico Bento</em>. Rio de Janeiro: Ed. Globo, nº 335, Nov./99)")
  + p("Nessa historinha, o efeito humorístico origina-se de uma situação criada pela fala da Rosinha no primeiro quadrinho, que é:"),
  figs(("q06", "Tira de Chico Bento em três quadros, sem as falas legíveis na descrição: Rosinha chama Chico e aponta uma câmera para ele; o flash dispara; no último quadro, Chico, sentado no chão, procura alguma coisa e diz: “Quem intendi as muié?”.")),
  ["Chico Bento", "sentido literal"], alts=dict(D[6], E="Cuidado com o <em>flash</em>!"))

X(7, "N", "Física", "Aquecedor solar", "<p>II está correta: o vidro deixa entrar a luz e retém a radiação infravermelha, como numa estufa. III também: superfícies escuras absorvem mais radiação. I é falsa: o reservatório de água quente deve ser isolado termicamente para não perder calor, e não bom condutor. Alternativa <strong>E</strong>.</p>",
  p("O resultado da conversão direta de energia solar é uma das várias formas de energia alternativa de que se dispõe. O aquecimento solar é obtido por uma placa escura coberta por vidro, pela qual passa um tubo contendo água. A água circula, conforme mostra o esquema abaixo.") + "[[fig:1]]"
  + fonte("Fonte: Adaptado de PALZ, Wolfgang. <em>Energia solar e fontes alternativas</em>. Hemus, 1981.")
  + p("São feitas as seguintes afirmações quanto aos materiais utilizados no aquecedor solar:")
  + I3("o reservatório de água quente deve ser metálico para conduzir melhor o calor.", "a cobertura de vidro tem como função reter melhor o calor, de forma semelhante ao que ocorre em uma estufa.", "a placa utilizada é escura para absorver melhor a energia radiante do Sol, aquecendo a água com maior eficiência.")
  + p("Dentre as afirmações acima, pode-se dizer que, apenas está(ão) correta(s):"),
  figs(("q07", "Esquema de aquecedor solar: um coletor inclinado, com vidro e placa escura, recebe a radiação solar; a água sobe aquecida até o reservatório de água quente, de onde sai água para o consumo; acima fica o reservatório de água fria, que alimenta o sistema.")),
  ["efeito estufa", "radiação"])

X(8, "M", "Matemática", "Porcentagem", "<p>As marcas X e Y respondem por 60% de 150 = 90 carros. Como X é o dobro de Y, Y + 2Y = 90, então Y = 30. Alternativa <strong>B</strong>.</p><p>60 (E) é o número de carros da marca X, e 90 seria o total das duas marcas juntas. Os outros 60 carros roubados são de outras marcas.</p>",
  p("Uma companhia de seguros levantou dados sobre os carros de determinada cidade e constatou que são roubados, em média, 150 carros por ano.", "O número de carros roubados da marca X é o dobro do número de carros roubados da marca Y, e as marcas X e Y juntas respondem por cerca de 60% dos carros roubados.", "O número esperado de carros roubados da marca Y é:"),
  tags=["porcentagem", "proporção"])

X(9, "N", "Física", "Astronomia", "<p>Vista de lado, cada lua aparece a uma distância de Júpiter que não passa do raio de sua órbita. O ponto 4, o mais afastado, só pode ser Calisto, a lua de órbita maior. O ponto 1, também longe, deve ser Ganimedes, a segunda maior órbita. Os pontos 2 e 3, perto do planeta, são Io e Europa, de órbitas menores. Alternativa <strong>B</strong>.</p>",
  p("A tabela abaixo resume alguns dados importantes sobre os satélites de Júpiter.")
  + tabela(["Nome", "Diâmetro (km)", "Distância média ao centro de Júpiter (km)", "Período orbital (dias terrestres)"],
           [["Io", "3.642", "421.800", "1,8"], ["Europa", "3.138", "670.900", "3,6"], ["Ganimedes", "5.262", "1.070.000", "7,2"], ["Calisto", "4.800", "1.880.000", "16,7"]])
  + p("Ao observar os satélites de Júpiter pela primeira vez, Galileu Galilei fez diversas anotações e tirou importantes conclusões sobre a estrutura de nosso universo. A figura abaixo reproduz uma anotação de Galileu referente a Júpiter e seus satélites.") + "[[fig:1]]"
  + p("De acordo com essa representação e com os dados da tabela, os pontos indicados por 1, 2, 3 e 4 correspondem, respectivamente, a:"),
  figs(("q09", "Desenho de Galileu: Júpiter como um círculo no meio; à esquerda, longe dele, o ponto 1; à direita, bem perto, os pontos 2 e 3; e, mais longe à direita, o ponto 4.")),
  ["luas de Júpiter", "Galileu"])

X(10, "N", "Biologia", "Respiração", "<p>Em altitude, a pressão atmosférica é menor, e com ela a pressão parcial do oxigênio: cada inspiração leva menos oxigênio aos pulmões. O organismo precisa de alguns dias para se adaptar, por exemplo produzindo mais hemácias. Alternativa <strong>A</strong>.</p>",
  p("A adaptação dos integrantes da seleção brasileira de futebol à altitude de La Paz foi muito comentada em 1995, por ocasião de um torneio, como pode ser lido no texto abaixo.")
  + ap("“A seleção brasileira embarca hoje para La Paz, capital da Bolívia, situada a 3.700 metros de altitude, onde disputará o torneio Interamérica. A adaptação deverá ocorrer em um prazo de 10 dias, aproximadamente. O organismo humano, em altitudes elevadas, necessita desse tempo para se adaptar, evitando-se, assim, risco de um colapso circulatório.”")
  + fonte("(Adaptado da revista <em>Placar</em>, edição fev.1995)")
  + p("A adaptação da equipe foi necessária principalmente porque a atmosfera de La Paz, quando comparada à das cidades brasileiras, apresenta:"),
  tags=["altitude", "pressão atmosférica"], alts=dict(D[10], E="maior pressão e menor temperatura."))

NUC = (tit("Texto para as questões 11 e 12.") + p("A energia térmica liberada em processos de fissão nuclear pode ser utilizada na geração de vapor para produzir energia mecânica que, por sua vez, será convertida em energia elétrica. Abaixo está representado um esquema básico de uma usina de energia nuclear.") + "[[fig:1]]")
F_NUC = figs(("q11", "Esquema de usina nuclear: as pilhas nucleares aquecem a água do reator, que vira vapor e move a turbina ligada ao gerador; o vapor passa pelo condensador, resfriado por água bombeada do rio, e volta ao reator por uma bomba d’água; a água do rio retorna aquecida ao rio."))
X(11, "N", "Biologia", "Poluição térmica", "<p>I está correta: a água mais quente dissolve menos oxigênio. II também: a temperatura altera o metabolismo dos peixes, que são animais de temperatura variável. III é falsa: o aquecimento costuma favorecer a proliferação de bactérias e algas. Alternativa <strong>D</strong>.</p>",
  NUC + p("Com relação ao impacto ambiental causado pela poluição térmica no processo de refrigeração da usina nuclear, são feitas as seguintes afirmações:")
  + I3("o aumento na temperatura reduz, na água do rio, a quantidade de oxigênio nela dissolvido, que é essencial para a vida aquática e para a decomposição da matéria orgânica.", "o aumento da temperatura da água modifica o metabolismo dos peixes.", "o aumento na temperatura da água diminui o crescimento de bactérias e de algas, favorecendo o desenvolvimento da vegetação.")
  + p("Das afirmativas acima, somente está(ão) correta(s):"), F_NUC, ["poluição térmica", "oxigênio dissolvido"])
X(12, "N", "Física", "Usina nuclear", "<p>I e II descrevem bem o funcionamento: o vapor a alta pressão gira a turbina, que, acoplada ao gerador, produz energia elétrica. III é falsa: no condensador, a água é resfriada (o vapor se condensa), e não pré-aquecida. Alternativa <strong>D</strong>.</p>",
  NUC + p("A partir do esquema são feitas as seguintes afirmações:")
  + I3("a energia liberada na reação é usada para ferver a água que, como vapor a alta pressão, aciona a turbina.", "a turbina, que adquire uma energia cinética de rotação, é acoplada mecanicamente ao gerador para produção de energia elétrica.", "a água depois de passar pela turbina é pré-aquecida no condensador e bombeada de volta ao reator.")
  + p("Dentre as afirmações acima, somente está(ão) correta(s):"), F_NUC, ["transformações de energia", "condensador"])

X(13, "M", "Matemática", "Progressão aritmética", "<p>As larguras dos 5 degraus variam igualmente de 60 cm a 30 cm, formando uma progressão aritmética de razão −7,5: 60; 52,5; 45; 37,5; 30. A soma é (60 + 30) × 5/2 = 225 cm. Alternativa <strong>D</strong>.</p>",
  p("Um marceneiro deseja construir uma escada trapezoidal com 5 degraus, de forma que o mais baixo e o mais alto tenham larguras respectivamente iguais a 60 cm e a 30 cm, conforme a figura:") + "[[fig:1]]"
  + p("Os degraus serão obtidos cortando-se uma peça linear de madeira cujo comprimento mínimo, em cm, deve ser:"),
  figs(("q13", "Escada em forma de trapézio com 5 degraus horizontais igualmente espaçados: o de cima mede 30 e o de baixo, 60.")),
  ["progressão aritmética", "trapézio"])

X(14, "N", "Física", "Rendimento", "<p>Do tanque saem 72 kW. No motor, 1 kW se perde por evaporação e 56,8 kW saem como calor nos gases de escape: 57,8 kW de 72 kW, cerca de 80%. Só 14,2 kW saem do motor como trabalho. Alternativa <strong>A</strong>.</p>",
  p("O esquema abaixo mostra, em termos de potência (energia/tempo), aproximadamente, o fluxo de energia, a partir de uma certa quantidade de combustível vinda do tanque de gasolina, em um carro viajando com velocidade constante.") + "[[fig:1]]"
  + p("O esquema mostra que, na queima da gasolina, no motor de combustão, uma parte considerável de sua energia é dissipada. Essa perda é da ordem de:"),
  figs(("q14", "Diagrama de fluxo de potência: do tanque de gasolina saem 72 kW; 1 kW se perde por evaporação; no motor de combustão, 56,8 kW saem como energia dos gases de escape e calor ao ar; 14,2 kW seguem para transmissão e engrenagens; destes, 2,2 kW vão para luzes, ventilador e outros, 3 kW se perdem como energia térmica, e 9 kW chegam às rodas.")),
  ["rendimento", "motor a combustão"])

X(15, "N", "Física", "Leitura de gráficos", "<p>No gráfico, há países com consumo perto de 1 TEP e outros perto de 5 TEP com IDH próximo de 0,7. Mais energia não garante, sozinha, mais desenvolvimento. Alternativa <strong>D</strong>.</p><p>A curva é crescente (A é falsa), há países com menos de 1 TEP e IDH acima de 0,8 (B é falsa), e vários países de IDH alto consomem menos de 7 TEP (E é falsa).</p>",
  p("As sociedades modernas necessitam cada vez mais de energia. Para entender melhor a relação entre desenvolvimento e consumo de energia, procurou-se relacionar o Índice de Desenvolvimento Humano (IDH) de vários países com o consumo de energia nesses países.",
    "O IDH é um indicador social que considera a longevidade, o grau de escolaridade, o PIB (Produto Interno Bruto) <em>per capita</em> e o poder de compra da população. Sua variação é de 0 a 1. Valores do IDH próximos de 1 indicam melhores condições de vida.",
    "Tentando-se estabelecer uma relação entre o IDH e o consumo de energia <em>per capita</em> nos diversos países, no biênio 1991-1992, obteve-se o gráfico abaixo, onde cada ponto isolado representa um país, e a linha cheia, uma curva de aproximação.") + "[[fig:1]]"
  + fonte("Fonte: GOLDEMBERG, J. <em>Energia, meio ambiente e desenvolvimento</em>. São Paulo: Edusp, 1998.") + p("Com base no gráfico, é correto afirmar que:"),
  figs(("q15", "Gráfico de dispersão do IDH (0 a 1) em função do consumo de energia per capita (0 a 10 TEP por habitante). Os pontos sobem rapidamente entre 0 e 2 TEP, de IDH cerca de 0,2 até 0,8, e depois ficam entre 0,8 e 0,95, com alguns pontos isolados mais baixos, como um perto de 5 TEP com IDH cerca de 0,73. A curva de aproximação cresce depressa e se estabiliza perto de 0,85. Nota: TEP é tonelada equivalente de petróleo.")),
  ["IDH", "consumo de energia"], alts=dict(D[15], E="os países com altos valores de IDH apresentam um grande consumo de energia <em>per capita</em> (acima de 7 TEP)."))

X(16, "N", "Biologia", "Evolução", "<p>Ema (América do Sul), avestruz (África) e emu (Austrália) vivem em continentes que um dia formaram um único supercontinente no hemisfério sul. Com a separação das massas continentais, as populações do ancestral comum ficaram isoladas e se diferenciaram. Alternativa <strong>D</strong>.</p><p>Essas aves não voam, então não poderiam ter cruzado oceanos (B), e surgiram muito antes dos humanos (C).</p>",
  p("No mapa, é apresentada a distribuição geográfica de aves de grande porte e que não voam.") + "[[fig:1]]"
  + p("Há evidências mostrando que essas aves, que podem ser originárias de um mesmo ancestral, sejam, portanto, parentes. Considerando que, de fato, tal parentesco ocorra, uma explicação possível para a separação geográfica dessas aves, como mostrada no mapa, poderia ser:"),
  figs(("q16", "Mapa-múndi com três aves indicadas: a ema na América do Sul, o avestruz na África e o emu na Austrália.")),
  ["deriva continental", "especiação"])

X(17, "H", "História", "Calendários", "<p>Os quatro calendários marcam o ano de 2000 de formas diferentes (2000, 1378, 5760, ano do coelho), cada um a partir de um marco próprio, quase sempre religioso. O calendário cristão é usado internacionalmente, mas cada cultura mantém o seu. Alternativa <strong>B</strong>.</p><p>A religião foi decisiva (D é falsa), e o calendário judaico, por exemplo, é mais antigo que o cristão (E).</p>",
  p("Os quatro calendários apresentados abaixo mostram a variedade na contagem do tempo em diversas sociedades.") + "[[fig:1]]"
  + fonte("Fonte: Adaptado de <em>Época</em>, nº 55, 7 de junho de 1999") + p("Com base nas informações apresentadas, pode-se afirmar que:"),
  figs(("q17", "Quatro calendários para a mesma data. Ocidental (gregoriano): 1º de janeiro de 2000, baseado no ciclo solar, tendo como referência o nascimento de Cristo. Islâmico: 24 de Ramadã de 1378, de base lunar, iniciado com a fuga de Maomé de Meca, em 622 d.C. Judaico: 23 de Tevet de 5760, calendário lunar a partir da criação do mundo conforme a Bíblia. Chinês: 7º dia do 12º mês do ano do coelho, calendário lunar iniciado em 2697 a.C., ano do patriarca chinês Huangti.")),
  ["calendários", "tempo histórico"])

X(18, "L", "Literatura", "Modernismo", "<p>“Precisa-se gentes”, com o verbo no singular e “gente” no plural, é uma construção da fala popular, contrária à norma culta (“precisa-se de gente”). É assim que Mário de Andrade imita a língua “brasileira”. Alternativa <strong>E</strong>.</p><p>As palavras de A, a pontuação (B) e a repetição de “bastante” (C) não são marcas específicas da linguagem popular.</p>",
  ap("“Precisa-se nacionais sem nacionalismo, (...) movidos pelo presente mas estalando naquele cio racial que só as tradições maduram! (...). Precisa-se gentes com bastante meiguice no sentimento, bastante força na peitaria, bastante paciência no entusiasmo e sobretudo, oh! sobretudo bastante vergonha na cara! (...) Enfim: precisa-se brasileiros! Assim está escrito no anúncio vistoso de cores desesperadas pintado sobre o corpo do nosso Brasil, camaradas.”")
  + fonte("(Jornal <em>A Noite</em>, São Paulo, 18/12/1925 <em>apud</em> LOPES, Telê Porto Ancona. <em>Mário de Andrade: ramais e caminhos</em>. São Paulo: Duas Cidades, 1972)")
  + p("No trecho acima, Mário de Andrade dá forma a um dos itens do ideário modernista, que é o de firmar a feição de uma língua mais autêntica, “brasileira”, ao expressar-se numa variante de linguagem popular identificada pela (o):"),
  tags=["Mário de Andrade", "variação linguística"],
  alts=A5("escolha de palavras como <em>cio</em>, <em>peitaria</em>, <em>vergonha</em>.", "emprego da pontuação.", "repetição do adjetivo <em>bastante</em>.", "concordância empregada em <em>Assim está escrito</em>.", "escolha de construção do tipo <em>precisa-se gentes</em>."))

X(19, "N", "Física", "Eclipse", "<p>O cone escuro da sombra da Lua atinge o ponto III, e a penumbra se estende de I a V. Quanto mais perto de III, mais o Sol aparece encoberto: a primeira foto, com só um crescente fino visível, é de III. Pontos de lados opostos do eixo da sombra veem a Lua cobrir lados opostos do disco solar: as outras duas fotos têm a parte escura em lados contrários, e correspondem a V (abaixo do eixo) e II (acima dele). Alternativa <strong>A</strong>.</p><p>Nas outras opções, pelo menos uma foto teria a parte encoberta do lado errado ou o ponto ficaria fora da sombra.</p>",
  p("A figura abaixo mostra um eclipse solar no instante em que é fotografado em cinco diferentes pontos do planeta.") + "[[fig:1]]" + p("Três dessas fotografias estão reproduzidas abaixo.") + "[[fig:2]]"
  + p("As fotos poderiam corresponder, respectivamente, aos pontos:"),
  figs(("q19a", "Esquema do eclipse: o Sol à direita, a Lua entre ele e a Terra, e a sombra da Lua, em cone, atingindo a superfície da Terra; na Terra estão marcados os pontos I, II, III, IV e V ao longo da borda voltada para o Sol."),
       ("q19b", "Três fotos do Sol eclipsado: na primeira, resta só um crescente fino; na segunda, cerca de metade do disco aparece; na terceira, um crescente largo, com pequena parte encoberta.")),
  ["eclipse solar", "sombra e penumbra"])

X(20, "L", "Literatura", "Modernismo", "<p>O poeta rejeita o lirismo “comedido”, “bem comportado”, preso às regras (“Abaixo os puristas”), e quer o lirismo dos loucos, dos bêbedos, dos clowns: “Não quero mais saber do lirismo que não é libertação”. É a proposta de um novo lirismo, livre. Alternativa <strong>E</strong>.</p><p>Ele não critica o lirismo louco (A) nem todo lirismo (B), e não propõe voltar a estéticas antigas (C, D).</p>",
  p("“Poética”, de Manuel Bandeira, é quase um manifesto do movimento modernista brasileiro de 1922. No poema, o autor elabora críticas e propostas que representam o pensamento estético predominante na época.") + "[[fig:1]]"
  + p("Com base na leitura do poema, podemos afirmar corretamente que o poeta:"),
  figs(("q20", "Trecho do poema “Poética”, de Manuel Bandeira: o poeta diz estar farto do lirismo comedido, bem comportado, de funcionário público, e do lirismo que consulta o dicionário; grita “abaixo os puristas”; diz querer o lirismo dos loucos, dos bêbedos e dos palhaços de Shakespeare; e termina recusando o lirismo que não é libertação.")),
  ["Manuel Bandeira", "Poética"])

X(21, "H", "Geografia", "Demografia", "<p>A população cresce quando entram mais pessoas do que saem. Entram os nascimentos e os imigrantes; saem as mortes e os emigrantes. Crescimento positivo significa N + I > M + E. Alternativa <strong>B</strong>.</p><p>C troca imigrantes por emigrantes; A e D indicariam diminuição da população.</p>",
  p("Ao longo do século XX, a taxa de variação na população do Brasil foi sempre positiva (crescimento). Essa taxa leva em consideração o número de nascimentos (N), o número de mortes (M), o de emigrantes (E) e o de imigrantes (I) por unidade de tempo.", "É correto afirmar que, no século XX:"),
  tags=["crescimento populacional"])

X(22, "N", "Biologia", "Ciclo da água", "<p>No gráfico, a área agrícola tem o pico de fluxo mais alto e mais rápido: quase toda a chuva escorre logo para o rio. Na floresta natural, o pico é baixo e tardio, porque a vegetação retém (intercepta) parte da água e retarda o escoamento. A interceptação é maior no ambiente natural preservado. Alternativa <strong>A</strong>.</p>",
  p("O gráfico abaixo representa o fluxo (quantidade de água em movimento) de um rio, em três regiões distintas, após certo tempo de chuva.") + "[[fig:1]]"
  + p("Comparando-se, nas três regiões, a interceptação da água da chuva pela cobertura vegetal, é correto afirmar que tal interceptação:"),
  figs(("q22", "Gráfico do fluxo fluvial em função do tempo depois que a chuva começa (0 a 60 minutos): a curva da área agrícola tem pico alto e estreito por volta de 12 minutos; a da floresta regenerada, pico médio por volta de 20 minutos; a da floresta natural, pico baixo e largo por volta de 33 minutos.")),
  ["interceptação", "escoamento superficial"])

X(23, "H", "Geografia", "Hidrelétricas", "<p>A represa inunda grandes áreas, destrói hábitats e altera o ambiente do rio, afetando a fauna e a flora. Alternativa <strong>D</strong>.</p><p>Usinas hidrelétricas não queimam combustível, então não causam chuva ácida nem poluição atmosférica relevante (A, B, E), e não elevam o nível dos oceanos.</p>",
  p("No ciclo da água, usado para produzir eletricidade, a água de lagos e oceanos, irradiada pelo Sol, evapora-se dando origem a nuvens e se precipita como chuva. É então represada, corre de alto a baixo e move turbinas de uma usina, acionando geradores. A eletricidade produzida é transmitida através de cabos e fios e é utilizada em motores e outros aparelhos elétricos. Assim, para que o ciclo seja aproveitado na geração de energia elétrica, constrói-se uma barragem para represar a água.",
    "Entre os possíveis impactos ambientais causados por essa construção, devem ser destacados:"),
  tags=["usina hidrelétrica", "impacto ambiental"])

X(24, "H", "Geografia", "Movimento aparente do Sol", "<p>Lisboa fica ao norte do Trópico de Câncer: o Sol do meio-dia está sempre ao sul, e janelas voltadas para o norte quase não recebem sol. Curitiba fica ao sul do Trópico de Capricórnio: o Sol está sempre ao norte, e janelas voltadas para o sul ficam sem sol. As janelas não devem estar voltadas para norte e sul, respectivamente. Alternativa <strong>A</strong>.</p>",
  p("“Casa que não entra sol, entra médico.” Esse antigo ditado reforça a importância de, ao construirmos casas, darmos orientações adequadas aos dormitórios, de forma a garantir o máximo conforto térmico e salubridade.",
    "Assim, confrontando casas construídas em Lisboa (ao norte do Trópico de Câncer) e em Curitiba (ao sul do Trópico de Capricórnio), para <strong>garantir a necessária luz do sol</strong>, as janelas dos quartos <strong>não</strong> devem estar voltadas, respectivamente, para os pontos cardeais:"),
  tags=["trópicos", "insolação"])

X(25, "M", "Matemática", "Juros compostos", "<p>Com juros de 2% ao mês: depois de 1 mês, 20.400; de 2 meses, 20.808; de 3 meses, 21.224,16. Em três meses João já tem o valor do carro e sobram cerca de R$ 224, aproximadamente R$ 225. Alternativa <strong>C</strong>.</p>",
  p("João deseja comprar um carro cujo preço à vista, com todos os descontos possíveis, é de R$ 21.000,00, e esse valor não será reajustado nos próximos meses.", "Ele tem R$ 20.000,00, que podem ser aplicados a uma taxa de juros compostos de 2% ao mês, e escolhe deixar todo o seu dinheiro aplicado até que o montante atinja o valor do carro.", "Para ter o carro, João deverá esperar:"),
  tags=["juros compostos"])

X(26, "H", "Geografia", "Regiões brasileiras", "<p>W tem todas as taxas abaixo das do Brasil: é o Norte. X tem a maior taxa de causas mal definidas (15), típica do acesso precário à saúde: o Nordeste. Y tem as maiores taxas de câncer e de doenças respiratórias, ligadas à maior esperança de vida e à poluição: o Sul. Z tem a maior taxa de causas externas (9): o Sudeste, com mais trânsito e violência urbana. Sobra K para o Centro-Oeste. Alternativa <strong>C</strong>.</p>",
  p("A tabela abaixo apresenta <strong>algumas</strong> das principais causas de mortes no Brasil, distribuídas por região.")
  + tabela(["Taxa por 10.000 habitantes", "Brasil", "K", "X", "W", "Y", "Z"],
           [["Causas mal definidas", "9", "5", "15", "8", "6", "6"], ["Causas externas", "7", "8", "5", "5", "7", "9"], ["Neoplasias (cânceres)", "6", "5", "3", "3", "9", "9"], ["Doenças respiratórias", "6", "4", "3", "2", "8", "7"]])
  + fonte("Fonte: Ministério da Saúde, 1996")
  + p("São conhecidas ainda as seguintes informações sobre as causas de óbitos:")
  + "<ul><li>A dificuldade na obtenção de informações, a falta de notificação e o acesso precário aos serviços de saúde são fatores relevantes na contabilização dos óbitos por causas mal definidas.</li><li>O aumento da esperança de vida faz com que haja cada vez mais pessoas com maiores chances de desenvolver algum tipo de câncer.</li><li>As mortes por doenças do aparelho respiratório estão estreitamente associadas à poluição nos grandes centros urbanos.</li><li>Os acidentes de trânsito e os assassinatos representam a quase totalidade das mortes por causas externas.</li><li>A região Norte é a única que apresenta todas as taxas por 10.000 habitantes abaixo da taxa média brasileira.</li></ul>"
  + p("Levando em consideração essas informações e o panorama social, econômico e ambiental do Brasil, pode-se concluir que as regiões K, X, W, Y e Z da tabela indicam, respectivamente, as regiões:"),
  tags=["causas de morte", "leitura de tabela"])

X(27, "N", "Biologia", "Origem da vida", "<p>No gráfico, a vida aparece há cerca de 3,1 bilhões de anos, quando a quantidade de oxigênio na atmosfera ainda era praticamente zero. O oxigênio só começa a subir depois do início da fotossíntese. Alternativa <strong>A</strong>.</p><p>O teor de oxigênio variou bastante depois da fotossíntese (C, D) e ainda subia quando surgiram os primeiros vertebrados terrestres (E).</p>",
  p("O gráfico abaixo representa a evolução da quantidade de oxigênio na atmosfera no curso dos tempos geológicos. O número 100 sugere a quantidade atual de oxigênio na atmosfera, e os demais valores indicam diferentes porcentagens dessa quantidade.") + "[[fig:1]]"
  + p("De acordo com o gráfico é correto afirmar que:"),
  figs(("q27", "Gráfico do oxigênio na atmosfera (em % da quantidade atual, escala logarítmica de 0 a 100) em função do tempo, de −4 a 0 bilhões de anos. A curva fica em zero na atmosfera primitiva e no aparecimento da vida (−3,1); sobe devagar depois do começo da fotossíntese (−2,7), durante a fase de atmosfera semelhante à de Marte; chega a cerca de 1% por volta de −1,6, quando se forma o anteparo de ozônio; sobe rápido depois da primeira célula eucarionte (cerca de −1) e do Pré-cambriano, atinge cerca de 100 na época dos primeiros vertebrados e da conquista da terra, e oscila perto desse valor nos períodos mais recentes.")),
  ["oxigênio atmosférico", "fotossíntese"], alts=dict(D[27], A="as primeiras formas de vida surgiram na ausência de O<sub>2</sub>."))

X(28, "H", "Geografia", "Migração", "<p>Os mapas das décadas de 50 e 60 mostram grandes fluxos do Nordeste para o Sudeste. Os migrantes nordestinos, em geral trabalhadores rurais, tornaram-se operários na indústria de São Paulo, então em expansão: mudaram de lugar e de condição social. Alternativa <strong>A</strong>.</p>",
  p("Os fluxos migratórios humanos, representados nos mapas abaixo, mais do que um deslocamento espacial podem significar uma mudança de condição social.") + "[[fig:1]]"
  + fonte("Fonte: Adaptado de SANTOS, Regina Bega. <em>Migrações no Brasil</em>. São Paulo: Scipione, 1994.") + p("Analisando-se os mapas, pode-se afirmar que essa mudança ocorreu com:"),
  figs(("q28", "Três mapas do Brasil com setas de migração. Décadas de 50 e de 60: setas grossas do Nordeste para o Sudeste. Décadas de 60 e de 70: setas do Nordeste e do Sul para o Centro-Oeste e o Sudeste. Décadas de 70 e de 80: setas do Sul, do Nordeste e do Sudeste para o Centro-Oeste e a Amazônia.")),
  ["migração nordestina", "industrialização"])

X(29, "H", "História", "Segundo Reinado", "<p>João, o sineiro, repica pela guerra, pelo ventre livre, pela abolição e pela República, e “repicaria pelo Império, se o Império retornasse”. Ele toca os sinos em qualquer acontecimento marcante, por ofício e costume, e não por convicção. Alternativa <strong>D</strong>.</p>",
  p("O texto abaixo foi extraído de uma crônica de Machado de Assis e refere-se ao trabalho de um escravo.")
  + ap("“Um dia começou a guerra do Paraguai e durou cinco anos, João repicava e dobrava, dobrava e repicava pelos mortos e pelas vitórias. Quando se decretou o ventre livre dos escravos, João é que repicou. Quando se fez a abolição completa, quem repicou foi João. Um dia proclamou-se a República. João repicou por ela, repicaria pelo Império, se o Império retornasse.”")
  + fonte("(ASSIS, Machado de. Crônica sobre a morte do escravo João, 1897)") + p("A leitura do texto permite afirmar que o sineiro João:"),
  tags=["Machado de Assis", "abolição"])

X(30, "N", "Física", "Condução térmica", "<p>Depois de muito tempo no refrigerador, a garrafa e a lata estão à mesma temperatura. A lata parece mais fria porque o alumínio conduz calor muito melhor que o vidro e retira calor da mão mais depressa. Alternativa <strong>D</strong>.</p><p>E inverte a comparação: o vidro é pior condutor que o alumínio.</p>",
  p("Uma garrafa de vidro e uma lata de alumínio, cada uma contendo 330 mL de refrigerante, são mantidas em um refrigerador pelo mesmo longo período de tempo. Ao retirá-las do refrigerador com as mãos desprotegidas, tem-se a sensação de que a lata está mais fria que a garrafa. É correto afirmar que:"),
  tags=["condutividade térmica", "sensação térmica"])

X(31, "H", "Geografia", "Globalização", "<p>O quinto mais rico concentra 86% do PIB, 82% das exportações e 93,3% das conexões à Internet, e a distância de renda entre ricos e pobres passou de 30 para 1 a 74 para 1. O cenário é de concentração crescente de renda, recursos e riqueza. Alternativa <strong>D</strong>.</p>",
  p("Em 1999, o Programa das Nações Unidas para o Desenvolvimento elaborou o “Relatório do Desenvolvimento Humano”, do qual foi extraído o trecho abaixo.")
  + ap("Nos últimos anos da década de 90, o quinto da população mundial que vive nos países de renda mais elevada tinha:")
  + "<ul><li>86% do PIB mundial, enquanto o quinto de menor renda, apenas 1%;</li><li>82% das exportações mundiais, enquanto o quinto de menor renda, apenas 1%;</li><li>74% das linhas telefônicas mundiais, enquanto o quinto de menor renda, apenas 1,5%;</li><li>93,3% das conexões com a Internet, enquanto o quinto de menor renda, apenas 0,2%.</li></ul>"
  + ap("A distância da renda do quinto da população mundial que vive nos países mais pobres - que era de 30 para 1, em 1960 — passou para 60 para 1, em 1990, e chegou a 74 para 1, em 1997.")
  + p("De acordo com esse trecho do relatório, o cenário do desenvolvimento humano mundial, nas últimas décadas, foi caracterizado pela:"),
  tags=["desigualdade", "concentração de renda"], alts=dict(D[31], E="distribuição eqüitativa dos resultados das inovações tecnológicas."))

LEITE = (tit("Texto para as questões 32 e 33.") + p("O autor do texto abaixo critica, ainda que em linguagem metafórica, a sociedade contemporânea em relação aos seus hábitos alimentares.")
  + ap("“Vocês que têm mais de 15 anos, se lembram quando a gente comprava leite em garrafa, na leiteria da esquina? (...) Mas vocês não se lembram de nada, pô! Vai ver nem sabem o que é vaca. Nem o que é leite. Estou falando isso porque agora mesmo peguei um pacote de leite – leite em pacote, imagina, Tereza! – na porta dos fundos e estava escrito que é pasterizado, ou pasteurizado, sei lá, tem vitamina, é garantido pela embromatologia, foi enriquecido e o escambau.",
       "Será que isso é mesmo leite? No dicionário diz que leite é outra coisa: ‘Líquido branco, contendo água, proteína, açúcar e sais minerais’. Um alimento pra ninguém botar defeito. O ser humano o usa há mais de 5.000 anos. É o único alimento só alimento. A carne serve pro animal andar, a fruta serve pra fazer outra fruta, o ovo serve pra fazer outra galinha (...) O leite é só leite. Ou toma ou bota fora.",
       "Esse aqui examinando bem, é só pra botar fora. Tem chumbo, tem benzina, tem mais água do que leite, tem serragem, sou capaz de jurar que nem vaca tem por trás desse negócio.",
       "Depois o pessoal ainda acha estranho que os meninos não gostem de leite. Mas, como não gostam? Não gostam como? Nunca tomaram! Múúúúúúú!”")
  + fonte("(FERNANDES, Millôr. <em>O Estado de S. Paulo</em>, 22 de agosto de 1999)"))
X(32, "L", "Língua Portuguesa", "Interpretação de texto", "<p>O autor ironiza o leite industrializado, cheio de aditivos e “garantias”, a ponto de duvidar que ainda seja leite: as pessoas perderam a referência do alimento natural e não sabem mais julgar sua qualidade (“Nunca tomaram!”). Alternativa <strong>C</strong>.</p><p>Ele não fala da economia do gado (A) nem de queda na produção (B).</p>",
  LEITE + p("A crítica do autor é dirigida:"), tags=["Millôr Fernandes", "crônica"])
X(33, "L", "Língua Portuguesa", "Formação de palavras", "<p>“Embromatologia” mistura “embromação” (enganação) com “bromatologia”, o estudo dos alimentos. A palavra inventada sugere que a tal garantia científica do leite é uma enganação. Alternativa <strong>B</strong>.</p><p>Lactologia (C) não é o estudo das embalagens, e a palavra não é termo científico (A, D).</p>",
  LEITE + p("A palavra <strong><em>embromatologia</em></strong> usada pelo autor é:"), tags=["neologismo", "Millôr Fernandes"])

X(34, "N", "Química", "Poluição do ar", "<p>I é plausível: a concentração de NO cai enquanto a de NO<sub>2</sub> sobe, pela oxidação de NO em NO<sub>2</sub>. II também: o CO tem picos nos horários de maior tráfego. III é falsa: os veículos emitem óxidos de nitrogênio sempre que circulam. IV é falsa: o ozônio da baixa atmosfera é formado ali mesmo, por reações com luz solar, e não vem da estratosfera. Alternativa <strong>A</strong>.</p>",
  p("O gráfico abaixo refere-se às variações das concentrações de poluentes na atmosfera, no decorrer de um dia útil, em um grande centro urbano.") + "[[fig:1]]"
  + fonte("(Adaptado de NOVAIS, Vera. <em>Ozônio: aliado ou inimigo</em>. São Paulo: Scipione, 1998)") + p("As seguintes explicações foram dadas para essas variações:")
  + I4("A concentração de NO diminui, e a de NO<sub>2</sub> aumenta em razão da conversão de NO em NO<sub>2</sub>.", "A concentração de monóxido de carbono no ar está ligada à maior ou à menor intensidade de tráfego.",
       "Os veículos emitem óxidos de nitrogênio apenas nos horários de pico de tráfego do período da manhã.", "Nos horários de maior insolação, parte do ozônio da estratosfera difunde-se para camadas mais baixas da atmosfera.")
  + p("Dessas explicações, são plausíveis somente:"),
  figs(("q34", "Gráfico da concentração de poluentes ao longo do dia (0 a 24 horas). NO tem pico perto das 7h; NO2, pico perto das 9h; O3, pico perto das 12h; CO tem um pico menor perto das 8h e um pico maior perto das 18h–19h.")),
  ["poluentes atmosféricos", "ozônio"])

X(35, "H", "História", "Política econômica", "<p>O primeiro texto defende a integração regional como forma de inserção no mundo globalizado; o segundo descreve a política de substituição de importações da era Vargas, que estimulou a produção nacional diante da crise e do encarecimento dos importados. São políticas diferentes. Alternativa <strong>C</strong>.</p><p>Só a política de Vargas era protecionista (B), e o segundo texto não fala de integração regional (D).</p>",
  p("Os textos abaixo relacionam-se a momentos distintos da nossa história.")
  + ap("“A integração regional é um instrumento fundamental para que um número cada vez maior de países possa melhorar a sua inserção num mundo globalizado, já que eleva o seu nível de competitividade, aumenta as trocas comerciais, permite o aumento da produtividade, cria condições para um maior crescimento econômico e favorece o aprofundamento dos processos democráticos. A integração regional e a globalização surgem assim como processos complementares e vantajosos.”")
  + fonte("(Declaração de Porto, VIII Cimeira Ibero-Americana, Porto, Portugal, 17 e 18 de outubro de 1998)")
  + ap("“Um considerável número de mercadorias passou a ser produzido no Brasil, substituindo o que não era possível ou era muito caro importar. Foi assim que a crise econômica mundial e o encarecimento das importações levaram o governo Vargas a criar as bases para o crescimento industrial brasileiro.”")
  + fonte("(POMAR, Wladimir. <em>Era Vargas – a modernização conservadora</em>)") + p("É correto afirmar que as políticas econômicas mencionadas nos textos são:"),
  tags=["substituição de importações", "integração regional"])

X(36, "N", "Biologia", "Ecologia", "<p>O esquema mostra só os lugares onde cada ave se alimenta. Aves que usam o mesmo local só competem se disputarem o mesmo recurso; sem saber o que cada uma come, não dá para concluir se há competição. Alternativa <strong>E</strong>.</p>",
  p("O esquema abaixo representa os diversos meios em que se alimentam aves, de diferentes espécies, que fazem ninho na mesma região.") + "[[fig:1]]"
  + p("Com base no esquema, uma classe de alunos procurou identificar a possível existência de competição alimentar entre essas aves e concluiu que:"),
  figs(("q36", "Esquema com quatro tipos de aves, cada um numa linha, e setas que partem do ninho, perto do mar, até os ambientes onde se alimentam: terreno seco ou cultura, arrozais, pântanos, estepe salgada, charcos pouco salgados, charcos salgados, ilhotas de nidificação, dunas e praias, e mar. A ave do tipo 3 vai a quase todos os ambientes; as outras vão a alguns deles, com ambientes em comum.")),
  ["competição", "nicho ecológico"], alts=dict(D[36], E="não se pode afirmar se há competição entre as aves que se alimentam em uma mesma região sem conhecer os tipos de alimento que consomem."))

FERRO = (tit("Texto para as questões 37 e 38.") + p("O ferro pode ser obtido a partir da hematita, minério rico em óxido de ferro, pela reação com carvão e oxigênio. A tabela a seguir apresenta dados da análise de minério de ferro (hematita) obtido de várias regiões da Serra de Carajás.")
  + tabela(["Minério da região", "Teor de enxofre (S) / % em massa", "Teor de ferro (Fe) / % em massa", "Teor de sílica (SiO<sub>2</sub>) / % em massa"], [["1", "0,019", "63,5", "0,97"], ["2", "0,020", "68,1", "0,47"], ["3", "0,003", "67,6", "0,61"]])
  + fonte("Fonte: ABREU, S. F. <em>Recursos minerais do Brasil</em>, vol. 2. São Paulo: Edusp, 1973"))
X(37, "N", "Química", "Minérios", "<p>O SO<sub>2</sub> vem do enxofre do minério. O minério 3 tem muito menos enxofre (0,003%, cerca de 6 vezes menos que os outros) e quase tanto ferro quanto o melhor (67,6% contra 68,1%). É o mais conveniente. Alternativa <strong>C</strong>.</p>",
  FERRO + p("No processo de produção do ferro, dependendo do minério utilizado, forma-se mais ou menos SO<sub>2</sub>, um gás que contribui para o aumento da acidez da chuva. Considerando esse impacto ambiental e a quantidade de ferro produzida, pode-se afirmar que seria mais conveniente o processamento do minério da(s) região(ões):"),
  tags=["dióxido de enxofre", "chuva ácida"])
X(38, "N", "Química", "Estequiometria", "<p>200 t de minério da região 1 têm 0,97% de sílica: 1,94 t. Como 60 g de sílica reagem com 100 g de calcário, 1,94 t × 100/60 ≈ 3,2 t. Alternativa <strong>B</strong>.</p><p>1,9 (A) é a massa de sílica, e não a de calcário.</p>",
  FERRO + p("No processo de produção do ferro, a sílica é removida do minério por reação com calcário (CaCO<sub>3</sub>). Sabe-se, teoricamente (cálculo estequiométrico), que são necessários 100 g de calcário para reagir com 60 g de sílica.", "Dessa forma, pode-se prever que, para a remoção de toda a sílica presente em 200 toneladas do minério na região 1, a massa de calcário necessária é, aproximadamente, em toneladas, igual a:"),
  tags=["proporção de massas", "porcentagem em massa"], alts=dict(D[38], E="8,0."))

APOSTA = (tit("Texto para as questões 39 e 40.") + p("Um apostador tem três opções para participar de certa modalidade de jogo, que consiste no sorteio aleatório de um número dentre dez.")
  + "<ul><li><strong>1ª opção:</strong> comprar três números para um único sorteio.</li><li><strong>2ª opção:</strong> comprar dois números para um sorteio e um número para um segundo sorteio.</li><li><strong>3ª opção:</strong> comprar um número para cada sorteio, num total de três sorteios.</li></ul>")
X(39, "M", "Matemática", "Probabilidade", "<p>X = 3/10 = 0,30. Y = 1 − P(não ganhar nenhum) = 1 − 0,8 × 0,9 = 0,28. Z = 1 − 0,9³ = 1 − 0,729 = 0,271. Logo X > Y > Z. Alternativa <strong>E</strong>.</p><p>Espalhar os números em vários sorteios abre a chance de ganhar mais de uma vez, mas diminui a de ganhar pelo menos uma.</p>",
  APOSTA + p("Se X, Y, Z representam as probabilidades de o apostador <strong>ganhar algum prêmio</strong>, escolhendo, respectivamente, a 1ª, a 2ª ou a 3ª opções, é correto afirmar que:"),
  tags=["probabilidade", "evento complementar"])
X(40, "M", "Matemática", "Probabilidade", "<p>Na 2ª opção, a chance de perder o primeiro sorteio (com dois números) é 8/10, e a de perder o segundo (com um número) é 9/10. Como os sorteios são independentes, a probabilidade de não ganhar nenhum é 0,8 × 0,9 = 0,72 = 72%. Alternativa <strong>C</strong>.</p>",
  APOSTA + p("Escolhendo a 2ª opção, a probabilidade de o apostador <strong>não ganhar</strong> em qualquer dos sorteios é igual a:"),
  tags=["probabilidade", "eventos independentes"], alts=dict(D[40], E="65%."))

BOATO = (tit("Texto para as questões 41 e 42.") + p("Um boato tem um público-alvo e alastra-se com determinada rapidez. Em geral, essa rapidez é diretamente proporcional ao número de pessoas desse público que conhecem o boato e diretamente proporcional também ao número de pessoas que não o conhecem. Em outras palavras, sendo R a rapidez de propagação, P o público-alvo e x o número de pessoas que conhecem o boato, tem-se:", "R(x) = k·x·(P − x), onde k é uma constante positiva característica do boato."))
X(41, "M", "Matemática", "Função quadrática", "<p>R(x) = kx(P − x) = −kx² + kPx é uma função do 2º grau com coeficiente de x² negativo (k > 0): o gráfico é uma parábola com a concavidade para baixo, que corta o eixo x em 0 e em P. Alternativa <strong>E</strong>.</p><p>C seria uma parábola com a concavidade para cima.</p>",
  BOATO + p("O gráfico cartesiano que melhor representa a função R(x), para x real, é:"),
  figs(("q41a", "Gráfico em degraus: segmentos horizontais cada vez mais altos."), ("q41b", "Gráfico: reta horizontal."), ("q41c", "Gráfico: parábola com a concavidade para cima, tocando o eixo x."),
       ("q41d", "Gráfico: reta decrescente."), ("q41e", "Gráfico: parábola com a concavidade para baixo, partindo da origem e voltando ao eixo x.")),
  ["parábola", "função do 2º grau"], alts=ALT(1))
X(42, "M", "Matemática", "Função quadrática", "<p>A parábola R(x) = kx(P − x) tem raízes 0 e P, e o vértice fica no ponto médio entre elas: x = P/2 = 44.000/2 = 22.000 pessoas. Alternativa <strong>B</strong>.</p><p>Faz sentido: no começo, poucos conhecem o boato; no fim, poucos ainda não o conhecem. A propagação é mais rápida quando metade do público já sabe.</p>",
  BOATO + p("Considerando o modelo acima descrito, se o público-alvo é de 44.000 pessoas, então a máxima rapidez de propagação ocorrerá quando o boato for conhecido por um número de pessoas igual a:"),
  tags=["vértice da parábola", "máximo"])

X(43, "M", "Matemática", "Geometria espacial", "<p>No cilindro deitado, a seção horizontal é mais larga no meio da altura e estreita perto do fundo e do topo. Perto do meio, um pequeno aumento da altura já acrescenta muito volume; perto das pontas, é preciso subir mais para somar o mesmo volume. As graduações ficam mais juntas no meio e mais espaçadas nas pontas, como na vara (A). Alternativa <strong>A</strong>.</p>",
  p("Uma empresa de transporte armazena seu combustível em um reservatório cilíndrico enterrado horizontalmente. Seu conteúdo é medido com uma vara graduada em vinte intervalos, de modo que a distância entre duas graduações consecutivas representa sempre o mesmo volume.") + "[[fig:1]]"
  + "[[fig:2]]" + p("A ilustração que melhor representa a distribuição das graduações na vara é:"),
  figs(("q43", "Cilindro deitado, com uma vara vertical atravessando-o pelo meio, do topo ao fundo."),
       ("q43v", "Cinco varas graduadas, de (A) a (E). Em (A), as marcas ficam mais juntas no meio e mais espaçadas perto das pontas. Em (B), mais juntas perto das pontas e mais espaçadas no meio. Em (C), igualmente espaçadas. Em (D), mais juntas em cima e mais espaçadas embaixo. Em (E), mais espaçadas em cima e mais juntas embaixo.")),
  ["cilindro", "volume"], alts=A5("Vara (A).", "Vara (B).", "Vara (C).", "Vara (D).", "Vara (E)."))

X(44, "M", "Matemática", "Proporcionalidade", "<p>O galpão tem 10 m × 11 m = 110 m². Tirando o hall (20 m²), sobram 90 m² para 90 + 60 + 120 = 270 fardos: 1/3 m² por fardo. O depósito III, com 120 fardos, tem 40 m². Com 10 m de comprimento, sua largura é 4 m. Alternativa <strong>D</strong>.</p>",
  p("Em uma empresa, existe um galpão que precisa ser dividido em três depósitos e um <em>hall</em> de entrada de 20 m², conforme a figura abaixo. Os depósitos I, II e III serão construídos para o armazenamento de, respectivamente, 90, 60 e 120 fardos de igual volume, e suas áreas devem ser proporcionais a essas capacidades.") + "[[fig:1]]"
  + p("A largura do depósito III dever ser, em metros, igual a:"),
  figs(("q44", "Planta retangular de 10 m por 11 m: à esquerda, o depósito I, de toda a altura; no meio, em cima, o hall de 20 m² e, embaixo, o depósito II; à direita, o depósito III, de toda a altura.")),
  ["área", "divisão proporcional"])

X(45, "H", "Geografia", "Relevo", "<p>O relevo resulta de forças internas (tectonismo, vulcanismo, movimentos do manto) e externas (chuva, vento, rios). Um “esguicho” de material do manto empurrando o planalto para cima é uma explicação plausível, porque considera os movimentos profundos do interior da Terra. Alternativa <strong>C</strong>.</p><p>O relevo se modifica continuamente (A), e as forças externas não explicam sozinhas um planalto tão alto (B).</p>",
  ap("“O continente africano há muito tempo desafia os geólogos porque toda a sua metade meridional, a que fica ao sul, ergue-se a mais de 1.000 metros sobre o nível do mar. (...) Uma equipe de pesquisadores apresentou uma solução desse desafio sugerindo a existência de um esguicho de lava subterrânea empurrando o planalto africano de baixo para cima.”")
  + fonte("(Adaptado de <em>Revista Superinteressante</em>. São Paulo: Abril, novembro de 1998, p. 12)")
  + p("Considerando a formação do relevo terrestre, é correto afirmar, com base no texto, que a solução proposta é:"),
  tags=["agentes internos do relevo"])

X(46, "L", "Literatura", "Intertextualidade", "<p>A charge “Demarcação das terras indígenas” mostra covas abertas: a única terra garantida ao índio seria a da sepultura. Em “Morte e Vida Severina”, João Cabral faz a mesma ironia com o lavrador pobre: a cova “é a parte que te cabe deste latifúndio”. Alternativa <strong>B</strong>.</p><p>Os outros textos falam da morte ou da terra, mas sem ligar a cova à falta de terra para quem trabalha nela.</p>",
  p("Em muitos jornais, encontramos charges, quadrinhos, ilustrações, inspirados nos fatos noticiados. Veja um exemplo:") + "[[fig:1]]" + fonte("<em>Jornal do Commercio</em>, 22/8/93")
  + p("O texto que se refere a uma situação semelhante à que inspirou a charge é:"),
  figs(("q46", "Charge de Miguel com o título “Demarcação das terras indígenas”: uma pá fincada na terra ao lado de várias covas retangulares abertas no chão."),
       ("q46a", "Quatro versos de Álvares de Azevedo: o eu lírico pede que o enterrem na floresta, sob uma cruz com a inscrição de que foi poeta, sonhou e amou na vida. Fonte: Poesias escolhidas."),
       ("q46b", "Oito versos de João Cabral de Melo Neto, de “Morte e Vida Severina”: a cova medida a palmos é a conta menor que o lavrador tirou em vida, de bom tamanho, a parte que lhe cabe deste latifúndio."),
       ("q46c", "Cinco versos de Mário Chamie, que jogam com as palavras medir, medida, medo, terra e lavra, falando do duro campo, muito cerco e várzea."),
       ("q46d", "Oito versos de Ferreira Gullar que anunciam o caso de Pedro João Boa-Morte, lavrador da Paraíba do Norte, que talvez tenha morte boa porque vida ele não tinha."),
       ("q46e", "Três versos de Machado de Assis: o eu lírico traz flores, restos arrancados da terra, para quem a morte separou dele.")),
  ["charge", "João Cabral de Melo Neto"], alts=ALT(2))

X(47, "N", "Biologia", "Lixo", "<p>O aterro sanitário cobre o lixo com terra e diminui o contato humano com ele (I). O depósito a céu aberto só tem a vantagem de ser barato (III). A incineração reduz muito o volume do lixo (IV). Alternativa <strong>B</strong>.</p><p>Nenhum dos três produz adubo (II); isso é feito na compostagem.</p>",
  p("Um dos grandes problemas das regiões urbanas é o acúmulo de lixo sólido e sua disposição. Há vários processos para a disposição do lixo, dentre eles o aterro sanitário, o depósito a céu aberto e a incineração. Cada um deles apresenta vantagens e desvantagens.", "Considere as seguintes vantagens de métodos de disposição do lixo:")
  + I4("diminuição do contato humano direto com o lixo;", "produção de adubo para agricultura;", "baixo custo operacional do processo;", "redução do volume de lixo.")
  + p("A relação correta entre cada um dos processos para a disposição do lixo e as vantagens apontadas é:"),
  tags=["aterro sanitário", "incineração"],
  alts=A5("Aterro sanitário: I. Depósito a céu aberto: II. Incineração: I.", "Aterro sanitário: I. Depósito a céu aberto: III. Incineração: IV.", "Aterro sanitário: II. Depósito a céu aberto: IV. Incineração: I.",
          "Aterro sanitário: II. Depósito a céu aberto: I. Incineração: IV.", "Aterro sanitário: III. Depósito a céu aberto: II. Incineração: I."))

FLUOR = (tit("Texto para as questões 48 e 49.")
  + ap("No Brasil, mais de 66 milhões de pessoas beneficiam-se hoje do abastecimento de água fluoretada, medida que vem reduzindo, em cerca de 50%, a incidência de cáries. Ocorre, entretanto, que profissionais da saúde muitas vezes prescrevem flúor oral ou complexos vitamínicos com flúor para crianças ou gestantes, levando à ingestão exagerada da substância. O mesmo ocorre com o uso abusivo de algumas marcas de água mineral que contêm flúor. O excesso de flúor - fluorose - nos dentes pode ocasionar desde efeitos estéticos até defeitos estruturais graves.",
       "Foram registrados casos de fluorose tanto em cidades com água fluoretada pelos poderes públicos como em outras, abastecidas por lençóis freáticos que naturalmente contêm flúor.")
  + fonte("(Adaptado da <em>Revista da Associação Paulista de Cirurgiões Dentistas - APCD</em>, vol. 53, nº 1, jan./fev. 1999)"))
X(48, "N", "Biologia", "Saúde bucal", "<p>I está de acordo com o texto: o flúor reduz as cáries, mas o excesso causa fluorose. III também: o texto cita vitaminas, flúor oral e água mineral como outras fontes. II não pode ser afirmada: o texto diz que os lençóis contêm flúor, mas não compara sua concentração com a da água tratada. Alternativa <strong>D</strong>.</p>",
  FLUOR + p("Com base nesse texto, são feitas as afirmações abaixo.")
  + I3("A fluoretação da água é importante para a manutenção do esmalte dentário, porém não pode ser excessiva.", "Os lençóis freáticos citados contêm compostos de flúor, em concentrações superiores às existentes na água tratada.", "As pessoas que adquiriram fluorose podem ter utilizado outras fontes de flúor além da água de abastecimento público, como, por exemplo, cremes dentais e vitaminas com flúor.")
  + p("Pode-se afirmar que, apenas:"), tags=["flúor", "fluorose"])
X(49, "N", "Química", "Concentração", "<p>Em uma hora (3.600 s), a Estação trata 30.000 × 3.600 = 108.000.000 L. Com no máximo 1,5 mg por litro: 1,5 × 108.000.000 = 162.000.000 mg = 162 kg. Alternativa <strong>E</strong>.</p><p>Quem esquece de converter a hora em 3.600 segundos encontra valores muito menores, como 1,5 kg (A) ou 4,5 kg (B).</p>",
  FLUOR + p("Determinada Estação trata cerca de 30.000 litros de água por segundo. Para evitar riscos de fluorose, a concentração máxima de fluoretos nessa água não deve exceder a cerca de 1,5 miligrama por litro de água.", "A quantidade máxima dessa espécie química que pode ser utilizada com segurança, no volume de água tratada em uma hora, nessa Estação, é:"),
  tags=["concentração em mg/L", "conversão de unidades"])

X(50, "N", "Química", "Álcool combustível", "<p>Pelo esquema, 1 tonelada de cana produz 70 litros de etanol. Para 12 bilhões de litros: 12 × 10<sup>9</sup> ÷ 70 ≈ 1,7 × 10<sup>8</sup> toneladas. Alternativa <strong>A</strong>.</p><p>Os outros dados do esquema (bagaço, melaço, vinhoto) não entram na conta: só importa a relação entre a cana e o etanol.</p>",
  p("O esquema ilustra o processo de obtenção do álcool etílico a partir da cana-de-açúcar.") + "[[fig:1]]"
  + p("Em 1996, foram produzidos no Brasil 12 bilhões de litros de álcool. A quantidade de cana-de-açúcar, em toneladas, que teve de ser colhida para esse fim foi aproximadamente"),
  figs(("q50", "Fluxograma: cana-de-açúcar (1 tonelada) passa pela trituração, que gera bagaço (250 kg) e garapa; a garapa passa por concentração e cristalização, gerando açúcar escuro e melaço (250 kg); o açúcar escuro é refinado em açúcar comum (sacarose); o melaço passa por fermentação, gerando mosto fermentado e vinhoto (910 litros); o mosto passa por destilação, gerando etanol (70 litros) e óleo fúsel e resíduo.")),
  ["etanol", "notação científica"],
  alts=A5("1,7 × 10<sup>8</sup>.", "1,2 × 10<sup>9</sup>.", "1,7 × 10<sup>9</sup>.", "1,2 × 10<sup>10</sup>.", "7,0 × 10<sup>10</sup>."))

X(51, "H", "Geografia", "Petróleo", "<p>Pelo texto, o petróleo se formou de restos de vida aquática nos oceanos primitivos ao longo de muito tempo: é não renovável na escala humana e é encontrado em áreas submarinas e em áreas continentais que já foram mar. Alternativa <strong>E</strong>.</p><p>Há exploração em terra também (B), e o petróleo polui apesar da origem natural (C).</p>",
  p("Para compreender o processo de exploração e o consumo dos recursos petrolíferos, é fundamental conhecer a gênese e o processo de formação do petróleo descritos no texto abaixo.")
  + ap("“O petróleo é um combustível fóssil, originado provavelmente de restos de vida aquática acumulados no fundo dos oceanos primitivos e cobertos por sedimentos. O tempo e a pressão do sedimento sobre o material depositado no fundo do mar transformaram esses restos em massas viscosas de coloração negra denominadas jazidas de petróleo.”")
  + fonte("(Adaptado de TUNDISI. <em>Usos de energia</em>. São Paulo: Atual Editora, 1991)") + p("As informações do texto permitem afirmar que:"),
  tags=["combustíveis fósseis"], alts=dict(D[51], E="o petróleo é um recurso não renovável a curto prazo, explorado em áreas continentais de origem marinha ou em áreas submarinas."))

LOCKE = (tit("Texto para as questões 52 e 53.") + p("O texto abaixo, de John Locke (1632-1704), revela algumas características de uma determinada corrente de pensamento.")
  + ap("“Se o homem no estado de natureza é tão livre, conforme dissemos, se é senhor absoluto da sua própria pessoa e posses, igual ao maior e a ninguém sujeito, por que abrirá ele mão dessa liberdade, por que abandonará o seu império e sujeitar-se-á ao domínio e controle de qualquer outro poder?",
       "Ao que é óbvio responder que, embora no estado de natureza tenha tal direito, a utilização do mesmo é muito incerta e está constantemente exposto à invasão de terceiros porque, sendo todos senhores tanto quanto ele, todo homem igual a ele e, na maior parte, pouco observadores da eqüidade e da justiça, o proveito da propriedade que possui nesse estado é muito inseguro e muito arriscado. Estas circunstâncias obrigam-no a abandonar uma condição que, embora livre, está cheia de temores e perigos constantes; e não é sem razão que procura de boa vontade juntar-se em sociedade com outros que estão já unidos, ou pretendem unir-se, para a mútua conservação da vida, da liberdade e dos bens a que chamo de propriedade.”")
  + fonte("(<em>Os Pensadores</em>. São Paulo: Nova Cultural, 1991)"))
X(52, "H", "Filosofia", "Contratualismo", "<p>Para Locke, as pessoas deixam o estado de natureza e formam a sociedade política para garantir “a mútua conservação da vida, da liberdade e dos bens”. O governo nasce de um acordo para proteger esses direitos. Alternativa <strong>D</strong>.</p><p>O governo não vem da natureza (A) nem pertence ao rei (B), e Locke se opõe ao absolutismo (C).</p>",
  LOCKE + p("Do ponto de vista político, podemos considerar o texto como uma tentativa de justificar:"), tags=["John Locke", "contrato social"])
X(53, "H", "Filosofia", "Liberalismo", "<p>A defesa da liberdade individual, da propriedade e de um governo criado para protegê-las é a base do liberalismo político, do qual Locke é um dos fundadores. Alternativa <strong>A</strong>.</p><p>Os socialismos (B, D) criticam a propriedade privada, e o anarquismo (E) rejeita o Estado.</p>",
  LOCKE + p("Analisando o texto, podemos concluir que se trata de um pensamento:"), tags=["liberalismo", "John Locke"], alts=dict(D[53], E="do anarquismo."))

REPOLHO = (tit("Texto para as questões 54 e 55.") + p("O suco extraído do repolho roxo pode ser utilizado como indicador do caráter ácido (pH entre 0 e 7) ou básico (pH entre 7 e 14) de diferentes soluções. Misturando-se um pouco de suco de repolho e da solução, a mistura passa a apresentar diferentes cores, segundo sua natureza ácida ou básica, de acordo com a escala abaixo.")
  + "[[fig:1]]" + p("Algumas soluções foram testadas com esse indicador, produzindo os seguintes resultados:")
  + tabela(["", "Material", "Cor"], [["I", "Amoníaco", "Verde"], ["II", "Leite de magnésia", "Azul"], ["III", "Vinagre", "Vermelho"], ["IV", "Leite de vaca", "Rosa"]]))
F_REP = figs(("q53", "Escala de cores do indicador de repolho roxo em função do pH: vermelho de 1 a 3; rosa de 4 a 6; roxo de 7 a 8; azul de 9 a 10; verde de 11 a 12; amarelo de 13 a 14."))
X(54, "N", "Química", "Indicadores", "<p>Pela escala, verde (pH 11–12) e azul (pH 9–10) indicam meio básico; vermelho (pH 1–3) e rosa (pH 4–6), meio ácido. Amoníaco e leite de magnésia são básicos; vinagre e leite de vaca, ácidos. Alternativa <strong>E</strong>.</p>",
  REPOLHO + p("De acordo com esses resultados, as soluções I, II, III e IV têm, respectivamente, caráter:"), F_REP, ["pH", "indicador ácido-base"])
X(55, "N", "Química", "Indicadores", "<p>Sucos de abacaxi e de limão são ácidos (o limão, bem mais). Na escala, as cores ácidas são o vermelho (pH 1–3) e o rosa (pH 4–6). Alternativa <strong>D</strong>.</p><p>Verde, azul e amarelo indicam meio básico, e roxo, meio próximo do neutro.</p>",
  REPOLHO + p("Utilizando-se o indicador citado em sucos de abacaxi e de limão, pode-se esperar como resultado as cores:"), F_REP, ["pH", "ácidos do cotidiano"],
  alts=A5("rosa ou amarelo.", "vermelho ou roxo.", "verde ou vermelho.", "rosa ou vermelho.", "roxo ou azul."))

X(56, "H", "Geografia", "Fim da URSS", "<p>Em 1991, com a desintegração da União Soviética, as repúblicas soviéticas declararam independência uma após a outra, e o Cazaquistão foi uma delas, em dezembro daquele ano. Era uma nova correção a fazer no mapa. Alternativa <strong>D</strong>.</p><p>O número de países aumentava (B), e a Alemanha tinha acabado de se reunificar (E).</p>",
  p("O quadrinho publicado na revista <em>Newsweek</em> (23/9/1991) ilustra o desespero dos cartógrafos para desenhar o novo mapa-múndi diante das constantes mudanças de fronteiras.") + "[[fig:1]]"
  + p("Levando em consideração o contexto da época em que a charge foi publicada, dentre as frases abaixo, a que melhor completa o texto da fala, propondo outra correção no mapa, é:"),
  figs(("q56", "Cartum: um homem, num escritório de cartografia cheio de mapas e de uma televisão, entrega uma folha a um cartógrafo atordoado, de mãos para o alto, e diz: “Outra correção, Peter...”.")),
  ["fim da União Soviética", "nova ordem mundial"])

X(57, "L", "Língua Portuguesa", "Colocação pronominal", "<p>Oswald mostra que o povo diz “Me dá um cigarro”, e Cegalla admite o pronome átono no início da frase na conversa familiar e na fala de personagens. Ambos relativizam a regra: ela vale para a escrita formal, mas não para todos os usos. Alternativa <strong>E</strong>.</p><p>O gramático não condena a regra (A) nem nega que haja regras (D).</p>",
  p("O uso do pronome átono no início das frases é destacado por um poeta e por um gramático nos textos abaixo.")
  + ap("<strong>Pronominais</strong>", "Dê-me um cigarro<br>Diz a gramática<br>Do professor e do aluno<br>E do mulato sabido", "Mas o bom negro e o bom branco<br>Da Nação Brasileira<br>Dizem todos os dias<br>Deixa disso camarada<br>Me dá um cigarro")
  + fonte("(ANDRADE, Oswald de. <em>Seleção de textos</em>. São Paulo: Nova Cultural, 1988)")
  + ap("“Iniciar a frase com pronome átono só é lícito na conversação familiar, despreocupada, ou na língua escrita quando se deseja reproduzir a fala dos personagens (...).”")
  + fonte("(CEGALLA, Domingos Paschoal. <em>Novíssima gramática da língua portuguesa</em>. São Paulo: Nacional, 1980)")
  + p("Comparando a explicação dada pelos autores sobre essa regra, pode-se afirmar que ambos:"),
  tags=["próclise", "Oswald de Andrade"])

X(58, "M", "Matemática", "Razão", "<p>O grupo de renda superior tem 5% da população e consome 10% da energia: 10/5 = 2 unidades por pessoa (em termos relativos). O grupo de renda inferior tem 50% da população e consome 30%: 30/50 = 0,6. A razão é 2/0,6 ≈ 3,3. Alternativa <strong>B</strong>.</p>",
  p("O Brasil, em 1997, com cerca de 160 × 10<sup>6</sup> habitantes, apresentou um consumo de energia da ordem de 250.000 TEP (tonelada equivalente de petróleo), proveniente de diversas fontes primárias.",
    "O grupo com renda familiar de mais de vinte salários mínimos representa 5% da população brasileira e utiliza cerca de 10% da energia total consumida no país.",
    "O grupo com renda familiar de até três salários mínimos representa 50% da população e consome 30% do total de energia.",
    "Com base nessas informações, pode-se concluir que o consumo médio de energia para um indivíduo do grupo de renda superior é <u>x vezes maior</u> do que para um indivíduo do grupo de renda inferior. O valor aproximado de x é:"),
  tags=["razão", "consumo per capita"], alts=A5("2,1.", "3,3.", "6,3.", "10,5.", "12,7."))

X(59, "L", "Língua Portuguesa", "Ironia", "<p>Garfield sugere ao dono, que quer pintar um quadro, que “corte uma orelha”, referência a Van Gogh, que cortou a própria orelha. Ele conhece a história e a usa com ironia. Alternativa <strong>D</strong>.</p>",
  p("As histórias em quadrinhos, por vezes, utilizam animais como personagens e a eles atribuem comportamento humano. O gato Garfield é exemplo desse fato.") + "[[fig:1]]"
  + fonte("Fonte: Caderno Vida e Arte, <em>Jornal do Povo</em>, Fortaleza")
  + p("Van Gogh, pintor holandês nascido em 1853, é um dos principais nomes da pintura mundial. É dele o quadro abaixo.") + "[[fig:2]]" + fonte("VAN GOGH. <em>Auto-retrato de orelha cortada</em>.")
  + p("O 3º quadrinho sugere que Garfield:"),
  figs(("q59", "Tira de Garfield, de Jim Davis, em três quadros: Jon, de boina, diz “Estou inspirado hoje!”; depois, com pincel e paleta, diz “Vou pintar uma pintura!”; no último, pergunta “Por onde começo?”, e Garfield responde: “Corte uma orelha”."),
       ("q59b", "Autorretrato de Van Gogh com a orelha enfaixada, usando gorro de pele e fumando cachimbo.")),
  ["Garfield", "Van Gogh"])

X(60, "H", "Geografia", "Curvas de nível", "<p>O parque industrial deve ficar em área plana, longe da vegetação, fora da cidade e perto das rodovias: a região I, onde as duas rodovias se cruzam. A torre de transmissão deve ficar no ponto mais alto, para ter alcance: a região E, junto ao topo do morro, onde as curvas de nível chegam a 40. Alternativa <strong>C</strong>.</p>",
  p("Um determinado município, representado na planta abaixo, dividido em regiões de A a I, com altitudes de terrenos indicadas por curvas de nível, precisa decidir pela localização das seguintes obras:")
  + "<ol><li>instalação de um parque industrial.</li><li>instalação de uma torre de transmissão e recepção.</li></ol>" + "[[fig:1]]"
  + p("Considerando impacto ambiental e adequação, as regiões onde deveriam ser, de preferência, instaladas <strong>indústrias e torre</strong>, são, respectivamente:"),
  figs(("q60", "Planta de um município dividida em nove regiões (A a I, em três linhas). Há manchas de vegetação em A, B, C, D, G e na borda de F; curvas de nível de 10, 20, 30 e 40 formam um morro cujo topo (40) fica entre B e E; um rio desce de A por D até H e outro vem de G; os dois seguem juntos para leste, por H e F; a cidade ocupa o centro do mapa, entre E, H e F; e duas rodovias, uma vinda de C e outra de H, se cruzam na região I, que é plana e sem vegetação. Escala 1:100.000 e seta do norte.")),
  ["curvas de nível", "planejamento urbano"], alts=A5("E e G.", "H e A.", "I e E.", "B e I.", "E e F."))

X(61, "H", "Geografia", "Recursos hídricos", "<p>A região III tem água poluída por esgotos domésticos e industriais (há indústrias e pouco tratamento de esgoto) e usa água para irrigação (há agricultura). Alternativa <strong>D</strong>.</p><p>A região I tem água pouco poluída, o que não combina com alta densidade (A). A região II tem poluição urbana e industrial forte, ao contrário de C. E E contradiz o lançamento de esgotos.</p>",
  p("Encontram-se descritas a seguir algumas das características das águas que servem três diferentes regiões.")
  + "<ul><li><strong>Região I</strong> - Qualidade da água pouco comprometida por cargas poluidoras, casos isolados de mananciais comprometidos por lançamento de esgotos; assoreamento de alguns mananciais.</li><li><strong>Região II</strong> - Qualidade comprometida por cargas poluidoras urbanas e industriais; área sujeita a inundações; exportação de carga poluidora para outras unidades hidrográficas.</li><li><strong>Região III</strong> - Qualidade comprometida por cargas poluidoras domésticas e industriais e por lançamento de esgotos; problemas isolados de inundação; uso da água para irrigação.</li></ul>"
  + p("De acordo com essas características, pode-se concluir que:"),
  tags=["poluição da água", "uso do solo"])

X(62, "N", "Biologia", "Diabetes", "<p>A insulina facilita a entrada da glicose nas células. Se há pouca insulina, a glicose não entra nas células e se acumula no sangue (hiperglicemia). Alternativa <strong>D</strong>.</p><p>A insulina é um hormônio, não uma enzima (A, B); o excesso de glicose vem da falta de insulina, e não do excesso (C, E).</p>",
  p("O metabolismo dos carboidratos é fundamental para o ser humano, pois a partir desses compostos orgânicos obtém-se grande parte da energia para as funções vitais. Por outro lado, desequilíbrios nesse processo podem provocar hiperglicemia ou diabetes.",
    "O caminho do açúcar no organismo inicia-se com a ingestão de carboidratos que, chegando ao intestino, sofrem a ação de enzimas, “quebrando-se” em moléculas menores (glicose, por exemplo) que serão absorvidas.",
    "A insulina, hormônio produzido no pâncreas, é responsável por facilitar a entrada da glicose nas células. Se uma pessoa produz pouca insulina, ou se sua ação está diminuída, dificilmente a glicose pode entrar na célula e ser consumida.",
    "Com base nessas informações, pode-se concluir que:"),
  tags=["insulina", "glicemia"])

X(63, "N", "Biologia", "Eutrofização", "<p>A partir de t<sub>3</sub>, o esgoto traz mais nutrientes, e a produção primária e a decomposição aumentam; os decompositores consomem oxigênio, que cai. A partir de t<sub>6</sub>, o oxigênio fica insuficiente e os peixes morrem. Alternativa <strong>D</strong>.</p><p>A decomposição continua (B), e a produção primária ainda estava alta quando os peixes começaram a morrer (C).</p>",
  p("Os esgotos domésticos constituem grande ameaça aos ecossistemas de lagos ou represas, pois deles decorrem graves desequilíbrios ambientais. Considere o gráfico abaixo, no qual no intervalo de tempo entre t<sub>1</sub> e t<sub>3</sub>, observou-se a estabilidade em ecossistema de lago, modificado a partir de t<sub>3</sub> pelo maior despejo de esgoto.") + "[[fig:1]]"
  + p("Assinale a interpretação que está de acordo com o gráfico."),
  figs(("q63", "Gráfico de t1 a t9 com quatro curvas: nutrientes, estáveis até t3 e depois subindo; produção primária, estável até t3, subindo até t6 e depois caindo um pouco; peixes, estáveis até t3, subindo até t6 e depois caindo; oxigênio, estável até t3 e depois caindo continuamente.")),
  ["eutrofização", "oxigênio dissolvido"],
  alts=A5("Entre t<sub>3</sub> e t<sub>6</sub>, a competição pelo oxigênio leva à multiplicação de peixes, bactérias e outros produtores.", "A partir de t<sub>3</sub>, a decomposição do esgoto é impossibilitada pela diminuição do oxigênio disponível.",
          "A partir de t<sub>6</sub>, a mortandade de peixes decorre da diminuição da população de produtores.", "A mortandade de peixes, a partir de t<sub>6</sub>, é devida à insuficiência de oxigênio na água.", "A partir de t<sub>3</sub>, a produção primária aumenta devido à diminuição dos consumidores."))

completar(Q, R)
