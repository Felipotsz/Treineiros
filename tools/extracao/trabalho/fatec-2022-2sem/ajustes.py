# Ajustes da conferência humana: Vestibular FATEC 2º semestre de 2022 (exame de 08/01/2023)
# Texto conferido com a imagem de cada página. Tema: Agenda 2030 e os 17 ODS (apresentada na capa).
# 54 questões; a prova tem 5 h no total, incluindo a redação (que fica fora do simulado).
# Matéria: a do gabarito oficial; nas "Multidisciplinar", a matéria principal + tag "multidisciplinar".
# Rascunho com colunas embaralhadas: todos os enunciados e alternativas foram escritos aqui.
# Gabarito: oficial (2SEM22), sem anuladas. Letra da canção da NOFX (Q15) como imagem, sem transcrever.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import A, carregar, enun, tabela, colunas, completar, trecho

ID = "fatec-2022-2sem"
META = {
    "id": ID,
    "banca": "FATEC",
    "ano": 2022,
    "semestre": 2,
    "titulo": "Vestibular FATEC, 2º semestre de 2022",
    "fonte": "Centro Paula Souza",
    "dataExame": "2022-07-17",
    "duracaoMinutos": 300,
    "tema": "Objetivos de Desenvolvimento Sustentável",
    "apresentacao": "<p>Prezado(a) candidato(a), em setembro de 2015, representantes de mais de 150 países membros da Organização das Nações Unidas (ONU) decidiram adotar uma agenda comum de desenvolvimento: a Agenda 2030.</p><p>Essa agenda é composta por 17 Objetivos de Desenvolvimento Sustentável (ODS), e tem como metas a atingir até 2030, entre outras, a erradicação da fome e da pobreza, a promoção da saúde e da educação de qualidade, a promoção da igualdade de gênero e a garantia do acesso à água potável.</p><p>Boa prova!</p>",
}
EXTRAS = {"apresentacao": "Quadro com os ícones dos 17 Objetivos de Desenvolvimento Sustentável da ONU, numerados de 1 a 17: erradicação da pobreza; fome zero e agricultura sustentável; saúde e bem-estar; educação de qualidade; igualdade de gênero; água potável e saneamento; energia limpa e acessível; trabalho decente e crescimento econômico; indústria, inovação e infraestrutura; redução das desigualdades; cidades e comunidades sustentáveis; consumo e produção responsáveis; ação contra a mudança global do clima; vida na água; vida terrestre; paz, justiça e instituições eficazes; parcerias e meios de implementação."}

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


def alts(*textos):
    return dict(zip("ABCDE", textos))


def troca(html, pares):
    for a, b in pares:
        assert a in html, a
        html = html.replace(a, b, 1)
    return html


# ---------- textos compartilhados ----------
WUHAN = (chamada("Leia o texto para responder às questões 12 e 13.")
         + apoio(*T(6, "No início da epidemia de COVID–19", "e examinados."), "Constatou-se que:",
                 "• somente 20 dos passageiros selecionados estiveram em Wuhan ou em Huanggang;<br>• exatamente 6 desses 20 passageiros estiveram em Wuhan e em Huanggang; e<br>• nenhum desses 20 passageiros esteve em Ezhou."))
P12 = p("Admita que, dos 36 passageiros selecionados, 17 estiveram em Huanggang.", "Logo, é correto afirmar que o número de passageiros que estiveram em Wuhan é")

SEPHKO = (chamada("Leia os quadrinhos para responder às questões 16 e 17.") + "[[fig:1]]" + url("https://tinyurl.com/vqlsr54", "20.04.2022", "Original colorido."))
SEPHKO_IMG = figs(("q16", "Quadrinhos de Sephko, em inglês, em quatro quadros. 1: “The effort of many scientists” (o esforço de muitos cientistas), com uma cientista fazendo cálculos no papel diante de um computador. 2: “One of the greatest technological challenges” (um dos maiores desafios tecnológicos), com um foguete decolando. 3: “All of this to deliver internet…” (tudo isso para levar internet…), com um satélite em órbita da Terra. 4: “To Billy” (para o Billy), com um homem gritando para o celular: “The Earth is flat!!!!” (a Terra é plana!!!!)."))
P16 = p("O humor se constrói nos quadrinhos a partir da ideia que,")

OLHOS = (chamada("Leia o texto para responder às questões de 26 a 28.")
         + apoio(*T(11, "Uma noite, há anos, acordei bruscamente", "cor de olhos d’água. [...]",
                    ["Sempre ao lado de minha mãe", "Eu me lembrava de algumas", "E foi então que", "E quando, após longos dias", "Vi só lágrimas"]))
         + fonte("Conceição Evaristo, <em>Olhos d’água</em>. Rio de Janeiro: Pallas – Fundação Biblioteca Nacional, 2016."))
P26 = p("A trajetória de vida da narradora-personagem é marcada pela fome, diante da qual a mãe utilizava brincadeiras para distrair as filhas, gerando no texto uma oposição poética entre a <strong>ausência</strong> (de alimentos) e a <strong>abundância</strong> (de imaginação).",
        "Assinale a alternativa em que as expressões representam, respectivamente, o contraste exposto.")

PL = (apoio(*T(12, "A prática da Produção mais Limpa (P+L)", "Ciclo de Vida dos Produtos.", ["Em relação aos processos", "Hoje, no entanto", "A busca pela minimização", "A trajetória dos produtos"]))
      + url("https://tinyurl.com/recsu5q", "10.04.2022"))

IATE = (chamada("Leia o texto para responder às questões 32 e 33.")
        + p(*T(13, "O ODS 7 evoca a necessidade", "não tinha relação com o empresário.", ["Há pouco tempo circulou"]))
        + apoio(*T(13, "O conceito base do projeto chamou", "cerca de 6 945 km.", ["A embarcação conta com"]))
        + url("https://tinyurl.com/trf8o7x", "10.04.2022"))
P32 = p("Sabendo que “1 nó” equivale a “1 milha náutica por hora”, podemos determinar que a embarcação citada no texto vai atingir, em km/h, a velocidade aproximada de")

PLASTICO = (chamada("Leia o texto para responder às questões 36 e 37.")
            + apoio(*T(15, "Os plásticos são insolúveis em água", "interferir na reprodução.", ["Os ecossistemas marinhos", "Pesquisas demonstram"]))
            + url("https://tinyurl.com/t9z9yby", "22.04.2022"))
P36 = p("Acerca das informações relacionadas ao tema tratado no texto, assinale a alternativa correta.")

BIOGAS = (chamada("Leia o texto para responder às questões 41 e 42.")
          + apoio(*T(17, "Em todo o mundo, 1,3 bilhão de toneladas", "para a produção de energia.", ["Biodigestor é um compartimento"])))
P41 = p("Nos biodigestores, ocorre a fermentação da Matéria Orgânica (MO) por microrganismos sem a presença de oxigênio com liberação de energia e de gases tais como CH<sub>4</sub>, H<sub>2</sub>, H<sub>2</sub>S, CO<sub>2</sub>, NH<sub>3</sub>, N<sub>2</sub> e H<sub>2</sub>O.",
        "De acordo com o texto, a equação química simplificada que descreve a fermentação ocorrida nos biodigestores é")

RADIO = (chamada("Leia a resenha sobre o filme <em>Radioactive</em> para responder às questões 49 e 50.")
         + apoio("<em>Radioactive</em> Review", "Director Marjane Satrapi has made a stuffy and patronising drama that does a great disservice to its undeniably fascinating subject",
                 "★☆☆☆☆ (uma estrela de cinco)", *T(20, "As of late, it appears that large sectors", "disastrously unstable reactions."))
         + url("https://tinyurl.com/rysbdux", "20.04.2022")
         + fonte("Glossário: <em>stuffy</em>: chata · <em>patronizing</em>: paternalista · <em>Hidden Figures</em> (filme): Estrelas Além do Tempo"))
P49 = p("De acordo com a resenha, o filme <em>Radioactive</em> obteve crítica negativa, pois")

MALALA = (chamada("Leia o texto para responder às questões 53 e 54.")
          + apoio(*T(21, "Em 12 de julho de 2013, Malala Yousafzai", "lutarem por si mesmas.", ["“Queridos irmãos e irmãs, [...] aqui", "Nós percebemos a importância", "Hoje eu estou focando"]),
                  *T(21, "Queridos irmãos e irmãs, queremos escolas", "podem mudar o mundo.”", ["Queridos irmãos e irmãs, nós não", "Deixem-nos, portanto"]))
          + url("https://tinyurl.com/s7n3xuj", "21.04.2022"))
P53 = p("Após a leitura atenta do discurso, percebe-se que o texto desenvolvido tem por objetivo")

Q = {
1: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": MULTI + ["saneamento", "água potável"],
    "enunciado": apoio(*T(2, "De acordo com um relatório da Organização Mundial", "passaram de 67 % para 71 %.", ["O documento afirma ainda", "Apesar dos dados alarmantes"]))
                 + url("https://tinyurl.com/msv3sc5r", "21.04.2022") + p("Analisando os dados trazidos pela reportagem, podemos concluir corretamente que"),
    "alternativas": alts("a universalização do acesso à água de maneira adequada acarretará o fim da mortalidade infantil.",
                         "o acesso à água potável para a população da Terra não é pleno, mesmo com a melhoria verificada nesse acesso.",
                         "é possível erradicar a COVID–19 e aumentar a qualidade de vida das pessoas mais pobres oferecendo a elas acesso adequado a banheiros e a água potável.",
                         "mais da metade da população da Terra não tem acesso a saneamento básico, que causa a morte de bilhões de pessoas, principalmente no continente europeu.",
                         "o problema do acesso à água potável aos habitantes da Terra cessaria se a água presente nos oceanos fosse distribuída para as pessoas que não utilizam esse bem, pois essa água é rica em sais minerais."),
    "explicacao": "<p>O acesso à água potável subiu de 70% para 74%, mas ainda falta para 26% da população: melhorou, mas não é pleno. Alternativa <strong>B</strong>.</p><p>Água adequada reduz, mas não acaba com a mortalidade infantil (A), e não erradica a COVID-19 (C). Em 2020, 54% tinham saneamento, então menos da metade não tinha, e a Europa é a região mais bem atendida (D). E a água do mar, salgada, não é potável (E).</p>"},
