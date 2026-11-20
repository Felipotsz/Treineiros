# Enem 1999 (data não confirmada; dataExame omitida), Prova 1 – amarela: prova única de 63 questões (modelo antigo, sem divisão por áreas).
# Fonte do PDF: arquivo 'Prova_Caderno_Amarelo_1999' do usuário (rodapé "AMARELA"; redação sobre cidadania e participação social, com o tema de protagonismo juvenil).
# Gabarito: cópia do gabarito oficial (Ministério da Educação/Inep, Prova 1 – Amarela) no acervo da USP: GABARITO_ENEM_1999_AMARELA.pdf, lido duas vezes.
# Uma coluna; números "01".."63" em Arial-Bold: extrator com LINHAS=1 NXR=26-34 YMIN=40 YMAX=805. O número fica um pouco abaixo da primeira linha do
# enunciado, então a primeira linha de cada questão aparece no fim da anterior no texto extraído; os enunciados foram montados à mão.
# Protegidos como imagem: Vinicius de Moraes (Q1) e os poemas da Q48 (Drummond, Chico Buarque, Adélia Prado), estes renderizados em letra maior.
# Em texto: citações em prosa (Machado, Faoro, Aurélio, Augusto dos Anjos, Copérnico, Leonardo, Aluísio Azevedo, Rubem Braga, Drummond em prosa, João Cabral em prosa).
import sys, pathlib, re, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar

ID = "enem-1999"
META = {"id": ID, "banca": "Enem", "ano": 1999, "titulo": "Enem 1999: Prova objetiva", "fonte": "Inep",
        "duracaoMinutos": 300, "area": "Prova objetiva (63 questões)", "caderno": "amarelo", "dia": 1, "fonteGabarito": {"oficial": True, "nome": "gabarito oficial do Inep, em cópia guardada pelo Instituto de Física da USP", "url": "https://fep.if.usp.br/~profis/arquivo/avaliacao/enem/provas_gabaritos/1999/GABARITO_ENEM_1999_AMARELA.pdf"}}
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
# A primeira linha de cada questão sai colada na alternativa E da anterior: corta-se E no fim verdadeiro.
CORTE = {1: "(Aurélio)", 2: "5", 3: "dano ambiental.", 5: "2 000 anos.", 6: "escalas diferentes.", 8: "respectivamente.", 9: "III e IV",
         10: "fé e razão.", 11: "II e III são corretas.", 13: "EUA e a URSS.", 14: "alaranjado de metila.", 15: "II e III são plausíveis.",
         17: "financeiros americanos.", 18: "pelos dois grupos.", 19: "68 pontos.", 20: "5", 21: "5", 22: "desenvolvimento.”", 23: "educação melhor!”",
         24: "ao lado OR.", 25: "100%", 26: "Meridiano de Greenwich.", 27: "Boa Vista.", 28: "Z, W e Y.", 31: "autoridade e da tradição.",
         32: "panelas comuns.", 33: "não varia.", 34: "ciclo da água.", 37: "II e III estão corretas.", 38: "atingido anteriormente.", 39: "I e III",
         40: "atividades rurais.", 41: "Sobradinho.", 42: "convencer o leitor.", 44: "para pasto”.", 45: "nem energia térmica.", 46: "o seu comércio.",
         47: "não aumenta mais.", 48: "ausência de recursos.", 49: "capitais européias.", 51: "menor durabilidade.", 54: "dos decompositores.",
         55: "I e III são adequadas.", 57: "ebulição alta.", 58: "próximas da superfície.", 60: "Segunda Guerra Mundial."}
for _n, _fim in CORTE.items():
    _e = D[_n]["E"]; D[_n]["E"] = re.sub(r"\s+", " ", _e[:_e.index(_fim) + len(_fim)]).strip()
D[5]["C"] = "1 000 anos."
D[12]["E"] = "5 meses."
D[8]["E"] = "em II e III, indica reflexividade e equivale a “a si mesma” e “a si mesmas”, respectivamente."
D[56] = {k: v.replace("seta x", "seta ①").replace("seta y", "seta ②").replace("momento x", "momento ①").replace("momento y", "momento ②") for k, v in D[56].items()}
D[56]["E"] = "o controle de pragas por meio do uso de inseticidas é muito mais eficaz que o controle biológico, pois os seus efeitos são muito mais rápidos e têm maior durabilidade."
I4 = lambda *xs: '<ol type="I"><li>' + "</li><li>".join(xs) + "</li></ol>"

X(1, "L", "Língua Portuguesa", "Semântica", "<p>Em “Que mesmo em face do maior encanto”, “mesmo” é advérbio com sentido de “até”, “ainda”: mesmo diante do maior encanto. Em C, “mesmo em doses variáveis” tem o mesmo valor: o remédio não fez efeito nem com doses variáveis. Alternativa <strong>C</strong>.</p><p>Em A e B, “mesmo” é adjetivo (“as mesmas ruas”, “o mesmo contraste”, igual); em D e E, significa “realmente”, “de fato”.</p>",
  "[[fig:1]]" + fonte("(MORAES, Vinícius de. <em>Antologia poética</em>. São Paulo: Cia das Letras, 1992)")
  + p("A palavra <strong>mesmo</strong> pode assumir diferentes significados, de acordo com a sua função na frase. Assinale a alternativa em que o sentido de <strong>mesmo</strong> equivale ao que se verifica no 3º verso da 1ª estrofe do poema de Vinícius de Moraes."),
  figs(("q01", "“Soneto de fidelidade”, de Vinicius de Moraes, em quatro estrofes: o eu lírico promete ser atento ao amor antes de tudo, mesmo diante de outro encanto, e vivê-lo em cada momento, na alegria e na tristeza; quando vierem a morte ou a solidão, quer poder dizer que o amor não foi imortal, por ser chama, mas foi infinito enquanto durou. O 3º verso da 1ª estrofe diz que, mesmo em face do maior encanto, o pensamento se encante mais pelo amor.")),
  ["Vinicius de Moraes", "advérbio"],
  alts=A5("“Pai, para onde fores, / irei também trilhando as <strong>mesmas</strong> ruas...” (Augusto dos Anjos)", "“Agora, como outrora, há aqui o <strong>mesmo</strong> contraste da vida interior, que é modesta, com a exterior, que é ruidosa.” (Machado de Assis)",
          "“Havia o mal, profundo e persistente, para o qual o remédio não surtiu efeito, <strong>mesmo</strong> em doses variáveis.” (Raimundo Faoro)", "“Mas, olhe cá, Mana Glória, há <strong>mesmo</strong> necessidade de fazê-lo padre?” (Machado de Assis)",
          "“Vamos de qualquer maneira, mas vamos <strong>mesmo</strong>.” (Aurélio)"))

X(2, "M", "Matemática", "Raciocínio lógico", "<p>Aldo só conhece os telefones de Beto e Dino. Quem conhece o de Carlos? Só Ênio (e o próprio Carlos). Beto conhece Dino, e Dino conhece Ênio. O caminho mais curto é Aldo → Dino → Ênio → Carlos: Aldo liga para Dino, Dino liga para Ênio e Ênio liga para Carlos. São 3 telefonemas. Alternativa <strong>C</strong>.</p>",
  p("Vinte anos depois da formatura, cinco colegas de turma decidem organizar uma confraternização. Para marcar o dia e o local da confraternização, precisam comunicar-se por telefone. Cada um conhece o telefone de alguns colegas e desconhece o de outros. No quadro abaixo, o número 1 indica que o colega da linha correspondente conhece o telefone do colega da coluna correspondente; o número 0 indica que o colega da linha não conhece o telefone do colega da coluna. Exemplo: Beto sabe o telefone do Dino que não conhece o telefone do Aldo.")
  + tabela(["", "Aldo", "Beto", "Carlos", "Dino", "Ênio"], [["<strong>Aldo</strong>", "1", "1", "0", "1", "0"], ["<strong>Beto</strong>", "0", "1", "0", "1", "0"], ["<strong>Carlos</strong>", "1", "0", "1", "1", "0"], ["<strong>Dino</strong>", "0", "0", "0", "1", "1"], ["<strong>Ênio</strong>", "1", "1", "1", "1", "1"]])
  + p("O número <strong>mínimo</strong> de telefonemas que Aldo deve fazer para se comunicar com Carlos é:"),
  tags=["grafos", "leitura de tabela"])

TERRA = (tit("Texto para as questões 3 a 5.") + ap("Se compararmos a idade do planeta Terra, avaliada em quatro e meio bilhões de anos (4,5 × 10<sup>9</sup> anos), com a de uma pessoa de 45 anos, então, quando começaram a florescer os primeiros vegetais, a Terra já teria 42 anos. Ela só conviveu com o homem moderno nas últimas quatro horas e, há cerca de uma hora, viu-o começar a plantar e a colher. Há menos de um minuto percebeu o ruído de máquinas e de indústrias e, como denuncia uma ONG de defesa do meio ambiente, foi nesses últimos sessenta segundos que se produziu todo o lixo do planeta!"))
X(3, "N", "Biologia", "Tempo geológico", "<p>Na escala, a industrialização ocupa só o último minuto de uma vida de 45 anos, e mesmo assim produziu todo o lixo do planeta. O texto quer mostrar a rapidez e o tamanho inédito do dano ambiental causado pela indústria. Alternativa <strong>E</strong>.</p><p>A agricultura surgiu muito depois dos vegetais (A), e o ser humano não causou todas as transformações da Terra (C).</p>",
  TERRA + p("O texto acima, ao estabelecer um paralelo entre a idade da Terra e a de uma pessoa, pretende mostrar que"), tags=["escala de tempo", "impacto ambiental"])
X(4, "M", "Matemática", "Proporção", "<p>A escala transforma 4,5 bilhões de anos em 45 anos: cada ano “da pessoa” vale 100 milhões de anos. Uma hora é 1/8.760 de ano, ou seja, cerca de 100.000.000/8.760 ≈ 11.400 anos reais. A agricultura começou há cerca de 10 000 anos. Alternativa <strong>D</strong>.</p>",
  TERRA + p("O texto permite concluir que a agricultura começou a ser praticada há cerca de"), tags=["escala", "regra de três"])
X(5, "M", "Matemática", "Proporção", "<p>Na escala, 4,5 × 10<sup>9</sup> anos reais correspondem a 45 anos: a razão é 10<sup>8</sup>. Então 15 × 10<sup>9</sup> anos reais correspondem a 15 × 10<sup>9</sup>/10<sup>8</sup> = 150 anos. Alternativa <strong>B</strong>.</p><p>O Universo tem pouco mais de três vezes a idade da Terra: 3,3 × 45 ≈ 150.</p>",
  TERRA + p("Na teoria do <em>Big Bang</em>, o Universo surgiu há cerca de 15 bilhões de anos, a partir da explosão e expansão de uma densíssima gota. De acordo com a escala proposta no texto, essa teoria situaria o início do Universo há cerca de"),
  tags=["escala", "notação científica"])

X(6, "M", "Matemática", "Gráficos", "<p>Os dois gráficos mostram os mesmos dados: de 2.000 para 2.200 linhas, 200 linhas novas. No gráfico I, o eixo vertical tem escala comprimida e a subida parece pequena; no II, o eixo começa em 2.000 e é esticado, e a subida parece enorme. A diferença está só na escolha das escalas. Alternativa <strong>D</strong>.</p><p>Nenhum dos dois está errado (B, C), e eles podem ser comparados lendo os valores (E).</p>",
  p("Para convencer a população local da ineficiência da Companhia Telefônica Vilatel na expansão da oferta de linhas, um político publicou no jornal local o gráfico I, abaixo representado. A Companhia Vilatel respondeu publicando dias depois o gráfico II, onde pretende justificar um grande aumento na oferta de linhas. O fato é que, no período considerado, foram instaladas, efetivamente, 200 novas linhas telefônicas.")
  + "[[fig:1]]" + p("Analisando os gráficos, pode-se concluir que"),
  figs(("q06", "Dois gráficos do número total de linhas telefônicas de janeiro a dezembro, ambos de 2.000 a 2.200 linhas. No gráfico I, o eixo vertical é curto e vai de 0 a 2.200: a linha sobe pouco. No gráfico II, o eixo vertical começa em 2.000 e é bem alto: a mesma subida, passando por 2.050 em abril e 2.150 em agosto, parece muito íngreme.")),
  ["escala", "leitura de gráfico"])

