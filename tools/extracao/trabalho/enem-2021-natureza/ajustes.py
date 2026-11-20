# Enem 2021, 2º dia, caderno azul: Ciências da Natureza (questões 91 a 135 do caderno; no site, 1 a 45, com numeroOriginal).
# Texto do PDF embaralhado: rascunho feito com DECOD=1 (tools/enem_decod.py). Símbolos em fonte Symbol/CambriaMath
# não decodificam: fórmulas das Q94, 101, 105, 115, 131 e 133 escritas à mão.
# Quadros das Q91, 96, 107, 108, 109, 119, 124, 130, 133 e 134 em tabela HTML. Sextilha de cordel (Q108) como imagem.
# Alternativas-imagem nas Q102, 105, 126 e 135. Sem anuladas nesta área.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, paragrafos_enem

ID = "enem-2021-natureza"
META = {"id": ID, "banca": "Enem", "ano": 2021, "titulo": "Enem 2021: Ciências da Natureza", "fonte": "Inep", "dataExame": "2021-11-28",
        "duracaoMinutos": 150, "area": "Ciências da Natureza", "caderno": "azul", "dia": 2}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2021-dia2-azul")
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


def X(n, materia, assunto, expl, imagens=(), tags=(), enun=None, trocas=(), alts=None):
    e = LIMPA(enun or E(n))
    for a, b in trocas:
        assert a in e, a; e = e.replace(a, b)
    Q[n - 90] = {"materia": materia, "assunto": assunto, "area": "Ciências da Natureza", "tags": list(tags), "numeroOriginal": n,
                 "enunciado": e, "alternativas": {k: LIMPA(v) for k, v in dict(alts or D[n]["alternativas"]).items()},
                 "imagens": list(imagens), "explicacao": expl}


X(91, "Química", "Funções inorgânicas", "<p>A solução preparada tem pH 4,3, mais ácida que a faixa ideal (5,5 a 6,5). Para corrigir, é preciso adicionar uma base. Entre as opções, a única base é o <strong>hidróxido de potássio, KOH</strong>, que ainda fornece K<sup>+</sup>, um macronutriente que já está abaixo do valor de referência (3,5 contra 6,0 mmol/L). Alternativa <strong>E</strong>.</p><p>O ácido fosfórico (A) baixaria ainda mais o pH; CaSO<sub>4</sub> (B) é um sal neutro; Al<sub>2</sub>O<sub>3</sub> (C) é insolúvel e o alumínio é nocivo às plantas; FeCl<sub>2</sub> (D) tem caráter ácido.</p>",
  tags=["pH", "neutralização", "hidroponia"],
  enun=p(T(91, 0)) + '<table class="tabela"><thead><tr><th colspan="2" rowspan="2">Espécies químicas</th><th colspan="2">Concentração, mmol/L</th></tr>'
       '<tr><th>Composição de referência (5,5 &lt; pH &lt; 6,5)</th><th>Solução nutritiva preparada (pH = 4,3)</th></tr></thead><tbody>'
       '<tr><td rowspan="5">Macronutrientes</td><td>N (NH<sub>4</sub><sup>+</sup>)</td><td>1,0</td><td>0,8</td></tr>'
       '<tr><td>P (H<sub>2</sub>PO<sub>4</sub><sup>−</sup>)</td><td>1,0</td><td>1,0</td></tr>'
       '<tr><td>K<sup>+</sup></td><td>6,0</td><td>3,5</td></tr><tr><td>Ca<sup>2+</sup></td><td>4,0</td><td>3,0</td></tr>'
       '<tr><td>SO<sub>4</sub><sup>2−</sup></td><td>2,0</td><td>1,0</td></tr>'
       '<tr><td rowspan="2">Micronutrientes</td><td>Fe<sup>2+</sup></td><td>90 × 10<sup>−3</sup></td><td>70 × 10<sup>−3</sup></td></tr>'
       '<tr><td>Cl<sup>−</sup></td><td>-</td><td>4,5 × 10<sup>−3</sup></td></tr></tbody></table>' + fonte(T(91, 2)) + p(T(91, 3)),
  alts={"A": "ácido fosfórico, H<sub>3</sub>PO<sub>4</sub>.", "B": "sulfato de cálcio, CaSO<sub>4</sub>.", "C": "óxido de alumínio, Al<sub>2</sub>O<sub>3</sub>.",
        "D": "cloreto de ferro(II), FeCl<sub>2</sub>.", "E": "hidróxido de potássio, KOH."})
X(92, "Física", "Ondas", "<p>As barras são do mesmo material, então o som se propaga nelas com a mesma velocidade: v<sub>1</sub> = v<sub>2</sub>. Na frequência fundamental, o comprimento de onda é proporcional ao comprimento da barra, e f = v/λ. A barra menor tem λ menor e, portanto, frequência maior: <strong>f<sub>1</sub> &gt; f<sub>2</sub> e v<sub>1</sub> = v<sub>2</sub></strong>. Alternativa <strong>D</strong>.</p><p>A velocidade depende do meio, não do tamanho da barra; por isso as opções com v<sub>1</sub> ≠ v<sub>2</sub> (A, C e E) estão erradas, e B inverte a relação das frequências.</p>",
  figs(("q92", "Foto de um sino dos ventos com várias barras metálicas penduradas; setas indicam o comprimento 1, de uma barra curta, e o comprimento 2, de uma barra longa.")),
  ["frequência fundamental", "velocidade do som"],
  enun=p(T(92, 0)) + "[[fig:1]]" + p(T(92, 3)).replace("f1", "f<sub>1</sub>").replace("v1", "v<sub>1</sub>").replace("f2", "f<sub>2</sub>").replace("v2", "v<sub>2</sub>"),
  alts={"A": "f<sub>1</sub> &lt; f<sub>2</sub> e v<sub>1</sub> &lt; v<sub>2</sub>.", "B": "f<sub>1</sub> &lt; f<sub>2</sub> e v<sub>1</sub> = v<sub>2</sub>.", "C": "f<sub>1</sub> &lt; f<sub>2</sub> e v<sub>1</sub> &gt; v<sub>2</sub>.", "D": "f<sub>1</sub> &gt; f<sub>2</sub> e v<sub>1</sub> = v<sub>2</sub>.", "E": "f<sub>1</sub> &gt; f<sub>2</sub> e v<sub>1</sub> &gt; v<sub>2</sub>."})
X(93, "Biologia", "Evolução", "<p>A capacidade de imitar animais perigosos ou pouco atrativos protege o polvo de predadores. Os indivíduos que tinham esse comportamento sobreviviam e se reproduziam mais, e a característica se espalhou por seleção natural: os polvos <strong>sobreviveram às pressões seletivas com esses comportamentos</strong>. Alternativa <strong>E</strong>.</p><p>Não há ancestral comum próximo com peixes e serpentes (A), as mutações não são dirigidas (B), a observação não cria característica hereditária (C) e convergência adaptativa (D) se refere a estruturas parecidas surgidas de forma independente, não a imitação de comportamento.</p>",
  figs(("q93", "Seis fotos numeradas: 1, polvo achatado sobre a areia; 2, peixe-linguado; 3, polvo com tentáculos listrados abertos; 4, peixe-leão; 5, polvo com dois tentáculos estendidos como uma cobra; 6, serpente-marinha listrada.")),
  ["mimetismo", "seleção natural"], enun=p(T(93, 0)) + "[[fig:1]]" + fonte(T(93, 2)) + p(T(93, 3)))
