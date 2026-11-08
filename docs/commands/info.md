# The `info` command

The `info` command shows the page count, PDF version, file size, bookmark counts, and page sizes of a PDF. The text output lists the first five page sizes in points and reports how many pages it omitted. The JSON output includes every page with its width, height, and rotation. Bookmark counts include the total and the number of top-level entries.

```bash
# Show a human-readable summary
calpdf info book.pdf

# Write machine-readable JSON to standard output
calpdf info book.pdf --format json

# Write JSON to a file
calpdf info book.pdf --format json -o info.json
```

The `--format` option selects one of two output modes:

| `--format` value | Behavior                                                                                                                     |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `text` (default) | Prints a summary to the terminal. The `--output` option has no effect, and calpdf prints a warning if you pass it.           |
| `json`           | Prints machine-readable JSON to standard output so you can pipe it to another program. Use `--output` to write it to a file. |
