# Chapter 9 — Finishing Pass and Figures

*Where the book becomes visible — and the visual fluency trap arrives on schedule.*

---

Here is one paragraph from a draft of Chapter 7 of *ai-for-designers*, exactly as Cowork produced it:

> *Five things to watch for in the draft. Voice will drift toward Wikipedia. Specificity will be invented where the pantry was thin. Domain judgment will be missing where the model could not infer it. The middle will be padded. Bridge questions will gesture rather than commit.*

And here is the same paragraph after a finishing pass:

> ## Five failure modes — read in this order
> *The model is good at producing prose that reads correct and means nothing. Here is what to look for first.*
>
> Voice will drift toward Wikipedia. Specificity will be invented where the pantry was thin. Domain judgment will be missing where the model could not infer it. The middle will be padded. Bridge questions will gesture rather than commit.
>
> <!-- → [INFOGRAPHIC: Five Failure Modes — a 5-row table laid out as a vertical taxonomy. Left column: failure name. Middle column: how it sounds in a draft. Right column: rewrite move. Two-color (ink + ochre), no gradients.] -->

Same prose. Three additions. A heading that names what is coming. An italic subtitle that says what the section is actually doing. And an HTML comment at the moment the reader needs to see the taxonomy as a structure rather than a list.

The "after" is still missing something. There is no figure yet. There is only a comment that says *a figure goes here, and here is what it should do*. That comment is a contract between the author and the figure pipeline — it tells the next stage where a figure belongs and what work it is supposed to do.

This chapter runs three operations in sequence. Every chapter gets a subtitle that earns its place and honest visual placeholder comments at the moments they would help. CAJAL reads those chapters and proposes figure candidates, ranked. The proposals become real SVGs, real PNGs, real D3 files. The book becomes visible.

You are also going to learn what the visual fluency trap looks like, because it is going to arrive. CAJAL can produce a chart that is technically a chart, semantically empty, and convincingly designed. You will catch it the same way you caught the verbal fluency trap in Chapter 1. The skill transfers.

---

Before the three operations, a note on tooling. CAJAL's SVG generator and the PNG converter at `SCRIPTS/svg-to-png.mjs` are Node.js programs. You need Node 18 or higher. If you don't already have it:

**Mac:** `brew install node` then verify with `node --version`.

**Windows:** `winget install OpenJS.NodeJS.LTS` then verify with `node --version`.

**Linux (Ubuntu/Debian):** `sudo apt update && sudo apt install -y nodejs npm` then verify both.

From inside your book directory, run `cd SCRIPTS/ && npm install sharp`. That installs the PNG converter's one dependency. If it fails on Mac silicon with a message about Python or libvips, rerun with `npm install --include=optional sharp`. That is the only workaround you will need. [verify — `sharp` install paths can drift between major versions on macOS]

You do not need to learn Node. You do not need to read any JavaScript. You need it on your machine so the scripts run. Five minutes.

---

The Chapter Finishing Pass does exactly two things to each chapter file. It does not touch your prose. It inserts an italic subtitle on the line below the main heading if one is missing, and it inserts HTML comments at the places in the text where a table, image, infographic, or chart would genuinely help the reader.

That is it. Two passes, no rewrite, no reorganization. The finishing pass runs after the human rewrite from Chapter 8. The prose is the author's at this point. The pass adds navigational scaffolding on top.

The subtitle distinction is worth spending time on because it is where most finishing passes fail.

A topic heading names territory. *"Color theory."* It is true. It is also the kind of thing a Wikipedia stub would say. A subtitle surfaces tension. *"Why every accessible palette starts with grayscale."* That second one is doing work — it tells the reader what the chapter's argument is going to be. It commits the author to a position.

Cole Knaflic calls this "the so-what" — the move from naming a category to naming a claim.[^knaflic] Robert Bringhurst treats it as a typographic move: the subtitle is a different rank of text and should look different on the page.[^bringhurst] Both are describing the same underlying requirement, which is that a subtitle should be impossible to move to a different chapter without breaking.

Three rules that make a subtitle work:

Less than fifteen words. If you cannot state the central tension in fifteen words, the chapter does not yet know what its central tension is — return to Chapter 4. A claim, not a category: if the subtitle could appear under a different chapter's heading without breaking, it is not doing chapter-specific work. Italic in the rendered EPUB: reflowable EPUBs reliably honor italic styling; they do not reliably honor custom CSS classes; italic is the safe contract.

