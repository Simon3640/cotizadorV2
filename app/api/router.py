from fastapi import APIRouter

from app.api.routes import ping
from app.api.routes.v1 import user, auth, product, buyer, sale, bucket


api_router = APIRouter()

api_router.include_router(ping.router, tags=["ping"])
api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(product.router, prefix="/product", tags=["product"])
api_router.include_router(buyer.router, prefix="/buyer", tags=["buyer"])
api_router.include_router(sale.router, prefix="/sale", tags=["sale"])
api_router.include_router(bucket.router, prefix="/bucket", tags=["bucket"])