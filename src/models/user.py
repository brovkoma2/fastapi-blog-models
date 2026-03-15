from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from src.infrastructure.database import Base


class User(Base):
    __tablename__ = "auth_user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(150), unique=True, nullable=False, index=True)
    email = Column(String(254), unique=True, nullable=False, index=True)
    first_name = Column(String(150), default='', server_default='')
    last_name = Column(String(150), default='', server_default='')
    password = Column(String(128), nullable=False)
    is_active = Column(Boolean, default=True)
    date_joined = Column(DateTime(timezone=True), nullable=False, default=datetime.now, server_default=func.now())
    is_superuser = Column(Boolean, nullable=False, default=False, server_default='0')
    is_staff = Column(Boolean, nullable=False, default=False, server_default='0')