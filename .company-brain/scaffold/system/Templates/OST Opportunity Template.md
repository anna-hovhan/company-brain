<%*
const f = tp.file.folder(true);
const layer = f.startsWith("Company") ? "company" : f.startsWith("Teams") ? "team" : "personal";
const team = f.startsWith("Teams/") ? f.split("/")[1] : "";
const parent = await tp.system.prompt("parent outcome or opportunity, as [[OUT - Name]]");
-%>
---
date: <% tp.date.now("YYYY-MM-DD") %>
type: opportunity
tags: [opportunity, discovery]
ai-first: true
layer: <% layer %>
team: <% team ? '"[[' + team + ']]"' : "" %>
parent: "<% parent %>"
segment: "[[TBD]]"
evidence: []
opportunity_size: 3
status: open
---

# <% tp.file.title %>

## For future agent
This note is an opportunity in an opportunity solution tree under <% parent %>: a customer need, pain, or desire, framed from the customer's point of view and backed by the evidence listed. It is not a solution.

## Opportunity
TBD. In the customer's words where possible: "I struggle to...", "I wish I could...".

## Evidence
Interview notes, support tickets, analytics, each linked and dated. Without evidence this is an assumption, not an opportunity.
- TBD

## Sizing
- How many customers have it: TBD
- How often: TBD
- How painful or valuable: TBD
- Fit with our strategy and VPC: TBD

## Solutions
```dataview
TABLE impact, effort, confidence, status, roadmap
WHERE type = "solution" AND contains(string(parent), this.file.name)
```

## Sub-opportunities
```dataview
LIST WHERE type = "opportunity" AND contains(string(parent), this.file.name)
```
