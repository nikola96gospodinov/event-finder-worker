from app.celery_app import celery_app


@celery_app.task
def example_task():
    return "Hello from Celery!"
