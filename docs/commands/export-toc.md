# The `export-toc` command

The `export-toc` command reads a PDF's bookmarks and exports them as a _table of
contents (ToC)_ in JSON or a tree view. Page numbers are 1-indexed physical page
positions.

By default, calpdf prints JSON to standard output so you can pipe it to another
program. To write the JSON to a file, use `--output`. To print a human-readable
tree instead, use `--format tree`:

```bash
calpdf export-toc book.pdf
calpdf export-toc book.pdf -o toc.json
calpdf export-toc book.pdf --format tree
```

With `--format tree`, calpdf prints the tree to the terminal. `--output` has no
effect, and calpdf prints a warning if you pass it.

The JSON output matches the format described in
[The ToC JSON format](../reference/toc-json-format.md). A bookmark without a
page target gets a `pageNumber` of `null`. The [`apply-toc`](apply-toc.md)
command rejects `null`, so edit or remove those entries before you apply the
file.

## A book with no bookmarks

A scanned book often has no bookmarks, so the export is an empty list. Add the
entries in a text editor, then apply the file with [`apply-toc`](apply-toc.md):

```bash
calpdf export-toc book.pdf -o toc.json
calpdf apply-toc book.pdf toc.json
```
