# BUILD-LOG — what-is-brutalist
# append-only — every command, error, fix, MISSING:, and final result

## Session start: 2026-07-12

---

### SETUP

- Directories created: media/, manim/, mp3/, pantry/, images/, mp4/
- Read: beat_sheet.json (16 beats: B00–B14, B99)
- Read: animated_graphics.py (teardown palette, library components)
- Read: runtime/remotion/src/scenes/NikBearBrownTerminalAsk.tsx (schema: command, topic, segment, runningText — NO output prop yet)
- Read: runtime/remotion/src/scenes/NikBearBrownCodeBlock.tsx (schema: filename, segment, topic, code — hardcodes "python" label)
- Read: runtime/remotion/src/scenes/BrutalistTerminalOpen.tsx (schema: command, checklist, topic)
- Read: runtime/remotion/src/scenes/BrutalistCommentCTA.tsx (schema: filename, code, variant, topic)
- Env: ELEVENLABS_API_KEY=<set> — narrated cut possible
- Env: ELEVENLABS_VOICE_NIKBEARBROWN=<set>
- Manim: /opt/homebrew/bin/manim — available
- Remotion node_modules: not installed — will npm install

### PROP MAPPING (beat sheet intent → component schema)

- B00 BrutalistTerminalOpen: command ✓, checklist ✓, topic (default)
- B04 NikBearBrownCodeBlock: language→filename(.py), caption→segment, code ✓
- B10 NikBearBrownTerminalAsk: command ✓, output[] MISSING from schema → extending component
- B12 NikBearBrownTerminalAsk: same as B10
- B13 NikBearBrownCodeBlock: language="bash"→filename(.sh), caption→segment, code ✓
- B99 BrutalistCommentCTA: comment+cta→code, variant ✓

### STEP 1 — Writing scenes.py

