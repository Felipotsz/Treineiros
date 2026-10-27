/* Service worker: deixa o site funcionar sem internet.
   - "Casca" do site (páginas, estilos, scripts, fontes, índices leves): guardada na instalação, no cache VERSAO.
   - Provas, figuras e PDFs: pesados para o celular, NÃO são baixados de uma vez. Ficam no cache DADOS
     quando a pessoa abre a prova ou toca em "Guardar para usar sem internet". Esse cache sobrevive às
     atualizações do site (só a casca é trocada).
   Rode "python3 tools/validar.py --indexar" depois de mudar arquivos: ele atualiza a lista abaixo.
   Troque VERSAO para os aparelhos pegarem a versão nova da casca. */
var VERSAO = "treineiros-7ff19b8bcb";
var DADOS = "treineiros-dados";
/* ARQUIVOS:INICIO */
var ARQUIVOS = [
  "./",
  ".gitignore",
  "404.html",
  "apoie.html",
  "assets/fonts/cedarville-cursive-400.woff2",
  "assets/fonts/playfair-display-400-italic.woff2",
  "assets/fonts/playfair-display-700-italic.woff2",
  "assets/fonts/playfair-display-700.woff2",
  "assets/fonts/playfair-display-800.woff2",
  "assets/fonts/source-serif-4-400-italic.woff2",
  "assets/fonts/source-serif-4-400.woff2",
  "assets/fonts/source-serif-4-600.woff2",
  "assets/fonts/source-serif-4-700.woff2",
  "assets/icon-192.png",
  "assets/icon-512.png",
  "assets/icon-maskable-512.png",
  "assets/logo-noturno.svg",
  "assets/logo.svg",
  "assets/og.png",
  "assets/vendor/katex/contrib/auto-render.min.js",
  "assets/vendor/katex/fonts/KaTeX_AMS-Regular.woff2",
  "assets/vendor/katex/fonts/KaTeX_Caligraphic-Bold.woff2",
  "assets/vendor/katex/fonts/KaTeX_Caligraphic-Regular.woff2",
  "assets/vendor/katex/fonts/KaTeX_Fraktur-Bold.woff2",
  "assets/vendor/katex/fonts/KaTeX_Fraktur-Regular.woff2",
  "assets/vendor/katex/fonts/KaTeX_Main-Bold.woff2",
  "assets/vendor/katex/fonts/KaTeX_Main-BoldItalic.woff2",
  "assets/vendor/katex/fonts/KaTeX_Main-Italic.woff2",
  "assets/vendor/katex/fonts/KaTeX_Main-Regular.woff2",
  "assets/vendor/katex/fonts/KaTeX_Math-BoldItalic.woff2",
  "assets/vendor/katex/fonts/KaTeX_Math-Italic.woff2",
  "assets/vendor/katex/fonts/KaTeX_SansSerif-Bold.woff2",
  "assets/vendor/katex/fonts/KaTeX_SansSerif-Italic.woff2",
  "assets/vendor/katex/fonts/KaTeX_SansSerif-Regular.woff2",
  "assets/vendor/katex/fonts/KaTeX_Script-Regular.woff2",
  "assets/vendor/katex/fonts/KaTeX_Size1-Regular.woff2",
  "assets/vendor/katex/fonts/KaTeX_Size2-Regular.woff2",
  "assets/vendor/katex/fonts/KaTeX_Size3-Regular.woff2",
  "assets/vendor/katex/fonts/KaTeX_Size4-Regular.woff2",
  "assets/vendor/katex/fonts/KaTeX_Typewriter-Regular.woff2",
  "assets/vendor/katex/katex.min.css",
  "assets/vendor/katex/katex.min.js",
  "assets/vendor/qrcode.js",
  "busca.html",
  "css/base.css",
  "css/busca.css",
  "css/components.css",
  "css/estudo.css",
  "css/home.css",
  "css/info.css",
  "css/provas.css",
  "css/redacao.css",
  "css/simulado.css",
  "css/variables.css",
  "data/assuntos.json",
  "data/edicoes.json",
  "data/indice-questoes.json",
  "data/provas.json",
  "data/redacao.json",
  "enem.html",
  "estudo.html",
  "etec.html",
  "fatec.html",
  "favicon.svg",
  "fontes.html",
  "importar.html",
  "index.html",
  "js/apoie.js",
  "js/backup.js",
  "js/busca.js",
  "js/config.js",
  "js/dados.js",
  "js/estudo.js",
  "js/formulas.js",
  "js/home.js",
  "js/layout.js",
  "js/lista.js",
  "js/logo.js",
  "js/motor.js",
  "js/provas.js",
  "js/questao.js",
  "js/redacao.js",
  "js/registro.js",
  "js/render.js",
  "js/reportar.js",
  "js/resultado.js",
  "js/revisar.js",
  "js/simulado.js",
  "js/storage.js",
  "js/theme.js",
  "js/transferir.js",
  "js/treino.js",
  "lista.html",
  "manifest.webmanifest",
  "provas.html",
  "questao.html",
  "redacao.html",
  "resultado.html",
  "simulado.html",
  "vestibulares.html"
];
/* ARQUIVOS:FIM */
var PESADO = /\/(data\/provas\/|assets\/img\/|assets\/provas\/)|\/data\/busca\.json$/;

self.addEventListener("install", function (e) {
  e.waitUntil(caches.open(VERSAO).then(function (c) { return c.addAll(ARQUIVOS); }).then(function () { return self.skipWaiting(); }));
});
self.addEventListener("activate", function (e) {
  e.waitUntil(caches.keys().then(function (nomes) {
    return Promise.all(nomes.filter(function (n) { return n !== VERSAO && n !== DADOS; }).map(function (n) { return caches.delete(n); }));
  }).then(function () { return self.clients.claim(); }));
});
/* Rede primeiro (sempre a versão mais nova); sem internet, usa o que está guardado. */
self.addEventListener("fetch", function (e) {
  var req = e.request;
  if (req.method !== "GET") return;
  var url = new URL(req.url);
  if (url.origin !== location.origin) return;          // tudo (fontes, KaTeX, QR) é do próprio site
  var destino = PESADO.test(url.pathname) ? DADOS : VERSAO;
  e.respondWith(
    fetch(req).then(function (res) {
      if (res && res.ok) { var copia = res.clone(); caches.open(destino).then(function (c) { c.put(req, copia); }); }
      return res;
    }).catch(function () {
      return caches.match(req, { ignoreSearch: true }).then(function (r) { return r || (req.mode === "navigate" ? caches.match("index.html") : undefined); });
    })
  );
});
