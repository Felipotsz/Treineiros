/* Questão avulsa: questao.html?id=<prova>&n=<número>. Serve para mandar uma questão a alguém (professor, grupo de estudo).
   Folha da questão (enunciado, alternativas, correção e ações) e, ao lado, quem é o site e mais questões do mesmo assunto.
   No celular, o aviso "Alguém te mandou" fica numa faixa fina acima da questão, para não se perder no fim da página. */
(function () {
  const params = new URLSearchParams(location.search), ID = params.get("id"), N = parseInt(params.get("n"), 10);
  const app = document.getElementById("app"), aviso = document.getElementById("aviso"), E = Render.esc;
  const falar = t => { aviso.textContent = t; aviso.hidden = false; if (window.anunciar) anunciar(t); };
  const erro = msg => { app.innerHTML = `<h1>Questão</h1><p>${E(msg)}</p><p><a class="btn" href="busca.html">Buscar questões</a></p>`; };
  if (!ID || !(N > 0)) return erro("Endereço incompleto: falta a prova ou o número da questão.");

  let lista = [], indice = [];
  // nome curto de uma prova: "ETEC 2024, 2º sem." ou "Enem 2022"
  const curto = p => !p ? "" : p.semestre ? `${p.banca} ${p.ano}, ${p.semestre}º sem.` : p.ano ? `${p.banca} ${p.ano}` : (p.titulo || "");

  Dados.lista().then(l => {
    lista = l;
    if (!l.find(p => p.id === ID)) throw new Error("prova");
    return Dados.prova(ID);
  }).then(prova => {
    const i = prova.questoes.findIndex(q => q.numero === N);
    if (i < 0) return erro("Esta prova não tem a questão " + N + ".");
    mostrar(prova, i, null);
    // o índice é leve e só serve para "Mais deste assunto": se falhar, a lateral só fica sem a lista
    Dados.indice().then(ix => { indice = ix; mostrar(prova, i, respostaAtual); }).catch(() => {});
  }).catch(e => erro(e && e.message === "prova" ? "Não encontramos esta prova." : "Não foi possível carregar a questão."));

  let respostaAtual = null, sorteio = null;
  function maisDoAssunto(prova, q) {
    if (!q.assunto || !indice.length) return [];
    if (sorteio) return sorteio;
    const iguais = indice.filter(x => x.a === q.assunto && x.m === q.materia && !(x.p === prova.id && x.n === q.numero));
    const outras = Treino.embaralhar(iguais.filter(x => x.p !== prova.id)), mesma = Treino.embaralhar(iguais.filter(x => x.p === prova.id));
    sorteio = { todas: iguais, mostra: outras.concat(mesma).slice(0, 3) };
    return sorteio;
  }
  function mostrar(prova, i, resposta) {
    respostaAtual = resposta;
    const q = prova.questoes[i], ant = prova.questoes[i - 1], prox = prova.questoes[i + 1], rev = !!resposta;
    const rot = Registro.rotuloOrigem(prova, q), nOrig = (q.origem && q.origem.numeroOriginal) || q.numero;
    document.title = rot + " | Treineiros";
    const alts = Object.keys(q.alternativas).map(l => {
      let cls = "alt", st = "";
      if (rev && q.gabarito !== "ANULADA") {
        if (l === q.gabarito) { cls += " is-correta"; st = resposta === l ? "Você acertou" : "Gabarito"; }
        else if (l === resposta) { cls += " is-errada"; st = "Errada"; }
      } else if (l === resposta) cls += " is-selecionada";
      return `<button type="button" class="${cls}" data-letra="${l}"${rev ? ' aria-disabled="true"' : ""}><span class="alt__letra">${l}</span><span>${Render.alternativa(q, l)}</span><span class="alt__status">${st}</span></button>`;
    }).join("");
    const mais = maisDoAssunto(prova, q);
    const nTreino = mais.todas ? Math.min(10, mais.todas.length + 1) : 0;
    const fonte = prova.fonte ? `com gabarito do ${E(prova.fonte)}` : "com o gabarito oficial";
    const veio = `<p class="sobretitulo">Alguém te mandou esta questão?</p><p>Ela é da prova oficial, ${fonte}. Responda e veja a explicação, sem cadastro.</p>`;
    app.innerHTML = `<div class="qa">
      <aside class="qa__veio qa__veio--topo" aria-label="Sobre esta questão">${veio}</aside>
      <article class="qa__folha questao" aria-labelledby="qt">
        <header class="qa__topo">
          <h1 id="qt" tabindex="-1">Questão ${E(nOrig)} <em>· ${E(curto(prova))}</em></h1>
          <p class="qa__tags"><span class="qa__mat">${E(q.materia)}</span>${q.assunto ? `<span class="qa__ass">${E(q.assunto)}</span>` : ""}${(Array.isArray(q.tags) ? q.tags : []).map(t => `<span class="qa__ass qa__ass--leve">${E(t)}</span>`).join("")}</p>
        </header>
        <div class="qa__corpo">
          ${Render.enunciado(q)}
          <div role="group" aria-label="Alternativas" class="qa__alts">${alts}</div>
          ${rev ? Render.explicacao(q) : `<p class="qa__dica">Toque numa alternativa. A correção comentada aparece logo abaixo.</p>`}
          <div class="qa__acoes">
            ${nTreino > 1 ? `<button type="button" class="btn btn--primary" id="b-treinar">Treinar ${nTreino} de ${E(q.assunto)}</button>` : ""}
            <a class="btn${nTreino > 1 ? "" : " btn--primary"}" href="simulado.html?id=${encodeURIComponent(ID)}">Fazer a prova inteira</a>
            <button type="button" class="btn qa__link" id="b-link"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M10 14a5 5 0 0 0 7 0l3-3a5 5 0 0 0-7-7l-1 1M14 10a5 5 0 0 0-7 0l-3 3a5 5 0 0 0 7 7l1-1"/></svg>Copiar link</button>
          </div>
          <nav class="qa__nav" aria-label="Outras questões desta prova">
            ${ant ? `<a href="?id=${encodeURIComponent(ID)}&n=${ant.numero}">‹ Anterior</a>` : "<span></span>"}
            <button type="button" class="btn btn--ghost" id="b-rep">Reportar erro</button>
            ${prox ? `<a href="?id=${encodeURIComponent(ID)}&n=${prox.numero}">Próxima ›</a>` : "<span></span>"}
          </nav>
        </div>
      </article>
      <div class="qa__lado">
        <aside class="qa__veio qa__veio--lado" aria-label="Sobre esta questão">${veio}</aside>
        ${mais.mostra && mais.mostra.length ? `<section class="qa__mais" aria-labelledby="qa-mais"><h2 id="qa-mais">Mais de ${E(q.assunto)}</h2><ul>${mais.mostra.map(x => {
          const p = lista.find(y => y.id === x.p);
          return `<li><a href="questao.html?id=${encodeURIComponent(x.p)}&n=${x.n}"><b>${E(curto(p) || x.p)}</b><span>Questão ${x.n}</span></a></li>`;
        }).join("")}</ul><a class="qa__busca" href="busca.html?materia=${encodeURIComponent(q.materia)}&assunto=${encodeURIComponent(q.assunto)}">Ver as ${mais.todas.length + 1} questões do assunto</a></section>` : ""}
      </div></div>`;
    app.querySelectorAll(".alt").forEach(b => b.addEventListener("click", () => {
      if (rev) return;
      Registro.somarAtividade(1);
      mostrar(prova, i, b.dataset.letra);
      const ex = app.querySelector(".explicacao"); if (ex) { ex.setAttribute("tabindex", "-1"); ex.focus(); }
    }));
    document.getElementById("b-link").onclick = () => Registro.copiar(location.href).then(ok => falar(ok ? "Link copiado." : "Não foi possível copiar o link."));
    document.getElementById("b-rep").onclick = () => Reportar.abrir(prova, q).then(res => falar(Reportar.mensagem(res)));
    const bt = document.getElementById("b-treinar");
    if (bt) bt.onclick = () => {
      bt.disabled = true;
      const refs = [{ provaId: prova.id, numero: q.numero }].concat(Treino.embaralhar(mais.todas).slice(0, nTreino - 1).map(x => ({ provaId: x.p, numero: +x.n })));
      Dados.provas(refs.map(r => r.provaId)).then(ps => {
        const itens = refs.map(r => ps[r.provaId] && { prova: ps[r.provaId], q: ps[r.provaId].questoes.find(x => x.numero === r.numero) }).filter(x => x && x.q);
        location.href = Treino.montar(`Treino: ${q.assunto}`, itens);
      }).catch(() => { bt.disabled = false; falar("Não foi possível montar o treino agora."); });
    };
    Formulas.renderizar(app);
  }
})();
