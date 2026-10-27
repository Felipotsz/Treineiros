# Ajustes da conferência humana: Vestibular FATEC 2º semestre de 2025 (exame de 29/06/2025)
# Texto conferido com a imagem de cada página. Tema implícito: economia verde e sustentabilidade.
# 64 questões (esta edição tem 64, não 60); a prova tem 5 h no total, incluindo a redação.
# Matéria: a do gabarito oficial; nas "Multidisciplinar", a matéria principal + tag "multidisciplinar".
# Letras de canção (Q28-30 e Q46-49) como imagem; o alt descreve sem transcrever.
# Gabarito: oficial (2SEM25), sem anuladas; Q61-64 acrescentadas à mão (o leitor cortava em 60). Conferido nas 64.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import A, carregar, enun, tabela, colunas, completar, trecho

ID = "fatec-2025-2sem"
META = {
    "id": ID,
    "banca": "FATEC",
    "ano": 2025,
    "semestre": 2,
    "titulo": "Vestibular FATEC, 2º semestre de 2025",
    "fonte": "Centro Paula Souza",
    "dataExame": "2025-06-29",
    "duracaoMinutos": 300,
    "tema": "Economia verde",
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


def sem_inicio(h, ate):
    """Tira do enunciado do rascunho tudo até o fim do parágrafo que contém 'ate' (textos compartilhados)."""
    i = h.find(ate)
    if i < 0: raise ValueError(f"não encontrado: {ate[:40]!r}")
    return h[h.find("</p>", i) + 4:]


# ---------- textos compartilhados ----------
P1 = p("Ao se compararem os textos, pode-se concluir corretamente que")
BASE1 = enun(R, 2)[:enun(R, 2).find("<p>Assinale a alternativa que analisa")]
BASE1 = BASE1.replace("<p><strong>Leia os textos para responder às questões de 01 a 03.</strong></p>", chamada("Leia os textos para responder às questões de 01 a 03."))

ADUBO = enun(R, 6)[:enun(R, 6).find("<p>Com base no texto, é correto afirmar que</p>")]
ADUBO = ADUBO.replace("<p><strong>Leia o texto para responder às questões 06 e 07.</strong></p>", chamada("Leia o texto para responder às questões 06 e 07."))
P6 = p("Com base no texto, é correto afirmar que")

IA = (chamada("Leia o texto para responder às questões 16 e 17.")
      + apoio("ARTIFICAL INTELLIGENCE", "<strong>AI’s carbon footprint is bigger than you think</strong>",
              "Generating one image takes as much energy as fully charging your smartphone.", "By Melissa Heikkilä — December 5, 2023")
      + url("https://tinyurl.com/4es9fs6a", "04.10.2024", ""))
P16 = p("O texto apresenta")

SEMENTES = (chamada("Leia o texto para responder às questões de 28 a 30.")
            + p("A canção <em>Sementes</em>, composta por Drik Barbosa, Emicida, Nave e Thiago Jamelão, propõe sensibilizar, conscientizar e mudar o cenário do trabalho infantil por meio da poesia. Acompanhe um trecho.")
            + "[[fig:1]]")
SEMENTES_IMG = figs(("q28", "Trecho da canção “Sementes”, em 13 versos numerados (01, 05 e 10 marcados na margem). A letra compara a criança a uma semente e a uma flor, que não se desenvolvem sob pressão nem sem água, sol e tempo, e afirma que é triste e covarde cortar a infância ao meio e que criança não tem trabalho. Em negrito: “Se” (verso 01), “Que” (verso 04), “Como” (verso 05), “se” (verso 07) e “Pra” (verso 11)."))
P28 = p("Utilizando os 3 primeiros versos da canção, é possível criar as sequências de letras:", "• S, T, M, M, T.", "• N, D, S, N, V.", "• M, S, M, C, S.",
        "Essas sequências possuem uma determinada lógica de formação.", "Caso a mesma lógica fosse aplicada ao quarto verso da canção, a sequência correspondente seria")

PEGADA = (chamada("Leia o texto para responder às questões 32 e 33.")
          + apoio(*[x.replace("(CO2eq)", "(CO<sub>2</sub>eq)") for x in T(12, "A pegada de carbono mede", "diferentes tipos de produtos.", ["O gráfico mostra"])])
          + "[[fig:1]]" + fonte("&lt;https://tinyurl.com/2jr6sztz&gt;. Acesso em: 13.11.2024."))
PEGADA_IMG = figs(("q32", "Gráfico de barras horizontais: pegada de carbono, em kg de CO₂eq por quilograma de alimento. Carne bovina 99,5; chocolate amargo 46,6; carne de cordeiro 39,7; café 28,5; camarão de criadouro 26,9; queijo 23,9; peixe de criadouro 13,6; carne suína 12,3; carne avina 9,9; ovo 4,7."))
P32 = p("Em relação aos alimentos referidos no gráfico, assinale a alternativa correta.")

HIDROGENIO = (chamada("Leia o texto e o esboço da Tabela Periódica para responder às questões 40 e 41.")
              + apoio(*[x.replace("(H2O)", "(H<sub>2</sub>O)") for x in T(15, "O hidrogênio verde, uma fonte", "patente do novo produto.", ["Nesse processo, são", "Uma equipe de cientistas"])])
              + url("https://tinyurl.com/d3s36det", "03.10.2024") + "[[fig:1]]")
HIDROGENIO_IMG = figs(("q40", "Esboço da Tabela Periódica, só com os símbolos dos elementos, em 7 períodos (linhas) e 18 grupos (colunas), mais as duas linhas de lantanídeos e actinídeos embaixo. No 6º período, lado a lado: Cs, Ba, La, Hf, Ta, W, Re, Os, Ir, Pt, Au, Hg, Tl, Pb, Bi, Po, At, Rn."))
P40 = p("Considerando os elementos raros e caros usados como catalisadores no processo de obtenção do hidrogênio verde, mencionados no texto, e as suas posições na Tabela Periódica, podemos concluir corretamente que esses elementos são")

JOGOS = (chamada("Leia o texto para responder às questões 44 e 45.")
         + p("O Green Game Jam é um evento que desafia estúdios de jogos a incorporarem temas ambientais em seus títulos. Em 2024, os organizadores propuseram reunir os jogadores para agir no mundo real.",
             "Suponha que, como parte dessas ações que reuniram os jogadores, houve um campeonato. O quadro a seguir reúne os resultados de algumas partidas disputadas entre 5 competidores que se enfrentaram uma única vez. Cada letra no interior do quadro indica um resultado possível:",
             "• <em>E</em> indica um empate entre os jogadores;", "• <em>V</em> indica a vitória do jogador da linha em questão; e", "• <em>D</em> indica a derrota do jogador da linha correspondente.")
         + tabela(["", "Alice", "Bruno", "Carla", "Diego", "Elias"],
                  [["<strong>Alice</strong>", "—", "<em>D</em>", "<em>E</em>", "<em>V</em>", "<em>E</em>"],
                   ["<strong>Bruno</strong>", "<em>V</em>", "—", "<em>D</em>", "<em>V</em>", "<em>V</em>"],
                   ["<strong>Carla</strong>", "<em>E</em>", "<em>V</em>", "—", "<em>D</em>", "<em>V</em>"],
                   ["<strong>Diego</strong>", "<em>D</em>", "<em>D</em>", "<em>V</em>", "—", "<em>E</em>"],
                   ["<strong>Elias</strong>", "<em>E</em>", "<em>D</em>", "<em>D</em>", "<em>E</em>", "—"]]))
P44 = p("As informações descritas no quadro permitem concluir corretamente que")

BABACU = (chamada("Leia o texto para responder às questões de 46 a 49.") + "[[fig:1]]")
BABACU_IMG = figs(("q46", "Trecho de canção, em nove versos, de “O (En)canto das Quebradeiras de Coco Babaçu no Maranhão” (SILVA e SILVA, UFMA; &lt;https://tinyurl.com/3r6j99a9&gt;, acesso em 17.10.2024). Os versos exaltam as palmeiras de babaçu, a terra fértil e a natureza que dá o fruto; chamam as “senhoras guerreiras” à luta para custear a alimentação, falam do produto que chega a outras nações como exportação e terminam com a alegria do eu lírico ao ver a matéria-prima circulando no país."))
P46 = p("De acordo com o texto, é correto afirmar que")

CRISE = (chamada("Leia o texto para responder às questões 50 e 51.") + "[[fig:1]]"
         + url("https://tinyurl.com/3apz9yr8", "04.10.2024", "Original colorido."))
CRISE_IMG = figs(("q50", "Desenho: numa parede, a placa “Crise climática”. Abaixo, duas placas de direção: “Prevenidos – sala 1”, com seta para a esquerda, e “Despreparados – salas 2 a 100”, com seta para a direita. Uma pessoa pequena, sozinha, olha para as placas."))
P50 = p("Sobre o texto, é correto afirmar que se trata de")

FRUTAS = (chamada("Leia o texto para responder às questões 56 e 57.") + "[[fig:1]]"
          + url("https://tinyurl.com/2m2buenx", "30.09.2024", ""))
FRUTAS_IMG = figs(("q56", "Cartaz em inglês “How far did your fruit commute?”: as food miles de uma salada de frutas vendida num supermercado do Reino Unido, da fazenda até o supermercado. Maçãs, 11 690 milhas, da Nova Zelândia; bananas, 5 424, da Costa Rica; cana-de-açúcar, 4 683, da Jamaica; morangos, 3 666, dos EUA; abacaxis, 3 176, de Gana; uvas, 2 181, do Egito; laranjas, 1 254, do Marrocos; total da salada: 43 345 milhas. “95% fruit, 50% vegetables eaten in the UK are imported.” Um parágrafo explica que food miles são a distância que um alimento percorre do ponto de origem até a mesa e que isso afeta o ambiente pelo carbono liberado no transporte. No pé: “Buy local &amp; buy in season”."))
P56 = p("De acordo com o texto, é correto afirmar que a expressão <em>food miles</em> pode ser entendida como")

Q = {
1: {"materia": "Português", "assunto": "Interpretação de texto", "tags": ["economia verde", "comparação de textos"],
    "enunciado": BASE1 + P1,
    "alternativas": {"A": "o conceito expresso no texto I não se encaixa no exemplo expresso no texto II, pois este ilustra a exploração de bens não renováveis.",
                     "B": "o conceito expresso no texto II não se encaixa no texto I, uma vez que a economia verde visa ao lucro sem se preocupar com aspectos sociais.",
                     "C": "o conceito expresso no texto I vai ao encontro do exemplo dado no texto II, já que este enquadra-se nos princípios de respeito ao meio ambiente.",
                     "D": "os exemplos apresentados nos textos I e II se opõem ao ilustrarem, respectivamente, o controle dos meios de produção e a equidade de gênero.",
                     "E": "o exemplo dado no texto II ilustra uma atividade extrativista que, apesar de recente e igualitária, contrapõe-se aos princípios expostos no texto I."},
    "explicacao": "<p>O extrativismo do babaçu gera renda, fortalece um povo tradicional e preserva a região dos babaçuais: é um exemplo de bem-estar, inclusão e respeito ao meio ambiente, como na economia verde do texto I. Alternativa <strong>C</strong>.</p><p>O coco babaçu é renovável (A). O texto I fala justamente em inclusão social, não em lucro a qualquer custo (B). Os textos não se opõem (D e E), e a atividade das quebradeiras é histórica, não recente (E).</p>"},
2: {"materia": "Português", "assunto": "Classes de palavras", "tags": ["conjunções", "pronome relativo"],
    "enunciado": BASE1 + p("Assinale a alternativa que analisa corretamente os termos em negrito nos textos."),
    "explicacao": "<p>“Portanto” é conjunção conclusiva, com o mesmo valor de “então” e “logo”. Alternativa <strong>E</strong>.</p><p>“Significativamente” é advérbio, não substantivo, e intensifica o verbo “reduzir” (A). Em “princípios-chave”, “chave” funciona como substantivo que qualifica e fica invariável, então o plural está correto (B). “Mesma” retoma “qualidade de vida”, não “equidade” (C). E o antecedente de “que” é “mulheres”, pois são elas que exercem a atividade (D).</p>"},
3: {"materia": "Português", "assunto": "Coesão e referência", "tags": ["pronomes"],
    "enunciado": BASE1 + p("O pronome presente em “restaurá-la” (texto I) retoma"),
    "explicacao": "<p>Em “a economia deve salvaguardar a natureza, restaurá-la e investir nela”, o pronome “la” retoma <strong>“a natureza”</strong>: é ela que deve ser restaurada. Alternativa <strong>E</strong>.</p><p>Os outros termos aparecem antes no texto, mas não completam o sentido de “restaurar” nessa frase (A, B, C e D).</p>"},
4: {"materia": "História", "assunto": "História contemporânea", "tags": MULTI + ["contraexemplo", "meio ambiente"],
    "enunciado": enun(R, 4, trocas=[("Registraram‹HIFEN›se", "Registraram-se")]),
    "alternativas": {"B": "O Império Romano cujo colapso de sua sociedade foi decorrente de uma combinação de crises econômicas, militares, políticas e sociais, dentre elas epidemias que reduziram significativamente a população, o que afetou, por exemplo, a produção agrícola.",
                     "C": "A União Soviética, durante a corrida armamentista e a industrialização pesada no século XX, priorizou o desenvolvimento econômico e militar, o que levou à degradação ambiental severa, como o desastre de Chernobyl e a destruição do Mar de Aral."},
    "explicacao": "<p>O trecho de Rachel Carson conta que o próprio povo destruiu o equilíbrio com o ambiente. Um contraexemplo é um caso em que a sociedade convive com a natureza sem degradá-la: os <strong>terraços agrícolas dos Incas</strong> produziam alimentos sem destruir o ambiente. Alternativa <strong>D</strong>.</p><p>A Alemanha nazista, a União Soviética e a Revolução Industrial são exemplos de ação humana que degradou o ambiente, ou seja, confirmam o trecho (A, C e E). E a queda de Roma não trata da relação com o ambiente (B).</p>"},
5: {"materia": "História", "assunto": "História contemporânea", "tags": ["Revolução Verde", "agropecuária"],
    "explicacao": "<p>A Revolução Verde trouxe sementes melhoradas, máquinas, adubos químicos e agrotóxicos para aumentar a produção, muitas vezes com prejuízo ao meio ambiente e à saúde. Alternativa <strong>D</strong>.</p><p>As alternativas A, B e C descrevem a agricultura tradicional, de pouca tecnologia. E descreve práticas agroecológicas, o oposto do modelo da Revolução Verde.</p>"},
6: {"materia": "Biologia", "assunto": "Botânica", "tags": ["adubação verde", "ciclo do nitrogênio"],
    "enunciado": ADUBO + P6,
    "explicacao": "<p>O texto diz que a adubação verde aumenta a fixação do nitrogênio, deixa o solo mais fértil e permite reduzir pesticidas e fertilizantes, o que <strong>diminui a poluição</strong>. Alternativa <strong>D</strong>.</p><p>Quem fixa o nitrogênio são as bactérias, não os restos de plantas (A). A adubação verde aumenta a FBN e é favorável ao ambiente (B). O texto fala de inoculantes biológicos, não sintéticos (C). E agrotóxicos não fazem a fixação do nitrogênio (E).</p>"},
7: {"materia": "Biologia", "assunto": "Ecologia", "tags": ["ciclo do nitrogênio", "mutualismo"],
    "enunciado": ADUBO + p("Na FBN, a participação das bactérias do gênero mencionado no texto é importante porque esses micro-organismos"),
    "explicacao": "<p>As bactérias <em>Rhizobium</em>, nos nódulos das raízes, transformam o N₂ do ar em compostos nitrogenados que a planta usa. Em troca, recebem da planta a matéria orgânica da fotossíntese. É uma relação de mutualismo. Alternativa <strong>E</strong>.</p><p>Elas não são decompositoras (A), não transformam nitratos em carboidratos (B), não corrigem a acidez do solo (C) e não reduzem a absorção de minerais (D).</p>"},
8: {"materia": "Geografia", "assunto": "Fontes de energia", "tags": ["bioeconomia", "Proálcool"],
    "explicacao": "<p>O <strong>Proálcool</strong>, de 1975, incentivou o etanol da cana-de-açúcar como combustível para enfrentar a crise do petróleo: um recurso biológico no lugar de um fóssil. Alternativa <strong>C</strong>.</p><p>O ICMBio é de 2007 e o Ibama, de 1989, e nenhum dos dois é um modelo de produção (A e B). A Petrobras (1953) e a CSN (1941) são de outras décadas e lidam com petróleo e aço, recursos não renováveis (D e E).</p>"},
9: {"materia": "Química", "assunto": "Reações químicas", "tags": ["equação química"],
    "alternativas": {"C": "CO<sub>2</sub>(g) + H<sub>2</sub>O(ℓ) + C<sub>17</sub>H<sub>35</sub>COONa(aq) → C<sub>17</sub>H<sub>35</sub>COOH(aq) + NaHCO<sub>3</sub>(aq)",
                     "A": "CO<sub>3</sub>(g) + H<sub>2</sub>O(ℓ) + C<sub>17</sub>H<sub>35</sub>COONa(aq) → NaHCO<sub>3</sub>(aq) + C<sub>17</sub>H<sub>35</sub>COOH(aq)",
                     "B": "CO(g) + H<sub>2</sub>O(ℓ) + C<sub>17</sub>H<sub>35</sub>COONa(aq) → C<sub>17</sub>H<sub>35</sub>COOH(aq) + NaHCO<sub>3</sub>(aq)",
                     "E": "CO<sub>2</sub>(g) + C<sub>17</sub>H<sub>35</sub>COONa(aq) + H<sub>2</sub>O(ℓ) + C<sub>17</sub>H<sub>35</sub>COOH(aq) → NaHCO<sub>3</sub>(aq)"},
    "explicacao": "<p>Os reagentes são o gás carbônico (CO₂), a água e o estearato de sódio; os produtos, o ácido esteárico e o bicarbonato de sódio. Alternativa <strong>C</strong>, que ainda está balanceada.</p><p>Gás carbônico é CO₂, não CO₃ nem CO (A e B). D esquece a água e o bicarbonato. E põe o ácido esteárico, que é produto, entre os reagentes.</p>"},
10: {"materia": "Química", "assunto": "Estrutura atômica", "tags": MULTI + ["mol", "constante de Avogadro"],
     "enunciado": p("A moda sustentável busca reduzir o impacto ambiental da indústria, promovendo o uso consciente de materiais e recursos. Visando alcançar esse objetivo, a tecnologia de materiais das áreas de construção civil e têxtil possibilitou o desenvolvimento de uma camiseta inovadora, capaz de absorver o CO<sub>2</sub> do ar. A imagem retrata a quantidade de gás carbônico removida do ar, em um dia, por uma camiseta e por uma árvore adulta.", classe="apoio")
                  + "[[fig:1]]" + url("https://tinyurl.com/2w7ft535", "03.10.2024")
                  + p("De acordo com os dados apresentados, podemos concluir corretamente que X camisetas capturam, em um dia, a mesma quantidade de gás carbônico que uma árvore adulta captura diariamente.",
                      "<strong>Dados:</strong> massa molar do CO<sub>2</sub> = 44 g/mol e constante de Avogadro = 6 × 10<sup>23</sup> /mol",
                      "Assinale a alternativa que contém o valor correto de X."),
     "imagens": figs(("q10", "Duas nuvens com setas para baixo. A primeira, “22 g de CO₂”, aponta para uma camiseta. A segunda, “75 × 10²³ moléculas de CO₂”, aponta para uma árvore.")),
     "explicacao": "<p>A árvore captura 75 × 10²³ ÷ 6 × 10²³ = 12,5 mol de CO₂, ou seja, 12,5 · 44 = 550 g. Cada camiseta captura 22 g, então X = 550 ÷ 22 = <strong>25</strong>. Alternativa <strong>E</strong>.</p><p>Outro caminho: 22 g são 0,5 mol, e 12,5 ÷ 0,5 = 25. Esquecer de converter tudo para a mesma unidade leva aos outros valores.</p>"},
11: {"materia": "História", "assunto": "Idade Média", "tags": ["rotação trienal", "agricultura"],
     "explicacao": "<p>Na rotação trienal, a terra era dividida em três partes: uma recebia um cultivo, outra um cultivo diferente e a terceira ficava em pousio, revezando a cada ano. O solo descansava e <strong>recuperava a fertilidade</strong>, e a produção aumentou. Alternativa <strong>A</strong>.</p><p>O sistema alterava a vegetação original, que era derrubada para o cultivo (B). As alternativas C, D e E descrevem a agricultura moderna, com logística global, motores e monocultura com químicos.</p>"},
12: {"materia": "Química", "assunto": "Química ambiental", "tags": MULTI + ["biogás", "fontes de energia"],
     "explicacao": "<p>O biogás, rico em metano, vem da <strong>decomposição de matéria orgânica</strong> (restos vegetais, esterco, lixo, esgoto) por bactérias, sem oxigênio. Alternativa <strong>A</strong>.</p><p>O CO₂ não contém metano (B). Rochas e materiais inorgânicos não geram biogás (C). O nióbio é um metal conhecido desde o século XIX (D). E a eletrólise da água produz hidrogênio e oxigênio (E).</p>"},
13: {"materia": "Química", "assunto": "Reações químicas", "tags": ["combustão", "estequiometria"],
     "enunciado": p("A gasolina é uma mistura de hidrocarbonetos, dentre eles, o octano (C<sub>8</sub>H<sub>18</sub>).", "Nos motores, a combustão completa do octano produz gás carbônico e água, conforme a equação",
                    "\\[\\begin{aligned}&\\text{C}_8\\text{H}_{18}(\\text{g}) + \\tfrac{25}{2}\\,\\text{O}_2(\\text{g}) \\\\ &\\rightarrow 8\\,\\text{CO}_2(\\text{g}) + 9\\,\\text{H}_2\\text{O}(\\ell)\\end{aligned}\\]",
                    "\\(\\Delta_r H^0 = -5\\,471{,}0\\) kJ/mol",
                    "Outro combustível que pode ser usado é o metano (CH<sub>4</sub>), um dos componentes do biogás. A combustão completa do metano produz gás carbônico e água, conforme a equação",
                    "\\[\\text{CH}_4(\\text{g}) + 2\\,\\text{O}_2(\\text{g}) \\rightarrow \\text{CO}_2(\\text{g}) + 2\\,\\text{H}_2\\text{O}(\\ell) \\]",
                    "\\(\\Delta_r H^0 = -890{,}0\\) kJ/mol",
                    "Considerando as informações apresentadas nessas equações, podemos concluir que o uso do metano como combustível, em vez do octano, apresenta menor impacto ambiental, pois a queima"),
     "explicacao": "<p>A queima de 1 mol de metano libera 1 mol de CO₂; a de 1 mol de octano, 8 mol. Como o CO₂ é um gás de efeito estufa, o metano tem menor impacto. Alternativa <strong>D</strong>.</p><p>As duas queimas consomem oxigênio, não produzem (A). As duas liberam energia, pois ΔH é negativo (B). Não há liberação de hidrogênio (C). E a menor quantidade de água não é o que reduz o impacto (E).</p>"},
14: {"materia": "Matemática", "assunto": "Funções", "tags": ["função do 2º grau"],
     "enunciado": p("O uso de fontes renováveis de energia, como a energia eólica, cresceu nos últimos anos devido às crescentes demandas relacionadas ao desenvolvimento sustentável.",
                    "Em uma determinada região, suponha que a potência gerada por um modelo de aerogerador possa ser modelada (ou aproximada) pela função P(v) = –5v<sup>2</sup> + 160v – 470, em que P(v) representa a potência gerada em kW e v corresponde à velocidade do vento em m/s, sendo 4 ≤ v ≤ 16.",
                    "Assinale a alternativa que indica a velocidade do vento, em m/s, necessária para que a potência gerada pelo aerogerador seja igual a 630 kW."),
     "explicacao": "<p>–5v² + 160v – 470 = 630 dá –5v² + 160v – 1 100 = 0, ou v² – 32v + 220 = 0. As raízes são v = 10 e v = 22. Como 4 ≤ v ≤ 16, fica <strong>v = 10 m/s</strong>. Alternativa <strong>C</strong>.</p><p>Conferindo: –5 · 100 + 1 600 – 470 = 630. Os outros valores não satisfazem a equação.</p>"},
15: {"materia": "Física", "assunto": "Energia", "tags": ["consumo de energia"],
     "enunciado": p("Ferramentas de Inteligência Artificial Generativas (IA Gen) têm se tornado um desafio para a economia verde, devido ao excessivo consumo de energia que esses recursos demandam.",
                    "Essas ferramentas chegam a ultrapassar o consumo anual médio de energia de uma cidade cujo consumo por habitante é de 50 kWh. Para se ter uma ideia, em um ano, uma das principais ferramentas de IA Gen teve um consumo médio de energia de, aproximadamente, 450 MWh. Dados: k = 10<sup>3</sup>; M = 10<sup>6</sup>",
                    "Considerando que as informações sobre os consumos da cidade e da ferramenta de IA Gen foram coletados simultaneamente, e tendo-os como referência, podemos afirmar corretamente que, se fosse uma cidade, o consumo de energia despendido por essa ferramenta teria condições de suprir uma população aproximada de pessoas igual a"),
     "explicacao": "<p>450 MWh = 450 000 kWh. Dividindo pelo consumo de cada habitante: 450 000 ÷ 50 = <strong>9 000 pessoas</strong>. Alternativa <strong>A</strong>.</p><p>Errar a conversão de MWh para kWh por um fator de 10 ou de 1 000 leva aos outros valores (C, D e E).</p>"},
16: {"materia": "Inglês", "assunto": "Vocabulário", "tags": ["graus de comparação"],
     "enunciado": IA + P16,
     "explicacao": "<p>“<em>Bigger than</em>” é um comparativo de superioridade (maior que), e “<em>as much energy as</em>” é um comparativo de igualdade (tanta energia quanto). Alternativa <strong>A</strong>.</p><p>Não há comparativo de inferioridade, que seria “<em>less ... than</em>” (B e D), nem superlativo, que seria “<em>the biggest</em>” (C, D e E).</p>"},
17: {"materia": "Física", "assunto": "Eletricidade", "tags": MULTI + ["energia elétrica"],
     "enunciado": IA + p("Para o carregamento da bateria de um celular, considere os seguintes dados:", "• o valor médio da carga completa da bateria é de 3 000 mAh; e", "• o potencial elétrico de operação é 5,0 V.",
                         "Com base nesses dados e na informação contida no texto, podemos afirmar corretamente que uma imagem gerada por IA Gen consome, aproximadamente, energia equivalente, em Wh, a"),
     "alternativas": {"A": "0,000 000 15.", "B": "0,000 15.", "C": "15.", "D": "15 000.", "E": "15 000 000."},
     "explicacao": "<p>O texto diz que gerar uma imagem gasta o mesmo que carregar o celular por completo. A energia da carga é E = carga × tensão = 3 Ah × 5 V = <strong>15 Wh</strong>. Alternativa <strong>C</strong>.</p><p>Usar 3 000 mAh sem converter para Ah dá 15 000 (D). As outras erram a conversão de unidades.</p>"},
18: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": ["saneamento básico", "esquistossomose"],
     "explicacao": "<p>A esquistossomose é causada por um verme (o esquistossomo), cujas larvas se desenvolvem em <strong>caramujos de água doce</strong> e depois penetram na pele de quem entra na água contaminada. Alternativa <strong>D</strong>.</p><p>A cólera é causada por bactéria e não é transmitida por insetos (A). A leptospirose é causada por bactéria, transmitida pela urina de ratos (B e C); o barbeiro transmite a doença de Chagas (B). E telas contra insetos não previnem a esquistossomose (E).</p>"},
19: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["economia circular"],
     "explicacao": "<p>A economia circular quer <strong>eliminar o desperdício</strong>: em vez de extrair, usar e descartar, ela reutiliza, recicla e regenera recursos. Alternativa <strong>C</strong>.</p><p>Ela busca reduzir, e não potencializar, os impactos negativos (A). Solar, eólica e biomassa são renováveis, e o objetivo é diminuir a dependência dos fósseis (B). Não trata de punição criminal nem de religião (D). E não busca aumentar consumo e emissões (E).</p>"},
