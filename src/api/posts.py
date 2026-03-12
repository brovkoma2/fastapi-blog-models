from fastapi import APIRouter, HTTPException, status
from typing import List
from datetime import datetime

from schemas.posts import PostCreate, PostResponse
from data.storage import storage

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.get("/", response_model=List[PostResponse])
async def get_posts():
    return list(storage.posts.values())


@router.get("/{post_id}", response_model=PostResponse)
async def get_post(post_id: int):
    post = storage.posts.get(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.post("/", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
async def create_post(post_data: PostCreate):
    post_id = storage.get_next_id("posts")
    new_post = {
        "id": post_id,
        "title": post_data.title,
        "text": post_data.text,
        "pub_date": post_data.pub_date or datetime.now(),
        "author_id": post_data.author_id,
        "category_id": post_data.category_id,
        "location_id": post_data.location_id,
        "is_published": True,
        "created_at": datetime.now()
    }

    storage.posts[post_id] = new_post
    return PostResponse.model_validate(new_post)


@router.put("/{post_id}", response_model=PostResponse)
async def update_post(post_id: int, title: str = None, text: str = None):
    post = storage.posts.get(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    if title:
        post["title"] = title
    if text:
        post["text"] = text

    storage.posts[post_id] = post
    return PostResponse.model_validate(post)


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int):
    if post_id not in storage.posts:
        raise HTTPException(status_code=404, detail="Post not found")

    comments_to_delete = [
        cid for cid, c in storage.comments.items()
        if c["post_id"] == post_id
    ]
    for cid in comments_to_delete:
        del storage.comments[cid]

    del storage.posts[post_id]
    return None