The visual placeholder comments are the other half of the finishing pass output, and the brief inside each comment is what separates useful scaffolding from decoration. The format is:

```
<!-- → [INFOGRAPHIC: Five Failure Modes — a 5-row table laid out as a vertical taxonomy. Left column: failure name. Middle column: how it sounds in a draft. Right column: rewrite move. Two-color (ink + ochre), no gradients.] -->
```

The arrow is a grep target so you can find all pending visuals at once. The bracket type — `INFOGRAPHIC`, `CHART`, `TABLE`, `IMAGE`, `DIAGRAM` — tells the enrichment pass which generator to invoke. The description after the colon is the brief the figure-generation step reads.

Three rules for a brief that does not produce a generic figure. Name the data, not the category: not "a chart of failure modes" but "a 5-row table, named columns, two-color." Name the constraint: "No gradients. Two-color. Flat fills." Name the load it has to carry: "The reader should leave knowing the rewrite move, not just that there are five failure modes." A brief that names data, constraint, and load is one that any figure generator — CAJAL, a junior designer, or a future tool none of us has seen — can execute against a clear standard.

<!-- → [TABLE: visual placeholder comment anatomy — three columns: element (arrow / bracket type / brief), what it does, example — showing how the three parts of the comment format map to different downstream uses] -->

| Element | What it does | Example |
|---|---|---|
| The arrow | A grep target so you can find every pending visual at once | `→` |
| The bracket type | Tells the enrichment pass which generator to invoke | `INFOGRAPHIC`, `CHART`, `TABLE`, `IMAGE`, `DIAGRAM` |
| The brief (after the colon) | The instruction the figure-generation step reads — names data, constraint, and load | `Five Failure Modes — a 5-row table... Two-color (ink + ochre), no gradients.` |

![A single placeholder-comment string segmented into three regions left to right — the arrow as grep target, the bracket type as generator selector, the brief after the colon — each region dropping a callout line to a reserved cell naming its downstream role.](../images/09-finishing-pass-and-figures-fig-01.png)
*Figure 9.1 — Anatomy of a visual placeholder comment*

---

CAJAL Image Suggest runs across every chapter and proposes figures. It does not generate any SVG yet. It writes one file per chapter at `pantry/{chapter-slug}-cajal.md`, listing every figure it thinks would help, ranked by priority, with a full SCOPE prompt for each. The Finishing Pass and Image Suggest prompts are reproduced in Appendix G.

Think of `cajal.md` as a menu. You will reject some items. You will modify some. You will add candidates CAJAL missed. The point of having proposals in their own file before any SVG is generated is that you get an editorial pass between the candidate inventory and the rendered figure. What you do not edit, you ship.

CAJAL scans chapter prose for three signal patterns. Understanding them is understanding why it proposes what it proposes.

**MC — Mechanism Complexity.** The chapter describes a process with three or more interdependent steps. The pipeline overview in Chapter 5 is MC. The three-pass rewrite loop in Chapter 8 is MC. Most "and then this, and then this" passages trigger MC.

**VG — Verification Gap.** The chapter makes a structural claim the reader cannot verify from prose alone. "The Combined Test has fourteen items in two groups" is a VG signal — the reader has to be shown the structure to confirm it. "Cowork reads four files in order" is VG.

**PQ — Proportional or Quantitative.** Any percentages, ratios, counts, or comparisons. "Steady workers complete in four to six weeks" is PQ. "Eighty percent of indie ebook units" is PQ. Anything with a number that compares to another number.

Tamara Munzner's *Visualization Analysis and Design* calls the underlying diagnostic the "what-why-how" framework: what data do you have, why is the reader looking, how should it be encoded.[^munzner] CAJAL's MC/VG/PQ is a coarser, faster version of the same — a triage layer before the full what-why-how decision.

Open a `cajal.md` after a run and you will see a structure like this:

```
# Figure Plan — Chapter 7

## Figure 7.1 (Critical, MC)
**Title:** The eight-section Cowork chapter structure
**Trigger:** Chapter describes 8 sequential sections each Cowork chapter follows.
**SCOPE:**
  Specification: One-column vertical flow diagram, 8 boxes.
  Content: Section name + one-line "what it does" per box.
  Organization: Top-to-bottom, arrow between each.
  Presentation: Two-color (ink + ochre). No gradients. Flat fills.
  Exclusions: No icons. No screenshots. No decorative borders.
```

