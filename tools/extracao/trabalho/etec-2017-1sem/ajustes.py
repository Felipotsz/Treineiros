# Ajustes da conferência humana: Vestibulinho ETEC 1º semestre de 2017 (exame de 18/12/2016)
# Texto conferido com a imagem de cada página; caixas de texto via trecho().
# A letra de "O Sal da Terra" (Q45) fica como imagem (alt descreve, não transcreve).
# O rascunho embaralhou as questões 43 a 46 da página 20: enunciados e alternativas escritos aqui.
# Gabarito: oficial (1º SEM/17). Sem anuladas. Tema: um mundo melhor.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import A, carregar, enun, tabela, colunas, completar, trecho

ID = "etec-2017-1sem"
META = {
    "id": ID,
    "banca": "ETEC",
    "ano": 2017,
    "semestre": 1,
    "titulo": "Vestibulinho ETEC, 1º semestre de 2017",
    "fonte": "Centro Paula Souza",
    "dataExame": "2016-12-18",
    "duracaoMinutos": 240,
    "tema": "Um mundo melhor",
    "apresentacao": "<p>Prezado(a) candidato(a), há muitas questões importantes que permeiam as nossas vidas atualmente. Como diminuir a fome no mundo? Quais tecnologias e iniciativas nos ajudarão a superar os males que nos afligem? Como buscar a boa convivência entre pessoas e povos? Nesta prova, você encontrará temas que ajudam a (re)pensar maneiras de abordar essas e outras questões para que possamos ter, em um futuro não muito distante, um mundo melhor.</p><p>Boa prova!</p>",
    "pdf": f"assets/provas/{ID}.pdf",
}
EXTRAS = {"apresentacao": "Ilustração de silhuetas de pessoas de mãos dadas formando uma roda em volta do globo terrestre."}

R = carregar(ID)


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


def it(texto, *termos):
    for t in termos: texto = texto.replace(t, f"<em>{t}</em>")
    return texto


# ---------- textos compartilhados ----------
FOME = (chamada("Leia o texto para responder às questões de números 01 a 03.")
        + apoio(*T(2, "O conceito de segurança alimentar", "desenvolvimento sustentável.",
                   ["Segundo a Organização das Nações Unidas", "Alguns fatores contribuem", "Os principais sinais", "A subnutrição também causa",
                    "É preciso unir esforços", "Campanhas de educação alimentar"]))
        + url("http://tinyurl.com/jxajnjy", "02.09.2016"))
P1 = p("De acordo com o texto, é correto afirmar que")

CARTAZ = (chamada("Leia o cartaz para responder às questões de números 04 e 05.") + "[[fig:1]]" + url("http://tinyurl.com/hv2r4hp", "06.09.2016", "Original colorido."))
CARTAZ_IMG = {"arquivo": "q04", "alt": "Cartaz da ONU: uma pizza cortada em sete fatias, uma delas faltando. No espaço vazio está escrito “Uma a cada sete pessoas no mundo passa fome”, com “sete” e “fome” em destaque. Embaixo: “Essa realidade pode mudar. Colabore.”, com “Colabore” em destaque, o símbolo da ONU e o endereço www.onu.org.br."}
P4 = p("Esse cartaz faz alusão à questão da fome no mundo, convocando o leitor a repensar e mudar os seus hábitos de consumo.",
       "O cartaz é um gênero textual cuja função é chamada de injuntiva e apresenta características tais como")

NANO = (chamada("Leia o texto para responder às questões de números 06 e 07.")
        + apoio(*[it(x, "in vitro") for x in T(4, "No tratamento da maioria dos cânceres", "partículas ultrapequenas.",
                                                ["Para minimizar", "A nanotecnologia se tornou", "No combate ao câncer", "Nos testes in vitro", "Esse resultado foi", "Porém, por trás"])])
        .replace("(10–9 m)", "(10<sup>–9</sup> m)").replace("(10-9 m)", "(10<sup>–9</sup> m)")
        + url("http://tinyurl.com/zesrhtm", "16.09.2016"))
P6 = p("De acordo com o texto, é correto afirmar que")

PAINEL = (chamada("Leia o texto para responder às questões de números 09 e 10.")
          + apoio("Um painel fotovoltaico converte energia solar em energia elétrica de forma sustentável.",
                  "Suponha que, em uma região plana, será instalado um sistema de painéis fotovoltaicos para suprir uma comunidade com energia elétrica.",
                  "Segue a descrição de alguns itens do projeto:<br>• instalação de 5 filas paralelas entre si; cada fila contendo 10 painéis;<br>"
                  "• cada painel foi montado com 4 módulos fotovoltaicos congruentes entre si, conforme figura;<br>"
                  "• em cada módulo fotovoltaico, a superfície de captação da energia solar é de forma retangular, com dimensões de 65 cm por 150 cm;<br>"
                  "• os painéis deverão estar separados, de modo que um não faça sombra sobre o outro e, também, não sejam encobertos pela sombra de qualquer outro objeto;<br>"
                  "• os painéis são idênticos entre si e estão apoiados sobre o solo.")
          + "[[fig:1]]")
PAINEL_IMG = {"arquivo": "q09", "alt": "Dois painéis inclinados, apoiados no solo, cada um formado por 4 módulos retangulares (2 por 2), com a “superfície de captação da energia solar” indicada. Cada módulo mede 65 cm no sentido da inclinação e 150 cm na largura. O Sol está acima, à direita."}
P9 = p("No projeto descrito, a área total da superfície de captação de energia solar é, em metros quadrados,")

ILHA = (chamada("Leia o texto para responder às questões de números 11 e 12.")
        + apoio(*T(7, "Os centros urbanos possuem", "(“Um grau a menos”)", ["A cor cinza", "O adensamento", "Um estudo realizado"])).replace("(“Um grau a menos”)</p>", "(“Um grau a menos”).</p>"))
P11 = p("Para justificar a cor proposta pela ONG, o argumento físico é de que a maioria das ondas incidentes presentes na luz branca são")

CHUVA = (chamada("Leia o texto para responder às questões de números 15 e 16.")
         + p("O fenômeno da chuva ácida está relacionado ao aumento da poluição em regiões industrializadas. Os agentes poluentes são distribuídos pelos ventos, causando danos à saúde humana e ao meio ambiente.",
             "Gases gerados pelas indústrias, veículos e usinas energéticas reagem com o vapor de água existente na atmosfera, formando compostos ácidos que se acumulam em nuvens, ocorrendo, assim, a condensação, da mesma forma como são originadas as chuvas comuns.",
             "Um desses gases, o SO<sub>2</sub>, é proveniente da combustão do enxofre, impureza presente em combustíveis fósseis, como o carvão e derivados do petróleo. Ele leva à formação do ácido sulfúrico.",
             "O esquema ilustra esse processo.")
         + "[[fig:1]]" + url("http://tinyurl.com/hh8kmmh", "09.09.16", "Adaptado. Original colorido."))
CHUVA_IMG = {"arquivo": "q15", "alt": "Esquema “Chuva ácida”: uma indústria queima carvão, S(carvão) + O₂ → SO₂; na atmosfera forma-se SO₃ e a reação SO₂ + ½ O₂ + H₂O → H₂SO₄; uma nuvem despeja chuva de H₂SO₄ sobre árvores e sobre um lago."}
P15 = p("O ácido representado no esquema contém em sua molécula")

ENIGMA = (chamada("Leia a charge e responda às questões de números 18 e 19.") + "[[fig:1]]" + url("http://tinyurl.com/j2t828n", "02.09.2016", "Original colorido."))
ENIGMA_IMG = {"arquivo": "q18", "alt": "Charge “O enigma do lixo”, de Junião: uma esfinge feita de um monte de lixo (garrafas, latas, embalagens) diz: “Recicla-me ou te devoro!!”"}
P18 = p("A charge dialoga com uma parte do enigma da Esfinge de Tebas, criatura mitológica grega: “Decifra-me, ou devoro-te”.",
        "Assinale a alternativa que contenha o nome que pode ser dado ao diálogo entre a charge e o enigma.")

