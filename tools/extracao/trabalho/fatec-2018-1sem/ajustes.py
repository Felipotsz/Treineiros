# Ajustes da conferência humana: Vestibular FATEC 1º semestre de 2018 (exame de 14/01/2018)
# Texto conferido com a imagem de cada página. Tema implícito: Trabalho (redação: o emprego perfeito: realidade ou ficção?).
# 54 questões; a prova tem 5 h no total, incluindo a redação (que fica fora do simulado).
# Matéria: a do gabarito oficial; nas "Multidisciplinar", a matéria principal + tag "multidisciplinar".
# Rascunho com colunas embaralhadas: enunciados e alternativas escritos aqui.
# Gabarito: oficial (1º SEM/18), sem anuladas. Q36: gabarito oficial D (20 di) diverge da conta exata (24 di): observação na explicação.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import A, carregar, enun, tabela, colunas, completar, trecho

ID = "fatec-2018-1sem"
META = {
    "id": ID,
    "banca": "FATEC",
    "ano": 2018,
    "semestre": 1,
    "titulo": "Vestibular FATEC, 1º semestre de 2018",
    "fonte": "Centro Paula Souza",
    "dataExame": "2018-01-14",
    "duracaoMinutos": 300,
    "tema": "Trabalho",
}

R = carregar(ID)
MULTI = ["multidisciplinar"]


def T(pag, inicio, fim, paragrafos=()):
    fix = lambda x: x.replace("ﬀ ", "ff").replace("ﬃ ", "ffi").replace("ﬄ ", "ffl").replace("ﬀ", "ff").replace("ﬃ", "ffi").replace("ﬄ", "ffl")
    return [fix(x) for x in trecho(ID, pag, inicio, fix(fim) if False else fim, paragrafos)]


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

def AL(pag, inicio, fim):
    """Alternativas copiadas do texto do PDF: de '(A) ...' até o fim da (E)."""
    s = " ".join(T(pag, inicio, fim))
    partes = re.split(r"\(([A-E])\)\s*", s)
    d = {partes[i]: partes[i + 1].strip() for i in range(1, len(partes) - 1, 2)}
    assert list(d) == list("ABCDE"), (pag, inicio, list(d))
    return d


# ---------- textos compartilhados ----------
DESIG = (chamada("Leia o texto para responder às questões de números 03 e 04.")
         + apoio("<strong>A desigualdade no mundo</strong>", *T(3, "Neste momento, o 1% mais rico", "níveis de desigualdade.", ["Após décadas de trabalho"]))
         + url("https://tinyurl.com/y8bbbchy", "31.10.2017")
         + p("*Riqueza é a soma dos valores de bens materiais, como imóveis ou propriedades, e de bens financeiros, como aplicações ou ações.", classe="fonte")
         + apoio("Adote:<br>• Total da riqueza mundial: 250 trilhões de dólares;<br>• Total da riqueza concentrada pelas oito pessoas mais ricas do mundo: 428,4 bilhões de dólares;<br>• Total da população mundial: 7,2 bilhões de habitantes."))
P3 = p("A média da riqueza, por pessoa, entre os que fazem parte do 1% mais rico da população mundial é, em milhões de dólares, aproximadamente igual a")

SACHE = (chamada("Leia o texto para responder às questões de números 20 a 22.")
         + apoio(*[x.replace("(Ca2+)", "(Ca<sup>2+</sup>)").replace("(SO4", "(SO<sub>4</sub><sup>2–</sup>").replace("ClO1–", "C<em>ℓ</em>O<sup>1–</sup>").replace("</sup> )", "</sup>)") for x in
                   T(10, "Estima-se que cerca de um bilhão", "água limpa para o consumo.", ["Para purificar a água", "Assim, em pouco tempo"])])
         + url("http://tinyurl.com/y7gdw9qx", "13.11.2017"))
P20 = p("Dois processos de separação de misturas descritos no texto são")

CARRO = (chamada("Leia o texto para responder às questões de números 23 e 24.")
         + apoio("<strong>De onde vem o cheiro de carro novo?</strong>", " ".join(T(11, "De acordo com o gerente de uma montadora", "altas temperaturas para evaporarem.")).replace("(COVs)", "(COV<sub>S</sub>)"))
         + url("http://tinyurl.com/y8ucob6c", "13.11.2017"))
P23 = p("É correto afirmar que os compostos orgânicos responsáveis pelo cheiro de carro novo apresentam")

FAKE = (chamada("Leia o texto para responder às questões de números 25 a 29.")
        + apoio("<strong>Technology brought us fake news — and it will help us kill it</strong>",
                *T(12, "“Fake news” - websites disseminating", "revenue from Facebook.", ["Fake news is news that affects", "On the positive side", "Forbes indicates"]))
        + url("https://tinyurl.com/y8jfq2t4", "07.11.2017")
        + apoio("<strong>Glossário</strong><br><em>beget</em><sup>1</sup>: gerar, criar, produzir.<br><em>fallout</em><sup>2</sup>: efeitos negativos."))
FAKE = FAKE.replace("beget1", "beget<sup>1</sup>").replace("fallout2", "fallout<sup>2</sup>")
P25 = p("Assinale a alternativa correta, de acordo com o texto.")

PIRAMIDE = (chamada("Leia os textos e o gráfico para responder às questões de números 32 a 34.")
            + p(" ".join(T(14, "Um artista plástico deseja construir", "todas as suas proporções."))) + "[[fig:1]]"
            + apoio("Nesse gráfico, considere que a altura da pirâmide referente à riqueza dos 10% mais ricos seja 90% da altura da pirâmide total de distribuição de riqueza e que essas pirâmides sejam semelhantes entre si.")
            + p("Para construir a obra, ele utilizará quatro triângulos isósceles congruentes entre si e um quadrado, todos feitos de metal, deixando o interior da pirâmide vazio. A pirâmide terá 4 metros de altura, e a base quadrada terá 6 metros de lado."))
PIRAMIDE_IMG = figs(("q32", "Gráfico “Distribuição da riqueza entre os 10% mais ricos e os 90% mais pobres — Brasil”: uma pirâmide de base quadrada em que quase toda a pirâmide, a parte de cima, é escura (mais ricos) e só uma fatia fina junto à base é clara (mais pobres)."))
P32 = p("No gráfico, o percentual que o volume da pirâmide referente aos 10% mais ricos representa do volume total é, aproximadamente, igual a")

RADAR = (chamada("Leia o texto para responder às questões de números 35 a 37.")
         + p(" ".join(T(15, "Os dispositivos eletrônicos colocados", "conforme a figura.")).replace("1o laço", "1º laço").replace("2o laço", "2º laço")) + "[[fig:1]]"
         + p("Essas duas velocidades medidas são validadas e correlacionadas com as velocidades a serem consideradas (V<sub>C</sub>), conforme apresentado na tabela parcial de valores referenciais de velocidade para infrações (art. 218 do Código de Trânsito Brasileiro – CTB). Caso essas velocidades verificadas no 1º e no 2º laço sejam iguais, esse valor é denominado <em>velocidade medida</em> (V<sub>M</sub>), e ele é relacionado à <em>velocidade considerada</em> (V<sub>C</sub>). A câmera fotográfica é acionada para registrar a imagem da placa do veículo a ser multado apenas nas situações em que esse esteja trafegando acima do limite máximo permitido para aquele local e faixa de rolamento, considerando os valores de V<sub>C</sub>.")
         + p("<strong>Tabela Parcial de Velocidades Referenciais</strong> (Art. 218 CTB)")
         + tabela(["V<sub>M</sub> (km/h)", "V<sub>C</sub> (km/h)"], [["90", "83"], ["81", "74"], ["72", "65"], ["63", "56"], ["54", "47"], ["45", "38"]]))
RADAR_IMG = figs(("q35", "Vista de cima de uma pista com faixas de rolamento. Em cada faixa há três sensores no chão, ligados em sequência, formando o 1º e o 2º laço; um carro, à esquerda, passa sobre eles, e câmeras nos postes laterais apontam para a pista."))
P35 = p("Considere que, em cada faixa de rolagem, os sensores estejam distantes entre si cerca de 3 metros e suponha que o carro da figura esteja deslocando-se para a esquerda e passe pelo primeiro laço com uma velocidade de 15 m/s, levando, portanto, 0,20 s para passar pelo segundo laço.",
        "Se a velocidade limite dessa pista for 50 km/h, podemos afirmar que o veículo")

CERRADO = (chamada("Leia o texto para responder às questões de números 40 e 41.")
           + apoio(*T(16, "(...) segundo maior bioma da América do Sul", "expansão da fronteira agrícola brasileira.", ["Considerado como um dos", "Nas três últimas décadas"]))
           + url("http://www.mma.gov.br/biomas", "07.11.2017")
           + p("*<em>hotspots</em> são áreas de elevada riqueza natural em termos de biodiversidade e que carecem de uma urgente conservação", classe="fonte"))
CERRADO = CERRADO.replace("*hotspots mundiais", "*<em>hotspots</em> mundiais").replace("Estima- se", "Estima-se")
P40 = p("Assinale a alternativa que contenha o bioma ao qual o texto faz referência.")

ESTILO = (chamada("Leia o texto para responder às questões de números 50 a 52.")
          + apoio("<strong>Palavras: uma questão de estilo</strong><br><em>A construção de um bom texto depende da criatividade de quem o escreve. Veja como o uso das palavras exerce um papel importante nesse contexto.</em>",
                  " ".join(T(20, "João Ribeiro, eminente gramático", "olfativas ou gustativas.")))
          + url("https://tinyurl.com/y7wzrn8k", "07.11.2017"))
