# SOURCES — claude-liam-cap-03-two-customer-pair
# "Recipe for AI, Card for Human." | Reallocation Engine Capstone · E3 of 8

## Verbatim quotes (3 required by VERBATIM QUOTE LAW)

### Quote 1 — B05 (Mechanism · shared contract)
> "An agent that loads the shared contract before running the first command operates inside a defined constraint. An agent that skips it operates from its own priors."
- Source: chapters/04-two-customers.md — "What each artifact contains" section

### Quote 2 — B06 (Mechanism · failure modes)
> "That last section is the one that gets skipped when someone writes a recipe fast. And it is the one you need most at eleven PM on a Thursday when the output looks wrong and you don't know why."
- Source: chapters/04-two-customers.md — after Table 4.1

### Quote 3 — B07 (Mechanism · future-you)
> "The reader who has forgotten everything is not a hypothetical. It is you in three months. The human artifact is a letter you are writing to that person. Write it like it is."
- Source: chapters/04-two-customers.md — "Both artifacts honor the verified-data contract" section

## Self-demo source
- Command: `sed -n '105,109p' assignments/ASSIGNMENT-professional-contribution-capstone-250pt.md`
- Real output verified at build time: lines 105-109 show all nine recipe sections and human card fields
- No generation. No credits. $0.00.

## Content grounding
- Nine recipe sections: assignment Step 2 lines 105-107
- Human card fields (purpose, can/can't verify, dependencies, annotated commands, what it produces, failure modes): assignment Step 2 lines 107-109
- recipes/_shared.md as required read: chapters/04-two-customers.md, "What each artifact contains"
- Table 4.1 (AI vs human artifact structural difference): chapters/04-two-customers.md
- Failure modes as the skipped section: chapters/04-two-customers.md, after Table 4.1
- Future-you as the human customer: chapters/04-two-customers.md, "Both artifacts honor the verified-data contract"
- Same-commit enforcement: chapters/04-two-customers.md, "Drift is a failure mode"
