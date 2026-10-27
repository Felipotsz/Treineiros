# Ajustes da conferência humana: Vestibular FATEC 1º semestre de 2023 (exame de 08/01/2023)
# Texto conferido com a imagem de cada página. Tema implícito: Tecnologia (a redação pede a preparação para o mercado de trabalho na 4ª Revolução Industrial).
# 54 questões; a prova tem 5 h no total, incluindo a redação (que fica fora do simulado).
# Matéria: a do gabarito oficial; nas "Multidisciplinar", a matéria principal + tag "multidisciplinar".
# Rascunho com colunas embaralhadas: todos os enunciados e alternativas foram escritos aqui.
# Gabarito: oficial (1SEM23), sem anuladas.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import A, carregar, enun, tabela, colunas, completar, trecho

ID = "fatec-2023-1sem"
META = {
    "id": ID,
    "banca": "FATEC",
    "ano": 2023,
    "semestre": 1,
    "titulo": "Vestibular FATEC, 1º semestre de 2023",
    "fonte": "Centro Paula Souza",
    "dataExame": "2023-01-08",
    "duracaoMinutos": 300,
    "tema": "Tecnologia",
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


def alts(*textos):
    return dict(zip("ABCDE", textos))


def troca(html, pares):
    for a, b in pares:
        assert a in html, a
        html = html.replace(a, b, 1)
    return html


# ---------- textos compartilhados ----------
MILTON = (chamada("Leia o excerto de Milton Santos para responder às questões 12 e 13.")
          + apoio(*T(7, "Após a Segunda Guerra Mundial, tem início", "meio técnico-científico-informacional.", ["Nesse período, os objetos"]))
          + fonte("SANTOS, Milton. <em>A Natureza do Espaço: Técnica e Tempo, Razão e Emoção.</em> São Paulo, SP. EDUSP, 2002. Adaptado.")
          + fonte("*Égide (s.f.): escudo; por derivação, o que protege, ampara."))
MILTON = troca(MILTON, [("A união entre a técnica e a ciência vai dar-se sob a égide* do mercado que, graças à ciência e à técnica, torna-se um mercado global.",
                         "<strong>A união entre a técnica e a ciência vai dar-se sob a égide* do mercado que, graças à ciência e à técnica, torna-se um mercado global.</strong>"),
                        ("meio técnico-científico-informacional.", "<em>meio técnico-científico-informacional</em>.")])
P12 = p("Parafrasear é reescrever um texto utilizando uma linguagem diferente, mas mantendo seu sentido original.", "Assinale a alternativa que apresenta a paráfrase correta da passagem destacada no texto.")

POLIO = (chamada("Leia os textos para responder às questões 15 e 16.")
         + apoio("<strong>Texto 1</strong>", *T(8, "No Brasil, as atividades de imunização", "Americana da Saúde (Opas/OMS).", ["Em 1980 foi estabelecida", "A doença é considerada"]))
         + url("https://tinyurl.com/ydw3v8z7", "28.10.2022")
         + apoio("<strong>Texto 2</strong>", *T(8, "Dados oficiais da Campanha Nacional", "lista de alto risco para a doença.", ["Em 2020, o relatório"]))
         + url("https://tinyurl.com/mr39nu8u", "28.10.2022"))
P15 = p("Segundo os textos, é correto afirmar que,")

PLATAO = (chamada("Leia o texto para responder às questões 20 e 21.")
          + apoio(*T(10, "Platão (428 a.C. – 347 a.C.), filósofo", "como um poliedro convexo no qual"),
                  "• todas as faces são formadas por polígonos regulares e congruentes entre si;<br>• o mesmo número de arestas encontra-se em todos os vértices; e<br>• os ângulos poliédricos são congruentes entre si.",
                  *T(10, "Muitos séculos depois, os químicos", "estão mostradas na imagem."))
          + "[[fig:1]]")
PLATAO_IMG = figs(("q20", "Cinco geometrias moleculares, cada uma com o desenho geométrico correspondente acima. Linear: um segmento de reta; modelo com três átomos alinhados, ângulo de 180°. Trigonal plana: um triângulo; átomo central ligado a três átomos no mesmo plano, ângulos de 120°. Tetraédrica: uma pirâmide de base triangular, de 4 faces triangulares iguais; átomo central ligado a quatro átomos, ângulos de 109,5°. Bipiramidal trigonal: duas pirâmides triangulares unidas pela base; átomo central ligado a cinco átomos, ângulos de 90° e 120°. Octaédrica: duas pirâmides de base quadrada unidas pela base, 8 faces triangulares; átomo central ligado a seis átomos, ângulos de 90°."))
P20 = p("Assinale a alternativa que apresenta geometrias moleculares que coincidem com os poliedros de Platão.")

TECHJOB = (chamada("Leia o texto para responder às questões 24 e 25.")
           + apoio("<strong>Tech job market is up this year</strong>",
                   "Despite high-profile threats of layoffs and a dip in job postings in June, the tech market remains strong, especially for data-related skills.",
                   "By Paul Krill<br>Editor at Large, InfoWorld | AUG 24, 2022 3:00 AM PDT",
                   *T(12, "Demand for tech talent continues to grow", "to lead in tech job postings.", ["Those with skills to build", "Of the top 50 employers", "Technologists’ preference", "Traditional tech hubs"]))
           + url("https://tinyurl.com/nhbdyasv", "27.10.2022"))
P24 = p("Segundo o texto, o mercado de trabalho na área tecnológica")

CIBER = (chamada("Leia o texto para responder às questões 28 e 29.")
         + apoio(*T(13, "O ciberespaço, impulsionado pela rede", "a Geografia deve buscar compreender."))
         + url("https://tinyurl.com/239pf2nj", "05.11.2022"))
P28 = p("Analisando o contexto da passagem “sendo o ciberespaço parte integrante da sociedade contemporânea”, percebe-se que há, com a oração seguinte, uma relação de")

NFC = (chamada("Leia o texto para responder às questões 32 e 33.")
       + apoio(it(" ".join(T(14, "Uma tecnologia cada vez mais utilizada", "de aproximadamente 0,1 ns.")), "Near Field Communication"))
       + apoio("Considere as seguintes informações:<br><em>M (mega) = 10<sup>6</sup></em><br><em>c (centi) = 10<sup>–2</sup></em><br><em>n (nano) = 10<sup>–9</sup></em><br>v = λ · f<br>\\(v = \\dfrac{\\Delta S}{\\Delta t}\\)"))
NFC = troca(NFC, [("3,0 × 108 m/s", "3,0 × 10<sup>8</sup> m/s")])
P32 = p("Assinale a alternativa que apresenta corretamente, em cm, a distância máxima de operação dessa tecnologia.")

CHERRY = (chamada("Leia o texto para responder às questões 44 e 45.")
          + apoio("<strong>Cherry picking in the media</strong>",
                  *(lambda ps: ps[:-1] + [ps[-1] + " say the following:"])(T(19, "Cherry picking is often used by the media", "engages in cherry picking might", ["For example, consider a situation"])),
                  "<strong>“</strong>A recent study found that there are plenty of scientists who disagree with the consensus position on this phenomenon.”",
                  *T(19, "This statement represents an example of", "majority of scientists support this position."))
          + url("https://tinyurl.com/yjem2sm2", "28.10.2022"))
P44 = p("O fenômeno descrito no texto indica a prática de")

MAGICO = p(*T(20, "Umas das profissões que usa bastante tecnologia", "consegue levantá-la."))

QUERINO = (chamada("Leia o texto para responder às questões 53 e 54.")
           + apoio(*T(22, "Os povos africanos que foram trazidos pro Brasil", "não se sabe nem o nome.", ["No ciclo do ouro", "Tem um alemão"]))
           + fonte("<em>Projeto Querino</em>, Transcrição do episódio 05: Os Piores Patrões.")
           + url("https://tinyurl.com/yacpau7w", "28.10.2022"))
P53 = p("Segundo o texto, é correto afirmar que")

Q = {
1: {"materia": "Português", "assunto": "Gêneros textuais", "tags": MULTI + ["charge"],
    "enunciado": p("Leia a charge.") + "[[fig:1]]" + url("https://tinyurl.com/ms4ycbkz", "28.10.2022", "Original colorido.")
                 + p("Ao analisar a linguagem verbal e não verbal da charge apresentada, pode-se concluir corretamente que"),
    "imagens": figs(("q01", "Charge de Mike Keefe, “The evolution of communication” (a evolução da comunicação). Sobre o alto de um globo, uma fila de personagens, da esquerda para a direita, cada um com uma placa: “First written word” (primeira palavra escrita), um homem das cavernas gravando numa pedra; “Movable type” (tipos móveis), um homem numa prensa; “Mass publication” (publicação em massa), um homem de terno lendo um livro; “Email”, um rapaz digitando num notebook; “Twitter”, um rapaz curvado sobre o celular, descendo o outro lado do globo, que diz: “140 characters. What more is there to say?” (140 caracteres. O que mais há para dizer?), enquanto se ouve “Tweet tweet”.")),
    "alternativas": alts("demonstra a revolução da habilidade humana de estabelecer unicamente conexões interpessoais a partir da invenção do livro.",
                         "institui a prensa móvel como o ápice do desenvolvimento das técnicas de produção cultural da humanidade.",
                         "atribui à linguagem escrita primitividade uma vez que está atrelada unicamente ao homem das cavernas.",
                         "ironiza o aparente retrocesso da capacidade comunicativa do ser humano em oposição à evolução tecnológica.",
                         "relaciona a publicação e a divulgação de livros de autoajuda ao início do desenvolvimento pessoal e financeiro do indivíduo."),
    "explicacao": "<p>A fila sobe da primeira palavra escrita até a publicação em massa e depois desce, com o usuário do Twitter curvado como o homem das cavernas, achando que 140 caracteres bastam. A charge <strong>ironiza</strong> a ideia de que a tecnologia avança enquanto a capacidade de se comunicar regride. Alternativa <strong>D</strong>.</p><p>O livro não é apresentado como única forma de conexão (A), e o ápice da curva é a publicação em massa, não a prensa (B). A charge não diz que a escrita é primitiva (C) nem fala de autoajuda (E).</p>"},
2: {"materia": "História", "assunto": "Pré-História", "tags": ["tecnologia"],
    "enunciado": apoio(*T(2, "A palavra tecnologia se refere", "sobrevivência dos homens na Terra."))
                 + url("https://tinyurl.com/55cmrw79", "28.10.2022") + p("Entre as tecnologias desenvolvidas no período citado no texto, destaca-se"),
    "alternativas": alts("a criação de máquinas simples movidas a energias renováveis, como eólica e solar, para produção de armas e utensílios domésticos.",
                         "a utilização de tecidos finos para a confecção de bolas utilizadas na prática de esportes de guerra, disputados por grupos nômades rivais.",
                         "a invenção da escrita e dos rudimentos de um sistema de remessa postal que atuava como uma forma de estabelecer comunicação à distância.",
                         "a produção de tecidos de seda, cultivado em grandes lavouras às margens dos rios Tigre e Eufrates, na região conhecida como Crescente Fértil.",
                         "a atividade de lascar pedras umas nas outras a fim de produzir ferramentas pontiagudas e cortantes, utilizadas para a caça e para o manuseio de alimentos."),
    "explicacao": "<p>No Paleolítico (Idade da Pedra Lascada), os seres humanos lascavam pedras para fazer ferramentas cortantes e pontiagudas, usadas na caça e no preparo dos alimentos. Alternativa <strong>E</strong>.</p><p>Máquinas movidas a energia eólica ou solar para fabricar armas não existiam (A), nem tecidos finos para bolas (B). A escrita marca justamente o fim da Pré-História (C). E a seda é chinesa, produzida bem depois, e não vem de lavouras na Mesopotâmia (D).</p>"},
3: {"materia": "Geografia", "assunto": "Globalização",
    "enunciado": apoio(*T(3, "A globalização é caracterizada pelo intenso", "geográfico cada vez mais.", ["Apesar de o termo globalização"]))
                 + url("https://tinyurl.com/yechfdaw", "13.10.2022") + p("De acordo com o texto, é correto afirmar que"),
    "alternativas": alts("a globalização foi criada no século XXI como uma tentativa para diminuir o consumismo presente nas sociedades modernas.",
                         "o avanço da tecnologia, aplicada em diversos ramos da economia, faz o processo de globalização se intensificar.",
                         "o termo globalização começou a ser utilizado ainda no feudalismo, período de grandes avanços técnicos e científicos.",
                         "o processo de globalização teve início no final do século XX e foi resultante da constante involução dos processos técnicos.",
                         "a evolução que ocorreu nos meios de comunicação e de transporte contribuiu para a retração do processo de globalização."),
    "explicacao": "<p>O texto diz que o avanço tecnológico nos meios de comunicação e de transporte “ampliaram a inter-relação” entre os lugares e que o desenvolvimento das técnicas integrou o espaço “cada vez mais”: a tecnologia <strong>intensifica</strong> a globalização. Alternativa <strong>B</strong>.</p><p>O termo é do fim do século XX, e o processo começa nas Grandes Navegações (A, C e D). O texto fala de evolução das técnicas, não de involução (D), e de ampliação, não de retração (E).</p>"},
4: {"materia": "Raciocínio lógico", "assunto": "Lógica", "tags": ["diagramas de Venn", "conjuntos"],
    "enunciado": p("Peter Drucker, pai da Administração moderna, enunciou a proposição <em>“Todas as inovações eficazes são surpreendentemente simples”</em>.",
                   "Considere verdadeiras a proposição de Drucker e a proposição <strong>p</strong>: <em>“uma roda é uma inovação eficaz”</em>.",
                   "Em cada alternativa são apresentados diagramas de Euler-Veen, nas quais <strong>A</strong> é o conjunto das inovações eficazes, <strong>B</strong> é o conjunto das inovações “supreendentemente simples”, e existe uma região tracejada que representa o conjunto ao qual uma roda pertence.",
                   "Assim sendo, assinale a alternativa cujo diagrama indica corretamente as relações descritas."),
    "imagens": figs(("q04a", "Diagrama A: o círculo A, todo tracejado, dentro do círculo B."),
                    ("q04b", "Diagrama B: o círculo B, menor, cruza a borda do círculo A; a parte de B fora de A está tracejada."),
                    ("q04c", "Diagrama C: os círculos A e B se cruzam; só a interseção está tracejada."),
                    ("q04d", "Diagrama D: o círculo A, menor, cruza a borda do círculo B; a parte de A fora de B está tracejada."),
                    ("q04e", "Diagrama E: o círculo B, todo tracejado, dentro do círculo A.")),
    "alternativas": {"A": "[[fig:1]]", "B": "[[fig:2]]", "C": "[[fig:3]]", "D": "[[fig:4]]", "E": "[[fig:5]]"},
    "explicacao": "<p>“Todas as inovações eficazes são surpreendentemente simples” significa que A está contido em B. A roda é uma inovação eficaz, então pertence a A, e portanto também a B. O diagrama certo mostra A dentro de B, com A tracejado. Alternativa <strong>A</strong>.</p><p>Em B, C e D, parte de A fica fora de B, o que contradiz a frase de Drucker. E em E é B que está dentro de A, e a região tracejada não representa todo o conjunto A.</p>"},
5: {"materia": "Biologia", "assunto": "Microbiologia", "tags": ["fermentação", "história da ciência"],
    "enunciado": p(*T(4, "Apesar de o termo biotecnologia ter sido", "um processo exclusivamente químico.", ["Em 1674, os agentes"]), "A partir do texto, é correto inferir que"),
    "alternativas": alts("as observações detalhadas de micro-organismos em processos de fermentação foram feitas por mesopotâmicos, egípcios e gregos.",
                         "o pesquisador Antonie Van Leeuwenhoek, apesar de usar um microscópio simples, conseguiu, pela primeira vez, descrever o ciclo de vida de micro-organismos fermentadores.",
                         "os cientistas franceses demonstraram que a fermentação é um processo exclusivamente químico que origina moléculas orgânicas pequenas sem valor energético e inúteis ao consumo humano.",
                         "o cientista Louis Pasteur contribuiu para a área das ciências relacionadas à tecnologia dos alimentos ao demonstrar que todos os processos de fermentação eram resultados de atividade microbiana.",
                         "os processos de fermentação na produção de bebidas alcoólicas, pães, iogurtes e queijos ocorrem de maneira espontânea, desde a antiguidade até os dias atuais, e independem da existência de qualquer organismo vivo."),
    "explicacao": "<p>O texto diz que Pasteur “comprovou que eram causados pela ação de micro-organismos presentes no ar”, derrubando a ideia de que a fermentação era um processo só químico. Isso fundou a base científica da tecnologia de alimentos. Alternativa <strong>D</strong>.</p><p>Os povos antigos usavam a fermentação sem conhecer seus agentes (A). Leeuwenhoek descreveu a existência dos micro-organismos, não seu ciclo de vida (B). Pasteur derrubou, e não confirmou, a teoria química (C). E a fermentação depende de seres vivos (E).</p>"},
6: {"materia": "Biologia", "assunto": "Microbiologia", "tags": MULTI + ["fermentação alcoólica", "Egito Antigo"],
    "enunciado": p("A produção de pão teve notório desenvolvimento no Antigo Egito devido a vários fatores, entre os quais se destacam: o cultivo do trigo nas férteis margens do Nilo; os progressos na farinação e na peneiração da farinha; a preparação da massa, que era amassada com os pés; e os conhecimentos empíricos sobre fermentação.",
                   "No entanto, os egípcios não sabiam que os principais responsáveis pelo processo de fermentação da massa eram os fungos unicelulares <u><em>Saccharomyces cerevisiae</em></u>, conhecidos como leveduras. Nesse processo, a massa se expande e se torna mais aerada e leve.",
                   "As leveduras mencionadas no texto transformam, por meio de enzimas, os açúcares da massa em"),
    "alternativas": alts("dióxido de carbono e etanol.", "gás oxigênio e glicose.", "dióxido de carbono e gás oxigênio.", "gás oxigênio e ácido lático.", "dióxido de nitrogênio e metanol."),
    "explicacao": "<p>Na <strong>fermentação alcoólica</strong>, as leveduras transformam açúcares em etanol e dióxido de carbono (C₆H₁₂O₆ → 2 C₂H₅OH + 2 CO₂). É o CO₂ que forma bolhas e faz a massa crescer; o álcool evapora no forno. Alternativa <strong>A</strong>.</p><p>A fermentação não produz gás oxigênio (B, C e D). O ácido lático vem da fermentação lática, feita por bactérias (D). E dióxido de nitrogênio e metanol não são produtos da fermentação do pão (E).</p>"},
7: {"materia": "História", "assunto": "Idade Média", "tags": ["renascimento comercial e urbano", "artesãos"],
    "enunciado": p("Observe as imagens.") + "[[fig:1]]"
                 + fonte("&lt;https://tinyurl.com/mwhxmrdf&gt; Acesso em: 12.11.2022 · &lt;https://tinyurl.com/3tbr628n&gt; Acesso em: 12.11.2022")
                 + p("As cenas retratam"),
    "imagens": figs(("q07", "Duas gravuras antigas, em preto e branco, de oficinas artesanais. Na primeira, homens trabalham em bancadas, cortando e montando peças, com ferramentas e produtos pendurados nas paredes. Na segunda, com a legenda “Fig. 216 — Hatter” (chapeleiro), artesãos preparam chapéus: um homem trabalha com um arco, outro se agacha junto a um tanque, e há fôrmas de chapéu numa prateleira.")),
    "alternativas": alts("a divisão do trabalho nas linhas de montagem desenvolvidas por Henri Ford, na segunda Revolução Industrial, que se iniciou nos Estados Unidos.",
                         "a melhora das condições de trabalho dos operários da França que, contra os patrões, lideraram a Revolução Francesa, a qual promoveu mudanças nas leis trabalhistas.",
                         "a utilização de instrumentos e técnicas variados para a fabricação de diferentes produtos no período que ficou conhecido como Renascimento Urbano, na Idade Média.",
                         "as preferências e hábitos de lazer dos membros da elite romana, que foram acusados de se dedicar a atividades supérfluas, enquanto a população pobre passava fome.",
                         "as ocupações exercidas pelos escravizados africanos no Brasil colonial, que viveu grande desenvolvimento técnico e tecnológico com a chegada de mão de obra especializada."),
    "explicacao": "<p>As gravuras mostram oficinas de artesãos, com ferramentas manuais e produção em pequena escala, típicas das cidades europeias que renasceram a partir do século XI com o comércio, organizadas em corporações de ofício. Alternativa <strong>C</strong>.</p><p>Não há linha de montagem nem máquinas (A). As cenas não mostram conflito entre operários e patrões nem a Revolução Francesa (B). Não retratam lazer da elite romana (D) nem escravizados no Brasil (E).</p>"},
8: {"materia": "Matemática", "assunto": "Porcentagem", "tags": ["redução percentual"],
    "enunciado": p("Em meio às cidades, tem germinado um modelo de negócio: as fazendas verticais.",
                   "Nelas os alimentos são cultivados em uma espécie de laboratório que pode ser montado em prédios ou contêineres. Nesse processo, utiliza-se um litro de água por pé de alface, produzindo hortaliça livre de agrotóxicos. Contudo, se fosse no campo, seguindo o modelo tradicional, estima-se que seriam necessários 40 litros de água por pé de alface. Além disso, se no campo a semente pode levar até 70 dias para virar a hortaliça, na fazenda vertical, a média é de 40 dias.",
                   "Assim, é correto afirmar que as fazendas verticais promovem uma redução de cerca de ____<strong>I</strong>____ na quantidade de água utilizada na agricultura tradicional, e de aproximadamente ____<strong>II</strong>____ na quantidade de dias para a semente virar hortaliça.",
                   "Assinale a alternativa que completa de forma correta as informações I e II do texto."),
    "alternativas": colunas(["I", "II"], [["25,0 %", "42,9 %"], ["25,0 %", "50,0 %"], ["25,0 %", "57,1 %"], ["97,5 %", "42,9 %"], ["97,5 %", "57,1 %"]]),
    "explicacao": "<p>Água: de 40 L para 1 L, uma redução de 39 L em 40, ou 39 ÷ 40 = 97,5%. Dias: de 70 para 40, uma redução de 30 em 70, ou 30 ÷ 70 ≈ 42,9%. Alternativa <strong>D</strong>.</p><p>25% vem de dividir 1 por 40 sem tirar de 100% (A, B e C). E 57,1% é 40 ÷ 70, a fração que sobra, não a redução (C e E).</p>"},
9: {"materia": "Matemática", "assunto": "Matrizes",
    "enunciado": p("Qualquer elemento de uma matriz <strong>M</strong> pode ser representado por <strong>m<sub>ij</sub></strong>, em que “i” representa a linha e “j”, a coluna em que esse elemento se localiza.",
                   "Dada a matriz <strong>M</strong>, considere que cada elemento <strong>m<sub>ij</sub></strong> da matriz apresentada indica a quantidade, em quilogramas, da hortaliça h<sub>i</sub> (h<sub>1</sub> = agrião, h<sub>2</sub> = almeirão e h<sub>3</sub> = alface) produzida pela fazenda vertical f<sub>j</sub> (f<sub>1</sub>, f<sub>2</sub> e f<sub>3</sub>). Assim, cada elemento dessa matriz representa a quantidade de um tipo de hortaliça produzida em média, semanalmente, para cada fazenda.")
                 + "\\[M = \\begin{bmatrix} 250 & 580 & 640 \\\\ 160 & 110 & 80 \\\\ 900 & 620 & 590 \\end{bmatrix}\\]"
                 + p("A análise dos dados apresentados na matriz permite concluir corretamente que, em média, a produção semanal,"),
    "alternativas": alts("do total de hortaliças da fazenda f<sub>3</sub> foi maior do que a da fazenda f<sub>1</sub>.", "de alface da fazenda f<sub>2</sub> foi menor do que nas demais.",
                         "de almeirão da fazenda f<sub>1</sub> é o dobro da fazenda f<sub>3</sub>.", "de agrião da fazenda f<sub>2</sub> foi maior do que nas demais.",
                         "do total de hortaliças da fazenda f<sub>1</sub> foi maior do que a da fazenda f<sub>3</sub>."),
    "explicacao": "<p>As linhas são as hortaliças e as colunas, as fazendas. O almeirão é a linha 2: m<sub>21</sub> = 160 kg na f<sub>1</sub> e m<sub>23</sub> = 80 kg na f<sub>3</sub>. Como 160 = 2 · 80, é o dobro. Alternativa <strong>C</strong>.</p><p>Os totais por fazenda (colunas) são f<sub>1</sub> = 1 310, f<sub>2</sub> = 1 310 e f<sub>3</sub> = 1 310 kg: nenhum é maior que outro (A e E). A alface da f<sub>2</sub> (620) não é a menor; a menor é a da f<sub>3</sub> (590) (B). E o agrião da f<sub>2</sub> (580) é menor que o da f<sub>3</sub> (640) (D).</p>"},
10: {"materia": "Química", "assunto": "Reações químicas", "tags": ["combustão", "energia"],
     "enunciado": p(*T(5, "A combustão de 1,0 kg de hidrogênio libera", "abastecido com 5,6 kg de hidrogênio.", ["Considerando que um carro"])),
     "alternativas": alts("1,0 × 10<sup>3</sup>", "1,6 × 10<sup>3</sup>", "1,9 × 10<sup>4</sup>", "2,1 × 10<sup>4</sup>", "3,2 × 10<sup>4</sup>"),
     "explicacao": "<p>A combustão de 5,6 kg libera 5,6 · 28 700 = 160 720 kcal. O carro aproveita 20%: 0,2 · 160 720 ≈ 32 144 kcal ≈ <strong>3,2 × 10<sup>4</sup> kcal</strong>. Alternativa <strong>E</strong>.</p><p>Os outros valores vêm de esquecer a massa de 5,6 kg ou de aplicar a porcentagem de forma errada.</p>"},
11: {"materia": "Química", "assunto": "Reações químicas", "tags": ["hidrogênio", "fontes de energia"],
     "enunciado": p("A produção de hidrogênio requer grande quantidade de energia. Dependendo da fonte de energia utilizada no processo de produção dessa substância, o hidrogênio é classificado por cores:")
                  + tabela(["Cor", "Produção"], [["<strong>Verde</strong>", "é produzido pela eletrólise da água. Esse processo usa energia proveniente de fontes renováveis cuja emissão de gases estufa é baixa."],
                                                  ["<strong>Turquesa</strong>", "é produzido a partir da pirólise do principal componente do gás natural (gás metano), que produz gás hidrogênio e carbono sólido."],
                                                  ["<strong>Marrom</strong>", "é produto da gaseificação do carvão, ou seja, da reação do carvão com vapor d’água em altas temperaturas, processo que usa energia derivada de fontes de energia não renováveis."],
                                                  ["<strong>Cinza</strong>", "é obtido da reforma a vapor do gás natural, que consiste na reação do gás metano com vapor d’água."]])
                  + p("A figura mostra as fontes de energia e o modo como estão relacionadas à produção de hidrogênio.") + "[[fig:1]]"
                  + p("Considerando o texto e a figura, o hidrogênio produzido em (I), (II), (III) e (IV) é classificado, respectivamente, pelas cores"),
     "imagens": figs(("q11", "Esquema com uma nuvem “HIDROGÊNIO” no centro, ligada a quatro processos. (I), à direita: C(s) + H₂O(v) → CO(g) + H₂(g), com calor, a partir de uma fonte de energia fóssil (energia térmica). (II), acima: CH₄(g) → C(s) + 2 H₂(g), com calor, a partir de uma fonte de energia solar ou nuclear (energia térmica). (III), abaixo: CH₄(g) + H₂O(v) ⇌ CO(g) + 3 H₂(g), a partir de uma fonte de energia fóssil (energia térmica). (IV), à esquerda: H₂O(ℓ) → ½ O₂(g) + H₂(g), com um raio indicando eletricidade, a partir de uma fonte de energia eólica ou solar (energia elétrica).")),
     "alternativas": alts("verde, turquesa, marrom e cinza.", "turquesa, verde, cinza e marrom.", "marrom, cinza, turquesa e verde.", "marrom, turquesa, cinza e verde.", "cinza, marrom, verde e turquesa."),
     "explicacao": "<p>(I) Carvão (C) reagindo com vapor d’água: gaseificação do carvão, <strong>marrom</strong>. (II) Metano se decompondo em carbono sólido e hidrogênio: pirólise, <strong>turquesa</strong>. (III) Metano reagindo com vapor d’água: reforma a vapor, <strong>cinza</strong>. (IV) Eletrólise da água com energia eólica ou solar: <strong>verde</strong>. Alternativa <strong>D</strong>.</p><p>As outras alternativas trocam pelo menos um dos processos de cor.</p>"},
12: {"materia": "Português", "assunto": "Semântica", "tags": ["paráfrase"],
     "enunciado": MILTON + P12,
     "alternativas": alts("A junção entre técnica e ciência ocorre com o auxílio do mercado que, por causa da ciência e da técnica, transforma-se em um mercado global.",
                          "A separação da técnica e da ciência ocorre por causa do mercado que, pela influência daquelas, transforma-se em mercado global.",
                          "A influência da técnica sobre a ciência ocorre por causa do mercado global que só existe devido à transmissão do conhecimento.",
                          "A harmonização entre técnica e ciência deve ser feita pela influência do mercado global apesar da diferença existente entre elas.",
                          "A síntese da técnica e da ciência se dá por meio da influência do comércio global que se transmuta em mercado global apesar da ciência e da técnica."),
     "explicacao": "<p>“União” vira “junção”, “sob a égide do mercado” (sob a proteção, com o amparo) vira “com o auxílio do mercado”, e “graças à ciência e à técnica” vira “por causa da ciência e da técnica”. O sentido se mantém. Alternativa <strong>A</strong>.</p><p>B troca união por separação. C fala de influência de uma sobre a outra e muda a causa. D transforma o fato em obrigação (“deve ser feita”) e inventa uma diferença. E diz “apesar da ciência e da técnica”, o contrário de “graças a”.</p>"},
13: {"materia": "Geografia", "assunto": "Globalização", "tags": ["meio técnico-científico-informacional"],
     "enunciado": p("De acordo com Milton Santos, o meio técnico-científico-informacional refere-se"), "apoio_de": (12, P12),
     "alternativas": alts("à condição primitiva do ser humano, em um espaço geográfico pouco modificado.", "à influência da natureza sobre as relações humanas durante a Idade Média.",
                          "ao fim do uso da ciência e da tecnologia pelos seres humanos.", "à união entre a ciência e a técnica, aliadas à informação.", "à mecanização integral do meio natural do nosso planeta."),
     "explicacao": "<p>Para Milton Santos, depois da Segunda Guerra a ciência e a técnica se unem, e os objetos técnicos passam a ser também informacionais: é o meio <strong>técnico-científico-informacional</strong>. Alternativa <strong>D</strong>.</p><p>A condição primitiva e pouco modificada é o meio natural (A). O texto trata do período posterior à Segunda Guerra, não da Idade Média (B). A ciência e a tecnologia ganham importância, não deixam de ser usadas (C). E o autor não fala em mecanização integral do planeta (E).</p>"},
14: {"materia": "Biologia", "assunto": "Genética", "tags": ["DNA recombinante", "biotecnologia"],
     "enunciado": p(*T(7, "Até a década de 1980, a insulina aplicada", "insulina humana porque receberam", ["Com os avanços nos conhecimentos", "Nessa técnica, as bactérias", "As bactérias modificadas passam"])),
     "alternativas": alts("os fragmentos de ribose e de grupos fosfatos, que são importantes na produção do DNA.", "as enzimas de restrição, que cortam o RNA em pontos específicos.",
                          "a sequência da molécula de DNA que codifica esse hormônio.", "os aminoácidos do DNA e do RNA, que são usados na produção desse hormônio.",
                          "as moléculas de RNA mensageiro do genoma humano, que transportam aminoácidos."),
     "explicacao": "<p>Na técnica do DNA recombinante, o <strong>gene humano da insulina</strong>, um trecho de DNA, é inserido na bactéria. Ela passa a transcrever e traduzir esse gene, produzindo a proteína humana. Alternativa <strong>C</strong>.</p><p>O DNA tem desoxirribose, não ribose, e fragmentos soltos não produzem proteína (A). Enzimas de restrição cortam DNA e são só uma ferramenta do processo (B). DNA e RNA não têm aminoácidos (D). E quem transporta aminoácidos é o RNA transportador (E).</p>"},
15: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": MULTI + ["poliomielite", "vacinação"],
     "enunciado": POLIO + P15,
     "alternativas": alts("em 2020, um relatório da OMS expressou satisfação com o programa de vacinação brasileiro, celebrando a possibilidade de reintrodução do poliovírus no Brasil.",
                          "no Brasil, a imunização em massa foi iniciada em 1961, em um programa abrangente que manteve a continuidade necessária para o controle da doença.",
                          "embora a primeira campanha nacional de imunização contra a pólio tenha sido elaborada no Brasil em 1980, atualmente a adesão à vacinação é baixa.",
                          "desenvolvida por Oswaldo Cruz, a técnica de diagnóstico do poliovírus, erradicou a doença na década de 1970 e, por isso, atualmente o país saiu da lista de alto risco para a doença.",
                          "desde 1961, a vacinação contra a pólio é obrigatória e, atualmente, o Brasil imuniza 44% de suas crianças, um número satisfatório para o controle da doença no país."),
     "explicacao": "<p>O Texto 1 diz que a primeira campanha nacional foi em 1980, e o Texto 2, que em 2022 “a adesão à vacina ainda é baixa”, com só 44% das crianças vacinadas. Alternativa <strong>C</strong>.</p><p>O relatório de 2020 expressou preocupação, não satisfação (A). A imunização de 1961 não teve abrangência nem continuidade (B). A técnica de diagnóstico foi introduzida no Instituto Oswaldo Cruz, a doença foi eliminada em 1994, e hoje o país está na lista de alto risco (D). E 44% não é satisfatório (E).</p>"},
16: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": ["poliomielite", "vírus"],
     "enunciado": p("Sobre a doença descrita nos textos, é correto afirmar que"), "apoio_de": (15, P15),
     "alternativas": alts("deve ser tratada por meio da aplicação de soro produzido a partir das bactérias patogênicas atenuadas que causam essa enfermidade.",
                          "se espalha rapidamente entre comunidades sem cobertura vacinal adequada, pois a ampla vacinação impede a circulação do vírus.",
                          "deve ser prevenida por meio de vacinas que contenham os anticorpos específicos para combater os micro-organismos causadores dessa infecção.",
                          "trata-se de uma doença bacteriana transmitida por gotículas de saliva, ou por meio da ingestão de água ou alimentos contaminados por fezes de doentes.",
                          "apresenta várias formas de transmissão, principalmente por meio da picada dos insetos infectados, conhecidos popularmente como barbeiros; ou por meio do contato com uma pessoa contaminada, quando esta espirra ou tosse."),
     "explicacao": "<p>A poliomielite é causada por um vírus. Quando muita gente está vacinada, o vírus não encontra onde circular; onde a cobertura cai, ele volta a se espalhar rapidamente. Por isso a baixa adesão preocupa a OMS. Alternativa <strong>B</strong>.</p><p>A pólio é viral, não bacteriana, e não há soro para ela (A e D). A vacina contém o vírus atenuado ou inativado, não anticorpos (C). E o barbeiro transmite a doença de Chagas, não a pólio (E).</p>"},
