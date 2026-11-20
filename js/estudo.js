/* Meu estudo: painel do dia, revisão espaçada, plano, treino por matéria, estatísticas e caderno de erros. */
(function () {
  const $ = s => document.querySelector(s);
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const dizer = txt => { $("#status").textContent = txt; };
  const ir = url => { location.href = url; };
  const dataBr = s => typeof s === "string" ? s.split("-").reverse().join("/") : "—";

  let indice = [], idx = new Set(), listaProvas = [];
  const bancaDe = {};                // id da prova → banca

  /* ---- Hoje: contagem regressiva, meta diária e sequência, em três cartões ---- */
  const DIAS = ["dom", "seg", "ter", "qua", "qui", "sex", "sáb"];
  function faixa(meta, feitas, seq, alvo, d) {
    const hojeTxt = new Date().toLocaleDateString("pt-BR", { weekday: "long", day: "numeric", month: "long" });
    $("#hoje-data").textContent = hojeTxt.charAt(0).toUpperCase() + hojeTxt.slice(1);
    const pend = Registro.pendentesHoje().length;
    const itens = [];
    if (alvo && d > 0) itens.push([`${esc(alvo.nome)} em`, `${d} ${d === 1 ? "dia" : "dias"}`]);
    itens.push(["Hoje", Rotina.metaHoje().folga ? `${feitas} · folga` : `${feitas} de ${meta.questoesDia}`]);
    itens.push(["Seguidos", `${seq} ${seq === 1 ? "dia" : "dias"}`]);
    if (pend) itens.push(["Para revisar", String(pend)]);
    $("#faixa-num").innerHTML = itens.map(([t, v]) => `<div><dt>${t}</dt><dd>${v}</dd></div>`).join("");
  }
  function painel() {
    const mh = Rotina.metaHoje();                                   // com rotina, a meta é a do dia (0 na folga)
    const meta = { questoesDia: Math.max(1, mh.q) };                 // evita divisão por zero
    const ativ = Armazem.ler("atividade", {}), feitas = ativ[Registro.hoje()] || 0;
    const alvo = Armazem.ler("alvo", null), seq = Registro.sequencia();
    const d = alvo && typeof alvo.data === "string" ? Registro.diasAte(alvo.data) : NaN;
    let cont;
    if (!alvo) cont = `<p class="hoje__vazio">Quando é a sua prova? Defina a data para ver quantos dias faltam.</p>`;
    else if (isNaN(d)) cont = "<p>A data salva não é válida. Defina de novo.</p>";
    else if (d > 0) cont = `<p class="hoje__grande">${d} <span>${d === 1 ? "dia" : "dias"}</span></p><p>para ${esc(alvo.nome)}, ${new Date(alvo.data + "T12:00:00").toLocaleDateString("pt-BR", { day: "numeric", month: "long" })}</p>`;
    else if (d === 0) cont = `<p class="hoje__grande">Hoje</p><p>é a prova de ${esc(alvo.nome)}. Boa sorte!</p>`;
    else cont = "<p>A data da prova já passou. Defina uma nova.</p>";
    // meta: 10 bolinhas; com meta maior que 10, cada bolinha vale uma fração
    const B = Math.min(10, meta.questoesDia), cheias = Math.min(B, Math.floor(feitas / meta.questoesDia * B));
    const bolinhas = Array.from({ length: B }, (_, i) => `<i class="${i < cheias ? "cheia" : ""}"></i>`).join("");
    const falta = Math.max(0, meta.questoesDia - feitas);
    // últimos 7 dias
    const dias = Array.from({ length: 7 }, (_, i) => {
      const dt = new Date(); dt.setDate(dt.getDate() - (6 - i));
      const chave = dt.getFullYear() + "-" + String(dt.getMonth() + 1).padStart(2, "0") + "-" + String(dt.getDate()).padStart(2, "0");
      return { rot: i === 6 ? "hoje" : DIAS[dt.getDay()], feito: !!ativ[chave], hoje: i === 6 };
    });
    $("#painel").innerHTML = `<div class="hoje">
      <section class="hoje__card hoje__card--escuro" aria-labelledby="hc-cont">
        <h3 id="hc-cont">Contagem regressiva</h3>${cont}
        <details class="hoje__editar"${alvo ? "" : " open"}><summary>${alvo ? "Trocar a prova ou a data" : "Definir a prova"}</summary>
          <form id="f-alvo"><label class="rotulo" for="i-nome">Prova</label><input id="i-nome" class="campo" value="${alvo && alvo.nome ? esc(alvo.nome) : ""}" placeholder="ex.: Vestibulinho ETEC">
            <label class="rotulo" for="i-data">Data</label><input id="i-data" class="campo" type="date" value="${alvo && /^\d{4}-\d{2}-\d{2}$/.test(alvo.data) ? alvo.data : ""}">
            <button class="btn btn--claro" type="submit">Salvar</button></form></details>
      </section>
      <section class="hoje__card" aria-labelledby="hc-meta">
        <h3 id="hc-meta">Meta de hoje</h3>
        <p class="hoje__grande">${feitas} <span>${mh.folga ? "questões hoje" : `de ${meta.questoesDia} questões`}</span></p>
        <div class="hoje__bolinhas" role="progressbar" aria-label="Meta de hoje" aria-valuemin="0" aria-valuemax="${meta.questoesDia}" aria-valuenow="${Math.min(feitas, meta.questoesDia)}" style="--n:${B}">${bolinhas}</div>
        <p class="legenda">${mh.folga ? "Hoje é folga na sua rotina." + (feitas ? " Mesmo assim, você já fez " + feitas + "." : "") : falta ? `Faltam ${falta}.` : "Meta de hoje cumprida."}</p>
        ${mh.daRotina ? `<p class="legenda"><a href="#cap-rotina">A meta segue a sua rotina</a></p>` : `<details class="hoje__editar"><summary>Mudar a meta</summary>
          <form id="f-meta"><label class="rotulo" for="i-meta">Questões por dia</label><input id="i-meta" class="campo" type="number" min="1" max="500" value="${meta.questoesDia}"><button class="btn" type="submit">Salvar meta</button></form></details>`}
      </section>
      <section class="hoje__card" aria-labelledby="hc-seq">
        <h3 id="hc-seq">Sequência</h3>
        <p class="hoje__grande">${seq} <span>${seq === 1 ? "dia seguido" : "dias seguidos"}</span></p>
        <ol class="hoje__semana" aria-label="Últimos 7 dias">${dias.map(x => `<li><i class="${x.feito ? (x.hoje ? "hoje" : "feito") : ""}" aria-hidden="true"></i><span>${x.rot}</span><span class="sr">${x.feito ? ": estudou" : ": não estudou"}</span></li>`).join("")}</ol>
      </section></div>`;
    faixa(meta, feitas, seq, alvo, d);
    faixaHoje();
    if ($("#f-meta")) $("#f-meta").addEventListener("submit", e => {
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

  /* ---- Minha rotina: faixa com o dia de hoje, grade da semana, como montar o treino e o lembrete ---- */
  let materias = [];
  function faixaHoje() {
    const el = $("#faixa-hoje"), r = Rotina.ler();
    el.hidden = !Rotina.ativa(r); $("#faixa-num").hidden = !el.hidden;
    if (el.hidden) return;
    const d = Rotina.hoje(r), prox = Rotina.proxima(r), dia = Rotina.NOMES[new Date().getDay()].toLowerCase();
    el.innerHTML = d
      ? `<p class="rot-hoje__rot">Hoje · ${dia}, ${Rotina.horaTxt(d.h)}</p><p class="rot-hoje__mat">${esc(Rotina.matTxt(d.m))}</p>
         <p class="rot-hoje__det">${d.q} questões · ${Rotina.duracao(Rotina.minutos(d))}${r.modo === "revisao" ? " · revisão primeiro" : ""}</p>
         <button class="btn btn--claro btn--grande" type="button" id="b-rot-hoje">Começar o treino de hoje</button>`
      : `<p class="rot-hoje__rot">Hoje · ${dia}</p><p class="rot-hoje__mat">Folga</p>
         <p class="rot-hoje__det">${prox ? `Próximo: ${prox.nome.toLowerCase()}, ${Rotina.horaTxt(prox.dia.h)} · ${esc(Rotina.matTxt(prox.dia.m))}` : ""}</p>
         <a class="btn btn--contorno-claro" href="#cap-rotina">Ver a rotina</a>`;
    const b = $("#b-rot-hoje"); if (b) b.onclick = () => treinoDoDia(b);
  }
  // o treino do dia: primeiro as revisões que vencem hoje (das matérias do dia), depois questões novas sorteadas
  function treinoDoDia(botao) {
    const r = Rotina.ler(), d = Rotina.hoje(r) || (Rotina.proxima(r) || {}).dia;
    if (!d) return dizer("Monte a sua rotina primeiro.");
    if (!indice.length) return dizer("Carregando as provas… tente de novo em instantes.");
    if (botao) botao.disabled = true;
    const mats = d.m.length ? d.m : materias, usadas = new Set(), refs = [];
    if (r.modo === "revisao") Registro.pendentesHoje().filter(e => existe(e) && mats.includes(e.materia)).slice(0, d.q)
      .forEach(e => { usadas.add(e.provaId + "#" + e.numero); refs.push({ provaId: e.provaId, numero: e.numero }); });
    const feitas = new Set(Registro.listarErros().map(e => e.provaId + "#" + e.numero));
    const pool = Treino.embaralhar(indice.filter(x => !x.x && mats.includes(x.m) && (!r.banca || bancaDe[x.p] === r.banca) && !usadas.has(x.p + "#" + x.n)));
    // prefere questões que ainda não estão no caderno de erros
    pool.sort((a, b) => feitas.has(a.p + "#" + a.n) - feitas.has(b.p + "#" + b.n));
    pool.slice(0, d.q - refs.length).forEach(x => refs.push({ provaId: x.p, numero: x.n }));
    if (!refs.length) { if (botao) botao.disabled = false; return dizer("Não há questões dessas matérias com os filtros da rotina."); }
    const dia = Rotina.NOMES[new Date().getDay()].toLowerCase();
    montarDeRefs(refs, `Rotina de ${dia}: ${Rotina.matTxt(d.m)}`).then(() => { if (botao) botao.disabled = false; });
  }
  function rotina() {
    const r = Rotina.ler(), nd = Object.keys(r.dias).length;
    const total = Object.keys(r.dias).reduce((t, k) => t + r.dias[k].q, 0);
    const dia = k => {
      const d = r.dias[k], nome = Rotina.NOMES[k];
      if (!d) return `<section class="rot-dia rot-dia--folga" data-k="${k}"><div class="rot-dia__topo"><b>${Rotina.CURTOS[k]}<span class="rot-dia__longo">${nome.slice(3)}</span></b>
        <label class="chave"><input type="checkbox" data-liga="${k}"><span class="sr">Estudar ${nome.toLowerCase()}</span></label></div><span class="rot-dia__folga">folga</span></section>`;
      const resto = materias.filter(m => !d.m.includes(m));
      return `<section class="rot-dia" data-k="${k}"><div class="rot-dia__topo"><b>${Rotina.CURTOS[k]}<span class="rot-dia__longo">${nome.slice(3)}</span></b>
        <label class="chave"><input type="checkbox" data-liga="${k}" checked><span class="sr">Estudar ${nome.toLowerCase()}</span></label></div>
        <label class="rot-dia__hora"><span class="sr">Horário de ${nome.toLowerCase()}</span><input type="time" class="campo" data-hora="${k}" value="${d.h}"></label>
        <div class="rot-dia__mats">${d.m.map(m => `<button type="button" class="rot-mat" data-tira="${k}" data-m="${esc(m)}" aria-label="Tirar ${esc(m)} de ${nome.toLowerCase()}">${esc(m)} <span aria-hidden="true">×</span></button>`).join("")}
          ${d.m.length < 6 && resto.length ? `<label class="rot-mais"><span class="sr">Pôr uma matéria em ${nome.toLowerCase()}</span><select class="campo" data-poe="${k}"><option value="">+ matéria</option>${resto.map(m => `<option>${esc(m)}</option>`).join("")}</select></label>` : ""}
          ${d.m.length ? "" : `<span class="rot-dia__dica">Sem matéria: sorteia de todas</span>`}</div>
        <div class="rot-dia__q"><button type="button" class="rot-passo" data-q="${k}" data-d="-1" aria-label="Menos questões em ${nome.toLowerCase()}"${d.q <= Rotina.Q_MIN ? " disabled" : ""}>−</button>
          <span><b>${d.q}</b> questões</span>
          <button type="button" class="rot-passo" data-q="${k}" data-d="1" aria-label="Mais questões em ${nome.toLowerCase()}"${d.q >= Rotina.Q_MAX ? " disabled" : ""}>+</button></div></section>`;
    };
    const google = Object.keys(r.dias).sort((a, b) => Rotina.ORDEM.indexOf(+a) - Rotina.ORDEM.indexOf(+b))
      .map(k => `<li><a href="${esc(Rotina.linkGoogle(k, r.dias[k]))}" target="_blank" rel="noopener">${Rotina.NOMES[k]}, ${Rotina.horaTxt(r.dias[k].h)}</a></li>`).join("");
    $("#rotina").innerHTML = `<div class="titulo-linha rot-tit"><h3>A sua <em>semana</em></h3><span class="titulo-linha__extra">${nd ? `${nd} ${nd === 1 ? "dia" : "dias"} · ${total} questões` : "Ligue os dias em que vai estudar"}</span></div>
      <div class="rot-grade">${Rotina.ORDEM.map(dia).join("")}</div>
      <div class="rot-cartoes">
        <section class="rot-cartao"><h4>Como montar o treino do dia</h4>
          <label class="cfg__op"><input type="radio" name="rot-modo" value="revisao"${r.modo === "revisao" ? " checked" : ""}><span><strong>Revisão primeiro</strong><span class="cfg__desc">As erradas que voltam hoje entram antes das novas</span></span></label>
          <label class="cfg__op"><input type="radio" name="rot-modo" value="novas"${r.modo === "novas" ? " checked" : ""}><span><strong>Só questões novas</strong><span class="cfg__desc">A revisão fica no capítulo Revisão de hoje</span></span></label>
          <label class="rotulo" for="rot-banca">Provas</label>
          <select id="rot-banca" class="campo"><option value="">Todas (ETEC, FATEC e Enem)</option>${["ETEC", "FATEC", "Enem"].map(b => `<option${r.banca === b ? " selected" : ""}>${b}</option>`).join("")}</select>
          <p class="legenda">Tempo sugerido: ${Config.minutosPorQuestaoTreino} minutos por questão.</p>
        </section>
        <section class="rot-cartao rot-cartao--escuro"><h4>Lembrete no celular</h4>
          <p>O seu calendário cria um lembrete em cada dia da rotina, no horário marcado, com o que estudar e o link do treino. Funciona sem cadastro.</p>
          <p class="botoes"><button class="btn btn--claro btn--grande" type="button" id="b-ics"${nd ? "" : " disabled"}><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3.5" y="5" width="17" height="15" rx="3"/><path d="M3.5 10h17M8 3v4M16 3v4"/></svg>Adicionar ao meu calendário</button></p>
          ${nd ? `<details class="rot-google"><summary>Usa o Google Agenda? Adicione dia por dia</summary><ul>${google}</ul></details>` : ""}
          <p class="rot-cartao__pe">Mudou a rotina? Adicione de novo e apague os lembretes antigos no calendário.</p>
          ${nd ? `<button type="button" class="btn btn--contorno-claro rot-apagar" id="b-rot-apagar">Apagar a rotina e voltar à meta fixa</button>` : ""}
        </section></div>`;
    const salvar = (fn, msg) => { const x = Rotina.ler(); fn(x); Rotina.gravar(x); rotina(); painel(); sumario(); dizer(msg || "Rotina salva."); };
    $("#rotina").querySelectorAll("[data-liga]").forEach(c => c.onchange = () => salvar(x => {
      const k = c.dataset.liga;
      if (c.checked) { const ant = Object.keys(x.dias)[0]; x.dias[k] = { h: ant ? x.dias[ant].h : "19:00", m: [], q: 20 }; } else delete x.dias[k];
    }, c.checked ? `${Rotina.NOMES[c.dataset.liga]} entrou na rotina.` : `${Rotina.NOMES[c.dataset.liga]} virou folga.`));
    $("#rotina").querySelectorAll("[data-hora]").forEach(i => i.onchange = () => { if (/^\d{2}:\d{2}$/.test(i.value)) salvar(x => { x.dias[i.dataset.hora].h = i.value; }); });
    $("#rotina").querySelectorAll("[data-poe]").forEach(sl => sl.onchange = () => { if (sl.value) salvar(x => { x.dias[sl.dataset.poe].m.push(sl.value); }, `${sl.value} entrou em ${Rotina.NOMES[sl.dataset.poe].toLowerCase()}.`); });
    $("#rotina").querySelectorAll("[data-tira]").forEach(b => b.onclick = () => salvar(x => { const d = x.dias[b.dataset.tira]; d.m = d.m.filter(m => m !== b.dataset.m); }, `${b.dataset.m} saiu de ${Rotina.NOMES[b.dataset.tira].toLowerCase()}.`));
    $("#rotina").querySelectorAll("[data-q]").forEach(b => b.onclick = () => salvar(x => { const d = x.dias[b.dataset.q]; d.q += +b.dataset.d * Rotina.Q_PASSO; }));
    $("#rotina").querySelectorAll("[name=rot-modo]").forEach(i => i.onchange = () => salvar(x => { x.modo = i.value; }));
    $("#rot-banca").onchange = () => salvar(x => { x.banca = $("#rot-banca").value; });
    $("#b-ics").onclick = () => { Rotina.baixarIcs(); dizer("Arquivo do calendário baixado. Abra o arquivo para criar os lembretes."); };
    const ap = $("#b-rot-apagar"); if (ap) ap.onclick = () => { Rotina.apagar(); rotina(); painel(); sumario(); dizer("Rotina apagada. A meta fixa voltou."); };
  }

  /* ---- Sumário: um link por capítulo, com um resumo do que tem dentro ---- */
  function sumario() {
    const pend = Registro.pendentesHoje().length, abertos = Registro.listarErros().filter(e => e.status === "aberta").length;
    const h = Armazem.ler("historico", []), est = Registro.estatisticas(h);
    const rd = Rotina.ler(), nd = Object.keys(rd.dias).length;
    const caps = [["hoje", "Hoje", "Prova, meta e sequência"], ["rotina", "Minha rotina", nd ? `${nd} ${nd === 1 ? "dia" : "dias"} por semana` : "Monte a sua semana"], ["revisao", "Revisão", pend ? `${pend} para hoje` : "Nada para hoje"],
      ["misto", "Simulado misto", "Uma prova nova"], ["treino", "Treino por matéria", "Matérias e assuntos"],
      ["stats", "Estatísticas", h.length ? `${est.total} questões feitas` : "Depois do 1º simulado"], ["erros", "Caderno de erros", abertos ? `${abertos} em aberto` : "Vazio por enquanto"]];
    $("#sumario").innerHTML = caps.map(([id, nome, sub], i) => `<li><a href="#cap-${id}"><span class="sumario__n">${i + 1}</span><span><b>${nome}</b><small>${sub}</small></span></a></li>`).join("");
    const ints = (Config.intervalosRevisaoDias || []).join(", ").replace(/, (\d+)$/, " e $1");
    $("#ints").textContent = ints;
    if (!("IntersectionObserver" in window)) return;
    const links = [...$("#sumario").querySelectorAll("a")];
    const marcar = id => links.forEach(a => { const on = a.getAttribute("href") === "#" + id; a.classList.toggle("atual", on); if (on) a.setAttribute("aria-current", "true"); else a.removeAttribute("aria-current"); });
    marcar("cap-hoje");
    const obs = new IntersectionObserver(ents => { const v = ents.filter(x => x.isIntersecting)[0]; if (v) marcar(v.target.id); }, { rootMargin: "-25% 0px -65% 0px" });
    document.querySelectorAll(".cap").forEach(c => obs.observe(c));
  }

  /* ---- Treinos montados a partir de várias provas ----
     O sorteio usa só o índice leve; depois baixa apenas as provas das questões escolhidas. */
  const existe = r => idx.has(r.provaId + "#" + r.numero);
  function montarDeRefs(refs, titulo, opcoes) {
    dizer("Montando o treino…");
    return Dados.provas(refs.map(r => r.provaId)).then(ps => {
      const itens = refs.map(r => ps[r.provaId] && { prova: ps[r.provaId], q: ps[r.provaId].questoes.find(q => q.numero === r.numero) }).filter(x => x && x.q);
      if (!itens.length) return dizer("Não foi possível carregar essas questões agora. Confira a internet e tente de novo.");
      ir(Treino.montar(titulo, itens, opcoes));
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

  /* Revisão rápida: 5 questões do caderno de erros, primeiro as que vencem hoje, depois as que vencem antes.
     Cabe numa pausa de 10 minutos e mantém o caderno andando mesmo em dias corridos. */
  const RAPIDA = 5;
  function revisaoRapida() {
    const abertas = Registro.listarErros().filter(e => e.status === "aberta" && existe(e))
      .sort((a, b) => (a.proxima || "") < (b.proxima || "") ? -1 : (a.proxima || "") > (b.proxima || "") ? 1 : 0);
    return abertas.slice(0, RAPIDA);
  }
  function revisao() {
    const pend = Registro.pendentesHoje().filter(existe), rapida = revisaoRapida();
    const feitaHoje = Armazem.ler("revisao-rapida", "") === Registro.hoje();
    $("#revisao").innerHTML = (pend.length
      ? `<p><strong>${pend.length}</strong> ${pend.length === 1 ? "questão pede" : "questões pedem"} revisão hoje, no ritmo da revisão espaçada.</p><p class="botoes"><button class="btn btn--primary btn--grande" id="b-rev" type="button">Começar a revisão</button></p>`
      : "<p>Nada para revisar hoje. As questões erradas voltam aqui no dia certo, para reforçar a memória.</p>")
      + (rapida.length ? `<h3>Revisão rápida</h3><p>${feitaHoje ? "Você já fez a revisão rápida hoje. Pode repetir se quiser." : `Sem tempo? ${rapida.length === 1 ? "Uma questão" : rapida.length + " questões"} do caderno de erros, as mais atrasadas primeiro: cerca de ${rapida.length * 2} minutos.`}</p><button class="btn" id="b-rapida" type="button">Fazer a revisão rápida</button>` : "");
    const b = $("#b-rev"); if (b) b.onclick = () => treinoDeEntradas(pend, "Revisão de hoje", 30);
    const br = $("#b-rapida");
    if (br) br.onclick = () => { Armazem.gravar("revisao-rapida", Registro.hoje()); montarDeRefs(rapida, "Revisão rápida", { minutos: rapida.length * 2, rotuloTempo: "2 min por questão" }); };
  }

  /* ---- Simulado misto: questões de todas as edições de uma banca, na proporção de matérias das provas reais ---- */
  // Proporção: conta as questões válidas de cada matéria em todas as provas da banca; reparte o total pelo maior resto.
  // Enem: a área de cada questão sai da matéria (vale também para o modelo antigo, de 63 questões)
  const AREA = { "Matemática": "Matemática", "Física": "Natureza", "Química": "Natureza", "Biologia": "Natureza",
    "História": "Humanas", "Geografia": "Humanas", "Filosofia": "Humanas", "Sociologia": "Humanas",
    "Português": "Linguagens", "Artes": "Linguagens", "Educação Física": "Linguagens", "Inglês": "Linguagens", "Espanhol": "Linguagens" };
  const AREAS = ["Linguagens", "Humanas", "Natureza", "Matemática"];
  function proporcao(banca, filtro) {
    const pool = indice.filter(x => !x.x && bancaDe[x.p] === banca && (!filtro || filtro(x))), cont = {};
    pool.forEach(x => { cont[x.m] = (cont[x.m] || 0) + 1; });
    return { pool: pool, cont: cont, total: pool.length };
  }
  function repartir(cont, total, n) {
    const ms = Object.keys(cont), alvo = ms.map(m => ({ m: m, exato: cont[m] / total * n }));
    alvo.forEach(a => { a.q = Math.floor(a.exato); });
    let falta = n - alvo.reduce((s, a) => s + a.q, 0);
    alvo.slice().sort((a, b) => (b.exato - b.q) - (a.exato - a.q)).forEach(a => { if (falta > 0) { a.q++; falta--; } });
    return alvo.filter(a => a.q > 0);
  }
  // sorteia n questões de um grupo, na proporção de matérias dele
  function sortear(pr, n) {
    const refs = [];
    repartir(pr.cont, pr.total, Math.min(n, pr.total)).forEach(a => {
      Treino.embaralhar(pr.pool.filter(x => x.m === a.m)).slice(0, a.q).forEach(x => refs.push({ provaId: x.p, numero: x.n, m: x.m }));
    });
    return refs;
  }
  /* Simulado misto: quatro cartões (só ETEC, só FATEC, só Enem ou provas mescladas) e, embaixo, as opções do escolhido.
     Prova pura: a nota é a daquela prova. Mesclada: metade de cada prova, sem nota (o resultado mostra acertos por prova). */
  function mistoForm() {
    const tem = b => Object.keys(bancaDe).some(id => bancaDe[id] === b);
    const bancas = ["ETEC", "FATEC", "Enem"].filter(tem);
    if (!bancas.length) { $("#misto").innerHTML = "<p>Ainda não há provas carregadas.</p>"; return; }
    function ref(b) {   // tamanho e tempo: os da prova mais recente da banca (na FATEC, 1 h das 5 h fica para a redação)
      const ps = listaProvas.filter(p => p.banca === b).sort((x, y) => (y.ano - x.ano) || ((y.semestre || 0) - (x.semestre || 0)));
      const p = ps[0] || {};
      const tot = p.totalQuestoes || 50, min = b === "FATEC" ? Math.max(60, (p.duracaoMinutos || 300) - 60) : (p.duracaoMinutos || 240);
      return { total: tot, minutos: min, edicoes: ps.length, recente: p };
    }
    const CART = {
      ETEC: ["Só ETEC", () => `${ref("ETEC").total} questões de ${ref("ETEC").edicoes} provas, na proporção da prova real. ${Motor.duracaoTexto(ref("ETEC").minutos)}.`, "Nota da ETEC: acertos"],
      FATEC: ["Só FATEC", () => `${ref("FATEC").total} questões, na proporção da prova real. ${Motor.duracaoTexto(ref("FATEC").minutos)}; a redação fica de fora.`, "Nota da FATEC: parte objetiva"],
      Enem: ["Só Enem", () => "Escolha as áreas: Linguagens, Humanas, Natureza ou Matemática. 45 questões por área.", "Acertos por matéria (sem TRI)"],
      Mescla: ["Provas mescladas", () => "Duas ou as três provas juntas, metade de cada, na proporção de matérias de cada prova.", "Sem nota: acertos por prova"]
    };
    const tipos = bancas.concat(bancas.length > 1 ? ["Mescla"] : []);
    const cartao = (t, i) => `<label class="misto-op${t === "Mescla" ? " misto-op--mescla" : ""}"><input type="radio" name="m-tipo" value="${t}"${i === 0 ? " checked" : ""}>
      <span class="misto-op__cima"><span class="misto-op__tag">${t === "Mescla" ? "Mescla" : t}</span></span>
      <b>${CART[t][0]}</b><span class="misto-op__d">${CART[t][1]()}</span><span class="misto-op__nota">${CART[t][2]}</span></label>`;
    const pilula = (nome, v, rot, on) => `<label class="chk chk--pilula"><input type="checkbox" name="${nome}" value="${v}"${on ? " checked" : ""}> ${rot}</label>`;
    $("#misto").innerHTML = `<form id="f-misto" class="cfg">
      <div class="misto-ops" role="radiogroup" aria-label="De onde vêm as questões">${tipos.map(cartao).join("")}</div>
      <div class="misto-opcoes">
        <div class="misto-grupo" data-para="ETEC FATEC"><fieldset><legend class="rotulo">Tamanho</legend>
          <div class="segmento cfg__seg"><label><input type="radio" name="m-tam" value="1" checked><span>Prova inteira</span></label><label><input type="radio" name="m-tam" value="0.5"><span>Meia prova</span></label></div></fieldset></div>
        <div class="misto-grupo" data-para="Enem"><fieldset><legend class="rotulo">Áreas</legend><div class="pilulas">${AREAS.map((a, i) => pilula("m-area", a, a, i === 2)).join("")}</div></fieldset>
          <fieldset class="misto-lingua"><legend class="rotulo">Língua estrangeira (Linguagens)</legend>
          <div class="segmento cfg__seg"><label><input type="radio" name="m-lingua" value="Inglês" checked><span>Inglês</span></label><label><input type="radio" name="m-lingua" value="Espanhol"><span>Espanhol</span></label></div></fieldset></div>
        <div class="misto-grupo" data-para="Mescla"><div class="cfg__duas">
          <fieldset><legend class="rotulo">Quais provas misturar</legend><div class="pilulas">${bancas.map((b, i) => pilula("m-banca", b, b, i < 2)).join("")}</div></fieldset>
          <fieldset><legend class="rotulo">Tamanho</legend><div class="segmento cfg__seg misto-seg3">${[20, 40, 60].map(n => `<label><input type="radio" name="m-n" value="${n}"${n === 40 ? " checked" : ""}><span>${n}</span></label>`).join("")}</div></fieldset></div>
          <div class="misto-aviso" role="note"><span aria-hidden="true">i</span><p><b>Este simulado não tem nota.</b> Cada prova calcula a nota de um jeito: a ETEC soma acertos, a FATEC usa peso com a redação e o Enem usa a TRI. Misturando, nenhuma dessas notas vale. O resultado mostra os acertos por matéria e por prova de origem.</p></div></div>
      </div>
      <div class="abre__pe-form"><p id="m-info"></p><button class="btn btn--primary btn--grande" type="submit" id="m-ok">Montar o simulado</button></div></form>`;
    const f = $("#f-misto");
    const marcados = nome => [...f.querySelectorAll(`[name=${nome}]:checked`)].map(i => i.value);
    // plano do simulado conforme o cartão: { refs(), n, minutos, titulo, misto, texto, ok }
    function plano() {
      const tipo = f.elements["m-tipo"].value;
      if (tipo === "ETEC" || tipo === "FATEC") {
        const r = ref(tipo), fr = parseFloat(f.elements["m-tam"].value), n = Math.round(r.total * fr), pr = proporcao(tipo);
        const partes = repartir(pr.cont, pr.total, n).sort((a, c) => c.q - a.q);
        return { ok: true, n, minutos: Math.round(r.minutos * fr), misto: tipo, titulo: `Simulado misto ${tipo}`, rotulo: `Proporcional à prova da ${tipo}`,
          texto: `<b>${n} questões em ${Motor.duracaoTexto(Math.round(r.minutos * fr))}</b>, sorteadas de ${r.edicoes} provas da ${tipo}: ${partes.map(a => `${esc(a.m)} ${a.q}`).join(", ")}.`,
          refs: () => {
            const refs = sortear(pr, n);
            const ordem = [...new Set(indice.filter(x => x.p === r.recente.id).map(x => x.m))];   // matérias em blocos, na ordem da prova mais recente
            return refs.sort((x, y) => { const i = ordem.indexOf(x.m), j = ordem.indexOf(y.m); return (i < 0 ? 99 : i) - (j < 0 ? 99 : j); });
          } };
      }
      if (tipo === "Enem") {
        const areas = marcados("m-area"), lingua = f.elements["m-lingua"].value, outra = lingua === "Inglês" ? "Espanhol" : "Inglês";
        f.querySelector(".misto-lingua").hidden = !areas.includes("Linguagens");
        if (!areas.length) return { ok: false, texto: "Escolha pelo menos uma área." };
        const n = areas.length * 45, minutos = n * Config.minutosPorQuestaoTreino;
        return { ok: true, n, minutos, misto: "Enem", titulo: `Simulado misto Enem: ${areas.join(", ")}`, rotulo: `${Config.minutosPorQuestaoTreino} minutos por questão`,
          texto: `<b>${n} questões em ${Motor.duracaoTexto(minutos)}</b>, 45 por área (${areas.join(", ")}), de todas as edições do Enem. <span>Sem nota TRI: o resultado mostra os acertos.</span>`,
          refs: () => [].concat(...areas.map(a => sortear(proporcao("Enem", x => AREA[x.m] === a && x.m !== outra), 45))) };
      }
      const bs = marcados("m-banca"), n = parseInt(f.elements["m-n"].value, 10);
      if (bs.length < 2) return { ok: false, texto: "Marque pelo menos duas provas para mesclar. Para uma só, use o cartão dela." };
      const cada = bs.map((b, i) => Math.floor(n / bs.length) + (i < n % bs.length ? 1 : 0)), minutos = n * Config.minutosPorQuestaoTreino;
      return { ok: true, n, minutos, misto: "Mescla", titulo: `Simulado mesclado: ${bs.join(", ")}`, rotulo: `${Config.minutosPorQuestaoTreino} minutos por questão`,
        texto: `<b>${n} questões em ${Motor.duracaoTexto(minutos)}</b>: ${bs.map((b, i) => `${cada[i]} da ${b}`).join(", ").replace("da Enem", "do Enem")}. <span>Sem nota.</span>`,
        refs: () => [].concat(...bs.map((b, i) => sortear(proporcao(b, b === "Enem" ? (x => x.m !== "Espanhol") : null), cada[i]))) };
    }
    function info() {
      const tipo = f.elements["m-tipo"].value;
      f.querySelectorAll(".misto-grupo").forEach(g => { g.hidden = !g.dataset.para.split(" ").includes(tipo); });
      const pl = plano();
      $("#m-info").innerHTML = pl.texto; $("#m-ok").disabled = !pl.ok;
    }
    f.addEventListener("change", info); info();
    f.addEventListener("submit", e => {
      e.preventDefault();
      const pl = plano(); if (!pl.ok) return;
      montarDeRefs(pl.refs(), pl.titulo, { minutos: pl.minutos, rotuloTempo: pl.rotulo, misto: pl.misto });
    });
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
    $("#treino").innerHTML = mats.length ? `<form id="f-treino"><fieldset class="passo"><legend><span class="passo__n">1.</span> Matérias</legend><div class="pilulas">${mats.map((m, i) => `<label class="chk chk--pilula"><input type="checkbox" name="mat" value="${esc(m)}"${i === 0 ? " checked" : ""}> ${esc(m)}</label>`).join("")}</div></fieldset>
      <fieldset class="passo" id="t-assuntos"><legend><span class="passo__n">2.</span> Assuntos <span class="legenda">(opcional: sem marcar nenhum, vale qualquer assunto)</span></legend><div class="pilulas"></div><p class="legenda" id="t-resumo"></p></fieldset>
      <div class="passo passo--linha"><div><label class="rotulo" for="t-qtd">3. Quantas questões</label><select id="t-qtd" class="campo">${[10, 20, 30, 50].map(n => `<option>${n}</option>`).join("")}</select></div>
      <div><label class="rotulo" for="t-banca">4. De qual vestibular</label><select id="t-banca" class="campo"><option value="">Todos</option>${bancas.map(b => `<option>${esc(b)}</option>`).join("")}</select></div>
      <button class="btn btn--primary btn--grande" type="submit">Montar treino</button></div></form>` : "<p>Ainda não há provas carregadas.</p>";
    const f = $("#f-treino"); if (!f) return;
    // a lista de assuntos acompanha as matérias marcadas (mantendo o que já estava marcado)
    function atualizarAssuntos() {
      const marcados = new Set([...f.querySelectorAll("[name=assunto]:checked")].map(x => x.value));
      const sel = [...f.querySelectorAll("[name=mat]:checked")].map(x => x.value);
      const html = sel.map(m => Object.keys(porMat[m] || {}).sort().map(a => {
        const k = m + " · " + a;
        return `<label class="chk chk--pilula"><input type="checkbox" name="assunto" value="${esc(k)}"${marcados.has(k) ? " checked" : ""}> ${esc(a)} <span class="conta">${porMat[m][a]}</span></label>`;
      }).join("")).join("");
      f.querySelector("#t-assuntos .pilulas").innerHTML = html || '<p class="legenda">As matérias marcadas ainda não têm assuntos cadastrados.</p>';
    }
    f.querySelectorAll("[name=mat]").forEach(c => c.addEventListener("change", atualizarAssuntos));
    // quantas questões a escolha atual tem
    const resumo = () => {
      const sel = [...f.querySelectorAll("[name=mat]:checked")].map(x => x.value), as = [...f.querySelectorAll("[name=assunto]:checked")].map(x => x.value), b = $("#t-banca").value;
      const n = indice.filter(x => !x.x && sel.includes(x.m) && (!b || bancaDe[x.p] === b) && (!as.length || as.includes(x.m + " · " + x.a))).length;
      $("#t-resumo").textContent = sel.length ? `${as.length ? as.length + (as.length === 1 ? " assunto marcado" : " assuntos marcados") + " · " : ""}${n} ${n === 1 ? "questão disponível" : "questões disponíveis"}.` : "";
    };
    f.addEventListener("change", resumo);
    atualizarAssuntos(); resumo();
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
    $("#caderno").innerHTML = `<div class="passo passo--linha"><div><label class="rotulo" for="c-status">Mostrar</label><select id="c-status" class="campo"><option value="aberta">Em aberto</option><option value="resolvida">Resolvidas</option><option value="">Todas</option></select></div>
      <div><label class="rotulo" for="c-mat">Matéria</label><select id="c-mat" class="campo"><option value="">Todas</option>${mats.map(m => `<option>${esc(m)}</option>`).join("")}</select></div></div>
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

  painel(); stats(); sumario();
  Promise.all([Dados.indice(), Dados.lista()]).then(([ind, lista]) => {
    indice = ind; idx = new Set(ind.map(x => x.p + "#" + x.n));
    listaProvas = lista;
    lista.forEach(p => { bancaDe[p.id] = p.banca; });
    materias = [...new Set(ind.map(x => x.m))].sort((a, b) => a.localeCompare(b, "pt"));
    rotina(); revisao(); mistoForm(); plano(); treinoForm(); caderno();
    // vindo do lembrete do calendário: começa o treino do dia direto
    if (new URLSearchParams(location.search).get("rotina") === "hoje" && Rotina.ativa()) { history.replaceState(null, "", location.pathname); treinoDoDia(null); }
  }).catch(() => {
    const msg = "Não foi possível carregar as provas. Se abriu o arquivo direto, use um servidor local (veja o README).";
    dizer(msg);
    ["#rotina", "#revisao", "#misto", "#plano", "#treino", "#caderno"].forEach(s => { $(s).innerHTML = "<p>Indisponível agora: as provas não carregaram.</p>"; });   // não deixa "Carregando…" para sempre
  });
})();
