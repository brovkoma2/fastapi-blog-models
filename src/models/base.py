from datetime import datetime
from sqlalchemy import Column, Boolean, DateTime
from src.infrastructure.database import Base


class PublishedModel(Base):
    __abstract__ = True

    is_published = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now)