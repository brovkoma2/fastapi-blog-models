from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api import posts, categories, users, comments


def create_app() -> FastAPI:
    app = FastAPI(
        title="Blogicum API",
        description="API для блог-платформы Blogicum",
        version="1.0.0"
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(posts.router)
    app.include_router(categories.router)
    app.include_router(users.router)
    app.include_router(comments.router)

    return app