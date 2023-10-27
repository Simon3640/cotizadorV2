from app.protocols.db.utils.model import BaseModel


class Buyer(BaseModel):
    email: str | None
    names: str | None
    last_names: str | None
    address: str | None
    age: int | None
    phone: str | None
