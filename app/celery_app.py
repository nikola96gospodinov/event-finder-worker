from celery import Celery

from core.config import settings

celery_app = Celery(
    "event_finder_worker",
    broker=settings.UPSTASH_REDIS_REST_URL,
    backend=settings.UPSTASH_REDIS_REST_URL,
    include=["app.tasks"],
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    worker_prefetch_multiplier=1,
    worker_max_tasks_per_child=100,
    broker_connection_retry_on_startup=True,
)

if __name__ == "__main__":
    celery_app.start()