X(94, "Física", "Cinemática", "<p>O canhão B dispara a 53°, com v<sub>x</sub> = 0,6 v e v<sub>y</sub> = 0,8 v. Para atingir A, a bala percorre 120 m na horizontal e sobe 35 m. Tempo: t = 120/(0,6 v) = 200/v. Na vertical: 35 = 0,8 v · (200/v) − 5 · (200/v)<sup>2</sup> = 160 − 200 000/v<sup>2</sup>. Então 200 000/v<sup>2</sup> = 125 e v<sup>2</sup> = 1 600: <strong>v = 40 m/s</strong>. Alternativa <strong>C</strong>.</p><p>Como a bala anterior, com o mesmo ângulo, passou tangenciando P, o obstáculo não impede essa trajetória.</p>",
  figs(("q94", "Cenário do jogo: o canhão A está à esquerda, no alto de um planalto de 35 m de altura; o canhão B, embaixo à direita, a 120 m na horizontal de A, aponta para cima com ângulo θ e velocidade v₀. Perto da borda do planalto há uma elevação com o ponto P, 10 m acima do planalto. A gravidade aponta para baixo.")),
  ["lançamento oblíquo"],
  enun=p("A figura foi extraída de um antigo jogo para computadores, chamado <em>Bang! Bang!</em>") + "[[fig:1]]"
       + p("No jogo, dois competidores controlam os canhões <strong>A</strong> e <strong>B</strong>, disparando balas alternadamente com o objetivo de atingir o canhão do adversário; para isso, atribuem valores estimados para o módulo da velocidade inicial de disparo \\(\\left(|\\vec{v}_0|\\right)\\) e para o ângulo de disparo (θ).",
           "Em determinado momento de uma partida, o competidor <strong>B</strong> deve disparar; ele sabe que a bala disparada anteriormente, θ = 53°, passou tangenciando o ponto <strong><em>P</em></strong>.",
           "No jogo, \\(|\\vec{g}|\\) é igual a 10 m/s<sup>2</sup>. Considere sen 53° = 0,8, cos 53° = 0,6 e desprezível a ação de forças dissipativas.")
       + fonte(T(94, 5)) + p("Com base nas distâncias dadas e mantendo o último ângulo de disparo, qual deveria ser, aproximadamente, o menor valor de \\(|\\vec{v}_0|\\) que permitiria ao disparo efetuado pelo canhão <strong>B</strong> atingir o canhão <strong>A</strong>?"))
X(95, "Química", "Radioatividade", "<p>Em 35 anos cabem 35/5 = 7 meias-vidas. A cada meia-vida a massa cai à metade: 500 → 250 → 125 → 62,5 → 31,25 → 15,6 → 7,8 → <strong>3,9 g</strong>, ou seja, 500/2<sup>7</sup> = 500/128 ≈ 3,9 g. Alternativa <strong>A</strong>.</p><p>31,2 g (B) corresponde a só 4 meias-vidas, e 62,5 g (C) a 3.</p>",
  tags=["meia-vida", "decaimento"])
X(96, "Biologia", "Genética", "<p>Trocar C por U no códon 4 transforma CAA em <strong>UAA</strong>, que é códon de parada. A tradução para logo no quarto códon e a proteína fica com só 3 aminoácidos, a menor de todas. Alternativa <strong>B</strong>.</p><p>Na E, sem os dois primeiros nucleotídeos do códon 5, a leitura vira AUG UUU GUU CAA <strong>UAG</strong>: a parada vem no quinto códon (4 aminoácidos). A deleção de G (A) e as trocas em C e D não criam parada antes.</p>",
  tags=["código genético", "mutação", "códon de parada"],
  enun=p(T(96, 0)) + tabela(["1", "2", "3", "4", "5", "6", "7"], [["AUG", "UUU", "GUU", "CAA", "UGU", "AGU", "UAG"]]) + p(T(96, 2)))
X(97, "Química", "Química orgânica", "<p>O óleo vegetal é formado por triglicerídeos (ésteres de ácidos graxos com glicerol). Aquecido com soda cáustica (NaOH), ele sofre hidrólise básica e forma glicerol e sais de ácidos graxos, que são o sabão. Essa reação se chama <strong>saponificação</strong>. Alternativa <strong>E</strong>.</p><p>A esterificação (D) é a reação inversa, de formação de ésteres; redução, epoxidação e substituição não produzem sabão.</p>",
  tags=["saponificação", "óleo de cozinha"])
X(98, "Biologia", "Fisiologia animal", "<p>No feto, o pulmão não funciona: o oxigênio vem da placenta. O forame oval desvia o sangue do átrio direito para o esquerdo, sem passar pelo pulmão, e o sangue segue pelo corpo numa passagem única pelo coração, como na circulação simples dos <strong>peixes</strong>. Alternativa <strong>D</strong>.</p><p>Nas aves (A) há separação completa e as duas circulações; nos répteis e anfíbios (B e E) a mistura existe, mas a comparação correta para a circulação fetal sem pequena circulação é a dos peixes.</p>",
  tags=["circulação fetal", "forame oval"])
X(99, "Física", "Termologia", "<p>Entre o Sol e a ilha de calor não há meio material: a energia chega por ondas eletromagnéticas, a <strong>irradiação</strong>. Entre a ilha de calor e a brisa, o texto descreve um “fluxo de ar vertical” que leva a energia térmica para cima: é a <strong>convecção</strong>, transporte de calor pelo movimento do próprio fluido. Alternativa <strong>A</strong>.</p><p>Condução (C) exigiria contato entre corpos sem movimento de matéria, e a convecção não pode ocorrer no vácuo entre o Sol e a Terra (D e E).</p>",
  figs(("q99", "Esquema com três subsistemas: o Sol no alto à esquerda, linhas curvas representando a brisa marítima à direita e prédios representando a ilha de calor embaixo.")),
  ["irradiação", "convecção", "ilha de calor"],
  enun=p(T(99, 0)) + "[[fig:1]]" + ap(T(99, 6)) + fonte(T(99, 7)) + p(T(99, 8)))
X(100, "Física", "Dinâmica", "<p>A pedra cai antes da rolha, e a folha amassada cai antes da esticada, embora tenha a mesma massa. O que muda nos dois casos é a forma e a área exposta ao ar: a <strong>resistência do ar</strong> é o fator comum. Sem ar, todos cairiam com a mesma aceleração. Alternativa <strong>B</strong>.</p><p>Peso e massa (A e C) não mudam ao amassar o papel, e a aceleração da gravidade (E) é a mesma para todos.</p>",
  tags=["queda livre", "resistência do ar"],
  enun=p(T(100, 0), T(100, 1)) + ap(T(100, 2) + " " + T(100, 3), T(100, 4)) + fonte(T(100, 5)) + p(T(100, 6)))
