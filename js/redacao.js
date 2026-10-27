/* Redação: tema oficial (ou livre), cronômetro, folha pautada com contagem de linhas e autoavaliação pelas 5 competências do Enem.
   Rascunho em "redacao-atual"; redações terminadas em "redacoes" (as 30 mais recentes). */
(function () {
  const app = document.getElementById("app"), aviso = document.getElementById("aviso");
  const E = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const MAX_LINHAS = 30, MIN_LINHAS = 8;             // no Enem, texto com até 7 linhas recebe nota zero
  let dados = null, atual = null, relogio = null, ultimo = 0, salvoEm = 0, timerAviso = null;

  function falar(t) { clearTimeout(timerAviso); aviso.textContent = t; aviso.hidden = false; if (window.anunciar) anunciar(t); timerAviso = setTimeout(() => { aviso.hidden = true; }, 8000); }
  const salvar = () => { if (atual) Armazem.gravar("redacao-atual", atual); };
  const dataBr = iso => new Date(iso).toLocaleDateString("pt-BR");

  /* ---- Início: escolher tema e tempo; histórico ---- */
  function inicio() {
    clearInterval(relogio);
    const salva = Armazem.ler("redacao-atual", null), hist = Armazem.ler("redacoes", []);
    const opcoes = dados.temas.map((t, i) => `<option value="${i}">${E(t.banca)} ${t.ano}: ${E(t.tema)}</option>`).join("");
    app.innerHTML = `<h1>Redação</h1>
      <p>Escreva com um tema oficial, no tempo que escolher, e depois avalie seu texto pelas 5 competências do Enem. A correção é sua: use a autoavaliação como guia e, se puder, peça a um professor para corrigir também.</p>
      ${salva && salva.tema ? `<p class="aviso">Você tem uma redação em andamento: “${E(salva.tema)}”. <button class="btn" id="b-cont" type="button">Continuar</button></p>` : ""}
      <form id="f-red" class="cfg">
        <fieldset><legend>Tema</legend>
          <label class="cfg__op"><input type="radio" name="origem" value="oficial" checked><span><strong>Tema oficial</strong><br>
            <select id="r-tema" class="campo" aria-label="Tema oficial">${opcoes}</select></span></label>
          <label class="cfg__op"><input type="radio" name="origem" value="livre"><span><strong>Outro tema</strong><br>
            <input id="r-livre" class="campo" maxlength="200" placeholder="Escreva o tema" aria-label="Outro tema"></span></label>
        </fieldset>
        <fieldset><legend>Tempo</legend>
          <label class="cfg__op"><input type="radio" name="tempo" value="90" checked><span><strong>1h30</strong><br>Tempo que costuma sobrar para a redação no dia do Enem.</span></label>
          <label class="cfg__op"><input type="radio" name="tempo" value="60"><span><strong>1 hora</strong><br>Para treinar sob pressão.</span></label>
          <label class="cfg__op"><input type="radio" name="tempo" value="0"><span><strong>Sem cronômetro</strong><br>O tempo gasto continua sendo registrado.</span></label>
        </fieldset>
        <button class="btn btn--primary" type="submit">Começar a escrever</button>
      </form>
      <h2 class="secao-seguinte">Suas redações</h2>
      ${hist.length ? `<ul class="lista-plano">${hist.map((r, i) => `<li><span><strong>${r.total} pontos</strong><br>${E(r.tema)}<br><span class="legenda">Escrita em ${dataBr(r.data)}</span></span><button class="btn" type="button" data-ver="${i}">Ver</button></li>`).join("")}</ul>`
        : "<p>As redações que você terminar aparecem aqui, com a nota da autoavaliação.</p>"}`;
    const f = document.getElementById("f-red");
    document.getElementById("r-livre").addEventListener("input", () => { f.elements.origem.value = "livre"; });
    document.getElementById("r-tema").addEventListener("change", () => { f.elements.origem.value = "oficial"; });
    f.addEventListener("submit", e => {
      e.preventDefault();
      if (salva && salva.tema && !window.confirm("Começar outra substitui a redação em andamento. Continuar?")) return;
      let t;
      if (f.elements.origem.value === "livre") {
        const livre = document.getElementById("r-livre").value.trim();
        if (!livre) { falar("Escreva o tema ou escolha um tema oficial."); document.getElementById("r-livre").focus(); return; }
        t = { banca: "", ano: "", tema: livre };
      } else t = dados.temas[+document.getElementById("r-tema").value];
      const min = +f.elements.tempo.value;
      atual = { tema: t.tema, banca: t.banca, ano: t.ano, minutos: min, tempoRestanteSeg: min ? min * 60 : null, tempoGastoSeg: 0, texto: "", pausado: false };
      salvar(); escrever();
    });
    const bc = document.getElementById("b-cont");
    if (bc) bc.onclick = () => { atual = salva; atual.pausado = false; escrever(); };
    app.querySelectorAll("[data-ver]").forEach(b => b.onclick = () => ver(hist[+b.dataset.ver]));
  }

  /* ---- Escrevendo ---- */
  function escrever() {
    app.innerHTML = `<div class="barra"><div><span class="versalete">${atual.tempoRestanteSeg === null ? "Tempo gasto" : "Tempo restante"}</span> <span id="tempo" role="timer"></span></div>
        <div class="barra__acoes"><button class="btn" id="b-pausa" type="button">Pausar</button><button class="btn btn--primary" id="b-fim" type="button">Terminei</button></div></div>
      <div class="tema-box"><p class="versalete">Tema${atual.ano ? ` (${E(atual.banca)} ${atual.ano})` : ""}</p><p><strong>${E(atual.tema)}</strong></p></div>
      <p><label for="texto">Seu texto (dissertativo-argumentativo, de ${MIN_LINHAS} a ${MAX_LINHAS} linhas na folha oficial)</label></p>
      <textarea id="texto" class="folha-red" spellcheck="false" autocomplete="off"></textarea>
      <p class="contadores" id="cont" aria-live="polite"></p>
      <p class="legenda">O corretor ortográfico do navegador fica desligado, como no papel. A contagem de linhas é uma estimativa (cerca de 75 letras por linha).</p>`;
    const t = document.getElementById("texto");
    t.value = atual.texto || "";
    const contar = () => {
      const c = Motor.contarRedacao(t.value), alerta = c.linhas > MAX_LINHAS || (c.linhas > 0 && c.linhas < MIN_LINHAS);
      document.getElementById("cont").innerHTML = `<span>${c.palavras} ${c.palavras === 1 ? "palavra" : "palavras"}</span><span class="${alerta ? "alerta" : ""}">cerca de ${c.linhas} de ${MAX_LINHAS} linhas${c.linhas > MAX_LINHAS ? " (passou do limite)" : c.linhas > 0 && c.linhas < MIN_LINHAS ? " (texto curto demais: até 7 linhas vale zero)" : ""}</span>`;
    };
    let tSalvar = null;
    t.addEventListener("input", () => { atual.texto = t.value; contar(); clearTimeout(tSalvar); tSalvar = setTimeout(salvar, 500); });
    contar(); t.focus();
    document.getElementById("b-pausa").onclick = () => {
      atual.pausado = !atual.pausado; ultimo = Date.now(); salvar();
      document.getElementById("b-pausa").textContent = atual.pausado ? "Retomar" : "Pausar";
      t.readOnly = atual.pausado;
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

  /* ---- Autoavaliação pelas 5 competências ---- */
  function avaliar() {
    clearInterval(relogio); salvar();
    const c = Motor.contarRedacao(atual.texto);
    app.innerHTML = `<h1 id="h-av" tabindex="-1">Autoavaliação</h1>
      <div class="tema-box"><p><strong>${E(atual.tema)}</strong></p><p class="legenda">${c.palavras} palavras, cerca de ${c.linhas} linhas, ${Motor.fmt(atual.tempoGastoSeg)} escrevendo.</p></div>
      <details class="revisao"><summary>Reler o texto</summary><div class="texto-red">${E(atual.texto).replace(/\n/g, "<br>")}</div></details>
      <p>Leia seu texto com calma e marque, em cada competência, o nível que ele atinge. Seja exigente: no Enem, cada uma vale de 0 a 200.</p>
      <form id="f-av">${dados.competencias.map(cp => `<fieldset class="comp"><legend>Competência ${cp.n}: ${E(cp.titulo)}</legend><p>${E(cp.descricao)}</p>
        <div class="linha">${dados.niveis.map(nv => `<label class="chk"><input type="radio" name="c${cp.n}" value="${nv.pontos}"${nv.pontos === 120 ? " checked" : ""}> ${nv.pontos} <span class="legenda">(${E(nv.rotulo)})</span></label>`).join("")}</div></fieldset>`).join("")}
        <p>Total: <strong id="av-total" aria-live="polite"></strong></p>
        <p><button class="btn btn--primary" type="submit">Guardar redação</button> <button class="btn" type="button" id="b-voltar">Voltar a escrever</button></p></form>`;
    const f = document.getElementById("f-av");
    const total = () => dados.competencias.reduce((s, cp) => s + +f.elements["c" + cp.n].value, 0);
    const mostrar = () => { document.getElementById("av-total").textContent = total() + " de 1000"; };
    f.addEventListener("change", mostrar); mostrar();
    document.getElementById("h-av").focus();
    document.getElementById("b-voltar").onclick = () => { escrever(); };
    f.addEventListener("submit", e => {
      e.preventDefault();
      const notas = dados.competencias.map(cp => +f.elements["c" + cp.n].value);
      const reg = { data: new Date().toISOString(), tema: atual.tema, banca: atual.banca, ano: atual.ano, texto: atual.texto,
                    notas: notas, total: notas.reduce((a, b) => a + b, 0), tempoGastoSeg: atual.tempoGastoSeg };
      const hist = Armazem.ler("redacoes", []); hist.unshift(reg); Armazem.gravar("redacoes", hist.slice(0, 30));
      Armazem.apagar("redacao-atual"); atual = null;
      Registro.somarAtividade(1);                     // conta para a sequência de dias
      ver(reg, true);
    });
  }

  /* ---- Ver uma redação guardada ---- */
  function ver(r, nova) {
    app.innerHTML = `<h1 id="h-ver" tabindex="-1">${nova ? "Redação guardada" : "Sua redação"}</h1>
      <p class="nota-red">${r.total}<span class="legenda"> de 1000 (autoavaliação)</span></p>
      <div class="tema-box"><p><strong>${E(r.tema)}</strong></p><p class="legenda">Escrita em ${dataBr(r.data)}, em ${Motor.fmt(r.tempoGastoSeg || 0)}.</p></div>
      <table class="tabela"><caption class="versalete">Por competência</caption><tbody>${dados.competencias.map((cp, i) => `<tr><th scope="row">${cp.n}. ${E(cp.titulo)}</th><td>${r.notas[i]}</td></tr>`).join("")}</tbody></table>
      <div class="explicacao texto-red">${E(r.texto).replace(/\n/g, "<br>")}</div>
      <div class="nav sem-impressao"><button class="btn btn--primary" type="button" id="b-nova">Escrever outra</button>
        <button class="btn" type="button" id="b-copiar">Copiar o texto</button><button class="btn" type="button" id="b-print">Imprimir ou salvar em PDF</button></div>`;
    document.getElementById("h-ver").focus();
    document.getElementById("b-nova").onclick = inicio;
    document.getElementById("b-print").onclick = () => window.print();
    document.getElementById("b-copiar").onclick = () => Registro.copiar(r.texto).then(ok => falar(ok ? "Texto copiado." : "Não foi possível copiar."));
  }

  window.addEventListener("pagehide", salvar);
  document.addEventListener("visibilitychange", () => { if (document.hidden) salvar(); });
  fetch("data/redacao.json").then(r => { if (!r.ok) throw 0; return r.json(); }).then(d => { dados = d; inicio(); })
    .catch(() => { app.innerHTML = "<h1>Redação</h1><p>Não foi possível carregar os temas. Se abriu o arquivo direto, use um servidor local (veja o README).</p>"; });
})();
