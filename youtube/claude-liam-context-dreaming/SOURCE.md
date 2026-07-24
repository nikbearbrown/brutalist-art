# SOURCE.md — claude-liam-context-dreaming

> **VERIFICATION STATUS:** This document is reconstructed from the talk
> title, BUILD PROMPT clues, and publicly available information about the
> event. Every claim marked `VERIFY` must be checked against the actual
> talk recording before the reel is final. This document is the single
> authority for on-screen quotes and results claims — nothing goes on
> screen that isn't here first.

---

## Primary source

| Field | Value |
|---|---|
| **Title** | "Learning while you sleep: Beyond memory to dreaming" |
| **Speaker** | Lamis Mukta |
| **Affiliation** | Anthropic Applied AI |
| **Event** | AI Native DevCon London |
| **Month/Year** | June 2026 |
| **URL** | https://www.youtube.com/watch?v=tTcxVv8HHNw |
| **Runtime** | VERIFY |
| **Slides** | Not yet available |

---

## Key concepts (as inferred from BUILD PROMPT — VERIFY each)

### 1. The amnesiac condition
AI sessions begin from zero; accumulated context from prior sessions is
lost unless explicitly re-injected. As session volume multiplies, the gap
between what was learned and what is retained compounds.

**On-screen highlight in B03:** the word *"multiplying"* (underlined on
the spoken word) — VERIFY exact wording in talk.

---

### 2. The archive phase / RAG ceiling
Mukta characterizes current memory systems (RAG, embeddings) as an
"archive phase." RAG is strong on episodic retrieval but struggles with
semantic and procedural knowledge that forms *across* documents, not
within any single chunk.

**Taxonomy (VERIFY exact terms used by Mukta):**
- **Episodic** — what happened; where RAG performs well
- **Semantic** — what things mean; how concepts relate; RAG struggles
- **Procedural** — how to act in a recurring situation; RAG fails

**Cross-chunk problem (VERIFY term):** An insight that emerges only when
fragment A and fragment C are simultaneously in context has no retrievable
embedding — no address in the vector store.

---

### 3. The dreaming paradigm
When a session ends, a background process runs on the accumulated
context. Not user-query inference — a synthesis operation:

**Dream loop (VERIFY exact framing):**
1. **Read** — ingest full session context
2. **Synthesize** — extract persistent, coherent patterns
3. **Write** — store a condensed *knowledge delta* to a persistent dream
   store

**Knowledge delta (VERIFY term):** the difference between what the model
knew entering the session and what the session produced. The store
accumulates deltas.

---

### 4. Optimistic locking (B20)
**The concurrency problem:** active sessions read from the dream store
while dreaming processes write to it.

**Mukta's solution: optimistic locking** (VERIFY exact phrase) — the
dreaming write assumes no conflict, commits tentatively, and reconciles
only on actual collision. The live session is never blocked.

Source: database concurrency theory (pessimistic locking vs. optimistic
locking). Applied here to AI memory architecture.

> **On-screen text at B20 (VERIFY exact wording from talk):**
> "optimistic locking"
> (Terracotta label appears on spoken word.)

---

### 5. Tiered dream store
Hot → warm → cold storage tiers. Dreaming writes to hot; re-consolidation
promotes items upward as they prove durable. **Promotion criterion
(VERIFY):** soft alignment — the model tests whether a hot insight
remains consistent with cold-store knowledge. Consistent: promote.
Contradictory: queue for reconciliation.

---

### 6. RAD / DEG dual representation (B33)
Every stored insight is held in two forms:

| Label | Form | Use |
|---|---|---|
| **RAD** | the embedding (numerical vector) | vector operations: search, clustering |
| **DEG** | the natural-language label | reasoning: "this resembles that conclusion" |

**VERIFY:** exact acronym expansion (Mukta coins these terms; confirm
they stand for what is asserted here or correct them).

> **On-screen annotation at B33:** terracotta brackets draw on around
> "RAD" and "DEG" labels at the spoken words.

---

### 7. Speaker-reported benchmarks
These numbers are speaker-reported, preliminary, from synthetic
benchmarks. The reel must keep that framing on-screen.

| Condition | vs. RAG only | Note |
|---|---|---|
| Dreaming + RAG, multi-session tasks | +34–41% | VERIFY range |
| Dreaming + RAG, single-session tasks | ~0% | VERIFY |

> **Every on-screen appearance of these numbers must carry the
> "Speaker-reported" tag. Do not strip the qualifier.**

---

### 8. Reconciliation (open problem)
Mukta acknowledges reconciliation — updating the dream store when
understanding changes — as an open design question. The talk frames it
as analogous to the human problem of deliberate unlearning.

---

### 9. Margin stability (B43)
Short sessions, contradictory sessions, sessions with no recurring
patterns: edge cases where dreaming is most likely to consolidate noise.
Mukta's test suite includes these deliberately.

---

## Key quote (VERIFY verbatim)

> "A model that sleeps is not the same model that woke up."

This is the climactic line, used in B42. **Must match SOURCE.md
character-for-character before render.** Do not rephrase.

---

## Hard rules binding every on-screen reference to this source

1. **No imagery of Lamis Mukta** — Tier 3 subject; no photos, no
   AI-generated portraits. All vox stills are Tier 1 generic, source: ai.
2. **Speaker-reported results keep their framing** — "34–41%" is always
   preceded by "speaker-reported" or "Mukta reports."
3. **VERIFY-flagged items must be confirmed before the reel is final** —
   they may appear in the beat sheet as drafts, but the FACTCHECK.md must
   clear them before Gate D1.
4. **URL in credits only, not in narration.**
