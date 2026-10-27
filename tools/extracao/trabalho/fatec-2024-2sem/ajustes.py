# Ajustes da conferência humana: Vestibular FATEC 2º semestre de 2024 (exame de 30/06/2024)
# Texto conferido com a imagem de cada página. Tema implícito: América Latina.
# 54 questões; a prova tem 5 h no total, incluindo a redação (que fica fora do simulado).
# Matéria: a do gabarito oficial; nas "Multidisciplinar", a matéria principal + tag "multidisciplinar".
# O rascunho transformou quase todas as caixas de texto em figuras: os textos vêm do PDF via trecho().
# Gabarito: oficial (2SEM24), sem anuladas; Q44 RETIFICADA para C (a conta confirma: 30/992 ≈ 3,0%).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import A, carregar, enun, tabela, colunas, completar, trecho

ID = "fatec-2024-2sem"
META = {
    "id": ID,
    "banca": "FATEC",
    "ano": 2024,
    "semestre": 2,
    "titulo": "Vestibular FATEC, 2º semestre de 2024",
    "fonte": "Centro Paula Souza",
    "dataExame": "2024-06-30",
    "duracaoMinutos": 300,
    "tema": "América Latina",
    "pdf": f"assets/provas/{ID}.pdf",
}

R = carregar(ID)
MULTI = ["multidisciplinar"]


def T(pag, inicio, fim, paragrafos=()):
    return trecho(ID, pag, inicio, fim, paragrafos)


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


def it(texto, *termos):
    for t in termos: texto = texto.replace(t, f"<em>{t}</em>")
    return texto


def sub(texto):
    """Índices químicos que o texto do PDF perde (CO2 → CO<sub>2</sub>)."""
    for a, b in (("CO2", "CO<sub>2</sub>"), ("NH3", "NH<sub>3</sub>"), ("C8H18", "C<sub>8</sub>H<sub>18</sub>"), ("CH3OH", "CH<sub>3</sub>OH")):
        texto = texto.replace(a, b)
    return texto


def alts(*textos):
    return dict(zip("ABCDE", textos))


# ---------- textos compartilhados ----------
AMLAT = (chamada("Leia o texto para responder às questões 02 e 03.")
         + apoio(*T(2, "A expressão América Latina está", "Belize não a integram."))
         + fonte("RODRIGUES, L. S. Topônimos latino-americanos: um estudo etimológico. In: Revista de Estudos de Linguagem. Vol. 26, n.º 3. Belo Horizonte: UFMG, pp.1031-1055. Adaptado."))
P2 = p("Assinale a alternativa em que é apresentado um país da América Latina cujo nome tem o maior número de anagramas.")

PANAMA = (chamada("Leia o texto para responder às questões de 06 a 08.")
          + apoio(*T(4, "O Canal do Panamá é uma construção", "transferida para o Panamá.", ["A França iniciou"]))
          + url("http://tinyurl.com/ysw4r7b3", "23.01.2024"))
P6 = p("Segundo o texto, é possível afirmar corretamente que a mencionada obra de engenharia atingiu seu propósito por meio de construções de eclusas e comportas, que se baseiam")

PIB = (chamada("Leia o texto para responder às questões de 09 a 11.")
       + p(*T(5, "A Comissão Econômica para a América Latina", "alguns dos países dessa região."))
       + tabela(["País", "Crescimento do PIB (%) – Ano de 2023", "Crescimento do PIB (%) – Ano de 2024"],
                [["Argentina", "–2,5", "–1,0"], ["Brasil", "3,0", "1,6"], ["Costa Rica", "4,9", "3,8"], ["El Salvador", "2,3", "2,0"], ["Haiti", "–1,8", "1,0"], ["Jamaica", "2,1", "1,9"],
                 ["México", "3,6", "2,5"], ["Panamá", "6,1", "4,2"], ["Peru", "0,3", "2,4"], ["Suriname", "2,0", "3,0"], ["Uruguai", "1,0", "3,2"], ["Venezuela", "3,0", "4,0"]])
       + fonte("Fonte dos dados: &lt;http://tinyurl.com/3nejy632&gt; Acesso em: 12.01.2024."))
P9 = p("Se considerarmos apenas os países dessa lista que fazem parte da América do Sul, podemos calcular a média aritmética referente à projeção do crescimento percentual desses países para o ano de 2024.",
       "Assinale, dentre as alternativas apresentadas, aquela na qual há um país da América do Sul cujo crescimento do PIB, em 2024, é mais próximo de M.")

LATAM24 = (chamada("Leia o texto para responder às questões 13 e 14.")
           + apoio("<strong>Latin America in 2024</strong>", "<em>Despite mediocre growth, political risk is declining and cautious optimism is increasingly warranted.</em>",
                   *T(6, "SÃO PAULO — Despite a challenging", "Latin America in recent years."))
           + url("https://tinyurl.com/2zpnfdct", "16.01.2024"))
P13 = p("A partir da leitura do texto, infere-se que, na América Latina,")

EFUEL = (chamada("Leia o texto para responder às questões de 15 a 18.")
         + p(*[sub(it(x, "e-fuel")) for x in T(7, "No extremo sul do Chile, foi inaugurada", "conforme o esquema.", ["O vento é responsável", "Uma estação aspira"])])
         + "[[fig:1]]" + fonte("Fonte dos dados: &lt;http://tinyurl.com/2p853jje&gt; Acesso em: 23.01.2024."))
EFUEL_IMG = figs(("q15", "Esquema “Produção de gasolina sintética”. A água fornece H₂; do ar, pelo processo (I), obtém-se CO₂ (líquido). Os dois entram na reação (II): x CO₂ + y H₂ → 1 CH₃OH + 1 H₂O, que produz metanol sintético (CH₃OH). O metanol vira gasolina sintética. A combustão incompleta da gasolina gera CO, que volta (reaproveitamento) para a produção de metanol; a combustão completa gera CO₂, que volta para o CO₂ (líquido)."))
P15 = p("Assinale a alternativa que contém o nome correto da mudança de estado físico, ocorrida com o dióxido de carbono, no processo indicado em (I).")

JUAREZ = (chamada("Leia o texto para responder às questões de 28 a 30.")
          + apoio(*T(12, "Em 1977, o Centro Médico Especializado", "registrado nas Américas.", ["Os grânulos desse", "Aparentemente, o objetivo", "Esse é um dos maiores"]))
          + fonte("Fonte dos dados: &lt;http://tinyurl.com/ym4uh6su&gt; e &lt;http://tinyurl.com/bddbw4y6&gt; Acesso em: 10.01.2024. Adaptado."))
P28 = p("Assinale a alternativa que indica, em metros cúbicos, o volume total de grânulos do radioisótopo mencionado no texto. (Adote π = 3)")

MAPA = (chamada("Leia os textos para responder às questões 34 e 35.")
        + p("<strong>Texto I</strong>") + "[[fig:1]]" + url("http://tinyurl.com/uptfzk7z", "16.02.2024", "")
        + apoio("<strong>Texto II</strong>", *T(14, "Este não é um mapa como os convencionais", "como sedes de sua sociedade.", ["Seu autor, Joaquín", "Em sua obra, esse autor"]))
        + fonte("SALES, C.M. “Cartografia, Arte e Visões de Mundo na Reprodução do ‘Mapa Invertido da América do Sul’”. In: Espaço e Cultura, UERJ, RJ, n.39, p.158. Adaptado."))
MAPA_IMG = figs(("q34", "Desenho de Joaquín Torres-García, de 1943: o mapa da América do Sul de cabeça para baixo, com a ponta sul do continente em cima, junto à inscrição “Polo S”, e a linha do Equador embaixo. Em volta, um sol, uma lua, estrelas, um barco a vela, um peixe e ondas. Sobre Montevidéu, as coordenadas “S. 34°41′ W 56°9′”. Assinatura “JTG 43”."))
MAPA_NEGRITO = {"Este não é um mapa como os convencionais, que": "Este não é um mapa como os convencionais, <strong>que</strong>",
                "publicou-o em 1943": "publicou-<strong>o</strong> em 1943", "em Montevidéu, o qual": "em Montevidéu, <strong>o qual</strong>",
                "comportamento que ele chamou": "comportamento que <strong>ele</strong> chamou", "capitais latinas que não": "capitais latinas <strong>que</strong> não"}
for a, b in MAPA_NEGRITO.items():
    assert a in MAPA, a
    MAPA = MAPA.replace(a, b)
P34 = p("No texto apresentado, o(s) pronome(s)")

