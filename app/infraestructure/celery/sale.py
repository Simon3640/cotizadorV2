from typing import TypeVar

from app.protocols.db.models.sale import Sale
from app.infraestructure.celery.celery_app import celery_app, WORKER_ENVIRONMENT

ModelType = TypeVar("ModelType")


class AMQPObserverSale:
    def create(self, *, sale: Sale) -> None:
        celery_app.send_task(
            name="sale", args=[sale.id], queue=f"cotizadorV2-sale{WORKER_ENVIRONMENT}"
        )



amqp_observer_sale = AMQPObserverSale()
