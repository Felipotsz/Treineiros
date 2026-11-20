# Enem 2011, 2º dia, caderno azul: Linguagens (questões 91 a 135; no site, 1 a 45). Em 2011 Linguagens e Matemática eram no 2º dia.
# Duas provas: enem-2011-linguagens-ingles (91–95 = inglês) e enem-2011-linguagens-espanhol (91–95 = espanhol); 96–135 iguais.
# Letras e poemas modernos como imagem (alt descreve, não transcreve): Q94 (Bob Marley), Q99 (João Cabral), Q113 (Manuel Bandeira), Q116 (Gilka Machado),
# Q118 (Antônio Cícero; a prova imprimiu por engano a referência de Gilka Machado) e Q120 (Geraldo Vandré).
# Em texto, domínio público: Q101 e Q104 (Noel Rosa, m. 1937). Prosa fica em texto. Q122–123 e Q133–134 compartilham texto/imagem.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent / "tools"))
from enem_aj import carregar_enem, enunciado_enem, paragrafos_enem

D = carregar_enem("enem-2011-dia2-azul")
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


PP = lambda n: [x for t, x in P(n) if t == "p"]
CONAR = (tit("Texto para as questões 122 e 123") + "[[fig:1]]"
         + ap("Nós adoraríamos dizer que somos perfeitos. Que somos infalíveis. Que não cometemos nem mesmo o menor deslize. E só não falamos isso por um pequeno detalhe: seria uma mentira. Aliás, em vez de usar a palavra “mentira”, como acabamos de fazer, poderíamos optar por um eufemismo. “Meia-verdade”, por exemplo, seria um termo muito menos agressivo. Mas nós não usamos esta palavra simplesmente porque não acreditamos que exista uma “Meia-verdade”. Para o Conar, Conselho Nacional de Autorregulamentação Publicitária, existem a verdade e a mentira. Existem a honestidade e a desonestidade. Absolutamente nada no meio. O Conar nasceu há 29 anos (viu só? não arredondamos para 30) com a missão de zelar pela ética na publicidade. Não fazemos isso porque somos bonzinhos (gostaríamos de dizer isso, mas, mais uma vez, seria mentira). Fazemos isso porque é a única forma da propaganda ter o máximo de credibilidade. E, cá entre nós, para que serviria a propaganda se o consumidor não acreditasse nela?",
              "Qualquer pessoa que se sinta enganada por uma peça publicitária pode fazer uma reclamação ao Conar. Ele analisa cuidadosamente todas as denúncias e, quando é o caso, aplica a punição.")
         + fonte("Anúncio veiculado na <em>Revista Veja</em>. São Paulo: Abril. Ed. 2120, ano 42, nº 27, 8 jul. 2009."))
CONAR_FIG = figs(("q122", "Topo do anúncio: o título “O Conar existe para coibir os exageros na propaganda.” seguido da frase “E ele é 100% eficiente nesta missão.”, riscada com um traço; ao lado, o logotipo do Conar, com a legenda “Propaganda boa é propaganda responsável”."))
EVOL = figs(("q133", "Charge da evolução humana: da esquerda para a direita, um macaco, hominídeos cada vez mais eretos, um homem com lança, outro com ferramenta, e por fim um homem de novo curvado, sentado diante de um computador."))
EVOL_F = fonte("Disponível em: http://www.wordinfo.info. Acesso em: 27 abr. 2010.")


ING = {
1: Q_(91, "Inglês", "Interpretação de texto", "<p>O texto diz que quem sai da escola antes dos 16 anos tem cinco vezes mais chance de sofrer um ataque cardíaco e morrer do que os “university graduates”, os formados na universidade. A expressão serve para mostrar que <strong>maior nível de estudo reduz riscos de ataques do coração</strong>. Alternativa <strong>E</strong>.</p><p>Os 10 000 pacientes (A) são os participantes do estudo, e não o número de pessoas atacadas pela doença.</p>",
      ["notícia", "vocabulário"],
      extra={"enunciado": ap(T(91, 0)) + fonte("World Report News. Magazine <em>Speak Up</em>. Ano XIV, nº 170. Editora Camelot, 2001.") + p("Em relação às pesquisas, a utilização da expressão <em>university graduates</em> evidencia a intenção de informar que")}),
2: Q_(92, "Inglês", "Interpretação de texto", "<p>No quadro “Reports due today!”, a aluna diz: “My report is about how important it is to save paper, electricity, and other resources. I’ll send it to you telepathically.” Ela não fez o relatório e usa o próprio tema como desculpa. Ela tenta <strong>convencer de que fez o relatório solicitado</strong>. Alternativa <strong>E</strong>.</p><p>O trabalho não foi entregue (A): ela promete mandá-lo por telepatia.</p>",
      ["charge", "humor"],
      extra={"imagens": figs(("q92", "Charge de Glasbergen: no quadro da sala está escrito “Reports due today!”. Uma aluna diz à professora: “My report is about how important it is to save paper, electricity, and other resources. I’ll send it to you telepathically.”"))}),
3: Q_(93, "Inglês", "Interpretação de texto", "<p>O site do Mappiness diz: “We’re particularly interested in how people’s happiness is affected by their local environment ― air pollution, noise, green spaces”. O aplicativo registra humor e situação. O projeto trata da <strong>relação entre o nível de felicidade das pessoas e o ambiente no qual se encontram</strong>. Alternativa <strong>D</strong>.</p><p>A guerra (A) aparece só como exemplo da diferença entre felicidade e bem-estar.</p>",
      ["felicidade", "divulgação científica"],
      extra={"enunciado": tit("How’s your mood?") + "[[fig:1]]" + ap(T(93, 2), T(93, 3), T(93, 4)) + fonte(T(93, 5)) + p(T(93, 6)),
             "imagens": figs(("q93", "Foto de um muro com a palavra “Happiness” grafitada em letras grandes."))}),
4: Q_(94, "Inglês", "Interpretação de texto", "<p>A letra repete que haverá guerra (“Everywhere is war”) enquanto uma raça for considerada superior, enquanto houver cidadãos de primeira e segunda classe e enquanto a cor da pele importar mais que a cor dos olhos. Marley alerta para <strong>a persistência da guerra enquanto houver diferenças raciais e sociais</strong>. Alternativa <strong>B</strong>.</p><p>A letra fala de luta, e não de inércia da África (A).</p>",
      ["canção", "racismo"],
      extra=img(94, "q94", "Letra de “War”, de Bob Marley, em inglês: repete que haverá guerra em toda parte enquanto a filosofia de uma raça superior e outra inferior não for abandonada, enquanto houver cidadãos de primeira e segunda classe e enquanto a cor da pele importar mais que a cor dos olhos; cita os regimes que oprimem irmãos em Angola, Moçambique e África do Sul e afirma que os africanos lutarão e vencerão.",
                "[[fig:1]]" + p(T(94, 4).replace("música War", "música <em>War</em>")))),
5: Q_(95, "Inglês", "Interpretação de texto", "<p>Jon pergunta se Garfield se lembra da ex-namorada Jodell; Garfield responde “You know... the psycho?”, e Jon diz “You’ll have to be more specific”: são várias as ex-namoradas malucas. O humor vem de que <strong>Garfield conhece as ex-namoradas de Jon e considera mais de uma como maluca</strong>. Alternativa <strong>D</strong>.</p>",
      ["tirinha", "humor"],
      extra={"imagens": figs(("q95", "Tirinha do Garfield em três quadros. Jon pergunta: “Remember my old girlfriend Jodell?”. Garfield pensa: “You know... the psycho?”. Jon responde: “You’ll have to be more specific.”"))}),
}

