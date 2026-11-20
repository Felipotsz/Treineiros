# Enem 2009, 1º dia (05/12/2009), caderno azul: Ciências da Natureza (questões 1 a 45). Em 2009 a Natureza abria o 1º dia.
# Texto legível. Quadros das Q18, Q19, Q25, Q28 e Q43 em HTML. Alternativas-imagem nas Q21 (ciclos de vida) e Q36 (estruturas químicas).
# Sem anuladas nesta área.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, paragrafos_enem

ID = "enem-2009-natureza"
META = {"id": ID, "banca": "Enem", "ano": 2009, "titulo": "Enem 2009: Ciências da Natureza", "fonte": "Inep", "dataExame": "2009-12-05",
        "duracaoMinutos": 150, "area": "Ciências da Natureza", "caderno": "azul", "dia": 1}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2009-dia1-azul")
Q = {}
P = lambda n: paragrafos_enem(D[n])
T = lambda n, i: P(n)[i][1]
p = lambda *xs: "".join(f"<p>{x}</p>" for x in xs)
ap = lambda *xs: "".join(f'<p class="apoio">{x}</p>' for x in xs)
tit = lambda x: f'<p class="apoio"><strong>{x}</strong></p>'
fonte = lambda x: f'<p class="fonte">{x}</p>'
ALT = lambda ini: {k: f"[[fig:{i}]]" for i, k in enumerate("ABCDE", ini)}
LIMPA = lambda s: re.sub(r"fi ([a-zà-ú])", r"fi\1", re.sub(r"fl ([a-zà-ú])", r"fl\1", re.sub(r"(\w)- -(\w)", r"\1-\2", s)))
OL = lambda *xs: "<ol>" + "".join(f"<li>{x}</li>" for x in xs) + "</ol>"
FR = lambda *xs: {k: f"\\({v}\\)" for k, v in zip("ABCDE", xs)}


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


def X(n, materia, assunto, expl, imagens=(), tags=(), enun=None, trocas=(), alts=None, anulacao=None, quim=False):
    e = LIMPA(enun or E(n))
    if quim: e = QF(e)
    for a, b in trocas:
        assert a in e, a; e = e.replace(a, b)
    Q[n] = {"materia": materia, "assunto": assunto, "area": "Ciências da Natureza", "tags": list(tags), "numeroOriginal": n,
                 "enunciado": e, "alternativas": {k: (QF if quim else str)(LIMPA(v)) for k, v in dict(alts or D[n]["alternativas"]).items()},
                 "imagens": list(imagens), "explicacao": expl}
    if anulacao: Q[n]["anulacao"] = anulacao


SUB = lambda s: re.sub(r"(?<=[A-Za-z\)])(\d+)", r"<sub>\1</sub>", s)
LISTA = lambda s: "<ul>" + "".join(f"<li>{x.strip()}</li>" for x in s.split("•") if x.strip()) + "</ul>"
EQ = lambda *xs: '<p class="apoio">' + "<br>".join(xs) + "</p>"
SUP = lambda s: s.replace("m/s2", "m/s<sup>2</sup>").replace("g/cm3", "g/cm<sup>3</sup>").replace("mm3", "mm<sup>3</sup>")

CAP = lambda x: f'<p class="apoio" style="text-align:center">{x}</p>'
L = lambda s: s.replace("m�", "mL").replace("mol/�", "mol/L").replace("mg/�", "mg/L")


NAO_QUIM = {"L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8", "E1", "E2", "E3"}


def QF(s):
    """Índices químicos: CO2 → CO<sub>2</sub>, Cu2+ → Cu<sup>2+</sup> (só em texto, fora de tags)."""
    s = re.sub(r"\b(Cu|Zn|Fe|Pb|Ni)2\+", r"\1<sup>2+</sup>", s)
    def tok(m):
        t = m.group(0)
        if t in NAO_QUIM or not re.fullmatch(r"(?:[A-Z][a-z]?\d*|\((?:[A-Z][a-z]?\d*)+\)\d*)+", t): return t
        return re.sub(r"(?<=[A-Za-z\)])(\d+)", r"<sub>\1</sub>", t)
    partes = re.split(r"(<[^>]+>)", s)
    return "".join(x if x.startswith("<") else re.sub(r"(?<![\w/])(?=[A-Z(])[A-Za-z0-9()]*\d[A-Za-z0-9()]*(?![\w])", tok, x) for x in partes)

MENOS = lambda s: s.replace("-1", "<sup>−1</sup>").replace("-3", "<sup>−3</sup>")
TBL = lambda *a: tabela(*a)

