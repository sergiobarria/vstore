from typing import List
from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "VStore E-commerce API"
    API_V1_STR: str = "/api/v1"
    DESCRIPTION: str = """
        Backend server application for the VStore book store app
    """
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:3000"]


settings = Settings()
