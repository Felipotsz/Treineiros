# Enem 2023, 2º dia, caderno azul: Ciências da Natureza (questões 91 a 135 do caderno; no site, 1 a 45, com numeroOriginal).
# O rótulo "QUESTÃO 109" não existe na camada de texto do PDF: Q108 e Q109 escritas à mão. Alternativas-imagem nas Q110 e Q132.
# Quadros das Q94, 100, 110, 118 e 121 em tabela HTML; rótulos de figuras que vazaram como texto foram descartados.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, paragrafos_enem

ID = "enem-2023-natureza"
META = {"id": ID, "banca": "Enem", "ano": 2023, "titulo": "Enem 2023: Ciências da Natureza", "fonte": "Inep", "dataExame": "2023-11-12",
        "duracaoMinutos": 150, "area": "Ciências da Natureza", "caderno": "azul", "dia": 2}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2023-dia2-azul")
Q = {}
P = lambda n: paragrafos_enem(D[n])
p = lambda *xs: "".join(f"<p>{x}</p>" for x in xs)
ap = lambda *xs: "".join(f'<p class="apoio">{x}</p>' for x in xs)
fonte = lambda x: f'<p class="fonte">{x}</p>'
ALT = lambda ini: {k: f"[[fig:{i}]]" for i, k in enumerate("ABCDE", ini)}


def quim(s):
    s = re.sub(r"(?<=[A-Z\)a-z])(\d+)(?=[A-Z(\s,.;:)⋅]|$|<|−|–|\+)", r"<sub>\1</sub>", s)
    for a, b in (("mol<sub>−1</sub>", "mol<sup>−1</sup>"), ("mol−1", "mol<sup>−1</sup>"), ("mol–1", "mol<sup>−1</sup>")):
        s = s.replace(a, b)
    return s


def figs(*pares):
    return [{"arquivo": a, "alt": t} for a, t in pares]


def tabela(cab, linhas):
    return ('<table class="tabela"><thead><tr>' + "".join(f"<th>{c}</th>" for c in cab) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in l) + "</tr>" for l in linhas) + "</tbody></table>")


def E(n, pular=(), troca=None, trocas=()):
    """Enunciado a partir dos parágrafos: pula índices, troca parágrafos inteiros por HTML pronto."""
    troca = troca or {}
    par = P(n)
    ult = max([i for i, (t, _) in enumerate(par) if t == "fonte" and i not in pular], default=-1)
    h = []
    for i, (t, x) in enumerate(par):
        if i in pular: continue
        if i in troca: h.append(troca[i]); continue
        if t == "fig": h.append(f"[[fig:{x}]]")
        elif t == "fonte": h.append(fonte(x))
        elif t == "titulo": h.append(f'<p class="apoio"><strong>{x}</strong></p>' if i < ult else f"<p><strong>{x}</strong></p>")
        elif i < ult: h.append(ap(x))
        else: h.append(p(x))
    s = "".join(h)
    for a, b in trocas:
        assert a in s, a; s = s.replace(a, b)
    return s


def X(n, materia, assunto, expl, imagens=(), tags=(), enun=None, trocas=(), alts=None, q_=False):
    q = {"materia": materia, "assunto": assunto, "area": "Ciências da Natureza", "tags": list(tags), "numeroOriginal": n,
         "enunciado": enun or E(n, trocas=trocas), "alternativas": dict(alts or D[n]["alternativas"]),
         "imagens": list(imagens), "explicacao": expl}
    if q_: q["enunciado"] = quim(q["enunciado"]); q["alternativas"] = {k: quim(v) for k, v in q["alternativas"].items()}
    Q[n - 90] = q


X(91, "Biologia", "Ecologia", "<p>As bombas de sementes fazem germinar plantas nativas mesmo em solo pobre. Mais plantas significam mais flores, e as flores fornecem néctar e pólen, que são o alimento das abelhas. O método <strong>aumenta a oferta de alimento</strong>. Alternativa <strong>D</strong>.</p><p>O texto não fala de predadores (A), de pesticidas (B), de abrigo (C) ou de locais de reprodução (E).</p>",
  tags=["abelhas", "polinização"])
X(92, "Biologia", "Fisiologia humana", "<p>A “palidez” das crianças é sinal de anemia ferropriva. O ferro é parte da hemoglobina, que transporta oxigênio no sangue; a panela de ferro e o prego enferrujado liberam ferro no feijão. As estratégias serviam para <strong>prevenir a anemia</strong>. Alternativa <strong>B</strong>.</p><p>Diarreia, verminoses, raquitismo (falta de vitamina D) e febre amarela (A, C, D e E) não se tratam com ferro.</p>",
  tags=["ferro", "anemia"])
X(93, "Química", "Energia", "<p>A usina nuclear aquece água com a energia da fissão do urânio, sem queimar carvão, petróleo ou gás. Por isso ela <strong>produz calor sem o consumo de combustíveis fósseis</strong> e sem emitir CO<sub>2</sub> na geração. Alternativa <strong>E</strong>.</p><p>Os resíduos radioativos são difíceis de tratar (A); a usina não exige desmatamento (B) nem emite gases que causam chuva ácida (C) ou gases tóxicos (D) na operação normal.</p>",
  tags=["energia nuclear"])
