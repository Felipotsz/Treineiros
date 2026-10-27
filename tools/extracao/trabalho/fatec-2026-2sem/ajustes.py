# Ajustes da conferência humana: Vestibular FATEC 2º semestre de 2026 (exame de 28/06/2026)
# Texto conferido com a imagem de cada página. Tema implícito: futebol (Copa do Mundo de 2026).
# 60 questões; a prova tem 5 h no total, incluindo a redação (que fica fora do simulado).
# Matéria: a do gabarito oficial; nas "Multidisciplinar", a matéria principal + tag "multidisciplinar".
# Poema de Vinicius de Moraes (Q56-57) como imagem; o alt descreve sem transcrever.
# Gabarito: oficial (2SEM26), sem anuladas, conferido com resolução própria. Q6: o gabarito (C) só fecha
# contando proteínas e carboidratos, como o enunciado manda; a explicação diz isso.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import A, carregar, enun, tabela, colunas, completar, trecho

ID = "fatec-2026-2sem"
META = {
    "id": ID,
    "banca": "FATEC",
    "ano": 2026,
    "semestre": 2,
    "titulo": "Vestibular FATEC, 2º semestre de 2026",
    "fonte": "Centro Paula Souza",
    "dataExame": "2026-06-28",
    "duracaoMinutos": 300,
    "tema": "Futebol",
    "pdf": f"assets/provas/{ID}.pdf",
}

R = carregar(ID)
MULTI = ["multidisciplinar"]


def p(*paragrafos, classe=None):
    abre = f'<p class="{classe}">' if classe else "<p>"
    return "".join(abre + x + "</p>" for x in paragrafos)


def apoio(*paragrafos):
    return '<p class="apoio">' + A.join(paragrafos) + "</p>"


def fonte(t):
    return f'<p class="fonte">{t}</p>'


def url(u, data, extra="Adaptado."):
    return fonte(f"&lt;{u}&gt; Acesso em: {data}." + (" " + extra if extra else ""))


def chamada(t):
    return f'<p class="chamada">{t}</p>'


def figs(*pares):
    return [{"arquivo": a, "alt": t} for a, t in pares]


def sem_url_no_texto(h, u, data, extra="Adaptado."):
    """O rascunho junta a fonte ao parágrafo: separa em <p class="fonte">."""
    marca = f" &lt;{u}&gt; Acesso em: {data}." + (" " + extra if extra else "")
    if marca not in h: raise ValueError(f"fonte não encontrada: {u}")
    return h.replace(marca, "</p>" + url(u, data, extra) + "<p>")


# ---------- textos compartilhados ----------
RADAR = (chamada("Leia o texto para responder às questões de 07 a 10.")
         + p("Uma franquia de jogos eletrônicos de futebol, em 2018, utilizava gráficos de radar para mensurar as habilidades dos personagens. Nesse tipo de gráfico, cada eixo é igualmente espaçado e corresponde a uma habilidade diferente do personagem analisado, de forma que valores mais altos são representados por pontos mais distantes do centro do gráfico. Isso permite identificar e comparar os pontos fortes e fracos de cada personagem. Veja os gráficos.")
         + "[[fig:1]][[fig:2]]")
RADAR_IMG = figs(("q07a", "Gráfico de radar do Personagem 1, com seis eixos de 0 a 5. Valores: Agilidade 4, Força 5, Equilíbrio 4, Precisão 3, Resistência 2 e Técnica 4."),
                 ("q07b", "Gráfico de radar do Personagem 2, com seis eixos de 0 a 5. Valores: Agilidade 4, Força 3, Equilíbrio 5, Precisão 4, Resistência 4 e Técnica 1."))
P7 = p("A partir das informações apresentadas no gráfico, é correto afirmar que")

TRIONDA = (chamada("Leia o texto para responder às questões de 11 a 13.")
           + p("A Trionda, a bola da Copa de 2026, é baseada no tetraedro regular: um sólido formado por quatro faces triangulares iguais. Desta forma, a bola é composta por apenas 4 painéis (o menor número já usado).",
               "O truque para obter o formato esférico foi transformar os lados retos dos triângulos em curvas, obtendo o formato base para o painel que compõe a bola, conforme a figura. O modelo Pro, que será usado nos campos, tem cerca de 69 cm de circunferência e custo estimado em R$ 1.300,00, contudo existe um modelo Mini, mais barato.")
           + url("https://tinyurl.com/yt3feud6", "21.03.2026", "Traduzido e adaptado. Original colorido.")
           + "[[fig:1]]")
TRIONDA_IMG = figs(("q11", "Em cima, um tetraedro (pirâmide de quatro faces triangulares) e, ao lado, a bola Trionda, esférica, com quatro painéis curvos. Embaixo, um triângulo se transforma, em etapas, em um painel com os lados curvados, com o recado: “Os lados do triângulo se transformam em curvas.”"))
P11 = p("De acordo com o texto, apesar do truque utilizado para obter o formato esférico da Trionda, pode-se afirmar que, após esse processo, a característica do tetraedro que permanece preservada é")

CHARGE = (chamada("Leia a charge para responder às questões 29 e 30.") + "[[fig:1]]"
          + url("https://tinyurl.com/ywr9da5v", "10.04.2026", "Original colorido."))
CHARGE_IMG = figs(("q29", "Charge em um estádio da Copa do Mundo (“World Cup”). Na arquibancada, uma torcida animada, com bandeiras dos Estados Unidos e a palavra “USA”, levanta um grande cartaz: “YOU PLAY LIKE A GIRL!”. Uma pessoa da torcida comenta: “Remember when that was an insult?”."))
P29 = p("A palavra “like”, na sentença “You play like a girl”, indica")

SOCIO = (chamada("Leia o texto para responder às questões 31 e 32.")
         + apoio("<strong>The Sociology of Football</strong>",
                 "The Sociology of Football is the study of the social dynamics, cultural significance, and institutional structures surrounding football (soccer) as a global phenomenon. <strong><u>It</u></strong> examines how football influences and reflects social identities, community relations, and power dynamics, as well as <strong><u>its</u></strong> role in shaping societal values and norms.")
         + url("https://tinyurl.com/2sbb5a7a", "10.04.2026", ""))
P31 = p("De acordo com o texto, a Sociologia do Futebol estuda")

GLT = (chamada("Leia o texto para responder às questões 36 e 37.")
       + p("Para resolver a polêmica questão no futebol “a bola entrou ou não?”, em 2012, a IFAB (International Football Association Board) colocou em teste dois sistemas de GLT (Goal-Line Technology) que enviam, em menos de 1 segundo, um sinal de rádio criptografado aos oficiais da partida e ao relógio do árbitro com a mensagem “GOAL”.", classe="apoio"))
P36 = p("Um desses sistema é o GoalRef, que se baseia em indução eletromagnética. Para funcionar, ao redor da estrutura de cada baliza (conjunto traves e travessão), são instalados cabos de cobre que funcionam como antenas de baixa frequência. A bola, por sua vez, é fabricada com três bobinas de cobre finas, posicionadas de forma adequada.",
        "Quando a bola entra na zona do campo magnético gerado pela baliza, o fluxo magnético (ϕ) que atravessa essas bobinas varia. Essa variação (Δ) no fluxo magnético, num determinado intervalo de tempo (<em>t</em>), induz uma força eletromotriz (ε). Quanto maior a variação do fluxo magnético no tempo ou menor o tempo de interação com o campo, maior será a força eletromotriz induzida. Assim, quando a bola cruza completamente a linha, gera uma “perturbação” no campo magnético da baliza e o sistema envia o sinal de rádio criptografado aos oficiais da partida.",
        "Com base nessa descrição, assinale a alternativa que representa corretamente a equação física envolvida nesse processo.")

POEMA = (chamada("Leia o poema “O Anjo das Pernas Tortas”, de Vinicius de Moraes, para responder às questões 56 e 57.")
         + "[[fig:1]]" + url("https://tinyurl.com/5xuymkxz", "04.04.2026", ""))
