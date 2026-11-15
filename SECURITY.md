# Segurança

## O que este projeto instala

O plugin só carrega texto: instruções em Markdown (skills). Ele não roda servidor, não instala programas, não executa scripts e não pede acesso a contas. Os agentes que o usam continuam com as permissões e as aprovações de cada app.

## O que conta como problema de segurança

- Uma instrução da skill que leve o agente a agir sem aprovação em algo irreversível: enviar, publicar, pagar, apagar.
- Uma instrução que leve o agente a expor dados da pessoa ou de terceiros.
- Qualquer conteúdo no repositório que funcione como injeção de instruções contra o agente.
- Um arquivo de manifesto ou catálogo que faça um app instalar algo além das skills.

## Como relatar

Não abra uma issue pública. Use o [relato privado de vulnerabilidade do GitHub](https://github.com/Syntelix-AI/orquestrar/security/advisories/new) ou escreva para **contato@syntelix.ia.br**.

Conte o app e o modelo, o pedido feito ao agente, o que ele fez e o que deveria ter feito. Retire dados pessoais antes de enviar.

A resposta inicial deve chegar em até 7 dias. Correções entram numa versão nova, com o caso adicionado aos evals.

## Versões atendidas

Só a versão mais recente recebe correções.
