---
date: {{TODAY}}
type: hub
tags: [hub, discovery]
ai-first: true
layer: company
---

# Company Discovery

## For future agent
This is the company discovery hub: opportunity solution trees that connect each desired outcome (usually a key result) to customer opportunities, candidate solutions, and assumption tests. The trees below are generated from the OUT, OPP, SOL, and EXP notes in this folder.

## How to read this
Each tree starts at an outcome, branches into opportunities (customer needs, pains, desires, backed by evidence), then solutions, then experiments that test the riskiest assumptions. See [[Opportunity Solution Tree]]. Each tree also has a canvas file whose cards are the real notes. Add nodes with `/company-brain:ost`; then `brain refresh` redraws everything.

## Open experiments
```dataview
TABLE parent, assumption_type, result
FROM "Company/Discovery"
WHERE type = "experiment" AND result = "pending"
```

<!-- brain:auto:start ost -->
No outcomes yet. Start a tree with `/company-brain:ost`.
<!-- brain:auto:end ost -->
