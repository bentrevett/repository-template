# repository-template

A repository template for Python projects, inspired by [this](https://github.com/neubig/starter-repo) one, but using `uv` and not using `mypy` or GitHub Actions.

## Usage

To get a local copy of the template:
- Click "Use this template" (green button, top right) and "Create a new repository"
- Give it a name and (if you want) a description
- Open a terminal and run `git clone https://github.com/<your-username>/<your-repository-name>.git`

To use the template:
- Open a terminal and navigate into your repository's directory
- If you don't have `uv` installed, install `uv` with `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Install the pre-commit hooks: `uv run pre-commit install`
- Run tests: `uv run pytest`
- Execute code: `uv run example/add.py`
- Run linter: `uv run ruff check`
- Run formatter: `uv run ruff format`
