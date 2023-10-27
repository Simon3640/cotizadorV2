from app.protocols.db.utils.model import BaseModel


class Product(BaseModel):
    reference: str
    image: str | None
    name: str | None
    description: str | None
    value: int
