# Installation

calpdf needs Python 3.11 or later, [Git](https://git-scm.com/downloads), and the
`uv` package manager. If you don't have `uv` yet, see the
[uv installation guide](https://docs.astral.sh/uv/).

## Install from source

Clone the repository and enter it:

```bash
git clone https://github.com/athaurian/calpdf.git
cd calpdf
```

Install the command with `uv`:

```bash
uv tool install .
```

This installs calpdf in its own environment. If the `calpdf` command isn't
found afterward, run `uv tool update-shell` and restart your shell.

To set up a development environment instead, see [Development](development.md).

## External dependencies

calpdf depends on one external program:

- `qpdf`: Required by the [`optimize`](commands/optimize.md) command. Install it
  before you optimize a PDF.

## First run

The [`info`](commands/info.md) command reads a PDF and prints its properties. It
only reads the file, so you can run it on a PDF you care about:

```bash
calpdf info book.pdf
```

When you are ready to change something, [`set-cover`](commands/set-cover.md) and
[`optimize`](commands/optimize.md) are a good place to start because each makes
one change and keeps a backup. For a full pass over one book, see the
[example session](index.md#example-session) on the home page. If you would
rather stay in Calibre, the [Calibre plugin](calibre.md) runs the same tasks in
a dialog.

## Arch Linux

If you run Arch Linux, you can install the signed `calpdf-git` package from my
[Forge repository](https://github.com/athaurian/forge). For setup instructions,
see the
[Forge README](https://github.com/athaurian/forge#set-up-the-repository).
