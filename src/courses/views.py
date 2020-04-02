from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .models import Course, Review
from .serializers import CourseSerializer, ReviewSerializer


class ListCreateCourse(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    

class RetrieveUpdateDestroyCourse(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer