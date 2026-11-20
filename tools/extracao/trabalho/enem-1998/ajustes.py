# Enem 1998 (data não confirmada; dataExame omitida), Prova 1 – amarela: prova única de 63 questões (modelo antigo, a primeira edição do Enem).
# Fonte do PDF: arquivo 'Prova_Caderno_Amarelo_1998' do usuário (cabeçalho "ENEM/98", rodapé "amarela"; redação "Viver e Aprender").
# Gabarito: cópia do gabarito oficial (Ministério da Educação/Inep, "Gabaritos oficiais das questões objetivas da prova do ENEM 1998", Prova 1 – Amarela)
# no acervo da USP: GABARITO_ENEM_1998_AMARELA.pdf, lido duas vezes.
# Uma coluna; as questões 1 e 2 já estão na página 1 (com a redação): extrator com START=0 LINHAS=1 NXR=33-56 YMIN=40 YMAX=805.
# O texto comum que vem antes de cada grupo de questões cai na alternativa E anterior: cortado com o dicionário CORTE.
# Protegidos como imagem: os dois textos da Q8 (Macedo, domínio público, e Manuel Bandeira), renderizados em letra maior.
# Em texto: crônica de Veríssimo e prosa de Bandeira (prosa), Camões (domínio público).
import sys, pathlib, re, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar

ID = "enem-1998"
META = {"id": ID, "banca": "Enem", "ano": 1998, "titulo": "Enem 1998: Prova objetiva", "fonte": "Inep",
        "duracaoMinutos": 300, "area": "Prova objetiva (63 questões)", "caderno": "amarelo", "dia": 1, "fonteGabarito": {"oficial": True, "nome": "gabarito oficial do Inep, em cópia guardada pelo Instituto de Física da USP", "url": "https://fep.if.usp.br/~profis/arquivo/avaliacao/enem/provas_gabaritos/1998/GABARITO_ENEM_1998_AMARELA.pdf"}}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 64)}
D = {int(k): v for k, v in json.loads((pathlib.Path(__file__).resolve().parent / "alts.json").read_text(encoding="utf-8")).items()}
Q = {}
p = lambda *xs: "".join(f"<p>{x}</p>" for x in xs)
ap = lambda *xs: "".join(f'<p class="apoio">{x}</p>' for x in xs)
tit = lambda x: f'<p class="apoio"><strong>{x}</strong></p>'
fonte = lambda x: f'<p class="fonte">{x}</p>'
ALT = lambda ini: {k: f"[[fig:{i}]]" for i, k in enumerate("ABCDE", ini)}
A5 = lambda *xs: dict(zip("ABCDE", xs))
I3 = lambda *xs: '<ol type="I">' + "".join(f"<li>{x}</li>" for x in xs) + "</ol>"
AREAS = {"L": "Linguagens", "H": "Ciências Humanas", "N": "Ciências da Natureza", "M": "Matemática"}


def figs(*pares):
    return [{"arquivo": a, "alt": t} for a, t in pares]


def tabela(cab, linhas):
    return ('<table class="tabela"><thead><tr>' + "".join(f"<th>{c}</th>" for c in cab) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in l) + "</tr>" for l in linhas) + "</tbody></table>")


def QF(s):
    partes = re.split(r"(<[^>]+>)", s)
    return "".join(x if x.startswith("<") else re.sub(r"\b(CO|O|N|H|SO|NO)(\d)\b", r"\1<sub>\2</sub>", x) for x in partes)


def X(n, area, materia, assunto, expl, enun, imagens=(), tags=(), alts=None, quim=False):
    e = re.sub(r"<((?:www\.|http)[^<>]*)>", r"&lt;\1&gt;", enun)
    if quim: e = QF(e)
    al = dict(alts or D[n])
    assert sorted(al) == list("ABCDE"), (n, al)
    Q[n] = {"materia": materia, "assunto": assunto, "area": AREAS[area], "tags": list(tags), "numeroOriginal": n,
            "enunciado": e, "alternativas": {k: (QF(v) if quim else v) for k, v in al.items()},
            "imagens": list(imagens), "explicacao": expl}



# ----------------------------------------------------------------
CORTE = {2: "1200 bolinhas.", 5: "momentaneamente", 6: "estão corretas.", 7: "nada sofreria.", 8: "igual ao homem.", 10: "90 cm", 13: "a turbina.",
         14: "expressão mundial.", 15: "1988 e 1991.", 16: "fora da União Européia.", 17: "Língua Portuguesa.", 19: "6kg e 8kg", 21: "1/6", 27: "60",
         30: "III apenas.", 32: "exatamente iguais.", 34: "teatral.", 35: "morrer.", 36: "120", 39: "2 e 3", 40: "definitivas e absolutas.",
         42: "uma só classe.", 44: "vertiginosamente.", 46: "III, IV e V, apenas.", 49: "prejudiciais à saúde.", 51: "30%", 53: "I e III, apenas.",
         54: "de uma dada área.", 56: "III, I, IV, apenas.", 57: "III e IV, apenas.", 58: "eleger deputados.", 60: "9 e 15 segundos.", 61: "crescimento econômico.", 62: "da altitude."}
for _n, _fim in CORTE.items():
    _e = D[_n]["E"]; D[_n]["E"] = re.sub(r"\s+", " ", _e[:_e.index(_fim) + len(_fim)]).strip()
D[5]["E"] = "pegá-los momentaneamente."
for _n in D:
    D[_n] = {k: re.sub(r"\s+", " ", v).strip() for k, v in D[_n].items()}
I4 = lambda *xs: '<ol type="I"><li>' + "</li><li>".join(xs) + "</li></ol>"

BOLAS = tit("Texto para as questões 1 e 2.") + p("Observe nas questões 1 e 2 o que foi feito para colocar bolinhas de gude de 1 cm de diâmetro numa caixa cúbica com 10 cm de aresta.")
X(1, "M", "Matemática", "Contagem", "<p>Com bolinhas de 1 cm numa caixa de 10 cm, cabem 10 em cada direção: cada camada tem 10 × 10 = 100 bolinhas, e há 10 camadas. Total: 10 × 10 × 10 = 1000 bolinhas. Alternativa <strong>C</strong>.</p>",
  BOLAS + p("Uma pessoa arrumou as bolinhas em camadas superpostas iguais, tendo assim empregado:") + "[[fig:1]]",
  figs(("q01", "Caixa cúbica cheia de bolinhas arrumadas em fileiras e camadas regulares.")), ["volume do cubo", "contagem"])
X(2, "M", "Matemática", "Contagem", "<p>Nas camadas alternadas, uma camada tem 10 × 10 = 100 bolinhas, e a seguinte, apoiada nos vãos, tem 9 × 9 = 81. Com 12 camadas, são 6 de cada tipo: 6 × 100 + 6 × 81 = 600 + 486 = 1086 bolinhas. Alternativa <strong>D</strong>.</p><p>Essa arrumação cabe mais bolinhas que a do cubo simples (1000), porque as camadas se encaixam e ocupam menos altura.</p>",
  BOLAS + p("Uma segunda pessoa procurou encontrar outra maneira de arrumar as bolas na caixa achando que seria uma boa idéia organizá-las em camadas alternadas, onde cada bolinha de uma camada se apoiaria em 4 bolinhas da camada inferior, como mostra a figura. Deste modo, ela conseguiu fazer 12 camadas. Portanto, ela conseguiu colocar na caixa:") + "[[fig:1]]",
  figs(("q02", "Uma bolinha descendo para se apoiar no vão entre quatro bolinhas da camada de baixo.")), ["contagem", "empacotamento"])

GALERA = (tit("Texto para as questões 3 a 5.") + p("Para falar e escrever bem, é preciso, além de conhecer o padrão formal da Língua Portuguesa, saber adequar o uso da linguagem ao contexto discursivo. Para exemplificar este fato, seu professor de Língua Portuguesa convida-o a ler o texto <em>Aí, Galera</em>, de Luís Fernando Veríssimo. No texto, o autor brinca com situações de discurso oral que fogem à expectativa do ouvinte.")
  + ap("<strong>Aí, Galera</strong>", "<em>Jogadores de futebol podem ser vítimas de estereotipação. Por exemplo, você pode imaginar um jogador de futebol dizendo “estereotipação”? E, no entanto, por que não?</em>",
       "<em>- Aí, campeão. Uma palavrinha pra galera.<br>- Minha saudação aos aficionados do clube e aos demais esportistas, aqui presentes ou no recesso dos seus lares.<br>- Como é?<br>- Aí, galera.<br>- Quais são as instruções do técnico?<br>- Nosso treinador vaticinou que, com um trabalho de contenção coordenada, com energia otimizada, na zona de preparação, aumentam as probabilidades de, recuperado o esférico, concatenarmos um contragolpe agudo com parcimônia de meios e extrema objetividade, valendo-nos da desestruturação momentânea do sistema oposto, surpreendido pela reversão inesperada do fluxo da ação.<br>- Ahn?<br>- É pra dividir no meio e ir pra cima pra pegá eles sem calça.<br>- Certo. Você quer dizer mais alguma coisa?<br>- Posso dirigir uma mensagem de caráter sentimental, algo banal, talvez mesmo previsível e piegas, a uma pessoa à qual sou ligado por razões, inclusive, genéticas?<br>- Pode.<br>- Uma saudação para a minha progenitora.<br>- Como é?<br>- Alô, mamãe!<br>- Estou vendo que você é um, um...<br>- Um jogador que confunde o entrevistador, pois não corresponde à expectativa de que o atleta seja um ser algo primitivo com dificuldade de expressão e assim sabota a estereotipação?<br>- Estereoquê?<br>- Um chato?<br>- Isso.</em>")
  + fonte("<em>Correio Braziliense</em>, 13/05/1998."))
X(3, "L", "Língua Portuguesa", "Variação linguística", "<p>O público espera um jogador de linguagem simples, mas ele fala de modo muito formal, inadequado a uma entrevista à beira do campo, e com grande desenvoltura e vocabulário rebuscado (“vaticinou”, “progenitora”). As duas situações que fogem à expectativa são essas. Alternativa <strong>B</strong>.</p>",
  GALERA + p("O texto retrata duas situações relacionadas que fogem à expectativa do público. São elas:"), tags=["Veríssimo", "adequação linguística"])
