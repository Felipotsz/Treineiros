/* Revisão do autor: lista questões pendentes, permite editar a explicação e marcar como conferida.
   As alterações ficam em "revisao-autor" e são baixadas como revisao.json para o tools/aplicar_revisao.py. */
(function () {
  const $ = s => document.querySelector(s), E = Render.esc;
  const CH = "revisao-autor";                       // { "provaId#numero": { revisada: true, explicacao: "..." } }
  let provas = {}, alts = Armazem.ler(CH, {});
  const chave = (p, q) => p.id + "#" + q.numero;
  const problemas = q => {
    const v = [];
    if (!q.explicacaoRevisada) v.push("não revisada");
    if (!q.explicacao) v.push("sem explicação");
    else if (/REVISAR/.test(q.explicacao)) v.push("marcada REVISAR");
    if (!q.assunto) v.push("sem assunto");
    if (q.gabarito === "ANULADA") v.push("anulada");
    return v;
  };
  function gravar() { Armazem.gravar(CH, alts); resumo(); }
  function resumo() {
    const n = Object.keys(alts).length;
    $("#r-baixar").disabled = !n;
    $("#r-baixar").textContent = n ? `Baixar alterações (${n})` : "Baixar alterações (revisao.json)";
  }
  function lista() {
    const id = $("#r-prova").value, todas = $("#r-mostrar").value === "todas";
    const itens = [];
    Object.keys(provas).sort().forEach(pid => {
      if (id && pid !== id) return;
      provas[pid].questoes.forEach(q => { const pr = problemas(q); if (todas || pr.length) itens.push({ p: provas[pid], q: q, pr: pr }); });
    });
    $("#r-resumo").textContent = itens.length + (itens.length === 1 ? " questão" : " questões");
    $("#r-lista").innerHTML = itens.map(({ p, q, pr }, i) => {
      const k = chave(p, q), a = alts[k] || {};
      return `<details class="revisao" data-k="${E(k)}"><summary>${E(p.titulo)} · questão ${q.numero} · ${E(q.materia)}${q.assunto ? " · " + E(q.assunto) : ""}${pr.length ? " · " + pr.join(", ") : ""}${a.revisada ? " · conferida aqui" : ""}</summary>
        <p class="origem">${E(Registro.rotuloOrigem(p, q))} · arquivo data/provas/${E(p.id)}.json</p>
        ${Render.enunciado(q)}${Render.anulacao(q)}
        ${Render.alternativas(q, q.gabarito)}
        <p><strong>Gabarito no JSON:</strong> ${E(q.gabarito)}</p>
        <p><label for="e${i}">Explicação (HTML simples; fórmulas com \\( \\))</label><br>
        <textarea id="e${i}" class="campo" rows="5" data-campo="explicacao">${E(a.explicacao !== undefined ? a.explicacao : q.explicacao || "")}</textarea></p>
        <div class="explicacao" aria-live="polite"><span class="explicacao__rotulo">Prévia</span><p class="previa">${a.explicacao !== undefined ? a.explicacao : q.explicacao || ""}</p></div>
        <p><label class="chk"><input type="checkbox" data-campo="revisada"${a.revisada ? " checked" : ""}> Conferi enunciado, alternativas, gabarito e explicação com o PDF</label></p>
      </details>`;
    }).join("") || "<p>Nada pendente com esses filtros. Bom trabalho!</p>";
    $("#r-lista").querySelectorAll("details").forEach(d => {
      const k = d.dataset.k, [pid, num] = k.split("#"), q = provas[pid].questoes.find(x => String(x.numero) === num);
      const t = d.querySelector("textarea"), c = d.querySelector("[data-campo=revisada]"), prev = d.querySelector(".previa");
      let timer = null;
      t.addEventListener("input", () => {
        const a = alts[k] || (alts[k] = {});
        if (t.value === (q.explicacao || "")) delete a.explicacao; else a.explicacao = t.value;
        if (!Object.keys(a).length) delete alts[k];
        gravar();
        clearTimeout(timer); timer = setTimeout(() => { prev.innerHTML = t.value; Formulas.renderizar(prev); }, 400);
      });
      c.addEventListener("change", () => {
        const a = alts[k] || (alts[k] = {});
        if (c.checked) a.revisada = true; else delete a.revisada;
        if (!Object.keys(a).length) delete alts[k];
        gravar();
      });
      d.addEventListener("toggle", () => { if (d.open) Formulas.renderizar(d); }, { once: true });
    });
  }
  $("#r-baixar").addEventListener("click", () => {
    const corpo = JSON.stringify({ app: "treineiros-revisao", geradoEm: new Date().toISOString(), alteracoes: alts }, null, 2);
    const url = URL.createObjectURL(new Blob([corpo], { type: "application/json" }));
    const a = document.createElement("a"); a.href = url; a.download = "revisao.json"; document.body.appendChild(a); a.click(); a.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  });
  $("#r-limpar").addEventListener("click", () => {
    if (!window.confirm("Descartar todas as marcações e explicações editadas neste navegador?")) return;
    alts = {}; gravar(); lista();
  });
  ["#r-prova", "#r-mostrar"].forEach(s => $(s).addEventListener("change", lista));
  resumo();
  Treino.carregarTodas().then(p => {
    provas = p;
    $("#r-prova").innerHTML = '<option value="">Todas as provas</option>' + Object.keys(p).sort().map(id => `<option value="${E(id)}">${E(p[id].titulo)}</option>`).join("");
    lista();
  }).catch(() => { $("#r-lista").innerHTML = "<p>Não foi possível carregar as provas. Use um servidor local (veja o README).</p>"; });
})();