POEMA_IMG = figs(("q56", "Soneto “O Anjo das Pernas Tortas”, de Vinicius de Moraes, em quatro estrofes, com verbos no presente. Na 1ª, a um passe de Didi, Garrincha avança com o “couro” (a bola) colado aos pés, dribla um, dribla dois e para, como quem mede o lance. Na 2ª, ele pressente a jogada, se lança mais rápido que o pensamento, dribla mais dois, e a bola “trança” feliz entre seus pés, “um pé de vento”. Na 3ª, a multidão, “contrita”, “em ato de morte”, se levanta e grita um canto de esperança. Na 4ª, Garrincha, “o anjo”, atende: “Goooool!”; o poema diz que é pura imagem, “um G que chuta um o dentro da meta, um l”, e termina: “É pura dança!”."))
P56 = p("Após a leitura atenta do poema, é correto afirmar que")

MANCHETES = (chamada("Leia os textos para responder às questões 58 e 59.")
             + apoio("Texto I", "<strong>DECLARAÇÕES MISÓGINAS DE ZAGUEIRO CONTRA ÁRBITRA MARCAM ELIMINAÇÃO DO BRAGANTINO</strong>",
                     "“Não adianta a gente jogar contra São Paulo, Palmeiras, Corinthians e eles colocarem uma mulher para apitar”, diz Gustavo Marques")
             + fonte("<em>Folha de São Paulo</em>, 21 de fevereiro de 2026")
             + apoio("Texto II", "<strong>JOGADOR DO BRAGANTINO PEGA 12 JOGOS DE SUSPENSÃO POR FALAS SEXISTAS CONTRA ARBITRAGEM</strong>",
                     "Zagueiro Gustavo Marques é punido pelo Tribunal de Justiça Desportiva de São Paulo")
             + fonte("<em>Folha de São Paulo</em>, 5 de março de 2026"))
P58 = p("Ao se compararem os dois textos, conclui-se corretamente que")

Q = {
1: {"materia": "Biologia", "assunto": "Citologia", "tags": ["fermentação lática", "respiração celular"],
    "explicacao": "<p>Sem oxigênio suficiente, a fibra muscular faz fermentação lática: quebra a glicose em <strong>lactato</strong> e obtém ATP rapidamente, ainda que em pouca quantidade. Alternativa <strong>D</strong>.</p><p>A fermentação produz menos ATP que a respiração aeróbica (A). A fermentação lática não libera CO<sub>2</sub>, e os ribossomos fazem proteínas, não respiração (B). O produto é ácido lático, não acético (C). E etanol é produto da fermentação alcoólica, de leveduras (E).</p>"},
2: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": ["tuberculose", "bactérias"],
    "explicacao": "<p>A tuberculose é causada por uma bactéria (o bacilo de Koch) e passa de pessoa para pessoa pelo ar, em gotículas de tosse, fala e espirro. O <strong>uso de máscara</strong> perto de um doente reduz a inalação dessas gotículas. Alternativa <strong>C</strong>.</p><p>Atividade física não dá imunidade, e a doença não é viral (A e E). Ela não se transmite pela água nem por alimentos crus (B e D). E tomar antibiótico preventivo sem indicação não é uma medida de prevenção geral (E).</p>"},
3: {"materia": "Biologia", "assunto": "Fisiologia humana", "tags": ["sangue", "hormônios"],
    "explicacao": "<p>Sem EPO, a medula produz menos hemácias, e chega menos oxigênio aos músculos. O resultado é <strong>intolerância ao esforço e fadiga</strong>, sinais típicos de anemia. Alternativa <strong>B</strong>.</p><p>A icterícia vem do acúmulo de bilirrubina, ligado ao fígado ou à destruição de hemácias (A). A falta de hemácias não causa hipertensão imediata (C), não aumenta a densidade óssea (D) nem causa fotofobia (E).</p>"},
4: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": ["saneamento básico"],
    "explicacao": "<p>Banheiros secos e fossas sépticas tratam os dejetos por processos biológicos (compostagem ou biodigestão), evitam o esgoto a céu aberto e ainda <strong>economizam água potável</strong>. Alternativa <strong>E</strong>.</p><p>A compostagem trata lixo orgânico, e o objetivo é a salubridade, não a insalubridade (A). Cisternas são uma boa solução de captação de água (B). A eutrofização mata os peixes por falta de oxigênio (C). E só construir hospitais, sem saneamento, não resolve a causa do problema (D).</p>"},
5: {"materia": "Biologia", "assunto": "Ecologia", "tags": ["espécies invasoras"],
    "enunciado": enun(R, 5, quebras=["É uma espécie exótica"]),
    "explicacao": "<p>O texto diz que a agressividade e a <strong>facilidade de adaptação</strong> do javali, junto com a <strong>reprodução descontrolada</strong> e a falta de predadores, fazem a população crescer. Alternativa <strong>E</strong>.</p><p>Os javalis reviram o solo e aumentam a erosão (A). Não ajudam na criação de bovinos (B). Não controlam lagartas: eles mesmos destroem lavouras (C). E, como espécie invasora, prejudicam as plantas nativas (D).</p>"},
6: {"materia": "Biologia", "assunto": "Nutrição e saúde", "tags": MULTI + ["nutrição", "energia dos alimentos"],
    "enunciado": p("O café da manhã de um jogador de futebol foi composto, entre outros itens, por:")
                 + tabela(["Itens", "Proteínas (g)", "Carboidratos (g)", "Lipídios (g)"],
                          [["Ovos mexidos", "30", "4", "17"], ["Abacate", "2", "9", "15"], ["Iogurte Grego", "30", "10", "14"], ["Granola", "3", "20", "3"], ["Suco de laranja", "1,5", "21", "0,2"]])
                 + p("Considerando as proteínas e os carboidratos, que têm o mesmo valor energético (4 kcal/g), assinale a alternativa que apresenta corretamente o item mais energético do café da manhã."),
    "explicacao": "<p>O enunciado manda considerar só proteínas e carboidratos (4 kcal/g cada). Somando os dois: ovos 34 g, abacate 11 g, iogurte 40 g, granola 23 g e suco 22,5 g. O <strong>iogurte</strong> tem mais: 40 · 4 = 160 kcal. Alternativa <strong>C</strong>.</p><p>Os ovos dão 34 · 4 = 136 kcal nessa conta (A). Atenção: se os lipídios entrassem (9 kcal/g), os ovos chegariam a 289 kcal e passariam o iogurte (286 kcal). Mas o enunciado pede só proteínas e carboidratos. Abacate, granola e suco ficam bem abaixo (B, D e E).</p>"},
7: {"materia": "Matemática", "assunto": "Estatística", "tags": ["gráfico de radar"],
    "enunciado": RADAR + P7, "imagens": RADAR_IMG,
    "explicacao": "<p>No Personagem 1, o maior valor é a força (5). No Personagem 2, o maior valor é o equilíbrio (5). Alternativa <strong>D</strong>.</p><p>O Personagem 2 tem mais resistência que o 1 (4 contra 2) (A). Ele perde em força e técnica (B). Os dois não empatam em equilíbrio (4 e 5) nem em força (5 e 3) (C). E o Personagem 1 empata em agilidade (4 e 4) e perde em resistência e precisão (E).</p>"},
8: {"materia": "Matemática", "assunto": "Probabilidade",
    "enunciado": p("Sorteando-se ao acaso uma das habilidades de qualquer um dos dois personagens, a probabilidade de ela ser menor ou igual a 3 é"),
    "apoio_de": (7, P7),
    "alternativas": {l: f"\\(\\dfrac{{{a}}}{{{b}}}\\)" for l, (a, b) in zip("ABCDE", [(1, 2), (1, 3), (1, 6), (5, 6), (5, 12)])},
    "explicacao": "<p>São 12 habilidades no total (6 de cada personagem). Valores menores ou iguais a 3: no Personagem 1, precisão (3) e resistência (2); no Personagem 2, força (3) e técnica (1). São 4 casos em 12: 4/12 = <strong>1/3</strong>. Alternativa <strong>B</strong>.</p><p>Contar só os valores menores que 3 daria 2/12 = 1/6 (C). E 5/12 viria de contar também um valor 4 por engano (E).</p>"},
