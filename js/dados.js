/* Dados: carrega os arquivos do site uma vez só por página e guarda a promessa (cache em memória).
   No celular isso importa: uma prova inteira só é baixada quando alguém realmente precisa dela.
   - lista()          → data/provas.json  (provas disponíveis)
   - edicoes()        → data/edicoes.json (todas as edições, inclusive sem prova)
   - indice()         → data/indice-questoes.json (matéria/assunto de cada questão: leve)
   - prova(id)        → data/provas/<id>.json
   - provas([ids])    → { id: prova } só das pedidas */
var Dados = (function () {
  var cache = {};
  function json(url) {
    if (!cache[url]) cache[url] = fetch(url).then(function (r) { if (!r.ok) throw new Error(r.status === 404 ? "nao-encontrada" : "rede"); return r.json(); });
    // se der erro, permite tentar de novo depois (ex.: voltou a internet)
    cache[url].catch(function () { delete cache[url]; });
    return cache[url];
  }
  function lista() { return json("data/provas.json").then(function (l) { return Array.isArray(l) ? l : []; }); }
  function edicoes() { return json("data/edicoes.json").then(function (d) { return (d && d.edicoes) || []; }).catch(function () { return []; }); }
  function indice() { return json("data/indice-questoes.json").then(function (l) { return Array.isArray(l) ? l : []; }); }
  function prova(id) {
    return lista().then(function (l) {
      var item = l.filter(function (p) { return p.id === id; })[0];
      if (!item) throw new Error("nao-encontrada");
      return json(item.arquivo);
    });
  }
  function provas(ids) {
    var unicos = ids.filter(function (x, i) { return ids.indexOf(x) === i; });
    return Promise.all(unicos.map(function (id) { return prova(id).catch(function () { return null; }); })).then(function (ps) {
      var m = {}; ps.forEach(function (p) { if (p && Array.isArray(p.questoes)) m[p.id] = p; }); return m;
    });
  }
  // Busca a questão (objeto completo) de uma referência { provaId, numero }
  function questao(ref) {
    return prova(ref.provaId).then(function (p) {
      return { prova: p, q: p.questoes.filter(function (q) { return q.numero === ref.numero; })[0] || null };
    });
  }
  return { lista: lista, edicoes: edicoes, indice: indice, prova: prova, provas: provas, questao: questao, json: json };
})();
