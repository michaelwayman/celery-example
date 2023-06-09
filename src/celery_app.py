import os
from celery import Celery

broker_url = os.getenv("CELERY_BROKER", "redis://0.0.0.0:6379/0")

app = Celery("tasks", broker=broker_url, broker_connection_retry_on_startup=True, backend=broker_url)
