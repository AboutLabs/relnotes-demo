# Demo D-001 – CLI-Version für Supportanfragen anzeigen

## Fachlicher Anlass
Ein Supportmitarbeiter muss erkennen können, welche RelNotes-Version installiert ist. Die Abfrage soll ohne Eingabedatei möglich sein.

## Ablauf (15 Minuten)
1. **3 Minuten:** `relnotes --help` und `cli.py` zeigen. Teilnehmer formulieren vor dem Prompt die Abnahme: Ausgabe enthält Version, Exit-Code 0, kein `--input` erforderlich.
2. **3 Minuten:** Auftrag im Plan-Modus selbst formulieren. `AGENTS.md`, betroffene Dateien und geplante Tests prüfen; dann Umsetzung starten.
3. **5 Minuten:** Diff besprechen und `relnotes --version` ausführen. Prüfen, ob die Implementierung mit argparse zusammenarbeitet; ein anderer korrekter Ansatz ist anhand Verhalten und Wartbarkeit zu beurteilen.
4. **4 Minuten:** CLI-Test mit `SystemExit(0)` und Versionsausgabe zeigen. Gesamtsuite ausführen: die drei bekannten Parserfehler bleiben. Ergebnis committen.

## Beobachtungsauftrag
Welche Anforderung verhindert, dass `--version` irrtümlich eine Eingabedatei verlangt? Welcher Test weist dies nach?

## Prompthilfe nach der Anforderungsrunde
> Plane eine Option `--version` für RelNotes. Sie soll die Projektversion ausgeben und erfolgreich enden, ohne `--input` zu benötigen. Beachte `AGENTS.md`. Nenne die betroffenen Dateien und den passenden Test. Warte vor Codeänderungen auf meine Freigabe.

Nach Planfreigabe:

> Setze diesen Plan um. Ergänze den Test und führe die zugehörigen Tests sowie die Gesamtsuite aus. Die bekannten Parserfehler bleiben außerhalb dieses Auftrags.

## Übergabe und Fallback
Die Demo läuft im Trainer-Repository. Die Teilnehmer beginnen L-001 an ihrem eigenen Stand; `--version` ist keine Voraussetzung. Bei ausgefallenem Agenten Plan und Diff anhand eines vorbereiteten Referenzstands erklären. Trainerbefehl: `python scripts/build_course_checkpoint.py m001 <neuer-zielordner>` aus dem Master-Repository. Die Musterlösung wird nur im Trainerpaket bereitgestellt.
