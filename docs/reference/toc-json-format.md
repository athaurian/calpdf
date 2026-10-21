# The ToC JSON format

A ToC file is a list of entries, and each entry has a `title`, a `pageNumber`, and a `children` list. The following sample shows the format:

```json
[
  {
    "title": "Chapter 1",
    "pageNumber": 1,
    "children": [
      {
        "title": "Section 1.1",
        "pageNumber": 3,
        "children": []
      }
    ]
  }
]
```

The [`export-toc`](../commands/export-toc.md) command produces files in this format, and the [`apply-toc`](../commands/apply-toc.md) command reads them to replace a PDF's bookmarks. The `export-toc` command writes `null` for a bookmark without a page target, and the `apply-toc` command rejects it, so edit or remove those entries before you apply the file.

For the field-by-field specification, run `calpdf apply-toc --help`.
