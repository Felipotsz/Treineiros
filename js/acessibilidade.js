/* Treineiros: menu de acessibilidade.
   Adaptado do pacote "Acessibilidade Universal" (React) para o site estático, sem dependências.
   - O botão fica no cabeçalho (ao lado do modo noturno) e na folha "Mais"; não há botão flutuante, porque
     no celular a barra de navegação e a barra da prova ocupam os cantos de baixo.
   - As escolhas ficam no aparelho (localStorage "treineiros:acessibilidade") e viram atributos data-a11y-* no <html>.
     O js/theme.js aplica essas mesmas escolhas no <head>, antes de desenhar, para a página não piscar.
   - Ficaram de fora do pacote original: a prancha de comunicação (o site não tem campo de mensagem),
     as legendas (não há vídeos), os alertas visuais (o site não usa avisos que somem sozinhos) e a troca de idioma.
   - A leitura em voz alta lê a seleção ou, sem seleção, a questão que está na tela (com o texto das figuras). */
(function () {
  "use strict";
  var CHAVE = "treineiros:acessibilidade";
  var TAMANHOS = ["small", "normal", "large", "xlarge", "xxlarge"];
  var ESCALA = { small: .85, normal: 1, large: 1.15, xlarge: 1.3, xxlarge: 1.5 };
  var PADRAO = { fontSize: "normal", readingFont: "padrao", textSpacing: "normal", highContrast: false, visionMode: "normal",
    highlightLinks: false, readingGuide: "off", readSelection: false, speechRate: 1, libras: false,
    reducedMotion: false, enhancedFocus: false, bigCursor: false };
  var raiz = document.documentElement;
  var temVoz = "speechSynthesis" in window;
  var corMeta = document.querySelector('meta[name="theme-color"]'), corOriginal = corMeta && corMeta.getAttribute("content");

  function ler() {
    var c = {};
    try { c = JSON.parse(localStorage.getItem(CHAVE) || "{}") || {}; } catch (e) {}
    var o = {}; for (var k in PADRAO) o[k] = k in c ? c[k] : PADRAO[k];
    return o;
  }
  var config = ler();

  function aplicar() {
    var e = ESCALA[config.fontSize] || 1;
    raiz.style.fontSize = e === 1 ? "" : Math.round(16 * e) + "px";
    if (e > 1) raiz.setAttribute("data-a11y-tamanho", config.fontSize); else raiz.removeAttribute("data-a11y-tamanho");
    function liga(nome, sim) { if (sim) raiz.setAttribute("data-a11y-" + nome, ""); else raiz.removeAttribute("data-a11y-" + nome); }
    function valor(nome, v, neutro) { if (v === neutro) raiz.removeAttribute("data-a11y-" + nome); else raiz.setAttribute("data-a11y-" + nome, v); }
    liga("contraste", config.highContrast); liga("sem-animacao", config.reducedMotion); liga("links", config.highlightLinks);
    liga("foco", config.enhancedFocus); liga("cursor", config.bigCursor);
    valor("fonte", config.readingFont, "padrao"); valor("espacamento", config.textSpacing, "normal"); valor("visao", config.visionMode, "normal");
    guia(config.readingGuide);
    libras(config.libras);
    leituraAutomatica(config.readSelection);
    if (corMeta) corMeta.setAttribute("content", config.highContrast ? (raiz.getAttribute("data-theme") === "dark" ? "#000000" : "#FFFFFF") : corOriginal);
  }
  function salvar() { try { localStorage.setItem(CHAVE, JSON.stringify(config)); } catch (e) {} }
  function mudar(m, msg) {
    for (var k in m) config[k] = m[k];
    aplicar(); salvar(); desenhar();
    status(msg || "Salvo neste aparelho");
  }

  // ---------- Ícones (traço, como os do resto do site) ----------
  var ICONE_A11Y = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">' +
    '<circle cx="12" cy="12" r="10.25"/><circle cx="12" cy="6.4" r="1.65" fill="currentColor" stroke="none"/><path d="M6.6 9.4c1.9.45 3.6.65 5.4.65s3.5-.2 5.4-.65"/><path d="M12 10.05v3.7"/><path d="M9.5 18.1 12 13.75l2.5 4.35"/></svg>';
  function ico(d) { return '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">' + d + "</svg>"; }
  var I = {
    menos: ico('<path d="M5 12h14"/>'), mais: ico('<path d="M12 5v14M5 12h14"/>'),
    voz: ico('<path d="M11 5 6 9H2v6h4l5 4z"/><path d="M15.5 8.5a5 5 0 0 1 0 7M19 5a10 10 0 0 1 0 14"/>'),
    parar: ico('<rect x="6" y="6" width="12" height="12" rx="1.5"/>'),
    fechar: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
    voltar: ico('<path d="M3 12a9 9 0 1 0 3-6.7L3 8"/><path d="M3 3v5h5"/>')
  };

  // ---------- Painel ----------
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function op(acao, valor, rotulo, ativo, extra) {
    return '<button type="button" class="a11y-op' + (extra && extra.chave ? " a11y-op--chave" : "") + '" data-acao="' + acao + '"' +
      (valor != null ? ' data-valor="' + esc(valor) + '"' : "") + (ativo != null ? ' aria-pressed="' + !!ativo + '"' : "") +
      (extra && extra.attr ? " " + extra.attr : "") + ">" + rotulo + "</button>";
  }
  function chave(nome, rotulo) { return op("alternar", nome, "<span>" + rotulo + "</span>", config[nome], { chave: true }); }
  function grupo(acao, nome, itens) {
    return '<div class="a11y__grupo" role="group" aria-label="' + esc(nome) + '">' +
      itens.map(function (i) { return op(acao, i[0], i[1], config[acao] === i[0] || config[acao] === +i[0], i[2] ? { attr: i[2] } : null); }).join("") + "</div>";
  }
  function secao(titulo, corpo) { return '<section class="a11y__secao"><h3>' + titulo + "</h3>" + corpo + "</section>"; }

  var dlg = document.createElement("dialog");
  dlg.className = "a11y"; dlg.id = "painel-a11y"; dlg.setAttribute("aria-labelledby", "a11y-t");
  dlg.innerHTML = '<div class="a11y__topo"><h2 id="a11y-t">' + ICONE_A11Y + "Acessibilidade</h2>" +
    '<button type="button" class="btn-icone" data-acao="fechar">' + I.fechar + '<span class="sr">Fechar</span></button></div>' +
    '<div class="a11y__corpo"></div>' +
    '<div class="a11y__rodape"><p role="status" aria-live="polite" id="a11y-status">Salvo só neste aparelho</p>' +
    op("restaurar", null, I.voltar + "Restaurar") + "</div>";
  document.body.appendChild(dlg);
  var corpo = dlg.querySelector(".a11y__corpo");
  var statusEl = dlg.querySelector("#a11y-status"), tStatus;
  function status(t) {
    clearTimeout(tStatus); statusEl.textContent = t;
    tStatus = setTimeout(function () { statusEl.textContent = "Salvo só neste aparelho"; }, 2500);
  }

  function desenhar() {
    var i = TAMANHOS.indexOf(config.fontSize);
    var html =
      secao("Tamanho do texto",
        '<div class="a11y__fonte">' + op("fonte", -1, I.menos + '<span aria-hidden="true">A</span><span class="sr">Diminuir o texto</span>', null, { attr: i <= 0 ? "disabled" : "" }) +
        '<span class="a11y__valor" aria-live="polite"><span class="sr">Tamanho: </span>' + Math.round(ESCALA[config.fontSize] * 100) + "%</span>" +
        op("fonte", 1, I.mais + '<span aria-hidden="true">A</span><span class="sr">Aumentar o texto</span>', null, { attr: i >= TAMANHOS.length - 1 ? "disabled" : "" }) + "</div>") +
      secao("Letra e espaçamento",
        '<p class="a11y__rotulo" id="a11y-r-fonte">Fonte de leitura</p>' +
        grupo("readingFont", "Fonte de leitura", [["padrao", "Do site", 'data-fonte="padrao"'], ["legivel", "Legível", 'data-fonte="legivel"'], ["dislexia", "Dislexia", 'data-fonte="dislexia"']]) +
        '<p class="a11y__dica">Legível: Atkinson Hyperlegible, com letras bem diferentes entre si. Dislexia: OpenDyslexic.</p>' +
        '<p class="a11y__rotulo">Espaçamento do texto</p>' +
        grupo("textSpacing", "Espaçamento do texto", [["normal", "Normal"], ["medio", "Médio"], ["amplo", "Amplo"]]) +
        '<p class="a11y__dica">Mais espaço entre linhas, letras e palavras ajuda a não pular linha nos textos longos.</p>') +
      secao("Cores",
        '<div class="a11y__lista">' + chave("highContrast", "Alto contraste") + "</div>" +
        '<p class="a11y__dica">Vale para o modo claro e para o noturno. As figuras das questões continuam como na prova.</p>' +
        '<p class="a11y__rotulo">Ajuste para daltonismo</p>' +
        '<div class="a11y__lista" role="group" aria-label="Ajuste para daltonismo">' +
        [["normal", "Cores normais"], ["deuteranopia", "Deuteranopia (verde)"], ["protanopia", "Protanopia (vermelho)"], ["tritanopia", "Tritanopia (azul)"], ["achromatopsia", "Tons de cinza"]]
          .map(function (m) { return op("visionMode", m[0], m[1], config.visionMode === m[0]); }).join("") + "</div>") +
      secao("Leitura",
        '<div class="a11y__lista">' + chave("highlightLinks", "Destacar links") + "</div>" +
        '<p class="a11y__rotulo">Guia de leitura</p>' +
        grupo("readingGuide", "Guia de leitura", [["off", "Desligado"], ["regua", "Régua"], ["mascara", "Máscara"]]) +
        '<p class="a11y__dica">Uma faixa acompanha o dedo, o mouse ou o foco do teclado. A máscara escurece o resto da tela.</p>' +
        (temVoz ? '<p class="a11y__rotulo">Ouvir em voz alta</p><div class="a11y__lista">' +
          op("lerAgora", null, I.voz + "Ler a questão (ou o trecho selecionado)") + op("pararFala", null, I.parar + "Parar a leitura") +
          chave("readSelection", "Ler sozinho o que eu selecionar") + "</div>" +
          '<p class="a11y__rotulo">Velocidade da voz</p>' + grupo("speechRate", "Velocidade da voz", [["0.75", "Devagar"], ["1", "Normal"], ["1.25", "Rápida"]]) +
          '<p class="a11y__dica">Usa a voz do próprio aparelho: nada é enviado para fora. As figuras são lidas pela descrição.</p>' : "")) +
      secao("Libras",
        '<div class="a11y__lista">' + chave("libras", "Tradutor de Libras (VLibras)") + "</div>" +
        '<p class="a11y__dica">Serviço gratuito do Governo Federal. Ligado, aparece o botão do VLibras na lateral: selecione um texto e toque nele. Precisa de internet.</p>') +
      secao("Movimento e navegação",
        '<div class="a11y__lista">' + chave("reducedMotion", "Reduzir animações") + chave("enhancedFocus", "Foco do teclado reforçado") + chave("bigCursor", "Cursor do mouse grande") + "</div>" +
        '<details class="a11y__atalhos"><summary>Atalhos de teclado</summary><ul>' +
        [[["Alt", "A"], "Abrir ou fechar este painel"], [["Alt", "+"], "Aumentar o texto"], [["Alt", "−"], "Diminuir o texto"], [["Alt", "C"], "Alto contraste"],
         [["Alt", "L"], "Ler a questão ou a seleção"], [["Alt", "R"], "Régua de leitura"], [["Esc"], "Fechar o painel"]]
          .map(function (a) { return '<li><span class="a11y__teclas">' + a[0].map(function (k) { return "<kbd>" + k + "</kbd>"; }).join(" + ") + "</span><span>" + a[1] + "</span></li>"; }).join("") +
        "</ul></details>");
    // redesenha mantendo o foco no mesmo botão
    var ativo = document.activeElement, sel = null;
    if (ativo && dlg.contains(ativo) && ativo.dataset && ativo.dataset.acao) sel = '[data-acao="' + ativo.dataset.acao + '"]' + (ativo.dataset.valor != null ? '[data-valor="' + ativo.dataset.valor + '"]' : "");
    var aberto = corpo.querySelector("details[open]"), rolagem = corpo.scrollTop;
    corpo.innerHTML = html;
    corpo.scrollTop = rolagem;
    if (aberto) corpo.querySelector("details").open = true;
    if (sel) { var el = corpo.querySelector(sel); if (el && el.disabled) el = corpo.querySelector('[data-acao="fonte"]:not([disabled])'); if (el) el.focus({ preventScroll: true }); }
  }

  function mudarFonte(passo) {
    var i = Math.min(TAMANHOS.length - 1, Math.max(0, TAMANHOS.indexOf(config.fontSize) + passo));
    mudar({ fontSize: TAMANHOS[i] }, "Texto em " + Math.round(ESCALA[TAMANHOS[i]] * 100) + "%");
  }
  dlg.addEventListener("click", function (ev) {
    if (ev.target === dlg) { fechar(); return; }                 // toque fora do painel
    var b = ev.target.closest("[data-acao]"); if (!b) return;
    var a = b.dataset.acao, v = b.dataset.valor;
    if (a === "fechar") fechar();
    else if (a === "fonte") mudarFonte(+v);
    else if (a === "alternar") { var m = {}; m[v] = !config[v]; mudar(m, (m[v] ? "Ligado: " : "Desligado: ") + b.textContent.trim()); }
    else if (a === "speechRate") mudar({ speechRate: +v });
    else if (a === "restaurar") { pararFala(); mudar(JSON.parse(JSON.stringify(PADRAO)), "Tudo voltou ao padrão"); }
    else if (a === "lerAgora") { fechar(); lerAgora(); }
    else if (a === "pararFala") pararFala();
    else { var n = {}; n[a] = v; mudar(n); }
  });

  var quemAbriu = null;
  function abrir() {
    quemAbriu = document.activeElement;
    var mais = document.getElementById("folha-mais"); if (mais && mais.open) mais.close();
    desenhar();
    if (dlg.showModal) dlg.showModal(); else dlg.setAttribute("open", "");
    sincronizarBotoes(true);
  }
  function fechar() { if (dlg.close) dlg.close(); else dlg.removeAttribute("open"); }
  dlg.addEventListener("close", function () {
    sincronizarBotoes(false);
    var volta = quemAbriu && document.contains(quemAbriu) && quemAbriu.offsetParent !== null ? quemAbriu : document.getElementById("btn-a11y");
    if (volta) volta.focus();
  });
  function alternarPainel() { if (dlg.open) fechar(); else abrir(); }

  // ---------- Botões: cabeçalho e folha "Mais" ----------
  function sincronizarBotoes(aberto) {
    document.querySelectorAll("[data-abre-a11y]").forEach(function (b) { b.setAttribute("aria-expanded", aberto ? "true" : "false"); });
  }
  var acoes = document.querySelector(".cab__acoes");
  if (acoes) {
    var b = document.createElement("button");
    b.type = "button"; b.className = "btn-icone"; b.id = "btn-a11y"; b.title = "Acessibilidade (Alt + A)";
    b.setAttribute("aria-haspopup", "dialog"); b.setAttribute("aria-controls", "painel-a11y"); b.setAttribute("data-abre-a11y", "");
    b.innerHTML = ICONE_A11Y + '<span class="sr">Acessibilidade</span>';
    acoes.insertBefore(b, acoes.firstChild);
    b.addEventListener("click", abrir);
  }
  var temaFolha = document.getElementById("btn-tema-folha");
  if (temaFolha) {
    var bf = document.createElement("button");
    bf.type = "button"; bf.className = "btn folha__tema"; bf.setAttribute("aria-haspopup", "dialog"); bf.setAttribute("aria-controls", "painel-a11y"); bf.setAttribute("data-abre-a11y", "");
    bf.innerHTML = ICONE_A11Y + "Acessibilidade";
    temaFolha.parentNode.insertBefore(bf, temaFolha);
    bf.addEventListener("click", abrir);
  }
  sincronizarBotoes(false);
  // links "#acessibilidade" em qualquer página abrem o painel
  document.addEventListener("click", function (ev) {
    var a = ev.target.closest && ev.target.closest('a[href$="#acessibilidade"]');
    if (a && a.pathname === location.pathname) { ev.preventDefault(); abrir(); }
  });
  if (location.hash === "#acessibilidade") setTimeout(abrir, 0);

  // ---------- Filtros de cor (daltonismo) ----------
  var svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  svg.setAttribute("class", "a11y-filtros"); svg.setAttribute("aria-hidden", "true"); svg.setAttribute("focusable", "false");
  svg.innerHTML = "<defs>" +
    '<filter id="a11y-deuteranopia"><feColorMatrix type="matrix" values="0.625 0.375 0 0 0  0.7 0.3 0 0 0  0 0.3 0.7 0 0  0 0 0 1 0"/></filter>' +
    '<filter id="a11y-protanopia"><feColorMatrix type="matrix" values="0.567 0.433 0 0 0  0.558 0.442 0 0 0  0 0.242 0.758 0 0  0 0 0 1 0"/></filter>' +
    '<filter id="a11y-tritanopia"><feColorMatrix type="matrix" values="0.95 0.05 0 0 0  0 0.433 0.567 0 0  0 0.475 0.525 0 0  0 0 0 1 0"/></filter></defs>';
  document.body.appendChild(svg);

  // ---------- Guia de leitura ----------
  var guiaEl = null, guiaParar = null;
  function guia(modo) {
    if (guiaParar) { guiaParar(); guiaParar = null; }
    if (guiaEl) { guiaEl.remove(); guiaEl = null; }
    if (!modo || modo === "off") return;
    guiaEl = document.createElement("div");
    guiaEl.className = "a11y-guia a11y-guia--" + modo; guiaEl.setAttribute("aria-hidden", "true");
    document.body.appendChild(guiaEl);
    var y = innerHeight / 3, x = innerWidth / 2, alvo = null, quadro = 0;
    function posicionar() {
      quadro = 0;
      guiaEl.style.setProperty("--y", y + "px");
      var el = alvo || document.elementFromPoint(x, y);
      if (el instanceof Element && !el.closest(".a11y")) {
        var css = getComputedStyle(el), l = parseFloat(css.lineHeight);
        guiaEl.style.setProperty("--linha", Math.round(isFinite(l) ? l : parseFloat(css.fontSize) * 1.4) + "px");
      }
      alvo = null;
    }
    function mover(ny, nx, el) { y = ny; x = nx; alvo = el || null; if (!quadro) quadro = requestAnimationFrame(posicionar); }
    function aoMover(e) { mover(e.clientY, e.clientX); }
    function aoTocar(e) { if (e.touches[0]) mover(e.touches[0].clientY, e.touches[0].clientX); }
    function aoFocar(e) { if (!(e.target instanceof Element) || e.target.closest(".a11y")) return; var r = e.target.getBoundingClientRect(); mover(r.top + r.height / 2, r.left + r.width / 2, e.target); }
    posicionar();
    addEventListener("pointermove", aoMover, { passive: true });
    addEventListener("touchmove", aoTocar, { passive: true });
    document.addEventListener("focusin", aoFocar);
    guiaParar = function () { cancelAnimationFrame(quadro); removeEventListener("pointermove", aoMover); removeEventListener("touchmove", aoTocar); document.removeEventListener("focusin", aoFocar); };
  }

  // ---------- Leitura em voz alta ----------
  var lendoEl = null;
  // Texto falado de um trecho da página: pula o que está escondido e lê as figuras pela descrição (alt).
  function textoDe(el) {
    var partes = [];
    var BLOCO = /^(P|LI|DIV|SECTION|ARTICLE|H[1-6]|TR|TD|TH|FIGCAPTION|BLOCKQUOTE|TABLE|UL|OL|BUTTON|LABEL|FIELDSET)$/;
    (function andar(n) {
      if (n.nodeType === 3) { partes.push(n.nodeValue); return; }
      if (n.nodeType !== 1) return;
      if (n.hidden || n.getAttribute("aria-hidden") === "true" || /^(SCRIPT|STYLE|NOSCRIPT|TEMPLATE|SVG)$/i.test(n.nodeName)) return;
      var css = getComputedStyle(n);
      if (css.display === "none" || css.visibility === "hidden") { if (!n.classList.contains("sr")) return; }
      if (n.nodeName === "IMG") { var alt = (n.getAttribute("alt") || "").trim(); if (alt) partes.push(" Figura: " + alt + ". "); return; }
      if (n.matches("details:not([open])")) { var s = n.querySelector("summary"); if (s) andar(s); return; }
      if (n.matches(".nav,.nav--extra,.barra,.reportar,[role=toolbar]")) return;     // botões de navegação da prova não são lidos
      var bloco = BLOCO.test(n.nodeName);
      if (bloco) partes.push(" \n");
      for (var c = n.firstChild; c; c = c.nextSibling) andar(c);
      if (bloco) partes.push(" \n");
    })(el);
    return partes.join("").replace(/[ \t]+/g, " ").replace(/\s*\n\s*/g, ". ").replace(/(\.\s*){2,}/g, ". ").replace(/([:;?!,])\.\s/g, "$1 ").replace(/^[.\s]+/, "").trim();
  }
  function alvoDaLeitura() {
    var q = document.querySelector("main .questao") || document.querySelector("main .redacao-tema, main article");
    return q || document.querySelector("main") || document.body;
  }
  // O Chrome corta falas longas: divide em frases de até ~220 caracteres e enfileira.
  function pedacos(t) {
    var frases = t.match(/[^.!?;:]+[.!?;:]*\s*/g) || [t], out = [], atual = "";
    frases.forEach(function (f) {
      if ((atual + f).length > 220 && atual) { out.push(atual); atual = ""; }
      while (f.length > 220) { var corte = f.lastIndexOf(" ", 220); if (corte < 60) corte = 220; out.push(f.slice(0, corte)); f = f.slice(corte); }
      atual += f;
    });
    if (atual.trim()) out.push(atual);
    return out;
  }
  function vozPt() {
    var vs = speechSynthesis.getVoices();
    return vs.find(function (v) { return v.lang === "pt-BR"; }) || vs.find(function (v) { return /^pt/i.test(v.lang); }) || null;
  }
  function falar(texto, el) {
    if (!temVoz || !texto || !texto.trim()) return;
    pararFala();
    var v = vozPt(), lista = pedacos(texto.trim().slice(0, 12000));
    if (el) { lendoEl = el; el.classList.add("a11y-lendo"); }
    lista.forEach(function (p, i) {
      var u = new SpeechSynthesisUtterance(p);
      u.lang = "pt-BR"; u.rate = config.speechRate || 1; if (v) u.voice = v;
      if (i === lista.length - 1) u.onend = u.onerror = tirarDestaque;
      speechSynthesis.speak(u);
    });
    if (window.anunciar) anunciar("Lendo em voz alta. Alt + L de novo ou Esc para parar.");
  }
  function tirarDestaque() { if (lendoEl) { lendoEl.classList.remove("a11y-lendo"); lendoEl = null; } }
  function pararFala() { if (temVoz) speechSynthesis.cancel(); tirarDestaque(); }
  function selecao() { var s = window.getSelection && getSelection(); return s ? s.toString() : ""; }
  function lerAgora() {
    if (!temVoz) return;
    if (speechSynthesis.speaking) { pararFala(); return; }
    var s = selecao();
    if (s.trim()) falar(s); else { var el = alvoDaLeitura(); falar(textoDe(el), el); }
  }
  var ultimaLida = "", lerSozinho = null;
  function leituraAutomatica(sim) {
    if (lerSozinho) { document.removeEventListener("mouseup", lerSozinho); document.removeEventListener("keyup", lerSozinho); document.removeEventListener("touchend", lerSozinho); lerSozinho = null; }
    if (!sim || !temVoz) return;
    lerSozinho = function () {
      setTimeout(function () {
        var t = selecao().trim();
        if (t.length > 1 && t !== ultimaLida) falar(t);
        ultimaLida = t;
      }, 30);
    };
    document.addEventListener("mouseup", lerSozinho); document.addEventListener("keyup", lerSozinho); document.addEventListener("touchend", lerSozinho);
  }
  addEventListener("pagehide", function () { if (temVoz) speechSynthesis.cancel(); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && temVoz && speechSynthesis.speaking && !dlg.open) pararFala(); });

  // ---------- VLibras (só carrega quando a pessoa liga) ----------
  var VLIBRAS = "https://vlibras.gov.br/app", vlCarregando = null;
  function libras(sim) {
    var r = document.querySelector("[vw]");
    if (!sim) { if (r) r.style.display = "none"; return; }
    if (r) { r.style.display = ""; return; }
    r = document.createElement("div");
    r.setAttribute("vw", ""); r.className = "enabled";
    r.innerHTML = '<div vw-access-button class="active"></div><div vw-plugin-wrapper><div class="vw-plugin-top-wrapper"></div></div>';
    document.body.appendChild(r);
    if (vlCarregando) return;
    vlCarregando = true;
    var s = document.createElement("script");
    s.src = VLIBRAS + "/vlibras-plugin.js"; s.async = true;
    s.onload = function () {
      try { new window.VLibras.Widget(VLIBRAS); if (typeof window.onload === "function") window.onload(); } catch (e) {}
    };
    s.onerror = function () { vlCarregando = null; status("Não deu para carregar o VLibras. Confira a internet."); if (window.anunciar) anunciar("Não deu para carregar o VLibras. Confira a internet."); };
    document.body.appendChild(s);
  }

  // ---------- Atalhos Alt + tecla (tecla física: funciona em qualquer teclado; AltGr fica livre) ----------
  document.addEventListener("keydown", function (e) {
    if (!e.altKey || e.ctrlKey || e.metaKey) return;
    var t = e.code;
    if (t === "KeyA") alternarPainel();
    else if (t === "Equal" || t === "NumpadAdd") mudarFonte(1);
    else if (t === "Minus" || t === "NumpadSubtract") mudarFonte(-1);
    else if (t === "KeyC") mudar({ highContrast: !config.highContrast }, config.highContrast ? "Alto contraste desligado" : "Alto contraste ligado");
    else if (t === "KeyL") lerAgora();
    else if (t === "KeyR") mudar({ readingGuide: config.readingGuide === "off" ? "regua" : "off" });
    else return;
    e.preventDefault();
    if (t !== "KeyA" && t !== "KeyL" && !dlg.open && window.anunciar) anunciar(statusEl.textContent);
  });

  // o tema (claro/noturno) muda a cor da barra do navegador no alto contraste
  new MutationObserver(function () { aplicar(); }).observe(raiz, { attributes: true, attributeFilter: ["data-theme"] });

  aplicar();
  window.Acessibilidade = { abrir: abrir, fechar: fechar, config: function () { return JSON.parse(JSON.stringify(config)); }, mudar: mudar, ler: lerAgora, parar: pararFala };
})();
