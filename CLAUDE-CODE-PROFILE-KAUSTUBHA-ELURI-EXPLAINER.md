# Claude Code Prompt — Student Profile: Kaustubha Venkata Eluri (16:9, claude-liam)

The worked exemplar for the claude-explainer STUDENT/FELLOW PROFILE mode.

Source: NortheasternISE, "Why Most AI Projects Fail in Production — And One
Engineer Who Bridges That Gap" by Aditi Shinde (Mar 31, 2026),
northeasternise.substack.com. Subject: Kaustubha Venkata Eluri.

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace. Free pipeline only —
Kokoro voice, no ElevenLabs, no higgsfield, no publishing, no git commit or
push.

```text
Build one 16:9 claude-explainer video in STUDENT/FELLOW PROFILE mode (see the
"Input mode — Student / Fellow profiles" section of
skills/make/ai-explainer/SKILL.md) profiling Kaustubha Venkata Eluri, from
the NortheasternISE article "Why Most AI Projects Fail in Production — And One
Engineer Who Bridges That Gap" (Aditi Shinde, Mar 31 2026). claude-liam voice,
@HumanitariansAI branding. Free pipeline only: Kokoro voice, no ElevenLabs, no
higgsfield, no publishing, no git commit or push. Run without approval pauses.

READ COMPLETELY BEFORE ACTING

- AGENTS.md
- CLAUDE-BRAND.md
- skills/make/ai-explainer/SKILL.md — especially the new
  "Input mode — Student / Fellow profiles" section (this build IS its exemplar)
- skills/make/explainer/SKILL.md (and MOTION.md / REMOTION.md)
- skills/make/your-turn/SKILL.md
- docs/remotion-best-practices/SKILL.md
- runtime/remotion/src/tokens/claude.ts

FORMAT

- 1920x1080 (16:9), 30 fps.
- Voice/persona: Liam (Kokoro am_onyx), register Teardown-warm (celebratory
  but honest; the skepticism points at the industry blind spot, never at the
  subject). Liam narrates ABOUT Kaustubha and signs "Liam, in for Bear" — he
  never speaks AS him. Folder chip @HumanitariansAI (HAI logo bug).
- Audio-first; length from beats — expect 3–5 minutes.
- Title: "The Engineer Who Stayed" (or restate the article's own framing).
  Restate the article title + author in the description.

THE ONE IDEA (build everything to land this)
  "Trustworthiness is a system property, not a model property. A model that
  works in isolation is a curiosity; a system that works in production is a
  tool." Every beat is evidence for that one line.

THE STORY (profile spine, Teardown-warm)

Cold open (the hook as mystery): most AI projects don't die because the model
is wrong. They die in the gap between "works in development" and "works when
someone depends on it." Most engineers hit that moment and hand it off.
Kaustubha stayed.
Arc: the mindset came from architectural engineering — a field where buildings
must stand up after you leave. He carried it into software: if you build it,
you're responsible for whether it keeps working.
Evidence (his work, as the argument): accessibility systems at
Smith-Kettlewell (where failure isn't a bug, it's a barrier); full-stack AI at
Evenness; and the project set that all sits on the same boundary —
RapidTriage AI (clinical decision-support under time pressure), Echolin.AI
(deepfake detection with robustness + explainability), Semantic Diff Prompting
(efficiency in vision-language systems), NEUQuest (a mobile platform where
usability and reliability matter as much as features).
What production demands (the teardown of the myth): APIs fail regularly — not
sometimes, regularly; pipelines break; user behavior is unpredictable;
performance matters under load. A system that works for one user and breaks at
a hundred is a demonstration with a critical flaw. The question shifts from
"does this work?" to "does this KEEP working when I'm not in the room?"
The uncelebrated space: the industry celebrates the 2% benchmark bump and the
novel architecture, not the engineer who makes the system stable under load.
"This is not the engineering that gets you cited. This is the engineering that
gets you used."
Landing: trustworthiness isn't perfection — it's reliability, explainability,
resilience to failure, and thoughtful design under real constraints. It's a
system property. That's the work most people skip, and it's what Kaustubha
builds toward.

STRUCTURE (claude-explainer skeleton + your-turn closing)

- Beat 0 — ClaudeComposerAsk cold open. Liam: "Most AI projects don't fail
  because the model is wrong. They fail in the gap between 'works in the lab'
  and 'works when someone depends on it.' Here's one engineer who stayed in
  that gap. Liam, in for Bear."
- Middle — the arc → evidence → production-demands → uncelebrated-space beats,
  carried by the figures below.
- Closing per your-turn: VERDICT recap card (the thesis) → PERSON CREDIT card
  → Your Turn composer beat → title re-read on the @HumanitariansAI brand card.
- Your Turn prompt (Liam reads it in full): "Audit my ML project for the gap
  between 'works in the lab' and 'works when someone depends on it.' List what
  breaks under real load, noisy real-world inputs, and API failures — and for
  each, how to make it degrade gracefully instead of catastrophically."

FIGURES (rebuild as native motion — REBUILD LAW; never lift the article's images)

FIGURE 1 — THE GAP (the spine visual)
  A widening gap between two platforms: "works in development" (metrics green,
  curated data) on the left, "works when someone depends on it" (noisy inputs,
  latency, API failures, scale, trust) on the right. Most projects fall into
  the gap; a bridge is drawn across it. Terracotta on the bridge. This visual
  recurs as a motif.

FIGURE 2 — MODEL vs SYSTEM (the thesis engine)
  One "model" node (accurate in isolation) surrounded by the system it lives
  in — integration, deployment, reliability, failure handling. Narration:
  these aren't model problems, they're system problems. The terracotta line:
  "a curiosity → a tool" as the model node is absorbed into a working system.

FIGURE 3 — THE PROJECTS ON ONE BOUNDARY (evidence chips)
  Four chips — RapidTriage AI · Echolin.AI · Semantic Diff Prompting ·
  NEUQuest — each landing on the SAME boundary line (the lab↔production gap),
  with a one-line "what it must do" under each. They're different domains, one
  discipline. (ChipGrid illustration starter fits.)

FIGURE 4 — WHAT PRODUCTION DEMANDS (the resilience beat)
  A pipeline running; then an API node fails — one branch shows catastrophic
  collapse (whole system red), the other degrades gracefully (system holds,
  one node amber). Repeat the pattern quickly for: data-format change,
  unexpected user input, 1→100 users under load. Narration: "does this KEEP
  working?" Terracotta on "degrade gracefully, not catastrophically."

FIGURE 5 — CITED vs USED (the uncelebrated-space beat)
  A balance/contrast: left, what the industry celebrates (benchmark +2%, novel
  architecture, the accepted paper); right, what it doesn't (stable under load,
  graceful API handling, explainability clinicians trust, latency that meets
  deadlines). Land the line on screen, serif: "the engineering that gets you
  used."

PERSON CREDIT card (required, near the outro)
  Kaustubha Venkata Eluri — Northeastern University (Teaching Assistant,
  Mobile App Development; Academic Peer Mentor; Student Ambassador).
  Links VERBATIM: GitHub github.com/Kaustubha-09 · LinkedIn
  linkedin.com/in/kaustubha-ve. Article CTA, kept soft: "building production
  ML systems and need someone who makes systems reliable, not just accurate?
  Reach out." Author credit on the SOURCES card: Aditi Shinde, NortheasternISE,
  Mar 31 2026.

FIGURE RULES

- Claude fidelity palette: cream #FAF9F5 page, warm ink #3D3929, terracotta
  #D97757 as the ONE accent per beat. EB Garamond segment titles, Title Case.
  @HumanitariansAI logo bug per LOGO LAW; full-size HAI mark on the outro card.
- HONESTY (DOUBLE-CHECK LAW for people): only what the article states — real
  institutions, projects, roles. Invent no metric, quote, credential, or
  accomplishment. Keep soft attributions soft. Reproduce names and links
  exactly. No numbers appear on screen that the article doesn't support (the
  article gives none — so this reel carries NO invented statistics).
- Transform-don't-cut within figure beats.

OUTPUTS

- Build into the owning series' folder per the ownership rule — suggest
  ../humanitarians_html/youtube/claude-liam-profile-kaustubha-eluri/ (or the
  NortheasternISE profile-series folder if one exists; create it if not):
  - beat_sheet.json (persona Liam, folderLabel @HumanitariansAI)
  - claude-liam-profile-kaustubha-eluri.mp4 (1920x1080)
  - SOURCES.md — article URL, author, date; every on-screen name and link
    verbatim; note explicitly that the reel carries no statistics because the
    source states none.
- Verify the mp4 exists and plays (probe duration + frame count), run the
  VISUAL QC LAW frame pass, then end with the beat → timestamp table.
- If a figure fails to render after two attempts, replace that beat with a
  slate naming it and log it — never silently drop it.
```