X(7, "L", "Língua Portuguesa", "Interpretação de texto", "<p>Rui não aceita a ideia de “carreira meteórica” (“Nada disso”), mas reconhece que a medalha é “algo a mais para oferecer” na concorrência por emprego. E diz que as coisas mudam rápido e ele não sabe qual será sua profissão: é difícil prever o mercado de trabalho. Ele concorda só em parte. Alternativa <strong>E</strong>.</p>",
  p("Leia o texto abaixo.")
  + ap("<em>Cabelos longos, brinco na orelha esquerda, físico de skatista. Na aparência, o estudante brasiliense Rui Lopes Viana Filho, de 16 anos, não lembra em nada o estereótipo dos gênios. Ele não usa pesados óculos de grau e está longe de ter um ar introspectivo. No final do mês passado, Rui retornou de Taiwan, onde enfrentou 419 competidores de todo o mundo na 39ª Olimpíada Internacional de Matemática. A reluzente medalha de ouro que ele trouxe na bagagem está dependurada sobre a cama de seu quarto, atulhado de rascunhos dos problemas matemáticos que aprendeu a decifrar nos últimos cinco anos.</em>",
       "<strong>Veja</strong> – Vencer uma olimpíada serve de passaporte para uma carreira profissional meteórica?",
       "<strong>Rui</strong> – Nada disso. Decidi me dedicar à Olimpíada porque sei que a concorrência por um emprego é cada vez mais selvagem e cruel. Agora tenho algo a mais para oferecer. O problema é que as coisas estão mudando muito rápido e não sei qual será minha profissão. Além de ser muito novo para decidir sobre o meu futuro profissional, sei que esse conceito de carreira mudou muito.")
  + fonte("(Entrevista de Rui Lopes Viana Filho à <em>Veja</em>, 05/08/1998, n.31, p. 9-10)")
  + p("Na pergunta, o repórter estabelece uma relação entre a entrada do estudante no mercado de trabalho e a vitória na Olimpíada. O estudante"),
  tags=["entrevista", "argumentação"])

X(8, "L", "Língua Portuguesa", "Pronomes", "<p>Em I, “as pessoas se amam muito mais” no Natal tem sentido recíproco (umas às outras). Em II, Susanita responde “você também se ama muito mais”, com sentido reflexivo (a si mesma). Em III, Mafalda passa a duvidar: as pessoas se amam “a si mesmas” no Natal, também reflexivo. Alternativa <strong>E</strong>.</p>",
  "[[fig:1]]" + fonte("(QUINO. <em>Mafalda inédita</em>. São Paulo: Martins Fontes, 1993)")
  + p("Observando as falas das personagens, analise o emprego do pronome <strong>SE</strong> e o sentido que adquire no contexto. No contexto da narrativa, é correto afirmar que o pronome <strong>SE</strong>,"),
  figs(("q08", "Tira da Mafalda, de Quino, em três quadros. I: Mafalda diz “Eu gosto do Natal porque as pessoas se amam muito mais”, e Susanita pergunta “Ah!... Você também sente isso?”. II: Susanita diz “Como fico feliz! Quer dizer que você também se ama muito mais no Natal? Eu, então, você nem imagina o quanto eu me amo no Natal!”. III: Mafalda, pensativa, se pergunta “Por que será que as pessoas se amam muito mais no Natal?”.")),
  ["pronome se", "reciprocidade"])

X(9, "N", "Química", "Reações ácido-base", "<p>A calagem tem duas etapas: a cal reage com a água e forma hidróxido de cálcio, CaO + H<sub>2</sub>O → Ca(OH)<sub>2</sub> (II); depois o hidróxido neutraliza os íons H<sup>+</sup> do solo, formando água e deixando Ca<sup>2+</sup>: Ca(OH)<sub>2</sub> + 2H<sup>+</sup> → Ca<sup>2+</sup> + 2H<sub>2</sub>O (III). Alternativa <strong>C</strong>.</p><p>I forma um composto que não existe, Ca(OH)<sub>3</sub>, e IV é desbalanceada e faz o caminho inverso.</p>",
  p("Suponha que um agricultor esteja interessado em fazer uma plantação de girassóis. Procurando informação, leu a seguinte reportagem:")
  + ap("<strong>Solo ácido não favorece plantio</strong>", "<em>Alguns cuidados devem ser tomados por quem decide iniciar o cultivo do girassol. A oleaginosa deve ser plantada em solos descompactados, com pH acima de 5,2 (que indica menor acidez da terra). Conforme as recomendações da Embrapa, o agricultor deve colocar, por hectare, 40 kg a 60 kg de nitrogênio, 40 kg a 80 kg de potássio e 40 kg a 80 kg de fósforo.</em>",
       "<em>O pH do solo, na região do agricultor, é de 4,8. Dessa forma, o agricultor deverá fazer a “calagem”.</em>")
  + fonte("(<em>Folha de S. Paulo</em>, 25/09/1996)")
  + p("Suponha que o agricultor vá fazer calagem (aumento do pH do solo por adição de cal virgem – CaO). De maneira simplificada, a diminuição da acidez se dá pela interação da cal (CaO) com a água presente no solo, gerando hidróxido de cálcio (Ca(OH)<sub>2</sub>), que reage com os íons H<sup>+</sup> (dos ácidos), ocorrendo, então, a formação de água e deixando íons Ca<sup>2+</sup> no solo.", "Considere as seguintes equações:")
  + I4("CaO + 2H<sub>2</sub>O → Ca(OH)<sub>3</sub>", "CaO + H<sub>2</sub>O → Ca(OH)<sub>2</sub>", "Ca(OH)<sub>2</sub> + 2H<sup>+</sup> → Ca<sup>2+</sup> + 2H<sub>2</sub>O", "Ca(OH)<sub>2</sub> + H<sup>+</sup> → CaO + H<sub>2</sub>O")
  + p("O processo de calagem descrito acima pode ser representado pelas equações:"),
  tags=["calagem", "neutralização"], alts=A5("I e II", "I e IV", "II e III", "II e IV", "III e IV"))

X(10, "H", "Filosofia", "Fé e razão", "<p>A encíclica quer uma razão “mais segura e perspicaz com o apoio que recebe da fé”, e São Tomás afirma que as verdades da razão não contradizem as da fé. Os dois textos buscam conciliar fé e razão. Alternativa <strong>E</strong>.</p><p>Não há contradição entre eles (A), e Tomás não punha a razão acima da fé (B).</p>",
  p("Considere os textos abaixo.")
  + ap("<em>(...) de modo particular, quero encorajar os crentes empenhados no campo da filosofia para que iluminem os diversos âmbitos da atividade humana, graças ao exercício de uma razão que se torna mais segura e perspicaz com o apoio que recebe da fé.</em>")
  + fonte("(Papa João Paulo II. <em>Carta Encíclica Fides et Ratio aos bispos da igreja católica sobre as relações entre fé e razão</em>, 1998)")
  + ap("<em>As verdades da razão natural não contradizem as verdades da fé cristã.</em>") + fonte("(São Tomás de Aquino - pensador medieval)")
  + p("Refletindo sobre os textos, pode-se concluir que"),
  tags=["São Tomás de Aquino", "escolástica"])

X(11, "N", "Física", "Dilatação térmica", "<p>Com o calor, a gasolina se dilata: o mesmo litro tem menos massa. Abastecer com a temperatura mais baixa dá mais massa por litro (II está correta, e I está errada). Vendendo por quilograma, a dilatação não mudaria a quantidade comprada (III está correta). Alternativa <strong>E</strong>.</p>",
  p("A gasolina é vendida por litro, mas em sua utilização como combustível, a massa é o que importa. Um aumento da temperatura do ambiente leva a um aumento no volume da gasolina. Para diminuir os efeitos práticos dessa variação, os tanques dos postos de gasolina são subterrâneos. Se os tanques <strong>não</strong> fossem subterrâneos:")
  + I3("Você levaria vantagem ao abastecer o carro na hora mais quente do dia pois estaria comprando mais massa por litro de combustível.", "Abastecendo com a temperatura mais baixa, você estaria comprando mais massa de combustível para cada litro.", "Se a gasolina fosse vendida por kg em vez de por litro, o problema comercial decorrente da dilatação da gasolina estaria resolvido.")
  + p("Destas considerações, somente"),
  tags=["dilatação", "densidade"])

X(12, "N", "Física", "Energia elétrica", "<p>Cada quilograma de alumínio consome 20 kWh na produção. Para 10 kg: 200 kWh. Como a casa consome 100 kWh por mês, essa energia daria para 2 meses. Alternativa <strong>B</strong>.</p><p>Os dados sobre a produção nacional e o lixo não entram na conta.</p>",
  p("O alumínio se funde a 666 °C e é obtido à custa de energia elétrica, por eletrólise – transformação realizada a partir do óxido de alumínio a cerca de 1 000 °C.")
  + ap("<em>A produção brasileira de alumínio, no ano de 1985, foi da ordem de 550 000 toneladas, tendo sido consumidos cerca de 20 kWh de energia elétrica por quilograma do metal. Nesse mesmo ano, estimou-se a produção de resíduos sólidos urbanos brasileiros formados por metais ferrosos e não-ferrosos em 3 700 t/dia, das quais 1,5% estima-se corresponder ao alumínio.</em>")
  + fonte("([Dados adaptados de] FIGUEIREDO, P. J. M. <em>A sociedade do lixo: resíduos, a questão energética e a crise ambiental</em>. Piracicaba: UNIMEP, 1994)")
  + p("Suponha que uma residência tenha objetos de alumínio em uso cuja massa total seja de 10 kg (panelas, janelas, latas etc.). O consumo de energia elétrica mensal dessa residência é de 100 kWh. Sendo assim, na produção desses objetos utilizou-se uma quantidade de energia elétrica que poderia abastecer essa residência por um período de"),
  tags=["kWh", "alumínio"])

X(13, "H", "História", "Fim da Guerra Fria", "<p>O texto cita a derrubada do Muro de Berlim, a reunificação alemã, a libertação dos países da Cortina de Ferro e o fim da União Soviética: estruturas do mundo dividido em dois blocos. A “desmontagem das estruturas do passado” é o fim da Guerra Fria. Alternativa <strong>A</strong>.</p>",
  p("Em dezembro de 1998, um dos assuntos mais veiculados nos jornais era o que tratava da moeda única européia. Leia a notícia destacada abaixo.")
  + ap("<em>O nascimento do Euro, a moeda única a ser adotada por onze países europeus a partir de 1º de janeiro, é possivelmente a mais importante realização deste continente nos últimos dez anos que assistiu à derrubada do Muro de Berlim, à reunificação das Alemanhas, à libertação dos países da Cortina de Ferro e ao fim da União Soviética. Enquanto todos esses eventos têm a ver com a desmontagem de estruturas do passado, o Euro é uma ousada aposta no futuro e uma prova da vitalidade da sociedade Européia. A “Euroland”, região abrangida por Alemanha, Áustria, Bélgica, Espanha, Finlândia, França, Holanda, Irlanda, Itália, Luxemburgo e Portugal, tem um PIB (Produto Interno Bruto) equivalente a quase 80% do americano, 289 milhões de consumidores e responde por cerca de 20% do comércio internacional. Com este cacife, o Euro vai disputar com o dólar a condição de moeda hegemônica.</em>")
  + fonte("(<em>Gazeta Mercantil</em>, 30/12/1998)") + p("A matéria refere-se à “desmontagem das estruturas do passado” que pode ser entendida como"),
  tags=["Guerra Fria", "euro"])

