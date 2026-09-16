"""Versionsvorschlag nach Semantic Versioning (SemVer).

SemVer nummeriert Releases als MAJOR.MINOR.PATCH (z. B. 2.3.1):
inkompatible Aenderung -> Major, neues Verhalten -> Minor,
Fehlerbehebung -> Patch.

Dieses Modul ist ein Platzhalter fuer ISSUE-02 (Lab L-003, Level 1).
Es wird von der CLI noch nicht aufgerufen; grouping/render laufen ohne Version.

Regeln laut Issue:
  - mind. ein Breaking Change  -> Major-Bump (2.3.1 -> 3.0.0)
  - sonst mind. ein feat       -> Minor-Bump (2.3.1 -> 2.4.0)
  - sonst mind. ein fix/perf   -> Patch-Bump (2.3.1 -> 2.3.2)
  - sonst                      -> Version unveraendert
"""

from __future__ import annotations

from relnotes.parser import Commit


def suggest_version(current: str, commits: list[Commit]) -> str:
    """Schlaegt die naechste Version vor. Siehe ISSUE-02."""
    raise NotImplementedError("ISSUE-02: noch nicht implementiert")
