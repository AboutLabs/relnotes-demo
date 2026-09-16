# Demo D-002 – Scope-Fehler reproduzieren und gezielt korrigieren

## Fachlicher Anlass
Ein API-Commit wird mit einem fehlerhaften Scope dargestellt. Das Team möchte die Darstellung korrigieren und bestehende Parserfunktionen erhalten.

## Ablauf (15 Minuten)
1. **3 Minuten:** `python -m pytest tests/test_parser.py -q` ausführen. `test_scope_ohne_klammern` lesen und fehlerhafte sowie erwartete Scope-Ausgabe vergleichen.
2. **3 Minuten:** Teilnehmer eine Hypothese formulieren lassen. Erst danach den Plan für eine gezielte Änderung an `parser.py` anfordern.
3. **5 Minuten:** Umsetzung und Werkzeugaufrufe prüfen. Der Auftrag umfasst nur BUG-1. Diff gegen die fachliche Anforderung lesen; keine feste Zeilenanzahl als Erfolgsmaß verlangen.
4. **4 Minuten:** Parser- und Gesamttests ausführen. Nur BUG-2 und BUG-3 bleiben fehlgeschlagen. Scope-Korrektur committen und den Teilnehmern als abgegrenzten Patch zur gemeinsamen Übernahme zeigen.

## Beobachtungsauftrag
Welche Änderung ist fachlich nötig? Bleiben andere Fehler außerhalb dieses Auftrags? Was sagt der erfolgreiche Zieltest über noch ungeprüfte Fälle aus?

## Prompthilfe
> Analysiere `test_scope_ohne_klammern` und `parser.py`. Nenne die Ursache, eine minimale Korrektur und den Testnachweis für BUG-1. BUG-2 und BUG-3 bleiben offen. Bestehende Assertions bleiben erhalten. Beachte `AGENTS.md` und warte auf meine Planfreigabe.

## Übergabe und Fallback
Die Vorführung verändert kein Teilnehmer-Repository automatisch. Vor L-002 übernimmt jedes Team nur die gezeigte Scope-Korrektur, prüft den Diff und bestätigt genau zwei verbleibende Parserfehler. Referenzstand `d002` ist im Trainerpaket erzeugbar. Bei Schwierigkeiten die eine Korrektur gemeinsam einarbeiten; Quiet-Code und eigene Tests behalten.