17: {"materia": "Química", "assunto": "Equilíbrio químico", "tags": ["constante de equilíbrio"],
     "enunciado": p("O hidrogênio é matéria-prima fundamental na produção de produtos químicos como amônia, indispensável na indústria de fertilizantes.",
                    "Na produção de amônia, temos o equilíbrio químico representado pela equação química:")
                  + "\\[\\text{N}_2(g) + 3\\,\\text{H}_2(g) \\rightleftharpoons 2\\,\\text{NH}_3(g)\\]"
                  + p("A expressão da constante de equilíbrio da produção de amônia é dada por:")
                  + "\\[K = \\frac{[\\textit{PRODUTOS}]}{[\\textit{REAGENTES}]} = \\frac{[\\text{NH}_3]^2}{[\\text{H}_2]^3 \\cdot [\\text{N}_2]}\\]"
                  + p("Agora, considere a equação química que representa o equilíbrio químico da reforma a vapor do gás natural:")
                  + "\\[\\text{CH}_4(g) + \\text{H}_2\\text{O}(g) \\rightleftharpoons 3\\,\\text{H}_2(g) + \\text{CO}(g)\\]"
                  + p("Desse modo, assinale a alternativa que contém a expressão correta da constante de equilíbrio para a transformação que ocorre na reforma a vapor do gás natural."),
     "alternativas": alts("\\(K = \\dfrac{[\\text{CH}_4]}{[\\text{H}_2]}\\)", "\\(K = \\dfrac{[\\text{H}_2\\text{O}] \\cdot [\\text{CH}_4]}{[\\text{H}_2]^3}\\)",
                          "\\(K = \\dfrac{[\\text{CH}_4] \\cdot [\\text{H}_2\\text{O}]}{[\\text{CO}] \\cdot [\\text{H}_2]^3}\\)", "\\(K = \\dfrac{[\\text{CO}] \\cdot [\\text{H}_2]^3}{[\\text{CH}_4] \\cdot [\\text{H}_2\\text{O}]}\\)",
                          "\\(K = \\dfrac{[\\text{CO}] \\cdot [\\text{H}_2]}{[\\text{CH}_4] \\cdot [\\text{H}_2\\text{O}]}\\)"),
     "explicacao": "<p>A constante tem os produtos no numerador e os reagentes no denominador, cada concentração elevada ao seu coeficiente. Os produtos são CO (coeficiente 1) e H₂ (coeficiente 3); os reagentes, CH₄ e H₂O (coeficiente 1). Então \\(K = \\dfrac{[\\text{CO}] \\cdot [\\text{H}_2]^3}{[\\text{CH}_4] \\cdot [\\text{H}_2\\text{O}]}\\). Alternativa <strong>D</strong>.</p><p>A e B invertem produtos e reagentes ou esquecem um deles. C inverte a fração inteira. E esquece o expoente 3 do H₂.</p>"},
