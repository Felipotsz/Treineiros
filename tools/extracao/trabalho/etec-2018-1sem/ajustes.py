# Ajustes da conferência humana: Vestibulinho ETEC 1º semestre de 2018 (exame de 21/01/2018)
# Texto conferido com a imagem de cada página; caixas de texto via trecho().
# Letras de canção (Carlinhos Brown, Marcelo Jeneci, Marisa Monte) e alternativas com versos de canções recentes
# ficam como imagem: o alt descreve, não transcreve. Gabarito: oficial (1º SEM/18). Sem tema único.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import A, carregar, enun, tabela, colunas, completar, trecho

ID = "etec-2018-1sem"
META = {
    "id": ID,
    "banca": "ETEC",
    "ano": 2018,
    "semestre": 1,
    "titulo": "Vestibulinho ETEC, 1º semestre de 2018",
    "fonte": "Centro Paula Souza",
    "dataExame": "2018-01-21",
    "duracaoMinutos": 240,
    "apresentacao": "<p>Prezado(a) candidato(a), nesta prova você vai se deparar com diversos temas nas diferentes áreas do conhecimento. As questões abordarão conceitos e conteúdos que fizeram parte de sua formação escolar até agora.</p><p>Boa prova!</p>",
    "pdf": f"assets/provas/{ID}.pdf",
}
EXTRAS = {"apresentacao": "Ilustração em lápis de um globo terrestre cercado por fitas e hexágonos com símbolos de várias áreas do conhecimento: letras “ABC abc”, um átomo, livros, instrumentos de medida e um microscópio."}

R = carregar(ID)


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


def sub(texto, *pares):
    for a, b in pares: texto = texto.replace(a, b)
    return texto


def figs_alt(primeira=1):
    return {l: f"[[fig:{primeira + i}]]" for i, l in enumerate("ABCDE")}


# ---------- textos compartilhados ----------
CRONICA = (chamada("Leia a crônica de Paulo Brabo e responda às questões de números 01 e 02.")
           + apoio("<strong>DUZENTAS GRAMAS</strong>", T(2, "Meu amigo Hélio, que é pai", "virtude e integridade. [...]")[0])
           + url("https://tinyurl.com/ya6ta9cr", "09.11.2017", ""))
P1 = p("Segundo o texto, é possível afirmar que")

MISTURAS = (chamada("Leia o texto para responder às questões de números 04 e 05.")
            + apoio(*T(3, "A natureza apresenta diversas", "fosse possível.", ["Por essa razão"]))
            + url("https://tinyurl.com/y8j567ag", "10.11.2017", ""))
P4 = p("Assinale a alternativa que apresenta um exemplo de mistura homogênea.")

PEGADA = (chamada("Leia o texto para responder às questões de números 09 a 11.")
          + apoio(*[sub(x, ("(water footprint)", "(<em>water footprint</em>)")) for x in
                    T(5, "A pegada hídrica", "na média mundial.", ["Por exemplo, 17 000"])]))
P9 = (p("Considere a tabela:")
      + tabela(["País", "Consumo de Carne<sup>(1)</sup> (kg/pessoa/ano)", "Pegada Hídrica da Carne<sup>(2)</sup> (m<sup>3</sup>/tonelada)"],
               [["EUA", "43", "14 500"], ["Brasil", "32", "19 400"], ["México", "23", "17 500"], ["Reino Unido", "18", "9 900"],
                ["Ucrânia", "10", "12 600"], ["China", "5", "13 700"], ["Bolívia", "12", "77 000"],
                ["<strong>Média Mundial</strong>", "<strong>9</strong>", "<strong>15 400</strong>"]])
      + fonte("Fonte dos dados &lt;https://tinyurl.com/ybmecog4&gt; Acesso em: 09.11.2017.<br><sup>(1)</sup> consumo médio do país<br><sup>(2)</sup> a pegada hídrica da carne de um país depende de vários fatores, como a composição e a origem da alimentação do gado")
      + p("Com base nos dados da tabela, é correto afirmar que"))

BAFOMETRO = (chamada("Leia o texto para responder às questões de números 18 e 19.")
             + apoio(*T(8, "Há mais de um tipo de bafômetro", "6 meses a 1 ano."))
             + url("https://tinyurl.com/yctm9zrz", "10.11.2017"))
P18 = p("No etilômetro que muda de cor na presença do álcool, ocorre a seguinte reação química:",
        "K<sub>2</sub>Cr<sub>2</sub>O<sub>7 </sub>(aq) + 4 H<sub>2</sub>SO<sub>4 </sub>(aq) + 3 CH<sub>3</sub>CH<sub>2</sub>OH (g) → Cr<sub>2</sub>(SO<sub>4</sub>)<sub>3 </sub>(aq) + 3 CH<sub>3</sub>CHO (g) + 7 H<sub>2</sub>O (ℓ) + 4 K<sub>2</sub>SO<sub>4 </sub>(aq)",
        "(O K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub> é alaranjado e o Cr<sub>2</sub>(SO<sub>4</sub>)<sub>3</sub> é verde.)",
        "É possível identificarmos, na reação, a presença de")

RADAR = (p("Para exemplificar uma aplicação do conceito de velocidade média, um professor de Ciências explica aos seus alunos como é medida a velocidade de um veículo quando passa por um radar.",
           "Os radares usam a tecnologia dos sensores magnéticos. Geralmente são três sensores instalados no asfalto alguns metros antes do radar. Esse equipamento mede quanto tempo o veículo demora para ir de um sensor ao outro, calculando a partir daí, a velocidade média do veículo.")
         + "[[fig:1]]" + url("http://tinyurl.com/yd9pdgk7", "12.11.2017", "")
         + p("Considere um veículo trafegando numa pista cuja velocidade máxima permitida seja de 40 km/h (aproximadamente 11 m/s) e a distância média entre os sensores consecutivos seja de 2 metros."))

RESERV = (chamada("Leia o texto e considere a figura para responder às questões de números 36 e 37.")
          + p("O trapézio retângulo ABCD da figura representa a superfície de um reservatório de água.") + "[[fig:1]]"
          + apoio("Na figura, tem-se que: AB = 20 m; CD = 15 m; AD = 12 m; o ângulo D\\(\\hat{A}\\)B é reto."))
P36 = p("Admita que, a cada metro quadrado da superfície desse reservatório, 3 litros de água evaporem por dia.",
        "Em um dia em que a variação da quantidade de água dependeu apenas da evaporação, o reservatório perdeu <strong>N</strong> litros de água. O valor de <strong>N</strong> é")

ESPELHO = (chamada("Leia o texto para responder às questões de números 42 e 43.")
           + apoio(T(18, "Quando você fica à frente de um espelho plano", "como mostrado na figura.")[0]) + "[[fig:1]]")
P42 = (p("Imagine que você esteja em frente a um espelho plano, a uma distância de 0,5 m. Suponha que esse espelho seja deslocado no mesmo plano em 0,4 m, se distanciando de você, conforme a figura.")
       + "[[fig:2]]" + p("A distância, representada no esquema pela letra <strong><em>y</em></strong>, entre você e a sua imagem, será, em metros, de"))

JENECI = (chamada("Leia a música de Marcelo Jeneci e responda às questões de números 44 e 45.") + "[[fig:1]]")
JENECI_IMG = {"arquivo": "q44", "alt": "Trecho da letra da canção “Dar-te-ei”, de Marcelo Jeneci. O eu lírico enumera presentes que não dará à pessoa amada, como papéis, discos, casacos, bombons e festas, porque estragam ou acabam, e diz que, por fim, dará os seus beijos e os seus lábios, que ficam. Fonte: &lt;https://tinyurl.com/ybf22rpl&gt;, acesso em 10.11.2017."}
P44 = p("O autor da música enumera e destaca todas as coisas que dará e o que não dará a(o) sua(seu) amada(o), enfocando que prefere as coisas que “ficam”. Para isso, ele faz uso da linguagem em seu sentido denotativo e conotativo.",
        "Assinale a alternativa em que há o exemplo e a explicação corretos dos tipos de linguagens utilizadas na música.")

MISSOES = (chamada("Leia o texto e observe o mapa para responder às questões de números 47 e 48.")
           + apoio(*T(21, "A partir do início do século XVII", "sob controle espanhol.", ["Entretanto, com a assinatura", "Os povos guarani guerrearam"]))
           + "[[fig:1]]" + url("https://tinyurl.com/y82hlhrb", "13.11.2017", "Original colorido."))
MISSOES_IMG = {"arquivo": "q47", "alt": "Mapa da região das missões jesuíticas, entre Paraguai, Argentina, Uruguai e o sul do Brasil, com Assunção, Foz do Iguaçu, Curitiba, Florianópolis e Porto Alegre. Cerca de trinta povoados, como São Miguel, São Nicolau, São Luís e Santo Ângelo, aparecem agrupados entre os rios Paraná e Uruguai. Uma linha tracejada marca os limites da região missioneira."}
P47 = p("De acordo com as informações apresentadas no texto e no mapa, é correto afirmar que")

