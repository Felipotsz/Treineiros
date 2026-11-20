# Enem 2016, 1º dia, caderno azul: Ciências Humanas (questões 1 a 45; no 1º dia de 2016 vinham Humanas e Natureza).
# Texto legível (sem DECOD). Alternativas-imagem na Q17 (projeções cartográficas). Shakespeare (Q6) em texto, domínio público.
# Sem anuladas nesta área.
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
from enem_aj import carregar_enem, enunciado_enem, paragrafos_enem

ID = "enem-2016-humanas"
META = {"id": ID, "banca": "Enem", "ano": 2016, "titulo": "Enem 2016: Ciências Humanas", "fonte": "Inep", "dataExame": "2016-11-05",
        "duracaoMinutos": 135, "area": "Ciências Humanas", "caderno": "azul", "dia": 1}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
D = carregar_enem("enem-2016-dia1-azul")
Q = {}
P = lambda n: paragrafos_enem(D[n])
T = lambda n, i: P(n)[i][1]
p = lambda *xs: "".join(f"<p>{x}</p>" for x in xs)
ap = lambda *xs: "".join(f'<p class="apoio">{x}</p>' for x in xs)
fonte = lambda x: f'<p class="fonte">{x}</p>'
ALT = lambda ini: {k: f"[[fig:{i}]]" for i, k in enumerate("ABCDE", ini)}
tit = lambda x: f'<p class="apoio"><strong>{x}</strong></p>'
LIMPA = lambda s: re.sub(r"fi ([a-zà-ú])", r"fi\1", re.sub(r"fl ([a-zà-ú])", r"fl\1", re.sub(r"(\w)- -(\w)", r"\1-\2", s)))


def figs(*pares):
    return [{"arquivo": a, "alt": t} for a, t in pares]


def X(n, materia, assunto, expl, imagens=(), tags=(), enun=None, trocas=(), alts=None):
    e = LIMPA(enun or enunciado_enem(D[n]))
    for a, b in trocas:
        assert a in e, a; e = e.replace(a, b)
    al = {k: LIMPA(v) for k, v in (alts or D[n]["alternativas"]).items()}
    Q[n] = {"materia": materia, "assunto": assunto, "area": "Ciências Humanas", "tags": list(tags), "numeroOriginal": n,
                 "enunciado": e, "alternativas": al, "imagens": list(imagens), "explicacao": expl}


def tabela(cab, linhas):
    return ('<table class="tabela"><thead><tr>' + "".join(f"<th>{c}</th>" for c in cab) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in l) + "</tr>" for l in linhas) + "</tbody></table>")



def tabela(cab, linhas):
    return ('<table class="tabela"><thead><tr>' + "".join(f"<th>{c}</th>" for c in cab) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in l) + "</tr>" for l in linhas) + "</tbody></table>")


X(1, "Filosofia", "Ética", "<p>Schopenhauer compara a satisfação dos desejos à esmola, que mata a fome hoje e a prolonga amanhã, e a resignação à fortuna herdada, que livra de preocupações para sempre. A felicidade depende de controlar os próprios desejos: é a <strong>administração da independência interior</strong>, ideia que vem dos estoicos. Alternativa <strong>B</strong>.</p><p>A busca de prazeres efêmeros (E) é justamente o que o texto rejeita.</p>",
  tags=["Schopenhauer", "estoicismo"], trocas=[("Aforismo para a sabedoria da vida", "<em>Aforismo para a sabedoria da vida</em>")])
X(2, "História", "Nova República", "<p>A Nova República começou com Tancredo, eleito pelo Colégio Eleitoral, e com Sarney, que tinha sido presidente do partido de apoio à ditadura. Muitos políticos do regime militar continuaram no poder: a continuidade foi a <strong>presença de políticos com trajetórias no regime autoritário</strong>. Alternativa <strong>C</strong>.</p><p>O bipartidarismo e os atos institucionais (A e D) já tinham acabado.</p>",
  tags=["redemocratização", "Sarney"], trocas=[("Jornal do Brasil", "<em>Jornal do Brasil</em>")])
