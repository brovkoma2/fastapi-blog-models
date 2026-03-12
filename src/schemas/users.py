from pydantic import BaseModel, ConfigDict
from typing import Optional


class UserBase(BaseModel):
    login: str
    email: str


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    is_active: bool = True

    model_config = ConfigDict(from_attributes=True)