LIXO = (chamada("Leia o texto para responder às questões de números 20 e 21.")
        + apoio(*T(11, "A produção e o descarte de lixo", "pelo acúmulo de lixo são muitos:", ["O lixo pode ser definido", "A reciclagem é necessária"]),
                "• " + T(11, "quando o lixo é constantemente", "podendo provocar enchentes;")[0] + "<br>• "
                + T(11, "o lixo exposto ao ar", "e a peste bubônica;")[0] + "<br>• "
                + T(11, "quando o lixo se acumula", "na cadeia alimentar.")[0])
        + url("http://tinyurl.com/glauzaz", "10.09.16"))
P20 = p("De acordo com o texto, necessitamos reciclar, pois esse processo")

ADICHIE = (chamada("Leia o trecho da palestra “O perigo de uma única história”, da escritora nigeriana Chimamanda Adichie, para responder às questões de números 27 e 28.")
           + apoio(T(13, "É assim que se cria uma única história", "depende do poder.")[0], "* Igbo: sociedade da região da Nigéria.")
           + url("http://tinyurl.com/z7wcfj4", "23.09.2016"))
P27 = p("Segundo a escritora, há estruturas de poder que explicam porque as relações entre os povos são como são, definindo inclusive a forma como um fala sobre o outro.",
        "Assinale a alternativa que corresponde corretamente à ideia por ela apresentada nesse trecho.")

IRMAS = (chamada("Leia o texto para responder às questões de números 31 e 32.")
         + apoio(*T(14, "Cidades-irmãs” é o nome", "duas ou mais cidades.", ["Inicialmente, seu principal", "Esses acordos entre"])).replace("<p class=\"apoio\">Cidades-irmãs”", "<p class=\"apoio\">“Cidades-irmãs”")
         + url("http://tinyurl.com/hb9y68n", "26.08.2016")
         + p("Oficialmente, a cidade de São Paulo reconhece 42 cidades como cidades-irmãs, dentre elas citamos Milão, Osaka, Lisboa, Seul, Chicago, La Paz, Luanda, Pequim, Buenos Aires, Lima, Tel Aviv, Bucareste, Santiago do Chile, Toronto, Xangai, Barcelona, Miami, Coimbra, Damasco, Montevidéu e Havana."))
P31 = p("De acordo com o texto, podemos afirmar corretamente que")

VACINA = (chamada("Leia o texto para responder às questões de números 33 e 34.")
          + apoio(*[it(x, "Aedes aegypti") for x in T(15, "No Brasil, o Programa Nacional", "objetivando a melhoria da qualidade de vida da população.",
                                                      ["Esse programa é uma", "A vacinação estimula", "Com os avanços", "Outras vacinas para"])])
          + url("http://tinyurl.com/zg8c76o", "02.09.2016"))
P33 = p("De acordo com o texto, é correto afirmar que")

LEITE = (chamada("Leia o texto e a tabela para responder às questões de números 35 e 36.")
         + p("O aleitamento materno é a mais sábia estratégia natural de vínculo, afeto, proteção e nutrição para a criança e constitui a mais sensível, econômica e eficaz intervenção para redução da morbimortalidade infantil. Permite ainda um grandioso impacto na promoção da saúde integral da dupla mãe/bebê.",
             "Nos primeiros dias após o nascimento, o leite materno é chamado de colostro. O leite de mães de recém-nascidos prematuros é diferente do de mães de bebês a termo.",
             "A principal proteína do leite materno é a lactoalbumina e a do leite de vaca é a caseína, de difícil digestão para a espécie humana.",
             "A tabela apresenta as diferenças entre o colostro e o leite maduro, entre o leite de mães de bebês a pré-termo e de bebês a termo e entre o leite materno e o leite de vaca.")
         + tabela(["Nutriente", "Colostro (3-5 dias), a termo<sup>(1)</sup>", "Colostro (3-5 dias), a pré-termo<sup>(2)</sup>",
                   "Leite maduro (26-29 dias), a termo<sup>(1)</sup>", "Leite maduro (26-29 dias), a pré-termo<sup>(2)</sup>", "Leite de vaca"],
                  [["Calorias (kcal/dL)", "48", "58", "62", "70", "69"], ["Lipídios (g/dL)", "1,8", "3,0", "3,0", "4,1", "3,7"],
                   ["Proteína (g/dL)", "1,9", "2,1", "1,3", "1,4", "3,3"], ["Lactose (g/dL)", "5,1", "5,0", "6,5", "6,0", "4,8"]])
         + fonte("<sup>(1)</sup> Bebê a termo: gestação de 39 a 40 semanas.<br><sup>(2)</sup> Bebê a pré-termo: gestação de 37 a 38 semanas.<br>&lt;http://tinyurl.com/z2xs272&gt; Acesso em: 01.09.2016. Adaptado."))
P35 = p("De acordo com o texto e a tabela, pode-se afirmar que")

RAMPA = (chamada("Leia o texto e analise a figura para responder às questões de números 37 e 38.")
         + p("No mundo de hoje a acessibilidade é um direito e, para garanti-lo, são necessárias algumas adaptações, como as rampas em locais públicos, conforme mostra a figura.") + "[[fig:1]]")
RAMPA_IMG = {"arquivo": "q37", "alt": "Desenho de uma escada de três degraus ao lado de uma rampa longa e suave, que levam ao mesmo patamar."}
P37 = p("Suponha que a rampa desenhada na figura tenha 6 m de comprimento. Se, sobre a rampa, um cadeirante mover sua cadeira com velocidade constante de 0,2 m/s, o tempo necessário para conseguir vencer o desnível do ponto mais baixo ao mais alto é, em segundos,")

MAFALDA = (chamada("Leia a tirinha que apresenta o diálogo entre Mafalda e seu pai e responda às questões de números 39 e 40.") + "[[fig:1]]"
           + fonte("QUINO. <em>Toda a Mafalda</em>/Quino; [tradutores Andréa Stahel M. da Silva et al.]. São Paulo: Martins Fontes, 1993, pg. 110."))
MAFALDA_IMG = {"arquivo": "q39", "alt": "Tirinha da Mafalda em cinco quadrinhos. 1: o pai lê no jornal: “…que aplicou um soco no goleiro, diante da indiferença do árbitro, que não marcou a falta…” 2: ele se levanta indignado: “Como alguém pode ficar impassível diante disso?” 3: Mafalda, com o jornal no chão, lê: “É cada vez maior o número de crianças abandonadas e desnutridas.” 4: Mafalda diz ao pai: “É bom ver que você se preocupa com uma coisa tão importante, papai! Todo mundo devia ser como você!” 5: o pai fica parado, sem graça."}
P39 = p("No segundo quadrinho, o pai de Mafalda utiliza a expressão “ficar impassível”. Já Mafalda, ao apresentar seu ponto de vista, emprega uma expressão que se contrapõe à usada pelo pai.",
        "Assinale a alternativa que contém essa expressão.")

SAL = (chamada("Questões 45 e 46") + p("Leia a letra da música “O Sal da Terra”, escrita por Beto Guedes e Ronaldo Bastos.") + "[[fig:1]]")
SAL = SAL.replace('<p class="chamada">Questões 45 e 46</p>', "")
SAL_IMG = {"arquivo": "q45", "alt": "Letra da canção “O Sal da Terra”, de Beto Guedes e Ronaldo Bastos, em dez estrofes curtas. Ela convida a “arrumar” a casa comum, fala em não ferir o semelhante, em precisar de todo mundo para banir a opressão e construir uma vida nova, chama a Terra de o mais bonito dos planetas, maltratado por dinheiro, fala em juntar forças e repartir melhor o pão, recriar o paraíso para quem vem depois, e termina pedindo que o amor nasça, flua, cresça e viva. Fonte: &lt;http://tinyurl.com/jxqu5yq&gt;, acesso em 26.08.2016."}
P45 = p("A letra da música transmite a ideia de que é possível construir um mundo melhor.", "A partir de elementos do texto, é correto afirmar que, para isso, é necessário")

