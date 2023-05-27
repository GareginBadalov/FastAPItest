from uuid import UUID

from fastapi import APIRouter, Depends
from fastapi_users.authentication import JWTStrategy
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.auth import current_user, get_jwt_strategy
from src.schemas.user import UsersRead, UserRead
from src.crud.crud_user import UserManager, get_user_manager
from src.db.database import get_async_session

router = APIRouter()


@router.get("/{user_id}", dependencies=[Depends(current_user)], response_model=UserRead)
async def get_specific_user(
        user_id: UUID,
        user_manager: UserManager = Depends(get_user_manager)
):
    user = await user_manager.get(user_id)
    return user


@router.get("/userByToken/{token}", dependencies=[Depends(current_user)], response_model=UserRead)
async def get_specific_user_by_token(
        token: str,
        user_manager: UserManager = Depends(get_user_manager),
        strategy: JWTStrategy = Depends(get_jwt_strategy)
):

    user = await strategy.read_token(token, user_manager)
    return user


@router.get("/", dependencies=[Depends(current_user)], response_model=UsersRead)
async def get_all_users(
        session: AsyncSession = Depends(get_async_session),
        user_manager: UserManager = Depends(get_user_manager)
):
    users = await user_manager.get_all_users(session)
    return UsersRead(users=users)
