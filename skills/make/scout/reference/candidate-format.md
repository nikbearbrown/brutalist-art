# Candidate Card Format (vox)

Every candidate uses this exact schema — it supersedes the bears-doodles card
for vox builds. SLATE-RUNNER's Plan step reads these fields; do not rename,
reorder, or drop any. One blank line between cards. Cards live in
`<book>/youtube/video-ideas.md`.

## Template

```
## Candidate NN — <Title as a "Why ..." or surprising statement>
- Source: `<book>/chapters/<file>.md`
- Topic: <the on-screen kicker string, e.g. COMPUTATIONAL SKEPTICISM — the topic, never the book title, never a chapter number>
- Hook: <one sentence — the tension/paradox, no visual required>
- Key case: <the cold open — ONE concrete instance of the mystery, something specific happening, shown not summarized>
- The Question: <gap formula — "X should predict Y. Here is the case where it didn't. Why?" — this becomes the mandatory QUESTION beat, on screen and in narration>
- Core idea: <one sentence — the mechanism that resolves the question>
- Visual object: <the single thing on screen the whole film orbits>
- Manim move: <one verb from the move vocabulary in selection.md>
- Example seed: <a simple, realistic, MADE-UP instance for THE EXAMPLE act (16:9 only) — small concrete numbers/names, walked end to end; labeled illustrative at build time>
- Length band: <~1 min | 2–3 min | 3–5 min — derived from the arc; if the honest treatment exceeds 5:00, SPLIT into two cards each with its own Question>
- Still lanes: <geo | c2v | raster — suggested lane per fill-in still; geo for abstract mechanism plates, c2v for figurative flat-style objects, raster only for photographic-feel/faces/archival>
- Prerequisites: <comma-separated concepts the viewer must already have>
- Exclusions: <specific rabbit holes to NOT include — derivations, formalisms, second examples, history>
- Score: <N>/10
```

The builder appends `- Watch: \`open /abs/path/<slug>-review.mp4\`` at Done —
the scout never writes it.

## Worked example (the standard to match)

```
## Candidate 08 — Why Two AIs Checking Each Other Is One Blind Spot Twice
- Source: `computational-skepticism-for-ai/chapters/13-accountability-who-is-responsible-when-the-system-fails.md`
- Topic: COMPUTATIONAL SKEPTICISM
- Hook: Adding a second AI to check the first feels like a safety net.
- Key case: A generator writes a confident, subtly wrong claim; the checker model reviews it and passes it; it ships.
- The Question: A second checker should catch what the first one missed. This one caught nothing. Why?
- Core idea: Common cause failure — a checker trained on the same data with the same architecture has correlated blind spots, so the exact error most likely to fool the generator sails through the monitor too.
- Visual object: Two sieves with holes in the same place, and the one bad grain that falls through both
- Manim move: compare
- Example seed: Your team runs 200 AI-drafted contract summaries through an AI reviewer built on the same base model; it flags 9 typos and zero of the 6 hallucinated clause numbers a paralegal later finds.
- Length band: 3–5 min
- Still lanes: geo (aligned-holes plate), c2v (foundry/factory object if needed)
- Prerequisites: what a language model is (roughly), the idea of redundancy
- Exclusions: no Gödel incompleteness formalism, no seven-tier taxonomy, no chain-of-thought-monitoring literature, no FDA/aviation case histories beyond one spoken aside
- Score: 9/10
```

## Field notes
- **Title** — a "Why …" question or counterintuitive claim; the film's spine and often the thumbnail line. Never a textbook-section name.
- **Topic** — what the B01 kicker and endcard show. Topic, not book. One string per book, decided once (`metadata.topic` at build).
- **Hook vs Key case vs The Question** — the hook is the *tension in words*; the key case is the *concrete instance shown* in the cold open (a specific thing happening to a specific someone/something); the Question is the *gap formula* the film exists to answer. If you cannot write all three distinctly, the concept is not ready — that is SLATE-RUNNER's "plan bug" caught at scout time.
- **Example seed** — the builder expands this into THE EXAMPLE act (1–3 beats right before RECAP, 16:9 only; the 9:16 drops it). Invented but plausible; small numbers a viewer can count.
- **Length band** — derived, never chosen. Band, not promise: the beat sheet's audio decides. Over 5:00 honest = split NOW, at card time, each half with its own Question.
- **Still lanes** — a suggestion that seeds SHOTLIST/PROMPTS lanes; the builder may override.
- **Exclusions** — specific, not generic; they bound the QUESTION. "no Bayes formula, no odds-form shortcut" beats "keep it simple."
- **Score** — per selection.md rubric; order cards highest first.
