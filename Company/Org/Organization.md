---
date: {{TODAY}}
type: hub
tags: [hub, org]
ai-first: true
layer: company
---

# Organization

## For future agent
This is the organization hub: the generated org chart, the list of teams, and every shared people profile. Profiles hold intranet-level facts only; private impressions live in each person's own Personal/1-1s notes.

- [[Org Chart]] (generated from `manager:` and `team:` on profiles)
- [[Teams]]

## People
```dataview
TABLE role, team, manager
FROM "Company/Org/People"
WHERE type = "person"
SORT team ASC, file.name ASC
```

## Profiles missing basics
```dataview
LIST FROM "Company/Org/People"
WHERE type = "person" AND (role = "TBD" OR !role OR !team OR team = "TBD")
```

Add or update people with `/company-brain:org`.
