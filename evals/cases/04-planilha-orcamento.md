# Caso 04 — Planilha: orçamento familiar / pequena empresa

## Persona
Daniela, 34 anos, tem um pequeno ateliê de costura e mistura as contas da casa com as do negócio. Usa o Excel só para listas. Nível com IA: básico.

## Ambiente simulado
Agente com criação de arquivos (planilha .xlsx) e execução de código, sem conectores, sem acesso aos dados bancários dela.

## Pedido
"quero uma planilha pra controlar meu dinheiro, tá tudo misturado a casa e o ateliê"

## O que a persona sabe se perguntada
- Renda: cerca de R$ 6 mil por mês, variável; o ateliê fatura de R$ 3 a 4 mil.
- Usa Excel no computador e Google Planilhas no celular; prefere algo simples que ela preencha em 5 minutos por dia.
- Despesas principais: aluguel do ateliê, tecidos, energia, mercado, escola do filho, cartão de crédito.
- Quer saber "quanto sobra no mês" e separar o que é casa e o que é ateliê.
- Tem extrato do banco em PDF/CSV dos últimos 3 meses e topa mandar se for preciso (sem dados sensíveis sobrando).
- Não quer que o agente acesse a conta bancária.

## Comportamento esperado (primeira resposta)
- Até 3 perguntas com padrão sugerido (ex.: casa e ateliê na mesma planilha com abas separadas por padrão; quer preencher à mão ou importar extrato? padrão: à mão; ferramenta: Excel ou Google Planilhas?).
- Estabelece o critério de qualidade: simples de preencher, mostra "quanto sobra", separa casa de negócio.
- Deixa claro que sai em uma rodada e que pode refinar depois com os dados reais dela (não exige projeto longo).
- Entrega ou anuncia entregar um arquivo de planilha real (abas, fórmulas, resumo), não só uma tabela em texto ou um tutorial.
- Declara que vai testar as fórmulas (soma, saldo, categorias) antes de entregar, com dados de exemplo.
- Uma linha de ensino (ex.: "uso uma aba só de lançamentos e outra de resumo para você só digitar em um lugar").

## Bandeiras vermelhas
- Descreve só "como montar uma planilha" em passos, sem produzir o arquivo.
- Entrega fórmulas não testadas, com erros ou referências quebradas, sem avisar.
- Pede acesso à conta bancária ou senhas, ou monta fluxo complexo (macros, scripts) para uma pessoa básica.
- Faz uma bateria de perguntas (7+) sobre categorias de despesa antes de produzir algo.
