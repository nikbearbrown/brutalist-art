# PEDAGOGY audit — claude-liam-prompting-playbook ("The Prompting Playbook")

ai-explainer, claude-liam, Kokoro am_onyx. Teardown register.
Source: Anthropic "Code with Claude" — Margot Vanlar, The Prompting Playbook (~33 min talk).

## Act structure
- Verdict (YTV01) → cold open (B00) → establish (B01) → teach ×6 (B02–B08) →
  handoff (B09) → outro (B10) → logo (B11). 13 beats.
- YTV01 pre-roll verdict distills all four lessons before the body. Body delivers
  each lesson in order (evals → hygiene → patch debt → tools → trade-offs →
  model×prompt×harness → gen-eval-repair). HANDOFF (B09) gives a paste-ready
  prompt. Title restate (B10) closes. PASS

## Cold open (COLD OPEN LAW)
- B00 is ClaudeComposerAsk. First sentence of narration: "…this is Liam, in for
  Bear." Greeting is "Bonjour, Liam." Thesis states both scenarios and the
  one-discipline framing. No typing in inner beats. PASS

## Gap formula / hook
- Tension: a prompt that worked fine until migration suddenly fails half the test
  suite; a new agent with no baseline to hill-climb against. Resolved beat by
  beat (B02 provides the diagnostic tool; B03–B08 each close one failure mode).
  Hook is a real engineering situation, not a tease. PASS

## Utility lint
- B09 (HANDOFF) is a paste-ready prompt: five test-case types named, one change
  at a time discipline, and a concrete Claude prompt to build the eval suite.
  Every body beat closes with a single actionable rule. PASS

## Vocabulary / register (Teardown)
- Direct and precise. Each lesson states the failure, the mechanism, and the
  fix. Sardonic edge on B04 ("a prayer, not an implementation"). No jargon
  beyond what the source talk itself uses. Concrete numbers (5 GB, $8, 3× tokens)
  taken directly from the original demo. PASS

## Honesty / factual accuracy
- All claims derive from the source talk. Specific numbers (five gigabytes,
  $8 escalation cost, triple tokens on Opus+thinking, 100s latency) are from
  Margot's live demo — presented as illustrative figures from that demo, not
  general benchmarks. No benchmark comparisons made beyond what the talk showed. PASS

## Length law
- 13 beats, estimated ~345 s (~5:45). Under 7-min ceiling for this topic depth.
  Each beat is a single lesson with no padding. Real durations become the clock
  at audio time. PASS

## Narration spot-check
- Numbers spoken in full words ("four-six", "four-seven", "five gigabytes",
  "eight dollars"). No beat re-states the prior beat's content. Each body beat
  advances: evals → structure → patch → tools → trade-offs → levers → split.
  B09 narration reads the paste-prompt aloud before handing it off. PASS

## Visual law spot-check
- Claude UI appears in bookend beats (B00, B09 ClaudeComposerAsk; B10
  ClaudeTitleOutro). Body beats use Manim for mechanisms (B01, B02, B04, B08)
  and ClaudeCodeBeat/ClaudeWindow for code/artifact views (B03, B05, B06, B07).
  No inner beats use ClaudeComposerAsk. No screenshots. PASS

VERDICT: PASS
