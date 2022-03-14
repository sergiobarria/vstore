from uuid import UUID

from app.schemas.base import BaseSchema
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
