"""Rendering der gruppierten Commits als Markdown.

Erwartet das Dict aus grouping.group_commits (Keys bereits in SECTION_ORDER).
Die CLI uebergibt derzeit kein ``version``; der Parameter ist fuer spaetere
Anbindung an semver.suggest_version vorgesehen.
"""

from __future__ import annotations

from relnotes.parser import Commit

#: Interne Bucket-Keys -> Ueberschriften im Changelog.
SECTION_TITLES = {
    "breaking": "Breaking Changes",
    "feat": "Features",
    "fix": "Bugfixes",
    "perf": "Performance",
    "refactor": "Refactoring",
    "docs": "Dokumentation",
    "test": "Tests",
    "build": "Build",
    "ci": "CI",
    "chore": "Sonstiges",
}


def format_commit(commit: Commit) -> str:
    """Formatiert einen Commit als Markdown-Listeneintrag.

    Beispiel mit Scope: ``- **parser**: fehler behoben (abc1234, Anna)``
    Ohne Scope:         ``- fehler behoben (abc1234, Anna)``
    """
    scope = f"**{commit.scope}**: " if commit.scope else ""
    return f"- {scope}{commit.description} ({commit.hash}, {commit.author})"


def render_markdown(groups: dict[str, list[Commit]], version: str | None = None) -> str:
    """Rendert die Gruppen als Markdown-Changelog."""
    title = f"# Release Notes {version}" if version else "# Release Notes"
    lines = [title, ""]
    for key, commits in groups.items():
        lines.append(f"## {SECTION_TITLES.get(key, key)}")
        lines.append("")
        for commit in commits:
            lines.append(format_commit(commit))
        lines.append("")
    # Immer genau ein abschliessendes Newline, auch bei leeren Gruppen.
    return "\n".join(lines).rstrip() + "\n"
