---
date: {{TODAY}}
type: team
tags: [team]
ai-first: true
layer: team
team: "[[{{TEAM}}]]"
lead: "[[{{TEAM_LEAD}}]]"
parent: "[[TBD]]"
mission: "TBD"
slack: "TBD"
rituals: []
---

# {{TEAM}}

## For future agent
This is the charter and hub of the {{TEAM}} team space: mission, members, the objectives the team owns, and links to its projects, meetings, weekly updates, discovery, decisions, board, and roadmap. Members come from people profiles whose `team:` is this note.

## Mission
TBD. What this team exists to achieve for the company, in one or two sentences. It should ladder up to [[Mission]].

## Members
```dataview
TABLE role, manager
FROM "Company/Org/People"
WHERE type = "person" AND contains(string(team), "{{TEAM}}")
SORT file.name ASC
```

## Objectives this quarter
```dataview
TABLE owner, status, parent, last_checkin
FROM "Teams/{{TEAM}}/OKRs"
WHERE type = "objective" AND period = dateformat(date(today), "yyyy-'Q'q")
```

## Team space
- [[{{TEAM}} OKRs]] | [[{{TEAM}} Projects]] | [[{{TEAM}} Meetings]] | [[{{TEAM}} Weekly]]
- [[{{TEAM}} Discovery]] | [[{{TEAM}} Prioritization]] | [[{{TEAM}} Roadmap]] | [[{{TEAM}} Board]]
- [[{{TEAM}} Decisions]] | [[{{TEAM}} Knowledge]]

## Ways of working
- Rituals: TBD (weekly sync, planning, retro)
- Weekly updates: each member runs `/company-brain:weekly` and publishes a team update; the lead runs `/company-brain:team-weekly`.
- Decisions that affect other teams are recorded in [[Company Decisions]].

Part of [[Teams]].