EVOCE = (chamada("Leia a letra da música “É você” de Marisa Monte e responda às questões de números 49 e 50.") + "[[fig:1]]"
         + p("Releia os trechos.") + "[[fig:2]]"
         + p("Percebemos que os exemplos <strong>I</strong> e <strong>II</strong> se tratam de períodos compostos."))
EVOCE_IMG = [{"arquivo": "q49", "alt": "Letra da canção “É você”, de Marisa Monte, em duas estrofes curtas. O eu lírico se dirige a uma pessoa amada, a única que o acompanha na vida, fala dos dois em lugares como a floresta, o salão, a biblioteca e o saguão, e repete que na vida só resta seguir. Fonte: &lt;https://tinyurl.com/ycdar4y4&gt;, acesso em 13.11.2017."},
             {"arquivo": "q49b", "alt": "Quadro com dois trechos da canção. I: “É você [...]” seguido de uma oração em negrito, iniciada por “que”, sobre a pessoa que vai com o eu lírico na vida agora. II: “É você [...]” seguido de uma oração em negrito, iniciada por “que”, sobre a pessoa que invadiu o centro do espelho."}]
P49 = p("Assim, assinale a alternativa que indica o efeito de sentido que as orações destacadas produzem sobre as não destacadas.")

Q = {
1: {"materia": "Português", "assunto": "Variação linguística", "tags": ["crônica"],
    "enunciado": CRONICA + P1,
    "explicacao": "<p>O título “Duzentas gramas” é a forma que o próprio autor usa na padaria, ou seja, faz parte da sua <strong>oralidade</strong>. A crônica mostra que o amigo Hélio trata a forma “correta” como sinal de cultura e de virtude, o que envolve <strong>prestígio social</strong>. Alternativa <strong>D</strong>.</p><p>O autor critica a ideia de que existam formas “incorretas” de pronunciar (A). A forma “correta” defendida por Hélio é a da norma culta, não a coloquial (B). O texto questiona, e não defende, que certos modos de falar não deveriam existir (C). E a situação descrita é perfeitamente real (E).</p>"},
2: {"materia": "Português", "assunto": "Classes de palavras", "tags": ["concordância nominal"],
    "enunciado": p("Releia o trecho.")
                 + apoio("Meu amigo Hélio [...] fica indignado quando peço na padaria duzentas gramas de presunto – quando a forma correta, insiste ele, é “duzentos” gramas.")
                 + p("Hélio aponta um desvio da norma padrão na expressão <strong>“duzentas gramas</strong>” utilizada pelo autor no seu dia a dia. No entanto, ele não aponta o motivo dessa expressão não estar <em>correta</em>.",
                     "Assinale a alternativa que contenha o tipo de problema identificado por Hélio."),
    "apoio_de": (1, P1),
    "explicacao": "<p>“Grama”, como unidade de massa, é palavra masculina (<em>o</em> grama). O numeral “duzentos” deve concordar em gênero com ela: “duzentos gramas”. É um caso de <strong>concordância nominal</strong>. Alternativa <strong>A</strong>.</p><p>Não há verbo envolvido no problema (B e D). Regência trata da relação entre um termo e seu complemento, não de concordância (C e D). E o problema é de gênero, não de número (C e E).</p>"},
3: {"materia": "Geografia", "assunto": "População", "tags": ["urbanização"],
    "enunciado": p("A tabela apresenta os maiores centros urbanos do planeta em três diferentes momentos: 1900, 2001 e 2015.")
                 + tabela(["1900", "Pop.*", "2001", "Pop.*", "2015", "Pop.*"], [
                     ["<strong>Londres</strong> (Inglaterra)", "6,6", "<strong>Tóquio</strong> (Japão)", "29", "<strong>Tóquio</strong> (Japão)", "29"],
                     ["<strong>Nova York</strong> (Estados Unidos)", "3,4", "<strong>Cidade do México</strong> (México)", "18", "<strong>Mumbai</strong> (Índia)", "26"],
                     ["<strong>Paris</strong> (França)", "2,7", "<strong>São Paulo</strong> (Brasil)", "17", "<strong>Lagos</strong> (Nigéria)", "25"],
                     ["<strong>Berlim</strong> (Alemanha)", "1,9", "<strong>Mumbai</strong> (Índia)", "17", "<strong>São Paulo</strong> (Brasil)", "20"],
                     ["<strong>Chicago</strong> (Estados Unidos)", "1,7", "<strong>Nova York</strong> (Estados Unidos)", "16", "<strong>Karachi</strong> (Paquistão)", "19"],
                     ["<strong>Viena</strong> (Áustria)", "1,7", "<strong>Xangai</strong> (China)", "14", "<strong>Daca</strong> (Bangladesh)", "19"],
                     ["<strong>Tóquio</strong> (Japão)", "1,5", "<strong>Los Angeles</strong> (Estados Unidos)", "13", "<strong>Cidade do México</strong> (México)", "19"],
                     ["<strong>Wuhan</strong> (China)", "1,5", "<strong>Lagos</strong> (Nigéria)", "13", "<strong>Xangai</strong> (China)", "18"],
                     ["<strong>Filadélfia</strong> (Estados Unidos)", "1,3", "<strong>Calcutá</strong> (Índia)", "13", "<strong>Nova York</strong> (Estados Unidos)", "18"],
                     ["<strong>São Petersburgo</strong> (Rússia)", "1,3", "<strong>Buenos Aires</strong> (Argentina)", "12", "<strong>Calcutá</strong> (Índia)", "17"]])
                 + fonte("Fonte dos dados: &lt;http://tinyurl.com/y9khp95z&gt; Acesso em: 15.11.2017. Adaptado.<br>*População em milhões de habitantes.")
                 + p("Sobre a distribuição espacial dos grandes centros urbanos pelo mundo apresentados na tabela, é possível afirmar corretamente, que"),
    "alternativas": {"C": "no ano de 2001, duas das maiores aglomerações urbanas do planeta pertenciam à América Latina.",
                     "D": "nos três momentos registrados na tabela aparece, pelo menos, uma cidade do continente europeu."},
    "explicacao": "<p>Em 2015, seis das dez maiores aglomerações ficam na <strong>Ásia</strong>: Tóquio, Mumbai, Karachi, Daca, Xangai e Calcutá. A maioria está num único continente. Alternativa <strong>B</strong>.</p><p>Em 1900 (fim do século XIX), as maiores cidades ficavam em países desenvolvidos da Europa e dos Estados Unidos (A). Em 2001, eram três da América Latina: Cidade do México, São Paulo e Buenos Aires (C). Não há cidade europeia em 2001 nem em 2015 (D). E a terceira maior de 2015 é Lagos, na África (E).</p>"},
4: {"materia": "Química", "assunto": "Substâncias e misturas",
    "enunciado": MISTURAS + P4,
    "explicacao": "<p>Gases sempre se misturam por completo, formando uma só fase. <strong>Gás nitrogênio + gás hélio</strong> é uma mistura homogênea. Alternativa <strong>C</strong>.</p><p>Água e gasolina, e água e óleo, não se misturam e formam duas fases (A e B). A fuligem são partículas sólidas suspensas no ar (D). E a areia não se dissolve, ficando visível no sal (E).</p>"},
5: {"materia": "Química", "assunto": "Separação de misturas",
    "enunciado": p("Um procedimento que permite separar, sem o uso de qualquer fonte de calor, uma mistura de água e óleo de cozinha é a"),
    "apoio_de": (4, P4),
    "explicacao": "<p>Água e óleo são líquidos que não se misturam e têm densidades diferentes. Deixando a mistura em repouso (num funil de decantação, por exemplo), o óleo fica por cima e a água por baixo, e dá para separá-los sem aquecer. É a <strong>decantação</strong>. Alternativa <strong>A</strong>.</p><p>Sublimação e destilação envolvem aquecimento (B e D). Peneiração separa sólidos de tamanhos diferentes (C). E a filtração separa sólidos de líquidos (E).</p>"},
6: {"materia": "História", "assunto": "Brasil República", "tags": ["separação dos poderes"],
    "explicacao": "<p>Os “três poderes” da praça são o <strong>Executivo</strong> (Palácio do Planalto), o <strong>Legislativo</strong> (Congresso Nacional) e o <strong>Judiciário</strong> (Supremo Tribunal Federal). A ideia de separá-los, de forma independente e equilibrada, vem de <strong>Montesquieu</strong>. Alternativa <strong>E</strong>.</p><p>Presidente, governadores e prefeitos são níveis de governo, não poderes (A). A divisão medieval era em clero, nobreza e servos (B). Platão não propôs presidente nem deputados (C). E Senado e Câmara formam um único poder, o Legislativo (D).</p>"},
7: {"materia": "Química", "assunto": "Estrutura atômica",
    "enunciado": p("Um fogo de artifício é composto basicamente por pólvora (mistura de enxofre, carvão e salitre) e por um sal de um elemento determinado, por exemplo, sais de cobre, como CuCℓ<sub>2</sub>, que irá determinar a cor verde azulada da luz produzida na explosão.")
                 + "[[fig:1]]" + url("https://tinyurl.com/ybcuml9u", "15.11.2017")
                 + p("Observe as representações dos elementos enxofre e cobre presentes em um fogo de artifício: \\({}^{32}_{16}S\\) e \\({}^{64}_{29}Cu\\).",
                     "A partir da análise dessas representações, assinale a alternativa que apresenta, respectivamente, o número de massa do enxofre e o número de nêutrons do cobre."),
    "imagens": [{"arquivo": "q07", "alt": "Foto de um fogo de artifício explodindo no céu escuro, com raios de luz saindo de um ponto central."}],
    "explicacao": "<p>O número de cima é o número de massa, e o de baixo, o número atômico (prótons). O enxofre tem massa <strong>32</strong>. O cobre tem 64 − 29 = <strong>35</strong> nêutrons. Alternativa <strong>B</strong>.</p><p>29 é o número de prótons do cobre (A e C). 16 é o número atômico do enxofre, não a massa (C, D e E). E 64 é a massa do cobre (E).</p>"},
8: {"materia": "Química", "assunto": "Reações químicas", "tags": ["Lei de Lavoisier"],
    "enunciado": apoio(*T(4, "Lavoisier foi quem descobriu", "Lei de Lavoisier.", ["Lavoisier também foi"]))
                 + url("https://tinyurl.com/ybcuml9u", "15.11.2017")
                 + p("Em um experimento para obtenção de salitre, foram anotadas as massas utilizadas, porém o aluno esqueceu de anotar a massa formada de nitrato de potássio, conforme a figura.")
                 + tabela(["KCℓ", "+ HNO<sub>3</sub>", "→ KNO<sub>3</sub>", "+ HCℓ"], [["745 g", "630 g", "<strong><em>x</em></strong> g", "365 g"]])
                 + p("O aluno não se preocupou com esse fato, pois aplicando a Lei de Lavoisier é possível encontrar a massa desconhecida, representada por <strong><em>x</em></strong> na tabela.",
                     "Assinale a alternativa que apresenta a massa de salitre, em gramas, obtida nesse experimento."),
    "explicacao": "<p>Pela Lei de Lavoisier, a massa dos reagentes é igual à dos produtos: 745 + 630 = <em>x</em> + 365. Então 1 375 = <em>x</em> + 365 e <em>x</em> = <strong>1 010 g</strong>. Alternativa <strong>D</strong>.</p><p>1 375 g é a massa total dos reagentes (E). 630 e 745 são as massas de cada reagente (B e C). E 101 g tem a ordem de grandeza errada (A).</p>"},
9: {"materia": "Matemática", "assunto": "Interpretação de dados", "tags": ["pegada hídrica"],
    "enunciado": PEGADA + P9,
    "explicacao": "<p>A pegada da carne na Bolívia é 77 000 m³/t, e a média mundial é 15 400 m³/t. Como 5 · 15 400 = 77 000, a da Bolívia é <strong>cinco vezes</strong> a média. Alternativa <strong>C</strong>.</p><p>Os EUA consomem mais carne que o Brasil e têm pegada menor, então uma não aumenta com a outra (A). 19 400 m³ por tonelada equivalem a 19 400 litros por quilo, não 19,4 (B). 17 500 não chega ao dobro de 13 700 (D). E 43/14 500 e 10/12 600 não formam proporção (E).</p>"},
10: {"materia": "Matemática", "assunto": "Razão e proporção",
     "enunciado": p("Por ser um consumidor voraz de chocolate, João estabeleceu que, para não exagerar, sempre comerá exatamente 1 kg de chocolate a cada 5 dias. Ao estudar o conceito de pegada hídrica em sua aula de Ciências, João calculou que, após um ano, a pegada hídrica do seu consumo de chocolate será de <strong>N</strong> metros cúbicos de água, considerando a média mundial.",
                    "Assim sendo, o valor de <strong>N</strong> está mais próximo de"),
     "apoio_de": (9, P9),
     "explicacao": "<p>Em um ano, João come 365 ÷ 5 = 73 kg de chocolate. Cada quilo exige 17 000 L = 17 m³ de água. Então N = 73 · 17 = 1 241 m³, mais próximo de <strong>1 200</strong>. Alternativa <strong>D</strong>.</p><p>Esquecer de converter litros em metros cúbicos, ou contar um só quilo, leva a valores muito diferentes (A, B, C e E).</p>"},
11: {"materia": "Matemática", "assunto": "Equações", "tags": ["sistema de equações"],
     "enunciado": p("No lanche da tarde, João comeu um pão com queijo, de massa total de 200 g. Curioso como sempre, determinou que, considerando só a produção dos dois ingredientes desse lanche (o pão e o queijo), o consumo de água foi de 830 litros.",
                    "Sabendo que, em média, a pegada hídrica do pão é de 1,6 L/g e a do queijo é de 5,0 L/g, pode-se concluir corretamente que, em relação a esse consumo,"),
     "apoio_de": (9, P9),
     "alternativas": {"A": "a quantidade de pão é igual à quantidade de queijo."},
     "explicacao": "<p>Sejam <em>p</em> e <em>q</em> as massas de pão e de queijo. Então <em>p</em> + <em>q</em> = 200 e 1,6<em>p</em> + 5<em>q</em> = 830. Substituindo <em>p</em> = 200 − <em>q</em>: 320 − 1,6<em>q</em> + 5<em>q</em> = 830, ou seja, 3,4<em>q</em> = 510 e <em>q</em> = 150 g. Logo <em>p</em> = 50 g, e a quantidade de queijo é o <strong>triplo</strong> da de pão. Alternativa <strong>E</strong>.</p><p>As outras relações não satisfazem as duas equações ao mesmo tempo. C inverte pão e queijo.</p>"},
12: {"materia": "Física", "assunto": "Cinemática", "tags": ["referencial", "lançamento horizontal"],
     "enunciado": enun(R, 12, figs={"p06-1": 1}).replace("<p>Desprezando", '<p class="fonte">&lt;https://tinyurl.com/y8cvpjzm&gt; Acesso em: 15.11.2017. Original colorido.</p><p>Desprezando'),
     "imagens": [{"arquivo": "q12", "alt": "Um avião aparece em três posições ao longo de uma linha horizontal. A caixa solta por ele descreve uma curva para baixo e, a cada instante, está sempre na vertical abaixo do avião, marcada por linhas tracejadas. Uma pessoa observa do chão."}],
     "explicacao": "<p>Ao ser solta, a caixa mantém a velocidade horizontal do avião. Para quem está <strong>no avião</strong>, ela fica sempre logo abaixo e cai em <strong>linha reta vertical</strong>. Para quem está na Terra, ela combina o movimento horizontal com a queda e descreve uma parábola. Alternativa <strong>B</strong>.</p><p>A parábola é vista por quem está no chão, não no avião (A), e a reta vertical, por quem está no avião, não no chão (C). A caixa cai, então não segue reta horizontal (D). E a trajetória depende do referencial (E).</p>"},
13: {"materia": "Biologia", "assunto": "Fisiologia humana", "tags": ["sistema digestório"],
     "explicacao": "<p>A <strong>epiglote</strong> é a lâmina de cartilagem que fecha a entrada da laringe quando engolimos, desviando o alimento para o esôfago. Alternativa <strong>A</strong>.</p><p>Cárdia e piloro são as aberturas de entrada e saída do estômago (B e C). A glote é a abertura da laringe que a epiglote cobre (D). E o ceco é a primeira parte do intestino grosso (E).</p>"},
14: {"materia": "Física", "assunto": "Energia",
     "enunciado": p("Um aluno deseja calcular a energia envolvida no cozimento de um certo alimento.", "Para isso, verifica que a potência do forno que utilizará é de 1 000 W.",
                    "Ao colocar o alimento no forno e marcar o tempo (∆t) gasto até o seu cozimento, ele concluiu que 3 minutos eram o bastante.")
                  + apoio("Lembre-se que: \\(P = \\dfrac{E}{\\Delta t}\\), em que <strong>P</strong> = potência (W), <strong>E</strong> = energia (J) e \\(\\Delta t\\) = variação de tempo (s).")
                  + p("Dessa maneira, a energia (E) necessária para cozinhar o alimento é de"),
     "explicacao": "<p>3 minutos são 180 s. Então E = P · ∆t = 1 000 W · 180 s = <strong>180 000 J</strong>. Alternativa <strong>A</strong>.</p><p>Usar 3 em vez de 180 s, ou errar a conversão, leva aos valores menores (C e E). B e D não correspondem a nenhuma conta correta.</p>"},
15: {"materia": "História", "assunto": "História contemporânea", "tags": ["Revolução Russa"],
     "enunciado": enun(R, 15),
     "explicacao": "<p>Em 1917 ocorreu a <strong>Revolução Russa</strong>: o czarismo caiu e os bolcheviques tomaram o poder, instaurando o regime socialista ligado à cor vermelha. Alternativa <strong>E</strong>.</p><p>Nicolau II foi o último czar e foi derrubado em 1917 (A). A Igreja Ortodoxa é de muitos séculos antes (B). A União Soviética só acabou em 1991 (C). E o texto diz que o Kremlin é de 1156 (D).</p>"},
16: {"materia": "Geografia", "assunto": "População", "tags": ["pirâmide etária"],
     "enunciado": enun(R, 16, figs={"p07-1": 1}).replace("<p>Fonte dos dados: Instituto", '<p class="fonte">Fonte dos dados: Instituto'),
     "imagens": [{"arquivo": "q16", "alt": "Duas pirâmides etárias do Brasil, de 1991 e 2010, com mulheres à esquerda e homens à direita, faixas de 0 a 9 até 80 ou mais. Em 1991 a base é larga e o topo estreito. Em 2010 a base (0 a 9 e 10 a 19 anos) encolheu e as faixas de adultos e idosos aumentaram."}],
     "explicacao": "<p>De 1991 para 2010, a base da pirâmide diminuiu (menos crianças) e o topo engordou (mais adultos e idosos): a população está envelhecendo. As verbas devem priorizar a <strong>assistência aos idosos e a previdência</strong>. Alternativa <strong>E</strong>.</p><p>A natalidade já está caindo, então controlá-la não é prioridade (A). Pré-natal, creches e serviços para crianças atendem a faixas que estão diminuindo (B, C e D).</p>"},
17: {"materia": "Português", "assunto": "Classes de palavras", "tags": ["crase", "tirinha"],
     "enunciado": p("Leia a tirinha.") + "[[fig:1]]"
                  + fonte("QUINO (Joaquín Salvador Lavado). <em>Toda Mafalda</em>. São Paulo: Martins Fontes, 2008. p. 256.")
                  + p("A interpretação do humor da tirinha se dá, em partes, pelo entendimento do funcionamento da crase utilizada no segundo quadrinho.",
                      "Assinale a alternativa em que há a explicação correta para <strong><em>esse caso específico</em></strong> do uso da crase."),
     "imagens": [{"arquivo": "q17", "alt": "Tirinha da Mafalda em três quadrinhos. 1: num jardim florido, Mafalda exclama: “Graças a Deus, chegou a primavera!” 2: um senhor idoso, curvado e de bengala, diz a outro: “Graças a Deus, cheguei à primavera”. 3: Mafalda, de cara fechada, pensa: “E eu dizendo trivialidades!”"}],
     "explicacao": "<p>No segundo quadrinho, o idoso diz que “chegou <em>à</em> primavera” (da vida, sobreviveu a mais um inverno). O verbo “chegar” pede a preposição “a”, que se junta ao artigo “a” de “a primavera”, formando a crase. Alternativa <strong>A</strong>.</p><p>A crase aí não é opcional, e quem rege a preposição é o verbo, não o substantivo (B). A pessoa do verbo não determina a crase (C). Não há locução prepositiva (D). E não há pronome possessivo (E).</p>"},
18: {"materia": "Química", "assunto": "Substâncias e misturas",
     "enunciado": BAFOMETRO + P18,
     "explicacao": "<p>Os reagentes são K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub>, H<sub>2</sub>SO<sub>4</sub> e CH<sub>3</sub>CH<sub>2</sub>OH: <strong>três substâncias compostas</strong>, cada uma formada por mais de um elemento. Alternativa <strong>B</strong>.</p><p>Não há substância simples (de um só elemento) nem nos reagentes nem nos produtos (A e C). A substância verde, Cr<sub>2</sub>(SO<sub>4</sub>)<sub>3</sub>, não tem sódio (D). E o ácido dos reagentes é o sulfúrico, não o clorídrico (E).</p>"},
19: {"materia": "Química", "assunto": "Interpretação de dados", "tags": ["concentração"],
     "enunciado": p("Um adulto de 75 kg possui, em média, 5 litros de sangue. Esse adulto foi flagrado, no teste do bafômetro, com nível alcoólico exatamente igual ao limite máximo permitido.",
                    "A massa de álcool contida no sangue desse adulto, em mg, é igual a"),
     "apoio_de": (18, P18),
     "explicacao": "<p>O limite permitido é 0,1 mg por litro de sangue. Com 5 litros: 0,1 · 5 = <strong>0,5 mg</strong>. Alternativa <strong>E</strong>.</p><p>0,1 é a concentração por litro, não a massa total (A). 0,3 é o nível de embriaguez (C). A massa do corpo (75 kg) não entra na conta.</p>"},
20: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": ["verminoses"],
     "explicacao": "<p>As larvas que entram pela pele dos pés descalços, se fixam no intestino e sugam sangue, causando anemia, são do ancilóstomo: a doença é o <strong>amarelão</strong> (ancilostomose). Alternativa <strong>D</strong>.</p><p>A doença de Chagas é causada por um protozoário, transmitido pelo barbeiro (A). Na esquistossomose a larva também penetra pela pele, mas na água, e o verme vive nas veias do fígado (B). A leptospirose é causada por uma bactéria (C). E a teníase vem da carne mal cozida (E).</p>"},