SISTEMAS = (chamada("Leia o texto para responder às questões 46 e 47.")
            + apoio("<strong>What´s the Difference Between the Metric and Imperial System?</strong>", "Aug 11, 2021",
                    *T(19, "While most of the world uses", "different meanings in different places.", ["What Is the Metric System?", "The Metric System, or SI", "What Is the Imperial System?", "The British Imperial System was"]))
            + url("https://tinyurl.com/yc5v9dh7", "16.02.2024"))
for t in ("What Is the Metric System?", "What Is the Imperial System?"):
    SISTEMAS = SISTEMAS.replace(t, f"<strong>{t}</strong>")
P46 = p("Baseando-se no texto, assinale a alternativa correta.")

UPANO = (chamada("Leia o texto para responder às questões de 49 a 51.")
         + apoio("<strong>Huge ancient lost city found in the Amazon</strong>",
                 *T(20, "The discovery changes what we know", "focussed on agriculture.", ["While we knew about cities", "“It changes the way", "The city was built", "Dr Dorison said", "The societies were clearly"]))
         + url("https://tinyurl.com/37cbjmbk", "20.01.2024"))
P49 = p("De acordo com o texto, o que pode ter levado à destruição da sociedade em questão foi")

Q = {
1: {"materia": "História", "assunto": "Pré-História", "tags": ["povoamento da América"],
    "enunciado": p("<strong>OS CAMINHOS DO SER HUMANO PARA A AMÉRICA</strong>") + "[[fig:1]]"
                 + fonte("Fonte dos dados: &lt;http://tinyurl.com/yc26bf4v&gt; Acesso em: 07.02.2024.") + p("A leitura do mapa permite concluir, corretamente, que"),
    "imagens": figs(("q01", "Mapa-múndi “Os caminhos do ser humano para a América”, com setas das prováveis rotas. Da África, perto do Deserto do Saara, saem rotas para a Europa e para a Ásia. Da Sibéria, uma rota atravessa o Estreito de Bering até o Alasca e desce pela América do Norte até a América do Sul. Do sudeste asiático, pelas Filipinas e Nova Guiné, e da Polinésia saem rotas pelo Oceano Pacífico, com desenhos de barcos, que chegam à América do Sul e à América Central. Escala de 3 020 km.")),
    "explicacao": "<p>O mapa mostra que as rotas partem de um ponto comum, na África, e seguem por caminhos diferentes (por Bering, pelo Pacífico) até a América. Alternativa <strong>B</strong>.</p><p>As rotas que chegam à América do Norte vêm da Sibéria, pelo Estreito de Bering, e não da Oceania (A). A Europa não é o ponto de partida (C). O mapa não mostra rotas que saem da América Latina (D). E há rotas por terra, como a de Bering (E).</p>"},
2: {"materia": "Matemática", "assunto": "Análise combinatória", "tags": ["anagramas"],
    "enunciado": AMLAT + P2,
    "explicacao": "<p>Pelo texto, Canadá não é da América Latina, e Guiana e Jamaica não a integram. Restam México e Panamá. MÉXICO tem 6 letras diferentes: 6! = 720 anagramas. PANAMÁ tem 6 letras com o A repetido 3 vezes: 6! ÷ 3! = 120. O maior é o <strong>México</strong>. Alternativa <strong>D</strong>.</p><p>Guiana e Jamaica também têm letras repetidas e, de qualquer forma, não são latino-americanos (B e C).</p>"},
3: {"materia": "Raciocínio lógico", "assunto": "Lógica", "tags": ["conjuntos"],
    "enunciado": AMLAT + p("Considere os conjuntos:", "• X = {x | x é um país da América Latina};", "• Y = {y | y é um país cujo idioma oficial não é o espanhol}.",
                           "Se um país pertence ao conjunto C = Y – X, então, geograficamente, esse país"),
    "explicacao": "<p>Y − X reúne os países que estão em Y (idioma oficial não é o espanhol) e não estão em X (não são da América Latina). Exemplos: Guiana, Suriname, Jamaica. Alternativa <strong>E</strong>.</p><p>O conjunto não é vazio (A), e os países de Y − X não estão na América Latina nem falam espanhol (B, C e D).</p>"},
4: {"materia": "Biologia", "assunto": "Zoologia", "tags": ["mamíferos"],
    "enunciado": p("A América Latina é uma região rica em biodiversidade, abrigando uma grande variedade de espécies de mamíferos, como as capivaras (<em>Hydrochoerus hydrochaeris</em>), maiores roedores vivos do mundo.",
                   "Entre as características que pertencem exclusivamente a classe dos animais citados no texto, destaca-se corretamente a presença de"),
    "explicacao": "<p>Pelos, glândulas mamárias e diafragma são exclusivos dos mamíferos. Alternativa <strong>E</strong>.</p><p>Mamíferos não têm escamas (A e B), têm coração com quatro cavidades, não três (C), e são endotérmicos, não ectotérmicos (A e D).</p>"},
5: {"materia": "História", "assunto": "História contemporânea", "tags": ["Revolução Cubana"],
    "explicacao": "<p>Colônia espanhola até 1898, independente com a intervenção dos EUA, sob a ditadura de Fulgêncio Batista: é Cuba. O movimento de oposição foi a <strong>Revolução Cubana</strong> (1959), liderada por Fidel Castro. Alternativa <strong>D</strong>.</p><p>O Haiti foi colônia francesa e ficou independente em 1804 (A). Demerara fica na atual Guiana, colônia britânica (B). E as revoluções Francesa e Russa aconteceram na Europa (C e E).</p>"},
6: {"materia": "Física", "assunto": "Hidrostática", "tags": ["vasos comunicantes", "empuxo"],
    "enunciado": PANAMA + P6,
    "explicacao": "<p>Uma eclusa é uma câmara entre dois níveis de água. Ao abrir as comportas, a água passa de uma câmara para a outra até os níveis se igualarem: são <strong>vasos comunicantes</strong>. E o navio sobe ou desce porque flutua, sustentado pelo <strong>empuxo</strong> (princípio de Arquimedes). Alternativa <strong>C</strong>.</p><p>Termodinâmica, inércia, momento linear e óptica não explicam o funcionamento de uma eclusa (A, B, D e E).</p>"},
7: {"materia": "Geografia", "assunto": "Transportes e logística", "tags": ["Canal do Panamá"],
    "enunciado": PANAMA + p("Com base no texto, é correto afirmar que"),
    "explicacao": "<p>Um navio que vai da costa leste para a costa oeste dos EUA pelo canal evita a volta pelo Cabo Horn, no extremo sul da América, e percorre uma distância muito menor. Alternativa <strong>E</strong>.</p><p>Foi o Panamá que se tornou independente da Colômbia, com incentivo dos EUA (A). Em 1999, os EUA transferiram o canal ao Panamá, não a França aos EUA (B). As eclusas ficam no próprio canal, entre o Atlântico e o Pacífico (C). E o Cabo Horn fica no extremo sul do continente, não no Canadá (D).</p>"},
8: {"materia": "Física", "assunto": "Cinemática", "tags": ["velocidade média"],
    "enunciado": PANAMA + p("Antes da construção do canal, um navio cargueiro, que fosse do ponto Atlântico do Canal do Panamá até o ponto Pacífico desse canal, precisaria passar pelo Cabo Horn, conforme descrito no texto.",
                            "Suponha que esse navio conseguisse percorrer o trecho, citado no parágrafo anterior, navegando, sem paradas ou intercorrências, a uma velocidade média de cruzeiro de aproximadamente 20 nós.",
                            "Adotando 1 nó como 1,9 km/h, é correto afirmar que o navio faria essa viagem, aproximadamente, em"),
    "explicacao": "<p>A velocidade é 20 · 1,9 = 38 km/h. A rota pelo Cabo Horn tem cerca de 19 000 km: t = 19 000 ÷ 38 = 500 h. Em dias: 500 ÷ 24 ≈ <strong>20 dias</strong>. Alternativa <strong>D</strong>.</p><p>As alternativas em horas são pequenas demais (A, B e C). E 10 dias seria a metade do tempo (E).</p>"},
9: {"materia": "Matemática", "assunto": "Estatística", "tags": MULTI + ["média aritmética"],
    "enunciado": PIB + P9,
    "explicacao": "<p>Os países da lista que ficam na América do Sul são Argentina (–1,0), Brasil (1,6), Peru (2,4), Suriname (3,0), Uruguai (3,2) e Venezuela (4,0). A média é 13,2 ÷ 6 = 2,2. Entre as alternativas, o país sul-americano mais próximo de 2,2 é o <strong>Peru</strong> (2,4). Alternativa <strong>D</strong>.</p><p>Costa Rica, El Salvador e Jamaica não ficam na América do Sul (A, B e C). E o Uruguai (3,2) fica mais longe da média (E).</p>"},
10: {"materia": "Matemática", "assunto": "Porcentagem", "tags": ["aumentos sucessivos"],
     "enunciado": PIB + p("Considere que o PIB da Venezuela, no ano de 2022, foi estimado em cerca de US$ 196 bilhões. Então, de acordo com as previsões da CEPAL, a projeção para o ano de 2024, em bilhões, deve ser próxima de"),
     "explicacao": "<p>A Venezuela cresce 3,0% em 2023 e 4,0% em 2024: 196 · 1,03 · 1,04 = 201,88 · 1,04 ≈ <strong>209,96</strong>. Alternativa <strong>A</strong>.</p><p>Somar 7% de uma vez dá 209,72, perto de B, mas os aumentos são sucessivos. Aplicar só um dos anos dá valores menores (C e D).</p>"},
11: {"materia": "Matemática", "assunto": "Interpretação de dados", "tags": MULTI + ["tabelas"],
     "enunciado": PIB + p("A partir dos dados apresentados no quadro, o país que teve a maior variação percentual no crescimento do PIB, de 2023 a 2024, foi"),
     "explicacao": "<p>As variações de 2023 para 2024: Haiti, de –1,8 para 1,0 (2,8 pontos); Argentina, de –2,5 para –1,0 (1,5); Panamá, de 6,1 para 4,2 (–1,9); Brasil, de 3,0 para 1,6 (–1,4); México, de 3,6 para 2,5 (–1,1). A maior é a do <strong>Haiti</strong>. Alternativa <strong>E</strong>.</p><p>As outras alternativas têm variações menores (A, B, C e D).</p>"},
12: {"materia": "Geografia", "assunto": "Geopolítica", "tags": ["república de bananas", "imperialismo"],
     "enunciado": apoio(*[it(x, "O Almirante") for x in T(6, "O termo “república de bananas” foi cunhado", "fora da América Latina.", ["Até o fim do século XIX", "O termo acabou ganhando", "O que chama a atenção"])])
                  + url("http://tinyurl.com/36j5hyn6", "26.01.2024") + p("De acordo com o texto, é correto afirmar que"),
     "explicacao": "<p>O texto diz que a expressão passou a se referir a países marcados pela monocultura, com instituições fracas e em que empresas estrangeiras influenciam as decisões nacionais. Alternativa <strong>B</strong>.</p><p>Honduras fica na América Central, não na Ásia (A). Porter era escritor, não presidente (C). Os anglo-saxões não aplicam a expressão a países fora da América Latina (D). E o texto não fala de países africanos (E).</p>"},
13: {"materia": "Inglês", "assunto": "Interpretação de texto",
     "enunciado": LATAM24 + P13,
     "explicacao": "<p>O texto fala em “cautious optimism” e diz que o crescimento de 2023 (2,2%) foi “somewhat better than the 1.7% initially projected”: há <strong>um certo otimismo</strong> diante de um crescimento melhor do que o esperado. Alternativa <strong>D</strong>.</p><p>O risco político está diminuindo (A), o crescimento é positivo (B), o tom não é de pessimismo (C), e o crescimento ficou abaixo da média mundial de 3,2% (E).</p>"},
14: {"materia": "Inglês", "assunto": "Coesão e referência", "tags": ["conectivos"],
     "enunciado": p("A palavra <em>Despite</em>, no texto, é usada para"), "apoio_de": (13, P13),
     "explicacao": "<p><em>Despite</em> significa “apesar de”: “apesar do crescimento medíocre, o risco político diminui”; “apesar de um cenário desafiador, 2023 não foi um ano ruim”. Ela <strong>contrapõe informações</strong>. Alternativa <strong>B</strong>.</p><p>A palavra não retoma causas (A), não introduz exemplos (C), não suprime o tom negativo (D) nem marca consequências (E).</p>"},
15: {"materia": "Química", "assunto": "Substâncias e misturas", "tags": ["mudanças de estado físico"],
     "enunciado": EFUEL + P15, "imagens": EFUEL_IMG,
     "explicacao": "<p>Em (I), o CO₂ separado do ar, que está no estado gasoso, passa ao estado líquido: é a <strong>condensação</strong> (liquefação). Alternativa <strong>A</strong>.</p><p>Vaporização e ebulição são a passagem do líquido para o gás (B e E). Sublimação é do sólido direto para o gás (C). E fusão é do sólido para o líquido (D).</p>"},
16: {"materia": "Química", "assunto": "Reações químicas", "tags": ["balanceamento"],
     "enunciado": p("Considerando a equação química (II), que representa a reação de produção de metanol, os valores de <em>x</em> e <em>y</em>, que tornam a equação corretamente balanceada, são, respectivamente,"),
     "apoio_de": (15, P15),
     "explicacao": "<p>Do lado direito há 1 C, 4 H + 2 H = 6 H e 1 + 1 = 2 O. Então x = 1 (1 C e 2 O no CO₂) e y = 3 (3 H₂ = 6 H): CO₂ + 3 H₂ → CH₃OH + H₂O. Alternativa <strong>C</strong>.</p><p>As outras combinações deixam o carbono, o hidrogênio ou o oxigênio desbalanceados.</p>"},
17: {"materia": "Química", "assunto": "Química ambiental", "tags": ["carbono neutro"],
     "enunciado": p(sub("Um processo neutro em carbono ou de carbono neutro é aquele que não contribui para o aumento da quantidade de carbono emitido na atmosfera na forma de gases, como CO e CO2."),
                    "Podemos concluir corretamente que a produção da gasolina sintética pode ser considerada neutra em carbono, já que, de acordo com o esquema, o hidrogênio e o dióxido de carbono são transformados em gasolina sintética, cuja"),
     "apoio_de": (15, P15),
     "alternativas": alts("combustão libera água para a atmosfera.", "combustão produz carbono e gás hidrogênio.", "combustão não libera energia.", "produção reaproveita o carbono gerado no processo.", "produção gera metanol, composto não tóxico."),
     "explicacao": "<p>No esquema, o CO e o CO₂ da combustão voltam para a produção de metanol. O carbono que a queima libera é o mesmo que foi retirado do ar: a <strong>produção reaproveita o carbono</strong>. Alternativa <strong>D</strong>.</p><p>Liberar água não tem relação com o carbono (A). A combustão produz CO e CO₂, não carbono e hidrogênio (B), e libera energia (C). E o metanol é tóxico (E).</p>"},
18: {"materia": "Química", "assunto": "Reações químicas", "tags": ["estequiometria"],
     "enunciado": p(sub("O combustível sintético emite, em sua queima, apenas 10 % da quantidade de CO2 emitida na combustão de combustíveis fósseis."),
                    sub("Esta equação química balanceada representa a queima da gasolina (C8H18) de origem fóssil."),
                    "\\[\\text{C}_8\\text{H}_{18}(\\text{g}) + \\tfrac{25}{2}\\,\\text{O}_2(\\text{g}) \\rightarrow 8\\,\\text{CO}_2(\\text{g}) + 9\\,\\text{H}_2\\text{O}(\\text{g})\\]",
                    sub("Considere que um motor realizou a queima de 114 g de C8H18 (M = 114 g/mol) de origem fóssil."),
                    sub("Caso esse mesmo motor utilizasse gasolina sintética, a massa de CO2 (M = 44 g/mol) emitida, em gramas, seria de, aproximadamente,")),
     "apoio_de": (15, P15),
     "alternativas": alts("523.", "352.", "207.", "35.", "22."),
     "explicacao": "<p>114 g de octano são 1 mol, que produz 8 mol de CO₂: 8 · 44 = 352 g. A gasolina sintética emite só 10% disso: 0,1 · 352 ≈ <strong>35 g</strong>. Alternativa <strong>D</strong>.</p><p>352 g é a emissão da gasolina fóssil (B). E 22 g seria meio mol de CO₂, sem relação com a conta (E).</p>"},
19: {"materia": "Biologia", "assunto": "Ecologia", "tags": ["controle biológico", "plantas daninhas"],
     "enunciado": apoio(*[it(x, "Digitaria insularis") for x in T(8, "A América Latina é apontada pela Organização", "a produção de suas sementes.", ["Uma das espécies infestantes", "Nesses casos, o controle"])])
                  + url("http://tinyurl.com/4rsy2rpd", "30.01.2024") + p("É correto afirmar que o método de controle biológico, citado no texto,"),
     "alternativas": alts("colabora para o aumento da quantidade de resíduos tóxicos de defensivos agrícolas nos alimentos cultivados com as espécies infestantes.",
                          "permite o desenvolvimento e o aumento da taxa de dispersão das espécies infestantes nocivas à agricultura de soja, milho e trigo.",
                          "introduz genes de resistência aos herbicidas nas PDDC, responsáveis pelos principais problemas da agricultura mundial.",
                          "impede o controle e o combate das pragas nas plantações, facilitando a dispersão das sementes das espécies invasoras.",
                          "consiste no uso de organismos para reduzir ou erradicar, nas plantações, a infestação de espécies nocivas."),
     "explicacao": "<p>O controle biológico usa seres vivos, como os fungos citados, para conter a praga: eles inibem o crescimento do capim-amargoso e diminuem suas sementes. Alternativa <strong>E</strong>.</p><p>O método diminui o uso de defensivos (A), reduz a dispersão da praga (B e D) e não introduz genes nas plantas daninhas (C).</p>"},
20: {"materia": "Biologia", "assunto": "Fisiologia humana", "tags": ["proteínas"],
     "enunciado": apoio(*T(9, "Segundo a FAO, a produção de proteína animal", "leite e ovos."))
                  + url("http://tinyurl.com/4n5fyxxp", "11.02.2024")
                  + p("Segundo especialistas, no organismo humano, esse tipo de nutriente desempenha várias funções biológicas importantes, como as realizadas"),
     "alternativas": alts("pela hemoglobina, que provoca a coagulação e que estimula a reparação dos vasos sanguíneos lesados.",
                          "pelas enzimas, que se ligam aos gases respiratórios e que distribuem o gás carbônico dos alvéolos pulmonares a todas as células do corpo.",
                          "pelo colágeno, que atua como catalisador de reações químicas e que diminui a elasticidade e a hidratação da pele e das cartilagens humanas.",
                          "pelas imunoglobulinas, que agem na defesa e atuam contra os antígenos que entram no organismo por meio de vacinação ou de uma infecção ativa.",
                          "pela insulina, que atua no controle da ovulação, no desenvolvimento de características sexuais secundárias femininas e pelo controle do ciclo menstrual."),
     "explicacao": "<p>As imunoglobulinas são os anticorpos, proteínas que atuam na defesa contra antígenos, seja na vacinação, seja numa infecção. Alternativa <strong>D</strong>.</p><p>A hemoglobina transporta oxigênio, e quem atua na coagulação são as plaquetas e os fatores de coagulação (A). As enzimas catalisam reações, e quem transporta os gases é a hemoglobina (B). O colágeno dá firmeza e elasticidade à pele (C). E quem controla a ovulação e o ciclo são os hormônios sexuais, não a insulina (E).</p>"},
21: {"materia": "Física", "assunto": "Cinemática", "tags": MULTI + ["fusos horários"],
     "enunciado": apoio(*T(9, "A cidade mexicana de La Paz", "segundo ranking de uma revista estadunidense."))
                  + url("http://tinyurl.com/mtesk8wu", "14.01.2024")
                  + p("O quadro apresenta as coordenadas de tempo em GMT (Greenwich Mean Time), que são utilizadas para definir os fusos horários.")
                  + tabela(["Lugares", "Fuso horário na região"], [["La Paz (México)", "– 7 GMT"], ["PNP (Chile)", "– 4 GMT"]])
                  + p("Suponha que seja possível embarcar em um voo direto entre esses dois lugares e que a aeronave faça esse trajeto com velocidade média de 900 km/h.",
                      "Se um passageiro embarcasse em La Paz às 09h45min, ele desembarcaria no PNP, aproximadamente, às"),
     "alternativas": alts("6 h 45 min.", "12 h 45 min.", "16 h 45 min.", "19 h 45 min.", "22 h 45 min."),
     "explicacao": "<p>O voo dura 9 000 ÷ 900 = 10 h. Saindo às 9h45 de La Paz, chega às 19h45 no horário de La Paz. O PNP está 3 horas à frente (–4 contra –7 GMT): 19h45 + 3 h = <strong>22h45</strong>. Alternativa <strong>E</strong>.</p><p>19h45 esquece o fuso (D), e 16h45 subtrai as 3 horas em vez de somar (C).</p>"},
22: {"materia": "Raciocínio lógico", "assunto": "Lógica", "tags": ["proporção"],
     "enunciado": p("O congestionamento de tráfego é um desafio para a saúde econômica da América Latina. Investir em transporte público pode ser uma solução, uma vez que essa modalidade de transporte pode ser vista como uma maneira inteligente de usar o espaço público.",
                    "Dados apontam que um carro de médio porte ocupa 8 m² e transporta até 5 pessoas, enquanto um ônibus básico ocupa 56 m² e transporta até 70 pessoas.",
                    "Logo, para transportar simultaneamente 70 pessoas, a quantidade mínima de carros necessária é de ___<strong>I</strong>___, o que equivale ao espaço público ocupado por ___<strong>II</strong>___ ônibus.",
                    "Assinale a alternativa que completa corretamente os espaços numerados."),
     "alternativas": colunas(["I", "II"], [["28", "1"], ["14", "4"], ["14", "2"], ["7", "2"], ["7", "4"]]),
     "explicacao": "<p>Para 70 pessoas, são 70 ÷ 5 = 14 carros, que ocupam 14 · 8 = 112 m². Um ônibus ocupa 56 m², então 112 m² é o espaço de 112 ÷ 56 = 2 ônibus. Alternativa <strong>C</strong>.</p><p>28 carros levariam 140 pessoas (A). E 7 carros só levariam 35 (D e E).</p>"},
23: {"materia": "Matemática", "assunto": "Funções", "tags": ["função do 1º grau", "frações"],
     "enunciado": p("A taxa bruta de matrícula é o indicador mais usado em todo o mundo para monitorar o acesso à educação. O gráfico apresentado foi elaborado utilizando uma aproximação linear para os valores dessa taxa de matrícula no ensino superior.")
                  + "[[fig:1]]" + fonte("Fonte dos dados: &lt;http://tinyurl.com/4w8m89rz&gt; Acesso em: 12.01.2024.")
                  + p("De acordo com o gráfico, pode-se concluir, corretamente, que a taxa bruta de matrículas no ensino superior, estimada no ano de"),
     "imagens": figs(("q23", "Gráfico de linha “Taxa bruta de matrícula no ensino superior na América Latina e Caribe de 2000 a 2020”, em %. Uma reta crescente parte de 23,1 em 2000 e chega a 54,1 em 2020, com pontos marcados em 2005, 2010 e 2015.")),
     "alternativas": alts("2000, corresponde à metade daquela aferida no ano de 2010.", "2005, é um número que pertence ao conjunto dos números não positivos.",
                          "2010, equivale ao mesmo número representado pela fração irredutível \\(\\dfrac{193}{500}\\).", "2015, quando comparada com aquela medida no ano de 2000, é três vezes maior.",
                          "2020, mostra uma desaceleração no número de matriculados em relação ao ano de 2015."),
     "explicacao": "<p>Como a aproximação é linear, 2010 fica no meio: (23,1 + 54,1) ÷ 2 = 38,6%. E 38,6% = 0,386 = 386/1 000 = <strong>193/500</strong>. Alternativa <strong>C</strong>.</p><p>23,1 não é metade de 38,6 (A). A taxa de 2005 (30,85) é positiva (B). A de 2015 (46,35) é cerca de duas vezes a de 2000, não três (D). E a reta continua subindo no mesmo ritmo (E).</p>"},
24: {"materia": "Física", "assunto": "Energia", "tags": ["energia cinética"],
     "enunciado": p(*T(10, "A Organização Pan-Americana de Saúde", "periodicamente calibrados.", ["Um dos principais motivos"]),
                    "Uma história clássica, ocorrida em 2021, foi a suspensão da Carteira Nacional de Habilitação (CNH) de um motociclista que teria percorrido uma estrada a cerca de 900 km/h (≅ 250 m/s).",
                    "Suponha que ele estivesse realmente a essa velocidade e o conjunto moto-piloto tivesse massa igual a 200 kg.",
                    "Despreze quaisquer ações dissipativas e assinale a alternativa que apresenta, aproximadamente, o valor da energia cinética, em joules, envolvida no conjunto moto-piloto no momento do registro.",
                    "Dado: \\(E_c = \\dfrac{m \\cdot v^2}{2}\\)"),
     "alternativas": alts("2,8 × 10<sup>8</sup>", "8,6 × 10<sup>7</sup>", "1,4 × 10<sup>7</sup>", "6,2 × 10<sup>6</sup>", "5,0 × 10<sup>5</sup>"),
     "explicacao": "<p>E<sub>c</sub> = 200 · 250² ÷ 2 = 100 · 62 500 = 6 250 000 J ≈ <strong>6,2 × 10⁶ J</strong>. Alternativa <strong>D</strong>.</p><p>Usar 900 km/h sem converter para m/s dá 8,1 × 10⁷, perto de B. E 5,0 × 10⁵ esquece de elevar a velocidade ao quadrado (E).</p>"},
25: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": ["doença de Chagas", "protozooses"],
     "enunciado": apoio(*T(11, "Segundo a OPAS, na América Latina", "ausência de sintomas clínicos."))
                  + url("http://tinyurl.com/2s4fbhd2", "30.01.2024")
                  + p("Para prevenir, detectar, tratar essa enfermidade e quebrar a cadeia de transmissão, é importante saber que essa doença se caracteriza por ser"),
     "alternativas": alts("uma infecção bacteriana transmitida por contato direto com os indivíduos contaminados, a qual causa coceira e infecções generalizadas.",
                          "uma infecção cutânea micótica debilitante, a qual causa necroses nos tecidos epiteliais, nos ossos, nos tecidos moles e gera problemas cardíacos.",
                          "uma doença viral transmitida aos seres humanos por meio de mordidas de animais infectados, a qual pode ocasionar convulsões e problemas pulmonares.",
                          "uma protozoose transmitida aos seres humanos por meio de insetos hematófagos contaminados, a qual pode ser fatal quando os sintomas se desenvolvem.",
                          "uma verminose transmitida aos seres humanos pela picada de fêmeas infectadas de mosquitos, a qual pode provocar hemorragias, patologias hepáticas e morte."),
     "explicacao": "<p>A doença de Chagas é causada pelo protozoário <em>Trypanosoma cruzi</em> e transmitida pelo barbeiro, um inseto que se alimenta de sangue. Pode ser fatal, sobretudo pelas lesões no coração. Alternativa <strong>D</strong>.</p><p>Ela não é bacteriana (A), nem causada por fungo (B), nem viral transmitida por mordida, que é a raiva (C). E não é verminose transmitida por mosquito (E).</p>"},
