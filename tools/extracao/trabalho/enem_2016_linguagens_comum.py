# Enem 2016, 2º dia, caderno azul: Linguagens (questões 91 a 135; no site, 1 a 45). Em 2016 Linguagens e Matemática eram no 2º dia.
# Duas provas: enem-2016-linguagens-ingles (91–95 = inglês) e enem-2016-linguagens-espanhol (91–95 = espanhol); 96–135 iguais.
# Letras e poemas modernos como imagem (alt descreve, não transcreve): Q94 (McCartney), Q93-es (Sueños mexicanos), Q111 (Chico Buarque),
# Q113 (Armando Freitas Filho), Q116 (Ana Cristina Cesar), Q120 (Jaguar Wanderley), Q121 (João Cabral), Q125 (Saramago).
# Em texto, domínio público: Q100 (Cláudio Manuel da Costa).
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent / "tools"))
from enem_aj import carregar_enem, enunciado_enem, paragrafos_enem

D = carregar_enem("enem-2016-dia2-azul")
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

ING = {
1: Q_(91, "Inglês", "Interpretação de texto", "<p>O texto diz que ainda é quase impossível imprimir órgãos com estrutura em 3D, como fígado e rins, mas que “at the moment, skin and other flat tissues are most promising for the inkjet”. A perspectiva mais promissora é o <strong>desenvolvimento de uma tinta para produzir pele e tecidos humanos finos</strong>, a bio-ink. Alternativa <strong>C</strong>.</p><p>Os rins (D) são citados justamente como estrutura difícil de imprimir.</p>",
      ["texto de divulgação", "tecnologia"],
      extra={"enunciado": tit("Frankentissue: printable cell technology") + ap(T(91, 0).replace("Frankentissue: printable cell technology ", "").replace("bio- ink", "bio-ink"), T(91, 1)) + fonte(T(91, 2)) + p(T(91, 3))}),
2: Q_(92, "Inglês", "Interpretação de texto", "<p>O cartaz lista desastres (pandemia, terrorismo, terremoto, furacão, acidente nuclear) e pergunta: “Would you know what to do if disaster struck here? Learn to live prepared.” O endereço leva às <strong>medidas de emergência a serem tomadas em catástrofes</strong>. Alternativa <strong>E</strong>.</p><p>Os desastres citados aconteceram em outros lugares, não em Connecticut (D).</p>",
      ["cartaz", "vocabulário"],
      extra={"enunciado": "[[fig:1]]" + fonte(T(92, 1)) + p(T(92, 2).replace("em sites oficiais", "em <em>sites</em> oficiais")),
             "imagens": figs(("q92", "Cartaz: em fundo preto, pares de palavras em inglês, “Global Flu Pandemic”, “9/11 Terrorism”, “Earthquake Haiti”, “Katrina Hurricane”, “Chernobyl Nuclear”; embaixo, “Connecticut? Would you know what to do if disaster struck here? Learn to live prepared. To learn more about living prepared, go to ct.gov/dph/prepare”, ao lado da capa de um guia de preparação para emergências."))}),
3: Q_(93, "Inglês", "Interpretação de texto", "<p>O Politecnico di Milano anunciou que, a partir de 2014, a maioria de seus cursos será dada e avaliada inteiramente em inglês, porque, se continuar falando italiano, a universidade corre o risco de ficar isolada. Ela decidiu <strong>substituir a língua nacional para se inserir no contexto da globalização</strong>. Alternativa <strong>D</strong>.</p>",
      ["notícia", "globalização"],
      extra={"enunciado": tit("Italian university switches to English") + ap("<em>By Sean Coughlan, BBC News education correspondent</em>", T(93, 1), T(93, 2)) + fonte(T(93, 3)) + p(T(93, 4))}),
4: Q_(94, "Inglês", "Interpretação de texto", "<p>A canção compara pessoas negras e brancas ao ébano e ao marfim, as teclas pretas e brancas do piano, que vivem “in perfect harmony”, e pergunta por que as pessoas não fazem o mesmo, se “people are the same wherever we go”. McCartney defende <strong>o respeito étnico</strong>. Alternativa <strong>E</strong>.</p>",
      ["canção", "metáfora"],
      extra=com_fig(94, "q94", "Letra de “Ebony and ivory”, de Paul McCartney, em inglês, como aparece na prova: o ébano e o marfim convivem em perfeita harmonia lado a lado no teclado do piano, e o eu lírico pergunta por que as pessoas não fazem o mesmo, já que são iguais em todo lugar, com o bem e o mal em cada um, e aprendem a dar umas às outras o que precisam para sobreviver.",
                    enun="[[fig:1]]" + fonte("McCARTNEY, P. Disponível em: www.paulmccartney.com. Acesso em: 30 maio 2016.") + p(T(94, 1).split("2016. ")[1]))),
5: Q_(95, "Inglês", "Interpretação de texto", "<p>O texto explica que BOGOF é a sigla de uma estratégia de marketing de supermercado, “the best-known of the supermarket marketing strategies”, que atrai o consumidor com a ideia de levar algo de graça (“buy one get one free”). A expressão serve para <strong>anunciar mercadorias em promoção</strong>. Alternativa <strong>A</strong>.</p><p>O sentido de “vá embora” (B) é só a semelhança sonora com “Bog off!”.</p>",
      ["acrônimo", "consumo"]),
}

