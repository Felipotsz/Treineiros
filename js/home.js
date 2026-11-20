/* Página inicial: abas dos cadernos (Enem, ETEC, FATEC) com a pilha de cadernos, cartão do Pix,
   próximas provas (Config.proximasProvas) e o lembrete de contagem regressiva e sequência de dias. */
(function () {
  function E(t) { return String(t).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  // ---------- Capítulo 1: os cadernos ----------
  var TEXTOS = {
    enem: { desc: "Todas as edições, de 1998 a 2026. As provas de 63 questões do modelo antigo e as atuais, separadas por área. A redação tem os temas oficiais e temas extras.",
            sobre: ["enem.html", "O que é o Enem"] },
    etec: { desc: "O Vestibulinho das Escolas Técnicas Estaduais de São Paulo: ensino médio, médio com técnico e cursos técnicos.",
            sobre: ["etec.html", "O que é a ETEC"] },
    fatec: { desc: "O Vestibular das Faculdades de Tecnologia do Estado de São Paulo, para os cursos superiores de tecnologia, gratuitos.",
             sobre: ["fatec.html", "O que é a FATEC"] }
  };
  var MOSTRAR = 11;                                   // cartões de edição antes do "ver todas"
  var abas = [].slice.call(document.querySelectorAll(".seletor [role=tab]"));
  var painel = document.getElementById("painel-cadernos");
  var listaEd = document.getElementById("edicoes"), desc = document.getElementById("cadernos-desc");
  var livros = [].slice.call(document.querySelectorAll("#pilha .livro"));
  var provas = null;

  function edicoesDe(banca) {
    if (!provas) return null;
    if (banca === "enem") {                           // Enem: uma entrada por ano, que leva à lista de áreas daquele ano
      var anos = {};
      provas.forEach(function (p) { if (p.banca === "Enem") anos[p.ano] = true; });
      var lista = Object.keys(anos).map(Number).sort(function (a, b) { return b - a; });
      return { total: lista.length, itens: lista.map(function (a) {
        return { href: "provas.html?banca=enem&ano=" + a, ano: a, sub: a >= 2009 ? "2 dias · 4 áreas" : "63 questões" };
      }), rotuloTodas: "Ver as " + lista.length + " edições" };
    }
    var nome = banca === "etec" ? "ETEC" : "FATEC";
    var ps = provas.filter(function (p) { return p.banca === nome; })
      .sort(function (a, b) { return (b.ano - a.ano) || ((b.semestre || 0) - (a.semestre || 0)); });
    return { total: ps.length, itens: ps.map(function (p) {
      return { href: "simulado.html?id=" + encodeURIComponent(p.id), ano: p.ano, sub: p.semestre ? p.semestre + "º semestre" : "" };
    }), rotuloTodas: "Ver as " + ps.length + " provas" };
  }

  function mostrar(banca) {
    abas.forEach(function (a) {
      var sel = a.dataset.banca === banca;
      a.setAttribute("aria-selected", sel); a.tabIndex = sel ? 0 : -1;
      if (sel) painel.setAttribute("aria-labelledby", a.id);
    });
    desc.textContent = TEXTOS[banca].desc;
    var eds = edicoesDe(banca), todas = "provas.html?banca=" + banca;
    listaEd.setAttribute("data-cor", banca);
    listaEd.innerHTML = (eds ? eds.itens.slice(0, MOSTRAR).map(function (e) {
      return '<li><a class="edicao" href="' + e.href + '"><b>' + e.ano + "</b><span>" + E(e.sub) + "</span></a></li>";
    }).join("") : "") +
      '<li><a class="edicao edicao--todas" href="' + todas + '">' + (eds ? eds.rotuloTodas : "Ver as provas") + "</a></li>";
    // pilha: o caderno escolhido vai para a frente (vaga 2), os outros ficam atrás na ordem de sempre
    var ordem = ["fatec", "etec", "enem"].filter(function (b) { return b !== banca; }).concat(banca);
    livros.forEach(function (l) { l.setAttribute("data-vaga", ordem.indexOf(l.dataset.banca)); });
  }

  abas.forEach(function (a, i) {
    a.addEventListener("click", function () { mostrar(a.dataset.banca); });
    a.addEventListener("keydown", function (ev) {           // setas, Home e End, como numa barra de abas
      var n = { ArrowRight: i + 1, ArrowLeft: i - 1, Home: 0, End: abas.length - 1 }[ev.key];
      if (n === undefined) return;
      ev.preventDefault();
      var alvo = abas[(n + abas.length) % abas.length];
      alvo.focus(); mostrar(alvo.dataset.banca);
    });
  });
  if (abas.length) {
    mostrar("enem");
    if (window.Dados) Dados.lista().then(function (l) {
      provas = l;
      var atual = abas.filter(function (a) { return a.getAttribute("aria-selected") === "true"; })[0];
      mostrar(atual ? atual.dataset.banca : "enem");
    }).catch(function () {});
  }

  // ---------- Pix ----------
  var cfg = (window.Config && Config.apoio) || {};
  var chave = (cfg.pixChave || "").trim();
  var cxQr = document.getElementById("home-pix-qr"), cxChave = document.getElementById("home-pix-chave"), bCopiar = document.getElementById("home-pix-copiar");
  if (cxChave) {
    if (!chave) {
      cxChave.textContent = "em breve"; bCopiar.hidden = true;
    } else {
      cxChave.innerHTML = E(chave).replace("@", "@<wbr>");      // quebra a linha depois do @, se precisar
      if (cfg.pixQr) {                                // só troca o aviso pela imagem se ela carregar de verdade
        var img = new Image();
        img.alt = "QR Code do Pix para apoiar o Treineiros" + (cfg.pixNome ? ", em nome de " + cfg.pixNome : "");
        img.onload = function () { cxQr.textContent = ""; cxQr.classList.add("tem-qr"); cxQr.appendChild(img); };
        img.src = cfg.pixQr;
      }
      bCopiar.addEventListener("click", function () {
        function ok() { bCopiar.textContent = "Chave copiada"; if (window.anunciar) anunciar("Chave Pix copiada"); setTimeout(function () { bCopiar.textContent = "Copiar chave Pix"; }, 2500); }
        function manual() {
          var r = document.createRange(); r.selectNodeContents(cxChave);
          var s = getSelection(); s.removeAllRanges(); s.addRange(r);
          if (window.anunciar) anunciar("Chave selecionada. Use copiar do seu aparelho.");
        }
        if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(chave).then(ok, manual); else manual();
      });
    }
  }

  // ---------- Próximas provas ----------
  var agenda = document.getElementById("agenda");
  var ICONE_CAL = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3.5" y="5" width="17" height="15" rx="3"/><path d="M3.5 10h17M8 3v4M16 3v4"/></svg>';
  var MESES = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"];
  var itens = (window.Config && Config.proximasProvas) || [];
  if (agenda) {
    var hoje = new Date(); hoje.setHours(0, 0, 0, 0);
    agenda.innerHTML = itens.filter(function (p) {                  // provas que já passaram saem sozinhas
      return !p.data || new Date(p.data + "T12:00:00") >= hoje;
    }).map(function (p) {
      var dataHtml;
      if (p.data) {
        var d = new Date(p.data + "T12:00:00");
        dataHtml = '<div class="agenda__data"><b>' + d.getDate() + "</b><small>" + MESES[d.getMonth()] + " " + d.getFullYear() + "</small></div>";
      } else {
        dataHtml = '<div class="agenda__data">' + ICONE_CAL + "<em>Em<br>breve</em></div>";
      }
      return "<li>" + dataHtml + '<div class="agenda__txt"><span class="agenda__tag">' + E(p.banca) + "</span><h3>" + E(p.titulo) + "</h3>" +
        "<p>" + E(p.nota || (p.data ? "Data do edital oficial" : "Data em breve")) + "</p>" +
        (p.link ? '<a href="' + E(p.link) + '" rel="noopener">Ver o edital</a>' : "") + "</div></li>";
    }).join("");
    if (!agenda.children.length) agenda.closest("section").hidden = true;
  }

  // ---------- Contagem regressiva e sequência de dias, se o aluno já definiu ----------
  var el = document.getElementById("status-home");
  if (!el || !window.Registro) return;
  var alvo = Armazem.ler("alvo", null), seq = Registro.sequencia(), partes = [];
  if (alvo && alvo.data) {
    var dd = Registro.diasAte(alvo.data);
    if (dd > 0) partes.push("Faltam " + dd + (dd === 1 ? " dia" : " dias") + " para " + alvo.nome + ".");
    else if (dd === 0) partes.push("A prova de " + alvo.nome + " é hoje. Boa sorte!");
  }
  if (seq > 0) partes.push("Você estudou " + seq + (seq === 1 ? " dia seguido." : " dias seguidos."));
  el.textContent = partes.join(" ");
})();
