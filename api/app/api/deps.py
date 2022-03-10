from app.database.session import engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel.sql.expression import Select, SelectOfScalar

# def get_session() -> Generator[Session, None, None]:
#     with Session(engine) as session:
#         yield session


async def get_session() -> AsyncSession:
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session


"""
The next 2 lines are temporary solution to avoid SQLModel warning about SQL caching
By doing this I can import "select" directly from SQLModel and not from SQLAlchemy

Related issues:
https://github.com/tiangolo/sqlmodel/issues/189
"""
SelectOfScalar.inherit_cache = True  # type: ignore
Select.inherit_cache = True  # type: ignore
