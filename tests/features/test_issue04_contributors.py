"""Feature-Tests fuer ISSUE-04 (--contributors). Reserve-Issue fuer schnelle Teams.

Skip-Marker entfernen, sobald das Feature implementiert ist.
"""
import pytest

pytestmark = pytest.mark.skip(reason="ISSUE-04: Skip entfernen, wenn implementiert (Reserve)")


def make(author, type_="feat"):
    from relnotes.parser import Commit
    return Commit(hash="abc1234", author=author, type=type_, scope=None,
                  description="x", breaking=False)


def test_contributors_sektion_sortiert_nach_anzahl():
    from relnotes.render import contributors_section
    commits = [make("Anna"), make("Ben"), make("Anna"), make("Cem"), make("Anna"), make("Ben")]
    section = contributors_section(commits)
    assert "## Mitwirkende" in section
    lines = [line for line in section.splitlines() if line.startswith("-")]
    assert lines[0] == "- Anna (3 Commits)"
    assert lines[1] == "- Ben (2 Commits)"
    assert lines[2] == "- Cem (1 Commit)"
