from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_name: str = "nothanagentic-backend-demo"
    environment: str = "local"
    database_url: str = "postgresql+asyncpg://app:app@localhost:5432/app"
    log_level: str = "INFO"


@lru_cache
def get_settings() -> Settings:
    return Settings()
