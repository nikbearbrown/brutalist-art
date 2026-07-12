# Chapter 11 — Creating Figures

*Why the hard part of a figure is deciding what to leave out.*

---

A designer-author types a sentence into an image model: *"A diagram showing how the Cowork pipeline turns a TIKTOC.md into a finished book."* Ten seconds later a picture arrives. It is beautiful. It has gradient-filled boxes, soft drop shadows, fourteen labeled nodes, three legends, a pair of decorative gears, and an arrow that loops back on itself for reasons no one can explain. It looks like it came from a consulting deck. The author stares at it. Then they try to follow it — to trace, with a finger, the path a manuscript actually takes through the pipeline — and they cannot. The arrows go everywhere. Two of the labels contradict the prose they were drawn from. One word is misspelled in a font no one chose.

The figure is not wrong, exactly. It is full. And a figure that is full is a figure that has made no decisions.

This is the visual fluency trap, arriving at the level of the picture. You met its verbal cousin in Chapter 1 — prose that reads correct and means nothing. You met it again in Chapter 9, where a chart can be technically a chart and semantically empty. Here is the version that costs you most, because images carry more authority than sentences. A reader will distrust a clumsy paragraph and give a polished diagram the benefit of the doubt. The polish *is* the danger.

Chapter 9 gave you the production pipeline — the finishing pass that marks where figures go, CAJAL Image Suggest proposing candidates, the SVG-to-PNG build that makes them real. This chapter goes underneath that pipeline to the craft it runs on. Not *how do I generate a figure* — generation is free now, and free is the whole problem. The question is *how do I decide what a single figure is allowed to contain*, and how do I make a machine that wants to give me everything give me only that.

The skill has a name in this toolchain. It is called CAJAL, and it is not tied to this book. It works the same on a signaling cascade, a treaty structure, a monetary-transmission mechanism, or a pipeline diagram. Learn it once here and it transfers to every book in the series — and to any figure you ever commission again. The full CAJAL command set and the SVG Style Guide are in Appendix I.

---

## A figure is a cognitive commitment

Start with the constraint that governs everything else, because it is a fact about the reader's head, not a matter of taste.

In 1956 George Miller published the most cited paper in the history of psychology, "The Magical Number Seven, Plus or Minus Two," and fixed in everyone's mind that working memory holds about seven items.[^miller] The number turned out to be optimistic. Nelson Cowan, reviewing decades of tighter experiments in 2001, put the real capacity at closer to four chunks — four independent things a mind can hold and relate at once before something falls out.[^cowan] Not four thousand. Four.

A figure is a request that the reader hold its parts in working memory simultaneously and see how they relate. That is the entire job of a figure: relation. If the figure shows four interacting components, a reader can hold them. If it shows fourteen, the reader holds the first four, loses them fetching the next four, and walks away with the *impression* of having understood — which is worse than confusion, because confusion at least knows itself.

John Sweller built a whole instructional theory on this, cognitive load theory: the load a learner can carry is fixed and small, so every element competing for attention that is not doing teaching work is actively subtracting from the elements that are.[^sweller] Decoration is not neutral. A gradient is not free. The two ornamental gears in the diagram above did not merely fail to help; they consumed capacity a reader needed for the arrows.

So here is the trade-off, named plainly, because every figure decision is a trade between the two:

**Comprehensiveness versus comprehension.** Everything you add to show how complete your understanding is, you subtract from the reader's ability to follow it. The figure that contains your whole mental model teaches nothing. The figure that contains one relation, cleanly, teaches that relation.

This is why the operative rule across the entire craft is a ceiling: **six to eight labeled components per figure, and never more.** Not as a stylistic preference — as a working-memory budget. When a concept genuinely has more than eight moving parts, the answer is not a smaller font and a bigger canvas. The answer is two figures.

![Two vertical bars on a shared zero-based count axis — a taller bar for Miller's seven-item claim and a shorter bar for Cowan's four-chunk capacity — crossed by a horizontal threshold line marking the six-to-eight component ceiling.](../images/11-creating-figures-fig-01.png)
*Figure 11.1 — The component ceiling: seven vs four*

Knowing *when* to split is itself a decision with criteria. The cleanest test is Cowan's number applied directly: more than four distinct interacting components, and you are probably past one figure. Branching structure — parallel paths, competing outcomes, a policy that hits the economic and legal and social systems at once — splits, because branches multiply the relations a reader must track. A process that crosses scales (individual to institution to society; short-run to long-run) splits, because forcing a reader to translate between scales inside one frame is its own load. The reductive instinct here is correct. When in doubt, the figure wants to be two figures.

