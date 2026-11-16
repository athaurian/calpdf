# Backup behavior

In-place commands ([`replace-cover`](../commands/replace-cover.md), [`set-cover`](../commands/set-cover.md), [`apply-toc`](../commands/apply-toc.md), and [`optimize`](../commands/optimize.md) when run without `-o` / `--output`) share a single `book.pdf.bak` backup file alongside `book.pdf`. Passing `-o` writes to a new file and never creates or reads a `.bak` file.

## Why `.bak` is used as the input baseline

When you run an in-place command for the first time, `calpdf` copies `book.pdf` to `book.pdf.bak`.

On any later in-place run while `book.pdf.bak` still exists, `calpdf` reads from `book.pdf.bak` as its source rather than the already-modified `book.pdf`. This lets you re-run a command with different settings (for example, testing `--fit match-width` vs `--fit fill` on a cover) without stacking edits on top of an already-altered PDF.

### Chaining different in-place edits

Because every in-place run starts from `book.pdf.bak`, running a second in-place command (or editing `book.pdf` in an external program) while `book.pdf.bak` exists will overwrite the newer `book.pdf` changes with a fresh pass from `.bak`. If `book.pdf` has a newer modification timestamp than `book.pdf.bak`, `calpdf` prints a warning before proceeding.

To chain multiple operations (`set-cover`, then `apply-toc`, then `optimize`):

- **Commit the current state as the new baseline**: Delete `book.pdf.bak` between steps so the next command backs up your updated PDF, or
- **Write to explicit output files**: Pass `-o` to each step.

## Restoring the original PDF

Run [`calpdf restore book.pdf`](../commands/restore.md) (or use the **Backup** tab in the [Calibre plugin](../calibre.md)) to copy `book.pdf.bak` back over `book.pdf` and delete `book.pdf.bak`.