18: {"materia": "Biologia", "assunto": "Citologia", "tags": ["microscópios"],
     "enunciado": p(*T(9, "Os microscópios e outros instrumentos ópticos", "engenheiros, entre outros."), "Com relação a alguns desses instrumentos, é correto afirmar que"),
     "alternativas": alts("a invenção dos microscópios eletrônicos foi fundamental para a descoberta das primeiras células e permitiu a identificação dos elementos químicos da tabela periódica.",
                          "as lunetas são um tipo de microscópio óptico de baixo custo muito utilizado nos hospitais para baratear a realização de diversos tipos de exames de sangue.",
                          "os microscópios eletrônicos apresentam elevado poder de resolução que permite o estudo minucioso das estruturas celulares.",
                          "as observações detalhadas dos vírus, em microbiologia, foram feitas a partir da invenção do primeiro microscópio óptico simples.",
                          "o principal objetivo do uso dos microscópios ópticos é possibilitar o estudo minucioso da estrutura dos átomos e das ligações químicas."),
     "explicacao": "<p>O microscópio eletrônico usa feixes de elétrons e tem resolução muito maior que a do óptico, o que permite ver em detalhe organelas e membranas, a chamada ultraestrutura celular. Alternativa <strong>C</strong>.</p><p>As primeiras células foram vistas no século XVII com microscópios ópticos, e o eletrônico é do século XX (A). Lunetas servem para observar objetos distantes, não são microscópios (B). Vírus só puderam ser vistos com o microscópio eletrônico (D). E microscópios ópticos não mostram átomos (E).</p>"},
