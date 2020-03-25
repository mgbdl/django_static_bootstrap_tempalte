from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from config import settings

@shared_task
def send_emails_users():
    asunto = 'Test message'
    message = 'Wellcome, this is a CELERY, RABBITMQ & DANGO test message'
    users = User.objects.all()
    for user in users:
        send_mail(asunto, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)