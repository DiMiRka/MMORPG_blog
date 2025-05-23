import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MMORPG_blog.settings')

app = Celery('MMORPG_blog')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_mails_every_monday_8am': {
        'task': 'board.tasks.send_mails',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
    },
}