2: {"materia": "Biologia", "assunto": "Separação de misturas", "tags": ["tratamento de água"],
    "enunciado": p("Considerando que a vida na Terra é fortemente dependente de água, entre os ODS destaca-se a melhoria da qualidade da água, a fim de se obter a água potável para todos.",
                   "O processo convencional de tratamento de água é dividido em etapas que aparecem numeradas no esquema.") + "[[fig:1]]"
                 + p("As etapas numeradas 3, 4 e 5 do esquema são denominadas, correta e respectivamente,"),
    "imagens": figs(("q02", "Esquema de uma estação de tratamento de água. (1) Represa, de onde a água é bombeada. (2) Adição de sulfato de alumínio, cal e cloro. (3) Primeiro tanque, onde a água é agitada. (4) Segundo tanque, onde as partículas se depositam no fundo. (5) Tanque com camadas de carvão, areia e cascalho. (6) Adição de flúor, cloro e cal. (7) Reservatório de água final (ETA). (8) Reservatório dos bairros. (9) Distribuição para a cidade.")),
    "alternativas": colunas(["3", "4", "5"], [["coagulação", "desinfecção", "filtração"], ["filtração", "coagulação", "decantação"], ["floculação", "decantação", "filtração"], ["decantação", "filtração", "floculação"], ["floculação", "decantação", "desinfecção"]]),
    "explicacao": "<p>Depois de receber o sulfato de alumínio e a cal (coagulação, etapa 2), a água é agitada para formar flocos (<strong>floculação</strong>, 3). Os flocos se depositam no fundo do tanque (<strong>decantação</strong>, 4) e a água passa por carvão, areia e cascalho (<strong>filtração</strong>, 5). Alternativa <strong>C</strong>.</p><p>A desinfecção, com cloro, vem depois da filtração, na etapa 6 (A e E). E a ordem é floculação, decantação e filtração, não o contrário (B e D).</p>"},
3: {"materia": "História", "assunto": "Antiguidade", "tags": ["Império Romano", "aquedutos"],
    "enunciado": p("Em Roma, no período do Império, as riquezas geradas pelas conquistas permitiram a realização de inúmeras obras públicas, entre as quais os famosos aquedutos, conforme a figura.") + "[[fig:1]]"
                 + url("https://tinyurl.com/36kewcw6", "23.04.2022", "Original colorido.") + p("Essas estruturas arquitetônicas"),
    "imagens": figs(("q03", "Foto de um aqueduto romano de pedra com três andares de arcos sobrepostos sobre um rio, como a Pont du Gard, na França.")),
    "alternativas": alts("eram cópias de projetos de engenharia desenvolvidos pelos povos nômades da pré-história.", "foram construídas para possibilitar a travessia de animais de carga, que levavam armamento pesado.",
                         "transportavam água do Mar do Norte para as províncias dos territórios da Gália Romana, da Grécia continental e do norte da África.",
                         "utilizavam a força da gravidade, por meio de canais de pedra ou tijolo ligeiramente inclinados, para levar água para cidades e vilas do Império Romano.",
                         "eram barreiras militares instaladas em pontos estratégicos para proteção dos rios de fronteira do Império Romano, diante das ameaças de invasão germânica."),
    "explicacao": "<p>Os aquedutos levavam água das nascentes até as cidades por canais com uma leve inclinação: a água corria pela força da gravidade, e os arcos mantinham o declive ao atravessar vales e rios. Alternativa <strong>D</strong>.</p><p>Povos nômades não tinham essas obras (A). Não eram pontes para animais (B) nem barreiras militares (E). E transportavam água doce de nascentes próximas, não água salgada do Mar do Norte (C).</p>"},
4: {"materia": "Matemática", "assunto": "Geometria espacial", "tags": ["volume", "densidade"],
    "enunciado": apoio("É comum que a camada de gelo da Groenlândia derreta durante o verão do Hemisfério Norte. As altas temperaturas registradas em 2019 fizeram o fenômeno começar mais cedo. Só no mês de julho, a Groenlândia perdeu cerca de 198 bilhões de toneladas de gelo, o equivalente a ____________ de piscinas olímpicas.")
                 + url("https://tinyurl.com/qlk43pb", "22.04.2022")
                 + apoio("Dados:<br>• Uma piscina olímpica tem a forma de um bloco retangular de dimensões 50 m de comprimento, 25 m de largura e 2 m de profundidade.<br>• Densidade do gelo: 0,9 kg/L<br>• 1 m<sup>3</sup> = 1 000 L<br>• 1 t = 1 000 kg")
                 + p("O valor que preenche corretamente a lacuna do texto é"),
    "alternativas": alts("75 milhões.", "88 milhões.", "75 bilhões.", "80 bilhões.", "85 trilhões."),
    "explicacao": "<p>A massa é 198 × 10⁹ t = 198 × 10¹² kg. O volume é 198 × 10¹² ÷ 0,9 = 220 × 10¹² L = 220 × 10⁹ m³. Uma piscina tem 50 · 25 · 2 = 2 500 m³. São 220 × 10⁹ ÷ 2 500 = 88 × 10⁶, ou <strong>88 milhões</strong> de piscinas. Alternativa <strong>B</strong>.</p><p>Esquecer a densidade dá 79,2 milhões, perto de A. As outras alternativas erram a potência de dez.</p>"},
5: {"materia": "Química", "assunto": "Separação de misturas", "tags": MULTI + ["tratamento de água", "cloro"],
    "enunciado": apoio(*T(3, "Existem soluções baratas e eficientes para resolver", "dez litros de água.", ["A água armazenada na cisterna"]))
                 + url("https://tinyurl.com/2p8u5695", "19.04.2022")
                 + p("Acerca das informações relacionadas ao tema tratado no texto, complete a frase:")
                 + apoio("O Aqualuz gasta ____<strong>I</strong>____ horas para tratar a água de uma cisterna de 240 litros e não utiliza ____<strong>II</strong>____, que é uma substância simples nociva à saúde utilizada para desinfectar a água em uma etapa nas estações de tratamento.")
                 + p("Assinale a alternativa que preenche, correta e respectivamente, os espaços em branco."),
    "alternativas": colunas(["I", "II"], [["96", "cloreto de ferro (III)"], ["96", "cloro"], ["96", "sulfato de alumínio"], ["44", "cloro"], ["44", "cloreto de ferro (III)"]]),
    "explicacao": "<p>São 240 ÷ 10 = 24 ciclos de 4 horas: 24 · 4 = <strong>96 horas</strong>. A substância simples usada na desinfecção da água é o <strong>cloro</strong> (Cℓ₂), formado por um só elemento. Alternativa <strong>B</strong>.</p><p>Cloreto de ferro (III) e sulfato de alumínio são substâncias compostas e são usados na coagulação, não na desinfecção (A, C e E). E 44 horas não sai da conta (D e E).</p>"},
6: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": MULTI + ["doenças negligenciadas"],
    "enunciado": apoio(*T(4, "Um dos ODS é assegurar uma vida saudável", "esquistossomose e tuberculose.", ["Embora existam financiamentos", "No Brasil, por meio de dados"]))
                 + url("https://tinyurl.com/rmojmk8", "22.04.2022") + p("Assinale a alternativa correta de acordo com o texto."),
    "alternativas": alts("As DTN são consideradas endêmicas porque seus agentes causadores se alastram rapidamente, independentemente das condições de higiene, habitação e saneamento dos locais, atingindo grande parcela da população do país.",
                         "As DTN representam a principal necessidade médica dos países desenvolvidos, devido à ausência de condições adequadas de saneamento básico, tratamento de água e habitação precária.",
                         "As DTN associam-se a vários problemas, dentre as quais a falta de opções terapêuticas, o baixo investimento na produção de vacinas e de novos medicamentos para o tratamento.",
                         "As DTN, típicas das regiões subdesenvolvidas do planeta, são exclusivamente associadas às tendências genéticas das populações dessas regiões.",
                         "As DTN no Brasil estão diretamente associadas à falta de alimentação adequada, a hipovitaminoses, a traumas físicos externos e à ingestão de água contaminada."),
    "explicacao": "<p>O texto diz que as pesquisas sobre as DTN “não se revertem em novos medicamentos, métodos diagnósticos e/ou vacinas”, porque o potencial de lucro é pequeno. Alternativa <strong>C</strong>.</p><p>Elas dependem justamente das condições de higiene e saneamento (A) e afetam sobretudo os países em desenvolvimento (B). Não são genéticas, mas infecciosas (D). E não estão ligadas a hipovitaminoses nem a traumas (E).</p>"},
7: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": ["dengue"],
    "enunciado": p("A dengue, uma doença negligenciada por anos, se alastra rapidamente pelo globo.", "Considerando as características gerais dessa doença, é correto afirmar que"),
    "alternativas": alts("a contaminação ocorre por contato direto com a saliva ou o muco de uma pessoa infectada, por meio de gotículas respiratórias produzidas ao tossir ou espirrar.",
                         "os agentes causadores são microscópicos e dotados de núcleo organizado capaz de orientar a produção de proteínas prejudiciais ao organismo humano.",
                         "a transmissão poderia ser evitada com a eliminação de reservatórios de água parada onde se reproduzem os insetos vetores.",
                         "o tratamento é feito por meio de antibióticos, que inibem a proliferação celular dos agentes causadores da doença.",
                         "a melhor maneira de prevenção é uma vacina específica produzida a partir de bactérias atenuadas ou mortas."),
    "explicacao": "<p>A dengue é transmitida pela picada do mosquito <em>Aedes aegypti</em>, que se reproduz em água parada. Eliminar esses criadouros evita a transmissão. Alternativa <strong>C</strong>.</p><p>A dengue não passa de pessoa para pessoa por gotículas (A). O agente é um vírus, que não tem núcleo (B). Antibióticos não agem contra vírus (D). E a vacina é feita com vírus, não com bactérias (E).</p>"},