X(1, "Biologia", "Ecologia", "<p>O texto aponta o desmatamento como fator recente de aumento do CO<sub>2</sub> na atmosfera. A vegetação retira CO<sub>2</sub> do ar na fotossíntese; reduzir o desmatamento mantém esse sumidouro funcionando. Alternativa <strong>C</strong>.</p><p>Queimar biomassa (B) libera mais gases; aumentar o vapor de água (D) reforçaria o efeito estufa; e reduzir o calor irradiado pela Terra (A) não é algo que se controle com industrialização.</p>",
  tags=["efeito estufa", "desmatamento"], quim=True,
  enun=ap(T(1, 0) + " " + T(1, 1)) + ap(T(1, 2) + " " + T(1, 3) + " " + T(1, 4)) + fonte(T(1, 5)) + p(T(1, 6)))
X(2, "Biologia", "Fisiologia humana", "<p>O gráfico mostra várias curvas de concentração de álcool no sangue ao longo do tempo: cada curva começa num pico diferente (doses diferentes) e cai até zero em tempos diferentes. Ele representa quanto tempo o organismo leva para metabolizar diferentes quantidades de álcool. Alternativa <strong>D</strong>.</p><p>Não há “hora do dia” no eixo, só tempo depois da ingestão, e não há uma média única (A, E).</p>",
  figs(("q2", "Gráfico da concentração de álcool no sangue (mg%) em função do tempo (horas), de 0 a 8 h, com quatro curvas: todas sobem rápido e depois descem; a maior chega a cerca de 85 mg% e zera perto de 7 h, a menor chega a cerca de 18 mg% e zera perto de 2 h. Uma linha tracejada marca 50 mg%.")),
  ["metabolismo do álcool", "leitura de gráfico"])
X(3, "Biologia", "Imunologia", "<p>Vacinas induzem o organismo a produzir sua própria defesa (anticorpos e células de memória) antes do contato com o agente. Uma vacina eficiente contra o HIV deveria induzir essa imunidade e proteger contra a infecção. Alternativa <strong>A</strong>.</p><p>Vacina não altera o genoma (B), não produz antígenos que bloqueiam o vírus (C, quem faz isso são os anticorpos), e o HIV não é transmitido por animais (D) nem por saliva (E).</p>",
  tags=["vacina", "HIV"])
X(4, "Biologia", "Genética", "<p>As plantas vieram da mesma planta por clonagem: o genótipo é idêntico em todas. A cor das folhas mudou por causa do ambiente (sem luz não há clorofila), então os fenótipos são diferentes. Fenótipo = genótipo + ambiente. Alternativa <strong>B</strong>.</p>",
  tags=["genótipo e fenótipo", "clonagem"])
X(5, "Física", "Gravitação", "<p>Kepler partiu de anos de observação de Marte e chegou a uma conclusão (órbitas elípticas) que pôde ser testada e estendida aos outros planetas: é o método científico. Alternativa <strong>E</strong>.</p><p>Uma ideia não vale mais por ser antiga (A); Copérnico viveu antes do “Rei Sol” (B), num tempo em que a Igreja controlava a pesquisa (C); a Alemanha nem existia como país unificado (D).</p>",
  tags=["história da ciência", "leis de Kepler"], trocas=[("(1571- 1630)", "(1571-1630)")])
X(6, "Biologia", "Ecologia", "<p>Os combustíveis fósseis guardam carbono retirado da atmosfera há milhões de anos. Queimá-los libera esse carbono como CO<sub>2</sub>, aumentando a quantidade de carbono na atmosfera mais rápido do que os outros compartimentos conseguem absorver. Alternativa <strong>D</strong>.</p>",
  tags=["ciclo do carbono", "combustíveis fósseis"], quim=True)
X(7, "Biologia", "Biotecnologia", "<p>A bactéria modificada produz insulina humana em mais quantidade e em menos tempo, o que barateia e amplia o acesso ao hormônio. A consequência direta é um impacto favorável na saúde de quem tem diabetes. Alternativa <strong>D</strong>.</p><p>A técnica substitui, e não aperfeiçoa, a extração do pâncreas suíno (A); não envolve animais transgênicos (E) nem síntese química (C).</p>",
  tags=["DNA recombinante", "insulina"])
X(8, "Biologia", "Ecologia", "<p>Uma hidrelétrica represa o rio e alaga uma grande área. Numa região de rios cercados por mata, o lago destrói o habitat de animais terrestres. Alternativa <strong>B</strong>.</p><p>A usina não emite muito CO<sub>2</sub> (C, típico de termelétrica), a água não é consumida nas turbinas (D) e a represa faz o rio depositar mais sedimentos antes da barragem, não menos (E).</p>",
  tags=["hidrelétrica", "impacto ambiental"])
X(9, "Biologia", "Ecologia", "<p>Nos períodos glaciais o clima ficava mais seco: as florestas encolhiam e os ambientes abertos se expandiam. Plantas com adaptações à aridez, como estruturas que reduzem a perda de água, ocupavam áreas maiores. Alternativa <strong>D</strong>.</p><p>O texto diz o contrário de A e E: quem ficava em refúgios eram as florestas.</p>",
  tags=["paleoclima", "biomas"])
