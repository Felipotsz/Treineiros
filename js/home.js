/* Página inicial: questão de demonstração e o lembrete de contagem regressiva e sequência de dias. */
(function () {
  // Questão de demonstração: marcar = preencher a bolha; mostra a correção logo abaixo
  var demo = document.getElementById("experimente");
  if (demo) {
    var gab = demo.dataset.gabarito, expl = document.getElementById("demo-expl");
    var botoes = [].slice.call(demo.querySelectorAll(".alt"));
    function responder(letra) {
      botoes.forEach(function (b) {
        var l = b.dataset.letra, st = b.querySelector(".alt__status");
        b.classList.remove("is-correta", "is-errada", "is-selecionada");
        b.setAttribute("aria-disabled", "true"); b.removeAttribute("aria-pressed");
        if (l === gab) { b.classList.add("is-correta"); st.textContent = letra === gab ? "Você acertou" : "Gabarito"; }
        else if (l === letra) { b.classList.add("is-errada"); st.textContent = "Sua resposta"; }
        else st.textContent = "";
      });
      expl.hidden = false; expl.focus();
      if (window.Registro) Registro.somarAtividade(1);
    }
    botoes.forEach(function (b) {
      b.addEventListener("click", function () { if (b.getAttribute("aria-disabled") !== "true") responder(b.dataset.letra); });
    });
    document.getElementById("demo-de-novo").addEventListener("click", function () {
      botoes.forEach(function (b) { b.classList.remove("is-correta", "is-errada"); b.removeAttribute("aria-disabled"); b.setAttribute("aria-pressed", "false"); b.querySelector(".alt__status").textContent = ""; });
      expl.hidden = true; botoes[0].focus();
    });
  }

  // Contagem regressiva e sequência de dias, se o aluno já definiu
  var el = document.getElementById("status-home");
  if (!el || !window.Registro) return;
  var alvo = Armazem.ler("alvo", null), seq = Registro.sequencia(), partes = [];
  if (alvo && alvo.data) {
    var d = Registro.diasAte(alvo.data);
    if (d > 0) partes.push("Faltam " + d + (d === 1 ? " dia" : " dias") + " para " + alvo.nome + ".");
    else if (d === 0) partes.push("A prova de " + alvo.nome + " é hoje. Boa sorte!");
  }
  if (seq > 0) partes.push("Você estudou " + seq + (seq === 1 ? " dia seguido." : " dias seguidos."));
  el.textContent = partes.join(" ");
})();
