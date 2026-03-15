from src.infrastructure.database import database
from src.infrastructure.repositories import PostRepository, UserRepository, CommentRepository
from src.schemas.comments import CommentCreate, CommentResponse


class CreateCommentUseCase:

    def __init__(self):
        self._repo = CommentRepository()
        self._database = database

    def execute(self, comment_data: CommentCreate, author_id: int) -> CommentResponse:
        with self._database.session() as session:
            post_repo = PostRepository()
            post = post_repo.get_by_id(session, comment_data.post_id)
            if not post:
                raise ValueError(f"Post with id {comment_data.post_id} not found")

            user_repo = UserRepository()
            author = user_repo.get_by_id(session, author_id)
            if not author:
                raise ValueError(f"Author with id {author_id} not found")

            comment = self._repo.create(
                session,
                text=comment_data.text,
                post_id=comment_data.post_id,
                author_id=author_id
            )
            session.commit()
            return CommentResponse.model_validate(comment)