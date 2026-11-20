# Enem 2005 (28/08/2005), Prova 1 — amarela: prova única de 63 questões (modelo antigo, sem divisão por áreas).
# Fonte do PDF: arquivo 'Provas_Gabaritos_ENEM_2005' do usuário. Gabarito: acervo da USP (GABARITO_ENEM_2005_AMARELA), lido duas vezes.
# Data: Portaria Inep nº 6/2005, art. 15 ("será realizado no dia 28 de agosto de 2005").
# O extrator padrão não lê este layout; as alternativas vêm de alts.json (extrator próprio) e os enunciados são escritos aqui.
# Cada questão leva a grande área mais próxima. Poemas e letras protegidos (Drummond Q1–2 e Q58, Portinari Q20, Renato Teixeira
# e trova Q33, versão de Chico Buarque Q56, Bandeira Q58) como imagem; Mário de Andrade (Q9) e Machado (Q63), de domínio público, em texto.
import sys, pathlib, re, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar

ID = "enem-2005"
META = {"id": ID, "banca": "Enem", "ano": 2005, "titulo": "Enem 2005: Prova objetiva", "fonte": "Inep", "dataExame": "2005-08-28",
        "duracaoMinutos": 300, "area": "Prova objetiva (63 questões)", "caderno": "amarelo", "dia": 1, "fonteGabarito": {"oficial": True, "nome": "gabarito oficial do Inep, em cópia guardada pelo Instituto de Física da USP", "url": "https://fep.if.usp.br/~profis/arquivo/avaliacao/enem/provas_gabaritos/2005/"}}
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


# ---------------------------------------------------------------- 1–2: Drummond, “A dança e a alma”
F_DANCA = figs(("q01", "Poema “A dança e a alma”, de Carlos Drummond de Andrade, em quatro quadras. O poeta diz que a dança não é só movimento, mas concentração e graça natural; que nela pairamos no éter, e não no solo; que é seiva e força, um estar entre céu e chão onde a paixão se liberta e a alma descreve suas parábolas mais divinas sem fugir à forma do ser."))
DANCA = p("As questões 1 e 2 referem-se ao poema.") + "[[fig:1]]" + fonte("Carlos Drummond de Andrade. <em>Obra completa</em>. Rio de Janeiro: Aguilar, 1964. p. 366.")
X(1, "L", "Literatura", "Interpretação de poema", "<p>O poema nega que a dança seja só movimento: ela é concentração, faz pairar “no éter” e permite que a paixão se liberte e que a alma descreva “suas mais divinas parábolas”. A definição que melhor traduz isso é a da expressão corporal que ultrapassa os limites físicos e libera o espírito. Alternativa <strong>B</strong>.</p><p>As outras falam de comunicação, sequência de passos, ritmo musical ou desenvolvimento intelectual, ideias que não estão no poema.</p>",
  DANCA + p("A definição de dança, em linguagem de dicionário, que mais se aproxima do que está expresso no poema é"), F_DANCA, ["Drummond", "dança"])
X(2, "L", "Literatura", "Interpretação de poema", "<p>Na segunda estrofe, “No solo não, no éter pairamos”: o éter (o espaço celeste, o ar) se opõe ao solo, como o alto ao baixo. Alternativa <strong>A</strong>.</p><p>“Chão” (C) aparece em outra estrofe e tem sentido próximo ao de solo, e não oposto; seiva, paixão e ser não formam contraste com ele.</p>",
  DANCA + p("O poema “A Dança e a Alma” é construído com base em contrastes, como “movimento” e “concentração”. Em uma das estrofes, o termo que estabelece contraste com <u>solo</u> é:"), F_DANCA, ["antítese", "Drummond"])

X(3, "H", "Geografia", "Mercado de trabalho", "<p>Paulo tem Ensino Médio completo e, mesmo assim, só achou vaga de garçom por um salário mínimo. A interpretação II (baixa qualificação explica o desemprego) não basta para o caso: II complementa I, porque o baixo crescimento acirrou a competição e pessoas mais escolarizadas passam a aceitar funções abaixo de sua formação. Alternativa <strong>E</strong>.</p><p>A situação de Paulo não confirma que o acesso ao trabalho esteja garantido só para quem tem curso superior (B).</p>",
  p("Leia os textos abaixo:") + tit("I - A situação de um trabalhador")
  + ap("<em>Paulo Henrique de Jesus está há quatro meses desempregado. Com o Ensino Médio completo, ou seja, 11 anos de estudo, ele perdeu a vaga que preenchia há oito anos de encarregado numa transportadora de valores, ganhando R$800,00. Desde então, e com 50 currículos já distribuídos, só encontra oferta para ganhar R$300,00, um salário mínimo. Ele aceitou trabalhar por esse valor, sem carteira assinada, como garçom numa casa de festas para fazer frente às despesas.</em>")
  + fonte("<em>O Globo</em>, 20/07/2005.") + tit("II - Uma interpretação sobre o acesso ao mercado de trabalho")
  + ap("<em>Atualmente, a baixa qualificação da mão-de-obra é um dos responsáveis pelo desemprego no Brasil.</em>")
  + p("A relação que se estabelece entre a situação (I) e a interpretação (II) e a razão para essa relação aparece em:"),
  tags=["desemprego", "escolaridade"])

X(4, "H", "Geografia", "Transportes", "<p>O país X é pequeno, desenvolvido e muito urbanizado, tem rios que congelam (o que limita a navegação e os portos) e petróleo próprio: as distâncias curtas e o combustível barato favorecem o rodoviário, depois o ferroviário, e por último o aquaviário. Alternativa <strong>A</strong>.</p><p>O país Y, grande, com rios caudalosos, litoral extenso e exportação de produtos primários de baixo valor, deveria priorizar o aquaviário e o ferroviário, que barateiam o frete de grandes volumes por longas distâncias; por isso B e D estão erradas.</p>",
  p("Leia as características geográficas dos países X e Y.")
  + tabela(["País X", "País Y"], [["desenvolvido", "subdesenvolvido"], ["pequena dimensão territorial", "grande dimensão territorial"],
          ["clima rigoroso com congelamento de alguns rios e portos", "ausência de problemas climáticos, rios caudalosos e extenso litoral"],
          ["intensa urbanização", "concentração populacional e econômica na faixa litorânea"],
          ["auto-suficiência de petróleo", "exportador de produtos primários de baixo valor agregado"]])
  + p("A partir da análise dessas características é adequado priorizar as diferentes modalidades de transporte de carga, na seguinte ordem:"),
  tags=["modais de transporte"])

X(5, "H", "História", "África", "<p>II e III estão corretas: as fronteiras traçadas pelos colonizadores europeus ignoraram a distribuição dos povos, separando grupos aparentados e juntando rivais, e depois das independências isso alimentou guerras civis, golpes e conflitos étnicos. Alternativa <strong>E</strong>.</p><p>I erra ao atribuir a divisão aos interesses da “maior potência capitalista na época da descolonização”: a partilha foi feita pelas potências europeias no fim do século XIX (Conferência de Berlim), muito antes da descolonização.</p>",
  p("Um professor apresentou os mapas abaixo numa aula sobre as implicações da formação das fronteiras no continente africano.") + "[[fig:1]]"
  + p("Com base na aula e na observação dos mapas, os alunos fizeram três afirmativas:")
  + I3("A brutal diferença entre as fronteiras políticas e as fronteiras étnicas no continente africano aponta para a artificialidade em uma divisão com objetivo de atender apenas aos interesses da maior potência capitalista na época da descolonização.",
       "As fronteiras políticas jogaram a África em uma situação de constante tensão ao desprezar a diversidade étnica e cultural, acirrando conflitos entre tribos rivais.",
       "As fronteiras artificiais criadas no contexto do colonialismo, após os processos de independência, fizeram da África um continente marcado por guerras civis, golpes de estado e conflitos étnicos e religiosos.")
  + fonte("<em>Atualidades/Vestibular 2005</em>, 1º sem., ed. Abril, p. 68.") + p("É verdadeiro apenas o que se afirma em"),
  figs(("q05", "Dois mapas da África sob o título “As fronteiras étnicas e políticas da África”: no primeiro, “Divisão política”, poucas fronteiras de traçado retilíneo separam os países; no segundo, “Divisão étnica”, o continente aparece retalhado em centenas de pequenas áreas de povos diferentes, que não coincidem com as fronteiras políticas.")),
  ["fronteiras", "colonialismo"])

X(6, "L", "Língua Portuguesa", "Variação linguística", "<p>Todos os exemplos são de palavras diferentes para as mesmas peças de roupa: terno é “fato”, paletó é “casaco”, meias são “peúgas”, suéter é “camisola”. A diferença destacada é de vocabulário (léxico). Alternativa <strong>A</strong>.</p><p>O texto não trata de pronúncia, de formação de palavras (derivação), de gênero gramatical nem de ordem das palavras na frase (sintaxe).</p>",
  p("Leia com atenção o texto:") + ap("[Em Portugal], você poderá ter alguns probleminhas se entrar numa loja de roupas desconhecendo certas sutilezas da língua. Por exemplo, não adianta pedir para ver os ternos — peça para ver os <em>fatos</em>. Paletó é <em>casaco</em>. Meias são <em>peúgas</em>. Suéter é <em>camisola</em> — mas não se assuste, porque calcinhas femininas são <em>cuecas</em>. (Não é uma delícia?)")
  + fonte("Ruy Castro. <em>Viaje Bem</em>. Ano VIII, nº 3, 78.") + p("O texto destaca a diferença entre o português do Brasil e o de Portugal quanto"),
  tags=["português de Portugal", "léxico"])

X(7, "H", "História", "Era Vargas", "<p>O parêntese “nunca esse adjetivo foi tão próprio” alude ao papel de Lacerda na crise de 1954: sua campanha contra Vargas e o atentado da rua Tonelero, em que Lacerda foi alvo, levaram à pressão que terminou no suicídio. E a comoção popular com a morte de Getúlio fez recuar os conservadores, que adiaram o golpe planejado. Alternativa <strong>A</strong>.</p><p>Lacerda não foi “responsável direto” pela morte (D), e o suicídio não facilitou regimes autoritários de imediato; ao contrário, permitiu a posse de Juscelino em 1955 (E).</p>",
  p("Zuenir Ventura, em seu livro “Minhas memórias dos outros” (São Paulo: Planeta do Brasil, 2005), referindo-se ao fim da “Era Vargas” e ao suicídio do presidente em 1954, comenta:")
  + ap("<em>Quase como castigo do destino, dois anos depois eu iria trabalhar no jornal de Carlos Lacerda, o inimigo mortal de Vargas (e nunca esse adjetivo foi tão próprio).</em>")
  + p("Diante daquele contexto histórico, muitos estudiosos acreditam que, com o suicídio, Getúlio Vargas atingiu não apenas a si mesmo, mas o coração de seus aliados e a mente de seus inimigos.",
      "A afirmação que aparece “entre parênteses” no comentário e uma conseqüência política que atingiu os inimigos de Vargas aparecem, respectivamente, em:"),
  tags=["Getúlio Vargas", "Carlos Lacerda", "1954"])

X(8, "H", "Geografia", "Orientação", "<p>Se o sol nasce à direita dos meninos, a direita deles é o leste: eles estão voltados para o norte, e o caminho “à esquerda” que indicam segue para oeste. A cada encruzilhada, dobrar à esquerda gira a direção 90° no sentido anti-horário: de oeste para sul, e de sul para leste. O senhor caminhou para oeste, sul e leste. Alternativa <strong>A</strong>.</p><p>Quem toma a esquerda do próprio senhor, de frente para os meninos (olhando para o sul), chega a leste, norte e oeste (D); o gabarito considera a esquerda indicada pelos meninos.</p>",
  p("Leia o texto abaixo.") + tit("O jardim de caminhos que se bifurcam")
  + ap("(....) Uma lâmpada aclarava a plataforma, mas os rostos dos meninos ficavam na sombra. Um me perguntou: O senhor vai à casa do Dr. Stephen Albert? Sem aguardar resposta, outro disse: A casa fica longe daqui, mas o senhor não se perderá se tomar esse caminho à esquerda e se em cada encruzilhada do caminho dobrar à esquerda.")
  + fonte("Adaptado. Borges, J. <em>Ficções</em>. Rio de Janeiro: Globo, 1997. p. 96.")
  + p("Quanto à cena descrita acima, considere que") + I3("o sol nasce à direita dos meninos;", "o senhor seguiu o conselho dos meninos, tendo encontrado duas encruzilhadas até a casa.")
  + p("Concluiu-se que o senhor caminhou, respectivamente, nos sentidos:"),
  tags=["pontos cardeais", "Borges"])

