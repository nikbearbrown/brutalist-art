# BUILD-NOTES — ch04-medhavy-test

**Date:** 2026-07-15  
**Source:** `brutalist-art/docs/Chapter-04-lecture-deck.html` (24 slides)  
**Output:** `ch04-medhavy-test/deck.html` (medhavy palette, af_kore voice, 24 slides, audio inlined)  
**Total audio:** ~1,075 s (~18 min)

---

## Per-slide component choices

| Slide | Section | Title | Component | Reason |
|---|---|---|---|---|
| S01 | Chapter 4 | Cancer Is Fundamentally a **Genetic** Disease | `thesis` | The load-bearing claim for the entire chapter — biggest one-line assertion |
| S02 | Objectives | Five **Objectives** | `stack` / `wire` | 5 labeled points with sub-descriptions — wire stack is the right shape |
| S03 | §4.1 | DNA **Alteration** Is How Cancer Starts | `flow` + `lead` | 4-step causal chain: error → altered gene → altered protein → cancer |
| S04 | §4.1.1 | DNA Packs into a **Chromosome** | `flow` | Packaging hierarchy: helix → histones → nucleosome → chromatin → chromosome |
| S05 | §4.1.2 | Replication Is **Semiconservative** | `flow` | Replication fork process: helicase → origins → leading + lagging → ligase |
| S06 | §4.1.3 | One Error per **Billion** Bases | `stat-row` | Two magnitudes (error rate + mechanism) — stat-row with `big` numbers |
| S07 | §4.1.4 | **Genomic Instability** Drives Tumorigenesis | `thesis` | Second load-bearing claim — instability as engine; named in accent |
| S08 | §4.1.4 | Replication **Stress** Generates Double-Strand Breaks | `flow` | Concrete mechanism: oncogene → low dNTPs → fork collapse → DSBs |
| S09 | §4.2.1 | Mutations: **Two Scales** of Change | `grid2` | Two distinct flavors of mutation (large-scale vs. point) — grid2 comparison |
| S10 | §4.2.2 | Proto-Oncogene → **Gas Pedal** Stuck | `balance` | Trade-off between proto-oncogene (normal) and oncogene (stuck on) |
| S11 | §4.2.2 | Three Routes to **Oncogene** Activation | `grid3` | Three mechanisms — point mutation, amplification, translocation — equal weight |
| S12 | §4.2.2 | **Both Alleles** Must Fall: Two-Hit Rule | `balance` | Trade-off: intact alleles (safe) vs. two-hit loss (cancer) |
| S13 | §4.2.2 | **TP53** — Guardian of the Genome | `flow` | p53 activation pathway: damage → ATM/ATR → release from MDM2 → p21 or apoptosis |
| S14 | §4.2.3 | **13–44** Mutations per Genome per Year | `stat-row` | Two key numbers: mutation rate + 10,000× variation — stat-row |
| S15 | §4.3 | **90% of Cancers** Have Chromosomal Changes | `callout` | One non-negotiable fact that must land — callout format |
| S16 | §4.3 | **Detection** and Hereditary Patterns | `stack` / `wire` | 4 labeled detection/heredity tools — wire stack |
| S17 | §4.4 | Four **Repair** Pathways Guard the Genome | `grid2` (2×2) | Four named pathways, each with damage type — grid2, DSB repair `.hot` |
| S18 | §4.4.2 | NER: **Excise**, Fill, Seal | `flow` | Three-step repair process — clean sequential flow |
| S19 | §4.4.2 | DSBs: **Accurate HR** vs Fast NHEJ | `balance` | Trade-off: HR (accurate, slow) vs NHEJ (fast, error-prone), fulcrum = DSB |
| S20 | §4.4.4 | Broken **Repair** = Mutator Phenotype | `stack` / `wire` | 3 named failure modes: mutator phenotype, Lynch, XP |
| S21 | §4.5 | Cancer Behaves as an **Evolutionary** Process | `thesis` | Synthesis claim — cancer as somatic evolution |
| S22 | §4.5.2 | CIN at the **Chromosome** Level, MSI at Sequence | `balance` | Two instability flavors with opposite karyotype appearances |
| S23 | §4.5.4 | **Drivers** Propel the Cancer; Passengers Ride | `grid2` | Two-way taxonomy: driver vs passenger — grid2 |
| S24 | Summary | Stability to Survive, **Change** to Evolve | `close` + `callout` | Chapter close with tag cloud + the central tension as callout |

---

## Figures lost (source had images, deck has none)

The source HTML used images from `chapter 4 image/` for 9 slides:
- S03 (4-1-1.jpg), S05 (4-1-2.jpg), S07 (4-1-4-1.jpg), S08 (4-1-4-2.jpg)
- S10 (4-2-2-1.jpg), S11 (4-2-2-2.jpg), S12 (4-2-2-3.jpg), S13 (4-2-2-4.png)
- S16 (4-3-1.jpg), S18 (4-4-2-1.png), S19 (4-4-2-2.png), S21 (4-5-1.jpg)

These are NCI / HAI-sourced images. The focus-rules build replaces them with semantic
components — this is by design (no bullet walls, no split figure/text layout).
If the figures are needed for a later iteration, they can be added as a `pantry/` asset
and embedded into a `body_html` `<img>` inside a `cell-part` or below a `lead`.

---

## Forced component choices

- **S02 (Objectives)**: 5-wire stack is borderline — one more item and it would need to
  split into two slides. At 5 it fits without crowding.
- **S13 (TP53 flow)**: The fork at the end (p21 checkpoint OR apoptosis) is expressed as
  `<span class="arw">or</span>` between the two terminal chips. Not a standard `arw` use
  but visually correct.
- **S16**: Title starts with an empty `["", false]` pair (Detection has no natural prefix).
  This renders fine — build_deck.py skips empty non-accented strings.
- **S23**: Same empty-prefix pattern for "Drivers".

---

## What to try next

- Drop in the NCI images as `pantry/` assets if the visual proof point matters
- Run a second voice (af_heart) to compare registers against af_kore
- Promote to a canonical ch04-lecture folder in `cancer-medicine/lectures/`
  once the deck passes Bear's eyeball review
