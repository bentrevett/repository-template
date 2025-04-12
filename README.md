# repository-template

## Usage

- If you don't have `uv` installed, install `uv` with `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Install the pre-commit hooks (or else they won't run): `uv run pre-commit install`
- Run tests: `uv run pytest`
- Execute code: `uv run example/add.py`
- Run linter: `uv run ruff check`
- Run formatted: `uv run ruff format`