X(3, "Geografia", "Urbanização", "<p>A proposta é de casas que se deslocam sobre trilhos, podendo ficar perto do trabalho durante a semana. Com isso, os moradores deixariam de fazer todo dia o trajeto casa-trabalho-casa, o <strong>movimento pendular</strong>. Alternativa <strong>B</strong>.</p><p>Êxodo rural e migração de retorno (A e C) são mudanças definitivas de residência, não idas e vindas diárias.</p>",
  figs(("q03", "Foto de pequenas casas em forma de caixa colocadas sobre trilhos de trem, num vale entre montanhas, passando sob uma ponte.")), ["migração pendular", "mobilidade urbana"])
X(4, "Geografia", "Rede urbana", "<p>O texto descreve várias cidades de outros estados que estão sob a influência do Rio de Janeiro, que oferece serviços e comando econômico a elas. Uma metrópole que atrai e comanda uma área ao redor forma uma <strong>região polarizada</strong>. Alternativa <strong>C</strong>.</p><p>Conurbação (D) seria a junção física das manchas urbanas, o que não ocorre entre o Rio e Vitória ou Juiz de Fora.</p>",
  tags=["hierarquia urbana", "polarização"])
X(5, "História", "Brasil Colônia", "<p>Os europeus chamaram povos muito diferentes pelo mesmo nome, “índios” ou “negros da terra”, a partir de sua posição econômica e jurídica, sem considerar as culturas desses povos. Isso revela uma <strong>compreensão etnocêntrica acerca das populações dos territórios conquistados</strong>. Alternativa <strong>C</strong>.</p><p>A designação comum não vem do reconhecimento de uma ancestralidade comum (B), mas do desinteresse pela diversidade.</p>",
  tags=["etnocentrismo", "povos indígenas"], trocas=[("ao status econômico", "ao <em>status</em> econômico"), ("Viagem incompleta", "<em>Viagem incompleta</em>"), ("Dicionário de conceitos históricos", "<em>Dicionário de conceitos históricos</em>")])
X(6, "Filosofia", "Existencialismo", "<p>Hamlet se pergunta se deve viver ou morrer e hesita diante do desconhecido que viria depois da morte: a reflexão sobre a própria existência gera angústia. O existencialismo também parte dessa tensão entre <strong>consciência de si e angústia humana</strong>. Alternativa <strong>A</strong>.</p><p>O solilóquio não fala de destino nem de loucura (B e D).</p>",
  tags=["Shakespeare", "angústia"],
  enun='<p class="apoio">Ser ou não ser — eis a questão.<br>Morrer — dormir — Dormir! Talvez sonhar. Aí está o obstáculo!<br>Os sonhos que hão de vir no sono da morte<br>Quando tivermos escapado ao tumulto vital<br>Nos obrigam a hesitar: e é essa a reflexão<br>Que dá à desventura uma vida tão longa.</p>' + fonte("SHAKESPEARE, W. <em>Hamlet</em>. Porto Alegre: L&amp;PM, 2007.") + p(T(6, 5)))
X(7, "Sociologia", "Gênero", "<p>O anúncio de 1968 diz que as mulheres do futuro farão da Lua “um lugar mais limpo”: até no espaço, o papel da mulher seria limpar. Em 2016, uma equipe da Nasa metade feminina ainda recebe comentários machistas. Os dois textos mostram a <strong>manutenção de estereótipos de gênero</strong>. Alternativa <strong>D</strong>.</p><p>Os comentários de 2016 mostram que a equiparação de papéis (E) ainda não se completou.</p>",
  figs(("q07", "Anúncio antigo em preto e branco: uma mulher com capacete de astronauta segura um frasco de produto de limpeza; embaixo, a frase em inglês sobre as mulheres do futuro e a Lua.")), ["estereótipos de gênero", "publicidade"],
  trocas=[("TEXTO II Metade da nova equipe da Nasa é composta por mulheres", "TEXTO II</strong></p><p class=\"apoio\"><strong>Metade da nova equipe da Nasa é composta por mulheres")])
X(8, "História", "Escravidão", "<p>O texto destaca as mulheres comerciantes da África Ocidental, autônomas e móveis. Essa tradição reapareceu nas cidades do Brasil escravista, com as escravizadas e libertas que vendiam alimentos e outros produtos nas ruas, as “negras de ganho”. É a <strong>presença de mulheres negras no comércio de rua de diversos produtos e alimentos</strong>. Alternativa <strong>C</strong>.</p><p>Os costumes africanos foram mantidos e adaptados, não dissolvidos (D).</p>",
  tags=["escravos de ganho", "mulheres africanas"], trocas=[("Identidades, memórias e histórias em terras africanas", "<em>Identidades, memórias e histórias em terras africanas</em>")])
