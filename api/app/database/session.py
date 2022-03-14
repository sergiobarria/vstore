from typing import Generator

from app.core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

USER = settings.DB_USERNAME
PASSWORD = settings.DB_PASSWORD
HOST = settings.DB_HOST
PORT = settings.DB_PORT
NAME = settings.DB_NAME

DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session() -> Generator:
    with SessionLocal() as session:
        yield session
