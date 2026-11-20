/* Página Sobre: a "Questão 01" (a origem do projeto) vira uma questão de verdade.
   Sem script, o gabarito já aparece marcado; com ele, a pessoa escolhe uma alternativa e só então vê o gabarito comentado. */
(function () {
  var lista = document.getElementById("origem-alts"), gab = document.getElementById("origem-gab");
  if (!lista || !gab) return;
  var caixa = lista.closest(".q-origem");
  caixa.classList.add("q-origem--jogo");
  gab.hidden = true;
  var itens = Array.prototype.slice.call(lista.children);
  itens.forEach(function (li) {
    var b = document.createElement("button");
    b.type = "button";
    while (li.firstChild) b.appendChild(li.firstChild);
    b.setAttribute("aria-label", "Alternativa " + li.dataset.letra + ": " + b.textContent.replace(/^[A-E]/, "").trim());
    li.appendChild(b);
    b.addEventListener("click", function () {
      itens.forEach(function (x) { x.classList.remove("errada", "revelada"); x.querySelector("button").removeAttribute("aria-pressed"); });
      b.setAttribute("aria-pressed", "true");
      var certa = li.hasAttribute("data-certa");
      if (!certa) li.classList.add("errada");
      lista.querySelector("[data-certa]").classList.add("revelada");
      gab.hidden = false;
      if (window.anunciar) anunciar((certa ? "Acertou. " : "Não foi dessa vez: a resposta é E. ") + gab.textContent.replace(/\s+/g, " ").trim());
    });
  });
})();
