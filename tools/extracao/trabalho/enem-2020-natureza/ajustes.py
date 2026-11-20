# Enem 2020 (impresso, 1ª aplicação, jan. 2021), 2º dia, caderno azul: Ciências da Natureza (questões 91 a 135; no site, 1 a 45).
# Texto do PDF legível (sem DECOD). Quadros das Q102, 122 e 125 em tabela HTML; equações das Q112 e 120 à mão.
# Alternativas-imagem nas Q93 e 113. Q135 anulada (Inep não deu motivo; análise: nenhuma alternativa descreve bem a origem do C. arabica).
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, paragrafos_enem

ID = "enem-2020-natureza"
META = {"id": ID, "banca": "Enem", "ano": 2020, "titulo": "Enem 2020: Ciências da Natureza", "fonte": "Inep", "dataExame": "2021-01-24",
        "duracaoMinutos": 150, "area": "Ciências da Natureza", "caderno": "azul", "dia": 2}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2020-dia2-azul")
Q = {}
P = lambda n: paragrafos_enem(D[n])
T = lambda n, i: P(n)[i][1]
p = lambda *xs: "".join(f"<p>{x}</p>" for x in xs)
ap = lambda *xs: "".join(f'<p class="apoio">{x}</p>' for x in xs)
fonte = lambda x: f'<p class="fonte">{x}</p>'
ALT = lambda ini: {k: f"[[fig:{i}]]" for i, k in enumerate("ABCDE", ini)}
LIMPA = lambda s: re.sub(r"fi ([a-zà-ú])", r"fi\1", re.sub(r"fl ([a-zà-ú])", r"fl\1", re.sub(r"(\w)- -(\w)", r"\1-\2", s)))
OL = lambda *xs: "<ol>" + "".join(f"<li>{x}</li>" for x in xs) + "</ol>"


def figs(*pares):
    return [{"arquivo": a, "alt": t} for a, t in pares]


def tabela(cab, linhas):
    return ('<table class="tabela"><thead><tr>' + "".join(f"<th>{c}</th>" for c in cab) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in l) + "</tr>" for l in linhas) + "</tbody></table>")


def E(n, pular=(), trocas=()):
    par = [x for i, x in enumerate(P(n)) if i not in pular]
    ult = max([i for i, (t, _) in enumerate(par) if t == "fonte"], default=-1)
    h = []
    for i, (t, x) in enumerate(par):
        if t == "fig": h.append(f"[[fig:{x}]]")
        elif t == "fonte": h.append(fonte(x))
        elif t == "titulo": h.append(f'<p class="apoio"><strong>{x}</strong></p>' if i < ult else f"<p><strong>{x}</strong></p>")
        elif i < ult: h.append(ap(x))
        else: h.append(p(x))
    s = "".join(h)
    for a, b in trocas:
        assert a in s, a; s = s.replace(a, b)
    return s


def X(n, materia, assunto, expl, imagens=(), tags=(), enun=None, trocas=(), alts=None, anulacao=None):
    e = LIMPA(enun or E(n))
    for a, b in trocas:
        assert a in e, a; e = e.replace(a, b)
    Q[n - 90] = {"materia": materia, "assunto": assunto, "area": "Ciências da Natureza", "tags": list(tags), "numeroOriginal": n,
                 "enunciado": e, "alternativas": {k: LIMPA(v) for k, v in dict(alts or D[n]["alternativas"]).items()},
                 "imagens": list(imagens), "explicacao": expl}
    if anulacao: Q[n - 90]["anulacao"] = anulacao


SUB = lambda s: re.sub(r"(?<=[A-Za-z\)])(\d+)", r"<sub>\1</sub>", s)
LISTA = lambda s: "<ul>" + "".join(f"<li>{x.strip()}</li>" for x in s.split("•") if x.strip()) + "</ul>"

X(91, "Física", "Eletrostática", "<p>Ao se esfregar na calça, o gato troca cargas por atrito: elétrons passam de um material para o outro, e os pelos ficam eletrizados (por isso se arrepiam, com os fios se repelindo). Na eletrização por atrito há <strong>movimentação de elétrons entre a calça e os pelos do gato</strong>. Alternativa <strong>D</strong>.</p><p>Prótons e átomos não se transferem (A e B), e as cargas não são criadas (C), só transferidas.</p>",
  figs(("q91", "Tirinha do Garfield em três quadros: o gato se esfrega nas pernas de calça de uma pessoa, ronronando (“PURRR”), e no último quadro aparece com todos os pelos arrepiados, pensando “Eu odeio eletricidade estática”.")),
  ["eletrização por atrito"])
X(92, "Química", "Polímeros", "<p>Polímeros convencionais, como o polietileno, levam centenas de anos para se decompor e se acumulam no ambiente. Os biodegradáveis são decompostos por microrganismos em pouco tempo. A grande vantagem é que <strong>são degradados em um tempo bastante menor que os convencionais</strong>. Alternativa <strong>D</strong>.</p><p>Eles ainda podem poluir e ter aditivos tóxicos (A e C), e a reciclagem continua desejável (B).</p>",
  tags=["polímeros biodegradáveis"])