X(10, "Biologia", "Fisiologia vegetal", "<p>A fotossíntese é o único processo que converte energia do Sol em energia química, e todos os seres vivos dependem dessa energia guardada nos carboidratos. Logo, a vida na Terra depende, em última análise, do Sol. Alternativa <strong>C</strong>.</p><p>CO<sub>2</sub> e água são pobres em energia (A); quem converte energia são os cloroplastos, não os carboidratos (B); a respiração libera carbono, não retira (D).</p>",
  tags=["fotossíntese", "fluxo de energia"], quim=True)
X(11, "Biologia", "Fisiologia humana", "<p>O hipotálamo, parte do sistema nervoso, controla a temperatura do corpo. No calor, ele ativa a sudorese: o suor evapora e leva calor da pele. Alternativa <strong>C</strong>.</p><p>Anticorpos são do sistema imunológico, não do endócrino (E), e os outros sistemas citados não regulam a temperatura.</p>",
  tags=["termorregulação", "sudorese"])
X(12, "Química", "Equilíbrio químico", "<p>O equilíbrio produz OH<sup>−</sup>. Se o meio for básico (muito OH<sup>−</sup>), o equilíbrio é deslocado para a esquerda (princípio de Le Chatelier): sobra mais ânion do sabão e menos ácido carboxílico, que é pouco eficiente. Os sabões funcionam melhor em pH básico. Alternativa <strong>A</strong>.</p><p>Em meio ácido, o H<sup>+</sup> consome o OH<sup>−</sup> e o equilíbrio vai para a direita, o que se quer evitar.</p>",
  figs(("q12", "Fórmula de um sal de ácido carboxílico: longa cadeia em zigue-zague de carbonos terminada em CO<sub>2</sub><sup>−</sup>Na<sup>+</sup>.")),
  ["deslocamento de equilíbrio", "sabões"],
  enun=p(T(12, 0)) + "[[fig:1]]" + p(T(12, 2)) + CAP("CH<sub>3</sub>(CH<sub>2</sub>)<sub>16</sub>COO<sup>−</sup> + H<sub>2</sub>O ⇌ CH<sub>3</sub>(CH<sub>2</sub>)<sub>16</sub>COOH + OH<sup>−</sup>") + p(T(12, 4), T(12, 5)))
X(13, "Biologia", "Ecologia", "<p>O texto reconhece os dois lados: estradas integram as comunidades, mas fragmentam habitats. A saída equilibrada é permitir as obras quando forem necessárias e depois de estudos que mostrem como evitar ou compensar os impactos. Alternativa <strong>D</strong>.</p><p>Proibir tudo (A, B) ignora o benefício social; dizer que os impactos são temporários e reversíveis (E) contraria o texto.</p>",
  tags=["impacto ambiental", "desenvolvimento sustentável"])
X(14, "Física", "Energia", "<p>A eficiência geral é o produto das etapas: 0,35 × 0,90 × 0,05. A etapa mais fraca é a lâmpada (5%), e as linhas também perdem energia. Usar condutores melhores nas linhas e lâmpadas fluorescentes, que convertem muito mais energia em luz, eleva o produto. Alternativa <strong>E</strong>.</p><p>Mais combustível (A) não muda a eficiência; lâmpadas incandescentes geram muito calor (B); cabos mais finos aumentam a perda (D).</p>",
  figs(("q14", "Esquema de usina de força (E1 = 0,35), linhas de transmissão (E2 = 0,90) e lâmpada numa casa (E3 = 0,05); eficiência geral da conversão de energia química em luminosa = E1 × E2 × E3 = 0,35 × 0,90 × 0,05 = 0,016, ou 1,6%.")),
  ["eficiência energética", "transmissão de energia"])
X(15, "Química", "Eletroquímica", "<p>Os metais com maior força redutora que o cobre (chumbo, níquel e zinco) se oxidam no ânodo e passam para a solução. Os de menor força redutora (ouro, platina e prata) não se oxidam e se depositam abaixo do ânodo, como lama anódica. Alternativa <strong>B</strong>.</p>",
  figs(("q15", "Série de metais em ordem de força redutora crescente, de cima para baixo: ouro, platina, prata, cobre, chumbo, níquel e zinco; uma seta para baixo indica o aumento da força redutora.")),
  ["eletrólise", "refino do cobre"], quim=True)
X(16, "Biologia", "Genética", "<p>No esquema, um único RNA dá origem a três proteínas diferentes (a, b e c). Ou seja, a partir do mesmo produto da transcrição é possível obter variantes de proteínas (como no processamento alternativo do RNA). Alternativa <strong>D</strong>.</p><p>A seta dupla entre DNA e RNA mostra que o fluxo não é só de mão única (B).</p>",
  figs(("q16", "Esquema: o DNA com uma seta circular de replicação; seta dupla entre DNA e RNA indicando transcrição; do RNA, três setas de tradução para proteína “a”, proteína “b” e proteína “c”.")),
  ["síntese proteica", "transcrição e tradução"])
