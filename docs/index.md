---
template: home.html
---

# calpdf

Hi. This is the documentation I wrote for calpdf, a simple PDF toolkit. If you'd rather read the source code, it's on [GitHub](https://github.com/athaurian/calpdf). I use it alongside Calibre, but it is also a standalone tool that does not require Calibre.

calpdf handles common PDF tasks, including the following:

- Replacing a PDF's cover
- Compressing a PDF when possible
- Editing its table of contents
- Fetching covers from several sources

When calpdf changes a PDF in place, it keeps one `.bak` copy of the original before the first change, and `calpdf restore` puts it back.

I made calpdf because I wanted a small CLI tool for these tasks instead of a full PDF editor. It works on PDFs in a Calibre library or anywhere else on disk.

You can use calpdf inside Calibre through the [Calibre plugin](calibre.md), which provides a graphical interface.

---

<div class="asciinema-demo" role="group" data-asciinema-cast="assets/casts/cover-and-restore.cast" data-asciinema-poster="npt:2" aria-label="Terminal recording of a cover replacement and restore session"></div>
<p class="asciinema-caption">The sample book is small, so the sizes in the recording are small.</p>

---

calpdf is for people who are comfortable using a terminal. Start with [Installation](installation.md).

## Example session

A typical session on one book looks like this:

```bash
# Inspect the PDF first
calpdf info book.pdf

# Download a cover and apply it in one step
calpdf set-cover book.pdf 9780387967875

# Compress the PDF when possible
calpdf optimize book.pdf

# Export the bookmarks, edit the JSON, and apply it
calpdf export-toc book.pdf -o toc.json
calpdf apply-toc book.pdf toc.json
```

## Commands

Each command has its own page with its options and examples:

| Command                                      | Description                                                                                   |
| -------------------------------------------- | --------------------------------------------------------------------------------------------- |
| [`replace-cover`](commands/replace-cover.md) | Replaces the first page of a PDF with a cover image, or inserts the image as a new first page |
| [`dl-cover`](commands/dl-cover.md)           | Downloads a cover image for a book by ASIN, ISBN, or OLID                                     |
| [`set-cover`](commands/set-cover.md)         | Downloads a cover by ASIN, ISBN, or OLID and applies it to a PDF in one step                  |
| [`extract-cover`](commands/extract-cover.md) | Extracts the largest image from a PDF page and saves it as a separate file                    |
| [`optimize`](commands/optimize.md)           | Compresses a PDF with `qpdf` and removes metadata by default                                  |
| [`info`](commands/info.md)                   | Shows a PDF's page count, version, file size, bookmarks, and page sizes                       |
| [`export-toc`](commands/export-toc.md)       | Exports a PDF's bookmarks as a table of contents (ToC) in JSON or a tree view                 |
| [`apply-toc`](commands/apply-toc.md)         | Replaces the bookmarks of a PDF with the table of contents from a JSON file                   |
| [`restore`](commands/restore.md)             | Copies the `.bak` backup back over a PDF and deletes the backup                               |

## Options and reference

| Reference                                       | Description                          |
| ----------------------------------------------- | ------------------------------------ |
| [Global options](global-options.md)             | Options placed before any subcommand |
| [ToC JSON format](reference/toc-json-format.md) | Table of contents JSON format        |
| [Backup behavior](reference/backup-behavior.md) | How backups work                     |

To set up a development environment, see [Development](development.md).