20: {"materia": "Raciocínio lógico", "assunto": "Lógica", "tags": MULTI + ["conjuntos", "diagrama de Venn"],
     "enunciado": "[[fig:1]]" + p("De acordo com o Diagrama de Euler-Venn apresentado, pode-se afirmar corretamente que a economia"),
     "imagens": figs(("q20", "Diagrama de Euler-Venn dentro de um retângulo “Green Economy”. Três círculos que se cruzam: A (em cima), B (embaixo à esquerda) e C (embaixo à direita). O círculo D fica dentro de A, na região em que A, B e C se cruzam. Legenda: A → Bioeconomy; B → Low Carbon Economy; C → Circular Economy; D → Bio-based Economy; A ∩ B ∩ C ∩ D → Sustainable Economy.")),
     "explicacao": "<p>Pela legenda, a economia sustentável é A ∩ B ∩ C ∩ D, ou seja, resulta da intersecção da bioeconomia, da economia de baixo carbono, da circular e da de base biológica. Alternativa <strong>E</strong>.</p><p>A economia circular cruza a bioeconomia e está dentro da economia verde (A). D está contida em A, e não o contrário (B). B não é a intersecção dos outros (C). E a economia sustentável está contida na bioeconomia (D).</p>"},
21: {"materia": "Raciocínio lógico", "assunto": "Lógica", "tags": ["associação lógica"],
     "enunciado": p("A economia verde depende de profissionais voltados para o desenvolvimento sustentável. Entre as possíveis áreas de atuação, pode-se citar",
                    "• <strong>gestão ambiental</strong>, que trabalha na redução de impactos ambientais;", "• <strong>biocombustíveis</strong>, que desenvolve combustíveis a partir de matéria orgânica de origem vegetal ou animal;",
                    "• <strong>produção agropecuária</strong>, que pode promover práticas agropecuárias ecológicas; e", "• <strong>meio ambiente e recursos hídricos</strong>, que asseguram o uso eficiente dos recursos naturais, principalmente água.",
                    "Quatro estudantes, Rose, Caio, Rita e Carlos, estão decididos a atuar em apenas uma dentre as áreas mencionadas. Sabe-se que:",
                    "• cada área será escolhida por apenas um dos estudantes;", "• Rose não quer trabalhar com a redução de impactos ambientais;",
                    "• Caio e Carlos não querem trabalhar com o uso eficiente de recursos naturais; e", "• Rita quer trabalhar com o desenvolvimento de biocombustíveis.",
                    "Assinale a alternativa que é a única associação correta possível entre área escolhida e o estudante a partir das informações apresentadas."),
     "alternativas": colunas(["Rose", "Carlos", "Caio"], [
         ["tecnólogo em biocombustíveis", "tecnólogo em meio ambiente e recursos hídricos", "tecnólogo em gestão ambiental"],
         ["tecnólogo em gestão ambiental", "tecnólogo em meio ambiente e recursos hídricos", "tecnólogo em produção agropecuária"],
         ["tecnólogo em meio ambiente e recursos hídricos", "tecnólogo em produção agropecuária", "tecnólogo em gestão ambiental"],
         ["tecnólogo em biocombustíveis", "tecnólogo em produção agropecuária", "tecnólogo em meio ambiente e recursos hídricos"],
         ["tecnólogo em produção agropecuária", "tecnólogo em gestão ambiental", "tecnólogo em biocombustíveis"]]),
     "explicacao": "<p>Rita fica com biocombustíveis. Caio e Carlos não querem meio ambiente e recursos hídricos, e Rose não quer gestão ambiental; então meio ambiente e recursos hídricos fica com <strong>Rose</strong>. Caio e Carlos dividem gestão ambiental e produção agropecuária. Das alternativas, só a <strong>C</strong> respeita tudo isso. Alternativa <strong>C</strong>.</p><p>A, D e E dão biocombustíveis a quem não é Rita. B põe Rose em gestão ambiental, que ela não quer, e Carlos em meio ambiente.</p>"},
