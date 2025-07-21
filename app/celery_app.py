from celery import Celery

from core.upstash_connection_link import get_upstash_redis_url

celery_app = Celery(
    "event_finder_worker",
    broker=get_upstash_redis_url(),
    backend=get_upstash_redis_url(),
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