21: {"materia": "Física", "assunto": "Cinemática", "tags": ["velocidade média"],
     "enunciado": RADAR + p("O mínimo intervalo de tempo que o veículo leva para percorrer a distância entre um sensor e outro consecutivo, a fim de não ultrapassar o limite de velocidade é, aproximadamente, de"),
     "imagens": [{"arquivo": "q21", "alt": "Foto de uma rua com radar de velocidade em um poste; no asfalto aparecem as marcas retangulares dos sensores instalados antes do radar."}],
     "explicacao": "<p>Para não passar de 11 m/s, o veículo precisa levar pelo menos t = d ÷ v = 2 ÷ 11 ≈ <strong>0,18 s</strong> entre dois sensores. Alternativa <strong>B</strong>.</p><p>Com menos tempo, a velocidade passaria do limite: em 0,10 s, por exemplo, seriam 20 m/s (A). 0,20 s e 0,22 s respeitam o limite, mas não são o tempo mínimo (C e D).</p>"},
22: {"materia": "Química", "assunto": "Estrutura atômica", "tags": ["teste da chama"],
     "enunciado": apoio(T(9, "O teste da chama é um procedimento", "presente na amostra.")[0])
                  + url("https://tinyurl.com/yb7jxftm", "10.11.2017")
                  + p("A tabela apresenta a cor esperada para os cátions de alguns elementos químicos.")
                  + tabela(["Elemento", "Cor da luz emitida"], [["sódio", "amarela"], ["potássio", "violeta"], ["cálcio", "alaranjada"], ["estrôncio", "vermelha"], ["cobre", "verde"]])
                  + p("A professora de laboratório de Ciências apresenta três amostras de sais: CuSO<sub>4</sub>, KNO<sub>3</sub> e NaCℓ, para os alunos as identificarem com base nessa tabela.",
                      "Assinale a alternativa que relaciona, corretamente, o sal à respectiva cor no teste da chama."),
     "alternativas": colunas(["Sal", "Cor da luz emitida"], [["KNO<sub>3</sub>", "violeta"], ["NaCℓ", "vermelha"], ["CuSO<sub>4</sub>", "amarela"], ["KNO<sub>3</sub>", "alaranjada"], ["CuSO<sub>4</sub>", "alaranjada"]]),
     "explicacao": "<p>O KNO<sub>3</sub> tem o cátion potássio (K<sup>+</sup>), que dá luz <strong>violeta</strong>. Alternativa <strong>A</strong>.</p><p>O NaCℓ tem sódio, que dá luz amarela, não vermelha (B). O CuSO<sub>4</sub> tem cobre, que dá luz verde (C e E). E o potássio não dá luz alaranjada, que é a do cálcio (D).</p>"},
