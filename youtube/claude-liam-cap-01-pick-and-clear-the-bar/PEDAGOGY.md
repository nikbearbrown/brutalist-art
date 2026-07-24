# PEDAGOGY — claude-liam-cap-01-pick-and-clear-the-bar
# "Pick and Clear the Bar." | Reallocation Engine Capstone · E1 of 8
# Built: 2026-07-19 | Kokoro am_onyx

## VERDICT: PASS

## Pedagogical review

### Prediction gate (B03)
- **Question asked**: "What is the one condition without which a contribution grades at zero?"
- **What it probes**: The learner should predict that finding-shaped output with no script is the zero condition — or minimally that every number must trace to a record. The actual reveal (B05–B07) confirms: criterion 1 is the floor and criterion 7 is the zero condition that caps at zero, not merely deducts.
- **Reveal beat**: B05 (criterion 1), B07 (zero condition)
- **Germane friction preserved**: The prediction is placed before the seven criteria are shown — the learner must commit to a principle before seeing the list.

### Self-demo (B04)
- **Command**: `grep -n "^[0-9]\." assignments/ASSIGNMENT-professional-contribution-capstone-250pt.md`
- **Output**: Real — verified locally. Seven numbered criteria at lines 76–85. No generation. No credits. $0.00.
- **Source**: `/Users/bear/Documents/CoWork/bear-textbooks/books/the-reallocation-engine/assignments/ASSIGNMENT-professional-contribution-capstone-250pt.md`
- **Grounding claim**: Grep on a file that exists on disk. Output is the real terminal output verified at build time.

### Verbatim quote law (3 required)
1. **B05** — "Run the script and read the audit before you prompt. Never invent a count, a rate, or a coverage number." — Source: assignments/ASSIGNMENT-professional-contribution-capstone-250pt.md (quoting recipes/_shared.md prime directive)
2. **B06** — "if a gate has no failure path, it is not a gate, it is decoration." — Source: assignments/ASSIGNMENT-professional-contribution-capstone-250pt.md, criterion 3
3. **B07** — "A contribution that produces finding-shaped output with no script behind it is, by the book's own definition, the failure the engine exists to prevent — and is graded as such." — Source: assignments/ASSIGNMENT-professional-contribution-capstone-250pt.md, criterion 7

### Illustrate law (5 UI + 6 illustration)
- UI beats: B00 (ClaudeComposerAsk), B03 (ClaudeComposerAsk), B04 (ClaudeCodeBeat), BVDT (ClaudeVerdictArtifact), BHTF (ClaudeComposerAsk) = 5 ✓
- Illustration beats: B01 (SkillTeardownAnatomy), B02 (SkillTeardownPipeline), B05 (SkillTeardownMechanism), B06 (SkillTeardownMechanism), B07 (SkillTeardownMechanism), B08 (SkillTeardownMechanism) = 6 ✓

### In-for-Bear law
- "Liam, in for Bear." present in B00 narration_text ✓
- "Bonjour, Liam." greeting in B00 ✓

### Content grounding
- Contribution categories grounded on: assignments/ASSIGNMENT-professional-contribution-capstone-250pt.md Step 1
- Five engine components grounded on: chapters/16-the-build-and-the-honest-run.md + the assignment's "engine" paragraph
- Skip-rate ≥50% grounded on: chapters/15-the-pipeline-tracker-and-the-skip-rate.md
- Two-customer pair (nine sections + card fields) grounded on: chapters/04-two-customers.md + assignment Step 2
- Governance files (SNICKERDOODLE.md, DATA_CONTRACT.md, recipes/_shared.md) grounded on: assignment "engine" paragraph
- Gate-behavior harness as "high value, tight scope" grounded on: assignment Step 1 bar, fourth entry under "Scorers & validation harnesses"
- Privacy rule (data/ats/ uncommitted) grounded on: assignment criterion 6 + Ch 16 ethics gate
- Chapter 16 "Can the model verify..." doctrine grounded on: Ch 16 table "Give to the AI / Keep for yourself"

### Demos use fictional scenario
- B04 demo uses the assignment file which is public course material, no PII.
- BHTF exercise uses fictional scenario: learner picks from the named contribution menu.
