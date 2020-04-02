from django.urls import path
from .views import BlogPostRudView, BlogPostAPIView

app_name='api-postings'

urlpatterns = [

    path('', BlogPostAPIView.as_view(), name='post-listcreate'),
    path('<int:pk>', BlogPostAPIView.as_view(), name='post-rud'),
    
]