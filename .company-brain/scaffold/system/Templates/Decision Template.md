<%*
const f = tp.file.folder(true);
const layer = f.startsWith("Company") ? "company" : f.startsWith("Teams") ? "team" : "personal";
const team = f.startsWith("Teams/") ? f.split("/")[1] : "";
const context = await tp.system.prompt("context: the meeting, project or OKR this came from, as [[Note]]", "");
-%>
---
date: <% tp.date.now("YYYY-MM-DD") %>
type: decision
tags: [decision]
ai-first: true
layer: <% layer %>
team: <% team ? '"[[' + team + ']]"' : "" %>
status: proposed
decided_by: ["[[TBD]]"]
context: "<% context %>"
supersedes: ""
---

# <% tp.file.title %>

## For future agent
This note is a decision record at the <% layer %> layer, from <% context %>. It states the decision, the options considered, the reasoning, and the consequences. Check `status:` and `superseded_by` before relying on it.

## Decision
TBD. One sentence, active voice: "We will..."

## Context
TBD

## Options considered
| Option | Pros | Cons |
|---|---|---|
| TBD | TBD | TBD |

## Reasoning
TBD

## Consequences
- What changes: TBD
- What we accept as a cost: TBD
- Review date (optional): TBD