X(93, "Física", "Eletrodinâmica", "<p>A carga de 60 Ah se esgota em 5 dias = 120 h: a corrente de fuga é i = 60/120 = <strong>0,5 A</strong>. Para medir corrente, o amperímetro deve ficar <strong>em série</strong>, entre a bateria e o circuito do veículo, de modo que toda a corrente passe por ele. Alternativa <strong>B</strong>.</p><p>Em A o amperímetro está em paralelo com a bateria; D e E marcam 12 A, e C marca 2,5 A.</p>",
  figs(("q93a", "Esquema A: circuito do veículo ligado aos dois polos da bateria, e o amperímetro, marcando 0,5 A, ligado também diretamente aos dois polos, em paralelo."),
       ("q93b", "Esquema B: um fio do circuito do veículo vai a um polo da bateria; o outro passa pelo amperímetro, marcando 0,5 A, antes de chegar ao outro polo, em série."),
       ("q93c", "Esquema C: circuito do veículo ligado à bateria, e o amperímetro, marcando 2,5 A, ligado em paralelo à bateria por baixo."),
       ("q93d", "Esquema D: amperímetro marcando 12 A em série entre o circuito do veículo e um polo da bateria."),
       ("q93e", "Esquema E: amperímetro marcando 12 A ligado em paralelo ao circuito do veículo, ambos ligados à bateria.")),
  ["amperímetro", "carga elétrica"], enun=p(T(93, 0)), alts=ALT(1))
X(94, "Química", "Funções orgânicas", "<p>Procura-se cadeia poli-insaturada (várias duplas ligações) com hidroxila (—OH) em carbono terminal, isto é, um álcool primário. A estrutura 1 (geraniol, o principal componente do óleo de rosas) tem duas duplas C=C e termina em CH<sub>2</sub>OH. Alternativa <strong>A</strong>.</p><p>A 2 e a 5 são aldeídos (CHO); a 3 é cíclica, saturada e com OH em carbono secundário; a 4 é um fenol.</p>",
  figs(("q94", "Cinco fórmulas estruturais: (1) cadeia aberta com duas duplas ligações terminando em CH₂OH; (2) cadeia aberta com uma dupla terminando em CHO; (3) anel de seis carbonos saturado com OH e grupo isopropila; (4) anel aromático com OH (fenol) e grupo isopropila; (5) cadeia com duas duplas e grupo CHO.")),
  ["álcool", "óleo essencial"], enun=p(T(94, 0)) + "[[fig:1]]" + p("Qual substância o empresário deverá utilizar?"),
  alts={"A": "1", "B": "2", "C": "3", "D": "4", "E": "5"})
X(95, "Biologia", "Ecologia", "<p>A população isolada numa ilha de mata pequena se extingue por falta de espaço, de alimento e de troca genética com outras populações. Ligar os fragmentos permite que os animais circulem entre eles: a medida é a <strong>construção de corredores ecológicos</strong>. Alternativa <strong>C</strong>.</p><p>O efeito de borda (B) é prejudicial e deve ser reduzido; espécies introduzidas (E) ameaçam as nativas.</p>",
  tags=["fragmentação de hábitats", "corredores ecológicos"])
X(96, "Química", "Cinética química", "<p>Massa molar da sacarose: 12 · 12 + 22 · 1 + 11 · 16 = 342 g/mol. 171 g = 0,5 mol em 0,5 L: concentração inicial de 1 mol/L. A concentração cai à metade a cada 100 min; em 400 min são 4 meias-vidas: 1/2<sup>4</sup> = 1/16 = <strong>6,25 × 10<sup>−2</sup> mol L<sup>−1</sup></strong>. Alternativa <strong>B</strong>.</p><p>1,25 × 10<sup>−1</sup> (C) corresponde a 3 meias-vidas.</p>",
  tags=["meia-vida", "concentração"], trocas=[("(C12H22O11)", "(C<sub>12</sub>H<sub>22</sub>O<sub>11</sub>)"), ("g mol−1", "g mol<sup>−1</sup>")],
  alts={"A": "2,50 × 10<sup>−3</sup> mol L<sup>−1</sup>", "B": "6,25 × 10<sup>−2</sup> mol L<sup>−1</sup>", "C": "1,25 × 10<sup>−1</sup> mol L<sup>−1</sup>", "D": "2,50 × 10<sup>−1</sup> mol L<sup>−1</sup>", "E": "4,27 × 10<sup>−1</sup> mol L<sup>−1</sup>"})
X(97, "Química", "Ciclos biogeoquímicos", "<p>O petróleo do pré-sal é carbono que ficou guardado sob sedimentos por milhões de anos. Ao ser extraído e queimado, libera CO<sub>2</sub> na atmosfera mais depressa do que os processos naturais conseguem absorver: desequilíbrio no ciclo do <strong>carbono, devido à liberação das cadeias carbônicas aprisionadas abaixo dos sedimentos</strong>. Alternativa <strong>D</strong>.</p><p>O petróleo é formado essencialmente por hidrocarbonetos, não por compostos de nitrogênio ou fósforo (A, B e E).</p>",
  tags=["pré-sal", "ciclo do carbono"])
X(98, "Física", "Eletromagnetismo", "<p>Pela lei de Faraday, a d.d.p. induzida é proporcional à rapidez com que o fluxo magnético varia. Se as pás giraram mais rápido sem mudança no ímã nem nas bobinas, a variação do fluxo ficou mais rápida: aumentou a <strong>rapidez com que o fluxo magnético varia através das bobinas, por meio de um aumento em sua velocidade angular</strong>. Alternativa <strong>D</strong>.</p><p>O aumento foi inesperado, durante o funcionamento: ninguém trocou bobinas ou ímãs (B, C e E).</p>",
  tags=["lei de Faraday", "gerador"])
