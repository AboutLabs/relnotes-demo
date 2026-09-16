"""Kommandozeilen-Einstieg fuer RelNotes.

Orchestriert die Pipeline, ohne selbst zu parsen oder zu formatieren:
Argumente lesen, Datei laden, parse -> group -> render, Ergebnis schreiben.
Die Statistik geht immer nach stderr, damit stdout reines Markdown bleibt.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from relnotes.grouping import group_commits
from relnotes.parser import parse_lines
from relnotes.render import render_markdown


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="relnotes",
        description="Generiert Release Notes aus Conventional Commits.",
    )
    parser.add_argument(
        "--input", "-i", required=True,
        help="Datei mit Log-Zeilen (Format: hash|autor|subject)",
    )
    parser.add_argument(
        "--output", "-o",
        help="Zieldatei fuer das Markdown (Standard: stdout)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    text = Path(args.input).read_text(encoding="utf-8")
    # Nur nicht-leere Zeilen zaehlen: leere Zeilen sind kein "Skip" im Sinne
    # von Merge-Commits oder unbekannten Typen.
    total = sum(1 for line in text.splitlines() if line.strip())
    commits = parse_lines(text)
    markdown = render_markdown(group_commits(commits))

    if args.output:
        Path(args.output).write_text(markdown, encoding="utf-8")
    else:
        print(markdown)

    skipped = total - len(commits)
    print(
        f"{len(commits)} Commits verarbeitet, {skipped} Zeilen uebersprungen.",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
