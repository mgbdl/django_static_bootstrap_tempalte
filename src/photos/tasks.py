from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect

from celery.schedules import crontab
from celery.decorators import periodic_task, task
from celery.utils.log import  get_task_logger

from photos.utils import save_latest_flickr_image
from photos.models import Photo

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute='*/15')),
    name="save_latest_flickr_image_task",
    ignore_result=True
)
def save_latest_flickr_image_task():
    """
    Saves latest image from Flickr
    """
    save_latest_flickr_image()
    logger.info("Saved image from Flickr")