ESTILO = ESTILO.replace("(O Momento Literário)", "(<em>O Momento Literário</em>)").replace("romance Memorial de Aires", "romance <em>Memorial de Aires</em>")
P50 = p("Assinale a afirmação correta a respeito das ideias presentes no texto.")

Q = {
1: {"materia": "Português", "assunto": "Interpretação de texto", "tags": MULTI + ["Maslow", "motivação"],
    "enunciado": p("Leia o texto.") + apoio(" ".join(T(2, "O ser humano é único em sua essência.", "de autoestima e de autorrealização."))) + url("https://tinyurl.com/y968aj3g", "07.11.2017")
                 + p("O texto cita a Teoria da Hierarquia das Necessidades Humanas, de Abraham Maslow, com a finalidade de"),
    "alternativas": AL(2, "(A) desmentir a ideia de que a necessidade", "prescinde de autoafirmação."),
    "explicacao": "<p>O texto usa Maslow para sustentar que “motivação é o resultado dos estímulos que agem sobre as pessoas levando-as à ação”: o ser humano precisa de estímulos que o motivem a agir. Alternativa <strong>B</strong>.</p><p>O texto não desmente nada sobre aceitação (A). Ele destaca as diferenças entre as pessoas, não uma universalidade (C). Não contesta a motivação no trabalho (D). E diz que o ser humano <em>precisa</em> ser reconhecido, o contrário de “prescindir” de autoafirmação (E).</p>"},
2: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": MULTI + ["tirinha", "Dilbert"],
    "enunciado": p("Leia a tirinha que mostra o diálogo do personagem Dilbert (de óculos, sentado ao computador) com o seu chefe.") + "[[fig:1]]" + url("https://tinyurl.com/y95p2e6a", "07.11.2017")
                 + p("Na última quadrícula, o chefe menciona “habilidades de comunicação” (<em>communication skills</em>) com a intenção de"),
    "imagens": figs(("q02", "Tirinha do Dilbert em três quadros. 1) O chefe: “I signed you up for a class to try and get rid of that thing you have.” Dilbert: “What thing?” 2) Chefe: “The thing. You know. The thing that makes you the way you are.” Dilbert: “My personality?” 3) Chefe: “Exactly. But we call it communication skills because it sounds less rude.” (Inscrevi você num curso para tentar se livrar daquela coisa que você tem. — Que coisa? — A coisa que faz você ser do jeito que é. — Minha personalidade? — Exatamente. Mas chamamos de habilidades de comunicação porque soa menos grosseiro.)")),
    "alternativas": AL(2, "(A) mascarar o desejo de que Dilbert", "do questionamento e da comunicação."),
    "explicacao": "<p>O chefe admite que quer que Dilbert se livre da própria personalidade, mas chama o curso de “habilidades de comunicação” porque “soa menos grosseiro”: o nome serve para <strong>mascarar</strong> a intenção real. Alternativa <strong>A</strong>.</p><p>Ele não quer afirmar a individualidade de Dilbert (B), não fala em timidez (C), não busca melhorar as relações (D) nem incentivar o questionamento (E).</p>"},
3: {"materia": "Matemática", "assunto": "Operações e problemas", "tags": MULTI + ["média", "notação científica", "desigualdade"],
    "enunciado": DESIG + P3,
    "alternativas": alts("1,567", "1,623", "1,736", "1,892", "1,904"),
    "explicacao": "<p>O 1% mais rico tem metade da riqueza: 125 trilhões de dólares. Esse 1% são 1% de 7,2 bilhões = 72 milhões de pessoas. Média: 125 × 10¹² ÷ 72 × 10⁶ ≈ 1,736 × 10⁶ dólares = <strong>1,736 milhão</strong>. Alternativa <strong>C</strong>.</p><p>O ponto-chave é ler que o 1% tem “a mesma riqueza que os outros 99%”, isto é, metade do total.</p>"},
4: {"materia": "Matemática", "assunto": "Operações e problemas", "tags": MULTI + ["média", "desigualdade"],
    "enunciado": p("A média da riqueza, por pessoa, entre os que fazem parte da metade mais pobre da população mundial é, em dólares, igual a"), "apoio_de": (3, P3),
    "alternativas": alts("111", "113", "115", "117", "119"),
    "explicacao": "<p>A metade mais pobre tem a mesma riqueza que as oito pessoas mais ricas: 428,4 bilhões de dólares, divididos entre 3,6 bilhões de pessoas. 428,4 ÷ 3,6 = <strong>119 dólares</strong>. Alternativa <strong>E</strong>.</p>"},
5: {"materia": "Geografia", "assunto": "População", "tags": MULTI + ["gráficos", "juventude e trabalho"],
    "enunciado": p("Recentemente têm sido observadas grandes transformações no panorama da educação e do mercado de trabalho, afetando principalmente os jovens. Considere os gráficos.") + "[[fig:1]][[fig:2]]"
                 + url("https://tinyurl.com/y9pl9z2j", "06.11.2017")
                 + p("* não foi realizada a PNAD. Os números foram obtidos a partir de média simples dos valores entre os anos anterior e posterior.", classe="fonte")
                 + apoio("<strong>PEA:</strong> População Economicamente Ativa<br><strong>Estuda e PEA:</strong> jovens que estudam e trabalham<br><strong>Só PEA:</strong> jovens que só trabalham<br><strong>Nem-nem:</strong> jovens que não estudam nem trabalham")
                 + p("A partir da leitura dos gráficos, é possível concluir que"),
    "imagens": figs(("q05a", "Gráfico 1 — Renda média dos adultos e taxa de atividade dos jovens, Brasil (1992–2012). A renda dos adultos (linha preta, eixo de R$ 200 a R$ 380) sobe de cerca de R$ 210 em 1992 para R$ 305 em 1996–1998, cai para cerca de R$ 283 em 1999–2002 e R$ 263 em 2003, e depois sobe sem parar até cerca de R$ 365 em 2012. A taxa de atividade dos jovens (PEA – Jovens, linha cinza, eixo de 58% a 68%) cai de 67% em 1992 para 62,5% em 1996, oscila perto de 63% até 2004, sobe a 65,4% em 2005 e depois cai até cerca de 59% em 2011–2012."),
                    ("q05b", "Gráfico 2 — Distribuição de jovens de 15 a 24 anos por situação de atividade e estudo, Brasil (1992–2012). Só PEA cai de 49% em 1992 para cerca de 38% em 1999–2003, sobe a 41% em 2005 e fica perto de 40% até 2012. Só Estuda sobe de 16% para cerca de 24% em 2000–2003 e depois para 27% em 2011–2012. Estuda e PEA sobe de 18% para 25% em 1999 e cai a cerca de 19–20% em 2011–2012. Nem-nem fica entre 12% e 16%, com leve alta no fim do período (14% em 2012).")),
    "alternativas": AL(5, "(A) no período 1995–2006, houve aumento", "quanto dos jovens que só trabalham."),
    "explicacao": "<p>De 2009 a 2012, a renda dos adultos sobe (de cerca de R$ 330 para R$ 365) e a taxa de atividade dos jovens cai (de cerca de 63% para 59%). No mesmo período, a fatia dos que só estudam sobe de cerca de 25% para 27%. Alternativa <strong>C</strong>.</p><p>De 1995 a 2006 a taxa de atividade dos jovens não aumentou (A). De 2002 a 2003 a renda caiu, não ficou estagnada (B). De 1992 a 1995 os nem-nem diminuíram e os que só estudam aumentaram (D). De 1995 a 1998 a renda subiu e a atividade dos jovens caiu (E).</p>"},
6: {"materia": "Química", "assunto": "Funções orgânicas", "tags": MULTI + ["aminoácidos", "biometria"],
    "enunciado": apoio(*T(5, "Nos últimos anos, a leitura biométrica", "formando um produto colorido.", ["As impressões digitais são", "Há vários reagentes"])) + url("http://tinyurl.com/y99dvkto", "13.11.2017")
                 + p("A equação química simplificada que representa a reação que ocorre entre a ninidrina e uma das moléculas presentes no suor (apresentada na equação como composto X) é") + "[[fig:1]]"
                 + p("O composto X que reage com a ninidrina apresenta as funções orgânicas"),
    "imagens": figs(("q06", "Equação: 2 ninidrina + composto X → produto cor púrpura. A ninidrina é um anel benzênico fundido a um anel de cinco carbonos com dois C=O e um carbono com dois OH. O composto X é R–CH(NH₂)–COOH: um carbono ligado a H, a um grupo R, a um NH₂ e a um C(=O)OH. O produto é formado por duas unidades da ninidrina ligadas por N.")),
    "alternativas": alts("amida e álcool.", "amina e cetona.", "amina e aldeído.", "amida e ácido carboxílico.", "amina e ácido carboxílico."),
    "explicacao": "<p>O composto X, R–CH(NH₂)–COOH, é um aminoácido: tem o grupo NH₂ (<strong>amina</strong>) e o grupo COOH (<strong>ácido carboxílico</strong>). Alternativa <strong>E</strong>.</p><p>Não há N ligado a C=O, que seria amida (A e D). O OH está no grupo COOH, não é álcool (A). E o C=O pertence ao ácido carboxílico, não a cetona ou aldeído (B e C).</p>"},
