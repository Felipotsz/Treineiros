# Enem 2007 (26/08/2007), Prova 1 — amarela: prova única de 63 questões (modelo antigo, anterior a 2009, sem divisão por áreas).
# Fonte do PDF: arquivos 'Provas_Gabaritos_ENEM_2006/2008' do usuário (ambos são esta prova). Gabarito: acervo da USP (GABARITO_ENEM_2007_AMARELA), lido duas vezes.
# Cada questão leva a grande área mais próxima (para o resultado por área). Poemas de Ferreira Gullar (Q14) e Hugo Pontes (Q48) como imagem.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, paragrafos_enem

ID = "enem-2007"
META = {"id": ID, "banca": "Enem", "ano": 2007, "titulo": "Enem 2007: Prova objetiva", "fonte": "Inep", "dataExame": "2007-08-26",
        "duracaoMinutos": 300, "area": "Prova objetiva (63 questões)", "caderno": "amarelo", "dia": 1, "fonteGabarito": {"oficial": True, "nome": "gabarito oficial do Inep, em cópia guardada pelo Instituto de Física da USP", "url": "https://fep.if.usp.br/~profis/arquivo/avaliacao/enem/provas_gabaritos/2007/GABARITO_ENEM_2007_AMARELA.pdf"}}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 64)}
D = carregar_enem("enem-2007-amarela")
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


