/* Testes de fluxo num navegador de verdade (Chromium, via Playwright).
   Uso, na raiz do projeto:
     npm install --no-save playwright && npx playwright install chromium   (uma vez)
     python3 -m http.server 8000 &                                        (servidor local)
     node tools/testar_navegador.js http://localhost:8000/
   Variável opcional CHROMIUM=/caminho/do/chrome para usar um navegador já instalado.
   Também roda sozinho no GitHub (.github/workflows/validar.yml). */
const { chromium } = require("playwright");
const fs = require("fs"), path = require("path");
// Os testes usam provas de exemplo próprias (tools/testes/), servidas no lugar dos dados reais:
// assim continuam valendo quando as provas de verdade entrarem e os exemplos saírem do site.
const FIX = path.join(__dirname, "testes");
async function usarExemplos(alvo) {
  await alvo.route(/\/data\/indice-questoes\.json$/, r => r.fulfill({ path: path.join(FIX, "indice-questoes.json"), contentType: "application/json" }));
  await alvo.route(/\/data\/busca\/[a-z0-9-]+\.json$/, r => {
    const arq = path.join(FIX, "busca", /[a-z0-9-]+\.json$/.exec(r.request().url())[0]);
    return fs.existsSync(arq) ? r.fulfill({ path: arq, contentType: "application/json" }) : r.fulfill({ status: 404, body: "" });
  });
  await alvo.route(/\/data\/provas\.json$/, r => r.fulfill({ path: path.join(FIX, "provas.json"), contentType: "application/json" }));
  await alvo.route(/\/data\/provas\/(exemplo-[a-z]+)\.json$/, r => {
    const nome = /exemplo-[a-z]+\.json/.exec(r.request().url())[0];
    return r.fulfill({ path: path.join(FIX, nome), contentType: "application/json" });
  });
}
const BASE = process.argv[2] || "http://localhost:8123/";
let falhas = 0;
const ok = (cond, nome) => { console.log((cond ? "  ok   " : "  FALHA ") + nome); if (!cond) falhas++; };

async function novaPagina(browser, opts = {}) {
  const ctx = await browser.newContext(Object.assign({ serviceWorkers: "block" }, opts.celular ? { viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true } : {}));
  if (opts.bloquear) await ctx.addInitScript(() => {
    for (const k of ["localStorage", "sessionStorage"])
      Object.defineProperty(window, k, { get() { throw new DOMException("bloqueado", "SecurityError"); } });
  });
  if (!opts.reais) await usarExemplos(ctx);          // reais: usa os dados de verdade do site (provas publicadas)
  const page = await ctx.newPage();
  page.erros = [];
  page.on("pageerror", e => page.erros.push(e.message));
  page.on("console", m => { if (m.type() === "error" && !/fonts\.g|ERR_NAME|ERR_INTERNET|net::|404 \(File not found\)/.test(m.text())) page.erros.push(m.text()); });
  if (opts.rotas) for (const [pad, fn] of opts.rotas) await page.route(pad, fn);
  return page;
}
const texto = p => p.locator("main").innerText();
// espera (até 5 s) o texto aparecer na página: evita falha falsa quando a página ainda está carregando dados
const contem = (p, ...trechos) => p.waitForFunction(t => t.every(x => (document.querySelector("main") || document.body).innerText.includes(x)), trechos, { timeout: 5000 }).then(() => true, () => false);

