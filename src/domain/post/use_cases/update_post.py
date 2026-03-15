from typing import Optional
from src.infrastructure.database import database
from src.infrastructure.repositories import PostRepository, CategoryRepository, LocationRepository
from src.schemas.posts import PostResponse


class UpdatePostUseCase:

    def __init__(self):
        self._repo = PostRepository()
        self._database = database

    def execute(
            self,
            post_id: int,
            title: str = None,
            text: str = None,
            category_id: int = None,
            location_id: int = None
    ) -> Optional[PostResponse]:
        with self._database.session() as session:
            post = self._repo.get_by_id(session, post_id)
            if not post:
                return None

            if category_id is not None:
                category_repo = CategoryRepository()
                category = category_repo.get_by_id(session, category_id)
                if not category:
                    raise ValueError(f"Category with id {category_id} not found")

            if location_id is not None:
                location_repo = LocationRepository()
                location = location_repo.get_by_id(session, location_id)
                if not location:
                    raise ValueError(f"Location with id {location_id} not found")

            update_data = {}
            if title is not None:
                update_data["title"] = title
            if text is not None:
                update_data["text"] = text
            if category_id is not None:
                update_data["category_id"] = category_id
            if location_id is not None:
                update_data["location_id"] = location_id

            self._repo.update(session, post, **update_data)
            session.commit()
            return PostResponse.model_validate(post)