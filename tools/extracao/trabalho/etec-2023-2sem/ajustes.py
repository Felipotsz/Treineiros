# Ajustes da conferência humana: Vestibulinho ETEC 2º semestre de 2023 (exame de 04/06/2023)
# Texto conferido com a imagem de cada página. Gabarito: gabarito oficial (2SEM23). Tema: estado de São Paulo.
import re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import A, carregar, enun, tabela, colunas, completar

META = {
    "id": "etec-2023-2sem",
    "banca": "ETEC",
    "ano": 2023,
    "semestre": 2,
    "titulo": "Vestibulinho ETEC, 2º semestre de 2023",
    "fonte": "Centro Paula Souza",
    "dataExame": "2023-06-04",
    "duracaoMinutos": 240,
    "tema": "Estado de São Paulo",
    "pdf": "assets/provas/etec-2023-2sem.pdf",
}

R = carregar("etec-2023-2sem")
I = "interdisciplinar"
P1 = "<p>Os termos em destaque no texto podem ser substituídos, correta e respectivamente, por</p>"
P6 = "<p>De acordo com o texto, é correto afirmar que</p>"
P19 = ("<p>O linguado é um animal bentônico, que vive sob areia e cascalho no fundo do mar, ficando apenas com os olhos para fora. Por isso, ele consegue visualizar o chão ao seu redor e imitar os locais onde vive, mudando sua própria cor.</p>"
       "<p>Essa importante adaptação do linguado, que lhe permite tornar-se praticamente invisível, recebe o nome de</p>")
P21 = "<p>De acordo com os textos, é correto afirmar que</p>"
P29 = "<p>Tendo como base a linguagem verbal e não verbal, é correto afirmar que</p>"
P31 = "<p>O texto menciona a necessidade de uma obra de infraestrutura para atender à demanda da produção de café, que</p>"
P37 = "<p>Segundo o texto,</p>"

CAIPIRA = enun(R, 1, ["É nesse contexto que surge", "Para o professor, essa", "Mas, durante a era"],
               trocas=[("</p><p>Os termos", '</p><p class="fonte">&lt;https://tinyurl.com/5n8ajwn4&gt; Acesso em: 02.03.2023. Adaptado.</p><p>Os termos')],
               chamada="Leia o texto para responder às questões de 01 a 03.")

COXINHA = ('<p class="chamada">Leia o texto para responder às questões 06 a 09.</p>'
           + R[6]["enunciado"].split('<p class="apoio"><strong>Leia o texto para responder às questões 06 a 09.</strong></p>')[1].split("[[FIG")[0]
           .replace("ponham‹HIFEN›nas", "ponham-nas"))

SABESP = ('<p class="chamada">Leia os textos para responder às questões de 21 a 23.</p>'
          '<p class="apoio">Considerada a maior companhia de saneamento do Brasil, a Sabesp foi criada no ano de 1973 a partir da fusão de seis empresas privadas que atuavam na distribuição de água e na coleta de esgotos em várias regiões do estado de São Paulo.' + A +
          'Nos primeiros anos, a empresa chegou a receber a adesão de, em média, oito cidades por mês, alcançando rapidamente o patamar de centenas de municípios atendidos e conseguindo diminuir, cada vez mais, o índice de mortalidade infantil.' + A +
          'Entre as conquistas que marcaram a história da Sabesp na década de 1970, estão as implantações do Sistema Cantareira, responsável pelo abastecimento de parcela significativa da Região Metropolitana de São Paulo, e, nos anos seguintes, dos sistemas integrados de distribuição de água e de coleta de esgotos.</p>'
          '<p class="fonte">&lt;https://tinyurl.com/zm7mht6k&gt; Acesso em: 28.02.23. Adaptado.</p>'
          '<p class="apoio">As estações de tratamento de água (ETAs) da Sabesp funcionam como verdadeiras fábricas para produzir água potável.' + A +
          'Atualmente, são tratados, aproximadamente, 120 mil litros de água por segundo.</p>'
          '<p class="fonte">&lt;https://tinyurl.com/ycfrmbt5&gt; Acesso em: 28.02.23. Adaptado.</p>')

