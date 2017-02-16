web: gunicorn at3.wsgi --log-file -
worker: celery --app=tasks.app beat -l info -S django
