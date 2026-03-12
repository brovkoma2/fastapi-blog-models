from fastapi import APIRouter, HTTPException, status
from typing import List
from datetime import datetime

from schemas.users import UserCreate, UserResponse
from data.storage import storage

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=List[UserResponse])
async def get_users():
    return list(storage.users.values())


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    user = storage.users.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserCreate):
    user_id = storage.get_next_id("users")
    new_user = {
        "id": user_id,
        "login": user_data.login,
        "email": user_data.email,
        "password": user_data.password,
        "is_active": True,
        "date_joined": datetime.now()
    }

    storage.users[user_id] = new_user
    return UserResponse.model_validate(new_user)