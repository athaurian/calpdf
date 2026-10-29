# Installation

You need Python 3.11 or later, [Git](https://git-scm.com/downloads), and the `uv` package manager. If you don't have `uv` yet, see the [uv installation guide](https://docs.astral.sh/uv/).

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

This installs calpdf in its own environment. If the `calpdf` command is not found afterward, run `uv tool update-shell` and restart your shell.

To set up a development environment instead, see [Development](development.md).

## External dependencies

calpdf uses one program that it does not install for you:

- `qpdf`: The [`optimize`](commands/optimize.md) command requires it. You must install it before you can optimize a PDF.

## First run

The [`info`](commands/info.md) command reads a PDF and prints what it finds. It is a safe first step on a file you care about:

```bash
calpdf info book.pdf
```

When you are ready to change something, the [`set-cover`](commands/set-cover.md) and [`optimize`](commands/optimize.md) commands are good first jobs. For a full pass over one book, see the [example session](index.md#example-session) on the home page. You can run the same jobs in a dialog with the [Calibre plugin](calibre.md), if you would rather stay in Calibre.

## Arch Linux

If you run Arch Linux, you can install the signed `calpdf-git` package from my [Forge repository](https://github.com/athaurian/forge). For setup instructions, see the [Forge README](https://github.com/athaurian/forge#set-up-the-repository).
