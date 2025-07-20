# Python project

[I'm Switching to Python and Actually Liking It](https://www.cesarsotovalero.net/blog/i-am-switching-to-python-and-actually-liking-it.html)

## Project Structure

```
./
│
├── .github/ # GitHub Actions workflows for CI/CD pipelines
│   ├── workflows/ # Directory containing YAML files for automated workflows
│   └── dependabot.yml # Configuration for Dependabot to manage dependencies
│
├── .vscode/ # VSCode configuration for the project
│   ├── launch.json # Debugging configurations for VSCode
│   └── settings.json # Project-specific settings for VSCode
│
├── docs/ # Website and docs (a static SPA with MkDocs)
│
├── project-api/ # Backend API for handling business logic and heavy processing
│   ├── data/ # Directory for storing datasets or other static files
│   ├── notebooks/ # Jupyter notebooks for quick (and dirty) experimentation and prototyping
│   ├── tools/ # Utility scripts and tools for development or deployment
│   ├── src/ # Source code for the backend application
│   │   ├── app/ # Main application code
│   │   └── tests/ # Unit tests for the backend
│   │
│   ├── .dockerignore # Specifies files to exclude from Docker builds
│   ├── .python-version # Python version specification for pyenv
│   ├── Dockerfile # Docker configuration for containerizing the backend
│   ├── Makefile # Automation tasks for building, testing, and deploying
│   ├── pyproject.toml # Python project configuration file
│   ├── README.md # Documentation for the backend API
│   └── uv.lock # Lock file for dependencies managed by UV
│
├── project-ui/ # Frontend UI for the project (Next.js, React, etc.)
│
├── .gitignore # Global Git ignore file for the repository
├── .pre-commit-config.yaml # Configuration for pre-commit hooks
├── CONTRIBUTING.md # Guidelines for contributing to the project
├── docker-compose.yml # Docker Compose configuration for multi-container setups
├── LICENSE # License information for the project (I always choose MIT)
├── Makefile # Automation tasks for building, testing, and deploying
└── README.md # Main documentation for the project (main features, installation, and usage)```
```

## [uv](https://astral.sh/uv/): Python project management tool

```bash
# Install uv globally if not already installed
curl -sSfL <https://astral.sh/install.sh> | sh

# Initialize a new project (adds .gitignore, .python-version, pyproject.toml, etc.)
uv init project-api

# Add some dependencies into the project and update pyproject.toml
cd project-api
uv add --dev pytest ruff pre-commit mkdocs fastapi pydantic

# Update the lock file with the latest versions of the dependencies (creates a .venv if not already created)
uv sync
```

# VS Code Python runtime activate

In VSCode

- Open `project-api\main.py`, on right bottom corner, click version.
- Enter interpreter path: `project-api\.venv\Scripts\python.exe`.
- "Kill Terminal" and reopen it
- It should run `& d:/Projects/GitHub/ChrisTorng/python-project/project-api/.venv/Scripts/Activate.ps1` and shows `(project-api)` as currently activated environment.

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

## [FastAPI](https://fastapi.tiangolo.com/): web framework for building APIs based on standard Python type hints

Add [project-api/src/app/api.py](project-api/src/app/api.py) and [project-api/src/app/__init__.py](project-api/src/app/__init__.py).

Run with:
```bash
fastapi run project-api/src/app/api.py
```

Open [http://localhost:8000/](http://localhost:8000/) run the default API.

Open [http://localhost:8000/docs](http://localhost:8000/docs) to see the API documentation.


## [pytest](https://docs.pytest.org/en/stable/): unit test framework

Add [project-api/src/app/tests/test_api.py](project-api/src/app/tests/test_api.py).

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

```bash
mkdocs new project-api
cd project-api
mkdocs serve -a 127.0.0.1:8001
```
Open [http://127.0.0.1:8001/](http://127.0.0.1:8001/) to view the documentation site.

Update [mkdocs.yml](project-api/mkdocs.yml) to add navigation and theme.

```bash
mkdocs build
```

Add `project-api/site/` to `.gitignore` to ignore the generated site files.

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

Add [.github/workflows/CI-API.yaml](.github/workflows/CI-API.yaml).

## [Dependabot](https://dependabot.com/)

Add [.github/dependabot.yml](.github/dependabot.yml).

## [pre-commit](https://pre-commit.com/) Hooks

Add [.pre-commit-config.yaml](.pre-commit-config.yaml), with `ruff check/format` and `gitleaks`.

```bash
pre-commit autoupdate
pre-commit install
pre-commit run --all-files
```

Now every time you commit, it will run the pre-commit hooks defined in `.pre-commit-config.yaml`.

## [Podman](https://podman.io/)

Add [Dockerfile](project-api/Dockerfile) and [docker-compose.yml](docker-compose.yml).

```bash
uv add --dev podman-compose
podman machine start
podman-compose build
podman-compose up --build -d
podman-compose stop
```

## [Make](https://www.gnu.org/software/make/)

Add [project-api/Makefile](project-api/Makefile).

```bash
cd project-api
make test
make format-fix
make lint-fix
```

Add [Makefile](Makefile).

```bash
podman machine start
make infra-build
make infra-up
make infra-stop
```