X(9, "L", "Literatura", "Modernismo", "<p>O poema contrasta modos de falar (“falem mole”, “arranhem os erres”, “escancarem as vogais”) e a diferença de valor do dinheiro entre o Sul e o Norte (“o quinhentos réis meridional / vira cinco tostões”), que remete às desigualdades econômicas. As diferenças são linguísticas e econômicas. Alternativa <strong>B</strong>.</p><p>Não há referência a etnias, religiões, folclore ou literatura.</p>",
  p("As dimensões continentais do Brasil são objeto de reflexões expressas em diferentes linguagens. Esse tema aparece no seguinte poema:")
  + ap("“(....)<br>Que importa que uns falem mole descansado<br>Que os cariocas arranhem os erres na garganta<br>Que os capixabas e paroaras escancarem as vogais?<br>Que tem se o quinhentos réis meridional<br>Vira cinco tostões do Rio pro Norte?<br>Junto formamos este assombro de misérias e grandezas,<br>Brasil, nome de vegetal! (....)”")
  + fonte("Mário de Andrade. <em>Poesias completas</em>. 6. ed. São Paulo: Martins Editora, 1980.")
  + p("O texto poético ora reproduzido trata das diferenças brasileiras no âmbito"),
  tags=["Mário de Andrade", "variação linguística"])

X(10, "L", "Língua Portuguesa", "Interpretação de tirinha", "<p>Na tira, o personagem entra em pânico e desliga o telefone porque do outro lado atendeu uma pessoa de verdade: ele já está tão acostumado às máquinas que o contato humano o assusta. A contradição é entre as relações pessoais e o avanço tecnológico, que deveria facilitá-las. Alternativa <strong>A</strong>.</p><p>A tira não fala de exclusão digital, de neoliberalismo nem de ignorância dos cidadãos.</p>",
  "[[fig:1]]" + p("A situação abordada na tira torna explícita a <u>contradição</u> entre a"),
  figs(("q10", "Tira “Frank e Ernest”, de Thaves: um homem diante de uma máquina de escrever com cara de susto, e o outro personagem comenta: “Entrei em pânico e desliguei! Que tipo de empresa deixaria uma pessoa de verdade atender o telefone?”")),
  ["tecnologia", "tirinha"], alts=dict(D[10], A="relações pessoais e o avanço tecnológico."))

X(11, "N", "Biologia", "Nutrição", "<p>As vitaminas A, D, E e K são lipossolúveis: dissolvem-se nas gorduras e são absorvidas no intestino junto com elas, nas micelas formadas com a bile. Se o remédio impede a digestão e a absorção das gorduras, essas vitaminas saem com as fezes. Alternativa <strong>E</strong>.</p><p>Vitaminas não são fonte de energia (A), não reagem com o remédio (C) e não são quebradas pelas lipases (D).</p>",
  p("A obesidade, que nos países desenvolvidos já é tratada como epidemia, começa a preocupar especialistas no Brasil. Os últimos dados da Pesquisa de Orçamentos Familiares, realizada entre 2002 e 2003 pelo IBGE, mostram que 40,6% da população brasileira estão acima do peso, ou seja, 38,8 milhões de adultos. Desse total, 10,5 milhões são considerados obesos. Várias são as dietas e os remédios que prometem um emagrecimento rápido e sem riscos. Há alguns anos foi lançado no mercado brasileiro um remédio de ação diferente dos demais, pois inibe a ação das lipases, enzimas que aceleram a reação de quebra de gorduras. Sem serem quebradas elas não são absorvidas pelo intestino, e parte das gorduras ingeridas é eliminada com as fezes. Como os lipídios são altamente energéticos, a pessoa tende a emagrecer. No entanto, esse remédio apresenta algumas contra-indicações, pois a gordura não absorvida lubrifica o intestino, causando desagradáveis diarréias. Além do mais, podem ocorrer casos de baixa absorção de vitaminas lipossolúveis, como as A, D, E e K, pois"),
  tags=["vitaminas lipossolúveis", "lipases"])

X(12, "M", "Matemática", "Leitura de gráficos", "<p>O real está mais desvalorizado quando um dólar custa mais reais. O pico do gráfico, perto de R$ 3,90, ocorre no fim de 2002, pouco antes de janeiro de 2003. Alternativa <strong>B</strong>.</p><p>No fim de 2001 e no início de 2005 o dólar estava entre R$ 2,40 e R$ 2,80, e no início de 2003 já havia recuado para cerca de R$ 3,50.</p>",
  p("No gráfico abaixo, mostra-se como variou o valor do dólar, em relação ao real, entre o final de 2001 e o início de 2005. Por exemplo, em janeiro de 2002, um dólar valia cerca de R$ 2,40.")
  + "[[fig:1]]" + fonte("Fonte: Banco Central do Brasil.") + p("Durante esse período, a época em que o real esteve mais desvalorizado em relação ao dólar foi no"),
  figs(("q12", "Gráfico de linha da cotação do dólar em reais, de dezembro de 2001 a janeiro de 2005, com escala de 1,20 a 4,00. A curva começa perto de 2,40, sobe a partir de meados de 2002 até o pico de cerca de 3,90 no fim de 2002, cai para perto de 2,90 ao longo de 2003, tem uma pequena alta para 3,20 em meados de 2004 e termina perto de 2,70 no início de 2005.")),
  ["câmbio"])

X(13, "N", "Química", "Chuva ácida", "<p>O carvão mineral contém enxofre. Na queima, forma SO2 e SO3, que reagem com a água e originam ácido sulfúrico (H2SO4); a água do riacho fica ácida e mata peixes e plantas. Alternativa <strong>E</strong>.</p><p>A queima não produz ácido clorídrico (C) e o monóxido de carbono não aquece a água (B).</p>",
  p("Diretores de uma grande indústria siderúrgica, para evitar o desmatamento e adequar a empresa às normas de proteção ambiental, resolveram mudar o combustível dos fornos da indústria. O carvão vegetal foi então substituído pelo carvão mineral. Entretanto, foram observadas alterações ecológicas graves em um riacho das imediações, tais como a morte dos peixes e dos vegetais ribeirinhos. Tal fato pode ser justificado em decorrência"),
  tags=["carvão mineral", "óxidos de enxofre"], quim=True,
  alts=A5("da diminuição de resíduos orgânicos na água do riacho, reduzindo a demanda de oxigênio na água.",
          "do aquecimento da água do riacho devido ao monóxido de carbono liberado na queima do carvão.",
          "da formação de ácido clorídrico no riacho a partir de produtos da combustão na água, diminuindo o pH.",
          "do acúmulo de elementos no riacho, tais como, ferro, derivados do novo combustível utilizado.",
          "da formação de ácido sulfúrico no riacho a partir dos óxidos de enxofre liberados na combustão."))

X(14, "N", "Física", "Energia", "<p>Ao puxar a corda, o arco se deforma e armazena energia potencial elástica. Quando o menino solta a flecha, o arco volta à forma original e essa energia vira energia cinética da flecha. Alternativa <strong>C</strong>.</p><p>A energia gravitacional entra só depois, conforme a flecha sobe ou desce na trajetória, e não no instante do lançamento.</p>",
  p("Observe a situação descrita na tirinha abaixo.") + "[[fig:1]]" + fonte("Francisco Caruso &amp; Luisa Daou. <em>Tirinhas de Física</em>, vol. 2, CBPF, Rio de Janeiro, 2000.")
  + p("Assim que o menino lança a flecha, há transformação de um tipo de energia em outra. A transformação, nesse caso, é de energia"),
  figs(("q14", "Tirinha em três quadros. Um menino com arco mira um garoto amarrado a uma árvore com uma maçã na cabeça; uma menina pergunta se ele quer matá-lo ou acertar a maçã. Ela o aconselha a mirar mais para cima para compensar a gravidade; ele mira mais alto. No último quadro, a flecha acerta a maçã, e o garoto amarrado diz: “Ufa! Ainda bem que Lisa chegou!”.")),
  ["arco e flecha", "energia elástica"])

X(15, "N", "Física", "Movimento circular", "<p>Ao girar o peso em círculo, o fio precisa puxá-lo para o centro: é a força centrípeta, que aumenta com a velocidade. Essa tração no fio, transmitida pelo tubo, fica maior que o peso da garrafa e a faz subir. Alternativa <strong>D</strong>.</p><p>Não há líquido envolvendo a garrafa para gerar empuxo (C), e a gravidade (B) puxa a garrafa para baixo, e não para cima.</p>",
  "[[fig:1]]" + fonte("Adaptado. Luisa Daou &amp; Francisco Caruso, <em>Tirinhas de Física</em>, vol. 2, CBPF, Rio de Janeiro, 2000.")
  + p("Observe o fenômeno indicado na tirinha acima.", "A força que atua sobre o peso e produz o deslocamento vertical da garrafa é a força"),
  figs(("q15", "Tirinha em dois quadros. No primeiro, uma mão segura um tubo; por dentro dele passa um fio com um pequeno peso na ponta de cima e uma garrafa com água pendurada na ponta de baixo; um balão diz: “Vou levantar a garrafa sem puxar o fio ou o peso...”. No segundo, a mão gira o tubo e o peso descreve um círculo horizontal acima dele, e a garrafa aparece mais alta, perto do tubo.")),
  ["força centrípeta"], alts=dict(D[15], E="elástica."))

X(16, "H", "Geografia", "Demografia", "<p>Só I está correta: o Brasil tem 43,2% de jovens, contra cerca de 20% a 26% nos EUA e na Suécia, e os jovens são os que mais usam a internet. Alternativa <strong>A</strong>.</p><p>II e III não se apoiam nos dados: nem a tabela nem o texto falam de distribuição por classes sociais ou de banda larga, e o acesso à internet no Brasil era muito desigual entre as classes.</p>",
  tabela(["País", "Tipo", "Jovens", "Adultos", "Idosos"], [['Estados Unidos', 'maduro', '25,7', '57,4', '16,9'], ['Suécia', 'maduro', '19,8', '56,7', '23,5'], ['Brasil', 'em transição', '43,2', '48,5', '8,3'], ['Bangladesh', 'jovem', '50,2', '44,8', '5,0'], ['Nigéria', 'jovem', '55,4', '40,1', '4,5']])
  + fonte("Jovens: até 19 anos; adultos: de 20 a 59 anos; idosos: 60 anos ou mais. Tipo: classificação do país (“maduro”, em transição ou “jovem”).") + fonte("Distribuição etária da população em alguns países (em %). Elaborada a partir de dados do US Bureau of Census. <em>World Population Profile</em>: 1999.")
  + ap("<em>Os brasileiros tiveram, em junho, o maior tempo de navegação residencial na internet entre 11 países monitorados pelo Ibope/NetRatings: média mensal de 16 horas e 54 minutos por pessoa. O país ficou à frente de nações como a França, Japão, Estados Unidos e Espanha.</em>")
  + fonte("Adaptado. <em>Folha de S.Paulo</em>, 23/07/2005.")
  + p("Com base na tabela e no texto acima, analise os possíveis motivos para a liderança do Brasil no tempo de uso da internet.")
  + I3("O país tem uma estrutura populacional com maior percentual de jovens do que os países da Europa e os EUA.",
       "O uso de internet em casa se distribui igualmente entre as classes A, B e C, o que demonstra iniciativas de inclusão digital.",
       "A adesão ao sistema de internet por banda larga ocorre, porque essa tecnologia promove a mudança de comportamento dos usuários.")
  + p("Está correto apenas o que se afirma em"),
  tags=["estrutura etária", "internet"])

