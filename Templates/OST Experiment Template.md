<%*
const f = tp.file.folder(true);
const layer = f.startsWith("Company") ? "company" : f.startsWith("Teams") ? "team" : "personal";
const team = f.startsWith("Teams/") ? f.split("/")[1] : "";
const parent = await tp.system.prompt("solution being tested, as [[SOL - Name]]");
const assumption = await tp.system.prompt("assumption being tested");
const assumption_type = await tp.system.prompt("assumption_type: desirability, viability, feasibility, usability or ethical", "desirability");
-%>
---
date: <% tp.date.now("YYYY-MM-DD") %>
type: experiment
tags: [experiment, discovery]
ai-first: true
layer: <% layer %>
team: <% team ? '"[[' + team + ']]"' : "" %>
parent: "<% parent %>"
assumption: "<% assumption %>"
assumption_type: <% assumption_type %>
method: "TBD"
success_criteria: "TBD"
result: pending
owner: "[[TBD]]"
---

# <% tp.file.title %>

## For future agent
This note is an assumption test for <% parent %>. It records the assumption (<% assumption %>), the method, the success criteria set before running it, and the result. Result pending means no conclusion yet.

## Assumption
<% assumption %>

## Method
TBD. Fastest, cheapest test that could prove it wrong (prototype test, one-question survey, data mining, fake door, concierge).

## Success criteria (set before running)
TBD

## Result
TBD. Data, date, and what it means for the solution: keep, change, or drop.

## Next step
TBD
