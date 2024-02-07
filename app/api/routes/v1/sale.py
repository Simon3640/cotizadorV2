from typing import Any

from fastapi import APIRouter, HTTPException, Depends, Body

from app.schemas.sale import (
    SaleUpdate,
    SaleInDB,
    SaleProducts,
    SaleResponse,
    SaleMultiResponse,
    Consecutive,
)
from app.services.sale import sale_svc
from app.protocols.db.models.user import User
from app.api.middleware.bearer import get_current_active_empleado
from app.infraestructure.db.models.consecutive import consecutive_repo


router = APIRouter()


@router.post("", response_model=SaleInDB, status_code=201)
def create_sale(
    *,
    new_sale: list[SaleProducts],
    buyer_id: int,
    user: User = Depends(get_current_active_empleado),
) -> SaleInDB:
    """Endpoint to create a new sale in db

    Args:
        new_sale (SaleCreate): Schema

    Returns:
        SaleInDB: Sale in DB schema
    """

    sale = sale_svc.create(obj_in=new_sale, user_id=user.id, buyer_id=buyer_id)
    return sale


@router.get("", response_model=list[SaleMultiResponse], status_code=200)
def get_all_sale(
    *, skip: int = 0, limit: int = 10, user: User = Depends(get_current_active_empleado)
) -> list[SaleMultiResponse]:
    return sale_svc.get_multi(skip=skip, limit=limit, order_by="created_at-")


@router.get("/{id}", response_model=SaleResponse, status_code=200)
def get_sale(
    *,
    id: int,
    # user: User = Depends(get_current_active_empleado)
) -> SaleInDB:
    sale = sale_svc.get(id=id)
    if not sale:
        raise HTTPException(404, "Sale not found")
    return sale


@router.patch("/{id}", response_model=None)
def update_sale(
    *, obj_in: SaleUpdate, id: int, user: User = Depends(get_current_active_empleado)
) -> None:
    sale = sale_svc.get(id=id)
    if not sale:
        raise HTTPException(404, "Sale not found")
    sale_svc.update(id=id, obj_in=obj_in)
    return None


@router.patch("/worker/{id}", response_model=None)
def update_sale(
    *,
    obj_in: SaleUpdate,
    id: int,
) -> None:
    sale = sale_svc.get(id=id)
    if not sale:
        raise HTTPException(404, "Sale not found")
    sale_svc.update(id=id, obj_in=obj_in, worker=True)
    return None


@router.delete("/{id}", response_model=None, status_code=204)
def delete_sale(*, id: int, user: User = Depends(get_current_active_empleado)) -> None:
    sale = sale_svc.delete(id=id)
    if sale == 0:
        raise HTTPException(404, "Sale not found")
    return None


@router.post("/consecutive")
def consecutive(consecutive: Consecutive = Body()):
    consecutive_repo.update_consecutivo(consecutive.consecutive)
    return None