[^miller]: Miller, G. A. (1956). "The Magical Number Seven, Plus or Minus Two." *Psychological Review*, 63(2), 81–97.
[^cowan]: Cowan, N. (2001). "The magical number 4 in short-term memory." *Behavioral and Brain Sciences*, 24(1), 87–114.
[^sweller]: Sweller, J. (1988). "Cognitive Load During Problem Solving." *Cognitive Science*, 12(2), 257–285.

---

## SCOPE, and the parameter that does the work

If the component ceiling is the constraint, SCOPE is the instrument for staying under it. It is the five-part frame CAJAL builds every figure prompt around, and the order matters less than the fact that all five are answered before a single pixel is requested.

**S — Specification.** The physical facts: canvas size, format, the publisher style you are targeting. A single-column 89mm textbook figure and a double-column 180mm *Nature* panel are different objects, and deciding which one you are making is not a detail you resolve afterward.

**C — Content.** Only the concepts, entities, and relationships you have explicitly confirmed belong. Precise terms. Nothing inferred, nothing "while we're at it."

**O — Organization.** The spatial logic. Process and causation run left to right; an arrow (→) means progression, a bar (⊣) means blockage. Comparison goes side by side against a shared axis. The layout is an argument about how the parts relate.

**P — Presentation.** Flat vector, a colorblind-safe palette with the hex values named, uniform strokes, white ground. One counterintuitive rule lives here, and it is worth pausing on: **you do not tell the image generator what aesthetic to use.** You specify content, layout, color mapping, and exclusions. The generator chooses the look. Removing style suggestions reliably improves the output, because the model is better at rendering a clean diagram than at obeying your taste while also getting the structure right.

**E — Exclusions.** The list of what must not appear. And this is the parameter that does the work.

Here is the claim at the center of the whole craft, the one sentence to carry out of this chapter: **the exclusion list is more important than the inclusion list.** Anyone can say what a figure is about. The figures that fail — the fourteen-node monsters — fail because no one ever wrote down what the figure was *not* about. Left without that list, every image model defaults to comprehensive. It will pull in adjacent concepts, upstream context, the downstream implications, the related framework you mentioned once. A populated E block is the difference between a figure that clarifies and a figure you spend an afternoon editing clutter out of. A SCOPE prompt without an E block is not finished.

![Five stacked horizontal bands in fixed S-C-O-P-E order, with the bottom E band rendered visibly larger than the four uniform bands above it to encode its dominant weight.](../images/11-creating-figures-fig-02.png)
*Figure 11.2 — The SCOPE frame, E carries the weight*

This is also where the tool's two personalities diverge, and choosing between them is a real decision. In **silent mode**, CAJAL infers concept, audience, and components from whatever text you hand it and returns a clean SCOPE immediately — no questions. Fast, and correct often enough to be useful when you already know what you want. In **interactive mode**, it refuses to move until you have answered, in order: what chapter is this for; what is the concept, in exactly one sentence; what does the reader already know; what are the three-to-eight components; and — the gate it holds hardest — what must not appear. It will not generate output while the exclusion list is empty.

The gates are not bureaucracy. They are the order in which a figure has to be decided to come out clarifying. Skip the one-sentence concept and you get a figure about two things. Skip the audience and you get components a novice can't read or an expert doesn't need. Skip the exclusions and you get the consulting deck. Silent mode trades the gates for speed; you take that trade knowingly, on figures simple enough that the inference is safe.

![Two left-to-right tracks converging on one shared SCOPE-output node — a top track running a single silent node straight to the output, and a bottom track passing through five sequential gate nodes whose final exclusions gate is drawn as a hard blocking lock.](../images/11-creating-figures-fig-03.png)
*Figure 11.3 — Silent vs interactive mode gates*

Before any of this, the tool reads the chapter and triages — one pass per *concept*, not per section, because a section with six ideas wants six independent decisions, not one averaged compromise. Three signals fire a figure. **Mechanism complexity:** a process with three or more interdependent steps. **Verification gap:** a structural claim the reader can't confirm from prose alone — "the test has fourteen items in two groups" is something you must be *shown*. **Proportional or quantitative:** any number that compares to another number. Each candidate comes ranked. Critical means the reader misunderstands a core claim without it. Important means it cuts real cognitive load. Supplementary means the prose stands without it — and the honest fate of most Supplementary figures is the cutting-room floor. A textbook is not improved by a figure on every page.

---

## Two palettes, one rule, and the file that ships

A figure that has decided what it contains still has to render — and render across a Kindle library that spans a retina iPad and a six-year-old e-ink Paperwhite. The constraints here look like style. They are really about degrading gracefully across hardware you will never see.

