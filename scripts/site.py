#!/usr/bin/env python3
"""Gera docs/index.html (pt-BR) e docs/en/index.html (en) a partir de um só modelo.

Uso: python3 scripts/site.py
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = "https://github.com/Syntelix-AI/orquestrar"
SOURCE = "Syntelix-AI/orquestrar"
ISSUE_RELATO = f"{REPO}/issues/new?template=relato-profissional.yml"

CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>'

# Pontos das rodadas às cegas (evals/runs/2026-11-14-v03/RELATORIO.md)
SCORES = [("Claude", "9", "9", 134, 94), ("Codex", "8", "9", 101, 70), ("Gemini", "9", "9", 126, 66)]
MAX_POINTS = 9 * 16

T = {
"pt": {
  "lang": "pt-BR", "prefix": "", "other": "en/", "other_label": "EN", "other_name": "English",
  "title": "orquestrar · do pedido vago ao trabalho entregue e conferido",
  "description": "Plugin aberto para Claude, ChatGPT e Codex que conduz qualquer tarefa com método: entende o pedido, testa a ferramenta, confere antes de entregar e pede aprovação antes do que não dá para desfazer.",
  "skip": "Pular para o conteúdo",
  "nav": [("#como-funciona", "Como funciona"), ("#resultados", "Resultados"), ("#instalar", "Instalar"), ("#packs", "Packs")],
  "hero_kicker": "Plugin aberto para agentes de IA",
  "hero_h1": "Peça do seu jeito. <em>O método fica com o agente.</em>",
  "hero_lede": "O orquestrar faz o Claude, o ChatGPT e o Codex conduzirem qualquer tarefa como alguém experiente: entendem o que você quer, testam o que a ferramenta consegue, conferem antes de entregar e param para pedir sua aprovação antes do que não dá para desfazer.",
  "cta_install": "Instalar", "cta_github": "Ver no GitHub",
  "chips": ["Claude", "ChatGPT", "Codex", "Gratuito e aberto"],
  "ex_bar": "Exemplo de uma rodada de testes", "ex_bar2": "Codex · com orquestrar",
  "ex_you": "Você", "ex_agent": "Agente",
  "ex_user": "preciso de posts pro instagram do mes todo, vendo vela artesanl",
  "ex_agent_html": "Vou preparar um calendário do mês com ideias de imagem, texto e legenda. Começo com uma amostra para você ver se combina com a sua marca.<ol><li>Quantos posts por semana? <span class=\"default\">Se não souber: três.</span></li><li>Para quem você vende? <span class=\"default\">Se não souber: velas para presentear.</span></li><li>Que tom? <span class=\"default\">Se não souber: acolhedor e simples.</span></li></ol>Pode responder do seu jeito ou só dizer “pode seguir”.<span class=\"stop\">Não tenho acesso ao seu Instagram: não publico nada.</span>",
  "ex_note": "Resumo de uma resposta real dos testes (caso 05).",
  "cmp_kicker": "O que muda", "cmp_h2": "A mesma pergunta, <em>com e sem método.</em>",
  "cmp_lede": "Caso real dos testes: “meu plano de saúde negou um exame que o médico pediu, preciso fazer uma carta ou petição pra eles. me ajuda?”",
  "cmp_without": "Sem método", "cmp_with": "Com orquestrar",
  "cmp_without_items": ["Abre com cinco perguntas, nenhuma com resposta padrão.", "Nada começa até você responder tudo.", "Não diz como vai conferir as regras do plano.", "Não deixa claro que o texto precisa de revisão antes de ser enviado."],
  "cmp_with_items": ["Já começa o rascunho da carta e pergunta em cima dele.", "No máximo três perguntas, cada uma com um padrão seguro.", "Diz que vai conferir as regras aplicáveis antes de afirmar qualquer direito.", "Entrega um documento editável e lembra que o envio é decisão sua."],
  "how_kicker": "Como funciona", "how_h2": "Cinco fases, <em>e uma triagem antes.</em>",
  "how_lede": "O agente percorre as fases sozinho. Você só aparece quando há uma decisão que é sua.",
  "phases": [
    ("0", "Triagem", "Pergunta simples recebe resposta direta e completa. Sem cerimônia.", ""),
    ("1", "Intenção", "Resultado, prazo e limites. Até três perguntas, cada uma com um padrão.", ""),
    ("2", "Diagnóstico", "Testa o que a ferramenta consegue e escolhe a menor forma de trabalho.", ""),
    ("3", "Execução", "Prepara tudo o que é reversível. Para antes de enviar, publicar ou apagar.", "decide"),
    ("4", "Verificação", "Confere números, fontes e formatos. Quem produz não aprova.", "verify"),
    ("5", "Entrega", "Um documento, planilha ou pasta, com um recibo curto do que foi feito.", ""),
  ],
  "ben_kicker": "Por que usar", "ben_h2": "Menos esforço seu, <em>mais cuidado do agente.</em>",
  "benefits": [
    ("Você não precisa saber escrever prompts", "Peça como pediria a um colega. O agente descobre o que falta com poucas perguntas, cada uma com uma resposta padrão.", ""),
    ("Nada irreversível sem você", "E-mails, publicações, envios e exclusões ficam preparados e esperando o seu “pode enviar”.", "decide"),
    ("Conferido antes de chegar", "O agente diz o que verificou e o que ficou em aberto. Quem fez o trabalho não é quem aprova.", ""),
    ("Algo para usar, não texto solto", "O resultado vem como documento, planilha ou slides que você edita, e um recibo do que foi feito.", ""),
  ],
  "res_kicker": "Resultados", "res_h2": "Testado às cegas, <em>em três famílias de modelos.</em>",
  "res_lede": "Em cada caso, um juiz recebe duas respostas sem saber qual usou o orquestrar: a do mesmo modelo com o plugin e a do mesmo modelo sem ele.",
  "res_wins": "vitórias em 9 casos", "res_with": "com", "res_without": "sem", "res_points": "pontos",
  "res_v04_label": "Versão 0.4, com repetições:", "res_v04_text": "16 vitórias e 1 empate em 17 comparações, nenhuma derrota.",
  "res_link": "Ver os relatórios dos testes",
  "inst_kicker": "Instalar", "inst_h2": "Escolha o seu app.",
  "inst_lede": "Leva um minuto. Se os menus aparecerem em inglês, os nomes estão entre parênteses.",
  "copy": "Copiar", "copied": "Copiado",
  "tabs": [
    ("claude", "Claude", [
      "Abra <span class=\"path\">Personalizar (Customize)</span> e vá à aba <span class=\"path\">Plugins</span>.",
      "Em <span class=\"path\">Plugins pessoais (Personal plugins)</span>, clique em <span class=\"path\">+</span> e escolha <span class=\"path\">Adicionar marketplace (Add marketplace)</span>.",
      "Escolha adicionar a partir de um repositório e cole:{copy:" + SOURCE + "}",
      "Instale o <span class=\"path\">orquestrar</span> na lista que aparecer.",
    ], "Vale no Claude da web, no desktop e no Claude Code, que recebe os plugins da sua conta. Se você já tinha enviado o .zip da skill, remova a cópia avulsa em Personalizar → Skills, para não ficarem duas."),
    ("chatgpt", "ChatGPT e Codex (desktop)", [
      "Abra <span class=\"path\">Plugins</span> no app (no modo de trabalho ou na aba Codex).",
      "Clique em <span class=\"path\">Adicionar marketplace</span>.",
      "Em <span class=\"path\">Origem</span>, cole:{copy:" + SOURCE + "}Em <span class=\"path\">Referência do Git</span>, use <code>main</code>. Deixe <span class=\"path\">Caminhos esparsos</span> vazio.",
      "Instale o <span class=\"path\">orquestrar</span> na lista de plugins.",
    ], "Se o seu app do ChatGPT não mostra a opção de adicionar marketplace, use a aba “Só a skill”: o envio de plugins próprios ao chat pode depender do seu plano."),
    ("claude-code", "Claude Code", [
      "Num terminal com o Claude Code aberto, rode:{copy:/plugin marketplace add " + SOURCE + "}",
      "Depois:{copy:/plugin install orquestrar@orquestrar}",
    ], "Para conferir, rode <code>/plugin</code> e procure o orquestrar entre os instalados."),
    ("codex-cli", "Codex CLI", [
      "No terminal, rode:{copy:codex plugin marketplace add " + SOURCE + "}",
      "Depois:{copy:codex plugin add orquestrar@orquestrar}",
    ], "Comece uma sessão nova do Codex para a skill aparecer. Testado no Codex CLI 0.169."),
    ("zip", "Só a skill (.zip)", [
      "Baixe o arquivo:{download}",
      "No Claude: <span class=\"path\">Personalizar → Skills → + → Enviar uma skill (Upload a skill)</span>.",
      "No ChatGPT: <span class=\"path\">Skills → Criar → Enviar do computador</span>. No ChatGPT, as skills da web e do desktop não sincronizam: envie nos dois se usar os dois.",
    ], "Assim você instala só a skill, sem catálogo. Atualizações não chegam sozinhas: baixe de novo quando sair uma versão."),
  ],
  "download": "Baixar orquestrar-skill.zip",
  "packs_kicker": "Packs por profissão", "packs_h2": "O método é geral. <em>Cada profissão tem o seu jeito.</em>",
  "packs_lede": "Os packs ensinam ao agente o que é próprio de cada área: as perguntas certas, os documentos típicos, as fontes para conferir e onde é preciso parar e pedir aprovação. Eles nascem de relatos de quem trabalha na área.",
  "packs": [
    ("Jurídico", "Prazos, peças, pesquisa de jurisprudência e o que nunca se protocola sem revisão."),
    ("Pesquisa acadêmica", "Pergunta de pesquisa, revisão de literatura, citações que existem de verdade."),
    ("Estudos", "Planos de estudo, fichamentos e revisão que respeitam o tempo real de quem estuda."),
    ("Organização pessoal", "Semanas possíveis, listas que cabem na agenda e prioridades que não se perdem."),
  ],
  "pack_status": "procurando profissionais",
  "packs_cta": "Contar como eu trabalho com IA", "packs_cta2": "Como um pack é feito",
  "packs_note": "Não precisa programar. Um relato curto já vira caso de teste e orienta o pack da sua área.",
  "faq_kicker": "Perguntas", "faq_h2": "Antes de instalar.",
  "faq": [
    ("É seguro?", "O plugin é só texto: instruções que o agente lê. Ele não roda programas, não instala nada no seu computador e não pede acesso a contas. O agente continua com as mesmas permissões de antes, e a skill manda que ele pare e peça sua aprovação antes de enviar, publicar, pagar ou apagar."),
    ("Quanto custa?", "Nada. O orquestrar é aberto, sob a licença MIT. Ele usa o plano que você já tem em cada app; a disponibilidade de plugins e skills depende desse plano."),
    ("Meu assistente vai ficar lento ou cheio de perguntas?", "Não deveria. Perguntas simples continuam com resposta direta, e os testes têm uma armadilha só para isso. Em tarefas maiores, são no máximo três perguntas, cada uma com uma resposta padrão: você pode só dizer “pode seguir”."),
    ("Funciona em outras línguas?", "A skill está escrita em português, mas o agente responde na língua em que você escreve."),
    ("Como eu removo?", "Na mesma tela de plugins do app, desinstale o orquestrar. No terminal: /plugin uninstall orquestrar@orquestrar (Claude Code) ou codex plugin remove orquestrar@orquestrar (Codex)."),
    ("Quem faz?", "David Fiocchi, da Syntelix, com contribuições abertas a qualquer pessoa. Relatos de uso real valem mais que qualquer opinião: é com eles que o método melhora."),
  ],
  "footer_thesis": "Nenhuma inteligência progride sozinha.",
  "footer_made": "Feito por David Fiocchi · <a href=\"https://syntelix.ia.br\">Syntelix</a>",
  "footer_links": [("GitHub", REPO), ("Como contribuir", f"{REPO}/blob/main/CONTRIBUTING.md"), ("Licença MIT", f"{REPO}/blob/main/LICENSE")],
},
"en": {
  "lang": "en", "prefix": "../", "other": "../", "other_label": "PT", "other_name": "Português",
  "title": "orquestrar · from a vague request to finished, checked work",
  "description": "Open plugin for Claude, ChatGPT and Codex that runs any task with a method: understands the request, tests the tool, checks before delivering and asks for approval before anything that can't be undone.",
  "skip": "Skip to content",
  "nav": [("#how", "How it works"), ("#results", "Results"), ("#install", "Install"), ("#packs", "Packs")],
  "hero_kicker": "Open plugin for AI agents",
  "hero_h1": "Ask your way. <em>The agent brings the method.</em>",
  "hero_lede": "orquestrar makes Claude, ChatGPT and Codex run any task like someone experienced: they work out what you want, test what the tool can do, check before delivering and stop to ask you before anything that can't be undone.",
  "cta_install": "Install", "cta_github": "View on GitHub",
  "chips": ["Claude", "ChatGPT", "Codex", "Free and open"],
  "ex_bar": "Example from a test round", "ex_bar2": "Codex · with orquestrar",
  "ex_you": "You", "ex_agent": "Agent",
  "ex_user": "need instagram posts for the whole month, i sell handmade candels",
  "ex_agent_html": "I'll put together a month-long calendar with image ideas, copy and captions. I'll start with a sample so you can see if it fits your brand.<ol><li>How many posts a week? <span class=\"default\">If unsure: three.</span></li><li>Who do you sell to? <span class=\"default\">If unsure: candles as gifts.</span></li><li>What tone? <span class=\"default\">If unsure: warm and simple.</span></li></ol>Answer however you like, or just say “go ahead”.<span class=\"stop\">I don't have access to your Instagram: I won't post anything.</span>",
  "ex_note": "Translated summary of a real answer from the tests (case 05).",
  "cmp_kicker": "What changes", "cmp_h2": "Same question, <em>with and without a method.</em>",
  "cmp_lede": "A real test case: “my health plan denied a test my doctor ordered, I need to write them a letter or a petition. can you help?”",
  "cmp_without": "Without a method", "cmp_with": "With orquestrar",
  "cmp_without_items": ["Opens with five questions, none with a default answer.", "Nothing starts until you answer them all.", "Doesn't say how it will check the plan's rules.", "Doesn't make clear the text needs review before it's sent."],
  "cmp_with_items": ["Starts drafting the letter and asks on top of the draft.", "Three questions at most, each with a safe default.", "Says it will check the applicable rules before claiming any right.", "Delivers an editable document and reminds you that sending it is your call."],
  "how_kicker": "How it works", "how_h2": "Five phases, <em>and a triage first.</em>",
  "how_lede": "The agent goes through the phases on its own. You only come in when there's a decision that is yours.",
  "phases": [
    ("0", "Triage", "A simple question gets a direct, complete answer. No ceremony.", ""),
    ("1", "Intent", "Result, deadline and limits. Up to three questions, each with a default.", ""),
    ("2", "Diagnosis", "Tests what the tool can do and picks the smallest way of working.", ""),
    ("3", "Execution", "Prepares everything reversible. Stops before sending, publishing or deleting.", "decide"),
    ("4", "Verification", "Checks numbers, sources and formats. Whoever produced it doesn't approve it.", "verify"),
    ("5", "Delivery", "A document, spreadsheet or folder, with a short receipt of what was done.", ""),
  ],
  "ben_kicker": "Why use it", "ben_h2": "Less effort from you, <em>more care from the agent.</em>",
  "benefits": [
    ("No prompt writing needed", "Ask as you'd ask a colleague. The agent finds what's missing with a few questions, each with a default answer.", ""),
    ("Nothing irreversible without you", "Emails, posts, submissions and deletions stay prepared and wait for your “send it”.", "decide"),
    ("Checked before it reaches you", "The agent says what it verified and what's still open. Whoever did the work isn't who approves it.", ""),
    ("Something to use, not loose text", "Results come as documents, spreadsheets or slides you can edit, plus a receipt of what was done.", ""),
  ],
  "res_kicker": "Results", "res_h2": "Tested blind, <em>across three model families.</em>",
  "res_lede": "In each case, a judge gets two answers without knowing which used orquestrar: the same model with the plugin and the same model without it.",
  "res_wins": "wins in 9 cases", "res_with": "with", "res_without": "without", "res_points": "points",
  "res_v04_label": "Version 0.4, with repetitions:", "res_v04_text": "16 wins and 1 tie in 17 comparisons, no losses.",
  "res_link": "See the test reports",
  "inst_kicker": "Install", "inst_h2": "Pick your app.",
  "inst_lede": "It takes a minute.",
  "copy": "Copy", "copied": "Copied",
  "tabs": [
    ("claude", "Claude", [
      "Open <span class=\"path\">Customize</span> and go to the <span class=\"path\">Plugins</span> tab.",
      "Under <span class=\"path\">Personal plugins</span>, click <span class=\"path\">+</span> and choose <span class=\"path\">Add marketplace</span>.",
      "Choose to add from a repository and paste:{copy:" + SOURCE + "}",
      "Install <span class=\"path\">orquestrar</span> from the list.",
    ], "Works on Claude web, desktop and Claude Code, which receives your account's plugins. If you had already uploaded the skill's .zip, remove that copy under Customize → Skills so you don't have two."),
    ("chatgpt", "ChatGPT and Codex (desktop)", [
      "Open <span class=\"path\">Plugins</span> in the app (in work mode or in the Codex tab).",
      "Click <span class=\"path\">Add marketplace</span>.",
      "Under <span class=\"path\">Source</span>, paste:{copy:" + SOURCE + "}Under <span class=\"path\">Git ref</span>, use <code>main</code>. Leave <span class=\"path\">Sparse paths</span> empty.",
      "Install <span class=\"path\">orquestrar</span> from the plugin list.",
    ], "If your ChatGPT app doesn't show the option to add a marketplace, use the “Just the skill” tab: adding your own plugins to chat may depend on your plan."),
    ("claude-code", "Claude Code", [
      "In a terminal with Claude Code open, run:{copy:/plugin marketplace add " + SOURCE + "}",
      "Then:{copy:/plugin install orquestrar@orquestrar}",
    ], "To check, run <code>/plugin</code> and look for orquestrar among installed plugins."),
    ("codex-cli", "Codex CLI", [
      "In a terminal, run:{copy:codex plugin marketplace add " + SOURCE + "}",
      "Then:{copy:codex plugin add orquestrar@orquestrar}",
    ], "Start a new Codex session for the skill to show up. Tested on Codex CLI 0.169."),
    ("zip", "Just the skill (.zip)", [
      "Download the file:{download}",
      "In Claude: <span class=\"path\">Customize → Skills → + → Upload a skill</span>.",
      "In ChatGPT: <span class=\"path\">Skills → Create → Upload from your computer</span>. ChatGPT's web and desktop skills don't sync: upload to both if you use both.",
    ], "This installs only the skill, with no catalog. Updates won't arrive on their own: download again when a new version ships."),
  ],
  "download": "Download orquestrar-skill.zip",
  "packs_kicker": "Packs by profession", "packs_h2": "The method is general. <em>Every profession has its own way.</em>",
  "packs_lede": "Packs teach the agent what belongs to each field: the right questions, typical documents, sources to check against, and where it must stop and ask. They're built from accounts of people who work in the field.",
  "packs": [
    ("Legal", "Deadlines, filings, case-law research, and what is never filed without review."),
    ("Academic research", "Research questions, literature reviews, citations that actually exist."),
    ("Studying", "Study plans, notes and review that respect a student's real time."),
    ("Personal organization", "Doable weeks, lists that fit the calendar and priorities that don't get lost."),
  ],
  "pack_status": "looking for professionals",
  "packs_cta": "Tell us how you work with AI", "packs_cta2": "How a pack is made",
  "packs_note": "No coding needed. A short account already becomes a test case and shapes the pack for your field.",
  "faq_kicker": "Questions", "faq_h2": "Before you install.",
  "faq": [
    ("Is it safe?", "The plugin is just text: instructions the agent reads. It doesn't run programs, install anything on your computer or ask for account access. The agent keeps the same permissions as before, and the skill tells it to stop and ask for your approval before sending, publishing, paying or deleting."),
    ("How much does it cost?", "Nothing. orquestrar is open source under the MIT license. It uses the plan you already have in each app; plugin and skill availability depends on that plan."),
    ("Will my assistant get slow or ask too many questions?", "It shouldn't. Simple questions still get direct answers, and the tests include a trap just for that. For bigger tasks, it asks three questions at most, each with a default: you can just say “go ahead”."),
    ("Does it work in other languages?", "The skill is written in Portuguese, but the agent replies in the language you write in."),
    ("How do I remove it?", "Uninstall orquestrar on the same plugins screen in your app. In a terminal: /plugin uninstall orquestrar@orquestrar (Claude Code) or codex plugin remove orquestrar@orquestrar (Codex)."),
    ("Who makes it?", "David Fiocchi, from Syntelix, with contributions open to anyone. Real usage reports beat any opinion: that's how the method improves."),
  ],
  "footer_thesis": "No intelligence progresses alone.",
  "footer_made": "Made by David Fiocchi · <a href=\"https://syntelix.ia.br\">Syntelix</a>",
  "footer_links": [("GitHub", REPO), ("Contributing", f"{REPO}/blob/main/CONTRIBUTING.md"), ("MIT license", f"{REPO}/blob/main/LICENSE")],
},
}

IDS = {"pt": {"how": "como-funciona", "results": "resultados", "install": "instalar"},
       "en": {"how": "how", "results": "results", "install": "install"}}


def step_html(text, s):
    """Troca {copy:...} por uma caixa com botão de copiar e {download} pelo botão de download."""
    out = text
    while "{copy:" in out:
        a = out.index("{copy:")
        b = out.index("}", a)
        value = out[a + 6:b]
        box = (f'<span class="copy"><code>{escape(value)}</code>'
               f'<button type="button" data-copy="{escape(value)}" data-done="{escape(s["copied"])}">{escape(s["copy"])}</button></span>')
        out = out[:a] + box + out[b + 1:]
    dl = (f'<span class="actions" style="margin-top:.7rem"><a class="btn btn--primary" href="{s["prefix"]}download/orquestrar-skill.zip" download>'
          f'{escape(s["download"])}</a></span>')
    return out.replace("{download}", dl)


def render(code):
    s = T[code]
    ids = IDS[code]
    p = s["prefix"]
    nav = "".join(f'<a class="nav-link" href="{h}">{escape(t)}</a>' for h, t in s["nav"])
    chips = "".join(f'<li class="chip">{CHECK}{escape(c)}</li>' for c in s["chips"])
    without = "".join(f"<li>{escape(i)}</li>" for i in s["cmp_without_items"])
    with_ = "".join(f"<li>{escape(i)}</li>" for i in s["cmp_with_items"])
    phases = "".join(
        f'<li class="phase{" phase--" + k if k else ""} reveal"><div class="node">{n}</div><h3>{escape(t)}</h3><p>{escape(d)}</p></li>'
        for n, t, d, k in s["phases"])
    benefits = "".join(
        f'<article class="finding{" finding--" + k if k else ""} reveal"><h3>{escape(t)}</h3><p>{escape(d)}</p></article>'
        for t, d, k in s["benefits"])
    scores = ""
    for fam, w, total, a, b in SCORES:
        scores += (f'<div class="score reveal"><p class="meta">{fam}</p>'
                   f'<p class="score__big">{w}<span>/</span>{total}</p><p class="meta">{escape(s["res_wins"])}</p>'
                   f'<p class="meta" style="margin-top:1.1rem">{escape(s["res_with"])} · {a} {escape(s["res_points"])}</p>'
                   f'<div class="bar bar--with"><i style="width:{a / MAX_POINTS * 100:.1f}%"></i></div>'
                   f'<p class="meta">{escape(s["res_without"])} · {b} {escape(s["res_points"])}</p>'
                   f'<div class="bar bar--without"><i style="width:{b / MAX_POINTS * 100:.1f}%"></i></div></div>')
    tabs, panels = "", ""
    for i, (tid, label, steps, note) in enumerate(s["tabs"]):
        sel = "true" if i == 0 else "false"
        tabs += (f'<button class="tab" role="tab" id="tab-{tid}" aria-controls="panel-{tid}" aria-selected="{sel}" '
                 f'tabindex="{0 if i == 0 else -1}">{escape(label)}</button>')
        items = "".join(f"<li>{step_html(st, s)}</li>" for st in steps)
        panels += (f'<div class="tabpanel" role="tabpanel" id="panel-{tid}" aria-labelledby="tab-{tid}"{"" if i == 0 else " hidden"}>'
                   f'<h3>{escape(label)}</h3><ol class="steps">{items}</ol><p class="note">{note}</p></div>')
    packs = "".join(
        f'<article class="pack reveal"><span class="status">{escape(s["pack_status"])}</span><h3>{escape(t)}</h3><p>{escape(d)}</p></article>'
        for t, d in s["packs"])
    faq = "".join(f"<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>" for q, a in s["faq"])
    links = " · ".join(f'<a href="{u}">{escape(t)}</a>' for t, u in s["footer_links"])
    alt = "en" if code == "pt" else "pt-BR"

    return f"""<!DOCTYPE html>
