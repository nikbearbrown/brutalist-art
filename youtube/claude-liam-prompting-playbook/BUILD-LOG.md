# BUILD-LOG — claude-liam-prompting-playbook

## 2026-07-20 — Initial script written

- Source: Anthropic "Code with Claude" talk — Margot Vanlar, "The Prompting Playbook" (~33 min)
- Created: `beat_sheet.json` (13 beats: YTV01 + B00–B11), `NARRATION.md`
- Status: **GATE P PENDING** — no audio generated
- Next: human sign-off on narration → set `metadata.gate_p: "approved"` → run audio

### Structural decisions

- 12 body beats + logo outro ≈ 5:45 total (estimated)
- Reel distills four core lessons from the talk: evals, hygiene, patch debt, capability gap
- Two sub-lessons embedded: both-sides trade-off framing (B06), gen-eval-repair loop (B08)
- Visual mix: 4 Manim scenes (B01, B02, B04, B08), 2 ClaudeCodeBeat (B03, B05), 2 ClaudeWindow (B06, B07), bookends (B00, B09, B10, B11)
- Folder: `brutalist-art/youtube/claude-liam-prompting-playbook/` (consistent with claude-liam prompt-tutorial series)
