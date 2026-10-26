---
date: {{TODAY}}
type: hub
tags: [hub, projects]
ai-first: true
layer: company
---

# Company Projects

## For future agent
This is the company projects hub: company-wide initiatives with their owners, status, OKR links, and roadmap position.

```dataview
TABLE owner, status, roadmap, okrs, due
FROM "Company/Projects"
WHERE type = "project"
SORT status ASC, due ASC
```

Part of [[Company|{{COMPANY}}]].