8: {"materia": "Química", "assunto": "Soluções", "tags": ["concentração"],
    "enunciado": p(*T(4, "Devido ao consumo exagerado de bebidas alcoólicas", "aproximadamente,", ["O etilômetro (bafômetro)", "A concentração em gramas", "Considere que uma pessoa", "Supondo que todo etanol"]))
                 + apoio("Dados:<br>• concentração de etanol no vinho = 80,2 g/L<br>• uma pessoa adulta apresenta, em média, 5 L de sangue"),
    "alternativas": alts("1,05.", "1,60.", "2,57.", "3,58.", "4,16."),
    "explicacao": "<p>Em 100 mL (0,1 L) de vinho há 80,2 · 0,1 = 8,02 g de etanol. Diluídos em 5 L de sangue: 8,02 ÷ 5 ≈ <strong>1,60 g/L</strong>. Alternativa <strong>B</strong>.</p><p>Os outros valores vêm de erros na conversão de mililitros para litros ou na divisão pelo volume de sangue.</p>"},
9: {"materia": "Química", "assunto": "Química orgânica", "tags": ["fórmula estrutural"],
    "enunciado": p("Um dos medicamentos mais utilizados para o tratamento do alcoolismo é o acamprosato, cuja estrutura está representada na figura.") + "[[fig:1]]"
                 + p("Observando a fórmula estrutural do acamprosato, é correto afirmar que esse composto é"),
    "imagens": figs(("q09", "Fórmula estrutural do acamprosato: CH₃–C(=O)–NH–CH₂–CH₂–CH₂–SO₃H. Um grupo CH₃ ligado a um carbono com dupla ligação a oxigênio, ligado a NH, seguido de três grupos CH₂ e de um grupo SO₃H.")),
    "alternativas": alts("inorgânico, formado por 3 elementos químicos.", "inorgânico, formado por 4 elementos químicos.", "inorgânico, formado por 5 elementos químicos.", "orgânico, formado por 4 elementos químicos.", "orgânico, formado por 5 elementos químicos."),
    "explicacao": "<p>O composto tem uma cadeia de carbonos ligados a hidrogênios: é <strong>orgânico</strong>. Os elementos são C, H, O, N e S: <strong>5</strong>. Alternativa <strong>E</strong>.</p><p>Não é inorgânico (A, B e C). E esquecer o enxofre, do grupo SO₃H, ou o nitrogênio, do NH, dá 4 (D).</p>"},
10: {"materia": "Raciocínio lógico", "assunto": "Analogias",
     "enunciado": p("SIDA está para AIDS assim como 1246 está para"),
     "alternativas": alts("1462.", "6421.", "6241.", "2461.", "4612."),
     "explicacao": "<p>Numerando as letras de SIDA (S = 1, I = 2, D = 3, A = 4), a palavra AIDS corresponde à ordem 4, 2, 3, 1. Aplicando essa ordem a 1246 (1º = 1, 2º = 2, 3º = 4, 4º = 6), temos 4º, 2º, 3º, 1º = 6, 2, 4, 1: <strong>6241</strong>. Alternativa <strong>C</strong>.</p><p>As outras alternativas usam outras permutações dos algarismos.</p>"},
11: {"materia": "História", "assunto": "Brasil República", "tags": MULTI + ["Revolta da Vacina"],
     "enunciado": p("Em 1904, as autoridades propuseram uma política de saúde pública para a cidade do Rio de Janeiro. Esta política gerou uma grande revolta popular.",
                    "Tanto a atuação do diretor de saúde pública quanto sua política foram satirizadas pelos jornais da época, que publicaram charges como a da figura.") + "[[fig:1]]"
                  + url("https://tinyurl.com/ulwjbys", "23.04.2022", "") + p("Assinale a alternativa que apresenta, corretamente, o contexto histórico a que a charge faz referência."),
     "imagens": figs(("q11", "Charge antiga: um homem com a inscrição “Oswaldo, o Esfolador” no casaco ergue um chicote e segura pelo colarinho um homem do povo, assustado, que tenta se afastar; ao fundo, silhuetas de guardas.")),
     "alternativas": alts("O aumento no número de moradores de rua provocou epidemias de leptospirose, hanseníase e dengue, e levou o governo de Oswald de Andrade a deportar essas pessoas para os morros cariocas.",
                          "A Lei do Esgoto, criada por Osvaldo Aranha, sob pressão dos administradores da Companhia City de Urbanização, deslocou famílias pobres para bairros sem acesso a sistemas de tratamento de resíduos.",
                          "A população do Rio de Janeiro reagiu à política sanitarista de Oswaldo Cruz, que incluía a vacinação forçada, iniciando a Revolta da Vacina, que deixou 30 mortos e centenas de pessoas feridas, presas e deportadas.",
                          "O presidente Getúlio Vargas alterou as leis sanitárias e permitiu o escoamento de grandes volumes de esgoto da capital federal, Rio de Janeiro, em direção ao interior de São Paulo, o que prejudicou a população rural.",
                          "O envio forçado de pessoas doentes para colônias de leprosos na Amazônia brasileira provocou uma onda de protestos contra o presidente Arthur Bernardes, reprimidos com violência pela força policial do Rio de Janeiro."),
     "explicacao": "<p>Em 1904, o sanitarista Oswaldo Cruz, diretor de saúde pública, tornou obrigatória a vacina contra a varíola. A vacinação à força, somada às demolições de cortiços, provocou a <strong>Revolta da Vacina</strong>. A charge o mostra como um “esfolador” que agride o povo. Alternativa <strong>C</strong>.</p><p>Oswald de Andrade foi escritor (A), Osvaldo Aranha e Getúlio Vargas atuaram a partir de 1930 (B e D), e Arthur Bernardes governou de 1922 a 1926 (E).</p>"},
12: {"materia": "Raciocínio lógico", "assunto": "Lógica", "tags": ["conjuntos"],
     "enunciado": WUHAN + P12,
     "alternativas": alts("3.", "6.", "9.", "12.", "15."),
     "explicacao": "<p>Pela união de conjuntos, n(W ∪ H) = n(W) + n(H) − n(W ∩ H): 20 = n(W) + 17 − 6, então n(W) = <strong>9</strong>. Alternativa <strong>C</strong>.</p><p>3 é o número de quem esteve só em Wuhan (A). 6 é a interseção (B). E 15 viria de esquecer de descontar a interseção (E).</p>"},
13: {"materia": "Matemática", "assunto": "Probabilidade",
     "enunciado": p("Escolhendo-se um passageiro ao acaso, dentre os selecionados e examinados, a probabilidade de ele ter estado em exatamente duas das três cidades citadas no texto é de"), "apoio_de": (12, P12),
     "alternativas": alts("\\(\\dfrac{1}{6}\\).", "\\(\\dfrac{1}{3}\\).", "\\(\\dfrac{5}{9}\\).", "\\(\\dfrac{7}{9}\\).", "\\(\\dfrac{17}{36}\\)."),
     "explicacao": "<p>Quem esteve em Wuhan ou Huanggang não foi a Ezhou. Então, entre esses 20, só os 6 que foram a Wuhan e Huanggang estiveram em exatamente duas cidades. Os outros 16 não estiveram nem em Wuhan nem em Huanggang, então estiveram no máximo em Ezhou. A probabilidade é 6 ÷ 36 = <strong>1/6</strong>. Alternativa <strong>A</strong>.</p><p>1/3 viria de usar 12 casos (B), e 17/36 usa o total de Huanggang (E).</p>"},
14: {"materia": "Raciocínio lógico", "assunto": "Interpretação de dados", "tags": MULTI + ["função do 1º grau"],
     "enunciado": p("Considere os grupos A e B que não possuem acesso universal a serviços de água potável.",
                    "O plano cartesiano da figura apresenta os gráficos com as previsões de essas populações atingirem o acesso universal a serviços de água potável nos próximos 15 anos.",
                    "Suponha que essas previsões tenham crescimentos lineares.") + "[[fig:1]]" + p("Analise o gráfico e assinale a alternativa correta."),
     "imagens": figs(("q14", "Gráfico da previsão de acesso a serviços de água potável (%) por anos. Duas retas chegam juntas a 100% em 15 anos. A do grupo A (linha contínua) parte de cerca de 80% e sobe pouco. A do grupo B (linha tracejada) parte de cerca de 25% e sobe muito mais.")),
     "alternativas": alts("A previsão é de que o grupo B atinja o acesso universal num intervalo de tempo menor do que o do grupo A.", "A previsão é de que o grupo A atinja o acesso universal num intervalo de tempo menor do que o do grupo B.",
                          "ao final desses 15 anos, nenhum grupo atingirá o acesso universal.", "A taxa de crescimento da previsão de acesso do grupo A é maior do que a do grupo B.", "A taxa de crescimento da previsão de acesso do grupo B é maior do que a do grupo A."),
     "explicacao": "<p>As duas retas chegam a 100% no mesmo instante, aos 15 anos. Como o grupo B parte de um valor bem menor, sua reta é mais inclinada: a <strong>taxa de crescimento</strong> de B é maior. Alternativa <strong>E</strong>.</p><p>Os dois grupos atingem o acesso universal ao mesmo tempo, aos 15 anos (A, B e C). E a inclinação de A é menor (D).</p>"},
