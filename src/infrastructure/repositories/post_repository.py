from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import desc

from src.models import Post


class PostRepository:

    def get_all(self, session: Session, skip: int = 0, limit: int = 10) -> List[Post]:
        return session.query(Post).order_by(desc(Post.pub_date)).offset(skip).limit(limit).all()

    def get_by_id(self, session: Session, post_id: int) -> Optional[Post]:
        return session.query(Post).filter(Post.id == post_id).first()

    def get_by_author(self, session: Session, author_id: int) -> List[Post]:
        return session.query(Post).filter(Post.author_id == author_id).all()

    def get_by_category(self, session: Session, category_id: int) -> List[Post]:
        return session.query(Post).filter(Post.category_id == category_id).all()

    def create(self, session: Session, **kwargs) -> Post:
        post = Post(**kwargs)
        session.add(post)
        session.flush()
        return post

    def update(self, session: Session, post: Post, **kwargs) -> Post:
        for key, value in kwargs.items():
            if value is not None:
                setattr(post, key, value)
        return post

    def delete(self, session: Session, post: Post) -> None:
        session.delete(post)