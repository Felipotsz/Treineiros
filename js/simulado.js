/* Simulado: telas (retomar, configurar, prova, pausa), cronômetro, persistência e conveniências. */
(function () {
  const params = new URLSearchParams(location.search);
  const ID = params.get("id");
  const MODO = params.get("modo") === "erradas" ? "erradas" : "completo";
  const SUF = MODO === "erradas" ? ":erradas" : "";
  const CH_AND = "andamento:" + ID + SUF, CH_RES = "resultado:" + ID + SUF, CH_RAS = "rascunho:" + ID + SUF;
  const app = document.getElementById("app"), dlg = document.getElementById("dlg"), aviso = document.getElementById("aviso");
  let prova = null, estado = null, relogio = null, ultimo = 0, salvoEm = 0, tela = "", listaProvas = [];
  const prefs = Armazem.ler("prefs", {});          // preferências do aluno (ocultar tempo, modo foco)
  const abertos = { nota: false, rascunho: false }; // lembra quais caixas estavam abertas entre as telas
  let opcoesAbertas = false;                         // celular: botões extras da barra (Ocultar tempo, Modo foco)
  const LEGENDA_MAPA = "Preenchida: respondida. Tracejada: marcada para revisão. Destacada: questão atual.";

  const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const erro = msg => { document.getElementById("conteudo").classList.remove("pag"); app.innerHTML = `<h1>Ops</h1><p>${esc(msg)}</p><p><a class="btn" href="provas.html">Voltar às provas</a></p>`; };
  let avisouArmazem = false, timerAviso = null;
  // Salva o andamento. Se o navegador não deixar gravar de forma permanente, avisa uma vez.
  const salvar = () => {
    if (!estado || estado.finalizado) return;
    if (!Armazem.gravar(CH_AND, estado) && !avisouArmazem) {
      avisouArmazem = true;
      falar("Atenção: este navegador não está deixando salvar o andamento de forma permanente (modo privado ou espaço cheio). Não feche esta aba antes de finalizar.");
    }
  };
  function falar(txt) {
    clearTimeout(timerAviso);                  // uma mensagem nova não some antes do tempo por causa da anterior
    aviso.textContent = txt; aviso.hidden = false;
    if (window.anunciar) anunciar(txt);          // leitor de tela (a caixa visível não tem role=status, para não ler duas vezes)
    timerAviso = setTimeout(() => { aviso.hidden = true; }, 8000);
  }

  /* Janela de confirmação acessível (<dialog>) */
  function confirmar(titulo, texto, botoes) {
    dlg.className = ""; dlg.removeAttribute("aria-label"); dlg.setAttribute("aria-labelledby", "dlg-t");
    dlg.innerHTML = `<h2 id="dlg-t">${esc(titulo)}</h2><p>${esc(texto)}</p><div class="acoes"></div>`;
    botoes.forEach(b => {
      const x = document.createElement("button");
      x.type = "button"; x.className = "btn" + (b.primario ? " btn--primary" : ""); x.textContent = b.rot;
      x.onclick = () => { dlg.close(); if (b.fn) b.fn(); };
      dlg.querySelector(".acoes").appendChild(x);
    });
    dlg.showModal();
  }

  /* ---- Carregamento ---- */
  const falha = codigo => { const e = new Error(codigo); e.codigo = codigo; return e; };
  const MENSAGENS = {
    "sem-treino": "Este treino não está mais salvo neste navegador. Monte um novo em Meu estudo.",
    "nao-encontrada": "Não encontramos esta prova. Ela pode ter sido removida, ou o endereço está incompleto.",
    "vazia": "Esta prova está sem questões.",
    "sem-resultado": "Para refazer só as erradas, finalize antes o simulado completo desta prova.",
    "rede": "Não foi possível carregar a prova. Se abriu o arquivo direto, use um servidor local (veja o README)."
  };
  function obterProva() {
    if (ID === "treino") {                                   // treino montado no "Meu estudo"
      const t = Armazem.ler("treino-ativo", null);
      return t ? Promise.resolve(t) : Promise.reject(falha("sem-treino"));
    }
    return fetch("data/provas.json").then(r => { if (!r.ok) throw falha("rede"); return r.json(); }).then(lista => {
      listaProvas = Array.isArray(lista) ? lista : [];
      const item = listaProvas.find(p => p.id === ID);
      // Enem, Linguagens com as duas línguas: prova montada na hora (js/linguas.js)
      if (!item && Linguas.partes(ID) && Linguas.partes(ID).lingua === "ambas") return Linguas.compor(ID, listaProvas).catch(e => { throw falha(e && e.message === "rede" ? "rede" : "nao-encontrada"); });
      if (!item) throw falha("nao-encontrada");
      return fetch(item.arquivo).then(r => { if (!r.ok) throw falha(r.status === 404 ? "nao-encontrada" : "rede"); return r.json(); });
    });
  }
  function carregar() {
    if (!ID) return erro("Nenhuma prova escolhida.");
    obterProva().then(p => {
      if (!p || !Array.isArray(p.questoes) || !p.questoes.length) throw falha("vazia");
      prova = p;
      if (MODO === "erradas") {            // refazer só o que errou ou deixou em branco
        const ant = Motor.normalizarEstado(Armazem.ler("resultado:" + ID, null), p);
        if (!ant) throw falha("sem-resultado");
        const nums = Motor.pontuar(ant, p).revisar.map(x => x.q.numero), total = p.questoes.length;
        p.questoes = p.questoes.filter(q => nums.includes(q.numero));
        if (!p.questoes.length) return erro("Você não errou nenhuma questão. Parabéns!");
        p.duracaoMinutos = Math.max(1, Math.round(p.duracaoMinutos * p.questoes.length / total));
        p.titulo += " (só as erradas)";
      }
      iniciar();
    }).catch(e => erro(MENSAGENS[e && e.codigo] || MENSAGENS.rede));
  }
  function iniciar() {
    document.title = prova.titulo + " | Treineiros";
    // normaliza: andamento de versão antiga, ou de quando o JSON da prova era diferente
    const salvo = Motor.normalizarEstado(Armazem.ler(CH_AND, null), prova);
    if (salvo && !salvo.finalizado) telaRetomar(salvo); else telaConfig();
  }

  /* ---- Telas iniciais: faixa com a capa do caderno e uma folha que sobe sobre ela ---- */
  const corpo = document.getElementById("conteudo");
  const modoAbertura = on => corpo.classList.toggle("pag", on);
  function rotuloBanca() {
    if (prova.misto === "Mescla") return "Simulado mesclado";
    if (prova.misto) return "Simulado misto " + prova.misto;
    if (prova.treino) return "Treino";
    return { ETEC: "Vestibulinho ETEC", FATEC: "Vestibular FATEC", Enem: "Enem" }[prova.banca] || prova.banca || "Simulado";
  }
  function materiasHtml() {
    const cont = {};
    prova.questoes.forEach(q => { if (q.materia) cont[q.materia] = (cont[q.materia] || 0) + 1; });
    const lista = Object.entries(cont).sort((x, y) => y[1] - x[1] || x[0].localeCompare(y[0], "pt"));
    if (lista.length < 2) return "";
    const mostra = lista.slice(0, 4), resto = lista.length - mostra.length;
    return `<ul class="abre__mats" aria-label="Questões por matéria">${mostra.map(([m, n]) => `<li>${esc(m)} <b>${n}</b></li>`).join("")}${resto ? `<li class="abre__mais">+ ${resto} ${resto === 1 ? "matéria" : "matérias"}</li>` : ""}</ul>`;
  }
  function faixaHtml() {
    const n = prova.questoes.length, tempo = Motor.duracaoTexto(prova.duracaoMinutos);
    const virgula = prova.titulo.indexOf(", ");
    const titulo = virgula > 0 ? `${esc(prova.titulo.slice(0, virgula))}, <em>${esc(prova.titulo.slice(virgula + 2))}</em>` : esc(prova.titulo);
    const sub = prova.treino ? (n === 1 ? "questão" : "questões") : prova.semestre ? `${prova.semestre}º semestre` : prova.area ? String(prova.area).replace(/\s*\(.*\)\s*$/, "") : prova.ano ? "" : "questões";
    const grande = prova.treino ? n : (prova.ano || n);
    const lead = [prova.dataExame ? `Prova aplicada em ${Render.dataBr(prova.dataExame)}` : "", prova.fonte && !prova.treino ? `gabarito oficial do ${esc(prova.fonte)}` : "", prova.tema ? `tema: ${esc(prova.tema)}` : ""].filter(Boolean).join(" · ");
    const trilha = prova.treino ? `<a href="estudo.html">Meu estudo</a> › ${esc(rotuloBanca())}` : `<a href="provas.html">Provas</a> › ${esc(prova.banca)}${prova.ano ? " " + prova.ano : ""}`;
    return `<section class="faixa abre" aria-labelledby="abre-t"><div class="faixa__in abre__in">
      <div class="abre__capa" aria-hidden="true">
        <span class="abre__banca">${esc(rotuloBanca())}</span>
        <span class="abre__ano"><b>${esc(grande)}</b>${sub ? `<i>${esc(sub)}</i>` : ""}</span>
        <span class="abre__pe"><span>${n} ${n === 1 ? "questão" : "questões"}</span><span>${esc(tempo)}</span></span>
      </div>
      <div class="abre__texto">
        <nav class="trilha--faixa" aria-label="Você está em">${trilha}</nav>
        <h1 id="abre-t">${titulo}</h1>
        ${lead ? `<p class="faixa__lead">${lead}</p>` : ""}
        ${materiasHtml()}
      </div></div></section>`;
  }
  function telaRetomar(salvo) {
    const n = prova.questoes.length;
    modoAbertura(true);
    app.innerHTML = `${faixaHtml()}<div class="abre__folha-wrap"><div class="abre__folha">
      <h2>Você parou <em>no meio</em></h2>
      <p class="abre__resumo">Questão ${salvo.atual + 1} de ${n}, ${salvo.tempoRestanteSeg === null ? "tempo gasto " + Motor.fmt(salvo.tempoGastoSeg) : "faltam " + Motor.fmt(salvo.tempoRestanteSeg)}.</p>
      <div class="abre__pe-form"><p>O andamento fica salvo neste aparelho.</p>
      <div class="botoes"><button class="btn btn--primary" id="b-cont" type="button">Continuar de onde parou</button> <button class="btn" id="b-novo" type="button">Recomeçar</button></div></div>
    </div></div>`;
    document.getElementById("b-cont").onclick = () => { estado = salvo; estado.pausado = false; ligar(); };
    document.getElementById("b-novo").onclick = () => confirmar("Recomeçar?", "O andamento salvo será apagado.", [
      { rot: "Recomeçar", primario: true, fn: () => { Armazem.apagar(CH_AND); Armazem.apagar(CH_RAS); telaConfig(); } }, { rot: "Voltar" }]);
  }
  // caderno oficial: link direto da prova (linkProva) ou a página de provas da banca (Config.fontesOficiais)
  const fonteOf = () => (Config.fontesOficiais || {})[prova.banca] || null;
  const linkPdf = () => prova.linkProva || (fonteOf() && fonteOf().url) || "";
  const corCaderno = () => prova.caderno ? ` Use o caderno <strong>${esc(prova.caderno)}</strong>: a numeração das questões aqui segue esse caderno.` : "";
  const linkCaderno = () => linkPdf() ? ` <a href="${esc(linkPdf())}" target="_blank" rel="noopener">${prova.linkProva ? "Abrir o caderno oficial (PDF)" : "Baixar o caderno no site " + "do " + esc(fonteOf().nome)}</a>.` : "";
  // cronômetro: cartões com bolha
  const opcao = (nome, valor, titulo, desc, marcado) =>
    `<label class="cfg__op"><input type="radio" name="${nome}" value="${valor}"${marcado ? " checked" : ""}><span><strong>${titulo}</strong><span class="cfg__desc">${desc}</span></span></label>`;
  // correção e formato: segmento de duas opções (rádios de verdade, para teclado e leitor de tela)
  const segmento = (nome, ops) => `<div class="segmento cfg__seg">${ops.map(([v, t, marcado]) =>
    `<label><input type="radio" name="${nome}" value="${v}"${marcado ? " checked" : ""}><span>${t}</span></label>`).join("")}</div>`;
  // de onde veio o gabarito, quando não é o documento oficial publicado pela banca no próprio site
  function gabaritoFonteHtml() {
    const f = prova.fonteGabarito; if (!f) return "";
    const nome = f.url ? `<a href="${esc(f.url)}" target="_blank" rel="noopener">${esc(f.nome)}</a>` : esc(f.nome);
    return f.oficial
      ? `<p class="cfg__meta">Fonte do gabarito: ${nome}.</p>`
      : `<p class="aviso">O Inep não publica o gabarito desta edição no site oficial. Fonte do gabarito usado aqui: ${nome}. Se encontrar alguma resposta diferente do oficial, use o botão “Reportar erro”.</p>`;
  }
  // Enem, Linguagens: escolha da língua estrangeira (Inglês, Espanhol ou as duas)
  function linguaHtml() {
    if (MODO !== "completo" || !Linguas.temEscolha(prova.id, listaProvas)) return "";
    const atual = Linguas.partes(prova.id).lingua;
    return `<fieldset class="cfg__lingua"><legend class="rotulo">Língua estrangeira</legend>
      ${segmento("lingua", [["ingles", "Inglês", atual === "ingles"], ["espanhol", "Espanhol", atual === "espanhol"], ["ambas", "As duas", atual === "ambas"]])}
      <p class="cfg__dica">${atual === "ambas" ? "As 5 questões de Inglês e as 5 de Espanhol, mais as 40 comuns: 50 questões." : "As 5 primeiras questões são de " + Linguas.NOMES[atual] + "; as outras 40 são comuns às duas versões."}</p></fieldset>`;
  }
  function telaConfig() {
    const oficial = Motor.duracaoTexto(prova.duracaoMinutos), n = prova.questoes.length;
    const anuladas = prova.questoes.filter(q => q.gabarito === "ANULADA").length;
    const ilustra = prova.imagensProva && prova.imagensProva.apresentacao;
    const DICAS = {
      imediata: "Mostra se acertou e explica na hora. A resposta fica travada.",
      final: "Só mostra o resultado no final. Você pode trocar as respostas até finalizar.",
      tela: "Uma questão por vez, com enunciado, figuras e ferramentas.",
      cartao: "Você faz a prova no papel (caderno oficial impresso) e só marca as respostas aqui. A correção sai no final." + corCaderno() + linkCaderno()
    };
    modoAbertura(true);
    app.innerHTML = `${faixaHtml()}<div class="abre__folha-wrap">
      <form id="cfg" class="cfg abre__folha">
      ${gabaritoFonteHtml()}
      ${prova.apresentacao ? `<div class="cfg__apres">${ilustra ? Render.figura(ilustra, false, true) : ""}${prova.apresentacao}</div>` : ""}
      ${anuladas ? `<p class="aviso">${anuladas === 1 ? "Uma questão desta prova foi anulada" : `${anuladas} questões desta prova foram anuladas`} pela banca: ${prova.banca === "Enem" ? (anuladas === 1 ? "como no Enem, ela fica fora da conta de acertos" : "como no Enem, elas ficam fora da conta de acertos") : (anuladas === 1 ? "ela vale ponto para todos" : "elas valem ponto para todos") + ", como no dia da prova"}. A justificativa aparece na correção.</p>` : ""}
      <h2>Como você quer <em>fazer?</em></h2>
      ${linguaHtml()}
      <fieldset><legend class="rotulo">Cronômetro</legend><div class="cfg__ops">
      ${opcao("modo", "oficial", (prova.misto ? "Tempo da prova " + esc(prova.misto) : prova.treino ? "Tempo sugerido" : prova.composta ? "Tempo ajustado" : "Oficial") + " · " + oficial,
        prova.rotuloTempo ? esc(prova.rotuloTempo) : prova.treino ? `${Config.minutosPorQuestaoTreino} min por questão` : "A duração da prova de verdade", true)}
      ${opcao("modo", "personalizado", "Personalizado", '<input type="number" id="min" class="campo" min="1" max="600" value="60" aria-label="Minutos do cronômetro personalizado"> minutos', false)}
      ${opcao("modo", "nenhum", "Sem cronômetro", "No seu ritmo; o tempo gasto é anotado", false)}
      </div></fieldset>
      <div class="cfg__duas">
      <fieldset><legend class="rotulo">Correção</legend>
      ${segmento("correcao", [["imediata", "Modo estudo", true], ["final", "Modo prova", false]])}
      <p class="cfg__dica" id="d-correcao" aria-live="polite">${DICAS.imediata}</p></fieldset>
      ${prova.treino || prova.composta ? "" : `<fieldset><legend class="rotulo">Formato</legend>
      ${segmento("formato", [["tela", "Na tela", true], ["cartao", "Cartão-resposta", false]])}
      <p class="cfg__dica" id="d-formato" aria-live="polite">${DICAS.tela}</p></fieldset>`}
      </div>
      <div class="abre__pe-form"><p id="cfg-resumo"></p>
      <button class="btn btn--primary btn--grande" type="submit">Começar a prova <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></button></div>
      </form></div>`;
    const form = document.getElementById("cfg"), min = document.getElementById("min");
    // trocar a língua estrangeira abre a outra versão da prova (cada uma guarda o próprio andamento)
    form.querySelectorAll("[name=lingua]").forEach(r => r.addEventListener("change", () => {
      const pt = Linguas.partes(prova.id); prefs.lingua = r.value; Armazem.gravar("prefs", prefs);
      location.href = "simulado.html?id=" + encodeURIComponent(pt.base + "-" + r.value);
    }));
    const resumo = () => {
      const modo = form.elements.modo.value, m = parseInt(min.value, 10);
      const tempo = modo === "oficial" ? "em " + oficial : modo === "personalizado" ? (m >= 1 ? `em ${Motor.duracaoTexto(m)}` : "no tempo que você escolher") : "sem cronômetro";
      const corr = form.elements.correcao.value === "imediata" ? "com correção na hora" : "com o resultado no final";
      document.getElementById("cfg-resumo").innerHTML = `<b>${n} ${n === 1 ? "questão" : "questões"} ${tempo}</b>, ${corr}. <span>Dá para pausar e continuar depois.</span>`;
      document.getElementById("d-correcao").textContent = DICAS[form.elements.correcao.value];
      const df = document.getElementById("d-formato"); if (df) df.innerHTML = DICAS[form.elements.formato.value];
    };
    min.addEventListener("input", () => { form.elements.modo.value = "personalizado"; resumo(); });
    min.addEventListener("focus", () => { form.elements.modo.value = "personalizado"; resumo(); });
    // no cartão-resposta a correção é sempre no final
    form.addEventListener("change", e => {
      if (e.target.name === "formato") {
        const cartao = form.elements.formato.value === "cartao";
        if (cartao) form.elements.correcao.value = "final";
        form.querySelector('[name=correcao][value=imediata]').disabled = cartao;
      }
      resumo();
    });
    resumo();
    form.addEventListener("submit", e => {
      e.preventDefault();
      const modo = form.elements.modo.value, m = parseInt(min.value, 10);
      if (modo === "personalizado" && !(m >= 1 && m <= 600)) { falar("Digite um tempo entre 1 e 600 minutos."); min.focus(); return; }
      estado = Motor.novoEstado(prova, modo, m, form.elements.correcao.value, form.elements.formato ? form.elements.formato.value : "tela");
      salvar(); ligar();
    });
  }

  /* ---- Cronômetro (usa o relógio real, então não atrasa com a aba em segundo plano) ---- */
  function ligar() {
    modoAbertura(false);
    clearInterval(relogio);
    ultimo = Date.now(); salvoEm = ultimo;
    relogio = setInterval(tique, 1000);
    renderProva("#qt");
  }
  const MAX_SALTO = 300; // segundos. Um salto maior que isso = aparelho dormiu ou a aba foi congelada.
  function tique() {
    if (!estado || estado.pausado || estado.finalizado) return;
    const agora = Date.now(), dt = Math.round((agora - ultimo) / 1000);
    if (dt < 1) return;
    if (dt > MAX_SALTO) {
      // Sem isso, fechar o notebook no meio do simulado e voltar no dia seguinte encerraria a prova
      // por tempo (ou somaria horas a uma questão). Tratamos como pausa: esse intervalo não conta.
      ultimo = agora; pausar();
      falar("O simulado foi pausado porque o aparelho ficou inativo. Esse intervalo não contou no tempo.");
      return;
    }
    ultimo += dt * 1000;
    const antes = estado.tempoRestanteSeg, acabou = Motor.tickear(estado, dt);
    atualizarRelogio();
    if (agora - salvoEm >= 5000) { salvar(); salvoEm = agora; }
    if (antes !== null) {
      if (antes > 600 && estado.tempoRestanteSeg <= 600) falar("Faltam 10 minutos.");
      if (antes > 60 && estado.tempoRestanteSeg <= 60) falar("Falta 1 minuto.");
    }
    if (acabou) { falar("Tempo esgotado."); finalizar(true); }
  }
  function atualizarRelogio() {
    const t = document.getElementById("tempo");
    if (!t) return;
    t.setAttribute("aria-hidden", !!prefs.ocultarTempo);
    t.textContent = prefs.ocultarTempo ? "••:••" : Motor.fmt(estado.tempoRestanteSeg === null ? estado.tempoGastoSeg : estado.tempoRestanteSeg);
  }

  /* ---- Tela da prova ---- */
  function responder(q, letra) {
    const nova = !estado.respostas[q.numero];
    if (!Motor.responder(estado, q.numero, letra)) return;
    if (nova) Registro.somarAtividade(1);                      // conta para a meta e a sequência do dia
    salvar();
    renderProva(Motor.revelado(estado, q.numero) ? "#expl" : `[data-letra="${letra}"]`);
  }
  /* Cabeçalho da prova (comum à tela da questão e ao cartão-resposta), como o topo de uma folha de respostas:
     linha 1: nome curto da prova, onde você está e o relógio em pílula; linha 2: progresso em segmentos e as ações. */
  function tituloCurto() {
    if (prova.semestre) return `${prova.banca} ${prova.ano} · ${prova.semestre}º semestre`;
    if (prova.banca === "Enem" && prova.area) return `Enem ${prova.ano} · ${String(prova.area).replace(/\s*\(.*\)\s*$/, "")}`;
    return prova.titulo || "Simulado";
  }
  const ICO_PAUSA = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M9 6v12M15 6v12"/></svg>';
  const ICO_OPC = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><circle cx="5" cy="12" r="1.8"/><circle cx="12" cy="12" r="1.8"/><circle cx="19" cy="12" r="1.8"/></svg>';
  const ICO_ANT = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 5l-7 7 7 7"/></svg>';
  const ICO_PROX = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 5l7 7-7 7"/></svg>';
  const ICO_MAPA = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="6" cy="6" r="2.2"/><circle cx="12" cy="6" r="2.2"/><circle cx="18" cy="6" r="2.2"/><circle cx="6" cy="12" r="2.2"/><circle cx="12" cy="12" r="2.2" fill="currentColor"/><circle cx="18" cy="12" r="2.2"/><circle cx="6" cy="18" r="2.2"/><circle cx="12" cy="18" r="2.2"/><circle cx="18" cy="18" r="2.2"/></svg>';
  const ICO_MARCA = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M6 21V4h11l-2 4 2 4H6"/></svg>';
  function barraHtml(onde, prog) {
    return `<div class="barra${opcoesAbertas ? " barra--opcoes" : ""}">
        <div class="barra__linha">
          <div class="barra__id"><p class="barra__prova">${esc(tituloCurto())}</p><p class="barra__onde">${onde}</p></div>
          <div class="barra__tempo"><span class="sr">${estado.tempoRestanteSeg === null ? "Tempo gasto" : "Tempo restante"}: </span><span id="tempo" role="timer"></span></div>
        </div>
        <div class="barra__linha barra__linha--2">
          <div class="barra__prog" id="prog-c">${prog}</div>
          <div class="barra__acoes">
            <button type="button" class="btn btn-icone barra__opc" id="b-opc" aria-expanded="${!!opcoesAbertas}" aria-controls="b-ocultar b-foco" title="Opções">${ICO_OPC}<span class="sr">Opções</span></button>
            <button type="button" class="btn barra__extra" id="b-ocultar" aria-pressed="${!!prefs.ocultarTempo}">Ocultar tempo</button>
            <button type="button" class="btn barra__extra" id="b-foco" aria-pressed="${!!prefs.foco}">Modo foco</button>
            <button type="button" class="btn btn-icone" id="b-pausar" title="Pausar">${ICO_PAUSA}<span class="barra__rot">Pausar</span></button>
            <button type="button" class="btn btn--primary" id="b-fim">Finalizar</button>
          </div>
        </div>
      </div>`;
  }
  function ligarBarra(rerender) {
    document.getElementById("b-opc").onclick = () => { opcoesAbertas = !opcoesAbertas; rerender("#b-opc"); };
    document.getElementById("b-ocultar").onclick = () => { prefs.ocultarTempo = !prefs.ocultarTempo; Armazem.gravar("prefs", prefs); rerender("#b-ocultar"); };
    document.getElementById("b-foco").onclick = () => { prefs.foco = !prefs.foco; Armazem.gravar("prefs", prefs); rerender("#b-foco"); };
    document.getElementById("b-pausar").onclick = pausar;
    document.getElementById("b-fim").onclick = tentarFinalizar;
    atualizarRelogio();
  }
  /* Progresso em segmentos, como as linhas da folha: cheios = respondidas, o de latão = onde você está.
     Até 30 questões, um segmento por questão; acima disso, os segmentos agrupam questões. */
  const progHtml = (feitas, n, atual) => {
    const S = Math.min(n, 30), cheios = Math.round(feitas / n * S);
    const aqui = atual === undefined ? -1 : Math.min(S - 1, Math.floor(atual / n * S));
    let seg = "";
    for (let i = 0; i < S; i++) seg += `<i class="${i === aqui ? "aqui" : i < cheios ? "feito" : ""}"></i>`;
    return `<div class="prog"><div class="progresso progresso--seg" role="progressbar" aria-label="Questões respondidas" aria-valuemin="0" aria-valuemax="${n}" aria-valuenow="${feitas}" aria-valuetext="${feitas} de ${n} respondidas">${seg}</div><p>${feitas} de ${n} respondidas</p></div>`;
  };

  /* ---- Cartão-resposta: a prova é feita no papel; aqui só as bolinhas ---- */
  function renderCartao(foco) {
    tela = "cartao";
    document.body.classList.toggle("foco", !!prefs.foco);
    const n = prova.questoes.length;
    const linhas = prova.questoes.map(q => {
      const num = (q.origem && q.origem.numeroOriginal) || q.numero, resp = estado.respostas[q.numero];
      return `<li><fieldset class="cartao__q"><legend>Questão ${num}</legend>${Object.keys(q.alternativas).map(l =>
        `<label class="bolha"><input type="radio" name="q${q.numero}" value="${l}"${resp === l ? " checked" : ""}><span aria-hidden="true">${l}</span><span class="sr">${l}</span></label>`).join("")}</fieldset></li>`;
    }).join("");
    app.innerHTML = barraHtml("Cartão-resposta", progHtml(Motor.respondidas(estado, prova), n)) + `
      <section class="cartao-folha" aria-labelledby="ct"><h2 id="ct" tabindex="-1">Cartão-resposta</h2>
      <p>Resolva no caderno impresso e marque aqui.${corCaderno() || " Os números são os mesmos do caderno."}${linkCaderno()}</p>
      <ol class="cartao">${linhas}</ol></section>`;
    app.querySelectorAll(".cartao input").forEach(r => r.addEventListener("change", () => {
      const num = +r.name.slice(1), nova = !estado.respostas[num];
      if (!Motor.responder(estado, num, r.value)) return;
      if (nova) Registro.somarAtividade(1);
      salvar();
      document.getElementById("prog-c").innerHTML = progHtml(Motor.respondidas(estado, prova), n);   // sem redesenhar tudo: o foco fica na bolinha
    }));
    ligarBarra(renderCartao);
    if (foco) { const f = app.querySelector(foco); if (f) f.focus(); }
  }

  function renderProva(foco) {
    if (estado.pausado) return renderPausa();
    if (estado.config.formato === "cartao") return renderCartao(foco === "#qt" ? "#ct" : foco);
    tela = "prova";
    document.body.classList.toggle("foco", !!prefs.foco);
    const n = prova.questoes.length, q = prova.questoes[estado.atual], r = Registro.ref(prova, q);
    const resp = estado.respostas[q.numero], anulada = q.gabarito === "ANULADA", rev = Motor.revelado(estado, q.numero);
    const feitas = Motor.respondidas(estado, prova), marcada = estado.marcadas.includes(q.numero);
    const chute = (estado.chutes || []).includes(q.numero), elims = (estado.eliminadas || {})[q.numero] || [];
    const alts = Object.keys(q.alternativas).map(l => {
      let cls = "alt", st = "";
      if (rev && !anulada) {
        if (l === q.gabarito) { cls += " is-correta"; st = resp === l ? "Você acertou" : "Gabarito"; }
        else if (l === resp) { cls += " is-errada"; st = "Errada"; }
      } else if (resp === l) cls += " is-selecionada";
      const elim = !rev && elims.includes(l);
      if (elim) cls += " is-eliminada";
      const risca = rev ? "" : `<button type="button" class="alt-risca" data-risca="${l}" aria-pressed="${elim}" aria-label="Eliminar alternativa ${l}" title="Eliminar alternativa">✕</button>`;
      // aria-pressed diz ao leitor de tela qual alternativa está marcada (a cor sozinha não diz)
      return `<div class="alt-linha"><button type="button" class="${cls}" data-letra="${l}"${rev ? ' aria-disabled="true"' : ` aria-pressed="${resp === l}"`}><span class="alt__letra">${l}</span><span>${Render.alternativa(q, l)}${elim ? '<span class="sr"> (eliminada)</span>' : ""}</span><span class="alt__status">${st}</span></button>${risca}</div>`;
    }).join("");
    // explicação, com anulação/retificação; o foco vai para ela depois de responder (id="expl")
    const expl = rev ? Render.explicacao(q, { id: "expl" }) : "";
    const mapa = prova.questoes.map((x, i) => {
      const resp2 = estado.respostas[x.numero], m = estado.marcadas.includes(x.numero), atual = i === estado.atual;
      return `<li><button type="button" data-i="${i}" class="${resp2 ? "is-resp" : ""} ${m ? "is-marca" : ""} ${atual ? "is-atual" : ""}"${atual ? ' aria-current="true"' : ""} aria-label="Questão ${i + 1}, ${resp2 ? "respondida" : "em branco"}${m ? ", marcada para revisão" : ""}">${i + 1}</button></li>`;
    }).join("");

    app.innerHTML = barraHtml(`Questão ${estado.atual + 1} de ${n}`, progHtml(feitas, n, estado.atual)) + `
      <section class="questao" aria-labelledby="qt">
        <h2 id="qt" class="q-tit q-tit--folha" tabindex="-1" aria-label="Questão ${estado.atual + 1} de ${n}"><span class="q-tit__n" aria-hidden="true">${String(estado.atual + 1).padStart(2, "0")}</span></h2>
        <p class="origem">${esc(Registro.rotuloOrigem(prova, q))}</p>
        ${Render.tags(q).replace("</p>", `${marcada ? ' <span class="tag">Marcada para revisão</span>' : ""}${chute ? ' <span class="tag">Chute</span>' : ""}</p>`)}
        ${Render.enunciado(q, { zoom: true, ja: true })}
        <div role="group" aria-label="Alternativas">${alts}</div>${expl}
        <div class="nav nav--principal" role="group" aria-label="Navegação entre questões">
          <button type="button" class="btn nav__ant" id="b-ant"${estado.atual === 0 ? " disabled" : ""} aria-label="Questão anterior">${ICO_ANT}<span class="nav__rot">Anterior</span></button>
          <button type="button" class="btn nav__mapa" id="b-mapa" aria-haspopup="dialog" aria-label="Mapa de questões, você está na ${estado.atual + 1} de ${n}">${ICO_MAPA}<span aria-hidden="true">${estado.atual + 1}/${n}</span></button>
          <button type="button" class="btn nav__marca" id="b-marca" aria-pressed="${marcada}" aria-label="Rever depois: marcar para revisão">${ICO_MARCA}<span aria-hidden="true"><span class="nav__curto">Rever</span><span class="nav__longo">Rever depois</span></span></button>
          <button type="button" class="btn btn--primary nav__prox" id="b-prox"${estado.atual === n - 1 ? " disabled" : ""}>Próxima${ICO_PROX}</button>
        </div>
        <div class="nav nav--extra">
          ${rev ? "" : `<button type="button" class="btn" id="b-chute" aria-pressed="${chute}">Foi chute</button>`}
          <button type="button" class="btn btn--ghost" id="b-rep">Reportar erro</button>
        </div>
        <details class="nota" id="d-nota"><summary>Minhas anotações</summary><textarea id="nota" class="campo" rows="3" aria-label="Anotações sobre esta questão"></textarea></details>
        <details class="nota" id="d-ras"><summary>Rascunho</summary><textarea id="rascunho" class="campo" rows="6" aria-label="Rascunho da prova"></textarea></details>
        <details class="atalhos"><summary>Atalhos de teclado</summary><p>A a E: responder. Shift + A a E: eliminar alternativa. Setas: navegar. M: marcar para revisão. P: pausar ou retomar.</p></details>
      </section>
      <nav class="mapa-bloco" aria-label="Mapa de questões"><h3>Mapa de questões</h3><ul class="mapa">${mapa}</ul>
        <p class="legenda">${LEGENDA_MAPA}</p></nav>`;

    /* anotações (por questão) e rascunho (da prova): salvos a cada tecla */
    const dn = document.getElementById("d-nota"), dr = document.getElementById("d-ras"), tn = document.getElementById("nota"), tr = document.getElementById("rascunho");
    tn.value = Registro.nota(r); tr.value = Armazem.ler(CH_RAS, "");
    dn.open = abertos.nota || !!tn.value; dr.open = abertos.rascunho || !!tr.value;
    dn.addEventListener("toggle", () => { abertos.nota = dn.open; });
    dr.addEventListener("toggle", () => { abertos.rascunho = dr.open; });
    tn.addEventListener("input", () => Registro.gravarNota(r, tn.value));
    tr.addEventListener("input", () => Armazem.gravar(CH_RAS, tr.value));

    app.querySelectorAll(".alt").forEach(b => b.addEventListener("click", () => responder(q, b.dataset.letra)));
    app.querySelectorAll(".alt-risca").forEach(b => b.addEventListener("click", () => {
      Motor.alternarEliminada(estado, q.numero, b.dataset.risca); salvar(); renderProva(`[data-risca="${b.dataset.risca}"]`);
    }));
    app.querySelectorAll(".figura-btn").forEach(b => b.addEventListener("click", () => ampliar(b.dataset.src, b.dataset.alt)));
    app.querySelectorAll("img.figura").forEach(img => img.addEventListener("error", () => {   // figura que não carregou
      const p = document.createElement("p"); p.className = "aviso";
      p.textContent = "Não foi possível carregar uma figura desta questão. Use \u201cReportar erro\u201d para avisar.";
      (img.closest(".fig") || img).replaceWith(p);
    }));
    app.querySelectorAll(".mapa button").forEach(b => b.addEventListener("click", () => irPara(+b.dataset.i)));
    document.getElementById("b-mapa").onclick = () => abrirMapa(mapa);
    document.getElementById("b-ant").onclick = () => irPara(estado.atual - 1);
    document.getElementById("b-prox").onclick = () => irPara(estado.atual + 1);
    document.getElementById("b-marca").onclick = () => { Motor.alternarMarca(estado, q.numero); salvar(); renderProva("#b-marca"); };
    const bc = document.getElementById("b-chute");
    if (bc) bc.onclick = () => { Motor.alternarChute(estado, q.numero); salvar(); renderProva("#b-chute"); };
    document.getElementById("b-rep").onclick = () => Reportar.abrir(prova, q).then(res => falar(Reportar.mensagem(res)));
    ligarBarra(renderProva);
    Formulas.renderizar(app);
    if (foco) { const f = app.querySelector(foco); if (f) f.focus(); }
  }
  function irPara(i) {
    if (i < 0 || i >= prova.questoes.length) return;
    estado.atual = i; salvar(); renderProva("#qt");
  }

  /* ---- Mapa de questões em janela (no celular o mapa da página fica escondido) ---- */
  function abrirMapa(mapa) {
    dlg.className = "dlg-mapa"; dlg.removeAttribute("aria-label"); dlg.setAttribute("aria-labelledby", "dlg-t");
    dlg.innerHTML = `<h2 id="dlg-t">Mapa de questões</h2><p class="legenda">${Motor.respondidas(estado, prova)} de ${prova.questoes.length} respondidas. ${LEGENDA_MAPA}</p>
      <ul class="mapa">${mapa}</ul><div class="acoes"><button type="button" class="btn" id="b-fechar">Fechar</button></div>`;
    dlg.querySelectorAll(".mapa button").forEach(b => b.addEventListener("click", () => { dlg.close(); irPara(+b.dataset.i); }));
    document.getElementById("b-fechar").onclick = () => dlg.close();
    dlg.showModal();
    const atual = dlg.querySelector("[aria-current]"); if (atual) atual.focus();
  }

  /* ---- Pausa ---- */
  function pausar() { estado.pausado = true; salvar(); renderPausa(); }
  function retomar() { estado.pausado = false; ultimo = Date.now(); salvar(); renderProva("#qt"); }
  function renderPausa() {
    tela = "pausa";
    document.body.classList.remove("foco");
    app.innerHTML = `<section class="pausa"><h1>Simulado pausado</h1>
      <p>Seu tempo está parado e nada foi perdido. Ao retomar, você volta para a questão ${estado.atual + 1}.</p>
      <p>${estado.tempoRestanteSeg === null ? "Tempo gasto" : "Tempo restante"}: <strong>${Motor.fmt(estado.tempoRestanteSeg === null ? estado.tempoGastoSeg : estado.tempoRestanteSeg)}</strong></p>
      <button type="button" class="btn btn--primary" id="b-ret">Retomar</button></section>`;
    const b = document.getElementById("b-ret"); b.focus();
    b.onclick = retomar;
  }

  /* ---- Ampliar figura ---- */
  // Tela cheia no celular; "Aumentar" dobra o tamanho e deixa rolar pela figura (tirinhas, mapas, gráficos)
  function ampliar(src, alt) {
    dlg.className = "dlg-zoom"; dlg.removeAttribute("aria-labelledby"); dlg.setAttribute("aria-label", "Figura ampliada");
    dlg.innerHTML = `<div class="zoom-area"><img class="zoom" src="${esc(src)}" alt="${esc(alt || "Figura")}"></div>
      <p class="zoom-desc">${esc(alt || "")}</p>
      <div class="acoes"><button type="button" class="btn" id="b-mais" aria-pressed="false">Aumentar</button><button type="button" class="btn btn--primary" id="b-fechar">Fechar</button></div>`;
    const area = dlg.querySelector(".zoom-area"), mais = document.getElementById("b-mais");
    mais.onclick = () => { const g = area.classList.toggle("grande"); mais.setAttribute("aria-pressed", g); mais.textContent = g ? "Tamanho normal" : "Aumentar"; };
    document.getElementById("b-fechar").onclick = () => dlg.close();
    dlg.showModal();
  }

  /* ---- Atalhos de teclado ---- */
  const anunciarMarca = n => { if (window.anunciar) anunciar(estado.marcadas.includes(n) ? "Marcada para revisão." : "Marca de revisão removida."); };
  document.addEventListener("keydown", e => {
    // e.key pode vir vazio (ex.: preenchimento automático do Chrome)
    if (!e.key || !estado || estado.finalizado || dlg.open || e.ctrlKey || e.metaKey || e.altKey) return;
    if (/^(INPUT|TEXTAREA|SELECT)$/.test(e.target.tagName)) return;
    const k = e.key.toLowerCase();
    if (tela === "pausa") { if (k === "p") retomar(); return; }
    if (tela === "cartao") { if (k === "p") pausar(); return; }
    if (tela !== "prova") return;
    const q = prova.questoes[estado.atual], L = k.toUpperCase();
    if (k.length === 1 && "abcde".includes(k) && q.alternativas[L]) {
      // o foco fica no controle correspondente, para o teclado e o leitor de tela não "voltarem ao topo"
      if (e.shiftKey) { if (!Motor.revelado(estado, q.numero)) { Motor.alternarEliminada(estado, q.numero, L); salvar(); renderProva(`[data-risca="${L}"]`); } }
      else responder(q, L);
    } else if (k === "arrowright") irPara(estado.atual + 1);
    else if (k === "arrowleft") irPara(estado.atual - 1);
    else if (k === "m") { Motor.alternarMarca(estado, q.numero); salvar(); renderProva("#b-marca"); anunciarMarca(q.numero); }
    else if (k === "p") pausar();
  });

  /* ---- Finalizar ---- */
  function tentarFinalizar() {
    const pend = Motor.pendentes(estado, prova);
    if (!pend.length) return confirmar("Finalizar simulado", "Todas as questões foram respondidas. Finalizar agora?",
      [{ rot: "Finalizar", primario: true, fn: () => finalizar(false) }, { rot: "Voltar" }]);
    confirmar("Questões em branco", `Você deixou ${pend.length} ${pend.length === 1 ? "questão" : "questões"} em branco. Deseja finalizar mesmo assim?`, [
      { rot: "Ir para a primeira em branco", fn: () => irPara(prova.questoes.findIndex(q => q.numero === pend[0])) },
      { rot: "Finalizar mesmo assim", primario: true, fn: () => finalizar(false) },
      { rot: "Voltar" }]);
  }
  function finalizar(porTempo) {
    // Evita finalizar duas vezes (ex.: o tempo acaba com a janela "Finalizar?" aberta e o aluno clica nela):
    // contaria duas vezes no histórico e no caderno de erros.
    if (!estado || estado.finalizado) return;
    clearInterval(relogio);
    estado.finalizado = true; estado.pausado = false;
    Armazem.apagar(CH_AND); Armazem.apagar(CH_RAS);         // apaga antes: libera espaço se o armazenamento estiver cheio
    Armazem.gravar(CH_RES, estado);
    // Um resultado completo novo torna obsoleto o "só as erradas" anterior (as erradas agora são outras).
    if (MODO === "completo") { Armazem.apagar("andamento:" + ID + ":erradas"); Armazem.apagar("resultado:" + ID + ":erradas"); Armazem.apagar("rascunho:" + ID + ":erradas"); }
    const p = Motor.pontuar(estado, prova), chutes = estado.chutes || [];
    if (window.contarEvento) contarEvento(prova.treino ? "treino-concluido" : "prova-concluida/" + String(prova.banca).toLowerCase());
    Registro.registrarResultado(prova.questoes.map(q => {            // alimenta o caderno de erros
      const resp = estado.respostas[q.numero];
      const status = q.gabarito === "ANULADA" ? "anulada" : !resp ? "branco" : resp === q.gabarito ? "acerto" : "erro";
      return { ref: Registro.ref(prova, q), materia: q.materia, assunto: q.assunto || "", status: status, chute: chutes.includes(q.numero) };
    }));
    const h = Armazem.ler("historico", []);
    h.unshift({ provaId: ID + SUF, titulo: prova.titulo, banca: prova.banca, treino: !!prova.treino, data: new Date().toISOString(),
      acertos: p.acertos, total: p.total, percentual: p.percentual, tempoGastoSeg: estado.tempoGastoSeg, porTempo: !!porTempo, porMateria: p.porMateria, porAssunto: p.porAssunto });
    Armazem.gravar("historico", h.slice(0, 50));
    location.href = "resultado.html?id=" + encodeURIComponent(ID) + (MODO === "erradas" ? "&modo=erradas" : "");
  }

  document.addEventListener("visibilitychange", () => { if (document.hidden) salvar(); });
  window.addEventListener("pagehide", salvar);
  carregar();
})();
