from app.services.base import ServiceBase
from app.services.sale_product import sale_product_svc
from app.schemas.sale import (
    SaleUpdate,
    SaleCreate,
    SaleCreate,
    SaleProducts,
    SaleResponse,
)
from app.schemas.sale_product import SaleProductCreate
from app.protocols.db.models.sale import Sale
from app.protocols.db.crud.sale import CRUDSaleProtocol
from app.core.exceptions import NoObserverRegister


class SaleService(ServiceBase[Sale, SaleCreate, SaleUpdate, CRUDSaleProtocol]):
    def create(
        self, *, obj_in: list[SaleProducts], user_id: int, buyer_id: int
    ) -> Sale:
        sale_create = SaleCreate(user_id=user_id, buyer_id=buyer_id)
        sale = super().create(obj_in=sale_create)
        for sale_product in obj_in:
            obj_create = SaleProductCreate(
                sale_id=sale.id,
                product_id=sale_product.product_id,
                total=sale_product.total,
                tax=sale_product.tax,
            )
            sale_product_svc.create(obj_in=obj_create)
        return sale

    def get(self, *, id: int) -> SaleResponse:
        if not self.observer:
            raise NoObserverRegister(self.__class__.__name__)
        return self.observer.get(id=id)


sale_svc = SaleService()
