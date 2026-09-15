from relnotes.grouping import group_commits
from relnotes.parser import Commit
from relnotes.render import format_commit, render_markdown


def make(type_, scope=None, desc="x", breaking=False):
    return Commit(hash="abc1234", author="Anna", type=type_, scope=scope,
                  description=desc, breaking=breaking)


def test_format_commit_mit_scope():
    line = format_commit(make("fix", scope="parser", desc="scope repariert"))
    assert line == "- **parser**: scope repariert (abc1234, Anna)"


def test_format_commit_ohne_scope():
    line = format_commit(make("feat", desc="neues feature"))
    assert line == "- neues feature (abc1234, Anna)"


def test_render_markdown_enthaelt_titel_und_sektionen():
    groups = group_commits([make("feat", desc="a"), make("fix", desc="b")])
    markdown = render_markdown(groups, version="v1.2.0")
    assert markdown.startswith("# Release Notes v1.2.0")
    assert "## Features" in markdown
    assert "## Bugfixes" in markdown
    assert markdown.index("## Features") < markdown.index("## Bugfixes")


def test_breaking_sektion_steht_oben():
    groups = group_commits([make("feat", desc="a", breaking=True), make("fix", desc="b")])
    markdown = render_markdown(groups)
    assert markdown.index("## Breaking Changes") < markdown.index("## Features")
