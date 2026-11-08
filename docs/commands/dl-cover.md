# The `dl-cover` command

The `dl-cover` command downloads a cover image for a book. Pass an _Amazon Standard Identification Number (ASIN)_, an _International Standard Book Number (ISBN)_, or an _Open Library ID (OLID)_:

```bash
# Download a cover by ASIN
calpdf dl-cover B08X92NRKV

# Download a cover by ISBN and save it with a specific name
calpdf dl-cover 9780387967875 -o mycover.jpg

# Download a cover by Open Library ID
calpdf dl-cover OL123W
```

Without `--output`, calpdf saves the image in the current directory as `BOOK_ID_cover.jpg` or `BOOK_ID_cover.png`, choosing the extension from the detected image format. `BOOK_ID` is the identifier you passed. The identifier can only contain ASCII letters, digits, and dashes. `--output` writes the downloaded bytes unchanged to the path you give, so it does not convert the image or change the extension.

calpdf tries Amazon first, then Open Library by ISBN and by OLID. It uses the first response that returns HTTP 200, is at least 1 KB, and starts with a JPEG or PNG signature.

To download a cover and apply it to a PDF in one step, use [`set-cover`](set-cover.md).
