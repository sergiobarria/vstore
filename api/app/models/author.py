from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class AuthorBase(SQLModel):
    """Base author model"""

    name: str = Field(max_length=100, index=True)
    bio: str = Field(max_length=7000)
    # image: str


class Author(AuthorBase, table=True):
    """Main Author model table"""

    __tablename__ = "authors"

    id: UUID | None = Field(
        default_factory=uuid4, primary_key=True, index=True, nullable=False
    )


class AuthorCreate(AuthorBase):
    """Response model for creating new authors and add them to db"""

    pass


class AuthorRead(AuthorBase):
    """Response model for reading author docs from the db and return them to the user"""

    id: UUID


class AuthorUpdate(SQLModel):
    """Response model to update author doc in db"""

    name: str | None = None
    bio: str | None = None
