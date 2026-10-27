/* Transferir: leva o progresso para outro aparelho por um link (que vira QR code).
   Os dados vão no "#" do endereço: essa parte nunca é enviada ao servidor.
   Formato: importar.html#d=<z|j><base64url>  (z = comprimido com deflate, j = JSON puro) */
var Transferir = (function () {
  var P = "treineiros:";
  var LIMITE = 2300;                 // caracteres do link que ainda cabem num QR code legível pela câmera
  // O que vai no QR: o essencial do estudo. Andamentos, resultados e treinos são grandes e ficam de fora.
  var CHAVES = ["erros", "historico", "notas", "atividade", "meta", "alvo", "prefs"];

  function b64url(bytes) {
    var s = ""; for (var i = 0; i < bytes.length; i++) s += String.fromCharCode(bytes[i]);
    return btoa(s).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
  }
  function deB64url(txt) {
    var s = atob(txt.replace(/-/g, "+").replace(/_/g, "/")), b = new Uint8Array(s.length);
    for (var i = 0; i < s.length; i++) b[i] = s.charCodeAt(i);
    return b;
  }
  function comprimir(texto) {
    var bytes = new TextEncoder().encode(texto);
    if (typeof CompressionStream === "undefined") return Promise.resolve("j" + b64url(bytes));
    var fluxo = new Blob([bytes]).stream().pipeThrough(new CompressionStream("deflate-raw"));
    return new Response(fluxo).arrayBuffer().then(function (buf) { return "z" + b64url(new Uint8Array(buf)); });
  }
  function descomprimir(txt) {
    var bytes = deB64url(txt.slice(1));
    if (txt[0] === "j") return Promise.resolve(new TextDecoder().decode(bytes));
    if (typeof DecompressionStream === "undefined") return Promise.reject(new Error("navegador antigo"));
    var fluxo = new Blob([bytes]).stream().pipeThrough(new DecompressionStream("deflate-raw"));
    return new Response(fluxo).text();
  }
  function coletar(maxHistorico) {
    var d = {};
    CHAVES.forEach(function (k) {
      var v = Armazem.ler(k, null);
      if (v === null) return;
      if (k === "historico" && Array.isArray(v)) v = v.slice(0, maxHistorico).map(function (h) {   // sem campos pesados
        return { provaId: h.provaId, titulo: h.titulo, banca: h.banca, treino: h.treino, data: h.data, acertos: h.acertos, total: h.total,
                 percentual: h.percentual, tempoGastoSeg: h.tempoGastoSeg, porMateria: h.porMateria, porAssunto: h.porAssunto };
      });
      d[k] = v;
    });
    return d;
  }
  // Devolve { url, cortado } ou rejeita com "grande" se nem o mínimo couber.
  function gerarLink(base) {
    var tentativas = [50, 20, 10, 5, 0];
    function tentar(i) {
      if (i >= tentativas.length) return Promise.reject(new Error("grande"));
      var dados = coletar(tentativas[i]);
      if (i === tentativas.length - 1) delete dados.notas;              // último recurso: sem as anotações
      return comprimir(JSON.stringify({ v: 1, d: dados })).then(function (z) {
        var url = base + "#d=" + z;
        return url.length <= LIMITE ? { url: url, cortado: i > 0 } : tentar(i + 1);
      });
    }
    return tentar(0);
  }
  function lerLink(hash) {
    var m = /[#&]d=([A-Za-z0-9_-]+)/.exec(hash || "");
    if (!m) return Promise.reject(new Error("sem dados"));
    return descomprimir(m[1]).then(function (t) {
      var o = JSON.parse(t);
      if (!o || o.v !== 1 || typeof o.d !== "object") throw new Error("inválido");
      return o.d;
    });
  }
  // Grava o que veio do outro aparelho. O histórico é somado (sem repetir), o resto é substituído.
  function aplicar(d) {
    var n = 0;
    Object.keys(d).forEach(function (k) {
      if (CHAVES.indexOf(k) < 0) return;
      var v = d[k];
      if (k === "historico" && Array.isArray(v)) {
        var atual = Armazem.ler("historico", []), vistos = {};
        atual.concat(v).forEach(function (h) { if (h && h.data) vistos[h.data + h.provaId] = h; });
        v = Object.keys(vistos).map(function (x) { return vistos[x]; }).sort(function (a, b) { return a.data < b.data ? 1 : -1; }).slice(0, 50);
      }
      Armazem.gravar(k, v); n++;
    });
    return n;
  }
  return { gerarLink: gerarLink, lerLink: lerLink, aplicar: aplicar, CHAVES: CHAVES, P: P };
})();
