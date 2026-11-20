/* Auditoria do site inteiro, num navegador de verdade (Chromium, via Playwright).
   Para cada página × celular (390 px) e computador (1280 px) × tema claro e noturno, confere:
     - erros de script e de console;
     - rolagem lateral (algo mais largo que a tela);
     - imagens que não carregam e links internos quebrados;
     - acessibilidade automática com axe-core (contraste, rótulos, estrutura), quando instalado;
     - alvos de toque pequenos demais no celular (menos de 24 px).
   Uso, na raiz do projeto, com o servidor local no ar:
     npm install --no-save playwright axe-core
     node tools/auditar.js http://localhost:8000/
   Para simular o GitHub Pages de projeto (usuario.github.io/treineiros/), sirva a pasta de cima
   e passe o endereço com a subpasta: node tools/auditar.js http://localhost:8000/treineiros/ */
const { chromium } = require("playwright");
const fs = require("fs"), path = require("path");
let axeFonte = null;
try { axeFonte = fs.readFileSync(require.resolve("axe-core/axe.min.js"), "utf8"); } catch (e) { console.log("(axe-core não instalado: pulando a checagem automática de acessibilidade)"); }

const BASE = process.argv[2] || "http://localhost:8123/";
const RAIZ = path.join(__dirname, "..");
const primeira = JSON.parse(fs.readFileSync(path.join(RAIZ, "data", "provas.json"), "utf8"))[0];
const PAGINAS = ["index.html", "provas.html", "vestibulares.html", "etec.html", "fatec.html", "enem.html", "apoie.html", "fontes.html",
  "estudo.html", "busca.html", "lista.html", "redacao.html", "importar.html", "404.html"]
  .concat(primeira ? [`simulado.html?id=${primeira.id}`, `questao.html?id=${primeira.id}&n=1`, `q/${primeira.id}/1.html`] : []);
const MODOS = [["celular", { width: 390, height: 844 }, true], ["computador", { width: 1280, height: 860 }, false]];
const TEMAS = ["light", "dark"];

let falhas = 0, avisos = 0;
const falha = (m) => { falhas++; console.log("  FALHA " + m); };
const aviso = (m) => { avisos++; console.log("  aviso " + m); };

