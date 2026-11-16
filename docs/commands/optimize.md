# `optimize`

Compresses streams, removes unreferenced objects, and linearizes a PDF using `qpdf`.

```bash
calpdf optimize book.pdf
calpdf optimize book.pdf --keep-metadata --strip-color-profiles -o book-opt.pdf
```

If `-o` / `--output` is omitted, `book.pdf` is modified in place (see [Backup behavior](../reference/backup-behavior.md)).

## What gets removed by default

To shrink files as much as possible, `optimize` strips two structures unless configured otherwise:

- **Document metadata** (title, author, subject, keywords): Removed by default. Pass `--keep-metadata` to preserve these fields.
- **Document structure tree (accessibility tags)**: Always removed, even when `--keep-metadata` is set. Tagged PDFs store large element trees that often account for a sizable fraction of the file; do not run `optimize` on documents where screen-reader tag trees must be preserved.

## Options

| Option                   | Default  | Description                                                                                                                    |
| :----------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------- |
| `-o`, `--output PATH`    | In place | Write the optimized PDF to `PATH` instead of overwriting the input file.                                                       |
| `--keep-metadata`        | Off      | Preserve document info/XMP metadata (does not preserve the structure tree).                                                    |
| `--strip-color-profiles` | Off      | Remove `OutputIntents` and `ICCBased` color spaces. Useful when embedded ICC profiles bloat a grayscale or standard sRGB book. |
| `--force`                | Off      | Keep the output even if `qpdf` exits with an error code other than `0` or `3`.                                                 |

## Size changes and `qpdf` warnings

- **When files do not shrink (or grow slightly)**: PDFs dominated by already-compressed JPEG/JBIG2 scans have little stream redundancy left for `qpdf` to remove. Very small PDFs can also grow by a few kilobytes because `qpdf` adds linearization tables for fast web/reader paging.
- **`qpdf` exit code 3 vs `--force`**: `qpdf` returns exit code `3` when it repairs minor spec violations and still produces a valid PDF; `calpdf` accepts exit code `3` automatically. Pass `--force` only if `qpdf` reports a harder failure and you still want to keep the partial output.
