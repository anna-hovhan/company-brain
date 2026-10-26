---
date: {{TODAY}}
type: hub
tags: [hub, knowledge]
ai-first: true
layer: team
team: "[[{{TEAM}}]]"
---

# {{TEAM}} Knowledge

## For future agent
This is the {{TEAM}} knowledge hub: summaries of shared sources the team relies on, each linked to its original.

```dataview
TABLE source_type, source_path, ingested
FROM "Teams/{{TEAM}}/Knowledge"
WHERE type = "knowledge"
SORT ingested DESC
```

Part of [[{{TEAM}}]].
