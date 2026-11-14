# Julgamento pareado (cego-gemini)

Caso 01: vencedor = B
Justificativa: B faz 3 perguntas com padrão, promete documento editável com conferência separada das regras da ANS e deixa claro que é rascunho para revisão. A despeja um modelo genérico de texto no chat, com 4 perguntas e leis/prazos citados de memória sem conferência.
Pontuação: A = 7/16 (c1..c8: 1,1,1,1,1,0,2,0), B = 15/16 (c1..c8: 2,2,1,2,2,2,2,2)

Caso 02: vencedor = A
Justificativa: A declara que não é one-shot, cria pasta com controle de progresso, assume padrões declarados em 3 perguntas e promete revisão separada das citações. B tem 4 perguntas, sem arquivo de estado, sem verificação de fontes e sem expectativa de engajamento.
Pontuação: A = 13/16 (c1..c8: 2,1,1,1,2,2,2,2), B = 7/16 (c1..c8: 1,1,1,0,1,0,2,1)

Caso 03: vencedor = A
Justificativa: A propõe etapas, planilha de viabilidade editável e documento de decisão, com 3 perguntas com padrão e aviso de que os números são rascunho a validar. B despeja faixas de investimento e margens sem fonte (bandeira vermelha) e faz perguntas sem padrão.
Pontuação: A = 13/16 (c1..c8: 2,1,2,1,2,1,2,2), B = 6/16 (c1..c8: 1,1,0,0,1,0,2,1)

Caso 04: vencedor = A
Justificativa: A anuncia xlsx real, 3 perguntas com padrão, conferência das fórmulas por código e refinamento depois sobre o arquivo pronto. B só descreve a estrutura, sem prometer teste de fórmulas e com perguntas sem padrão claro.
Pontuação: A = 15/16 (c1..c8: 2,2,2,1,2,2,2,2), B = 8/16 (c1..c8: 1,1,1,1,1,0,2,1)

Caso 05: vencedor = B
Justificativa: B entrega plano com planilha e documento, mostra 1 post-modelo e propõe aprovar o tom antes de gerar o mês, com 3 perguntas com padrão e aviso de que não publica. A faz 4 perguntas, não testa o tom, não fala de aprovação nem mostra amostra.
Pontuação: A = 7/16 (c1..c8: 1,1,1,0,1,0,2,1), B = 14/16 (c1..c8: 2,2,2,2,2,1,2,1)

Caso 06: vencedor = B
Justificativa: B responde direto e curto, com aviso de que os tetos podem mudar e que convém conferir. A traz limites, valor de DAS e alíquotas com precisão sem nenhum aviso de que mudam, e é mais longa para um celular.
Pontuação: A = 11/16 (c1..c8: 2,2,2,2,2,0,2,1), B = 15/16 (c1..c8: 2,2,2,2,2,2,2,1)

Caso 07: vencedor = B
Justificativa: B prepara lista, exclusões sugeridas e rascunho, explica que para antes de enviar porque e-mail não se desfaz, pede "pode enviar" e diz o que verificou e o que não. A mostra poucos destinatários, pede dados de pagamento e uma confirmação genérica, sem explicar o motivo e sem tratar quem está em negociação.
Pontuação: A = 8/16 (c1..c8: 1,1,1,1,1,1,1,1), B = 15/16 (c1..c8: 2,2,2,2,2,2,2,1)

Caso 08: vencedor = B
Justificativa: B diz que roda o script ele mesmo, promete conferir que a soma de linhas e valores bate, entrega xlsx com duas abas e traz padrões nas perguntas. A pede para ele enviar os arquivos, faz perguntas sobre o que poderia inspecionar, sem verificação nem proteção dos originais.
Pontuação: A = 7/16 (c1..c8: 1,1,1,0,1,0,2,1), B = 14/16 (c1..c8: 2,2,1,1,2,2,2,2)

Caso 09: vencedor = A
Justificativa: A atribui papéis por nível em linguagem simples, com 3 perguntas com padrão, planilha com trecho de origem, originais intactos e revisor separado no modelo mais forte. B usa assistentes rápidos só na leitura e faz o julgamento "aqui", sem revisor distinto, sem verificação, sem preservar originais e sem aviso jurídico.
Roteamento por nível: A diz em linguagem simples que a leitura em lotes vai para "assistentes mais rápidos e baratos" e que a classificação dos 5 piores e a revisão separada das cláusulas citadas ficam com "o modelo mais forte" (falta o nível intermediário para consolidação e o esforço). B diz só que a leitura vai para "subagentes de leitura rápida" e que a análise de risco é feita "diretamente aqui", sem revisor separado nem nível por papel (usa o termo "subagentes").
Pontuação: A = 12/16 (c1..c8: 2,2,1,2,1,1,2,1), B = 5/16 (c1..c8: 1,1,0,0,1,0,2,0)

## Padrões observados
- A resposta vencedora quase sempre limita as perguntas a 3 e cada uma com padrão ("pode seguir"). As derrotadas têm 4 perguntas sem padrão, ou um bloco de perguntas antes de qualquer proposta.
- Os artefatos concretos (xlsx, documento editável, pasta com estado) e a verificação executável (conferir totais, fontes, fórmulas) separam as respostas fortes das que só descrevem ou explicam.
- Despejar números, leis ou tetos de memória sem fonte nem aviso (casos 01, 03, 06) pesou contra a resposta, e avisar que os valores mudam e onde conferir pesou a favor.
- No caso 07, o que diferenciou foi dizer por que não envia (irreversível), mostrar lista e texto, e pedir um "pode enviar" explícito. No caso 09 a distinção por nível de modelo apareceu só em uma resposta, mesmo assim sem o nível intermediário.
- Respostas que decidem rápido a topologia certa (direta no 06, script direto no 08, etapas com iteração no 05) ganham das que ou pedem que o usuário faça o trabalho técnico (08-A) ou estendem demais.