ROTULO = (tit("Texto para as questões 14 e 15.") + p("As informações abaixo foram extraídas do rótulo da água mineral de determinada fonte.")
  + tabela(["ÁGUA MINERAL NATURAL", ""], [["<strong>Composição química provável em mg/L</strong>", ""], ["Sulfato de estrôncio", "0,04"], ["Sulfato de cálcio", "2,29"], ["Sulfato de potássio", "2,16"], ["Sulfato de sódio", "65,71"],
       ["Carbonato de sódio", "143,68"], ["Bicarbonato de sódio", "42,20"], ["Cloreto de sódio", "4,07"], ["Fluoreto de sódio", "1,24"], ["Vanádio", "0,07"],
       ["<strong>Características físico-químicas</strong>", ""], ["pH a 25 °C", "10,00"], ["Temperatura da água na fonte", "24 °C"], ["Condutividade elétrica", "4,40 × 10<sup>−4</sup> ohms/cm"], ["Resíduo de evaporação a 180 °C", "288,00 mg/L"],
       ["<strong>Classificação</strong>", "“Alcalino-bicarbonatada, fluoretada, vanádica”"]])
  + p("Indicadores <strong>ácido base</strong> são substâncias que em solução aquosa apresentam cores diferentes conforme o pH da solução.", "O quadro abaixo fornece as cores que alguns indicadores apresentam à temperatura de 25 °C")
  + tabela(["Indicador", "Cores conforme o pH"], [["Azul de bromotimol", "amarelo em pH ≤ 6,0; azul em pH ≥ 7,6"], ["Vermelho de metila", "vermelho em pH ≤ 4,8; amarelo em pH ≥ 6,0"], ["Fenolftaleína", "incolor em pH ≤ 8,2; vermelho em pH ≥ 10,0"], ["Alaranjado de metila", "vermelho em pH ≤ 3,2; amarelo em pH ≥ 4,4"]]))
X(14, "N", "Química", "Indicadores", "<p>A água mineral tem pH 10; a de torneira, entre 6,5 e 7,5. A fenolftaleína fica vermelha em pH 10 e incolor na água de torneira. O azul de bromotimol fica azul em pH 10 e amarelo ou verde (intermediário) na de torneira. Os dois revelam a fraude. Alternativa <strong>A</strong>.</p><p>Vermelho de metila e alaranjado de metila ficam amarelos nas duas águas e não distinguem uma da outra.</p>",
  ROTULO + p("Suponha que uma pessoa inescrupulosa guardou garrafas vazias dessa água mineral, enchendo-as com água de torneira (pH entre 6,5 e 7,5) para serem vendidas como água mineral. Tal fraude pode ser facilmente comprovada pingando-se na “água mineral fraudada”, à temperatura de 25 °C, gotas de"),
  tags=["indicador ácido-base", "pH"])
X(15, "N", "Química", "Água mineral", "<p>A composição da água mineral vem dos minerais das rochas por onde ela passa: o vanádio vem da dissolução de minerais desse elemento (I). Uma broca não liberaria vanádio continuamente na água (II), e a água mineral não pode receber aditivos (III). Alternativa <strong>A</strong>.</p>",
  ROTULO + p("As seguintes explicações foram dadas para a presença do elemento vanádio na água mineral em questão")
  + I3("No seu percurso até chegar à fonte, a água passa por rochas contendo minerais de vanádio, dissolvendo-os.", "Na perfuração dos poços que levam aos depósitos subterrâneos da água, utilizaram-se brocas constituídas de ligas cromo-vanádio.", "Foram adicionados compostos de vanádio à água mineral.")
  + p("Considerando todas as informações do rótulo, pode-se concluir que apenas"),
  tags=["água mineral", "dissolução"])

X(16, "N", "Química", "Substâncias do cotidiano", "<p>Água sanitária é solução de hipoclorito de sódio (III); fermento em pó tem bicarbonato de sódio, que libera gás carbônico (IV); solução fisiológica é cloreto de sódio a 0,9% (I). Alternativa <strong>C</strong>.</p>",
  p("A água do mar pode ser fonte de materiais utilizados pelo ser humano, como os exemplificados no esquema abaixo.")
  + "<ul><li>Da água do mar se obtém o <strong>cloreto de sódio (I)</strong>.</li><li>Do cloreto de sódio se obtêm o cloro, a <strong>soda cáustica (II)</strong> e o carbonato de sódio.</li><li>Do cloro e da soda cáustica se obtém o <strong>hipoclorito de sódio (III)</strong>.</li><li>Do carbonato de sódio se obtém o <strong>bicarbonato de sódio (IV)</strong>.</li></ul>"
  + p("Os materiais I, II, III e IV existem como principal constituinte ativo de produtos de uso rotineiro. A alternativa que associa corretamente <strong>água sanitária</strong>, <strong>fermento em pó</strong> e <strong>solução fisiológica</strong> com os materiais obtidos da água do mar é:"),
  tags=["sais", "hipoclorito"],
  alts=A5("Água sanitária: II; fermento em pó: III; solução fisiológica: IV.", "Água sanitária: III; fermento em pó: I; solução fisiológica: IV.", "Água sanitária: III; fermento em pó: IV; solução fisiológica: I.",
          "Água sanitária: II; fermento em pó: III; solução fisiológica: I.", "Água sanitária: I; fermento em pó: IV; solução fisiológica: III."))

X(17, "L", "Língua Portuguesa", "Gêneros textuais", "<p>O artigo relembra a crise de 1929 num momento em que o Brasil vivia uma crise financeira iminente: o jornalista usa o passado para iluminar o presente, relacionando os fatos. Alternativa <strong>D</strong>.</p><p>Os dados de desemprego e do PIB americano são meios, e não o objetivo do texto (B, E).</p>",
  p("Leia um texto publicado no jornal <em>Gazeta Mercantil</em>. Esse texto é parte de um artigo que analisa algumas situações de crise no mundo, entre elas, a quebra da Bolsa de Nova Iorque em 1929, e foi publicado na época de uma iminente crise financeira no Brasil.")
  + ap("<em>Deu no que deu. No dia 29 de outubro de 1929, uma terça-feira, praticamente não havia compradores no pregão de Nova Iorque, só vendedores. Seguiu-se uma crise incomparável: o Produto Interno Bruto dos Estados Unidos caiu de 104 bilhões de dólares em 1929, para 56 bilhões em 1933, coisa inimaginável em nossos dias. O valor do dólar caiu a quase metade. O desemprego elevou-se de 1,5 milhão para 12,5 milhões de trabalhadores – cerca de 25% da população ativa – entre 1929 e 1933. A construção civil caiu 90%. Nove milhões de aplicações, tipo caderneta de poupança, perderam-se com o fechamento dos bancos. Oitenta e cinco mil firmas faliram. Houve saques e norte-americanos que passaram fome.</em>")
  + fonte("(<em>Gazeta Mercantil</em>, 05/01/1999)") + p("Ao citar dados referentes à crise ocorrida em 1929, em um artigo jornalístico atual, pode-se atribuir ao jornalista a seguinte intenção:"),
  tags=["crise de 1929", "intencionalidade"])

X(18, "N", "Biologia", "Saúde pública", "<p>A tabela mostra que a mortalidade infantil é maior nas regiões com mais famílias pobres e mais analfabetismo (Nordeste) e menor onde esses índices são baixos (Sul e Sudeste). Isso apoia a ideia do segundo grupo, de que a saúde depende das condições socioeconômicas. A tabela não traz dados sobre agentes biológicos ou químicos. Alternativa <strong>B</strong>.</p>",
  p("A tabela abaixo apresenta dados referentes à mortalidade infantil, à porcentagem de famílias de baixa renda com crianças menores de 6 anos e às taxas de analfabetismo das diferentes regiões brasileiras e do Brasil como um todo.")
  + tabela(["Região", "Mortalidade infantil*", "Famílias pobres**", "Analfab.***"],
           [["Norte", "35,6", "34,5", "12,7"], ["Nordeste", "59,0", "54,9", "29,4"], ["Sul", "22,5", "22,4", "8,3"], ["Sudeste", "25,2", "18,9", "8,6"], ["Centro-Oeste", "25,4", "25,5", "12,4"], ["<strong>Brasil</strong>", "<strong>36,7</strong>", "<strong>31,8</strong>", "<strong>14,7</strong>"]])
  + fonte("Fonte: <em>Folha de S. Paulo</em>, 11/03/99. * A mortalidade infantil indica o número de crianças que morrem antes de completar um ano de idade para cada grupo de 1.000 crianças que nasceram vivas. ** Famílias de baixa renda com crianças menores de 6 anos (em %). *** Taxa de analfabetismo em maiores de 15 anos (em %).")
  + p("Suponha que um grupo de alunos recebeu a tarefa de pesquisar fatores que interferem na manutenção da saúde ou no desenvolvimento de doenças. O primeiro grupo deveria colher dados que apoiassem a idéia de que combatendo-se agentes biológicos e químicos garante-se a saúde. Já o segundo grupo deveria coletar informações que reforçassem a idéia de que a saúde de um indivíduo está diretamente relacionada à sua condição socioeconômica.",
      "Os dados da tabela podem ser utilizados apropriadamente para"),
  tags=["mortalidade infantil", "condições socioeconômicas"])

X(19, "M", "Matemática", "Raciocínio lógico", "<p>A: 1º lugar para 14 eleitores (10 + 4), 2º para 5 (2 + 3), 3º para 14 (7 + 7): 42 + 10 + 14 = 66 pontos. B: 1º para 9, 2º para 17, 3º para 7: 27 + 34 + 7 = 68. C: 1º para 10, 2º para 11, 3º para 12: 30 + 22 + 12 = 64. B é eleito com 68 pontos. Alternativa <strong>C</strong>.</p><p>A teria mais votos em 1º lugar, mas perde pela pontuação.</p>",
  p("Imagine uma eleição envolvendo 3 candidatos A, B, C e 33 eleitores (votantes). Cada eleitor vota fazendo uma ordenação dos três candidatos. Os resultados são os seguintes:")
  + tabela(["Ordenação", "Nº de votantes"], [["A B C", "10"], ["A C B", "04"], ["B A C", "02"], ["B C A", "07"], ["C A B", "03"], ["C B A", "07"], ["<strong>Total de votantes</strong>", "<strong>33</strong>"]])
  + p("A primeira linha do quadro descreve que 10 eleitores escolheram A em 1º lugar, B em 2º lugar, C em 3º lugar e assim por diante.", "Considere o sistema de eleição no qual cada candidato ganha 3 pontos quando é escolhido em 1º lugar, 2 pontos quando é escolhido em 2º lugar e 1 ponto se é escolhido em 3º lugar. O candidato que acumular mais pontos é eleito. Nesse caso,"),
  tags=["sistemas de votação", "contagem"])

