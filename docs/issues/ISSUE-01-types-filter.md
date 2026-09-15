# Feature: Commit-Typen filtern (`--types`)

**Labels:** feature, demo-d-003
**Abnahme:** `tests/features/test_issue01_types_filter.py` (Skip-Marker entfernen)

## Beschreibung

Als Release-Manager möchte ich das Changelog auf bestimmte Commit-Typen
einschränken können (z. B. nur `feat` und `fix` für Kunden-Changelogs),
damit interne Commits (chore, ci, test) nicht im Kundendokument landen.

## Anforderungen

- Neue Funktion `filter_by_types(commits, types)` in `src/relnotes/grouping.py`;
  Reihenfolge der Commits bleibt erhalten.
- Neue CLI-Option `--types`, kommagetrennt: `relnotes -i log.txt --types feat,fix`
- Ohne `--types` bleibt das Verhalten unverändert.

## Definition of Done

- Skip-Marker in `tests/features/test_issue01_types_filter.py` entfernt
- `python -m pytest -q` komplett grün (keine Regressionen)
- Patch minimal, Commit nach Conventional Commits