<html lang="{s['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(s['title'])}</title>
<meta name="description" content="{escape(s['description'])}">
<meta property="og:title" content="{escape(s['title'])}">
<meta property="og:description" content="{escape(s['description'])}">
<meta property="og:type" content="website">
<link rel="alternate" hreflang="{alt}" href="{s['other']}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Ccircle cx='9' cy='10' r='4' fill='%23673981'/%3E%3Ccircle cx='23' cy='9' r='3' fill='%233f817c'/%3E%3Ccircle cx='16' cy='23' r='5' fill='%23d96f52'/%3E%3C/svg%3E">
<link rel="preload" href="{p}assets/fonts/source-serif-4.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{p}assets/fonts/inter.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{p}assets/site.css">
<script>document.documentElement.classList.add('js-reveal')</script>
</head>
<body>
<a class="skip" href="#conteudo">{escape(s['skip'])}</a>
<header class="topbar"><div class="shell">
  <a class="brand" href="./">orquestrar</a>
  <nav class="nav" aria-label="principal">{nav}<a class="nav-link" href="{REPO}">GitHub</a><a class="lang" href="{s['other']}" hreflang="{alt}" title="{escape(s['other_name'])}">{s['other_label']}</a></nav>
</div></header>

<main id="conteudo">
<section class="hero"><div class="shell">
  <div>
    <p class="kicker">{escape(s['hero_kicker'])}</p>
    <h1>{s['hero_h1']}</h1>
    <p class="lede">{escape(s['hero_lede'])}</p>
    <div class="actions"><a class="btn btn--primary" href="#{ids['install']}">{escape(s['cta_install'])}</a><a class="btn btn--secondary" href="{REPO}">{escape(s['cta_github'])}</a></div>
    <ul class="chips">{chips}</ul>
  </div>
  <figure class="artifact" style="margin:0">
    <div class="artifact__bar"><span class="meta">{escape(s['ex_bar'])}</span><span class="meta">{escape(s['ex_bar2'])}</span></div>
    <div class="msg msg--user"><span class="meta msg__who">{escape(s['ex_you'])}</span>{escape(s['ex_user'])}</div>
    <div class="msg msg--agent"><span class="meta msg__who">{escape(s['ex_agent'])}</span>{s['ex_agent_html']}</div>
    <figcaption class="meta" style="margin-top:1rem">{escape(s['ex_note'])}</figcaption>
  </figure>
