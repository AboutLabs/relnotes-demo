# Feature: Versionsvorschlag nach SemVer (`--suggest-version`)

**Labels:** feature, lab-l-003-level-1
**Abnahme:** `tests/features/test_issue02_semver.py` (Skip-Marker entfernen)

## Beschreibung

Als Team möchten wir aus den Commits seit dem letzten Release automatisch
einen Vorschlag für die nächste Versionsnummer ableiten, damit Releases
konsistent nach Semantic Versioning nummeriert werden.

## Anforderungen

Implementiere `suggest_version(current, commits)` in `src/relnotes/semver.py`:

| Bedingung (erste zutreffende gewinnt) | Bump | Beispiel (von 2.3.1) |
|---|---|---|
| mind. ein Breaking Change | Major | 3.0.0 |
| mind. ein `feat` | Minor | 2.4.0 |
| mind. ein `fix` oder `perf` | Patch | 2.3.2 |
| sonst | keiner | 2.3.1 |

CLI: `relnotes -i log.txt --suggest-version 1.2.0` gibt zusätzlich auf stderr
aus: `Versionsvorschlag: 1.3.0` (Format exakt so, siehe Tests).

## Ergänzende Abnahmekriterien

- Leere Commit-Liste: aktuelle Version bleibt erhalten.
- Bei mehreren Typen gilt die höchste Priorität unabhängig von der Reihenfolge.
- Nach einem Major-Bump werden Minor/Patch null; nach Minor wird Patch null.
- Eingabe im Kurs: drei nichtnegative Ganzzahlen `x.y.z`; Prerelease- und Build-Suffixe gehören nicht zu diesem Auftrag.
- Für `0.x` gilt ausdrücklich die vereinfachte Kurskonvention: Breaking Change erhöht auf `1.0.0`. Das ist eine Projektentscheidung, keine allgemeine SemVer-Pflicht für Entwicklungsstände.
- Der Vorschlag berücksichtigt die übergebenen Commits. Für Releases muss der Aufrufer die Historie seit dem letzten Release verwenden.

Referenz: https://semver.org/spec/v2.0.0.html

## Definition of Done

- Skip-Marker in `tests/features/test_issue02_semver.py` entfernt
- `python -m pytest -q` komplett grün (keine Regressionen)
- Patch minimal, Commit nach Conventional Commits, PR mit Beschreibung
