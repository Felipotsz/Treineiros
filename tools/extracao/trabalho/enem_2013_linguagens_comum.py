# Enem 2013, 2º dia, caderno azul: Linguagens (questões 91 a 135; no site, 1 a 45). Em 2013 Linguagens e Matemática eram no 2º dia.
# Duas provas: enem-2013-linguagens-ingles (91–95 = inglês) e enem-2013-linguagens-espanhol (91–95 = espanhol); 96–135 iguais.
# Letras e poemas modernos como imagem (alt descreve, não transcreve): Q92-es (Duerme negrito), Q94-es (Gloria Fuertes), Q100 (Gabriel, o Pensador),
# Q104 (Nuno Júdice), Q113 (Adélia Prado) e os trechos de canções nas alternativas da Q117.
# Em texto, domínio público: Q99 (Jorge de Lima, m. 1953) e Q116 (Raimundo Correia).
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent / "tools"))
from enem_aj import carregar_enem, enunciado_enem, paragrafos_enem

D = carregar_enem("enem-2013-dia2-azul")
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
ALT = lambda ini: {k: f"[[fig:{i}]]" for i, k in enumerate("ABCDE", ini)}

ING = {
1: Q_(91, "Inglês", "Interpretação de texto", "<p>A manchete diz “After prison blaze kills hundreds in Honduras, UN warns on overcrowding”: depois de um incêndio que matou centenas numa prisão de Honduras, a ONU alerta para a superlotação. O fato reportado é a <strong>ocorrência de um incêndio em um presídio superlotado em Honduras</strong>. Alternativa <strong>A</strong>.</p><p>A superlotação (B) é o tema do alerta da ONU, motivado pelo acontecimento, que é o incêndio.</p>",
      ["notícia", "manchete"],
      extra={"enunciado": tit("After prison blaze kills hundreds in Honduras, UN warns on overcrowding") + ap("15 February 2012", T(91, 2)) + fonte(T(91, 3)) + p(T(91, 4))}),
2: Q_(92, "Inglês", "Interpretação de texto", "<p>O texto diz que “humans and other mammals possess the same chemical road map for making it”, ou seja, humanos e outros mamíferos têm o mesmo “mapa químico” para produzir morfina, assim como os ratos estudados. O estudante descobriu que <strong>os ratos e os humanos possuem a mesma via metabólica para produção de morfina</strong>. Alternativa <strong>B</strong>.</p><p>O texto fala em “small steady amount”, uma quantidade pequena, e não grande (C).</p>",
      ["divulgação científica", "vocabulário"],
      extra={"enunciado": tit("National Geographic News") + ap("Christine Dell’Amore — Published April 26, 2010", T(92, 1)) + fonte(T(92, 2)) + p(T(92, 3).replace("na National Geographic", "na <em>National Geographic</em>"))}),
3: Q_(93, "Inglês", "Interpretação de texto", "<p>O texto chama Jobs de “Tech-Guru” e “Artist”, diz que suas conquistas são “staggering” (impressionantes) e que a revista “pays our respects to a digital pioneer”, homenageando um pioneiro digital. Ele se propõe a <strong>enaltecer sua contribuição para o mundo digital</strong>. Alternativa <strong>C</strong>.</p><p>O texto anuncia que vai relembrar as conquistas, mas não as descreve (B).</p>",
      ["homenagem", "biografia"]),
4: Q_(94, "Inglês", "Interpretação de texto", "<p>A quarta dica é “Spread your own culture around the world and learn about other cultures”: divulgar a própria cultura e conhecer outras. O comentário que faz as duas coisas é o de quem entrou num programa “para mostrar o que tem de bom em meu país e conhecer outras formas de ser”. Alternativa <strong>C</strong>.</p><p>As outras opções só aprendem sobre outras culturas, sem divulgar a própria.</p>",
      ["campanha", "diversidade cultural"],
      extra={"enunciado": tit("Do one thing for diversity and inclusion") + ap(T(94, 1), "<strong>" + T(94, 2) + "</strong>", "<br>".join(T(94, i) for i in range(3, 8)), T(94, 8)) + fonte(T(94, 9)) + p(T(94, 10).replace("on-line", "<em>on-line</em>"))}),
5: Q_(95, "Inglês", "Interpretação de texto", "<p>Calvin diz que nada que é ruim é culpa dele, que é vítima de más influências, e por isso não assume responsabilidade. No último quadro, o pai o manda tirar a neve com a pá, e ele reclama: “These discussions never go where they’re supposed to”. Calvin <strong>comenta que suas discussões com o pai não correspondem às suas expectativas</strong>. Alternativa <strong>C</strong>.</p><p>Ele não decide tirar a neve (A): é mandado a fazer isso.</p>",
      ["tirinha", "Calvin"],
      extra=com_fig(95, "q95", "Tirinha de Calvin e Haroldo em quatro quadros, em inglês. Calvin diz ao pai, que lê o jornal na poltrona, que concluiu que nada de ruim que faz é culpa dele: é jovem e influenciável, vítima de uma cultura que estimula valores ruins. O pai responde que vai ajudá-lo a desenvolver o caráter e o manda tirar a neve com a pá. No último quadro, Calvin, com a pá na neve, reclama que essas discussões nunca vão para onde deveriam.")),
}

