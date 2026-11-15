# Modelo de pack

1. Copie esta pasta para `plugins/orquestrar-<area>/` e troque `AREA`, `SEU NOME` e os textos em maiúsculas.
2. Renomeie `skills/orquestrar-AREA/` para `skills/orquestrar-<area>/`; o `name` do `SKILL.md` precisa ser igual ao nome da pasta.
3. Escreva de 5 a 10 casos em `evals/cases/<area>/`, a partir de relatos reais, incluindo armadilhas.
4. Adicione o plugin aos dois catálogos (`.claude-plugin/marketplace.json` e `.agents/plugins/marketplace.json`).
5. Rode `claude plugin validate .` na raiz e a rodada de evals da área.

Veja o [PACKS.md](../../PACKS.md) para o que entra em cada parte.
