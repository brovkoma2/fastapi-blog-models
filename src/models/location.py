from sqlalchemy import Column, Integer, String
from .base import PublishedModel


class Location(PublishedModel):
    __tablename__ = "blog_location"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256), nullable=False)