7: {"materia": "História", "assunto": "História contemporânea", "tags": MULTI + ["sociedade de massas", "Segunda Revolução Industrial"],
    "enunciado": p(" ".join(T(6, "Segundo o sociólogo e filósofo alemão Herbert Marcuse", "automóveis e eletroeletrônicos.")), "Podemos afirmar corretamente que a sociedade de massas surgiu"),
    "alternativas": AL(6, "(A) no início do século XX, quando a Segunda", "surgimento da classe operária."),
    "explicacao": "<p>A sociedade de massas nasceu com a <strong>Segunda Revolução Industrial</strong> (fim do século XIX e início do XX): produção em série, urbanização acelerada e grandes mercados consumidores na Europa e nos EUA. Alternativa <strong>A</strong>.</p><p>O Iluminismo é do século XVIII e não criou consumo de massa (B). O Humanismo é renascentista (C). A Grécia antiga não estendeu direitos a todos (D). E a classe operária surge com a industrialização, não no fim da Idade Média (E).</p>"},
8: {"materia": "Biologia", "assunto": "Ecologia", "tags": MULTI + ["relações ecológicas", "sociedade"],
    "enunciado": apoio(" ".join(T(6, "A análise dos padrões genéticos e ecológicos", "capacidade de trabalhar coletivamente.")).replace("Homo sapiens", "<em>Homo sapiens</em>"))
                 + p("A predominância do trabalho individual sobre o coletivo nas espécies que perderam a capacidade de trabalhar coletivamente é, necessariamente, explicada por alterações nas relações ecológicas do tipo"),
    "alternativas": alts("intraespecífica desarmônica.", "intraespecífica harmônica.", "interespecífica neutra.", "interespecífica harmônica.", "interespecífica desarmônica."),
    "explicacao": "<p>O trabalho coletivo de formigas, abelhas e cupins é uma <strong>sociedade</strong>: relação entre indivíduos da mesma espécie (intraespecífica) com benefício mútuo (harmônica). Se a espécie perdeu esse trabalho coletivo, mudou essa relação. Alternativa <strong>B</strong>.</p><p>As relações interespecíficas envolvem espécies diferentes (C, D e E). E a sociedade não é uma relação desarmônica (A).</p>"},
9: {"materia": "Física", "assunto": "Energia", "tags": MULTI + ["notação científica", "mobilidade urbana"],
    "enunciado": apoio(" ".join(T(6, "No relatório comparativo 2003–2014", "(automóveis e motos)."))) + fonte("Fonte dos dados: http://files.antp.org.br/2016/9/3/sistemasinformacao-mobilidade--comparativo-2003_2014.pdf. Acesso em: 10.11.2017.")
                 + p("É correto afirmar que a diferença entre a energia consumida pelo transporte coletivo e o transporte individual, em 2014, em GWh, foi, aproximadamente, de")
                 + apoio("Considere<br><strong>tep</strong> = <strong>t</strong>onelada <strong>e</strong>quivalente de <strong>p</strong>etróleo<br>1 tep = 1,2 × 10<sup>7</sup> Wh"),
    "alternativas": alts("8,4 × 10<sup>3</sup>", "8,4 × 10<sup>5</sup>", "8,4 × 10<sup>7</sup>", "8,4 × 10<sup>9</sup>", "8,4 × 10<sup>11</sup>"),
    "explicacao": "<p>Diferença: 10,3 − 3,3 = 7 Gtep = 7 × 10⁹ tep. Em Wh: 7 × 10⁹ × 1,2 × 10⁷ = 8,4 × 10¹⁶ Wh. Como 1 GWh = 10⁹ Wh: 8,4 × 10¹⁶ ÷ 10⁹ = <strong>8,4 × 10⁷ GWh</strong>. Alternativa <strong>C</strong>.</p><p>Esquecer de converter para GWh leva a 8,4 × 10¹⁶, e esquecer o “giga” de Gtep leva a 8,4 × 10⁻² GWh.</p>"},
10: {"materia": "Raciocínio lógico", "assunto": "Operações e problemas", "tags": ["equilíbrio", "balança"],
     "enunciado": p("A <strong>Figura 1</strong> representa uma balança cujos pratos estão nivelados. Nos pratos dessa balança estão cubos congruentes entre si, representados por quadrados, e esferas congruentes entre si, representadas por círculos.") + "[[fig:1]]"
                  + p("A <strong>Figura 2</strong> apresenta a mesma balança, porém há desnível entre os pratos. Nos pratos estão cubos e esferas idênticos aos da <strong>Figura 1</strong>.") + "[[fig:2]]"
                  + p("Para que os pratos da balança da <strong>Figura 2</strong> fiquem no mesmo nível, basta"),
     "imagens": figs(("q10a", "Figura 1, pratos nivelados. Prato A: 3 cubos e 9 esferas. Prato B: 5 cubos e 3 esferas."),
                     ("q10b", "Figura 2, prato B mais baixo. Prato A: 4 cubos e 3 esferas. Prato B: 7 cubos.")),
     "alternativas": AL(7, "(A) retirar duas esferas do prato A.", "(E) colocar dois cubos no prato B."),
     "explicacao": "<p>Na Figura 1: 3 cubos + 9 esferas = 5 cubos + 3 esferas, então 6 esferas = 2 cubos, ou <strong>1 cubo = 3 esferas</strong>.</p><p>Na Figura 2, em esferas: prato A = 4 · 3 + 3 = 15; prato B = 7 · 3 = 21. Tirando dois cubos de B, ele fica com 5 cubos = 15 esferas, igual a A. Alternativa <strong>B</strong>.</p><p>As outras deixam os pratos em 13 × 21 (A), 18 × 21 (C), 18 × 21 (D) e 15 × 27 (E).</p>"},
11: {"materia": "Raciocínio lógico", "assunto": "Raciocínio espacial", "tags": ["áreas", "quadrados"],
     "enunciado": p("O retângulo ABCD da figura foi decomposto em seis quadrados.") + "[[fig:1]]"
                  + p("Sabendo que o quadrado EFGH tem área igual a 1 cm<sup>2</sup>, então a área do retângulo ABCD é, em centímetros quadrados,"),
     "imagens": figs(("q11", "Retângulo ABCD dividido em seis quadrados: um grande à direita, ocupando toda a altura; à esquerda, um quadrado médio em cima e, embaixo dele, um quadrado menor encostado no grande; no canto inferior esquerdo, um quadrado ainda menor e, acima dele, dois quadradinhos lado a lado, um deles EFGH, com E e H no lado AD.")),
     "alternativas": alts("64.", "89.", "104.", "111.", "205."),
     "explicacao": "<p>Os dois quadradinhos têm lado 1. Embaixo deles, o quadrado do canto tem lado 1 + 1 = 2. Ao lado, o quadrado seguinte tem lado 1 + 2 = 3. Acima de tudo isso, o quadrado médio tem lado 2 + 3 = 5. O grande, que ocupa toda a altura, tem lado 3 + 5 = 8.</p><p>O retângulo mede 5 + 8 = 13 por 8: área = <strong>104 cm²</strong>. Alternativa <strong>C</strong>. Os lados seguem a sequência de Fibonacci: 1, 1, 2, 3, 5, 8.</p>"},
12: {"materia": "Raciocínio lógico", "assunto": "Operações e problemas", "tags": ["dedução", "tabelas"],
     "enunciado": p("Cada número inteiro de 2 a 9 foi representado por uma letra de A a H, não necessariamente nessa ordem e sem repetição, e essas letras foram dispostas em uma tabela da seguinte forma:")
                  + tabela(["", "E", "F", "G", "H"], [["<strong>A</strong>", "", "", "", "18"], ["<strong>B</strong>", "", "20", "", ""], ["<strong>C</strong>", "", "", "42", ""], ["<strong>D</strong>", "", "", "", ""]])
                  + p("Na tabela, cada número escrito é o produto do valor da letra de sua linha pelo valor da letra de sua coluna. Por exemplo, o produto de A por H é igual a 18.", "Nessas condições, o produto de D por E é igual a"),
     "alternativas": alts("15.", "18.", "21.", "24.", "26."),
     "explicacao": "<p>Com números de 2 a 9, sem repetir: 42 só pode ser 6 × 7, e 20 só pode ser 4 × 5. Então 18 não pode ser 3 × 6 (o 6 já foi usado): é 2 × 9. Sobram 3 e 8 para D e E, e D × E = <strong>24</strong>. Alternativa <strong>D</strong>.</p>"},