26: {"materia": "Português", "assunto": "Interpretação de texto", "tags": ["Eduardo Galeano"],
     "enunciado": chamada("Leia uma passagem da obra <em>O Livro dos Abraços</em>, de Eduardo Galeano, escritor uruguaio que retratou a América Latina entre as décadas de 1970 e 1980, para responder às questões 26 e 27.")
                  + apoio(*T(11, "A tevê dispara imagens", "os preços já os proíbem.", ["Na América Latina, a liberdade"]))
                  + p("Segundo o texto apresentado, é correto afirmar que"),
     "alternativas": alts("a televisão, como ferramenta democrática de divulgação de informação, representa diferentes expressões culturais.",
                          "a apropriação cultural ocorre nas gerações anteriores ao desenvolvimento da cultura de massa, fazendo-as se engajarem em movimentos sociais.",
                          "países da América Latina têm acesso pleno à liberdade de expressão, valendo-se de recursos sonoros e escritos para se comunicar livremente.",
                          "o incentivo ao desenvolvimento cultural, à liberdade de expressão e à mobilização social ocorre devido ao aparecimento da televisão e do rádio.",
                          "a mídia de massa gera um alheamento social, resultado da falta de acesso à cultura e da difusão de uma cultura hegemônica."),
     "explicacao": "<p>Para Galeano, a TV espalha “emoções importadas”, cria jovens “treinados para contemplar a vida em vez de fazê-la”, e os livros são proibidos pelo preço: a mídia de massa gera <strong>alheamento</strong>, com cultura hegemônica e pouco acesso à cultura. Alternativa <strong>E</strong>.</p><p>O texto critica a TV, não a vê como democrática (A e D), não fala das gerações anteriores (B) e diz que a liberdade de expressão se resume a resmungos (C).</p>"},
}

