# PEDAGOGY.md — claude-liam-context-dreaming

**Signed 2026-07-22 NBB** — talk watched and confirmed good; content matches SOURCE.md. Gate P also signed: proceed to audio generation.

VERDICT: PASS

---

## Learning objective

After watching, the viewer can explain:

1. **Why context windows don't solve session memory** — bigger storage
   is not the same as consolidation; the cross-chunk problem is
   structural.
2. **What dreaming adds beyond RAG** — the dream loop (read → synthesize
   → write), the knowledge delta, and why it helps across sessions but
   not within them.
3. **How optimistic locking enables dreaming without blocking** — the
   concurrency problem and its solution borrowed from database theory.
4. **What the RAD/DEG dual store is and why it matters** — two
   representations of the same insight; DEG is what enables reasoning,
   not just search.
5. **Where the design is honest about open problems** — reconciliation
   and margin stability are unresolved; the evidence is speaker-reported
   and preliminary.

---

## Audience

`claude-liam` channel — @NikBearBrown.

Practitioners and makers already using Claude who follow the channel's
Claude workflows. They understand RAG and embeddings. They've hit the
cross-session memory problem personally. They want to understand *why*
dreaming is architecturally different — not a tutorial on how to implement
it.

**Not for:** people new to LLMs (the reel doesn't explain what embeddings
are). People looking for an implementation guide (the talk itself
describes a mechanism, not a shipping product).

---

## Pedagogical approach

**Register:** Teardown (Feynman × MKBHD). Start with the problem the
viewer has already felt. Build the mechanism beat by beat. Evaluate
the evidence honestly — name what the speaker reported, name what's open.

**Concrete before abstract:** B02 opens with "you have a conversation, you
build something, tomorrow it doesn't know you" — the lived experience —
before introducing the theoretical frame.

**Prediction before reveal:** B16 sets up the question ("can AI
consolidate?") before ACT III answers it. B24's speaker-reported numbers
are contextualized *after* the mechanism is understood — the viewer can
evaluate them.

**Useful friction:** the open problems (B40–B43) are given equal weight to
the results. The verdict (B44) names what the design hasn't solved. The
handoff (B45) prompts the viewer to run the dreaming question on their own
work — not to accept the talk's conclusions but to probe them.

---

## Act structure rationale

| Act | Title | Why here |
|---|---|---|
| I | The Amnesiac | Anchor in the problem viewers have felt. The "multiplying sessions" frame shows the problem compounds. |
| II | The Archive | Characterize what RAG does well and where its ceiling is. The cross-chunk problem must be crisp before dreaming makes sense. |
| III | The Dream | Introduce the mechanism. Optimistic locking is the design insight that earns the most attention — it's counterintuitive that a write process doesn't block readers. |
| IV | The Mechanism | The RAD/DEG dual store, the tiered architecture, the promotion criterion, and the reconciliation gap. This is the most technically dense act — the vox run here earns its place as a pacing recovery. |
| V | The Evidence | Evaluation. Name the conditions, the results, the failure cases, and the open problems with equal honesty. The 0.5s lead silence at B42 is earned — it's the climactic statement. |

---

## Hard pedagogical rules for this reel

- **Never attribute understanding the speaker didn't claim.** Mukta's
  benchmarks are synthetic and preliminary; the reel must keep that
  framing every time they appear on screen.
- **One move per beat.** The cross-chunk problem, the dream loop, the
  optimistic locking mechanism — each gets its own beat. Never combine two
  mechanisms in one narration line.
- **The handoff prompt runs the dreaming question.** B45's YOUR TURN must
  invite the viewer to ask Claude to *perform* a dreaming operation on
  their own accumulated context — not to ask Claude what dreaming is.

---

## Gate P note

Gate P (audio spend authorization) requires a second human review of
narration on the animated slate. That gate fires separately after this
document is signed.

---

`[ PENDING SIGN-OFF ]`
