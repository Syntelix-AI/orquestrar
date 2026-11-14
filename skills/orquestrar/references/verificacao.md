# Verificação

Um texto bem escrito e errado é o risco principal do trabalho com IA, porque parece pronto. Por isso quem produz não aprova, e o critério é escrito **antes** de produzir.

## Classes

| Classe | Exemplos | Como verificar | Quem verifica |
|---|---|---|---|
| **V1 Executável** | soma de planilha, fórmula, script, formato de arquivo | rodar um check | o próprio check |
| **V2 Rastreável** | fatos de pesquisa, números de mercado, citação de lei ou norma | abrir a fonte e conferir cada afirmação importante | uma passada separada ou outro agente |
| **V3 Critérios** | texto no tom certo, documento completo, slides claros | aplicar a lista de critérios escrita antes | outro agente que não viu a produção |
| **V4 Humano** | preço, estratégia, mérito jurídico ou médico, gosto | apresentar opções e consequências | só a pessoa |

Quanto mais baixa a classe, mais barata a verificação. V4 nunca é "aprovado" por agente.

## Como montar os critérios

Escreva de 3 a 7 critérios observáveis antes de produzir. Exemplo para uma notificação extrajudicial:

- identifica remetente, destinatário e o fato com data;
- diz o que é pedido e em que prazo;
- lista os documentos anexos ou que faltam;
- não afirma lei ou número de artigo que não foi conferido;
- tem aviso de que é rascunho para revisão profissional.

## Revisão independente

- Em C3 ou acima: crie um revisor com só os critérios e o artefato. Ele devolve achados concretos ("o critério 3 falha porque…"), não opinião geral.
- Abaixo de C3: faça uma leitura separada, só de verificação, com os critérios na frente. Não revise enquanto escreve.

## Uma correção, depois mude

Corrija os achados uma vez e confira de novo só o que foi corrigido. Se o mesmo problema voltar, o problema é a abordagem: mais contexto, outra divisão ou um modelo mais forte.

## Diga o que ficou de fora

Todo recibo diz o que não foi possível verificar. "Não consegui conferir os preços ao vivo" é informação valiosa; esconder isso não é.
