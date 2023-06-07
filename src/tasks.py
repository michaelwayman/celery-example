from celery.utils.log import get_task_logger

from celery_app import app

logger = get_task_logger(__name__)


@app.task
def tweet_me(text):
    print(text)
    logger.warning(text)  # in case above doesn't show
