# SERIES ROADMAP — "Make It Visible: Visual Identity & Wireframes"

A how-to ai-explainer series for **INFO 7375 Assignment 7 — Visual Identity & Wireframes**
(a PDF + Figma board, 100 pts, due July 17, 2026). Audience: **students who locked brand strategy
in A6 and have never designed a logo, built a mood board, or wireframed a site.** Register:
**pragmatic, step-by-step** (Liam voice, `claude-liam`, Kokoro am_onyx). The series walks a
beginner from "my brand is a strategy document" to "a logo, a palette, a type system, a style
guide, and five wireframes I can hand to A8's website build."

> **Numbering note:** the course calls this **Assignment 7**. The *investor pitch video midterm*
> (due July 10) is separately numbered — I kept its roadmap as `a7-investor-pitch`; this one is
> `a7-visual`. This assignment feeds **A8** directly (A8's website "implements your Assignment 7
> brand assets — logo, color palette, typography, visual style"). Pick the **same path as A6**
> (A personal / B startup). Voice: `claude-liam`; `claude-hai` is the one-variable alternative.

## Toolkit tie-in (say it in E1)

This is the **`nina`** skill's home turf — its commands map 1:1 to the components:
`/brief` → Component 1, `/logo` + `/visual` + `/palette` + `/styleguide` → Component 2,
`/wireframes` → Component 3. The Your Turn prompts route students to `nina` for each piece, then
the human taste pass.

## The line that runs through the series

**You're making strategy visible, not rewriting it.** A6's mission, UVP, pillars, and positioning
carry directly in — the brief is a *one-page synthesis*, not a repeat. Every design decision is
filtered through the creative brief; if a choice doesn't trace to the brief, it's decoration.

## Honesty / craft threads (DOUBLE-CHECK LAW)

- **Generic = the top pitfall.** A visual identity that could belong to any brand in any industry
  scores lowest. Specific-to-your-archetype beats pretty-but-anonymous.
- **The brief must connect to the design.** A brief the logo and palette ignore is a wasted page —
  the video shows tracing each design choice back to a brief field.
- **Mood boards need RATIONALE, not just pretty pictures.** Every color has a hex + a reason; every
  inspiration image gets a one-sentence "why it belongs." "Just pretty pictures" is a named pitfall.
- **Wireframes are UX, not visual design.** Low-fidelity, structure and user flow — skipping UX
  thinking is a named pitfall. Don't polish; map the journey.
- **Adapt A6, don't rewrite it.** The brief is 2–3 sentences per field, pulled from A6.
- **The Madison +1 is judgment:** after generating logos/mood with AI, ask "does this actually look
  like the brand I described?" The pipeline gives options; YOU decide which is *true*. That decision
  is the +1 — the human-in-the-loop theme again.

## Series doctrine (every episode)

- **Assume zero design experience.** Define every term first time (creative brief, wordmark vs icon
  vs combination mark, clear space, mood board, hex, heading/body/accent font, wireframe, low-fi,
  information architecture, user flow). Never "just."
- **One deliverable per episode**, ending in the real artifact, with the paste-ready `nina` (or
  plain) prompt that generates options — then the "is it true to the brief?" pass.
- **ai-explainer bookends stay:** composer cold open → step-by-step body → verdict recap → Your
  Turn → title-restate outro. 16:9. Free pipeline. `"register": "Pragmatist"`.

---

## The episodes (build in this order)

### E1 — "The Creative Brief: One Page That Steers Every Design (Component 1, 20 pts)" (~5 min)
- **slug:** `claude-liam-a7v-01-creative-brief`
- **premise:** The brief is the filter for every visual choice that follows. Vague brief → vague
  design. Synthesize A6 into one page.
- **teach:** the six fields, 2–3 sentences each, pulled from A6 — **Brand Objective** (from the
  mission), **Target Audience** (2–3 segments from the positioning), **Key Message** (the UVP,
  copied **verbatim**), **Tone & Style** (from the personality traits + archetype), **Visual
  Direction** (2–3 sentences of mood, grounded in the archetype — this bridges to Component 2),
  **Success Metrics** (measurable, from the competitive positioning). Adapt, don't rewrite.
- **traps:** rewriting A6 strategy; vague fields; a brief the later designs ignore.
- **deliverable:** the one-page creative brief. Your Turn = `nina /brief` (or a prompt) that
  synthesizes the A6 deliverables into the six-field brief.

### E2 — "Logo Development: 4–5 Concepts + a Rationale (Component 2, logo)" (~6 min)
- **slug:** `claude-liam-a7v-02-logo`
- **premise:** A logo is a decision, not a lucky render — generate a few real directions, then
  defend one.
- **teach:** the three approaches — **wordmark**, **icon**, **combination mark**; create **4–5
  concepts** in Figma / Canva AI / Adobe Express; **document the iteration** (show the thinking);
  make **variations** that hold up small (mobile header) and large (billboard); write a clear
  **rationale for the final** — why this one, not the others, tied to the brief's archetype.
- **traps:** one concept, no exploration; a logo that dies at small size; no rationale.
- **deliverable:** 4–5 concepts + final + rationale. Your Turn = `nina /logo` (or a prompt) that
  proposes wordmark/icon/combination directions from the brief, then the "true to brief?" pick.

### E3 — "The Mood Board + Style-Guide Start: Color, Type, Style (Component 2, rest)" (~7 min)
- **slug:** `claude-liam-a7v-03-mood-and-styleguide`
- **premise:** The mood board is the visual world your brand lives in — and every piece of it has
  a reason.
- **teach:** **Color system** via **Coolors** — 2–3 primary + 2–3 secondary, each with a **hex code
  and a one-line rationale**; **Typography** — heading + body (+ optional accent), one or two fonts
  max, from **Google Fonts**, each with a written reason; **Visual style** — photography direction,
  illustration style, iconography; the **inspiration grid** — 8–10 curated images, each with a
  one-sentence "why it belongs." Then start the **style guide**: logo usage (sizing, clear space,
  placement) + color application (what goes where and why).
- **traps:** pretty pictures with no rationale; five fonts; colors with no hex/reason; no style guide.
- **deliverable:** the mood board + style-guide start. Your Turn = `nina /palette` + `/visual` +
  `/styleguide` (or prompts) drafting the color/type/style system from the brief.

### E4 — "Wireframe the Five Pages: Structure Over Polish (Component 3, pages + IA)" (~6 min)
- **slug:** `claude-liam-a7v-04-wireframes-pages`
- **premise:** Wireframes are the skeleton — where things go and why, not what they look like. Low-fi
  on purpose.
- **teach:** use **Figma wireframe kits**; build low-fidelity wireframes for **five pages** —
  **Homepage** (hero with the UVP prominent, nav, featured work/products, primary CTA), **About**
  (brand narrative + archetype, mission/vision/values, origin story, differentiation),
  **Portfolio/Products** (sample/feature layout, case-study framework, categorization),
  **Resume/Team** (timeline, skills/credentials, milestones), **Contact** (form, social, CTA).
  Teach **information architecture** — what belongs where and why.
- **traps:** visual polish instead of structure; skipping UX thinking; missing pages.
- **deliverable:** five low-fi wireframes. Your Turn = `nina /wireframes` (or a prompt) that drafts
  the page structures + IA from the brief and UVP.

### E5 — "Mobile, User Flow & the Platform Call (Component 3, rest)" (~5 min)
- **slug:** `claude-liam-a7v-05-mobile-and-platform`
- **premise:** A site isn't done as five desktop boxes — show the phone, the journey, and where
  you'll actually build it.
- **teach:** a **mobile-responsive homepage** wireframe (at minimum); **user-flow documentation**
  (how people move through the site); **interactive-element planning** (what responds to user
  actions); and a brief **platform comparison** — **Vercel v0 vs Framer AI vs Wix** — with a
  recommendation and why (this decision carries into A8's build).
- **traps:** no mobile frame; no user flow; a platform pick with no reasoning.
- **deliverable:** mobile homepage + user flow + platform recommendation. Your Turn = a prompt that
  maps the user flow and drafts the platform comparison for the student's project.

### E6 — "The Madison +1 & Ship It: PDF + Figma" (~4 min) — closer
- **slug:** `claude-liam-a7v-06-plus-one-and-submit`
- **premise:** Prove the human judged, then package it so A8 can pick it straight up.
- **teach:** the **Madison +1** — after generating logo/mood options with AI, ask "**does this
  actually look like the brand I described in my brief?**" and document the decision (the pipeline
  offers, you decide which is true). Then assemble the **PDF** (one-page brief, visual identity with
  rationale, all five wireframes incl. mobile homepage, platform comparison + recommendation) and
  the **Figma board** (labeled sections: brief summary, logo iterations, mood board, wireframes
  desktop + mobile, interactive annotations); submit **PDF to Canvas + Figma link**.
- **traps:** submitting AI output without the judgment note; a Figma board that's a pile, not
  labeled sections; assets A8 can't reuse.
- **deliverable:** the PDF + Figma board. Your Turn = "put your logo next to your creative brief —
  if it doesn't say what the brief says, that's the +1 decision to make before you export."

---

## Tight cut

Five-episode version: Brief (E1) · Logo (E2) · Mood + style guide (E3) · Wireframes all in one
(E4+E5) · +1 & ship (E6). The 6-episode cut is better because Component 3 (30 pts) needs the
desktop-pages and mobile/flow/platform work split for a beginner.

## Build order & mechanics

- Standalone ai-explainer reels, Pragmatist register, built into `<course-book>/youtube/`
  (or `brutalist-art/youtube/` — tell me the owning book slug). `nina` is the drafting engine for
  every component.
- Same pipeline: beat_sheet.json → PEDAGOGY (GATE P) → Kokoro am_onyx audio (free) → visuals →
  QC → BUILD-PROMPT.md. Re-verify Coolors / Figma wireframe-kit / Canva UIs at build; screens
  rebuilt natively.
- Series index: the full INFO 7375 arc is now mapped end to end — A1 (foundation), A2 (PRD), A3
  (data), A4 (intelligence), A5 (strategy) + A5A (interface) + A5B (recipe), A6 (brand strategy),
  the pitch midterm, **A7 visual identity (this)**, A8 (launch). A7's assets feed A8's website.
  Say the word and I'll stitch the **master INFO 7375 series index** (one ordered playlist, all
  assignments) and a resumable batch prompt to build the whole semester's how-to reels.
