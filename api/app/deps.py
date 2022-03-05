from typing import Generator
from app.database.db import SessionLocal


def get_db() -> Generator:
    """Get DB session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
