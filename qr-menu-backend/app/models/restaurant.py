from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.base import Base


class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    qr_code_url = Column(String, nullable=False)

    tables = relationship(
        "Table",
        back_populates="restaurant"
    )