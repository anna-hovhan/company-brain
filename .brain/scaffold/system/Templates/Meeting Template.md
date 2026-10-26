<%*
const f = tp.file.folder(true);
const layer = f.startsWith("Company") ? "company" : f.startsWith("Teams") ? "team" : "personal";
const team = f.startsWith("Teams/") ? f.split("/")[1] : "";
const meeting_type = await tp.system.prompt("meeting_type: all-hands, leadership, team, one-on-one, external or workshop", "team");
const attendees = await tp.system.prompt("attendees as [[Name]], [[Name]]", "");
-%>
---
date: <% tp.date.now("YYYY-MM-DD") %>
type: meeting
tags: [meeting]
ai-first: true
layer: <% layer %>
team: <% team ? '"[[' + team + ']]"' : "" %>
meeting_type: <% meeting_type %>
attendees: [<% attendees.split(",").filter(a => a.trim()).map(a => '"' + a.trim() + '"').join(", ") %>]
source: manual
project: ""
---

# <% tp.file.title %>

## For future agent
This note is a <% meeting_type %> meeting on <% tp.date.now("YYYY-MM-DD") %> at the <% layer %> layer. It captures the agenda, notes, decisions, and action items with owners and due dates; action items were routed to the owners' boards when the note was processed.

## Agenda
- <% tp.file.cursor() %>

## Notes
- TBD

## Decisions
- None.

## Action items
<!-- One line per action: - [ ] Owner-as-wikilink action @{YYYY-MM-DD} -->
