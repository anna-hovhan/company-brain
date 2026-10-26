---
date: {{TODAY}}
type: hub
tags: [hub, planning]
ai-first: true
layer: company
---

# Company Planning

## For future agent
This is the company planning hub: annual and quarterly plans and the operating cadence that connects strategy to weekly execution.

## Plans
```dataview
TABLE horizon, period, status
FROM "Company/Planning"
WHERE type = "plan"
SORT period DESC
```

## Operating cadence
| Rhythm | What happens | Skill | Output |
|---|---|---|---|
| Annual | revisit mission, vision, strategy; set annual objectives | `/company-brain:plan annual` | Annual Plan, annual objectives |
| Quarterly | score last quarter, set company then team OKRs, refresh discovery and roadmap | `/company-brain:plan quarterly` | Quarterly Plan, quarterly objectives |
| Weekly | personal weekly note, team updates, team roll-up, KR check-ins | `/company-brain:weekly`, `/company-brain:team-weekly` | weekly notes, check-ins |
| Daily | daily note with calendar, focus, and KR links | `/company-brain:daily` | daily note |

The planning chain: [[Mission]] and [[Vision]] to [[Company Strategy]] to annual objectives to quarterly objectives to team objectives to projects and solutions to weekly work.
