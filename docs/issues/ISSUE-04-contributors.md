# Feature: Mitwirkenden-Sektion (`--contributors`)

**Labels:** feature, reserve
**Abnahme:** `tests/features/test_issue04_contributors.py` (Skip-Marker entfernen)

## Beschreibung

Als Team möchten wir im Changelog sichtbar machen, wer zum Release
beigetragen hat.

## Anforderungen

- Neue Funktion `contributors_section(commits)` in `src/relnotes/render.py`:
  Überschrift `## Mitwirkende`, danach je Zeile `- <Name> (<n> Commits)`
  (Singular: `1 Commit`), sortiert nach Anzahl absteigend, bei Gleichstand
  alphabetisch.
- Neue CLI-Flag `--contributors` hängt die Sektion ans Markdown an
  (nur im Markdown-Format).

## Definition of Done

- Skip-Marker in `tests/features/test_issue04_contributors.py` entfernt
- `python -m pytest -q` komplett grün (keine Regressionen)
- Patch minimal, Commit nach Conventional Commits, PR mit Beschreibung