9: {"materia": "Matemática", "assunto": "Estatística", "tags": ["média aritmética"],
    "enunciado": p("A média aritmética das estatísticas das habilidades do Personagem 1 pertence a qual intervalo real?"),
    "apoio_de": (7, P7),
    "explicacao": "<p>Personagem 1: 4 + 5 + 4 + 3 + 2 + 4 = 22. A média é 22 ÷ 6 ≈ 3,67, que está no intervalo <strong>[3 ; 4[</strong>. Alternativa <strong>D</strong>.</p><p>O colchete virado para fora (como em 4[) indica que o extremo não entra no intervalo. Os outros intervalos não contêm 3,67.</p>"},
10: {"materia": "Matemática", "assunto": "Geometria plana", "tags": ["área", "trigonometria"],
     "enunciado": p("Assinale a alternativa que apresenta a área aproximada do polígono cinza, formado pela ligação das estatísticas das habilidades do Personagem 2 no gráfico de radar. Lembre-se de que a área de um triângulo pode ser calculada utilizando a fórmula \\(A = \\dfrac{\\ell_1 \\cdot \\ell_2 \\cdot \\operatorname{sen}\\theta}{2}\\), em que θ é o ângulo formado entre dois lados consecutivos do triângulo (ℓ<sub>1</sub> e ℓ<sub>2</sub>), e de que \\(\\sqrt{3} \\approx 1{,}7\\)."),
     "apoio_de": (7, P7),
     "alternativas": {"E": "23,8"},
     "explicacao": "<p>Os seis eixos dividem a volta em ângulos de 360° ÷ 6 = 60°, e sen 60° = √3/2. O polígono é formado por 6 triângulos com vértice no centro. Na ordem dos eixos, os valores do Personagem 2 são 4, 3, 5, 4, 4 e 1, e os produtos dos vizinhos somam 4·3 + 3·5 + 5·4 + 4·4 + 4·1 + 1·4 = 71.</p><p>Área = 71 · (√3/2) ÷ 2 = 71 · √3/4 ≈ 71 · 1,7 ÷ 4 ≈ <strong>30,2</strong>. Alternativa <strong>A</strong>.</p><p>Errar algum valor do gráfico, como ler a técnica como 2, ou esquecer um dos seis triângulos leva às outras alternativas.</p>"},
11: {"materia": "Matemática", "assunto": "Geometria espacial", "tags": ["poliedros"],
     "enunciado": TRIONDA + P11, "imagens": TRIONDA_IMG,
     "explicacao": "<p>Os lados retos viraram curvas, mas a bola continua com <strong>4 painéis</strong>, como o tetraedro tem 4 faces. A quantidade de regiões da superfície se mantém. Alternativa <strong>E</strong>.</p><p>Os ângulos, o volume e o comprimento das bordas mudam quando os lados retos viram curvas (A, B e C). E os painéis deixam de ser planos para formar a esfera (D).</p>"},
12: {"materia": "Matemática", "assunto": "Geometria espacial", "tags": ["esfera", "volume"],
     "enunciado": p("Lembrando que o volume de uma esfera é dado por \\(V = \\dfrac{4}{3} \\cdot \\pi \\cdot r^3\\), assinale a alternativa que apresenta o volume aproximado do modelo Pro da bola Trionda (adote π = 3)."),
     "apoio_de": (11, P11),
     "explicacao": "<p>A circunferência é 2πr = 69 cm. Com π = 3: 6r = 69, então r = 11,5 cm. Volume: V = (4/3) · 3 · 11,5³ = 4 · 1 520,875 ≈ <strong>6 084 cm³</strong>. Alternativa <strong>B</strong>.</p><p>Usar a circunferência como se fosse o diâmetro ou o raio leva a valores muito maiores ou menores.</p>"},
13: {"materia": "Matemática", "assunto": "Porcentagem",
     "enunciado": p("Suponha que o modelo Mini da bola Trionda custe R$ 100,00. Assinale a alternativa que apresenta, aproximadamente, a porcentagem que esse valor representa em relação ao preço do modelo Pro."),
     "apoio_de": (11, P11),
     "explicacao": "<p>100 ÷ 1 300 ≈ 0,077, ou seja, cerca de 7,7 % ≈ <strong>8 %</strong>. Alternativa <strong>B</strong>.</p><p>13 % seria a razão invertida, 1 300 ÷ 100 = 13, lida como porcentagem (D).</p>"},
14: {"materia": "Matemática", "assunto": "Funções", "tags": ["função do 2º grau"],
     "enunciado": p("O Método de Tracking, ou rastreamento da bola, é usado, por exemplo, para desenvolver câmeras com a função de seguir a bola durante os jogos.")
                  + url("https://tinyurl.com/4e9584y5", "21.03.2026")
                  + p("Suponha que uma câmera, usando essa tecnologia, tenha mapeado a trajetória de uma bola e registrado na tabela alguns dados, sendo que <strong><em>t</em></strong> é o tempo em segundos e <strong><em>A</em></strong> é a altura em metros em relação ao solo.")
                  + tabela(["<em>t</em>", "0", "1", "5"], [["<em>A</em>", "0", "8", "20"]])
                  + p("Logo, sabendo que a bola descreveu uma trajetória que pode ser modelada por uma função de 2º grau, assinale a alternativa na qual essa função está indicada corretamente."),
     "alternativas": {l: f"\\(A(t) = {f}\\)" for l, f in zip("ABCDE", ["-t^2 + 9t", "-t^2 + 5t", "-t^2 + 13t", "3t^2 + 5t", "3t^2 + 9t"])},
     "explicacao": "<p>Como A(0) = 0, a função é A(t) = at² + bt. Com t = 1: a + b = 8. Com t = 5: 25a + 5b = 20, ou seja, 5a + b = 4. Subtraindo: 4a = −4, então a = −1 e b = 9. A função é <strong>A(t) = −t² + 9t</strong>. Alternativa <strong>A</strong>.</p><p>Confira: A(1) = −1 + 9 = 8 e A(5) = −25 + 45 = 20. As outras não passam pelos dois pontos. Além disso, D e E têm a &gt; 0, o que daria uma parábola com a concavidade para cima, impossível para uma bola que sobe e desce.</p>"},
15: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": MULTI + ["sarampo", "vacinação", "porcentagem"],
     "enunciado": p("Leia o texto e assinale a alternativa que completa corretamente as lacunas.")
                  + apoio("Nas Américas, a transmissão endêmica de sarampo foi interrompida em 2002. Considerando o risco de importação desse vírus, diante da realização da Copa do Mundo de 2014 no Brasil, a Organização Pan-Americana em Saúde publicou, antes do evento, suas recomendações à população.",
                          "O sarampo é uma doença causada por ____<strong>(I)</strong>____, altamente contagiosa, que pode provocar surtos e exigir rápida ação de vigilância epidemiológica e vacinação massiva. No caso de vacinação massiva, o limiar de imunidade de rebanho é calculado usando a seguinte fórmula: \\(p = \\left(1 - \\dfrac{1}{R_0}\\right) \\cdot 100\\%\\), em que <strong><em>p</em></strong> é a proporção da população que deve ser vacinada para interromper a transmissão da doença e <strong>R<sub>0</sub></strong> é o número médio de novos casos gerados a partir de um caso inicial de sarampo em uma população totalmente suscetível (estimado entre 12 e 18).",
                          "Logo, no caso de uma epidemia de sarampo, a proporção mínima da população que deve ser vacinada para interromper a transmissão da doença é ____<strong>(II)</strong>____."),
     "alternativas": colunas(["I", "II"], [["uma bactéria", "94,4%"], ["um vírus", "94,4%"], ["um protozoário", "93,3%"], ["um vírus", "91,7%"], ["uma bactéria", "91,7%"]]),
     "explicacao": "<p>O próprio texto fala no “risco de importação desse <strong>vírus</strong>” (I). Para garantir a interrupção mesmo no pior caso, usa-se o maior R<sub>0</sub>, 18: p = (1 − 1/18) · 100 % ≈ <strong>94,4 %</strong> (II). Alternativa <strong>B</strong>.</p><p>O sarampo não é causado por bactéria nem protozoário (A, C e E). Com R<sub>0</sub> = 12, o menor valor, daria 91,7 % (D e E), que não basta se o R<sub>0</sub> real for maior. E 93,3 % corresponde a R<sub>0</sub> = 15 (C).</p>"},
