/* Página de fontes: painel público da revisão das explicações e créditos de quem revisa.
   Dados: data/provas.json (contagens por prova, geradas por tools/validar.py --indexar) e data/revisores.json (créditos). */
(function () {
  var alvo = document.getElementById("painel-revisao"), cred = null;   // créditos com nome foram retirados: os revisores pediram para não ser identificados
  if (!alvo) return;
  var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); };
  var pct = function (a, b) { return b ? Math.round(a / b * 100) : 0; };
  var num = function (n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, "."); };
  function barra(a, b, rotulo) {
    return '<div class="progresso" role="progressbar" aria-label="' + esc(rotulo) + '" aria-valuemin="0" aria-valuemax="' + b + '" aria-valuenow="' + a + '"><div class="progresso__barra" style="width:' + pct(a, b) + '%"></div></div>';
  }
  Promise.all([
    fetch("data/provas.json").then(function (r) { if (!r.ok) throw 0; return r.json(); }),
    fetch("data/revisores.json").then(function (r) { return r.ok ? r.json() : { revisores: {} }; }).catch(function () { return { revisores: {} }; })
  ]).then(function (res) {
    var lista = res[0], info = (res[1] && res[1].revisores) || {};
    var bancas = {}, tot = { provas: 0, q: 0, rev: 0, anul: 0, anA: 0 }, pessoas = {};
    lista.forEach(function (p) {
      var b = bancas[p.banca] || (bancas[p.banca] = { provas: 0, q: 0, rev: 0, anul: 0, anA: 0 });
      [b, tot].forEach(function (x) { x.provas++; x.q += p.totalQuestoes || 0; x.rev += p.revisadas || 0; x.anul += p.anuladas || 0; x.anA += p.anuladasPorAnalise || 0; });
      Object.keys(p.revisores || {}).forEach(function (n) { pessoas[n] = (pessoas[n] || 0) + p.revisores[n]; });
    });
    var linhas = Object.keys(bancas).sort().map(function (k) {
      var b = bancas[k];
      return "<tr><th scope=\"row\">" + esc(k) + "<br><span class=\"legenda\">" + b.provas + " provas</span></th><td>" + num(b.q) + "</td><td>" + num(b.rev) + " (" + pct(b.rev, b.q) + "%)</td><td>" + b.anul + "</td></tr>";
    }).join("");
    alvo.innerHTML = "<p><strong>" + num(tot.rev) + "</strong> de <strong>" + num(tot.q) + "</strong> explicações já foram conferidas por uma pessoa (" + pct(tot.rev, tot.q) + "%).</p>" + barra(tot.rev, tot.q, "Explicações revisadas") +
      '<table class="tabela"><caption class="versalete">Por vestibular</caption><thead><tr><th scope="col">Banca</th><th scope="col">Questões</th><th scope="col">Revisadas</th><th scope="col">Anuladas</th></tr></thead><tbody>' + linhas + "</tbody></table>" +
      (tot.anA ? "<p>Das " + tot.anul + " questões anuladas, " + tot.anA + " foram anuladas pela banca sem motivo publicado; nelas, a explicação traz a análise do Treineiros, identificada como tal.</p>" : "") +
      '<p class="legenda">Atualizado sempre que uma prova entra ou muda no site.</p>';
    if (!cred) return;
    var nomes = Object.keys(pessoas).sort(function (a, b) { return pessoas[b] - pessoas[a] || a.localeCompare(b); });
    cred.innerHTML = nomes.length
      ? '<ul class="lista-info">' + nomes.map(function (n) {
          var d = info[n] || {};
          var nome = d.link && /^https:\/\//.test(d.link) ? '<a href="' + esc(d.link) + '" rel="noopener" target="_blank">' + esc(n) + "</a>" : esc(n);
          return "<li><strong>" + nome + "</strong>" + (d.formacao ? ", " + esc(d.formacao) : "") + ": " + pessoas[n] + (pessoas[n] === 1 ? " explicação revisada" : " explicações revisadas") + ".</li>";
        }).join("") + "</ul>"
      : "<p>Ainda não há professores voluntários creditados. Quando alguém revisar explicações, o nome aparece aqui e em cada questão que conferiu.</p>";
  }).catch(function () {
    alvo.innerHTML = "<p>Não foi possível carregar os números agora.</p>";
  });
})();
