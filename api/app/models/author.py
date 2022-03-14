from app.database.base_class import Base
from sqlalchemy import Column, String

from .mixins import Timestamp


class Author(Timestamp, Base):
    """Author table model"""

    __tablename__ = "authors"

    name = Column(String, unique=True, nullable=False, index=True)
    bio = Column(String, nullable=False)