X(17, "Física", "Movimento circular", "<p>Velocidade média: 403 km em 1 h 25 min (≈ 1,42 h), cerca de 284 km/h ≈ 79 m/s. A aceleração lateral é centrípeta: a = v²/R, com a = 0,1 × 10 = 1 m/s². R = 79² ÷ 1 ≈ 6 240 m: o raio mínimo fica perto de 6 400 m. Alternativa <strong>E</strong>.</p>",
  tags=["aceleração centrípeta", "velocidade média"], trocas=[("m/s2", "m/s<sup>2</sup>")])
X(18, "Física", "Eletricidade", "<p>Para saber quantos aparelhos manter a temperatura, é preciso comparar o calor gerado pelas pessoas com a capacidade de refrigeração de cada modelo. Para dimensionar a espessura dos fios, é preciso saber a corrente elétrica que os aparelhos puxam. Alternativa <strong>E</strong>.</p><p>A frequência (D) é a mesma em todos os modelos e não influencia nem uma coisa nem outra.</p>",
  tags=["potência e corrente", "refrigeração"],
  enun=p(T(18, 0).replace("ar- condicionado", "ar-condicionado"))
       + TBL(["Capacidade de refrigeração kW/(BTU/h)", "Potência (W)", "Corrente elétrica - ciclo frio (A)", "Eficiência energética COP (W/W)", "Vazão de ar (m<sup>3</sup>/h)", "Frequência (Hz)"],
             [["3,52/(12.000)", "1.193", "5,8", "2,95", "550", "60"], ["5,42/(18.000)", "1.790", "8,7", "2,95", "800", "60"], ["5,42/(18.000)", "1.790", "8,7", "2,95", "800", "60"],
              ["6,45/(22.000)", "2.188", "10,2", "2,95", "960", "60"], ["6,45/(22.000)", "2.188", "10,2", "2,95", "960", "60"]])
       + fonte("Disponível em: http://www.institucional.brastemp.com.br. Acesso em: 13 jul. 2009 (adaptado).") + p(T(18, 3).replace("ar- condicionado", "ar-condicionado")))
_t19 = T(19, 1)
X(19, "Física", "Eletricidade", "<p>Aparelhos: 120 + 3 000 + 500 + 200 + 200 + 50 = 4 070 W. Lâmpadas, pela área de cada cômodo: cozinha 3 × 3 = 9 m² (100 W); banheiro 1,5 × 2,1 = 3,15 m² (60 W); quarto 2,8 × 3 = 8,4 m² (100 W); corredor 1,5 × 0,9 = 1,35 m² (60 W), somando 320 W. Total: 4 070 + 320 = <strong>4 390 W</strong>. Alternativa <strong>D</strong>.</p>",
  figs(("q19", "Planta baixa: à esquerda, cozinha de 3 m por 3 m com geladeira, fogão, ferro elétrico, rádio e uma lâmpada; no meio, banheiro de 1,5 m de largura e 2,1 m de profundidade com chuveiro elétrico e lâmpada, e abaixo dele um corredor com lâmpada; à direita, quarto de 2,8 m por 3 m com televisor, aparelho de som e lâmpada.")),
  ["potência elétrica", "área"],
  enun=p(T(19, 0)) + TBL(["Aparelhos", "Potência (W)"], [["Aparelho de som", "120"], ["Chuveiro elétrico", "3.000"], ["Ferro elétrico", "500"], ["Televisor", "200"], ["Geladeira", "200"], ["Rádio", "50"]])
       + fonte(_t19[_t19.index("*Eletrodutos"):_t19.index(" A escolha")]) + p(_t19[_t19.index("A escolha"):].replace("m2", "m<sup>2</sup>"))
       + TBL(["Área do cômodo (m<sup>2</sup>)", "Sala/copa/cozinha (W)", "Quarto, varanda e corredor (W)", "Banheiro (W)"], [["Até 6,0", "60", "60", "60"], ["6,0 a 7,5", "100", "100", "60"], ["7,5 a 10,5", "100", "100", "100"]])
       + "[[fig:1]]" + fonte(T(19, 5)) + p(T(19, 6)))
X(20, "Física", "Termodinâmica", "<p>Os gases quentes que saem pela chaminé levam energia que hoje é desperdiçada. Aproveitar esse calor para mover outro gerador aumenta a energia elétrica obtida com o mesmo combustível. Alternativa <strong>E</strong>.</p><p>Reduzir combustível (A) reduz a geração; menos água no condensador (B) ou dutos que perdem mais calor (D) pioram o rendimento.</p>",
  figs(("q20", "Diagrama de uma usina: combustível e ar entram na caldeira, que produz vapor; o vapor move a turbina ligada ao gerador de eletricidade; o vapor é condensado com água fria vinda de um lago e devolvida quente; uma bomba devolve a água líquida à caldeira; gases da combustão saem pela chaminé.")),
  ["rendimento", "usina termelétrica"])
