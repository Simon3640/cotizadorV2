from fastapi import APIRouter, HTTPException, Depends, Body

from app.schemas.user import UserCreate, UserUpdate, UserInDB, UserSearch
from app.services.user import user_svc
from app.protocols.db.models.user import User
from app.api.middleware.bearer import (
    get_current_active_superempleado,
    get_current_empleado,
)


router = APIRouter()


@router.post("", response_model=UserInDB, status_code=201)
def create_user(
    *, new_user: UserCreate, user: User = Depends(get_current_active_superempleado)
) -> UserInDB:
    """Endpoint to create a new user in db

    Args:
        new_user (UserCreate): Schema

    Returns:
        UserInDB: User in DB schema
    """

    user = user_svc.create(obj_in=new_user)
    return user


@router.get("", response_model=list[UserInDB], status_code=200)
def get_all_user(
    *,
    skip: int = 0,
    limit: int = 10,
    user: User = Depends(get_current_active_superempleado),
    payload: UserSearch = Depends(UserSearch)
) -> list[UserInDB]:
    return user_svc.get_multi(
        skip=skip,
        limit=limit,
        payload=payload.dict(exclude_none=True, exclude_unset=True),
    )


@router.get("/{id}", response_model=UserInDB, status_code=200)
def get_user(*, id: int, user: User = Depends(get_current_empleado)) -> UserInDB:
    if id == 0:
        return user
    user = user_svc.get(id=id)
    if not user:
        raise HTTPException(404, "User not found")
    return user


@router.patch("/{id}", response_model=None)
def update_user(*, obj_in: UserUpdate, id: int) -> None:
    user = user_svc.get(id=id)
    if not user:
        raise HTTPException(404, "User not found")
    user_svc.update(id=id, obj_in=obj_in)
    return None


@router.patch("/new-password/{id}", response_model=None)
def update_password(
    *, password: str, id: int, user: User = Depends(get_current_empleado)
) -> None:
    if user.id != id or not user.is_superuser:
        raise HTTPException(403, "You are not allowed to update this user")
    current_user = user_svc.get(id=id)
    if not current_user:
        raise HTTPException(404, "User not found")
    user_svc.update_password(id=id, password=password)
    return None


@router.delete("/{id}", response_model=None, status_code=204)
def delete_user(*, id: int) -> None:
    user = user_svc.delete(id=id)
    if user == 0:
        raise HTTPException(404, "User not found")
    return None