X(9, "Sociologia", "Capitalismo", "<p>Polanyi mostra que, com a industrialização, trabalho, terra e dinheiro passaram a ser organizados para a venda no mercado. O trabalho humano virou algo que se compra e se vende: a consequência é a <strong>consolidação da força de trabalho como mercadoria</strong>. Alternativa <strong>C</strong>.</p><p>As terras comunais foram cercadas e vendidas, não expandidas (A).</p>",
  tags=["Polanyi", "mercantilização"], trocas=[("A grande transformação", "<em>A grande transformação</em>")])
X(10, "História", "Brasil Colônia", "<p>A Inconfidência Mineira (1789) queria a independência da colônia, mas não tocava na escravidão. A Conjuração Baiana (1798), com participação de alfaiates, soldados e escravizados, foi além: “avançou sobre a decorrência” da condição colonial, propondo a igualdade e o fim da escravidão. A diferença estava em <strong>abolir a escravidão africana</strong>. Alternativa <strong>B</strong>.</p><p>Anular o domínio metropolitano (C) era objetivo das duas.</p>",
  tags=["Conjuração Baiana", "Inconfidência Mineira"], trocas=[("Viagem incompleta", "<em>Viagem incompleta</em>")])
X(11, "História", "Patrimônio cultural", "<p>A foto mostra as mãos de um artesão fabricando uma viola, um saber transmitido entre gerações e registrado pelo Iphan como patrimônio. O texto fala de novas formas de patrimônio, além dos bens materiais. O bem protegido é um dos <strong>conhecimentos tradicionais</strong>. Alternativa <strong>E</strong>.</p><p>O que se protege é o modo de fazer, não o objeto em si (B).</p>",
  figs(("q11", "Foto em preto e branco das mãos de um artesão trabalhando no corpo de madeira de uma viola em construção.")), ["patrimônio imaterial", "Iphan"],
  trocas=[("Cultura política e leituras do passado", "<em>Cultura política e leituras do passado</em>")])
X(12, "Geografia", "Geopolítica", "<p>A China instalou uma plataforma em águas que Vietnã e Filipinas também reivindicam, para mostrar que pode impor seu controle. O conflito é sobre quem tem soberania sobre aquelas águas: a <strong>jurisdição da soberania territorial</strong>. Alternativa <strong>D</strong>.</p><p>O texto não trata de zonas econômicas especiais (A), que são áreas de incentivo dentro da China.</p>",
  tags=["Mar da China Meridional", "petróleo"], trocas=[("Le Monde Diplomatique Brasil", "<em>Le Monde Diplomatique Brasil</em>")])
X(13, "História", "Ditaduras na América Latina", "<p>A Operação Condor foi a colaboração entre as ditaduras do Cone Sul, apoiadas na Doutrina de Segurança Nacional e no anticomunismo, para trocar informações e perseguir opositores além das fronteiras. O objetivo era coordenar a <strong>repressão de ativistas oposicionistas</strong>. Alternativa <strong>D</strong>.</p>",
  tags=["Operação Condor", "Doutrina de Segurança Nacional"], trocas=[("Ditadura de Segurança Nacional no Rio Grande do Sul (1964-1985)", "<em>Ditadura de Segurança Nacional no Rio Grande do Sul (1964-1985)</em>")])
X(14, "História", "Era Vargas", "<p>A Justiça do Trabalho, instalada no Estado Novo, fazia parte da estrutura em que o Estado regulava as relações entre patrões e empregados, com sindicatos controlados e representantes classistas. O objetivo era <strong>ordenar os conflitos laborais</strong> dentro do Estado. Alternativa <strong>B</strong>.</p><p>O Estado Novo combatia greves e sindicatos livres (A e C).</p>",
  tags=["Justiça do Trabalho", "corporativismo"], trocas=[("Repensando o Estado Novo", "<em>Repensando o Estado Novo</em>")])
X(15, "Sociologia", "Indústria cultural", "<p>Adorno e Horkheimer dizem que todos são “livres” para se divertir e escolher, mas a escolha reflete a coerção econômica e “é sempre a mesma coisa”. A liberdade de escolha oferecida pela indústria cultural é uma <strong>ilusão da contemporaneidade</strong>. Alternativa <strong>E</strong>.</p><p>O texto não vê essa liberdade como conquista (D): ela é aparente.</p>",
  tags=["Escola de Frankfurt", "indústria cultural"], trocas=[("Dialética do esclarecimento", "<em>Dialética do esclarecimento</em>")])
