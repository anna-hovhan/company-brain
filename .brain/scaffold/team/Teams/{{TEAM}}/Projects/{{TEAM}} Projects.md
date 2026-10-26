---
date: {{TODAY}}
type: hub
tags: [hub, projects]
ai-first: true
layer: team
team: "[[{{TEAM}}]]"
---

# {{TEAM}} Projects

## For future agent
This is the {{TEAM}} projects hub: the team's projects with owner, status, roadmap position, and the key results they serve.

```dataview
TABLE owner, status, roadmap, okrs, due
FROM "Teams/{{TEAM}}/Projects"
WHERE type = "project"
SORT status ASC, due ASC
```

Part of [[{{TEAM}}]].
