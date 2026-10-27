/* Meu estudo: painel do dia, revisão espaçada, plano, treino por matéria, estatísticas e caderno de erros. */
(function () {
  const $ = s => document.querySelector(s);
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const dizer = txt => { $("#status").textContent = txt; };
  const ir = url => { location.href = url; };
  const dataBr = s => typeof s === "string" ? s.split("-").reverse().join("/") : "—";

  let indice = [], idx = new Set();
  const bancaDe = {};                // id da prova → banca

  /* ---- Hoje: meta diária, sequência e contagem regressiva ---- */
  function painel() {
    const metaSalva = Armazem.ler("meta", { questoesDia: 10 });
    const meta = { questoesDia: metaSalva.questoesDia >= 1 ? Math.floor(metaSalva.questoesDia) : 10 };   // evita divisão por zero
    const feitas = Armazem.ler("atividade", {})[Registro.hoje()] || 0;
    const alvo = Armazem.ler("alvo", null), seq = Registro.sequencia();
    let contagem = "<p>Defina a data da sua prova para acompanhar quantos dias faltam.</p>";
    const d = alvo && typeof alvo.data === "string" ? Registro.diasAte(alvo.data) : NaN;
    if (alvo && isNaN(d)) contagem = "<p>A data salva não é válida. Defina de novo.</p>";
    else if (alvo) {
      contagem = d > 0 ? `<p>Faltam <strong>${d}</strong> ${d === 1 ? "dia" : "dias"} para ${esc(alvo.nome)}.</p>`
        : d === 0 ? `<p>A prova de ${esc(alvo.nome)} é <strong>hoje</strong>. Boa sorte!</p>` : "<p>A data da prova já passou. Defina uma nova.</p>";
    }
    $("#painel").innerHTML = `
      <p><strong>${seq}</strong> ${seq === 1 ? "dia seguido" : "dias seguidos"} estudando.</p>
      <p>Hoje: <strong>${feitas}</strong> de <strong>${meta.questoesDia}</strong> questões.</p>
      <div class="progresso" role="progressbar" aria-label="Meta de hoje" aria-valuemin="0" aria-valuemax="${meta.questoesDia}" aria-valuenow="${Math.min(feitas, meta.questoesDia)}"><div class="progresso__barra" style="width:${Math.min(100, feitas / meta.questoesDia * 100)}%"></div></div>
      <form id="f-meta" class="linha"><label for="i-meta">Meta diária (questões)</label><input id="i-meta" class="campo" type="number" min="1" max="500" value="${meta.questoesDia}"><button class="btn" type="submit">Salvar meta</button></form>
      <h3>Contagem regressiva</h3>${contagem}
      <form id="f-alvo" class="linha"><span class="par"><label for="i-nome">Prova</label><input id="i-nome" class="campo" value="${alvo && alvo.nome ? esc(alvo.nome) : ""}" placeholder="ex.: ETEC"></span><span class="par"><label for="i-data">Data</label><input id="i-data" class="campo" type="date" value="${alvo && /^\d{4}-\d{2}-\d{2}$/.test(alvo.data) ? alvo.data : ""}"></span><button class="btn" type="submit">Salvar</button></form>`;
    $("#f-meta").addEventListener("submit", e => {
      e.preventDefault();
      const n = parseInt($("#i-meta").value, 10);
      if (n >= 1 && n <= 500) { Armazem.gravar("meta", { questoesDia: n }); painel(); dizer("Meta salva."); }
      else dizer("A meta deve ficar entre 1 e 500 questões.");
    });
    $("#f-alvo").addEventListener("submit", e => {
      e.preventDefault();
      const nome = $("#i-nome").value.trim(), data = $("#i-data").value;
      if (!nome || !data) return dizer("Preencha o nome da prova e a data.");
      Armazem.gravar("alvo", { nome: nome, data: data }); painel(); dizer("Contagem regressiva salva.");
    });
  }

  /* ---- Treinos montados a partir de várias provas ----
     O sorteio usa só o índice leve; depois baixa apenas as provas das questões escolhidas. */
  const existe = r => idx.has(r.provaId + "#" + r.numero);
  function montarDeRefs(refs, titulo) {
    dizer("Montando o treino…");
    return Dados.provas(refs.map(r => r.provaId)).then(ps => {
      const itens = refs.map(r => ps[r.provaId] && { prova: ps[r.provaId], q: ps[r.provaId].questoes.find(q => q.numero === r.numero) }).filter(x => x && x.q);
      if (!itens.length) return dizer("Não foi possível carregar essas questões agora. Confira a internet e tente de novo.");
      ir(Treino.montar(titulo, itens));
    }).catch(() => dizer("Não foi possível carregar as provas agora. Confira a internet e tente de novo."));
  }
  function treinoDeEntradas(entradas, titulo, limite) {
    if (!entradas.length) return dizer("Não há questões em aberto para treinar com esses filtros.");
    const refs = entradas.filter(existe).slice(0, limite || 30);
    if (!refs.length) return dizer("Essas questões não estão disponíveis no site agora.");
    montarDeRefs(refs, titulo);
  }
  // Treino sorteado com filtros. assuntos: lista de chaves "Matéria · Assunto" (vazia = qualquer assunto das matérias)
  function treinoFiltrado(materias, assuntos, qtd, banca, titulo) {
    const pool = indice.filter(x => !x.x && materias.includes(x.m) && (!banca || bancaDe[x.p] === banca)
      && (!assuntos.length || assuntos.includes(x.m + " · " + x.a)));
    if (!pool.length) return dizer("Não há questões com esses filtros.");
    const nomes = assuntos.length ? assuntos.map(a => a.split(" · ")[1]) : materias;
    montarDeRefs(Treino.embaralhar(pool).slice(0, qtd).map(x => ({ provaId: x.p, numero: x.n })), titulo || "Treino: " + nomes.join(", "));
  }

  function revisao() {
    const pend = Registro.pendentesHoje().filter(existe);
    $("#revisao").innerHTML = pend.length
      ? `<p><strong>${pend.length}</strong> ${pend.length === 1 ? "questão pede" : "questões pedem"} revisão hoje, no ritmo da revisão espaçada.</p><button class="btn btn--primary" id="b-rev" type="button">Revisar agora</button>`
      : "<p>Nada para revisar hoje. As questões erradas voltam aqui no dia certo, para reforçar a memória.</p>";
    const b = $("#b-rev"); if (b) b.onclick = () => treinoDeEntradas(pend, "Revisão de hoje", 30);
  }
  // Plano: os assuntos (mín. 3 questões) e as matérias (mín. 5) com menor percentual de acertos
  function plano() {
    const est = Registro.estatisticas(Armazem.ler("historico", []));
    const fracos = (grupo, minimo) => Object.keys(grupo).map(k => Object.assign({ k: k }, grupo[k])).filter(x => x.total >= minimo && x.pct < 100).sort((a, b) => a.pct - b.pct || b.total - a.total);
    const assuntos = fracos(est.porAssunto, 3).slice(0, 5), materias = fracos(est.porMateria, 5).slice(0, 3);
    const item = (rot, x, attr) => `<li><span><strong>${rot}</strong>: ${x.pct}% de acertos (${x.acertos} de ${x.total})</span><button type="button" class="btn" ${attr}>Treinar 10 questões</button></li>`;
    let html = "";
    if (assuntos.length) html += `<h3>Assuntos para reforçar</h3><ul class="lista-plano">${assuntos.map(x => item(`${esc(x.assunto)} <span class="tag">${esc(x.materia)}</span>`, x, `data-assunto="${esc(x.k)}" data-mat="${esc(x.materia)}"`)).join("")}</ul>`;
    if (materias.length) html += `<h3>Matérias para reforçar</h3><ul class="lista-plano">${materias.map(x => item(esc(x.k), x, `data-mat="${esc(x.k)}"`)).join("")}</ul>`;
    $("#plano").innerHTML = html || "<p>Faça alguns simulados e o plano aparece aqui, com os assuntos e as matérias que mais precisam de treino.</p>";
    $("#plano").querySelectorAll("[data-mat]").forEach(b => {
      b.onclick = () => treinoFiltrado([b.dataset.mat], b.dataset.assunto ? [b.dataset.assunto] : [], 10, "");
    });
  }
  function treinoForm() {
    const mats = [...new Set(indice.map(x => x.m))].sort(), bancas = [...new Set(Object.values(bancaDe))].sort();
    // assuntos por matéria, com quantas questões cada um tem (sem as anuladas)
    const porMat = {};
    indice.forEach(x => {
      if (!x.a || x.x) return;
      const m = porMat[x.m] || (porMat[x.m] = {}); m[x.a] = (m[x.a] || 0) + 1;
    });
    $("#treino").innerHTML = mats.length ? `<form id="f-treino"><fieldset><legend>Matérias</legend>${mats.map((m, i) => `<label class="chk"><input type="checkbox" name="mat" value="${esc(m)}"${i === 0 ? " checked" : ""}> ${esc(m)}</label>`).join("")}</fieldset>
      <fieldset id="t-assuntos"><legend>Assuntos (opcional: sem marcar nenhum, vale qualquer assunto)</legend><div></div></fieldset>
      <div class="linha"><label for="t-qtd">Quantidade</label><select id="t-qtd" class="campo">${[10, 20, 30, 50].map(n => `<option>${n}</option>`).join("")}</select>
      <label for="t-banca">Banca</label><select id="t-banca" class="campo"><option value="">Todas</option>${bancas.map(b => `<option>${esc(b)}</option>`).join("")}</select>
      <button class="btn btn--primary" type="submit">Montar treino</button></div></form>` : "<p>Ainda não há provas carregadas.</p>";
    const f = $("#f-treino"); if (!f) return;
    // a lista de assuntos acompanha as matérias marcadas (mantendo o que já estava marcado)
    function atualizarAssuntos() {
      const marcados = new Set([...f.querySelectorAll("[name=assunto]:checked")].map(x => x.value));
      const sel = [...f.querySelectorAll("[name=mat]:checked")].map(x => x.value);
      const html = sel.map(m => Object.keys(porMat[m] || {}).sort().map(a => {
        const k = m + " · " + a;
        return `<label class="chk"><input type="checkbox" name="assunto" value="${esc(k)}"${marcados.has(k) ? " checked" : ""}> ${esc(a)} <span class="legenda">(${porMat[m][a]})</span></label>`;
      }).join("")).join("");
      f.querySelector("#t-assuntos div").innerHTML = html || '<p class="legenda">As matérias marcadas ainda não têm assuntos cadastrados.</p>';
    }
    f.querySelectorAll("[name=mat]").forEach(c => c.addEventListener("change", atualizarAssuntos));
    atualizarAssuntos();
    f.addEventListener("submit", e => {
      e.preventDefault();
      const m = [...f.querySelectorAll("[name=mat]:checked")].map(x => x.value);
      if (!m.length) return dizer("Escolha ao menos uma matéria.");
      const a = [...f.querySelectorAll("[name=assunto]:checked")].map(x => x.value);
      treinoFiltrado(m, a, parseInt($("#t-qtd").value, 10), $("#t-banca").value);
    });
  }

  /* ---- Estatísticas ---- */
  function grafico(pontos) {
    if (pontos.length < 2) return "<p>O gráfico aparece depois de 2 simulados.</p>";
    const W = 600, H = 180, pad = 30;
    const x = i => pad + i * (W - 2 * pad) / (pontos.length - 1), y = v => H - pad - v / 100 * (H - 2 * pad);
    const linhas = [0, 50, 100].map(v => `<line x1="${pad}" x2="${W - pad}" y1="${y(v)}" y2="${y(v)}" stroke="var(--line)"/><text x="4" y="${y(v) + 4}" font-size="11" fill="var(--text-muted)">${v}%</text>`).join("");
    pontos = pontos.map(v => typeof v === "number" && isFinite(v) ? v : 0);   // histórico antigo sem percentual
    const pts = pontos.map((v, i) => `${x(i).toFixed(1)},${y(v).toFixed(1)}`).join(" ");
    const bolas = pontos.map((v, i) => `<circle cx="${x(i).toFixed(1)}" cy="${y(v).toFixed(1)}" r="4" fill="var(--gold)"/>`).join("");
    return `<svg class="grafico" viewBox="0 0 ${W} ${H}" role="img" aria-label="Evolução do percentual de acertos nos últimos simulados: ${pontos.join("%, ")}%">${linhas}<polyline points="${pts}" fill="none" stroke="var(--gold)" stroke-width="3"/>${bolas}</svg>`;
  }
  // Tabela de desempenho por assunto (do pior para o melhor)
  function tabelaAssuntos(est) {
    const linhas = Object.keys(est.porAssunto).map(k => est.porAssunto[k]).filter(x => x.total > 0).sort((a, b) => a.pct - b.pct || b.total - a.total);
    if (!linhas.length) return "";
    const tr = x => `<tr><th scope="row">${esc(x.assunto)}</th><td>${esc(x.materia)}</td><td>${x.pct}%</td><td>${x.acertos} de ${x.total}</td></tr>`;
    const tabela = v => `<table class="tabela tabela--larga"><caption class="versalete">Acertos por assunto, do pior para o melhor</caption><thead><tr><th scope="col">Assunto</th><th scope="col">Matéria</th><th scope="col">Acertos</th><th scope="col">Questões</th></tr></thead><tbody>${v.map(tr).join("")}</tbody></table>`;
    return `<h3>Por assunto</h3>${tabela(linhas.slice(0, 8))}` +
      (linhas.length > 8 ? `<details class="atalhos"><summary>Ver todos os ${linhas.length} assuntos</summary>${tabela(linhas)}</details>` : "");
  }
  function stats() {
    const h = Armazem.ler("historico", []), est = Registro.estatisticas(h);
    if (!h.length) { $("#stats").innerHTML = "<p>Suas estatísticas aparecem depois do primeiro simulado.</p>"; return; }
    const barras = Object.keys(est.porMateria).sort().map(m => { const v = est.porMateria[m]; return `<li><span>${esc(m)}</span><div class="progresso" role="progressbar" aria-label="Acertos em ${esc(m)}" aria-valuemin="0" aria-valuemax="100" aria-valuenow="${v.pct}"><div class="progresso__barra" style="width:${v.pct}%"></div></div><span>${v.pct}% (${v.acertos} de ${v.total})</span></li>`; }).join("");
    $("#stats").innerHTML = `<ul class="resumo-numeros"><li><strong>${est.simulados}</strong> ${est.simulados === 1 ? "simulado feito" : "simulados feitos"}</li><li><strong>${est.total}</strong> questões respondidas</li><li><strong>${est.pct}%</strong> de acertos no geral</li></ul>
      <h3>Por matéria</h3><ul class="mat-barras">${barras}</ul>${tabelaAssuntos(est)}<h3>Evolução</h3>${grafico(h.slice(0, 20).reverse().map(x => x.percentual))}`;
  }

  /* ---- Caderno de erros ---- */
  function caderno() {
    const todos = Registro.listarErros(), mats = [...new Set(todos.map(e => e.materia))].sort();
    if (!todos.length) { $("#caderno").innerHTML = "<p>Quando você errar, deixar em branco ou chutar uma questão, ela entra aqui e volta para revisão no momento certo.</p>"; return; }
    $("#caderno").innerHTML = `<div class="linha"><label for="c-status">Mostrar</label><select id="c-status" class="campo"><option value="aberta">Em aberto</option><option value="resolvida">Resolvidas</option><option value="">Todas</option></select>
      <label for="c-mat">Matéria</label><select id="c-mat" class="campo"><option value="">Todas</option>${mats.map(m => `<option>${esc(m)}</option>`).join("")}</select></div>
      <p id="c-resumo" role="status"></p><p><button class="btn btn--primary" id="b-treinar" type="button">Treinar os erros em aberto</button></p><div id="c-lista"></div>`;
    const filtrados = () => todos.filter(e => (!$("#c-status").value || e.status === $("#c-status").value) && (!$("#c-mat").value || e.materia === $("#c-mat").value));
    const motivo = { erro: "Errada", branco: "Em branco", chute: "Acerto por chute" };
    function lista() {
      const vis = filtrados();
      $("#c-resumo").textContent = vis.length + (vis.length === 1 ? " questão" : " questões");
      $("#c-lista").innerHTML = vis.map((e, k) => {
        if (!existe(e)) return `<p class="revisao">Questão de uma prova que não está disponível agora (${esc(e.provaId)}).</p>`;
        return `<details class="revisao" data-k="${k}"><summary>${esc(e.assunto || e.materia)} <span class="legenda">${e.assunto ? esc(e.materia) + ", " : ""}${(motivo[e.motivo] || e.motivo).toLowerCase()}${e.status === "resolvida" ? ", resolvida" : ""}</span></summary>
          <div class="c-corpo"><p>Carregando a questão…</p></div>
          <p class="origem">${e.status === "aberta" ? "Próxima revisão em " + dataBr(e.proxima) + "." : "Questão resolvida."} Você já tentou ${e.tentativas} ${e.tentativas === 1 ? "vez" : "vezes"}.</p>
          <p><a class="btn btn--ghost" href="questao.html?id=${encodeURIComponent(e.provaId)}&n=${e.numero}">Abrir só esta questão</a></p></details>`;
      }).join("");
      // a questão completa só é baixada quando a pessoa abre o item (economiza dados no celular)
      $("#c-lista").querySelectorAll("details[data-k]").forEach(d => d.addEventListener("toggle", () => {
        if (!d.open || d.dataset.ok) return;
        d.dataset.ok = "1";
        const e = vis[+d.dataset.k], corpo = d.querySelector(".c-corpo");
        Dados.questao(e).then(({ prova: p, q }) => {
          if (!q) { corpo.innerHTML = "<p>Esta questão não está mais na prova.</p>"; return; }
          const correta = q.gabarito === "ANULADA" ? "questão anulada pela banca" : `${q.gabarito}) ${q.alternativas[q.gabarito] ? Render.alternativa(q, q.gabarito) : ""}`;
          corpo.innerHTML = `<p class="origem">${esc(Registro.rotuloOrigem(p, q))}</p>${Render.enunciado(q)}<p><strong>Resposta correta:</strong> ${correta}</p>${Render.explicacao(q)}`;
          Formulas.renderizar(corpo);
        }).catch(() => { corpo.innerHTML = "<p>Não foi possível carregar a questão agora. Confira a internet.</p>"; delete d.dataset.ok; });
      }));
    }
    $("#c-status").addEventListener("change", lista); $("#c-mat").addEventListener("change", lista);
    $("#b-treinar").onclick = () => treinoDeEntradas(todos.filter(e => e.status === "aberta" && (!$("#c-mat").value || e.materia === $("#c-mat").value)), "Caderno de erros", 30);
    lista();
  }

  painel(); stats();
  Promise.all([Dados.indice(), Dados.lista()]).then(([ind, lista]) => {
    indice = ind; idx = new Set(ind.map(x => x.p + "#" + x.n));
    lista.forEach(p => { bancaDe[p.id] = p.banca; });
    revisao(); plano(); treinoForm(); caderno();
  }).catch(() => {
    const msg = "Não foi possível carregar as provas. Se abriu o arquivo direto, use um servidor local (veja o README).";
    dizer(msg);
    ["#revisao", "#plano", "#treino", "#caderno"].forEach(s => { $(s).innerHTML = "<p>Indisponível agora: as provas não carregaram.</p>"; });   // não deixa "Carregando…" para sempre
  });
})();
