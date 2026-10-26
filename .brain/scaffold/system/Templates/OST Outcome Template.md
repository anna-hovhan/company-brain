<%*
const f = tp.file.folder(true);
const layer = f.startsWith("Company") ? "company" : f.startsWith("Teams") ? "team" : "personal";
const team = f.startsWith("Teams/") ? f.split("/")[1] : "";
const kr = await tp.system.prompt("key result this outcome drives, as [[Objective note#^kr1]]", "");
const metric = await tp.system.prompt("metric, for example median minutes to first value");
-%>
---
date: <% tp.date.now("YYYY-MM-DD") %>
type: outcome
tags: [outcome, discovery]
ai-first: true
layer: <% layer %>
team: <% team ? '"[[' + team + ']]"' : "" %>
kr: "<% kr %>"
metric: "<% metric %>"
status: active
owner: "[[TBD]]"
---

# <% tp.file.title %>

## For future agent
This note is the desired outcome at the root of an opportunity solution tree: a measurable result (<% metric %>) tied to <% kr %>. Opportunities below it are customer needs discovered through research; the tree view is generated in the discovery hub.

## Outcome
TBD. A product or business outcome the team can influence, not an output.

## Current and target
- Baseline (with date): TBD
- Target: TBD

## Opportunities
```dataview
TABLE opportunity_size, status, segment
WHERE type = "opportunity" AND contains(string(parent), this.file.name)
SORT opportunity_size DESC
```

## Research cadence
Who talks to customers, how often, and where interview notes live: TBD

Method: [[Opportunity Solution Tree]].
