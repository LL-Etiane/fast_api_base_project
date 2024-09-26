from celery import Celery
from app.settings import CELERY_BROKER_URL, CELERY_RESULT_BACKEND, BASE_DIR

celery = Celery(
    "tasks",
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND
)

celery.conf.update(
    result_expires=3600,
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    broker_connection_retry_on_startup=True,
)


celery.autodiscover_tasks(["app.tasks"])