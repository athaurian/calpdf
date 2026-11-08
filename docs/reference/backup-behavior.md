# Backup behavior

Commands that modify a PDF in place ([`replace-cover`](../commands/replace-cover.md), [`set-cover`](../commands/set-cover.md), [`apply-toc`](../commands/apply-toc.md), and [`optimize`](../commands/optimize.md)) keep a backup of the original file with a `.bak` suffix. A command that writes to a different file with `--output` leaves the input untouched, so it keeps no backup. To restore the original, run [`restore`](../commands/restore.md):

```bash
calpdf restore book.pdf
```

The backup is created once, before the first change. Later changes leave it unchanged, so the backup always holds the version from before that first change. To start a fresh backup, remove the `.bak` file and run the command again.

An in-place command reads the backup as its source, so its output is based on the backup. When the PDF's modification time is newer than the backup's, calpdf prints a warning because the command bases its output on the backup and discards the newer PDF content.

For a summary, run `calpdf --help`.