GARRAFA = (tit("Texto para as questões 20 e 21.") + p("Uma garrafa cilíndrica está fechada, contendo um líquido que ocupa quase completamente seu corpo, conforme mostra a figura. Suponha que, para fazer medições, você disponha apenas de uma régua milimetrada.") + "[[fig:1]]")
F_GAR = figs(("q20", "Garrafa de corpo cilíndrico e gargalo estreito, fechada, com líquido até perto do alto do corpo cilíndrico."))
X(20, "M", "Matemática", "Volume do cilindro", "<p>O líquido ocupa um cilindro: o volume é π r² h. Basta medir o diâmetro (ou a circunferência) do corpo da garrafa e a altura do líquido: 2 medições. Alternativa <strong>B</strong>.</p><p>O líquido não chega ao gargalo, então sua forma é um cilindro perfeito e não é preciso medir mais nada; a espessura do vidro é desprezada.</p>",
  GARRAFA + p("Para calcular o volume do líquido contido na garrafa, o número mínimo de medições a serem realizadas é:"), F_GAR, ["cilindro", "medição"], alts=A5("1", "2", "3", "4", "5"))
X(21, "M", "Matemática", "Volume do cilindro", "<p>Além do diâmetro e da altura do líquido (2 medições), falta o volume do ar, que inclui o gargalo, de forma irregular. Virando a garrafa de cabeça para baixo, o ar fica na parte cilíndrica e basta medir a altura dessa camada de ar: 3 medições. Alternativa <strong>C</strong>.</p>",
  GARRAFA + p("Para calcular a capacidade total da garrafa, lembrando que você pode virá-la, o número mínimo de medições a serem realizadas é:"), F_GAR, ["cilindro", "medição indireta"], alts=A5("1", "2", "3", "4", "5"))

DEMO = (tit("Texto para as questões 22 e 23.") + p("Em material para análise de determinado <em>marketing</em> político, lê-se a seguinte conclusão:")
  + ap("<em>A explosão demográfica que ocorreu a partir dos anos 50, especialmente no Terceiro Mundo, suscitou teorias ou políticas demográficas divergentes. Uma primeira teoria, dos neomalthusianos, defende que o crescimento demográfico dificulta o desenvolvimento econômico, já que provoca uma diminuição na renda nacional per capita e desvia os investimentos do Estado para setores menos produtivos. Diante disso, o país deveria desenvolver uma rígida política de controle de natalidade. Uma segunda, a teoria reformista, argumenta que o problema não está na renda per capita e sim na distribuição irregular da renda, que não permite o acesso à educação e saúde. Diante disso o país deve promover a igualdade econômica e a justiça social.</em>"))
X(22, "H", "Geografia", "Teorias demográficas", "<p>Os neomalthusianos defendem o controle da natalidade como condição para o desenvolvimento: “Controle populacional – nosso passaporte para o desenvolvimento”. Alternativa <strong>A</strong>.</p><p>B e E expressam a visão reformista; C e D defendem o crescimento populacional.</p>",
  DEMO + p("Qual dos <em>slogans</em> abaixo poderia ser utilizado para defender o ponto de vista neomalthusiano?"), tags=["neomalthusianismo"])
X(23, "H", "Geografia", "Teorias demográficas", "<p>Para os reformistas, o problema é a má distribuição de renda, que impede o acesso à saúde e à educação; com esses direitos garantidos, as famílias reduziriam o número de filhos por escolha. “Com saúde e educação, o planejamento familiar virá por opção!” Alternativa <strong>B</strong>.</p><p>A, C e E põem o controle populacional como causa do desenvolvimento, que é a ideia neomalthusiana.</p>",
  DEMO + p("Qual dos <em>slogans</em> abaixo poderia ser utilizado para defender o ponto de vista dos reformistas?"), tags=["teoria reformista"])

ENCONTRO = (tit("Texto para as questões 24 e 25.") + p("José e Antônio viajarão em seus carros com as respectivas famílias para a cidade de Serra Branca. Com a intenção de seguir viagem juntos, combinam um encontro no marco inicial da rodovia, onde chegarão, de modo independente, entre meio-dia e 1 hora da tarde. Entretanto, como não querem ficar muito tempo esperando um pelo outro, combinam que o primeiro que chegar ao marco inicial esperará pelo outro, no máximo, meia hora; após esse tempo, seguirá viagem sozinho.",
  "Chamando de <strong>x</strong> o horário de chegada de José e de <strong>y</strong> o horário de chegada de Antônio, e representando os pares (x; y) em um sistema de eixos cartesianos, a região OPQR indicada corresponde ao conjunto de todas as possibilidades para o par (x; y):") + "[[fig:1]]")
F_ENC = ("q23", "Quadrado OPQR num sistema de eixos: no eixo horizontal, chegada de José, de 0 (12h) a 1 (13h); no vertical, chegada de Antônio, de 0 (12h) a 1 (13h). O é a origem, R = (1; 0), Q = (1; 1) e P = (0; 1).")
X(24, "M", "Matemática", "Plano cartesiano", "<p>Chegar no mesmo horário significa x = y. No quadrado, esses pontos formam a diagonal que vai de O (0; 0) a Q (1; 1). Alternativa <strong>A</strong>.</p><p>A diagonal PR é x + y = 1, que não representa chegadas iguais.</p>",
  ENCONTRO + p("Na região indicada, o conjunto de pontos que representa o evento “José e Antônio chegam ao marco inicial exatamente no mesmo horário” corresponde"),
  figs(F_ENC), ["reta y = x", "plano cartesiano"])
X(25, "M", "Matemática", "Probabilidade geométrica", "<p>Eles viajam juntos quando a diferença entre as chegadas é de no máximo meia hora: a faixa entre as retas y = x + 1/2 e y = x − 1/2 (regiões II e III). Fora dela ficam dois triângulos (I e IV), cada um com catetos 1/2 e área 1/8. A faixa tem área 1 − 2 × 1/8 = 3/4 do quadrado: 75%. Alternativa <strong>D</strong>.</p>",
  ENCONTRO + p("Segundo o combinado, para que José e Antônio viajem juntos, é necessário que y − x ≤ 1/2 ou que x − y ≤ 1/2.") + "[[fig:2]]"
  + p("De acordo com o gráfico e nas condições combinadas, as chances de José e Antônio viajarem juntos são de:"),
  figs(F_ENC, ("q25", "O quadrado de lado 1, com eixos “José” e “Antônio”, dividido pelas retas y = x + 1/2, y = x e y = x − 1/2 em quatro regiões: I, o triângulo no canto superior esquerdo, acima de y = x + 1/2; II, entre y = x + 1/2 e y = x; III, entre y = x e y = x − 1/2; IV, o triângulo no canto inferior direito, abaixo de y = x − 1/2.")),
  ["probabilidade geométrica", "área"], alts=A5("0%", "25%", "50%", "75%", "100%"))

SOMBRA = (tit("Texto para as questões 26 e 27.") + p("No primeiro dia do inverno no Hemisfério Sul, uma atividade de observação de sombras é realizada por alunos de Macapá, Porto Alegre e Recife. Para isso, utiliza-se uma vareta de 30 cm fincada no chão na posição vertical. Para marcar o tamanho e a posição da sombra, o chão é forrado com uma folha de cartolina, como mostra a figura:")
  + "[[fig:1]]" + "[[fig:2]]" + p("Nas figuras abaixo, estão representadas as sombras projetadas pelas varetas nas três cidades, no mesmo instante, ao meio-dia. A linha pontilhada indica a direção Norte-Sul.") + "[[fig:3]]")
F_SOM = figs(("q26a", "Mapa do Brasil com as capitais marcadas, a linha do Equador passando perto de Macapá e o Trópico de Capricórnio passando perto de São Paulo. Boa Vista e Macapá ficam no extremo norte; Natal e Recife, no extremo leste; Porto Alegre, no extremo sul; Brasília, Goiânia e Cuiabá, no centro."),
             ("q26b", "Vareta vertical fincada numa cartolina, projetando uma sombra sobre ela."),
             ("q26c", "Três cartolinas com a linha Norte-Sul pontilhada e a sombra ao meio-dia. Recife: sombra média, voltada para baixo e para a direita da linha. Porto Alegre: sombra longa, voltada para baixo e para a esquerda. Macapá: sombra curta, voltada para baixo e um pouco para a esquerda."))
X(26, "N", "Física", "Movimento aparente do Sol", "<p>No início do inverno do Hemisfério Sul, o Sol do meio-dia fica sobre o Trópico de Câncer, ao norte de todas as três cidades. Quanto mais ao sul a cidade, mais inclinados chegam os raios e mais longa é a sombra: Macapá, quase no Equador, tem a sombra mais curta; Porto Alegre, a mais longa. Entre as opções, o comprimento cresce com o afastamento do Equador. Alternativa <strong>B</strong>.</p>",
  SOMBRA + p("Levando-se em conta a localização destas três cidades no mapa, podemos afirmar que os comprimentos das sombras serão tanto maiores quanto maior for o afastamento da cidade em relação ao"), F_SOM, ["sombra", "latitude"])
X(27, "N", "Física", "Movimento aparente do Sol", "<p>O meio-dia do relógio é o mesmo nas três cidades, mas o meio-dia solar depende da longitude. Em Recife, mais a leste, o Sol já passou do ponto mais alto, e a sombra cai de um lado; em Porto Alegre e Macapá, mais a oeste, o Sol ainda não chegou lá, e a sombra cai do outro. A sombra ficaria sobre a linha numa cidade de longitude intermediária, entre Recife e as outras duas: Brasília. Alternativa <strong>D</strong>.</p><p>Natal fica a leste até de Recife; Manaus, Cuiabá e Boa Vista ficam a oeste de Macapá e Porto Alegre.</p>",
  SOMBRA + p("Pelos resultados da experiência, num mesmo instante, em Recife a sombra se projeta à direita e nas outras duas cidades à esquerda da linha pontilhada na cartolina. É razoável, então, afirmar que existe uma localidade em que a sombra deverá estar bem mais próxima da linha pontilhada, em vias de passar de um lado para o outro. Em que localidade, dentre as listadas abaixo, seria mais provável que isso ocorresse?"),
  F_SOM, ["longitude", "hora solar"])

CLONE = (tit("Texto para as questões 28 e 29.") + p("A seqüência abaixo indica de maneira simplificada os passos seguidos por um grupo de cientistas para a clonagem de uma vaca:")
  + I4("Retirou-se um óvulo da vaca Z. O núcleo foi desprezado, obtendo-se um óvulo anucleado.", "Retirou-se uma célula da glândula mamária da vaca W. O núcleo foi isolado e conservado, desprezando-se o resto da célula.",
       "O núcleo da célula da glândula mamária foi introduzido no óvulo anucleado. A célula reconstituída foi estimulada para entrar em divisão.", "Após algumas divisões, o embrião foi implantado no útero de uma terceira vaca Y, mãe de aluguel. O embrião se desenvolveu e deu origem ao clone."))
X(28, "N", "Biologia", "Clonagem", "<p>O material genético do clone (o núcleo) veio da célula mamária da vaca W. O óvulo de Z perdeu o núcleo, e a vaca Y só abrigou o embrião. As características genéticas são as de W. Alternativa <strong>B</strong>.</p><p>Na prática, o citoplasma do óvulo de Z traz um pouco de DNA mitocondrial, mas a questão trata da informação genética nuclear.</p>",
  CLONE + p("Considerando-se que os animais Z, W e Y não têm parentesco, pode-se afirmar que o animal resultante da clonagem tem as características genéticas da vaca"), tags=["clonagem", "núcleo celular"])
X(29, "N", "Biologia", "Clonagem", "<p>O clone tem os mesmos genes de W. Se Y for a mãe biológica de W, W herdou metade de seus genes de Y. Logo, o clone também tem 50% dos genes de Y. Alternativa <strong>C</strong>.</p><p>Gestar o embrião não transfere genes: os 50% vêm do parentesco entre Y e W.</p>",
  CLONE + p("Se a vaca Y, utilizada como “mãe de aluguel”, for a mãe biológica da vaca W, a porcentagem de genes da “mãe de aluguel”, presente no clone será"), tags=["herança genética", "clonagem"],
  alts=A5("0%", "25%", "50%", "75%", "100%"))

