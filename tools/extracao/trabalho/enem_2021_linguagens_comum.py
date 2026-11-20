# Enem 2021, 1º dia, caderno azul: Linguagens (questões 1 a 45 do caderno). Duas provas no site:
# enem-2021-linguagens-ingles (1–5 = inglês) e enem-2021-linguagens-espanhol (1–5 = espanhol); 6–45 iguais nas duas.
# Texto vindo do rascunho decodificado (DECOD=1, tools/enem_decod.py). Poemas e letras como imagem:
# Q2 (Benjamin Zephaniah), Q7 (Manoel de Barros), Q11 (Chico Buarque e João Bosco), Q37 (Gonzaguinha), Q38 (Hilda Hilst),
# Q39 (Nelson Sargento), Q41 (Sosígenes Costa).
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent / "tools"))
from enem_aj import carregar_enem, enunciado_enem, paragrafos_enem

D = carregar_enem("enem-2021-dia1-azul")
p = lambda *xs: "".join(f"<p>{x}</p>" for x in xs)
ap = lambda *xs: "".join(f'<p class="apoio">{x}</p>' for x in xs)
fonte = lambda x: f'<p class="fonte">{x}</p>'
tit = lambda x: f'<p class="apoio"><strong>{x}</strong></p>'
P = lambda n: paragrafos_enem(D[n])
T = lambda n, i: P(n)[i][1]
LIMPA = lambda s: re.sub(r"fi ([a-zà-ú])", r"fi\1", re.sub(r"(\w)- -(\w)", r"\1-\2", s))   # "fi " de ligadura e hífen duplicado


def figs(*pares):
    return [{"arquivo": a, "alt": t} for a, t in pares]


def corta(s, marca):
    i = s.index(marca); return s[:i].strip(), s[i:].strip()


def com_fig(n, arq, alt, enun=None):
    """Figura + referência + comando (ou enunciado próprio com [[fig:1]])."""
    if enun is None:
        par = P(n)
        enun = "[[fig:1]]" + fonte([x for t, x in par if t == "fonte"][-1]) + p([x for t, x in par if t == "p"][-1])
    return {"enunciado": enun, "imagens": figs((arq, alt))}


def Q_(n, materia, assunto, expl, tags=(), trocas=(), extra=None, alts=None):
    q = {"materia": materia, "assunto": assunto, "area": "Linguagens", "tags": list(tags), "numeroOriginal": int(str(n).split("-")[0]),
         "enunciado": enunciado_enem(D[n]), "alternativas": dict(alts or D[n]["alternativas"]), "imagens": [], "explicacao": expl}
    if extra: q.update(extra)
    e = LIMPA(q["enunciado"])
    for a, b in trocas:
        assert a in e, a; e = e.replace(a, b)
    q["enunciado"] = e
    q["alternativas"] = {k: LIMPA(re.sub(r"\s*INSTRUÇÕES PARA A REDAÇÃO.*$", "", v)) for k, v in q["alternativas"].items()}
    return q


ING = {
1: Q_(1, "Inglês", "Interpretação de texto", "<p>O texto critica o culto às celebridades: a imagem delas é fabricada por consultores, as empresas as usam para vender, e o público acredita em tudo. Mas conclui que a culpa é da sociedade: “We are the people who seemed to have lost the ability to think for ourselves”. O objetivo é <strong>ressaltar a necessidade de reflexão dos fãs</strong>. Alternativa <strong>C</strong>.</p><p>O texto diz que as celebridades não podem ser culpadas por tudo (D) e não elogia seus méritos ou o marketing (A e E).</p>",
      ["culto às celebridades"]),
2: Q_(2, "Inglês", "Interpretação de texto", "<p>O poema imita uma receita (ingredientes, “stir vigorously”, “simmer”, “serve with justice”) para contar como pictos, romanos, normandos, vikings e imigrantes de vários países formaram os britânicos. O gênero receita evidencia <strong>a riqueza da mistura cultural</strong>. Alternativa <strong>A</strong>.</p><p>O poema valoriza a mistura de povos e línguas, não uma origem geográfica (B) ou intolerância (E).</p>",
      ["poema", "multiculturalismo"],
      extra={"enunciado": tit("The British (serves 60 million)") + "[[fig:1]]" + fonte(T(2, 4)) + p(T(2, 5)),
             "imagens": figs(("q02", "Poema “The British (serves 60 million)”, de Benjamin Zephaniah, como aparece na prova, escrito como uma receita culinária: os “ingredientes” são os povos que formaram a Grã-Bretanha ao longo da história, dos antigos bretões, romanos e normandos aos imigrantes de várias partes do mundo, misturados em fogo baixo e unidos pela língua inglesa."))}),
3: Q_(3, "Inglês", "Interpretação de texto", "<p>O texto lembra que, na terra natal dos antepassados de Michelle Obama, mulheres negras eram tratadas por apelidos (“gal”, “auntie”), destinadas ao campo ou à cozinha, e “by definition, not ladies”. A ideia de uma mulher negra como primeira-dama “would have been unthinkable”: a <strong>ascensão social era improvável</strong>. Alternativa <strong>A</strong>.</p><p>“Unthinkable” se refere à primeira-dama, não à troca de nome (B) ou ao trabalho feminino (D).</p>",
      ["Michelle Obama", "racismo"],
      extra={"enunciado": tit("Becoming") + ap(T(3, 1) + " " + T(3, 2) + " " + T(3, 3)) + fonte(T(3, 4)) + p(T(3, 5))}),
4: Q_(4, "Inglês", "Interpretação de texto", "<p>No cartum, a mulher diz: “My desire to be well-informed is currently at odds with my desire to remain sane”. “At odds with” significa “em conflito com”: ela quer se informar, mas as notícias a deixam abalada. Revela a <strong>dificuldade de conciliar diferentes anseios</strong>. Alternativa <strong>B</strong>.</p><p>O cartum não fala de fontes confiáveis (A), tecnologia (C), imparcialidade (D) ou de preferir boas notícias (E).</p>",
      ["cartum", "vocabulário"],
      extra=com_fig(4, "q04", "Cartum: um casal caminha por uma rua com prédios ao fundo; a mulher diz: “My desire to be well-informed is currently at odds with my desire to remain sane.”")),
5: Q_(5, "Inglês", "Interpretação de texto", "<p>Celine diz que a beleza da Europa pode ser opressiva e que gosta de Los Angeles por ser “neutral”; Jesse acha a cidade feia. Ela diz ainda que Veneza só é romântica porque a beleza contém os instintos. Os personagens mostram que a avaliação de um lugar depende da <strong>perspectiva do visitante</strong>. Alternativa <strong>B</strong>.</p><p>A mesma cidade é vista de modos opostos, então não é a beleza do local que decide (A).</p>",
      ["roteiro de cinema", "pontos de vista"],
      trocas=[("KRIZAN, K.; LINKLATER, R. Before Sunrise: screenplay.", "KRIZAN, K.; LINKLATER, R. <em>Before Sunrise</em>: screenplay.")]),
}