ESP = {
1: Q_("91-es", "Espanhol", "Interpretação de texto", "<p>Dois homens à moda antiga parecem prontos para um duelo: um diz “¡Lo reto a un duelo!”, e o outro aceita, mas propõe que um use o <em>joystick</em> e o outro, as teclas. As armas seriam controles de videogame. O humor está na <strong>sugestão de armas não convencionais para um duelo</strong>. Alternativa <strong>C</strong>.</p><p>O comentário “Ya no es como antes” se refere à mudança de costumes, e não a um deslocamento no tempo (D).</p>",
      ["charge", "humor"],
      extra=com_fig("91-es", "q91es", "Charge de Tute: dois homens de chapéu e cachecol, frente a frente. Um diz “¡Lo reto a un duelo!”, e o outro responde “Está bien, pardo. Pero yo con el joystick y uste con las teclas”. No alto, um quadro diz “Ya no es como antes...”.",
                    enun="[[fig:1]]" + fonte("TUTE. <em>Tutelandia</em>. Disponível em: www.gocomics.com. Acesso em: 20 fev. 2012.") + p(T("91-es", 2)))),
2: Q_("92-es", "Espanhol", "Interpretação de texto", "<p>A mãe está no campo trabalhando para trazer comida ao filho, e a cantiga diz: “Trabajando y no le pagan”. A canção denuncia trabalho sem pagamento: <strong>retrata a precariedade das relações de trabalho no campo</strong>. Alternativa <strong>C</strong>.</p><p>A mãe está ausente por necessidade, e não por falta de afeto (B).</p>",
      ["cantiga de ninar", "trabalho rural"],
      extra=com_fig("92-es", "q92es", "Letra da cantiga “Duerme negrito”, em espanhol: a voz embala o menino dizendo que a mãe está no campo e vai lhe trazer comida e outras coisas, e termina contando que ela trabalha duramente e não recebe pagamento.",
                    enun="[[fig:1]]" + fonte("Disponível em: http://letras.mus.br. Acesso em: 26 jun. 2012 (fragmento).") + p("<em>Duerme negrito</em> é uma cantiga de ninar da cultura popular hispânica, cuja letra problematiza uma questão social, ao"))),
3: Q_("93-es", "Espanhol", "Interpretação de texto", "<p>O texto diz que Cortés fez de Malintzin “su intérprete y amante” e que ela lhe ensinou “que algo estaba podrido en el reino de Moctezuma”, que o império “tenía pies de barro”. Ela atuou como <strong>intérprete do conquistador, possibilitando-lhe conhecer as fragilidades do Império</strong>. Alternativa <strong>A</strong>.</p><p>Ela foi também amante (C), mas o texto destaca o papel de intérprete na conquista.</p>",
      ["Malinche", "conquista do México"], trocas=[("El espejo enterrado", "<em>El espejo enterrado</em>")]),
4: Q_("94-es", "Espanhol", "Interpretação de texto", "<p>“Tener mala leche” é ter mau humor, mau gênio. No quinto verso, o eu lírico diz “En vez de mala leche yo doy llanto”: em vez de mau humor, ela dá choro. Ela se apresenta como pessoa <strong>capaz de transformar mau humor em pranto</strong>. Alternativa <strong>E</strong>.</p><p>A coragem (D) aparece em outro verso (“Por lo más peligroso me paseo”), e não na expressão “mala leche”.</p>",
      ["expressão idiomática", "poema"],
      extra=com_fig("94-es", "q94es", "Poema “Cabra sola”, de Gloria Fuertes, em espanhol: o eu lírico conta que dizem que é como a cabra, mas uma cabra estranha, que em vez de mau gênio dá choro, passeia pelo perigoso, se dá bem com todos os bichos e vive sozinha, sem companhia, e diz que, se sofrer é ser como uma cabra, então ela é.",
                    enun="[[fig:1]]" + fonte("FUERTES, G. <em>Poeta de guardia</em>. Barcelona: Lumen, 1990.") + p(T("94-es", 2)))),
5: Q_("95-es", "Espanhol", "Interpretação de texto", "<p>O autor critica a unificação imposta pela Espanha e defende que cada país desenvolveu cultura e espanhol próprios: “ninguno vale más que otro” e o espanhol atual “es el conjunto de veintidós españoles nacionales”. As <strong>variedades do espanhol têm igual relevância linguística e cultural</strong>. Alternativa <strong>B</strong>.</p><p>O texto diz que a unificação empobrece, e não enriquece, a língua (E).</p>",
      ["variação linguística", "espanhol"],
      extra={"enunciado": tit("Pensar la lengua del siglo XXI") + ap(LIMPA(T("95-es", 0)).replace("Pensar la lengua del siglo XXI ", "").replace("pluricéntrica", "<em>pluricéntrica</em>"), LIMPA(T("95-es", 1))) + fonte(T("95-es", 2)) + p(T("95-es", 3))}),
}

