# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Andexor Network, Inc.
# Author: Ed Jenkins<ed@andexor.net>

###########
# STAGE 1 #
###########

# Stage 1: Build the application.
FROM python:3.14-slim AS builder

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Create a build directory.
WORKDIR /web

# Create a virtual environment.
ENV UV_PROJECT_ENVIRONMENT=/opt/venv

# Copy build configuration files.
COPY pyproject.toml uv.lock ./

# Install dependencies.
RUN uv sync --no-install-project --no-dev

###########
# STAGE 2 #
###########

# STAGE 2: Package it for release.
FROM python:3.14-slim AS prod

# Add metadata.
LABEL Author="Ed Jenkins<ed@andexor.net>" \
      Copyright="Copyright 2026 Andexor Network, Inc." \
      Owner="Andexor Network, Inc."

# Configure Python.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH"

# Create the working directory.
WORKDIR /web

# Create a user.
RUN useradd --create-home andexor

# Copy the virtual environment from the builder stage.
COPY --from=builder /opt/venv /opt/venv

# Copy the app and documentation.
COPY --chown=andexor:andexor ./app ./app
COPY --chown=andexor:andexor ./doc ./doc

# Run as the app user.
USER andexor

# Open a port.
EXPOSE 8000

# Run the app.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers", "--http", "zttp", "--http2"]
