# Enem 2014, 2º dia, caderno azul: Linguagens (questões 91 a 135; no site, 1 a 45). Em 2014 Linguagens e Matemática eram no 2º dia.
# Duas provas: enem-2014-linguagens-ingles (91–95 = inglês) e enem-2014-linguagens-espanhol (91–95 = espanhol); 96–135 iguais.
# Letras e poemas modernos como imagem (alt descreve, não transcreve): Q92 (Bob Dylan), Q95-es (Circe Maia), Q108 (Manuel Bandeira),
# Q128 (Geir Campos), Q129 (Antônio de Barros).
# Em texto, domínio público: Q93 (Robert Frost, 1916), Q113 (Gregório de Matos), Q119 (Augusto dos Anjos), Q124 (Cruz e Sousa).
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent / "tools"))
from enem_aj import carregar_enem, enunciado_enem, paragrafos_enem

D = carregar_enem("enem-2014-dia2-azul")
p = lambda *xs: "".join(f"<p>{x}</p>" for x in xs)
ap = lambda *xs: "".join(f'<p class="apoio">{x}</p>' for x in xs)
fonte = lambda x: f'<p class="fonte">{x}</p>'
tit = lambda x: f'<p class="apoio"><strong>{x}</strong></p>'
P = lambda n: paragrafos_enem(D[n])
T = lambda n, i: P(n)[i][1]
LIMPA = lambda s: re.sub(r"fi ([a-zà-ú])", r"fi\1", re.sub(r"fl ([a-zà-ú])", r"fl\1", re.sub(r"(\w)- -(\w)", r"\1-\2", s)))


def figs(*pares):
    return [{"arquivo": a, "alt": t} for a, t in pares]


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




ALT = lambda ini: {k: f"[[fig:{i}]]" for i, k in enumerate("ABCDE", ini)}
LET = lambda *ls: "<br>".join(ls)
EM = lambda s, *ws: [s := s.replace(w, f"<em>{w}</em>") for w in ws][-1] if ws else s


SON = lambda *estrofes: ap(*["<br>".join(e.split(" / ")) for e in estrofes])

ING = {
1: Q_(91, "Inglês", "Interpretação de texto", "<p>“A tall order” é uma tarefa difícil, e “the sky isn’t the limit” brinca com a expressão “o céu é o limite”, já que o arquiteto quer construir o primeiro arranha-céu invisível. O texto explica como a Infinity Tower, em Seul, vai “desaparecer” projetando na fachada a imagem do que está atrás dela. O tema são as <strong>inovações tecnológicas usadas para a construção de um novo arranha-céu em Seul</strong>. Alternativa <strong>A</strong>.</p><p>Wee rejeita justamente a competição pelo prédio mais alto (D).</p>",
      ["título", "expressão idiomática"],
      extra={"enunciado": tit("A Tall Order") + ap("<em>" + T(91, 1) + "</em>", T(91, 2), T(91, 3), T(91, 4), T(91, 5), T(91, 6)) + fonte(T(91, 7)) + p(T(91, 8).replace("expressões A Tall Order e The sky isn’t the limit", "expressões <em>A Tall Order</em> e <em>The sky isn’t the limit</em>"))}),
2: Q_(92, "Inglês", "Interpretação de texto", "<p>A canção se dirige aos “masters of war”, os que fabricam armas, bombas e aviões, se escondem atrás de mesas e põem uma arma na mão do jovem. O eu lírico diz que eles constroem para destruir e mentem que uma guerra mundial pode ser vencida. O protesto é contra <strong>o sistema que recruta soldados para guerras motivadas por interesses econômicos</strong>. Alternativa <strong>C</strong>.</p><p>A crítica não é aos soldados (B), que recebem a arma, mas a quem lucra com a guerra.</p>",
      ["canção", "protesto"],
      extra=com_fig(92, "q92", "Letra de “Masters of War”, de Bob Dylan, em inglês, como aparece na prova: o eu lírico se dirige aos que fabricam armas, bombas e aviões de guerra e se escondem atrás de muros e mesas, acusa-os de construir só para destruir, de pôr uma arma em sua mão e fugir quando as balas voam, e os compara a Judas por mentirem que uma guerra mundial pode ser vencida.",
                    enun="[[fig:1]]" + fonte("BOB DYLAN. <em>The Freewheelin’ Bob Dylan</em>. Nova York: Columbia Records, 1963 (fragmento).") + p("Na letra da canção <em>Masters of War</em>, há questionamentos e reflexões que aparecem na forma de protesto contra"))),
3: Q_(93, "Inglês", "Interpretação de texto", "<p>Diante de dois caminhos, o eu lírico escolheu “the one less traveled by”, o menos percorrido, e diz que isso “has made all the difference”. Na metáfora da vida como viagem, ele <strong>festeja o fato de ter sido ousado na escolha que fez</strong>. Alternativa <strong>A</strong>.</p><p>Ele não lamenta (B) nem diz que viaja pouco (C): fala de uma escolha decisiva.</p>",
      ["poema", "metáfora"],
      extra={"enunciado": tit("The Road Not Taken (by Robert Frost)") + ap("Two roads diverged in a wood, and I —<br>I took the one less traveled by,<br>And that has made all the difference.") + fonte(T(93, 1))
             + p(T(93, 2).replace("poema The Road Not Taken", "poema <em>The Road Not Taken</em>"))}),
4: Q_(94, "Inglês", "Interpretação de texto", "<p>No site, Kate Watts escolheu compartilhar “a sushi platter”, que costuma pagar 20 dólares, e ao lado aparece “If you share, you will feed 240 children” e o botão “Feed them now”. O WeFeedback recebe o valor de uma comida para alimentar crianças: ela <strong>fez doação para caridade</strong>. Alternativa <strong>C</strong>.</p><p>Ela não comprou comida (A): o valor do prato vira doação.</p>",
      ["site", "solidariedade"],
      extra=com_fig(94, "q94", "Página do site WeFeedback (“sharing food, changing lives”), com o contador de refeições doadas e um formulário em inglês: “My name is… Kate Watts”, “I want to share… a sushi platter”, “I usually pay… 20 $ (USD)”, “More servings will feed more children… 3”, total de $60.00. Ao lado, uma caneca diz “If you share, you will feed 240 children” e um botão “Feed them now”.",
                    enun="[[fig:1]]" + fonte(T(94, 1)) + p(T(94, 2).replace("o site WeFeedback", "o <em>site</em> WeFeedback")))),
5: Q_(95, "Inglês", "Interpretação de texto", "<p>Segundo o texto, o Globish é “a sort of English lite”, “a means of simplifying the language and giving it rules so it can be understood by all”. Seu criador diz que não é uma língua nem carrega cultura, só serve para comunicar. É uma variedade que <strong>altera a estrutura do idioma para possibilitar a comunicação internacional</strong>. Alternativa <strong>D</strong>.</p><p>O falante nativo justamente não entende o Globish (B), e o criador nega que ele seja como o esperanto (C).</p>",
      ["Globish", "variação linguística"],
      extra={"enunciado": tit("If You Can’t Master English, Try Globish") + ap(T(95, 0).replace("If You Can’t Master English, Try Globish ", ""), T(95, 1), T(95, 2), T(95, 3)) + fonte(T(95, 4))
             + p(T(95, 5).replace("o Globish (Global English)", "o <em>Globish</em> (<em>Global English</em>)"))},
      alts={**D[95]["alternativas"], "A": "tem <em>status</em> de língua por refletir uma cultura global.", "E": "apresenta padrões de fala idênticos aos da variedade usada pelos falantes nativos."}),
}

