import uvicorn
from fastapi import FastAPI

from src.core.auth import auth_backend, fastapi_users
from src.schemas.user import UserRead, UserCreate
from src.api.api_v1.api import api_router

app = FastAPI(
    title="Test App"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    api_router
)


if __name__ == '__main__':
    uvicorn.run("src.main:app", host="localhost", log_level="info")