X(16, "Geografia", "Blocos econômicos", "<p>A Parceria Transpacífica reúne países muito diferentes dos dois lados do Pacífico: economias ricas e inovadoras (EUA, Japão, Canadá, Austrália) e países com mão de obra barata ou recursos naturais (Vietnã, Malásia, México, Peru, Chile). Juntos, eles se completam nas cadeias produtivas: <strong>vantagens locacionais complementares</strong>. Alternativa <strong>E</strong>.</p><p>Os países não têm padrão social, moeda ou cultura em comum (A, B e D).</p>",
  figs(("q16", "Mapa-múndi centrado no Pacífico com os países da Parceria Transpacífica destacados: Canadá, Estados Unidos, México, Peru, Chile, Japão, Vietnã, Malásia, Cingapura, Brunei, Austrália e Nova Zelândia.")),
  ["Parceria Transpacífica", "cadeias produtivas"], enun=tit("Parceria Transpacífica") + "[[fig:1]]" + fonte(T(16, 3)) + p(T(16, 2)))
X(17, "Geografia", "Cartografia", "<p>O logotipo da ONU mostra o mundo visto de cima do Polo Norte, com os continentes em volta dele e paralelos em círculos concêntricos. É uma projeção azimutal (plana), em que o plano de projeção toca o globo num ponto, o polo. O modelo correto mostra um plano tangente ao polo. Alternativa <strong>A</strong>.</p><p>O cone (B) e o cilindro (C, E) dão as projeções cônica e cilíndrica.</p>",
  figs(("q17", "Logotipo da ONU: o mapa-múndi visto a partir do Polo Norte, com círculos concêntricos e linhas que partem do centro, cercado por dois ramos de oliveira."),
       ("q17a", "Alternativa A: um globo com um plano circular encostado no Polo Norte."),
       ("q17b", "Alternativa B: um globo envolvido por um cone, com o vértice acima do polo."),
       ("q17c", "Alternativa C: um globo dentro de um cilindro vertical."),
       ("q17d", "Alternativa D: um globo com um plano inclinado encostado num ponto qualquer da superfície."),
       ("q17e", "Alternativa E: um globo dentro de um cilindro deitado, na horizontal.")),
  ["projeção azimutal", "projeções cartográficas"], enun="[[fig:1]]" + fonte(T(17, 1)) + p(T(17, 2)), alts=ALT(2))
X(18, "Geografia", "Questões ambientais", "<p>Pelo mercado de créditos de carbono, países e empresas que poluem mais podem comprar créditos de quem polui menos, em vez de reduzir as próprias emissões. Os críticos dizem que os ricos continuam poluindo e transferem o esforço para os pobres: a estratégia promove a <strong>desigualdade na distribuição do impacto ecológico</strong>. Alternativa <strong>D</strong>.</p>",
  tags=["Protocolo de Quioto", "créditos de carbono"], trocas=[("Amazônia: geopolítica", "<em>Amazônia</em>: geopolítica")])
X(19, "Geografia", "Globalização", "<p>As remessas de imigrantes para seus países de origem ficaram mais fáceis com o avanço das telecomunicações e da informática, que permitem transferir dinheiro de forma rápida e barata entre países. Alternativa <strong>B</strong>.</p><p>Os países centrais continuaram restringindo a imigração e o trabalho estrangeiro; não houve quebra de barreiras para pessoas (C).</p>",
  tags=["remessas", "redes de comunicação"], trocas=[("A nova des-ordem mundial", "<em>A nova des-ordem mundial</em>")])
X(20, "Filosofia", "Racionalismo", "<p>Descartes diz que decorar demonstrações e raciocínios de outros não torna ninguém matemático ou filósofo: é preciso ser capaz de julgar por si. O conhecimento verdadeiro vem da <strong>autonomia do sujeito pensante</strong>. Alternativa <strong>D</strong>.</p><p>Retomar Platão e Aristóteles (B) é justamente o que ele critica como “histórias”.</p>",
  tags=["Descartes", "método"], trocas=[("Regras para a orientação do espírito", "<em>Regras para a orientação do espírito</em>")])