X(101, "Química", "Estequiometria", "<p>Pelo texto, 100 g de glicose rendem cerca de 50 g de etanol; então 50 kg rendem 25 kg em conversão total. Com 80% de conversão: 0,8 × 25 = 20 kg = 20 000 g de etanol. Volume: V = m/d = 20 000/0,80 = 25 000 mL = <strong>25 L</strong>. Alternativa <strong>C</strong>.</p><p>20 (B) é a massa em kg, sem dividir pela densidade; 16 (A) aplicaria duas vezes o fator 0,8.</p>",
  tags=["rendimento", "fermentação"],
  enun=p(T(101, 0).replace("C6H12O6", "C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>"))
       + '<p class="centro">Fermentação alcoólica: \\(\\mathrm{C_6H_{12}O_6 \\longrightarrow 2\\,CH_3CH_2OH + 2\\,CO_2}\\)</p>' + p(T(101, 2), T(101, 3)))
X(102, "Física", "Eletrodinâmica", "<p>A montagem tem duas pilhas de cobre e zinco ligadas em série (somando as tensões, o voltímetro marca 2,20 V). O cronômetro é a carga, que no esquema aparece como resistor, e o voltímetro está ligado em paralelo com ele. O circuito com <strong>duas pilhas em série, no mesmo sentido, alimentando um resistor com o voltímetro em paralelo</strong>. Alternativa <strong>B</strong>.</p><p>Em C as pilhas estão em oposição (as tensões se anulariam); em A há uma pilha só e o voltímetro em série; D e E têm resistores ou pilhas a mais.</p>",
  figs(("q102", "Montagem: dois pares de béqueres, cada par com uma placa de cobre em solução de CuSO₄ e uma placa de zinco em solução de ZnSO₄, ligados por papel umedecido com Na₂SO₄. Os fios ligam os dois pares em série a um cronômetro digital e a um voltímetro, que marca 2,20 V."),
       ("q102a", "Circuito com uma pilha, um resistor e um voltímetro, todos em série."),
       ("q102b", "Circuito com duas pilhas em série no mesmo sentido, alimentando um resistor, com um voltímetro ligado em paralelo ao resistor."),
       ("q102c", "Circuito com duas pilhas em série, mas em sentidos opostos, alimentando um resistor, com um voltímetro em paralelo ao resistor."),
       ("q102d", "Circuito com uma pilha entre quatro resistores em série, um resistor e um voltímetro em paralelo."),
       ("q102e", "Circuito com quatro pilhas em série, um resistor e um voltímetro em série.")),
  ["pilhas", "circuito elétrico", "voltímetro"],
  enun=p(T(102, 0)) + "[[fig:1]]" + p(T(102, 2)), alts=ALT(2))
X(103, "Química", "Funções orgânicas", "<p>O ácido acetilsalicílico tem um grupo carboxila (—COOH), que reage com NaOH numa neutralização. A <strong>titulação com NaOH</strong> (teste 5) mede quanto ácido há em cada comprimido, e foi ela que mostrou só 40% do esperado. Alternativa <strong>E</strong>.</p><p>Massa e densidade (1 e 2) não distinguem o princípio ativo dos componentes inertes; o papel indicador (3) só diz se o meio é ácido, sem medir a quantidade; a temperatura de fusão (4) indica pureza, mas não quantifica.</p>",
  figs(("q103", "Fórmula estrutural do ácido acetilsalicílico: anel benzênico com um grupo carboxila (COOH) e, na posição vizinha, um grupo éster (O—CO—CH₃).")),
  ["titulação", "ácido acetilsalicílico"],
  enun=p(T(103, 0)) + OL("obtenção da massa do comprimido;", "medição da densidade do comprimido;", "verificação do pH com papel indicador;",
                         "determinação da temperatura de fusão do comprimido;", "titulação com solução aquosa de NaOH.")
       + p("Após a realização dos testes, o lote do medicamento foi reprovado porque a quantidade de ácido acetilsalicílico por comprimido foi de apenas 40% da esperada.")
       + "[[fig:1]]" + p(T(103, 7)))
X(104, "Biologia", "Ecologia", "<p>Os compostos tóxicos (metais pesados dos rejeitos) não são degradados nem eliminados com facilidade: acumulam-se nos tecidos e passam de um nível trófico para o seguinte, aumentando a concentração a cada nível. É a magnificação trófica. Entre os citados, quem está no topo da cadeia são os <strong>golfinhos</strong>. Alternativa <strong>B</strong>.</p><p>Fitoplâncton e algas (C e E) são produtores; esponjas e peixes herbívoros (A e D) estão em níveis mais baixos.</p>",
  tags=["magnificação trófica", "Mariana"])
X(105, "Física", "Eletromagnetismo", "<p>Visto de cima, as cargas se movem para dentro da página (sentido de \\(\\vec{g}\\)) e o campo \\(\\vec{B}\\) aponta para a direita. Pela regra da mão direita, \\(\\vec{F} = q\\,\\vec{v} \\times \\vec{B}\\): para a carga positiva, a força aponta para baixo na figura; para a negativa, o sentido se inverte e a força aponta para cima. Forças opostas, perpendiculares à haste: <strong>+ para baixo e − para cima</strong>. Alternativa <strong>A</strong>.</p><p>B e D dariam forças iguais nas duas cargas, o que ignora o sinal; E inverte os sentidos; C põe as forças ao longo da haste, paralelas a \\(\\vec{B}\\), o que é impossível.</p>",
  figs(("q105", "Vista de cima: linhas de campo magnético horizontais apontando para a direita (B) e o haltere, com a esfera positiva à esquerda e a negativa à direita. Ao lado, o símbolo ⊗ indica que a gravidade aponta para dentro da página."),
       ("q105a", "Haltere com uma seta para baixo na carga positiva e uma seta para cima na carga negativa."),
       ("q105b", "Haltere com setas para baixo nas duas cargas."),
       ("q105c", "Haltere com setas ao longo da haste, das duas cargas apontando para o centro."),
       ("q105d", "Haltere com setas para cima nas duas cargas."),
       ("q105e", "Haltere com uma seta para cima na carga positiva e uma seta para baixo na carga negativa.")),
  ["força magnética", "regra da mão direita"],
  enun=p("Duas esferas carregadas com cargas iguais em módulo e sinais contrários estão ligadas por uma haste rígida isolante na forma de haltere. O sistema se movimenta sob ação da gravidade numa região que tem um campo magnético horizontal uniforme \\((\\vec{B})\\), da esquerda para a direita. A imagem apresenta o sistema visto de cima para baixo, no mesmo sentido da aceleração da gravidade \\((\\vec{g})\\) que atua na região.")
       + "[[fig:1]]" + p(T(105, 4)), alts=ALT(2))
