---
date: {{TODAY}}
type: hub
tags: [hub, teams]
ai-first: true
layer: team
---

# Teams

## For future agent
This is the hub of team spaces. Each team folder under Teams/ holds its charter, OKRs, projects, meetings, weekly updates, discovery, decisions, board, and roadmap. Team spaces are visible to the whole company and owned by the team.

```dataview
TABLE lead, mission, parent
FROM "Teams"
WHERE type = "team"
SORT file.name ASC
```

Create a team with `/company-brain:org add team` or `brain team add "<Team>"`. Org-wide view: [[Organization]].
