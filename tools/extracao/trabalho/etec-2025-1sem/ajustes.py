# Ajustes da conferência humana: Vestibulinho ETEC 1º semestre de 2025 (exame de 15/12/2024)
# Refeito em 23/10/2026 (a primeira versão se perdeu no reinício do ambiente). Texto conferido com as páginas.
# Tema implícito: plantas (sem texto de apresentação na prova).
# O poema de João Doederlein (Q50) fica como imagem; o alt descreve sem transcrever.
# Gabarito: oficial (1º SEM/25). Sem anuladas. Gabarito conferido com resolução própria nas 50 questões.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import A, carregar, enun, tabela, colunas, completar, trecho

ID = "etec-2025-1sem"
META = {
    "id": ID,
    "banca": "ETEC",
    "ano": 2025,
    "semestre": 1,
    "titulo": "Vestibulinho ETEC, 1º semestre de 2025",
    "fonte": "Centro Paula Souza",
    "dataExame": "2024-12-15",
    "duracaoMinutos": 240,
    "tema": "Plantas",
    "pdf": f"assets/provas/{ID}.pdf",
}

R = carregar(ID)


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


def figs_q(*pares):
    return [{"arquivo": a, "alt": t} for a, t in pares]


# ---------- textos e figuras compartilhados ----------
TIRINHA = (chamada("Leia os textos para responder às questões de 07 a 09.") + "[[fig:1]]"
           + url("https://tinyurl.com/3dxrhkpp", "13.09.2024", "Original colorido."))
TIRINHA_IMG = ("q07", "Tirinha “Cientirinhas #180”, em quatro quadrinhos, com plantas em vasos. 1º: uma planta carnívora conta: “Aí eu disse pra Rosa: ‘Amiga, para de sofrer por esse boy lixo!’ Porque tu me conhece, né? Eu falo na lata!”. 2º: “A coitada tava lá debaixo da sacada, toda borocochô. Mas me deu uma ojeriza do Cravo, menina!”. 3º: duas flores conversam; uma diz: “Gente! Como é tagarela essa planta carnívora!”, e a outra responde: “Ela é desse jeito pra não morrer de fome.”. 4º: a primeira pergunta: “Como assim?”, e a outra diz: “Uai, você não sabia? Em boca fechada não entra mosca!”")

EUGENOL_IMG = ("q12", "Fórmulas estruturais lado a lado. Eugenol: anel benzênico com um grupo OH, um grupo O–CH₃ vizinho a ele e, do lado oposto, a cadeia CH₂–CH=CH₂; ao todo, C₁₀H₁₂O₂. Vanilina: o mesmo anel com OH e O–CH₃, mas no lugar da cadeia há um grupo aldeído, H–C=O; ao todo, C₈H₈O₃.")
Q12_15 = ["O cravo-da-índia é amplamente", "Seu óleo essencial"]

DORMENTE = (chamada("Leia os textos para responder às questões 25 e 26.")
            + apoio("A utilização de dormentes de madeira em ferrovias garante a fixação e o alinhamento dos trilhos. Eles podem ser de tipos variados: roliços, semi-roliços, de duas faces e prismáticos.",
                    "Um dormente prismático, por exemplo, mede 2 metros de comprimento, 0,24 metros de largura, 0,16 metros de altura e tem o formato de um paralelepípedo retorretângulo, conforme imagem.",
                    "Em ferrovias brasileiras, são usados, normalmente, 1600 dormentes por quilômetro.")
            + "[[fig:1]]" + url("https://tinyurl.com/3wxpuvrx", "09.09.2024"))
DORMENTE_IMG = ("q25", "Ilustração de um dormente de madeira em forma de paralelepípedo, com 2 m de comprimento, 0,24 m de largura e 0,16 m de altura, e de um trilho de aço. Setas ligam os dois a uma foto de trecho de ferrovia, em que os trilhos estão presos sobre dormentes alinhados lado a lado, em meio a pedras.")
P25 = p("Suponha que, em uma região do Brasil, será construída uma linha férrea de 2 km usando apenas dormentes prismáticos.",
        "Logo, o volume total de madeira, em metros cúbicos, necessária para os dormentes utilizados na construção dessa linha é")

MORINGA_Q = ["Suas folhas são ricas", "Dentro de suas longas"]
MORINGA_T = [("ossos</p><p class=\"apoio\">e dentes", "ossos e dentes")]

