from string import ascii_letters

import tasks
import random

from celery_app import app


def main():
    task_name = "".join(random.choices(ascii_letters, k=8))
    tasks.recursive_task.apply_async(args=[task_name])


if __name__ == "__main__":
    main()
