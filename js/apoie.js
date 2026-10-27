/* Página "Apoie": mostra o QR code e a chave Pix configurados em Config.apoio.
   Sem chave configurada, fica o aviso "Pix em breve" que já está no HTML (nada quebra). */
(function () {
  var cfg = (window.Config && Config.apoio) || {};
  var chave = (cfg.pixChave || "").trim();
  if (!chave) return;

  var caixaQr = document.getElementById("pix-qr"), caixaChave = document.getElementById("pix-chave");

  // QR code: só troca o aviso pela imagem se ela carregar de verdade
  if (cfg.pixQr) {
    var img = new Image();
    img.alt = "QR code do Pix para apoiar o Treineiros" + (cfg.pixNome ? ", em nome de " + cfg.pixNome : "");
    img.onload = function () { caixaQr.textContent = ""; caixaQr.classList.remove("pix__qr--vazio"); caixaQr.appendChild(img); };
    img.src = cfg.pixQr;
  }

  caixaChave.innerHTML =
    "<p>Aponte a câmera do app do seu banco para o QR code, ou copie a chave aleatória abaixo e cole na opção Pix com chave." +
    (cfg.pixNome ? " O nome que vai aparecer é <strong></strong>." : "") + "</p>" +
    '<p class="pix__chave"><code id="pix-txt"></code><button type="button" class="btn" id="pix-copiar">Copiar chave</button></p>';
  if (cfg.pixNome) caixaChave.querySelector("strong").textContent = cfg.pixNome;
  document.getElementById("pix-txt").textContent = chave;

  var botao = document.getElementById("pix-copiar");
  botao.addEventListener("click", function () {
    function ok() { botao.textContent = "Chave copiada"; if (window.anunciar) anunciar("Chave Pix copiada"); setTimeout(function () { botao.textContent = "Copiar chave"; }, 2500); }
    function manual() {                                       // sem acesso à área de transferência: seleciona o texto
      var r = document.createRange(); r.selectNodeContents(document.getElementById("pix-txt"));
      var s = getSelection(); s.removeAllRanges(); s.addRange(r);
      if (window.anunciar) anunciar("Chave selecionada. Use copiar do seu aparelho.");
    }
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(chave).then(ok, manual); else manual();
  });
})();
