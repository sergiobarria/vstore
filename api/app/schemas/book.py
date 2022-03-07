from uuid import UUID
from pydantic import BaseModel


class BookBase(BaseModel):
    title: str


class Book(BookBase):
    """Book class for reading and returning data from the API"""

    class Config:
        orm_mode = True


class BookInDatabase(BookBase):
    id: UUID

    class Config:
        orm_mode = True