LUMINOL = (tit("Texto para as questões 17 e 18.")
  + ap("<em>Na investigação forense, utiliza-se luminol, uma substância que reage com o ferro presente na hemoglobina do sangue, produzindo luz que permite visualizar locais contaminados com pequenas quantidades de sangue, mesmo em superfícies lavadas.</em>",
       "<em>É proposto que, na reação do luminol (I) em meio alcalino, na presença de peróxido de hidrogênio (II) e de um metal de transição (M<sup>n+</sup>), forma-se o composto 3-amino ftalato (III) que sofre uma relaxação dando origem ao produto final da reação (IV), com liberação de energia (hν) e de gás nitrogênio (N2).</em>")
  + fonte("Adaptado. <em>Química Nova</em>, 25, nº 6, 2002. pp. 1003-1011.") + "[[fig:1]]"
  + ap("Dados: pesos moleculares: Luminol = 177; 3-amino ftalato = 164"))
F_LUM = figs(("q17", "Esquema da reação: luminol (I), uma estrutura com anel benzênico ligado a NH2 e a um anel com dois grupos C=O e dois NH, reage com H2O2 (II) e Mn+ e forma o 3-amino ftalato excitado (III, entre colchetes com asterisco, com dois grupos carboxilato). Este se converte no 3-amino ftalato (IV), liberando hν e N2."))
X(17, "N", "Química", "Reações químicas", "<p>A luz vem da própria reação química: o 3-amino ftalato é formado em estado excitado e, ao relaxar, emite fótons. Emissão de luz por reação química é quimiluminescência. Alternativa <strong>C</strong>.</p><p>Não há absorção prévia de radiação, como na fluorescência e na fosforescência (A, D), nem corrente elétrica (B) ou reação nuclear (E).</p>",
  LUMINOL + p("Na reação <u>do luminol</u>, está ocorrendo o fenômeno de"), F_LUM, ["luminol", "quimiluminescência"], quim=True)
X(18, "N", "Química", "Estequiometria", "<p>A proporção é de 1 mol de luminol para 1 mol de produto IV. 54 g de luminol são 54/177 ≈ 0,305 mol, que daria 0,305 × 164 ≈ 50,0 g de 3-amino ftalato com rendimento total. Com 70%: 0,7 × 50,0 ≈ 35,0 g. Alternativa <strong>D</strong>.</p><p>A alternativa C (86,0) multiplica as massas sem dividir, e B (114,8) esquece a conversão em mols.</p>",
  LUMINOL + p("Na análise de uma amostra biológica para análise forense, utilizou-se 54 g de luminol e peróxido de hidrogênio em excesso, obtendo-se um rendimento final de 70%. Sendo assim, a quantidade do produto final (IV) formada na reação foi de"),
  F_LUM, ["rendimento", "massa molar"], quim=True)

X(19, "H", "História", "Amazônia", "<p>A ordem é: o surto da borracha (fim do século XIX e início do XX), a criação da Sudam (1966, no regime militar), o Projeto Ferro Carajás (início dos anos 1980) e o Projeto Calha Norte (1985). Ou seja, IV, III, II, I. Alternativa <strong>A</strong>.</p><p>O Calha Norte, de ocupação militar das fronteiras ao norte do Amazonas, é o mais recente dos quatro.</p>",
  p("Observe as seguintes estratégias para a ocupação da Amazônia Brasileira.")
  + '<ol type="I"><li>Desenvolvimento de infra-estrutura do projeto Calha Norte;</li><li>Exploração mineral por meio do Projeto Ferro Carajás;</li><li>Criação da Superintendência para o Desenvolvimento da Amazônia;</li><li>Extração do látex durante o chamado Surto da Borracha.</li></ol>'
  + p("A ordenação desses elementos, desde o mais antigo ao mais recente, é a seguinte:"),
  tags=["ocupação da Amazônia"])

PORT = (tit("Texto para as questões 20 e 21.") + p("Cândido Portinari (1903-1962), um dos mais importantes artistas brasileiros do século XX, tratou de diferentes aspectos da nossa realidade em seus quadros.")
  + "[[fig:1]]" + p("Sobre a temática dos “Retirantes”, Portinari também escreveu o seguinte poema:") + "[[fig:2]]"
  + fonte("Cândido Portinari. <em>Poemas</em>. Rio de Janeiro: J. Olympio, 1964."))
F_PORT = figs(("q20a", "Quatro reproduções de quadros de Portinari, numeradas. 1: casais dançando num salão. 2: um grupo de figuras magras e esfarrapadas, com crianças e trouxas, em paisagem árida. 3: uma família de retirantes em pé, de roupas pobres, com crianças, contra um céu claro. 4: uma figura solitária com chapéu e roupa de retalhos coloridos, como um arlequim."),
              ("q20b", "Fragmento do poema de Portinari sobre os retirantes: descreve homens de ventre enorme, mulheres com trouxas, corpos disformes com panos sujos e rasgados, vindos de terras secas e de pedregulhos que doem como fagulhas de carvão, e mulheres barrigudas carregando garotos que choramingam."))
X(20, "L", "Artes", "Artes visuais", "<p>O poema descreve os retirantes da seca: famílias pobres, de corpos deformados, com trouxas e crianças, vindas das terras secas. As obras 2 e 3 mostram exatamente grupos de retirantes esfarrapados com crianças. Alternativa <strong>C</strong>.</p><p>A obra 1 retrata um baile e a 4, uma figura solitária de arlequim, temas sem relação com a migração da seca.</p>",
  PORT + p("Das quatro obras reproduzidas, assinale aquelas que abordam a problemática que é tema do poema."), F_PORT, ["Portinari", "retirantes"])
X(21, "N", "Biologia", "Parasitoses", "<p>O ciclo do <em>Schistosoma mansoni</em> precisa de pessoas infectadas (que eliminam ovos nas fezes) e de caramujos do gênero <em>Biomphalaria</em>, hospedeiros intermediários, em água doce. Sem saneamento, as fezes chegam aos rios e lagoas, e as larvas (cercárias) penetram na pele de quem entra na água. Alternativa <strong>C</strong>.</p><p>Não há vacina contra a esquistossomose, e ela não é transmitida por insetos, roedores ou gatos.</p>",
  PORT + p("No texto de Portinari, algumas das pessoas descritas provavelmente estão infectadas com o verme <em>Schistosoma mansoni</em>. Os “homens de enorme ventre bojudo” corresponderiam aos doentes da chamada “barriga d’água”.",
           "O ciclo de vida do <em>Schistosoma mansoni</em> e as condições sócio-ambientais de um local são fatores determinantes para maior ou menor incidência dessa doença. O aumento da incidência da esquistossomose deve-se à presença de"),
  F_PORT, ["esquistossomose", "saneamento"])

X(22, "N", "Biologia", "Citologia", "<p>A amostra perdeu 200 − 80 = 120 mg de água, ou seja, 120/200 = 60% da massa era água. Pela tabela, esse é o teor do tecido conjuntivo. Alternativa <strong>D</strong>.</p><p>Quem toma os 80 mg restantes como água chega a 40%, valor que não está na tabela; a substância cinzenta (85%) e as hemácias (65%) têm teores diferentes.</p>",
  p("A água é um dos componentes mais importantes das células. A tabela abaixo mostra como a quantidade de água varia em seres humanos, dependendo do tipo de célula. Em média, a água corresponde a 70% da composição química de um indivíduo normal.")
  + tabela(["Tipo de célula", "Quantidade de água"], [["Tecido nervoso – substância cinzenta", "85%"], ["Tecido nervoso – substância branca", "70%"], ["Medula óssea", "75%"],
           ["Tecido conjuntivo", "60%"], ["Tecido adiposo", "15%"], ["Hemácias", "65%"], ["Ossos (sem medula)", "20%"]])
  + fonte("Fonte: L.C. Junqueira e J. Carneiro. <em>Histologia Básica</em>. 8. ed., Rio de Janeiro: Guanabara Koogan, 1985.")
  + p("Durante uma biópsia, foi isolada uma amostra de tecido para análise em um laboratório. Enquanto intacta, essa amostra pesava 200 mg. Após secagem em estufa, quando se retirou toda a água do tecido, a amostra passou a pesar 80 mg. Baseado na tabela, pode-se afirmar que essa é uma amostra de"),
  tags=["água nas células", "porcentagem"],
  alts=A5("tecido nervoso – substância cinzenta.", "tecido nervoso – substância branca.", "hemácias.", "tecido conjuntivo.", "tecido adiposo."))

X(23, "H", "Geografia", "Desigualdade", "<p>O Sul da Ásia (cerca de 40% a 45%) e a África Subsaariana (46% a 50%) têm, em todos os anos, as maiores porcentagens de população vivendo com menos de US$ 1 por dia. Alternativa <strong>A</strong>.</p><p>O total mundial caiu de 28,3% para 24,0% (B); na África Subsaariana o índice subiu até 1993 e depois caiu (C); a tabela traz porcentagens, não números absolutos (D); e o Oriente Médio e Norte da África caiu de 4,3% para 1,9% (E).</p>",
  p("Analise o quadro acerca da distribuição da miséria no mundo, nos anos de 1987 a 1998.") + tit("Mapa da Miséria — população que vive com menos de US$ 1 por dia (em %)")
  + tabela(["Região", "1987", "1990", "1993", "1996", "1998*"],
           [["Extremo Oriente e Pacífico", "26,6", "27,6", "25,2", "14,9", "15,3"], ["Europa e Ásia Central", "0,2", "1,6", "4,0", "5,1", "5,1"],
            ["América Latina e Caribe", "15,3", "16,8", "15,3", "15,6", "15,6"], ["Oriente Médio e Norte da África", "4,3", "2,4", "1,9", "1,8", "1,9"],
            ["Sul da Ásia", "44,9", "44,0", "42,4", "42,3", "40,0"], ["África Subsaariana", "46,6", "47,7", "49,7", "48,5", "46,3"], ["Mundo", "28,3", "29,0", "28,1", "24,5", "24,0"]])
  + fonte("*Preliminar. Fonte: Banco Mundial. Adaptado. <em>Gazeta Mercantil</em>, 17 de outubro de 2001, p. A-6.")
  + p("A leitura dos dados apresentados permite afirmar que, no período considerado,"),
  tags=["pobreza", "leitura de tabela"])

X(24, "H", "Geografia", "Espaço agrário", "<p>Entre 1990 e 2002, a produção de grãos quase dobrou (de 56,0 para 97,5 milhões de toneladas), enquanto a área plantada ficou quase igual (de 36,8 para 37,8 milhões de hectares). Produzir muito mais na mesma área é ganho de produtividade, ligado à mecanização e à tecnologia em lavouras como a soja. Alternativa <strong>A</strong>.</p><p>Não houve incorporação proporcional de terras (B), e a modernização reduziu, em vez de aumentar, o uso de mão de obra (C).</p>",
  "[[fig:1]]" + p("Considerando os conhecimentos sobre o espaço agrário brasileiro e os dados apresentados no gráfico, é correto afirmar que, no período indicado,"),
  figs(("q24", "Gráfico “Produção de grãos” (soja, trigo, milho, arroz e algodão) de 1990 a 2002, este último como previsão. A linha de produção, em milhões de toneladas, sobe de 56,0 em 1990 para 73,6 em 1996 e 97,5 em 2002. A linha de área plantada, em milhões de hectares, fica quase reta: 36,8 em 1990, 36,3 em 1996 e 37,8 em 2002. Fontes: Censo Agropecuário, IBGE e Ministério da Agricultura.")),
  ["produtividade agrícola", "modernização do campo"])

