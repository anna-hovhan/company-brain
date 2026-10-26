---
date: {{TODAY}}
type: hub
tags: [hub, decisions]
ai-first: true
layer: company
---

# Company Decisions

## For future agent
This is the company decision log: decisions that affect the whole company, with status and what each supersedes.

```dataview
TABLE status, decided_by, context, supersedes
FROM "Company/Decisions"
WHERE type = "decision"
SORT date DESC
```

Part of [[Company|{{COMPANY}}]].
