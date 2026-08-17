# nothanagentic-backend-demo

Base backend skeleton — FastAPI + Postgres + SQLAlchemy 2.0 async + Pydantic
v2, managed with [uv](https://docs.astral.sh/uv/), linted/formatted with
[Ruff](https://docs.astral.sh/ruff/), type-checked with `mypy --strict`.
Structured as a modular monolith: one self-contained package per domain
under `src/app/modules/`.

No LLM/agent automation (review bots, MCP servers, etc.) is wired in yet —
this is intentionally just the base project. Add that layer deliberately
later, on top of this foundation.

## Stack

| Concern | Choice |
|---|---|
| Web framework | FastAPI |
| Package manager | uv |
| Lint/format | Ruff |
| Type checker | mypy --strict |
| Validation | Pydantic v2 |
| ORM | SQLAlchemy 2.0 async + asyncpg |
| Migrations | Alembic |
| DB | PostgreSQL |
| Tests | pytest + pytest-asyncio + httpx AsyncClient |
| Config | pydantic-settings |
| Observability | structlog |
| Task runner | just |

See [`AGENTS.md`](AGENTS.md) for the rules an AI coding agent should follow
in this repo (`CLAUDE.md` is a symlink to it).

## Getting started

```bash
cp .env.example .env
docker compose up -d postgres
just sync
just migrate   # once there are migrations
just run
```

Open http://localhost:8000/docs for the interactive API docs.

## Common tasks

```bash
just lint        # ruff check + format check
just fmt          # ruff check --fix + format
just typecheck    # mypy --strict
just test         # pytest
just check        # lint + typecheck + test
just migration "add foo table"   # new alembic revision
just migrate      # apply migrations
```

## Layout

```
src/app/
├── main.py            # FastAPI app factory
├── core/               # cross-cutting: config, db session, logging, exceptions
├── modules/
│   └── items/          # example domain module (router/schemas/models/service/repository)
└── shared/              # code reused by 2+ modules, earned not pre-built
```

`items` is a placeholder domain module demonstrating the pattern — replace
or remove it once real domains land.