NUC = lambda a, z, s: f"{{}}^{{{a}}}_{{{z}}}\\mathit{{{s}}}"
Q.update({
27: {"materia": "Português", "assunto": "Figuras de linguagem", "tags": ["metáfora"],
     "enunciado": p("O uso de conotação é recorrente, no texto apresentado, devido a seu caráter literário.", "Isso fica evidente na oração “o planeta inteiro é um vasto subúrbio de Dallas”, que é uma"),
     "apoio_de": (26, p("Segundo o texto apresentado, é correto afirmar que")),
     "alternativas": alts("metáfora.", "zeugma.", "personificação.", "paradoxo.", "catacrese."),
     "explicacao": "<p>O planeta é chamado de “subúrbio de Dallas” (cidade dos EUA e nome de uma série de TV famosa): uma comparação sem conectivo, que diz que o mundo todo ficou parecido com os EUA da televisão. É uma <strong>metáfora</strong>. Alternativa <strong>A</strong>.</p><p>Zeugma é omitir um termo já dito (B). Personificação dá traços humanos a seres não humanos (C). Paradoxo une ideias contraditórias (D). E catacrese é usar uma palavra fora do sentido por falta de outra (E).</p>"},
28: {"materia": "Matemática", "assunto": "Geometria espacial", "tags": ["volume do cilindro", "notação científica"],
     "enunciado": JUAREZ + P28,
     "alternativas": alts(*[f"{v} × 10<sup>–6</sup>" for v in ("1,0", "1,5", "3,0", "4,5", "6,0")]),
     "explicacao": "<p>Cada grânulo é um cilindro de raio 0,5 mm e altura 1 mm: V = π · r² · h = 3 · 0,25 · 1 = 0,75 mm³. Os 6 000 grânulos somam 4 500 mm³. Como 1 mm³ = 10⁻⁹ m³, o total é 4 500 × 10⁻⁹ = <strong>4,5 × 10⁻⁶ m³</strong>. Alternativa <strong>D</strong>.</p><p>Usar o diâmetro (1 mm) como raio dá 18 000 mm³ = 1,8 × 10⁻⁵ m³, fora das alternativas. E 6,0 × 10⁻⁶ conta os grânulos como cubos de 1 mm³ (E).</p>"},
29: {"materia": "Química", "assunto": "Estrutura atômica", "tags": MULTI + ["radioatividade", "emissão beta"],
     "enunciado": p(f"O radioisótopo cobalto-60 \\(\\left({NUC(60, 27, 'Co')}\\right)\\) emite uma partícula beta negativa, transformando-se no isótopo estável níquel-60 \\(\\left({NUC(60, 28, 'Ni')}\\right)\\).",
                    "A alternativa que contém a equação nuclear correta para representar a emissão descrita é"),
     "apoio_de": (28, P28),
     "alternativas": {"A": f"\\({NUC(60, 27, 'Co')} + {NUC(0, -1, 'β')} \\rightarrow {NUC(60, 28, 'Ni')}\\)".replace("\\mathit{β}", "\\beta"),
                      "B": f"\\({NUC(27, 60, 'Co')} + {NUC(4, 2, 'β')} \\rightarrow {NUC(28, 60, 'Ni')}\\)".replace("\\mathit{β}", "\\beta"),
                      "C": f"\\({NUC(27, 60, 'Co')} \\rightarrow {NUC(0, 0, 'β')} + {NUC(28, 60, 'Ni')}\\)".replace("\\mathit{β}", "\\beta"),
                      "D": f"\\({NUC(27, 60, 'Co')} \\rightarrow {NUC('+1', 0, 'β')} + {NUC(28, 60, 'Ni')}\\)".replace("\\mathit{β}", "\\beta"),
                      "E": f"\\({NUC(60, 27, 'Co')} \\rightarrow {NUC(0, -1, 'β')} + {NUC(60, 28, 'Ni')}\\)".replace("\\mathit{β}", "\\beta")},
     "explicacao": "<p>Na emissão beta negativa, o núcleo emite um elétron, \\({}^{0}_{-1}\\beta\\): o número de massa fica igual (60) e o número atômico sobe 1 (27 → 28). A partícula aparece entre os produtos: \\({}^{60}_{27}\\mathit{Co} \\rightarrow {}^{0}_{-1}\\beta + {}^{60}_{28}\\mathit{Ni}\\). Alternativa <strong>E</strong>.</p><p>A põe a partícula beta como reagente, o que não é uma emissão. B usa uma partícula de massa 4, que é a alfa. C, D e B trocam os números de massa e atômicos. E D usa a beta positiva (pósitron).</p>"},
30: {"materia": "Raciocínio lógico", "assunto": "Sequências", "tags": MULTI + ["meia-vida", "porcentagem"],
     "enunciado": p("Meia-vida é o tempo necessário para que a atividade radioativa de um elemento seja reduzida pela metade.",
                    "Levando em consideração que um ano possui 365 dias, verifica-se que a atividade radioativa do radioisótopo diminuiu, num período de 7300 dias, um percentual equivalente a"),
     "apoio_de": (28, P28),
     "alternativas": alts("93,75.", "87,50.", "25,00.", "12,50.", "6,25."),
     "explicacao": "<p>7 300 dias são 7 300 ÷ 365 = 20 anos, ou 4 meias-vidas de 5 anos. A atividade cai para 100 → 50 → 25 → 12,5 → 6,25%. Ela diminuiu 100 − 6,25 = <strong>93,75%</strong>. Alternativa <strong>A</strong>.</p><p>6,25% é o que resta, não o quanto diminuiu (E). E 87,50 seria a queda depois de 3 meias-vidas (B).</p>"},
31: {"materia": "Geografia", "assunto": "Industrialização brasileira", "tags": ["maquiladoras", "globalização"],
     "enunciado": apoio(*T(13, "A partir da década de 1960, diversas empresas", "seus direitos mais básicos.")) + url("http://tinyurl.com/mrx8kpr3", "30.01.2024")
                  + p("Essas empresas, em sua maioria, são"),
     "explicacao": "<p>As maquiladoras são, em geral, empresas estadunidenses instaladas no norte do México, perto da fronteira: importam peças dos EUA, montam os produtos com mão de obra barata e exportam de volta. Alternativa <strong>D</strong>.</p><p>Elas ficam no norte, não no sul do México, e pagam salários baixos (A). O México não faz parte do Mercosul (B). Não são principalmente europeias nem de cosméticos (C). E não se instalaram por causa de jazidas no sul (E).</p>"},
32: {"materia": "Biologia", "assunto": "Evolução", "tags": ["Darwin", "seleção natural"],
     "explicacao": "<p>Darwin propôs a <strong>seleção natural</strong>: os seres mais bem adaptados ao ambiente sobrevivem e se reproduzem mais, passando suas características adiante. Alternativa <strong>D</strong>.</p><p>Transmissão de características adquiridas e lei do uso e desuso são ideias de Lamarck (A e E). E genética, biotecnologia, clonagem e genoma vieram muito depois de Darwin (B e C).</p>"},
33: {"materia": "Química", "assunto": "Reações químicas", "tags": ["equilíbrio químico", "Le Chatelier"],
     "enunciado": p(sub(T(13, "Os excrementos de aves e morcegos", "como a amônia (NH3).")[0]),
                    "Esta equação química representa o equilíbrio que ocorre na decomposição da amônia em nitrogênio e hidrogênio:",
                    "\\[2\\,\\text{NH}_3(\\text{g}) \\rightleftharpoons \\text{N}_2(\\text{g}) + 3\\,\\text{H}_2(\\text{g})\\]",
                    "O químico francês Le Chatelier, estudando o comportamento de sistemas em equilíbrio quando sujeitos à variação de fatores como concentração, pressão e temperatura, chegou às seguintes conclusões:",
                    "• o aumento da concentração de reagentes desloca o equilíbrio no sentido dos produtos;", "• a diminuição da concentração de reagentes desloca o equilíbrio no sentido dos reagentes;",
                    "• o aumento da pressão desloca o equilíbrio no sentido do menor volume gasoso; e", "• a diminuição da pressão desloca o equilíbrio no sentido de maior volume gasoso.",
                    "Desse modo, considerando apenas essas conclusões, para deslocar o equilíbrio da referida equação no sentido da formação de amônia, deve-se"),
     "explicacao": "<p>A amônia fica do lado com menos mols de gás: 2 mol, contra 1 + 3 = 4 mol do outro lado. O aumento da pressão desloca o equilíbrio para o menor volume gasoso, ou seja, para a <strong>formação de amônia</strong>. Alternativa <strong>E</strong>.</p><p>Aumentar o NH₃ deslocaria para a decomposição (A). Diminuir N₂ ou H₂ também favoreceria a decomposição (B e C). E diminuir a pressão favoreceria o lado de 4 mol (D).</p>"},
34: {"materia": "Português", "assunto": "Coesão e referência", "tags": ["pronomes"],
     "enunciado": MAPA + P34, "imagens": MAPA_IMG,
     "explicacao": "<p>No terceiro parágrafo, “que não se apresentavam como sedes de sua sociedade” fala das capitais: o pronome relativo <strong>que</strong> retoma “as principais capitais latinas”. Alternativa <strong>E</strong>.</p><p>No primeiro parágrafo, “que” retoma “os convencionais” (mapas), e “o”, no segundo, retoma o mapa de Torres-García, não a expressão “mapa artístico” (A). “O qual” retoma “movimento artístico” (B). “O” não se refere a “autor” (C). E “ele” retoma o autor, não “comportamento” (D).</p>"},
35: {"materia": "Português", "assunto": "Interpretação de texto", "tags": ["mapa artístico"],
     "enunciado": p("De acordo com os textos, é correto afirmar que"), "apoio_de": (34, P34),
     "alternativas": alts("os movimentos artístico-literários das Américas são dependentes de modelos europeus até hoje, no século XXI.",
                          "a arte latino-americana do século XX realizou-se sob a influência de artistas parisienses que foram exilados da Europa.",
                          "a obra de Joaquín Torres-García, apesar de apresentar uma preocupação estética, tem os elementos exigidos pela Geografia para ser considerada também um mapa.",
                          "o desconforto gerado pela falta de uma identidade artística própria motivou artistas da América do Sul a buscarem, em sua cultura e em seu espaço, inspiração para suas obras.",
                          "o desenvolvimento de uma arte genuína, sem influência estrangeira, foi rapidamente concretizado devido à urgência da população em buscar uma identidade cultural própria."),
     "explicacao": "<p>O texto II diz que Torres-García e outros modernistas, incomodados com a cópia de modelos europeus, passaram a exaltar a cultura e os motivos do Uruguai e da América do Sul. O mapa de cabeça para baixo é um exemplo disso. Alternativa <strong>D</strong>.</p><p>O texto não fala do século XXI (A). “Exilados da Europa” era como Torres-García chamava os artistas locais que copiavam a Europa (B). O mapa não tem escala, legenda nem coordenadas completas exigidas pela Geografia (C). E o artista encontrou dificuldades, nada foi rápido (E).</p>"},
36: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": ["gêneros textuais", "convite"],
     "enunciado": "[[fig:1]]" + url("https://tinyurl.com/4xsxj9xb", "17.01.2024", "") + p("O texto apresentado pertence ao gênero"),
     "imagens": figs(("q36", "Convite em inglês: “You're invited – 5th Annual Gala Fundraiser”, em apoio ao “Unidos en la Música: a Latin American Festival”. Domingo, 25 de fevereiro de 2024, às 17h; US$ 100 por pessoa mais taxas; inclui jantar de 4 pratos com harmonização de vinhos; La Cocina International, 530 A1A Beach Blvd, St Augustine, FL, dentro do Castillo Real Hotel. “Join us for an evening of fine dining, dancing and entertainment.” Embaixo, logos de patrocinadores.")),
     "explicacao": "<p>“You're invited” (você está convidado) e “Gala Fundraiser” (jantar de gala beneficente) mostram um <strong>convite</strong> para um jantar que arrecada fundos, num hotel em St. Augustine. Alternativa <strong>C</strong>.</p><p>Não é um curso (A) nem um concerto em ginásio (B). O vinho acompanha um jantar pago (US$ 100), não é degustação gratuita (D). E não é uma campanha para criar bandas (E).</p>"},
37: {"materia": "Geografia", "assunto": "Tectônica de placas", "tags": ["terremotos"],
     "explicacao": "<p>No oeste da América do Sul, a placa de Nazca mergulha sob a placa Sul-Americana. Esse choque forma os Andes e causa muitos terremotos, como no Chile e no Peru. Alternativa <strong>A</strong>.</p><p>A placa de Cocos fica na costa oeste da América Central, não no leste da América do Sul (B). As placas Indiana, Euro-asiática, Arábica, Australiana, do Pacífico e Filipina ficam longe da América Latina (C, D e E).</p>"},
38: {"materia": "Raciocínio lógico", "assunto": "Lógica", "tags": ["condicional", "contrapositiva"],
     "enunciado": p("Três conhecidos, Ceci, Peri e Iracema, estão decidindo se vão visitar Cuba. Contudo, devido a questões pessoais, sabe-se que:",
                    "I. Ceci só vai visitar Cuba, se Iracema for;", "II. se Peri for visitar Cuba, Ceci também irá.", "Assinale a alternativa que apresenta uma conclusão lógica verdadeira."),
     "explicacao": "<p>A frase I diz: se Ceci vai, então Iracema vai. A contrapositiva, que é equivalente, é: se Iracema não vai, então Ceci não vai. Alternativa <strong>D</strong>.</p><p>As premissas não dizem que ninguém vai (A). Se Ceci for, nada impede Peri de ir (B). Se Peri for, Ceci vai e, então, Iracema também vai (C). E nada garante que Peri e Iracema irão (E).</p>"},
39: {"materia": "Física", "assunto": "Física moderna", "tags": ["César Lattes", "partículas"],
     "enunciado": apoio(*[it(x, "Processes involving charged mesons", "Nature") for x in T(16, "O físico brasileiro César Lattes", "um novo campo de estudos da Física.", ["O comitê do Nobel"])])
                  + url("https://tinyurl.com/2ey7cd5d", "29.01.2024")
                  + p("Podemos afirmar, corretamente, que o campo de estudo relacionado à descoberta de Lattes refere-se a"),
     "explicacao": "<p>O méson pi (píon) é uma partícula subatômica. A descoberta de Lattes pertence à <strong>Física de Partículas</strong>. Alternativa <strong>A</strong>.</p><p>A Física Clássica trata de fenômenos macroscópicos (B). A Biofísica estuda os seres vivos (C), a Termodinâmica, o calor (D), e o Eletromagnetismo, os fenômenos elétricos e magnéticos (E).</p>"},
40: {"materia": "Biologia", "assunto": "Ecologia", "tags": ["biodiversidade", "extinção"],
     "enunciado": apoio(*T(16, "O Relatório Planeta Vivo, produzido", "os lagartos da Caatinga.")) + url("http://tinyurl.com/tddbfhnr", "11.02.2024")
                  + p("Entre os fatores que impactam a vida dos animais monitorados, é correto afirmar que"),
     "explicacao": "<p>Extração ilegal de madeira, exploração de plantas e tráfico de animais e plantas silvestres destroem hábitats e populações e levam espécies à extinção. Alternativa <strong>E</strong>.</p><p>A contaminação por garimpo prejudica os botos (A). O desmatamento diminui as chances de sobrevivência (B). Espécies introduzidas desequilibram o ecossistema e não causam mutações (C). E o aquecimento prejudica muitas espécies (D).</p>"},
41: {"materia": "História", "assunto": "Ditadura militar", "tags": ["Itaipu"],
     "enunciado": apoio(*T(17, "A Usina Hidrelétrica de Itaipu corresponde", "em 1984.")) + url("http://tinyurl.com/35hpw5d7", "10.02.2024")
                  + p("Com base no texto, é correto concluir que o projeto"),
     "alternativas": alts("foi resultado da pressão brasileira sobre o Paraguai, que não desejava participar da execução da obra.",
                          "sofreu sucessivos atrasos em sua execução, uma vez que sua inviabilidade foi atestada pela Ata do Iguaçu.",
                          "foi inteiramente concebido e executado no período em que os dois países viviam sob regimes ditatoriais.",
                          "valorizou a cultura tradicional dos povos indígenas, demarcando e preservando seus territórios originais.",
                          "assegurou a preservação ambiental ao garantir a manutenção do curso original do rio Paraná, por pressão do governo brasileiro."),
     "explicacao": "<p>O projeto vai de 1966 (Ata do Iguaçu) a 1984 (início do funcionamento). Nesse período, o Brasil vivia a ditadura militar (1964–1985) e o Paraguai, a ditadura de Stroessner (1954–1989). Alternativa <strong>C</strong>.</p><p>O texto diz que a usina veio dos interesses dos dois países (A). A Ata analisou a viabilidade, não atestou inviabilidade (B). O texto não fala de povos indígenas (D). E o curso do rio Paraná foi desviado em 1978 (E).</p>"},
42: {"materia": "Física", "assunto": "Ondas", "tags": ["som", "acústica"],
     "enunciado": p(*T(17, "Heitor Villa-Lobos (1887–1959)", "um orifício circular na frente.", ["O violão acústico é"])) + "[[fig:1]]"
                  + p("Sobre os conceitos de Física que envolvem esse instrumento musical, podemos afirmar corretamente que"),
     "imagens": figs(("q42", "Desenho de um violão com as partes indicadas: corpo, caixa de ressonância, braço, cordas, ponte e orifício circular.")),
     "explicacao": "<p>A frequência da corda depende da sua tensão e do seu comprimento. Quando o violonista aperta a corda no braço, encurta a parte que vibra e muda a nota. Alternativa <strong>B</strong>.</p><p>Bem tocadas, as cordas vibram nas frequências das notas (A). A caixa de ressonância amplifica o som, não diminui (C). Materiais e formatos diferentes mudam o timbre (D). E o violão acústico não converte energia em eletricidade (E).</p>"},
43: {"materia": "Geografia", "assunto": "Geopolítica", "tags": ["Essequibo", "fronteiras"],
     "enunciado": p("Leia o texto e complete a frase.")
                  + apoio("A região de Essequibo, reivindicada ___<strong>I</strong>___, engloba praticamente toda a área a oeste do Rio Essequibo, no território ___<strong>II</strong>___. A região em questão tem cerca de 159 mil quilômetros quadrados (um pouco maior do que o estado do Ceará) tomados pelo bioma amazônico e é rica em recursos minerais e naturais.")
                  + url("http://tinyurl.com/4d2mp7uy", "24.01.2024")
                  + p("Assinale a alternativa que completa, correta e respectivamente, o texto"),
     "alternativas": colunas(["I", "II"], [["pela Guiana", "brasileiro"], ["pela Guiana", "surinamês"], ["pela Venezuela", "surinamês"], ["pela Venezuela", "guianense"], ["pelo Brasil", "venezuelano"]]),
     "explicacao": "<p>Essequibo é uma região da Guiana, a oeste do rio Essequibo, que a Venezuela reivindica: é reivindicada <strong>pela Venezuela</strong>, no território <strong>guianense</strong>. Alternativa <strong>D</strong>.</p><p>A região não é brasileira nem do Suriname (A, B e C), e o Brasil não a reivindica (E).</p>"},
44: {"materia": "Matemática", "assunto": "Probabilidade", "tags": ["probabilidade condicional"],
     "retificada": True,
     "explicacao": "<p>A probabilidade de o primeiro sorteado ser latino-americano é 6/32 e, depois, a do segundo também ser é 5/31: (6/32) · (5/31) = 30/992 ≈ 0,030 = <strong>3,0%</strong>, entre 2,2% e 3,3%. Alternativa <strong>C</strong>. O gabarito oficial desta questão foi retificado para C.</p><p>Esquecer que o segundo sorteio é sem reposição, (6/32)² ≈ 3,5%, leva a D. Os outros intervalos não contêm o valor.</p>"},
45: {"materia": "História", "assunto": "História contemporânea", "tags": ["independências na América", "Libertadores"],
     "enunciado": apoio(*T(18, "Em 1958, num congresso da Conmebol", "se destacaram na história do continente.")) + url("http://tinyurl.com/37dxb88m", "10.02.2024")
                  + p("O conjunto de líderes, a que o texto se refere, foi responsável"),
     "alternativas": alts("pelo fim das ditaduras cívico-militares implementadas nos países do chamado “Cone Sul”, região que abriga México, Guatemala e Honduras.",
                          "pela eliminação das seleções de Alemanha, Itália, Espanha e França das Copas do Mundo de 1934, 1938, 1950 e 1954.",
                          "pela independência dos países de colonização espanhola e portuguesa na porção Sul do Continente Americano.",
                          "pela resistência dos povos indígenas da América Latina à dominação colonial espanhola e portuguesa no continente.",
                          "pela abolição legal do tráfico e do comércio de escravizados africanos, que levou à libertação de milhares de cativos em todo o continente."),
     "explicacao": "<p>Os “libertadores da América” são os líderes das independências do início do século XIX, como Simón Bolívar, José de San Martín e Bernardo O’Higgins. Alternativa <strong>C</strong>.</p><p>México, Guatemala e Honduras não ficam no Cone Sul (A). O nome não homenageia jogadores (B). Os libertadores eram, em geral, da elite criolla, não líderes indígenas (D). E a abolição veio depois e em datas diferentes em cada país (E).</p>"},
46: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": MULTI + ["sistemas de medidas"],
     "enunciado": SISTEMAS + P46,
     "explicacao": "<p>O texto diz: “The Metric System, or SI (Système International)”: o Sistema Métrico também é chamado de <strong>Sistema Internacional</strong>. Alternativa <strong>E</strong>.</p><p>O Reino Unido usou o sistema imperial de 1824 até adotar o métrico em 1965 (A e C). Só três países não adotaram o sistema métrico (B). E o sistema imperial padronizou pés e libras (D).</p>"},
