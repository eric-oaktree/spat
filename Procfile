web: gunicorn at3.wsgi --log-file -
worker: celery -A at3 beat -l info -S django