X(21, "História", "Roma Antiga", "<p>Políbio quer explicar como os romanos submeteram “quase todo o mundo habitado” em menos de 53 anos, nas guerras contra Cartago e os reinos helenísticos. A experiência é a <strong>concretização do desígnio imperialista</strong> de Roma. Alternativa <strong>C</strong>.</p><p>O cristianismo (D) surgiu séculos depois, e a libertação dos etruscos (E) é muito anterior.</p>",
  tags=["Políbio", "expansão romana"], trocas=[("História. Brasília", "<em>História</em>. Brasília")])
X(22, "História", "Oriente Médio", "<p>Marjane Satrapi lembra que, depois da Revolução Islâmica de 1979, o véu passou a ser obrigatório nas escolas, e as meninas aparecem de véu e separadas por sexo. A mudança de regime mudou o cotidiano: <strong>transformação política e modificação de costumes</strong>. Alternativa <strong>E</strong>.</p>",
  figs(("q22", "Quadrinhos de Persépolis: a narradora, de véu, diz que tinha 10 anos em 1980; em outro quadro, sua classe de meninas, todas de véu; abaixo, cenas da Revolução Islâmica de 1979 e do véu tornado obrigatório nas escolas em 1980.")),
  ["Revolução Iraniana", "Persépolis"], trocas=[("Persépolis. São Paulo", "<em>Persépolis</em>. São Paulo")])
X(23, "Filosofia", "Pré-socráticos", "<p>Heráclito diz que tudo muda (“não se pode banhar duas vezes no mesmo rio”); Parmênides, que o ser é imutável, sem começo nem fim. A oposição entre devir e permanência trata da natureza do ser: são <strong>discussões de base ontológica</strong>. Alternativa <strong>C</strong>.</p><p>Os pré-socráticos rompem com a explicação mitológica (B) e são anteriores aos sofistas (D).</p>",
  tags=["Heráclito", "Parmênides"], trocas=[("Fragmentos (Sobre a natureza)", "<em>Fragmentos (Sobre a natureza)</em>"), ("Da natureza. São Paulo", "<em>Da natureza</em>. São Paulo")])
X(24, "Sociologia", "Democracia", "<p>A democracia deliberativa quer chegar, pelo diálogo racional, a um acordo satisfatório para todos: a <strong>obtenção do consenso</strong>. A ativista desconfia desse diálogo, porque as desigualdades favorecem os poderosos, e defende a oposição crítica e a <strong>mobilização das minorias</strong>. Alternativa <strong>C</strong>.</p>",
  tags=["democracia deliberativa", "ativismo"], trocas=[("Revista Brasileira de Ciência Política", "<em>Revista Brasileira de Ciência Política</em>")])
X(25, "Filosofia", "Ética", "<p>Hans Jonas diz que a técnica moderna ameaça a própria natureza humana e o futuro, exigindo uma nova ética da responsabilidade: agir de modo que a vida humana continue possível na Terra. O objetivo é garantir a <strong>sobrevivência de gerações futuras</strong>. Alternativa <strong>B</strong>.</p>",
  tags=["Hans Jonas", "princípio responsabilidade"], trocas=[("O princípio da responsabilidade", "<em>O princípio da responsabilidade</em>")])
X(26, "História", "Brasil Colônia", "<p>São Benedito, santo negro, era usado pela Igreja para atrair escravizados à fé católica, oferecendo-lhes um modelo de obediência. A imagem e a prática de contar a vida dos santos serviam para <strong>cristianizar a população afro-brasileira</strong>. Alternativa <strong>B</strong>.</p><p>As irmandades negras ressignificaram esses santos depois; a intenção da Igreja não era reduzir as confrarias (A).</p>",
  figs(("q26", "Gravura antiga emoldurada de São Benedito: um santo negro, com auréola, vestido com hábito e capa ricamente decorados, segurando o Menino Jesus.")), ["catequese", "santos negros"],
  trocas=[("Imagem de São Benedito.", "<em>Imagem de São Benedito</em>."), ("Revista de História da Biblioteca Nacional", "<em>Revista de História da Biblioteca Nacional</em>")])
