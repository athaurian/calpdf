# Installation

## Requirements

- Python `3.11+`
- Git and [`uv`](https://docs.astral.sh/uv/) (for source installs)
- `qpdf` on `PATH` (only required for [`calpdf optimize`](commands/optimize.md))

## Install with `uv`

```bash
git clone https://github.com/athaurian/calpdf.git
cd calpdf
uv tool install .
```

If `~/.local/bin` is not on your `PATH`, run `uv tool update-shell` and restart your shell.

## Arch Linux (Forge repository)

If you use the [`forge`](https://github.com/athaurian/forge) repository, install the signed package with `pacman`:

```bash
sudo pacman -S calpdf-git
```

Prefer this package over `uv tool install` if you also use the [Calibre plugin](calibre.md), because `pacman` installs `calpdf` into the system Python environment that Calibre imports from.

## Verify the install

```bash
calpdf --version
calpdf info book.pdf
```
