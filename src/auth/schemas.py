import uuid
from datetime import datetime
from typing import List

from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    username: str


class UserCreate(schemas.BaseUserCreate):
    username: str
    registered_at: datetime


class UsersRead:
    users: List[UserRead]