Q = {
1: {"materia": "Biologia", "assunto": "Botânica", "tags": ["cultivo"],
    "enunciado": enun(R, 1, quebras=["Outro papel", "Compreender suas"]),
    "explicacao": "<p>Água em excesso encharca o solo e ocupa os espaços onde haveria ar; sem oxigênio, as raízes não conseguem respirar. Por isso, cada planta deve receber <strong>a quantidade certa de água</strong>. Alternativa <strong>C</strong>.</p><p>A adubação correta repõe nutrientes e não é tóxica (A). Lesmas e caramujos comem as plantas e não polinizam (B). O controle biológico é justamente uma forma de combater pragas (D). E o vento aumenta, em vez de impedir, a evaporação da água do solo (E).</p>"},
2: {"materia": "Geografia", "assunto": "Agropecuária", "tags": ["monocultura"],
    "enunciado": enun(R, 2, quebras=["Atualmente, usamos", "Geralmente, 60", "Além disso, a monocultura", "Por outro lado"]),
    "explicacao": "<p>O texto diz que a monocultura de arroz, milho e trigo “pode provocar a degradação do solo”, com esgotamento de nutrientes. O cultivo de uma única espécie numa área está ligado ao <strong>empobrecimento do solo</strong> e também favorece pragas e doenças. Alternativa <strong>D</strong>.</p><p>Só 6 a 7 mil das 30 mil espécies comestíveis foram cultivadas (A). Dependemos de apenas 30 das 170 culturas comerciais (B). Os três grãos não fornecem as vitaminas e os minerais necessários (C). E as culturas esquecidas talvez não tenham sido devidamente pesquisadas ou tenham baixo rendimento (E).</p>"},
3: {"materia": "Geografia", "assunto": "Agropecuária", "tags": ["trigo"],
    "enunciado": enun(R, 3).replace('<p class="apoio">HARARI', '<p class="fonte">HARARI'),
    "explicacao": "<p>O texto cita as Grandes Planícies da América do Norte, onde hoje se caminha por centenas de quilômetros só entre plantações de trigo. Essa região fica nos <strong>Estados Unidos e no Canadá</strong>, grandes produtores do cereal. Alternativa <strong>D</strong>.</p><p>No Centro-Oeste brasileiro predominam soja e milho (A). A Grã-Bretanha aparece só como comparação de tamanho (B). O Oriente Médio exporta principalmente petróleo (C). E o texto diz que o trigo “não gostava de rochas e pedregulhos” (E).</p>"},
4: {"materia": "Biologia", "assunto": "Botânica", "tags": ["PANCs"],
    "explicacao": "<p>O texto diz que as PANCs atendem à demanda por nutrientes e que produzi-las em larga escala “poderia ajudar a combater a fome”. Alternativa <strong>B</strong>.</p><p>Elas suprem as necessidades humanas de nutrientes (A), são resistentes a doenças e pragas (C), têm boa adaptação climática (D) e ainda não são produzidas em larga escala, só por pequenas comunidades (E).</p>"},
5: {"materia": "Matemática", "assunto": "Porcentagem", "tags": ["arredondamento"],
    "enunciado": p("Leia o texto e assinale a alternativa que completa correta e respectivamente os espaços numerados.")
                 + apoio("Sócrates não tomou um pingado<sup>1</sup> com Platão. Cleópatra e Júlio César jamais marcaram um <em>date</em><sup>2</sup> num café de Alexandria. A humanidade só conheceu o café bem depois. Hoje, ele é um dos mais valiosos produtos primários comercializados no mundo, tanto que, em 2022, foi produzido um total de 171,7 milhões de sacas desse grão.",
                         "É curioso observar que cada saca de café verde tem 60 kg e rende somente 48 kg de café torrado, ou seja, o café perde cerca de ____<strong>I</strong>____ % de sua massa durante o processo de torrefação. Deste modo, é possível estimar que, para produzir uma tonelada de café torrado, são necessárias, no mínimo, ____<strong>II</strong>____ sacas de café verde.")
                 + url("https://tinyurl.com/3w9a2x3h", "09.09.2024")
                 + fonte("<sup>1</sup> pingado – leite com café. <sup>2</sup> <em>date</em> – encontro romântico com alguém."),
    "alternativas": colunas(["I", "II"], [["12", "21"], ["12", "35"], ["20", "35"], ["20", "21"], ["21", "35"]]),
    "explicacao": "<p>A saca perde 60 − 48 = 12 kg, e 12 ÷ 60 = 0,20 = <strong>20 %</strong> (I). Uma tonelada são 1 000 kg de café torrado, e cada saca rende 48 kg: 1 000 ÷ 48 ≈ 20,8. Com 20 sacas não se chega a uma tonelada, então são necessárias, no mínimo, <strong>21 sacas</strong> (II). Alternativa <strong>D</strong>.</p><p>12 é a perda em quilos, não em porcentagem (A e B). E 35 não vem de nenhuma conta coerente com os dados (B, C e E).</p>"},
6: {"materia": "Física", "assunto": "Eletricidade", "tags": ["lei de Ohm", "notação científica"],
    "enunciado": p("Plantas carnívoras, como as dioneias, são conhecidas pelo aprisionamento de suas presas. Esse movimento ocorre por um processo denominado tigmonastia, em que, ao serem tocadas, as células sensíveis da planta geram sinais elétricos que são propagados rapidamente e fazem com que a planta se feche.",
                   "Durante o fechamento das folhas, a resistência elétrica entre dois pontos do caule pode ser obtida por meio da Lei de Ohm, conhecida por U = R · i, em que a diferença de potencial (U) aplicada nesses pontos gera uma corrente elétrica (i) que depende da resistência elétrica (R) do material.",
                   "Se uma diferença de potencial de 1 × 10<sup>–1</sup> volt é aplicada entre esses pontos e a corrente elétrica medida é de 2 × 10<sup>–8</sup> ampères, a resistência elétrica, medida em ohm, do caule da planta é"),
    "alternativas": {l: f"5 × 10<sup>{e}</sup>." for l, e in zip("ABCDE", ["–9", "–7", "–1", "6", "8"])},
    "explicacao": "<p>Pela lei de Ohm, R = U ÷ i = (1 × 10<sup>–1</sup>) ÷ (2 × 10<sup>–8</sup>) = 0,5 × 10<sup>7</sup> = <strong>5 × 10<sup>6</sup> Ω</strong>. Alternativa <strong>D</strong>.</p><p>Multiplicar U por i, em vez de dividir, dá 2 × 10<sup>–9</sup>, perto do valor de A. Errar o sinal dos expoentes na divisão leva a B, C e E.</p>"},
7: {"materia": "Português", "assunto": "Interpretação de texto", "tags": ["humor", "tirinha"],
    "enunciado": TIRINHA + p("A construção de humor no texto se deve, entre outros fatores,"), "imagens": figs_q(TIRINHA_IMG),
    "explicacao": "<p>A planta carnívora fala sem parar sobre a vida das outras flores (a Rosa, o Cravo). A outra flor explica que ela é assim “pra não morrer de fome” e brinca com o ditado “em boca fechada não entra mosca”: falar o tempo todo é o que permite à planta pegar moscas. O humor está na <strong>fofoca como traço essencial para a sobrevivência</strong> da planta carnívora. Alternativa <strong>E</strong>.</p><p>O Cravo é criticado, não valorizado (A). A linguagem é coloquial, não solene (B). Não há violência doméstica sendo amenizada (C). E são plantas que ganham comportamentos humanos, e não o contrário (D).</p>"},
8: {"materia": "Português", "assunto": "Classes de palavras", "tags": ["vocativo", "tirinha"],
    "enunciado": TIRINHA + p("Após a leitura atenta dos quadrinhos, é correto afirmar que"), "imagens": figs_q(TIRINHA_IMG),
    "explicacao": "<p>Em “Amiga, para de sofrer” e em “mas me deu uma ojeriza do Cravo, menina!”, os termos “amiga” e “menina” chamam o interlocutor, isto é, quem ouve a fala: são <strong>vocativos</strong>. Alternativa <strong>C</strong>.</p><p>As referências à canção “O Cravo brigou com a Rosa” são intertextuais, não metalinguísticas (A). “Ojeriza” mantém o sentido de aversão (B). “Pra” indica finalidade (“pra não morrer de fome”) e destinatário (“disse pra Rosa”), não lugar (D). E a linguagem coloquial combina com a tirinha (E).</p>"},
9: {"materia": "Português", "assunto": "Classes de palavras", "tags": ["interjeição", "tirinha"],
    "enunciado": TIRINHA + p("No quarto quadrinho, a interjeição “uai” evidencia que a personagem, diante da pergunta de sua amiga, experiencia"), "imagens": figs_q(TIRINHA_IMG),
    "explicacao": "<p>“Uai, você não sabia?” mostra espanto de quem achava aquilo óbvio. A interjeição “uai” expressa <strong>surpresa</strong>. Alternativa <strong>A</strong>.</p><p>Nada na fala indica alegria, medo, indiferença (apatia) ou aversão (B a E).</p>"},
10: {"materia": "História", "assunto": "História contemporânea", "tags": ["Revolução dos Cravos", "Portugal"],
     "enunciado": enun(R, 10, quebras=["Um dos motivos"]),
     "explicacao": "<p>O movimento que derrubou a ditadura salazarista em 25 de abril de 1974 ficou conhecido pelos cravos colocados nos canos das armas dos soldados: a <strong>Revolução dos Cravos</strong>, em <strong>Portugal</strong>. Alternativa <strong>E</strong>.</p><p>As outras alternativas não têm relação com Salazar nem com Marcello Caetano, que governaram Portugal (A a D).</p>"},
11: {"materia": "História", "assunto": "História contemporânea", "tags": ["descolonização da África"],
     "enunciado": enun(R, 11, quebras=["Um dos motivos"]),
     "explicacao": "<p>As guerras coloniais portuguesas aconteceram em Angola, Moçambique e Guiné-Bissau, e Portugal também controlava Cabo Verde e São Tomé e Príncipe. <strong>Angola e Cabo Verde</strong> eram colônias portuguesas. Alternativa <strong>A</strong>.</p><p>Nigéria e África do Sul foram colônias britânicas (B). Madagascar, Senegal, Mali e República Centro-Africana foram francesas (C e E). A Etiópia nunca foi colônia de forma duradoura, e o Saara Ocidental foi espanhol (D).</p>"},
12: {"materia": "Química", "assunto": "Química orgânica", "tags": ["cravo-da-índia"],
     "enunciado": enun(R, 12, quebras=Q12_15, figs={"p07-1": 1}), "imagens": figs_q(EUGENOL_IMG),
     "explicacao": "<p>O texto diz que o uso do cravo-da-índia em doces começou por “sua ação repelente que impede a invasão de formigas, motivo pelo qual é usado popularmente em açucareiros”. Alternativa <strong>B</strong>.</p><p>O cravo era vendido “a preço de ouro”, sem extração de ouro (A). Ele é usado em medicamentos por suas propriedades antimicrobianas e anti-inflamatórias, não pela ação repelente (C). O cravo serviu para sintetizar a vanilina, que não está no óleo essencial (D). E o aroma de baunilha é da vanilina, não do eugenol (E).</p>"},
13: {"materia": "Química", "assunto": "Química orgânica", "tags": ["fórmula molecular"],
     "enunciado": enun(R, 13, quebras=Q12_15, figs={"p07-1": 1}), "imagens": figs_q(EUGENOL_IMG),
     "explicacao": "<p>Contando os átomos das estruturas: o eugenol é C<sub>10</sub>H<sub>12</sub>O<sub>2</sub> e a vanilina é C<sub>8</sub>H<sub>8</sub>O<sub>3</sub>. A diferença é de <strong>dois átomos de carbono, quatro de hidrogênio e um de oxigênio</strong>. Alternativa <strong>E</strong>.</p><p>Os números de carbonos (10 e 8) e de hidrogênios (12 e 8) são diferentes (A e B). Os dois têm os mesmos elementos, C, H e O (C). E as estruturas não são idênticas (D).</p>"},
14: {"materia": "História", "assunto": "Grandes Navegações", "tags": ["especiarias"],
     "enunciado": enun(R, 14, quebras=Q12_15 + ["Assinale a alternativa que apresenta, corretamente"], figs={"p07-1": 1}), "imagens": figs_q(EUGENOL_IMG),
     "explicacao": "<p>O cravo-da-índia é nativo das ilhas Molucas, na Ásia. Ele chegou ao Brasil com os <strong>portugueses</strong>, que controlavam a rota marítima das especiarias aberta pelas <strong>Grandes Navegações</strong>. Alternativa <strong>A</strong>.</p><p>A planta não é americana, então não poderia vir por trilhas incas (B) nem com os povos de Clóvis, que vieram da Ásia, e não da Europa (C). Não é africana (D). E não é típica da Itália (E).</p>"},
15: {"materia": "Química", "assunto": "Substâncias e misturas", "tags": ["separação de misturas"],
     "enunciado": enun(R, 15, quebras=Q12_15, figs={"p07-1": 1, "p08-1": 2}).replace("[[fig:2]]", "[[fig:2]]" + fonte("Fonte dos dados em: &lt;https://tinyurl.com/3pmnrh9b&gt; Adaptado. Acesso em: 09.09.2024.")).replace("na figura, é denominado", "na figura é denominado"),
     "imagens": figs_q(EUGENOL_IMG, ("q15", "Aparelho de destilação: um balão com cravo e água é aquecido por uma manta elétrica; o vapor sobe e passa por um tubo resfriado por água fria (condensador), que goteja o líquido condensado em um béquer, onde se forma uma emulsão.")),
     "explicacao": "<p>O balão aquece cravo e água, o vapor passa pelo condensador resfriado com água fria e volta ao estado líquido, que é recolhido no béquer. É uma <strong>destilação</strong> (por arraste de vapor). Alternativa <strong>D</strong>.</p><p>Filtração separa sólido de líquido com um filtro (A). Decantação usa a diferença de densidade, com a mistura em repouso (B). Sublimação é a passagem direta de sólido para gás (C). E floculação aglomera partículas com um produto químico (E).</p>"},
16: {"materia": "Matemática", "assunto": "Análise combinatória", "tags": ["arranjo"],
     "enunciado": enun(R, 16, trocas=[("supermercado: • pessoas", "supermercado:</p><p class=\"apoio\">• pessoas"), ("congelados; • pessoas", "congelados;</p><p class=\"apoio\">• pessoas"), ("peixaria; e • pessoas", "peixaria; e</p><p class=\"apoio\">• pessoas"), ("vinhos. A popularidade", "vinhos.</p><p class=\"apoio\">A popularidade")], quebras=["Assinale a alternativa que apresenta corretamente"]),
     "explicacao": "<p>A palavra ABACAXI tem 5 letras diferentes: A, B, C, X e I. Uma sigla de 3 letras diferentes depende da ordem (ABC é diferente de BCA), então é um arranjo: 5 · 4 · 3 = <strong>60</strong>. Alternativa <strong>C</strong>.</p><p>Contar as 7 letras da palavra, com as repetições, daria 7 · 6 · 5 = 210 (E). E 35 seria uma combinação de 7 letras tomadas 3 a 3, que ignora a ordem (B).</p>"},
17: {"materia": "Matemática", "assunto": "Porcentagem",
     "enunciado": enun(R, 17, trocas=[("supermercado: • pessoas", "supermercado:</p><p class=\"apoio\">• pessoas"), ("congelados; • pessoas", "congelados;</p><p class=\"apoio\">• pessoas"), ("peixaria; e • pessoas", "peixaria; e</p><p class=\"apoio\">• pessoas"), ("vinhos. A popularidade", "vinhos.</p><p class=\"apoio\">A popularidade"),
                                     ("[[FIG:p09-1]]", tabela(["Faixa etária", "Usuários (%)"], [["18 – 24", "38"], ["25 – 34", "45"], ["35 – 44", "13"], ["45 – 54", "3"], ["55 – 64", "1"]]) + fonte("Fonte dos dados em: &lt;https://tinyurl.com/3pmnrh9b&gt; Adaptado. Acesso em: 09.09.2024."))],
                  quebras=["A tabela apresenta", "Logo, se for constatado"]),
     "explicacao": "<p>Dos 200 participantes, 75 % são homens: 0,75 · 200 = 150. O setor de congelados recebe a faixa de 18 a 24 anos, que corresponde a 38 % dos usuários: 0,38 · 150 = <strong>57</strong>. Alternativa <strong>B</strong>.</p><p>Aplicar 38 % sobre as 200 pessoas daria 76, mas aí entrariam também as mulheres. Os outros valores não correspondem à combinação dos dois percentuais.</p>"},
18: {"materia": "Biologia", "assunto": "Botânica", "tags": ["angiospermas"],
     "enunciado": enun(R, 18, trocas=[("exemplo: • na América", "exemplo:</p><p class=\"apoio\">• na América"), ("sementes. • na América", "sementes.</p><p class=\"apoio\">• na América"), ("(costela-de-adão).</p><p class=\"apoio\">Essa", "(costela-de-adão). Essa")]),
     "alternativas": colunas(["Grupo vegetal", "Vasos condutores", "Folhas", "Flores", "Frutos comestíveis", "Sementes no interior dos frutos"], [
         ["Pteridófitas", "Não", "Não", "Sim", "Sim", "Não"], ["Gimnospermas", "Sim", "Sim", "Não", "Sim", "Sim"], ["Angiospermas", "Sim", "Sim", "Sim", "Sim", "Sim"],
         ["Gimnospermas", "Não", "Sim", "Sim", "Não", "Sim"], ["Angiospermas", "Não", "Sim", "Não", "Não", "Sim"]]),
     "explicacao": "<p>As duas plantas têm flores e frutos com sementes dentro: são <strong>angiospermas</strong>. Como toda angiosperma, também têm vasos condutores e folhas. A linha com “Sim” em todas as colunas é a da alternativa <strong>C</strong>.</p><p>Pteridófitas não têm flores, frutos nem sementes (A). Gimnospermas não têm flores verdadeiras nem frutos, e têm vasos condutores (B e D). E a linha E nega os vasos, as flores e os frutos, que o texto descreve.</p>"},
19: {"materia": "Biologia", "assunto": "Botânica", "tags": ["fotossíntese", "respiração celular"],
     "explicacao": "<p>A fotossíntese depende de luz. A respiração, que libera a energia da glicose, acontece o tempo todo nas células da planta, <strong>com ou sem luz</strong>. Alternativa <strong>D</strong>.</p><p>Só a fotossíntese transforma gás carbônico e água em glicose e oxigênio; a respiração faz o inverso (A e E). A respiração não depende de clorofila (B). E a fotossíntese não ocorre no escuro (C).</p>"},
20: {"materia": "Química", "assunto": "Substâncias e misturas", "tags": ["fotossíntese"],
     "enunciado": enun(R, 20, figs={"p10-1": 1}),
     "imagens": figs_q(("q20", "Esquema da fotossíntese: o Sol ilumina uma folha; setas mostram a entrada de CO₂ do ar e de H₂O pelo caule, a saída de O₂ e a formação de C₆H₁₂O₆ na folha. Abaixo, a equação 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂.")),
     "explicacao": "<p>Na equação 6CO<sub>2</sub> + 6H<sub>2</sub>O → C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> + 6O<sub>2</sub>, só o O<sub>2</sub> é formado por um único elemento. Há <strong>apenas uma substância simples</strong>. Alternativa <strong>A</strong>.</p><p>Há três substâncias compostas: CO<sub>2</sub>, H<sub>2</sub>O e glicose (B). A água é reagente, não produto (C). O gás carbônico é consumido, e quem é liberado é o oxigênio (D). E a fotossíntese absorve energia luminosa em vez de liberá-la (E).</p>"},
21: {"materia": "Biologia", "assunto": "Botânica", "tags": ["fotossíntese", "luz"],
     "enunciado": enun(R, 21, trocas=[("iluminação: • grupo I", "iluminação:</p><p>• grupo I"), ("visível); • grupo II", "visível);</p><p>• grupo II"), ("verde; e • grupo III", "verde; e</p><p>• grupo III")]),
     "explicacao": "<p>A clorofila absorve bem a luz azul e a vermelha, que fazem parte da luz branca. Com todas as cores do espectro visível, o <strong>grupo I</strong> faz mais fotossíntese e cresce mais. Alternativa <strong>C</strong>.</p><p>Sem luz não há fotossíntese (A). A luz verde é quase toda refletida pelas folhas, por isso elas parecem verdes, e é a menos aproveitada (B e E). E a luz branca não está na faixa do ultravioleta (D).</p>"},
22: {"materia": "Geografia", "assunto": "Biomas", "tags": ["Caatinga"],
     "explicacao": "<p>A Caatinga tem vegetação <strong>heterogênea</strong>, adaptada ao <strong>clima semiárido</strong>: folhas pequenas ou transformadas em espinhos, caules que armazenam água e raízes profundas para suportar a estiagem. Alternativa <strong>C</strong>.</p><p>A descreve uma mistura de Cerrado e Mata dos Cocais. B descreve a Floresta Amazônica. D mistura floresta e campos. E descreve a Mata de Araucárias ou a taiga.</p>"},
23: {"materia": "Física", "assunto": "Termologia", "tags": ["ilha de calor", "propagação do calor"],
     "explicacao": "<p>Na ilha de calor, asfalto e concreto absorvem a radiação solar durante o dia e <strong>irradiam</strong> esse calor para o ambiente, inclusive à noite. Alternativa <strong>A</strong>.</p><p>Os prédios não impedem a movimentação das nuvens nem as chuvas (B). Veículos não “transportam” calor por condução (C). O fenômeno não vem do calor das residências conduzido para fora (D). E o calor do metrô não explica a ilha de calor (E).</p>"},
24: {"materia": "Geografia", "assunto": "Clima", "tags": ["ilha de calor", "áreas verdes"],
     "explicacao": "<p>As copas das árvores fazem sombra, <strong>absorvem parte da radiação solar</strong> e liberam vapor de água pela transpiração. Assim, o solo e as construções esquentam menos. Alternativa <strong>B</strong>.</p><p>O oxigênio liberado não muda o clima (A). As árvores não absorvem todo o gás carbônico nem eliminam a poluição (C). A fotossíntese não cria uma barreira para a energia do Sol (D). E não há brisas quentes sendo bloqueadas (E).</p>"},
25: {"materia": "Matemática", "assunto": "Geometria espacial", "tags": ["volume"],
     "enunciado": DORMENTE + P25, "imagens": figs_q(DORMENTE_IMG),
     "explicacao": "<p>O volume de um dormente é 2 · 0,24 · 0,16 = 0,0768 m³. Em 2 km são 2 · 1 600 = 3 200 dormentes. Volume total: 3 200 · 0,0768 = <strong>245,76 m³</strong>. Alternativa <strong>D</strong>.</p><p>Contar só 1 km dá 122,88 (B). Os outros valores vêm de erros na multiplicação das medidas.</p>"},
26: {"materia": "Matemática", "assunto": "Razão e proporção", "tags": ["porcentagem"],
     "enunciado": p("Suponha que, na construção de um trecho de 1 km de ferrovia no Brasil, uma empresa distribuiu os dormentes de forma que:",
                    "• 25 % sejam do tipo roliço;", "• 30 % sejam do tipo semi-roliço;", "• 35 % sejam do tipo de duas faces;", "• e o restante sejam do tipo prismático.",
                    "Diante dessas condições, é correto afirmar que"),
     "apoio_de": (25, P25),
     "alternativas": {"A": "a razão entre a quantidade de dormentes do tipo roliço e do tipo prismático, nessa ordem, é igual a \\(\\dfrac{2}{1}\\).",
                      "E": "a razão entre a quantidade de dormentes do tipo de duas faces e do tipo semi-roliço, nessa ordem, é igual a \\(\\dfrac{7}{6}\\)."},
     "explicacao": "<p>Os prismáticos são 100 − 25 − 30 − 35 = 10 %. A razão entre os de duas faces e os semi-roliços é 35 : 30 = <strong>7/6</strong>. Alternativa <strong>E</strong>.</p><p>Roliços para prismáticos dá 25 : 10 = 5/2 (A). Semi-roliços mais prismáticos dão 40 % (B). Os dormentes ficam espalhados por toda a ferrovia, e 10 % de 1 km seriam 100 m, não 300 (C). E a diferença entre duas faces e prismáticos é de 25 pontos percentuais (D).</p>"},
27: {"materia": "História", "assunto": "Idade Média", "tags": ["Inquisição"],
     "explicacao": "<p>Entre o fim da Idade Média e o início da Idade Moderna, a Igreja intensificou a repressão a práticas consideradas heréticas. A <strong>Inquisição</strong> investigou e perseguiu as chamadas “bruxas”, vistas como agentes do demônio. Alternativa <strong>C</strong>.</p><p>O Iluminismo é do século XVIII e criticava a Igreja (A). A intensificação de fluxos por avanços técnicos descreve a globalização atual (B). As repúblicas europeias são bem posteriores (D). E as máquinas a vapor surgiram na Revolução Industrial, no século XVIII (E).</p>"},
28: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": ["baixa umidade do ar"],
     "explicacao": "<p>Com o ar seco e a fumaça, é preciso cuidar sobretudo de <strong>crianças e idosos</strong>, mais vulneráveis, e incentivar a <strong>ingestão de água</strong> e de sucos naturais para manter o corpo hidratado. Alternativa <strong>E</strong>.</p><p>Umidificadores deixam o ambiente mais úmido, não mais seco (A). Beber pouca água piora a desidratação (B). Ambientes fechados acumulam ácaros, que pioram as alergias (C). E fungos e mofo fazem mal ao sistema respiratório (D).</p>"},
