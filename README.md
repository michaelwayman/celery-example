# celery-example
Repo to show a friend how to easy-mode use celery for local dev


```shell
cd src
celery --app=tasks:app worker --loglevel=INFO -n docker@%h --concurrency=2
```

```shell
cd src
FLOWER_UNAUTHENTICATED_API=True celery --app=tasks:app flower
```

___


```shell
docker compose up
```
