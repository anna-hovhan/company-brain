---
date: {{TODAY}}
type: hub
tags: [hub, okrs]
ai-first: true
layer: team
team: "[[{{TEAM}}]]"
---

# {{TEAM}} OKRs

## For future agent
This is the {{TEAM}} OKR hub: the team's quarterly objectives and key results. Each team objective names the company key result it ladders up to in `parent:`.

```dataview
TABLE period, owner, status, parent, last_checkin
FROM "Teams/{{TEAM}}/OKRs"
WHERE type = "objective"
SORT period DESC, file.name ASC
```

Company context: [[Company OKRs]], cascade in the latest OKR Tree listed in [[Company OKRs]]. Method: [[OKRs]]. Part of [[{{TEAM}}]].
