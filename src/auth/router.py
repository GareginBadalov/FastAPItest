from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.schemas import UserRead
from src.auth.models import User
from src.database import get_async_session

router = APIRouter(
    prefix="/users",
    tags=["User"]
)


@router.get("/{user_id}")
async def get_specific_user(user_id: str, session: AsyncSession = Depends(get_async_session)):
    query = select(User).where(User.id == user_id)
    result = await session.execute(query)
    result = result.scalar()
    return UserRead(username=result.username,
                    id=result.id,
                    email=result.email,
                    is_active=result.is_active,
                    is_superuser=result.is_superuser,
                    is_verified=result.is_verified
                    )


@router.get("/")
async def get_all_users(session: AsyncSession = Depends(get_async_session)):
    query = select(User)
    result = await session.execute(query)
    result = result.scalars().all()
    return [
        UserRead(username=c.username,
                 id=c.id,
                 email=c.email,
                 is_active=c.is_active,
                 is_superuser=c.is_superuser,
                 is_verified=c.is_verified) for c in result]
