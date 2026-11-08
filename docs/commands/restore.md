# The `restore` command

The `restore` command copies the `.bak` backup back over the PDF and deletes the
backup. Use it to undo an in-place edit, such as a bad run of `replace-cover`,
`set-cover`, `apply-toc`, or `optimize`.

```bash
calpdf restore book.pdf
```

The command accepts the PDF or its backup file.

For more information about how the backups work, see
[Backup behavior](../reference/backup-behavior.md).
