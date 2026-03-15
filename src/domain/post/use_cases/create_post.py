from datetime import datetime
from src.infrastructure.database import database
from src.infrastructure.repositories import (
    PostRepository, UserRepository,
    CategoryRepository, LocationRepository
)
from src.schemas.posts import PostCreate, PostResponse


class CreatePostUseCase:

    def __init__(self):
        self._repo = PostRepository()
        self._database = database

    def execute(self, post_data: PostCreate, author_id: int) -> PostResponse:
        with self._database.session() as session:
            user_repo = UserRepository()
            author = user_repo.get_by_id(session, author_id)
            if not author:
                raise ValueError(f"Author with id {author_id} not found")

            category_repo = CategoryRepository()
            category = category_repo.get_by_id(session, post_data.category_id)
            if not category:
                raise ValueError(f"Category with id {post_data.category_id} not found")

            if post_data.location_id:
                location_repo = LocationRepository()
                location = location_repo.get_by_id(session, post_data.location_id)
                if not location:
                    raise ValueError(f"Location with id {post_data.location_id} not found")

            post = self._repo.create(
                session,
                title=post_data.title,
                text=post_data.text,
                pub_date=post_data.pub_date or datetime.now(),
                author_id=author_id,
                category_id=post_data.category_id,
                location_id=post_data.location_id
            )
            session.commit()
            return PostResponse.model_validate(post)