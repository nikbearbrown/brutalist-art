# PEDAGOGY audit — claude-liam-a2-03-prd-problem-solution ("Write a PRD Like a PM, Part 1: Problem & Solution")

Episode 3 of the "Plan It Like a PM — Your Madison PRD" series for INFO 7375 Assignment 2. Covers PRD Part 1 — Problem Statement and Proposed Solution, together worth 20 pts (10 each). Builds on the gap identified in Episode 2 as the Madison project anchor. claude-liam, Kokoro am_onyx.
Series of 4 episodes building a Madison PRD. Audited against ai-explainer house + frame laws.

## Act structure
- B00 cold open → B01 what a PRD is and why the problem statement is the anchor → B02 three required elements of a good problem statement → B03 specificity test (three-question format) → B04 proposed solution requirements → B05 traps → BVDT verdict → BHTF your turn handoff → BOUT outro. 9 beats. PASS

## Cold open (COLD OPEN LAW)
- B00 is ClaudeComposerAsk (shot type "ClaudeComposerAsk" per the beat_sheet). Liam self-introduces ("E3. PRD — Product Requirements Document."). Output lines enumerate the two deliverables: Problem Statement (10 pts) with its three required parts, and Proposed Solution (10 pts) with its Madison-specific requirements. PASS

## Gap formula / hook
- Opening tension: "Get these right, and every section that follows has a foundation. Get them wrong, and the vagueness compounds." This stakes the episode not just as 20 points but as the structural integrity of the entire PRD. The three-question specificity test in B03 operationalizes the tension: any FAIL on the test is a flag to revise before writing the solution. PASS

## Utility lint
- BHTF prompt produces a concrete pressure-test of the student's draft problem statement — four checks (specific user, observable pain, cost stated, "why Madison" answered), each returning PASS/FAIL with a one-sentence explanation plus an improved draft for any failure. Directly usable: student pastes their draft and gets actionable revision guidance before putting anything on the Figma board. Read aloud by Liam with the usage instruction ("Take the gap you identified in Episode 2 — specifically the gap your project is built around") and the loop named ("draft, pressure-test, revise, move on"). HANDOFF LAW: prompt read aloud, process discussed. PASS

## Vocabulary / register (Pragmatist)
- Steps-first throughout. "PRD" defined on first use in B00 ("PM-speak for the single written agreement a team makes before anyone writes a line of code"). Three required problem statement elements (WHO, WHAT, COST) introduced with labels in B02. Five Madison layers named by formal name in B04 with example components (MarketMind Research, Brand Voice Personalization, AI Concierge, Multi-Armed Bandit / Thompson sampling). "Why Madison" framed as a required, graded question — not optional context. Register matches how-to series doctrine. PASS

## Honesty (DOUBLE-CHECK LAW)
- Specificity is the explicit honesty mechanism: the three-question test in B03 is a structured check against vagueness rather than a list of suggestions. B02 recommends using industry numbers if they exist ("a study, a report, a benchmark") and distinguishes a real cost statement from "vibes." B04 distinguishes a technically interesting challenge from "just wiring up an API call." The "why Madison" requirement named in B04 and reinforced in B05 prevents the proposed solution from being indistinguishable from a generic AI project — a concrete false-safety check. PASS

## Length law
- 9 beats, est. ~255s (~4:15) at Kokoro pace (B00: 20s, B01: 30s, B02: 40s, B03: 25s, B04: 40s, B05: 25s, BVDT: 25s, BHTF: 40s, BOUT: 5s, total narration 250s — task described as ~4.2 min). Appropriate for a 20-point section focused on two tightly coupled, conceptually foundational PRD sections. PASS

## Visual law spot-check
- ILLUSTRATE LAW: B00 ClaudeComposerAsk for the cold open; B01 ClaudeWindow artifact for the PRD definition and anchor framing; B02 ClaudeComposerAsk for the problem statement drafting prompt; B03 ClaudeWindow artifact for the three-question specificity test; B04 ClaudeComposerAsk for the proposed solution drafting prompt; B05 ClaudeWindow artifact for the four traps; BVDT ClaudeVerdictArtifact for the rules summary; BHTF ClaudeComposerAsk for the pressure-test handoff prompt; BOUT ClaudeTitleOutro. ASK→RESULT: B02 shows the problem statement prompt (ask) and its three output lines — WHO, WHAT, COST (result); B04 shows the solution prompt (ask) and its three output lines — named layer/component, "why Madison," technically interesting challenge (result); BHTF shows the four-check prompt (ask) and the five output lines including "improved draft for any failing section" (result). SparkLine present on B01 ("anchor → solution → stories → metrics"), B03 ("specific user → observable pain → stated cost → PASS"), B05 ("specific → costed → Madison-specific → technically grounded"). No fabricated screenshots. PASS

VERDICT: PASS