X(21, "Biologia", "Reprodução", "<p>No ser humano, o organismo adulto é diploide (2n) e produz gametas haploides (n) por meiose. A fecundação forma o zigoto (2n), que cresce por mitose até virar adulto. O esquema certo é o C. Alternativa <strong>C</strong>.</p><p>O esquema A, com esporófito e gametófito, é de plantas; nos outros, a meiose ou a mitose está no lugar trocado, ou o zigoto aparece haploide.</p>",
  figs(("q21a", "Ciclo A: zigoto (2n) vira esporófito (2n), que por meiose forma esporos (n); esporos formam o gametófito (n), que produz gametas (n); a fecundação forma o zigoto."),
       ("q21b", "Ciclo B: organismo adulto (2n) forma gametas (n) por mitose; fecundação forma zigoto (n); zigoto vira adulto por meiose."),
       ("q21c", "Ciclo C: organismo adulto (2n) forma gametas (n) por meiose; fecundação forma zigoto (2n); zigoto vira adulto por mitose."),
       ("q21d", "Ciclo D: organismo adulto (2n) forma gametas (n) por mitose; fecundação forma zigoto (2n); zigoto vira adulto por meiose."),
       ("q21e", "Ciclo E: organismo adulto (2n) forma gametas (n) por meiose; fecundação forma zigoto (n); zigoto vira adulto por mitose.")),
  ["ciclo de vida", "meiose e mitose"], enun=p(T(21, 0), T(21, 1)) + fonte(T(21, 7)), alts=ALT(1))
X(22, "Biologia", "Fisiologia humana", "<p>Na iontoforese, uma corrente elétrica fraca leva o medicamento pela pele direto ao local que precisa ser tratado. Como o remédio não se espalha pelo corpo todo, como ocorre na via oral, os efeitos colaterais diminuem. Alternativa <strong>D</strong>.</p><p>O texto diz que a técnica é indolor e não invasiva (A, B), e a figura mostra a eletrosmose levando também moléculas sem carga (E).</p>",
  figs(("q22", "Duas ilustrações da pele com eletrodos ligados a uma bateria. A, eletrorrepulsão: o eletrodo de mesmo sinal empurra o medicamento carregado pela pele até o vaso sanguíneo. B, eletrosmose: o fluxo de solvente entre os eletrodos arrasta o medicamento para dentro da pele.")),
  ["iontoforese", "absorção de medicamentos"])
X(23, "Química", "Química ambiental", "<p>A pergunta pede uma medida que acabe definitivamente com o problema. Enquanto as pilhas tiverem cádmio, chumbo e mercúrio, sempre haverá risco de descarte errado. Substituir esses metais por substâncias menos nocivas e não bioacumulativas elimina a causa. Alternativa <strong>E</strong>.</p><p>As medidas de coleta e devolução (C, D) reduzem o problema, mas não o eliminam.</p>",
  tags=["metais pesados", "descarte de pilhas"],
  enun=ap(T(23, 0)) + ap(T(23, 1) + " " + T(23, 2)) + fonte(T(23, 3)) + p(T(23, 4)))
X(24, "Física", "Termologia", "<p>No gráfico, quando a temperatura sobe ao longo do dia, a umidade relativa cai, e à noite acontece o contrário. A temperatura sobe por causa da insolação; logo, a insolação provoca variação da umidade relativa. Alternativa <strong>A</strong>.</p><p>A umidade relativa é inversa à temperatura nesse caso, não direta (C), e é uma razão, não uma quantidade absoluta de vapor (D).</p>",
  figs(("q24", "Gráfico de 0 a 24 horas com duas curvas: umidade relativa (eixo da esquerda, de 50% a 80%) e temperatura (eixo da direita, de −2 °C a 16 °C). A umidade fica perto de 70% de madrugada e cai até cerca de 48% por volta das 16 h; a temperatura faz o inverso, subindo até cerca de 11 °C à tarde.")),
  ["umidade relativa", "temperatura"])
X(25, "Biologia", "Saúde e doenças", "<p>Sensibilidade = positivos entre os infectados = 45 ÷ 50 = 90%: a cada 100 infectados, o teste classifica 90 como positivos. Alternativa <strong>B</strong>.</p><p>Os falsos positivos são 38, não 5 (A); a especificidade é 912 ÷ 950 = 96%, ou seja, 96 em cada 100 não infectados dão negativo, não positivo (C).</p>",
  tags=["sensibilidade e especificidade", "teste diagnóstico"],
  enun=p(T(25, 0)) + TBL(["Resultado do teste", "Condição real: infectado", "Condição real: não infectado", "Total"], [["positivo", "45", "38", "83"], ["negativo", "5", "912", "917"], ["total", "50", "950", "1.000"]]) + fonte(T(25, 3)) + p(T(25, 4)))
