# Backup behavior

Commands that modify a PDF in place ([`replace-cover`](../commands/replace-cover.md), [`set-cover`](../commands/set-cover.md), [`apply-toc`](../commands/apply-toc.md), and [`optimize`](../commands/optimize.md)) keep a backup of the original file with a `.bak` suffix. A command that writes to a different file with `--output` leaves the input untouched, so it keeps no backup. To restore the original, run [`restore`](../commands/restore.md):

```bash
calpdf restore book.pdf
```

The backup is created once, before the first change. Later changes leave it unchanged, so the backup always holds the version from before that first change. To start a fresh backup, remove the `.bak` file and run the command again.

A command reads the backup as its source, so its output is based on the backup. When the PDF is newer than the backup, because you edited it or ran another command, calpdf prints a warning before it discards the newer content.

For a summary, run `calpdf --help`.