X(106, "Química", "Isomeria", "<p>Na figura, a lumirrubina tem a mesma fórmula molecular da bilirrubina, mas um dos anéis da ponta se fechou num ciclo maior, ligado a outra parte da molécula: muda o esqueleto de carbonos, não a função nem só a posição de um grupo. É um <strong>isômero de cadeia</strong>. Alternativa <strong>C</strong>.</p><p>Não há carbono quiral criado (A), as funções orgânicas são as mesmas (B), e não se trata apenas de mudar a posição de um grupo (D) ou a disposição em torno de uma dupla ligação (E).</p>",
  figs(("q106", "Esquema da fototerapia: a radiação de 400 a 500 nm atinge a bilirrubina, que não é suficientemente excretada pelo recém-nascido (hiperbilirrubinemia), e a converte em lumirrubina, forma isomérica com um anel a mais, que é excretada pela bile e pela urina.")),
  ["isomeria plana", "fototerapia"],
  enun=p(T(106, 0)) + fonte(T(106, 1)) + "[[fig:1]]" + fonte(T(106, 3)) + p(T(106, 4)))
X(107, "Física", "Energia", "<p>As duas versões vão de 0 a 100 km/h: ganham a mesma energia cinética (mesmo carro, mesma variação de velocidade). Potência é energia dividida pelo tempo. A versão a álcool faz isso em 12,9 s, menos que os 13,4 s da gasolina, então tem a <strong>maior taxa de variação de energia cinética</strong> e a maior potência. Alternativa <strong>C</strong>.</p><p>A velocidade máxima maior (B) não indica potência no trecho considerado, e quem demora mais (E) tem potência menor, não maior.</p>",
  tags=["potência", "energia cinética"],
  enun=p(T(107, 0)) + tabela(["Parâmetro", "Motor a gasolina", "Motor a álcool"],
                             [["Aceleração", "de 0 a 100 km/h em 13,4 s", "de 0 a 100 km/h em 12,9 s"], ["Velocidade máxima", "165 km/h", "163 km/h"]]) + p(T(107, 2)))
X(108, "Física", "Gravitação", "<p>A sextilha dá duas pistas: o planeta é “menos denso que a água” e está a uma distância da Terra pouco menor que a do Sol. Na tabela, o único planeta com densidade relativa menor que 1 é <strong>Saturno</strong> (0,7). Sua distância ao Sol é 9,6 u.a.; quando está do mesmo lado que a Terra, fica a cerca de 8,6 u.a. de nós. Alternativa <strong>D</strong>.</p><p>Júpiter (1,3), Urano (1,2) e Netuno (1,7) têm densidade maior que a da água, e Mercúrio é rochoso (5,6).</p>",
  figs(("q108verso", "Sextilha de cordel em seis versos, como aparece na prova: descreve um astro que está distante da Terra quase tanto quanto o Sol e que é menos denso que a água.")),
  ["densidade", "sistema solar"],
  enun='<p class="apoio"><strong>TEXTO I</strong></p>' + ap("No cordel intitulado <em>Senhor dos Anéis</em>, de autoria de Gonçalo Ferreira da Silva, lê-se a sextilha:") + "[[fig:1]]" + fonte(T(108, 3))
       + '<p class="apoio"><strong>TEXTO II</strong></p>' + ap("Distâncias médias dos planetas ao Sol e suas densidades médias")
       + tabela(["Planetas", "Distância média ao Sol (u.a.)", "Densidade relativa média"],
                [["*Mercúrio", "0,39", "5,6"], ["*Vênus", "0,72", "5,2"], ["*Terra", "1,0", "5,5"], ["*Marte", "1,5", "4,0"], ["**Ceres", "2,8", "2,1"],
                 ["*Júpiter", "5,2", "1,3"], ["*Saturno", "9,6", "0,7"], ["*Urano", "19", "1,2"], ["*Netuno", "30", "1,7"], ["**Plutão", "40", "2,0"], ["**Éris", "68", "2,5"]])
       + fonte("u.a. = 149 600 000 km, é a unidade astronômica, *Planeta clássico, **Planeta-anão") + fonte("Características dos planetas. Disponível em: www.astronoo.com. Acesso em: 8 nov. 2019 (adaptado).")
       + p(T(108, 7)))
SUB = lambda s: re.sub(r"R(\d)", r"R<sub>\1</sub>", s)
X(109, "Física", "Eletrodinâmica", "<p>Pela segunda lei de Ohm, R = ρL/A, e ρ é a mesma para todos. Basta comparar L/A: fio 1: 312/9 ≈ 34,7; fio 2: 47/4 ≈ 11,8; fio 3: 54/2 = 27; fio 4: 106/1 = 106. Em ordem crescente: <strong>R<sub>2</sub> &lt; R<sub>3</sub> &lt; R<sub>1</sub> &lt; R<sub>4</sub></strong>. Alternativa <strong>C</strong>.</p><p>Ordenar só pelo comprimento daria R<sub>2</sub> &lt; R<sub>3</sub> &lt; R<sub>4</sub> &lt; R<sub>1</sub>, e só pela área, a ordem da alternativa A.</p>",
  tags=["segunda lei de Ohm", "resistividade"],
  enun=p(T(109, 0)) + tabela(["", "Área", "Comprimento", "Resistência elétrica"],
                             [["<strong>Fio 1</strong>", "9", "312", "R<sub>1</sub>"], ["<strong>Fio 2</strong>", "4", "47", "R<sub>2</sub>"],
                              ["<strong>Fio 3</strong>", "2", "54", "R<sub>3</sub>"], ["<strong>Fio 4</strong>", "1", "106", "R<sub>4</sub>"]])
       + fonte(T(109, 2)) + p(T(109, 3)),
  alts={k: SUB(v).replace(" < ", " &lt; ") for k, v in D[109]["alternativas"].items()})
X(110, "Biologia", "Metabolismo energético", "<p>O texto fala de compostos orgânicos “catabolizados com menor rendimento energético”, gerando subprodutos que servem de combustível. É a <strong>fermentação</strong>: a degradação incompleta da glicose, sem oxigênio, produz etanol (álcool) ou metano (na fermentação metanogênica), usados como combustíveis. Alternativa <strong>B</strong>.</p><p>Fotossíntese e quimiossíntese (A e C) fixam carbono; respiração aeróbica e fosforilação oxidativa (D e E) rendem muita energia e liberam só CO<sub>2</sub> e água.</p>",
  tags=["fermentação", "biocombustíveis"])
X(111, "Biologia", "Ecologia", "<p>O plano já cuida da sensibilização, da capacitação da limpeza e da separação dentro da escola. Falta o destino: se ninguém recolher os recicláveis, eles acabam no lixo comum. É preciso <strong>firmar parceria com a prefeitura ou cooperativa de catadores para o recolhimento e a destinação apropriada</strong>. Alternativa <strong>B</strong>.</p><p>Campanhas nos bairros, visitas ao lixão, divulgação e coletores fora da escola (A, C, D e E) vão além do ambiente escolar e não resolvem o destino do material.</p>",
  tags=["coleta seletiva", "reciclagem"],
  enun=p("Uma escola iniciou o processo educativo para implantação da coleta seletiva e destino de materiais recicláveis. Para atingir seus objetivos, a instituição planejou:")
       + OL("sensibilizar a comunidade escolar, desenvolvendo atividades em sala e extraclasse de maneira contínua;",
            "capacitar o pessoal responsável pela limpeza da escola quanto aos novos procedimentos adotados com a coleta seletiva; e",
            "distribuir coletores de materiais recicláveis específicos nas salas, pátio e outros ambientes para acondicionamento dos resíduos.")
       + p("Para completar a ação proposta no ambiente escolar, o que falta ser inserido no planejamento?"))
