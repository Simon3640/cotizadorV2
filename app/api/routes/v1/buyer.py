from fastapi import APIRouter, HTTPException, Depends

from app.schemas.buyer import BuyerCreate, BuyerUpdate, BuyerInDB
from app.services.buyer import buyer_svc
from app.protocols.db.models.user import User
from app.api.middleware.bearer import get_current_active_empleado


router = APIRouter()


@router.post("", response_model=BuyerInDB, status_code=201)
def create_buyer(
    *, new_buyer: BuyerCreate, user: User = Depends(get_current_active_empleado)
) -> BuyerInDB:
    """Endpoint to create a new buyer in db

    Args:
        new_buyer (BuyerCreate): Schema

    Returns:
        BuyerInDB: Buyer in DB schema
    """

    buyer = buyer_svc.create(obj_in=new_buyer)
    return buyer


@router.get("", response_model=list[BuyerInDB], status_code=200)
def get_all_buyer(
    *, skip: int = 0, limit: int = 10, user: User = Depends(get_current_active_empleado)
) -> list[BuyerInDB]:
    return buyer_svc.get_multi(skip=skip, limit=limit)


@router.get("/{id}", response_model=BuyerInDB, status_code=200)
def get_buyer(
    *, id: int, user: User = Depends(get_current_active_empleado)
) -> BuyerInDB:
    buyer = buyer_svc.get(id=id)
    if not buyer:
        raise HTTPException(404, "Buyer not found")
    return buyer


@router.patch("/{id}", response_model=None)
def update_buyer(
    *, obj_in: BuyerUpdate, id: int, user: User = Depends(get_current_active_empleado)
) -> None:
    buyer = buyer_svc.get(id=id)
    if not buyer:
        raise HTTPException(404, "Buyer not found")
    buyer_svc.update(id=id, obj_in=obj_in)
    return None


@router.delete("/{id}", response_model=None, status_code=204)
def delete_buyer(*, id: int, user: User = Depends(get_current_active_empleado)) -> None:
    buyer = buyer_svc.delete(id=id)
    if buyer == 0:
        raise HTTPException(404, "Buyer not found")
    return None