The SCOPE prompt is what the SVG Generator reads. Title, ranking, trigger, and five SCOPE fields — Specification, Content, Organization, Presentation, Exclusions — appear consistently across all chapters.

The editorial pass through a `cajal.md` takes ten minutes per chapter and is worth every minute of it. Critical figures should map directly to a primary learning outcome. Open the chapter. If the Critical figure does not encode the thing the reader is supposed to leave knowing, demote it and find one that does. Important figures support a key argument but are not load-bearing — these are usually safe. Supplementary figures are nice-to-have, and the honest answer is often "skip this one." A textbook is not improved by having a figure on every page.

![A top-to-bottom decision tree with three nodes — Critical (does it map to a primary outcome?), Important (does it support a key argument?), Supplementary (skip unless time allows) — each with a pass-through arrow to the next test, the Critical node carrying a demote redirect and the Supplementary node terminating in a skip glyph.](../images/09-finishing-pass-and-figures-fig-02.png)
*Figure 9.2 — CAJAL figure-priority decision path*

<!-- → [INFOGRAPHIC: CAJAL figure priority decision tree — three nodes: Critical (does it map to a primary outcome?), Important (does it support a key argument?), Supplementary (skip unless time allows) — flat two-color, no decorative elements] -->

[^knaflic]: Knaflic, C. N. (2015). *Storytelling with Data*. Wiley.
[^bringhurst]: Bringhurst, R. (2013). *The Elements of Typographic Style* (4th ed.). Hartley & Marks.
[^munzner]: Munzner, T. (2014). *Visualization Analysis and Design*. CRC Press.

---

The SVG Generator reads the `cajal.md` files you have edited and produces real SVG files in `images/`. The pipeline then runs `node SCRIPTS/svg-to-png.mjs` to convert every new SVG to a 300-DPI PNG, runs the enrichment pass that inserts markdown image links at the placeholder locations, and writes a corresponding D3 v7 HTML file in `d3/` for any figure with interactive data underneath it.

You do not write any JavaScript. You read the `cajal-svg-log.md` written at the end, and you open the PNGs.

PNG is the publication artifact. Kindle's reflow engine renders PNGs reliably across every device — Paperwhite, iPad, iPhone, Colorsoft, desktop Kindle app. SVG is the source artifact. You keep it because it is editable, version-controlled, and re-renderable at any resolution. PNG is what ships in the EPUB. SVG is what survives a redesign. This is the same separation as `combined.md` → EPUB+PDF: the source is text, the build output is the binary the device renders. You do not edit the build output. You edit the source and rebuild.

![A left-to-right systems diagram of the CAJAL pipeline — Finishing Pass, CAJAL Image Suggest producing cajal.md, SVG Generator producing SVG source, the svg-to-png converter producing the 300-DPI PNG, the enrichment pass inserting markdown links — with a downward D3 companion branch off the source stage and a divider marking SVG and D3 as source artifacts versus the PNG that ships in the EPUB.](../images/09-finishing-pass-and-figures-fig-03.png)
*Figure 9.3 — The CAJAL pipeline: prose to publication artifact*

The D3 files in `d3/` are for figures that have data structure underneath them — anything CAJAL flagged as MC or PQ that could be interactive. What they are honestly for: not for the published EPUB (EPUBs do not reliably execute JavaScript), but as authorable source artifacts so the next edition has editable chart code, and optionally as a companion-web property if you want readers to explore the data. If you do not plan to host the D3 files anywhere, they cost nothing to keep in the repository. The PNG is what the reader sees in the book.

The AI+1 visual standard is what you audit every generated figure against. It is the visual analogue of the Combined Test from Chapter 8 — stripped down, device-agnostic, constraint-first. The constraint exists so the *content* of the figure carries the load, not the chrome.

Two-color or three-color maximum per figure. ColorBrewer "Set2" for qualitative comparisons and "Blues" for sequential data are the safe defaults. Avoid red/green pairings — about 8% of male readers have some form of red-green color blindness. Every figure must read in grayscale.

Flat fills only. No gradients. Gradients render as a smooth ramp on retina iPad and as a banded mess on e-ink Paperwhite. Flat fills degrade gracefully across every device in that range.

No rounded corners, no drop shadows. They look contemporary in Figma. They look pixelated at reflow.

