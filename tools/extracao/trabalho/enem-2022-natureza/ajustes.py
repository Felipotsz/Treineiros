# Enem 2022, 2º dia, caderno azul: Ciências da Natureza (questões 91 a 135 do caderno; no site, 1 a 45, com numeroOriginal).
# Muitas fórmulas e estruturas vieram picadas na camada de texto: enunciados das Q91, 93, 96, 100, 103, 106, 108, 112, 116, 134 escritos à mão.
# Alternativas-imagem nas Q95, 96, 103 e 106. Quadros das Q94, 96, 101, 109, 115, 116, 120, 121, 128 em tabela HTML. Sem anuladas nesta área.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, paragrafos_enem

ID = "enem-2022-natureza"
META = {"id": ID, "banca": "Enem", "ano": 2022, "titulo": "Enem 2022: Ciências da Natureza", "fonte": "Inep", "dataExame": "2022-11-20",
        "duracaoMinutos": 150, "area": "Ciências da Natureza", "caderno": "azul", "dia": 2}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2022-dia2-azul")
Q = {}
P = lambda n: paragrafos_enem(D[n])
T = lambda n, i: P(n)[i][1]
p = lambda *xs: "".join(f"<p>{x}</p>" for x in xs)
ap = lambda *xs: "".join(f'<p class="apoio">{x}</p>' for x in xs)
fonte = lambda x: f'<p class="fonte">{x}</p>'
ALT = lambda ini: {k: f"[[fig:{i}]]" for i, k in enumerate("ABCDE", ini)}
LISTA = lambda s: "<ul>" + "".join(f"<li>{x.strip()}</li>" for x in s.split("•") if x.strip()) + "</ul>"


def quim(s):
    return re.sub(r"(?<=[A-Z\)a-z])(\d+)(?=[A-Z(\s,.;:)⋅]|$|<|−|–|\+)", r"<sub>\1</sub>", s)


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


def X(n, materia, assunto, expl, imagens=(), tags=(), enun=None, trocas=(), alts=None, q_=False):
    q = {"materia": materia, "assunto": assunto, "area": "Ciências da Natureza", "tags": list(tags), "numeroOriginal": n,
         "enunciado": enun or E(n, trocas=trocas), "alternativas": dict(alts or D[n]["alternativas"]),
         "imagens": list(imagens), "explicacao": expl}
    if q_: q["enunciado"] = quim(q["enunciado"]); q["alternativas"] = {k: quim(v) for k, v in q["alternativas"].items()}
    Q[n - 90] = q


X(91, "Química", "Oxirredução", "<p>O persulfato (S<sub>2</sub>O<sub>8</sub><sup>2−</sup>) é convertido pelo Fe(III) no radical sulfato, um oxidante fortíssimo, que ataca o TCE e o transforma em CO<sub>2</sub>, H<sub>2</sub>O e Cl<sup>−</sup>, como mostra o esquema. O TCE é oxidado e o persulfato é reduzido: a remediação se baseia em reações de <strong>oxirredução</strong>. Alternativa <strong>A</strong>.</p><p>Não há troca de grupos (B), formação de sólido (C), perda de água (D) ou ácido reagindo com base (E).</p>",
  figs(("q91", "Esquema em corte do solo: um caminhão injeta persulfato (S₂O₈²⁻) num poço; no subsolo, com Fe(III), ele vira o radical •SO₄⁻, que reage com o TCE (tricloroeteno, depositado no fundo do aquífero como DNAPL) e forma produtos intermediários clorados até H₂O, CO₂ e Cl⁻. Um poço de monitoramento fica à direita.")),
  ["persulfato", "remediação ambiental"],
  enun=ap("A figura ilustra esquematicamente um processo de remediação de solos contaminados com tricloroeteno (TCE), um agente desengraxante. Em razão de vazamentos de tanques de estocagem ou de manejo inapropriado de resíduos industriais, ele se encontra presente em águas subterrâneas, nas quais forma uma fase líquida densa não aquosa (DNAPL) que se deposita no fundo do aquífero. Essa tecnologia de descontaminação emprega o íon persulfato (S<sub>2</sub>O<sub>8</sub><sup>2−</sup>), que é convertido no radical •SO<sub>4</sub><sup>−</sup> por minerais que contêm Fe(III). O esquema representa de forma simplificada o mecanismo de ação química sobre o TCE e a formação dos produtos de degradação.")
       + "[[fig:1]]" + fonte(T(91, 5).replace("Química Nova", "<em>Química Nova</em>")) + p(T(91, 6)))
X(92, "Biologia", "Parasitologia", "<p>A filariose é transmitida por mosquitos (<em>Culex</em>) e a leishmaniose pelo mosquito-palha (flebotomíneo). As duas dependem de insetos vetores, então uma medida comum de prevenção é o <strong>controle das populações dos vetores</strong>. Alternativa <strong>D</strong>.</p><p>Vermífugo e esgoto (B e C) não atingem a leishmaniose; carne bem cozida (E) previne teníase; incinerar lixo (A) não é a medida específica.</p>",
  tags=["vetores", "doenças tropicais"])
X(93, "Física", "Energia", "<p>Os painéis aproveitam 20% de 1 500 W/m<sup>2</sup>, isto é, 300 W por metro quadrado. Para gerar 150 MW = 150 000 000 W: 150 000 000 ÷ 300 = <strong>500 000 m<sup>2</sup></strong>. Alternativa <strong>B</strong>.</p><p>100 000 m<sup>2</sup> (D) ignora a eficiência; 250 000 m<sup>2</sup> (C) considera só uma usina.</p>",
  tags=["potência", "eficiência"],
  enun=p(T(93, 0).replace("1 500 W m2", "1 500 W/m<sup>2</sup>")) + fonte(T(93, 1)) + p(T(93, 2)),
  alts={k: v.replace(" m2", " m<sup>2</sup>") for k, v in D[93]["alternativas"].items()})
