from enum import Enum

from app.protocols.db.utils.model import BaseModel
from app.protocols.db.models.sale_product import SaleProduct
from app.protocols.db.models.user import User
from app.protocols.db.models.buyer import Buyer

class SaleStatus(str, Enum):
    PRICE = "PRICE"
    PAID = "PAID"
    CANCELLED = "CANCELLED"
    REMISSION = "REMISSION"


class Sale(BaseModel):
    user_id: int
    buyer_id: int
    status: SaleStatus

    buyer: Buyer
    user: User

    sale_product: SaleProduct