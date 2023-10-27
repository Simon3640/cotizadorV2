from typing import TYPE_CHECKING

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.model import BaseModel

if TYPE_CHECKING:
    from .sale_product import SaleProduct



class Product(BaseModel):
    reference = Column(String(100), unique=True)
    image = Column(String(250), nullable=True)
    name = Column(String(200), nullable=True)
    description = Column(String(100), nullable=True)
    value = Column(Integer, nullable=False)

    sale_product = relationship("SaleProduct", back_populates="product")
