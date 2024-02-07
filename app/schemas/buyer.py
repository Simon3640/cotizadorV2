from pydantic import BaseModel, Field

from app.schemas.model import GeneralResponse


class BuyerBase(BaseModel):
    email: str
    names: str | None
    last_names: str | None
    address: str | None
    age: int | None
    phone: str | None


class BuyerCreate(BuyerBase):
    ...


class BuyerUpdate(BuyerBase):
    ...


class BuyerInDB(GeneralResponse, BuyerBase):
    ...


class BuyerSearch(BaseModel):
    names__icontains: str | None = Field(None, alias="names")
    email__icontains: str | None = Field(None, alias="email")
    phone__icontains: str | None = Field(None, alias="phone")

    class Config:
        allow_population_by_field_name = True