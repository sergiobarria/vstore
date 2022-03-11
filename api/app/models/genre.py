from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class GenreBase(SQLModel):
    """Genre base model"""

    name: str = Field(index=True)


class Genre(GenreBase, table=True):
    """Main Genre model table"""

    __tablename__ = "genres"

    id: UUID | None = Field(
        default_factory=uuid4, primary_key=True, index=True, nullable=False
    )


class GenreCreate(GenreBase):
    """Response model for creating new genres and adding them to the database"""

    pass


class GenreRead(GenreBase):
    """Response model for reading docs from the database an return them to the user"""

    id: UUID


class GenreUpdate(SQLModel):
    """Response model to update genre in db"""

    name: str | None = None
