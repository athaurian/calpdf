# `restore`

Reverts an in-place edit by copying `book.pdf.bak` back over `book.pdf` and deleting `book.pdf.bak`.

```bash
calpdf restore book.pdf
```

You can pass either the PDF path (`book.pdf`) or the backup path (`book.pdf.bak`). For details on when `.bak` files are created and reused, see [Backup behavior](../reference/backup-behavior.md).
