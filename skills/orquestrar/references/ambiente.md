# Ambiente

Modelos erram com frequência sobre as próprias ferramentas. Por isso o diagnóstico é feito **testando**, e classificado por **capacidade**, não pelo nome do produto. Nomes e recursos mudam todo mês; a escada de capacidades continua valendo.

## Como testar em segundos

1. Olhe a lista de ferramentas que você recebeu. Ferramentas carregadas sob demanda contam: procure por elas.
2. Para cada capacidade que a tarefa precisa, faça a chamada mais barata possível: listar uma pasta, rodar `echo`, uma busca curta, listar conectores.
3. Se a chamada falhar, trate a capacidade como ausente e siga no nível de baixo. Não tente contornar bloqueios de rede ou permissão.

Não narre esse teste para a pessoa. Mencione o resultado só quando ele muda o que ela vai receber ("aqui não consigo acessar seu e-mail; se você colar as mensagens, eu sigo").

## A escada

| Nível | Sinais | O que muda no trabalho |
|---|---|---|
| **C0** só conversa | nenhuma ferramenta além de responder | etapas curtas, a pessoa cola o material, verificação por releitura separada contra critérios escritos antes |
| **C1** arquivos e código | ler e escrever arquivos, rodar Python ou Node | números e formatos conferidos por código; artefatos como arquivos de verdade |
| **C2** mundo externo | busca na web, conectores (e-mail, drive, agenda, CRM), navegador | fontes vivas citadas; dados da própria pessoa; ações externas exigem gate |
| **C3** subagentes | ferramenta para criar outra instância com contexto próprio | trabalho em paralelo; revisor independente de verdade |
| **C4** tempo | tarefas agendadas, segundo plano, execução longa, outras ferramentas de agente | loops contínuos, trabalho que dura dias, retomada automática |

Os níveis se acumulam: C3 normalmente tem C1 e C2, mas confirme cada um.

## Exemplos em ambientes comuns

São exemplos para reconhecer sinais, não garantias. Confirme sempre testando.

- **Chat no celular, sem extras:** costuma ser C0. Às vezes tem busca na web (C2 parcial).
- **Apps de chat com criação de arquivos e execução de código:** C1, frequentemente C2 com busca e conectores.
- **Agentes de terminal ou IDE (ferramentas de código):** C1 garantido, quase sempre C3 com subagentes, às vezes C4 com tarefas em segundo plano.
- **Ambientes de trabalho com conectores corporativos:** C2 forte (documentos, e-mail, planilhas da pessoa); verifique permissões de escrita.

## Quando o ambiente não basta

Diga em uma linha o que falta e o que isso muda, e ofereça o caminho: "aqui não consigo gerar a planilha como arquivo; te passo a tabela pronta para colar e as fórmulas" ou "se você abrir isto num ambiente com navegador, eu consigo conferir os preços ao vivo". Não deixe a tarefa parada esperando o ambiente ideal.
