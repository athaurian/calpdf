# ToC JSON format

[`export-toc`](../commands/export-toc.md) and [`apply-toc`](../commands/apply-toc.md) use a UTF-8 JSON array of bookmark objects. Top-level array items are root bookmarks, and nested items live inside each entry's `children` array.

```json
[
  {
    "title": "Preface",
    "pageNumber": 5,
    "children": []
  },
  {
    "title": "Chapter 1: Foundations",
    "pageNumber": 11,
    "children": [
      {
        "title": "1.1 Definitions",
        "pageNumber": 11,
        "children": []
      },
      {
        "title": "1.2 Examples",
        "pageNumber": 18,
        "children": []
      }
    ]
  }
]
```

## Field rules

| Field        | Type                | Rules                                                                                                                                       |
| :----------- | :------------------ | :------------------------------------------------------------------------------------------------------------------------------------------ |
| `title`      | `string`            | Required. Must be non-empty when passed to `apply-toc`.                                                                                     |
| `pageNumber` | `integer` or `null` | Required. 1-indexed physical page number (`1` to total pages). Always refers to the physical PDF page, not custom display labels like `iv`. |
| `children`   | `array`             | Required. List of child bookmark objects (`[]` when the bookmark has no children).                                                          |

### Handling `pageNumber: null`

Some PDFs contain section header bookmarks without a page destination. `export-toc` exports these as `"pageNumber": null` so no hierarchy data is lost, but `apply-toc` requires every bookmark to point to a valid integer page. Assign a page number or remove the entry before running `apply-toc`.
