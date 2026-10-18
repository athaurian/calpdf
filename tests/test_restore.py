"""Tests for the restore command."""

from pathlib import Path

from typer.testing import CliRunner

from calpdf.cli import app

runner = CliRunner()


class TestRestoreCLI:
    def test_restores_pdf_and_removes_backup(self, tmp_path: Path):
        pdf = tmp_path / "book.pdf"
        bak = tmp_path / "book.pdf.bak"
        original = b"original bytes"
        pdf.write_bytes(b"modified contents")
        bak.write_bytes(original)

        result = runner.invoke(app, ["restore", str(pdf)])

        assert result.exit_code == 0, result.output
        assert pdf.read_bytes() == original
        assert not bak.exists()
        compact = " ".join(result.output.split())
        assert "Success: Restored" in compact

    def test_takes_bak_path(self, tmp_path: Path):
        pdf = tmp_path / "book.pdf"
        bak = tmp_path / "book.pdf.bak"
        pdf.write_bytes(b"modified")
        bak.write_bytes(b"original")

        result = runner.invoke(app, ["restore", str(bak)])

        assert result.exit_code == 0, result.output
        assert pdf.read_bytes() == b"original"
        assert not bak.exists()

    def test_missing_backup(self, tmp_path: Path):
        result = runner.invoke(app, ["restore", str(tmp_path / "book.pdf")])
        assert result.exit_code == 1
        assert "error:" in result.output.lower()
        assert "backup" in result.output.lower()

    def test_quiet_suppresses_output(self, tmp_path: Path):
        pdf = tmp_path / "book.pdf"
        pdf.write_bytes(b"modified")
        pdf.with_name("book.pdf.bak").write_bytes(b"original")

        result = runner.invoke(app, ["--quiet", "restore", str(pdf)])

        assert result.exit_code == 0
        assert "Success" not in result.output
