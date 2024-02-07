from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


class CRUDProductProtocol(CRUDProtocol[Product, ProductCreate, ProductUpdate]):
    def create_or_update(self, *, product: ProductCreate) -> None:
        ...