22: {"materia": "Geografia", "assunto": "Agropecuária e meio ambiente", "tags": MULTI + ["cana-de-açúcar"],
     "explicacao": "<p>Os resíduos da cana, como o bagaço e a vinhaça, podem ser usados para produzir <strong>biogás</strong> e energia, um aspecto positivo do cultivo. Alternativa <strong>E</strong>.</p><p>Contaminação da água por fertilizantes (A), perda de biodiversidade (B), poluição pela queima (C) e infestação de pragas (D) são aspectos negativos.</p>"},
23: {"materia": "História", "assunto": "Revolução Industrial", "tags": ["trabalho assalariado"],
     "explicacao": "<p>Artesãos que perdem os instrumentos de trabalho, viram assalariados e enfrentam longas jornadas, máquinas, ruído e poluição: é o retrato da <strong>Revolução Industrial</strong>. Alternativa <strong>C</strong>.</p><p>No feudalismo, os servos trabalhavam a terra do senhor, sem salário (A). A Revolução Francesa foi uma revolução política (B). Na Grécia e no Brasil colonial, o trabalho era em grande parte escravo, não assalariado (D e E).</p>"},
24: {"materia": "Geografia", "assunto": "Fontes de energia", "tags": ["biocombustíveis"],
     "explicacao": "<p>Um ponto negativo dos biocombustíveis é a expansão das plantações de matéria-prima sobre áreas de alimentos, o que pode <strong>encarecer os alimentos</strong>. Alternativa <strong>B</strong>.</p><p>As outras alternativas trazem aspectos positivos: menos emissões (A), empregos locais (C), menor dependência dos fósseis (D) e matéria-prima renovável (E).</p>"},
