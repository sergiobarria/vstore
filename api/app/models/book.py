import enum
from typing import List
from uuid import UUID, uuid4

from pydantic import condecimal
from sqlalchemy import ARRAY
from sqlmodel import Column, Field, Float, SQLModel, String


class Language(enum.Enum):
    english = "english"
    spanish = "spanish"


class BookBase(SQLModel):
    """Base book model"""

    title: str = Field(index=True)
    summary: str = Field(max_length=5000)
    hard_cover_price: condecimal(decimal_places=2, ge=0) | None = Field(default=0)
    paperback_price: condecimal(decimal_places=2, ge=0) | None = Field(default=0)
    # language: Language = Field(sa_column=Column(Enum(Language)))
    published_year: int = Field(ge=0)
    num_of_pages: int = Field(ge=0)
    reading_age: int | None = None
    isbn_10: str = Field(max_length=100)
    item_weight_pounds: float
    stock_qty: int = Field(ge=0)
    is_bestseller: bool = Field(default=False)
    num_of_reviews: int = Field(ge=0)
    rating: condecimal(decimal_places=2, ge=0, le=5) = Field(default=4)
    genres: List[str] = Field(sa_column=Column(ARRAY(String())))
    dimensions: List[float] = Field(sa_column=Column(ARRAY(Float)))
    # images: List[str] = Field()

    # Relationships


class Book(BookBase, table=True):
    """Main Book model table"""

    __tablename__ = "books"

    id: UUID | None = Field(default_factory=uuid4, primary_key=True, index=True)


class BookCreate(BookBase):
    """Model for creating new books and add them to database"""

    pass


class BookRead(BookBase):
    """Model for reading docs from the database and return them to the user"""

    id: UUID


class BookUpdate(SQLModel):
    """Model to update doc in database"""

    title: str | None = None
    summary: str | None = Field(max_length=5000)
    hard_cover_price: condecimal(decimal_places=2, ge=0) | None = Field(default=0)
    paperback_price: condecimal(decimal_places=2, ge=0) | None = Field(default=0)
    language: Language | None = Field(default="english")
    published_year: int | None = Field(ge=0)
    num_of_pages: int | None = Field(ge=0)
    reading_age: int | None = Field(ge=0)
    isbn_10: str | None = Field(max_length=100)
    item_weight_pounds: float | None = None
    stock_qty: int | None = Field(ge=0)
    is_bestseller: bool | None = Field(default=False)
    num_of_reviews: int | None = Field(ge=0)
    rating: condecimal(decimal_places=2, ge=0, le=5) | None = Field(default=4)
    genres: List[str] | None = None
    dimensions: List[float] | None = None