29: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["queimadas"],
     "explicacao": "<p>Contra queimadas e incêndios, ajudam a <strong>educação ambiental</strong> e o incentivo a <strong>práticas agrícolas sustentáveis</strong>, que dispensam o fogo para limpar terrenos. Alternativa <strong>D</strong>.</p><p>As outras alternativas propõem ações que aumentariam os incêndios: liberar queimadas, reduzir a fiscalização, estimular o desmatamento e usar o fogo como limpeza (A, B, C e E).</p>"},
30: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["sustentabilidade"],
     "enunciado": enun(R, 30, quebras=["Com base nisso"]),
     "explicacao": "<p>A missão pede escolhas sustentáveis e não violentas, que considerem o meio ambiente e também as implicações sociais e éticas. A melhor orientação é buscar o <strong>equilíbrio entre preservação ambiental e bem-estar humano</strong>, minimizando impactos negativos. Alternativa <strong>A</strong>.</p><p>Usar plantas exóticas sem avaliar os efeitos ameaça os ecossistemas (B). Ativismo agressivo prejudica pessoas e não é “não violento” (C). O cultivo de vegetais também pode causar desmatamento, como mostra o caso do agave (D). E alimentos ultraprocessados dependem, sim, de recursos naturais (E).</p>"},
31: {"materia": "Matemática", "assunto": "Funções", "tags": ["função do 2º grau"],
     "enunciado": p("Durante o Renascimento, houve um aumento de interesse por plantas medicinais. Desse período, data o primeiro uso medicinal da dedaleira, da qual, hoje, é obtido um fitofármaco conhecido como digoxina, usado no tratamento de insuficiência cardíaca.",
                    "Suponha que, nesse período histórico, a eficácia do tratamento com dedaleira, em função das semanas de tratamento, pudesse ser estimada pela expressão matemática")
                  + "<p>\\[E(t) = -2t^2 + 15t + 9\\]</p>"
                  + p("em que,", "• <strong>E(t)</strong> é a eficácia do tratamento, em porcentagem; e", "• <strong>t</strong> é o tempo, em semanas, desde o início do tratamento (t ≥ 0).",
                      "Assinale a alternativa na qual é apontada a eficácia do tratamento após 6 semanas."),
     "explicacao": "<p>Basta substituir t = 6: E(6) = −2 · 36 + 15 · 6 + 9 = −72 + 90 + 9 = <strong>27 %</strong>. Alternativa <strong>B</strong>.</p><p>Um erro comum é calcular −2 · 6² como +72, o que daria 171, fora das alternativas. Ou esquecer o termo 9, o que daria 18.</p>"},
