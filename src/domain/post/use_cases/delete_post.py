from src.infrastructure.database import database
from src.infrastructure.repositories import PostRepository, CommentRepository


class DeletePostUseCase:

    def __init__(self):
        self._repo = PostRepository()
        self._database = database

    def execute(self, post_id: int) -> bool:
        with self._database.session() as session:
            post = self._repo.get_by_id(session, post_id)
            if not post:
                return False

            comment_repo = CommentRepository()
            comments = comment_repo.get_by_post(session, post_id)
            for comment in comments:
                comment_repo.delete(session, comment)

            self._repo.delete(session, post)
            session.commit()
            return True