EMPATIA = (chamada("Leia o trecho do texto Empatia, de Martha Medeiros, e responda às questões de números 49 e 50.")
           + apoio("<strong>Empatia</strong>", *(lambda a, b: [a[0] + " " + b[0]] + b[1:])(T(22, "As pessoas se preocupam em ser simpáticas", "colocar no lugar"),
                                                                      T(22, "do outro, de compreendê-lo", "outro fez por merecer.", ["Foi força de expressão", "Narciso acha feio"])))
           + url("http://tinyurl.com/jg7o8tk", "06.09.2016")
           + apoio("* O termo narcisismo provém do mito grego de Narciso, e denota admiração exagerada pela própria imagem."))
P49 = p("De acordo com a mensagem transmitida pelo texto, assinale a alternativa que apresenta um possível sinônimo para empatia.")

Q = {
1: {"materia": "Biologia", "assunto": "Nutrição e saúde", "tags": ["subnutrição"],
    "enunciado": FOME + P1,
    "explicacao": "<p>O texto diz que a subnutrição causa apatia e desmaios porque o cérebro usa a glicose como fonte de energia, e que ela pode levar a outras doenças e “até a morte”. A <strong>falta de nutrientes prejudica o sistema nervoso</strong> e pode matar. Alternativa <strong>E</strong>.</p><p>O texto não cita luz nem transgênicos como causas (A). Os danos da subnutrição são irreversíveis e não vêm do excesso de gordura (B). A subnutrição é a falta, e não a oferta, de glicose (C). E 1,3 bilhão de toneladas é o que se perde e desperdiça, um terço da produção (D).</p>"},
2: {"materia": "Geografia", "assunto": "População", "tags": ["fome"],
    "enunciado": p("De acordo com o texto, um dos fatores responsáveis pelo agravamento dos casos de subnutrição é"), "apoio_de": (1, P1),
    "explicacao": "<p>O texto cita a “má distribuição de renda” entre os fatores que agravam a subnutrição: famílias de baixa ou nenhuma renda não conseguem comprar os alimentos básicos, que ficam <strong>caros demais para elas</strong>. Alternativa <strong>D</strong>.</p><p>O texto não fala de água nos países europeus (A). Ele diz que há muita perda, não ausência de perdas (B). A produção de alimentos não vem diminuindo (C). E a baixa escolaridade não diminui áreas agrícolas (E).</p>"},
3: {"materia": "Matemática", "assunto": "Razão e proporção", "tags": ["notação científica"],
    "enunciado": p("Suponha que", "• não ocorra, no mundo, o desperdício anual de alimento divulgado pela FAO, isto é, que todo esse alimento possa ser tratado e conservado para a alimentação humana; e",
                   "• todo esse alimento seja destinado a todas as pessoas subnutridas do mundo, de acordo com os dados da ONU.",
                   "Nessas condições, em 2015 (ano que teve 365 dias), a quantidade de alimento, em quilogramas, destinada, em média, por pessoa, por dia, estaria mais próxima de"),
    "apoio_de": (1, P1),
    "explicacao": "<p>O desperdício é de 1,3 bilhão de toneladas = 1,3 · 10<sup>12</sup> kg por ano, para 800 milhões de pessoas: 1,3 · 10<sup>12</sup> ÷ 8 · 10<sup>8</sup> ≈ 1 625 kg por pessoa por ano. Por dia: 1 625 ÷ 365 ≈ 4,5 kg, mais próximo de <strong>4</strong>. Alternativa <strong>C</strong>.</p><p>Os outros valores vêm de erros na conversão de toneladas em quilos ou de esquecer de dividir pelos dias do ano.</p>"},
4: {"materia": "Português", "assunto": "Gêneros textuais", "tags": ["cartaz"],
    "enunciado": CARTAZ + P4, "imagens": [CARTAZ_IMG],
    "explicacao": "<p>O cartaz quer convencer o leitor a agir (função injuntiva ou apelativa): tem <strong>caráter persuasivo</strong> e usa <strong>verbo no imperativo</strong>, “Colabore”. Alternativa <strong>A</strong>.</p><p>Ele defende um ponto de vista, não só descreve (B e D). Não tem estrofes nem rimas (C). E não narra um enredo (E).</p>"},
5: {"materia": "Português", "assunto": "Classes de palavras",
    "enunciado": p("As palavras “sete”, “fome” e “colabore”, em destaque no cartaz, podem ser classificadas, correta e respectivamente, nas classes gramaticais"), "apoio_de": (4, P4),
    "explicacao": "<p>“Sete” indica quantidade: <strong>numeral</strong>. “Fome” nomeia uma situação: <strong>substantivo</strong>. “Colabore” é uma ação, no imperativo: <strong>verbo</strong>. Alternativa <strong>E</strong>.</p><p>“Sete” não é artigo (A e B). “Fome” não é preposição nem advérbio (C e D). E “colabore” não é adjetivo, substantivo nem conjunção (A, B e D).</p>"},
6: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": ["nanotecnologia"],
    "enunciado": NANO + P6,
    "explicacao": "<p>O texto diz que as nanopartículas “levam o fármaco, em altas concentrações, até as células cancerosas, evitando que a maioria das células saudáveis sejam atingidas”. Os <strong>fármacos podem ser direcionados</strong> às células tumorais. Alternativa <strong>C</strong>.</p><p>É possível levar as nanopartículas até as células tumorais (A). Elas mataram 70% das tumorais e só 10% das saudáveis (B). O texto fala do risco como possibilidade, sem citar coração e pulmões atingidos, e as nanopartículas eram de sílica revestidas de folato (D). E nanopartículas não são células nem radioativas (E).</p>"},
7: {"materia": "Química", "assunto": "Funções orgânicas", "tags": ["fórmula molecular"],
    "enunciado": p("O uso de fármacos já conhecidos dentro dessas nanoparticulas é uma das aplicações positivas dessa tecnologia. Desse modo, seria usada uma menor quantidade do medicamento e diminuindo, assim, os efeitos colaterais.",
                   "Observe a estrutura do ácido 5-aminosalicílico, fármaco utilizado como anti-inflamatório intestinal.") + "[[fig:1]]"
                 + p("Assinale a alternativa que apresenta a fórmula molecular, desse ácido."),
    "apoio_de": (6, P6),
    "imagens": [{"arquivo": "q07", "alt": "Fórmula estrutural do ácido 5-aminossalicílico: um anel de seis carbonos com três grupos CH; a um carbono do anel ligam-se o NH₂, a outro o OH e a outro o grupo COOH (C ligado a O por ligação dupla e a OH)."}],
    "explicacao": "<p>Contando os átomos: 6 carbonos no anel + 1 no grupo COOH = <strong>7 C</strong>; hidrogênios: 3 dos CH do anel, 2 do NH<sub>2</sub>, 1 do OH e 1 do COOH = <strong>7 H</strong>; <strong>1 N</strong>; e oxigênios: 1 do OH + 2 do COOH = <strong>3 O</strong>. Fórmula: C<sub>7</sub>H<sub>7</sub>NO<sub>3</sub>. Alternativa <strong>A</strong>.</p><p>B esquece um oxigênio. C esquece o carbono do COOH. D e E não indicam as quantidades ou omitem elementos.</p>"},
