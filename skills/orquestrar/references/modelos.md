# Modelos e esforço

A pessoa não precisa saber qual modelo é bom para quê. Você precisa. Este arquivo é um roteador simples: o **papel** de cada parte do trabalho define um **nível** de modelo e um **esforço**; uma tabela datada traduz o nível para os modelos atuais.

Ordem das decisões: forma do trabalho → quem executa → nível e esforço. O modelo é a última escolha, nunca a primeira.

## 1. Quem é você

Antes de distribuir trabalho, saiba quem está conduzindo:

- Procure no seu próprio contexto o nome do modelo que você é (o ambiente costuma informar). Se não souber, trate como **equilibrado** e diga "desconhecido" se perguntarem.
- Se você é **rápido**: conduza, mas mande decisões difíceis (arquitetura, julgamento ambíguo, revisão de alto risco) para um nível acima quando o ambiente permitir; quando não permitir, deixe essas decisões explícitas para a pessoa.
- Se você é **máximo**: não gaste seu nível em volume. Delegue extração, coleta e conversões para níveis abaixo e guarde-se para síntese, decisão e integração.

## 2. O que o ambiente deixa escolher

Teste, como no diagnóstico de ambiente:

- **Escolhe modelo e esforço por subagente:** aplique a tabela do item 3.
- **Escolhe só o modelo da conversa:** recomende à pessoa trocar no seletor quando valer muito a pena ("para esta revisão de contrato, vale usar o modelo mais forte"). Não insista.
- **Não escolhe nada:** compense com forma de trabalho (etapas menores, critérios mais explícitos, verificação mais forte).

## 3. Papel → nível e esforço

| Papel do nó | Nível | Esforço |
|---|---|---|
| Triagem e roteamento | rápido | baixo |
| Extração, conversão, mapeamento, varredura de arquivos | rápido | baixo |
| Coleta de pesquisa numa frente | rápido ou equilibrado | médio |
| Revisão com check executável (V1) | rápido | baixo |
| Redação, síntese, relatório | equilibrado | médio |
| Código delimitado com testes | equilibrado | médio |
| Revisão por fonte ou critérios (V2, V3) | equilibrado | alto |
| Conversa com a pessoa, condução | o modelo já ativo | o padrão do ambiente |
| Planejamento, arquitetura, decisão ambígua | máximo | alto |
| Código complexo, depuração difícil | máximo | alto |
| Revisão final de alto custo de erro (jurídico, dinheiro, segurança) | máximo | alto |

Esforço baixo serve para trabalho mecânico com verificação; médio é o normal; alto é para ambiguidade, evidência conflitante ou erro caro.

## 4. Quando subir

- Primeiro classifique a falha. Falha de ferramenta, permissão, rede ou instrução mal escrita **não** justifica modelo mais forte: conserte a causa.
- Resultado fraco por qualidade: uma correção no mesmo nível. Se o mesmo problema voltar, suba o **produtor** de nível (ou melhore o pacote), em vez de pagar mais revisões.
- O revisor não precisa ser mais forte que o produtor: precisa ser capaz de aplicar os critérios. Check executável pode ser revisado pelo nível rápido.

## 5. Tradução de níveis (exemplos, conferidos em nov/2026)

Nomes mudam rápido. Confira o que o ambiente oferece antes de usar; esta tabela é ponto de partida, não verdade.

| Fornecedor | Rápido | Equilibrado | Máximo |
|---|---|---|---|
| Anthropic (Claude) | Haiku | Sonnet | Opus |
| OpenAI (Codex, ChatGPT) | Luna | Terra | Sol |
| Google (Gemini) | Flash | confira no ambiente | confira no ambiente |

Quando um fornecedor tiver um nível acima do "máximo" com restrições extras de uso, trate-o como fora da escada: use só se a pessoa pedir.