X(94, "Química", "Soluções", "<p>A dureza da água vem dos íons cálcio e magnésio, que formam carbonatos e sulfatos pouco solúveis (o “calcário” das tubulações). Para controlar as obstruções, o teste certo é o do <strong>cálcio</strong>, o teste 1. Alternativa <strong>A</strong>.</p><p>Cloreto forma sais solúveis (2); turbidez, coliformes e sólidos sedimentáveis (3, 4 e 5) medem outras características da água.</p>",
  tags=["dureza da água"],
  enun=p(P(94)[0][1]) + tabela(["Teste", "Parâmetro medido"], [["1", "Cálcio"], ["2", "Cloreto"], ["3", "Turbidez"], ["4", "Coliformes totais"], ["5", "Sólidos sedimentáveis"]]) + p(P(94)[2][1]))
X(95, "Biologia", "Fisiologia animal", "<p>Músculos vermelhos têm muita mioglobina e mitocôndrias e recebem muito sangue (oxigênio). Eles fazem respiração aeróbica e produzem ATP por muito tempo, sustentando o voo longo. Favorecem um <strong>metabolismo corpóreo elevado</strong>. Alternativa <strong>B</strong>.</p><p>Manobras e arrancadas rápidas (A e D) dependem dos músculos brancos; aerodinâmica e altitude (C e E) não dependem do tipo de músculo.</p>",
  tags=["aves", "metabolismo aeróbico"])
X(96, "Química", "Estequiometria", "<p>1 mol de CaCl<sub>2</sub> (111 g) absorve 2 mol de água (2 · 18 = 36 g). O ganho de massa é 36 ÷ 111 ≈ 0,324, ou seja, cerca de <strong>32%</strong>. Alternativa <strong>D</strong>.</p><p>24% (C) seria 36 ÷ 147, a fração de água no sal já hidratado, não o ganho em relação ao anidro; 16% (B) considera só uma molécula de água.</p>",
  tags=["hidratos", "massa molar"], q_=True)
X(97, "Biologia", "Fisiologia vegetal", "<p>O etileno é um hormônio vegetal gasoso que os próprios frutos liberam e que acelera o amadurecimento. No recipiente fechado, o gás não se dispersa, e o <strong>acúmulo de gás etileno</strong> faz os abacates amadurecerem mais rápido. Alternativa <strong>A</strong>.</p><p>Umidade, CO<sub>2</sub>, luz e falta de O<sub>2</sub> (B a E) não aceleram o amadurecimento; o CO<sub>2</sub> e a falta de O<sub>2</sub> até o retardam.</p>",
  tags=["etileno", "hormônios vegetais"], q_=True)
X(98, "Biologia", "Fotossíntese", "<p>Os cloroplastos mantidos funcionais nas células da lesma fazem fotossíntese. O produto primário da fotossíntese é a glicose, um <strong>carboidrato</strong>. Alternativa <strong>B</strong>.</p><p>Ácidos nucleicos, proteínas, vitaminas e lipídios (A, C, D e E) são produzidos depois, a partir dos carboidratos e de outros nutrientes.</p>",
  tags=["cloroplastos", "endossimbiose"])
X(99, "Biologia", "Parasitologia", "<p>A leishmaniose visceral é transmitida pelo mosquito-palha (flebotomíneo), que se infecta ao picar e sugar o sangue do cão contaminado. O protozoário no <strong>sangue</strong> do cão é o que representa risco de transmissão. Alternativa <strong>D</strong>.</p><p>Urina, saliva, fezes e secreções (A, B, C e E) não transmitem a doença, porque a transmissão é pelo vetor.</p>",
  tags=["leishmaniose", "zoonoses"], trocas=[("gênero Leishmania", "gênero <em>Leishmania</em>")])
X(100, "Física", "Cinemática", "<p>Na altura máxima, a esfera para por um instante (v = 0) e começa a descer. A aceleração é a da gravidade, que não muda durante todo o movimento: não é nula e aponta <strong>para baixo</strong>. Assim, <strong>v = 0 e a ≠ 0 para baixo</strong>. Alternativa <strong>C</strong>.</p><p>É erro comum achar que a aceleração se anula no topo (B); se ela fosse nula, a esfera ficaria parada lá.</p>",
  tags=["lançamento vertical", "aceleração da gravidade"],
  enun=p(P(100)[0][1]) + tabela(["Grandeza cinemática", "Módulo", "Sentido"], [["Velocidade", "v ≠ 0", "Para cima"], ["Velocidade", "v ≠ 0", "Para baixo"], ["Velocidade", "v = 0", "Indefinido*"], ["Aceleração", "a ≠ 0", "Para cima"], ["Aceleração", "a ≠ 0", "Para baixo"], ["Aceleração", "a = 0", "Indefinido*"]]) + fonte(P(100)[2][1]) + p(P(100)[3][1]))
X(101, "Biologia", "Fisiologia humana", "<p>Depois da ovulação, o folículo vira o corpo lúteo, que produz progesterona e estrógeno. Sem fecundação, o corpo lúteo degenera no fim do ciclo, e a produção desses hormônios cai, o que leva à menstruação. A queda se relaciona à <strong>regressão do corpo lúteo ovariano</strong>. Alternativa <strong>A</strong>.</p><p>A ovulação e o pico de LH e FSH (C e D) acontecem no meio do ciclo; ocitocina e adrenalina (B e E) não controlam esse processo.</p>",
  tags=["ciclo menstrual", "corpo lúteo"], trocas=[("Premenstrual Syndrome: a Systematic Review. The Lancet", "Premenstrual Syndrome: a Systematic Review. <em>The Lancet</em>")])
