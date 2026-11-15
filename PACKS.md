# Packs por profissão

O orquestrar é um método geral. Ele sabe conduzir uma tarefa, mas não sabe, por exemplo, que um prazo processual não pode ser estimado, que um orientador espera ver a pergunta de pesquisa antes do método ou que uma lista de tarefas pessoal precisa caber na semana real de quem a usa.

Um **pack** é um plugin pequeno que ensina isso ao agente, área por área. Ele não repete o método: soma ao método o que é próprio da profissão.

## O que um pack contém

Cada pack responde às mesmas cinco perguntas que o método faz, só que para a sua área:

| Pergunta do método | O que o pack traz |
|---|---|
| **Intenção:** o que perguntar? | As 3 perguntas que mais mudam o resultado nessa área, cada uma com uma resposta padrão segura. |
| **Diagnóstico:** o que testar? | Ferramentas e fontes típicas da área (bases de jurisprudência, repositórios acadêmicos, agenda, planilha de estudos). |
| **Execução:** onde parar? | Os pontos de autoridade da área: o que nunca se envia, protocola, publica ou apaga sem aprovação. |
| **Verificação:** como conferir? | As fontes primárias e os erros clássicos da área (citação inventada, artigo revogado, data errada). |
| **Entrega:** que artefato? | Os formatos que a profissão usa de verdade (petição, fichamento, cronograma, plano semanal) e o recibo esperado. |

E, o mais importante, **casos de eval tirados de profissionais reais**: pedidos que eles fazem à IA, com o que esperam e o que os incomoda.

## Estrutura

```
plugins/orquestrar-<area>/
  plugin.json                     manifesto Agent Plugins 1.0
  .claude-plugin/plugin.json      manifesto do Claude Code
  skills/orquestrar-<area>/
    SKILL.md                      quando usar e o que muda no método
    references/                   intenção, fontes, autoridade, artefatos da área
evals/cases/<area>/               casos de profissionais reais
```

O ponto de partida está em [`templates/pack/`](templates/pack/). Cada pack entra no catálogo como um plugin separado, para que a pessoa instale só o que usa.

## Como um pack nasce

1. **Relatos.** Profissionais contam como trabalham com IA hoje: [abra um relato](https://github.com/CafeSemCafeina/orquestrar/issues/new?template=relato-profissional.yml). Não precisa saber programar.
2. **Casos.** Os relatos viram de 5 a 10 casos de eval da área, no formato de [`evals/cases/`](evals/cases/), incluindo ao menos uma armadilha (um pedido simples que não deve virar projeto e uma ação que exige aprovação).
3. **Rascunho.** Alguém escreve o pack a partir do modelo, preferindo mostrar exemplos concretos a listar regras.
4. **Teste às cegas.** O pack é comparado ao orquestrar sem pack nos casos da área. Entra no catálogo se vencer na maioria e não perder nas armadilhas.
5. **Revisão de quem é da área.** Pelo menos um profissional da área lê o pack antes da primeira versão.

## Packs em construção

| Pack | Estado | Discussão |
|---|---|---|
| Jurídico | procurando profissionais | [relatos](https://github.com/CafeSemCafeina/orquestrar/issues?q=label%3Apack%3Ajuridico) |
| Pesquisa acadêmica | procurando profissionais | [relatos](https://github.com/CafeSemCafeina/orquestrar/issues?q=label%3Apack%3Apesquisa) |
| Estudos | procurando profissionais | [relatos](https://github.com/CafeSemCafeina/orquestrar/issues?q=label%3Apack%3Aestudos) |
| Organização pessoal e produtividade | procurando profissionais | [relatos](https://github.com/CafeSemCafeina/orquestrar/issues?q=label%3Apack%3Aprodutividade) |

## O que um pack não faz

- Não substitui o profissional nem dá parecer: o pack ensina o agente a trabalhar melhor com a pessoa, e as decisões continuam com ela.
- Não guarda dados de clientes, pacientes ou alunos. Casos de eval usam situações simuladas, sem nomes reais.
- Não traz servidores, programas ou acesso a contas. Se uma área precisar de uma integração, isso é discutido numa issue antes.
