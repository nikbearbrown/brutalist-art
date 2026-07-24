# PEDAGOGY — claude-liam-cap-02-build-it-runs
# "Build It So It Runs." | Reallocation Engine Capstone · E2 of 8
# Built: 2026-07-19 | Kokoro am_onyx

## VERDICT: PASS

## Pedagogical review

### Prediction gate (B03)
- **Question asked**: "Name the error class in phase 3 integration that looks like correct behavior while being wrong."
- **What it probes**: The learner should name the gate-as-vote bug — liveness and timeline acting as weighted votes instead of multipliers. The AI cannot catch this from the inside because the code runs, produces numbers in a plausible range, and is internally consistent. Only a plausibility audit catches it.
- **Reveal beat**: B05 (gate-as-vote bug: integration handoff must prove multiplier behavior)
- **Germane friction preserved**: Prediction placed before the bug is named. Learner must commit to a description before seeing Ch 16's exact name.

### Self-demo (B04)
- **Command**: `grep -n "handoff\|It works\|two-customer" assignments/ASSIGNMENT-professional-contribution-capstone-250pt.md`
- **Output**: Real — verified locally at lines 77, 93, 99, 104, 208. No generation. No credits. $0.00.
- **Grounding claim**: Grep on existing local file. Output verified at build time.

### Verbatim quote law (3 required)
1. **B05** — "The handoff condition is the most important element of the whole build. 'The scan returns real postings with provenance' is a handoff condition. 'It looks done' is not." — Source: chapters/16-the-build-and-the-honest-run.md
2. **B06** — "The places where builds go wrong are almost always places where a phase ended on a feeling rather than a test." — Source: chapters/16-the-build-and-the-honest-run.md
3. **B07** — "Drift is its own failure mode — not a consequence of forgetting to maintain the docs, but a structural property of having two artifacts with no enforcement binding them." — Source: chapters/04-two-customers.md

### Illustrate law (5 UI + 6 illustration)
- UI beats: B00 (ClaudeComposerAsk), B03 (ClaudeComposerAsk), B04 (ClaudeCodeBeat), BVDT (ClaudeVerdictArtifact), BHTF (ClaudeComposerAsk) = 5 ✓
- Illustration beats: B01 (SkillTeardownAnatomy), B02 (SkillTeardownPipeline), B05 (SkillTeardownMechanism), B06 (SkillTeardownMechanism), B07 (SkillTeardownMechanism), B08 (SkillTeardownMechanism) = 6 ✓

### In-for-Bear law
- "Liam, in for Bear." present in B00 narration_text ✓
- "Hola, Liam." greeting in B00 ✓

### Content grounding
- Six build phases: chapters/16-the-build-and-the-honest-run.md, "How you build it" section
- Gate-as-vote bug: chapters/16-the-build-and-the-honest-run.md, phase 3 discussion + plausibility audit
- Handoff conditions: chapters/16-the-build-and-the-honest-run.md
- Two-customer pair structure: chapters/04-two-customers.md + assignment Step 2
- Drift failure mode: chapters/04-two-customers.md, "Drift is a failure mode" section
- Give to AI / Keep for yourself: chapters/16-the-build-and-the-honest-run.md, boundary table
- 90-pt grading split (60 code + 30 two-customer pair): assignment Step 2 + grading table
- EMPTY vs ERROR separation: assignment Step 2, "It works" sub-criteria
