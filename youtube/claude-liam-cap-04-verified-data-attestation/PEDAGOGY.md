# PEDAGOGY — claude-liam-cap-04-verified-data-attestation
# "Every Number Traces." | Reallocation Engine Capstone · E4 of 8
# Built: 2026-07-19 | Kokoro am_onyx

## VERDICT: PASS

## Pedagogical review

### Prediction gate (B03)
- **Question asked**: "The ethics gate has two parts: privacy and honesty. What is the exact consequence when either part fails — not later, not after the run?"
- **What it probes**: The non-optional, run-blocking nature of the ethics gate. Ch 16 is explicit: "If a run would breach either gate, you don't run it." The assignment adds: "If either fails, the run does not happen." The gate is not a warning — it is a hard stop.
- **Reveal beat**: B06 (ethics gate → honesty → gate fails → run blocked)
- **Germane friction preserved**: Question placed before B06 reveals the answer.

### Self-demo (B04)
- **Command**: `sed -n '113,130p' assignments/ASSIGNMENT-professional-contribution-capstone-250pt.md`
- **Output**: Real — Step 3 section: seven label types (record / script-output / local-evidence / external-source / model-inference / your-input / missing) + ethics gate definition (privacy + honesty) + "If either fails, the run does not happen." No generation. No credits. $0.00.

### Verbatim quote law (3 required)
1. **B05** — "The test: can the model verify this against reality, or only against itself? If only against itself, it's yours." — Source: chapters/16-the-build-and-the-honest-run.md, Give to AI / Keep for yourself table caption
2. **B06** — "An engine that optimizes your search by shading the truth is the failure mode this book exists to prevent — fluency in the service of a false impression is still a false impression, and it is worse when it arrives in a polished format." — Source: chapters/16-the-build-and-the-honest-run.md, "The ethics gate" section, Honesty paragraph
3. **B07** — "For any sentence in a system output, one question settles it: could this sentence have been produced by counting records? If yes, it must trace to a script output or an audit report. If it cannot be traced, it is not allowed to stand." — Source: chapters/03-the-verified-data-contract.md

### Illustrate law (5 UI + 6 illustration)
- UI beats: B00 (ClaudeComposerAsk), B03 (ClaudeComposerAsk), B04 (ClaudeCodeBeat), BVDT (ClaudeVerdictArtifact), BHTF (ClaudeComposerAsk) = 5 ✓
- Illustration beats: B01 (SkillTeardownAnatomy), B02 (SkillTeardownPipeline), B05 (SkillTeardownMechanism), B06 (SkillTeardownMechanism), B07 (SkillTeardownMechanism), B08 (SkillTeardownMechanism) = 6 ✓

### In-for-Bear law
- "Liam, in for Bear." present in B00 narration_text ✓
- "Merhaba, Liam." greeting in B00 ✓

### Content grounding
- Seven label types (record / script-output / local-evidence / external-source / model-inference / your-input / missing): assignment Step 3 lines 113-120
- Ethics gate (privacy + honesty, both non-optional): assignment Step 3 lines 123-125; chapters/16-the-build-and-the-honest-run.md "The ethics gate"
- Give/Keep table + one-question test: chapters/16-the-build-and-the-honest-run.md "The boundary, made operational"
- One-question test: chapters/03-the-verified-data-contract.md
- "If either fails, the run does not happen": assignment Step 3 line ~125; chapters/16-the-build-and-the-honest-run.md "The ethics gate"
- Human signs the attestation, not the model: assignment criterion 6 (never self-certifies)