X(4, "L", "Língua Portuguesa", "Variação linguística", "<p>Num congresso internacional, espera-se de um professor universitário a norma culta. A frase de E mistura “a gente” com “termos” e tem construção coloquial e confusa: é inadequada ao contexto. Alternativa <strong>E</strong>.</p><p>Nas outras, a linguagem combina com a situação: conversa informal na rua (A) e entre amigos (B), registro cuidado numa reunião (C) e numa carta formal (D).</p>",
  GALERA + p("O texto mostra uma situação em que a linguagem usada é <strong><u>inadequada</u></strong> ao contexto. Considerando as diferenças entre língua oral e língua escrita, assinale a opção que representa também uma inadequação da linguagem usada ao contexto:"),
  tags=["registro formal e informal", "adequação linguística"])
X(5, "L", "Língua Portuguesa", "Expressões idiomáticas", "<p>“Pegar alguém sem calça” é surpreender o adversário despreparado, desprotegido. Em língua culta: “pegá-los desprevenidos”. Alternativa <strong>B</strong>.</p><p>O jogador acabara de falar em surpreender o sistema oposto “pela reversão inesperada do fluxo da ação”.</p>",
  GALERA + p("A expressão “pegá eles sem calça” poderia ser substituída, sem comprometimento de sentido, em língua culta, formal, por:"), tags=["expressão idiomática", "norma culta"])

X(6, "H", "Geografia", "Ciclo da água", "<p>II, III, IV e V estão corretas: as plantas devolvem água pela transpiração; o ciclo liga litosfera, atmosfera e biosfera; a gravidade faz a chuva cair e os rios correrem; e o ser humano interfere no ciclo (represas, desmatamento, impermeabilização). I é falsa: a maior parte da evaporação ocorre nos oceanos, que cobrem a maior parte do planeta. Alternativa <strong>D</strong>.</p>",
  p("O sol participa do ciclo da água, pois além de aquecer a superfície da Terra dando origem aos ventos, provoca a evaporação da água dos rios, lagos e mares. O vapor da água, ao se resfriar, condensa em minúsculas gotinhas, que se agrupam formando as nuvens, neblinas ou névoas úmidas. As nuvens podem ser levadas pelos ventos de uma região para outra. Com a condensação e, em seguida, a chuva, a água volta à superfície da Terra, caindo sobre o solo, rios, lagos e mares. Parte dessa água evapora retornando à atmosfera, outra parte escoa superficialmente ou infiltra-se no solo, indo alimentar rios e lagos. Esse processo é chamado de ciclo da água.", "Considere, então, as seguintes afirmativas:")
  + '<ol type="I"><li>a evaporação é maior nos continentes, uma vez que o aquecimento ali é maior do que nos oceanos.</li><li>a vegetação participa do ciclo hidrológico por meio da transpiração.</li><li>o ciclo hidrológico condiciona processos que ocorrem na litosfera, na atmosfera e na biosfera.</li><li>a energia gravitacional movimenta a água dentro do seu ciclo.</li><li>o ciclo hidrológico é passível de sofrer interferência humana, podendo apresentar desequilíbrios.</li></ol>',
  tags=["ciclo hidrológico"])

X(7, "N", "Física", "Torque", "<p>O peso do portão, somado ao do garoto na ponta livre, tende a girar o portão para baixo em torno das dobradiças. A dobradiça de cima (A) é puxada para fora, e a de baixo (B) é empurrada contra o muro. O esforço de tração em A é maior, então é mais provável que ela arrebente primeiro. Alternativa <strong>A</strong>.</p>",
  p("Um portão está fixo em um muro por duas dobradiças A e B, conforme mostra a figura, sendo P o peso do portão.") + "[[fig:1]]"
  + p("Caso um garoto se dependure no portão pela extremidade livre, e supondo que as reações máximas suportadas pelas dobradiças sejam iguais,"),
  figs(("q07", "Portão retangular preso ao muro, à esquerda, por duas dobradiças: A, mais em cima, e B, mais embaixo; a outra extremidade do portão fica livre.")),
  ["momento de uma força", "equilíbrio"])

X(8, "L", "Literatura", "Intertextualidade", "<p>Nos dois textos, as lágrimas do homem fazem parte da encenação do amor romântico idealizado: o homem “terno e curvo” que chora “pranto de sangue”, o sujeito que jura “uma paixão do tamanho de um bonde” e se ajoelha. É a esse tratamento idealizado da relação homem/mulher que os autores aludem, para alertar a mulher de que ele é falso. Alternativa <strong>A</strong>.</p><p>Os textos não falam da família (C) nem comparam o valor da mulher e do homem (D, E).</p>",
  "[[fig:1]]" + p("Os autores, ao fazerem alusão às imagens da lágrima sugerem que:"),
  figs(("q08", "Dois textos. Texto 1, de Joaquim Manoel de Macedo: aconselha a mulher a não amar e a não crer no homem terno que jura amor e chora pranto de sangue, porque as lágrimas são gotas da mentira e o juramento, manto da perfídia. Texto 2, de Manuel Bandeira: aconselha Teresa a não acreditar no sujeito sentimental que jura uma paixão enorme, chora, se ajoelha e se rasga todo, porque é lágrima de cinema, tapeação, mentira, e termina com “cai fora”.")),
  ["Manuel Bandeira", "amor romântico"])

X(9, "N", "Biologia", "Hormônios", "<p>II está correta: o crescimento depende da herança genética e de fatores ambientais, como alimentação, exercício e sono. III também: os anabolizantes afetam o sistema circulatório, e problemas circulatórios podem causar impotência. I é falsa: o efeito anabolizante é o ganho muscular, e o maior perigo da automedicação é a falta de controle das doses. IV é falsa: as mulheres também sofrem efeitos graves, como masculinização. Alternativa <strong>D</strong>.</p>",
  p("Matéria publicada em jornal diário discute o uso de anabolizantes (apelidados de “bombas”) por praticantes de musculação. Segundo o jornal, “<em>os anabolizantes são hormônios que dão uma força extra aos músculos. Quem toma consegue ganhar massa muscular mais rápido que normalmente. Isso porque uma pessoa pode crescer até certo ponto, segundo sua herança genética e independentemente do quanto ela se exercite</em>”. Um professor de musculação, diz: “<em>Comecei a tomar bomba por conta própria. Ficava nervoso e tremia. Fiquei impotente durante uns seis meses. Mas como sou lutador de vale tudo, tenho que tomar</em>”.",
    "A respeito desta matéria, dois amigos fizeram os seguintes comentários:")
  + I4("o maior perigo da auto-medicação é seu fator anabolizante, que leva à impotência sexual.", "o crescimento corporal depende tanto dos fatores hereditários quanto do tipo de alimentação da pessoa, se pratica ou não esportes, se dorme as 8 horas diárias.",
       "os anabolizantes devem ter mexido com o sistema circulatório do professor de musculação, pois ele até ficou impotente.", "os anabolizantes são mais perigosos para os homens, pois as mulheres, além de não correrem o risco da impotência, são protegidas pelos hormônios femininos.")
  + p("Tomando como referência as informações da matéria do jornal e o que se conhece da fisiologia humana, pode-se considerar que estão corretos os comentários:"),
  tags=["anabolizantes", "automedicação"])

X(10, "M", "Matemática", "Semelhança", "<p>A pessoa de 1,80 m faz sombra de 0,60 m: a altura é 3 vezes a sombra, e o poste (sombra de 2,00 m) tem 6 m. Mais tarde, a sombra do poste mede 1,50 m: a razão sombra/altura passa a 1,50/6 = 1/4. A sombra da pessoa será 1,80/4 = 0,45 m = 45 cm. Alternativa <strong>B</strong>.</p>",
  p("<strong>A sombra de uma pessoa que tem 1,80 m de altura mede 60 cm. No mesmo momento, a seu lado, a sombra projetada de um poste mede 2,00 m. Se, mais tarde, a sombra do poste diminuiu 50 cm, a sombra da pessoa passou a medir:</strong>"),
  tags=["semelhança de triângulos", "proporção"])

USINA = tit("Texto para as questões 11 a 13.") + p("Na figura abaixo está esquematizado um tipo de usina utilizada na geração de eletricidade.") + "[[fig:1]]"
F_US = figs(("q11", "Esquema de usina: a água de uma represa, à altura h, desce por um tubo até uma turbina; a turbina, embaixo, está ligada por um eixo a um gerador; do gerador saem fios até uma torre de transmissão."))
X(11, "N", "Física", "Usinas", "<p>A água represada desce, ganha velocidade e gira a turbina: a usina aproveita a energia cinética da água, que vem da energia potencial da altura h. É uma hidrelétrica. Alternativa <strong>B</strong>.</p><p>Não há queima de combustível (C), vento (D) nem reação nuclear (E).</p>",
  USINA + p("Analisando o esquema, é possível identificar que se trata de uma usina:"), F_US, ["hidrelétrica", "energia cinética"])
X(12, "N", "Física", "Potência", "<p>A potência elétrica é 0,9 da potência da queda d’água: P = 0,9 × (massa por segundo) × g × h. Então a massa por segundo é 512 × 10<sup>6</sup>/(0,9 × 10 × 120) ≈ 474 000 kg/s. Como 1 litro de água tem 1 kg, a vazão é da ordem de 500 000 litros por segundo. Alternativa <strong>E</strong>.</p>",
  USINA + p("A eficiência de uma usina, do tipo da representada na figura da questão anterior, é da ordem de 0,9, ou seja, 90% da energia da água no início do processo se transforma em energia elétrica. A usina Ji-Paraná, do Estado de Rondônia, tem potência instalada de 512 milhões de watt, e a barragem tem altura de aproximadamente 120 m. A vazão do rio Ji-Paraná, em litros de água por segundo, deve ser da ordem de:"),
  F_US, ["energia potencial", "rendimento"])
X(13, "N", "Física", "Transformações de energia", "<p>A energia cinética vira elétrica entre a turbina e o gerador (I): a turbina gira o gerador. A energia potencial gravitacional vira cinética entre a água no nível h e a turbina (II): a água cai e ganha velocidade. Alternativa <strong>D</strong>.</p>",
  USINA + p("No processo de obtenção de eletricidade, ocorrem várias transformações de energia. Considere duas delas:", "<strong>I.</strong> cinética em elétrica; <strong>II.</strong> potencial gravitacional em cinética.", "Analisando o esquema, é possível identificar que elas se encontram, respectivamente, entre:"),
  F_US, ["transformações de energia"],
  alts=A5("I: a água no nível h e a turbina; II: o gerador e a torre de distribuição.", "I: a água no nível h e a turbina; II: a turbina e o gerador.", "I: a turbina e o gerador; II: a turbina e o gerador.", "I: a turbina e o gerador; II: a água no nível h e a turbina.", "I: o gerador e a torre de distribuição; II: a água no nível h e a turbina."))