X(26, "Química", "Química ambiental", "<p>Os ácidos fortes da lista são o H<sub>2</sub>SO<sub>4</sub> (sulfúrico) e o HNO<sub>3</sub> (nítrico); H<sub>2</sub>CO<sub>3</sub>, HNO<sub>2</sub> e H<sub>2</sub>SO<sub>3</sub> são ácidos fracos. Os fortes se ionizam quase totalmente e são os que mais baixam o pH da chuva. Alternativa <strong>D</strong>.</p>",
  tags=["chuva ácida", "força dos ácidos"], quim=True)
X(27, "Física", "Gravitação", "<p>Em órbita, o telescópio continua sujeito à gravidade da Terra: a 560 km de altura, o peso dele ainda é quase 85% do que seria na superfície. É justamente essa força-peso que o mantém em órbita, fazendo o papel de força centrípeta. A frase não se justifica. Alternativa <strong>D</strong>.</p><p>A sensação de “sem peso” vem de tudo estar em queda livre junto, e não da falta de gravidade (A).</p>",
  figs(("q27", "Fotografia de um astronauta em traje espacial trabalhando junto ao telescópio Hubble, em órbita.")),
  ["peso e massa", "órbita"])
X(28, "Biologia", "Ecologia", "<p>A área está quase toda desmatada, então recebe luz direta. As espécies que se desenvolvem bem ao sol pleno (pioneiras), como 2, 3 e 5, são as indicadas para começar o reflorestamento; depois de formada a sombra, entram as de sombra. Alternativa <strong>B</strong>.</p><p>A espécie 8 é ruim ao sol (A), e a área desmatada não tem dossel fechado (E).</p>",
  tags=["sucessão ecológica", "espécies pioneiras"],
  enun=p(T(28, 0)) + TBL(["Espécie", "Sol pleno", "Sombreamento 30%", "Sombreamento 50%", "Sombreamento 90%"],
       [["1", "Razoável", "Bom", "Razoável", "Ruim"], ["2", "Bom", "Razoável", "Ruim", "Ruim"], ["3", "Bom", "Bom", "Razoável", "Ruim"], ["4", "Bom", "Bom", "Bom", "Bom"], ["5", "Bom", "Razoável", "Ruim", "Ruim"],
        ["6", "Ruim", "Razoável", "Bom", "Bom"], ["7", "Ruim", "Ruim", "Ruim", "Razoável"], ["8", "Ruim", "Ruim", "Razoável", "Ruim"], ["9", "Ruim", "Razoável", "Bom", "Bom"], ["10", "Razoável", "Razoável", "Razoável", "Bom"]])
       + p("Para o reflorestamento da região desmatada,"))
X(29, "Química", "Atomística", "<p>No gráfico, para Z = 50, os núcleos estáveis ficam entre N ≈ 62 e N ≈ 74. Isso dá de 12 a 24 nêutrons a mais que o número de prótons. Alternativa <strong>D</strong>.</p><p>Só os núcleos leves ficam perto da reta N = Z (B); núcleos maiores precisam de mais nêutrons para serem estáveis.</p>",
  figs(("q29", "Gráfico do número de nêutrons (N, de 0 a 150) em função do número de prótons (Z, de 0 a 110), com os núcleos estáveis marcados como uma faixa de pontos que começa sobre a reta N = Z e se afasta dela para cima à medida que Z cresce.")),
  ["isótopos", "estabilidade nuclear"])
X(30, "Física", "Eletricidade", "<p>Calor para aquecer a água: 200 000 g × 4,19 × 35 ≈ 29 330 kJ. Potência do resistor: P = U²/R = 110² ÷ 11 = 1 100 W. Tempo: 29 330 000 ÷ 1 100 ≈ 26 700 s ≈ 7,4 h. O gerador gasta 1 L por hora, ou seja, cerca de 7 L, contra 1 L na queima direta: sete vezes mais. Alternativa <strong>D</strong>.</p>",
  tags=["potência elétrica", "calorimetria"], trocas=[("J g-1 °C-1", "J g<sup>−1</sup> °C<sup>−1</sup>")])
X(31, "Física", "Ondulatória", "<p>Se a intensidade de transmissão e o nível de recepção são os mesmos, a área coberta por cada antena depende de como a intensidade diminui com a distância. No modelo da questão, essa queda é igual para as duas tecnologias, qualquer que seja a frequência. Então o número de antenas seria o mesmo. Alternativa <strong>E</strong>.</p><p>GSM tem frequência maior e comprimento de onda menor (A), e as duas ondas viajam à mesma velocidade, a da luz (C).</p>",
  tags=["ondas eletromagnéticas", "frequência"])
X(32, "Física", "Física moderna", "<p>A radiação descrita é o raio X. Os ossos têm muito cálcio, que absorve mais raio X que os átomos leves dos tecidos moles (carbono, hidrogênio, oxigênio). Onde há osso, chega menos radiação ao filme, que fica claro. Alternativa <strong>B</strong>.</p><p>A radiação não transforma cálcio em fósforo (A), e o filme claro indica absorção, não refração (D).</p>",
  figs(("q32", "Radiografia do pescoço de perfil, com as vértebras cervicais e o crânio em tom claro e os tecidos moles em tom escuro.")),
  ["raio X", "absorção de radiação"])
