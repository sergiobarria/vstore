from typing import List

from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn


class Settings(BaseSettings):
    PROJECT_NAME: str = "VStore E-commerce API"
    API_V1_STR: str = "/api/v1"
    DESCRIPTION: str = """
        Backend server application for the VStore book store app
    """
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:3000"]

    # Database Info
    # DB_USER: str = os.getenv("DB_USER")
    # DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    # DB_HOST: str = os.getenv("DB_HOST")
    # DB_PORT: Union[int, str] = os.getenv("DB_PORT")
    # DB_NAME: str = os.getenv("DB_NAME")

    SQLITE_ASYNC_DB_URL: str = "sqlite+aiosqlite:///vstore.db"
    # PG_DATABASE_URL: PostgresDsn | None = (
    #     f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    # )
    PG_DATABASE_URL: PostgresDsn | None = (
        "postgresql+asyncpg://sergio@localhost:5432/vstore"
    )

    # class Config:
    #     env_file = ".env"


# @lru_cache()
# def get_settings() -> Settings:
#     return Settings()


settings = Settings()