15: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": ["letra de canção"],
     "enunciado": p("Considere o excerto da música <em>Idiots are taking over</em>, da banda de punk rock NOFX.") + "[[fig:1]]"
                  + fonte("Glossário: <em>fittest</em>: mais apto · <em>worsen</em>: piorar · <em>mob</em>: multidão · <em>inbred</em>: inato") + p("Segundo o texto, é correto afirmar que"),
     "imagens": figs(("q15", "Trecho da letra da canção “Idiots Are Taking Over”, da banda NOFX, em inglês, em três estrofes. A letra diz que os idiotas tomaram o poder e se espalham como um câncer social; que Darwin estaria se revirando no caixão, porque os mais aptos sobrevivem cada vez menos e a mentalidade de multidão raivosa virou regra; e que não há sentido na democracia quando a ignorância é celebrada, já que o voto de um cientista político vale o mesmo que o de qualquer pessoa. Fonte: &lt;https://tinyurl.com/twd3lby&gt; Acesso em: 20.04.2022. Adaptado.")),
     "alternativas": alts("apenas cientistas políticos poderão controlar uma grande massa ignorante.", "a democracia atualmente pressupõe a ignorância celebrada pela sociedade.", "há a disseminação de uma doença social causada por vícios como o álcool.",
                          "pessoas ignorantes e tolas estão assumindo postos de destaque.", "Darwin, cuja teoria criacionista foi banida, está se revirando no caixão."),
     "explicacao": "<p>O título e o refrão dizem que “os idiotas estão assumindo o controle” (<em>taking over</em>): pessoas tolas e ignorantes passam a ocupar posições de destaque. Alternativa <strong>D</strong>.</p><p>A letra diz que o voto do cientista político vale o mesmo que o de qualquer um, e não que ele controlará as massas (A). Ela critica a democracia em que a ignorância é celebrada, não diz que a democracia a pressupõe (B). O “câncer social” é a ignorância, não o álcool (C). E a teoria de Darwin é a da evolução, não o criacionismo (E).</p>"},
16: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": ["quadrinhos"],
     "enunciado": SEPHKO + P16, "imagens": SEPHKO_IMG,
     "alternativas": alts("apesar de todo o empenho científico para o desenvolvimento da internet, a rede permite opiniões que contradizem a ciência.", "apesar de serem pessoas diferentes, a cientista e Billy compartilham das mesmas opiniões acerca da ciência.",
                          "apesar dos esforços dos cientistas, os satélites lançados ainda não conseguiram entrar em órbita.", "apesar dos avanços tecnológicos, os cientistas ainda não conseguiram calcular o diâmetro da Terra.",
                          "apesar de ter tantos computadores sofisticados, a cientista somente consegue fazer cálculos no papel."),
     "explicacao": "<p>Os três primeiros quadros mostram o enorme esforço científico para levar a internet às pessoas; no último, Billy usa essa internet para dizer que a Terra é plana, negando a própria ciência que a criou. Alternativa <strong>A</strong>.</p><p>A cientista e Billy pensam o oposto (B). O satélite está em órbita (C). O quadrinho não fala do diâmetro da Terra (D) nem critica o uso do papel (E).</p>"},
17: {"materia": "Física", "assunto": "Dinâmica", "tags": ["leis de Newton"],
     "enunciado": p(*T(8, "Para garantir o acesso igualitário e amplo", "da Mecânica Clássica."), "Podemos afirmar corretamente que um conceito representado no segundo quadrinho se refere ao princípio"),
     "apoio_de": (16, P16),
     "alternativas": alts("da incerteza.", "da ação e reação.", "de Arquimedes.", "de Heisenberg.", "de Pascal."),
     "explicacao": "<p>O foguete empurra os gases para baixo, e os gases empurram o foguete para cima com uma força de mesma intensidade e sentido oposto: é a 3ª lei de Newton, o princípio da <strong>ação e reação</strong>. Alternativa <strong>B</strong>.</p><p>O princípio da incerteza, de Heisenberg, é da Física Quântica, não da Mecânica Clássica (A e D). Os princípios de Arquimedes (empuxo) e de Pascal (pressão nos fluidos) não explicam a decolagem (C e E).</p>"},
18: {"materia": "História", "assunto": "Brasil Colônia", "tags": ["mineração"],
     "explicacao": "<p>No século XVIII, a mineração em Minas Gerais buscava ouro e diamantes e usava sobretudo mão de obra escravizada. Hoje, o principal minério exportado pelo estado é o <strong>minério de ferro</strong>. Alternativa <strong>B</strong>.</p><p>O nióbio não era explorado no período colonial (A). A região só foi explorada a partir do fim do século XVII, não nos séculos XIV ou XV (C e E). Minas era a maior produtora de ouro da colônia, e a mineração é uma das principais atividades do estado (D). E não há escravizados hoje (E).</p>"},
19: {"materia": "Geografia", "assunto": "População", "tags": ["taxa de fecundidade"],
     "enunciado": apoio(*T(8, "A taxa de fecundidade de 1,48 filho por mulher", "ou mais filhos.", ["Embora a taxa de fecundidade", "O governo anunciou"]))
                  + url("https://tinyurl.com/rcm3vhu", "10.04.2022") + p("As propostas do governo russo para aumentar a taxa de fecundidade naquele país decorrem da"),
     "explicacao": "<p>Para uma população se manter estável, cada mulher precisa ter, em média, cerca de 2,1 filhos (a taxa de reposição). Com 1,48, a população nativa russa tende a <strong>diminuir</strong>. Alternativa <strong>C</strong>.</p><p>Os imigrantes não superam os nascidos na Rússia (A). A densidade demográfica russa é baixa, não está entre as maiores (B). O UNICEF não faz esse tipo de exigência (D). E a população russa se concentra no oeste, na parte europeia, e o leste e o norte, na Sibéria, são pouco povoados (E).</p>"},
20: {"materia": "Matemática", "assunto": "Geometria plana", "tags": ["área", "energia solar"],
     "enunciado": p(*T(9, "João, preocupado com nosso planeta", "por dia. Após estudar o problema, adquiriu módulos solares fotovoltaicos com forma retangular e as seguintes características:"),
                    "• potência diária gerada por módulo: 265 W; e<br>• dimensão de cada módulo: 1,65 m por 1,00 m, com espessura desprezível.",
                    *T(9, "Os módulos serão instalados no telhado", "para atender suas necessidades.", ["Assinale a alternativa"]))
                  + apoio("Despreze quaisquer formas de perda de energia."),
     "explicacao": "<p>São necessários 2 120 ÷ 265 = 8 módulos. Cada um ocupa 1,65 · 1,00 = 1,65 m². A área total é 8 · 1,65 = <strong>13,2 m²</strong>. Alternativa <strong>B</strong>.</p><p>As outras áreas correspondem a números de módulos que não são inteiros.</p>"},
21: {"materia": "Geografia", "assunto": "População", "tags": MULTI + ["desemprego"],
     "enunciado": apoio(*T(9, "De acordo com o Instituto Brasileiro de Geografia", "e de pardos, 13,6 %.", ["Segundo dados do IBGE", "Esse grupo tem a 2ª", "A taxa de desemprego no período", "No período, o desemprego"]))
                  + url("https://tinyurl.com/rsspqcs", "21.04.2022") + p("Sobre o desemprego no Brasil e de acordo com o texto, é correto afirmar que a taxa de desemprego é maior"),
     "explicacao": "<p>A maior taxa do texto é a dos jovens de 14 a 17 anos (40,6%). Um dos fatores é a exigência de experiência e qualificação, que os mais jovens ainda não têm. Alternativa <strong>E</strong>.</p><p>A faixa de 18 a 24 anos tem a 2ª maior taxa, e a falta de qualificação, não o excesso, é que dificulta (A). A taxa é maior entre as mulheres, mas porque historicamente elas ganham menos e enfrentam mais barreiras (B e C). E a taxa maior entre pretos se deve à desigualdade, não à maior escolaridade (D).</p>"},
22: {"materia": "Matemática", "assunto": "Porcentagem", "tags": ["variações sucessivas"],
     "enunciado": p("Leia a reportagem publicada em 21.05.2019.")
                  + apoio(*T(9, "Segundo estudo do Instituto Brasileiro de Economia", "pobres apresentou:", ["O estudo revela"]),
                          "• aumento de 10 % da renda acumulada, no período de 2012 a 2015; e<br>• redução de 20 % da renda acumulada, no período de 2016 a março de 2019.")
                  + url("https://tinyurl.com/5bh2rp9v", "22.04.2022")
                  + p("A partir das informações do texto, assinale a alternativa que apresenta a queda acumulada na variação de renda da população mais pobre, de 2012 a março de 2019."),
     "alternativas": alts("10 %", "11 %", "12 %", "13 %", "14 %"),
     "explicacao": "<p>Variações sucessivas se multiplicam: 1,10 · 0,80 = 0,88. A renda final é 88% da inicial, uma queda acumulada de <strong>12%</strong>. Alternativa <strong>C</strong>.</p><p>Somar as porcentagens (+10% − 20%) daria uma queda de 10%, que é a armadilha da questão (A).</p>"},
23: {"materia": "História", "assunto": "História contemporânea", "tags": ["apartheid"],
     "enunciado": apoio(T(10, "A legislação estabeleceu acessos diferenciados", "da dos brancos.")[0])
                  + fonte("Araribá plus: história. 9. 4ªed. São Paulo: Moderna, 2014, p.197.") + p("O texto faz referência ao regime de segregação conhecido como"),
     "explicacao": "<p>A classificação dos sul-africanos por raça, a separação dos espaços e a proibição dos casamentos inter-raciais definem o <strong>apartheid</strong>, regime de segregação racial da África do Sul (1948–1994). Alternativa <strong>A</strong>.</p><p>A Secessão foi a guerra civil dos Estados Unidos (B). Black Power e Black Lives Matter são movimentos contra o racismo (C e E). E o antissemitismo é a discriminação contra judeus (D).</p>"},