25: {"materia": "Física", "assunto": "Eletricidade", "tags": ["campo elétrico", "baterias"],
     "explicacao": "<p>A diferença de potencial entre os eletrodos cria um <strong>campo elétrico</strong>, e é ele que faz os íons de sódio se moverem pelo eletrólito. Alternativa <strong>D</strong>.</p><p>O potencial não “se movimenta”; o que se move são cargas (A). Os íons se inserem nos eletrodos durante a carga e a descarga (B). O efeito Doppler é das ondas e não tem relação com baterias (C). E quem cria a diferença de potencial são os eletrodos, não o eletrólito (E).</p>"},
26: {"materia": "História", "assunto": "História contemporânea", "tags": ["história ambiental"],
     "explicacao": "<p>O texto diz que a História Ambiental rejeita a ideia de que os humanos se desenvolveram sem restrições naturais e de que as consequências ecológicas do passado podem ser ignoradas. Ou seja, ela considera <strong>o meio ambiente um fator determinante</strong> e as consequências das ações passadas. Alternativa <strong>C</strong>.</p><p>As alternativas A, B, D e E repetem justamente as premissas que, segundo o texto, a História Ambiental rejeita.</p>"},
27: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": ["charge", "ironia"],
     "enunciado": p("Leia a charge.") + "[[fig:1]]" + url("https://tinyurl.com/mu4339k6", "01.10.2024", "") + p("O humor do texto provém de"),
     "imagens": figs(("q27", "Charge “The magic of marketing”, em preto e branco. Uma cidade poluída: arranha-céus, um avião, uma usina nuclear soltando fumaça, chaminés de um incinerador de lixo (“trash burner”), um congestionamento de carros e lixo espalhado na rua. Cada elemento traz o rótulo “green”: “green skyscrapers”, “green aircraft”, “green power”, “green waste disposal”, “green cars” e “green packaging”.")),
     "explicacao": "<p>As palavras “green” (verde, sustentável) aparecem coladas a aviões, usina, incinerador, carros e lixo, que na imagem poluem. O texto verbal diz o contrário do não verbal: é <strong>ironia</strong>, uma crítica ao marketing “verde”. Alternativa <strong>E</strong>.</p><p>Anacoluto é uma quebra na estrutura da frase (A). Catacrese é usar uma palavra fora do sentido original por falta de outra (B). A charge não ameniza a tragédia, ela a expõe (C). E não há máquinas com características humanas (D).</p>"},