16: {"materia": "Geografia", "assunto": "População", "tags": ["imigração italiana", "racismo"],
     "enunciado": sem_url_no_texto(enun(R, 16, quebras=["Durante a década de 1920"]), "https://tinyurl.com/3djz269p", "28.03.2026"),
     "explicacao": "<p>Mesmo fundado por italianos, o clube tinha torcedores de fora desse padrão, como a “Vovó do Pito”, mulher negra e ex-escravizada, e passou a incluir atletas brasileiros e negros. Ou seja, o clube <strong>se integrava à sociedade em que estava</strong>, em vez de segregar. Alternativa <strong>E</strong>.</p><p>O texto mostra a presença de negros no clube (A e C). A “Vovó do Pito” era torcedora, não presidente (B). E a Itália é um país europeu (D).</p>"},
17: {"materia": "Geografia", "assunto": "Geopolítica", "tags": ["Bálcãs", "Kosovo"],
     "enunciado": sem_url_no_texto(enun(R, 17), "https://tinyurl.com/yb7xk75a", "26.03.2026"),
     "explicacao": "<p>O <strong>Kosovo</strong>, região de maioria albanesa, declarou independência da Sérvia em 2008, e a Sérvia não a reconhece. Essa é a principal disputa entre sérvios e albaneses. Alternativa <strong>B</strong>.</p><p>Palestina (Oriente Médio), Caxemira (Índia e Paquistão), Catalunha (Espanha) e Nagorno-Karabakh (Armênia e Azerbaijão) são conflitos de outras regiões (A, C, D e E).</p>"},
18: {"materia": "Geografia", "assunto": "Transportes e logística", "tags": ["ferrovias", "café"],
     "explicacao": "<p>No fim do século XIX e início do XX, a <strong>expansão do café</strong> pelo interior paulista levou à construção de ferrovias que levavam a produção ao porto de Santos. Os funcionários dessas companhias fundaram vários clubes. Alternativa <strong>D</strong>.</p><p>As ferrovias vieram por causa do café, não de fábricas ferroviárias (A). A soja do Centro-Oeste (B) e o Proálcool (C) são de décadas mais recentes. E os campos de futebol não foram construídos pelo governo como lazer (E).</p>"},
19: {"materia": "Geografia", "assunto": "Urbanização", "tags": ["impermeabilização do solo", "enchentes"],
     "explicacao": "<p>As várzeas são áreas que recebem a água das cheias dos rios. Impermeabilizadas, elas deixam de absorver a chuva, que escoa mais rápido e em maior volume para os rios. Isso <strong>aumenta as enchentes e inundações</strong>. Alternativa <strong>C</strong>.</p><p>A impermeabilização diminui a infiltração e a recarga dos lençóis freáticos (A e B), não muda a quantidade de chuva (D) e aumenta a velocidade de escoamento (E).</p>"},
20: {"materia": "Geografia", "assunto": "Cartografia", "tags": ["hemisférios", "Linha do Equador"],
     "explicacao": "<p>A Linha do Equador divide a Terra nos hemisférios Norte, ou <strong>Setentrional</strong> (Boreal), e Sul, ou <strong>Meridional</strong> (Austral). Alternativa <strong>A</strong>.</p><p>Greenwich é o meridiano que divide o Oriente do Ocidente, e o Equador é a linha, não um hemisfério (B). Ocidental, Oriental, Oeste e Leste se referem à divisão pelo meridiano de Greenwich (C, D e E).</p>"},
21: {"materia": "Geografia", "assunto": "Cartografia", "tags": MULTI + ["fusos horários"],
     "enunciado": enun(R, 21, quebras=["Sabendo que o estado"]),
     "explicacao": "<p>São Paulo (UTC−3) está 2 horas adiantado em relação ao Acre (UTC−5). Se o jogo começou às 19 h no Acre, em São Paulo eram <strong>21 h</strong>. Alternativa <strong>D</strong>.</p><p>Diminuir as 2 horas, em vez de somar, daria 17 h (B). E 19 h ignora a diferença de fuso (C).</p>"},
22: {"materia": "Química", "assunto": "Funções inorgânicas", "tags": ["óxidos"],
     "enunciado": enun(R, 22, quebras=["O composto químico liberado"]),
     "explicacao": "<p>O texto diz que o NO “não reage com substâncias presentes no organismo como água, ácidos e bases”. Um óxido que não reage com água, ácidos nem bases é um <strong>óxido neutro</strong> (como também o CO e o N<sub>2</sub>O). Alternativa <strong>D</strong>.</p><p>Hidrácidos são ácidos sem oxigênio, como o HCℓ (A). Hidróxidos são bases com OH<sup>–</sup> (B). Óxidos ácidos reagem com água formando ácidos (C). E sais oxigenados têm um cátion e um ânion com oxigênio (E).</p>"},
23: {"materia": "Química", "assunto": "Química orgânica", "tags": ["funções orgânicas", "fenol"],
     "enunciado": enun(R, 23, figs={"p08-1": 1}),
     "imagens": figs(("q23", "Fórmulas estruturais. Adrenalina: anel benzênico com dois grupos OH ligados ao anel e uma cadeia lateral com um OH em carbono da cadeia e um grupo NH–CH₃. Dopamina: anel benzênico com dois grupos OH ligados ao anel e uma cadeia lateral CH₂–CH₂–NH₂.")),
     "explicacao": "<p>As duas moléculas têm dois grupos <strong>–OH ligados diretamente ao anel aromático</strong>: é a função <strong>fenol</strong>. Alternativa <strong>B</strong>.</p><p>Só a adrenalina tem OH ligado a carbono saturado da cadeia, o álcool (A). Nenhuma das duas tem amida, ácido carboxílico ou cetona (C, D e E); o nitrogênio delas é de amina.</p>"},
24: {"materia": "Química", "assunto": "Funções inorgânicas", "tags": ["sais", "nomenclatura"],
     "enunciado": enun(R, 24, trocas=[("[[FIG:p09-1]]", tabela(["Sais", "Cor"], [["NaCℓ", "Amarela"], ["CuCℓ<sub>2</sub>", "Verde"], ["KNO<sub>3</sub>", "Lilás"], ["SrCℓ<sub>2</sub>", "Vermelho"], ["Ca(NO<sub>3</sub>)<sub>2</sub>", "Laranja"]]))]),
     "explicacao": "<p>Pelo quadro, o lilás vem do KNO<sub>3</sub>, o <strong>nitrato de potássio</strong>, e o verde vem do CuCℓ<sub>2</sub>, o <strong>cloreto de cobre(II)</strong>. Alternativa <strong>B</strong>.</p><p>Cloreto de sódio dá amarelo, e cloreto de cobalto não está no quadro (A). Estrôncio dá vermelho e cálcio dá laranja (C e D). E “nitreto” é outro tipo de composto (N<sup>3–</sup>); o KNO<sub>3</sub> é nitrato (E).</p>"},
25: {"materia": "Química", "assunto": "Soluções", "tags": ["concentração comum"],
     "enunciado": enun(R, 25, trocas=[("[[FIG:p09-2]]", "<p>\\[\\text{Concentração} = \\dfrac{\\text{massa do soluto}}{\\text{volume da solução}}\\]</p>")], quebras=["Assinale a alternativa que contém"]),
     "explicacao": "<p>A massa ingerida é 0,042 g = 42 mg. Com concentração de 140 mg/L, o volume é V = 42 ÷ 140 = 0,3 L = <strong>300 mL</strong>. Alternativa <strong>C</strong>.</p><p>Esquecer de converter gramas em miligramas, ou litros em mililitros, leva a valores mil vezes maiores ou menores, fora das alternativas.</p>"},
