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
      if (!item && Linguas.partes(ID) && Linguas.partes(ID).lingua === "ambas") return Linguas.compor(ID, lista);   // Enem com as duas línguas
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
  // simulado misto de uma prova só: vale a nota daquela prova; mesclado: sem nota, acertos por prova de origem
  const BANCA_ID = id => /^etec-/.test(id) ? "ETEC" : /^fatec-/.test(id) ? "FATEC" : /^enem-/.test(id) ? "Enem" : "Outras";
  const comoBanca = prova => prova.treino && Config.pontuacao[prova.misto] ? Object.assign({}, prova, { banca: prova.misto, treino: false }) : prova;
  function semNota(prova) {
    const por = {};
    prova.questoes.forEach(q => {
      if (q.gabarito === "ANULADA") return;
      const b = prova.misto === "Enem" ? q.materia : BANCA_ID(q.ref && q.ref.provaId || ""), x = por[b] || (por[b] = { a: 0, t: 0 });
      x.t++; if (estado.respostas[q.numero] === q.gabarito) x.a++;
    });
    const linhas = Object.keys(por).sort().map(b => `<tr><th scope="row">${esc(b)}</th><td>${por[b].a} de ${por[b].t}</td><td>${Math.round(por[b].a / por[b].t * 100)}%</td></tr>`).join("");
    const txt = prova.misto === "Enem"
      ? "No Enem, a nota usa a TRI, que precisa dos parâmetros de cada questão publicados pelo Inep. Eles ainda não estão no site, então este resultado mostra só os acertos."
      : "Cada prova calcula a nota de um jeito: a ETEC soma acertos, a FATEC usa peso com a redação e o Enem usa a TRI. Misturando, nenhuma dessas notas vale, então o resultado mostra os acertos por prova de origem.";
    return `<section class="oficial oficial--sem" aria-labelledby="h-of"><h2 id="h-of">Sem nota, <em>só acertos</em></h2><p>${txt}</p>
      <table class="tabela"><caption class="versalete">${prova.misto === "Enem" ? "Por matéria" : "Por prova de origem"}</caption><thead><tr><th scope="col">${prova.misto === "Enem" ? "Matéria" : "Prova"}</th><th scope="col">Acertos</th><th scope="col">%</th></tr></thead><tbody>${linhas}</tbody></table></section>`;
  }
  function formatoOficial(prova, r) {
    if (prova.treino && (prova.misto === "Mescla" || prova.misto === "Enem")) return semNota(prova);
    prova = comoBanca(prova);
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
    prova = comoBanca(prova);
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
    if (prova.composta) return `<p class="aviso">${explica} Com as duas línguas na mesma prova não dá para estimar a nota: no Enem só conta a língua escolhida. Para ter a estimativa, faça a prova com Inglês ou com Espanhol.</p>`;
    const areas = {};
    prova.questoes.forEach(q => { const k = q.area || q.materia; (areas[k] = areas[k] || []).push(q); });   // Enem: área do Inep (q.area); a matéria é a disciplina
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
    const tipo = it => it.chute ? "chute" : it.resposta ? "errada" : "branco";
    const linkQuestao = q => { const r = Registro.ref(prova, q); return `questao.html?id=${encodeURIComponent(r.provaId)}&n=${r.numero}`; };
    const rotulo = it => it.chute ? "Acerto por chute" : it.resposta ? "Errada" : "Em branco";
    const lentas = prova.questoes.map(q => ({ q: q, t: tempos[q.numero] || 0 })).filter(x => x.t > 0).sort((a, b) => b.t - a.t).slice(0, 3);
    const media = prova.questoes.length ? estado.tempoGastoSeg / prova.questoes.length : 0;
    const imprimir = () => document.querySelectorAll("details").forEach(d => { d.open = true; });
    const n = { errada: itens.filter(x => tipo(x) === "errada").length, branco: r.brancas, chute: chutesOk.length };
    const nRefazer = r.revisar.length;
    const banca = prova.treino ? "" : prova.banca;
    const treinar = m => `busca.html?materia=${encodeURIComponent(m)}${banca ? "&banca=" + encodeURIComponent(banca) : ""}`;

    // Por matéria: da que mais precisa para a que menos
    const mats = Object.keys(r.porMateria).map(m => {
      const x = r.porMateria[m], pct = x.total ? Math.round(x.acertos / x.total * 100) : 0;
      return { m, ac: x.acertos, tot: x.total, pct, rev: itens.filter(it => it.q.materia === m).length };
    }).sort((a, b) => a.pct - b.pct || b.tot - a.tot);
    const nivel = p => p < 50 ? "baixo" : p < 75 ? "medio" : "alto";
    const tabela = mats.map(x => `<tr>
        <th scope="row">${esc(x.m)}</th>
        <td class="num">${x.ac} de ${x.tot}</td>
        <td><span class="aprov aprov--${nivel(x.pct)}"><span class="aprov__barra" aria-hidden="true"><span style="width:${x.pct}%"></span></span><b>${x.pct}%</b></span></td>
        <td class="acoes-mat">${x.rev ? `<button type="button" class="btn btn--ghost" data-mat="${esc(x.m)}">Rever ${x.rev === 1 ? "1 questão" : `${x.rev} questões`}</button>` : `<span class="legenda">Gabaritou</span>`}
          <a class="btn" href="${treinar(x.m)}">Treinar<span class="sr"> ${esc(x.m)}</span></a></td></tr>`).join("");

    const rev = itens.map((it, i) => { const q = it.q; return `
      <details class="revisao" data-tipo="${tipo(it)}" data-materia="${esc(q.materia)}"><summary><span class="revisao__n">${String(q.numero).padStart(2, "0")}</span> <span class="revisao__mat">${esc(q.materia)}${q.assunto ? " · " + esc(q.assunto) : ""}</span> <span class="revisao__tipo revisao__tipo--${tipo(it)}">${rotulo(it)}</span></summary>
        <p class="origem">${esc(Registro.rotuloOrigem(prova, q))}</p>
        ${Render.enunciado(q)}
        ${Render.alternativas(q, q.gabarito === "ANULADA" ? "" : q.gabarito, it.resposta)}
        ${it.resposta ? "" : '<p class="legenda">Você deixou esta questão em branco.</p>'}
        ${Render.explicacao(q)}
        <p><label for="n${i}">Minhas anotações</label><br><textarea id="n${i}" class="campo" rows="3" data-i="${i}"></textarea></p>
        <p class="sem-impressao"><a class="btn btn--ghost" href="${linkQuestao(q)}">Abrir só esta questão</a> <button type="button" class="btn btn--ghost" data-rep="${i}">Reportar erro</button></p>
      </details>`; }).join("");
    const filtro = (t, rot, qtd, on) => qtd ? `<button type="button" class="chip-f" data-f="${t}" aria-pressed="${on}">${rot} · ${qtd}</button>` : "";
    const primeiroFiltro = n.errada ? "errada" : n.branco ? "branco" : "chute";

    // O que fazer agora: três passos, com o que este resultado pede
    const piores = mats.filter(x => x.pct < 100).slice(0, 2);
    const passos = [];
    if (itens.length) passos.push({ t: `Entenda ${itens.length === 1 ? "a questão para revisar" : `as ${itens.length} questões para revisar`}`, d: "Cada uma tem o comentário de por que a certa está certa e por que as outras não estão.", a: `<a class="btn btn--claro" href="#revisar">Ver a correção</a>` });
    if (piores.length) passos.push({ t: `Treine ${piores.map(x => x.m).join(" e ")}`, d: `${piores.length > 1 ? "Foram as matérias" : "Foi a matéria"} com menos acertos: ${piores.map(x => `${x.ac} de ${x.tot}`).join(" e ")}.`, a: `<a class="btn btn--contorno-claro" href="${treinar(piores[0].m)}">Treinar ${esc(piores[0].m)}</a>` });
    const ints = Config.intervalosRevisaoDias || [1];
    if (itens.length) passos.push({ t: ints[0] === 1 ? "Volte amanhã" : `Volte em ${ints[0]} dias`, d: `As questões para revisar entram na revisão espaçada e voltam em Meu estudo depois de ${ints.join(", ").replace(/, (\d+)$/, " e $1")} dias.`, a: `<a class="faixa-link" href="estudo.html">Abrir Meu estudo</a>` });
    else passos.push({ t: "Faça outra prova", d: "Você acertou tudo com segurança. Tente uma prova de outro ano ou um simulado misto.", a: `<a class="btn btn--claro" href="provas.html">Escolher outra prova</a>` });

    const texto = `Treineiros — ${prova.titulo}: ${r.acertos} de ${r.total} (${r.percentual}%) em ${Motor.fmt(estado.tempoGastoSeg)}. ${new URL("index.html", location.href).href}`;
    const hm = seg => { const m = Math.round(seg / 60), h = Math.floor(m / 60); return h ? `${h}h${String(m % 60).padStart(2, "0")}` : `${m} min`; };
    const duracao = prova.duracaoMinutos ? ` de ${Motor.duracaoTexto(prova.duracaoMinutos)}` : "";

    app.innerHTML = `
      <section class="res-topo" aria-labelledby="h1">
        <div class="res-topo__nota">
          <p class="sobretitulo">${esc(prova.titulo)}${ERR ? " · só as erradas" : ""}</p>
          <h1 id="h1" tabindex="-1">${ERR ? "As erradas, <em>corrigidas.</em>" : "Sua folha, <em>corrigida.</em>"}</h1>
          <section class="placar" aria-label="Pontuação">
            <p class="placar__n">${r.acertos}<span>/${r.total}</span></p>
            <p class="placar__rot">${r.acertos === 1 ? "acerto" : "acertos"}<br><span>${r.percentual}% de acertos</span></p>
            <div class="carimbo carimbo--res" aria-hidden="true"><div><span>Treineiros</span><b>Corrigido</b><span>${hm(estado.tempoGastoSeg)}${duracao}</span></div></div>
          </section>
        </div>
        <div class="res-topo__lado">
          <ul class="resumo-numeros">
            <li><strong>${r.erros}</strong> ${r.erros === 1 ? "errada" : "erradas"}</li>
            <li><strong>${r.brancas}</strong> em branco</li>
            <li><strong>${chutes.length}</strong> ${chutes.length === 1 ? "chute" : "chutes"}${chutes.length ? `, ${chutesOk.length} ${chutesOk.length === 1 ? "certo" : "certos"}` : ""}</li>
          </ul>
          <p class="botoes sem-impressao">
            ${!ERR && nRefazer ? `<a class="btn btn--primary btn--grande" href="simulado.html?id=${id}&modo=erradas">Refazer ${nRefazer === 1 ? "a que não acertei" : `as ${nRefazer} que não acertei`}</a>` : ""}
            <a class="btn btn--grande" href="provas.html">Escolher outra prova</a></p>
          <p class="legenda">${Motor.fmt(media)} por questão, em média${lentas.length ? `. Onde mais demorou: ${lentas.map(x => `questão ${x.q.numero} (${Motor.fmt(x.t)})`).join(", ")}` : ""}.</p>
        </div>
      </section>
      ${estado.tempoRestanteSeg === 0 ? '<p class="aviso">O tempo acabou e o simulado foi encerrado automaticamente.</p>' : ""}
      ${formatoOficial(prova, r)}

      <section class="res-sec" aria-labelledby="h-mat">
        <div class="titulo-linha"><h2 id="h-mat">Por matéria</h2><span class="titulo-linha__extra">da que mais precisa para a que menos</span></div>
        <div class="tabela-rola cartao-tabela"><table class="tabela tabela--mat">
          <thead><tr><th scope="col">Matéria</th><th scope="col">Acertos</th><th scope="col">Aproveitamento</th><th scope="col"><span class="sr">O que fazer</span></th></tr></thead>
          <tbody>${tabela}</tbody></table></div>
        <p class="legenda">“Rever” mostra abaixo só as questões desta prova daquela matéria que você errou, deixou em branco ou acertou chutando. “Treinar” abre questões novas da matéria, de todas as provas.</p>
      </section>

      <section class="res-sec" id="revisar" aria-labelledby="h-rev">
        <div class="titulo-linha"><h2 id="h-rev">Para revisar</h2></div>
        ${itens.length ? `<div class="filtros-rev sem-impressao" role="group" aria-label="Mostrar">${filtro("errada", "Erradas", n.errada, primeiroFiltro === "errada")}${filtro("branco", "Em branco", n.branco, primeiroFiltro === "branco")}${filtro("chute", "Chutes certos", n.chute, primeiroFiltro === "chute")}${itens.length > 1 ? `<button type="button" class="chip-f" data-f="" aria-pressed="false">Todas · ${itens.length}</button>` : ""}</div>
        <p class="filtro-mat sem-impressao" id="filtro-mat" hidden></p>
        <div id="lista-rev">${rev}</div>` : "<p>Você acertou tudo com segurança. Parabéns!</p>"}
      </section>

      <section class="agora" aria-labelledby="h-agora">
        <div class="agora__topo"><h2 id="h-agora">O que fazer <em>agora</em></h2><span class="mao">na ordem, de cima para baixo</span></div>
        <ol class="agora__passos">${passos.map((p, i) => `<li><span class="agora__n" aria-hidden="true">${i + 1}</span><h3>${p.t}</h3><p>${p.d}</p>${p.a}</li>`).join("")}</ol>
      </section>

      <div class="nav sem-impressao">
        <a class="btn" href="simulado.html?id=${id}">Refazer a prova inteira</a>
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

    // Filtros da revisão: por tipo (erradas, em branco, chutes) e, vindo da tabela, por matéria
    let fTipo = primeiroFiltro, fMat = "";
    const filtroMat = document.getElementById("filtro-mat");
    const aplicar = () => {
      app.querySelectorAll("#lista-rev .revisao").forEach(d => { d.hidden = (fTipo && d.dataset.tipo !== fTipo) || (fMat && d.dataset.materia !== fMat); });
      app.querySelectorAll(".chip-f").forEach(c => c.setAttribute("aria-pressed", c.dataset.f === fTipo));
      if (filtroMat) {
        filtroMat.hidden = !fMat;
        filtroMat.innerHTML = fMat ? `Mostrando só ${esc(fMat)}. <button type="button" class="btn-link" id="b-limpa-mat">Mostrar todas as matérias</button>` : "";
        const bl = document.getElementById("b-limpa-mat"); if (bl) bl.onclick = () => { fMat = ""; aplicar(); };
      }
    };
    app.querySelectorAll(".chip-f").forEach(c => c.onclick = () => { fTipo = c.dataset.f; aplicar(); });
    app.querySelectorAll("[data-mat]").forEach(b => b.onclick = () => {
      fMat = b.dataset.mat; fTipo = "";
      aplicar();
      const alvo = document.getElementById("revisar"); alvo.scrollIntoView({ behavior: "smooth", block: "start" });
      if (window.anunciar) anunciar(`Mostrando as questões de ${fMat} para revisar`);
    });
    if (itens.length) aplicar();
    window.addEventListener("beforeprint", () => { app.querySelectorAll("#lista-rev .revisao").forEach(d => { d.hidden = false; }); });

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
