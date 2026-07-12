---
name: cubs
description: >
  Bear's Cubs — early-childhood concept films (ages 1–5): colors, shapes,
  numbers, basic categories. Built on the vox chassis (audio-first beat sheets,
  slot contract, Manim/geoplate visuals, QC gates) but governed by
  developmental-psychology constraints, not explainer doctrine: slow pacing,
  question-pause-confirm contingency, exemplar variability, music discipline,
  co-viewing prompts, age-band runtime caps. Gate K (scripts/kids_gate.py)
  validates every beat sheet BEFORE audio or render. Use when the user types
  `cubs`, `kids video`, or asks for a toddler/preschool concept video.
---

# Bear's Cubs — early-childhood concept films

One episode teaches ONE categorical concept (a color, a shape, a number) to one
age band. The design rules are research constraints, not style preferences —
each traces to a finding in `reference/pedagogy.md`. The pipeline reuses the
vox toolkit: `generate_audio.py` (per-beat mp3s; `"silent": true` beats ARE the
response pauses), `vox_compile.py` (slot contract), Manim/geoplates for the
visuals, Gates A/B/W — plus **Gate K**, the pedagogy validator that runs FIRST.

## The laws (each one is validated by Gate K)
1. **One host, camera-address.** The Bear Brown mascot is the recurring host
   across ALL episodes (video-deficit mitigation: consistency builds the
   parasocial relationship). Narration is second person ("you"), never
   narrator-about-a-scene.
2. **Pacing:** teaching beats run 4–9 seconds; at most ONE new visual stimulus
   per beat; background `static` (or `minimal`) during teaching. No sub-2s
   cuts, ever. Everything on screen that isn't the target is already-familiar.
3. **Contingency triad:** every concept gets question → PAUSE → confirm. The
   pause is a real `"silent": true` beat of 2–4 seconds — no music sting, no
   cutaway, nothing. The confirm works whether or not the child answered
   ("Yes! That's a circle!"). The pause is the mechanism; never fill it.
4. **Exemplar variability:** 3–5 exemplars per concept, varying on dimensions
   UNRELATED to the target (red apple, red firetruck, red sock — sizes and
   shapes differ, "red" is constant), ONE label word used verbatim every time
   (never "red" then "crimson" then "the warm color"), and exactly ONE
   contrast case near the end ("this is NOT red").
5. **Music discipline:** music appears only in ONE dedicated song beat, under
   15 seconds, reused VERBATIM across the series (a retrieval cue, not a new
   song per episode). Teaching and pause beats are unscored — silence is
   correct design, not a gap.
6. **Co-viewing close:** the final beat invites real-world action with an
   adult ("Find something round in your room and show a grown-up!"), not a
   passive sign-off. (AAP co-viewing guidance; also the differentiator from
   algorithmic filler.)
7. **Length + concept by age band:** `1-3` → ≤ 4:00 total; `4-5` → ≤ 8:00.
   Gate K holds the cap AND the concept map (colors for 1-2; big-three shapes
   from 2-3; small cardinality from 3-4; never drawing tutorials or numerals
   for the young band — reference/pedagogy.md). The 1-3 band is positioned as
   CO-VIEWED 24-36 months per AAP/WHO.
8. **Closed pose library:** host beats set `host_pose` from the eight named
   poses in `reference/characters.md` (wave/present/point/listen/celebrate/
   not/sing/bye — one per beat role). Same bear, same poses, every episode;
   a new pose is a series-level decision, recorded in characters.md first.
9. **Rewatchability:** design for the 10th viewing — no surprise-dependent
   beats. Same structure every episode is a feature.

## Beat sheet (shared schema + `role` and kids fields)
`metadata`: `slug, series, age_band ("1-3"|"4-5"), concept, label_word,
topic, host: "bearbrown"`. Each beat carries `role`: one of
`hello | anchor | teach | question | pause | confirm | recap | contrast |
song | return | coview`. The anchor (pure swatch before exemplars), recap
(spoken exemplar list, no montage), and return (target card at the close) are
the live-teacher moves; the question beat uses a NEW exemplar (retrieval with
transfer). Production grammar — gaze cueing, sentence-final double labels,
minimal-pair contrast, no pointing during choice questions — lives in
reference/pedagogy.md and is part of the plan review.
`teach` beats carry `exemplar {object, attributes}`, `new_stimuli` (≤1),
`background_motion`. `pause` beats are `"silent": true, "silence_s": 2–4`.
`song` beats carry `music_cue`. Visuals per beat use the vox shot system —
geoplates (big flat primitives on cream) are the house style; the mascot
composites from `bearbrown/` clips.

## The loop (per episode)
1. **Plan** — write `beat_sheet.json` per the laws. Folder:
   `books/kids/<series>/<slug>/` (kebab-case, one per episode).
2. **GATE K (free, blocks everything):**
   `python3 aspects/kids/scripts/kids_gate.py <episode>` — must PASS before
   audio. Fix the sheet, never annotate around a failure.
3. **Audio** — `generate_audio.py <episode>` (slow, warm voice settings;
   pauses generate as silence — spends credits on spoken beats only).
4. **Visuals** — geoplate SVGs / Manim scenes per beat; Gates A + W apply.
5. **Compile** — `vox_compile.py`; mascot host beats composite from
   `bearbrown/`; review MP4 for the human.
Never bypass Gate K. An episode that fails pedagogy does not get a voice.


## SONG MODE — music videos, 100% Midjourney
For song episodes (the family band): lyrics in, MJ video clips out, the song
as the only audio track. Inputs in the episode folder
(`books/kids/songs/<slug>/`): `lyrics.txt` (TITLE:/ARTIST: header + one line
per line), `characters.json` (token registry with GitHub-raw refs — see
reference/star-tokens.md), `style.json`, and `song.mp3` when ready.

1. **Segment:** `python3 aspects/kids/scripts/song_prompts.py <episode>` —
   groups the lyric into ~16-word beats (V01…), writes the beat-sheet
   skeleton + PROMPTS.md with scene placeholders.
2. **Author scenes:** the builder writes one `scene` per beat in
   beat_sheet.json — concrete objects, RECURRING MOTIFS (the same card, tile,
   tower across the film), character [TOKEN]s where they belong. NEVER ask
   Midjourney to render words: scribble-line cards and single glyphs at most;
   real text comes from the caption plane. Rerun the script → final
   PROMPTS.md (each beat carries only the refs its scene uses).
3. **Volunteers (the pick gate):** paste each block, generate grids, reject
   against the identity anchors, pick the keeper, animate it (MJ
   image-to-video), download, rename `V##-<anything>.mp4`, drop in `pantry/`.
4. **Build:** pantry intake strips the clips' audio (the SONG is the only
   track); beat timings come from forced alignment of the lyric against
   song.mp3 (the lyric-match discipline); `vox_compile` conforms each clip
   (center-cut / slow-to-fit, replace_log for extremes) and compiles with
   `--audio song.mp3`. Karaoke captions ride as CC, never a second cut.

Gate K's concept laws (exemplar sets, pause triads, co-viewing) do NOT apply
to song mode; the pacing laws still do — no sub-2s cuts, one scene per beat,
and the identity law (identity-stable, boil is the medium) governs every
generation. Worked example: `books/kids/songs/godel-unprovable-truths/`.