28: {"materia": "Raciocínio lógico", "assunto": "Sequências", "tags": ["padrões"],
     "enunciado": SEMENTES + P28, "imagens": SEMENTES_IMG,
     "explicacao": "<p>Cada sequência é formada pelas <strong>cinco primeiras consoantes</strong> do verso, na ordem em que aparecem, pulando as vogais. No quarto verso, as cinco primeiras consoantes são Q, P, R, S, R (o “u” de “que” e o “é” são vogais). Alternativa <strong>A</strong>.</p><p>B conta o “u” como se fosse consoante. C, D e E trocam ou repetem letras.</p>"},
29: {"materia": "Raciocínio lógico", "assunto": "Sequências", "tags": ["códigos"],
     "enunciado": SEMENTES + p("Estudantes do curso de Ciências de Dados, durante uma aula, criaram um código para ocultar e proteger informações. Ao aplicá-lo à palavra SEMENTES, obtém-se a sequência:",
                               "<strong>18 – 04 – 12 – 04 – 13 – 19 – 04 – 18</strong>",
                               "Utilizando o mesmo código, assinale a alternativa na qual se apresenta o número do verso em que se encontra a palavra representada pela sequência:",
                               "<strong>00 – 03 – 20 – 11 – 19 – 14</strong>"),
     "imagens": SEMENTES_IMG,
     "explicacao": "<p>O código troca cada letra pela sua posição no alfabeto, começando do zero: A = 00, B = 01, ..., E = 04, M = 12, N = 13, S = 18, T = 19. Então 00 – 03 – 20 – 11 – 19 – 14 = A, D, U, L, T, O: “<strong>adulto</strong>”, que está no verso 11. Alternativa <strong>D</strong>.</p><p>Os outros números de verso não têm a palavra “adulto”.</p>"},
30: {"materia": "Português", "assunto": "Classes de palavras", "tags": ["preposição", "conjunções"],
     "enunciado": SEMENTES + p("Sobre os elementos em negrito na canção, é correto afirmar que"), "imagens": SEMENTES_IMG,
     "explicacao": "<p>No verso 11, “pra” é a forma reduzida da preposição “para” e indica finalidade, como “a fim de”. Alternativa <strong>E</strong>.</p><p>“Se”, no verso 01, é conjunção condicional, não integrante (A). “Que”, no verso 04, não retoma “coisa”: a frase completa a ideia anterior (B). “Como”, no verso 05, é comparativo, mas não equivale a “conforme” (C). E “se”, no verso 07, é parte do verbo pronominal “abrir-se”, que não pode ser retirada sem mudar o sentido (D).</p>"},
31: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": MULTI + ["captura de carbono"],
     "enunciado": apoio("<strong>What is carbon capture and storage?</strong>", enun(R, 31).split('<p class="apoio">')[1].split("</p>")[0])
                  + url("https://tinyurl.com/2zhm4hzr", "28.09.2024", "") + p("Segundo o texto, a tecnologia conhecida como CCS consiste em"),
     "explicacao": "<p>O texto diz que a CCS captura o CO₂ “at emission sources” (nos locais de emissão), transporta e armazena “in a suitable deep, underground location” (num local subterrâneo profundo). Alternativa <strong>B</strong>.</p><p>A tecnologia captura dióxido de carbono, não oxigênio (A). Não o purifica (C), não fala em monóxido de carbono (A e D) e não enterra as fontes de emissão no oceano (E).</p>"},
32: {"materia": "Biologia", "assunto": "Nutrição e saúde", "tags": MULTI + ["pegada de carbono", "nutrientes"],
     "enunciado": PEGADA + P32, "imagens": PEGADA_IMG,
     "explicacao": "<p>Dos 10 alimentos, 8 são fontes ricas em proteína: carne bovina, carne de cordeiro, camarão, queijo, peixe, carne suína, carne de ave e ovo. Mais da metade. Alternativa <strong>B</strong>.</p><p>Entre os cinco com maior pegada estão carnes e camarão, que não são ricos em carboidrato (A). Chocolate, queijo, carnes e ovo têm gordura: mais de um quarto dos alimentos é fonte de lipídios (C). Só o chocolate é rico em açúcar (D). E carnes e ovos não têm fibras (E).</p>"},
}

