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
  for (const nome of ["indice-questoes.json", "busca.json"])
    await alvo.route(new RegExp("/data/" + nome.replace(".", "\\.") + "$"), r => r.fulfill({ path: path.join(FIX, nome), contentType: "application/json" }));
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
    ok((await texto(p)).includes("questão 2 de 3"), "recarregar na pausa → tela de retomar na questão 2");
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
    await p.goto(BASE + "simulado.html?id=exemplo-etec");
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
    await p.goto(BASE + "simulado.html?id=exemplo-enem");
    ok((await texto(p)).includes("questão 1 de 3"), "andamento v1 com atual fora do limite → questão 1");
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
    await p.waitForURL(/resultado/); await p.getByRole("link",{name:"Refazer só as erradas"}).click();
    await p.getByRole("button",{name:"Começar a prova"}).click();
    ok((await p.locator("#qt").getAttribute("aria-label")) === "Questão 1 de 3", "erradas: 3 questões");
    await p.click('[data-letra="B"]');                          // deixa um andamento de "erradas"
    await p.goto(BASE + "simulado.html?id=exemplo-enem"); await p.getByRole("button",{name:"Começar a prova"}).click();
    await p.click('[data-letra="B"]'); await p.click("#b-fim"); await p.getByRole("button",{name:"Finalizar mesmo assim"}).click();
    await p.waitForURL(/resultado/); await p.getByRole("link",{name:"Refazer só as erradas"}).click();
    await p.waitForTimeout(300);
    ok(!(await texto(p)).includes("em andamento"), "andamento antigo de 'erradas' foi descartado");
    ok((await texto(p)).includes("2 questões"), "erradas novas: 2 questões");
    await p.context().close();
  }


  console.log("9. Logo, fórmulas locais e página estática de questão");
  {
    const p = await novaPagina(browser);
    await p.goto(BASE + "index.html");
    ok(await p.locator(".cab .logo").count() === 1 && await p.locator(".rodape .logo").count() === 1, "logo no cabeçalho e no rodapé");
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
    await p.goto(BASE + "busca.html"); await p.fill("#b-texto", "fotossintese"); await p.waitForTimeout(500);
    ok((await p.locator("#b-contagem").innerText()).startsWith("1 "), "busca sem acento encontra 'fotossíntese'");
    ok(await p.locator("#cesta").isHidden(), "cesta escondida enquanto vazia");
    await p.check("input[data-k]"); await p.fill("#b-texto", "plural"); await p.waitForTimeout(500); await p.check("input[data-k]");
    await p.fill("#c-nome", "Lista da turma");
    const url = await p.evaluate(() => Treino.endereco("lista.html?l=" + encodeURIComponent(Treino.codificarLista(JSON.parse(localStorage.getItem("treineiros:lista-montando")))) + "&t=Lista%20da%20turma"));
    await p.goto(url);
    ok(await contem(p, "Lista da turma", "2 questões"), "link da lista abre com 2 questões");
    await p.getByRole("button", { name: "Começar o treino" }).click(); await p.waitForURL(/id=treino/);
    ok((await texto(p)).includes("2 questões"), "lista vira treino");
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
    ok((await texto(q)).includes("1</strong>") || (await texto(q)).includes("1 simulados"), "página de receber lê o link");
    await q.getByRole("button", { name: "Receber o progresso" }).click(); await q.waitForURL(/estudo/);
    ok((await q.evaluate(() => JSON.parse(localStorage.getItem("treineiros:meta")).questoesDia)) === 25, "progresso chegou no outro aparelho");
    await q.context().close(); await p.context().close();
  }

  console.log("15. Redação");
  {
    const p = await novaPagina(browser);
    await p.goto(BASE + "redacao.html");
    await p.check('input[name="modelo"][value="Enem"]').catch(() => {});      // modelo Enem: 5 competências
    const sel = p.locator("select").first();                                 // tema do Enem (a FATEC exige título)
    if (await sel.count()) { const v = await sel.evaluate(s => { const o = [...s.options].find(o => /Enem/.test(o.parentElement.label || "")); return o ? o.value : null; }); if (v) await sel.selectOption(v); }
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
    ok(t.includes("Em 2021 não houve prova em nenhum semestre"), "2021 explicado uma vez, no topo do ano");
    ok(await p.locator(".ed--sem-prova").count() === 8, "8 semestres sem prova (2020/2, 2021/1, 2021/2, 2022/1 × ETEC e FATEC)");
    ok((await p.locator(".ed--em-breve", { hasText: "Em breve" }).count()) >= 2, "ETEC 2025/2 e FATEC 2025/1 aparecem como em breve");
    await p.locator(".chip", { hasText: "FATEC" }).click();
    ok((await p.locator(".ed .ed__banca", { hasText: "ETEC" }).count()) === 0 && (await p.locator(".ed .ed__banca", { hasText: "FATEC" }).count()) > 0, "filtro FATEC esconde ETEC");
    await p.locator(".chip", { hasText: "Todas" }).click(); await p.check("#f-so");
    ok(await p.locator(".ed--sem-prova").count() === 0, "'Só provas disponíveis' esconde os semestres sem prova");
    ok(!(await p.evaluate(() => document.documentElement.scrollWidth > innerWidth)), "sem rolagem lateral no celular");
    await p.context().close();
  }

  console.log("18. Provas reais no celular: todas as questões, figuras, fórmulas, navegação");
  {
    const lista = JSON.parse(fs.readFileSync(path.join(__dirname, "..", "data", "provas.json"), "utf8"));
    for (const meta of lista) {
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

  await browser.close();
  console.log(falhas ? `\n${falhas} FALHA(S)` : "\nTudo certo.");
  process.exit(falhas ? 1 : 0);
})();
