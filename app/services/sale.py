from app.services.base import ServiceBase
from app.services.sale_product import sale_product_svc
from app.schemas.sale import (
    SaleUpdate,
    SaleCreate,
    SaleCreate,
    SaleProducts,
    SaleResponse,
    SaleStatus,
)
from app.schemas.sale_product import SaleProductCreate
from app.protocols.db.models.sale import Sale
from app.protocols.db.crud.sale import CRUDSaleProtocol
from app.core.exceptions import NoObserverRegister
from app.infraestructure.celery.sale import amqp_observer_sale
from app.infraestructure.db.models.consecutive import consecutive_repo


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
                discount=sale_product.discount,
            )
            sale_product_svc.create(obj_in=obj_create)
        amqp_observer_sale.create(sale=sale)
        return sale

    def update(self, *, id: int, obj_in: SaleUpdate, worker: bool = False) -> Sale:
        sale = self.get(id=id)
        if sale.status == SaleStatus.PAID and not worker:
            raise Exception("Invalid Sale status")
        if obj_in.status == SaleStatus.PAID:
            consecutive = consecutive_repo.get_consecutivo()
            obj_in.consecutive = consecutive
            consecutive_repo.update_consecutivo(consecutive + 1)
        sale = super().update(id=id, obj_in=obj_in)
        if (
            sale.status == SaleStatus.PAID or sale.status == SaleStatus.REMISSION
        ) and not worker:
            amqp_observer_sale.create(sale=sale)
        return sale

    def get(self, *, id: int) -> SaleResponse:
        if not self.observer:
            raise NoObserverRegister(self.__class__.__name__)
        return self.observer.get(id=id)


sale_svc = SaleService()