X(14, "H", "História", "Conflitos contemporâneos", "<p>Índia e Paquistão já travaram três guerras pela Caxemira e, em 1998, testaram bombas atômicas e rejeitaram a condenação da ONU: estão numa escalada perigosa de solução de problemas pela força. Alternativa <strong>D</strong>.</p><p>A bomba já existia em 1945, antes da independência do Paquistão em 1947 (A), e a Caxemira está dividida entre os dois países, não é independente (C).</p>",
  p("Os efeitos abomináveis das armas nucleares já foram sentidos pelos japoneses há mais de 50 anos (1945). Vários países têm, isoladamente, capacidade nuclear para comprometer a vida na Terra. Montar o seu sistema de defesa é um direito de todas as nações, mas um ato irresponsável ou um descuido pode desestruturar, pelo medo ou uso, a vida civilizada em vastas regiões. A não-proliferação de armas nucleares é importante.",
    "No 1º domingo de junho de 98, Índia e Paquistão rejeitaram a condenação da ONU, decorrente da explosão de bombas atômicas pelos dois países, a título de teste nuclear e comemoradas com festa, especialmente no Paquistão. O governo paquistanês (país que possui maioria da população muçulmana) considerou que a condenação não levou em conta o motivo da disputa: o território de CAXEMIRA, pelo qual já travaram 3 guerras desde sua independência (em 1947, do Império Britânico, que tinha o Subcontinente Indiano como colônia). Dois terços da região, de maioria muçulmana, pertencem à Índia e 1/3 ao Paquistão.",
    "Sobre o tempo e os argumentos podemos dizer que:"),
  tags=["Caxemira", "armas nucleares"])

X(15, "H", "Geografia", "Leitura de gráficos", "<p>No gráfico, a menor taxa é de cerca de 8,7% (1989) e a maior, de cerca de 15,2% (1992): no período, a taxa ficou entre 8% e 16%. Alternativa <strong>D</strong>.</p><p>A maior taxa passa de 14% (A); 1995 não foi o menor valor (B); depois de 1992 a taxa caiu e voltou a subir (C); e entre 1988 e 1989 ela caiu (E).</p>",
  p("Um estudo sobre o problema do desemprego na Grande São Paulo, no período 1985-1996, realizado pelo SEADE-DIEESE, apresentou o seguinte gráfico sobre taxa de desemprego.") + "[[fig:1]]"
  + p("Pela análise do gráfico, é correto afirmar que, no período considerado,"),
  figs(("q15", "Gráfico “Médias anuais da taxa de desemprego total, Grande São Paulo, 1985–1996”. Valores aproximados: 1985, 12,2%; 1986, 9,6%; 1987, 9,2%; 1988, 9,7%; 1989, 8,7%; 1990, 10,3%; 1991, 11,7%; 1992, 15,2%; 1993, 14,6%; 1994, 14,2%; 1995, 13,2%; 1996, 15,1%. Fonte: SEP, Convênio SEADE-DIEESE.")),
  ["desemprego", "leitura de gráfico"])

X(16, "H", "Geografia", "União Europeia", "<p>Num bloco econômico, os países somam mercados e esforços: a economia alemã ganha escala para concorrer com as de fora do bloco, como Estados Unidos e Japão. Alternativa <strong>E</strong>.</p><p>O bloco amplia o mercado e a livre iniciativa entre os membros (A, B, C) e aumenta a concorrência interna, sem garantir empregos (D).</p>",
  p("As diferentes formas em que as sociedades se organizam socioeconomicamente visam a atender suas necessidades para a época. O liberalismo, atualmente, assume papel crescente, com os Estados diminuindo sua atuação em várias áreas, inclusive vendendo empresas estatais. Da idéia de interferência estatal na economia, do “Estado de Bem-Estar”, da assistência social ampla e emprego garantido por lei, e, às vezes, à custa de subsídios (na Europa defendido pela Social-Democracia), caminha-se para um Estado enxuto e ágil, onde a manutenção do progresso econômico e uma maior liberdade na conquista do mercado são as formas de assegurar ao cidadão o acesso ao bem-estar. Nem sempre a população concorda.",
    "Neste contexto, as eleições gerais na Alemanha, em 1998, poderão levar Helmuth Kohl, com longa e frutuosa carreira à frente daquele país, a entregar o posto ao social-democrata Gerhard Schroeder. O desemprego na Alemanha atinge seu ponto máximo. A moeda única européia será o fim do Marco Alemão. A imagem de Helmuth Kohl começa a desvanecer-se. Conseguirá vencer este ano? Seja como for, ele luta. Mas recebeu um novo e tremendo golpe: o Partido Liberal (FDP) deixou Kohl. O secretário Geral do FDP, Guido Westerwelle declarou: Começou o fim da era Kohl!",
    "A Alemanha ajuda a concretizar o bloco econômico da União Européia. A participação neste bloco implica a adoção de um sistema socioeconômico que:"),
  tags=["blocos econômicos", "neoliberalismo"])

X(17, "L", "Literatura", "Modernismo", "<p>Bandeira valoriza o “pra mim brincar” das cariocas que não sabem gramática: o Modernismo buscou a identidade brasileira e levou para a literatura a fala real do povo, com sua diversidade. Alternativa <strong>A</strong>.</p><p>Bandeira elogia a fala das cariocas (B, E), e os modernistas romperam com a tradição portuguesa (C).</p>",
  p("A discussão sobre gramática na classe está “quente”. Será que os brasileiros sabem gramática? A professora de Português propõe para debate o seguinte texto:")
  + ap("<strong>PRA MIM BRINCAR</strong>", "<em>Não há nada mais gostoso do que o mim sujeito de verbo no infinito. Pra mim brincar. As cariocas que não sabem gramática falam assim. Todos os brasileiros deviam de querer falar como as cariocas que não sabem gramática.</em>", "<em>— As palavras mais feias da língua portuguesa são quiçá, alhures e miúde.</em>")
  + fonte("(BANDEIRA, Manuel. <em>Seleta em prosa e verso</em>. Org: Emanuel de Moraes. 4ª ed. Rio de Janeiro, José Olympio, 1986. Pág. 19)")
  + p("Com a orientação da professora e após o debate sobre o texto de Manuel Bandeira, os alunos chegaram à seguinte conclusão:"),
  tags=["Manuel Bandeira", "fala brasileira"])

ACUCAR = tit("Texto para as questões 18 e 19.") + p("Um armazém recebe sacos de açúcar de 24 kg para que sejam empacotados em embalagens menores. O único objeto disponível para pesagem é uma balança de 2 pratos, sem os pesos metálicos.")
X(18, "M", "Matemática", "Raciocínio lógico", "<p>Sem pesos, a balança só serve para dividir uma quantidade em duas partes iguais, equilibrando os pratos. Com uma pesagem, os 24 kg viram dois pacotes de 12 kg. Alternativa <strong>E</strong>.</p><p>Pacotes de 3, 4, 6 ou 8 kg exigiriam outras divisões ou pesos de referência, que não existem.</p>",
  ACUCAR + p("Realizando uma única pesagem, é possível montar pacotes de:"), tags=["divisão ao meio", "raciocínio lógico"])
X(19, "M", "Matemática", "Raciocínio lógico", "<p>Primeira pesagem: 24 kg em 12 + 12. Segunda pesagem: um pacote de 12 kg em 6 + 6. Com exatamente duas pesagens há pacotes de 6 kg, 12 kg (o que não foi dividido) e 18 kg (juntando 12 + 6). Alternativa <strong>C</strong>.</p><p>3 kg exigiriam uma terceira divisão.</p>",
  ACUCAR + p("Realizando exatamente duas pesagens, os pacotes que podem ser feitos são os de:"), tags=["divisão ao meio", "raciocínio lógico"])

TVE = tit("Texto para as questões 20 e 21.") + p("Em um concurso de televisão, apresentam-se ao participante 3 fichas voltadas para baixo, estando representada em cada uma delas as letras T, V e E. As fichas encontram-se alinhadas em uma ordem qualquer. O participante deve ordenar as fichas ao seu gosto, mantendo as letras voltadas para baixo, tentando obter a sigla TVE. Ao desvirá-las, para cada letra que esteja na posição correta ganhará um prêmio de R$ 200,00.")
X(20, "M", "Matemática", "Probabilidade", "<p>As 3 fichas podem ficar em 3! = 6 ordens. Nenhuma letra no lugar certo só acontece em VET e ETV: 2 casos. A probabilidade é 2/6 = 1/3. Alternativa <strong>B</strong>.</p><p>As 6 ordens são TVE (3 acertos), TEV, VTE e EVT (1 acerto cada), e VET e ETV (nenhum acerto).</p>",
  TVE + p("A probabilidade de o <strong><u>participante</u></strong> não ganhar qualquer prêmio é igual a:"), tags=["permutações", "probabilidade"])
X(21, "M", "Matemática", "Probabilidade", "<p>Ganhar R$ 400,00 seria acertar exatamente 2 letras. Mas, se duas letras estão no lugar certo, a terceira também está, porque só sobra o lugar dela. É impossível: probabilidade 0. Alternativa <strong>A</strong>.</p>",
  TVE + p("A probabilidade de o <strong><u>concorrente</u></strong> ganhar exatamente o valor de R$ 400,00 é igual a:"), tags=["probabilidade", "evento impossível"])

CONTAS = (tit("Texto para as questões 22 a 24.") + p("No quadro abaixo estão as contas de luz e água de uma mesma residência. Além do valor a pagar, cada conta mostra como calculá-lo, em função do consumo de água (em m³) e de eletricidade (em kWh). Observe que, na conta de luz, o valor a pagar é igual ao consumo multiplicado por um certo fator. Já na conta de água, existe uma tarifa mínima e diferentes faixas de tarifação.")
  + p("<strong>Companhia de Eletricidade</strong>") + tabela(["Fornecimento", "Valor (R$)"], [["401 kWh × 0,13276000", "53,23"]])
  + p("<strong>Companhia de Saneamento — tarifas de água por m³</strong>")
  + tabela(["Faixas de consumo (m³)", "Tarifa (R$)", "Consumo", "Valor (R$)"], [["até 10", "5,50", "tarifa mínima", "5,50"], ["11 a 20", "0,85", "7", "5,95"], ["21 a 30", "2,13", "", ""], ["31 a 50", "2,13", "", ""], ["acima de 50", "2,36", "", ""], ["", "", "<strong>Total</strong>", "<strong>11,45</strong>"]]))