ESP = {
1: Q_("91-es", "Espanhol", "Interpretação de texto", "<p>“Desmachupizar” é tirar Machu Picchu do centro do turismo peruano. O texto diz que a cidadela concentra 70% da receita turística e que a Unesco alerta que o monumento está perto do “punto de saturación”. O vocábulo se refere ao <strong>excesso de turistas na terra dos incas</strong>. Alternativa <strong>D</strong>.</p><p>O problema não é a falta de turistas (A), mas a concentração deles em Machu Picchu.</p>",
      ["turismo", "neologismo"]),
2: Q_("92-es", "Espanhol", "Interpretação de texto", "<p>O título da palestra é “Muerto por el código: transparencia de software en los dispositivos médicos implantables”, e o texto fala do “riesgo potencialmente mortal” das falhas. O autor quer <strong>alertar sobre os riscos mortais de determinados softwares de uso médico para o ser humano</strong>. Alternativa <strong>B</strong>.</p><p>Não se trata de falhas médicas (C), e sim de falhas de programação.</p>",
      ["notícia", "tecnologia"]),
3: Q_("93-es", "Espanhol", "Interpretação de texto", "<p>O texto diz que o Comitê reúne mais de 180 delegações “para deliberar sobre las nuevas candidaturas y el estado de conservación y de riesgo de los bienes ya declarados Patrimonio Mundial”. Entre as tarefas está a <strong>discussão sobre o estado de conservação dos bens já declarados patrimônios mundiais</strong>. Alternativa <strong>D</strong>.</p><p>As análises citadas são do Icomos e de outros órgãos, e não do Ministério da Cultura (C).</p>",
      ["patrimônio cultural", "Unesco"]),
4: Q_("94-es", "Espanhol", "Interpretação de texto", "<p>O tango nasceu nos bairros pobres, chegou aos cabarés da classe média, foi aclamado em Paris nos anos 1920 e hoje revive em versões de rock e filmes estrangeiros. É reconhecido por <strong>sobreviver e se difundir, ultrapassando as fronteiras do país</strong>. Alternativa <strong>C</strong>.</p><p>O texto mostra que o tango mudou (A) e sofreu influência de Londres e Paris (E).</p>",
      ["tango", "cultura argentina"]),
5: Q_("95-es", "Espanhol", "Interpretação de texto", "<p>O texto mostra o volume de lixo no México, diz que consumir racionalmente ajuda o ambiente e que reciclar economiza energia, água e matérias-primas. A frase final, “É preciso saber para começar a agir”, mostra a intenção de <strong>informar o leitor a respeito da importância da reciclagem para a conservação do meio ambiente</strong>. Alternativa <strong>A</strong>.</p>",
      ["reciclagem", "meio ambiente"], trocas=[("m3", "m<sup>3</sup>")]),
}

