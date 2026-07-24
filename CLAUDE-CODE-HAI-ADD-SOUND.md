# Claude Code Prompt — Add Sound to Silent HAI Videos (Kokoro, free)

The HAI videos rendered SILENT — their narration mp3s were never generated, so the
audio-first pipeline composited silence. This generates the free Kokoro narration
(the reel's assigned HAI voice — Liam `am_onyx` or Kore af_kore), re-renders at 4K so the
sound composites in, and overwrites the silent copy in `TMP/hai`. Unattended, FREE
only — never ElevenLabs, never publishes.

Run three of these in parallel — one per channel; each touches a different catalog
and TMP subfolder, so they don't conflict.

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books`

Paste the whole block below — nothing to edit.

```text
Add sound to every silent HAI video. Unattended batch: no approval pauses, reels
independent, one failure never stops the batch. FREE ONLY — Kokoro via
generate_audio_kokoro.py; NEVER ElevenLabs, NEVER generate_audio.py, NO publish,
NO git commit or push.

READ ONCE BEFORE THE BATCH
- brutalist-art/runtime/scripts/generate_audio_kokoro.py   (the free voice engine)
- brutalist-art/runtime/scripts/run.sh                     (art run: renders + composites audio)
- SCRIPTS/morning_render.py                                (how the .md description is built)

WORK LIST
Every reel folder under books/humanitarians_html/youtube that has a rendered master (<slug>.mp4 in the
reel root, or mp4/<slug>.mp4) whose master has NO audio stream. Reels nest at
youtube/<topic>/<reel>/. Test for audio with:
  ffprobe -v error -select_streams a -show_entries stream=codec_type -of csv=p=0 <master>
Empty output = silent = in the work list. (<slug> = beat_sheet.json metadata.slug,
else the folder name.)

PER-REEL LOOP
1. VOICE SANITY. Open beat_sheet.json. Every beat must be engine "kokoro" with a
   Kokoro voice (am_onyx or af_kore). If ANY beat is engine "elevenlabs", SKIP the
   reel and log NEEDS-CONVERT (run the HAI converter first) — never call a paid engine.
2. GENERATE AUDIO (free):
   python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py <reel>
   Writes mp3/beat-<ID>.mp3 per beat and updates the beat durations (audio-first).
   If it reports a missing Kokoro model/voices file, STOP the whole batch and say so
   (one-time setup: download voices-v1.0.bin per the script header) — never fall back
   to any paid engine.
3. RE-RENDER at 4K so the audio composites in (skip authoring gates — re-render of
   shipped content):
   ART_FACTS=0 ART_QC=0 bash brutalist-art/runtime/scripts/run.sh <reel>
4. VERIFY the fresh master now HAS an audio stream AND reads 3840x2160. If still
   silent, log FAILED(still-silent) and continue.
5. RE-STAGE: copy the fresh master over the silent one in TMP/hai:
   cp <reel>/<slug>.mp4  books/TMP/hai/<the filename already there>.mp4
   (match the existing TMP/hai filename, which may carry a book__ prefix). Leave the
   .md sidecar as-is — only the video changed.
6. LOG one line: reel, audio-added?, resolution.

GUARDRAILS
- FREE ONLY. Never engine "elevenlabs", never generate_audio.py (the paid script).
- Idempotent: reels whose master already has audio are SKIPPED.
- No publish, no git.

FINISH
Write ADD-SOUND-LOG-hai.md at books/TMP/hai: totals, fixed, skipped(has-audio),
skipped(needs-convert), failed(reasons). Then STOP.
```