X(99, "Física", "Cinemática", "<p>O carro acelera a 1 m/s<sup>2</sup> até 72 km/h = 20 m/s: leva 20 s e percorre 200 m. Daí segue a 20 m/s. O semáforo A (500 m) deve abrir quando o carro estiver a 400 m: 20 s + 200/20 = 30 s. B (1 000 m), com o carro a 900 m: 30 + 25 = 55 s. C, com o carro a 1 400 m: 80 s. Respostas: <strong>30 s, 55 s e 80 s</strong>. Alternativa <strong>D</strong>.</p><p>Esquecer os 100 m de antecedência daria 35 s, 60 s e 85 s (E).</p>",
  figs(("q99", "Esquema de uma avenida reta com quatro semáforos indicados por setas, na ordem O, A, B e C.")),
  ["MUV", "MU"], enun=p(T(99, 0)) + "[[fig:1]]" + p(T(99, 3).replace("1 m s−2", "1 m s<sup>−2</sup>").replace("72 km h−1", "72 km h<sup>−1</sup>")))
X(100, "Química", "Química orgânica", "<p>O PVC tem cloro ligado à cadeia. Ao ser aquecido, libera um gás diatômico heteronuclear (dois átomos diferentes): o <strong>HCl</strong>. Ele é ácido, muda a cor do indicador na solução alcalina e reage com carbonato de sódio liberando CO<sub>2</sub> (Na<sub>2</sub>CO<sub>3</sub> + 2 HCl → 2 NaCl + H<sub>2</sub>O + CO<sub>2</sub>). Alternativa <strong>E</strong>.</p><p>H<sub>2</sub> e Cl<sub>2</sub> (A e B) são homonucleares; CO<sub>2</sub> (D) é triatômico; CO (C) não libera CO<sub>2</sub> com carbonato.</p>",
  figs(("q100", "Fórmula do policloreto de vinila: unidade de repetição –CH₂–CHCl– entre colchetes, com índice n.")),
  ["PVC", "ácidos"], enun=p(T(100, 0)) + "[[fig:1]]" + p(SUB(T(100, 2).replace("Policloreto de vinila (PVC) ", ""))) + p(T(100, 3)),
  alts={"A": "H<sub>2</sub>", "B": "Cl<sub>2</sub>", "C": "CO", "D": "CO<sub>2</sub>", "E": "HCl"})
X(101, "Biologia", "Evolução", "<p>Em D1, depois que a barreira desaparece, as duas subpopulações voltam a ocupar a mesma área, mas continuam com cores separadas, sem formas intermediárias: não se cruzam mais, há <strong>duas populações separadas por isolamento reprodutivo</strong> (formaram-se espécies). Alternativa <strong>C</strong>.</p><p>Em D2 as cores se misturam, indicando que voltaram a cruzar; não há nova barreira geográfica em D1 (A).</p>",
  figs(("q101", "Esquema ao longo do tempo: A, uma população; B, duas subpopulações separadas por uma barreira I; C, as subpopulações com cores diferentes; D1, as duas ocupam lado a lado a mesma área com as cores distintas; D2, as cores se misturam numa área contínua.")),
  ["especiação", "isolamento reprodutivo"], enun=p(T(101, 0)) + "[[fig:1]]" + p("A representação indica que, no momento D, na situação"))
X(102, "Química", "Separação de misturas", "<p>Na extração, o óleo bruto é obtido com hexano: um solvente apolar dissolve o óleo, também apolar (“semelhante dissolve semelhante”), e deixa para trás o resto. Essa subetapa depende <strong>apenas da polaridade das substâncias</strong>. Alternativa <strong>D</strong>.</p><p>Trituração, cozimento e prensagem (A, B e C) são processos mecânicos ou térmicos; a destilação (E) separa pela diferença de temperatura de ebulição.</p>",
  tags=["extração por solvente", "polaridade"],
  enun=p(T(102, 0)) + '<table class="tabela"><thead><tr><th>Etapa</th><th>Subetapa</th><th>O que ocorre</th></tr></thead><tbody>'
       '<tr><td rowspan="4">Preparação da matéria-prima</td><td>Seleção dos grãos</td><td>Separação das sujidades mais grossas</td></tr>'
       '<tr><td>Descascamento</td><td>Separação de polpa e casca</td></tr><tr><td>Trituração</td><td>Rompimento dos tecidos e das paredes das células</td></tr>'
       '<tr><td>Cozimento</td><td>Aumento da permeabilidade das membranas celulares</td></tr>'
       '<tr><td rowspan="3">Extração do óleo bruto</td><td>Prensagem</td><td>Remoção parcial do óleo</td></tr>'
       '<tr><td>Extração</td><td>Obtenção do óleo bruto com hexano</td></tr><tr><td>Destilação</td><td>Separação do óleo e do solvente</td></tr></tbody></table>'
       + p(T(102, 3)))
X(103, "Química", "Ácidos e bases", "<p>O texto destaca que o CO<sub>2</sub> é facilmente solubilizado em água. Dissolvido, ele forma ácido carbônico (CO<sub>2</sub> + H<sub>2</sub>O ⇌ H<sub>2</sub>CO<sub>3</sub> ⇌ H<sup>+</sup> + HCO<sub>3</sub><sup>−</sup>), o que aumenta a concentração de H<sup>+</sup>: há <strong>redução do potencial hidrogeniônico (pH) da água</strong>, a acidificação dos oceanos. Alternativa <strong>A</strong>.</p><p>Mais CO<sub>2</sub> não reduz a fotossíntese (C), e o gás não congela nos polos (E).</p>",
  tags=["acidificação dos oceanos"])
X(104, "Biologia", "Fisiologia animal", "<p>As aves aquáticas flutuam e se mantêm secas porque suas penas são cobertas por uma camada oleosa, produzida pela glândula uropigiana. A lavagem com detergente remove o petróleo, mas também essa camada. Antes de voltar à água, elas precisam <strong>refazer a camada de cera impermeabilizante das penas</strong>. Alternativa <strong>E</strong>.</p><p>As penas não precisam ser trocadas (C); a flutuação não depende de músculos ou de massa corporal (A e B).</p>",
  tags=["glândula uropigiana", "derramamento de petróleo"])
