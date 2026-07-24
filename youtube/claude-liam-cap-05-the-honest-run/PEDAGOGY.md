# PEDAGOGY — claude-liam-cap-05-the-honest-run
# "The Honest Run." | Reallocation Engine Capstone · E5 of 8
# Built: 2026-07-19 | Kokoro am_onyx

## VERDICT: PASS

## Pedagogical review

### Prediction gate (B03)
- **Question asked**: "Of the five Step 4 deliverables, the assignment says one is worth more than a clean run. Which one?"
- **What it probes**: The deliberate break attempt. The assignment states explicitly: "The break attempt is worth more than a clean run." Most students submit a clean run. The assignment weights the attempt to break your own contribution as a signal of professional rigor — you only discover edge cases by trying to trigger them.
- **Reveal beat**: B05 (plausibility audit / break attempt — the gate-as-vote bug is the canonical example) and B08 (the break attempt explicitly named as the proof of rigor)
- **Germane friction preserved**: Question placed before B05 which contains the gate-as-vote quote.

### Self-demo (B04)
- **Command**: `sed -n '128,148p' assignments/ASSIGNMENT-professional-contribution-capstone-250pt.md`
- **Output**: Real — Step 4 section: all five deliverables including "The break attempt is worth more than a clean run." and "pasted, not described." No generation. No credits. $0.00.

### Verbatim quote law (3 required)
1. **B05** — "The code ran. The number looked reasonable. It was wrong in exactly the way fluency hides: internally consistent, grounded in nothing." — Source: chapters/16-the-build-and-the-honest-run.md — "The first real run" section, gate-as-vote bug
2. **B06** — "The skip rate is the dial that tells you whether the reallocation principle is actually operating or has quietly collapsed." — Source: chapters/15-the-pipeline-tracker-and-the-skip-rate.md
3. **B07** — "The engine knows what it measured: funding records, government filings, ATS postings, occupation demand curves, your dates. It could not know that the founder of a skipped startup is your former lab partner." — Source: chapters/16-the-build-and-the-honest-run.md — "What the machine could not know" section

### Illustrate law (5 UI + 6 illustration)
- UI beats: B00 (ClaudeComposerAsk), B03 (ClaudeComposerAsk), B04 (ClaudeCodeBeat), BVDT (ClaudeVerdictArtifact), BHTF (ClaudeComposerAsk) = 5 ✓
- Illustration beats: B01 (SkillTeardownAnatomy), B02 (SkillTeardownPipeline), B05 (SkillTeardownMechanism), B06 (SkillTeardownMechanism), B07 (SkillTeardownMechanism), B08 (SkillTeardownMechanism) = 6 ✓

### In-for-Bear law
- "Liam, in for Bear." present in B00 narration_text ✓
- "Namaste, Liam." greeting in B00 ✓

### Content grounding
- Five Step 4 deliverables: assignment Step 4 lines 128-148
- "The break attempt is worth more than a clean run": assignment Step 4
- Gate-as-vote bug / plausibility audit: chapters/16-the-build-and-the-honest-run.md "The first real run"
- Skip rate ≥50% target: chapters/15-the-pipeline-tracker-and-the-skip-rate.md
- "What the machine could not know": chapters/16-the-build-and-the-honest-run.md "What the machine could not know"
- npm run targets (ats:scan, ats:liveness, ats:verify) + python scripts/ats/analyze-patterns.py: chapters/16-the-build-and-the-honest-run.md "The first real run" code block