</div></section>

<section><div class="shell">
  <div class="section-head"><p class="kicker">{escape(s['cmp_kicker'])}</p><h2>{s['cmp_h2']}</h2><p class="lede">{escape(s['cmp_lede'])}</p></div>
  <div class="compare">
    <article class="panel reveal"><p class="meta">{escape(s['cmp_without'])}</p><ul>{without}</ul></article>
    <article class="panel panel--with reveal"><p class="meta" style="color:var(--purple-600)">{escape(s['cmp_with'])}</p><ul>{with_}</ul></article>
  </div>
</div></section>

<section id="{ids['how']}"><div class="shell">
  <div class="section-head"><p class="kicker">{escape(s['how_kicker'])}</p><h2>{s['how_h2']}</h2><p class="lede">{escape(s['how_lede'])}</p></div>
  <ol class="phases">{phases}</ol>
</div></section>

<section><div class="shell">
  <div class="section-head"><p class="kicker">{escape(s['ben_kicker'])}</p><h2>{s['ben_h2']}</h2></div>
  <div class="findings">{benefits}</div>
</div></section>

<section class="night" id="{ids['results']}"><div class="shell">
  <div class="section-head"><p class="kicker kicker--light">{escape(s['res_kicker'])}</p><h2>{s['res_h2']}</h2><p class="lede">{escape(s['res_lede'])}</p></div>
  <div class="scores">{scores}</div>
  <div class="v04"><span class="meta" style="color:var(--purple-200)">{escape(s['res_v04_label'])}</span><strong>16/17</strong><span>{escape(s['res_v04_text'])}</span></div>
  <div class="actions"><a class="btn btn--light" href="{REPO}/tree/main/evals">{escape(s['res_link'])}</a></div>
