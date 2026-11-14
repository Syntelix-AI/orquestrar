# orquestrar

Uma skill para levar qualquer tarefa com IA do pedido vago a um artefato verificado, sem que você precise estudar engenharia de prompts ou de agentes.

Você diz o que quer. O agente:

1. **entende a intenção**: resultado, prazo e limites, com no máximo três perguntas, cada uma com resposta padrão;
2. **diagnostica**: testa o que o ambiente consegue fazer e escolhe a menor forma de trabalho que resolve;
3. **executa**: divide quando vale a pena e para antes de qualquer ação irreversível;
4. **verifica**: quem produz não aprova;
5. **entrega um artefato** que você controla (documento, planilha, slides, diagrama, pasta de projeto) e um recibo curto.

Perguntas simples continuam recebendo respostas simples.

## Status

v0.2 experimental: venceu o mesmo modelo sem a skill em 8 de 9 casos numa rodada às cegas ([relatório](evals/runs/2026-11-14/RELATORIO.md)). Os evals em [`evals/`](evals/) medem a primeira resposta do agente contra o mesmo modelo sem a skill.

## Instalação

A skill segue o padrão aberto [Agent Skills](https://agentskills.io): é a pasta [`skills/orquestrar/`](skills/orquestrar/).

- **Claude (app):** compacte a pasta `skills/orquestrar` em .zip e envie em Configurações → Skills.
- **Claude Code:** copie para `~/.claude/skills/orquestrar` ou `.claude/skills/orquestrar` no projeto.
- **Codex e outras ferramentas compatíveis:** copie para `~/.agents/skills/orquestrar` ou para a pasta de skills da ferramenta.
- **Via CLI:** `npx skills add <este-repo>`.

## Estrutura

```
skills/orquestrar/
  SKILL.md                 o método em 5 fases
  references/
    intencao.md            como perguntar pouco e bem
    ambiente.md            escada de capacidades C0–C4
    topologia.md           que forma de trabalho escolher
    contexto.md            o que cada parte precisa saber; estado do projeto
    verificacao.md         classes V1–V4
    modelos.md             roteador: papel → nível de modelo e esforço
    artefatos.md           formatos por uso e recibo
evals/                     casos, régua e resultados
```

## Licença

MIT.
