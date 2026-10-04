from datetime import datetime

from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship

from app.database.base import Base
from app.models.enums import OrderStatus


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    status = Column(
        Enum(OrderStatus),
        nullable=False,
        default=OrderStatus.PENDING
    )

    total_price = Column(Float, nullable=False)

    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    restaurant_id = Column(
        Integer,
        ForeignKey("restaurants.id"),
        nullable=False
    )

    table_id = Column(
        Integer,
        ForeignKey("tables.id"),
        nullable=False
    )

    restaurant = relationship(
        "Restaurant",
        back_populates="orders"
    )