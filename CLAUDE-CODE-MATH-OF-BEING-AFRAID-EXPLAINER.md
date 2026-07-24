# Claude Code Prompt — The Math of Being Afraid Together (16:9, claude-liam)

Source: Zebonastic (Substack) — "The Math of Being Afraid Together," by Seth
Brown & Humanitarians AI, May 17 2026.
https://zebonastic.substack.com/

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace. All facts and the
equation are embedded — no web access needed.

```text
Build one 16:9 claude-explainer video on the Zebonastic essay "The Math of
Being Afraid Together" (Seth Brown & Humanitarians AI) — a step-by-step
PROOF of why co-op horror games work despite horror needing isolation.
claude-liam channel. The essay is an argument that builds one claim on the
last, culminating in an equation; the video must honor that chain — each beat
rests on the beat before it. Free pipeline only: Kokoro voice, no ElevenLabs,
no higgsfield, no publishing, no git commit or push. Run without approval
pauses (no paid spend is possible under these constraints).

READ COMPLETELY BEFORE ACTING

- AGENTS.md
- CLAUDE-BRAND.md
- skills/make/ai-explainer/SKILL.md
- skills/make/explainer/SKILL.md (and the MOTION.md / REMOTION.md it points to)
- docs/remotion-best-practices/SKILL.md
- runtime/remotion/src/tokens/claude.ts

FORMAT

- 1920x1080 (16:9), 30 fps.
- Channel claude-liam: persona Liam (in for Bear), voice Kokoro am_onyx,
  register Teardown. Do not use ElevenLabs.
- Attribution: this is a Zebonastic essay by Seth Brown & Humanitarians AI —
  credit them on screen at the open (small source chip) and in the outro. The
  channel handle is @NikBearBrown; the brand/outro card reads
  "Zebonastic · Seth Brown & Humanitarians AI".
- Audio-first: narration generated and measured per beat FIRST; every beat
  conforms to its audio. Length derives from the beats — expect 5–7 minutes.

THE STORY (Teardown register — it is a proof, not a tour; do not assert
anything the prior beat did not earn)

Hook / the paradox: horror is built on isolation. Strip away company, light,
certainty, and the nervous system does the rest. So putting a friend in the
room should BREAK the genre. It didn't — it became one of the most lucrative
formats in games. Phasmophobia: 23M+ copies. Lethal Company, one developer,
~$113.9M by January 2024. That gap is the thing to explain.
Step 1 — The axiom: fear is a measurable physical state — sympathetic nervous
system, heart rate, skin conductance, cortisol. Not a metaphor. And company
changes it: a trusted ally triggers social buffering — oxytocin down-regulates
the HPA axis, lowering cortisol. A friend makes terror objectively, chemically
less. The game hands the player a biological cheat code just by letting them
bring someone.
Step 2 — The complication: a group isn't one averaged mood; it's several
nervous systems wired together. Two effects the buffer alone misses:
context-dependence (co-op RAISES load during fiddly low-threat tasks —
coordination costs attention — so it reshapes fear's timing, flattening quiet
parts, concentrating spikes) and contagion (one player's panic transmits to
teammates who haven't even seen the threat). Now there's enough structure to
write it down.
Step 3 — The model (present the equation, treat it as a teaching scaffold):
  TPI = Ψ · (Hc/N) · (1 + β · Σ δij · e^(−λ·dij))
  Threat Perception Index rises with environmental stress Ψ and information
  deficit Hc; falls as nearby living players N rises and buffering β works;
  the key term is communication fidelity δij, decaying with distance dij at
  rate λ. Push players apart or put a wall between them and the denominator
  shrinks — TPI climbs. The craft line: "You don't design fear into a co-op
  horror game. You design the safety net, then spend the rest of development
  taking it away."
Step 4 — First application, the Alpha Hero Problem: arm the players (Leon,
Isaac, Doom Marine) and add co-op — N rises, δ stays high (stand back-to-back
and shoot), denominator balloons, TPI craters, it becomes a brawler. Patching
the numerator (less ammo) yields frustration, not fear. The fix is a different
premise: the SURVIVOR — weak, no real weapons, scavenge and escape; one
mistake drops N and spikes everyone at once. Horror comes from the players'
structural inability to fight back.
Step 5 — Three worked examples, each attacking a different term:
  • Phasmophobia attacks Hc (information deficit) — investigative loop, gather
    evidence, classify the entity; the weapon is knowledge. Its weakness the
    model predicts: deduction needs predictable entities, so Ψ is capped.
  • Lethal Company attacks δ (communication) — proximity voice chat where
    distance and walls degrade volume (λ·dij made audible); monsters like the
    Bracken and Coil-Head weaponize attention itself.
  • Haunt & Harvest (tabletop, Witchway Games) proves it's not about graphics
    — face-down drafting keeps Hc high and δ degraded with nothing but
    cardboard. Fear needs structural uncertainty, not polygons.
Step 6 — Where the model breaks (honest): players aren't rational nodes. The
bystander effect / volunteer's dilemma (Dead by Daylight). Dunning–Kruger and
rage-quits that spike TPI unpredictably. And no term for LAUGHTER — the
emergent comedy of spectacular failure, the release valve designers never
wrote. The fraction measures fear; it can't measure the joy of watching fear
go wrong.
Landing: trace the chain back to one fact about the body. Horror did need
isolation. Co-op horror didn't abandon that — it learned to MANUFACTURE
isolation on demand, inside a room full of people. The terror was never in the
monster. It was in the distance between you and the person who was supposed to
have your back.

STRUCTURE (claude-explainer skeleton)

- Beat 0 — ClaudeComposerAsk cold open. Liam poses the paradox: "Horror needs
  you alone. So why does putting your friends in the room sell tens of
  millions of copies?"
- Middle — the six steps as a visibly BUILDING proof (see figure beats). A
  running "proof spine" motif: each step pins a new card onto a vertical chain
  on the side, so the viewer sees the argument accumulate.
- Second-to-last — Your Turn composer beat, suggested prompt typed in:
  "Design a co-op horror mechanic that attacks the communication term."
- Last — outro card: title restated + "Zebonastic · Seth Brown &
  Humanitarians AI" + @NikBearBrown.

FIGURE / MOTION BEATS

FIG 1 — THE PARADOX & THE STAKES
  Left: a lone figure in a dark room, a fear-meter pegged high. Right: add a
  second figure — the meter DROPS. Then two sales facts stamp in: "23,000,000
  copies — Phasmophobia" and "$113.9M by Jan 2024 — Lethal Company, one
  developer." The contradiction is the terracotta moment: fear drops, sales
  soar.

FIG 2 — THE AXIOM (the body)
  A simple body diagram lighting up: heart rate up, skin conductance up,
  cortisol up under threat. Then a second figure appears beside it and an
  "oxytocin ↓ HPA axis ↓ cortisol" chain animates — the fear-meter eases.
  Label: social buffering. This is Step 1's card pinned to the proof spine.

FIG 3 — THE COMPLICATION (two effects)
  Split beat. (a) Context-dependence: a timeline of fear where co-op flattens
  the quiet stretches and sharpens the spikes — animate a solo curve morphing
  into a spikier co-op curve. (b) Contagion: three linked figures; one flashes
  panic and it propagates along the links to the others.

FIG 4 — THE EQUATION (centerpiece)
  Build TPI = Ψ · (Hc/N) · (1 + β · Σ δij · e^(−λ·dij)) term by term, each
  term fading in AS Liam names it, with a one-word gloss under each (Ψ =
  environment, Hc = what you don't know, N = friends nearby, β = the buffer,
  δ = can you hear each other, d = distance). Then DEMONSTRATE the mechanic:
  slide two player dots apart / drop a wall between them → the denominator
  visibly shrinks → the TPI value climbs (show it as a rising bar or gauge,
  not a fake decimal). Terracotta moment: the wall dropping and TPI spiking.
  Overlay the craft quote as it lands.

FIG 5 — THE ALPHA HERO PROBLEM
  Armed heroes stand back-to-back, N goes up, δ stays high, the TPI gauge
  collapses to near-zero — visually "the horror drains out," it becomes a
  brawler. Then swap to the SURVIVOR: weapons greyed out, one figure gets
  snatched, N drops by one, and every remaining gauge spikes in the same
  instant. Contrast is the whole beat.

FIG 6 — THREE GAMES, THREE TERMS (triptych)
  Three panels, each highlighting the term it attacks in the equation:
  Phasmophobia → Hc glows; Lethal Company → δ glows (show proximity voice as a
  volume arc decaying with distance / muffled by a wall); Haunt & Harvest →
  Hc high + δ degraded, rendered as literal face-down cardboard cards. Caption
  the through-line: "information and connection, not polygons." Reuse the same
  equation from FIG 4 so the shared fraction is unmistakable.

FIG 7 — WHERE THE MODEL BREAKS
  The clean fraction gets three "the equation has no term for ___" overlays
  stamped across it: hesitation (bystander effect / volunteer's dilemma),
  ego (Dunning–Kruger, rage-quit), and — the big one — LAUGHTER. End on the
  laughter card in the accent color: the fraction measures fear, not the joy
  of watching it go wrong.

FIG 8 — THE PROOF SPINE, COMPLETED
  The vertical chain of step-cards, now full, collapses back to the single
  bottom card: "fear is physiological, and company dampens it." Narration
  traces the whole argument back to that one fact, then the closing line about
  manufacturing isolation in a room full of people.

RULES

- Claude fidelity palette: cream #FAF9F5 page, warm ink #3D3929, terracotta
  #D97757 as the ONE accent per beat. EB Garamond segment titles, Title Case.
- This is NOT an Anthropic-research subject — it's a games essay — so the
  visual language is the Claude explainer skin, but the CONTENT is the essay's
  proof. The Claude UI appears only in the bookends (ILLUSTRATE LAW).
- Transform-don't-cut; the equation terms and the proof-spine cards MOVE and
  accumulate rather than hard-cutting.
- Numbers allowed on screen (verbatim from the essay): 23,000,000 copies
  (Phasmophobia); $113.9M by January 2024 (Lethal Company); 13 victory points
  (Haunt & Harvest). The equation exactly as written above. No invented stats.
- Do NOT present the TPI equation as established physics — Liam calls it a
  teaching scaffold, exactly as the essay does.

OUTPUTS

- youtube/claude-liam-math-of-being-afraid-together/
  - beat_sheet.json
  - claude-liam-math-of-being-afraid-together.mp4 (1920x1080)
  - SOURCES.md — every on-screen number, the equation, and the two verbatim
    quotes, each tied to the essay.
- Verify the mp4 exists and plays (probe duration and frame count) before
  reporting done, and end with the beat → timestamp table.
- If a figure animation fails to render after two attempts, replace that beat
  with a slate card naming it and log the failure — never silently drop it.
```
