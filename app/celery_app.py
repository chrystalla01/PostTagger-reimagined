import os
from celery import Celery

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")
celery_app = Celery("pi_tasks", broker=REDIS_URL, backend=REDIS_URL, include=["app.tasks"])
celery_app.conf.update(
    task_track_started=True,
    result_expires=3600,
    worker_hijack_root_logger=False,
)
