# Como contribuir

Obrigado pelo interesse. O orquestrar melhora com uso real, então a contribuição mais valiosa quase nunca é código.

> Contributions in English are welcome. Issues and pull requests can be written in either language.

## Formas de contribuir, da mais à menos valiosa

### 1. Conte como você trabalha com IA (sem código)

Se você é profissional de alguma área, como direito, pesquisa, ensino ou saúde, ou simplesmente usa IA para se organizar, [abra um relato](https://github.com/CafeSemCafeina/orquestrar/issues/new?template=relato-profissional.yml). Conte que tarefas você leva para a IA, o que funciona, o que irrita e o que você não confia em deixar com ela.

Relatos são a matéria-prima dos [packs por profissão](PACKS.md), o principal pedido de contribuição deste projeto.

### 2. Relate um caso de uso

Usou o orquestrar e algo chamou atenção, bom ou ruim? [Abra um caso de campo](https://github.com/CafeSemCafeina/orquestrar/issues/new?template=caso-de-campo.yml): o pedido, o app, o que o agente fez e o que você esperava. Casos de campo viram casos de eval.

Antes de colar uma conversa, retire nomes, documentos e dados pessoais seus e de outras pessoas.

### 3. Construa um pack

Leia o [PACKS.md](PACKS.md), abra uma [proposta de pack](https://github.com/CafeSemCafeina/orquestrar/issues/new?template=proposta-de-pack.yml) e parta de [`templates/pack/`](templates/pack/).

### 4. Melhore o método

Mudanças em `plugins/orquestrar/skills/orquestrar/` seguem uma regra: **a versão nova precisa vencer, ou ao menos não perder, para a anterior nos evals**, inclusive nas armadilhas. Veja [`evals/README.md`](evals/README.md) para rodar.

Abra uma issue antes de uma mudança grande, para combinarmos o que medir.

## Pull requests

1. Faça um fork e crie um branch a partir de `main`.
2. Mantenha cada PR pequeno e com um propósito.
3. Se mudou a skill, anexe o relatório da rodada de evals em `evals/runs/<data>-<versão>/`.
4. Se mudou um plugin, rode `claude plugin validate .` na raiz do repositório.
5. Atualize o [CHANGELOG.md](CHANGELOG.md) na seção "Não lançado".

## Estilo de escrita da skill

- Português do Brasil, frases curtas, voz ativa.
- Exemplos concretos valem mais que regras abstratas.
- Fale com o agente, não sobre ele: "pergunte no máximo três coisas", não "o agente deve perguntar".
- Termos técnicos (subagente, topologia, harness) são do agente, nunca da pessoa atendida.
- Sem emoji. Nenhuma promessa sem fonte ou teste.

## Versões

Seguimos [versionamento semântico](https://semver.org/lang/pt-BR/). Enquanto a versão for 0.x, qualquer versão pode mudar o comportamento da skill.

## Código de conduta

Ao participar, você concorda com o [código de conduta](CODE_OF_CONDUCT.md).
