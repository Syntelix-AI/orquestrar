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

v0.4 experimental: numa rodada às cegas, a v0.3 venceu o mesmo modelo sem a skill em 9 de 9 casos no Claude, 8 de 9 no Codex e 9 de 9 no Gemini ([relatório](evals/runs/2026-11-14-v03/RELATORIO.md)). A v0.4 ajustou a resposta direta e o roteador e não perdeu nenhum dos 17 pares testados (16 vitórias e 1 empate; [relatório](evals/runs/2026-11-14-v04/RELATORIO.md)). Os evals em [`evals/`](evals/) medem a primeira resposta do agente contra o mesmo modelo sem a skill.

## Instalação

O mesmo conteúdo sai em três embalagens. A skill fica num lugar só, [`plugins/orquestrar/skills/orquestrar/`](plugins/orquestrar/skills/orquestrar/), no padrão aberto [Agent Skills](https://agentskills.io).

**Claude Code (plugin):**

```
/plugin marketplace add CafeSemCafeina/orquestrar
/plugin install orquestrar@orquestrar
```

**Codex, ChatGPT e outros clientes do padrão Agent Plugins 1.0:** o plugin portátil é a pasta [`plugins/orquestrar/`](plugins/orquestrar/), com `plugin.json` na raiz. O catálogo para o Codex está em [`.agents/plugins/marketplace.json`](.agents/plugins/marketplace.json):

```
codex plugin marketplace add CafeSemCafeina/orquestrar
```

Depois instale pelo diretório de plugins do Codex ou do app do ChatGPT.

**App do Claude ou do ChatGPT (só a skill):** rode `./scripts/empacotar.sh`, que gera `dist/orquestrar-skill.zip`, e envie o arquivo na tela de skills do app.

**Copiando a pasta:** copie `plugins/orquestrar/skills/orquestrar` para `~/.claude/skills/` (Claude Code) ou `~/.agents/skills/` (Codex e compatíveis).

O repositório é privado. Enquanto for, quem instala precisa ter acesso de leitura a ele no GitHub.

## Estrutura

```
.claude-plugin/marketplace.json     catálogo do Claude Code (o Codex também lê)
.agents/plugins/marketplace.json    catálogo do Codex
plugins/orquestrar/
  plugin.json                       manifesto Agent Plugins 1.0
  .claude-plugin/plugin.json        manifesto do Claude Code
  skills/orquestrar/
    SKILL.md                        o método em 5 fases
    references/
      intencao.md                   como perguntar pouco e bem
      ambiente.md                   escada de capacidades C0–C4
      topologia.md                  que forma de trabalho escolher
      contexto.md                   o que cada parte precisa saber; estado do projeto
      verificacao.md                classes V1–V4
      modelos.md                    roteador: papel → nível de modelo e esforço
      artefatos.md                  formatos por uso e recibo
scripts/empacotar.sh                gera o .zip da skill
evals/                              casos, régua e resultados
```

Sem servidor MCP, hooks ou comandos: o plugin só carrega a skill. Ela funciona sozinha em qualquer ambiente, e coisas a mais só entram quando houver uma necessidade concreta.

## Licença

MIT.