13: {"materia": "Raciocínio lógico", "assunto": "Análise combinatória", "tags": ["princípio multiplicativo"],
     "enunciado": apoio("João vai criar uma senha para o seu roteador. Para ter mais segurança,<br>• a senha terá nove caracteres que não se repetem, sendo 4 algarismos, 3 letras e 2 caracteres não alfanuméricos;<br>• a senha ou começará ou terminará por um caractere não alfanumérico;<br>• as três letras serão seguidas por um único caractere não alfanumérico seguido por quatro algarismos;<br>• há distinção entre letra maiúscula e letra minúscula;<br>• as letras serão escolhidas entre <strong>a</strong>, <strong>i</strong>, <strong>p</strong>, <strong>g</strong>, <strong>k</strong> e <strong>v</strong>, apenas;<br>• os caracteres não alfanuméricos serão escolhidos entre <strong>!</strong>, <strong>%</strong>, <strong>&amp;</strong> e <strong>&gt;</strong>, apenas.",
                        "Observe dois exemplos de senhas nas condições dadas:<br><strong>!pGk&amp;8460</strong> ou <strong>AiV%3841&gt;</strong>")
                  + p("Assim sendo, a quantidade de senhas distintas que João pode formar é"),
     "alternativas": alts("12<sup>3</sup> · 10<sup>4</sup> · 4<sup>2</sup>", "12<sup>2</sup> · 11 · 10<sup>2</sup> · 9 · 8 · 7 · 2", "12<sup>2</sup> · 11 · 10<sup>2</sup> · 9 · 8 · 7 · 3", "12<sup>2</sup> · 11 · 10 · 9 · 8 · 7 · 4", "12<sup>2</sup> · 11 · 10 · 9 · 8 · 7 · 2"),
     "explicacao": "<p>O bloco “3 letras + símbolo + 4 algarismos” fica fixo, e o outro símbolo vai no começo ou no fim: <strong>2</strong> posições.</p><p>Letras: 6 letras × 2 (maiúscula/minúscula) = 12 opções, sem repetir: 12 · 11 · 10. Algarismos: 10 · 9 · 8 · 7. Símbolos: 4 · 3 = 12.</p><p>Total: 2 · 12 · 11 · 10 · 10 · 9 · 8 · 7 · 12 = 12² · 11 · 10² · 9 · 8 · 7 · 2. Alternativa <strong>B</strong>.</p><p>A ignora que os caracteres não se repetem. C, D e E erram o número de posições ou perdem um fator 10.</p>"},
14: {"materia": "Raciocínio lógico", "assunto": "Lógica", "tags": ["princípio da casa dos pombos"],
     "enunciado": p(" ".join(T(8, "Todos os vinte e três livros de uma coleção", "pelo menos, dois livros.")), "Nessas condições, conclui-se necessariamente que"),
     "alternativas": AL(8, "(A) nenhum aluno receberá quatro livros.", "a mesma quantidade de livros."),
     "explicacao": "<p>Se ninguém recebesse 4 ou mais livros, cada aluno teria no máximo 3, e os seis juntos teriam no máximo 18 — menos que 23. Então <strong>algum aluno recebe pelo menos quatro</strong>. Alternativa <strong>B</strong>.</p><p>As outras não são obrigatórias: por exemplo, 2 + 2 + 2 + 2 + 2 + 13 = 23 contraria A, C, D e E.</p>"},
15: {"materia": "História", "assunto": "História contemporânea", "tags": ["Era Napoleônica", "Código Civil"],
     "enunciado": p(" ".join(T(9, "Ao assumir o poder na França", "a maior potência do mundo.")), "Conhecido como Era Napoleônica, o período em que Napoleão Bonaparte governou a França ficou marcado"),
     "alternativas": AL(9, "(A) pela promulgação de um novo Código Civil", "todos os países do continente."),
     "explicacao": "<p>O <strong>Código Civil napoleônico</strong> (1804) consolidou conquistas da Revolução: igualdade perante a lei, fim dos privilégios feudais, casamento civil e divórcio, Estado laico. Alternativa <strong>A</strong>.</p><p>Napoleão viveu em guerra com a Inglaterra, e o Tratado de Versalhes é de 1919 (B). Não houve imigração das colônias (C) nem guerra contra os EUA, que até compraram dele a Louisiana (D). A União Europeia é do século XX (E).</p>"},
16: {"materia": "História", "assunto": "Antiguidade", "tags": ["Grécia antiga", "religião"],
     "enunciado": p(" ".join(T(9, "Ernst Gombrich, historiador de arte", "imponentes construções.")), "Essa característica da arquitetura reflete um aspecto importante da religião grega, já que"),
     "alternativas": AL(9, "(A) os deuses gregos eram considerados infalíveis", "os materiais usados na construção."),
     "explicacao": "<p>Os deuses gregos eram <strong>antropomórficos</strong>: imortais, mas com paixões e defeitos humanos, como ciúme, vingança e egoísmo. Templos em escala humana combinam com deuses próximos dos homens. Alternativa <strong>D</strong>.</p><p>Os deuses não eram infalíveis (A). Os quatro elementos são uma ideia de filósofos, não a religião (B). E C e E não têm base na tradição grega.</p>"},
17: {"materia": "História", "assunto": "Idade Moderna", "tags": ["Reforma Protestante", "imprensa"],
     "enunciado": p("Leia o texto.") + apoio(" ".join(T(9, "A Reforma Protestante jamais teria ocorrido", "aos fiéis”, comentou."))) + url("https://tinyurl.com/yatbezyk", "02.11.2017", "")
                  + p("Historicamente, a relação que o texto estabelece entre Martinho Lutero e a imprensa de Gutenberg se evidencia, principalmente, na"),
     "alternativas": alts("edição de material filosófico crítico à fé cristã.", "criação do primeiro jornal evangélico diário.", "publicação de novelas religiosas populares.", "divulgação de produtos e serviços bíblicos.", "impressão da Bíblia em alemão."),
     "explicacao": "<p>Lutero defendia a leitura direta da Bíblia pelos fiéis e a traduziu para o <strong>alemão</strong>; a imprensa permitiu imprimi-la em grande quantidade. Alternativa <strong>E</strong>.</p><p>Lutero não criticava a fé cristã (A), não criou jornal (B) nem novelas (C), e combatia justamente a venda de indulgências (D).</p>"},
18: {"materia": "História", "assunto": "Entreguerras", "tags": ["nazismo", "crise de 1929"],
     "enunciado": p("Observe a tabela.", "<strong>Crescimento do Partido Nazista – Alemanha 1925-1932</strong>")
                  + tabela(["Ano", "Nº de filiados"], [["1925", "27 717"], ["1926", "49 523"], ["1927", "72 590"], ["1928", "108 717"], ["1929", "176 426"], ["1930", "389 000"], ["1931", "806 294"], ["1932", "1 414 975"]])
                  + fonte("Fonte dos dados: MARTIN, P.M. <em>et alii</em>. <em>Geografía y Historia</em>. Zaragoza: Edelvives, 1995. V.4, p.82.")
                  + p("A tabela mostra o crescimento do número de filiados ao Partido Nazista Alemão entre as décadas de 1920 e 1930.", "Assinale a alternativa que associa, corretamente, o crescimento do número de filiados e o contexto internacional."),
     "alternativas": AL(10, "(A) O número de filiados ao Partido Nazista no ano de 1932", "o número de filiados ao partido."),
     "explicacao": "<p>A crise de 1929 derrubou a economia alemã, que dependia de empréstimos americanos: desemprego em massa e descrédito da República de Weimar. Os filiados mais que dobraram de 1929 para 1930. Alternativa <strong>B</strong>.</p><p>O pacto entre Hitler e Stálin é de 1939, e o nazismo era anticomunista (A). O nazismo não era pacifista, e os alemães rejeitavam o Tratado de Versalhes (C). Não houve queda em 1927 (D). E a prosperidade não explica um partido de crise (E).</p>"},
19: {"materia": "História", "assunto": "Brasil Colônia", "tags": ["Inconfidência Mineira"],
     "enunciado": p(" ".join(T(10, "Na década de 1780, na capitania de Minas Gerais", "Brasil colônia.")), "Conhecido como Inconfidência Mineira, esse movimento foi provocado principalmente"),
     "alternativas": AL(10, "(A) pela política de incentivo ao desenvolvimento", "da escravidão no território nacional."),
     "explicacao": "<p>A Inconfidência reagiu ao <strong>quinto</strong> (imposto de 20% sobre o ouro) e à ameaça da <strong>derrama</strong>, ao alvará que proibia manufaturas na colônia (1785) e foi inspirada pelo Iluminismo e pela independência dos EUA. Alternativa <strong>D</strong>.</p><p>A Lei de Terras e o fim do tráfico são do século XIX (A). A presença holandesa é do século XVII (B). A família real chegou em 1808 (C). E não havia universidades na colônia nem abolição (E).</p>"},
20: {"materia": "Química", "assunto": "Substâncias e misturas", "tags": ["separação de misturas"],
     "enunciado": SACHE + P20,
     "alternativas": alts("destilação e filtração.", "decantação e filtração.", "decantação e levigação.", "centrifugação e filtração.", "centrifugação e destilação."),
     "explicacao": "<p>O sulfato de cálcio “vai ao fundo do recipiente juntamente com a sujeira”: <strong>decantação</strong>. Depois a água passa por um pano: <strong>filtração</strong>. Alternativa <strong>B</strong>.</p><p>Não há aquecimento e condensação (destilação), corrente de água para arrastar sólidos leves (levigação) nem rotação (centrifugação).</p>"},
21: {"materia": "Química", "assunto": "Funções inorgânicas", "tags": ["sais", "fórmulas"],
     "enunciado": p("Assinale a alternativa que contém a fórmula correta do sulfato de cálcio"), "apoio_de": (20, P20),
     "alternativas": alts("Ca(SO<sub>4</sub>)<sub>2</sub>", "Ca<sub>3</sub>(SO<sub>4</sub>)<sub>2</sub>", "CaSO<sub>4</sub>", "Ca<sub>2</sub>SO<sub>4</sub>", "Ca<sub>4</sub>SO"),
     "explicacao": "<p>Ca²⁺ e SO₄²⁻ têm cargas de mesmo valor, então se combinam 1 para 1: <strong>CaSO₄</strong>. Alternativa <strong>C</strong>.</p>"},
