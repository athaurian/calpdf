---
template: home.html
---

# calpdf

Hi. This is a simple PDF toolkit. I use it alongside Calibre, but it really is just a standalone tool I made for myself.

calpdf handles the small jobs that usually come up when dealing with PDFs, such as replacing a PDF's cover, reducing its file size when possible, and editing its table of contents. calpdf can fetch covers from various sources too, as a bonus.

When calpdf changes a PDF in place, it keeps a `.bak` backup of the original, so it's unlikely that you'll experience severe data loss when using the tool.

I made calpdf because I wanted a small CLI tool for these jobs, not another bloated PDF editor. It works on PDFs in a Calibre library or anywhere else on disk.

---

<div class="asciinema-demo" role="group" data-asciinema-cast="assets/casts/cover-and-restore.cast" data-asciinema-poster="npt:2" aria-label="Terminal recording of the cover and restore flow"></div>
<p class="asciinema-caption">The sample book is small, so the numbers are small too.</p>

---

This documentation is for people who are comfortable using a terminal. Start with [Installation](installation.md).

## Commands

Each command has its own page with its options and examples:

- The [`replace-cover`](commands/replace-cover.md) command replaces the first page of a PDF with a cover image, or inserts the image as a new first page.
- The [`dl-cover`](commands/dl-cover.md) command downloads a cover image for a book by ASIN or ISBN.
- The [`set-cover`](commands/set-cover.md) command downloads a cover by ASIN or ISBN and applies it to a PDF in one step.
- The [`extract-cover`](commands/extract-cover.md) command extracts the cover image from a PDF page and saves it as a separate file.
- The [`optimize`](commands/optimize.md) command tries to make a PDF smaller with `qpdf`.
- The [`info`](commands/info.md) command shows information about a PDF, such as its page count, file size, bookmarks, and page sizes.
- The [`export-toc`](commands/export-toc.md) command exports the bookmarks, or _table of contents (ToC)_, of a PDF.
- The [`apply-toc`](commands/apply-toc.md) command replaces the bookmarks of a PDF with the table of contents from a JSON file.
- The [`restore`](commands/restore.md) command copies the `.bak` backup back over a PDF and deletes the backup.

## Options and reference

You can place a few options before any subcommand. For the list, see [Global options](global-options.md).

The rest of the reference covers [the ToC JSON format](reference/toc-json-format.md) and [backup behavior](reference/backup-behavior.md).

To set up a development environment, see [Development](development.md).