8: {"materia": "História", "assunto": "História contemporânea", "tags": ["ONU"],
    "enunciado": p("A Carta das Nações Unidas é o documento de fundação da Organização das Nações Unidas (ONU), que ocorreu em 1945. Leia um trecho dessa carta.")
                 + apoio(T(5, "Nós, os povos das Nações Unidas", "grandes e pequenas.")[0]) + url("http://tinyurl.com/gtpa4k3", "23.08.2016")
                 + p("Sobre essa organização, assinale a alternativa correta."),
    "explicacao": "<p>A Declaração Universal dos Direitos Humanos, aprovada pela ONU em 1948, retoma propósitos da Carta, como a fé nos direitos fundamentais e na <strong>dignidade humana</strong>. Alternativa <strong>C</strong>.</p><p>A ONU foi criada em 1945, logo após a Segunda Guerra, e a Guerra Fria veio depois (A). Os países do Eixo foram os derrotados, e a ONU nasceu dos Aliados (B). As duas guerras mundiais aconteceram antes da ONU existir (D). E ela foi iniciativa das grandes potências vencedoras (E).</p>"},
9: {"materia": "Matemática", "assunto": "Geometria plana", "tags": ["área do retângulo"],
    "enunciado": PAINEL + P9, "imagens": [PAINEL_IMG],
    "explicacao": "<p>São 5 filas × 10 painéis × 4 módulos = 200 módulos. Cada módulo tem 0,65 m × 1,5 m = 0,975 m². Área total: 200 × 0,975 = <strong>195 m²</strong>. Alternativa <strong>A</strong>.</p><p>Os outros valores vêm de erros na contagem dos módulos ou na conversão de centímetros para metros.</p>"},
10: {"materia": "Matemática", "assunto": "Trigonometria",
     "enunciado": p("A figura apresenta o modelo matemático para a determinação da distância mínima entre dois painéis de filas paralelas e adjacentes do projeto descrito.")
                  + "[[fig:2]]"
                  + apoio("Na figura, tem-se que:<br>• A: ponto que representa o topo do painel;<br>• B: representa o ponto de apoio do painel no solo;<br>• o segmento \\(\\overline{AB}\\) representa o painel;<br>"
                          "• C: representa o ponto de apoio no solo do painel paralelo e mais próximo;<br>• o segmento \\(\\overline{AH}\\) representa a distância do topo do painel ao solo;<br>"
                          "• β representa a medida do ângulo de incidência dos raios do Sol em relação ao solo*;<br>• d = BC é a distância entre os pontos B e C.",
                          "*A distância mínima entre dois painéis que estão em filas paralelas e adjacentes depende do ângulo (β) de incidência solar às 12 h do dia do solstício de inverno, momento em que o Sol atinge a maior declinação em latitude, medida a partir da linha do equador.")
                  + p("Na figura, sabendo que BH = 120 cm e que, no local de instalação dos painéis, β = 21,80°, a distância mínima (d) entre dois painéis que estão em filas paralelas e adjacentes é, em metros,")
                  + apoio("Dados: sen 21,80° = 0,3714; cos 21,80° = 0,9285; tg 21,80° = 0,40"),
     "apoio_de": (9, P9),
     "imagens": [{"arquivo": "q10", "alt": "Esquema de perfil: dois painéis inclinados, desenhados como segmentos que descem da esquerda para a direita. O topo A do segundo painel fica acima do ponto H do solo; o pé do painel é B. Um raio do Sol passa por A com ângulo β em relação a uma reta paralela ao solo e chega ao solo no ponto C, pé do painel anterior. A distância d vai de C a B."}],
     "explicacao": "<p>Cada painel tem 2 módulos no sentido da inclinação, então AB = 2 × 65 = 130 cm. No triângulo retângulo ABH: AH² = 130² − 120² = 2 500, então AH = 50 cm. No triângulo ACH, tg β = AH ÷ CH, ou seja, 0,40 = 50 ÷ CH, e CH = 125 cm. Então d = CH + HB = 125 + 120 = 245 cm = <strong>2,45 m</strong>. Alternativa <strong>B</strong>.</p><p>Usar o seno ou o cosseno no lugar da tangente, ou esquecer de somar HB, leva aos outros valores.</p>"},
11: {"materia": "Física", "assunto": "Óptica", "tags": ["cor e reflexão"],
     "enunciado": ILHA + P11,
     "explicacao": "<p>Superfícies brancas <strong>refletem</strong> a maior parte da luz que recebem. Assim, a energia é <strong>devolvida para fora</strong> da construção, e o interior esquenta menos. Alternativa <strong>C</strong>.</p><p>Quem absorve a luz são as superfícies escuras (A). Se a luz é refletida, a energia não fica no telhado (B). E a tinta não refrata a luz para dentro ou para fora (D e E).</p>"},
12: {"materia": "Física", "assunto": "Termologia", "tags": ["escalas termométricas"],
     "enunciado": p("O título da campanha, “Um grau a menos”, pode ser ambíguo para algum desavisado, uma vez que a escala termométrica utilizada não é mencionada. Em caráter global, são consideradas três unidades de temperatura: grau Celsius (ºC), grau Fahrenheit (ºF) e kelvin (K). A relação entre as variações de temperaturas nas três escalas é feita por meio das expressões:")
                  + apoio("\\(\\Delta t_K = \\Delta t_C\\) e \\(\\dfrac{\\Delta t_C}{5} = \\dfrac{\\Delta t_F}{9}\\), em que: \\(\\Delta t_K\\) é a variação da temperatura em kelvin; \\(\\Delta t_C\\) é a variação da temperatura em Celsius; \\(\\Delta t_F\\) é a variação da temperatura em Fahrenheit.")
                  + p("Na campanha, a expressão “Um grau a menos” significa que a temperatura do telhado sofrerá variação de 1 grau, como por exemplo, de 30 ºC para 29 ºC.",
                      "Considerando-se que o 1 grau a menos, da campanha, corresponde a 1 ºC, essa variação de temperatura equivale a variação de"),
     "apoio_de": (11, P11),
     "explicacao": "<p>Pela primeira expressão, uma variação de 1 °C é igual a uma variação de <strong>1 K</strong>. Alternativa <strong>B</strong>.</p><p>Em Fahrenheit, 1 °C corresponde a 9/5 = 1,8 °F, não a 1 °F nem a 0,9 °F (A e C). 32 °F e 273 K são pontos da escala (o gelo derretendo), não variações (D e E).</p>"},
13: {"materia": "Geografia", "assunto": "Globalização", "tags": ["ONU", "Haiti"],
     "enunciado": apoio(T(8, "Em um mundo marcado por conflitos", "forma de intervenção armada.")[0]) + url("http://tinyurl.com/gvm8cjv", "26.08.2016")
                  + p("Historicamente, o Brasil envia soldados para participar de operações de paz. Em 2004, foi criada pelo Conselho de Segurança da ONU a Missão das Nações Unidas para Estabilização do Haiti (Minustah).",
                      "De acordo com o texto, essa missão foi criada para"),
     "explicacao": "<p>As operações de paz servem para que as partes em conflito superem suas disputas por meio pacífico. A Minustah foi criada em 2004 para <strong>restabelecer a segurança e a ordem institucional</strong> do Haiti, depois de crises políticas e violência. Alternativa <strong>A</strong>.</p><p>O Haiti não é conhecido por garimpos de diamantes (B), não era o centro do Cartel de Medellín (C), não era o principal poluidor do Caribe (D), e a missão não tinha como foco trabalho escravo em plantações de soja e trigo (E).</p>"},
14: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["mudanças climáticas"],
     "enunciado": apoio(*T(8, "As mudanças climáticas estão ocorrendo", "conservar e recuperar os ecossistemas.", ["Estudos sugerem", "A adaptação às mudanças"]))
                  + p("A partir das informações do texto, é correto afirmar que"),
     "explicacao": "<p>O texto propõe reduzir as emissões de gases do efeito estufa e “conservar e recuperar os ecossistemas” para diminuir os impactos das mudanças climáticas. Alternativa <strong>A</strong>.</p><p>O texto liga a globalização às mudanças climáticas (B). A desertificação é citada como um dos efeitos (C). A tarefa “não é apenas dos governantes” (D). E a redução da biodiversidade aparece entre as consequências (E).</p>"},
