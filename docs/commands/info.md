# `info`

Displays a PDF's page count, PDF specification version, file size, bookmark count (total and top-level), and page dimensions.

```bash
calpdf info book.pdf
calpdf info book.pdf --format json -o info.json
```

## Options

| Option                  | Default | Description                                                                                                                                                       |
| :---------------------- | :------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--format [text\|json]` | `text`  | `text` prints a human-readable summary that groups identical page sizes. `json` outputs machine-readable metadata including individual dimensions for every page. |
| `-o`, `--output PATH`   | stdout  | Write JSON output to `PATH`. Has no effect (and prints a warning) when `--format text` is active.                                                                 |
