from relnotes.grouping import group_commits
from relnotes.parser import Commit


def make(type_, breaking=False, desc="x"):
    return Commit(hash="abc1234", author="Anna", type=type_, scope=None,
                  description=desc, breaking=breaking)


def test_gruppen_folgen_der_sektionsreihenfolge():
    commits = [make("chore"), make("fix"), make("feat")]
    groups = group_commits(commits)
    assert list(groups.keys()) == ["feat", "fix", "chore"]


def test_breaking_changes_erscheinen_separat_und_im_typ():
    commits = [make("feat", breaking=True, desc="grosse aenderung")]
    groups = group_commits(commits)
    assert "breaking" in groups
    assert groups["breaking"][0].description == "grosse aenderung"
    assert groups["feat"][0].description == "grosse aenderung"


def test_leere_gruppen_werden_weggelassen():
    groups = group_commits([make("fix")])
    assert list(groups.keys()) == ["fix"]
