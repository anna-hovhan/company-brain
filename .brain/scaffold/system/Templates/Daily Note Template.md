<%*
const f = tp.file.folder(true);
const layer = f.startsWith("Company") ? "company" : f.startsWith("Teams") ? "team" : "personal";
const team = f.startsWith("Teams/") ? f.split("/")[1] : "";
-%>
---
date: <% tp.date.now("YYYY-MM-DD") %>
type: daily
tags: [daily]
ai-first: true
layer: <% layer %>
team: <% team ? '"[[' + team + ']]"' : "" %>
week: <% tp.date.now("GGGG-[W]WW") %>
energy: 
---

# <% tp.file.title %>

## For future agent
This note is the personal daily note for <% tp.date.now("YYYY-MM-DD") %>: calendar, focus linked to key results, captures, and end-of-day notes. Local-only; promote anything shareable rather than linking to it.

## Focus
Top three, each linked to the KR it moves:
- [ ] TBD

## Calendar
- TBD

## Notes and captures
- <% tp.file.cursor() %>

## Done today
- TBD

## Tomorrow
- TBD
