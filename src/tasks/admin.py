from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .tasks import send_emails_users

# Register your models here.
class AuthAdmin(UserAdmin):

    actions = ['send_emails_action',]

    def send_emai_action(self, request, queryset):
        send_emails_users.delay()
        updated_files = queryset.update(is_staff=True)

        return True

admin.site.unregister(User)
admin.site.register(User, AuthAdmin)
