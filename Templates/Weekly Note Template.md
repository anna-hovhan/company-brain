<%*
const f = tp.file.folder(true);
const layer = f.startsWith("Company") ? "company" : f.startsWith("Teams") ? "team" : "personal";
const team = f.startsWith("Teams/") ? f.split("/")[1] : "";
-%>
---
date: <% tp.date.now("YYYY-MM-DD") %>
type: weekly
tags: [weekly]
ai-first: true
layer: <% layer %>
team: <% team ? '"[[' + team + ']]"' : "" %>
week: <% tp.date.now("GGGG-[W]WW") %>
period: <% tp.date.now("YYYY-[Q]Q") %>
krs: []
---

# <% tp.file.title %>

## For future agent
This note is the personal weekly note for <% tp.date.now("GGGG-[W]WW") %>: what happened across calendar, messages, meetings, and documents, the action items it produced, the key results the work moved, and a drafted team update. Local-only; the team update is published separately.

## Top priorities this week
| Priority | KR it moves | Status |
|---|---|---|
| TBD | TBD | TBD |

## What happened
### Meetings
- TBD
### Messages and email
- TBD
### Documents and tickets
- TBD

## Action items
Routed to [[My Board]] (mine) or the team board (team commitments):
- [ ] TBD

## KR check-ins
| KR | Value | Confidence | Note |
|---|---|---|---|

## Wins and learnings
- TBD

## Blockers and risks
- TBD

## Team update (draft, not shared until published)
- Highlights: TBD
- KR progress: TBD
- Next week: TBD
- Help needed: TBD

## Private
Reflections that stay here.
