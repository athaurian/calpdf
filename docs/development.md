# Development

calpdf needs Python 3.11 or later, [uv](https://docs.astral.sh/uv/), and Git. The common checks also need `make` and Node.js, because the Makefile runs Prettier through `npx`.

## Set up the checkout

Clone the repository and enter it:

```bash
git clone https://github.com/athaurian/calpdf.git
cd calpdf
```

Install the project and its development tools:

```bash
uv sync --dev
```

This creates a virtual environment in `.venv` and installs calpdf, pytest, Ruff, mypy, and Zensical. The `--dev` flag includes the development dependency group from `pyproject.toml`.

## Run the checkout

Use `uv run` to run calpdf from the checkout without a separate global install:

```bash
uv run calpdf --version
uv run calpdf info book.pdf
```

The `uv run python -m calpdf` command reaches the same entry point. To try `optimize`, install `qpdf` first, as described in [External dependencies](installation.md#external-dependencies).

## Project layout

- The `src/calpdf/` directory holds the package and command modules. The `cli.py` module registers the commands.
- The `tests/` directory holds the pytest suite and the fixtures that build sample PDFs and images.
- The `docs/` directory holds the Markdown source for this site. The `zensical.toml` file defines the navigation and theme.
- The `Makefile` wraps the common checks.

## Test and lint

Run the narrowest check while you work, then run `make check` before you open a pull request. It runs the lint checks, builds the documentation, and runs the test suite.

- The `make test` command runs the pytest suite.
- The `make lint` command runs Ruff, mypy, and Prettier without changing files.
- The `make format` command rewrites Python and Markdown with Ruff and Prettier.
- The `make docs` command builds the site and fails on broken links or missing pages.
- The `make check` command runs the lint checks, the docs build, and the tests.

To run one test file, give it to pytest directly:

```bash
uv run pytest tests/test_toc.py
```

You can add `::TestValidateToc` or a test name to run a smaller part of the file.

## Documentation

The site is built with [Zensical](https://zensical.org/). Preview it while you edit:

```bash
make docs-serve
```

Zensical prints the preview address when it starts, and the preview reloads when a file changes. To build it once instead, run `make docs`.

The shared theme comes from the [docs-theme](https://github.com/athaurian/docs-theme) repository. The files `docs/stylesheets/extra.css`, `overrides/home.html`, `overrides/main.html`, and `docs/javascripts/theme-transition.js` are copies of its files. Make theme changes in docs-theme and run its `make sync`, rather than editing the copies here. Styles that belong only to this site go in `docs/stylesheets/calpdf.css`.

To publish a change, merge it to `main`. The docs workflow builds the site for every pull request and every push to `main`. Only a push to `main` deploys the site to GitHub Pages.

## Continuous integration

The CI workflow in `.github/workflows/ci.yml` runs on pushes to `main` and on pull requests. A lint job runs `ruff check`, `ruff format --check`, and `mypy`. A test job runs pytest on Python 3.11, 3.12, and 3.13.

Dependencies are pinned in `uv.lock`. After you change `pyproject.toml`, run `uv lock` and commit the updated lockfile.