15: {"materia": "Química", "assunto": "Funções inorgânicas", "tags": ["chuva ácida"],
     "enunciado": CHUVA + P15, "imagens": [CHUVA_IMG],
     "explicacao": "<p>O ácido do esquema é o ácido sulfúrico, H<sub>2</sub>SO<sub>4</sub>: 2 átomos de hidrogênio + 1 de enxofre + 4 de oxigênio = <strong>7 átomos</strong>. Alternativa <strong>C</strong>.</p><p>A molécula tem três elementos (H, S e O), não dois nem sete (D e E). E 3 e 6 átomos não correspondem à fórmula (A e B).</p>"},
16: {"materia": "Química", "assunto": "Separação de misturas", "tags": ["petróleo"],
     "enunciado": p("Uma forma de atenuar o fenômeno descrito seria a retirada do enxofre dos combustíveis derivados do petróleo, como o diesel e o óleo combustível.", "Esses dois combustíveis são obtidos do petróleo por"),
     "apoio_de": (15, P15),
     "explicacao": "<p>O petróleo é uma mistura de líquidos com pontos de ebulição diferentes. Nas refinarias, ele é separado por <strong>destilação fracionada</strong>, que recolhe cada fração (gasolina, querosene, diesel, óleo combustível) numa faixa de temperatura. Alternativa <strong>E</strong>.</p><p>Filtração e decantação separam sólidos de líquidos ou líquidos que não se misturam (A e C). Sublimação é a passagem de sólido a gás (B). E fusão fracionada separa sólidos pelo ponto de fusão (D).</p>"},
17: {"materia": "Geografia", "assunto": "Climatologia", "tags": ["aquecimento global"],
     "enunciado": p("Considere e reflita sobre a charge que ironiza um fenômeno climático que ocorre no meio ambiente.") + "[[fig:1]]"
                  + url("http://tinyurl.com/j2xno9e", "09.09.16", "Original colorido.") + p("Sobre esse fenômeno é correto afirmar que"),
     "imagens": [{"arquivo": "q17", "alt": "Charge “Aquecimento global”: pinguins diante de uma geladeira, com o gelo derretido ao redor. Um diz: “É tudo o que a gente queria…”; outro responde: “Podemos comprar no crediário…”"}],
     "explicacao": "<p>O aquecimento global é causado principalmente pela intensificação do efeito estufa, e um dos <strong>principais gases responsáveis é o gás carbônico</strong>, liberado na queima de combustíveis fósseis e nas queimadas. Alternativa <strong>B</strong>.</p><p>O gelo polar derrete, não sublima por resfriamento (A). A quantidade de gelo diminui com o aquecimento (C). A camada de ozônio é destruída por outros gases, como os CFCs (D). E os polos estão entre as regiões mais afetadas (E).</p>"},
18: {"materia": "Português", "assunto": "Interpretação de texto", "tags": ["intertextualidade", "charge"],
     "enunciado": ENIGMA + P18, "imagens": [ENIGMA_IMG],
     "explicacao": "<p>A charge retoma e transforma a frase da Esfinge (“Decifra-me, ou devoro-te”) para falar do lixo. Esse diálogo entre textos se chama <strong>intertextualidade</strong>. Alternativa <strong>D</strong>.</p><p>Ambiguidade é o duplo sentido (A). Coesão é a ligação entre partes de um texto (B). Desfecho é o final de uma narrativa (C). E transitividade é a relação do verbo com seus complementos (E).</p>"},
19: {"materia": "Português", "assunto": "Conectivos", "tags": ["orações coordenadas"],
     "enunciado": p("Em “Recicla-me ou te devoro”, há a presença de duas orações que estabelecem entre si uma relação de"), "apoio_de": (18, P18),
     "explicacao": "<p>A conjunção “ou” liga duas possibilidades que se excluem: ou acontece uma coisa, ou a outra. É uma relação de <strong>alternância</strong>. Alternativa <strong>B</strong>.</p><p>Adição seria com “e” (A). Conclusão, com “portanto” (C). Explicação, com “pois” (D). E oposição, com “mas” (E).</p>"},
20: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["lixo", "reciclagem"],
     "enunciado": LIXO + P20,
     "explicacao": "<p>O texto explica que o lixo exposto atrai baratas, ratos, insetos e urubus, que transmitem várias doenças. Reciclar diminui o lixo acumulado e, assim, <strong>pode reduzir a proliferação de doenças</strong> por esses animais. Alternativa <strong>C</strong>.</p><p>É o lixo, e não a reciclagem, que dificulta o fluxo dos rios (A). A reciclagem não elimina animais (B). O chorume espalha metais pesados tóxicos, que não são essenciais (D). E ele contamina o solo, não o fertiliza (E).</p>"},
21: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["lixões"],
     "enunciado": p("No Brasil, grande parte do lixo ainda é dispensada em lixões, que são áreas que não são preparadas para receber o lixo de forma ambientalmente adequada.", "O descarte do lixo nesse tipo de área pode causar"),
     "apoio_de": (20, P20),
     "explicacao": "<p>Nos lixões, o lixo fica direto sobre o solo, sem impermeabilização. O <strong>chorume</strong> produzido pela decomposição infiltra no solo e pode <strong>contaminar o lençol freático</strong>. Alternativa <strong>C</strong>.</p><p>A inversão térmica ocorre na baixa atmosfera, não por causa do lixo na mesosfera (A). Lixões não são asfaltados (B). Lixo hospitalar não deve ir para lixões, e a chuva ácida vem de gases de combustão (D). E as ilhas de calor aquecem os centros urbanos (E).</p>"},
22: {"materia": "Matemática", "assunto": "Porcentagem", "tags": ["notação científica"],
     "enunciado": p("Leia os trechos para responder à questão.")
                  + apoio(T(11, "Os benefícios da reciclagem do papel", "15 a 20 árvores.")[0]) + url("http://tinyurl.com/5s9g6ub", "12.09.2016")
                  + apoio(T(11, "Em 2015, 46,3% do papel", "cadeia produtiva.")[0]) + url("http://tinyurl.com/3gldkj5", "12.09.2016")
                  + p("No Brasil, em 2015, considerando uma produção e comercialização total de 10 milhões de toneladas de papel, de acordo com os dados dos trechos, podem-se salvar até N árvores.", "O valor de N é"),
     "alternativas": {"A": "2,315 · 10<sup>4</sup>.", "B": "2,315 · 10<sup>5</sup>.", "C": "9,260 · 10<sup>6</sup>.", "D": "9,260 · 10<sup>7</sup>.", "E": "9,260 · 10<sup>8</sup>."},
     "explicacao": "<p>Foram reciclados 46,3% de 10 milhões de toneladas: 0,463 · 10<sup>7</sup> = 4,63 · 10<sup>6</sup> t. Com até 20 árvores salvas por tonelada: N = 20 · 4,63 · 10<sup>6</sup> = 92,6 · 10<sup>6</sup> = <strong>9,260 · 10<sup>7</sup></strong>. Alternativa <strong>D</strong>.</p><p>C e E erram a potência de 10. A e B usam outros fatores, como 15 árvores ou 5 árvores por tonelada, com potências erradas.</p>"},
23: {"materia": "Física", "assunto": "Eletrostática", "tags": ["eletrização"],
     "explicacao": "<p>Um corpo fica com carga positiva quando <strong>perde elétrons</strong>, que são as partículas que se movem de um corpo a outro na eletrização. Alternativa <strong>D</strong>.</p><p>Prótons e nêutrons ficam presos no núcleo e não são trocados na eletrização por atrito (A, B, C e E). E nêutrons nem têm carga.</p>"},
