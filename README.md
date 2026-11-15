<div align="center">

# orquestrar

**Do pedido vago ao trabalho entregue e conferido.**

Um plugin para Claude, ChatGPT, Codex e outros agentes de IA que conduz qualquer tarefa com método: entende o que você quer, testa o que a ferramenta consegue fazer, escolhe a menor forma de trabalho que resolve, confere antes de entregar e pede sua aprovação antes de qualquer ação que não dá para desfazer.

[Site e instalação](https://cafesemcafeina.github.io/orquestrar/) · [English](README.en.md) · [Evals](evals/) · [Como contribuir](CONTRIBUTING.md)

![Licença MIT](https://img.shields.io/badge/licen%C3%A7a-MIT-673981)
![Versão 0.4.0](https://img.shields.io/badge/vers%C3%A3o-0.4.0-673981)
![Agent Skills](https://img.shields.io/badge/padr%C3%A3o-Agent%20Skills-3f817c)
![Agent Plugins 1.0](https://img.shields.io/badge/padr%C3%A3o-Agent%20Plugins%201.0-3f817c)

</div>

---

## Por que existe

Quem usa IA no dia a dia costuma ouvir que precisa aprender a escrever prompts, montar agentes e dividir tarefas. O orquestrar inverte isso: você pede do seu jeito, e o método fica com o agente.

Você continua decidindo **o que** quer. O agente decide **como** fazer e explica o porquê em uma linha.

## Como funciona

| Fase | O que o agente faz | O que muda para você |
|---|---|---|
| **0 · Triagem** | Decide se a tarefa pede método ou uma resposta direta. | Pergunta simples continua recebendo resposta simples e completa. |
| **1 · Intenção** | Entende resultado, prazo e limites. Pergunta no máximo três coisas, cada uma com uma resposta padrão. | Você pode responder só "pode seguir". |
| **2 · Diagnóstico** | Testa o que a ferramenta consegue (arquivos, web, conectores, assistentes paralelos) e escolhe a menor forma de trabalho que resolve. | Nada de prometer o que a ferramenta não faz. |
| **3 · Execução** | Divide o trabalho quando vale a pena e prepara de verdade tudo o que é reversível. | Antes de enviar, publicar ou apagar, ele para e pede sua aprovação. |
| **4 · Verificação** | Confere números, fontes e formatos; quem produz não aprova o próprio trabalho. | Você recebe o que foi conferido e o que ficou em aberto. |
| **5 · Entrega** | Entrega um artefato (documento, planilha, slides, pasta de projeto) e um recibo curto. | Algo que você usa, não um bloco de texto no chat. |

Quando a ferramenta deixa escolher modelos, o plano diz em palavras simples quem faz o quê: assistentes mais rápidos leem, um modelo intermediário consolida, o mais forte decide e outro assistente revisa.

## Resultados

O orquestrar é testado contra o mesmo modelo sem o plugin, às cegas: um juiz recebe as duas respostas sem saber qual é qual. Os casos incluem armadilhas, como uma pergunta simples que não deve virar projeto e um pedido de envio de e-mail em massa que não deve ser executado sem aprovação.

| Rodada | Família de modelos | Vitórias | Pontos (com × sem) |
|---|---|---|---|
| v0.3 | Claude | 9 de 9 | 134 × 94 |
| v0.3 | Codex (OpenAI) | 8 de 9 | 101 × 70 |
| v0.3 | Gemini (Google) | 9 de 9 | 126 × 66 |
| v0.4 | Claude e Codex, com repetições | 16 de 17, 1 empate | [relatório](evals/runs/2026-11-14-v04/RELATORIO.md) |

**Limites, para ler os números com cuidado:** os testes medem a primeira resposta do agente, não a tarefa inteira; o juiz é um modelo de linguagem; os 9 casos foram escritos para o projeto, não colhidos de usuários reais. Os relatórios completos, as respostas brutas e a régua estão em [`evals/`](evals/).

## Instalação

O passo a passo de cada app está no [site](https://cafesemcafeina.github.io/orquestrar/).

**Claude (web e desktop):** Customize → Plugins → Personal plugins → **+** → Add marketplace → `CafeSemCafeina/orquestrar`. Depois instale o `orquestrar`.

**ChatGPT desktop e Codex:** Plugins → Adicionar marketplace → origem `CafeSemCafeina/orquestrar`, referência `main`. Depois instale o `orquestrar`.

**Claude Code:**

```
/plugin marketplace add CafeSemCafeina/orquestrar
/plugin install orquestrar@orquestrar
```

**Codex CLI:**

```
codex plugin marketplace add CafeSemCafeina/orquestrar
codex plugin add orquestrar@orquestrar
```

**Só a skill, por upload:** baixe [`orquestrar-skill.zip`](https://cafesemcafeina.github.io/orquestrar/download/orquestrar-skill.zip) e envie na tela de skills do Claude ou do ChatGPT.

## Packs por profissão

O orquestrar é o método geral. Os **packs** trazem o que cada área tem de próprio: as perguntas certas para entender o pedido, os artefatos típicos, as fontes para conferir e os pontos em que é preciso parar e pedir aprovação.

| Pack | Estado |
|---|---|
| Jurídico | procurando profissionais |
| Pesquisa acadêmica | procurando profissionais |
| Estudos | procurando profissionais |
| Organização pessoal e produtividade | procurando profissionais |
| A sua área | [proponha](https://github.com/CafeSemCafeina/orquestrar/issues/new?template=relato-profissional.yml) |

Construir packs é o principal pedido de contribuição deste projeto, e começa sem código: [conte como você trabalha com IA hoje](https://github.com/CafeSemCafeina/orquestrar/issues/new?template=relato-profissional.yml). Cada relato vira casos de teste e orienta o pack da sua área. Veja [PACKS.md](PACKS.md).

## Estrutura do repositório

```
.claude-plugin/marketplace.json     catálogo para Claude (o Codex também lê)
.agents/plugins/marketplace.json    catálogo para Codex e ChatGPT
plugins/orquestrar/                 o plugin
  plugin.json                       manifesto Agent Plugins 1.0
  .claude-plugin/plugin.json        manifesto do Claude Code
  skills/orquestrar/
    SKILL.md                        o método em 5 fases
    references/                     intenção, ambiente, topologia, contexto,
                                    verificação, modelos e artefatos
templates/pack/                     ponto de partida para um pack novo
evals/                              casos, régua e relatórios das rodadas
docs/                               site (GitHub Pages)
scripts/empacotar.sh                gera o .zip da skill
```

O plugin só carrega skills: não roda servidor, não instala programas e não pede acesso a contas.

## Contribuir

Leia o [CONTRIBUTING.md](CONTRIBUTING.md). Em resumo: relatos de uso real valem mais que opiniões, e toda mudança na skill precisa vencer, ou ao menos não perder, para a versão anterior nos evals.

Este projeto segue um [código de conduta](CODE_OF_CONDUCT.md). Para falhas de segurança, veja [SECURITY.md](SECURITY.md). O histórico de versões está no [CHANGELOG.md](CHANGELOG.md).

## Licença

[MIT](LICENSE). Feito por David Fiocchi, da [Syntelix](https://syntelix.ia.br).
