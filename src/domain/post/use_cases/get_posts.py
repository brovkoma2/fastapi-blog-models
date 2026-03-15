from typing import List
from src.infrastructure.database import database
from src.infrastructure.repositories import PostRepository
from src.schemas.posts import PostResponse


class GetPostsUseCase:

    def __init__(self):
        self._repo = PostRepository()
        self._database = database

    def execute(self, skip: int = 0, limit: int = 10) -> List[PostResponse]:
        with self._database.session() as session:
            posts = self._repo.get_all(session, skip, limit)
            return [PostResponse.model_validate(post) for post in posts]