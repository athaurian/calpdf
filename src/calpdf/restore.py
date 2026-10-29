"""Restore a PDF from the backup that in-place commands keep."""

import shutil
from pathlib import Path

import typer

from calpdf import output
from calpdf.common import AppError, message, normalize_paths


def restore_backup(input_pdf: Path) -> tuple[Path, Path]:
    """Copy the backup over the PDF, delete it, and return both paths."""
    out_file, backup_file = normalize_paths(input_pdf)
    if not backup_file.is_file():
        raise AppError(f"No backup found at '{backup_file}'.")
    try:
        shutil.copy2(backup_file, out_file)
    except Exception as exc:
        raise AppError(
            f"Could not restore '{out_file}' from '{backup_file}': {message(exc)}"
        ) from exc
    backup_file.unlink()
    return out_file, backup_file


def main(
    input_pdf: Path = typer.Argument(
        ...,
        help="Path to the PDF to restore, or to its '.bak' file",
    ),
) -> None:
    """Restore a PDF from its backup, then delete the backup."""
    try:
        out_file, backup_file = restore_backup(input_pdf)
        output.success(f"Success: Restored '{out_file}' from '{backup_file}'.")
    except typer.Exit:
        raise
    except AppError as exc:
        output.error(str(exc))
        raise typer.Exit(1) from None
    except Exception as exc:
        output.error(message(exc))
        raise typer.Exit(1) from None
