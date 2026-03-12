from pydantic import BaseModel, ConfigDict
from datetime import datetime


class CommentBase(BaseModel):
    text: str


class CommentCreate(CommentBase):
    post_id: int
    author_id: int


class CommentResponse(CommentBase):
    id: int
    post_id: int
    author_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)