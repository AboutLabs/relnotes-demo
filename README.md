# RelNotes – Release Notes aus Conventional Commits

Kursprojekt zum ppedv-Seminar **Agentic Coding – KI-Agenten im Entwickleralltag**.

RelNotes ist ein kleines CLI-Tool, das aus Git-Historie (Conventional Commits)
strukturierte Release Notes generiert – und im Kurs den kompletten Team-Workflow
durchläuft: **Issue → Agent → Branch → Pull Request → Review → CI → Release**.
Am Ende des Tages begründen Sie eine Release-Entscheidung; die Veröffentlichung ist optional.

## Bekannte Fehler im Kursstart

Die Fehler sind für die Übungen vorbereitet. Drei Tests in `tests/test_parser.py` markieren eingebaute
Fehler – sie sind der Arbeitsvorrat für Demo D-002 und Lab L-002:

| Test | Bug | Wird gelöst in |
|---|---|---|
| `test_scope_ohne_klammern` | BUG-1: Scope enthält Klammern | **Demo D-002** (Trainer) |
| `test_bang_markiert_breaking_change` | BUG-2: `!` wird ignoriert | **Lab L-002, Pflicht** |
| `test_grossschreibung_und_whitespace_werden_normalisiert` | BUG-3: `Fix:` fällt raus | **Lab L-002, Pflicht** |

Die Tests unter `tests/features/` sind **geskippt** – sie gehören zu den
Feature-Issues (siehe `docs/issues/`) und werden in Demo D-003 und Lab L-003
gezielt aktiviert. Ziel: erfüllte Anforderungen, erfolgreiche aktive Tests und begründete Abnahme.

## Setup (ca. 5 Minuten)

**Kurs-VM (Windows Server, PowerShell):** Repo liegt meist vorbereitet — nur
`gh auth login --web`. Einrichtung nach Gruppengröße:
[`docs/einrichtung-teilnehmer.md`](../../docs/einrichtung-teilnehmer.md) (Master-Repo).

**Selbst-Setup** (Generalprobe / kleine Gruppe), in **PowerShell**:

```powershell
git clone <team-repo>
cd <team-repo>
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
python -m pytest -q              # Erwartung: 3 failed, 15 passed, 10 skipped
relnotes --input sample-data/commits.txt
gh auth login --web
.\seed_issues.ps1                 # 4 Kurs-Issues (nicht ./seed_issues.sh!)
gh issue list
```

> **Hinweis:** `./seed_issues.sh` in PowerShell schlägt auf Windows-Server-VMs
> fehl (WSL-Stub). Immer `.\seed_issues.ps1` oder `py -3 seed_issues.py` nutzen.

## Projektstruktur

```
src/relnotes/       Produktivcode (parser, grouping, render, semver, cli)
tests/              pytest-Suite (Definition of Done für Bugs)
tests/features/     Abnahmekriterien für die Feature-Issues (geskippt)
sample-data/        Beispiel-Log für lokale Läufe
docs/issues/        Feature-Issues als Markdown (Quelle für seed_issues.ps1 / seed_issues.py)
demos/              Demo-Drehbücher M-001 bis M-004
labs/               Lab-Aufgabenblätter L-001 bis L-004 (eigener Auftrag vor optionaler Prompthilfe)
AGENTS.md           Team-Regeln für KI-Agenten (versioniert und geprüft)
.cursor/rules/      Cursor-spezifische Projektregeln
.github/workflows/  ci.yml (Lab L-004) und release.yml (Demo D-004)
```

## Tagesablauf (Kurzfassung)

| Modul | Demo (Drehbuch in `demos/`) | Lab und Nachweis |
|---|---|---|
| M-001 | D-001: Agent ergänzt `--version` | L-001: Agent ergänzt `--quiet` |
| M-002 | D-002: Agent fixt BUG-1 gegen pytest | L-002: BUG-2 und BUG-3 fixen |
| M-003 | D-003: Issue #1 → Agent → PR | L-003: ISSUE-02 → PR → Peer-Review |
| M-004 | D-004: Release-Pipeline live | L-004: CI-Gegenprobe und Release-Entscheidung |

## Konventionen

- Commits nach [Conventional Commits](https://www.conventionalcommits.org/) –
  RelNotes verarbeitet die ausgewählte Historie beim Release.
- Unabhängiges Review vor Übernahme; nach M-004 zusätzlich CI. Technischen Schutz und mögliche Ausnahmen im Repository prüfen.
- Agent-Regeln stehen in `AGENTS.md` und `.cursor/rules/` – Änderungen daran
  laufen über Pull Requests wie jeder andere Code.

*Dieses Repository dient ausschließlich Schulungszwecken (ppedv AG).*

## Übergaben und Nachweise

Die Scope-Korrektur aus D-002 wird vor L-002 gemeinsam in jedes Team-Repository übernommen. `--version` und `--types` aus den Demos sind keine Voraussetzungen der Pflicht-Labs. Nach L-002 müssen beide Parserfehler korrigiert sein. Nach L-003 ist ISSUE-02 geprüft und integriert. Absolute Testzahlen nach Kursstart hängen von eigenen Ergänzungen ab.

Verwenden Sie `docs/arbeitsnachweis.md` und die PR-Vorlage. Ohne Actions-Zugriff ist eine lokale Gegenprobe möglich; Trigger und serverseitige Sperren gelten damit noch nicht als geprüft. Vor einem Tag wird der aktuelle Stand geprüft; `release.yml` führt zusätzlich Tests am Tag aus.
