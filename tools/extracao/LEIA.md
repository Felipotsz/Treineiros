# Como uma prova em PDF vira prova no site

Fluxo usado em todas as provas da ETEC e da FATEC. Cada passo deixa um arquivo que dá para conferir.

Precisa de: `pip install pymupdf pillow` (e `pdftotext`, do pacote poppler, para ler os gabaritos).

## 1. Rascunho automático
```
python3 tools/extracao/rascunho.py PROVA.pdf trabalho/<id>/rascunho --paginas 2-23
```
O script:
- lê o texto na ordem certa (uma ou duas colunas);
- mantém negrito, itálico, sobrescrito e subscrito, e o ℓ das fórmulas químicas;
- separa as questões e as alternativas;
- reconhece os textos de apoio compartilhados ("Leia o texto para responder às questões 8 e 9").

Ele também salva as páginas em imagem (`pag/`) e um recorte automático das figuras (`fig/`), que só serve de ponto de partida.

**Não confie no rascunho:** ele erra em fórmulas montadas (isótopos, frações), rótulos dentro de figuras, poemas e faixas que estão como imagem.

## 2. Gabarito oficial
O gabarito vem **só** do PDF oficial. Linhas com "ANULADA" e "Retificada" precisam de atenção. Um caso real: em FATEC 1SEM20, as questões 51 e 52 mostram a letra e "ANULADA" na coluna da disciplina.

## 3. Recorte das figuras
1. `python3 tools/extracao/grade.py PROVA.pdf trabalho/<id>/grade 4 7 11` gera as páginas com uma grade de coordenadas.
2. Também dá para listar as coordenadas dos desenhos e dos textos curtos de cada página com o PyMuPDF.
3. Escreva os retângulos em `recortes.json` (`{"q06": [página, x0, y0, x1, y1]}`).
4. Rode `python3 tools/extracao/recortar.py PROVA.pdf recortes.json trabalho/<id>/img` e **confira cada recorte**, procurando rótulos cortados.

Tabelas simples viram `<table>` em HTML, não imagem.

## 4. Ajustes (conferência humana)
`trabalho/<id>/ajustes.py` é onde fica o trabalho de verdade. Ele tem:
- `META` (data do exame, duração, tema, apresentação, PDF);
- para cada questão:
  - matéria, assunto e tags;
  - correções do texto, conferidas com a imagem da página;
  - figuras com **descrição para leitor de tela**;
  - **explicação** (por que a certa está certa e por que cada errada está errada);
  - nas anuladas: `anulacao` com `fonte` ("oficial" ou "analise") e o `motivo`.

As regras de conteúdo são as do prompt de extração:
- transcrição fiel (inclusive erros do original);
- fórmulas em LaTeX;
- o mesmo nome para o mesmo assunto (veja `data/assuntos.json`);
- `explicacaoRevisada` sempre `false`, até uma pessoa conferir em `revisar.html`.

## 5. Montar, validar e testar
```
python3 tools/extracao/montar.py trabalho/<id>/ajustes.py trabalho/<id>/rascunho/rascunho.json gabaritos.json trabalho/<id>/img
python3 tools/validar.py --aceitar-assuntos     # só depois de conferir os assuntos novos
python3 tools/validar.py --indexar
node tools/testar_navegador.js http://localhost:8000/
```
O `montar.py` avisa sobre marcador de figura esquecido, questão sem explicação e anulada sem justificativa. O teste de navegador passa por **todas as questões de todas as provas** numa tela de celular. Ele confere:
- rolagem lateral;
- figuras que não carregam;
- fórmulas que não foram desenhadas.

Por fim, copie o PDF da prova para `assets/provas/<id>.pdf` (usado no modo cartão-resposta) e tire o `status` da edição em `data/edicoes.json`, se houver.
