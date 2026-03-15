from typing import List, Optional
from sqlalchemy.orm import Session

from src.models import Category


class CategoryRepository:

    def get_all(self, session: Session, skip: int = 0, limit: int = 10) -> List[Category]:
        return session.query(Category).offset(skip).limit(limit).all()

    def get_by_id(self, session: Session, category_id: int) -> Optional[Category]:
        return session.query(Category).filter(Category.id == category_id).first()

    def get_by_slug(self, session: Session, slug: str) -> Optional[Category]:
        return session.query(Category).filter(Category.slug == slug).first()

    def check_slug_unique(self, session: Session, slug: str) -> bool:
        return session.query(Category).filter(Category.slug == slug).first() is None

    def create(self, session: Session, **kwargs) -> Category:
        category = Category(**kwargs)
        session.add(category)
        session.flush()
        return category

    def update(self, session: Session, category: Category, **kwargs) -> Category:
        for key, value in kwargs.items():
            if value is not None:
                setattr(category, key, value)
        return category

    def delete(self, session: Session, category: Category) -> None:
        session.delete(category)