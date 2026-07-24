# BUILD-PROMPT — claude-liam-cap-08-video-and-submit
# "Leave the Error In." | Reallocation Engine Capstone · E8 of 8
# Built: 2026-07-19 | Kokoro am_onyx | 284.4s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-cap-08-video-and-submit
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-cap-08-video-and-submit
python3 runtime/scripts/compile.py youtube/claude-liam-cap-08-video-and-submit --height 1080
open youtube/claude-liam-cap-08-video-and-submit/claude-liam-cap-08-video-and-submit.mp4
```

## Key decisions
- **Greeting**: Salve (Latin) — E8 of 8, the finale.
- **Title**: "Leave the Error In." — the counterintuitive doctrine that defines Step 7's honest-footage standard; the most memorable single instruction in the assignment.
- **Prediction gate (B03)**: asks what to do when the contribution errors on camera — reveals in B06 that the correct move is leave it in and narrate the fix; that footage is better than a clean take.
- **Self-demo**: sed showing Step 7 requirements directly — the leave-the-error-in rule and the screen-capture requirement are the two most operationally specific lines. Real, free, no generation.
- **Three verbatim quotes across B05–B07**: all from assignment Step 7 — no-cut definition, leave-the-error-in doctrine, screen-capture-not-pasted-output rule. All three are Step 7's operational standards; all three from the same primary source.
- **B08 (THE_PICK)**: the no-cut doctrine as the restriction that proves depth — if you cannot narrate an error in real time, you do not own the fix. No verbatim quote.
- **Runtime**: 284.4s (4m44s) — thematically within the 3–6min assignment requirement for the video itself.
- **MINOR-COSMETIC**: B04 ClaudeCodeBeat very short (3.2s — 6-word narration); BOUT 0.8s; SKIN LINT B03 false positive on ClaudeComposerAsk sparkLine (non-schema field). All non-blocking.
