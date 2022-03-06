import enum

from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, Text, Float, Enum
from sqlalchemy.orm import relationship

from app.database.base_class import Base


class Language(enum.Enum):
    english = 1
    spanish = 2


# class Genres(enum.Enum):
#     fantasy =


class BookModel(Base):
    """Base class for the database Book model"""

    __tablename__ = "books"

    # id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False, index=True)
    # summary = Column(String(3000), nullable=False)
    # hardcover_price = Column(Float(asdecimal=True), nullable=True)
    # hardcover_price_discount = Column(Float(asdecimal=True), nullable=True)
    # paperback_price = Column(Float(asdecimal=True), nullable=True)
    # paperback_price_discount = Column(Float(asdecimal=True), nullable=True)
    # language = Column(Enum(Language))
    # year = Column(Integer, nullable=False),
    # genres =

    # Relationships
    # author = None