23: {"materia": "Biologia", "assunto": "Citologia",
     "explicacao": "<p>A célula da folha de roseira tem <strong>mitocôndrias</strong>, <strong>cloroplastos</strong>, <strong>parede celular</strong> (de celulose) e <strong>membrana nuclear</strong>, já que é eucariótica. Tem todas as estruturas citadas. Alternativa <strong>E</strong>.</p><p>A célula vegetal também tem mitocôndrias e parede (A). A célula animal não tem cloroplastos (B). A bactéria não tem membrana nuclear, mitocôndrias nem cloroplastos (C). E o fungo e a célula animal têm mitocôndrias e membrana nuclear, e o fungo tem parede celular (D).</p>"},
24: {"materia": "História", "assunto": "Antiguidade", "tags": ["Egito"],
     "enunciado": apoio(*T(10, "Uma equipe internacional de cientistas", "e a do rei.", ["Construída por ordem", "É possível entrar"]))
                  + url("https://tinyurl.com/yd3qv7pu", "14.11.2017") + p("Com base nas informações do texto, é correto afirmar que"),
     "explicacao": "<p>O texto diz que a pirâmide foi construída por ordem do faraó Khufu, que reinou por volta de 2500 a.C., ou seja, há <strong>mais de quatro mil anos</strong>, e que em 2017 foi descoberto um grande espaço vazio no seu interior. Alternativa <strong>C</strong>.</p><p>Ela não tem dois mil anos e deixou de ser a construção mais alta (A). Zeus é um deus grego, e o texto não fala em homenagem a deuses (B). Gizé é o lugar, não uma pessoa (D). E as pirâmides eram túmulos, não palácios residenciais (E).</p>"},
