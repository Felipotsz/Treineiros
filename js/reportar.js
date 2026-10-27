/* Reportar erro numa questão: abre um relato no GitHub ou, sem repositório configurado, copia o texto. */
var Reportar = (function () {
  function abrir(prova, q) {
    var r = Registro.ref(prova, q), rot = Registro.rotuloOrigem(prova, q);
    var corpo = "Questão: " + rot + "\nProva (id): " + r.provaId + "\nNúmero: " + r.numero +
      "\n\nO que está errado (enunciado, alternativa, gabarito ou explicação)?\n";
    if (/SEU-USUARIO/.test(Config.repoIssues))
      return Registro.copiar(corpo).then(function (ok) { return ok ? "copiado" : "falhou"; });
    window.open(Config.repoIssues + "?title=" + encodeURIComponent("Erro na questão: " + rot) + "&body=" + encodeURIComponent(corpo), "_blank", "noopener");
    return Promise.resolve("aberto");
  }
  var textos = {
    aberto: "Abrimos a página para você descrever o erro.",
    copiado: "Texto do relato copiado. Cole numa mensagem para quem mantém o site.",
    falhou: "Não foi possível copiar o texto do relato."
  };
  return { abrir: abrir, mensagem: function (res) { return textos[res] || textos.falhou; } };
})();
