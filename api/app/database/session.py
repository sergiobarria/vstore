from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URI = "sqlite:///./vstore.db"
SQLALCHEMY_DATABASE_URI = "sqlite+aiosqlite:///./vstore.db"
# SQLALCHEMY_DATABASE_URI = "sqlite:///./sqlite.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# When connecting to postgres remove the "check_same_thread" arg
engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={
                       "check_same_thread": False})
async_engine = create_async_engine(
    SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}, future=True, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

async_session = sessionmaker(
    async_engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()