def X(n, area, materia, assunto, expl, imagens=(), tags=(), enun=None, trocas=(), alts=None, anulacao=None, quim=False):
    e = LIMPA(enun or E(n))
    if quim: e = QF(e)
    e = re.sub(r"<((?:www\.|solar|http)[^<>]*)>", r"&lt;\1&gt;", e)
    for a, b in trocas:
        assert a in e, a; e = e.replace(a, b)
    Q[n] = {"materia": materia, "assunto": assunto, "area": AREAS[area], "tags": list(tags), "numeroOriginal": n,
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

AREAS = {"L": "Linguagens", "H": "Ciências Humanas", "N": "Ciências da Natureza", "M": "Matemática"}
J = lambda *xs: " ".join(xs)
K = lambda s: f"\\({s}\\)"
SEMHIF = lambda d: {k: re.sub(r"(\w)- (\w)", r"\1-\2", v) for k, v in d.items()}
A5 = lambda *xs: dict(zip("ABCDE", xs))
CAPA = lambda n: {k: f"[[fig:{i}]] {v}" for i, (k, v) in enumerate(zip("ABCDE", n), 1)}
ALTS = lambda n: SEMHIF(D[str(n)]["alternativas"] if str(n) in D else D[n]["alternativas"])


def SP(n, i, corte):
    """Parágrafo que juntou a referência e o comando: devolve (fonte, comando)."""
    a, b = T(n, i).split(corte, 1)
    return a + corte.strip(), b.strip()


# ---------- Questões 1 a 9 ----------
X(1, "H", "História", "Patrimônio cultural", "<p>Patrimônio imaterial é o que se transmite pelas práticas: festas, danças, saberes, tradições. O bumba-meu-boi é uma festa popular, com música, dança e teatro, recriada a cada geração. Alternativa <strong>C</strong>.</p><p>Cristo Redentor e Pelourinho são patrimônio material (construções), e as Cataratas do Iguaçu e a Esfinge são patrimônio natural e arqueológico, respectivamente.</p>",
  figs(("q01a", "Fotografia da estátua do Cristo Redentor, de braços abertos, sobre o Rio de Janeiro."), ("q01b", "Fotografia de casarões coloniais do Pelourinho, em Salvador."),
       ("q01c", "Fotografia de uma apresentação de bumba-meu-boi, com brincantes fantasiados em volta do boi."), ("q01d", "Fotografia das Cataratas do Iguaçu."), ("q01e", "Fotografia da Esfinge de Gizé, com uma pirâmide ao fundo.")),
  ["patrimônio imaterial", "cultura popular"], enun=ap(T(1, 0)) + fonte(T(1, 1)) + p(T(1, 2)) + fonte("Figuras extraídas da Internet."),
  alts=CAPA(["Cristo Redentor", "Pelourinho", "Bumba-meu-boi", "Cataratas do Iguaçu", "Esfinge de Gizé"]))
X(2, "L", "Artes", "Artes visuais", "<p>Lobato condena quem vê “anormalmente” a natureza, sob a influência das “escolas rebeldes” e de Picasso: as deformações expressionistas e cubistas que Anita Malfatti trouxe da Europa. A obra com rosto e corpo deformados e cores fortes é <em>A Boba</em>, da própria Anita. Alternativa <strong>E</strong>.</p><p>As outras obras seguem padrões acadêmicos ou realistas, como os “processos clássicos” que Lobato elogia.</p>",
  figs(("q02a", "Pintura “Nossa Senhora Auxiliadora e Dom Bosco”, de estilo religioso tradicional."), ("q02b", "Pintura “Vaso de Flores”, natureza-morta realista com rosas num vaso."),
       ("q02c", "Pintura “A Santa Ceia”, com Cristo e os apóstolos à mesa, em estilo clássico."), ("q02d", "Pintura “Acesso a Monte Serrat – Santos”, paisagem com escadaria e casa, em estilo realista."),
       ("q02e", "Pintura “A Boba”, de Anita Malfatti: mulher sentada com rosto e corpo deformados, traços angulosos e olhar de lado, em estilo expressionista.")),
  ["Anita Malfatti", "Modernismo"],
  enun=p("Sobre a exposição de Anita Malfatti, em 1917, que muito influenciaria a Semana de Arte Moderna, Monteiro Lobato escreveu, em artigo intitulado <em>Paranóia ou Mistificação</em>:") + ap(T(2, 1))
       + fonte("<em>O Diário de São Paulo</em>, dez./1917.") + p("Em qual das obras abaixo identifica-se o estilo de Anita Malfatti criticado por Monteiro Lobato no artigo?"),
  alts=CAPA(["Nossa Senhora Auxiliadora e Dom Bosco", "Vaso de Flores", "A Santa Ceia", "Acesso a Monte Serrat – Santos", "A Boba"]))
GRAC = (tit("Texto I") + ap("Agora Fabiano conseguia arranjar as idéias. O que o segurava era a família. Vivia preso como um novilho amarrado ao mourão, suportando ferro quente. Se não fosse isso, um soldado amarelo não lhe pisava o pé não. (...) Tinha aqueles cambões pendurados ao pescoço. Deveria continuar a arrastá-los? Sinha Vitória dormia mal na cama de varas. Os meninos eram uns brutos, como o pai. Quando crescessem, guardariam as reses de um patrão invisível, seriam pisados, maltratados, machucados por um soldado amarelo.")
        + fonte("Graciliano Ramos. <em>Vidas Secas</em>. São Paulo: Martins, 23.ª ed., 1969, p. 75.") + tit("Texto II")
        + ap("Para Graciliano, o roceiro pobre é um outro, enigmático, impermeável. Não há solução fácil para uma tentativa de incorporação dessa figura no campo da ficção. É lidando com o impasse, ao invés de fáceis soluções, que Graciliano vai criar <em>Vidas Secas</em>, elaborando uma linguagem, uma estrutura romanesca, uma constituição de narrador em que narrador e criaturas se tocam, mas não se identificam. Em grande medida, o debate acontece porque, para a intelectualidade brasileira naquele momento, o pobre, a despeito de aparecer idealizado em certos aspectos, ainda é visto como um ser humano de segunda categoria, simples demais, incapaz de ter pensamentos demasiadamente complexos. O que <em>Vidas Secas</em> faz é, com pretenso não envolvimento da voz que controla a narrativa, dar conta de uma riqueza humana de que essas pessoas seriam plenamente capazes.")
        + fonte("Luís Bueno. Guimarães, Clarice e antes. In: <em>Teresa</em>. São Paulo: USP, n.° 2, 2001, p. 254."))
X(3, "L", "Literatura", "Romance de 30", "<p>I está correta: o romance de 30 fez do pobre, antes pitoresco, o protagonista. II também: o texto II fala da tentativa de superar a distância entre o intelectual e o roceiro. III está errada: os romances denunciaram a situação do sertanejo, mas não mudaram sua posição social real. Alternativa <strong>D</strong>.</p>",
  tags=["Vidas Secas", "romance social"],
  enun=GRAC + p("A partir do trecho de <em>Vidas Secas</em> (texto I) e das informações do texto II, relativas às concepções artísticas do romance social de 1930, avalie as seguintes afirmativas.")
       + "<ol type=\"I\"><li>O pobre, antes tratado de forma exótica e folclórica pelo regionalismo pitoresco, transforma-se em protagonista privilegiado do romance social de 30.</li><li>A incorporação do pobre e de outros marginalizados indica a tendência da ficção brasileira da década de 30 de tentar superar a grande distância entre o intelectual e as camadas populares.</li><li>Graciliano Ramos e os demais autores da década de 30 conseguiram, com suas obras, modificar a posição social do sertanejo na realidade nacional.</li></ol>"
       + p("É correto apenas o que se afirma em"))
X(4, "L", "Língua Portuguesa", "Gêneros textuais", "<p>O texto II é crítica literária: usa linguagem predominantemente formal para discutir, na composição de <em>Vidas Secas</em>, a relação difícil entre o escritor (intelectual) e o personagem popular. Alternativa <strong>A</strong>.</p><p>Não há linguagem coloquial nem regionalista (C, E), e o autor não se dirige ao leitor (B).</p>",
  tags=["linguagem formal", "crítica literária"], enun=GRAC + p(T(4, 0)))
X(5, "M", "Matemática", "Geometria espacial", "<p>Com ripas rígidas de mesmo tamanho, só é possível montar um sólido real cujas arestas sejam todas iguais e se encontrem de modo coerente. O octaedro do desenho E tem 12 arestas iguais e pode ser construído. Alternativa <strong>E</strong>.</p><p>O cubo (A), o triângulo (B), o prisma hexagonal (C) e a figura D, como desenhados, têm ripas que passam ao mesmo tempo na frente e atrás umas das outras: são figuras impossíveis, como as de Escher.</p>",
  figs(("q05", "Litografia “Belvedere”, de Escher: edifício de vários andares com colunas que ligam a frente de um andar ao fundo do outro, criando uma construção impossível."),
       ("q05a", "Desenho A: cubo de ripas em que uma aresta da frente parece passar por trás de outra, figura impossível."),
       ("q05b", "Desenho B: triângulo de Penrose, de lados largos que se torcem de modo impossível."),
       ("q05c", "Desenho C: prisma hexagonal de ripas com encaixes contraditórios entre frente e fundo."),
       ("q05d", "Desenho D: figura de blocos largos em forma de triângulo com ripas internas que se cruzam de modo impossível."),
       ("q05e", "Desenho E: octaedro formado por ripas iguais, com dois vértices opostos e quatro no meio.")),
  ["figuras impossíveis", "poliedros"], enun=p(T(5, 0).replace("litografia Belvedere", "litografia <em>Belvedere</em>")) + "[[fig:1]]" + p(T(5, 2)), alts=ALT(2))
X(6, "N", "Biologia", "Ecologia", "<p>A campanha mostra um mico-leão-dourado atrás das grades com a frase “Nem sempre é o criminoso quem vai parar atrás das grades”: o animal é vítima do tráfico, e o crime é capturá-lo. Ela trata do comércio ilícito da fauna silvestre como ameaça à biodiversidade. Alternativa <strong>A</strong>.</p>",
  figs(("q06", "Cartaz com um mico-leão-dourado atrás de uma grade e a frase “Nem sempre é o criminoso quem vai parar atrás das grades”.")),
  ["tráfico de animais", "biodiversidade"], enun=p(T(6, 0)) + "[[fig:1]]" + fonte(SP(6, 2, "abr./2007.")[0].replace("Com Ciência Ambiental", "<em>Com Ciência Ambiental</em>")) + p(SP(6, 2, "abr./2007.")[1]))
X(7, "M", "Matemática", "Função afim", "<p>O gráfico cresce em linha reta de 239 (1983) a 461 (2007): aumento de 222 em 6 intervalos de 4 anos, ou 37 espécies a cada 4 anos. Em 2011: 461 + 37 = <strong>498</strong>. Alternativa <strong>C</strong>.</p>",
  figs(("q07", "Gráfico de barras do número de espécies ameaçadas de extinção de 1983 a 2007, a cada 4 anos, crescendo linearmente de 239 (1983) a 461 (2007).")),
  ["progressão aritmética", "leitura de gráfico"], enun=p(T(7, 0)) + "[[fig:1]]" + p(T(7, 2)))
X(8, "M", "Matemática", "Análise combinatória", "<p>Escolhe-se 1 entre os 2 cetáceos, 1 entre os 20 primatas e 1 entre os 33 roedores. Pelo princípio multiplicativo: 2 × 20 × 33 = <strong>1.320</strong>. Alternativa <strong>A</strong>.</p><p>Os outros grupos da tabela não entram na conta, porque o estudo exige exatamente uma espécie de cada um dos três grupos escolhidos.</p>",
  tags=["princípio multiplicativo"],
  enun=p(T(8, 0)) + tabela(["grupos taxonômicos", "número de espécies"], [["Artiodáctilos", "4"], ["Carnívoros", "18"], ["Cetáceos", "2"], ["Quirópteros", "103"], ["Lagomorfos", "1"], ["Marsupiais", "16"], ["Perissodáctilos", "1"], ["Primatas", "20"], ["Roedores", "33"], ["Sirênios", "1"], ["Edentados", "10"], ["Total", "209"]])
       + fonte("<em>T&amp;C Amazônia</em>, ano 1, n.o 3, dez./2003.") + p(T(8, 2)))
X(9, "N", "Biologia", "Genética de populações", "<p>O texto diz que a exploração predatória reduz o número de indivíduos e que a diversidade é essencial à adaptação. Menos árvores significa menos variabilidade genética, o que ameaça a espécie. Alternativa <strong>B</strong>.</p><p>O texto culpa a ação humana, não as causas naturais (C), e menos indivíduos reduzem a diversidade, não a aumentam (D).</p>",
  tags=["diversidade genética", "extinção"],
  enun=ap(T(9, 0)) + fonte("Internet: &lt;www.greenpeace.org.br&gt; (com adaptações).") + p("Com relação ao problema descrito no texto, é correto afirmar que"),
  alts=A5("a baixa adaptação do mogno ao ambiente amazônico é causa da extinção dessa madeira.", "a extração predatória do mogno pode reduzir o número de indivíduos dessa espécie e prejudicar sua diversidade genética.",
          "as causas naturais decorrentes das mudanças climáticas globais contribuem mais para a extinção do mogno que a interferência humana.", "a redução do número de árvores de mogno ocorre na mesma medida em que aumenta a diversidade biológica dessa madeira na região amazônica.",
          "o desinteresse do mercado madeireiro internacional pelo mogno contribuiu para a redução da exploração predatória dessa espécie."))
# ---------- Questões 10 a 30 ----------
CANA = (tit("Álcool, crescimento e pobreza") + ap("O lavrador de Ribeirão Preto recebe em média R$ 2,50 por tonelada de cana cortada. Nos anos 80, esse trabalhador cortava cinco toneladas de cana por dia. A mecanização da colheita o obrigou a ser mais produtivo. O corta-cana derruba agora oito toneladas por dia.",
        "O trabalhador deve cortar a cana rente ao chão, encurvado. Usa roupas mal-ajambradas, quentes, que lhe cobrem o corpo, para que não seja lanhado pelas folhas da planta. O excesso de trabalho causa a <em>birola</em>: tontura, desmaio, cãibra, convulsão. A fim de agüentar dores e cansaço, esse trabalhador toma drogas e soluções de glicose, quando não farinha mesmo. Tem aumentado o número de mortes por exaustão nos canaviais.",
        "O setor da cana produz hoje uns 3,5% do PIB. Exporta US$ 8 bilhões. Gera toda a energia elétrica que consome e ainda vende excedentes. A indústria de São Paulo contrata cientistas e engenheiros para desenvolver máquinas e equipamentos mais eficientes para as usinas de álcool. As pesquisas, privada e pública, na área agrícola (cana, laranja, eucalipto etc.) desenvolvem a bioquímica e a genética no país.")
        + fonte("<em>Folha de S. Paulo</em>, 11/3/2007 (com adaptações)."))
X(10, "H", "Geografia", "Agropecuária", "<p>O texto mostra os dois lados do setor: tecnologia, pesquisa e exportação, de um lado; trabalho exaustivo e mortes nos canaviais, do outro. A charge ironiza isso: com o título “o mundo de olho em nossa tecnologia”, mostra cortadores comendo com a mão. Alternativa <strong>E</strong>.</p><p>A charge não contradiz o texto (A): ela critica a mesma disparidade.</p>",
  figs(("q10", "Charge de Angeli com o título “Álcool: o mundo de olho em nossa tecnologia”: cortadores de cana comem sentados no canavial, observados por uma multidão de estrangeiros; um deles diz: “Ah, fico meio encabulado em ter de comer com a mão diante de tanta gente!”.")),
  ["trabalho no corte de cana", "charge"], enun=CANA + "[[fig:1]]" + fonte("<em>Folha de S. Paulo</em>, 25/3/2007.") + p("Confrontando-se as informações do texto com as da charge acima, conclui-se que"),
  alts=A5("a charge contradiz o texto ao mostrar que o Brasil possui tecnologia avançada no setor agrícola.", "a charge e o texto abordam, a respeito da cana-de-açúcar brasileira, duas realidades distintas e sem relação entre si.",
          "o texto e a charge consideram a agricultura brasileira avançada, do ponto de vista tecnológico.", "a charge mostra o cotidiano do trabalhador, e o texto defende o fim da mecanização da produção da cana-de-açúcar no setor sucroalcooleiro.",
          "o texto mostra disparidades na agricultura brasileira, na qual convivem alta tecnologia e condições precárias de trabalho, que a charge ironiza."))
X(11, "M", "Matemática", "Razão e proporção", "<p>Oito toneladas dão 800 litros de álcool, que custam 800 × 1,20 = R$ 960. O corta-cana ganha 8 × R$ 2,50 = R$ 20 por dia. Precisaria trabalhar 960 ÷ 20 = <strong>48 dias</strong>. Alternativa <strong>D</strong>.</p>",
  tags=["proporção", "operações"], enun=CANA + p(T(11, 0)))
X(12, "M", "Matemática", "Probabilidade", "<p>Pacientes com problemas respiratórios causados pelas queimadas: 50 idosos + 150 crianças = 200. Desses, 150 são crianças: 150 ÷ 200 = 0,75. Isso sugere reforçar a pediatria nas áreas afetadas. Alternativa <strong>E</strong>.</p><p>O espaço amostral são só os internados por causa das queimadas, não todos os pacientes.</p>",
  tags=["probabilidade condicional", "tabela"],
  enun=p(T(12, 0)) + tabela(["pacientes", "problemas respiratórios causados pelas queimadas", "problemas respiratórios resultantes de outras causas", "outras doenças", "total"], [["idosos", "50", "150", "60", "260"], ["crianças", "150", "210", "90", "450"]])
       + p("Escolhendo-se aleatoriamente um paciente internado nesse hospital por problemas respiratórios causados pelas queimadas, a probabilidade de que ele seja uma criança é igual a"))
X(13, "N", "Biologia", "Metabolismo energético", "<p>A glicose é a principal fonte de energia das células: na respiração celular ela é degradada e a energia liberada (ATP) é usada, por exemplo, na contração dos músculos. Alternativa <strong>A</strong>.</p><p>A glicose é solúvel em água (D), e o CO<sub>2</sub> da respiração não “estabiliza” o carbono atmosférico (E).</p>",
  tags=["glicose", "respiração celular"], quim=True, enun=CANA + p(T(13, 0)))
X(14, "L", "Literatura", "Poesia", "<p>O poema contrapõe o açúcar “branco e puro” do café em Ipanema ao trabalho de “homens de vida amarga e dura” em “usinas escuras”. Doçura e brancura de um lado; amargura e escuridão do outro: é a antítese da divisão social do trabalho. Alternativa <strong>E</strong>.</p><p>O dono da mercearia e o da usina (A, C) aparecem justamente como quem não fez o açúcar.</p>",
  figs(("q14", "Poema “O açúcar”, de Ferreira Gullar, em versos livres. O eu lírico observa o açúcar branco do café da manhã em Ipanema e refaz o caminho dele: não foi feito por ele, nem pelo dono da mercearia, nem pelo dono da usina, mas veio dos canaviais e foi produzido em usinas escuras por homens de vida amarga e dura.")),
  ["antítese", "Ferreira Gullar"], enun="[[fig:1]]" + fonte("Ferreira Gullar. <em>Toda Poesia</em>. Rio de Janeiro: Civilização Brasileira, 1980, p. 227-8.") + p(SP(14, 4, "p. 227-8.")[1]))
X(15, "N", "Biologia", "Energia", "<p>Em todos os caminhos do esquema há trabalho humano: cortar a cana, extrair o caldo, fabricar rapadura e açúcar, produzir etanol e alimentos industrializados. Nenhuma alternativa dispensa o trabalho para obter a energia. Alternativa <strong>D</strong>.</p><p>Só o caldo (1) é consumo quase direto; as demais exigem processamento (E).</p>",
  figs(("q15", "Esquema com quatro caminhos a partir da cana-de-açúcar até o ser humano: 1, caldo-de-cana; 2, rapadura; 3, açúcar refinado; 4, etanol, usado no transporte e na indústria para produzir alimentos industrializados.")),
  ["cadeia produtiva", "energia"], enun=p(T(15, 0)) + "[[fig:1]]" + p(T(15, 3)))
X(16, "H", "História", "Expansão marítima", "<p>O texto liga a identidade negra ao processo histórico iniciado pela chegada dos navegadores portugueses à África no século XV: comércio, tráfico, escravidão e colonização. Isso faz parte da expansão europeia do início da Idade Moderna. Alternativa <strong>D</strong>.</p><p>O texto mostra a ordem: descobrimento, comércio, tráfico, escravidão e só depois colonização (A, E).</p>",
  tags=["identidade negra", "expansão marítima"],
  enun=ap(T(16, 0)) + fonte("K. Munanga. Algumas considerações sobre a diversidade e a identidade negra no Brasil. In: <em>Diversidade na educação: reflexões e experiências</em>. Brasília: SEMTEC/MEC, 2003, p. 37.") + p(SP(16, 2, "p. 37.")[1]))
X(17, "H", "História", "Brasil Império", "<p>Singer diz que o Brasil independente seguiu exportando produtos primários com mão de obra escrava, ficou tecnicamente atrasado e dependente do exterior para bens de consumo e capitais. Ou seja, tornou-se dependente da economia europeia por industrializar-se tardiamente. Alternativa <strong>C</strong>.</p><p>O texto diz que os capitais externos permitiram iniciar a infraestrutura urbana (D).</p>",
  tags=["economia agroexportadora", "dependência"],
  enun=ap(T(17, 0), T(17, 1)) + fonte("Paul Singer. Evolução da economia e vinculação internacional. In: I. Sachs; J. Willheim; P. S. Pinheiro (Orgs.). <em>Brasil: um século de transformações</em>. São Paulo: Cia. das Letras, 2001, p. 80.") + p(SP(17, 3, "p. 80.")[1]),
  alts=ALTS(17))
X(18, "H", "História", "Brasil Império", "<p>A linha do tempo termina em 1888 com a Lei Áurea, assinada pela princesa Isabel, que aboliu a escravidão no Brasil. Alternativa <strong>D</strong>.</p><p>O primeiro passo foi o fim do tráfico (1850), antes do Ventre Livre (B); o processo levou quase 40 anos e teve forte oposição (A).</p>",
  tags=["abolição", "leis abolicionistas"],
  enun=tit("Abolição da escravatura") + tabela(["Ano", "Lei"], [["1850", "Lei Eusébio de Queirós (fim do tráfico negreiro)"], ["1871", "Lei do Ventre Livre (liberdade para os filhos de escravos nascidos a partir dessa data)"], ["1885", "Lei dos Sexagenários (liberdade para os escravos maiores de 60 anos)"], ["1888", "Lei Áurea (abolição da escravatura)"]])
       + p(T(18, 1)))
X(19, "L", "Literatura", "Modernismo", "<p>O texto de Oswald mostra a chegada desoladora (fedentina, febre amarela, gente amontoada, senzalas recém-desocupadas, feitores armados), e a pintura de Rocco mostra imigrantes cansados e carregados. Os dois retratam as dificuldades dos imigrantes ao chegar. Alternativa <strong>C</strong>.</p><p>A frase “Buenos Aires é aqui!” mostra imigrantes enganados sobre o destino, não argentinos (B).</p>",
  figs(("q19", "Pintura “Os imigrantes”, de Antonio Rocco (1910): famílias de imigrantes, com trouxas e crianças no colo, caminham cansadas em fila.")),
  ["imigração", "Oswald de Andrade"],
  enun="[[fig:1]]" + fonte("Antonio Rocco. <em>Os imigrantes</em>, 1910, Pinacoteca do Estado de São Paulo.") + ap(T(19, 2)) + fonte("Oswald de Andrade. <em>Marco Zero II – Chão</em>. Rio de Janeiro: Globo, 1991.") + p(T(19, 4)), alts=ALTS(19))
X(20, "H", "História", "República Velha", "<p>Mário diz que Drummond estava entusiasmado com a candidatura Vargas–João Pessoa, enquanto ele, que antes a desejava, agora a via “manchada” pelas alianças frágeis com oligarquias de vários estados. Simpatia de Drummond, desencanto de Mário com as composições políticas. Alternativa <strong>A</strong>.</p><p>Júlio Prestes era o candidato adversário (D), e Vargas fez muitas alianças (E).</p>",
  tags=["Aliança Liberal", "eleição de 1930"],
  enun=ap("São Paulo, 18 de agosto de 1929.", "Carlos [Drummond de Andrade],", "Achei graça e gozei com o seu entusiasmo pela candidatura Getúlio Vargas – João Pessoa. É. Mas veja como estamos... trocados. Esse entusiasmo devia ser meu e sou eu que conservo o ceticismo que deveria ser de você. (...).",
             "Eu... eu contemplo numa torcida apenas simpática a candidatura Getúlio Vargas, que antes desejara tanto. Mas pra mim, presentemente, essa candidatura (única aceitável, está claro) fica manchada por essas pazes fragílimas de governistas mineiros, gaúchos, paraibanos (...), com democráticos paulistas (que pararam de atacar o Bernardes) e oposicionistas cariocas e gaúchos. Tudo isso não me entristece. Continuo reconhecendo a existência de males necessários, porém me afasta do meu país e da candidatura Getúlio Vargas. Repito: única aceitável.", "Mário [de Andrade]")
       + fonte("Renato Lemos. <em>Bem traçadas linhas: a história do Brasil em cartas pessoais</em>. Rio de Janeiro: Bom Texto, 2004, p. 305.") + p("Acerca da crise política ocorrida em fins da Primeira República, a carta do paulista Mário de Andrade ao mineiro Carlos Drummond de Andrade revela"),
  alts=A5("a simpatia de Drummond pela candidatura Vargas e o desencanto de Mário de Andrade com as composições políticas sustentadas por Vargas.", "a veneração de Drummond e Mário de Andrade ao gaúcho Getúlio Vargas, que se aliou à oligarquia cafeeira de São Paulo.",
          "a concordância entre Mário de Andrade e Drummond quanto ao caráter inovador de Vargas, que fez uma ampla aliança para derrotar a oligarquia mineira.", "a discordância entre Mário de Andrade e Drummond sobre a importância da aliança entre Vargas e o paulista Júlio Prestes nas eleições presidenciais.",
          "o otimismo de Mário de Andrade em relação a Getúlio Vargas, que se recusara a fazer alianças políticas para vencer as eleições."))
X(21, "H", "História", "Revoluções liberais", "<p>A independência dos EUA (1776) e a Revolução Francesa (1789) se apoiaram nas ideias iluministas: igualdade, direito à vida, à liberdade e à busca da felicidade, e governo derivado dos governados. Ambas defendiam direitos essenciais à dignidade humana. Alternativa <strong>C</strong>.</p><p>A independência americana veio antes e inspirou a França, não o contrário (D).</p>",
  tags=["Iluminismo", "independência dos EUA"],
  enun=ap("Em 4 de julho de 1776, as treze colônias que vieram inicialmente a constituir os Estados Unidos da América (EUA) declaravam sua independência e justificavam a ruptura do Pacto Colonial. Em palavras profundamente subversivas para a época, afirmavam a igualdade dos homens e apregoavam como seus direitos inalienáveis: o direito à vida, à liberdade e à busca da felicidade. Afirmavam que o poder dos governantes, aos quais cabia a defesa daqueles direitos, derivava dos governados.",
             "Esses conceitos revolucionários que ecoavam o Iluminismo foram retomados com maior vigor e amplitude treze anos mais tarde, em 1789, na França.")
       + fonte("Emília Viotti da Costa. Apresentação da coleção. In: Wladimir Pomar. <em>Revolução Chinesa</em>. São Paulo: UNESP, 2003 (com adaptações).") + p("Considerando o texto acima, acerca da independência dos EUA e da Revolução Francesa, assinale a opção correta."),
  alts=A5("A independência dos EUA e a Revolução Francesa integravam o mesmo contexto histórico, mas se baseavam em princípios e ideais opostos.", "O processo revolucionário francês identificou-se com o movimento de independência norte-americana no apoio ao absolutismo esclarecido.",
          "Tanto nos EUA quanto na França, as teses iluministas sustentavam a luta pelo reconhecimento dos direitos considerados essenciais à dignidade humana.", "Por ter sido pioneira, a Revolução Francesa exerceu forte influência no desencadeamento da independência norte-americana.",
          "Ao romper o Pacto Colonial, a Revolução Francesa abriu o caminho para as independências das colônias ibéricas situadas na América."))
X(22, "H", "História", "Oriente Médio", "<p>O texto diz que a terceira guerra árabe-israelense, de 1967, ficou conhecida como Guerra dos Seis Dias “tal a rapidez da vitória de Israel”. Alternativa <strong>B</strong>.</p><p>A primeira guerra veio da recusa árabe ao plano da ONU (A); o Yom Kippur foi em 1973, e Israel existe desde 1948 (C); o cessar-fogo americano-soviético foi no Yom Kippur (D).</p>",
  tags=["conflito árabe-israelense"],
  enun=ap("Em 1947, a Organização das Nações Unidas (ONU) aprovou um plano de partilha da Palestina que previa a criação de dois Estados: um judeu e outro palestino. A recusa árabe em aceitar a decisão conduziu ao primeiro conflito entre Israel e países árabes.",
             "A segunda guerra (Suez, 1956) decorreu da decisão egípcia de nacionalizar o canal, ato que atingia interesses anglo-franceses e israelenses. Vitorioso, Israel passou a controlar a Península do Sinai. O terceiro conflito árabe-israelense (1967) ficou conhecido como Guerra dos Seis Dias, tal a rapidez da vitória de Israel.",
             "Em 6 de outubro de 1973, quando os judeus comemoravam o Yom Kippur (Dia do Perdão), forças egípcias e sírias atacaram de surpresa Israel, que revidou de forma arrasadora. A intervenção americano-soviética impôs o cessar-fogo, concluído em 22 de outubro.")
       + p("A partir do texto acima, assinale a opção correta."),
  alts=A5("A primeira guerra árabe-israelense foi determinada pela ação bélica de tradicionais potências européias no Oriente Médio.", "Na segunda metade dos anos 1960, quando explodiu a terceira guerra árabe-israelense, Israel obteve rápida vitória.",
          "A guerra do Yom Kippur ocorreu no momento em que, a partir de decisão da ONU, foi oficialmente instalado o Estado de Israel.", "A ação dos governos de Washington e de Moscou foi decisiva para o cessar-fogo que pôs fim ao primeiro conflito árabe-israelense.",
          "Apesar das sucessivas vitórias militares, Israel mantém suas dimensões territoriais tal como estabelecido pela resolução de 1947 aprovada pela ONU."))
DENG = (ap("O <em>Aedes aegypti</em> é vetor transmissor da dengue. Uma pesquisa feita em São Luís – MA, de 2000 a 2002, mapeou os tipos de reservatório onde esse mosquito era encontrado. A tabela abaixo mostra parte dos dados coletados nessa pesquisa.")
        + tabela(["tipos de reservatórios", "2000", "2001", "2002"], [["pneu", "895", "1.658", "974"], ["tambor/tanque/depósito de barro", "6.855", "46.444", "32.787"], ["vaso de planta", "456", "3.191", "1.399"], ["material de construção/peça de carro", "271", "436", "276"],
                 ["garrafa/lata/plástico", "675", "2.100", "1.059"], ["poço/cisterna", "44", "428", "275"], ["caixa d’água", "248", "1.689", "1.014"], ["recipiente natural, armadilha, piscina e outros", "615", "2.658", "1.178"], ["total", "10.059", "58.604", "38.962"]])
        + fonte("<em>Caderno Saúde Pública</em>, vol. 20, n.º 5, Rio de Janeiro, out./2004 (com adaptações). Valores: população de <em>A. aegypti</em>."))
X(23, "N", "Biologia", "Saúde e doenças", "<p>A maior parte dos mosquitos estava em tambores, tanques e depósitos de barro: 32.787 de 38.962 em 2002 (cerca de 84%). Atacar esses reservatórios primeiro reduz os focos mais rapidamente. Alternativa <strong>B</strong>.</p>",
  tags=["dengue", "leitura de tabela"], enun=DENG + p(T(23, 0)))
X(24, "M", "Matemática", "Porcentagem", "<p>De 2001 para 2002, a população caiu de 58.604 para 38.962: fator 38.962 ÷ 58.604 ≈ 0,665 (redução de cerca de 33,5%). Mantido o percentual, em 2003: 38.962 × 0,665 ≈ 25.900, maior que 20.000. Alternativa <strong>E</strong>.</p>",
  tags=["variação percentual"], enun=DENG + p(T(24, 0).replace("A. aegypti", "<em>A. aegypti</em>")))
X(25, "M", "Matemática", "Função exponencial", "<p>Uma hora e meia equivale a 1,5 meia-vida. A fração restante é (1/2)<sup>1,5</sup> = 1/(2√2) ≈ 0,35, ou seja, cerca de 35%. No gráfico, entre 1 meia-vida (50%) e 2 meias-vidas (25%), o ponto do meio fica perto de 35%. Alternativa <strong>D</strong>.</p><p>A queda não é linear: por isso não dá 37,5%, a média entre 50% e 25%.</p>",
  figs(("q25", "Gráfico da porcentagem de fármaco no organismo em função do número de meias-vidas (0 a 7): curva decrescente que começa em 100%, passa por 50% em 1, 25% em 2, 12,5% em 3 e se aproxima de zero.")),
  ["meia-vida", "decaimento exponencial"],
  enun=ap(T(25, 0).replace("meiavida", "meia-vida")) + "[[fig:1]]" + ap(T(25, 2)) + fonte("F. D. Fuchs e Cher l. Wannma. <em>Farmacologia Clínica</em>. Rio de Janeiro: Guanabara Koogan, 1992, p. 40.") + p(SP(25, 4, "p. 40.")[1]))
X(26, "L", "Língua Portuguesa", "Variação linguística", "<p>Na segunda versão, as palavras antigas foram trocadas por equivalentes atuais: constipação por resfriado, perrengue por mal, botica por farmácia, phtísica por tuberculose, gálico por sífilis, lombrigas por vermes. A estrutura das frases é a mesma: mudou o vocabulário. Alternativa <strong>A</strong>.</p>",
  tags=["variação histórica", "vocabulário"],
  enun=tit("Antigamente") + ap("Acontecia o indivíduo apanhar constipação; ficando perrengue, mandava o próprio chamar o doutor e, depois, ir à botica para aviar a receita, de cápsulas ou pílulas fedorentas. Doença nefasta era a phtísica, feia era o gálico. Antigamente, os sobrados tinham assombrações, os meninos, lombrigas (...)")
       + fonte("Carlos Drummond de Andrade. <em>Poesia completa e prosa</em>. Rio de Janeiro: Companhia José Aguilar, p. 1.184.") + p("O texto acima está escrito em linguagem de uma época passada. Observe uma outra versão, em linguagem atual.")
       + tit("Antigamente") + ap("Acontecia o indivíduo apanhar um resfriado; ficando mal, mandava o próprio chamar o doutor e, depois, ir à farmácia para aviar a receita, de cápsulas ou pílulas fedorentas. Doença nefasta era a tuberculose, feia era a sífilis. Antigamente, os sobrados tinham assombrações, os meninos, vermes (...)")
       + p("Comparando-se esses dois textos, verifica-se que, na segunda versão, houve mudanças relativas a"),
  alts=A5("vocabulário.", "construções sintáticas.", "pontuação.", "fonética.", "regência verbal."))
INDIO = (tit("O canto do guerreiro") + '<p class="apoio">Aqui na floresta<br>Dos ventos batida,<br>Façanhas de bravos<br>Não geram escravos,<br>Que estimem a vida<br>Sem guerra e lidar.<br>— Ouvi-me, Guerreiros,<br>— Ouvi meu cantar.</p>'
         + '<p class="apoio">Valente na guerra,<br>Quem há, como eu sou?<br>Quem vibra o tacape<br>Com mais valentia?<br>Quem golpes daria<br>Fatais, como eu dou?<br>— Guerreiros, ouvi-me;<br>— Quem há, como eu sou?</p>' + fonte("Gonçalves Dias.")
         + tit("Macunaíma (Epílogo)") + ap("Acabou-se a história e morreu a vitória.", "Não havia mais ninguém lá. Dera tangolomângolo na tribo Tapanhumas e os filhos dela se acabaram de um em um. Não havia mais ninguém lá. Aqueles lugares, aqueles campos, furos puxadouros arrastadouros meios-barrancos, aqueles matos misteriosos, tudo era solidão do deserto... Um silêncio imenso dormia à beira do rio Uraricoera. Nenhum conhecido sobre a terra não sabia nem falar da tribo nem contar aqueles casos tão pançudos. Quem podia saber do Herói?")
         + fonte("Mário de Andrade."))
X(27, "L", "Literatura", "Romantismo e Modernismo", "<p>No poema romântico, o guerreiro pergunta “Quem há, como eu sou?” com orgulho: o índio é herói idealizado. No epílogo de <em>Macunaíma</em>, “Quem podia saber do Herói?” fala de uma tribo extinta, de quem ninguém lembra. As perguntas expressam visões diferentes do indígena. Alternativa <strong>C</strong>.</p><p>O poema de Gonçalves Dias idealiza o índio (não é realista nem discriminatório, A e B) e não trata de extermínio (D).</p>",
  tags=["indianismo", "Macunaíma"], enun=INDIO + p(T(27, 0)))
X(28, "L", "Literatura", "Funções da linguagem", "<p>O poema traz “tacape”, palavra de origem tupi, e o texto de Mário traz “Tapanhumas” e “Uraricoera”, também de origem indígena. Os dois usam pelo menos uma palavra indígena. Alternativa <strong>C</strong>.</p><p>O poema se dirige aos guerreiros (“Ouvi-me”), então a função apelativa está presente (A); ele é em primeira pessoa, e o texto de Mário, em terceira (E).</p>",
  tags=["palavras de origem indígena", "funções da linguagem"], enun=INDIO + p("Considerando-se a linguagem desses dois textos, verifica-se que"))
X(29, "N", "Biologia", "Saúde", "<p>O texto destaca que 41,2% dos estudantes da educação básica pública já tinham consumido álcool: um dado alarmante sobre o consumo precoce, que mostra que o alcoolismo é um problema a ser enfrentado pela sociedade. Alternativa <strong>C</strong>.</p><p>A parece certa porque 7,3% é cerca do dobro de 3,5%, mas os 3,5% são de toda a indústria do álcool (do açúcar ao combustível), não só da bebida. As mulheres eram 5,7%, contra 17,1% dos homens (D).</p>",
  tags=["alcoolismo", "leitura de dados"],
  enun=ap(T(29, 0), T(29, 1)) + fonte("<em>Revista Brasileira de Psiquiatria</em>, v. 28, n.º 4, dez./2006 e Internet: &lt;www.alcoolismo.com.br&gt; (com adaptações).") + p(SP(29, 3, "(com adaptações).")[1]))
X(30, "N", "Biologia", "Saúde", "<p>A proteção vem do leite materno, e a região com maior porcentagem de aleitamento nos dois períodos (85,7% até o 4.º mês e 54,8% de 9 meses a 1 ano) é o Norte. Alternativa <strong>A</strong>.</p><p>O Centro-Oeste vem logo depois (83,9% e 47,8%); Sudeste e Sul têm as menores taxas de aleitamento prolongado.</p>",
  tags=["aleitamento materno", "anticorpos"],
  enun=p(T(30, 0)) + tabela(["região", "até o 4.º mês (em %)", "de 9 meses a 1 ano (em %)"], [["Norte", "85,7", "54,8"], ["Nordeste", "77,7", "38,8"], ["Sudeste", "75,1", "38,6"], ["Sul", "73,2", "37,2"], ["Centro-Oeste", "83,9", "47,8"]])
       + fonte("Ministério da Saúde, 2005.") + p(T(30, 3)))
# ---------- Questões 31 a 63 ----------
X(31, "N", "Biologia", "Saúde e doenças", "<p>Comparando os mapas, Minas Gerais passa de índice baixo, em 1985, para alto, em 1999: a infecção por LTA cresceu muito no estado. Alternativa <strong>A</strong>.</p><p>Os mapas não informam causas (campanhas, secas), e a leishmaniose é transmitida por mosquito-palha, não por roedor (E).</p>",
  figs(("q31", "Dois mapas do Brasil com o índice de infecção por leishmaniose tegumentar americana por estado, em 1985 e 1999 (caso não registrado, baixo, médio, alto, muito alto). Em 1999, vários estados aparecem com índices mais altos que em 1985, entre eles Minas Gerais, que passa de baixo para alto.")),
  ["leishmaniose", "leitura de mapas"], enun=p(T(31, 0)) + "[[fig:1]]" + fonte(SP(31, 2, "Ministério da Saúde.")[0]) + p(SP(31, 2, "Ministério da Saúde.")[1]))
X(32, "M", "Matemática", "Grandezas e medidas", "<p>A legenda indica os picos por região em meses: Norte em abril, Nordeste entre abril e maio, Sudeste entre junho e julho, Sul em julho. O vírus leva meses para ir do Norte ao Sul: a unidade adequada é o mês. Alternativa <strong>B</strong>.</p>",
  figs(("q32", "Mapa “O caminho do vírus – como o patógeno da gripe se espalha no Brasil”, com círculos cujo tamanho indica a intensidade da epidemia e setas do Norte para o Sul. Legenda: região Norte, pico em abril; Nordeste, entre abril e maio; Centro-Oeste, dados escassos; Sudeste, entre junho e julho; Sul, pico em julho.")),
  ["unidades de tempo", "leitura de mapa"], enun=p(T(32, 0)) + "[[fig:1]]" + fonte(T(32, 2).replace("Folha de S. Paulo", "<em>Folha de S. Paulo</em>")) + p(T(32, 3)))
X(33, "N", "Biologia", "Reprodução", "<p>A tirinha mostra bactérias se dividindo ao meio, ou seja, reprodução assexuada por divisão binária. Ela é rápida, simples e gera descendentes geneticamente iguais ao organismo original. Alternativa <strong>B</strong>.</p><p>Permuta de material genético e variabilidade (A, D) são próprias da reprodução sexuada.</p>",
  figs(("q33", "Tirinha de Fernando Gonsales em que uma bactéria sozinha reclama da solidão e, ao se dividir, passa a conversar com cópias de si mesma, até ficar cercada de bactérias iguais.")),
  ["reprodução assexuada", "bactérias"], enun="[[fig:1]]" + fonte("Fernando Gonsales. <em>Vá Pentear Macacos!</em> São Paulo: Devir, 2004.") + p(SP(33, 1, "Devir, 2004.")[1]))
X(34, "M", "Matemática", "Probabilidade", "<p>No gráfico, só a peixaria V vende peixe entre 2 °C e 4 °C (2,3 °C); as outras estão entre 8,9 °C e 14 °C. Uma em cinco: " + K("\\tfrac{1}{5}") + ". Alternativa <strong>D</strong>.</p><p>As temperaturas das outras peixarias estão muito acima do ideal, o que favorece a proliferação de bactérias.</p>",
  figs(("q34", "Gráfico de barras “Temperatura do pescado nas peixarias” (°C): I, 14,0; II, 13,2; III, 10,5; IV, 8,9; V, 2,3.")),
  ["probabilidade", "leitura de gráfico"], enun=tit("Temperatura do pescado nas peixarias") + "[[fig:1]]" + fonte("Associação Brasileira de Defesa do Consumidor (com adaptações).") + p(SP(34, 2, "(com adaptações).")[1]),
  alts=FR("\\dfrac{1}{2}", "\\dfrac{1}{3}", "\\dfrac{1}{4}", "\\dfrac{1}{5}", "\\dfrac{1}{6}"))
PROD = (tit("Aumento de produtividade") + ap("Nos últimos 60 anos, verificou-se grande aumento da produtividade agrícola nos Estados Unidos da América (EUA). Isso se deveu a diversos fatores, tais como expansão do uso de fertilizantes e pesticidas, biotecnologia e maquinário especializado. O gráfico abaixo apresenta dados referentes à agricultura desse país, no período compreendido entre 1948 e 2004.")
        + "[[fig:1]]" + fonte("<em>Scientific American Brasil</em>, jun./2007, p. 19 (com adaptações)."))
F_PROD = figs(("q35", "Gráfico das mudanças desde 1948 (%), de 1950 a 2004: a produtividade total da agricultura dos EUA cresce até cerca de 160%; os custos de material sobem até perto de 100% nos anos 1970, com oscilações; as despesas de capital sobem até cerca de 25% e depois caem; o uso da terra cai um pouco, abaixo de zero; os custos de mão de obra caem continuamente, até cerca de −75%."))
X(35, "H", "Geografia", "Agropecuária", "<p>O texto atribui o aumento da produtividade a fertilizantes, pesticidas, biotecnologia e maquinário: tecnologia. No gráfico, a produtividade sobe enquanto o uso da terra e a mão de obra caem. Alternativa <strong>E</strong>.</p><p>O uso da terra diminuiu (A), os custos de material subiram (B) e o uso de agrotóxicos aumentou (C).</p>",
  F_PROD, ["modernização agrícola", "produtividade"], enun=PROD + p(T(35, 0)))
X(36, "H", "Geografia", "Agropecuária", "<p>No gráfico, os custos de mão de obra caem para cerca de −75% em 2004, enquanto a produtividade sobe: a produtividade cresceu com redução de mais de 70% dos custos de mão de obra. Alternativa <strong>A</strong>.</p><p>A produtividade cresceu cerca de 160%, não mais de 200% (C).</p>",
  F_PROD, ["mecanização", "leitura de gráfico"], enun=PROD + p(T(36, 0)))
X(37, "M", "Matemática", "Raciocínio lógico", "<p>Na 4.ª etapa, a lata tem 900 mL e a garrafa de 800 mL tem 300 mL. Para chegar à 6.ª (lata com 100 mL, garrafa de 800 cheia e a de 500 com 300 mL), a 5.ª etapa passa os 300 mL para a garrafa de 500 mL, deixando a de 800 vazia: lata 900, garrafa de 500 com 300. Depois, enche-se a garrafa de 800 com a lata, que fica com 100 mL. Alternativa <strong>D</strong>.</p>",
  figs(("q37", "Seis etapas, a 5.ª omitida. 1.ª: lata com 1.200 mL e as duas garrafas vazias. 2.ª: lata com 400 mL e a garrafa maior cheia. 3.ª: lata com 400 mL, garrafa maior com 300 mL e a menor cheia. 4.ª: lata com 900 mL, garrafa maior com 300 mL e a menor vazia. 5.ª: interrogações. 6.ª: lata com 100 mL, garrafa maior cheia e a menor com 300 mL."),
       ("q37a", "Situação A: lata com 100 mL, garrafa maior com 700 mL e garrafa menor com 400 mL."), ("q37b", "Situação B: lata com 200 mL, garrafa maior cheia e garrafa menor com 200 mL."),
       ("q37c", "Situação C: lata com 400 mL e as duas garrafas vazias."), ("q37d", "Situação D: lata com 900 mL, garrafa maior vazia e garrafa menor com 300 mL."),
       ("q37e", "Situação E: lata com 900 mL, garrafa maior com 200 mL e garrafa menor com 100 mL.")),
  ["raciocínio lógico", "medidas de capacidade"],
  enun=p("A diversidade de formas geométricas espaciais criadas pelo homem, ao mesmo tempo em que traz benefícios, causa dificuldades em algumas situações. Suponha, por exemplo, que um cozinheiro precise utilizar exatamente 100 mL de azeite de uma lata que contenha 1.200 mL e queira guardar o restante do azeite em duas garrafas, com capacidade para 500 mL e 800 mL cada, deixando cheia a garrafa maior. Considere que ele não disponha de instrumento de medida e decida resolver o problema utilizando apenas a lata e as duas garrafas. As etapas do procedimento utilizado por ele estão ilustradas nas figuras a seguir, tendo sido omitida a 5.ª etapa.")
       + "[[fig:1]]" + p("Qual das situações ilustradas a seguir corresponde à 5.ª etapa do procedimento?"), alts=ALT(2))
X(38, "H", "Geografia", "Leitura de gráficos", "<p>O gráfico mostra a China em 1.º lugar, com 276 mil toneladas, e o Brasil em 15.º, com 33 mil toneladas. O título que corresponde ao gráfico é “China é o gigante na produção de mel no mundo e o Brasil está em 15.º lugar”. Alternativa <strong>E</strong>.</p><p>33 é a produção do Brasil, não sua posição (A).</p>",
  figs(("q38", "Gráfico de barras da produção de mel em 2005 (em milhares de toneladas) e a posição no ranking: China 1.ª, 276; EUA 2.ª, 82; Argentina 3.ª, 80; Turquia 4.ª, 75; México 5.ª, 55; ...; Brasil 15.ª, 33.")),
  ["leitura de gráfico", "título jornalístico"], enun="[[fig:1]]" + fonte("<em>Globo Rural</em>, jun./2007.") + p(T(38, 2)), alts=SEMHIF({k: v.replace("ranking", "<em>ranking</em>") for k, v in D[38]["alternativas"].items()}))
X(39, "H", "Geografia", "Mudanças climáticas", "<p>Com a subida do mar e a salinização dos rios, os fazendeiros trocaram o arroz pela criação de camarão: reestruturaram a produção para enfrentar a mudança ambiental. Alternativa <strong>C</strong>.</p><p>A nova atividade aumentou o desemprego (B) e substituiu as tradicionais (A).</p>",
  tags=["aquecimento global", "adaptação econômica"],
  enun=tit("Lucro na adversidade") + ap(T(39, 1), T(39, 2)) + fonte("<em>Globo Rural</em>, jun./2007, p. 18 (com adaptações).") + p(SP(39, 3, "(com adaptações).")[1]))
X(40, "N", "Biologia", "Ecologia", "<p>I: o aquecimento derrete o gelo marinho e aumenta a neve, alterando o ciclo da água. II: os pinguins põem ovos na neve e eles goram, afetando seu ciclo de vida. III: o gelo, a água sólida, é essencial para a vida nesses biomas polares. As três estão corretas. Alternativa <strong>E</strong>.</p>",
  tags=["aquecimento global", "ciclo da água"],
  enun=ap(T(40, 0).replace("6 oC", "6 °C"), T(40, 1)) + fonte("<em>Scientific American Brasil</em>, ano 2, n.º 21, 2004, p. 80 (com adaptações).") + p("A partir do texto acima, analise as seguintes afirmativas.")
       + '<ol type="I"><li>O aumento da temperatura global interfere no ciclo da água na península antártica.</li><li>O aquecimento global pode interferir no ciclo de vida de espécies típicas de região de clima polar.</li><li>A existência de água em estado sólido constitui fator crucial para a manutenção da vida em alguns biomas.</li></ol>' + p("É correto o que se afirma"))
X(41, "N", "Biologia", "Ecologia", "<p>Os ursos polares morrem afogados porque o gelo diminuiu: o aquecimento global ameaça espécies do Ártico e, com elas, a biodiversidade da região. Alternativa <strong>B</strong>.</p><p>O texto não fala em novas espécies (C) e mostra justamente que os animais não se adaptam rápido (E).</p>",
  tags=["biodiversidade", "aquecimento global"], enun=ap(T(41, 0).split(" A situação descrita")[0]) + p("A situação descrita acima"))
X(42, "N", "Física", "Clima", "<p>No gráfico, de 1960 a 1990, as curvas que sobem acima de zero (contribuição positiva para o aquecimento) são as dos gases estufa, do ozônio e da atividade solar. Aerossóis e atividade vulcânica contribuem para o resfriamento. Alternativa <strong>E</strong>.</p>",
  figs(("q42", "Gráfico de 1900 a 1990: em cima, a variação total da temperatura calculada, que sobe sobretudo depois de 1970; embaixo, a contribuição de cinco fatores — gases estufa, atividade solar e ozônio com contribuição positiva crescente no fim do período; aerossóis e atividade vulcânica com contribuição negativa.")),
  ["efeito estufa", "leitura de gráfico"], enun=p(T(42, 0)) + "[[fig:1]]" + fonte(T(42, 2)) + p(T(42, 3)))
X(43, "N", "Física", "Termologia", "<p>O vidro é transparente à luz visível, que entra e aquece os tanques pretos; o calor emitido por eles (infravermelho) atravessa mal o vidro e fica preso, como numa estufa. Alternativa <strong>B</strong>.</p><p>Superfícies pretas são ótimas absorvedoras (A), e a água circula por diferença de temperatura e densidade, não de energia luminosa (C).</p>",
  figs(("q43", "Aquecedor solar: caixa inclinada com vidraças duplas, dois tanques pintados de preto e camada refletiva no fundo; a água fria entra embaixo, pelo ponto X, e a água quente sai em cima, pelo ponto Y.")),
  ["efeito estufa", "aquecedor solar"],
  enun="[[fig:1]]" + ap("O uso mais popular de energia solar está associado ao fornecimento de água quente para fins domésticos. Na figura ao lado, é ilustrado um aquecedor de água constituído de dois tanques pretos dentro de uma caixa termicamente isolada e com cobertura de vidro, os quais absorvem energia solar.")
       + fonte("A. Hinrichs e M. Kleinbach. <em>Energia e meio ambiente</em>. São Paulo: Thompson, 3.ª ed., 2004, p. 529 (com adaptações).") + p("Nesse sistema de aquecimento,"))
X(44, "N", "Física", "Ondas eletromagnéticas", "<p>No gráfico, a perturbação por ondas de rádio começa logo após a explosão e dura mais que a de raios X, cuja barra é mais curta. Alternativa <strong>D</strong>.</p><p>Raios X e ondas de rádio viajam à velocidade da luz e chegam juntos (C); a tempestade magnética dura mais que a perturbação de rádio (A).</p>",
  figs(("q44", "Gráfico “Escala de tempo das perturbações solares e seus efeitos”, em escala de 1 minuto a 10 dias: raios X (primeiras alterações na ionosfera) e ondas de rádio (interferência de rádio) chegam em minutos, com a de rádio durando mais; partículas de alta energia (alteração na ionosfera polar) chegam em cerca de 1 hora e duram dias; o plasma solar (tempestade magnética) chega em 1 a 2 dias.")),
  ["ondas eletromagnéticas", "leitura de gráfico"], enun=p(T(44, 0)) + "[[fig:1]]" + fonte(T(44, 2)) + p(T(44, 3)))
FILTRO = (ap("A pele humana é sensível à radiação solar, e essa sensibilidade depende das características da pele. Os filtros solares são produtos que podem ser aplicados sobre a pele para protegê-la da radiação solar. A eficácia dos filtros solares é definida pelo fator de proteção solar (FPS), que indica quantas vezes o tempo de exposição ao sol, sem o risco de vermelhidão, pode ser aumentado com o uso do protetor solar. A tabela seguinte reúne informações encontradas em rótulos de filtros solares.")
          + tabela(["sensibilidade", "tipo de pele e outras características", "proteção recomendada", "FPS recomendado", "proteção a queimaduras"],
                   [["extremamente sensível", "branca, olhos e cabelos claros", "muito alta", "FPS ≥ 20", "muito alta"], ["muito sensível", "branca, olhos e cabelos próximos do claro", "alta", "12 ≤ FPS &lt; 20", "alta"],
                    ["sensível", "morena ou amarela", "moderada", "6 ≤ FPS &lt; 12", "moderada"], ["pouco sensível", "negra", "baixa", "2 ≤ FPS &lt; 6", "baixa"]])
          + fonte("<em>ProTeste</em>, ano V, n.o 55, fev./2007 (com adaptações)."))
X(45, "N", "Biologia", "Saúde", "<p>A tabela recomenda filtro para todos os tipos de pele, até para a pele negra (FPS de 2 a 6). Alternativa <strong>B</strong>.</p><p>O filtro reduz, mas não elimina o risco (A); os números da tabela são fatores de proteção, não minutos ou horas de exposição (C, E).</p>",
  tags=["filtro solar", "leitura de tabela"], enun=FILTRO + p(T(45, 0)))
X(46, "N", "Biologia", "Saúde", "<p>Os dois meninos são loiros de olhos azuis, ou seja, de pele extremamente sensível; a tabela recomenda FPS ≥ 20 para pessoas de olhos e cabelos claros, sem exceção para quem se recupera de icterícia. A mãe está certa e o pai, errado. Alternativa <strong>E</strong>.</p><p>FPS ≥ 20 dá proteção muito alta, não moderada (D).</p>",
  tags=["filtro solar", "interpretação"], enun=FILTRO + p(T(46, 0).split(" Na situação apresentada")[0]) + p("Na situação apresentada, comparada à opinião da mãe, a opinião do pai é"),
  alts={k: v.replace("≥ 20", "≥ 20") for k, v in D[46]["alternativas"].items()})
X(47, "H", "Geografia", "Meio ambiente", "<p>O texto mostra que o lixo eletrônico libera metais que contaminam solo e água. Um desenvolvimento sustentável exige controlar e monitorar esses efeitos sobre espécies de rios, solo e vegetação. Alternativa <strong>D</strong>.</p><p>O texto diz que a produção de lixo cresce com o desenvolvimento (C), e descartáveis aumentam o lixo (E).</p>",
  tags=["lixo eletrônico", "desenvolvimento sustentável"],
  enun=ap(T(47, 0)) + fonte("<em>Anuário Gestão Ambiental 2007</em>, p. 47-8 (com adaptações).") + p(SP(47, 1, "(com adaptações).")[1]))
X(48, "H", "Geografia", "Meio ambiente", "<p>O poema fala do minério esgotado e do lixo radioativo (“Torta II”) trazido para Poços de Caldas para “tapar os buracos”, um lixo que ninguém quer perto de casa. A indignação é com os problemas ambientais de escolher um local para depositar lixo tóxico. Alternativa <strong>E</strong>.</p><p>“Lixo do vizinho” é metáfora, não briga entre moradores (C), e “tapando os buracos” se refere às minas, não às estradas (D).</p>",
  figs(("q48", "Poema de Hugo Pontes sobre Poços de Caldas: diz que o planalto não serve mais porque o minério acabou e só restou a mancha, e que estão tapando os buracos com lixo radioativo trazido de fora, que ninguém gostaria de ver jogado no próprio quintal; termina falando dos sentimentos do povo, do poeta e do Brasil.")),
  ["lixo radioativo", "poesia"],
  enun=p("Um poeta habitante da cidade de Poços de Caldas – MG assim externou o que estava acontecendo em sua cidade:") + "[[fig:1]]"
       + fonte("Hugo Pontes. In: M.E.M. Helene. <em>A radioatividade e o lixo nuclear</em>. São Paulo: Scipione, 2002, p. 4.") + fonte("<sup>1</sup>Torta II – lixo radioativo de aspecto pastoso.")
       + p("A indignação que o poeta expressa no verso “Sentimentos mil: do povo, do poeta e do Brasil” está relacionada com"),
  alts={**D[48]["alternativas"], "E": re.split(r"\s+Textos? para as questões", D[48]["alternativas"]["E"])[0]})
PIR = (ap("Os gráficos abaixo, extraídos do sítio eletrônico do IBGE, apresentam a distribuição da população brasileira por sexo e faixa etária no ano de 1990 e projeções dessa população para 2010 e 2030.")
       + tit("Pirâmide etária absoluta – 1990") + "[[fig:1]]" + tit("Pirâmide etária absoluta – 2010") + "[[fig:2]]" + tit("Pirâmide etária absoluta – 2030") + "[[fig:3]]")
F_PIR = figs(("q49a", "Pirâmide etária do Brasil em 1990, por faixas de idade de 0 a 80 anos, homens à esquerda e mulheres à direita (escala até 2.000.000 de pessoas por idade): base larga e topo estreito, formato triangular de população jovem."),
             ("q49b", "Pirâmide etária projetada para 2010: base mais estreita que em 1990 e meio mais largo, com mais adultos."),
             ("q49c", "Pirâmide etária projetada para 2030: base estreita, corpo largo até cerca de 60 anos e topo mais cheio, indicando envelhecimento da população."))
X(49, "H", "Geografia", "População", "<p>As pirâmides mostram base cada vez mais estreita (menos nascimentos) e topo mais largo (mais idosos). Isso acompanha a melhoria das condições de vida, que aumenta a expectativa de vida. Alternativa <strong>A</strong>.</p><p>Mais idosos exigem mais investimento em saúde, não menos (D).</p>",
  F_PIR, ["pirâmide etária", "envelhecimento"], enun=PIR + p(T(49, 0)))
X(50, "H", "Geografia", "População", "<p>De 1990 para 2030, as faixas de idade mais altas se alargam a cada projeção. Mantida a tendência, em 2050 haverá ainda mais gente acima de 40 anos do que em 2030. Alternativa <strong>D</strong>.</p><p>As mulheres vivem mais que os homens (A), e a base jovem encolhe (B).</p>",
  F_PIR, ["pirâmide etária", "projeção"], enun=PIR + p("Se for confirmada a tendência apresentada nos gráficos relativos à pirâmide etária, em 2050,"), alts=D[53]["alternativas"])
X(51, "M", "Matemática", "Estimativa", "<p>Na pirâmide de 2030, cada faixa de idade tem em torno de 1,5 a 1,8 milhão de homens e o mesmo de mulheres, cerca de 3 milhões de pessoas por idade. Somando 81 idades (0 a 80) e considerando o topo mais estreito, o total fica perto de 230 a 240 milhões, entre 210 e 290 milhões. Alternativa <strong>C</strong>.</p><p>A leitura das barras é aproximada, mas as faixas das alternativas são largas: qualquer leitura razoável da pirâmide fica entre 210 e 290 milhões.</p>",
  F_PIR, ["estimativa", "leitura de gráfico"], enun=PIR + p("Se forem confirmadas as projeções apresentadas, a população brasileira com até 80 anos de idade será, em 2030,"),
  alts=A5("menor que 170 milhões de habitantes.", "maior que 170 milhões e menor que 210 milhões de habitantes.", "maior que 210 milhões e menor que 290 milhões de habitantes.", "maior que 290 milhões e menor que 370 milhões de habitantes.", "maior que 370 milhões de habitantes."))
X(52, "N", "Biologia", "Paleontologia", "<p>A distância entre duas marcas consecutivas (a pernada de 2,5 m) depende do comprimento das pernas e, portanto, do tamanho do animal. O comprimento total do rastro (A) depende só de quanto ele andou. Alternativa <strong>B</strong>.</p>",
  figs(("q52", "Fotografia de marcas de arranhões de dinossauro conservadas em rocha.")), ["proporção", "fósseis"],
  enun="[[fig:1]]" + ap("Uma equipe de paleontólogos descobriu um rastro de dinossauro carnívoro e nadador, no norte da Espanha.", "O rastro completo tem comprimento igual a 15 metros e consiste de vários pares simétricos de duas marcas de três arranhões cada uma, conservadas em arenito.",
                         "O espaço entre duas marcas consecutivas mostra uma pernada de 2,5 metros. O rastro difere do de um dinossauro não-nadador: “são as unhas que penetram no barro — e não a pisada —, o que demonstra que o animal estava nadando sobre a água: só tocava o solo com as unhas, não pisava”, afirmam os paleontólogos.")
       + fonte("Internet: &lt;www.noticias.uol.com.br&gt; (com adaptações).") + p("Qual dos seguintes fragmentos do texto, considerado isoladamente, é variável relevante para se estimar o tamanho do dinossauro nadador mencionado?"),
  alts=A5("“O rastro completo tem 15 metros de comprimento”", "“O espaço entre duas marcas consecutivas mostra uma pernada de 2,5 metros”", "“O rastro difere do de um dinossauro não-nadador”", "“são as unhas que penetram no barro — e não a pisada”", "“o animal estava nadando sobre a água: só tocava o solo com as unhas”"))
X(53, "H", "História", "Pré-história", "<p>Pinturas rupestres, como as da Toca do Pajaú (PI), foram feitas por grupos que viveram antes da chegada dos europeus e retratam cenas do cotidiano, como caça e danças. Alternativa <strong>C</strong>.</p><p>Elas são anteriores à colonização (A, E), e os dinossauros se extinguiram milhões de anos antes dos humanos (D).</p>",
  figs(("q53", "Pintura rupestre em rocha, com figuras de pessoas e de animais.")), ["arte rupestre", "pré-história brasileira"],
  enun="[[fig:1]]" + fonte("Pintura rupestre da Toca do Pajaú – PI. Internet: &lt;www.betocelli.com&gt;.") + p("A pintura rupestre acima, que é um patrimônio cultural brasileiro, expressa"),
  alts=A5("o conflito entre os povos indígenas e os europeus durante o processo de colonização do Brasil.", "a organização social e política de um povo indígena e a hierarquia entre seus membros.", "aspectos da vida cotidiana de grupos que viveram durante a chamada pré-história do Brasil.",
          "os rituais que envolvem sacrifícios de grandes dinossauros atualmente extintos.", "a constante guerra entre diferentes grupos paleoíndios da América durante o período colonial."))
X(54, "N", "Biologia", "Biologia geral", "<p>A fossilização leva milhares a milhões de anos; o crescimento de uma árvore, anos ou décadas; a germinação de uma semente, dias. Do mais lento ao mais rápido: fossilização, crescimento, germinação. Alternativa <strong>B</strong>.</p>",
  tags=["escalas de tempo"], enun=p("Fenômenos biológicos podem ocorrer em diferentes escalas de tempo. Assinale a opção que ordena exemplos de fenômenos biológicos, do mais lento para o mais rápido."),
  alts=A5("germinação de uma semente, crescimento de uma árvore, fossilização de uma samambaia", "fossilização de uma samambaia, crescimento de uma árvore, germinação de uma semente", "crescimento de uma árvore, germinação de uma semente, fossilização de uma samambaia",
          "fossilização de uma samambaia, germinação de uma semente, crescimento de uma árvore", "germinação de uma semente, fossilização de uma samambaia, crescimento de uma árvore"))
X(55, "N", "Biologia", "Evolução", "<p>A seleção natural, a sobrevivência de indivíduos com características genéticas favoráveis num ambiente, age sobre plantas e animais. Alternativa <strong>B</strong>.</p><p>O fluxo gênico aumenta a diversidade, não reduz (A); geração espontânea e herança de caracteres adquiridos foram descartadas (C, D); esporulação não ocorre em vertebrados (E).</p>",
  tags=["seleção natural"], enun=p("As mudanças evolutivas dos organismos resultam de alguns processos comuns à maioria dos seres vivos. É um processo evolutivo comum a plantas e animais vertebrados:"),
  alts=A5("movimento de indivíduos ou de material genético entre populações, o que reduz a diversidade de genes e cromossomos.", "sobrevivência de indivíduos portadores de determinadas características genéticas em ambientes específicos.", "aparecimento, por geração espontânea, de novos indivíduos adaptados ao ambiente.",
          "aquisição de características genéticas transmitidas aos descendentes em resposta a mudanças ambientais.", "recombinação de genes presentes em cromossomos do mesmo tipo durante a fase da esporulação."))
X(56, "N", "Biologia", "Genética", "<p>Metabolismo: respiração celular (reações que liberam energia). Autorreplicação: duplicação do DNA, o “material onde o programa está inscrito”. Mutação: alterações na sequência de bases do DNA. Alternativa <strong>D</strong>.</p>",
  tags=["DNA", "metabolismo"],
  enun=ap(T(56, 0)) + fonte("M. O. Murphy e l. O’neill (Orgs.). <em>O que é vida? 50 anos depois — especulações sobre o futuro da biologia</em>. São Paulo: UNESP. 1997 (com adaptações).") + p(SP(56, 2, "(com adaptações).")[1].replace("autoreplicação", "auto-replicação")))
X(57, "N", "Física", "Energia", "<p>O sobe-e-desce do compartimento de carga (movimento, energia cinética) faz girar o motor ligado ao gerador, que produz energia elétrica. No esquema: energia potencial → I (cinética) → II (elétrica). Alternativa <strong>A</strong>.</p>",
  figs(("q57a", "Infográfico “Mochila geradora de energia”: a mochila tem estrutura rígida e compartimento de carga suspenso por molas; ao caminhar, os quadris sobem e descem cerca de cinco centímetros, e o vai-e-vem do compartimento faz girar um motor conectado ao gerador de eletricidade."),
       ("q57b", "Esquema “Movimento da mochila”: energia potencial ⇄ energia I → energia II.")),
  ["transformação de energia"], enun="[[fig:1]]" + fonte("<em>Istoé</em>, n.o 1.864, set./2005, p. 69 (com adaptações).") + p(T(57, 2)) + "[[fig:2]]" + p(T(57, 4)))
ETANOL = (ap("As pressões ambientais pela redução na emissão de gás estufa, somadas ao anseio pela diminuição da dependência do petróleo, fizeram os olhos do mundo se voltarem para os combustíveis renováveis, principalmente para o etanol. Líderes na produção e no consumo de etanol, Brasil e Estados Unidos da América (EUA) produziram, juntos, cerca de 35 bilhões de litros do produto em 2006. Os EUA utilizam o milho como matéria-prima para a produção desse álcool, ao passo que o Brasil utiliza a cana-de-açúcar. O quadro abaixo apresenta alguns índices relativos ao processo de obtenção de álcool nesses dois países.")
          + tabela(["", "cana", "milho"], [["produção de etanol", "8 mil litros/ha", "3 mil litros/ha"], ["gasto de energia fóssil para produzir 1 litro de álcool", "1.600 kcal", "6.600 kcal"],
                   ["balanço energético", "positivo: gasta-se 1 caloria de combustível fóssil para a produção de 3,24 calorias de etanol", "negativo: gasta-se 1 caloria de combustível fóssil para a produção de 0,77 caloria de etanol"],
                   ["custo de produção/litro", "US$ 0,28", "US$ 0,45"], ["preço de venda/litro", "US$ 0,42", "US$ 0,92"]])
          + fonte("<em>Globo Rural</em>, jun./2007 (com adaptações)."))
X(58, "N", "Química", "Combustíveis", "<p>A cana produz 8 mil litros de etanol por hectare, contra 3 mil do milho: mais do dobro. Por isso é mais eficiente. Alternativa <strong>A</strong>.</p><p>A justificativa de B inverte os dados: o milho gasta mais energia fóssil (6.600 kcal contra 1.600).</p>",
  tags=["etanol", "eficiência"], enun=ETANOL + p(T(58, 0)))
X(59, "N", "Química", "Combustíveis", "<p>O etanol vem de plantas que absorvem CO<sub>2</sub> ao crescer; trocar gasolina por etanol reduz o saldo de emissões e pode atenuar o aumento do efeito estufa, como diz o texto. Alternativa <strong>C</strong>.</p><p>Monoculturas reduzem a biodiversidade e alteram o solo (A, E), e os balanços energéticos mostram impactos diferentes (B).</p>",
  tags=["etanol", "efeito estufa"], enun=ETANOL + p(T(59, 0)))
X(60, "N", "Física", "Energia", "<p>O vento (energia eólica) gera eletricidade sem queimar combustível e, portanto, sem emitir gases de efeito estufa. Óleo diesel, gasolina, carvão e gás natural são combustíveis fósseis que liberam CO<sub>2</sub>. Alternativa <strong>E</strong>.</p>",
  tags=["energia eólica", "aquecimento global"])
X(61, "N", "Física", "Energia", "<p>A máquina que menos gasta energia é a II (0,93 kWh), mas a que menos gasta água é a I (76,38 L). Logo, a máquina que menos consome energia não é a que consome menos água. Alternativa <strong>D</strong>.</p><p>A máquina V é a que mais gasta energia e também a que mais gasta água (E).</p>",
  figs(("q61a", "Figura I, consumo de energia (em kWh) das máquinas: I, 1,24; II, 0,94; III, 0,93; IV, 1,53; V, 1,83."), ("q61b", "Figura II, consumo de água (em L): I, 76,38; II, 99,35; III, 109,31; IV, 215,80; V, 325,80.")),
  ["leitura de gráfico", "consumo"], enun="[[fig:1]]" + fonte("Figura I") + "[[fig:2]]" + fonte("Figura II. Associação Brasileira de Defesa do Consumidor (com adaptações).") + p(T(61, 5)))
X(62, "N", "Química", "Água", "<p>Os três tipos são adequados ao consumo humano, ou seja, potáveis: a água mineral e a potável de mesa por definição, e a purificada é feita a partir de água potável. Alternativa <strong>A</strong>.</p><p>Só a água mineral tem ação medicamentosa (E), e a purificada é produzida artificialmente (C).</p>",
  tags=["água potável", "interpretação de texto"],
  enun=p(T(62, 0).split(" • ")[0]) + "<ul>" + "".join(f"<li>{x}</li>" for x in T(62, 0).split(" Com base nessas")[0].split(" • ")[1:]) + "</ul>" + p("Com base nessas" + T(62, 0).split(" Com base nessas")[1]))
X(63, "H", "Geografia", "Recursos hídricos", "<p>O fundamento III diz que, em situações de escassez, os usos prioritários são o consumo humano e a dessedentação de animais. Durante a estiagem, a irrigação deve ser interrompida para garantir o abastecimento da cidade. Alternativa <strong>B</strong>.</p><p>A água é bem público, não do dono da fazenda (A).</p>",
  tags=["Lei das Águas", "uso da água"],
  enun=p(T(63, 0)) + '<ol type="I"><li>a água é um bem de domínio público;</li><li>a água é um recurso natural limitado, dotado de valor econômico;</li><li>em situações de escassez, os usos prioritários dos recursos hídricos são o consumo humano e a dessedentação de animais;</li><li>a gestão dos recursos hídricos deve sempre proporcionar o uso múltiplo das águas.</li></ol>' + p(T(63, 2)))

# Revisão geral (12/11): o texto comum do grupo seguinte vazava para a alternativa E anterior.
for _q in Q.values():
    for _l, _v in list(_q["alternativas"].items()):
        _q["alternativas"][_l] = re.split(r"\s*(?:Texto para as questões \d|Instruções: As questões de números)", _v)[0]

completar(Q, R)
