from fastapi import APIRouter, HTTPException, status
from typing import List
from datetime import datetime

from schemas.categories import CategoryCreate, CategoryResponse
from data.storage import storage

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/", response_model=List[CategoryResponse])
async def get_categories():
    return list(storage.categories.values())


@router.get("/{category_id}", response_model=CategoryResponse)
async def get_category(category_id: int):
    category = storage.categories.get(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
async def create_category(category_data: CategoryCreate):
    category_id = storage.get_next_id("categories")
    new_category = {
        "id": category_id,
        "title": category_data.title,
        "description": category_data.description,
        "slug": category_data.slug,
        "is_published": True,
        "created_at": datetime.now()
    }

    storage.categories[category_id] = new_category
    return CategoryResponse.model_validate(new_category)


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(category_id: int):
    if category_id not in storage.categories:
        raise HTTPException(status_code=404, detail="Category not found")

    del storage.categories[category_id]
    return None