19: {"materia": "História", "assunto": "Renascimento", "tags": ["imprensa", "Gutenberg"],
     "enunciado": apoio("A Biblioteca Nacional do Reino Unido (British Library) declarou Johannes Gutenberg “o homem do milênio”, e há poucos outros que alguém poderia nomear para tal honra.")
                  + url("https://tinyurl.com/5n8tae2p", "28.10.2022") + p("Tal honraria se deve à invenção"),
     "alternativas": alts("da câmera fotográfica que permitiu a captação de imagens e impulsionou o mercado jornalístico no fim da Idade Média.",
                          "da imprensa, que permitiu a impressão de livros, jornais e panfletos, entre outros, e contribuiu para a disseminação de ideias.",
                          "dos estudos de anatomia, que possibilitaram a investigação e a cura de doenças como a peste negra, o tifo e a tuberculose.",
                          "dos satélites espaciais criados no contexto da Corrida Espacial, em que Estados Unidos e União Soviética disputavam a hegemonia tecnológica.",
                          "da internet, desenvolvida com o objetivo de permitir avanços tecnológicos nos campos da saúde e da educação."),
     "explicacao": "<p>Por volta de 1450, Gutenberg criou a <strong>prensa de tipos móveis</strong>. Ela barateou e acelerou a produção de livros e panfletos e ajudou a difundir as ideias do Renascimento e da Reforma Protestante. Alternativa <strong>B</strong>.</p><p>A fotografia é do século XIX (A). Gutenberg não estudou anatomia (C). Satélites e internet são do século XX (D e E).</p>"},
20: {"materia": "Química", "assunto": "Geometria molecular", "tags": MULTI + ["poliedros de Platão"],
     "enunciado": PLATAO + P20, "imagens": PLATAO_IMG,
     "alternativas": alts("trigonal plana e tetraédrica", "trigonal plana e octaédrica", "tetraédrica e octaédrica", "bipiramidal trigonal e tetraédrica", "bipiramidal trigonal e octaédrica"),
     "explicacao": "<p>Os poliedros de Platão são cinco: tetraedro, hexaedro (cubo), octaedro, dodecaedro e icosaedro. Entre as geometrias mostradas, só a <strong>tetraédrica</strong> (4 faces triangulares) e a <strong>octaédrica</strong> (8 faces triangulares) correspondem a eles. Alternativa <strong>C</strong>.</p><p>A trigonal plana é um triângulo, uma figura plana, não um poliedro (A e B). E na bipirâmide trigonal os vértices não têm o mesmo número de arestas: os do “equador” têm 4, e os dois polos, 3 (D e E).</p>"},
21: {"materia": "Química", "assunto": "Geometria molecular", "tags": MULTI,
     "enunciado": p("Dadas as substâncias: amônia, NH<sub>3</sub>; trióxido de enxofre, SO<sub>3</sub>; água, H<sub>2</sub>O; metano, CH<sub>4</sub> e dióxido de carbono, CO<sub>2</sub>.",
                    "Assinale a alternativa que apresenta a molécula com geometria trigonal plana.")
                  + apoio("Dados números atômicos<br>H = 1 · C = 6 · N = 7 · O = 8 · S = 16"),
     "apoio_de": (20, P20),
     "alternativas": alts("SO<sub>3</sub>", "NH<sub>3</sub>", "H<sub>2</sub>O", "CH<sub>4</sub>", "CO<sub>2</sub>"),
     "explicacao": "<p>No SO₃, o enxofre está ligado a três oxigênios e não tem par de elétrons livre: os três ligantes se distribuem num plano, a 120°. É <strong>trigonal plana</strong>. Alternativa <strong>A</strong>.</p><p>O NH₃ tem três ligantes e um par livre no nitrogênio, o que dá geometria piramidal (B). A água é angular (C), o metano é tetraédrico (D) e o CO₂ é linear (E).</p>"},
22: {"materia": "Física", "assunto": "Eletricidade", "tags": ["diferença de potencial"],
     "enunciado": p("Leia os quadrinhos.") + "[[fig:1]]" + url("https://tinyurl.com/vzz73asp", "24.11.2022", "Original colorido.") + p("Podemos afirmar corretamente que,"),
     "imagens": figs(("q22", "Quadrinhos em quatro faixas, cada uma com dois fios elétricos paralelos. 1: um passarinho e uma cobra estão pousados no fio de cima, tranquilos. 2: a cobra continua no fio de cima, e o passarinho voa para o fio de baixo. 3: o passarinho está no fio de baixo, e a cobra estica o corpo, com a cabeça descendo em direção a ele. 4: a cobra, com a cauda no fio de cima e a cabeça no fio de baixo, aparece eletrocutada, cercada de raios; o passarinho, no fio de baixo, observa.")),
     "alternativas": alts("no primeiro quadrinho, a cobra é eletrocutada porque o seu “serpentear” age como uma resistência elétrica, impossibilitando a passagem de corrente elétrica por seu corpo.",
                          "no segundo quadrinho, o passarinho não é eletrocutado por não estar tocando o fio de baixo, no qual a corrente elétrica passa.",
                          "no terceiro quadrinho, o passarinho não é eletrocutado, pois a cobra impede a passagem de corrente elétrica.",
                          "no quarto quadrinho, a cobra é eletrocutada, pois há passagem de corrente elétrica ao se conectar a dois potenciais elétricos diferentes.",
                          "nos quadrinhos, a cobra e o passarinho são eletrocutados por passarem de um fio a outro."),
     "explicacao": "<p>Quem toca um único fio fica com todo o corpo no mesmo potencial, sem diferença de potencial e, portanto, sem corrente. No quarto quadrinho, a cobra toca os dois fios ao mesmo tempo, que estão em potenciais diferentes: a corrente passa pelo corpo dela. Alternativa <strong>D</strong>.</p><p>Na primeira cena, a cobra não é eletrocutada (A). Os dois fios conduzem corrente; o passarinho está seguro porque toca um fio só (B e C). E só a cobra é eletrocutada (E).</p>"},
