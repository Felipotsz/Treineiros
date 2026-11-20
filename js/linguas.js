/* Enem, Linguagens: a língua estrangeira é escolhida na abertura do simulado (Inglês, Espanhol ou as duas).
   - Inglês e Espanhol são as provas de sempre (enem-AAAA-linguagens-ingles / -espanhol): andamento e resultado não mudam.
   - "As duas" é uma prova montada na hora (enem-AAAA-linguagens-ambas): as 5 de Inglês, as 5 de Espanhol e as 40 comuns,
     numeradas de 1 a 50, cada questão com a referência da prova de origem (q.ref), como nos treinos. */
var Linguas = (function () {
  var RE = /^(enem-\d{4}-linguagens)-(ingles|espanhol|ambas)$/;
  var NOMES = { ingles: "Inglês", espanhol: "Espanhol", ambas: "Inglês e Espanhol" };
  var LINGUA_DA = { ingles: "Inglês", espanhol: "Espanhol" };

  function partes(id) { var m = RE.exec(id || ""); return m ? { base: m[1], lingua: m[2] } : null; }
  // a edição tem as duas versões publicadas? (as mais antigas não têm escolha de língua)
  function temEscolha(id, lista) {
    var p = partes(id); if (!p) return false;
    return ["ingles", "espanhol"].every(function (l) { return lista.some(function (x) { return x.id === p.base + "-" + l; }); });
  }
  function baixar(item) { return fetch(item.arquivo).then(function (r) { if (!r.ok) throw new Error(r.status === 404 ? "nao-encontrada" : "rede"); return r.json(); }); }

  // monta a prova "as duas línguas" a partir da lista (data/provas.json)
  function compor(id, lista) {
    var p = partes(id);
    if (!p || p.lingua !== "ambas" || !temEscolha(id, lista)) return Promise.reject(new Error("nao-encontrada"));
    var item = function (l) { return lista.filter(function (x) { return x.id === p.base + "-" + l; })[0]; };
    return Promise.all([baixar(item("ingles")), baixar(item("espanhol"))]).then(function (ps) {
      var ing = ps[0], esp = ps[1];
      var deIng = ing.questoes.filter(function (q) { return q.materia === "Inglês"; });
      var deEsp = esp.questoes.filter(function (q) { return q.materia === "Espanhol"; });
      var comuns = ing.questoes.filter(function (q) { return q.materia !== "Inglês"; });
      var itens = deIng.map(function (q) { return [ing, q]; }).concat(deEsp.map(function (q) { return [esp, q]; }), comuns.map(function (q) { return [ing, q]; }));
      var qs = itens.map(function (x, i) {
        var q = JSON.parse(JSON.stringify(x[1]));
        q.ref = { provaId: x[0].id, numero: x[1].numero, rotulo: Registro.rotuloOrigem(x[0], x[1]) };
        q.numero = i + 1;
        delete q.origem;                                   // a numeração do caderno não vale aqui: são 50 questões seguidas
        return q;
      });
      var extra = qs.length - ing.questoes.length;
      return {
        id: id, banca: "Enem", ano: ing.ano, dia: ing.dia, fonte: ing.fonte, dataExame: ing.dataExame,
        titulo: String(ing.titulo).replace("(Inglês)", "(Inglês e Espanhol)"), area: "Linguagens (Inglês e Espanhol)",
        duracaoMinutos: Math.round(ing.duracaoMinutos * qs.length / ing.questoes.length),
        rotuloTempo: "A duração oficial mais o tempo proporcional às " + extra + " questões a mais",
        composta: true, questoes: qs,
        apresentacao: "<p><strong>Treino com as duas línguas:</strong> as " + deIng.length + " questões de Inglês, as " + deEsp.length +
          " de Espanhol e as " + comuns.length + " comuns. No Enem de verdade você responde só a língua que escolheu na inscrição; aqui o resultado conta todas.</p>"
      };
    });
  }
  return { partes: partes, temEscolha: temEscolha, compor: compor, NOMES: NOMES, LINGUA_DA: LINGUA_DA };
})();