X(102, "Química", "Química orgânica", "<p>A oxidação de um álcool secundário dá uma cetona com a carbonila no mesmo carbono que tinha a hidroxila. Para obter hexan-3-ona (C=O no carbono 3), oxida-se o <strong>hexan-3-ol</strong>. Alternativa <strong>C</strong>.</p><p>Hexan-1-ol (B) é álcool primário e dá aldeído e ácido; hexanal e ácido hexanoico (A e E) já estão oxidados no carbono 1; hex-1-en-1-ol (D) é um enol.</p>",
  tags=["oxidação de álcoois", "cetonas"])
X(103, "Biologia", "Botânica", "<p>Em musgos e samambaias, o anterozoide precisa nadar na água até a oosfera. Nas gimnospermas e angiospermas, o grão de pólen forma o <strong>tubo polínico</strong>, que leva o gameta masculino direto ao óvulo, sem depender da água para a fecundação. Alternativa <strong>D</strong>.</p><p>Semente e fruto (C e A) protegem e dispersam o embrião, mas não atuam na fecundação; esporos e vasos condutores (B e E) também existem em plantas que dependem da água.</p>",
  tags=["tubo polínico", "evolução das plantas"])
X(104, "Química", "Equilíbrio químico", "<p>O gluconato se liga fortemente ao íon alumínio e o retira da solução. Pelo princípio de Le Chatelier, o equilíbrio entre o alumínio preso no vidro e o dissolvido se desloca para repor esse íon, dissolvendo mais alumínio. Quanto maior a <strong>concentração de gluconato de cálcio</strong>, maior o deslocamento e o risco. Alternativa <strong>B</strong>.</p><p>Cor, espessura e esterilização prévia do vidro (A, C e D) não deslocam esse equilíbrio, e o texto não diz que a reação é endotérmica (E).</p>",
  tags=["Le Chatelier", "deslocamento de equilíbrio"])
X(105, "Biologia", "Botânica", "<p>O floema fica na casca e leva a seiva elaborada (açúcares da fotossíntese) das folhas para o resto da planta. Retirar um anel completo de casca (anelamento) corta todo o floema: os açúcares não chegam às raízes, que morrem, e depois a planta inteira. A morte vem da interrupção da <strong>nutrição das raízes</strong>. Alternativa <strong>E</strong>.</p><p>O xilema, mais interno, continua levando água às folhas, que seguem fazendo fotossíntese, transpiração e trocas gasosas (A, B e C) por um tempo.</p>",
  tags=["floema", "anel de Malpighi"])
X(106, "Biologia", "Imunologia", "<p>O RNAm da vacina entra na célula e é lido pelos ribossomos no citoplasma, como qualquer RNAm. Assim a célula fabrica a proteína do vírus (a espícula), que o sistema imune reconhece como antígeno e contra a qual produz anticorpos e células de memória: a <strong>tradução do RNAm em proteína viral desencadeia a resposta antigênica</strong>. Alternativa <strong>C</strong>.</p><p>A capa lipídica só protege o RNAm (A); ele não sequestra o vírus (B), não compete com o RNA viral (D) e não entra no genoma (E).</p>",
  tags=["vacinas de RNAm", "covid-19"])
X(107, "Biologia", "Reprodução", "<p>O acrossomo é uma vesícula na cabeça do espermatozoide com enzimas (como a hialuronidase) que digerem a corona radiata e a zona pelúcida que envolvem o ovócito. Inibidas essas enzimas, o espermatozoide não chega à membrana: o coquetel impediu a <strong>passagem do espermatozoide pela corona radiata e zona pelúcida</strong>. Alternativa <strong>D</strong>.</p><p>Pronúcleo, fim da meiose, fusão de membranas e mitose do zigoto (A, B, C e E) só aconteceriam depois dessa passagem.</p>",
  tags=["fecundação", "acrossomo"])
X(108, "Física", "Eletromagnetismo", "<p>Pela lei de Faraday, só aparece corrente induzida num condutor quando o fluxo magnético através dele varia. No fogão por indução, uma bobina sob o vidro recebe corrente alternada e cria um <strong>campo magnético variável</strong>, que induz correntes no fundo metálico da panela, aquecendo-o por efeito Joule. Alternativa <strong>D</strong>.</p><p>Radiação e condução (A e B) são formas de transmitir calor, não de induzir corrente; o campo elétrico variável (C) e a ressonância (E) não descrevem o funcionamento.</p>",
  tags=["indução eletromagnética", "lei de Faraday"], enun=p(P(108)[0][1]),
  alts={"A": "radiação.", "B": "condução.", "C": "campo elétrico variável.", "D": "campo magnético variável.", "E": "ressonância eletromagnética."})
X(109, "Física", "Dinâmica", "<p>Com velocidade constante, as forças se equilibram. No aparelho do tipo 1, a carga pende de polias fixas, que só mudam a direção: F = M<sub>1</sub>g. No tipo 2, a carga pende de uma polia móvel, sustentada por dois trechos de corda: F = M<sub>2</sub>g/2. Com a mesma força, M<sub>2</sub>g/2 = M<sub>1</sub>g, e \\(\\frac{M_2}{M_1} = 2\\). Alternativa <strong>D</strong>.</p><p>\\(\\frac{1}{2}\\) (B) inverte a razão; 1 (C) ignora a polia móvel; 4 (E) supõe duas polias móveis.</p>",
  figs(("q109", "Dois aparelhos de musculação. Aparelho do tipo 1: uma corda passa por polias fixas no alto da estrutura e segura diretamente a carga M₁; o usuário puxa a outra ponta com força F para cima. Aparelho do tipo 2: a carga M₂ pende de uma polia móvel, sustentada por dois trechos de corda, e o usuário puxa com a mesma força F.")),
  ["polias", "equilíbrio de forças"],
  enun=ap("Uma academia decide trocar gradualmente seus aparelhos de musculação. Agora, os frequentadores que utilizam os aparelhos do tipo 1 podem também utilizar os aparelhos do tipo 2, representados na figura, para elevar cargas correspondentes às massas M<sub>1</sub> e M<sub>2</sub>, com velocidade constante. A fim de que o exercício seja realizado com a mesma força \\(\\vec{F}\\), os usuários devem ser orientados a respeito da relação entre as cargas nos dois tipos de aparelhos, já que as polias fixas apenas mudam a direção das forças, enquanto a polia móvel divide as forças.",
             "Em ambos os aparelhos, considere as cordas inextensíveis, as massas das polias e das cordas desprezíveis e que não há dissipação de energia.")
       + "[[fig:1]]" + p("Para essa academia, qual deve ser a razão \\(\\frac{M_2}{M_1}\\) informada aos usuários?"),
  alts={"A": "\\(\\frac{1}{4}\\)", "B": "\\(\\frac{1}{2}\\)", "C": "1", "D": "2", "E": "4"})
