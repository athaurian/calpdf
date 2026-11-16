# `extract-cover`

Extracts the largest embedded raster image from a PDF page (page 1 by default).

```bash
# Saves to book_cover.jpg or book_cover.png
calpdf extract-cover book.pdf

# Extract from page 2 to a custom path
calpdf extract-cover book.pdf --page 2 -o cover.png
```

## Limitations

`extract-cover` selects the embedded image with the largest pixel area on the target page. If a cover is drawn entirely with vector paths, text, or tiled image strips rather than a single raster image, `extract-cover` will either find no image or extract only the largest fragment.

## Options

| Option                | Default                 | Description                                                                                                                               |
| :-------------------- | :---------------------- | :---------------------------------------------------------------------------------------------------------------------------------------- |
| `-o`, `--output PATH` | `BOOK_STEM_cover.<ext>` | Output file path. Unless `--raw` is set, the image is converted to match the `.jpg`/`.jpeg` or `.png` extension of `PATH`.                |
| `--page INTEGER`      | `1`                     | 1-indexed page number to inspect.                                                                                                         |
| `--raw`               | Off                     | Write the embedded image stream bytes straight to disk without re-encoding or checking that the file extension matches the stream format. |

## Using the extracted image in Calibre

If a PDF has a good cover on page 1 that is missing from Calibre's library metadata:

1. Run `calpdf extract-cover book.pdf`.
2. Open **Edit metadata** for the book in Calibre.
3. Drag `book_cover.jpg` (or `.png`) onto the cover preview pane.
