from sqlalchemy import Column, Integer, Boolean, ForeignKey

from app.database.base import Base


class Table(Base):
    __tablename__ = "tables"

    id = Column(Integer, primary_key=True, index=True)
    table_number = Column(Integer, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)

    restaurant_id = Column(
        Integer,
        ForeignKey("restaurants.id"),
        nullable=False
    )