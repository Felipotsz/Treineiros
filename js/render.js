/* Render: pedaços de HTML de questão usados por todas as páginas (simulado, resultado, questão avulsa,
   busca, caderno de erros, revisão do autor). Só monta texto HTML; quem chama decide onde colocar.
   Enunciados e alternativas vêm do nosso JSON (confiável), por isso entram sem escape.

   Figuras: "imagens" é uma lista; cada item pode ser só o caminho ("assets/img/x.webp") ou um objeto
   { src, alt, legenda }. Para pôr uma figura no meio do texto, escreva [[fig:1]] (1 = primeira da lista)
   no enunciado ou numa alternativa. Figuras sem marcador aparecem depois do enunciado. */
var Render = (function () {
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  // Lista normalizada: [{ src, alt, legenda }]
  function imagens(q) {
    return (Array.isArray(q.imagens) ? q.imagens : []).map(function (im, i) {
      if (typeof im === "string") return { src: im, alt: "Figura " + (i + 1) + " da questão " + q.numero, legenda: "" };
      return { src: im.src, alt: im.alt || "Figura " + (i + 1) + " da questão " + q.numero, legenda: im.legenda || "" };
    });
  }
  // Uma figura. zoom = true: vira botão que amplia (o simulado liga o clique em .figura-btn)
  // ja = true: carrega na hora (figura da questão que está na tela); senão, só quando chegar perto na rolagem
  function figura(im, zoom, ja) {
    var img = '<img class="figura" src="' + esc(im.src) + '" alt="' + esc(im.alt) + '"' + (ja ? "" : ' loading="lazy"') + ' decoding="async">';
    var corpo = zoom ? '<button type="button" class="figura-btn" data-src="' + esc(im.src) + '" data-alt="' + esc(im.alt) + '" aria-label="Ampliar: ' + esc(im.alt) + '">' + img + "</button>" : img;
    return '<figure class="fig">' + corpo + (im.legenda ? "<figcaption>" + im.legenda + "</figcaption>" : "") + "</figure>";
  }
  // Troca os marcadores [[fig:N]] de um trecho de HTML. "usadas" anota quais já apareceram.
  function comFiguras(html, lista, zoom, usadas, ja) {
    return String(html || "").replace(/\[\[fig:(\d+)\]\]/g, function (m, n) {
      var im = lista[+n - 1];
      if (!im) return "";
      usadas[+n - 1] = true;
      return figura(im, zoom, ja);
    });
  }
  // Enunciado completo, com as figuras no lugar certo. opcoes: { zoom }
  function enunciado(q, opcoes) {
    opcoes = opcoes || {};
    var lista = imagens(q), usadas = {};
    var html = comFiguras(q.enunciado, lista, opcoes.zoom, usadas, opcoes.ja);
    // figuras citadas só nas alternativas não se repetem aqui
    Object.keys(q.alternativas || {}).forEach(function (l) { String(q.alternativas[l]).replace(/\[\[fig:(\d+)\]\]/g, function (m, n) { usadas[+n - 1] = true; }); });
    var resto = lista.filter(function (im, i) { return !usadas[i]; }).map(function (im) { return figura(im, opcoes.zoom, opcoes.ja); }).join("");
    return '<div class="enunciado">' + html + "</div>" + resto;
  }
  // Texto de uma alternativa (pode ter figura)
  function alternativa(q, letra, opcoes) {
    return comFiguras(q.alternativas[letra], imagens(q), opcoes && opcoes.zoom, {});
  }
  // Alternativas como lista (sem interação). destacar = letra do gabarito ("" = não mostrar);
  // marcada = resposta do aluno (aparece como "Sua resposta" se estiver errada)
  function alternativas(q, destacar, marcada) {
    return '<ol class="alts-lista">' + Object.keys(q.alternativas).map(function (l) {
      var ok = destacar && l === destacar, errada = marcada && l === marcada && !ok;
      return '<li class="' + (ok ? "is-correta" : errada ? "is-errada" : "") + '"><span class="alt__letra">' + l + "</span><span>" + alternativa(q, l) + "</span>" +
        (ok ? '<span class="alt__status">' + (marcada === l ? "Sua resposta, correta" : "Gabarito") + "</span>" : errada ? '<span class="alt__status">Sua resposta</span>' : "") + "</li>";
    }).join("") + "</ol>";
  }
  /* Questão anulada: a justificativa diz se é oficial (da banca) ou análise nossa */
  function anulacao(q) {
    if (q.gabarito !== "ANULADA") return "";
    var a = q.anulacao || {};
    var origem = a.fonte === "oficial" ? "Justificativa oficial da banca" : "Análise do Treineiros (a banca não divulgou o motivo)";
    return '<div class="anulada" role="note"><p class="anulada__titulo">Questão anulada pela banca</p>' +
      "<p>Ela vale ponto para todos os candidatos, qualquer que seja a resposta.</p>" +
      (a.motivo ? '<p class="anulada__origem">' + origem + "</p>" + a.motivo : "") + "</div>";
  }
  function retificacao(q) {
    if (!q.retificada) return "";
    return '<p class="legenda">Gabarito retificado: a banca corrigiu a resposta desta questão depois da primeira divulgação. Aqui está a versão corrigida.</p>';
  }
  function estatistica(q) {
    return q.estatistica && typeof q.estatistica.pctAcerto === "number"
      ? '<p class="legenda">No Enem, ' + String(q.estatistica.pctAcerto).replace(".", ",") + "% dos candidatos acertaram esta questão (microdados do Inep).</p>" : "";
  }
  // Explicação completa: anulação, gabarito comentado, retificação, estatística e selo de revisão
  function explicacao(q, opcoes) {
    opcoes = opcoes || {};
    return anulacao(q) + '<div class="explicacao"' + (opcoes.id ? ' id="' + opcoes.id + '" tabindex="-1"' : "") + '><span class="explicacao__rotulo">Correção comentada</span>' +
      (q.explicacao ? q.explicacao.indexOf("<p") === 0 ? q.explicacao : "<p>" + q.explicacao + "</p>" : "<p>Sem explicação cadastrada.</p>") +
      retificacao(q) + estatistica(q) +
      '<p><span class="tag">' + (q.explicacaoRevisada ? "Explicação revisada" : "Explicação ainda não revisada") + "</span></p></div>";
  }
  // Tags de matéria, assunto e marcadores (ex.: interdisciplinar)
  function tags(q) {
    var extra = (Array.isArray(q.tags) ? q.tags : []).map(function (t) { return ' <span class="tag tag--leve">' + esc(t) + "</span>"; }).join("");
    return '<p class="tags"><span class="tag">' + esc(q.materia) + "</span>" + (q.assunto ? ' <span class="tag">' + esc(q.assunto) + "</span>" : "") + extra + "</p>";
  }
  // Texto puro (sem HTML), para busca
  function textoPuro(html) { return String(html || "").replace(/\[\[fig:\d+\]\]/g, " ").replace(/<[^>]+>/g, " ").replace(/&nbsp;/g, " ").replace(/\s+/g, " ").trim(); }
  // Normaliza para busca: minúsculas e sem acentos
  function normalizar(s) { return String(s).toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, ""); }
  // Nome da edição para mostrar ("ETEC · 2º sem/2026 · prova em 21/06/2026")
  function edicao(p) {
    var partes = [p.banca];
    if (p.semestre) partes.push(p.semestre + "º semestre de " + p.ano); else partes.push(String(p.ano));
    return partes.join(" · ");
  }
  function dataBr(iso) { return iso ? iso.split("-").reverse().join("/") : ""; }
  return { esc: esc, imagens: imagens, figura: figura, enunciado: enunciado, alternativa: alternativa, alternativas: alternativas,
           anulacao: anulacao, explicacao: explicacao, tags: tags, textoPuro: textoPuro, normalizar: normalizar,
           edicao: edicao, dataBr: dataBr, figuras: function (q) { return imagens(q).map(function (im) { return figura(im, false); }).join(""); } };
})();
