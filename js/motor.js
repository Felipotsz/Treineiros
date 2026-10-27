/* Motor: lógica pura, sem DOM. Fácil de testar e de portar para React. */
var Motor = (function () {
  function fmt(seg) {
    seg = Math.max(0, Math.round(seg));
    var h = Math.floor(seg / 3600), m = Math.floor((seg % 3600) / 60), s = seg % 60;
    var mm = (m < 10 ? "0" : "") + m, ss = (s < 10 ? "0" : "") + s;
    return h ? h + ":" + mm + ":" + ss : mm + ":" + ss;
  }
  function duracaoTexto(min) {
    if (min < 60) return min + " min";
    var h = Math.floor(min / 60), m = min % 60;
    return m ? h + "h" + (m < 10 ? "0" : "") + m : h + "h";
  }
  // modo: "oficial" | "personalizado" | "nenhum"
  function duracaoSeg(prova, modo, minutos) {
    if (modo === "oficial") return prova.duracaoMinutos * 60;
    if (modo === "personalizado") return Math.round(minutos * 60);
    return null;
  }
  // correcao: "imediata" (modo estudo) | "final" (modo prova)
  // formato: "tela" (uma questão por vez) | "cartao" (prova no papel, só o cartão-resposta na tela; corrige no final)
  function novoEstado(prova, modo, minutos, correcao, formato) {
    var cartao = formato === "cartao";
    return {
      versao: 2, provaId: prova.id, numeros: prova.questoes.map(function (q) { return q.numero; }),
      config: { modo: modo, minutos: modo === "personalizado" ? minutos : null, correcao: cartao || correcao === "final" ? "final" : "imediata",
                formato: cartao ? "cartao" : "tela" },
      tempoRestanteSeg: duracaoSeg(prova, modo, minutos), tempoGastoSeg: 0, atual: 0,
      respostas: {}, marcadas: [], eliminadas: {}, chutes: [], tempos: {}, pausado: false, finalizado: false
    };
  }
  // A correção só aparece se a resposta existe e o modo não é "prova".
  function revelado(estado, numero) {
    return !!estado.respostas[numero] && !(estado.config && estado.config.correcao === "final");
  }
  function responder(estado, numero, letra) {
    if (revelado(estado, numero)) return false;          // modo estudo: resposta travada
    if (estado.respostas[numero] === letra) return false;
    estado.respostas[numero] = letra; return true;
  }
  function alternarEm(lista, n) { var i = lista.indexOf(n); if (i < 0) lista.push(n); else lista.splice(i, 1); }
  function alternarMarca(estado, numero) { alternarEm(estado.marcadas, numero); }
  function alternarChute(estado, numero) { estado.chutes = estado.chutes || []; alternarEm(estado.chutes, numero); }
  function alternarEliminada(estado, numero, letra) {
    estado.eliminadas = estado.eliminadas || {};
    alternarEm(estado.eliminadas[numero] || (estado.eliminadas[numero] = []), letra);
  }
  function pendentes(estado, prova) {
    return prova.questoes.filter(function (q) { return !estado.respostas[q.numero]; }).map(function (q) { return q.numero; });
  }
  // Avança o relógio em "dt" segundos. Devolve true se o tempo acabou.
  function tickear(estado, dt) {
    dt = dt || 1;
    estado.tempoGastoSeg += dt;
    if (estado.numeros) {                                  // tempo gasto em cada questão
      var n = estado.numeros[estado.atual];
      estado.tempos = estado.tempos || {};
      estado.tempos[n] = (estado.tempos[n] || 0) + dt;
    }
    if (estado.tempoRestanteSeg === null) return false;
    estado.tempoRestanteSeg = Math.max(0, estado.tempoRestanteSeg - dt);
    return estado.tempoRestanteSeg === 0;
  }
  // Conserta um estado salvo (versão antiga, backup importado ou prova cujo JSON mudou).
  // Remove o que não existe mais na prova e completa campos que faltam. Devolve null se não der para usar.
  function normalizarEstado(e, prova) {
    if (!e || typeof e !== "object" || Array.isArray(e) || !prova || !prova.questoes || !prova.questoes.length) return null;
    var porNumero = {}, nums = prova.questoes.map(function (q) { porNumero[q.numero] = q; return q.numero; });
    var obj = function (v) { return v && typeof v === "object" && !Array.isArray(v) ? v : {}; };
    var lista = function (v) { return (Array.isArray(v) ? v : []).filter(function (n) { return porNumero[n]; }); };
    var num = function (v) { return typeof v === "number" && isFinite(v) && v >= 0; };

    var resp = obj(e.respostas), r2 = {};
    Object.keys(resp).forEach(function (n) { var q = porNumero[n]; if (q && q.alternativas[resp[n]]) r2[n] = resp[n]; });
    e.respostas = r2;
    e.marcadas = lista(e.marcadas); e.chutes = lista(e.chutes);
    var el = obj(e.eliminadas), el2 = {};
    Object.keys(el).forEach(function (n) { if (porNumero[n] && Array.isArray(el[n])) el2[n] = el[n]; });
    e.eliminadas = el2;
    e.tempos = obj(e.tempos);

    var c = obj(e.config);
    if (["oficial", "personalizado", "nenhum"].indexOf(c.modo) < 0) c.modo = e.tempoRestanteSeg === null ? "nenhum" : "oficial";
    if (c.modo === "personalizado" && !(c.minutos > 0)) c.modo = "oficial";
    c.formato = c.formato === "cartao" ? "cartao" : "tela";
    c.correcao = c.formato === "cartao" || c.correcao === "final" ? "final" : "imediata";
    e.config = c;
    if (c.modo === "nenhum") e.tempoRestanteSeg = null;
    else if (!num(e.tempoRestanteSeg)) e.tempoRestanteSeg = duracaoSeg(prova, c.modo, c.minutos);
    if (!num(e.tempoGastoSeg)) e.tempoGastoSeg = 0;

    e.numeros = nums;
    e.atual = typeof e.atual === "number" && e.atual >= 0 && e.atual < nums.length ? Math.floor(e.atual) : 0;
    e.pausado = !!e.pausado; e.finalizado = !!e.finalizado;
    e.versao = 2;
    return e;
  }
  // Quantas questões DESTA prova têm resposta (ignora respostas soltas de versões antigas).
  function respondidas(estado, prova) {
    return prova.questoes.filter(function (q) { return !!estado.respostas[q.numero]; }).length;
  }
  /* ---- Estimativa de nota TRI (Enem) ----
     Modelo logístico de 3 parâmetros e estimação EAP com distribuição a priori normal padrão, como descrito pelo Inep.
     itens: [{ a, b, c, acertou }]. opcoes: { D, media, dp }. Devolve { theta, nota } ou null.
     É uma ESTIMATIVA: o Inep usa detalhes de cálculo que não são públicos, então a nota oficial pode diferir. */
  function estimarTRI(itens, opcoes) {
    opcoes = opcoes || {};
    var D = opcoes.D || 1, media = opcoes.media === undefined ? 500 : opcoes.media, dp = opcoes.dp || 100;
    itens = (itens || []).filter(function (i) { return i && isFinite(i.a) && isFinite(i.b) && isFinite(i.c); });
    if (!itens.length) return null;
    var soma = 0, pesos = 0;
    for (var t = -4; t <= 4.0001; t += 0.05) {              // quadratura simples
      var log = -t * t / 2;                                    // priori normal (sem a constante, que se cancela)
      for (var k = 0; k < itens.length; k++) {
        var it = itens[k], p = it.c + (1 - it.c) / (1 + Math.exp(-D * it.a * (t - it.b)));
        p = Math.min(Math.max(p, 1e-9), 1 - 1e-9);
        log += it.acertou ? Math.log(p) : Math.log(1 - p);
      }
      var w = Math.exp(log); soma += t * w; pesos += w;
    }
    if (!pesos) return null;
    var theta = soma / pesos;
    return { theta: theta, nota: Math.round(media + dp * theta) };
  }
  // Pontuação com acréscimo percentual (ex.: ETEC: escola pública +10%, afrodescendente +3%)
  function comAcrescimo(pontos, percentual) { return Math.round(pontos * (1 + (percentual || 0) / 100) * 100) / 100; }

  /* Redação: palavras e linhas estimadas na folha oficial (cerca de 75 caracteres por linha; cada parágrafo começa linha nova) */
  function contarRedacao(texto, caracteresPorLinha) {
    var cpl = caracteresPorLinha || 75, t = String(texto || "");
    var palavras = (t.match(/[A-Za-zÀ-ÿ0-9]+(?:[-'][A-Za-zÀ-ÿ0-9]+)*/g) || []).length;
    var linhas = t.split(/\n/).reduce(function (n, par) { return n + (par.trim() ? Math.ceil(par.trim().length / cpl) : 0); }, 0);
    return { palavras: palavras, linhas: linhas, caracteres: t.length };
  }
  function chaveAssunto(q) { return q.assunto ? q.materia + " · " + q.assunto : ""; }
  function pontuar(estado, prova) {
    var r = { acertos: 0, erros: 0, brancas: 0, total: prova.questoes.length, porMateria: {}, porAssunto: {}, revisar: [] };
    prova.questoes.forEach(function (q) {
      var m = r.porMateria[q.materia] || (r.porMateria[q.materia] = { acertos: 0, total: 0 });
      // por assunto: a chave junta matéria e assunto, porque o mesmo nome pode existir em duas matérias
      var ka = chaveAssunto(q), a = ka ? (r.porAssunto[ka] || (r.porAssunto[ka] = { materia: q.materia, assunto: q.assunto, acertos: 0, total: 0 })) : null;
      var resp = estado.respostas[q.numero], certo = false;
      if (q.gabarito === "ANULADA") { r.acertos++; m.acertos++; m.total++; return; }   // anulada vale ponto para todos (não entra no assunto)
      m.total++; if (a) a.total++;
      if (!resp) { r.brancas++; r.revisar.push({ q: q, resposta: null }); }
      else if (resp === q.gabarito) { r.acertos++; m.acertos++; certo = true; }
      else { r.erros++; r.revisar.push({ q: q, resposta: resp }); }
      if (a && certo) a.acertos++;
    });
    r.percentual = r.total ? Math.round(r.acertos / r.total * 100) : 0;
    return r;
  }
  return { fmt: fmt, duracaoTexto: duracaoTexto, duracaoSeg: duracaoSeg, novoEstado: novoEstado, revelado: revelado,
           responder: responder, alternarMarca: alternarMarca, alternarChute: alternarChute, alternarEliminada: alternarEliminada,
           pendentes: pendentes, tickear: tickear, pontuar: pontuar, normalizarEstado: normalizarEstado, respondidas: respondidas, chaveAssunto: chaveAssunto,
           estimarTRI: estimarTRI, comAcrescimo: comAcrescimo, contarRedacao: contarRedacao };
})();
if (typeof module !== "undefined") module.exports = Motor; // para testar no Node
