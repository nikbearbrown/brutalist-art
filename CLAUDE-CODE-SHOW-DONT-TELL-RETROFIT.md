# Claude Code Prompt — SHOW-DON'T-TELL Retrofit (upgrade built videos to show, not tell)

The claude-explainer skill now carries the SHOW-DON'T-TELL LAW: if the
narration describes something that can move, the beat must SHOW it moving,
synchronized to the voiceover. Videos built before the law tend to have
"telling-only" beats — a static card or title on screen while the voice
describes a mechanism, a number, a comparison. This prompt audits built
videos beat by beat and rebuilds the offenders as animations that enact the
narration — WITHOUT touching the audio.

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Replace TARGETS with one or more built video folders (e.g.
`youtube/claude-liam-off-switch-gram youtube/hai-fellows/<slug>` — or `youtube/`
to sweep everything), then paste.

```text
TARGETS = <one or more built video folders under youtube/, space-separated>

Retrofit the built videos in TARGETS to comply with the SHOW-DON'T-TELL LAW
in skills/make/ai-explainer/SKILL.md (House laws): wherever the narration
describes something that CAN move, the beat must SHOW it moving, synchronized
to the voiceover. Free pipeline only: no ElevenLabs, no higgsfield, no
publishing, no git commit or push. Run without approval pauses.

READ FIRST
- skills/make/ai-explainer/SKILL.md  (House laws: SHOW-DON'T-TELL,
  REBUILD, LOGO, VISUAL QC — plus ILLUSTRATE LAW and SPARK-LINE LAW)
- skills/make/explainer/MOTION.md        (signaling principle: reveals land
  on the spoken word)
- runtime/remotion/src/tokens/claude.ts and layout.ts (SAFE constants)
- Each target's beat_sheet.json and SOURCES.md

HARD CONSTRAINT — THE AUDIO IS FROZEN
Do NOT regenerate, re-cut, or re-time any narration audio. The per-beat MP3s
are the master clock. Every fix happens inside the beat's existing duration:
you are replacing WHAT IS ON SCREEN, never what is said or when.

STEP 1 — AUDIT EVERY BEAT (per video)
Read the beat sheet and, for each beat, put the narration text next to what
the beat actually renders (read the scene code; sample a mid-beat frame with
ffmpeg if unsure). Classify:
- SHOWS: the visual enacts what the words say, timed to them. Leave it.
- TELLS: the narration describes motion, mechanism, growth, comparison,
  sequence, or change — but the screen holds a static card, a title, bullet
  text, an unrelated visual, or a graphic that appears fully-formed instead
  of performing what is being described. Flag it.
- EXEMPT: nothing in the line can move (pure judgment line, breathing beat,
  the composer bookends, the outro). Leave it.
Write the audit to <video>/_std/AUDIT.md: beat id | narration gist | what's
on screen now | SHOWS / TELLS / EXEMPT | planned fix for every TELLS row.

STEP 2 — REBUILD THE "TELLS" BEATS
For each flagged beat, build the animation that ENACTS the sentence, using
the skill's toolkit (C2 rhetorical patterns, C3 concept illustrations, Manim
fragments, or a custom Remotion scene on the cream stage):
- A number the voice says grows/shrinks → the bar/counter grows AS the words
  land, arriving at the value on the spoken figure.
- A process or pipeline being described → stages light up in narration
  order, one per phrase.
- A comparison → the two sides diverge on screen at the moment the contrast
  is spoken.
- A mechanism → it performs itself while being explained (parts move in the
  order the voice names them).
Time reveals to the words: use the beat's audio duration and, where the hit
must land mid-sentence, add sub_beats word-level timing rather than guessing
offsets. All House laws still apply: fidelity palette, one terracotta moment,
logo bug inside SAFE, only source-verifiable numbers on screen (check the
video's SOURCES.md before animating any figure — never invent data to make a
richer animation). Motion must enact the narration, not decorate it — do not
add wiggle to beats that were correctly still.

STEP 3 — RE-RENDER AND QC
Re-render only the changed beats, then recompile the video. Before
overwriting, copy the original mp4 to <video>/<slug>-pre-std.mp4 so the
before/after can be compared. Then run the full VISUAL QC LAW pass on the
new cut (frame sampling, 8-point rubric, _qc/REPORT.md, zero BLOCKER/MAJOR)
— new animation is exactly where overflow bugs breed.

STEP 4 — REPORT
Per video, append to _std/AUDIT.md: beats upgraded (with one line on what
each now shows), beats left as-is and why, QC result, and the old vs new
runtime (should be identical — the audio never moved). If a rebuilt beat
fails to render after two attempts, restore that beat's original visual and
log it — never ship a broken beat or a slate where a working visual existed.
End with a table across all TARGETS: video | beats audited | upgraded |
exempt | QC clean.
```
