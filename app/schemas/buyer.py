from pydantic import BaseModel

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
