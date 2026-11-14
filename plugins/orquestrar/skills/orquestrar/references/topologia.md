# Topologia

Topologia é a forma do trabalho: quem faz o quê, em que ordem e quem confere. Os padrões abaixo têm nomes diferentes em cada empresa (Anthropic, OpenAI, Google, Microsoft), mas são os mesmos. Todos concordam num ponto: **comece com um agente só e aumente a complexidade quando precisar**.

## Decida nesta ordem

A primeira resposta "sim" decide. Registre a segunda melhor opção e por que perdeu.

1. Eu resolvo bem numa resposta? → **Direto.**
2. A pessoa precisa conduzir a próxima conversa com um especialista? → **Passar adiante** (entregue um resumo para ela continuar em outro lugar).
3. As partes só aparecem no caminho? → **Orquestrador e trabalhadores.**
4. Há duas ou mais partes independentes, sem mexer nos mesmos arquivos? → **Paralelo** (até dois escrevendo; leitores podem ser mais).
5. Há etapas previsíveis, uma dependendo da outra? → **Cadeia.**
6. Há várias respostas possíveis e nenhum jeito objetivo de conferir? → **Várias tentativas e comparação** (caro; só quando errar custa muito).
7. Há critério claro para melhorar? → **Produzir e revisar em loop.**
8. Quem executa pode precisar de decisões no meio? → **Executor com conselheiro.**
9. Senão → **Um executor, só o resultado volta.**

## O objetivo muda a forma

| Objetivo dominante | Ajuste |
|---|---|
| Segurança (jurídico, dinheiro, saúde, reputação) | mais gates, revisão independente, ação externa só com aprovação |
| Velocidade | paralelo nas partes independentes |
| Especialização (tarefa que cruza áreas) | um especialista por área, um dono da integração |
| Gosto ou julgamento da pessoa | etapas curtas com ela, rascunhos cedo |
| Volume repetitivo | modelo mais barato executando, mais forte só nas dúvidas |
| Continuidade (projeto de dias) | estado do projeto em arquivo, retomada por etapa |

## Aumentação ou automação

- **Aumentação:** a pessoa decide em pontos-chave e o agente faz o resto. Padrão para tudo que envolve gosto, risco ou aprendizado dela.
- **Automação:** o agente faz de ponta a ponta. Só quando o critério de pronto é objetivo e o erro é barato ou reversível.

Na dúvida, aumentação. Automação sem critério objetivo produz trabalho convincente e errado, que é o pior tipo.

## Limites que economizam

- Um produtor, uma revisão completa, uma correção, uma revisão final só do que foi corrigido.
- Se a mesma falha sobreviver à correção, mude a abordagem (outra divisão, modelo mais forte, mais contexto) em vez de revisar de novo.
- Falha de ferramenta ou permissão não justifica modelo mais forte: conserte a ferramenta.

## Exemplos

| Tarefa | Forma | Por quê |
|---|---|---|
| "Qual a diferença entre X e Y?" | Direto | uma resposta resolve |
| Pesquisa de mercado com 4 perguntas | Paralelo + síntese | perguntas independentes; um dono escreve o relatório |
| Contrato | Cadeia: rascunho, revisão independente, decisão da pessoa | erro caro, critério escrito |
| Posts de um mês | Cadeia com a pessoa: linha editorial, aprovação, produção | o gosto dela decide |
| Juntar 30 planilhas | Direto com código, check de totais | determinístico, verificável |
| TCC | Projeto em etapas, estado em arquivo, revisão por capítulo | dura semanas, a pessoa precisa aprender e decidir |
