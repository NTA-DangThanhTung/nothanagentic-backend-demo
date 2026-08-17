default:
    @just --list

sync:
    uv sync

run:
    uv run uvicorn app.main:app --reload --app-dir src

lint:
    uv run ruff check .
    uv run ruff format --check .

fmt:
    uv run ruff check --fix .
    uv run ruff format .

typecheck:
    uv run mypy src

test:
    uv run pytest

check: lint typecheck test

migrate:
    uv run alembic upgrade head

migration name:
    uv run alembic revision --autogenerate -m "{{name}}"