Q.update({
33: {"materia": "Matemática", "assunto": "Porcentagem", "tags": ["gráfico de setores"],
     "enunciado": p("O gráfico de setor apresenta a participação percentual de diferentes atividades humanas para a composição da pegada de carbono do chocolate amargo fornecida no gráfico de barras.", classe="apoio")
                  + "[[fig:2]]" + fonte("&lt;https://tinyurl.com/2jr6sztz&gt;. Acesso em: 13.11.2024.")
                  + p("Considerando que a emissão total de CO<sub>2</sub>eq para produzir 1 kg de chocolate amargo seja a soma de todas as categorias apresentadas, assinale a alternativa que indica, em kg, a massa aproximada de CO<sub>2</sub>eq proveniente do “desmatamento” ao longo da cadeia produtiva do chocolate amargo."),
     "apoio_de": (32, P32),
     "imagens": figs(("q33", "Gráfico de setores da pegada de carbono do chocolate amargo: desmatamento 55,4%; perdas 27,6%; cultivo 14,4%; outros 2,6%.")),
     "explicacao": "<p>O chocolate amargo emite 46,6 kg de CO₂eq por quilograma, e 55,4% disso vem do desmatamento: 0,554 · 46,6 ≈ <strong>25,8 kg</strong>. Alternativa <strong>A</strong>.</p><p>46,6 é o total do chocolate (B), 55,4 é a porcentagem (C), e 99,5 é a pegada da carne bovina (E).</p>"},
34: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": ["sustentabilidade"],
     "explicacao": "<p>O texto define <em>ecology</em> como as relações entre os seres vivos e o ambiente, <em>economy</em> como a gestão e o uso dos recursos, e <em>equity</em> como decisões baseadas em justiça. Alternativa <strong>D</strong>.</p><p>O texto não fala em decisões rápidas nem em empregos (A), em agentes estrangeiros (B), em triagem de trabalhadores ou livre comércio (C), nem em políticos e órgãos internacionais (E).</p>"},
35: {"materia": "Matemática", "assunto": "Probabilidade", "tags": ["porcentagem"],
     "explicacao": "<p>60% das empresas aderiram, e 20% dessas (100% − 80%) não atingiram a meta: 0,6 · 0,2 = 0,12 = <strong>12%</strong>. Alternativa <strong>A</strong>.</p><p>20% é a parcela das que aderiram, não do total do município (B). 48% são as que aderiram e atingiram a meta (D). E 40% são as que não aderiram (C).</p>"},
36: {"materia": "Matemática", "assunto": "Funções", "tags": ["função exponencial"],
     "enunciado": p("Estudos apontam que, no Brasil, o aumento do número de veículos elétricos emplacados tem ocorrido de forma exponencial.",
                    "Suponha que esse crescimento possa ser modelado, a partir de 2016, pela função \\(N(t) = 70 \\cdot 2^{(t-2016)}\\), em que N(t) é o número de veículos elétricos emplacados no ano t.",
                    "De acordo com o modelo apresentado, assinale a alternativa que indica corretamente a estimativa do número de veículos elétricos a serem emplacados no Brasil, no ano de 2025."),
     "explicacao": "<p>N(2025) = 70 · 2⁹ = 70 · 512 = <strong>35 840</strong>. Alternativa <strong>D</strong>.</p><p>Usar 2⁸ = 256 dá 17 920, perto de C. E 1 260 vem de multiplicar 70 por 18 (2 · 9) em vez de elevar 2 à 9ª potência (A).</p>"},
37: {"materia": "Raciocínio lógico", "assunto": "Lógica", "tags": ["conjuntos"],
     "enunciado": p("A escritora sul-coreana Han Kang, ganhadora do Prêmio Nobel de Literatura de 2024, em seu romance “<em>A Vegetariana</em>”, conta a história de Yeong-hye, uma mulher que para de consumir todos os alimentos que contêm carne.",
                    "Sejam", "• A: conjunto de todos os alimentos que Yeong-hye comia antes de se tornar vegetariana;", "• B: conjunto de todos os alimentos que Yeong-hye pode consumir após se tornar vegetariana; e", "• C: conjunto de todos os alimentos que contêm carne.",
                    "Supondo que a única mudança nos hábitos alimentares de Yeong-hye seja a descrita no texto, assinale a alternativa na qual a expressão representa corretamente o conjunto B."),
     "alternativas": {"A": "C ∪ A", "B": "C – A", "C": "A ∩ C", "D": "A<sup>C</sup>", "E": "A – C"},
     "explicacao": "<p>Depois de virar vegetariana, ela continua comendo o que comia antes, menos o que tem carne: B = A − C. Alternativa <strong>E</strong>.</p><p>A ∪ C acrescentaria carne (A). C − A seriam alimentos com carne que ela nunca comeu (B). A ∩ C são justamente os que ela deixou de comer (C). E o complementar de A seriam os alimentos que ela não comia (D).</p>"},
38: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["Amazônia"],
     "explicacao": "<p>Se manter a floresta em pé vale sete vezes mais do que explorá-la, desmatar significa <strong>destruir riqueza</strong>, além de biodiversidade. Alternativa <strong>E</strong>.</p><p>Desmatar não traz benefícios ambientais nem protege a fauna e a flora (A e B). Ampliar pastagens não preserva o ambiente (C). E o texto diz que a floresta em pé vale mais do que a soja (D).</p>"},
39: {"materia": "História", "assunto": "Brasil Império", "tags": ["café", "Oeste Paulista"],
     "explicacao": "<p>O café esgotou o solo do Vale do Paraíba, e o fim do tráfico de escravizados (1850) tornou a mão de obra escassa e cara. A produção migrou para o Oeste Paulista, de terras férteis, que passou a usar imigrantes. Alternativa <strong>A</strong>.</p><p>O êxodo rural é um fenômeno posterior e não explica a mudança (B). O cercamento aconteceu na Inglaterra (C). A Lei de Terras dificultou, e não facilitou, o acesso dos pobres à terra (D). E a abolição foi nacional, em 1888, e os imigrantes vieram da Europa (E).</p>"},
40: {"materia": "Química", "assunto": "Estrutura atômica", "tags": ["tabela periódica"],
     "enunciado": HIDROGENIO + P40, "imagens": HIDROGENIO_IMG,
     "explicacao": "<p>Platina (Pt) e irídio (Ir) são metais de transição e estão lado a lado na mesma linha da tabela, o <strong>6º período</strong>. Alternativa <strong>B</strong>.</p><p>Eles ficam em grupos diferentes (Ir no 9, Pt no 10) (A). Não são ametais (C e D) nem gases nobres (E).</p>"},
41: {"materia": "Química", "assunto": "Reações químicas", "tags": ["catalisadores", "reação endotérmica"],
     "enunciado": HIDROGENIO + p("Baseando-se na reação de eletrólise da água, com e sem catalisador, mencionada no texto, assinale a alternativa que contém o esboço gráfico correto da variação da energia envolvida nesse processo."),
     "imagens": HIDROGENIO_IMG + figs(
         ("q41a", "Gráfico A: energia em função do caminho da reação. Os produtos ficam acima dos reagentes. A curva com catalisador (tracejada) tem o pico mais alto que a curva sem catalisador (contínua)."),
         ("q41b", "Gráfico B: os produtos ficam acima dos reagentes. A curva com catalisador (tracejada) tem o pico mais baixo que a curva sem catalisador (contínua)."),
         ("q41c", "Gráfico C: os produtos ficam acima dos reagentes. A curva com catalisador (tracejada) sobe a um pico alto, e a curva sem catalisador (contínua) desce abaixo dos reagentes antes de subir aos produtos."),
         ("q41d", "Gráfico D: os produtos ficam abaixo dos reagentes. A curva com catalisador (tracejada) tem o pico mais alto que a curva sem catalisador (contínua)."),
         ("q41e", "Gráfico E: os produtos ficam abaixo dos reagentes. A curva com catalisador (tracejada) tem o pico mais baixo que a curva sem catalisador (contínua).")),
     "alternativas": {"A": "[[fig:2]]", "B": "[[fig:3]]", "C": "[[fig:4]]", "D": "[[fig:5]]", "E": "[[fig:6]]"},
     "explicacao": "<p>A eletrólise da água é endotérmica: os produtos (H₂ e O₂) ficam com mais energia que os reagentes, acima no gráfico. E o catalisador diminui a energia de ativação, então a curva com catalisador tem o pico mais baixo. Alternativa <strong>B</strong>.</p><p>Em A, o catalisador aumentaria a energia de ativação. C não tem sentido físico. D e E mostram reações exotérmicas, com os produtos abaixo dos reagentes.</p>"},
42: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": ["soro e vacina", "animais peçonhentos"],
     "enunciado": p("As cobras conhecidas como jararacas-ilhoas (<em>Bothrops insularis</em>) vivem isoladas, na Ilha da Queimada Grande, a 35 km do litoral paulista, entre os municípios de Itanhaém e Peruíbe.",
                    "Apesar de possuir um tipo de veneno, altamente tóxico, pois uma única picada pode matar uma pessoa em apenas seis horas, a jararaca-ilhoa é um grande alvo de biopirataria, ou seja, de traficantes que retiram ilegalmente recursos de biodiversidade.",
                    "Caso uma pessoa seja picada por esse tipo de cobra, a terapia utilizada deve ser a de receber"),
     "explicacao": "<p>Depois da picada, é preciso neutralizar o veneno já: o <strong>soro antiofídico</strong> traz anticorpos prontos contra ele. Alternativa <strong>D</strong>.</p><p>Antibiótico combate bactérias, não veneno (A). O soro contém anticorpos, não antígenos (B). E a vacina leva dias ou semanas para fazer efeito e serve para prevenir, não para tratar (C e E).</p>"},
43: {"materia": "Biologia", "assunto": "Ecologia", "tags": ["biopirataria", "biodiversidade"],
     "explicacao": "<p>Retirar espécies ilegalmente da natureza diminui suas populações e pode levar à <strong>extinção</strong>, reduzindo a biodiversidade. Alternativa <strong>B</strong>.</p><p>A biopirataria não melhora a genética da fauna (A), é ilegal por definição (C), não traz ganhos para a biodiversidade (D), e a extinção afetaria primeiro as próprias espécies retiradas, não as que elas comem (E).</p>"},
44: {"materia": "Raciocínio lógico", "assunto": "Lógica", "tags": ["tabelas"],
     "enunciado": JOGOS + P44,
     "explicacao": "<p>Pelo quadro: Alice tem 1 vitória, 1 derrota e 2 empates; Bruno, 3 vitórias e 1 derrota; Carla, 2 vitórias, 1 derrota e 1 empate; Diego, 1 vitória, 2 derrotas e 1 empate; Elias, 0 vitória, 2 derrotas e 2 empates. Só Elias tem mais empates que vitórias sem ter vencido ninguém. Alternativa <strong>E</strong>.</p><p>Alice empata com Elias em número de empates e tem tantas vitórias quanto derrotas (A). Bruno perdeu para Carla, que teve empate (B). Carla enfrentou Bruno, que não empatou (C). E Diego venceu só Carla (D).</p>"},
