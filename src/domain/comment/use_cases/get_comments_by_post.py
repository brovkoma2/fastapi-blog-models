from typing import List
from src.infrastructure.database import database
from src.infrastructure.repositories import PostRepository, CommentRepository
from src.schemas.comments import CommentResponse


class GetCommentsByPostUseCase:

    def __init__(self):
        self._repo = CommentRepository()
        self._database = database

    def execute(self, post_id: int) -> List[CommentResponse]:
        with self._database.session() as session:
            post_repo = PostRepository()
            post = post_repo.get_by_id(session, post_id)
            if not post:
                raise ValueError(f"Post with id {post_id} not found")

            comments = self._repo.get_by_post(session, post_id)
            return [CommentResponse.model_validate(c) for c in comments]