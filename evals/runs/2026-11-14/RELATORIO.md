# Rodada de evals · 2026-11-14

## Resultado

| Caso | Rodada | Vencedor | Pontuação (skill vs baseline) |
|---|---|---|---|
| 01 Jurídico, plano de saúde | 1 | **skill** | 14 vs 8 |
| 02 TCC em 6 semanas | 1 | **skill** | 13 vs 8 |
| 03 Padaria no bairro | 1 | **skill** | 14 vs 9 |
| 04 Planilha casa + ateliê | 1 | **skill** (apertado) | 14 vs 11 |
| 05 Posts do mês | 1 | **skill** | 15 vs 7 |
| 06 Armadilha: MEI ou ME | 1 | empate | 15 vs 15 |
| 07 Armadilha: cobrança por e-mail | 1 | baseline | 11 vs 14 |
| 07 após reparo | 2 | **skill** (apertado) | 13 vs 12 |
| 08 Juntar 30 planilhas | 1 | **skill** | 14 vs 11 |
| 09 Roteador de modelos, 40 contratos | 2 | **skill** | 15 vs 13 |

**v0.1 (8 casos):** 6 vitórias, 1 empate, 1 derrota na armadilha 07. Reprovada pelo critério "não perder nas armadilhas".
**v0.2 (9 casos, com reparo e roteador):** 8 vitórias, 1 empate. Aprovada (meta: 7 de 9, sem derrota nas armadilhas).

## O reparo

No caso 07 a skill acertou o gate (não enviou nada), mas fez três perguntas e descreveu o processo em vez de preparar. A resposta vencedora já mostrava a lista de atrasados e o texto, pedindo só o "pode enviar". Mudança na v0.2: preparar é fazer de verdade tudo o que é reversível e mostrar o concreto; quando dá para adiantar sem risco, adiantar e perguntar em cima do rascunho.

## O que mais diferenciou (juiz)

- Até 3 perguntas com resposta padrão ("pode dizer só 'segue'") venceu 4 ou mais perguntas sem padrão.
- Anunciar um artefato retomável (arquivo de estado, planilha com fórmulas, calendário editável) venceu conteúdo despejado no chat.
- Declarar restrições óbvias ("não altero os originais", "não publico") decidiu casos.
- No 09, o baseline também distribuiu níveis de modelo; o diferencial da skill foi o revisor independente do ranking e a preservação dos originais.

## Limites desta rodada

- Avalia só a primeira resposta, simulada; não a execução completa.
- Uma amostra por caso, e produtor e juiz da mesma família de modelo (Sonnet). Os casos 04 e 07 tiveram margens pequenas.
- No 07 da rodada 2, a skill foi comparada com a resposta do baseline da rodada 1.
- A rodada no Codex (portabilidade) não rodou: a delegação do T3 só funciona de dentro de uma thread do T3, e criar uma thread exigia autorização.

## Próximos passos sugeridos

1. Rodar no Codex e num chat sem ferramentas (C0) para testar a portabilidade.
2. Repetir cada caso 3 vezes e usar um juiz de outra família de modelo.
3. Avaliar uma execução completa em 2 casos (01 e 08), com simulador de usuário.
