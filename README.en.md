<div align="center">

# orquestrar

**From a vague request to finished, checked work.**

A plugin for Claude, ChatGPT, Codex and other AI agents that runs any task with a method: it works out what you want, tests what the tool can actually do, picks the smallest way of working that gets it done, checks before delivering, and asks for your approval before anything that can't be undone.

[Website and install](https://cafesemcafeina.github.io/orquestrar/en/) · [Português](README.md) · [Evals](evals/) · [Contributing](CONTRIBUTING.md)

![MIT license](https://img.shields.io/badge/license-MIT-673981)
![Version 0.4.0](https://img.shields.io/badge/version-0.4.0-673981)
![Agent Skills](https://img.shields.io/badge/standard-Agent%20Skills-3f817c)
![Agent Plugins 1.0](https://img.shields.io/badge/standard-Agent%20Plugins%201.0-3f817c)

</div>

---

> The skill itself is written in Brazilian Portuguese and works in any language: agents follow it and reply in the language you write in.

## Why it exists

People who use AI every day keep hearing that they need to learn prompting, build agents and split tasks. orquestrar turns that around: you ask in your own words, and the method lives in the agent.

You still decide **what** you want. The agent decides **how** to do it, and explains why in one line.

## How it works

| Phase | What the agent does | What changes for you |
|---|---|---|
| **0 · Triage** | Decides whether the task needs a method or a direct answer. | Simple questions still get simple, complete answers. |
| **1 · Intent** | Works out the result, the deadline and the limits. Asks at most three questions, each with a default answer. | You can just say "go ahead". |
| **2 · Diagnosis** | Tests what the tool can do (files, web, connectors, parallel assistants) and picks the smallest way of working. | No promises the tool can't keep. |
| **3 · Execution** | Splits work only when it pays off, and really prepares everything that is reversible. | Before sending, publishing or deleting, it stops and asks you. |
| **4 · Verification** | Checks numbers, sources and formats; whoever produced the work doesn't approve it. | You get what was checked and what is still open. |
| **5 · Delivery** | Delivers an artifact (document, spreadsheet, slides, project folder) and a short receipt. | Something you can use, not a wall of chat text. |

When the tool lets it choose models, the plan says in plain words who does what: faster assistants read, a mid-tier model consolidates, the strongest model decides, and a separate assistant reviews.

## Results

orquestrar is tested blind against the same model without the plugin: a judge gets both answers without knowing which is which. Cases include traps, such as a simple question that must not become a project, and a mass email request that must not be sent without approval.

| Round | Model family | Wins | Points (with × without) |
|---|---|---|---|
| v0.3 | Claude | 9 of 9 | 134 × 94 |
| v0.3 | Codex (OpenAI) | 8 of 9 | 101 × 70 |
| v0.3 | Gemini (Google) | 9 of 9 | 126 × 66 |
| v0.4 | Claude and Codex, with repetitions | 16 of 17, 1 tie | [report](evals/runs/2026-11-14-v04/RELATORIO.md) |

**Limits, so you read the numbers carefully:** the tests measure the agent's first reply, not the whole task; the judge is a language model; the 9 cases were written for the project, not collected from real users. Full reports, raw answers and the rubric are in [`evals/`](evals/) (in Portuguese).

## Install

Step by step for each app on the [website](https://cafesemcafeina.github.io/orquestrar/en/).

**Claude (web and desktop):** Customize → Plugins → Personal plugins → **+** → Add marketplace → `CafeSemCafeina/orquestrar`. Then install `orquestrar`.

**ChatGPT desktop and Codex:** Plugins → Add marketplace → source `CafeSemCafeina/orquestrar`, ref `main`. Then install `orquestrar`.

**Claude Code:**

```
/plugin marketplace add CafeSemCafeina/orquestrar
/plugin install orquestrar@orquestrar
```

**Codex CLI:**

```
codex plugin marketplace add CafeSemCafeina/orquestrar
codex plugin add orquestrar@orquestrar
```

**Just the skill, by upload:** download [`orquestrar-skill.zip`](https://cafesemcafeina.github.io/orquestrar/download/orquestrar-skill.zip) and upload it on the skills screen in Claude or ChatGPT.

## Packs by profession

orquestrar is the general method. **Packs** add what each field has of its own: the right questions to understand a request, typical deliverables, sources to check against, and the points where the agent must stop and ask.

Legal, academic research, studying, and personal organization and productivity are the first packs we want to build. Building packs is this project's main call for contributions, and it starts with no code: [tell us how you work with AI today](https://github.com/CafeSemCafeina/orquestrar/issues/new?template=relato-profissional.yml). Each account becomes test cases and shapes the pack for your field. See [PACKS.md](PACKS.md).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). In short: real usage reports beat opinions, and every change to the skill has to beat, or at least not lose to, the previous version in the evals. Issues and pull requests in English are welcome.

This project follows a [code of conduct](CODE_OF_CONDUCT.md). For security issues, see [SECURITY.md](SECURITY.md). Version history is in [CHANGELOG.md](CHANGELOG.md).

## License

[MIT](LICENSE). Made by David Fiocchi, from [Syntelix](https://syntelix.ia.br).