47: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": MULTI + ["Sistema Internacional de Unidades"],
     "enunciado": p("Das informações contidas no texto, é possível inferir corretamente que"), "apoio_de": (46, P46),
     "explicacao": "<p>O texto lista as unidades fundamentais do SI: metro (m), quilograma (kg), segundo (s), ampère (A), kelvin (K), mol e candela (cd). Alternativa <strong>C</strong>.</p><p>Libéria, Myanmar e EUA não adotaram oficialmente o sistema métrico (A). A América Latina usa o sistema métrico (B). O ampère é a unidade de corrente elétrica, não de todas as grandezas elétricas (D). E “pé” é do sistema imperial, não do SI (E).</p>"},
48: {"materia": "Português", "assunto": "Gêneros textuais", "tags": ["tirinha"],
     "enunciado": "[[fig:1]]" + url("http://tinyurl.com/cwchj35a", "16.02.2024", "Original colorido.")
                  + p("A tirinha é um gênero que utiliza linguagem verbal e não verbal na construção de sentido.", "Ao analisá-la, conclui-se corretamente que"),
     "imagens": figs(("q48", "Tirinha “Cientirinhas #251”, em quatro quadros. 1: uma batata, em uma sala com o retrato de um nobre inglês e uma bandeira do Reino Unido na parede, toma chá à mesa; uma carta chega pela porta. 2: a batata lê a carta, animada: “Oba! É o resultado do meu teste de ancestralidade por DNA.” 3: a batata, assustada: “Oh my God!”. 4: o resultado do teste: “Cliente: Sra. Batata Inglesa. Resultado: seus antepassados vieram da América do Sul.”, com um mapa marcando Peru, Bolívia e Chile.")),
     "alternativas": alts("a personagem mantém hábitos condizentes com sua cultura ancestral.", "o susto expresso pela personagem evidencia sua falta de conhecimento histórico.",
                          "a influência da cultura estrangeira é assimilada conscientemente pela personagem.", "o resultado do teste demonstra a despreocupação da personagem com sua origem.",
                          "a expressão em inglês, dita pela personagem, é incoerente com o espaço em que está."),
     "explicacao": "<p>A “batata inglesa” se assusta ao descobrir que seus antepassados vieram da América do Sul. Mas a batata é originária dos Andes e foi levada para a Europa pelos colonizadores. O susto mostra que ela <strong>não conhece a própria história</strong>. Alternativa <strong>B</strong>.</p><p>Ela tem hábitos ingleses, não andinos (A). Ela não sabia da sua origem, então não a assimilou conscientemente (C). Ela fez o teste por se interessar pela origem (D). E o “Oh my God!” combina com o ambiente inglês (E).</p>"},
