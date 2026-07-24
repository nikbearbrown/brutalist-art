# Claude Code Prompt — NBB-Wrap an Existing Body Video

## Meaning of `nbb <video path>`

When Bear says `nbb` followed by a path to any existing MP4, treat that MP4 as a finished **body**, then search for all media and production files belonging to that video. The MP4 does not have to be inside its original reel folder.

The required structure is:

```text
CLAUDE COLD OPEN — Liam frames the video's question and asks, “Can you explain it, Bear?”
UNCHANGED BODY — original body narration, media, timing, and edit
VERDICT / SUMMARY — new NBB Teardown synthesis
YOUR TURN — Claude composer with a useful viewer prompt
CLAUDE EXPLAINER OUTRO — title restatement and @NikBearBrown
```

Run Claude Code from `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`. Replace `SOURCE_VIDEO` and paste:

```text
SOURCE_VIDEO=/absolute/path/to/the/existing/video.mp4

NBB-wrap SOURCE_VIDEO and render the finished video. The source MP4 is an already-edited body. Preserve it. Do not reinterpret “nbb” as permission to rewrite, replace, regenerate, or restyle the body.

Read completely before acting:
- AGENTS.md
- skills/make/nbb/SKILL.md
- skills/make/ai-explainer/SKILL.md
- skills/make/explainer/SKILL.md
- runtime/voices/teardown/VOICE.md
- skills/make/audience-preset/brands/nbb.md
- docs/remotion-best-practices/SKILL.md

SOURCE AND MEDIA DISCOVERY — REQUIRED FOR EVERY VIDEO

Do not assume the MP4's immediate parent is the complete reel. Find the media for that specific video.

1. Resolve SOURCE_VIDEO to an absolute path and verify it exists with `ffprobe`.
2. Derive a search slug from its filename. Remove only known output suffixes such as `.mp4`, `-cut`, `-final`, `-final-cut`, `-review`, `-slate`, `-master`, `-short`, `-916`, and audience suffixes. Preserve the actual subject words.
3. Begin with the MP4's parent, then search its ancestors and siblings. Also search `/Users/bear/Documents/CoWork/bear-textbooks/books/` for:
   - directories whose name equals or contains the derived slug;
   - `beat_sheet.json` and `beat_sheet.*.json` whose metadata slug, title, output filename, or media references match the video;
   - MP4s with the same filename or SHA-256;
   - matching `media/`, `pantry/`, `manim/`, `clips/`, `mp3/`, `audio/`, `remotion-src/`, `scenes.py`, subtitle, transcript, QC, provenance, and source-sidecar files.
4. Read every candidate beat sheet. Follow all explicit `audio_file`, `shot.source`, `shot.remotion.rendered.out`, media, Manim, clip, subtitle, and provenance paths instead of guessing.
5. Rank candidates using direct evidence:
   - strongest: candidate contains SOURCE_VIDEO and a matching beat sheet;
   - next: matching metadata slug/output filename plus referenced assets;
   - next: matching video SHA-256 or exact basename plus a complete beat/media structure;
   - weakest: name similarity alone.
6. Choose one canonical SOURCE_REEL only when the evidence is unambiguous. Record every candidate and the selection evidence in `SOURCE-DISCOVERY.md`.
7. If several copies exist, use the newest complete production reel only when its beat sheet and assets demonstrably produce the supplied video. Do not mix media from different versions merely because their slugs resemble each other.
8. If the supplied MP4 is a detached copy in `TMP`, `Downloads`, or another review folder, locate its original production reel by hash, basename, metadata, duration, and beat structure.
9. If no beat sheet or source assets can be found, the supplied MP4 itself becomes the locked body. Do not invent or regenerate missing media. Wrap the intact MP4 and report that only the flattened body was available.
10. Inspect the selected SOURCE_REEL for `beat_sheet.json`, variant sheets, `mp3/` or `audio/`, `media/`, `pantry/`, `manim/`, `clips/`, subtitles, source sidecars, and QC artifacts.
11. Write `SOURCE-MEDIA-LOCK.md` containing every discovered source asset path, its role, byte size, SHA-256, dimensions, duration if applicable, and the beat ID it serves.
12. Treat SOURCE_VIDEO, SOURCE_REEL, and every discovered source asset as read-only. Never modify, rename, overwrite, move, delete, regenerate, recolor, crop, or replace them.

OUTPUT

Create a sibling audience directory:

`<source-parent>/nbb-<source-slug>/`

Required files:
- `beat_sheet.nbb.json`
- `SOURCE-DISCOVERY.md`
- `SOURCE-MEDIA-LOCK.md`
- `PEDAGOGY.md`
- `FACTCHECK.md`
- `QC-sheet.png`
- `<source-slug>-nbb.mp4`
- `BUILD-REPORT.md`

Never double-prefix the slug. Never modify SOURCE_REEL.

THE BODY-LOCK LAW

The source video already contains the body. The discovered reel explains how that body was made. The body must remain exactly as supplied.

- Preserve the original body narration word for word.
- Reuse the original body audio. Do not regenerate it in Liam, Bear, Kokoro, or ElevenLabs.
- Preserve every body beat in the same order.
- Preserve every body beat's duration and in/out timing.
- Preserve every supplied image, video, Manim render, screen recording, archive asset, annotation, crop, color, transition, and edit.
- Do not apply a new palette to the body.
- Do not shorten or lengthen body beats.
- Do not rebuild body beats from their raw `media/` files when conformed `clips/` already exist. Reuse the conformed body clips so the edit remains exact.
- If the source beat sheet and finished MP4 disagree, the finished MP4 is the authority for the body.
- Never report media as missing until the required workspace-wide slug, beat-sheet-reference, basename, and hash search has completed.
- Never silently omit discovered `media/`, `pantry/`, `manim/`, audio, subtitle, or provenance files from the variant's media ledger.
- The only source material that may be omitted is the source's existing outro/end card. Do not omit substantive final explanation merely because it is the last beat.
- Verify all source assets retain their original SHA-256.

HOW TO IDENTIFY THE BODY

- If `beat_sheet.json` exists, identify current outro beats by `act: OUTRO`, end-card/subscribe branding, or an explicit outro component.
- Preserve every beat before the current outro as body, including a source beat named INTRO if it contains substantive teaching.
- Remove only the current outro/end card from the new assembly.
- If beat boundaries are unavailable, inspect the source MP4 and source clips. Determine the old outro's exact start time, take the body as `[00:00, old-outro-start)`, and document the timecode.
- Never discard the opening teaching beat just because the source lacks a Claude cold open. The new cold open is added before the complete existing body.

NEW NBB WRAPPER — ONLY THESE BEATS ARE NEW

### 1. Claude cold open

- This is the first beat.
- Render with `ClaudeComposerAsk` in the fixed Claude fidelity skin.
- Voice: Liam, Kokoro `am_onyx`.
- Greeting: one short world-language hello followed by `Liam`.
- Liam briefly frames the central question already answered by the body. Do not answer it and do not summarize the body in advance.
- End Liam's narration with the exact sentence: `Can you explain it, Bear?`
- Composer command: a concise version of the video's real central question.
- The Claude result/output lines should hand directly into the first unchanged body frame.
- Keep this beat short: generally 6–10 seconds.

### 2. Unchanged body

- Insert the exact locked body after the Liam cold open.
- Keep its existing narrator, media, audio, timing, visual treatment, and subtitles.
- Do not place Claude chrome around it.
- Do not add generated overlays or new captions on top of it.

### 3. Verdict / summary

- Add one new beat immediately after the body.
- Voice: Bear/NBB using `ELEVENLABS_VOICE_NIKBEARBROWN`.
- Register: Teardown.
- State what the body demonstrated, the mechanism that made it work, and the most important trade-off or limit.
- Use only claims supported by the unchanged body and its beat sheet.
- Render as a concise `ClaudeWindow` artifact/verdict page in the Claude fidelity skin.
- This beat synthesizes; it does not repeat the whole body.

### 4. “Your turn” handoff

- This is the second-to-last beat.
- Render with `ClaudeComposerAsk`.
- Set `greeting: "Your turn."` exactly.
- Set `runningText: "paste this into Claude…"`.
- Type one useful, paste-ready prompt that lets the viewer explore or apply the body's central idea.
- Voice: Bear/NBB using `ELEVENLABS_VOICE_NIKBEARBROWN`.
- Do not use a generic subscribe prompt.

### 5. Claude explainer outro

- This is the final beat.
- Remove and replace the source's current outro.
- Render with `ClaudeTitleOutro` in the fixed Claude fidelity skin.
- Restate the episode title, poster-style.
- Handle: `@NikBearBrown`.
- Use a short subline derived from the verdict.
- Do not use the generic NBB mascot outro, `OutroCTA`, or the source outro.

VOICE AND AUDIO RULES

- Liam speaks only the new cold open with Kokoro `am_onyx`.
- The original body keeps its original audio exactly.
- Bear speaks only the new verdict and “Your turn” handoff using `ELEVENLABS_VOICE_NIKBEARBROWN`.
- The final title outro may be silent unless its scene specification requires a short Bear line.
- Run GATE P on only the newly written Bear narration before generating paid audio.
- Measure all new MP3s. New wrapper visuals conform to those MP3s; the body never conforms to new audio because its original audio is locked.
- Normalize assembly loudness gently at joins if required, but do not alter or replace the body track. No music bed may cover the body unless it was already present.

MEDIA PRESERVATION AND ASSEMBLY

- Prefer stream-copy or lossless intermediate extraction for the unchanged body segment.
- If one final encode is required, use one consistent high-quality encode for the complete assembly and document it. Do not recursively re-encode individual body beats.
- Preserve source resolution and aspect ratio. The new wrapper must match the body's canvas.
- Do not stretch, crop, letterbox, recolor, or retime the body to fit the wrapper. Make the wrapper fit the body.
- Keep and reuse the source subtitles for the body. Add subtitles only for new wrapper narration, with correct timestamp offsets.
- The new variant may copy or symlink source body clips, but checksum validation must prove the original files remain untouched.

UNATTENDED BUILD

1. Resolve the source video, perform the complete media search, and write SOURCE-DISCOVERY.md.
2. Inspect the chosen source reel and write SOURCE-MEDIA-LOCK.md.
3. Scaffold the namespaced NBB directory without altering the source.
4. Author `beat_sheet.nbb.json` with: cold open → locked body → verdict → Your turn → Claude title outro.
5. Write PEDAGOGY.md and FACTCHECK.md. Repair only new wrapper material until both end with `VERDICT: PASS`.
6. Generate Liam Kokoro audio for the cold open.
7. Generate Bear ElevenLabs audio only for the new verdict and handoff after GATE P passes.
8. Render only the new wrapper visuals.
9. Assemble the new wrapper around the locked body and remove only the old outro.
10. Generate a QC contact sheet containing the cold open, representative frames from every body beat, verdict, handoff, and outro.
11. Compare the new body's frames and audio against the source. Apart from a single unavoidable final assembly encode, they must be perceptually and temporally identical.
12. Verify the final with ffprobe: expected dimensions, audio present, non-trivial file size, and duration equal to new cold open + locked body + verdict + handoff + outro.
13. Open the final MP4 for human review.

BUILD REPORT

Write BUILD-REPORT.md with:
- source video and source reel
- SOURCE-DISCOVERY.md path, candidates considered, and why the selected reel belongs to this video
- all discovered media, pantry, Manim, clip, audio, subtitle, and provenance locations
- exact old-outro removal timecode or removed beat IDs
- locked body duration
- body beat IDs and reused clip/audio paths
- source SHA-256 verification result
- new cold-open question and Liam audio path
- new verdict narration and Bear audio path
- “Your turn” prompt and Bear audio path
- final outro title and subline
- final MP4 path, duration, dimensions, audio-stream status, and file size
- PEDAGOGY and FACTCHECK verdicts
- QC sheet path
- any unavoidable re-encode
- ready-to-paste command: `open /absolute/path/to/<source-slug>-nbb.mp4`

Do not claim success unless the final MP4 exists, passes ffprobe, and the source files still match their original SHA-256 values. Never publish or push.
```

## Matter-waves example

```text
nbb /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/vox-matter-waves/vox-matter-waves.mp4
```