24: {"materia": "História", "assunto": "Povos indígenas", "tags": ["patrimônio imaterial"],
     "explicacao": "<p>O texto diz que o registro dos saberes indígenas do Alto Rio Negro como patrimônio, e a difusão desses conhecimentos, permite à sociedade “aprender a desenvolver atividades agrícolas menos danosas ao meio ambiente”. Alternativa <strong>B</strong>.</p><p>O Alto Rio Negro fica na Amazônia, não na caatinga (A). Os povos não são do Centro-Sul, e o texto não fala em exportação (C). Não são do Maranhão, e o registro é de 2010 (D). E o IPHAN reconheceu essas práticas como valiosas, não como danosas (E).</p>"},
25: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": ["saneamento"],
     "explicacao": "<p>Sem tratamento de esgoto, água e alimentos se contaminam com fezes, transmitindo <strong>diarreias, cólera e verminoses</strong>. Alternativa <strong>B</strong>.</p><p>Gripe e AIDS não são transmitidas por esgoto, e a hepatite C passa pelo sangue (A). Dengue e febre amarela são transmitidas por mosquitos, e a varíola por contato entre pessoas (C e E). A elefantíase é transmitida por mosquito (D).</p>"},
26: {"materia": "Geografia", "assunto": "Hidrografia", "tags": ["recursos hídricos"],
     "explicacao": "<p>O texto diz que, em escassez, o uso prioritário da água é o <strong>consumo humano e a dessedentação de animais</strong>. Os demais usos vêm depois. Alternativa <strong>D</strong>.</p><p>A lei não proíbe racionamento nem garante água gratuita a qualquer uso (A). A água não fica parada nos reservatórios (B). A indústria não tem prioridade (C). E não basta poder pagar (E).</p>"},
27: {"materia": "Português", "assunto": "Interpretação de texto",
     "enunciado": ADICHIE + P27,
     "explicacao": "<p>Para a escritora, as histórias são definidas pelo “nkali”, “ser maior do que o outro”: quem tem o poder conta a história e repete uma única imagem de um povo, que passa a ser a única forma como ele é visto. Alternativa <strong>C</strong>.</p><p>A ideia é o oposto de considerar a diversidade (A) e de respeitar as características do outro (B). O “nkali” é a estrutura de poder, não falar de outras histórias (D). E a repetição faz o povo se tornar aquilo, não evitar (E).</p>"},
28: {"materia": "História", "assunto": "Imperialismo e neocolonialismo",
     "enunciado": p("Assinale a alternativa que apresenta corretamente um exemplo, observado no continente de origem da escritora, de uma forma de dominação de um povo sobre outros."),
     "apoio_de": (27, P27),
     "explicacao": "<p>A escritora é nigeriana, da África. A partir do fim do século XIX, no <strong>imperialismo</strong> (Conferência de Berlim, 1884-1885), as potências europeias dividiram o território africano entre si. Alternativa <strong>C</strong>.</p><p>A, B e D falam da Ásia ou de situações históricas inventadas. E o apartheid foi na África do Sul, no século XX; o Haiti nem fica na África (E).</p>"},
29: {"materia": "Matemática", "assunto": "Operações e problemas", "tags": ["consumo de água"],
     "enunciado": apoio(*T(13, "A quantidade mínima de água necessária", "causado por vazamentos.", ["Para saber se você", "Se o resultado for"]))
                  .replace(" 3 menor que 150 L", "<br>✓ menor que 150 L").replace(" 3 entre 150 e 300 L", "<br>✓ entre 150 e 300 L").replace(" 3 maior de 300 L", "<br>✓ maior de 300 L")
                  + url("http://tinyurl.com/zzaso7z", "10.09.16")
                  + p("O consumo de água referente ao mês de setembro de uma residência com 5 moradores foi de 25 m<sup>3</sup>.",
                      "Sobre o consumo médio por morador por dia, é correto afirmar que esses, moradores"),
     "explicacao": "<p>25 m³ = 25 000 L. Setembro tem 30 dias e são 5 moradores: 25 000 ÷ 30 ÷ 5 ≈ 167 L por pessoa por dia. O valor fica entre 150 e 300 L: os moradores <strong>estão no limite do bom senso</strong>. Alternativa <strong>B</strong>.</p><p>Economia seria menos de 150 L (A e C). Refletir e procurar vazamentos valem para mais de 300 L (D e E).</p>"},
30: {"materia": "Química", "assunto": "Separação de misturas", "tags": ["tratamento de água"],
     "explicacao": "<p>Nas estações de tratamento, a água passa por <strong>floculação</strong> (as impurezas se juntam em flocos), <strong>decantação</strong> (os flocos se depositam), <strong>filtração</strong> e <strong>cloração</strong> (desinfecção), entre outras etapas. Alternativa <strong>E</strong>.</p><p>A, B e C deixam de fora etapas essenciais. E sublimação não faz parte do tratamento de água (D).</p>"},
31: {"materia": "Geografia", "assunto": "Globalização", "tags": ["cidades-irmãs"],
     "enunciado": IRMAS + P31,
     "explicacao": "<p>O texto diz que os acordos surgiram em 1947, logo após a Segunda Guerra, e que “inicialmente, seu principal objetivo era selar a paz e promover a reconciliação” entre países que tinham lutado em lados opostos. Alternativa <strong>E</strong>.</p><p>O texto não fala do Conselho de Segurança nem de religiões (A). As parcerias são reconhecidas oficialmente (B). Não há proibição entre cidades do mesmo continente (C). E as cidades não passam a ter um único prefeito (D).</p>"},
32: {"materia": "Geografia", "assunto": "Cartografia", "tags": ["continentes"],
     "enunciado": p("Dentre as cidades citadas como “irmãs” da capital paulista, podemos afirmar corretamente que"), "apoio_de": (31, P31),
     "explicacao": "<p>Contando as cidades citadas: Europa: Milão, Lisboa, Bucareste, Barcelona e Coimbra (5). Ásia: Osaka, Seul, Pequim, Tel Aviv, Xangai e Damasco (6). América: Chicago, La Paz, Buenos Aires, Lima, Santiago do Chile, Toronto, Miami, Montevidéu e Havana (9). África: Luanda (1). Há <strong>menos cidades africanas do que americanas</strong>. Alternativa <strong>D</strong>.</p><p>São 5 europeias, não 7 (A). Nenhuma é da Oceania (B). Há menos europeias que asiáticas (C). E há 9 americanas e 6 asiáticas (E).</p>"},
33: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": ["vacinas"],
     "enunciado": VACINA + P33,
     "explicacao": "<p>O texto diz que o programa de vacinação é “extremamente eficaz”, mas que “em alguns indivíduos, após a aplicação, podem ocorrer também efeitos colaterais como febre, inchaço no local da picada e náuseas”. Alternativa <strong>B</strong>.</p><p>A vacina da dengue é feita com vírus, não com bactérias (A). A faixa de 9 a 45 anos vale só para a vacina da dengue (C). As vacinas estimulam o corpo a produzir anticorpos, não os contêm (D). E a dengue é transmitida pelo mosquito <em>Aedes aegypti</em>, não por tosse (E).</p>"},
34: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": ["vacinas"],
     "enunciado": p("A produção de vacinas exige conhecimento técnico e controle de qualidade. Nessa produção, duas fases principais são importantes: a fase biológica, que identifica e faz as culturas dos micro-organismos causadores da doença, que serão, posteriormente, atenuados ou inativados; e a fase farmacêutica, que consiste na obtenção final do produto.",
                    "Assim, considerando uma vacina contra a dengue, para que sua eficiência seja constatada, ela deverá"),
     "apoio_de": (33, P33),
     "explicacao": "<p>Uma vacina eficiente faz o organismo vacinado <strong>produzir anticorpos específicos</strong> contra o vírus, criando memória imunológica. Alternativa <strong>E</strong>.</p><p>A defesa é feita pelos glóbulos brancos e anticorpos, não pelos vermelhos (A). A dengue é transmitida por mosquito, não por roedores (B). Vacinas não modificam o material genético (C). E combater o vetor no ambiente não é função da vacina (D).</p>"},