(async () => {
  const browser = await chromium.launch(process.env.CHROMIUM ? { executablePath: process.env.CHROMIUM } : {});

  console.log("1. Todas as páginas abrem sem erro de script");
  for (const pg of ["index.html", "provas.html", "estudo.html", "fontes.html", "vestibulares.html", "etec.html", "fatec.html", "enem.html", "apoie.html", "simulado.html?id=exemplo-enem", "resultado.html?id=exemplo-enem", "404.html",
                    "busca.html", "lista.html", "questao.html?id=exemplo-enem&n=1", "redacao.html", "importar.html", "revisar.html"]) {
    const p = await novaPagina(browser); await p.goto(BASE + pg); await p.waitForTimeout(400);
    ok(!p.erros.length, pg + (p.erros.length ? " → " + p.erros.join(" | ") : "")); await p.context().close();
  }

  console.log("2. Fluxo completo: responder, pausar, recarregar na pausa, finalizar");
  {
    const p = await novaPagina(browser);
    await p.goto(BASE + "simulado.html?id=exemplo-enem");
    await p.getByRole("button",{name:"Começar a prova"}).click();
    await p.click('[data-letra="B"]');
    ok(await p.locator(".alt.is-correta").count() === 1 && await p.locator("#expl").isVisible(), "modo estudo mostra correção");
    await p.click("#b-prox");
    await p.click("#b-pausar");
    ok((await texto(p)).includes("Simulado pausado"), "pausa");
    await p.reload(); await p.waitForSelector("#b-cont");
    ok(/questão 2 de 3/i.test(await texto(p)), "recarregar na pausa → tela de retomar na questão 2");
    await p.click("#b-cont");
    ok((await p.locator("#qt").getAttribute("aria-label")) === "Questão 2 de 3", "continua na questão 2");
    ok((await texto(p)).includes("1 de 3 respondidas"), "progresso preservado");
    await p.keyboard.press("c");
    await p.click("#b-fim");
    await p.getByRole("button",{name:"Finalizar mesmo assim"}).click();
    await p.waitForURL(/resultado/);
    await p.waitForSelector(".placar");
    ok((await p.locator(".placar__n").innerText()).startsWith("2"), "resultado: 2 acertos (Q1 pelo clique, Q2 pelo atalho C)");
    const h = await p.evaluate(() => JSON.parse(localStorage.getItem("treineiros:historico")));
    ok(h.length === 1, "histórico com 1 entrada");
    ok(!p.erros.length, "sem erros de script " + p.erros.join(" | "));
    await p.context().close();
  }

  console.log("3. Tempo esgotado e aparelho em repouso (relógio simulado)");
  {
    const p = await novaPagina(browser);
    await p.clock.install();
    await p.goto(BASE + "simulado.html?id=exemplo-etec");
    await p.check('input[value="personalizado"]'); await p.fill("#min", "1");
    await p.getByRole("button",{name:"Começar a prova"}).click();
    await p.clock.fastForward(400 * 1000);  // aparelho "dormiu" 400 s
    await p.clock.runFor(1500);
    ok((await texto(p)).includes("Simulado pausado"), "salto de 400 s vira pausa, não encerra a prova");
    ok((await p.locator("#aviso").innerText()).includes("inativo"), "avisa o motivo da pausa");
    await p.click("#b-ret");
    for (let i = 0; i < 62; i++) await p.clock.runFor(1000);
    await p.waitForURL(/resultado/, { timeout: 5000 });
    await p.waitForSelector(".placar");
    ok((await texto(p)).includes("O tempo acabou"), "tempo esgotado encerra e avisa no resultado");
    const h = await p.evaluate(() => JSON.parse(localStorage.getItem("treineiros:historico")));
    ok(h.length === 1 && h[0].porTempo, "uma única entrada no histórico, marcada porTempo");
    await p.context().close();
  }

  console.log("4. localStorage e sessionStorage bloqueados");
  {
    const p = await novaPagina(browser, { bloquear: true });
    await p.goto(BASE + "simulado.html?id=exemplo-etec"); await p.waitForSelector("#cfg-resumo b");
    ok(await p.locator(".aviso-armazem").isVisible(), "aviso de armazenamento bloqueado aparece");
    await p.getByRole("button",{name:"Começar a prova"}).click();
    await p.click('[data-letra="B"]'); await p.click("#b-prox"); await p.click('[data-letra="A"]');
    await p.click("#b-fim"); await p.locator("dialog").getByRole("button",{name:"Finalizar",exact:true}).click();
    await p.waitForURL(/resultado/); await p.waitForSelector(".placar", { timeout: 4000 }).catch(() => {});
    ok((await texto(p)).includes("50% de acertos"), "resultado aparece mesmo sem armazenamento");
    await p.goto(BASE + "estudo.html"); await p.waitForTimeout(500);
    ok(/1\s+simulado/.test(await texto(p)), "Meu estudo vê o simulado na mesma aba");
    ok(!p.erros.length, "sem erros de script " + p.erros.join(" | "));
    await p.context().close();
  }

  console.log("5. Dados de versões antigas e backup corrompido");
  {
    const p = await novaPagina(browser);
    await p.goto(BASE + "index.html");
    await p.evaluate(() => {
      localStorage.setItem("treineiros:andamento:exemplo-enem", JSON.stringify({ respostas: { 1: "B", 99: "A" }, atual: 10, tempoRestanteSeg: 500 }));
      localStorage.setItem("treineiros:historico", JSON.stringify("lixo"));
      localStorage.setItem("treineiros:meta", JSON.stringify({ questoesDia: 0 }));
      localStorage.setItem("treineiros:alvo", JSON.stringify({ nome: "ETEC", data: "ontem" }));
      localStorage.setItem("treineiros:erros", JSON.stringify({ "a#1": null, "exemplo-enem#2": { provaId: "exemplo-enem", numero: 2, status: "aberta" } }));
      localStorage.setItem("treineiros:atividade", "{quebrado");
    });
    await p.goto(BASE + "simulado.html?id=exemplo-enem"); await p.waitForSelector("#b-cont");
    ok(/questão 1 de 3/i.test(await texto(p)), "andamento v1 com atual fora do limite → questão 1");
    await p.click("#b-cont");
    ok((await texto(p)).includes("1 de 3 respondidas"), "resposta de questão inexistente ignorada");
    await p.click("#b-fim"); await p.getByRole("button",{name:"Finalizar mesmo assim"}).click();
    await p.waitForURL(/resultado/); await p.waitForSelector(".placar");
    ok(true, "finaliza mesmo com histórico corrompido");
    await p.goto(BASE + "estudo.html"); await p.waitForTimeout(600);
    const t = await texto(p);
    ok(t.includes("de 10 questões") && t.includes("data salva não é válida"), "meta 0 e data inválida tratadas");
    ok(!t.includes("undefined") && !t.includes("NaN"), "sem 'undefined'/'NaN' na tela");
    ok(!p.erros.length, "sem erros de script " + p.erros.join(" | "));
    await p.context().close();
  }

  console.log("6. Endereços e casos vazios");
  {
    const p = await novaPagina(browser);
    await p.goto(BASE + "simulado.html?id=nao-existe"); await p.waitForTimeout(400);
    ok((await texto(p)).includes("Não encontramos esta prova"), "id inexistente");
    await p.goto(BASE + "simulado.html?id=exemplo-etec&modo=erradas"); await p.waitForTimeout(400);
    ok((await texto(p)).includes("finalize antes o simulado completo"), "erradas sem resultado anterior");
    await p.goto(BASE + "simulado.html?id=treino"); await p.waitForTimeout(400);
    ok((await texto(p)).includes("Monte um novo em Meu estudo"), "treino inexistente");
    await p.goto(BASE + "resultado.html?id=nao-existe"); await p.waitForTimeout(400);
    ok((await texto(p)).includes("Nenhum resultado"), "resultado inexistente");
    await p.goto(BASE + "simulado.html"); await p.waitForTimeout(300);
    ok((await texto(p)).includes("Nenhuma prova escolhida"), "sem id");
    await p.goto(BASE + "estudo.html"); await p.waitForTimeout(600);
    await p.uncheck('[name=mat]:checked'); await p.getByRole("button",{name:"Montar treino"}).click();
    ok((await p.locator("#status").innerText()).includes("ao menos uma matéria"), "treino sem matéria");
    await p.check('[name=mat][value="Matemática"]'); await p.getByRole("button",{name:"Montar treino"}).click();
    await p.waitForURL(/id=treino/); await p.waitForTimeout(300);
    ok((await texto(p)).includes("Tempo sugerido"), "treino por matéria abre");
    ok(!p.erros.length, "sem erros de script " + p.erros.join(" | "));
    await p.context().close();
  }

  console.log("7. Questão anulada e figura que não carrega");
  {
    const p = await novaPagina(browser, { rotas: [["**/data/provas/exemplo-etec.json", async r => {
      const d = JSON.parse(fs.readFileSync(path.join(FIX, "exemplo-etec.json"), "utf8"));
      d.questoes[0].gabarito = "ANULADA"; d.questoes[1].imagens = ["assets/img/nao-existe.png"];
      await r.fulfill({ json: d });
    }]] });
    await p.goto(BASE + "simulado.html?id=exemplo-etec"); await p.getByRole("button",{name:"Começar a prova"}).click();
    await p.click('[data-letra="A"]');
    ok((await texto(p)).includes("anulada pela banca") && await p.locator(".alt.is-selecionada").count() === 1, "anulada: explica e mostra a escolha");
    await p.click("#b-prox"); await p.waitForTimeout(400);
    ok((await texto(p)).includes("Não foi possível carregar uma figura"), "figura quebrada vira aviso");
    await p.click('[data-letra="A"]');
    await p.click("#b-fim"); await p.locator("dialog").getByRole("button",{name:"Finalizar",exact:true}).click();
    await p.waitForURL(/resultado/); await p.waitForSelector(".placar");
    ok((await p.locator(".placar__n").innerText()).startsWith("1"), "anulada vale ponto");
    ok(await p.locator(".revisao img.figura").count() === 1, "revisão do resultado inclui a figura");
    await p.context().close();
  }

  console.log("8. Refazer erradas depois de um novo resultado completo");
  {
    const p = await novaPagina(browser);
    await p.goto(BASE + "simulado.html?id=exemplo-enem"); await p.getByRole("button",{name:"Começar a prova"}).click();
    await p.click('[data-letra="A"]'); await p.click("#b-fim"); await p.getByRole("button",{name:"Finalizar mesmo assim"}).click();
    await p.waitForURL(/resultado/); await p.getByRole("link",{name:/^Refazer (as \d+|a) que não acertei/}).click();
    await p.getByRole("button",{name:"Começar a prova"}).click();
    ok((await p.locator("#qt").getAttribute("aria-label")) === "Questão 1 de 3", "erradas: 3 questões");
    await p.click('[data-letra="B"]');                          // deixa um andamento de "erradas"
    await p.goto(BASE + "simulado.html?id=exemplo-enem"); await p.getByRole("button",{name:"Começar a prova"}).click();
    await p.click('[data-letra="B"]'); await p.click("#b-fim"); await p.getByRole("button",{name:"Finalizar mesmo assim"}).click();
    await p.waitForURL(/resultado/); await p.getByRole("link",{name:/^Refazer (as \d+|a) que não acertei/}).click();
    await p.waitForTimeout(300);
    ok(!(await texto(p)).includes("em andamento"), "andamento antigo de 'erradas' foi descartado");
    ok((await texto(p)).includes("2 questões"), "erradas novas: 2 questões");
    await p.context().close();
  }


  console.log("9. Logo, fórmulas locais e página estática de questão");
  {
    const p = await novaPagina(browser);
    await p.goto(BASE + "index.html");
    ok(await p.locator(".cab .marca__img:visible").count() === 1 && await p.locator(".rodape .marca__img:visible").count() === 1, "marca no cabeçalho e no rodapé");
    ok(await p.evaluate(() => [...document.querySelectorAll(".marca__img")].every(i => i.complete && i.naturalWidth > 0)), "imagens da logo carregam");
    // páginas em q/ são geradas dos dados reais: usa a primeira que existir
    const prim = JSON.parse(fs.readFileSync(path.join(__dirname, "..", "data", "provas.json"), "utf8"))[0];
    await p.goto(BASE + "q/" + prim.id + "/1.html"); await p.evaluate(() => { const e = document.querySelector(".enunciado"); if (e) { e.insertAdjacentHTML("beforeend", "<p>\\(x^2\\)</p>"); Formulas.renderizar(e); } });
    await p.waitForSelector(".katex", { timeout: 5000 }).catch(() => {});
    ok(await p.locator(".katex").count() > 0, "KaTeX local renderiza a fórmula (sem CDN)");
    ok(await p.locator(".cab .marca").getAttribute("href") === "index.html" && await p.evaluate(() => new URL(document.querySelector(".cab .marca").href).pathname === location.pathname.replace(/q\/.*$/, "index.html")), "links do menu funcionam dentro de q/");
    ok(!(await p.evaluate(() => document.documentElement.scrollWidth > innerWidth)), "sem rolagem lateral");
    await p.context().close();
  }

  console.log("10. Treino por assunto e estatísticas por assunto");
  {
    const p = await novaPagina(browser);
    await p.goto(BASE + "estudo.html"); await p.waitForTimeout(500);
    await p.uncheck("[name=mat]:checked"); await p.check('[name=mat][value="Matemática"]');
    ok(await p.locator("[name=assunto]").count() === 2, "assuntos da matéria aparecem");
    await p.check('[name=assunto][value="Matemática · Porcentagem"]');
    await p.getByRole("button", { name: "Montar treino" }).click(); await p.waitForURL(/id=treino/);
    await p.getByRole("button", { name: "Começar a prova" }).click();
    ok((await p.locator("#qt").getAttribute("aria-label")) === "Questão 1 de 1" && (await texto(p)).includes("Porcentagem"), "treino só com o assunto escolhido");
    await p.click('[data-letra="C"]'); await p.click("#b-fim"); await p.locator("dialog").getByRole("button", { name: "Finalizar", exact: true }).click();
    await p.waitForURL(/resultado/); await p.goto(BASE + "estudo.html"); await p.waitForTimeout(500);
    ok((await p.locator("#stats").innerText()).includes("Porcentagem"), "tabela por assunto no Meu estudo");
    await p.context().close();
  }

  console.log("11. Cartão-resposta e pontuação ETEC");
  {
    const p = await novaPagina(browser);
    await p.goto(BASE + "simulado.html?id=exemplo-etec"); await p.check("[value=cartao]");
    ok(await p.locator("[name=correcao][value=imediata]").isDisabled(), "cartão desativa o modo estudo");
    await p.getByRole("button", { name: "Começar a prova" }).click();
    await p.locator('.cartao input[name=q1][value=B]').check({ force: true }); await p.locator('.cartao input[name=q2][value=C]').check({ force: true });
    ok((await texto(p)).includes("2 de 2 respondidas"), "bolinhas contam no progresso");
    await p.reload(); await p.waitForSelector("#b-cont"); await p.click("#b-cont");
    ok(await p.locator('.cartao input[name=q1][value=B]').isChecked(), "cartão volta marcado depois de recarregar");
    await p.click("#b-fim"); await p.locator("dialog").getByRole("button", { name: "Finalizar", exact: true }).click();
    await p.waitForURL(/resultado/); await p.waitForSelector(".placar");
    ok((await texto(p)).includes("Pontuação: 2 pontos"), "pontuação no formato ETEC");
    await p.check('[data-acr="escola-publica"]'); await p.check('[data-acr="afrodescendente"]');
    ok((await p.locator("#of-total").innerText()).includes("2,26"), "pontuação acrescida de 13%");
    await p.context().close();
  }

  console.log("12. Estimativa TRI e % de acerto do Inep (dados injetados)");
  {
    const p = await novaPagina(browser, { rotas: [["**/data/provas/exemplo-enem.json", async r => {
      const d = JSON.parse(fs.readFileSync(path.join(FIX, "exemplo-enem.json"), "utf8"));
      d.questoes.forEach((q, i) => { q.tri = { a: 2, b: 0.5 + i * 0.3, c: 0.2 }; q.estatistica = { pctAcerto: 40 + i }; });
      await r.fulfill({ json: d });
    }]] });
    await p.goto(BASE + "simulado.html?id=exemplo-enem"); await p.getByRole("button", { name: "Começar a prova" }).click();
    await p.click('[data-letra="B"]');
    ok((await texto(p)).includes("40% dos candidatos acertaram"), "% de acerto do Inep na explicação");
    await p.click("#b-fim"); await p.getByRole("button", { name: "Finalizar mesmo assim" }).click();
    await p.waitForURL(/resultado/); await p.waitForSelector(".placar");
    const t = await texto(p);
    ok(t.includes("Nota estimada (TRI)") && /Linguagens\s+1 de 1\s+\d{3}/.test(t), "nota TRI estimada por área");
    await p.context().close();
  }

  console.log("13. Busca, lista compartilhada e questão avulsa");
  {
    const p = await novaPagina(browser);
    const pedidos = []; p.on("request", r => { if (/\/data\/busca\//.test(r.url())) pedidos.push(r.url().split("/").pop()); });
    await p.goto(BASE + "busca.html"); await p.waitForSelector("#mapa-mats .mapa-mat");
    ok(pedidos.length === 0, "mapa abre sem baixar trechos nem palavras");
    await p.locator("#mapa-mats [data-a]").first().click(); await p.waitForSelector("#b-lista .res");
    ok(pedidos.length > 0 && pedidos.every(n => n.endsWith("-t.json")), "ao escolher um assunto, baixa só os trechos da matéria");
    ok(!(await p.locator("#b-lista .res__trecho").first().innerText()).includes("Abra a questão"), "linhas mostram o trecho da questão");
    await p.click("#b-voltar");
    await p.fill("#b-texto", "fotossintese"); await p.waitForTimeout(500);
    ok((await p.locator("#b-contagem").innerText()).startsWith("1 "), "busca sem acento encontra 'fotossíntese'");
    ok(await p.locator("#cesta").isHidden(), "cesta escondida enquanto vazia");
    await p.check("input[data-k]"); await p.fill("#b-texto", "plural"); await p.waitForTimeout(500); await p.check("input[data-k]");
    await p.fill("#c-nome", "Lista da turma");
    const url = await p.evaluate(() => Treino.endereco("lista.html?l=" + encodeURIComponent(Treino.codificarLista(JSON.parse(localStorage.getItem("treineiros:lista-montando")))) + "&t=Lista%20da%20turma"));
    await p.goto(url);
    ok(await contem(p, "Lista da turma", "2 questões"), "link da lista abre com 2 questões");
    await p.getByRole("button", { name: "Começar o treino" }).click(); await p.waitForURL(/id=treino/);
    ok((await texto(p)).includes("2 questões"), "lista vira treino");
    await p.goto(BASE + "simulado.html?id=exemplo-etec"); await p.waitForSelector("#cfg-resumo b");
    ok(/questões em .*correção na hora/.test(await texto(p)), "abertura: resumo da prova ao lado do botão");
    await p.goto(BASE + "questao.html?id=exemplo-enem&n=2"); await p.click('[data-letra="C"]');
    ok(await contem(p, "Você acertou"), "questão avulsa corrige");
    await p.goto(BASE + "questao.html?id=exemplo-enem&n=99");
    ok(await contem(p, "não tem a questão 99"), "questão avulsa inexistente");
    await p.context().close();
  }

  console.log("14. QR code de progresso e página de receber");
  {
    const p = await novaPagina(browser);
    await p.goto(BASE + "index.html");
    await p.evaluate(() => { localStorage.setItem("treineiros:historico", JSON.stringify([{ provaId: "x", titulo: "X", data: "2026-01-01T00:00:00Z", acertos: 3, total: 5, percentual: 60, porMateria: {} }])); localStorage.setItem("treineiros:meta", '{"questoesDia":25}'); });
    await p.goto(BASE + "provas.html"); await p.click("#b-qr"); await p.waitForSelector("#qr svg");
    ok(true, "QR code gerado");
    const link = await p.evaluate(() => Transferir.gerarLink(new URL("importar.html", location.href).href).then(r => r.url));
    const q = await novaPagina(browser); await q.goto(link);
    ok(/simulados? no histórico/.test(await texto(q)) && (await texto(q)).includes("Troca"), "página de receber lê o link");
    ok(await q.locator("#b-copia").count() === 1, "receber: oferece guardar uma cópia antes");
    await q.getByRole("button", { name: "Receber o progresso" }).click(); await q.waitForURL(/estudo/);
    ok((await q.evaluate(() => JSON.parse(localStorage.getItem("treineiros:meta")).questoesDia)) === 25, "progresso chegou no outro aparelho");
    await q.context().close(); await p.context().close();
  }

  console.log("14b. Minha rotina");
  {
    const p = await novaPagina(browser);
    await p.goto(BASE + "estudo.html"); await p.waitForSelector("#rotina .rot-grade");
    const dw = await p.evaluate(() => new Date().getDay());
    await p.check(`[data-liga="${dw}"]`); await p.waitForSelector(`[data-poe="${dw}"]`);
    await p.selectOption(`[data-poe="${dw}"]`, "Matemática"); await p.waitForSelector(`[data-tira="${dw}"]`);
    await p.click(`[data-q="${dw}"][data-d="1"]`);
    const r = await p.evaluate(() => JSON.parse(localStorage.getItem("treineiros:rotina")));
    ok(r.dias[dw] && r.dias[dw].q === 25 && r.dias[dw].m[0] === "Matemática", "rotina guarda dia, matéria e questões");
    ok((await p.locator("#painel").innerText()).includes("de 25 questões"), "meta de hoje segue a rotina");
    ok(await p.locator("#faixa-hoje").isVisible() && (await p.locator("#faixa-hoje").innerText()).includes("Matemática"), "faixa mostra o treino de hoje");
    const ics = await p.evaluate(() => Rotina.ics());
    ok(/RRULE:FREQ=WEEKLY;BYDAY=[A-Z]{2}/.test(ics) && ics.includes("BEGIN:VALARM"), "lembrete do calendário com repetição semanal");
    await p.click("#b-rot-hoje"); await p.waitForURL(/id=treino/);
    ok(/questões?/.test(await texto(p)), "treino de hoje abre");
    await p.goto(BASE + "estudo.html"); await p.waitForSelector("#b-rot-apagar"); await p.click("#b-rot-apagar");
    ok(await p.locator("#f-meta").count() === 1, "apagar a rotina volta à meta fixa");
    await p.context().close();
  }

  console.log("15. Redação");
  {
    const p = await novaPagina(browser);
    await p.goto(BASE + "redacao.html");
    await p.check('input[name="modelo"][value="Enem"]');                    // modelo Enem: 5 competências
    ok(await p.locator(".tema-op:not([hidden])").count() > 0 && await p.locator('.tema-op:not([hidden])[data-banca="FATEC"]').count() === 0, "Enem: só temas do Enem na lista");
    await p.getByRole("button", { name: "Começar a escrever" }).click();
    await p.fill("#texto", "Texto curto.");
    ok((await p.locator("#cont").innerText()).includes("curto demais"), "avisa texto curto");
    await p.reload(); await p.waitForSelector("#f-red"); ok((await texto(p)).includes("Continuar"), "redação em andamento sobrevive ao recarregar");
    await p.click("#b-cont"); ok((await p.locator("#texto").inputValue()) === "Texto curto.", "texto preservado");
    await p.getByRole("button", { name: "Terminei" }).click(); await p.getByRole("button", { name: "Guardar redação" }).click();
    ok((await texto(p)).includes("600"), "autoavaliação soma 600 (5 × 120)");
    await p.context().close();
  }

  console.log("16. Revisão do autor");
  {
    const p = await novaPagina(browser);
    await p.goto(BASE + "revisar.html"); await p.waitForTimeout(500);
    ok((await p.locator("#r-resumo").innerText()).startsWith("2 "), "2 questões pendentes nos exemplos");
    await p.locator("#r-lista details").first().evaluate(d => { d.open = true; });
    await p.locator("#r-lista [data-campo=revisada]").first().check();
    ok((await p.locator("#r-baixar").innerText()).includes("(1)"), "marcação contada para baixar");
    await p.context().close();
  }

  console.log("17. Página de provas (dados reais): edições, semestres sem prova e em breve");
  {
    const p = await novaPagina(browser, { reais: true, celular: true });
    await p.goto(BASE + "provas.html"); await p.waitForSelector(".ed");
    const t = await texto(p);
    ok(t.includes("Em 2021 não houve prova da ETEC nem da FATEC em nenhum semestre"), "2021 explicado uma vez, no topo do ano");
    ok(await p.locator(".ed--sem-prova").count() === 8, "8 semestres sem prova (2020/2, 2021/1, 2021/2, 2022/1 × ETEC e FATEC)");
    ok((await p.locator(".ed--em-breve", { hasText: "Em breve" }).count()) >= 2, "ETEC 2025/2 e FATEC 2025/1 aparecem como em breve");
    await p.locator(".chip", { hasText: "FATEC" }).click();
    ok((await p.locator(".ed .ed__banca", { hasText: "ETEC" }).count()) === 0 && (await p.locator(".ed .ed__banca", { hasText: "FATEC" }).count()) > 0, "filtro FATEC esconde ETEC");
    await p.locator(".chip", { hasText: "Todas" }).click(); await p.check("#f-nao");
    ok(await p.locator(".ed--sem-prova").count() === 0 && await p.locator(".ed--ok").count() > 0, "'Só as que ainda não fiz' esconde os semestres sem prova");
    ok(await p.locator("#indice a").count() > 5, "índice de anos ao lado da lista");
    ok(!(await p.evaluate(() => document.documentElement.scrollWidth > innerWidth)), "sem rolagem lateral no celular");
    await p.context().close();
  }

  console.log("18. Provas reais no celular: todas as questões, figuras, fórmulas, navegação");
  {
    const lista = JSON.parse(fs.readFileSync(path.join(__dirname, "..", "data", "provas.json"), "utf8"));
    // SO=id1,id2 testa só essas provas nesta etapa (útil ao publicar uma prova nova)
    for (const meta of lista.filter(m => !process.env.SO || process.env.SO.split(",").includes(m.id))) {
      const p = await novaPagina(browser, { reais: true, celular: true });
      await p.goto(BASE + "simulado.html?id=" + meta.id);
      await p.getByRole("button", { name: "Começar a prova" }).click();
      let lateral = [], semFigura = [], semFormula = [];
      for (let i = 0; i < meta.totalQuestoes; i++) {
        if (i) { await p.click("#b-prox"); }
        await p.waitForFunction(n => document.querySelector("#qt") && document.querySelector("#qt").getAttribute("aria-label").startsWith("Questão " + n + " "), i + 1);
        await p.waitForTimeout(120);
        const r = await p.evaluate(async () => {
          const imgs = [...document.querySelectorAll(".questao img.figura")];
          await Promise.all(imgs.map(im => im.complete ? 0 : new Promise(ok => { im.onload = im.onerror = ok; })));
          return { lateral: document.documentElement.scrollWidth > innerWidth + 1,
                   quebradas: imgs.filter(im => !im.naturalWidth).length,
                   formulaCrua: /\\\(|\\\[/.test(document.querySelector(".questao").innerText) };
        });
        if (r.lateral) lateral.push(i + 1); if (r.quebradas) semFigura.push(i + 1);
        if (r.formulaCrua) { await p.waitForTimeout(800); if (/\\\(|\\\[/.test(await p.locator(".questao").innerText())) semFormula.push(i + 1); }
      }
      ok(!lateral.length, `${meta.id}: nenhuma questão com rolagem lateral ${lateral.join(",")}`);
      ok(!semFigura.length, `${meta.id}: todas as figuras carregam ${semFigura.join(",")}`);
      ok(!semFormula.length, `${meta.id}: todas as fórmulas renderizadas ${semFormula.join(",")}`);
      ok(await p.locator(".nav--principal").evaluate(e => getComputedStyle(e).position) === "fixed", `${meta.id}: navegação presa embaixo no celular`);
      await p.click("#b-mapa"); await p.locator("dialog .mapa button").first().click();
      ok((await p.locator("#qt").getAttribute("aria-label")).startsWith("Questão 1 "), `${meta.id}: mapa em janela leva à questão`);
      const fig = p.locator(".figura-btn").first();
      if (await fig.count()) { await fig.click(); ok(await p.locator("dialog.dlg-zoom img").isVisible(), `${meta.id}: figura amplia em tela cheia`); await p.click("#b-fechar"); }
      ok(!p.erros.length, `${meta.id}: sem erros de script ${p.erros.join(" | ")}`);
      await p.context().close();
    }
  }

  console.log("19. Simulado misto, revisão rápida, redação da FATEC, nota da FATEC e painel de revisão");
  {
    const p = await novaPagina(browser, { reais: true, celular: true });
    await p.goto(BASE + "estudo.html");
    await p.waitForSelector("#m-info:not(:empty)");
    ok(/50 questões em 4h/.test(await p.locator("#m-info").innerText()), "misto ETEC: 50 questões em 4 h");
    await p.check('[name=m-tipo][value=FATEC]'); await p.check('[name=m-tam][value="0.5"]');
    const info = await p.locator("#m-info").innerText();
    const n = parseInt(info, 10), soma = [...info.matchAll(/ (\d+)(?=[,.])/g)].map(m => +m[1]).filter(x => x < 20).reduce((a, b) => a + b, 0);
    ok(n > 0 && soma === n, `misto FATEC: soma por matéria (${soma}) = total (${n})`);
    await p.click("#f-misto button[type=submit]"); await p.waitForURL(/simulado\.html\?id=treino/);
    await p.waitForSelector("#cfg");
    ok((await texto(p)).includes(`${n} questões`) && (await texto(p)).includes("Proporcional à prova da FATEC"), "simulado misto abre com o tempo proporcional");
    // mescla: metade de cada prova, sem nota
    await p.goto(BASE + "estudo.html"); await p.waitForSelector("#f-misto");
    await p.check('[name=m-tipo][value=Mescla]');
    ok(await p.locator(".misto-aviso").isVisible() && /20 da ETEC, 20 da FATEC/.test(await p.locator("#m-info").innerText()), "mescla: aviso de sem nota e metade de cada prova");
    await p.check('[name=m-tipo][value=Enem]'); await p.check('[name=m-area][value=Matemática]');
    ok(/90 questões/.test(await p.locator("#m-info").innerText()), "misto Enem: 45 questões por área");
    await p.check('[name=m-tipo][value=Mescla]'); await p.click("#m-ok"); await p.waitForURL(/id=treino/); await p.waitForSelector("#cfg");
    ok((await texto(p)).includes("Simulado mesclado"), "mescla abre o simulado");
    // revisão rápida com erros vencidos
    await p.evaluate(() => { const e = {}; [["etec-2026-1sem", 3], ["fatec-2017-1sem", 12]].forEach(([id, n]) => { e[id + "#" + n] = { provaId: id, numero: n, materia: "X", status: "aberta", proxima: "2020-01-01", ultimo: "2020-01-01", tentativas: 1, motivo: "erro" }; }); localStorage.setItem("treineiros:erros", JSON.stringify(e)); });
    await p.goto(BASE + "estudo.html"); await p.waitForSelector("#b-rapida");
    await p.click("#b-rapida"); await p.waitForURL(/simulado\.html\?id=treino/); await p.waitForSelector("#cfg");
    ok((await texto(p)).includes("Revisão rápida") && (await texto(p)).includes("2 questões"), "revisão rápida monta 2 questões do caderno");
    await p.goto(BASE + "redacao.html"); await p.waitForSelector("#f-red");
    await p.check('input[name="modelo"][value="FATEC"]');
    ok(await p.locator('.tema-op:not([hidden])[data-banca="FATEC"] .tema-op__tag', { hasText: "FATEC" }).count() > 0 && await p.locator('.tema-op:not([hidden])[data-banca="Enem"]').count() === 0, "FATEC: temas com a etiqueta da FATEC");
    await p.getByRole("button", { name: "Começar a escrever" }).click();
    ok((await texto(p)).includes("narrativo ou dissertativo-argumentativo"), "tema da FATEC mostra os gêneros aceitos");
    await p.fill("#texto", "Título\n\nTexto."); await p.getByRole("button", { name: "Terminei" }).click();
    ok((await texto(p)).includes("Orientações da prova da FATEC"), "autoavaliação da FATEC confere as orientações");
    await p.goto(BASE + "fatec.html"); await p.fill("#cf-ac", "42"); await p.fill("#cf-red", "70"); await p.selectOption("#cf-bon", "10");
    ok((await p.locator("#cf-res").innerText()).includes("77,0"), "calculadora da FATEC: 42/60 e redação 70 com +10% = 77,0");
    await p.goto(BASE + "fontes.html"); await p.waitForFunction(() => !/Carregando/.test(document.querySelector("#painel-revisao").textContent));
    ok(/explicações já foram conferidas/.test(await p.locator("#painel-revisao").innerText()), "painel de revisão carrega");
    ok(!(await p.evaluate(() => document.documentElement.scrollWidth > innerWidth)), "fontes sem rolagem lateral no celular");
    await p.context().close();
  }

  console.log("20. Celular: barra de abas, folha Mais, chamada de apoio e página de funcionalidades");
  {
    const p = await novaPagina(browser, { celular: true });
    for (const pag of ["index.html", "provas.html", "estudo.html", "redacao.html", "funcionalidades.html", "apoie.html", "sobre.html", "vestibulares.html", "fontes.html"]) {
      await p.goto(BASE + pag); await p.waitForTimeout(250);
      ok(!(await p.evaluate(() => document.documentElement.scrollWidth > innerWidth)), pag + ": sem rolagem lateral a 390 px");
    }
    await p.setViewportSize({ width: 320, height: 640 });
    for (const pag of ["index.html", "apoie.html", "sobre.html", "funcionalidades.html"]) {
      await p.goto(BASE + pag); await p.waitForTimeout(250);
      ok(!(await p.evaluate(() => document.documentElement.scrollWidth > innerWidth)), pag + ": sem rolagem lateral a 320 px");
    }
    await p.setViewportSize({ width: 390, height: 844 });
    await p.goto(BASE + "estudo.html"); await p.waitForTimeout(250);
    ok(await p.locator(".abas .abas__item").count() === 5 && await p.locator(".abas").isVisible(), "5 destinos visíveis embaixo");
    ok(await p.locator('.abas a[aria-current="page"]').innerText() === "Meu estudo", "aba atual marcada");
    ok(!(await p.locator(".cab__nav").isVisible()), "menu do cabeçalho escondido no celular");
    await p.click("#btn-mais");
    ok(await p.locator("#folha-mais").isVisible(), "folha Mais abre");
    ok(await p.locator('#folha-mais a[href="funcionalidades.html"]').count() === 1, "folha Mais leva a Funcionalidades");
    await p.keyboard.press("Escape"); await p.waitForTimeout(150);
    ok(!(await p.locator("#folha-mais").isVisible()) && await p.evaluate(() => document.activeElement.id === "btn-mais"), "Esc fecha a folha e devolve o foco");
    ok(await p.locator(".apoio-cta").count() === 1 && await p.evaluate(() => document.querySelector(".apoio-cta").nextElementSibling.classList.contains("rodape")), "chamada de apoio logo antes do rodapé");
    ok(await p.locator('#folha-mais a[href="sobre.html"]').count() === 1, "folha Mais leva a Sobre");
    await p.goto(BASE + "sobre.html"); await p.waitForTimeout(200);
    ok(await p.locator(".apoio-cta").count() === 0 && await p.locator('a.rede--linkedin[href*="linkedin.com/in/"]').count() === 1 && await p.locator('a.rede--github[href="https://github.com/Felipotsz"]').count() === 1, "Sobre: links do LinkedIn e do GitHub, sem faixa de apoio repetida");
    ok(!/\(15\)|fg\.bieco|Juvenal/.test(await p.content()), "Sobre: sem telefone, e-mail pessoal nem endereço");
    await p.goto(BASE + "provas.html"); await p.waitForTimeout(200);
    ok((await p.locator(".apoio-cta figcaption").innerText()).trim() === "Felipe Gustavo Bieco", "faixa de apoio: nome embaixo da foto");
    await p.goto(BASE + "apoie.html"); await p.waitForTimeout(200);
    ok(await p.locator(".apoio-cta").count() === 0, "sem chamada de apoio na própria página Apoie");
    await p.goto(BASE + "simulado.html?id=exemplo-enem"); await p.waitForTimeout(300);
    ok(await p.locator(".abas").count() === 0, "sem barra de abas durante a prova");
    await p.setViewportSize({ width: 820, height: 1180 });
    await p.goto(BASE + "provas.html"); await p.waitForTimeout(200);
    ok(await p.locator(".abas").isVisible() && !(await p.locator(".cab__nav").isVisible()), "no tablet: barra de navegação embaixo");
    // computador de verdade (mouse, sem toque): tablet deitado com toque continua com a barra embaixo
    const pc = await novaPagina(browser);
    await pc.setViewportSize({ width: 1280, height: 800 });
    await pc.goto(BASE + "index.html"); await pc.waitForTimeout(200);
    ok(await pc.locator(".cab__nav").isVisible() && !(await pc.locator(".abas").isVisible()), "no computador: menu no topo, sem barra de abas");
    await pc.context().close();
    ok(!p.erros || !p.erros.length, "sem erros de script " + (p.erros || []).join(" | "));
    await p.context().close();
  }

  {
    console.log("\n# Enem: escolha da língua estrangeira");
    const p = await novaPagina(browser, { reais: true });
    await p.goto(BASE + "provas.html?banca=enem&ano=2026"); await p.waitForTimeout(400);
    const pils = await p.$$eval("#ano-2026 .area", as => as.map(a => a.textContent.trim()));
    ok(pils.filter(t => t.startsWith("Linguagens")).length === 1 && pils.length === 4, "Enem 2026: uma pílula só de Linguagens (4 provas)");
    await p.goto(BASE + "simulado.html?id=enem-2026-linguagens-ingles"); await p.waitForTimeout(500);
    ok(await p.locator("[name=lingua]").count() === 3 && await p.locator("[name=lingua][value=ingles]").isChecked(), "abertura: escolha Inglês, Espanhol ou as duas");
    await p.click("label:has([name=lingua][value=espanhol])"); await p.waitForURL(/linguagens-espanhol/); await p.waitForTimeout(400);
    ok(await p.locator("[name=lingua][value=espanhol]").isChecked(), "trocar para Espanhol abre a versão em Espanhol");
    await p.click("label:has([name=lingua][value=ambas])"); await p.waitForURL(/linguagens-ambas/); await p.waitForTimeout(500);
    ok(await contem(p, "50 questões") && await p.locator("[name=formato]").count() === 0, "as duas: 50 questões, sem cartão-resposta");
    await p.click("button[type=submit]"); await p.waitForTimeout(400);
    ok(await contem(p, "Questão 1 de 50"), "as duas: a prova abre com 50 questões");
    await p.goto(BASE + "simulado.html?id=enem-2010-humanas"); await p.waitForTimeout(400);
    ok(await p.locator("[name=lingua]").count() === 0, "outras áreas não mostram a escolha de língua");
    ok(!p.erros.length, "sem erros de script " + p.erros.join(" | "));
    await p.context().close();
  }

  {
    console.log("\n# Menu de acessibilidade");
    const p = await novaPagina(browser, { celular: true });
    await p.goto(BASE + "index.html"); await p.waitForTimeout(250);
    ok(await p.title() === "Treineiros | Simulados e Provas", "título da página inicial");
    ok(await p.locator("#btn-a11y").isVisible(), "botão de acessibilidade no cabeçalho");
    await p.click("#btn-a11y"); await p.waitForTimeout(200);
    ok(await p.locator("#painel-a11y").isVisible(), "painel abre");
    for (let i = 0; i < 4; i++) await p.click('#painel-a11y [data-acao="fonte"][data-valor="1"]:not([disabled])').catch(() => {});
    await p.click('#painel-a11y [data-acao="readingFont"][data-valor="dislexia"]');
    await p.click('#painel-a11y [data-acao="textSpacing"][data-valor="amplo"]');
    await p.click('#painel-a11y [data-acao="alternar"][data-valor="highContrast"]');
    const at = await p.evaluate(() => { const h = document.documentElement; return [h.style.fontSize, h.dataset.a11yFonte, h.dataset.a11yEspacamento, h.hasAttribute("data-a11y-contraste")]; });
    ok(at[0] === "24px" && at[1] === "dislexia" && at[2] === "amplo" && at[3], "opções chegam à página (150%, dislexia, amplo, contraste)");
    await p.keyboard.press("Escape"); await p.waitForTimeout(150);
    ok(!(await p.locator("#painel-a11y").isVisible()) && await p.evaluate(() => document.activeElement.id === "btn-a11y"), "Esc fecha e devolve o foco");
    for (const w of [390, 320]) {
      await p.setViewportSize({ width: w, height: 700 });
      for (const pag of ["index.html", "provas.html", "busca.html", "estudo.html", "vestibulares.html", "apoie.html", "sobre.html", "funcionalidades.html", "q/exemplo-enem/1.html"]) {
        const r = await p.goto(BASE + pag); if (!r || !r.ok()) continue;
        await p.waitForTimeout(200);
        ok(!(await p.evaluate(() => document.documentElement.scrollWidth > innerWidth)), pag + `: texto grande + dislexia + amplo, sem rolagem lateral a ${w} px`);
      }
    }
    await p.goto(BASE + "provas.html"); await p.waitForTimeout(200);
    ok(await p.evaluate(() => document.documentElement.getAttribute("data-a11y-fonte") === "dislexia"), "a escolha vale nas outras páginas");
    await p.keyboard.press("Alt+A"); await p.waitForTimeout(150);
    ok(await p.locator("#painel-a11y").isVisible(), "Alt + A abre o painel");
    await p.click('#painel-a11y [data-acao="restaurar"]');
    ok(await p.evaluate(() => !document.documentElement.style.fontSize && !document.documentElement.hasAttribute("data-a11y-fonte")), "Restaurar volta ao padrão");
    ok(!p.erros.length, "sem erros de script " + p.erros.join(" | "));
    await p.context().close();
  }

  await browser.close();
  console.log(falhas ? `\n${falhas} FALHA(S)` : "\nTudo certo.");
  process.exit(falhas ? 1 : 0);
})();
