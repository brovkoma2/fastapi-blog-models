from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from src.schemas.users import UserCreate, UserResponse
from src.api.depends import (
    get_users_use_case,
    get_user_by_id_use_case,
    get_create_user_use_case
)
from src.domain.user.use_cases import (
    GetUsersUseCase,
    GetUserByIdUseCase,
    CreateUserUseCase
)

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=List[UserResponse])
async def get_users(
    skip: int = 0,
    limit: int = 10,
    use_case: GetUsersUseCase = Depends(get_users_use_case)
):
    return use_case.execute(skip, limit)


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: int,
    use_case: GetUserByIdUseCase = Depends(get_user_by_id_use_case)
):
    user = use_case.execute(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_data: UserCreate,
    use_case: CreateUserUseCase = Depends(get_create_user_use_case)
):
    try:
        return use_case.execute(user_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))