</div></section>

<section id="{ids['install']}"><div class="shell">
  <div class="section-head"><p class="kicker">{escape(s['inst_kicker'])}</p><h2>{s['inst_h2']}</h2><p class="lede">{escape(s['inst_lede'])}</p></div>
  <div class="tabs" role="tablist" aria-label="{escape(s['inst_kicker'])}">{tabs}</div>
  {panels}
</div></section>

<section id="packs"><div class="shell">
  <div class="section-head"><p class="kicker">{escape(s['packs_kicker'])}</p><h2>{s['packs_h2']}</h2><p class="lede">{escape(s['packs_lede'])}</p></div>
  <div class="packs">{packs}</div>
  <div class="actions" style="margin-top:0"><a class="btn btn--primary" href="{ISSUE_RELATO}">{escape(s['packs_cta'])}</a><a class="btn btn--secondary" href="{REPO}/blob/main/PACKS.md">{escape(s['packs_cta2'])}</a></div>
  <p class="lede" style="font-size:.95rem">{escape(s['packs_note'])}</p>
</div></section>

<section><div class="shell faq">
  <div class="section-head"><p class="kicker">{escape(s['faq_kicker'])}</p><h2>{s['faq_h2']}</h2></div>
  {faq}
</div></section>
</main>

<footer><div class="shell">
  <div><p class="thesis">{escape(s['footer_thesis'])}</p><p style="margin:0">{s['footer_made']}</p></div>
  <p style="margin:0">{links}</p>
