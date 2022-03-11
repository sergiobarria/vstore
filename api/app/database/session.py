from app.core.config import settings
from sqlalchemy.ext.asyncio import create_async_engine

# For SQLite
# connect_args = {"check_same_thread": False}

engine = create_async_engine(settings.PG_DATABASE_URL, echo=True, connect_args={})
