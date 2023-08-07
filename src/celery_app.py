import os
from celery import Celery

broker_url = os.getenv("CELERY_BROKER", "redis://0.0.0.0:6379/0")

celery_conf = {
    "task_protocol": 1,
    # "worker_cancel_long_running_tasks_on_connection_loss": True,
    "task_acks_late": True,
    # "task_reject_on_worker_lost": True,
    # "task_send_sent_event": True,
    # "worker_send_task_events": True,
    # "task_track_started": True,
    # "broker_transport_options": {'visibility_timeout': 10},
    # "broker_connection_timeout": 25,
    # "task_ignore_result": False,
    # "worker_prefetch_multiplier": 1,
}

app = Celery("tasks", broker=broker_url, broker_connection_retry_on_startup=True, backend=broker_url, **celery_conf)