X(105, "Física", "Termodinâmica", "<p>O refrigerador retira calor do interior e o libera no ambiente pelo condensador (a grade atrás), onde o gás refrigerante se liquefaz. Se o ambiente em volta estiver quente, o calor sai com mais dificuldade, e o compressor precisa trabalhar mais para liquefazer o refrigerante: <strong>a liquefação da substância refrigerante no condensador exige mais trabalho do compressor</strong>. Alternativa <strong>D</strong>.</p><p>O problema não é o calor entrar no refrigerador (C), mas a dificuldade de o condensador perder calor.</p>",
  tags=["refrigerador", "máquina térmica"])
X(106, "Física", "Hidrostática", "<p>O ar do bolsão está em contato com a água a 50 m de profundidade, então está à pressão dessa profundidade. A variação de pressão em relação à superfície é Δp = ρgh = 1 000 · 10 · 50 = 5 × 10<sup>5</sup> Pa = 500 kPa. No gráfico, 500 kPa corresponde a <strong>60 minutos</strong> de descompressão. Alternativa <strong>C</strong>.</p><p>Usar os 30 m (300 kPa) daria cerca de 40 min (D).</p>",
  figs(("q106", "Esquema de uma caverna submersa: a água com pressão atmosférica de 1,0 × 10⁵ Pa na superfície; dentro da rocha há um bolsão de ar; uma cota de 50 m vai da superfície até o nível da água no bolsão, e uma de 30 m mostra a altura até a rocha."),
       ("q106b", "Gráfico do tempo de descompressão (min) em função da variação de pressão (kPa): cerca de 20 min entre 100 e 200 kPa, 40 min perto de 400 kPa, 60 min perto de 500 kPa, 80 min perto de 600 kPa e 100 min em 700 kPa.")),
  ["pressão hidrostática", "leitura de gráfico"],
  enun=p(T(106, 0)) + "[[fig:1]]" + p(T(106, 2)) + "[[fig:2]]" + p(T(106, 9).replace("10 m s−2", "10 m s<sup>−2</sup>").replace("1 000 kg m−3", "1 000 kg m<sup>−3</sup>")))
SUBS = lambda s: re.sub(r"([MP])(torre|modelo)", r"\1<sub>\2</sub>", s)
X(107, "Física", "Hidrostática", "<p>Com os mesmos materiais e escala 1:100 em cada dimensão, a massa cai com o volume: M<sub>modelo</sub> = M<sub>torre</sub>/100<sup>3</sup>. A área da base cai com o quadrado: A<sub>modelo</sub> = A<sub>torre</sub>/100<sup>2</sup>. Como p = Mg/A, P<sub>torre</sub>/P<sub>modelo</sub> = 100<sup>3</sup>/100<sup>2</sup> = 100 = <strong>10<sup>2</sup></strong>. Alternativa <strong>C</strong>.</p><p>10<sup>6</sup> (E) é só a razão entre as massas; 10<sup>4</sup> (D), entre as áreas.</p>",
  figs(("q107", "Desenho da Torre Eiffel, com sua estrutura de treliças de ferro.")),
  ["pressão", "escala"], enun=p(SUBS(T(107, 0).replace("Eiff el", "Eiffel"))) + "[[fig:1]]" + p(SUBS(T(107, 2)).replace(" ?", "?")),
  alts={k: f"10<sup>{e}</sup>" for k, e in zip("ABCDE", "01246")})
X(108, "Biologia", "Fisiologia humana", "<p>O estômago é muito ácido (pH perto de 2); o intestino tem pH próximo do neutro. Um revestimento que só libera o fármaco em pH neutro passa intacto pelo estômago e se dissolve no intestino. A finalidade é <strong>garantir que o fármaco não seja afetado pelas secreções gástricas</strong>. Alternativa <strong>C</strong>.</p><p>A liberação acontece justamente no intestino (contra A e B), e não depende da amilase salivar (D).</p>",
  tags=["pH do sistema digestório", "cápsulas gastrorresistentes"])
X(109, "Física", "Termologia", "<p>Quando a válvula começa a soltar vapor, a pressão interna já atingiu o valor de trabalho e a temperatura de ebulição se estabiliza. Mais chama não aumenta a temperatura: só faz mais água evaporar e escapar. Reduzir o fogo evita o <strong>consumo de gás desnecessário</strong>. Alternativa <strong>E</strong>.</p><p>A válvula já controla a pressão (A); o cozimento depende da temperatura, que se mantém com fogo baixo.</p>",
  tags=["panela de pressão", "ebulição"])
X(110, "Química", "Cinética química", "<p>Nanomateriais têm partículas minúsculas, e, para a mesma massa, quanto menores as partículas, maior a área exposta. Como as reações com catalisadores sólidos acontecem na superfície, mais área significa mais colisões efetivas e reação mais rápida: o êxito se deve à <strong>maior superfície de contato</strong>. Alternativa <strong>D</strong>.</p><p>O texto diz que se gasta menos energia (contra A e B); catalisadores diminuem, e não elevam, a energia de ativação (E).</p>",
  tags=["superfície de contato", "nanotecnologia"])
