/* Resultado: pontuação, tempo por questão, revisão com anotações, compartilhar e imprimir. */
(function () {
  const params = new URLSearchParams(location.search);
  const ID = params.get("id"), ERR = params.get("modo") === "erradas", SUF = ERR ? ":erradas" : "";
  const app = document.getElementById("app");
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const vazio = msg => { app.innerHTML = `<h1>Resultado</h1><p>${esc(msg)}</p><p><a class="btn" href="provas.html">Escolher uma prova</a></p>`; };
  const salvo = ID ? Armazem.ler("resultado:" + ID + SUF, null) : null;
  if (!salvo) return vazio("Nenhum resultado encontrado para esta prova.");
  let estado = null;

  function obterProva() {
    if (ID === "treino") {
      const t = Armazem.ler("treino-ativo", null);
      return t ? Promise.resolve(t) : Promise.reject(new Error("sem treino"));
    }
    return fetch("data/provas.json").then(r => { if (!r.ok) throw 0; return r.json(); }).then(lista => {
      const item = Array.isArray(lista) && lista.find(p => p.id === ID);
      if (!item) throw new Error("nao-encontrada");
      return fetch(item.arquivo).then(r => { if (!r.ok) throw 0; return r.json(); });
    });
  }
  obterProva().then(prova => {
    if (!prova || !Array.isArray(prova.questoes)) throw 0;
    if (Array.isArray(salvo.numeros)) prova.questoes = prova.questoes.filter(q => salvo.numeros.includes(q.numero));
    estado = Motor.normalizarEstado(salvo, prova);            // resultado salvo por versão antiga
    if (!estado) return vazio("Este resultado não corresponde mais às questões da prova. Refaça o simulado.");
    mostrar(prova);
  }).catch(e => (console.error(e), vazio(e && e.message === "nao-encontrada" ? "A prova deste resultado não está mais disponível."
    : ID === "treino" ? "Este treino não está mais salvo neste navegador." : "Não foi possível carregar a prova.")));

  /* ---- Pontuação no formato de cada vestibular ---- */
  function formatoOficial(prova, r) {
    if (prova.treino) return "";
    if (prova.banca === "Enem") return blocoTRI(prova);
    const cfg = Config.pontuacao[prova.banca];
    if (!cfg) return "";
    if (!cfg.acrescimos.length) return `<section class="oficial" aria-labelledby="h-of"><h2 id="h-of">No formato ${esc(prova.banca)}</h2><p>${esc(cfg.descricao)}</p><p>Parte objetiva: <strong>${r.acertos}</strong> de ${r.total} acertos.</p></section>`;
    const perfil = Armazem.ler("perfil", {});
    return `<section class="oficial" aria-labelledby="h-of"><h2 id="h-of">No formato ${esc(prova.banca)}</h2><p>${esc(cfg.descricao)}${ERR ? " (aqui, só nas questões refeitas)" : ""}</p>
      <p>Pontuação: <strong>${r.acertos}</strong> ${r.acertos === 1 ? "ponto" : "pontos"}.</p>
      <fieldset class="oficial__acr"><legend>Pontuação acrescida</legend>${cfg.acrescimos.map(a => `<label class="chk"><input type="checkbox" data-acr="${esc(a.id)}"${perfil[a.id] ? " checked" : ""}> ${esc(a.rotulo)} (+${a.percentual}%)</label>`).join("<br>")}</fieldset>
      <p id="of-total" role="status"></p><p class="legenda">O cálculo segue o Manual do Candidato; confira as regras do seu ano no site oficial.</p></section>`;
  }
  function ligarFormatoOficial(prova, r) {
    const cfg = Config.pontuacao[prova.banca], tot = document.getElementById("of-total");
    if (!cfg || !tot) return;
    const atualizar = () => {
      const perfil = {}; let pct = 0;
      app.querySelectorAll("[data-acr]").forEach(c => { perfil[c.dataset.acr] = c.checked; if (c.checked) pct += cfg.acrescimos.find(a => a.id === c.dataset.acr).percentual; });
      Armazem.gravar("perfil", perfil);
      tot.textContent = pct ? `Com a pontuação acrescida (+${pct}%): ${String(Motor.comAcrescimo(r.acertos, pct)).replace(".", ",")} pontos.` : "";
    };
    app.querySelectorAll("[data-acr]").forEach(c => c.addEventListener("change", atualizar));
    atualizar();
  }
  // Enem: estimativa TRI por área, se a prova tiver os parâmetros de todas as questões daquela área
  function blocoTRI(prova) {
    const explica = "No Enem oficial, a nota não é o percentual de acertos: ela usa a TRI (Teoria de Resposta ao Item), que considera a dificuldade das questões e a coerência das respostas.";
    if (ERR) return `<p class="aviso">${explica} Ao refazer só as erradas não dá para estimar a nota.</p>`;
    const areas = {};
    prova.questoes.forEach(q => { (areas[q.materia] = areas[q.materia] || []).push(q); });
    const linhas = Object.keys(areas).map(m => {
      const qs = areas[m].filter(q => q.gabarito !== "ANULADA");     // o Inep não usa itens anulados no cálculo
      if (!qs.length || !qs.every(q => q.tri)) return "";
      const c = Object.assign({}, Config.tri, Config.tri.calibracao[m] || {});
      const e = Motor.estimarTRI(qs.map(q => ({ a: q.tri.a, b: q.tri.b, c: q.tri.c, acertou: estado.respostas[q.numero] === q.gabarito })), c);
      return e ? `<tr><th scope="row">${esc(m)}</th><td>${qs.filter(q => estado.respostas[q.numero] === q.gabarito).length} de ${qs.length}</td><td><strong>${e.nota}</strong></td></tr>` : "";
    }).join("");
    if (!linhas) return `<p class="aviso">${explica} Use este resultado como referência de estudo, não como nota.</p>`;
    return `<section class="oficial" aria-labelledby="h-of"><h2 id="h-of">Nota estimada (TRI)</h2>
      <table class="tabela"><caption class="versalete">Estimativa por área, com os parâmetros oficiais das questões</caption>
      <thead><tr><th scope="col">Área</th><th scope="col">Acertos</th><th scope="col">Nota estimada</th></tr></thead><tbody>${linhas}</tbody></table>
      <p class="aviso">${explica} Esta estimativa usa os parâmetros publicados pelo Inep, mas o cálculo oficial tem detalhes que não são públicos: a nota real pode variar algumas dezenas de pontos.</p></section>`;
  }

  function mostrar(prova) {
    document.title = "Resultado | Treineiros";
    const r = Motor.pontuar(estado, prova), id = encodeURIComponent(ID), chutes = estado.chutes || [], tempos = estado.tempos || {};
    const chutesOk = prova.questoes.filter(q => chutes.includes(q.numero) && q.gabarito !== "ANULADA" && estado.respostas[q.numero] === q.gabarito);
    const itens = r.revisar.map(x => ({ q: x.q, resposta: x.resposta })).concat(chutesOk.map(q => ({ q: q, resposta: q.gabarito, chute: true })));
    const alt = (q, l) => `${l}) ${Render.alternativa(q, l)}`;
    const linkQuestao = q => { const r = Registro.ref(prova, q); return `questao.html?id=${encodeURIComponent(r.provaId)}&n=${r.numero}`; };
    const rotulo = it => it.chute ? "Acerto por chute" : it.resposta ? "Errada" : "Em branco";
    const materias = Object.keys(r.porMateria).map(m => `<tr><th scope="row">${esc(m)}</th><td>${r.porMateria[m].acertos} de ${r.porMateria[m].total}</td></tr>`).join("");
    const lentas = prova.questoes.map(q => ({ q: q, t: tempos[q.numero] || 0 })).filter(x => x.t > 0).sort((a, b) => b.t - a.t).slice(0, 3);
    const media = prova.questoes.length ? estado.tempoGastoSeg / prova.questoes.length : 0;
    const imprimir = () => document.querySelectorAll("details").forEach(d => { d.open = true; });
    const rev = itens.map((it, i) => { const q = it.q; return `
      <details class="revisao"><summary>Questão ${q.numero}: ${rotulo(it).toLowerCase()} <span class="legenda">${esc(q.materia)}${q.assunto ? ", " + esc(q.assunto) : ""}</span></summary>
        <p class="origem">${esc(Registro.rotuloOrigem(prova, q))}</p>
        ${Render.enunciado(q)}
        ${Render.alternativas(q, q.gabarito === "ANULADA" ? "" : q.gabarito, it.resposta)}
        ${it.resposta ? "" : '<p class="legenda">Você deixou esta questão em branco.</p>'}
        ${Render.explicacao(q)}
        <p><label for="n${i}">Minhas anotações</label><br><textarea id="n${i}" class="campo" rows="3" data-i="${i}"></textarea></p>
        <p class="sem-impressao"><a class="btn btn--ghost" href="${linkQuestao(q)}">Abrir só esta questão</a> <button type="button" class="btn btn--ghost" data-rep="${i}">Reportar erro</button></p>
      </details>`; }).join("");
    const texto = `Treineiros — ${prova.titulo}: ${r.acertos} de ${r.total} (${r.percentual}%) em ${Motor.fmt(estado.tempoGastoSeg)}. ${new URL("index.html", location.href).href}`;

    app.innerHTML = `
      <h1 id="h1" tabindex="-1">Resultado</h1><p class="cfg__meta">${esc(prova.titulo)}${ERR ? " (só as erradas)" : ""}</p>
      <section class="placar" aria-label="Pontuação"><p class="placar__n">${r.acertos}<span> de ${r.total}</span></p><p>${r.percentual}% de acertos</p></section>
      ${estado.tempoRestanteSeg === 0 ? '<p class="aviso">O tempo acabou e o simulado foi encerrado automaticamente.</p>' : ""}
      <ul class="resumo-numeros">
        <li><strong>${r.erros}</strong> ${r.erros === 1 ? "errada" : "erradas"}</li>
        <li><strong>${r.brancas}</strong> em branco</li>
        <li><strong>${Motor.fmt(estado.tempoGastoSeg)}</strong> de prova</li>
        <li><strong>${Motor.fmt(media)}</strong> por questão, em média</li>
      </ul>
      ${lentas.length ? `<p>Onde você mais demorou: ${lentas.map(x => `questão ${x.q.numero} (${Motor.fmt(x.t)})`).join(", ")}.</p>` : ""}
      ${chutesOk.length ? `<p class="aviso">Você acertou ${chutesOk.length} ${chutesOk.length === 1 ? "questão" : "questões"} chutando. Elas estão na revisão abaixo, porque acerto sem segurança também merece estudo.</p>` : ""}
      ${formatoOficial(prova, r)}
      <h2>Por matéria</h2>
      <table class="tabela"><caption>Acertos por matéria</caption><tbody>${materias}</tbody></table>
      <h2>Para revisar</h2>${rev || "<p>Você acertou tudo com segurança. Parabéns!</p>"}
      <div class="nav sem-impressao">
        ${!ERR && r.revisar.length ? `<a class="btn btn--primary" href="simulado.html?id=${id}&modo=erradas">Refazer só as erradas</a>` : ""}
        <a class="btn" href="simulado.html?id=${id}">Refazer a prova inteira</a>
        <a class="btn" href="estudo.html">Meu estudo</a>
        <button type="button" class="btn" id="b-share">Compartilhar resultado</button>
        <button type="button" class="btn" id="b-print">Imprimir ou salvar em PDF</button>
      </div>
      <p id="status" role="status"></p>`;
    const status = document.getElementById("status");
    document.getElementById("h1").focus();
    document.getElementById("b-print").onclick = () => { imprimir(); window.print(); };
    document.getElementById("b-share").onclick = () => {
      if (navigator.share) navigator.share({ text: texto }).catch(() => {});
      else Registro.copiar(texto).then(ok => { status.textContent = ok ? "Resultado copiado. É só colar na conversa." : "Não foi possível copiar o resultado."; });
    };
    ligarFormatoOficial(prova, r);
    app.querySelectorAll("textarea[data-i]").forEach(t => {
      const ref = Registro.ref(prova, itens[+t.dataset.i].q);
      t.value = Registro.nota(ref);
      t.addEventListener("input", () => Registro.gravarNota(ref, t.value));
    });
    app.querySelectorAll("[data-rep]").forEach(b => b.onclick = () =>
      Reportar.abrir(prova, itens[+b.dataset.rep].q).then(res => { status.textContent = Reportar.mensagem(res); }));
    window.addEventListener("beforeprint", imprimir);   // também pelo Ctrl+P
    Formulas.renderizar(app);
  }
})();