X(27, "História", "Era Vargas", "<p>No Estado Novo, setores do governo simpatizavam com o nazifascismo, e circulares secretas proibiram vistos a “pessoas de origem semita”. O antissemitismo da política imigratória reflete a <strong>simpatia de membros da burocracia pelo projeto totalitário alemão</strong>. Alternativa <strong>E</strong>.</p>",
  tags=["antissemitismo", "Estado Novo"], trocas=[("Brasil: 500 anos de povoamento", "<em>Brasil: 500 anos de povoamento</em>")])
X(28, "Filosofia", "Filosofia helenística", "<p>Pirro dizia que nada é justo ou injusto em si e que não se alcança a verdade, por isso suspendia o juízo e vivia indiferente a tudo. O ceticismo se caracteriza por <strong>defender a indiferença e a impossibilidade de obter alguma certeza</strong>. Alternativa <strong>C</strong>.</p><p>O prazer como fim da vida (B) é o epicurismo; desprezar convenções (A), o cinismo.</p>",
  tags=["ceticismo", "Pirro"], trocas=[("Vidas e sentenças dos filósofos ilustres", "<em>Vidas e sentenças dos filósofos ilustres</em>")])
X(29, "Geografia", "Urbanização", "<p>A função social da cidade exige que ela atenda a todos os moradores, inclusive os que estão fora do mercado formal. Uma política nesse sentido é a <strong>qualificação de serviços públicos em bairros periféricos</strong>, onde vivem os excluídos. Alternativa <strong>A</strong>.</p><p>Desregulamentar o mercado imobiliário nas favelas (E) favoreceria a especulação, não os moradores.</p>",
  tags=["função social da cidade", "Estatuto da Cidade"], trocas=[("Estudos Avançados", "<em>Estudos Avançados</em>")])
X(30, "Geografia", "Biomas", "<p>O Cerrado é considerado um <em>hotspot</em> porque perdeu grande parte da vegetação original e está muito ameaçado. A principal causa é a <strong>expansão da fronteira agrícola</strong>, com a soja e a pecuária ocupando o Centro-Oeste. Alternativa <strong>E</strong>.</p>",
  tags=["Cerrado", "hotspot"], trocas=[("25 hotspots", "25 <em>hotspots</em>"), ("conceito de hotspot", "conceito de <em>hotspot</em>"), ("Tantos cerrados", "<em>Tantos cerrados</em>")])
X(31, "Geografia", "Migrações", "<p>O governo húngaro ergueu um muro na fronteira e espalhou cartazes acusando imigrantes de “roubar” empregos. O ACNUR critica essa xenofobia promovida pelo próprio governo, que abre caminho para o <strong>fortalecimento das práticas de discriminação</strong>. Alternativa <strong>E</strong>.</p>",
  tags=["xenofobia", "refugiados"])
X(32, "Sociologia", "Durkheim", "<p>Durkheim critica as sínteses filosóficas e as intuições rápidas e quer estudar fatos bem delimitados, com provas. Ele propõe a <strong>adesão aos padrões de investigação típicos das ciências naturais</strong>, tratando os fatos sociais como coisas. Alternativa <strong>D</strong>.</p><p>Ele quer separar a sociologia da filosofia (A) e das hipóteses subjetivas (C).</p>",
  tags=["positivismo", "método sociológico"], trocas=[("O suicídio:", "<em>O suicídio</em>:")])
X(33, "História", "África", "<p>A foto mostra soldados conferindo os documentos de um homem negro de bicicleta. A “lei do passe” obrigava os negros a portar um documento para circular fora das áreas destinadas a eles: regulamentava o <strong>controle sobre a movimentação, desautorizando os negros a transitar em determinadas áreas das cidades</strong>. Alternativa <strong>D</strong>.</p>",
  figs(("q33", "Foto em preto e branco: dois soldados de capacete verificam os documentos de um homem negro que está ao lado de uma bicicleta, numa estrada.")), ["Apartheid", "segregação"],
  trocas=[("O regime do Apartheid", "O regime do <em>Apartheid</em>")])
X(34, "História", "Brasil Império", "<p>O texto diz que os primeiros críticos ambientais elogiavam a natureza pela riqueza e pelo potencial econômico e viam sua destruição como sinal de atraso. Para eles, o meio natural era <strong>ferramenta essencial para o avanço da nação</strong>. Alternativa <strong>A</strong>.</p><p>Eles não exaltavam a beleza nem viam a natureza como dádiva religiosa (B).</p>",
  tags=["crítica ambiental", "pensamento político"], trocas=[("Um sopro de destruição", "<em>Um sopro de destruição</em>")])
