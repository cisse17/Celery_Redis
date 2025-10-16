import os

from celery import celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery.settings')

app = celery("celery")

app.conf.from_object("django.conf:settings", namespace="CELERY") # premier mot definit sur settings CELERY_BRONKER OU CELERY_BACKEND_...

@app.task
def add_numbers():
    return 