from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.model import BaseModel

if TYPE_CHECKING:
    from .product import Product
    from .sale import Sale


class SaleProduct(BaseModel):
    tax = Column(Integer, nullable=True, default=0)
    total = Column(Integer, nullable=False, default=1)
    discount = Column(Integer, nullable=False, default=0)
    
    product_id = Column(Integer, ForeignKey("product.id"))
    product = relationship("Product", back_populates="sale_product")
    sale_id = Column(Integer, ForeignKey("sale.id"))
    sale = relationship("Sale", back_populates="sale_product")
