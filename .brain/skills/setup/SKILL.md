---
name: setup
description: Set up or update the Company Brain - company name, your identity (Me.md), teams, manager, timezone, fiscal year, sharing model (git, Google Drive, local), sources, and Obsidian. Use for "set up company brain", "onboard me to the brain", "add me to the brain", first run, or when a skill says Me.md is missing.
---

# Setup

Bootstrap a brain for its first user, or onboard a new teammate who just cloned it. Idempotent: running it again only fills gaps.

## Before you start
1. **Find the brain.** The session context has a **Company Brain** line with the brain path and the engine path. If it is missing, run `python3 "${CLAUDE_SKILL_DIR}/../../scripts/brain.py" root`. No brain found: stop and tell the user to open Claude in the brain folder or set the plugin's vault path.
2. **`brain`** below means `python3 "<engine>/scripts/brain.py" --root "<brain>"` (or `./brain` from the brain root).
3. **Read the rules** in `<brain>/CLAUDE.md` unless they are already loaded, and `Personal/Me.md` for who "me" and "my team" are. No `Me.md`: run the `setup` skill first.
4. **Write only with file tools or the `brain` CLI.** Never use the obsidian-second-brain MCP tools here; they point at a different vault.

## Steps
1. **Read the current state**: `brain whoami` and `brain check --severity warn`. Note what already exists (company name, teams, `me_file_exists`).
2. **Interview, one short question at a time** (skip anything already known; offer the obvious default):
   - Company name (default: the `company.name` in `brain.yaml`).
   - Your full name, role, home team, other teams, manager. Teammates joining an existing brain pick their team from `all_teams`.
   - Timezone (default: the system timezone, else `UTC`) and the fiscal-year start month (default 1).
   - Sharing model: `git` (private repo, review for company changes), `drive` (Google Shared Drive folders), or `local` (try it alone first). Explain in one line each; recommend `git` for teams that can use it.
   - Teams to create now (name and lead). Do not invent teams.
3. **Write**: `brain init --company "<C>" --me "<Full Name>" --role "<Role>" --team "<Home team>" [--team ...] --manager "<Manager>" --timezone <TZ> --fiscal-year-start <M> --sharing <model>`, then `brain team add "<Team>" --lead "<Lead>"` for each extra team. Show the created files grouped by layer.
4. **Purpose (optional, offer)**: if `Company/Mission.md` is still TBD, offer to draft mission, vision, and values with the `strategy` skill now or later.
5. **Sources (optional, offer)**: offer to mount Desktop or Google Drive folders with the `connect` skill (`brain sources` lists detected Drive accounts).
6. **Obsidian**: tell the user to open the brain folder as a vault. If `.obsidian/plugins/` lacks dataview, obsidian-kanban, templater-obsidian, or calendar, explain: Settings, Community plugins, turn off Restricted mode, install and enable those four. Graph colours by layer are preconfigured.
7. **Sharing**:
   - `git`: if `git remote -v` is empty, show (do not run) `git remote add origin <private repo URL>` and the first commit commands. Confirm `Personal/` is in `.gitignore` before any commit.
   - `drive`: explain mounting `Company/` and each `Teams/<Team>/` from a Shared Drive (`System/Layers and privacy.md`); keep `Personal/` local.
   - Teammates onboarding: they clone the repo, run this skill, then `brain connect --sync` for shared sources.
8. **Plugin everywhere (optional)**: to use the brain from any folder or Cowork, set the plugin's `vault_path` to the brain folder (`/plugin`, Company Brain, configure).
9. `brain refresh`, then summarize: who you are in the brain, teams, what to run next (`daily`, `weekly`, `okr`).

## Always
- Layers: Company/ and Teams/ are shared; Personal/ is local only. Never link from a shared note to a Personal note, and never copy content under `## Private` out of Personal/ (`references/layers.md`).
- AI-first notes: frontmatter with `date`, `type`, `tags`, `ai-first: true`, `layer`; a `## For future agent` preamble; `[[wikilinks]]` for every person, team, objective, and project (`references/ai-first-rules.md`, `references/schemas.md`).
- Search before create (`brain new` refuses duplicates and prints the existing path). Never invent facts, numbers, dates, or people: write `TBD` and ask.
- Finish with `brain refresh` when OKRs, discovery, scores, or people changed, otherwise `brain index`. With `sharing: git`, list the shared files changed and suggest a commit; never push or open a pull request yourself.