32: {"materia": "Geografia", "assunto": "Agropecuária", "tags": ["educação no campo"],
     "explicacao": "<p>O texto mostra que os alunos estudam as disciplinas comuns, como História e Matemática, e aplicam na propriedade da família o que aprendem. Eles <strong>adquirem as competências de qualquer escola e também conhecimentos do dia a dia no campo</strong>. Alternativa <strong>E</strong>.</p><p>Há aulas na escola em semanas alternadas (A). O projeto é promovido pela Secretaria de Estado da Educação (B). O modelo francês foi implantado no Brasil (C). E o curso é de Ensino Médio, que permite ingressar no Ensino Superior (D).</p>"},
33: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["Chico Mendes", "extrativismo"],
     "explicacao": "<p>O seringueiro faz cortes no tronco da seringueira (a sangria) para <strong>extrair o látex</strong>, a matéria-prima da borracha natural. Alternativa <strong>C</strong>.</p><p>Chico Mendes lutava contra o desmatamento, a soja e a pecuária na floresta (A e E). A seringueira é nativa da Amazônia, e derrubá-la contraria a atividade (B). E demarcar terras indígenas não é atividade do seringueiro (D).</p>"},
34: {"materia": "História", "assunto": "Brasil Colônia", "tags": ["drogas do sertão"],
     "explicacao": "<p>As “drogas do sertão” eram produtos da floresta amazônica, como cacau, cravo, canela, guaraná, salsaparrilha e castanha, <strong>exportados como especiarias para a Europa</strong>. Alternativa <strong>E</strong>.</p><p>Não eram entorpecentes nem produtos sintéticos (A), pecuários (B) ou industrializados (C). E os maias viviam na América Central (D).</p>"},
