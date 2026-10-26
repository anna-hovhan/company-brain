"""Guards around the vendored freshness lint and the hooks that apply it.

Company Brain vendors files from obsidian-second-brain (see .company-brain/upstream.json).
These tests make sure the freshness lint stays vendored unchanged, that it is wired into the
CLI and the hooks, that the brain itself obeys the policy, and that the guards really fire.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ENGINE = Path(__file__).resolve().parents[1]
BRAIN = ENGINE.parent
sys.path.insert(0, str(ENGINE / "scripts"))

import brain  # noqa: E402

# These must stay byte-for-byte copies of upstream. Downgrading one to "adapt" in
# upstream.json is a deliberate fork and has to change this list in the same review.
MUST_STAY_COPY = {
    ".company-brain/scripts/freshness_lint.py",
    ".company-brain/scripts/vault_scan.py",
    ".company-brain/references/freshness-policy.md",
    ".company-brain/tests/test_freshness_lint.py",
}


def conf() -> dict:
    return json.loads((ENGINE / "upstream.json").read_text(encoding="utf-8"))


def run_cli(root: Path, *args: str):
    # run the engine that ships inside the brain being tested, as ./brain does
    engine = root / ".company-brain" / "scripts" / "brain.py"
    return subprocess.run([sys.executable, str(engine), "--root", str(root), *args], capture_output=True, text=True)


def run_hook(name: str, file_path: Path, env_extra: dict | None = None) -> str:
    env = {k: v for k, v in os.environ.items() if k != "COMPANY_BRAIN_ALLOW_VENDORED_EDIT"}
    env.update(env_extra or {})
    event = json.dumps({"tool_input": {"file_path": str(file_path)}})
    r = subprocess.run([sys.executable, str(ENGINE / "hooks" / name)], input=event,
                       capture_output=True, text=True, env=env)
    assert r.returncode == 0, r.stderr
    return r.stdout.strip()


@pytest.fixture()
def brain_copy(tmp_path):
    dst = tmp_path / "brain"
    shutil.copytree(BRAIN, dst, ignore=shutil.ignore_patterns(".git", "__pycache__", "*.png", ".pytest_cache"))
    return dst


def note(path: Path, body: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("---\ndate: 2026-10-26\ntype: knowledge\ntags: [knowledge]\nai-first: true\nlayer: company\n---\n"
                    f"# {path.stem}\n\n## For future agent\nTest note.\n\n{body}\n", encoding="utf-8")
    return path


# --- vendored files stay vendored ------------------------------------------------------------

def test_vendored_copies_match_recorded_checksums():
    assert brain.vendored_integrity(BRAIN) == []


def test_freshness_files_are_marked_copy_with_checksums():
    copies = {f["local"]: f for f in conf()["files"] if f["mode"] == "copy"}
    assert MUST_STAY_COPY <= set(copies), "a freshness file was downgraded from copy to adapt"
    assert all(copies[p].get("sha256") for p in MUST_STAY_COPY)


def test_every_registered_file_exists():
    assert [f["local"] for f in conf()["files"] if not (BRAIN / f["local"]).exists()] == []


def test_integrity_check_catches_an_edit(tmp_path, monkeypatch):
    vendored = tmp_path / "vendored.py"
    vendored.write_text("print('upstream')\n", encoding="utf-8")
    cfg = tmp_path / "upstream.json"
    cfg.write_text(json.dumps({"files": [{"upstream": "x.py", "local": "vendored.py", "mode": "copy",
                                          "sha256": brain.sha256_file(vendored)}]}), encoding="utf-8")
    monkeypatch.setattr(brain, "UPSTREAM_CONF", cfg)
    assert brain.vendored_integrity(tmp_path) == []
    vendored.write_text("print('edited')\n", encoding="utf-8")
    problems = brain.vendored_integrity(tmp_path)
    assert len(problems) == 1 and "differs from the upstream copy" in problems[0]


def test_verify_flag_fails_when_a_copy_is_edited(brain_copy):
    assert run_cli(brain_copy, "upstream-check", "--verify").returncode == 0
    lint = brain_copy / ".company-brain" / "scripts" / "freshness_lint.py"
    lint.write_text(lint.read_text(encoding="utf-8") + "\n# local edit\n", encoding="utf-8")
    r = run_cli(brain_copy, "upstream-check", "--verify")
    assert r.returncode == 1 and "freshness_lint.py" in r.stdout


# --- the brain obeys its own policy ----------------------------------------------------------

def test_the_brain_is_freshness_clean():
    report = brain.freshness_report(BRAIN)
    assert report["errors"] == 0 and report["warnings"] == 0, report["findings"]


def test_new_brains_inherit_the_freshness_config():
    assert ".freshness.json" in brain.scaffold_system_sources(BRAIN)


# --- CLI wiring ------------------------------------------------------------------------------

def test_freshness_command_fails_on_an_undated_fast_fact(brain_copy):
    note(brain_copy / "Company" / "Knowledge" / "Pipeline.md", "The pipeline has 13 open deals.")
    r = run_cli(brain_copy, "freshness")
    assert r.returncode == 1 and "FRESH-1" in r.stdout and "Pipeline.md" in r.stdout


def test_freshness_command_passes_when_the_fact_is_stamped(brain_copy):
    stamp = dt.date.today().isoformat()
    note(brain_copy / "Company" / "Knowledge" / "Pipeline.md", f"The pipeline has 13 open deals (as of {stamp}).")
    assert run_cli(brain_copy, "freshness").returncode == 0


def test_check_reports_freshness_as_a_warning_not_an_error(brain_copy):
    note(brain_copy / "Company" / "Knowledge" / "Pipeline.md", "The pipeline has 13 open deals.")
    r = run_cli(brain_copy, "--json", "check")
    issues = json.loads(r.stdout)
    hits = [i for i in issues if "FRESH-1" in i["message"]]
    assert hits and hits[0]["severity"] == "warn" and r.returncode == 0


def test_engine_folder_is_exempt_from_the_lint(brain_copy):
    note(brain_copy / ".company-brain" / "references" / "example.md", "The pipeline has 13 open deals.")
    assert run_cli(brain_copy, "freshness").returncode == 0


# --- hooks -----------------------------------------------------------------------------------

def test_hooks_json_wires_both_guards():
    hooks = json.loads((ENGINE / "hooks" / "hooks.json").read_text(encoding="utf-8"))["hooks"]

    def commands(event):
        return [h["command"] for g in hooks[event] if "Write" in g["matcher"] for h in g["hooks"]]

    assert any("vendored_guard.py" in c for c in commands("PreToolUse"))
    assert any("freshness_guard.py" in c for c in commands("PostToolUse"))
    for script in ("vendored_guard.py", "freshness_guard.py"):
        assert (ENGINE / "hooks" / script).is_file()


def test_vendored_guard_denies_edits_to_a_copy_file():
    out = run_hook("vendored_guard.py", ENGINE / "scripts" / "freshness_lint.py")
    decision = json.loads(out)["hookSpecificOutput"]
    assert decision["permissionDecision"] == "deny" and "upstream-check --copy" in decision["permissionDecisionReason"]


def test_vendored_guard_allows_our_own_and_adapted_files():
    assert run_hook("vendored_guard.py", ENGINE / "scripts" / "brain.py") == ""
    assert run_hook("vendored_guard.py", ENGINE / "hooks" / "validate-ai-first.sh") == ""
    assert run_hook("vendored_guard.py", BRAIN / "README.md") == ""


def test_vendored_guard_can_be_overridden_on_purpose():
    out = run_hook("vendored_guard.py", ENGINE / "scripts" / "freshness_lint.py",
                   env_extra={"COMPANY_BRAIN_ALLOW_VENDORED_EDIT": "1"})
    assert out == ""


def test_freshness_guard_warns_on_a_bad_note_and_stays_quiet_on_a_good_one(brain_copy):
    bad = note(brain_copy / "Company" / "Knowledge" / "Bad.md", "The pipeline has 13 open deals.")
    out = json.loads(run_hook("freshness_guard.py", bad))
    assert "FRESH-1" in out["hookSpecificOutput"]["additionalContext"]
    stamp = dt.date.today().isoformat()
    good = note(brain_copy / "Company" / "Knowledge" / "Good.md", f"13 open deals (as of {stamp}).")
    assert run_hook("freshness_guard.py", good) == ""
