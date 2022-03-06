from typing import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import async_session


async def get_db() -> AsyncIterator[AsyncSession]:
    """Dependency function that yields db sessions
    """
    async with async_session() as session:
        yield session
        await session.commit()

# Sync db connection
# def get_db() -> Generator:
#     """Get DB session"""
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
