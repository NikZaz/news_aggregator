from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_aggregator.settings')

app = Celery('news_aggregator')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'parse_content_every_3_hours': {
        'task': 'news.tasks.parse_content_task',
        'schedule': crontab(minute=0, hour='*/1'),
    },
    'parse_content_bbc_every_3_hours': {
        'task': 'news.tasks.parse_content_bbc_task',
        'schedule': crontab(minute=0, hour='*/1'),
    }
}