X(110, "Química", "Estequiometria", "<p>Cada frasco tem 5,25 g ÷ 525 g/mol = 0,01 mol de Hg<sub>2</sub>(NO<sub>3</sub>)<sub>2</sub>. Pela equação, ele reage com 0,02 mol de NaCl (0,02 · 58 = 1,16 g) e forma 0,01 mol de Hg<sub>2</sub>Cl<sub>2</sub> (4,72 g). A massa de precipitado cresce em linha reta, a partir de zero, até 1,16 g de NaCl; depois, o NaCl sobra e a massa fica constante em cerca de 4,7 g. Esse é o gráfico <strong>B</strong>. Alternativa <strong>B</strong>.</p><p>O gráfico A satura cedo demais (0,58 g); C nunca satura; D e E não começam na origem.</p>",
  figs(("q110a", "Gráfico A: a massa de Hg₂Cl₂ cresce em linha reta de 0 até cerca de 4,7 g quando a massa de NaCl chega a cerca de 0,58 g e depois fica constante até 1,4 g."),
       ("q110b", "Gráfico B: a massa de Hg₂Cl₂ cresce em linha reta de 0 até cerca de 4,7 g quando a massa de NaCl chega a cerca de 1,16 g e depois fica constante até 1,4 g."),
       ("q110c", "Gráfico C: a massa de Hg₂Cl₂ cresce em linha reta de 0 até cerca de 5,5 g em 1,4 g de NaCl, sem patamar."),
       ("q110d", "Gráfico D: a massa de Hg₂Cl₂ começa em cerca de 2,6 g com 0 g de NaCl, sobe devagar até cerca de 4,7 g em 1,16 g e depois fica constante."),
       ("q110e", "Gráfico E: a massa de Hg₂Cl₂ começa em cerca de 5,3 g com 0 g de NaCl e sobe devagar até cerca de 6,5 g em 1,4 g, sem patamar.")),
  ["reagente limitante", "precipitação"], alts=ALT(1),
  enun=quim(ap(P(110)[0][1]) + '<p class="apoio">Hg2(NO3)2 (aq) + 2 NaCl (aq) → Hg2Cl2 (s) + 2 NaNO3 (aq)</p>' + ap(P(110)[2][1])
            + tabela(["Frasco", "I", "II", "III", "IV", "V", "VI", "VII"], [["Massa de NaCl (g)", "0,2", "0,4", "0,6", "0,8", "1,0", "1,2", "1,4"]])
            + ap(P(110)[4][1])) + p(P(110)[5][1]))
X(111, "Física", "Ondas", "<p>Quanto mais longo o barbante, mais energia a onda perde no caminho (atrito, vibração do fio, dissipação). A energia que chega à outra lata é menor, e o som fica mais fraco: diminui a <strong>amplitude</strong>. Alternativa <strong>C</strong>.</p><p>Altura, período e comprimento de onda (A, B e E) dependem da frequência, que é a da voz e não muda; a velocidade (D) depende do meio (o barbante), que é o mesmo.</p>",
  figs(("q111", "Tirinha sem falas: num gramado, um menino fala num telefone de latas ligado por um barbante longo e esticado a outro menino, que segura uma lata grande junto ao ouvido.")),
  ["intensidade sonora", "amplitude"])
X(112, "Física", "Ondas", "<p>A difração atrapalha quando o comprimento de onda é da ordem das cavidades. Para ler cavidades menores, o laser precisa ter o menor comprimento de onda possível. Entre as opções, o <strong>violeta</strong> tem o menor comprimento de onda (cerca de 400 nm), por isso os discos Blu-ray usam laser violeta-azulado. Alternativa <strong>A</strong>.</p><p>Azul, verde, vermelho e infravermelho (B a E) têm comprimentos de onda maiores; o infravermelho era o do CD.</p>",
  tags=["difração", "espectro eletromagnético"])
X(113, "Física", "Ondas", "<p>A onda esférica espalha a potência pela superfície de uma esfera de raio igual à distância. A 10 m, a área é 4πr² = 4 · 3 · 100 = 1 200 m². A intensidade mínima (no alcance máximo) é I = P/A = 2,4 · 10<sup>−3</sup> ÷ 1 200 = <strong>2,0 · 10<sup>−6</sup> W/m²</strong>. Alternativa <strong>A</strong>.</p><p>2,4 · 10<sup>−3</sup> (D) é a própria potência, sem dividir pela área; 2,0 · 10<sup>−5</sup> (B) usa a área de um círculo (πr²) com erro de potência de 10.</p>",
  tags=["intensidade de onda", "potência"],
  enun=p(P(113)[0][1].replace("O bluetooth", "O <em>bluetooth</em>").replace("No padrão bluetooth", "No padrão <em>bluetooth</em>")) + p("Para que o sinal de <em>bluetooth</em> seja detectado pelas antenas, o valor mínimo de sua intensidade, em \\(\\frac{W}{m^2}\\), é mais próximo de"),
  alts={k: re.sub(r"10–(\d)\.", r"10<sup>−\1</sup>.", v) for k, v in D[113]["alternativas"].items()})
