# PEDAGOGY — claude-liam-cap-06-ship-the-pr
# "Fork. Branch. Verify. Ship." | Reallocation Engine Capstone · E6 of 8
# Built: 2026-07-19 | Kokoro am_onyx

## VERDICT: PASS

## Pedagogical review

### Prediction gate (B03)
- **Question asked**: "A PR that fails conformance or leaks private data has a specific consequence in the grading table. What is it?"
- **What it probes**: The not-gradeable condition — not a point deduction, not a retry opportunity. The PR either passes both verify and doctor or it is not gradeable. This is the same hard stop as a run that breaches the ethics gate.
- **Reveal beat**: B05 (not-gradeable condition stated and explained)
- **Germane friction preserved**: Question placed before B05 which reveals the answer.

### Self-demo (B04)
- **Command**: `grep -n "contrib\|not gradeable\|verify.*doctor\|gap it closes\|limitation" assignments/ASSIGNMENT-professional-contribution-capstone-250pt.md | head -8`
- **Output**: Real — shows branch naming convention (contrib/<name>-<component>), not-gradeable condition (lines 154-155), verify+doctor requirement, PR description fields (lines 157-158). No generation. No credits. $0.00.

### Verbatim quote law (3 required)
1. **B05** — "A PR that fails conformance or leaks private data is not gradeable — the same bar the engine holds every run to." — Source: assignments/ASSIGNMENT-professional-contribution-capstone-250pt.md, Step 5
2. **B06** — "A tight, correct gate-behavior harness is worth more than an ambitious connector that fabricates coverage." — Source: assignments/ASSIGNMENT-professional-contribution-capstone-250pt.md, criteria section
3. **B07** — "You are not writing about the engine. You are adding something to it that runs, that a maintainer could merge, and that a hiring manager could open." — Source: assignments/ASSIGNMENT-professional-contribution-capstone-250pt.md, preamble

### Illustrate law (5 UI + 6 illustration)
- UI beats: B00 (ClaudeComposerAsk), B03 (ClaudeComposerAsk), B04 (ClaudeCodeBeat), BVDT (ClaudeVerdictArtifact), BHTF (ClaudeComposerAsk) = 5 ✓
- Illustration beats: B01 (SkillTeardownAnatomy), B02 (SkillTeardownPipeline), B05 (SkillTeardownMechanism), B06 (SkillTeardownMechanism), B07 (SkillTeardownMechanism), B08 (SkillTeardownMechanism) = 6 ✓

### In-for-Bear law
- "Liam, in for Bear." present in B00 narration_text ✓
- "Olá, Liam." greeting in B00 ✓

### Content grounding
- Step 5 requirements (fork, branch, file placement, verify+doctor, PR description): assignment Step 5 lines 149-161
- Branch naming convention contrib/<name>-<component>: assignment Step 5 line 151
- Not-gradeable condition: assignment Step 5 lines 154-155
- PR description four fields (gap, chapters, boundary, limitation): assignment Step 5 lines 157-158
- "The discipline, not the merge, is what's graded": assignment Step 5 line 161
- "tight, correct": assignment bar criteria
- Maintainer/hiring manager framing: assignment preamble lines 14-16
