"""Conventional-Commits-Parser fuer RelNotes.

Erwartetes Zeilenformat (aus `git log --pretty=format:"%h|%an|%s"`):

    a1b2c3d|Anna Beispiel|feat(api): login endpoint hinzugefuegt

Ablauf pro Zeile:
    1. In hash | autor | subject zerlegen (genau drei Felder).
    2. Subject gegen HEADER_RE matchen (type, optionaler Scope, optionaler Bang,
       Beschreibung).
    3. Typ gegen KNOWN_TYPES pruefen; unbekannte Typen (wip, Merge, ...)
       verwerfen.
    4. Commit-Dataclass bauen. Ungueltiges ergibt None und wird spaeter
       uebersprungen.

Hinweis fuer den Kurs: Dieses Modul enthaelt absichtlich eingebaute Fehler.
Die pytest-Suite zeigt, welche. Siehe README ("Bekannte Fehler im Kursstart").
"""

from __future__ import annotations

import re
from dataclasses import dataclass

#: Commit-Typen nach Conventional Commits, die RelNotes auswertet.
#: Alles ausserhalb (z. B. "wip", "Merge ...") faellt stillschweigend raus.
KNOWN_TYPES = {"feat", "fix", "perf", "refactor", "docs", "test", "build", "ci", "chore"}

# Named groups im Subject:
#   type  - Buchstabenfolge vor Scope/Bang/Doppelpunkt
#   scope - optionale Klammergruppe, z. B. (api)
#   bang  - optionales "!" nach Typ/Scope (Breaking-Marker im Header)
#   desc  - Rest nach ": "
# Drei Tests in tests/test_parser.py markieren Luecken in diesem Ablauf.
HEADER_RE = re.compile(
    r"^(?P<type>[a-z]+)"
    r"(?P<scope>\([^)]*\))?"
    r"(?P<bang>!)?"
    r":\s+(?P<desc>.+)$"
)


@dataclass
class Commit:
    """Ein geparster Commit als gemeinsames Modell fuer grouping, render und semver."""

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
    # maxsplit=2: die Beschreibung darf selbst "|" enthalten.
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
