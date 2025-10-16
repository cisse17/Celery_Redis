import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djcelery.settings')

app = Celery("djcelery")

# Charger la configuration depuis les settings Django
app.config_from_object("django.conf:settings", namespace="CELERY") # premier mot definit sur settings CELERY_BRONKER OU CELERY_BACKEND_...

@app.task
def add_numbers():
    return 

# Découverte automatique des tâches
app.autodiscover_tasks()