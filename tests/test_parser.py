"""Tests fuer den Commit-Parser.

Hinweis: Einige Tests schlagen absichtlich fehl - sie markieren die
eingebauten Bugs fuer Demo D-002 und Lab L-002.
"""

from relnotes.parser import parse_line, parse_lines


def test_einfacher_feat_commit():
    commit = parse_line("a1b2c3d|Anna Beispiel|feat: login endpoint hinzugefuegt")
    assert commit is not None
    assert commit.type == "feat"
    assert commit.scope is None
    assert commit.description == "login endpoint hinzugefuegt"
    assert commit.breaking is False


def test_scope_ohne_klammern():
    # BUG-1 (Demo D-002): scope muss "parser" sein, nicht "(parser)"
    commit = parse_line("b2c3d4e|Ben Muster|fix(parser): scope wird korrekt extrahiert")
    assert commit is not None
    assert commit.scope == "parser"


def test_bang_markiert_breaking_change():
    # BUG-2 (Lab L-002, Level 1): "!" nach Typ/Scope bedeutet Breaking Change
    commit = parse_line("c3d4e5f|Cem Yilmaz|feat(api)!: token statt session-cookie")
    assert commit is not None
    assert commit.breaking is True


def test_grossschreibung_und_whitespace_werden_normalisiert():
    # BUG-3 (Lab L-002, Pflichtaufgabe): "Fix:" und fuehrende Leerzeichen tolerieren
    commit = parse_line("d4e5f6a|Dana Weber|  Fix: tippfehler in fehlermeldung  ")
    assert commit is not None
    assert commit.type == "fix"
    assert commit.description == "tippfehler in fehlermeldung"


def test_breaking_change_marker_im_subject():
    commit = parse_line("e5f6a7b|Anna Beispiel|feat: neues schema BREAKING CHANGE: alte api entfernt")
    assert commit is not None
    assert commit.breaking is True


def test_unbekannter_typ_wird_verworfen():
    assert parse_line("f6a7b8c|Ben Muster|wip: irgendwas halbfertiges") is None


def test_merge_commit_wird_verworfen():
    assert parse_line("a7b8c9d|Bot|Merge pull request #7 from team/feature-x") is None


def test_kaputte_zeile_wird_verworfen():
    assert parse_line("nur-ein-feld") is None


def test_parse_lines_ueberspringt_leere_und_ungueltige_zeilen():
    text = "\n".join([
        "a1b2c3d|Anna Beispiel|feat: eins",
        "",
        "a7b8c9d|Bot|Merge pull request #3 from x/y",
        "b2c3d4e|Ben Muster|fix: zwei",
    ])
    commits = parse_lines(text)
    assert [c.description for c in commits] == ["eins", "zwei"]