25: {"materia": "Geografia", "assunto": "Biomas brasileiros", "tags": ["caatinga"],
     "explicacao": "<p>A caatinga tem <strong>clima semiárido</strong>, solo raso e pedregoso, e plantas adaptadas à seca, como os cactos, com folhas transformadas em espinhos. Alternativa <strong>D</strong>.</p><p>Folhas coriáceas, caules retorcidos e cascas grossas resistentes ao fogo descrevem o cerrado (A). A maior planície de inundação é o Pantanal (B). Palmeiras, samambaias e mata-paus em grande variedade lembram a Mata Atlântica (C). E clima subtropical com gramíneas é o pampa (E).</p>"},
26: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["enchentes urbanas"],
     "enunciado": p("Leia o texto.") + apoio(sub(T(11, "Um dos problemas urbanos mais dramáticos", "sobre o meio ambiente.")[0], ("de enchentes", "de <em>enchentes</em>")))
                  + url("http://tinyurl.com/y7pe3b38", "14.07.2017")
                  + p("Entre as ações que ajudam a reduzir o risco de enchentes e os problemas decorrentes estão a"),
     "explicacao": "<p>Nas cidades, as enchentes pioram porque o solo impermeabilizado não absorve a chuva e o lixo entope bueiros e rios. <strong>Recuperar as cabeceiras, ampliar as áreas verdes, permeabilizar o solo e descartar o lixo corretamente</strong> faz a água infiltrar e escoar melhor. Alternativa <strong>D</strong>.</p><p>Vegetação na foz não ajuda o escoamento rio acima, e alicerces altos não reduzem o risco (A). Retificar e canalizar rios faz a água correr mais rápido e transbordar mais à frente (B, C e E). E depositar sedimentos e impermeabilizar margens agrava o problema (C e E).</p>"},
27: {"materia": "Geografia", "assunto": "Hidrografia", "tags": ["mata ciliar", "porcentagem"],
     "enunciado": p("Leia os textos e considere o infográfico.")
                  + apoio("• Mata ciliar é a formação vegetal às margens dos rios, córregos, lagos, represas e nascentes. É considerada pelo Código Florestal Federal como Área de Preservação Permanente (APP), com diversas funções ambientais.",
                          "De acordo com o artigo 2<sup>o</sup> desse Código, a largura da faixa de mata ciliar a ser preservada está relacionada com a largura dos rios, córregos, lagos, represas e nascentes, conforme mostra a figura.")
                  + "[[fig:1]]"
                  + apoio("• Fora do estuário, o trecho mais largo do rio Amazonas, não interrompido por ilhas, fica a cerca de 20 km da foz do rio Xingu, onde tem 13 km de largura.")
                  + url("https://tinyurl.com/y9z2e43l", "26.11.2017", "")
                  + p("De acordo com o Código Florestal Federal, para o trecho de um rio cuja largura é 4% da largura do rio Amazonas (citada no texto), a largura da faixa de mata ciliar deve ser, em metros, igual a"),
     "imagens": [{"arquivo": "q27", "alt": "Infográfico de um rio que se alarga da nascente até a foz, com a faixa de mata ciliar exigida em cada trecho: nascente, mata ciliar de 50 m; rio com menos de 10 m de largura, 30 m; de 10 a 50 m, 50 m; de 50 a 200 m, 100 m; de 200 a 600 m, 200 m; acima de 600 m, 500 m."}],
     "explicacao": "<p>4% de 13 km é 0,04 · 13 000 m = 520 m. Um rio de 520 m de largura está na faixa de <strong>200 a 600 m</strong>, que exige mata ciliar de <strong>200 m</strong>. Alternativa <strong>B</strong>.</p><p>500 m é a faixa para rios com mais de 600 m (A). 100, 50 e 30 m valem para rios mais estreitos (C, D e E).</p>"},
28: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": ["vírus e bactérias"],
     "enunciado": p("Um grupo de estudantes conversando sobre a prevenção e o tratamento de diferentes tipos de doenças causadas por vírus e bactérias elaboraram os seguintes enunciados:")
                  + p("<strong>I</strong> Os vírus são acelulares.", "<strong>II</strong> Os vírus e as bactérias não possuem metabolismo próprio.",
                      "<strong>III</strong> As doenças causadas por vírus e bactérias não têm cura.", "<strong>IV</strong> As bactérias são seres parasitas obrigatórios.",
                      "<strong>V</strong> As bactérias são microscópicas.", classe="apoio")
                  + p("Assinale a alternativa que apresenta os enunciados corretos."),
     "explicacao": "<p>Os vírus não têm células (<strong>I</strong> correta), e as bactérias são seres microscópicos (<strong>V</strong> correta). Alternativa <strong>E</strong>.</p><p>As bactérias têm metabolismo próprio; só os vírus dependem de uma célula (II errada). Muitas doenças bacterianas e virais têm cura ou tratamento, como as tratadas com antibióticos (III errada). E muitas bactérias vivem livres no ambiente, não são parasitas obrigatórias (IV errada).</p>"},
29: {"materia": "Geografia", "assunto": "Climatologia", "tags": ["climas do Brasil"],
     "enunciado": p("Carla está organizando um encontro com velhos amigos de turma dos tempos de faculdade, com a intenção de comemorar 10 anos de formados.", "Por uma rede social, Carla manda uma mensagem:")
                  + apoio("Olá pessoal, já está tudo preparado!<br>Reservei um hotel de frente para o rio, contratei um bom churrasqueiro que vai fornecer tudo.<br>Não precisaremos nos preocupar com nada, só festejar e relembrar os velhos tempos.<br>Pessoal, não se esqueçam de trazer roupas leves e guarda-chuvas porque aqui é quente e úmido o ano todo. Marcos, você que está acostumado com o frio dos pampas, vai estranhar um pouco, mas a beleza da floresta e o pôr do sol refletindo nas águas desse riozão vão te recompensar.<br>Abraços a todos e até sexta.<br>Carla")
                  + p("Considerando o mapa e a partir da descrição da mensagem de Carla, assinale a alternativa que apresenta, correta e respectivamente, o número e o clima do local do encontro e do local em que Marcos mora.")
                  + "[[fig:1]]" + url("http://tinyurl.com/yae5jzdo", "13.11.2017", "Original colorido."),
     "imagens": [{"arquivo": "q29", "alt": "Mapa “Climas do Brasil, segundo Arthur Strahler”, com seis regiões numeradas: 1 cobre a Amazônia, no Norte; 2, o Brasil central; 3, o interior do Nordeste; 4, a faixa litorânea do Nordeste ao Sudeste; 5, o Sul; 6, uma área do Sudeste."}],
     "alternativas": colunas(["Local do encontro", "Local em que Marcos mora"], [
         ["6 – clima tropical de altitude", "5 – clima subtropical"], ["2 – clima tropical continental", "1 – clima equatorial"],
         ["4 – clima tropical oceânico", "3 – clima semiárido"], ["1 – clima equatorial", "5 – clima subtropical"], ["3 – clima semiárido", "1 – clima equatorial"]]),
     "explicacao": "<p>Quente e úmido o ano todo, com floresta e um “riozão”: é a Amazônia, área <strong>1</strong>, de <strong>clima equatorial</strong>. Marcos vem do frio dos pampas, no Sul, área <strong>5</strong>, de <strong>clima subtropical</strong>. Alternativa <strong>D</strong>.</p><p>O clima tropical de altitude é mais ameno e não tem calor o ano todo (A). O tropical continental e o semiárido têm estação seca bem marcada (B e E). E o tropical oceânico do litoral não corresponde à floresta e ao grande rio (C). Os pampas não ficam nas áreas 1 nem 3 (B, C e E).</p>"},
