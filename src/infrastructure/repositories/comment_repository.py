from typing import List, Optional
from sqlalchemy.orm import Session

from src.models import Comment


class CommentRepository:

    def get_by_id(self, session: Session, comment_id: int) -> Optional[Comment]:
        return session.query(Comment).filter(Comment.id == comment_id).first()

    def get_by_post(self, session: Session, post_id: int) -> List[Comment]:
        return session.query(Comment).filter(Comment.post_id == post_id).all()

    def get_by_author(self, session: Session, author_id: int) -> List[Comment]:
        return session.query(Comment).filter(Comment.author_id == author_id).all()

    def create(self, session: Session, **kwargs) -> Comment:
        comment = Comment(**kwargs)
        session.add(comment)
        session.flush()
        return comment

    def update(self, session: Session, comment: Comment, **kwargs) -> Comment:
        for key, value in kwargs.items():
            if value is not None:
                setattr(comment, key, value)
        return comment

    def delete(self, session: Session, comment: Comment) -> None:
        session.delete(comment)