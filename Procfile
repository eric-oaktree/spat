web: gunicorn at3.wsgi --log-file -
worker: celery worker --app=tasks.app
worker: celery -A --app=tasks.app beat -l info -S django
