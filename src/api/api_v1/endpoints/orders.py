from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src import crud
from src.schemas.order import OrderCreate, UserOrdersResponse, OrderResponse, OrderUpdate
from src.db.database import get_async_session
from src.core.auth import current_user

router = APIRouter()


@router.get("/{order_id}", dependencies=[Depends(current_user)], response_model=OrderResponse)
async def get_specific_order(order_id: UUID, session: AsyncSession = Depends(get_async_session)):
    order = await crud.order.get(session, order_id)
    return order


@router.get("/", dependencies=[Depends(current_user)], response_model=UserOrdersResponse)
async def get_orders(session: AsyncSession = Depends(get_async_session)):
    orders = await crud.order.get_multi(session)
    return UserOrdersResponse(orders=orders)


@router.get("", dependencies=[Depends(current_user)], response_model=UserOrdersResponse)
async def get_user_orders(user_id: str, session: AsyncSession = Depends(get_async_session)):
    user_orders = await crud.order.get_user_orders(user_id, session)
    return UserOrdersResponse(orders=user_orders)


@router.post("/create", dependencies=[Depends(current_user)], response_model=OrderResponse)
async def add_specific_order(new_order: OrderCreate, session: AsyncSession = Depends(get_async_session)):
    new_order = await crud.order.create(db=session, obj_in=new_order)
    return new_order


@router.post("/update/{order_id}", dependencies=[Depends(current_user)], response_model=OrderResponse)
async def update_order(order_id, new_data: OrderUpdate,  session: AsyncSession = Depends(get_async_session)):
    order = await crud.order.get(session, order_id)
    new_order = await crud.order.update(db=session, db_obj=order, obj_in=new_data)
    return new_order


@router.post("/delete/{order_id}", status_code=200, dependencies=[Depends(current_user)])
async def update_order(order_id, session: AsyncSession = Depends(get_async_session)):
    await crud.order.remove(db=session, obj_id=order_id)
    return {"success": True}
