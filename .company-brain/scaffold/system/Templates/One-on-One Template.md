<%*
const f = tp.file.folder(true);
const layer = f.startsWith("Company") ? "company" : f.startsWith("Teams") ? "team" : "personal";
const team = f.startsWith("Teams/") ? f.split("/")[1] : "";
const person = await tp.system.prompt("person as [[Name]]");
const cadence = await tp.system.prompt("cadence", "weekly");
-%>
---
date: <% tp.date.now("YYYY-MM-DD") %>
type: one-on-one
tags: [one-on-one]
ai-first: true
layer: <% layer %>
team: <% team ? '"[[' + team + ']]"' : "" %>
person: "<% person %>"
cadence: <% cadence %>
---

# <% tp.file.title %>

## For future agent
This note is the running 1:1 log with <% person %>, newest session first. It is personal and local-only; candid content sits under Private. Action items for others were copied to boards only when shareable.

## Standing topics
- Priorities and KRs
- Blockers
- Growth and feedback

## <% tp.date.now("YYYY-MM-DD") %>
- <% tp.file.cursor() %>

### Action items
- [ ] TBD

## Private
Notes that must never leave this file.
