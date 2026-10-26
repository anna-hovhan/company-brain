<%*
const f = tp.file.folder(true);
const layer = f.startsWith("Company") ? "company" : f.startsWith("Teams") ? "team" : "personal";
const team = f.startsWith("Teams/") ? f.split("/")[1] : "";
const role = await tp.system.prompt("role");
const person_team = await tp.system.prompt("team as [[Team]]", "");
const manager = await tp.system.prompt("manager as [[Name]]", "");
-%>
---
date: <% tp.date.now("YYYY-MM-DD") %>
type: person
tags: [person]
ai-first: true
layer: <% layer %>
team: "<% person_team %>"
role: "<% role %>"
manager: "<% manager %>"
location: TBD
start_date: TBD
timeline:
  - fact: "<% role %>"
    from: TBD
    until: present
    learned: <% tp.date.now("YYYY-MM-DD") %>
---

# <% tp.file.title %>

## For future agent
This note is the shared profile of <% tp.file.title %> (<% role %>): intranet-level facts only, used by the org chart and team pages. Private impressions and 1:1 notes about this person live in each colleague's own Personal/1-1s, never here.

## Role and responsibilities
- TBD

## Works on
```dataview
LIST FROM "Company" OR "Teams"
WHERE (type = "project" AND contains(string(owner), this.file.name)) OR (type = "objective" AND contains(string(owner), this.file.name))
```

## Reports
```dataview
LIST FROM "Company/Org/People" WHERE contains(string(manager), this.file.name)
```
