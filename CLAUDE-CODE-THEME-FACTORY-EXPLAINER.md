# Claude Code Prompt — The Theme Factory Skill (16:9, claude-liam)

First live exercise of the **skill-teardown modifier**
(`skills/make/ai-explainer/SKILL.md`). Source: Anthropic's
`theme-factory` skill — `../anthropics/skills/skills/theme-factory/`
(SKILL.md + `themes/` with 10 theme spec files + `theme-showcase.pdf`).

The teardown thesis: the skill's product isn't the ten palettes — it's the
CONSENT GATE written into its own instructions. Show the showcase, ask,
WAIT for explicit confirmation, only then apply. A skill that automates
consistency while forbidding itself from automating taste.

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace. Free pipeline only.

```text
Build one 16:9 ai-explainer video on Anthropic's theme-factory skill
under the skill-teardown modifier — the shipped instruction folder that
styles any artifact with one of 10 pre-set themes, but only AFTER a
mandatory human choice. The reel's visuals are the argument: one artifact
re-skinned LIVE through the themes — same plate, different prints, for
design systems. claude-liam channel. Free pipeline only: Kokoro voice, no
ElevenLabs, no higgsfield, no publishing, no git commit or push. Run
without approval pauses (no paid spend is possible under these
constraints).

READ COMPLETELY BEFORE ACTING

- AGENTS.md
- CLAUDE-BRAND.md
- skills/make/ai-explainer/SKILL.md  (the skill-teardown modifier
  section governs this build — read it as law, this is its first exercise)
- skills/make/explainer/SKILL.md (and the MOTION.md / REMOTION.md it points to)
- skills/make/your-turn/SKILL.md (closing block contract)
- docs/remotion-best-practices/SKILL.md
- runtime/remotion/src/tokens/claude.ts
- ../anthropics/skills/skills/theme-factory/SKILL.md  (the source — read
  it whole, per modifier rule 1)
- ../anthropics/skills/skills/theme-factory/themes/*.md  (all 10 theme
  spec files — the demo's data comes from these, verbatim hexes only)

FORMAT

- 1920x1080 (16:9), 30 fps.
- Channel claude-liam: persona Liam (in for Bear), folder chip
  @NikBearBrown, voice Kokoro am_onyx, register Teardown.
- Audio-first: narration generated and measured per beat FIRST; every beat
  conforms to its audio. Length derives from the beats — expect 4–6 min.
- Suggested title: "Claude, Restrained" (series style: Claude Seeded,
  Claude Taught, Claude Scripted). Restate the skill name in the
  description.

THE STORY (Teardown register)

Hook: Anthropic ships a skill with ten color themes — and its most
important instruction is the one that stops Claude from using them. Before
a single hex code lands, the skill orders Claude to show a PDF, ask which
theme you want, and WAIT.
Act 1 — What a skill is (compressed for series viewers): a folder of
instructions Claude reads before working. This one is tiny: a 3 KB
SKILL.md, ten ~500-byte theme files, one showcase PDF. A design system
that fits in a tweet thread.
Act 2 — The anatomy: each theme file is 4 hex colors + 2 fonts + a
"best used for" line. That's the whole spec. Verbatim beat: Golden Hour —
Mustard Yellow #f4a900, Terracotta #c1666b, Warm Beige #d4b896, Chocolate
Brown #4a403a, FreeSans Bold / FreeSans.
Act 3 — The consent gate (the thesis): the four-step Usage Instructions —
1 show the showcase, 2 ask for their choice, 3 wait for selection, 4 apply.
Verbatim: "Get explicit confirmation about the chosen theme." Steps 2–3
automate NOTHING — they exist to forbid automation. The skill encodes a
division of labor: Claude owns consistency, the human owns taste.
Act 4 — The demo (SELF-DEMO LAW): one artifact — a single slide card —
re-skinned live through the themes. Same layout, same content, ten
identities. Then the meta wink: this video's own cream-and-terracotta
frame is the same trick — a fixed theme applied over variable content.
The reel obeys the law it's explaining.
Act 5 — The escape hatch + the caveat: "Create your Own Theme" — when
none of the ten fit, Claude generates a new theme, but the gate survives:
show it for review, THEN apply. Honest Teardown caveat: 4 hexes and 2
fonts is a palette, not a brand system — no spacing scale, no iconography,
and contrast governance is one line ("Ensure proper contrast and
readability") doing very heavy lifting.
Landing: the skill's real invention is the workflow, not the colors.
Consistency automated; choice preserved.

STRUCTURE (ai-explainer skeleton + your-turn closing)

- Beat 0 — ClaudeComposerAsk cold open. Liam: "Anthropic wrote a skill
  with ten color themes. The most important line in it… is the one that
  makes Claude stop and ask. This is Liam, in for Bear."
- Middle — the five acts, carried by the figures below. ASK→RESULT pairs
  for every demo (composer micro-beat with the real theme-factory
  invocation typed in, then the styled result).
- Closing per your-turn: VERDICT recap card → Your Turn composer beat →
  title re-read on the @NikBearBrown brand card.
- Your Turn suggested prompt (Liam reads it in full): "Here's my deck.
  Use the theme-factory skill: show me the showcase and let me pick —
  but before I choose, tell me which theme YOU would have picked for
  this content, and what that choice says about my audience."

FIGURES — the reel's visuals ARE the skill's own output

Palette law for this episode (modifier + REBUILD LAW): frame chrome,
labels, and annotations stay in the Claude fidelity palette with ONE
terracotta accent — but theme swatches and themed demo cards show the
TRUE hex values from the theme files. The theme colors are the DATA;
retinting them would falsify the source. Log every hex used in SOURCES.md
against its theme file.

FIGURE 1 — THE ANATOMY SHOT (Act 1)
  The skill folder as an ink-line tree: SKILL.md (3.1 KB) · themes/ (10
  files, ~520 bytes each) · theme-showcase.pdf · LICENSE.txt. Byte counts
  on screen (real values from ls). Terracotta ring on themes/.

FIGURE 2 — THE THEME CARD SPEC (Act 2)
  Golden Hour rendered as a museum spec sheet: four true-hex swatches
  materializing with their names and codes, font pairing line, "best used
  for" plaque. Every value verbatim from themes/golden-hour.md.

FIGURE 3 — THE CONSENT GATE (Act 3; the thesis diagram)
  Four-node pipeline: SHOW → ASK → WAIT → APPLY. Nodes 1 and 4 are
  Claude-colored (machine work); nodes 2–3 carry the terracotta accent
  and a human silhouette (human work). The WAIT node pulses with the
  narration. Verbatim caption: "Get explicit confirmation about the
  chosen theme."

FIGURE 4 — SAME DECK, TEN SKINS (Act 4; the centerpiece)
  One slide card (title + two bullets + a small chart) re-skinned live
  through all 10 themes in sequence — Ocean Depths, Sunset Boulevard,
  Forest Canopy, Modern Minimalist, Golden Hour, Arctic Frost, Desert
  Rose, Tech Innovation, Botanical Garden, Midnight Galaxy — each with a
  gallery name plaque, ~3–4 s per theme, transform-don't-cut (colors and
  fonts morph, layout never moves). True hexes from each theme file.
  Precede with the ASK micro-beat: the composer typing "Style this slide
  with theme-factory." and the showcase appearing as the RESULT.

FIGURE 5 — THE FIXED-THEME MIRROR (Act 4 close; one breath)
  The demo card re-skins one more time — into THIS video's own cream /
  ink / terracotta — and the frame around it highlights: the reel's skin
  revealed as an eleventh theme. Spark line: "You're watching one."

FIGURE 6 — THE ESCAPE HATCH (Act 5)
  ASK→RESULT: composer types a custom-theme request ("None of these fit —
  generate a theme for a brutalist typography channel: cream paper, warm
  ink, one terracotta accent."). RESULT: a new theme card assembles in the
  skill's own spec format — then a review chip appears BEFORE it applies
  (the gate survives even for generated themes).

FIGURE 7 — THE ONE-LINE LAW (Act 5; the caveat)
  The sentence "Ensure proper contrast and readability" alone in serif,
  then a live contrast meter runs under three theme swatch pairs (true
  hexes, computed WCAG ratios shown as real numbers) — one passes large-
  text only, narration lands the caveat: a palette is not a brand system,
  and one sentence is not contrast governance.

FIGURE RULES

- Deterministic renders only; no screenshots, no screen recordings
  (SELF-DEMO LAW). The theme-showcase.pdf is NOT shown as an image — its
  content is rebuilt natively as Figure 4 (REBUILD LAW; caption once,
  small: "Redrawn from theme-showcase.pdf").
- Verbatim quotes on screen match SKILL.md exactly. Cite once per figure,
  small: "Source: Anthropic, theme-factory SKILL.md".
- Transform-don't-cut inside Figures 4–6.
- Any beat that cannot be built after two attempts becomes a labeled
  PIPELINE slate and is logged — never silently dropped.

OUTPUTS

- youtube/claude-liam-theme-factory/
  - beat_sheet.json
  - claude-liam-theme-factory.mp4 (1920x1080)
  - SOURCES.md — every verbatim quote with its SKILL.md line; every hex
    value mapped to its theme file; the computed WCAG ratios with the
    swatch pairs they came from.
  - BUILD-PROMPT.md (this prompt, per the build-prompt rule)
- QC per VISUAL QC LAW: sample frames at ≥2 fps plus 15/50/85% of each
  beat, READ the PNGs, audit the 9-point rubric, log to _qc/REPORT.md,
  re-render until zero BLOCKER/MAJOR.
- Verify the mp4 exists and plays (probe duration and frame count) before
  reporting done, and end with the beat → timestamp table.
```
