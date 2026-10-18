# The `restore` command

The `restore` command copies the `.bak` backup back over the PDF and deletes the backup. Use it to undo an in-place edit, such as a bad `apply-toc` or `optimize` run.

```bash
calpdf restore book.pdf
```

The command accepts the PDF or its backup file. After it runs, the PDF holds the original content and the `.bak` file is gone.

For more information about how the backups work, see [Backup behavior](../reference/backup-behavior.md).