Q = {
1: {"materia": "Português", "assunto": "Classes de palavras", "tags": [I],
    "enunciado": CAIPIRA,
    "explicacao": "<p>No contexto: “eram <strong>meio</strong> indígenas” = eram <strong>um pouco</strong> indígenas; a “<strong>gênese</strong> da música popular” = a <strong>origem</strong>; ritmos “<strong>distintos</strong>” = <strong>diferentes</strong>; uma identidade “<strong>própria</strong>” = <strong>particular</strong>. Alternativa <strong>C</strong>.</p><p>“Metade” (B e D) muda o sentido de “meio”, que aqui é advérbio de intensidade (“um pouco”), não numeral. “Ora” (E) indica alternância. “Contribuição” e “força” não equivalem a “gênese”. E “genérica” (E) diz o contrário de “própria”.</p>"},
2: {"materia": "Português", "assunto": "Interpretação de texto",
    "apoio_de": (1, P1),
    "explicacao": "<p>No trecho, a viola “tornou-se ‘um instrumento que tem ligação com essa crônica’”. “Crônica”, aqui, é a <strong>história</strong> que o texto vinha contando: a chegada da viola, seu uso pelas classes pobres e pelos escravizados. Ou seja, os <strong>elementos históricos</strong> da incorporação da viola à nossa cultura. Alternativa <strong>E</strong>.</p><p>O texto não fala do desaparecimento da viola (A), de reis portugueses (B), de um texto jornalístico (C) nem da brevidade do próprio texto (D).</p>"},
3: {"materia": "História", "assunto": "Brasil República", "tags": [I],
    "apoio_de": (1, P1),
    "explicacao": "<p>O último parágrafo diz que a cultura caipira foi depreciada na era da industrialização, vista como contrária à modernização, mas acabou sendo “uma âncora de representação identitária até da elite paulista”. Alternativa <strong>D</strong>.</p><p>Os bandeirantes eram “meio indígenas”: andavam descalços e teciam as próprias roupas (A). A viola chegou com a colonização portuguesa, muito antes da Revolução Industrial (B). A cultura caipira nasceu do <strong>encontro</strong> de bandeirantes e indígenas, já na colonização (C). E a música caipira é simples na técnica, mas sofisticada no ritmo (E).</p>"},
4: {"materia": "História", "assunto": "Brasil Colônia",
    "apoio_de": (1, P1),
    "explicacao": "<p>O encontro entre bandeirantes portugueses e indígenas aconteceu nas <strong>bandeiras</strong>: expedições que partiam de São Paulo, no período colonial, para capturar e escravizar indígenas e procurar ouro e pedras preciosas. Alternativa <strong>B</strong>.</p><p>As migrações do século XX (A) e a industrialização da década de 1960 (D) são muito posteriores. A viola não chegou à corte (C). E ela foi trazida pelos portugueses, não pelos africanos (E).</p>"},
5: {"materia": "Física", "assunto": "Ondas",
    "enunciado": enun(R, 5, figs={"p03-1": 1}) + "<p>Assinale a alternativa que apresenta o ponto na imagem em que um violeiro deve pressionar a corda para que seja gerado o som mais agudo na viola.</p>",
    "imagens": [{"arquivo": "q05", "alt": "Desenho de uma viola deitada, com o corpo à esquerda e o braço à direita. Ao longo do braço há cinco pontos marcados, do corpo para a ponta: A (bem perto da boca da viola), B, C, D e E (perto da cabeça do instrumento)."}],
    "explicacao": "<p>O som mais agudo é o de <strong>maior frequência</strong>. Pelo texto, quanto <strong>menor</strong> o comprimento da corda que vibra, maior a frequência. A parte da corda que vibra vai do ponto pressionado até o corpo da viola. Pressionando em <strong>A</strong>, o ponto mais próximo do corpo, sobra o menor trecho vibrando e o som fica mais agudo. Alternativa <strong>A</strong>.</p><p>Os pontos B, C, D e E deixam trechos cada vez mais longos vibrando, com sons cada vez mais graves.</p>"},
6: {"materia": "Português", "assunto": "Interpretação de texto",
    "enunciado": COXINHA + P6,
    "explicacao": "<p>O texto apresenta várias versões para a origem da coxinha (“rodeada de histórias e lendas”), mostra que a receita foi “modificada no Brasil” e cita São Paulo e Limeira. A origem é incerta, a receita mudou e o salgado é popular em São Paulo. Alternativa <strong>C</strong>.</p><p>A receita francesa citada é de 1780, século XVIII, e foi modificada (A). A cozinheira tentou <strong>recriar</strong> uma coxa de galinha, e a tentativa não é descrita como falha (B). O salgado era um lanche barato para operários, não símbolo da elite (D). E o texto não fala em estratégia de marketing (E).</p>"},
7: {"materia": "Português", "assunto": "Gêneros textuais",
    "apoio_de": (6, P6),
    "explicacao": "<p>O texto traz, entre aspas, uma receita antiga com <strong>verbos no imperativo</strong>: “Tomem”, “desossem-nas”, “recheiem-nas”, “fechem”, “fritem-nas”. São comandos a seguir: isso é próprio do tipo textual <strong>injuntivo</strong>. Alternativa <strong>B</strong>.</p><p>As evidências sobre a origem não são irrefutáveis, e o texto mostra várias versões (A). Ele não conta uma trajetória completa até a chegada ao Brasil (C), não descreve o sabor da coxinha (D) e não enfatiza a criatividade dos cozinheiros (E).</p>"},
8: {"materia": "Matemática", "assunto": "Razão e proporção", "tags": [I],
    "apoio_de": (6, P6),
    "explicacao": "<p>A receita pede 12 coxas, e o aluno tem 5 a menos: 7 coxas. Reduzindo proporcionalmente: \\(840 \\times \\dfrac{7}{12} = 70 \\times 7 = 490\\) g de pão ralado. Alternativa <strong>C</strong>.</p><p>350 g (B) seria a quantidade para 5 coxas, ou seja, só a parte que faltou.</p>"},
9: {"materia": "Projeto de vida", "assunto": "Projeto de vida e carreira", "tags": [I],
    "apoio_de": (6, P6),
    "explicacao": "<p>Sem coxas suficientes, a cozinheira não desistiu: teve a <strong>iniciativa</strong> de testar uma solução nova, transformando uma galinha inteira em “coxas”, e criou um <strong>produto</strong> novo. Isso é empreendedorismo. Alternativa <strong>E</strong>.</p><p>Ela agiu “por medo de represálias”, e não por paciência e empatia (A) ou por restrições alimentares do menino, que só gostava de coxas (B). O texto não fala em tentativa e erro (C) nem em fracasso aceitável (D).</p>"},
10: {"materia": "História", "assunto": "Brasil Colônia", "tags": [I],
     "enunciado": enun(R, 10, ["Conforme as informações"]),
     "explicacao": "<p>O culto começou em 1717 (<strong>Brasil Colônia</strong>), recebeu presentes da princesa Isabel no século XIX (<strong>Império</strong>), e a santa virou padroeira em 1930 e ganhou feriado em 1980 (<strong>República</strong>). Alternativa <strong>E</strong>.</p><p>A devoção surgiu com pescadores, mais de cem anos antes dos presentes da princesa Isabel (A). Ela não é restrita a uma classe social (B), teve apelo popular desde o início (C) e foi reconhecida pelas autoridades, com padroeira e feriado (D).</p>"},
11: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade",
     "enunciado": enun(R, 11) + "<p>Assinale a alternativa que apresenta ações que impactam positivamente o meio ambiente.</p>",
     "alternativas": {"A": "A recuperação de áreas degradadas e o esgotamento dos recursos naturais.",
                      "B": "A destruição da camada de ozônio e a utilização de energia eólica.",
                      "C": "A utilização de produtos biodegradáveis e a reciclagem de materiais.",
                      "D": "A potencialização do efeito estufa e a modificação de habitat.",
                      "E": "A diminuição de mananciais e a extinção de espécies."},
     "explicacao": "<p>Produtos biodegradáveis se decompõem mais rápido, e a reciclagem reduz o lixo e a extração de matéria-prima. As <strong>duas</strong> ações são positivas: alternativa <strong>C</strong>.</p><p>Nas alternativas A e B, uma ação é positiva (recuperar áreas degradadas, energia eólica) e a outra é negativa (esgotar recursos, destruir a camada de ozônio). As alternativas D e E só têm ações negativas.</p>"},
12: {"materia": "Projeto de vida", "assunto": "Projeto de vida e carreira",
     "enunciado": "<p>Leia o cartum.</p>[[fig:1]]<p class=\"fonte\">&lt;https://tinyurl.com/449s3jnc&gt; Acesso em: 03.03.2023.</p><p>De acordo com o cartum, o aprimoramento do intelecto pressupõe que o indivíduo</p>",
     "imagens": [{"arquivo": "q12", "alt": "Cartum “Mundo Avesso”, de Carlos Ruas. À esquerda, uma pedra baixa e arredondada, chamada “Ignorância”, onde uma pessoa está deitada confortavelmente dizendo “Tá tão bom aqui.”. À direita, uma torre alta e estreita, chamada “Intelecto”, com uma escada em espiral que sobe até o topo."}],
     "explicacao": "<p>No cartum, ficar deitado na “Ignorância” é confortável (“Tá tão bom aqui”), enquanto o “Intelecto” é uma torre alta, que exige esforço para subir. Desenvolver o intelecto exige <strong>sair da zona de conforto</strong>. Alternativa <strong>B</strong>.</p><p>Deitar e procrastinar (A) é justamente o que mantém a pessoa na ignorância. O cartum não trata de empatia (C), de contar com o destino (D) nem de saúde física (E).</p>"},
