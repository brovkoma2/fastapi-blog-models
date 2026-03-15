from typing import Optional
from src.infrastructure.database import database
from src.infrastructure.repositories import UserRepository
from src.schemas.users import UserResponse


class GetUserByIdUseCase:

    def __init__(self):
        self._repo = UserRepository()
        self._database = database

    def execute(self, user_id: int) -> Optional[UserResponse]:
        with self._database.session() as session:
            user = self._repo.get_by_id(session, user_id)
            return UserResponse.model_validate(user) if user else None