from contextlib import contextmanager

from celery_app import app


@contextmanager
def make_sync():
    try:
        app.conf.task_always_eager = True
        app.conf.task_eager_propagates = True
        yield
    finally:
        app.conf.task_always_eager = False
        app.conf.task_eager_propagates = False
