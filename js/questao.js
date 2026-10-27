/* Questão avulsa: questao.html?id=<prova>&n=<número>. Serve para mandar uma questão a alguém (professor, grupo de estudo). */
(function () {
  const params = new URLSearchParams(location.search), ID = params.get("id"), N = parseInt(params.get("n"), 10);
  const app = document.getElementById("app"), aviso = document.getElementById("aviso"), E = Render.esc;
  const falar = t => { aviso.textContent = t; aviso.hidden = false; if (window.anunciar) anunciar(t); };
  const erro = msg => { app.innerHTML = `<h1>Questão</h1><p>${E(msg)}</p><p><a class="btn" href="busca.html">Buscar questões</a></p>`; };
  if (!ID || !(N > 0)) return erro("Endereço incompleto: falta a prova ou o número da questão.");

  fetch("data/provas.json").then(r => { if (!r.ok) throw 0; return r.json(); }).then(lista => {
    const item = Array.isArray(lista) && lista.find(p => p.id === ID);
    if (!item) throw new Error("prova");
    return fetch(item.arquivo).then(r => { if (!r.ok) throw 0; return r.json(); });
  }).then(prova => {
    const i = prova.questoes.findIndex(q => q.numero === N);
    if (i < 0) return erro("Esta prova não tem a questão " + N + ".");
    mostrar(prova, i, null);
  }).catch(e => erro(e && e.message === "prova" ? "Não encontramos esta prova." : "Não foi possível carregar a questão."));

  function mostrar(prova, i, resposta) {
    const q = prova.questoes[i], ant = prova.questoes[i - 1], prox = prova.questoes[i + 1], rev = !!resposta;
    const rot = Registro.rotuloOrigem(prova, q);
    document.title = rot + " | Treineiros";
    const alts = Object.keys(q.alternativas).map(l => {
      let cls = "alt", st = "";
      if (rev && q.gabarito !== "ANULADA") {
        if (l === q.gabarito) { cls += " is-correta"; st = resposta === l ? "Você acertou" : "Gabarito"; }
        else if (l === resposta) { cls += " is-errada"; st = "Errada"; }
      } else if (l === resposta) cls += " is-selecionada";
      return `<button type="button" class="${cls}" data-letra="${l}"${rev ? ' aria-disabled="true"' : ""}><span class="alt__letra">${l}</span><span>${Render.alternativa(q, l)}</span><span class="alt__status">${st}</span></button>`;
    }).join("");
    app.innerHTML = `<section class="questao" aria-labelledby="qt">
        <h1 id="qt" tabindex="-1">${E(rot)}</h1>
        ${Render.tags(q)}
        ${Render.enunciado(q)}
        <div role="group" aria-label="Alternativas">${alts}</div>
        ${rev ? Render.explicacao(q) : ""}
        <div class="nav">
          ${ant ? `<a class="btn" href="?id=${encodeURIComponent(ID)}&n=${ant.numero}">Anterior</a>` : ""}
          ${prox ? `<a class="btn" href="?id=${encodeURIComponent(ID)}&n=${prox.numero}">Próxima</a>` : ""}
          <button type="button" class="btn" id="b-link">Copiar link desta questão</button>
          <a class="btn btn--primary" href="simulado.html?id=${encodeURIComponent(ID)}">Fazer a prova inteira</a>
          <button type="button" class="btn btn--ghost" id="b-rep">Reportar erro</button>
        </div></section>`;
    app.querySelectorAll(".alt").forEach(b => b.addEventListener("click", () => {
      if (rev) return;
      Registro.somarAtividade(1);
      mostrar(prova, i, b.dataset.letra);
      const ex = app.querySelector(".explicacao"); if (ex) { ex.setAttribute("tabindex", "-1"); ex.focus(); }
    }));
    document.getElementById("b-link").onclick = () => Registro.copiar(location.href).then(ok => falar(ok ? "Link copiado." : "Não foi possível copiar o link."));
    document.getElementById("b-rep").onclick = () => Reportar.abrir(prova, q).then(res => falar(Reportar.mensagem(res)));
    Formulas.renderizar(app);
  }
})();
