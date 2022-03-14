from app.database.base_class import Base
from sqlalchemy import Column, String

from .mixins import Timestamp


class Genre(Timestamp, Base):
    """Genre Table Model"""

    __tablename__ = "genres"

    name = Column(String, nullable=False, unique=True, index=True)