X(25, "H", "Sociologia", "Trabalho", "<p>Na primeira tira, quem é “pisado pelos governantes” só quer o direito de pisar também; na segunda, a fábula da cigarra e da formiga é atualizada: a formiga trabalhou duro a vida inteira e, no fim, alguém pisa nela. As duas ironizam o trabalhador que se esforça a vida toda e termina desamparado, como os aposentados. Alternativa <strong>A</strong>.</p><p>A atualização da fábula é o recurso, e não a ideia defendida (B).</p>",
  "[[fig:1]][[fig:2]]" + p("As tiras ironizam uma célebre fábula e a conduta dos governantes. Tendo como referência o estado atual dos países periféricos, pode-se afirmar que nessas histórias está contida a seguinte idéia:"),
  figs(("q25a", "Tira “Graúna”, de Henfil, em três quadros. Um personagem de chapéu reclama: “Toda hora somos pisados pelos governantes!”, e a Graúna concorda. Ele diz: “Vocês, mulheres, têm que exigir seus direitos!”. No último quadro, explica: “Exigir o direito de pisar também! Com seus pés maravilhosos!”, enquanto se joga aos pés dela, que diz “Ai!”."),
       ("q25b", "Tira “Frank e Ernest”, de Thaves, intitulada “Fábulas dos anos 90”: um homem conta ao outro: “Lembram-se da história da cigarra e da formiga? A formiga trabalhou duro a vida inteira e, no fim... alguém pisa nela.”")),
  ["Henfil", "cigarra e a formiga"])

X(26, "M", "Física", "Energia elétrica", "<p>Consumo diário: ar condicionado 1,5 × 8 = 12 kWh; chuveiro 3,3 × 1/3 = 1,1 kWh; freezer 0,2 × 10 = 2 kWh; geladeira 0,35 × 10 = 3,5 kWh; lâmpadas 0,10 × 6 = 0,6 kWh. Total: 19,2 kWh por dia, ou 576 kWh em 30 dias. A R$ 0,40 o kWh, o custo é 576 × 0,40 ≈ R$ 230. Alternativa <strong>E</strong>.</p>",
  p("Podemos estimar o consumo de energia elétrica de uma casa considerando as principais fontes desse consumo. Pense na situação em que apenas os aparelhos que constam da tabela abaixo fossem utilizados diariamente da mesma forma.")
  + tabela(["Aparelho", "Potência (KW)", "Tempo de uso diário (horas)"], [["Ar condicionado", "1,5", "8"], ["Chuveiro elétrico", "3,3", "1/3"], ["Freezer", "0,2", "10"], ["Geladeira", "0,35", "10"], ["Lâmpadas", "0,10", "6"]])
  + fonte("Tabela: A tabela fornece a potência e o tempo efetivo de uso diário de cada aparelho doméstico.")
  + p("Supondo que o mês tenha 30 dias e que o custo de 1 KWh é de R$ 0,40, o consumo de energia elétrica mensal dessa casa, é de aproximadamente"),
  tags=["kWh", "consumo de energia"], alts=A5("R$ 135.", "R$ 165.", "R$ 190.", "R$ 210.", "R$ 230."))

X(27, "N", "Biologia", "Evolução", "<p>Para Darwin, a variação já existe na população: há cascavéis que chocalham menos. Como as barulhentas são achadas e mortas pelo homem, as silenciosas sobrevivem e se reproduzem mais, e a característica aumenta na população. Alternativa <strong>D</strong>.</p><p>As outras alternativas dizem que a necessidade causa a mudança ou que as mutações surgem “para” adaptar o animal, ideias lamarckistas ou finalistas, e não darwinistas.</p>",
  p("As cobras estão entre os animais peçonhentos que mais causam acidentes no Brasil, principalmente na área rural. As cascavéis (<em>Crotalus</em>), apesar de extremamente venenosas, são cobras que, em relação a outras espécies, causam poucos acidentes a humanos. Isso se deve ao ruído de seu “chocalho”, que faz com que suas vítimas percebam sua presença e as evitem. Esses animais só atacam os seres humanos para sua defesa e se alimentam de pequenos roedores e aves. Apesar disso, elas têm sido caçadas continuamente, por serem facilmente detectadas. Ultimamente os cientistas observaram que essas cobras têm ficado mais silenciosas, o que passa a ser um problema, pois, se as pessoas não as percebem, aumentam os riscos de acidentes.",
    "A explicação darwinista para o fato de a cascavel estar ficando mais silenciosa é que"),
  tags=["seleção natural", "Darwin"])

X(28, "N", "Biologia", "Ecologia", "<p>Cabras e porcos, sem predadores na ilha, devoraram a vegetação rasteira, as cascas dos arbustos e depois ovos de tartarugas e aves e caranguejos. Faltou uma interação equilibrada entre os seres vivos, e o ecossistema foi alterado. Alternativa <strong>B</strong>.</p><p>O desequilíbrio começou com a destruição da vegetação, bem antes de os porcos comerem cabritos (D), e espécies exóticas reduzem, e não aumentam, a biodiversidade (E).</p>",
  p("Há quatro séculos alguns animais domésticos foram introduzidos na Ilha da Trindade como “reserva de alimento”. Porcos e cabras soltos davam boa carne aos navegantes de passagem, cansados de tanto peixe no cardápio. Entretanto, as cabras consumiram toda a vegetação rasteira e ainda comeram a casca dos arbustos sobreviventes. Os porcos revolveram raízes e a terra na busca de semente. Depois de consumir todo o verde, de volta ao estado selvagem, os porcos passaram a devorar qualquer coisa: ovos de tartarugas, de aves marinhas, caranguejos e até cabritos pequenos.",
    "Com base nos fatos acima, pode-se afirmar que"),
  tags=["espécies exóticas", "desequilíbrio ecológico"])

X(29, "M", "Matemática", "Razão e proporção", "<p>Com gasolina, 6.000 km pedem 600 litros, a R$ 2,20: R$ 1.320 por mês. Com GNV, 6.000 km pedem 500 m³, a R$ 1,10: R$ 550 por mês. A economia é de R$ 770 por mês, e 3.000/770 ≈ 3,9, ou seja, cerca de 4 meses. Alternativa <strong>B</strong>.</p>",
  p("O gás natural veicular (GNV) pode substituir a gasolina ou álcool nos veículos automotores. Nas grandes cidades, essa possibilidade tem sido explorada, principalmente, pelos táxis, que recuperam em um tempo relativamente curto o investimento feito com a conversão por meio da economia proporcionada pelo uso do gás natural. Atualmente, a conversão para gás natural do motor de um automóvel que utiliza a gasolina custa R$ 3.000,00. Um litro de gasolina permite percorrer cerca de 10 km e custa R$ 2,20, enquanto um metro cúbico de GNV permite percorrer cerca de 12 km e custa R$ 1,10. Desse modo, um taxista que percorra 6.000 km por mês recupera o investimento da conversão em aproximadamente"),
  tags=["GNV", "economia"])

X(30, "N", "Biologia", "Ecologia", "<p>O Gráfico II mostra que o maior número de espécies (40) vive com pH ótimo entre 7 e 8. No Gráfico I, o ambiente com pH nessa faixa é o D, com pH perto de 7,7. Alternativa <strong>D</strong>.</p><p>A tem pH 10 (cerca de 20 espécies), B e C ficam perto de 6 (cerca de 20 a 30) e E, com pH 5, entra na faixa de 20 espécies.</p>",
  p("Um estudo caracterizou 5 ambientes aquáticos, nomeados de A a E, em uma região, medindo parâmetros físico-químicos de cada um deles, incluindo o pH nos ambientes. O Gráfico I representa os valores de pH dos 5 ambientes. Utilizando o gráfico II, que representa a distribuição estatística de espécies em diferentes faixas de pH, pode-se esperar um maior número de espécies no ambiente:")
  + "[[fig:1]]",
  figs(("q30", "Gráfico I, de barras, com o pH de cada ambiente: A, 10; B, cerca de 5,7; C, 6; D, cerca de 7,7; E, 5. Gráfico II, histograma do número de espécies por faixa de pH ótimo de sobrevida: 4 a 5, 10 espécies; 5 a 6, 20; 6 a 7, 30; 7 a 8, 40; 8 a 9, 30; 9 a 10, 20.")),
  ["pH", "biodiversidade"], alts=A5("A.", "B.", "C.", "D.", "E."))

X(31, "N", "Química", "Resíduos sólidos", "<p>Plásticos recicláveis permitem reaproveitar o material, o que reduz o uso de petróleo (matéria-prima não renovável) e o acúmulo de lixo. Alternativa <strong>D</strong>.</p><p>Metais não são renováveis (A); a queima libera gás carbônico e substâncias tóxicas, e não resolve o problema (B, C); e reciclar não serve para “aumentar a qualidade” do produto (E).</p>",
  p("Os plásticos, por sua versatilidade e menor custo relativo, têm seu uso cada vez mais crescente. Da produção anual brasileira de cerca de 2,5 milhões de toneladas, 40% destinam-se à indústria de embalagens. Entretanto, este crescente aumento de produção e consumo resulta em lixo que só se reintegra ao ciclo natural ao longo de décadas ou mesmo de séculos. Para minimizar esse problema uma ação possível e adequada é"),
  tags=["reciclagem", "plásticos"])

X(32, "M", "Matemática", "Probabilidade", "<p>Método I: cada aluno do diurno tem chance 1/2 × 1/300 = 1/600, e cada aluno do noturno, 1/2 × 1/240 = 1/480, maior. Método II: cada aluno do diurno tem 1/16 × 1/30 = 1/480, e cada aluno do noturno, 1/16 × 1/40 = 1/640, menor. No I o noturno leva vantagem; no II, o diurno. Alternativa <strong>D</strong>.</p><p>Só o sorteio direto entre os 540 daria a mesma chance (1/540) a todos.</p>",
  p("Um aluno de uma escola será escolhido por sorteio para representá-la em uma certa atividade. A escola tem dois turnos. No diurno há 300 alunos, distribuídos em 10 turmas de 30 alunos. No noturno há 240 alunos, distribuídos em 6 turmas de 40 alunos.",
    "Em vez do sorteio direto envolvendo os 540 alunos, foram propostos dois outros métodos de sorteio.",
    "<strong>Método I</strong>: escolher ao acaso um dos turnos (por exemplo, lançando uma moeda) e, a seguir, sortear um dos alunos do turno escolhido.",
    "<strong>Método II</strong>: escolher ao acaso uma das 16 turmas (por exemplo, colocando um papel com o número de cada turma em uma urna e sorteando uma delas) e, a seguir, sortear um dos alunos dessa turma.",
    "Sobre os métodos <strong>I</strong> e <strong>II</strong> de sorteio é correto afirmar:"),
  tags=["probabilidade condicional", "sorteio"])

X(33, "L", "Língua Portuguesa", "Denotação e conotação", "<p>Em C, “dicionário-padrão” nomeia literalmente um tipo de dicionário: é o sentido próprio, denotativo. Alternativa <strong>C</strong>.</p><p>Nas demais o sentido é figurado: “cumprida a sol” (vida de trabalho sob o sol), “cenários” (os desenhos das impressões digitais), “bateria” (a energia do menino) e “fazer cócegas no raciocínio” (provocar o pensamento).</p>",
  p("O termo (ou expressão) destacado que está empregado em seu sentido próprio, denotativo ocorre em"),
  figs(("q33a", "Trecho de canção: “(....) É de laço e de nó / De gibeira o jiló / Dessa vida, cumprida a sol (....)”, com a expressão “cumprida a sol” destacada. Fonte: Renato Teixeira, Romaria, Kuarup Discos, setembro de 1992."),
       ("q33b", "Trova: “Protegendo os inocentes / é que Deus, sábio demais, / põe cenários diferentes / nas impressões digitais.”, com a palavra “cenários” destacada. Fonte: Maria N. S. Carvalho, Evangelho da Trova."),
       ("q33d", "Tirinha do Menino Maluquinho em dois quadros: uma mulher pensativa diz “Às vezes eu tenho a impressão...”, e no quadro seguinte, enquanto o menino pula agitado entre ela e outra mulher, completa: “...de que a bateria dele não acaba!”, com a palavra “bateria” destacada. Fonte: O Globo, agosto de 2002.")),
  ["sentido denotativo", "linguagem figurada"],
  alts=A5("[[fig:1]]", "[[fig:2]]",
          "“O <u><strong>dicionário-padrão</strong></u> da língua e os dicionários unilíngües são os tipos mais comuns de dicionários. Em nossos dias, eles se tornaram um objeto de consumo obrigatório para as nações civilizadas e desenvolvidas.” (Maria T. Camargo Biderman. <em>O dicionário-padrão da língua</em>. Alfa (28), 2743, 1974 Supl.)",
          "[[fig:3]]",
          "“Humorismo é a arte de <u><strong>fazer cócegas no raciocínio</strong></u> dos outros. Há duas espécies de humorismo: o trágico e o cômico. O trágico é o que não consegue fazer rir; o cômico é o que é verdadeiramente trágico para se fazer.” (Leon Eliachar. Acessado em julho de 2005.)"))