23: {"materia": "Biologia", "assunto": "Biotecnologia", "tags": ["agricultura de precisão"],
     "enunciado": p("A partir da década de 1960, o uso de tecnologia revolucionou a agricultura, no Brasil e no mundo, por meio de inúmeras inovações, como:",
                    "• na mecanização, pois o uso de máquinas, desde a preparação do solo até à colheita, agiliza o trabalho;<br>• na utilização de diversos tipos de sensores, que fornecem detalhes da plantação, como temperatura, umidade, minerais do solo, entre outros;<br>• no uso de imagens aéreas, que servem para o mapeamento de campos e para o controle de maquinários;<br>• no uso de drones, que permite monitoramento aéreo, em tempo real, dos processos de colheita;<br>• nas pesquisas, que cada vez mais avançam no melhoramento genético de plantas;<br>• e na inovação de fertilizantes e defensivos agrícolas, que se tornam mais sustentáveis.",
                    "A partir da leitura e da análise do texto, assinale a alternativa correta."),
     "alternativas": alts("As mudanças tecnológicas no setor de mecanização agrícola do Brasil estimularam a implantação do uso da tração animal por bovinos e equinos, pois apresentam maior rapidez nos processos de plantio e colheita.",
                          "Os sensores agrícolas que identificam na plantação informações, como, por exemplo, a necessidade de água no solo, registram e analisam os dados obtidos, o que potencializa a produtividade.",
                          "O uso de imagens aéreas e de drones impede o acompanhamento, em tempo real, de diferentes culturas e maquinários, pois não permite que os espaços de plantio sejam visualizados nas telas de computadores.",
                          "O melhoramento genético das plantas é decorrente da poluição ambiental e da utilização de elevadas quantidades de fertilizantes e defensivos agrícolas na lavoura, a fim de obter alimentos menos nutritivos.",
                          "Os avanços na mecanização e nas outras técnicas das atividades agrícolas apresentam pontos positivos ao meio ambiente, visto que impedem as mudanças climáticas."),
     "explicacao": "<p>O texto diz que os sensores “fornecem detalhes da plantação, como temperatura, umidade, minerais do solo”. Com esses dados, o agricultor irriga e aduba só onde precisa, e a produtividade aumenta. Alternativa <strong>B</strong>.</p><p>A mecanização substitui a tração animal (A). Drones e imagens aéreas permitem, e não impedem, o monitoramento em tempo real (C). O melhoramento genético busca plantas mais produtivas e resistentes, não resulta da poluição (D). E a tecnologia agrícola não impede as mudanças climáticas (E).</p>"},
24: {"materia": "Inglês", "assunto": "Interpretação de texto",
     "enunciado": TECHJOB + P24,
     "alternativas": alts("foi marcado por muitas demissões no primeiro semestre de 2022.", "teve crescimento de oferta de novos postos em todos os meses de 2022.", "tem aberto novas vagas de emprego apenas no sistema remoto.",
                          "mostrou aumento vertiginoso de contratações no primeiro semestre de 2022.", "apenas cresceu nos grandes centros urbanos da América e Europa."),
     "explicacao": "<p>O texto diz que as vagas cresceram 52% em relação ao primeiro semestre de 2021 e que 96% dos 50 maiores empregadores aumentaram as contratações no primeiro semestre de 2022. Alternativa <strong>D</strong>.</p><p>Fala-se em ameaças de demissão, não em muitas demissões (A). Houve queda de 17% em junho (B). Os profissionais preferem o trabalho remoto e híbrido, mas as vagas não são só remotas (C). E o texto só cita cidades dos Estados Unidos, sem dizer que o crescimento ficou restrito a elas (E).</p>"},
25: {"materia": "Inglês", "assunto": "Vocabulário", "tags": ["antônimos"],
     "enunciado": p("Assinale a alternativa que apresenta o correto par de antônimos presentes no texto."), "apoio_de": (24, P24),
     "alternativas": alts("threats – skills", "dip – spike", "layoffs – tools", "demand – talent", "employers – hubs"),
     "explicacao": "<p><em>Dip</em> é uma “queda” (a dip in job postings), e <em>spike</em>, um “pico”, uma alta repentina (a hiring spike). São antônimos. Alternativa <strong>B</strong>.</p><p><em>Threats</em> (ameaças) e <em>skills</em> (habilidades), <em>layoffs</em> (demissões) e <em>tools</em> (ferramentas), <em>demand</em> (demanda) e <em>talent</em> (talento), <em>employers</em> (empregadores) e <em>hubs</em> (polos) não têm sentidos opostos (A, C, D e E).</p>"},
26: {"materia": "Raciocínio lógico", "assunto": "Raciocínio espacial", "tags": ["porcentagem"],
     "enunciado": p(*T(12, "O carro de um motorista de aplicativo", "Barueri e Guarulhos é, em quilômetros, igual a", ["Logo, é correto afirmar"])),
     "alternativas": alts("19.", "38.", "48.", "58.", "96."),
     "explicacao": "<p>O carro quebrou a 25% do trajeto, e o posto fica a 50%. A distância entre eles é 50% − 25% = 25% do trajeto, que corresponde a 14,5 km. O trajeto todo é 4 · 14,5 = <strong>58 km</strong>. Alternativa <strong>D</strong>.</p><p>29 km seria a metade do trajeto, e 38, 48 e 96 vêm de usar outras frações (A, B, C e E).</p>"},
27: {"materia": "Física", "assunto": "Eletricidade", "tags": MULTI + ["sistema binário"],
     "enunciado": p(*[it(x, "binary digits") for x in T(13, "Em uma sociedade digital, dados são transmitidos", "finita desses algarismos binários.", ["Nos circuitos eletrônicos"])])
                  + tabela(["CARACTERES (Conversão para binário)", ""], [["A", "01000001"], ["B", "01000010"], ["C", "01000011"], ["D", "01000100"], ["E", "01000101"]])
                  + p("Na tabela, estão representados alguns caracteres e sua equivalência binária. Por sua vez, o gráfico representa apenas um desses caracteres.") + "[[fig:1]]"
                  + p("Relacionando o gráfico à tabela, podemos afirmar corretamente que o gráfico, o qual apresenta a intensidade de corrente elétrica de operação pelo tempo de transmissão do pulso, traz a informação do caráter"),
     "imagens": figs(("q27", "Gráfico de corrente (µA) por tempo (ns), dividido em oito intervalos de 0 a t₈. A corrente vale i nos intervalos de t₁ a t₂, de t₅ a t₆ e de t₇ a t₈, e vale zero nos demais (de 0 a t₁, de t₂ a t₅ e de t₆ a t₇).")),
     "alternativas": alts("A.", "B.", "C.", "D.", "E."),
     "explicacao": "<p>Lendo cada intervalo como um bit (corrente = 1, sem corrente = 0): 0–t₁: 0; t₁–t₂: 1; t₂–t₃: 0; t₃–t₄: 0; t₄–t₅: 0; t₅–t₆: 1; t₆–t₇: 0; t₇–t₈: 1. A sequência é 01000101, o caractere <strong>E</strong>. Alternativa <strong>E</strong>.</p><p>A (01000001), B (01000010), C (01000011) e D (01000100) diferem nos últimos bits.</p>"},
28: {"materia": "Português", "assunto": "Conectivos", "tags": ["orações reduzidas"],
     "enunciado": CIBER + P28,
     "alternativas": alts("consequência, equivalendo a “que consequentemente o ciberespaço se integra à sociedade contemporânea”.", "tempo, equivalendo a “quando o ciberespaço integrar-se à sociedade contemporânea”.",
                          "proporção, equivalendo a “na medida em que o ciberespaço faz parte da sociedade contemporânea”.", "concessão, equivalendo a “embora o ciberespaço seja parte integrante da sociedade contemporânea”.",
                          "causa, equivalendo a “já que o ciberespaço é parte integrante da sociedade contemporânea”."),
     "explicacao": "<p>A oração reduzida de gerúndio “sendo o ciberespaço parte integrante da sociedade” explica o motivo de ele ser “uma realidade que a Geografia deve buscar compreender”: tem valor de <strong>causa</strong>, como “já que o ciberespaço é parte integrante”. Alternativa <strong>E</strong>.</p><p>Ser parte da sociedade não é consequência (A) nem marca de tempo (B) ou de proporção (C). E não há ideia de oposição para ser concessão (D).</p>"},
29: {"materia": "Geografia", "assunto": "Conceitos geográficos", "tags": ["ciberespaço"],
     "enunciado": p("De acordo com o texto, é correto afirmar que a Geografia"), "apoio_de": (28, P28),
     "alternativas": alts("deve reconhecer o ciberespaço como parte de seu objeto de estudo.", "tem, no ciberespaço e no mundo virtual das redes, seus únicos objetos de estudo.",
                          "provoca mudanças nos hábitos culturais por ignorar a existência do ciberespaço.", "desvalorizou-se e modificou-se com a expansão e a multiplicação do ciberespaço.",
                          "obteve status de ciência, estudando os hábitos coletivos externados no ciberespaço."),
     "explicacao": "<p>O texto termina dizendo que o ciberespaço “é uma realidade que a Geografia deve buscar compreender”. Alternativa <strong>A</strong>.</p><p>O ciberespaço é parte do objeto da Geografia, não o único (B). Quem muda os hábitos é o ciberespaço, não a Geografia (C). O raciocínio geográfico “tem se revalorizado”, não desvalorizado (D). E a Geografia já era ciência antes do ciberespaço (E).</p>"},
30: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": ["cartum"],
     "enunciado": p("Leia o cartum.") + "[[fig:1]]" + url("https://tinyurl.com/5ce57zs7", "25.10.2022", "Original colorido.")
                  + apoio("«<em>We rarely back up our data. We prefer not to keep a permanent record of everything that goes wrong around here.</em>»")
                  + p("Com a avalanche de dados diários, os especialistas em cibersegurança orientam que as empresas mantenham uma forte política de backup nos seus sistemas. Entretanto, a personagem do cartum diz que não o faz, pois"),
     "imagens": figs(("q30", "Cartum de Randy Glasbergen: num escritório, um homem com crachá, sentado diante de um computador, fala com uma mulher de pé, também de crachá, que segura uma folha de papel. A legenda traz a fala dele.")),
     "alternativas": alts("não sabe como o fazer.", "não tem tempo para o fazer.", "seu sistema é imune a ataques.", "prefere que os erros não apareçam.", "confia que seus dados não serão perdidos."),
     "explicacao": "<p>A personagem diz: “Raramente fazemos backup. Preferimos não manter um registro permanente de tudo o que dá errado por aqui.” Ou seja, ela <strong>prefere que os erros não fiquem registrados</strong>. Alternativa <strong>D</strong>.</p><p>Ela não fala de não saber fazer (A), de falta de tempo (B), de sistema imune (C) nem de confiança de que os dados não se perdem (E).</p>"},
31: {"materia": "História", "assunto": "Brasil República", "tags": ["cultura de massa", "rádio e televisão"],
     "enunciado": apoio(*T(14, "Entre 1930 e 1960, o rádio foi o grande veículo", "formação da opinião pública.", ["A televisão, inaugurada em 1950", "O rádio, a televisão, o cinema"]))
                  + fonte("DOMINGUES, Joelza Esther. <em>História em documento. Imagem em texto.</em> 8. São Paulo: FTD, 2015. p.220. Adaptado.") + p("Segundo o texto,"),
     "alternativas": alts("o rádio desempenhou um papel inexpressivo como veículo de comunicação entre 1930 e 1960.", "as tecnologias de comunicação se popularizaram somente a partir da inauguração da televisão em 1950.",
                          "o rádio, inventado no Brasil, modernizou o país, juntamente com as emissoras radiofônicas estrangeiras.", "as novelas de rádio se popularizaram em 1950 e são a grande fonte de informação da opinião pública desde 1964.",
                          "as tecnologias da comunicação introduziram a cultura de massa no Brasil, e impactaram o acesso à informação."),
     "explicacao": "<p>O texto diz que “o rádio, a televisão, o cinema e a imprensa introduziram a cultura de massa no Brasil e foram importantes veículos de informação e de formação da opinião pública”. Alternativa <strong>E</strong>.</p><p>O rádio foi “o grande veículo de comunicação” do período (A) e se popularizou antes da TV (B). O texto não diz que o rádio foi inventado no Brasil (C) nem fala de novelas de rádio (D).</p>"},
