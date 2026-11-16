# `set-cover`

Downloads a cover by ASIN, ISBN, or Open Library ID and applies it to a PDF in one step. The downloaded image is stored in a temporary file and deleted as soon as the PDF is updated; use [`dl-cover`](dl-cover.md) first if you want to keep a copy of the image on disk.

```bash
calpdf set-cover book.pdf 9780387967875
calpdf set-cover book.pdf B08X92NRKV --mode insert --fit fill -o output.pdf
```

## Options

`set-cover` uses the same lookup rules as [`dl-cover`](dl-cover.md) and accepts the same placement and sizing options as [`replace-cover`](replace-cover.md) (`-o` / `--output`, `--mode`, `--pages`, `--fit`, and `--dpi`).

If `-o` / `--output` is omitted, `book.pdf` is modified in place (see [Backup behavior](../reference/backup-behavior.md)).
