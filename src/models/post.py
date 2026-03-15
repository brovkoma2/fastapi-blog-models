from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from .base import PublishedModel


class Post(PublishedModel):
    __tablename__ = "blog_post"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(256), nullable=False)
    text = Column(Text, nullable=False)
    image = Column(String(256), nullable=False, default='', server_default='')
    pub_date = Column(DateTime(timezone=True), nullable=False)

    author_id = Column(Integer, ForeignKey("auth_user.id", ondelete="CASCADE"), nullable=False)
    location_id = Column(Integer, ForeignKey("blog_location.id", ondelete="SET NULL"))
    category_id = Column(Integer, ForeignKey("blog_category.id", ondelete="SET NULL"), nullable=True)