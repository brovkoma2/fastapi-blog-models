from fastapi import APIRouter, HTTPException, status
from typing import List
from datetime import datetime

from schemas.comments import CommentCreate, CommentResponse
from data.storage import storage

router = APIRouter(prefix="/comments", tags=["Comments"])


@router.get("/post/{post_id}", response_model=List[CommentResponse])
async def get_comments_by_post(post_id: int):
    return [
        comment for comment in storage.comments.values()
        if comment["post_id"] == post_id
    ]


@router.post("/", response_model=CommentResponse, status_code=status.HTTP_201_CREATED)
async def create_comment(comment_data: CommentCreate):
    comment_id = storage.get_next_id("comments")
    new_comment = {
        "id": comment_id,
        "text": comment_data.text,
        "post_id": comment_data.post_id,
        "author_id": comment_data.author_id,
        "created_at": datetime.now()
    }

    storage.comments[comment_id] = new_comment
    return CommentResponse.model_validate(new_comment)


@router.delete("/{comment_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_comment(comment_id: int):
    if comment_id not in storage.comments:
        raise HTTPException(status_code=404, detail="Comment not found")

    del storage.comments[comment_id]
    return None