(async () => {
  const browser = await chromium.launch(process.env.CHROMIUM ? { executablePath: process.env.CHROMIUM } : {});
  const linksVistos = new Map();                       // endereço → status (cada link é conferido uma vez só)

  for (const [nomeModo, viewport, celular] of MODOS) for (const tema of TEMAS) {
    console.log(`\n== ${nomeModo}, tema ${tema === "dark" ? "noturno" : "claro"} ==`);
    const ctx = await browser.newContext({ viewport, isMobile: celular, hasTouch: celular, colorScheme: tema, serviceWorkers: "block" });
    await ctx.addInitScript(t => { try { localStorage.setItem("treineiros:tema", t); } catch (e) {} }, tema);
    for (const pg of PAGINAS) {
      const p = await ctx.newPage(), erros = [];
      p.on("pageerror", e => erros.push(e.message));
      p.on("console", m => { if (m.type() === "error") erros.push(m.text()); });
      p.on("response", r => { if (r.status() >= 400 && r.url().startsWith(BASE) && !/404\.html$/.test(pg)) erros.push(r.status() + " " + r.url().replace(BASE, "")); });
      await p.goto(BASE + pg, { waitUntil: "networkidle" });
      await p.waitForTimeout(250);
      const r = await p.evaluate(() => ({
        largura: document.documentElement.scrollWidth - innerWidth,
        largos: [...document.querySelectorAll("body *")].filter(e => { const b = e.getBoundingClientRect(); return b.width && b.right > innerWidth + 1 && getComputedStyle(e).position !== "fixed" && !e.closest(".comparar__rola,.tabela-rola,.katex-display,[tabindex]") ; })
          .slice(0, 3).map(e => e.tagName.toLowerCase() + (e.className && typeof e.className === "string" ? "." + e.className.split(" ")[0] : "")),
        imagens: [...document.images].filter(i => i.complete && !i.naturalWidth && !i.closest(".fig--erro")).map(i => i.getAttribute("src")),
        links: [...document.querySelectorAll("a[href]")].map(a => a.href).filter(h => h.startsWith(location.origin)),
        pequenos: [...document.querySelectorAll("a,button,input,select,summary,[role=button]")].filter(e => {
          const b = e.getBoundingClientRect(); if (!b.width || !b.height) return false;
          if (e.closest("p,li,td,dd,.fontes-info,.rodape,.trilha,figcaption,.origem") && e.tagName === "A") return false;   // link no meio do texto: exceção da WCAG 2.5.8
          if (e.tagName === "INPUT" && e.closest("label")) { const l = e.closest("label").getBoundingClientRect(); if (l.height >= 24 && l.width >= 24) return false; }   // a área de toque é o rótulo inteiro
          return b.width < 24 || b.height < 24;
        }).slice(0, 4).map(e => (e.id ? "#" + e.id : e.tagName.toLowerCase()) + " " + (e.textContent || "").trim().slice(0, 20))
      }));
      const rot = pg.padEnd(36);
      if (erros.length) falha(`${rot} erros: ${erros.join(" | ")}`);
      if (r.largura > 0) falha(`${rot} rolagem lateral de ${r.largura}px (${r.largos.join(", ")})`);
      if (r.imagens.length) falha(`${rot} imagens que não carregam: ${r.imagens.join(", ")}`);
      if (celular && r.pequenos.length) aviso(`${rot} alvos de toque pequenos: ${r.pequenos.join("; ")}`);
      for (const h of r.links) {
        const u = h.split("#")[0];
        if (!linksVistos.has(u)) { const resp = await ctx.request.get(u).catch(() => null); linksVistos.set(u, resp ? resp.status() : 0); }
        if (linksVistos.get(u) >= 400 || linksVistos.get(u) === 0) falha(`${rot} link quebrado: ${u.replace(BASE, "")} (${linksVistos.get(u)})`);
      }
      if (axeFonte) {
        await p.addScriptTag({ content: axeFonte });
        const res = await p.evaluate(() => axe.run(document, { runOnly: ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "best-practice"], rules: { "region": { enabled: false } } }));
        for (const v of res.violations) {
          const alvo = v.nodes.slice(0, 2).map(n => n.target.join(" ")).join("; ");
          (["serious", "critical"].includes(v.impact) ? falha : aviso)(`${rot} axe ${v.id} (${v.impact}): ${v.help} → ${alvo}`);
        }
      }
      if (!erros.length && r.largura <= 0 && !r.imagens.length) console.log("  ok    " + pg);
      await p.close();
    }
    await ctx.close();
  }

  // Teclado: o menu do celular abre, recebe o foco e fecha com Esc
  console.log("\n== teclado ==");
  {
    const ctx = await browser.newContext({ viewport: { width: 390, height: 844 }, serviceWorkers: "block" });
    const p = await ctx.newPage(); await p.goto(BASE + "index.html");
    await p.keyboard.press("Tab");
    const pular = await p.evaluate(() => document.activeElement.className);
    pular === "skip" ? console.log("  ok    primeiro Tab cai em 'Pular para o conteúdo'") : falha("primeiro Tab não cai no 'Pular para o conteúdo'");
    await p.click("#btn-menu");
    (await p.locator("#menu-principal").isVisible()) && (await p.evaluate(() => !!document.activeElement.closest("#menu-principal")))
      ? console.log("  ok    menu abre e o foco vai para o primeiro link") : falha("menu do celular não abre ou não recebe o foco");
    await p.keyboard.press("Escape");
    !(await p.locator("#menu-principal").isVisible()) && (await p.evaluate(() => document.activeElement.id)) === "btn-menu"
      ? console.log("  ok    Esc fecha o menu e devolve o foco") : falha("Esc não fecha o menu");
    await ctx.close();
  }

  await browser.close();
  console.log(`\n${falhas} falha(s), ${avisos} aviso(s).`);
  process.exit(falhas ? 1 : 0);
})();
