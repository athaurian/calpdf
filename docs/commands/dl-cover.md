# `dl-cover`

Downloads a book cover by Amazon ASIN (`B08X92NRKV`), ISBN-10/13 (`9780387967875`), or Open Library ID (`OL123W`).

```bash
# Saves to 9780387967875_cover.jpg (or .png, matching the server's format)
calpdf dl-cover 9780387967875

# Write raw downloaded bytes to an explicit path
calpdf dl-cover B08X92NRKV -o cover.jpg
```

## Lookup order and filtering

`dl-cover` queries sources in order and stops at the first valid image:

1. Amazon (direct product image lookup)
2. Open Library (by ISBN, then by Open Library ID)

To avoid saving broken placeholders, `dl-cover` skips HTTP errors, non-JPEG/PNG responses, and tiny placeholder images (such as 1×1 tracking pixels).

## Output naming and `--output`

- **Default filename**: Sanitizes the identifier to ASCII letters, digits, and dashes, and appends `_cover.jpg` or `_cover.png` based on the image's actual header bytes.
- **`-o`, `--output PATH`**: Writes the downloaded bytes directly to `PATH` without transcoding. Make sure the extension you choose matches the downloaded format (most sources return JPEG).
