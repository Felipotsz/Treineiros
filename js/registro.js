/* Registro: o que o aluno acumula com o tempo (erros, anotações, atividade, estatísticas).
   Tudo fica no navegador, via Armazem. Depende de storage.js e config.js. */
var Registro = (function () {
  function dataStr(d) { return d.getFullYear() + "-" + ("0" + (d.getMonth() + 1)).slice(-2) + "-" + ("0" + d.getDate()).slice(-2); }
  function hoje() { return dataStr(new Date()); }
  function somarDias(str, n) { var d = new Date(str + "T12:00:00"); d.setDate(d.getDate() + n); return dataStr(d); }
  function diasAte(str) { return Math.round((new Date(str + "T12:00:00") - new Date(hoje() + "T12:00:00")) / 86400000); }

  /* Atividade diária e sequência de dias */
  function somarAtividade(n) { var a = Armazem.ler("atividade", {}); a[hoje()] = (a[hoje()] || 0) + n; Armazem.gravar("atividade", a); }
  function sequencia() {
    var a = Armazem.ler("atividade", {}), d = hoje(), n = 0;
    if (!a[d]) d = somarDias(d, -1);            // hoje ainda não conta contra a sequência
    while (a[d]) { n++; d = somarDias(d, -1); }
    return n;
  }

  /* Identificação da questão (serve para prova normal e para treinos montados) */
  function ref(prova, q) { return q.ref || { provaId: prova.id, numero: q.numero }; }
  function chave(r) { return r.provaId + "#" + r.numero; }
  function rotuloOrigem(prova, q) {
    if (q.ref && q.ref.rotulo) return q.ref.rotulo;
    var o = q.origem || {};
    return prova.titulo + (o.caderno ? ", caderno " + o.caderno : "") + ", questão " + (o.numeroOriginal || q.numero);
  }

  /* Caderno de erros com revisão espaçada.
     itens: [{ ref, materia, assunto, status: "acerto"|"erro"|"branco"|"anulada", chute }] */
  function registrarResultado(itens) {
    var erros = Armazem.ler("erros", {}), ints = Config.intervalosRevisaoDias, h = hoje();
    itens.forEach(function (it) {
      var k = chave(it.ref), e = erros[k];
      if (it.status === "erro" || it.status === "branco" || (it.status === "acerto" && it.chute)) {
        if (!e) e = erros[k] = { provaId: it.ref.provaId, numero: it.ref.numero, tentativas: 0 };
        e.materia = it.materia; e.assunto = it.assunto; e.motivo = it.status === "acerto" ? "chute" : it.status;
        e.status = "aberta"; e.nivel = 0; e.ultimo = h; e.proxima = somarDias(h, ints[0]); e.tentativas++;
      } else if (it.status === "acerto" && e && e.status === "aberta") {
        e.nivel++; e.ultimo = h;
        if (e.nivel >= ints.length) e.status = "resolvida"; else e.proxima = somarDias(h, ints[e.nivel]);
      }
    });
    Armazem.gravar("erros", erros);
  }
  function listarErros() {
    var erros = Armazem.ler("erros", {});
    return Object.keys(erros).map(function (k) { return erros[k]; })
      .filter(function (e) { return e && typeof e === "object" && e.provaId && e.numero !== undefined; })   // ignora itens corrompidos
      .map(function (e) { e.materia = e.materia || "Sem matéria"; e.ultimo = e.ultimo || ""; e.tentativas = e.tentativas || 1; return e; })
      .sort(function (a, b) { return a.ultimo < b.ultimo ? 1 : -1; });
  }
  function pendentesHoje() {
    return listarErros().filter(function (e) { return e.status === "aberta" && e.proxima <= hoje(); });
  }

  /* Anotações por questão */
  function nota(r) { return Armazem.ler("notas", {})[chave(r)] || ""; }
  function gravarNota(r, txt) {
    var n = Armazem.ler("notas", {});
    if (txt.trim()) n[chave(r)] = txt; else delete n[chave(r)];
    Armazem.gravar("notas", n);
  }

  /* Estatísticas a partir do histórico de simulados */
  function estatisticas(h) {
    var r = { simulados: h.length, acertos: 0, total: 0, porMateria: {}, porAssunto: {} };
    var n = function (v) { return typeof v === "number" && isFinite(v) ? v : 0; };   // histórico antigo ou importado
    h.forEach(function (x) {
      if (!x || typeof x !== "object") return;
      r.acertos += n(x.acertos); r.total += n(x.total);
      var pm = x.porMateria && typeof x.porMateria === "object" ? x.porMateria : {};
      Object.keys(pm).forEach(function (m) {
        if (!pm[m]) return;
        var a = r.porMateria[m] || (r.porMateria[m] = { acertos: 0, total: 0 });
        a.acertos += n(pm[m].acertos); a.total += n(pm[m].total);
      });
      var pa = x.porAssunto && typeof x.porAssunto === "object" ? x.porAssunto : {};   // simulados antigos não têm
      Object.keys(pa).forEach(function (k) {
        if (!pa[k]) return;
        var a = r.porAssunto[k] || (r.porAssunto[k] = { materia: pa[k].materia, assunto: pa[k].assunto, acertos: 0, total: 0 });
        a.acertos += n(pa[k].acertos); a.total += n(pa[k].total);
      });
    });
    r.pct = r.total ? Math.round(r.acertos / r.total * 100) : 0;
    [r.porMateria, r.porAssunto].forEach(function (grupo) {
      Object.keys(grupo).forEach(function (k) { var a = grupo[k]; a.pct = a.total ? Math.round(a.acertos / a.total * 100) : 0; });
    });
    return r;
  }

  function copiar(texto) {
    if (navigator.clipboard && navigator.clipboard.writeText)
      return navigator.clipboard.writeText(texto).then(function () { return true; }, function () { return false; });
    var t = document.createElement("textarea"), ok = false;
    t.value = texto; t.setAttribute("readonly", ""); t.style.cssText = "position:fixed;opacity:0";
    document.body.appendChild(t); t.select();
    try { ok = document.execCommand("copy"); } catch (e) {}
    t.remove(); return Promise.resolve(ok);
  }

  return { hoje: hoje, somarDias: somarDias, diasAte: diasAte, somarAtividade: somarAtividade, sequencia: sequencia,
           ref: ref, rotuloOrigem: rotuloOrigem, registrarResultado: registrarResultado, listarErros: listarErros,
           pendentesHoje: pendentesHoje, nota: nota, gravarNota: gravarNota, estatisticas: estatisticas, copiar: copiar };
})();