45: {"materia": "Matemática", "assunto": "Probabilidade",
     "enunciado": JOGOS + p("Assinale a alternativa que apresenta corretamente a probabilidade de que um jogador, escolhido aleatoriamente dentre os cinco competidores mencionados no texto, tenha vencido, pelo menos, uma partida."),
     "alternativas": {"E": "0,2"},
     "explicacao": "<p>Alice, Bruno, Carla e Diego venceram pelo menos uma partida; só Elias não venceu. A probabilidade é 4/5 = <strong>0,8</strong>. Alternativa <strong>B</strong>.</p><p>0,2 é a probabilidade de escolher quem não venceu (E). E 1,0 contaria Elias também (A).</p>"},
46: {"materia": "Português", "assunto": "Interpretação de texto", "tags": ["canção", "quebradeiras de coco"],
     "enunciado": BABACU + P46, "imagens": BABACU_IMG,
     "explicacao": "<p>As “senhoras guerreiras” vão à luta para “custear alimentação” (a própria subsistência) e são “exportadoras” de um produto que chega a outras nações. Alternativa <strong>D</strong>.</p><p>O eu lírico está feliz com a exportação, não com a importação (A). A riqueza não é desperdiçada (B). A natureza dá o fruto, não arrecada doações (C). E o texto não fala de embates com outras nações (E).</p>"},
47: {"materia": "Português", "assunto": "Sintaxe", "tags": ["sujeito"],
     "enunciado": p("O termo sublinhado exerce a função de sujeito em"), "apoio_de": (46, P46),
     "alternativas": {"A": "“<u>Terra</u> fértil, olha a riqueza no chão”.", "B": "“Folhas verdes, oh que <u>maravilha</u>”.", "C": "“A <u>natureza</u> traz o fruto, a perfeição”.",
                      "D": "“Senhoras guerreiras, vão à luta, custear <u>alimentação</u>”.", "E": "“Nosso produto assim chegou em outras <u>nações</u>”."},
     "explicacao": "<p>Quem “traz o fruto”? A natureza: “natureza” é o núcleo do sujeito do verbo “trazer”. Alternativa <strong>C</strong>.</p><p>“Terra” é um chamamento, um vocativo (A). “Maravilha” está numa frase exclamativa, sem verbo (B). “Alimentação” é objeto de “custear” (D). E “nações” faz parte da indicação de lugar “em outras nações” (E).</p>"},
48: {"materia": "Português", "assunto": "Verbos", "tags": ["imperativo"],
     "enunciado": p("Transpondo o verbo do verso “Senhoras guerreiras, vão à luta” para o imperativo afirmativo, na segunda pessoa do plural, teríamos"), "apoio_de": (46, P46),
     "explicacao": "<p>O imperativo afirmativo de 2ª pessoa do plural (vós) vem do presente do indicativo sem o “s”: vós ides → <strong>ide</strong>. Alternativa <strong>C</strong>.</p><p>“Vá” é 3ª pessoa do singular (você) (A), “vai” é 2ª do singular (tu) (B), “vamos” é 1ª do plural (D) e “venham” é de outro verbo, “vir” (E).</p>"},
49: {"materia": "Português", "assunto": "Figuras de linguagem", "tags": ["personificação"],
     "enunciado": p("No verso “A natureza traz o fruto, a perfeição”, ocorre"), "apoio_de": (46, P46),
     "explicacao": "<p>A natureza aparece agindo como uma pessoa, que “traz” o fruto: é <strong>personificação</strong> (prosopopeia). Alternativa <strong>E</strong>.</p><p>Não há ideias opostas (A e B), nem palavra usada fora do sentido por falta de outra (C), nem suavização de algo ruim (D).</p>"},
50: {"materia": "Português", "assunto": "Gêneros textuais", "tags": ["charge"],
     "enunciado": CRISE + P50, "imagens": CRISE_IMG,
     "explicacao": "<p>É uma charge: trata de um tema atual (a crise climática) e critica com humor. Uma sala só para os prevenidos e 99 para os despreparados mostram que <strong>quase ninguém se prepara</strong>. Alternativa <strong>C</strong>.</p><p>É uma imagem única, não uma tirinha em quadros (A e E). O desenho não fala de acadêmicos nem de desmatamento (B). E a crítica é à falta de preparo, não ao interesse pela economia verde (D).</p>"},
51: {"materia": "Português", "assunto": "Formação de palavras", "tags": ["prefixos"],
     "enunciado": p("O prefixo usado em “despreparado” está presente também em"), "apoio_de": (50, P50),
     "explicacao": "<p>Em “despreparado”, o prefixo “des-” indica negação ou ação contrária (não preparado). O mesmo acontece em <strong>desabrigo</strong> (falta de abrigo). Alternativa <strong>D</strong>.</p><p>Em “apático”, o prefixo é “a-” (A); em “diálogo”, “dia-” (B); em “alinhado”, “a-” (C). E em “denunciado”, “de-” não forma uma ideia de negação: a palavra vem de “denunciar” (E).</p>"},
52: {"materia": "Matemática", "assunto": "Funções",
     "enunciado": p("Considere a função real <em>f</em>, definida pela expressão <em>f</em>(2 − x) = 3x<sup>2</sup>.", "Assinale a alternativa que apresenta corretamente o valor de <em>f</em>(−1)."),
     "explicacao": "<p>Para ter f(−1), é preciso que 2 − x = −1, ou seja, x = 3. Então f(−1) = 3 · 3² = <strong>27</strong>. Alternativa <strong>D</strong>.</p><p>Substituir x = −1 direto dá 3 (B), um erro comum. E 48 vem de usar x = 4 (E).</p>"},
53: {"materia": "Matemática", "assunto": "Geometria espacial", "tags": ["volume do cilindro"],
     "explicacao": "<p>V = área da base × altura = 200 000 · 5 = 1 000 000 m³. Como 1 m³ = 1 000 L, o volume é <strong>1 000 000 000 L</strong>. Alternativa <strong>E</strong>.</p><p>Esquecer de converter m³ em litros, ou converter com o fator errado, leva aos outros valores.</p>"},
54: {"materia": "História", "assunto": "História contemporânea", "tags": MULTI + ["Segunda Guerra Mundial", "reciclagem"],
     "enunciado": p("Durante a Segunda Guerra Mundial, nos Estados Unidos, foram feitas campanhas publicitárias que chamavam a população a contribuir, de diferentes formas, para os esforços de guerra. Os cartazes ilustram um dos aspectos dessas campanhas.")
                  + "[[fig:1]]" + url("https://tinyurl.com/yj5zaz4u", "26.09.2024", "") + p("A partir dos cartazes, pode-se concluir corretamente que"),
     "imagens": figs(("q54", "Dois cartazes de propaganda dos EUA na Segunda Guerra. No primeiro, três donas de casa marcham com uma faixa “Up housewives and at ’em!” e trazem papel, metal e ossos; embaixo: “Put out your paper, metal, bones – they make planes, guns, tanks, ships &amp; ammunition”. No segundo, “Scrap! Will help win – Don’t mix it!”: latas separadas por tipo de material (ferro, aço, borracha, latão, bronze, alumínio, cobre); embaixo: “Come on, C-H... do more! This isn’t peace – it’s war!”.")),
     "explicacao": "<p>Os cartazes pedem que a população junte papel, metal e ossos, porque “eles fazem aviões, armas, tanques, navios e munição”, e que não misture os materiais. A guerra exigia muita matéria-prima, e a <strong>separação e a reciclagem</strong> ajudavam a suprir a falta. Alternativa <strong>B</strong>.</p><p>Os cartazes não falam de compostagem (A), nem de estocar recursos (C), nem de um plano nacional de resíduos (D), nem de higiene (E).</p>"},
