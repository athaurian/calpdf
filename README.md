<div align="center">
<img src="docs/favicon.svg" alt="calpdf monogram" width="128">

# calpdf

</div>

Hi. This is calpdf, a simple PDF toolkit that I use alongside Calibre. It
handles common PDF tasks: replacing a cover, compressing a PDF when possible,
and editing its table of contents. It works on PDFs in a Calibre library or
anywhere else on disk.

When calpdf changes a PDF in place, it keeps one `.bak` copy of the original
before the first change, and `calpdf restore` puts it back.

Inside Calibre, the [Calibre plugin](docs/calibre.md) does the same work with a
graphical interface.

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

## Install

For requirements and install steps, see
[the installation page](docs/installation.md).

## Documentation

For the full documentation, see the [calpdf documentation](docs/index.md). It
covers [global options](docs/global-options.md), a page for each command, and
[the ToC JSON format](docs/reference/toc-json-format.md).

For development setup, see [`docs/development.md`](docs/development.md).

## License

Released under the MIT license. See [LICENSE](LICENSE) for the full text.
