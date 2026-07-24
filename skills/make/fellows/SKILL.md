---
name: fellows
description: >
  Fellow-showcase reels for Humanitarians AI — wrap a fellow's OWN video
  report (a .mov/.mp4 they recorded) in the Claude-branded bookends and ship
  it as an episode on @HumanitariansAI. The fellow-selected narrator asks
  Claude "I wonder what Humanitarians AI fellow [name] has been working on
  lately…", then
  summarizes the work in 2–3 beats (from the faster-whisper transcript +
  frames pulled from the report), the fellow's video then PLAYS AS IS, and the narrator
  reads Professor Bear's notes (feedback + next steps — human-signed, GATE N),
  a "Your turn" handoff invites the viewer to dig deeper with a prompt, and
  the standard Humanitarians AI outro closes. Use when the user types
  `fellows [video|folder]`, `fellow report`, `fellow showcase`, or drops a
  fellow's report video and asks to wrap/publish-prep it. Sibling of
  ai-explainer (same skeleton, different middle: the middle IS the fellow's
  video). Audio-first except the report beat (the report's own runtime is
  that beat's clock). The fellow chooses one persistent Kokoro voice. Never publishes.
---

# fellows — the Humanitarians AI fellow-showcase reel

A fellows video answers one question — *what has this fellow been building?* —
and lets the fellow answer most of it themselves. The reel is a frame around
their own report: the selected narrator sets it up, the report plays untouched, Professor Bear
responds, the viewer gets a prompt to go deeper. The skill's job is the frame,
never a re-edit of the fellow's work.

## The shared skeleton (a sibling of ai-explainer / cli-explainer)

Same Claude-branded bookends as the siblings; the MIDDLE is the fellow's own
video plus commentary around it:

1. **Beat 0 — the Claude composer** (`ClaudeComposerAsk`, COLD OPEN LAW).
2. **Middle — what differs:** 2–3 summary beats → the report AS IS → Professor
   Bear's notes.
3. **Second-to-last — "Your Turn"** (`greeting: "Your turn."`).
4. **Last — the STANDARD HUMANITARIANS AI OUTRO** (deliberate deviation from
   the siblings' title-restate outro — see OUTRO, below).

## Trigger

```
fellows [video-file | fellow-folder] [--fellow "Full Name"] [--project "Project Name"] [--out dir]
```

Also: "fellow report", "fellow showcase", "wrap [video] for Humanitarians".
Input is typically a raw recording dropped into `fellows/` (e.g.
`fellows/Causal Couture Phase 3 Report.mov`). If `--fellow` is not given and
the name is not in the filename or spoken in the transcript, ASK the human —
never guess a person's name (HONESTY, sharpened for people, per the
ai-explainer profile modifier).

## Persistent fellow voice

Each fellow chooses one Kokoro voice before the first report is generated and
keeps it across the whole report series. Store the choice in the fellow-level
README or profile and repeat the same `engine: "kokoro"` and voice ID in every
episode's metadata and narration beats.

When the fellow has not supplied a preference, use the name only as a starting
heuristic: female-coded names receive an `af_*` suggestion and male-coded names
receive an `am_*` suggestion. This is not an identity claim. The fellow's
explicit preference always overrides the heuristic. A later voice change is a
documented re-voice decision for the series, never a silent per-episode choice.

## Brand facts

| Slot | Value |
|---|---|
| Channel | `@HumanitariansAI` — folder chip and HAI logo bug on every beat (LOGO LAW; full-size on the outro). |
| Persona / voice | **Fellow-selected narrator** — one persistent Kokoro voice per fellow. Suggested default: `af_*` for female-coded names, `am_*` for male-coded names; the fellow's preference wins. Record `voice_policy`, `voice_approval`, and the selected voice ID in the beat sheet. |
| Skin | Claude fidelity skin for the composer bookends (`tokens/claude.ts` — never retint); RESULT/notes graphics render in the **humanitarians palette** (`tokens/humanitarians.ts`) per ASK→RESULT LAW. |
| Register | Teardown-warm, celebratory-but-honest (the profile-modifier rule): make the fellow's invisible work visible; any skepticism points at the problem space, never at the fellow. Professor Bear's notes are the honest-feedback beat — that's where critique lives, and it is constructive by construction. |
| Output | `fellows/[first-name-last-initial]/[YYYY-MM-DD-short-weekly-description]/` — all lowercase kebab-case. |

## The required beat spine

```
B00  INTRO       ClaudeComposerAsk cold open. command = "I wonder what
                 Humanitarians AI fellow [Name] has been working on lately…"
                 — the ask lands ANSWERED (output lines: project name, phase,
                 one-line what-it-is). greeting: `Fellows, [Name]` (the
                 profile-modifier pattern — the subject takes the persona
                 slot; overrides the world-language hello). Narration: the selected narrator
                 introduces the report and fellow.
B01–B03  THE WORK   2–3 beats. The selected narrator summarizes what the fellow built — from
                 the transcript, one idea per beat. Visuals: frames pulled
                 from the report (Ken Burns; FELLOW'S-WORK carve-out, below)
                 and/or rebuilt graphics in the humanitarians palette.
                 SPARK-LINE LAW binds where composer chrome appears.
B04  THE REPORT  The fellow's video PLAYS AS IS — pass-through beat.
                 media/B04.mp4 is the transcoded report; its OWN audio and
                 OWN runtime are kept. No trimming, no retiming, no voiceover
                 (THE REPORT IS THE CLOCK, below). Brand bug stays (LOGO LAW).
B05–B06  PROFESSOR BEAR'S NOTES   The selected narrator reads Bear's notes — one beat of
                 feedback (what's strong, what to tighten), one of NEXT
                 STEPS. Notes-card visuals, humanitarians palette. The
                 narration frames it explicitly: "Professor Bear's notes —"
                 GATE N governs (below).
B07  YOUR TURN   HANDOFF LAW unchanged: ClaudeComposerAsk, greeting
                 "Your turn.", runningText "paste this into Claude…",
                 command = a prompt that digs into the fellow's topic, repo,
                 or method — read ALOUD and discussed, never just typed.
B08  OUTRO       The STANDARD Humanitarians AI outro (OutroSeries / OutroCTA,
                 humanitarians palette, content from AUTHOR.MD's
                 Humanitarians AI section). The selected narrator signs off consistently.
```

A **FELLOW CREDIT card** is required near the outro (on or beside B06): the
fellow's name, program/cohort, project name, and their public links VERBATIM
(GitHub, LinkedIn — only links that actually exist; never invent one).

## The transcript (whisper first, everything hangs off it)

Before any beat is authored, transcribe the report with **faster-whisper**
(the toolkit's caption engine — same pipeline as music-video / deck-lecture):

```bash
ffmpeg -i "[report].mov" -vn -ac 1 -ar 16000 transcript/report.wav
python3 -c "from faster_whisper import WhisperModel; ..."   # or the runtime caption script
```

Write `transcript/report.txt` + `transcript/report.srt`. The transcript feeds
FOUR things: (1) the 2–3 summary beats, (2) the draft of Professor Bear's
notes, (3) `description.txt`, (4) the report beat's caption track — the reel's
`.srt` splices measured narration windows around the report's own aligned
captions, so CC ships for the WHOLE episode including the fellow's segment.

**Screenshots:** pull stills for the summary beats with
`ffmpeg -ss [t] -i "[report].mov" -frames:v 1 media/B01.png` — pick frames
that show the WORK (the demo, the chart, the interface), not the fellow's
face mid-sentence.

## Laws — inherited, plus three of this skill's own

All ai-explainer house laws bind (LOGO, SHOW-DON'T-TELL, FILL-THE-CANVAS,
DOUBLE-CHECK, VISUAL QC, SPARK-LINE, COLD OPEN, ASK→RESULT, HANDOFF, GATE P,
never-publish). The fellows-specific law set:

- **THE REPORT IS THE CLOCK (the one exception to audio-first).** Everywhere
  else narration MP3s are the master clock. The report beat's clock is the
  report's own measured runtime; its own audio is muxed as-is. Transcode
  container/resolution to the reel spec (1920×1080 h264, letterbox — never
  crop or stretch), but never retime, trim, speed up, or talk over it. If the
  human wants a trimmed cut, that is an explicit request logged in
  BUILD-LOG.md — never the skill's own call.
- **SOUND REPAIR (the carve-out inside the carve-out).** "As is" protects the
  fellow's CONTENT and TIMING, not bad audio. If the report's sound is poor —
  quiet, clipped, hummy, roomy, wildly uneven — FIX IT in the transcode step,
  timing untouched: loudness-normalize to the reel's target
  (`ffmpeg -af loudnorm=I=-16:TP=-1.5:LRA=11`, two-pass), denoise
  (`afftdn`, or `arnndn` for stubborn hiss), high-pass the rumble/hum
  (`highpass=f=80`, plus a notch at 60/50 Hz if needed), and de-ess/limit
  clipping peaks. The MATCH rule is the point: the fellow's segment must sit
  at the same perceived loudness as the selected narrator's narration — a viewer should never
  reach for the volume knob at the splice. Never pitch-shift, never
  time-stretch, never re-voice. Every filter applied is logged in
  BUILD-LOG.md; if the audio is beyond repair (unintelligible passages),
  flag it to the human with timestamps instead of shipping a bad segment.
- **FELLOW'S-WORK carve-out (of REBUILD LAW).** Frames and clips from the
  fellow's own report play as THEMSELVES — like the ACTUAL-CODE LAW in
  cli-explainer, the fellow's artifact is the receipt; rebuilding it would
  falsify it. Everything that is NOT the fellow's own material (context
  diagrams, comparison charts, the notes cards) is rebuilt native, REBUILD
  LAW unchanged.
- **GATE N — Professor Bear's notes are BEAR'S words.** The skill DRAFTS
  `NOTES.md` (feedback + next steps) from the transcript, in Bear's plain
  register, as a starting point — but the notes beats never go to audio until
  Bear has edited or signed `NOTES.md`. The selected narrator reads them AS Bear's notes
  ("Professor Bear's notes—"), so shipping an unsigned draft is
  impersonation, not a shortcut. GATE N sits beside GATE P in the build
  prompt and is logged in BUILD-LOG.md.
- **HONESTY (people-sharpened, from the profile modifier).** Only claims the
  fellow's own report makes — never invent an accomplishment, metric, quote,
  credential, or link. Soft attributions stay soft. Log the source video
  filename, duration, and transcription date in SOURCES.md.

## Flow

1. **Transcribe** (free): faster-whisper → `transcript/`; pull candidate
   stills; measure the report's duration.
2. **Author** `beat_sheet.json` in the spine above + draft `NOTES.md` +
   `description.txt`. Metadata: `audience: "Humanitarians AI"`,
   `palette: "claude"` bookends / `humanitarians` results, `engine: "kokoro"`,
   `voice: "[fellow-persistent-kokoro-id]"`, `voice_policy:
   "persistent-fellow-selected"`, `voice_approval: "APPROVED | PENDING"`,
   `register: "Teardown-warm"`.
3. **GATE N** — Bear signs `NOTES.md`. (GATE P too if ElevenLabs was
   requested; the Kokoro default spends nothing.)
4. **Audio**: `python3 runtime/scripts/generate_audio.py [reel]` — narration
   beats only; B04 is pass-through.
5. **Transcode the report** into `media/B04.mp4` (letterboxed, own audio) —
   applying SOUND REPAIR here if the report's audio needs it (loudnorm always;
   denoise/high-pass as required; log filters in BUILD-LOG.md).
6. **Render + assemble**: Remotion beats via
   `runtime/scripts/remotion_scenes.py [reel]` (foreground), then
   `compile.py [reel]` — conform to audio everywhere, to the report's runtime
   on B04; splice the caption tracks.
7. **QC**: the frame-level VISUAL QC LAW pass (sample frames, 9-point rubric,
   `_qc/REPORT.md`) — check the letterbox, the bug placement over the
   fellow's footage, and caption legibility across the splice.
8. Ship `BUILD-PROMPT.md` beside the beat sheet, as every reel does. Human
   reviews; publishing (youtube-publisher, Fellows playlist on
   @humanitariansai) is a separate, human-authorized step.

## Naming

Fellow folder: lowercase `first-name-last-initial`, for example `maya-r`.
Episode folder: `YYYY-MM-DD-short-description-of-that-weeks-work`, for example
`2026-07-10-building-the-verified-data-gate`. Title pattern:
`What's [Name] Building? — [Weekly Work]` (or the report's own title if it is
better).
