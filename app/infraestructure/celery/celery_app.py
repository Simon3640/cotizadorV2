from celery import Celery

from app.core.config import settings



CELERY_BROKER = f"{settings.AMQP_DSN}"
SCHEDULE_TIME = settings.SCHEDULE_TIME


WORKER_ENVIRONMENT = "" if settings.ENVIRONMENT == "prod" else "-dev"


celery_config = {
    "broker_url": CELERY_BROKER,
    "task_ignore_result": True,
    "result_expires": 7200,  # in secs
    "worker_prefetch_multiplier": 1,
}


celery_app = Celery("worker", config_source=celery_config)

celery_app.conf.task_routes = {
    "app.workers.sale.sale": {
        "queue": f"cotizadorV2-sale{WORKER_ENVIRONMENT}"
    }
}

celery_app.conf.update(
    task_track_started=True,
    accept_content=["json"],
)