X(112, "Biologia", "Biotecnologia", "<p>A consanguinidade aumenta a chance de um filhote herdar duas cópias de alelos recessivos causadores de doença, como o do albinismo. Para separar os animais de forma adequada, é preciso saber quem carrega esses alelos: o <strong>mapeamento genético</strong> identifica os portadores e o grau de parentesco. Alternativa <strong>E</strong>.</p><p>Transgenia, terapia gênica, vacina de DNA e clonagem terapêutica (A a D) não servem para orientar os cruzamentos.</p>",
  tags=["consanguinidade", "mapeamento genético"])
X(113, "Química", "Oxirredução", "<p>Seguindo o ciclo: em I o Cu é oxidado a Cu<sup>2+</sup> pelo HNO<sub>3</sub>; II, III e IV são precipitação, decomposição e reação com ácido, sem mudar o Nox do cobre (+2). Na etapa V, o zinco, mais reativo, reduz o Cu<sup>2+</sup> do CuSO<sub>4</sub> a cobre metálico (Nox 0). A redução do cobre ocorre na <strong>etapa V</strong>. Alternativa <strong>E</strong>.</p><p>Na etapa I ocorre o contrário, a oxidação do cobre.</p>",
  figs(("q113", "Ciclo do cobre: Cu reage com HNO₃ (I) e forma Cu(NO₃)₂; com NaOH (II) forma Cu(OH)₂; por aquecimento (III) forma CuO; com H₂SO₄ (IV) forma CuSO₄; com Zn e HCl (V) volta a Cu.")),
  ["número de oxidação", "ciclo do cobre"], enun=p(T(113, 0)) + "[[fig:1]]" + p(T(113, 6)))
X(114, "Biologia", "Sistema nervoso", "<p>O reflexo patelar é um arco reflexo simples: o neurônio sensorial leva o estímulo à <strong>medula espinal</strong>, onde faz sinapse direto com o neurônio motor, que contrai o músculo da coxa e levanta a perna, sem passar pelo encéfalo. Alternativa <strong>B</strong>.</p><p>Ponte, cerebelo, hipotálamo e neuro-hipófise (A, C, D e E) ficam no encéfalo e não coordenam esse reflexo.</p>",
  tags=["arco reflexo", "medula espinal"])
X(115, "Física", "Termologia", "<p>Com a mesma área, espessura total d e diferença de temperatura, a taxa de calor é proporcional à condutividade efetiva. Alumínio: k = 20; ferro: k = 8. Na panela composta, d<sub>1</sub> = d<sub>2</sub> = d/2: d/k<sub>ef</sub> = (d/2)/40 + (d/2)/5, logo k<sub>ef</sub> = 1/(1/80 + 1/10) = 80/9 ≈ 8,9 W/m K. A mais econômica é a que conduz mais: <strong>alumínio (20), cobre-aço (8,9) e ferro (8)</strong>. Alternativa <strong>B</strong>.</p><p>Tomar a média das condutividades (22,5) colocaria o cobre-aço em primeiro (A), mas em série vale a soma das “resistências térmicas”, dominada pelo aço.</p>",
  tags=["condução térmica", "condutividade"],
  enun=p("Na montagem de uma cozinha para um restaurante, a escolha do material correto para as panelas é importante, pois a panela que conduz mais calor é capaz de cozinhar os alimentos mais rapidamente e, com isso, há economia de gás. A taxa de condução do calor depende da condutividade <em>k</em> do material, de sua área <em>A</em>, da diferença de temperatura Δ<em>T</em> e da espessura <em>d</em> do material, sendo dada pela relação \\(\\dfrac{\\Delta Q}{\\Delta t} = k\\,A\\,\\dfrac{\\Delta T}{d}\\). Em panelas com dois materiais, a taxa de condução é dada por \\(\\dfrac{\\Delta Q}{\\Delta t} = A\\,\\dfrac{\\Delta T}{\\dfrac{d_1}{k_1} + \\dfrac{d_2}{k_2}}\\), em que <em>d</em><sub>1</sub> e <em>d</em><sub>2</sub> são as espessuras dos dois materiais, e <em>k</em><sub>1</sub> e <em>k</em><sub>2</sub> são as condutividades de cada material. Os materiais mais comuns no mercado para panelas são o alumínio (<em>k</em> = 20 W/m K), o ferro (<em>k</em> = 8 W/m K) e o aço (<em>k</em> = 5 W/m K) combinado com o cobre (<em>k</em> = 40 W/m K).",
         "Compara-se uma panela de ferro, uma de alumínio e uma composta de \\(\\frac{1}{2}\\) da espessura em cobre e \\(\\frac{1}{2}\\) da espessura em aço, todas com a mesma espessura total e com a mesma área de fundo.",
         "A ordem crescente da mais econômica para a menos econômica é"))
X(116, "Química", "Ácidos e bases", "<p>Para reagir com NaOH numa reação ácido-base de Brönsted-Lowry, o pesticida precisa doar um próton (H<sup>+</sup>). O composto III tem dois grupos <strong>fenol</strong> (OH ligado ao anel aromático), cujo hidrogênio é ácido o bastante para ser retirado pela base. Os demais não têm hidrogênio ácido desse tipo. O teste positivo é com o <strong>III</strong>. Alternativa <strong>C</strong>.</p><p>I tem amida (N—H muito pouco ácido), II tem N—H em anel e grupo nitro, IV é sulfona e V é éter e silano.</p>",
  figs(("q116", "Fórmulas estruturais de cinco pesticidas: I, uma ureia com anel diclorofenil (N—H e N,N-dimetil); II, anel de piridina clorado ligado a um anel imidazolidina com N—H e grupo N-nitro; III, dois anéis fenólicos (com OH) e vários cloros, ligados por CH₂; IV, anel benzênico ligado a um grupo sulfona com carbono di-iodado; V, molécula com anel etoxifenil, átomo de silício com metilas, cadeia de carbonos e anel fluorado com grupo fenóxi.")),
  ["fenol", "Brönsted-Lowry"], enun=p(T(116, 0)) + "[[fig:1]]" + p(T(116, 11)),
  alts={k: re.sub(r"\s*III V$", "", v) for k, v in D[116]["alternativas"].items()})
X(117, "Química", "Energia", "<p>Os dejetos suínos são matéria orgânica que, decomposta por bactérias sem oxigênio (biodigestão anaeróbia), produz <strong>biogás</strong>, rico em metano, usado como combustível. Isso reduz a poluição dos recursos hídricos e diversifica a matriz energética. Alternativa <strong>B</strong>.</p><p>Etanol vem da fermentação de açúcares (A), biodiesel de óleos e gorduras (E); butano e metanol (C e D) não são obtidos diretamente de dejetos.</p>",
  tags=["biogás", "biodigestor"])
