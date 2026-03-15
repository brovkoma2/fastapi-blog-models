from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from src.schemas.categories import CategoryCreate, CategoryResponse
from src.api.depends import (
    get_categories_use_case,
    get_category_by_id_use_case,
    get_create_category_use_case
)
from src.domain.category.use_cases import (
    GetCategoriesUseCase,
    GetCategoryByIdUseCase,
    CreateCategoryUseCase
)

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/", response_model=List[CategoryResponse])
async def get_categories(
    skip: int = 0,
    limit: int = 10,
    use_case: GetCategoriesUseCase = Depends(get_categories_use_case)
):
    return use_case.execute(skip, limit)


@router.get("/{category_id}", response_model=CategoryResponse)
async def get_category(
    category_id: int,
    use_case: GetCategoryByIdUseCase = Depends(get_category_by_id_use_case)
):
    category = use_case.execute(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
async def create_category(
    category_data: CategoryCreate,
    use_case: CreateCategoryUseCase = Depends(get_create_category_use_case)
):
    try:
        return use_case.execute(category_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))