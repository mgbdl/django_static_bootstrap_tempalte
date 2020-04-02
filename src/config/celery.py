from __future__ import absolute_import, unicode_literals

import os
from . import settings
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery('config')
# app = Celery('broker=CELERY_BROKER_URL')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS, force=True)
# app.autodiscover_tasks(force=True)

@app.task(bind=True)
def debug(self):
    print('Request: {0!r}'.format(self.request))