30: {"materia": "Biologia", "assunto": "Zoologia", "tags": ["artrópodes"],
     "explicacao": "<p>Todos os animais citados são artrópodes: têm <strong>patas articuladas</strong> e <strong>corpo segmentado</strong>, além de exoesqueleto. Alternativa <strong>B</strong>.</p><p>Todos têm exoesqueleto, não só os aracnídeos (A). Camarões, siris e lacraias também têm antenas (C). Moscas e algumas formigas também têm asas (D). E muitos não são venenosos nem voam (E).</p>"},
31: {"materia": "História", "assunto": "Pré-História", "tags": ["Serra da Capivara"],
     "enunciado": enun(R, 31, trocas=[("[[FIG:p13-2]]", "[[fig:1]]")], tirar_figs=False)
                  + url("https://tinyurl.com/ydhptjlb", "13.11.2017", "Adaptado. Original colorido.")
                  + p("De acordo com o texto e a imagem, assinale a alternativa correta."),
     "imagens": [{"arquivo": "q31", "alt": "Foto de pintura rupestre na rocha: um cervo grande, de chifres longos, e várias figuras humanas pequenas ao redor, como numa cena de caça."}],
     "alternativas": {"A": "Os vestígios de mais de dez mil anos encontrados no Piauí foram excluídos da lista do Patrimônio Mundial por terem sido ameaçados pelas queimadas que destruíram as chapadas.",
                      "B": "As chapadas e os vales do Piauí reúnem os mais antigos registros da presença humana no hemisfério sul, superando os registros africanos, que se acreditava serem os mais remotos."},
     "explicacao": "<p>O texto diz que as pinturas da Serra da Capivara representam “uma grande variedade de temas” e “são os mais antigos registros humanos no continente americano”, e a imagem mostra animais e uma cena de caça. Alternativa <strong>D</strong>.</p><p>O parque está na lista do Patrimônio Mundial (A). O texto fala do continente americano, não do hemisfério sul nem da África (B). Os registros foram feitos por populações pré-históricas, não por europeus (C). E a região fica no Piauí, e os registros têm dezenas de milhares de anos, não dois mil (E).</p>"},
32: {"materia": "Geografia", "assunto": "Agropecuária e meio ambiente", "tags": ["terraceamento"],
     "enunciado": p("Observe a imagem.") + "[[fig:1]]" + url("https://tinyurl.com/37rpb5j", "12.11.2017", "Adaptada. Original colorido.")
                  + p("A imagem está relacionada a um sistema agrícola de subsistência típico de regiões densamente povoadas do globo terrestre.",
                      "Assinale a alternativa correta que apresenta esse tipo de sistema agrícola, a técnica utilizada e a região de ocorrência no globo."),
     "imagens": [{"arquivo": "q32", "alt": "Foto de uma encosta montanhosa recortada em degraus (terraços) alagados, cultivados com arroz."}],
     "alternativas": colunas(["Sistema agrícola", "Técnica agrícola", "Região do mundo"], [
         ["jardinagem", "terraceamento", "Sudeste da Ásia"], ["plantations", "rotação de culturas", "Norte da África"], ["itinerante", "rotação de terras", "Norte da Rússia"],
         ["comercial", "mecanização", "Europa Ocidental"], ["kibutz", "irrigação", "Oriente Médio"]]),
     "explicacao": "<p>A foto mostra arrozais em degraus nas encostas. É a <strong>agricultura de jardinagem</strong>, intensiva e com muita mão de obra, que usa o <strong>terraceamento</strong> e é típica do <strong>Sudeste da Ásia</strong>, muito povoado. Alternativa <strong>A</strong>.</p><p>Plantations são monoculturas de exportação (B). A agricultura itinerante não existe no norte gelado da Rússia (C). A agricultura comercial mecanizada não é de subsistência (D). E kibutz é uma forma de organização coletiva de Israel, não a cena retratada (E).</p>"},
33: {"materia": "Português", "assunto": "Figuras de linguagem", "tags": ["aliteração"],
     "enunciado": p("Leia a letra da música “Segue o seco” de Carlinhos Brown.") + "[[fig:1]]" + url("https://tinyurl.com/yanhydsb", "02.12.2017", "")
                  + p("Um dos importantes aspectos para a interpretação dessa música é a sonoridade de seus versos. A repetição do <strong>fonema consonantal</strong> /s/ – como em “sacar” e “ser” – colabora para a construção e representação do cenário construído pela canção: a seca.",
                      "Selecione a alternativa em que a repetição intencional de fonema consonantal também acontece."),
     "imagens": [{"arquivo": "q33", "alt": "Letra da canção “Segue o seco”, de Carlinhos Brown. Os versos falam da seca do sertão (a boiada, a enxurrada, a trovoada e a enxada secas), repetem muitas palavras com o som de “s”, como “seco”, “sacar” e “sol”, e terminam com um pedido de chuva."},
                 {"arquivo": "q33a", "alt": "Alternativa A: três versos de uma canção de Caetano Veloso em que o eu lírico se diz mulato, com palavras que rimam em “-ato”."},
                 {"arquivo": "q33b", "alt": "Alternativa B: três versos de uma canção de Claudio Lins sobre um olhar trocado entre duas pessoas."},
                 {"arquivo": "q33c", "alt": "Alternativa C: “[...] Vozes veladas, veludosas vozes, / Volúpias dos violões, vozes veladas [...]” Cruz e Sousa."},
                 {"arquivo": "q33d", "alt": "Alternativa D: dois versos de uma canção de Chico Buarque que enumeram de onde vieram o pai, o avô, o bisavô e o tataravô do eu lírico."},
                 {"arquivo": "q33e", "alt": "Alternativa E: “Trabalha e teima, e lima, e sofre, e sua!” Bilac, Olavo."}],
     "alternativas": figs_alt(2),
     "explicacao": "<p>Nos versos de Cruz e Sousa, o som /v/ se repete de propósito em “<strong>v</strong>ozes <strong>v</strong>eladas, <strong>v</strong>eludosas <strong>v</strong>ozes, <strong>V</strong>olúpias dos <strong>v</strong>iolões”, imitando o som suave dos violões. É uma aliteração, como o /s/ da canção. Alternativa <strong>C</strong>.</p><p>Em A, o efeito sonoro vem da rima em “-ato”, não da repetição de uma consoante. Em B e D não há repetição intencional de fonema consonantal. Em E, o verso de Bilac repete a conjunção “e” (polissíndeto), que é uma vogal.</p>"},
34: {"materia": "Geografia", "assunto": "Biomas brasileiros", "tags": ["florestas equatoriais"],
     "enunciado": p("Analise o mapa que apresenta a distribuição de uma das formações vegetais do planeta") + "[[fig:1]]"
                  + fonte("&lt;http://tinyurl.com/y7pgjd6h&gt; Acesso em: 15.1./2017. Adaptado.")
                  + p("Assinale a alternativa que contenha o nome, a localização e um dos problemas que ameaçam essa formação vegetal"),
     "imagens": [{"arquivo": "q34", "alt": "Planisfério com uma formação vegetal destacada em preto: a maior área cobre a Amazônia, na América do Sul; há também manchas na bacia do Congo, na África, e no Sudeste Asiático e na Indonésia, todas próximas à linha do Equador."}],
     "alternativas": colunas(["Nome", "Localização", "Problema"], [
         ["Floresta de Coníferas", "latitudes médias", "exploração da madeira para a indústria de papel"], ["Savanas", "baixas latitudes", "expansão da produção mecanizada de grãos"],
         ["Floresta Temperada", "altas latitudes", "desmatamento para expansão urbana"], ["Pradarias", "altas latitudes", "expansão da agricultura mecanizada de cereais"],
         ["Floresta Equatorial", "baixa latitude", "desmatamento para expansão da agropecuária"]]),
     "explicacao": "<p>As áreas destacadas (Amazônia, Congo, Sudeste Asiático) ficam junto ao Equador: são as <strong>florestas equatoriais</strong>, de <strong>baixa latitude</strong>, ameaçadas sobretudo pelo <strong>desmatamento para a agropecuária</strong>. Alternativa <strong>E</strong>.</p><p>As coníferas ficam em altas latitudes do hemisfério norte (A). As savanas cercam as florestas, mas não coincidem com as áreas do mapa (B). Florestas temperadas e pradarias ficam em latitudes médias (C e D).</p>"},
35: {"materia": "Biologia", "assunto": "Fisiologia animal", "tags": ["hibernação"],
     "explicacao": "<p>Na hibernação, o metabolismo cai: o coração bate devagar, a respiração diminui e a <strong>temperatura do corpo cai muito</strong>, ficando bem abaixo da normal. Assim o animal gasta pouca energia. Alternativa <strong>C</strong>.</p><p>A temperatura não se mantém igual (A e B). Frequências aceleradas aumentariam o gasto de energia (B, D e E). E a temperatura não sobe (E).</p>"},
