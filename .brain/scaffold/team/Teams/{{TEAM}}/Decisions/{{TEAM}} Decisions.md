---
date: {{TODAY}}
type: hub
tags: [hub, decisions]
ai-first: true
layer: team
team: "[[{{TEAM}}]]"
---

# {{TEAM}} Decisions

## For future agent
This is the {{TEAM}} decision log: decisions scoped to the team.

```dataview
TABLE status, decided_by, context
FROM "Teams/{{TEAM}}/Decisions"
WHERE type = "decision"
SORT date DESC
```

Part of [[{{TEAM}}]].
