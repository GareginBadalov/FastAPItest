from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.orders.schemas import OrderCreate, UserOrdersResponse, OrderResponse
from src.database import get_async_session
from src.orders.models import Order

router = APIRouter(
    prefix="/orders",
    tags=["Order"]
)


@router.get("/{order_id}")
async def get_specific_order(order_id: str, session: AsyncSession = Depends(get_async_session)):
    query = select(Order).where(Order.id == order_id)
    result = await session.execute(query)
    result = result.scalar()
    return OrderResponse(
        id=result.id,
        user_id=result.user_id,
        quantity=result.quantity,
        amount=result.amount,
        created_at=result.created_at
    )


@router.get("/")
async def get_orders(session: AsyncSession = Depends(get_async_session)):
    query = select(Order)
    result = await session.execute(query)
    response = [
        OrderResponse(
            id=c.id,
            user_id=c.user_id,
            quantity=c.quantity,
            amount=c.amount,
            created_at=c.created_at
        ) for c in result.scalars().all()]
    return UserOrdersResponse(orders=response)


@router.get("")
async def get_user_orders(user_id: str, session: AsyncSession = Depends(get_async_session)):
    query = select(Order).where(Order.user_id == user_id)
    result = await session.execute(query)
    response = [
        OrderResponse(
            id=c.id,
            user_id=c.user_id,
            quantity=c.quantity,
            amount=c.amount,
            created_at=c.created_at
        ) for c in result.scalars().all()]
    return UserOrdersResponse(orders=response)


@router.post("/createOrder")
async def add_specific_order(new_order: OrderCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Order).values(**new_order.dict())
    await session.execute(stmt)
    await session.commit()
    return OrderResponse(**new_order.dict())
