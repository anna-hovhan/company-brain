<%*
const f = tp.file.folder(true);
const layer = f.startsWith("Company") ? "company" : f.startsWith("Teams") ? "team" : "personal";
const team = f.startsWith("Teams/") ? f.split("/")[1] : "";
-%>
---
date: <% tp.date.now("YYYY-MM-DD") %>
type: bmc
tags: [bmc, strategy]
ai-first: true
layer: <% layer %>
team: <% team ? '"[[' + team + ']]"' : "" %>
status: draft
owner: "[[TBD]]"
---

# <% tp.file.title %>

## For future agent
This note is a Business Model Canvas (Osterwalder) at the <% layer %> layer: the nine building blocks of how this business creates, delivers, and captures value. Value propositions link to the per-segment canvases.

## Customer segments
- TBD

## Value propositions
One per segment; link each [[Value Proposition Canvas]] note: TBD

## Channels
- TBD

## Customer relationships
- TBD

## Revenue streams
- TBD

## Key resources
- TBD

## Key activities
- TBD

## Key partnerships
- TBD

## Cost structure
- TBD

## Riskiest assumptions
- TBD

Method: [[Business Model Canvas]].
