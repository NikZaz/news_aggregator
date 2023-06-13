from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Установка переменной окружения для настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_aggregator.settings')

# Создание экземпляра Celery
app = Celery('news_aggregator')

# Конфигурация Celery из настроек Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическое обнаружение задач в приложении
app.autodiscover_tasks()

# Настройка расписания задач
app.conf.beat_schedule = {
    'parse_content_every_1_hours': {
        'task': 'news.tasks.parse_content_task',
        'schedule': crontab(minute=0, hour='*/1'),
    },
    'parse_content_bbc_every_1_hours': {
        'task': 'news.tasks.parse_content_bbc_task',
        'schedule': crontab(minute=0, hour='*/1'),
    }
}
