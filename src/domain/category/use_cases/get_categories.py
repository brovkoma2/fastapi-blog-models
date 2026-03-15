from typing import List
from src.infrastructure.database import database
from src.infrastructure.repositories import CategoryRepository
from src.schemas.categories import CategoryResponse


class GetCategoriesUseCase:

    def __init__(self):
        self._repo = CategoryRepository()
        self._database = database

    def execute(self, skip: int = 0, limit: int = 10) -> List[CategoryResponse]:
        with self._database.session() as session:
            categories = self._repo.get_all(session, skip, limit)
            return [CategoryResponse.model_validate(cat) for cat in categories]