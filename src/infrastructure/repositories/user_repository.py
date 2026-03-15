from typing import List, Optional
from sqlalchemy.orm import Session

from src.models import User


class UserRepository:

    def get_all(self, session: Session, skip: int = 0, limit: int = 10) -> List[User]:
        return session.query(User).offset(skip).limit(limit).all()

    def get_by_id(self, session: Session, user_id: int) -> Optional[User]:
        return session.query(User).filter(User.id == user_id).first()

    def get_by_username(self, session: Session, username: str) -> Optional[User]:
        return session.query(User).filter(User.username == username).first()

    def get_by_email(self, session: Session, email: str) -> Optional[User]:
        return session.query(User).filter(User.email == email).first()

    def create(self, session: Session, **kwargs) -> User:
        user = User(**kwargs)
        session.add(user)
        session.flush()
        return user

    def update(self, session: Session, user: User, **kwargs) -> User:
        for key, value in kwargs.items():
            if value is not None:
                setattr(user, key, value)
        return user

    def delete(self, session: Session, user: User) -> None:
        session.delete(user)