X(22, "M", "Matemática", "Função linear", "<p>Na conta de luz, o valor é proporcional ao consumo. Dobrando o consumo (802 kWh), o valor dobra: 2 × 53,23 = 106,46. Alternativa <strong>B</strong>.</p><p>R$ 802,00 (C) confunde o consumo em kWh com o valor em reais, e R$ 55,23 (A) soma 2 reais em vez de dobrar.</p>",
  CONTAS + p("Suponha que, no próximo mês, dobre o consumo de energia elétrica dessa residência. O novo valor da conta será de:"), tags=["proporcionalidade", "conta de luz"],
  alts=A5("R$ 55,23", "R$ 106,46", "R$ 802,00", "R$ 100,00", "R$ 22,90"))
X(23, "M", "Matemática", "Função por partes", "<p>O consumo atual é 10 + 7 = 17 m³; dobrado, 34 m³. Valor: tarifa mínima até 10 m³, R$ 5,50; de 11 a 20, 10 × 0,85 = R$ 8,50; de 21 a 30, 10 × 2,13 = R$ 21,30; e mais 4 m³ na faixa de 31 a 50, 4 × 2,13 = R$ 8,52. Total: R$ 43,82. Alternativa <strong>C</strong>.</p><p>R$ 22,90 (A) seria dobrar o valor da conta, o que não vale com faixas de preço crescente.</p>",
  CONTAS + p("Suponha agora que dobre o consumo d’água. O novo valor da conta será de:"), tags=["tarifas por faixa", "conta de água"],
  alts=A5("R$ 22,90", "R$ 106,46", "R$ 43,82", "R$ 17,40", "R$ 22,52"))
X(24, "M", "Matemática", "Função por partes", "<p>A conta de água tem um valor mínimo fixo até 10 m³ (trecho horizontal, que não começa em zero) e, depois, cresce em trechos retos cada vez mais inclinados, porque a tarifa por m³ aumenta de faixa em faixa. É o gráfico A. Alternativa <strong>A</strong>.</p><p>B começa do zero, sem tarifa mínima; C e D são retas, com tarifa única; E é constante.</p>",
  CONTAS + p("Dos gráficos abaixo, o que melhor representa o valor da conta de água, de acordo com o consumo, é:"),
  figs(("q24a", "Gráfico do valor (R$) em função do consumo (m³): um trecho horizontal acima de zero no começo e depois trechos retos cada vez mais inclinados."), ("q24b", "Gráfico partindo da origem, com trechos retos cada vez mais inclinados."),
       ("q24c", "Gráfico: reta inclinada partindo da origem."), ("q24d", "Gráfico: reta inclinada que começa acima de zero."), ("q24e", "Gráfico: reta horizontal acima de zero.")),
  ["função definida por partes", "gráficos"], alts=ALT(1))

ARVORE = (tit("Texto para as questões 25 a 27.") + p("O assunto na aula de Biologia era a evolução do Homem. Foi apresentada aos alunos uma árvore filogenética, igual à mostrada na ilustração, que relacionava primatas atuais e seus ancestrais.") + "[[fig:1]]")
F_ARV = figs(("q25", "Árvore filogenética provável dos antropoides, com escala de tempo em milhões de anos (0, 5, 10, 15, 25, 35, 50). Na base, há 50 milhões de anos, os mamíferos insetívoros. Os símios do Novo Mundo e os do Velho Mundo se separam cedo. Por volta de 15 milhões de anos, perto do Dryopithecus, partem os ramos do gibão (hilobatídeos), do orangotango, do gorila e do chimpanzé (pongídeos) e do homem (hominídeos). O ramo humano passa pelo Ramapithecus e pelo Australopithecus. O chimpanzé é o pongídeo cujo ramo se separa mais tarde do humano."))
X(25, "N", "Biologia", "Evolução humana", "<p>Na árvore, os antropoides atuais e o homem estão todos no topo (tempo 0): são contemporâneos (I). E as linhas do homem e dos antropoides se juntam num ancestral comum (III). II é falsa: o homem não descende dos macacos atuais; ambos descendem de ancestrais comuns. IV é falsa: há parentesco genético. Alternativa <strong>B</strong>.</p>",
  ARVORE + p("Após observar o material fornecido pelo professor, os alunos emitiram várias opiniões, a saber:")
  + I4("os macacos antropóides (orangotango, gorila e chimpanzé e gibão) surgiram na Terra mais ou menos contemporaneamente ao Homem.", "alguns homens primitivos, hoje extintos, descendem dos macacos antropóides.", "na história evolutiva, os homens e os macacos antropóides tiveram um ancestral comum.", "não existe relação de parentesco genético entre macacos antropóides e homens.")
  + p("Analisando a árvore filogenética, você pode concluir que:"), F_ARV, ["árvore filogenética", "ancestral comum"])
X(26, "N", "Biologia", "Evolução humana", "<p>O parente mais próximo é aquele cujo ramo se separou do nosso mais recentemente. Na árvore, entre os primatas atuais, é o chimpanzé, e a comparação de DNA e proteínas confirma isso. Alternativa <strong>B</strong>.</p><p>Australopithecus e Ramapithecus estão extintos; não são primatas atuais (A, C).</p>",
  ARVORE + p("Foram feitas comparações entre DNA e proteínas da espécie humana com DNA e proteínas de diversos primatas. Observando a árvore filogenética, você espera que os dados bioquímicos tenham apontado, entre os primatas atuais, como nosso parente mais próximo o:"),
  F_ARV, ["parentesco evolutivo"])
X(27, "N", "Biologia", "Evolução humana", "<p>Na árvore, os ramos do gibão, do orangotango, do gorila, do chimpanzé e do homem se juntam perto da linha de 15 milhões de anos, logo acima do Dryopithecus. É preciso voltar cerca de 15 milhões de anos. Alternativa <strong>C</strong>.</p>",
  ARVORE + p("Se fosse possível a uma máquina do tempo percorrer a evolução dos primatas em sentido contrário, aproximadamente quantos milhões de anos precisaríamos retroceder, de acordo com a árvore filogenética apresentada, para encontrar o ancestral comum do homem e dos macacos antropóides (gibão, orangotango, gorila e chimpanzé)?"),
  F_ARV, ["tempo evolutivo", "árvore filogenética"])

BIKE = (tit("Texto para as questões 28 a 30.") + p("As bicicletas possuem uma corrente que liga uma coroa dentada dianteira, movimentada pelos pedais, a uma coroa localizada no eixo da roda traseira, como mostra a figura.", "O número de voltas dadas pela roda traseira a cada pedalada depende do tamanho relativo destas coroas.") + "[[fig:1]]")
F_BIKE = ("q28", "Desenho de uma bicicleta vista de lado, com a corrente ligando a coroa dos pedais à coroa da roda traseira.")
X(28, "N", "Física", "Transmissão de movimento", "<p>A corrente percorre o mesmo comprimento nas duas coroas. Quanto maior a coroa dos pedais e menor a da roda traseira, mais voltas a roda dá a cada pedalada. Em A, a coroa dos pedais é grande e a traseira é a menor de todas. Alternativa <strong>A</strong>.</p>",
  BIKE + p("Em que opção abaixo a roda traseira dá o <strong>maior</strong> número de voltas por pedalada?"),
  figs(F_BIKE, ("q28a", "Bicicleta com coroa dos pedais grande e coroa traseira bem pequena."), ("q28b", "Bicicleta com coroa dos pedais e coroa traseira de tamanho parecido, ambas médias."),
       ("q28c", "Bicicleta com coroa dos pedais média, quase do tamanho da traseira."), ("q28d", "Bicicleta com coroa dos pedais pequena e coroa traseira grande."), ("q28e", "Bicicleta com coroa dos pedais média e coroa traseira pequena, mas não tanto quanto em A.")),
  ["coroa e catraca", "polias"], alts=ALT(2))
X(29, "N", "Física", "Transmissão de movimento", "<p>A coroa dos pedais tem 30 cm de diâmetro e a traseira, 10 cm: a cada pedalada, a roda traseira dá 30/10 = 3 voltas. A roda tem 80 cm de diâmetro (raio 0,4 m), e cada volta percorre 2 × 3 × 0,4 = 2,4 m. Em 3 voltas: 7,2 m. Alternativa <strong>C</strong>.</p><p>2,4 m (B) seria uma única volta da roda.</p>",
  BIKE + p("Quando se dá uma pedalada na bicicleta abaixo (isto é, quando a coroa acionada pelos pedais dá uma volta completa), qual é a distância aproximada percorrida pela bicicleta, sabendo-se que o comprimento de um círculo de raio R é igual a 2πR, onde π ≈ 3?") + "[[fig:2]]",
  figs(F_BIKE, ("q29", "Bicicleta com as medidas indicadas: roda traseira de 80 cm de diâmetro, coroa traseira de 10 cm e coroa dos pedais de 30 cm.")), ["comprimento da circunferência", "polias"])
X(30, "N", "Física", "Transmissão de movimento", "<p>I está correta: 2 coroas dianteiras × 5 traseiras = 10 combinações. III também: na subida, coroa dianteira pequena com traseira grande dá menos voltas da roda por pedalada, mas exige menos força. II é falsa: em alta velocidade, convém a dianteira grande com a traseira pequena, para a roda dar mais voltas a cada pedalada. Alternativa <strong>A</strong>.</p>",
  BIKE + p("Com relação ao funcionamento de uma bicicleta de marchas, onde cada marcha é uma combinação de uma das coroas dianteiras com uma das coroas traseiras, são formuladas as seguintes afirmativas:")
  + I3("numa bicicleta que tenha duas coroas dianteiras e cinco traseiras, temos um total de dez marchas possíveis onde cada marcha representa a associação de uma das coroas dianteiras com uma das traseiras.", "em alta velocidade, convém acionar a coroa dianteira de maior raio com a coroa traseira de maior raio também.", "em uma subida íngreme, convém acionar a coroa dianteira de menor raio e a coroa traseira de maior raio.")
  + p("Entre as afirmações acima, estão corretas:"), figs(F_BIKE), ["marchas", "princípio multiplicativo"])

