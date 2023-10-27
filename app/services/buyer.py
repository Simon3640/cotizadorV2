from app.services.base import ServiceBase
from app.schemas.buyer import (
    BuyerUpdate,
    BuyerCreate,
    BuyerCreate,
)
from app.protocols.db.models.buyer import Buyer
from app.protocols.db.crud.buyer import CRUDBuyerProtocol


class BuyerService(
    ServiceBase[Buyer, BuyerCreate, BuyerUpdate, CRUDBuyerProtocol]
):
    ...


buyer_svc = BuyerService()
