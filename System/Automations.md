---
date: {{TODAY}}
type: system
tags: [system]
ai-first: true
layer: company
---

# Automations

## For future agent
This note lists what Company Brain does automatically (hooks), what can be scheduled (daily, weekly, monthly, quarterly runs), and how to schedule them locally, since the brain lives on your machine and cloud schedulers cannot reach it.

## Always on (plugin hooks)
| Hook | When | What |
|---|---|---|
| `session_context.py` | every session start | tells Claude where the brain and engine are, who you are, the current quarter and week, and the layer rules |
| `validate-ai-first.sh` | after every write | warns when a note lacks AI-first frontmatter or the preamble, has banned characters, invalid tags, or secrets (vendored from obsidian-second-brain) |
| `layer_guard.py` | after every write | warns when a shared note links to a personal note, contains a Private section, or declares the wrong layer |

## Scaffold watcher (macOS, opt-in)
`./brain scaffold-sync --watch` installs a launchd agent for this brain, so edits to System/, Templates/, CLAUDE.md, Home.md, and vault settings flow into `.brain/scaffold/system` without running a command, whichever app made them (Obsidian, Cursor, Claude). It syncs on file changes and every 5 minutes (`--interval <seconds>` to change). It only writes the scaffold, never your notes. The log is in `~/Library/Logs/company-brain/`. Stop it with `./brain scaffold-sync --unwatch`; after moving the brain folder, run `--watch` again from the new place (the old agent is removed). macOS blocks background access to Desktop, Documents, and Downloads, so keep the brain elsewhere (for example `~/Brains/`) or give `python3` Full Disk Access; `--watch` warns when it is blocked.

## Suggested schedule
| Cadence | Prompt to schedule | Notes |
|---|---|---|
| Weekdays 08:30 | "Run the company-brain daily skill." | daily note before your first meeting |
| Fridays 15:00 | "Run the company-brain weekly skill. Do not publish the team update; leave it as a draft." | you review and publish |
| Mondays 09:00 (leads) | "Run the company-brain team-weekly skill for <Team> for last week." | roll-up before the team sync |
| Monthly, 1st | "Run the company-brain health skill and fix only errors; report the rest." | keeps the brain clean |
| Quarterly, last week | "Start the company-brain plan quarterly skill; draft only." | planning prep |

Unattended runs draft; they never publish team updates, promote notes, push to git, or send messages.

## How to schedule
- **Cowork (Claude desktop app), recommended**: open a Cowork session on the brain folder and create a scheduled task with the prompt above. It runs on your computer, so it can read and write the vault.
- **Claude Code headless with launchd**: `claude -p "<prompt>" --permission-mode acceptEdits` run from the brain folder. launchd strips the environment, so set an explicit `PATH` that includes `claude`, `python3`, and `uv`. Template: `.brain/automations/com.company-brain.weekly.plist.template`.
- **Cloud schedulers** (remote routines) run on a server and cannot see your local vault; use them only if the brain is in a git remote and you accept that the run happens on a copy.