24: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["Bolsa Família", "transferência de renda"],
     "enunciado": p("Leia o texto extraído do site do Ministério da Cidadania.")
                  + apoio(*T(10, "O Bolsa Família era um programa", "executava os pagamentos.", ["O Bolsa Família possuía"]))
                  + url("https://tinyurl.com/2p9abjm6", "10.04.2022") + p("Esse programa"),
     "explicacao": "<p>Ao complementar a renda das famílias mais pobres, o programa fazia do Estado um agente de <strong>redistribuição de renda</strong>, o que também movimenta a economia local. Alternativa <strong>B</strong>.</p><p>O programa não tratava de reforma agrária (A), não criou bancos: a Caixa fazia os pagamentos (C), não provocou demissões em massa (D) e era gerido pelos governos, não por ONGs (E).</p>"},
25: {"materia": "Raciocínio lógico", "assunto": "Sequências", "tags": ["calendário"],
     "enunciado": p(*T(10, "Todos os anos, milhares de pessoas tentam chegar", "imigração descritas.", ["Suponha que um país deseje", "Para receber esses imigrantes", "Assinale a alternativa que apresenta"])),
     "explicacao": "<p>Num mês de 31 dias, os dias 30 e 31 caem num sábado e num domingo. Então o dia 29 é sexta-feira. Como 29 − 1 = 28 é múltiplo de 7, o dia 1 cai no mesmo dia da semana que o dia 29: <strong>sexta-feira</strong>. Alternativa <strong>B</strong>.</p><p>Os outros dias da semana resultam de errar a contagem por um ou mais dias.</p>"},
26: {"materia": "Português", "assunto": "Texto literário", "tags": ["antítese"],
     "enunciado": OLHOS + P26,
     "explicacao": "<p>“Cheiro algum” mostra a falta de comida na panela (ausência), e “mãe era a Senhora, a Rainha” mostra a brincadeira inventada pela mãe nesses dias (abundância de imaginação). As duas estão no 3º parágrafo. Alternativa <strong>D</strong>.</p><p>“Silêncio nas horas” e “cheia de culpa” não falam de comida nem de imaginação (A). Em B e C, a ordem está invertida ou as duas expressões indicam a mesma ideia. E “rios caudalosos” se refere às lágrimas da mãe, não à imaginação (E).</p>"},
27: {"materia": "Português", "assunto": "Figuras de linguagem", "tags": ["metáfora"],
     "enunciado": p("Para reforçar a metáfora “cor de olhos d’água”, a autora do texto utiliza duas expressões relacionadas às águas: “rios caudalosos” e “águas correntezas”.",
                    "Essas locuções, além de exprimirem os sentimentos vivenciados pela mãe da narradora, também representam, respectivamente,"),
     "apoio_de": (26, P26),
     "explicacao": "<p>Rios caudalosos são rios cheios, de muita água: sugerem <strong>abundância</strong>. Correntezas são águas que avançam com ímpeto: sugerem <strong>força</strong>, a força da mãe que resiste. Alternativa <strong>E</strong>.</p><p>Escassez, insignificância, fraqueza, desilusão e miséria têm sentido oposto ao das imagens de água abundante e em movimento (A, B, C e D).</p>"},
28: {"materia": "Português", "assunto": "Figuras de linguagem", "tags": ["personificação"],
     "enunciado": p("A personificação é uma figura de linguagem amplamente empregada pela autora, por meio da qual ela dá vida ou traços humanos a objetos inanimados.", "Assinale a alternativa em que esse recurso é empregado"),
     "apoio_de": (26, P26),
     "alternativas": alts("Eu me lembrava de algumas histórias da infância de minha mãe.", "As labaredas [...] pareciam debochar do vazio de nosso estômago.", "...a brincadeira preferida era aquela em que a mãe era a Senhora, a Rainha.",
                          "Felizes, colhíamos flores cultivadas...", "...pude contemplar extasiada os olhos de minha mãe."),
     "explicacao": "<p>“Debochar” é uma ação humana, atribuída às labaredas, que são inanimadas: é personificação. Alternativa <strong>B</strong>.</p><p>Nas outras frases, quem age são pessoas (a narradora, a mãe, as filhas), sem atribuir traços humanos a objetos (A, C, D e E).</p>"},
29: {"materia": "Raciocínio lógico", "assunto": "Lógica", "tags": ["dedução"],
     "enunciado": p("Uma das metas estabelecidas pelos ODS é acabar com o tráfico de espécies da fauna e da flora.", "Suponha que, em uma determinada agência governamental,",
                    "• todas as investigações sobre tráfico de espécies ou são apenas casos que envolvem espécies da fauna ou são apenas casos que envolvem espécies da flora; e<br>• as investigações sobre casos que envolvem espécies da fauna não serão arquivadas.",
                    "É correto concluir que"),
     "alternativas": alts("toda investigação de casos que envolvem espécies da flora será arquivada.", "toda investigação que será arquivada é um caso que envolve espécies da flora.",
                          "um caso de uma investigação que não é arquivada com certeza envolve espécies da fauna.", "algumas investigações que serão arquivadas envolvem espécies da fauna.",
                          "nenhuma investigação que envolve espécies da flora será arquivada."),
     "explicacao": "<p>Toda investigação é só de fauna ou só de flora, e as de fauna nunca são arquivadas. Logo, se uma investigação foi arquivada, ela não é de fauna, e portanto é de flora. Alternativa <strong>B</strong>.</p><p>Nada garante que todas as de flora serão arquivadas (A), nem que nenhuma será (E). Uma investigação não arquivada pode ser de flora (C). E nenhuma de fauna é arquivada (D).</p>"},
30: {"materia": "Geografia", "assunto": "Biomas brasileiros", "tags": ["Pantanal"],
     "enunciado": p(*T(12, "Entre os objetivos propostos pela Agenda 2030", "assinale a alternativa correta.", ["Como exemplos de áreas úmidas", "A fim de conservar melhor", "Sobre esse bioma"])),
     "alternativas": alts("Apresenta vegetação constituída predominantemente por gramíneas e fauna de vertebrados formada principalmente por roedores, como hamsters e marmotas, além de carnívoros, como coiotes e alces.",
                          "Apesar de estarem em solo encharcado, as plantas desse bioma não absorvem água com eficiência devido às constantes temperaturas do solo abaixo de 5 °C e sofrem com a desidratação, processo chamado de seca fisiológica.",
                          "Ocupa cerca de 10 % do território brasileiro, estendendo-se principalmente pelos estados de Sergipe, Alagoas, Bahia e pelo norte de Minas Gerais. Entre as espécies vegetais, apresenta o pau-brasil, orquídeas e samambaias. A fauna se destaca pela presença do mico-leão-dourado, onças, guepardos e raposas.",
                          "Localiza-se na faixa equatorial do planeta, com fauna rica e abundante. A vegetação apresenta árvores de grande porte, cujas copas mais altas formam um “teto” de vegetação, sob o qual existe um patamar interno, formado pelas copas de árvores mais baixas.",
                          "Apresenta elevada biodiversidade, em que a fauna de vertebrados abunda, no meio aquático, em peixes, e no meio terrestre, em aves, capivaras, antas, onças, jacarés e serpentes. A flora é principalmente constituída por ervas, arbustos e árvores diversas, como palmeiras, ipês e aroeiras."),
     "explicacao": "<p>O Pantanal tem enorme biodiversidade: peixes nas águas e, em terra, aves, capivaras, antas, onças, jacarés e serpentes, com vegetação variada de campos, arbustos e árvores como palmeiras, ipês e aroeiras. Alternativa <strong>E</strong>.</p><p>A descreve pradarias da América do Norte (hamsters, marmotas e coiotes não são do Pantanal). B descreve a tundra, com solo gelado. C mistura Mata Atlântica e Caatinga, e guepardos são africanos. D descreve a floresta equatorial, e o Pantanal fica no Centro-Oeste.</p>"},
31: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["produção mais limpa", "ciclo de vida"],
     "enunciado": PL + p("De acordo com o texto, é correto afirmar que"),
     "alternativas": alts("o fim dos impactos ambientais ocorrerá no momento em que o percurso dos produtos a partir de sua produção for monitorado pela sociedade.",
                          "o rumo a ser seguido para atingirmos a sustentabilidade passa pela utilização dos combustíveis fósseis e sem a utilização de energia nuclear.",
                          "o ciclo da vida dos produtos é a redução do uso de materiais tóxicos e a eliminação, pela queima, de todos os resíduos gerados pelos sistemas produtivos.",
                          "a diretriz escolhida na busca pela sustentabilidade passa obrigatoriamente pela desassociação entre produção mais limpa e consumo mais limpo, pois são ações divergentes.",
                          "a redução dos impactos ambientais implica buscar a diminuição e mesmo a eliminação de processos nocivos ao meio ambiente, da extração da matéria-prima ao uso e ao descarte final de objetos."),
     "explicacao": "<p>O texto diz que minimizar os impactos deve incluir todo o percurso dos produtos, “desde a extração dos recursos naturais” até a “destinação final”: é o ciclo de vida dos produtos. Alternativa <strong>E</strong>.</p><p>O texto fala em minimizar os impactos, não em acabar com eles (A), e não trata de combustíveis fósseis nem de energia nuclear (B). O ciclo de vida é a trajetória do produto, não a queima de resíduos (C). E produção e consumo mais limpos são complementares (D).</p>"},
32: {"materia": "Física", "assunto": "Cinemática", "tags": ["conversão de unidades"],
     "enunciado": IATE + P32,
     "alternativas": alts("408.", "220.", "31.", "17.", "2."),
     "explicacao": "<p>O texto diz que 3 750 milhas náuticas equivalem a cerca de 6 945 km: 1 milha náutica ≈ 6 945 ÷ 3 750 ≈ 1,85 km. Então 17 nós = 17 milhas náuticas por hora ≈ 17 · 1,85 ≈ <strong>31 km/h</strong>. Alternativa <strong>C</strong>.</p><p>17 é o valor em nós, sem converter (D). E os outros valores vêm de dividir em vez de multiplicar ou de usar as distâncias de forma errada.</p>"},
