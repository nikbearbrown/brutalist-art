# PEDAGOGY — claude-liam-cap-03-two-customer-pair
# "Recipe for AI, Card for Human." | Reallocation Engine Capstone · E3 of 8
# Built: 2026-07-19 | Kokoro am_onyx

## VERDICT: PASS

## Pedagogical review

### Prediction gate (B03)
- **Question asked**: "Which card section gets skipped most often — and what fails when it does?"
- **What it probes**: The failure modes section. Ch 4 names this explicitly: "That last section is the one that gets skipped when someone writes a recipe fast." The consequence: at eleven PM when output looks wrong, you have no specific failure modes to diagnose against.
- **Reveal beat**: B06 (failure modes section — specific cause, specific symptom)
- **Germane friction preserved**: Question placed before B06 reveals the answer.

### Self-demo (B04)
- **Command**: `sed -n '105,109p' assignments/ASSIGNMENT-professional-contribution-capstone-250pt.md`
- **Output**: Real — verified locally. Lines 105-109 show all nine recipe sections and human card fields in 5 lines. No generation. No credits. $0.00.

### Verbatim quote law (3 required)
1. **B05** — "An agent that loads the shared contract before running the first command operates inside a defined constraint. An agent that skips it operates from its own priors." — Source: chapters/04-two-customers.md, "What each artifact contains" section
2. **B06** — "That last section is the one that gets skipped when someone writes a recipe fast. And it is the one you need most at eleven PM on a Thursday when the output looks wrong and you don't know why." — Source: chapters/04-two-customers.md, after Table 4.1
3. **B07** — "The reader who has forgotten everything is not a hypothetical. It is you in three months. The human artifact is a letter you are writing to that person. Write it like it is." — Source: chapters/04-two-customers.md, "Both artifacts honor the verified-data contract" section

### Illustrate law (5 UI + 6 illustration)
- UI beats: B00 (ClaudeComposerAsk), B03 (ClaudeComposerAsk), B04 (ClaudeCodeBeat), BVDT (ClaudeVerdictArtifact), BHTF (ClaudeComposerAsk) = 5 ✓
- Illustration beats: B01 (SkillTeardownAnatomy), B02 (SkillTeardownPipeline), B05 (SkillTeardownMechanism), B06 (SkillTeardownMechanism), B07 (SkillTeardownMechanism), B08 (SkillTeardownMechanism) = 6 ✓

### In-for-Bear law
- "Liam, in for Bear." present in B00 narration_text ✓
- "Ciao, Liam." greeting in B00 ✓

### Content grounding
- Nine recipe sections: assignment Step 2 lines 105-107
- Human card fields (purpose, can/can't verify, dependencies, annotated commands, what it produces, failure modes): assignment Step 2 lines 107-109
- recipes/_shared.md as required read: chapters/04-two-customers.md, "What each artifact contains"
- Table 4.1 (AI vs human artifact structural difference): chapters/04-two-customers.md
- Failure modes as the skipped section: chapters/04-two-customers.md, after Table 4.1
- Future-you as the human customer: chapters/04-two-customers.md, "Both artifacts honor the verified-data contract"
- Same-commit enforcement: chapters/04-two-customers.md, "Drift is a failure mode"