X(33, "Biologia", "Evolução", "<p>Ratos com pelagem parecida com o solo ficam menos visíveis aos predadores e sobrevivem e se reproduzem mais. Com o tempo, cada população fica com a cor do seu solo. Isso é seleção natural. Alternativa <strong>C</strong>.</p><p>Herança de caracteres adquiridos (E) é a ideia de Lamarck, rejeitada; a alimentação não muda genes (A).</p>",
  figs(("q33", "Mapa do sudeste dos Estados Unidos com pontos de coleta, do Alabama à Flórida, ligados a peles de ratos e amostras do solo de cada local: as peles e os solos vão do escuro, no interior, ao claro, no litoral.")),
  ["seleção natural", "camuflagem"], trocas=[("Peromyscus polionotus", "<em>Peromyscus polionotus</em>")])
X(34, "Biologia", "Ecologia", "<p>A compostagem é feita por microrganismos decompositores, e eles precisam de água para viver e agir. Se o composto não for umedecido, a decomposição para. Alternativa <strong>C</strong>.</p><p>Mau cheiro e ação de microrganismos sem oxigênio (A, E) aparecem com excesso de água, não com falta.</p>",
  tags=["compostagem", "decomposição"])
X(35, "Física", "Calorimetria", "<p>Calor para a água: Q = 1 000 kg × 4 200 × 80 = 3,36 × 10<sup>8</sup> J em uma hora, ou cerca de 93 300 W. Cada metro de refletor tem 6 m² e capta 6 × 800 = 4 800 W. Comprimento: 93 300 ÷ 4 800 ≈ 19,4 m, entre 15 m e 21 m. Alternativa <strong>A</strong>.</p>",
  figs(("q35", "Fotografia de uma fileira de longos espelhos parabólicos de uma usina termossolar, com o tubo receptor no foco.")),
  ["potência", "energia solar"],
  trocas=[("watts/m2", "watts/m<sup>2</sup>"), ("1 cal g-1 ºC-1 = 4.200 J kg-1 ºC-1", "1 cal g<sup>−1</sup> ºC<sup>−1</sup> = 4.200 J kg<sup>−1</sup> ºC<sup>−1</sup>"), ("1 m3", "1 m<sup>3</sup>")])
X(36, "Química", "Química orgânica", "<p>A molécula precisa de: anel aromático conjugado com a carbonila (alternância de ligações simples e duplas do anel até o C=O) e uma ponta apolar longa. A estrutura E tem os dois: anel ligado à dupla C=C conjugada com o éster e uma cadeia carbônica ramificada. Alternativa <strong>E</strong>.</p><p>A não tem cadeia apolar (é um ácido); B não tem anel; C não tem carbonila; em D a ligação entre anel e carbonila é simples, sem conjugação.</p>",
  figs(("q36a", "Estrutura A: anel benzênico com grupo CH<sub>3</sub>O, ligado a uma dupla C=C e a um grupo carboxila (COOH)."),
       ("q36b", "Estrutura B: cadeia aberta com uma dupla C=C conjugada a um éster, cuja outra ponta é uma cadeia ramificada; não há anel."),
       ("q36c", "Estrutura C: anel benzênico com CH<sub>3</sub>O, ligado a uma dupla C=C e a uma longa cadeia ramificada; não há carbonila."),
       ("q36d", "Estrutura D: anel benzênico com CH<sub>3</sub>O, ligado por duas ligações simples a um éster com cadeia ramificada."),
       ("q36e", "Estrutura E: anel benzênico com CH<sub>3</sub>O, ligado a uma dupla C=C conjugada a um éster com cadeia ramificada.")),
  ["conjugação", "polaridade"],
  enun=ap(T(36, 0)) + p("De acordo com as considerações do texto, qual das moléculas apresentadas a seguir é a mais adequada para funcionar como molécula ativa de protetores solares?"), alts=ALT(1))
X(37, "Física", "Óptica", "<p>Sem os cones, a pessoa só usa os bastonetes, que percebem a intensidade da luz, mas não a cor. O objeto iluminado pela luz vermelha reflete essa luz, e ela é percebida só como um nível de claridade: cinza. Alternativa <strong>D</strong>.</p>",
  tags=["visão", "cones e bastonetes"])
X(38, "Física", "Termologia", "<p>Dilatação: ΔV = V₀ · γ · Δθ = 20 000 × 10<sup>−3</sup> × 30 = 600 L a mais por dia. Vendidos a R$ 1,60: R$ 960 por dia; em uma semana, 7 × 960 = R$ 6 720, entre R$ 6.000,00 e R$ 6.900,00. Alternativa <strong>D</strong>.</p>",
  tags=["dilatação volumétrica"], trocas=[("1×10-3 ºC-1", "1×10<sup>−3</sup> ºC<sup>−1</sup>")])
