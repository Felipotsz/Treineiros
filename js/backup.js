/* Exportar e importar o progresso (não há login, então o progresso mora no navegador). */
(function () {
  var P = "treineiros:";
  function coletar() {
    var d = {};
    try {
      for (var i = 0; i < localStorage.length; i++) {
        var k = localStorage.key(i);
        if (k.indexOf(P) === 0 && k !== P + "tema") d[k] = localStorage.getItem(k);
      }
    } catch (e) {}
    return { app: "treineiros", versao: 1, exportadoEm: new Date().toISOString(), dados: d };
  }
  function exportar() {
    var c = coletar(), url = URL.createObjectURL(new Blob([JSON.stringify(c, null, 2)], { type: "application/json" }));
    var a = document.createElement("a");
    a.href = url; a.download = "treineiros-progresso-" + c.exportadoEm.slice(0, 10) + ".json";
    document.body.appendChild(a); a.click(); a.remove();
    setTimeout(function () { URL.revokeObjectURL(url); }, 1000);
    return Object.keys(c.dados).length;
  }
  function importar(texto) {
    var obj = JSON.parse(texto);
    if (!obj || obj.app !== "treineiros" || typeof obj.dados !== "object") throw new Error("arquivo inválido");
    var n = 0;
    Object.keys(obj.dados).forEach(function (k) {
      if (k.indexOf(P) !== 0 || typeof obj.dados[k] !== "string") return;
      try { JSON.parse(obj.dados[k]); localStorage.setItem(k, obj.dados[k]); n++; } catch (e) {}
    });
    return n;
  }
  var status = document.getElementById("bk-status"), bExp = document.getElementById("b-exp"), fImp = document.getElementById("f-imp");
  if (!bExp || !fImp) return;

  /* QR code com o progresso (js/transferir.js + assets/vendor/qrcode.js) */
  var bQr = document.getElementById("b-qr"), caixa = document.getElementById("qr");
  if (bQr && window.Transferir && window.qrcode) bQr.addEventListener("click", function () {
    bQr.disabled = true;
    Transferir.gerarLink(new URL("importar.html", location.href).href).then(function (r) {
      var qr = qrcode(0, "L"); qr.addData(r.url); qr.make();
      caixa.innerHTML = qr.createSvgTag({ cellSize: 4, margin: 4, scalable: true, alt: "QR code com o seu progresso" }) +
        "<p>Aponte a câmera do outro aparelho e abra o link." + (r.cortado ? " Para caber no QR code, foram só os simulados mais recentes do histórico." : "") + "</p>" +
        (location.protocol === "http:" && /localhost|127\.0\.0\.1/.test(location.hostname) ? "<p><strong>Atenção:</strong> este endereço é local (localhost) e não abre em outro aparelho. Funciona no site publicado.</p>" : "");
      caixa.hidden = false;
    }).catch(function () {
      status.textContent = "Seu progresso ficou grande demais para um QR code. Use Exportar progresso e mande o arquivo para o outro aparelho.";
    }).then(function () { bQr.disabled = false; });
  });
  bExp.addEventListener("click", function () {
    status.textContent = exportar() ? "Arquivo de progresso gerado." : "Ainda não há progresso salvo para exportar.";
  });
  fImp.addEventListener("change", function () {
    var f = fImp.files[0]; if (!f) return;
    if (!window.confirm("Importar substitui o andamento e o histórico salvos neste aparelho. Continuar?")) { fImp.value = ""; return; }
    var r = new FileReader();
    r.onload = function () {
      try { status.textContent = importar(r.result) + " itens importados. Atualizando…"; setTimeout(function () { location.reload(); }, 1200); }
      catch (e) { status.textContent = "Não foi possível importar: o arquivo não é um backup do Treineiros."; }
    };
    r.readAsText(f);
  });
})();
