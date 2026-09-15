"""Feature-Tests fuer ISSUE-03 (--format json). Lab L-003, Level 2.

Skip-Marker entfernen, sobald das Feature implementiert ist.
"""
import json

import pytest

pytestmark = pytest.mark.skip(reason="ISSUE-03: Skip entfernen, wenn implementiert (Lab L-003, Level 2)")


def make(type_, scope=None, desc="x"):
    from relnotes.parser import Commit
    return Commit(hash="abc1234", author="Anna", type=type_, scope=scope,
                  description=desc, breaking=False)


def test_to_json_liefert_parsebare_struktur():
    from relnotes.grouping import group_commits
    from relnotes.render import to_json
    groups = group_commits([make("feat", scope="api", desc="eins"), make("fix", desc="zwei")])
    data = json.loads(to_json(groups))
    assert data["sections"][0]["type"] == "feat"
    assert data["sections"][0]["items"][0]["description"] == "eins"
    assert data["sections"][0]["items"][0]["scope"] == "api"
    assert data["sections"][1]["items"][0]["author"] == "Anna"


def test_cli_schreibt_json(tmp_path):
    from relnotes.cli import main
    src = tmp_path / "commits.txt"
    src.write_text("a1b2c3d|Anna Beispiel|feat: eins\n", encoding="utf-8")
    out = tmp_path / "notes.json"
    main(["--input", str(src), "--output", str(out), "--format", "json"])
    data = json.loads(out.read_text(encoding="utf-8"))
    assert data["sections"][0]["items"][0]["description"] == "eins"