36: {"materia": "Matemática", "assunto": "Geometria plana", "tags": ["área do trapézio"],
     "enunciado": RESERV + P36,
     "imagens": [{"arquivo": "q36", "alt": "Trapézio retângulo ABCD: A embaixo à esquerda, B embaixo à direita, C em cima à direita e D em cima à esquerda. O lado AD é vertical, perpendicular à base AB; o lado BC é inclinado."}],
     "explicacao": "<p>A área do trapézio é (base maior + base menor) · altura ÷ 2 = (20 + 15) · 12 ÷ 2 = 210 m². Com 3 L por m²: N = 210 · 3 = <strong>630</strong>. Alternativa <strong>D</strong>.</p><p>720 vem de usar um retângulo 20 · 12 (E). 540 vem de 15 · 12 (C).</p>"},
37: {"materia": "Matemática", "assunto": "Geometria plana", "tags": ["teorema de Pitágoras"],
     "enunciado": p("Se, por uma questão de segurança, o reservatório precisa ser cercado, então o comprimento dessa cerca será, em metros, de"),
     "apoio_de": (36, P36),
     "alternativas": {"A": "60.", "B": "59.", "C": "58.", "D": "57.", "E": "56."},
     "explicacao": "<p>Falta o lado BC. Baixando uma perpendicular de C até AB, forma-se um triângulo retângulo com catetos 12 (a altura) e 20 − 15 = 5. Então BC = √(12² + 5²) = √169 = 13 m. O perímetro é 20 + 15 + 12 + 13 = <strong>60 m</strong>. Alternativa <strong>A</strong>.</p><p>Os outros valores vêm de errar o lado inclinado.</p>"},
38: {"materia": "História", "assunto": "Escravidão",
     "enunciado": apoio(*T(16, "A história também é contada", "nascimento do samba.", ["De acordo com as historiadoras"]))
                  + url("https://tinyurl.com/y7mz6urp", "14.11.2017") + p("Assinale a alternativa que corresponde corretamente às informações contidas no texto."),
     "explicacao": "<p>O texto diz que a região do Cais do Valongo, chamada de Pequena África, foi o principal porto de entrada de africanos escravizados e um espaço de encontro de africanos e afro-brasileiros, que marcou a cidade “como o próprio nascimento do samba”. Alternativa <strong>A</strong>.</p><p>O Rio era a “maior cidade escravista das Américas”, não teve escravidão pouco expressiva (B). A Lei Eusébio de Queirós é de 1850, não do século XX (C). A escravidão acabou em 1888, no século XIX, e o texto fala em mais de um milhão de pessoas (D). E esse milhão chegou na primeira metade do século XIX, não entre 1860 e 1910 (E).</p>"},
39: {"materia": "Física", "assunto": "Termologia", "tags": ["calorimetria"],
     "enunciado": p("Para demonstrar a quantidade de calor envolvida em um processo físico, uma professora de Ciências propõe o seguinte experimento a seus alunos.",
                    "Em um recipiente de vidro deve-se colocar 100 g de água destilada e medir a temperatura da mesma.",
                    "Posteriormente, o recipiente é aquecido até o início da ebulição, quando se mede novamente a temperatura da água, obtendo-se o valor de 100 °C.",
                    "A professora apresenta a equação que permite calcular a quantidade de calor envolvida no experimento:")
                  + apoio("\\(Q = m \\cdot c \\cdot \\Delta T\\)", "em que: Q = quantidade de calor (em cal); m = massa (em g); c = calor especifico da água (c = 1 cal/g °C); ∆T = variação de temperatura (em °C)")
                  + p("Supondo que um grupo constatou que a temperatura inicial era de 20 °C, a quantidade de calor necessária para aquecer somente a referida massa de água deve ser de"),
     "explicacao": "<p>A variação de temperatura é 100 − 20 = 80 °C. Então Q = 100 g · 1 cal/g °C · 80 °C = <strong>8 000 cal</strong>. Alternativa <strong>E</strong>.</p><p>Usar 100 °C ou 20 °C no lugar da variação, ou errar a conta, leva aos outros valores.</p>"},
40: {"materia": "Geografia", "assunto": "Cartografia", "tags": ["coordenadas geográficas"],
     "enunciado": p("Leia o texto.")
                  + apoio("<strong>Após sete anos, estádio dividido pela linha do Equador é reaberto no Amapá</strong>", T(17, "A linha do meio de campo", "horário de Brasília).")[0])
                  + url("https://tinyurl.com/2sr57f", "13.11.2017")
                  + p("A notícia destaca a reinauguração do Estádio Estadual Milton de Souza Corrêa, também conhecido como Zerão, pois é cortado ao meio pela linha do Equador de modo que os times jogam em hemisférios diferentes. A linha do Equador divide o planeta em dois hemisférios e é o marco inicial de uma coordenada geográfica.",
                      "Assinale a alternativa que apresenta corretamente"),
     "alternativas": colunas(["Hemisférios", "Coordenada Geográfica"], [["Boreal e Setentrional", "longitude"], ["Ocidental e Oriental", "longitude"], ["Austral e Meridional", "altitude"], ["Leste e Oeste", "latitude"], ["Sul e Norte", "latitude"]]),
     "explicacao": "<p>O Equador separa os hemisférios <strong>Norte e Sul</strong> e é o ponto de partida (0º) da <strong>latitude</strong>. Alternativa <strong>E</strong>.</p><p>Boreal e setentrional são nomes do mesmo hemisfério, o Norte (A), e austral e meridional, do Sul (C). Ocidental e oriental, ou Leste e Oeste, são separados pelo meridiano de Greenwich, ligado à longitude (B e D). E altitude não é coordenada geográfica (C).</p>"},
41: {"materia": "Matemática", "assunto": "Trigonometria", "tags": ["geometria analítica"],
     "enunciado": enun(R, 41, figs={"p17-3": 1}).replace("<p>3</p>", "").replace("ângulo BAC", "ângulo B\\(\\hat{A}\\)C"),
     "imagens": [{"arquivo": "q41", "alt": "Plano cartesiano com eixos x e y em quilômetros. Os pontos A e C estão na mesma altura, com C à direita de A; B está diretamente acima de C. Os três formam um triângulo retângulo em C."}],
     "alternativas": {"A": "\\(\\dfrac{3}{5}\\).", "B": "\\(\\dfrac{3}{4}\\).", "C": "\\(\\dfrac{4}{5}\\).", "D": "\\(\\dfrac{5}{4}\\).", "E": "\\(\\dfrac{4}{3}\\)."},
     "explicacao": "<p>O triângulo é retângulo em C. O cateto oposto ao ângulo BÂC é BC = 15 − 3 = 12, e o adjacente é AC = 18 − 2 = 16. Então tg BÂC = 12/16 = <strong>3/4</strong>. Alternativa <strong>B</strong>.</p><p>A hipotenusa mede 20, então 3/5 e 4/5 são o seno e o cosseno do ângulo (A e C). E 4/3 e 5/4 invertem as razões (D e E).</p>"},
42: {"materia": "Física", "assunto": "Óptica", "tags": ["espelho plano"],
     "enunciado": ESPELHO + P42,
     "imagens": [{"arquivo": "q42a", "alt": "Esquema: uma pessoa (o) à esquerda, um espelho no meio e a imagem (i) à direita, à mesma distância d1 do espelho que a pessoa."},
                 {"arquivo": "q42b", "alt": "Esquema em duas etapas. Em cima: você a 0,5 m do espelho e a imagem a d1 atrás dele. Embaixo: o espelho foi afastado 0,4 m; você fica a d2 do espelho, a imagem fica a d2 atrás dele, e y é a distância total entre você e a imagem."}],
     "explicacao": "<p>Depois do deslocamento, você fica a 0,5 + 0,4 = 0,9 m do espelho. A imagem fica à mesma distância atrás dele. Então y = 0,9 + 0,9 = <strong>1,8 m</strong>. Alternativa <strong>D</strong>.</p><p>0,4 m é só o deslocamento do espelho (A), e 0,8 m é o quanto a imagem se afastou de você (B). 1,0 m era a distância entre você e a imagem antes de mover o espelho (C). E 2,0 m soma errado as distâncias (E).</p>"},