32: {"materia": "Física", "assunto": "Ondas", "tags": ["velocidade", "ondas de rádio"],
     "enunciado": NFC + P32,
     "alternativas": alts("2", "3", "4", "5", "6"),
     "explicacao": "<p>A distância é ∆S = v · ∆t = 3,0 × 10⁸ m/s · 0,1 × 10⁻⁹ s = 3,0 × 10⁻² m = <strong>3 cm</strong>. Alternativa <strong>B</strong>.</p><p>Os outros valores vêm de erros na conversão de nano (10⁻⁹) ou de metros para centímetros.</p>"},
33: {"materia": "Física", "assunto": "Ondas", "tags": ["frequência", "comprimento de onda"],
     "enunciado": p("Sabendo que o comprimento de onda (λ) emitido por essa tecnologia é de aproximadamente 22 m, assinale a alternativa que apresenta correta e aproximadamente, em MHz, a frequência (f) de operação dela."), "apoio_de": (32, P32),
     "alternativas": alts("10,6", "11,5", "13,6", "15,5", "17,6"),
     "explicacao": "<p>Pela equação v = λ · f, f = v ÷ λ = 3,0 × 10⁸ ÷ 22 ≈ 1,36 × 10⁷ Hz = <strong>13,6 MHz</strong>. Alternativa <strong>C</strong>.</p><p>Os outros valores não saem da divisão de 3,0 × 10⁸ por 22.</p>"},
34: {"materia": "Matemática", "assunto": "Funções", "tags": ["função do 1º grau"],
     "enunciado": apoio(*T(15, "Os aplicativos de entrega modificaram", "o entregador ganha R$ 1,10."))
                  + url("https://tinyurl.com/yx68dbl2", "28.10.2022")
                  + p(*T(15, "De acordo com o texto, a função que relaciona", "descrito no texto, é")),
     "alternativas": alts("y = 0,70x.", "y = 4,60 + 1,10x.", "y = 4,30 + 1,40x.", "y = 2,50 + 3,20x.", "y = 5,70x."),
     "explicacao": "<p>Num processo completo há uma retirada (R$ 3,20) e uma entrega (R$ 1,40), valores fixos que somam R$ 4,60, e R$ 1,10 por quilômetro: y = 4,60 + 1,10x. Alternativa <strong>B</strong>.</p><p>C e D trocam o valor por quilômetro com um dos valores fixos. A e E não têm parte fixa e somam ou subtraem os valores de forma arbitrária.</p>"},
35: {"materia": "Português", "assunto": "Semântica", "tags": MULTI + ["verbete"],
     "enunciado": p("No dicionário, um verbete é um texto organizado assim: primeiro vem a palavra (chamada de entrada), depois sua classe morfológica e gênero e, por fim, os diferentes sentidos da palavra.",
                    "A figura apresenta um verbete de dicionário, cuja entrada foi omitida devido a um erro de impressão.") + "[[fig:1]]"
                  + p("Se a entrada que corresponde a essa definição é de um substantivo masculino formado por 8 letras, então é correto afirmar que sua primeira letra é"),
     "imagens": figs(("q35", "Recorte de um verbete de dicionário com a palavra de entrada coberta por uma mancha de tinta. Depois dela: “s.m. 1 atividade profissional regular remunerada ou assalariada.”")),
     "alternativas": alts("P.", "E.", "S.", "O.", "T."),
     "explicacao": "<p>Um substantivo masculino de 8 letras que significa “atividade profissional regular remunerada ou assalariada” é <strong>trabalho</strong> (T-R-A-B-A-L-H-O). Alternativa <strong>E</strong>.</p><p>“Emprego” tem o mesmo sentido, mas só 7 letras (B). “Serviço” também tem 7 (C). E não há sinônimos adequados de 8 letras começando por P ou O (A e D).</p>"},
36: {"materia": "Física", "assunto": "Astronomia", "tags": ["telescópios espaciais", "razão"],
     "enunciado": p(*T(15, "Em uma órbita aproximada de 530", "nossa existência presente e futura."), "Sobre os telescópios, é correto afirmar que"),
     "alternativas": alts("o James Webb ficará exposto a uma temperatura maior, pois é mais fácil não existir interferência de radiações infravermelhas com altas temperaturas.",
                          "a trajetória do Hubble é mais segura de se manter no espaço, pois está longe da interferência da gravidade e das tempestades solares.",
                          "eles estarão sujeitos à poluição oriunda da poeira cósmica advinda do Sol, apesar de a poluição atmosférica ser minimizada.",
                          "ambos operam apenas na faixa do infravermelho e entraram em operação simultaneamente.",
                          "a relação entre as órbitas do James Webb e a do Hubble até o momento é de, aproximadamente, três mil vezes."),
     "explicacao": "<p>A razão entre as distâncias é 1 500 000 km ÷ 530 km ≈ 2 830, cerca de <strong>três mil vezes</strong>. Alternativa <strong>E</strong>.</p><p>Telescópios infravermelhos precisam de frio, porque o calor emite infravermelho e atrapalha as medições (A). O Hubble, mais perto, sofre mais com a gravidade da Terra (B). O Sol não emite “poeira cósmica” que polua os telescópios (C). E o Hubble foi lançado em 1990 e opera sobretudo na luz visível e no ultravioleta (D).</p>"},
37: {"materia": "Geografia", "assunto": "Cartografia", "tags": ["GPS", "geotecnologias"],
     "enunciado": apoio(it(" ".join(T(16, "GPS (Global Positioning System ou Sistema", "e em qualquer lugar do planeta.")), "Global Positioning System"))
                  + url("https://tinyurl.com/2p8wmjx7", "12.10.2022") + p("É correto afirmar que esse sistema"),
     "alternativas": alts("utiliza satélites e dispositivos para fornecer informações sobre a localização do aparelho receptor no globo terrestre.", "funciona em qualquer lugar do universo, desde que as condições climáticas sejam favoráveis.",
                          "fornece as coordenadas de todos os lugares do subsolo terrestre, desde que tenhamos um receptor de sinais de televisão.", "capta os sinais dos balões atmosféricos, enviando-os para um receptor que calcula a posição do aparelho.",
                          "opera com perfeição em áreas continentais, porém, em alto-mar e no espaço aéreo, ele não é utilizado."),
     "explicacao": "<p>O GPS é um sistema de geolocalização por satélite que fornece ao aparelho receptor sua posição e a hora exata. Alternativa <strong>A</strong>.</p><p>Ele funciona em qualquer lugar do planeta, independentemente do clima, não do universo (B). Não usa sinais de TV nem mapeia o subsolo (C). Usa satélites, não balões (D). E é muito usado na navegação marítima e aérea (E).</p>"},
38: {"materia": "Raciocínio lógico", "assunto": "Raciocínio espacial", "tags": ["circunferência e retas paralelas"],
     "enunciado": p(*T(16, "Ao trabalhar com o serviço de entregas", "uma rua paralela a ela”.", ["Suponha que uma empresa", "Ao realizar o pedido"]))
                  + p("Devido a um problema no app, o entregador não consegue visualizar o endereço do cliente, tendo acesso apenas ao esquema da figura.") + "[[fig:1]]"
                  + p("Se a distância, em linha reta, da Empresa até a Avenida Bom Sucesso é de 4 km, a quantidade de pontos em que o endereço do cliente pode estar é"),
     "imagens": figs(("q38", "Esquema: uma circunferência pontilhada de raio 5 km com a Empresa (um entregador de moto) no centro. Uma reta horizontal, a Avenida Bom Sucesso, corta a parte de baixo da circunferência. Um segmento tracejado de 5 km liga a Empresa a um ponto da circunferência.")),
     "alternativas": alts("1.", "2.", "3.", "4.", "5."),
     "explicacao": "<p>O cliente está sobre a circunferência de raio 5 km. As ruas paralelas à avenida a 1 km dela ficam a 4 − 1 = 3 km ou a 4 + 1 = 5 km da Empresa. A rua a 3 km corta a circunferência em 2 pontos. A rua a 5 km fica tangente a ela e a toca em 1 ponto. São <strong>3</strong> pontos possíveis. Alternativa <strong>C</strong>.</p><p>Considerar só a rua entre a Empresa e a avenida dá 2 pontos (B). E supor que a rua mais distante também corta a circunferência em dois pontos dá 4 (D).</p>"},
39: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": MULTI + ["astronomia"],
     "enunciado": p("Leia o texto.")
                  + apoio("<strong>Climate change expected to reduce the quality of ground-based astronomical observations</strong>", "02 Oct 2022",
                          *T(16, "Climate change will negatively impact", "low temperature and water vapour.", ["The quality of astronomical observations"]))
                  + url("https://tinyurl.com/yvzdntd6", "26.10.2022")
                  + p("Segundo o texto, os instrumentos citados são frequentemente instalados em locais que apresentem"),
     "alternativas": alts("alta altitude e baixa temperatura.", "baixa altitude e baixa umidade.", "alto nível de vapor e baixa claridade atmosférica.", "pouca variação climática e baixa altitude.", "alta temperatura e alto nível de claridade."),
     "explicacao": "<p>O texto diz que os observatórios ficam em “high altitude” (grande altitude), em locais escolhidos por condições como “low temperature and water vapour” (baixa temperatura e pouco vapor d’água). Alternativa <strong>A</strong>.</p><p>A altitude é alta, não baixa (B e D). O vapor d’água deve ser baixo, e a claridade atmosférica, alta (C). E a temperatura deve ser baixa (E).</p>"},
40: {"materia": "Português", "assunto": "Figuras de linguagem", "tags": ["metáfora"],
     "enunciado": p("Analise a ilustração.") + "[[fig:1]]" + url("https://tinyurl.com/24ms5s3w", "28.10.2022", "Original colorido.")
                  + p("<em>Journey</em>, ilustração do artista polonês Pawel Kuczynski, é a concretização, por meio de imagens, de uma figura de linguagem.", "Assinale a alternativa que identifica essa figura de linguagem e que interpreta corretamente a obra."),
     "imagens": figs(("q40", "Ilustração “Journey”, de Pawel Kuczynski: um menino sentado num pequeno barco lê um livro. O mastro do barco carrega, como velas, vários livros abertos e enfunados pelo vento, como um veleiro.")),
     "alternativas": alts("Sinestesia, pois há a fusão das sensações visuais e auditivas na representação do farfalhar dos livros.", "Personificação, pois dá aos livros a capacidade de voar livremente como pássaros durante a sua elaboração.",
                          "Onomatopeia, pois representam-se os ruídos dos objetos que circulam a personagem durante uma viagem.", "Metáfora, pois atribui-se à leitura a capacidade de transportar os indivíduos a outras realidades, comparando-a a uma viagem.",
                          "Metonímia, pois o livro é utilizado como símbolo para representar o desenvolvimento cultural; e o jovem, como o futuro da sociedade."),
     "explicacao": "<p>Os livros viram as velas do barco que leva o menino: a imagem concretiza a ideia de que <strong>ler é viajar</strong>. A leitura é comparada, sem conectivo, a uma viagem: é uma <strong>metáfora</strong>. Alternativa <strong>D</strong>.</p><p>Não há fusão de sentidos (A), os livros não ganham características humanas nem voam como pássaros (B), a imagem não representa sons (C), e o livro não está no lugar de uma ideia relacionada a ele, como na metonímia (E).</p>"},
