# TODO-SCAN BRIEF — cross-repo gap analysis of the "brutalist" family

**You are a senior product/engineering analyst (Fable 5).** The `brutalist-art` refactor
(see `REFACTOR-BRIEF.md`) is complete. Your job now is to scan **every repository with the word
"brutalist" in its name**, find the gap between what is *promised/described* and what is
*actually built and working*, and write a single prioritized **`TODO.md`** of future and missing
features. You WRITE ONLY `TODO.md` (plus an appendix file if noted). You change no other code.
Never invent a feature or a gap — every TODO item must cite the file/doc that evidences it.

---

## 1. Scope — discover the repos, don't assume the list

From `bear-textbooks/books/`, enumerate every directory whose name contains `brutalist`
(case-insensitive). At the time of writing these exist — confirm and update by listing the folder:

| Repo | Type (verify) | What it is |
|---|---|---|
| `brutalist/` | ENGINE | The render/design engine: `manim/`, `remotion/`, `d3/`, `higgsfield/`, HTML/CSS/SVG, and the `BRUTALIST.md` spec. |
| `brutalist-art/` | TOOLKIT | The refactored consolidated video toolkit (skills/, examples/, setup, capability matrix). |
| `brutalist-d3-x-claude/` | BOOK | Chapters teaching the D3×Claude approach. |
| `brutalist-figma-claude/` | BOOK | Chapters + youtube on Figma×Claude. |
| `brutalist-using-d3-and-html-to-make-slide-decks/` | BOOK | Chapters + youtube on D3/HTML slide decks. |

Also check for stray `*brutalist*` files at the `books/` root (e.g. `AUTORUN-brutalist-one.md`)
and note them. **Do not** treat `.git`, `node_modules`, or media as content.

Note: the public GitHub `brutalist-art` repo is currently **empty** (nothing pushed). Treat
"publish the refactored toolkit to its remote" as a candidate TODO, but verify the remote state
before asserting it.

---

## 2. Method — build a promised-vs-built ledger

For each repo, read the authoritative sources and extract two lists: **claimed capabilities**
and **actual/working capabilities**. A TODO item is any delta between them.

Read, per repo:
- Specs & docs: `BRUTALIST.md`, `README.md`, `CLAUDE.md`, `AGENTS.md`, `HELP.md`, `KEYS.md`,
  `MANIFEST.md`, `CAPABILITIES.md`, `HOW-TO-USE.md`, `STATUS.md`, and any `*-SPEC.md`.
- Skill/command definitions: every `SKILL.md` (in `brutalist-art`, the renamed skills).
- Code: build scripts (`*.sh`, `build-*.py`), `manim/`, `remotion/src/`, `d3/`.
- Books: chapter markdown — the books DESCRIBE workflows and features; check whether the engine/
  toolkit actually implements what the prose teaches.

Mine these specific gap sources:
1. **Spec-vs-impl:** features described in `BRUTALIST.md` / book chapters with no implementation.
2. **Dangling references:** skills/scripts that reference scenes, files, patterns, or commands
   that do not exist (e.g. "until the Onda terminal scenes exist, use the fallback" — is it still
   a fallback?). Grep for `TODO`, `FIXME`, `HACK`, `XXX`, `not yet`, `until … exist`, `stub`,
   `placeholder`, `WIP`, `coming soon`.
3. **Refactor deferrals:** anything `brutalist-art/REFACTOR-BRIEF.md` explicitly left for later —
   the deck/lecture skills that were excluded, the figure/data skills that live as session skills
   vs vendored, any duplicate that was flagged. Check whether the refactor actually resolved them.
4. **Capability-matrix holes:** in `brutalist-art/CAPABILITIES.md`, any video type with no example,
   no documented key, or no working `--help`; any `.env.example` key not actually consumed by code
   (dead key) or any key used in code but missing from `.env.example` (undocumented key).
5. **Cross-repo duplication/divergence:** the same thing (e.g. brutalist-slides / D3 deck grammar)
   implemented differently across the engine, the toolkit, and the three books — a consolidation TODO.
6. **Publish/distribution gaps:** empty remotes, missing CI, no lockfiles, no LICENSE, no tests.
7. **Book↔tool coherence:** where a book teaches a capability using the OLD house names, flag a
   TODO to update the book to the refactored jargon (link to `GLOSSARY.md`).

---

## 3. Output — `TODO.md` (write it at `brutalist-art/TODO.md`)

A single prioritized backlog. Structure:

- **Header:** date, the repo list scanned (with commit hashes if available), and a one-paragraph
  state-of-the-family summary.
- **Prioritized items**, grouped by theme (e.g. Engine, Toolkit/Skills, Examples & Docs,
  Publishing/CI, Book coherence). Each item MUST have:
  - `### [P0|P1|P2] <short imperative title>`
  - **Repo(s):** which repo(s) it touches.
  - **Evidence:** the file (and line/section) that proves the gap — a quote or path. No evidence, no item.
  - **Why it matters:** the user-facing consequence.
  - **Acceptance criteria:** how you'd know it's done (testable).
  - **Rough effort:** S / M / L.
- **Appendix A — per-repo capability ledger:** for each repo, the claimed-vs-built table you built
  in §2, so the reasoning is auditable. Put this in `brutalist-art/TODO-APPENDIX.md` if it makes
  `TODO.md` too long.

Priority rubric: **P0** = something is referenced/documented as working but is broken or missing
(a promise the repo already makes); **P1** = a described-but-unbuilt feature or a real usability
gap (setup/docs/examples); **P2** = nice-to-have, polish, or long-horizon ideas.

---

## 4. Constraints
- **Read-only** across all repos except the single `TODO.md` (+ optional appendix) you write in
  `brutalist-art/`. Touch no book chapters, no code.
- Every claim traceable to a file. If you can't verify whether something works, mark the item
  **`[unverified]`** and state what you'd need to run to confirm — do not assert it as broken.
- De-duplicate: one TODO per real gap, even if it shows up in several repos (list all repos on the item).
- Prefer concrete, buildable items over vague aspirations. "Add a `music-video` example with source
  WAV" beats "improve examples."
- If a whole repo turns out to be dead/superseded (e.g. an old book fully replaced by the toolkit),
  say so explicitly as a single "archive/retire" TODO rather than filing many small gaps against it.

## 5. Definition of done
- `brutalist-art/TODO.md` exists, is prioritized, and every item cites evidence.
- Every `*brutalist*` repo in `books/` appears in the per-repo ledger (Appendix A), including any
  you discovered beyond the five expected.
- The refactor's explicit deferrals are each represented (resolved-and-closed, or still-open TODO).
- A human can pick the top P0 and start work from the acceptance criteria alone.

Begin by listing every `*brutalist*` directory under `books/` and building the per-repo ledger.
