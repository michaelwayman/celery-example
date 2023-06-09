from celery.utils.log import get_task_logger

from celery_app import app

logger = get_task_logger(__name__)


@app.task(bind=True)
def task_1(self, text):
    logger.warning(text + " TASK 1")
    task_2.delay(text)


@app.task(bind=True)
def task_2(self, text):
    logger.warning(text + " TASK 2")
    task_3.delay(text)


@app.task(bind=True)
def task_3(self, text):
    logger.warning(text + " TASK 3")
