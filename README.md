<div align="center">
<img src="docs/favicon.svg" alt="calpdf monogram" width="128">

# calpdf

</div>

Hi. This is a command-line toolkit for sanitizing PDFs. It's also available as a [Calibre plugin](https://github.com/athaurian/calibre-calpdf) if you prefer to use a GUI.

> [!NOTE]
> The name "calpdf" was inspired by Calibre, but calpdf itself is a standalone tool you can use anywhere on disk.

## Commands

| Command         | Purpose                                                                      |
| :-------------- | :--------------------------------------------------------------------------- |
| `info`          | Show page count, dimensions, PDF version, file size, and bookmark count      |
| `dl-cover`      | Download a cover image by ASIN, ISBN, or Open Library ID                     |
| `replace-cover` | Replace the first page(s) or prepend a cover from a local PNG/JPEG           |
| `set-cover`     | Download a cover by ID and apply it to a PDF in one step                     |
| `extract-cover` | Extract the largest image on a page (defaults to page 1)                     |
| `export-toc`    | Export the bookmark tree as JSON or a readable terminal tree                 |
| `apply-toc`     | Replace the PDF bookmark tree from a JSON file                               |
| `optimize`      | Compress streams, linearize, and strip metadata or color profiles via `qpdf` |
| `restore`       | Restore a PDF from its `.bak` backup and remove the backup                   |

## Quick start

```bash
# Inspect the PDF
calpdf info book.pdf

# Download and apply a cover by ISBN, writing to a new file or in place
calpdf set-cover book.pdf 9780387967875 -o book-covered.pdf

# Export bookmarks, edit toc.json, and apply them
calpdf export-toc book.pdf -o toc.json
calpdf apply-toc book.pdf toc.json

# Compress with qpdf
calpdf optimize book.pdf -o book-opt.pdf
```

### In-place backups

When you run an in-place command (`replace-cover`, `set-cover`, `apply-toc`, or `optimize` without `-o`), `calpdf` saves the original file to `book.pdf.bak`.

If `book.pdf.bak` already exists, in-place commands read from `book.pdf.bak` as their input so repeated runs (such as testing different cover fit modes) always start from the untouched original rather than stacking changes.

To chain different edits in place, either write to `-o` or remove `book.pdf.bak` between steps when you are happy with the current state. Run `calpdf restore book.pdf` at any time to revert to `.bak`.

## Documentation

For the full set of guides, see the [documentation index](https://athaurian.github.io/calpdf)

## License

MIT
