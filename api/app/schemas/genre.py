from uuid import UUID

from app.schemas.base import BaseSchema
from pydantic import Field


class GenreBase(BaseSchema):
    """This is the description of the base genre model"""

    name: str | None = Field(max_length=50)


class GenreCreate(GenreBase):
    """Response model for creating a new genre"""

    name: str


class GenreRead(GenreBase):
    """Response model for reading a genre from DB"""

    id: UUID


class GenreUpdate(GenreBase):
    """Response model for updating a genre"""

    ...


class GenreWithBook(BaseSchema):
    """Response model for genre including just ID and name"""

    id: UUID
    name: str