41: {"materia": "Geografia", "assunto": "Relevo", "tags": ["classificações do relevo brasileiro", "sensoriamento remoto"],
     "enunciado": apoio(*T(17, "Diversas classificações do relevo brasileiro", "com radar aerotransportado."))
                  + fonte("MORAES, Paulo Roberto. <em>Geografia Geral e do Brasil.</em> São Paulo, SP. 5 ed.: HARBRA, 2017. Adaptado.") + url("https://tinyurl.com/y9k2kndy", "13.10.2022")
                  + p("De acordo com o texto, é correto afirmar que"),
     "alternativas": alts("o professor Aroldo de Azevedo utilizou imagens de satélite na construção de sua classificação do relevo.", "o professor Aziz Ab’Saber utilizou o radar aerotransportado na construção de sua classificação do relevo.",
                          "o professor Jurandyr Ross conseguiu mapear a fauna brasileira utilizando sensoriamento remoto, a principal tecnologia de análise espacial existente na época.",
                          "o avanço tecnológico a serviço da ciência foi paulatino no que tange às classificações do relevo apresentadas.",
                          "o uso de tecnologias modernas está presente nas classificações do relevo, evidenciando que, mesmo no século XIX, foram realizadas três classificações do relevo."),
     "explicacao": "<p>As classificações vieram em etapas, cada uma com mais tecnologia e apoiada nas anteriores: esboços (anos 1940), fotografias aéreas (anos 1950 e 1960) e radar do RADAMBRASIL (anos 1980). O avanço foi <strong>paulatino</strong>, gradual. Alternativa <strong>D</strong>.</p><p>Aroldo de Azevedo usou esboços preexistentes (A). Ab’Saber usou fotografias aéreas, e o radar foi base para Ross (B). Ross classificou o relevo, não a fauna (C). E as três classificações são do século XX (E).</p>"},
42: {"materia": "Matemática", "assunto": "Estatística", "tags": ["desvio padrão"],
     "enunciado": p(*T(18, "A Orientação Profissional (OP) tem", "como mostrado na tabela.", ["Entre os instrumentos utilizados", "Essa escala está organizada"]))
                  + tabela(["Dimensões do EAP", "Mínimo", "Máximo", "Média", "Desvio Padrão"],
                           [["Ciências Exatas", "1,00", "5,00", "2,58", "1,05"], ["Artes e Comunicação", "1,00", "4,71", "2,64", "0,88"], ["Ciências Biológicas e da Saúde", "1,00", "5,00", "2,91", "1,13"],
                            ["Ciências Agrárias e Ambientais", "1,00", "5,00", "2,91", "1,13"], ["Atividades Burocráticas", "1,15", "5,00", "2,87", "0,81"], ["Ciências Humanas e Sociais Aplicadas", "1,00", "4,90", "2,93", "0,85"], ["Entretenimento", "1,00", "4,83", "2,42", "0,95"]])
                  + fonte("Tabela – Estatística Descritiva das Dimensões do EAP. &lt;https://tinyurl.com/3t8fm473&gt; Acesso em: 05.11.2022. Adaptado.")
                  + p("Com base nesses dados, assinale a afirmativa correta."),
     "alternativas": alts("As preferências dos entrevistados, em relação à dimensão <em>Atividades Burocráticas</em>, são as mais dispersas em torno da média.",
                          "Apesar de as médias serem diferentes, as preferências dos entrevistados são mais homogêneas em relação à dimensão <em>Atividades Burocráticas</em> do que à dimensão <em>Artes e Comunicação</em>.",
                          "As preferências dos entrevistados, em relação às dimensões <em>Ciências Exatas</em> e <em>Ciências Biológicas e da Saúde</em>, têm o mesmo nível de heterogeneidade, visto que possuem a mesma amplitude.",
                          "Apesar de as médias serem diferentes, as preferências dos entrevistados são mais homogêneas em relação à dimensão <em>Ciências Exatas</em> do que à dimensão <em>Artes e Comunicação</em>.",
                          "As preferências dos entrevistados, em relação à dimensão <em>Ciências Biológicas e da Saúde</em>, são as menos dispersas em torno da média."),
     "explicacao": "<p>Quanto menor o desvio padrão, mais homogêneos os dados. Atividades Burocráticas tem o menor desvio da tabela (0,81), menor que o de Artes e Comunicação (0,88). Alternativa <strong>B</strong>.</p><p>Atividades Burocráticas é a <em>menos</em> dispersa (A). A mesma amplitude não garante a mesma dispersão, e os desvios de Exatas (1,05) e Biológicas (1,13) são diferentes (C). Exatas (1,05) é mais heterogênea que Artes (0,88) (D). E Biológicas tem o maior desvio, empatada com Agrárias (E).</p>"},
43: {"materia": "Matemática", "assunto": "Geometria plana", "tags": ["escala", "perímetro"],
     "enunciado": p("Um estudante de Construção Civil da Fatec está executando um desenho técnico, para um projeto de uma fazenda vertical. Na planta baixa, apresentada na imagem, estão especificadas algumas medidas na escala 1∶500 – em que 1 m na medida real corresponde a 0,2 cm na planta baixa.") + "[[fig:1]]"
                  + p("Logo, o perímetro da construção será, em metros, igual a"),
     "imagens": figs(("q43", "Planta baixa em forma de L, com todos os ângulos retos. A parte de cima tem 10,5 cm de largura; o lado esquerdo tem 24,4 cm de altura; a parte de baixo se estende para a direita, e o degrau horizontal interno mede 11,9 cm.")),
     "alternativas": alts("18,7.", "46,8.", "93,6.", "187,2.", "468,0."),
     "explicacao": "<p>Numa figura em L com ângulos retos, o perímetro é igual ao do retângulo que a contém. A altura é 24,4 cm e a largura total é 10,5 + 11,9 = 22,4 cm: P = 2 · (24,4 + 22,4) = 93,6 cm na planta. Como 0,2 cm equivalem a 1 m, 93,6 ÷ 0,2 = <strong>468 m</strong>. Alternativa <strong>E</strong>.</p><p>93,6 é o perímetro em centímetros na planta, sem aplicar a escala (C). 187,2 e 46,8 usam a escala errada (o dobro ou a metade de 93,6) (B e D). E 18,7 vem de multiplicar por 0,2 em vez de dividir (A).</p>"},
44: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": ["cherry picking"],
     "enunciado": CHERRY + P44,
     "alternativas": alts("disseminar notícias falsas deliberadamente, provocando pânico.", "facilitar a interpretação do leitor, simplificando os fatos.", "focar em certos aspectos da notícia, ignorando fatos mais relevantes.",
                          "atrair o leitor para o consumo consciente, provocando reflexão.", "inventar dados preocupantes, causando sensacionalismo."),
     "explicacao": "<p>O texto define <em>cherry picking</em> (“escolher as cerejas”) como apresentar só um lado da história, ignorando os fatos que sustentam outros pontos de vista. No exemplo, o repórter cita os 1% que discordam e omite os 99%. Alternativa <strong>C</strong>.</p><p>A informação não é falsa nem inventada, apenas parcial (A e E). Não se trata de simplificar para o leitor (B) nem de estimular a reflexão (D).</p>"},
45: {"materia": "Inglês", "assunto": "Vocabulário",
     "enunciado": p("A expressão <em>plenty of</em> na sentença “there are <em>plenty of</em> scientists who disagree with the consensus position on this phenomenon” poderia ser substituída, sem prejuízo de informação, por"), "apoio_de": (44, P44),
     "alternativas": alts("few.", "less.", "much.", "many.", "enough."),
     "explicacao": "<p><em>Plenty of</em> significa “muitos”, “bastantes”. Com um substantivo contável no plural (<em>scientists</em>), o equivalente é <strong><em>many</em></strong>. Alternativa <strong>D</strong>.</p><p><em>Few</em> (poucos) e <em>less</em> (menos) têm sentido oposto (A e B). <em>Much</em> se usa com incontáveis (C). E <em>enough</em> (suficientes) muda o sentido (E).</p>"},
46: {"materia": "Geografia", "assunto": "População", "tags": MULTI + ["amplitude térmica", "cartografia"],
     "enunciado": apoio("A relação entre Matemática e Geografia é antiga. Entre os campos da Geografia que se utilizam da Matemática podemos citar a Cartografia, a Demografia e a Climatologia.")
                  + url("https://tinyurl.com/2jh6b4fv", "14.10.2022") + p("Assinale a alternativa em que o cálculo matemático e o conceito geográfico estão descritos de forma correta."),
     "alternativas": alts("A escala de um mapa é o valor percentual que indica quantas vezes a medida real de um território foi aumentada.", "A população absoluta é dada pela razão entre o total de habitantes de uma determinada região e a área abrangida por ela.",
                          "A amplitude térmica é a diferença entre as temperaturas máxima e mínima de um determinado local ao longo de um determinado tempo.", "As latitudes são semicircunferências imaginárias na superfície da Terra, cujos extremos coincidem com o Meridiano de Greenwich e com os Polos Norte e Sul.",
                          "A taxa de fecundidade é a diferença entre as taxas de natalidade e de mortalidade, representando a frequência com que ocorrem os nascimentos e os óbitos em uma dada população."),
     "explicacao": "<p>A <strong>amplitude térmica</strong> é a diferença entre a temperatura máxima e a mínima registradas num lugar em certo período (um dia, um ano). Alternativa <strong>C</strong>.</p><p>A escala indica quantas vezes a realidade foi <em>reduzida</em>, e não é um percentual (A). Habitantes divididos pela área é a densidade demográfica; a população absoluta é o total de habitantes (B). Semicircunferências de polo a polo são os meridianos; latitude é a distância angular até o Equador (D). E natalidade menos mortalidade é o crescimento vegetativo; fecundidade é o número médio de filhos por mulher (E).</p>"},
47: {"materia": "Química", "assunto": "Estrutura atômica", "tags": ["tabela periódica"],
     "enunciado": p(*T(20, "Um professor criou um jogo de estratégia", "da sala você irá escapar”.", ["Durante o jogo, na procura"])) + "[[fig:1]]"
                  + tabela(["Pista", ""], [["<strong>Pista 1</strong>", "Sou o elemento químico de número 1."], ["<strong>Pista 2</strong>", "Na forma de cátion bivalente, estou presente no leite, ossos e dentes."],
                                          ["<strong>Pista 3</strong>", "Sou o halogênio do segundo período."], ["<strong>Pista 4</strong>", "Sou o metal alcalino de menor raio atômico."]])
                  + p("Após ler atentamente as pistas, cada integrante do grupo selecionou alguns elementos para serem digitados no teclado e a ordem que foram digitados.",
                      "Amanda: H, Ca, Cℓ, He<br>Beatriz: He, Ca, Cℓ, Li<br>Carol: H, Ca, F, Li<br>Daniela: H, K, F, Li<br>Eduarda: He, Ca, F, H",
                      "A integrante do grupo que pressionou as teclas correspondentes aos elementos das pistas, na ordem em que foram descritos, foi"),
     "imagens": figs(("q47", "Teclado em forma de tabela periódica simplificada, só com os símbolos dos elementos, organizados nos 7 períodos e nos 18 grupos: H e He no 1º período; Li, Be, B, C, N, O, F e Ne no 2º; Na, Mg, Al, Si, P, S, Cl e Ar no 3º; e assim por diante, até Fr, Ra e os elementos do 7º período.")),
     "alternativas": alts("Amanda.", "Beatriz.", "Carol.", "Daniela.", "Eduarda."),
     "explicacao": "<p>Pista 1: o elemento de número atômico 1 é o hidrogênio (H). Pista 2: o cátion bivalente do leite, dos ossos e dos dentes é o Ca²⁺ (Ca). Pista 3: o halogênio do 2º período é o flúor (F). Pista 4: o metal alcalino de menor raio é o lítio (Li), o primeiro do grupo 1. A sequência H, Ca, F, Li é a de <strong>Carol</strong>. Alternativa <strong>C</strong>.</p><p>Amanda e Beatriz digitaram cloro (3º período), e Daniela, potássio no lugar do cálcio (A, B e D). Eduarda trocou a ordem e usou hélio (E).</p>"},
