from app.protocols.db.utils.model import BaseModel


class SaleProduct(BaseModel):
    sale_id: int
    product_id: int
    tax: int
    total: int
    discount: int
