# `export-toc`

Exports a PDF's bookmark tree as JSON (for editing and re-applying with [`apply-toc`](apply-toc.md)) or as an indented terminal tree.

```bash
# Write editable ToC JSON to a file
calpdf export-toc book.pdf -o toc.json

# Inspect the bookmark hierarchy in the terminal
calpdf export-toc book.pdf --format tree
```

## Options

| Option                  | Default | Description                                                                       |
| :---------------------- | :------ | :-------------------------------------------------------------------------------- |
| `-o`, `--output PATH`   | stdout  | Write JSON output to `PATH`. Ignored with a warning when `--format tree` is used. |
| `--format [json\|tree]` | `json`  | Output format. Only `json` can be passed back to `apply-toc`.                     |

## Page numbers and broken bookmarks

- **1-indexed physical pages**: `pageNumber` always refers to the physical page index starting at `1`, regardless of Roman numerals or custom reader page labels (`i`, `ii`, `A-1`). See [ToC JSON format](../reference/toc-json-format.md).
- **Unlinked bookmarks (`pageNumber: null`)**: If the source PDF has a bookmark with no destination page, `export-toc` preserves it with `"pageNumber": null`. You must replace `null` with an integer page number before running `apply-toc`, which rejects unlinked entries.

## Adding bookmarks to a PDF that has none

Exporting from a PDF without bookmarks writes an empty JSON list (`[]`), which you can populate and apply:

```bash
calpdf export-toc book.pdf -o toc.json
# Edit toc.json to add {"title": "...", "pageNumber": 1, "children": []} entries
calpdf apply-toc book.pdf toc.json
```
