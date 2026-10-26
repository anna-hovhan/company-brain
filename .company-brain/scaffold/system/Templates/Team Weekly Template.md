<%*
const f = tp.file.folder(true);
const layer = f.startsWith("Company") ? "company" : f.startsWith("Teams") ? "team" : "personal";
const team = f.startsWith("Teams/") ? f.split("/")[1] : "";
-%>
---
date: <% tp.date.now("YYYY-MM-DD") %>
type: team-weekly
tags: [team-weekly, weekly]
ai-first: true
layer: <% layer %>
team: <% team ? '"[[' + team + ']]"' : "" %>
week: <% tp.date.now("GGGG-[W]WW") %>
contributors: []
---

# <% tp.file.title %>

## For future agent
This note is the team roll-up for <% tp.date.now("GGGG-[W]WW") %>, aggregated from members' team updates: highlights, key result status, risks, decisions needed, and next week's focus.

## Summary
TBD. Three sentences for someone outside the team.

## Updates
```dataview
TABLE author, krs
FROM "Teams"
WHERE type = "team-update" AND week = this.week AND file.folder = this.file.folder
```

## KR status
| Objective | KR | Progress | Confidence | Trend |
|---|---|---|---|---|

## Highlights
- TBD

## Risks and blockers
- TBD

## Decisions needed
- TBD

## Next week
- TBD
