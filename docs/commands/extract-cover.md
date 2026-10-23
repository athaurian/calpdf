# The `extract-cover` command

The `extract-cover` command extracts the cover image from a PDF page and saves it as a separate file. Use it to pull a cover out of a PDF so you can reuse the image in Calibre or another tool.

```bash
# Save the cover from the first page. The extension follows the image format
calpdf extract-cover book.pdf

# Save the cover to a specific file and format
calpdf extract-cover book.pdf -o cover.jpg

# Write the original bytes from the second page, named for the embedded format
calpdf extract-cover book.pdf --page 2 --raw -o cover.png
```

Without `--output`, calpdf saves the image in the current directory as `BOOK_STEM_cover.jpg` or `BOOK_STEM_cover.png`, where `BOOK_STEM` is the PDF file name without its extension. The extension follows the image encoding. The command picks the largest image on the selected page, so it skips small icons and returns the image that most likely is the cover.

To write the original bytes without re-encoding, use `--raw`. With `--raw`, calpdf does not transcode the image, so the output extension must match the embedded image format; otherwise the file holds bytes that do not match its name.

## Reusing the cover in Calibre

Extract the cover when you need the image on its own:

```bash
calpdf extract-cover book.pdf
```

To set the extracted image as the book's cover in Calibre:

1. Open the book.
2. Choose **Edit metadata**.
3. Drag `book_cover.jpg` or `book_cover.png` onto the cover on the right.