13: {"materia": "Química", "assunto": "Substâncias e misturas",
     "enunciado": '<p class="apoio">A Companhia Ambiental do Estado de São Paulo (CETESB) é a agência do Governo do Estado responsável pelo controle, pela fiscalização, pelo monitoramento e pelo licenciamento de atividades geradoras de poluição.' + A +
                  'Em relação à qualidade do ar, há monitoramento automático para a avaliação de SO<sub>2</sub>, de material particulado inalável (MP<sub>10</sub>), de ozônio (O<sub>3</sub>), de óxidos de nitrogênio (NO e NO<sub>2</sub> – NOx), de monóxido de carbono (CO) e de hidrocarbonetos não-metânicos (NMHC); além disso, monitoram-se os parâmetros meteorológicos, como direção e velocidade do vento, temperatura e umidade relativa do ar.</p>'
                  '<p class="fonte">&lt;https://tinyurl.com/496kkmmb&gt; Acesso em: 01.03.23. Adaptado.</p><p>Entre as substâncias monitoradas pela CETESB, temos o</p>',
     "alternativas": {"A": "SO<sub>2</sub>, formado por átomos de 3 elementos químicos.",
                      "B": "O<sub>3</sub>, formado por 3 átomos de 1 elemento químico.",
                      "C": "NO<sub>2</sub>, formado por átomos de 3 elementos químicos.",
                      "D": "NO e o NO<sub>2</sub>, que diferem por 1 elemento químico.",
                      "E": "CO, que, diferentemente do CO<sub>2</sub>, é formado por 2 elementos químicos."},
     "explicacao": "<p>O ozônio, O<sub>3</sub>, tem <strong>3 átomos</strong> de um só elemento, o oxigênio. Alternativa <strong>B</strong>.</p><p>SO<sub>2</sub> (A) e NO<sub>2</sub> (C) têm 3 átomos, mas de apenas <strong>2</strong> elementos. NO e NO<sub>2</sub> (D) têm os mesmos elementos e diferem por 1 <strong>átomo</strong> de oxigênio. E CO e CO<sub>2</sub> (E) são formados pelos mesmos 2 elementos, carbono e oxigênio.</p>"},
14: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": [I],
     "enunciado": re.sub(r"produz</p>\[\[FIG:p06-1\]\]<p><strong>VESTIBULINHO[^<]*<sup>o</sup>[^<]*</strong> • ", "produz ", R[14]["enunciado"]),
     "explicacao": "<p>O texto diz que o Butantan produz soros “a partir da imunização de cavalos com antígenos”. O animal recebe o antígeno e produz anticorpos; depois, retira-se parte do sangue dele para extrair esses <strong>anticorpos</strong>, que formam o soro. Alternativa <strong>E</strong>.</p><p>A <em>Yersinia pestis</em> causa a peste bubônica, não a febre amarela nem a poliomielite (A). A peste é bacteriana, e o soro contém anticorpos prontos, não antígenos antivirais (B). O soro antipestoso era injetado nas <strong>pessoas</strong>, não usado para matar pulgas (C). E o soro, não a vacina, é usado contra envenenamentos (D).</p>"},
15: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade",
     "explicacao": "<p>O texto diz que a ponte foi sugerida “com o propósito de servir de suporte à instalação de uma tubulação a fim de conduzir o esgoto coletado nas cidades de Santos e de São Vicente” até o oceano. Alternativa <strong>C</strong>.</p><p>O esgoto ia das cidades para o oceano, não o contrário (A). Saturnino de Brito era engenheiro, e a peste bubônica é causada por bactéria, não por vírus (B). Itaipu, no texto, é uma ponta em Praia Grande, não a usina hidrelétrica (D). E Japuí e Barbosas são morros, não municípios (E).</p>"},
16: {"materia": "História", "assunto": "Brasil República", "tags": [I],
     "enunciado": enun(R, 16, figs={"p07-1": 1}).replace("[[fig:1]]", '[[fig:1]]<p class="fonte">&lt;https://tinyurl.com/2p85yzyn&gt; Acesso em: 29.04.2023.</p>'),
     "imagens": [{"arquivo": "q16", "alt": "Anúncio antigo, em preto e branco, sobre um fundo de mosaico de cacos. No centro, um círculo com o texto: “Caco colorido de cerâmica bem aplicado é bonito, bonito e barato”."}],
     "explicacao": "<p>O texto fala das décadas de 1940 a 1960, com indústrias cerâmicas, operários e a chegada dos prédios. Nesse período, São Paulo se <strong>consolidou como metrópole industrial</strong>, sobretudo a partir de 1950, com as montadoras de automóveis. Alternativa <strong>C</strong>.</p><p>São Paulo nunca foi capital do Brasil (A). Mem de Sá (B) e a vila pobre e isolada (D) são do século XVI. E a expansão do café ocorreu no interior do estado, no século XIX, não em bairros da capital (E).</p>"},
17: {"materia": "Química", "assunto": "Substâncias e misturas", "tags": [I],
     "enunciado": enun(R, 17, trocas=[("<p>Considere que densidade (d) é a razão entre a massa (<em>m</em>) e o volume (V) de uma amostra: <em>m </em> . d</p><p>V</p>",
                                       "<p>Considere que densidade (d) é a razão entre a massa (<em>m</em>) e o volume (V) de uma amostra: \\(d = \\dfrac{m}{V}\\).</p>")]),
     "explicacao": "<p>1 kg = 1 000 g. De \\(d = \\dfrac{m}{V}\\), temos \\(V = \\dfrac{m}{d} = \\dfrac{1000}{1{,}03} \\approx 970{,}9\\) cm³. Alternativa <strong>D</strong>.</p><p>1 030 (A) é o resultado de multiplicar massa e densidade, em vez de dividir. As outras alternativas erram a vírgula ou a conta.</p>"},
18: {"materia": "Química", "assunto": "Funções inorgânicas",
     "enunciado": enun(R, 18, trocas=[("<p>Ânion: Cℓ–</p>", "<p>Ânion: Cℓ<sup>–</sup></p>")]),
     "explicacao": "<p>Num sal, as cargas positivas e negativas se anulam. Na<sup>+</sup> e K<sup>+</sup> têm carga +1 e se combinam com um Cℓ<sup>–</sup>: NaCℓ e KCℓ. O Mg<sup>2+</sup> tem carga +2 e precisa de <strong>dois</strong> Cℓ<sup>–</sup>: MgCℓ<sub>2</sub>. Alternativa <strong>B</strong>.</p><p>MgCℓ (A) e Mg<sub>2</sub>Cℓ (C) não equilibram as cargas. E, por convenção, o cátion vem escrito primeiro na fórmula (D e E).</p>"},
