# orquestrar — estado do projeto

## Objetivo
v0.1: skill + 8 evals. Pronta se vencer o baseline (mesmo modelo sem skill) em pelo menos 6 de 8 casos, julgado às cegas.

## Restrições
- Projeto de diversão: não desviar das metas do ciclo.
- Repo privado; tornar público é decisão do David.

## Decisões
- 2026-11-14 Núcleo só em texto, padrão Agent Skills; embalagens de plugin depois da v0.1.
- 2026-11-14 Evals escritos por agente que não viu a skill (requisitos → testes).

- 2026-11-14 Roteador de modelos por papel → nível + esforço, com tabela de modelos datada e separada (pedido do David).
- 2026-11-14 Reparo v0.2: preparar de verdade o que é reversível antes de pedir aprovação.

## Feito
- Skill v0.2 (SKILL.md + 7 referências), README, LICENSE.
- 9 evals; rodada às cegas: v0.1 6/8 (reprovada no caso 07), v0.2 8/9 (aprovada). Ver evals/runs/2026-11-14/RELATORIO.md.

- Portabilidade: Codex 8/9 e Gemini 8/9 + 1 empate (rodada 3 via T3).

## Próximo passo
Criar o repositório privado vazio e fazer o push.

## Em aberto
- Nome definitivo do projeto.
- Repetições por caso e juiz de outra família de modelo.
- Embalagens de plugin (Agent Plugins 1.0 e Claude Code).
