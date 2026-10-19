<div align="center">
<img src="docs/favicon.svg" alt="calpdf monogram" width="128">

# calpdf

</div>

Hi. This is a simple PDF toolkit. I use it alongside Calibre, but it really is just a standalone tool I made for myself.

calpdf handles the small jobs that usually come up when dealing with PDFs, such as replacing a PDF's cover, reducing its file size when possible, and editing its table of contents. calpdf can fetch covers from various sources too, as a bonus.

When calpdf changes a PDF in place, it keeps a `.bak` backup of the original, so it's unlikely that you'll experience severe data loss when using the tool.

I made calpdf because I wanted a small CLI tool for these jobs, not another bloated PDF editor. It works on PDFs in a Calibre library or anywhere else on disk.

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
