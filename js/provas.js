/* Seleção de provas: todas as edições por ano (inclusive as que não tiveram prova), filtro por banca e ano,
   andamento de cada prova e opção de guardar a prova para usar sem internet. */
(function () {
  const $ = s => document.querySelector(s), E = Render.esc;
  const params = new URLSearchParams(location.search);
  const lista = $("#lista"), contagem = $("#contagem"), fAno = $("#f-ano"), fSo = $("#f-so");
  const CACHE_DADOS = "treineiros-dados";           // o mesmo nome do sw.js: provas guardadas para uso offline
  let edicoes = [], disponiveis = {}, banca = "";
  const BANCAS = { ETEC: "Vestibulinho ETEC", FATEC: "Vestibular FATEC" };

  // Junta as edições (edicoes.json) com as provas que já estão no site (provas.json)
  function montarLista(eds, provas) {
    provas.forEach(p => { disponiveis[p.id] = p; });
    const vistas = new Set(eds.map(e => e.id));
    provas.filter(p => !vistas.has(p.id)).forEach(p => eds.push({ id: p.id, banca: p.banca, ano: p.ano, semestre: p.semestre, dataExame: p.dataExame }));
    return eds.map(e => Object.assign({}, e, { prova: disponiveis[e.id] || null }))
      .sort((a, b) => b.ano - a.ano || (b.semestre || 0) - (a.semestre || 0) || a.banca.localeCompare(b.banca));
  }

  function situacao(p) {
    const and = Armazem.ler("andamento:" + p.id, null);
    if (and && and.respostas) {
      const feitas = Object.keys(and.respostas).length;
      return { texto: `Em andamento: ${feitas} de ${p.totalQuestoes} respondidas`, continuar: true };
    }
    const res = Armazem.ler("resultado:" + p.id, null);
    if (res && res.respostas) {
      const h = Armazem.ler("historico", []).find(x => x.provaId === p.id);
      return { texto: h ? `Última vez: ${h.acertos} de ${h.total} acertos` : "Você já fez esta prova", continuar: false };
    }
    return null;
  }

  function cartao(e) {
    const sem = e.semestre ? `${e.semestre}º semestre` : "";
    const nome = `${BANCAS[e.banca] || e.banca}${sem ? ", " + sem : ""}`;
    const data = e.dataExame ? `Prova de ${Render.dataBr(e.dataExame)}` : "";
    const p = e.prova;
    if (!p) {
      // cartão compacto: o motivo completo aparece uma vez só, no topo do ano (notaAno)
      const tipo = e.status === "sem-prova" ? "sem-prova" : "em-breve";
      const rot = e.status === "sem-prova" ? "Sem prova (pandemia)" : e.status === "em-breve" ? "Em breve" : "Em preparação";
      return `<article class="ed ed--mini ed--${tipo}" data-banca="${E(e.banca)}" aria-label="${E(nome)}, ${e.ano}: ${rot}">
        <p class="ed__topo"><span class="ed__banca">${E(e.banca)}</span> <strong class="ed__nome">${E(sem || String(e.ano))}</strong></p>
        <p class="ed__meta">${rot}${data ? ". " + data : ""}</p></article>`;
    }
    const sit = situacao(p);
    const meta = [`${p.totalQuestoes} questões`, Motor.duracaoTexto(p.duracaoMinutos)];
    if (p.anuladas) meta.push(`${p.anuladas} ${p.anuladas === 1 ? "anulada" : "anuladas"}`);
    return `<article class="ed ed--ok" data-banca="${E(p.banca)}">
      <p class="ed__topo"><span class="ed__banca">${E(p.banca)}</span>${p.revisadas === p.totalQuestoes ? ' <span class="ed__estado">explicações revisadas</span>' : ""}</p>
      <h3 class="ed__nome">${E(sem || String(p.ano))}</h3>
      <p class="ed__meta">${data}${data ? "<br>" : ""}${meta[0]} em ${meta[1]}${p.anuladas ? ` (${meta[2]})` : ""}</p>
      ${sit ? `<p class="ed__sit">${E(sit.texto)}</p>` : ""}
      <p class="ed__acoes"><a class="btn${sit && sit.continuar ? "" : " btn--primary"}" href="simulado.html?id=${encodeURIComponent(p.id)}">${sit && sit.continuar ? "Continuar" : sit ? "Fazer de novo" : "Começar"}<span class="sr"> ${E(nome)} ${p.ano}</span></a>
        <button type="button" class="btn btn--ghost ed__off" data-off="${E(p.id)}" hidden>Guardar para usar sem internet</button></p>
    </article>`;
  }

  function render() {
    const ano = fAno.value, so = fSo.checked;
    if (banca === "Enem") {
      lista.innerHTML = `<section class="ano"><h2>Enem</h2><article class="ed ed--em-breve"><p class="ed__topo"><span class="tag">Enem</span> <span class="ed__estado">Em breve</span></p>
        <p class="ed__motivo">As provas do Enem ainda vão ser adicionadas. Enquanto isso, treine a redação com os temas oficiais.</p><p><a class="btn" href="redacao.html">Treinar a redação</a></p></article></section>`;
      contagem.textContent = "";
      return;
    }
    const vis = edicoes.filter(e => (!banca || e.banca === banca) && (!ano || String(e.ano) === ano) && (!so || e.prova));
    const porAno = {};
    vis.forEach(e => { (porAno[e.ano] = porAno[e.ano] || []).push(e); });
    const anos = Object.keys(porAno).sort((a, b) => b - a);
    const prep = vis.some(e => !e.prova && !e.status)
      ? '<p class="ano__nota">Provas “em preparação” estão sendo digitadas para o site, com questões, figuras e explicações conferidas uma a uma.</p>' : "";
    lista.innerHTML = prep + (anos.map(a => `<section class="ano" aria-labelledby="ano-${a}"><h2 id="ano-${a}">${a}</h2>${notaAno(+a, porAno[a])}<div class="ano__grade">${porAno[a].map(cartao).join("")}</div></section>`).join("")
      || '<p class="vazio">Nenhuma prova com esses filtros.</p>');
    const n = vis.filter(e => e.prova).length;
    contagem.textContent = n + (n === 1 ? " prova disponível" : " provas disponíveis") + (vis.length > n ? `, ${vis.length - n} sem prova ou em breve` : "") + ".";
    ligarOffline();
  }
  // 2021: nenhum semestre teve prova. Avisa uma vez, no topo do ano, em vez de repetir em cada cartão.
  function notaAno(ano, eds) {
    const sem = eds.filter(e => !e.prova && e.status === "sem-prova"), breve = eds.filter(e => !e.prova && e.status === "em-breve");
    const notas = [];
    if (sem.length && sem.length === eds.length) notas.push(`Em ${ano} não houve prova em nenhum semestre: por causa da pandemia de covid-19, o Centro Paula Souza selecionou os candidatos pela análise do histórico escolar.`);
    else if (sem.length) notas.push(`Semestres marcados “sem prova”: por causa da pandemia de covid-19, a seleção foi pela análise do histórico escolar.${ano === 2022 ? " As provas presenciais voltaram no 2º semestre de 2022." : ""}`);
    if (breve.length) notas.push((breve.length === 1 ? "A prova marcada “em breve” aconteceu" : "As provas marcadas “em breve” aconteceram") + ", mas ainda não foram adicionadas ao Treineiros.");
    return notas.map(n => `<p class="ano__nota">${n}</p>`).join("");
  }

  /* ---- Guardar para usar sem internet: põe a prova e as figuras no cache que o sw.js usa ---- */
  function ligarOffline() {
    if (!("caches" in window) || !("serviceWorker" in navigator) || location.protocol !== "https:") return;   // só no site publicado
    lista.querySelectorAll("[data-off]").forEach(b => {
      const p = disponiveis[b.dataset.off];
      caches.open(CACHE_DADOS).then(c => c.match(p.arquivo)).then(r => {
        b.hidden = false;
        if (r) { b.textContent = "Disponível sem internet ✓"; b.disabled = true; }
      }).catch(() => {});
      b.onclick = () => {
        b.disabled = true; b.textContent = "Guardando…";
        Dados.prova(p.id).then(prova => {
          const urls = [p.arquivo].concat(...prova.questoes.map(q => Render.imagens(q).map(i => i.src)));
          Object.values(prova.imagensProva || {}).forEach(i => urls.push(i.src));
          return caches.open(CACHE_DADOS).then(c => c.addAll([...new Set(urls)]));
        }).then(() => { b.textContent = "Disponível sem internet ✓"; })
          .catch(() => { b.disabled = false; b.textContent = "Não deu certo. Tentar de novo"; });
      };
    });
  }

  function marcarChip() { document.querySelectorAll(".chip").forEach(c => c.setAttribute("aria-pressed", c.dataset.banca === banca)); }
  document.querySelectorAll(".chip").forEach(c => c.addEventListener("click", () => {
    banca = c.dataset.banca; marcarChip(); render();
    const u = new URLSearchParams(location.search); if (banca) u.set("banca", banca.toLowerCase()); else u.delete("banca");
    history.replaceState(null, "", location.pathname + (u.toString() ? "?" + u : "") + location.hash);
  }));
  fAno.addEventListener("change", render); fSo.addEventListener("change", render);

  Promise.all([Dados.edicoes(), Dados.lista()]).then(([eds, provas]) => {
    edicoes = montarLista(eds, provas);
    const anos = [...new Set(edicoes.map(e => e.ano))].sort((a, b) => b - a);
    fAno.innerHTML = '<option value="">Todos os anos</option>' + anos.map(a => `<option>${a}</option>`).join("");
    const b = (params.get("banca") || "").toLowerCase();
    banca = { etec: "ETEC", fatec: "FATEC", enem: "Enem" }[b] || "";
    marcarChip(); render();
  }).catch(() => { lista.innerHTML = '<p class="vazio">Não foi possível carregar a lista de provas. Se abriu o arquivo direto, use um servidor local (veja o README).</p>'; });
})();