DNA = (tit("Texto para as questões 31 e 32.") + p("João ficou intrigado com a grande quantidade de notícias envolvendo DNA: clonagem da ovelha Dolly, terapia gênica, testes de paternidade, engenharia genética, etc. Para conseguir entender as notícias, estudou a estrutura da molécula de DNA e seu funcionamento e analisou os dados do quadro a seguir.")
  + tabela(["", "Quadro"], [["I", "A T C C G G A T G C T T<br>T A G G C C T A C G A A"], ["II", "A T C C G G A T G C T T<br>⇓<br>U A G G C C U A C G A A"], ["III", "U A G G C C U A C G A A<br>⇓<br>Metionina Alanina Leucina Glutamato"], ["IV", "Bases nitrogenadas: A = Adenina; T = Timina; C = Citosina; G = Guanina; U = Uracila"]]))
X(31, "N", "Biologia", "DNA", "<p>No DNA, A pareia com T e C com G. Se A = 40%, T = 40%. Sobram 20% para C e G, divididos igualmente: C = 10% e G = 10%. Alternativa <strong>D</strong>.</p><p>A soma das quatro bases é sempre 100%, e as quantidades de bases que pareiam entre si são sempre iguais.</p>",
  DNA + p("Analisando-se o DNA de um animal, detectou-se que 40% de suas bases nitrogenadas eram constituídas por Adenina. Relacionando esse valor com o emparelhamento específico das bases, os valores encontrados para as outras bases nitrogenadas foram:"),
  tags=["pareamento de bases", "porcentagem"])
X(32, "N", "Biologia", "DNA", "<p>Em I, o DNA aparece com duas cadeias, cada uma com uma sequência de bases nitrogenadas. Alternativa <strong>A</strong>.</p><p>A complementação é sempre A–T e C–G (B é falsa); a quantidade de A numa cadeia é igual à de T na outra, não à de A (C); o DNA tem 4 tipos de bases, porque U só existe no RNA (D); e na mitose cada DNA forma 2 moléculas, não 4 (E).</p>",
  DNA + p("Em <strong>I</strong> está representado o trecho de uma molécula de DNA. Observando o quadro, pode-se concluir que:"), tags=["estrutura do DNA"])

CAMOES = (tit("Texto para as questões 33 e 34.") + ap("<em>Amor é fogo que arde sem se ver;<br>é ferida que dói e não se sente;<br>é um contentamento descontente;<br>é dor que desatina sem doer;</em>", "<em>É um não querer mais que bem querer;<br>é solitário andar por entre a gente;<br>é nunca contentar-se de contente;<br>é cuidar que se ganha em se perder;</em>",
  "<em>É querer estar preso por vontade;<br>é servir a quem vence, o vencedor;<br>é ter com quem nos mata lealdade.</em>", "<em>Mas como causar pode seu favor<br>nos corações humanos amizade,<br>se tão contrário a si é o mesmo Amor?</em>") + fonte("Luís de Camões"))
X(33, "L", "Literatura", "Figuras de linguagem", "<p>Em “É um contentamento descontente”, as palavras “contentamento” e “descontente” se opõem diretamente: é a antítese mais clara. Alternativa <strong>B</strong>.</p><p>Em A também há contradição (arder sem se ver), mas não entre termos opostos; D e E não trazem palavras de sentido contrário.</p>",
  CAMOES + p("O poema tem, como característica, a figura de linguagem denominada antítese, relação de oposição de palavras ou idéias. Assinale a opção em que essa oposição se faz claramente presente."), tags=["Camões", "antítese"])
X(34, "L", "Literatura", "Gêneros textuais", "<p>O soneto tenta definir o amor por uma sequência de afirmações (“Amor é...”) e termina com uma pergunta que conclui o raciocínio: como algo tão contraditório pode gerar amizade? É um texto argumentativo. Alternativa <strong>A</strong>.</p><p>Não conta uma história (B), não narra feitos heroicos (C) e não foi escrito para encenação (E).</p>",
  CAMOES + p("O poema pode ser considerado como um texto:"), tags=["Camões", "tipologia textual"])

X(35, "N", "Química", "Poluição do ar", "<p>Qualidade “péssima” corresponde a 30 a 40 ppm de CO. Pela tabela de sintomas, acima de 15 ppm há diminuição da capacidade visual, e dores de cabeça só a partir de 60 ppm. Nesse nível, a pessoa poderia ter a visão alterada. Alternativa <strong>B</strong>.</p>",
  p("Um dos índices de qualidade do ar diz respeito à concentração de monóxido de carbono (CO), pois esse gás pode causar vários danos à saúde. A tabela abaixo mostra a relação entre a qualidade do ar e a concentração de CO.")
  + tabela(["Qualidade do ar", "Concentração de CO – ppm* (média de 8h)"], [["Inadequada", "15 a 30"], ["Péssima", "30 a 40"], ["Crítica", "Acima de 40"]])
  + fonte("* ppm (parte por milhão) = 1 micrograma de CO por grama de ar (10<sup>−6</sup> g)")
  + p("Para analisar os efeitos do CO sobre os seres humanos, dispõe-se dos seguintes dados:")
  + tabela(["Concentração de CO (ppm)", "Sintomas em seres humanos"], [["10", "Nenhum"], ["15", "Diminuição da capacidade visual"], ["60", "Dores de cabeça"], ["100", "Tonturas, fraqueza muscular"], ["270", "Inconsciência"], ["800", "Morte"]])
  + p("Suponha que você tenha lido em um jornal que na cidade de São Paulo foi atingido um péssimo nível de qualidade do ar. Uma pessoa que estivesse nessa área poderia:"),
  tags=["monóxido de carbono", "leitura de tabela"])

X(36, "M", "Matemática", "Porcentagem", "<p>Homens: 32% de 250 = 80; na 1ª série, 40% de 80 = 32 (d). Na 3ª série há 20% de 250 = 50 alunos, 10 homens (f) e 40 mulheres (c). Homens na 2ª: 80 − 32 − 10 = 38 (e), e as mulheres da 2ª são também 38 (b). Mulheres no total: 250 − 80 = 170, logo a = 170 − 38 − 40 = 92. Alternativa <strong>C</strong>.</p>",
  p("Uma escola de ensino médio tem 250 alunos que estão matriculados na 1ª, 2ª ou 3ª série. 32% dos alunos são homens e 40% dos homens estão na 1ª série. 20% dos alunos matriculados estão na 3ª série, sendo 10 alunos homens. Dentre os alunos da 2ª série, o número de mulheres é igual ao número de homens.", "A tabela abaixo pode ser preenchida com as informações dadas:")
  + tabela(["", "1ª", "2ª", "3ª", "Total"], [["Mulher", "a", "b", "c", "a+b+c"], ["Homem", "d", "e", "f", "d+e+f"], ["<strong>Total</strong>", "a+d", "b+e", "c+f", "250"]])
  + p("O valor de <strong><u>a</u></strong> é:"),
  tags=["porcentagem", "tabela de dupla entrada"])

LAGOA = (tit("Texto para as questões 37 a 39.") + p("Em uma aula de Biologia, o seguinte texto é apresentado:")
  + ap("<strong>LAGOA AZUL ESTÁ DOENTE</strong>", "<em>Os vereadores da pequena cidade de Lagoa Azul estavam discutindo a situação da Saúde no Município. A situação era mais grave com relação a três doenças: Doença de Chagas, Esquistossomose e Ascaridíase (lombriga). Na tentativa de prevenir novos casos, foram apresentadas várias propostas:</em>")
  + "<ul><li><strong>Proposta 1:</strong> Promover uma campanha de vacinação.</li><li><strong>Proposta 2:</strong> Promover uma campanha de educação da população com relação a noções básicas de higiene, incluindo fervura de água.</li><li><strong>Proposta 3:</strong> Construir rede de saneamento básico.</li><li><strong>Proposta 4:</strong> Melhorar as condições de edificação das moradias e estimular o uso de telas nas portas e janelas e mosquiteiros de filó.</li><li><strong>Proposta 5:</strong> Realizar campanha de esclarecimento sobre os perigos de banhos nas lagoas.</li><li><strong>Proposta 6:</strong> Aconselhar o uso controlado de inseticidas.</li><li><strong>Proposta 7:</strong> Drenar e aterrar as lagoas do município.</li></ul>")
X(37, "N", "Biologia", "Esquistossomose", "<p>O saneamento básico (3) impede que as fezes dos doentes cheguem à água e contaminem o caramujo; e evitar banhos nas lagoas (5) impede que as larvas que saem do caramujo penetrem na pele das pessoas. Alternativa <strong>E</strong>.</p><p>Não existe vacina contra a esquistossomose (1), e o verme não é transmitido por inseto (4, 6).</p>",
  LAGOA + p("Em relação à Esquistossomose, a situação é complexa, pois o ciclo de vida do verme que causa a doença tem vários estágios, incluindo a existência de um hospedeiro intermediário, um caramujo aquático que é contaminado pelas fezes das pessoas doentes. Analisando as medidas propostas, o combate à doença terá sucesso se forem implementadas:"),
  tags=["esquistossomose", "saneamento"], alts=dict(D[37], E="3 e 5, pois prevenirão a contaminação do hospedeiro intermediário pelas fezes das pessoas doentes e a contaminação de pessoas sãs por águas contaminadas."))
X(38, "N", "Biologia", "Ascaridíase", "<p>A lombriga é transmitida pela ingestão de ovos presentes em água e alimentos contaminados por fezes. A rede de saneamento básico (3) corta essa contaminação para toda a população, com o maior benefício social. Alternativa <strong>B</strong>.</p>",
  LAGOA + p("Para o combate da Ascaridíase, a proposta que trará maior benefício social, se implementada pela Prefeitura, será:"), tags=["ascaridíase", "saneamento"])
X(39, "N", "Biologia", "Doença de Chagas", "<p>O barbeiro vive em frestas de casas de pau a pique e pica à noite. Melhorar as moradias e usar telas e mosquiteiros (4) e controlar o inseto com inseticidas (6) são as medidas mais efetivas. Alternativa <strong>C</strong>.</p><p>Não há vacina contra a doença de Chagas (1), e saneamento não atinge o barbeiro (3).</p>",
  LAGOA + p("Você sabe que a Doença de Chagas é causada por um protozoário (<em>Trypanosoma cruzi</em>) transmitido por meio da picada de insetos hematófagos (barbeiros). Das medidas propostas no texto “A Lagoa Azul Está Doente”, as mais efetivas na prevenção dessa doença são:"),
  tags=["doença de Chagas", "barbeiro"])

