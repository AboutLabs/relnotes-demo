# Agenten-Regeln für dieses Repository

Diese Datei beschreibt die Arbeitsanweisungen für KI-Agenten in diesem Projekt.
Prüfen Sie im verwendeten Werkzeug, ob und wie diese Datei geladen wird. Sie ist versioniert und wird
wie Code behandelt: Änderungen nur per Pull Request.

## Projekt in einem Satz

RelNotes generiert aus Git-Log-Zeilen (`hash|autor|subject`, Conventional
Commits) ein gruppiertes Markdown-Changelog. Python 3.11+, nur Standard-
bibliothek, Layout `src/`, Tests mit pytest.

## Befehle

- Tests: `python -m pytest -q`
- Einzelner Test: `python -m pytest tests/test_parser.py -q`
- CLI lokal: `relnotes --input sample-data/commits.txt`

## Regeln (verbindlich)

1. **Minimale Patches.** Ändere nur, was für die konkrete Aufgabe nötig ist.
   Kein Umformatieren fremder Dateien, kein Umbenennen ohne Auftrag.
   Erklärende Kommentare im Produktivcode und den Codewalkthrough in der
   README nicht entfernen, sofern die Aufgabe sie nicht betrifft.
2. **Tests sind die Abnahme.** Führe nach jeder Änderung `python -m pytest -q`
   aus. Eine Aufgabe ist erst fertig, wenn die zugehörigen Tests grün sind
   und keine vorher grünen Tests rot geworden sind. Zusätzlich sind Anforderungen,
   Diff und nicht abgedeckte Fälle zu prüfen.
3. **Vorhandene Tests werden niemals geändert oder gelöscht**, um sie grün zu
   bekommen. Neue Tests ergänzen ist erwünscht. Der Skip-Marker des ausdrücklich
   beauftragten Features darf zur Abnahme entfernt werden. Die isolierte neue
   CI-Gegenprobe aus L-004 ist zulässig und vor dem Merge wieder zu entfernen.
4. **Keine neuen Abhängigkeiten.** Das Projekt nutzt bewusst nur die
   Python-Standardbibliothek (plus pytest für Entwicklung).
5. **Keine Netzwerkzugriffe durch den Coding-Agenten, keine Secrets.** Lies keine
   Dateien außerhalb des Repos, gib keine Umgebungsvariablen aus. GitHub-Aktionen
   wie Push, PR, Review und Release führen die Teilnehmer selbst aus.
6. **Commits nach Conventional Commits**, Beschreibung auf Deutsch,
   z. B. `fix(parser): bang-marker setzt breaking-flag`.
7. **Erst planen, dann ändern.** Nenne vor Codeänderungen kurz die geplanten
   Schritte und betroffenen Dateien (Plan → Act → Reflect).