43: {"materia": "Física", "assunto": "Óptica", "tags": ["espelho plano"],
     "enunciado": p("Considere que, na situação anterior, você esteja vestindo uma camiseta com a palavra FÍSICA, conforme a figura.") + "[[fig:2]]"
                  + p("Se você se colocar de frente para o espelho plano, a palavra FÍSICA refletida se apresentará como mostrado na alternativa"),
     "apoio_de": (42, P42),
     "imagens": [{"arquivo": "q43", "alt": "Camiseta com a palavra FÍSICA escrita na frente."},
                 {"arquivo": "q43a", "alt": "Alternativa A: a palavra escrita de trás para a frente e com cada letra espelhada (a primeira é um A e a última um F invertido), como “FÍSICA” vista num espelho."},
                 {"arquivo": "q43b", "alt": "Alternativa B: as letras de trás para a frente, com algumas espelhadas, mas o F na posição normal."},
                 {"arquivo": "q43c", "alt": "Alternativa C: as letras de trás para a frente, com o C e o F na posição normal e o S espelhado."},
                 {"arquivo": "q43d", "alt": "Alternativa D: as letras de trás para a frente, com o C na posição normal e o S e o F espelhados."},
                 {"arquivo": "q43e", "alt": "Alternativa E: as letras de trás para a frente, todas na posição normal, sem espelhar."}],
     "alternativas": figs_alt(3),
     "explicacao": "<p>O espelho plano inverte a direita e a esquerda: a palavra aparece <strong>de trás para a frente</strong> e <strong>cada letra também fica espelhada</strong> (o C e o S se viram e o F aponta para o outro lado). É o que mostra a alternativa <strong>A</strong>.</p><p>Nas outras, pelo menos uma letra não foi espelhada (B, C e D) ou nenhuma foi (E), o que não acontece num espelho.</p>"},
44: {"materia": "Português", "assunto": "Figuras de linguagem", "tags": ["denotação e conotação"],
     "enunciado": JENECI + P44, "imagens": [JENECI_IMG] + [{"arquivo": f"q44{l}", "alt": a} for l, a in zip("abcde", [
         "Alternativa A: “Linguagem denotativa acontece quando a linguagem é utilizada em seu sentido literal.”, com o exemplo do verso sobre os lábios que serão do eu lírico e da pessoa amada.",
         "Alternativa B: “Linguagem conotativa acontece quando a linguagem é utilizada em seu sentido literal.”, com o exemplo do verso sobre os bombons, que acabam e derretem.",
         "Alternativa C: “Linguagem denotativa acontece quando a linguagem é utilizada em seu sentido figurado.”, com o exemplo do verso sobre os discos, que repetem e arranham.",
         "Alternativa D: “Linguagem conotativa acontece quando a linguagem é utilizada em seu sentido figurado.”, com o exemplo do verso sobre os lábios que serão do eu lírico e da pessoa amada.",
         "Alternativa E: “Linguagem denotativa acontece quando a linguagem é utilizada em seu sentido literal.”, com o exemplo do verso sobre as festas, que terminam e choram."])],
     "alternativas": figs_alt(2),
     "explicacao": "<p><strong>Conotação</strong> é o uso da linguagem em <strong>sentido figurado</strong>. No verso em que o eu lírico oferece os lábios, que “ficam”, ele não fala só de uma parte do corpo, mas do amor e da presença que permanecem. Alternativa <strong>D</strong>.</p><p>A e C trocam as definições (denotação é sentido literal) ou dão exemplo figurado como literal. B define conotação como sentido literal. E em E, festas que “choram” é sentido figurado, não literal.</p>"},
45: {"materia": "Português", "assunto": "Pronomes", "tags": ["colocação pronominal"],
     "enunciado": p("Há, nessa música, uma construção gramatical chamada de <u><em>mesóclise</em></u> – “dar-te-ei” – de pouco uso na linguagem escrita e quase extinto o uso na falada. Essa construção, chamada de colocação pronominal, é uma das três posições possíveis – de acordo com a gramática normativa.")
                  + apoio("<strong>Colocação pronominal:</strong> posição dos pronomes oblíquos átonos em relação ao verbo.",
                          "<strong>Ênclise:</strong> quando o pronome oblíquo átono é posicionado depois do verbo.",
                          "<strong>Mesóclise:</strong> quando o pronome oblíquo átono é posicionado entre o radical e a desinência das formas verbais do futuro do presente e futuro do pretérito.",
                          "<strong>Próclise:</strong> quando o pronome oblíquo átono é posicionado antes do verbo.")
                  + p("Baseando-se no que foi apresentado, assinale a alternativa que apresenta uma relação correta – de acordo com a gramática normativa – entre colocação pronominal e o seu uso na frase."),
     "apoio_de": (44, P44),
     "imagens": [{"arquivo": "q45b", "alt": "Alternativa B: “Ênclise” seguida de um verso da canção em que o eu lírico diz que não dará discos à pessoa amada, porque eles repetem; nele, o pronome “te” vem antes do verbo."}],
     "alternativas": {"B": "[[fig:2]]"},
     "explicacao": "<p>Em “Importava-se com o sucesso da prova”, o pronome “se” vem <strong>depois do verbo</strong>, ligado por hífen: é <strong>ênclise</strong>. Alternativa <strong>C</strong>.</p><p>“Faça-me” também é ênclise, não próclise (A). No verso da canção da alternativa B, o pronome vem antes do verbo (próclise). “Cantá-la-rei” está errado: a mesóclise correta seria “cantá-la-ei” (D). E em “Alguém me procurou?” há próclise (E).</p>"},
46: {"materia": "Física", "assunto": "Dinâmica", "tags": ["força resultante"],
     "enunciado": enun(R, 46, figs={"p20-2": 1}),
     "imagens": [{"arquivo": "q46", "alt": "Desenho de uma caixa entre duas crianças: Caio, à esquerda, empurra a caixa para a direita com a força F1; João, à direita, empurra para a esquerda com a força F2."}],
     "explicacao": "<p>Caio empurra para a direita com 100 N e João, para a esquerda com 75 N. A resultante é 25 N para a direita. Para a caixa ficar parada, alguém precisa fazer <strong>25 N para a esquerda</strong>, ou seja, <strong>junto com João</strong>. Alternativa <strong>E</strong>.</p><p>Ajudar Caio aumentaria a resultante (B e D). E 100 N ou 75 N junto com João fariam a caixa ir para a esquerda (A e C).</p>"},
47: {"materia": "História", "assunto": "Brasil Colônia", "tags": ["missões jesuíticas", "Tratado de Madri"],
     "enunciado": MISSOES + P47, "imagens": [MISSOES_IMG],
     "explicacao": "<p>O texto diz que, com o <strong>Tratado de Madri (1750)</strong>, sete povoados guarani a leste do rio Uruguai passaram aos domínios portugueses, e seus habitantes foram obrigados a se mudar, o que levou à guerra. Os povoados foram <strong>diretamente afetados</strong> pelo tratado. Alternativa <strong>D</strong>.</p><p>As missões começaram no início do século XVII; 1756 é o ano da derrota guarani (A). Os guarani resistiram ao tratado e se fixaram, na maioria, na área espanhola (B). Quem fundou as reduções foram jesuítas espanhóis (C). E o tratado que redefiniu os limites foi o de Madri, não o de Tordesilhas (E).</p>"},
48: {"materia": "História", "assunto": "Brasil Colônia", "tags": ["jesuítas"],
     "enunciado": p("Sobre a organização religiosa que fundou os povoados na bacia do Prata, assinale a alternativa correta de acordo com o contexto apresentado no texto e no mapa."),
     "apoio_de": (47, P47),
     "explicacao": "<p>Os padres jesuítas pertencem à <strong>Companhia de Jesus</strong>, que atuou na catequese, na educação e na fundação de aldeamentos na América portuguesa e espanhola. Alternativa <strong>D</strong>.</p><p>Os franciscanos não criaram nações independentes (A). Calvinistas e luteranos eram protestantes, e as coroas ibéricas eram católicas (B e C). E a Ordem de Cristo é portuguesa, não inglesa (E).</p>"},
49: {"materia": "Português", "assunto": "Classes de palavras", "tags": ["orações adjetivas"],
     "enunciado": EVOCE + P49, "imagens": EVOCE_IMG,
     "explicacao": "<p>As orações destacadas começam com o pronome relativo “que” e se referem a “você”, caracterizando essa pessoa (é a que vai com o eu lírico na vida, a que invadiu o espelho). Elas <strong>particularizam o “você”, restringindo-o</strong>. Alternativa <strong>B</strong>.</p><p>Elas não comparam momentos (A), não indicam tempo (C), nem modo ou lugar (D), nem causa (E).</p>"},
50: {"materia": "Português", "assunto": "Classes de palavras", "tags": ["orações adjetivas"],
     "enunciado": p("Ao analisarmos a função que as orações destacadas nos exemplos <strong>I</strong> e <strong>II</strong> exercem, podemos classificá-las como orações"),
     "apoio_de": (49, P49),
     "explicacao": "<p>Orações introduzidas por pronome relativo, que caracterizam um substantivo ou pronome anterior, funcionam como um adjetivo: são <strong>subordinadas adjetivas</strong>. Alternativa <strong>C</strong>.</p><p>Elas não fazem papel de substantivo (A) nem de advérbio (B). E não são coordenadas, porque dependem do termo que caracterizam (D e E).</p>"},
}
completar(Q, R)
