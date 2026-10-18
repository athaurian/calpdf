<div align="center">
<img src="docs/favicon.svg" alt="calpdf monogram" width="128">

# calpdf

</div>

Hi. This is a simple PDF toolkit to run alongside Calibre.

Calibre organizes your e-book library, but it's the wrong tool for editing an individual PDF. calpdf handles jobs that normally need a PDF editor, like downloading a cover, swapping it in, shrinking a PDF, or rewriting the bookmarks, each as a single command. It edits the PDF file in place and keeps a backup of the original. It works on files in your Calibre library or any other folder.

A typical session on one book looks like this:

```bash
# See what you are starting with
calpdf info book.pdf

# Download a cover and apply it in one step
calpdf set-cover book.pdf 9780387967875

# Make a PDF smaller (hopefully)
calpdf optimize book.pdf

# Pull the bookmarks out, write the entries by hand, and put them back
calpdf export-toc book.pdf -o toc.json
calpdf apply-toc book.pdf toc.json
```

## Installation

For requirements and install steps, see [Installation](https://athaurian.github.io/calpdf/installation/).

## Documentation

For the full documentation, see [calpdf documentation](https://athaurian.github.io/calpdf/). It covers [global options](https://athaurian.github.io/calpdf/global-options/), one page per command, and [the ToC JSON format](https://athaurian.github.io/calpdf/reference/toc-json-format/).

For development setup, see [`docs/development.md`](docs/development.md).
