from datetime import date
from typing import Any

from sqlalchemy import desc

from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models import Sale
from app.infraestructure.db.utils.session import SessionLocal
from app.schemas.sale import SaleCreate, SaleUpdate, SaleResponse, SaleMultiResponse


class SaleCrud(CRUDBase[Sale, SaleCreate, SaleUpdate]):
    def get(self, *, id: int) -> SaleResponse:
        with SessionLocal() as db:
            sale = db.query(Sale).filter(Sale.id == id).first()
            return SaleResponse.from_orm(sale)

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
        with SessionLocal() as db:
            sales = (
                db.query(Sale)
                .order_by(desc(Sale.created_at))
                .offset(skip)
                .limit(limit)
                .all()
            )
            sales_response = []
            for sale in sales:
                sales_response.append(SaleMultiResponse.from_orm(sale))
            return sales_response


sale_crud = SaleCrud(Sale)