There are, honestly, two color systems in play, and it helps to know why. The first is **Okabe-Ito** — an eight-color palette engineered to stay distinct for colorblind readers, which Elsevier, Wiley, and Springer Nature accept and red-green combinations fail.[^okabeito] This is the discipline-agnostic default, the one CAJAL specifies inside a SCOPE block, so the figure is submission-ready to a journal in any field. The second is the house skin: the **Bear Brown / Brutalist D3** palette the AI+1 renderer actually paints with — ink (`#2a1a0e`, warmer than black), one red (`#C8102E`) for the single highlighted data series, ochre (`#C8860E`) for decorative accents and *never* for data, and a ladder of neutral grays. CAJAL decides the figure's logic in the publisher-neutral system; the series renderer dresses it in the brand. Different layers, different jobs.

Both bow to one non-negotiable rule, and if you remember nothing else about color, remember this: **every figure must survive grayscale.** About eight percent of men have some red-green color deficiency, and every e-reader has a grayscale mode. So each color that encodes data must sit in its own luminance band — ink at the dark end, red in the mid-dark, grays laddered up toward the near-white plot field. Print the figure in black and white. If two data colors become the same gray, the figure has failed for a real fraction of its readers, and you add a second encoding — a pattern, a direct label — before you proceed.

The rest of the house style follows from the same device-agnostic logic. Flat fills only: a gradient is a smooth ramp on the iPad and a banded mess on e-ink. No rounded corners, no drop shadows — contemporary in Figma, pixelated at reflow. A fixed `viewBox` of 700×420, a 32-pixel margin, labels on an eight-pixel grid. And every SVG carries a `<title>` and a `<desc>` and a `role="img"`, which is an EPUB 3 accessibility requirement and doubles as a fact-check: alt text that drifts from what the figure shows is a flag that one of the two is wrong.[^w3c]

One production rule sounds like fussiness and is actually the most important defense against embarrassment: **no text labels baked into the generated image.** You request a blank, unannotated diagram and apply every word afterward, on a separate layer. The reason is mechanical. Image models hallucinate text — they produce confident, misspelled, illegible characters, the way the diagram at the top of this chapter misspelled a word in a font no one chose. Separate the picture from the words and that failure mode disappears completely.

Then there is the matter of which file is the book. The SVG is the source — editable, version-controlled, re-renderable at any resolution, the thing that survives a redesign. The PNG, rendered at 300 DPI by the converter you installed in Chapter 9, is the publication artifact — what Kindle's reflow engine renders reliably on every device. The D3 HTML file is a third thing: authorable source for any figure with live data underneath it, useful for the next edition or a companion website, not for the EPUB, which does not reliably run JavaScript. The relationship is exactly the one you already know from `combined.md` to EPUB. You edit the source and rebuild. You never edit the artifact the device renders.

[^okabeito]: Okabe, M., & Ito, K. (2008). "Color Universal Design (CUD): How to make figures and presentations that are friendly to colorblind people." jfly.uni-koeln.de/color/.
[^w3c]: W3C. (2023). *EPUB Accessibility 1.1*. w3.org/TR/epub-a11y-11/.

---

## Worked example: one figure, decided out loud

Take a concept from earlier in this book and run it through an interactive session, so you can watch the exclusions do their work. The concept: the eight-section structure every Cowork-drafted chapter follows, from Chapter 7.

**Concept, one sentence.** *A Cowork chapter draft is assembled from eight named sections, run in a fixed order.* That sentence passes the gate — it has one center, not two. An early draft of it read "the eight sections and how the Chapter Writer and pantry feed them," which is two figures wearing one sentence; the tooling belongs elsewhere.

**Audience.** A reader who has finished Chapter 7 and knows what the Chapter Writer is. So the figure does not need to re-explain Cowork, the pantry, or what a draft is. That prior knowledge is capacity you do not have to spend.

**Inclusion list.** Eight boxes — one per section — each with its name and a one-line statement of what it does. Eight is at the ceiling, which is the signal to check: is this one figure or two? It is one, because the relation is a single linear sequence with no branches. A ninth component would force the split.

**Exclusion list** — the gate held hardest. *No icons. No screenshots of the interface. No depiction of the pantry or the Writer. No arrows looping back (the sequence runs once, top to bottom). No word counts, no runtimes, no example prose.* Every one of those is a true, relevant fact about chapter drafting. Every one of them, in this figure, is clutter that would push a reader past four held chunks.

**Figure type and SCOPE.** A vertical process flow — eight boxes, top to bottom, a single arrow between each. The SCOPE block writes itself once the decisions are made:

