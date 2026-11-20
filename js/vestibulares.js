/* Vestibulares: a pergunta "onde você está nos estudos?" reordena os cartões e destaca a prova que faz mais sentido agora.
   A resposta fica guardada neste aparelho (perfil-etapa) para a próxima visita. */
(function () {
  var lista = document.getElementById("vest");
  if (!lista) return;
  var PERFIS = {
    "9ano": { quem: "no 9º ano", ordem: ["ETEC", "Enem", "FATEC"], destaque: "ETEC",
      chips: { ETEC: "A sua próxima prova", Enem: "Mais para frente", FATEC: "Depois do médio" },
      nota: "No 9º ano, o Vestibulinho da ETEC vem primeiro: é a porta para o ensino médio e o médio com técnico." },
    medio: { quem: "no ensino médio", ordem: ["Enem", "FATEC", "ETEC"], destaque: "Enem",
      chips: { Enem: "Faça agora como treino", FATEC: "No 3º ano", ETEC: "Cursos técnicos" },
      nota: "Antes do 3º ano, dá para fazer o Enem como treineiro. A FATEC entra no 3º ano, e a ETEC também tem cursos técnicos." },
    terminei: { quem: "com o ensino médio completo", ordem: ["Enem", "FATEC", "ETEC"], destaque: "Enem",
      chips: { Enem: "Para a faculdade", FATEC: "Faculdade gratuita", ETEC: "Cursos técnicos" },
      nota: "Com o médio completo, o Enem e a FATEC levam à faculdade; a ETEC continua aberta para os cursos técnicos." }
  };
  var quem = document.getElementById("vest-quem"), nota = document.getElementById("vest-nota");
  function aplicar(etapa) {
    var p = PERFIS[etapa] || PERFIS.medio;
    quem.textContent = p.quem; nota.textContent = p.nota;
    p.ordem.forEach(function (b) {
      var li = lista.querySelector('[data-banca="' + b + '"]');
      lista.appendChild(li);
      li.classList.toggle("vest--destaque", b === p.destaque);
      li.querySelector(".vest__chip").textContent = p.chips[b];
    });
  }
  var radios = [].slice.call(document.querySelectorAll('input[name="etapa"]'));
  var salva = window.Armazem ? Armazem.ler("perfil-etapa", "") : "";
  if (PERFIS[salva]) radios.forEach(function (r) { r.checked = r.value === salva; });
  radios.forEach(function (r) {
    r.addEventListener("change", function () {
      if (!r.checked) return;
      if (window.Armazem) Armazem.gravar("perfil-etapa", r.value);
      aplicar(r.value);
      if (window.anunciar) anunciar("Mostrando primeiro as provas para quem está " + PERFIS[r.value].quem);
    });
  });
  var marcado = radios.filter(function (r) { return r.checked; })[0];
  aplicar(marcado ? marcado.value : "medio");
})();
