from relnotes.cli import main


def test_cli_schreibt_markdown_datei(tmp_path):
    src = tmp_path / "commits.txt"
    src.write_text(
        "a1b2c3d|Anna Beispiel|feat: eins\n"
        "a7b8c9d|Bot|Merge pull request #3 from x/y\n",
        encoding="utf-8",
    )
    out = tmp_path / "NOTES.md"
    exit_code = main(["--input", str(src), "--output", str(out)])
    assert exit_code == 0
    content = out.read_text(encoding="utf-8")
    assert "# Release Notes" in content
    assert "eins" in content


def test_cli_meldet_statistik_auf_stderr(tmp_path, capsys):
    src = tmp_path / "commits.txt"
    src.write_text("a1b2c3d|Anna Beispiel|feat: eins\nkaputt\n", encoding="utf-8")
    main(["--input", str(src), "--output", str(tmp_path / "n.md")])
    captured = capsys.readouterr()
    assert "1 Commits verarbeitet, 1 Zeilen uebersprungen." in captured.err
