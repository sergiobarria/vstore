from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr | None = None
    is_active: bool | None = True
    is_superuser: bool = False
    first_name: str | None = None
    last_namte: str | None = None


class UserCreate(UserBase):
    email: EmailStr
    password: str
