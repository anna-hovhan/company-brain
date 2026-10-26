---
date: {{TODAY}}
type: hub
tags: [hub, home]
ai-first: true
layer: company
---

# Company Brain

## For future agent
This is the front door of the Company Brain vault: live dashboards for this week, the current quarter's objectives, the roadmap, recent decisions and meetings, and links into every area. Dataview tables render each reader's own data, so the personal sections show only the reader's notes.

## Start here
- [[Company]] (mission, strategy, OKRs, discovery, roadmap, organization) | [[Teams]] | [[Personal]] (yours only)
- How it works: [[How Company Brain works]] | [[Layers and privacy]] | [[Skills]] | [[Frameworks]] | [[Setup]]

## This week (personal)
```dataview
TABLE WITHOUT ID file.link AS "Note", krs AS "Key results"
FROM "Personal/Weekly" OR "Personal/Daily"
WHERE week = dateformat(date(today), "kkkk-'W'WW")
SORT file.name DESC
```

## Objectives this quarter
```dataview
TABLE level, owner, status, last_checkin
FROM "Company/OKRs" OR "Teams"
WHERE type = "objective" AND period = dateformat(date(today), "yyyy-'Q'q")
SORT level ASC, file.name ASC
```

## Roadmap: now
![[Company Roadmap#Now]]

## Recent decisions
```dataview
TABLE layer, status, decided_by
FROM "Company" OR "Teams"
WHERE type = "decision"
SORT date DESC
LIMIT 8
```

## Recent meetings
```dataview
TABLE meeting_type, layer
FROM "Company" OR "Teams" OR "Personal"
WHERE type = "meeting" OR type = "one-on-one"
SORT date DESC
LIMIT 8
```

## Ask Claude
`/company-brain:daily` | `/company-brain:weekly` | `/company-brain:okr checkin` | `/company-brain:meeting` | `/company-brain:ost` | `/company-brain:prioritize` | `/company-brain:health`