ESP = {
1: Q_("91-es", "Espanhol", "Interpretação de texto", "<p>Estela Carlotto resume a decisão como “una de cal y otra de arena, es querer quedar bien con Dios y con el diablo”: o tribunal concedeu o exame de DNA, mas limitou a comparação a um grupo de famílias, como quem agrada os dois lados. Ela usa a expressão para <strong>ironizar a parcialidade da Justiça nessa ação</strong>. Alternativa <strong>C</strong>.</p><p>Ela não critica a coleta do material (D), que considera “un paso importante”.</p>",
      ["expressão idiomática", "notícia"], trocas=[("jornal argentino Página 12,", "jornal argentino <em>Página 12</em>,")]),
2: Q_("92-es", "Espanhol", "Interpretação de texto", "<p>Cortázar diz que, ao ganhar um relógio, ganhamos a obrigação de dar corda, o medo de perdê-lo, a obsessão pela hora certa, e termina: “No te regalan un reloj, tú eres el regalado, a ti te ofrecen para el cumpleaños del reloj”. A pessoa passa a servir ao objeto: o texto convida o leitor a <strong>refletir sobre a coisificação do ser humano</strong>. Alternativa <strong>C</strong>.</p>",
      ["Cortázar", "crônica"], trocas=[("Historias de cronopios y de famas", "<em>Historias de cronopios y de famas</em>")]),
3: Q_("93-es", "Espanhol", "Interpretação de texto", "<p>Os versos interpretam sonhos com água: carregar um cântaro anuncia êxito, banhar-se em água fervendo anuncia inimigos, em água suja, perder alguém próximo. O aspecto da cultura popular é a <strong>crença na relevância dos sonhos como premonições ou conselhos</strong>. Alternativa <strong>B</strong>.</p>",
      ["cultura popular", "sonhos"],
      extra=com_fig("93-es", "q93es", "Versos “Agua”, em espanhol, como aparecem na prova: interpretações de sonhos com água; sonhar que carrega um cântaro na cabeça anuncia êxito; banhar-se num rio de água fervendo anuncia inimigos e traição; banhar-se em água suja anuncia a perda de alguém próximo.",
                    enun="[[fig:1]]" + fonte(T("93-es", 1).replace("Sueños mexicanos", "<em>Sueños mexicanos</em>")) + p(T("93-es", 2)))),
4: Q_("94-es", "Espanhol", "Interpretação de texto", "<p>O autor diz que os conselhos para buscar estabilidade eram “gato por liebre”: o mundo atual nos modela e nos “licua”, sempre em mudança. “Inestabilidad estable” une termos opostos para indicar a <strong>permanência da inconstância em uma sociedade marcada por contínuas mudanças</strong>. Alternativa <strong>E</strong>.</p>",
      ["paradoxo", "título"]),
5: Q_("95-es", "Espanhol", "Interpretação de texto", "<p>No grafite “No supe qué ponerme y me puse feliz”, o primeiro “ponerme” é vestir uma roupa; o segundo, “me puse feliz”, significa “fiquei feliz”: indica <strong>mudança de estado</strong>. Alternativa <strong>B</strong>.</p>",
      ["grafite", "polissemia"],
      extra={"enunciado": "[[fig:1]]" + fonte("ACCIÓN POÉTICA LIMA. Disponível em: https://twitter.com. Acesso em: 30 maio 2016.") + p(T("95-es", 1).split("2016. ")[1]),
             "imagens": figs(("q95es", "Foto de um muro branco com a frase pintada à mão em letras pretas: “No supe qué ponerme y me puse feliz”, assinada por Acción Poética Lima."))}),
}

