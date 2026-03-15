from typing import List
from src.infrastructure.database import database
from src.infrastructure.repositories import UserRepository
from src.schemas.users import UserResponse


class GetUsersUseCase:

    def __init__(self):
        self._repo = UserRepository()
        self._database = database

    def execute(self, skip: int = 0, limit: int = 10) -> List[UserResponse]:
        with self._database.session() as session:
            users = self._repo.get_all(session, skip, limit)
            return [UserResponse.model_validate(user) for user in users]