from sqlalchemy.exc import IntegrityError

from app.infraestructure.db.utils.session import SessionLocal
from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models import Product
from app.schemas.product import ProductCreate, ProductUpdate
from app.core.exceptions import ORMError


class ProductCrud(CRUDBase[Product, ProductCreate, ProductUpdate]):
    def create_or_update(self, *, product: ProductCreate) -> None:
        with SessionLocal() as db:
            try:
                existing_pruduct = (
                    db.query(Product).filter_by(reference=product.reference).first()
                )
                if existing_pruduct:
                    existing_pruduct.name = product.name
                    existing_pruduct.value = product.value
                    print(f"Product {product.reference} updated")
                else:
                    new_product = Product(**product.dict())
                    db.add(new_product)
                db.commit()
            except IntegrityError as e:
                raise ORMError(str(e))


product_crud = ProductCrud(Product)
