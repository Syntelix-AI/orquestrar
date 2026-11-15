# Changelog

Todas as mudanças relevantes do orquestrar. O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/) e as versões seguem [versionamento semântico](https://semver.org/lang/pt-BR/).

## [Não lançado]

### Adicionado
- Repositório preparado para ser público: README em português e inglês, guia de contribuição, código de conduta, política de segurança, modelos de issue e de pull request.
- Site no GitHub Pages com instalação por app, explicação do método e resultados dos evals.
- Especificação de packs por profissão ([PACKS.md](PACKS.md)) e modelo em `templates/pack/`.

## [0.4.0] - 2026-11-14

### Adicionado
- Empacotamento como plugin: Claude Code, Agent Plugins 1.0 (Codex, ChatGPT e outros) e .zip para upload no app.
- Catálogos para Claude Code (`.claude-plugin/marketplace.json`) e Codex (`.agents/plugins/marketplace.json`).

### Mudado
- Resposta direta continua completa: os pontos que decidem a questão e, quando valores ou regras mudam, onde conferir.
- O roteador de modelos cita o nível intermediário quando há consolidação e diz quando a revisão é feita por outro assistente.

### Resultado
- 17 pares às cegas (Claude e Codex): 16 vitórias, 1 empate, nenhuma derrota.

## [0.3.0] - 2026-11-14

### Mudado
- O plano anuncia em linguagem simples quem faz o quê por nível de modelo.

### Resultado
- Às cegas, com casos isolados: Claude 9/9, Codex 8/9, Gemini 9/9.

## [0.2.0] - 2026-11-14

### Adicionado
- Roteador de modelos por papel (`references/modelos.md`) e o caso de eval 09.

### Mudado
- Preparar é fazer de verdade tudo o que é reversível antes de pedir aprovação, em vez de descrever o processo.

### Resultado
- Claude 8/9 e 1 empate; portabilidade: Codex 8/9, Gemini 8/9 e 1 empate.

## [0.1.0] - 2026-11-14

### Adicionado
- Skill `orquestrar` em 5 fases, com 7 referências.
- 8 casos de eval, régua e protocolo de julgamento às cegas.

### Resultado
- Claude 6/8, com derrota na armadilha 07 (corrigida na 0.2.0).