26: {"materia": "Química", "assunto": "Polaridade e solubilidade", "tags": ["polaridade", "polímeros"],
     "enunciado": enun(R, 26, figs={"p10-1": 1}),
     "imagens": figs(("q26", "Quadro com duas colunas, Algodão e Dry fit. Fórmula estrutural: o algodão (celulose) é uma cadeia de anéis de glicose com muitos grupos OH; o dry fit (poliéster) é uma cadeia com anel benzênico e grupos éster (C=O ligado a O), sem grupos OH. Linha Polaridade: (I) para o algodão e (II) para o dry fit. Linha Absorção de água: (III) para o algodão e (IV) para o dry fit. Linha Suor: o algodão retém e o dry fit espalha.")),
     "explicacao": "<p>A celulose do algodão tem muitos grupos OH, que formam ligações de hidrogênio com a água: <strong>polaridade alta (I)</strong> e <strong>absorção alta (III)</strong>, por isso retém o suor. O poliéster do dry fit quase não tem grupos polares: <strong>polaridade baixa (II)</strong> e <strong>absorção baixa (IV)</strong>, por isso espalha o suor, que seca rápido. Alternativa <strong>B</strong>.</p><p>As outras combinações trocam alguma dessas características. Em especial, um tecido que retém o suor não pode ter absorção de água baixa (A e C).</p>"},
27: {"materia": "Biologia", "assunto": "Fisiologia humana", "tags": MULTI + ["termorregulação", "evaporação"],
     "enunciado": enun(R, 27, quebras=["No momento da partida", "Do ponto de vista fisiológico"], trocas=[("32 <sup>o</sup>C", "32 °C")]),
     "explicacao": "<p>O suor resfria o corpo quando evapora, porque a evaporação retira calor da pele. Com o ar muito úmido (alta pressão parcial de vapor de água), <strong>a evaporação fica difícil</strong> e o corpo perde menos calor. Alternativa <strong>C</strong>.</p><p>A umidade não desnatura enzimas (A) nem muda o calor específico da água (B). A pressão atmosférica não sobe por causa da umidade (D). E o suor é líquido: ele evapora, não sublima (E).</p>"},
28: {"materia": "Inglês", "assunto": "Interpretação de texto",
     "enunciado": enun(R, 28, trocas=[("<strong>Zayu™ the Jaguar</strong> Zayu", '<strong>Zayu™ the Jaguar</strong></p><p class="apoio">Zayu')]),
     "explicacao": "<p>O texto diz que o nome de Zayu foi inspirado em <em>unity, strength and joy</em> (união, força e alegria) e que ele mostra <em>exceptional ingenuity and agility</em> (engenhosidade excepcional e agilidade). Daí: <strong>força, agilidade e criatividade</strong>. Alternativa <strong>B</strong>.</p><p>Cuidado com o falso cognato: <em>ingenuity</em> é engenhosidade, criatividade, e não ingenuidade (A). O texto não fala de inocência, regionalismo, exceção ou religião (C, D e E).</p>"},
29: {"materia": "Inglês", "assunto": "Vocabulário", "tags": ["preposições"],
     "enunciado": CHARGE + P29, "imagens": CHARGE_IMG,
     "explicacao": "<p>Em “You play like a girl”, <em>like</em> significa “como”: compara o jeito de jogar ao de uma garota. Indica <strong>comparação</strong>. Alternativa <strong>C</strong>.</p><p>Aqui <em>like</em> não é o verbo “gostar” (A) e não indica oposição, exemplo ou distanciamento (B, D e E).</p>"},
30: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": ["charge"],
     "enunciado": CHARGE + p("A partir da charge, conclui-se corretamente que"), "imagens": CHARGE_IMG,
     "explicacao": "<p>Um torcedor comenta: “Lembra quando isso era um insulto?”. A frase “Você joga como uma garota”, antes ofensiva, virou elogio: a torcida <strong>tem orgulho</strong> de como as jogadoras estadunidenses jogam. Alternativa <strong>D</strong>.</p><p>A charge diz o contrário de que as mulheres jogam pior (A) e de que haja insulto ou ridicularização (B e E). E a torcida está comemorando, não hostilizando ninguém (C).</p>"},
31: {"materia": "Inglês", "assunto": "Interpretação de texto",
     "enunciado": SOCIO + P31,
     "explicacao": "<p>O texto define a Sociologia do Futebol como o estudo das “dinâmicas sociais, do significado cultural e das estruturas institucionais em torno do futebol”. Ela estuda as <strong>relações sociais e culturais em torno do futebol</strong>. Alternativa <strong>D</strong>.</p><p>O poder é só um dos pontos, e o texto não fala de desigualdades geradas pelo esporte (A). O fenômeno global é o próprio futebol, não “fenômenos globalizados” em geral (B). O texto não fala de violência (C) nem de classificação esportiva (E).</p>"},
32: {"materia": "Inglês", "assunto": "Coesão e referência", "tags": ["pronomes"],
     "enunciado": SOCIO + p("As palavras em destaque, “it” e “its”, referem-se, respectivamente, a"),
     "explicacao": "<p>“<em>It examines how football influences...</em>”: quem examina é a disciplina, <strong>the Sociology of Football</strong>. Em “<em>its role in shaping societal values</em>”, o papel é do <strong>football</strong>. Alternativa <strong>E</strong>.</p><p>O futebol não “examina” nada (A). E <em>its</em> retoma um termo no singular que tem papel na sociedade, o futebol, e não as outras expressões listadas (B, C e D).</p>"},
33: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": MULTI + ["resenha"],
     "enunciado": apoio("<strong>The English Game Review</strong>", "Hannah Parker",
                        "Period dramas aren’t to everyone’s taste, and the story of class wars in Britain has been told over and over again. Sometimes, it’s been told extremely well, but often the theme can be repetitive, insensitive and glamorised. Perhaps the same could be said about the FA Cup — some love it, but nowadays more seem to dislike it. Bringing the two together could be a disaster.",
                        "The new drama series about the early days of the FA Cup in the late 1800’s however, is an example of this theme being done well. The show is a perfect example of telling a class war story in a sensitive and realistic manner.")
                  + url("https://tinyurl.com/2zvwpt8c", "08.04.2026", "") + fonte("Glossário: <strong>FA</strong> – Football Association")
                  + p("A resenha a respeito da série “The English Game” é"),
     "explicacao": "<p>Depois de dizer que juntar os dois temas “poderia ser um desastre”, a autora usa <em>however</em> (porém) e afirma que a série é “um exemplo perfeito de contar uma história de luta de classes de forma <strong>sensível</strong> e realista”. A resenha é <strong>positiva</strong>. Alternativa <strong>A</strong>.</p><p>Repetição, insensibilidade e glamourização são os defeitos que a série evita (B e D). E as críticas aos dramas de época e ao risco de “desastre” são só a introdução, que o <em>however</em> contradiz (C e E).</p>"},
34: {"materia": "Física", "assunto": "Dinâmica", "tags": ["resistência do ar"],
     "enunciado": enun(R, 34, quebras=["Com base nessas informações"]),
     "explicacao": "<p>Em grandes altitudes o ar é mais rarefeito, com menos moléculas. A <strong>resistência do ar é menor</strong>, e a bola perde menos velocidade no caminho. Alternativa <strong>C</strong>.</p><p>Em altitude há menos oxigênio, não mais (A). O ar rarefeito não aumenta a potência das pernas (B). A bola com ar comprimido não fica mais leve que o ar (D). E, com menos pressão externa, a bola tende a ficar um pouco mais cheia, não menor (E).</p>"},
35: {"materia": "Física", "assunto": "Cinemática", "tags": ["lançamento oblíquo"],
     "enunciado": enun(R, 35, quebras=["Considerando a situação ideal"]),
     "alternativas": {"E": "sua velocidade vertical foi nula e a horizontal foi 16 m/s no ponto mais alto da trajetória."},
     "explicacao": "<p>Sem resistência do ar, a velocidade horizontal é constante: 96 m ÷ 6 s = 16 m/s. No ponto mais alto, a bola para de subir e começa a descer, então a <strong>velocidade vertical é nula</strong>, e a horizontal continua <strong>16 m/s</strong>. Alternativa <strong>E</strong>.</p><p>576 é 96 · 6, não uma velocidade (A). A velocidade vertical no topo é zero, não 16 m/s (B e D). E perto do chão a velocidade total é máxima, não nula (C).</p>"},