X(35, "História", "Primeira República", "<p>No coronelismo, o coronel garantia votos ao governo, e em troca controlava os cargos públicos locais. É uma troca de favores entre poder público e chefes locais: a <strong>disseminação de práticas clientelistas</strong>. Alternativa <strong>D</strong>.</p><p>O texto diz que o coronelismo dependia do fortalecimento do Estado, não da força das milícias locais (A).</p>",
  tags=["coronelismo", "clientelismo"], trocas=[("Pontos e bordados", "<em>Pontos e bordados</em>")])
X(36, "Geografia", "Recursos hídricos", "<p>O mapa mostra as maiores capacidades de dessalinização no Oriente Médio (Arábia Saudita, Emirados Árabes, Kuwait) e no norte da África, regiões desérticas com pouca água doce. A concentração se explica pela <strong>escassez de água potável</strong>. Alternativa <strong>C</strong>.</p><p>EUA, Espanha e Japão também dessalinizam, mas a concentração está nas áreas áridas.</p>",
  figs(("q36", "Mapa-múndi “Dessalinização das águas”, com a capacidade instalada por país em metros cúbicos por dia: Estados Unidos 5 653 941; Espanha 2 588 658; Japão 1 054 274; Emirados Árabes Unidos 6 228 017; Arábia Saudita 6 879 869; Kuwait 2 111 558. Os quadrados maiores se concentram no Oriente Médio e no norte da África.")),
  ["dessalinização", "escassez hídrica"], enun=tit("Dessalinização das águas") + p(T(36, 1)) + "[[fig:1]]" + fonte("EUA. <strong>Relatório da Academia Nacional de Ciências</strong>, 2008 (adaptado).") + p(T(36, 5)))
X(37, "Filosofia", "Nietzsche", "<p>Zaratustra descreve um mundo em que os homens se cansaram de suas obras e acreditam que “tudo é oco, tudo é igual, tudo passou”: os valores perderam o sentido. A alegoria mostra o niilismo como sintoma que <strong>destaca a decadência da cultura</strong>. Alternativa <strong>D</strong>.</p>",
  tags=["niilismo", "Nietzsche"], trocas=[("Assim falou Zaratustra", "<em>Assim falou Zaratustra</em>")])
X(38, "História", "República Populista", "<p>O anúncio do Simca Chambord mostra um carro moderno diante da arquitetura de Brasília: indústria automobilística e nova capital, símbolos do desenvolvimentismo de JK. Mas omite que a industrialização se concentrou no Sudeste, aumentando a distância em relação às outras regiões: a <strong>intensificação da desigualdade regional</strong>. Alternativa <strong>D</strong>.</p><p>A indústria se concentrou, não se desconcentrou (E), e entrou muito capital estrangeiro (B).</p>",
  figs(("q38", "Anúncio em preto e branco do automóvel Simca Chambord estacionado diante de um prédio moderno de Brasília, com a frase “Novo toque de elegância na moderna paisagem brasileira”.")),
  ["desenvolvimentismo", "JK"], enun="[[fig:1]]" + fonte("<em>O Cruzeiro</em>, década de 1960. Disponível em: www.memoriaviva.com.br. Acesso em: 28 fev. 2012 (adaptado).") + p("No anúncio, há referências a algumas das transformações ocorridas no Brasil nos anos 1950 e 1960.", T(38, 2)))
X(39, "Geografia", "Questões ambientais", "<p>A pesca industrial esgotou o bacalhau da Terra Nova e agora avança sobre outros mares, até a costa africana e a Antártida, em busca dos estoques restantes. O problema é a <strong>insustentabilidade do modelo de produção e consumo</strong>. Alternativa <strong>A</strong>.</p><p>O texto atribui o problema à sobrepesca, não a uma mudança natural dos oceanos (D).</p>",
  tags=["sobrepesca", "sustentabilidade"])