ESP = {
1: Q_("1-es", "Espanhol", "Interpretação de texto", "<p>A resenha cita Lorca dizendo que “Hoy no interesa más que una problemática: lo social” e que a obra que não seguir essa direção “está condenada al fracaso”; ele também fala do “dolor del hombre” e da injustiça. A finalidade é <strong>salientar o compromisso do entrevistado com as questões sociais</strong>. Alternativa <strong>C</strong>.</p><p>A menção ao “más allá” não indica atração mística (A); o texto não fala das elites (B).</p>",
      ["García Lorca", "resenha"]),
2: Q_("2-es", "Espanhol", "Interpretação de texto", "<p>Auxilio descreve o “tono español tan peculiar” dos escritores, a “musiquilla distinta”, as zetas e ces “encircularadas” e as eses “huérfanas”: as marcas do espanhol da Espanha, diferentes do seu, uruguaio, e do mexicano. Ela reflete sobre a <strong>variação linguística do espanhol</strong>. Alternativa <strong>A</strong>.</p><p>A limpeza e a sujeira dos papéis (B e D) são o contexto, não o tema da reflexão.</p>",
      ["Roberto Bolaño", "variação linguística"], trocas=[("BOLAÑO, R. A. Tres novelas.", "BOLAÑO, R. A. <em>Tres novelas</em>.")]),
3: Q_("3-es", "Espanhol", "Interpretação de texto", "<p>O texto diz que gravações feitas por celular revelaram conversas, acordos e chantagens que derrubaram governos e empresas e até libertaram um inocente. Chamá-lo de “guillotina del siglo XXI” destaca que o celular pode <strong>assumir utilidade jurídica</strong>, como prova em processos. Alternativa <strong>E</strong>.</p><p>Reunir pessoas e organizar movimentos (B e D) são outras funções citadas, não o sentido da “guilhotina”.</p>",
      ["redes sociais", "celular"]),
4: Q_("4-es", "Espanhol", "Interpretação de texto", "<p>Na comparação “como las aguas a una piedra”, os anos “reduziram e poliram” o velho como a água desgasta uma pedra: devagar e continuamente. A analogia serve para <strong>enfatizar a ação do tempo sobre a personagem</strong>. Alternativa <strong>A</strong>.</p><p>A imagem é sobre o homem, não sobre o ambiente ou o espaço (B e D).</p>",
      ["Borges", "comparação"], trocas=[("BORGES, J. L. Artificios.", "BORGES, J. L. <em>Artificios</em>.")]),
5: Q_("5-es", "Espanhol", "Interpretação de texto", "<p>Na charge, um homem diante da TV, que mostra guerra, crise, insegurança, miséria, violência e luxo obsceno, pergunta “¡Por Dios! ¿Qué le ha pasado al mundo?”, e o outro responde: “Nosotros”. O humor está na <strong>constatação do ser humano como o responsável pela condição caótica do mundo</strong>. Alternativa <strong>A</strong>.</p><p>O “¡Por Dios!” é só exclamação, não apelo religioso (B); a TV mostra as notícias, mas a crítica não é à mídia (D e E).</p>",
      ["charge", "humor"],
      extra=com_fig("5-es", "q05es", "Charge: dois homens num bar; uma TV mostra as palavras “guerra, crisis, inseguridad, miseria, violencia, lujo obsceno”. Um deles, assustado, pergunta: “¡Por Dios! ¿Qué le ha pasado al mundo?”; o outro, lendo o jornal, responde: “Nosotros.”")),
}