35: {"materia": "Física", "assunto": "Energia", "tags": ["transformação de energia"],
     "explicacao": "<p>No motor a diesel, a combustão libera a energia <strong>química</strong> do combustível, que vira energia <strong>cinética</strong>, o movimento do trator. Alternativa <strong>A</strong>.</p><p>O motor também gera calor e ruído, mas isso é perda, não o que contribui para a produtividade (C e D). O trator não é elétrico nem movido a luz (B e E).</p>"},
36: {"materia": "Física", "assunto": "Cinemática", "tags": ["velocidade média"],
     "explicacao": "<p>O perímetro do quadrado é 4 · 500 = 2 000 m = 2 km. A 10 km/h, o tempo é 2 ÷ 10 = 0,2 h = 0,2 · 60 = <strong>12 min</strong>. Alternativa <strong>B</strong>.</p><p>Considerar só um lado do quadrado dá 3 min (A). Esquecer de converter metros em quilômetros leva a 200 (D).</p>"},
37: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": ["malária", "protozoários"],
     "explicacao": "<p>A malária é causada por protozoários do gênero <em>Plasmodium</em>, transmitidos pela picada da fêmea do mosquito <em>Anopheles</em>. Alternativa <strong>E</strong>.</p><p>Ela não passa de pessoa para pessoa por contato direto (A). O barbeiro e o <em>Trypanosoma</em> estão ligados à doença de Chagas (B e D). E <em>Escherichia</em> é uma bactéria do intestino (C).</p>"},
