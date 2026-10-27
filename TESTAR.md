# Roteiro de teste no navegador

Os testes automáticos (`tools/testar_navegador.js`) cobrem a lógica: tempo, armazenamento, dados antigos, links. Este roteiro é para o que só uma pessoa vê: aparência, leitura e sensação de uso. Faça uma vez no computador e uma vez no celular, nos dois temas (botão "Modo noturno").

Antes: `python3 tools/validar.py --indexar`, depois `python3 -m http.server 8000` e abra http://localhost:8000.

## 1. Início e provas
1. **Início:** o logo aparece com as duas canetas pingando nos "i", sem cortes. No celular, o menu cabe numa faixa que rola de lado, e o botão de tema fica ao lado do logo.
   - *Confira:* nada encostado na borda; a página não rola para o lado.
2. **Provas:** os filtros de banca, ano e matéria funcionam juntos. Também abra `provas.html?banca=etec`, que já deve vir com ETEC escolhida.
   - *Confira:* os cartões têm a mesma altura na mesma linha e a etiqueta da banca é legível.

## 2. Simulado na tela
1. Inicie o Enem em **modo estudo** e responda certo e errado.
   - *Confira:* verde para o certo e vinho para o errado, com o texto "Você acertou", "Errada" e "Gabarito" (a cor não é o único sinal). A explicação aparece logo abaixo.
2. Use **✕** para eliminar uma alternativa: ela fica riscada. Depois use **Marcar para revisão** e **Foi chute**.
   - *Confira:* o quadrado da questão no mapa fica tracejado.
3. **Pausar:** a tela de pausa esconde a questão. Agora **recarregue a página** (F5), clique em **Continuar** e confira se voltou na mesma questão e com o mesmo tempo, com no máximo 5 segundos de diferença.
4. Teste as **anotações**, o **rascunho**, **Ocultar tempo** e **Modo foco** (que esconde o menu).
5. **Teclado (computador):**
   - as letras A a E respondem;
   - Shift + letra elimina;
   - as setas navegam;
   - M marca;
   - P pausa.
6. **Figura:** clique na figura para ampliar. A janela fecha com Esc ou com o botão Fechar.
7. Clique em **Finalizar** com questões em branco.
   - *Confira:* o aviso mostra quantas faltam e o botão "Ir para a primeira em branco" funciona.

## 3. Cartão-resposta
1. Na ETEC, escolha **Cartão-resposta**. A correção "Modo estudo" fica desativada.
2. Marque as bolinhas.
   - *Confira:* a marcada fica preenchida; no celular, dá para tocar sem errar a vizinha.
3. Finalize e confira o resultado.

## 4. Resultado
1. **Placar:** número grande e percentual. O tempo médio por questão e o "onde mais demorou" fazem sentido.
2. **ETEC:** aparece o bloco "No formato ETEC" com a pontuação acrescida. Marque as caixas e confira a conta: 10% e 3% somam 13%.
3. **Para revisar:** abra uma questão. Ela mostra figura, a sua resposta, a correta, a explicação, as anotações e o link "Abrir só esta questão".
4. Teste **Refazer só as erradas**, **Compartilhar** (no celular abre o menu de compartilhar) e **Imprimir**.
   - *Confira na prévia de impressão:* sem menu, com todas as questões abertas e fundo branco.

## 5. Meu estudo
1. Defina a **meta** e a **contagem regressiva**. A home deve mostrar "Faltam N dias".
2. Faça 2 simulados e veja o **gráfico de evolução**, a tabela **por assunto** e o **plano**, que aponta assuntos e matérias fracos.
3. Em **Treino por matéria**, marque uma matéria e veja os assuntos dela aparecerem. Marque um assunto e monte o treino.
4. No **Caderno de erros**, teste os filtros e "Treinar os erros em aberto".

## 6. Busca, listas e questão avulsa
1. Procure uma palavra com e sem acento ("fotossintese" deve achar "fotossíntese").
2. Marque 2 questões, dê nome à lista e clique em **Copiar link da lista**. Abra o link em outra aba: aparece a lista com o botão "Começar o treino".
3. Abra uma questão avulsa (`questao.html?id=...&n=...`), responda e use "Copiar link".

## 7. Redação
1. Escolha um tema e escreva.
   - *Confira:* as linhas da pauta acompanham o texto (no celular também); a contagem de linhas avisa abaixo de 8 e acima de 30.
2. **Pausar:** o texto fica travado. Saia da página e volte: aparece "Continuar".
3. Faça a autoavaliação, guarde a redação e veja ela no histórico.

## 8. Progresso entre aparelhos (só no site publicado, em https)
1. **Exportar e importar arquivo:** importe num navegador anônimo e confira se o histórico voltou.
2. **QR code:** gere o QR no computador, aponte a câmera do celular, abra o link e toque em "Receber o progresso". O Meu estudo do celular passa a mostrar o histórico.
3. **Modo offline:** abra o site, desligue a internet e navegue entre as páginas e uma prova. As fórmulas continuam aparecendo.

## 9. Acessibilidade (rápido)
1. **Tab desde o topo:** o primeiro item é "Pular para o conteúdo"; o contorno dourado aparece em tudo que recebe foco.
2. **Leitor de tela** (NVDA no Windows, VoiceOver no Mac ou iPhone, TalkBack no Android):
   - ao responder, ele lê a explicação;
   - os avisos ("Faltam 10 minutos", "Link copiado") são lidos;
   - a alternativa marcada é anunciada como "pressionado".
3. **Zoom de 200% no navegador:** nada some e nada se sobrepõe.
4. **Animações reduzidas** (nas configurações do sistema): as transições somem.

Encontrou algo? Anote a página, o aparelho, o tema e o passo, e me mande.
