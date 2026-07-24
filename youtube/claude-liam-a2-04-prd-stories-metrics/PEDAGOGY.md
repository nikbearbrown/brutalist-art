# PEDAGOGY audit — claude-liam-a2-04-prd-stories-metrics ("Write a PRD Like a PM, Part 2: User Stories & Success Metrics")

Episode 4 of the "Plan It Like a PM — Your Madison PRD" series for INFO 7375 Assignment 2. Covers PRD Part 2 — User Stories (As/I want/so that format, 3 required) and Success Metrics (what/how much/how measured, 3 required), together worth 20 pts (10 each). Builds on the Problem Statement from Episode 3. claude-liam, Kokoro am_onyx.
Series of 4 episodes building a Madison PRD. Audited against ai-explainer house + frame laws.

## Act structure
- B00 cold open → B01 user story format and requirements → B02 drafting three stories (prompt) → B03 strong vs. weak example → B04 success metrics — what earns credit → B05 excellence moves (baseline, named tool, edge case) → B06 traps → BVDT verdict → BHTF your turn handoff → BOUT outro. 10 beats. PASS

## Cold open (COLD OPEN LAW)
- B00 is ClaudeComposerAsk. Liam self-introduces ("E4. Two things separate a real PRD from a well-written essay about a project."). Output lines enumerate the two deliverables: User Stories (10 pts) in the As/I want/so that format, and Success Metrics (10 pts) answering what/how much/how measured. PASS

## Gap formula / hook
- Opening tension: "Two things separate a real PRD from a well-written essay about a project" — positions the episode as the precision gap between knowing the concept and producing a graded artifact. The strong vs. weak example in B03 makes the gap concrete: same intent, one earns full credit, the other earns none, and the difference is precision rather than effort or creativity. PASS

## Utility lint
- BHTF prompt produces a concrete conversion artifact — feature ideas converted to correctly formatted user stories, one success metric per story with a target value and named measurement method, and flags for vague benefits and unclear measurement methods. The prompt is the "conversion step — from 'here is what I think the system should do' to 'here is a PRD section that earns points.'" Read aloud by Liam with the explicit instruction to revise any vague benefit and add any missing measurement method before building on the Figma board. HANDOFF LAW: prompt read aloud, the revision loop discussed ("read the output... revise it... this is the conversion step"). PASS

## Vocabulary / register (Pragmatist)
- Steps-first throughout. "User story" defined structurally in B01 with all three parts labeled and their requirements stated. "Success metric" defined operationally in B04 ("a metric earns credit only if it answers three questions: what improves, by how much, and how you would measure it"). "Edge case" introduced in B05 with a worked example (high click-through with falling conversion). n8n named correctly as "a separate visual workflow tool, not part of Madison's architecture" (B05) — reinforces Episode 2's distinction. "Industry baseline" introduced in B05 with the instruction to name the source. Register matches how-to series doctrine. PASS

## Honesty (DOUBLE-CHECK LAW)
- Two honesty vectors. First, format precision: the three-question test for metrics (what/how much/how measured) maps directly to what the rubric checks, grounding the guidance in verifiable assessment criteria rather than advice. The strong vs. weak example in B03 is a concrete demonstration of the precision standard, not an abstract claim. Second, hallucination-adjacent: B04 gives a real industry baseline example (45 → under 15 minutes, Typeform survey at week 4) rather than a placeholder, modeling what a real metric looks like. B05 warns that AI-drafted metrics may lack measurement methods ("flag any metric that cannot be measured with the tools in the project") and names n8n correctly as a separate tool. BVDT re-states that stories must close the loop on Episode 3's problem statement — a cross-episode coherence check. PASS

## Length law
- 10 beats, est. ~285s (~4:45) at Kokoro pace (B00: 20s, B01: 30s, B02: 40s, B03: 25s, B04: 40s, B05: 30s, B06: 25s, BVDT: 25s, BHTF: 40s, BOUT: 5s, total narration 280s — task described as ~4.7 min). Appropriate for a 20-point section with two distinct deliverable types (format-precise stories and measurable metrics), each requiring its own worked example. PASS

## Visual law spot-check
- ILLUSTRATE LAW: B00 ClaudeComposerAsk for the cold open; B01 ClaudeWindow artifact for the user story template with three labeled parts; B02 ClaudeComposerAsk for the story-drafting prompt; B03 ClaudeWindow artifact for the strong vs. weak example; B04 ClaudeComposerAsk for the metrics-drafting prompt; B05 ClaudeWindow artifact for the three excellence moves with the n8n note; B06 ClaudeWindow artifact for the four traps; BVDT ClaudeVerdictArtifact for the rules summary; BHTF ClaudeComposerAsk for the handoff prompt; BOUT ClaudeTitleOutro. ASK→RESULT: B02 shows the story-drafting prompt (ask) and the four output lines including per-story MVP scope flag (result); B04 shows the metrics prompt (ask) and the four output lines including the "flagged" row (result); BHTF shows the feature-conversion prompt (ask) and the three output lines including vague-benefit and unclear-method flags (result). SparkLine present on B01 ("role → feature → benefit → complete story"), B03 ("precision → specificity → full credit"), B05 ("baseline → named tool → edge case → excellence"), B06 ("format → distinct needs → measurable → named method"). No fabricated screenshots. PASS

VERDICT: PASS
