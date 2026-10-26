# Layers and multiplayer rules

The canonical spec for how Company Brain separates personal, team, and company knowledge. Every skill that writes to the brain resolves the target layer with this document before writing. The human-readable version for the vault is `System/Layers and privacy.md`; if the two ever disagree, this file wins.

## The three layers

| Layer | Folder | Shared with | Committed to git | Typical content |
|---|---|---|---|---|
| company | `Company/` | everyone in the company | yes | mission, vision, values, strategy, company OKRs, plans, discovery, roadmap, org chart, people profiles, company projects, all-hands and leadership meetings, company decisions |
| team | `Teams/<Team>/` | everyone (owned and edited by the team) | yes | team charter, team OKRs, team projects, team meetings, team weekly updates and roll-ups, team discovery, team board and roadmap |
| personal | `Personal/` | nobody (local only) | no, gitignored | identity (`Me.md`), daily notes, personal weekly notes, 1:1s, private goals, personal board, inbox, drafts |

Two more folders sit beside the layers and are not layers:

- `Sources/` holds symlinks to external folders (Desktop, Google Drive). Read-only by rule, gitignored, machine-local. See `references/sources.md`.
- `System/` and `Templates/` hold the framework library, docs, and templates. Shared, committed, rarely edited.

The layer is recorded twice, on purpose: by the folder the note lives in (what git and Drive sharing act on) and by `layer:` in frontmatter (what agents and Dataview read). They must agree. `brain check` reports any note whose `layer:` does not match its folder.

## Identity

A brain has many users; each user's clone has exactly one `Personal/Me.md`. It is the identity record every skill reads first:

```yaml
---
type: me
person: "[[Jane Doe]]"        # links to the shared profile Company/Org/People/Jane Doe.md
teams: ["[[Platform]]"]       # team hubs this person belongs to
role: "Engineering Manager"
manager: "[[Sam Lee]]"
timezone: UTC
---
```

"Me" in any skill means the person in `Me.md`. "My team" means the first entry of `teams:` unless the user names another. If `Me.md` is missing, run `/company-brain:setup` (or `brain init`) before writing anything.

## Direction of links (the leak rule)

Links may point **up** the stack, never **down**:

```
Personal  ──links to──▶  Team  ──links to──▶  Company
    ▲                        ✕                    ✕
    └──── no shared note may link to a Personal note
```

- A personal note may link to anything.
- A team or company note may link to team and company notes only. A wikilink or embed from `Company/` or `Teams/` to a note in `Personal/` is a leak: for everyone else it is a dangling link, and its title alone can reveal private content (a 1:1 title, a draft decision).
- Dataview queries in shared notes may read `Personal/` (each person's query runs over their own local data). The leak rule applies to static links, not to code blocks.
- A team note may link to another team's notes. Teams are visible to the whole company; there is no team-private layer by default. A team that needs privacy uses a separate brain or a restricted Drive folder mounted as its team folder (see Sharing transports).

Enforced by: the `layer_guard` hook on every write, and `brain check` across the whole vault.

## Private sections

Inside a personal note, everything under a `## Private` heading (to the next heading of the same or higher level) is never copied into a shared note by any skill, including `/company-brain:promote`. Use it for candid notes in 1:1s, feedback drafts, and personal reflections.

## Promotion (personal to team to company)

Moving knowledge up the stack is always a deliberate, user-approved step:

1. The user asks to share, publish, or promote a note, or a skill's final step proposes it (the weekly skill proposes a team update).
2. The `promote` skill builds the shared version: drops `## Private` sections, rewrites links to `Personal/` notes as plain text, sets `layer:` and `team:`, and removes personal-only frontmatter (`energy`, `mood`).
3. The user sees the diff and confirms.
4. The shared note is written in the target layer. The personal note gets `promoted_to: "[[Shared note]]"` (an upward link, allowed). The shared note never records the personal note's path.

Nothing is ever promoted automatically by a hook, scheduled job, or background agent.

## Conflict-free multiplayer writes

When several people write to the same shared area, structure the files so that git never has to merge two people's edits to one file:

- **Weekly updates**: each person writes their own file `Teams/<Team>/Weekly/<YYYY>-W<WW> - <Team> - <Person>.md`. The team roll-up `... - <Team> - Team Weekly.md` is written by one person (the lead or whoever runs `/company-brain:team-weekly`).
- **KR check-ins**: the KR owner edits only their own KR line in the objective note, and appends one row to its `## Check-ins` table. Line-level changes by different owners merge cleanly.
- **Meetings**: one note per meeting, written by the note-taker. Other attendees add to it through a follow-up edit, not a second note.
- **Boards**: one board per team. Personal action items go on `Personal/My Board.md`, not on the team board, unless they are team commitments.
- **Generated views** (`OKR Tree`, `Prioritization`, `Org Chart`, discovery canvases) are rebuilt by `brain refresh` inside `<!-- brain:auto:... -->` markers. They can be regenerated by anyone at any time, so a merge conflict there is resolved by re-running `brain refresh`, never by hand.

## Sharing transports

| Model | How the shared layers travel | Personal layer | When to use |
|---|---|---|---|
| `git` (default) | The vault is a private git repo. `Company/`, `Teams/`, `System/`, `Templates/`, `.company-brain/` are committed. Changes to `Company/` go through pull requests | gitignored, never leaves the laptop | Teams comfortable with git, or using the Obsidian Git plugin |
| `drive` | `Company/` and each `Teams/<Team>/` are symlinks into Google Shared Drive folders (Drive for Desktop, mirror mode recommended) | a normal local folder | Non-technical teams. No review step, so keep company-layer edits to a few editors |
| `local` | Nothing is shared | local | Trying the system alone before inviting the team |

The model is recorded in `brain.yaml` under `sharing.model`. Skills read it to decide whether to suggest a commit or pull request after a shared-layer write (`git`) or just to save (`drive`, `local`). Skills never run `git push` and never open a pull request on their own: they show the user the command or ask first.

## What each skill writes where (summary)

| Activity | Layer by default | Override |
|---|---|---|
| Daily note, personal weekly, 1:1, private goal, inbox capture | personal | never shared directly; promote instead |
| Weekly team update | team (own file) | none |
| Team roll-up, team OKRs, team meeting, team project, team board | team | company when the user says it is company-wide |
| Mission, vision, values, strategy, VPC, BMC, company OKRs, annual and quarterly plans, roadmap, org chart, people profiles, all-hands, leadership meetings | company | team when the user scopes it to one team |
| Discovery (outcomes, opportunities, solutions, experiments) | the layer of the OKR the outcome serves | as stated by the user |
| Decision record | the layer of the thing decided | as stated |
| Ingested source summary | personal unless the source is shared and the user says so | as stated |

When the layer is genuinely unclear (for example a meeting with no attendee list), ask once. Default to personal when the user does not answer: a note in the wrong private place is easy to promote; a note in the wrong shared place has already leaked.