X(118, "Biologia", "Parasitologia", "<p>A curcumina é colocada na água dos criadouros, onde vivem as larvas do <em>Aedes aegypti</em>. É a larva que ingere a água e acumula a substância no intestino; ativada pela luz, ela destrói o tubo digestório e mata a larva, <strong>impedindo seu desenvolvimento</strong>. Alternativa <strong>D</strong>.</p><p>O mosquito adulto (A e E) não vive na água; ovos (B) não se alimentam; o texto fala em dano fatal ao intestino, não em falha na metamorfose (C).</p>",
  tags=["dengue", "larvicida"],
  enun=p(T(118, 0)) + fonte(T(118, 1)) + p("A forma de combate relatada tem como atividade o(a)"),
  alts={k: re.sub(r"\s*III V$", "", v) for k, v in D[118]["alternativas"].items()})
X(119, "Biologia", "Botânica", "<p>Para resistência mecânica e à degradação, o que importa é o <strong>cerne</strong>, a parte central do xilema, formada por células mortas impregnadas de substâncias (taninos, resinas) que resistem a fungos e cupins. A espécie 1 é a única com cerne em grande quantidade (+++), além de periderme e esclerênquima presentes. Alternativa <strong>A</strong>.</p><p>As espécies 2, 3 e 4 não têm cerne; a 5 tem pouco cerne, apesar de muito esclerênquima na periderme e no floema, tecidos que não formam a madeira usada na construção.</p>",
  tags=["xilema", "cerne", "madeira"],
  enun=p(T(119, 0)) + '<table class="tabela"><thead><tr><th colspan="5">Tecido analisado</th></tr><tr><th rowspan="2">Espécie</th><th rowspan="2">Periderme/Esclerênquima</th><th rowspan="2">Floema/Esclerênquima</th><th colspan="2">Xilema</th></tr><tr><th>Alburno</th><th>Cerne</th></tr></thead><tbody>'
       + "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td></tr>" for a, b, c, d, e in
                 [("1", "+ / +", "+ / −", "+", "+++"), ("2", "+ / −", "+ / −", "+++", "−"), ("3", "++ / −", "+++ / +", "+", "−"),
                  ("4", "+++ / +", "+++ / −", "+", "−"), ("5", "+++ / +", "+++ / +", "++", "+")]) + "</tbody></table>"
       + fonte("Legenda: (−) ausente, (+) presente em pequena quantidade, (++) presente em média quantidade, (+++) presente em grande quantidade.") + p(T(119, 4)))
X(120, "Química", "Cores e espectro", "<p>A cor que vemos é a complementar da cor absorvida. O caroteno tem cor amarelo-alaranjada; no círculo de cores complementares, o oposto do amarelo e do laranja fica na região do violeta e do azul (cerca de 400 a 480 nm). Os carotenos absorvem <strong>entre o violeta e o azul</strong>. Alternativa <strong>A</strong>.</p><p>Se absorvessem entre o laranja e o vermelho (E), pareceriam azul-esverdeados.</p>",
  figs(("q120", "À esquerda, espectro de absorção na região do visível (300 a 700 nm): a clorofila tem picos de absorção perto de 430 nm (azul) e 660 nm (vermelho); a antocianina, um pico largo perto de 530 nm (verde). À direita, círculo de cores complementares com as faixas: violeta (400–430 nm), azul (430–480), verde (480–560), amarelo (560–590), laranja (590–630) e vermelho (630–750); cores opostas no círculo são complementares.")),
  ["cor complementar", "pigmentos"], enun=p(T(120, 0), T(120, 1)) + "[[fig:1]]" + fonte(T(120, 7)) + p(T(120, 8)))
X(121, "Biologia", "Evolução", "<p>Na coevolução patógeno-hospedeiro, um parasita que mata o hospedeiro rapidamente perde o “abrigo” e tem menos chance de se espalhar. Com o tempo, são selecionadas formas menos letais. A <strong>baixa letalidade da dengue</strong> indica convivência mais longa e parasitismo mais eficiente com os humanos. Alternativa <strong>E</strong>.</p><p>A alta letalidade do ebola (C) indica, ao contrário, relação recente; o período de incubação (A e B) e a região da epidemia (D) não indicam o tempo de coevolução.</p>",
  tags=["coevolução", "virulência"])
X(122, "Biologia", "Saneamento", "<p>Na figura, o <strong>tanque séptico</strong> (etapa 3) é onde “o esgoto deve ficar em repouso por um período relativamente maior que nas outras etapas”. Esse repouso permite a decantação: os sólidos pesados descem e formam o lodo, separado da parte líquida. Alternativa <strong>C</strong>.</p><p>A caixa de gordura (1) retém gordura, a de passagem (2) só reúne o esgoto, o filtro biológico (5) usa bactérias e a cisterna (6) faz a cloração.</p>",
  figs(("q122", "Esquema “Como funciona a estação individual”: uma casa com as etapas 1, caixa de gordura (retém detritos da pia e da cozinha); 2, caixa de passagem (recebe o que vem dos banheiros e da lavanderia, reunindo todo o esgoto); 3, tanque séptico (o esgoto fica em repouso por um período relativamente maior que nas outras etapas); 4, caixa de inspeção (distribui os efluentes); 5, filtro biológico (colônias de bactérias consomem a matéria orgânica); 6, cisternas (etapa final, tratamento com cloro).")),
  ["tratamento de esgoto", "decantação"], enun=p(T(122, 0)) + "[[fig:1]]" + fonte(T(122, 7)) + p(T(122, 8)))
X(123, "Biologia", "Botânica", "<p>As auxinas são hormônios vegetais que, em concentração adequada, estimulam o enraizamento. Aplicadas na base da estaca, induzem a <strong>formação de raízes adventícias</strong> (raízes que nascem do caule), o que garante a fixação e a nutrição da nova planta. Alternativa <strong>D</strong>.</p><p>A floração (A) depende do fotoperíodo e de outros hormônios; as auxinas inibem, e não estimulam, as gemas laterais (B, dominância apical).</p>",
  tags=["auxinas", "estaquia"])
X(124, "Química", "Eletroquímica", "<p>O texto pede três condições: baixa temperatura, eletrólito polimérico (membrana) e meio ácido. A <strong>PEM</strong> opera entre 60 e 100 °C, usa ácido poliperfluorossulfônico sólido (um polímero) e suas semirreações envolvem H<sup>+</sup>, ou seja, meio ácido. Alternativa <strong>C</strong>.</p><p>A AFC opera em baixa temperatura, mas em meio básico (OH<sup>−</sup>); a PAFC é ácida, mas usa ácido fosfórico líquido; MSFC e SOFC operam acima de 600 °C.</p>",
  tags=["células a combustível", "hidrogênio"],
  enun=p(T(124, 0)) + '<table class="tabela"><thead><tr><th>Tipo de célula de combustível</th><th>Temperatura operacional (°C)</th><th>Eletrólito</th><th>Semirreações nos eletrodos</th></tr></thead><tbody>'
       '<tr><td>AFC</td><td>90 - 100</td><td>Hidróxido de potássio aquoso</td><td>H<sub>2</sub> + 2 OH<sup>−</sup> → 2 H<sub>2</sub>O + 2 e<sup>−</sup><br>½ O<sub>2</sub> + H<sub>2</sub>O + 2 e<sup>−</sup> → 2 OH<sup>−</sup></td></tr>'
       '<tr><td>MSFC</td><td>600 - 1 000</td><td>Carbonatos de lítio, sódio e/ou potássio fundidos</td><td>H<sub>2</sub> + CO<sub>3</sub><sup>2−</sup> → H<sub>2</sub>O + CO<sub>2</sub> + 2 e<sup>−</sup><br>½ O<sub>2</sub> + CO<sub>2</sub> + 2 e<sup>−</sup> → CO<sub>3</sub><sup>2−</sup></td></tr>'
       '<tr><td>PEM</td><td>60 - 100</td><td>Ácido poliperfluorossulfônico sólido</td><td rowspan="3">H<sub>2</sub> → 2 H<sup>+</sup> + 2 e<sup>−</sup><br>½ O<sub>2</sub> + 2 H<sup>+</sup> + 2 e<sup>−</sup> → H<sub>2</sub>O</td></tr>'
       '<tr><td>PAFC</td><td>175 - 200</td><td>Ácido fosfórico líquido</td></tr><tr><td>SOFC</td><td>600 - 1 000</td><td>Óxido de zircônio(IV) sólido</td></tr></tbody></table>'
       + p(T(124, 2)) + fonte(T(124, 3)) + p(T(124, 4)))
