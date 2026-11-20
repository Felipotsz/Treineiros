/* Redação: tema oficial (Enem ou FATEC), tema extra do Treineiros (com sorteio) ou livre, cronômetro, folha pautada com contagem de linhas e autoavaliação pelas 5 competências do Enem.
   Nos temas da FATEC: orientações da prova, resumo da coletânea (quando houver) e checagem das orientações antes da nota.
   Rascunho em "redacao-atual"; redações terminadas em "redacoes" (as 30 mais recentes). */
(function () {
  const app = document.getElementById("app"), aviso = document.getElementById("aviso");
  const E = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const MAX_LINHAS = 30, MIN_LINHAS = 8;             // no Enem, texto com até 7 linhas recebe nota zero
  let dados = null, atual = null, relogio = null, ultimo = 0, salvoEm = 0, timerAviso = null;

  function falar(t) { clearTimeout(timerAviso); aviso.textContent = t; aviso.hidden = false; if (window.anunciar) anunciar(t); timerAviso = setTimeout(() => { aviso.hidden = true; }, 8000); }
  const salvar = () => { if (atual) Armazem.gravar("redacao-atual", atual); };
  const ehFatec = t => t && t.banca === "FATEC";
  const rotuloEdicao = t => t.banca === "FATEC" && t.semestre ? `${t.ano}/${t.semestre}` : String(t.ano);
  const dataBr = iso => new Date(iso).toLocaleDateString("pt-BR");

  /* ---- Início: escolher tema e tempo; histórico ---- */
  function inicio() {
    clearInterval(relogio);
    const salva = Armazem.ler("redacao-atual", null), hist = Armazem.ler("redacoes", []);
    const extras = dados.temasExtras || [];
    const eixos = [...new Set(extras.map(x => x.eixo))];
    const opcoesExtras = eixos.map(ex => `<optgroup label="${E(ex)}">${extras.map((x, i) => x.eixo === ex ? `<option value="${i}">${E(x.tema)}</option>` : "").join("")}</optgroup>`).join("");
    const aba = (id, rot, ativa) => `<button type="button" role="tab" class="abas-tema__aba" id="aba-${id}" aria-controls="painel-${id}" aria-selected="${ativa}" tabindex="${ativa ? 0 : -1}">${rot}</button>`;
    const modelo0 = salva && salva.banca === "FATEC" ? "FATEC" : (Armazem.ler("redacao-modelo", "Enem") === "FATEC" ? "FATEC" : "Enem");
    // temas oficiais: um cartão por tema, com a etiqueta de onde ele caiu (Enem 2024, FATEC 2026/2)
    const ordem = dados.temas.map((t, i) => ({ t, i })).sort((x, y) => (y.t.ano - x.t.ano) || ((y.t.semestre || 0) - (x.t.semestre || 0)));
    const cartoes = ordem.map(({ t, i }) => `<label class="tema-op" data-banca="${E(t.banca)}"${t.banca === modelo0 ? "" : " hidden"}>
        <input type="radio" name="tema" value="${i}">
        <span class="tema-op__cima"><span class="tema-op__tag tema-op__tag--${t.banca === "FATEC" ? "fatec" : "enem"}">Tema ${t.banca === "FATEC" ? "da FATEC" : "do Enem"}</span><span class="tema-op__ano">${rotuloEdicao(t)}</span></span>
        <span class="tema-op__tema">${E(t.tema)}</span></label>`).join("");
    const modeloOp = (m, desc) => `<label class="modelo-op"><input type="radio" name="modelo" value="${m}"${m === modelo0 ? " checked" : ""}><span><strong>${m}</strong><span>${desc}</span></span></label>`;
    const tempoOp = (v, t, on) => `<label><input type="radio" name="tempo" value="${v}"${on ? " checked" : ""}><span>${t}</span></label>`;
    document.getElementById("conteudo").classList.add("pag");
    app.innerHTML = `<form id="f-red" class="cfg red-inicio">
      <section class="faixa" aria-labelledby="red-t"><div class="faixa__in">
        <div class="faixa__texto">
          <p class="sobretitulo">Redação</p>
          <h1 id="red-t">Escreva com <em>o relógio correndo</em></h1>
          <p class="faixa__lead">Folha oficial de 30 linhas, cronômetro e, no fim, você corrige a sua com a grade da banca. A correção é sua: use como guia e, se puder, peça a um professor para ler também.</p>
        </div>
        <fieldset class="modelos"><legend class="rotulo">Para qual prova?</legend>
          ${modeloOp("Enem", "Dissertativo-argumentativo, 5 competências, nota até 1000")}${modeloOp("FATEC", "Narrativo ou dissertativo, com título, a partir de uma coletânea")}
        </fieldset>
      </div></section>
      <div class="pag__corpo">
        ${salva && salva.tema ? `<p class="aviso red-andamento">Você tem uma redação em andamento: “${E(salva.tema)}”. <button class="btn" id="b-cont" type="button">Continuar</button></p>` : ""}
        <div class="titulo-linha red-tit"><h2>Escolha <em>o tema</em></h2>
          <div class="abas-tema titulo-linha__extra" role="tablist" aria-label="Tipo de tema">${aba("oficial", "Oficiais", true)}${extras.length ? aba("extra", "Extras", false) : ""}${aba("livre", "Meu tema", false)}</div></div>
        <div class="abas-tema__painel" role="tabpanel" id="painel-oficial" aria-labelledby="aba-oficial">
          <p class="legenda" id="r-of-leg"></p>
          <div class="temas-lista" role="radiogroup" aria-labelledby="aba-oficial">${cartoes}</div></div>
        ${extras.length ? `<div class="abas-tema__painel red-cartao" role="tabpanel" id="painel-extra" aria-labelledby="aba-extra" hidden>
          <p class="legenda">Temas escritos pelo Treineiros no estilo do Enem, para treinar mais. Não caíram em nenhuma prova.</p>
          <label class="rotulo" for="r-extra">Tema extra</label><select id="r-extra" class="campo">${opcoesExtras}</select>
          <p class="botoes"><button class="btn" type="button" id="b-sortear">Sortear um tema</button></p>
          <div id="r-pontos"></div></div>` : ""}
        <div class="abas-tema__painel red-cartao" role="tabpanel" id="painel-livre" aria-labelledby="aba-livre" hidden>
          <p class="legenda">Um tema que um professor passou ou que você quer treinar. A avaliação segue a prova escolhida acima.</p>
          <label class="rotulo" for="r-livre">Meu tema</label><input id="r-livre" class="campo" maxlength="200" placeholder="Escreva o tema"></div>
        <fieldset class="red-tempo"><legend class="rotulo">Quanto tempo?</legend>
          <div class="segmento cfg__seg">${tempoOp(90, "1h30", true)}${tempoOp(60, "1 hora", false)}${tempoOp(0, "Sem cronômetro", false)}</div>
          <p class="cfg__dica" id="r-tempo-dica"></p></fieldset>
        <div class="red-barra">
          <p id="r-escolha" aria-live="polite"></p>
          <button class="btn btn--claro btn--grande" type="submit">Começar a escrever</button>
        </div>
        <div class="titulo-linha red-hist"><h2>Suas <em>redações</em></h2></div>
        ${hist.length ? `<ul class="lista-plano">${hist.map((r, i) => `<li><span><strong>${r.total} pontos</strong>${r.banca ? ` <span class="tema-op__tag tema-op__tag--${r.banca === "FATEC" ? "fatec" : "enem"}">${E(r.banca)}</span>` : ""}<br>${E(r.tema)}<br><span class="legenda">Escrita em ${dataBr(r.data)}</span></span><button class="btn" type="button" data-ver="${i}">Ver</button></li>`).join("")}</ul>`
          : "<p>As redações que você terminar aparecem aqui, com a nota da autoavaliação.</p>"}
      </div></form>`;
    const f = document.getElementById("f-red");
    let origem = "oficial";
    const abas = [...app.querySelectorAll('[role="tab"]')];
    const abrir = (bt, foco) => {
      abas.forEach(x => { const on = x === bt; x.setAttribute("aria-selected", on); x.tabIndex = on ? 0 : -1; document.getElementById(x.getAttribute("aria-controls")).hidden = !on; });
      origem = bt.id.slice(4); if (foco) bt.focus();
      if (document.getElementById("r-escolha")) escolha();
    };
    abas.forEach((bt, i) => {
      bt.onclick = () => abrir(bt);
      bt.onkeydown = e => {                                         // setas trocam de aba (padrão de abas acessíveis)
        const d = { ArrowRight: 1, ArrowLeft: -1 }[e.key]; if (d === undefined) return;
        e.preventDefault();
        const vis = abas.filter(x => !x.hidden), j = vis.indexOf(bt);
        abrir(vis[(j + d + vis.length) % vis.length], true);
      };
    });
    // Enem ou FATEC: filtra os temas oficiais; os temas extras são no estilo do Enem
    const abaExtra = document.getElementById("aba-extra");
    const modelo = () => (f.querySelector("[name=modelo]:checked") || {}).value || "Enem";
    const aplicarModelo = () => {
      const m = modelo(); Armazem.gravar("redacao-modelo", m);
      let primeiro = null, n = 0;
      f.querySelectorAll(".tema-op").forEach(l => { const on = l.dataset.banca === m; l.hidden = !on; if (on) { n++; if (!primeiro) primeiro = l; } });
      f.querySelectorAll(".tema-op[hidden] input").forEach(i => { i.checked = false; });
      if (!f.querySelector(".tema-op:not([hidden]) input:checked") && primeiro) primeiro.querySelector("input").checked = true;
      document.getElementById("r-of-leg").textContent = `${n} temas que caíram ${m === "FATEC" ? "no Vestibular FATEC" : "no Enem"}, do mais recente para o mais antigo.`;
      if (abaExtra) { abaExtra.hidden = m === "FATEC"; if (m === "FATEC" && origem === "extra") abrir(document.getElementById("aba-oficial")); }
    };
    const DT = { 90: "Um tempo realista para planejar, escrever e revisar no dia da prova.", 60: "Para treinar sob pressão.", 0: "No seu ritmo; o tempo gasto continua sendo registrado." };
    const escolha = () => {
      const m = modelo(), tempo = { 90: "1h30", 60: "1 hora", 0: "sem cronômetro" }[f.elements.tempo.value];
      let txt;
      if (origem === "livre") { const v = document.getElementById("r-livre").value.trim(); txt = v ? `<b>Meu tema · ${E(m)}</b> ${E(v)}` : `<b>Meu tema</b> escreva o tema acima`; }
      else if (origem === "extra") { const x = extras[+selExtra.value]; txt = `<b>Tema extra</b> ${x ? E(x.tema) : ""}`; }
      else { const esc = f.querySelector(".tema-op:not([hidden]) input:checked"), t = esc && dados.temas[+esc.value]; txt = t ? `<b>${E(t.banca)} ${rotuloEdicao(t)}</b> ${E(t.tema)}` : "Escolha um tema"; }
      document.getElementById("r-escolha").innerHTML = `${txt} <span>· ${tempo}</span>`;
      document.getElementById("r-tempo-dica").textContent = DT[f.elements.tempo.value];
    };
    f.querySelectorAll("[name=modelo]").forEach(r => r.addEventListener("change", aplicarModelo));
    aplicarModelo();
    f.addEventListener("change", escolha); f.addEventListener("input", escolha);
    const selExtra = document.getElementById("r-extra");
    const mostrarPontos = () => {
      const x = extras[+selExtra.value];
      document.getElementById("r-pontos").innerHTML = x && x.pontos ? `<p class="tema-escolhido"><strong>${E(x.tema)}</strong></p><p class="legenda">Pontos de partida (não precisa usar todos):</p><ul class="legenda">${x.pontos.map(p => `<li>${E(p)}</li>`).join("")}</ul>` : "";
    };
    if (selExtra) {
      selExtra.addEventListener("change", mostrarPontos); mostrarPontos();
      document.getElementById("b-sortear").onclick = () => {
        let i; do { i = Math.floor(Math.random() * extras.length); } while (extras.length > 1 && i === +selExtra.value);
        selExtra.value = String(i); mostrarPontos(); escolha();
        if (window.anunciar) anunciar("Tema sorteado: " + extras[i].tema);
      };
    }
    f.addEventListener("submit", e => {
      e.preventDefault();
      if (salva && salva.tema && !window.confirm("Começar outra substitui a redação em andamento. Continuar?")) return;
      let t;
      if (origem === "livre") {
        const livre = document.getElementById("r-livre").value.trim();
        if (!livre) { falar("Escreva o tema ou escolha um tema oficial."); document.getElementById("r-livre").focus(); return; }
        t = { banca: modelo() === "FATEC" ? "FATEC" : "", ano: "", tema: livre };
      } else if (origem === "extra") {
        const x = extras[+selExtra.value];
        t = { banca: "", ano: "", tema: x.tema, extra: true, pontos: x.pontos || null };
      } else {
        const esc = f.querySelector(".tema-op:not([hidden]) input:checked");
        if (!esc) { falar("Escolha um tema."); return; }
        t = dados.temas[+esc.value];
      }
      const min = +f.elements.tempo.value;
      atual = { tema: t.tema, banca: t.banca, ano: t.ano, semestre: t.semestre || null, coletanea: t.coletanea || null, extra: !!t.extra, pontos: t.pontos || null, minutos: min, tempoRestanteSeg: min ? min * 60 : null, tempoGastoSeg: 0, texto: "", pausado: false };
      salvar(); escrever();
    });
    escolha();
    const bc = document.getElementById("b-cont");
    if (bc) bc.onclick = () => { atual = salva; atual.pausado = false; escrever(); };
    app.querySelectorAll("[data-ver]").forEach(b => b.onclick = () => ver(hist[+b.dataset.ver]));
  }

  /* ---- Escrevendo: a folha oficial, com linhas numeradas, e ao lado as linhas e as orientações ---- */
  const nomeProva = t => t.banca ? `${t.banca === "FATEC" ? "Vestibular FATEC" : "Enem"}${t.ano ? " " + rotuloEdicao(t) : ""}` : t.extra ? "Tema extra do Treineiros" : "Tema livre";
  function escrever() {
    document.getElementById("conteudo").classList.remove("pag");
    const fatec = ehFatec(atual);
    const numeros = Array.from({ length: MAX_LINHAS }, (_, i) => `<span${i < MIN_LINHAS ? ' class="min"' : ""}>${i + 1}</span>`).join("");
    const ladoOrient = fatec
      ? `<section class="lado-card" aria-labelledby="h-or"><h2 id="h-or" class="rotulo">Orientações da FATEC</h2><ul class="orient" id="orient">${(dados.orientacoesFatec || []).slice(0, 5).map((o, i) => `<li data-o="${i}"><span class="orient__b" aria-hidden="true"></span><span>${E(o)}<small></small></span></li>`).join("")}</ul></section>`
      : `<section class="lado-card" aria-labelledby="h-or"><h2 id="h-or" class="rotulo">O que a banca olha</h2><ol class="orient orient--comp">${dados.competencias.map(cp => `<li><span class="orient__n">C${cp.n}</span><span>${E(cp.titulo)}</span></li>`).join("")}</ol></section>`;
    app.innerHTML = `<div class="barra"><div class="barra__linha">
        <div class="barra__id"><p class="barra__prova">Redação · ${E(nomeProva(atual))}</p><p class="barra__onde" id="salvo">Rascunho salvo neste aparelho</p></div>
        <div class="barra__tempo"><span class="sr">${atual.tempoRestanteSeg === null ? "Tempo gasto" : "Tempo restante"}: </span><span id="tempo" role="timer"></span></div>
        <div class="barra__acoes"><button class="btn" id="b-pausa" type="button">Pausar</button><button class="btn btn--primary" id="b-fim" type="button">Terminei</button></div></div></div>
      <div class="red-escrever">
        <div class="red-folha-col">
          <details class="tema-faixa" open><summary><span class="tema-faixa__rot">Tema · ${E(nomeProva(atual))} <span class="tema-faixa__dica">· toque para recolher</span></span><span class="tema-faixa__tema">${E(atual.tema)}</span></summary>
            ${fatec ? orientacoesFatec() : `<p>Texto dissertativo-argumentativo, de ${MIN_LINHAS} a ${MAX_LINHAS} linhas, com proposta de intervenção.</p>`}
            ${atual.pontos ? `<p><strong>Pontos de partida</strong> (não precisa usar todos):</p><ul>${atual.pontos.map(p => `<li>${E(p)}</li>`).join("")}</ul>` : ""}</details>
          <div class="folha-oficial">
            ${fatec ? `<label class="folha-oficial__titulo"><span class="rotulo">Título</span><input id="titulo-red" maxlength="120" autocomplete="off" spellcheck="false" value="${E(atual.titulo || "")}" placeholder="Dê um título ao texto"></label>` : ""}
            <div class="folha-oficial__corpo">
              <div class="folha-oficial__num" aria-hidden="true">${numeros}</div>
              <label for="texto" class="sr">Seu texto</label>
              <textarea id="texto" class="folha-red" spellcheck="false" autocomplete="off"></textarea>
            </div>
          </div>
          <p class="legenda">O corretor ortográfico do navegador fica desligado, como no papel. As linhas da folha acompanham o que você escreve; a contagem é uma estimativa (cerca de 75 letras por linha).</p>
        </div>
        <aside class="red-lado">
          <section class="lado-card" aria-labelledby="h-lin"><h2 id="h-lin" class="rotulo">Linhas</h2>
            <div id="cont" aria-live="polite"></div></section>
          ${ladoOrient}
        </aside>
      </div>`;
    const t = document.getElementById("texto"), tit = document.getElementById("titulo-red");
    t.value = atual.texto || "";
    const crescer = () => { t.style.height = "auto"; t.style.height = Math.max(t.scrollHeight, 0) + "px"; };
    const contar = () => {
      const c = Motor.contarRedacao(t.value), alerta = c.linhas > MAX_LINHAS || (c.linhas > 0 && c.linhas < MIN_LINHAS);
      const seg = Array.from({ length: MAX_LINHAS }, (_, i) => `<i class="${i < Math.min(c.linhas, MAX_LINHAS) ? "cheia" : ""}${i === MIN_LINHAS - 1 ? " min" : ""}"></i>`).join("");
      const msg = c.linhas > MAX_LINHAS ? "Passou do limite de 30 linhas." : c.linhas > 0 && c.linhas < MIN_LINHAS ? "Texto curto demais: até 7 linhas vale zero." : c.linhas ? `Mínimo de ${MIN_LINHAS} já alcançado.` : `Escreva de ${MIN_LINHAS} a ${MAX_LINHAS} linhas.`;
      document.getElementById("cont").innerHTML = `<p class="lado-grande">${c.linhas} <span>de ${MAX_LINHAS}</span></p>
        <div class="linhas-barra" aria-hidden="true">${seg}</div>
        <p class="${alerta ? "alerta" : "legenda"}">${msg} ${c.palavras} ${c.palavras === 1 ? "palavra" : "palavras"}.</p>`;
      // orientações que dá para conferir sozinho: título e parágrafos
      const o = document.getElementById("orient");
      if (o) {
        const pars = t.value.split(/\n\s*\n|\n/).filter(x => x.trim()).length;
        const marca = (i, ok, txt) => { const li = o.querySelector(`[data-o="${i}"]`); if (!li) return; li.classList.toggle("ok", ok); li.querySelector("small").textContent = txt; };
        marca(0, !!(tit && tit.value.trim()), tit && tit.value.trim() ? "Feito: o texto tem título" : "Falta o título");
        marca(2, pars >= 2, pars ? `${pars} ${pars === 1 ? "parágrafo" : "parágrafos"} até agora` : "");
        [1, 3, 4].forEach(i => marca(i, false, "Confira ao reler"));
      }
    };
    let tSalvar = null;
    const aoMudar = () => { atual.texto = t.value; if (tit) atual.titulo = tit.value; contar(); crescer(); clearTimeout(tSalvar); tSalvar = setTimeout(salvar, 500); };
    t.addEventListener("input", aoMudar); if (tit) tit.addEventListener("input", aoMudar);
    contar(); crescer(); (tit && !tit.value ? tit : t).focus();
    document.getElementById("b-pausa").onclick = () => {
      atual.pausado = !atual.pausado; ultimo = Date.now(); salvar();
      document.getElementById("b-pausa").textContent = atual.pausado ? "Retomar" : "Pausar";
      t.readOnly = atual.pausado; if (tit) tit.readOnly = atual.pausado;
      falar(atual.pausado ? "Redação pausada. O tempo está parado." : "Tempo correndo de novo.");
    };
    document.getElementById("b-fim").onclick = () => {
      const c = Motor.contarRedacao(t.value);
      if (!c.palavras) { falar("Escreva o texto antes de terminar."); return; }
      avaliar();
    };
    clearInterval(relogio); ultimo = salvoEm = Date.now();
    relogio = setInterval(tique, 1000); mostrarTempo();
  }
  function tique() {
    if (!atual || atual.pausado) return;
    const agora = Date.now(), dt = Math.round((agora - ultimo) / 1000);
    if (dt < 1) return;
    ultimo += dt * 1000;
    if (dt > 300) { atual.pausado = true; salvar(); escrever(); falar("Pausamos porque o aparelho ficou inativo. Esse intervalo não contou."); return; }
    atual.tempoGastoSeg += dt;
    if (atual.tempoRestanteSeg !== null) {
      const antes = atual.tempoRestanteSeg;
      atual.tempoRestanteSeg = Math.max(0, antes - dt);
      if (antes > 600 && atual.tempoRestanteSeg <= 600) falar("Faltam 10 minutos.");
      if (antes > 0 && atual.tempoRestanteSeg === 0) { falar("O tempo acabou. Termine a frase e passe para a autoavaliação."); }
    }
    mostrarTempo();
    if (agora - salvoEm >= 5000) { salvar(); salvoEm = agora; }
  }
  function mostrarTempo() {
    const el = document.getElementById("tempo");
    if (el) el.textContent = Motor.fmt(atual.tempoRestanteSeg === null ? atual.tempoGastoSeg : atual.tempoRestanteSeg);
  }

  // Orientações oficiais da prova da FATEC e, quando houver, o resumo dos textos da coletânea
  function orientacoesFatec() {
    const col = atual.coletanea && atual.coletanea.length ? `<details class="tema-faixa__col"><summary>Resumo da coletânea da prova</summary><ul>${atual.coletanea.map(x => `<li>${E(x)}</li>`).join("")}</ul><p class="legenda">Resumo feito pelo Treineiros. Os textos completos estão no PDF da prova, na página de provas.</p></details>` : "";
    return `<p>A FATEC aceita <strong>texto narrativo ou dissertativo-argumentativo</strong>, com título. As orientações da prova estão ao lado.</p>${col}`;
  }

  /* ---- Autoavaliação pelas 5 competências ---- */
  function avaliar() {
    document.getElementById("conteudo").classList.remove("pag");
    clearInterval(relogio); salvar();
    const c = Motor.contarRedacao(atual.texto), fatec = ehFatec(atual);
    const temTitulo = !!(atual.titulo && atual.titulo.trim());
    const temPars = (atual.texto || "").split(/\n/).filter(x => x.trim()).length >= 2;
    const grade = `<div class="tabela-rola"><table class="grade-av">
      <thead><tr><th scope="col">Competência</th>${dados.niveis.map(nv => `<th scope="col" title="${E(nv.rotulo)}">${nv.pontos}</th>`).join("")}</tr></thead>
      <tbody>${dados.competencias.map(cp => `<tr><th scope="row"><details class="grade-av__comp"><summary><span class="grade-av__n">C${cp.n}</span> ${E(cp.titulo)}</summary><p>${E(cp.descricao)}</p></details></th>
        ${dados.niveis.map(nv => `<td><input type="radio" name="c${cp.n}" value="${nv.pontos}"${nv.pontos === 120 ? " checked" : ""} aria-label="Competência ${cp.n}, ${E(cp.titulo)}: ${nv.pontos} pontos (${E(nv.rotulo)})"></td>`).join("")}</tr>`).join("")}</tbody></table></div>
      <p class="grade-av__niveis legenda">${dados.niveis.map(nv => `<span><b>${nv.pontos}</b> ${E(nv.rotulo)}</span>`).join("")}</p>`;
    app.innerHTML = `<div class="av-topo"><div><p class="sobretitulo">Depois de terminar · ${E(nomeProva(atual))}</p>
        <h1 id="h-av" tabindex="-1">Corrija <em>como a banca</em></h1>
        <p class="legenda">${E(atual.tema)} · ${c.palavras} palavras, cerca de ${c.linhas} linhas, ${Motor.fmt(atual.tempoGastoSeg)} escrevendo.</p></div>
        <p class="av-total"><strong id="av-total" aria-live="polite"></strong><span> / 1000</span></p></div>
      <details class="revisao"><summary>Reler o texto</summary><div class="texto-red">${temTitulo ? `<p><strong>${E(atual.titulo)}</strong></p>` : ""}${E(atual.texto).replace(/\n/g, "<br>")}</div></details>
      ${fatec ? `<p class="aviso">A FATEC não divulga uma grade de correção por competências. Use as 5 competências do Enem como guia de estudo e confira antes as orientações da própria prova.</p>` : ""}
      <form id="f-av">${fatec ? `<fieldset class="comp"><legend>Orientações da prova da FATEC</legend><p>Marque as que seu texto cumpre.</p>${(dados.orientacoesFatec || []).slice(0, 5).map((o, i) => `<label class="chk"><input type="checkbox" name="o${i}"${(i === 0 && temTitulo) || (i === 2 && temPars) ? " checked" : ""}> ${E(o)}</label>`).join("<br>")}</fieldset>` : ""}
        <fieldset class="comp comp--grade"><legend>Marque, em cada competência, a bolinha que descreve o seu texto</legend><p>Toque no nome da competência para ver o que conta. Seja exigente: cada uma vale de 0 a 200.</p>${grade}</fieldset>
        <p class="botoes"><button class="btn btn--primary btn--grande" type="submit">Guardar redação</button> <button class="btn btn--grande" type="button" id="b-voltar">Voltar a escrever</button></p></form>`;
    const f = document.getElementById("f-av");
    const total = () => dados.competencias.reduce((s, cp) => s + +f.elements["c" + cp.n].value, 0);
    const mostrar = () => { document.getElementById("av-total").textContent = total(); };
    f.addEventListener("change", mostrar); mostrar();
    document.getElementById("h-av").focus();
    document.getElementById("b-voltar").onclick = () => { escrever(); };
    f.addEventListener("submit", e => {
      e.preventDefault();
      const notas = dados.competencias.map(cp => +f.elements["c" + cp.n].value);
      const pend = fatec ? (dados.orientacoesFatec || []).slice(0, 5).filter((o, i) => !f.elements["o" + i].checked) : [];
      const reg = { data: new Date().toISOString(), tema: atual.tema, banca: atual.banca, ano: atual.ano, semestre: atual.semestre || null, titulo: atual.titulo || "", texto: atual.texto, orientacoesPendentes: pend,
                    notas: notas, total: notas.reduce((a, b) => a + b, 0), tempoGastoSeg: atual.tempoGastoSeg };
      const hist = Armazem.ler("redacoes", []); hist.unshift(reg); Armazem.gravar("redacoes", hist.slice(0, 30));
      const atualExtra = atual.extra; Armazem.apagar("redacao-atual"); atual = null;
      Registro.somarAtividade(1);                     // conta para a sequência de dias
      if (window.contarEvento) contarEvento(reg.ano ? "redacao/oficial" : atualExtra ? "redacao/extra" : "redacao/livre");
      ver(reg, true);
    });
  }

  /* ---- Ver uma redação guardada ---- */
  function ver(r, nova) {
    document.getElementById("conteudo").classList.remove("pag");
    app.innerHTML = `<h1 id="h-ver" tabindex="-1">${nova ? "Redação guardada" : "Sua redação"}</h1>
      <p class="nota-red">${r.total}<span class="legenda"> de 1000 (autoavaliação)</span></p>
      <div class="tema-box"><p><strong>${E(r.tema)}</strong></p><p class="legenda">Escrita em ${dataBr(r.data)}, em ${Motor.fmt(r.tempoGastoSeg || 0)}.</p></div>
      ${r.orientacoesPendentes && r.orientacoesPendentes.length ? `<p class="aviso">Orientações da FATEC que você não marcou: ${r.orientacoesPendentes.map(E).join(" ")}</p>` : ""}
      <table class="tabela"><caption class="versalete">Por competência</caption><tbody>${dados.competencias.map((cp, i) => `<tr><th scope="row">${cp.n}. ${E(cp.titulo)}</th><td>${r.notas[i]}</td></tr>`).join("")}</tbody></table>
      <div class="explicacao texto-red">${r.titulo ? `<p><strong>${E(r.titulo)}</strong></p>` : ""}${E(r.texto).replace(/\n/g, "<br>")}</div>
      <div class="nav sem-impressao"><button class="btn btn--primary" type="button" id="b-nova">Escrever outra</button>
        <button class="btn" type="button" id="b-copiar">Copiar o texto</button><button class="btn" type="button" id="b-print">Imprimir ou salvar em PDF</button></div>`;
    document.getElementById("h-ver").focus();
    document.getElementById("b-nova").onclick = inicio;
    document.getElementById("b-print").onclick = () => window.print();
    document.getElementById("b-copiar").onclick = () => Registro.copiar((r.titulo ? r.titulo + "\n\n" : "") + r.texto).then(ok => falar(ok ? "Texto copiado." : "Não foi possível copiar."));
  }

  window.addEventListener("pagehide", salvar);
  document.addEventListener("visibilitychange", () => { if (document.hidden) salvar(); });
  fetch("data/redacao.json").then(r => { if (!r.ok) throw 0; return r.json(); }).then(d => { dados = d; inicio(); })
    .catch(() => { app.innerHTML = "<h1>Redação</h1><p>Não foi possível carregar os temas. Se abriu o arquivo direto, use um servidor local (veja o README).</p>"; });
})();
