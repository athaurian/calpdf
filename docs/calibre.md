# Calibre plugin

calpdf is mainly a command-line tool. I work from a terminal most of the time,
but switching out of the library to change a cover is tedious.
[CalPDF](https://github.com/athaurian/calibre-calpdf) is a graphical interface
for the same program.

<figure class="screenshot">
  <img src="https://raw.githubusercontent.com/athaurian/calibre-calpdf/main/docs/screenshots/contents.png" alt="The CalPDF dialog on the Contents tab, showing a book's bookmarks as a tree.">
  <figcaption>The Contents tab works on the selected book's outline, the PDF structure that stores bookmarks.</figcaption>
</figure>

## Direct integration

The plugin uses calpdf directly, so the backup rules, the ToC format, and the way
`qpdf` runs all match the CLI.

Calibre imports calpdf from the Python installation it runs on, so installing
calpdf using `uv tool install` does not help. On Arch, you can install
`calpdf-git` from my [Forge repository](https://github.com/athaurian/forge), and
it goes into the system Python that Calibre uses. Elsewhere, install calpdf into
the same Python installation. When the dialog opens, the plugin checks the
calpdf version and reports a mismatch instead of leaving you with a broken
dialog.

The plugin needs calpdf 0.2 or newer, Calibre 6 or newer, and `qpdf` on `PATH`
for the Optimize tab.

## Tabs

| Tab      | Action                                                                                                                     | calpdf command                                                                     |
| -------- | -------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Info     | Shows the page count, page size, file size, PDF version, bookmark count, and whether a backup exists.                      | [`info`](commands/info.md)                                                         |
| Cover    | Downloads a cover by ASIN or ISBN, or uses an image file. You can also replace the first page or prepend a new cover page. | [`set-cover`](commands/set-cover.md), [`replace-cover`](commands/replace-cover.md) |
| Contents | Edits the outline as a tree and imports or exports the ToC JSON.                                                           | [`export-toc`](commands/export-toc.md), [`apply-toc`](commands/apply-toc.md)       |
| Optimize | Runs `qpdf`, with options to strip color profiles and keep the document metadata.                                          | [`optimize`](commands/optimize.md)                                                 |
| Backup   | Puts the `.bak` copy back.                                                                                                 | [`restore`](commands/restore.md)                                                   |

<figure class="screenshot">
  <img src="https://raw.githubusercontent.com/athaurian/calibre-calpdf/main/docs/screenshots/info.png" alt="The CalPDF dialog on the Info tab, showing pages, page size, file size, version, and backup status.">
  <figcaption>The Info tab only reads the PDF and never writes to it.</figcaption>
</figure>

<figure class="screenshot">
  <img src="https://raw.githubusercontent.com/athaurian/calibre-calpdf/main/docs/screenshots/cover.png" alt="The CalPDF dialog on the Cover tab, with an image file selected and placement options.">
  <figcaption>The Cover tab shows a preview of the image before it replaces the first page or adds a new cover page.</figcaption>
</figure>

## Backup behavior

The plugin does not keep a version history. It uses the same `.bak` backup as
the CLI. The Backup tab puts that copy back and deletes it, the same way
[`restore`](commands/restore.md) does. If you close the dialog without applying
anything, the PDF is untouched.

## Install

The plugin is at
[athaurian/calibre-calpdf](https://github.com/athaurian/calibre-calpdf). The
README has the full build and install steps. To build and install from a
checkout, run:

```bash
git clone https://github.com/athaurian/calibre-calpdf.git
cd calibre-calpdf
make build
calibre-customize -a dist/calpdf.zip
```

Restart Calibre, then add the **CalPDF** button from **Preferences > Interface >
Toolbars & menus**.

I use CalPDF on Linux. On Windows and macOS, Calibre bundles its own Python, and
I have not covered how to install calpdf into it yet.
