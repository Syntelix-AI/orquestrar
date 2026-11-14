# Rodada de evals v0.3 · 2026-11-14

Skill v0.3 (commit a82d576): o plano anunciado diz, em palavras simples, quem faz o quê quando o ambiente deixa escolher modelo por parte. Mesmos 9 casos da v0.2, em três famílias de modelo, cada uma com e sem a skill, julgadas às cegas por juízes separados (Sonnet).

## Resultado

| Caso | Claude | Codex | Gemini |
|---|---|---|---|
| 01 Jurídico, plano de saúde | **skill** 15 vs 8 | **skill** 10 vs 4 | **skill** 15 vs 7 |
| 02 TCC em 6 semanas | **skill** 14 vs 8 | **skill** 8 vs 7 | **skill** 13 vs 7 |
| 03 Padaria no bairro | **skill** 15 vs 8 | **skill** 13 vs 7 | **skill** 13 vs 6 |
| 04 Planilha casa + ateliê | **skill** 15 vs 14 | **skill** 13 vs 8 | **skill** 15 vs 8 |
| 05 Posts do mês | **skill** 15 vs 9 | **skill** 13 vs 7 | **skill** 14 vs 7 |
| 06 Armadilha: MEI ou ME | **skill** 16 vs 15 | baseline 13 vs 14 | **skill** 15 vs 11 |
| 07 Armadilha: cobrança por e-mail | **skill** 15 vs 11 | **skill** 11 vs 9 | **skill** 15 vs 8 |
| 08 Juntar 30 planilhas | **skill** 14 vs 9 | **skill** 9 vs 8 | **skill** 14 vs 7 |
| 09 Roteador, 40 contratos | **skill** 15 vs 12 | **skill** 11 vs 6 | **skill** 12 vs 5 |
| **Total** | **9/9 · 134 vs 94** | **8/9 · 101 vs 70** | **9/9 · 126 vs 66** |

Modelos: Claude (subagentes desta sessão), `gpt-6.1-terra` (Codex) e `gemini-4-argon-medium` (Gemini), os dois últimos via T3 Code.

Comparado à v0.2 (Claude 8/9 + 1 empate, Codex 8/9, Gemini 8/9 + 1 empate): Claude e Gemini passam a vencer todos os casos; Codex fica igual.

## O roteador apareceu

O objetivo da v0.3 era o caso 09. Nas três famílias, a resposta com a skill disse em linguagem simples que a leitura vai para assistentes mais rápidos e que o julgamento do risco e a revisão ficam com o modelo mais forte. Nas três, os baselines ou não dividiram o trabalho por nível ou usaram jargão ("subagentes"). Em Claude, os juízes notaram que o baseline também dividiu, mas com termos técnicos; o diferencial foi linguagem simples e revisor separado. Ressalva dos juízes: nenhuma resposta nomeou o nível intermediário (consolidação) nem o esforço por papel.

## A derrota do Codex no caso 06

As duas respostas acertaram o comportamento esperado: responderam direto, sem orquestrar. A do baseline trouxe uma tabela um pouco mais completa (incluiu funcionários). Perda de 1 ponto, sem orquestração indevida. Pela regra da v0.2 ("não perder nas armadilhas") conta como falha; pela intenção da armadilha (não transformar pergunta simples em projeto), passou. Fica como ponto de atenção: em pergunta direta, a skill não deve deixar a resposta mais magra.

## Problemas de execução e como foram resolvidos

- **Contaminação entre casos (v0.2):** cada caso agora roda isolado: um subagente por caso (Claude) e uma rodada com contexto limpo por caso nas threads do T3 (`freshContext`).
- **Codex não conseguiu ler a skill em 5 casos (04, 05, 07, 08, 09):** o Windows negou a abertura de processo ("Acesso negado"). Refeitos lendo o arquivo pela ferramenta `node_repl` com `(await import('node:fs')).readFileSync(...)`. As respostas que falharam estão guardadas em `respostas/codex-skill-falhas/` e não entraram no julgamento.
- **Gemini e arquivos fora da própria pasta:** ler arquivo fora do workspace pede aprovação. A skill foi gravada dentro da pasta da thread e lida pela ferramenta de leitura, sem terminal; os 9 casos registram leitura concluída.

## Limites desta rodada

- Uma repetição por caso e por família; juízes da mesma família (Sonnet).
- Respostas de baseline do Codex e do Gemini e as 5 refeitas do Codex foram transcritas do retorno da thread, não exportadas por script; uma amostra do Gemini (08) foi conferida contra a thread e bateu.
- O Codex com skill leu a skill de dois jeitos: na primeira tentativa em 01–03 e 06, e pela `node_repl` nos outros cinco.

## Arquivos

- `cego-{claude,codex,gemini}/`: o que os juízes viram.
- `julgamento-{claude,codex,gemini}.md`: notas por critério e padrões observados.
- `chave.json`: qual letra era a skill em cada caso.
- `respostas/`: respostas originais por família e condição.

## Próximos passos sugeridos

1. Pedido simples não pode ficar mais magro com a skill: uma linha na triagem ("resposta direta continua completa").
2. Roteador: citar o nível intermediário quando houver consolidação.
3. Repetir 3 vezes por caso e usar juiz de outra família antes de chamar de estável.
