# NARRATION — claude-liam-prompting-playbook

**GATE P: pending — human sign-off required before audio generation**

Source: Anthropic "Code with Claude" — The Prompting Playbook (Margot Vanlar, Applied AI Engineer, ~33 min talk)
Channel: claude-liam | Voice: Kokoro am_onyx | Register: Teardown
Title: **The Prompting Playbook**
Subline: *Debug the prompt like code.*

---

## Beat narrations

### YTV01 — Verdict (pre-roll summary)

> The prompting playbook in four moves. Evals first — control, edge, and boundary cases — so every change is measured, not guessed. Hygiene second — XML structure, clear role, output contract — if you cannot tell policy from guidelines, neither can the model. Patch debt third — old defensive instructions break on new models; version-control the why, not just the what. Capability gap fourth — instructions do not add capability; if a task needs reliable arithmetic or a handoff, give the model a tool or a human escalation path. A prompt that works is debugged like code: reproducible cases, one failure mode at a time.

*~38 s | ClaudeVerdictArtifact*

---

### B00 — Cold Open

> Anthropic engineer Margot Vanlar ran the real prompting playbook on a real production prompt — and this is Liam, in for Bear. Two scenarios: a prompt that worked fine until the model migration, and a new agentic system built from zero. One discipline applies to both. Evals first, hygiene second, failure modes one at a time, tools where instructions fall short. Let's actually look at it.

*~23 s | ClaudeComposerAsk — greeting: "Bonjour, Liam"*

---

### B01 — Two Scenarios, One Discipline

> Engineers face two prompting scenarios. Scenario one: a prompt in production — multiple contributors, no clear owner, patches layered for previous models, and a migration suddenly breaks half the test cases. Scenario two: a new agent from scratch — no baseline, picking a model, a harness, and a first draft with nothing to hill-climb against. The same discipline applies to both. You need a reproducible test suite before you touch anything.

*~22 s | Manim: B01_TwoScenarios*

---

### B02 — Evals: The Rigorous Check

> Before targeting failure modes, you need an eval suite. Not optional — mandatory. Three categories. Control cases: unambiguous, should always pass, confirms the model handles the basics. Edge cases: failures you've seen before — the prompt now catches them explicitly so they can't silently regress. Boundary cases: when to escalate to a human or refuse outright — the model needs a clear sense of where its role ends. Without all three columns, you cannot tell if a prompt change was an improvement or just a different kind of wrong.

*~28 s | Manim: B02_EvalSuite*

---

### B03 — Hygiene: Structure the Prompt

> General hygiene before targeting specific failures. Rule of thumb: if you cannot tell guidelines from policy from data when reading the prompt — the model cannot either. The fix is structure. XML tags separating role, guidelines, policy, tone, customer context, and the user message. That cleanup alone improved performance on a failing scenario before any targeted instruction change. Separately: an output contract. A stop sequence on the closing XML tag tells the model exactly when to stop. Disciplined output structure matters most with nested JSON or structured schemas.

*~30 s | ClaudeCodeBeat (XML structure diff + harness stop sequence)*

---

### B04 — Patch Debt

> Here is a failure mode you won't find in a textbook. The customer's data includes exactly how much hotspot data they have — five gigabytes. The model tells them to check the account URL instead of answering directly. Why? An old instruction: "Never give a customer wrong plan details — point them to the URL." That instruction was written to stop hallucination on a previous model. Newer models follow instructions more literally. The patch became the bug. Best practice: version-control your defensive instructions. Track why they exist. An instruction written to stop a 2023 hallucination may cause 2025 information withholding.

*~30 s | Manim: B04_PatchDebt*

---

### B05 — Instructions Don't Add Capability

> Instructions do not add capability. "Critical: always calculate proration amounts correctly." That instruction does nothing. The model cannot reliably do mental arithmetic — telling it to do mental arithmetic correctly is not an implementation, it is a prayer. The fix was a tool. Whenever a calculation is needed, call the proration calculator. The math runs in deterministic code. The model reads the result and explains it to the customer. If you need reliable precision on a task — arithmetic, date logic, database lookup — define the tool, register it in the API, let the model decide when to call it.

*~30 s | ClaudeCodeBeat (instruction vs. tool API call)*

---

### B06 — Both Sides of the Trade-Off

> The billing error case. A customer has a billing conflict. The model tries to diagnose it instead of escalating. Why? The prompt said: "Avoid escalating unless absolutely necessary — escalations cost approximately eight dollars per case and count against fast-resolution metrics." One side of the trade-off. No mention of the cost of getting it wrong: a refund, plus customer trust. Models become more capable means they optimize trade-offs more aggressively. If you give them an incomplete cost function, they solve the wrong problem. State both sides. The cost of escalating AND the cost of not escalating — let the model weigh them.

*~30 s | ClaudeWindow (artifact view — one-sided vs. two-sided framing)*

---

### B07 — Model × Prompt × Harness

> New agent from scratch: a retail staff scheduler with hard constraints. Four approaches tested. Sonnet four-six with a simple prompt — all five trials fail. Opus four-seven, same prompt — violations drop significantly, still failing. Opus with extended thinking — compliant schedules, but triple the tokens and triple the latency. Sonnet four-six with a better prompt — two of five pass, but the model hits output limits before finishing. Model, prompt, and harness are three separate levers. Pulling any one of them in isolation often isn't enough.

*~30 s | ClaudeWindow (artifact view — four-approach comparison table)*

---

### B08 — Generate-Evaluate-Repair

> The winning configuration for the scheduler: three simple prompts instead of one complex one. Generator creates a draft schedule. Evaluator checks every hard constraint, reports specific violations with evidence. Repair prompt receives those violations and makes targeted fixes. Fewer tokens, lower latency than Sonnet with an enlarged prompt. Bonus: soft constraints at runtime — "Harry doesn't like working with Sally" goes into the evaluator description, no code changes to the validation function required. The pattern works because each prompt has one job. When a complex task has clear separable steps, separate them.

*~30 s | Manim: B08_GenEvalRepair*

---

### B09 — Handoff ("Your turn.")

> Your turn. Take a prompt you own. Write five test cases — one control, two edge cases, two boundary cases. Run it. Find the first failure mode. Apply one change: structure first, then a specific instruction, then a tool if instructions won't do it. Measure whether the failure count went down. Paste this into Claude to build the eval suite.

*~22 s | ClaudeComposerAsk — greeting: "Your turn."*

---

### B10 — Title Outro

> The Prompting Playbook. Liam, in for Bear.

*~8 s | ClaudeTitleOutro*

---

## Timing estimate

| Beat | Est. duration |
|---|---|
| YTV01 | 38 s |
| B00 | 23 s |
| B01 | 22 s |
| B02 | 28 s |
| B03 | 30 s |
| B04 | 30 s |
| B05 | 30 s |
| B06 | 30 s |
| B07 | 30 s |
| B08 | 30 s |
| B09 | 22 s |
| B10 | 8 s |
| B11 (logo) | 14 s |
| **Total** | **~5:45** |

---

## GATE P sign-off

Read the narrations above. If the script is approved for audio generation, sign below and set `metadata.gate_p` to `"approved"` in `beat_sheet.json`.

**Signed:** ___________________________  **Date:** ___________

**Notes / changes requested:**

