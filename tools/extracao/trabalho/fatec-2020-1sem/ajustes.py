# Ajustes da conferência humana: Vestibular FATEC 1º semestre de 2020 (exame de 08/12/2019)
# Texto conferido com a imagem de cada página. Tema implícito: mundo do trabalho (redação: empreendedorismo no Brasil do século XXI).
# 54 questões; a prova tem 5 h no total, incluindo a redação (que fica fora do simulado).
# Matéria: a do gabarito oficial; nas "Multidisciplinar", a matéria principal + tag "multidisciplinar".
# Rascunho com colunas embaralhadas: todos os enunciados e alternativas foram escritos aqui.
# Gabarito: oficial (1º SEM/20). Q51 e Q52 ANULADAS (o gabarito traz C e A ao lado de "ANULADA"; motivo não publicado). Poema de Gullar e versos da Q54 como imagem.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import A, carregar, enun, tabela, colunas, completar, trecho

ID = "fatec-2020-1sem"
META = {
    "id": ID,
    "banca": "FATEC",
    "ano": 2020,
    "semestre": 1,
    "titulo": "Vestibular FATEC, 1º semestre de 2020",
    "fonte": "Centro Paula Souza",
    "dataExame": "2019-12-08",
    "duracaoMinutos": 300,
    "tema": "Mundo do trabalho",
}

R = carregar(ID)
MULTI = ["multidisciplinar"]


def T(pag, inicio, fim, paragrafos=()):
    return trecho(ID, pag, inicio, fim, paragrafos)


def p(*paragrafos, classe=None):
    abre = f'<p class="{classe}">' if classe else "<p>"
    return "".join(abre + x + "</p>" for x in paragrafos)


def apoio(*paragrafos):
    return '<p class="apoio">' + A.join(paragrafos) + "</p>"


def fonte(t):
    return f'<p class="fonte">{t}</p>'


def url(u, data, extra="Adaptado."):
    return fonte(f"&lt;{u}&gt; Acesso em: {data}." + (" " + extra if extra else ""))


def chamada(t):
    return f'<p class="chamada">{t}</p>'


def figs(*pares):
    return [{"arquivo": a, "alt": t} for a, t in pares]


def it(texto, *termos):
    for t in termos: texto = texto.replace(t, f"<em>{t}</em>")
    return texto


def alts(*textos):
    return dict(zip("ABCDE", textos))


def troca(html, pares):
    for a, b in pares:
        assert a in html, a
        html = html.replace(a, b, 1)
    return html


# ---------- textos compartilhados ----------
ACUCAR = (chamada("Leia os textos I e II para responder às questões de 03 a 05.")
          + p("<strong>Texto I</strong>") + "[[fig:1]]"
          + p("<strong>Texto II</strong>") + "[[fig:2]]" + url("https://tinyurl.com/y4ur7lhb", "18.10.2019", "Original colorido.")
          + fonte("* Texto da imagem: “Em 1888, a princesa Isabel assinou a Lei Áurea, mas nem todo mundo conseguiu ler.”")
          + apoio("As informações contidas na imagem do texto II, localizadas no canto inferior direito, não foram reproduzidas, pois não interferem na resolução das questões apresentadas."))
ACUCAR_IMG = figs(("q03a", "Texto I: o poema “O Açúcar”, de Ferreira Gullar, em versos livres. O eu lírico adoça o café numa manhã em Ipanema e reflete que o açúcar branco e puro não foi feito por ele, nem pelo dono da mercearia, nem pelo dono da usina: veio de canaviais distantes, plantados e colhidos por homens que vivem sem hospital nem escola, não sabem ler e morrem de fome jovens, e foi produzido em usinas escuras por homens de vida amarga e dura. Fonte: GULLAR, F. “O Açúcar”. Toda poesia. Rio de Janeiro, Civilização Brasileira, 1980."),
                  ("q03b", "Texto II: foto em preto e branco de mãos negras segurando colmos de cana-de-açúcar dispostos como as grades de uma cela. No canto superior esquerdo, uma frase em letras pequenas."))
P3 = p("Após a leitura e a análise, infere-se corretamente que ambos os textos abordam temáticas")

SLIME = (chamada("Leia o texto para responder às questões de 20 a 24.")
         + p("<strong>A Química do <em>Slime</em></strong>")
         + apoio(*[it(x, "slime") for x in T(9, "A jornada histórica do slime tem início", "elevada viscosidade e elasticidade.", ["O slime caseiro pode ser", "A dissociação, em solução aquosa"])])
         + p("Os íons sódio interagem com a estrutura do PVAc conforme representado.") + "[[fig:1]]"
         + p("A reação entre o ácido bórico e o bicarbonato de sódio também origina o tetraborato de sódio, conhecido como “Bórax” (Na<sub>2</sub>B<sub>4</sub>O<sub>7</sub>). Este, em meio básico, transforma-se em tetrahidroxiborato, conforme representado na equação 1.") + "[[fig:2]]"
         + p("O PVAc reage com moléculas de água produzindo álcool polivinílico (PVA), conforme representado na equação 2.") + "[[fig:3]]"
         + p("O tetrahidroxiborato reage com o PVA (equação 3), formando novas ligações que interligam as cadeias do polímero que constitui o <em>slime</em>.") + "[[fig:4]]"
         + url("https://tinyurl.com/y4vmmd9w", "01.10.2019"))
SLIME = troca(SLIME, [("(NaHCO3)", "(NaHCO<sub>3</sub>)"), ("H3BO3", "H<sub>3</sub>BO<sub>3</sub>"), ("(Na3BO3)", "(Na<sub>3</sub>BO<sub>3</sub>)"), ("(Na+)", "(Na<sup>+</sup>)")])
SLIME_IMG = figs(("q20a", "Interação entre um íon sódio, Na⁺, e o PVAc: o Na⁺ fica ligado por uma linha pontilhada ao oxigênio da carbonila (C=O), que tem carga parcial negativa (δ⁻); o carbono tem carga parcial positiva (δ⁺) e está ligado a um CH₃ e, por um oxigênio, a um CH da cadeia do polímero."),
                 ("q20b", "Equação 1: Na₂B₄O₇ (bórax) + 7 H₂O + 2 OH⁻ → 4 [B(OH)₄]⁻ (ânion tetrahidroxiborato, um boro ligado a quatro grupos OH) + 2 Na⁺."),
                 ("q20c", "Equação 2: um trecho do PVAc, com dois grupos –O–C(=O)–CH₃ ligados a carbonos da cadeia, + 2 H₂O → um trecho do PVA, com dois grupos –OH no lugar, + 2 H₃C–C(=O)–OH (composto X)."),
                 ("q20d", "Equação 3: dois trechos de PVA, cada um com dois grupos –OH, + o tetrahidroxiborato ⇌ trecho da cadeia do slime, em que o boro fica ligado a quatro oxigênios (ligações I, II, III e IV), cada um preso a um carbono das cadeias de PVA, + 4 H₂O."))
P20 = p("Considerando que uma colher de chá de bicarbonato de sódio contém 5 g desse composto, é correto afirmar que o número de moléculas de bicarbonato de sódio utilizadas na fabricação do <em>slime</em> caseiro, conforme descrito no texto, corresponde a aproximadamente") \
    + apoio("Massa molar do NaHCO<sub>3</sub> = 84 g/mol<br>Constante de Avogadro: 6 × 10<sup>23</sup> mol<sup>–1</sup>")

RACISMO = (chamada("Leia o texto para responder às questões de 25 a 29.")
           + apoio("<strong>Minority ethnic Britons face ‘shocking’ job discrimination</strong>", "<u>Haroon Siddique</u><br>Thu 17 Jan 2019 17.00 GMT Last modified on Fri 18 Jan 2019 00.50 GMT",
                   *(lambda e, d: e[:-1] + [e[-1] + " " + d[0]] + d[1:])(
                       T(11, "A study by experts based at the Centre", "Runnymede, described the", ["A linked study by the same", "The research, part of a larger", "It echoes findings published", "Prof Anthony Heath, co-author", "Dr Zubaida Haque, the deputy"]),
                       T(11, "findings as shocking.", "security in work and life.”", ["“It’s clear that race relations"])))
           + url("https://tinyurl.com/y9nohdte", "07.10.2019") + fonte("*BME – Black and Minority Ethnicity"))
P25 = p("O estudo mencionado no texto aponta para a discriminação racial de")

ANTUNES = (chamada("Leia o texto para responder às questões de 51 a 54.")
           + apoio(*T(20, "O leitor encontra, neste belo número", "trabalho”, seus dilemas e desafios.",
                      ["[...]", "Se a Revolução Industrial", "As consequências são fortes", "É por isso que estamos", "Este número especial da Revista"]))
           + fonte("Ricardo Antunes, Editorial da Revista <em>Katálysis</em>, n.2, 2009. &lt;https://tinyurl.com/y6nchqmr&gt; Acesso em: 19.10.2019. Adaptado.")
           + fonte("*fetichizar: ação de admirar exageradamente, irrestritamente, incondicionalmente uma pessoa ou coisa."))
