#!/usr/bin/env python3
"""Bundle canonical guidance with each skill and check installed copies."""

import argparse
import hashlib
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"


def bundled_references():
    sources = {
        path.name: path for path in sorted((ROOT / "references").glob("*.md"))
    }
    sources["pull-request-template.md"] = ROOT / ".github/pull_request_template.md"
    result = {}
    for name, source in sources.items():
        text = source.read_text(encoding="utf-8")
        if name == "pull-request.md":
            text = text.replace(
                "../.github/pull_request_template.md", "pull-request-template.md"
            )
        header = (
            f"<!-- Generated from {source.relative_to(ROOT).as_posix()}; "
            "edit the source and run scripts/sync-references.py. -->\n\n"
        )
        result[name] = (header + text).encode("utf-8")
    return result


def reference_links_are_local(references):
    errors = []
    for name, content in references.items():
        prose = re.sub(r"```.*?```", "", content.decode("utf-8"), flags=re.S)
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", prose):
            path = target.split("#", 1)[0]
            if not path or ":" in path:
                continue
            if path not in references:
                errors.append(f"{name}: reference leaves the bundle: {target}")
    return errors


def expected_files(skill, references):
    files = {"SKILL.md": (skill / "SKILL.md").read_bytes()}
    for path in sorted(skill.rglob("*")):
        if path.is_file() and "references" not in path.relative_to(skill).parts:
            files[path.relative_to(skill).as_posix()] = path.read_bytes()
    files.update({f"references/{name}": data for name, data in references.items()})
    return files


def fingerprint(files):
    digest = hashlib.sha256()
    for name, content in sorted(files.items()):
        digest.update(name.encode("utf-8") + b"\0" + content + b"\0")
    return digest.hexdigest()[:12]


def compare(directory, files):
    differences = []
    for name, content in files.items():
        path = directory / name
        if not path.is_file():
            differences.append(f"missing {name}")
        elif path.read_bytes() != content:
            differences.append(f"changed {name}")
    for path in (directory / "references").glob("*.md"):
        name = path.relative_to(directory).as_posix()
        if name not in files and path.read_bytes().startswith(b"<!-- Generated from "):
            differences.append(f"obsolete {name}")
    return differences


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="Check generated references.")
    mode.add_argument(
        "--installed", type=Path, metavar="SKILLS_DIRECTORY",
        help="Compare installed skills with this source without modifying them.",
    )
    args = parser.parse_args()
    references = bundled_references()
    errors = reference_links_are_local(references)
    if errors:
        print("\n".join(errors))
        return 1

    failed = False
    found_installed = False
    for skill in sorted(SKILLS.iterdir()):
        if not (skill / "SKILL.md").is_file():
            continue
        files = expected_files(skill, references)
        if args.installed:
            destination = args.installed.expanduser() / skill.name
            if not destination.exists():
                print(f"{skill.name}: NOT INSTALLED")
                continue
            found_installed = True
            differences = compare(destination, files)
        elif args.check:
            destination = skill
            differences = compare(destination, {
                name: content for name, content in files.items()
                if name.startswith("references/")
            })
        else:
            for path in (skill / "references").glob("*.md"):
                if path.name not in references and path.read_bytes().startswith(b"<!-- Generated from "):
                    path.unlink()
            for name, content in references.items():
                destination = skill / "references" / name
                destination.parent.mkdir(parents=True, exist_ok=True)
                if not destination.is_file() or destination.read_bytes() != content:
                    destination.write_bytes(content)
            differences = []

        status = "STALE" if differences else "CURRENT"
        print(f"{skill.name}: {status} ({fingerprint(files)})")
        for difference in differences:
            print(f"  {difference}")
        failed |= bool(differences)
    if args.installed and not found_installed:
        print("No Equilio skills found in the supplied directory.")
        return 1
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