X(111, "Física", "Ondas", "<p>Os fones CR captam o ruído constante do ambiente e emitem uma onda sonora igual, mas em oposição de fase. As duas se somam e se anulam: é a <strong>interferência</strong> destrutiva. Por isso funcionam bem com ruídos regulares (turbinas) e mal com sons irregulares (vozes). Alternativa <strong>B</strong>.</p><p>Absorção (A) é o que fazem os fones comuns, com espuma; polarização (C) não ocorre com o som, que é onda longitudinal.</p>",
  tags=["interferência destrutiva", "cancelamento de ruído"])
X(112, "Química", "Equilíbrio químico", "<p>A hidratação do cloreto de cobalto é exotérmica (ΔH &lt; 0) e transforma o sal azul no hidratado rosa. Para voltar ao azul, é preciso deslocar o equilíbrio para a esquerda, no sentido endotérmico: fornecer calor e retirar água. A melhor opção é <strong>aquecer com secador de cabelos</strong>. Alternativa <strong>D</strong>.</p><p>Resfriar (A) e borrifar água (B) deslocariam o equilíbrio para a direita, mantendo o rosa.</p>",
  tags=["princípio de Le Chatelier", "cloreto de cobalto"],
  enun=p(T(112, 0)) + '<p class="centro">\\(\\underset{\\text{(azul)}}{\\mathrm{CoCl_2\\,(s)}} + \\mathrm{6\\,H_2O\\,(g)} \\rightleftharpoons \\underset{\\text{(rosa)}}{\\mathrm{CoCl_2 \\cdot 6\\,H_2O\\,(s)}}\\qquad \\Delta H &lt; 0\\)</p>' + p(T(112, 2)))
X(113, "Física", "Cinemática", "<p>Ao deixar a mesa, a bolinha mantém a velocidade horizontal V<sub>0</sub> (não há força horizontal) e ganha velocidade vertical por causa da gravidade. A combinação de movimento uniforme na horizontal e acelerado na vertical dá uma trajetória <strong>parabólica</strong>, que começa horizontal e vai ficando cada vez mais inclinada. Alternativa <strong>D</strong>.</p><p>A (para e cai) e C (cai na vertical) são as ideias dos desenhos animados; B é uma reta, e E começa caindo para baixo logo na borda.</p>",
  figs(("q113a", "Bolinha com velocidade V₀ sobre a mesa; a trajetória segue reta horizontal além da borda e depois desce em linha vertical até o solo."),
       ("q113b", "Trajetória em linha reta inclinada, da borda da mesa até o solo."),
       ("q113c", "Trajetória vertical, caindo logo ao lado da borda da mesa."),
       ("q113d", "Trajetória em curva parabólica: começa horizontal na borda da mesa e vai se inclinando até o solo, longe da mesa."),
       ("q113e", "Trajetória em curva que começa descendo junto à borda da mesa e vai se abrindo para longe, ficando quase horizontal perto do solo.")),
  ["lançamento horizontal"], enun=p(T(113, 0).replace("(V0)", "(V<sub>0</sub>)")), alts=ALT(1))
X(114, "Física", "Ondas", "<p>Num tubo fechado de comprimento L, as ressonâncias são harmônicos ímpares: f<sub>n</sub> = n · v/(4L). Com L = 30 m e v = 360 m/s, f<sub>1</sub> = 360/120 = 3 Hz, e as ressonâncias consecutivas diferem de 2f<sub>1</sub> = 6 Hz. Se 135 Hz (n = 45) é uma ressonância, a próxima é 135 + 6 = <strong>141 Hz</strong>. Alternativa <strong>C</strong>.</p><p>Somar só f<sub>1</sub> daria 138 Hz (B), mas os harmônicos pares não existem no tubo fechado.</p>",
  tags=["tubo sonoro fechado", "harmônicos"], trocas=[("360 m s-1", "360 m s<sup>−1</sup>")])
X(115, "Biologia", "Biotecnologia", "<p>A soja recebeu um gene de outro organismo (a cianovirina-N vem de uma cianobactéria), que a faz produzir uma proteína que ela não tinha. Inserir no genoma um gene de outra espécie é a <strong>transgenia</strong>, e a planta é um organismo transgênico. Alternativa <strong>B</strong>.</p><p>O melhoramento genético (E) usa cruzamentos dentro da espécie; terapia gênica (D) é tratamento em pessoas.</p>",
  tags=["transgênicos"])
X(116, "Física", "Eletrodinâmica", "<p>Os quatro resistores de 100 Ω dividem os 12 V em partes iguais: 3 V em cada um. Entre B e E há três resistores: <strong>9 V</strong>. O equipamento tem 10 kΩ, muito mais que 300 Ω, então quase não altera o divisor, e a corrente nele é i = 9/10 000 = <strong>0,9 mA</strong>. Alternativa <strong>D</strong>.</p><p>Entre A e E (E) haveria 12 V; 30 mA (A e B) seria a corrente nos resistores, não no equipamento.</p>",
  figs(("q116", "Divisor de tensão: uma fonte CC de 12 V alimenta quatro resistores de 100 Ω em série; há terminais A, B, C, D e E nas extremidades e entre cada par de resistores.")),
  ["divisor de tensão", "lei de Ohm"], enun=p(T(116, 0)) + "[[fig:1]]" + p(T(116, 4), T(116, 5)))
X(117, "Biologia", "Imunologia", "<p>A técnica combina anticorpos, que reconhecem apenas as células do tumor (imunoterapia), com uma molécula ativada por luz infravermelha (foto). O nome adequado é <strong>fotoimunoterapia</strong>. Alternativa <strong>D</strong>.</p><p>Não se usa radiação ionizante (A), cores visíveis (B), quimioterápico (C) nem campo magnético (E).</p>",
  tags=["anticorpos", "câncer"])
