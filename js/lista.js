/* Lista compartilhada: lista.html?l=<prova:1.2~prova2:5>&t=<nome>. Mostra o que tem na lista e monta o treino. */
(function () {
  const params = new URLSearchParams(location.search), app = document.getElementById("app"), E = Render.esc;
  const pedidos = Treino.decodificarLista(params.get("l")), titulo = (params.get("t") || "Lista de questões").slice(0, 80);
  if (!pedidos.length) { app.innerHTML = `<h1>Lista de questões</h1><p>Este link não tem questões. Peça um novo para quem enviou, ou monte a sua em <a href="busca.html">Buscar questões</a>.</p>`; return; }
  const ids = [...new Set(pedidos.map(p => p.provaId))];
  Treino.carregarTodas(ids).then(provas => {
    const itens = pedidos.map(p => provas[p.provaId] && { prova: provas[p.provaId], q: provas[p.provaId].questoes.find(q => q.numero === p.numero) }).filter(x => x && x.q);
    const faltam = pedidos.length - itens.length;
    document.title = titulo + " | Treineiros";
    if (!itens.length) { app.innerHTML = `<h1>${E(titulo)}</h1><p>As questões desta lista não estão mais disponíveis no site.</p>`; return; }
    app.innerHTML = `<h1>${E(titulo)}</h1>
      <p>${itens.length} ${itens.length === 1 ? "questão" : "questões"}${faltam ? ` (${faltam} da lista original não ${faltam === 1 ? "está mais disponível" : "estão mais disponíveis"})` : ""}. Tempo sugerido: ${Motor.duracaoTexto(itens.length * Config.minutosPorQuestaoTreino)}.</p>
      <ol class="lista-itens">${itens.map(x => `<li>${E(Registro.rotuloOrigem(x.prova, x.q))} <span class="legenda">${E(x.q.materia)}${x.q.assunto ? ", " + E(x.q.assunto) : ""}</span></li>`).join("")}</ol>
      <p><button class="btn btn--primary" id="b-comecar" type="button">Começar o treino</button></p>
      <p class="legenda">Começar substitui o treino que você tiver em andamento neste aparelho.</p>`;
    document.getElementById("b-comecar").onclick = () => { location.href = Treino.montar(titulo, itens); };
  }).catch(() => { app.innerHTML = "<h1>Lista de questões</h1><p>Não foi possível carregar as provas.</p>"; });
})();
