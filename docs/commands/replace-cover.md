# The `replace-cover` command

The `replace-cover` command replaces the first page of a PDF with a cover image, or inserts the image as a new first page. The image must be a PNG or JPEG file.

The following examples show common ways to use it:

```bash
# Replace the first page with a new cover image
calpdf replace-cover book.pdf cover.jpg

# Insert the image as a new first page without removing any pages
calpdf replace-cover book.pdf cover.jpg --mode insert

# Write to a new file instead of updating the input file
calpdf replace-cover book.pdf cover.jpg -o output.pdf

# Replace the first two pages
calpdf replace-cover book.pdf cover.jpg --pages 2
```

By default, the command updates the PDF in place and keeps a backup of the original file. These options control where the result goes and how the cover is built:

| Option           | Effect                                                                                                  |
| ---------------- | ------------------------------------------------------------------------------------------------------- |
| `--output`, `-o` | Writes the result to a new file.                                                                        |
| `--mode`         | Selects `replace` (the default) or `insert`, which keeps all pages.                                     |
| `--pages`        | Controls how many pages the image replaces (only used in replace mode).                                 |
| `--dpi`          | Sets the resolution of the cover image (the default is 300 dots per inch, and the range is 72 to 1200). |

For more information, see [Backup behavior](../reference/backup-behavior.md).

The target page sets the cover size. In replace mode, it is the first page that remains after the replaced pages. If every page is replaced, it is the last page. In insert mode, it is the first page.

The `--fit` option controls how the image fits on the page:

- `match-width` (the default) keeps the width of the target page and sets the height from the image's aspect ratio, so the image fills the page with no cropping and no empty space.
- `fill` scales the image to cover the exact target page size and crops the parts that overflow.
- `fit` scales the image to fit inside the exact target page size and centers it on a white background.

When replace mode removes pages, calpdf also removes bookmark entries, named destinations, internal links, and open actions that point to the removed pages.

If you swap the arguments and pass the image as the first argument, calpdf detects the mix-up and prints a hint.

The [`set-cover`](set-cover.md) command accepts the same options, except for the image argument.