ESP = {
1: Q_("91-es", "Espanhol", "Interpretação de texto", "<p>O cartaz diz “Las mujeres <strong>podemos</strong> lactar durante el embarazo y en tándem, siendo una práctica natural y respetuosa con <strong>nuestros</strong> hijos”. Quem fala se coloca entre as mulheres que amamentam, como uma delas: as marcas de primeira pessoa do plural <strong>promovem uma identificação entre o enunciador e o leitor para aproximá-los</strong>. Alternativa <strong>D</strong>.</p><p>O tom é próximo e informal, e não formal (A) ou impositivo (B).</p>",
      ["campanha", "pessoa do discurso"],
      extra=com_fig("91-es", "q91es", "Cartaz da associação Azaral com o título “Lactancia durante el embarazo y en tándem” sobre a foto de uma mulher grávida, de biquíni, amamentando uma criança pequena na praia. Embaixo: “Las mujeres podemos lactar durante el embarazo y en tándem, siendo una práctica natural y respetuosa con nuestros hijos”.")),
2: Q_("92-es", "Espanhol", "Interpretação de texto", "<p>O autor diz que o emigrante oscila entre duas atitudes: viver de saudade da pátria ou mergulhar na nova cultura. O mestiço se sente parte de dois mundos sem se integrar por completo a nenhum deles. O dilema é a <strong>constatação de sua existência no entrelugar</strong>, entre duas culturas. Alternativa <strong>A</strong>.</p><p>Cortar raízes (E) é só uma das duas atitudes possíveis, e não o dilema.</p>",
      ["imigração", "identidade"], trocas=[("Historia de España", "<em>Historia de España</em>")]),
3: Q_("93-es", "Espanhol", "Interpretação de texto", "<p>Barret diz ter visto “muchas cosas tristes”: a terra fértil e selvagem que sufoca o homem, que planta uma semente e não sabe qual planta é a sua, e os caminhos devorados pela vegetação e apagados pelas inundações. A percepção é de <strong>desalento frente às adversidades naturais</strong>. Alternativa <strong>A</strong>.</p><p>A terra é fértil demais, e não impossível de cultivar (C).</p>",
      ["crônica", "natureza"], trocas=[("Lo que he visto. Cuba", "<em>Lo que he visto</em>. Cuba")], alts={**D["93-es"]["alternativas"]}),
4: Q_("94-es", "Espanhol", "Interpretação de texto", "<p>“Sudar la gota gorda” significa fazer um grande esforço, trabalhar duro. Vargas Llosa diz que escrever lhe “cuesta mucho trabajo” e o faz suar, embora nada lhe dê tanto prazer. A escrita, para ele, <strong>demanda expressiva dedicação</strong>. Alternativa <strong>E</strong>.</p><p>Memória e fantasia (A) aparecem no texto, mas não é isso que a expressão indica.</p>",
      ["expressão idiomática", "Vargas Llosa"]),
5: Q_("95-es", "Espanhol", "Interpretação de texto", "<p>O poema contrapõe o dia longo das crianças ao tempo que, para os adultos, se estreita: a manhã vira meio-dia e logo anoitece, “se me fue el día”, e um ladrão oculto “roba mi vida”. O tema é a <strong>angústia provocada pela fugacidade do tempo</strong>. Alternativa <strong>C</strong>.</p><p>O “ladrão” é uma metáfora do tempo, e não da violência urbana (D).</p>",
      ["poema", "tempo"],
      extra=com_fig("95-es", "q95es", "Poema “El robo”, de Circe Maia, em espanhol, como aparece na prova: para as crianças o dia é largo como avenidas abertas; para os adultos o tempo se estreita, a manhã logo vira meio-dia e anoitece, uma voz diz que o dia se foi entre voltas e voltas e o eu lírico conclui que algum ladrão oculto rouba sua vida.",
                    enun="[[fig:1]]" + fonte("MAIA, C. <em>Obra poética</em>. Montevidéu: Rebecalinke, 2010.") + p("O poema <em>El robo</em>, de Circe Maia, poetisa uruguaia contemporânea, trata do(a)"))),
}

