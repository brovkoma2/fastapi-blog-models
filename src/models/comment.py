from datetime import datetime
from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from src.infrastructure.database import Base


class Comment(Base):
    __tablename__ = "blog_comment"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.now, server_default=func.now())

    post_id = Column(Integer, ForeignKey("blog_post.id", ondelete="CASCADE"), nullable=False)
    author_id = Column(Integer, ForeignKey("auth_user.id", ondelete="CASCADE"), nullable=False)