38: {"materia": "História", "assunto": "Povos indígenas", "tags": ["mandioca"],
     "explicacao": "<p>A mandioca é nativa da América do Sul e foi domesticada por povos indígenas há milhares de anos, no território que hoje é o Brasil. Para vários povos, é um <strong>alimento sagrado</strong>, presente em mitos de origem. Alternativa <strong>B</strong>.</p><p>A mandioca é um alimento muito nutritivo e não é alucinógena (A). É consumida em todo o Brasil (C). Algumas variedades têm compostos que liberam cianeto, mas o processamento os elimina, e a venda é permitida (D). E ela já era cultivada muito antes da imigração árabe (E).</p>"},
39: {"materia": "Biologia", "assunto": "Fisiologia humana", "tags": ["nutrientes"],
     "enunciado": enun(R, 39, quebras=MORINGA_Q, trocas=MORINGA_T),
     "explicacao": "<p>O texto diz que as folhas têm cálcio, potássio, fósforo, magnésio e ferro, e que “alguns desses minerais não só fortalecem ossos e dentes, como também colaboram na contração muscular”. Alternativa <strong>B</strong>.</p><p>O texto cita propriedades benéficas, não intoxicações (A). As fibras ajudam o intestino, e não o atrapalham (C). As sementes ficam nas vagens e se associam a níveis maiores de colesterol bom, não menores (D). E as sementes atraem impurezas; o texto não diz que matam micro-organismos (E).</p>"},
