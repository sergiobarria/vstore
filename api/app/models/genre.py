from typing import TYPE_CHECKING

from app.database.base_class import Base
from sqlalchemy import Column, String

from .mixins import Timestamp

# from sqlalchemy.orm import relationship


if TYPE_CHECKING:
    from .book import Book  # noqa: F401


class Genre(Timestamp, Base):
    """Genre Table Model"""

    __tablename__ = "genres"

    name = Column(String, nullable=False, unique=True, index=True)

    # book = relationship("Book", back_populates="genres")
