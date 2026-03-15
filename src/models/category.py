from sqlalchemy import Column, Integer, String, Text
from .base import PublishedModel


class Category(PublishedModel):
    __tablename__ = "blog_category"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(256), nullable=False)
    description = Column(Text, nullable=False)
    slug = Column(String(50), unique=True, nullable=False, index=True)