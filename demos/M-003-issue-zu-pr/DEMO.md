# Demo D-003 – Commit-Filter als nachvollziehbaren Pull Request übergeben

## Fachlicher Anlass
Das Release-Team benötigt für eine interne Übersicht nur ausgewählte Commit-Typen. Die Änderung soll ein anderer Entwickler prüfen können.

## Erforderlicher Demo-Stand
Bereiten Sie ein eigenes Trainer-Demorepository auf dem Referenzstand `m002` vor. Darin sind Quiet-Funktion und alle drei Parserkorrekturen enthalten; die Feature-Tests bleiben übersprungen. Prüfen Sie den Stand unmittelbar vor der Demo:

```bash
python scripts/build_course_checkpoint.py m002 <neuer-zielordner>
cd <neuer-zielordner>
python -m pytest -q
```

Erwartet werden keine fehlgeschlagenen Tests. Die konkrete Zahl erfolgreicher Tests kann nach eigenen Ergänzungen abweichen.

## Ablauf (15 Minuten)
1. **3 Minuten:** ISSUE-01 unter `docs/issues/ISSUE-01-types-filter.md` lesen. Gemeinsam Anforderungen und einen passenden Test benennen. GitHub-Issue über den Titel auswählen, nicht eine feste Nummer voraussetzen.
2. **4 Minuten:** Branch `feat/issue-01-types-filter` anlegen. Auftrag im Plan-Modus formulieren; Filterverhalten, Dateien und Testplan prüfen, dann umsetzen.
3. **4 Minuten:** Nur den Skip-Marker für ISSUE-01 entfernen. Gezielt und vollständig testen. Diff und Testausgabe in die PR-Vorlage übernehmen; unzutreffende Agentenaussagen korrigieren.
4. **4 Minuten:** Reviewer prüft einen konkreten Fall und begründet Approval oder Request changes. Zeigen, welche Schutzregeln tatsächlich konfiguriert sind. Ohne technische Sperre bleibt das Review eine Kursvereinbarung.

## Beobachtungsauftrag
Kann der Reviewer aus dem PR erkennen, welches Problem gelöst wurde, welche Prüfungen liefen und welche Einschränkungen verbleiben?

## Prompthilfe
> Plane ISSUE-01 anhand des Issue-Texts. Nenne betroffene Dateien und Tests, beachte AGENTS.md und warte auf Freigabe. Bereite nach geprüfter Umsetzung eine PR-Beschreibung mit Problem, Änderung und tatsächlich ausgeführten Testbefehlen vor. Den PR öffne ich selbst.

## Übergabe und Fallback
Die Filterfunktion ist keine Voraussetzung für das SemVer-Lab. Alle Teams beginnen ISSUE-02 von ihrem geprüften M-002-Stand. Nach dem Demo-Review keine ungeprüften Änderungen in Team-Repositories kopieren. Bei fehlendem GitHub-Zugriff Diff und PR-Vorlage lokal prüfen; serverseitiges Review gilt dann noch nicht als nachgewiesen. Falls der Demo-Stand nicht stimmt, den vorbereiteten `m002`-Stand verwenden und die Abweichung nicht live reparieren.
