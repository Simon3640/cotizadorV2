from app.services.base import ServiceBase
from app.schemas.product import (
    ProductUpdate,
    ProductCreate,
    ProductCreate,
)
from app.protocols.db.models.product import Product
from app.protocols.db.crud.product import CRUDProductProtocol
from app.core.logging import get_logger

log = get_logger(__name__)


class ProductService(
    ServiceBase[Product, ProductCreate, ProductUpdate, CRUDProductProtocol]
):
    def create_or_update(self, *, product: ProductCreate) -> None:
        if self.observer:
            self.observer.create_or_update(product=product)
            log.debug(f"Product {product.reference} created")


product_svc = ProductService()