X(40, "H", "História", "Era Vargas", "<p>Vargas teve faces diferentes ao longo de quinze anos: medidas nacionalistas e trabalhistas, mas também a ditadura do Estado Novo e alianças com as elites. Cada grupo toma uma parte dessas características, muitas vezes ligadas a um momento, como se fosse a postura definitiva. Os dois erram por parcialidade. Alternativa <strong>E</strong>.</p>",
  ap("<em>A figura de Getúlio Vargas, como personagem histórica, é bastante polêmica, devido à complexidade e à magnitude de suas ações como presidente do Brasil durante um longo período de quinze anos (1930-1945). Foram anos de grandes e importantes mudanças para o país e para o mundo. Pode-se perceber o destaque dado a Getúlio Vargas pelo simples fato de este período ser conhecido no Brasil como a “Era Vargas”.</em>",
     "<em>Entretanto, Vargas não é visto de forma favorável por todos. Se muitos o consideram como um fervoroso nacionalista, um progressista ativo e o “Pai dos Pobres”, existem outros tantos que o definem como ditador oportunista, um intervencionista e amigo das elites.</em>")
  + p("Provavelmente você percebeu que as duas opiniões sobre Vargas são opostas, defendendo valores praticamente antagônicos. As diferentes interpretações do papel de uma personalidade histórica podem ser explicadas, conforme uma das opções abaixo. Assinale-a."),
  tags=["Getúlio Vargas", "interpretação histórica"])

JURU = (tit("Texto para as questões 41 e 42.") + p("Alunos de uma escola no Rio de Janeiro são convidados a participar de uma excursão ao Parque Nacional de Jurubatiba. Antes do passeio, eles lêem o trecho de uma reportagem publicada em uma revista:")
  + ap("<em>“Jurubatiba será o primeiro parque nacional em área de restinga, num braço de areia com 31 quilômetros de extensão, formado entre o mar e dezoito lagoas. Numa área de 14.000 hectares, ali vivem jacarés, capivaras, lontras, tamanduás-mirins, além de milhares de aves e de peixes de água doce e salgada. Os peixes de água salgada, na época das cheias, passam para as lagoas, onde encontram abrigo, voltando ao mar na cheia seguinte. Nos terrenos mais baixos, próximos aos lençóis freáticos, as plantas têm água suficiente para agüentar longas secas. Já nas áreas planas, os cactos são um dos poucos vegetais que proliferam, pintando o areal com um verde pálido.”</em>"))
X(41, "N", "Biologia", "Adaptações vegetais", "<p>Nas áreas planas e arenosas da restinga, sem acesso ao lençol freático, as plantas que sobrevivem, como os cactos, têm adaptações contra a perda de água: caules e folhas com cutícula espessa. Alternativa <strong>C</strong>.</p><p>Muitas folhas (A) aumentariam a perda de água, e no areal não há árvores frondosas (E).</p>",
  JURU + p("Depois de ler o texto, os alunos podem supor que, em Jurubatiba, os vegetais que sobrevivem nas áreas planas têm características tais como:"), tags=["restinga", "xeromorfismo"])
X(42, "N", "Biologia", "Classificação dos animais", "<p>O texto cita jacarés (répteis), capivaras, lontras e tamanduás-mirins (mamíferos), aves e peixes. São mamíferos, répteis, peixes e aves. Alternativa <strong>D</strong>.</p><p>Não há anfíbios citados (B, C), e a classificação de A deixa de fora os jacarés.</p>",
  JURU + p("O texto anterior cita alguns exemplos de animais que vivem em Jurubatiba e podem ser classificados como:"), tags=["vertebrados", "classificação"])

X(43, "H", "Geografia", "Exclusão social", "<p>O texto liga desemprego, analfabetismo, falta de moradia e migrações repetidas. Os trabalhadores sem qualificação, com menos acesso ao emprego formal, são os que engrossam as fileiras dos excluídos. Alternativa <strong>D</strong>.</p><p>O desemprego não se explica só pelo aumento da população (A), e a exclusão atinge sobretudo quem não tem qualificação (B, E).</p>",
  p("Depois de estudar as migrações, no Brasil, você lê o seguinte texto:")
  + ap("<em>O Brasil, por suas características de crescimento econômico, e apesar da crise e do retrocesso das últimas décadas, é classificado como um país moderno. Tal conceito pode ser, na verdade, questionado se levarmos em conta os indicadores sociais: o grande número de desempregados, o índice de analfabetismo, o déficit de moradia, o sucateamento da saúde, enfim, a avalanche de brasileiros envolvidos e tragados num processo de repetidas migrações (...)</em>")
  + fonte("(adap. VALIN, 1996, pág. 50. <em>Migrações: da perda de terra à exclusão social</em>. SP, Atual, 1996)") + p("Analisando os indicadores citados no texto, você pode afirmar que:"),
  tags=["migrações", "mão de obra"])
X(44, "H", "Geografia", "Globalização", "<p>A globalização concentra investimentos e tecnologia nos países ricos e nos trabalhadores qualificados; nos países subdesenvolvidos, ela agrava o desemprego e a desigualdade, provocando “exclusão social”. Alternativa <strong>D</strong>.</p><p>Ela não reduz o fluxo migratório (A) nem aumenta o crescimento populacional (B), e beneficia os países industrializados (C).</p>",
  p("Um dos fenômenos mais discutidos e polêmicos da atualidade é a “Globalização”, a qual impacta de forma negativa:"), tags=["globalização", "exclusão social"])

GLOBAL = (tit("Texto para as questões 45 e 46.") + p("Você está fazendo uma pesquisa sobre a globalização e lê a seguinte passagem, em um livro:")
  + ap("<strong>A SOCIEDADE GLOBAL</strong>", "<em>As pessoas se alimentam, se vestem, moram, se comunicam, se divertem, por meio de bens e serviços mundiais, utilizando mercadorias produzidas pelo capitalismo mundial, globalizado. Suponhamos que você vá com seus amigos comer Big Mac e tomar Coca-Cola no Mc Donald’s. Em seguida, assiste a um filme de Steven Spielberg e volta para casa num ônibus de marca Mercedes. Ao chegar em casa, liga seu aparelho de TV Philips para ver o videoclip de Michael Jackson e, em seguida, deve ouvir um CD do grupo Simply Red, gravado pela BMG Ariola Discos em seu equipamento AIWA. Veja quantas empresas transnacionais estiveram presentes nesse seu curto programa de algumas horas.</em>")
  + fonte("Adap. PRAXEDES et alli, 1997. <em>O MERCOSUL</em>. SP, Ed. Ática, 1997."))
X(45, "H", "Geografia", "Globalização", "<p>Com o mesmo lanche, os mesmos filmes, músicas e marcas em toda parte, a cultura das transnacionais vai apagando hábitos e particularidades locais: o capitalismo globalizado tende a eliminar as particularidades culturais dos povos. Alternativa <strong>A</strong>.</p><p>As transnacionais do texto vêm de culturas diferentes, como Estados Unidos, Alemanha, Holanda e Japão (E), e a globalização atinge o mundo todo (D).</p>",
  GLOBAL + p("Com base no texto e em seus conhecimentos de Geografia e História, marque a resposta correta."), tags=["homogeneização cultural", "transnacionais"])
X(46, "H", "Geografia", "Globalização", "<p>O texto mostra a globalização econômica e cultural ao mesmo tempo (II), trata filmes, programas de TV e música como produtos de consumo (IV), e as empresas citadas têm sede nos EUA, na Europa Ocidental e no Japão (V). Alternativa <strong>B</strong>.</p><p>A globalização não garante acesso a todos (I) e tende a reduzir a diversidade de costumes (III).</p>",
  GLOBAL + p("A leitura do texto ajuda você a compreender que:")
  + '<ol type="I"><li>a globalização é um processo ideal para garantir o acesso a bens e serviços para toda a população.</li><li>a globalização é um fenômeno econômico e, ao mesmo tempo, cultural.</li><li>a globalização favorece a manutenção da diversidade de costumes.</li><li>filmes, programas de TV e música são mercadorias como quaisquer outras.</li><li>as sedes das empresas transnacionais mencionadas são os EUA, Europa Ocidental e Japão.</li></ol>'
  + p("Destas afirmativas estão corretas:"), tags=["globalização", "indústria cultural"])

BARC = (tit("Texto para as questões 47 a 49.") + p("Seguem abaixo alguns trechos de uma matéria da revista “Superinteressante”, que descreve hábitos de um morador de Barcelona (Espanha), relacionando-os com o consumo de energia e efeitos sobre o ambiente.")
  + I3("“Apenas no banho matinal, por exemplo, um cidadão utiliza cerca de 50 litros de água, que depois terá que ser tratada. Além disso, a água é aquecida consumindo 1,5 quilowatt-hora (cerca de 1,3 milhões de calorias), e para gerar essa energia foi preciso perturbar o ambiente de alguma maneira....”",
       "“Na hora de ir para o trabalho, o percurso médio dos moradores de Barcelona mostra que o carro libera 90 gramas do venenoso monóxido de carbono e 25 gramas de óxidos de nitrogênio ... Ao mesmo tempo, o carro consome combustível equivalente a 8,9 kWh.”",
       "“Na hora de recolher o lixo doméstico... quase 1 kg por dia. Em cada quilo há aproximadamente 240 gramas de papel, papelão e embalagens; 80 gramas de plástico; 55 gramas de metal; 40 gramas de material biodegradável e 80 gramas de vidro.”"))
X(47, "N", "Química", "Tratamento de água", "<p>A água usada no banho vai para o esgoto e, para voltar ao consumo, passa por tratamento: decantação para separar partículas, filtração, cloração para eliminar microrganismos e, em alguns casos, fluoretação. Alternativa <strong>D</strong>.</p><p>Destilação (B) é cara demais em grande escala, e o sabão não impede o tratamento (E).</p>",
  BARC + p("No trecho I, a matéria faz referência ao tratamento necessário à água resultante de um banho. As afirmações abaixo dizem respeito a tratamentos e destinos dessa água. Entre elas, a mais plausível é a de que a água:"),
  tags=["tratamento de água", "decantação e filtração"])
X(48, "N", "Física", "Efeito Joule", "<p>No chuveiro elétrico, a corrente passa pela resistência e a energia elétrica se transforma em energia térmica (efeito Joule), que aquece a água. Alternativa <strong>C</strong>.</p><p>Não há etapa mecânica (B), e a energia elétrica pode vir de várias fontes, não necessariamente do petróleo (E).</p>",
  BARC + p("Também com relação ao trecho I, supondo a existência de um chuveiro elétrico, pode-se afirmar que:"), tags=["chuveiro elétrico", "efeito Joule"])