COMUM = {
6: Q_(96, "Língua Portuguesa", "Gêneros textuais", "<p>A notícia informa que as doações cresceram e que seis estados zeraram a fila de transplante de córnea, mas não todos os estados nem todos os órgãos. O cartaz continua pedindo doações. Os textos se completam: o cartaz é <strong>complementar, pois a notícia diz que a doação de órgãos cresceu e o cartaz solicita doações</strong>. Alternativa <strong>B</strong>.</p><p>A notícia não diz que o país superou a necessidade de doação (A).</p>",
      ["notícia", "cartaz"],
      extra={"enunciado": tit("TEXTO I") + tit(T(96, 0).replace("TEXTO I ", "")) + ap(T(96, 1), T(96, 2)) + tit("TEXTO II") + "[[fig:1]]" + fonte(T(96, 5)) + p(T(96, 6)),
             "imagens": figs(("q96", "Cartaz com a foto de um homem sorridente de cabelos grisalhos e o texto “Seja um doador de órgãos. Avise a sua família.”"))}),
7: Q_(97, "Educação Física", "Esportes de combate", "<p>O texto diz que o MMA deixou de ser uma espécie de vale-tudo: “agora, a modalidade tem regras e acompanhamento médico obrigatório para que o esporte apague o estigma negativo”, e virou o grande evento que tira espaço do boxe. As mudanças <strong>visam delimitar a violência das lutas, preservando a integridade dos atletas e enquadrando a modalidade no formato do esporte de espetáculo</strong>. Alternativa <strong>E</strong>.</p><p>O objetivo não é levar o MMA às academias como prática de saúde (C) nem ao lazer (A).</p>",
      ["MMA", "esporte-espetáculo"], trocas=[("UFC: saiba como o MMA nocauteou o boxe em oito golpes", "<em>UFC: saiba como o MMA nocauteou o boxe em oito golpes</em>"), ("Veja, 10", "<em>Veja</em>, 10")]),
8: Q_(98, "Educação Física", "Saúde e atividade física", "<p>O texto diz que a suplementação só é benéfica para um pequeno grupo, como atletas com dieta desequilibrada, e que a mídia e a indústria estimulam o uso entre adolescentes, com o mito do corpo ideal e bilhões em propaganda. A ingestão <strong>é estimulada pela indústria voltada para adolescentes que buscam um corpo ideal</strong>. Alternativa <strong>B</strong>.</p><p>O texto nega que os suplementos sejam indispensáveis para quem faz atividade física (A).</p>",
      ["suplementos", "padrão de beleza"]),
9: Q_(99, "Literatura", "Literatura contemporânea", "<p>No texto I, João Guedes sai do campo, empobrece na cidade e acaba preso por roubo de ovelha; no texto II, o narrador sai da cadeia e não acha emprego. Nos dois, a <strong>falta de oportunidades na cidade dialoga com a pobreza do campo rumo à criminalidade</strong>. Alternativa <strong>C</strong>.</p><p>Os textos mostram causas sociais do crime, e não uma criminalidade inerente ao ser humano (A).</p>",
      ["campo e cidade", "violência"], trocas=[("Porteira fechada", "<em>Porteira fechada</em>"), ("Feliz Ano Novo", "<em>Feliz Ano Novo</em>")]),
10: Q_(100, "Literatura", "Modernismo", "<p>“A vida é assim: esquenta e esfria, aperta e daí afrouxa […] O que ela quer da gente é coragem.” Riobaldo resume a experiência numa frase curta, que vale como verdade geral. O desabafo se aproxima de um <strong>aforismo, por expor uma máxima em poucas palavras</strong>. Alternativa <strong>D</strong>.</p><p>Não há personagens animais nem lição narrada, como numa fábula (B).</p>",
      ["Guimarães Rosa", "aforismo"], trocas=[("Grande sertão: veredas. Rio", "<em>Grande sertão: veredas</em>. Rio"), ("romance Grande sertão: veredas,", "romance <em>Grande sertão: veredas</em>,")]),
11: Q_(101, "Língua Portuguesa", "Coesão textual", "<p>Em “Há qualquer coisa de especial <strong>nisso</strong> de botar a cara na janela em crônica de jornal”, o pronome “nisso” aponta para a frente: anuncia o que vem logo depois, “botar a cara na janela em crônica de jornal”. É uma referência catafórica. Alternativa <strong>A</strong>.</p>",
      ["pronomes", "catáfora"], trocas=[("Pensar é transgredir", "<em>Pensar é transgredir</em>")]),
12: Q_(102, "Artes", "Música", "<p>John Cage abre a porta da sala de concerto para que os ruídos da rua entrem na composição: o som do ambiente passa a fazer parte da obra. Isso representa a <strong>intenção do compositor de que os sons extramusicais sejam parte integrante da música</strong>. Alternativa <strong>D</strong>.</p><p>A porta aberta é uma imagem para incluir ruídos, e não para democratizar o acesso ao concerto (A e E).</p>",
      ["John Cage", "música contemporânea"], trocas=[("O ouvido pensante", "<em>O ouvido pensante</em>")]),
13: Q_(103, "Língua Portuguesa", "Argumentação", "<p>A autora lembra que se fala muito em crise da leitura, mas diz que pesquisas acadêmicas indicam que “talvez não seja exatamente assim”: os brasileiros leem, só que leem livros que as pesquisas tradicionais não levam em conta. Ela <strong>questiona a existência de uma crise de leitura com base nos dados de pesquisas acadêmicas</strong>. Alternativa <strong>D</strong>.</p><p>Ela não atribui a crise ao desinteresse dos jovens (E): contesta essa ideia.</p>",
      ["leitura", "posicionamento"]),
14: Q_(104, "Língua Portuguesa", "Variação linguística", "<p>Possenti diz que não existe um único português correto: o estilo dos contratos, dos manuais, dos juízes, dos cordelistas e dos jornais é diferente. Dominar a língua é saber <strong>adequar as formas da língua a diferentes tipos de texto e contexto</strong>. Alternativa <strong>D</strong>.</p><p>O autor diz que a escola deve, sim, continuar a corrigir, e não desprezar a gramática (E).</p>",
      ["adequação", "norma padrão"], trocas=[("Gramática na cabeça. Língua Portuguesa", "Gramática na cabeça. <em>Língua Portuguesa</em>")]),
15: Q_(105, "Língua Portuguesa", "Gêneros textuais", "<p>O cartaz mostra um monstro escuro, com as palavras “Para algumas crianças o pesadelo chega antes do sono”, e pede “Denuncie qualquer caso de violência sexual infantil. Ligue 100”. A metáfora do pesadelo serve para <strong>dar a devida dimensão do que é o abuso sexual para uma criança, enfatizando a importância da denúncia</strong>. Alternativa <strong>C</strong>.</p><p>O cartaz não diz que o abuso ocorre durante o sono (E): o pesadelo é a própria violência.</p>",
      ["propaganda", "metáfora"],
      extra=com_fig(105, "q105", "Cartaz com um monstro preto de braços abertos, formado pelas palavras “Para algumas crianças o pesadelo chega antes do sono”. No canto: “Denuncie qualquer caso de violência sexual infantil. Ligue 100.”")),
16: Q_(106, "Língua Portuguesa", "Oralidade", "<p>Na fala espontânea, “né” é um marcador conversacional: o falante verifica se o ouvinte está acompanhando e mantém o turno enquanto organiza o pensamento. É uma <strong>estratégia típica de manutenção da interação oral</strong>. Alternativa <strong>B</strong>.</p><p>Não é marca de pouca escolaridade (A) nem de uma região (D): aparece na fala de pessoas de todo o país.</p>",
      ["marcadores conversacionais", "fala"], trocas=[("Corpus discurso &amp; gramática", "<em>Corpus discurso &amp; gramática</em>")] if "&amp;" in enunciado_enem(D[106]) else []),
17: Q_(107, "Língua Portuguesa", "Gêneros digitais", "<p>O texto diz que o blog deixou de ser só um diário da rotina e passou a permitir que qualquer pessoa publique ideias e opiniões e que outras comentem, “criando um grande debate aberto a todos”. Ele se destaca como <strong>espaço para exposição de opiniões e circulação de ideias</strong>. Alternativa <strong>B</strong>.</p><p>O texto não fala em substituir os diários (C) nem em aperfeiçoar a escrita (D).</p>",
      ["blog", "internet"], trocas=[("Blog é concebido", "<em>Blog</em> é concebido"), ("dos posts", "dos <em>posts</em>"), ("dos blogs requer", "dos <em>blogs</em> requer"), ("dos blogs está", "dos <em>blogs</em> está"), ("na web", "na <em>web</em>")],
      alts=D[107]["alternativas"]),
18: Q_(108, "Literatura", "Modernismo", "<p>Bandeira faz poesia com os brinquedos baratos do camelô (balões, macaquinho, perereca, canetinhas) e com a fala dos vendedores nas calçadas. Coisas comuns da rua viram matéria lírica: o poema <strong>traduz em linguagem lírica o mosaico de elementos de significação corriqueira</strong>. Alternativa <strong>C</strong>.</p><p>Os brinquedos aparecem como alegria das calçadas, e não como crítica à pobreza (B).</p>",
      ["Manuel Bandeira", "cotidiano"],
      extra=com_fig(108, "q108", "Poema “Camelôs”, de Manuel Bandeira, como aparece na prova: o eu lírico abençoa o camelô dos brinquedos baratos, enumera os balões coloridos, o macaquinho que sobe no coqueiro, a perereca que pula e as canetinhas que nunca escreverão, reproduz o pregão de um vendedor e diz que eles ensinam nas ruas os mitos da meninice e dão aos homens tristes uma lição de infância.",
                    enun="[[fig:1]]" + fonte("BANDEIRA, M. <em>Estrela da vida inteira</em>. Rio de Janeiro: Nova Fronteira, 2007.") + p(T(108, 6)))),
19: Q_(109, "Literatura", "Realismo", "<p>Brás Cubas defende Cotrim, dizendo que sua dureza com os escravos, que ele prendia e mandava açoitar, não vinha de índole má, mas era “puro efeito de relações sociais”. Ao desculpar a tortura como algo natural, o narrador expõe o cunhado e a sociedade escravista: a ironia está em <strong>atribuir a “efeito de relações sociais” a naturalidade com que Cotrim prendia e torturava os escravos</strong>. Alternativa <strong>B</strong>.</p>",
      ["Machado de Assis", "ironia"], trocas=[("Memórias póstumas de Brás Cubas. Rio", "<em>Memórias póstumas de Brás Cubas</em>. Rio"), ("Realismo na literatura brasileira, Memórias póstumas de Brás Cubas condensa", "Realismo na literatura brasileira, <em>Memórias póstumas de Brás Cubas</em> condensa")]),
20: Q_(110, "Língua Portuguesa", "Funções da linguagem", "<p>“O exercício da crônica” é uma crônica que fala de como se escreve uma crônica: o cronista diante da máquina, buscando um fato no noticiário. A função predominante é a metalinguística, que se constitui <strong>nas dificuldades de se escrever uma crônica por meio de uma crônica</strong>. Alternativa <strong>E</strong>.</p>",
      ["metalinguagem", "crônica"], trocas=[("Para viver um grande amor: crônicas e poemas", "<em>Para viver um grande amor: crônicas e poemas</em>")]),
21: Q_(111, "Língua Portuguesa", "Modalização", "<p>Em “a água potável <strong>deve</strong> acabar logo, em 2050”, o verbo “dever” indica probabilidade, uma hipótese sobre o futuro. Junto com as “teorias mais pessimistas”, ele expressa <strong>uma previsão trágica a respeito das fontes de água potável</strong>. Alternativa <strong>D</strong>.</p><p>Não se trata de uma constatação (A), mas de uma projeção.</p>",
      ["modalização", "verbo dever"]),
22: Q_(112, "Língua Portuguesa", "Gêneros textuais", "<p>O texto diz que a TV do futuro “permite assistir ao que você quer, quando quer” e que a segunda tela (tablet ou smartphone) torna o engajamento nas redes sociais tão importante quanto a audiência. As novas tecnologias vão <strong>contemplar os desejos individuais com recursos de ponta</strong>. Alternativa <strong>B</strong>.</p><p>A TV não vira o principal meio de acesso às redes (C): as redes ficam na segunda tela.</p>",
      ["televisão", "tecnologia"],
      extra=com_fig(112, "q112", "Abertura de reportagem com o título “Viva a nova TV!” e o texto: “Diga olá para a televisão do futuro. Ela permite assistir ao que você quer, quando quer. A segunda tela é um tablet ou smartphone, e o engajamento nas redes sociais torna-se mais importante do que a audiência. Preparado para essa revolução?”, por Paula Rothmann.")),
23: Q_(113, "Literatura", "Barroco", "<p>O soneto compara a chegada de um novo governante à Bahia com a libertação dos hebreus do Egito: Deus teria vindo “estirpar desta cidade / O Faraó do povo brasileiro”, ou seja, o governante anterior, tratado como tirano. Sob o tema religioso, há uma <strong>crítica velada à forma de governo vigente</strong>. Alternativa <strong>C</strong>.</p><p>A Páscoa e o Faraó são usados como metáfora política, e não como reflexão sobre dogmas (D).</p>",
      ["Gregório de Matos", "sátira"],
      extra={"enunciado": SON("Quando Deus redimiu da tirania / Da mão do Faraó endurecido / O Povo Hebreu amado, e esclarecido, / Páscoa ficou da redenção o dia.",
                              "Páscoa de flores, dia de alegria / Àquele Povo foi tão afligido / O dia, em que por Deus foi redimido; / Ergo sois vós, Senhor, Deus da Bahia.",
                              "Pois mandado pela alta Majestade / Nos remiu de tão triste cativeiro, / Nos livrou de tão vil calamidade.",
                              "Quem pode ser senão um verdadeiro / Deus, que veio estirpar desta cidade / O Faraó do povo brasileiro.")
                         + fonte("DAMASCENO, D. (Org.). <em>Melhores poemas: Gregório de Matos</em>. São Paulo: Globo, 2006.") + p(T(113, 5))}),
24: Q_(114, "Língua Portuguesa", "Argumentação", "<p>O texto apresenta as visões de que o Brasil é samba ou MPB como estereótipos e as derruba com dados: segundo uma pesquisa do Ibope de 2012-2013, o sertanejo encanta mais da metade do país. A estratégia baseia-se na <strong>apresentação dos resultados de uma pesquisa que retrata o quadro atual da preferência popular</strong>. Alternativa <strong>A</strong>.</p><p>Os estrangeirismos e a ironia (C e D) aparecem, mas a prova da tese são os números da pesquisa.</p>",
      ["argumento por dados", "música brasileira"],
      extra={"enunciado": tit("O Brasil é sertanejo") + ap(T(114, 1), T(114, 2), T(114, 3)) + fonte("GIRON, L. A. <em>Época</em>, n. 805, out. 2013 (fragmento).")
             + p("O texto objetiva convencer o leitor de que a configuração da preferência musical dos brasileiros não é mais a mesma da dos anos 1970. " + T(114, 5))}),
25: Q_(115, "Língua Portuguesa", "Gêneros textuais", "<p>O anúncio faz perguntas ao leitor (“Você já foi chamado de nerd? Já passou um bom tempo pensando em coisas que a maior parte de seus amigos nem sabia que existia?”) e conclui “Você é perfeito para nós”. Ele <strong>apresenta como estratégia a formação de um perfil por meio de perguntas direcionadas, o que dinamiza a interação texto-leitor</strong>. Alternativa <strong>B</strong>.</p><p>O anúncio valoriza o nerd, em vez de usar um estereótipo negativo (D).</p>",
      ["anúncio", "interlocução"],
      extra=com_fig(115, "q115", "Anúncio com a foto de um rapaz de óculos sentado num banco com um tablet, diante de uma parede com ícones de tecnologia. Título: “Queremos seu talento, exatamente como ele é”. Texto: “Você já foi chamado de nerd? Já passou um bom tempo pensando em coisas que a maior parte de seus amigos nem sabia que existia? É louco por novas tecnologias? Está entre os melhores alunos das melhores faculdades? Você é perfeito para nós. Nossa empresa de tecnologia reúne talentos para aprimorar processos produtivos de empresas líderes. Se você quer continuar a ser o melhor, venha trabalhar conosco.”",
                    enun="[[fig:1]]" + fonte("<em>Scientific American Brasil</em>, ano 11, n. 134, jul. 2013 (adaptado).") + p(T(115, 2)))),
26: Q_(116, "Língua Portuguesa", "Tecnologias da comunicação", "<p>A linotipo compunha linhas inteiras de tipos de uma vez, muito mais rápido que a composição letra por letra, e barateou a impressão de jornais, revistas e livros. Em termos sociais, o impacto foi a <strong>produção acessível de materiais informacionais</strong>. Alternativa <strong>D</strong>.</p><p>A montagem acelerada de textos (C) é o efeito técnico; a pergunta pede o efeito social.</p>",
      ["imprensa", "linotipo"]),
27: Q_(117, "Artes", "Cultura popular", "<p>As oficinas de Juazeiro e do Crato mantêm a impressão manual, letra por letra, e a capa em xilogravura, mesmo com a indústria gráfica informatizada; o texto diz que isso “faz parte da filosofia do trabalho”. Unir essas técnicas <strong>auxilia na manutenção da essência identitária dessa tradição popular</strong>. Alternativa <strong>E</strong>.</p><p>O texto valoriza a tradição, e não a renovação (B).</p>",
      ["cordel", "xilogravura"]),
28: Q_(118, "Língua Portuguesa", "Variação linguística", "<p>O cronista mostra palavras que caíram em desuso: “fita de cinema” em vez de “filme”, “artista” em vez de “ator”, “defluxo” em vez de “resfriado”. Quem usa as antigas revela a idade. A variação no tempo, a <strong>utilização de inovações no léxico, é percebida na comparação de gerações</strong>. Alternativa <strong>B</strong>.</p><p>O texto constata a mudança, sem dizer que as palavras novas devem ser incentivadas (A).</p>",
      ["variação histórica", "léxico"], trocas=[("Folha de S. Paulo", "<em>Folha de S. Paulo</em>")]),
29: Q_(119, "Literatura", "Pré-Modernismo", "<p>O soneto mantém a forma fixa, os versos decassílabos e as rimas ricas, herdados do Parnasianismo e do Simbolismo, mas traz um vocabulário científico (“carbono”, “amoníaco”, “epigênesis”) e uma visão de angústia e decomposição que choca o leitor. A transição está na <strong>manutenção de elementos formais do Parnasianismo e do Simbolismo, com inovação na expressividade e o desconcerto existencial</strong>. Alternativa <strong>D</strong>.</p><p>O soneto e a métrica (A) são justamente o que o Modernismo abandonaria.</p>",
      ["Augusto dos Anjos", "cientificismo"],
      extra={"enunciado": tit("Psicologia de um vencido") + SON("Eu, filho do carbono e do amoníaco, / Monstro de escuridão e rutilância, / Sofro, desde a epigênesis da infância, / A influência má dos signos do zodíaco.",
                              "Profundíssimamente hipocondríaco, / Este ambiente me causa repugnância... / Sobe-me à boca uma ânsia análoga à ânsia / Que se escapa da boca de um cardíaco.",
                              "Já o verme — este operário das ruínas — / Que o sangue podre das carnificinas / Come, e à vida em geral declara guerra,",
                              "Anda a espreitar meus olhos para roê-los, / E há de deixar-me apenas os cabelos, / Na frialdade inorgânica da terra!")
                         + fonte("ANJOS, A. <em>Obra completa</em>. Rio de Janeiro: Nova Aguilar, 1994.") + p(T(119, 6))}),
30: Q_(120, "Literatura", "Literatura contemporânea", "<p>A crônica narra, com humor e meias-palavras, as aventuras do velho Abílio com as donas casadas e o vizinho que tenta imitá-lo com chantagem. O narrador não julga nem ensina: mostra com malícia o que acontece. O caráter é <strong>irônico, pois apresenta com malícia a convivência entre vizinhos</strong>. Alternativa <strong>C</strong>.</p><p>Não há nostalgia (B) nem lição de conduta (E).</p>",
      ["Dalton Trevisan", "ironia"], trocas=[("Mistérios de Curitiba", "<em>Mistérios de Curitiba</em>")]),
31: Q_(121, "Língua Portuguesa", "Gêneros textuais", "<p>O editorial retoma uma reportagem do próprio jornal sobre o lixo jogado na estrada e a comenta, criticando o descaso e cobrando providências. A função social do editorial é <strong>interpretar criticamente fatos noticiados e considerados relevantes para a opinião pública</strong>. Alternativa <strong>D</strong>.</p><p>O editorial expressa a opinião do jornal, e não a do autor da notícia (E).</p>",
      ["editorial", "opinião"]),
32: Q_(122, "Artes", "Arte contemporânea", "<p>Os “Bichos” de Lygia Clark são placas de metal ligadas por dobradiças que o público pode manipular, mudando a forma da obra. O espectador deixa de só olhar e passa a agir: é a <strong>participação efetiva do espectador na obra, o que determina a proximidade entre arte e vida</strong>. Alternativa <strong>A</strong>.</p><p>A obra não é feita de objetos do cotidiano (B), nem produzida em série (E).</p>",
      ["Lygia Clark", "Neoconcretismo"],
      extra=com_fig(122, "q122", "Foto de uma mão manipulando a escultura “Bicho de bolso”, de Lygia Clark: pequenas placas de metal triangulares e retangulares unidas por dobradiças, formando uma figura angulosa.",
                    enun="[[fig:1]]" + fonte("CLARK, L. <em>Bicho de bolso</em>. Placas de metal, 1966.") + p(T(122, 2).replace("obra Bicho de bolso", "obra <em>Bicho de bolso</em>")))),
33: Q_(123, "Artes", "Música", "<p>Cavaquinho e violão são a base do <strong>choro e do samba</strong>, gêneros urbanos de origem carioca. Alternativa <strong>C</strong>.</p><p>Maracatu, frevo e baião (A, B e E) têm como base percussão, metais ou sanfona, zabumba e triângulo.</p>",
      ["choro", "instrumentos"], trocas=[("O kronjong", "O <em>kronjong</em>")]),
34: Q_(124, "Literatura", "Simbolismo", "<p>O soneto fala de um “ser humilde entre os humildes seres”, cujo sofrimento ninguém viu, para quem “o mundo foi negro e duro”, e que carregou uma “cruz infernal”. Cruz e Sousa, poeta negro e filho de escravizados, enfrentou o preconceito racial. A percepção traduz-se em <strong>sofrimento tácito diante dos limites impostos pela discriminação</strong>. Alternativa <strong>A</strong>.</p><p>“Embriagado, tonto de prazeres” não indica vício (B): faz parte da visão de um mundo sem saída.</p>",
      ["Cruz e Sousa", "Simbolismo"],
      extra={"enunciado": tit("Vida obscura") + SON("Ninguém sentiu o teu espasmo obscuro, / ó ser humilde entre os humildes seres, / embriagado, tonto de prazeres, / o mundo para ti foi negro e duro.",
                              "Atravessaste no silêncio escuro / a vida presa a trágicos deveres / e chegaste ao saber de altos saberes / tornando-te mais simples e mais puro.",
                              "Ninguém te viu o sentimento inquieto, / magoado, oculto e aterrador, secreto, / que o coração te apunhalou no mundo,",
                              "Mas eu que sempre te segui os passos / sei que cruz infernal prendeu-te os braços / e o teu suspiro como foi profundo!")
                         + fonte("SOUSA, C. <em>Obra completa</em>. Rio de Janeiro: Nova Aguilar, 1961.") + p(T(124, 3))}),
35: Q_(125, "Literatura", "Literatura contemporânea", "<p>Verissimo conta a visita dos Reis Magos, uma passagem bíblica solene, com gírias como “plá”, “se flagraram”, “dar cascata”, “tá falado”, “dar uma incerta”. O humor nasce do <strong>contraste entre o tema abordado e a linguagem utilizada</strong>. Alternativa <strong>E</strong>.</p><p>A linguagem é coloquial, e não rebuscada (A).</p>",
      ["Verissimo", "humor"], trocas=[("O nariz e outras crônicas", "<em>O nariz e outras crônicas</em>")]),
36: Q_(126, "Artes", "Teatro", "<p>As rubricas (“arrepelando-se de raiva”, “Batendo com o pé”) são indicações do autor sobre gestos e emoções. Numa montagem, o diretor e os atores podem segui-las ou não, assim como podem mudar cenário, figurino e até o texto. Elas constituem uma <strong>possibilidade, porque o texto pode ser mudado, assim como outros elementos</strong>. Alternativa <strong>B</strong>.</p><p>As rubricas não são irrelevantes (C): orientam a encenação, mas não a obrigam.</p>",
      ["rubricas", "encenação"],
      extra={"enunciado": ap("FABIANA, <em>arrepelando-se de raiva</em> — Hum! Ora, eis aí está para que se casou meu filho, e trouxe a mulher para minha casa. É isto constantemente. Não sabe o senhor meu filho que quem casa quer casa... Já não posso, não posso, não posso! <em>(Batendo com o pé).</em> Um dia arrebento, e então veremos!")
             + fonte("PENA, M. <em>Quem casa quer casa</em>. www.dominiopublico.gov.br. Acesso em: 7 dez. 2012.") + p(T(126, 2))}),
37: Q_(127, "Língua Portuguesa", "Intertextualidade", "<p>A charge refaz <em>Guernica</em> com um carro destruído e o balão: “O trânsito no feriadão é sempre um quadro dramático”. “Quadro dramático” tem dois sentidos: a pintura de Picasso, que é um quadro, e a situação trágica das estradas. É <strong>uma expressão polissêmica, “quadro dramático”, remetendo-se tanto à obra pictórica quanto ao contexto do trânsito brasileiro</strong>. Alternativa <strong>E</strong>.</p>",
      ["charge", "polissemia"],
      extra=com_fig(127, "q127", "Charge de Iotti que recria em preto e branco o painel “Guernica”, de Picasso, com figuras de pessoas e animais em desespero, e põe no centro um carro destroçado. No alto, um balão diz: “O trânsito no feriadão é sempre um quadro dramático!”",
                    enun="[[fig:1]]" + fonte("Jornal <em>Zero Hora</em>, 2 mar. 2006.") + p(T(127, 2).replace("cena de Guernica", "cena de <em>Guernica</em>")))),
38: Q_(128, "Literatura", "Poesia contemporânea", "<p>Cada “mas” vem depois de uma ação de resignação (morder o fruto amargo, cumprir o trato injusto, sofrer o esquema falso) e introduz o que realmente importa ao eu lírico: avisar aos outros. O “mas” traz <strong>a introdução do argumento mais forte de uma sequência</strong>, que prepara a proposta final de um mundo novo. Alternativa <strong>C</strong>.</p><p>As ações não são inconciliáveis (B): o eu lírico faz as duas coisas.</p>",
      ["conjunção mas", "operadores argumentativos"],
      extra=com_fig(128, "q128", "Poema “Tarefa”, de Geir Campos, como aparece na prova: em versos paralelos, o eu lírico propõe morder o fruto amargo, cumprir o trato injusto e sofrer o esquema falso sem ceder, mas avisar aos outros o quanto são amargos, injustos e falsos, e dizer que são coisas que podem mudar, até confiar à gente exausta o plano de um mundo novo e mais humano.",
                    enun="[[fig:1]]" + fonte("CAMPOS, G. <em>Tarefa</em>. Rio de Janeiro: Civilização Brasileira, 1981.") + p(T(128, 2)))),
39: Q_(129, "Língua Portuguesa", "Variação linguística", "<p>“Cabra”, no sentido de “sujeito, homem”, é uma palavra típica do falar nordestino, assim como a contração “pr’esses”. O verso que singulariza o falar popular regional é <strong>“Vou mostrar pr’esses cabras”</strong>. Alternativa <strong>C</strong>.</p><p>“Tou” (B) é uma redução comum na fala de todo o país, e não só regional.</p>",
      ["regionalismo", "xaxado"],
      extra=com_fig(129, "q129", "Letra de “Óia eu aqui de novo”, de Antônio de Barros, como aparece na prova: o eu lírico anuncia que voltou para xaxar e mostrar aos cabras que ainda dá no couro, chama a morena vestida de chita e manda chamar Maria, Luzia, Zabé e Raque.",
                    enun="[[fig:1]]" + fonte("BARROS, A. <em>Óia eu aqui de novo</em>. Disponível em: www.luizluagonzaga.mus.br. Acesso em: 5 maio 2013 (fragmento).") + p(T(129, 3)))),
40: Q_(130, "Língua Portuguesa", "Interpretação de texto", "<p>O especialista diz que o Brasil tem condições de desenvolver tecnologia própria e que o governo deve usar seu poder de compra de softwares e hardwares de segurança “de forma a fomentar essas empresas, a produção de conhecimento na área e a construção de uma cadeia de produção nacional”. A necessidade é <strong>promover a indústria de segurança da informação</strong>. Alternativa <strong>B</strong>.</p><p>Os canais de denúncia são citados, mas não para incentivar delatores (D).</p>",
      ["segurança da informação", "tecnologia"], trocas=[("compra de softwares", "compra de <em>softwares</em>"), ("e hardwares", "e <em>hardwares</em>")]),
41: Q_(131, "Língua Portuguesa", "Gêneros textuais", "<p>A charge anuncia a primeira foto feita pelo robô Opportunity em Marte e mostra o robô fazendo uma <em>selfie</em> com o braço esticado, como as pessoas fazem nas redes sociais. A crítica é à <strong>circulação digital excessiva de autorretratos</strong>. Alternativa <strong>C</strong>.</p>",
      ["charge", "selfie"],
      extra=com_fig(131, "q131", "Tirinha: o texto “Nasa divulga a primeira foto feita pelo robô Opportunity no solo de Marte. Veja:” e, embaixo, o robô num terreno vazio, fazendo pose e fotografando a si mesmo com o braço esticado, como numa selfie.",
                    enun="[[fig:1]]" + fonte("WILL. Disponível em: www.willtirando.com.br. Acesso em: 7 nov. 2013.") + p("<em>Opportunity</em> é o nome de um veículo explorador que aterrissou em Marte com a missão de enviar informações à Terra. A charge apresenta uma crítica ao(à)"))),
42: Q_(132, "Literatura", "Literatura contemporânea", "<p>O texto II diz que prima Constança repetia os ditados “procurando interpretar os desígnios de Deus, transformar os seus desejos nos desígnios de Deus”. Ela usa o saber popular a favor do que ela mesma queria: <strong>aciona os ditados para justificar suas ações</strong>. Alternativa <strong>C</strong>.</p><p>Ela não os toma como verdade divina (E): usa-os para fazer parecer divino o próprio desejo.</p>",
      ["ditados populares", "intertextualidade"], trocas=[("Folclore literário e linguístico", "<em>Folclore literário e linguístico</em>"), ("Uma vida em segredo", "<em>Uma vida em segredo</em>")]),
43: Q_(133, "Artes", "Cultura juvenil", "<p>O texto diz que nos bailes black das periferias se disseminou um estilo que buscava valorizar a cultura negra, nas músicas, nas roupas e nos penteados. O hip-hop no Brasil é uma forma de <strong>afirmação de identidade dos jovens que a praticam</strong>. Alternativa <strong>D</strong>.</p><p>Os jovens partiram da black music americana, mas criaram algo próprio, e não uma simples reprodução (E).</p>",
      ["hip-hop", "identidade"]),
44: Q_(134, "Língua Portuguesa", "Variação linguística", "<p>O texto mostra que os empréstimos acompanham a história: palavras indígenas e africanas, depois as dos imigrantes, e depois as europeias, que chegaram sem passar por Portugal após a Independência. Eles <strong>deixaram marcas da história vivida pela nação, como a colonização e a imigração</strong>. Alternativa <strong>A</strong>.</p><p>Os empréstimos afastaram, e não aproximaram, o português do Brasil do de Portugal (D).</p>",
      ["empréstimos linguísticos", "português do Brasil"], trocas=[("O português da gente", "<em>O português da gente</em>")]),
45: Q_(135, "Língua Portuguesa", "Gêneros textuais", "<p>Na peça, uma mão segura um megafone que tem o cabo de uma arma de fogo, ao lado do slogan “Paz só se consegue com Voz”. A arma, que representa a violência, vira instrumento para amplificar a palavra: a ideia vem da <strong>associação entre uma arma de fogo e um megafone</strong>. Alternativa <strong>B</strong>.</p><p>A mão com o megafone (D) sozinha não traria a ideia de trocar a violência pela palavra.</p>",
      ["propaganda", "metáfora visual"],
      extra=com_fig(135, "q135", "Peça publicitária: uma mão segura pelo cabo um megafone cujo punho tem a forma de uma pistola; ao lado, o logotipo “Voz da Comunidade” e a frase “Paz só se consegue com Voz”.")),
}


def montar(lingua):
    Q = dict(ING if lingua == "ingles" else ESP)
    Q.update(COMUM)
    return Q
