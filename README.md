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

# Activate the .venv
uv venv activate
```

## gitleaks

[gitleaks](https://github.com/gitleaks/gitleaks) - [Releases](https://github.com/gitleaks/gitleaks/releases) - Show all 14 assets - Download gitleaks_xxx_windows_x64.zip

Make a `gitleaks.cmd` in PATH folder. You can run `gitleaks` in Terminal.

