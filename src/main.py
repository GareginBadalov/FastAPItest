import uvicorn
from fastapi import FastAPI

from src.auth.base_config import auth_backend, fastapi_users
from src.auth.schemas import UserRead, UserCreate
from src.orders.router import router as router_orders
from src.auth.router import router as router_users

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
    router_orders
)

app.include_router(
    router_users
)


if __name__ == '__main__':
    uvicorn.run("src.main:app", host="localhost", log_level="info")
