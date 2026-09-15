# Feature: JSON-Ausgabe (`--format json`)

**Labels:** feature, lab-l-003-level-2
**Abnahme:** `tests/features/test_issue03_json.py` (Skip-Marker entfernen)

## Beschreibung

Als Plattform-Team möchten wir die Release Notes maschinenlesbar abgreifen
(z. B. für ein internes Dashboard oder einen Slack-Bot), daher braucht
RelNotes neben Markdown eine JSON-Ausgabe.

## Anforderungen

- Neue Funktion `to_json(groups)` in `src/relnotes/render.py`.
  Struktur (siehe Tests): `{"sections": [{"type", "title", "items": [
  {"hash", "scope", "description", "author", "breaking"}]}]}`
- JSON mit `ensure_ascii=False` und `indent=2`.
- Neue CLI-Option `--format` mit den Werten `markdown` (Default) und `json`.

## Definition of Done

- Skip-Marker in `tests/features/test_issue03_json.py` entfernt
- `python -m pytest -q` komplett grün (keine Regressionen)
- Patch minimal, Commit nach Conventional Commits, PR mit Beschreibung
