# Progresso da extração

## Publicadas
- etec-2026-2sem (piloto)
- etec-2024-2sem (10 figuras; poema de Lubi Prates como imagem; Q25 retificada B)
- etec-2024-1sem (6 figuras; letra da Canção pra Amazônia como imagem)
- etec-2023-2sem (10 figuras; tabelas de lacunas viram "I: x; II: y")
- etec-2023-1sem (40 questões, 3 h; 8 figuras; texto sobre ilustração transcrito)
- etec-2022-2sem (tema Profissões; alternativas-imagem Q34 e Q44)
- etec-2020-1sem (sem tema; Q23 ANULADA com justificativa por análise; Q42 alternativas-imagem de ímãs)
- etec-2019-2sem (tema Biodiversidade; 12 figuras; textos longos via aj.trecho())
- etec-2019-1sem (12 figuras de apoio; Q48 gabarito oficial usa atalho "tirar 12%", explicado)
- etec-2018-2sem (tema Sustentabilidade; caixas de texto viram figura no rascunho: textos via trecho(); Q33 alternativas-imagem)
- etec-2018-1sem (sem tema; letras de Carlinhos Brown, Jeneci e Marisa Monte e alternativas com versos como imagem; Q33, Q43, Q44 alternativas-imagem)
- etec-2017-2sem (tema Diversão; Q30/Q31 ANULADAS: figura da Tabela ausente, justificativa por análise; Q19, Q23, Q42 alternativas-imagem)
- etec-2025-1sem (refeita; tema Plantas; 7 figuras; tabelas Q5/Q17/Q18 em HTML; isótopos Q41 em KaTeX; poema Q50 como imagem)
- etec-2026-1sem (refeita; PDF recolocado)
- etec-2017-1sem (tema Um mundo melhor; rascunho embaralhou Q43-46, escritas à mão; letra O Sal da Terra como imagem)

- fatec-2026-2sem (tema Futebol; 60 questões; poema de Vinicius como imagem)
- fatec-2026-1sem (tema Ciência e tecnologia; rascunho embaralhou p11, p15-18; letra Rocket Man como imagem; tabela de durações Q46 fica no P46 para não vazar para Q47/48)
- fatec-2025-2sem (tema Economia verde; 64 questões, não 60: gabaritos.py cortava em 60, Q61-64 postas à mão; letras Sementes e Quebradeiras como imagem; Q41 alternativas-imagem)
- fatec-2023-1sem (tema Tecnologia; tudo escrito no ajustes.py; Q4 e Q42 de tabela/diagramas; Q17 KaTeX; Q44 texto em duas colunas montado à mão)
- fatec-2023-2sem (tema Alimentação; rascunho embaralhou as colunas: todos os enunciados e alternativas escritos no ajustes.py; Q39 ANULADA com justificativa por análise (guia do rótulo diz '20 % or less is high'); Q40 com observação (kcal × cal); Q12 aresta lateral 13 → apótema 12; Q51 fórmulas condensadas)
- fatec-2024-1sem (tema Arte; caixas de texto viraram figura: textos via trecho(); Q14 sumiu do rascunho, escrita à mão; letras Fotografia 3x4 e O Pulso como imagem; Q42 alternativas-imagem; Q49 com observação sobre a simplificação da banca)
- fatec-2024-2sem (tema América Latina; caixas de texto viraram figura: textos via trecho(); Q44 retificada C; Q29 equações nucleares em KaTeX)

## Perdidas no reinício de 23/10
- (refeitas: etec-2026-1sem, etec-2025-1sem)

## Em andamento
- FATEC (15 provas)


## Lições
- aj.trecho(id, pág, início, fim, [inícios de parágrafo]): copia texto do texto.txt (pymupdf) sem redigitar; repor itálicos à mão.
- montar.py: apoio_de herda só as figuras citadas no apoio (não as da pergunta da outra questão).
- Figura como alternativa: CSS limita a 10rem de altura (.alts-lista/.alt).
- Anulada sem motivo oficial: buscar na web; se nada, anulacao {fonte: 'analise', motivo} e explicação de como seria resolvida.
- tools/aj.py: enun(R, n, quebras, trocas, chamada, figs), tabela(), colunas(), completar(Q, R) no fim do ajustes.py.
- rascunho.py corrigido (figura de largura total quebrava a ordenação).
- Gabaritos com 'Retificada' adicionados à mão em gabaritos.json (ETEC 2024/2 Q25, FATEC 2024/2 Q44).
- Reinício do ambiente apaga tudo: rodar tools/salvar.sh <nome> a cada 2 ou 3 provas e enviar o zip.
- apoio_de: o texto da pergunta da questão-fonte (P_n) precisa conter tudo o que é só dela (tabelas, 'Logo, ...'), senão vaza para as irmãs.
- Escrever ajustes.py grandes em duas partes (Write + cat >>), e nunca transcrever letra de música: só imagem + alt descritivo.
- rascunho.py: figuras vazias/fora da página são descartadas (davam erro no pixmap).