33: {"materia": "Física", "assunto": "Termologia", "tags": ["escalas termométricas"],
     "enunciado": p("De acordo com o texto, o hidrogênio é resfriado à temperatura de"), "apoio_de": (32, P32),
     "alternativas": alts("zero absoluto.", "20 K acima do zero absoluto.", "20 K abaixo do zero absoluto.", "526 K acima do zero absoluto.", "526 K abaixo do zero absoluto."),
     "explicacao": "<p>T(K) = T(°C) + 273 = −253 + 273 = 20 K. O zero absoluto é 0 K, então o hidrogênio fica <strong>20 K acima do zero absoluto</strong>. Alternativa <strong>B</strong>.</p><p>Não existe temperatura abaixo do zero absoluto (C e E). E 526 vem de somar 253 e 273 (D e E).</p>"},
34: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["queimadas"],
     "enunciado": apoio(*T(14, "Na Austrália a temporada de incêndios florestais", "para o fogo se expandir.", ["Um mês antes, em agosto", "Mas os casos não são similares", "Na Amazônia, as plantas"]))
                  + url("https://tinyurl.com/2p8dmtm8", "19.04.2022") + p("De acordo com o texto, é correto afirmar que"),
     "alternativas": alts("as altas temperaturas verificadas tanto na Amazônia quanto na Austrália foram as causas dos incêndios em ambas as matas.",
                          "tanto a floresta amazônica quanto as florestas australianas são acostumadas com o fogo e, portanto, poderão se regenerar rapidamente.",
                          "as mudanças climáticas contribuíram para a propagação dos incêndios em áreas florestais da Amazônia e da Austrália, apesar de as causas das queimadas não serem semelhantes.",
                          "a queimada na Amazônia ocorreu pelo aumento do processo de desertificação a que essa área está exposta, diferentemente da Austrália, país de clima frio, onde não existem desertos.",
                          "as florestas australianas, por serem úmidas, não pegam fogo de maneira espontânea, diferentemente da floresta amazônica que, em função do tempo seco, fica exposta a queimadas naturais."),
     "explicacao": "<p>O texto diz que os casos “não são similares”: na Austrália, os incêndios são naturais; na Amazônia, a floresta “só queima se alguém colocar fogo”. Mas as mudanças climáticas facilitaram a expansão do fogo. Alternativa <strong>C</strong>.</p><p>Na Amazônia a causa é humana, não o calor (A), e as plantas de lá não são adaptadas ao fogo (B). O texto não fala em desertificação, e a Austrália tem clima quente e muitos desertos (D). E a floresta úmida é a amazônica; a australiana é seca (E).</p>"},
35: {"materia": "Química", "assunto": "Química orgânica", "tags": ["reciclagem", "nomenclatura"],
     "enunciado": p(*T(14, "A reciclagem terciária é a aplicação", "ácido clorídrico, HCl (reação 1).", ["Um dos processos utilizados", "A pirólise do PVC"]))
                  + apoio("Reação 1 &nbsp; PVC → HCℓ + C<sub>2</sub>H<sub>4</sub>")
                  + p("Em seguida, o HCℓ gerado passa por um filtro onde é absorvido pelo hidróxido de cálcio, formando o cloreto de cálcio, X (reação 2).")
                  + apoio("Reação 2 &nbsp; 2 HCℓ + Ca(OH)<sub>2</sub> → 2 H<sub>2</sub>O + X")
                  + p("O nome do composto orgânico formado na reação 1 e a fórmula do composto X produzido na reação 2 são, respectivamente,"),
     "trocar": [("HCl", "HCℓ")],
     "alternativas": colunas(["Reação 1", "Reação 2"], [["etino", "CaCℓ<sub>2</sub>"], ["etino", "CℓCa"], ["eteno", "Cℓ<sub>2</sub>Ca"], ["eteno", "CaCℓ"], ["eteno", "CaCℓ<sub>2</sub>"]]),
     "explicacao": "<p>C₂H₄ tem uma dupla ligação entre os carbonos (CH₂=CH₂): é o <strong>eteno</strong>. O cálcio forma Ca²⁺ e o cloro, Cℓ⁻; o sal neutro tem dois cloretos para cada cálcio, com o cátion escrito primeiro: <strong>CaCℓ₂</strong>. Alternativa <strong>E</strong>.</p><p>Etino é C₂H₂, com tripla ligação (A e B). Cℓ₂Ca e CℓCa invertem a ordem (B e C). E CaCℓ não neutraliza as cargas (D).</p>"},
36: {"materia": "Biologia", "assunto": "Ecologia", "tags": ["poluição por plásticos"],
     "enunciado": PLASTICO + P36,
     "alternativas": alts("As “grandes ilhas de lixo” constituem-se como a forma adequada para a coleta, reciclagem e tratamento do lixo plástico dos oceanos.",
                          "A poluição causada pelo lançamento de resíduos plásticos nos oceanos pode causar o fenômeno conhecido como maré vermelha, devido ao aumento dos decompositores nas teias alimentares.",
                          "As áreas oceânicas conhecidas como “ilhas de lixo” são regiões de intensa degradação dos resíduos plásticos, devido à grande quantidade de bactérias decompositoras anaeróbicas e à falta do gás oxigênio.",
                          "As pesquisas demonstram que os resíduos plásticos lançados aos oceanos, ao sofrerem a ação das correntes marinhas, das variações de salinidade, de pressão, de temperatura e de atrito, em um intervalo de tempo médio, não prejudicam mais os ecossistemas.",
                          "Em meio marinho, os plásticos apresentam inúmeras ameaças ecológicas, como a inibição da capacidade reprodutiva dos animais, o bloqueio do trato digestório daqueles que ingerem esses plásticos e a transferência de poluentes para a cadeia alimentar."),
     "explicacao": "<p>O texto diz que os fragmentos de plástico, confundidos com alimento, bloqueiam as vias respiratórias e o estômago dos animais e podem interferir na reprodução; ao ser ingeridos, levam poluentes para a cadeia alimentar. Alternativa <strong>E</strong>.</p><p>As ilhas de lixo são um problema, não uma solução (A). A maré vermelha é causada pela proliferação de algas, não por plásticos (B). O plástico tem “baixo potencial de degradação” (C). E os fragmentos continuam prejudicando os ecossistemas (D).</p>"},
37: {"materia": "Biologia", "assunto": "Ecologia", "tags": ["biodegradação"],
     "enunciado": p("Sobre a degradação do material descrito no texto, é correto afirmar que"), "apoio_de": (36, P36),
     "alternativas": alts("ela independe de fatores ambientais, tais como: umidade, temperatura, disponibilidade de oxigênio e luminosidade.", "ela ocorre intensamente nas “grandes ilhas de lixo” encontradas nos oceanos, devido à falta de matéria orgânica desses locais.",
                          "as bactérias e os fungos decompositores possuem enzimas específicas para transformar rapidamente a matéria mineral em orgânica.", "os materiais resistentes à biodegradação, quando descartados incorretamente, representam um grande desafio da gestão ambiental contemporânea.",
                          "os resíduos de plásticos após se fragmentarem nos oceanos são benéficos nos processos respiratórios e reprodutivos de muitos animais marinhos, pois são facilmente digeridos."),
     "explicacao": "<p>Plásticos resistem à biodegradação e permanecem no ambiente por muito tempo. Descartados de forma errada, acumulam-se nos mares: é um grande desafio da gestão ambiental atual. Alternativa <strong>D</strong>.</p><p>O próprio texto cita fatores do meio (sol, temperatura, oxigênio) que atuam no plástico (A). A degradação é lenta, não intensa (B). Os decompositores transformam matéria orgânica em mineral, não o contrário (C). E os fragmentos prejudicam os animais (E).</p>"},
38: {"materia": "Matemática", "assunto": "Porcentagem",
     "enunciado": apoio("Em 2020 no Brasil, 97 % das pessoas com idade entre 7 e 14 anos estavam matriculadas na escola. O restante, correspondente a 1,5 milhão de pessoas com essa idade escolar, estava fora da sala de aula.")
                  + url("https://tinyurl.com/tfs6qgm", "22.04.2022") + p("Segundo os dados apresentados, em 2020, o número de pessoas com idade entre 7 e 14 anos que estavam matriculadas na escola, em milhões, era"),
     "alternativas": alts("48,5.", "45,3.", "43,5.", "42,7.", "40,5."),
     "explicacao": "<p>Os 3% fora da escola correspondem a 1,5 milhão, então o total é 1,5 ÷ 0,03 = 50 milhões. Os matriculados são 50 − 1,5 = <strong>48,5 milhões</strong>. Alternativa <strong>A</strong>.</p><p>Os outros valores vêm de calcular o total de forma errada.</p>"},
39: {"materia": "Física", "assunto": "Eletricidade", "tags": ["carga elétrica"],
     "enunciado": p(*T(16, "Com o intuito de diminuir significativamente", "unidade de medida “A·h”.", ["Apesar da criação das baterias"]), "É correto afirmar que essa unidade de medida se refere à grandeza física"),
     "trocar": [("“A·h”", "“<strong>A·h</strong>”")],
     "alternativas": alts("carga elétrica.", "corrente elétrica.", "potencial elétrico.", "resistência elétrica.", "capacitância elétrica."),
     "explicacao": "<p>Como i = Q ÷ ∆t, a carga é Q = i · ∆t: corrente (A) vezes tempo (h). O ampère-hora é uma unidade de <strong>carga elétrica</strong> (1 A·h = 3 600 C). Alternativa <strong>A</strong>.</p><p>A corrente se mede em A (B), o potencial em V (C), a resistência em Ω (D) e a capacitância em F (E).</p>"},