X(34, "M", "Matemática", "Geometria plana", "<p>Ponha a estrada CD no eixo x e A e B em (0, 40) e (40, 40). Ser equidistante de A e B coloca o ponto na mediatriz de AB, x = 20, que é a perpendicular a CD por seu ponto médio. Se ele está a d km da estrada, sua distância a A é √(20² + (40 − d)²). Igualando a d: 400 + 1600 − 80d + d² = d², logo d = 25 km. Alternativa <strong>C</strong>.</p><p>O centro do quadrado (A) fica a 20 km da estrada, mas a cerca de 28 km de A.</p>",
  p("Quatro estações distribuidoras de energia A, B, C e D estão dispostas como vértices de um quadrado de 40 km de lado. Deseja-se construir uma estação central que seja ao mesmo tempo equidistante das estações A e B e da estrada (reta) que liga as estações C e D.",
    "A nova estação deve ser localizada"),
  tags=["mediatriz", "distância"])

X(35, "N", "Biologia", "Paleontologia", "<p>Pelo esquema, xifosuras, trilobitas e braquiópodos viveram por vários períodos, e os ostracodermos existiram do Cambriano ao Devoniano. Só os placodermos existiram apenas no Devoniano: sua presença no mesmo estrato é o que define a idade da nova espécie. Alternativa <strong>E</strong>.</p><p>Os ostracodermos (D) também aparecem em períodos anteriores, por isso não bastam para fixar o Devoniano.</p>",
  p("Uma expedição de paleontólogos descobre em um determinado extrato geológico marinho uma nova espécie de animal fossilizado. No mesmo extrato, foram encontrados artrópodes xifosuras e trilobitas, braquiópodos e peixes ostracodermos e placodermos.")
  + "[[fig:1]]"
  + p("O esquema acima representa os períodos geológicos em que esses grupos viveram. Observando esse esquema os paleontólogos concluíram que o período geológico em que haviam encontrado essa nova espécie era o Devoniano, tendo ela uma idade estimada entre 405 milhões e 345 milhões de anos.",
      "Destes cinco grupos de animais que estavam associados à nova espécie, aquele que foi determinante para a definição do período geológico em que ela foi encontrada é"),
  figs(("q35", "Esquema dos períodos geológicos, do Cambriano (embaixo) ao Quaternário (em cima), agrupados nas eras Paleozoica, Mesozoica e Cenozoica, com barras verticais mostrando quando viveu cada grupo: xifosura, do Ordoviciano ao Quaternário; trilobita, do Cambriano ao Triássico; braquiópodo, do Cambriano ao Quaternário; ostracodermo, do Cambriano ao Devoniano; placodermo, só no Devoniano, entre duas linhas tracejadas que marcam esse período.")),
  ["fósseis-guia", "Devoniano"])

X(36, "N", "Biologia", "Ecologia", "<p>Um bom biodetector precisa reagir rápido. A espécie I morre em poucas horas com os dois tipos de poluente, dando o alarme logo após a contaminação. Alternativa <strong>A</strong>.</p><p>A espécie II resiste algumas horas antes de morrer, e a III quase não é afetada; espécies resistentes demoram a indicar o problema, o contrário do que se quer (B, C, E).</p>",
  p("Quando um reservatório de água é agredido ambientalmente por poluição de origem doméstica ou industrial, uma rápida providência é fundamental para diminuir os danos ecológicos. Como o monitoramento constante dessas águas demanda aparelhos caros e testes demorados, cientistas têm se utilizado de biodetectores, como peixes que são colocados em gaiolas dentro da água, podendo ser observados periodicamente.",
    "Para testar a resistência de três espécies de peixes, cientistas separaram dois grupos de cada espécie, cada um com cem peixes, totalizando seis grupos. Foi, então, adicionada a mesma quantidade de poluentes de origem doméstica e industrial, em separado. Durante o período de 24 horas, o número de indivíduos passou a ser contado de hora em hora. Os resultados são apresentados abaixo.")
  + "[[fig:1]]" + p("Pelos resultados obtidos, a espécie de peixe mais indicada para ser utilizada como detectora de poluição, a fim de que sejam tomadas providências imediatas, seria"),
  figs(("q36", "Três gráficos do número de peixes (0 a 100) ao longo de 24 horas, com uma curva para poluentes domésticos e outra para industriais. Espécie I: o número cai de 100 a quase zero logo nas primeiras horas, com os dois poluentes. Espécie II: fica em 100 por algumas horas e depois despenca, com os dois. Espécie III: cai pouco ao longo do dia, com os dois.")),
  ["bioindicadores", "poluição"])

X(37, "N", "Biologia", "Biotecnologia", "<p>O texto diz que os riscos ambientais são pequenos porque a soja transgênica “não tem possibilidade de cruzamento com outras plantas” e só 1% de chance de polinização cruzada com outra soja: ela não passa o gene a espécies selvagens. Alternativa <strong>C</strong>.</p><p>As doses de herbicida (B) e os testes de segurança (D, E) dizem respeito à estabilidade e à segurança do produto, e não ao risco ambiental; e o texto afirma que a resistência é estável (A).</p>",
  p("A Embrapa possui uma linhagem de soja transgênica resistente ao herbicida IMAZAPIR. A planta está passando por testes de segurança nutricional e ambiental, processo que exige cerca de três anos. Uma linhagem de soja transgênica requer a produção inicial de 200 plantas resistentes ao herbicida e destas são selecionadas as dez mais “estáveis”, com maior capacidade de gerar descendentes também resistentes. Esses descendentes são submetidos a doses de herbicida três vezes superiores às aplicadas nas lavouras convencionais. Em seguida, as cinco melhores são separadas e apenas uma delas é levada a testes de segurança. Os riscos ambientais da soja transgênica são pequenos, já que ela não tem possibilidade de cruzamento com outras plantas e o perigo de polinização cruzada com outro tipo de soja é de apenas 1%.",
    "A soja transgênica, segundo o texto, apresenta baixo risco ambiental porque"),
  tags=["transgênicos", "soja"])

X(38, "M", "Matemática", "Probabilidade", "<p>Pelo gráfico, 8 ex-alunas não têm filhos, 7 têm 1 filho, 6 têm 2 e 2 têm 3 (total de 23). Os filhos são 7 × 1 + 6 × 2 + 2 × 3 = 25, dos quais 7 são filhos únicos. A probabilidade é 7/25. Alternativa <strong>E</strong>.</p><p>A alternativa D (7/23) divide pelo número de mães, mas o sorteio é entre os filhos.</p>",
  p("As 23 ex-alunas de uma turma que completou o Ensino Médio há 10 anos se encontraram em uma reunião comemorativa. Várias delas haviam se casado e tido filhos. A distribuição das mulheres, de acordo com a quantidade de filhos, é mostrada no gráfico abaixo.")
  + "[[fig:1]]" + p("Um prêmio foi sorteado entre todos os filhos dessas ex-alunas. A probabilidade de que a criança premiada tenha sido um(a) filho(a) único(a) é"),
  figs(("q38", "Gráfico de barras do número de mulheres por quantidade de filhos: sem filhos, 8; 1 filho, 7; 2 filhos, 6; 3 filhos, 2.")),
  ["gráfico de barras"], alts=A5(r"\(\frac{1}{3}\)", r"\(\frac{1}{4}\)", r"\(\frac{7}{15}\)", r"\(\frac{7}{23}\)", r"\(\frac{7}{25}\)"))

X(39, "H", "Geografia", "Climatologia", "<p>Perto do Equador, a temperatura média é alta (24 °C a 28 °C, pela tabela). O ar quente consegue reter mais vapor de água; ao subir e esfriar, esse vapor condensa e cai como chuva abundante. Alternativa <strong>C</strong>.</p><p>O ar frio retém menos vapor, e não mais (D); A, B e E não explicam o mecanismo pelo qual a temperatura afeta a precipitação.</p>",
  p("A água é um dos fatores determinantes para todos os seres vivos, mas a precipitação varia muito nos continentes, como podemos observar no mapa abaixo.") + "[[fig:1]]"
  + tabela(["Latitude (°) / hemisfério", "Temperatura média (°C)"], [["60 / Norte", "0"], ["30 / Norte", "10"], ["10 / Norte", "24"], ["10 / Sul", "28"], ["30 / Sul", "14"], ["60 / Sul", "9"]])
  + fonte("Robert E. Ricklefs. <em>A Economia da Natureza</em>, 3. ed. Rio de Janeiro: Guanabara Koogan, 1996. p. 55.")
  + p("Ao examinar a tabela da temperatura média anual em algumas latitudes, podemos concluir que as chuvas são mais abundantes nas maiores latitudes próximas do Equador, porque"),
  figs(("q39", "Mapa-múndi “Mapa de distribuição dos grandes desertos e das áreas úmidas”, com as latitudes 60° N, 30° N, 0°, 30° S e 60° S marcadas. As áreas úmidas (mais de 1.500 mm de chuva por ano), em preto, concentram-se na faixa equatorial: Amazônia, África central e Sudeste Asiático. Os desertos (menos de 250 mm), em cinza, ficam perto de 30° N e 30° S, como o Saara, a Arábia e a Austrália.")),
  ["chuvas", "latitude"])

X(40, "H", "Geografia", "Fontes de energia", "<p>As duas afirmativas estão corretas: o petróleo está concentrado (64% no Oriente Médio), enquanto o gás natural se divide principalmente entre a ex-União Soviética (38,7%) e o Oriente Médio (33%), além de outras regiões; e o gráfico mostra que o gás natural é o que menos emite CO2, um dos principais gases do efeito estufa. Alternativa <strong>C</strong>.</p><p>O CO2 tem grande importância no efeito estufa (B), e o Brasil também contribui para o problema (D).</p>",
  p("Nos últimos meses o preço do petróleo tem alcançado recordes históricos. Por isso a procura de fontes energéticas alternativas se faz necessária. Para os especialistas, uma das mais interessantes é o gás natural, pois ele apresentaria uma série de vantagens em relação a outras opções energéticas.",
    "A tabela compara a distribuição das reservas de petróleo e de gás natural no mundo, e a figura, a emissão de monóxido de carbono entre vários tipos de fontes energéticas.")
  + tabela(["Região", "Distribuição de petróleo no mundo (%)", "Distribuição de gás natural no mundo (%)"],
           [["América do Norte", "3,5", "5,0"], ["América Latina", "13,0", "6,0"], ["Europa", "2,0", "3,6"], ["Ex-União Soviética", "6,3", "38,7"],
            ["Oriente Médio", "64,0", "33,0"], ["África", "7,2", "7,7"], ["Ásia/Oceania", "4,0", "6,0"]])
  + tit("Emissão de dióxido de carbono (CO2)") + "[[fig:1]]" + fonte("Fonte: Gas World International – Petroleum Economist.")
  + p("A partir da análise da tabela e da figura, são feitas as seguintes afirmativas:")
  + I3("<em>Enquanto as reservas mundiais de petróleo estão concentradas geograficamente, as reservas mundiais de gás natural são mais distribuídas ao redor do mundo garantindo um mercado competitivo, menos dependente de crises internacionais e políticas.</em>",
       "<em>A emissão de dióxido de carbono (CO2) para o gás natural é a mais baixa entre os diversos combustíveis analisados, o que é importante, uma vez que esse gás é um dos principais responsáveis pelo agravamento do efeito estufa.</em>")
  + p("Com relação a essas afirmativas pode-se dizer que"),
  figs(("q40", "Gráfico de barras da emissão de dióxido de carbono, em escala de 0 a 160: carvão de baixo teor de enxofre, cerca de 145; carvão de alto teor de enxofre, cerca de 120; óleo residual, cerca de 78; óleos destilados, cerca de 75; gás natural, cerca de 56.")),
  ["gás natural", "efeito estufa"], quim=True)

