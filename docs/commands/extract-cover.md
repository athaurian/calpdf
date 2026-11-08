# The `extract-cover` command

The `extract-cover` command extracts the largest image from a PDF page and saves it as a separate file. Use it to save a cover image from a PDF so you can reuse the image in Calibre or another tool.

```bash
# Save the largest image from the first page
calpdf extract-cover book.pdf

# Save the cover to a specific file and format
calpdf extract-cover book.pdf -o cover.jpg

# Write the original bytes from the second page with the default name
calpdf extract-cover book.pdf --page 2 --raw
```

Without `--output`, calpdf saves the image in the current directory as `BOOK_STEM_cover.png` when the embedded image uses the `/FlateDecode` filter and as `BOOK_STEM_cover.jpg` otherwise. `BOOK_STEM` is the PDF file name without its extension. The command picks the image with the largest pixel area on the selected page, so it skips small icons and returns the image that most likely is the cover.

To write the original bytes without re-encoding, use `--raw`. With `--raw`, calpdf writes the embedded bytes unchanged and does not check the output extension. If the extension does not match the embedded format, the file holds bytes that do not match its name.

## Reusing the cover in Calibre

Extract the cover when you need the image on its own:

```bash
calpdf extract-cover book.pdf
```

To set the extracted image as the book's cover in Calibre:

1. Open the book.
2. Choose **Edit metadata**.
3. Drag the extracted file (for `book.pdf`, that is `book_cover.jpg` or `book_cover.png`) onto the cover on the right.