19: {"materia": "Biologia", "assunto": "Ecologia",
     "enunciado": '<p class="chamada">Leia os textos para responder às questões 19 e 20.</p>'
                  '<p class="apoio"><strong>Lenda do Peixe Tapa</strong>' + A +
                  'Andava São Pedro passeando pelas praias de Ilhabela, em São Paulo, quando, preocupado com a maré, perguntou ao linguado: “a maré enche ou vaza?”.' + A +
                  'O linguado, em vez de responder direito, imitou São Pedro com voz fanhosa e boca torta.' + A +
                  'Então, São Pedro deu-lhe um tapa e lhe falou: “com os olhos para trás hás de ficar”.' + A +
                  'É por isso que o linguado é chamado de peixe tapa, é chato, tem boca torta e os olhos “por cima” das costas em um lado só.</p>'
                  '<p class="fonte">&lt;https://tinyurl.com/4kawxktv&gt; Acesso em:15.04.2023. Adaptado.</p>[[fig:1]]' + P19,
     "imagens": [{"arquivo": "q19", "alt": "Desenho de um linguado visto de cima: peixe achatado e oval, com nadadeiras em franja por toda a borda do corpo, manchas na pele e os dois olhos do mesmo lado da cabeça."}],
     "explicacao": "<p>Mudar de cor para se confundir com o ambiente e ficar quase invisível é <strong>camuflagem</strong>. Alternativa <strong>C</strong>.</p><p>Protocooperação (A), comensalismo (B), inquilinismo (D) e predatismo (E) são relações ecológicas entre espécies diferentes, não adaptações de um animal ao ambiente.</p>"},
20: {"materia": "Geografia", "assunto": "Movimentos da Terra", "tags": [I],
     "enunciado": enun(R, 20, figs={"p09-2": 1}).replace("[[fig:1]]", '[[fig:1]]<p class="fonte">&lt;https://tinyurl.com/ypuc8c79&gt; Acesso em: 14.04.2023. Original colorido.</p>'),
     "apoio_de": (19, P19),
     "imagens": [{"arquivo": "q20", "alt": "Quadrinhos em cinco faixas, no espaço. A Terra chama a Lua: “Ei, psiu!”. A Lua: “Tá falando comigo?”; a Terra: “É! Você mesmo!”. A Terra: “Vem aqui um pouquinho!”; a Lua: “Pra quê?”. A Terra: “Só pra eu testar uma coisa”. A Lua: “Tá”, e se aproxima. Na última faixa, uma onda gigante cobre os prédios de uma cidade."}],
     "explicacao": "<p>A Lua atrai a água dos oceanos. As regiões da Terra mais próximas da Lua sofrem atração maior, e ali o nível do mar sobe: é a <strong>maré alta</strong>. Com a rotação da Terra, diferentes regiões passam por essa posição ao longo do dia. Nos quadrinhos, a Lua chega perto demais e o mar invade a cidade. Alternativa <strong>E</strong>.</p><p>A Lua não sai de sua órbita para formar as marés (A e B). E as marés dependem principalmente da Lua, não de ser dia ou noite (C e D).</p>"},
21: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade", "tags": [I],
     "enunciado": SABESP + P21,
     "explicacao": "<p>O texto diz que a Sabesp atua na distribuição de água e na coleta de esgotos e que, com isso, conseguiu diminuir a mortalidade infantil. Água tratada e esgoto coletado evitam doenças. Alternativa <strong>C</strong>.</p><p>A Sabesp surgiu da fusão de empresas <strong>privadas</strong> (A). Recebeu adesão de <strong>cidades</strong>, não de outros estados (B). O Cantareira abastece parte da Região Metropolitana de São Paulo, não o estado inteiro (D). E as ETAs produzem água potável, não água destilada (E).</p>"},
22: {"materia": "Matemática", "assunto": "Operações e problemas",
     "apoio_de": (21, P21),
     "explicacao": "<p>Metade de 375 é 187,5, então é preciso ultrapassar esse número: <strong>188</strong> municípios. Com 8 adesões por mês: \\(\\dfrac{188}{8} = 23{,}5\\) meses. São necessários 24 meses, ou seja, <strong>2 anos</strong>, o menor número inteiro de anos que resolve o problema. Alternativa <strong>E</strong>.</p><p>1,00, 1,25, 1,50 e 1,75 ano equivalem a 12, 15, 18 e 21 meses: tempo insuficiente para mais da metade (A a D). Além disso, só 1,00 e 2,00 são números inteiros.</p>"},
23: {"materia": "Matemática", "assunto": "Notação científica", "tags": [I],
     "enunciado": "<p>A vazão (z) é a rapidez com que o volume (v) de um determinado fluido escoa ao longo do tempo (t), ou seja, \\(z = \\dfrac{v}{t}\\).</p>"
                  "<p>De acordo com o texto, podemos considerar que a vazão de água potável da Sabesp é de aproximadamente 1,2 × 10<sup>5</sup> L/s.</p>"
                  "<p>Para determinar o volume tratado em 1 minuto, temos que:</p>"
                  "\\[z = \\frac{v}{t} \\rightarrow 1{,}2 \\times 10^5\\ \\text{L/s} = \\frac{v}{60\\ \\text{s}}\\]"
                  "\\[\\rightarrow v = (1{,}2 \\times 10^5\\ \\text{L/s}) \\times 60\\ \\text{s}\\]"
                  "\\[\\rightarrow v = 72 \\times 10^5\\ \\text{L} = 7{,}2 \\times 10^6\\ \\text{L}.\\]"
                  "<p>Dessa forma, ao fim de um dia, a Sabesp terá tratado um volume, em litros, de aproximadamente</p>",
     "apoio_de": (21, P21),
     "explicacao": "<p>Um dia tem 24 × 60 = 1 440 minutos. Em 1 minuto são 7,2 × 10<sup>6</sup> L, então em um dia: \\(7{,}2 \\times 10^6 \\times 1440 \\approx 1{,}04 \\times 10^{10}\\) L. Alternativa <strong>D</strong>.</p><p>As outras alternativas erram a potência de 10, por exemplo usando horas em vez de minutos.</p>"},
24: {"materia": "Química", "assunto": "Separação de misturas", "tags": [I],
     "enunciado": enun(R, 24, trocas=[('<p class="fonte">&lt;https://tinyurl.com/ycfrmbt5&gt; Acesso em: 28.02.23. Adaptado.</p>', "")]).replace("</p><p>Nessa última", '</p><p class="fonte">&lt;https://tinyurl.com/ycfrmbt5&gt; Acesso em: 28.02.23. Adaptado.</p><p>Nessa última'),
     "explicacao": "<p>Na decantação, os flocos de sujeira, mais <strong>densos</strong> que a água, afundam e se acumulam no fundo dos tanques, de onde são retirados. Alternativa <strong>E</strong>.</p><p>Os flocos não derretem nem evaporam (A e B). Eles não se dissolvem; se dissolvessem, não poderiam ser separados por decantação (C). E, por serem mais densos, eles afundam em vez de boiar (D).</p>"},