Every SVG has a `<title>` and `<desc>` element. This is an EPUB 3 accessibility requirement per the W3C EPUB Accessibility 1.1 specification.[^w3c] It is also a fact-checking aid — alt text that drifts from what the figure shows is a flag that the figure or the description needs updating.

Axes are labeled. Units are declared. Source and date are present. This is Tufte's rule, stated plainly in *The Visual Display of Quantitative Information* and violated constantly in AI-generated figures.[^tufte]

And the figure earns its place. If the prose conveys the information as efficiently as the figure would, delete the figure. Tufte's data-ink ratio is the diagnostic: the proportion of a figure's ink devoted to non-redundant data. Generic decoration is what he called chartjunk. A figure that is present because CAJAL proposed it and nobody said no is chartjunk with a SCOPE prompt.

There is a contested edge to this last rule worth naming honestly. Bateman and colleagues published "Useful Junk?" at CHI 2010 with empirical evidence that embellished charts are better remembered than minimalist ones.[^bateman] Mona Chalabi's hand-drawn data illustrations in the Guardian make the same argument from data journalism — visual personality is a data-integrity move because it signals provenance and single-author accountability. Both are legitimate. Both are out of scope for the AI+1 series default. The reasoning: a $1 Kindle book is read across more devices than any other format, and the device-agnostic constraint wins until there is a specific reason to break it.

[^w3c]: W3C. (2023). *EPUB Accessibility 1.1*. w3.org/TR/epub-a11y-11/.
[^tufte]: Tufte, E. R. (2001). *The Visual Display of Quantitative Information* (2nd ed.). Graphics Press.
[^bateman]: Bateman, S., et al. (2010). "Useful Junk? The Effects of Visual Embellishment on Comprehension and Memorability of Charts." *CHI 2010*.

---

The worked example is Chapter 7 of *ai-for-designers* through the full pipeline, showing what each step produced and what was accepted, modified, and rejected.

**Step 1 — Chapter Finishing Pass.** Before the pass, the chapter heading read `# Chapter 7 — Running the Chapter Writer`. After:

```
# Chapter 7 — Running the Chapter Writer
*Why the first draft of a fourteen-chapter book takes one hour and three weeks of preparation.*
```

The subtitle surfaces the tension — the real runtime is not the model's hour but the author's preparation. Three visual placeholder comments were inserted, including the one that became Figure 7.1:

```
<!-- → [INFOGRAPHIC: The eight-section Cowork chapter structure — 8 vertical boxes, top to bottom, ink + ochre. Each box has section name and one-line description. No icons.] -->
```

**Step 2 — `07-cowork-draft-run-cajal.md`.** Three figures proposed. The Critical figure (Figure 7.1, MC trigger) was the eight-section structure flow diagram — it fired because the chapter describes eight sequential sections each draft follows. The SCOPE named the data, the constraint, and the load. One Important figure (Figure 7.2, five failure modes taxonomy, VG trigger) was accepted as-is. One Supplementary figure (Figure 7.3, a histogram of `[verify]` flag counts across draft runs, PQ trigger) was modified before generation — the original SCOPE called for ten bars; the data only supported five distinct buckets, so the SCOPE was edited down.

One CAJAL suggestion was rejected entirely: a fourth proposal for a wordcloud of common failure terms, flagged as Supplementary. Wordclouds violate the visual standard — they have no data-ink discipline, they cannot be made device-agnostic, and they encode nothing the prose doesn't already encode more precisely. Deleted from the `cajal.md` before the SVG step.

**Step 3 — SVG and PNG output.** Three SVG files at `images/07-cowork-draft-run-fig-01.svg` through `fig-03.svg`. The PNG converter produced three PNGs at 300 DPI. The enrichment pass inserted the markdown links:

```
![The eight-section Cowork chapter structure](../images/07-cowork-draft-run-fig-01.png)
*Figure 7.1 — Eight sections, run in order, no skipping. CAJAL output, edited.*
```

D3 companion files appeared for Figure 7.1 (the section-structure diagram, MC trigger) and Figure 7.3 (the histogram, PQ trigger). Figure 7.2 (the taxonomy, VG trigger) did not get a D3 companion — it is a static structural diagram, and an interactive version would be over-engineered for it. The enrichment pass made that judgment automatically.

---

CAJAL produces solid first-pass figures. For most handbook chapters that is enough. For chapters where the figure *is* the argument — where the page is dominated by a chart that the prose orbits around — two companion books in this series cover the territory the enrichment pass cannot.

