<%*
const f = tp.file.folder(true);
const layer = f.startsWith("Company") ? "company" : f.startsWith("Teams") ? "team" : "personal";
const team = f.startsWith("Teams/") ? f.split("/")[1] : "";
const author = await tp.system.prompt("author as [[Full Name]]");
-%>
---
date: <% tp.date.now("YYYY-MM-DD") %>
type: team-update
tags: [team-update, weekly]
ai-first: true
layer: <% layer %>
team: <% team ? '"[[' + team + ']]"' : "" %>
week: <% tp.date.now("GGGG-[W]WW") %>
author: "<% author %>"
krs: []
---

# <% tp.file.title %>

## For future agent
This note is <% author %>'s team update for <% tp.date.now("GGGG-[W]WW") %>: highlights, key result progress, next week's plan, and help needed. It is shared with the team and was published from the author's personal weekly note.

## Highlights
- TBD

## KR progress
| KR | Value | Confidence | Note |
|---|---|---|---|

## Next week
- TBD

## Help needed
- TBD
