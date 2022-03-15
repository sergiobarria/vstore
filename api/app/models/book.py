import enum
from typing import TYPE_CHECKING

from app.database.base_class import Base
from sqlalchemy import ARRAY, Boolean, Column, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .mixins import Timestamp

# from sqlalchemy.dialects.postgresql import UUID


if TYPE_CHECKING:
    from .author import Author  # noqa: F401
    from .genre import Genre  # noqa: F401


class BooksWithAuthors(Base):
    """Association table for Books and Authors"""

    book_id = Column(ForeignKey("books.id"), primary_key=True)
    author_id = Column(ForeignKey("authors.id"), primary_key=True)


class Language(str, enum.Enum):
    english = "english"
    spanish = "spanish"


class Book(Timestamp, Base):
    """Book table model"""

    __tablename__ = "books"

    title = Column(String, nullable=False, unique=True, index=True)
    summary = Column(String, nullable=False)
    hardcover_price = Column(Integer, nullable=True)
    paperback_price = Column(Integer, nullable=True)
    language = Column(Enum(Language))
    published_year = Column(Integer, nullable=False)
    num_of_pages = Column(Integer, nullable=False)
    reading_age = Column(Integer, nullable=True)
    item_weight_pounds = Column(Float, nullable=False)
    stock_qty = Column(Integer, nullable=False)
    is_bestseller = Column(Boolean, default=False)
    dimensions = Column(ARRAY(Float), nullable=False)
    # author_id = Column(UUID(as_uuid=True), ForeignKey("authors.id"))

    authors = relationship(
        "Author", secondary="BooksWithAuthors", back_populates="books"
    )
    # author = relationship("Author", back_populates="books")
    # genres = relationship("Genre", back_populates="book")
