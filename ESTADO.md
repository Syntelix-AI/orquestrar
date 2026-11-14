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
- 2026-11-14 v0.3: o plano diz em palavras simples quem faz o quê quando dá para escolher modelo por parte.
- 2026-11-14 Evals rodam um caso por vez, com contexto limpo (sem contaminação entre casos).
- 2026-11-14 v0.4: resposta direta completa (com onde conferir); roteador cita o nível intermediário e o revisor separado.
- 2026-11-14 Empacotamento: uma skill, três embalagens (plugin Claude Code, Agent Plugins 1.0 com catálogo do Codex, .zip). Sem MCP, hooks nem comandos.
- 2026-11-14 Evals em volume vão para o Codex (T3); o Claude roda só o enxuto (pedido do David, custo).

## Feito
- Skill v0.4 (SKILL.md + 7 referências), README, LICENSE.
- 9 evals; v0.1 6/8 (reprovada no 07), v0.2 8/9 (aprovada). Ver evals/runs/2026-11-14/RELATORIO.md.
- Portabilidade v0.2: Codex 8/9, Gemini 8/9 + 1 empate.
- v0.3 às cegas: Claude 9/9 (134 vs 94), Codex 8/9 (101 vs 70; perdeu o 06 por 1 ponto, sem orquestrar), Gemini 9/9 (126 vs 66). Roteador apareceu em linguagem simples nas três. Ver evals/runs/2026-11-14-v03/RELATORIO.md.
- v0.4: 17 pares às cegas, 16 vitórias e 1 empate, nenhuma derrota; Codex venceu 06 nas 3 repetições. Ver evals/runs/2026-11-14-v04/RELATORIO.md.
- Plugin empacotado em plugins/orquestrar/: `claude plugin validate` passou (plugin e catálogo) e a instalação local pelo catálogo funcionou. Codex CLI 0.169.0 no PC do David: `codex plugin marketplace add CafeSemCafeina/orquestrar` + `codex plugin add orquestrar@orquestrar` instalaram e habilitaram sem avisos de formato, e `codex exec` reconhece a skill como `orquestrar:orquestrar` (descrição aparece truncada). Não testado: sessão real do Claude Code carregando a skill.
- Repositório privado CafeSemCafeina/orquestrar criado e atualizado.

## Próximo passo
Testar numa sessão real do Claude Code. Avaliar se a descrição deve começar pelo gatilho, já que o Codex mostra só o começo dela. Tornar o repositório público é decisão do David.

## Em aberto
- Nome definitivo do projeto.
- Repetições por caso e juiz de outra família de modelo.
- Ícone para listagem em diretórios (o validador avisa que falta).
- MCP: não agora; reavaliar quando houver embalagem de plugin.
