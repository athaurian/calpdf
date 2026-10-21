# The `export-toc` command

The `export-toc` command reads the bookmarks of a PDF and exports them as a _table of contents (ToC)_. Page numbers are 1-indexed physical page positions.

By default, calpdf prints JSON to standard output, which is convenient for piping to other programs. To write the JSON to a file, use `--output`. To print a human-readable tree instead, use `--format tree`:

```bash
calpdf export-toc book.pdf
calpdf export-toc book.pdf -o toc.json
calpdf export-toc book.pdf --format tree
```

With `--format tree`, calpdf prints the tree to the terminal, and the `--output` option has no effect. calpdf prints a warning if you pass it anyway.

The JSON output matches the format described in [The ToC JSON format](../reference/toc-json-format.md). A bookmark without a page target gets a `pageNumber` of `null`. The [`apply-toc`](apply-toc.md) command rejects `null`, so edit or remove those entries before you apply the file.

## A book with no bookmarks

A scanned book often arrives with no bookmarks at all, and the export comes back as an empty list. Write the entries into the file with any text editor, then apply it with [`apply-toc`](apply-toc.md):

```bash
calpdf export-toc book.pdf -o toc.json
calpdf apply-toc book.pdf toc.json
```
