from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.sale_product import SaleProduct
from app.schemas.sale_product import SaleProductCreate, SaleProductUpdate


class CRUDSaleProductProtocol(CRUDProtocol[SaleProduct, SaleProductCreate, SaleProductUpdate]):
    ...
