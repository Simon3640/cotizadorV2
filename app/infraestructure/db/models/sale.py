from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, ForeignKey, Enum, String
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.model import BaseModel
from app.schemas.sale import SaleStatus

if TYPE_CHECKING:
    from .buyer import Buyer
    from .user import User
    from .sale_product import SaleProduct


class Sale(BaseModel):
    buyer_id = Column(Integer, ForeignKey("buyer.id"))
    buyer = relationship("Buyer", back_populates="sales")
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="sales")

    status = Column(Enum(SaleStatus), default=SaleStatus.PRICE)
    consecutive = Column(Integer, nullable=True)
    document = Column(String, nullable=True)


    sale_product = relationship("SaleProduct", back_populates="sale")
