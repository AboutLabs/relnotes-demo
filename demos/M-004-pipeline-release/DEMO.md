# Demo D-004 – Den geprüften Tag-Stand vor der Veröffentlichung testen

## Fachlicher Anlass
Ein erfolgreicher PR-Lauf beweist nicht, dass ein später gesetzter Tag denselben Stand bezeichnet. Vor Veröffentlichung sollen daher die Tests am Tag-Stand erneut laufen.

## Erforderlicher Demo-Stand
Bereiten Sie ein eigenes Trainer-Demorepository auf dem Referenzstand `m003` vor. Darin sind Quiet-Funktion, Parserkorrekturen und der Versionsvorschlag aus ISSUE-02 enthalten. Prüfen Sie den Stand unmittelbar vor der Demo:

```bash
python scripts/build_course_checkpoint.py m003 <neuer-zielordner>
cd <neuer-zielordner>
python -m pytest -q
relnotes -i sample-data/commits.txt --suggest-version 2.3.1
```

Erwartet werden keine fehlgeschlagenen Tests und ein Versionsvorschlag. Die Filterfunktion aus D-003 ist nicht erforderlich.

## Ablauf (15 Minuten)
1. **4 Minuten:** `release.yml` lesen: Tag-Trigger, Checkout, Installation mit Dev-Abhängigkeiten, pytest, Commit-Bereich, Generierung, Release. Der Testschritt steht vor Generierung und Veröffentlichung.
2. **4 Minuten:** Geprüften Integrationsstand und Review zeigen. `git status` und `git rev-parse HEAD` kontrollieren. Aktuellen Release-Tag ermitteln; nur folgende Commits für den Versionsvorschlag verwenden. Ohne vorherigen Tag gilt die gesamte Historie. Beispielbefehle im Trainer-Leitfaden verwenden und Platzhalter auflösen.
3. **4 Minuten:** Einen neuen, geprüften Tag auf den beabsichtigten Commit setzen und pushen. Actions-Lauf öffnen und Commit-ID sowie tatsächliche Testausführung kontrollieren.
4. **3 Minuten:** Nach erfolgreichem Abschluss Release Notes gegen ausgewählte Commits prüfen. Bei laufendem Job Status als offen markieren; in der Auswertung erneut prüfen.

## Beobachtungsauftrag
Welcher Commit wird getestet? An welcher Stelle verhindert ein pytest-Fehler die Veröffentlichung? Was muss zusätzlich fachlich geprüft werden?

## Übergabe und Fallback
Die Teilnehmer benötigen für L-004 einen integrierten, fehlerfreien Stand aus M-003. Ihr `ci.yml` bleibt absichtlich unvollständig. Ohne Actions-Zugriff pytest und die Generierung lokal zeigen. Das belegt weder den Tag-Trigger noch die serverseitige Veröffentlichung; diese Prüfungen werden ausdrücklich als offen dokumentiert. Ein Release ist keine Pflicht, die begründete Release-Entscheidung schon. Falls der Demo-Stand nicht stimmt, den vorbereiteten `m003`-Stand verwenden und die Abweichung nicht live reparieren.
