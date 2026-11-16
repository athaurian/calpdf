# `apply-toc`

Replaces the entire bookmark tree of a PDF with the hierarchy defined in a ToC JSON file.

```bash
calpdf apply-toc book.pdf toc.json
calpdf apply-toc book.pdf toc.json -o book-toc.pdf
```

If `-o` / `--output` is omitted, `book.pdf` is modified in place (see [Backup behavior](../reference/backup-behavior.md)).

## Validation and page labels

Before modifying the PDF, `apply-toc` validates every entry against the [ToC JSON format](../reference/toc-json-format.md):

- `title` must be a non-empty string.
- `pageNumber` must be an integer between `1` and the document's physical page count. Entries exported with `"pageNumber": null` are rejected until you assign a valid page number.
- `children` must be a list of nested bookmark entries.

Replacing bookmarks only updates the outline tree; existing custom page labels in the PDF (such as Roman numerals `i–xii` for front matter) are preserved intact.

## Demo

<div class="asciinema-demo" role="group" data-asciinema-cast="../../assets/casts/toc-round-trip.cast" data-asciinema-poster="npt:2" aria-label="Terminal recording of a table of contents round trip"></div>
<p class="asciinema-caption">The sample book is small, so the numbers are small too.</p>