COMUM = {
6: Q_(96, "Língua Portuguesa", "Funções da linguagem", "<p>O texto é sobre a leitura: diz o que é ler, como se atribui sentido a um texto. A metalinguagem está no fato de o texto <strong>discorrer sobre o ato de leitura</strong>, usando a linguagem para falar de um processo da própria linguagem. Alternativa <strong>D</strong>.</p>",
      ["metalinguagem", "leitura"], trocas=[("Do mundo da leitura para a leitura do mundo", "<em>Do mundo da leitura para a leitura do mundo</em>")]),
7: Q_(97, "Língua Portuguesa", "Gêneros digitais", "<p>O texto descreve como os boatos costumam ser: “mensagens dramáticas ou alarmantes que acompanham imagens chocantes, falam de crianças doentes ou avisam sobre falsos vírus”. Reconhecer esses traços permite desconfiar: a estratégia é <strong>analisar a linguagem utilizada nas mensagens recebidas</strong>. Alternativa <strong>B</strong>.</p>",
      ["hoax", "internet"], trocas=[("O hoax, como", "O <em>hoax</em>, como"), ("exemplos de hoax.", "exemplos de <em>hoax</em>."), ("por e-mail", "por <em>e-mail</em>"), ("Se o hoax for do tipo phishing (derivado de fishing,", "Se o <em>hoax</em> for do tipo <em>phishing</em> (derivado de <em>fishing</em>,"), ("sobre os hoaxes,", "sobre os <em>hoaxes</em>,")]),
8: Q_(98, "Artes", "Arte pública", "<p>O mosaico, numa estação de metrô, reproduz uma colcha de retalhos, objeto doméstico e comum, com formas geométricas coloridas. Ele leva o passageiro a <strong>apreciar a estética do cotidiano</strong>. Alternativa <strong>A</strong>.</p><p>A obra é para ser vista no caminho, não tocada ou percorrida (B e E).</p>",
      ["mosaico", "Claudio Tozzi"],
      extra={"enunciado": "[[fig:1]]" + fonte(T(98, 1).replace("Colcha de retalhos.", "<em>Colcha de retalhos</em>.")) + p(T(98, 2).replace("Colcha de retalhos", "<em>Colcha de retalhos</em>")),
             "imagens": figs(("q98", "Foto de um grande painel de mosaico na parede de uma estação de metrô, com retângulos e formas geométricas de padrões variados, lembrando uma colcha de retalhos."))}),
9: Q_(99, "Língua Portuguesa", "Variação linguística", "<p>“O peste” e “cachorro da molest’a” são xingamentos típicos da fala nordestina, região de Suassuna. Eles <strong>caracterizam usos linguísticos de uma região</strong>. Alternativa <strong>B</strong>.</p>",
      ["variação regional", "Suassuna"], trocas=[("O santo e a porca.", "<em>O santo e a porca</em>.")]),
10: Q_(100, "Literatura", "Arcadismo", "<p>O eu lírico não reconhece mais a paisagem, onde havia fonte e árvores floridas, e conclui que são os seus males que fazem “tudo degenera[r]”. A natureza decai junto com o sofrimento dele: há <strong>empatia entre os sofrimentos do eu e a agonia da terra</strong>. Alternativa <strong>E</strong>.</p>",
      ["Cláudio Manuel da Costa", "soneto"],
      extra={"enunciado": tit("Soneto VII") + ap(LET("Onde estou? Este sítio desconheço:", "Quem fez tão diferente aquele prado?", "Tudo outra natureza tem tomado;", "E em contemplá-lo tímido esmoreço."),
                                                 LET("Uma fonte aqui houve; eu não me esqueço", "De estar a ela um dia reclinado:", "Ali em vale um monte está mudado:", "Quanto pode dos anos o progresso!"),
                                                 LET("Árvores aqui vi tão florescentes,", "Que faziam perpétua a primavera:", "Nem troncos vejo agora decadentes."),
                                                 LET("Eu me engano: a região esta não era;", "Mas que venho a estranhar, se estão presentes", "Meus males, com que tudo degenera!")) + fonte(T(100, 5).replace("Poemas.", "<em>Poemas</em>.")) + p(T(100, 6))}),
11: Q_(101, "Língua Portuguesa", "Coesão textual", "<p>“Acontecendo de o cientista provocar um dano…” equivale a “Se o cientista provocar um dano…”: o rato só deixa de vocalizar se houver a lesão. A relação é de <strong>condição</strong>. Alternativa <strong>C</strong>.</p>",
      ["oração reduzida", "relações lógicas"]),
12: Q_(102, "Língua Portuguesa", "Semântica", "<p>“Mandinga” passou a significar feitiçaria por causa da situação histórica: os portugueses, nas grandes navegações, consideravam bruxos os africanos que indicavam onde havia ouro. O sentido nasceu de um <strong>contexto sócio-histórico</strong>. Alternativa <strong>A</strong>.</p>",
      ["etimologia", "mudança semântica"], trocas=[("O pulo do gato 3", "<em>O pulo do gato 3</em>")]),
13: Q_(103, "Língua Portuguesa", "Argumentação", "<p>O Texto I diz que, no consumismo, as coisas são personificadas e as pessoas, coisificadas; o Texto II, que o código da alma virou código do consumidor. Os dois mostram que o consumo <strong>provoca mudanças nos valores sociais</strong>. Alternativa <strong>B</strong>.</p><p>Só o Texto I menciona as datas comemorativas e a mídia (C e E).</p>",
      ["consumismo", "intertextualidade"], trocas=[("livro O capital,", "livro <em>O capital</em>,")]),
14: Q_(104, "Língua Portuguesa", "Coesão textual", "<p>Antes dos dois pontos, o autor afirma que procurar a essência do conto entre a obra e o autor é um erro; depois deles, explica por quê e onde procurar: entre o texto e o leitor. Os dois pontos servem para <strong>introduzir um argumento esclarecedor</strong>. Alternativa <strong>D</strong>.</p>",
      ["pontuação", "dois-pontos"], trocas=[("De amor e trevas", "<em>De amor e trevas</em>")]),
15: Q_(105, "Língua Portuguesa", "Gêneros textuais", "<p>A campanha mostra a água “invisível” gasta para produzir carne, um lençol de algodão, ovos, pão e cerveja e diz “Economizar bens de consumo e evitar o desperdício também é poupar água”. O leitor é incitado a <strong>adotar práticas de consumo consciente</strong>. Alternativa <strong>A</strong>.</p>",
      ["campanha", "água virtual"],
      extra={"enunciado": "[[fig:1]]" + fonte("<em>National Geographic Brasil</em>, n. 151, out. 2012 (adaptado).") + p(T(105, 1).split("(adaptado). ")[1]),
             "imagens": figs(("q105", "Cartaz “A água invisível”: uma silhueta humana formada por gotas e desenhos, com balões indicando a água gasta na produção de bens; cada quilo de carne bovina exige em média 15 mil litros de água (do alimento do gado à limpeza dos dejetos); 1 copo de cerveja, 75 litros; 1 kg de pão, 1 600 litros; 1 ovo, 3 340 litros; 1 lençol de algodão, 10 600 litros. O texto lembra que o Brasil exporta água na forma de soja e cereais. Embaixo: “Economizar bens de consumo e evitar o desperdício também é poupar água.”"))}),
16: Q_(106, "Língua Portuguesa", "Gêneros digitais", "<p>O texto diz que a internet acabou com o controle sobre quem é dono dos arquivos, e cita Paulo Coelho, que viu as vendas do livro aumentarem depois de ele mesmo divulgar uma versão gratuita. Distribuir cópias passa a ser visto de outro modo: a internet propicia a <strong>reavaliação do conceito de propriedade intelectual</strong>. Alternativa <strong>D</strong>.</p>",
      ["pirataria", "direitos autorais"], trocas=[("livro O alquimista,", "livro <em>O alquimista</em>,"), ("para download", "para <em>download</em>"), ("seu blog,", "seu <em>blog</em>,"), ("Veja, n.", "<em>Veja</em>, n.")]),
17: Q_(107, "Literatura", "Prosa contemporânea", "<p>Hideo, o pai, senta à cabeceira; os filhos homens, à direita e à esquerda, por ordem de nascimento; a esposa e as filhas comem de pé, depois. A posição de cada um à mesa reproduz a hierarquia da família: <strong>o lugar à mesa metaforiza uma estrutura de poder</strong>. Alternativa <strong>E</strong>.</p>",
      ["Oscar Nakasato", "patriarcado"], trocas=[("Nihonjin. São Paulo", "<em>Nihonjin</em>. São Paulo")]),
18: Q_(108, "Língua Portuguesa", "Gêneros textuais", "<p>Os autores descrevem o livro <em>Madeira de ponta a ponta</em>, como foi feito e o que revela, e o avaliam (“olhar jornalístico, crítico e ao mesmo tempo didático”). É um texto de apresentação, para <strong>apresentar informações e comentários sobre o livro</strong>. Alternativa <strong>A</strong>.</p>",
      ["apresentação de livro", "Amazônia"], trocas=[("a obra Madeira de ponta a ponta revela", "a obra <em>Madeira de ponta a ponta</em> revela"), ("Madeira de ponta a ponta: o caminho", "<em>Madeira de ponta a ponta</em>: o caminho")]),
19: Q_(109, "Língua Portuguesa", "Gêneros textuais", "<p>A peça mostra telas de celular sobre uma rua com uma criança atravessando, e diz: “Se você não percebeu a criança aqui, imagine no trânsito. Trânsito sem celular”. O objetivo é <strong>influenciar o comportamento de motoristas em relação ao uso de celular no trânsito</strong>. Alternativa <strong>D</strong>.</p>",
      ["campanha", "linguagem verbal e não verbal"],
      extra={"imagens": figs(("q109", "Peça publicitária: várias imagens de celulares mostrando uma avenida, e numa delas, quase despercebida, uma criança atravessando a rua. Texto: “Se você não percebeu a criança aqui, imagine no trânsito. Trânsito sem celular. Atenda a esse chamado. Seja você a mudança no trânsito.”"))}),
20: Q_(110, "Literatura", "Prosa poética", "<p>A pérola nasce de uma contaminação: a ostra reage a um corpo estranho secretando nácar, camada sobre camada, aos poucos. A autora compara isso à arte, “transformação da dor”: “É preciso continuar secretando o nácar”. A imagem <strong>concebe a criação literária como trabalho progressivo e de autoconhecimento</strong>. Alternativa <strong>C</strong>.</p><p>O sofrimento é o ponto de partida, mas o texto valoriza o trabalho contínuo, não o esquecimento (A).</p>",
      ["Heloisa Seixas", "metáfora"], trocas=[("Pérolas absolutas Há,", "<strong>Pérolas absolutas</strong></p><p class=\"apoio\">Há,"), ("Uma ilha chamada livro", "<em>Uma ilha chamada livro</em>")]),
21: Q_(111, "Literatura", "Canção", "<p>A letra é um diário: o eu lírico registra o que aconteceu “hoje”, encontros e ameaças, e como reagiu a eles (“Mas eu não quebro porque sou macio”). É uma <strong>narrativa autorreflexiva</strong>. Alternativa <strong>E</strong>.</p><p>Os conhecidos e o inimigo são citados, mas não há diálogo com eles (A).</p>",
      ["Chico Buarque", "gênero diário"],
      extra=com_fig(111, "q111", "Trecho da letra “Querido diário”, de Chico Buarque, como aparece na prova: o eu lírico conta ao diário que encontrou conhecidos que lhe desejam o bem e têm pena de sua solidão e, depois, que um inimigo o esperou armado na curva do rio para quebrá-lo, mas ele não se quebra, porque é macio.",
                    enun="[[fig:1]]" + fonte(T(111, 1).replace("Chico. Rio", "<em>Chico</em>. Rio")) + p(T(111, 2)))),
22: Q_(112, "Literatura", "Prosa", "<p>A primeira parte segue o dono, que não entende o que acontece com a galinha; a segunda passa para a própria galinha, que também “não compreendia nada”. O narrador alterna os olhares, com carinho pelos dois: <strong>apropriação de diferentes pontos de vista, incorporados afetivamente</strong>. Alternativa <strong>D</strong>.</p>",
      ["João Alphonsus", "foco narrativo"], trocas=[("Galinha cega O dono", "<strong>Galinha cega</strong></p><p class=\"apoio\">O dono"), ("Contos e novelas", "<em>Contos e novelas</em>")]),
23: Q_(113, "Literatura", "Poesia", "<p>O poeta descreve a escrita como corte: “corto os conectivos/ corto as palavras rentes/ com tesoura de jardim/ cega e bruta/ com facão de mato”, e a marca do corte deve ficar nas palavras que sobram. Ele põe em evidência o <strong>agressivo trabalho de supressão</strong>. Alternativa <strong>C</strong>.</p>",
      ["Armando Freitas Filho", "metapoesia"],
      extra=com_fig(113, "q113", "Poema “Sem acessórios nem som”, de Armando Freitas Filho, como aparece na prova: em versos curtos, o eu lírico diz escrever para se livrar de escrever, sem enfeites; como o pensamento pesa, corta conectivos e palavras com ferramentas rústicas de jardim e de mato, e quer que a marca do corte fique nas palavras que sobraram e no caminho aberto à força.",
                    enun="[[fig:1]]" + fonte(T(113, 1).replace("Máquina de escrever", "<em>Máquina de escrever</em>")) + p(T(113, 2)))),
24: Q_(114, "Artes", "Arte contemporânea", "<p>Em <em>A origem da obra de arte</em>, o visitante pega letras-vaso, planta sementes e forma palavras e frases no campo. A obra só se completa com essa ação: <strong>o observador da obra atua como seu criador</strong>. Alternativa <strong>B</strong>.</p>",
      ["Marilá Dardot", "arte participativa"],
      extra={"enunciado": "[[fig:1]]" + ap(T(114, 1).replace("A origem da obra de arte (2002)", "<em>A origem da obra de arte</em> (2002)")) + fonte(T(114, 2)) + p(T(114, 3)),
             "imagens": figs(("q114", "Foto de um gramado diante de um pavilhão moderno, com dezenas de vasos de cerâmica em forma de letras espalhados pelo chão, alguns com plantas."))}),
25: Q_(115, "Língua Portuguesa", "Variação linguística", "<p>Os poetas não podiam usar “caga-lume”, palavra considerada indecorosa, “em papéis sérios”; por isso se criou “pirilampo”. O tabu é a <strong>restrição ao uso de um vocábulo pouco aceito socialmente</strong>. Alternativa <strong>E</strong>.</p>",
      ["tabu linguístico", "neologismo"], trocas=[("Caminhos do português", "<em>Caminhos do português</em>")]),
26: Q_(116, "Literatura", "Poesia contemporânea", "<p>O poema imita uma lição escolar, definindo gêneros e tipos de lirismo de forma seca e didática. Esse tom explicativo, de manual, é o próprio recurso poético do texto: <strong>o tom explicativo e contido constitui uma forma peculiar de expressão poética</strong>. Alternativa <strong>B</strong>.</p>",
      ["Ana Cristina Cesar", "metapoesia"],
      extra=com_fig(116, "q116", "Poema “Primeira lição”, de Ana Cristina Cesar, como aparece na prova: em tom de lição escolar, lista os gêneros de poesia (lírico, satírico, didático, épico, ligeiro), define o lirismo como linguagem do coração e explica, como num manual, o lirismo elegíaco, bucólico e erótico e os gêneros elegia, nênia, endecha e epitáfio e epicédio.",
                    enun="[[fig:1]]" + fonte(T(116, 1).replace("Poética. São", "<em>Poética</em>. São")) + p(T(116, 2)))),
27: Q_(117, "Língua Portuguesa", "Gêneros textuais", "<p>A repetição de “Você pode não acreditar: mas houve um tempo em que…” apresenta cenas de confiança e convivência: leite e pão deixados na porta, ruas seguras, visitas, namoros no portão. O cronista quer <strong>sensibilizar o leitor sobre o modo como as pessoas se relacionavam entre si num tempo mais aprazível</strong>. Alternativa <strong>B</strong>.</p>",
      ["crônica", "repetição"],
      extra={"enunciado": tit("Você pode não acreditar") + ap(T(117, 0).replace("Você pode não acreditar Você", "Você"), *[T(117, i) for i in range(1, 7)]) + fonte("SANT’ANNA, A. R. <em>Estado de Minas</em>, 5 maio 2013 (fragmento).") + p(T(117, 7).split("(fragmento). ")[1])}),
28: Q_(118, "Língua Portuguesa", "Gêneros textuais", "<p>O texto resume o livro e o avalia: “uma ótima opção”, “obra de fácil leitura”, que aborda a álgebra “de forma interessante, inteligente e acessível”. É uma resenha: busca <strong>fazer a apreciação de uma obra a partir de uma síntese crítica</strong>. Alternativa <strong>C</strong>.</p><p>Com tantas avaliações, o resumo não é impessoal (B).</p>",
      ["resenha", "gêneros textuais"], trocas=[("O livro A fórmula secreta conta", "O livro <em>A fórmula secreta</em> conta"), ("análise, A fórmula secreta apresenta-se", "análise, <em>A fórmula secreta</em> apresenta-se")]),
29: Q_(119, "Literatura", "Prosa", "<p>O narrador se detém na velha: bem-vestida, cheia de joias, mas com rugas que “disfarçavam” o rosto de antes, e comenta: “Chega-se a um certo ponto — e o que foi não importa”. A filha a deixa no trem, e ela fica sozinha, sensível a um gesto de uma desconhecida. O fragmento enfatiza o <strong>sentimento de solidão alimentado pelo processo de envelhecimento</strong>. Alternativa <strong>E</strong>.</p><p>O incômodo com a gentileza de Angela (D) é um sintoma desse isolamento, não o foco principal.</p>",
      ["Clarice Lispector", "conto"], trocas=[("A partida de trem Marcava", "<strong>A partida de trem</strong></p><p class=\"apoio\">Marcava"), ("Onde estivestes de noite", "<em>Onde estivestes de noite</em>"), ("bem- vestida", "bem-vestida"), ("do Opala da", "do <em>Opala</em> da")]),
30: Q_(120, "Literatura", "Poesia", "<p>Cada geração achou “normal” o que fazia: apanhar e bater fazia parte do senso comum sobre como educar, até que se descobriu que estava errado. O eu lírico, da geração do meio, errou ao aceitar e ao repetir esse comportamento. A angústia vem da <strong>consciência das imperfeições aceitas na construção do senso comum</strong>. Alternativa <strong>B</strong>.</p><p>A revolta das novas gerações (C) é citada, mas a angústia é do eu lírico, que percebe o próprio erro.</p>",
      ["Jaguar Wanderley", "gerações"],
      extra=com_fig(120, "q120", "Trecho do poema “Esses chopes dourados”, de J. Wanderley, como aparece na prova: o eu lírico conta que a geração de seu pai batia na dele, que achava isso normal; a dele bateu na seguinte sem saber que era errado, e a seguinte cresceu com ódio; agora que todas as gerações sabem, é péssimo ter sido a do meio, que errou ao apanhar e ao bater, e que se descobre inocente apesar de amaldiçoada.",
                    enun="[[fig:1]]" + fonte(T(120, 2).replace("Os cem melhores poemas brasileiros do século", "<em>Os cem melhores poemas brasileiros do século</em>")) + p(T(120, 3)))),
31: Q_(121, "Literatura", "Geração de 45", "<p>O poeta recusa usar “flor” no sentido gasto e diz “Flor é a palavra/ flor”, e passa a recriá-la por imagens: o salto da ave, o salto fora do sono, uma explosão, uma máquina. Ele propõe a recriação de <strong>uma palavra, a partir de imagens com as quais ela pode ser comparada, a fim de assumir novos significados</strong>. Alternativa <strong>A</strong>.</p>",
      ["João Cabral", "metalinguagem"],
      extra=com_fig(121, "q121", "Trecho do poema “Antiode”, de João Cabral de Melo Neto, como aparece na prova: o eu lírico diz à poesia que não a escreverá no sentido gasto de “flor”, como virtude ou enfeite, e afirma que flor é a palavra flor, que ele compara ao salto de uma ave para o voo, ao despertar do sono, a uma explosão posta a funcionar como uma máquina.",
                    enun="[[fig:1]]" + fonte(T(121, 1).replace("Psicologia da composição", "<em>Psicologia da composição</em>")) + p(T(121, 2)))),
32: Q_(122, "Língua Portuguesa", "Gêneros textuais", "<p>A campanha explica que nenhum teste pega todas as infecções (há a janela imunológica) e termina em destaque: “DA SUA HONESTIDADE DEPENDE A VIDA DE QUEM VAI RECEBER SEU SANGUE”. O objetivo é <strong>conscientizar o doador de sua corresponsabilidade pela qualidade do sangue</strong>. Alternativa <strong>A</strong>.</p>",
      ["campanha", "doação de sangue"], trocas=[("Qual é a segurança do sangue? Para", "<strong>Qual é a segurança do sangue?</strong></p><p class=\"apoio\">Para")]),
33: Q_(123, "Língua Portuguesa", "Variação linguística", "<p>O Texto I tem as marcas da fala (pausas, hesitações), e o Texto II é sua versão escrita, revisada. Mas em ambos a professora usa a variedade de prestígio das pessoas escolarizadas da cidade: são <strong>amostras do português culto urbano</strong>. Alternativa <strong>E</strong>.</p><p>Hesitações e reformulações (A) só aparecem no Texto I.</p>",
      ["fala e escrita", "retextualização"], trocas=[("Da fala para a escrita", "<em>Da fala para a escrita</em>")]),
34: Q_(124, "Língua Portuguesa", "Variação linguística", "<p>Os personagens discutem se “outrossim”, “óbice”, “ônus” e “resquício” são palavras “de domingo” ou “de segunda-feira”: são palavras formais, de documentos, que eles tratam como se tivessem dia certo de uso. O efeito é o <strong>tom humorístico, ocasionado pela ocorrência de palavras empregadas em contextos formais</strong>. Alternativa <strong>B</strong>.</p>",
      ["Verissimo", "humor"], trocas=[("De domingo — Outrossim…", "<strong>De domingo</strong></p><p class=\"apoio\">— Outrossim…"), ("Comédias da vida privada", "<em>Comédias da vida privada</em>")]),
35: Q_(125, "Literatura", "Gêneros textuais", "<p>O poema usa a forma da receita, com verbos de instrução (“Tome-se”, “Deita-se”, “se reforce”) e quantidades (“Três gotas de tristeza”, “uma pitada de morte”), para falar do amor do poeta. A mescla está em que ele <strong>introduz procedimentos prescritivos na composição do poema</strong>. Alternativa <strong>A</strong>.</p>",
      ["Saramago", "hibridismo de gêneros"],
      extra=com_fig(125, "q125", "Poema “Receita”, de José Saramago, como aparece na prova: em forma de receita culinária, manda tomar um poeta, uma nuvem de sonho, uma flor, gotas de tristeza e uma veia sangrando de pavor e, quando a massa ferve, juntar a luz de um corpo de mulher e uma pitada de morte, que é o que um amor de poeta requer.",
                    enun="[[fig:1]]" + fonte(T(125, 1).replace("Os poemas possíveis", "<em>Os poemas possíveis</em>")) + p(T(125, 2)))),
36: Q_(126, "Artes", "Teatro", "<p>A foto mostra os atores do Grupo Galpão ao ar livre, cercados de espectadores sentados no chão, sem palco ou teatro. O que caracteriza o teatro de rua é <strong>dispensar o edifício teatral para a sua realização</strong>. Alternativa <strong>A</strong>.</p><p>Há figurinos e elementos de circo (B e C), mas eles podem estar em qualquer teatro.</p>",
      ["teatro de rua", "Grupo Galpão"],
      extra={"enunciado": "[[fig:1]]" + fonte("Espetáculo <em>Romeu e Julieta</em>, Grupo Galpão. GUTO MUNIZ. Disponível em: www.focoincena.com.br. Acesso em: 30 maio 2016.") + p(T(126, 2)),
             "imagens": figs(("q126", "Foto em preto e branco de um espetáculo ao ar livre: uma atriz de vestido largo dança diante da plateia sentada no chão, e outro ator, de guarda-chuva, aparece no alto de uma escada."))}),
37: Q_(127, "Língua Portuguesa", "Gêneros textuais", "<p>Possenti diz que estuda piadas pela sua constituição linguística e que elas dão “uma coleção de fatos e dados impressionantes” sobre a língua e a sociedade. A piada é destacada pelo <strong>seu potencial como objeto de investigação</strong>. Alternativa <strong>E</strong>.</p>",
      ["piada", "linguística"], trocas=[("O humor e a língua Há", "<strong>O humor e a língua</strong></p><p class=\"apoio\">Há"), ("Ciência Hoje, n.", "<em>Ciência Hoje</em>, n.")]),
38: Q_(128, "Educação Física", "Gênero e esporte", "<p>Maggie insiste em treinar boxe, esporte visto como masculino, mesmo depois de ouvir “Eu não treino garotas”. Sua atitude representa a <strong>transposição de limites impostos à mulher num espaço de predomínio masculino</strong>. Alternativa <strong>C</strong>.</p>",
      ["boxe", "feminilidades"], trocas=[("O filme Menina de ouro conta", "O filme <em>Menina de ouro</em> conta"), ("Menina de ouro e a representação", "<em>Menina de ouro</em> e a representação")]),
39: Q_(129, "Educação Física", "Saúde", "<p>Uma visão ampliada de saúde considera também as condições sociais e econômicas, não só o corpo. Terezinha diz que seu principal desafio foi a falta de recursos financeiros: sem dinheiro para um atleta-guia, treinava sozinha e sofria quedas e trombadas. O fator que revela essa perspectiva é a <strong>condição financeira</strong>. Alternativa <strong>B</strong>.</p><p>Nutrição, prevenção de lesões e treino (A, C e D) são cuidados que ela só passou a ter quando teve recursos.</p>",
      ["esporte paralímpico", "saúde integral"], trocas=[("Entrevista com Terezinha Guilhermina Terezinha", "<strong>Entrevista com Terezinha Guilhermina</strong></p><p class=\"apoio\">Terezinha"), ("no Guinness Book", "no <em>Guinness Book</em>"), ("atletaguia", "atleta-guia")]),
40: Q_(130, "Educação Física", "Esportes coletivos", "<p>O drible é a ação de quem tem a bola para avançar em direção ao gol, superando o marcador. Ele corresponde à <strong>progressão da equipe</strong> com a posse da bola em direção ao alvo adversário. Alternativa <strong>B</strong>.</p>",
      ["handebol", "princípios operacionais"]),
41: Q_(131, "Língua Portuguesa", "Gêneros textuais", "<p>Machado diz que os jornais velhos provocam “a recomposição do extinto, a revivescência do passado”, como as ruínas de uma civilização. O jornal é visto como <strong>instrumento de reconstrução da memória</strong>. Alternativa <strong>C</strong>.</p>",
      ["Machado de Assis", "crônica"], trocas=[("BONS DIAS! 14 de junho de 1889", "BONS DIAS!</strong></p><p class=\"apoio\"><em>14 de junho de 1889</em><strong>"), ("Bons dias! (Crônicas", "<em>Bons dias!</em> (Crônicas")]),
42: Q_(132, "Artes", "Arte moderna", "<p>Bacon pinta o próprio rosto deformado, e Duras descreve o seu como “destruído”. A arte do século XX, marcada pelas guerras e pela descoberta do inconsciente, deixou de representar o sujeito como inteiro e estável. A deformação vem <strong>das catástrofes que assolaram o século XX e da descoberta de uma realidade psíquica pela psicanálise</strong>. Alternativa <strong>B</strong>.</p>",
      ["Francis Bacon", "subjetividade moderna"],
      extra={"enunciado": tit("TEXTO I") + "[[fig:1]]" + fonte("BACON, F. <em>Três estudos para um autorretrato</em>. Óleo sobre tela, 37,5 x 31,8 cm (cada), 1974. Disponível em: www.metmuseum.org. Acesso em: 30 maio 2016.") + tit("TEXTO II") + ap(T(132, 4)) + fonte(T(132, 5).replace("O amante.", "<em>O amante</em>.")) + p(T(132, 6)),
             "imagens": figs(("q132", "Três retratos lado a lado do pintor Francis Bacon, com o rosto deformado por pinceladas fortes, manchas e partes que parecem arrancadas."))}),
43: Q_(133, "Literatura", "Teatro", "<p>O trecho tem as indicações entre parênteses e em maiúsculas (“De súbito, pedagógica, volta-se para o homem”, “FAZ UMA PAUSA”, “O HOMEM TORNA A SE DEBATER”), que orientam gestos e movimentos dos atores. O que o caracteriza como texto teatral é o <strong>uso de rubricas para construir a ação dramática</strong>. Alternativa <strong>D</strong>.</p><p>Não há narrador no texto teatral (C).</p>",
      ["rubrica", "texto dramático"], trocas=[("Lições de motim DONA COTINHA", "<strong>Lições de motim</strong></p><p class=\"apoio\">DONA COTINHA"), ("Lições de motim. Goiânia", "<em>Lições de motim</em>. Goiânia"), ("caracteriza Lições de motim como", "caracteriza <em>Lições de motim</em> como")]),
44: Q_(134, "Artes", "Música", "<p>O texto destaca o “paradoxo”: Túlio Piva, gaúcho de família italiana, nascido na fronteira com a Argentina, falava de samba, morro e mulata com categoria. O contraste valoriza o artista: <strong>contraste entre o local de nascimento e a escolha pelo gênero samba</strong>. Alternativa <strong>A</strong>.</p>",
      ["samba", "crítica musical"], trocas=[("Tem que ter mulata,", "<em>Tem que ter mulata</em>,")]),
45: Q_(135, "Literatura", "Miniconto", "<p>O diálogo sugere que uma criança, brincando de pegador, levou cinco tiros de um policial. As reticências em “O PM pensou que…” deixam para o leitor completar o que o PM pensou (que ela era um criminoso). Indicam <strong>uma informação implícita</strong>. Alternativa <strong>B</strong>.</p>",
      ["reticências", "miniconto"],
      extra={"enunciado": tit("L.J.C.") + ap(LET("— 5 tiros?", "— É.", "— Brincando de pegador?", "— É. O PM pensou que…", "— Hoje?", "— Cedinho.")) + fonte(T(135, 1).replace("Os cem menores contos brasileiros do século", "<em>Os cem menores contos brasileiros do século</em>")) + p(T(135, 2))}),
}


def montar(lingua):
    Q = dict(ING if lingua == "ingles" else ESP)
    Q.update(COMUM)
    return Q
