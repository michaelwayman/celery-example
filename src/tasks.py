from time import sleep

from celery import shared_task, Task
from celery.utils.log import get_task_logger

from celery_app import app

logger = get_task_logger(__name__)


class BaseTask(Task):
    # store_errors_even_if_ignored = True
    # track_started = True
    # acks_late = True
    # ignore_result = False

    # def on_success(self, retval, task_id, args, kwargs):
    #     logger.warning(("on_success", retval, task_id, args, kwargs))
    #
    # def on_failure(self, exc, task_id, args, kwargs, einfo):
    #     logger.warning(("on_failure", exc, task_id, args, kwargs, einfo))
    #
    # def before_start(self, task_id, args, kwargs):
    #     logger.warning(("before_start", task_id, args, kwargs))
    #
    # def after_return(self, status, retval, task_id, args, kwargs, einfo):
    #     logger.warning(("after_return", status, retval, task_id, args, kwargs, einfo))
    #
    # def on_retry(self, exc, task_id, args, kwargs, einfo):
    #     logger.warning(("on_retry", exc, task_id, args, kwargs, einfo))
    ...


@shared_task(bind=True, base=BaseTask)
def recursive_task(self, name, count: int = 15):
    logger.warning(f"NAME: {name}, COUNT: {count}")
    sleep(1)
    if count > 0:
        recursive_task.apply_async(args=[name], kwargs={"count": count - 1})
