from typing import List
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.crud.base import CRUDBase
from src.models.order import Order
from src.schemas.order import OrderCreate, OrderUpdate


class CRUDOrder(CRUDBase[Order, OrderCreate, OrderUpdate]):
    async def get_user_orders(
            self, user_id: UUID, db: AsyncSession, *, skip: int = 0, limit: int = 5000
    ) -> List[dict]:
        query = select(self.model).filter(self.model.user_id == user_id).order_by(self.model.id).offset(skip).limit(limit)
        result = await db.execute(query)
        return [c.__dict__ for c in result.scalars().all()]


order = CRUDOrder(Order)
