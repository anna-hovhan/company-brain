---
date: {{TODAY}}
type: hub
tags: [hub, meetings]
ai-first: true
layer: company
---

# Company Meetings

## For future agent
This is the company meetings hub: all-hands, leadership, and other company-wide meetings, newest first.

```dataview
TABLE meeting_type, attendees
FROM "Company/Meetings"
WHERE type = "meeting"
SORT date DESC
LIMIT 30
```

Part of [[Company|{{COMPANY}}]].
