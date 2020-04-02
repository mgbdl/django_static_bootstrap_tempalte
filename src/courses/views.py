from django.shortcuts import render
from django.shortcuts import get_object_or_404

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


class ListCreateReview(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # Gets multiple items
    def get_queryset(self):
        # Figure out how to get required queryset
        return self.queryset.filter(course_id=self.kwargs.get('course_pk'))

    def perform_create(self, serializer):
        # Tie result to a specific user email.
        course = get_object_or_404(
            Course, pk=self.kwargs.get('course_pk'))
        serializer.save(course=course)


class RetrieveUpdateDestroyReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # Gets a single item
    def get_object(self):
        return get_object_or_404(
            self.get_queryset(), 
            course_id=self.kwargs.get('course_pk'), 
            pk=self.kwargs.get('pk')
        )