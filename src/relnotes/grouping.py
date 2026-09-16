"""Gruppierung geparster Commits fuer die Ausgabe.

Wandelt die flache Commit-Liste in Buckets um: ein Dictionary, dessen Keys
die Sektionen aus SECTION_ORDER sind und dessen Values Listen von Commits
sind. Breaking-Commits stehen in zwei Buckets: einmal unter "breaking" (oben
im Changelog) und einmal unter ihrem Conventional-Typ (feat/fix/...).
"""

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
        # Typ-Bucket immer fuellen, auch wenn der Commit schon unter breaking liegt.
        buckets[commit.type].append(commit)
    return {key: value for key, value in buckets.items() if value}
