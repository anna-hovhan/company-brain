# Running the brain's commands from a session started elsewhere

A session started inside the vault loads `CLAUDE.md`, the commands and the write guard on its own. A session started anywhere else (a skill named `company-brain:<command>`) has none of that and does the steps below by hand. Keep this file in step with `CLAUDE.md` and the hooks in `.claude/settings.json`: it is the one place that says what such a session does instead.

## Where to work

`$ROOT` is the vault the session found (`ROOT="$REPO"`). Work from there (`cd "$ROOT"`): the commands' paths are relative to it. Never clone a second copy: personal notes live only in the owner's copy.

## Load the rules

Read `$ROOT/CLAUDE.md` in full (the operating manual), then `$ROOT/index.md` as it says (`brain index` if it is missing), then `$ROOT/Personal/Me.md` for who "me" is (missing: the `setup` command).

## Do the write guard's work by hand

The guard (`.company-brain/hooks/vendored_guard.py`, a hook on every write) does not run in a session started elsewhere. Follow `CLAUDE.md`'s note rules by hand: the AI-first frontmatter and preamble, ASCII punctuation, layers, and links that point up, never down. After writing, run `brain check`, and `brain index` when `CLAUDE.md` says to.

## Always

- Promotion from personal to team or company, and anything leaving `Personal/`, only on the user's explicit yes, as `CLAUDE.md` says.
- Ask before any `git pull`, commit or push. `upstream-sync` maintains the vault's tooling: run it only when the user names it.
