from celery.utils.log import get_task_logger
import multiprocessing

from celery_app import app
from utils import make_sync

logger = get_task_logger(__name__)


@app.task(bind=True)
def task_1(self, throw=False):
    logger.warning(f"PID: {multiprocessing.current_process().pid}")
    logger.warning(f"app.conf.task_always_eager={app.conf.task_always_eager}")
    if throw:
        raise ValueError("Teehee")


@app.task(bind=True)
def always_eager_then_sleep(self, seconds):
    with make_sync():
        logger.warning(f"PID: {multiprocessing.current_process().pid}")
        logger.warning(f"app.conf.task_always_eager={app.conf.task_always_eager}")
        sleep_task.delay(seconds)
        try:
            task_1.delay(throw=True)
        except ValueError:
            logger.error("Errors propagate with always_eager")


@app.task(bind=True)
def sleep_task(self, seconds):
    logger.warning(f"PID: {multiprocessing.current_process().pid}")
    logger.warning(f"app.conf.task_always_eager={app.conf.task_always_eager}")
    import time
    time.sleep(seconds)
