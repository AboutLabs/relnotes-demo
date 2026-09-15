"""Gruppierung geparster Commits fuer die Ausgabe."""

from __future__ import annotations

from relnotes.parser import Commit

#: Reihenfolge der Sektionen im Changelog. "breaking" steht immer oben.
SECTION_ORDER = [
    "breaking",
    "feat",
    "fix",
    "perf",
    "refactor",
    "docs",
    "test",
    "build",
    "ci",
    "chore",
]


def group_commits(commits: list[Commit]) -> dict[str, list[Commit]]:
    """Gruppiert Commits nach Typ; Breaking Changes zusaetzlich separat.

    Leere Gruppen werden weggelassen. Die Reihenfolge der Keys folgt
    SECTION_ORDER.
    """
    buckets: dict[str, list[Commit]] = {key: [] for key in SECTION_ORDER}
    for commit in commits:
        if commit.breaking:
            buckets["breaking"].append(commit)
        buckets[commit.type].append(commit)
    return {key: value for key, value in buckets.items() if value}