COMUM = {
6: Q_(96, "Língua Portuguesa", "Gêneros textuais", "<p>A redação escolar de 1911 descreve a bandeira com exaltação (“a mais bonita de todas”) e diz que o verde indica as matas e o amarelo as riquezas. Para o leitor de hoje, o documento mostra como a escola <strong>funcionava como veículo de transmissão de valores patrióticos próprios do período</strong>. Alternativa <strong>A</strong>.</p><p>O texto é uma descrição de aluno, e não um manual de comportamento em eventos cívicos (B).</p>",
      ["documento histórico", "patriotismo"],
      extra=com_fig(96, "q96", "Manuscrito escolar de 1911, do Grupo Escolar de Palmeiras, com o desenho de uma bandeira do Brasil num mastro e o texto “A nossa bandeira”: um trecho de poema e uma descrição em letra cursiva, dizendo que a bandeira brasileira é a mais bonita de todas, que o verde indica as matas, o amarelo as riquezas, a esfera azul o céu, as estrelas os estados, e a faixa traz o lema “Ordem e Progresso”, terminando com “Salve! Bandeira Brazileira”.",
                    enun="[[fig:1]]" + fonte("GRUPO ESCOLAR DE PALMEIRAS. <em>Redações de Maria Anna de Biase e J. B. Pereira sobre a Bandeira Nacional</em>. Palmeiras (SP), 18 nov. 1911. Acervo APESP. Coleção DAESP. C10279. Disponível em: www.arquivoestado.sp.gov.br. Acesso em: 15 maio 2013.") + p(T(96, 2).replace("on-line", "<em>on-line</em>"))),
      alts={**D[96]["alternativas"], "D": "argumenta em favor da construção de uma nação com igualdade de direitos.", "E": "apresenta uma metodologia de ensino restrita a uma determinada época."}),
7: Q_(97, "Educação Física", "Jogo", "<p>Huizinga define o jogo como atividade livre, com fim em si mesma, acompanhada de “tensão e alegria” e da consciência de ser diferente da vida cotidiana. A fruição acontece pelo <strong>caráter lúdico, que permite experiências inusitadas</strong>. Alternativa <strong>D</strong>.</p><p>Competitividade e refinamento técnico (B e C) são marcas do esporte, e não do jogo como Huizinga o define.</p>",
      ["Huizinga", "ludicidade"], trocas=[("Homo ludens", "<em>Homo ludens</em>")]),
8: Q_(98, "Língua Portuguesa", "Argumentação", "<p>As formas destacadas, “carregamos”, “podemos”, “desenvolvemos”, “somos” e “controlamos”, estão na primeira pessoa do plural: o autor se inclui junto com o leitor. Assim, ele <strong>torna o leitor copartícipe do ponto de vista de que ele manipula as novas tecnologias e por elas é manipulado</strong>. Alternativa <strong>D</strong>.</p><p>O texto diz que controlamos e somos controlados, e não só que somos controlados (C).</p>",
      ["primeira pessoa do plural", "artigo de opinião"],
      extra={"enunciado": tit("Novas tecnologias") + ap(T(98, 0).replace("Novas tecnologias ", "").replace("Por esse motivo carregamos", "Por esse motivo <strong>carregamos</strong>"),
                                                    T(98, 1).replace("não podemos", "não <strong>podemos</strong>").replace("desenvolvemos", "<strong>desenvolvemos</strong>"),
                                                    T(98, 2).replace("somos livres", "<strong>somos</strong> livres").replace("tanto controlamos", "tanto <strong>controlamos</strong>"))
             + fonte(T(98, 3).replace("A microfísica do espetáculo", "<em>A microfísica do espetáculo</em>")) + p(T(98, 4))}),
9: Q_(99, "Literatura", "Modernismo", "<p>O eu lírico diz que as gerações tentarão apagar a cor do negro, mas “não apagarão de suas almas, a tua alma”, e enumera figuras da resistência e da escravidão (Zumbi, negro-fujão, negro rebelde). Diz ainda que a raça branca, que o enforcou, “enforca-se de tédio”. Há <strong>preservação da memória ancestral e resistência negra à apatia cultural dos brancos</strong>. Alternativa <strong>B</strong>.</p>",
      ["Jorge de Lima", "negritude"],
      extra={"enunciado": tit("Olá! Negro") + ap("<br>".join([
          "Os netos de teus mulatos e de teus cafuzos", "e a quarta e a quinta gerações de teu sangue sofredor", "tentarão apagar a tua cor!",
          "E as gerações dessas gerações quando apagarem", "a tua tatuagem execranda,", "não apagarão de suas almas, a tua alma, negro!",
          "Pai-João, Mãe-negra, Fulô, Zumbi,", "negro-fujão, negro cativo, negro rebelde", "negro cabinda, negro congo, negro ioruba,",
          "negro que foste para o algodão de USA", "para os canaviais do Brasil,", "para o tronco, para o colar de ferro, para a canga",
          "de todos os senhores do mundo;", "eu melhor compreendo agora os teus <em>blues</em>", "nesta hora triste da raça branca, negro!",
          "Olá, Negro! Olá, Negro!", "A raça que te enforca, enforca-se de tédio, negro!"]))
          + fonte("LIMA, J. <em>Obras completas</em>. Rio de Janeiro: Aguilar, 1958 (fragmento).") + p(T(99, 3))}),
10: Q_(100, "Língua Portuguesa", "Variação linguística", "<p>A letra usa formas da fala do dia a dia: “pro céu”, “pra fazer”, “levanta aí”, “se liga aí”, “pode crer”, “te botaram”. Essas escolhas dão ao texto <strong>espontaneidade, pelo uso da linguagem coloquial</strong>. Alternativa <strong>D</strong>.</p><p>Não há linguagem própria da internet (A), e as expressões são coloquiais, mais do que gírias de um grupo (C).</p>",
      ["linguagem coloquial", "rap"],
      extra=com_fig(100, "q100", "Trecho da letra de “Até quando?”, de Gabriel, o Pensador: o eu lírico diz ao ouvinte que não adianta olhar para o céu com muita fé e pouca luta, que ele deve protestar e fazer greve, e que não é porque Jesus sofreu que ele tem de sofrer.",
                    enun="[[fig:1]]" + fonte("GABRIEL, O PENSADOR. <em>Seja você mesmo (mas não seja sempre o mesmo)</em>. Rio de Janeiro: Sony Music, 2001 (fragmento).") + p(T(100, 3)))),
11: Q_(101, "Língua Portuguesa", "Interpretação de texto", "<p>Cada quadrado da manta fazia a avó lembrar uma história, e, quando os retalhos se gastavam, eram trocados por outros, com novas histórias. A valorização se evidencia pela <strong>correlação entre os retalhos da manta e as muitas histórias de tradição oral que os formavam</strong>. Alternativa <strong>E</strong>.</p><p>A comparação com joias e palácios (A) aparece só como pergunta retórica no início.</p>",
      ["resenha", "memória"],
      extra={"enunciado": tit(T(101, 0)) + ap(T(101, 1)) + fonte(T(101, 2).replace("Língua Portuguesa", "<em>Língua Portuguesa</em>")) + p(T(101, 3))}),
12: Q_(102, "Língua Portuguesa", "Gêneros digitais", "<p>A autora diz que o hipertexto redefine os papéis de autor e leitor e revisa os modelos de leitura e escrita, e que não se limita ao meio eletrônico, pois também pode existir no papel. Ele é um <strong>novo modo de leitura e de organização da escrita</strong>. Alternativa <strong>C</strong>.</p><p>O texto nega que o hipertexto seja exclusivo dos meios eletrônicos (A e B).</p>",
      ["hipertexto", "leitura"], trocas=[("Educação na cibercultura", "<em>Educação na cibercultura</em>")]),
13: Q_(103, "Língua Portuguesa", "Gêneros textuais", "<p>O cartaz mostra uma gota com o planeta dentro, caindo de uma torneira, e conjuga o verbo “derreter”: “Eu derreto. Tu derretes. Você derrete...você tem certeza que quer conjugar este verbo?”. A pergunta põe a escolha nas mãos do leitor: <strong>a agressão ao planeta é dependente da posição assumida pelo homem frente aos problemas ambientais</strong>. Alternativa <strong>E</strong>.</p>",
      ["propaganda", "aquecimento global"],
      extra=com_fig(103, "q103", "Cartaz: de uma torneira cai uma gota de água com o planeta Terra dentro. Texto: “Eu derreto. Tu derretes. Você derrete...você tem certeza que quer conjugar este verbo?”")),
14: Q_(104, "Literatura", "Funções da linguagem", "<p>O poeta começa com o verbete do dicionário e conta que não pode escrever o poema sobre a “rapariga” porque, no Brasil, a palavra tem outro sentido; acaba decidindo escrever sobre o café. O texto fala do próprio processo de escrever o poema: há <strong>tematização do fazer artístico, pela discussão do ato de construção da própria obra</strong>. Alternativa <strong>D</strong>.</p>",
      ["metalinguagem", "variação lexical"],
      extra=com_fig(104, "q104", "Poema “Lusofonia”, de Nuno Júdice, como aparece na prova: começa com o verbete do dicionário para “rapariga” (moça em Portugal, meretriz no Brasil). O eu lírico conta que queria escrever um poema sobre uma rapariga sentada num café de Lisboa, mas, por causa do sentido da palavra no Brasil, teria de trocá-la por outras e, no fim, decide escrever um poema sobre o café.",
                    enun="[[fig:1]]" + fonte("JÚDICE, N. <em>Matéria do Poema</em>. Lisboa: D. Quixote, 2008.") + p(T(104, 3)))),
15: Q_(105, "Língua Portuguesa", "Gêneros textuais", "<p>Uma lei precisa ser interpretada do mesmo jeito por todos. O Estatuto define com exatidão quem é criança e quem é adolescente e lista os direitos de forma precisa, sem margem a interpretações diferentes. Destaca-se o emprego de <strong>palavras e construções que evitem ambiguidade</strong>. Alternativa <strong>B</strong>.</p><p>O texto legal não usa expressões informais (C) nem exemplos (E).</p>",
      ["texto legal", "precisão"],
      extra={"enunciado": ap(T(105, 0), T(105, 1), T(105, 2)) + fonte("BRASIL. Lei n. 8 069, de 13 de julho de 1990. <em>Estatuto da criança e do adolescente</em>. Disponível em: www.planalto.gov.br (fragmento).")
             + p(T(105, 4).replace("Disponível em: www.planalto.gov.br (fragmento). ", "").replace("o Estatuto da criança e do adolescente", "o <em>Estatuto da criança e do adolescente</em>"))}),
16: Q_(106, "Língua Portuguesa", "Tecnologias da comunicação", "<p>Castells diz que os movimentos culturais se constroem em torno dos sistemas de comunicação, como a internet, porque é por eles que chegam às pessoas. A mobilização pelas redes sociais no Egito confirma que <strong>os sistemas de comunicação são mecanismos importantes de adesão e compartilhamento de valores sociais</strong>. Alternativa <strong>E</strong>.</p><p>A internet difunde valores, mas não os atribui (A).</p>",
      ["redes sociais", "Primavera Árabe"]),
17: Q_(107, "Língua Portuguesa", "Gêneros textuais", "<p>O edital publica o tombamento de imóveis da Rua Augusta, ou seja, o reconhecimento deles como patrimônio a ser preservado. O leitor que concorda com a decisão diria: “Congratulações! <strong>O patrimônio histórico da cidade merece todo empenho para ser preservado</strong>.” Alternativa <strong>E</strong>.</p><p>Tombar não é derrubar (A), nem construir moradias populares (D).</p>",
      ["tombamento", "edital"],
      extra={"enunciado": tit("Secretaria de Cultura<br>EDITAL") + ap(T(107, 1), T(107, 2)) + fonte("<em>Folha de S. Paulo</em>, 5 ago. 2011 (adaptado).")
             + p(T(107, 3).replace("Folha de S. Paulo, 5 ago. 2011 (adaptado). ", ""))}),
18: Q_(108, "Educação Física", "Saúde e atividade física", "<p>O texto culpa a alimentação com muito sal e açúcar, pouco leite, frutas e feijão, e a preguiça, já que as meninas do programa não praticavam esporte. E diz que as doenças que viriam na velhice, como hipertensão e diabetes, já aparecem nos jovens. Isso indica que <strong>a falta de atividade física somada a uma alimentação nutricionalmente desequilibrada constituem fatores relacionados ao aparecimento de doenças crônicas entre os adolescentes</strong>. Alternativa <strong>A</strong>.</p>",
      ["sedentarismo", "obesidade"], trocas=[("Revista Saúde", "<em>Revista Saúde</em>")]),
19: Q_(109, "Artes", "Artes visuais", "<p>A ilustração mostra um menino puxando um vagão de trem pesado enquanto outro menino, ao lado, puxa um trenzinho de brinquedo. Sem texto, a imagem contrapõe duas infâncias e leva o espectador a pensar sobre o trabalho infantil. A arte serve para <strong>provocar a reflexão sobre essa realidade</strong>. Alternativa <strong>C</strong>.</p><p>A obra não propõe soluções (D) nem mostra vários países (E).</p>",
      ["trabalho infantil", "ilustração"],
      extra=com_fig(109, "q109", "Ilustração de Pawel Kuczynski: um menino magro, com uma corda no ombro, faz força para puxar um vagão de trem carregado de carvão; ao lado, outro menino, de boné, olha para ele segurando a corda de um trenzinho de brinquedo.",
                    enun="[[fig:1]]" + fonte("KUCZYNSKIEGO, P. <em>Ilustração</em>, 2008. Disponível em: http://capu.pl. Acesso em: 3 ago. 2012.") + p(T(109, 2).replace("Disponível em: http://capu.pl. Acesso em: 3 ago. 2012. ", "")))),
20: Q_(110, "Artes", "Artes visuais", "<p>O cartum mostra várias figuras iguais, com cabeças que parecem chaves de dar corda, como brinquedos que repetem o mesmo movimento. Só uma figura escura, no canto, é diferente. Ela representa a <strong>reação ao controle do pensamento coletivo</strong>. Alternativa <strong>E</strong>.</p><p>A figura não é oprimida pelas outras (A): ela se destaca por não seguir o padrão.</p>",
      ["cartum", "individualidade"],
      extra=com_fig(110, "q110", "Cartum de Caulos: muitas figuras brancas iguais, com cabeças em forma de chave de dar corda, e, no canto inferior direito, uma única figura preta, diferente das outras.",
                    enun="[[fig:1]]" + fonte("CAULOS. Disponível em: www.caulos.com. Acesso em: 24 set. 2011.") + p(T(110, 1).replace("CAULOS. Disponível em: www.caulos.com. Acesso em: 24 set. 2011. ", "")))),
21: Q_(111, "Educação Física", "Dança", "<p>A quadrilha veio dos salões franceses, foi adaptada pelo gosto popular brasileiro e ganhou marcações próprias e versões regionais, como as urbanas do Rio. É folclórica por <strong>abordar as tradições e costumes de determinados povos ou regiões distintas de uma mesma nação</strong>. Alternativa <strong>B</strong>.</p><p>Ela não tem caráter religioso (A) nem técnica de dança-espetáculo (C).</p>",
      ["quadrilha", "festas juninas"], trocas=[("Dicionário do folclore brasileiro", "<em>Dicionário do folclore brasileiro</em>")]),
22: Q_(112, "Língua Portuguesa", "Coesão textual", "<p>Depois de “ou não física”, o autor escreve “dois pontos” por extenso e, em seguida, dá exemplos de violência não física: o político que mente, a publicidade que joga baixo, as manipulações psicológicas. A frase <strong>é um recurso estilístico que promove satisfatoriamente a sequenciação de ideias, introduzindo apostos exemplificativos</strong>. Alternativa <strong>C</strong>.</p><p>A escolha não prejudica a sequência (E): ela anuncia os exemplos, como os dois-pontos fariam.</p>",
      ["pontuação", "estilo"],
      extra={"enunciado": tit("Jogar limpo") + ap(T(112, 0).replace("Jogar limpo ", "")) + fonte("<em>Língua Portuguesa</em>, São Paulo, ano 5, n. 66, abr. 2011 (adaptado).")
             + p(T(112, 1).replace("Língua Portuguesa, São Paulo, ano 5, n. 66, abr. 2011 (adaptado). ", ""))}),
23: Q_(113, "Literatura", "Gêneros literários", "<p>O texto conta uma cena simples, em versos curtos: a mulher recusa o convite para o teatro, mas depois grita “TEATRO!” diante do espelho, até quebrá-lo, numa atuação “perfeita”, sem plateia. O desfecho inesperado e a condensação do sentido <strong>surpreendem o leitor pelo seu efeito poético</strong>. Alternativa <strong>B</strong>.</p><p>Não é relato de fato real (A) nem de experiência teatral profissional (C).</p>",
      ["Adélia Prado", "poema"],
      extra=com_fig(113, "q113", "Poema “A diva”, de Adélia Prado, como aparece na prova: Maria José recusa um convite para ir ao teatro porque está cansada de trabalhar; depois, sozinha, repete a palavra “teatro” cada vez mais alto diante do espelho, até que ele se quebra, sem aplauso, e o poema termina com a palavra “Perfeita”.",
                    enun="[[fig:1]]" + fonte("PRADO, A. <em>Oráculos de maio</em>. São Paulo: Siciliano, 1999.") + p(T(113, 2).replace("o texto A diva", "o texto <em>A diva</em>")))),
24: Q_(114, "Artes", "Artes visuais", "<p>A carta é um documento histórico em que o português descreve os nativos com o seu olhar (“tão bem-dispostos, tão bem feitos e galantes”). A tela de Portinari põe em primeiro plano os indígenas, em movimento agitado, com os braços erguidos, enquanto os navios chegam. A <strong>carta mostra o olhar do colonizador sobre a gente da terra, e a pintura destaca, em primeiro plano, a inquietação dos nativos</strong>. Alternativa <strong>C</strong>.</p><p>As obras são de épocas diferentes (E): 1500 e 1956.</p>",
      ["Portinari", "Carta de Caminha"],
      extra={"enunciado": tit("TEXTO I") + ap(T(114, 1)) + fonte("CASTRO, S. <em>A carta de Pero Vaz de Caminha</em>. Porto Alegre: L&amp;PM, 1996 (fragmento).") + tit("TEXTO II") + "[[fig:1]]"
             + fonte("PORTINARI, C. <em>O descobrimento do Brasil</em>. 1956. Óleo sobre tela, 199 × 169 cm. Disponível em: www.portinari.org.br. Acesso em: 12 jun. 2013.") + p(T(114, 6)),
             "imagens": figs(("q114", "Pintura “O descobrimento do Brasil”, de Portinari: em primeiro plano, figuras indígenas nuas, alongadas, com os braços erguidos em movimentos agitados, algumas segurando paus; ao fundo, à esquerda, velas de uma caravela."))}),
25: Q_(115, "Literatura", "Teatro", "<p>O repórter repete “espremido, empilhado, esmagado de corpo e alma” várias vezes, aplicando as palavras ao Querô e aos outros meninos, e fala de seus “desesperos” e “ódios”. A repetição intensifica a ideia de <strong>opressão física e moral, que gera rancor nos meninos</strong>. Alternativa <strong>A</strong>.</p><p>O texto fala em ódio e desespero, e não em apatia (B).</p>",
      ["Plínio Marcos", "repetição"],
      extra={"enunciado": tit("Querô") + ap(*[x.strip() for x in re.split(r"\s(?=DELEGADO —|SARARÁ —|REPÓRTER —|\(Luz)", T(115, 0).replace("Querô ", "", 1))]).replace("(Luz apaga no delegado e acende no repórter, que se dirige ao público.)", "<em>(Luz apaga no delegado e acende no repórter, que se dirige ao público.)</em>")
             + fonte("MARCOS, P. <em>Melhor teatro</em>. São Paulo: Global, 2003 (fragmento).") + p(T(115, 2))}),
26: Q_(116, "Literatura", "Parnasianismo", "<p>O soneto diz que, se a dor de cada um aparecesse no rosto, muita gente que hoje causa inveja causaria pena, e que muitos que riem guardam um sofrimento escondido, cuja única felicidade é “parecer aos outros venturosa”. As pessoas escondem o que sentem para parecer felizes: <strong>a necessidade de ser socialmente aceito leva o indivíduo a agir de forma dissimulada</strong>. Alternativa <strong>A</strong>.</p>",
      ["Raimundo Correia", "soneto"],
      extra={"enunciado": tit("Mal secreto") + SON("Se a cólera que espuma, a dor que mora / N’alma, e destrói cada ilusão que nasce, / Tudo o que punge, tudo o que devora / O coração, no rosto se estampasse;",
                                                 "Se se pudesse, o espírito que chora, / Ver através da máscara da face, / Quanta gente, talvez, que inveja agora / Nos causa, então piedade nos causasse!",
                                                 "Quanta gente que ri, talvez, consigo / Guarda um atroz, recôndito inimigo, / Como invisível chaga cancerosa!",
                                                 "Quanta gente que ri, talvez existe, / Cuja ventura única consiste / Em parecer aos outros venturosa!")
             + fonte("CORREIA, R. In: PATRIOTA, M. <em>Para compreender Raimundo Correia</em>. Brasília: Alhambra, 1995.") + p(T(116, 5))}),
27: Q_(117, "Artes", "Música", "<p>Nos anos 1970, depois do tropicalismo, a indústria cultural passou a lançar uma música jovem, voltada ao mercado de massa e influenciada pelo rock internacional, adaptado à realidade brasileira. Entre os trechos, quem representa essa nova era é <strong>Rita Lee, com “Ovelha negra”</strong>, de 1975. Alternativa <strong>D</strong>.</p><p>As outras canções são anteriores: marchinha de carnaval, samba-canção e bossa nova.</p>",
      ["rock brasileiro", "indústria cultural"], trocas=[("Pequena história da música popular: da modinha ao tropicalismo", "<em>Pequena história da música popular: da modinha ao tropicalismo</em>")],
      extra={"imagens": figs(("q117a", "Alternativa A: trecho da letra de “As pastorinhas”, de Noel Rosa e João de Barro."), ("q117b", "Alternativa B: trecho da letra de “A noite do meu bem”, de Dolores Duran."),
                             ("q117c", "Alternativa C: trecho da letra de “No rancho fundo”, de Ary Barroso e Lamartine Babo."), ("q117d", "Alternativa D: trecho da letra de “Ovelha negra”, de Rita Lee."),
                             ("q117e", "Alternativa E: trecho da letra de “Chega de saudade”, de Tom Jobim e Vinicius de Moraes."))},
      alts=ALT(1)),
28: Q_(118, "Língua Portuguesa", "Variação linguística", "<p>“Pra valer” é uma forma coloquial: a redução “pra” (de “para”) e a expressão “pra valer”, no sentido de “de verdade”, são típicas da fala. A marca está em <strong>“Pelé estava se aposentando pra valer pela primeira vez [...]”</strong>. Alternativa <strong>D</strong>.</p><p>“Titubear” (B) é uma palavra até formal.</p>",
      ["linguagem informal", "reportagem"],
      extra={"enunciado": tit("Futebol: “A rebeldia é que muda o mundo”") + ap("<em>" + T(118, 1) + "</em>", T(118, 2), T(118, 3), T(118, 4), T(118, 5)) + fonte(T(118, 6)) + p(T(118, 7))}),
29: Q_(119, "Língua Portuguesa", "Coesão textual", "<p>O personagem começa com um ditado contra a preguiça (“A preguiça é a mãe de todos os vícios”), mas continua com “mas uma mãe é uma mãe e é preciso respeitá-la”, e conclui que vai continuar sem fazer nada. O humor vem do <strong>emprego de uma oração adversativa, que orienta a quebra da expectativa ao final</strong>. Alternativa <strong>A</strong>.</p><p>O “mas” é adversativo, e não aditivo (B e E).</p>",
      ["conjunção adversativa", "humor"],
      extra=com_fig(119, "q119", "Quadrinho com um personagem da turma da Mafalda sentado relaxado numa cadeira, com os pés para cima, pensando: “A preguiça é a mãe de todos os vícios, mas uma mãe é uma mãe e é preciso respeitá-la, pronto!”")),
30: Q_(120, "Língua Portuguesa", "Gêneros textuais", "<p>A charge mostra uma avenida tomada de carros parados, com o título “Não há movimento” e o balão “Certo estava Parmênides… ‘Não há movimento!!!’”. A frase do filósofo, que negava o movimento, vira piada sobre o trânsito urbano. O texto <strong>ironiza a dificuldade de locomoção no trânsito urbano, devida ao grande fluxo de veículos</strong>. Alternativa <strong>B</strong>.</p><p>A charge mostra uma cidade, e não estradas com caminhões (A).</p>",
      ["charge", "intertextualidade"],
      extra=com_fig(120, "q120", "Charge com o título “Não há movimento”: uma avenida engarrafada, com filas de carros e ônibus parados entre os prédios. Um balão diz: “Certo estava Parmênides… ‘Não há movimento!!!’”")),
31: Q_(121, "Língua Portuguesa", "Coesão textual", "<p>Na elipse do sujeito, o sujeito fica oculto porque pode ser recuperado do contexto. Em “Supõe-se que fizesse referência ao modo violento como o vírus se apossa do organismo”, o sujeito de “fizesse” (o verbo francês <em>gripper</em>, mencionado antes) não aparece. Alternativa <strong>E</strong>.</p><p>Em C e D, “o primeiro” e “o segundo” retomam os termos por substituição, e não por elipse.</p>",
      ["elipse", "coesão"], trocas=[("o italiano influenza", "o italiano <em>influenza</em>"), ("o francês grippe", "o francês <em>grippe</em>"), ("latim medieval influentia", "latim medieval <em>influentia</em>"), ("verbo gripper", "verbo <em>gripper</em>"), ("Sobre palavras.Veja", "Sobre palavras. <em>Veja</em>")]),
32: Q_(122, "Literatura", "Realismo", "<p>Normalmente o relógio lembra a Brás Cubas o tempo perdido e a morte. Na noite do beijo, porém, ele ouve “os minutos ganhados”: o relógio, materialização do tempo, deixa de ser motivo de angústia e passa a marcar o prazer de um caso com uma mulher casada. A metáfora mostra que <strong>o relógio representa a materialização do tempo e redireciona o comportamento idealista de Brás Cubas</strong>. Alternativa <strong>D</strong>.</p>",
      ["Machado de Assis", "metáfora"],
      extra={"enunciado": tit("Capítulo LIV — A pêndula") + ap(T(122, 1).replace("estireime", "estirei-me"), "— Outra de menos...<br>— Outra de menos...<br>— Outra de menos...<br>— Outra de menos...", T(122, 6).replace("davalhe", "dava-lhe"), T(122, 7).replace("tumultuavamme", "tumultuavam-me"))
             + fonte("ASSIS, M. <em>Memórias póstumas de Brás Cubas</em>. Rio de Janeiro: Nova Aguilar, 1992 (fragmento).") + p(T(122, 9))}),
33: Q_(123, "Língua Portuguesa", "Gêneros textuais", "<p>O título fala do “comércio da distração”. Isso se explica pela crítica de Carr de que as empresas lucram com a fragmentação da atenção: “quanto mais rápido passamos de uma informação para a outra, mais dinheiro as empresas de internet fazem”. A internet <strong>garante a empresas a obtenção de mais lucro com a recente fragilidade de nossa atenção</strong>. Alternativa <strong>E</strong>.</p><p>O raciocínio raso (B) é outra crítica do autor, mas não é ela que explica a palavra “comércio”.</p>",
      ["notícia", "título"],
      extra={"enunciado": tit("Para Carr, internet atua no comércio da distração") + ap("<em>Autor de “A Geração Superficial” analisa a influência da tecnologia na mente</em>", T(123, 1).replace("Autor de “A Geração Superficial” analisa a influência da tecnologia na mente ", ""), T(123, 2), T(123, 3), T(123, 4))
             + fonte("ROXO, E. <em>Folha de S. Paulo</em>, 18 fev. 2012 (adaptado).") + p(T(123, 6))}),
34: Q_(124, "Literatura", "Literatura contemporânea", "<p>O narrador de <em>A hora da estrela</em> não começa pela história: reflete sobre a origem de tudo, sobre o pensar e o sentir e sobre como começar a narrativa. Ele <strong>revela-se um sujeito que reflete sobre questões existenciais e sobre a construção do discurso</strong>. Alternativa <strong>C</strong>.</p><p>Ele está envolvido com a história, e não indiferente (A).</p>",
      ["Clarice Lispector", "narrador"], trocas=[("A hora da estrela. Rio", "<em>A hora da estrela</em>. Rio"), ("com a obra A hora da estrela", "com a obra <em>A hora da estrela</em>"), ("pré- pré-história", "pré-pré-história")]),
35: Q_(125, "Língua Portuguesa", "Gêneros textuais", "<p>O texto I diz que a vitamina D pode vir do sol e de alguns alimentos, como manteiga, gema de ovo e fígado. O texto II rebate: ela praticamente não está nas nossas dietas, e a natureza planejou que a produzíssemos na pele. Ele se contrapõe ao I quando <strong>enfatiza que a vitamina D é mais comumente produzida pelo corpo que absorvida por meio de alimentos</strong>. Alternativa <strong>C</strong>.</p><p>O texto II só levanta a pergunta “seria a vitamina D realmente uma vitamina?”, sem comprová-la (A).</p>",
      ["divulgação científica", "contraposição"]),
36: Q_(126, "Língua Portuguesa", "Tecnologias da comunicação", "<p>A autora diz que a informática é nova, mas que suas bases estão nos modelos anteriores, e que “a impressão é a matriz que deflagrou todo esse processo comunicacional eletrônico”. A escrita contribui por <strong>fornecer base essencial para o progresso das tecnologias de comunicação e informação</strong>. Alternativa <strong>E</strong>.</p>",
      ["escrita", "tecnologia"]),
37: Q_(127, "Artes", "Arte contemporânea", "<p>Paulo Nazareth, mineiro, viajou até Miami e expôs uma Kombi cheia de bananas, com uma placa em espanhol, numa feira de arte dos Estados Unidos. A obra mistura o estereótipo do Brasil, a viagem, a língua estrangeira e o mercado de arte: <strong>articula questões de identidade, território e códigos de linguagens</strong>. Alternativa <strong>C</strong>.</p><p>Ele não usa técnicas e suportes tradicionais (B): é uma <em>performance</em>.</p>",
      ["performance", "arte contemporânea"],
      extra=com_fig(127, "q127", "Foto da obra de Paulo Nazareth: o artista, de cabelo crespo volumoso, em pé ao lado de uma Kombi cheia de cachos de bananas, segura uma placa escrita à mão em espanhol, “No me olvide cuando yo sea un nombre importante”, traduzida na prova.",
                    enun="[[fig:1]]" + fonte("(Tradução da placa: “Não me esqueçam quando eu for um nome importante.”) NAZARETH, P. <em>Mercado de Artes / Mercado de Bananas</em>. Miami Art Basel, EUA, 2011. Disponível em: www.40forever.com.br. Acesso em: 31 jul. 2012.") + p(T(127, 2).replace("na performance", "na <em>performance</em>")))),
38: Q_(128, "Língua Portuguesa", "Funções da linguagem", "<p>O quadrinho define o que é um livro: papel costurado ou colado, letras que formam palavras e sentenças, histórias e sonhos, e, sobretudo, algo que só existe quando é lido. É a função metalinguística, que se caracteriza por <strong>fazer um exercício de reflexão a respeito dos princípios que estruturam a forma e o conteúdo de um livro</strong>. Alternativa <strong>D</strong>.</p>",
      ["metalinguagem", "quadrinhos"],
      extra=com_fig(128, "q128", "Quadrinho “Quadrinho quadrado”, de Caulos, em quatro quadros com definições: “Definições intangíveis”, com um livro aberto; “Um livro é feito de letras que formam palavras dispostas em sentenças”; “Um livro é feito de papel costurado ou colado em páginas”; “Um livro é feito de histórias e sonhos (d)escritos”; “Será um livro uma sentença?”; “Olhos!”; e por fim “Mas um livro só é um livro quando é feito sobretudo de...”, com uma pessoa lendo.",
                    enun=tit("Quadrinho quadrado") + "[[fig:1]]" + fonte("XAVIER, C. Disponível em: www.releituras.com. Acesso em: 24 abr. 2010.") + p(T(128, 3)))),
39: Q_(129, "Literatura", "Modernismo", "<p>Em volta dos versos de Oswald aparecem anotações à mão, como “País do futebol”, “Números como versos”, “Cette = ?” e “Vitórias do Clube Paulistano”. Elas orientam o leitor a entender as referências históricas e culturais do poema. São <strong>direcionamentos possíveis para uma leitura crítica de dados histórico-culturais</strong>. Alternativa <strong>A</strong>.</p>",
      ["Oswald de Andrade", "intertextualidade"],
      extra=com_fig(129, "q129", "Página da exposição “brasilidade em construção”: o poema de Oswald de Andrade sobre os placares de futebol (“a europa curvou-se ante o Brasil / 7 a 2 / 3 a 1 / A injustiça de Cette / 4 a 0 / 2 a 1 / 2 a 0 / 3 a 1 / E meia dúzia na cabeça dos portugueses”), cercado de anotações à mão: “País do futebol”, “Números como versos”, “Cette = ?? Não! Clube francês!”, “Meia dúzia = 6” e “Vitórias do Clube Paulistano”.",
                    enun="[[fig:1]]" + fonte("MUSEU DA LÍNGUA PORTUGUESA. <em>Oswald de Andrade: o culpado de tudo</em>. 27 set. 2011 a 29 jan. 2012. São Paulo: Prol Gráfica, 2012.") + p(T(129, 2)))),
40: Q_(130, "Língua Portuguesa", "Argumentação", "<p>“Na verdade” indica que o autor vai corrigir uma ideia comum: a de que “índios” são um grupo único e atrasado. Ele mostra que são mais de trezentos povos com 180 línguas e que suas ideias são modernas. O objetivo é <strong>apresentar informações pouco divulgadas a respeito dos indígenas no Brasil, para defender o caráter desses povos como civilizações, em contraposição a visões preconcebidas</strong>. Alternativa <strong>E</strong>.</p>",
      ["operador argumentativo", "povos indígenas"], trocas=[("As razões de ser guarani-kaiowá", "<em>As razões de ser guarani-kaiowá</em>")]),
41: Q_(131, "Língua Portuguesa", "Gêneros textuais", "<p>A tirinha diz “No mundo conectado não há preconceitos”, “não há ignorância”, “e não há covardia”, mas as imagens desmentem cada frase: um homem baixo e moreno se descreve no computador como “alto, loiro e sincero”, um menino diz “Ler pra quê? Tem tudo na Wikipédia!” ao lado de outro que lê <em>Os sertões</em>, e uma moça leva o fora por mensagem de celular: “eu não te amo mais”. A atitude é <strong>crítica, expressa pelas ironias</strong>. Alternativa <strong>A</strong>.</p>",
      ["ironia", "internet"],
      extra=com_fig(131, "q131", "Tirinha de três quadros. Legendas: “No mundo conectado não há preconceitos”, com um homem no computador dizendo “Sou alto, loiro e sincero”; “Não há ignorância”, com um menino dizendo “Ler pra quê? Tem tudo na Wikipédia!” ao lado de outro, confuso, que lê “Os sertões”; e “E não há covardia”, com uma moça chorando diante do celular, que mostra a nova mensagem “Eu não te amo mais”.")),
42: Q_(132, "Língua Portuguesa", "Variação linguística", "<p>O segundo compadre pergunta como se diz a palavra, “lagarto ou largato?”, mas o primeiro responde sobre o animal: “o bicho passou muito rápido”. Ele entende a pergunta como se fosse sobre a espécie. O humor vem de ele <strong>desconsiderar o conteúdo linguístico da pergunta</strong>. Alternativa <strong>C</strong>.</p>",
      ["piada", "pronúncia"],
      extra={"enunciado": tit("Dúvida") + ap(T(132, 0).replace("Dúvida ", ""), "— Passou um largato ali!<br>O outro perguntou:<br>— Lagarto ou largato?<br>O primeiro respondeu:<br>— Num sei não, o bicho passou muito rápido.") + fonte("<em>Piadas coloridas</em>. Rio de Janeiro: Gênero, 2006.") + p(T(132, 3))}),
43: Q_(133, "Língua Portuguesa", "Linguagem visual", "<p>Na capa, uma cabeça cheia de engrenagens tem uma venda sobre os olhos, ao lado do texto que diz que sites de busca manipulam resultados e há sites invisíveis. A venda simboliza o que não nos deixam ver: <strong>faz uma denúncia quanto às informações que são omitidas dos usuários da rede, sendo empregada no sentido conotativo</strong>. Alternativa <strong>B</strong>.</p>",
      ["linguagem conotativa", "capa de revista"],
      extra={"enunciado": tit("O que a internet esconde de você") + ap(T(133, 1).replace("Sites de busca", "<em>Sites</em> de busca").replace("cada site", "cada <em>site</em>")) + "[[fig:1]]"
             + fonte("GRAVATÁ, A. <em>Superinteressante</em>, São Paulo, ed. 297, nov. 2011 (adaptado).") + p(T(133, 4)),
             "imagens": figs(("q133", "Ilustração de uma cabeça humana com o alto cheio de engrenagens, peças e fios, e uma faixa preta cobrindo os olhos, como uma venda; embaixo, uma boca metálica e um botão “Help”."))}),
44: Q_(134, "Língua Portuguesa", "Gêneros digitais", "<p>O texto diz que, no <em>cyberbullying</em>, as pessoas não estão cara a cara e que “o anonimato pode aumentar a crueldade dos comentários e das ameaças”. A prática é potencializada por <strong>dificultar a identificação do agressor incógnito</strong>. Alternativa <strong>B</strong>.</p><p>O alcance maior (A) pode até existir, mas o texto destaca o anonimato.</p>",
      ["cyberbullying", "anonimato"],
      extra={"enunciado": tit("O que é <em>bullying</em> virtual ou <em>cyberbullying</em>?") + ap(T(134, 1).replace("e-mails, sites, blogs", "<em>e-mails</em>, <em>sites</em>, <em>blogs</em>"), T(134, 2)) + fonte(T(134, 3)) + p(T(134, 4).replace("do bullying", "do <em>bullying</em>"))}),
45: Q_(135, "Língua Portuguesa", "Gêneros textuais", "<p>Os gráficos mostram que os casamentos entre pessoas acima de 60 anos cresceram 44%, contra 28% na população em geral, e que a parcela dessa faixa no mercado de trabalho subiu de 31% para 38%. Eles <strong>sintetizam o crescente número de casamentos e de ocupação no mercado de trabalho</strong>. Alternativa <strong>E</strong>.</p><p>As taxas não cresceram na mesma proporção (D): 44% e de 31% para 38%.</p>",
      ["infográfico", "dados estatísticos"],
      extra={"enunciado": "[[fig:1]]" + fonte("<em>Veja</em>, São Paulo, 21 abr. 2010 (adaptado).") + p(T(135, 10)),
             "imagens": figs(("q135", "Infográfico “Casados e independentes”: um novo levantamento do IBGE mostra que os casamentos entre pessoas na faixa dos 60 anos crescem, desde 2003, a um ritmo 60% maior que o da população em geral. Gráfico de setores do aumento no número de casamentos entre 2003 e 2008: 44% entre pessoas acima dos 60 e 28% na população brasileira. Um fator determinante é que mais pessoas nessa idade estão no mercado de trabalho. Gráfico da população com mais de 60 anos no mercado de trabalho: 31% em 2003 e 38% hoje (dado de 2008). Fontes: IBGE e OIT."))}),
}


def montar(lingua):
    Q = dict(ING if lingua == "ingles" else ESP)
    Q.update(COMUM)
    return Q