X(94, "Química", "Funções inorgânicas", "<p>(1) Ácido clorídrico com cianeto de potássio: o ácido forte desloca o HCN, gás muito tóxico (KCN + HCl → KCl + HCN). (2) Ácido nítrico concentrado com sacarose (matéria orgânica): o HNO<sub>3</sub> é oxidante forte e reage energicamente com o açúcar. O resultado é <strong>liberação de gás tóxico e reação oxidativa forte</strong>. Alternativa <strong>A</strong>.</p><p>B inverte a ordem; o quadro não fala de sais tóxicos (C e E) nem de gás oxidante (D e E).</p>",
  tags=["incompatibilidade química", "segurança"],
  enun=p(T(94, 0)) + tabela(["Substância", "Incompatibilidade", "Riscos associados"],
                            [["Ácidos minerais fortes concentrados", "Bases fortes<br>Cianetos<br>Hipoclorito de sódio", "Reação enérgica, explosão, produção de oxidante forte e produto tóxico"],
                             ["Ácido nítrico concentrado", "Matéria orgânica", "Reação enérgica, explosão e produto tóxico"]])
       + p(T(94, 2)) + ap("(1) ácido clorídrico concentrado com cianeto de potássio;<br>(2) ácido nítrico concentrado com sacarose.") + fonte(T(94, 4)) + p(T(94, 5)))
X(95, "Física", "Eletromagnetismo", "<p>Pela regra da mão direita, com a corrente para cima, as linhas de campo são circunferências em torno do fio no sentido anti-horário, vistas de cima. Em cada ponto, a bússola se alinha tangente a essa circunferência, com o norte apontando no sentido do campo. A configuração correta é a <strong>D</strong>. Alternativa <strong>D</strong>.</p><p>As outras alternativas mostram as agulhas apontando para o fio, para fora dele ou no sentido horário.</p>",
  figs(("q95", "Um fio vertical com corrente i para cima atravessa uma placa horizontal; os pontos A, B e C estão numa circunferência tracejada em torno do fio. Ao lado, uma bússola com a agulha (norte em preto, sul em branco)."),
       ("q95a", "Alternativa A: três bússolas em torno do fio, com as agulhas em direções diferentes, não tangentes à circunferência."),
       ("q95b", "Alternativa B: três bússolas com as agulhas apontando todas no mesmo sentido."),
       ("q95c", "Alternativa C: três bússolas tangentes à circunferência, no sentido horário visto de cima."),
       ("q95d", "Alternativa D: três bússolas tangentes à circunferência, com o norte no sentido anti-horário visto de cima."),
       ("q95e", "Alternativa E: três bússolas com as agulhas apontando radialmente em relação ao fio.")),
  ["regra da mão direita", "campo magnético de fio"], alts=ALT(2),
  enun=p(T(95, 0).replace("corrente elétrica i,", "corrente elétrica <em>i</em>,")) + "[[fig:1]]" + p(T(95, 2).replace("corrente i,", "corrente <em>i</em>,")))
X(96, "Física", "Eletrodinâmica", "<p>Parada respiratória ocorre entre 20 mA e 100 mA. Com a pele molhada (1 kΩ), a tensão precisa ficar entre 20 V e 100 V. Uma bateria (12 V) dá 12 mA; duas em série, somando 24 V, dão 24 mA. A associação <strong>A</strong> liga as duas baterias em série, com o + de uma no − da outra, e aplica 24 V entre A e B. Alternativa <strong>A</strong>.</p><p>Nas outras, as baterias ficam em oposição (0 V) ou em paralelo (12 V), dando corrente de no máximo 12 mA.</p>",
  figs(("q96a", "Associação A: duas baterias em série, com o terminal negativo da primeira ligado ao positivo da segunda; A no positivo da primeira e B no negativo da segunda."),
       ("q96b", "Associação B: duas baterias ligadas pelo negativo de uma ao negativo da outra (em oposição)."),
       ("q96c", "Associação C: duas baterias com os fios cruzados, ligando polos iguais entre si."),
       ("q96d", "Associação D: duas baterias ligadas pelo positivo de uma ao positivo da outra (em oposição)."),
       ("q96e", "Associação E: duas baterias em paralelo, uma em cima da outra, com A e B nas junções laterais.")),
  ["corrente elétrica", "associação de geradores"], alts=ALT(1),
  enun=p(T(96, 0)) + tabela(["Corrente elétrica", "Dano físico"], [["Até 10 mA", "Dor e contração muscular"], ["De 10 mA até 20 mA", "Aumento das contrações musculares"], ["De 20 mA até 100 mA", "Parada respiratória"], ["De 100 mA até 3 A", "Fibrilação ventricular"], ["Acima de 3 A", "Parada cardíaca e queimaduras"]])
       + ap(T(96, 2), T(96, 3)) + fonte(T(96, 4).replace("Biofísica: fundamentos e aplicações.", "<em>Biofísica</em>: fundamentos e aplicações.")) + p(T(96, 5)))
X(97, "Química", "Separação de misturas", "<p>Os hexafluoretos de U-235 e U-238 diferem só um pouco na massa. A <strong>centrifugação</strong> separa componentes pela massa (as moléculas mais pesadas vão para fora do rotor), e é o método usado hoje nas ultracentrífugas de enriquecimento de urânio. Alternativa <strong>B</strong>.</p><p>Peneiração separa por tamanho de partícula; solventes e destilação dependem de propriedades químicas e pontos de ebulição quase iguais aqui; isótopos não se separam por magnetismo (A, C, D e E).</p>",
  tags=["enriquecimento de urânio", "centrifugação"])
X(98, "Biologia", "Biotecnologia", "<p>O vírus funciona como vetor: leva às células da retina uma cópia normal do gene RPE65. A célula passa a transcrever e traduzir esse gene, produzindo a enzima que faltava. O sucesso vem da <strong>expressão do gene responsável pela produção da enzima normal</strong>. Alternativa <strong>E</strong>.</p><p>O código genético é universal e não é corrigido (A); o RNA ribossômico não muda (B); não se induzem mutações (C); a proteína é produzida pelas células, não liberada pronta (D).</p>",
  tags=["terapia gênica", "vetor viral"])
