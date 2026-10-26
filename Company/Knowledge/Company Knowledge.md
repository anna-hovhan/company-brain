---
date: {{TODAY}}
type: hub
tags: [hub, knowledge]
ai-first: true
layer: company
---

# Company Knowledge

## For future agent
This is the company knowledge hub: summaries of shared sources (strategy decks, research, policies) ingested into the brain, each linked to its original.

```dataview
TABLE source_type, source_path, ingested
FROM "Company/Knowledge"
WHERE type = "knowledge"
SORT ingested DESC
```

Part of [[Company|Your Company Name]].