49: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": ["arqueologia"],
     "enunciado": UPANO + P49,
     "alternativas": alts("um vulcão.", "um meteoro.", "um terremoto.", "uma epidemia.", "uma guerra."),
     "explicacao": "<p>O texto diz que a região fica à sombra de um vulcão “that created rich local soils but also may have led to the destruction of the society”. Alternativa <strong>A</strong>.</p><p>O texto não fala de meteoro, terremoto, epidemia ou guerra (B, C, D e E).</p>"},
50: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": ["arqueologia"],
     "enunciado": UPANO + p("A nova descoberta descrita no texto aponta que, na região Amazônica,"),
     "explicacao": "<p>O texto diz que casas e praças “were connected by an astounding network of roads and canals”: as sociedades se conectavam por <strong>estradas e canais</strong>. Alternativa <strong>E</strong>.</p><p>Os maias viviam na América Central, e o texto não fala deles (A). A descoberta mostra justamente o contrário de vilarejos isolados, de nômades e de povos sem agricultura (B, C e D).</p>"},
51: {"materia": "História", "assunto": "América pré-colombiana", "tags": MULTI + ["arqueologia"],
     "enunciado": UPANO + p("Com base no texto, é correto afirmar que"),
     "explicacao": "<p>A cidade foi construída há cerca de 2 500 anos, com uma rede complexa de estradas e canais. Quando Colombo chegou, a América já era povoada por sociedades com conhecimentos e técnicas complexos. Alternativa <strong>D</strong>.</p><p>O vale do Upano fica no Equador, não no Amazonas brasileiro (A). Colombo não chegou lá, e a cidade já tinha sido abandonada (B). As sociedades praticavam a agricultura (C). E automóveis só surgiram no século XIX (E).</p>"},
