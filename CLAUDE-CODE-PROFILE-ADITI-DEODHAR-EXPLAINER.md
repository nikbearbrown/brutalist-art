# Claude Code Prompt — Student Profile: Aditi Deodhar (16:9, claude-liam)

A claude-explainer in STUDENT/FELLOW PROFILE mode.

Source: NortheasternISE, "The Cost of the Pivot — How Aditi Deodhar Learned to
Stop, Discard What Works, and Build What Matters" (NortheasternISE, Feb 27,
2026), northeasternise.substack.com. Subject: Aditi Deodhar.

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace. Free pipeline only —
Kokoro voice, no ElevenLabs, no higgsfield, no publishing, no git commit or
push.

```text
Build one 16:9 claude-explainer video in STUDENT/FELLOW PROFILE mode (see the
"Input mode — Student / Fellow profiles" section of
skills/make/ai-explainer/SKILL.md) profiling Aditi Deodhar, from the
NortheasternISE article "The Cost of the Pivot" (Feb 27 2026). claude-liam
voice, @HumanitariansAI branding. Free pipeline only: Kokoro voice, no
ElevenLabs, no higgsfield, no publishing, no git commit or push. Run without
approval pauses.

READ COMPLETELY BEFORE ACTING

- AGENTS.md
- CLAUDE-BRAND.md
- skills/make/ai-explainer/SKILL.md — especially the
  "Input mode — Student / Fellow profiles" section
- skills/make/explainer/SKILL.md (and MOTION.md / REMOTION.md)
- skills/make/your-turn/SKILL.md
- docs/remotion-best-practices/SKILL.md
- runtime/remotion/src/tokens/claude.ts

FORMAT

- 1920x1080 (16:9), 30 fps.
- Voice/persona: Liam (Kokoro am_onyx), register Teardown-warm (celebratory
  but honest; the skepticism aims at the systems not designed for the people
  who must navigate them — never at the subject). Liam narrates ABOUT Aditi
  and signs "Liam, in for Bear"; he never speaks AS her. Folder chip
  @HumanitariansAI (HAI logo bug).
- Audio-first; length from beats — expect 3–5 minutes.
- Title: "The Cost of the Pivot". Restate the article title + author
  (NortheasternISE, Feb 27 2026) in the description.

THE ONE IDEA (build everything to land this)
  The willingness to STOP — to discard working code six hours into a
  competition and rebuild around the real problem — is a learned discipline,
  not a personality trait. "This isn't working, let's start over" is the skill
  that made everything after it possible. Building what matters costs more than
  building what works, and Aditi kept paying it.

THE STORY (profile spine, Teardown-warm)

Cold open (the hook as mystery): six hours into a women's-health hackathon,
her team's app WORKED — symptom tracker, clean demo, on track to finish. Then
a user asked one question: "How are women supposed to afford this?" She told
the team to stop. Discard the working code. Start over. Why would a good
engineer throw away a working build with the clock running out?
Arc — the relocation: 22 years in Pune — school, an Electronics &
Telecom degree at PICT, two years as an SDE at Persistent Systems — then she
left all of it for a permanent restart in Boston with no network and no
scaffolding. She chose the discomfort deliberately: hackathons where she knew
no one, events where she introduced herself to strangers. What it built in her
wasn't just range — it was attention to what people navigating unfamiliar
systems actually need.
Evidence — the builds (each: a gap named → a build → something that serves
people the old tools missed):
  • MediPedia — a local RAG medical-FAQ chatbot built on a budget of ZERO:
    Ollama running LLMs locally, FAISS vector DB, Hugging Face embeddings,
    Python + Streamlit, every component on her own machine, no paid APIs, no
    cloud. Constraint treated as a design problem — and the stack is
    replicable by anyone who can't afford proprietary infrastructure. It's
    why Jutly Inc. hired her as an AI Engineer.
  • Jutly (co-op) — an early-stage Cambridge startup: she learned to operate
    without a playbook — prototype fast, hit dead ends, keep moving.
  • SecureStream AI — 2nd at Confluent AI Day 2025: real-time privacy
    detection on Confluent Cloud + Kafka + Flink + MongoDB, in a three-hour
    sprint.
  • MIT Women's Health AI Hackathon — a conversational agent for documented
    gaps in women's-health research data.
Community — the room she didn't have to enter: as Hub Leader for Rewriting
the Code Boston she led programming for 60+ women in tech over three months —
community infrastructure that's "invisible until it's absent." Mentored two
students through AnitaB.org on the international-student job hunt; earned the
GHC 2024 Advancing Inclusion Scholarship.
The record: MS in Information Systems, Dec 2025, GPA 3.717 — held while doing
a co-op, leading an org, competing in hackathons, and earning two AWS certs
(Cloud Practitioner, AI Practitioner) independently. The number understates it.
The pivot, paid off: FinFluent — an AI personal-finance assistant that helps
women navigate healthcare financial decisions (HSAs, deductibles, maternity
leave) in natural language. DreamAI 2025 finalist; Aditi led the pitch. Every
element of that pivot traces to something specific: the confidence to rebuild
from MediPedia, the instinct to listen and change course from Jutly, the drive
to build for women from her own experience, the maturity to pitch from a course
she chose as a strategic investment.
Landing: "I'm not done figuring it all out. Miles to go. But I feel like I'm
getting there." Not performed idealism — the honest language of someone who
has been paying costs and knows the distance left. The pivot has a cost. She
keeps choosing to pay it.

STRUCTURE (claude-explainer skeleton + your-turn closing)

- Beat 0 — ClaudeComposerAsk cold open. Liam: "Six hours into the hackathon,
  her app worked. Then a user asked one question — and she told her team to
  throw the working code away. Here's why that was the right call. Liam, in
  for Bear."
- Middle — arc → builds → community → the record → the pivot-paid-off, carried
  by the figures below.
- Closing per your-turn: VERDICT recap card (the thesis) → PERSON CREDIT card
  → Your Turn composer beat → title re-read on the @HumanitariansAI brand card.
- Your Turn prompt (Liam reads it in full): "I'm building something that
  technically works. Interview me like a skeptical user: who is this actually
  for, what can't they afford or access, and where does 'it works' quietly
  fail the person it's supposed to serve? Then tell me what I'd have to discard
  to build what matters instead."

FIGURES (rebuild as native motion — REBUILD LAW; never lift the article's images)

FIGURE 1 — THE PIVOT (the spine visual)
  A timeline six hours into a countdown: a working build (green, "symptom
  tracker — demo ready") advancing — then a user question drops in ("How are
  women supposed to afford this?") and the path FORKS: keep the working build
  (grey, dead-ends) vs discard-and-rebuild (terracotta, → FinFluent). The
  terracotta fork is the whole video. Recurs as a motif.

FIGURE 2 — ZERO-BUDGET STACK (MediPedia)
  An assembly diagram: constraint chip "$0 budget / no cloud / no paid APIs"
  on the left; on the right the stack self-assembles from open parts — Ollama
  (local LLM) → Hugging Face embeddings → FAISS (vector DB) → Python +
  Streamlit — all inside one "her own machine" boundary. Caption: "constraint
  as a design problem." Terracotta on the closed local boundary. (LayerStack /
  SourceFlow starter fits.)

FIGURE 3 — GAP → BUILD → SERVES (the pattern across her work)
  A repeating three-node motif applied to four chips — MediPedia, SecureStream
  AI (2nd, Confluent AI Day), MIT Women's Health agent, FinFluent — each
  showing "gap named → build → who it reaches." Same shape four times: she
  finds the gap, builds, and the result serves people the old tools missed.

FIGURE 4 — INVISIBLE UNTIL ABSENT (community infrastructure)
  A room filling: 60+ nodes (women in tech) connecting into a warm network
  over "three months"; then the facilitator node is removed and the network
  frays — the line "invisible until it's absent" lands. Side chips: RTC Boston
  Hub Leader · 2 AnitaB.org mentees · GHC 2024 Advancing Inclusion Scholarship.

FIGURE 5 — WHAT 3.717 UNDERSTATES (the record)
  The GPA number sits center; around it, the things held at the SAME time
  orbit in — co-op, RTC leadership, multiple hackathons, 2 AWS certs
  (independent), a cross-country relocation. Narration: the number understates
  the achievement; the achievement is everything it was held alongside.

PERSON CREDIT card (required, near the outro)
  Aditi Deodhar — MS Information Systems, Northeastern University College of
  Engineering (Dec 2025). AI Engineer. Selected recognitions from the article:
  DreamAI 2025 finalist (FinFluent, pitch lead); 2nd, Confluent AI Day 2025
  (SecureStream AI); GHC 2024 Advancing Inclusion Scholarship (AnitaB.org);
  College of Engineering spotlight, Oct 2025. Public presence named in the
  article: Google Scholar profile, a Medium technical blog, an active public
  GitHub — include these as LABELS only (the article gives no handle URLs, so
  show no invented links). Author credit on the SOURCES card: NortheasternISE,
  Feb 27 2026.

FIGURE RULES

- Claude fidelity palette: cream #FAF9F5 page, warm ink #3D3929, terracotta
  #D97757 as the ONE accent per beat. EB Garamond segment titles, Title Case.
  @HumanitariansAI logo bug per LOGO LAW; full-size HAI mark on the outro card.
- HONESTY (DOUBLE-CHECK LAW for people): only what the article states — real
  institutions, projects, roles, awards, the GPA 3.717, the direct quote
  ("I'm not done figuring it all out. Miles to go. But I feel like I'm getting
  there."). Invent no metric, no handle URL, no accomplishment. The article
  gives no GitHub/Scholar/Medium URLs — name them as labels, show no invented
  links. Reproduce the quote and names exactly; keep soft attributions soft.
- Transform-don't-cut within figure beats.

OUTPUTS

- Build into the owning series' folder per the ownership rule — match wherever
  the Kaustubha Eluri profile was built (the NortheasternISE / HAI profile
  series); suggest
  ../humanitarians_html/youtube/claude-liam-profile-aditi-deodhar/ if no series
  folder exists yet (create it):
  - beat_sheet.json (persona Liam, folderLabel @HumanitariansAI)
  - claude-liam-profile-aditi-deodhar.mp4 (1920x1080)
  - SOURCES.md — article URL, author, date; every on-screen name/award/quote
    verbatim; note that public-presence links are labels only (no URLs in
    source) and that the only statistic is the GPA 3.717.
- Verify the mp4 exists and plays (probe duration + frame count), run the
  VISUAL QC LAW frame pass, then end with the beat → timestamp table.
- If a figure fails to render after two attempts, replace that beat with a
  slate naming it and log it — never silently drop it.
```