X(41, "N", "Biologia", "Ácidos nucleicos", "<p>O DNA de todos os seres vivos é feito dos mesmos componentes: desoxirribose, fosfato e as bases A, T, C e G. Quimicamente, o DNA vegetal não tem nada de especial, e qualquer DNA serviria. Alternativa <strong>A</strong>.</p><p>Clorofila não faz parte do DNA (B), DNA aplicado ao cabelo não causa mutação no couro cabeludo (C), e o caráter ácido, e não básico, é o que dá nome à molécula (E).</p>",
  p("Um fabricante afirma que um produto disponível comercialmente possui DNA vegetal, elemento que proporcionaria melhor hidratação dos cabelos.") + "[[fig:1]]"
  + p("Sobre as características químicas dessa molécula essencial à vida, é correto afirmar que o DNA"),
  figs(("q41", "Pote de creme com a marca fictícia “Wxyz”, o desenho de uma dupla hélice e os dizeres “Com DNA vegetal, 450 g”.")),
  ["DNA", "propaganda"])

X(42, "M", "Matemática", "Proporção", "<p>No padrão, cada fileira tem 1 pastilha preta a cada 5, ou seja, 1/5 = 20% da área é preta e 80% é branca. O custo por metro quadrado é 0,8 × 8 + 0,2 × 10 = 6,40 + 2,00 = R$ 8,40. Alternativa <strong>B</strong>.</p><p>Outra conta: o revestimento custa R$ 8 por m², mais R$ 2 a mais em cada 20% de área preta, isto é, 8 + 0,4.</p>",
  p("Um pátio de grandes dimensões vai ser revestido por pastilhas quadradas brancas e pretas, segundo o padrão representado abaixo, que vai ser repetido em toda a extensão do pátio.") + "[[fig:1]]"
  + p("As pastilhas de cor branca custam R$ 8,00 por metro quadrado e as de cor preta, R$ 10,00. O custo por metro quadrado do revestimento será de"),
  figs(("q42", "Malha quadriculada de pastilhas brancas com pastilhas pretas espalhadas em padrão regular: em cada fileira, uma pastilha preta a cada cinco, deslocada de uma fileira para a outra.")),
  ["média ponderada"], alts=A5("R$ 8,20.", "R$ 8,40.", "R$ 8,60.", "R$ 8,80.", "R$ 9,00."))

X(43, "N", "Biologia", "Zoologia", "<p>Se cada fase larval tem forma, alimentação e habitat diferentes, larvas e adultos da mesma espécie não disputam os mesmos recursos. A metamorfose diminui a competição intraespecífica. Alternativa <strong>C</strong>.</p><p>Ocupar fases diferentes aumenta, e não diminui, o número de nichos ocupados pela espécie (D), e não aumenta a predação entre os indivíduos (A).</p>",
  p("A atividade pesqueira é antes de tudo extrativista, o que causa impactos ambientais. Muitas espécies já apresentam sério comprometimento em seus estoques e, para diminuir esse impacto, várias espécies vêm sendo cultivadas. No Brasil, o cultivo de algas, mexilhões, ostras, peixes e camarões, vem sendo realizado há alguns anos, com grande sucesso, graças ao estudo minucioso da biologia dessas espécies.",
    "Os crustáceos decápodes, por exemplo, apresentam durante seu desenvolvimento larvário, várias etapas com mudança radical de sua forma.")
  + "[[fig:1]]" + fonte("Algumas das fases larvárias de crustáceos")
  + p("Não só a sua forma muda, mas também a sua alimentação e habitat. Isso faz com que os criadores estejam atentos a essas mudanças, porque a alimentação ministrada tem de mudar a cada fase.",
      "Se para o criador, essas mudanças são um problema para a espécie em questão, essa metamorfose apresenta uma vantagem importante para sua sobrevivência, pois"),
  figs(("q43", "Desenhos de quatro fases larvais de crustáceos, de formas muito diferentes entre si: uma larva pequena com longos apêndices, uma com espinhos, uma achatada com muitas patas e, por fim, uma já parecida com um camarão.")),
  ["metamorfose", "competição"])

X(44, "L", "Artes", "Surrealismo", "<p>Transgênicos misturam características de espécies diferentes. A obra B mostra um ser híbrido, com a parte de cima de peixe e a de baixo de mulher, que traduz essa ideia. Alternativa <strong>B</strong>.</p><p>As outras obras exploram outros enigmas de Magritte: figuras de chapéu-coco recortadas, um navio feito de mar, a pintura que “não é um cachimbo” e o pintor que pinta um pássaro olhando um ovo.</p>",
  p("Os transgênicos vêm ocupando parte da imprensa com opiniões ora favoráveis ora desfavoráveis. Um organismo ao receber material genético de outra espécie, ou modificado da mesma espécie, passa a apresentar novas características. Assim, por exemplo, já temos bactérias fabricando hormônios humanos, algodão colorido e cabras que produzem fatores de coagulação sangüínea humana.",
    "O belga René Magritte (1896 – 1967), um dos pintores surrealistas mais importantes, deixou obras enigmáticas. Caso você fosse escolher uma ilustração para um artigo sobre os transgênicos, qual das obras de Magritte, abaixo, estaria mais de acordo com esse tema tão polêmico?"),
  figs(("q44a", "Pintura de Magritte: duas figuras de costas, de sobretudo e chapéu-coco, a da direita com o corpo recortado mostrando céu e nuvens."),
       ("q44b", "Pintura de Magritte: na beira do mar, um ser deitado na areia com a cabeça e o tronco de peixe e as pernas de mulher."),
       ("q44c", "Pintura de Magritte: um veleiro em mar agitado, com o casco e as velas feitos da mesma textura das ondas."),
       ("q44d", "Pintura de Magritte: um cachimbo, com a frase em francês “Ceci n’est pas une pipe” (Isto não é um cachimbo)."),
       ("q44e", "Pintura de Magritte: um pintor diante do cavalete olha um ovo sobre a mesa e pinta na tela um pássaro de asas abertas.")),
  ["René Magritte", "transgênicos"], alts=ALT(1))

X(45, "N", "Biologia", "Botânica", "<p>As angiospermas são as plantas com flores e frutos, e muitas dependem de insetos para a polinização, como as árvores frutíferas. Sem insetos, sua reprodução cairia drasticamente. Alternativa <strong>E</strong>.</p><p>Algas, briófitas e pteridófitas não têm flores nem polinização, e as gimnospermas, como os pinheiros, são polinizadas pelo vento.</p>",
  p("Caso os cientistas descobrissem alguma substância que impedisse a reprodução de todos os insetos, certamente nos livraríamos de várias doenças em que esses animais são vetores. Em compensação teríamos grandes problemas como a diminuição drástica de plantas que dependem dos insetos para polinização, que é o caso das"),
  tags=["polinização", "angiospermas"])

X(46, "M", "Matemática", "Análise combinatória", "<p>Cada um dos 6 pontos pode estar em destaque ou não: são 2<sup>6</sup> = 64 combinações. Tirando a única em que nenhum ponto se destaca, restam 64 − 1 = 63 caracteres. Alternativa <strong>D</strong>.</p><p>720 (E) seria 6!, o número de ordenações dos pontos, o que não é o caso.</p>",
  p("A escrita Braile para cegos é um sistema de símbolos no qual cada caráter é um conjunto de 6 pontos dispostos em forma retangular, dos quais pelo menos um se destaca em relação aos demais.", "Por exemplo, a letra A é representada por") + "[[fig:1]]"
  + p("O número total de caracteres que podem ser representados no sistema Braile é"),
  figs(("q46", "Cela braile com 6 pontos em 3 linhas e 2 colunas, na qual só o ponto superior esquerdo é maior, em destaque.")),
  ["princípio multiplicativo", "braile"], alts=A5("12.", "31.", "36.", "63.", "720."))

X(47, "N", "Biologia", "Ecologia", "<p>Os anfíbios terrestres se reproduzem quando há água em abundância. No gráfico, as chuvas mais intensas vão de novembro a fevereiro (cerca de 240 mm em novembro, 310 em dezembro, 300 em janeiro e 200 em fevereiro). Alternativa <strong>B</strong>.</p><p>De maio a setembro chove quase nada, e março e abril já mostram queda das chuvas.</p>",
  p("Em uma área observa-se o seguinte regime pluviométrico:") + "[[fig:1]]"
  + p("Os anfíbios são seres que podem ocupar tanto ambientes aquáticos quanto terrestres. Entretanto, há espécies de anfíbios que passam todo o tempo na terra ou então na água. Apesar disso, a maioria das espécies terrestres depende de água para se reproduzir e o faz quando essa existe em abundância. Os meses do ano em que, nessa área, esses anfíbios terrestres poderiam se reproduzir mais eficientemente são de"),
  figs(("q47", "Gráfico de barras da precipitação mensal (mm) de janeiro a dezembro: jan, cerca de 300; fev, 200; mar, 150; abr, 100; mai, 40; jun a set, entre 15 e 30; out, 130; nov, 240; dez, 310.")),
  ["anfíbios", "regime de chuvas"])

X(48, "H", "Geografia", "Problemas ambientais urbanos", "<p>A maior queixa em X são os dejetos tóxicos (34%), o que pede controle de despejo industrial; em Y, o lixo (40%), que pede manejamento de lixo; em Z, o esgoto aberto (36%), que pede esgotamento sanitário. Alternativa <strong>E</strong>.</p><p>A poluição do ar só aparece com peso em Z (23%), e nem lá é a principal queixa, por isso não cabe começar pelo controle de emissão de gases.</p>",
  p("Moradores de três cidades, aqui chamadas de X, Y e Z, foram indagados quanto aos tipos de poluição que mais afligiam as suas áreas urbanas. Nos gráficos abaixo estão representadas as porcentagens de reclamações sobre cada tipo de poluição ambiental.")
  + "[[fig:1]]" + p("Considerando a queixa principal dos cidadãos de cada cidade, a primeira medida de combate à poluição em cada uma delas seria, respectivamente:"),
  figs(("q48", "Três gráficos de setores. Cidade X: dejetos tóxicos 34%, poluição sonora 30%, lixo 24%, esgoto aberto 12%, poluição do ar 0%. Cidade Y: lixo 40%, dejetos tóxicos 23%, poluição sonora 22%, poluição do ar 13%, esgoto aberto 2%. Cidade Z: esgoto aberto 36%, poluição do ar 23%, lixo 22%, dejetos tóxicos 12%, poluição sonora 7%.")),
  ["poluição", "gráfico de setores"],
  alts={k: f"X: {x}; Y: {y}; Z: {z}." for k, (x, y, z) in {
      "A": ("manejamento de lixo", "esgotamento sanitário", "controle emissão de gases"),
      "B": ("controle de despejo industrial", "manejamento de lixo", "controle emissão de gases"),
      "C": ("manejamento de lixo", "esgotamento sanitário", "controle de despejo industrial"),
      "D": ("controle emissão de gases", "controle de despejo industrial", "esgotamento sanitário"),
      "E": ("controle de despejo industrial", "manejamento de lixo", "esgotamento sanitário")}.items()})

