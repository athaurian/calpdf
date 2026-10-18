# Backup behavior

Commands that modify a PDF in place ([`replace-cover`](../commands/replace-cover.md), [`set-cover`](../commands/set-cover.md), [`apply-toc`](../commands/apply-toc.md), and [`optimize`](../commands/optimize.md)) keep a backup of the original file with a `.bak` suffix. To restore the original, copy the `.bak` file back over the PDF:

```bash
cp book.pdf.bak book.pdf
```

The backup is created once, before the first change. Later changes leave it as it is. The file always holds the version from before that first change. To start a fresh backup, remove the `.bak` file and run the command again.

For the full behavior, run `calpdf --help`.