25: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": [I],
     "explicacao": "<p>O texto diz que o flúor se une ao cálcio e ao fosfato do esmalte e forma um material resistente, que ajuda a prevenir as cáries causadas pelos ácidos das bactérias. Alternativa <strong>E</strong>.</p><p>A higiene bem feita <strong>reduz</strong> as bactérias e as placas (A). A acidez produzida pelas bactérias <strong>desmineraliza</strong> o esmalte (B). O flúor não digere restos de comida (C). E a fluoretação diminui a desmineralização, não a aumenta (D).</p>"},
26: {"materia": "Geografia", "assunto": "Meio ambiente e sociedade",
     "enunciado": '<p class="apoio">Promessa vem, promessa vai. Já são muitos anos de juras e sonhos de despoluição do Tietê, o maior rio do estado de São Paulo.' + A +
                  'A degradação dessa veia aquática começou ainda na década de 1940, e, hoje, quem passa pelas suas margens tem que tapar as narinas. Estudo recém-divulgado pela Fundação SOS Mata Atlântica traz o retrato da degradação: o trecho morto do rio Tietê chegou a 163 km em 2019, aumento de 33,6 % em relação aos 122 km do ano anterior e está muito maior que a poluição registrada na série histórica (71 km em 2014).</p>'
                  '<p class="fonte">&lt;https://tinyurl.com/4kcsn444&gt; Acesso em: 13.03.2023. Adaptado.</p><p>De acordo com o texto, é correto afirmar que</p>',
     "explicacao": "<p>O trecho morto passou de 122 km (2018) para 163 km (2019): \\(163 - 122 = 41\\) km a mais. Alternativa <strong>D</strong>.</p><p>A poluição começou na década de 1940, não no século XIX (A), e há mais de oitenta anos, não menos de vinte (B). 122 km é o trecho morto em 2018, não o tamanho do rio, e 71 km é de 2014 (C). E o texto não diz que havia promessas de limpeza em 1940 por pressão popular (E).</p>"},
27: {"materia": "História", "assunto": "Brasil Império",
     "enunciado": '<p class="apoio">O Museu Paulista da Universidade de São Paulo, também conhecido como Museu do Ipiranga, é o museu público mais antigo da nossa capital, e sua sede é um monumento-edifício. É o mais importante museu da Universidade de São Paulo (USP) e um dos mais visitados da cidade.' + A +
                  'O museu foi inaugurado oficialmente em 7 de setembro de 1895 com o nome Museu de História Natural. Atualmente caracteriza-se como uma instituição científica, cultural e educacional que exerce pesquisa, ensino e extensão com atuação no campo da História.</p>'
                  '<p class="fonte">&lt;https://tinyurl.com/2ehjfu5f&gt; Acesso em: 17.03.2023. Adaptado.</p><p>O museu apresentado no texto foi fundado para celebrar</p>',
     "explicacao": "<p>O Museu do Ipiranga fica às margens do riacho do Ipiranga, onde D. Pedro I proclamou a Independência, e foi inaugurado num <strong>7 de setembro</strong>. O prédio foi construído como monumento à <strong>Proclamação da Independência</strong>. Alternativa <strong>E</strong>.</p><p>A anexação do Acre (A) foi em 1903, depois da inauguração. O texto não liga o museu à Guerra do Paraguai (B), à chegada da família real (C) nem ao extermínio de indígenas (D).</p>"},
28: {"materia": "Projeto de vida", "assunto": "Ética e cidadania",
     "enunciado": enun(R, 28, figs={"p12-1": 1}),
     "imagens": [{"arquivo": "q28", "alt": "Infográfico “Projeto de vida”, do programa Inova Educação, do governo de São Paulo. Uma pessoa sobe uma escada até uma nuvem com “Atividades trabalhadas de forma progressiva”. De um lado da escada, perguntas; do outro, atividades: “Com o que eu quero trabalhar?”, visita a espaços de trabalho e entrevista com profissionais; “O que mais eu quero estudar?”, pesquisa sobre universidades e cursos; “Como seguir estudando vai me ajudar a atingir os meus sonhos?”, retomada dos sonhos e conexão com oportunidades do ensino médio; “Como posso ser um cidadão mais participativo?”, trabalho voluntário; “Quais são os meus sonhos?”, levantamento de sonhos a partir de filmes inspiradores; “Como lidar com as novas demandas escolares?”, criação de agenda de atividades escolares."}],
     "explicacao": "<p>No infográfico, a atividade ligada à pergunta “Como posso ser um cidadão mais participativo?” é o <strong>trabalho voluntário</strong>. Visitar e conversar com pacientes internados é um exemplo de voluntariado. Alternativa <strong>D</strong>.</p><p>As outras alternativas são atividades remuneradas, profissionais ou comerciais (A, B, C e E), e não trabalho voluntário.</p>"},
29: {"materia": "Português", "assunto": "Gêneros textuais", "tags": [I],
     "enunciado": '<p class="chamada">Leia o texto para responder às questões 29 e 30.</p>[[fig:1]]<p class="fonte">&lt;https://tinyurl.com/2zhyhejb&gt; Acesso em: 03.03.2023. Original colorido.</p>' + P29,
     "imagens": [{"arquivo": "q29", "alt": "Charge de Gu Charges. No alto, a legenda “Enquanto isso na grande...”. Um ciclista sorridente pedala por uma cidade, ao lado de uma placa que aponta para “Centro” e “Litoral”, e diz: “Nada melhor que uma bike para desestressar!”. Ele carrega na bicicleta uma enorme garrafa de vidro com um engarrafamento de carros, ônibus e caminhões dentro, cheia de fumaça."}],
     "explicacao": "<p>A charge opõe o ciclista, que se move livremente (mobilidade), ao trânsito parado dentro de uma garrafa (imobilidade). A garrafa representa uma expressão figurada, o “engarrafamento”, tomada ao pé da letra. Alternativa <strong>A</strong>.</p><p>Não há nenhuma intervenção divina na imagem (B). A bicicleta aparece como solução, e não como algo inviável (C e E). E a charge não diz que o problema é impossível de resolver (D).</p>"},
30: {"materia": "Português", "assunto": "Conectivos",
     "apoio_de": (29, P29),
     "explicacao": "<p>Em “Nada melhor <strong>que</strong> uma bike”, o “que” introduz o segundo termo de uma <strong>comparação</strong> e depende de “melhor”. Alternativa <strong>D</strong>.</p><p>“Enquanto” indica tempo simultâneo, e não alternância (A). “Isso” é pronome demonstrativo e retoma o que se vê na cena (B). As reticências de “Enquanto isso na grande...” deixam a frase em suspenso, sem enumeração (C). E, em “para desestressar”, “para” indica finalidade, não destino (E).</p>"},
