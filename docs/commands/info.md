# The `info` command

The `info` command shows information about a PDF, such as the number of pages, the PDF version, the file size, the bookmark count, and the page sizes. The text output lists up to five page sizes and summarizes the rest. The JSON output includes every page.

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