40: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": MULTI + ["quadrinhos"],
     "enunciado": p("Considere os quadrinhos.") + "[[fig:1]]" + url("https://tinyurl.com/msnbaaea", "23.04.2022", "Original colorido.")
                  + p("Os principais personagens dos quadrinhos rejeitam o uso de canudinhos porque"),
     "imagens": figs(("q40", "Tirinha “Cientirinhas #114”, de Merlin, em inglês, em quatro quadros. 1: um casal segura copos de bebida. 2: alguém pergunta ao homem: “Why didn't you get a straw?” (por que você não pegou um canudo?). 3: a mulher responde: “Why should I? Aren't you aware that plastic straws may end up in the oceans?” (por que deveria? Você não sabe que canudos de plástico podem acabar nos oceanos?). 4: o casal vai embora num grande carro esportivo a gasolina, que solta fumaça, e diz: “True. What would become of the planet if it weren't for concerned citizens like us?” (verdade. O que seria do planeta se não fossem cidadãos conscientes como nós?).")),
     "alternativas": alts("se preocupam com o alto consumo de combustíveis renováveis.", "se preocupam que seu descarte final possa gerar um impacto ambiental.", "se entediam com essa discussão sobre produtos descartáveis.",
                          "são ambientalistas a favor do uso de produtos descartáveis.", "são consumistas que não se preocupam com a vida marinha."),
     "explicacao": "<p>A mulher diz que não usou canudo porque os canudos de plástico “podem acabar nos oceanos”: a preocupação é com o <strong>descarte</strong> e o impacto ambiental. Alternativa <strong>B</strong>.</p><p>Eles não falam de combustíveis renováveis (A). Não demonstram tédio (C). Rejeitam o descartável, não o defendem (D). E dizem se preocupar com a vida marinha, ainda que sejam incoerentes ao usar um carro poluidor (E).</p>"},
41: {"materia": "Química", "assunto": "Reações químicas", "tags": ["biodigestor", "fermentação anaeróbica"],
     "enunciado": BIOGAS + P41,
     "alternativas": alts("MO + energia → CH<sub>4</sub> + H<sub>2</sub> + H<sub>2</sub>S + CO<sub>2</sub> + NH<sub>3</sub> + N<sub>2</sub> + H<sub>2</sub>O",
                          "MO + O<sub>2</sub> + energia → CH<sub>4</sub> + H<sub>2</sub> + H<sub>2</sub>S + CO<sub>2</sub> + NH<sub>3</sub> + N<sub>2</sub> + H<sub>2</sub>O",
                          "MO → CH<sub>4</sub> + H<sub>2</sub> + H<sub>2</sub>S + CO<sub>2</sub> + NH<sub>3</sub> + N<sub>2</sub> + H<sub>2</sub>O + energia",
                          "MO + O<sub>2</sub> → CH<sub>4</sub> + H<sub>2</sub> + H<sub>2</sub>S + CO<sub>2</sub> + NH<sub>3</sub> + N<sub>2</sub> + H<sub>2</sub>O + energia",
                          "MO + energia → CH<sub>4</sub> + H<sub>2</sub> + H<sub>2</sub>S + CO<sub>2</sub> + NH<sub>3</sub> + N<sub>2</sub> + H<sub>2</sub>O + O<sub>2</sub>"),
     "explicacao": "<p>A fermentação ocorre “sem a presença de oxigênio” (não há O₂ entre os reagentes) e “com liberação de energia” (a energia aparece entre os produtos). Alternativa <strong>C</strong>.</p><p>A e E põem a energia como reagente, ou seja, absorvida. B e D incluem O₂ nos reagentes. E E ainda libera O₂, que não está na lista de gases.</p>"},
42: {"materia": "Química", "assunto": "Cinética química", "tags": ["fatores que alteram a velocidade"],
     "enunciado": p(*T(17, "Um grupo de alunos construiu um biodigestor", "no biodigestor foi a", ["No entanto, após uma semana", "Com base na adaptação"])),
     "apoio_de": (41, P41),
     "alternativas": alts("luz.", "umidade.", "temperatura.", "forma do recipiente.", "área da superfície do gerador."),
     "explicacao": "<p>O saco preto absorve a radiação solar e aquece o biodigestor. Com a <strong>temperatura</strong> maior, os microrganismos trabalham mais rápido e as reações se aceleram. Alternativa <strong>C</strong>.</p><p>O saco preto bloqueia a luz em vez de deixá-la entrar, e a luz não é o que acelera a fermentação (A). A umidade, a forma do recipiente e a área do gerador não mudaram (B, D e E).</p>"},
43: {"materia": "História", "assunto": "Revolução Industrial",
     "enunciado": p(*T(17, "Internet, telefone celular e computador pessoal", "marcada pela invenção", ["Entretanto, a parceria"])),
     "alternativas": alts("do satélite e da bússola.", "do gramofone e da luneta.", "do rádio e do sistema GPS.", "do automóvel e do telefone.", "do tear manual e da imprensa."),
     "explicacao": "<p>A Segunda Revolução Industrial, na segunda metade do século XIX, trouxe a eletricidade, o petróleo, o aço, o motor a combustão, o <strong>automóvel</strong> e o <strong>telefone</strong>. Alternativa <strong>D</strong>.</p><p>Satélite e GPS são do século XX (A e C). A bússola, a luneta, o tear manual e a imprensa são muito anteriores (A, B e E).</p>"},
44: {"materia": "Português", "assunto": "Interpretação de texto", "tags": MULTI + ["humor", "quadrinhos"],
     "enunciado": p("Leia os quadrinhos.") + "[[fig:1]]" + url("https://tinyurl.com/tbgmcf5", "23.04.2022", "Original colorido.")
                  + p("Os quadrinhos apresentados abordam uma temática relevante para a sociedade utilizando linguagem coloquial.",
                      "Analisando-se as informações verbais e não verbais utilizadas na construção da tirinha, afirma-se corretamente que o humor decorre"),
     "imagens": figs(("q44", "A mesma tirinha “Cientirinhas #114”, de Merlin, em português. 1: um casal segura copos de bebida. 2: alguém pergunta: “Ué? Você não pegou canudinho?”. 3: a mulher responde: “De jeito nenhum! Você não sabia que canudos de plástico podem acabar nos oceanos?”. 4: o casal sai num grande carro esportivo, que solta fumaça, dizendo: “Verdade. O que seria do planeta se não fossem por cidadãos conscientes como nós?”.")),
     "alternativas": alts("do contraste entre as ações politicamente corretas realizadas pelas personagens e suas falas preconceituosas.",
                          "da coerência entre o posicionamento das personagens, que acreditam na inutilidade de ações ambientalmente corretas.",
                          "da representação de ações consideradas fisicamente saudáveis realizadas no discurso das personagens, mas não postas em prática.",
                          "da oposição existente entre as falas das personagens, que compreendem de formas diferentes o conceito de consumo sustentável.",
                          "da incoerência existente entre o discurso de proteção ambiental das personagens e a concretização das ações representadas nos quadrinhos."),
     "explicacao": "<p>O casal se diz consciente por recusar o canudo de plástico, mas sai num carro grande e poluente. O humor está na <strong>incoerência</strong> entre o discurso ambiental e a ação. Alternativa <strong>E</strong>.</p><p>As falas não são preconceituosas (A). Eles defendem ações ambientais, não as acham inúteis (B). O tema não é a saúde física (C). E as personagens concordam entre si (D).</p>"},
45: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": ["gráfico"],
     "enunciado": p("Leia as informações publicadas em 23.10.2019 no site da World Economic Forum.")
                  + apoio(" ".join(T(18, "In terms of wealth per adult, the biggest winners", "prices (–6 %).")))
                  + p("<strong>Change in wealth per adult 2018-19, biggest gains and losses</strong>") + "[[fig:1]]"
                  + fonte("USD: American Dollar. Fonte dos dados: &lt;https://tinyurl.com/rloougx&gt; Acesso em: 20.04.2022.")
                  + p("Considerando as informações dadas sobre as riquezas de indivíduos entre 2018 e 2019, é correto afirmar que"),
     "imagens": figs(("q45", "Gráfico de barras horizontais “Figure 2: Change in wealth per adult 2018-19, biggest gains and losses”, em dólares. Ganhos, do maior para o menor: Switzerland (Suíça), cerca de 17 800; United States, cerca de 11 000; Japan e Netherlands, cerca de 8 000 cada; New Zealand, cerca de 8 000; Singapore, cerca de 6 000; Israel, Canada e Spain, cerca de 4 000 a 5 000. Perdas: Belgium, Turkey e Norway, entre 2 000 e 4 000; Australia, cerca de 28 700.")),
     "alternativas": alts("124 000 australianos se tornaram milionários no período pré-pandemia.", "a Suíça foi o único país que apresentou queda nos preços das residências.", "Suécia e Estados Unidos da América são os países com melhores rendimentos <em>per capita</em>.",
                          "nos dois países da Oceania mencionados no gráfico, os cidadãos perderam renda.", "Japão e Países Baixos apresentam dados de ganhos semelhantes."),
     "explicacao": "<p>No gráfico, as barras do Japão e dos Países Baixos (<em>Netherlands</em>) têm praticamente o mesmo tamanho. Alternativa <strong>E</strong>.</p><p>A Austrália perdeu 124 mil milionários (A), e foi ela, não a Suíça, que teve queda no preço das casas (B). O país do topo é a Suíça (<em>Switzerland</em>), não a Suécia (C). E a Nova Zelândia, o outro país da Oceania, teve ganho (D).</p>"},
46: {"materia": "Raciocínio lógico", "assunto": "Lógica", "tags": ["divisores e múltiplos"],
     "enunciado": p(*T(19, "Aurora é uma garota de 10 anos", "Foram dadas as seguintes pistas:", ["Dentro de uma caixa trancada"]),
                    "• o segredo do cadeado é composto por 3 algarismos indo-arábicos distintos em ordem decrescente;<br>• algarismos divisores de 5 não fazem parte deste segredo;<br>• algarismos múltiplos de 3 não fazem parte deste segredo; e<br>• o maior algarismo do segredo é ímpar.",
                    "Com essas afirmações, Aurora foi a mais rápida e ganhou os bombons ao descobrir que o segredo é") + "[[fig:1]]",
     "imagens": figs(("q46", "Ilustração de um cadeado com segredo de três rodas numeradas.")),
     "alternativas": alts("1 2 4", "1 4 2", "5 4 2", "7 4 0", "7 4 2"),
     "explicacao": "<p>Os divisores de 5 são 1 e 5; os múltiplos de 3 entre os algarismos são 0, 3, 6 e 9. Sobram 2, 4, 7 e 8. O maior algarismo é ímpar, então é 7, e os outros dois, menores que 7, são 4 e 2. Em ordem decrescente: <strong>742</strong>. Alternativa <strong>E</strong>.</p><p>A, B e C usam 1 ou 5, e A e B não estão em ordem decrescente. D usa o 0, múltiplo de 3.</p>"},