X(125, "Física", "Termologia", "<p>O corpo perde calor principalmente pela evaporação do suor, que retira energia da pele. Em dias úmidos, o ar já está perto da saturação de vapor-d’água, e <strong>o suor evapora com mais dificuldade</strong>: o calor se acumula e a sensação é de abafamento. Alternativa <strong>B</strong>.</p><p>A umidade não aumenta a temperatura do vapor (A) nem a absorção de radiação (C); o ar úmido, aliás, conduz um pouco melhor o calor (D); e, com o ar mais frio que o corpo, o vapor não condensa na pele (E).</p>",
  figs(("q125", "Tirinha de Calvin e Haroldo em quatro quadros, os dois descendo uma ladeira num carrinho. Calvin: “Tá quente hoje, né?”. Haroldo: “É mesmo.” Haroldo: “Mas o que me incomoda mesmo é a umidade.” Calvin: “Você não gosta de umidade?”. Haroldo: “Não mesmo.” Calvin: “Então, salta correndo.”")),
  ["evaporação", "umidade do ar"], enun=p(T(125, 0)) + "[[fig:1]]" + fonte(T(125, 2)) + p(T(125, 3)))
X(126, "Física", "Eletrodinâmica", "<p>No circuito D, o ponto B do primeiro interruptor vai à bateria. Com AB fechado, acende a lâmpada verde. Com BC fechado, a corrente segue até o ponto B do segundo interruptor, que escolhe entre a vermelha (AB) e a azul (BC). Assim, sempre <strong>exatamente uma lâmpada acende</strong>, e qualquer uma das três pode ser escolhida. Alternativa <strong>D</strong>.</p><p>Nos outros circuitos, alguma lâmpada nunca acende, duas acendem juntas ou há combinação em que nenhuma acende.</p>",
  figs(("q126", "Materiais: uma bateria; três lâmpadas, verde, vermelha e azul; um interruptor de alavanca com os contatos A, B e C e seu símbolo de três pontos."),
       ("q126a", "Circuito A: as lâmpadas verde e vermelha vão aos pontos A dos dois interruptores; a azul volta direto à bateria; o B do primeiro interruptor vai à bateria e o C do primeiro está ligado ao A do segundo."),
       ("q126b", "Circuito B: verde e vermelha vão aos pontos A dos interruptores; azul e o B do segundo voltam à bateria; os pontos C dos dois interruptores estão ligados entre si."),
       ("q126c", "Circuito C: verde e vermelha vão aos pontos A dos interruptores; os pontos B dos dois interruptores estão ligados entre si e à bateria; a azul volta direto à bateria; os pontos C ficam soltos."),
       ("q126d", "Circuito D: verde vai ao A do primeiro interruptor e vermelha ao A do segundo; o B do primeiro vai à bateria; o C do primeiro está ligado ao B do segundo; o C do segundo está ligado à lâmpada azul."),
       ("q126e", "Circuito E: os pontos A dos dois interruptores estão ligados entre si, assim como os pontos C; verde e vermelha vão aos pontos A, e os pontos B ligam a bateria e a lâmpada azul.")),
  ["interruptor three-way", "circuitos"],
  enun=p(T(126, 0)) + "[[fig:1]]" + p(T(126, 7)), alts=ALT(2))
X(127, "Biologia", "Ecologia", "<p>As preguiças-gigantes comiam frutos e eliminavam as sementes nas fezes, em outros lugares: eram dispersoras. Com a extinção, as plantas perderam esse “transporte”, as sementes passaram a cair perto da planta-mãe e a vegetação ficou restrita a áreas menores. Houve redução de <strong>fatores de disseminação das sementes</strong>. Alternativa <strong>C</strong>.</p><p>A preguiça não polinizava flores (A) nem alterava o tamanho das plantas (B), o número de sementes por fruto (D) ou os hábitats (E).</p>",
  tags=["dispersão de sementes", "megafauna"])
X(128, "Física", "Eletrodinâmica", "<p>Energia gasta no percurso: 110 km ÷ 5,0 km/kWh = 22 kWh. Potência do carregador: P = U · i = 220 · 20 = 4 400 W = 4,4 kW. Tempo: t = E/P = 22/4,4 = <strong>5,0 h</strong>. Alternativa <strong>D</strong>.</p><p>0,005 (A) sai de dividir 22 por 4 400 sem converter W em kW; 2,5 h (C) corresponderia ao dobro da potência.</p>",
  tags=["potência elétrica", "energia", "carro elétrico"])
X(129, "Biologia", "Botânica", "<p>Na dupla fecundação das angiospermas, um núcleo espermático fecunda a oosfera (forma o zigoto, 2n) e outro se une aos dois núcleos polares, formando o <strong>endosperma</strong> (3n). Esse tecido armazena nutrientes que alimentam o embrião durante o desenvolvimento e a germinação: é um tecido de <strong>reserva para o embrião</strong>. Alternativa <strong>B</strong>.</p><p>O fruto vem do ovário (A), o revestimento da semente vem dos tegumentos (C), e o endosperma não protege o megagametófito (D) nem forma vasos (E).</p>",
  tags=["dupla fecundação", "endosperma"])
QF = lambda s: re.sub(r"(?<=[A-Za-z\)])(\d+)", r"<sub>\1</sub>", s)
X(130, "Química", "Química orgânica", "<p>Ésteres derivados do ácido etanoico (acético) são os acetatos: acetato de isoamila e acetato de benzila. O de benzila tem anel aromático (cadeia insaturada); o de isoamila, CH<sub>3</sub>CO<sub>2</sub>(CH<sub>2</sub>)<sub>2</sub>CH(CH<sub>3</sub>)<sub>2</sub>, só tem ligações simples entre carbonos: cadeia saturada. Seu aroma é de <strong>banana</strong>. Alternativa <strong>B</strong>.</p><p>Pêssego (C) é o acetato de benzila, aromático; kiwi, rum e uva (A, D e E) vêm de outros ácidos.</p>",
  tags=["ésteres", "flavorizantes"],
  enun=p(T(130, 0)) + tabela(["Nome", "Fórmula", "Aroma"],
                             [["Benzoato de metila", QF("C6H5CO2CH3"), "Kiwi"], ["Acetato de isoamila", QF("CH3CO2(CH2)2CH(CH3)2"), "Banana"],
                              ["Acetato de benzila", QF("CH3CO2CH2C6H5"), "Pêssego"], ["Propanoato de isobutila", QF("CH3CH2CO2CH2CH(CH3)2"), "Rum"],
                              ["Antranilato de metila", QF("C6H4NH2CO2CH3"), "Uva"]]) + p(T(130, 2)))
