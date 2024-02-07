from fastapi import APIRouter, HTTPException, Depends, UploadFile, BackgroundTasks

from app.schemas.product import ProductCreate, ProductUpdate, ProductInDB, ProductSearch
from app.services.product import product_svc
from app.protocols.db.models.user import User
from app.api.middleware.bearer import get_current_active_empleado
from app.utils.background_tasks import register_products_from


router = APIRouter()


@router.post("", response_model=ProductInDB, status_code=201)
def create_product(
    *, new_product: ProductCreate, user: User = Depends(get_current_active_empleado)
) -> ProductInDB:
    """Endpoint to create a new product in db

    Args:
        new_product (ProductCreate): Schema

    Returns:
        ProductInDB: Product in DB schema
    """

    product = product_svc.create(obj_in=new_product)
    return product


@router.get("", response_model=list[ProductInDB], status_code=200)
def get_all_product(
    *,
    skip: int = 0,
    limit: int = 10,
    user: User = Depends(get_current_active_empleado),
    payload: ProductSearch = Depends(ProductSearch)
) -> list[ProductInDB]:
    return product_svc.get_multi(
        skip=skip,
        limit=limit,
        payload=payload.dict(exclude_none=True),
        order_by="id-",
    )


@router.get("/{id}", response_model=ProductInDB, status_code=200)
def get_product(
    *, id: int, user: User = Depends(get_current_active_empleado)
) -> ProductInDB:
    product = product_svc.get(id=id)
    if not product:
        raise HTTPException(404, "Product not found")
    return product


@router.patch("/{id}", response_model=None)
def update_product(
    *, obj_in: ProductUpdate, id: int, user: User = Depends(get_current_active_empleado)
) -> None:
    product = product_svc.get(id=id)
    if not product:
        raise HTTPException(404, "Product not found")
    product_svc.update(id=id, obj_in=obj_in)
    return None


@router.delete("/{id}", response_model=None, status_code=204)
def delete_product(
    *, id: int, user: User = Depends(get_current_active_empleado)
) -> None:
    product = product_svc.delete(id=id)
    if product == 0:
        raise HTTPException(404, "Product not found")
    return None


@router.post("/csv")
def upload_csv(
    file: UploadFile,
    background_task: BackgroundTasks,
    user: User = Depends(get_current_active_empleado),
):
    background_task.add_task(register_products_from, file.file)
    return None