```
S — Single column, 89mm, vertical flow, 8 boxes. 300 DPI PNG + SVG source.
C — One box per section: name + one-line function. Eight sections only.
O — Top-to-bottom, one arrow between adjacent boxes. No branches, no loops.
P — Flat vector. Ink boxes on white, one accent on the first box. No icons.
E — No interface screenshots. No pantry/Writer depiction. No metrics.
    No return arrows. No example text inside boxes.
```

![Eight identical section boxes stacked vertically and connected by a single downward arrow between each adjacent pair — a flat linear sequence sitting exactly at the eight-component ceiling, with no branches or return loops.](../images/11-creating-figures-fig-04.png)
*Figure 11.4 — The worked example: eight-section vertical process flow*

What did the discipline buy? A reader scans the figure in about twelve seconds and leaves knowing the sequence — which was the only job. The version without an exclusion list would have arrived with a Cowork logo, a sidebar of token counts, and a helpful loop back to the top, and it would have taught the sequence to no one.

---

The deeper point is that none of these decisions were about this book. Swap the eight sections for the stages of glycolysis, the clauses of a treaty, or the steps of a monetary-transmission mechanism, and the moves are identical: state the concept in one sentence, name what the reader already knows, hold the component ceiling, and write down what must not appear. The craft is portable because working memory is. That is why this chapter sits in a book about making textbooks with AI and would sit, unchanged, in a book about anything else.

---

## AI Wayback Machine — Santiago Ramón y Cajal

The tool is named after a person, and the person is the lesson.

Santiago Ramón y Cajal won the 1906 Nobel Prize for showing that the nervous system is built from discrete cells — neurons — rather than one continuous web. He proved it, in large part, with drawings. Working in the 1890s and 1900s, he would sit at the microscope for hours, then draw the neural tissue from memory at a separate table. That detail matters. He was not tracing what he saw. He was reconstructing the essential structure, and in the gap between the slide and the page he left things out — the debris, the artifacts of staining, the cells that did not bear on the argument. His figures are reductions, not reproductions.

They are also still in textbooks, more than a century later, which is not true of almost any photograph of neural tissue from the same period. They survived because a trained human decided what mattered and excluded the rest. A modern stain shows more. Cajal's drawing shows *the point*.

That is the exclusion list, a hundred years early. The figure earns its place not by containing everything true, but by containing only what teaches.

> **Prompt to run in Claude or ChatGPT:**
>
> "Find images of Santiago Ramón y Cajal's neuron drawings and read about his method of drawing from memory after leaving the microscope. In 200 words, explain how his deliberate exclusions — what he left out of each drawing — are what made the figures last. Then take one figure planned for your own book, name three specific things you could exclude from it, and say what each exclusion would buy the reader in working-memory terms."

---

## Exercises

**Exercise 11.1 (Apply) — Write the exclusion list you skipped.** Open one `cajal.md` from your Chapter 9 run and pick a Critical-ranked figure. Ignore its inclusion list for a moment and write its exclusion list from scratch: name at least five true, relevant things about the concept that must *not* appear in this figure. For each, write one clause naming what the exclusion buys — the working-memory chunk it protects.

**Deliverable:** One figure's exclusion list, five items minimum, each with its one-clause justification. If you cannot find five things to exclude, the concept is probably too thin to need a figure — note that instead.

**Exercise 11.2 (Apply) — Run one figure through an interactive SCOPE session.** Take the same figure and run it through the five gates by hand: concept in exactly one sentence; what the reader already knows; the three-to-eight component inclusion list; the exclusion list from 11.1; figure type. Write the full SCOPE block (S/C/O/P/E). Confirm the component count is eight or fewer. If it exceeds eight, apply the split test — components, branching, scale — and state where the second figure begins.

**Deliverable:** One complete SCOPE block plus a one-sentence verdict: one figure, or two, and why.

**Exercise 11.3 (Apply) — Test a figure in grayscale.** Take one rendered figure from your book that uses more than one color to encode data. View or print it in grayscale. For each data color, name its approximate luminance band (dark / mid / light). If any two data categories become indistinguishable in grayscale, add a second encoding — a pattern, a direct label — and note the fix.

**Deliverable:** One figure assessed in grayscale, a pass/fail per data color, and either a confirmation that all bands are distinct or the specific second encoding you added.

---

## Bridge — Chapter 12

The figures are now decided, not just generated — each one holding a single relation a reader can carry, each one surviving grayscale and reflow, each one having left out more than it kept.

