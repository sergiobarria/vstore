from typing import List
from uuid import UUID

from app.models.book import Language
from app.schemas.base import BaseSchema
from pydantic import Field


class BookBase(BaseSchema):
    """This is the description of the base book model"""

    title: str | None = Field(max_length=100)
    summary: str | None = Field(max_length=7000)
    hardcover_price: int | None = Field(ge=0)
    paperback_price: int | None = Field(ge=0)
    language: Language | None = Field(default=Language.english)
    published_year: int | None = Field(ge=0)
    num_of_pages: int | None = Field(ge=0)
    reading_age: int | None = Field(ge=0)
    item_weight_pounds: float | None = Field(ge=0)
    stock_qty: int | None = Field(ge=0)
    is_bestseller: bool | None = Field(default=False)
    dimensions: List[float] | None


class BookCreate(BookBase):
    """Response model for creating a book"""

    title: str
    summary: str
    hardcover_price: int
    paperback_price: int
    language: Language
    published_year: int
    num_of_pages: int
    reading_age: int
    item_weight_pounds: float
    stock_qty: int
    is_bestseller: bool
    dimensions: List[float]


class BookRead(BookBase):
    """Response model for getting a book from DB"""

    id: UUID


class BookUpdate(BookBase):
    """Response model for updating a book"""

    ...
