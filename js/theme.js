/* Tema claro/noturno. Carregar no <head> SEM defer, para não "piscar". */
(function () {
  var CHAVE = "treineiros:tema";
  function ler() { try { return localStorage.getItem(CHAVE); } catch (e) { return null; } }
  function aplicar(t) {
    document.documentElement.setAttribute("data-theme", t);
    document.documentElement.style.colorScheme = t;
  }
  var prefereEscuro = window.matchMedia && matchMedia("(prefers-color-scheme: dark)").matches;
  aplicar(ler() || (prefereEscuro ? "dark" : "light"));
  // Menu de acessibilidade (js/acessibilidade.js): aplica as escolhas salvas antes de desenhar a página, sem piscar
  try {
    var a11y = JSON.parse(localStorage.getItem("treineiros:acessibilidade") || "{}"), raiz = document.documentElement;
    var escala = { small: .85, large: 1.15, xlarge: 1.3, xxlarge: 1.5 }[a11y.fontSize];
    if (escala) raiz.style.fontSize = Math.round(16 * escala) + "px";
    if (escala > 1) raiz.setAttribute("data-a11y-tamanho", a11y.fontSize);
    ["contraste:highContrast", "sem-animacao:reducedMotion", "links:highlightLinks", "foco:enhancedFocus", "cursor:bigCursor"].forEach(function (p) {
      p = p.split(":"); if (a11y[p[1]]) raiz.setAttribute("data-a11y-" + p[0], "");
    });
    if (a11y.readingFont && a11y.readingFont !== "padrao") raiz.setAttribute("data-a11y-fonte", a11y.readingFont);
    if (a11y.textSpacing && a11y.textSpacing !== "normal") raiz.setAttribute("data-a11y-espacamento", a11y.textSpacing);
    if (a11y.visionMode && a11y.visionMode !== "normal") raiz.setAttribute("data-a11y-visao", a11y.visionMode);
  } catch (e) {}
  window.Tema = {
    atual: function () { return document.documentElement.getAttribute("data-theme"); },
    alternar: function () {
      var novo = this.atual() === "dark" ? "light" : "dark";
      aplicar(novo);
      try { localStorage.setItem(CHAVE, novo); } catch (e) {}
      return novo;
    }
  };
})();
