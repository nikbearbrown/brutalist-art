# SOURCES — claude-liam-reel-updater
# "Claude, Updated." | reel-updater skill teardown

## Verbatim quotes (3 required by VERBATIM QUOTE LAW)

### Quote 1 — B05 (Mechanism · Act 1)
> "Dry-run by default. It prints the plan and writes UPDATE.md; it changes nothing."
- Source: skills/make/reel-updater/SKILL.md — Gates & safety section
- Role: the dry-run law — safe to run at any time, plan before any file changes; stated once, in B05

### Quote 2 — B06 (Mechanism · Act 2)
> "Credit discipline: the strip spends nothing. Only the new outro beats ever get new audio, via generate_audio.py --only"
- Source: skills/make/reel-updater/SKILL.md — Gates & safety section
- Role: the credit discipline law — body audio never re-generated, only new beats bill; stated once, in B06

### Quote 3 — B07 (Mechanism · Act 3)
> "Idempotent: a reel with no mascot outro and no orphans is reported clean and skipped; re-running is safe."
- Source: skills/make/reel-updater/SKILL.md — Gates & safety section
- Role: the idempotency law — run-all is safe, clean reels are no-ops; stated once, in B07

## Self-demo source
- Phase: migration audit — free drift scan across all books/*/youtube/* beat_sheets
- Reference: SKILL.md — detect drift step, idempotency guarantee
- Output: B04 ClaudeCodeBeat showing: outro-orig files found (83 reels already migrated), beat_sheet scan (2761 total, 0 drift remaining)
- Not faked: scan runs against live filesystem; numbers (83, 2761, 0) are exact counts at build time; no files deleted, no audio generated
