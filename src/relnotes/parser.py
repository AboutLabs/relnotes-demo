"""Conventional-Commits-Parser fuer RelNotes.

Erwartetes Zeilenformat (aus `git log --pretty=format:"%h|%an|%s"`):

    a1b2c3d|Anna Beispiel|feat(api): login endpoint hinzugefuegt

Hinweis fuer den Kurs: Dieses Modul enthaelt absichtlich eingebaute Fehler.
Die pytest-Suite zeigt, welche. Siehe README ("Warum sind Tests rot?").
"""

from __future__ import annotations

import re
from dataclasses import dataclass

#: Commit-Typen nach Conventional Commits, die RelNotes auswertet.
KNOWN_TYPES = {"feat", "fix", "perf", "refactor", "docs", "test", "build", "ci", "chore"}

HEADER_RE = re.compile(
    r"^(?P<type>[a-z]+)"
    r"(?P<scope>\([^)]*\))?"
    r"(?P<bang>!)?"
    r":\s+(?P<desc>.+)$"
)


@dataclass
class Commit:
    """Ein geparster Commit."""

    hash: str
    author: str
    type: str
    scope: str | None
    description: str
    breaking: bool = False


def parse_line(line: str) -> Commit | None:
    """Parst eine einzelne Log-Zeile.

    Gibt ``None`` zurueck, wenn die Zeile kein gueltiger
    Conventional Commit ist (z. B. Merge-Commits).
    """
    parts = line.split("|", 2)
    if len(parts) != 3:
        return None
    sha, author, subject = parts

    match = HEADER_RE.match(subject)
    if not match:
        return None

    ctype = match.group("type")
    if ctype not in KNOWN_TYPES:
        return None

    scope = match.group("scope")
    breaking = "BREAKING CHANGE" in subject

    return Commit(
        hash=sha.strip(),
        author=author.strip(),
        type=ctype,
        scope=scope,
        description=match.group("desc").strip(),
        breaking=breaking,
    )


def parse_lines(text: str) -> list[Commit]:
    """Parst mehrzeiligen Log-Text und ueberspringt ungueltige Zeilen."""
    commits: list[Commit] = []
    for line in text.splitlines():
        if not line.strip():
            continue
        commit = parse_line(line)
        if commit is not None:
            commits.append(commit)
    return commits