X(30, "M", "Matemática", "Sólidos de revolução", "<p>Cada figura, girando em torno da haste, gera um sólido com o mesmo perfil. A figura 1, com dois braços horizontais separados por um vão, gera dois discos (D). A figura 2, com uma ponta inclinada, gera um sólido com uma parte cônica (E). A figura 3 gera um disco largo com uma saliência (A). A 4, com dois triângulos, gera dois cones opostos (B). E a 5, em forma de E, gera três discos (C). Alternativa <strong>D</strong>.</p>",
  p("Assim como na relação entre o perfil de um corte de um torno e a peça torneada, sólidos de revolução resultam da rotação de figuras planas em torno de um eixo. Girando-se as figuras abaixo em torno da haste indicada obtêm-se os sólidos de revolução que estão na coluna da direita.") + "[[fig:1]]"
  + p("A correspondência correta entre as figuras planas e os sólidos de revolução obtidos é:"),
  figs(("q30", "À esquerda, cinco figuras planas numeradas de 1 a 5, cada uma presa a uma haste vertical à direita; à direita, cinco sólidos de revolução, de A a E. 1: forma de C, com um braço em cima e outro embaixo. 2: retângulo com uma ponta inclinada em cima. 3: forma com um degrau largo no meio. 4: duas pontas triangulares, uma em cima e outra embaixo. 5: forma de E, com três braços. A: um disco largo com uma cúpula. B: dois cones unidos pelas bases. C: três discos empilhados. D: dois discos separados. E: um cone sobre um cilindro.")),
  ["sólidos de revolução", "visualização espacial"])

X(31, "H", "História", "Revolução Científica", "<p>Copérnico chegou ao heliocentrismo “depois de longas investigações” e quer ser julgado por demonstrações matemáticas, não pela Escritura. Leonardo exige que a prática se apoie em teoria e que um caso seja testado “duas ou três vezes” antes de virar regra. Os dois valorizam a experiência, a observação e a demonstração. Alternativa <strong>D</strong>.</p><p>Ambos rejeitam a autoridade da tradição e da Bíblia como critério científico (C, E).</p>",
  ap("<em>(...) Depois de longas investigações, convenci-me por fim de que o Sol é uma estrela fixa rodeada de planetas que giram em volta dela e de que ela é o centro e a chama. Que, além dos planetas principais, há outros de segunda ordem que circulam primeiro como satélites em redor dos planetas principais e com estes em redor do Sol. (...) Não duvido de que os matemáticos sejam da minha opinião, se quiserem dar-se ao trabalho de tomar conhecimento, não superficialmente mas duma maneira aprofundada, das demonstrações que darei nesta obra. Se alguns homens ligeiros e ignorantes quiserem cometer contra mim o abuso de invocar alguns passos da Escritura (sagrada), a que torçam o sentido, desprezarei os seus ataques: as verdades matemáticas não devem ser julgadas senão por matemáticos.</em>")
  + fonte("(COPÉRNICO, N. <em>De Revolutionibus orbium caelestium</em>.)")
  + ap("<em>Aqueles que se entregam à prática sem ciência são como o navegador que embarca em um navio sem leme nem bússola. Sempre a prática deve fundamentar-se em boa teoria. Antes de fazer de um caso uma regra geral, experimente-o duas ou três vezes e verifique se as experiências produzem os mesmos efeitos. Nenhuma investigação humana pode se considerar verdadeira ciência se não passa por demonstrações matemáticas.</em>")
  + fonte("(VINCI, Leonardo da. <em>Carnets</em>.)") + p("O aspecto a ser ressaltado em ambos os textos para exemplificar o racionalismo moderno é"),
  tags=["Copérnico", "método científico"])

PANELA = (tit("Texto para as questões 32 e 33.") + p("A panela de pressão permite que os alimentos sejam cozidos em água muito mais rapidamente do que em panelas convencionais. Sua tampa possui uma borracha de vedação que não deixa o vapor escapar, a não ser através de um orifício central sobre o qual assenta um peso que controla a pressão. Quando em uso, desenvolve-se uma pressão elevada no seu interior. Para a sua operação segura, é necessário observar a limpeza do orifício central e a existência de uma válvula de segurança, normalmente situada na tampa.",
  "O esquema da panela de pressão e um diagrama de fase da água são apresentados abaixo.") + "[[fig:1]]")
F_PAN = figs(("q31", "À esquerda, esquema de panela de pressão sobre o fogo, com líquido embaixo, vapor em cima e a válvula de segurança na tampa. À direita, diagrama de fase da água: pressão (0 a 5 atm) em função da temperatura (0 a 160 °C); a curva separa a região do líquido, acima, da do vapor, abaixo, passando por 1 atm a 100 °C e subindo para cerca de 2 atm perto de 120 °C e 4 atm perto de 145 °C."))
X(32, "N", "Física", "Mudanças de fase", "<p>Com a pressão interna maior que a atmosférica, a água só ferve a uma temperatura mais alta (pelo diagrama, cerca de 120 °C a 2 atm). Os alimentos ficam em contato com água acima da temperatura normal de ebulição e cozinham mais depressa. Alternativa <strong>B</strong>.</p>",
  PANELA + p("A vantagem do uso de panela de pressão é a rapidez para o cozimento de alimentos e isto se deve"), F_PAN, ["panela de pressão", "ponto de ebulição"])
X(33, "N", "Física", "Mudanças de fase", "<p>Quando o vapor começa a sair pela válvula, a pressão interna já está no valor fixado pelo peso, e a temperatura de ebulição correspondente fica constante. Mantendo a fervura com fogo baixo, a temperatura não muda, e o tempo de cozimento também não. Alternativa <strong>E</strong>.</p><p>Fogo alto só faz sair mais vapor, sem aumentar a temperatura.</p>",
  PANELA + p("Se, por economia, abaixarmos o fogo sob uma panela de pressão logo que se inicia a saída de vapor pela válvula, de forma simplesmente a manter a fervura, o tempo de cozimento"), F_PAN, ["panela de pressão", "temperatura de ebulição"])

X(34, "H", "Geografia", "Hidrelétricas", "<p>A represa cria um grande espelho d’água parado: aumenta a área de evaporação, e com isso a umidade relativa do ar na região. Alternativa <strong>D</strong>.</p><p>A represa muda o regime do rio (vazão e velocidade abaixo dela), então há impacto (A, B), e não acelera os rios (C).</p>",
  p("A construção de grandes projetos hidroelétricos também deve ser analisada do ponto de vista do regime das águas e de seu ciclo na região. Em relação ao ciclo da água, pode-se argumentar que a construção de grandes represas"),
  tags=["represas", "evaporação"])

SOL = (tit("Texto para as questões 35 a 37.") + p("O diagrama abaixo representa a energia solar que atinge a Terra e sua utilização na geração de eletricidade. A energia solar é responsável pela manutenção do ciclo da água, pela movimentação do ar, e pelo ciclo do carbono que ocorre através da fotossíntese dos vegetais, da decomposição e da respiração dos seres vivos, além da formação de combustíveis fósseis.") + "[[fig:1]]")
F_SOL = figs(("q35", "Diagrama de fluxo: a energia proveniente do Sol, 200 bilhões de MW, vai para aquecimento do solo, evaporação da água, aquecimento do ar e absorção pelas plantas. A evaporação gera energia potencial (chuvas), usada nas usinas hidroelétricas, que produzem 100 000 MW. A absorção pelas plantas gera petróleo, gás e carvão, usados nas usinas termoelétricas, que produzem 400 000 MW. As duas juntas geram eletricidade: 500 000 MW."))
X(35, "N", "Física", "Energia", "<p>A eletricidade produzida é de 500 000 MW = 5 × 10<sup>5</sup> MW; a energia solar recebida é de 200 bilhões de MW = 2 × 10<sup>11</sup> MW. A fração é 5 × 10<sup>5</sup>/2 × 10<sup>11</sup> = 2,5 × 10<sup>−6</sup>. Alternativa <strong>B</strong>.</p>",
  SOL + p("De acordo com o diagrama, a humanidade aproveita, na forma de energia elétrica, uma fração da energia recebida como radiação solar, correspondente a:"),
  F_SOL, ["notação científica", "potência"], alts=A5("4 × 10<sup>−9</sup>", "2,5 × 10<sup>−6</sup>", "4 × 10<sup>−4</sup>", "2,5 × 10<sup>−3</sup>", "4 × 10<sup>−2</sup>"))
X(36, "N", "Física", "Fontes de energia", "<p>A modalidade que usa combustíveis fósseis é a termoelétrica, com petróleo, gás ou carvão. Esses combustíveis se formaram a partir de restos de seres vivos ao longo de centenas de milhões de anos. Alternativa <strong>E</strong>.</p><p>200 anos (C) e 1 milhão de anos (D) são tempos muito curtos para a formação do petróleo.</p>",
  SOL + p("De acordo com este diagrama, uma das modalidades de produção de energia elétrica envolve combustíveis fósseis. A modalidade de produção, o combustível e a escala de tempo típica associada à formação desse combustível são, respectivamente,"),
  F_SOL, ["combustíveis fósseis", "tempo geológico"],
  alts=A5("hidroelétricas, chuvas, um dia.", "hidroelétricas, aquecimento do solo, um mês.", "termoelétricas, petróleo, 200 anos.", "termoelétricas, aquecimento do solo, 1 milhão de anos.", "termoelétricas, petróleo, 500 milhões de anos."))
X(37, "N", "Física", "Fontes de energia", "<p>Só I está correta: a água das chuvas é renovável, e os combustíveis fósseis levam muito tempo para se formar. II é falsa: represas alagam áreas e alteram ecossistemas. III é falsa: o represamento não aumenta as chuvas do sertão nordestino. Alternativa <strong>A</strong>.</p>",
  SOL + p("No diagrama estão representadas as duas modalidades mais comuns de usinas elétricas, as hidroelétricas e as termoelétricas. No Brasil, a construção de usinas hidroelétricas deve ser incentivada porque essas")
  + I3("utilizam fontes renováveis, o que não ocorre com as termoelétricas que utilizam fontes que necessitam de bilhões de anos para serem reabastecidas.", "apresentam impacto ambiental nulo, pelo represamento das águas no curso normal dos rios.", "aumentam o índice pluviométrico da região de seca do Nordeste, pelo represamento de águas.")
  + p("Das três afirmações acima, somente"), F_SOL, ["energia renovável", "hidrelétricas"])

X(38, "M", "Matemática", "Probabilidade", "<p>Uma média de um raio a cada 10 anos não determina quando o próximo cairá: os raios são eventos aleatórios e independentes, e a chance de a estação ser atingida num período não depende de há quanto tempo ela existe ou de quando caiu o último raio. Alternativa <strong>D</strong>.</p><p>Uma média não garante intervalos regulares (B, C) nem impede longos períodos sem raios (E).</p>",
  p("Uma estação distribuidora de energia elétrica foi atingida por um raio. Este fato provocou escuridão em uma extensa área. Segundo estatísticas, ocorre em média a cada 10 anos um fato desse tipo. Com base nessa informação, pode-se afirmar que"),
  tags=["eventos independentes", "média"])