22: {"materia": "Química", "assunto": "Reações químicas", "tags": ["número de oxidação"],
     "enunciado": p("Os números de oxidação do enxofre e do cloro nos íons SO<sub>4</sub><sup>2–</sup> e C<em>ℓ</em>O<sup>1–</sup> são, respectivamente,"), "apoio_de": (20, P20),
     "alternativas": alts("1+ e 2–", "4+ e 1–", "5+ e 0", "6+ e 1+", "8+ e 2+"),
     "explicacao": "<p>O oxigênio vale −2. No SO₄²⁻: S + 4(−2) = −2, então S = <strong>+6</strong>. No ClO⁻: Cl + (−2) = −1, então Cl = <strong>+1</strong>. Alternativa <strong>D</strong>.</p>"},
23: {"materia": "Química", "assunto": "Propriedades da matéria", "tags": ["volatilidade", "pressão de vapor"],
     "enunciado": CARRO + P23,
     "alternativas": alts("alta resistência ao calor.", "alta pressão de vapor.", "alta condutividade elétrica.", "elevada condutividade térmica.", "elevada maleabilidade."),
     "explicacao": "<p>Os COVs evaporam sem precisar de altas temperaturas: são <strong>voláteis</strong>, e substância volátil tem <strong>alta pressão de vapor</strong>. Alternativa <strong>B</strong>.</p><p>As outras propriedades não têm relação com evaporar e espalhar cheiro; condutividade e maleabilidade são típicas de metais.</p>"},
24: {"materia": "Química", "assunto": "Termoquímica", "tags": ["entalpia de formação", "lei de Hess"],
     "enunciado": p("O benzeno sofre reação de combustão segundo a equação balanceada") + apoio("\\[\\text{C}_6\\text{H}_6(\\ell) + \\tfrac{15}{2}\\,\\text{O}_2(\\text{g}) \\rightarrow 6\\,\\text{CO}_2(\\text{g}) + 3\\,\\text{H}_2\\text{O}(\\ell)\\]")
                  + p("A entalpia de combustão do benzeno pode ser determinada conhecendo-se os valores das entalpias de formação do gás carbônico, assim como da água e do benzeno líquidos.", "A tabela apresenta os valores de entalpia de formação de algumas substâncias nas condições padrão.")
                  + tabela(["Substância", "Entalpia de formação (kJ/mol)"], [["C<sub>6</sub>H<sub>6</sub> (<em>ℓ</em>)", "+ 50"], ["CO<sub>2</sub> (g)", "– 394"], ["H<sub>2</sub>O (<em>ℓ</em>)", "– 286"]])
                  + p("A entalpia de combustão completa do benzeno, em kJ/mol, é"),
     "apoio_de": (23, P23),
     "alternativas": alts("– 3 272", "– 3 172", "– 2 122", "+ 2 364", "+ 3 272"),
     "explicacao": "<p>ΔH = Σ produtos − Σ reagentes = [6(−394) + 3(−286)] − [50 + 0] = −2 364 − 858 − 50 = <strong>−3 272 kJ/mol</strong>. Alternativa <strong>A</strong>.</p><p>O O₂ é substância simples e tem entalpia de formação zero. Somar o +50 em vez de subtrair dá −3 172 (B). E combustão libera calor, por isso ΔH é negativo (D e E).</p>"},
25: {"materia": "Inglês", "assunto": "Interpretação de texto",
     "enunciado": FAKE + P25,
     "alternativas": alts("O termo <em>fake news</em> se aplica aos <em>websites</em> que difundem notícias falsas.", "A existência de <em>fake news</em> contribuiu para o desenvolvimento do universo digital.", "As eleições americanas foram as responsáveis pelo início da divulgação de <em>fake news</em>.",
                          "O termo <em>fake news</em> é usado para designar toda informação que se baseia em fatos reais.", "O resultado das eleições americanas foi, inegavelmente, uma consequência de <em>fake news</em>."),
     "explicacao": "<p>O texto abre com a definição: “<em>Fake news – websites disseminating news stories that are false</em>”. Alternativa <strong>A</strong>.</p><p>O texto diz que as <em>fake news</em> afetam o universo digital, não que o desenvolveram (B). As eleições não marcam o início delas (C). Elas são falsas, não baseadas em fatos (D). E “<em>there is no way to definitively ascertain its effect on voting</em>” — o efeito na eleição não pode ser comprovado (E).</p>"},
26: {"materia": "Inglês", "assunto": "Interpretação de texto",
     "enunciado": p("Assinale a alternativa que apresenta, de acordo com o texto, elementos que podem ser considerados razões para a disseminação ou o aumento de <em>fake news</em>."), "apoio_de": (25, P25),
     "alternativas": {k: v.replace("social media", "<em>social media</em>").replace("fake news", "<em>fake news</em>").replace("websites", "<em>websites</em>") for k, v in AL(12, "(A) A recusa em aceitar comentários negativos", "reproduzidas repetidamente.").items()},
     "explicacao": "<p>O texto diz: “<em>It is disseminated on social media platforms just because dissemination of information without vetting has always been a feature of those platforms. This was designed to facilitate communication</em>”. Alternativa <strong>B</strong>.</p><p>Ninguém recusa comentários negativos; ao contrário, “<em>no one removes a negative comment</em>” (A). O Facebook não é a única plataforma (C). Os sites convencem “<em>many people</em>”, não todos (D). E E não aparece no texto.</p>"},
27: {"materia": "Inglês", "assunto": "Interpretação de texto",
     "enunciado": p("A respeito do papel do Facebook na disseminação de <em>fake news</em>, pode-se afirmar corretamente, tendo por base o texto apresentado, que"), "apoio_de": (25, P25),
     "alternativas": {k: v.replace("fake news", "<em>fake news</em>") for k, v in AL(12, "(A) o Facebook, apesar de possibilitar", "a política de liberdade de expressão do site.").items()},
     "explicacao": "<p>O texto diz que o Facebook “<em>is by far the largest</em>” hospedeiro involuntário de <em>fake news</em>, com cerca de 2 bilhões de usuários por mês, e liga isso à liberdade de postar (“<em>the freedom to post</em>”). Alternativa <strong>E</strong>.</p><p>O Facebook serviu, sim, como meio de divulgação (A). Não houve diminuição de usuários (B) nem censura explícita, e sim detecção automática e mudança nos anúncios (C). E o texto não fala em gosto por tragédias (D).</p>"},
}

