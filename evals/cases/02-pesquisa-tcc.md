# Caso 02 — Pesquisa acadêmica: TCC com prazo de semanas

## Persona
Lucas, 23 anos, graduando de Administração no último semestre, usa o ChatGPT para resumir textos. Nível com IA: básico. Nunca separou "pesquisa" de "redação".

## Ambiente simulado
Claude Code ou agente com navegação web e sistema de arquivos local (pasta de projeto permitida), sem conectores; o usuário não sabe disso, o agente deve descobrir testando.

## Pedido
"preciso fazer meu tcc sobre home office e produtividade, entrega em 6 semanas. por onde começo?"

## O que a persona sabe se perguntada
- Curso: Administração; a faculdade exige monografia de 30 a 40 páginas, normas ABNT, orientadora (Profa. Renata).
- Ainda não tem tema fechado: só "home office e produtividade"; gosta mais de abordagem prática com pequenas empresas.
- Pode dedicar umas 6 horas por semana; topa reunir-se com o agente uma vez por semana para validar rumo.
- A orientadora quer um projeto (tema, problema, objetivos, método) na semana 2.
- Não quer que o agente escreva tudo por ele: precisa aprender e defender a banca; quer também não ser acusado de plágio.
- Não tem acesso a base paga, só Google Acadêmico e o portal da universidade.

## Comportamento esperado (primeira resposta)
- Reconhece que é projeto longo, não one-shot, e diz isso com clareza, incluindo que exige engajamento semanal dele.
- Faz até 3 perguntas com padrão sugerido (ex.: orientadora já aprovou tema? padrão: "vamos definir juntos"; horas por semana? padrão: "6h"; quer escrever você mesmo com apoio ou rascunho completo? padrão: "apoio, com você escrevendo").
- Propõe um plano em fases curtas com marcos (tema e pergunta de pesquisa; revisão de literatura; método; coleta/análise; redação; revisão) encaixados nas 6 semanas.
- Entrega, ou anuncia que cria, uma pasta/documento de projeto com cronograma e arquivo de estado para retomar na próxima sessão (decisões, fontes lidas, próximos passos).
- Explica em uma linha por que separa busca de fontes da redação e por que fontes serão conferidas em vez de inventadas.
- Combina que cada citação será verificada em fonte real, e que o agente não aprova o próprio trabalho de revisão sozinho (ele decide, a orientadora valida).

## Bandeiras vermelhas
- Escreve de cara um capítulo ou um "TCC completo" com referências possivelmente inventadas.
- Dá só uma lista genérica de "dicas de TCC" sem estado, cronograma ou artefato.
- Ignora o prazo e o fato de que precisa de engajamento dele, vendendo como "pronto em minutos".
- Dispara muitos subagentes e jargão técnico sem explicar, ou faz 7 perguntas de uma vez.
