/* Seleção de provas: todas as edições por ano (inclusive as que não tiveram prova), filtro por banca e ano,
   andamento de cada prova e opção de guardar a prova para usar sem internet. */
(function () {
  const $ = s => document.querySelector(s), E = Render.esc;
  const params = new URLSearchParams(location.search);
  const lista = $("#lista"), contagem = $("#contagem"), fAno = $("#f-ano"), fNao = $("#f-nao"), indice = $("#indice");
  const CACHE_DADOS = "treineiros-dados";           // o mesmo nome do sw.js: provas guardadas para uso offline
  let edicoes = [], disponiveis = {}, banca = "";
  const BANCAS = { ETEC: "Vestibulinho ETEC", FATEC: "Vestibular FATEC" };

  // Junta as edições (edicoes.json) com as provas que já estão no site (provas.json)
  function montarLista(eds, provas) {
    provas.forEach(p => { disponiveis[p.id] = p; });
    const vistas = new Set(eds.map(e => e.id));
    provas.filter(p => !vistas.has(p.id)).forEach(p => eds.push({ id: p.id, banca: p.banca, ano: p.ano, semestre: p.semestre, area: p.area, dataExame: p.dataExame }));
    return eds.map(e => Object.assign({}, e, { prova: disponiveis[e.id] || null }))
      .sort((a, b) => b.ano - a.ano || (b.semestre || 0) - (a.semestre || 0) || a.banca.localeCompare(b.banca));
  }

  // Situação de uma prova neste aparelho: em andamento, feita ou nova
  function situacao(p) {
    const and = Armazem.ler("andamento:" + p.id, null);
    if (and && and.respostas) {
      const feitas = Object.keys(and.respostas).length;
      return { tipo: "andando", texto: `Na questão ${Math.min(feitas + 1, p.totalQuestoes)} de ${p.totalQuestoes}`, curto: `${feitas}/${p.totalQuestoes}` };
    }
    const res = Armazem.ler("resultado:" + p.id, null);
    if (res && res.respostas) {
      const h = Armazem.ler("historico", []).find(x => x.provaId === p.id);
      return { tipo: "feita", texto: h ? `Feita: ${h.acertos} de ${h.total}` : "Você já fez", curto: h ? `${h.acertos}/${h.total}` : "feita" };
    }
    return null;
  }
  const bolha = sit => `<span class="ed__bolha${sit ? " ed__bolha--" + sit.tipo : ""}" aria-hidden="true">${sit && sit.tipo === "feita" ? "✓" : ""}</span>`;
  const BANCA_LONGA = { ETEC: "Vestibulinho ETEC", FATEC: "Vestibular FATEC", Enem: "Enem" };

  // Uma linha da folha: bolinha de situação, nome, tempo e o botão da ação
  function linha(e) {
    const sem = e.semestre ? `${e.semestre}º semestre` : e.area || "";
    const nome = `${BANCAS[e.banca] || e.banca}${sem ? ", " + sem : ""}`;
    const data = e.dataExame ? `Prova de ${Render.dataBr(e.dataExame)}` : "";
    const p = e.prova;
    if (!p) {
      const tipo = e.status === "sem-prova" ? "sem-prova" : "em-breve";
      const rot = e.status === "sem-prova" ? "Sem prova (pandemia)" : e.status === "em-breve" ? "Em breve" : "Em preparação";
      return `<li class="ed ed--mini ed--${tipo}" data-banca="${E(e.banca)}" aria-label="${E(nome)}, ${e.ano}: ${rot}">
        <span class="ed__bolha ed__bolha--vazia" aria-hidden="true"></span>
        <div class="ed__txt"><p class="ed__banca">${E(BANCA_LONGA[e.banca] || e.banca)}</p><h3 class="ed__nome">${E(sem || String(e.ano))}</h3>${data ? `<p class="ed__meta">${data}</p>` : ""}</div>
        <p class="ed__sit ed__sit--${tipo}">${rot}</p></li>`;
    }
    const sit = situacao(p);
    let meta = `${p.totalQuestoes} questões${p.banca === "FATEC" ? " e redação" : ""} · ${Motor.duracaoTexto(p.duracaoMinutos)}`;
    if (p.anuladas) meta += ` · ${p.anuladas} ${p.anuladas === 1 ? "anulada" : "anuladas"}`;
    const acao = sit && sit.tipo === "andando" ? "Continuar" : sit ? "Fazer de novo" : "Começar";
    return `<li class="ed ed--ok" data-banca="${E(p.banca)}">
      ${bolha(sit)}
      <div class="ed__txt"><p class="ed__banca">${E(BANCA_LONGA[p.banca] || p.banca)}${p.revisadas === p.totalQuestoes ? ' <span class="ed__estado">· questões revisadas</span>' : ""}</p>
        <h3 class="ed__nome">${E(sem || String(p.ano))}</h3><p class="ed__meta">${meta}${data ? ` · ${data}` : ""}</p></div>
      <p class="ed__sit ed__sit--${sit ? sit.tipo : "nova"}">${sit ? E(sit.texto) : "Não começou"}</p>
      <p class="ed__acoes">${sit && sit.tipo === "feita" ? `<a class="btn" href="resultado.html?id=${encodeURIComponent(p.id)}">Ver resultado<span class="sr"> ${E(nome)} ${p.ano}</span></a>` : ""}
        <a class="btn${sit && sit.tipo === "andando" ? " btn--primary" : ""}" href="simulado.html?id=${encodeURIComponent(p.id)}">${acao}<span class="sr"> ${E(nome)} ${p.ano}</span></a>
        <button type="button" class="btn btn--ghost ed__off" data-off="${E(p.id)}" hidden>Guardar para usar sem internet</button></p>
    </li>`;
  }

  // Enem com escolha de língua: Inglês e Espanhol viram uma pílula só, "Linguagens"; a língua se escolhe na abertura do simulado.
  // A pílula mostra a versão em andamento (ou a já feita) e, sem nenhuma, abre a última língua escolhida.
  function juntarLinguas(areas) {
    const ing = areas.find(e => /-linguagens-ingles$/.test(e.prova.id)), esp = areas.find(e => /-linguagens-espanhol$/.test(e.prova.id));
    if (!ing || !esp) return areas;
    const base = ing.prova.id.replace(/-ingles$/, ""), pref = (Armazem.ler("prefs", {}).lingua) || "ingles";
    const versoes = ["ingles", "espanhol", "ambas"].map(l => {
      const p = l === "ingles" ? ing.prova : l === "espanhol" ? esp.prova : Object.assign({}, ing.prova, { id: base + "-ambas", totalQuestoes: ing.prova.totalQuestoes + 5 });
      return { l, p, sit: situacao(p) };
    });
    const v = versoes.find(x => x.sit && x.sit.tipo === "andando") || versoes.find(x => x.l === pref && x.sit) || versoes.find(x => x.sit) || versoes.find(x => x.l === pref) || versoes[0];
    const junta = Object.assign({}, ing, { area: "Linguagens", prova: v.p, lingua: v.sit ? Linguas.NOMES[v.l] : "" });
    return areas.filter(e => e !== ing && e !== esp).concat(junta);
  }

  // Enem: uma linha por ano, com as áreas em pílulas (cada área é uma prova)
  function linhaEnem(ano, eds) {
    const ORDEM = ["Linguagens", "Linguagens (Inglês)", "Linguagens (Espanhol)", "Ciências Humanas", "Ciências da Natureza", "Matemática"];
    const pos = e => { const i = ORDEM.indexOf(e.area); return i < 0 ? 99 : i; };
    const areas = juntarLinguas(eds.filter(e => e.prova)).sort((a, b) => pos(a) - pos(b));
    if (!areas.length) return eds.map(linha).join("");
    const sits = areas.map(e => situacao(e.prova));
    const geral = sits.some(x => x && x.tipo === "andando") ? { tipo: "andando" } : sits.every(x => x && x.tipo === "feita") ? { tipo: "feita" } : null;
    const p0 = (areas.find(e => e.area !== "Linguagens") || areas[0]).prova;   // a contagem de questões não depende da língua escolhida
    const modelo = ano >= 2009 ? `2 dias · ${areas.length} provas · ${p0.totalQuestoes} questões cada` : `${p0.totalQuestoes} questões · ${Motor.duracaoTexto(p0.duracaoMinutos)}`;
    return `<li class="ed ed--ok ed--enem" data-banca="Enem">
      ${bolha(geral)}
      <div class="ed__txt"><p class="ed__banca">Enem</p><h3 class="ed__nome">Enem ${ano}</h3><p class="ed__meta">${modelo}${areas.length > 1 ? " · escolha uma:" : ""}</p>
        <ul class="ed__areas">${areas.map((e, i) => {
          const s = sits[i], rot = e.area || "Prova completa";
          return `<li><a class="area${s ? " area--" + s.tipo : ""}" href="${s && s.tipo === "feita" ? "resultado" : "simulado"}.html?id=${encodeURIComponent(e.prova.id)}">${E(rot)}${s ? ` <span class="area__sit">· ${e.lingua ? E(e.lingua) + " " : ""}${s.tipo === "feita" ? "✓ " : ""}${E(s.curto)}</span>` : ""}</a></li>`;
        }).join("")}</ul></div>
    </li>`;
  }

  function render() {
    const ano = fAno.value, nao = fNao.checked;
    const vis = edicoes.filter(e => (!banca || e.banca === banca) && (!ano || String(e.ano) === ano) && (!nao || (e.prova && !situacao(e.prova))));
    const porAno = {};
    vis.forEach(e => { (porAno[e.ano] = porAno[e.ano] || []).push(e); });
    const anos = Object.keys(porAno).sort((a, b) => b - a);
    const prep = vis.some(e => !e.prova && !e.status)
      ? '<p class="ano__nota">Provas “em preparação” estão sendo digitadas para o site, com questões, figuras e explicações conferidas uma a uma.</p>' : "";
    lista.innerHTML = prep + (anos.map(a => {
      const eds = porAno[a], enem = eds.filter(e => e.banca === "Enem"), outras = eds.filter(e => e.banca !== "Enem");
      const n = eds.filter(e => e.prova).length;
      return `<section class="ano" id="ano-${a}" aria-labelledby="ano-t-${a}"><div class="titulo-linha"><h2 id="ano-t-${a}">${a}</h2><span class="titulo-linha__extra">${n ? n + (n === 1 ? " prova" : " provas") : "sem prova no site"}</span></div>${notaAno(+a, eds)}
        <ol class="ano__lista">${(enem.length ? linhaEnem(+a, enem) : "") + outras.map(linha).join("")}</ol></section>`;
    }).join("") || '<p class="vazio">Nenhuma prova com esses filtros.</p>');
    const n = vis.filter(e => e.prova).length;
    contagem.textContent = n + (n === 1 ? " prova" : " provas") + (vis.length > n ? `, mais ${vis.length - n} sem prova ou em breve` : "") + ".";
    // índice lateral: um link por ano, com quantas provas tem
    indice.hidden = anos.length < 2;
    indice.innerHTML = `<p class="rotulo">Índice</p><ol>${anos.map(a => {
      const k = porAno[a].filter(e => e.prova).length;
      return `<li><a href="#ano-${a}"><span>${a}</span><span class="indice__n">${k}</span></a></li>`;
    }).join("")}</ol>`;
    marcarIndice();
    ligarOffline();
  }
  // Índice: o ano que está na tela fica marcado
  let obs = null;
  function marcarIndice() {
    if (obs) obs.disconnect();
    const links = [...indice.querySelectorAll("a")];
    const marcar = id => links.forEach(a => { const on = a.getAttribute("href") === "#" + id; a.classList.toggle("atual", on); if (on) a.setAttribute("aria-current", "true"); else a.removeAttribute("aria-current"); });
    if (links[0]) marcar(links[0].getAttribute("href").slice(1));
    if (!("IntersectionObserver" in window)) return;
    obs = new IntersectionObserver(ents => { const v = ents.filter(x => x.isIntersecting).sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top)[0]; if (v) marcar(v.target.id); },
      { rootMargin: "-20% 0px -70% 0px" });
    lista.querySelectorAll(".ano").forEach(sec => obs.observe(sec));
  }
  // 2021: nenhum semestre teve prova. Avisa uma vez, no topo do ano, em vez de repetir em cada cartão.
  function notaAno(ano, eds) {
    const cps = eds.filter(e => e.banca !== "Enem");     // a nota da pandemia é sobre ETEC e FATEC (o Enem de 2021 aconteceu)
    const sem = cps.filter(e => !e.prova && e.status === "sem-prova"), breve = eds.filter(e => !e.prova && e.status === "em-breve");
    const notas = [];
    if (sem.length && sem.length === cps.length) notas.push(`Em ${ano} não houve prova da ETEC nem da FATEC em nenhum semestre: por causa da pandemia de covid-19, o Centro Paula Souza selecionou os candidatos pela análise do histórico escolar.`);
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
  fAno.addEventListener("change", render); fNao.addEventListener("change", render);

  Promise.all([Dados.edicoes(), Dados.lista()]).then(([eds, provas]) => {
    edicoes = montarLista(eds, provas);
    const anos = [...new Set(edicoes.map(e => e.ano))].sort((a, b) => b - a);
    const total = edicoes.filter(e => e.prova).length;
    const sob = document.getElementById("provas-total"); if (sob) sob.textContent = `${total} provas oficiais · de ${anos[anos.length - 1]} a ${anos[0]}`;
    fAno.innerHTML = '<option value="">Todos os anos</option>' + anos.map(a => `<option>${a}</option>`).join("");
    const anoPedido = params.get("ano"); if (anoPedido && anos.includes(Number(anoPedido))) fAno.value = anoPedido;   // vindo da página inicial
    const b = (params.get("banca") || "").toLowerCase();
    banca = { etec: "ETEC", fatec: "FATEC", enem: "Enem" }[b] || "";
    marcarChip(); render();
  }).catch(() => { lista.innerHTML = '<p class="vazio">Não foi possível carregar a lista de provas. Se abriu o arquivo direto, use um servidor local (veja o README).</p>'; });
})();
