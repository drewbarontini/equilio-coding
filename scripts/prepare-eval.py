#!/usr/bin/env python3
"""Copy behavioral cases and skill instructions into an isolated temporary run."""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile


ROOT = Path(__file__).resolve().parents[1]


def fingerprints(directory):
    result = {}
    for skill in sorted(directory.iterdir()):
        if not (skill / "SKILL.md").is_file():
            continue
        digest = hashlib.sha256()
        for path in sorted(skill.rglob("*")):
            if path.is_file():
                name = path.relative_to(skill).as_posix()
                digest.update(name.encode() + b"\0" + path.read_bytes() + b"\0")
        result[skill.name] = digest.hexdigest()
    return result


def git(directory, *args):
    return subprocess.check_output(
        ["git", "-C", str(directory), *args], text=True, stderr=subprocess.PIPE
    ).strip()


def prepare(root, cases):
    # Reject invalid selections before allocating or copying anything.
    for case in cases:
        source = root / "evals/cases" / case
        if not (source / "request.md").is_file() or not (source / "workspace").is_dir():
            raise ValueError(f"Incomplete evaluation case: {case}")
    run = Path(tempfile.mkdtemp(prefix="equilio-behavior-"))
    shutil.copytree(root / "skills", run / "skills")
    baseline_heads = {}
    for case in cases:
        source = root / "evals/cases" / case
        workspace = run / case
        shutil.copytree(source / "workspace", workspace)
        shutil.copy2(source / "request.md", workspace / "request.md")
        if any(workspace.glob("*.py")):
            git(workspace, "init", "--quiet", "--template=")
            git(workspace, "add", ".")
            git(workspace, "-c", "user.name=Equilio Eval", "-c",
                "user.email=eval@example.test", "-c", "core.hooksPath=/dev/null",
                "-c", "commit.gpgsign=false", "commit", "--quiet", "-m", "Fixture baseline")
            baseline_heads[case] = git(workspace, "rev-parse", "HEAD")
    manifest = {
        "source_commit": git(root, "rev-parse", "HEAD"),
        "source_dirty": bool(git(root, "status", "--porcelain")),
        "skill_fingerprints": fingerprints(run / "skills"),
        "cases": cases,
        "baseline_heads": baseline_heads,
    }
    (run / "run.json").write_text(json.dumps(manifest, indent=2) + "\n")
    return run


def main():
    available = sorted(path.name for path in (ROOT / "evals/cases").iterdir() if path.is_dir())
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", action="append", choices=available,
                        help="Prepare only this case; repeat to select several. Defaults to all.")
    args = parser.parse_args()
    print(prepare(ROOT, list(dict.fromkeys(args.case or available))))


if __name__ == "__main__":
    main()
