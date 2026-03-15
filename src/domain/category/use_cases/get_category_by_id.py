from typing import Optional
from src.infrastructure.database import database
from src.infrastructure.repositories import CategoryRepository
from src.schemas.categories import CategoryResponse


class GetCategoryByIdUseCase:

    def __init__(self):
        self._repo = CategoryRepository()
        self._database = database

    def execute(self, category_id: int) -> Optional[CategoryResponse]:
        with self._database.session() as session:
            category = self._repo.get_by_id(session, category_id)
            return CategoryResponse.model_validate(category) if category else None