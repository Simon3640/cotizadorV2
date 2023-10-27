from sqlalchemy import event

from app.infraestructure.db.utils.model import BaseModel
from app.infraestructure.db.models import User
from app.infraestructure.db.utils import session
from app.core.logging import get_logger
from app.core.config import settings
from app.services.crypt import crypt_svc
from app.services import user_svc, product_svc, buyer_svc, sale_product_svc, sale_svc
from app.infraestructure.db.crud import (
    user_crud,
    product_crud,
    buyer_crud,
    sale_product_crud,
    sale_crud,
)

log = get_logger(__name__)


def init_db() -> None:
    """si es una base de datos en memoria se deben generar los esquemas inmediatamente"""

    @event.listens_for(BaseModel.metadata, "after_create")
    def receive_after_create(target, connection, tables, **kw):
        for table in tables:
            log.info("The table " + table.name + " was created")

    @event.listens_for(User.__table__, "after_create")
    def create_admin_user(table, conn, *args, **kwargs):
        db_obj = {
            "email": settings.SUPER_USER_EMAIL,
            "hashed_password": crypt_svc.get_password_hash(
                settings.SUPER_USER_PASSWORD
            ),
            "is_superuser": True,
        }
        conn.execute(table.insert().values(**db_obj))
        log.info(f"Usuarios iniciales creados")

    BaseModel.metadata.create_all(bind=session.engine)
    user_svc.register_observer(user_crud)
    product_svc.register_observer(product_crud)
    buyer_svc.register_observer(buyer_crud)
    sale_product_svc.register_observer(sale_product_crud)
    sale_svc.register_observer(sale_crud)
