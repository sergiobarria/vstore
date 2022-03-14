import enum

from app.database.base_class import Base
from sqlalchemy import ARRAY, Boolean, Column, Enum, Float, Integer, String

from .mixins import Timestamp


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
