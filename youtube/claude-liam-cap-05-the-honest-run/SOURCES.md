# SOURCES — claude-liam-cap-05-the-honest-run
# "The Honest Run." | Reallocation Engine Capstone · E5 of 8

## Verbatim quotes (3 required by VERBATIM QUOTE LAW)

### Quote 1 — B05 (Mechanism · plausibility audit / gate-as-vote bug)
> "The code ran. The number looked reasonable. It was wrong in exactly the way fluency hides: internally consistent, grounded in nothing."
- Source: chapters/16-the-build-and-the-honest-run.md — "The first real run" section, gate-as-vote bug

### Quote 2 — B06 (Mechanism · skip rate)
> "The skip rate is the dial that tells you whether the reallocation principle is actually operating or has quietly collapsed."
- Source: chapters/15-the-pipeline-tracker-and-the-skip-rate.md

### Quote 3 — B07 (Mechanism · what the machine could not know)
> "The engine knows what it measured: funding records, government filings, ATS postings, occupation demand curves, your dates. It could not know that the founder of a skipped startup is your former lab partner."
- Source: chapters/16-the-build-and-the-honest-run.md — "What the machine could not know" section

## Self-demo source
- Command: `sed -n '128,148p' assignments/ASSIGNMENT-professional-contribution-capstone-250pt.md`
- Real output verified at build time: lines 128-148 show all five Step 4 deliverables including "The break attempt is worth more than a clean run." and "pasted, not described."
- No generation. No credits. $0.00.

## Content grounding
- Five Step 4 deliverables: assignment Step 4 lines 128-148
- "The break attempt is worth more than a clean run": assignment Step 4
- Gate-as-vote bug / plausibility audit: chapters/16-the-build-and-the-honest-run.md "The first real run"
- Skip rate ≥50% target: chapters/15-the-pipeline-tracker-and-the-skip-rate.md
- npm run targets (ats:scan, ats:liveness, ats:verify) + python scripts/ats/analyze-patterns.py: chapters/16-the-build-and-the-honest-run.md "The first real run" code block
- "What the machine could not know": chapters/16-the-build-and-the-honest-run.md