47: {"materia": "Matemática", "assunto": "Sequências", "tags": ["progressão geométrica"],
     "enunciado": p(*T(19, "Uma pessoa, com 95 kg de massa", "aproximará cada vez mais de", ["No primeiro trimestre", "Assim sendo, mantendo"]))
                  + apoio("Lembre-se de que:<br>Soma S dos infinitos termos de uma Progressão Geométrica:<br>\\(S = \\dfrac{a_1}{1 - q}\\), −1 &lt; q &lt; 1, em que <strong>a<sub>1</sub></strong> é o termo inicial e <strong>q</strong> é a razão da sequência"),
     "alternativas": alts("55 kg.", "60 kg.", "62 kg.", "67 kg.", "70 kg."),
     "explicacao": "<p>As reduções formam uma PG infinita: 14 + 7 + 3,5 + ..., com a₁ = 14 e q = 1/2. A soma é 14 ÷ (1 − 1/2) = 28 kg. A massa se aproxima de 95 − 28 = <strong>67 kg</strong>. Alternativa <strong>D</strong>.</p><p>70 kg seria tirar só 25 kg, e os outros valores não saem da soma da PG.</p>"},
48: {"materia": "Física", "assunto": "Física moderna", "tags": ["radioatividade"],
     "enunciado": p(it(" ".join(T(19, "Apesar da 1ª pessoa a ganhar dois prêmios", "de Química, em 1935.")), "Radioatividade"),
                    "De uma maneira sintética, podemos definir o fenômeno científico citado no texto como a ação de"),
     "alternativas": alts("núcleos instáveis os quais emitem partículas e radiação eletromagnética.", "prótons instáveis os quais emitem subpartículas e radiação eletromagnética.", "elétrons instáveis os quais emitem subpartículas e radiação eletromagnética.",
                          "pósitrons instáveis os quais emitem partículas e não radiação eletromagnética.", "nêutrons instáveis os quais emitem subpartículas e não radiação eletromagnética."),
     "explicacao": "<p>Radioatividade é a emissão espontânea feita por <strong>núcleos atômicos instáveis</strong>, que liberam partículas (alfa, beta) e radiação eletromagnética (gama) até se estabilizarem. Alternativa <strong>A</strong>.</p><p>O fenômeno é do núcleo como um todo, não de prótons, elétrons, pósitrons ou nêutrons isolados (B, C, D e E). E a radiação gama é eletromagnética (D e E).</p>"},
49: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": ["resenha"],
     "enunciado": RADIO + P49,
     "alternativas": alts("sua diretora comete erros científicos e força uma temática feminista.", "apresenta uma produção enfadonha, apesar do tema fascinante.", "sua diretora apela para um drama moralista e ultrapassado.",
                          "valoriza a participação das mulheres nas ciências.", "incentiva a paridade de gêneros nos laboratórios."),
     "explicacao": "<p>A resenha diz que a diretora fez um drama “<em>stuffy</em>” (chato) que presta um desserviço a um tema “<em>undeniably fascinating</em>” (inegavelmente fascinante). Alternativa <strong>B</strong>.</p><p>A crítica não aponta erros científicos (A) nem chama o drama de ultrapassado (C). E valorizar as mulheres na ciência e incentivar a paridade não são motivos da crítica negativa (D e E).</p>"},
50: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": ["resenha"],
     "enunciado": p("A resenha aponta para o crescente número de"), "apoio_de": (49, P49),
     "alternativas": alts("filmes que são patrocinados por corporações comerciais.", "mulheres na direção de filmes na indústria cinematográfica.", "produções sobre mulheres que se destacam nas áreas científicas.",
                          "erros nas representações de conceitos científicos.", "filmes com teor moralista e patronal."),
     "explicacao": "<p>A resenha fala de “<em>an increasing number of releases</em>” com “<em>girls and women exploring science and technology</em>”: um número crescente de filmes sobre mulheres nas ciências. Alternativa <strong>C</strong>.</p><p>O texto não fala de patrocínio (A), de diretoras (B) nem de erros científicos (D). E o tom moralista é uma crítica a esses filmes, não aquilo que cresce (E).</p>"},
51: {"materia": "Física", "assunto": "Eletricidade", "tags": MULTI + ["transmissão de dados"],
     "enunciado": p("Leia as manchetes apresentadas, veiculadas em janeiro de 2020.")
                  + apoio("Aplicativo de relacionamento usa inteligência artificial como arma contra o abuso")
                  + url("https://tinyurl.com/qufhtur", "05.04.2022")
                  + apoio("Inteligência artificial emitiu aviso sobre coronavírus em dezembro") + url("https://tinyurl.com/uoj2s7w", "05.04.2022")
                  + apoio("A inteligência artificial invade o mundo da arte") + url("https://tinyurl.com/vqyk5qy", "05.04.2022")
                  + p(*[it(x, "binary digits") for x in T(20, "Metas propostas pela Agenda 2030 da ONU", "transmissão de dados são", ["A IA tem sido uma aliada", "Podemos afirmar que os campos"])]),
     "alternativas": alts("Termologia e Termodinâmica, pois o tráfego dos bits depende de quanto eles conseguem alterar as condições térmicas do meio.",
                          "Cinemática e Dinâmica, devido à quantidade e à velocidade dos bits a serem processados durante o tráfego de informação.",
                          "Eletricidade e Eletromagnetismo, já que os bits podem ser transmitidos usando correntes elétricas ou ondas eletromagnéticas.",
                          "Gravitação Universal e Astrologia, porque as transmissões de bits estão diretamente ligadas ao alinhamento universal de estrelas e planetas.",
                          "Quântica e Nuclear, uma vez que a coleta e o armazenamento de informações são possíveis mediante a alteração de partículas subatômicas."),
     "explicacao": "<p>Os bits trafegam como pulsos de corrente elétrica nos cabos ou como ondas eletromagnéticas (rádio, wi-fi, luz nas fibras ópticas): campos da <strong>Eletricidade e do Eletromagnetismo</strong>. Alternativa <strong>C</strong>.</p><p>A transmissão não depende de alterar a temperatura (A), nem da cinemática de corpos (B). Astrologia não é ciência (D). E a física nuclear não está na transmissão de dados (E).</p>"},
52: {"materia": "História", "assunto": "História contemporânea", "tags": ["Revolução Francesa", "direitos das mulheres"],
     "explicacao": "<p>A Revolução Francesa aprovou o divórcio (1792) e outros direitos civis para as mulheres, mas não lhes deu cidadania política: elas não votavam e, em 1793, os clubes femininos foram proibidos. Alternativa <strong>E</strong>.</p><p>As mulheres não ganharam mais direitos que os demais grupos (A), a Declaração dos Direitos da Mulher, de Olympe de Gouges, não foi adotada e não pregava superioridade (B), o 8 de março é do século XX (C), e não houve abolição do trabalho doméstico (D).</p>"},
53: {"materia": "Português", "assunto": "Interpretação de texto", "tags": ["discurso"],
     "enunciado": MALALA + P53,
     "alternativas": alts("relatar o cotidiano de jovens mulheres que lutam pela igualdade de gênero em Nova Iorque.", "convencer os homens a abdicarem do direito das mulheres à independência e à educação.",
                          "denunciar a violência de professores contrários aos extremistas que lutam pela igualdade de gênero.", "mobilizar a sociedade, principalmente as mulheres, a lutar pelo direito à educação e ao conhecimento.",
                          "enaltecer os esforços desempenhados por grandes lideranças mundiais a favor da universalização da saúde."),
     "explicacao": "<p>Malala convoca o público (“Deixem-nos travar uma luta gloriosa”, “Deixem-nos pegar nossos livros e canetas”) e pede às mulheres que lutem por si mesmas pelo direito à educação. É um texto de <strong>mobilização</strong>. Alternativa <strong>D</strong>.</p><p>O discurso não relata cotidianos (A), não pede que os homens abram mão de nada (B), não denuncia professores, e são os extremistas que temem a educação (C), e o tema é a educação, não a saúde (E).</p>"},
54: {"materia": "Português", "assunto": "Funções da linguagem", "tags": ["vocativo"],
     "enunciado": p("Ocorre, no texto, a repetição da expressão “queridos irmãos e irmãs”.", "O frequente uso dessa expressão, além de identificar os seus interlocutores, expressa"), "apoio_de": (53, P53),
     "alternativas": alts("respeito, pois o contexto formal de comunicação impõe o uso do tratamento coloquial utilizado.", "afetividade, uma vez que qualquer contexto comunicativo impõe o uso formal de pronomes de tratamento.",
                          "ironia da enunciadora, que, mesmo diante da formalidade do contexto, opta pelo tratamento informal e cômico.", "proximidade, pois, embora o contexto seja formal, ela utiliza um tratamento afetivo para sugerir familiaridade.",
                          "desenvoltura da enunciadora, que, mesmo reconhecendo a formalidade do discurso, opta por se distanciar do público alvo."),
     "explicacao": "<p>Numa assembleia da ONU, um contexto formal, Malala chama o público de “queridos irmãos e irmãs”: um tratamento afetivo, que cria <strong>proximidade</strong> e sugere uma família unida pela mesma causa. Alternativa <strong>D</strong>.</p><p>Um contexto formal não impõe tratamento coloquial (A), nem todo contexto exige pronomes formais (B), não há ironia nem comicidade (C), e a expressão aproxima, em vez de distanciar (E).</p>"},
}
completar(Q, R)
