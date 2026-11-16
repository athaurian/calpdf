---
template: home.html
---

# calpdf

This is the documentation index. If you want an overview instead, see [the project's README.md](https://github.com/athaurian/calpdf/blob/main/README.md).

---

<div class="asciinema-demo" role="group" data-asciinema-cast="assets/casts/cover-and-restore.cast" data-asciinema-poster="npt:2" aria-label="Terminal recording of a cover replacement and restore session"></div>
<p class="asciinema-caption">The sample book is small, so the sizes in the recording are small as well.</p>

---

## Commands

| Command                                      | Description                                                           |
| :------------------------------------------- | :-------------------------------------------------------------------- |
| [`info`](commands/info.md)                   | Inspect page count, dimensions, PDF version, file size, and bookmarks |
| [`replace-cover`](commands/replace-cover.md) | Replace the first page(s) or insert a new cover from a PNG/JPEG       |
| [`dl-cover`](commands/dl-cover.md)           | Download a cover image by ASIN, ISBN, or Open Library ID              |
| [`set-cover`](commands/set-cover.md)         | Download a cover by ID and apply it in one step                       |
| [`extract-cover`](commands/extract-cover.md) | Extract the largest embedded image from a page                        |
| [`export-toc`](commands/export-toc.md)       | Export PDF bookmarks as JSON or an indented tree                      |
| [`apply-toc`](commands/apply-toc.md)         | Replace PDF bookmarks from a JSON file                                |
| [`optimize`](commands/optimize.md)           | Compress and linearize PDFs with `qpdf`                               |
| [`restore`](commands/restore.md)             | Revert an in-place edit from its `.bak` file                          |

## Guides and reference

| Page                                            | Description                                                       |
| :---------------------------------------------- | :---------------------------------------------------------------- |
| [Installation](installation.md)                 | Install with `uv` or from the Arch Linux Forge repository         |
| [Calibre plugin](calibre.md)                    | Use `calpdf` inside Calibre and share the same Python environment |
| [Global options](global-options.md)             | `--quiet`, `--no-color`, `--version`, and shell completion        |
| [ToC JSON format](reference/toc-json-format.md) | Schema and page-numbering rules for `export-toc` and `apply-toc`  |
| [Backup behavior](reference/backup-behavior.md) | How `.bak` files are created, reused as a baseline, and restored  |
| [Development](development.md)                   | Test, lint, and documentation build targets                       |
