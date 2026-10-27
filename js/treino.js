/* Treino: monta uma "prova virtual" com questões de várias provas (por matéria, erros, revisão do dia). */
var Treino = (function () {
  // ids (opcional): carrega só essas provas. Sem ids, carrega todas.
  function carregarTodas(ids) {
    return fetch("data/provas.json").then(function (r) { if (!r.ok) throw new Error("lista"); return r.json(); }).then(function (lista) {
      if (ids) lista = lista.filter(function (i) { return ids.indexOf(i.id) >= 0; });
      return Promise.all(lista.map(function (i) {
        return fetch(i.arquivo).then(function (r) { if (!r.ok) throw 0; return r.json(); }).catch(function () { return null; });   // prova com problema fica de fora
      }));
    }).then(function (ps) {
      var m = {};
      ps.forEach(function (p) { if (p && p.id && Array.isArray(p.questoes)) m[p.id] = p; });
      return m;
    });
  }
  function embaralhar(v) {
    var a = v.slice();
    for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t; }
    return a;
  }
  // itens: [{ prova, q }]. Guarda a prova virtual e devolve o endereço do simulado.
  function montar(titulo, itens) {
    var qs = itens.map(function (x, i) {
      var q = JSON.parse(JSON.stringify(x.q));
      q.ref = { provaId: x.prova.id, numero: x.q.numero, rotulo: Registro.rotuloOrigem(x.prova, x.q) };
      q.numero = i + 1;
      return q;
    });
    var prova = { id: "treino", banca: "Treino", ano: new Date().getFullYear(), titulo: titulo, fonte: "Questões de várias provas",
                  duracaoMinutos: Math.max(1, qs.length * Config.minutosPorQuestaoTreino), treino: true, questoes: qs };
    Armazem.gravar("treino-ativo", prova);
    // um treino novo substitui o anterior por completo (inclusive o rascunho, que era de outras questões)
    ["andamento:treino", "resultado:treino", "rascunho:treino",
     "andamento:treino:erradas", "resultado:treino:erradas", "rascunho:treino:erradas"].forEach(function (k) { Armazem.apagar(k); });
    return "simulado.html?id=treino";
  }
  /* Lista compartilhável: "prova-a:1.2.3~prova-b:7" (cabe num link, sem servidor) */
  function codificarLista(itens) {          // itens: [{ provaId, numero }]
    var grupos = {}, ordem = [];
    itens.forEach(function (i) { if (!grupos[i.provaId]) { grupos[i.provaId] = []; ordem.push(i.provaId); } grupos[i.provaId].push(i.numero); });
    return ordem.map(function (id) { return id + ":" + grupos[id].join("."); }).join("~");
  }
  function decodificarLista(txt) {
    var itens = [];
    String(txt || "").split("~").forEach(function (g) {
      var p = g.split(":"), id = p[0];
      if (!/^[a-z0-9-]+$/.test(id) || !p[1]) return;
      p[1].split(".").forEach(function (n) { n = parseInt(n, 10); if (n > 0) itens.push({ provaId: id, numero: n }); });
    });
    return itens.slice(0, 200);
  }
  // Monta o endereço completo de uma página do site (para copiar e compartilhar)
  function endereco(pagina) { return new URL(pagina, location.href).href; }
  return { carregarTodas: carregarTodas, embaralhar: embaralhar, montar: montar,
           codificarLista: codificarLista, decodificarLista: decodificarLista, endereco: endereco };
})();