X(49, "N", "Química", "Combustão", "<p>O monóxido de carbono se forma quando a combustão é incompleta, por falta de oxigênio suficiente para formar só CO<sub>2</sub>. Alternativa <strong>A</strong>.</p><p>Carros a álcool também produzem CO (B), e os óxidos de nitrogênio vêm justamente dos motores (D).</p>",
  BARC + p("Com referência ao trecho II, pode-se afirmar que:"), tags=["combustão incompleta", "monóxido de carbono"])

TV = (tit("Texto para as questões 50 e 51.") + p("Uma pesquisa de opinião foi realizada para avaliar os níveis de audiência de alguns canais de televisão, entre 20h e 21h, durante uma determinada noite.", "Os resultados obtidos estão representados no gráfico de barras abaixo:") + "[[fig:1]]")
F_TV = figs(("q50", "Gráfico de barras do número de residências por canal: TvA cerca de 32, TvB cerca de 30, TvC cerca de 20, TvD cerca de 100 e nenhum canal cerca de 15."))
X(50, "M", "Matemática", "Leitura de gráficos", "<p>Somando as barras: cerca de 32 + 30 + 20 + 100 + 15 ≈ 197, aproximadamente 200 residências. Alternativa <strong>D</strong>.</p><p>Quem não assistia a nenhum canal também foi entrevistado e entra na conta.</p>",
  TV + p("O número de residências atingidas nessa pesquisa foi <strong><u>aproximadamente</u></strong> de:"), F_TV, ["gráfico de barras"])
X(51, "M", "Matemática", "Porcentagem", "<p>A TvB tem cerca de 30 residências de um total de cerca de 200: 30/200 = 15%. Alternativa <strong>A</strong>.</p><p>30% (E) seria confundir o número de residências da TvB com a porcentagem, esquecendo que o total é cerca de 200, e não 100.</p>",
  TV + p("A percentagem de entrevistados que declararam estar assistindo à TvB é <strong><u>aproximadamente</u></strong> igual a:"), F_TV, ["porcentagem", "gráfico de barras"])

CHUVA = tit("Texto para as questões 52 e 53.") + p("Um dos problemas ambientais decorrentes da industrialização é a poluição atmosférica. Chaminés altas lançam ao ar, entre outros materiais, o dióxido de enxofre (SO<sub>2</sub>) que pode ser transportado por muitos quilômetros em poucos dias. Dessa forma, podem ocorrer precipitações ácidas em regiões distantes, causando vários danos ao meio ambiente (chuva ácida).")
X(52, "N", "Química", "Chuva ácida", "<p>A chuva ácida ataca o carbonato de cálcio do mármore (I) e da pedra-sabão das esculturas do Aleijadinho (II), e também corrói metais como o ferro e o alumínio (III). Pode agir nas três obras. Alternativa <strong>E</strong>.</p>",
  CHUVA + p("Um dos danos ao meio ambiente diz respeito à corrosão de certos materiais. Considere as seguintes obras:")
  + I3("monumento Itamarati - Brasília (mármore).", "esculturas do Aleijadinho - MG (pedra sabão, contém carbonato de cálcio).", "grades de ferro ou alumínio de edifícios.") + p("A ação da chuva ácida pode acontecer em:"),
  tags=["corrosão", "carbonatos"])
X(53, "N", "Química", "Chuva ácida", "<p>I e II estão corretas: a chuva ácida baixa o pH de lagos, matando espécies sensíveis, e acidifica o solo, prejudicando plantas. III é falsa: chuva ácida tem pH <em>menor</em> que o da água destilada, e não maior. Alternativa <strong>C</strong>.</p>",
  CHUVA + p("Com relação aos efeitos sobre o ecossistema, pode-se afirmar que:")
  + I3("as chuvas ácidas poderiam causar a diminuição do pH da água de um lago, o que acarretaria a morte de algumas espécies, rompendo a cadeia alimentar.", "as chuvas ácidas poderiam provocar acidificação do solo, o que prejudicaria o crescimento de certos vegetais.", "as chuvas ácidas causam danos se apresentarem valor de pH maior que o da água destilada.")
  + p("Dessas afirmativas está(ão) correta(s):"), tags=["pH", "acidificação"])

X(54, "H", "Geografia", "Climogramas", "<p>A afirmativa está certa: dois lugares com totais anuais de chuva parecidos podem ter climas bem diferentes se num deles as chuvas se concentram em poucos meses e no outro se espalham pelo ano. Distribuição e total pluviométrico juntos definem as condições de umidade. Alternativa <strong>B</strong>.</p><p>A distribuição das chuvas sozinha não define o clima (E), porque a temperatura também importa.</p>",
  p("As figuras abaixo representam a variação anual de temperatura e a quantidade de chuvas mensais em dado lugar, sendo chamados de climogramas. Neste tipo de gráfico, as temperaturas são representadas pelas linhas, e as chuvas pelas colunas.") + "[[fig:1]]"
  + p("Leia e analise.", "<strong>A distribuição das chuvas no decorrer do ano, conforme mostrado nos gráficos, é um parâmetro importante na caracterização de um clima.</strong>", "A esse respeito podemos dizer que a afirmativa:"),
  figs(("q54", "Dois climogramas, de janeiro a dezembro, com temperatura (12 a 28 °C, linha) e chuva (0 a 400 mm, colunas). Climograma 1: temperatura alta o ano todo, entre cerca de 23 e 27 °C; chuvas concentradas entre março e junho, com até cerca de 160 mm, e quase nada no resto do ano. Climograma 2: temperatura com grande variação, de cerca de 25 °C no verão a cerca de 13 °C no inverno; chuvas bem distribuídas, em torno de 100 a 150 mm todos os meses.")),
  ["climograma", "regime de chuvas"])

DEPO = (tit("Texto para as questões 55 e 56.") + p("Em uma disputa por terras, em Mato Grosso do Sul, dois depoimentos são colhidos: o do proprietário de uma fazenda e o de um integrante do Movimento dos Trabalhadores Rurais sem Terras:")
  + ap("<strong>Depoimento 1</strong>", "<em>“A minha propriedade foi conseguida com muito sacrifício pelos meus antepassados. Não admito invasão. Essa gente não sabe de nada. Estão sendo manipulados pelos comunistas. Minha resposta será à bala. Esse povo tem que saber que a Constituição do Brasil garante a propriedade privada. Além disso, se esse governo quiser as minhas terras para a Reforma Agrária terá que pagar, em dinheiro, o valor que eu quero.”</em> — proprietário de uma fazenda no Mato Grosso do Sul.",
       "<strong>Depoimento 2</strong>", "<em>“Sempre lutei muito. Minha família veio para a cidade porque fui despedido quando as máquinas chegaram lá na Usina. Seu moço, acontece que eu sou um homem da terra. Olho pro céu, sei quando é tempo de plantar e de colher. Na cidade não fico mais. Eu quero um pedaço de terra, custe o que custar. Hoje eu sei que não estou sozinho. Aprendi que a terra tem um valor social. Ela é feita para produzir alimento. O que o homem come vem da terra. O que é duro é ver que aqueles que possuem muita terra e não dependem dela para sobreviver, pouco se preocupam em produzir nela.”</em> — integrante do Movimento dos Trabalhadores Rurais Sem Terra (MST), de Corumbá – MS."))
X(55, "H", "Geografia", "Questão agrária", "<p>O proprietário invoca a Constituição, que garante a propriedade privada (I), diz que os sem-terra são manipulados pelos comunistas (II) e que a terra foi conquistada com sacrifício dos antepassados (III). Ele não diz que o problema depende só da justiça (IV): ameaça responder à bala. Alternativa <strong>D</strong>.</p>",
  DEPO + p("A partir da leitura do depoimento 1, os argumentos utilizados para <u>defender a posição do proprietário de terras</u> são:")
  + I4("A Constituição do país garante o direito à propriedade privada, portanto, invadir terras é crime.", "O MST é um movimento político controlado por partidos políticos.", "As terras são o fruto do árduo trabalho das famílias que as possuem.", "Este é um problema político e depende unicamente da decisão da justiça.")
  + p("Estão corretas as proposições:"), tags=["reforma agrária", "argumentação"])
X(56, "H", "Geografia", "Questão agrária", "<p>O argumento do trabalhador para ter direito à terra é que ela tem valor social, deve produzir alimento e ser de quem trabalha nela, e não de quem a acumula sem produzir (II). A mecanização (IV) aparece no depoimento como parte da sua história pessoal, e não como argumento para defender a sua posição. Alternativa <strong>B</strong>.</p><p>Ele não diz que a distribuição está sendo resolvida (I) e defende, e não suprime, o valor social da terra (III).</p>",
  DEPO + p("A partir da leitura do depoimento 2, quais os argumentos utilizados para <u>defender a posição de um trabalhador rural sem terra</u>?")
  + I4("A distribuição mais justa da terra no país está sendo resolvida, apesar de que muitos ainda não têm acesso a ela.", "A terra é para quem trabalha nela e não para quem a acumula como bem material.", "É necessário que se suprima o valor social da terra.", "A mecanização do campo acarreta a dispensa de mão-de-obra rural.")
  + p("Estão corretas as proposições:"), tags=["função social da terra", "argumentação"])

X(57, "N", "Biologia", "Ecologia", "<p>Sem predadores, os veados cresceram até cerca de 100 mil, devastaram as pastagens pelo consumo e pelo pisoteio, e os filhotes morreram de fome (IV). A predação, que mantinha a população equilibrada com os recursos, era um fator positivo para a população como um todo (III). Alternativa <strong>E</strong>.</p><p>I inventa predadores sem base no gráfico, e II é falsa: a fome matou mais que a predação.</p>",
  p("No início deste século, com a finalidade de possibilitar o crescimento da população de veados no planalto de Kaibab, no Arizona (EUA), moveu-se uma caçada impiedosa aos seus predadores – pumas, coiotes e lobos. No gráfico abaixo, a linha cheia indica o crescimento real da população de veados, no período de 1905 a 1940; a linha pontilhada indica a expectativa quanto ao crescimento da população de veados, nesse mesmo período, caso o homem não tivesse interferido em Kaibab.")
  + "[[fig:1]]" + fonte("Extraído de AMABIS &amp; MARTHO, <em>Fundamentos de Psicologia Moderna</em>, pág. 42")
  + p("Para explicar o fenômeno que ocorreu com a população de veados após a interferência do homem, o mesmo estudante elaborou as seguintes hipóteses e/ou conclusões:")
  + I4("lobos, pumas e coiotes não eram, certamente, os únicos e mais vorazes predadores dos veados; quando estes predadores, até então desapercebidos, foram favorecidos pela eliminação de seus competidores, aumentaram numericamente e quase dizimaram a população de veados.", "a falta de alimentos representou para os veados um mal menor que a predação.",
       "ainda que a atuação dos predadores pudesse representar a morte para muitos veados, a predação demonstrou-se um fator positivo para o equilíbrio dinâmico e sobrevivência da população como um todo.", "a morte dos predadores acabou por permitir um crescimento exagerado da população de veados, isto levou à degradação excessiva das pastagens, tanto pelo consumo excessivo como pelo seu pisoteamento.")
  + p("O estudante, desta vez, acertou se indicou as alternativas:"),
  figs(("q57", "Gráfico do número de veados de 1905 a 1940. Com a proibição da caça e a eliminação dos predadores, a população sobe de cerca de 4 mil para cerca de 100 mil por volta de 1924; os primeiros filhotes morrem de fome e depois 60% dos filhotes morrem; a população despenca para 40 mil, 30 mil e 20 mil por volta de 1930 e chega a 10 mil em 1939. A linha pontilhada, a expectativa sem interferência, fica estável em torno de 30 mil a 40 mil.")),
  ["predação", "capacidade de suporte"])

