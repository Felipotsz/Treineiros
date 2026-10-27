/* Configurações do projeto. Edite aqui depois de publicar. */
var Config = {
  // Endereço de "novo relato" do seu repositório no GitHub (botão "Reportar erro").
  // Enquanto tiver SEU-USUARIO, o botão apenas copia o texto do relato.
  repoIssues: "https://github.com/Felipotsz/Treineiros/issues/new",
  minutosPorQuestaoTreino: 3,                 // tempo sugerido nos treinos
  intervalosRevisaoDias: [1, 3, 7, 14, 30],   // revisão espaçada das questões erradas

  // Estimativa de nota TRI do Enem (só aparece quando a prova tem os parâmetros "tri" de todas as questões).
  // nota = media + dp × θ. "calibracao" permite ajustar por área depois de comparar com notas oficiais,
  // ex.: { "Matemática": { media: 489, dp: 134 } }.
  tri: { D: 1, media: 500, dp: 100, calibracao: {} },

  // Página "Apoie" (apoie.html). Enquanto pixChave estiver vazia, a página mostra "Pix em breve" no lugar do QR code.
  // pixQr: caminho da imagem do QR code (gere no app do seu banco e salve em assets/apoio/).
  apoio: {
    pixChave: "",                              // chave aleatória, ex.: "123e4567-e89b-12d3-a456-426614174000"
    pixNome: "",                               // nome que aparece no app do banco ao pagar
    pixQr: "assets/apoio/pix-qr.png"
  },

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
