/* Armazem: guarda os dados do aluno no navegador, sem nunca quebrar a página.
   1º localStorage (permanente). Se estiver bloqueado ou cheio:
   2º sessionStorage (vale até fechar a aba). Se também falhar:
   3º memória guardada em window.name (sobrevive a trocar de página na mesma aba).
   Ler sempre devolve o padrão quando o dado salvo está corrompido ou tem tipo diferente
   (ex.: backup importado de outra versão). */
var Armazem = (function () {
  var P = "treineiros:", MARCA = "treineiros-memoria:";
  var modo = "local";                       // "local" | "sessao" | "memoria": onde a última gravação foi parar

  function areaDe(nome) { try { return window[nome] || null; } catch (e) { return null; } }
  function testar(a) {
    if (!a) return false;
    try { a.setItem(P + "__teste", "1"); a.removeItem(P + "__teste"); return true; } catch (e) { return false; }
  }
  var local = areaDe("localStorage"), sessao = areaDe("sessionStorage");
  if (!testar(local)) { local = null; modo = testar(sessao) ? "sessao" : "memoria"; }
  if (!testar(sessao)) sessao = null;

  // Memória da aba: guardada em window.name para não se perder ao navegar entre as páginas do site.
  var memoria = {};
  try { if (window.name.indexOf(MARCA) === 0) memoria = JSON.parse(window.name.slice(MARCA.length)) || {}; } catch (e) { memoria = {}; }
  function salvarMemoria() {
    try { window.name = Object.keys(memoria).length ? MARCA + JSON.stringify(memoria) : ""; } catch (e) {}
  }

  function mesmoTipo(v, padrao) {
    if (padrao === null || padrao === undefined) return true;
    if (Array.isArray(padrao)) return Array.isArray(v);
    if (typeof padrao === "object") return v !== null && typeof v === "object" && !Array.isArray(v);
    return typeof v === typeof padrao;
  }
  // A cópia mais nova fica na camada mais "frágil" (memória > sessão > local), então lê nessa ordem.
  function cru(k) {
    if (Object.prototype.hasOwnProperty.call(memoria, P + k)) return memoria[P + k];
    try { if (sessao) { var s = sessao.getItem(P + k); if (s !== null) return s; } } catch (e) {}
    try { if (local) return local.getItem(P + k); } catch (e) {}
    return null;
  }
  function ler(k, padrao) {
    var v = cru(k);
    if (v === null || v === undefined || v === "") return padrao;
    try { v = JSON.parse(v); } catch (e) { return padrao; }
    return mesmoTipo(v, padrao) ? v : padrao;
  }
  function gravar(k, v) {
    var txt;
    try { txt = JSON.stringify(v); } catch (e) { return false; }
    try {
      if (local) {
        local.setItem(P + k, txt);
        // gravou no lugar certo: remove cópias provisórias que ficariam "mais novas"
        try { if (sessao) sessao.removeItem(P + k); } catch (e) {}
        if (P + k in memoria) { delete memoria[P + k]; salvarMemoria(); }
        modo = "local";
        return true;
      }
    } catch (e) {}
    try { if (sessao) { sessao.setItem(P + k, txt); modo = "sessao"; return false; } } catch (e) {}
    memoria[P + k] = txt; salvarMemoria(); modo = "memoria";
    return false;                              // false = não ficou salvo de forma permanente
  }
  function apagar(k) {
    try { if (local) local.removeItem(P + k); } catch (e) {}
    try { if (sessao) sessao.removeItem(P + k); } catch (e) {}
    if (P + k in memoria) { delete memoria[P + k]; salvarMemoria(); }
  }
  return { ler: ler, gravar: gravar, apagar: apagar, modo: function () { return modo; } };
})();