*AI for Graphs* is the companion on chart-making with AI assistance for non-statisticians. The most relevant chapters for a handbook author: chart selection by question (Munzner's what-why-how applied as a decision flowchart — when is a small-multiples grid the right answer; when is a dual-axis chart never the right answer); the reading-on-device pass (render a chart at iPad, iPhone, e-ink, and PDF print sizes before committing); and reading a chart for what it is hiding (the Challenger O-ring case as the canonical figure that fails its argument — this is the chapter for catching the visual fluency trap).

*AI for Infographics* is the companion on instructional figures that replace sections of prose rather than illustrating them. The most relevant chapters: taxonomy figures (the structural diagram type Figure 7.2 belongs to; how to design one the reader can scan in twelve seconds; Williams's CRAP principles from *The Non-Designer's Design Book* applied to instructional layout[^williams]); process diagrams beyond linear flows (when to leave a flowchart behind for parallel tracks, branches, or feedback loops); and the accessibility audit (alt text, color-blind palettes, screen-reader-readable SVG structure).

You do not need either companion to finish your handbook. You need them when you are fighting CAJAL — when the default output is producing figures and you can see they are wrong but cannot say what would be right.

[^williams]: Williams, R. (2014). *The Non-Designer's Design Book* (4th ed.). Peachpit.

---

## AI Wayback Machine — Florence Nightingale

Most readers know Florence Nightingale as the nurse who reformed military hospital sanitation during the Crimean War. Fewer know that she designed the chart that did the reforming.

The figure was a polar-area diagram — the *Diagram of the Causes of Mortality in the Army in the East* (1858) — showing month by month that preventable disease killed far more British soldiers than battle wounds did. She designed it for Queen Victoria and Parliament, not for statisticians, because the standard mortality tables were not changing anyone's mind. The chart did. Sanitary reform of military hospitals followed. In 1859 she was elected the first female fellow of the Royal Statistical Society.

The chart earned its place by changing policy. That is the only criterion for a Critical figure that matters.

> **Prompt to run in Claude or ChatGPT:**
>
> "Visit the Wikipedia page for Florence Nightingale. Read the 'Statistics and sanitary reform' section. In 200 words, explain why her Rose Diagram is a figure that earned its place by Tufte's data-ink criteria. Then propose one figure in your own textbook draft that could be redesigned in the same spirit — surfacing the argument the data already supports. Name the specific chapter and figure you are testing, and ask whether the constraint that made Nightingale's choice right (audience, device, story) applies to your case."

---

## Exercises

**Exercise 9.1 (Apply) — Run the Chapter Finishing Pass.** Run the Chapter Finishing Pass on your book. Confirm every chapter has a one-line italic subtitle and at least two visual placeholder comments. For each subtitle, write one sentence answering: *what argument does this subtitle commit the chapter to?* If you cannot answer in one sentence, the subtitle is a territory label. Rewrite it.

**Deliverable:** A list of every chapter's subtitle and the one-sentence argument each names. Flag any subtitle you could not answer for.

**Exercise 9.2 (Apply) — Run CAJAL Image Suggest; audit one `cajal.md`.** Run CAJAL Image Suggest. Open the `cajal.md` for one chapter — pick the chapter you are most uncertain about visually. Confirm the Critical-ranked figure maps directly to one of the chapter's primary learning outcomes from your TIKTOC.md. If it does not, rewrite the SCOPE prompt until it does, or demote it. Identify one Supplementary-ranked figure you will skip and note the reason.

**Deliverable:** One edited `cajal.md` with at least one SCOPE rewrite and at least one deletion, plus a one-paragraph note explaining the editorial decisions.

**Exercise 9.3 (Apply) — Run the CAJAL SVG Generator and enrichment pass; audit three figures.** Run the CAJAL SVG Generator then the enrichment pass. Confirm at least one PNG per chapter exists in `images/`, at least one D3 file per chapter (where appropriate) exists in `d3/`, and the chapter files now contain markdown image links at the placeholder locations. Then open three figures at random and audit against the visual standard: two-color or three-color; flat fills; axes labeled, units declared, source and date present; `<title>` and `<desc>` in the SVG.

**Deliverable:** Three audited figures with a one-line pass/fail per criterion, plus one identified fix.

---

## Bridge — Chapter 10

The book is now visually complete. Subtitles surface the arguments. Figures encode what prose cannot encode efficiently. The PNGs render on every device. The SVGs are version-controlled and editable.

What is missing is the layer that makes this an *AI+1* textbook rather than a textbook about AI. The reader needs LLM exercises and Dig Deeper prompts that are only useful in this domain, for this reader, at this career stage. Chapter 10 adds that layer — and the fluency trap returns one final time, at pedagogy scale.

---

## Prompts

### Figure 9.1 — Anatomy of a visual placeholder comment
Build an annotated-schematic figure as a single self-contained HTML file with inline CSS and D3 7.9.0 from the cdnjs CDN. Data shape: one comment string decomposed into three segment objects (arrow, bracket type, brief) each with a downstream-role string (grep target, generator selector, figure brief). Marks: one horizontal bar at top segmented into three regions left to right; one callout line dropping from each region to a reserved role cell below. Channels: x-position within the bar encodes reading order of the comment syntax; each segment carries a distinct fill tint to separate the three parts; callout lines encode the segment-to-role mapping. Sort: fixed left-to-right syntax order (arrow, bracket, brief). Annotation: region labels and role-cell labels. No zero baseline (schematic). Deliverable: one HTML file, inline CSS, D3 7.9.0, responsive via ResizeObserver, role="img" with title and desc.

### Figure 9.2 — CAJAL figure-priority decision path
Build a top-to-bottom decision-tree flowchart as a single self-contained HTML file with inline CSS and D3 7.9.0 from the cdnjs CDN. Data shape: three decision-node objects (Critical, Important, Supplementary) each with a yes/no test string, plus two terminal outcomes (keep, skip) and one demote redirect off the Critical node. Marks: three stacked decision nodes; pass-through arrows linking each test to the next; a side outcome arrow per node; the Supplementary node terminating in a skip glyph; the Critical node showing one demote redirect arrow. Channels: vertical position encodes the order tests are applied; the keep outcome and skip glyph are visually distinguished. Sort: fixed Critical then Important then Supplementary order. Annotation: node test labels and outcome labels. No zero baseline (decision tree). Deliverable: one HTML file, inline CSS, D3 7.9.0, responsive via ResizeObserver, role="img" with title and desc.

### Figure 9.3 — The CAJAL pipeline: prose to publication artifact
Build a left-to-right systems flowchart as a single self-contained HTML file with inline CSS and D3 7.9.0 from the cdnjs CDN. Data shape: six node objects — Finishing Pass, CAJAL Image Suggest (cajal.md), SVG Generator (SVG source), svg-to-png converter (PNG), enrichment pass (markdown links), D3 companion (branch) — plus one source-versus-output divider flag. Marks: five main-flow nodes left to right joined by single arrows; the D3 node as one downward branch off the SVG/source stage; a divider glyph separating source artifacts (SVG, D3) from the PNG that ships in the EPUB. Channels: x-position encodes pipeline sequence; the PNG/ships node and the D3 branch each carry a distinct fill to mark the source-versus-output split. Sort: fixed pipeline order 1 to 5 with the branch off stage 3. Annotation: node labels and a source/ships divider label. No zero baseline (process diagram). Deliverable: one HTML file, inline CSS, D3 7.9.0, responsive via ResizeObserver, role="img" with title and desc.

---

## References

1. Knaflic, C. N. (2015). *Storytelling with Data*. Wiley. https://www.wiley.com/en-us/Storytelling+with+Data:+A+Data+Visualization+Guide+for+Business+Professionals-p-9781119002253
2. Munzner, T. (2014). *Visualization Analysis and Design*. CRC Press. https://infovis-wiki.net/wiki/Munzner,_T.:Visualization_Analysis_and_Design,_A_K_Peters/CRC_Press,_2014
3. W3C (2023). *EPUB Accessibility 1.1*. https://www.w3.org/TR/epub-a11y-11/
4. Tufte, E. R. (2001). *The Visual Display of Quantitative Information* (2nd ed.). Graphics Press. https://infovis-wiki.net/wiki/Data-Ink_Ratio
5. Bateman, S., et al. (2010). "Useful Junk? The Effects of Visual Embellishment on Comprehension and Memorability of Charts." *CHI 2010*. https://dl.acm.org/doi/10.1145/1753326.1753716
6. Royal Statistical Society (2020). "Nightingale 2020: the bicentenary of our first female fellow." https://rss.org.uk/news-publication/news-publications/2020/general-news/nightingale-2020-the-bicentenary-our-first-female/