X(131, "Biologia", "Fisiologia humana", "<p>No gráfico, cada pequena divisão do eixo do tempo vale 0,2 s (escala indicada). Entre dois picos consecutivos do sinal há cerca de 5 divisões: 5 × 0,2 = 1,0 s por batimento. Em um minuto: 60/1,0 = <strong>60 batimentos</strong>. Alternativa <strong>B</strong>.</p><p>Contar os picos por divisão grande sem a escala leva a valores como 30 ou 120 (A e D).</p>",
  figs(("q131", "Eletrocardiograma: sinal V_EC (mV) em função do tempo (s), sobre papel quadriculado; picos altos aparecem em intervalos regulares de cerca de 5 quadradinhos, e uma escala indica que um quadradinho corresponde a 0,2 s. Um retângulo tracejado destaca um ciclo cardíaco.")),
  ["eletrocardiograma", "frequência cardíaca"],
  enun=p("O eletrocardiograma é um exame cardíaco que mede a intensidade dos sinais elétricos advindos do coração. A imagem apresenta o resultado típico obtido em um paciente saudável e a intensidade do sinal (V<sub>EC</sub>) em função do tempo.") + "[[fig:1]]" + p(T(131, 3)))
X(132, "Biologia", "Genética", "<p>Os pais são portadores e não têm a doença, mas podem ter um filho afetado com probabilidade de 1/4. É exatamente o cruzamento Aa × Aa, em que só o genótipo aa (1/4) manifesta a característica: herança de caráter <strong>recessivo</strong>. Alternativa <strong>A</strong>.</p><p>Se fosse dominante (B), um dos pais portadores teria a doença; codominância (C) mostraria fenótipo intermediário nos heterozigotos; o texto fala de um único gene (não poligênico, D).</p>",
  tags=["herança autossômica recessiva"])
X(133, "Química", "Eletroquímica", "<p>Em cada pilha, o lítio (menor potencial) é o ânodo e o iodo o cátodo: ΔE = E<sub>cátodo</sub> − E<sub>ânodo</sub> = 0,54 − (−3,05) = 3,59 V. Três pilhas em série: 3 × 3,59 = <strong>10,77 V</strong>, dentro da faixa do carrinho de controle remoto (10,5 a 10,9 V). Alternativa <strong>D</strong>.</p><p>Somar os potenciais sem inverter o do lítio (0,54 + −3,05) daria valor negativo; uma única pilha (3,59 V) serviria para o celular (B).</p>",
  tags=["pilhas", "potencial padrão", "associação em série"],
  enun=p(T(133, 0)) + tabela(["", "Dispositivo eletrônico", "Faixa de força eletromotriz (V)"],
                             [["I", "Relógio de parede", "1,2 a 1,5"], ["II", "Celular", "3,5 a 3,8"], ["III", "Câmera digital", "7,5 a 7,8"],
                              ["IV", "Carrinho de controle remoto", "10,5 a 10,9"], ["V", "Notebook/Laptop", "19,5 a 20,0"]])
       + p(T(133, 2)) + '<p class="centro">\\(\\mathrm{I_2 + 2\\,e^- \\rightarrow 2\\,I^-}\\qquad E^\\circ = +0{,}54\\ \\mathrm{V}\\)</p>'
       + '<p class="centro">\\(\\mathrm{Li^+ + e^- \\rightarrow Li}\\qquad E^\\circ = -3{,}05\\ \\mathrm{V}\\)</p>' + p(T(133, 5)))
X(134, "Física", "Termologia", "<p>O alcoolômetro funciona por flutuação, e a leitura depende da densidade da solução. Com o aumento da temperatura, o líquido (e o próprio instrumento) se dilata: o volume aumenta, a densidade diminui e o alcoolômetro afunda mais, indicando um teor de álcool diferente do real. Por isso é preciso corrigir. A causa é a <strong>mudança do volume dos materiais por dilatação</strong>. Alternativa <strong>C</strong>.</p><p>A densidade diminui, não aumenta (B); a concentração e as propriedades químicas da mistura não mudam (D e E); a dissociação da água (A) é desprezível.</p>",
  tags=["dilatação", "densidade", "empuxo"],
  enun=p(T(134, 0)) + '<table class="tabela"><thead><tr><th colspan="7">Tabela de correção do alcoolômetro com temperatura 20 °C</th></tr>'
       '<tr><th rowspan="2">°GL</th><th colspan="6">Leitura da temperatura (°C)</th></tr><tr><th>20</th><th>21</th><th>22</th><th>23</th><th>24</th><th>25</th></tr></thead><tbody>'
       '<tr><td>35</td><td>35,0</td><td>34,6</td><td>34,2</td><td>33,8</td><td>33,4</td><td>33,0</td></tr>'
       '<tr><td>36</td><td>36,0</td><td>35,6</td><td>35,2</td><td>34,8</td><td>34,4</td><td>34,0</td></tr></tbody></table>'
       + fonte(T(134, 2)) + p(T(134, 3)))
X(135, "Química", "Polímeros", "<p>O polímero condutor precisa de ligações duplas conjugadas, isto é, alternadas com simples ao longo de toda a cadeia principal. Na estrutura D, a unidade que se repete é —CH=CH—: ligada às vizinhas, forma …C=C—C=C—C=C…, a alternância contínua do poliacetileno, o polímero premiado. Alternativa <strong>D</strong>.</p><p>A (poliestireno) e B não têm duplas na cadeia principal; em C e E há uma dupla por unidade separada da seguinte por carbonos saturados, sem conjugação contínua.</p>",
  figs(("q135a", "Unidade de repetição com cadeia principal só de ligações simples e um anel benzênico como ramificação (poliestireno)."),
       ("q135b", "Unidade de repetição com cadeia principal de ligações simples e uma carbonila (C=O) ligada à cadeia."),
       ("q135c", "Unidade de repetição com quatro carbonos e uma ligação dupla, separada da unidade seguinte por ligações simples entre carbonos saturados."),
       ("q135d", "Unidade de repetição de dois carbonos ligados por ligação dupla, que se alterna com ligações simples ao longo de toda a cadeia (poliacetileno)."),
       ("q135e", "Unidade de repetição com uma ligação dupla na cadeia e um carbono quaternário com metila e grupo éster (COOCH₃).")),
  ["polímeros condutores", "duplas conjugadas"],
  enun=p(T(135, 0)) + fonte(T(135, 1)) + p("Um exemplo desse polímero é representado pela estrutura"), alts=ALT(1))

completar(Q, R)