X(58, "H", "História", "Cidadania", "<p>Em 1879, um deputado negou que os escravos fossem brasileiros; mais de um século depois, um projeto precisa transformar meninos de rua “de pivetes em cidadãos”. A cidadania continua incompleta para milhões de brasileiros. Alternativa <strong>D</strong>.</p><p>A abolição não trouxe cidadania plena aos ex-escravos (B), e cidadania vai além do voto (E).</p>",
  p("Você está estudando o abolicionismo no Brasil e ficou perplexo ao ler o seguinte documento:")
  + ap("<strong>Texto 1</strong> — <em>Discurso do deputado baiano Jerônimo Sodré Pereira – Brasil 1879</em>", "<em>No dia 5 de março de 1879, o deputado baiano Jerônimo Sodré Pereira, discursando na Câmara, afirmou que era preciso que o poder público olhasse para a condição de um milhão de brasileiros, que jazem ainda no cativeiro. Nessa altura do discurso foi aparteado por um deputado que disse: “BRASILEIROS, <u>NÃO</u>”.</em>")
  + p("Em seguida, você tomou conhecimento da existência do Projeto Axé (Bahia), nos seguintes termos:")
  + ap("<strong>Texto 2</strong> — <em>Projeto Axé, Lição de cidadania – 1998 – Brasil</em>", "<em>Na língua africana Iorubá, axé significa força mágica. Em Salvador, Bahia, o Projeto Axé conseguiu fazer, em apenas três anos, o que sucessivos governos não foram capazes: a um custo dez vezes inferior ao de projetos governamentais, ajuda meninos e meninas de rua a construírem projetos de vida, transformando-os de pivetes em cidadãos.</em>",
       "<em>A receita do Axé é simples: competência pedagógica, administração eficiente, respeito pelo menino, incentivo, formação e bons salários para os educadores. Criado em 1991 pelo advogado e pedagogo italiano Cesare de Florio La Rocca, o Axé atende hoje a mais de duas mil crianças e adolescentes.</em>",
       "<em>A cultura afro, forte presença na Bahia, dá o tom do Projeto Erê (entidade criança do candomblé), a parte cultural do Axé. Os meninos participam da banda mirim do Olodum, do Ilé Ayê e de outros blocos, jogam capoeira e têm um grupo de teatro.</em>", "<em>Todas as atividades são remuneradas. Além da bolsa semanal, as crianças têm alimentação, uniforme e vale-transporte.</em>")
  + p("Com a leitura dos dois textos, você descobriu que a cidadania:"),
  tags=["escravidão", "cidadania"])

CORRIDA = tit("Texto para as questões 59 e 60.") + p("Em uma prova de 100 m rasos, o desempenho típico de um corredor padrão é representado pelo gráfico a seguir:") + "[[fig:1]]"
F_COR = figs(("q59", "Gráfico da velocidade (0 a 12 m/s) em função do tempo (0 a 16 s): a velocidade sobe rapidamente de 0 a cerca de 8 m/s no primeiro segundo e a cerca de 10 m/s em 2 s; chega a cerca de 10,7 m/s por volta de 4 s e fica praticamente constante até cerca de 9 s; depois cai devagar e, de 12 a 15 s, cai mais rápido, até cerca de 5,5 m/s."))
X(59, "N", "Física", "Cinemática", "<p>Entre 5 e 8 segundos, a curva é praticamente horizontal, por volta de 10,7 m/s: a velocidade é aproximadamente constante. Alternativa <strong>C</strong>.</p><p>De 0 a 5 s o corredor acelera, e de 12 a 15 s a velocidade cai.</p>",
  CORRIDA + p("Baseado no gráfico, em que intervalo de tempo a <strong><u>velocidade</u></strong> do corredor é aproximadamente constante?"), F_COR, ["velocidade", "leitura de gráfico"])
X(60, "N", "Física", "Cinemática", "<p>A aceleração é a taxa de variação da velocidade: no gráfico, a inclinação da curva. A curva é mais íngreme logo na largada, entre 0 e 1 segundo, quando a velocidade sobe de 0 a cerca de 6 m/s. Alternativa <strong>A</strong>.</p>",
  CORRIDA + p("Em que intervalo de tempo o corredor apresenta <strong><u>aceleração</u></strong> máxima?"), F_COR, ["aceleração", "inclinação do gráfico"])

X(61, "H", "Geografia", "América Latina", "<p>O próprio texto afirma que a América Latina se insere num processo de democratização, com algumas oportunidades de crescimento econômico-social. Alternativa <strong>E</strong>.</p><p>Cuba é apresentada como exceção, com restrições à liberdade (A, C).</p>",
  p("A América Latina dos últimos anos insere-se num processo de democratização, oferecendo algumas oportunidades de crescimento econômico-social num contexto de liberdade e dependência econômica internacional. Cuba continua caracterizada por uma organização própria com restrições à liberdade econômica e política, crescimento em alguns aspectos sociais e um embargo econômico americano datado de 1962. Em 1998, o Papa João Paulo II visitou Cuba e depois disse ao cardeal Jaime Ortega, arcebispo de Havana, e a 13 bispos em visita ao Vaticano que apreciou as mudanças realizadas em Cuba após sua visita à ilha e espera que sejam criados novos espaços legais e sociais, para que a sociedade civil de Cuba possa crescer em autonomia e participação. A resposta internacional ao intercâmbio com Cuba foi boa, mas as autoridades locais mostraram pouco entusiasmo, não estando dispostas a abandonar o sistema socialista monopartidário.",
    "A maioria dos países latino-americanos tem se envolvido, nos últimos anos, em processos de formação socioeconômicos caracterizados por:"),
  tags=["redemocratização", "Cuba"])

X(62, "N", "Química", "Ebulição", "<p>Quanto maior a altitude, menor a pressão atmosférica (tabela), e a água ferve quando sua pressão de vapor iguala essa pressão, o que acontece a uma temperatura mais baixa (gráfico). O Pico da Neblina, o lugar mais alto, tem a menor temperatura de ebulição. Alternativa <strong>C</strong>.</p><p>Natal, ao nível do mar, tem a maior temperatura de ebulição (B).</p>",
  p("A tabela a seguir registra a pressão atmosférica em diferentes altitudes, e o gráfico relaciona a pressão de vapor da água em função da temperatura")
  + tabela(["Altitude (km)", "Pressão atmosférica (mmHg)"], [["0", "760"], ["1", "600"], ["2", "480"], ["4", "300"], ["6", "170"], ["8", "120"], ["10", "100"]]) + "[[fig:1]]"
  + p("Um líquido, num frasco aberto, entra em ebulição a partir do momento em que a sua pressão de vapor se iguala à pressão atmosférica. Assinale a opção correta, considerando a tabela, o gráfico e os dados apresentados, sobre as seguintes cidades:")
  + tabela(["Cidade", "Altitude"], [["Natal (RN)", "nível do mar"], ["Campos do Jordão (SP)", "1628 m"], ["Pico da Neblina (RR)", "3014 m"]]) + p("A temperatura de ebulição será:"),
  figs(("q62", "Gráfico da pressão de vapor da água (0 a 800 mmHg) em função da temperatura (0 a 120 °C): a curva cresce cada vez mais rápido, passando por cerca de 150 mmHg a 60 °C, 360 a 80 °C, 530 a 90 °C e 760 a 100 °C.")),
  ["pressão de vapor", "altitude"])

X(63, "N", "Química", "pH", "<p>Os alunos mediram pH entre 4,5 e 6,0: a solução é ácida. Dobrando o volume com água, a concentração de H<sup>+</sup> cai pela metade e o pH sobe um pouco (cerca de 0,3), mas a solução continua ácida, abaixo de 7. Os novos valores devem ficar entre 5 e 7. Alternativa <strong>C</strong>.</p><p>Diluir não deixa a solução mais ácida (A, D) nem a torna neutra (E).</p>",
  p("O pH informa a acidez ou a basicidade de uma solução. A escala abaixo apresenta a natureza e o pH de algumas soluções e da água pura, a 25 °C.") + "[[fig:1]]"
  + p("Uma solução desconhecida estava sendo testada no laboratório por um grupo de alunos. Esses alunos decidiram que deveriam medir o pH dessa solução como um dos parâmetros escolhidos na identificação da solução. Os resultados obtidos estão na tabela abaixo.")
  + tabela(["Aluno", "Valor de pH"], [["Carlos", "4,5"], ["Gustavo", "5,5"], ["Simone", "5,0"], ["Valéria", "6,0"], ["Paulo", "4,5"], ["Wagner", "5,0"], ["Renata", "5,0"], ["Rodrigo", "5,5"], ["Augusta", "5,0"], ["Eliane", "5,5"]])
  + p("Da solução testada pelos alunos, o professor retirou 100 ml e adicionou água até completar 200 ml de solução diluída. O próximo grupo de alunos a medir o pH deverá encontrar para o mesmo:"),
  figs(("q63", "Escala de pH de 0 a 14: ácido de 0 a 7, neutro em 7, básico de 7 a 14. Suco de limão, cerca de 2; saliva, cerca de 6 a 7; água pura, 7; clara de ovo, cerca de 8; sabão, cerca de 12.")),
  ["pH", "diluição"], alts=dict(D[63], E="sempre o valor 7."))

completar(Q, R)
