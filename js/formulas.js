/* Fórmulas com KaTeX, carregado só quando a página tem fórmula.
   Nos JSONs use \\( ... \\) para fórmula no texto e \\[ ... \\] para fórmula em destaque. */
var Formulas = (function () {
  // KaTeX 0.16.9 guardado no próprio site (funciona offline e sem depender de CDN)
  var base = "assets/vendor/katex/", carregando = null;
  function tem(el) { return /\\\(|\\\[|\$\$/.test(el.textContent); }
  function carregar() {
    if (window.renderMathInElement) return Promise.resolve();
    if (carregando) return carregando;
    carregando = new Promise(function (ok, falha) {
      var css = document.createElement("link"); css.rel = "stylesheet"; css.href = base + "katex.min.css"; document.head.appendChild(css);
      function js(src, depois) { var s = document.createElement("script"); s.src = src; s.onload = depois; s.onerror = falha; document.head.appendChild(s); }
      js(base + "katex.min.js", function () { js(base + "contrib/auto-render.min.js", ok); });
    });
    return carregando;
  }
  function renderizar(el) {
    if (!el || !tem(el)) return;
    carregar().then(function () {
      window.renderMathInElement(el, { throwOnError: false, delimiters: [
        { left: "$$", right: "$$", display: true }, { left: "\\[", right: "\\]", display: true }, { left: "\\(", right: "\\)", display: false }] });
    }).catch(function () { /* sem internet: a fórmula aparece como texto */ });
  }
  return { renderizar: renderizar };
})();