36: {"materia": "Física", "assunto": "Magnetismo", "tags": ["indução eletromagnética", "lei de Faraday"],
     "enunciado": GLT + P36,
     "alternativas": {"A": "\\(\\varepsilon = \\dfrac{|\\Delta\\phi|}{\\Delta t}\\)", "B": "\\(t = \\dfrac{|\\Delta\\varepsilon|}{\\Delta\\phi}\\)", "C": "\\(\\Delta\\phi = \\dfrac{|\\Delta t|}{\\Delta\\varepsilon}\\)",
                      "D": "\\(\\varepsilon = \\dfrac{|\\Delta t|}{\\Delta\\phi}\\)", "E": "\\(\\phi = \\dfrac{|\\Delta\\varepsilon|}{\\Delta t}\\)"},
     "explicacao": "<p>O texto diz que a força eletromotriz é maior quanto maior a variação do fluxo e quanto menor o tempo. Então ε é diretamente proporcional a Δϕ e inversamente proporcional a Δt: <strong>ε = |Δϕ| / Δt</strong>, a lei de Faraday. Alternativa <strong>A</strong>.</p><p>D inverte a relação (ε cresceria com o tempo). B, C e E isolam grandezas que o texto não descreve dessa forma.</p>"},
37: {"materia": "Física", "assunto": "Ondas", "tags": ["frequência e período", "notação científica"],
     "enunciado": GLT + enun(R, 37, quebras=["Com base nessa descrição"]),
     "alternativas": {"E": "2,0 × 10<sup>–6</sup>.", "A": "2,0 × 10<sup>6</sup>.", "B": "2,0 × 10<sup>3</sup>.", "C": "2,0 × 10<sup>0</sup>.", "D": "2,0 × 10<sup>–3</sup>."},
     "explicacao": "<p>O período é o inverso da frequência: T = 1 ÷ 500 = 0,002 s = <strong>2,0 × 10<sup>–3</sup> s</strong>. Alternativa <strong>D</strong>.</p><p>Os valores com expoente positivo confundem período com frequência (A, B e C). E 10<sup>–6</sup> seria um microssegundo, mil vezes menor (E).</p>"},
38: {"materia": "Física", "assunto": "Termologia", "tags": ["gases", "transformação isovolumétrica"],
     "enunciado": p("Pelas regras do futebol, a bola oficial deve estar calibrada com uma pressão entre 0,60 atm e 1,10 atm ao nível do mar.",
                    "Em um jogo numa cidade litorânea, os oficiais da partida calibraram uma bola a 0,90 atm a uma temperatura de 27 °C. Durante uma parada técnica, a bola ficou exposta ao Sol e sua temperatura subiu para 57 °C, porém o seu volume permaneceu constante. Antes de reiniciar a partida, o árbitro pediu nova checagem da calibração.",
                    "Lembrando que: \\(T_K = T_C + 273\\) e \\(\\dfrac{P_0 \\cdot V_0}{T_0} = \\dfrac{P_1 \\cdot V_1}{T_1}\\)",
                    "Admitindo que o ar no interior da bola se comporte como gás ideal, podemos afirmar corretamente que a bola"),
     "explicacao": "<p>Em kelvin: T<sub>0</sub> = 300 K e T<sub>1</sub> = 330 K. Com volume constante, P<sub>1</sub> = P<sub>0</sub> · T<sub>1</sub>/T<sub>0</sub> = 0,90 · 330/300 = 0,99 ≈ <strong>1,00 atm</strong>. Está dentro do limite de 1,10 atm, então a bola <strong>foi mantida</strong>. Alternativa <strong>C</strong>.</p><p>Com o aquecimento, a pressão sobe, não cai nem fica igual (A e B). 1,20 atm e 1,90 atm vêm de fazer a conta em graus Celsius em vez de kelvin (D e E): 0,90 · 57/27 ≈ 1,90.</p>"},
39: {"materia": "Física", "assunto": "Energia", "tags": MULTI + ["teorema da energia cinética", "inglês"],
     "explicacao": "<p>O trabalho da força resultante é igual à variação da energia cinética. A bola sai do repouso e atinge cerca de 31 m/s: W = m · v² ÷ 2 = 0,42 · 31² ÷ 2 = 0,21 · 961 ≈ <strong>202 J</strong>. Alternativa <strong>B</strong>.</p><p>Usar a velocidade em km/h (110,79) daria cerca de 2 580 J (A). Esquecer de elevar ao quadrado dá 0,21 · 31 ≈ 7 J (E), e esquecer de dividir por 2 daria cerca de 404 J.</p>"},
40: {"materia": "História", "assunto": "Antiguidade", "tags": ["jogos com bola"],
     "explicacao": "<p>O texto diz que os jogos com bola exigiam regras compartilhadas, antecipar movimentos e cooperação, “habilidades que também foram úteis na caça e na defesa de territórios”. Eles <strong>desenvolveram habilidades sociais e cognitivas</strong>. Alternativa <strong>D</strong>.</p><p>O texto não diz que substituíram a caça (A) nem que vieram depois da escrita (B). Eram coletivos, não individuais (C). E o túmulo de uma criança mostra que crianças também usavam bolas (E).</p>"},
41: {"materia": "História", "assunto": "Antiguidade", "tags": ["Grécia", "Roma"],
     "enunciado": sem_url_no_texto(enun(R, 41), "https://tinyurl.com/nhatdzy7", "02.04.2026", "Traduzido e adaptado.").replace("</p><p>" + "</p>", "</p>"),
     "explicacao": "<p>O <em>epískyros</em> grego exigia agilidade, precisão e espírito de equipe e não era visto como competição séria. O <em>harpastum</em> romano era violento e servia ao treinamento militar. A diferença mostra <strong>gregos valorizando movimento e cooperação, e romanos, utilidade militar e combate</strong>. Alternativa <strong>E</strong>.</p><p>Os romanos se inspiraram no jogo grego, não o desprezaram (A). Quem tinha função militar era o <em>harpastum</em> (B). O texto não fala em inferioridade cultural (C) nem em jogos só femininos ou masculinos (D).</p>"},
42: {"materia": "História", "assunto": "América pré-colombiana", "tags": ["astecas", "maias"],
     "explicacao": "<p>O texto diz que, para os astecas, o jogo representava a batalha entre o Sol e as forças noturnas, e que os sacrifícios humanos serviam para <strong>manter o Sol iluminando a Terra</strong>. Alternativa <strong>B</strong>.</p><p>O formato em “I” não imitava os templos (A). O templo era construído antes do campo, e quem era sacrificado eram os vencedores, em honra ao Sol (C e D). E era proibido usar mãos e pés (E).</p>"},
43: {"materia": "História", "assunto": "Ditadura militar", "tags": ["ditadura civil-militar"],
     "explicacao": "<p>Em 1978, o Brasil vivia a <strong>ditadura civil-militar</strong> (1964–1985). O punho cerrado era um gesto de protesto, e o técnico, capitão do Exército, teria seguido ordens do regime. Alternativa <strong>C</strong>.</p><p>A Era Vargas terminou em 1945 (A). O Pacto Colonial e o Primeiro Reinado são do período colonial e imperial (B e E). E a República Velha terminou em 1930 (D).</p>"},
44: {"materia": "História", "assunto": "Era Vargas", "tags": ["Era Vargas", "racismo"],
     "explicacao": "<p>O governo usou a seleção para exaltar o Estado Novo e a ideia de “democracia racial”, mas os jogadores negros sofreram racismo na imprensa e voltaram ao anonimato e a subempregos. A <strong>propaganda contrastava com a realidade</strong>. Alternativa <strong>D</strong>.</p><p>O próprio texto mostra que a “democracia racial” não correspondia à realidade (A). E não diz que Vargas abandonou o esporte (B), que o futebol foi proibido (C) ou que a Copa foi ignorada (E).</p>"},
