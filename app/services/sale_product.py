from app.services.base import ServiceBase
from app.schemas.sale_product import (
    SaleProductUpdate,
    SaleProductCreate,
    SaleProductCreate,
)
from app.protocols.db.models.sale_product import SaleProduct
from app.protocols.db.crud.sale_product import CRUDSaleProductProtocol


class SaleProductService(
    ServiceBase[SaleProduct, SaleProductCreate, SaleProductUpdate, CRUDSaleProductProtocol]
):
    ...


sale_product_svc = SaleProductService()
