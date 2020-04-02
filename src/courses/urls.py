from django.urls import path

from .views import (
    ListCreateCourse, RetrieveUpdateDestroyCourse,
    ListCreateReview, RetrieveUpdateDestroyReview,
)

app_name = 'courses'
urlpatterns = [
    path('', ListCreateCourse.as_view(), name='course_list'),
    path('<int:pk>/', RetrieveUpdateDestroyCourse.as_view(), name='course_detail'),
    path('<int:course_pk>/reviews/', ListCreateReview.as_view(), name='review_list'),
    path('<int:course_pk>/reviews/<int:pk>/', RetrieveUpdateDestroyReview, name='review_detail'),
]