X(39, "L", "Língua Portuguesa", "Acentuação", "<p>Se a tônica for o segundo PA, a palavra é paroxítona terminada em ditongo crescente (-lia) e leva acento: PAPÁLIA (I). Se a tônica for LI, “i” e “a” ficam em sílabas diferentes (hiato), a palavra é paroxítona terminada em “a” e não leva acento: PAPALIA (III). II erra: o acento do hiato vale quando o “i” tônico vem depois de outra vogal, como em “saída”; em PA-PA-LI-A, o “i” vem depois de consoante, e a palavra é só uma paroxítona terminada em “a”. Alternativa <strong>E</strong>.</p>",
  p("Diante da visão de um prédio com uma placa indicando SAPATARIA PAPALIA, um jovem deparou com a dúvida: como pronunciar a palavra PAPALIA?") + "[[fig:1]]"
  + p("Levado o problema à sala de aula, a discussão girou em torno da utilidade de conhecer as regras de acentuação e, especialmente, do auxílio que elas podem dar à correta pronúncia de palavras. Após discutirem pronúncia, regras de acentuação e escrita, três alunos apresentaram as seguintes conclusões a respeito da palavra PAPALIA:")
  + I3("Se a sílaba tônica for o segundo PA, a escrita deveria ser PAPÁLIA, pois a palavra seria paroxítona terminada em ditongo crescente.", "Se a sílaba tônica for LI, a escrita deveria ser PAPALÍA, pois “i” e “a” estariam formando hiato.", "Se a sílaba tônica for LI, a escrita deveria ser PAPALIA, pois não haveria razão para o uso de acento gráfico.")
  + p("A conclusão está correta apenas em:"),
  figs(("q39", "Foto de um prédio de dois andares com a placa “SAPATARIA PAPALIA” na fachada.")), ["acentuação", "sílaba tônica"])

X(40, "H", "Geografia", "Brasil", "<p>O texto descreve um país moderno, com crescimento urbano rápido, mas com pobreza persistente, vastas áreas subpovoadas e uma das sociedades mais desiguais do mundo: grandes diferenças sociais e regionais num país moderno do Terceiro Mundo. Alternativa <strong>C</strong>.</p>",
  p("Uma pesquisadora francesa produziu o seguinte texto para caracterizar nosso país:")
  + ap("<em>O Brasil, quinto país do mundo em extensão territorial, é o mais vasto do hemisfério Sul. Ele faz parte essencialmente do mundo tropical, à exceção de seus estados mais meridionais, ao sul de São Paulo. O Brasil dispõe de vastos territórios subpovoados, como o da Amazônia, conhece também um crescimento urbano extremamente rápido, índices de pobreza que não diminuem e uma das sociedades mais desiguais do mundo. Qualificado de “terra de contrastes”, o Brasil é um país moderno do Terceiro Mundo, com todas as contradições que isso tem por conseqüência.</em>")
  + fonte("([Adaptado de] DROULERS, Martine. <em>Dictionnaire geopolitique des états</em>. Organizado por Yves Lacoste. Paris: Éditions Flamarion, 1995)")
  + p("O Brasil é qualificado como uma “terra de contrastes” por"),
  tags=["desigualdade regional"])

X(41, "N", "Física", "Razão", "<p>Área alagada por potência (km²/MW): Tucuruí 2 430/4 240 ≈ 0,57; Sobradinho 4 214/1 050 ≈ 4,0; Itaipu 1 350/12 600 ≈ 0,11; Ilha Solteira 1 077/3 230 ≈ 0,33; Furnas 1 450/1 312 ≈ 1,1. A maior razão é a de Sobradinho. Alternativa <strong>E</strong>.</p>",
  p("Muitas usinas hidroelétricas estão situadas em barragens. As características de algumas das grandes represas e usinas brasileiras estão apresentadas no quadro abaixo.")
  + tabela(["Usina", "Área alagada (km²)", "Potência (MW)", "Sistema hidrográfico"], [["Tucuruí", "2 430", "4 240", "Rio Tocantins"], ["Sobradinho", "4 214", "1 050", "Rio São Francisco"], ["Itaipu", "1 350", "12 600", "Rio Paraná"], ["Ilha Solteira", "1 077", "3 230", "Rio Paraná"], ["Furnas", "1 450", "1 312", "Rio Grande"]])
  + p("A razão entre a área da região alagada por uma represa e a potência produzida pela usina nela instalada é uma das formas de estimar a relação entre o dano e o benefício trazidos por um projeto hidroelétrico. A partir dos dados apresentados no quadro, o projeto que mais onerou o ambiente em termos de área alagada por potência foi"),
  tags=["razão", "hidrelétricas"])

X(42, "L", "Literatura", "João Cabral de Melo Neto", "<p>João Cabral diz que fala “com” uma linguagem enxuta, “do” sertão seco e áspero, “por” o sertanejo e “para” quem precisa ser alertado sobre a miséria do Nordeste. A linguagem reflete o tema, e o texto denuncia um fato social para leitores determinados. Alternativa <strong>A</strong>.</p>",
  p("Leia o que disse João Cabral de Melo Neto, poeta pernambucano, sobre a função de seus textos:")
  + ap("“<strong>Falo somente com o que falo:</strong> a linguagem enxuta, contato denso; <strong>falo somente do que falo</strong>: a vida seca, áspera e clara do sertão; <strong>falo somente por quem falo</strong>: o homem sertanejo sobrevivendo na adversidade e na míngua. <strong>Falo somente para quem falo:</strong> para os que precisam ser alertados para a situação da miséria no Nordeste.”")
  + p("Para João Cabral de Melo Neto, no texto literário,"),
  tags=["função social da literatura"])

X(43, "N", "Biologia", "Imunização", "<p>O soro (criança I) traz anticorpos prontos: a quantidade é alta logo no início e vai caindo, porque o organismo não os produz. A vacina (criança II) estimula o próprio organismo a produzir anticorpos: a quantidade começa baixa e sobe até se estabilizar. É o gráfico B. Alternativa <strong>B</strong>.</p>",
  p("A variação da quantidade de anticorpos específicos foi medida por meio de uma experiência controlada, em duas crianças durante um certo período de tempo. Para a imunização de cada uma das crianças foram utilizados dois procedimentos diferentes:")
  + "<ul><li><strong>Criança I:</strong> <em>aplicação de soro imune.</em></li><li><strong>Criança II:</strong> <em>vacinação.</em></li></ul>"
  + p("O gráfico que melhor representa as taxas de variação da quantidade de anticorpos nas crianças I e II é:"),
  figs(("q43a", "Gráfico de anticorpos em função do tempo: as curvas I e II sobem juntas e se estabilizam."), ("q43b", "Gráfico: a curva I começa alta e cai; a curva II começa baixa e sobe até se estabilizar."),
       ("q43c", "Gráfico: a curva I começa baixa e sobe; a curva II fica baixa e quase constante."), ("q43d", "Gráfico: a curva I começa alta e cai; a curva II fica baixa e quase constante."), ("q43e", "Gráfico: as curvas I e II começam altas e caem juntas.")),
  ["soro e vacina", "anticorpos"], alts=ALT(1))

X(44, "H", "Geografia", "Conservação do solo", "<p>O lado II é uma encosta íngreme de rocha permeável: dá para plantar, desde que se evite a erosão, por exemplo com plantio em curvas de nível, que segura a água e o solo. Alternativa <strong>C</strong>.</p><p>Arar a encosta (A) aumenta a erosão; ela pode ser evitada (B); e o lado II, alto, não sofre inundação (D).</p>",
  p("Um agricultor adquiriu alguns alqueires de terra para cultivar e residir no local. O desenho abaixo representa parte de suas terras.") + "[[fig:1]]"
  + p("Pensando em construir sua moradia no lado I do rio e plantar no lado II, o agricultor consultou seus vizinhos e escutou as frases abaixo. Assinale a frase do vizinho que deu a sugestão mais correta."),
  figs(("q44", "Corte do terreno: à esquerda, o lado II, uma encosta alta e íngreme; no meio, o rio, no fundo do vale; à direita, o lado I, mais baixo e suave. Sob a superfície, uma camada de rocha permeável; abaixo, a região do lençol de água subterrânea; e, no fundo, rocha impermeável.")),
  ["curvas de nível", "erosão"])

X(45, "N", "Física", "Conservação da energia", "<p>A energia total sempre se conserva, em qualquer transformação: ela pode mudar de forma ou ser dissipada como calor, mas não é criada nem destruída. Isso vale para todos os processos da tabela. Alternativa <strong>A</strong>.</p><p>A dissipação de calor (B) não viola a conservação: a energia passa para outra forma.</p>",
  p("A tabela a seguir apresenta alguns exemplos de processos, fenômenos ou objetos em que ocorrem transformações de energia. Nessa tabela, aparecem as direções de transformação de energia. Por exemplo, o termopar é um dispositivo onde energia térmica se transforma em energia elétrica.")
  + tabela(["Processo", "De (energia)", "Em (energia)"], [["Transformador", "Elétrica", "Elétrica"], ["Termopar", "Térmica", "Elétrica"], ["Reações endotérmicas", "Térmica", "Química"], ["Dinamite", "Química", "Mecânica"], ["Pêndulo", "Mecânica", "Mecânica"], ["Fusão", "Térmica", "Térmica"]])
  + p("Dentre os processos indicados na tabela, ocorre conservação de energia"),
  tags=["conservação de energia", "transformações de energia"])

X(46, "H", "Geografia", "Desemprego estrutural", "<p>O desemprego estrutural vem de mudanças permanentes na produção: automação, novas tecnologias e novas formas de gerenciamento eliminam postos que não voltam, mesmo quando a economia cresce. Alternativa <strong>D</strong>.</p><p>A descreve o desemprego conjuntural, de crise; o setor de serviços não absorve todos os demitidos (B).</p>",
  p("Um dos maiores problemas da atualidade é o aumento desenfreado do desemprego. O texto abaixo destaca esta situação.")
  + ap("<em>O desemprego é hoje um fenômeno que atinge e preocupa o mundo todo. (...) A onda de desemprego recente não é conjuntural, ou seja, provocada por crises localizadas e temporárias. Está associada a mudanças estruturais na economia, daí o nome de desemprego estrutural.</em>", "<em>O desemprego manifesta-se hoje na maioria das economias, incluindo a dos países ricos. A OIT estima em 1 bilhão – um terço da força de trabalho mundial – o número de desempregados em todo o mundo em 1998. Desse total, 150 milhões encontram-se abertamente desempregados e entre 750 e 900 milhões estão subempregados.</em>")
  + fonte("([CD-ROM] <em>Almanaque Abril 1999</em>. São Paulo: Abril.)") + p("Pode-se compreender o desemprego estrutural em termos da internacionalização da economia associada"),
  tags=["desemprego estrutural", "automação"])

X(47, "N", "Química", "Leitura de gráficos", "<p>A curva sobe rápido no início (cerca de 10 mícrons nos primeiros 30 000 anos) e depois cada vez mais devagar, quase se estabilizando perto de 15 mícrons. A espessura aumenta mais rapidamente quando a pedra é mais jovem. Alternativa <strong>C</strong>.</p><p>A curva não é uma reta (A), e continua subindo um pouco depois de 100 000 anos (E).</p>",
  p("A obsidiana é uma pedra de origem vulcânica que, em contato com a umidade do ar, fixa água em sua superfície formando uma camada hidratada. A espessura da camada hidratada aumenta de acordo com o tempo de permanência no ar, propriedade que pode ser utilizada para medir sua idade. O gráfico abaixo mostra como varia a espessura da camada hidratada, em mícrons (1 mícron = 1 milésimo de milímetro) em função da idade da obsidiana.")
  + "[[fig:1]]" + p("Com base no gráfico, pode-se concluir que a espessura da camada hidratada de uma obsidiana"),
  figs(("q47", "Gráfico da espessura hidratada (0 a 15 mícrons) em função da idade (0 a 140 000 anos): a curva sobe rápido no começo, chega a cerca de 10 mícrons por volta de 30 000 anos, a cerca de 14 mícrons por volta de 60 000 anos e depois cresce bem devagar, chegando perto de 15,5 mícrons em 140 000 anos.")),
  ["taxa de variação", "leitura de gráfico"])

