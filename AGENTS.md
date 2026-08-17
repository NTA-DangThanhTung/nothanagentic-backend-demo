# AGENTS.md

Base backend project. No LLM/agent automation is wired into this repo yet
(no CI review action, no MCP servers) — it's a plain modular-monolith
FastAPI skeleton. Add automation deliberately later, not by default.

## Verify before saying "done"

```bash
just lint       # ruff check + ruff format --check
just typecheck  # mypy --strict on src/
just test       # pytest
just check      # all three
```

## Architecture rules

- One package per domain under `src/app/modules/<domain>/`, each self-contained:
  `router.py` (thin HTTP layer), `schemas.py` (Pydantic in/out), `models.py`
  (SQLAlchemy), `service.py` (business logic), `repository.py` (data access),
  `dependencies.py` (FastAPI `Depends` wiring).
- Business logic lives in `service.py`, never in `router.py`.
- `src/app/shared/` is for code reused by 2+ modules, earned through repeated
  use — don't create abstractions preemptively.
- `src/app/core/` is cross-cutting infra: config, DB engine/session, logging,
  exception handlers. Not a dumping ground for domain logic.

## Forbidden

- No dropping tables outside an Alembic migration.
- No force-pushing `main`.
- No new dependency without checking it's actually needed — this is a small
  base project, keep the dependency tree lean.

## Secrets

- Config comes from `.env` (see `.env.example`) via `pydantic-settings`.
  Never hardcode credentials or log request bodies containing PII.

## Glossary

- **Item** — the one example domain module in this skeleton, purely to show
  the router/schema/model/service/repository shape. Replace/remove it once
  real domains exist.
