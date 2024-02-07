from pydantic import BaseModel, Field

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


class ProductSearch(BaseModel):
    reference__icontains: str | None = Field(None, alias="reference")
    name__icontains: str | None = Field(None, alias="name")

    class Config:
        allow_population_by_field_name = True