X(48, "L", "Literatura", "Intertextualidade", "<p>Os três poemas começam com “Quando nasci” e um anjo que anuncia o destino do poeta: Chico e Adélia retomam a imagem de Drummond (o anjo que define a vida de quem nasce), adaptando-a a outros sentidos. É reiteração de imagens. Alternativa <strong>A</strong>.</p><p>Eles não negam nem contradizem Drummond (B, D); a retomada é um recurso criativo (C, E).</p>",
  p("Quem não passou pela experiência de estar lendo um texto e defrontar-se com passagens já lidas em outros? Os textos conversam entre si em um diálogo constante. Esse fenômeno tem a denominação de intertextualidade. Leia os seguintes textos:")
  + "[[fig:1]]" + p("Adélia Prado e Chico Buarque estabelecem intertextualidade, em relação a Carlos Drummond de Andrade, por"),
  figs(("q48", "Três trechos. I, de Carlos Drummond de Andrade (“Alguma poesia”): ao nascer, um anjo torto, dos que vivem na sombra, diz ao poeta que seja “gauche” na vida. II, de Chico Buarque: ao nascer, um anjo safado decreta que o eu lírico está predestinado a ser errado, e sua estrada já entorta na saída, mas ele vai até o fim. III, de Adélia Prado (“Bagagem”): ao nascer, um anjo esbelto, desses que tocam trombeta, anuncia que ela vai carregar bandeira, carga muito pesada para uma mulher.")),
  ["Drummond", "intertextualidade"])

X(49, "H", "História", "Revolução Industrial", "<p>A legislação trabalhista e a jornada de oito horas foram conquistas obtidas pela organização dos trabalhadores: sindicatos, greves e partidos operários. Alternativa <strong>C</strong>.</p><p>Não houve escassez de mão de obra (B), e os partidos comunistas não venceram eleições nas capitais europeias (E).</p>",
  p("A Revolução Industrial ocorrida no final do século XVIII transformou as relações do homem com o trabalho. As máquinas mudaram as formas de trabalhar, e as fábricas concentraram-se em regiões próximas às matérias-primas e grandes portos, originando vastas concentrações humanas. Muitos dos operários vinham da área rural e cumpriam jornadas de trabalho de 12 a 14 horas, na maioria das vezes em condições adversas. A legislação trabalhista surgiu muito lentamente ao longo do século XIX e a diminuição da jornada de trabalho para oito horas diárias concretizou-se no início do século XX.",
    "Pode-se afirmar que as conquistas no início deste século, decorrentes da legislação trabalhista, estão relacionadas com"),
  tags=["direitos trabalhistas", "movimento operário"])

X(50, "N", "Biologia", "Teia alimentar", "<p>O milho é comido por gafanhotos, pássaros, galinhas e roedores; o cachorro-do-mato come pássaros, galinhas e roedores; e os pássaros comem gafanhotos. Sem cachorros-do-mato, pássaros e roedores aumentaram; sem pássaros, os gafanhotos explodiram. Essa teia é a B. Alternativa <strong>B</strong>.</p><p>As outras põem as setas no sentido errado (o milho comendo a galinha, o cachorro-do-mato servindo de alimento) ou ligam os seres numa cadeia linear que não corresponde ao caso.</p>",
  p("Um agricultor, que possui uma plantação de milho e uma criação de galinhas, passou a ter sérios problemas com os cachorros-do-mato que atacavam sua criação. O agricultor, ajudado pelos vizinhos, exterminou os cachorros-do-mato da região. Passado pouco tempo, houve um grande aumento no número de pássaros e roedores que passaram a atacar as lavouras. Nova campanha de extermínio e, logo depois da destruição dos pássaros e roedores, uma grande praga de gafanhotos, destruiu totalmente a plantação de milho e as galinhas ficaram sem alimento.",
    "Analisando o caso acima, podemos perceber que houve desequilíbrio na teia alimentar representada por:"),
  tags=["cadeia alimentar", "desequilíbrio ecológico"],
  alts=A5("milho → gafanhotos → pássaro → galinha → roedores → cachorro-do-mato.",
          "milho → pássaro, gafanhoto, galinha e roedores; gafanhoto → pássaro; pássaro, gafanhoto, galinha e roedores → cachorro-do-mato.",
          "galinha → milho; milho → gafanhotos, roedores e pássaros; gafanhotos, roedores e pássaros → cachorro-do-mato.",
          "cachorro-do-mato → roedores, pássaros, gafanhotos e galinha; roedores, pássaros, gafanhotos e galinha → milho.",
          "galinha → milho → gafanhotos → pássaro → roedores → cachorro-do-mato."))

X(51, "N", "Física", "Potência elétrica", "<p>Pela tabela, a lâmpada de 120 V ligada em 127 V dissipa 65 W (maior potência), produz 920 lúmens (mais luz) e dura em média 452 horas (menos da metade das 1000 h da de 127 V). Alternativa <strong>D</strong>.</p><p>Ligada numa tensão acima da de projeto, a corrente é maior, o filamento esquenta mais e se desgasta mais depressa.</p>",
  p("Lâmpadas incandescentes são normalmente projetadas para trabalhar com a tensão da rede elétrica em que serão ligadas. Em 1997, contudo, lâmpadas projetadas para funcionar com 127 V foram retiradas do mercado e, em seu lugar, colocaram-se lâmpadas concebidas para uma tensão de 120 V. Segundo dados recentes, essa substituição representou uma mudança significativa no consumo de energia elétrica para cerca de 80 milhões de brasileiros que residem nas regiões em que a tensão da rede é de 127 V.",
    "A tabela abaixo apresenta algumas características de duas lâmpadas de 60 W, projetadas respectivamente para 127 V (antiga) e 120 V (nova), quando ambas encontram-se ligadas numa rede de 127 V.")
  + tabela(["Lâmpada (projeto original)", "60 W – 127 V", "60 W – 120 V"], [["Tensão da rede elétrica", "127 V", "127 V"], ["Potência medida (W)", "60", "65"], ["Luminosidade medida (lúmens)", "750", "920"], ["Vida útil média (horas)", "1000", "452"]])
  + p("Acender uma lâmpada de 60 W e 120 V em um local onde a tensão na tomada é de 127 V, comparativamente a uma lâmpada de 60 W e 127 V no mesmo local tem como resultado:"),
  tags=["potência", "tensão elétrica"])

X(52, "M", "Matemática", "Leitura de gráficos", "<p>Em 1975, a população está caindo depois do pico de 10 mil (por volta de 1970) e vale cerca de 9 mil. Na subida anterior, a curva passa por 8 mil em 1960 e por quase 10 mil em 1965; ela cruza os 9 mil por volta de 1963. Alternativa <strong>B</strong>.</p><p>Em 1967 (C), a população já estava perto de 10 mil, e em 1970 (D) estava no máximo.</p>",
  p("O número de indivíduos de certa população é representado pelo gráfico abaixo.") + "[[fig:1]]" + p("Em 1975, a população tinha um tamanho aproximadamente igual ao de:"),
  figs(("q52", "Gráfico do número de indivíduos (em milhares, de 1 a 10) de 1940 a 1990: a curva começa em 1 mil em 1940, sobe devagar até 1945 e depois rápido, passando por cerca de 3,7 mil em 1950, 8 mil em 1960 e 9,6 mil em 1965; chega ao máximo de 10 mil por volta de 1970, cai para cerca de 9 mil em 1975 e 8,3 mil em 1980, e se estabiliza perto de 8 mil.")),
  ["leitura de gráfico", "dinâmica populacional"])

X(53, "H", "História", "Brasil Império", "<p>A cidade descrita tem chaminés de fábricas e operários a caminho do trabalho, convivendo com carrocinhas, vacas de leite e carros de água: elementos de uma economia agrária e de uma industrial, sinal do início da industrialização no Brasil do século XIX. Alternativa <strong>A</strong>.</p><p>A economia brasileira não era industrial desde o século XVIII (B), e o texto mostra a indústria presente no cotidiano (E).</p>",
  ap("<em>Viam-se de cima as casas acavaladas umas pelas outras, formando ruas, contornando praças. As chaminés principiavam a fumar; deslizavam as carrocinhas multicores dos padeiros; as vacas de leite caminhavam com o seu passo vagaroso, parando à porta dos fregueses, tilintando o chocalho; os quiosques vendiam café a homens de jaqueta e chapéu desabado; cruzavam-se na rua os libertinos retardios com os operários que se levantavam para a obrigação; ouvia-se o ruído estalado dos carros de água, o rodar monótono dos bondes.</em>")
  + fonte("(AZEVEDO, Aluísio de. <em>Casa de Pensão</em>. São Paulo: Martins, 1973)") + p("O trecho, retirado de romance escrito em 1884, descreve o cotidiano de uma cidade, no seguinte contexto:"),
  tags=["industrialização", "Aluísio Azevedo"])

X(54, "N", "Biologia", "Florestas tropicais", "<p>Nas florestas tropicais, os nutrientes estão na própria vegetação e nas folhas caídas. O calor e a umidade aceleram a decomposição, e os nutrientes voltam rapidamente às plantas, sem se acumular no solo. Alternativa <strong>E</strong>.</p><p>O solo dessas florestas é pobre, não fértil por ser profundo (A); e a produção de oxigênio não explica a nutrição das plantas (D).</p>",
  ap("<em>Apesar da riqueza das florestas tropicais, elas estão geralmente baseadas em solos inférteis e improdutivos. Grande parte dos nutrientes é armazenada nas folhas que caem sobre o solo, não no solo propriamente dito. Quando esse ambiente é intensamente modificado pelo ser humano, a vegetação desaparece, o ciclo dos nutrientes é alterado e a terra se torna rapidamente infértil.</em>")
  + fonte("(CORSON, Walter H. <em>Manual Global de Ecologia</em>, 1993)")
  + p("No texto acima, pode parecer uma contradição a existência de florestas tropicais exuberantes sobre solos pobres. No entanto, este fato é explicado pela"),
  tags=["ciclagem de nutrientes", "decompositores"])

X(55, "H", "Geografia", "Reciclagem", "<p>Reciclar papel (I) e baratear produtos com papel reciclado (III) diminuem a necessidade de matéria-prima nova e, assim, a pressão sobre as florestas nativas. Reduzir tarifas de importação (II) só muda o lugar de onde vem o papel e pode transferir o desmatamento para outros países: não ajuda o meio ambiente global. Alternativa <strong>E</strong>.</p>",
  p("Com o uso intensivo do computador como ferramenta de escritório, previu-se o declínio acentuado do uso de papel para escrita. No entanto, essa previsão não se confirmou, e o consumo de papel ainda é muito grande. O papel é produzido a partir de material vegetal e, por conta disso, enormes extensões de florestas já foram extintas, uma parte sendo substituída por reflorestamentos homogêneos de uma só espécie (no Brasil, principalmente eucalipto).",
    "Para evitar que novas áreas de florestas nativas, principalmente as tropicais, sejam destruídas para suprir a produção crescente de papel, foram propostas as seguintes ações:")
  + I3("Aumentar a reciclagem de papel, através da coleta seletiva e processamento em usinas.", "Reduzir as tarifas de importação de papel.", "Diminuir os impostos para produtos que usem papel reciclado.")
  + p("Para um meio ambiente global mais saudável, apenas"),
  tags=["papel reciclado", "desmatamento"])

