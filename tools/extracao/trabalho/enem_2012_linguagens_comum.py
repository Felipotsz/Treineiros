# Enem 2012, 2º dia, caderno azul: Linguagens (questões 91 a 135; no site, 1 a 45). Em 2012 Linguagens e Matemática eram no 2º dia.
# Duas provas: enem-2012-linguagens-ingles (91–95 = inglês) e enem-2012-linguagens-espanhol (91–95 = espanhol); 96–135 iguais.
# Letras e poemas modernos como imagem (alt descreve, não transcreve): Q91 (Langston Hughes), Q100 (Drummond), Q111 (Blitz), Q112 (Cecília Meireles),
# Q113 (Manoel de Barros), Q115 (Simonal), Q117 (Sonia Queiroz), Q118 (Verissimo), Q126 (Cacaso).
# Em texto, domínio público: Q116 (Camões) e Q135 (Mário de Andrade, m. 1945). Prosa fica em texto.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent / "tools"))
from enem_aj import carregar_enem, enunciado_enem, paragrafos_enem

D = carregar_enem("enem-2012-dia2-azul")
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


def TAB(cab, linhas):
    h = "<table class=\"tabela\"><thead><tr>" + "".join(f"<th>{c}</th>" for c in cab) + "</tr></thead><tbody>"
    return h + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in l) + "</tr>" for l in linhas) + "</tbody></table>"


def img(n, arq, alt, enun):
    return {"enunciado": enun, "imagens": figs((arq, alt))}


ING = {
1: Q_(91, "Inglês", "Interpretação de texto", "<p>O eu lírico conta que o mandam comer na cozinha quando chegam visitas, uma prática racista. Mas ele ri, come bem e fica forte, e afirma que amanhã estará à mesa, ninguém ousará mandá-lo para a cozinha e os outros verão como ele é bonito e terão vergonha. O sentimento é de <strong>coragem, pela superação</strong>. Alternativa <strong>A</strong>.</p><p>A vergonha (B) é o que ele prevê para os outros, e não para si mesmo.</p>",
      ["poema", "racismo"],
      extra=img(91, "q91", "Poema “I, too”, de Langston Hughes, em inglês, em versos curtos: o eu lírico, “o irmão mais escuro”, conta que o mandam comer na cozinha quando chegam visitas, mas ele ri, come bem e se fortalece, e anuncia que um dia estará à mesa com todos, que ninguém ousará excluí-lo e que os outros sentirão vergonha; termina afirmando que ele também é a América.",
                "[[fig:1]]" + p("Langston Hughes foi um poeta negro americano que viveu no século XX e escreveu <em>I, too</em> em 1932.", T(91, 7)))),
2: Q_(92, "Inglês", "Interpretação de texto", "<p>A notícia da BBC diz que “Author J. K. Rowling has announced plans to publish her first novel for adults”, que será “very different” dos livros de Harry Potter. O objetivo é <strong>informar que a autora de Harry Potter agora pretende escrever para adultos</strong>. Alternativa <strong>D</strong>.</p><p>O livro ainda não foi publicado (B), e não é da série Harry Potter (A e E). A nova editora (C) é um detalhe, e não o foco.</p>",
      ["notícia", "literatura"],
      extra={"enunciado": ap("23 February 2012 Last update at 16:53 GMT — BBC World Service") + tit("J. K. Rowling to pen first novel for adults") + "[[fig:1]]" + ap(T(92, 2), T(92, 3), T(92, 4)) + fonte(T(92, 5)) + p(T(92, 6)),
             "imagens": figs(("q92", "Foto de J. K. Rowling sorrindo, de cabelos loiros na altura dos ombros, com crédito da agência Reuters."))}),
3: Q_(93, "Inglês", "Interpretação de texto", "<p>Cameron diz que faltou aos jovens “respect and boundaries but also love”, mas que, quando eles infringem a lei, é preciso ser “very tough”. Ele defende o “tough love”, o amor com firmeza. O foco é <strong>reforçar a ideia de que os jovens precisam de amor, mas também de firmeza</strong>. Alternativa <strong>D</strong>.</p><p>Ele não fala em excesso de amor (C): fala em falta de amor e de limites.</p>",
      ["citação", "tumultos na Inglaterra"],
      extra={"enunciado": tit("Quotes of the Day") + ap("Friday, Sep. 02, 2011", T(93, 2), T(93, 3)) + fonte(T(93, 4)) + p(T(93, 5))}),
4: Q_(94, "Inglês", "Variação linguística", "<p>No primeiro quadro, um homem diz a outro que ele não deveria estar ali se não fala “English real good”, frase com dupla negação e adjetivo no lugar de advérbio. No segundo, o outro responde corrigindo a gramática dele. Os dois avaliam a fala alheia por um único padrão: há <strong>dificuldade de reconhecer a existência de diferentes usos da linguagem</strong>. Alternativa <strong>B</strong>.</p><p>O cartum não mostra entendimento fácil entre sotaques (E), e sim o preconceito linguístico dos dois lados.</p>",
      ["cartum", "preconceito linguístico"],
      extra={"imagens": figs(("q94", "Cartum de Donar em dois quadros. No primeiro, um homem de boné e camiseta, com uma lata de bebida, aponta para outro e diz: “Ain’t no way y’all shuld be here if ya dont speak English real good!”. No segundo, o outro, de camisa e gravata, responde com o dedo erguido: “Sure! May I suggest you avoid double negatives and don’t forget to use an adverb!”."))}),
5: Q_(95, "Inglês", "Interpretação de texto", "<p>A frase de Hendrix é “When the power of love overcomes the love of power, the world will know peace”: quando o poder do amor superar o amor pelo poder, o mundo conhecerá a paz. Ele defende que <strong>o amor pelo poder deve ser menor do que o poder do amor</strong>. Alternativa <strong>B</strong>.</p><p>A paz é a consequência, e não a causa do amor (A). Ele não diz que a busca pelo poder deve deixar de existir (E), e sim que deve ser superada pelo amor.</p>",
      ["citação", "jogo de palavras"],
      extra={"enunciado": "[[fig:1]]" + p(T(95, 1).replace("status", "<em>status</em>").replace("love, power e peace", "<em>love</em>, <em>power</em> e <em>peace</em>")),
             "imagens": figs(("q95", "Mãos segurando uma folha com a frase, em letras grandes: “When the power of love overcomes the love of power, the world will know peace.” — Jimi Hendrix."))}),
}

