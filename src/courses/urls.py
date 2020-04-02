from django.urls import path

from .views import ListCreateCourse, RetrieveUpdateDestroyCourse

app_name = 'courses'
urlpatterns = [
    path('', ListCreateCourse.as_view(), name='course_list'),
    path('<int:pk>/', RetrieveUpdateDestroyCourse.as_view(), name='course_detail'),
]