40: {"materia": "Biologia", "assunto": "Fisiologia humana", "tags": ["nutrientes", "sangue"],
     "enunciado": enun(R, 40, quebras=MORINGA_Q, trocas=MORINGA_T),
     "explicacao": "<p>O <strong>ferro</strong> faz parte da hemoglobina, a proteína das hemácias que transporta oxigênio dos pulmões aos tecidos. Alternativa <strong>A</strong>.</p><p>O escorbuto é causado pela falta de vitamina C, e a visão depende da vitamina A (B). Anticorpos são proteínas produzidas pelo corpo, não vitaminas (C). O mineral ligado à tireoide é o iodo (D). E o ser humano não produz vitamina C, por isso precisa ingeri-la (E).</p>"},
41: {"materia": "Química", "assunto": "Estrutura atômica", "tags": ["número de massa"],
     "enunciado": enun(R, 41, quebras=MORINGA_Q, trocas=MORINGA_T)
                  + "<p>Dados: \\({}^{40}_{20}\\mathrm{Ca}\\quad {}^{39}_{19}\\mathrm{K}\\quad {}^{31}_{15}\\mathrm{P}\\quad {}^{24}_{12}\\mathrm{Mg}\\quad {}^{56}_{26}\\mathrm{Fe}\\)</p>",
     "explicacao": "<p>O número de nêutrons é a massa (em cima) menos o número atômico (embaixo). No cálcio: 40 − 20 = <strong>20 nêutrons</strong>. Alternativa <strong>A</strong>.</p><p>O número atômico do ferro é 26; 56 é a massa (B). O do potássio é 19; 15 é o do fósforo (C). O menor número de massa é o do magnésio, 24 (D). E quem tem mais nêutrons é o ferro, 56 − 26 = 30; o magnésio tem só 12 (E).</p>"},
42: {"materia": "Química", "assunto": "Química orgânica", "tags": ["solubilidade", "vitaminas"],
     "enunciado": enun(R, 42, quebras=MORINGA_Q, trocas=MORINGA_T, figs={"p20-1": 1}),
     "imagens": figs_q(("q42", "Fórmulas estruturais. Vitamina A: uma longa cadeia de carbonos com várias ligações duplas alternadas, ligada a um anel de seis carbonos com grupos CH₃, e um único grupo OH na ponta da cadeia. Vitamina C: um anel de cinco átomos com um oxigênio e um grupo C=O, ligado a uma cadeia curta; ao todo, quatro grupos OH espalhados pela molécula.")),
     "explicacao": "<p>A vitamina C tem quatro grupos OH espalhados pela estrutura, que interagem com a água. A vitamina A é uma longa cadeia de carbono e hidrogênio, com um só OH na ponta. Por isso, a vitamina <strong>C é mais solúvel em água</strong> que a A. Alternativa <strong>C</strong>.</p><p>A vitamina A é lipossolúvel (A e D), e a C é hidrossolúvel (B e E).</p>"},
43: {"materia": "História", "assunto": "Brasil Colônia", "tags": ["plantation"],
     "explicacao": "<p>A produção de açúcar colonial seguiu o modelo de <em>plantation</em>: <strong>monocultura</strong> voltada à exportação, em grandes propriedades (<strong>latifúndios</strong>), com <strong>mão de obra escravizada</strong>. Alternativa <strong>C</strong>.</p><p>Não havia diversificação, reforma agrária nem trabalho assalariado (A). Rotação trienal, feudalismo e servidão são da Europa medieval (B). E agricultura familiar, produção orgânica e propriedade coletiva não marcaram a colônia (D e E).</p>"},
44: {"materia": "História", "assunto": "Antiguidade", "tags": ["Egito", "escrita"],
     "explicacao": "<p>Do caule do papiro, cortado em tiras prensadas, os egípcios faziam um <strong>material fino e resistente para escrever</strong>, também chamado papiro. Alternativa <strong>C</strong>.</p><p>O papiro não era usado para fazer armas (A), construir canais (B), fazer pigmentos de maquiagem (D) ou como base de pomadas (E).</p>"},
45: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["agrofloresta"],
     "explicacao": "<p>Götsch reflorestou a fazenda e hoje tira renda de uma pequena área, onde cultiva cacau de alto valor em meio à floresta. <strong>Preservar o meio ambiente pode gerar renda</strong>. Alternativa <strong>E</strong>.</p><p>A fazenda era desmatada e hoje dá lucro (A). Ali se produzem frutas, legumes e cacau (B). A criação de porcos e o cultivo convencional esgotaram o solo (C). E o texto não fala em danos ambientais causados por melhorar o bem-estar (D).</p>"},