X(99, "Biologia", "Ecologia", "<p>A jaqueira é uma espécie exótica que se espalhou com sucesso pelo país. Ela <strong>ocupa áreas de vegetação nativa e substitui parcialmente a flora original</strong>, competindo por luz e espaço e reduzindo a biodiversidade. Alternativa <strong>A</strong>.</p><p>Uma população não se mantém acima da capacidade de suporte (D); a espécie reduz, não aumenta, as relações ecológicas (C e E).</p>",
  tags=["espécies exóticas", "biodiversidade"], trocas=[("(Artocarpus heterophyllus)", "(<em>Artocarpus heterophyllus</em>)")])
X(100, "Física", "Cinemática", "<p>Na horizontal, a 1 m de altura, a queda dura t = √(2h/g) = √0,2 ≈ 0,447 s. Nesse tempo a água anda 3 m, então v = 3 ÷ 0,447 ≈ 6,7 m/s (v<sup>2</sup> = 9 ÷ 0,2 = 45). Na vertical, a altura alcançada é h = v<sup>2</sup>/2g = 45/20 = <strong>2,25 m</strong>. Alternativa <strong>B</strong>.</p><p>4,50 m (D) esquece o fator 2 de v<sup>2</sup>/2g.</p>",
  tags=["lançamento horizontal", "lançamento vertical"], enun=p(T(100, 0).replace("10 m s-2", "10 m/s<sup>2</sup>"), T(100, 1)))
X(101, "Química", "Cinética e porcentagem", "<p>A perda de sacarose em 10 h é 50% por mg/L de microrganismos. RB72: 13,0 × (1 − 0,35) ≈ 8,5; RB84: 18,0 × 0,6 = 10,8; RB92: 16,0 × 0,7 = 11,2; SP79: 14,0 × 0,75 = 10,5; SP80: 17,0 × 0,55 ≈ 9,4 g/L. A maior concentração final é a da <strong>RB92</strong>. Alternativa <strong>C</strong>.</p><p>RB84 (B) tem mais sacarose no início, mas perde 40% dela.</p>",
  tags=["leitura de tabela", "fermentação"],
  enun=p(T(101, 0).replace("cana- -de-açúcar", "cana-de-açúcar").replace("cana-de- -açúcar", "cana-de-açúcar"))
       + tabela(["Amostra", "RB72", "RB84", "RB92", "SP79", "SP80"], [["Concentração inicial de sacarose (g L<sup>−1</sup>)", "13,0", "18,0", "16,0", "14,0", "17,0"], ["Concentração de microrganismos (mg L<sup>−1</sup>)", "0,7", "0,8", "0,6", "0,5", "0,9"]])
       + ap(T(101, 2).replace("mg L−1", "mg L<sup>−1</sup>")) + fonte(T(101, 3)) + p(T(101, 4)))
X(102, "Biologia", "Biotecnologia", "<p>A PCR usa DNA polimerase, que só copia DNA. Como o SARS-CoV-2 é um vírus de RNA, antes da PCR o RNA viral precisa ser convertido em DNA pela transcriptase reversa: a etapa serve para <strong>obter moléculas de cDNA viral por meio da transcrição reversa</strong>. Alternativa <strong>E</strong>.</p><p>Anticorpos (B) são outro tipo de teste; cultivar o vírus (C) não é etapa da PCR.</p>",
  tags=["RT-PCR", "covid-19"])
X(103, "Física", "Estática", "<p>Na muleta atuam: o peso (P), vertical para baixo, no centro de massa; a força F, paralela à muleta, aplicada no topo; a normal (N), vertical para cima, no ponto de contato com o piso; e o atrito estático (f<sub>e</sub>), horizontal, no ponto de contato, opondo-se à tendência de escorregar (para fora). O esquema que mostra isso é o <strong>E</strong>. Alternativa <strong>E</strong>.</p><p>Nos outros, o peso, a normal ou o atrito estão aplicados no ponto errado ou com sentido errado.</p>",
  figs(("q103", "Muleta vertical pressionada contra o piso por uma força F de cima para baixo, com o centro de massa CM no meio."),
       ("q103a", "Esquema A: muleta inclinada, com F no topo; N para cima e P para baixo no ponto de contato; atrito f_e no contato apontando para a direita."),
       ("q103b", "Esquema B: muleta inclinada, com F no topo; N e P aplicados no centro de massa; atrito f_e no contato apontando para a esquerda."),
       ("q103c", "Esquema C: muleta inclinada, com F no topo; N para cima e P para baixo no ponto de contato; atrito f_e no contato para a direita."),
       ("q103d", "Esquema D: muleta inclinada, com F no topo; N e P aplicados no centro de massa; atrito f_e no contato para a esquerda."),
       ("q103e", "Esquema E: muleta inclinada, com F no topo; P para baixo no centro de massa; N para cima no ponto de contato; atrito f_e no contato apontando para a direita.")),
  ["diagrama de forças", "atrito"], alts=ALT(2),
  enun=ap("Tribologia é o estudo da interação entre duas superfícies em contato, como desgaste e atrito, sendo de extrema importância na avaliação de diferentes produtos e de bens de consumo em geral. Para testar a conformidade de uma muleta, realiza-se um ensaio tribológico, pressionando-a verticalmente contra o piso com uma força \\(\\vec{F}\\), conforme ilustra a imagem, em que CM representa o centro de massa da muleta.")
       + "[[fig:1]]" + ap("Mantendo-se a força \\(\\vec{F}\\) paralela à muleta, varia-se lentamente o ângulo entre a muleta e a vertical, até o máximo ângulo imediatamente anterior ao de escorregamento, denominado ângulo crítico. Esse ângulo também pode ser calculado a partir da identificação dos pontos de aplicação, da direção e do sentido das forças peso \\((\\vec{P})\\), normal \\((\\vec{N})\\) e de atrito estático \\((\\vec{f_e})\\).")
       + p(T(103, 7)))
