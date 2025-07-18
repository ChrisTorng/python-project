# Python project

[I'm Switching to Python and Actually Liking It](https://www.cesarsotovalero.net/blog/i-am-switching-to-python-and-actually-liking-it.html)

```bash
# Install uv globally if not already installed
curl -sSfL <https://astral.sh/install.sh> | sh

# Initialize a new project (adds .gitignore, .python-version, pyproject.toml, etc.)
uv init python-api

# Add some dependencies into the project and update pyproject.toml
cd python-api
uv add --dev pytest ruff pre-commit mkdocs fastapi pydantic

# Update the lock file with the latest versions of the dependencies (creates a .venv if not already created)
uv sync
```

# VS Code Python runtime activate

In VSCode

- Open `python-api\main.py`, on right bottom corner, click version.
- Enter interpreter path: `python-api\.venv\Scripts\python.exe`.
- "Kill Terminal" and reopen it
- It should run `& d:/Projects/GitHub/ChrisTorng/python-project/python-api/.venv/Scripts/Activate.ps1` and shows `(python-api)` as currently activated environment.

## [gitleaks](https://github.com/gitleaks/gitleaks): prevent API key or password leaks

 - [Releases](https://github.com/gitleaks/gitleaks/releases) - Show all 14 assets - Download gitleaks_xxx_windows_x64.zip

Make a `gitleaks.cmd` in PATH folder. You can run `gitleaks` in Terminal.

## [ruff](https://github.com/astral-sh/ruff): super-fast linter and code formatter

```bash
# Lint all files under current folder, or in `/path/to/code` (and any subdirectories).
ruff check (path/to/code/)

# Format all files under current folder, or in `/path/to/code` (and any subdirectories).
ruff format (path/to/code/)
```

## https://github.com/astral-sh/ty: type checker

## [pytest](https://docs.pytest.org/en/stable/): unit test framework

```bash
uv run pytest
```

## [Pydantic](https://pydantic-docs.helpmanual.io/): data validation and settings management library

[Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)

```python
from pydantic import BaseSettings

class Settings(BaseSettings):
    api_key: str
    db_url: str

    class Config:
        env_file = ".env"

settings = Settings()
```

##  [MkDocs](https://www.mkdocs.org/): documentation and static generation of the website

## [FastAPI](https://fastapi.tiangolo.com/): web framework for building APIs based on standard Python type hints

## [dataclasses](https://docs.python.org/3/library/dataclasses.html): a Python feature that provides a way to define classes that are primarily used to store data.

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(1, 2)
print(p)  # Output: Point(x=1, y=2)
```

## [GitHub Actions](https://github.com/features/actions)

```yaml
name: CI-API

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    # runs-on: windows-latest
    # runs-on: macos-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      - name: Build Docker image
        run: docker build -t project-api:ci ./project-api
      - name: Run tests
        run: docker run --rm project-api:ci pytest
```
