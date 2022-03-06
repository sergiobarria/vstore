from typing import Any
from uuid import UUID
from sqlalchemy_utils import UUIDType
from pydantic import BaseModel


class BookBase(BaseModel):
    title: str


class BookSchema(BookBase):
    """Book class for reading and returning data from the API"""

    class Config:
        orm_mode = True


class BookInDatabase(BookBase):
    id: UUID

    class Config:
        orm_mode = True