31: {"materia": "História", "assunto": "Brasil Império",
     "enunciado": enun(R, 31, ["Inaugurada em 1867"], chamada="Leia o texto para responder às questões 31 e 32.").split("<p>O texto menciona")[0] + P31,
     "explicacao": "<p>No século XIX, o café era o <strong>principal produto de exportação</strong> do Brasil, vendido principalmente para os Estados Unidos e a Europa. Por isso era preciso uma ferrovia que levasse a produção do interior ao porto de Santos. Alternativa <strong>E</strong>.</p><p>O café superou o tabaco e o açúcar nesse período (A). Ele era exportado, não voltado ao mercado interno (B), e era produzido no Brasil, não importado da Etiópia (C). E ocupava posição central, não irrelevante, nas exportações (D).</p>"},
32: {"materia": "Física", "assunto": "Cinemática", "tags": [I],
     "apoio_de": (31, P31),
     "explicacao": "<p>A Estação Valongo é o marco zero (km 0) e a da Luz fica no quilômetro 79. A distância é de 79 km, percorrida em 2 horas: \\(v = \\dfrac{79}{2} = 39{,}5\\) km/h. Alternativa <strong>C</strong>.</p><p>69,5 km/h (A) seria usar os 139 km até Jundiaí. E 34,5 km/h (D) sai de dividir 69 por 2.</p>"},
33: {"materia": "Geografia", "assunto": "Agropecuária e meio ambiente", "tags": [I],
     "enunciado": enun(R, 33, ["Atualmente, um dos"]),
     "explicacao": "<p>O Brasil é o maior exportador de <strong>soja</strong> do mundo, e o porto de Santos, o maior do país, é um dos principais pontos de saída desse grão. Alternativa <strong>E</strong>.</p><p>O Brasil importa semicondutores (A), fertilizantes (C) e trigo (D), em vez de exportá-los em grande quantidade. E o óleo de palma (B) não está entre os principais produtos exportados por Santos.</p>"},
34: {"materia": "História", "assunto": "Brasil República",
     "enunciado": enun(R, 34, trocas=[('<p class="apoio">CAMPOS, C.;', '<p class="fonte">CAMPOS, C.;')]),
     "explicacao": "<p>O texto diz que cada nome “recordaria vários acontecimentos históricos que marcaram o estado de São Paulo” e que as referências fazem menção “à localização geográfica do país (América Latina) e às correntes imigratórias”. Alternativa <strong>D</strong>.</p><p>O texto não fala em padrão do governo federal (A) nem em cópia por outras ferrovias (B); e a linha é de 1904, não do século XVII. A imigração japonesa começou em 1908, e não no século XIX (C). E o texto diz que muitos nomes “foram posteriormente mudados” (E).</p>"},
35: {"materia": "Projeto de vida", "assunto": "Projeto de vida e carreira",
     "enunciado": "<p>Leia os textos</p>"
                  '<p class="apoio">A única revolução possível é a que se faz dentro de nós. Não é possível libertar um povo sem, antes, livrar-se da escravidão de si mesmo. Sem esta [revolução interna], qualquer outra será insignificante, efêmera e ilusória, quando não um retrocesso. Cada pessoa tem sua caminhada própria. Faça o melhor que puder. Seja o melhor que puder. O resultado virá na mesma proporção de seu esforço. Compreenda que, se não veio, cumpre a você (a mim e a todos) modificar suas (nossas) técnicas, visões, verdades etc. Nossa caminhada somente termina no túmulo. Ou até mesmo além… Segue a essência de quem teve sucesso em vencer um império…</p>'
                  '<p class="fonte">GANDHI, Mahatma. <em>A única revolução possível é dentro de nós</em>.</p>'
                  '<p class="apoio">[…] O sentido da vida é tudo aquilo que nos encaminha na direção da realização do nosso projeto. Cada vez que você dá um passo […] na direção da consecução do seu projeto, você se realiza como pessoa. […] Uma vida sem rumo deve ser como um barco sem bússola, um filme sem roteiro.</p>'
                  '<p class="fonte">COSTA, Antônio Carlos Gomes da. <em>Educação e vida</em>. Belo Horizonte: Modus Faciendi, 2001. p. 34-35. &lt;https://tinyurl.com/2tk27pm2&gt; Acesso em: 13.03.2023. Adaptado.</p>'
                  "<p>Com base nos textos, é correto afirmar que</p>",
     "explicacao": "<p>O primeiro texto diz que “cada pessoa tem sua caminhada própria” e pede “faça o melhor que puder”; o segundo, que cada passo em direção ao próprio projeto nos realiza como pessoa. Os dois valorizam <strong>traçar os próprios caminhos</strong> e o <strong>esforço</strong>. Alternativa <strong>B</strong>.</p><p>Os textos falam de uma revolução interna, não industrial (A). O barco sem bússola representa uma vida <strong>sem</strong> rumo, o contrário de um projeto estruturado (C). O “império” vencido, na fala de Gandhi, é o domínio britânico sobre a Índia, não um regime a ser criado (D). E os textos não defendem retrocessos (E).</p>"},
36: {"materia": "Biologia", "assunto": "Doenças e saúde",
     "enunciado": enun(R, 36),
     "explicacao": "<p>Os fatores de risco que podem ser modificados incluem o peso, a alimentação, o sedentarismo e o uso correto de remédios. <strong>Controlar o excesso de peso</strong> e <strong>tomar as medicações indicadas</strong> são atitudes importantes. Alternativa <strong>D</strong>.</p><p>Pressão alta, falta de exames (A), sedentarismo (B), excesso de sal e de álcool (C) e dieta gordurosa sem verduras (E) são justamente fatores que aumentam o risco de doenças do coração.</p>"},
37: {"materia": "História", "assunto": "Brasil República",
     "enunciado": enun(R, 37, chamada="Leia o texto para responder às questões de 37 a 39."),
     "explicacao": "<p>O texto diz que a reforma procurou “eliminar os estigmas que ligavam São Paulo ao passado colonial”, e que a demolição da Igreja do Rosário dos Homens Pretos foi um exemplo disso. Alternativa <strong>C</strong>.</p><p>O triângulo recebeu “especial atenção” na reforma, em vez de ser excluído (A). O objetivo era eliminar o passado colonial, não preservá-lo (B). O cargo de prefeito foi criado em 1899, e não em 1911, que é quando Antônio Prado saiu (D). E o prefeito direcionou a modernização, em vez de interrompê-la (E).</p>"},
38: {"materia": "Matemática", "assunto": "Geometria plana",
     "enunciado": enun(R, 38, figs={"p17-1": 1}),
     "apoio_de": (37, P37),
     "imagens": [{"arquivo": "q38", "alt": "Mapa do centro histórico de São Paulo, com o Largo São Francisco, o Pateo do Collegio e o Largo São Bento. Uma linha preta grossa contorna a região, formando um polígono irregular com vários vértices: segue por cima, à direita, desce em diagonal pela borda direita e sobe pela esquerda."}],
     "explicacao": "<p>Contando os lados da linha preta no mapa, o polígono tem <strong>11 lados</strong>: é um <strong>undecágono</strong>. Alternativa <strong>D</strong>.</p><p>Apesar do nome “Triângulo Histórico”, a região atual não é um triângulo (A). Quadrilátero tem 4 lados (B), heptágono 7 (C) e dodecágono 12 (E).</p>"},
