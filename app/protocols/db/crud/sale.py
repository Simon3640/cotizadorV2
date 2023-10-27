from typing import Any
from datetime import date

from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.sale import Sale
from app.schemas.sale import SaleCreate, SaleUpdate, SaleResponse, SaleMultiResponse


class CRUDSaleProtocol(CRUDProtocol[Sale, SaleCreate, SaleUpdate]):
    def get(self, *, id: int) -> SaleResponse:
        ...

    def get_multi(
        self,
        *,
        payload: dict[str, Any] | None = None,
        skip: int = 0,
        limit: int = 10,
        order_by: str | None = None,
        date_range: dict[str, date] | None = None,
        values: tuple[str] | None = None
    ) -> list[SaleMultiResponse]:
        ...
