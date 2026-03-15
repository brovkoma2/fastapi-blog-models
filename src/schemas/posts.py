from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class PostBase(BaseModel):
    title: str
    text: str
    pub_date: Optional[datetime] = None
    category_id: int
    location_id: Optional[int] = None


class PostCreate(PostBase):
    author_id: int
    image: Optional[str] = None


class PostResponse(PostBase):
    id: int
    author_id: int
    is_published: bool = True
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)