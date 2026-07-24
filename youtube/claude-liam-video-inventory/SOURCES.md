# SOURCES — claude-liam-video-inventory
# "Claude, Audited." | video-inventory skill teardown

## Verbatim quotes (3 required by VERBATIM QUOTE LAW)

### Quote 1 — B05 (Mechanism · Act 1)
> "The audit is a deterministic script, not an LLM pass — it finishes in one shot and cannot run out of context."
- Source: skills/upload/video-inventory/SKILL.md — Design section
- Role: the deterministic law — scripts finish; LLM passes stall; stated once, in B05

### Quote 2 — B06 (Mechanism · Act 2)
> "It is a pure function of the filesystem — no partial state, no credits, no network."
- Source: skills/upload/video-inventory/SKILL.md — Design section
- Role: the pure-function law — reads disk, writes YOUTUBE.MD, changes nothing; stated once, in B06

### Quote 3 — B07 (Mechanism · Act 3)
> "There is nothing to resume and no state to corrupt."
- Source: skills/upload/video-inventory/SKILL.md — Design section
- Role: the idempotency law — re-run anytime, regenerates from disk, instant; stated once, in B07

## Self-demo source
- Phase: live audit run — `python3 runtime/scripts/inventory.py /books`
- Reference: SKILL.md — "deterministic script" and "pure function" guarantees
- Output: B04 ClaudeCodeBeat showing 2762 reels / 49 books → YOUTUBE.MD; complete:19 | 16:9:255 | 9:16:19; slate-only:22 | blocked:193; done in ~1s | cost $0.00
- Not faked: inventory.py reads filesystem paths and file sizes only; no LLM call, no network, no context window; numbers are exact counts at build time