X(104, "Biologia", "Fisiologia humana", "<p>A eritropoietina estimula a medula óssea a produzir hemácias (eritropoiese). Com mais hemácias, há mais hemoglobina, e o sangue carrega mais oxigênio aos músculos: o doping aumenta a <strong>taxa de transporte de oxigênio pelo sangue</strong>. Alternativa <strong>E</strong>.</p><p>O hormônio não aumenta a frequência cardíaca, o pulmão ou a massa muscular (A, B e C) e favorece a atividade aeróbica, não a anaeróbica (D).</p>",
  tags=["eritropoietina", "doping"], trocas=[("chamado doping sanguíneo", "chamado <em>doping</em> sanguíneo"), ("Esse tipo de doping", "Esse tipo de <em>doping</em>")])
X(105, "Física", "Dinâmica", "<p>As duas colisões duram o mesmo tempo. Nos pneus o carro volta, então a variação de velocidade (de +v a −v') é maior que nos blocos (de +v a 0): pelo teorema do impulso, a <strong>força média é maior na barreira de pneus</strong>. Nos blocos o carro para, perdendo toda a energia cinética; nos pneus parte dela é devolvida: a <strong>energia dissipada é maior nos blocos</strong>. Alternativa <strong>A</strong>.</p>",
  tags=["impulso", "energia dissipada"])
X(106, "Química", "Equilíbrio ácido-base", "<p>Com pH entre 5 e 7: a carboxila (pK<sub>a</sub> 1,8) está bem abaixo do pH, então perde o H<sup>+</sup> e fica como COO<sup>−</sup>; o amínio (pK<sub>a</sub> 7,9) está acima do pH, então continua protonado (NH<sub>3</sub><sup>+</sup>); o tiol (pK<sub>a</sub> 10,5) fica como SH. A estrutura é HS–C–C–COO<sup>−</sup> com NH<sub>3</sub><sup>+</sup>: a <strong>C</strong>. Alternativa <strong>C</strong>.</p>",
  figs(("q106", "Fórmula estrutural plana da penicilamina: HS–C(CH₃)₂–CH(NH₂)–COOH."),
       ("q106a", "Estrutura A: ⁻S–C(CH₃)₂–CH(NH₂)–COO⁻."),
       ("q106b", "Estrutura B: ⁻S–C(CH₃)₂–CH(NH₂)–COOH."),
       ("q106c", "Estrutura C: HS–C(CH₃)₂–CH(NH₃⁺)–COO⁻."),
       ("q106d", "Estrutura D: ⁻S–C(CH₃)₂–CH(NH₃⁺)–COOH."),
       ("q106e", "Estrutura E: HS–C(CH₃)₂–CH(NH₃⁺)–COOH.")),
  ["pKa", "ionização"], alts=ALT(2),
  enun=p(T(106, 0)) + "<ul><li>carboxila: —COOH, cujo p<em>K</em><sub>a</sub> é igual a 1,8;</li><li>amino: —NH<sub>2</sub>, que pode ser convertido em amínio (—NH<sub>3</sub><sup>+</sup>, cujo p<em>K</em><sub>a</sub> é igual a 7,9);</li><li>tiol: —SH, cujo p<em>K</em><sub>a</sub> é igual a 10,5.</li></ul>"
       + p("Sabe-se que p<em>K</em><sub>a</sub> = −log <em>K</em><sub>a</sub>.") + "[[fig:1]]" + p(T(106, 4)))
X(107, "Química", "Cinética química", "<p>No esquema, o H<sup>+</sup> protona o oxigênio da ligação entre os açúcares, a ligação se rompe, a água entra e, no fim, o H<sup>+</sup> é liberado de volta, sem ser consumido. Esse é o papel de um catalisador: <strong>aumentar a velocidade da reação</strong>. Alternativa <strong>C</strong>.</p><p>Um catalisador não desloca o equilíbrio nem muda a constante (B e D).</p>",
  figs(("q107", "Esquema da hidrólise ácida de um polissacarídeo: um H⁺ se liga ao oxigênio que une dois anéis de glicose; a ligação se rompe, formando um carbocátion; uma molécula de água ataca esse carbono; no final, forma-se o açúcar com OH e o H⁺ é liberado.")),
  ["catálise ácida", "etanol de segunda geração"],
  enun=p(T(107, 0)) + "[[fig:1]]" + fonte("OGEDA, T. L.; PETRI, D. F. S. [...] <em>Química Nova</em>, n. 7, 2010 (adaptado).") + p("Nessa conversão de polissacarídeos, a função do íon H<sup>+</sup> é"))
X(108, "Química", "Titulação", "<p>Foram gastos 8,0 mL de NaOH 0,10 mol/L, ou 0,80 mmol. Pela equação, 1 ácido tartárico reage com 2 NaOH: 0,40 mmol de ácido, que pesam 0,40 × 150 = 60 mg em 25,0 mL. Em 1 L: 60 × 40 = 2 400 mg = <strong>2,4 g/L</strong>. Alternativa <strong>B</strong>.</p><p>4,8 g/L (D) esquece a proporção 1 : 2.</p>",
  figs(("q108", "Equação da titulação: ácido tartárico (HOOC–CH(OH)–CH(OH)–COOH, massa molar 150 g/mol) + 2 NaOH → NaOOC–CH(OH)–CH(OH)–COONa + 2 H₂O.")),
  ["estequiometria", "concentração"],
  enun=p(T(108, 0).replace("mol L−1", "mol L<sup>−1</sup>")) + "[[fig:1]]" + p("A concentração de ácido tartárico no vinho analisado é mais próxima de:"),
  alts={k: v.split(" O OH")[0].replace("g L−1", "g L<sup>−1</sup>") for k, v in D[108]["alternativas"].items()})
