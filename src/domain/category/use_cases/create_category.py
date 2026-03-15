from src.infrastructure.database import database
from src.infrastructure.repositories import CategoryRepository
from src.schemas.categories import CategoryCreate, CategoryResponse


class CreateCategoryUseCase:

    def __init__(self):
        self._repo = CategoryRepository()
        self._database = database

    def execute(self, category_data: CategoryCreate) -> CategoryResponse:
        with self._database.session() as session:
            if not self._repo.check_slug_unique(session, category_data.slug):
                raise ValueError(f"Category with slug {category_data.slug} already exists")

            category = self._repo.create(
                session,
                title=category_data.title,
                description=category_data.description,
                slug=category_data.slug,
                is_published=True
            )
            session.commit()
            return CategoryResponse.model_validate(category)