X(118, "Biologia", "Zoologia", "<p>O maior desafio da vida fora da água é não perder água. O exoesqueleto de quitina dos artrópodes, coberto de cera, é pouco permeável e reduz a desidratação. O sucesso dos aracnídeos em terra se deve ao <strong>exoesqueleto constituído de quitina que auxilia no controle hídrico corporal</strong>. Alternativa <strong>C</strong>.</p><p>A circulação aberta (D) não impede desidratação, e o ácido úrico economiza água, mas não por estabilizar o pH (B).</p>",
  tags=["artrópodes", "exoesqueleto"], trocas=[("Aracnídeos.", "<em>Aracnídeos</em>."), ("filo Arthropoda", "filo <em>Arthropoda</em>")])
X(119, "Biologia", "Ecologia", "<p>O esgoto traz muita matéria orgânica, e os microrganismos que a decompõem consomem oxigênio. Perto do despejo, a DBO é máxima e o oxigênio dissolvido baixo. No gráfico, o ponto 1 tem a maior DBO (cerca de 12,5 mg/L) e OD baixo (cerca de 4 mg/L). Alternativa <strong>A</strong>.</p><p>O ponto 3 tem o menor OD, mas DBO baixa, típico de trecho de decomposição já avançada, depois do despejo.</p>",
  figs(("q119", "Gráfico de OD (asterisco) e DBO (cruz), em mg/L, nos pontos de amostragem 1 a 5: ponto 1, DBO cerca de 12,5 e OD cerca de 4; ponto 2, DBO cerca de 6,5 e OD cerca de 2,5; ponto 3, DBO cerca de 1,5 e OD cerca de 1; ponto 4, DBO cerca de 4,5 e OD cerca de 3,5; ponto 5, DBO cerca de 4 e OD cerca de 6.")),
  ["DBO", "poluição orgânica"],
  enun=p(T(119, 0)) + "[[fig:1]]" + fonte(T(119, 3).replace("mg L−1", "mg L<sup>−1</sup>")) + p(T(119, 4)) + fonte(T(119, 5)) + p(T(119, 6)))
X(120, "Química", "Estequiometria", "<p>Diferença de emissão: 2,6 − 0,45 = 2,15 mol de CO<sub>2</sub> por km; em 1 000 km, 2 150 mol de CO<sub>2</sub> a menos. Pela equação, 1 mol de etanol gera 2 mol de CO<sub>2</sub>: equivale a 1 075 mol de etanol, ou 1 075 · 46 ≈ 49 450 g ≈ <strong>50 kg</strong>. Alternativa <strong>A</strong>.</p><p>120 kg (E) seria o etanol total do carro a combustão (2,6 · 1 000/2 · 46), sem descontar o elétrico.</p>",
  tags=["estequiometria", "carro elétrico"],
  enun=p(SUB(T(120, 0)).replace("g mol−1", "g mol<sup>−1</sup>")) + '<p class="centro">C<sub>2</sub>H<sub>5</sub>OH (l) + 3 O<sub>2</sub> (g) → 2 CO<sub>2</sub> (g) + 3 H<sub>2</sub>O (g)</p>'
       + p(SUB(T(120, 2))) + fonte(T(120, 3)) + p(T(120, 4)))
X(121, "Biologia", "Fotossíntese", "<p>As bactérias aeróbias se concentram onde há mais oxigênio, isto é, onde a alga faz mais fotossíntese. No esquema, o maior acúmulo de bactérias fica na faixa do <strong>vermelho</strong> (há outro acúmulo menor no azul-violeta), regiões que a clorofila absorve melhor. Alternativa <strong>E</strong>.</p><p>No verde (B) quase não há bactérias: a clorofila reflete essa luz.</p>",
  figs(("q121", "Esquema do experimento de Engelmann: um filamento de alga verde iluminado por um microespectro (vermelho, amarelo, verde, azul, anil e violeta); muitas bactérias aeróbias se acumulam sobre a faixa do vermelho, algumas sobre o azul e o violeta, e quase nenhuma sobre o verde e o amarelo.")),
  ["Engelmann", "espectro de absorção"], enun=p(T(121, 0)) + "[[fig:1]]" + p(T(121, 5)))
IT = lambda s: re.sub(r"(A\. lumbricoides|A\. suum|S\. mansoni|T\. saginata|Ancylostoma)", r"<em>\1</em>", s)
X(122, "Biologia", "Parasitologia", "<p>Só flutuam os ovos menos densos que a solução (1,15 g/mL): <em>Ancylostoma</em> (1,06), <em>A. lumbricoides</em> (1,11) e <em>A. suum</em> (1,13). Os de <em>S. mansoni</em> (1,18) e <em>T. saginata</em> (1,30) afundam. Alternativa <strong>C</strong>.</p><p>As alternativas com <em>S. mansoni</em> ou <em>T. saginata</em> (A, B, D e E) incluem ovos mais densos que a solução.</p>",
  tags=["densidade", "exame de fezes"],
  enun=p(T(122, 0).replace("1,15 g mL−1", "1,15 g mL<sup>−1</sup>")) + tabela(["Parasito", "Densidade (g mL<sup>−1</sup>)"],
       [["<em>Ancylostoma</em>", "1,06"], ["<em>Ascaris lumbricoides</em>", "1,11"], ["<em>Ascaris suum</em>", "1,13"], ["<em>Schistosoma mansoni</em>", "1,18"], ["<em>Taenia saginata</em>", "1,30"]])
       + fonte(T(122, 2)) + p(T(122, 3)), alts={k: IT(v) for k, v in D[122]["alternativas"].items()})