X(109, "Química", "Radioatividade", "<p>Pelo quadro, a massa cai à metade (de 12,0 para 6,0 µg) em 8 dias: a meia-vida é 8 dias. Em 40 dias passam 5 meias-vidas: 12 ÷ 2<sup>5</sup> = 12 ÷ 32 ≈ <strong>0,4 µg</strong>. Alternativa <strong>D</strong>.</p><p>0,8 µg (C) corresponde a 4 meias-vidas (32 dias); 1,5 µg (B), a 3.</p>",
  tags=["meia-vida", "iodo-131"],
  enun=p(T(109, 0).replace("radioisótopo 131I", "radioisótopo <sup>131</sup>I").replace("isótopo 131I", "isótopo <sup>131</sup>I"))
       + tabela(["Tempo (dia)", "0", "2", "4", "5", "6", "8", "14"], [["Massa residual de <sup>131</sup>I (µg)", "12,0", "10,1", "8,5", "7,8", "7,2", "6,0", "3,6"]]) + p(T(109, 2)))
X(110, "Biologia", "Evolução", "<p>A espécie 1 produz milhares de gametas e não cuida da prole; as espécies 2, 3 e 4 produzem cada vez menos gametas, mas protegem mais os embriões (vigilância, desova fora da água, desenvolvimento no saco vocal do pai). São caminhos diferentes para deixar descendentes: <strong>o sucesso reprodutivo pode ser garantido por estratégias diferentes</strong>. Alternativa <strong>D</strong>.</p><p>A espécie 1 mostra que o cuidado parental não é necessário (B); não há “grau de evolução” superior (C).</p>",
  tags=["estratégias reprodutivas", "anfíbios"], enun=p(T(110, 0)) + ap(T(110, 1), T(110, 2), T(110, 3), T(110, 4)) + p(T(110, 5)))
X(111, "Física", "Óptica e astronomia", "<p>A energia produzida pela placa é máxima em 10/01 e mínima em 10/07: o dia é mais longo e o Sol mais alto em janeiro, verão do hemisfério sul. A residência está no hemisfério sul, mas não perto do polo (ali, em julho, não haveria sol algum), e a variação ao longo do ano descarta o Equador: fica perto do <strong>Trópico de Capricórnio</strong>. Alternativa <strong>A</strong>.</p>",
  figs(("q111a", "Esquema da Terra em 21 de dezembro: o eixo inclinado; o lado iluminado (dia) à esquerda, recebendo os raios do Sol; marcados o Polo Norte, o Círculo Polar Ártico, o Trópico de Câncer, o Equador, o Trópico de Capricórnio, o Círculo Polar Antártico e o Polo Sul; a incidência direta ao meio-dia ocorre no Trópico de Capricórnio."),
       ("q111b", "Gráfico de barras da energia produzida pela placa em 4 dias: maior em 10/01, menor em 10/04, mínima em 10/07 e de novo alta em 10/10.")),
  ["estações do ano", "energia solar"],
  enun=p(T(111, 0)) + "[[fig:1]]" + p(T(111, 5)) + "[[fig:2]]" + fonte(T(111, 9)) + p(T(111, 10)))
X(112, "Física", "Dinâmica", "<p>Soltando o balanço a 90°, no ponto mais baixo v<sup>2</sup> = 2gL. Ali, a tração total é T = mg + mv<sup>2</sup>/L = mg + 2mg = 3mg = 3 · 24 · 10 = 720 N, dividida entre as duas cordas: 360 N em cada. Com 25% de margem: 360 · 1,25 = <strong>450 N</strong>. Alternativa <strong>D</strong>.</p><p>360 N (C) é a tração sem a margem; 900 N (E) não divide entre as duas cordas.</p>",
  tags=["movimento circular", "força centrípeta"],
  enun=p(T(112, 0)) + LISTA("O ângulo máximo atingido pelo balanço em relação à vertical é igual a 90°;•Os filhos utilizarão o balanço até que tenham uma massa de 24 kg.")
       + p("Além disso, ele aproxima o movimento do balanço para o movimento circular uniforme, considera que a aceleração da gravidade é igual a 10 m/s<sup>2</sup> e despreza forças dissipativas.", T(112, 2)))
X(113, "Química", "Eletroquímica", "<p>Os filmes de zircônia e alumina são cerâmicos, não metais: não se oxidam no lugar do ferro nem fornecem elétrons. Eles cobrem a superfície e isolam o ferro do oxigênio e da umidade: é o <strong>efeito de barreira, que impede o contato com o agente oxidante</strong>. Alternativa <strong>D</strong>.</p><p>Proteção catódica, metal de sacrifício e galvanização (A, B e E) usam outro metal; a passivação (C) usa o óxido do próprio metal.</p>",
  tags=["corrosão", "nanotecnologia"], q_=True, trocas=[("Química Nova", "<em>Química Nova</em>")])
X(114, "Biologia", "Citologia", "<p>Em meio hipotônico, a água entra na célula por osmose e vai para o vacúolo. A célula vegetal não estoura por causa da parede celular; o vacúolo cresce e o pigmento fica mais diluído: <strong>aumento do vacúolo com diluição do pigmento no seu interior</strong>. Alternativa <strong>C</strong>.</p><p>O murchamento (E) aconteceria em meio hipertônico; a parede impede o rompimento (A, B e D).</p>",
  tags=["osmose", "célula vegetal"], trocas=[("Tradescantia pallida purpurea", "<em>Tradescantia pallida purpurea</em>")])
X(115, "Física", "Calorimetria", "<p>Com o mesmo volume V e a mesma energia Q: ΔT = Q/(ρVc). A razão é ΔT<sub>concreto</sub>/ΔT<sub>água</sub> = (ρc)<sub>água</sub>/(ρc)<sub>concreto</sub> = (1 000 · 4,2)/(2 500 · 0,8) = 4 200/2 000 = <strong>2,1</strong>. Alternativa <strong>B</strong>.</p><p>5,3 (D) compara só os calores específicos, esquecendo as densidades; 2,5 (C) compara só as densidades.</p>",
  tags=["calor específico", "ilha de calor"],
  enun=p(T(115, 0)) + tabela(["", "Densidade (kg/m<sup>3</sup>)", "Calor específico (J/g °C)"], [["Água", "1 000", "4,2"], ["Concreto", "2 500", "0,8"]]) + fonte(T(115, 2)) + p(T(115, 3)))
