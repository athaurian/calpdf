import shutil
from unittest.mock import patch, MagicMock
from pathlib import Path
from typer.testing import CliRunner

from calpdf.cli import app

runner = CliRunner()


def _fake_qpdf_write(
    source: Path | None = None,
    *,
    payload: bytes | None = None,
    returncode: int = 0,
    stderr: str = "",
):
    """Stand in for ``subprocess.run``, writing the output path.

    The output is a copy of *source*, or *payload* when given. qpdf writes
    the output before the command moves it into place, so tests fake the
    write through the command's last argument.
    """

    def run(cmd, **kwargs):
        if payload is not None:
            Path(cmd[-1]).write_bytes(payload)
        else:
            assert source is not None
            shutil.copy2(source, cmd[-1])
        result = MagicMock()
        result.returncode = returncode
        result.stderr = stderr
        return result

    return run


class TestOptimizeCLI:
    def test_qpdf_not_found(self, sample_pdf: Path, tmp_path: Path):
        with patch("calpdf.optimize.shutil.which", return_value=None):
            result = runner.invoke(
                app,
                ["optimize", str(sample_pdf), "-o", str(tmp_path / "out.pdf")],
            )
            assert result.exit_code == 1
            # Typer's CliRunner mixes stderr into result.output
            assert "qpdf" in result.output.lower()

    def test_success(self, sample_pdf: Path, tmp_path: Path):
        out = tmp_path / "out.pdf"
        with (
            patch("calpdf.optimize.shutil.which", return_value="/usr/bin/qpdf"),
            patch(
                "calpdf.optimize.subprocess.run",
                side_effect=_fake_qpdf_write(sample_pdf),
            ),
        ):
            result = runner.invoke(app, ["optimize", str(sample_pdf), "-o", str(out)])
            assert result.exit_code == 0
            assert any(
                line.lower().startswith("success:")
                for line in result.output.splitlines()
            )

    def test_qpdf_failure_without_force(self, sample_pdf: Path, tmp_path: Path):
        out = tmp_path / "out.pdf"
        mock_result = MagicMock()
        mock_result.returncode = 2
        mock_result.stderr = "something broke"

        with (
            patch("calpdf.optimize.shutil.which", return_value="/usr/bin/qpdf"),
            patch("calpdf.optimize.subprocess.run", return_value=mock_result),
        ):
            result = runner.invoke(app, ["optimize", str(sample_pdf), "-o", str(out)])
            assert result.exit_code == 1
            # The reason qpdf failed must reach the user.
            assert "something broke" in result.output

    def test_missing_input(self, tmp_path: Path):
        result = runner.invoke(
            app,
            ["optimize", str(tmp_path / "nope.pdf")],
        )
        assert result.exit_code == 1
        assert "error:" in result.output.lower()

    def test_force_fails_when_qpdf_produces_no_output(
        self, sample_pdf: Path, tmp_path: Path
    ):
        out = tmp_path / "out.pdf"
        mock_result = MagicMock()
        mock_result.returncode = 2
        mock_result.stderr = "something broke"
        with (
            patch("calpdf.optimize.shutil.which", return_value="/usr/bin/qpdf"),
            patch("calpdf.optimize.subprocess.run", return_value=mock_result),
        ):
            result = runner.invoke(
                app,
                ["optimize", str(sample_pdf), "-o", str(out), "--force"],
            )
        assert result.exit_code == 1
        assert "no output" in result.output.lower()

    def test_force_succeeds_when_output_file_exists(
        self, sample_pdf: Path, tmp_path: Path
    ):
        out = tmp_path / "out.pdf"
        with (
            patch("calpdf.optimize.shutil.which", return_value="/usr/bin/qpdf"),
            patch(
                "calpdf.optimize.subprocess.run",
                side_effect=_fake_qpdf_write(
                    sample_pdf, returncode=2, stderr="something broke"
                ),
            ),
        ):
            result = runner.invoke(
                app,
                ["optimize", str(sample_pdf), "-o", str(out), "--force"],
            )
        assert result.exit_code == 0
        assert "warning" in result.output.lower()
        # The reason qpdf failed must reach the user.
        assert "something broke" in result.output

    def test_qpdf_exit_3_warns_but_succeeds(self, sample_pdf: Path, tmp_path: Path):
        out = tmp_path / "out.pdf"
        with (
            patch("calpdf.optimize.shutil.which", return_value="/usr/bin/qpdf"),
            patch(
                "calpdf.optimize.subprocess.run",
                side_effect=_fake_qpdf_write(sample_pdf, returncode=3),
            ),
        ):
            result = runner.invoke(app, ["optimize", str(sample_pdf), "-o", str(out)])
        assert result.exit_code == 0
        assert "warnings" in result.output.lower()

    def test_exit_3_relays_qpdf_warnings(self, sample_pdf: Path, tmp_path: Path):
        out = tmp_path / "out.pdf"
        with (
            patch("calpdf.optimize.shutil.which", return_value="/usr/bin/qpdf"),
            patch(
                "calpdf.optimize.subprocess.run",
                side_effect=_fake_qpdf_write(
                    sample_pdf, returncode=3, stderr="WARNING: repaired input"
                ),
            ),
        ):
            result = runner.invoke(app, ["optimize", str(sample_pdf), "-o", str(out)])
        assert result.exit_code == 0
        assert "WARNING: repaired input" in result.output

    def test_keep_metadata_drops_strip_flags(self, sample_pdf: Path, tmp_path: Path):
        out = tmp_path / "out.pdf"
        with (
            patch("calpdf.optimize.shutil.which", return_value="/usr/bin/qpdf"),
            patch(
                "calpdf.optimize.subprocess.run",
                side_effect=_fake_qpdf_write(sample_pdf),
            ) as mock_run,
        ):
            result = runner.invoke(
                app,
                ["optimize", str(sample_pdf), "-o", str(out), "--keep-metadata"],
            )
        assert result.exit_code == 0
        cmd = mock_run.call_args[0][0]
        assert "--remove-info" not in cmd
        assert "--remove-metadata" not in cmd

    def test_strip_color_profiles_runs_native_then_qpdf(
        self, sample_pdf: Path, tmp_path: Path
    ):
        out = tmp_path / "out.pdf"
        with (
            patch("calpdf.optimize.shutil.which", return_value="/usr/bin/qpdf"),
            patch(
                "calpdf.optimize.subprocess.run",
                side_effect=_fake_qpdf_write(sample_pdf),
            ) as mock_run,
            patch("calpdf.optimize.strip_color_profiles") as mock_strip,
        ):
            result = runner.invoke(
                app,
                [
                    "optimize",
                    str(sample_pdf),
                    "-o",
                    str(out),
                    "--strip-color-profiles",
                ],
            )
        assert result.exit_code == 0, result.stdout
        mock_strip.assert_called_once()
        assert mock_run.call_count == 1
        qpdf_cmd = mock_run.call_args[0][0]
        assert "--linearize" in qpdf_cmd

    def test_strip_color_profiles_removes_output_intents(self, tmp_path: Path):
        import pikepdf

        src = tmp_path / "with_icc.pdf"
        pdf = pikepdf.Pdf.new()
        pdf.add_blank_page(page_size=(612, 792))
        icc = pdf.make_stream(b"dummy icc")
        icc["/N"] = 3
        icc["/Alternate"] = pikepdf.Name("/DeviceRGB")
        intent = pikepdf.Dictionary(
            {
                "/Type": pikepdf.Name("/OutputIntent"),
                "/S": pikepdf.Name("/GTS_PDFX"),
                "/OutputConditionIdentifier": "sRGB",
                "/DestOutputProfile": icc,
            }
        )
        pdf.Root["/OutputIntents"] = pikepdf.Array([intent])
        pdf.save(src)

        dst = tmp_path / "stripped.pdf"
        from calpdf.optimize import strip_color_profiles

        strip_color_profiles(src, dst)
        with pikepdf.open(dst) as out:
            assert "/OutputIntents" not in out.Root
        # surgical: only 1 object removed (the intent), Producer preserved
        with pikepdf.open(src) as a, pikepdf.open(dst) as b:
            assert len(list(b.objects)) == len(list(a.objects)) - 1


