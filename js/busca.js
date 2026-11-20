/* Treinar por assunto: ao abrir, o mapa de assuntos (uma ficha por matéria); ao tocar num assunto ou buscar uma palavra,
   o índice de matérias e assuntos ao lado e as questões em linhas, com a bolinha para pôr na lista.
   Para pesar pouco no celular, o mapa e o índice usam só data/indice-questoes.json (já guardado para uso offline).
   O resto vem por matéria e só quando precisa: data/busca/<matéria>-t.json (os trechos das linhas, ao abrir a matéria)
   e data/busca/<matéria>-p.json (as palavras, só quando alguém digita). A questão completa só é baixada quando aberta.
   A lista montada fica em "lista-montando" e vira treino ou link compartilhável. */
(function () {
  const $ = s => document.querySelector(s), E = Render.esc, N = Render.normalizar;
  const POR_PAGINA = 20, CH = "lista-montando", NO_MAPA = 5;
  let indice = [], visiveis = [], mostrados = 0, cesta = Armazem.ler(CH, []);
  let filtro = { q: "", banca: "", materia: "", assunto: "" };
  const chave = it => it.p + "#" + it.n;
  const naCesta = k => cesta.some(c => c.provaId + "#" + c.numero === k);
  const params = new URLSearchParams(location.search);
  const COR = { Enem: "ouro", FATEC: "ouro", ETEC: "caneta" };
  const nf = n => n.toLocaleString("pt-BR");
  // nome do arquivo da matéria: igual ao fatia() de tools/validar.py
  const fatia = m => N(m).replace(/[^0-9a-z]+/g, "-").replace(/^-+|-+$/g, "") || "outras";
  const pedacos = {};                                          // "matemática-t" → Promise<{ "prova#n": texto }>
  const pedaco = (m, tipo) => pedacos[fatia(m) + "-" + tipo] || (pedacos[fatia(m) + "-" + tipo] =
    Dados.json(`data/busca/${fatia(m)}-${tipo}.json`).catch(e => { delete pedacos[fatia(m) + "-" + tipo]; throw e; }));
  // garante trechos (t) ou palavras (p) das matérias destes itens; devolve quando todos chegaram
  function completar(itens, tipo) {
    const mats = [...new Set(itens.filter(it => tipo === "t" ? it.e === undefined : it.w === undefined).map(it => it.m))];
    return Promise.all(mats.map(m => pedaco(m, tipo).then(d => {
      itens.forEach(it => { if (it.m === m) { const v = d[chave(it)] || ""; if (tipo === "t") it.e = v; else it.w = v; } });
    })));
  }
  let vez = 0;                                                 // descarta respostas de buscas antigas

  // contagens para o mapa e o índice, sempre respeitando o vestibular escolhido
  function contar() {
    const porMat = {};
    indice.forEach(it => {
      if (filtro.banca && it.b !== filtro.banca) return;
      const m = porMat[it.m] || (porMat[it.m] = { n: 0, as: {} });
      m.n++; if (it.a) m.as[it.a] = (m.as[it.a] || 0) + 1;
    });
    return porMat;
  }
  const ordenarAs = as => Object.keys(as).sort((a, b) => as[b] - as[a] || a.localeCompare(b));

  /* ---- Mapa de assuntos ---- */
  function mapa() {
    const pm = contar(), mats = Object.keys(pm).sort((a, b) => pm[b].n - pm[a].n);
    $("#mapa-n").textContent = `${mats.length} matérias · toque num assunto`;
    $("#mapa-mats").innerHTML = mats.map(m => {
      const as = ordenarAs(pm[m].as), resto = as.length - NO_MAPA;
      const pil = (a, oculto) => `<a class="area" href="?materia=${encodeURIComponent(m)}&assunto=${encodeURIComponent(a)}" data-m="${E(m)}" data-a="${E(a)}"${oculto ? " hidden" : ""}>${E(a)}</a>`;
      return `<article class="mapa-mat"><div class="mapa-mat__topo"><h3><a href="?materia=${encodeURIComponent(m)}" data-m="${E(m)}">${E(m)}</a></h3><span>${nf(pm[m].n)} questões</span></div>
        <div class="mapa-mat__as">${as.map((a, i) => pil(a, i >= NO_MAPA)).join("")}</div>
        ${resto > 0 ? `<button type="button" class="btn-link mapa-mat__mais" aria-expanded="false">+ ${resto} ${resto === 1 ? "assunto" : "assuntos"}</button>` : ""}</article>`;
    }).join("") || "<p>Nenhuma questão para este vestibular.</p>";
    $("#mapa-mats").querySelectorAll(".mapa-mat__mais").forEach(b => b.onclick = () => {
      const abrir = b.getAttribute("aria-expanded") !== "true";
      b.closest(".mapa-mat").querySelectorAll(".area").forEach((a, i) => { if (i >= NO_MAPA) a.hidden = !abrir; });
      b.setAttribute("aria-expanded", abrir);
      b.textContent = abrir ? "Mostrar menos" : b.dataset.rot || b.textContent;
    });
    $("#mapa-mats").querySelectorAll(".mapa-mat__mais").forEach(b => { b.dataset.rot = b.textContent; });
    $("#mapa-mats").querySelectorAll("[data-m]").forEach(a => a.addEventListener("click", ev => {
      ev.preventDefault(); escolher(a.dataset.m, a.dataset.a || "");
    }));
  }

  /* ---- Índice ao lado dos resultados ---- */
  function indiceLado() {
    const pm = contar(), mats = Object.keys(pm).sort();
    $("#b-indice").innerHTML = `<button type="button" class="btn-link indice-assuntos__voltar" id="b-voltar">‹ Voltar ao mapa</button><p class="rotulo">Índice</p><ul>${mats.map(m => {
      const aberta = m === filtro.materia;
      const sub = aberta ? `<ul>${ordenarAs(pm[m].as).map(a => `<li><a href="#" data-m="${E(m)}" data-a="${E(a)}"${a === filtro.assunto ? ' aria-current="true"' : ""}><span>${E(a)}</span><span>${pm[m].as[a]}</span></a></li>`).join("")}</ul>` : "";
      return `<li class="${aberta ? "aberta" : ""}"><a href="#" data-m="${E(m)}" data-a=""${aberta && !filtro.assunto ? ' aria-current="true"' : ""}><span>${E(m)}</span><span>${pm[m].n}</span></a>${sub}</li>`;
    }).join("")}</ul>`;
    $("#b-indice").querySelectorAll("[data-m]").forEach(a => a.addEventListener("click", ev => { ev.preventDefault(); escolher(a.dataset.m, a.dataset.a); }));
    $("#b-voltar").onclick = () => { filtro.q = ""; filtro.materia = ""; filtro.assunto = ""; $("#b-texto").value = ""; aplicar(); $("#titulo").scrollIntoView({ behavior: "smooth" }); };
  }

  function escolher(m, a) {
    filtro.materia = m || ""; filtro.assunto = a || "";
    aplicar();
    const alvo = $("#resultados"); if (alvo && !alvo.hidden) alvo.scrollIntoView({ behavior: "smooth", block: "start" });
  }

  /* ---- Filtrar e mostrar ---- */
  function aplicar() {
    const termos = N(filtro.q).split(/[^0-9a-z]+/).filter(t => t.length > 1);
    const buscando = termos.length || filtro.materia || filtro.assunto;
    // guarda a busca no endereço (dá para mandar o link da busca)
    const u = new URLSearchParams();
    if (filtro.q.trim()) u.set("q", filtro.q.trim());
    if (filtro.banca) u.set("banca", filtro.banca); if (filtro.materia) u.set("materia", filtro.materia); if (filtro.assunto) u.set("assunto", filtro.assunto);
    history.replaceState(null, "", location.pathname + (u.toString() ? "?" + u : ""));
    document.querySelectorAll("#b-bancas button").forEach(b => b.setAttribute("aria-pressed", b.dataset.banca === filtro.banca));
    $("#mapa").hidden = !!buscando; $("#resultados").hidden = !buscando;
    if (!buscando) { mapa(); return; }
    const minha = ++vez;
    const base = indice.filter(it => (!filtro.banca || it.b === filtro.banca) && (!filtro.materia || it.m === filtro.materia)
      && (!filtro.assunto || it.a === filtro.assunto));
    const falta = termos.length && base.some(it => it.w === undefined);
    if (falta) {
      $("#b-contagem").textContent = "Procurando nas questões…";
      $("#b-lista").innerHTML = ""; $("#b-mais").hidden = true;
    }
    (termos.length ? completar(base, "p") : Promise.resolve()).then(() => {
      if (minha !== vez) return;
      mostrar(termos, base.filter(it => termos.every(t => it.w.includes(t))));
    }).catch(() => { if (minha === vez) $("#b-contagem").textContent = "Não foi possível buscar agora. Confira a internet e tente de novo."; });
  }
  function mostrar(termos, lista) {
    visiveis = lista;
    $("#res-t").innerHTML = filtro.assunto ? `${E(filtro.assunto)}${termos.length ? ` <em>· “${E(filtro.q.trim())}”</em>` : ""}`
      : filtro.materia ? `${E(filtro.materia)}${termos.length ? ` <em>· “${E(filtro.q.trim())}”</em>` : ""}` : `<em>“${E(filtro.q.trim())}”</em>`;
    $("#b-contagem").textContent = visiveis.length + (visiveis.length === 1 ? " questão encontrada" : " questões encontradas");
    const chip = (rot, campo) => `<span class="filtro-chip">${E(rot)}<button type="button" data-tira="${campo}" aria-label="Tirar o filtro ${E(rot)}">×</button></span>`;
    const nomeTreino = filtro.assunto || filtro.materia || filtro.q.trim();
    $("#b-chips").innerHTML = `<button type="button" class="btn busca__voltar" id="b-voltar2">‹ Mapa</button>` + (filtro.materia ? chip(filtro.assunto ? `${filtro.materia} · ${filtro.assunto}` : filtro.materia, filtro.assunto ? "assunto" : "materia") : "")
      + (termos.length ? chip(`“${filtro.q.trim()}”`, "q") : "")
      + (filtro.banca ? chip(filtro.banca, "banca") : "")
      + (visiveis.length ? `<span class="busca__acoes"><button type="button" class="btn" id="b-marcar">${visiveis.length > 50 ? "Marcar as 20 primeiras" : `Marcar as ${visiveis.length}`}</button>
        <button type="button" class="btn btn--primary" id="b-treinar10">Treinar ${Math.min(10, visiveis.length)} de ${E(nomeTreino)}</button></span>` : "");
    $("#b-chips").querySelectorAll("[data-tira]").forEach(b => b.onclick = () => {
      const c = b.dataset.tira;
      if (c === "q") { filtro.q = ""; $("#b-texto").value = ""; } else if (c === "materia") { filtro.materia = ""; filtro.assunto = ""; } else filtro[c] = "";
      aplicar();
    });
    const bm = $("#b-marcar");
    if (bm) bm.onclick = () => {
      visiveis.slice(0, visiveis.length > 50 ? 20 : visiveis.length).forEach(it => { const k = chave(it); if (!naCesta(k)) cesta.push({ provaId: it.p, numero: +it.n }); });
      Armazem.gravar(CH, cesta); mostrarCesta();
      document.querySelectorAll("#b-lista input[data-k]").forEach(c => { c.checked = naCesta(c.dataset.k); marcarLinha(c); });
    };
    const bt = $("#b-treinar10");
    if (bt) bt.onclick = () => treinar(Treino.embaralhar(visiveis).slice(0, 10).map(it => ({ provaId: it.p, numero: +it.n })), `Treino: ${nomeTreino}`, bt);
    indiceLado();
    $("#b-voltar2").onclick = () => $("#b-voltar").click();
    $("#b-lista").innerHTML = ""; mostrados = 0; mais();
  }

  function marcarLinha(c) { const li = c.closest(".res"); if (li) li.classList.toggle("res--na-lista", c.checked); }
  function mais() {
    const lote = visiveis.slice(mostrados, mostrados + POR_PAGINA), minha = vez;
    $("#b-mais").disabled = true;
    completar(lote, "t").catch(() => {}).then(() => { if (minha === vez) desenhar(lote); $("#b-mais").disabled = false; });
  }
  function desenhar(lote) {
    const tmp = document.createElement("ol");
    tmp.innerHTML = lote.map(it => {
      const k = chave(it);
      return `<li class="res${naCesta(k) ? " res--na-lista" : ""}">
        <label class="res__marca"><input type="checkbox" data-k="${E(k)}"${naCesta(k) ? " checked" : ""}><span class="sr">Incluir na lista: ${E(it.r)}</span></label>
        <div class="res__txt">
          <p class="res__topo"><span class="res__banca res__banca--${COR[it.b] || "caneta"}">${E(it.b)}</span> <strong>${E(it.r.replace(/^(Vestibulinho |Vestibular )/, ""))}</strong>${it.a ? ` <span class="res__assunto">${E(it.a)}</span>` : ` <span class="res__assunto">${E(it.m)}</span>`}</p>
          <p class="res__trecho">${it.e ? E(it.e) : "Abra a questão para ler o enunciado."}</p>
          <details data-k="${E(k)}"><summary>Ver a questão inteira</summary><div class="res__corpo"><p>Carregando…</p></div></details>
          <p class="res__acoes"><a href="questao.html?id=${encodeURIComponent(it.p)}&n=${it.n}">Responder agora</a></p>
        </div>
      </li>`;
    }).join("");
    tmp.querySelectorAll("details[data-k]").forEach(d => d.addEventListener("toggle", () => {
      if (!d.open || d.dataset.ok) return;
      d.dataset.ok = "1";
      const [provaId, n] = d.dataset.k.split("#"), corpo = d.querySelector(".res__corpo");
      Dados.questao({ provaId: provaId, numero: +n }).then(({ q }) => {
        if (!q) { corpo.innerHTML = "<p>Questão não encontrada.</p>"; return; }
        corpo.innerHTML = `${Render.enunciado(q)}${Render.alternativas(q, "")}
          <details><summary>Ver resposta e explicação</summary><p><strong>Resposta:</strong> ${q.gabarito === "ANULADA" ? "questão anulada" : E(q.gabarito)}</p>${Render.explicacao(q)}</details>`;
        Formulas.renderizar(corpo);
      }).catch(() => { corpo.innerHTML = "<p>Não foi possível carregar agora. Confira a internet.</p>"; delete d.dataset.ok; });
    }));
    tmp.querySelectorAll("input[data-k]").forEach(c => c.addEventListener("change", () => {
      const [provaId, n] = c.dataset.k.split("#");
      cesta = cesta.filter(x => x.provaId + "#" + x.numero !== c.dataset.k);
      if (c.checked) cesta.push({ provaId: provaId, numero: +n });
      Armazem.gravar(CH, cesta); mostrarCesta(); marcarLinha(c);
    }));
    const novos = [...tmp.children];
    novos.forEach(el => $("#b-lista").appendChild(el));
    novos.forEach(el => Formulas.renderizar(el.querySelector(".res__trecho")));
    if (!visiveis.length) $("#b-lista").innerHTML = '<li class="busca__vazio">Nenhuma questão com esses filtros. Tente outras palavras ou volte ao mapa.</li>';
    mostrados += lote.length;
    $("#b-mais").hidden = mostrados >= visiveis.length;
    if (!$("#b-mais").hidden) $("#b-mais").textContent = `Mostrar mais ${Math.min(POR_PAGINA, visiveis.length - mostrados)}`;
  }

  /* ---- Onde você mais erra (do caderno, neste aparelho) ---- */
  function ondeErra() {
    const est = Registro.estatisticas(Armazem.ler("historico", []));
    const fracos = Object.keys(est.porAssunto).map(k => est.porAssunto[k]).filter(x => x.total >= 3 && x.pct < 100 && x.assunto)
      .sort((a, b) => a.pct - b.pct || b.total - a.total).slice(0, 3);
    const el = $("#b-erra");
    if (!fracos.length) { el.hidden = true; return; }
    el.hidden = false;
    el.innerHTML = `<span class="rotulo">Onde você mais erra</span>${fracos.map(x => `<a class="erra__item" href="?materia=${encodeURIComponent(x.materia)}&assunto=${encodeURIComponent(x.assunto)}" data-m="${E(x.materia)}" data-a="${E(x.assunto)}">${E(x.assunto)} · ${x.pct}%</a>`).join("")}`;
    el.querySelectorAll("[data-m]").forEach(a => a.addEventListener("click", ev => { ev.preventDefault(); escolher(a.dataset.m, a.dataset.a); }));
  }

  /* ---- Sua lista ---- */
  function mostrarCesta() {
    $("#cesta").hidden = !cesta.length;
    $("#c-n").textContent = cesta.length + (cesta.length === 1 ? " questão" : " questões");
    $("#c-bolhas").innerHTML = "<i></i>".repeat(Math.min(cesta.length, 5));
  }
  function linkLista() {
    return Treino.endereco("lista.html?l=" + encodeURIComponent(Treino.codificarLista(cesta)) + "&t=" + encodeURIComponent($("#c-nome").value.trim() || "Lista de questões"));
  }
  function treinar(refs, titulo, botao) {
    const st = $("#c-status"); if (st) st.textContent = "Montando o treino…";
    if (botao) botao.disabled = true;
    Dados.provas(refs.map(c => c.provaId)).then(ps => {
      const itens = refs.map(c => ps[c.provaId] && { prova: ps[c.provaId], q: ps[c.provaId].questoes.find(q => q.numero === c.numero) }).filter(x => x && x.q);
      if (itens.length) location.href = Treino.montar(titulo, itens);
      else { if (st) st.textContent = "Não foi possível carregar as questões agora."; if (botao) botao.disabled = false; }
    }).catch(() => { if (st) st.textContent = "Não foi possível carregar as questões agora."; if (botao) botao.disabled = false; });
  }

  $("#b-mais").addEventListener("click", mais);
  let timer = null;
  $("#b-texto").addEventListener("input", () => { clearTimeout(timer); timer = setTimeout(() => { filtro.q = $("#b-texto").value; aplicar(); }, 250); });
  document.querySelectorAll("#b-bancas button").forEach(b => b.addEventListener("click", () => { filtro.banca = b.dataset.banca; filtro.assunto = filtro.assunto && contar()[filtro.materia] && contar()[filtro.materia].as[filtro.assunto] ? filtro.assunto : ""; aplicar(); }));
  $("#c-limpar").addEventListener("click", () => {
    cesta = []; Armazem.gravar(CH, cesta); mostrarCesta();
    document.querySelectorAll("input[data-k]").forEach(c => { c.checked = false; marcarLinha(c); });
  });
  $("#c-treinar").addEventListener("click", () => treinar(cesta, $("#c-nome").value.trim() || "Lista de questões", $("#c-treinar")));
  $("#c-link").addEventListener("click", () => {
    const url = linkLista();
    Registro.copiar(url).then(ok => { $("#c-status").textContent = ok ? "Link copiado. Quem abrir pode treinar com estas questões." : "Não foi possível copiar. Link: " + url; });
  });

  mostrarCesta(); ondeErra();
  Promise.all([Dados.indice(), Dados.lista()]).then(([ix, provas]) => {
    const pp = {}; provas.forEach(p => { pp[p.id] = p; });
    indice = (Array.isArray(ix) ? ix : []).filter(it => pp[it.p]).map(it => {
      const p = pp[it.p];
      return Object.assign({}, it, { b: p.banca, r: `${p.titulo}${it.c ? `, caderno ${it.c}` : ""}, questão ${it.o || it.n}` });
    });
    const nm = new Set(indice.map(it => it.m)).size;
    $("#b-total").textContent = `${nf(indice.length)} questões · ${nm} matérias · todas as provas`;
    filtro = { q: params.get("q") || "", banca: params.get("banca") || "", materia: params.get("materia") || "", assunto: params.get("assunto") || "" };
    if (!["", "Enem", "ETEC", "FATEC"].includes(filtro.banca)) filtro.banca = "";
    $("#b-texto").value = filtro.q;
    aplicar();
  }).catch(() => { $("#mapa-mats").innerHTML = "<p>Não foi possível carregar a busca. Se abriu o arquivo direto, use um servidor local (veja o README).</p>"; });
})();