X(116, "Física", "Eletrodinâmica", "<p>A maior potência é a do nível superquente com 3 L/min (ΔT = 30 °C) — ou, igualmente, 6 L/min com 15 °C. Com 3 L/min = 50 g/s: P = 50 · 4,2 · 30 = 6 300 W. A corrente é 6 300 ÷ 220 ≈ 28,6 A. O múltiplo de 5 imediatamente superior é <strong>30 A</strong>. Alternativa <strong>B</strong>.</p><p>60 A (A) dobraria a vazão sem reduzir o ΔT.</p>",
  tags=["potência elétrica", "disjuntor"],
  enun=p(T(116, 0)) + tabela(["Vazão (L/min)", "ΔT morno (°C)", "ΔT quente (°C)", "ΔT superquente (°C)"], [["3", "10", "20", "30"], ["6", "5", "10", "15"]])
       + p("Utiliza-se um disjuntor para proteger o circuito dessa ducha contra sobrecargas elétricas em qualquer nível de aquecimento. Por padrão, o disjuntor é especificado pela corrente nominal igual ao múltiplo de 5 A imediatamente superior à corrente máxima do circuito. Considere que a ducha deve ser ligada em 220 V e que toda a energia é dissipada através da resistência do chuveiro e convertida em energia térmica transferida para a água, que apresenta calor específico de 4,2 J/(g °C) e densidade de 1 000 g/L.", T(116, 4)))
X(117, "Química", "Reações inorgânicas", "<p>Mármore é carbonato de cálcio. Com ácido clorídrico: CaCO<sub>3</sub> + 2 HCl → CaCl<sub>2</sub> + H<sub>2</sub>O + <strong>CO<sub>2</sub></strong>. O gás que borbulha é o gás carbônico. Alternativa <strong>C</strong>.</p><p>H<sub>2</sub> (A) sairia de ácido com metal; O<sub>2</sub>, CO e Cl<sub>2</sub> não se formam nessa reação.</p>",
  figs(("q117", "Um frasco com ácido e um pedaço de mármore no fundo; uma mangueira leva o gás produzido a um béquer com líquido, onde borbulha.")),
  ["carbonatos", "gás carbônico"], q_=True, enun=quim(p(T(117, 0))) + "[[fig:1]]" + p(T(117, 3)))
X(118, "Biologia", "Fisiologia animal", "<p>O gráfico mostra a concentração alta nos machos controle, baixa nas fêmeas e muito reduzida nos machos expostos à atrazina, que sofreram desmasculinização e hermafroditismo. O hormônio típico de machos, ligado aos caracteres sexuais masculinos, é a <strong>testosterona</strong>. Alternativa <strong>C</strong>.</p><p>O estrogênio (A) seria mais alto nas fêmeas; feromônio, somatotrofina e FSH (B, D e E) não explicam a desmasculinização.</p>",
  figs(("q118", "Gráfico de barras da concentração do hormônio (ng/mL): machos controle, cerca de 4; machos expostos à atrazina, cerca de 0,4; fêmeas controle, cerca de 0,5.")),
  ["desreguladores endócrinos", "atrazina"],
  enun=p(T(118, 0)) + "[[fig:1]]" + fonte(T(118, 3).replace("Proceedings of the National Academy of Sciences", "<em>Proceedings of the National Academy of Sciences</em>")) + p(T(118, 4)))
X(119, "Física", "Eletrodinâmica", "<p>A lâmpada tem R = U<sup>2</sup>/P = 4,5<sup>2</sup>/4,5 = 4,5 Ω. Com uma pilha invertida, as forças eletromotrizes ficam 1,5 + 1,5 − 1,5 = 1,5 V. A resistência total é 4,5 + 3 · 0,5 = 6 Ω. I = 1,5 ÷ 6 = <strong>0,25 A</strong>. Alternativa <strong>A</strong>.</p><p>0,33 A (B) esquece as resistências internas.</p>",
  tags=["lei de Pouillet", "gerador"])
X(120, "Biologia", "Bioquímica", "<p>A atividade sobe de 10 °C a 15 °C e depois cai com o aumento da temperatura. Acima da temperatura ótima, o calor desfaz as ligações que mantêm a forma da enzima, o sítio ativo se deforma e ela perde atividade: <strong>modificação da estrutura tridimensional da enzima</strong> (desnaturação). Alternativa <strong>E</strong>.</p><p>Só a temperatura variou (A e D); enzimas não são consumidas (C) e diminuem, não aumentam, a energia de ativação (B).</p>",
  tags=["enzimas", "desnaturação"],
  enun=quim(p(T(120, 0))) + tabela(["Ensaio", "Temperatura (°C)", "Decomposição de H<sub>2</sub>O<sub>2</sub> (10<sup>−12</sup> mol/min)"], [["1", "10", "8,0"], ["2", "15", "10,5"], ["3", "20", "9,5"], ["4", "25", "5,0"], ["5", "30", "3,6"], ["6", "35", "3,1"]]) + p(T(120, 3)))
X(121, "Biologia", "Microbiologia", "<p>Para atingir o fungo (eucarionte) sem afetar bactérias (procariontes), o alvo deve existir só em eucariontes. Bactérias não têm microtúbulos; fungos têm, e precisam deles para separar as cromátides na divisão. O antimicrobiano <strong>2</strong> é o seletivo. Alternativa <strong>B</strong>.</p><p>Ribossomos, membrana plasmática e síntese de DNA e RNA (1, 3, 4 e 5) existem nos dois grupos.</p>",
  tags=["antimicrobianos", "procariontes e eucariontes"],
  enun=p(T(121, 0)) + tabela(["Antimicrobiano", "Ação", "Efeito"], [["1", "Une-se aos ribossomos", "Impede a síntese proteica"], ["2", "Une-se aos microtúbulos", "Impede a segregação das cromátides"], ["3", "Une-se aos fosfolipídeos da membrana plasmática", "Reduz a permeabilidade da membrana plasmática"], ["4", "Interfere na síntese de timina", "Inibe a síntese de DNA"], ["5", "Interfere na síntese de uracila", "Impede a síntese de RNA"]]) + p(T(121, 2)))
