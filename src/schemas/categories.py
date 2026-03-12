from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class CategoryBase(BaseModel):
    title: str
    description: str
    slug: str


class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int
    is_published: bool = True
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)