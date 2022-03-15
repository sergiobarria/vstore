from typing import TYPE_CHECKING

from app.database.base_class import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .mixins import Timestamp

if TYPE_CHECKING:
    from .book import Book, BooksWithAuthors  # noqa: F401


class Author(Timestamp, Base):
    """Author table model"""

    __tablename__ = "authors"

    name = Column(String, unique=True, nullable=False, index=True)
    bio = Column(String, nullable=False)

    books = relationship("Book", secondary="BooksWithAuthors", back_populates="authors")
