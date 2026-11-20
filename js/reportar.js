/* Reportar erro numa questão: abre um e-mail para Config.contatoEmail (não exige conta em lugar nenhum);
   sem e-mail, abre um relato no GitHub; sem nenhum dos dois, copia o texto para a pessoa colar onde preferir. */
var Reportar = (function () {
  function abrir(prova, q) {
    var r = Registro.ref(prova, q), rot = Registro.rotuloOrigem(prova, q);
    var corpo = "Questão: " + rot + "\nProva (id): " + r.provaId + "\nNúmero: " + r.numero +
      "\n\nO que está errado (enunciado, alternativa, gabarito ou explicação)?\n";
    var titulo = "Erro na questão: " + rot;
    if (Config.contatoEmail && /@/.test(Config.contatoEmail)) {
      location.href = "mailto:" + Config.contatoEmail + "?subject=" + encodeURIComponent("[Treineiros] " + titulo) + "&body=" + encodeURIComponent(corpo);
      return Promise.resolve("email");
    }
    if (/SEU-USUARIO/.test(Config.repoIssues || "SEU-USUARIO")) {
      return Registro.copiar(corpo).then(function (ok) { return ok ? "copiado" : "falhou"; });
    }
    window.open(Config.repoIssues + "?template=erro-em-questao.yml&title=" + encodeURIComponent(titulo) + "&questao=" + encodeURIComponent(rot) + "&prova=" + encodeURIComponent(r.provaId) + "&numero=" + r.numero + "&body=" + encodeURIComponent(corpo), "_blank", "noopener");
    return Promise.resolve("aberto");
  }
  var textos = {
    aberto: "Abrimos a página para você descrever o erro.",
    email: "Abrimos seu aplicativo de e-mail com o relato pronto para " + Config.contatoEmail + ". Descreva o erro e envie.",
    copiado: "Texto do relato copiado. Cole numa mensagem para quem mantém o site (o contato está nas páginas Sobre e Apoie).",
    falhou: "Não foi possível copiar o texto do relato."
  };
  return { abrir: abrir, mensagem: function (res) { return textos[res] || textos.falhou; } };
})();
