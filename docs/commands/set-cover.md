# The `set-cover` command

The `set-cover` command downloads a cover and applies it to a PDF in one step,
so you don't have to run [`dl-cover`](dl-cover.md) and then
[`replace-cover`](replace-cover.md). The book identifier can be an ASIN, ISBN,
or Open Library ID, as for [`dl-cover`](dl-cover.md). The downloaded image is
temporary. The command deletes it after it applies the cover. Use
[`dl-cover`](dl-cover.md) if you want to keep the image file.

```bash
calpdf set-cover book.pdf B08X92NRKV
calpdf set-cover book.pdf 9780387967875 --mode insert
```

The first example replaces the first page with the downloaded cover. The second
inserts the cover as a new first page and keeps all the pages.

The command accepts the same options as the `replace-cover` command, except for
the image argument. For more information about these options, see
[The `replace-cover` command](replace-cover.md).
