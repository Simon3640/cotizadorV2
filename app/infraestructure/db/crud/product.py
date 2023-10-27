from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models import Product
from app.schemas.product import ProductCreate, ProductUpdate


class ProductCrud(CRUDBase[Product, ProductCreate, ProductUpdate]):
    ...


product_crud = ProductCrud(Product)
