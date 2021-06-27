from django.conf import settings
from celery import Celery

app = Celery('project', broker=settings.CELERY_BROKER_URL)
app.autodiscover_tasks()
