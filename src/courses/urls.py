from django.urls import path

from .views import ListCourse

app_name = 'courses'
urlpatterns = [
    path('', ListCourse.as_view(), name='course_list')
]