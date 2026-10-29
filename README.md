# hello

A minimal Hello World Python project with tests and CI.

## Features

- `src/` package layout
- `greet(name)` function with a default value of `"World"`
- CLI entry point via `argparse` with an optional `--name` argument
- `python -m hello` module execution
- Unit tests with `pytest`
- Linting with `ruff`
- GitHub Actions CI for Python 3.11+

## Install

Create a virtual environment and install the package in editable mode with development dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

## Run

Default greeting:

```bash
python -m hello
# Output: Hello, World!
```

Custom name:

```bash
python -m hello --name Alice
# Output: Hello, Alice!
```

Or use the installed console script:

```bash
hello --name Alice
```

## Test

Run the test suite with `pytest`:

```bash
pytest tests/ -v
```

## Lint

Run lint checks with `ruff`:

```bash
ruff check src tests
```