X(123, "Química", "Separação de misturas", "<p>O acetato de etila tem baixa solubilidade em água e densidade diferente (0,9 g/cm<sup>3</sup>): forma com ela uma mistura heterogênea de dois líquidos, com o acetato por cima. A separação mais simples é <strong>decantar a mistura separando os dois componentes em um funil adequado</strong> (funil de separação). Alternativa <strong>E</strong>.</p><p>Filtração (B) separa sólidos de líquidos; evaporar (A) perderia o acetato que se quer recuperar.</p>",
  tags=["funil de separação", "mistura heterogênea"],
  enun=p(T(123, 0), "Considere os dados do acetato de etila:") + LISTA(T(123, 1).split(":", 1)[1].replace("g cm−3", "g cm<sup>−3</sup>")) + p(T(123, 2)))
X(124, "Química", "Química ambiental", "<p>O petróleo é formado por hidrocarbonetos, apolares (hidrofóbicos) e menos densos que a água. Ele não se mistura com ela e forma uma camada na superfície, que bloqueia a luz e as trocas de gases entre o mar e a atmosfera: os componentes <strong>têm caráter hidrofóbico e baixa densidade, impedindo as trocas gasosas</strong>. Alternativa <strong>D</strong>.</p><p>O petróleo não se dissolve na água (C) nem a acidifica (B).</p>",
  tags=["derramamento de petróleo", "densidade"])
X(125, "Biologia", "Genética", "<p>Grupo O: r<sup>2</sup> = 0,25, r = 0,5. A homozigotos: p<sup>2</sup> = 0,16, p = 0,4. Como p + q + r = 1, q = 0,1. Quem é do grupo B pode receber de B e de O: q<sup>2</sup> + 2qr + r<sup>2</sup> = 0,01 + 0,10 + 0,25 = 0,36 = <strong>36%</strong>. Alternativa <strong>D</strong>.</p><p>11% (A) são só os doadores do grupo B; 26% (C) esquece os heterozigotos.</p>",
  tags=["Hardy-Weinberg", "sistema ABO"],
  enun=p(T(125, 0).replace("de IA", "de I<sup>A</sup>").replace("de IB", "de I<sup>B</sup>"))
       + tabela(["Grupo", "Genótipos", "Frequências"], [["A", "I<sup>A</sup>I<sup>A</sup> e I<sup>A</sup>i", "p<sup>2</sup> + 2pr"], ["B", "I<sup>B</sup>I<sup>B</sup> e I<sup>B</sup>i", "q<sup>2</sup> + 2qr"], ["AB", "I<sup>A</sup>I<sup>B</sup>", "2pq"], ["O", "ii", "r<sup>2</sup>"]])
       + p(T(125, 2)))
X(126, "Química", "Radioatividade", "<p>A bomba atômica funciona pela <strong>fissão nuclear do urânio, provocada por nêutrons</strong>: o núcleo de urânio-235 absorve um nêutron, se divide em núcleos menores e libera mais nêutrons e muita energia, numa reação em cadeia. Os fragmentos radioativos formam a poeira radioativa. Alternativa <strong>A</strong>.</p><p>A fusão de hidrogênio (B) é a da bomba de hidrogênio, não a atômica; elétrons e pósitrons não provocam essas reações (C e D).</p>",
  tags=["fissão nuclear", "bomba atômica"])
X(127, "Biologia", "Ecologia", "<p>As plantas pioneiras cobrem rápido o solo exposto, fazem sombra, retêm água, diminuem a evaporação e acrescentam matéria orgânica. Assim criam condições para as espécies seguintes da sucessão. No solo, elas promovem a <strong>estabilização da umidade</strong>. Alternativa <strong>C</strong>.</p><p>A cobertura vegetal diminui a luz que chega ao solo e a temperatura dele (A e D).</p>",
  tags=["sucessão ecológica", "plantas pioneiras"],
  enun=p(T(127, 0)) + fonte(T(127, 1) + " " + T(127, 2).split(" Essas plantas")[0]) + p("Essas plantas" + T(127, 2).split(" Essas plantas")[1]))
X(128, "Física", "Calorimetria", "<p>O aquecedor de 50 W compensa exatamente a perda de calor. Desligado por 1 h, a água perde Q = 50 · 3 600 = 180 000 J. Com 50 L = 50 kg e c = 4 000 J/(kg K): ΔT = Q/(mc) = 180 000/(50 · 4 000) = <strong>0,9 °C</strong>. Alternativa <strong>C</strong>.</p><p>3,6 °C (B) usaria 1 kg/L com 12,5 L; 0,3 °C e 0,6 °C (E e D) vêm de erro nas unidades de tempo.</p>",
  tags=["potência", "calor específico"], trocas=[("utilizamse", "utilizam-se"), ("4,0 kJ kg−1 K−1", "4,0 kJ kg<sup>−1</sup> K<sup>−1</sup>"), ("1 kg L−1", "1 kg L<sup>−1</sup>")])
X(129, "Biologia", "Citologia", "<p>O melhor quimioterápico deve reduzir muito as células tumorais e poupar as normais. O II reduz as tumorais de cerca de 36 milhões (CT) para 15 milhões e mantém as normais em cerca de 28 milhões, acima até do controle (21). Alternativa <strong>B</strong>.</p><p>O III reduz mais o tumor, mas mata muitas células normais (cerca de 8 milhões); o IV aumenta o tumor.</p>",
  figs(("q129", "Gráfico de barras do número de células (milhão): tumorais (barras escuras) CT 36, I 30, II 15, III 10, IV 50, V 36; normais (barras claras) CN 21, I 21, II 28, III 8, IV 35, V 21.")),
  ["quimioterapia", "leitura de gráfico"], enun=p(T(129, 0)) + "[[fig:1]]" + p(T(129, 3)))
