from pydantic import BaseModel, EmailStr

from app.schemas.model import GeneralResponse


class ProductBase(BaseModel):
    reference: str
    image: str | None
    name: str | None
    description: str | None
    value: int


class ProductCreate(ProductBase):
    ...


class ProductUpdate(BaseModel):
    reference: str | None
    image: str | None
    name: str | None
    description: str | None
    value: int | None


class ProductInDB(GeneralResponse, ProductBase):
    ...