X(49, "N", "Biologia", "Controle biológico", "<p>A única curva que chega a 50% de sobrevivência cai de cerca de 70% no dia 8 para 40% no dia 10, cruzando os 50% entre esses dias (perto do dia 9). Alternativa <strong>D</strong>.</p><p>Atenção: na legenda do gráfico original, essa curva que despenca aparece como a dos mosquitos “não expostos”, e a que fica perto de 90% como a dos “expostos”. Pelo sentido do experimento (fungos que matam mosquitos) e pelo gabarito, a curva que cai é a do grupo exposto; a legenda parece trocada.</p>",
  "[[fig:1]]" + p("Foram publicados recentemente trabalhos relatando o uso de fungos como controle biológico de mosquitos transmissores da malária. Observou-se o percentual de sobrevivência dos mosquitos <em>Anopheles</em> sp. após exposição ou não a superfícies cobertas com fungos sabidamente pesticidas, ao longo de duas semanas. Os dados obtidos estão presentes no gráfico acima. No grupo exposto aos fungos, o período em que houve 50% de sobrevivência ocorreu entre os dias"),
  figs(("q49", "Gráfico da porcentagem de sobrevivência dos mosquitos em função dos dias após a exposição (0 a 14). A curva tracejada com círculos, rotulada na legenda como “mosquitos expostos”, fica entre 90% e 100% o tempo todo. A curva contínua com quadrados, rotulada como “mosquitos não expostos”, fica perto de 90% até o dia 6 e depois cai: 80% no dia 7, 70% no dia 8, 55% no dia 9, 40% no dia 10, 25% no dia 11, 20% no dia 12 e 5% no dia 14.")),
  ["fungos", "malária"], alts=A5("2 e 4.", "4 e 6.", "6 e 8.", "8 e 10.", "10 e 12."))

X(50, "N", "Biologia", "Evolução", "<p>Na árvore, o ramo dos macacos do Velho Mundo se separa do ramo dos grandes macacos e humanos num ponto bem à direita da extinção dos dinossauros (cerca de 65 milhões de anos), a pouco mais de duas divisões depois da marca de 60 milhões, cada uma de 10 milhões de anos: cerca de 40 milhões de anos. Alternativa <strong>B</strong>.</p><p>85 milhões de anos (E) é a idade do ancestral comum mais antigo, e 65 milhões (D), a extinção dos dinossauros.</p>",
  "[[fig:1]]" + fonte("Fonte: Raquel Aguiar, <em>Ciência Hoje on-line</em> 13/05/02.")
  + p("Foi proposto um novo modelo de evolução dos primatas elaborado por matemáticos e biólogos. Nesse modelo o grupo de primatas pode ter tido origem quando os dinossauros ainda habitavam a Terra, e não há 65 milhões de anos, como é comumente aceito.",
      "Examinando esta árvore evolutiva podemos dizer que a divergência entre os macacos do Velho Mundo e o grupo dos grandes macacos e de humanos ocorreu há aproximadamente"),
  figs(("q50", "Árvore evolutiva dos primatas sobre uma escala de tempo em milhões de anos (90, 80, 70, 60 e mais marcas a cada 10 milhões até o presente), do Cretáceo superior e Paleoceno aos primatas atuais. O ancestral comum mais antigo fica perto de 85 milhões de anos, antes da linha da extinção dos dinossauros (cerca de 65). Dele saem os ramos de lêmures e lóris, de társios e macacos do Novo Mundo, e um ramo que se divide em macacos do Velho Mundo e grandes macacos e humanos por volta de 40 milhões de anos.")),
  ["primatas", "árvore filogenética"], alts=A5("10 milhões de anos.", "40 milhões de anos.", "55 milhões de anos.", "65 milhões de anos.", "85 milhões de anos."))

X(51, "H", "Geografia", "Saúde e desenvolvimento", "<p>I e II estão corretas: as doenças negligenciadas (malária, doença de Chagas, leishmaniose, tuberculose) são ligadas à pobreza, à subnutrição e à falta de saneamento, e atraem pouco a indústria farmacêutica, porque os doentes estão em países pobres e o retorno econômico é baixo. Alternativa <strong>D</strong>.</p><p>III é falsa: essas doenças são endêmicas no Brasil e atingem milhões de pessoas.</p>",
  p("Entre 1975 e 1999, apenas 15 novos produtos foram desenvolvidos para o tratamento da tuberculose e de doenças tropicais, as chamadas doenças negligenciadas. No mesmo período, 179 novas drogas surgiram para atender portadores de doenças cardiovasculares. Desde 2003, um grande programa articula esforços em pesquisa e desenvolvimento tecnológico de instituições científicas, governamentais e privadas de vários países para reverter esse quadro de modo duradouro e profissional.",
    "Sobre as doenças negligenciadas e o programa internacional, considere as seguintes afirmativas:")
  + I3("As doenças negligenciadas, típicas das regiões subdesenvolvidas do planeta, são geralmente associadas à subnutrição e à falta de saneamento básico.",
       "As pesquisas sobre as doenças negligenciadas não interessam à indústria farmacêutica porque atingem países em desenvolvimento sendo economicamente pouco atrativas.",
       "O programa de combate às doenças negligenciadas endêmicas não interessa ao Brasil porque atende a uma parcela muito pequena da população.")
  + p("Está correto apenas o que se afirma em:"),
  tags=["doenças negligenciadas"])

X(52, "H", "Geografia", "Biomas brasileiros", "<p>Pelo gráfico, a área de vegetação natural foi de 33,3 mil km² em 1990-1992 para 34,6 mil km² em 2000-2001: a área de 2000-2001 é maior. Alternativa <strong>E</strong>.</p><p>De 1962-1963 para 1971-1973 a queda foi de 72,6 para 43,9 mil km², cerca de 40%, e não 50% (A); a devastação continuou depois dos anos 60 (C); e 34,6 é a área em mil km², e não uma porcentagem (D).</p>",
  p("Em um estudo feito pelo Instituto Florestal, foi possível acompanhar a evolução de ecossistemas paulistas desde 1962. Desse estudo publicou-se o Inventário Florestal de São Paulo, que mostrou resultados de décadas de transformações da Mata Atlântica.")
  + "[[fig:1]]" + fonte("Fonte: <em>Pesquisa</em>. 91, São Paulo: FAPESP, set/2003, p. 48.")
  + p("Examinando o gráfico da área de vegetação natural remanescente (em mil km<sup>2</sup>) pode-se inferir que"),
  figs(("q52", "Gráfico de barras “Área de vegetação natural (em mil km²)”: 1962-1963, 72,6; 1971-1973, 43,9; 1990-1992, 33,3; 2000-2001, 34,6.")),
  ["Mata Atlântica"], alts=dict(D[52], E="a área preservada da Mata Atlântica nos anos 2000 e 2001 é maior do que a registrada no período de 1990-1992."))

X(53, "H", "Geografia", "Recursos hídricos", "<p>Os dois pontos de vista concordam que a obra pode beneficiar o Nordeste, mas os dois dizem que ela não basta: o primeiro exige melhor gestão das águas, e o segundo, escoamento da produção e educação das pessoas. O projeto deve ir além do aumento de recursos hídricos. Alternativa <strong>D</strong>.</p><p>Nenhum dos textos prevê fracasso certo (E) nem defende evitar a gestão participativa (C).</p>",
  ap("Segundo a análise do Prof. Paulo Canedo de Magalhães, do Laboratório de Hidrologia da COPPE, UFRJ, o projeto de transposição das águas do Rio São Francisco envolve uma vazão de água modesta e não representa nenhum perigo para o Velho Chico, mas pode beneficiar milhões de pessoas. No entanto, o sucesso do empreendimento dependerá do aprimoramento da capacidade de gestão das águas nas regiões doadora e receptora, bem como no exercício cotidiano de operar e manter o sistema transportador.",
     "Embora não seja contestado que o reforço hídrico poderá beneficiar o interior do Nordeste, um grupo de cientistas e técnicos, a convite da SBPC, numa análise isenta, aponta algumas incertezas no projeto de transposição das águas do Rio São Francisco. Afirma também que a água por si só não gera desenvolvimento e será preciso implantar sistemas de escoamento de produção, capacitar e educar pessoas, entre outras ações.")
  + fonte("Adaptado. <em>Ciência Hoje</em>, volume 37, número 217, julho de 2005.")
  + p("Os diferentes pontos de vista sobre o megaprojeto de transposição das águas do Rio São Francisco quando confrontados indicam que"),
  tags=["transposição do São Francisco", "semiárido"])

X(54, "N", "Biologia", "Evolução", "<p>O gráfico mostra o pico de O2 (perto de 30%) por volta de 300 milhões de anos, no Carbonífero, quando surgiram os animais gigantes. Com mais oxigênio no ar, organismos grandes, como insetos que respiram por traqueias, conseguiam absorver O2 suficiente. Alternativa <strong>C</strong>.</p><p>A queda do oxigênio no Permiano coincide com a grande extinção, e não com aumento da biodiversidade (E); o texto não fala de nitrogênio (A) nem de mutações causadas por CO2 (D).</p>",
  p("Pesquisas recentes estimam o seguinte perfil da concentração de oxigênio (O2) atmosférico ao longo da história evolutiva da Terra:") + "[[fig:1]]"
  + p("No período Carbonífero entre aproximadamente 350 e 300 milhões de anos, houve uma ampla ocorrência de animais gigantes, como por exemplo insetos voadores de 45 centímetros e anfíbios de até 2 metros de comprimento. No entanto, grande parte da vida na Terra foi extinta há cerca de 250 milhões de anos, durante o período Permiano. Sabendo-se que o O2 é um gás extremamente importante para os processos de obtenção de energia em sistemas biológicos, conclui-se que"),
  figs(("q54", "Gráfico da concentração de O2 (%) em função do tempo, de 600 milhões de anos atrás até hoje. A curva fica entre 12% e 15% até cerca de 450 milhões de anos, sobe a um pico perto de 30% por volta de 300 milhões de anos, cai para cerca de 12% perto de 250 milhões de anos e depois oscila entre 15% e 23% até hoje.")),
  ["oxigênio atmosférico", "Carbonífero"], quim=True)

X(55, "M", "Matemática", "Aritmética", "<p>Para 24685, do último ao primeiro algarismo: 5 × 1 = 5; 8 × 2 = 16, que vira 17; 6 × 1 = 6; 4 × 2 = 8; 2 × 1 = 2. A soma é 5 + 17 + 6 + 8 + 2 = 38, e o resto da divisão por 10 é 8. Alternativa <strong>E</strong>.</p><p>Quem esquece de somar 1 ao 16 chega a 37 e marca 7, que não está entre as opções; quem começa a alternância pelo primeiro algarismo obtém outro valor.</p>",
  p("Os números de identificação utilizados no cotidiano (de contas bancárias, de CPF, de Carteira de Identidade etc) usualmente possuem um dígito de verificação, normalmente representado após o hífen, como em 17326-9. Esse dígito adicional tem a finalidade de evitar erros no preenchimento ou digitação de documentos. Um dos métodos usados para gerar esse dígito utiliza os seguintes passos:")
  + "<ul><li>multiplica-se o último algarismo do número por 1, o penúltimo por 2, o antepenúltimo por 1, e assim por diante, sempre alternando multiplicações por 1 e por 2.</li><li>soma-se 1 a cada um dos resultados dessas multiplicações que for maior do que ou igual a 10.</li><li>somam-se os resultados obtidos.</li><li>calcula-se o resto da divisão dessa soma por 10, obtendo-se assim o dígito verificador.</li></ul>"
  + p("O dígito de verificação fornecido pelo processo acima para o número 24685 é"),
  tags=["dígito verificador"], alts=A5("1.", "2.", "4.", "6.", "8."))

