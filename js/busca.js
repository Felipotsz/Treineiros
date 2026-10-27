/* Busca de questões em todas as provas + montagem de lista compartilhável.
   Usa data/busca.json (palavras de cada questão, sem acento): a questão completa só é baixada quando aberta. */
(function () {
  const $ = s => document.querySelector(s), E = Render.esc, N = Render.normalizar;
  const POR_PAGINA = 20, CH = "lista-montando";
  let indice = [], visiveis = [], mostrados = 0, cesta = Armazem.ler(CH, []);
  const chave = it => it.p + "#" + it.n;
  const naCesta = k => cesta.some(c => c.provaId + "#" + c.numero === k);
  const params = new URLSearchParams(location.search);

  function opcoes(sel, valores, todos) {
    const atual = sel.value;
    sel.innerHTML = `<option value="">${todos}</option>` + valores.map(v => `<option>${E(v)}</option>`).join("");
    if (valores.includes(atual)) sel.value = atual;
  }
  function atualizarAssuntos() {
    const m = $("#b-mat").value, b = $("#b-banca").value;
    opcoes($("#b-assunto"), [...new Set(indice.filter(it => (!m || it.m === m) && (!b || it.b === b) && it.a).map(it => it.a))].sort(), "Todos");
  }
  function filtrar() {
    const termos = N($("#b-texto").value).split(/[^0-9a-z]+/).filter(t => t.length > 1);
    const b = $("#b-banca").value, m = $("#b-mat").value, a = $("#b-assunto").value;
    visiveis = indice.filter(it => (!b || it.b === b) && (!m || it.m === m) && (!a || it.a === a) && termos.every(t => it.w.includes(t)));
    // guarda a busca no endereço (dá para mandar o link da busca)
    const u = new URLSearchParams();
    if ($("#b-texto").value.trim()) u.set("q", $("#b-texto").value.trim());
    if (b) u.set("banca", b); if (m) u.set("materia", m); if (a) u.set("assunto", a);
    history.replaceState(null, "", location.pathname + (u.toString() ? "?" + u : ""));
    $("#b-contagem").textContent = visiveis.length + (visiveis.length === 1 ? " questão encontrada" : " questões encontradas");
    $("#b-lista").innerHTML = ""; mostrados = 0; mais();
  }
  function mais() {
    const lote = visiveis.slice(mostrados, mostrados + POR_PAGINA);
    const div = document.createElement("div");
    div.innerHTML = lote.map(it => {
      const k = chave(it);
      return `<article class="revisao res">
        <div class="res__topo"><strong>${E(it.r)}</strong>
          <label class="chk"><input type="checkbox" data-k="${E(k)}"${naCesta(k) ? " checked" : ""}> Incluir na lista</label></div>
        <p class="tags"><span class="tag">${E(it.m)}</span>${it.a ? ` <span class="tag">${E(it.a)}</span>` : ""}</p>
        <p class="res__trecho">${E(it.e)}</p>
        <details data-k="${E(k)}"><summary>Ver questão completa</summary><div class="res__corpo"><p>Carregando…</p></div></details>
        <div class="res__acoes"><a class="btn" href="questao.html?id=${encodeURIComponent(it.p)}&n=${it.n}">Responder esta questão</a></div>
      </article>`;
    }).join("");
    const novos = [...div.children];
    div.querySelectorAll("details[data-k]").forEach(d => d.addEventListener("toggle", () => {
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
    div.querySelectorAll("input[data-k]").forEach(c => c.addEventListener("change", () => {
      const [provaId, n] = c.dataset.k.split("#");
      cesta = cesta.filter(x => x.provaId + "#" + x.numero !== c.dataset.k);
      if (c.checked) cesta.push({ provaId: provaId, numero: +n });
      Armazem.gravar(CH, cesta); mostrarCesta();
    }));
    novos.forEach(el => $("#b-lista").appendChild(el));
    novos.forEach(el => Formulas.renderizar(el.querySelector(".res__trecho")));   // fórmulas no trecho
    if (!visiveis.length) $("#b-lista").innerHTML = "<p>Nenhuma questão com esses filtros. Tente outras palavras.</p>";
    mostrados += lote.length;
    $("#b-mais").hidden = mostrados >= visiveis.length;
  }
  function mostrarCesta() {
    $("#cesta").hidden = !cesta.length;
    $("#c-n").textContent = cesta.length + (cesta.length === 1 ? " questão" : " questões");
  }
  function linkLista() {
    return Treino.endereco("lista.html?l=" + encodeURIComponent(Treino.codificarLista(cesta)) + "&t=" + encodeURIComponent($("#c-nome").value.trim() || "Lista de questões"));
  }

  $("#b-mais").addEventListener("click", mais);
  let timer = null;
  $("#b-texto").addEventListener("input", () => { clearTimeout(timer); timer = setTimeout(filtrar, 250); });
  ["#b-banca", "#b-mat"].forEach(s => $(s).addEventListener("change", () => { atualizarAssuntos(); filtrar(); }));
  $("#b-assunto").addEventListener("change", filtrar);
  $("#c-limpar").addEventListener("click", () => {
    cesta = []; Armazem.gravar(CH, cesta); mostrarCesta();
    document.querySelectorAll("input[data-k]").forEach(c => { c.checked = false; });
  });
  $("#c-treinar").addEventListener("click", () => {
    $("#c-status").textContent = "Montando o treino…";
    Dados.provas(cesta.map(c => c.provaId)).then(ps => {
      const itens = cesta.map(c => ps[c.provaId] && { prova: ps[c.provaId], q: ps[c.provaId].questoes.find(q => q.numero === c.numero) }).filter(x => x && x.q);
      if (itens.length) location.href = Treino.montar($("#c-nome").value.trim() || "Lista de questões", itens);
      else $("#c-status").textContent = "Não foi possível carregar as questões agora.";
    });
  });
  $("#c-link").addEventListener("click", () => {
    const url = linkLista();
    Registro.copiar(url).then(ok => { $("#c-status").textContent = ok ? "Link copiado. Quem abrir pode treinar com estas questões." : "Não foi possível copiar. Link: " + url; });
  });

  mostrarCesta();
  Dados.json("data/busca.json").then(lista => {
    indice = Array.isArray(lista) ? lista : [];
    opcoes($("#b-banca"), [...new Set(indice.map(it => it.b))].sort(), "Todas");
    opcoes($("#b-mat"), [...new Set(indice.map(it => it.m))].sort(), "Todas");
    $("#b-texto").value = params.get("q") || "";
    $("#b-banca").value = params.get("banca") || ""; $("#b-mat").value = params.get("materia") || "";
    atualizarAssuntos(); $("#b-assunto").value = params.get("assunto") || "";
    filtrar();
  }).catch(() => { $("#b-lista").innerHTML = "<p>Não foi possível carregar a busca. Se abriu o arquivo direto, use um servidor local (veja o README).</p>"; });
})();