ESP = {
1: Q_("91-es", "Espanhol", "Interpretação de texto", "<p>O morto foi enterrado num bosque de pinheiros, mas o caixão de pinho veio de Ohio; junto a uma mina de ferro, mas os pregos vieram de Pittsburg; e assim por diante, com terno de Nova York e sapatos de Boston. O texto termina: “Guatemala no facilitó nada al funeral, excepto el cadáver”. É uma crítica <strong>à dependência de produtos estrangeiros por uma nação</strong>. Alternativa <strong>A</strong>.</p><p>O texto mostra que a Guatemala tem recursos (E), mas importa tudo.</p>",
      ["crítica social", "dependência econômica"]),
2: Q_("92-es", "Espanhol", "Interpretação de texto", "<p>O texto diz que a escavação vai revelar a extensão e a forma do “patio que, según las investigaciones, sirvió hace unos 1 500 [años] como escenario de extraños rituales”. Pode-se inferir que <strong>o sítio arqueológico possui um pátio que foi palco de rituais</strong>. Alternativa <strong>D</strong>.</p><p>A pirâmide é de adobe (C) e foi construída pelos moches, e não no período colonial (A). Os escombros vieram do saque colonial e das escavações recentes (E).</p>",
      ["notícia", "arqueologia"]),
3: Q_("93-es", "Espanhol", "Interpretação de texto", "<p>Galeano diz que a América Latina “sigue trabajando de sirvienta”, que tudo nela se transformou em capital europeu ou norte-americano e que sua estrutura foi determinada “desde fuera”. A riqueza local alimenta a prosperidade de outros. As relações com as nações exploradoras <strong>sempre se caracterizaram por uma rede de dependências</strong>. Alternativa <strong>A</strong>.</p><p>Os exploradores mudaram ao longo do tempo, da Europa para os Estados Unidos (B), e o texto cita os “caporales nativos” que se beneficiaram (E).</p>",
      ["Eduardo Galeano", "dependência"]),
4: Q_("94-es", "Espanhol", "Formação de palavras", "<p>Susanita diz que uma mulher que não cozinha, não passa, não lava e não limpa “es menos mujer”. Quando Mafalda pergunta se a mulher com empregadas é pouco mulher, ela distingue “la mujerez” do “status”. Para ela, a “mujerez” está em fazer as tarefas de casa: o vocábulo remete à <strong>valorização das mulheres que realizam todas as tarefas domésticas</strong>. Alternativa <strong>B</strong>.</p><p>Quem tem empregadas tem “status” (D), e não “mujerez”.</p>",
      ["Mafalda", "neologismo"],
      extra={"imagens": figs(("q94es", "Tirinha da Mafalda, de Quino, em quatro quadros. Susanita diz que os homens acham a mulher inferior e Mafalda responde que é porque a veem em tarefas domésticas. Susanita retruca que para isso existem as mulheres: a mulher que não cozinha, não passa, não lava e não limpa é “menos” mulher. Mafalda pergunta se então uma mulher com cozinheira, lavadeira e empregada é pouco mulher. Susanita, com o dedo erguido, responde: “¡Momentito!... Una cosa es la mujerez y otra el status”."))}),
5: Q_("95-es", "Espanhol", "Argumentação", "<p>O autor diz que os britânicos invocam a resolução 1514 da ONU, sobre a autodeterminação dos povos coloniais, mas que ela se aplica a povos subjugados por potência estrangeira, “que no es el caso de Malvinas”, onde a Grã-Bretanha expulsou a população e instalou a sua. Para ele, <strong>o princípio de autodeterminação carece de aplicabilidade no caso das Ilhas Malvinas</strong>. Alternativa <strong>C</strong>.</p><p>O texto promete respeitar o modo de vida dos ilhéus, e não repatriá-los (E).</p>",
      ["artigo de opinião", "Malvinas"],
      extra={"enunciado": tit("Las Malvinas son nuestras") + ap(T("95-es", 1), T("95-es", 2), T("95-es", 3)) + fonte("MENEM, E. Disponível em: www.lanacion.com.ar. Acesso em: 18 fev. 2012 (adaptado).")
             + p("O texto apresenta uma opinião em relação à disputa entre a Argentina e o Reino Unido pela soberania sobre as Ilhas Malvinas, ocupadas pelo Reino Unido em 1833.", T("95-es", 5))}),
}