ANTUNES = troca(ANTUNES, [("Revista Katálysis, um", "Revista <em>Katálysis</em>, um"), ("“informatização”", "“<strong>informatização</strong>”"), ("“informalização”", "“<strong>informalização</strong>”"), ("cybertariado", "<em>cybertariado</em>")])
P51 = p("Assinale a alternativa que apresenta uma análise correta das informações apresentadas no texto.")
ANUL = "O Centro Paula Souza anulou esta questão no gabarito oficial e não publicou o motivo; ao lado da anulação, o gabarito ainda traz a letra {L}. "

Q = {
1: {"materia": "Inglês", "assunto": "Interpretação de texto", "tags": MULTI + ["charge", "ironia"],
    "enunciado": p("Leia a charge.") + "[[fig:1]]" + url("https://tinyurl.com/y3lrke6a", "08.10.2019", "Original colorido.") + p("A ironia da charge se constrói no fato de"),
    "imagens": figs(("q01", "Charge em inglês: uma mulher sentada à mesa lê um jornal com a manchete “Jobs are returning!” (os empregos estão voltando!) e o subtítulo “But they're low wage, no benefits jobs” (mas são empregos de baixo salário e sem benefícios). Um homem sorridente entra pela porta e diz: “Good news… each of my three jobs are letting me take Labor Day off!” (boa notícia… cada um dos meus três empregos vai me deixar folgar no Dia do Trabalho!).")),
    "explicacao": "<p>O homem comemora que seus <strong>três empregos</strong> lhe dão folga no Dia do Trabalho, enquanto o jornal avisa que os novos empregos pagam pouco e não têm benefícios. A ironia está em alguém parecer feliz com subempregos que o obrigam a trabalhar em três lugares. Alternativa <strong>A</strong>.</p><p>A manchete diz que os empregos não têm benefícios (B), não são bons (C), não trazem vantagens (D) e não pagam bem (E).</p>"},
2: {"materia": "Geografia", "assunto": "Globalização", "tags": MULTI + ["precariado", "trabalho informal"],
    "enunciado": apoio(*T(2, "O conceito de precariado se refere", "horários regulares de trabalho."))
                 + url("https://tinyurl.com/y6kgyeqz", "10.10.2019") + p("De acordo com o texto, o precariado é um grupo de pessoas que"),
    "alternativas": alts("não aceita a tutela do Estado e negocia sua força de trabalho diretamente com o governo, que o repassa às empresas, conseguindo, dessa forma, remunerações acima do mercado.",
                         "não é explorado pelo fato de trabalhar sem folgas semanais, uma vez que possui registro na carteira de trabalho, e aceita, voluntariamente, não tirar as férias anuais previstas em lei.",
                         "não possui um emprego formal e, portanto, não possui direitos trabalhistas, estando sujeito às atividades com longas jornadas de trabalho, por prazo determinado e em condições insalubres.",
                         "não recebe mais que um salário mínimo, contudo, possui horários regulares de trabalho e está amparado pelas leis trabalhistas, que permitem uma remuneração menor que a prevista na Constituição Federal.",
                         "não quer ter um emprego formal, mas tem seus direitos trabalhistas legais respeitados, mesmo cumprindo jornadas de trabalho superiores a vinte horas diárias, e também possui estabilidade no emprego de caráter oficial."),
    "explicacao": "<p>O texto diz que o precariado aceita “empregos instáveis, sem uma identidade ocupacional”, com exploração e sem horários regulares: são trabalhadores sem emprego formal e, portanto, sem direitos trabalhistas. Alternativa <strong>C</strong>.</p><p>O precariado não negocia com o governo nem ganha acima do mercado (A). Ele é explorado e não tem carteira assinada (B). Não tem horários regulares nem amparo das leis (D). E não há estabilidade nem direitos respeitados (E).</p>"},
3: {"materia": "Português", "assunto": "Interpretação de texto", "tags": MULTI + ["intertextualidade"],
    "enunciado": ACUCAR + P3, "imagens": ACUCAR_IMG,
    "explicacao": "<p>O poema contrapõe o eu lírico, que adoça o café em Ipanema, aos trabalhadores rurais que vivem na miséria e produziram o açúcar. A imagem, com mãos negras presas atrás de “grades” de cana e a frase sobre a Lei Áurea, denuncia a exploração da mão de obra, que continuou depois da abolição. Os temas são <strong>similares</strong>. Alternativa <strong>D</strong>.</p><p>Os textos tratam justamente da desigualdade (A). O Texto II não fala de impacto ambiental (B), o poema não mostra a alienação dos poetas nem a imagem fala de centros urbanos (C), e os textos não descrevem ciclos econômicos de períodos diferentes (E).</p>"},
4: {"materia": "Física", "assunto": "Energia", "tags": MULTI + ["proporção"],
    "enunciado": p(*[it(x, "International Sugar Journal") for x in T(3, "Atualmente, o cultivo da cana-de-açúcar está", "aproximada e respectivamente, de", ["Com as informações fornecidas"])]),
    "alternativas": colunas(["Gcal/h", "kg"], [["1,3", "1 350"], ["1,3", "150"], ["1,7", "135"], ["1,7", "150"], ["1,7", "1 350"]]),
    "explicacao": "<p>Um boia-fria cortava 9 t de cana em 12 h. Energia: 9 · 1,7 = 15,3 Gcal em 12 h, ou 15,3 ÷ 12 ≈ <strong>1,3 Gcal/h</strong>. Açúcar: 9 · 150 = <strong>1 350 kg</strong>. Alternativa <strong>A</strong>.</p><p>1,7 Gcal e 150 kg são os valores de uma tonelada só, sem considerar as 9 t e as 12 h (C, D e E). E 150 kg ignora as 9 t (B).</p>"},
5: {"materia": "História", "assunto": "Brasil Colônia", "tags": ["escravidão", "engenhos de açúcar"],
    "enunciado": p("O texto II remete a um período de produção do açúcar em que se estabeleceu um tipo característico de relação social e de trabalho.",
                   "Assinale a alternativa que apresenta, corretamente, algumas das características dessas relações sociais e de trabalho nos engenhos de açúcar da América portuguesa, no século XVI."),
    "apoio_de": (3, P3),
    "explicacao": "<p>A Igreja e os colonizadores usavam interpretações bíblicas (como a “maldição de Cam”) para justificar a escravidão como castigo ou expiação. Os africanos escravizados eram separados de suas famílias e comunidades no tráfico e na venda. Alternativa <strong>B</strong>.</p><p>Os africanos eram capturados à força, não se ofereciam (A). Nos engenhos do Nordeste predominou a mão de obra africana, não a indígena andina (C). Imigrantes italianos e alemães só vieram no século XIX (D). E a escravidão colonial não seguia um modelo africano de produção de <em>commodities</em> (E).</p>"},
6: {"materia": "Biologia", "assunto": "Genética", "tags": ["biotecnologia", "eletroforese"],
    "enunciado": p(*T(4, "Embora há milhares de ano o ser humano", "referidos no texto.", ["Assim, a Biotecnologia moderna", "Atualmente, sabe-se que certas", "Assinale a alternativa que associa"])),
    "alternativas": colunas(["enzimas bacterianas", "processo"], [["endonucleases de restrição", "centrifugação"], ["DNA polimerase", "eletroforese"], ["transcriptase reversa", "centrifugação"], ["endonucleases de restrição", "eletroforese"], ["DNA polimerase", "centrifugação"]]),
    "explicacao": "<p>As enzimas bacterianas que cortam o DNA em pontos específicos são as <strong>endonucleases (enzimas) de restrição</strong>. Os fragmentos são separados por tamanho num gel, sob corrente elétrica: é a <strong>eletroforese</strong>, base do teste de DNA. Alternativa <strong>D</strong>.</p><p>A DNA polimerase copia o DNA, não o corta (B e E). A transcriptase reversa produz DNA a partir de RNA (C). E a centrifugação separa por densidade, não usa gel (A, C e E).</p>"},
7: {"materia": "Química", "assunto": "Reações químicas", "tags": ["termoquímica", "entalpia de formação"],
    "enunciado": p(*T(4, "Uma das áreas de aplicação dos conhecimentos", "fermentação alcoólica da glicose é"))
                 + "\\[\\text{C}_6\\text{H}_{12}\\text{O}_6(aq) \\rightarrow 2\\,\\text{C}_2\\text{H}_6\\text{O}(aq) + 2\\,\\text{CO}_2(g) \\qquad \\Delta_r H = ?\\]"
                 + p("Assinale a alternativa que apresenta o valor correto da entalpia padrão da reação (∆<sub>r</sub>H) de fermentação da glicose, em kJ/mol.")
                 + tabela(["Substância", "∆<sub>f</sub>H (kJ/mol)"], [["C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>(aq)", "– 1 277"], ["C<sub>2</sub>H<sub>6</sub>O(aq)", "– 278"], ["CO<sub>2</sub>(g)", "– 394"]]),
    "alternativas": alts("– 67", "– 32", "+16", "+32", "+67"),
    "explicacao": "<p>∆H = Σ(produtos) − Σ(reagentes) = [2 · (–278) + 2 · (–394)] − (–1 277) = (–556 – 788) + 1 277 = –1 344 + 1 277 = <strong>–67 kJ/mol</strong>. Alternativa <strong>A</strong>.</p><p>Inverter produtos e reagentes dá +67 (E). E esquecer os coeficientes 2 leva a valores como –32 ou +32 (B e D).</p>"},
8: {"materia": "Matemática", "assunto": "Porcentagem", "tags": MULTI + ["gráfico de setores", "trabalho informal"],
    "enunciado": p("Leia o gráfico que apresenta a distribuição do trabalho informal no Brasil, em milhões de trabalhadores, referente ao segundo trimestre de 2019.") + "[[fig:1]]"
                 + p("Segundo o gráfico, a porcentagem aproximada de trabalhadores empregados no setor privado sem carteira assinada, em relação ao total de trabalhadores informais, é"),
    "imagens": figs(("q08", "Gráfico de setores do trabalho informal no Brasil, em milhões de trabalhadores: conta própria sem carteira assinada, 19,42; empregado no setor privado sem carteira assinada, 11,66; trabalhador doméstico sem carteira assinada, 4,53; trabalhador familiar auxiliar, 2,23; empregador sem CNPJ, 0,85.")),
    "alternativas": alts("10%", "20%", "30%", "40%", "50%"),
    "explicacao": "<p>O total é 19,42 + 11,66 + 4,53 + 2,23 + 0,85 = 38,69 milhões. Os empregados no setor privado sem carteira são 11,66 milhões: 11,66 ÷ 38,69 ≈ 0,30, ou cerca de <strong>30%</strong>. Alternativa <strong>C</strong>.</p><p>50% seria a fatia da conta própria (E). Os demais valores não correspondem a nenhuma fatia.</p>"},
9: {"materia": "Matemática", "assunto": "Estatística", "tags": MULTI + ["média aritmética"],
    "enunciado": p(*T(5, "Carlos está desempregado já há algum tempo", "curtas de 5 quilômetros."))
                 + tabela(["Plataforma", "Valor da viagem para o passageiro (R$)", "Taxa do valor da viagem que vai para o motorista", "Valor que o motorista recebe (R$)"],
                          [["I", "12,88", "75%", "9,66"], ["II", "13,50", "75%", "10,12"], ["III", "11,64", "100%", "11,64"], ["IV", "14,05", "80%", "11,24"], ["V", "19,54", "80%", "15,63"], ["VI", "18,10", "100%", "18,10"]])
                 + p(*T(5, "Carlos trabalhará apenas com plataformas", "às exigências de Carlos é", ["Assim, a quantidade"])),
    "alternativas": alts("1", "2", "3", "4", "5"),
    "explicacao": "<p>A média do que o motorista recebe é (9,66 + 10,12 + 11,64 + 11,24 + 15,63 + 18,10) ÷ 6 = 76,39 ÷ 6 ≈ 12,73. Ficam acima só as plataformas V (15,63) e VI (18,10): <strong>2</strong> aplicativos. Alternativa <strong>B</strong>.</p><p>Usar a média do valor pago pelo passageiro (cerca de 14,95) daria também 2, mas o critério é o valor recebido pelo motorista.</p>"},
10: {"materia": "Raciocínio lógico", "assunto": "Lógica", "tags": ["contagem"],
     "enunciado": p("Um grupo de 8 alunos da Fatec do curso de Têxtil e Moda está prestando consultoria a 32 <em>startups</em>. Cada uma dessas <em>startups</em> é auxiliada precisamente por 3 alunos desse grupo, e cada aluno auxilia o mesmo número de <em>startups</em>.",
                    "Nessas condições, a quantidade de <em>startups</em> que cada aluno auxilia é"),
     "alternativas": alts("8.", "9.", "10.", "11.", "12."),
     "explicacao": "<p>Cada uma das 32 startups recebe 3 alunos: são 32 · 3 = 96 “atendimentos”. Divididos igualmente entre os 8 alunos, cada um auxilia 96 ÷ 8 = <strong>12</strong> startups. Alternativa <strong>E</strong>.</p><p>Dividir só 32 por 8 daria 4, e as demais alternativas não saem da conta.</p>"},
11: {"materia": "Raciocínio lógico", "assunto": "Sequências", "tags": ["padrões"],
     "enunciado": p("Observe os grupos de palavras que seguem uma determinada lógica:")
                  + tabela(["", "", "", ""], [["<strong>I.</strong>", "Corte", "Afiador", "Bestialidade"], ["<strong>II.</strong>", "Forte", "Educador", "Multiplicidade"], ["<strong>III.</strong>", "Norte", "", "Relatividade"], ["<strong>IV.</strong>", "Sorte", "Observador", "Trivialidade"]])
                  + p("Seguindo a mesma lógica, assinale a palavra que completa, de maneira coerente, o espaço vazio na <strong>linha III</strong> da tabela."),
     "alternativas": alts("Empreendedor.", "Questionador.", "Inspirador.", "Unificador.", "Transformador."),
     "explicacao": "<p>Na coluna do meio, as palavras começam pelas vogais em ordem: <strong>A</strong>fiador, <strong>E</strong>ducador, ?, <strong>O</strong>bservador. A palavra que falta começa com I: <strong>Inspirador</strong>. Todas também terminam em “-dor”. Alternativa <strong>C</strong>.</p><p>Empreendedor começa com E, Unificador com U, e Questionador e Transformador com consoantes (A, B, D e E).</p>"},
12: {"materia": "Raciocínio lógico", "assunto": "Raciocínio espacial", "tags": ["acessibilidade", "círculo"],
     "enunciado": p(*T(6, "A utilização de cadeira de rodas impõe limites", "eixo de rotação da cadeira, de raio igual a", ["De acordo com as dimensões"])) + "[[fig:1]]",
     "imagens": figs(("q12", "Duas figuras vistas de cima de uma pessoa em cadeira de rodas. Figura 1 – Rotação de 90°: a manobra ocupa um quadrado de 1,20 m por 1,20 m. Figura 2 – Rotação de 180°: a manobra ocupa um retângulo de 1,50 m de largura por 1,20 m de altura.")),
     "alternativas": alts("0,60.", "0,75.", "0,85.", "1,20.", "1,50."),
     "explicacao": "<p>Na rotação de 180°, a cadeira precisa de 1,50 m de largura, a maior medida necessária. Para girar 360°, ela precisa dessa largura em qualquer direção: um círculo de diâmetro 1,50 m, ou seja, raio de <strong>0,75 m</strong>. É o que recomenda a ABNT. Alternativa <strong>B</strong>.</p><p>0,60 m é a metade de 1,20 m, insuficiente para a manobra de 180° (A). E 1,20 e 1,50 são diâmetros, não raios (D e E).</p>"},
13: {"materia": "Física", "assunto": "Eletricidade", "tags": ["resistência elétrica", "proporção"],
     "enunciado": p("Douglas, aluno do curso de Instalações Elétricas, sabe que a resistência elétrica de um fio é diretamente proporcional ao seu comprimento e inversamente proporcional ao quadrado do diâmetro de sua secção transversal.",
                    "Durante uma atividade prática do curso, Douglas precisou realizar uma melhoria em uma máquina. Para isso um fio deveria ser trocado por outro do mesmo material, mas cujo",
                    "• comprimento seria 60% maior; e<br>• diâmetro seria 20% menor.",
                    "Assinale a alternativa que apresenta corretamente a relação entre a resistência do fio retirado (R<sub>1</sub>) e a resistência do novo fio (R<sub>2</sub>)."),
     "alternativas": alts("R<sub>2</sub> = 0,20 · R<sub>1</sub>", "R<sub>2</sub> = 0,30 · R<sub>1</sub>", "R<sub>2</sub> = 0,75 · R<sub>1</sub>", "R<sub>2</sub> = 1,50 · R<sub>1</sub>", "R<sub>2</sub> = 2,50 · R<sub>1</sub>"),
     "explicacao": "<p>R é proporcional a L ÷ d². O novo fio tem L₂ = 1,6 L₁ e d₂ = 0,8 d₁: R₂ = R₁ · 1,6 ÷ 0,8² = R₁ · 1,6 ÷ 0,64 = <strong>2,5 · R₁</strong>. Alternativa <strong>E</strong>.</p><p>Esquecer de elevar o diâmetro ao quadrado daria 1,6 ÷ 0,8 = 2 (nenhuma alternativa). Os outros valores invertem a proporção.</p>"},
14: {"materia": "Raciocínio lógico", "assunto": "Análise combinatória", "tags": ["princípio multiplicativo", "potências"],
     "enunciado": p("No mundo digital, podem-se definir as cores com o auxílio de um sistema de códigos que é composto pelo sinal de sustenido (#) seguido por seis caracteres que podem ser algarismos (que vão de 0 até 9) ou letras (de A até F).",
                    "Deste modo, são exemplos de códigos que representam cores:")
                  + tabela(["Código", "Cor"], [["#084D6E", "Azul Petróleo"], ["#DA70D6", "Orquídea"], ["#FF00FF", "Fúcsia"]])
                  + url("https://tinyurl.com/y4qkz9j5", "19.10.2019") + p("Logo, utilizando esse código, a quantidade de cores que é possível representar é igual a"),
     "alternativas": alts("2<sup>6</sup>", "2<sup>10</sup>", "2<sup>12</sup>", "2<sup>18</sup>", "2<sup>24</sup>"),
     "explicacao": "<p>Cada um dos 6 caracteres pode ser um de 16 símbolos (10 algarismos + 6 letras). São 16⁶ = (2⁴)⁶ = <strong>2²⁴</strong> cores. Alternativa <strong>E</strong>.</p><p>2⁶ seria ter só 2 opções por caractere (A). E 2¹⁰, 2¹² e 2¹⁸ não correspondem a 16 opções em 6 posições (B, C e D).</p>"},
15: {"materia": "História", "assunto": "Idade Média", "tags": ["peste negra", "demografia"],
     "enunciado": p("Observe o gráfico.") + "[[fig:1]]" + fonte("Fonte dos dados &lt;https://tinyurl.com/yyu562xp&gt; Acesso em: 05.10.2019.")
                  + p("A leitura do gráfico permite concluir, corretamente, que o período de queda demográfica mais acentuada na Europa ocorreu"),
     "imagens": figs(("q15", "Gráfico de área “Evolução demográfica da Europa”, população em milhões por ano, de 1000 a 1500: cerca de 40 em 1000; sobe aos poucos até cerca de 72 em 1300; cai bruscamente para cerca de 52 em 1350 e 50 em 1400; volta a subir para cerca de 60 em 1450 e 67 em 1500.")),
     "explicacao": "<p>A maior queda do gráfico vai de cerca de 72 milhões, em 1300, para cerca de 52 milhões, em 1350: a primeira metade do século XIV. É a época da <strong>peste negra</strong> (a partir de 1347), que matou de um quarto a um terço da população europeia. Alternativa <strong>D</strong>.</p><p>Nos séculos XI, XII e XIII a população cresceu (A, B e C). E na segunda metade do século XV ela voltou a subir (E).</p>"},
16: {"materia": "História", "assunto": "Brasil Colônia", "tags": ["capitanias hereditárias"],
     "enunciado": apoio(*T(7, "O projeto de ocupação populacional da Colônia", "efetivamente prosperaram.", ["O sistema, contudo"]))
                  + url("https://tinyurl.com/y6q37ysu", "15.10.2019") + p("Assinale a alternativa que apresenta, corretamente, algumas das causas do fracasso do sistema descrito no texto."),
     "explicacao": "<p>A maioria das capitanias fracassou pela resistência indígena, pelos altos custos e pela falta de recursos dos donatários, que contavam com pouca ajuda da Coroa. Só Pernambuco e São Vicente prosperaram. Alternativa <strong>A</strong>.</p><p>A Lei de Terras é de 1850 (B). A burguesia não recorreu a cortes internacionais (C). O clima de monções é asiático (D). E os corsários franceses não ocuparam as capitanias (E).</p>"},
17: {"materia": "História", "assunto": "Imperialismo e neocolonialismo", "tags": ["Conferência de Berlim"],
     "enunciado": apoio(*T(8, "Tinha cinco metros o mapa que dominou", "conflitos internos no continente.", ["Quando a Conferência chegou", "Representantes de diversos"]))
                  + url("https://tinyurl.com/y4z6b4j7", "15.10.2019") + p("Assinale a alternativa que apresenta, corretamente, a conferência a que o texto se refere e o processo histórico que se iniciou a partir dela."),
     "explicacao": "<p>A conferência convocada por Bismarck em Berlim (1884–1885) definiu regras para a partilha da <strong>África</strong> entre as potências europeias. As duas exceções citadas são a Libéria e a Etiópia, que não foram colonizadas. Alternativa <strong>D</strong>.</p><p>O Tratado de Verdun é do século IX (A), Tordesilhas e Madri trataram da América (B e C), e a divisão de Berlim veio depois da Segunda Guerra, não em Versalhes (E).</p>"},
18: {"materia": "História", "assunto": "Era Vargas", "tags": ["trabalho feminino", "leis trabalhistas"],
     "enunciado": apoio(" ".join(T(8, "No Brasil, nas primeiras décadas do século XX", "capaz de protegê-las")) + " " + " ".join(T(8, "de tal exploração. Somente", "de trabalho em 8 horas diárias.")))
                  + url("https://tinyurl.com/y5sq4pkp", "15.10.2019") + p("Segundo o texto,"),
     "explicacao": "<p>O texto diz que, na Era Vargas, houve a regulamentação do trabalho de mulheres e crianças e que Getúlio Vargas fixou a jornada em 8 horas diárias. Alternativa <strong>C</strong>.</p><p>As manifestações conquistaram direitos, não a jornada de 10 a 14 horas (A). No começo do século não havia leis que protegessem as operárias (B e D). E os 68% se referem à mão de obra da indústria têxtil, não à população brasileira (E).</p>"},
19: {"materia": "História", "assunto": "História contemporânea", "tags": ["Guerra Fria"],
     "explicacao": "<p>Na Guerra da Coreia (1950–1953) e na do Vietnã (1955–1975), EUA e URSS apoiaram lados opostos, e também disputaram influência nas independências africanas, como em Angola e Moçambique. Alternativa <strong>A</strong>.</p><p>Os conflitos de B, D e E são dos séculos XVIII e XIX, antes da Guerra Fria. E a Guerra do Golfo (1991) e a da Síria (a partir de 2011) são do fim ou depois dela (C).</p>"},
20: {"materia": "Química", "assunto": "Estequiometria", "tags": ["mol", "constante de Avogadro"],
     "enunciado": SLIME + P20, "imagens": SLIME_IMG,
     "alternativas": alts("6,2 × 10<sup>22</sup>", "7,1 × 10<sup>22</sup>", "9,1 × 10<sup>22</sup>", "2,0 × 10<sup>23</sup>", "3,0 × 10<sup>23</sup>"),
     "explicacao": "<p>A receita usa duas colheres: 2 · 5 = 10 g de NaHCO₃. Isso é 10 ÷ 84 ≈ 0,119 mol, ou 0,119 · 6 × 10²³ ≈ <strong>7,1 × 10²²</strong> unidades. Alternativa <strong>B</strong>.</p><p>Usar uma colher só daria cerca de 3,6 × 10²². E os outros valores vêm de erros na massa molar ou na potência de dez.</p><p>Observação: o bicarbonato de sódio é um composto iônico; a rigor, contam-se “fórmulas” ou “unidades”, e não moléculas, mas a questão usa a palavra no sentido comum.</p>"},
21: {"materia": "Química", "assunto": "Reações químicas", "tags": ["balanceamento"],
     "enunciado": p("Assinale a alternativa que contém a equação química balanceada que representa, corretamente, a reação que ocorre entre o ácido bórico e o bicarbonato de sódio."), "apoio_de": (20, P20),
     "alternativas": alts("H<sub>3</sub>BO<sub>3</sub> + Na<sub>3</sub>HCO<sub>3</sub> → Na<sub>3</sub>BO<sub>3</sub> + H<sub>2</sub>O + CO<sub>2</sub>", "H<sub>3</sub>BO<sub>3</sub> + 3 NaHCO<sub>3</sub> → Na<sub>3</sub>BO<sub>3</sub> + H<sub>2</sub>O + CO<sub>2</sub>",
                          "H<sub>3</sub>BO<sub>3</sub> + 3 NaHCO<sub>3</sub> → Na<sub>3</sub>BO<sub>3</sub> + 3 H<sub>2</sub>O + 3 CO<sub>2</sub>", "H<sub>3</sub>BO<sub>2</sub> + 3 NaHCO<sub>3</sub> → Na<sub>3</sub>BO<sub>2</sub> + 3 H<sub>2</sub>O + 3 CO<sub>2</sub>",
                          "H<sub>2</sub>BO<sub>2</sub> + 2 NaHCO<sub>3</sub> → Na<sub>2</sub>BO<sub>2</sub> + 2 H<sub>2</sub>O + 2 CO<sub>2</sub>"),
     "explicacao": "<p>As fórmulas corretas são H₃BO₃, NaHCO₃ e Na₃BO₃ (dadas no texto). Para formar Na₃BO₃ são necessários 3 NaHCO₃, que trazem 3 C (3 CO₂) e, com os 3 H do ácido, 6 H (3 H₂O). Conferindo O: 3 + 9 = 12 de um lado; 3 + 3 + 6 = 12 do outro. Alternativa <strong>C</strong>.</p><p>A usa a fórmula errada Na₃HCO₃. B não está balanceada. D e E trocam as fórmulas do ácido bórico e do borato.</p>"},
22: {"materia": "Química", "assunto": "Polaridade e solubilidade", "tags": ["forças intermoleculares"],
     "enunciado": p("A interação entre os íons sódio e as estruturas do PVAc é denominada, corretamente, como"), "apoio_de": (20, P20),
     "alternativas": alts("dipolo-dipolo.", "dipolo instantâneo-dipolo induzido.", "ligação de hidrogênio.", "íon-dipolo.", "íon-íon."),
     "explicacao": "<p>O Na⁺ é um íon e se atrai pelo oxigênio da carbonila, que tem carga parcial negativa (δ⁻) num grupo polar: é uma interação <strong>íon-dipolo</strong>. Alternativa <strong>D</strong>.</p><p>Dipolo-dipolo e dipolo induzido envolvem só moléculas, sem íons (A e B). Não há H ligado a F, O ou N interagindo (C). E o PVAc não é um íon (E).</p>"},
23: {"materia": "Química", "assunto": "Funções orgânicas", "tags": ["hidrólise", "ácido carboxílico"],
     "enunciado": p("Na equação 2, o nome da reação química que ocorre entre o PVAc e a água e o nome da função orgânica a que pertence o composto X, formado na reação, são, respectivamente,"), "apoio_de": (20, P20),
     "alternativas": alts("hidrólise e álcool.", "hidrólise e acetona.", "hidrólise e ácido carboxílico.", "esterificação e ácido carboxílico.", "esterificação e acetona."),
     "explicacao": "<p>O PVAc é um éster que reage com água e se quebra: é uma <strong>hidrólise</strong>. O composto X, H₃C–COOH, tem o grupo carboxila: é um <strong>ácido carboxílico</strong> (o ácido acético). Alternativa <strong>C</strong>.</p><p>A esterificação é a reação inversa, que forma ésteres (D e E). O álcool é o PVA, não o composto X (A). E acetona é uma cetona, sem grupo –OH (B e E).</p>"},
24: {"materia": "Química", "assunto": "Estrutura atômica", "tags": ["ligações químicas"],
     "enunciado": p("Na equação 3, as ligações químicas I, II, III e IV, formadas no trecho da cadeia do <em>slime</em>, são denominadas"), "apoio_de": (20, P20),
     "alternativas": alts("ligações iônicas.", "ligações covalentes.", "ligações metálicas.", "ligações de hidrogênio.", "ligações apolares."),
     "explicacao": "<p>As ligações I a IV unem o oxigênio a átomos de carbono e de boro, todos não metais, que compartilham elétrons: são <strong>ligações covalentes</strong>. Alternativa <strong>B</strong>.</p><p>Não há metal formando íons nessas ligações (A e C). Ligações de hidrogênio são interações entre moléculas (D). E as ligações entre O e C ou B são polares (E).</p>"},
25: {"materia": "Inglês", "assunto": "Interpretação de texto",
     "enunciado": RACISMO + P25,
     "explicacao": "<p>O texto cita discriminação contra “black Britons and those of south Asian origin – particularly Pakistanis”: <strong>negros e asiáticos</strong> (do sul da Ásia). Alternativa <strong>D</strong>.</p><p>O estudo compara os candidatos de minorias aos brancos britânicos (caucasianos), que não são discriminados (A e E). E o texto não menciona latinos (B e C).</p>"},
26: {"materia": "Inglês", "assunto": "Interpretação de texto",
     "enunciado": p("Segundo o texto, estudos indicam que a discriminação está presente tanto na busca por emprego, quanto"), "apoio_de": (25, P25),
     "explicacao": "<p>O texto cita a série <em>Bias in Britain</em>, segundo a qual pessoas de minorias sofrem discriminação “when seeking a room to rent” (ao procurar um quarto para alugar): na <strong>locação de residência</strong>. Alternativa <strong>A</strong>.</p><p>O texto não fala de comércio, vistos, política ou seguros (B, C, D e E).</p>"},
27: {"materia": "Inglês", "assunto": "Interpretação de texto",
     "enunciado": p("De acordo com o Professor Anthony Heath, o que causa surpresa em relação à pesquisa apresentada é que"), "apoio_de": (25, P25),
     "explicacao": "<p>O professor diz: “The absence of any real decline in discrimination against black British and people of Pakistani background is a disturbing finding” (a ausência de queda real na discriminação contra negros e paquistaneses é um achado perturbador). Alternativa <strong>E</strong>.</p><p>O estudo diz que a discriminação ficou “unchanged”, inalterada, e não que aumentou ou diminuiu (A, B e C). E não menciona latinos (D).</p>"},
28: {"materia": "Inglês", "assunto": "Interpretação de texto",
     "enunciado": p("Segundo a fala da Dra. Zubaida Haque, o mais preocupante é"), "apoio_de": (25, P25),
     "explicacao": "<p>Ela diz que não é só o racismo velado ou inconsciente que preocupa: “it’s overt and conscious racism” (é o racismo aberto e consciente), com candidatos selecionados pela etnia ou pelo nome. Alternativa <strong>E</strong>.</p><p>A fala não trata de xenofobia, misoginia, sexismo nem antissemitismo (A, B, C e D).</p>"},
29: {"materia": "Inglês", "assunto": "Interpretação de texto",
     "enunciado": p("A diretora do grupo Runnymede acredita que o panorama descrito"), "apoio_de": (25, P25),
     "explicacao": "<p>Ela diz que, para as minorias, a discriminação significa “higher unemployment, lower wages, poorer conditions and less security in work and life”: o panorama <strong>degrada as condições de trabalho das minorias</strong>. Alternativa <strong>B</strong>.</p><p>Ela não fala de violência (A), diz que há menos segurança, não mais (C), afirma que não há consequências reais para os empregadores (D) e critica a lei atual, sem dizer que leis mais rígidas são impedidas (E).</p>"},
30: {"materia": "Matemática", "assunto": "Operações e problemas", "tags": ["aplicativos de transporte"],
     "enunciado": p("Amanda resolveu complementar seu orçamento doméstico como motorista por aplicativo. Como já possui um automóvel inscreveu-se numa plataforma em que o valor cobrado do passageiro por viagem depende basicamente de três fatores:",
                    "• o valor fixo de R$ 2,00 cobrado no início de qualquer viagem;<br>• o valor de R$ 0,26 por minuto de viagem;<br>• o valor de R$ 1,40 por quilômetro rodado.",
                    "Além disso, Amanda sabe que", "• a plataforma do aplicativo retém um quarto do valor pago pelo passageiro;<br>• terá um custo de combustível no valor de R$ 0,28 por quilômetro rodado.",
                    "Suponha que ela realizará apenas viagens de 5 km, com duração de 10 minutos cada.",
                    "Considerando que Amanda deseja receber mensalmente o valor líquido mínimo de R$ 2.190,00, o menor número de viagens mensais, como motorista de aplicativo, que Amanda precisa fazer é"),
     "alternativas": alts("280", "300", "320", "340", "360"),
     "explicacao": "<p>Cada viagem custa ao passageiro 2,00 + 10 · 0,26 + 5 · 1,40 = 2,00 + 2,60 + 7,00 = R$ 11,60. Amanda fica com três quartos: 8,70. Tirando o combustível (5 · 0,28 = 1,40), sobram R$ 7,30 por viagem. São 2 190 ÷ 7,30 = <strong>300</strong> viagens. Alternativa <strong>B</strong>.</p><p>Esquecer o combustível daria cerca de 252 viagens, e esquecer a retenção da plataforma, cerca de 214.</p>"},
31: {"materia": "Matemática", "assunto": "Funções", "tags": ["função do 2º grau", "máximo"],
     "alternativas": alts("R$ 2.000,00", "R$ 2.200,00", "R$ 2.350,00", "R$ 2.450,00", "R$ 2.540,00"),
     "explicacao": "<p>Com x assentos vazios, viajam 50 − x passageiros, e cada um paga 40 + 2x. A receita é R(x) = (50 − x)(40 + 2x) = −2x² + 60x + 2 000. O máximo fica no vértice, x = 60 ÷ 4 = 15: R = 35 · 70 = <strong>R$ 2.450,00</strong>. Alternativa <strong>D</strong>.</p><p>R$ 2.000,00 é a receita com o ônibus lotado (A), que não é a maior.</p>"},
32: {"materia": "Matemática", "assunto": "Razão e proporção", "tags": ["misturas"],
     "alternativas": alts("10", "20", "30", "40", "50"),
     "explicacao": "<p>Na razão 2 : 3, os 50 L têm 20 L de gasolina e 30 L de álcool. Para ficar em 1 : 3, o álcool precisa ser o triplo da gasolina: 60 L. Faltam 60 − 30 = <strong>30 L</strong>. Alternativa <strong>C</strong>.</p><p>10 e 20 L não chegam à razão 1 : 3, e 40 e 50 L passam dela.</p>"},
33: {"materia": "Matemática", "assunto": "Probabilidade", "tags": ["combinação"],
     "alternativas": alts("20%", "30%", "40%", "50%", "60%"),
     "explicacao": "<p>Escolher 3 de 5 substâncias dá C(5, 3) = 10 poções. A poção fica sem efeito quando contém as duas substâncias que se anulam; a terceira pode ser qualquer uma das outras 3: são 3 casos. A probabilidade é 3 ÷ 10 = <strong>30%</strong>. Alternativa <strong>B</strong>.</p><p>60% é a probabilidade de conter pelo menos uma das duas, não as duas (E). E 70% seria a chance de a poção funcionar.</p>"},
34: {"materia": "Matemática", "assunto": "Geometria plana", "tags": ["área do triângulo", "trigonometria"],
     "enunciado": p("Na figura temos um mapa onde se localiza a Praça Tales de Mileto. A prefeitura pretende cobri-la completamente com grama.") + "[[fig:1]]"
                  + apoio("Considere retilíneos esses trechos de ruas e avenidas")
                  + p("Admita que a medida do ângulo agudo formado entre a Rua Fibonacci e a Avenida Descartes é igual a 60º, e que a Avenida Bhaskara é paralela à Avenida Descartes.", "Nessas condições, o total da área a ser gramada é, em metros quadrados, igual a"),
     "imagens": figs(("q34", "Mapa de ruas: a Avenida Bhaskara e a Avenida Descartes são horizontais e paralelas; a Rua Fibonacci é inclinada e corta as duas; a Rua Arquimedes desce em diagonal. A Praça Tales de Mileto é um triângulo entre a Rua Fibonacci, a Rua Arquimedes e a Avenida Bhaskara, com um lado de 240 m ao longo da Rua Fibonacci e um lado de 300 m ao longo da Avenida Bhaskara.")),
     "alternativas": alts("20 400 · √3", "20 400 · √2", "27 000", "18 000 · √3", "12 000"),
     "explicacao": "<p>Como a Avenida Bhaskara é paralela à Descartes, o ângulo entre a Rua Fibonacci e a Bhaskara também é 60° (ângulos correspondentes). Esse é o ângulo entre os lados de 240 m e 300 m da praça. A área é \\(\\tfrac{1}{2} \\cdot 240 \\cdot 300 \\cdot \\text{sen}\\,60° = 36\\,000 \\cdot \\tfrac{\\sqrt{3}}{2} = 18\\,000\\sqrt{3}\\) m². Alternativa <strong>D</strong>.</p><p>36 000 sem o seno não aparece; 27 000 e 12 000 vêm de usar outros ângulos ou fórmulas (C e E).</p>"},
35: {"materia": "Física", "assunto": "Cinemática", "tags": ["gráfico v × t", "paraquedas"],
     "enunciado": p("Considere o gráfico de velocidade vertical por tempo") + "[[fig:1]]"
                  + p("Considerando-se um sistema de referência ideal orientado de cima para baixo, podemos associar o gráfico ao movimento aproximado de"),
     "imagens": figs(("q35", "Gráfico de velocidade por tempo: a velocidade cresce em linha reta de 0 até V₁ no instante t₁; fica constante em V₁ até t₂; cai rapidamente para V₂, menor, entre t₂ e t₃; fica constante em V₂ até t₄; e cai até zero em t₅.")),
     "explicacao": "<p>O paraquedista cai acelerando (de 0 a t₁), atinge uma velocidade limite (V₁), abre o paraquedas e freia (t₂ a t₃), desce com uma nova velocidade constante menor (V₂) e para ao chegar ao solo (t₅). Alternativa <strong>D</strong>.</p><p>O balão e o foguete sobem, contra o sentido positivo adotado (A e B). A fruta não tem trechos de velocidade constante nem freia em duas etapas (C). E a águia não para no solo (E).</p>"},
36: {"materia": "Física", "assunto": "Movimento circular", "tags": ["força centrípeta"],
     "enunciado": p(*[it(x, "tether", "Tether in Space 2019") for x in T(14, "O tether consiste em dois objetos fixos", "mais longas.")]) + "[[fig:1]]" + fonte("Obs.: Imagem fora de escala.")
                  + p(*T(14, "Uma espaçonave de 100 toneladas", "em newtons, é", ["Assumindo que a massa"]))
                  + apoio("Lembre-se de que<br>\\(a_c = \\dfrac{V^2}{R}\\)"),
     "imagens": figs(("q36", "Esquema fora de escala: um asteroide no centro de uma trajetória circular pontilhada, ligado por um cabo a uma espaçonave na borda do círculo. A seta da velocidade tangencial da nave indica |Vt| = 28 800 km/h.")),
     "alternativas": alts("6,4 × 10<sup>7</sup>", "6,4 × 10<sup>5</sup>", "6,4 × 10<sup>3</sup>", "8,3 × 10<sup>4</sup>", "8,3 × 10<sup>6</sup>"),
     "explicacao": "<p>Em unidades do SI: v = 28 800 ÷ 3,6 = 8 000 m/s, R = 100 km = 10⁵ m e m = 100 t = 10⁵ kg. F = m · v² ÷ R = 10⁵ · (8 × 10³)² ÷ 10⁵ = 64 × 10⁶ = <strong>6,4 × 10⁷ N</strong>. Alternativa <strong>A</strong>.</p><p>As alternativas com 8,3 vêm de usar a velocidade em km/h (D e E), e as demais, de erros nas potências de dez (B e C).</p>"},
37: {"materia": "Física", "assunto": "Óptica", "tags": ["eclipse solar"],
     "enunciado": apoio(" ".join(T(15, "Em 2019 comemora-se, em todo o mundo", "Teoria da Relatividade Geral do físico Albert Einstein.")))
                  + fonte("&lt;http://tinyurl.com/y2rn2ptp&gt;. Acesso em: 10.10.2019. Adaptado.") + p("Sobre o eclipse referido, é correto afirmar que"),
     "explicacao": "<p>No eclipse solar, a <strong>Lua passa entre o Sol e a Terra</strong> e projeta sua sombra sobre a Terra. Onde cai a sombra, o eclipse é total; onde cai a penumbra, é parcial. Alternativa <strong>E</strong>.</p><p>Eclipses não provam que a Terra é plana (A). As regiões estão trocadas em B. A Terra entre o Sol e a Lua é o eclipse lunar (C). E o Sol não projeta sombra, ele é a fonte de luz (D).</p>"},
38: {"materia": "Física", "assunto": "Física moderna", "tags": ["relatividade restrita"],
     "explicacao": "<p>Pela Relatividade Restrita, para um objeto muito rápido em relação ao observador, o tempo passa mais devagar (<strong>dilatação do tempo</strong>) e o comprimento na direção do movimento diminui (<strong>contração do comprimento</strong>). Alternativa <strong>C</strong>.</p><p>O comprimento contrai, não dilata (A e B), e as duas coisas acontecem juntas (D e E). Observação: a rigor, nenhum objeto com massa chega à velocidade da luz; os efeitos aparecem perto dela.</p>"},
39: {"materia": "Física", "assunto": "Termologia", "tags": ["escalas termométricas", "taxa de variação"],
     "enunciado": p(*[it(x, "pre-cooler") for x in T(15, "Recentemente, uma empresa britânica apresentou", "térmico, em °C/s, é", ["Isso só é possível", "Com base nessas informações"])]),
     "alternativas": alts("25 460", "20 000", "2 546", "2 000", "250"),
     "explicacao": "<p>Uma variação de 1 000 K é também uma variação de 1 000 °C, porque as duas escalas têm graus do mesmo tamanho. Em 50 ms = 0,05 s, a taxa é 1 000 ÷ 0,05 = <strong>20 000 °C/s</strong>. Alternativa <strong>B</strong>.</p><p>Converter a variação somando 273, como se fosse uma temperatura, leva a valores como 25 460 (A). E 2 000 vem de usar 0,5 s (D).</p>"},
40: {"materia": "Geografia", "assunto": "População", "tags": MULTI + ["vacinação", "saúde pública"],
     "enunciado": apoio(*T(15, "O Brasil é reconhecido internacionalmente", "antigas e controladas no País.", ["No entanto, a cobertura vacinal", "Para o governo, é cedo", "O que o governo mais teme"]))
                  + url("https://tinyurl.com/y8ur2re7", "10.10.2019") + p("Uma consequência do problema abordado é"),
     "explicacao": "<p>Com menos gente vacinada, doenças controladas podem voltar a circular, mais pessoas adoecem e o sistema de saúde gasta mais com tratamento. Alternativa <strong>D</strong>.</p><p>A falta de vacinação não elimina os agentes de doença; ao contrário, ajuda a espalhá-los (A e C). A vacina estimula, e não interrompe, a produção de anticorpos (B). E a asma não é uma doença infecciosa evitada por vacina (E).</p>"},
41: {"materia": "Geografia", "assunto": "Tectônica de placas", "tags": ["Cordilheira dos Andes", "hidrografia"],
     "enunciado": apoio(T(16, "“A América do Sul ficou como um continente", "no Equador”.")[0])
                  + fonte("MIRANDA, Evaristo Eduardo de. <em>Quando o Amazonas corria para o Pacífico: uma história desconhecida da Amazônia.</em> Petrópolis, RJ. 2 ed.: VOZES, 2007.")
                  + p("A inversão do sentido dos rios amazônicos, mencionada no texto, ocorreu em consequência"),
     "explicacao": "<p>O soerguimento dos <strong>Andes</strong>, no Terciário (era Cenozoica), bloqueou a saída dos rios para o Pacífico. A água se acumulou e acabou escoando para leste, rumo ao Atlântico, como o Amazonas faz hoje. Alternativa <strong>B</strong>.</p><p>A Pangeia se formou no fim da era Paleozoica, não no Pré-Cambriano (A). Não houve desertificação na Amazônia no Jurássico (C). A abertura do Atlântico ocorreu no Mesozoico (D). E o istmo do Panamá surgiu há poucos milhões de anos, não no Carbonífero (E).</p>"},
42: {"materia": "Geografia", "assunto": "Cartografia", "tags": ["escala"],
     "alternativas": alts("1:3 000", "1:30 000", "1:300 000", "1:3 000 000", "1:30 000 000"),
     "explicacao": "<p>1 500 km = 150 000 000 cm. A escala é 50 : 150 000 000 = 1 : 3 000 000. Alternativa <strong>D</strong>.</p><p>As outras escalas erram a conversão de quilômetros para centímetros por uma ou mais potências de dez.</p>"},
43: {"materia": "Geografia", "assunto": "Geopolítica", "tags": ["Revolução Islâmica", "Irã"],
     "enunciado": apoio(T(16, "“No Oriente Médio, nos anos 1950", "controle estadunidense.”")[0])
                  + url("https://tinyurl.com/y5jobeuu", "10.10.2019")
                  + p(*T(16, "Desde 1953, o Irã foi um grande aliado", "em decorrência da", ["O fato que levou"])),
     "explicacao": "<p>A <strong>Revolução Islâmica</strong> de 1979 derrubou o xá Reza Pahlevi, aliado dos EUA, e criou a República Islâmica do Irã, liderada pelo aiatolá Khomeini. A crise dos reféns na embaixada americana levou ao rompimento em 1980. Alternativa <strong>E</strong>.</p><p>Saddam Hussein governava o Iraque, que atacou o Irã em 1980 (A). Não houve revolução socialista no Irã (B). Quem invadiu o Kuwait foi o Iraque, em 1990 (C). E o 11 de Setembro foi em 2001, e Bin Laden era saudita (D).</p>"},
44: {"materia": "Geografia", "assunto": "Globalização", "tags": ["capitalismo", "livre mercado"],
     "enunciado": apoio(it(T(17, "“O livre mercado é um termo conciso", "serviços não-tangíveis.”")[0], "commodities"))
                  + url("https://tinyurl.com/yywpe8lx", "10.10.2019") + p("A expressão “livre mercado”, presente no texto, é típica de uma sociedade"),
     "explicacao": "<p>O livre mercado, com trocas voluntárias reguladas pela oferta e pela demanda, é a base da sociedade <strong>capitalista</strong>. Alternativa <strong>E</strong>.</p><p>O anarquismo rejeita o Estado, mas também a lógica de mercado capitalista (A). No feudalismo, a relação entre senhores e servos era de obrigações, não de livre negociação (B). No socialismo, a economia é planejada pelo Estado (C). E as monarquias têm poder central (D).</p>"},
45: {"materia": "Biologia", "assunto": "Botânica", "tags": ["câmbio", "anéis de crescimento"],
     "enunciado": apoio(T(17, "Os cientistas que realizam pesquisas históricas", "são mais estreitos.")[0])
                  + fonte("(Amabis, José Mariano; MARTHO, Gilberto Rodrigues. <em>Biologia dos Organismos.</em> – 3ª. ed. – São Paulo: Moderna, 2009. Adaptado.)")
                  + p("Sobre os anéis de crescimento de certas espécies de árvores, é correto afirmar que são formados"),
     "explicacao": "<p>O câmbio produz xilema de forma diferente ao longo do ano: na primavera, o xilema tem vasos largos e paredes finas (xilema primaveril, mais claro); no fim do verão, vasos estreitos e paredes grossas (xilema estival, mais escuro). Cada par forma um anel. Alternativa <strong>A</strong>.</p><p>No inverno o câmbio para, e o xilema de vasos largos é o primaveril (B). O floema conduz seiva elaborada, e o câmbio depende do ambiente (C). Os vasos lenhosos conduzem seiva bruta e crescem menos no inverno (D). E os anéis não se formam só no verão (E).</p>"},
46: {"materia": "Biologia", "assunto": "Ecologia", "tags": ["micorrizas", "mutualismo"],
     "explicacao": "<p>Nas micorrizas, as hifas aumentam a área de absorção das raízes e ajudam a planta a obter minerais; em troca, o fungo recebe açúcares produzidos pela planta. É um mutualismo. Alternativa <strong>E</strong>.</p><p>A relação não é de parasitismo (A). Fungos não fazem fotossíntese (B). No comensalismo um ganha e o outro não é afetado; aqui os dois ganham (C). E os fungos ajudam, e não impedem, a absorção de sais (D).</p>"},
47: {"materia": "Biologia", "assunto": "Doenças e saúde", "tags": ["verminoses"],
     "enunciado": p(*T(18, "Os nematelmintos são vermes que causam", "por nematelmintos nos seres humanos.", ["Os textos se referem"]))
                  + apoio("<strong>I</strong> " + T(18, "Verminose, habitualmente sem sintomatologia", "contaminados com fezes humanas.")[0])
                  + apoio("<strong>II</strong> " + " ".join(T(18, "Verminose que pode ser assintomática", "têm como hábito andar descalças.")))
                  + p("Assinale a alternativa que indica, correta e respectivamente, as verminoses descritas nos textos I e II."),
     "alternativas": colunas(["I", "II"], [["Filariose", "Ascaridíase"], ["Ancilostomose", "Filariose"], ["Ascaridíase", "Ancilostomose"], ["Ancilostomose", "Ascaridíase"], ["Ascaridíase", "Filariose"]]),
     "explicacao": "<p>I: transmissão pela ingestão de ovos em água e alimentos contaminados, com risco de obstrução intestinal por muitos vermes: <strong>ascaridíase</strong> (lombriga). II: larvas que penetram pela pele dos pés e causam anemia por perda de ferro: <strong>ancilostomose</strong> (amarelão). Alternativa <strong>C</strong>.</p><p>A filariose é transmitida por mosquitos e afeta os vasos linfáticos (A, B e E). D inverte as duas doenças.</p>"},
48: {"materia": "Biologia", "assunto": "Botânica", "tags": ["pteridófitas", "ciclo de vida"],
     "enunciado": p("O esquema representa o ciclo reprodutivo de uma pteridófita (samambaia).") + "[[fig:1]]" + p("Sobre esse ciclo, é correto afirmar que"),
     "imagens": figs(("q48", "Esquema circular do ciclo: o esporo dá origem ao gametófito, que produz anterozoide e oosfera; os dois se unem e formam o zigoto, que se desenvolve no esporófito; o esporófito produz esporos, recomeçando o ciclo.")),
     "explicacao": "<p>Nas samambaias, o esporófito (diploide) é a planta que vemos, a geração predominante. Ele forma esporos por <strong>meiose</strong>. Os esporos (haploides) originam o gametófito, que produz gametas por mitose. Alternativa <strong>B</strong>.</p><p>O gametófito forma gametas por mitose, não por meiose (A). A união do anterozoide com a oosfera forma o zigoto, que dá origem ao esporófito (C). O gametófito é haploide e pequeno (D). E o esporófito é diploide (E).</p>"},
49: {"materia": "Biologia", "assunto": "Genética", "tags": ["sistema ABO"],
     "enunciado": p(*T(19, "Os tipos sanguíneos do sistema ABO", "grupo O.", ["Esses tipos sanguíneos", "Entre os alelos", "Considere a seguinte"]),
                    "Sabendo-se que o marido tem o aglutinogênio A, podemos afirmar que os genótipos da mulher e do seu marido são, respectivamente,"),
     "trocar": [("alelos múltiplos: IA, IB e i", "alelos múltiplos: <strong>I<sup>A</sup>, I<sup>B</sup> e i</strong>"), ("Entre os alelos IA e IB", "Entre os <strong>alelos I<sup>A</sup> e I<sup>B</sup></strong>"), ("sobre o alelo i", "sobre o <strong>alelo i</strong>")],
     "alternativas": colunas(["♀", "♂"], [["I<sup>B</sup>i", "I<sup>B</sup>i"], ["I<sup>B</sup>I<sup>B</sup>", "I<sup>A</sup>i"], ["I<sup>B</sup>i", "I<sup>A</sup>i"], ["I<sup>A</sup>I<sup>B</sup>", "I<sup>B</sup>I<sup>B</sup>"], ["I<sup>B</sup>i", "I<sup>A</sup>I<sup>A</sup>"]]),
     "explicacao": "<p>O filho é do grupo O (ii): recebeu um alelo i de cada um. A mulher tem anti-A, então não tem aglutinogênio A: é B ou O. Pelas alternativas, ela é I<sup>B</sup>i. O marido tem aglutinogênio A e precisa ter um i: I<sup>A</sup>i. Alternativa <strong>C</strong>.</p><p>Quem é I<sup>B</sup>I<sup>B</sup> ou I<sup>A</sup>I<sup>A</sup> não tem o alelo i e não pode ter filho O (B, D e E). E I<sup>B</sup>i não tem aglutinogênio A, então não pode ser o marido (A).</p>"},
50: {"materia": "Português", "assunto": "Gêneros textuais", "tags": ["charge"],
     "enunciado": p("Leia a charge.") + "[[fig:1]]" + url("https://tinyurl.com/y4xtwcwo", "19.10.2019", "") + p("De acordo com as informações verbais e não verbais apresentadas na charge, pode-se depreender, corretamente, que"),
     "imagens": figs(("q50", "Charge de Tiens em três quadros. 1: um homem diante de uma agência de empregos com várias placas “Não há vagas”. 2: o homem lê o jornal de classificados e ouve ao telefone: “Desculpe, mas não há vagas!”. 3: o mesmo homem, agora motorista de aplicativo num carro com a placa “Uber”, responde a uma mulher com duas crianças que pede “3 pessoas, por favor”: “Ok, há vagas!”.")),
     "explicacao": "<p>Sem conseguir emprego, o homem persiste e passa a dirigir por aplicativo, onde agora é ele quem tem “vagas”. A charge mostra a <strong>resiliência e a persistência</strong> que levam as pessoas a se adaptar a novas formas de trabalho. Alternativa <strong>E</strong>.</p><p>A charge mostra falta de vagas, não sobra (A e B). O transporte por aplicativo é justamente uma atividade alternativa (C). E as vagas formais não são inúmeras, mas inexistentes (D).</p><p>Observação do Treineiros: a charge também pode ser lida como crítica à precarização do trabalho, que é o tema de outras questões da prova; a banca escolheu a leitura da adaptação.</p>"},
51: {"materia": "Português", "assunto": "Interpretação de texto",
     "enunciado": ANTUNES + P51,
     "anulacao": {"fonte": "oficial", "motivo": ANUL.format(L="C") + "Pela análise do Treineiros, a alternativa C é a que melhor resume o texto, mas ela fala em “desumanização das relações trabalhistas” como causa, enquanto o autor atribui a perda de sentido da vida ao capitalismo e à nova divisão do trabalho; a relação de causa e efeito da alternativa não está explícita no texto, o que pode ter motivado a anulação."},
     "explicacao": "<p>Questão anulada. Se fosse corrigida pela letra que o gabarito traz (C): o autor diz que a vida fica “desprovida de sentido no trabalho” e se esgota “no mundo sublimado do consumo” ou “na labuta incansável pelas qualificações de todo tipo”. É o que a alternativa C resume.</p><p>As mudanças recentes geram precarização, não lucro ao trabalhador (A), nem carteira assinada (B). A revista é justamente um esforço de pesquisadores sobre o tema (D). E o texto fala em degradação, não em garantias trabalhistas desde a Revolução Industrial (E).</p>"},
52: {"materia": "Português", "assunto": "Sintaxe", "tags": ["reescrita", "voz passiva"],
     "enunciado": p("Dentre as propostas de reescrita dos diferentes trechos retirados do texto, assinale a única que mantém o sentido original e que respeita as normas da variedade culta da língua portuguesa."),
     "apoio_de": (51, P51),
     "alternativas": colunas(["Texto original", "Texto reescrito"], [
         ["“É por isso que estamos presenciando uma desconstrução do trabalho sem precedentes...”", "É por isso que uma desconstrução inédita do trabalho está sendo presenciada por nós..."],
         ["“A vida se consolida, cada vez mais, como sendo desprovida de sentido no trabalho...”", "Consolidam a vida, ininterruptamente, tirando do trabalho o sentido..."],
         ["“...o capitalismo aprofundou ainda mais as penalizações que está impondo ao universo laborativo...”", "As penalizações impostas ao universo laborativo aprofundaram ainda mais o capitalismo..."],
         ["“...as últimas décadas do século passado e os inícios do atual vêm presenciando a generalização de ‘outras formas e modalidades de precarização’ ...”", "... entre meados do século XIX e início do século XXI, a difusão de “outras formas e modalidades de precarização” foi presenciada..."],
         ["“Este número especial da Revista Katálysis... é uma contribuição efetiva para a linhagem crítica, atualizada e original, tanto pelos temas selecionados, quanto pela qualidade e competência dos colaboradores presentes...”", "Uma contribuição efetiva pela linguagem crítica moderna e clássica foi feita pelo número especial da Revista Katálysis, devido aos temas abordados e à qualidade dos colaboradores..."]]),
     "anulacao": {"fonte": "oficial", "motivo": ANUL.format(L="A") + "Pela análise do Treineiros, há um problema no próprio enunciado: o trecho citado como original na alternativa A (“uma desconstrução do trabalho sem precedentes”) não é igual ao do texto (“uma desconstrução sem precedentes do trabalho”), e a troca muda o que é “sem precedentes”. Isso compromete justamente a alternativa que o gabarito indicava."},
     "explicacao": "<p>Questão anulada. Se fosse corrigida pela letra que o gabarito traz (A): a reescrita passa a frase para a voz passiva (“está sendo presenciada por nós”) e troca “sem precedentes” por “inédita”, mantendo o sentido.</p><p>B troca o sujeito e diz que alguém “tira do trabalho o sentido”. C inverte a relação: no original, é o capitalismo que aprofunda as penalizações. D muda o período (“meados do século XIX”). E troca “linhagem” por “linguagem” e “atualizada e original” por “moderna e clássica”.</p>"},
53: {"materia": "Português", "assunto": "Formação de palavras",
     "enunciado": p("Os termos “continuidade”, “desconstrução” e “desmanche” são palavras constituídas por diferentes processos de formação de palavras.",
                    "Assinale a alternativa cujas palavras são formadas, respectivamente, pelos mesmos processos dos vocábulos apresentados no enunciado."),
     "apoio_de": (51, P51),
     "explicacao": "<p>“Continuidade” (contínuo + -idade) é derivação sufixal; “desconstrução” (des- + construção, com o sufixo -ção de construir) é derivação prefixal e sufixal; “desmanche” vem do verbo desmanchar por derivação regressiva. O mesmo vale para “vivência” (viver + -ência), “rememoração” (re- + memorar + -ção) e “renúncia” (de renunciar, regressiva). Alternativa <strong>B</strong>.</p><p>“Endeusar” e “entardecer” são parassintéticas, e “aguardente” é composição (A e C). “Desmantelar” não é derivação regressiva (D). E “remontar” é prefixal (E).</p>"},
54: {"materia": "Português", "assunto": "Figuras de linguagem", "tags": ["paronomásia"],
     "enunciado": p("Os termos destacados no texto são exemplos de paronomásia, figura sonora definida, segundo o Dicionário Houaiss de Língua Portuguesa, como “figura de linguagem que extrai expressividade da combinação de palavras que apresentam semelhança fônica, mas possuem sentidos diferentes”.",
                    "Assinale a alternativa em que o autor também utilizou a paronomásia na construção de seus versos."),
     "apoio_de": (51, P51),
     "imagens": figs(("q54a", "Versos de Manuel Bandeira, do poema “Pneumotórax”: uma enumeração de sintomas de doença, o lamento pela vida que não foi vivida e a repetição da palavra tosse."),
                     ("q54b", "Versos de Carlos Drummond de Andrade: uma imagem da lua no céu, chamada de irônica e diurética, comparada a uma gravura de sala de jantar."),
                     ("q54c", "Versos de Carlos Drummond de Andrade: o eu lírico lamenta não ter amado o semelhante nem cuidado dos outros, e só ter dito algumas palavras melodiosas ao voltar da festa."),
                     ("q54d", "Versos de Paul Verlaine, em tradução, sobre a arte poética: a música antes de tudo, o ímpar, o que é vago e solúvel no ar, sem nada que pouse ou pese. Os verbos “preza” e “pesa”, no fim do primeiro e do último verso, têm sons parecidos."),
                     ("q54e", "Versos de Carlos Drummond de Andrade sobre o amor, que vive entre brigar e perdoar, com a repetição invertida “briga perdoa perdoa briga”.")),
     "alternativas": {"A": "[[fig:1]]", "B": "[[fig:2]]", "C": "[[fig:3]]", "D": "[[fig:4]]", "E": "[[fig:5]]"},
     "explicacao": "<p>Em Verlaine, “preza” e “pesa” têm som quase igual e sentidos diferentes, como “informatização” e “informalização” no texto: é paronomásia. Alternativa <strong>D</strong>.</p><p>A repete a mesma palavra (“tosse”), o que é anáfora ou repetição, não paronomásia. B usa adjetivos inesperados para a lua. C enumera ações. E repete as mesmas palavras em ordem invertida (quiasmo).</p>"},
}
completar(Q, R)
