#!/usr/bin/env python3
"""Legt die vier Kurs-Issues im aktuellen GitHub-Repo an (benötigt: gh auth login).

Aufruf (Kurs-VM Windows Server, **PowerShell**):
    .\\seed_issues.ps1         # empfohlen
    py -3 seed_issues.py       # Alternative

Linux / macOS / Git Bash:
    ./seed_issues.sh
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
ISSUES_DIR = REPO_ROOT / "docs" / "issues"

ISSUES: list[tuple[str, str, str]] = [
    (
        "ISSUE-01-types-filter.md",
        "Feature: Commit-Typen filtern (--types)",
        "feature",
    ),
    (
        "ISSUE-02-semver.md",
        "Feature: Versionsvorschlag nach SemVer (--suggest-version)",
        "feature",
    ),
    (
        "ISSUE-03-json-format.md",
        "Feature: JSON-Ausgabe (--format json)",
        "feature",
    ),
    (
        "ISSUE-04-contributors.md",
        "Feature: Mitwirkenden-Sektion (--contributors)",
        "feature",
    ),
]


def _run(cmd: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        text=True,
        capture_output=True,
        encoding="utf-8",
        check=check,
    )


def _require_gh() -> None:
    if not shutil.which("gh"):
        print(
            "FEHLER: GitHub CLI (gh) nicht gefunden.\n"
            "Installieren: https://cli.github.com/ — danach: gh auth login --web",
            file=sys.stderr,
        )
        sys.exit(1)
    status = _run(["gh", "auth", "status"], check=False)
    if status.returncode != 0:
        print(
            "FEHLER: gh ist nicht angemeldet.\n"
            "Bitte zuerst ausführen: gh auth login --web",
            file=sys.stderr,
        )
        if status.stderr.strip():
            print(status.stderr.strip(), file=sys.stderr)
        sys.exit(1)


def _existing_titles() -> set[str]:
    result = _run(
        ["gh", "issue", "list", "--state", "all", "--json", "title", "-L", "100"],
        check=False,
    )
    if result.returncode != 0:
        return set()
    try:
        items = json.loads(result.stdout or "[]")
    except json.JSONDecodeError:
        return set()
    return {str(item.get("title", "")) for item in items}


def _ensure_feature_label() -> None:
    _run(
        [
            "gh",
            "label",
            "create",
            "feature",
            "--color",
            "0e8a16",
            "--description",
            "Neues Feature",
        ],
        check=False,
    )


def _create_issue(body_file: Path, title: str, labels: str) -> None:
    if not body_file.is_file():
        print(f"FEHLER: Issue-Datei fehlt: {body_file}", file=sys.stderr)
        sys.exit(1)

    print(f"Erzeuge Issue: {title}")
    cmd = [
        "gh",
        "issue",
        "create",
        "--title",
        title,
        "--body-file",
        str(body_file),
        "--label",
        labels,
    ]
    result = _run(cmd, check=False)
    if result.returncode != 0:
        # Label fehlt im Repo — ohne Label erneut versuchen
        result = _run(
            [
                "gh",
                "issue",
                "create",
                "--title",
                title,
                "--body-file",
                str(body_file),
            ],
            check=False,
        )
    if result.returncode != 0:
        print(result.stderr.strip() or result.stdout.strip(), file=sys.stderr)
        sys.exit(result.returncode)
    url = (result.stdout or "").strip()
    if url:
        print(url)


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    _require_gh()
    _ensure_feature_label()

    existing = _existing_titles()
    created = 0
    skipped = 0

    for filename, title, labels in ISSUES:
        if title in existing:
            print(f"Überspringe (existiert bereits): {title}")
            skipped += 1
            continue
        _create_issue(ISSUES_DIR / filename, title, labels)
        created += 1

    print(f"\nFertig. Neu: {created}, übersprungen: {skipped}.")
    print("Prüfen: gh issue list")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