X(122, "Biologia", "Fisiologia humana", "<p>O veneno da cascavel provoca hemorragia porque interfere na coagulação; a molécula derivada dele modula a coagulação sanguínea. Um anticoagulante pode servir para <strong>impedir a formação de trombos</strong>, coágulos que entopem vasos, como em alguns acidentes vasculares cerebrais. Alternativa <strong>A</strong>.</p><p>Anemia, urticária, linfonodos e pressão arterial (B a E) não dependem da coagulação.</p>",
  tags=["coagulação", "toxinas"])
X(123, "Física", "Gravitação", "<p>A gravidade que o Sol exerce nos planetas depende só da massa dele e da distância (F = GMm/d<sup>2</sup>). Trocando o Sol por um buraco negro de mesma massa, a força em cada planeta não muda, e as órbitas continuam iguais: <strong>eles manteriam suas órbitas inalteradas</strong>. Alternativa <strong>E</strong>.</p><p>O raio de 3 km só importa para quem chega muito perto; os planetas estão a milhões de quilômetros.</p>",
  tags=["lei da gravitação", "buraco negro"])
X(124, "Química", "Oxirredução", "<p>O ozônio (O<sub>3</sub>) desinfeta porque é um <strong>oxidante</strong> forte: oxida membranas, proteínas e material genético dos microrganismos. Pela mesma ação, também ataca as vias respiratórias e mucosas humanas, por isso seu uso indiscriminado é arriscado. Alternativa <strong>B</strong>.</p><p>O ozônio não é catalisador, redutor, ácido ou base (A, C, D e E).</p>",
  tags=["ozônio", "agentes oxidantes"], trocas=[("Química Nova", "<em>Química Nova</em>")])
X(125, "Biologia", "Genética", "<p>Cada célula da mulher inativa ao acaso um dos X. Numa heterozigota, algumas células expressam o alelo normal e outras o recessivo, em proporções que variam de mulher para mulher e de tecido para tecido. Por isso, a doença aparece com intensidades diferentes: <strong>expressividade variável</strong>. Alternativa <strong>E</strong>.</p><p>Não há um gene com vários efeitos (A), mutação (B), interação de genes (C) ou indivíduos com o genótipo que nunca manifestam (D).</p>",
  figs(("q125", "Esquema: um gameta masculino (22+X) e um feminino (22+X) formam o zigoto (44+XX), que se divide até a blástula; em cada célula, um dos X é inativado ao acaso. No corpo da mulher, amostras de células mostram manchas: umas com o X paterno inativado (pretas) e outras com o X materno inativado (brancas).")),
  ["inativação do X", "mosaicismo"], enun=p(T(125, 0)) + "[[fig:1]]" + p(T(125, 5)))
X(126, "Química", "Tratamento de água", "<p>Na coagulação, os sólidos em suspensão se juntam em flocos; na <strong>decantação</strong>, esses flocos, mais densos, descem para o fundo dos tanques. É aí que sai a maior parte dos sólidos. Alternativa <strong>B</strong>.</p><p>A filtração (C) retira o que sobrou; desinfecção e fluoretação (D e E) não removem sólidos.</p>",
  tags=["estação de tratamento", "decantação"])
X(127, "Biologia", "Metabolismo energético", "<p>Na fosforilação oxidativa, a cadeia respiratória bombeia prótons e eles voltam pela ATP sintase, produzindo ATP. A termogenina abre outro caminho para esses prótons; a energia vira calor em vez de ATP. Ela interfere na <strong>fosforilação oxidativa</strong>. Alternativa <strong>E</strong>.</p><p>Glicólise, fermentação, ciclo de Krebs e oxidação do piruvato (A a D) não usam o gradiente de prótons.</p>",
  tags=["termogenina", "fosforilação oxidativa"], trocas=[("Vida: a ciência da biologia.", "<em>Vida</em>: a ciência da biologia.")])
X(128, "Física", "Eletrodinâmica", "<p>Pela analogia com a lei de Ohm, R = U/i. Rota 1: 510/4 = 127,5; rota 2: 608/4 = 152; rota 3: 575/3 ≈ 191,7. Da menor para a maior resistência: <strong>1, 2, 3</strong>. Alternativa <strong>A</strong>.</p><p>Ordenar só pela d.d.p. daria 1, 3, 2 (B).</p>",
  tags=["lei de Ohm", "modelagem"],
  enun=p(T(128, 0), T(128, 1)) + tabela(["Rota", "d.d.p. (J/(carro·m))", "Corrente (carro/s)"], [["1", "510", "4"], ["2", "608", "4"], ["3", "575", "3"]]) + p(T(128, 3)))
X(129, "Química", "Equilíbrio químico", "<p>Com o pH menor, há mais H<sup>+</sup> no solo. A amônia, que é base, recebe esse próton e vira amônio: NH<sub>3</sub> + H<sup>+</sup> → NH<sub>4</sub><sup>+</sup>. Em solo ácido é favorecida a formação de <strong>NH<sub>4</sub><sup>+</sup></strong>. Alternativa <strong>C</strong>.</p><p>N<sub>2</sub>, NO<sub>2</sub><sup>−</sup> e NO<sub>3</sub><sup>−</sup> (A, D e E) não são favorecidos pelo excesso de H<sup>+</sup>; NH<sub>3</sub> (B) é consumida.</p>",
  figs(("q129", "Esquema do ciclo do nitrogênio: bactérias fixadoras de N₂ (no solo e nos nódulos das raízes de leguminosas) produzem amônia e amônio (NH₃, NH₄⁺); decompositores fazem a amonificação; bactérias nitrificantes transformam em nitritos (NO₂⁻) e nitratos (NO₃⁻); as plantas assimilam os nitratos; bactérias desnitrificantes devolvem N₂ à atmosfera.")),
  ["ciclo do nitrogênio", "chuva ácida"],
  enun=p(T(129, 0)) + "[[fig:1]]" + ap(T(129, 2)) + fonte(T(129, 3)) + p(T(129, 4)),
  alts={"A": "N<sub>2</sub>", "B": "NH<sub>3</sub>", "C": "NH<sub>4</sub><sup>+</sup>", "D": "NO<sub>2</sub><sup>−</sup>", "E": "NO<sub>3</sub><sup>−</sup>"})
