# Global options

You can place the following options before any subcommand:

```bash
calpdf --quiet COMMAND ...      # suppress informational output except errors and warnings
calpdf --no-color COMMAND ...   # disable colored output
calpdf --version                # show the version and exit
```

The `--quiet` option does not suppress JSON data. The `info --format json` and `export-toc` commands still write their JSON to standard output.

The `--quiet` and `--version` options have the short forms `-q` and `-v`. To see the help text and the list of commands, run `calpdf` without arguments. To view a command's options, run `calpdf COMMAND --help`.

Tab completion is built in. To install it for the current shell, run:

```bash
calpdf --install-completion
```

Run it once per shell type, then restart the shell. To print the completion code instead of installing it, run `calpdf --show-completion`.