</div></footer>

<script>
(function () {{
  var tabs = Array.prototype.slice.call(document.querySelectorAll('[role="tab"]'));
  function select(tab) {{
    tabs.forEach(function (t) {{
      var on = t === tab;
      t.setAttribute('aria-selected', on ? 'true' : 'false');
      t.tabIndex = on ? 0 : -1;
      document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
    }});
  }}
  tabs.forEach(function (t, i) {{
    t.addEventListener('click', function () {{ select(t); }});
    t.addEventListener('keydown', function (e) {{
      var n = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
      if (!n) return;
      var next = tabs[(i + n + tabs.length) % tabs.length];
      select(next); next.focus(); e.preventDefault();
    }});
  }});
  document.querySelectorAll('[data-copy]').forEach(function (b) {{
    var label = b.textContent;
    b.addEventListener('click', function () {{
      var text = b.getAttribute('data-copy');
      function ok() {{ b.textContent = b.getAttribute('data-done'); b.classList.add('done'); setTimeout(function () {{ b.textContent = label; b.classList.remove('done'); }}, 1800); }}
      if (navigator.clipboard) {{ navigator.clipboard.writeText(text).then(ok, fallback); }} else {{ fallback(); }}
      function fallback() {{ var ta = document.createElement('textarea'); ta.value = text; document.body.appendChild(ta); ta.select(); try {{ document.execCommand('copy'); ok(); }} catch (e) {{}} document.body.removeChild(ta); }}
    }});
  }});
  var els = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window)) {{ els.forEach(function (e) {{ e.classList.add('is-in'); }}); return; }}
  var io = new IntersectionObserver(function (entries) {{
    entries.forEach(function (en) {{ if (en.isIntersecting) {{ en.target.classList.add('is-in'); io.unobserve(en.target); }} }});
  }}, {{ rootMargin: '0px 0px -8% 0px' }});
  els.forEach(function (e) {{ io.observe(e); }});
}})();
</script>
</body>
</html>
"""


def main():
    (ROOT / "docs").mkdir(exist_ok=True)
    (ROOT / "docs" / "en").mkdir(exist_ok=True)
    (ROOT / "docs" / "index.html").write_text(render("pt"), encoding="utf-8")
    (ROOT / "docs" / "en" / "index.html").write_text(render("en"), encoding="utf-8")
    print("docs/index.html, docs/en/index.html")


if __name__ == "__main__":
    main()
