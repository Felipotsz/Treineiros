/* Minha rotina (Meu estudo, capítulo 2): os dias da semana, o horário, as matérias e quantas questões em cada dia.
   Guardada em "rotina": { dias: { "1": { h: "19:00", m: ["Português"], q: 20 }, ... }, modo: "revisao" | "novas", banca: "" }
   As chaves dos dias seguem Date.getDay() (0 = domingo). Com rotina, a meta do dia passa a ser a do dia da rotina.
   O lembrete vai para o calendário do celular (arquivo .ics com repetição semanal) ou, dia por dia, para o Google Agenda. */
var Rotina = (function () {
  var NOMES = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"];
  var CURTOS = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"];
  var ORDEM = [1, 2, 3, 4, 5, 6, 0];                               // a semana começa na segunda
  var ICS_DIA = ["SU", "MO", "TU", "WE", "TH", "FR", "SA"];
  var Q_MIN = 5, Q_MAX = 60, Q_PASSO = 5;

  function limpa(r) {
    var out = { dias: {}, modo: r && r.modo === "novas" ? "novas" : "revisao", banca: r && ["ETEC", "FATEC", "Enem"].indexOf(r.banca) >= 0 ? r.banca : "" };
    var dias = r && r.dias && typeof r.dias === "object" ? r.dias : {};
    Object.keys(dias).forEach(function (k) {
      var d = dias[k];
      if (!/^[0-6]$/.test(k) || !d || typeof d !== "object") return;
      out.dias[k] = {
        h: /^\d{2}:\d{2}$/.test(d.h) ? d.h : "19:00",
        m: Array.isArray(d.m) ? d.m.filter(function (x) { return typeof x === "string"; }).slice(0, 6) : [],
        q: Math.min(Q_MAX, Math.max(Q_MIN, Math.round((+d.q || 20) / Q_PASSO) * Q_PASSO))
      };
    });
    return out;
  }
  function ler() { return limpa(Armazem.ler("rotina", null)); }
  function gravar(r) { Armazem.gravar("rotina", limpa(r)); }
  function ativa(r) { r = r || ler(); return Object.keys(r.dias).length > 0; }
  function apagar() { Armazem.apagar("rotina"); }
  // o dia de hoje na rotina: null = folga (ou sem rotina)
  function hoje(r) { r = r || ler(); return r.dias[String(new Date().getDay())] || null; }
  // a próxima sessão depois de hoje: { dia, nome }
  function proxima(r) {
    r = r || ler();
    for (var i = 1; i <= 7; i++) { var dw = (new Date().getDay() + i) % 7; if (r.dias[dw]) return { dia: r.dias[dw], nome: NOMES[dw], dw: dw }; }
    return null;
  }
  // meta de questões de hoje: da rotina quando existe (0 na folga); senão, a meta fixa
  function metaHoje() {
    var r = ler();
    if (ativa(r)) { var d = hoje(r); return { q: d ? d.q : 0, daRotina: true, folga: !d }; }
    var m = Armazem.ler("meta", { questoesDia: 10 });
    return { q: m.questoesDia >= 1 ? Math.floor(m.questoesDia) : 10, daRotina: false, folga: false };
  }
  function minutos(d) { return d.q * ((window.Config && Config.minutosPorQuestaoTreino) || 3); }
  function duracao(min) { var h = Math.floor(min / 60), m = min % 60; return h ? h + "h" + (m ? String(m).padStart(2, "0") : "") : m + " min"; }
  function matTxt(m) { return !m.length ? "Matérias variadas" : m.length === 1 ? m[0] : m.slice(0, -1).join(", ") + " e " + m[m.length - 1]; }
  function horaTxt(h) { var p = h.split(":"); return +p[0] + "h" + (p[1] !== "00" ? p[1] : ""); }

  /* ---- Lembretes ---- */
  function pad(n) { return String(n).padStart(2, "0"); }
  function proximaData(dw, h) {                                   // a próxima ocorrência do dia dw, no horário h
    var p = h.split(":"), d = new Date(); d.setHours(+p[0], +p[1], 0, 0);
    var add = (dw - d.getDay() + 7) % 7;                       // hoje entra mesmo se o horário já passou: a semana começa agora
    d.setDate(d.getDate() + add); return d;
  }
  function carimbo(d) { return d.getFullYear() + pad(d.getMonth() + 1) + pad(d.getDate()) + "T" + pad(d.getHours()) + pad(d.getMinutes()) + "00"; }
  function linkTreino() { return new URL("estudo.html?rotina=hoje", location.href).href; }
  function texto(d) { return d.q + " questões de " + matTxt(d.m) + " (" + duracao(minutos(d)) + ")."; }
  function escIcs(s) { return String(s).replace(/\\/g, "\\\\").replace(/[,;]/g, "\\$&").replace(/\n/g, "\\n"); }
  function ics(r) {
    r = r || ler();
    var agora = carimbo(new Date()), linhas = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Treineiros//Rotina//PT", "CALSCALE:GREGORIAN", "METHOD:PUBLISH"];
    Object.keys(r.dias).forEach(function (k) {
      var d = r.dias[k], ini = proximaData(+k, d.h), fim = new Date(ini.getTime() + minutos(d) * 60000);
      linhas.push("BEGIN:VEVENT", "UID:treineiros-rotina-" + k + "-" + agora + "@treineiros", "DTSTAMP:" + agora,
        "DTSTART:" + carimbo(ini), "DTEND:" + carimbo(fim), "RRULE:FREQ=WEEKLY;BYDAY=" + ICS_DIA[+k],
        "SUMMARY:" + escIcs("Estudar: " + matTxt(d.m)), "DESCRIPTION:" + escIcs(texto(d) + "\nComeçar: " + linkTreino()), "URL:" + linkTreino(),
        "BEGIN:VALARM", "ACTION:DISPLAY", "DESCRIPTION:" + escIcs("Hora de estudar: " + matTxt(d.m)), "TRIGGER:PT0M", "END:VALARM", "END:VEVENT");
    });
    linhas.push("END:VCALENDAR");
    return linhas.join("\r\n") + "\r\n";
  }
  function baixarIcs() {
    var url = URL.createObjectURL(new Blob([ics()], { type: "text/calendar;charset=utf-8" })), a = document.createElement("a");
    a.href = url; a.download = "treineiros-rotina.ics"; document.body.appendChild(a); a.click(); a.remove();
    setTimeout(function () { URL.revokeObjectURL(url); }, 2000);
  }
  function linkGoogle(k, d) {
    var ini = proximaData(+k, d.h), fim = new Date(ini.getTime() + minutos(d) * 60000);
    return "https://calendar.google.com/calendar/render?action=TEMPLATE&text=" + encodeURIComponent("Estudar: " + matTxt(d.m)) +
      "&dates=" + carimbo(ini) + "/" + carimbo(fim) + "&recur=" + encodeURIComponent("RRULE:FREQ=WEEKLY;BYDAY=" + ICS_DIA[+k]) +
      "&details=" + encodeURIComponent(texto(d) + "\nComeçar: " + linkTreino());
  }

  return { NOMES: NOMES, CURTOS: CURTOS, ORDEM: ORDEM, Q_MIN: Q_MIN, Q_MAX: Q_MAX, Q_PASSO: Q_PASSO,
    ler: ler, gravar: gravar, ativa: ativa, apagar: apagar, hoje: hoje, proxima: proxima, metaHoje: metaHoje,
    minutos: minutos, duracao: duracao, matTxt: matTxt, horaTxt: horaTxt, ics: ics, baixarIcs: baixarIcs, linkGoogle: linkGoogle };
})();