35: {"materia": "Biologia", "assunto": "Nutrição e saúde", "tags": ["leite materno"],
     "enunciado": LEITE + P35,
     "explicacao": "<p>Pela tabela, o leite maduro a pré-termo tem 6,0 g/dL de lactose, mais que o leite de vaca (4,8 g/dL), e 1,4 g/dL de proteína, menos que o colostro (1,9 ou 2,1 g/dL). Alternativa <strong>D</strong>.</p><p>O leite maduro a termo tem 6,5 g/dL de lactose, não 7,0 (A). A lactoalbumina é a proteína do leite materno; a do leite de vaca é a caseína, de difícil digestão (B e C). E o colostro tem menos lipídios que o leite maduro (E).</p>"},
36: {"materia": "Matemática", "assunto": "Razão e proporção", "tags": ["concentração"],
     "enunciado": p("A quantidade de lactose que um bebê a pré-termo de 4 dias ingere ao ser amamentado com 80 mL de leite materno é, em gramas,"), "apoio_de": (35, P35),
     "explicacao": "<p>Com 4 dias, o bebê toma colostro; a pré-termo, ele tem 5,0 g de lactose por decilitro (100 mL). Em 80 mL = 0,8 dL: 5,0 · 0,8 = <strong>4,0 g</strong>. Alternativa <strong>C</strong>.</p><p>0,4 e 40 vêm de errar a conversão de mililitros em decilitros (B e D).</p>"},
37: {"materia": "Física", "assunto": "Cinemática", "tags": ["velocidade média"],
     "enunciado": RAMPA + P37, "imagens": [RAMPA_IMG],
     "explicacao": "<p>Com velocidade constante, t = d ÷ v = 6 ÷ 0,2 = <strong>30 s</strong>. Alternativa <strong>D</strong>.</p><p>A rampa tem 6 m de comprimento, e é esse o caminho percorrido pela cadeira (não o desnível vertical). Os outros valores vêm de dividir ou multiplicar errado: 6 · 2 = 12 (A), 6 ÷ 0,4 = 15 (B) ou 6 ÷ 0,3 = 20 (C).</p>"},
38: {"materia": "Física", "assunto": "Energia", "tags": ["potência", "máquinas simples"],
     "enunciado": apoio("Considere que:<br>• uma rampa é um exemplo de máquina simples, oferecendo uma vantagem mecânica para quem a utiliza;<br>• uma pessoa, subindo pela escada ou pela rampa, tem que realizar o mesmo trabalho contra a força peso;<br>• essa mesma pessoa suba pela escada em um tempo menor que o necessário para subir pela rampa.")
                  + p("A vantagem do uso da rampa para realizar o trabalho contra a força peso, em comparação com o uso da escada, se deve ao fato de que, pela rampa,"),
     "apoio_de": (37, P37),
     "explicacao": "<p>Potência é trabalho dividido pelo tempo. O trabalho é o mesmo nos dois caminhos, mas pela rampa ele é feito em mais tempo, então a <strong>potência empregada é menor</strong>. Alternativa <strong>A</strong>.</p><p>A potência não é maior nem igual, porque o tempo pela rampa é maior (B e C). E a energia potencial gravitacional ganha é a mesma, pois o desnível é o mesmo (D e E).</p>"},
39: {"materia": "Português", "assunto": "Interpretação de texto", "tags": ["tirinha"],
     "enunciado": MAFALDA + P39, "imagens": [MAFALDA_IMG],
     "explicacao": "<p>“Ficar impassível” é não se abalar, não se importar. Mafalda diz ironicamente que o pai “<strong>se preocupa</strong>” com uma coisa importante, expressão de sentido oposto. Alternativa <strong>C</strong>.</p><p>“O número de crianças”, “é bom ver”, “com uma coisa” e “ser como você” não se opõem a “ficar impassível” (A, B, D e E).</p>"},
40: {"materia": "Português", "assunto": "Classes de palavras", "tags": ["vocativo"],
     "enunciado": p("Na tirinha, Mafalda faz uso de um vocativo. Ela usa esse termo – que atua como uma forma de chamamento de um interlocutor real ou hipotético – como forma de deixar evidente o seu interlocutor.",
                    "Tendo isso em vista, assinale a alternativa que contenha o vocativo utilizado por Mafalda."),
     "apoio_de": (39, P39),
     "explicacao": "<p>Em “É bom ver que você se preocupa com uma coisa tão importante, <strong>papai</strong>!”, Mafalda chama o pai: “papai” é o vocativo, separado por vírgula. Alternativa <strong>D</strong>.</p><p>“Você” é o sujeito da oração (A). “Se” é pronome (B). “Tão” é advérbio de intensidade (C). E “como” é conjunção (E).</p>"},
41: {"materia": "História", "assunto": "Idade Média", "tags": ["expansão árabe"],
     "enunciado": enun(R, 41, figs={"p19-1": 1}).replace("<p>Sobre esse período", fonte("VICENTINO, C.; DORIGO, G. <em>História Geral e do Brasil</em>. São Paulo: Scipione, 2010, p. 177.") + "<p>Sobre esse período"),
     "imagens": [{"arquivo": "q41", "alt": "Mapa da expansão árabe: em tom escuro, as conquistas durante a vida de Maomé, na Arábia (Medina e Meca); em tom mais claro, as conquistas dos califas (632 a 750), do norte da África e da Península Ibérica (Córdoba, Sevilha) até a Pérsia e Samarcanda. Poitiers, na França, e o Império Bizantino ficam fora da área conquistada."}],
     "explicacao": "<p>A expansão árabe chegou à Península Ibérica (Al-Andalus) e, por ali, levou à Europa conhecimentos de <strong>Álgebra, Astronomia, Medicina</strong> e Filosofia, além de transformações culturais. Alternativa <strong>E</strong>.</p><p>O Império Romano do Ocidente já tinha acabado (476), e os árabes difundiram o árabe, não o latim (A). Os árabes não atravessaram o Atlântico (B). Bizantinos e francos resistiram ao avanço, como na batalha de Poitiers, e o período é a Idade Média (C). E os árabes não dominaram Bizâncio, Poitiers nem Roma (D).</p>"},
42: {"materia": "Matemática", "assunto": "Equações",
     "explicacao": "<p>Seja <em>x</em> a proteína do arroz; a da lentilha é 3<em>x</em>. Então <em>x</em> + 3<em>x</em> = 28, ou seja, <em>x</em> = <strong>7 g de proteína do arroz</strong> (e 21 g da lentilha). Alternativa <strong>A</strong>.</p><p>As outras quantidades não respeitam a relação de triplo: a lentilha deu 21 g, não 23 nem 25 (D e E).</p>"},
