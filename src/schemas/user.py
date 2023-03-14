import uuid
from typing import List

from fastapi_users import schemas
from pydantic import BaseModel


class UserRead(schemas.BaseUser[uuid.UUID]):
    username: str


class UserCreate(schemas.BaseUserCreate):
    username: str


class UsersRead(BaseModel):
    users: List[UserRead]
