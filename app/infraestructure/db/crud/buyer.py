from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models import Buyer
from app.schemas.buyer import BuyerCreate, BuyerUpdate


class BuyerCrud(CRUDBase[Buyer, BuyerCreate, BuyerUpdate]):
    ...


buyer_crud = BuyerCrud(Buyer)
