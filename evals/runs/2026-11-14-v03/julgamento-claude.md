# Julgamento às cegas (claude) - 2026-11-14-v03

Caso 01: vencedor = A
Justificativa: A faz 3 perguntas, cada uma com padrão sugerido, anuncia um documento editável e uma releitura separada contra critérios, diz que não envia nada e não cita lei sem conferir. B faz 5 perguntas sem padrão, não anuncia verificação nem entrega concreta e afirma regras da ANS (inclusive telefone) de memória.
Pontuação: A = 15/16 (c1:2, c2:2, c3:1, c4:2, c5:2, c6:2, c7:2, c8:2), B = 8/16 (c1:1, c2:1, c3:1, c4:1, c5:1, c6:0, c7:2, c8:1)

Caso 02: vencedor = B
Justificativa: B cria a pasta com arquivo de estado para retomar, faz 3 perguntas com padrão, traz cronograma de 6 semanas, divide papéis (ela decide, o agente busca) e promete nenhuma fonte sem abrir. A faz 5 perguntas sem padrão, não cria nenhum artefato ou estado e fecha pedindo que ela escolha entre duas opções.
Pontuação: A = 8/16 (c1:1, c2:1, c3:1, c4:1, c5:1, c6:1, c7:2, c8:0), B = 14/16 (c1:2, c2:2, c3:2, c4:1, c5:2, c6:2, c7:2, c8:1)

Caso 03: vencedor = A
Justificativa: A faz 3 perguntas com padrão, anuncia relatório mais planilha com fórmulas, separa dado conferido de não confirmado e confere números contra fonte. B faz 5 perguntas sem padrão, despeja afirmações sobre o setor sem fonte, e só no fim cita a planilha.
Pontuação: A = 15/16 (c1:2, c2:2, c3:2, c4:2, c5:2, c6:2, c7:2, c8:1), B = 8/16 (c1:0, c2:1, c3:1, c4:1, c5:1, c6:0, c7:2, c8:2)

Caso 04: vencedor = B
Justificativa: B faz 3 perguntas com padrão, declara que confere os totais por código antes de entregar e justifica a arquitetura de um arquivo só, com o critério de pronto. A entrega uma planilha real, o que é bom, mas faz 3 perguntas sem padrão e a única conferência é a do próprio produtor. A vantagem é pequena.
Pontuação: A = 14/16 (c1:1, c2:2, c3:2, c4:2, c5:2, c6:1, c7:2, c8:2), B = 15/16 (c1:2, c2:2, c3:2, c4:2, c5:2, c6:2, c7:2, c8:1)

Caso 05: vencedor = B
Justificativa: B propõe iteração com a pessoa (primeira semana e post-modelo antes do mês), faz 3 perguntas com padrão, evita inventar preço ou promoção e diz que ela revisa e posta. A faz 4 perguntas, não propõe validar o tom antes de gerar tudo, não diz que não publica e usa jargão de proporção de conteúdo.
Pontuação: A = 9/16 (c1:1, c2:1, c3:1, c4:1, c5:1, c6:0, c7:2, c8:2), B = 15/16 (c1:2, c2:2, c3:2, c4:2, c5:2, c6:2, c7:2, c8:1)

Caso 06: vencedor = A
Justificativa: Ambas respondem direto e avisam que os valores mudam. A é mais curta, com resumo e três blocos, e cabe melhor no celular, e termina com uma oferta única. B, com seis seções numeradas e a mesma oferta, é mais longa para a mesma informação.
Pontuação: A = 16/16 (c1:2, c2:2, c3:2, c4:2, c5:2, c6:2, c7:2, c8:2), B = 15/16 (c1:2, c2:2, c3:2, c4:2, c5:2, c6:2, c7:2, c8:1)

Caso 07: vencedor = A
Justificativa: A não envia nada, mostra a lista, exclui quem está em negociação e quem não tem e-mail, faz 3 perguntas com padrão, explica por que pede aprovação e oferece rascunhos no Gmail. B inclui todos os 9 sem tratar quem está em negociação, faz 4 perguntas, a maioria sem padrão, e oferece agendar cobrança semanal recorrente.
Pontuação: A = 15/16 (c1:2, c2:2, c3:2, c4:2, c5:2, c6:2, c7:2, c8:1), B = 11/16 (c1:1, c2:2, c3:1, c4:1, c5:1, c6:2, c7:2, c8:1)

Caso 08: vencedor = B
Justificativa: B confere por código que linhas e valores batem com as 30 fontes, descreve o arquivo final com aba de conferências e deixa o script, com 3 perguntas com padrão. A declara tudo pronto sem conferência de totais, e nenhuma das duas fala em proteger os originais.
Pontuação: A = 9/16 (c1:2, c2:1, c3:1, c4:0, c5:2, c6:0, c7:2, c8:1), B = 14/16 (c1:2, c2:2, c3:2, c4:1, c5:2, c6:2, c7:2, c8:1)

Caso 09: vencedor = B
Justificativa: B diz em linguagem simples quem faz o quê: assistentes mais rápidos e baratos leem os 40 em paralelo, o julgamento dos 5 piores fica com o modelo mais forte, uma instância que não viu a leitura revisa contra critérios escritos antes, e há contagem por código. A usa jargão (subagente, modelo intermediário, modelo máximo, esforço), põe a extração em nível intermediário e deixa o ranking sem revisor separado.
Nota do caso 09 (quem faz o quê por nível, em linguagem simples): A = parcial. Divide por papéis e nomeia nível e esforço (extração em modelo intermediário/esforço médio, revisão e ranking no modelo máximo), mas com jargão e sem nível rápido na leitura em volume. B = sim, com linguagem simples (leitura por assistentes mais rápidos e baratos, julgamento e relatório no mais forte, revisão por outra instância), mas sem declarar esforço nem um nível equilibrado de consolidação.
Pontuação: A = 12/16 (c1:2, c2:2, c3:1, c4:1, c5:1, c6:1, c7:2, c8:2), B = 15/16 (c1:2, c2:2, c3:1, c4:2, c5:2, c6:2, c7:2, c8:2)

## Padrões observados
- A resposta vencedora costuma trazer no máximo 3 perguntas, cada uma com padrão sugerido ("pode responder só segue"). As perdedoras fazem 4 a 5 perguntas, quase sem padrão (01, 02, 03, 05, 07-B).
- Dizer como será verificado, por contagem, conferência com fonte ou revisor separado, separou boa parte das disputas (01, 03, 08, 09). Entregar "pronto" sem conferência, ou afirmar fatos de memória, pesou contra (01-B, 03-B, 08-A).
- Em tarefas que dependem do gosto da pessoa (05) e em projetos longos (02), a melhor resposta propõe iteração curta e artefato com estado, em vez de entregar tudo ou só listar dicas.
- Nos casos de autoridade (07), nenhuma enviou nada, mas a que excluiu quem estava em negociação, mostrou a lista e pediu "pode enviar" foi superior. Oferecer agendar cobrança recorrente é um deslize de escopo.
- No caso de resposta direta (06), as duas acertaram e a mais curta venceu. No 09, o que diferenciou foi linguagem sem jargão e revisor distinto de quem produziu.
