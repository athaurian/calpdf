# The `optimize` command

The `optimize` command uses `qpdf` to compress a PDF. By default, it also
removes metadata such as the title and author. It also removes the document
structure tree, which holds the accessibility tags. `--keep-metadata` doesn't
preserve the structure tree.

The result depends on what is inside the file:

- Scanned books and comics often shrink by a large percentage.
- Files that the publisher already compressed may not shrink.
- Files that are already optimized can grow slightly because `qpdf` adds
  linearization data.

When the command finishes, it reports how the size changed, as in
`Size: 2.5 MB to 425.7 KB, 84% smaller.` If the size doesn't change, the report
ends with `unchanged`.

The following examples show common ways to use it:

```bash
calpdf optimize book.pdf
calpdf optimize book.pdf --keep-metadata
calpdf optimize book.pdf --strip-color-profiles
calpdf optimize book.pdf -o optimized.pdf
```

By default, the command updates the PDF in place and keeps a backup. The options
in the examples have these effects:

| Option                   | Effect                                                                         |
| ------------------------ | ------------------------------------------------------------------------------ |
| `--keep-metadata`        | Keeps the metadata.                                                            |
| `--strip-color-profiles` | Removes ICC color profiles (document OutputIntents and image ICCBased spaces). |
| `--output`, `-o`         | Writes the result to a new file.                                               |

For more information about backups, see
[Backup behavior](../reference/backup-behavior.md).

If `qpdf` exits with a nonzero code other than 3, calpdf stops and reports an
error. Use `--force` to continue. If `qpdf` exits with code 3, it reported
warnings; calpdf prints those warnings and continues.

The `optimize` command requires `qpdf`. For more information, see
[External dependencies](../installation.md#external-dependencies).
