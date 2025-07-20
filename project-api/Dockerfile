FROM python:3.11-slim

# Install system dependencies
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY uv.lock pyproject.toml README.md ./
RUN uv sync --frozen --no-cache --group dev

# Bring in the actual application code
COPY src/app app/
COPY src/tests tests/
COPY tools tools/

# Define a command to run the application
# CMD ["/app/.venv/bin/fastapi", "run", "app/api.py", "--port", "8000", "--host", "0.0.0.0"]
CMD ["uv", "run", "fastapi", "run", "app/api.py", "--port", "8000", "--host", "0.0.0.0"]