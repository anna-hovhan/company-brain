<%*
const f = tp.file.folder(true);
const layer = f.startsWith("Company") ? "company" : f.startsWith("Teams") ? "team" : "personal";
const team = f.startsWith("Teams/") ? f.split("/")[1] : "";
const parent = await tp.system.prompt("parent opportunity, as [[OPP - Name]]");
const impact = await tp.system.prompt("impact 1-5", "3");
const effort = await tp.system.prompt("effort 1-5", "3");
-%>
---
date: <% tp.date.now("YYYY-MM-DD") %>
type: solution
tags: [solution, discovery]
ai-first: true
layer: <% layer %>
team: <% team ? '"[[' + team + ']]"' : "" %>
parent: "<% parent %>"
impact: <% impact %>
effort: <% effort %>
confidence: medium
reach: 
status: idea
roadmap: none
project: ""
---

# <% tp.file.title %>

## For future agent
This note is a candidate solution for the opportunity <% parent %>, scored impact <% impact %> and effort <% effort %> on 1-5 scales for the effort-impact matrix. Status and roadmap fields say how far it has progressed; assumption tests are the experiments linked below.

## Solution
TBD. What we would build or change, in one paragraph.

## Why it addresses the opportunity
TBD

## Scoring rationale
- Impact (1-5) because: TBD
- Effort (1-5) because: TBD
- Confidence (high, medium, low) because: TBD
- Reach (optional, for RICE: customers or events per quarter): TBD

## Riskiest assumptions
| Assumption | Type | Test |
|---|---|---|
| TBD | desirability / viability / feasibility / usability / ethical | TBD |

## Experiments
```dataview
TABLE assumption_type, method, result
WHERE type = "experiment" AND contains(string(parent), this.file.name)
```

Method: [[Opportunity Solution Tree]], [[Effort-Impact Matrix]].
