from typing import Optional
from src.infrastructure.database import database
from src.infrastructure.repositories import PostRepository
from src.schemas.posts import PostResponse


class GetPostByIdUseCase:

    def __init__(self):
        self._repo = PostRepository()
        self._database = database

    def execute(self, post_id: int) -> Optional[PostResponse]:
        with self._database.session() as session:
            post = self._repo.get_by_id(session, post_id)
            return PostResponse.model_validate(post) if post else None