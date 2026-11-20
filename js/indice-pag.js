/* Sumário lateral de páginas longas (Enem, ETEC, FATEC): marca a seção que está na tela. */
(function () {
  var nav = document.querySelector(".sumario-pag");
  if (!nav || !("IntersectionObserver" in window)) return;
  var links = [].slice.call(nav.querySelectorAll("a"));
  function marcar(id) {
    links.forEach(function (a) {
      var on = a.getAttribute("href") === "#" + id;
      a.classList.toggle("atual", on);
      if (on) a.setAttribute("aria-current", "true"); else a.removeAttribute("aria-current");
    });
  }
  var alvos = links.map(function (a) { var h = document.getElementById(a.getAttribute("href").slice(1)); return h && h.closest("section"); }).filter(Boolean);
  if (links[0]) marcar(links[0].getAttribute("href").slice(1));
  var obs = new IntersectionObserver(function (ents) {
    var v = ents.filter(function (e) { return e.isIntersecting; })[0];
    if (v) { var h = v.target.querySelector("h2"); if (h) marcar(h.id); }
  }, { rootMargin: "-25% 0px -65% 0px" });
  alvos.forEach(function (s) { obs.observe(s); });
})();