COMUM = {
6: Q_(96, "Educação Física", "Exercício e saúde", "<p>A figura diz que, com o treino, os pulmões difundem mais oxigênio ao sangue, o coração bombeia mais sangue por batimento e “bate mais lentamente em repouso”, e os músculos queimam mais gordura. São adaptações benéficas a <strong>diminuição da frequência cardíaca em repouso e o aumento da oxigenação do sangue</strong>. Alternativa <strong>A</strong>.</p><p>A frequência em repouso diminui (B e E), e a gordura corporal diminui (C e D).</p>",
      ["fisiologia do exercício", "frequência cardíaca"],
      extra={"imagens": figs(("q96", "Infográfico “Efeitos do exercício físico” com três etapas ligadas por setas. Pulmões: fornecem oxigênio ao sangue; com o treino, podem receber mais ar e difundir mais oxigênio ao sangue. Coração: bombeia sangue rico em oxigênio aos músculos; aumenta de tamanho, pode bombear mais sangue por batimento e bate mais lentamente em repouso ou durante o exercício. Músculos: utilizam o oxigênio para queimar combustível e produzir energia; adquirem tônus e podem queimar mais combustível, especialmente gordura, durante o exercício. Rodapé: a ventilação, a circulação e o metabolismo estão intimamente ligados e todos melhoram com o treinamento."))}),
7: Q_(97, "Língua Portuguesa", "Gêneros textuais", "<p>O anúncio oferece a assinatura da revista impressa e, “com mais R$ 58,10”, a versão digital para <em>tablet</em> e PC. A revista passa a ser vendida também em outro suporte: as tecnologias <strong>proporcionaram mudanças no paradigma de consumo e oferta de revistas e livros</strong>. Alternativa <strong>A</strong>.</p><p>O anúncio não desvaloriza o impresso (B), que continua sendo oferecido, nem vende equipamentos (C e D).</p>",
      ["publicidade", "tecnologia"],
      extra={"imagens": figs(("q97", "Anúncio em duas faixas: “Assine Nossa Revista e com mais R$ 58,10...” e “...leve também a versão digital para tablet e PC por 1 ano e meio.”"))}),
8: Q_(98, "Literatura", "Romantismo", "<p>O texto apresenta Alencar como autor de clássicos “com temas nativistas, indianistas e históricos”, “tido como o pai do romance no Brasil”, e diz que parte do seu acervo inédito será digitalizada para revelar suas múltiplas facetas. A digitalização <strong>terá importante papel na preservação da memória linguística e da identidade nacional</strong>. Alternativa <strong>D</strong>.</p><p>O texto não diz que a digitalização é necessária para compreender os romances (A).</p>",
      ["José de Alencar", "memória"], trocas=[("O guarani e Iracema", "<em>O guarani</em> e <em>Iracema</em>")]),
9: Q_(99, "Língua Portuguesa", "Variação linguística", "<p>O relato transcreve a fala: “passeá”, “brincá”, “andá”, reticências marcando pausas, alongamento (“a::”), risos e reformulações (“dos meus treze aos dezessete anos”). O que o caracteriza como fala é o <strong>predomínio de linguagem informal entrecortada por pausas</strong>. Alternativa <strong>A</strong>.</p><p>O vocabulário é comum, e não regional desconhecido (B), e o relato é compreensível (E).</p>",
      ["oralidade", "transcrição"]),
10: Q_(100, "Literatura", "Poesia", "<p>O menino ouve sempre “Que vai ser quando crescer?” e se pergunta se ser é ter um corpo, um jeito, um nome, se terá de mudar de nome, corpo e jeito. Ele conclui: “Não vou ser. Não quero ser”. As questões nascem <strong>no conflito do padrão corporal imposto contra as convicções de ser autêntico e singular</strong>. Alternativa <strong>A</strong>.</p><p>Ele recusa as imposições, e não as aceita (B).</p>",
      ["Drummond", "identidade"],
      extra=img(100, "q100", "Texto em prosa poética “Verbo ser”, de Carlos Drummond de Andrade: uma criança repete a pergunta que todos lhe fazem sobre o que vai ser quando crescer, questiona o que é ser, se é ter corpo, jeito e nome, se precisará mudar tudo isso para crescer, brinca com o som da palavra “ser” e termina recusando-se a ser.",
                "[[fig:1]]" + p(T(100, 3)))),
11: Q_(101, "Literatura", "Conto", "<p>O personagem “manejava bem os cordéis de seus títeres”, mas é também “títere voluntário e consciente”, entregando braço, pernas e cabeça quando lhe convém. Ele acredita dominar os jogos sociais, mas se torna um boneco. A crítica está <strong>na imagem do títere ou fantoche em que o personagem acaba por se transformar, acreditando dominar os jogos de poder na linguagem</strong>. Alternativa <strong>A</strong>.</p><p>Ele domina os jogos discursivos (B) e os usa por conveniência, e não aleatoriamente (D).</p>",
      ["Samuel Rawet", "metáfora"], trocas=[("Diálogo.", "<em>Diálogo</em>.")]),
12: Q_(102, "Língua Portuguesa", "Coesão", "<p>Em 1912, Conrad diz que ninguém mais se lembra de Crane. A anotação de 1919 começa com “Muito peixe foi embrulhado pelas folhas de jornal”: os jornais envelhecem e viram papel de embrulho, ou seja, o tempo passou. A metáfora marca a <strong>temporalidade</strong>, situando no tempo o que é relatado. Alternativa <strong>B</strong>.</p><p>Uma parte não é causa da outra (A): a frase só liga os dois momentos do diário.</p>",
      ["Rubem Fonseca", "metáfora"],
      extra={"enunciado": tit("Labaredas nas trevas") + ap("Fragmentos do diário secreto de Teodor Konrad Nalecz Korzeniowski", T(102, 1), T(102, 2).replace("The London Mercury", "<em>The London Mercury</em>")) + fonte(T(102, 3)) + p(T(102, 4))}),
13: Q_(103, "Língua Portuguesa", "Semântica", "<p>Na charge, uma família pobre se espreme numa rede de dormir, sob a placa “Rede social”, e um deles diz “Rede social aqui em casa é outra coisa!”. A expressão “rede social”, que remete à internet, ganha o sentido de rede de deitar compartilhada. A frase recorre à <strong>polissemia</strong>. Alternativa <strong>A</strong>.</p><p>Não há oposição entre advérbios de lugar (C) nem antônimos (E): o efeito vem do duplo sentido de “rede”.</p>",
      ["charge", "polissemia"],
      extra={"imagens": figs(("q103", "Charge de Ivan Cabral: uma família numerosa e pobre, adultos e crianças, espremida numa rede de dormir que quase toca o chão. Uma placa diz “Rede social”, e um dos homens diz: “Rede social aqui em casa é outra coisa!”."))}),
14: Q_(104, "Língua Portuguesa", "Gêneros digitais", "<p>Chartier lembra o sonho de Kant de que cada um fosse “ao mesmo tempo leitor e autor”, emitindo juízos e construindo “um espaço de intercâmbio crítico das ideias e opiniões”. O texto eletrônico realiza esse sonho ao <strong>propiciar o livre e imediato acesso às informações e ao intercâmbio de julgamentos</strong>. Alternativa <strong>A</strong>.</p><p>Entretenimento, publicidade e visibilidade pessoal (C, D e E) não aparecem no texto.</p>",
      ["Roger Chartier", "texto eletrônico"], trocas=[("A aventura do livro: do leitor ao navegador", "<em>A aventura do livro: do leitor ao navegador</em>")]),
15: Q_(105, "Língua Portuguesa", "Pronomes de tratamento", "<p>Numa roda em que a moça tratava todos por “você”, ela chamou o autor de “o senhor”, o que o fez se sentir velho e distante. O trecho que descreve essa violação é: <strong>“Essa palavra, ‘senhor’, no meio de uma frase ergueu entre nós um muro frio e triste”</strong>. Alternativa <strong>A</strong>.</p><p>As outras frases comentam a condição do autor ou a idade dele, mas não descrevem o efeito do tratamento.</p>",
      ["Rubem Braga", "crônica"], trocas=[("A borboleta amarela", "<em>A borboleta amarela</em>")]),
16: Q_(106, "Língua Portuguesa", "Argumentação", "<p>A bruxa e a serpente oferecem a maçã à Branca de Neve e ouvem “Não, obrigada”. No terceiro quadro, um vendedor oferece a maçã com um bônus: “Com mais 10,00 você ganha um celular”, e no último ele explica: “Questão de técnica”. Ele persuade pela <strong>indução, ao elaborar o discurso de acordo com os anseios do consumidor</strong>. Alternativa <strong>E</strong>.</p><p>Os outros também mostraram o produto (A): o diferencial é a oferta pensada para o desejo da cliente.</p>",
      ["tirinha", "persuasão"],
      extra={"imagens": figs(("q106", "Tirinha de Laerte em quatro quadros. A Branca de Neve, de costas, recusa a maçã oferecida pela bruxa: “Não, obrigada”. Depois recusa a maçã oferecida por uma serpente: “Não, obrigada”. No terceiro quadro, um vendedor de terno, sorridente, oferece a maçã e diz: “Com mais 10,00 você ganha um celular”. No último, a bruxa e a serpente olham para o vendedor, que ajeita a gravata e diz: “Questão de técnica”."))}),
17: Q_(107, "Língua Portuguesa", "Argumentação", "<p>Para sustentar que não somos tão especiais, o autor dá exemplos de animais com inteligência, amor, consciência e cultura (corvos de luto, chimpanzés que se reconhecem no espelho, cetáceos que transmitem hábitos) e os compara às características “tidas como exclusivas dos humanos”. As estratégias são <strong>exemplificação e comparação</strong>. Alternativa <strong>B</strong>.</p><p>O texto não hierarquiza (A): ao contrário, nega a supremacia humana.</p>",
      ["divulgação científica", "estratégias argumentativas"],
      extra={"enunciado": tit("Não somos tão especiais") + "[[fig:1]]" + ap("<em>Extra, extra. Este macaco é humano.</em>", T(107, 2))
             + ap(*["<strong>" + x.split(" ", 1)[0] + "</strong><br>" + x.split(" ", 1)[1] for x in (T(107, i) for i in range(3, 7))])
             + fonte("BURGIERMAN, D. <em>Superinteressante</em>, n. 190, jul. 2003.") + p(T(107, 8)),
             "imagens": figs(("q107", "Foto de um chimpanzé sentado sobre um caixote de madeira, lendo um jornal aberto com as duas mãos, como uma pessoa."))}),
18: Q_(108, "Língua Portuguesa", "Variação linguística", "<p>O texto de Drummond usa palavras que hoje quase ninguém usa, como “debicar”, “tunda”, “liró” e “convescote”, e a tabela traz o significado atual delas. Palavras caem em desuso e outras surgem: <strong>o léxico do português representa uma realidade linguística variável e diversificada</strong>. Alternativa <strong>E</strong>.</p><p>A língua de antigamente tinha termos para o cotidiano (A): são justamente esses que mudaram.</p>",
      ["Drummond", "léxico"],
      extra={"enunciado": ap("<strong>TEXTO I</strong>") + tit("Antigamente") + ap(T(108, 1)) + fonte(T(108, 2)) + ap("<strong>TEXTO II</strong>") + tit("Palavras do arco da velha")
             + TAB(["Expressão", "Significado"], [["Cair nos braços de Morfeu", "Dormir"], ["Debicar", "Zombar, ridicularizar"], ["Tunda", "Surra"], ["Mangar", "Escarnecer, caçoar"], ["Tugir", "Murmurar"],
                   ["Liró", "Bem-vestido"], ["Copo d’água", "Lanche oferecido pelos amigos"], ["Convescote", "Piquenique"], ["Bilontra", "Velhaco"], ["Treteiro de topete", "Tratante atrevido"], ["Abrir o arco", "Fugir"]])
             + fonte("FIORIN, J. L. As línguas mudam. In: <em>Revista Língua Portuguesa</em>, n. 24, out. 2007 (adaptado).") + p(T(108, 5).replace("texto Antigamente", "texto <em>Antigamente</em>"))}),
19: Q_(109, "Língua Portuguesa", "Semântica", "<p>Hagar mostra os tubarões seguindo o barco e diz: “É como se eles soubessem que algo ruim vai acontecer!”. A expressão “é como se” introduz uma hipótese, uma suposição. Ela leva o enunciado ao campo da <strong>possibilidade, pois a proximidade dos tubarões leva à suposição do perigo iminente para os homens</strong>. Alternativa <strong>D</strong>.</p><p>Não há conformidade (A): o tempo não aparece como indício, e sim os tubarões.</p>",
      ["tirinha", "conectivos"],
      extra={"imagens": figs(("q109", "Tirinha de Hagar, de Dik Browne: o barco viking navega perto de um rochedo, com vários tubarões nadando atrás. Um tripulante diz: “Veja quantos tubarões estão seguindo a gente!”, e Hagar responde: “É como se eles soubessem que algo ruim vai acontecer!”."))}),
20: Q_(110, "Literatura", "Prosa poética", "<p>Manoel de Barros conta que a avó disse que ele “voltou de ateu”, como quem se fantasia, e que todos riram porque a preposição deslocada fez “de uma informação um chiste”. O narrador gosta dessas falas e diz que elas têm “perfume de poesia”. O autor destaca <strong>a valorização da dimensão lúdica e poética presente nos usos coloquiais da linguagem</strong>. Alternativa <strong>E</strong>.</p><p>Ele não trata essas falas como desvios (A): ele as celebra.</p>",
      ["Manoel de Barros", "linguagem coloquial"], trocas=[("Memórias inventadas: a infância", "<em>Memórias inventadas: a infância</em>")]),
21: Q_(111, "Língua Portuguesa", "Gêneros textuais", "<p>O Texto I diz que a linguagem do rádio propõe o diálogo com o ouvinte, com simplicidade, concisão e linguagem coloquial. A canção imita um locutor: “Eu tenho aqui em minhas mãos uma carta / Uma carta d’uma ouvinte”, conta a história e se dirige à moça. Ela apresenta <strong>estilo simples e marcado pela interlocução com o receptor, típico da comunicação radiofônica</strong>. Alternativa <strong>A</strong>.</p><p>A canção imita o rádio, em vez de se afastar dele (B e C).</p>",
      ["linguagem do rádio", "canção"],
      extra=img(111, "q111", "Texto II, letra da canção “A dois passos do paraíso”, da Blitz: um locutor da Rádio Atividade apresenta o programa de dedicatórias, lê a carta de uma ouvinte de pseudônimo romântico cujo noivo, um caminhoneiro de uma pequena cidade do Norte, fugiu no dia do casamento, e pede que ele volte para ela, que o espera.",
                ap("<strong>TEXTO I</strong>", T(111, 1)) + fonte(T(111, 2).replace("A linguagem do rádio multimídia", "<em>A linguagem do rádio multimídia</em>")) + "[[fig:1]]" + p(T(111, 6)))),
22: Q_(112, "Literatura", "Modernismo", "<p>O poema diz que todo o sentido da vida começa nas palavras, que elas são sonho, audácia, calúnia e derrota, que são “frágil, frágil, como o vidro / e mais que o aço poderosa” e que reis, impérios e povos rodam por seu impulso. A reflexão é que <strong>as relações humanas, em suas múltiplas esferas, têm seu equilíbrio vinculado ao significado das palavras</strong>. Alternativa <strong>B</strong>.</p><p>O poema afirma o poder das palavras, e não um alcance limitado (E).</p>",
      ["Cecília Meireles", "Romanceiro da Inconfidência"],
      extra=img(112, "q112", "Fragmento do “Romanceiro da Inconfidência”, de Cecília Meireles, em versos curtos: o eu lírico se dirige às palavras, admirando sua estranha potência, e diz que nelas começam o sentido da vida, o amor e o sonho, mas também a calúnia e a derrota; que são frágeis como o vidro e mais poderosas que o aço, e que reis, impérios e povos se movem por seu impulso.",
                "[[fig:1]]" + p(T(112, 4).replace("Romanceiro da Inconfidência", "<em>Romanceiro da Inconfidência</em>")))),
23: Q_(113, "Literatura", "Poesia", "<p>O poema imita o Salmo 23 (“O Senhor é meu pastor”), mas o pastor é Pote Cru, um andarilho que vaga entre restos (trapos, couros, vísceras, baratas, dálias secas) e dorme em ruínas. O eu lírico o segue porque também se interessa pelas coisas desprezadas: ele o <strong>acompanha na opção pela insignificância das coisas</strong>. Alternativa <strong>E</strong>.</p><p>Não há busca de salvação divina (B): a relação com a Bíblia é paródica.</p>",
      ["Manoel de Barros", "intertextualidade"],
      extra=img(113, "q113", "Poema de Manoel de Barros que retoma o salmo bíblico do pastor: o eu lírico diz que Pote Cru é seu pastor e o guiará, e descreve-o vagando à tarde entre restos e coisas desprezadas, como trapos, couros, vísceras de bichos, baratas e flores secas; conta que ele dormia nas ruínas de um convento, foi encontrado em osso e tinha voz de oratórios perdidos.",
                "[[fig:1]]" + p(T(113, 2)))),
24: Q_(114, "Língua Portuguesa", "Gêneros textuais", "<p>O cartaz usa a pintura de Dalí, com relógios derretidos, mas a mensagem é “O atraso na devolução de livros acarreta multa e gera transtornos para os usuários. Respeite as datas de devolução”. A obra de arte só chama a atenção: a função é <strong>educativa, orientando o comportamento de usuários de um serviço</strong>. Alternativa <strong>D</strong>.</p><p>O cartaz não pretende popularizar a arte (A) nem promover a apreciação da obra (C).</p>",
      ["cartaz", "função comunicativa"],
      extra={"imagens": figs(("q114", "Cartaz do Sistema de Bibliotecas da UFG com o título “Cumprir prazos é uma obra-prima” e o aviso “O atraso na devolução de livros acarreta multa e gera transtornos para os usuários. Respeite as datas de devolução.”, sobre a pintura “A persistência da memória”, de Salvador Dalí, com relógios moles derretendo sobre um galho e uma mesa; no lugar de alguns relógios aparecem livros."))}),
25: Q_(115, "Educação Física", "Esporte e sociedade", "<p>A canção diz que, nos noventa minutos do jogo, “Esqueço a casa e o trabalho” e repete que a vida, o dinheiro, o salário, a fome e a comida “ficam lá fora”. O futebol aparece como algo que faz esquecer os problemas. A letra é crítica por <strong>promover a reflexão sobre a alienação provocada pelo futebol</strong>. Alternativa <strong>D</strong>.</p><p>Lazer e alegria (B e C) aparecem, mas a crítica está no esquecimento de tudo o mais.</p>",
      ["futebol", "alienação"],
      extra=img(115, "q115", "Fragmento da letra de “Aqui é o país do futebol”, de Wilson Simonal: diz que o Brasil fica vazio no domingo à tarde, que nos campos e avenidas o país só é futebol, e que nos noventa minutos de emoção a pessoa esquece a casa e o trabalho; segue uma longa repetição de versos dizendo que a vida, o dinheiro, a cama, a mesa, o salário, a fome, a comida e tudo mais ficam lá fora.",
                "[[fig:1]]" + p(T(115, 5).replace("canção Aqui é o país do futebol", "canção <em>Aqui é o país do futebol</em>")))),
26: Q_(116, "Artes", "Renascimento", "<p>O soneto descreve uma mulher de “leda serenidade”, “presença moderada e graciosa”, riso doce e repouso “alegre e comedido”. A pintura de Rafael mostra uma moça de postura contida, expressão serena e roupa sóbria. Os dois <strong>apresentam um retrato ideal de mulher marcado pela sobriedade e o equilíbrio</strong>, típico do Renascimento. Alternativa <strong>C</strong>.</p><p>Não há emotividade nem conflito (E), nem excesso de enfeites (B).</p>",
      ["Camões", "Rafael"],
      extra={"enunciado": tit("LXXVIII (Camões, 1525?-1580)")
             + SON("Leda serenidade deleitosa, / Que representa em terra um paraíso; / Entre rubis e perlas doce riso; / Debaixo de ouro e neve cor-de-rosa;",
                   "Presença moderada e graciosa, / Onde ensinando estão despejo e siso / Que se pode por arte e por aviso, / Como por natureza, ser fermosa;",
                   "Fala de quem a morte e a vida pende, / Rara, suave; enfim, Senhora, vossa; / Repouso nela alegre e comedido:",
                   "Estas as armas são com que me rende / E me cativa Amor; mas não que possa / Despojar-me da glória de rendido.")
             + fonte("CAMÕES, L. <em>Obra completa</em>. Rio de Janeiro: Nova Aguilar, 2008.") + "[[fig:1]]"
             + fonte("SANZIO, R. (1483-1520) <em>A mulher com o unicórnio</em>. Roma, Galleria Borghese. Disponível em: www.arquipelagos.pt. Acesso em: 29 fev. 2012.") + p(T(116, 5)),
             "imagens": figs(("q116", "Pintura de Rafael, “A mulher com o unicórnio”: retrato de meio corpo de uma jovem loira, de expressão serena, com vestido de mangas largas e um colar com pingente, segurando no colo um pequeno unicórnio."))}),
27: Q_(117, "Literatura", "Poesia", "<p>O poema contrapõe os irmãos, que se sujam na lama, provam do fogo, se lambuzam e se jogam na cama, à irmã, “cercada de alvura e enxovais”, “fechada provendo a comida”, “servindo, contida” e “afiançada por dote e marido”. Eles vivem com liberdade, e ela, presa às funções domésticas. Ela conclui que <strong>os papéis sociais destinados aos gêneros produzem efeitos e graus de autorrealização desiguais</strong>. Alternativa <strong>E</strong>.</p>",
      ["Sonia Queiroz", "papéis de gênero"],
      extra=img(117, "q117", "Poema “Das irmãs”, de Sonia Queiroz, em quatro estrofes curtas: em cada uma, os irmãos aparecem livres, sujando-se, provocando-se, comendo à vontade e jogando-se na cama, enquanto a voz feminina se mostra cercada de alvura e enxovais, fechada cozinhando, servindo contida e, por fim, comprometida por dote e marido.",
                "[[fig:1]]" + p(T(117, 2)))),
28: Q_(118, "Literatura", "Poesia", "<p>O pedido de casamento é feito em termos práticos: “juntar / Nossas rendas e / expectativas de vida”, ter “2, 3 filhos” e “ser meio felizes”. O título chama o sedutor de “médio”. A crítica está <strong>na mensagem veiculada pelo poema, em que os valores da sociedade são ironizados, o que é acentuado pelo uso do adjetivo “médio” no título e do advérbio “meio” no verso final</strong>. Alternativa <strong>B</strong>.</p><p>“Meio felizes” não quer dizer que só um dos cônjuges seria feliz (C), e sim que os dois seriam mais ou menos felizes.</p>",
      ["Verissimo", "ironia"],
      extra=img(118, "q118", "Poema curto “O sedutor médio”, de Luis Fernando Verissimo: o eu lírico propõe à amada, em tom prático, juntar rendas e expectativas de vida, ter dois ou três filhos e ser mais ou menos felizes.",
                "[[fig:1]]" + p(T(118, 2).replace("poema O sedutor médio", "poema <em>O sedutor médio</em>")))),
29: Q_(119, "Língua Portuguesa", "Gêneros textuais", "<p>O leitor elogia a reportagem, mas pergunta se a maioria dos leitores tem “obras de arte que precisam ser fotografadas antes da separação” e sugere “conselhos mais básicos”, como a partilha dos bens e a pensão dos filhos. Ele <strong>rebate o enfoque dado ao tema pela reportagem, lançando novas ideias</strong>. Alternativa <strong>E</strong>.</p><p>As dicas que ele cita (D) servem para mostrar o que faltou na reportagem, e não são o objetivo da carta.</p>",
      ["carta do leitor", "argumentação"], trocas=[("manifestase", "manifesta-se")]),
30: Q_(120, "Língua Portuguesa", "Gêneros textuais", "<p>O texto apresenta o SendLater, uma extensão do Thunderbird que permite agendar o envio de mensagens, chama o programa de “ótimo” e explica como usá-lo. O objetivo é <strong>divulgar um produto ampliador da funcionalidade de um recurso comunicativo</strong>. Alternativa <strong>E</strong>.</p><p>A extensão não elimina entraves no envio (A) nem seleciona destinatários (C): ela só agenda o envio.</p>",
      ["texto informativo", "tecnologia"],
      extra={"enunciado": tit("E-mail com hora programada") + ap("Redação INFO, 28 de agosto de 2007.", "<strong>" + T(120, 1).replace("Thunderbird", "<em>Thunderbird</em>").replace("SendLater", "<em>SendLater</em>") + "</strong>",
             T(120, 2).replace("e-mail", "<em>e-mail</em>").replace("Thunderbird", "<em>Thunderbird</em>").replace("SendLater", "<em>SendLater</em>")) + fonte(T(120, 3))
             + p(T(120, 4).replace("SendLater", "<em>SendLater</em>").replace("E-mail com hora programada", "<em>E-mail com hora programada</em>"))}),
31: Q_(121, "Artes", "Cubismo", "<p>Em <em>Les Demoiselles d’Avignon</em>, Picasso fragmenta as figuras em planos geométricos, com rostos inspirados em máscaras africanas, e abandona a perspectiva clássica. A obra inaugura o Cubismo, caracterizado pela <strong>pintura de modelos em planos irregulares</strong>. Alternativa <strong>A</strong>.</p><p>A mulher como tema, os vários modelos e a nudez (B, C e E) já existiam na arte clássica: não são o que rompe com ela.</p>",
      ["Picasso", "Cubismo"],
      extra={"enunciado": "[[fig:1]]" + fonte("PICASSO, P. <em>Les Demoiselles d’Avignon</em>. Nova York, 1907. ARGAN, G. C. <em>Arte moderna: do Iluminismo aos movimentos contemporâneos</em>. São Paulo: Companhia das Letras, 1992.") + p(T(121, 2).replace("quadro Les Demoiselles d’Avignon", "quadro <em>Les Demoiselles d’Avignon</em>")),
             "imagens": figs(("q121", "Pintura “Les Demoiselles d’Avignon”, de Picasso: cinco figuras femininas nuas, com corpos angulosos e fragmentados em planos geométricos; duas delas têm rostos que lembram máscaras africanas."))}),
32: Q_(122, "Artes", "Tropicalismo", "<p>Os Mutantes fizeram parte da Tropicália, que misturou rock e guitarra elétrica com música brasileira, ruídos, colagens sonoras e referências eruditas. O desafio à tradição está nas <strong>sonoridades experimentais e confluência de elementos populares e eruditos</strong>. Alternativa <strong>C</strong>.</p><p>O grupo incorporou influências estrangeiras, em vez de se opor a elas (E).</p>",
      ["Os Mutantes", "contracultura"],
      extra={"imagens": figs(("q122", "Capa do LP “Os Mutantes”, de 1968: os três integrantes posam com roupas e acessórios extravagantes, um deles de capa preta, outro sentado em primeiro plano; o nome do grupo aparece em letras grandes e irregulares no canto inferior."))}),
33: Q_(123, "Língua Portuguesa", "Variação linguística", "<p>Rubem Alves admite o erro: “E confesso: ele está certo. O certo é ‘varrição’”, e diz que, num vestibular, o equívoco “poderia me valer uma reprovação”. Mas lembra que na roça de Minas o povo fala “varreção”. Ele reconhece <strong>a necessidade da norma padrão em situações formais de comunicação escrita</strong>. Alternativa <strong>B</strong>.</p><p>Ele não defende o dicionário em contextos informais (E): diz que, para o povo, “não é o dicionário que faz a língua”.</p>",
      ["Rubem Alves", "norma-padrão"],
      extra={"enunciado": ap(T(123, 0), T(123, 1) + " " + T(123, 2), T(123, 3)) + fonte("ALVES, R. <em>Mais badulaques</em>. São Paulo: Parábola, 2004 (fragmento).") + p(T(123, 5))}),
34: Q_(124, "Literatura", "Pré-Modernismo", "<p>Policarpo acreditou no tupi como língua nacional, na fertilidade da terra e na doçura do povo, e cada crença terminou em decepção: o tupi trouxe o riso e a loucura, a terra não era fértil, o povo matava prisioneiros. Ele conclui que “a pátria que quisera ter era um mito”. A <strong>construção de uma pátria a partir de elementos míticos, como a cordialidade do povo, a riqueza do solo e a pureza linguística, conduz à frustração ideológica</strong>. Alternativa <strong>C</strong>.</p>",
      ["Lima Barreto", "nacionalismo"],
      extra={"enunciado": ap(*[T(124, i) for i in range(6)]).replace("do folk-lore", "do <em>folk-lore</em>") + fonte("BARRETO, L. <em>Triste fim de Policarpo Quaresma</em>. Disponível em: www.dominiopublico.gov.br. Acesso em: 8 nov. 2011.")
             + p("O romance <em>Triste fim de Policarpo Quaresma</em>, de Lima " + T(124, 8))}),
35: Q_(125, "Língua Portuguesa", "Interpretação de texto", "<p>O autor diz que o problema “não é a penúria, mas a abundância” e que há uma desarmonia entre uma oferta incoerente e uma demanda que “exige uma escolha muito mais rápida”, pois o homem moderno, apressado e estressado, quer um condensado do que importa. A relação é desarmônica porque <strong>a oferta é incoerente com o tempo que as pessoas têm para digerir a quantidade de informação disponível</strong>. Alternativa <strong>D</strong>.</p><p>O texto não fala em abundância de liberdade de escolha (C).</p>",
      ["informação", "sociedade moderna"], trocas=[("pós- industriais", "pós-industriais"), ("tornamse", "tornam-se")]),
36: Q_(126, "Literatura", "Poesia marginal", "<p>O poema é de 1972, durante a ditadura. Morcegos de olheiras, cabras malignas, hienas infiltradas, um porco “belicoso de radar” e centuriões sentinelas “do Oiapoque ao Chuí” são figuras de vigilância e repressão em todo o país. O poeta <strong>caracteriza o momento de opressão através de alegorias de forte poder de impacto</strong>. Alternativa <strong>D</strong>.</p><p>Os animais representam os agentes da repressão, e não as vítimas (B) nem a resistência (C).</p>",
      ["Cacaso", "ditadura militar"],
      extra=img(126, "q126", "Poema “Logia e mitologia”, de Cacaso: o eu lírico diz que seu coração de 1972 já não bate alegre, pois sabe que há morcegos, cabras, hienas infiltradas e um porco com radar espalhados por toda parte, que algo sangra e ri, que a vida anoitece e que há centuriões e sentinelas do Oiapoque ao Chuí.",
                "[[fig:1]]" + p("O título do poema explora a expressividade de termos que representam o conflito do momento histórico vivido pelo poeta na década de 1970. Nesse contexto, é correto afirmar que"))),
37: Q_(127, "Língua Portuguesa", "Funções da linguagem", "<p>O cronista abre pedindo desculpas, diz que “não dá” para ser divertido e encerra com “Estou nervoso. Estou zangado.”. A crônica gira em torno do estado de espírito de quem escreve, em primeira pessoa. Na função emotiva, <strong>a atitude do enunciador se sobrepõe àquilo que está sendo dito</strong>. Alternativa <strong>B</strong>.</p><p>O foco no código é a função metalinguística (A), no interlocutor, a conativa (C), e no referente, a referencial (D).</p>",
      ["crônica", "função emotiva"], trocas=[("segundafeira", "segunda-feira")]),
38: Q_(128, "Língua Portuguesa", "Variação linguística", "<p>Bagno defende o “ter” existencial e outros usos brasileiros, mas escreve na norma-padrão porque o texto é uma entrevista publicada num informativo de editora, situação formal. Ele <strong>adapta o nível de linguagem à situação comunicativa, uma vez que o gênero entrevista requer o uso da norma padrão</strong>. Alternativa <strong>A</strong>.</p><p>Ele não restringe a norma coloquial aos não escolarizados (C) nem acredita no português europeu como modelo (D).</p>",
      ["Marcos Bagno", "adequação linguística"], trocas=[("ex- colonizadores", "ex-colonizadores")]),
39: Q_(129, "Língua Portuguesa", "Variação linguística", "<p>O texto diz que todas as línguas podem expressar qualquer conteúdo, mas que na prática isso depende do vocabulário: não se fala de física quântica em camaiurá ou latim porque “não haveria vocabulário próprio”, que pode ser criado com tempo e esforço. Ele enfatiza <strong>a existência de diferenças vocabulares entre os idiomas, especificidades relacionadas à própria cultura dos falantes de uma comunidade</strong>. Alternativa <strong>D</strong>.</p><p>O texto nega que haja línguas mais primitivas (B e C).</p>",
      ["léxico", "cultura"], trocas=[("Miniaurélio: o dicionário da língua portuguesa", "<em>Miniaurélio</em>: o dicionário da língua portuguesa")]),
40: Q_(130, "Língua Portuguesa", "Variação linguística", "<p>A autora mostra que o “ter” existencial já aparecia no século XVI e que “haver” existencial com concordância foi visto como novidade no século XVIII. Ela conclui que “nada é categórico e um purismo estreito só revela um conhecimento deficiente da língua”. Para ela, <strong>os comportamentos puristas são prejudiciais à compreensão da constituição linguística</strong>. Alternativa <strong>E</strong>.</p><p>Ela critica a avaliação hierarquizante (C) e a norma única (D).</p>",
      ["ter e haver", "purismo"], trocas=[("Cadernos de Letras da UFF", "<em>Cadernos de Letras da UFF</em>")]),
41: Q_(131, "Artes", "Barroco", "<p>Os profetas de Aleijadinho representam figuras sagradas, mas com traços, gestos e expressões próximos do povo mineiro, e não idealizados como no modelo europeu. A obra revela <strong>personalidade, modelando uma imagem sacra com feições populares</strong>. Alternativa <strong>D</strong>.</p><p>A estátua é de um profeta bíblico, e não de mineiros (A) nem de personalidades do reinado (E).</p>",
      ["Aleijadinho", "Barroco mineiro"],
      extra={"imagens": figs(("q131", "Foto de uma das estátuas dos profetas de Aleijadinho, em pedra-sabão, no adro do Santuário do Bom Jesus de Matosinhos: figura de barba, com túnica de muitas dobras e turbante, com uma das mãos erguida; ao fundo, a fachada da igreja."))}),
42: Q_(132, "Língua Portuguesa", "Intertextualidade", "<p>A frase “Lugar de mulher também é na oficina” retoma o dito machista “lugar de mulher é na cozinha”, mas troca o lugar e acrescenta “também”. A notícia mostra que as mulheres matriculadas nos cursos automotivos passaram de 5 para 79, com crescimento de 1 480%. O enunciado serve para <strong>demonstrar que a situação das mulheres mudou na sociedade contemporânea</strong>. Alternativa <strong>A</strong>.</p><p>A frase dialoga com o dito popular (C), mas a comparação é um meio: o objetivo é mostrar a mudança. O texto relata um fato, sem defender uma tese (B).</p>",
      ["notícia", "intertextualidade"]),
43: Q_(133, "Língua Portuguesa", "Linguagem visual", "<p>A peça diz “Garanta sua sacola retornável! Sem sua ajuda o mundo é insustentável” e oferece uma sacola retornável a quem fizer R$ 70,00 em compras. A imagem do globo terrestre com a sacola reforça a ideia de cuidado com o planeta. O anúncio quer que o leitor <strong>consuma produtos de modo responsável e ecológico</strong>. Alternativa <strong>E</strong>.</p><p>O anúncio estimula as compras, e não evita o consumo (B e C).</p>",
      ["publicidade", "sustentabilidade"],
      extra={"imagens": figs(("q133", "Anúncio de um supermercado: no alto, “Garanta sua sacola retornável! Sem sua ajuda o mundo é insustentável”, com a palavra “in” em destaque; ao centro, um globo terrestre segurado por mãos, ao lado de uma sacola de pano; embaixo, “Até 11/03, a cada R$ 70,00 em compras, apresente seu cupom fiscal e garanta uma sacola retornável”."))}),
44: Q_(134, "Literatura", "Conto", "<p>O personagem jura não beber álcool, mas passa a “beber” paisagens, músicas de Tom Jobim, versos de Quintana e quadros de Segall. Ele morre de “etilismo abstrato”, de uma “carraspana de pôr do sol”. A ironia vem da <strong>metaforização do sentido literal do verbo “beber”</strong>. Alternativa <strong>A</strong>.</p><p>Os nomes de artistas (E) não são aleatórios: são as coisas que ele “bebe”.</p>",
      ["Drummond", "ironia"], trocas=[("embebedavase", "embebedava-se"), ("Contos plausíveis", "<em>Contos plausíveis</em>")]),
45: Q_(135, "Literatura", "Modernismo", "<p>O eu lírico se diz “um tupi tangendo um alaúde”: o tupi representa o nativo, e o alaúde, instrumento europeu, a cultura importada. A identidade nacional é <strong>problematizada na oposição tupi (selvagem) x alaúde (civilizado), apontando a síntese nacional que seria proposta no Manifesto Antropófago</strong>. Alternativa <strong>D</strong>.</p><p>O título remete aos trovadores medievais, e não aos repentistas (B).</p>",
      ["Mário de Andrade", "identidade nacional"],
      extra={"enunciado": tit("O trovador") + SON("Sentimentos em mim do asperamente / dos homens das primeiras eras... / As primaveras do sarcasmo / intermitentemente no meu coração arlequinal... / Intermitentemente... / Outras vezes é um doente, um frio / na minha alma doente como um longo som redondo... / Cantabona! Cantabona! / Dlorom... / Sou um tupi tangendo um alaúde!")
             + fonte("ANDRADE, M. In: MANFIO, D. Z. (Org.) <em>Poesias completas de Mário de Andrade</em>. Belo Horizonte: Itatiaia, 2005.") + p(T(135, 3).replace("Em O trovador", "Em <em>O trovador</em>"))}),
}


def montar(lingua):
    Q = dict(ING if lingua == "ingles" else ESP)
    Q.update(COMUM)
    return Q