X(130, "Biologia", "Fisiologia animal", "<p>Os bastonetes respondem à quantidade de fótons. Se forem mais sensíveis, bastam poucos fótons para estimulá-los: o animal consegue <strong>enxergar bem em ambientes mal iluminados</strong>, como acontece com animais noturnos. Alternativa <strong>C</strong>.</p><p>A percepção de cores depende dos cones (A, B e E), e o animal precisaria de menos, não de mais, luz (D).</p>",
  tags=["visão", "bastonetes"])
X(131, "Química", "Química orgânica", "<p>Todas as substâncias da figura (benzaldeído, salicilato de metila, anetol, vanilina, eugenol e cinamaldeído) têm em comum o anel de seis carbonos com ligações alternadas, o <strong>anel benzênico</strong>, que define os compostos aromáticos. Alternativa <strong>C</strong>.</p><p>Nem todas têm ramificações (A) ou carbonos assimétricos (E); insaturações e oxigênio (B e D) existem em muitos compostos não aromáticos.</p>",
  figs(("q131", "Fórmulas estruturais de seis compostos encontrados em óleos vegetais, todos com um anel benzênico: benzaldeído (óleo de amêndoas), salicilato de metila (óleo de gaultéria), anetol (óleo de anis), vanilina (óleo de baunilha), eugenol (óleo de cravos) e cinamaldeído (óleo de canela).")),
  ["compostos aromáticos"], enun=p(T(131, 0)) + "[[fig:1]]" + fonte("SOLOMONS, T. W. G.; FRYHLE, C. B. <em>Química orgânica</em>. Rio de Janeiro: LTC, 2009 (adaptado).") + p(T(131, 9)))
X(132, "Biologia", "Ecologia", "<p>O texto diz que a bactéria e o vírus vivem dentro das células do mosquito e “necessitarão de recursos comuns”. A <em>Wolbachia</em> disputa esses recursos com o vírus e reduz a carga viral: há <strong>competição do vírus e da bactéria no hospedeiro</strong>. Alternativa <strong>D</strong>.</p><p>A bactéria não come o vírus (A), não esteriliza o mosquito (B), não altera seu genótipo (C) nem recebe genes do vírus (E).</p>",
  tags=["Wolbachia", "dengue"],
  enun=p(T(132, 0).replace("Aedes aegypti", "<em>Aedes aegypti</em>").replace("bactéria Wolbachia", "bactéria <em>Wolbachia</em>").replace("Método Wolbachia", "Método <em>Wolbachia</em>")) + fonte(T(132, 1)) + p(T(132, 2)),
  alts={**D[132]["alternativas"], "E": "inserção de material genético do vírus na bactéria."})
X(133, "Biologia", "Imunologia", "<p>O <em>T. cruzi</em> modificado passou a produzir a molécula do tumor. O sistema imune, ao combater o protozoário, aprende a reconhecer essa molécula e passa a atacar as células tumorais que a têm. O mecanismo é a <strong>apresentação de antígeno específico</strong>. Alternativa <strong>D</strong>.</p><p>Não é ataque ao próprio corpo por erro (A), alergia (B), resposta inespecífica (C) ou anti-inflamatória (E).</p>",
  tags=["vacina", "antígeno"], trocas=[("Trypanosoma cruzi", "<em>Trypanosoma cruzi</em>"), ("um T. cruzi", "um <em>T. cruzi</em>")])
X(134, "Física", "Ondas", "<p>Nos gráficos, o mesmo pico do sinal aparece no detector A (na água) em cerca de 220 s e no B (no ar) em cerca de 232 s: 12 s de diferença. Então L/340 − L/1 540 = 12, ou seja, L · (1 540 − 340)/(340 · 1 540) = 12, L = 12 · 523 600/1 200 ≈ <strong>5 240 m</strong>. Alternativa <strong>D</strong>.</p><p>78 900 m (B) usaria só a velocidade na água com o tempo de 232 s; 14 400 m (C), a diferença de velocidades.</p>",
  figs(("q134a", "Esquema: um barco à esquerda, com o detector B na proa e o detector A submerso, e uma geleira à direita, a uma distância L."),
       ("q134b", "Dois gráficos de sinal em função do tempo (208 a 244 s): no detector A o pico aparece por volta de 220 s; no detector B, por volta de 232 s.")),
  ["velocidade do som", "intervalo de tempo"],
  enun=p("O sinal sonoro oriundo da queda de um grande bloco de gelo de uma geleira é detectado por dois dispositivos situados em um barco, sendo que o detector A está imerso em água e o B, na proa da embarcação. Sabe-se que a velocidade do som na água é de 1 540 m/s e no ar é de 340 m/s.")
       + "[[fig:1]]" + p(T(134, 5)) + "[[fig:2]]" + p(T(134, 9)))
X(135, "Física", "Óptica", "<p>A luz do sol entra pela parte da garrafa acima do telhado e, ao passar do ar para a água (e da água para o ar, dentro da casa), muda de direção e se espalha em várias direções: é a <strong>refração</strong>, que faz a garrafa funcionar como uma lâmpada. Alternativa <strong>E</strong>.</p><p>A difração (A) exigiria aberturas da ordem do comprimento de onda da luz, e o texto diz que o buraco é muito maior.</p>",
  figs(("q135", "Duas fotos: à esquerda, uma garrafa PET com água iluminada pela luz do sol, presa no teto e brilhando como uma lâmpada; à direita, o interior escuro de uma casa iluminado por essas garrafas, com um homem sentado.")),
  ["refração", "luz engarrafada"])

completar(Q, R)
