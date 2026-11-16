# Global options

Pass global flags before the subcommand name:

```bash
calpdf [GLOBAL OPTIONS] COMMAND [ARGS]...
```

| Option            | Description                                                                                                                                                                                                             |
| :---------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-q`, `--quiet`   | Suppress status messages and progress output. Warnings, errors, and machine-readable data written to stdout (`info --format json` and `export-toc` without `-o`) are still printed so shell pipelines continue to work. |
| `--no-color`      | Disable ANSI color formatting in terminal output.                                                                                                                                                                       |
| `-v`, `--version` | Print the `calpdf` version and exit.                                                                                                                                                                                    |

## Shell completion

Install or inspect tab-completion scripts for your current shell (`bash`, `zsh`, `fish`, or `powershell`):

```bash
calpdf --install-completion
calpdf --show-completion
```
