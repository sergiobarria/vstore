from typing import List
from uuid import UUID

from app.schemas.base import BaseSchema

# if TYPE_CHECKING:
from app.schemas.book import BookSimple
from pydantic import Field


class AuthorBase(BaseSchema):
    """This is the description of the base author model"""

    name: str | None = Field(max_length=100)
    bio: str | None = Field(max_length=7000)


class AuthorCreate(AuthorBase):
    """Response model for create an author"""

    name: str
    bio: str


class AuthorRead(AuthorBase):
    """Response model for reading author from DB"""

    id: UUID


class AuthorUpdate(AuthorBase):
    """Response model for updating an author"""

    ...


class AuthorSimple(BaseSchema):
    """Respons model that includes only ID and name from the author"""

    id: UUID
    name: str


class AuthorSchema(AuthorRead):
    """Response model for retrieving an author and including related books"""

    books: List[BookSimple] = []
