/* Configurações do projeto. Edite aqui depois de publicar. */
var Config = {
  // Endereço de "novo relato" no GitHub. O botão "Reportar erro" só usa este caminho se contatoEmail estiver vazio.
  repoIssues: "https://github.com/Felipotsz/treineiros/issues/new",
  // E-mail que recebe os relatos de erro: o botão "Reportar erro" abre o aplicativo de e-mail com o relato pronto.
  contatoEmail: "educacao.treineiros@gmail.com",
  // Onde baixar os cadernos e gabaritos oficiais. O site não guarda mais os PDFs: a tela de abertura de cada prova
  // aponta para cá (ou para "linkProva" da prova, se ela tiver um link direto para o PDF).
  fontesOficiais: {
    Enem: { nome: "Inep", url: "https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/enem/provas-e-gabaritos" },
    ETEC: { nome: "Vestibulinho Etec", url: "https://www.vestibulinhoetec.com.br/" },
    FATEC: { nome: "Vestibular Fatec", url: "https://www.vestibularfatec.com.br/" }
  },
  // Contagem de visitas com o GoatCounter (sem cookies, sem dados pessoais). Crie a conta em goatcounter.com com o
  // e-mail do projeto e ponha aqui só o código do site: "treineiros" para https://treineiros.goatcounter.com.
  // Vazio = nada é contado e nenhum script de fora é carregado.
  goatcounter: "treineiros",
  minutosPorQuestaoTreino: 3,                 // tempo sugerido nos treinos
  intervalosRevisaoDias: [1, 3, 7, 14, 30],   // revisão espaçada das questões erradas

  // Estimativa de nota TRI do Enem (só aparece quando a prova tem os parâmetros "tri" de todas as questões).
  // nota = media + dp × θ. "calibracao" permite ajustar por área depois de comparar com notas oficiais,
  // ex.: { "Matemática": { media: 489, dp: 134 } }.
  tri: { D: 1, media: 500, dp: 100, calibracao: {} },

  // Página "Apoie" (apoie.html). Enquanto pixChave estiver vazia, a página mostra "Pix em breve" no lugar do QR code.
  // pixQr: caminho da imagem do QR code (gere no app do seu banco e salve em assets/apoio/).
  apoio: {
    pixChave: "educacao.treineiros@gmail.com",  // chave Pix (e-mail)
    pixNome: "Felipe Gustavo Bieco",           // nome que aparece no app do banco ao pagar
    pixQr: "assets/apoio/pix-qr.png"
  },

  // Próximas provas, na página inicial (acima do rodapé). Deixe "data" vazia enquanto o edital não sair: aparece "Em breve".
  // Quando sair, ponha a data no formato "AAAA-MM-DD" (e, se quiser, o link do edital). Prova que já passou some sozinha.
  proximasProvas: [
    { banca: "ETEC", titulo: "Vestibulinho, 1º semestre de 2027", data: "", link: "", nota: "Data em breve, no edital do Centro Paula Souza" },
    { banca: "FATEC", titulo: "Vestibular, 1º semestre de 2027", data: "", link: "", nota: "Data em breve, no edital do Centro Paula Souza" },
    { banca: "Enem", titulo: "Enem 2027", data: "", link: "", nota: "Data em breve, no edital do Inep" }
  ],

  // Pontuação no formato de cada vestibular. Confira no manual do candidato de cada ano e ajuste aqui.
  pontuacao: {
    ETEC: {
      descricao: "No Vestibulinho, cada acerto vale 1 ponto.",
      acrescimos: [                                     // Sistema de Pontuação Acrescida (percentuais sobre a nota)
        { id: "escola-publica", rotulo: "Cursei todo o Ensino Fundamental II em escola pública", percentual: 10 },
        { id: "afrodescendente", rotulo: "Sou afrodescendente", percentual: 3 }
      ]
    },
    FATEC: {
      descricao: "Mostramos só a parte objetiva: a nota oficial do Vestibular Fatec também considera a redação, que não faz parte do simulado.",
      acrescimos: []
    }
  }
};