class TestOptimizeSizeReport:
    """The command reports how the file size changed."""

    def _invoke(self, args: list[str], written_size: int):
        with (
            patch("calpdf.optimize.shutil.which", return_value="/usr/bin/qpdf"),
            patch(
                "calpdf.optimize.subprocess.run",
                side_effect=_fake_qpdf_write(payload=b"x" * written_size),
            ),
        ):
            return runner.invoke(app, args)

    def test_reports_a_smaller_file(self, tmp_path: Path):
        src = tmp_path / "big.pdf"
        src.write_bytes(b"y" * 4096)
        out = tmp_path / "out.pdf"

        result = self._invoke(["optimize", str(src), "-o", str(out)], 1024)

        assert result.exit_code == 0
        assert "Size: 4.0 KB to 1.0 KB, 75% smaller." in result.output

    def test_in_place_compares_against_the_input_file(self, tmp_path: Path):
        src = tmp_path / "book.pdf"
        src.write_bytes(b"y" * 2048)
        # qpdf reads the leftover backup, but the report describes the input
        # file, which is the one the user sees change.
        src.with_name(src.name + ".bak").write_bytes(b"y" * 4096)

        result = self._invoke(["optimize", str(src)], 1024)

        assert result.exit_code == 0
        assert "Size: 2.0 KB to 1.0 KB, 50% smaller." in result.output

    def test_quiet_suppresses_the_report(self, tmp_path: Path):
        src = tmp_path / "big.pdf"
        src.write_bytes(b"y" * 4096)
        out = tmp_path / "out.pdf"

        result = self._invoke(["--quiet", "optimize", str(src), "-o", str(out)], 1024)

        assert result.exit_code == 0
        assert "Size:" not in result.output