X(56, "L", "Literatura", "Intertextualidade", "<p>Na tirinha, Mafalda vê a notícia de “nova tentativa de desarmamento” virar um avião de papel que cai e se espatifa: a paz parece impossível. Na canção, o eu lírico insiste em sonhar o “sonho impossível” e acredita que “o mundo vai ver uma flor brotar do impossível chão”. Uma visão é pessimista, a outra é esperançosa. Alternativa <strong>D</strong>.</p><p>Por isso os dois textos não concordam (B) nem transmitem, juntos, uma mensagem otimista (E).</p>",
  p("Leia estes textos.") + tit("Texto 1") + "[[fig:1]]" + fonte("QUINO. <em>O mundo da Mafalda</em>. São Paulo: Martins Fontes, 1999. p. 3.")
  + tit("Texto 2 — Sonho Impossível") + "[[fig:2]]" + fonte("J. Darione – M. Leigh – Versão de Chico Buarque de Hollanda e Ruy Guerra, 1972.")
  + p("A tirinha e a canção apresentam uma reflexão sobre o futuro da humanidade. É correto concluir que os dois textos"),
  figs(("q56a", "Tira de Mafalda, de Quino, em cinco quadros, sem falas até o fim. Mafalda lê no jornal a manchete “Nova tentativa de desarmamento”, recorta a notícia, dobra-a em forma de avião de papel e o lança; o avião rodopia e se espatifa no chão (“ploc”). No último quadro, Mafalda pensa: “Depois eu é que sou a pessimista!”."),
       ("q56b", "Letra da canção “Sonho impossível”, em versão de Chico Buarque e Ruy Guerra: o eu lírico se propõe a sonhar o sonho impossível, lutar quando é fácil ceder, vencer o inimigo invencível e tocar o chão inacessível, sem se importar com o tamanho das guerras; acredita que valerá a pena e que o mundo verá uma flor brotar do chão impossível.")),
  ["Mafalda", "Chico Buarque"])

X(57, "N", "Biologia", "Fisiologia animal", "<p>O hormônio juvenil impede que o inseto perca as características de larva. Se a larva o ingere continuamente ao comer a planta, nunca chega à fase adulta e, portanto, não se reproduz: a planta reduz a população de insetos que a atacam. Alternativa <strong>A</strong>.</p><p>O hormônio não acelera a chegada à fase adulta (D) e não impede as mudas, que dependem da ecdisona (E).</p>",
  p("O desenvolvimento da maior parte das espécies de insetos passa por vários estágios até chegar à fase adulta, quando finalmente estão aptos à reprodução. Esse desenvolvimento é um jogo complexo de hormônios. A ecdisona promove as mudas (ecdíases), mas o hormônio juvenil impede que o inseto perca suas características de larva. Com o tempo, a quantidade desse hormônio diminui e o inseto chega à fase adulta.")
  + "[[fig:1]]"
  + p("Cientistas descobriram que algumas árvores produzem um composto químico muito semelhante ao hormônio juvenil dos insetos. A vantagem de uma árvore que produz uma substância que funcione como hormônio juvenil é que a larva do inseto, ao se alimentar da planta, ingere esse hormônio e"),
  figs(("q57", "Esquema do desenvolvimento de um besouro: ovo, larvas de tamanhos crescentes, pupa e adulto, ligados por setas de “muda”. A ecdisona atua em todas as mudas; o hormônio juvenil também, mas com setas cada vez mais finas, indicando que sua quantidade diminui até a fase adulta.")),
  ["hormônio juvenil", "metamorfose"])

POEMAS = (p("Leia estes poemas.") + "[[fig:1]]"
  + fonte("Texto 1: Manuel Bandeira. <em>Poesia completa e prosa</em>. Rio de Janeiro: Aguilar, 1983. p. 395. Texto 2: Carlos Drummond de Andrade. <em>Obra completa</em>. Rio de Janeiro: Aguilar, 1964. p. 53."))
F_POEMAS = figs(("q58", "Dois poemas lado a lado. Texto 1, “Auto-retrato”, de Manuel Bandeira: o poeta se descreve com ironia como provinciano que não sabe escolher gravata, poeta ruim na prosa, arquiteto e músico falhados, sem família, religião ou filosofia, e “um tísico profissional” (tísico: tuberculoso). Texto 2, “Poema de sete faces”, de Drummond: um anjo torto diz ao poeta, quando ele nasce, que vá ser “gauche” na vida; o eu lírico pergunta a Deus por que o abandonou, se sabia que ele era fraco, e termina dizendo que, se se chamasse Raimundo, seria uma rima, não uma solução, e que mais vasto que o mundo é o seu coração."))
X(58, "L", "Literatura", "Modernismo", "<p>Os dois eus líricos se veem como fracassados ou deslocados: Bandeira se descreve como poeta ruim, arquiteto e músico falhados, sem família nem religião; Drummond nasce destinado a ser “gauche” e se sente fraco e abandonado. O tom dos dois é pessimista, ainda que com ironia. Alternativa <strong>B</strong>.</p><p>Nenhum descreve o físico (A) ou narra a vida desde o nascimento em detalhe (D), e a doença só aparece no poema de Bandeira (C).</p>",
  POEMAS + p("Esses poemas têm em comum o fato de"), F_POEMAS, ["Manuel Bandeira", "Drummond"])
X(59, "L", "Literatura", "Intertextualidade", "<p>Drummond retoma a frase de Cristo na cruz (“Meu Deus, por que me abandonaste?”) para expressar o abandono do próprio eu lírico. Repetir de propósito as palavras de outra pessoa, com finalidade expressiva, é um recurso estilístico de intertextualidade (citação). Alternativa <strong>D</strong>.</p><p>Não se trata de vício de linguagem (B) nem de repetição desnecessária (C).</p>",
  POEMAS + p("No verso “Meu Deus, por que me abandonaste” do texto 2, Drummond retoma as palavras de Cristo, na cruz, pouco antes de morrer. Esse recurso de repetir palavras de outrem equivale a"),
  F_POEMAS, ["intertextualidade", "Drummond"])

X(60, "M", "Matemática", "Estatística", "<p>Concluíram o Ensino Médio os que têm Médio completo (54) e os que já estão no Superior incompleto (14): 68 jogadores. Em 112, isso é 68/112 ≈ 0,607, ou seja, cerca de 60%. Alternativa <strong>D</strong>.</p><p>68% (E) confunde o número de jogadores com a porcentagem, e 48% (B) considera só os 54 do Médio completo (54/112).</p>",
  p("A escolaridade dos jogadores de futebol nos grandes centros é maior do que se imagina, como mostra a pesquisa abaixo, realizada com os jogadores profissionais dos quatro principais clubes de futebol do Rio de Janeiro.")
  + "[[fig:1]]" + fonte("<em>O Globo</em>, 24/7/2005.") + p("De acordo com esses dados, o percentual dos jogadores dos quatro clubes que concluíram o Ensino Médio é de aproximadamente:"),
  figs(("q60", "Gráfico de barras da escolaridade de 112 jogadores: Fundamental incompleto, 14; Fundamental, 16; Médio incompleto, 14; Médio, 54; Superior incompleto, 14.")),
  ["porcentagem", "gráfico de barras"], alts=A5("14%.", "48%.", "54%.", "60%.", "68%."))

X(61, "M", "Matemática", "Geometria espacial", "<p>Até a metade da altura, o cone com a ponta para baixo (V1) contém só a parte estreita: um cone semelhante de razão 1/2, com 1/8 do volume total. O recipiente 2, mais largo embaixo, tem a parte de baixo mais volumosa (V2 é o maior). No recipiente 3, de dois cones unidos pela ponta, a metade de baixo é um cone com a base embaixo, maior que V1 e menor que V2. Assim, V1 &lt; V3 &lt; V2. Alternativa <strong>B</strong>.</p>",
  p("Os três recipientes da figura têm formas diferentes, mas a mesma altura e o mesmo diâmetro da boca. Neles são colocados líquido até a metade de sua altura, conforme indicado nas figuras.") + "[[fig:1]]"
  + p("Representando por V<sub>1</sub>, V<sub>2</sub> e V<sub>3</sub> o volume de líquido em cada um dos recipientes, tem-se"),
  figs(("q61", "Três recipientes de mesma altura e mesma boca, cheios até a metade. V1: um cone com a ponta para baixo. V2: um recipiente arredondado, como uma tigela funda. V3: dois cones unidos pela ponta, como uma ampulheta, com o cone de baixo apoiado pela base.")),
  ["volume", "semelhança"],
  alts=A5(r"\(V_1 = V_2 = V_3\)", r"\(V_1 < V_3 < V_2\)", r"\(V_1 = V_3 < V_2\)", r"\(V_3 < V_1 < V_2\)", r"\(V_1 < V_2 = V_3\)"))

X(62, "N", "Física", "Radioatividade", "<p>O lixo atômico contém isótopos radioativos que continuam emitindo radiação por milhares de anos, e o decaimento não pode ser acelerado nem interrompido por nenhum processo químico ou físico conhecido. Por isso ele precisa ser isolado por muito tempo. Alternativa <strong>A</strong>.</p><p>O volume de rejeito é pequeno (B), ele não é orgânico (C) e não exala gases venenosos nem destrói a camada de ozônio (D, E).</p>",
  p("Um problema ainda não resolvido da geração nuclear de eletricidade é a destinação dos rejeitos radiativos, o chamado “lixo atômico”. Os rejeitos mais ativos ficam por um período em piscinas de aço inoxidável nas próprias usinas antes de ser, como os demais rejeitos, acondicionados em tambores que são dispostos em áreas cercadas ou encerrados em depósitos subterrâneos secos, como antigas minas de sal. A complexidade do problema do lixo atômico, comparativamente a outros lixos com substâncias tóxicas, se deve ao fato de"),
  tags=["lixo atômico", "meia-vida"])

X(63, "L", "Literatura", "Realismo", "<p>A ilustração mantém o essencial do texto (a chuva, o pequeno grupo de amigos, o discurso à beira da cova), mas acrescenta elementos que Machado não menciona: o guarda-chuva que abriga o grupo, a estátua de um anjinho, colunas caídas e uma coroa de flores no chão. Ela apresenta detalhes ausentes na cena verbal. Alternativa <strong>A</strong>.</p><p>Por acrescentar esses detalhes, não é uma reprodução fiel (B); mas também não contraria nem distorce a cena (C, E), e o clima sombrio é adequado ao enterro (D).</p>",
  p("Leia o texto e examine a ilustração:") + tit("Óbito do autor")
  + ap("(....) expirei às duas horas da tarde de uma sexta-feira do mês de agosto de 1869, na minha bela chácara de Catumbi. Tinha uns sessenta e quatro anos, rijos e prósperos, era solteiro, possuía cerca de trezentos contos e fui acompanhado ao cemitério por onze amigos. Onze amigos! Verdade é que não houve cartas nem anúncios. Acresce que chovia — peneirava — uma chuvinha miúda, triste e constante, tão constante e tão triste, que levou um daqueles fiéis da última hora a intercalar esta engenhosa idéia no discurso que proferiu à beira de minha cova: — “Vós, que o conhecestes, meus senhores, vós podeis dizer comigo que a natureza parece estar chorando a perda irreparável de um dos mais belos caracteres que tem honrado a humanidade. Este ar sombrio, estas gotas do céu, aquelas nuvens escuras que cobrem o azul como um crepe funéreo, tudo isto é a dor crua e má que lhe rói à natureza as mais íntimas entranhas; tudo isso é um sublime louvor ao nosso ilustre finado.” (....)")
  + "[[fig:1]]" + fonte("Adaptado. Machado de Assis. <em>Memórias póstumas de Brás Cubas</em>. Ilustrado por Cândido Portinari. Rio de Janeiro: Cem Bibliófilos do Brasil, 1943. p. 1.")
  + p("Compare o texto de Machado de Assis com a ilustração de Portinari. É correto afirmar que a ilustração do pintor"),
  figs(("q63", "Ilustração a traço de Portinari: num cemitério, sob chuva forte, um pequeno grupo de homens de casaca se abriga sob um guarda-chuva enquanto outro, de pé ao lado de um túmulo, discursa com a mão erguida; ao redor há túmulos, uma coroa de flores no chão, colunas caídas e a estátua de um anjinho.")),
  ["Machado de Assis", "Portinari"])

completar(Q, R)
