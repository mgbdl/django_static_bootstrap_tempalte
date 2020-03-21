from django.conf import settings
from django.db import models
from django.urls import reverse

from rest_framework.reverse import reverse as api_reverse
# Create your models here.


class BlogPost(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, null=True, blank=True)
    content = models.TextField(max_length=120, null=True, blank=True)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.user.name)

    @property
    def owner(self):
        return self.owner

    
    def get_api_url(self, request=None):
        return api_reverse("api_postings:post-rud", kwargs={'pk': self.pk}, request=request)