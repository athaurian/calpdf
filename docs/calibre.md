# Calibre plugin

Switching out of Calibre to a terminal just to swap a cover or fix a bookmark tree is tedious. [`calibre-calpdf`](https://github.com/athaurian/calibre-calpdf) wraps `calpdf` in a Calibre dialog so you can run the same operations directly on the selected book in your library.

<figure class="screenshot">
  <img src="https://raw.githubusercontent.com/athaurian/calibre-calpdf/main/docs/screenshots/contents.png" alt="The CalPDF dialog on the Contents tab, showing a book's bookmarks as a tree.">
  <figcaption>The Contents tab shows the selected book's bookmarks as a tree.</figcaption>
</figure>

## Tab to CLI mapping

| Plugin tab   | Equivalent `calpdf` command                                                                         |
| :----------- | :-------------------------------------------------------------------------------------------------- |
| **Info**     | [`calpdf info`](commands/info.md)                                                                   |
| **Cover**    | [`calpdf replace-cover`](commands/replace-cover.md) and [`calpdf set-cover`](commands/set-cover.md) |
| **Contents** | [`calpdf export-toc`](commands/export-toc.md) and [`calpdf apply-toc`](commands/apply-toc.md)       |
| **Optimize** | [`calpdf optimize`](commands/optimize.md)                                                           |
| **Backup**   | [`calpdf restore`](commands/restore.md)                                                             |

<figure class="screenshot">
  <img src="https://raw.githubusercontent.com/athaurian/calibre-calpdf/main/docs/screenshots/info.png" alt="The CalPDF dialog on the Info tab, showing pages, page size, file size, version, and backup status.">
  <figcaption>The Info tab only reads the PDF and never writes to it.</figcaption>
</figure>

<figure class="screenshot">
  <img src="https://raw.githubusercontent.com/athaurian/calibre-calpdf/main/docs/screenshots/cover.png" alt="The CalPDF dialog on the Cover tab, with an image file selected and placement options.">
  <figcaption>The Cover tab shows a preview of the image before it replaces the first page or adds a new cover page.</figcaption>
</figure>

Both the plugin and the CLI share the same `book.pdf.bak` file; see [Backup behavior](reference/backup-behavior.md) for how `.bak` baselines work.

## Python environment requirement

The plugin imports `calpdf` inside Calibre's Python process:

- **Do not use `uv tool install` for plugin setups**: `uv tool install` places `calpdf` in an isolated virtual environment that Calibre cannot see. Install `calpdf` into the Python environment Calibre runs under (for example, via `calpdf-git` on Arch Linux).
- **Linux only**: Windows and macOS Calibre builds bundle an isolated Python runtime without a documented way to install third-party libraries into it.

For build, installation, and development instructions, see the [`calibre-calpdf` repository](https://github.com/athaurian/calibre-calpdf).
