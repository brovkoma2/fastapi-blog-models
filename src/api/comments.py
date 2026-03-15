from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from src.schemas.comments import CommentCreate, CommentResponse
from src.api.depends import (
    get_comments_by_post_use_case,
    get_create_comment_use_case,
    get_delete_comment_use_case
)
from src.domain.comment.use_cases import (
    GetCommentsByPostUseCase,
    CreateCommentUseCase,
    DeleteCommentUseCase
)

router = APIRouter(prefix="/comments", tags=["Comments"])


@router.get("/post/{post_id}", response_model=List[CommentResponse])
async def get_comments_by_post(
    post_id: int,
    use_case: GetCommentsByPostUseCase = Depends(get_comments_by_post_use_case)
):
    try:
        return use_case.execute(post_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/", response_model=CommentResponse, status_code=status.HTTP_201_CREATED)
async def create_comment(
    comment_data: CommentCreate,
    author_id: int,
    use_case: CreateCommentUseCase = Depends(get_create_comment_use_case)
):
    try:
        return use_case.execute(comment_data, author_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{comment_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_comment(
    comment_id: int,
    use_case: DeleteCommentUseCase = Depends(get_delete_comment_use_case)
):
    if not use_case.execute(comment_id):
        raise HTTPException(status_code=404, detail="Comment not found")
    return None