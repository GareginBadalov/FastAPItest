import uuid
from datetime import datetime

from sqlalchemy import Column, TIMESTAMP, Uuid, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base


class Order(Base):
    __tablename__ = "order"

    id = Column(Uuid, nullable=False, primary_key=True, default=uuid.uuid4)
    user_id = Column(Uuid, ForeignKey("user.id"))
    quantity = Column(Integer, nullable=False)
    amount = Column(Float)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    user = relationship("User", back_populates="orders")
