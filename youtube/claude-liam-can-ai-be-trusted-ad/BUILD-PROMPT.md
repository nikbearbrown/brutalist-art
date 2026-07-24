# BUILD-PROMPT — claude-liam-can-ai-be-trusted-ad · "The Ad That Answered Itself"

**GATE P: SIGNED** (Bear, 2026-07-21 — "go"). Audio spend approved: Kokoro `am_onyx`,
free/local. Never ElevenLabs, never publish, never git push.

Run Claude Code from `~/Documents/CoWork/bear-textbooks/books/brutalist-art`
(typically `claude --dangerously-skip-permissions`), then paste the prompt below.

```text
Build the reel youtube/claude-liam-can-ai-be-trusted-ad/ end to end. GATE P is
already SIGNED (see NARRATION-GATE-P.md in the folder) — generate audio without
pausing for approval. Free pipeline only: Kokoro am_onyx, no ElevenLabs, no
higgsfield, never publish, no git commit or push.

READ FIRST
- skills/make/ai-explainer/SKILL.md — note the REWRITTEN SHOW-DON'T-TELL LAW:
  it now binds at authoring time; every body beat in this reel carries a
  `show` block (ordered visual events with `at` fractions). The show blocks
  are the approved shot list — build them, don't reinterpret them.
- CLAUDE-BRAND.md (fidelity palette, one terracotta accent, EB Garamond,
  Title Case segments, spark-line law, logo bug per LOGO LAW)
- youtube/claude-liam-can-ai-be-trusted-ad/beat_sheet.json (9 beats, show
  blocks, verbatim on-screen evidence), SOURCES.md (every quote verbatim by
  handle — on-screen text must match EXACTLY), NARRATION-GATE-P.md,
  slate-previz.html (open it — the animated slate IS the approved previz;
  match its staging beat for beat)
- youtube/claude-liam-sycophancy-to-subterfuge/ as the schema exemplar

STEP 1 — AUDIO (the master clock)
python3 runtime/scripts/generate_audio.py youtube/claude-liam-can-ai-be-trusted-ad/
(Kokoro am_onyx per the beat sheet). ffprobe every mp3 and write
actual_duration_s into beat_sheet.json. Do not touch the narration text.

STEP 2 — SCENES (build the show blocks, timed to the words)
Frames per beat = ceil((mp3 + 0.4s) * 30). Map each show event's `at`
fraction onto the beat's REAL duration; where a hit must land mid-sentence
(B03's sort on "sort themselves", B04's strike on "fixes the question"),
derive sub_beats word timing from the mp3 (faster-whisper) rather than
guessing. Five new concept scenes on the cream stage, one terracotta moment
each, all evidence text VERBATIM from SOURCES.md:
- AdQuestionChain (B01): the ad's own questions land as grain polaroid cards,
  one per phrase; a ghost "?" fades in behind at ~0.72; spark line last.
- ReactionSplit (B02): verbatim comment cards drop in — praise left-tilted,
  attacks right-tilted; a counter climbs to 99+; spark line.
- JoyDreadSplit (B03): six labeled frame-cards enter mixed, then SORT on the
  spoken cue — warm left under "NO AI IN IT", ominous right under "THE AI";
  left glows cream, right dims to ink; @bong-garcia card stamps; spark line.
- WrongQuestionSwap (B04): "Can AI be trusted?" full-frame serif; terracotta
  strike draws through "AI" ON the spoken word; "the companies building it"
  types into the gap; @BenGrimm977 card slides up; spark line.
- HumanPianoBeat (B05): live piano waveform animates throughout; track-ID
  comment chips ping in; track card (Duval Timothy — "Ball" (2017) · Apron
  Records) flips up; stamp "recorded 9 years before the ad"; spark line.
Standard scenes: ClaudeComposerAsk for B00 (type-on + send arms + the three
RESULT lines landing per COLD OPEN LAW) and B07 (greeting "Your turn.",
type-on, runningText "paste this into Claude…"); ClaudeVerdictArtifact for
B06 with lines revealing ONE PER SPOKEN PHRASE (never pre-loaded);
ClaudeTitleOutro for B08. Logo bug on every beat inside SAFE.

STEP 3 — ASSEMBLE + QC
Conform and compile to youtube/claude-liam-can-ai-be-trusted-ad/
claude-liam-can-ai-be-trusted-ad.mp4 (and the -slate.mp4 cut). Then the full
VISUAL QC LAW pass: ffmpeg frame sampling (≥2 fps plus each beat at
15/50/85%), READ the PNGs, 9-point rubric, log to _qc/REPORT.md, fix root
causes and re-render until zero BLOCKER/MAJOR. Also verify against
slate-previz.html that every show event actually fires and lands near its
spoken cue, and audit the finished cut against the PPT TEST: if any body
beat plays as a static slide while the voice talks, rebuild that beat.

STEP 4 — REPORT
Per-beat mp3 durations, total runtime, QC findings, and the output paths.
Update SOURCES.md build section. Then STOP — do not publish, do not start
another reel.
```
