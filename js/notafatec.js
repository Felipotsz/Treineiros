/* Calculadora da nota final da FATEC (página fatec.html): 80% objetiva + 20% redação, escala 0–100, bônus sobre a nota final. */
(function () {
  var f = document.getElementById("calc-fatec");
  if (!f) return;
  var $ = function (id) { return document.getElementById(id); };
  var num = function (v, max) { v = parseFloat(String(v).replace(",", ".")); return isNaN(v) ? 0 : Math.max(0, Math.min(max, v)); };
  var br = function (x) { return x.toFixed(1).replace(".", ","); };
  function calcular() {
    var tot = parseInt($("cf-tot").value, 10), ac = num($("cf-ac").value, tot), red = num($("cf-red").value, 100), bon = parseInt($("cf-bon").value, 10) / 100;
    $("cf-ac").max = tot;
    var obj = ac / tot * 100, fin = (0.8 * obj + 0.2 * red) * (1 + bon);
    var zero = ac === 0 || red === 0;
    $("cf-res").innerHTML = zero ? "Nota zero na parte objetiva ou na redação desclassifica o candidato."
      : "Parte objetiva: <strong>" + br(obj) + "</strong>. Nota final: <strong>" + br(fin) + "</strong>" + (bon ? " (com " + Math.round(bon * 100) + "% de pontuação acrescida)" : "") + ".";
  }
  f.addEventListener("input", calcular); f.addEventListener("change", calcular);
  f.addEventListener("submit", function (e) { e.preventDefault(); });
  calcular();
})();
