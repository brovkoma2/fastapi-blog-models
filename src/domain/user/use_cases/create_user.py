from src.infrastructure.database import database
from src.infrastructure.repositories import UserRepository
from src.schemas.users import UserCreate, UserResponse


class CreateUserUseCase:

    def __init__(self):
        self._repo = UserRepository()
        self._database = database

    def execute(self, user_data: UserCreate) -> UserResponse:
        with self._database.session() as session:
            if self._repo.get_by_username(session, user_data.username):
                raise ValueError(f"User with username {user_data.username} already exists")

            if self._repo.get_by_email(session, user_data.email):
                raise ValueError(f"User with email {user_data.email} already exists")

            user = self._repo.create(
                session,
                username=user_data.username,
                email=user_data.email,
                password=user_data.password,
                is_active=True
            )
            session.commit()
            return UserResponse.model_validate(user)