X(56, "N", "Biologia", "Controle de pragas", "<p>Depois da introdução do inimigo natural (seta ①), a praga oscila, mas fica controlada perto do nível P. O inseticida (seta ②) derrubou a praga e também seus predadores; sem eles, a praga se recuperou mais depressa e passou muito acima de P. Alternativa <strong>D</strong>.</p><p>O controle biológico funcionava (C é falsa), e o inseticida piorou a situação (E é falsa).</p>",
  p("O crescimento da população de uma praga agrícola está representado em função do tempo, no gráfico abaixo, onde a densidade populacional superior a <strong>P</strong> causa prejuízo à lavoura.", "No momento apontado pela seta ①, um agricultor introduziu uma espécie de inseto que é inimigo natural da praga, na tentativa de controlá-la biologicamente.",
    "No momento indicado pela seta ②, o agricultor aplicou grande quantidade de inseticida, na tentativa de eliminar totalmente a praga.") + "[[fig:1]]" + p("A análise do gráfico permite concluir que"),
  figs(("q56", "Gráfico da densidade populacional da praga ao longo do tempo, com uma linha pontilhada no nível P. No início, a densidade sobe muito acima de P; na seta ①, quando o inimigo natural é introduzido, ela cai e passa a oscilar abaixo de P. Na seta ②, com o inseticida, ela cai bruscamente e logo volta a subir, passando muito acima de P.")),
  ["controle biológico", "inseticidas"])

X(57, "N", "Química", "Dessalinização", "<p>Já existem processos conhecidos para tirar o sal da água do mar, como a destilação e a osmose reversa, mas eles gastam muita energia e são caros em larga escala. Alternativa <strong>A</strong>.</p><p>Os sais podem ser separados (B, D), e a temperatura de ebulição da água do mar é só um pouco maior que a da água pura (E).</p>",
  p("Em nosso planeta a quantidade de água está estimada em 1,36 × 10<sup>6</sup> trilhões de toneladas. Desse total, calcula-se que cerca de 95% são de água salgada e dos 5% restantes, quase a metade está retida nos pólos e geleiras.", "O uso de água do mar para obtenção de água potável ainda não é realidade em larga escala. Isso porque, entre outras razões,"),
  tags=["água potável", "dessalinização"])

X(58, "N", "Química", "Evaporação", "<p>Como só a água evapora, os sais dissolvidos ficam para trás. Nos campos irrigados, a água evapora do solo e deixa os sais, que se acumulam: é a salinização. Alternativa <strong>C</strong>.</p><p>Pela mesma razão, a evaporação aumenta (e não diminui) a salinidade da superfície do mar (E), e os sais não evaporam com a água (A, B).</p>",
  p("Segundo o poeta Carlos Drummond de Andrade, a “água é um projeto de viver”. Nada mais correto, se levarmos em conta que toda água com que convivemos carrega, além do puro e simples H<sub>2</sub>O, muitas outras substâncias nela dissolvidas ou em suspensão. Assim, o ciclo da água, além da própria água, também promove o transporte e a redistribuição de um grande conjunto de substâncias relacionadas à dinâmica da vida.",
    "No ciclo da água, a evaporação é um processo muito especial, já que apenas moléculas de H<sub>2</sub>O passam para o estado gasoso. Desse ponto de vista, uma das conseqüências da evaporação pode ser"),
  tags=["salinização", "ciclo da água"])

X(59, "N", "Química", "Conservação de alimentos", "<p>Depois de aberto, o leite fica exposto aos microrganismos do ar (V); fora da geladeira, no verão, a temperatura favorece sua multiplicação (II) e acelera as transformações químicas (III). Alternativa <strong>C</strong>.</p><p>O leite sempre teve água líquida (I), e a instrução não trata de conservantes (IV).</p>",
  p("A deterioração de um alimento é resultado de transformações químicas que decorrem, na maioria dos casos, da interação do alimento com microrganismos ou, ainda, da interação com o oxigênio do ar, como é o caso da rancificação de gorduras. Para conservar por mais tempo um alimento deve-se, portanto, procurar impedir ou retardar ao máximo a ocorrência dessas transformações.",
    "Os processos comumente utilizados para conservar alimentos levam em conta os seguintes fatores:")
  + '<ol type="I"><li>microrganismos dependem da água líquida para sua sobrevivência.</li><li>microrganismos necessitam de temperaturas adequadas para crescerem e se multiplicarem. A multiplicação de microrganismos, em geral, é mais rápida entre 25 °C e 45 °C, aproximadamente.</li><li>transformações químicas têm maior rapidez quanto maior for a temperatura e a superfície de contato das substâncias que interagem.</li><li>há substâncias que acrescentadas ao alimento dificultam a sobrevivência ou a multiplicação de microrganismos.</li><li>no ar há microrganismos que encontrando alimento, água líquida e temperaturas adequadas crescem e se multiplicam.</li></ol>'
  + p("Em uma embalagem de leite “longa-vida”, lê-se: <strong>“Após aberto é preciso guardá-lo em geladeira”</strong>", "Caso uma pessoa <strong>não</strong> siga tal instrução, principalmente no verão tropical, o leite se deteriorará rapidamente, devido a razões relacionadas com"),
  tags=["microrganismos", "refrigeração"], alts=A5("o fator I, apenas.", "o fator II, apenas.", "os fatores II, III e V, apenas.", "os fatores I, II e III, apenas.", "os fatores I, II, III, IV e V."))

X(60, "H", "História", "Guerra Fria", "<p>A Guerra Fria foi o período, entre o fim da Segunda Guerra e o fim da URSS, em que Estados Unidos e União Soviética, as duas superpotências que emergiram do conflito, se enfrentaram em disputas políticas, militares, econômicas e ideológicas, sem guerra direta entre elas. Alternativa <strong>E</strong>.</p>",
  ap("<em>Os 45 anos que vão do lançamento das bombas atômicas até o fim da União Soviética, não foram um período homogêneo único na história do mundo. (...) dividem-se em duas metades, tendo como divisor de águas o início da década de 70. Apesar disso, a história deste período foi reunida sob um padrão único pela situação internacional peculiar que o dominou até a queda da URSS.</em>")
  + fonte("(HOBSBAWM, Eric J. <em>Era dos Extremos</em>. São Paulo: Cia das Letras, 1996)") + p("O período citado no texto e conhecido por “Guerra Fria” pode ser definido como aquele momento histórico em que houve"),
  tags=["Guerra Fria", "bipolaridade"])

X(61, "M", "Matemática", "Média ponderada", "<p>A média é a soma de cada velocidade vezes sua porcentagem: (20 × 5 + 30 × 15 + 40 × 30 + 50 × 40 + 60 × 6 + 70 × 3 + 80 × 1)/100 = (100 + 450 + 1 200 + 2 000 + 360 + 210 + 80)/100 = 4 400/100 = 44 km/h. Alternativa <strong>B</strong>.</p>",
  p("Um sistema de radar é programado para registrar automaticamente a velocidade de todos os veículos trafegando por uma avenida, onde passam em média 300 veículos por hora, sendo 55 km/h a máxima velocidade permitida. Um levantamento estatístico dos registros do radar permitiu a elaboração da distribuição percentual de veículos de acordo com sua velocidade aproximada.")
  + "[[fig:1]]" + p("A velocidade média dos veículos que trafegam nessa avenida é de:"),
  figs(("q61", "Gráfico de barras da porcentagem de veículos por velocidade: 20 km/h, 5%; 30 km/h, 15%; 40 km/h, 30%; 50 km/h, 40%; 60 km/h, 6%; 70 km/h, 3%; 80 km/h, 1%.")),
  ["média ponderada", "estatística"])

X(62, "N", "Biologia", "Leptospirose", "<p>A sequência lógica é: o lixo acumulado atrai e faz proliferar os ratos (II); o lixo entope bueiros e provoca enchentes (III); a enchente espalha a urina e os dejetos dos animais (I); e quem tem contato com a água contaminada pode pegar leptospirose (IV). Alternativa <strong>E</strong>.</p>",
  ap("<strong><em>Casos de leptospirose crescem na região</em></strong>", "<em>M.P.S. tem 12 anos e está desde janeiro em tratamento de leptospirose. Ela perdeu a tranqüilidade e encontrou nos ratos, (...), os vilões de sua infância. “Se eu não os matar, eles me matam”, diz. Seu medo reflete um dos maiores problemas do bairro: a falta de saneamento básico e o acúmulo de lixo...</em>")
  + fonte("(<em>O Estado de S. Paulo</em>, 31/07/1997)")
  + ap("<strong><em>Oito suspeitos de leptospirose</em></strong>", "<em>A cidade ficou sob as águas na madrugada de anteontem e, além de 120 desabrigados, as inundações estão fazendo outro tipo de vítimas: já há oito suspeitas de casos de leptospirose (...) transmitida pela urina de ratos contaminados.</em>")
  + fonte("(<em>Folha de S. Paulo</em>, 12/02/1999)") + p("As notícias dos jornais sobre casos de leptospirose estão associadas aos fatos:")
  + I4("Quando ocorre uma enchente, as águas espalham, além do lixo acumulado, todos os dejetos dos animais que ali vivem.", "O acúmulo de lixo cria ambiente propício para a proliferação dos ratos.", "O lixo acumulado nos terrenos baldios e nas margens de rios entope os bueiros e compromete o escoamento das águas em dias de chuva.", "As pessoas que vivem na região assolada pela enchente, entrando em contato com a água contaminada, têm grande chance de contrair a leptospirose.")
  + p("A <strong>seqüência</strong> de fatos que relaciona corretamente a leptospirose, o lixo, as enchentes e os roedores é:"),
  tags=["leptospirose", "saneamento"])

X(63, "L", "Literatura", "Crônica", "<p>“Atingir o máximo de matizes com o mínimo de elementos” é fazer muito com pouco. Drummond diz algo parecido quando define a obra de Braga como “narrativa direta e econômica”: sem excessos, só o essencial. Alternativa <strong>A</strong>.</p><p>“Real, palpável” e “sentimento de realidade” falam do assunto da obra, não da economia de meios.</p>",
  ap("<em>E considerei a glória de um pavão ostentando o esplendor de suas cores; é um luxo imperial. Mas andei lendo livros, e descobri que aquelas cores todas não existem na pena do pavão. Não há pigmentos. O que há são minúsculas bolhas d’água em que a luz se fragmenta, como em um prisma. O pavão é um arco-íris de plumas.</em>",
     "<em>Eu considerei que este é o luxo do grande artista, atingir o máximo de matizes com o mínimo de elementos. De água e luz ele faz seu esplendor; seu grande mistério é a simplicidade.</em>",
     "<em>Considerei, por fim, que assim é o amor, oh! Minha amada; de tudo que ele suscita e esplende e estremece e delira em mim existem apenas meus olhos recebendo a luz de teu olhar. Ele me cobre de glórias e me faz magnífico.</em>")
  + fonte("(BRAGA, Rubem. <em>Ai de ti, Copacabana</em>. 20.ed.)")
  + p("O poeta Carlos Drummond de Andrade escreveu assim sobre a obra de Rubem Braga:")
  + ap("<em>O que ele nos conta é o seu dia, o seu expediente de homem, apanhado no essencial, narrativa direta e econômica. (...) É o poeta do real, do palpável, que se vai diluindo em cisma. Dá o sentimento da realidade e o remédio para ela.</em>")
  + p("Em seu texto, Rubem Braga afirma que “este é o luxo do grande artista, atingir o máximo de matizes com o mínimo de elementos”. Afirmação semelhante pode ser encontrada no texto de Carlos Drummond de Andrade, quando, ao analisar a obra de Braga, diz que ela é"),
  tags=["Rubem Braga", "crônica"], alts=dict(D[63], E="seu remédio."))

Q.setdefault(4, {})["alternativas"] = {'A': '365 anos.', 'B': '460 anos.', 'C': '900 anos.', 'D': '10 000 anos.', 'E': '460 000 anos.'}  # texto vizinho grudava na alternativa C
Q.setdefault(12, {})["alternativas"] = {'A': '1 mês.', 'B': '2 meses.', 'C': '3 meses.', 'D': '4 meses.', 'E': '5 meses.'}  # texto vizinho grudava na alternativa D
completar(Q, R)
