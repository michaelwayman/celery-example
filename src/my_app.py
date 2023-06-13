import time
import tasks


def test_always_eager_localized():
    tasks.always_eager_then_sleep.delay(10)
    time.sleep(1)
    tasks.task_1.delay(3)
    tasks.sleep_task.delay(10)


if __name__ == "__main__":
    test_always_eager_localized()