39: {"materia": "Matemática", "assunto": "Geometria plana",
     "enunciado": enun(R, 39, quebras=["• o Pateo do Collegio e o Largo São Bento", "• o Largo São Francisco e o Largo São Bento"]),
     "apoio_de": (37, P37),
     "explicacao": "<p>O triângulo tem dois lados iguais, de 500 m: é <strong>isósceles</strong>. Para saber o tipo de ângulo, comparamos o quadrado do maior lado com a soma dos quadrados dos outros dois: \\(800^2 = 640\\,000\\) e \\(500^2 + 500^2 = 500\\,000\\). Como 640 000 é maior, o ângulo oposto ao maior lado é obtuso: o triângulo é <strong>obtusângulo</strong>. Alternativa <strong>C</strong>.</p><p>Escaleno (B e D) teria os três lados diferentes. Se os dois valores fossem iguais, seria retângulo (E); se o quadrado do maior lado fosse menor, acutângulo (A).</p>"},
40: {"materia": "Biologia", "assunto": "Botânica",
     "enunciado": enun(R, 40, trocas=[("<p>•</p><p><em>Lago", "<p>• <em>Lago"), ("tartarugas; •</p><p><em>Bosque das", "tartarugas;</p><p>• <em>Bosque das"),
                                      ("móveis; e •</p><p><em>Bosque do", "móveis; e</p><p>• <em>Bosque do"), ("no texto , podemos", "no texto , podemos")]),
     "explicacao": "<p>Ciprestes e pinheiros são <strong>gimnospermas</strong>: plantas com sementes “nuas”, que não ficam dentro de frutos (como as pinhas). Alternativa <strong>B</strong>.</p><p>Animais respiram consumindo oxigênio e liberando gás carbônico, não o contrário (A). As plantas citadas têm clorofila e fazem fotossíntese (C). Pau-brasil e imbuia são árvores grandes, com vasos condutores; estão ameaçados pela exploração da madeira (D). E bichos-preguiça e bugios são herbívoros e fazem parte do ecossistema (E).</p>"},
41: {"materia": "História", "assunto": "Brasil Império",
     "enunciado": enun(R, 41),
     "explicacao": "<p>O texto diz que a Estrada das Lágrimas foi “batizada em homenagem à árvore” e que, nos anos 1980, a figueira foi declarada patrimônio ambiental e “imune de corte” pela Secretaria de Estado do Meio Ambiente. Alternativa <strong>E</strong>.</p><p>A árvore tem entre 360 e 400 anos, então nasceu por volta do século XVII (A). Quem quis derrubá-la foi o dono do terreno; o prefeito Firmiano Pinto a protegeu (B). D. Pedro I passou pela árvore, mas quem chorava eram as famílias dos soldados, e a Guerra do Paraguai foi no reinado de D. Pedro II (C). E ela é mais antiga que a guerra (D).</p>"},
42: {"materia": "Biologia", "assunto": "Evolução",
     "enunciado": enun(R, 42, trocas=[('<p>A descoberta descrita no texto evidencia corretamente que</p><p class="fonte">&lt;https://tinyurl.com/5bsxkp3x&gt; Acesso em: 04.03.2023. Adaptado.</p>',
                                       '<p class="fonte">&lt;https://tinyurl.com/5bsxkp3x&gt; Acesso em: 04.03.2023. Adaptado.</p><p>A descoberta descrita no texto evidencia corretamente que</p>')]),
     "explicacao": "<p>A partir de poucos ossos e um dente, os paleontólogos identificaram o grupo dos animais, sua alimentação, época, tamanho e peso. Os <strong>registros fósseis</strong> permitem estudar seres vivos de outras épocas. Alternativa <strong>D</strong>.</p><p>Os titanossauros não existem mais: as espécies mudaram (A). Um ser totalmente decomposto não deixa fóssil (B). Partes duras, como ossos e dentes, são as que mais fossilizam, como mostra o próprio texto (C). E as partes moles costumam ser decompostas antes de fossilizar (E).</p>"},
43: {"materia": "Matemática", "assunto": "Análise combinatória",
     "enunciado": enun(R, 43, quebras=["• a Capela das Mercês", "• a Estação Ferroviária", "• o Museu Frei Galvão", "• a Cachoeira Salto Botelho", "• a Fazenda Vila Rica", "• o Museu do Café, em Santos."]),
     "explicacao": "<p>A primeira parada é fixa: o Museu do Café. Sobram 6 destinos para as outras duas paradas, e a ordem importa. Para a segunda parada há 6 opções; para a terceira, 5. Total: \\(6 \\times 5 = 30\\) roteiros. Alternativa <strong>B</strong>.</p><p>15 (A) seria sem levar em conta a ordem. E 210 (E) seria escolher os três destinos em ordem entre os 7, sem fixar o primeiro (7 × 6 × 5).</p>"},
44: {"materia": "Geografia", "assunto": "Cartografia",
     "enunciado": "<p>Considere o mapa.</p><p>Vamos supor que a equipe de futebol da Ferroviária de Araraquara irá disputar uma partida de futebol amistosa contra a equipe do Paulista de Jundiaí no estádio deste.</p>[[fig:1]]"
                  "<p>O avião que transportará a equipe de Araraquara voará deste município, em linha reta, em direção ao município de Jundiaí no sentido</p>",
     "imagens": [{"arquivo": "q44", "alt": "Mapa do estado de São Paulo com algumas cidades. Araraquara fica no centro-norte do estado; Jundiaí fica mais abaixo e à direita, entre Campinas e São Paulo, perto do litoral. O símbolo do norte aponta para cima."}],
     "explicacao": "<p>No mapa, com o norte para cima, Jundiaí fica <strong>abaixo</strong> (ao sul) e <strong>à direita</strong> (a leste) de Araraquara. O sentido do voo é o <strong>sudeste</strong>. Alternativa <strong>D</strong>.</p><p>Noroeste (A) e nordeste (B) apontariam para cima; sudoeste (C) apontaria para baixo e para a esquerda; e norte (E), para cima.</p>"},
