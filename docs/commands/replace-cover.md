# `replace-cover`

Replaces the opening page(s) of a PDF—or prepends a new page 1—using a local PNG or JPEG image.

```bash
calpdf replace-cover book.pdf cover.jpg
calpdf replace-cover book.pdf cover.png --mode insert --fit fill -o output.pdf
```

If `-o` / `--output` is omitted, `book.pdf` is modified in place (see [Backup behavior](../reference/backup-behavior.md)).

## Options

| Option                           | Default       | Description                                                                                                                                                                                                  |
| :------------------------------- | :------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-o`, `--output PATH`            | In place      | Write the modified PDF to `PATH` instead of overwriting the input file.                                                                                                                                      |
| `--mode [replace\|insert]`       | `replace`     | `replace` removes the first `--pages` pages before inserting the cover, **along with any bookmarks and internal links targeting those removed pages**. Use `insert` when page 1 is content you want to keep. |
| `--pages INTEGER`                | `1`           | Number of leading pages to remove in `replace` mode (`1–50`). Ignored in `insert` mode.                                                                                                                      |
| `--fit [match-width\|fill\|fit]` | `match-width` | How to adapt the cover image when its aspect ratio differs from the target page.                                                                                                                             |
| `--dpi INTEGER`                  | `300`         | Rendering resolution (`72–1200` DPI) used when calculating page dimensions from pixel size.                                                                                                                  |

## Fit modes and page sizing

`calpdf` picks the target page width and height from the first surviving page after the cover (for example, page 2 when replacing page 1). If no pages survive—such as a single-page PDF in `replace` mode—the page size is derived from the image's pixel dimensions and `--dpi`.

- **`match-width` (default)**: Scales the cover to match the target page width and adjusts the cover page's height to match the image's aspect ratio. Prevents cropping and margins while keeping page width consistent across the book.
- **`fill`**: Scales the image to completely fill the target width and height, cropping any excess on the top/bottom or left/right edges.
- **`fit`**: Scales the entire image to fit inside the target width and height, centering it with margins on the shorter axis.