55: {"materia": "Química", "assunto": "Estudo dos gases", "tags": ["equação de Clapeyron", "biodiesel"],
     "enunciado": apoio("O diesel comercializado no Brasil é uma mistura que contém atualmente 14% de biodiesel. Se esse percentual for aumentado para 25%, o Brasil deixará de emitir mais de 330 milhões de toneladas de CO<sub>2</sub> em 10 anos.")
                  + url("https://tinyurl.com/yc568vmh", "01.10.2024")
                  + p("Considerando que a pressão é de 1 atm e que a temperatura é 300 K, assinale a alternativa a qual indica o volume aproximado de CO<sub>2</sub>, em litros, que deixará de ser emitido pelo Brasil ao realizar a mudança, descrita no texto, na composição do diesel.",
                      "Dados: massa molar do CO<sub>2</sub> = 44 g/mol, 1 t = 10<sup>6</sup> g; Equação de estado de um gás: P ⋅ V = n ⋅ R ⋅ T; \\(R = 0{,}082\\ \\dfrac{\\text{atm} \\cdot \\text{L}}{\\text{K} \\cdot \\text{mol}}\\)"),
     "explicacao": "<p>330 milhões de toneladas = 3,3 × 10⁸ · 10⁶ g = 3,3 × 10¹⁴ g. Em mols: n = 3,3 × 10¹⁴ ÷ 44 = 7,5 × 10¹² mol. Então V = nRT ÷ P = 7,5 × 10¹² · 0,082 · 300 ÷ 1 ≈ <strong>1,84 × 10¹⁴ L</strong>. Alternativa <strong>E</strong>.</p><p>7,50 × 10¹² é o número de mols, não o volume (C). E 2,46 × 10¹² esquece de multiplicar pelo número de mols certo (B).</p>"},
56: {"materia": "Inglês", "assunto": "Vocabulário", "tags": ["food miles"],
     "enunciado": FRUTAS + P56, "imagens": FRUTAS_IMG,
     "explicacao": "<p>O cartaz explica: “Food miles are the distance a certain food has to travel from its point of origin to its destination – our kitchen table.” É a <strong>distância que o alimento percorre</strong> da origem até o consumidor. Alternativa <strong>D</strong>.</p><p><em>Miles</em> são milhas, não milhares (A). Não se trata de viagens turísticas (B), de quantidade de frutas (C) nem da quantidade de CO₂, que é uma consequência das food miles (E).</p>"},
57: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": ["campanha"],
     "enunciado": FRUTAS + p("A campanha tem por objetivo"), "imagens": FRUTAS_IMG,
     "explicacao": "<p>O lema “Buy local &amp; buy in season” pede que o leitor compre alimentos <strong>da sua região e da estação</strong>, que viajam menos e emitem menos carbono. Alternativa <strong>A</strong>.</p><p>A campanha não fala de exportação britânica (B), não elogia a globalização dos alimentos (C), não trata de intercâmbio de sementes (D) nem de aumentar exportações de países emergentes (E).</p>"},
58: {"materia": "Matemática", "assunto": "Sequências", "tags": ["progressão aritmética"],
     "enunciado": p("Como parte de um projeto ambiental, foram plantadas mudas de árvores frutíferas em um terreno, dispostas em linha reta mantendo sempre a mesma distância entre as árvores.",
                    "A primeira muda foi plantada a 2 metros do início do terreno. A segunda, a uma distância de (6 + x) metros também do início do terreno. E, a terceira, ficou a 18 metros do início do terreno.",
                    "Logo, essa sequência de distâncias forma uma Progressão"),
     "explicacao": "<p>Se a distância entre as árvores é sempre a mesma, as posições formam uma PA. O termo do meio é a média dos vizinhos: 6 + x = (2 + 18) ÷ 2 = 10. A sequência é 2, 10, 18, de <strong>razão 8</strong>. Alternativa <strong>E</strong>.</p><p>4 é o valor de x, não a razão (A e B). E não é PG: 10 ÷ 2 = 5, mas 18 ÷ 10 = 1,8 (B e D).</p>"},
59: {"materia": "Matemática", "assunto": "Análise combinatória", "tags": ["permutação com repetição"],
     "enunciado": p("Sabendo que n! = n ⋅ (n – 1) ⋅ (n – 2) … 3 ⋅ 2 ⋅ 1, com n natural, pode-se afirmar que o número total de permutações distintas formadas com as 8 letras da palavra SEMENTES é dado por"),
     "alternativas": {"A": "8!", "B": "8! ÷ (3! ⋅ 2!)", "C": "8! ÷ (8 – 8)!", "D": "8! ÷ (2! ⋅ 2! ⋅ 2!)", "E": "8! ÷ (2! ⋅ 2!)"},
     "explicacao": "<p>SEMENTES tem 8 letras, com o E repetido 3 vezes e o S repetido 2 vezes (M, N e T aparecem uma vez). Na permutação com repetição, divide-se 8! pelos fatoriais das repetições: <strong>8! ÷ (3! ⋅ 2!)</strong>. Alternativa <strong>B</strong>.</p><p>8! contaria trocas entre letras iguais (A e C, já que 0! = 1). D e E erram as repetições.</p>"},
60: {"materia": "Física", "assunto": "Termologia", "tags": ["calor sensível"],
     "enunciado": p("Uma das práticas de sustentabilidade é o uso de “telhados verdes” ou “eco telhados”. Trata-se de uma cobertura vegetal colocada sobre o telhado de uma construção. Esses telhados têm a função de reduzir a temperatura interna das edificações e melhorar a umidade relativa do ar no local, reduzindo significativamente o alto consumo de energia.",
                    "Considere a cobertura de uma construção sem o uso do telhado verde, mas, sim, de um concreto cujo calor específico do material seja 1 000 J/kg·°C e massa total de 5 000 kg. Em uma situação específica, esse material absorve 75 MJ de energia em um dia de exposição direta ao Sol. Nessa mesma situação, caso fosse usado o telhado verde, a temperatura seria reduzida em 5 °C.",
                    "Sabendo que Q = m·c·Δθ, assinale a alternativa que apresenta corretamente a variação da temperatura observada, em °C, caso fosse usado o telhado verde nas condições apresentadas."),
     "explicacao": "<p>Sem o telhado verde: Δθ = Q ÷ (m · c) = 75 000 000 ÷ (5 000 · 1 000) = 15 °C. Com o telhado verde, a variação seria 5 °C menor: 15 − 5 = <strong>10 °C</strong>. Alternativa <strong>D</strong>.</p><p>15 °C é a variação sem o telhado verde (C), 20 °C soma os 5 °C em vez de subtrair (B), e 5 °C é só a redução (E).</p>"},
61: {"materia": "Física", "assunto": "Óptica", "tags": ["reflexão e refração", "energia solar"],
     "explicacao": "<p>Se o revestimento reduz a luz refletida, sobra mais luz para entrar no semicondutor e ser convertida em eletricidade. Alternativa <strong>A</strong>.</p><p>Aumentar ou completar a reflexão faria o contrário: menos luz absorvida (B, C e D). E não existe índice de refração nulo: o menor possível é o do vácuo, igual a 1 (E).</p>"},
62: {"materia": "Matemática", "assunto": "Geometria plana", "tags": ["área do retângulo"],
     "explicacao": "<p>O telhado tem 8 · 5 = 40 m², e cada placa, 1 · 2 = 2 m². Cabem 40 ÷ 2 = 20 placas (por exemplo, 4 fileiras de 5 placas). Em 30 dias: 20 · 1,2 · 30 = <strong>720 kWh</strong>. Alternativa <strong>E</strong>.</p><p>Esquecer de multiplicar por todas as placas, ou usar o número errado de placas, leva aos outros valores.</p>"},
63: {"materia": "Física", "assunto": "Cinemática", "tags": ["velocidade média", "gráficos"],
     "enunciado": enun(R, 63, figs={"p22-1": 1, "p22-2": 2}, trocas=[("a massa CO<sub>2</sub>", "a massa de CO<sub>2</sub>")]),
     "imagens": figs(("q63a", "Gráfico 1: consumo de gasolina (L) em função da velocidade (km/h). Pontos: 10,0 L a 80 km/h, 12,5 L a 100 km/h e 20,0 L a 120 km/h, ligados por uma curva crescente."),
                     ("q63b", "Gráfico 2: posição (km) em função do tempo (h), uma reta crescente. Pontos: 50 km em 0 h, 100 km em 0,5 h, 150 km em 1,0 h e 200 km em 1,5 h.")),
     "explicacao": "<p>No gráfico 2, o carro anda 50 km a cada 0,5 h: v = 100 km/h. No gráfico 1, a 100 km/h o consumo é de 12,5 L. Com 2 kg de CO₂ por litro: 12,5 · 2 = <strong>25 kg</strong>. Alternativa <strong>C</strong>.</p><p>20 kg viria de usar 10 L (80 km/h) (B), e 40 kg, de usar 20 L (120 km/h) (D).</p>"},
64: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["crédito de carbono"],
     "explicacao": "<p>Créditos de carbono são obtidos por quem reduz ou remove emissões. Desenvolver <strong>energia limpa e renovável</strong> diminui as emissões de gases de efeito estufa. Alternativa <strong>E</strong>.</p><p>Combustíveis fósseis emitem CO₂ (A). Derrubar florestas libera carbono (B). Queimar lixo em altos-fornos também emite (C). E aumentar as emissões é o contrário do objetivo dos créditos (D).</p>"},
})
completar(Q, R)
