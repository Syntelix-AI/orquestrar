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

## Portabilidade: Codex e Gemini (rodada 3, via T3 Code)

Mesmos 9 casos, skill v0.2, cada fornecedor com e sem a skill, em threads separadas no T3 Code e julgamento às cegas por juízes diferentes. Modelos: `gpt-6.1-terra` (Codex) e `gemini-4-argon-medium` (Gemini).

| Fornecedor | Vitórias da skill | Derrotas | Empates | Pontos (skill vs baseline) |
|---|---|---|---|---|
| Codex | 8 | 1 (caso 06) | 0 | 113 vs 80 |
| Gemini | 8 | 0 | 1 (caso 06) | 118 vs 81 |

- A derrota do Codex no 06 foi contaminação do método de teste: os 9 casos rodaram na mesma conversa e a resposta à pergunta sobre MEI assumiu que a pessoa fabrica velas (do caso 05). Nas próximas rodadas, cada caso vai numa thread própria.
- O roteador de modelos quase não aparece nas respostas: o juiz do Codex notou que nenhuma resposta do 09 atribuiu nível e esforço por papel. O ganho no 09 veio do revisor independente. Item para a v0.3.
- O Gemini tende a narrar trabalho como já concluído mesmo pedindo só a primeira mensagem; a skill não corrigiu isso.
- Os textos do baseline do Codex e do Gemini foram transcritos por um agente, não gravados por script; o do Codex com skill foi conferido contra a thread.

## Limites desta rodada

- Avalia só a primeira resposta, simulada; não a execução completa.
- Uma amostra por caso, e produtor e juiz da mesma família de modelo (Sonnet). Os casos 04 e 07 tiveram margens pequenas.
- No 07 da rodada 2, a skill foi comparada com a resposta do baseline da rodada 1.
- Na rodada 1, todos os casos de cada lado rodaram na mesma conversa; isso pode contaminar casos vizinhos.

## Próximos passos sugeridos

1. Um caso por thread; incluir um chat sem ferramentas (C0).
1b. Fazer o roteador de modelos aparecer: no 09, exigir nível e esforço por parte quando o ambiente permite.
2. Repetir cada caso 3 vezes e usar um juiz de outra família de modelo.
3. Avaliar uma execução completa em 2 casos (01 e 08), com simulador de usuário.
