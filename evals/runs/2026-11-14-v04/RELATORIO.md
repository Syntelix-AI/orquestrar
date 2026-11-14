# Rodada de evals v0.4 · 2026-11-14

Dois ajustes sobre a v0.3:

1. **Triagem:** responder direto não é responder pela metade. A resposta direta traz os pontos que decidem a questão (uma tabela curta, se comparar coisas) e, quando valores ou regras mudam, diz onde conferir.
2. **Roteador:** o plano cita o nível intermediário quando há consolidação e diz se a revisão é feita por outro assistente, não por quem produziu.

Rodada enxuta por decisão do David: o volume foi para o Codex, e o Claude rodou só os dois casos que mudaram. Um juiz Sonnet julgou 17 pares às cegas, em ordem sorteada; para as respostas do Codex, é um juiz de outra família.

## Resultado

| Par | Repetições | Vencedor | Pontos (skill vs baseline) |
|---|---|---|---|
| Codex 06 · MEI ou ME (armadilha) | 3 | **skill** 3 de 3 | 16 vs 15 nas três |
| Codex 07 · cobrança por e-mail (armadilha) | 3 | **skill** 3 de 3 | 11 vs 8 nas três |
| Codex 09 · roteador, 40 contratos | 3 | **skill** 3 de 3 | 11 vs 7 nas três |
| Codex 01, 02, 03, 04, 05, 08 (regressão) | 1 cada | **skill** 6 de 6 | 69 vs 41 |
| Claude 06 | 1 | empate | 15 vs 15 |
| Claude 09 | 1 | **skill** | 15 vs 11 |

**16 vitórias, 1 empate e nenhuma derrota em 17 pares.** O Codex, que na v0.3 perdeu o 06 por 1 ponto, venceu as três repetições. Os casos que não mudaram continuam vencendo.

## O que os ajustes fizeram

- **Caso 06:** com a skill, o Codex passou a responder com tabela e a apontar onde conferir (Portal do Empreendedor, Portal do Simples Nacional). Sem a skill, o aviso era genérico ("vale confirmar"). A margem é pequena (1 ponto), mas se repetiu nas três rodadas. No Claude, as duas respostas trouxeram os mesmos números de memória com aviso de onde conferir: empate.
- **Caso 09:** em todas as respostas com a skill (3 do Codex e 1 do Claude), o plano disse em linguagem simples: assistentes rápidos leem, um modelo intermediário consolida, o mais forte julga, e outro assistente revisa. Sem a skill, o Codex lê tudo sozinho, e o Claude usa jargão e revisa o próprio ranking.

## Limites

- Juiz único, da família Claude. Para os dois pares do Claude, juiz e respondente são da mesma família.
- As repetições do Codex receberam pontuações idênticas, porque os textos de cada condição saíram muito parecidos entre si. Isso indica estabilidade do modelo, não três medidas independentes de qualidade.
- A primeira repetição do baseline de 06, 07 e 09 é a da v0.3, gerada com um prompt quase igual (sem a frase "nem descreva trabalho como já concluído"). As outras duas usam o prompt atual.
- As 6 repetições novas do baseline do Codex foram transcritas do retorno da thread. As respostas com skill foram extraídas por script.
- Um envio do caso 01 com texto errado foi descartado; vale o reenvio com o texto exato.
- Fraqueza comum aos dois lados, apontada pelo juiz: quase nenhuma resposta trata prazo e engajamento nem declara restrições (originais intactos, o que não tocar).

## Arquivos

`cego/` (o que o juiz viu), `julgamento.md`, `chave.json`, `respostas/` e `prompts/` (prompts das rodadas do Claude).
