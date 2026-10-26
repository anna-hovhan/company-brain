---
date: {{TODAY}}
type: hub
tags: [hub, meetings]
ai-first: true
layer: team
team: "[[{{TEAM}}]]"
---

# {{TEAM}} Meetings

## For future agent
This is the {{TEAM}} meetings hub: team syncs, planning sessions, retros, and workshops, newest first.

```dataview
TABLE meeting_type, attendees
FROM "Teams/{{TEAM}}/Meetings"
WHERE type = "meeting"
SORT date DESC
LIMIT 30
```

Part of [[{{TEAM}}]].
