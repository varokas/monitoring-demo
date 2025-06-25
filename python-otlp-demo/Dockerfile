FROM python:3.12-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Set working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml uv.lock ./
COPY src/* src/

# Install dependencies
RUN uv sync --frozen

# Run the application
CMD ["uv", "run", "src/main.py"]