from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models import SaleProduct
from app.schemas.sale_product import SaleProductCreate, SaleProductUpdate


class SaleProductProductCrud(CRUDBase[SaleProduct, SaleProductCreate, SaleProductUpdate]):
    ...


sale_product_crud = SaleProductProductCrud(SaleProduct)
