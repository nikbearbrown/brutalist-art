# BUILD-LOG — installs
# append-only — every command, error, fix, MISSING:, and final result

## Session start: 2026-07-12

---

### SETUP

- Directories created: media/, manim/, mp3/, pantry/, images/
- Read: beat_sheet.json (15 beats: B00–B13, B99)
- Read: docs/Installs.md (source doc)
- Read: runtime/README.md
- Read: runtime/manim/animated_graphics.py (teardown palette, library components)
- Read: runtime/remotion/src/scenes/* (BrutalistTerminalOpen, NikBearBrownCodeBlock, NikBearBrownTerminalAsk, BrutalistCommentCTA schemas)
- Read: runtime/remotion/src/Root.tsx (registered compositions, durationInFrames)
- Env: ELEVENLABS_API_KEY=<set> — narrated cut possible
- Env: ELEVENLABS_VOICE_NIKBEARBROWN=<set>

### BEAT SUMMARY

GRAPHIC/MANIM (9): B01 B03 B04 B06 B07 B09 B10 B11 B12
REMOTION (6): B00 B02 B05 B08 B13 B99

### PROP MAPPING (beat sheet intent → component schema)

- B00 BrutalistTerminalOpen: command ✓, checklist ✓, topic="SET UP ONCE"
- B02 NikBearBrownCodeBlock: code ✓, language="bash" ✓, caption ✓
- B05 NikBearBrownCodeBlock: code ✓, language="bash" ✓, caption ✓
- B08 NikBearBrownTerminalAsk: command ✓, output[] ✓, segment="PYTHON VENV", runningText="checking dependencies…"
- B13 NikBearBrownTerminalAsk: command ✓, output[] ✓, segment="KEY CHECK", runningText="validating keys…"
- B99 BrutalistCommentCTA: title→code (comment lines), handle→code, url→code, variant="A", topic="SET UP ONCE"