48: {"materia": "Física", "assunto": "Magnetismo", "tags": ["eletroímã"],
     "enunciado": MAGICO + p("Sobre a realização do truque descrito, é correto afirmar que envolve conceitos de"),
     "alternativas": alts("termologia, uma vez que o botão aciona uma resistência elétrica que aquece a superfície da mala.", "eletromagnetismo, pois o botão acionado interrompe a passagem de corrente elétrica em uma bobina, colocada no palco, a qual atrai o material ferromagnético da mala.",
                          "eletromecânica, uma vez que o botão aciona, no palco, um intenso campo elétrico que repele a mala.", "eletrostática, pois o botão acionado proporciona um potencial elétrico entre a mala e o palco.",
                          "dinâmica, uma vez que o botão aciona um microexplosivo que provoca uma força elétrica contra a mala."),
     "explicacao": "<p>Sob o palco há um <strong>eletroímã</strong>: uma bobina que, com corrente, cria um campo magnético e prende a base de metal ferromagnético da mala. Quando o mágico aperta o botão, a corrente é interrompida, o campo desaparece e qualquer pessoa levanta a mala. Alternativa <strong>B</strong>.</p><p>Aquecer a mala não a prende ao chão (A). Um campo elétrico não atrai metal ferromagnético dessa forma, e o efeito seria repelir, não prender (C e D). E um explosivo não faz parte do truque (E).</p>"},
49: {"materia": "Raciocínio lógico", "assunto": "Raciocínio espacial", "tags": ["truque de mágica"],
     "enunciado": p("Mágicos podem utilizar técnicas que mexem com o imaginário e o senso lógico das pessoas. Um exemplo disso é o truque “Dado Dinamite”.") + "[[fig:1]]"
                  + p("Nele, o mágico apresenta um cartão no qual o público vê um ponto no centro; ao virar o cartão e mostrar o verso, o público vê dois pontos no cartão. Quando o mágico vira novamente esse cartão, onde o público enxergava um ponto, agora vê dois pontos e, virando novamente, o público vê, então, três pontos.",
                      "Considerando que foram usados apenas a frente e o verso de um único cartão, sem que exista nenhum outro artifício, o número mínimo de pontos que o mágico deve desenhar no cartão (frente e verso) utilizado é igual a"),
     "imagens": figs(("q49", "Quatro desenhos do mesmo cartão quadrado, segurado por uma mão que cobre um dos cantos. Frente: um ponto no centro, com a mão no canto superior esquerdo. Verso: dois pontos, nos cantos superior esquerdo e inferior direito, com a mão no canto superior direito. Frente: pontos no canto superior esquerdo e no centro, com a mão no canto inferior direito. Verso: pontos nos cantos superior esquerdo, superior direito e inferior direito, com a mão no canto inferior esquerdo.")),
     "alternativas": alts("4.", "5.", "6.", "7.", "8."),
     "explicacao": "<p>O truque usa a mão para esconder pontos. A frente precisa de, no mínimo, 2 pontos: o do centro e o de um canto, que a mão cobre na primeira vez. O verso precisa de, no mínimo, 3: na primeira vez a mão cobre um deles, e o público vê dois; depois, a mão cobre outro canto, e aparecem os três. Total mínimo: 2 + 3 = <strong>5</strong> pontos. Alternativa <strong>B</strong>.</p><p>Com 4 pontos, um dos lados não teria o número que o público chega a ver (A). E 6, 7 ou 8 pontos funcionam, mas não são o mínimo (C, D e E).</p>"},
50: {"materia": "Raciocínio lógico", "assunto": "Sequências", "tags": ["baralho", "ordem cíclica"],
     "enunciado": p(*T(21, "As profissões de mágico e de matemático podem", "ordem cíclica representada na figura."))
                  + apoio("A♣ · 4♥ · 7♠ · 10♦ · K♣ · 3♥ · 6♠ · 9♦ · Q♣ · 2♥ · 5♠ · 8♦ · J♣ · A♥ · 4♠ · 7♦ · 10♣ · K♥ · 3♠ · 6♦ · 9♣ · Q♥ · 2♠ · 5♦ ...")
                  + apoio("Cada carta possui um símbolo (número ou letra); e um naipe (♣; ♥; ♠; ♦).")
                  + p(*T(21, "Durante a apresentação, são convidados ao palco", "o terceiro espectador está segurando a carta",
                         ["O mágico então irá distribuir", "Ele pergunta ao primeiro espectador", "Para o segundo espectador", "Logo, o mágico pode deduzir"])),
     "trocar": [("tem um K.", "tem um <strong>K</strong>.")],
     "alternativas": alts("3♣.", "6♥.", "6♣.", "10♥.", "10♠."),
     "explicacao": "<p>Na ordem cíclica, cada carta vale 3 a mais que a anterior (A, 4, 7, 10, K, 3, ...: depois de K = 13 vem 13 + 3 − 13 = 3), e os naipes se repetem na ordem ♣, ♥, ♠, ♦. O corte não muda essa ordem. O primeiro espectador tem um K; o segundo, uma carta de ♦, que é o naipe seguinte ao do K, então o K é de ♠. As cartas são K♠, 3♦ e, para o terceiro, <strong>6♣</strong>. Alternativa <strong>C</strong>.</p><p>3♣ seria a carta seguinte a um K♦, mas aí o segundo seria de ♣ (A). 6♥, 10♥ e 10♠ não seguem K e uma carta de ♦ na sequência (B, D e E).</p>"},
51: {"materia": "História", "assunto": "Pré-História", "tags": ["Revolução Neolítica"],
     "enunciado": apoio(*T(21, "Os estudos arqueológicos apontam que as primeiras", "aumento populacional em grande escala."))
                  + url("https://tinyurl.com/yc2tnd5p", "28.10.2022") + p("O processo descrito no texto é chamado de"),
     "alternativas": alts("Feudalismo ou Sistema Feudal.", "Êxodo Rural ou Fuga para as Cidades.", "Monocultura ou Sistema de Plantation.", "Revolução Neolítica ou Revolução Agrícola.", "Rotação trienal de culturas ou Agricultura Transgênica."),
     "explicacao": "<p>A passagem da caça e coleta nômade para a agricultura e o sedentarismo, há cerca de 10 mil a 12 mil anos, é a <strong>Revolução Neolítica</strong> (ou Revolução Agrícola). Alternativa <strong>D</strong>.</p><p>O feudalismo é medieval (A), o êxodo rural é a saída do campo para a cidade (B), a plantation é a monocultura colonial (C), e a rotação trienal (Idade Média) e os transgênicos (século XX) são muito posteriores (E).</p>"},
52: {"materia": "Química", "assunto": "Reações químicas", "tags": ["termoquímica", "Lei de Hess"],
     "enunciado": p("A variação de entalpia de uma reação química pode ser calculada pela Lei de Hess. Nessa lei a variação de entalpia da reação global corresponde à soma das variações de entalpia das reações sucessivas do processo.",
                    "A pirólise do metano é dada pela equação")
                  + "\\[\\text{CH}_4(g) \\rightarrow \\text{C}(s) + 2\\,\\text{H}_2(g) \\qquad \\Delta H = ?\\]"
                  + p("Para calcular a variação de entalpia da pirólise do metano, considere as reações sucessivas (I), (II) e (III) e seus respectivos valores de entalpia.",
                      "(I) CH<sub>4</sub>(g) + 2 O<sub>2</sub>(g) → CO<sub>2</sub>(g) + 2 H<sub>2</sub>O(ℓ) &nbsp; ∆H = –890 kJ/mol<br>(II) C(s) + O<sub>2</sub>(g) → CO<sub>2</sub>(g) &nbsp; ∆H = –393 kJ/mol<br>(III) H<sub>2</sub>(g) + ½ O<sub>2</sub>(g) → H<sub>2</sub>O(ℓ) &nbsp; ∆H = –286 kJ/mol",
                      "Assinale a alternativa que corresponde ao valor correto da entalpia da reação de pirólise do metano, em kJ/mol."),
     "alternativas": alts("–75", "+75", "–180", "+180", "+215"),
     "explicacao": "<p>Mantém-se (I) como está (–890 kJ), inverte-se (II) para formar C(s) (+393 kJ) e inverte-se (III) multiplicada por 2 para formar 2 H₂(g) (+572 kJ). Somando: CH₄ → C + 2 H₂, com ∆H = –890 + 393 + 572 = <strong>+75 kJ/mol</strong>. Alternativa <strong>B</strong>.</p><p>–75 vem de esquecer de trocar algum sinal (A). E –180, +180 e +215 vêm de não multiplicar (III) por 2 ou de errar os sinais (C, D e E).</p>"},
53: {"materia": "Português", "assunto": "Interpretação de texto",
     "enunciado": QUERINO + P53,
     "alternativas": alts("as etnias africanas aprimoraram, no Brasil, as técnicas rudimentares de produção agrícola por entrarem em contato com novas tecnologias.",
                          "os africanos trouxeram, para além das contribuições linguísticas e religiosas, técnicas de produção importantes para o desenvolvimento econômico nacional.",
                          "a técnica da bateia, desenvolvida no Brasil por africanos, foi responsável por uma revolução na forma de exploração das minas de pedras preciosas.",
                          "houve, durante o século XIX, a incorporação do instrumento alemão de fundição, chamado cadinho, às siderúrgicas nacionais, possível apenas pelo uso da mão de obra escravizada.",
                          "havia, na produção da cana-de-açúcar, um plano de carreira seguido pelos trabalhadores de origem africana: começavam no corte do produto e seguiam até à função de mestre-de-açúcar."),
     "explicacao": "<p>O texto mostra que os africanos escravizados trouxeram tecnologias: pecuária e agricultura complexa, o ofício de mestre-de-açúcar, a bateia na mineração e o cadinho na siderurgia. Alternativa <strong>B</strong>.</p><p>Eles já vinham de sociedades com técnicas complexas, não rudimentares (A). A bateia foi trazida da África, e era usada para o ouro (C). O cadinho é africano, e o alemão só o adaptou (D). E muitos africanos já chegavam e eram postos como mestres-de-açúcar, sem um plano de carreira (E).</p>"},
54: {"materia": "Português", "assunto": "Gêneros textuais", "tags": ["oralidade", "podcast"],
     "enunciado": p("O texto apresentado, levando em conta seu canal de divulgação e seu gênero, caracteriza-se pelo uso de"), "apoio_de": (53, P53),
     "alternativas": alts("períodos longos, formados por orações subordinadas, características do editorial de empresas jornalísticas.", "termos técnicos típicos da linguagem radiofônica, uma vez que se trata de uma notícia sobre achados arqueológicos.",
                          "vocabulário acessível, com algumas repetições típicas de oralidade, por se tratar de um texto informativo falado, como, por exemplo, um <em>podcast</em>.",
                          "vocabulário infantil, marcado pelas repetições, pelos diminutivos e pelos termos de cunho afetivo, porque é um relato pessoal.", "linguagem rebuscada, com predomínio de figuras de linguagem e inversões sintáticas, pois se trata de uma crônica literária."),
     "explicacao": "<p>O texto é a transcrição de um episódio de <em>podcast</em> (Projeto Querino) e tem marcas da fala: “pro Brasil”, “tá marcado”, “lá no século XVI”, “Tem um alemão, o Barão...”, “fez lá uma pequena adaptação”. O vocabulário é acessível, e o objetivo é informar. Alternativa <strong>C</strong>.</p><p>Os períodos são curtos, e não é um editorial (A). Não há termos técnicos de rádio, e o tema não são achados arqueológicos (B). Não há vocabulário infantil nem relato pessoal (D). E a linguagem não é rebuscada nem literária (E).</p>"},
}
completar(Q, R)
