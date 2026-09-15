"""Feature-Tests fuer ISSUE-02 (--suggest-version). Lab L-003, Level 1.

Skip-Marker entfernen, sobald das Feature implementiert ist.
"""
import pytest

pytestmark = pytest.mark.skip(reason="ISSUE-02: Skip entfernen, wenn implementiert (Lab L-003, Level 1)")


def make(type_, breaking=False):
    from relnotes.parser import Commit
    return Commit(hash="abc1234", author="Anna", type=type_, scope=None,
                  description="x", breaking=breaking)


def test_breaking_change_bumpt_major():
    from relnotes.semver import suggest_version
    assert suggest_version("2.3.1", [make("feat", breaking=True)]) == "3.0.0"


def test_feat_bumpt_minor():
    from relnotes.semver import suggest_version
    assert suggest_version("2.3.1", [make("feat"), make("fix")]) == "2.4.0"


def test_fix_bumpt_patch():
    from relnotes.semver import suggest_version
    assert suggest_version("2.3.1", [make("fix"), make("perf")]) == "2.3.2"


def test_nur_docs_und_chore_aendern_nichts():
    from relnotes.semver import suggest_version
    assert suggest_version("2.3.1", [make("docs"), make("chore")]) == "2.3.1"


def test_cli_gibt_versionsvorschlag_aus(tmp_path, capsys):
    from relnotes.cli import main
    src = tmp_path / "commits.txt"
    src.write_text("a1b2c3d|Anna Beispiel|feat: eins\n", encoding="utf-8")
    main(["--input", str(src), "--output", str(tmp_path / "n.md"),
          "--suggest-version", "1.0.0"])
    captured = capsys.readouterr()
    assert "Versionsvorschlag: 1.1.0" in captured.err