COMUM = {
6: Q_(96, "Educação Física", "Corpo e sociedade", "<p>O texto diz que o corpo passou a ser “modelado pelos exercícios físicos da moda”, com mais academias e salas de musculação. A busca é por padrões estéticos: aumentou a procura por <strong>dietas que preconizam a ingestão excessiva ou restrita de macronutrientes, bem como exercícios que permitem aumentar a massa muscular e modelar o corpo</strong>. Alternativa <strong>E</strong>.</p><p>As outras alternativas falam de saúde e bem-estar, sem relação com o culto ao corpo descrito no texto.</p>",
      ["culto ao corpo", "estética"], trocas=[("Caderno do professor: educação física", "<em>Caderno do professor: educação física</em>")]),
7: Q_(97, "Língua Portuguesa", "Gêneros digitais", "<p>No infográfico, a amizade assimétrica “não é recíproca”: posso seguir alguém sem pedir permissão, como no Twitter. O ponto positivo é tornar “muito mais fácil a formação de laços e comunidades”. Ela <strong>facilita a interação entre pessoas em virtude de interesses comuns</strong>. Alternativa <strong>D</strong>.</p><p>O infográfico diz que ela dificulta a amizade íntima (C).</p>",
      ["infográfico", "redes sociais"],
      extra={"imagens": figs(("q97", "Infográfico “Amizade pós-moderna: a internet e as redes sociais se baseiam em dois tipos de relação”. Amizade simétrica: é recíproca, a pessoa precisa autorizar o pedido; a favor, a privacidade; contra, reduz a possibilidade de conhecer gente nova; exemplos: Facebook, Orkut, Flickr, LinkedIn, MSN, Last.fm. Amizade assimétrica: não é recíproca, posso adicionar ou seguir alguém sem pedir permissão; a favor, torna muito mais fácil a formação de laços e comunidades; contra, é mais difícil virar amizade íntima, pois a interação é pública; exemplos: Twitter, Buzz, Tumblr, Blip.fm."))}),
8: Q_(98, "Língua Portuguesa", "Gêneros digitais", "<p>Marcuschi define o hipertexto como escrita “não sequencial e não linear”, em que o leitor define “interativamente o fluxo de sua leitura” e se torna “coautor do texto final”. O hipertexto <strong>possibilita ao leitor escolher seu próprio percurso de leitura, sem seguir sequência predeterminada, constituindo-se em atividade mais coletiva e colaborativa</strong>. Alternativa <strong>E</strong>.</p><p>O texto não diz que a informação da internet é sempre segura (D).</p>",
      ["hipertexto", "leitura"]),
9: Q_(99, "Literatura", "Poesia", "<p>Severino tenta se identificar, mas cada traço (o nome, a mãe Maria, o pai Zacarias) é compartilhado por muitos outros. O texto II diz que “quanto mais se define, menos se individualiza”. A resposta vem pela <strong>representação, na figura do personagem-narrador, de outros Severinos que compartilham sua condição</strong>. Alternativa <strong>C</strong>.</p><p>Os traços não são minuciosos (A): são justamente genéricos.</p>",
      ["João Cabral", "Morte e Vida Severina"],
      extra=img(99, "q99", "Texto I, trecho de “Morte e vida severina”, de João Cabral de Melo Neto, em versos curtos: o retirante diz que seu nome é Severino, mas, como há muitos Severinos, passaram a chamá-lo Severino de Maria e depois da Maria do finado Zacarias, o que ainda não basta, pois há muitos na freguesia; termina perguntando como dizer quem fala a Vossas Senhorias.",
                "[[fig:1]]" + ap("<strong>Texto II</strong>", T(99, 4)) + fonte(T(99, 5).replace("João Cabral: a poesia do menos", "<em>João Cabral: a poesia do menos</em>"))
                + p(T(99, 6).replace("Morte e Vida Severina", "<em>Morte e Vida Severina</em>")))),
10: Q_(100, "Língua Portuguesa", "Intertextualidade", "<p>O anúncio mostra pés de um cadáver com a etiqueta “Noites do Terror” e a frase “Quem é morto sempre aparece”. Ela retoma o dito popular “Quem é vivo sempre aparece”, trocando “vivo” por “morto”. O entendimento requer <strong>o reconhecimento do intertexto entre a publicidade e um dito popular</strong>. Alternativa <strong>D</strong>.</p>",
      ["publicidade", "dito popular"],
      extra={"imagens": figs(("q100", "Anúncio em preto e branco: as solas de dois pés, como de um cadáver, com uma etiqueta presa ao dedo escrita “Noites do Terror”; embaixo, a frase “Quem é morto sempre aparece.”"))}),
11: Q_(101, "Literatura", "Música popular", "<p>A canção pergunta, com ironia, como alguém tem palacete, joias e criados “sem ter nenhuma herança ou parente”, e diz que o dinheiro “nasce de repente” e que ele “acha nas ruas” anéis e dinheiro. A atualidade está <strong>na ironia, ao se referir ao enriquecimento de origem duvidosa de alguns</strong>. Alternativa <strong>A</strong>.</p><p>A crítica não é a quem é rico (B), mas a quem enriquece de forma suspeita.</p>",
      ["Noel Rosa", "ironia"],
      extra={"enunciado": ap("<strong>Texto I</strong>") + tit("Onde está a honestidade?")
             + SON("Você tem palacete reluzente / Tem joias e criados à vontade / Sem ter nenhuma herança ou parente / Só anda de automóvel na cidade...", "E o povo pergunta com maldade: / Onde está a honestidade? / Onde está a honestidade?",
                   "O seu dinheiro nasce de repente / E embora não se saiba se é verdade / Você acha nas ruas diariamente / Anéis, dinheiro e felicidade...", "Vassoura dos salões da sociedade / Que varre o que encontrar em sua frente / Promove festivais de caridade / Em nome de qualquer defunto ausente...")
             + fonte(T(101, 4)) + ap("<strong>Texto II</strong>", T(101, 5).replace("Texto II ", "")) + fonte(T(101, 6)) + p(T(101, 7).replace("canção Onde está a honestidade?", "canção <em>Onde está a honestidade?</em>"))}),
12: Q_(102, "Literatura", "Regionalismo", "<p>Riobaldo, fazendeiro, fala do meeiro Zé-Zim, que não cria nada porque gosta de mudar, e lembra que ele próprio, menino pobre, dependeu da proteção dos Guedes. O agregado é livre para ir embora, mas depende do dono da terra. O narrador <strong>mostra como a condição material da vida do sertanejo é dificultada pela sua dupla condição de homem livre e, ao mesmo tempo, dependente</strong>. Alternativa <strong>D</strong>.</p>",
      ["Guimarães Rosa", "Grande Sertão: Veredas"], trocas=[("Grande Sertão: Veredas", "<em>Grande Sertão: Veredas</em>")]),
13: Q_(103, "Língua Portuguesa", "Gêneros textuais", "<p>Braulio Tavares diz que os folhetos talvez desapareçam, mas os poemas “continuarão sendo publicados e lidos” em CD-ROM, livro eletrônico ou outros meios, pois o texto é “uma espécie de alma imortal, capaz de reencarnar em corpos variados”. Ele defende que <strong>os textos continuarão vivos e passíveis de reprodução em novas tecnologias, mesmo que os livros desapareçam</strong>. Alternativa <strong>D</strong>.</p>",
      ["cordel", "suportes"]),
14: Q_(104, "Literatura", "Música popular", "<p>O samba diz que a gíria do morro foi aceita pela cidade, que “o samba não tem tradução no idioma francês” e que o que o malandro diz “é brasileiro, já passou de português”. Noel critica o “I love you” e o “alô boy”. Ele propõe <strong>valorizar a fala popular brasileira como patrimônio linguístico e forma legítima de identidade nacional</strong>. Alternativa <strong>C</strong>.</p><p>Ele rejeita os estrangeirismos (A), e não defende o português padrão (B).</p>",
      ["Noel Rosa", "metalinguagem"],
      extra={"enunciado": tit("Não tem tradução")
             + SON("[...]", "Lá no morro, se eu fizer uma falseta / A Risoleta desiste logo do francês e do inglês / A gíria que o nosso morro criou / Bem cedo a cidade aceitou e usou", "[...]",
                   "Essa gente hoje em dia que tem mania de exibição / Não entende que o samba não tem tradução no idioma francês / Tudo aquilo que o malandro pronuncia / Com voz macia é brasileiro, já passou de português / Amor lá no morro é amor pra chuchu / As rimas do samba não são <em>I love you</em> / E esse negócio de alô, alô <em>boy</em> e alô <em>Johnny</em> / Só pode ser conversa de telefone")
             + fonte("ROSA, N. In: SOBRAL, João J. V. A tradução dos bambas. <em>Revista Língua Portuguesa</em>. Ano 4, nº 54. São Paulo: Segmento, abr. 2010 (fragmento).")
             + p(T(104, 2).replace("políticoculturais", "político-culturais").replace("samba Não tem tradução", "samba <em>Não tem tradução</em>"))}),
15: Q_(105, "Educação Física", "Dança", "<p>O texto diz que as danças folclóricas estão ligadas a aspectos religiosos, festas, lendas, fatos históricos e ao cotidiano. Como expressão de um povo, a dança revela <strong>manifestações afetivas, históricas, ideológicas, intelectuais e espirituais de um povo, refletindo seu modo de expressar-se no mundo</strong>. Alternativa <strong>A</strong>.</p><p>O texto inclui os fatos históricos (B) e não fala em ranking (D).</p>",
      ["folclore", "cultura corporal"], trocas=[("Proposta Curricular do Estado de São Paulo: Educação Física", "<em>Proposta Curricular do Estado de São Paulo: Educação Física</em>")]),
16: Q_(106, "Língua Portuguesa", "Coesão", "<p>“Além disso” acrescenta mais um benefício da vida saudável aos que já foram citados, dando continuidade à enumeração: <strong>marca uma sequenciação de ideias</strong>. Alternativa <strong>A</strong>.</p><p>“Mas também” soma, e não contrasta (B); “como” introduz exemplos, e não generalização (C); “fatores” retoma a redução do estresse e o aumento da capacidade física (E).</p>",
      ["conectivos", "coesão"], trocas=[("Nossa vida", "<em>Nossa vida</em>"), ("Época", "<em>Época</em>")]),
17: Q_(107, "Artes", "Arquitetura", "<p>As colunas do Palácio da Alvorada têm linhas curvas amplas e opostas, que se encontram na base e no alto, sem ornamentos. A legenda diz que “foram elas que o mundo inteiro copiou”. Observa-se <strong>o traçado simples de amplas linhas curvas opostas, resultando em formas marcantes</strong>. Alternativa <strong>B</strong>.</p><p>Não há rebuscamento nem excesso de ornamentação (D e E).</p>",
      ["Niemeyer", "arquitetura moderna"],
      extra={"enunciado": "[[fig:1]]" + fonte("<em>Brasília 50 anos</em>. <em>Veja</em>. Nº 2 138, nov. 2009.") + p("Utilizadas desde a Antiguidade, as colunas, elementos verticais de sustentação, foram sofrendo modificações e incorporando novos materiais com ampliação de possibilidades. Ainda que as clássicas colunas gregas sejam retomadas, notáveis inovações são percebidas, por exemplo, nas obras de Oscar Niemeyer, arquiteto brasileiro nascido no Rio de Janeiro em 1907.", T(107, 2)),
             "imagens": figs(("q107", "Desenho de Niemeyer das colunas do Palácio da Alvorada: linhas curvas que se abrem e se fecham, tocando o chão em ponta, com uma pessoa pequena ao lado para escala. Legenda: “Imodesto: ‘As colunas do Alvorada podiam ser mais fáceis de construir, sem aquelas curvas. Mas foram elas que o mundo inteiro copiou’”."))}),
18: Q_(108, "Educação Física", "Lutas", "<p>O texto diz que as lutas tinham objetivo guerreiro ou um apelo filosófico, como concepção de vida. Os enfrentamentos de torcidas e gangues usam os gestos sem esse sentido. O objetivo foi mal compreendido porque as lutas <strong>apresentam a possibilidade de desenvolver o autocontrole, o respeito ao outro e a formação do caráter</strong>. Alternativa <strong>B</strong>.</p><p>As lutas não têm como objetivo golpes agressivos (C).</p>",
      ["artes marciais", "violência"], trocas=[("Educação Física na escola: Implicações para a prática pedagógica", "<em>Educação Física na escola: Implicações para a prática pedagógica</em>")]),
19: Q_(109, "Língua Portuguesa", "Argumentação", "<p>O autor lembra Cícero, que via encantos e dificuldades em todas as idades, aponta o paradoxo de querermos viver muito e depois sofrermos com a velhice, e conclui que ler Cícero “pode ajudar a aceitar melhor a passagem do tempo”. O objetivo é <strong>mostrar às pessoas que é possível aceitar, sem angústia, o envelhecimento</strong>. Alternativa <strong>E</strong>.</p>",
      ["envelhecimento", "Cícero"], trocas=[("A Arte do Envelhecimento", "<em>A Arte do Envelhecimento</em>"), ("Época", "<em>Época</em>")]),
20: Q_(110, "Artes", "Arte contemporânea", "<p>Nelson Leirner encaixa uma cadeira de verdade num tronco de árvore: o objeto do cotidiano é deslocado e ganha um sentido “mágico”, “inquietante e absurdo”, como diz o texto. A obra apresenta características <strong>abstracionistas e de releitura do objeto</strong>. Alternativa <strong>D</strong>.</p><p>A cadeira perde sua função (A): não pode ser usada como móvel.</p>",
      ["Nelson Leirner", "ressignificação do objeto"],
      extra={"imagens": figs(("q110", "Foto da obra “Tronco com cadeira”, de Nelson Leirner: uma cadeira de madeira encaixada dentro de um tronco de árvore cortado, apoiado no chão."))},
      trocas=[("O simbolismo nas artes plásticas", "<em>O simbolismo nas artes plásticas</em>"), ("O homem e os seus símbolos", "<em>O homem e os seus símbolos</em>")]),
21: Q_(111, "Língua Portuguesa", "Gêneros textuais", "<p>O texto conta uma história curta, com personagens e diálogo, e termina com uma resposta engraçada (“inté que é uma feiura caprichada”), feita para provocar riso. É uma <strong>anedota, pelo enredo e humor característicos</strong>. Alternativa <strong>A</strong>.</p><p>Não é relato de fatos verídicos (D) nem reportagem (E).</p>",
      ["anedota", "variação linguística"], trocas=[("Almanaque Brasil de Cultura Popular", "<em>Almanaque Brasil de Cultura Popular</em>")]),
22: Q_(112, "Artes", "Pintura rupestre", "<p>A pintura rupestre da Toca do Salitre e o grafite urbano usam paredes para registrar figuras, ideias e crenças de quem os fez, em épocas muito distantes. O elemento comum é <strong>o registro do pensamento e das crenças das sociedades em várias épocas</strong>. Alternativa <strong>C</strong>.</p><p>Nenhuma das duas é restrita às elites (D e E).</p>",
      ["grafite", "arte rupestre"],
      extra={"enunciado": ap("<strong>TEXTO I</strong>") + "[[fig:1]]" + ap("<strong>TEXTO II</strong>") + "[[fig:2]]" + p(T(112, 6)),
             "imagens": figs(("q112a", "Foto de pinturas rupestres na Toca do Salitre, no Piauí: figuras humanas e traços pintados numa parede de rocha. Fonte: www.fumdham.org.br."),
                             ("q112b", "Foto de um grafite urbano: figuras humanas grandes e contorcidas pintadas numa parede. Arte urbana, foto de Diego Singh. Fonte: www.diaadia.pr.gov.br."))}),
23: Q_(113, "Literatura", "Modernismo", "<p>O eu lírico diz que na roça cada criatura é única e observa enterros, carrocinhas e o murmúrio da água, que sugere “que a vida passa! que a vida passa! / E que a mocidade vai acabar”. A calma do campo faz perceber o tempo: é <strong>a percepção do caráter efêmero da vida, possibilitada pela observação da aparente inércia da vida rural</strong>. Alternativa <strong>B</strong>.</p><p>Ele prefere a estrada à cidade (A).</p>",
      ["Manuel Bandeira", "campo e cidade"],
      extra=img(113, "q113", "Poema “Estrada”, de Manuel Bandeira, em versos livres: o eu lírico diz que a estrada onde mora interessa mais que uma avenida urbana, pois na cidade todos se parecem e ali cada criatura é única, até os cães; descreve gente que vai e vem, um enterro a pé, uma carrocinha de leite puxada por um bode, e o murmúrio da água que sugere que a vida passa e que a mocidade vai acabar.",
                "[[fig:1]]" + p(PP(113)[-1].replace("poema Estrada", "poema <em>Estrada</em>")))),
24: Q_(114, "Artes", "Cubismo", "<p><em>Guernica</em> é um painel em preto, branco e cinza, com figuras fragmentadas e planas (o cavalo, o touro, a mãe com o filho morto), que mostram várias dimensões do bombardeio ao mesmo tempo, sem perspectiva realista. É um <strong>painel ideográfico, monocromático, que enfoca várias dimensões de um evento, renunciando à realidade</strong>. Alternativa <strong>A</strong>.</p><p>A obra não é fotográfica (B e E) nem sem emoção (C e D): é um protesto carregado de dor.</p>",
      ["Picasso", "Guernica"],
      extra={"enunciado": "[[fig:1]]" + p(T(114, 2).replace("obra Guernica", "obra <em>Guernica</em>")),
             "imagens": figs(("q114", "Pintura “Guernica”, de Picasso, em preto, branco e cinza: figuras fragmentadas e distorcidas, entre elas um cavalo agonizante, um touro, uma mulher com uma criança morta nos braços, um guerreiro caído e uma lâmpada no alto."))},
      alts={**D[114]["alternativas"], "E": "uso de vários ícones que representam personagens fragmentados bidimensionalmente, de forma fotográfica livre de sentimentalismo."}),
25: Q_(115, "Língua Portuguesa", "Argumentação", "<p>O autor afirma que, no Brasil, ler e escrever não basta para a cidadania, que depende “da ruptura com o ciclo da pobreza, que penaliza um largo contingente populacional”. Ele <strong>faz uma avaliação crítica a respeito da condição cidadã do brasileiro</strong>. Alternativa <strong>D</strong>.</p><p>Ele não critica os processos de alfabetização (A): diz que eles são necessários, mas insuficientes.</p>",
      ["cidadania", "leitura"]),
26: Q_(116, "Literatura", "Modernismo", "<p>Gilka Machado brinca com o duplo sentido de “língua”: o idioma e o órgão do beijo (“ó língua-lama, ó língua-resplendor”, “carne de som”). Ela trata do desejo feminino, tema ousado para a época, e cria palavras compostas. A poeta <strong>explora a construção da essência feminina, a partir da polissemia de “língua”, e inova o léxico</strong>. Alternativa <strong>E</strong>.</p>",
      ["Gilka Machado", "erotismo"],
      extra=img(116, "q116", "Fragmento do poema “Lépida e leve”, de Gilka Machado: o eu lírico feminino se dirige à “língua do meu Amor”, que a envolve, a veste e a prende como uma aranha, e declara amá-la como todas as mulheres a amam, chamando-a de língua-lama e língua-resplendor, pela carne de som que empresta às ideias e pelas frases mudas dos silêncios de amor.",
                "[[fig:1]]" + p(T(116, 6)))),
27: Q_(117, "Literatura", "Naturalismo", "<p>O fado português deixa todos tristes, “até mesmo os brasileiros”, mas, quando começa o chorado baiano, “o sangue de toda aquela gente” desperta, e a música vira “gemidos e suspiros”, “carícia de fera”. O texto <strong>mostra o poder envolvente da música brasileira, que cala o fado português</strong>. Alternativa <strong>C</strong>.</p><p>Não há omissão de nomes portugueses (A) nem descrição de cenário (B).</p>",
      ["Aluísio Azevedo", "O Cortiço"], trocas=[("O Cortiço. São Paulo", "<em>O Cortiço</em>. São Paulo"), ("romance O Cortiço", "romance <em>O Cortiço</em>")]),
28: Q_(118, "Literatura", "Poesia", "<p>O poema diz que guardar não é trancar em cofre, mas olhar, admirar, velar, e que por isso se escreve e se publica um poema: para guardar o que se quer guardar. A literatura guarda experiências e sentimentos. O texto <strong>reforça a capacidade da literatura em promover a subjetividade e os valores humanos</strong>. Alternativa <strong>C</strong>.</p><p>O poema não diz que a poesia é superior a outras formas de memória (E).</p>",
      ["Antônio Cícero", "memória"],
      extra=img(118, "q118", "Poema “Guardar”, de Antônio Cícero: o eu lírico diz que guardar uma coisa não é escondê-la ou trancá-la num cofre, mas olhá-la, admirá-la, velar por ela; que melhor se guarda o voo de um pássaro do que o pássaro sem voo; e que por isso se escreve, se publica e se declama um poema, para guardar o que se quer guardar.",
                "[[fig:1]]" + fonte("Referência como impressa na prova: MACHADO, G. In: MORICONI, I. (org.). <em>Os cem melhores poemas brasileiros do século</em>. Rio de Janeiro: Objetiva, 2001. O poema “Guardar” é de Antônio Cícero.") + p(T(118, 4)))),
29: Q_(119, "Língua Portuguesa", "Variação linguística", "<p>O texto mostra que, no período colonial, português e tupi “viveram lado a lado como línguas de comunicação”, e Vieira conta que em São Paulo se falava a língua dos índios em casa e os meninos aprendiam português na escola. O patrimônio linguístico vem da <strong>interação pacífica no uso da língua portuguesa e da língua tupi</strong>. Alternativa <strong>E</strong>.</p>",
      ["tupi", "formação do português brasileiro"], trocas=[("História da língua portuguesa", "<em>História da língua portuguesa</em>")],
      alts={**D[119]["alternativas"], "E": "interação pacífica no uso da língua portuguesa e da língua tupi."}),
30: Q_(120, "Língua Portuguesa", "Funções da linguagem", "<p>A canção fala da dor do eu lírico, que não vai mentir nem esconder o que sente e diz que vai “voltar pra mim / Seguir sozinho assim”. Na função emotiva, o emissor <strong>imprime à canção as marcas de sua atitude pessoal, seus sentimentos</strong>. Alternativa <strong>A</strong>.</p><p>Persuadir o receptor (C) é a função conativa, e explicar a linguagem (D), a metalinguística.</p>",
      ["Geraldo Vandré", "função emotiva"],
      extra=img(120, "q120", "Letra de “Pequeno concerto que virou canção”, de Geraldo Vandré: o eu lírico diz que não há por que mentir ou esconder a dor maior do que seu coração suporta, que quem nunca soube amar não entende de amor, e que vai voltar para si e seguir sozinho até sentir de novo o coração capaz de amar.",
                "[[fig:1]]" + p(T(120, 3)))),
31: Q_(121, "Língua Portuguesa", "Funções da linguagem", "<p>A notícia apresenta dados da pesquisa: o volume estimado de 86 000 km³, a localização sob Amazonas, Pará e Amapá e a citação do geólogo. Na função referencial, o autor prioriza <strong>os aspectos objetivos e precisos</strong>. Alternativa <strong>B</strong>.</p><p>Opiniões e persuasão (A e C) caracterizam outras funções.</p>",
      ["função referencial", "notícia"],
      extra={"enunciado": tit("É água que não acaba mais") + ap(T(121, 1)) + fonte("<em>Época</em>. Nº 623, 26 abr. 2010.") + p(T(121, 3))},
      alts={**D[121]["alternativas"], "E": "os aspectos subjetivos da mencionada pesquisa."}),
32: Q_(122, "Língua Portuguesa", "Gêneros textuais", "<p>O anúncio risca a frase “E ele é 100% eficiente nesta missão”, como se a corrigisse por ser exagerada, e depois explica que não usa nem “meia-verdade”. Ao fazer uma propaganda que se corrige para não exagerar, o Conar fala da própria publicidade: <strong>subverte o fazer publicitário pelo uso de sua metalinguagem</strong>. Alternativa <strong>D</strong>.</p>",
      ["metalinguagem", "publicidade"], extra={"enunciado": CONAR + p("O recurso gráfico utilizado no anúncio publicitário ― de destacar a potencial supressão de trecho do texto ― reforça a eficácia pretendida, revelada na estratégia de"), "imagens": CONAR_FIG},
      alts={"A": "ressaltar a informação no título, em detrimento do restante do conteúdo associado.", "B": "incluir o leitor por meio do uso da 1ª pessoa do plural no discurso.", "C": "contar a história da criação do órgão como argumento de autoridade.",
            "D": "subverter o fazer publicitário pelo uso de sua metalinguagem.", "E": "impressionar o leitor pelo jogo de palavras no texto."}),
33: Q_(123, "Língua Portuguesa", "Gêneros textuais", "<p>O anúncio, publicado numa revista de grande circulação, explica o que é o Conar, sua missão e diz que “qualquer pessoa que se sinta enganada por uma peça publicitária pode fazer uma reclamação”. O objetivo é <strong>informar os consumidores em geral sobre a atuação do Conar</strong>. Alternativa <strong>A</strong>.</p><p>O texto se dirige ao público leitor, e não a publicitários ou empresários (B, D e E).</p>",
      ["publicidade", "Conar"], extra={"enunciado": CONAR + p("Considerando a autoria e a seleção lexical desse texto, bem como os argumentos nele mobilizados, constata-se que o objetivo do autor do texto é"), "imagens": CONAR_FIG},
      alts={"A": "informar os consumidores em geral sobre a atuação do Conar.", "B": "conscientizar publicitários do compromisso ético ao elaborar suas peças publicitárias.", "C": "alertar chefes de família, para que eles fiscalizem o conteúdo das propagandas veiculadas pela mídia.",
            "D": "chamar a atenção de empresários e anunciantes em geral para suas responsabilidades ao contratarem publicitários sem ética.", "E": "chamar a atenção de empresas para os efeitos nocivos que elas podem causar à sociedade, se compactuarem com propagandas enganosas."}),
34: Q_(124, "Língua Portuguesa", "Argumentação", "<p>O título “Se no inverno é difícil acordar, imagine dormir” brinca com o desconforto do leitor ao acordar no frio e o compara ao de quem não tem onde dormir. O problema do leitor parece pequeno diante do dos necessitados: é <strong>o jogo de palavras entre “acordar” e “dormir”, o que relativiza o problema do leitor em relação ao dos necessitados</strong>. Alternativa <strong>E</strong>.</p>",
      ["publicidade", "campanha do agasalho"],
      extra={"imagens": figs(("q124", "Anúncio com o título “Se no inverno é difícil acordar, imagine dormir.” e o texto: “Com a chegada do inverno, muitas pessoas perdem o sono. São milhões de necessitados que lutam contra a fome e o frio. Para vencer esta batalha, eles precisam de você. Deposite qualquer quantia. Você ajuda milhares de pessoas a terem uma boa noite e dorme com a consciência tranquila.”"))},
      trocas=[("Veja.", "<em>Veja</em>.")]),
35: Q_(125, "Língua Portuguesa", "Variação linguística", "<p>O texto diz que o Museu da Língua apresenta o idioma como “algo vivo e fundamental para o entendimento do que é ser brasileiro” e que a forma como falamos é “talvez a melhor expressão da brasilidade”. Ressalta a <strong>importância da língua para a construção da identidade nacional</strong>. Alternativa <strong>B</strong>.</p>",
      ["Museu da Língua Portuguesa", "identidade"], trocas=[("Revista Língua Portuguesa", "<em>Revista Língua Portuguesa</em>")]),
36: Q_(126, "Língua Portuguesa", "Gêneros textuais", "<p>O texto I diz que “sobram desculpas esfarrapadas e falta competência da classe política”. O texto II critica governo e prefeitura por só mandarem as pessoas saírem das áreas de risco e propõe um serviço preventivo. Os dois apontam para a <strong>incapacidade política para agir de forma diligente na resolução das mazelas sociais</strong>. Alternativa <strong>C</strong>.</p><p>Só o texto II propõe um órgão como o SUS (D).</p>",
      ["carta do leitor", "desastres naturais"], trocas=[("Istoé", "<em>Istoé</em>"), ("Carta Capital", "<em>Carta Capital</em>")]),
37: Q_(127, "Língua Portuguesa", "Linguagem visual", "<p>A imagem mostra um saco de açúcar com a forma de uma barriga, e o mote é “Mude sua embalagem”. O corpo é comparado a uma embalagem de açúcar: quem consome açúcar fica com essa forma. O anúncio quer <strong>associar o vocábulo “açúcar” à imagem do corpo fora de forma, sugerindo a substituição desse produto pelo adoçante</strong>. Alternativa <strong>D</strong>.</p>",
      ["publicidade", "metáfora visual"],
      extra={"imagens": figs(("q127", "Anúncio de adoçante: um saco branco escrito “Açúcar”, com dobras que lembram uma barriga e um umbigo; no canto, a frase “Mude sua embalagem”."))}),
38: Q_(128, "Língua Portuguesa", "Variação linguística", "<p>O texto diz que normas prestigiadas e estigmatizadas convivem no território, mas há uma “interseção de usos que configuram uma norma nacional distinta da do português europeu”. Chama a atenção para a <strong>existência de usos da língua que caracterizam uma norma nacional do Brasil, distinta da de Portugal</strong>. Alternativa <strong>C</strong>.</p><p>O texto fala do século XVIII como início da bifurcação, e não da difusão do português (B).</p>",
      ["norma linguística", "português brasileiro"], trocas=[("Ensino de gramática: descrição e uso", "<em>Ensino de gramática: descrição e uso</em>")]),
39: Q_(129, "Língua Portuguesa", "Pronomes", "<p>Uma cobra diz “Vamos arrasar eles!”, e a outra propõe acertar o pronome antes. Pela norma-padrão, o objeto direto pede o pronome oblíquo: “arrasá-los”. “Eles” é pronome reto, próprio da função de sujeito. O uso é inadequado porque <strong>contraria a marcação das funções sintáticas de sujeito e objeto</strong>. Alternativa <strong>B</strong>.</p>",
      ["pronome oblíquo", "norma-padrão"],
      extra={"enunciado": "[[fig:1]]" + fonte("VERÍSSIMO, L. F. <em>As cobras em: Se Deus existe que eu seja atingido por um raio</em>. Porto Alegre: L&amp;PM, 1997.") + p(T(129, 2)),
             "imagens": figs(("q129", "Tirinha d’As Cobras em três quadros: uma cobra diz “Vamos massacrá-los!” e a outra responde “Vamos!”; depois diz “Vamos arrasar eles!”, e a outra repete “Vamos!”; no último quadro, a segunda diz: “Mas antes, vamos acertar o pronome.”"))}),
40: Q_(130, "Língua Portuguesa", "Variação linguística", "<p>A mesma planta, <em>Manihot utilissima</em>, recebe nomes diferentes conforme a região: aipim, castelinha, macaxeira, maniva, maniveira. O fenômeno revela que <strong>existem variedades regionais para nomear uma mesma espécie de planta</strong>. Alternativa <strong>A</strong>.</p><p>Os nomes não indicam espécies diferentes (D).</p>",
      ["variação regional", "léxico"],
      extra={"enunciado": tit("MANDIOCA – mais um presente da Amazônia") + ap(T(130, 1).replace("Manihot utilissima", "<em>Manihot utilissima</em>"), T(130, 2)) + fonte("<em>O melhor do Globo Rural</em>. Fev. 2005 (fragmento).")
             + p("De acordo com o texto, há no Brasil uma variedade de nomes para a <em>Manihot utilissima</em>, nome científico da mandioca. Esse fenômeno revela que")}),
41: Q_(131, "Língua Portuguesa", "Variação linguística", "<p>O texto diz que certos usos, como “tem muitos livros”, “para mim fazer” e “aluga-se casas”, aparecem até em quem domina a variedade padrão, porque revelam tendências de mudança da língua. Isso mostra que <strong>falantes que dominam a variedade padrão demonstram usos que confirmam a diferença entre a norma idealizada e a efetivamente praticada</strong>. Alternativa <strong>B</strong>.</p>",
      ["norma culta", "mudança linguística"], trocas=[("Ensino de gramática: descrição e uso", "<em>Ensino de gramática: descrição e uso</em>")]),
42: Q_(132, "Língua Portuguesa", "Variação linguística", "<p>Os guaranis da aldeia Sapucaí não quiseram chamar o computador de “computador” e criaram <em>aiú irú rive</em>, “caixa pra acumular a língua”, além de <em>angojhá</em> (rato) para mouse e <em>oventã</em> (janela) para windows. A reação revela <strong>a preservação da identidade, demonstrada pela conservação do idioma, mesmo com a utilização de novas tecnologias</strong>. Alternativa <strong>C</strong>.</p>",
      ["empréstimos linguísticos", "língua indígena"],
      extra={"enunciado": tit("Palavra indígena") + ap("<em>" + T(132, 1) + "</em>", T(132, 2), T(132, 3), T(132, 4), T(132, 5) + " " + T(132, 6)) + fonte(T(132, 7)) + p(T(132, 8))},
      alts={**D[132]["alternativas"], "E": "a apropriação da nova tecnologia de forma gradual, evidente quando os guaranis incorporaram a novidade tecnológica ao seu estilo de vida com a possibilidade de acesso à internet."}),
43: Q_(133, "Educação Física", "Saúde e postura", "<p>A charge da evolução termina com o homem de novo curvado, sentado diante do computador, como os primeiros hominídeos. O problema ilustrado é a postura: <strong>o uso contínuo do computador de forma inadequada tem ocasionado má postura corporal</strong>. Alternativa <strong>E</strong>.</p><p>A imagem não mostra dores de cabeça (A) nem obesidade (D), e sim a coluna curvada.</p>",
      ["postura", "computador"], extra={"enunciado": tit("Imagem para as questões 133 e 134") + "[[fig:1]]" + EVOL_F + p(T(133, 0)), "imagens": EVOL}),
44: Q_(134, "Língua Portuguesa", "Linguagem visual", "<p>A charge retoma a sequência da evolução, mas no fim o homem volta a se curvar, preso ao computador. A metáfora sugere que a tecnologia, em vez de só fazer avançar, cria uma nova dependência: <strong>o surgimento de um homem dependente de um novo modelo tecnológico</strong>. Alternativa <strong>A</strong>.</p><p>A charge não fala de exclusão digital (C).</p>",
      ["charge", "evolução"], extra={"enunciado": tit("Imagem para as questões 133 e 134") + "[[fig:1]]" + EVOL_F + p(T(134, 0)), "imagens": EVOL},
      alts={**D[134]["alternativas"]}),
45: Q_(135, "Língua Portuguesa", "Gêneros digitais", "<p>O texto diz que o limite de 140 caracteres é “oportunidade única de compreender a importância da concisão” e que tudo cabe num <em>tweet</em>, da literatura ao jornalismo. A concisão exige clareza: a rede <strong>estimula a produção de frases com clareza e objetividade, fatores que potencializam a comunicação interativa</strong>. Alternativa <strong>E</strong>.</p>",
      ["Twitter", "concisão"],
      extra={"enunciado": tit(T(135, 0)) + ap("<em>" + T(135, 1) + "</em>", T(135, 2)) + fonte(T(135, 3)) + p(T(135, 4))}),
}


def montar(lingua):
    Q = dict(ING if lingua == "ingles" else ESP)
    Q.update(COMUM)
    return Q
