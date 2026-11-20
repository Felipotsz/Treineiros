/* Injeta cabeçalho, faixa de apoio, rodapé, "pular para o conteúdo" e a região de anúncios em todas as páginas,
   e registra o modo offline. Em celular e tablet, a navegação é uma barra fixa embaixo, com 5 destinos:
   Início, Provas, Meu estudo, Redação e Mais (folha com o resto do site). O cabeçalho fica só com a marca e o modo noturno. */
(function () {
  /* Contagem de visitas (GoatCounter), só se Config.goatcounter estiver preenchido e fora do localhost.
     window.contarEvento("prova-concluida") registra ações que importam, sem dados pessoais. */
  var gc = window.Config && Config.goatcounter;
  window.contarEvento = function (nome) {
    try { if (window.goatcounter && goatcounter.count) goatcounter.count({ path: "evento/" + nome, title: nome, event: true }); } catch (e) {}
  };
  if (gc && !/^(localhost|127\.|0\.0\.0\.0)/.test(location.hostname)) {
    var sc = document.createElement("script");
    sc.async = true; sc.src = "https://gc.zgo.at/count.js";
    sc.setAttribute("data-goatcounter", "https://" + gc + ".goatcounter.com/count");
    document.head.appendChild(sc);
  }

  var pagina = location.pathname.split("/").pop() || "index.html";
  // páginas de questão estática (q/) e páginas de vestibular contam como "Provas"/"Vestibulares" no menu
  var grupo = { "simulado.html": "provas.html", "resultado.html": "provas.html", "questao.html": "provas.html", "lista.html": "busca.html",
                "etec.html": "vestibulares.html", "fatec.html": "vestibulares.html", "enem.html": "vestibulares.html" }[pagina] || pagina;
  var principais = [["provas.html", "Provas"], ["busca.html", "Treinar por assunto"], ["redacao.html", "Redação"], ["vestibulares.html", "Vestibulares"], ["sobre.html", "Sobre"]];
  // A marca: o nome e a fileira de bolhas do cartão-resposta, com a terceira preenchida
  var MARCA = '<img class="marca__img marca__img--dia" src="assets/logo-dia.png" width="495" height="168" alt="treineiros">' +
    '<img class="marca__img marca__img--noite" src="assets/logo-noite.png" width="495" height="168" alt="treineiros">';
  // no rodapé (sempre escuro) vai só a versão clara das letras
  var MARCA_RODAPE = '<img class="marca__img" src="assets/logo-noite.png" width="495" height="168" alt="treineiros">';
  function li(l) { return '<li><a href="' + l[0] + '"' + (l[0] === grupo ? ' aria-current="page"' : "") + ">" + l[1] + "</a></li>"; }
  var ICONE_LUA = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>';

  var skip = document.createElement("a");
  // com <base> (páginas em q/), "#conteudo" sozinho apontaria para a raiz do site
  skip.className = "skip"; skip.href = document.querySelector("base") ? location.href.split("#")[0] + "#conteudo" : "#conteudo"; skip.textContent = "Pular para o conteúdo";

  var cab = document.createElement("header");
  cab.className = "cab";
  cab.innerHTML = '<div class="cab__in">' +
    '<a class="marca" href="index.html">' + MARCA + '<span class="sr">, página inicial</span></a>' +
    '<nav class="cab__nav" id="menu-principal" aria-label="Principal"><ul>' + principais.map(li).join("") + "</ul></nav>" +
    '<div class="cab__acoes"><button type="button" class="btn-icone" id="btn-tema" aria-pressed="false" title="Modo noturno">' + ICONE_LUA + '<span class="sr">Modo noturno</span></button>' +
      '<a class="btn" href="estudo.html"' + (grupo === "estudo.html" ? ' aria-current="page"' : "") + '>Meu estudo</a>' +
      '<a class="btn btn--primary" href="provas.html">Começar</a></div>' +
    "</div>";

  var rodape = document.createElement("footer");
  rodape.className = "rodape";
  var email = (window.Config && Config.contatoEmail) || "";
  rodape.innerHTML = '<div class="rodape__marca"><a class="marca" href="index.html">' + MARCA_RODAPE + '<span class="sr">, página inicial</span></a>' +
      "<p>Simulados gratuitos com provas oficiais. Sem cadastro: seu progresso fica no seu aparelho.</p></div>" +
    '<div class="rodape__in">' +
    '<nav aria-label="Treinar"><h2>Treinar</h2><ul><li><a href="provas.html">Provas</a></li><li><a href="busca.html">Treinar por assunto</a></li><li><a href="redacao.html">Redação</a></li><li><a href="estudo.html">Meu estudo</a></li></ul></nav>' +
    '<nav aria-label="Vestibulares"><h2>Vestibulares</h2><ul><li><a href="enem.html">Enem</a></li><li><a href="etec.html">ETEC</a></li><li><a href="fatec.html">FATEC</a></li></ul></nav>' +
    '<nav aria-label="Projeto"><h2>Projeto</h2><ul><li><a href="sobre.html">Sobre</a></li><li><a href="apoie.html">Apoie</a></li><li><a href="fontes.html">Fontes e créditos</a></li><li><a href="provas.html#bk">Levar o progresso</a></li>' +
      (email ? '<li><a href="mailto:' + email + '">' + email + "</a></li>" : "") + "</ul></nav></div>" +
    '<div class="rodape__fim"><p>As questões são das provas oficiais do Centro Paula Souza (ETEC e FATEC) e do Inep (Enem), reunidas para estudo. ' +
      "Projeto independente e sem fins lucrativos, sem vínculo com essas instituições.</p></div>";

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

  // ---------- Faixa de apoio, logo antes do rodapé (a página inicial e a Apoie têm a sua, a Sobre termina com "Quer ajudar?"; o simulado não tem) ----------
  if (pagina !== "apoie.html" && pagina !== "sobre.html" && pagina !== "simulado.html" && pagina !== "index.html") {
    var cta = document.createElement("aside");
    cta.className = "apoio-cta"; cta.setAttribute("aria-labelledby", "apoio-cta-t");
    cta.innerHTML = '<div class="apoio-cta__in">' +
      '<figure class="cta-autor"><img class="apoio-cta__foto" src="assets/fotos/autor-retrato-190.webp" srcset="assets/fotos/autor-retrato-190.webp 1x, assets/fotos/autor-retrato-380.webp 2x" width="190" height="228" alt="" loading="lazy">' +
      '<figcaption>Felipe Gustavo Bieco</figcaption></figure>' +
      '<div class="apoio-cta__texto"><p class="apoio-cta__selo">Gratuito e sem anúncios</p>' +
      '<h2 id="apoio-cta-t">O Treineiros é feito <em>por uma pessoa</em></h2>' +
      "<p>Se ele está te ajudando a estudar, você pode apoiar com um Pix de qualquer valor. É opcional: tudo continua liberado para todo mundo.</p>" +
      '<p class="apoio-cta__botoes"><a class="btn btn--contorno-claro" href="sobre.html">Conhecer o projeto</a>' +
      '<a class="btn btn--contorno-claro" href="apoie.html#outras">Outras formas de ajudar</a></p></div>' +
      '<div class="pix-cartao"><p class="pix-cartao__rot">Pix</p><div class="pix-cartao__qr" id="cta-pix-qr">QR Code<br>do Pix</div>' +
      '<p class="pix-cartao__instr">Ou use a chave (e-mail):</p><p class="pix-cartao__chave" id="cta-pix-chave"></p>' +
      '<button type="button" class="btn btn--primary" id="cta-pix-copiar">Copiar chave Pix</button></div></div>';
    document.body.insertBefore(cta, rodape);
    // Pix: a chave e o QR vêm de Config.apoio; sem chave, o cartão diz "em breve"
    (function () {
      var ap = (window.Config && Config.apoio) || {}, chave = (ap.pixChave || "").trim();
      var cxQr = document.getElementById("cta-pix-qr"), cxChave = document.getElementById("cta-pix-chave"), bt = document.getElementById("cta-pix-copiar");
      if (!chave) { cxChave.textContent = "em breve"; bt.hidden = true; return; }
      cxChave.innerHTML = chave.replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }).replace("@", "@<wbr>");
      if (ap.pixQr) {
        var img = new Image();
        img.alt = "QR Code do Pix para apoiar o Treineiros" + (ap.pixNome ? ", em nome de " + ap.pixNome : "");
        img.onload = function () { cxQr.textContent = ""; cxQr.classList.add("tem-qr"); cxQr.appendChild(img); };
        img.src = ap.pixQr;
      }
      bt.addEventListener("click", function () {
        function ok() { bt.textContent = "Chave copiada"; if (window.anunciar) anunciar("Chave Pix copiada"); setTimeout(function () { bt.textContent = "Copiar chave Pix"; }, 2500); }
        function manual() { var r = document.createRange(); r.selectNodeContents(cxChave); var sel = getSelection(); sel.removeAllRanges(); sel.addRange(r); if (window.anunciar) anunciar("Chave selecionada. Use copiar do seu aparelho."); }
        if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(chave).then(ok, manual); else manual();
      });
    })();
  }

  // ---------- Barra de navegação inferior (celular) ----------
  var ICO = {
    inicio: '<path d="M4 11l8-7 8 7v9H4z" /><path d="M10 20v-5h4v5" />',
    provas: '<path d="M7 3h7l4 4v14H7z" /><path d="M14 3v4h4M10 12h5M10 16h5" />',
    redacao: '<path d="M4 20l1-4L16 5l3 3L8 19z" /><path d="M14 7l3 3M4 20h16" />',
    estudo: '<path d="M5 20V10M10 20V4M15 20v-8M20 20v-5" />',
    mais: '<circle cx="5" cy="12" r="1.6" /><circle cx="12" cy="12" r="1.6" /><circle cx="19" cy="12" r="1.6" />'
  };
  function icone(n) { return '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">' + ICO[n] + "</svg>"; }
  var abaAtual = { "index.html": "inicio", "provas.html": "provas", "simulado.html": "provas", "resultado.html": "provas", "questao.html": "provas",
                   "redacao.html": "redacao", "estudo.html": "estudo" }[pagina] || (document.querySelector("base") ? "provas" : "mais");
  var semAbas = pagina === "simulado.html";            // durante a prova, a barra da própria prova ocupa o rodapé da tela
  if (!semAbas) {
    var abas = document.createElement("nav");
    abas.className = "abas"; abas.setAttribute("aria-label", "Navegação principal");
    function aba(id, href, rotulo) {
      return '<li><a class="abas__item" href="' + href + '"' + (abaAtual === id ? ' aria-current="page"' : "") + ">" + icone(id) + "<span>" + rotulo + "</span></a></li>";
    }
    abas.innerHTML = "<ul>" + aba("inicio", "index.html", "Início") + aba("provas", "provas.html", "Provas") + aba("estudo", "estudo.html", "Meu estudo") + aba("redacao", "redacao.html", "Redação") +
      '<li><button type="button" class="abas__item" id="btn-mais" aria-haspopup="dialog" aria-controls="folha-mais"' + (abaAtual === "mais" ? ' data-atual="sim"' : "") + ">" +
      icone("mais") + "<span>Mais</span></button></li></ul>";
    document.body.appendChild(abas);
    document.documentElement.classList.add("tem-abas");

    var grupos = [
      ["Treinar", [["busca.html", "Treinar por assunto"], ["provas.html#bk", "Levar o progresso para outro aparelho"]]],
      ["Vestibulares", [["vestibulares.html", "Comparar os vestibulares"], ["etec.html", "Vestibulinho ETEC"], ["fatec.html", "Vestibular FATEC"], ["enem.html", "Enem"]]],
      ["Projeto", [["sobre.html", "Sobre"], ["funcionalidades.html", "Funcionalidades"], ["apoie.html", "Apoie"], ["fontes.html", "Fontes e créditos"]]]
    ];
    var folha = document.createElement("dialog");
    folha.className = "folha"; folha.id = "folha-mais"; folha.setAttribute("aria-labelledby", "folha-mais-t");
    folha.innerHTML = '<div class="folha__topo"><h2 id="folha-mais-t">Mais</h2>' +
      '<button type="button" class="btn-icone folha__fechar" id="btn-mais-fechar"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg><span class="sr">Fechar</span></button></div>' +
      grupos.map(function (g) {
        return '<section class="folha__grupo"><h3>' + g[0] + "</h3><ul>" + g[1].map(function (l) {
          return '<li><a href="' + l[0] + '"' + (l[0] === pagina ? ' aria-current="page"' : "") + ">" + l[1] + "</a></li>";
        }).join("") + "</ul></section>";
      }).join("") +
      '<button type="button" class="btn folha__tema" id="btn-tema-folha" aria-pressed="false">' + ICONE_LUA + "Modo noturno</button>";
    document.body.appendChild(folha);
    var bMais = document.getElementById("btn-mais");
    function abrirMais() { if (folha.showModal) folha.showModal(); else folha.setAttribute("open", ""); bMais.setAttribute("aria-expanded", "true"); }
    function fecharMais() { if (folha.close) folha.close(); else folha.removeAttribute("open"); }
    bMais.addEventListener("click", abrirMais);
    document.getElementById("btn-mais-fechar").addEventListener("click", fecharMais);
    folha.addEventListener("close", function () { bMais.setAttribute("aria-expanded", "false"); bMais.focus(); });
    folha.addEventListener("click", function (e) { if (e.target === folha) fecharMais(); });   // toque fora do painel fecha
    bMais.setAttribute("aria-expanded", "false");
  }

  var btn = document.getElementById("btn-tema");
  var btnF = document.getElementById("btn-tema-folha");
  function sincronizar() { var e = Tema.atual() === "dark"; btn.setAttribute("aria-pressed", e); if (btnF) btnF.setAttribute("aria-pressed", e); }
  btn.addEventListener("click", function () { Tema.alternar(); sincronizar(); });
  if (btnF) btnF.addEventListener("click", function () { Tema.alternar(); sincronizar(); });
  sincronizar();

  // Modo offline (PWA). Só em https, para não atrapalhar o teste local.
  if ("serviceWorker" in navigator && location.protocol === "https:") navigator.serviceWorker.register("sw.js").catch(function () {});
})();
