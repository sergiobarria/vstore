from typing import List, Union

from dotenv import load_dotenv
from pydantic import AnyHttpUrl, BaseSettings

load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = "VStore E-commerce API"
    API_V1_STR: str = "/api/v1"
    DESCRIPTION: str = """
        Backend server application for the VStore book store app
    """
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:3000"]

    # Database Info
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: Union[int, str]
    DB_NAME: str

    SQLITE_ASYNC_DB_URL: str = "sqlite+aiosqlite:///vstore.db"

    class Config:
        env_file = ".env"


settings = Settings()
