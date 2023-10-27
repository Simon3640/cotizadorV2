from typing import TYPE_CHECKING

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.model import BaseModel

if TYPE_CHECKING:
    from .sale import Sale


class Buyer(BaseModel):
    email = Column(String(100), nullable=True, unique=True)
    names = Column(String(100), nullable=True)
    last_names = Column(String(100), nullable=True)
    address = Column(String(100), nullable=True)
    age = Column(Integer, nullable=True)
    phone = Column(String(14), nullable=True, unique=True)

    sales = relationship("Sale", back_populates="buyer")
