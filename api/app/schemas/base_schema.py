from lib2to3.pytree import Base
from pydantic import BaseModel


class BaseSchema(BaseModel):
    class Config(BaseModel.Config):
        orm_mode = True