52: {"materia": "Raciocínio lógico", "assunto": "Sequências", "tags": ["sistemas de numeração"],
     "enunciado": p("Quéchua é uma família de línguas falada por diversos grupos étnicos, ao longo da região da cordilheira dos Andes.", "O quadro mostra os dez primeiros numerais nas línguas portuguesa e quéchua.")
                  + tabela(["Português", "Quéchua"], [["um", "<em>shuc</em>"], ["dois", "<em>ishcai</em>"], ["três", "<em>quimsa</em>"], ["quatro", "<em>chuscu</em>"], ["cinco", "<em>pichca</em>"],
                                                     ["seis", "<em>sucta</em>"], ["sete", "<em>canchis</em>"], ["oito", "<em>pusac</em>"], ["nove", "<em>iscun</em>"], ["dez", "<em>chunca</em>"]])
                  + p("Nessa família de línguas, no que se refere ao seu sistema de numeração, existem algumas regras que são regulares e não variam. Por exemplo, se o nome de um algarismo está",
                      "• antes do numeral 10, isso indica uma multiplicação: <em>pusac chunca</em> é oito vezes dez, ou seja, 80;",
                      "• depois do numeral 10, isso indica uma adição: <em>chunca pusac</em> é dez mais oito, ou seja, 18.")
                  + fonte("D’AMORE, B. Matemática em Algumas Culturas da América do Sul: uma contribuição à Etnomatemática. Boletim de Educação Matemática, vol.16, n.19, 2003. Adaptado.")
                  + p("Seguindo a lógica de formação numérica apresentada no texto, o numeral trinta e nove (39), na língua quéchua, é"),
     "explicacao": "<p>39 = 3 × 10 + 9. O 3 (<em>quimsa</em>) vem antes do 10 (<em>chunca</em>), para multiplicar, e o 9 (<em>iscun</em>) vem depois, para somar: <em>quimsa chunca iscun</em>. Alternativa <strong>A</strong>.</p><p>B põe o 9 antes do 10, o que seria uma multiplicação. C seria 10 + 3 + 9. D e E começam pelo 9, que multiplicaria o 10.</p>"},
