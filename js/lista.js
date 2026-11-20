/* Lista compartilhada: lista.html?l=<prova:1.2~prova2:5>&t=<nome>. Mostra o que tem na lista e monta o treino.
   Faixa com o nome da lista e a ficha (questões, tempo sugerido, começar); embaixo, as questões agrupadas por prova. */
(function () {
  const params = new URLSearchParams(location.search), app = document.getElementById("app"), E = Render.esc;
  const pedidos = Treino.decodificarLista(params.get("l")), titulo = (params.get("t") || "Lista de questões").slice(0, 80);
  const simples = (t, msg) => { app.innerHTML = `<section class="faixa"><div class="faixa__in"><div class="faixa__texto"><p class="sobretitulo">Lista de questões</p><h1>${E(t)}</h1><p class="faixa__lead">${msg}</p></div></div></section>`; };
  const curto = p => p.semestre ? `${p.banca} ${p.ano} · ${p.semestre}º sem.` : p.area ? `${p.banca} ${p.ano} · ${String(p.area).replace(/\s*\(.*\)\s*$/, "")}` : p.ano ? `${p.banca} ${p.ano}` : p.titulo;
  if (!pedidos.length) return simples("Lista de questões", 'Este link não tem questões. Peça um novo para quem enviou, ou monte a sua em <a href="busca.html">Treinar por assunto</a>.');
  const ids = [...new Set(pedidos.map(p => p.provaId))];
  Treino.carregarTodas(ids).then(provas => {
    const itens = pedidos.map(p => provas[p.provaId] && { prova: provas[p.provaId], q: provas[p.provaId].questoes.find(q => q.numero === p.numero) }).filter(x => x && x.q);
    const faltam = pedidos.length - itens.length;
    document.title = titulo + " | Treineiros";
    if (!itens.length) return simples(titulo, "As questões desta lista não estão mais disponíveis no site.");
    // agrupa por prova, na ordem em que aparecem na lista
    const grupos = [];
    itens.forEach(x => { let g = grupos.find(g => g.prova === x.prova); if (!g) grupos.push(g = { prova: x.prova, qs: [] }); g.qs.push(x.q); });
    const n = itens.length, min = n * Config.minutosPorQuestaoTreino;
    const tempo = min < 60 ? `${min} <small>min</small>` : E(Motor.duracaoTexto(min));
    app.innerHTML = `<section class="faixa lista-faixa" aria-labelledby="li-t"><div class="faixa__in">
        <div class="faixa__texto">
          <p class="sobretitulo">Lista de questões recebida</p>
          <h1 id="li-t">${E(titulo)}</h1>
          <p class="faixa__lead">${n} ${n === 1 ? "questão" : "questões"} de ${grupos.length} ${grupos.length === 1 ? "prova oficial" : "provas oficiais"}, com gabarito e explicação.${faltam ? ` ${faltam} da lista original não ${faltam === 1 ? "está mais disponível" : "estão mais disponíveis"}.` : ""}</p>
        </div>
        <div class="faixa__painel lista-ficha">
          <dl><div><dt>Questões</dt><dd>${n}</dd></div><div><dt>Tempo sugerido</dt><dd>${tempo}</dd></div></dl>
          <button class="btn btn--claro btn--grande" id="b-comecar" type="button">Começar o treino</button>
          <p>Se você tem um treino em andamento neste aparelho, ele será substituído por esta lista.</p>
        </div></div></section>
      <div class="pag__corpo">
        <div class="titulo-linha"><h2>O que tem <em>na lista</em></h2></div>
        <div class="lista-grupos">${grupos.map(g => `<section class="lista-grupo"><h3>${E(curto(g.prova))}<span>${g.qs.length} ${g.qs.length === 1 ? "questão" : "questões"}</span></h3>
          <ol class="lista-itens">${g.qs.map(q => `<li><a href="questao.html?id=${encodeURIComponent(g.prova.id)}&n=${q.numero}"><b>Q${E((q.origem && q.origem.numeroOriginal) || q.numero)}</b><span>${E(q.materia)}${q.assunto ? " · " + E(q.assunto) : ""}</span></a></li>`).join("")}</ol></section>`).join("")}</div>
        <p class="lista-montar">Quer montar a sua? Em <a href="busca.html">Treinar por assunto</a>, marque as questões e toque em “Mandar o link”.</p>
      </div>`;
    document.getElementById("b-comecar").onclick = () => { location.href = Treino.montar(titulo, itens); };
  }).catch(() => simples("Lista de questões", "Não foi possível carregar as provas."));
})();
