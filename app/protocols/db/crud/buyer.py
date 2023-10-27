from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.buyer import Buyer
from app.schemas.buyer import BuyerCreate, BuyerUpdate


class CRUDBuyerProtocol(CRUDProtocol[Buyer, BuyerCreate, BuyerUpdate]):
    ...
