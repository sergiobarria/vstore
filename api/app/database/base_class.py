from typing import Any
import uuid

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy_utils import UUIDType


@as_declarative()
class Base:
    # Add uuid for postgres db
    # id: uuid.UUID = Column(
    #     UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id: UUIDType = Column(UUIDType(binary=False),
                          primary_key=True, default=uuid.uuid4)
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