Q.update({
28: {"materia": "Inglês", "assunto": "Interpretação de texto",
     "enunciado": p("Ainda sobre o Facebook, pode-se afirmar corretamente, com base nos argumentos expostos no texto, que os impactos de <em>fake news</em>"), "apoio_de": (25, P25),
     "alternativas": {k: v.replace("fake news", "<em>fake news</em>") for k, v in AL(13, "(A) afetam positivamente a companhia, promovendo", "confiável para as marcas do que era antes.").items()},
     "explicacao": "<p>O texto diz: “<em>the fallout from fake news during the election cycle may cause advertisers to pull back from Facebook, as it is less ‘brand safe’ than formerly</em>”. Alternativa <strong>E</strong>.</p><p>Os impactos são negativos, não positivos (A e B). O Facebook só anunciou ferramentas depois da eleição (C). E o texto diz “<em>may cause</em>” (pode causar) e chama o Facebook de hospedeiro involuntário, não de agente essencial na criação (D).</p>"},
29: {"materia": "Inglês", "assunto": "Formação de palavras", "tags": ["prefixos"],
     "enunciado": p("A palavra <strong><em>un</em></strong><em>checked</em>, presente no quarto parágrafo, é formada por meio da adição do prefixo <strong><em>un-</em></strong> ao termo <em>checked</em>.",
                    "A alternativa que apresenta uma palavra gramaticalmente correta e formada pelo processo de prefixação, tal como <strong><em>un</em></strong><em>checked</em>, é"),
     "apoio_de": (25, P25),
     "alternativas": alts("<strong><em>ir</em></strong><em>real.</em>", "<strong><em>un</em></strong><em>polite.</em>", "<strong><em>in</em></strong><em>certain.</em>", "<strong><em>under</em></strong><em>cook.</em>", "<strong><em>des</em></strong><em>motivated.</em>"),
     "explicacao": "<p><em>Undercook</em> (cozinhar pouco) existe em inglês e é formado pelo prefixo <em>under-</em>. Alternativa <strong>D</strong>.</p><p>As formas corretas seriam <em>unreal</em> (A), <em>impolite</em> (B), <em>uncertain</em> (C) e <em>demotivated</em> (E).</p>"},
30: {"materia": "Matemática", "assunto": "Probabilidade", "tags": ["gráficos", "probabilidade condicional"],
     "enunciado": p("Leia o gráfico.") + "[[fig:1]]" + fonte("Fonte dos dados: &lt;https://tinyurl.com/y8bbbchy&gt; Acesso em: 31.10.2017.")
                  + apoio("Adote:<br>• População negra no Brasil em 2016: 54%;<br>• População branca no Brasil em 2016: 46%.")
                  + p("Com base no gráfico e nos dados apresentados, escolhido um brasileiro assalariado ao acaso, a probabilidade de ele ser negro e estar nas faixas salariais 0 a 0,5 salário mínimo ou 0,5 a 1 salário mínimo é igual a"),
     "imagens": figs(("q30", "Gráfico de colunas “Distribuição de negros e brancos por faixa salarial (em salários mínimos) – Brasil (2016)”, em % de cada grupo. 0 a 0,5: brancos 6%, negros 15%. 0,5 a 1: brancos 8%, negros 12%. 1 a 1,5: brancos 31%, negros 40%. 1,5 a 2: brancos 14%, negros 11%. 2 a 5: brancos 29%, negros 18%. 5 a 10: brancos 8%, negros 3%. Mais que 10: brancos 4%, negros 1%.")),
     "alternativas": alts("11,25%", "12,46%", "13,72%", "14,58%", "15,94%"),
     "explicacao": "<p>Entre os negros, 15% + 12% = 27% estão nas duas faixas. Como os negros são 54% da população: 0,54 × 0,27 = 0,1458 = <strong>14,58%</strong>. Alternativa <strong>D</strong>.</p><p>Os percentuais do gráfico são dentro de cada grupo, por isso é preciso multiplicar pela participação dos negros na população.</p>"},
31: {"materia": "Matemática", "assunto": "Porcentagem", "tags": ["equação do 1º grau"],
     "enunciado": p(" ".join(T(14, "Os salários de um homem branco", "desse homem branco.")).replace("R$ 4.380,00", "R$ 4.380,00"), "Com base nessas informações, o salário dessa mulher e desse homem negro são, respectivamente, iguais a"),
     "alternativas": alts("R$ 1.140,00 e R$ 2.000,00", "R$ 1.240,00 e R$ 1.140,00", "R$ 1.240,00 e R$ 2.000,00", "R$ 2.000,00 e R$ 1.140,00", "R$ 2.000,00 e R$ 1.240,00"),
     "explicacao": "<p>Seja x o salário do homem branco: x + 0,62x + 0,57x = 2,19x = 4 380, então x = 2 000. Mulher: 0,62 × 2 000 = <strong>R$ 1.240,00</strong>; homem negro: 0,57 × 2 000 = <strong>R$ 1.140,00</strong>. Alternativa <strong>B</strong>.</p><p>D e E trazem o salário do homem branco, que não foi pedido.</p>"},
32: {"materia": "Matemática", "assunto": "Geometria espacial", "tags": ["semelhança", "volume"],
     "enunciado": PIRAMIDE + P32, "imagens": PIRAMIDE_IMG,
     "alternativas": alts("58%", "62%", "73%", "87%", "90%"),
     "explicacao": "<p>Em sólidos semelhantes, a razão entre os volumes é o cubo da razão de semelhança: (0,9)³ = 0,729 ≈ <strong>73%</strong>. Alternativa <strong>C</strong>.</p><p>0,9² = 81% seria a razão entre áreas, e 90% a razão entre alturas (E).</p>"},
33: {"materia": "Matemática", "assunto": "Geometria espacial", "tags": ["pirâmide", "área lateral", "semelhança"],
     "enunciado": p("Para destacar a diferença entre os mais ricos e os mais pobres, o artista pintará toda a área lateral da obra com tons diferentes de tinta, um mais escuro (para os 10% mais ricos) e outro mais claro (para os 90% mais pobres), como no gráfico. O custo da tinta mais escura é de R$ 20,00 por metro quadrado, e o custo da tinta mais clara é de R$ 10,00 por metro quadrado.",
                    "O custo total para pintar essa obra será, em reais, igual a") + apoio("A base da pirâmide e as linhas divisórias <strong>não</strong> serão pintadas."),
     "apoio_de": (32, P32),
     "alternativas": alts("895,00", "914,00", "1.086,00", "1.148,00", "1.256,00"),
     "explicacao": "<p>O apótema de cada face é √(4² + 3²) = 5 m. Área lateral: 4 × (6 × 5 ÷ 2) = 60 m².</p><p>A parte escura é uma pirâmide semelhante com razão 0,9: sua área lateral é 0,9² × 60 = 48,6 m². A parte clara é o resto: 60 − 48,6 = 11,4 m².</p><p>Custo: 48,6 × 20 + 11,4 × 10 = 972 + 114 = <strong>R$ 1.086,00</strong>. Alternativa <strong>C</strong>.</p><p>Usar a razão 0,9 direto, sem elevar ao quadrado, dá 54 × 20 + 6 × 10 = 1 140.</p>"},
34: {"materia": "Matemática", "assunto": "Geometria espacial", "tags": ["pirâmide", "área total"],
     "enunciado": p("O total de metal necessário para construir essa obra será, em metros quadrados, igual a") + apoio("Despreze a espessura das placas de metal."),
     "apoio_de": (32, P32),
     "alternativas": alts("58", "60", "72", "84", "96"),
     "explicacao": "<p>Área total = área lateral + base = 60 + 6 × 6 = <strong>96 m²</strong>. Alternativa <strong>E</strong>.</p><p>A área lateral vem dos quatro triângulos de base 6 e altura (apótema) 5: 4 × 15 = 60 (B, que esquece a base).</p>"},
35: {"materia": "Física", "assunto": "Cinemática", "tags": ["velocidade média", "conversão de unidades"],
     "enunciado": RADAR + P35, "imagens": RADAR_IMG,
     "alternativas": alts("não será multado, pois V<sub>M</sub> é menor do que a velocidade mínima permitida.", "não será multado, pois V<sub>C</sub> é menor do que a velocidade máxima permitida.", "não será multado, pois V<sub>C</sub> é menor do que a velocidade mínima permitida.",
                          "será multado, pois V<sub>M</sub> é maior do que a velocidade máxima permitida.", "será multado, pois V<sub>C</sub> é maior do que a velocidade máxima permitida."),
     "explicacao": "<p>V<sub>M</sub> = 3 m ÷ 0,20 s = 15 m/s = 15 × 3,6 = 54 km/h. Pela tabela, V<sub>M</sub> = 54 corresponde a V<sub>C</sub> = 47 km/h, abaixo do limite de 50 km/h. Alternativa <strong>B</strong>.</p><p>A multa considera V<sub>C</sub>, não V<sub>M</sub> (D). E 50 km/h é a velocidade máxima, não a mínima (A e C).</p>"},
36: {"materia": "Física", "assunto": "Óptica", "tags": ["lentes", "vergência"],
     "enunciado": p("Podemos aproximar o conjunto de lentes da câmera fotográfica representada na figura a uma única lente convergente. Considere que a distância entre essa lente e o veículo a ser fotografado seja de 25 cm, e que a distância entre essa lente e o sensor fotossensível (anteparo) na câmera seja de 5 cm.")
                  + apoio("Considere<br>\\(\\dfrac{1}{f} = \\dfrac{1}{p} + \\dfrac{1}{p'}\\)<br><em>f</em> ⇒ distância focal<br><em>p</em> ⇒ distância objeto–lente<br><em>p′</em> ⇒ distância imagem–lente")
                  + p("Assinale a alternativa que apresenta o valor aproximado da vergência, em dioptrias, dessa lente."),
     "apoio_de": (35, P35),
     "alternativas": alts("0,05", "0,20", "5", "20", "25"),
     "explicacao": "<p>Vergência é V = 1/f, com distâncias em metros. A resposta oficial é <strong>20 di</strong>, alternativa <strong>D</strong>, que corresponde a considerar só a distância da imagem: 1/0,05 = 20.</p><p>Observação: a conta completa com os dados do enunciado é 1/f = 1/0,25 + 1/0,05 = 4 + 20 = <strong>24 di</strong>, mais próxima de 25 (E) do que de 20. A resposta da banca só se justifica se o veículo for tratado como um objeto muito distante (1/p ≈ 0), o que não combina com os 25 cm informados. O gabarito oficial não foi alterado; fique atento a esse tipo de aproximação.</p>"},
37: {"materia": "Física", "assunto": "Eletromagnetismo", "tags": ["indução eletromagnética"],
     "enunciado": p(" ".join(T(15, "Ao passar pelos laços detectores", "aeroportos.")), "Nesses dispositivos, o sinal é gerado através de uma"), "apoio_de": (35, P35),
     "alternativas": AL(15, "(A) força eletromotriz induzida pela movimentação de um elemento ferro", "de um material orgânico."),
     "explicacao": "<p>O texto diz que veículos têm materiais <strong>ferromagnéticos</strong>. Ao se moverem sobre o laço, alteram o fluxo magnético e induzem uma força eletromotriz (lei de Faraday). Alternativa <strong>A</strong>.</p><p>Materiais para e diamagnéticos interagem muito fracamente com o campo (B e C). E não é qualquer material que gera o sinal (D e E).</p>"},
38: {"materia": "Física", "assunto": "Termodinâmica", "tags": ["transformações gasosas", "trabalho"],
     "enunciado": p("O gráfico apresenta o comportamento de um gás ideal em um processo cíclico que se inicia no ponto A.") + "[[fig:1]]" + p("Com base no gráfico apresentado, podemos afirmar corretamente que"),
     "imagens": figs(("q38", "Gráfico P (atm) × V (ℓ) de um ciclo retangular percorrido no sentido horário: A (2 ℓ; 3 atm) → B (6 ℓ; 3 atm) → C (6 ℓ; 1 atm) → D (2 ℓ; 1 atm) → A.")),
     "alternativas": AL(16, "(A) entre os pontos D e A ocorre transformação isocórica", "isobárica de expansão."),
     "explicacao": "<p>De B para C o volume fica em 6 ℓ: transformação <strong>isocórica</strong>, e sem variação de volume o trabalho é <strong>nulo</strong>. Alternativa <strong>B</strong>.</p><p>D → A também é isocórica, mas o trabalho é nulo, não negativo (A). C → D é isobárica com compressão, e o trabalho é negativo, não nulo (C). A → B é isobárica de expansão, não isocórica (D). E A e D não são ligados por uma isobárica (E).</p>"},
39: {"materia": "Física", "assunto": "Eletromagnetismo", "tags": ["análise dimensional", "Biot-Savart"],
     "enunciado": p(" ".join(T(16, "Os experimentos realizados pelos físicos franceses", "pode ser dada pela equação")))
                  + apoio("\\[\\Delta|\\vec{B}| = \\frac{\\mu_0}{4\\pi}\\cdot\\frac{i\\cdot\\Delta L\\cdot \\operatorname{sen}\\theta}{r^2}\\]")
                  + p("Se considerarmos que \\(\\Delta|\\vec{B}|\\) está em tesla, <em>i</em> está em ampère, Δ<em>L</em> e <em>r</em> estão em metros, e θ em radianos, podemos dizer que a unidade de medida da constante de permeabilidade magnética do vácuo (μ<sub>0</sub>) é dada em"),
     "alternativas": alts("T · A · m<sup>2</sup> · rad / m", "T · m<sup>2</sup> / A · rad · m", "T · m / A · rad", "T · m / A", "T · m · A"),
     "explicacao": "<p>Isolando μ₀: μ₀ = 4π · B · r² / (i · ΔL · sen θ). O seno de um ângulo é um número puro, sem unidade (o “rad” fica no ângulo, não no seno). Então: T · m² / (A · m) = <strong>T · m / A</strong>. Alternativa <strong>D</strong>.</p><p>B e C erram ao pôr “rad” na unidade, como se o seno a carregasse.</p>"},
40: {"materia": "Geografia", "assunto": "Biomas",
     "enunciado": CERRADO + P40,
     "alternativas": alts("Mata Atlântica.", "Caatinga.", "Floresta Amazônica.", "Pantanal.", "Cerrado."),
     "explicacao": "<p>O <strong>Cerrado</strong> é o segundo maior bioma da América do Sul, com cerca de 22% do território brasileiro, abriga nascentes de grandes bacias (alto potencial aquífero) e é, depois da Mata Atlântica, o bioma mais alterado pela ocupação humana. Alternativa <strong>E</strong>.</p><p>O maior bioma é a Amazônia (C). Caatinga e Pantanal são bem menores (B e D).</p>"},
41: {"materia": "Geografia", "assunto": "Agropecuária", "tags": ["fronteira agrícola", "soja"],
     "enunciado": p("A principal atividade econômica que ameaça o bioma citado no texto é a"), "apoio_de": (40, P40),
     "alternativas": alts("expansão da criação de gado bovino de leite.", "expansão da criação de gado ovino para lã.", "extração e processamento do pau-brasil.", "expansão do cultivo mecanizado de soja.", "expansão do cultivo extensivo de cacau."),
     "explicacao": "<p>A fronteira agrícola no Cerrado avança sobretudo com a <strong>soja mecanizada</strong>, favorecida pelo relevo plano e pela correção do solo. Alternativa <strong>D</strong>.</p><p>A pecuária no Cerrado é principalmente de corte, não de leite (A). Ovinos para lã são do Sul (B). O pau-brasil é da Mata Atlântica (C). E o cacau é da Bahia e da Amazônia (E).</p>"},
42: {"materia": "Geografia", "assunto": "Cartografia", "tags": ["projeção de Mercator"],
     "enunciado": p("Observe o planisfério.") + "[[fig:1]]" + url("https://tinyurl.com/yb57zobr", "07.11.2017", "Adaptado. Original colorido.")
                  + p(" ".join(T(17, "As projeções cartográficas são produzidas", "projeção de Mercator.")), "Sobre a referida projeção podemos afirmar corretamente que se trata de uma"),
     "imagens": figs(("q42", "Planisfério na projeção de Mercator, com meridianos de −180° a 180° e paralelos de −80° a 80°. Os paralelos ficam cada vez mais afastados em direção aos polos, e por isso a Groenlândia e a Antártida aparecem enormes.")),
     "alternativas": AL(17, "(A) projeção cilíndrica conforme", "próximo à linha do Equador."),
     "explicacao": "<p>Mercator é uma projeção <strong>cilíndrica conforme</strong>: preserva os ângulos e as formas, mas exagera as áreas perto dos polos — a Groenlândia parece do tamanho da África. Alternativa <strong>A</strong>.</p><p>Ela não é cônica (B) nem azimutal (D). Projeção que preserva áreas é a equivalente, como a de Peters (C). E a distorção de área é maior nos polos, não no Equador (E).</p>"},
43: {"materia": "Geografia", "assunto": "Geopolítica", "tags": ["Acordo de Paris", "Trump"],
     "enunciado": p("Leia os trechos de declarações de Donald Trump, presidente dos Estados Unidos.") + apoio(*T(18, "“A economia cresceu e isso", "que não precisamos”.", ["“Admito que a mudança"])) + url("https://tinyurl.com/yaeoj29p", "08.11.2017")
                  + p("Essas declarações de Donald Trump, para justificar a retirada dos Estados Unidos do acordo para reduzir emissões de gases de efeito estufa no contexto do desenvolvimento sustentável, revelam"),
     "alternativas": AL(18, "(A) a preocupação com o crescimento da economia", "de energias renováveis."),
     "explicacao": "<p>Trump prioriza os empregos e cidades americanas (“Youngstown, Detroit e Pittsburgh à frente de Paris”) e trata o combate à mudança climática como gasto desnecessário: posição <strong>isolacionista</strong>, que põe interesses econômicos locais acima dos ambientais globais. Alternativa <strong>C</strong>.</p><p>Não há reconhecimento da importância ambiental (A), nem sintonia com os europeus, que apoiavam o acordo (B). A China permaneceu no acordo (D). E Trump defendia indústrias tradicionais, não renováveis (E).</p>"},
44: {"materia": "Geografia", "assunto": "Geopolítica", "tags": ["curdos", "Oriente Médio"],
     "enunciado": p("Leia o texto.") + apoio(" ".join(T(18, "Quase 93% do grupo étnico no Iraque", "3,3 milhões de pessoas.")).replace("Quase 93% do grupo", "Quase 93% do grupo"), "Público, Lisboa 27.09.2017.") + url("https://tinyurl.com/ybs2zpyz", "08.11.2017")
                  + p(" ".join(T(18, "A notícia faz referência à luta histórica", "que esse povo nunca aceitou.")), "Trata-se do povo"),
     "alternativas": alts("catalão.", "curdo.", "druso.", "palestino.", "tibetano."),
     "explicacao": "<p>Os <strong>curdos</strong> são o maior povo sem Estado do mundo, divididos entre Turquia, Síria, Iraque e Irã. Em setembro de 2017, o Curdistão iraquiano votou pela independência em referendo não reconhecido. Alternativa <strong>B</strong>.</p><p>Os catalães vivem na Espanha (A), os drusos são uma minoria religiosa do Levante (C), os palestinos lutam por um Estado em Gaza e na Cisjordânia (D), e os tibetanos estão na China (E).</p>"},
45: {"materia": "Biologia", "assunto": "Evolução", "tags": ["fósseis", "petróleo"],
     "enunciado": p(" ".join(T(18, "A prospecção de petróleo, uma atividade", "uma vez que o petróleo"))),
     "alternativas": AL(18, "(A) resulta da decomposição parcial dos tecidos", "em um passado remoto."),
     "explicacao": "<p>O petróleo se forma a partir de matéria orgânica de microrganismos marinhos (plâncton) soterrada em rochas sedimentares. Microfósseis identificam camadas com idade e ambiente propícios: por isso a Paleontologia ajuda a achar petróleo. Alternativa <strong>D</strong>.</p><p>O petróleo não vem de dinossauros (A) nem de esqueletos fósseis (B). Fica em rochas sedimentares, não metamórficas (C). E não é óleo secretado por seres vivos (E).</p>"},
46: {"materia": "Biologia", "assunto": "Reprodução", "tags": ["ciclos de vida", "meiose"],
     "enunciado": p(" ".join(T(18, "As estratégias de reprodução sexuada", "são classificados em:")))
                  + apoio("• Haplobionte haplonte (como o dos <strong>fungos</strong> sapróbitos <em>Rhizopus</em>);<br>• Haplobionte diplonte (como o dos Animalia);<br>• Diplobionte (como o das <strong>plantas</strong> Embryophyta).")
                  + p("A principal diferença entre esses ciclos consiste no momento em que ocorre"),
     "alternativas": alts("mitose.", "diapausa.", "esporulação.", "nascimento.", "meiose."),
     "explicacao": "<p>Os ciclos se distinguem pelo momento da <strong>meiose</strong>: no haplonte ela é zigótica (logo após a fecundação), no diplonte é gamética (forma os gametas) e no diplobionte é espórica (forma esporos). Alternativa <strong>E</strong>.</p><p>A mitose ocorre em todos os ciclos (A). Diapausa, esporulação e nascimento não definem os tipos de ciclo (B, C e D).</p>"},
47: {"materia": "Biologia", "assunto": "Genética", "tags": ["transcrição", "RNA"],
     "enunciado": p(" ".join(T(19, "Agentes mutagênicos são aqueles", "o gene não sofreu mutação.")), "Dessa forma, a sequência <strong>3′ AGACATATA 5′</strong> de um gene terá escapado à ação de um agente mutagênico caso seja"),
     "alternativas": alts("traduzida em RNAt de sequência <strong>3′TCTGTATAT 5′</strong>.", "traduzida em RNAm de sequência <strong>3′TCTGTATAT 5′</strong>.", "transcrita em RNAm de sequência <strong>5′ UCUGUAUAU 3′</strong>.", "transcrita em RNAm de sequência <strong>5′AGACATATA 3′</strong>.", "transcrita em RNAt de sequência <strong>3′UCUGUAUAU 5′</strong>."),
     "explicacao": "<p>DNA vira RNA por <strong>transcrição</strong>, e o RNA mensageiro é complementar e antiparalelo ao molde, com U no lugar de T: 3′ AGACATATA 5′ → <strong>5′ UCUGUAUAU 3′</strong>. Alternativa <strong>C</strong>.</p><p>Tradução é RNA → proteína, e RNA não tem T (A e B). D não é complementar. E tem a orientação invertida e fala em RNAt.</p>"},
48: {"materia": "Biologia", "assunto": "Genética", "tags": ["grupos sanguíneos", "sistema ABO"],
     "enunciado": apoio("Em um caso hipotético, apenas dois homens, um do grupo sanguíneo <strong>B</strong> (genótipo <strong>I<sup>B</sup>_</strong>) e outro do grupo sanguíneo <strong>A</strong> (genótipo <strong>I<sup>A</sup>_</strong>), podem ser o pai biológico de uma menina do grupo <strong>O</strong> (genótipo <strong>ii</strong>).")
                  + p("Nesse cenário, seria possível determinar com segurança a paternidade se um dos homens"),
     "alternativas": alts("tivesse ou o pai ou a mãe do grupo <strong>O</strong>.", "tivesse o pai e a mãe, ambos do grupo <strong>AB</strong>.", "fosse pai de um menino do grupo <strong>O</strong>.", "fosse pai de um menino do grupo <strong>A</strong>.", "fosse pai de um menino do grupo <strong>B</strong>."),
     "explicacao": "<p>A menina é ii, então o pai tem de ter um alelo i. Se um dos homens tem pai e mãe AB (I<sup>A</sup>I<sup>B</sup>), ele só pode ter recebido I<sup>A</sup> ou I<sup>B</sup> de cada um: é I<sup>A</sup>I<sup>A</sup> ou I<sup>B</sup>I<sup>B</sup>, sem alelo i. Esse homem fica descartado, e o pai é o outro. Alternativa <strong>B</strong>.</p><p>Ter pai ou mãe O só torna provável que o homem tenha o alelo i, sem excluir o outro (A). Ter um filho O mostra que ele tem i, mas o outro também pode ter (C). Filhos A ou B não decidem nada (D e E).</p>"},
49: {"materia": "Biologia", "assunto": "Botânica", "tags": ["anéis de crescimento", "fanerógamas"],
     "enunciado": p(*T(19, "As madeiras continuam sendo, no século XXI", "estado do Tocantins.", ["Para obter certificação"])) + "[[fig:1]]" + url("https://tinyurl.com/y7obj3f", "07.11.2017", "Original colorido.")
                  + p("A comercialização desses móveis"),
     "imagens": figs(("q49", "Fotografia de um corte de tronco de madeira mostrando muitas faixas alternadas claras e escuras, bem marcadas e paralelas: anéis de crescimento.")),
     "alternativas": AL(19, "(A) permitiria que a empresa obtivesse o certificado, já que a madeira apresenta alburno típico do crescimento primário", "fanerógamas temperadas, que não são nativas do Tocantins."),
     "explicacao": "<p>Anéis de crescimento bem marcados surgem do <strong>crescimento secundário</strong> em climas com estações bem definidas, com alternância de lenho de primavera e de inverno: são típicos de árvores (fanerógamas) de clima <strong>temperado</strong>. Uma madeira assim não seria nativa do Tocantins, de clima tropical, e o certificado seria negado. Alternativa <strong>E</strong>.</p><p>Briófitas não formam madeira (B e C). Alburno e anéis não vêm do crescimento primário (A e D).</p>"},
50: {"materia": "Português", "assunto": "Interpretação de texto", "tags": ["estilo"],
     "enunciado": ESTILO + P50,
     "alternativas": AL(20, "(A) O autor que busque um estilo narrativo marcante", "a informalidade da linguagem é inadmissível."),
     "explicacao": "<p>O texto diz que o estilo não está só nas palavras isoladas, “mas em sua configuração estilística”, no jogo entre elas dentro da frase. Alternativa <strong>D</strong>.</p><p>“Preterir” é desprezar, e o texto valoriza a conjunção entre forma e fundo (A). O estilo não se restringe à palavra isolada (B). João Ribeiro fala em “ideia precisa e exata”, não prolixa (C). E o texto admite que até “desvios” podem ser questão de estilo (E).</p>"},
51: {"materia": "Português", "assunto": "Interpretação de texto", "tags": ["Machado de Assis"],
     "enunciado": p("O autor menciona <em>Memorial de Aires</em>, de Machado de Assis, com o intuito de"), "apoio_de": (50, P50),
     "alternativas": AL(20, "(A) destacar a preferência de Machado de Assis", "desprendimento formal do autor."),
     "explicacao": "<p>A frase de Machado é usada para mostrar como os tempos verbais, a oposição singular/plural e a afirmação/negação constroem a narrativa e são “um traço estilístico marcante”. Alternativa <strong>D</strong>.</p><p>O exemplo não trata de linguagem popular (A), da indiferença de Aires (B), de falta de coesão (C) nem de oposição à gramática tradicional (E).</p>"},
52: {"materia": "Português", "assunto": "Figuras de linguagem", "tags": ["sinestesia"],
     "enunciado": p("O texto faz referência à sinestesia, um recurso semântico capaz de tornar o texto mais expressivo.", "Assinale a alternativa que apresenta um exemplo da <strong>figura de linguagem</strong> conhecida como sinestesia."),
     "apoio_de": (50, P50),
     "alternativas": alts("O toque de suas mãos era frio como a neve.", "Suas palavras eram amargas e frias.", "Caía lá fora a neve fria.", "O inverno sem você é glacial.", "O frio contava as histórias de tempos passados."),
     "explicacao": "<p>Sinestesia mistura sensações de sentidos diferentes: “palavras” (audição) “amargas” (paladar) e “frias” (tato). Alternativa <strong>B</strong>.</p><p>A é comparação, C é pleonasmo, D é metáfora/hipérbole e E é personificação.</p>"},
53: {"materia": "Português", "assunto": "Literatura", "tags": ["Machado de Assis", "Realismo"],
     "enunciado": p(" ".join(T(21, "Memorial de Aires é o último romance", "série de episódios que se intercalam.")).replace("Memorial de Aires é", "<em>Memorial de Aires</em> é"), "O trecho a seguir foi retirado do prefácio <em>Advertência</em>, que introduz a obra.")
                  + apoio(" ".join(T(21, "Quem me leu Esaú e Jacó", "se aparecer algum dia.")).replace("Esaú e Jacó", "<em>Esaú e Jacó</em>"))
                  + fonte("ASSIS, Machado de. <em>Memorial de Aires</em>. In:_______. Obra completa. Rio de Janeiro: Nova Aguilar, 1986. p. 1096.")
                  + p("Com base na leitura dos textos e nas obras de Machado de Assis, é correto afirmar que"),
     "alternativas": {k: it(v, "Memorial de Aires", "O Alienista", "Quincas Borba", "Memórias Póstumas de Brás Cubas", "Iaiá Garcia", "Dom Casmurro") for k, v in AL(21, "(A) Memorial de Aires e O Alienista", "ações e reações das personagens.").items()},
     "explicacao": "<p>Os romances da fase madura de Machado, como <em>Dom Casmurro</em> e <em>Memorial de Aires</em>, mergulham na psicologia das personagens: ciúme, memória, motivações íntimas. Alternativa <strong>E</strong>.</p><p>A ironia é marca de Machado, inclusive nessas obras (A). Rubião, de <em>Quincas Borba</em>, termina louco e na miséria (B). Brás Cubas e Aires narram em primeira pessoa (C). E <em>Iaiá Garcia</em> é da fase romântica; a “trilogia realista” reúne <em>Memórias Póstumas</em>, <em>Quincas Borba</em> e <em>Dom Casmurro</em> (D).</p>"},
54: {"materia": "Português", "assunto": "Gramática", "tags": ["tempos verbais", "correlação"],
     "enunciado": p("Na frase de Machado de Assis citada no texto (“Aires não pensava nada, mas percebeu que os outros pensavam alguma cousa”), a relação entre os tempos verbais, embora contrastante, é coerente.", "Assinale a alternativa que também apresenta a correta relação entre os tempos verbais."),
     "apoio_de": (50, P50),
     "alternativas": AL(21, "(A) O pesquisador leu a obra completa", "(E) O pesquisador leria a obra completa de Clarice Lispector para que tenha podido identificar as marcas de estilo da escritora."),
     "explicacao": "<p>Pretérito perfeito do indicativo (“leu”) combina com pretérito imperfeito do subjuntivo (“pudesse”): <strong>leu ... para que pudesse</strong>. Alternativa <strong>A</strong>.</p><p>As outras misturam tempos que não se correlacionam: “lia ... terá podido” (B), “lê ... pudera” (C), “lerá ... tivesse podido” (D), “leria ... tenha podido” (E). O certo seria, por exemplo, “lê ... para que possa”, “lerá ... para que possa” ou “leria ... para que pudesse”.</p>"},
})
completar(Q, R)
