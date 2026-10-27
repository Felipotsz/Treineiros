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
