from src.infrastructure.database import database
from src.infrastructure.repositories import CommentRepository


class DeleteCommentUseCase:

    def __init__(self):
        self._repo = CommentRepository()
        self._database = database

    def execute(self, comment_id: int) -> bool:
        with self._database.session() as session:
            comment = self._repo.get_by_id(session, comment_id)
            if not comment:
                return False

            self._repo.delete(session, comment)
            session.commit()
            return True