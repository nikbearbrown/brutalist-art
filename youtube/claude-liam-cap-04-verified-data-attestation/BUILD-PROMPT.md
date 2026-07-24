# BUILD-PROMPT — claude-liam-cap-04-verified-data-attestation
# "Every Number Traces." | Reallocation Engine Capstone · E4 of 8
# Built: 2026-07-19 | Kokoro am_onyx | 380.4s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-cap-04-verified-data-attestation
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-cap-04-verified-data-attestation
python3 runtime/scripts/compile.py youtube/claude-liam-cap-04-verified-data-attestation --height 1080
open youtube/claude-liam-cap-04-verified-data-attestation/claude-liam-cap-04-verified-data-attestation.mp4
```

## Key decisions
- **Greeting**: Merhaba (Turkish) — E4 of 8.
- **Title**: "Every Number Traces." — the core attestation doctrine stated as a fact, not an aspiration.
- **Seven labels in B01**: record / script-output / local-evidence / external-source / model-inference / your-input / missing — the exact taxonomy from assignment Step 3. model-inference and missing as accent items (the ones most often mishandled).
- **Prediction gate (B03)**: asks consequence of ethics gate failure — reveals in B06 that the run is blocked, not warned. Hard-stop framing is what the gate is.
- **Self-demo**: `sed -n '113,130p'` on assignment — shows Step 3 with all seven labels and the ethics gate definition including "If either fails, the run does not happen." Real, free, no generation.
- **Three verbatim quotes across B05–B07**: Give/Keep table test (Ch 16), honesty gate (Ch 16), one-question test (Ch 3). Two from Ch 16, one from Ch 3 — the two chapters that define the attestation architecture.
- **B08 (THE_PICK)**: model-inference is the correct label, not a failure — the failure is calling model-inference a record. No verbatim quote (quote: "", cite: "").
- **MINOR-COSMETIC**: B04 ClaudeCodeBeat moderate slow-mo (known pattern, non-blocking).