45: {"materia": "Geografia", "assunto": "Globalização", "tags": MULTI + ["divisão internacional do trabalho", "migrações"],
     "explicacao": "<p>Os jogadores africanos são mão de obra procurada e barata para os clubes europeus, e o lucro das transferências fica longe dos clubes de origem. É o mesmo padrão de outras migrações: <strong>trabalho de países periféricos atendendo países centrais</strong>, como na divisão internacional do trabalho. Alternativa <strong>A</strong>.</p><p>O fluxo vai da África para a Europa, não o contrário (B). O texto mostra justamente africanos na Europa (C). O futebol faz parte do capitalismo globalizado (D). E não há proibição de saída de jogadores (E).</p>"},
46: {"materia": "Raciocínio lógico", "assunto": "Raciocínio espacial", "tags": ["rotação"],
     "enunciado": p("Considere a imagem, gerada por IA, baseada na bola Trionda e um ponto P no centro dessa imagem.") + "[[fig:1]]"
                  + p("Caso se efetue, na imagem, uma rotação de 90° no sentido horário em torno do ponto P e, em seguida, retirar-se o ponto P da imagem gerada, qual imagem será obtida?"),
     "imagens": figs(("q46", "Desenho circular em preto e branco inspirado na bola Trionda, com o ponto P no centro. Há três regiões principais: no alto à esquerda, uma folha de bordo; no alto à direita, uma estrela grande com um pequeno troféu e a palavra FIFA; embaixo, um desenho de olho com raios, como uma onda."),
                     ("q46a", "Alternativa A: a mesma imagem, sem o ponto P e sem girar: folha de bordo no alto à esquerda, estrela com o troféu no alto à direita e olho embaixo."),
                     ("q46b", "Alternativa B: estrela com o troféu no alto à esquerda, olho à direita e folha de bordo embaixo."),
                     ("q46c", "Alternativa C: olho no alto, folha de bordo embaixo à direita e estrela com o troféu à esquerda, com o troféu de lado."),
                     ("q46d", "Alternativa D: folha de bordo no alto à direita, estrela com o troféu embaixo à direita e olho à esquerda."),
                     ("q46e", "Alternativa E: imagem espelhada: estrela com o troféu no alto à direita, olho à esquerda e folha de bordo embaixo, com o troféu invertido.")),
     "alternativas": {l: f"[[fig:{i}]]" for i, l in enumerate("ABCDE", start=2)},
     "explicacao": "<p>Numa rotação de 90° no sentido horário, o que está no alto à esquerda vai para o alto à direita, o que está no alto à direita vai para baixo à direita, e o que está embaixo vai para a esquerda. Então a folha de bordo fica no alto à direita, a estrela com o troféu embaixo à direita e o olho à esquerda. Alternativa <strong>D</strong>.</p><p>A é a imagem sem girar. B corresponde a uma rotação no sentido anti-horário. C equivale a girar 180°. E é um espelhamento, já que o troféu aparece invertido.</p>"},
47: {"materia": "Raciocínio lógico", "assunto": "Sequências", "tags": ["padrões"],
     "explicacao": "<p>A palavra em negrito é ALLEZ, com 5 símbolos (A, L, L, E, Z), que se repetem nessa ordem. Como 1 985 = 5 · 397, a posição 1 985 é a última de um bloco completo: a letra <strong>Z</strong>. Alternativa <strong>D</strong>.</p><p>O ponto de exclamação não está em negrito, então não entra no bloco repetido (E). As letras A, L e E aparecem em outras posições do bloco (A, B e C).</p>"},
48: {"materia": "Raciocínio lógico", "assunto": "Analogias",
     "explicacao": "<p>A prancha é o objeto essencial com que se pratica o surfe. No futebol, esse objeto é a <strong>bola</strong>. Alternativa <strong>B</strong>.</p><p>Área, campo e estádio são lugares (A, C e E), e drible é uma jogada (D). Nenhum deles faz o papel que a prancha tem no surfe.</p>"},
49: {"materia": "Raciocínio lógico", "assunto": "Lógica", "tags": ["regras"],
     "enunciado": apoio("As regras do futebol de campo são as mesmas em todo o planeta. Entre elas, temos:",
                        "<strong>1.</strong> as duas equipes devem usar cores que as distingam uma da outra e da equipe de arbitragem;",
                        "<strong>2.</strong> cada goleiro deve usar cores que os distingam dos outros jogadores e da equipe de arbitragem;",
                        "<strong>3.</strong> se as camisetas dos dois goleiros forem da mesma cor e nenhum deles tiver outra camiseta, o árbitro permitirá que o jogo seja disputado.",
                        "<strong>4.</strong> as camisas interiores (também conhecidas como segunda pele) devem ter uma única cor, que será a mesma que a cor principal da manga da camiseta; e",
                        "<strong>5.</strong> os jogadores de uma mesma equipe devem usar calções interiores de mesma cor.")
                  + url("https://tinyurl.com/4veyff7x", "21.03.2026")
                  + p("Considere que, em uma partida oficial entre um Time A e um Time B, percebe-se que", "• o Time A usa camiseta azul com mangas azuis;", "• o Time B usa camiseta verde com mangas brancas;", "• a arbitragem usa preto;",
                      "• ambos os goleiros usam amarelo e não possuem outro uniforme;", "• um jogador do Time B usa camisa interior verde;", "• dois jogadores do Time A usam calções interiores, um usa azul e outro usa branco.",
                      "Com base nas regras apresentadas, quantas infrações foram cometidas na situação descrita?"),
     "explicacao": "<p>Azul, verde e preto se distinguem (regra 1). Os goleiros de amarelo se distinguem dos demais (regra 2), e a regra 3 permite que os dois usem a mesma cor. Infrações: a camisa interior do jogador do Time B é verde, mas a manga da camiseta é branca (regra 4); e os calções interiores do Time A têm cores diferentes (regra 5). São <strong>duas</strong>. Alternativa <strong>C</strong>.</p><p>Contar os goleiros de mesma cor como infração daria três (D), mas a regra 3 permite esse caso.</p>"},
50: {"materia": "Raciocínio lógico", "assunto": "Lógica", "tags": ["conectivos lógicos"],
     "enunciado": p("Andrea, Elias e Iara são torcedores de um mesmo time de futebol, mas, como são supersticiosos, seguem certas regras quando se trata de vestir a camisa de seu time para ir torcer:",
                    "• Ou Elias ou Iara devem usar a camisa do time;", "• Andrea usa a camisa do time se, e somente se, Elias usar; e", "• Se Iara usar a camisa do time, então Andrea também usa.",
                    "Quando os três forem torcer pelo seu time, de acordo com as regras expostas, conclui-se corretamente que"),
     "explicacao": "<p>Suponha que Iara use a camisa. Pela 3ª regra, Andrea usa; pela 2ª, Elias também usa. Mas a 1ª regra (“ou… ou…”) exige que só um entre Elias e Iara use. Contradição: <strong>Iara nunca usa</strong>. Então Elias usa (1ª regra) e, pela 2ª, Andrea também. Alternativa <strong>A</strong>.</p><p>Todas as outras alternativas fazem Iara usar a camisa ou deixam Elias sem ela, o que quebra alguma regra (B a E).</p>"},
51: {"materia": "Geografia", "assunto": "Cartografia", "tags": MULTI + ["rosa dos ventos", "orientação"],
     "enunciado": p("No mapa, estão indicados alguns dos estádios da Copa do Mundo de 2026.") + "[[fig:1]]"
                  + p("Sabendo que, durante esse evento esportivo, o time do Brasil deve jogar contra", "• o Marrocos no dia 13 de junho, no MetLife Stadium;", "• o Haiti no dia 19 de junho, no Lincoln Financial Field; e", "• a Escócia no dia 24 de junho, no Hard Rock Stadium, em Miami.",
                      "Então, na ordem dos eventos descritos, os deslocamentos entre os estádios onde ocorrerão os jogos do time do Brasil devem se dar nos sentidos"),
     "imagens": figs(("q51", "Mapa dos Estados Unidos e do sul do Canadá com estádios da Copa de 2026. Na costa leste, de cima para baixo: Boston, New York (MetLife Stadium), logo abaixo e um pouco à esquerda Philadelphia (Lincoln Financial Field), Atlanta e, bem ao sul, na ponta da Flórida, Miami (Hard Rock Stadium). Abaixo do mapa, uma rosa dos ventos com 16 direções e as legendas em inglês dos pontos cardeais, colaterais e subcolaterais.")),
     "explicacao": "<p>De Nova York (MetLife) para a Filadélfia, o deslocamento é para baixo e um pouco para a esquerda no mapa: <strong>sudoeste</strong>. Da Filadélfia para Miami, a viagem é longa, quase toda para o sul e um pouco para o oeste: <strong>sul-sudoeste</strong>. Alternativa <strong>E</strong>.</p><p>Os deslocamentos são para o sul, não para o norte (A e B). E vão para o oeste, não para o leste (C e D).</p>"},
