# Development

## Requirements and setup

- Python `3.11+`, Git, `uv`, and `make`
- Node.js with `npx` (used by `make format` and `make lint` to run Prettier on Markdown files)
- `qpdf` on `PATH` (for `optimize` integration tests)

Install dependencies into the project virtual environment:

```bash
uv sync --dev
```

## Common tasks

| Target            | Purpose                                                 |
| :---------------- | :------------------------------------------------------ |
| `make test`       | Run the `pytest` suite                                  |
| `make lint`       | Run Ruff checks, mypy, and Prettier format verification |
| `make format`     | Auto-format Python with Ruff and Markdown with Prettier |
| `make docs`       | Build the Zensical documentation site in strict mode    |
| `make docs-serve` | Serve the documentation locally with live reload        |
| `make check`      | Run `lint`, `test`, and strict `docs` build together    |

## Updating dependencies and shared assets

- **Dependencies**: After editing `pyproject.toml`, run `uv lock` and commit the updated `uv.lock` so CI builds remain reproducible.
- **Docs theme**: The Zensical theme assets in `docs/` are synced from [`docs-theme`](https://github.com/athaurian/docs-theme); do not hand-edit generated theme overrides in this repository.
- **Calibre plugin screenshots**: Plugin UI screenshots are rendered in the [`calibre-calpdf`](https://github.com/athaurian/calibre-calpdf) repository via `make ui`.