45: {"materia": "Matemática", "assunto": "Estatística",
     "enunciado": enun(R, 45).split("</p>")[0] + "</p>"
                  + tabela(["Destinos", "Avaliação no Google", "Avaliação no TripAdvisor"],
                           [["Aparecida", "4,76", "4,50"], ["Campos do Jordão", "4,57", "4,33"], ["Eldorado", "4,58", "4,30"], ["Ilhabela", "4,63", "4,47"], ["Olímpia", "4,41", "3,98"]])
                  + '<p class="fonte">fonte dos dados: &lt;https://tinyurl.com/yckj57ja&gt; Acesso em: 09.03.2023. Adaptado.</p>'
                  + "<p>De acordo com os dados apresentados, é correto afirmar que o destino turístico que possui a melhor avaliação média, considerando os dois sites, é</p>",
     "explicacao": "<p>Médias de cada destino: Aparecida \\(\\dfrac{4{,}76 + 4{,}50}{2} = 4{,}63\\); Campos do Jordão 4,45; Eldorado 4,44; Ilhabela 4,55; Olímpia 4,195. A maior é a de <strong>Aparecida</strong>. Alternativa <strong>A</strong>.</p>"},
46: {"materia": "Química", "assunto": "Substâncias e misturas",
     "explicacao": "<p>A água mineral contém água e vários <strong>sais minerais dissolvidos</strong>: é uma <strong>mistura</strong> homogênea. Alternativa <strong>E</strong>.</p><p>Substância composta (A) e substância pura (C) teriam só H<sub>2</sub>O, como a água destilada. Substância simples (B) é formada por um só elemento, como O<sub>2</sub>. E “mistura destilada” (D) não faz sentido: a destilação separa a água dos sais.</p>"},
47: {"materia": "Física", "assunto": "Pressão", "tags": [I],
     "enunciado": enun(R, 47).split("<p>Sabendo que")[0]
                  + "<p>Sabendo que a pressão atmosférica é inversamente proporcional à altitude, ao partir de Paranapiacaba em direção ao Porto de Santos, podemos sentir a orelha entupir porque a altitude ....<strong>(I)</strong>.... e, por isso, a pressão da orelha média irá ....<strong>(II)</strong>.... em relação ao seu valor no início da viagem.</p>"
                  + "<p>Assinale a alternativa que completa correta e respectivamente as lacunas do texto.</p>",
     "alternativas": colunas(["(I)", "(II)"], [["diminui", "aumentar"], ["diminui", "diminuir"], ["diminui", "se manter igual"], ["aumenta", "diminuir"], ["aumenta", "aumentar"]]),
     "explicacao": "<p>Paranapiacaba fica no alto da serra e Santos, no nível do mar: descendo, a altitude <strong>diminui</strong> (I). Como a pressão é inversamente proporcional à altitude, a pressão externa aumenta, e a pressão da orelha média precisa <strong>aumentar</strong> para se igualar a ela (II). Alternativa <strong>A</strong>.</p><p>Na descida, a altitude não aumenta (D e E). E, com a pressão externa maior, a da orelha não diminui nem fica igual (B e C): enquanto ela não aumenta, sentimos a orelha entupida.</p>"},
48: {"materia": "Projeto de vida", "assunto": "Ética e cidadania",
     "explicacao": "<p>Cristiane conta que começou jogando “somente com meninos — não tinha menina”, com preconceito, e que a família “não tinha condições financeiras”. Ela só pôde ir a uma escolinha graças a um vizinho. Alternativa <strong>C</strong>.</p><p>Não havia meninas nas partidas da infância dela (A), e o futebol feminino hoje está “muito melhor” do que antes (B). Ela precisou da ajuda do vizinho, e não teve facilidade (D). E não bastou o esforço próprio: o apoio de outras pessoas foi decisivo (E).</p>"},
49: {"materia": "Física", "assunto": "Termologia", "tags": [I],
     "enunciado": "<p>Uma das principais atrações turísticas da cidade de Boituva, no estado de São Paulo, é o passeio de balão de ar quente. O princípio de funcionamento desses balões está relacionado ao aumento ou à diminuição da densidade média do balão resultantes do resfriamento ou do aquecimento do ar em seu interior, respectivamente.</p>"
                  "<p>Dessa forma, para iniciar um passeio, o balonista deve ....<strong>(I)</strong>.... o ar no interior do balão. Assim, o ar irá se ....<strong>(II)</strong>...., ....<strong>(III)</strong>.... a densidade média do balão e, consequentemente, fazendo-o subir.</p>"
                  "<p>Assinale a alternativa que completa correta e respectivamente as lacunas do texto.</p>",
     "alternativas": colunas(["(I)", "(II)", "(III)"], [["aquecer", "expandir", "diminuindo"], ["resfriar", "expandir", "diminuindo"], ["aquecer", "expandir", "aumentando"], ["resfriar", "contrair", "aumentando"], ["aquecer", "contrair", "diminuindo"]]),
     "explicacao": "<p>Para subir, o balão precisa ficar menos denso que o ar em volta. O balonista <strong>aquece</strong> o ar (I); o ar quente se <strong>expande</strong> (II), parte dele sai do balão, e a densidade média do balão <strong>diminui</strong> (III). Alternativa <strong>A</strong>.</p><p>Resfriar o ar faz o balão descer (B e D). Com a expansão, a densidade não aumenta (C). E o ar aquecido não se contrai (E).</p>"},
50: {"materia": "Projeto de vida", "assunto": "Ética e cidadania", "tags": [I],
     "enunciado": "[[fig:1]]<p class=\"fonte\">&lt;https://tinyurl.com/mrzfa2dc&gt; Acesso em: 03.03.2023. Original colorido.</p>"
                  "<p>Nos quadrinhos dados, o humor é utilizado para criticar o uso constante de alguns recursos tecnológicos que podem levar à perda da autonomia.</p>"
                  "<p>Uma atitude possível para combater esse processo na sociedade atual é</p>",
     "imagens": [{"arquivo": "q50", "alt": "Quadrinho “Cientirinhas #260”, em quatro quadros. 1: uma menina conta para outra, que mexe no celular: “Sabe, eu tava lendo sobre um fungo parasita chamado cordyceps, que transforma formigas numa espécie de zumbi.” 2: uma formiga sobe numa árvore pensando: “Preciso achar luz... umidade... calor...”, com a legenda “O fungo invade o sistema nervoso da formiga e a controla como uma marionete.” 3: a menina diz, assustada: “Já pensou perder sua vontade própria? Espero que isso nunca aconteça com a gente.” 4: a amiga se afasta, com o celular erguido e o olhar vidrado: “Sem internet... preciso achar sinal de wi-fi...”, enquanto a primeira pergunta: “Eeei! Aonde você vai?”."}],
     "explicacao": "<p>Na tirinha, a menina presa ao celular age como a formiga controlada pelo fungo: perde a própria vontade. Para não ficar dependente da tecnologia, é preciso desenvolver o <strong>autoconhecimento</strong> e o <strong>senso crítico</strong>, que tornam a pessoa questionadora e independente. Alternativa <strong>E</strong>.</p><p>Usar ainda mais o celular (A) ou trocá-lo por um computador (B) não resolve a dependência. A (C) fala em contatos virtuais, que reforçam o problema. E linguagem informal (D) não tem relação com a perda de autonomia.</p>"},
}
completar(Q, R)
