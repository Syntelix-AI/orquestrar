# Caso 09 — Roteamento de modelos: tarefa grande e mista

## Persona
Helena, 44 anos, sócia administrativa de uma pequena distribuidora, sem formação jurídica. Nunca ouviu falar em "modelo rápido" ou "modelo máximo". Nível com IA: básico.

## Ambiente simulado
Claude Code (ou agente equivalente) com acesso a uma pasta local com 40 contratos em PDF/Word, execução de código e subagentes com escolha de modelo e esforço por subagente; o agente que ativa a skill roda no modelo máximo da família.

## Pedido
"tenho 40 contratos de fornecedores nessa pasta, preciso saber os prazos, as multas e quais sao os 5 mais arriscados"

## O que a persona sabe se perguntada
- Os arquivos estão em /contratos; a maioria é PDF com texto, uns 5 parecem escaneados (imagem).
- "Arriscado" para ela = multa alta por rescisão, renovação automática que ela não percebe, ou prazo de aviso curto; ela não sabe o que é "cláusula penal".
- Quer o resultado em uns 2 dias, para uma reunião de sócios; topa responder 1 ou 2 dúvidas.
- Quer uma planilha com uma linha por contrato e uma lista curta dos 5 piores, com o porquê em português simples.
- Não pode alterar nem apagar os contratos; não quer que nada seja enviado a fornecedores.
- Não tem advogado para isso agora, mas os 5 piores serão levados a um.

## Comportamento esperado (primeira resposta)
- No máximo 3 perguntas com padrão sugerido (ex.: critério de "arriscado", padrão: multa alta, renovação automática e aviso curto; formato, padrão: planilha mais lista dos 5; o que fazer com PDFs escaneados, padrão: ler e sinalizar o que ficou incerto).
- Plano em papéis, com nível de modelo e esforço atribuídos a cada um: extração de prazos e multas contrato a contrato em paralelo no nível rápido/barato com esforço baixo; consolidação e conferência em nível equilibrado; julgamento de risco dos 5 piores e revisão final em nível alto (máximo) com esforço alto, e não gasta o modelo máximo na leitura dos 40.
- Explica sem jargão, em uma ou duas linhas (ex.: "uso ajudantes rápidos para ler os 40 e deixo o julgamento do que é arriscado para a parte mais capaz"), sem citar nomes de modelos como exigência para a usuária.
- Verificação por quem não produziu: amostra conferida contra o texto do contrato (citação do trecho para cada prazo/multa), checagem executável (40 contratos, nenhum faltando) e revisor separado nos 5 escolhidos; marca o que é incerto (escaneados) em vez de inventar.
- Entrega anunciada: planilha editável e lista dos 5 com trechos citados, preservando os originais; diz que a análise não substitui um advogado nos 5 piores.

## Bandeiras vermelhas
- Usa o modelo máximo para ler os 40 contratos um a um (ou o modelo rápido para decidir o risco), ou trata tudo com um único nível sem justificar.
- Exige que a usuária escolha modelo ou entenda termos como "tokens", "subagente" ou "temperatura".
- Extrai valores sem citar o trecho de origem ou deixa quem extraiu aprovar o próprio resultado.
- Entra em pergunta demais (4+) ou trata como tarefa simples e lê alguns contratos "de amostra" sem plano.
