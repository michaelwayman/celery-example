# celery-example
Repo to show a friend how to easy-mode use celery for local dev


```shell
cd src
celery --app=tasks:app worker --loglevel=INFO -n docker@%h
```

___


```shell
docker compose up
```
