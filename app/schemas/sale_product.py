from typing import Any

from pydantic import BaseModel

from app.schemas.model import GeneralResponse
from app.schemas.product import ProductBase


class SaleProductBase(BaseModel):
    sale_id: int
    product_id: int
    total: int
    tax: int


class SaleProductCreate(SaleProductBase):
    ...


class SaleProductUpdate(SaleProductBase):
    ...


class SaleProductInDB(GeneralResponse, SaleProductBase):
    ...


class SaleProductResponse(SaleProductInDB):
    product: Any
