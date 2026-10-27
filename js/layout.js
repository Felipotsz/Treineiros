/* Injeta cabeçalho, rodapé, "pular para o conteúdo" e a região de anúncios em todas as páginas,
   e registra o modo offline. No celular, o menu abre num painel pelo botão "Menu". */
(function () {
  var pagina = location.pathname.split("/").pop() || "index.html";
  // páginas de questão estática (q/) e páginas de vestibular contam como "Provas"/"Vestibulares" no menu
  var grupo = { "simulado.html": "provas.html", "resultado.html": "provas.html", "questao.html": "provas.html", "lista.html": "busca.html",
                "etec.html": "vestibulares.html", "fatec.html": "vestibulares.html", "enem.html": "vestibulares.html" }[pagina] || pagina;
  var principais = [["provas.html", "Provas"], ["estudo.html", "Meu estudo"], ["busca.html", "Buscar"], ["redacao.html", "Redação"],
                    ["vestibulares.html", "Vestibulares"], ["apoie.html", "Apoie"]];
  var secundarios = [["index.html", "Início"], ["etec.html", "ETEC"], ["fatec.html", "FATEC"], ["enem.html", "Enem"], ["fontes.html", "Fontes e créditos"]];
  function li(l) { return '<li><a href="' + l[0] + '"' + (l[0] === grupo ? ' aria-current="page"' : "") + ">" + l[1] + "</a></li>"; }
  var ICONE_MENU = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18" stroke="currentColor" stroke-width="2" stroke-linecap="round" fill="none"/></svg>';
  var ICONE_LUA = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>';

  var skip = document.createElement("a");
  // com <base> (páginas em q/), "#conteudo" sozinho apontaria para a raiz do site
  skip.className = "skip"; skip.href = document.querySelector("base") ? location.href.split("#")[0] + "#conteudo" : "#conteudo"; skip.textContent = "Pular para o conteúdo";

  var cab = document.createElement("header");
  cab.className = "cab";
  cab.innerHTML = '<div class="cab__in">' +
    (window.LOGO_SVG ? '<a class="marca marca--logo" href="index.html">' + LOGO_SVG + '<span class="sr">Treineiros, página inicial</span></a>'
                     : '<a class="marca" href="index.html">Treineiros</a>') +
    '<button type="button" class="btn-icone cab__menu" id="btn-menu" aria-expanded="false" aria-controls="menu-principal">' + ICONE_MENU + "Menu</button>" +
    '<nav class="cab__nav" id="menu-principal" aria-label="Principal"><ul>' + principais.map(li).join("") + "</ul>" +
    '<ul class="cab__secundarios">' + secundarios.map(li).join("") + "</ul></nav>" +
    '<div class="cab__acoes"><button type="button" class="btn-icone" id="btn-tema" aria-pressed="false" title="Modo noturno">' + ICONE_LUA + '<span class="sr">Modo noturno</span></button></div>' +
    "</div>";

  var rodape = document.createElement("footer");
  rodape.className = "rodape";
  rodape.innerHTML = '<div class="rodape__in">' +
    '<div class="rodape__sobre">' + (window.LOGO_SVG ? LOGO_SVG : "<strong>Treineiros</strong>") +
      "<p>Simulados gratuitos com as provas oficiais da ETEC e da FATEC. Sem cadastro: seu progresso fica no seu aparelho.</p></div>" +
    '<nav aria-label="Treinar"><h2>Treinar</h2><ul><li><a href="provas.html">Provas</a></li><li><a href="estudo.html">Meu estudo</a></li><li><a href="busca.html">Buscar questões</a></li><li><a href="redacao.html">Redação</a></li></ul></nav>' +
    '<nav aria-label="Vestibulares"><h2>Vestibulares</h2><ul><li><a href="etec.html">ETEC</a></li><li><a href="fatec.html">FATEC</a></li><li><a href="enem.html">Enem</a></li></ul></nav>' +
    '<nav aria-label="Projeto"><h2>Projeto</h2><ul><li><a href="apoie.html">Quem faz e como apoiar</a></li><li><a href="fontes.html">Fontes e créditos</a></li><li><a href="provas.html#bk">Levar o progresso para outro aparelho</a></li></ul></nav>' +
    '<p class="rodape__fim">As questões são das provas oficiais do Centro Paula Souza (ETEC e FATEC) e do Inep (Enem), reunidas para estudo. ' +
      "O Treineiros é um projeto independente e sem fins lucrativos, sem vínculo com essas instituições.</p></div>";

  var main = document.querySelector("main");

  // Região de anúncios para leitor de tela, sempre presente na página. Um aviso que aparece numa caixa
  // que estava escondida nem sempre é lido; escrevendo aqui (vazio → texto), ele é anunciado.
  var anuncio = document.createElement("div");
  anuncio.className = "sr"; anuncio.id = "anuncio"; anuncio.setAttribute("role", "status"); anuncio.setAttribute("aria-live", "polite");
  document.body.appendChild(anuncio);
  window.anunciar = function (txt) { anuncio.textContent = ""; setTimeout(function () { anuncio.textContent = txt; }, 80); };
  document.body.insertBefore(skip, document.body.firstChild);
  document.body.insertBefore(cab, main);
  document.body.appendChild(rodape);

  // Aviso quando o navegador não deixa salvar de forma permanente (modo privado, cookies bloqueados, espaço cheio).
  if (window.Armazem && Armazem.modo() !== "local" && main) {
    var av = document.createElement("p");
    av.className = "aviso-armazem";
    av.textContent = "Este navegador não está deixando o Treineiros guardar seu progresso (modo privado, bloqueio de dados do site ou espaço cheio). " +
      "Ele vale só enquanto esta aba estiver aberta.";
    main.insertBefore(av, main.firstChild);
  }

  // Menu do celular: abre e fecha; Esc fecha e devolve o foco ao botão
  var bMenu = document.getElementById("btn-menu"), menu = document.getElementById("menu-principal");
  var celular = window.matchMedia ? matchMedia("(max-width: 59.99rem)") : { matches: false };
  function ajustarMenu() { if (celular.matches) { menu.hidden = bMenu.getAttribute("aria-expanded") !== "true"; } else { menu.hidden = false; } }
  bMenu.addEventListener("click", function () {
    var abrir = bMenu.getAttribute("aria-expanded") !== "true";
    bMenu.setAttribute("aria-expanded", abrir); ajustarMenu();
    if (abrir) { var a = menu.querySelector("a"); if (a) a.focus(); }
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && bMenu.getAttribute("aria-expanded") === "true") { bMenu.setAttribute("aria-expanded", "false"); ajustarMenu(); bMenu.focus(); }
  });
  document.addEventListener("click", function (e) {                  // toque fora do menu fecha
    if (bMenu.getAttribute("aria-expanded") === "true" && !cab.contains(e.target)) { bMenu.setAttribute("aria-expanded", "false"); ajustarMenu(); }
  });
  if (celular.addEventListener) celular.addEventListener("change", ajustarMenu);
  ajustarMenu();

  var btn = document.getElementById("btn-tema");
  function sincronizar() { btn.setAttribute("aria-pressed", Tema.atual() === "dark"); }
  btn.addEventListener("click", function () { Tema.alternar(); sincronizar(); });
  sincronizar();

  // Modo offline (PWA). Só em https, para não atrapalhar o teste local.
  if ("serviceWorker" in navigator && location.protocol === "https:") navigator.serviceWorker.register("sw.js").catch(function () {});
})();