X(114, "Física", "Dinâmica", "<p>O atrito estático máximo é μmg = 0,2 · 2 000 = 400 N. Na aceleração (3 m/s²), a caixa precisa de 200 · 3 = 600 N para a frente; o atrito dá 400 N e a corda 2 (do lado da cabine) completa: T<sub>2</sub> = 200 N, T<sub>1</sub> = 0. Na frenagem (5 m/s²), precisa de 1 000 N para trás; o atrito dá 400 N e a corda 1 (traseira) dá T<sub>1</sub> = 600 N, T<sub>2</sub> = 0. Alternativa <strong>A</strong>.</p><p>B soma o atrito à força em vez de descontá-lo; C não desconta o atrito na aceleração.</p>",
  figs(("q114", "Caminhão visto de lado, andando para a direita (seta V). Na carroceria, uma caixa de massa M presa por duas cordas horizontais: a corda 1 liga a caixa à traseira da carroceria e a corda 2 liga a caixa à frente, junto à cabine.")),
  ["leis de Newton", "atrito estático"],
  enun=p(P(114)[0][1].replace("m/s2", "m/s<sup>2</sup>")) + "[[fig:1]]" + p(P(114)[3][1]),
  alts={k: re.sub(r"T(\d)", r"T<sub>\1</sub>", v) for k, v in D[114]["alternativas"].items()})
X(115, "Biologia", "Ecologia", "<p>Metais tóxicos não são digeridos nem metabolizados como fonte de energia: são elementos químicos que não se degradam. O aguapé absorve esses metais pelas raízes e os mantém <strong>acumulados nos tecidos</strong>; depois as plantas são retiradas da água. Alternativa <strong>B</strong>.</p><p>Enzimas, estômatos, glândulas e uso energético (A, C, D e E) não eliminam metais.</p>",
  tags=["biorremediação", "metais pesados"])
X(116, "Biologia", "Ecologia", "<p>Os decompositores transformam a matéria orgânica (detritos) em amônia: é a amonificação, a etapa <strong>2</strong>. Sem eles, essa etapa não aconteceria. Alternativa <strong>B</strong>.</p><p>A etapa 1 é a fixação do nitrogênio; 3 e 4 são a nitrificação (nitrosação e nitratação); 5 é a desnitrificação, todas feitas por outros grupos de bactérias.</p>",
  figs(("q116", "Esquema do ciclo do nitrogênio: Gás nitrogênio → (1) Amônia; Detritos → (2) Amônia; Amônia → (3) Nitrito → (4) Nitrato; e uma seta (5) volta do Nitrato ao Gás nitrogênio.")),
  ["ciclo do nitrogênio", "decompositores"], enun=p(P(116)[0][1]) + "[[fig:1]]" + p(P(116)[3][1]))
X(117, "Física", "Física moderna", "<p>Em um ano, o tripulante voa no máximo 1 000 h, das quais 80% (800 h) em cruzeiro, a 2 μSv/h: 800 · 2 = 1 600 μSv = 1,6 mSv. Dividindo pela dose de uma radiografia torácica: 1,6 ÷ 0,2 = <strong>8</strong> radiografias. Alternativa <strong>A</strong>.</p><p>10 (B) usaria as 1 000 h inteiras; 80 e 100 (C e D) erram a conversão de micro para mili.</p>",
  tags=["radiação ionizante", "unidades"], trocas=[("O tripulante de aeronaves e a radiação ionizante.", "<em>O tripulante de aeronaves e a radiação ionizante</em>.")])
X(118, "Química", "Química orgânica", "<p>O texto pede hidrocarboneto saturado, de 8 a 12 carbonos e ramificado. O <strong>2,2,4-trimetilpentano</strong> (isoctano, C<sub>8</sub>H<sub>18</sub>) atende a tudo: é a referência de octanagem 100. Alternativa <strong>C</strong>.</p><p>n-decano (I) é de cadeia normal; n-heptano (II) é normal e tem 7 C; o composto IV tem ligação dupla (é insaturado), e o V é um álcool, não hidrocarboneto.</p>",
  tags=["hidrocarbonetos", "octanagem"],
  enun=p(P(118)[0][1]) + tabela(["Composto", "Nomenclatura"], [["I", "<em>n</em>-decano"], ["II", "<em>n</em>-heptano"], ["III", "2,2,4-trimetilpentano"], ["IV", "3-etil-4-metilex-1-eno"], ["V", "3-etil-2-metilpentan-1-ol"]]) + p(P(118)[2][1]))
X(119, "Química", "Gases", "<p>Pela equação dos gases ideais, PV = nRT, com T = 650 + 273 = 923 K e V = 100 mL = 0,1 L: P = 0,1 · 0,082 · 923 ÷ 0,1 ≈ <strong>76 atm</strong>. Alternativa <strong>C</strong>.</p><p>53 atm (D) usa a temperatura em °C (650); 756 atm (A) erra a conversão de mL para L.</p>",
  tags=["equação de Clapeyron"],
  enun=ap(P(119)[0][1]) + fonte(P(119)[1][1].replace("Cartilha de limpeza urbana.", "<em>Cartilha de limpeza urbana</em>.")) + p(P(119)[2][1], "Considere: \\(R = 0{,}082\\ \\frac{\\text{L} \\cdot \\text{atm}}{\\text{mol} \\cdot \\text{K}}\\)", P(119)[4][1]))
