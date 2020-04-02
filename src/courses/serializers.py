from rest_framework import serializers

from .models import Course, Review

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = (
            'id', 
            'title',
            'url',
        )

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = (
            'id', 
            'course',
            'email',
            'comment',
            'rating',
            'created_at',
        )
        extra_kwargs = {
            'email': {'write_only': True}
        }
        