X(130, "Física", "Ondas eletromagnéticas", "<p>Herschel descobriu que a temperatura subia mais além do vermelho, numa região sem luz visível: a radiação infravermelha. No aparato, o prisma desvia menos o vermelho e mais o violeta; o recipiente além do vermelho, que recebe o infravermelho, é o <strong>A</strong>. Alternativa <strong>A</strong>.</p><p>O recipiente E, do lado do violeta, recebe menos energia térmica.</p>",
  figs(("q130", "Caixa isolada e opaca: a luz solar entra, atravessa um prisma e se decompõe; o vermelho incide do lado esquerdo e o violeta do lado direito sobre cinco recipientes, A, B, C, D e E; o espectro visível cobre os recipientes do meio, e o A fica além do vermelho.")),
  ["infravermelho", "dispersão da luz"], enun=p(T(130, 0)) + fonte(T(130, 1)) + p(T(130, 2)) + "[[fig:1]]" + p(T(130, 4)))
X(131, "Química", "Química verde", "<p>A Química Verde quer processos rápidos e seletivos, com poucos reagentes, só o produto desejado e sem solventes agressivos. A reação E tem poucos reagentes, um único produto (sem coprodutos) e usa um catalisador de metal não tóxico, que acelera e torna a reação seletiva: <strong>A + ½B → C</strong>. Alternativa <strong>E</strong>.</p><p>B e D formam coprodutos; C usa solvente orgânico; A exige altas pressões, com gasto de energia.</p>",
  tags=["química verde", "catalisador"],
  alts={**D[131]["alternativas"], "E": "A + \\(\\frac{1}{2}\\)B → C (a reação ocorre com o uso de um catalisador contendo um metal não tóxico)."})
X(132, "Química", "Química ambiental", "<p>Entre os resíduos dos fogos estão compostos de chumbo, cromo, bário e antimônio (metais pesados, tóxicos) e gases como NO<sub>2</sub> e SO<sub>2</sub>. O risco ambiental vem de <strong>os produtos da queima conterem metais pesados e gases tóxicos que resultam em poluição atmosférica</strong>. Alternativa <strong>D</strong>.</p><p>Sódio e potássio (C) dão cor, mas não são os mais tóxicos; os resíduos já queimados não são inflamáveis nem explosivos (A e B).</p>",
  tags=["fogos de artifício", "poluição atmosférica"])
X(133, "Física", "Eletrostática", "<p>A carroceria metálica do carro funciona como uma gaiola de Faraday: se o raio a atingir, as cargas se distribuem pela superfície externa do metal e o campo elétrico no interior fica nulo. A proteção vem da <strong>blindagem pela carcaça metálica</strong>. Alternativa <strong>C</strong>.</p><p>Os pneus não isolam uma descarga de milhões de volts (A); por isso o conversível, sem teto metálico, não protege.</p>",
  tags=["gaiola de Faraday", "blindagem eletrostática"])
X(134, "Química", "Densidade", "<p>Pelo esquema, a água sobe de 5 para 7 mL com A (2 mL), para 10 com B (3 mL), para 12 com C (2 mL) e para 16 com D (4 mL). Densidades: A = 26/2 = 13; B = 27/3 = 9; C = 10/2 = 5; D = 36/4 = 9 g/cm<sup>3</sup>. Só <strong>B e D</strong> têm a densidade do cobre. Alternativa <strong>D</strong>.</p><p>Medir o volume de cada moeda pelo nível total, sem subtrair o anterior, levaria a escolher outras.</p>",
  figs(("q134", "Cinco provetas com água: a primeira com 5 mL; a segunda com a moeda A e 7 mL; a terceira com A e B e 10 mL; a quarta com A, B e C e 12 mL; a quinta com A, B, C e D e 16 mL.")),
  ["densidade", "deslocamento de volume"],
  enun=p(T(134, 0).replace("9 g cm−³", "9 g cm<sup>−3</sup>")) + "[[fig:1]]" + p("Com base nos dados obtidos, o investidor adquiriu as moedas"))
X(135, "Biologia", "Genética", "<p>Pela análise do Treineiros: para dois parentais diploides (2n = 22) gerarem um descendente com 44 cromossomos, cada um deveria contribuir com um gameta não reduzido (2n), o que exige erro nos dois. A explicação mais próxima é a D, mas ela fala em “meiose gamética”, e nas plantas a meiose é espórica; a A daria um triploide. Por isso nenhuma alternativa está plenamente correta. A mais próxima seria a D. Alternativa <strong>D</strong>, se a questão não tivesse sido anulada.</p>",
  tags=["poliploidia", "alopoliploidia"],
  anulacao={"fonte": "analise", "motivo": "O Inep anulou a questão sem divulgar o motivo. Pela análise, nenhuma alternativa descreve corretamente a origem do café arábica: a que aponta erro nos dois parentais (D) fala em “meiose gamética”, que não ocorre em plantas (a meiose é espórica), e a duplicação em um só parental (A) geraria um triploide."},
  trocas=[("são Coffea canephora e Coffea arabica", "são <em>Coffea canephora</em> e <em>Coffea arabica</em>"), ("entre C. canephora e C. eugenioides", "entre <em>C. canephora</em> e <em>C. eugenioides</em>"), ("cromossomos de C. arabica", "cromossomos de <em>C. arabica</em>"), ("espécie C. arabica", "espécie <em>C. arabica</em>")],
  alts={**D[135]["alternativas"], "E": D[135]["alternativas"]["E"].replace("C. arabica", "<em>C. arabica</em>")})

completar(Q, R)