X(120, "Física", "Eletrodinâmica", "<p>Cada conjunto é uma lâmpada em paralelo com R; os três estão em série. Quando L<sub>2</sub> queima, o conjunto do meio fica só com R, cuja resistência é maior que a da associação em paralelo. A resistência total aumenta, a corrente total cai, e a tensão sobre os conjuntos de L<sub>1</sub> e L<sub>3</sub> diminui: os brilhos ficam <strong>menos intensos</strong>. Alternativa <strong>C</strong>.</p><p>L<sub>1</sub> e L<sub>3</sub> estão em situações iguais, então mudam do mesmo jeito (D e E não fazem sentido).</p>",
  figs(("q120", "Circuito: uma fonte de energia (pilha) alimenta, em série, três conjuntos; em cada conjunto, uma lâmpada (L₁, L₂ ou L₃) está em paralelo com um resistor R.")),
  ["associação mista", "resistores"],
  enun=p(re.sub(r"\(L ?1, L2 e L3\)", "(L<sub>1</sub>, L<sub>2</sub> e L<sub>3</sub>)", P(120)[0][1]).replace("lâmpada L2", "lâmpada L<sub>2</sub>")) + "[[fig:1]]" + p(P(120)[3][1].replace("L2", "L<sub>2</sub>")),
  alts={k: re.sub(r"L ?(\d)", r"L<sub>\1</sub>", v) for k, v in D[120]["alternativas"].items()})
X(121, "Química", "Ligações químicas", "<p>O caráter iônico de uma ligação aumenta com a diferença de eletronegatividade entre os átomos. O oxigênio tem 3,44; o metal de menor eletronegatividade é o potássio (0,82), dando a maior diferença (2,62). O cátion do <strong>potássio</strong> forma a interação mais iônica. Alternativa <strong>A</strong>.</p><p>Cálcio, magnésio, zinco e ferro (B a E) têm eletronegatividades maiores e formam ligações com mais caráter covalente.</p>",
  figs(("q121", "Esquema: à esquerda, a superfície do “Solo com biocarvão” com um grupo carboxilato (C=O e O⁻); uma seta com Mⁿ⁺ leva à direita, ao “Solo fertilizado”, em que o cátion Mⁿ⁺ está ligado ao O⁻ do carboxilato.")),
  ["eletronegatividade", "caráter iônico"],
  enun=ap(P(121)[0][1], P(121)[1][1].replace("(—COO−)", "(—COO<sup>−</sup>)").replace("Mn+", "M<sup>n+</sup>")) + "[[fig:1]]" + ap(P(121)[6][1])
       + tabela(["Elemento metálico", "Eletronegatividade"], [["K", "0,82"], ["Ca", "1,00"], ["Mg", "1,31"], ["Zn", "1,65"], ["Fe", "1,83"]])
       + fonte(P(121)[8][1].replace("ChemMatters", "<em>ChemMatters</em>")) + p(P(121)[9][1]))
X(122, "Física", "Termologia", "<p>O vapor entra a 120 °C e sai como água líquida a 100 °C. Primeiro ele esfria de 120 °C para 100 °C, cedendo <strong>calor sensível</strong>; depois condensa a 100 °C, cedendo <strong>calor latente de condensação</strong>. Essa é a energia que a parede passa ao doce. Alternativa <strong>D</strong>.</p><p>A vaporização (A, C e E) é o que acontece com a água do doce, que recebe essa energia; não é a fonte dela.</p>",
  tags=["calor sensível", "calor latente"])
X(123, "Química", "Isomeria", "<p>O ibuprofeno é quiral: tem um carbono assimétrico (ligado a H, CH<sub>3</sub>, COOH e ao anel), e por isso apresenta isomeria óptica. Entre os outros, só o <strong>butilbrometo de escopolamina</strong> tem carbono quiral (o carbono ligado ao H, ao anel, ao CH<sub>2</sub>OH e à carbonila, além dos do biciclo). Alternativa <strong>E</strong>.</p><p>Fenacetina, paracetamol, dipirona e diclofenaco (A a D) não têm carbono com quatro ligantes diferentes.</p>",
  figs(("q123a", "Fórmula estrutural plana do ibuprofeno: um anel benzênico ligado, de um lado, a um grupo isobutila e, do outro, a um carbono com CH₃ e um grupo COOH."),
       ("q123b", "Fórmulas estruturais de fenacetina, paracetamol, dipirona sódica, diclofenaco sódico e butilbrometo de escopolamina; esta última tem um carbono ligado a H, a um anel benzênico, a um grupo CH₂OH e a um grupo éster.")),
  ["isomeria óptica", "carbono quiral"], enun=ap(P(123)[0][1]) + "[[fig:1]]" + p(P(123)[3][1]) + "[[fig:2]]" + p(P(123)[10][1]))
X(124, "Física", "Cinemática", "<p>O carro (100 km/h) leva 480 ÷ 100 = 4,8 h = 288 min, mais 10 pedágios de 3 min = 30 min: 318 min. O caminhão (80 km/h), com cobrança automática, leva 480 ÷ 80 = 6 h = 360 min. A diferença é 360 − 318 = <strong>42 minutos</strong>. Alternativa <strong>B</strong>.</p><p>72 min (C) esquece os pedágios; 30 min (A) é só o tempo de pedágio.</p>",
  tags=["velocidade média"], enun=ap(P(124)[0][1]) + p(P(124)[1][1], P(124)[2][1]),
  alts={**D[124]["alternativas"], "E": "360"})
