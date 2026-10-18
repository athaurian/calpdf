"""Tests for calpdf.output."""

from calpdf import output


class TestQuietMode:
    def test_suppresses_info(self, capsys):
        output.configure(quiet=True)
        output.info("hello")
        captured = capsys.readouterr()
        assert "hello" not in captured.out

    def test_suppresses_success(self, capsys):
        output.configure(quiet=True)
        output.success("done")
        captured = capsys.readouterr()
        assert "done" not in captured.out

    def test_keeps_warnings_and_errors(self, capsys):
        output.configure(quiet=True)
        output.warning("careful")
        output.error("boom")
        captured = capsys.readouterr()
        assert "careful" in captured.err
        assert "boom" in captured.err


class TestErrorAndWarningGoToStderr:
    def test_error_writes_to_stderr(self, capsys):
        output.error("boom")
        captured = capsys.readouterr()
        assert "boom" in captured.err
        assert "boom" not in captured.out

    def test_warning_writes_to_stderr(self, capsys):
        output.warning("careful")
        captured = capsys.readouterr()
        assert "careful" in captured.err
        assert "careful" not in captured.out


class TestFormatSize:
    def test_bytes(self):
        assert output.format_size(1023) == "1023 bytes"

    def test_kilobytes(self):
        assert output.format_size(1024) == "1.0 KB"
        assert output.format_size(435913) == "425.7 KB"

    def test_megabytes(self):
        assert output.format_size(1024 * 1024) == "1.0 MB"
        assert output.format_size(2647736) == "2.5 MB"


class TestFormatSizeChange:
    def test_unchanged(self):
        assert output.format_size_change(1024, 1024) == "1.0 KB, unchanged."

    def test_smaller(self):
        assert (
            output.format_size_change(2647736, 435913)
            == "2.5 MB to 425.7 KB, 84% smaller."
        )

    def test_larger(self):
        assert (
            output.format_size_change(77060, 77787)
            == "75.3 KB to 76.0 KB, 0.9% larger."
        )

    def test_below_ten_percent_keeps_a_decimal(self):
        assert output.format_size_change(1000, 950) == (
            "1000 bytes to 950 bytes, 5.0% smaller."
        )

    def test_tiny_change_rounds_to_a_floor(self):
        # The two labels round to the same number, so the percentage has to
        # carry the change on its own.
        assert (
            output.format_size_change(1000000, 999999)
            == "976.6 KB to 976.6 KB, less than 0.1% smaller."
        )

    def test_empty_before(self):
        assert output.format_size_change(0, 1024) == "0 bytes to 1.0 KB, larger."


class TestRenderTocTree:
    def test_renders_entries(self, capsys):
        output.render_toc_tree(
            [
                {"title": "Ch 1", "pageNumber": 1, "children": []},
                {
                    "title": "Ch 2",
                    "pageNumber": 3,
                    "children": [{"title": "Sec 2.1", "pageNumber": 4, "children": []}],
                },
            ]
        )
        captured = capsys.readouterr()
        assert "Ch 1" in captured.out
        assert "Ch 2" in captured.out
        assert "Sec 2.1" in captured.out
        assert "(p. 1)" in captured.out

    def test_empty_tree_prints_note(self, capsys):
        output.render_toc_tree([])
        captured = capsys.readouterr()
        assert "no bookmarks" in captured.out.lower()