46: {"materia": "Português", "assunto": "Coesão e referência", "tags": ["pronomes"],
     "enunciado": enun(R, 46, trocas=[('<p class="apoio"><strong>Leia o texto para responder às questões de 46 a 49.</strong></p>', '<p class="chamada">Leia o texto para responder às questões de 46 a 49.</p>'),
                                     ("<strong>Biotecnologia Indígena</strong> Entre", "<strong>Biotecnologia Indígena</strong></p><p class=\"apoio\">Entre"),
                                     ("<p>I e II se referem ao termo “culinária”.</p>", "")]),
     "alternativas": {"A": "I e II se referem ao termo “culinária”.", "B": "II, III e IV se referem ao termo “florestas”.", "C": "IV e V se referem à expressão “variante domesticada”."},
     "explicacao": "<p>“Que” (VIII) retoma “frutos” (“frutos que foram manipulados”) e “eles” (IX) retoma os <strong>povos indígenas</strong>, que manipularam esses frutos. Alternativa <strong>E</strong>.</p><p>I e II se referem ao cupuaçu (A). II se refere ao cupuaçu, enquanto III e IV retomam “florestas primárias” (B). V se refere ao cupuaçu (C). E VI retoma a técnica de cruzar espécimes, e VII retoma “Holoceno” (D).</p>"},
47: {"materia": "Português", "assunto": "Interpretação de texto",
     "enunciado": enun(R, 47, trocas=[('<p class="apoio"><strong>Leia o texto para responder às questões de 46 a 49.</strong></p>', '<p class="chamada">Leia o texto para responder às questões de 46 a 49.</p>'),
                                     ("<strong>Biotecnologia Indígena</strong> Entre", "<strong>Biotecnologia Indígena</strong></p><p class=\"apoio\">Entre")]),
     "explicacao": "<p>O texto diz que a domesticação começou há 5 a 8 mil anos e que “uma segunda fase da domesticação se deu mais recentemente, nos últimos dois séculos”. Houve <strong>duas etapas</strong>. Alternativa <strong>C</strong>.</p><p>O cupuaçu não foi encontrado nas florestas primárias (A). O cupuí já existia; o cupuaçu surgiu de técnicas elaboradas, não de interferência esporádica (B). Darwin deu nome a uma prática muito anterior a ele (D). E o desmatamento só veio com os europeus (E).</p>"},
48: {"materia": "Português", "assunto": "Conectivos", "tags": ["conjunção condicional"],
     "enunciado": enun(R, 48, trocas=[('<p class="apoio"><strong>Leia o texto para responder às questões de 46 a 49.</strong></p>', '<p class="chamada">Leia o texto para responder às questões de 46 a 49.</p>'),
                                     ("<strong>Biotecnologia Indígena</strong> Entre", "<strong>Biotecnologia Indígena</strong></p><p class=\"apoio\">Entre")]),
     "alternativas": {"D": "“<strong>Se</strong> o cupuaçu não nascia ‘naturalmente’ em áreas de fraca interferência humana, era razoável supor que ele seria uma variante domesticada do cupuí...”",
                      "E": "“Antes da colonização, a Amazônia foi um centro de domesticação <strong>e</strong> modificação de espécies selvagens.”"},
     "explicacao": "<p>A conjunção <strong>“se”</strong> introduz uma condição, e a partir dela o texto levanta uma hipótese (“era razoável supor que ele seria uma variante domesticada”). Alternativa <strong>D</strong>.</p><p>“Entre” delimita um intervalo de tempo (A). “Da” liga “obra” a “mão humana”, indicando origem (B). “Que” é pronome relativo e retoma “indígenas” (C). E “e” soma ideias (E).</p>"},
49: {"materia": "Português", "assunto": "Pontuação", "tags": ["travessão"],
     "enunciado": enun(R, 49, trocas=[('<p class="apoio"><strong>Leia o texto para responder às questões de 46 a 49.</strong></p>', '<p class="chamada">Leia o texto para responder às questões de 46 a 49.</p>'),
                                     ("<strong>Biotecnologia Indígena</strong> Entre", "<strong>Biotecnologia Indígena</strong></p><p class=\"apoio\">Entre")]),
     "explicacao": "<p>O trecho entre travessões diz o que são os mateiros: “os guias locais da região amazônica”. É uma <strong>explicação</strong> do termo anterior (um aposto explicativo). Alternativa <strong>B</strong>.</p><p>O trecho não contradiz, corrige (retificação), enumera nem adverte (A, C, D e E).</p>"},
50: {"materia": "Português", "assunto": "Texto literário", "tags": ["poema"],
     "enunciado": "[[fig:1]]" + url("https://tinyurl.com/47zu6p23", "13.09.2024", "") + p("Depreende-se do poema que o processo de crescimento pressupõe"),
     "imagens": figs_q(("q50", "Poema curto de João Doederlein (@akapoeta), em versos livres e com letras minúsculas. O eu lírico se compara a uma árvore torta que cresceu num lugar que não lhe daria espaço: perdeu folhas, queimou os galhos por alcançar o sol cedo demais e chora junto com a chuva para ninguém notar. Diz que crescer é um pouco se adaptar e um pouco se aceitar, que é injusto mas necessário, e termina dizendo que suas raízes o empurram para o céu e que é uma árvore que queria ser estrela.")),
     "explicacao": "<p>O eu lírico diz que “crescer é um pouco de se adaptar / com se aceitar” e que, apesar das dificuldades, suas raízes o empurram “pro céu”. Crescer pressupõe <strong>conciliar a aceitação de si com a resiliência</strong> diante dos problemas. Alternativa <strong>B</strong>.</p><p>O poema diz que crescer “é um pouco injusto” (A). O eu lírico esconde o choro “pra ninguém perceber” (C). Não há busca por sucesso a qualquer custo (D). E ele não se resigna: quer “ser estrela” (E).</p>"},
}
completar(Q, R)