X(125, "Biologia", "Genética", "<p>Cada pessoa com trissomia do 21 forma, na meiose, gametas com um cromossomo 21 ou com dois. Combinando os gametas dos dois pais: 1 + 1 = zigoto normal; 1 + 2 = trissômico; 2 + 2 = tetrassômico. Os zigotos podem ser <strong>normais, trissômicos ou tetrassômicos</strong>. Alternativa <strong>E</strong>.</p><p>As outras alternativas excluem combinações possíveis; o caso real citado mostra que um filho normal pode nascer.</p>",
  tags=["síndrome de Down", "meiose"],
  enun=E(125, trocas=[('<p class="apoio">Pais com síndrome de Down A síndrome', '<p class="apoio"><strong>Pais com síndrome de Down</strong></p><p class="apoio">A síndrome'), ("Três anos após dar à luz, mãe portadora de síndrome de Down revela detalhes de seu dia a dia.", "<em>Três anos após dar à luz, mãe portadora de síndrome de Down revela detalhes de seu dia a dia</em>.")]))
X(126, "Química", "Funções orgânicas", "<p>A amina (R<sub>3</sub>N), de cadeia longa, é pouco solúvel em água. Ao reagir com HCl, vira o sal cloridrato (R<sub>3</sub>NH)<sup>+</sup>Cl<sup>−</sup>, formado por íons, que se dissolvem bem no plasma, que é aquoso. A conversão aumenta o <strong>caráter iônico</strong>. Alternativa <strong>C</strong>.</p><p>A basicidade diminui (A), a lipofilicidade diminui (B), a cadeia carbônica não muda (D) e não há oxirredução (E).</p>",
  tags=["aminas", "solubilidade"],
  enun=p(P(126)[0][1], "R<sub>3</sub>N + HCl → (R<sub>3</sub>NH)<sup>+</sup>Cl<sup>−</sup>", P(126)[2][1]))
X(127, "Biologia", "Metabolismo energético", "<p>Na cadeia respiratória, o NADH entrega elétrons e volta a NAD<sup>+</sup>. Se o cianeto bloqueia a citocromo c oxidase, os elétrons param de fluir: os transportadores ficam reduzidos e o NADH não consegue se oxidar. A concentração de <strong>NADH</strong> aumenta. Alternativa <strong>C</strong>.</p><p>A produção de ATP e de água cai (A e B); o CO<sub>2</sub> também diminui, porque o ciclo de Krebs para sem NAD<sup>+</sup> (D); a quantidade da enzima não muda (E).</p>",
  figs(("q127", "Esquema da cadeia respiratória: o substrato do nutriente é oxidado a CO₂, reduzindo NAD⁺ a NADH; os elétrons passam do NADH ao transportador 1, ao 2, ao 3 e à citocromo c oxidase (Fe³⁺ é reduzido a Fe²⁺), e por fim ao O₂, que forma H₂O. Cada transportador alterna entre forma reduzida e forma oxidada.")),
  ["cadeia respiratória", "cianeto"],
  enun=ap('<strong>Toxicidade do cianeto</strong>') + ap(P(127)[0][1].replace("Toxicidade do cianeto ", "").replace("NAD+", "NAD<sup>+</sup>").replace("Fe3+", "Fe<sup>3+</sup>").replace("Fe2+", "Fe<sup>2+</sup>").replace("citocromo c", "citocromo <em>c</em>"))
       + "[[fig:1]]" + fonte(P(127)[6][1].replace("Biologia molecular da célula.", "<em>Biologia molecular da célula</em>.")) + p(P(127)[7][1]),
  alts={**D[127]["alternativas"], "E": "citocromo <em>c</em> oxidase."})
X(128, "Física", "Ondas", "<p>Duas ondas interferem quando se superpõem com a mesma frequência: o receptor do rádio, sintonizado numa frequência, captaria também o sinal do celular. A interferência só ocorre se as ondas <strong>tiverem a mesma frequência</strong>. Alternativa <strong>C</strong>.</p><p>Ondas de rádio e de celular não são audíveis (A); potência e intensidade (B e D) não determinam a interferência; e todas as ondas eletromagnéticas têm a mesma velocidade no ar (E).</p>",
  tags=["ondas eletromagnéticas", "interferência"])
X(129, "Química", "Polaridade", "<p>O Aldrin é apolar (simétrico, com baixa polaridade) e por isso se dissolve em gorduras, não em água. Ele se acumula nos tecidos gordurosos e é encontrado em maior concentração no <strong>leite, por causa do alto teor de gorduras</strong>. Alternativa <strong>E</strong>.</p><p>Saliva, sangue, lágrima e urina (A a D) são fluidos essencialmente aquosos, onde uma substância apolar se dissolve pouco.</p>",
  figs(("q129", "Fórmula estrutural do Aldrin: dois anéis bicíclicos fundidos, com seis átomos de cloro na parte inferior da molécula.")),
  ["bioacumulação", "lipossolubilidade"], q_=True,
  enun=ap(P(129)[0][1]) + "[[fig:1]]" + fonte(P(129)[3][1].replace("Química Nova", "<em>Química Nova</em>")) + p(P(129)[4][1], P(129)[5][1]))
