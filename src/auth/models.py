from datetime import datetime
from typing import List

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.orm import relationship, Mapped

from src.orders.models import Order
from src.database import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    username = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    orders: Mapped[List[Order]] = relationship("Order", back_populates="user")