43: {"materia": "Geografia", "assunto": "Globalização", "tags": ["refugiados", "charge"],
     "enunciado": p("Analise esta charge do cartunista Latuff.") + "[[fig:1]]" + url("http://tinyurl.com/htthtb7", "23.09.2016", "Original colorido.") + p("É correto afirmar que a charge"),
     "imagens": [{"arquivo": "q43", "alt": "Charge de Latuff, de 2015: na beira do mar, à noite, os corpos de um homem, uma mulher e uma criança estão caídos na água rasa; ao lado deles, uma placa com a palavra “Imigração”. O céu escuro tem estrelas amarelas, como as da bandeira da União Europeia."}],
     "alternativas": {"A": "ilustra a imigração de europeus após os diversos atentados ocorridos recentemente em países como França e Itália.",
                      "B": "ironiza o muro de contenção à imigração mexicana nos Estados Unidos, construído no norte do país no início de 2015.",
                      "C": "critica a ação brasileira em relação aos refugiados haitianos, que morrem ao tentar atravessar o mar do Norte rumo ao Brasil.",
                      "D": "apresenta a questão dos refugiados, sobretudo sírios que, por conta da guerra em seu país, tentam chegar à Europa pelo Mediterrâneo.",
                      "E": "debate a situação dos jovens britânicos que, por conta da saída do Reino Unido da União Europeia, têm dificuldades para emigrar para os países vizinhos."},
     "explicacao": "<p>A charge, de 2015, mostra uma família morta no mar sob um céu com as estrelas da União Europeia. Ela trata da <strong>crise dos refugiados</strong>, principalmente sírios fugindo da guerra, que morriam tentando chegar à Europa pelo Mediterrâneo. Alternativa <strong>D</strong>.</p><p>Não se trata de europeus emigrando (A) nem da fronteira dos Estados Unidos (B). Haitianos não atravessam o mar do Norte para chegar ao Brasil (C). E a saída do Reino Unido da União Europeia foi decidida só em 2016 (E).</p>"},
44: {"materia": "Biologia", "assunto": "Fisiologia humana", "tags": ["sistema cardiovascular"],
     "enunciado": enun(R, 44),
     "alternativas": {"A": "pericardite.", "B": "infarto agudo do miocárdio.", "C": "doença vascular periférica.", "D": "acidente vascular cerebral.", "E": "doença das válvulas cardíacas."},
     "explicacao": "<p>As artérias coronárias levam sangue ao músculo do coração (miocárdio). Quando são obstruídas, parte do miocárdio fica sem oxigênio e pode morrer: é o <strong>infarto agudo do miocárdio</strong>. Alternativa <strong>B</strong>.</p><p>Pericardite é a inflamação da membrana que envolve o coração (A). A doença vascular periférica atinge as artérias dos membros (C). O AVC atinge os vasos do cérebro (D). E as doenças das válvulas não envolvem as coronárias (E).</p>"},
45: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": ["desenvolvimento sustentável"],
     "enunciado": SAL + P45, "imagens": [SAL_IMG],
     "alternativas": {"A": "investir na automação industrial, que substitui a mão de obra humana pelas máquinas e acaba com a destruição do meio ambiente.",
                      "B": "diminuir o consumo de bens materiais e buscar formas de conciliar o progresso econômico com a preservação dos recursos ambientais.",
                      "C": "realizar reformas urbanas que permitam desmatar áreas de florestas nativas e construir cidades cada vez mais tecnológicas, democráticas e limpas.",
                      "D": "eliminar o consumo de bens não duráveis e aumentar a retirada de matérias-primas da natureza, para trazer de volta o equilíbrio natural do planeta Terra.",
                      "E": "explorar mais as reservas de sal, pois a natureza não tem fornecido matérias-primas adequadas para a produção de alimentos, encarecendo os produtos agrícolas."},
     "explicacao": "<p>A letra critica o planeta maltratado “por dinheiro” e fala em repartir melhor o pão e recriar o paraíso “para merecer quem vem depois”. Isso combina com <strong>consumir menos e conciliar o progresso com a preservação</strong> dos recursos. Alternativa <strong>B</strong>.</p><p>A automação não acaba com a destruição ambiental (A). Desmatar florestas nativas vai contra a ideia da canção (C). Retirar mais matérias-primas não traz equilíbrio (D). E “o sal da Terra” é uma metáfora, não fala de reservas de sal (E).</p>"},
46: {"materia": "Física", "assunto": "Magnetismo", "tags": ["ímãs"],
     "enunciado": apoio(*T(21, "Pela primeira vez, cientistas detectaram", "constitui um ímã natural.", ["Um desses materiais"]))
                  + url("http://tinyurl.com/hzvm3fh", "30.09.16")
                  + p("Sobre o óxido citado no texto, é correto afirmar que ele apresenta"),
     "explicacao": "<p>Todo ímã, como a magnetita, tem <strong>dois polos magnéticos, norte e sul</strong>, e <strong>os dois atraem o ferro</strong>, que não é um ímã. Alternativa <strong>A</strong>.</p><p>Os dois polos atraem o ferro, não só um deles (B e C). E ímãs não têm polos leste e oeste; esses são pontos cardeais (D e E).</p>"},
47: {"materia": "História", "assunto": "Brasil República", "tags": ["Constituição de 1988"],
     "explicacao": "<p>A Constituição de 1988, chamada de “Constituição Cidadã” por Ulysses Guimarães, define no artigo 3º, entre os objetivos do país, a <strong>redução das desigualdades sociais e regionais</strong>. Alternativa <strong>B</strong>.</p><p>Ela é de 1988, e o voto feminino veio em 1932 (A). Foi feita por uma Assembleia Constituinte, não por senadores no início do século XX (C). Está em vigor desde 1988 e incorpora tratados de direitos humanos (D). E a Constituição de 1967 foi a do regime militar, não a atual (E).</p>"},
48: {"materia": "Física", "assunto": "Termologia", "tags": ["dilatação térmica"],
     "enunciado": enun(R, 48, trocas=[("[[FIG:p22-1]]", apoio("Para um objeto como um muro, o acréscimo ou decréscimo da área da superfície do muro é calculado pela expressão: \\(\\Delta S = S_0 \\cdot \\beta \\cdot \\Delta\\theta\\)",
                                                              "Em que: ΔS → representa a variação (acréscimo ou diminuição) da área da superfície que o muro apresentará; S<sub>0</sub> → é a área original da superfície do muro, antes de ocorrer a dilatação térmica; β → é uma constante que está relacionada com o material que foi utilizado em sua construção; Δθ → é a variação de temperatura à qual o muro é submetido."))], tirar_figs=False),
     "explicacao": "<p>Com o mesmo material (mesmo β): muro menor, ΔS = 100 · β · 20 = 2 000β; muro maior, ΔS = 200 · β · 40 = 8 000β. A variação do maior é <strong>quatro vezes maior</strong>. Alternativa <strong>E</strong>.</p><p>Considerar só a área ou só a temperatura dobradas dá “duas vezes maior” (D). E o muro maior, mais aquecido, não pode dilatar menos (A e B).</p>"},
49: {"materia": "Português", "assunto": "Interpretação de texto",
     "enunciado": EMPATIA + P49,
     "explicacao": "<p>O texto define empatia como “a capacidade de se colocar no lugar do outro, de compreendê-lo emocionalmente”, ou seja, <strong>identificar-se</strong> com o outro. Alternativa <strong>D</strong>.</p><p>Esforço, exigência e determinação não têm esse sentido (A, B e E). E o narcisismo é o contrário: ele “impede a empatia” (C).</p>"},
50: {"materia": "Português", "assunto": "Conectivos",
     "enunciado": p("Releia as sentenças do texto.")
                  + apoio("• Se pisam no seu pé, reclama e exige que os holofotes se voltem para essa agressão gravíssima.<br>• Se pisarem no pé do outro, é porque o outro fez por merecer.")
                  + p("A autora não utilizou nenhum elemento coesivo para interligar ambas as sentenças. Se um revisor decidisse unir esses dois períodos e inserir o período resultante novamente no texto, preservando o sentido original pretendido pela autora, ele deveria utilizar o(s) elemento(s) coesivo(s)"),
     "apoio_de": (49, P49),
     "explicacao": "<p>As duas frases mostram atitudes opostas do narcisista: reclama quando é com ele, mas acha justo quando é com o outro. A relação é de <strong>oposição</strong>, expressa por “<strong>no entanto</strong>”. Alternativa <strong>D</strong>.</p><p>“Que” e “porque” não indicam oposição (A e C). E “não só… como também” indicam adição (B e E).</p>"},
}
completar(Q, R)