The book is, at this point, as good as the author and the pipeline can make it. What remains is the part no generator can do for you: checking that every claim in it is true, building the files a store will accept, and shipping. Chapter 12 runs the final fact-check, builds the EPUB and the PDF, and submits the book to the world — where it discovers what the pipeline could not check on your behalf.

---

## Prompts

### Figure 11.1 — The component ceiling: seven vs four
Build a two-bar comparison chart as a single self-contained HTML file with inline CSS and D3 7.9.0 from the CDN. Data: two values on a shared count axis — Miller's claim at 7 and Cowan's revised capacity at 4 — plus a horizontal reference line at the 6-to-8 component ceiling (draw the line at 7). Marks: two vertical bars and one horizontal threshold line. Channels: x position encodes the named source; bar height encodes item count. Use a linear y-scale with a zero baseline; bars must rise from zero. Keep the two bars in author order (Miller then Cowan); do not sort by value. Annotate the threshold line as the component ceiling and label each bar with its source and value. Use the red series color for the threshold line only; render both bars in neutral palette grays. Deliverable: one HTML file, role="img" SVG with title and desc, ResizeObserver redraw, dark-mode and reduced-motion media queries.

### Figure 11.2 — The SCOPE frame, E carries the weight
Build a stacked-band schematic as a single self-contained HTML file with inline CSS and D3 7.9.0 from the CDN. Data: five bands in fixed top-to-bottom order S, C, O, P, E, where E carries a larger weight than the four uniform bands above it. Marks: five horizontal rectangles stacked vertically. Channels: vertical position encodes SCOPE order; band height (and a single accent fill) encodes E's dominant weight. Keep bands in fixed S-to-E order; do not sort. No quantitative axis. Annotate each band with its SCOPE letter and label E as the parameter that does the work. Use the red series color for the E band emphasis only; render S, C, O, P in neutral palette grays. Deliverable: one HTML file, role="img" SVG with title and desc, ResizeObserver redraw, dark-mode and reduced-motion media queries.

### Figure 11.3 — Silent vs interactive mode gates
Build a two-path flow diagram as a single self-contained HTML file with inline CSS and D3 7.9.0 from the CDN. Data: a top path of one silent node flowing directly to a shared SCOPE-output node, and a bottom path of five sequential gate nodes (chapter, one-sentence concept, prior knowledge, components, exclusions) flowing to the same output, with the final exclusions gate marked as a hard blocking lock. Marks: rectangle nodes joined by left-to-right arrows, plus a lock glyph on the exclusions gate. Channels: y position separates the two tracks; x position encodes gate order on the bottom track; the lock glyph encodes the held-hardest gate. Keep gates in fixed order; do not sort. No quantitative scale. Annotate each node and mark the shared output. Use the red series color for the exclusions lock only. Deliverable: one HTML file, role="img" SVG with title and desc, ResizeObserver redraw, dark-mode and reduced-motion media queries.

### Figure 11.4 — The worked example: eight-section vertical process flow
Build a vertical process flowchart as a single self-contained HTML file with inline CSS and D3 7.9.0 from the CDN. Data: eight identical section boxes in a single linear sequence, connected by one downward arrow between each adjacent pair (the deliberate at-ceiling case). Marks: eight uniform rectangles and seven connecting arrows. Channels: vertical position encodes sequence order; no branches, no loops, no return arrows. Keep boxes in fixed sequence order; do not sort. No quantitative scale. Annotate each box with its section name and the entry box distinctly. Use the red series color for the first (entry) box only; render the remaining seven in neutral palette grays. Deliverable: one HTML file, role="img" SVG with title and desc, ResizeObserver redraw, dark-mode and reduced-motion media queries.

---

## References

1. Miller, G. A. (1956). "The Magical Number Seven, Plus or Minus Two." *Psychological Review*, 63(2), 81–97. https://en.wikipedia.org/wiki/The_Magical_Number_Seven,_Plus_or_Minus_Two
2. Cowan, N. (2001). "The magical number 4 in short-term memory." *Behavioral and Brain Sciences*, 24(1), 87–114. https://pubmed.ncbi.nlm.nih.gov/11515286/
3. Sweller, J. (1988). "Cognitive Load During Problem Solving." *Cognitive Science*, 12(2), 257–285. https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1202_4
4. Okabe, M., & Ito, K. (2008). "Color Universal Design (CUD)." jfly.uni-koeln.de/color/. https://conceptviz.app/blog/okabe-ito-palette-hex-codes-complete-reference
5. W3C (2023). *EPUB Accessibility 1.1*. https://www.w3.org/TR/epub-a11y-11/
6. NobelPrize.org. "Life and discoveries of Santiago Ramón y Cajal." https://www.nobelprize.org/prizes/medicine/1906/cajal/article/
