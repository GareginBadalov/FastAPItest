from datetime import datetime
from typing import List
from uuid import uuid4

from pydantic import BaseModel, UUID4, Field


class OrderCreate(BaseModel):
    user_id: UUID4
    quantity: int
    amount: int


class OrderResponse(BaseModel):
    id: UUID4 = Field(default_factory=uuid4)
    user_id: UUID4
    quantity: int
    amount: int
    created_at: datetime = Field(default_factory=datetime.utcnow)


class UserOrdersResponse(BaseModel):
    orders: List[OrderResponse]