X(130, "Física", "Termologia", "<p>O copo “não esquenta na parte externa”: o material é mau condutor de calor, com <strong>baixa condutividade térmica</strong>. E, por ser reutilizável, substitui muitos copos descartáveis, <strong>reduzindo o resíduo não biodegradável</strong>. Alternativa <strong>D</strong>.</p><p>O copo tem 50% de plástico não biodegradável, então não é totalmente biodegradável (A e E); a condutividade é baixa, não alta (B); e ele não aumenta resíduos (C).</p>",
  tags=["condutividade térmica", "sustentabilidade"])
X(131, "Química", "Propriedades da matéria", "<p>O refrigerante comum tem grande quantidade de açúcar dissolvido no mesmo volume, enquanto o diet tem adoçantes em massas muito pequenas. Mais massa no mesmo volume significa <strong>maior densidade</strong>; por isso a lata comum afunda na água e a diet costuma boiar. Alternativa <strong>A</strong>.</p><p>O açúcar aumenta a viscosidade (B), a massa de solutos (D) e abaixa a temperatura de congelamento (E); o gás é o mesmo nas duas (C).</p>",
  tags=["densidade", "propriedades coligativas"], q_=True,
  trocas=[("Química Nova na Escola", "<em>Química Nova na Escola</em>")])
X(132, "Física", "Gases", "<p>Com volume e quantidade de ar constantes, a transformação é isovolumétrica: P/T é constante, e a pressão é proporcional à temperatura absoluta. No resfriamento, o ponto sai de (T<sub>0</sub>, P<sub>0</sub>) e desce em linha reta (que passaria pela origem) até T, com pressão menor. Esse é o gráfico <strong>E</strong>. Alternativa <strong>E</strong>.</p><p>B seria isobárico; C, uma hipérbole, é de transformação isotérmica; D e A aumentam a pressão ao esfriar.</p>",
  figs(("q132a", "Gráfico A: a pressão fica constante em P₀ enquanto a temperatura cai de T₀ até T e depois cai na vertical, em T."),
       ("q132b", "Gráfico B: segmento horizontal em P₀, de T₀ até T (pressão constante)."),
       ("q132c", "Gráfico C: curva hiperbólica de (T₀, P₀) até T, com a pressão subindo enquanto a temperatura cai."),
       ("q132d", "Gráfico D: segmento de reta de (T₀, P₀) até T, com a pressão subindo pouco enquanto a temperatura cai."),
       ("q132e", "Gráfico E: segmento de reta inclinado de (T₀, P₀) até T, com a pressão diminuindo proporcionalmente à temperatura.")),
  ["transformação isovolumétrica", "gás ideal"], alts=ALT(1),
  enun=p(P(132)[0][1].replace("pressão P0", "pressão <em>P</em><sub>0</sub>").replace("pneus era T0", "pneus era <em>T</em><sub>0</sub>").replace("temperatura ambiente T.", "temperatura ambiente <em>T</em>."), P(132)[1][1]))
X(133, "Química", "Química orgânica", "<p>O texto diz que os microrganismos não quebram moléculas ramificadas. A parte apolar desse tensoativo tem uma cadeia muito ramificada; trocá-la por uma <strong>cadeia normal</strong> (linear) torna o detergente biodegradável, como os alquilbenzenossulfonatos lineares usados hoje. Alternativa <strong>E</strong>.</p><p>Retirar a parte polar ou trocar o grupo aniônico (A, C e D) mexe na função detergente, não na biodegradação; o anel aromático (B) não é o problema apontado.</p>",
  figs(("q133", "Fórmula estrutural do tensoativo não biodegradável: uma cadeia carbônica longa e muito ramificada ligada a um anel benzênico, que tem na outra ponta um grupo sulfonato (SO₃⁻ Na⁺).")),
  ["detergentes", "biodegradabilidade"], enun=p(P(133)[0][1]) + "[[fig:1]]" + p(P(133)[4][1]))
X(134, "Biologia", "Citologia", "<p>Micronúcleos são fragmentos de DNA que ficam fora do núcleo principal quando, na divisão celular, pedaços de cromossomos (ou cromossomos inteiros) não são puxados corretamente pelo fuso. Eles se originam dos <strong>cromossomos</strong>. Alternativa <strong>E</strong>.</p><p>Nucléolos, lisossomos, ribossomos e mitocôndrias (A a D) não se separam pelo fuso mitótico na divisão celular.</p>",
  tags=["micronúcleos", "mitose"],
  trocas=[("Micronúcleos em células tumorais: biologia e implicações para a tumorigênese.", "<em>Micronúcleos em células tumorais</em>: biologia e implicações para a tumorigênese.")])
X(135, "Física", "Ondas", "<p>O pulso vai e volta pela camada líquida no intervalo entre os dois ecos: 1,1 − 0,5 = 0,6 s. Nesse tempo, percorre 2 · 450 = 900 m. A velocidade é 900 ÷ 0,6 = <strong>1 500 m/s</strong>. Alternativa <strong>D</strong>.</p><p>540 m/s (B) e 270 m/s (A) multiplicam a distância pelo tempo em vez de dividir; 818 m/s (C) divide 900 por 1,1; 1 800 m/s (E) divide 900 por 0,5.</p>",
  figs(("q135", "Esquema do subsolo: um emissor e detector de pulsos na superfície; abaixo, uma camada de rocha, uma camada de líquido com 450 m de espessura e outra camada de rocha.")),
  ["eco", "velocidade do som"], enun=p(P(135)[0][1]) + "[[fig:1]]" + p(P(135)[2][1]))

completar(Q, R)
