from app.services.base import ServiceBase
from app.schemas.product import (
    ProductUpdate,
    ProductCreate,
    ProductCreate,
)
from app.protocols.db.models.product import Product
from app.protocols.db.crud.product import CRUDProductProtocol


class ProductService(
    ServiceBase[Product, ProductCreate, ProductUpdate, CRUDProductProtocol]
):
    ...


product_svc = ProductService()
