from src.domain.post.use_cases import (
    GetPostsUseCase,
    GetPostByIdUseCase,
    CreatePostUseCase,
    UpdatePostUseCase,
    DeletePostUseCase
)
from src.domain.user.use_cases import (
    GetUsersUseCase,
    GetUserByIdUseCase,
    CreateUserUseCase
)
from src.domain.category.use_cases import (
    GetCategoriesUseCase,
    GetCategoryByIdUseCase,
    CreateCategoryUseCase
)
from src.domain.comment.use_cases import (
    GetCommentsByPostUseCase,
    CreateCommentUseCase,
    DeleteCommentUseCase
)


def get_posts_use_case() -> GetPostsUseCase:
    return GetPostsUseCase()


def get_post_by_id_use_case() -> GetPostByIdUseCase:
    return GetPostByIdUseCase()


def get_create_post_use_case() -> CreatePostUseCase:
    return CreatePostUseCase()


def get_update_post_use_case() -> UpdatePostUseCase:
    return UpdatePostUseCase()


def get_delete_post_use_case() -> DeletePostUseCase:
    return DeletePostUseCase()


def get_users_use_case() -> GetUsersUseCase:
    return GetUsersUseCase()


def get_user_by_id_use_case() -> GetUserByIdUseCase:
    return GetUserByIdUseCase()


def get_create_user_use_case() -> CreateUserUseCase:
    return CreateUserUseCase()


def get_categories_use_case() -> GetCategoriesUseCase:
    return GetCategoriesUseCase()


def get_category_by_id_use_case() -> GetCategoryByIdUseCase:
    return GetCategoryByIdUseCase()


def get_create_category_use_case() -> CreateCategoryUseCase:
    return CreateCategoryUseCase()


def get_comments_by_post_use_case() -> GetCommentsByPostUseCase:
    return GetCommentsByPostUseCase()


def get_create_comment_use_case() -> CreateCommentUseCase:
    return CreateCommentUseCase()


def get_delete_comment_use_case() -> DeleteCommentUseCase:
    return DeleteCommentUseCase()