X(40, "Geografia", "Mundo do trabalho", "<p>O texto mostra que a tecnologia aumenta a produtividade (o vendedor ambulante recebe as bebidas no <em>just in time</em>), mas sem gerar emprego formal nem melhorar a renda. O que explica isso é o <strong>impacto da tecnologia e as modificações na estrutura produtiva</strong>. Alternativa <strong>C</strong>.</p><p>O exemplo é o trabalho informal, o oposto da regularização (B).</p>",
  tags=["informalidade", "reestruturação produtiva"], trocas=[("graças ao just in time", "graças ao <em>just in time</em>"), ("Crítica à razão dualista e o ornitorrinco", "<em>Crítica à razão dualista e o ornitorrinco</em>")],
  alts={**D[40]["alternativas"], "B": "inovação <em>toyotista</em> e a regularização do trabalho formal."})
X(41, "Sociologia", "Modernidade", "<p>Para Berman, a modernidade promete aventura e crescimento, mas ameaça destruir tudo; une a espécie humana, mas é “uma unidade paradoxal, uma unidade de desunidade”. É uma <strong>dinâmica social contraditória</strong>. Alternativa <strong>A</strong>.</p>",
  tags=["Berman", "modernidade"], trocas=[("Tudo que é sólido desmancha no ar", "<em>Tudo que é sólido desmancha no ar</em>")])
X(42, "Sociologia", "Meios de comunicação", "<p>Carr diz que a internet lhe dá acesso a uma quantidade enorme de informação, mas que agora ele não consegue mais ler com concentração: a atenção se dispersa. O paradoxo é <strong>associar uma experiência superficial à abundância de informações</strong>. Alternativa <strong>A</strong>.</p>",
  tags=["internet", "atenção"], trocas=[("tempo on-line", "tempo <em>on-line</em>"), ("a net parece", "a <em>net</em> parece"), ("Is Google making us stupid?", "<em>Is Google making us stupid?</em>")])
X(43, "História", "Primeira República", "<p>A página mostra parisienses bebendo café do Brasil num quiosque em Paris. No início do século XX, o Brasil era o grande exportador mundial de café: seu papel era de <strong>fornecedor de produtos agrícolas</strong>. Alternativa <strong>D</strong>.</p><p>O Brasil importava, e não formava, os padrões de consumo europeus (C e E).</p>",
  figs(("q43", "Página de revista de 1909 com o título “O café do Brazil em Paris”: ilustração de pessoas agasalhadas tomando café diante de uma barraca de rua em Paris, com um letreiro anunciando café do Brasil.")),
  ["economia cafeeira", "agroexportação"], trocas=[("para A Illustração Brazileira", "para <em>A Illustração Brazileira</em>"), ("do Je Sais Tout.", "do <em>Je Sais Tout</em>."), ("A Illustração Brazileira, n.", "<em>A Illustração Brazileira</em>, n.")])
X(44, "Geografia", "Espaço rural", "<p>Renato Teixeira diz que a música caipira mudou porque mudou a vida no campo: hoje o interior é conectado, globalizado e rico, com atividades além da agricultura tradicional (agroindústria, turismo, serviços). O aspecto é a <strong>expansão de atividades das novas ruralidades</strong>. Alternativa <strong>B</strong>.</p>",
  tags=["novas ruralidades", "música caipira"], trocas=[("Folha de São Paulo", "<em>Folha de São Paulo</em>")])
X(45, "Geografia", "Demografia", "<p>O gráfico mostra a queda da taxa de fecundidade no Brasil (de 5,8 para 1,9 filho por mulher entre 1970 e 2010) e em outros países. Com menos nascimentos, entram menos jovens no mercado de trabalho nas décadas seguintes: diminui a <strong>oferta de mão de obra nacional</strong>. Alternativa <strong>A</strong>.</p><p>A despesa previdenciária (D) aumenta com o envelhecimento, não diminui.</p>",
  figs(("q45", "Gráfico “Taxa de fecundidade total” de 1970 a 2010 para Brasil, China, Coreia do Sul, Portugal, EUA e Japão. O Brasil cai de 5,8 em 1970 para 4,4 em 1980, 2,9 em 1990, 2,4 em 2000 e 1,9 em 2010; os outros países terminam entre cerca de 1,2 e 2,0.")),
  ["transição demográfica", "fecundidade"], enun=p(T(45, 0)) + "[[fig:1]]" + fonte("Fontes: IBGE e OCDE. Disponível em: http://epoca.globo.com. Acesso em: 20 out. 2015 (adaptado).") + p(T(45, 6)),
  alts={**D[45]["alternativas"], "E": "imigração de trabalhadores qualificados."})

completar(Q, R)
