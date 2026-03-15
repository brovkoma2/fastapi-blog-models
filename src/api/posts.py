from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional

from src.schemas.posts import PostCreate, PostResponse
from src.api.depends import (
    get_posts_use_case,
    get_post_by_id_use_case,
    get_create_post_use_case,
    get_update_post_use_case,
    get_delete_post_use_case
)
from src.domain.post.use_cases import (
    GetPostsUseCase,
    GetPostByIdUseCase,
    CreatePostUseCase,
    UpdatePostUseCase,
    DeletePostUseCase
)

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.get("/", response_model=List[PostResponse])
async def get_posts(
    skip: int = 0,
    limit: int = 10,
    use_case: GetPostsUseCase = Depends(get_posts_use_case)
):
    return use_case.execute(skip, limit)


@router.get("/{post_id}", response_model=PostResponse)
async def get_post(
    post_id: int,
    use_case: GetPostByIdUseCase = Depends(get_post_by_id_use_case)
):
    post = use_case.execute(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.post("/", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
async def create_post(
    post_data: PostCreate,
    author_id: int,
    use_case: CreatePostUseCase = Depends(get_create_post_use_case)
):
    try:
        return use_case.execute(post_data, author_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{post_id}", response_model=PostResponse)
async def update_post(
    post_id: int,
    title: Optional[str] = None,
    text: Optional[str] = None,
    category_id: Optional[int] = None,
    location_id: Optional[int] = None,
    use_case: UpdatePostUseCase = Depends(get_update_post_use_case)
):
    try:
        post = use_case.execute(
            post_id,
            title=title,
            text=text,
            category_id=category_id,
            location_id=location_id
        )
        if not post:
            raise HTTPException(status_code=404, detail="Post not found")
        return post
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(
    post_id: int,
    use_case: DeletePostUseCase = Depends(get_delete_post_use_case)
):
    if not use_case.execute(post_id):
        raise HTTPException(status_code=404, detail="Post not found")
    return None