X(39, "Física", "Termodinâmica", "<p>O calor flui sozinho do quente para o frio. Na geladeira, ele vai do interior frio para o exterior quente, o que não é espontâneo e exige trabalho do compressor. Alternativa <strong>B</strong>.</p><p>O calor cedido ao exterior é maior que o retirado, porque inclui o trabalho do compressor (C); quanto pior o isolamento, menor a eficiência (D).</p>",
  figs(("q39", "Esquema de uma geladeira: a tubulação passa pelo compartimento do congelador, segue para o compressor e para a serpentina externa, e volta passando pela válvula de expansão.")),
  ["segunda lei da termodinâmica", "refrigerador"])
X(40, "Química", "Química e tecnologia", "<p>O texto diz que, em escala nanométrica, a matéria tem propriedades diferentes das habituais. Partículas tão pequenas podem atravessar poros e canais das células, com efeitos ainda desconhecidos sobre os seres vivos e o ambiente; por isso é preciso estudar mais. Alternativa <strong>D</strong>.</p><p>Bactérias têm cerca de um milionésimo de metro, mil vezes maiores que um nanômetro (E).</p>",
  tags=["nanotecnologia"])
X(41, "Biologia", "Genética", "<p>O texto diz que mais cópias por célula aumentam a chance de achar DNA intacto. Cada célula tem centenas de mitocôndrias, cada uma com várias cópias de DNA mitocondrial, herdado da mãe. Comparando com a mãe do casal, dá para confirmar o parentesco. Alternativa <strong>A</strong>.</p><p>A vítima é filha, então não tem cromossomo Y (D), e os autossomos estão em apenas duas cópias de cada (E).</p>",
  tags=["DNA mitocondrial", "herança materna"])
X(42, "Biologia", "Ecologia", "<p>Os efluentes têm muita matéria particulada em suspensão, que turva a água e bloqueia a luz. Sem luz, o fitoplâncton faz menos fotossíntese e a produtividade primária do ambiente marinho cai. Alternativa <strong>E</strong>.</p><p>Na nitrificação, o nitrito é o intermediário e o nitrato é o produto final, não o contrário (C).</p>",
  tags=["carcinicultura", "produtividade primária"])
X(43, "Química", "Termoquímica", "<p>Calor por mol de CO<sub>2</sub>: metano, 890 ÷ 1 = 890 kJ; butano, 2 878 ÷ 4 ≈ 720 kJ; octano, 5 471 ÷ 8 ≈ 684 kJ. Em ordem crescente: gasolina, GLP e gás natural. Alternativa <strong>A</strong>.</p><p>O número de mols de CO<sub>2</sub> é o número de carbonos da fórmula.</p>",
  tags=["entalpia de combustão", "combustíveis"],
  enun=ap(QF(T(43, 0)).replace("( 0 25 H Δ )", "(ΔH<sup>0</sup><sub>25</sub>)"))
       + TBL(["composto", "fórmula molecular", "massa molar (g/mol)", "ΔH<sup>0</sup><sub>25</sub> (kJ/mol)"], [["metano", "CH<sub>4</sub>", "16", "−890"], ["butano", "C<sub>4</sub>H<sub>10</sub>", "58", "−2.878"], ["octano", "C<sub>8</sub>H<sub>18</sub>", "114", "−5.471"]])
       + p(T(43, 3)))
X(44, "Química", "Soluções", "<p>Etanol inicial: 20% de 800 kg = 160 kg. O álcool hidratado leva 96% de 100 kg = 96 kg. Sobram 160 − 96 = 64 kg de etanol num resíduo de 800 − 100 = 700 kg. Concentração: 64 ÷ 700 ≈ 9,14%, entre 9,0% e 9,2%. Alternativa <strong>D</strong>.</p>",
  tags=["porcentagem em massa", "destilação"], enun=ap(T(44, 0)) + p(T(44, 1) + " " + T(44, 2) + " " + T(44, 3)))
X(45, "Física", "Eletricidade", "<p>Seja R a resistência de cada lâmpada. L7 + L8 (2R) em paralelo com L5 + L6 (2R) dá R; somando L4, o ramo vale 2R, em paralelo com L2 + L3 (2R). Os dois ramos têm a mesma resistência e recebem a mesma corrente: a corrente de L4 é igual à de L2 e L3. Alternativa <strong>B</strong>.</p><p>L1 recebe a corrente total, e L5 a L8 recebem metade da corrente de L4.</p>",
  figs(("q45", "Circuito com bateria E: L1 em série na saída; depois um ramo para baixo com L2 e L3 em série; em seguida L4 em série; depois outro ramo com L5 e L6 em série; por fim L7 e L8 em série fechando o circuito.")),
  ["associação de resistores", "corrente elétrica"])

completar(Q, R)