52: {"materia": "Português", "assunto": "Semântica", "tags": ["sinônimos"],
     "explicacao": "<p>“Pouco a pouco” é <strong>progressivamente</strong>; “extrapola”, <strong>supera</strong>; “deliberadamente”, <strong>intencionalmente</strong>; e “provavelmente”, <strong>talvez</strong>. Alternativa <strong>E</strong>.</p><p>“Limita-se a” e “submete-se a” têm sentido oposto a “extrapola” (A e C). “Repentinamente” e “involuntariamente” contrariam “deliberadamente” (C e D). E “decerto” e “seguramente” indicam certeza, não probabilidade (A, B e D).</p>"},
53: {"materia": "Português", "assunto": "Interpretação de texto",
     "explicacao": "<p>O texto mostra que o “futebolês” incorporou termos da culinária e do jogo do bicho e entrou na linguagem coloquial. Ele <strong>dialoga com outras áreas e se incorpora ao cotidiano</strong>. Alternativa <strong>A</strong>.</p><p>O texto diz que as expressões não constavam nos dicionários e não fala da elite intelectual (B). Elas não são restritas aos profissionais (C) nem se limitam a “bola” (D). E a culinária e o jogo do bicho foram fontes de algumas expressões, não a origem de todas (E).</p>"},
54: {"materia": "Português", "assunto": "Semântica", "tags": ["provérbios"],
     "explicacao": "<p>“Bola pra frente” quer dizer deixar o que passou para trás e seguir em frente. O provérbio com o mesmo sentido é “<strong>Águas passadas não movem moinhos</strong>”. Alternativa <strong>C</strong>.</p><p>“A cavalo dado...” fala de não reclamar de presente (A); “Antes só...” prefere a solidão à má companhia (B); “Dai a César...” fala de dar a cada um o que é seu (D); e “Quem semeia vento...” fala de consequências (E).</p>"},
55: {"materia": "Português", "assunto": "Interpretação de texto", "tags": ["charge", "linguagem não verbal"],
     "enunciado": p("Analise a charge.") + "[[fig:1]]" + url("https://tinyurl.com/ue68hep2", "03.04.2026", "Original colorido.")
                  + p("Na charge, o cartão apresentado é vermelho.", "Sobre a linguagem verbal e não verbal utilizada na construção da charge, é correto afirmar que"),
     "imagens": figs(("q55", "Charge: a mão de uma árbitra, de quem só aparece o braço, ergue um cartão (vermelho) e apita, com o som “PRIII!!!” saindo do apito. À frente, um jogador corre com um tronco de madeira (um taco) nas mãos; sua cabeça é coberta por um saco, e na camisa está escrito “MACHISMO” e “MISOGINIA”. No chão, uma bola parada.")),
     "alternativas": {"E": "o saco, que cobre a identidade do agressor, assim como a ausência do rosto da árbitra, igualam vítima e criminoso na imagem."},
     "explicacao": "<p>A árbitra expulsa, com o cartão vermelho, um jogador que tem “machismo” e “misoginia” escritos no corpo. O cartão expressa <strong>a recusa em aceitar a reprodução de preconceitos dentro do campo</strong>. Alternativa <strong>A</strong>.</p><p>A mulher aparece exercendo sua autoridade, não invisibilizada (B). A bola parada mostra o jogo interrompido pela falta, não a revisão das regras (C). O taco reforça a agressividade, não ameniza (D). E a charge não iguala a árbitra ao agressor (E).</p>"},
56: {"materia": "Português", "assunto": "Texto literário", "tags": ["poema", "figuras de linguagem"],
     "enunciado": POEMA + P56, "imagens": POEMA_IMG,
     "explicacao": "<p>A multidão “contrita”, “em ato de morte”, que se levanta e grita um “canto de esperança”, mostra os torcedores <strong>tensos</strong>, à espera do gol. Alternativa <strong>C</strong>.</p><p>“Couro” é a bola, não a resistência do jogador (A). “Um pé de vento” mostra a rapidez do drible, e não a perda da bola pelo rival (B). “Anjo” é Garrincha, mas o “G” é a letra da palavra “Gol”, que no desenho do poema chuta o “o” (D). E “pura imagem” e “pura dança” exaltam o futebol como arte, sem nada de impopular (E).</p>"},
57: {"materia": "Português", "assunto": "Verbos", "tags": ["tempo verbal", "poema"],
     "enunciado": POEMA + p("Os verbos, no poema, estão conjugados"), "imagens": POEMA_IMG,
     "explicacao": "<p>Os verbos estão no presente (“avança”, “dribla”, “se lança”, “grita”, “atende”), como numa narração esportiva ao vivo, que <strong>aproxima as ações do leitor</strong>. Alternativa <strong>B</strong>.</p><p>O presente contínuo seria “está avançando”, e as ações são rápidas, não lentas (A). Os verbos não estão no passado (C e D). E não é um presente atemporal: as ações são de um lance específico de Garrincha (E).</p>"},
58: {"materia": "Português", "assunto": "Gêneros textuais", "tags": ["notícia", "manchete"],
     "enunciado": MANCHETES + P58,
     "explicacao": "<p>A manchete do texto I começa pelas “declarações misóginas” do zagueiro, ou seja, destaca o preconceito. A do texto II começa por “Jogador do Bragantino pega 12 jogos de suspensão”, destacando o jogador punido. Alternativa <strong>C</strong>.</p><p>Pôr “por falas sexistas” no fim não enfatiza a ação; o foco está na punição (A). O nome do atleta aparece na linha fina, que é onde se identificam pessoas, sem intenção de disfarçar (B). “Misóginas” não ameniza nada; é até mais forte que “sexistas” (D). E os textos não comparam a técnica dos jogadores com a arbitragem (E).</p>"},
59: {"materia": "Português", "assunto": "Sintaxe", "tags": ["reescrita", "manchete"],
     "enunciado": MANCHETES + p("Assinale a alternativa que apresenta a reescrita correta de uma das manchetes."),
     "explicacao": "<p>“Devido a falas sexistas contra a arbitragem, jogador do Bragantino é suspenso por 12 jogos” mantém o sentido da manchete II: o jogador foi suspenso por causa de falas sexistas. Alternativa <strong>B</strong>.</p><p>As declarações foram do zagueiro contra a árbitra, não o contrário (A). Quem suspendeu foi o Tribunal, e foi o jogador, não o time (C). A árbitra não eliminou o time, e as falas eram misóginas, não contra a misoginia (D). E o zagueiro não “se declarou misógino” nem eliminou o time (E).</p>"},
60: {"materia": "Biologia", "assunto": "Fisiologia humana", "tags": MULTI + ["altitude", "respiração"],
     "enunciado": enun(R, 60, quebras=["Imagine que, na final", "Diante desse cenário"]),
     "explicacao": "<p>O São Paulo sai de 760 m para 4 338 m, uma diferença de cerca de 3 580 m. O Always Ready sai de 4 150 m, quase a mesma altitude do jogo, e seus atletas já estão aclimatados. O São Paulo <strong>tende a sentir mais</strong> o Mal da Montanha. Alternativa <strong>D</strong>.</p><p>Morar perto do nível do mar é justamente o que faz o São Paulo sentir mais (A). Passar dias em São Paulo tiraria a aclimatação do Always Ready (B). Ser atleta de alto desempenho não anula o efeito da altitude (C). E estar aclimatado à altitude diminui os sintomas, não aumenta (E).</p>"},
}
completar(Q, R)
