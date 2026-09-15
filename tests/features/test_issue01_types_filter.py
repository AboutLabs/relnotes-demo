"""Feature-Tests fuer ISSUE-01 (--types Filter). Wird in Demo D-003 geloest.

Skip-Marker entfernen, sobald das Feature implementiert ist.
"""
import pytest

pytestmark = pytest.mark.skip(reason="ISSUE-01: Skip entfernen, wenn implementiert (Demo D-003)")


def make(type_, desc="x"):
    from relnotes.parser import Commit
    return Commit(hash="abc1234", author="Anna", type=type_, scope=None,
                  description=desc, breaking=False)


def test_filter_behaelt_nur_gewuenschte_typen():
    from relnotes.grouping import filter_by_types
    commits = [make("feat"), make("fix"), make("chore")]
    result = filter_by_types(commits, ["feat", "fix"])
    assert [c.type for c in result] == ["feat", "fix"]


def test_cli_akzeptiert_types_option(tmp_path):
    from relnotes.cli import main
    src = tmp_path / "commits.txt"
    src.write_text(
        "a1b2c3d|Anna Beispiel|feat: eins\n"
        "b2c3d4e|Ben Muster|chore: aufraeumen\n",
        encoding="utf-8",
    )
    out = tmp_path / "NOTES.md"
    main(["--input", str(src), "--output", str(out), "--types", "feat,fix"])
    content = out.read_text(encoding="utf-8")
    assert "eins" in content
    assert "aufraeumen" not in content
