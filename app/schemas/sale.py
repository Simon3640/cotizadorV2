from enum import Enum

from pydantic import BaseModel, validator

from app.schemas.model import GeneralResponse
from app.schemas.sale_product import SaleProductResponse
from app.schemas.user import UserInDB
from app.schemas.buyer import BuyerInDB
from app.utils.sale_product import total_from, total_tax_from


class SaleStatus(str, Enum):
    PRICE = "PRICE"
    PAID = "PAID"
    CANCELLED = "CANCELLED"
    REMISSION = "REMISSION"


class SaleBase(BaseModel):
    user_id: int
    buyer_id: int
    status: SaleStatus | None = SaleStatus.PRICE


class SaleCreate(SaleBase):
    ...


class SaleUpdate(BaseModel):
    user_id: int | None
    buyer_id: int | None
    status: SaleStatus | None


class SaleInDB(GeneralResponse, SaleBase):
    ...


class SaleProducts(BaseModel):
    product_id: int
    total: int
    tax: int


class SaleMultiResponse(SaleInDB):
    user: UserInDB
    buyer: BuyerInDB


class SaleResponse(SaleInDB):
    sale_product: list[SaleProductResponse]

    total: float | None

    @validator("total")
    def total_sale(cls, value, values):
        return total_from(values["sale_product"])

    total_tax: float | None

    @validator("total_tax")
    def total_tax_sale(cls, value, values):
        return total_tax_from(values["sale_product"])
