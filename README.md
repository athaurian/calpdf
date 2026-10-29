<div align="center">
<img src="docs/favicon.svg" alt="calpdf monogram" width="128">

# calpdf

</div>

Hi. This is calpdf, a simple PDF toolkit that I use alongside Calibre. It handles the small jobs that come up with PDFs, such as replacing a cover, reducing its file size, and editing its table of contents. It works on PDFs in a Calibre library or anywhere else on disk.

When calpdf changes a PDF in place, it keeps one `.bak` copy of the original before the first change, and `calpdf restore` puts it back.

You can run the same jobs inside Calibre through the [Calibre plugin](docs/calibre.md), which gives you a friendlier interface.

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

For requirements and install steps, see [Installation](docs/installation.md).

## Documentation

For the full documentation, see [calpdf documentation](docs/index.md). It covers [global options](docs/global-options.md), a page for each command, and [the ToC JSON format](docs/reference/toc-json-format.md).

For development setup, see [`docs/development.md`](docs/development.md).