C = lambda n, *a, **k: Q_(n, *a, **k)
COMUM = {
6: C(6, "Português", "Gêneros textuais", "<p>O texto acumula hipóteses sobre o que teria acontecido: “Se ele tivesse sido capturado… o impacto equivaleria”, “se caísse no continente, abriria uma cratera… e destruiria”, “se desabasse no oceano, provocaria maremotos”. A <strong>recorrência de formulações hipotéticas</strong> torna a notícia alarmante. Alternativa <strong>B</strong>.</p><p>Velocidade, distância e opinião dos astrônomos (A, C e E) são dados; “no mínimo” (D) é pontual.</p>",
     ["notícia", "hipóteses"]),
7: C(7, "Português", "Variação linguística", "<p>O poeta zomba do literato que trocou “Mário-pega-sapo” por “Mário-Captura-Sapo” para não “macular a língua”, e oferece ao dicionarista as expressões “estar na draga” e “viver na draga”, “pois que o povo já as registrou”. Ele <strong>valoriza o uso de variedades populares</strong>. Alternativa <strong>D</strong>.</p><p>O poema critica o preciosismo, não a fala popular (B e C), e não propõe regras novas (E).</p>",
     ["Manoel de Barros", "preconceito linguístico"],
     extra={"enunciado": tit("A draga") + "[[fig:1]]" + fonte(T(7, 13).replace("Gramática expositiva do chão: poesia quase toda.", "<em>Gramática expositiva do chão</em>: poesia quase toda.")) + p(T(7, 14)),
            "imagens": figs(("q07", "Fragmento do poema “A draga”, de Manoel de Barros, reproduzido da prova: a gente não sabia se a draga tinha nascido ali no Porto, como um pé de árvore ou uma duna; meia dúzia de loucos e bêbados moravam dentro dela; um deles era o amigo Mário-pega-sapo. Quando Mário morreu, um literato oficial, em necrológio caprichado, chamou-o de Mário-Captura-Sapo — “Ai que dor!” —, pois fazia-lhe nojo a forma coloquial e queria “captura” em vez de “pega” para não macular a língua. Da velha draga, abrigo de vagabundos e bêbados, restaram as expressões “estar na draga”, “viver na draga” (por estar sem dinheiro, viver na miséria), que o poeta oferece ao filólogo Aurélio Buarque de Hollanda para que as registre em seus léxicos, “pois que o povo já as registrou”."))}),
8: C(8, "Português", "Argumentação", "<p>A citação do diretor destaca que o documentário foi o único finalista feito fora do eixo Estados Unidos-Europa. Isso reforça o feito de um filme sobre um “Brasil profundo”, rodado na zona rural do Crato, ser premiado em Londres: a <strong>proeza da premiação de uma história ambientada no interior do Nordeste brasileiro</strong>. Alternativa <strong>C</strong>.</p><p>A citação não fala do museu (A), da falta de concorrentes (B) ou de investimentos (D).</p>",
     ["argumentação", "citação"], trocas=[("O documentário O menino que fez um museu,", "O documentário <em>O menino que fez um museu</em>,"), ("o diretor, O menino que fez um museu foi", "o diretor, <em>O menino que fez um museu</em> foi")]),
9: C(9, "Português", "Literatura", "<p>Os trabalhadores comentam a sorte do companheiro com ditados populares: “Quem não tem brio engorda!”, “P’ra uns, as vacas morrem… p’ra outros até boi pega a parir…”. O texto preserva a cultura pelo <strong>emprego de ditados populares que resgatam memórias e saberes coletivos</strong>. Alternativa <strong>D</strong>.</p><p>A doença é desculpa (A); as profissões não estão extintas (B); os nomes não são o ponto (C).</p>",
     ["Guimarães Rosa", "ditados populares"], trocas=[("ROSA, J. G. Sagarana.", "ROSA, J. G. <em>Sagarana</em>.")]),
10: C(10, "Português", "Gêneros textuais", "<p>As alternativas A a D descrevem fatos do filme (diretor, prêmio, personagem, câmera, enredo). Na E, dizer que premiar “uma abordagem tão ousada e radical” “não deixaria de ser um passo à frente dos votantes” traz, de forma indireta, a opinião do resenhista de que o filme merece o Oscar: <strong>opinião implícita</strong>. Alternativa <strong>E</strong>.</p>",
     ["resenha", "opinião"],
     extra={"enunciado": tit(corta(T(10, 0), "Centenas de")[0].replace("Son of Saul", "<em>Son of Saul</em>")) + ap(corta(T(10, 0), "Centenas de")[1], T(10, 1), T(10, 2), T(10, 3), T(10, 4), T(10, 5), T(10, 6)).replace("Son of Saul", "<em>Son of Saul</em>") + fonte("<em>Carta Capital</em>, n. 873, 22 out. 2015.") + p(T(10, 8).replace("Son of Saul", "<em>Son of Saul</em>"))},
     alts={k: v.replace("Son of Saul", "<em>Son of Saul</em>") for k, v in D[10]["alternativas"].items()}),
11: C(11, "Português", "Literatura", "<p>Na canção, um escravizado implora à Sinhá que não o ponha no tronco nem lhe fure os olhos, jurando que não a olhou no banho; usa “vosmecê”, “vassuncê”, e “chora em iorubá” mas “ora por Jesus”. O vocabulário e a situação <strong>remetem à violência física e simbólica contra os povos escravizados</strong>. Alternativa <strong>A</strong>.</p><p>O tema não é a influência musical (B), o sincretismo relativizado (C) ou um amor entre classes (D).</p>",
     ["Chico Buarque", "escravidão"],
     extra={"enunciado": tit("Sinhá") + "[[fig:1]]" + fonte(T(11, 2).replace("Chico.", "<em>Chico</em>.")) + p(T(11, 3)),
            "imagens": figs(("q11", "Trecho da letra “Sinhá”, de Chico Buarque e João Bosco, como aparece na prova: um homem escravizado nega ter visto a dona se banhar, diz que estava na roça, pergunta por que vão castigá-lo no tronco e cegá-lo, e conta que chora em iorubá, mas reza a Jesus."))}),
12: C(12, "Português", "Gêneros textuais", "<p>A peça mostra metade de uma garrafa PET e metade de um cachorro, com os textos “Esse pet é descartável. Esse não.” e “Abandono é crime”. O jogo com a palavra “pet” (o plástico e o animal) busca <strong>sensibilizar o público em relação ao abandono de animais domésticos</strong>. Alternativa <strong>D</strong>.</p><p>A lei é citada, mas o foco é a comparação que comove, não a sanção (E).</p>",
     ["campanha", "abandono de animais"],
     extra=com_fig(12, "q12", "Peça de campanha: uma imagem dividida ao meio — metade de uma garrafa PET e metade de um cachorro. Textos: “Esse pet é descartável. Esse não.” e “Abandono é crime. Lei Federal nº 9.605/98”.")),
13: C(13, "Português", "Gêneros textuais", "<p>A Graúna, de Henfil, anuncia que, quando o neném nascer, renunciará aos prazeres, à vida folgazã, à beleza física, à vida social e aos projetos individuais, e conclui: “Assim termina mais um capítulo na luta da mulher por sua emancipação…”. A tirinha quer <strong>ironizar as condições de igualdade</strong>: a maternidade ainda exigia que a mulher abrisse mão de si. Alternativa <strong>C</strong>.</p><p>A frase final é irônica: não reforça a luta (A) nem a autonomia (B).</p>",
     ["Henfil", "ironia"],
     extra=com_fig(13, "q13", "Tirinha de Henfil em seis quadros, no sertão com cactos: a Graúna diz “Quando neném nascer, renunciarei aos prazeres mundanos…”; depois “Renunciarei à vida folgazã, renunciarei à busca da beleza física!”; “Renunciarei à vida social! Renunciarei aos projetos individualistas!”; num quadro fica em silêncio e, no último, conclui: “Assim termina mais um capítulo na luta da mulher por sua emancipação…”.")),
14: C(14, "Artes", "Arte contemporânea", "<p>A reportagem apresenta a escultura de refugiados numa balsa no fundo do mar e diz que “a imagem é tão forte que dispensa qualquer palavra. Exatamente o papel da arte”. Ela chama a atenção para <strong>a arte como perpetuadora de episódios marcantes da humanidade</strong>, que precisam ser lembrados para não se repetir. Alternativa <strong>E</strong>.</p><p>O museu não foi feito como memorial (D), e o foco não é o turismo ou a inovação (A e C).</p>",
     ["Jason de Caires Taylor", "refugiados"],
     extra={"enunciado": tit(T(14, 0)) + "[[fig:1]]" + fonte(T(14, 2).replace("A balsa de Lampedusa.", "<em>A balsa de Lampedusa</em>.")) + ap(T(14, 3).replace("A balsa de Lampedusa,", "<em>A balsa de Lampedusa</em>,"), T(14, 4), T(14, 5), T(14, 6)) + fonte(T(14, 7)) + p(T(14, 8).replace("obra A balsa de Lampedusa", "obra <em>A balsa de Lampedusa</em>")),
            "imagens": figs(("q14", "Escultura submersa “A balsa de Lampedusa”: um bote de borracha com dez figuras humanas, adultos e crianças, de expressão abatida, no fundo do mar."))}),
15: C(15, "Artes", "Música", "<p>Pestana quer compor obras clássicas, na sala cheia de retratos de Mozart, mas só consegue escrever polcas dançantes, que fazem sucesso nas ruas. O conflito do personagem representa a <strong>tensa relação entre o erudito e o popular na constituição da música brasileira</strong>. Alternativa <strong>D</strong>.</p><p>O conto não diz que a música popular é simples (A) nem fala de referências africanas predominantes (B).</p>",
     ["Machado de Assis", "maxixe"], trocas=[("ASSIS, M. Um homem célebre.", "ASSIS, M. <em>Um homem célebre</em>."), ("WISNIK, J. M. Machado maxixe: o caso Pestana.", "WISNIK, J. M. <em>Machado maxixe</em>: o caso Pestana.")]),
16: C(16, "Português", "Argumentação", "<p>O artigo critica a pressa e a comunicação vazia e cita a letra de “Sinal fechado”, em que dois conhecidos se encontram num sinal e trocam frases rápidas e superficiais. A canção <strong>exemplifica o fato criticado no texto com uma situação concreta</strong>. Alternativa <strong>B</strong>.</p><p>A letra mostra o problema; a solução (o <em>slow life</em>) vem depois, no texto (E).</p>",
     ["Paulinho da Viola", "exemplificação"], trocas=[("à cultura fast,", "à cultura <em>fast</em>,"), ("o movimento slow life,", "o movimento <em>slow life</em>,")]),
17: C(17, "Educação Física", "Esporte e sociedade", "<p>O texto mostra o racismo no futebol: os negros Barbosa e Bigode foram culpados pela derrota de 1950, e Paulo César Lima foi chamado de “jogador-problema” por não aceitar o papel de “bom negro”. A <strong>atitude contestadora de um “jogador-problema”</strong> enfraqueceu o mito da democracia racial, ao expor o racismo. Alternativa <strong>E</strong>.</p><p>A culpa dada a Barbosa e Bigode (A) mostra o racismo, mas o texto atribui a quebra do mito à contestação.</p>",
     ["racismo no futebol", "democracia racial"]),
18: C(18, "Artes", "Pintura", "<p>“Moema”, de Victor Meirelles, mostra a índia morta na praia, com o corpo belo e sensual, numa cena trágica tirada do poema “Caramuru”. O Romantismo aparece na <strong>representação dramática e idealizada do corpo da índia</strong>. Alternativa <strong>D</strong>.</p><p>A beleza não é retrato fiel (A), e o tema central não é a fragilidade humana (B).</p>",
     ["Victor Meirelles", "Romantismo"],
     extra={"imagens": figs(("q18", "Pintura “Moema”, de Victor Meirelles: uma índia nua, morta, deitada de costas na areia, à beira-mar, com os cabelos longos espalhados; ao fundo, o mar e algumas figuras pequenas na praia."))},
     trocas=[("MEIRELLES, V. Moema.", "MEIRELLES, V. <em>Moema</em>."), ("cena de Caramuru,", "cena de <em>Caramuru</em>,")]),
19: C(19, "Educação Física", "Lazer", "<p>As crianças de hoje brincam menos, mais em casa, muitas vezes sozinhas e com aparelhos eletrônicos, num jogo individual com a máquina. As mudanças <strong>promoveram uma vivência corporal menos ativa</strong>. Alternativa <strong>D</strong>.</p><p>O texto mostra menos convívio, menos lazer e menos tempo para brincar (contra A, B e E).</p>",
     ["infância", "brincadeiras"]),
20: C(20, "Artes", "Dança", "<p>Mini@tures junta corpo, dança, computação gráfica e internet: “a graça das miniaturas está justamente na contaminação entre mídias”. É inovador por <strong>produzir uma arte multimodal, com o intuito de ampliar as possibilidades de expressão estética</strong>. Alternativa <strong>D</strong>.</p><p>O corpo do bailarino continua presente (contra C), e o texto não fala de financiamento (B).</p>",
     ["dança e tecnologia"],
     extra={"enunciado": ap(T(20, 0)) + "[[fig:1]]" + ap(T(20, 2).replace("Mini@tures é", "<em>Mini@tures</em> é").replace("Mini@tures explora", "<em>Mini@tures</em> explora")) + fonte(T(20, 3)) + p(T(20, 4)),
            "imagens": figs(("q20", "Dezesseis pequenos quadros em preto e branco com silhuetas de um bailarino em diferentes movimentos e cenários."))}),
21: C(21, "Português", "Argumentação", "<p>O texto I diz que os estoques de água doce são inesgotáveis, repostos sempre pelo ciclo hidrológico. O texto II diz que o lago do reservatório não alimenta os aquíferos, que por isso “não conseguem recuperar seu nível”. Divergem sobre a possibilidade de <strong>manter os estoques de água doce</strong>. Alternativa <strong>A</strong>.</p>",
     ["recursos hídricos", "textos em diálogo"],
     extra={"enunciado": tit("TEXTO I") + tit("O mito da estiagem em São Paulo") + ap(T(21, 1), T(21, 2)) + fonte(T(21, 3)) + tit("TEXTO II") + ap(T(21, 5), T(21, 6)) + fonte(T(21, 7)) + p(T(21, 8))}),
22: C(22, "Português", "Variação linguística", "<p>O texto mostra o “você” e o “tu” convivendo, com usos diferentes conforme a região e a época. A possibilidade de usar os dois <strong>caracteriza a diversidade da língua</strong>. Alternativa <strong>B</strong>.</p><p>O uso não depende só da idade (A), o “tu” não é usado em todo o país (C) e a língua muda, não se mantém (E).</p>",
     ["pronomes de tratamento", "variação regional"]),
23: C(23, "Artes", "Dança", "<p>John Lennon da Silva dançou “A morte do cisne”, coreografia do balé clássico, com o estilo <em>popping</em> da <em>street dance</em>, de jeans e tênis. A releitura mostra que <strong>a criação artística é beneficiada pelo encontro de modelos oriundos de diferentes realidades socioculturais</strong>. Alternativa <strong>B</strong>.</p><p>A versão não reforça hierarquias (C) nem limita o artista (D).</p>",
     ["balé e dança urbana"], trocas=[("O solo A morte do cisne,", "O solo <em>A morte do cisne</em>,"), ("o estilo popping da street dance", "o estilo <em>popping</em> da <em>street dance</em>"), ("inovadora de A morte do cisne,", "inovadora de <em>A morte do cisne</em>,")],
     alts=D[23]["alternativas"]),
24: C(24, "Português", "Literatura", "<p>O narrador descreve o preso que apanhou dezenas de vezes, teve ossos quebrados, foi jogado de uma laje e deixado para morrer, sem saber por quê, e agora só obedece. A ficção <strong>traz à tona atitudes de um estado de exceção</strong>, em que a lei não protege e a violência é arbitrária. Alternativa <strong>B</strong>.</p><p>O texto não usa o absurdo (E) e denuncia, não perpetua, o senso comum (A).</p>",
     ["Ana Paula Maia", "violência"], trocas=[("Assim na terra como embaixo da terra.", "<em>Assim na terra como embaixo da terra</em>.")]),
25: C(25, "Português", "Literatura", "<p>O delegado intimida o vizinho, que ele toma por estrangeiro (“gringo”), com ameaças exageradas e gírias (“dura lex”, “Morou?”, “vai tudo em cana”), até ser surpreendido pela resposta firme da esposa. O exagero do discurso confere à narrativa um <strong>tom anedótico</strong>. Alternativa <strong>B</strong>.</p><p>A hostilidade (D) existe, mas é tratada com humor, como num caso contado.</p>",
     ["Fernando Sabino", "humor"], trocas=[("In: Os melhores contos.", "In: <em>Os melhores contos</em>.")]),
26: C(26, "Português", "Coesão e coerência", "<p>“O gigante do Brasil”, no hino, refere-se a Dom Pedro II; depois, “O Pedro mencionado” retoma exatamente esse Pedro. Há <strong>interdependência entre “O gigante do Brasil” e “O Pedro mencionado”</strong>. Alternativa <strong>D</strong>.</p><p>“O bruxo do Cosme Velho” (E) retoma Machado de Assis, não Dom Pedro II.</p>",
     ["coesão referencial"]),
27: C(27, "Artes", "Design", "<p>O texto diz que os móveis criados sob influência de Brasília abandonaram o gosto rebuscado e adotaram “linhas retas e curvas suaves”. Nas cadeiras de Sérgio Rodrigues, a estética brasiliense <strong>surge na simplificação das informações visuais de cada composição</strong>. Alternativa <strong>E</strong>.</p><p>Há linhas retas e curvas (contra A); o rebuscado foi abandonado (B); os materiais variam (D).</p>",
     ["design de móveis", "Brasília"],
     extra={"enunciado": "[[fig:1]]" + fonte("RODRIGUES, S. Acervo pessoal.") + ap(T(27, 1).split("Acervo pessoal. ", 1)[1]) + fonte(T(27, 2)) + p(T(27, 3)),
            "imagens": figs(("q27", "Fotografia de três peças de mobiliário de Sérgio Rodrigues: uma cadeira de madeira com assento e encosto retos, uma poltrona de linhas retas com assento estofado e outra poltrona de madeira com encosto de palhinha."))}),
28: C(28, "Português", "Tecnologia e comunicação", "<p>O Facebook muda o design para valorizar os Grupos, porque mais de 1 bilhão de usuários já entram nessa aba, e para dar mais atenção ao Marketplace. As mudanças acompanham o que os usuários fazem: as tecnologias <strong>assimilam os comportamentos dos usuários</strong>. Alternativa <strong>B</strong>.</p><p>O texto não fala de privacidade (A) nem de lucro como motivo (D).</p>",
     ["redes sociais", "design"], trocas=[("polêmico feed de notícias", "polêmico <em>feed</em> de notícias"), ("sai o feed, entra", "sai o <em>feed</em>, entra")]),
29: C(29, "Português", "Argumentação", "<p>O autor diz que não basta ler para estar informado: é preciso “conhecer as entrelinhas”, “ter um pé atrás”, investigar e procurar “os elementos ocultos” de uma notícia. Ele quer convencer os leitores a <strong>adotarem uma postura crítica em relação às informações recebidas</strong>. Alternativa <strong>C</strong>.</p><p>O texto diz que não existe isenção absoluta (contra A e E).</p>",
     ["leitura crítica", "mídia"], trocas=[("cunhou o slogan", "cunhou o <em>slogan</em>")]),
30: C(30, "Português", "Variação linguística", "<p>Pelino corrige “asseguro” em plena conversa na botica, interrompendo o papo com regras gramaticais. Ele aplica a norma-padrão a qualquer conversa, sem distinguir situações: <strong>desconsidera diferentes níveis de formalidade nas situações de comunicação</strong>. Alternativa <strong>E</strong>.</p><p>Ele é rígido, não complacente (C), e defende, não invalida, a gramática normativa (D).</p>",
     ["Lima Barreto", "purismo"], trocas=[("BARRETO, L. A Nova Califórnia.", "BARRETO, L. <em>A Nova Califórnia</em>.")]),
31: C(31, "Educação Física", "Práticas de aventura", "<p>O uretano deu mais aderência às rodas e “possibilitou a um maior número de pessoas inexperientes começar a prática”, o que trouxe campeonatos, marcas e lojas. Esses fatores <strong>contribuíram para a democratização do skate</strong>. Alternativa <strong>A</strong>.</p><p>O skate não substituiu o surfe (D); a profissão não é o tema (C).</p>",
     ["skate", "história do esporte"]),
32: C(32, "Português", "Funções da linguagem", "<p>Na crônica, o narrador fala de si: lembra o estojo da infância, o cheiro que o “tonteava de prazer”, acha o notebook “abominável” e conclui: “Acho que piorei de estojo e de vida”. Predomina a função emotiva, que põe em foco o <strong>enunciador, buscando expressar sua atitude em relação ao conteúdo do enunciado</strong>. Alternativa <strong>D</strong>.</p>",
     ["Carlos Heitor Cony", "função emotiva"],
     extra={"enunciado": tit("Estojo escolar") + ap(corta(T(32, 0), "Rio de Janeiro")[1], T(32, 1), T(32, 2), T(32, 3), T(32, 4), T(32, 5)) + fonte(T(32, 6).replace("Crônicas para ler na escola.", "<em>Crônicas para ler na escola</em>.")) + p(T(32, 7))}),
33: C(33, "Português", "Gêneros textuais", "<p>Os quadrinhos contam como o livro foi feito (pesquisa, roteiro, desenho à tinta, edição digital) e terminam: “Depois de todo trabalho, este livro só precisa de mais uma coisa: ser lido”. Funcionam como prefácio pela <strong>função de apresentação do livro</strong> ao leitor. Alternativa <strong>A</strong>.</p><p>O processo de criação (C e D) é o conteúdo, mas o que faz dele um prefácio é apresentar a obra.</p>",
     ["prefácio", "quadrinhos"],
     extra=com_fig(33, "q33", "Quadrinhos: “A pesquisa foi o primeiro passo na produção deste livro” (uma senhora diz: “Deixa de drama, a maior parte do material está on-line”); “seguida da seleção das informações e da elaboração de um roteiro”; “o desenho feito à tinta” (“Não olha ainda!”); “e depois editado e colorizado digitalmente”; “Depois de todo trabalho, este livro só precisa de mais uma coisa: ser lido.”, com duas mulheres lendo o livro.")),
34: C(34, "Português", "Gêneros textuais", "<p>O infográfico mostra os riscos do celular antes de dormir para crianças (falta de hormônios, obesidade, problemas de atenção) e termina com “O que fazer?”: ficar sem telas antes de dormir, reduzir a luz, deixar o telefone longe. O objetivo é <strong>influenciar o leitor a mudar atitudes e hábitos considerados prejudiciais às crianças</strong>. Alternativa <strong>B</strong>.</p><p>Há dados de estudo, mas o foco é a mudança de comportamento (A); não se fala de exercícios (C).</p>",
     ["infográfico", "saúde infantil"],
     extra=com_fig(34, "q34", "Infográfico “Os riscos para crianças do uso do celular antes de dormir”: estudo do King’s College conclui que essas crianças e adolescentes têm maior risco de obesidade, baixo sistema imunológico, crescimento atrofiado e depressão. A falta de sono reduz hormônios (melatonina, leptina, GH, cortisol); a luz forte confunde o relógio biológico; os estímulos deixam o cérebro em alerta; a criança demora a dormir e descansa menos, com problemas de comportamento, de atenção e de memória. “O que fazer?”: ficar entre 30 minutos e 2 horas sem telas antes de dormir; reduzir a intensidade da luz; manter o telefone longe, porque no quarto a expectativa de mensagens atrapalha o sono.")),
35: C(35, "Português", "Literatura", "<p>Os homens definem a mulher pelo estado civil (“Está viúva?”, “o marido ainda vive?”, “Não é casada”, “Solteira? Assim, assim”), pela idade e pela aparência, e por exclusão de profissões (“vá excluindo as profissões e chegará lá”). A mulher <strong>tem sua identidade e seu lugar referendados pelo homem</strong>. Alternativa <strong>D</strong>.</p>",
     ["Machado de Assis", "condição feminina"]),
36: C(36, "Artes", "Arte contemporânea", "<p>Hazoumé transforma galões de plástico descartados em máscaras, que não foram feitas para serem usadas, mas para mostrar as formas humanas do lixo e denunciar seu acúmulo. A obra denota o <strong>reposicionamento estético de objetos por meio da mudança de função</strong>. Alternativa <strong>B</strong>.</p><p>A combinação de materiais não empobrece a arte (A), e a obra não pede interação (C).</p>",
     ["Romuald Hazoumé", "ready-made"],
     extra={"imagens": figs(("q36", "Máscara feita com um galão plástico branco cortado, com a boca do galão parecendo um nariz, e tiras de tecido colorido estampado caindo como cabelos."))},
     trocas=[("HAZOUMÉ, R. Nanawax.", "HAZOUMÉ, R. <em>Nanawax</em>."), ("FARTHING, S. Tudo sobre arte.", "FARTHING, S. <em>Tudo sobre arte</em>.")]),
37: C(37, "Português", "Literatura", "<p>A canção dá “conselhos” ao trabalhador: sorrir, rezar pelo patrão, esquecer o desemprego, baixar a cabeça, agradecer e obedecer “pelo bem da nação”, em troca de um “fuscão no juízo final”. Composta na ditadura, a letra quer <strong>ironizar a incorporação de ideias e atitudes conformistas</strong>. Alternativa <strong>A</strong>.</p><p>Ela não defende deveres cívicos (B); critica, não propõe, a indiferença (E).</p>",
     ["Gonzaguinha", "ironia"],
     extra={"enunciado": tit("Comportamento geral") + "[[fig:1]]" + fonte(T(37, 5).replace("Luiz Gonzaga Jr.", "<em>Luiz Gonzaga Jr.</em>")) + p(T(37, 6)),
            "imagens": figs(("q37", "Trecho da letra “Comportamento geral”, de Gonzaguinha, como aparece na prova, em quatro estrofes: em tom irônico, a canção “ensina” o trabalhador a mostrar sempre alegria, rezar pelo patrão, esquecer o desemprego, baixar a cabeça, agradecer e obedecer a tudo, com a promessa de um prêmio no juízo final."))}),
38: C(38, "Português", "Literatura", "<p>O eu lírico pede ao outro que mande dizer “É lua cheia. A casa está vazia”, para que ele volte; lembra o brilho das marés, os peixes rosados e os pés molhados, e imagina voltar “revestida de luz”. O desejo remete ao <strong>sonho de autorrealização desenhado pela memória</strong>. Alternativa <strong>C</strong>.</p><p>Não há ceticismo (A), tédio do eu lírico (B) ou julgamento (D).</p>",
     ["Hilda Hilst", "lirismo"],
     extra={"enunciado": "[[fig:1]]" + fonte(T(38, 1).replace("Júbilo, memória, noviciado da paixão.", "<em>Júbilo, memória, noviciado da paixão</em>.")) + p(T(38, 2)),
            "imagens": figs(("q38", "Poema de Hilda Hilst, como aparece na prova: o eu lírico pede à pessoa amada que mande avisar, com um sinal ligado à lua e à casa vazia, quando puder voltar; evoca as marés, peixes rosados e pés molhados, e diz que voltaria a vê-la revestida de luz."))}),
39: C(39, "Português", "Variação linguística", "<p>Marcas informais típicas da fala aparecem em “deita logo <strong>falação</strong>” (palavra coloquial) e em “vai <strong>pros bailes</strong>” (contração de “para os”). Alternativa <strong>A</strong>.</p><p>“Você”, “teatro de revista”, “perfeito”, “Carnaval”, “oculista”, “curar” e “falso moralista” são palavras comuns também na norma-padrão (B a E).</p>",
     ["Nelson Sargento", "coloquialismo"],
     extra={"enunciado": tit("Falso moralista") + "[[fig:1]]" + fonte("NELSON SARGENTO. <em>Sonho de um sambista</em>. São Paulo: Eldorado, 1979.") + p(T(39, 4).split("1979. ", 1)[1]),
            "imagens": figs(("q39", "Letra “Falso moralista”, de Nelson Sargento, como aparece na prova, em quatro estrofes: o eu lírico acusa alguém que condena a juventude, o teatro de revista e a arte moderna, mas vai a bailes, deixa a companheira para beber com os amigos e falta ao trabalho para curar a ressaca; por isso o chama de falso moralista."))}),
40: C(40, "Português", "Literatura", "<p>O narrador descreve Alda, internada e esquecida num hospital psiquiático, com imagens poéticas: ela é uma princesa refugiada num palácio, “chegada pelos caminhos da dor”, uma criança que brinca na areia. A percepção é <strong>alimentada pela imersão lírica no espaço da segregação</strong>. Alternativa <strong>C</strong>.</p><p>O tom é amoroso, não irônico (A) ou resignado (B).</p>",
     ["Maura Lopes Cançado", "lirismo"],
     extra={"enunciado": tit("Introdução a Alda") + ap(corta(T(40, 0), "Dizem que")[1], T(40, 1)) + fonte(T(40, 2).replace("O sofredor do ver.", "<em>O sofredor do ver</em>.")) + p(T(40, 3))}),
41: C(41, "Português", "Literatura", "<p>O pavão vermelho é a alegria, que pousa “como um sol” no joelho do eu lírico, supera os outros pavões, é “festa de púrpura” e “o próprio doge” (soberano). Depois dele, “os meus outros pavões foram-se embora”. A imagem <strong>metaforiza a conquista de sua plena realização</strong>. Alternativa <strong>D</strong>.</p><p>“A cor vermelha chega a ser sonora” é uma sinestesia (C), mas é um detalhe, não o sentido da imagem.</p>",
     ["Sosígenes Costa", "soneto"],
     extra={"enunciado": tit("O pavão vermelho") + "[[fig:1]]" + fonte(T(41, 4).replace("Poesia completa: Sosígenes Costa.", "<em>Poesia completa</em>: Sosígenes Costa.")) + p(T(41, 5)),
            "imagens": figs(("q41", "Soneto “O pavão vermelho”, de Sosígenes Costa, como aparece na prova: a alegria é comparada a um pavão vermelho que passou a morar no quintal do eu lírico, descrito com imagens de sol, aurora, púrpura e fogo; a cor chega a parecer sonora, e os pavões de outras cores que ele tivera foram embora."))}),
42: C(42, "Educação Física", "Corpo e sociedade", "<p>O texto diz que a sociedade inventa e reinventa o corpo segundo os valores de cada época, e a obra mostra a mulher sensual da propaganda dos anos 1960. A erotização do corpo feminino tem sido constituída pela <strong>educação do gesto, da vontade e do comportamento</strong>: aprendemos como o corpo deve se mostrar. Alternativa <strong>C</strong>.</p><p>Exercícios, medicamentos e espaços (A, B e D) são meios específicos, não a construção cultural de que fala o texto.</p>",
     ["Pop Art", "corpo feminino"],
     extra={"imagens": figs(("q42", "Pintura “Garota com bola”, de Roy Lichtenstein, em estilo de história em quadrinhos: uma jovem de maiô, sorrindo, com os braços erguidos segurando uma bola de praia sobre a cabeça."))},
     trocas=[("LICHTENSTEIN, R. Garota com bola.", "LICHTENSTEIN, R. <em>Garota com bola</em>."), ("artístico Pop Art,", "artístico <em>Pop Art</em>,")]),
43: C(43, "Artes", "Quadrinhos", "<p>Nos quadrinhos de “Cumbe”, escravizados lembram o calunga (o mar) que os separou da África e um deles diz: “Nanã, se a gente beber a nsanga e enfrentar o calunga, podemos ficar juntos lá na outra terra”. A cena une lirismo e violência ao <strong>acentuar a resistência identitária dos povos escravizados</strong>, que mantêm sua língua e suas crenças. Alternativa <strong>D</strong>.</p><p>Os afetos e a ancestralidade se mantêm, apesar do exílio (contra A e E).</p>",
     ["Marcelo D’Salete", "escravidão"],
     extra={"enunciado": "[[fig:1]]" + fonte("D’SALETE, M. <em>Cumbe</em>. São Paulo: Veneta, 2018, p. 10-11 (adaptado).") + p(T(43, 1).split("(adaptado). ", 1)[1]),
            "imagens": figs(("q43", "Seis quadros em preto e branco: pessoas negras escravizadas num canavial e numa senzala; uma legenda diz “O tata contou sobre o calunga, o mar que não acaba”; um homem diz a uma mulher: “Nanã, se a gente beber a nsanga e enfrentar o calunga, podemos ficar juntos lá na outra terra”; nos últimos quadros, “Longe daqui” e “Longe disso tudo”."))}),
44: C(44, "Português", "Literatura", "<p>O narrador conta que a matraca anunciava que um vereador educava cobras e macacos, o que era “perfeitamente falso”, mas as pessoas juravam ter visto cascavéis dançando no peito dele, “só devida à absoluta confiança no sistema”. A matraca se associa à disseminação de <strong>informações não fidedignas</strong>. Alternativa <strong>D</strong>.</p><p>A matraca anunciava também produtos e serviços (B e E), mas a ironia está na mentira aceita como verdade.</p>",
     ["Machado de Assis", "ironia"], trocas=[("ASSIS, M. O alienista.", "ASSIS, M. <em>O alienista</em>.")]),
45: C(45, "Artes", "Música", "<p>A autora diz que o choro é “riquíssima manifestação da genuína alma brasileira”, lembra Abel Ferreira, sua sonoridade “ímpar”, seus parceiros e o acervo guardado, e cita a falta de incentivo e de divulgação. Os argumentos buscam <strong>destacar a relevância histórica e a riqueza estética do choro</strong>. Alternativa <strong>C</strong>.</p><p>A falta de divulgação nas escolas é citada por Leonor Bianchi (A), mas não é o objetivo do texto.</p>",
     ["choro", "Abel Ferreira"],
     extra={"enunciado": ap(T(45, 0).replace("Chorando baixinho (1942)", "<em>Chorando baixinho</em> (1942)").replace("Ingênuo (1958)", "<em>Ingênuo</em> (1958)"), T(45, 1).replace("Revista do Choro", "<em>Revista do Choro</em>")) + fonte(T(45, 2)) + p(T(45, 3))}),
}


def montar(lingua):
    Q = dict(ING if lingua == "ingles" else ESP)
    Q.update(COMUM)
    return Q
