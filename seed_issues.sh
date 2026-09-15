#!/usr/bin/env bash
# Legt die Kurs-Issues an. Bevorzugt seed_issues.py (plattformübergreifend).
# Windows ohne Git Bash: py seed_issues.py  oder  .\seed_issues.ps1
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

run_python() {
  if command -v python3 >/dev/null 2>&1; then
    exec python3 "$ROOT/seed_issues.py" "$@"
  fi
  if command -v python >/dev/null 2>&1; then
    exec python "$ROOT/seed_issues.py" "$@"
  fi
  if command -v py >/dev/null 2>&1; then
    exec py -3 "$ROOT/seed_issues.py" "$@"
  fi
  return 1
}

if run_python "$@"; then
  exit 0
fi

# Fallback ohne Python (nur gh + bash)
set +e
gh label create feature --color 0e8a16 --description "Neues Feature" 2>/dev/null

create() {
  local file="$1" title="$2" labels="$3"
  echo "Erzeuge Issue: $title"
  gh issue create --title "$title" --body-file "docs/issues/$file" --label "$labels" \
    || gh issue create --title "$title" --body-file "docs/issues/$file"
}

create ISSUE-01-types-filter.md "Feature: Commit-Typen filtern (--types)" "feature"
create ISSUE-02-semver.md       "Feature: Versionsvorschlag nach SemVer (--suggest-version)" "feature"
create ISSUE-03-json-format.md  "Feature: JSON-Ausgabe (--format json)" "feature"
create ISSUE-04-contributors.md "Feature: Mitwirkenden-Sektion (--contributors)" "feature"

echo "Fertig. Issues: gh issue list"