53: {"materia": "História", "assunto": "Povos indígenas", "tags": MULTI + ["queros", "Bem-Viver"],
     "enunciado": apoio(*T(22, "Os queros são descendentes", "vida coletiva e em comunidade.")) + url("http://tinyurl.com/2umjhehd", "08.02.2024")
                  + p("Segundo o texto, é correto afirmar que"),
     "explicacao": "<p>O texto diz que os queros valorizam a comunicação com a terra, a reciprocidade com a vida (Ayni) e a vida coletiva (Ayllu), em busca do “Bem-Viver”. Alternativa <strong>C</strong>.</p><p>Eles são camponeses e pastores, não descuidados (A e E). Valorizam o coletivo, não o individual (B). E mantêm a língua e a tradição incas (D).</p>"},
54: {"materia": "História", "assunto": "América colonial", "tags": ["conquista da América", "Las Casas"],
     "enunciado": p("Leia o texto que um missionário dominicano escreveu aos reis da Espanha em 1565.")
                  + apoio(*[it(x, "encomiendas", "repartimentos") for x in T(22, "Todas as guerras que chamamos de conquista", "até o dia do Juízo Final.")])
                  + fonte("LUSTOSA, Oscar de Figueiredo. “Notas para um centenário: Bartolomeu de Las Casas (1474-1575)”. In: Revista de História. V. 51, nº 102, p. 717-729, 1975. Traduzido e adaptado.")
                  + p("Segundo o texto,"),
     "explicacao": "<p>O missionário chama as guerras de conquista de “injustíssimas”, diz que as encomiendas são “cruéis e tirânicas” e que as riquezas foram roubadas: a conquista foi marcada pela <strong>opressão e pela violência</strong> contra os nativos. Alternativa <strong>E</strong>.</p><p>As “Índias” do texto são a América, não a Ásia (A e D). Os nativos é que têm direito a uma guerra justa contra os espanhóis (B). E não havia harmonia (C).</p>"},
})
completar(Q, R)
