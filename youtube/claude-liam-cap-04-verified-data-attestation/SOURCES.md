# SOURCES — claude-liam-cap-04-verified-data-attestation
# "Every Number Traces." | Reallocation Engine Capstone · E4 of 8

## Verbatim quotes (3 required by VERBATIM QUOTE LAW)

### Quote 1 — B05 (Mechanism · Give/Keep boundary)
> "The test: can the model verify this against reality, or only against itself? If only against itself, it's yours."
- Source: chapters/16-the-build-and-the-honest-run.md — Give to AI / Keep for yourself table caption

### Quote 2 — B06 (Mechanism · honesty gate)
> "An engine that optimizes your search by shading the truth is the failure mode this book exists to prevent — fluency in the service of a false impression is still a false impression, and it is worse when it arrives in a polished format."
- Source: chapters/16-the-build-and-the-honest-run.md — "The ethics gate" section, Honesty paragraph

### Quote 3 — B07 (Mechanism · one-question test)
> "For any sentence in a system output, one question settles it: could this sentence have been produced by counting records? If yes, it must trace to a script output or an audit report. If it cannot be traced, it is not allowed to stand."
- Source: chapters/03-the-verified-data-contract.md

## Self-demo source
- Command: `sed -n '113,130p' assignments/ASSIGNMENT-professional-contribution-capstone-250pt.md`
- Real output verified at build time: lines 113-130 show Step 3 header, seven label types, and ethics gate definition (privacy + honesty) including "If either fails, the run does not happen."
- No generation. No credits. $0.00.

## Content grounding
- Seven label types (record / script-output / local-evidence / external-source / model-inference / your-input / missing): assignment Step 3 lines 113-120
- Ethics gate (privacy + honesty, both non-optional): assignment Step 3 lines 123-125; chapters/16-the-build-and-the-honest-run.md "The ethics gate"
- Give/Keep table + boundary test: chapters/16-the-build-and-the-honest-run.md "The boundary, made operational"
- One-question test: chapters/03-the-verified-data-contract.md
- "If either fails, the run does not happen": assignment Step 3; chapters/16-the-build-and-the-honest-run.md
- Human signs attestation, not model: assignment criterion 6 ("never self-certifies honesty — a human signs the attestation")
