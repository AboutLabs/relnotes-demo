# Legt die Kurs-Issues an (Wrapper für seed_issues.py).
# Voraussetzung: gh auth login --web
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$py = Get-Command py -ErrorAction SilentlyContinue
if ($py) {
    & py -3 (Join-Path $here "seed_issues.py") @args
    exit $LASTEXITCODE
}
$python = Get-Command python -ErrorAction SilentlyContinue
if ($python) {
    & python (Join-Path $here "seed_issues.py") @args
    exit $LASTEXITCODE
}
Write-Error "Python nicht gefunden. Bitte Python 3.11+ installieren oder 'py -3 seed_issues.py' ausführen."
exit 1
