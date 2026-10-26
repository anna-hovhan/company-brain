#!/usr/bin/env python3
"""SessionStart hook: tell the session where the Company Brain and its engine live.

Inside the brain (cwd under a folder holding brain.yaml) it injects the full
summary: identity, current period, the CLI invocation, and the layer rules.
Elsewhere it injects two lines pointing at the configured brain, so the skills
still know where to write without flooding unrelated sessions.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ENGINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE / "scripts"))

try:
    import brain  # noqa: E402
except Exception as exc:  # never break session start
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart",
                                             "additionalContext": f"Company Brain engine failed to load: {exc}"}}))
    sys.exit(0)


def inside(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def main() -> None:
    cwd = Path(os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd())
    local = None
    for cand in (cwd.resolve(), *cwd.resolve().parents):
        if (cand / "brain.yaml").is_file():
            local = cand
            break
    configured = brain.find_root(os.environ.get("CLAUDE_PLUGIN_OPTION_VAULT_PATH") or None)
    if local:
        text = brain.session_summary(local)
    elif configured:
        text = (f"**Company Brain** is configured at `{configured}` (engine `{ENGINE}`). "
                f"Company Brain skills read and write there; run its CLI as "
                f"`python3 \"{ENGINE}/scripts/brain.py\" --root \"{configured}\" <command>` and read "
                f"`{configured}/CLAUDE.md` before writing.")
    else:
        text = (f"Company Brain plugin is installed (engine `{ENGINE}`) but no brain was found: "
                "open Claude in the brain folder or set the plugin's vault path in /plugin.")
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": text}}))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart",
                                                 "additionalContext": f"Company Brain context unavailable: {exc}"}}))
